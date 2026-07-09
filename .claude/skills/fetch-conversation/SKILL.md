---
description: Fetch conversation data from Athena using the data-sampling MCP server
---

Fetch conversation data from Athena using the generative-agent-optimization-mcp data-sampling server.

## Context

This skill fetches conversation logs from Athena using the `fetch_conversations_by_id` MCP tool, which provides:
- Efficient querying via the data-sampling MCP server
- Support for optional human agent utterances (from prod_docausal chatmessage table)
- Automatic interleaving of human agent and GenAgent messages chronologically
- CSV and JSON output formats

## Usage

When the user requests to fetch a conversation:

1. **Parse the request** to determine:
   - Company marker (required) - e.g., assurantauto
   - Conversation ID(s) (required) - one or more conversation IDs to fetch
   - Include human agent utterances (optional) - defaults to false
   - Save individual conversation files (optional) - defaults to false
   - Is voice (optional) - defaults to false (set to true to fetch _int variants for voice data)

2. **Fetch the conversation** using the MCP tool:
   ```
   mcp__data-sampling__fetch_conversations_by_id(
     company_marker='assurantauto',
     conversation_ids=['<conversation_id>'],
     include_human_agent_utterances=true,  # optional
     save_conversations=true               # optional
   )
   ```

## Parameters

- `company_marker`: The company marker (e.g., assurantauto, mtagnostic1, jetblue)
- `conversation_ids`: List of conversation IDs to fetch
- `include_human_agent_utterances` (optional): Boolean, default False. If True, fetches and interleaves human agent - customer utterances from chatmessage table
- `save_conversations` (optional): Boolean, default False. If True, saves individual conversation JSON files
- `is_voice` (optional): Boolean, default False. If True, fetches both base and _int variants for voice data
- `team` (optional): AWS team role, defaults to "eng". Must be one of: research, mleng, di, eng, product
- `output_dir` (optional): Output directory for results, defaults to data/sampled_convos

## Output

The tool generates:
- **CSV file**: `assurantauto_specific_conversations.csv` containing turn-by-turn conversation data
- **JSON files** (if save_conversations=True): Individual conversation files in format `platform::assurantauto::<conversation_id>::<customer_id>.json`

The CSV/JSON contains:
- `payload__company_id__company_marker`: Company identifier
- `payload__external_conversation_id__id`: Conversation ID
- `payload__actions`: JSON-encoded array of conversation actions
- Human agent utterances (if requested): Synthetic GA-shaped actions with `action_id` prefix "message::HA"

## Examples

**Example 1: Fetch single conversation**
```
fetch_conversations_by_id(
    company_marker='assurantauto',
    conversation_ids=['2744210576-1101730289-2550584737-0188171332'],
    save_conversations=true
)
```

**Example 2: Fetch with human agent utterances**
```
fetch_conversations_by_id(
    company_marker='assurantauto',
    conversation_ids=['2744210576-1101730289-2550584737-0188171332'],
    include_human_agent_utterances=true,
    save_conversations=true
)
```

**Example 3: Fetch multiple conversations**
```
fetch_conversations_by_id(
    company_marker='assurantauto',
    conversation_ids=['conv_id_1', 'conv_id_2', 'conv_id_3'],
    save_conversations=true
)
```

**Example 4: Fetch voice data (with _int variants)**
```
fetch_conversations_by_id(
    company_marker='assurantauto',
    conversation_ids=['conv_id'],
    is_voice=true,
    save_conversations=true
)
```

## Important Notes

- Requires AWS credentials and VPN access for Athena queries
- The MCP server uses team-based access control:
  - For GA logs: uses `team` parameter (defaults to "eng")
  - For human agent utterances: uses `DATA_SAMPLING_UTTERANCES_TEAM` env var (defaults to "di-prod-sso-utterances")
- Human agent utterances are only available for conversations that escalated to human agents
- Synthetic human agent actions are created with timestamps matching the chatmessage records
- Output files are stored in `data/sampled_convos/` by default (in generative-agent-optimization-mcp directory)

## Integration with /analyze-conversation

After fetching conversations, analyze them using `/analyze-conversation`:

**Typical workflow:**
1. Fetch conversation(s): `/fetch-conversation` → outputs CSV and JSON files
2. Analyze the fetched conversation(s): `/analyze-conversation` → reads and analyzes the data

## Human Agent Utterances Feature

When `include_human_agent_utterances=true`:
- Queries prod_docausal chatmessage table for human agent messages
- Creates synthetic GA-formatted actions for each human agent utterance
- Interleaves them chronologically with GenAgent actions
- Preserves all metadata and timestamps
- Works seamlessly for escalated conversations

This allows complete conversation analysis including both the GenAgent phase and the human agent handoff phase.