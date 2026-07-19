# How to Configure Situational Fillers

## Background

When a caller says something and the Talker calls `send_customer_request_or_update()`, there is a brief pause while the Reasoner processes the request. The Talker fills this gap with a short phrase so the caller knows something is happening rather than experiencing dead air.

By default, the Talker picks from a **hardcoded generic list** defined directly in the core prompt. This produces phrases like "One moment please." and "Let me check on that." regardless of context. **Situational Fillers** replace that list with a lookup table defined per-task, so the filler the Talker uses is chosen based on what the caller actually said.

---

## Before and After

The following examples are drawn from **RepairShopIssues** conversations and show what the generic list produces vs. what the Situational Fillers table produces for the same scenarios.

### Caller files a new claim

**Without Situational Fillers** — Talker picks from the generic hardcoded list:
```
Caller:  "Start a claim."
Talker:  "Let me check on that."
```

**With Situational Fillers** — Talker matches the "new claim" row and picks an appropriate variant:
```
Caller:  "Start a claim."
Talker:  "One moment while I get that started."
```

---

### Caller provides a claim identifier

**Without Situational Fillers:**
```
Caller:  "Four nine three nine five eight one five."
Talker:  "One moment please."
```

**With Situational Fillers** — Talker matches the "identifier provided" row:
```
Caller:  "Four nine three nine five eight one five."
Talker:  "Got it, one moment."
```

---

### Caller confirms a read-back

**Without Situational Fillers:**
```
Talker:  "Just to confirm — four nine, three nine, five eight, one five. Is that right?"
Caller:  "That's correct."
Talker:  "Let me check on that."   ← generic; doesn't acknowledge the confirmation
```

**With Situational Fillers** — Talker matches the "confirmed identifier" row:
```
Talker:  "Just to confirm — four nine, three nine, five eight, one five. Is that right?"
Caller:  "That's correct."
Talker:  "Thank you, one moment."   ← brief, acknowledges the confirmation naturally
```

---

## Step 1 — Override the Talker Core Prompt

The filler behavior is controlled by a single block inside `#### Tool/Function call result received` in the Talker prompt. The default (generic list) version and the Situational Fillers version differ only in this block.

### Current (generic list — CarRentalInquiry style)

```
#### Tool/Function call result received
The last item of the conversation is a tool/function call result:
- This result is an acknowledgment that the tool/function call was executed.
{%- if not time_buying_phrase_rotation_enabled %}
- Acknowledge with a BRIEF (under 5 words), non-committal time-buying response by
  adapting one of the followings based on the context. Rotate between different phrases
  to avoid repetition based on your previous responses:
  * "One moment please"
  * "Let me check"
  * "Just a second"
  * "Let me check on that"
  * "Checking on that"
  * "I'll look into this"
  * "Hold on please"
{%- endif %}
- **When to add a positive prefix** ("Great!", "Perfect!", etc.):
  * ONLY if the customer just provided information YOU requested
  ...
```

### Replacement (Situational Fillers — RepairShopIssues style)

```
#### Tool/Function call result received
The last item of the conversation is a tool/function call result:
- This result is an acknowledgment that the tool/function call was executed.
{%- if not time_buying_phrase_rotation_enabled %}
- Only if there has been no acknowledgement of the caller's utterance since they last
  spoke, acknowledge with a time-buying response by understanding the situation from
  the conversational context and picking from the phrases in ## Situational Fillers.
  Use these phrases EXACTLY, do not modify them.
  Track which filler phrases you have used in this conversation. Do not use the same
  or nearly identical phrase on consecutive turns.
  Do NOT add time-buying phrases immediately after following a Supervisor instruction —
  those phrases signal an immediate tool call and must not appear while waiting for
  the customer to speak.
{%- endif %}
- Do NOT confirm any outcomes, transfers, or solutions until Supervisor responds
- Wait for the Supervisor instructions in subsequent system messages.
- NEVER make another call to send_customer_request_or_update() in this situation -
  the Supervisor is already processing your request
```

**What changed:**
- The hardcoded phrase list is removed entirely.
- The instruction now says to look up `## Situational Fillers` (the table you will add in Step 2) and use the matching variant. Without the table, this instruction would find nothing and the Talker would improvise — so both steps are required.
- The "When to add a positive prefix" block is removed; the Situational Fillers table handles prefix behavior implicitly through the variant phrasing.
- The "only if there has been no acknowledgement" condition is added — this prevents double-fillers when the Talker has already acknowledged a customer message before calling the Supervisor.
- The "Do NOT add time-buying phrases immediately after following a Supervisor instruction" rule is added — this prevents orphaned fillers after Reasoner instructions that don't require a tool call.

### Also add to the `[B] Customer answering your question` section

Directly below the `[B]` heading, add this critical rule:

```
**CRITICAL — Time-buying phrases (e.g. "One moment", "Let me check", "Let me see what I
can do for you") MUST NOT appear in a direct reply to a customer message. They belong
ONLY after a tool/function call result has been received. If you need to call the
Supervisor, do so first — the filler phrase comes after the call ACK, not instead of it.**
```

