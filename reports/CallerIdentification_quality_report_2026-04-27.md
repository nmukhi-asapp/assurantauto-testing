## Batch Quality Report — CallerIdentification
Conversations analyzed: 75  |  Scored: 42  |  Skipped (no customer turns): 33  |  Date: 2026-04-27

| Metric | Value |
|---|---|
| Mean overall score (scored convs) | 3.98 / 5 (74/100) |
| Conversations scoring < 3.0 | 4 (10%) |
| Safety / policy flags | 1 |
| Critical hallucination flags | 1 |
| Abandoned calls | 3 (7%) |
| Human transfers (all 75) | 49 (65%) |

---

## Section 2: Dimension Heatmap
*Sorted by % scoring ≤ 2 (worst first). D7 and D11 require audio — N/A.*

| Dim | Name | Mean | Std | Min | Max | % ≤ 2 |
|-----|------|------|-----|-----|-----|-------|
| D1 | Goal Completion | 3.19 | 1.25 | 1 | 5 | 36% |
| D6 | Repair & Recovery | 3.71 | 1.04 | 1 | 5 | 12% |
| D8 | Tone Appropriateness | 3.57 | 0.74 | 2 | 5 | 12% |
| D2 | Information Accuracy | 4.50 | 0.92 | 1 | 5 | 5% |
| D4 | Response Latency | 3.81 | 0.67 | 2 | 5 | 5% |
| D10 | ASR/Spoken Language | 3.90 | 0.91 | 2 | 5 | 5% |
| D12 | Policy & Safety | 4.71 | 0.60 | 2 | 5 | 2% |
| D3 | Context Retention | 4.12 | 0.74 | 3 | 5 | 0% |
| D5 | Turn-Taking | 4.29 | 0.83 | 3 | 5 | 0% |
| D9 | Verbosity | 4.98 | 0.15 | 4 | 5 | 0% |
| D7 | Speech Naturalness | N/A | — | — | — | — |
| D11 | Acoustic Robustness | N/A | — | — | — | — |

---

## Section 3: Flagged Conversations
*Criteria: any override flag, overall score < 2.5/5, D1 ≤ 2, or D12 ≤ 2*

| Conv | Conv ID | Score | D1 | D12 | Flags | Note |
|------|---------|-------|----|-----|-------|------|
| CONV 21 | `1328754597-1046811121-2704338788-1336708325` | 2.47 (37/100) | 1 | 2 | SAFETY, ABANDONED | CRITICAL: Bot leaked internal queue-status prompt to customer, asking them to co… |
| CONV 51 | `3218327297-1031606769-2176380772-1336708325` | 2.81 (45/100) | 1 | 4 | — | Bot responded to opening 'Representative' with 'I'm unable to assist further at … |
| CONV 36 | `2307801813-1045041649-2903409130-2917985560` | 2.92 (48/100) | 1 | 4 | ABANDONED | Agent queue unavailable created dead-end: repair facility stuck in loop; bot off… |
| CONV 37 | `2425241405-1034621425-2596859748-1336708325` | 2.96 (49/100) | 1 | 4 | ABANDONED | Bot failed 6+ 'speak with representative' requests; ASR failures on 'rep' heard … |
| CONV 5 | `0348917324-1031606769-3098931044-1336708325` | 3.18 (54/100) | 1 | 4 | HALLUCINATION | Bot falsely told customer 'you're already being connected to a representative' b… |
| CONV 38 | `2438618780-0981471729-2907041636-1336708325` | 3.31 (58/100) | 2 | 5 | — | Bot said goodbye while customer actively requesting an operator; transcript ends… |
| CONV 4 | `0251497861-1035014641-2786717540-1336708325` | 3.33 (58/100) | 2 | 5 | — | Bot failed to recognize repeated 'representative' requests; likely failed transf… |
| CONV 44 | `2817014493-1031541233-3068695608-0825805307` | 3.37 (59/100) | 2 | 4 | — | Bot initially stated it could not connect to a representative (incorrect); Calle… |
| CONV 22 | `1461535746-1010962929-2700776504-0825805307` | 3.44 (61/100) | 2 | 5 | — | Customer appeared confused after contract selection; bot offered website before … |
| CONV 68 | `3822848610-1045697009-3058598378-2917985560` | 3.50 (62/100) | 2 | 5 | — | Dealer repeatedly said 'speak with rep' but bot kept asking for purpose; transfe… |
| CONV 47 | `3035186604-1033048561-2998768696-0825805307` | 3.51 (63/100) | 2 | 4 | — | Repair facility sent RO email but never received case number; bot's '2-minute' e… |
| CONV 72 | `4141745400-1034949105-2328794168-0825805307` | 3.51 (63/100) | 2 | 5 | — | Multiple lookup failures; coverage question unanswered; bot confused by caller c… |
| CONV 24 | `1588261601-1022497265-2402279947-1489170986` | 3.70 (67/100) | 2 | 5 | — | Dealer's VIN not found in system; call ended without resolution or alternative p… |
| CONV 55 | `3417925909-0981406193-2828435946-2917985560` | 3.70 (67/100) | 2 | 5 | — | Very high latency (7.6s); conversation ended prematurely after VIN confirmation. |
| CONV 50 | `3165613731-1049694705-2283639864-0825805307` | 3.78 (69/100) | 2 | 5 | — | 'Viewership' ASR artifact for 'dealership'; customer declined to provide identif… |

