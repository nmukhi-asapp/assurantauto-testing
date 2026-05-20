#!/usr/bin/env python3
"""Analyze CallerIdentification conversations for the May 12 follow-up questions.

Q1: % of calls routed to ContractHolderIssues whose ANI matches the
    sellingDealerPhone on one of the returned contracts (i.e., caller is a dealer).
Q2: Calls where the same VIN appears on multiple contracts in the GLOW response.
Q3: Calls from callers not classified as contract holder / dealership / repair facility.
Q5: For contractHolder + repairFacility calls, fraction where the send_sms_to_phone
    round-trip latency exceeded 3 s.
"""
from __future__ import annotations

import glob
import json
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("/Users/nmukhi/work/code/generative-agent-optimization-mcp/sampled_convos/CallerIdentification")


def parse_ts(s: str) -> datetime:
    # Handles "2026-04-28T14:19:12.713000Z"
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def get_ani(actions: list[dict]) -> str | None:
    for a in actions:
        if a.get("type") == "function_response":
            fr = a["function_response"]
            if fr.get("request", {}).get("function_name") == "decrypt_variables":
                resp = fr.get("response") or {}
                if isinstance(resp, dict):
                    p = resp.get("PhoneNumber")
                    if p:
                        return str(p)
    return None


def get_contracts(actions: list[dict]) -> list[dict]:
    """Return the contract[] list from the first successful get_contract_and_claims_data_ivr."""
    for a in actions:
        if a.get("type") != "function_response":
            continue
        fr = a["function_response"]
        if fr.get("request", {}).get("function_name") != "get_contract_and_claims_data_ivr":
            continue
        resp = fr.get("response") or {}
        # response is wrapped: {"response": {"success": true, "contractClaims": {"contract": [...]}}}
        inner = resp.get("response", resp) if isinstance(resp, dict) else {}
        if not isinstance(inner, dict) or not inner.get("success"):
            continue
        cc = inner.get("contractClaims") or {}
        contracts = cc.get("contract") or []
        if isinstance(contracts, list):
            return contracts
    return []


def is_rf_response(actions: list[dict]) -> bool | None:
    for a in actions:
        if a.get("type") != "function_response":
            continue
        fr = a["function_response"]
        if fr.get("request", {}).get("function_name") == "is_repair_facility":
            resp = fr.get("response") or {}
            inner = resp.get("response", resp) if isinstance(resp, dict) else {}
            if isinstance(inner, dict):
                # Look for true-ish flag
                for k, v in inner.items():
                    if isinstance(v, bool):
                        return v
                    if isinstance(v, str) and v.lower() in ("true", "false"):
                        return v.lower() == "true"
            return None
    return None


def get_user_type(actions: list[dict]) -> str | None:
    """Last set_customer_type call wins."""
    last = None
    for a in actions:
        if a.get("type") == "function_request":
            fr = a.get("function_request", {})
            if fr.get("function_name") == "set_customer_type":
                last = fr.get("parameters", {}).get("user_type")
    return last


def entered_tasks(actions: list[dict]) -> list[str]:
    return [a.get("task_name") for a in actions if a.get("type") == "enter_task"]


def transcript(actions: list[dict]) -> list[tuple[str, str]]:
    out = []
    for a in actions:
        if a.get("type") == "message":
            m = a.get("message") or {}
            speaker = m.get("speaker") or m.get("sender") or a.get("source_system", "?")
            text = m.get("text") or m.get("content") or ""
            out.append((speaker, text))
    return out


def find_sms_latencies(actions: list[dict]) -> list[float]:
    """Return list of (response_ts - request_ts) seconds for send_sms_to_phone pairs."""
    reqs: dict[str, datetime] = {}
    lats: list[float] = []
    for a in actions:
        if a.get("type") == "function_request":
            fr = a.get("function_request", {})
            if fr.get("function_name") == "send_sms_to_phone":
                rid = fr.get("request_id")
                if rid:
                    reqs[rid] = parse_ts(a["timestamp"])
        elif a.get("type") == "function_response":
            fr = a.get("function_response", {})
            if fr.get("request", {}).get("function_name") == "send_sms_to_phone":
                rid = fr.get("request", {}).get("request_id")
                if rid and rid in reqs:
                    dt = (parse_ts(a["timestamp"]) - reqs[rid]).total_seconds()
                    lats.append(dt)
    return lats


