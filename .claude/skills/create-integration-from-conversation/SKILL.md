---
description: Fetch a real conversation from Athena and convert it into an integration test case for talker prompt testing.
arguments:
  - name: args
    description: "Format: <company-marker> <conversation-id> [--profile-team <team>] [--csv <path>] — followed by a description of what to test"
---

# Create Integration Test from Real Conversation

You are creating an integration test case from a real production conversation fetched from Athena.

## Step 1: Parse Arguments

Parse `$ARGUMENTS` to extract:
- `company-marker` (required, first positional arg)
- `conversation-id` (required, second positional arg)
- `--profile-team` (optional, default: "mleng")
- `--csv` (optional, path to pre-downloaded CSV file)
- Everything after the flags is the **test description**: what behavior to test and where to cut the conversation.

Example invocations:
```
/create-integration-from-conversation broadway17 01JKC4T970DK6AWF1KFBAX8PR8 Customer gets frustrated after long wait — test empathy in time-buying phrase
/create-integration-from-conversation jetblue 01ABC123 --csv path/to/data.csv Customer says they don't need anything else — test wrap-up protocol
```

## Step 2: Fetch the Conversation

Run the fetch script from the generative-agent repository:

```bash
cd /Users/mmarucco/Documents/Repositories/generative-agent && \
poetry run python tools/fetch_convo_from_athena/fetch_convo_from_athena.py \
  --company-marker <company-marker> \
  --conversation-id <conversation-id> \
  [--filename-csv <csv-path>] \
  [--profile-team <team>]
```

The script outputs a JSON file to `tools_output/athena_actions/<company-marker>_<conversation-id>_actions.json`.

Read that output file. The conversation is in `model_input.actions[]` — an array of ModelAction objects sorted by timestamp.

## Step 3: Understand the Conversation

Each ModelAction has a `type` field. The relevant types and their mapping to the integration test format are:

| ModelAction type     | Test item type          | Notes                                                    |
|----------------------|-------------------------|----------------------------------------------------------|
| `message`            | `message`               | Has `sender` (customer/agent/bot/system) → map to `role` (user/assistant/assistant/system). Has `text`. |
| `function_request`   | `function_call`         | Has `name` → `function_name`, `arguments` → `args`, generate a `call_id`.  |
| `function_response`  | `function_call_output`  | Match `call_id` to the preceding `function_request`.     |
| `instructions`       | `reasoner_response`     | The Supervisor/Reasoner instructions. Has `text`.        |
| `barge_in`           | `barge_in`              | Customer interrupted. Include as `{"type": "barge_in"}`. |
| `enter_task`         | *(skip)*                | Internal routing — do not include.                       |
| `llm_request`        | *(skip)*                | Internal — do not include.                               |
| `thought`            | *(skip)*                | Internal reasoning — do not include.                     |
| `greg_response`      | *(skip)*                | Internal — do not include.                               |

Sender mapping for `message` type:
- `customer` → `"role": "user"`
- `agent` or `bot` → `"role": "assistant"`
- `system` → `"role": "system"` (usually skip these unless they contain relevant reasoner instructions)

Display a summary of the full conversation to the user showing turn numbers and content so they can confirm the cut point.

## Step 4: Prune the Conversation

Based on the user's test description, identify the right cut point. Rules:
- **Always cut so the last item is a customer message** (`"role": "user"`). The test evaluates what the assistant does NEXT.
- Remove all items after the cut point.
- Remove system messages that are not reasoner instructions.
- Remove any `enter_task`, `llm_request`, `thought`, and `greg_response` actions.
- Keep the conversation coherent — include the welcome message, the customer's initial request, and all relevant back-and-forth up to the cut point.
- If the conversation has function calls, make sure each `function_call` has a matching `function_call_output` (except possibly the very last one if it's after the cut).

## Step 5: Determine Test Metadata

Based on the user's description, determine:

1. **Test name**: snake_case, descriptive, concise (e.g., `empathy_time_buying_long_wait`, `skip_ack_short_answer`)
2. **Description**: One sentence explaining what behavior is being tested.
3. **Tags**: Always include `"should_pass"` and `"prompt_best_practices"`. Add relevant behavior tags like:
   - `"tone_matching"` — for emotional tone tests
   - `"acknowledgment_skip"` — for ack skip scenarios
   - `"empathy_phrases"` — for empathy-related tests
   - `"wrap_up"` — for end-of-conversation tests
   - `"derailing"` — for topic change tests
   - `"clarification"` — for unclear input tests
   - Or create a new descriptive tag if none fit.
4. **company_marker**: Use the one from the fetched conversation.
5. **input_variables**: Include `"taskName"` if the conversation has an `enter_task` action (use its task name). Check existing test cases for the company's typical input variables.

## Step 6: Write Evaluation Rules

Create 2-4 specific, testable rules based on what the test description says. Rules should:
- Be phrased as assertions about what the assistant SHOULD or SHOULD NOT do.
- Be specific enough that an LLM evaluator can judge pass/fail.
- Reference the prompt guidelines being tested.

Examples:
- `"The assistant does NOT use a positive prefix like 'Great!', 'Perfect!', or 'Awesome!' before its time-buying response."`
- `"The assistant uses a neutral or empathetic time-buying phrase appropriate for a customer reporting a problem."`
- `"The assistant calls send_customer_request_or_update() to notify the Supervisor that the customer doesn't need further assistance."`
- `"The assistant proceeds to ask the next question without a lengthy preamble."`

## Step 7: Generate the Test Case JSON

Assemble the final JSON in this exact format:

```json
{
    "settings": {
        "name": "<test_name>",
        "description": "<description>",
        "tags": ["should_pass", "prompt_best_practices", "<behavior_tag>"]
    },
    "company_marker": "<company_marker>",
    "input_variables": {
        "taskName": "<TaskName>"
    },
    "conversation_items": [
        {
            "type": "message",
            "role": "assistant",
            "text": "..."
        },
        {
            "type": "message",
            "role": "user",
            "text": "..."
        },
        {
            "type": "function_call",
            "function_name": "send_customer_request_or_update",
            "args": {
                "customer_request_or_update": "..."
            },
            "call_id": "call-001"
        },
        {
            "type": "function_call_output",
            "call_id": "call-001"
        },
        {
            "type": "reasoner_response",
            "text": "..."
        }
    ],
    "rules": [
        "Rule 1...",
        "Rule 2..."
    ]
}
```

Ask the user to confirm the test name and suggest a target directory. Default: `integration_test_cases/talker_prompt_best_practices/`.

Write the file to `<target_directory>/<test_name>.json`.

## Important Notes

- Use `call-001`, `call-002`, etc. for `call_id` values (sequential).
- For `function_call_output`, only include `type` and `call_id` (no output content — the test framework handles this).
- The `text` in messages should be cleaned up from raw transcription artifacts but keep the natural spoken style (this is voice, not chat).
- If the conversation uses a different `send_customer_request_or_update` argument format, preserve it as-is from the original.
- Do NOT include any conversation items after the final customer message — the test evaluates the assistant's next response.