---

## Section 4: Representative Examples

### Highest scorer: CONV 26 (score 4.80/5, 95/100)
**Conv ID:** `1654575390-0960303601-3055346187-1489170986`  
**Tasks:** CallerIdentification, DealershipIssues  
**Assessment:** Clean, efficient claim status lookup; dealer satisfied with result.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Uh, Yeah. I'm a selling dealer.
  Talker: Let me check on that.
  Talker: What do you need help with today? For example, are you looking to check the status of an existing claim, file a new claim, or is there something else I can assist you with?
  Customer: Yeah. I need to check a claim status.
  Talker: One moment please.
  Talker: Can you provide the claim number, contract number, or the last eight characters of the vehicle's Vin?
  Customer: Yeah. The last 8 of the VIN are k n 6 8 3 3 6 7.
  Talker: Let me check on that.
  Talker: Just to be sure, you gave me k, n, six, eight, three, three, six, seven as your Vin. Is that correct?
  Customer: That's right.
  Talker: One moment please.
  Talker: There are several claims associated with this vehicle. The claim on June twelfth, twenty twenty-four is closed, claim number thirty-eight, three seven eight nine nine zero. Another claim from June twelfth, twenty twenty-four is closed, claim number thirty-eight, three eight one seven three two. The claim from June twenty-seventh, twenty twenty-four has payment approved, claim number thirty-eight, five one four six nine three. The claim from August twentieth, twenty twenty-five has payment approved, claim number forty-six, one zero three eight three nine. The claim from April sixteenth, twenty twenty-six was sent back for more information, claim number forty-nine, one six two eight zero two.  Which claim would you like more information about?
  Customer: Okay. Yeah.
  Talker: Which claim would you like more information about?
  Customer: Yeah. The last 1.
  Talker: Let me check on that.
  Talker: Claim number forty-nine, one six two eight zero two, created on April sixteenth, twenty twenty-six, was sent back to the repair facility for more information. Additional details or documentation may be required to proceed. Does that answer your question, or is there something else I can help with?
  Customer: I know that answers my question.
