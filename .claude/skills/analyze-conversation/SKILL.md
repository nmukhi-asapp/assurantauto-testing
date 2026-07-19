---
description: Analyze conversation data and identify issues
---

# Conversation Analysis Instructions

## Initial Setup

When this command is invoked, first check if the user has already provided conversation files to analyze:

1. **Check for existing conversation files**:
   - Look in `tools_output/athena_actions/` for recently fetched conversations
   - Check if the user has specified a file or folder path
   - Look in `special_conversations/` for existing conversation files

2. **If no conversation files are found or specified**:
   - Ask the user if they want to fetch a conversation first using `/fetch-conversation`
   - Provide a helpful prompt like: "I don't see any conversation files to analyze. Would you like to fetch a conversation from Athena first? You can use `/fetch-conversation` with a company marker and conversation ID."
   - Wait for the user to either:
     - Run `/fetch-conversation` to fetch new conversations
     - Provide a path to existing conversation files
     - Specify a folder to analyze

3. **Once conversation files are available**:
   - Confirm which files will be analyzed
   - Proceed with the analysis

<context>
## Context

### System Architecture
GA will answer customer messages in "turns". Each turn will start by receiving a customer message, from another the customer (see message actions, sender), which triggers GA to start processing the conversation so far. All turns are included in the conversations, there's no explicit turn separation in the file. A turn only ends when GA sends messages (message actions with bot  in them).

Note that turns can be "interrupted" if a user sends messages while GA is processing. GA will continue by starting a new turn with all context up to the last received customer message, and any interrupted turns are discarted.

### Additional Context Resources
To get more context as needed:
- GA runs with LLMs. The core instructions file is here: generative-agent/asapp/generative_agent/prompters/task/template_prefix_kb_aware.j2
- GA source code in python is available to you in generative-agent/. NOTE this is a large codebase.
- GA also uses "task instructions" which in this case are here: task-instructions/. If you need task instructions and can't find them, please ask.
- GA also uses "functions" that are configured via tooling, and you can see their definition here: function-definitions/functions.json. If you need function instructions and can't find them, please ask.

### Key ModelActions
In each turn GA uses those instructions, plus "ModelActions" as input (the result from previous turns) and also produces "ModelActions" as an output, and that creates a conversation. The most important ones for us are:
- **thought**: the chain-of-thought output of GA. This is created by GA following the instructions in the j2 files above.
- **message**: messages from either a previous IVR/VirtualAgent system, the customer, or GA itself.
- **function_request / response**: the a function call that results from GA's output.
- **escalate_live_agent**: an escalation to a live agent that occured as a result of a function request.
- **system_transfer**: a transfer that occured as a result of a function request.

If a message or function request is from GA, the preceding thoughts will include hints as to WHY GA called that function or spoke the message.

### Filler / Time-Buying Phrases
GA sometimes sends a short acknowledgement/stalling message ("One moment while I check that.", "Let me look into that for you.", "Give me a second.") before it actually does the real work of a turn. This exists in two forms depending on channel:
- **Voice (Talker/Reasoner architecture)**: the Talker plays one of these while handing off to the Reasoner via the `send_customer_request_or_update` function. Some companies define an exact, closed list of allowed phrases per task in GACS under `voiceCommunicationGuidelines` → a `## Situational Fillers` section (a table of Situation → Example customer turn → Use, or a bullet list). If you have GACS access for the company (e.g. `mcp__gacs__get_branch`, or the task-instructions folder), fetch this list first and match against it exactly (case-insensitive, ignore trailing punctuation). In the action log, `source_system` values like `task_bot` and `function_caller*` belong to the Reasoner; `voice_assistant` and `voice_orchestrator` belong to the Talker.
- **Chat**: a separate FillerBot may emit an acknowledgement/time-buying message (`source_system` such as `FILLER_BOT`) before the main bot's real response.
- **No company-specific list available**: fall back to a heuristic — flag any short (roughly under 15 words) bot message that contains no concrete answer or data and matches common time-buying language: "one moment", "give me a second/moment", "let me check/look into/look up/pull up that", "hold on", "just a second", "I'll look into this", "bear with me", etc.

For every filler/time-buying message found, check whether the turn that follows it (up to the next customer-facing bot message) contains **any `function_request` at all**. If it does not — the turn only reasoned and replied without calling any function/API — that is a **delegation opportunity**: the round-trip wasn't needed, and if the Talker/front-end had been given more context (either the specific fact/answer directly, or a scripted sub-flow to run on its own), it could have skipped the filler and handled the exchange in a single turn.

### Business Objective
As a product, the objective of GenerativeAgent is to automate customer service. In this vein, a measure of success for GA is how much it is able to contain customer interactions, successfully resolving customer's issues without escalating to a live agent. Escalations should only happen if GA isn't able to solve the customer's issues with the tools and knowledge it has.

### Important Metrics and Definitions