def main() -> None:
    files = sorted(glob.glob(str(DATA_DIR / "*.json")))
    print(f"Conversations: {len(files)}")

    # Per-conversation records
    records = []
    for fp in files:
        with open(fp) as f:
            d = json.load(f)
        mi = d["model_input"]
        actions = mi["actions"]
        ext_id = mi.get("external_conversation_id") or os.path.basename(fp)
        rec = {
            "file": os.path.basename(fp),
            "ext_id": ext_id,
            "tasks": entered_tasks(actions),
            "ani": get_ani(actions),
            "contracts": get_contracts(actions),
            "is_rf": is_rf_response(actions),
            "user_type": get_user_type(actions),
            "sms_latencies": find_sms_latencies(actions),
            "transcript": transcript(actions),
        }
        records.append(rec)

    # ---- Q1 ----
    ch_calls = [r for r in records if "ContractHolderIssues" in r["tasks"]]
    q1_dealer_phone_in_contracts = []  # ANI matches sellingDealerPhone
    q1_eventually_dealer = []  # set_customer_type=dealership
    q1_multi_contract_disambig = []  # >1 contract returned, disambiguation likely
    for r in ch_calls:
        ani = r["ani"]
        contracts = r["contracts"]
        dealer_phones = [c.get("sellingDealerPhone") for c in contracts if c.get("sellingDealerPhone")]
        if ani and ani in dealer_phones:
            q1_dealer_phone_in_contracts.append(r)
        if r["user_type"] == "dealership":
            q1_eventually_dealer.append(r)
        if len(contracts) > 1:
            q1_multi_contract_disambig.append(r)

    # Search transcripts for dealer-revealing language
    def dealer_revealing(r) -> bool:
        for speaker, text in r["transcript"]:
            t = (text or "").lower()
            if "i'm a dealer" in t or "im a dealer" in t or "i am a dealer" in t:
                return True
            if "from the dealership" in t or "calling from" in t and "dealer" in t:
                return True
            if "none of those" in t and any(w in t for w in ("car", "vehicle", "vin")):
                return True
            if "not any of those" in t:
                return True
        return False

    q1_transcript_reveals_dealer = [r for r in ch_calls if dealer_revealing(r)]

    print()
    print("=== Q1: Dealer phone numbers routed to ContractHolderIssues ===")
    print(f"Total CH-routed calls: {len(ch_calls)}")
    print(f"  ANI matches sellingDealerPhone of returned contract: {len(q1_dealer_phone_in_contracts)} ({100*len(q1_dealer_phone_in_contracts)/max(1,len(ch_calls)):.1f}%)")
    print(f"  Bot later set user_type=dealership (despite CH routing): {len(q1_eventually_dealer)}")
    print(f"  Multi-contract disambiguation needed (>1 contract returned): {len(q1_multi_contract_disambig)} ({100*len(q1_multi_contract_disambig)/max(1,len(ch_calls)):.1f}%)")
    print(f"  Transcript reveals dealer language: {len(q1_transcript_reveals_dealer)}")

    union = set()
    for grp in (q1_dealer_phone_in_contracts, q1_eventually_dealer, q1_transcript_reveals_dealer):
        for r in grp:
            union.add(r["ext_id"])
    print(f"  Union (any dealer signal): {len(union)} ({100*len(union)/max(1,len(ch_calls)):.1f}%)")

    print("\nExamples of ANI==sellingDealerPhone:")
    for r in q1_dealer_phone_in_contracts[:5]:
        dphones = sorted({c.get("sellingDealerPhone") for c in r["contracts"]})
        dnames = sorted({c.get("sellingDealerName") for c in r["contracts"]})
        print(f"  {r['ext_id']} ANI={r['ani']} contracts={len(r['contracts'])} dealerPhones={dphones} dealerNames={dnames[:2]}")

    # ---- Q2 ----
    print()
    print("=== Q2: Same VIN, multiple contracts ===")
    q2_hits = []
    for r in records:
        vins = defaultdict(list)
        for c in r["contracts"]:
            v = c.get("VIN")
            if v:
                vins[v].append(c)
        multi = {v: cs for v, cs in vins.items() if len(cs) > 1}
        if multi:
            q2_hits.append((r, multi))
    print(f"Calls with at least one VIN appearing on multiple contracts: {len(q2_hits)} of {len(records)}")
    for r, multi in q2_hits[:10]:
        for v, cs in multi.items():
            names = [(c.get("customerFirstName"), c.get("customerLastName"), c.get("status"), c.get("productName")) for c in cs]
            print(f"  {r['ext_id']} VIN={v} ({len(cs)} contracts) -> {names}")

    # ---- Q3 ----
    print()
    print("=== Q3: Callers not CH / dealer / repair facility ===")
    classified = {"contractHolder", "dealership", "repairFacility"}
    q3_other = [r for r in records if r["user_type"] == "other"]
    q3_unclassified = [r for r in records if r["user_type"] is None]
    q3_total = q3_other + q3_unclassified
    print(f"  user_type=other: {len(q3_other)}")
    print(f"  set_customer_type never called: {len(q3_unclassified)}")
    print(f"  Total non-CH/Dealer/RF: {len(q3_total)} of {len(records)} ({100*len(q3_total)/len(records):.1f}%)")
    print(f"  (Strict, user_type=='other' only): {len(q3_other)} ({100*len(q3_other)/len(records):.1f}%)")

    # Show what happened to unclassified
    print("\nUnclassified examples (no set_customer_type):")
    for r in q3_unclassified[:10]:
        # Count messages
        n_msgs = len(r["transcript"])
        print(f"  {r['ext_id']} tasks={r['tasks']} msgs={n_msgs}")
    print("\nuser_type=other examples:")
    for r in q3_other:
        n_msgs = len(r["transcript"])
        print(f"  {r['ext_id']} tasks={r['tasks']} msgs={n_msgs}")

    # ---- Q5 ----
    print()
    print("=== Q5: SMS latency >3s for CH/RF calls ===")
    chrf_calls = [r for r in records if r["user_type"] in ("contractHolder", "repairFacility")]
    chrf_with_sms = [r for r in chrf_calls if r["sms_latencies"]]
    over_3s = [r for r in chrf_with_sms if any(l > 3.0 for l in r["sms_latencies"])]
    all_lats = [l for r in chrf_with_sms for l in r["sms_latencies"]]
    over_3s_lats = [l for l in all_lats if l > 3.0]
    print(f"  CH/RF calls: {len(chrf_calls)}")
    print(f"  CH/RF calls with at least one send_sms_to_phone API call: {len(chrf_with_sms)}")
    print(f"  CH/RF calls where any send_sms >3s: {len(over_3s)} ({100*len(over_3s)/max(1,len(chrf_with_sms)):.1f}% of those with SMS)")
    print(f"  Per-call API-call basis: {len(over_3s_lats)} / {len(all_lats)} = {100*len(over_3s_lats)/max(1,len(all_lats)):.1f}%")
    if all_lats:
        all_lats_s = sorted(all_lats)
        p50 = all_lats_s[len(all_lats_s)//2]
        p90 = all_lats_s[int(len(all_lats_s)*0.9)] if len(all_lats_s) >= 10 else all_lats_s[-1]
        p99 = all_lats_s[int(len(all_lats_s)*0.99)] if len(all_lats_s) >= 100 else all_lats_s[-1]
        print(f"  Latency p50={p50:.2f}s p90={p90:.2f}s p99={p99:.2f}s max={max(all_lats):.2f}s")
    print("\n  Examples >3s:")
    for r in over_3s[:10]:
        slow = [l for l in r["sms_latencies"] if l > 3.0]
        print(f"    {r['ext_id']} user={r['user_type']} latencies={[f'{l:.2f}s' for l in r['sms_latencies']]}")


if __name__ == "__main__":
    main()