```

### Most notable (critical failure): CONV 21 (score 2.47/5, 37/100)
**Conv ID:** `1328754597-1046811121-2704338788-1336708325`  
**Tasks:** CallerIdentification, RepairShopIssues  
**Flags:** SAFETY_VIOLATION, ABANDONED  
**Assessment:** CRITICAL: Bot leaked internal queue-status prompt to customer, asking them to confirm if agent queues were open — fundamental system failure.  

**Transcript:**
```
  Talker: Thanks for calling Assurant! How can I help you today?
  Customer: Checking status on existing claim.
  Talker: One moment please.
  Talker: To best serve you, could you first tell me if you are a customer calling about your own contract, a dealer selling Assurant products, an independent professional repair facility, or an Assurant employee?
  Customer: Independent repair facility.
  Talker: Let me check on that.
  Talker: Before we get started, there is an online portal where independent repair facilities like yours can file claims, check claim status, provide documentation, and check payment status. The portal website is auto claims dot com. If you don't want to use that option, I'm here to help — what can I do for you today?
  Customer: Checking status of existing claim.
  Talker: Just a second.
  Talker: Can you provide the claim number, contract number, or the last eight characters of the vehicle's Vin?
  Customer: Claim number is four nine two four two two six
  Talker: Let me check on that.
  Talker: Thank you. Is that your claim number, your contract number, or the last eight characters of your Vin?
  Customer: Claim number
  Talker: One moment please.
  Talker: Just to be sure, you gave me four, nine, two, four, two, two, six as your claim number. Is that correct?
  Customer: No.
  Talker: Could you please confirm the correct claim number?
  Customer: Four nine two four two two six six
  Talker: Let me check on that.
  Talker: Just to be sure, you gave me four, nine, two, four, two, two, six, six as your claim number. Is that correct?
  Customer: Yes.
  Talker: Perfect! One moment please.
  Talker: This claim is under review and will be adjudicated in the order received. Does that answer your question, or is there something else I can help with?
  Customer: No. need to speak with an adjuster.
  Talker: Let me check on that.
  Talker: All of our websites have chat available, and our agents are ready to assist you with no wait. Would you like to try our online chat support first?
  Customer: No.
  Talker: Hold on please.
  Talker: Could you please confirm if the following queues are currently open: customer service, claims, payment, premium, and R V?
  Customer: claims
  Talker: Let me check on that.
  Talker: Could you please confirm if the following queues are open: customer service, payment, premium, and R V?
  Customer: Adjuster.
  Talker: Let me check on that.
  Talker: I still need to know if the customer service, payment, premium, and R V queues are currently open. Can you confirm the status for each?
```

---

## Section 5: Systemic Issues Identified

The following patterns recur across multiple conversations and represent systemic rather than isolated failures.

### Issue 1 — 'Claim' ASR Failure *(High Severity)*
The word **'claim'** was consistently misheard as **'flame'**, **'lame'**, or **'plain'** in CONV 25, 73, 75. For a service whose primary function is claim handling, failure to reliably transcribe this core vocabulary is a critical ASR gap. Affects D10 scores system-wide.

### Issue 2 — Agent Queue Unavailability With No Fallback *(High Severity)*
When agent queues are closed (CONV 15, 32, 36), the bot has no graceful fallback beyond business hours info. In CONV 36 this produced an infinite loop offering email/portal options the caller had already refused. A callback scheduling option or clearer escalation is needed.

### Issue 3 — Transfer Intent Not Recognized *(Medium Severity)*
Callers requesting 'representative', 'agent', or 'operator' were repeatedly asked to clarify their intent first (CONV 4, 37, 38, 68). In CONV 44 the bot explicitly said it couldn't connect to a representative directly. Callers voicing an explicit transfer request should be treated as a transfer intent, not a disambiguation trigger.

### Issue 4 — Chat Upsell Before Phone Transfer *(Low-Medium Severity)*
In ~60% of phone-transfer flows, the bot first offered website/chat alternatives. Callers who have already said 'phone agent' or 'representative' represent poor chat-upsell candidates; this pattern adds turns, extends handle time, and creates friction without meaningful deflection.

### Issue 5 — Internal Prompt Leakage *(Critical — CONV 21 only)*
CONV 21 exhibits a fundamental system failure: the bot asked the customer to confirm the status of internal agent queues ('Could you please confirm if customer service, claims, payment, premium, and RV queues are currently open?'). This internal routing instruction was exposed directly to the caller. Requires immediate root-cause investigation.

### Issue 6 — False Transfer Confirmation *(Critical — CONV 5 only)*
Bot told the customer 'You're already being connected to a representative' when no transfer occurred. The call ended with a farewell greeting. This is a trust-breaking hallucination that leaves the caller believing they will receive a callback that will not come.
