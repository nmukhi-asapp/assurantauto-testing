#!/usr/bin/env python3
"""
Generate an HTML report for an assurantauto scenario run.

Usage:
    python generate_report.py <run_dir> [--output report.html] [--scenarios-dir ...]

Example:
    python generate_report.py \
        scenario-runs/assurantauto/e2e_full_20260423 \
        --output reports/assurantauto_e2e_full_20260423_report.html
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml

# Add time inspector to path
# Override with TIME_INSPECTOR_DIR env var if repos are not siblings of this repo
_default_time_inspector = Path(__file__).resolve().parent.parent / "generative-agent-time-inspector"
TIME_INSPECTOR_DIR = Path(os.environ.get("TIME_INSPECTOR_DIR", str(_default_time_inspector)))
sys.path.insert(0, str(TIME_INSPECTOR_DIR))

try:
    from analyze import (
        analyze_span, TurnSpan, Activity,
        AT_DEAD_AIR, AT_BOT_SPEAKING, AT_TALKER_LLM,
        parse_ts, ts_diff_ms,
        ACTIVITY_HEX, ROW_ORDER, ROW_SHORT_LABEL, ACTIVITY_CONFIG, fmt_ms,
    )
    try:
        from analyze import AT_CUSTOMER
    except ImportError:
        from analyze import AT_CUSTOMER_SPEECH as AT_CUSTOMER  # renamed in newer versions
    PLOTLY_AVAILABLE = True
    try:
        import plotly.graph_objects as go
    except ImportError:
        PLOTLY_AVAILABLE = False
except ImportError as e:
    print(f"Warning: time inspector not available: {e}", file=sys.stderr)
    PLOTLY_AVAILABLE = False

SCENARIOS_BASE = Path(__file__).parent / "scenarios/E2E"
EXCESSIVE_DEAD_AIR_MS = 5000
WPM = 130  # assumed speaking rate for bot TTS duration estimate


# ─── Data loading ─────────────────────────────────────────────────────────────

def find_scenario_yaml(scenario_id: str, base_dir: Path) -> Optional[Path]:
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if not f.endswith(".yaml"):
                continue
            path = Path(root) / f
            try:
                with open(path) as fh:
                    d = yaml.safe_load(fh)
                if d and d.get("id") == scenario_id:
                    return path
            except Exception:
                pass
    return None


def load_run(run_dir: Path, scenarios_base: Path) -> dict:
    """Load a run directory, scanning for scenario subdirs (doesn't require summary.json)."""
    run_dir = Path(run_dir)

    dirname = run_dir.name
    branch = "unknown"
    for b in ("sandbox", "main", "prod", "draft"):
        if b in dirname:
            branch = b
            break

    # Scan for all scenario result directories matching {sid}-run_{n}
    import re as _re
    scenario_dirs = sorted(
        [d for d in run_dir.iterdir()
         if d.is_dir() and _re.match(r'.+-run_\d+$', d.name)],
        key=lambda d: d.name,
    )

    scenarios = {}
    for scenario_dir in scenario_dirs:
        # Parse sid and run_index from dir name
        m = _re.match(r'^(.+)-run_(\d+)$', scenario_dir.name)
        if not m:
            continue
        sid = m.group(1)

        results_path = scenario_dir / "results.json"
        if not results_path.exists():
            continue
        results = json.loads(results_path.read_text())

        state_path = scenario_dir / "state.json"
        state = json.loads(state_path.read_text()) if state_path.exists() else None

        yaml_path = find_scenario_yaml(sid, scenarios_base)
        yaml_data = None
        if yaml_path:
            with open(yaml_path) as f:
                yaml_data = yaml.safe_load(f)

        tasks = []
        if state:
            seen = set()
            for a in state.get("actions", []):
                if a.get("type") == "enter_task":
                    tn = a.get("task_name", "")
                    if tn and tn not in seen:
                        seen.add(tn)
                        tasks.append(tn)

        run_ts = None
        if state:
            actions = state.get("actions", [])
            if actions:
                run_ts = actions[0].get("timestamp", "")

        scenarios[sid] = {
            "scenario_id": sid,
            "results": results,
            "state": state,
            "yaml_data": yaml_data,
            "tasks": tasks,
            "run_ts": run_ts,
        }

    # Build aggregate summary from scanned results (no dependency on summary.json)
    total_cost = sum(sc["results"].get("total_cost", 0) for sc in scenarios.values())
    passed = failed = 0
    for sc in scenarios.values():
        for er in sc["results"].get("evaluation_results", []):
            if not er.get("applicable", True) or er.get("passed") is None:
                continue
            p = er["passed"]
            if (all(p) if isinstance(p, list) else p):
                passed += 1
            else:
                failed += 1
    total_evals = passed + failed
    summary = {
        "total_cost": total_cost,
        "passed": passed,
        "failed": failed,
        "total": total_evals,
        "total_passrate": passed / total_evals if total_evals > 0 else 0,
        "results": list(scenarios.values()),
    }

    return {
        "run_dir": str(run_dir),
        "run_name": run_dir.name,
        "branch": branch,
        "summary": summary,
        "scenarios": scenarios,
    }


# ─── Conversation analysis ────────────────────────────────────────────────────

def _dedupe_text(text: str) -> str:
    """Remove doubled-text echo artifact from TR voice simulation."""
    text = text.strip()
    if len(text) > 20:
        mid = len(text) // 2
        first_half = text[:mid].strip()
        second_half = text[mid:].strip()
        if second_half.startswith(first_half[:20]):
            return first_half
    return text


def _speaking_ms(text: str) -> float:
    """Estimate TTS speaking duration from word count."""
    words = len(text.split()) if text else 1
    return max(500.0, (words / WPM) * 60_000)


def get_bot_messages_in_span(actions: list, span_start: datetime, span_end: datetime) -> list:
    """Return voice_assistant/bot messages within [span_start, span_end)."""
    s = span_start.isoformat()
    e = span_end.isoformat()
    return [
        a for a in actions
        if a.get("type") == "message"
        and a.get("source_system") == "voice_assistant"
        and a.get("message", {}).get("sender") == "bot"
        and s <= a.get("timestamp", "") < e
    ]


def build_corrected_dead_air_and_bot_speaking(
    span: TurnSpan, actions: list
) -> "tuple[list, list]":
    """
    Return (bot_speaking_activities, dead_air_activities) computed correctly.

    Bot speaking: one Activity per bot message, duration estimated from word count.
    Dead air: silence AFTER a bot message finishes speaking until the NEXT bot
              message starts. Dead air does NOT overlap with bot speaking.
    """
    bot_msgs = get_bot_messages_in_span(actions, span.span_start, span.span_end)
    span_start = span.span_start

    bot_speaking = []
    dead_air = []

    for i, msg in enumerate(bot_msgs):
        msg_ts = parse_ts(msg["timestamp"])
        text = (msg.get("message") or {}).get("text", "")
        start_ms = ts_diff_ms(span_start, msg_ts)
        end_ms = start_ms + _speaking_ms(text)

        # Cap speaking end at span duration to avoid overrun
        span_duration_ms = ts_diff_ms(span.span_start, span.span_end)
        end_ms = min(end_ms, span_duration_ms)

        bot_speaking.append(Activity(
            activity_type=AT_BOT_SPEAKING,
            start_ms=start_ms,
            end_ms=end_ms,
            details={"bot_messages": [text], "note": ""},
        ))

        if i + 1 < len(bot_msgs):
            next_ts = parse_ts(bot_msgs[i + 1]["timestamp"])
            next_start_ms = ts_diff_ms(span_start, next_ts)
            silence_ms = next_start_ms - end_ms
            if silence_ms >= 800:  # perceptible silence
                next_text = (bot_msgs[i + 1].get("message") or {}).get("text", "")
                dead_air.append(Activity(
                    activity_type=AT_DEAD_AIR,
                    start_ms=end_ms,
                    end_ms=next_start_ms,
                    details={
                        "gap_between": [text[:80], next_text[:80]],
                        "running_activities": [],
                    },
                ))

    return bot_speaking, dead_air


def get_conversation_spans(state: dict) -> list:
    """Return TurnSpan list from state, with corrected dead air and bot speaking."""
    if not PLOTLY_AVAILABLE:
        return []

    raw_actions = state.get("actions", [])
    actions = sorted(raw_actions, key=lambda a: a.get("timestamp", ""))

    # Filter real customer turns (>3s gap from previous)
    all_customer = [
        a for a in actions
        if a.get("type") == "message"
        and a.get("source_system") == "customer"
        and a.get("message", {}).get("sender") == "customer"
    ]
    real_customer_turns = []
    for msg in all_customer:
        if not real_customer_turns:
            real_customer_turns.append(msg)
        else:
            gap_ms = ts_diff_ms(
                parse_ts(real_customer_turns[-1]["timestamp"]),
                parse_ts(msg["timestamp"]),
            )
            if gap_ms > 3000:
                real_customer_turns.append(msg)

    if not real_customer_turns:
        return []

    spans = []
    for i, turn in enumerate(real_customer_turns):
        span_start = parse_ts(turn["timestamp"])
        is_last = i + 1 >= len(real_customer_turns)
        span_end = (
            parse_ts(actions[-1]["timestamp"])
            if is_last
            else parse_ts(real_customer_turns[i + 1]["timestamp"])
        )

        span_start_str = span_start.isoformat()
        span_end_str = span_end.isoformat()
        actions_in_span = [
            a for a in actions
            if span_start_str <= a.get("timestamp", "") < span_end_str
        ]

        has_reasoner = any(
            a.get("type") == "llm_request"
            and "reasoner" in a.get("llm_request", {}).get("prompt_type", "")
            for a in actions_in_span
        )

        # Get LLM/API/etc activities from time inspector (simulation_mode=False
        # so it finds voice_assistant bot messages correctly), then replace
        # bot_speaking and dead_air with our corrected versions.
        raw_activities = analyze_span(
            span_start, span_end, actions_in_span
        )
        # Strip time inspector's bot_speaking and dead_air (they overlap)
        activities = [
            a for a in raw_activities
            if a.activity_type not in (AT_BOT_SPEAKING, AT_DEAD_AIR, AT_TALKER_LLM)
        ]

        # Add corrected bot_speaking and dead_air
        bot_speaking, dead_air = build_corrected_dead_air_and_bot_speaking(
            TurnSpan(
                turn_index=i,
                customer_text="",
                span_start=span_start,
                span_end=span_end,
                is_last_span=is_last,
                has_reasoner=has_reasoner,
            ),
            actions,
        )
        # Compute customer speaking duration, then apply a single uniform shift to
        # all non-customer activities so that the first one starts exactly at
        # speaking_ms (i.e. right after the customer finishes). Using one global
        # offset preserves relative timing between all non-customer activities
        # (LLM calls, bot speaking, dead air) so they never overlap each other.
        customer_text = _dedupe_text(turn.get("message", {}).get("text", ""))
        word_count = len(customer_text.split()) if customer_text else 1
        speaking_ms = max(500.0, (word_count / WPM) * 60_000)

        all_non_customer = activities + bot_speaking + dead_air
        if all_non_customer:
            earliest_start = min(a.start_ms for a in all_non_customer)
            global_shift = max(0.0, speaking_ms - earliest_start)
        else:
            global_shift = 0.0

        def _apply_shift(act: Activity) -> Activity:
            if global_shift == 0.0:
                return act
            return Activity(
                activity_type=act.activity_type,
                start_ms=act.start_ms + global_shift,
                end_ms=act.end_ms + global_shift,
                details=act.details,
            )

        activities = [_apply_shift(a) for a in activities]
        activities.extend(_apply_shift(a) for a in bot_speaking)
        activities.extend(_apply_shift(a) for a in dead_air)

        # Prepend customer utterance at position 0
        activities.insert(0, Activity(
            activity_type=AT_CUSTOMER,
            start_ms=0,
            end_ms=speaking_ms,
            details={"text": customer_text},
        ))

        activities.sort(key=lambda a: a.start_ms)

        spans.append(TurnSpan(
            turn_index=i,
            customer_text=customer_text,
            span_start=span_start,
            span_end=span_end,
            is_last_span=is_last,
            has_reasoner=has_reasoner,
            activities=activities,
        ))

    return spans


def count_excessive_dead_air(spans: list) -> list:
    """Return list of dead_air activities with duration >= EXCESSIVE_DEAD_AIR_MS."""
    return [
        {
            "turn": span.turn_index + 1,
            "duration_ms": act.duration_ms,
            "customer_text": span.customer_text,
            "details": act.details,
        }
        for span in spans
        for act in span.activities
        if act.activity_type == AT_DEAD_AIR and act.duration_ms >= EXCESSIVE_DEAD_AIR_MS
    ]


def extract_transcript(state: dict) -> list:
    """Extract chronological transcript from state dict."""
    actions = sorted(state.get("actions", []), key=lambda a: a.get("timestamp", ""))

    # Find start time
    first_msg = next(
        (a for a in actions
         if a.get("type") == "message"
         and a.get("source_system") in ("voice_assistant", "customer")
         and a.get("message", {}).get("sender") in ("bot", "customer")),
        None,
    )
    if not first_msg:
        return []
    start_ts = parse_ts(first_msg["timestamp"])

    # The talker's internal paraphrase (e.g. "Caller identified themselves as…") is
    # always the customer/customer message immediately after send_customer_request_or_update.
    # Build a set of those IDs to exclude from the transcript.
    summary_ids = set()
    for idx, a in enumerate(actions):
        if (a.get("type") == "function_request"
                and (a.get("function_request") or {}).get("function_name") == "send_customer_request_or_update"):
            # Walk forwards to find the next customer message
            for nxt in actions[idx + 1:]:
                if nxt.get("type") == "message_audio_completed":
                    continue
                if (nxt.get("type") == "message"
                        and nxt.get("source_system") == "customer"
                        and nxt.get("message", {}).get("sender") == "customer"):
                    summary_ids.add(nxt.get("id"))
                break

    transcript = []
    seen_bot_texts = set()

    for a in actions:
        if a.get("type") != "message":
            continue
        src = a.get("source_system", "")
        msg = a.get("message", {})
        sender = msg.get("sender", "")
        text = msg.get("text", "").strip()
        if not text:
            continue

        ts = parse_ts(a["timestamp"])
        offset_s = (ts - start_ts).total_seconds()
        time_str = f"{int(offset_s // 60)}:{int(offset_s % 60):02d}"

        if src == "voice_assistant" and sender == "bot":
            key = text[:100]
            if key in seen_bot_texts:
                continue
            seen_bot_texts.add(key)
            transcript.append({"time": time_str, "speaker": "agent", "text": text})

        elif sender == "customer" and a.get("id") not in summary_ids:
            # Real customer speech (works for both prod voice_assistant/customer
            # and scenario-runner customer/customer messages)
            transcript.append({"time": time_str, "speaker": "customer",
                                "text": _dedupe_text(text)})

    # Merge consecutive agent turns (filler + response sent before customer replies)
    merged = []
    for entry in transcript:
        if merged and entry["speaker"] == "agent" and merged[-1]["speaker"] == "agent":
            merged[-1]["text"] += " " + entry["text"]
        else:
            merged.append(entry)
    return merged


# ─── Plotly timeline ──────────────────────────────────────────────────────────

def _activity_hover_custom(act: Activity, turn_index: int) -> str:
    """Custom hover tooltip, including AT_CUSTOMER text."""
    d = act.details
    at = act.activity_type
    cfg = ACTIVITY_CONFIG.get(at, {"label": at})
    label = cfg["label"]

    lines = [
        f"<b>Turn {turn_index + 1} — {label}</b>",
        f"Start: {fmt_ms(act.start_ms)} &nbsp; End: {fmt_ms(act.end_ms)} &nbsp; Duration: <b>{fmt_ms(act.duration_ms)}</b>",
        "─" * 30,
    ]

    if at == AT_CUSTOMER:
        text = d.get("text", "")
        lines.append(f"<b>Customer said:</b>")
        # Word-wrap at ~80 chars
        words = text.split()
        line_buf, wrapped = [], []
        for w in words:
            line_buf.append(w)
            if len(" ".join(line_buf)) > 80:
                wrapped.append(" ".join(line_buf))
                line_buf = []
        if line_buf:
            wrapped.append(" ".join(line_buf))
        for wl in wrapped[:6]:
            lines.append(f"  {wl}")
        if len(wrapped) > 6:
            lines.append(f"  <i>…</i>")

    elif at == AT_DEAD_AIR:
        gap = d.get("gap_between", ["", ""])
        lines.append(f'After: <i>"{gap[0]}"</i>')
        lines.append(f'Before: <i>"{gap[1]}"</i>')
        running = d.get("running_activities", [])
        if running:
            lines.append("<b>Cause (running during silence):</b>")
            for r in running:
                lines.append(f"  • {r}")
        else:
            lines.append("<i>Agent processing / LLM inference</i>")

    elif at == AT_BOT_SPEAKING:
        msgs = d.get("bot_messages", [])
        if msgs:
            for msg in msgs[:2]:
                short = msg[:120]
                lines.append(f'<i>"{short}{"…" if len(msg) > 120 else ""}"</i>')
        lines.append("<i>(duration estimated from word count)</i>")

    elif at in ("reasoner_llm", "task_selector_llm", "other_llm"):
        lines.append(f"<b>Model:</b> {d.get('model', '?')}")
        lines.append(f"<b>Prompt type:</b> {d.get('prompt_type', '?')}")
        lines.append(f"<b>Tokens:</b> {d.get('input_tokens', '?')} in → {d.get('output_tokens', '?')} out")
        if d.get("cost_usd"):
            lines.append(f"<b>Cost:</b> ${d['cost_usd']:.5f}")
        thought = d.get("thought", "")
        if thought:
            lines.append("─" * 30)
            lines.append("<b>Thought:</b>")
            words = thought.split()
            line_buf, chunk_lines = [], []
            for w in words:
                line_buf.append(w)
                if len(" ".join(line_buf)) > 90:
                    chunk_lines.append(" ".join(line_buf))
                    line_buf = []
            if line_buf:
                chunk_lines.append(" ".join(line_buf))
            for cl in chunk_lines[:8]:
                lines.append(f"  {cl}")
            if len(chunk_lines) > 8:
                lines.append(f"  <i>… ({len(chunk_lines) - 8} more lines)</i>")

    elif at in ("api_call", "utility_call", "system_call"):
        lines.append(f"<b>Function:</b> {d.get('function_name', '?')}")
        success = d.get("success")
        lines.append(f"<b>Success:</b> {'✓' if success else ('✗' if success is False else '?')}")
        if d.get("parameters_preview"):
            p = d["parameters_preview"][:200]
            lines.append(f"<b>Input:</b> {p}{'…' if len(d['parameters_preview']) > 200 else ''}")
        if d.get("response_preview"):
            r = d["response_preview"][:200]
            lines.append(f"<b>Output:</b> {r}{'…' if len(d['response_preview']) > 200 else ''}")
        if d.get("error"):
            lines.append(f"<b>Error:</b> {d['error']}")

    return "<br>".join(lines)


def build_timeline_div(conv_meta: dict, spans: list, title: str) -> str:
    if not PLOTLY_AVAILABLE or not spans:
        return "<p class='no-data'>Timeline not available.</p>"

    def row_key(n: int, at: str) -> str:
        return f"T{n+1}\u200b{at}"

    span_active = [{a.activity_type for a in s.activities} for s in spans]

    categoryarray = []
    categorymap = {}
    for span in reversed(spans):
        n = span.turn_index
        active = span_active[n]
        sep_key = f"_sep_T{n+1}"
        categoryarray.append(sep_key)
        categorymap[sep_key] = f"── Turn {n+1} ──"
        for at in reversed(ROW_ORDER):
            if at in active:
                k = row_key(n, at)
                categoryarray.append(k)
                categorymap[k] = f"T{n+1} · {ROW_SHORT_LABEL.get(at, at)}"

    fig = go.Figure()
    seen_types: set = set()

    for span in spans:
        n = span.turn_index
        total_ms = span.total_duration_ms
        for act in span.activities:
            at = act.activity_type
            cfg = ACTIVITY_CONFIG.get(at, {"label": at})
            color = ACTIVITY_HEX.get(at, "#888888")
            show_legend = at not in seen_types
            seen_types.add(at)

            duration = act.end_ms - act.start_ms
            hover = _activity_hover_custom(act, n)

            if at == AT_CUSTOMER:
                utterance = act.details.get("text", "")
                bar_text = f'"{utterance[:60]}{"…" if len(utterance) > 60 else ""}"'
                opacity = 0.35
            else:
                bar_text = cfg["label"] if duration > total_ms * 0.06 else ""
                opacity = 0.90

            fig.add_trace(go.Bar(
                name=cfg["label"],
                x=[duration],
                base=[act.start_ms],
                y=[row_key(n, at)],
                orientation="h",
                marker_color=color,
                marker_line_width=0.5,
                marker_line_color="rgba(0,0,0,0.2)",
                opacity=opacity,
                hovertemplate=hover + "<extra></extra>",
                legendgroup=at,
                showlegend=show_legend,
                text=bar_text,
                textposition="inside",
                insidetextanchor="start",
                textfont=dict(size=10, color="white"),
            ))

    shapes = []
    for span in spans:
        n = span.turn_index
        sep_key = f"_sep_T{n+1}"
        shapes.append(dict(
            type="line", xref="paper", yref="y",
            x0=0, x1=1, y0=sep_key, y1=sep_key,
            line=dict(color="#bbb", width=1, dash="dot"),
        ))

    n_rows = len(categoryarray)
    chart_height = max(500, n_rows * 26 + 180)

    fig.update_layout(
        title=dict(text=f"<b>{title}</b>", x=0.01, font=dict(size=13, color="#333")),
        barmode="overlay",
        height=chart_height,
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="#ffffff",
        font=dict(color="#333", size=11),
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0,
            bgcolor="rgba(255,255,255,0.9)", bordercolor="#ddd", borderwidth=1,
        ),
        hovermode="closest",
        hoverlabel=dict(bgcolor="#fff", bordercolor="#ccc", font_size=12,
                        font_family="monospace", namelength=-1,
                        font=dict(color="#333")),
        margin=dict(l=160, r=20, t=90, b=50),
        shapes=shapes,
        xaxis=dict(title="ms from turn start", gridcolor="#e5e7eb",
                   zerolinecolor="#ccc", tickformat=",", color="#555"),
        yaxis=dict(
            categoryorder="array", categoryarray=categoryarray,
            tickvals=list(categorymap.keys()), ticktext=list(categorymap.values()),
            tickfont=dict(size=10, color="#555"), gridcolor="#e5e7eb",
        ),
    )

    return fig.to_html(full_html=False, include_plotlyjs=False)