**Turn Duration vs. Time Between Turns:**
- **Turn Duration**: The time GA takes to process and respond (from receiving customer's message until GA sends a response). This is a critical performance metric.
- **Time Between Turns**: The time the customer takes to respond after GA's message. This is NOT a processing delay or system issue - it's normal customer behavior.

**Output Safety Detections:**
- Output safety detections are NOT failures - they are the system working correctly.
- When output safety blocks a message, it means the safety mechanism successfully prevented GA from sending unsupported or hallucinated information.
- However, frequent output safety detections may indicate the underlying model needs better grounding or instructions.

**User Input Issues:**
- When a user provides problematic data (e.g., typos in email addresses), this is NOT a system error or suspicious behavior.
- GA should be resilient and intelligent enough to detect such issues and ask for confirmation.
- Example: If an email has an obvious typo like "user@gma8l.com" (should be "gmail.com"), GA should recognize this and confirm with the customer.
</context>

<objective>
## Objective

Your general objective is to help GA developers debugging what happened in certain conversations, and uncover specific patterns that might be happening.

The conversations you must investigate will be specified by the user or found in standard locations like:
- `tools_output/athena_actions/` (freshly fetched conversations)
- `special_conversations/` (saved conversation files)
- Any path provided by the user

Each conversation file is a JSON listing the ModelActions in that conversation.

Include things like:
- Analysis per turn
- **Turn duration** (how long GA took to respond)
- Time between turns (how long customer took to respond)
- Specific errors that happened
- Anything suspicious
- **Filler / time-buying phrase usage** — every filler GA sent, and whether the turn that followed made an actual function call (see Filler / Time-Buying Phrases in Context)
- **Potential improvements** - actionable recommendations for making GA more resilient and effective

### Analysis Approach

Analyze conversations one by one. You must prioritize accuracy over speed here.

### Critical Analysis Guidelines

When analyzing conversations, go beyond surface-level observations. For each issue or escalation, identify:

1. **Root Cause**: What actually went wrong? Was it a function failure, missing information, user error, or something else?
2. **GA's Response**: How did GA handle the situation? Was it appropriate?
3. **Resilience Opportunities**: Could GA have been more intelligent or resilient in handling the situation?
4. **Latency**: Did any prompt calls (llm_request) take a long time (over 10s)? This is important because if a turn takes over 5 minutes to run, then there could be problems with article cache misses (cahce TTL is 5 mins).
5. **Filler Round-Trip Waste**: Did GA send a filler/time-buying message and then respond without making any function call in that same turn? If so, this is a missed delegation opportunity — note what specific instruction or context (a direct FAQ answer, or a self-contained scripted sub-flow) would have let the Talker/front-end handle it without the round-trip.

**Example of Deep Analysis:**

Instead of just noting "Function failed, escalated to live agent," provide:
- **Problematic area**: send_itinerary_email_as_string function
- **Issue**: Customer provided email with obvious typo (user@gma8l.com instead of gmail.com). Function returned sent=false. GA immediately offered escalation instead of investigating.
- **Potential improvement**: Add error handling instructions to function definition: "If the function response is sent=false and the email appears to have a typo (common patterns: gma8l, gmial, yahooo, etc.), confirm with the customer whether they provided the correct email address before escalating."

This level of analysis helps developers understand not just what happened, but how to make GA better.
</objective>

<output>
## Output

### File Structure
- Use folder **analysis-output/** for your analysis
- Create an analysis results file per conversation in the format: `analysis-<conversation-id>.md`
- You might be asked to analyze a conversation that has been analyzed before, that's okay. Overwrite the file. But remember: your final summary should include ALL conversations in the analysis.

### Per-Conversation Analysis Format

For each turn, include a very brief analysis including:
- **Turn number and timestamps** (start and end)
- **Turn duration** (how long GA took to process and respond)
- **Time from previous turn** (how long the customer took to respond - not a delay)
- **Customer message(s)** and key context
- **GA's thoughts** (chain-of-thought reasoning)
- **Function calls** and their results (success/failure)
- **Bot response(s)**
- **Filler / time-buying phrase used** (if any), and whether that turn made a function call
- **Issues or observations** if any.

After all turns, provide:
- **Summary statistics**: Total turns, average turn duration, any concerning patterns
- **Filler analysis**: total filler/time-buying messages used, how many were NOT followed by any function call in the same turn (delegation opportunities), and for each opportunity: the customer's question, the filler used, what GA responded with, and a recommended fix — either (a) push the answer/knowledge directly into the Talker/front-end's own instructions so it can self-serve, or (b) delegate the surrounding multi-step flow to the Talker/front-end to run autonomously (e.g. a company-defined "Run Without Supervisor" journey) instead of round-tripping per step
- **Issue analysis**: Deep dive into problems with root cause, GA's response, and potential improvements
- **Overall assessment**: Healthy, suspicious, or unhealthy with clear reasoning

### Final Summary Table
At the end, provide a very short summary table of each conversation:
- **Columns:** Conversation ID, Status, Fillers (Opportunities), Notes
- **Status values:** Include an emoji:
  - ✅ for HEALTHY
  - ⚠️ for SUSPICIOUS
  - ❌ for UNHEALTHY
- **Fillers (Opportunities):** format as `total (opportunities)`, e.g. `5 (3)` meaning 5 filler/time-buying messages used, 3 of them with no function call in the same turn
- **Notes:** Keep them short
- **Format:** Even-spaced markdown table format
</output>

---

## Workflow

When `/analyze-conversation` is invoked:

1. Check for conversation files in expected locations or as specified by the user
2. If no files found, suggest using `/fetch-conversation` to fetch conversations from Athena first
3. Once files are available, confirm with the user which conversations to analyze
4. Proceed with detailed analysis for each conversation
5. Output results to `analysis_output/` folder

## Integration with /fetch-conversation

This command works seamlessly with `/fetch-conversation`:

**Example workflow:**
```
User: /fetch-conversation
[Provides: company-marker=mtagnostic1, conversation-id=CAb2bd05aa...]
[Output saved to: tools_output/athena_actions/mtagnostic1_CAb2bd05aa..._actions.json]

User: /analyze-conversation
[System checks tools_output/athena_actions/, finds the fetched conversation]
[Proceeds with analysis and outputs to analysis_output/]
```

Alternatively, users can specify the path directly:
```
User: /analyze-conversation tools_output/athena_actions/mtagnostic1_CAb2bd05aa..._actions.json
```

Or analyze a folder of conversations:
```
User: /analyze-conversation special_conversations/
```

---

Now identify which conversations to analyze based on the instructions above.