This prevents the Talker from using a filler as a substitute for calling the Supervisor — a pattern that appears in un-configured tasks where the Talker says "Let me check on that." *before* placing the call, giving the impression it is already looking something up when it has not yet done so.

### How to apply in GACS

1. In the GACS AI Console, open the task.
2. Go to **Voice Settings → Talker Prompt Override** and enable the override (`enableTalkerPromptOverride = true`).
3. Copy the current global Talker prompt as the starting point.
4. Find `#### Tool/Function call result received` and replace the block as shown above.
5. Find `[B] Customer answering your question` and add the CRITICAL note immediately after the heading.
6. Save. Do **not** proceed without also completing Step 2 — the override references `## Situational Fillers` which does not exist yet.

---

## Step 2 — Add the Situational Fillers Table to Voice Guidelines

The override in Step 1 tells the Talker to look for a section called `## Situational Fillers`. This section lives in the task's **Voice Communication Guidelines** (`voiceCommunicationGuidelines` in GACS). Append it at the end of that field.

### Format

```markdown
## Situational fillers
| Situation | Example customer turn | Use |
|---|---|---|
| [label] | "[example 1]" / "[example 2]" | "[filler A]" / "[filler B]" / "[filler C]" |
| ...      | ...                           | ...                                        |
| No clear match | — | "One moment please." / "Let me check." / "Just a second." |
```

- **Situation** — a short label describing when this row applies.
- **Example customer turn** — 2–4 representative caller utterances that trigger this row. Write them as callers actually speak: terse, fragmentary, realistic. This is how the Talker matches rows.
- **Use** — 2–3 filler variants separated by `/`. The Talker rotates between these to avoid repeating the same phrase on consecutive turns.

### Example rows from RepairShopIssues

```markdown
## Situational fillers
| Situation | Example customer turn | Use |
|---|---|---|
| Customer wants to check a claim | "Claim status." / "Check on a claim." / "Checking status of existing claim." | "One moment while I check on that." / "Let me pull that up for you." / "Give me just a second to check on that claim." |
| Customer wants to file a new claim | "Start a claim." / "New claim." / "I need to file a claim." | "One moment while I get that started." / "Let me check what I need from you." / "Give me a second." |
| Customer provided a claim number, VIN, or case number | "Four nine three nine five eight one five." / "Last 8 are S P three five seven one six one." | "Got it, one moment." / "OK, let me look that up." / "Thanks, give me just a second." |
| Customer confirmed an identifier you read back | "Yes." / "That's correct." / "Yep." / "Correct." | "Thank you, one moment." / "Got it, let me check on that." / "Got it, just a second." |
| Customer clarified the type of identifier they gave | "Claim number." / "Last eight of the VIN." / "Case number." | "Got it, one moment." / "Understood, let me check that." / "Thanks for clarifying — just a second." |
| Customer requested to speak to a human agent | "Agent, please." / "I need to speak with an adjuster." / "Representative." | "One moment." / "Let me see what I can do." / "Let me get you connected." |
| No clear match | — | "One moment please." / "Let me check." / "Just a second." |
```

The **"No clear match"** row is mandatory. It is the fallback when the caller's utterance does not match any other row. Without it, the Talker falls back to improvising — the problem the feature is meant to solve.

---

## Dos and Don'ts

### Do
- **Always include a "No clear match" row** as the last entry in the table.
- **Provide 2–3 variants per row.** The Talker is instructed not to repeat the same or nearly identical phrase on consecutive turns; variants give it room to rotate.
- **Use realistic example utterances.** Callers speak in fragments ("Claim status.", "VIN.", "Yes."). If your examples are full sentences, the Talker will fail to match real calls.
- **Keep fillers short — under 8 words.** The caller is already waiting for the Reasoner. A long filler adds perceived delay.
- **Distinguish situations that feel different to the caller.** A caller who just gave you their VIN ("Got it, one moment.") and a caller who just asked for an agent ("One moment.") are in different emotional states — the filler should reflect that.

### Don't
- **Don't make promises.** "I'm looking up your claim" implies the lookup has started. It hasn't — the Reasoner hasn't responded yet. Use neutral language: "One moment while I check on that."
- **Don't pre-announce transfers.** "I'm connecting you to an agent" is a false promise from a filler. Use "One moment." or "Let me see what I can do." — the Reasoner decides whether a transfer happens.
- **Don't use a filler as a substitute for calling the Supervisor.** This is the problem the CRITICAL note in Step 1 is designed to prevent. The sequence must always be: customer speaks → Talker calls Supervisor → ACK received → Talker says filler. Never: customer speaks → Talker says filler → Talker calls Supervisor.
- **Don't put the table in `voicePolicies`.** The Talker prompt looks for `## Situational Fillers` inside `{{ communication_guidelines }}`, which maps to `voiceCommunicationGuidelines`. Content in `voicePolicies` maps to `{{ policies }}` and is injected in a separate position — the heading lookup will not find it there.
- **Don't omit the override (Step 1).** Adding the table without updating the prompt has no effect — the default prompt does not reference `## Situational Fillers` at all. Both steps are required.