# ─── Mock data summary ────────────────────────────────────────────────────────

def _mock_summary(yaml_data: dict) -> str:
    if not yaml_data:
        return "<em>No scenario data available.</em>"
    lines = []
    mock_responses = (yaml_data.get("mock_user") or {}).get("mock_responses") or {}
    for fn_name, responses in mock_responses.items():
        if not responses:
            continue
        first = responses[0].get("response", {})
        summary = _summarize_response(fn_name, first)
        lines.append(f"<div class='mock-fn'><span class='fn-name'>{fn_name}</span> → {summary}</div>")
    return "\n".join(lines) if lines else "<em>No mock responses defined.</em>"


def _summarize_response(fn_name: str, response: dict) -> str:
    try:
        if fn_name == "get_contract_and_claims_data_ivr":
            inner = response.get("response", {}).get("contractClaims", {})
            contracts = inner.get("contract", [])
            parts = []
            for c in contracts[:1]:
                name = f"{c.get('customerFirstName','')} {c.get('customerLastName','')}"
                claims = c.get("claims", [])
                claim_parts = [f"claim #{cl.get('claimNumber','?')} ({cl.get('status','?')})"
                               for cl in claims[:2]]
                parts.append(
                    f"Contract {c.get('contractNumber','?')} — {name.strip()}, "
                    f"{c.get('status','?')}; {', '.join(claim_parts) or 'no claims'}"
                )
            return "; ".join(parts) if parts else json.dumps(response)[:120]
        elif fn_name == "is_repair_facility":
            value = response.get('repairFacilityOrSellingDealer', response.get('isRepairFacility'))
            return f"repairFacilityOrSellingDealer={value}"
        elif fn_name == "escalate_to_agent_from_ivr":
            return f"success={response.get('success')}, TransferReason={response.get('TransferReason','?')}"
        elif fn_name == "decrypt_variables":
            return f"PhoneNumber={response.get('PhoneNumber','?')}"
        else:
            s = json.dumps(response, default=str)
            return s[:120] + ("…" if len(s) > 120 else "")
    except Exception:
        return str(response)[:120]


# ─── Eval results ─────────────────────────────────────────────────────────────

def get_eval_rows(results: dict) -> list:
    rows = []
    for er in results.get("evaluation_results", []):
        applicable = er.get("applicable", True)
        passed = er.get("passed")
        rules = er.get("evaluation", {}).get("rules", [])
        applicability = er.get("evaluation", {}).get("applicability")
        for rule in rules:
            if not applicable or passed is None:
                status = "n/a"
            elif isinstance(passed, list):
                status = "pass" if all(passed) else "fail"
            else:
                status = "pass" if passed else "fail"
            rows.append({"rule": rule, "status": status, "applicability": applicability})
    return rows


def scenario_pass_rate(results: dict) -> tuple:
    passed = total = 0
    for er in results.get("evaluation_results", []):
        if not er.get("applicable", True):
            continue
        p = er.get("passed")
        if p is None:
            continue
        total += 1
        passed += 1 if (all(p) if isinstance(p, list) else p) else 0
    return passed, total


# ─── HTML rendering ───────────────────────────────────────────────────────────

STATUS_ICON = {
    "pass": '<span class="badge pass">✓ Pass</span>',
    "fail": '<span class="badge fail">✗ Fail</span>',
    "n/a": '<span class="badge na">— N/A</span>',
}


def render_eval_table(rows: list, label: str) -> str:
    html = f"""
    <table class="eval-table">
      <thead>
        <tr>
          <th class="rule-col">Evaluation Rule</th>
          <th class="status-col">{label}</th>
        </tr>
      </thead>
      <tbody>"""
    for r in rows:
        app = r.get("applicability")
        app_note = ""
        if app:
            app_list = app if isinstance(app, list) else [app]
            app_note = f'<div class="applicability">Applies when: {"; ".join(app_list)}</div>'
        html += f"""
        <tr>
          <td class="rule-text">{r['rule']}{app_note}</td>
          <td class="status-cell">{STATUS_ICON.get(r['status'], r['status'])}</td>
        </tr>"""
    html += "\n      </tbody>\n    </table>"
    return html


def render_dead_air_section(excessive: list) -> str:
    if not excessive:
        return "<em class='ok'>No excessive dead air periods (≥ 5 seconds)</em>"
    items = "".join(
        f'<li><strong>{e["duration_ms"]/1000:.1f}s</strong> after turn {e["turn"]}: '
        f'<em>"{e["customer_text"][:80]}"</em></li>'
        for e in excessive
    )
    return f"<ul class='dead-air-list'>{items}</ul>"


def render_transcript(transcript: list) -> str:
    if not transcript:
        return "<em>No transcript available.</em>"
    html = '<div class="transcript">'
    for entry in transcript:
        cls = "agent-line" if entry["speaker"] == "agent" else "customer-line"
        lbl = "Agent" if entry["speaker"] == "agent" else "Customer"
        text = entry["text"].replace("<", "&lt;").replace(">", "&gt;")
        html += f"""
        <div class="transcript-line {cls}">
          <span class="ts">{entry['time']}</span>
          <span class="speaker">{lbl}</span>
          <span class="text">{text}</span>
        </div>"""
    html += "</div>"
    return html


# ─── Full HTML report ─────────────────────────────────────────────────────────

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
       background: #f5f6f7; color: #24292e; display: flex; min-height: 100vh; }
a { color: #0366d6; text-decoration: none; }
a:hover { text-decoration: underline; }

/* Sidebar */
#sidebar { width: 260px; min-width: 220px; background: #fff; border-right: 1px solid #e1e4e8;
           padding: 16px 0; position: fixed; top: 0; left: 0; height: 100vh;
           overflow-y: auto; z-index: 100; }
#sidebar-header { padding: 0 16px 12px; border-bottom: 1px solid #e1e4e8; margin-bottom: 8px; }
#sidebar-header h1 { font-size: 15px; font-weight: 600; color: #24292e; }
#sidebar-header .branch-tag { display: inline-block; padding: 1px 8px; border-radius: 10px;
                               font-size: 11px; font-weight: 600; background: #f1f8ff;
                               color: #0366d6; border: 1px solid #c8e1ff; margin-top: 4px; }
.nav-item { display: block; padding: 6px 16px; font-size: 13px; color: #586069; cursor: pointer;
            border-left: 3px solid transparent; transition: all 0.15s; }
.nav-item:hover { background: #f6f8fa; color: #24292e; }
.nav-item.active { background: #f1f8ff; color: #0366d6; border-left-color: #0366d6; font-weight: 500; }
.nav-sep { height: 1px; background: #e1e4e8; margin: 6px 16px; }
.nav-sub { padding-left: 28px; font-size: 12px; }
.nav-passrate { float: right; font-size: 11px; font-weight: 600; margin-top: 1px; }

/* Main content */
#main { margin-left: 260px; padding: 32px 36px; max-width: 1400px; flex: 1; }

/* Pages */
.page { display: none; }
.page.active { display: block; }

h2.page-title { font-size: 22px; font-weight: 700; margin-bottom: 6px; color: #24292e; }
.run-subtitle { font-size: 14px; color: #586069; margin-bottom: 28px; }

/* Cards */
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 16px; margin-bottom: 28px; }
.card { background: #fff; border: 1px solid #e1e4e8; border-radius: 8px; padding: 16px; }
.card h3 { font-size: 11px; text-transform: uppercase; letter-spacing: 0.07em; color: #586069; margin-bottom: 8px; }
.card .value { font-size: 26px; font-weight: 700; }
.card .sub { font-size: 12px; color: #586069; margin-top: 4px; }

/* Section */
.section { background: #fff; border: 1px solid #e1e4e8; border-radius: 8px; padding: 20px 24px; margin-bottom: 20px; }
.section h3 { font-size: 15px; font-weight: 600; margin-bottom: 14px; color: #24292e; }
.section-label { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.07em;
                 color: #586069; margin: 20px 0 10px; }
.section-label:first-child { margin-top: 0; }

/* Scenario description */
.scenario-desc { font-size: 14px; color: #586069; margin-bottom: 24px; line-height: 1.6; }

/* Mock data */
.mock-fn { font-size: 12px; margin-bottom: 6px; font-family: 'SF Mono', 'Consolas', monospace; }
.fn-name { color: #e36209; font-weight: 600; }

/* Customer goals */
.customer-goals { padding-left: 20px; }
.customer-goals li { font-size: 13px; color: #24292e; margin-bottom: 6px; line-height: 1.6; }

/* Tags */
.tags-list { display: flex; flex-wrap: wrap; gap: 6px; }
.tag { background: #f1f8ff; border: 1px solid #c8e1ff; border-radius: 12px;
       padding: 2px 10px; font-size: 12px; color: #0366d6; }

/* Eval table */
.eval-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.eval-table th { background: #f6f8fa; padding: 8px 12px; text-align: left; font-size: 11px;
                 text-transform: uppercase; letter-spacing: 0.06em; color: #586069;
                 border-bottom: 2px solid #e1e4e8; border-top: 1px solid #e1e4e8; }
.eval-table td { padding: 9px 12px; border-bottom: 1px solid #e1e4e8; vertical-align: top; }
.eval-table .rule-col { width: 78%; }
.eval-table .status-col { width: 22%; text-align: center; }
.rule-text { color: #24292e; line-height: 1.5; }
.applicability { font-size: 11px; color: #6a737d; margin-top: 3px; font-style: italic; }
.status-cell { text-align: center; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
.badge.pass { background: #dcffe4; color: #28a745; border: 1px solid #a3d9a5; }
.badge.fail { background: #ffeef0; color: #d73a49; border: 1px solid #fdaeb7; }
.badge.na   { background: #f6f8fa; color: #6a737d; border: 1px solid #d1d5da; }

/* Dead air */
.dead-air-list { padding-left: 20px; font-size: 13px; }
.dead-air-list li { margin-bottom: 6px; color: #d73a49; }
.dead-air-list em { color: #586069; }
em.ok { color: #28a745; font-style: normal; font-size: 13px; }

/* Transcript */
.transcript { font-size: 13px; line-height: 1.7; max-height: 550px; overflow-y: auto;
              background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px; padding: 12px 16px; }
.transcript-line { display: grid; grid-template-columns: 44px 72px 1fr; gap: 8px;
                   padding: 5px 0; border-bottom: 1px solid #e1e4e8; }
.transcript-line:last-child { border-bottom: none; }
.ts { color: #6a737d; font-family: monospace; font-size: 11px; padding-top: 2px; }
.speaker { font-weight: 600; font-size: 12px; }
.agent-line .speaker { color: #28a745; }
.customer-line .speaker { color: #0366d6; }
.text { color: #24292e; }

/* Timeline container */
.timeline-container { width: 100%; overflow-x: auto; }
.timeline-container > div { min-width: 800px; }

/* Summary scenario table */
.scenario-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.scenario-table th { background: #f6f8fa; padding: 8px 12px; text-align: left; font-size: 11px;
                     text-transform: uppercase; letter-spacing: 0.06em; color: #586069;
                     border-bottom: 2px solid #e1e4e8; border-top: 1px solid #e1e4e8; }
.scenario-table td { padding: 9px 12px; border-bottom: 1px solid #e1e4e8; }
.scenario-table tr:hover td { background: #f6f8fa; }
.sc-link { cursor: pointer; color: #0366d6; font-weight: 500; }
.sc-link:hover { text-decoration: underline; }

/* Pass bar */
.pass-bar-wrap { display: flex; align-items: center; gap: 8px; }
.pass-bar-bg { flex: 1; height: 8px; background: #e1e4e8; border-radius: 4px; overflow: hidden; }
.pass-bar-fill { height: 100%; border-radius: 4px; }
.pass-bar-label { font-size: 12px; font-weight: 600; min-width: 36px; text-align: right; }

/* Stat list */
.stat-list { list-style: none; }
.stat-list li { display: flex; justify-content: space-between; padding: 6px 0;
                border-bottom: 1px solid #f0f0f0; font-size: 13px; }
.stat-list li:last-child { border-bottom: none; }
.stat-val { font-weight: 600; color: #24292e; }

/* Transfer params */
.transfer-params-table { width: 100%; border-collapse: collapse; font-size: 13px; font-family: 'SF Mono', 'Consolas', monospace; }
.transfer-params-table td { padding: 5px 10px; border-bottom: 1px solid #e1e4e8; vertical-align: top; }
.transfer-params-table td:first-child { font-weight: 600; color: #e36209; width: 35%; white-space: nowrap; }
.transfer-params-table td:last-child { color: #24292e; word-break: break-all; }
.transfer-params-table tr:last-child td { border-bottom: none; }
"""

JS = """
function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const page = document.getElementById(id);
  if (page) page.classList.add('active');
  const nav = document.querySelector('[data-page="' + id + '"]');
  if (nav) nav.classList.add('active');
  window.scrollTo(0, 0);
}
"""


def _pass_bar(passed: int, total: int) -> str:
    pct = (passed / total * 100) if total > 0 else 0
    color = "#28a745" if pct >= 80 else "#e36209" if pct >= 50 else "#d73a49"
    return (f'<div class="pass-bar-wrap">'
            f'<div class="pass-bar-bg"><div class="pass-bar-fill" '
            f'style="width:{pct:.0f}%;background:{color}"></div></div>'
            f'<span class="pass-bar-label" style="color:{color}">{pct:.0f}%</span>'
            f'</div>')


def build_summary_page(run: dict) -> str:
    s = run["summary"]
    branch = run["branch"]

    # Avg excessive dead air
    dead_totals = []
    for sc in run["scenarios"].values():
        if sc["state"]:
            spans = get_conversation_spans(sc["state"])
            dead_totals.append(len(count_excessive_dead_air(spans)))
    avg_dead = sum(dead_totals) / len(dead_totals) if dead_totals else 0

    # Run timestamp
    run_ts = "unknown"
    for sc in run["scenarios"].values():
        if sc["run_ts"]:
            try:
                dt = datetime.fromisoformat(sc["run_ts"].replace("Z", "+00:00"))
                run_ts = dt.strftime("%Y-%m-%d %H:%M UTC")
                break
            except Exception:
                pass

    # All tasks
    all_tasks = sorted({t for sc in run["scenarios"].values() for t in sc["tasks"]})
    tasks_html = "".join(f'<span class="tag">{t}</span>' for t in all_tasks)

    # Per-scenario rows
    rows = ""
    for sid, sc in run["scenarios"].items():
        p, t = scenario_pass_rate(sc.get("results", {}))
        desc = (sc.get("yaml_data") or {}).get("description", "")
        rows += (f'<tr><td><span class="sc-link" onclick="showPage(\'scenario-{sid}\')">{sid}</span>'
                 f'<div style="font-size:11px;color:#586069;margin-top:2px">{desc}</div></td>'
                 f'<td>{_pass_bar(p,t)}'
                 f'<span style="font-size:11px;color:#586069;margin-left:6px">{p}/{t}</span></td>'
                 f'</tr>')

    pct = s["total_passrate"] * 100
    pct_color = "#28a745" if pct >= 80 else "#e36209" if pct >= 50 else "#d73a49"

    return f"""
    <div id="page-summary" class="page active">
      <h2 class="page-title">{run['run_name']}</h2>
      <p class="run-subtitle">assurantauto E2E — branch: <strong>{branch}</strong> — {len(run['scenarios'])} scenarios</p>

      <div class="section">
        <h3>Run Summary</h3>
        <ul class="stat-list">
          <li><span>Pass rate</span><span class="stat-val" style="color:{pct_color}">{pct:.1f}%</span></li>
          <li><span>Rules passed</span><span class="stat-val">{int(s['passed'])} / {int(s['total'])}</span></li>
          <li><span>Scenarios run</span><span class="stat-val">{len(run['scenarios'])}</span></li>
          <li><span>Total cost</span><span class="stat-val">${s['total_cost']:.4f}</span></li>
          <li><span>Avg excessive dead air / call</span><span class="stat-val">{avg_dead:.1f}</span></li>
          <li><span>Run timestamp</span><span class="stat-val" style="font-weight:400">{run_ts}</span></li>
        </ul>
      </div>

      <div class="section">
        <h3>Tasks Covered</h3>
        <div class="tags-list">{tasks_html or '<em>none</em>'}</div>
      </div>

      <div class="section">
        <h3>Scenarios</h3>
        <table class="scenario-table">
          <thead><tr><th>Scenario</th><th>Pass Rate</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
    </div>"""


def get_escalation_params(state: dict) -> Optional[dict]:
    """Return the parameters of the first escalate_to_agent_from_ivr call, or None."""
    if not state:
        return None
    for action in state.get("actions", []):
        if action.get("type") == "function_request":
            fr = action.get("function_request", {})
            if fr.get("function_name") == "escalate_to_agent_from_ivr":
                return fr.get("parameters", {})
    return None


def render_escalation_params(params: dict) -> str:
    # Key params to highlight first, remainder follow alphabetically
    priority_keys = ["GACallerType", "GAIntent", "TransferReason", "ClaimStatus",
                     "contractFoundBy", "Identified", "Question"]
    ordered = [(k, params[k]) for k in priority_keys if k in params]
    ordered += [(k, v) for k, v in sorted(params.items()) if k not in priority_keys]
    empty_cell = '<em style="color:#6a737d">—</em>'
    rows = "".join(
        f"<tr><td>{k}</td><td>{str(v) if v not in (None, '', 'null') else empty_cell}</td></tr>"
        for k, v in ordered
    )
    return f'<table class="transfer-params-table">{rows}</table>'


def build_scenario_page(sid: str, sc: dict, label: str) -> str:
    yaml_data = sc.get("yaml_data") or {}
    description = yaml_data.get("description", sid)
    goals = (yaml_data.get("customer") or {}).get("goals", [])
    evals = get_eval_rows(sc.get("results", {}))

    spans = get_conversation_spans(sc["state"]) if sc.get("state") else []
    excessive = count_excessive_dead_air(spans)
    transcript = extract_transcript(sc["state"]) if sc.get("state") else []
    timeline_html = build_timeline_div(sc.get("state") or {}, spans, f"{sid} — {label}")
    escalation_params = get_escalation_params(sc.get("state"))

    goals_html = "".join(f"<li>{g}</li>" for g in goals) if goals else "<li><em>None defined.</em></li>"
    tasks_html = " ".join(f'<span class="tag">{t}</span>' for t in sc.get("tasks", []))

    p, t = scenario_pass_rate(sc.get("results", {}))

    return f"""
    <div id="scenario-{sid}" class="page">
      <h2 class="page-title">{sid}</h2>
      <p class="scenario-desc">{description}</p>

      <div class="section">
        <h3>Scenario Overview</h3>
        <div class="section-label">Customer Goals</div>
        <ul class="customer-goals">{goals_html}</ul>
        <div class="section-label">Mock API Responses</div>
        {_mock_summary(yaml_data)}
        <div class="section-label">Tasks Invoked</div>
        <div class="tags-list">{tasks_html or '<em>none recorded</em>'}</div>
      </div>

      <div class="section">
        <h3>Evaluation Results
          <span style="font-size:12px;color:#586069;font-weight:400;margin-left:10px">{p}/{t} rules passed</span>
        </h3>
        {render_eval_table(evals, label)}
      </div>

      <div class="section">
        <h3>Excessive Dead Air <span style="font-size:12px;color:#586069;font-weight:400">(≥ 5 seconds, {len(excessive)} period{'s' if len(excessive) != 1 else ''})</span></h3>
        {render_dead_air_section(excessive)}
      </div>

      <div class="section">
        <h3>Execution Timeline</h3>
        <div class="timeline-container">
          {timeline_html}
        </div>
      </div>

      <div class="section">
        <h3>Transcript</h3>
        {render_transcript(transcript)}
      </div>

      {f'''<div class="section">
        <h3>Transfer Parameters <span style="font-size:12px;color:#586069;font-weight:400">(escalate_to_agent_from_ivr)</span></h3>
        {render_escalation_params(escalation_params)}
      </div>''' if escalation_params is not None else ''}
    </div>"""


def build_nav(run: dict) -> str:
    items = ('<span class="nav-item active" data-page="page-summary" '
             'onclick="showPage(\'page-summary\')">Summary</span>\n'
             '<div class="nav-sep"></div>\n')
    for sid, sc in run["scenarios"].items():
        p, t = scenario_pass_rate(sc.get("results", {}))
        pct = (p / t * 100) if t > 0 else 0
        color = "#28a745" if pct >= 80 else "#e36209" if pct >= 50 else "#d73a49"
        pct_badge = f'<span class="nav-passrate" style="color:{color}">{pct:.0f}%</span>'
        items += (f'<span class="nav-item nav-sub" data-page="scenario-{sid}" '
                  f'onclick="showPage(\'scenario-{sid}\')">{sid}{pct_badge}</span>\n')

    branch_tag = f'<div class="branch-tag">{run["branch"]}</div>'
    header = f'<div id="sidebar-header"><h1>{run["run_name"]}</h1>{branch_tag}</div>'
    return f'<nav id="sidebar">{header}\n{items}</nav>'


def generate_report(run_dir: str, output_path: str, scenarios_dir: str = None) -> None:
    if scenarios_dir is None:
        scenarios_dir = str(SCENARIOS_BASE)

    print(f"Loading run: {run_dir}")
    run = load_run(Path(run_dir), Path(scenarios_dir))
    label = run["branch"]

    print("Building summary page...")
    summary_page = build_summary_page(run)

    pages = [summary_page]
    for i, (sid, sc) in enumerate(run["scenarios"].items(), 1):
        print(f"Building scenario page {i}/{len(run['scenarios'])}: {sid}")
        pages.append(build_scenario_page(sid, sc, label))

    nav = build_nav(run)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{run['run_name']} — Scenario Report</title>
  <script src="https://cdn.plot.ly/plotly-2.35.0.min.js"></script>
  <style>
{CSS}
  </style>
</head>
<body>
{nav}
<main id="main">
{"".join(pages)}
</main>
<script>
{JS}
</script>
</body>
</html>"""

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"\nReport written to: {out}")


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", help="Run directory (e.g. sandbox_20260406_run1)")
    parser.add_argument("--output", "-o", default=None,
                        help="Output HTML path (default: <run_dir>/report.html)")
    parser.add_argument("--scenarios-dir", default=None)
    args = parser.parse_args()

    output = args.output or str(Path(args.run) / "report.html")
    generate_report(args.run, output, args.scenarios_dir)


if __name__ == "__main__":
    main()
