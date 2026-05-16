#!/usr/bin/env python3
"""Fetch a specific conversation by ID from Athena."""

import json
import os
import sys
from pathlib import Path

# Add repo root to Python path (for core/ module)
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Add generative-agent-optimization-mcp to path (for data_sampling)
# Override with MCP_REPO_DIR env var if repos are not siblings of this repo
_default_mcp = project_root.parent / "generative-agent-optimization-mcp"
mcp_root = Path(os.environ.get("MCP_REPO_DIR", str(_default_mcp)))
sys.path.insert(0, str(mcp_root))

from generative_agent_optimization.data_sampling.get_historical_convos import (
    fetch_convo_turns_by_id,
)
from core.conversation_utils import merge_conversation_data

def fetch_voice_conversation(company_marker: str, conversation_id: str, team: str = "research"):
    """Fetch a voice conversation including both base and internal conversations."""

    print(f"Fetching voice conversation {conversation_id} for {company_marker}...")

    # For voice conversations, fetch both base and _int conversations
    base_id = conversation_id
    int_id = f"{conversation_id}_int"
    all_ids = [base_id, int_id]

    # Fetch the data
    convo_turns, df = fetch_convo_turns_by_id(
        company_marker=company_marker,
        conversation_ids=all_ids,
        team=team,
    )

    print(f"Fetched {len(convo_turns)} conversation parts")

    # Group conversations by base ID
    conversations_by_id = {}
    for turns in convo_turns:
        model_input = turns.to_model_input()
        external_id = model_input.external_conversation_id

        # Determine if this is an _int conversation
        is_int = external_id.endswith("_int")

        if base_id not in conversations_by_id:
            conversations_by_id[base_id] = {"base": None, "int": None}

        wrapped = {"model_input": model_input.model_dump()}

        if is_int:
            conversations_by_id[base_id]["int"] = wrapped
            print(f"  Found internal (reasoner) conversation: {external_id}")
        else:
            conversations_by_id[base_id]["base"] = wrapped
            print(f"  Found base (talker-customer) conversation: {external_id}")

    # Merge conversations
    if base_id in conversations_by_id:
        convos = conversations_by_id[base_id]
        if convos["base"] and convos["int"]:
            print("Merging both talker-customer and talker-reasoner conversations...")
            merged_data = merge_conversation_data(convos["base"], convos["int"])
        elif convos["base"]:
            print("Only base conversation found, no internal conversation available")
            merged_data = merge_conversation_data(convos["base"])
        elif convos["int"]:
            print("Only internal conversation found, no base conversation available")
            merged_data = merge_conversation_data(convos["int"])
            merged_data["model_input"]["external_conversation_id"] = base_id
        else:
            print("ERROR: No conversations found!")
            return None

        # Save to fetched_conversations/ inside this repo, regardless of cwd
        output_dir = str(project_root / "fetched_conversations")
        os.makedirs(output_dir, exist_ok=True)

        customer_id = merged_data["model_input"].get("customer_id", "")
        file_path = os.path.join(
            output_dir,
            f"platform::{company_marker}::{base_id}::{customer_id}.json",
        )

        with open(file_path, "w") as file:
            json.dump(merged_data, file, indent=2)

        print(f"\nSaved merged conversation to: {file_path}")

        # Print summary
        actions = merged_data["model_input"].get("actions", [])
        print(f"\nConversation Summary:")
        print(f"  Conversation ID: {base_id}")
        print(f"  Customer ID: {customer_id}")
        print(f"  Total actions: {len(actions)}")

        # Count message types
        message_count = sum(1 for a in actions if a.get("action_type") == "MESSAGE")
        llm_request_count = sum(1 for a in actions if a.get("action_type") == "LLM_REQUEST")
        print(f"  Messages: {message_count}")
        print(f"  LLM Requests: {llm_request_count}")

        return file_path
    else:
        print(f"ERROR: Conversation {base_id} not found!")
        return None

if __name__ == "__main__":
    # Configuration
    company_marker = "assurantauto"
    conversation_id = "4281067467-1309610481-2732102712-0825805307"
    team = "research"  # AWS team role for Athena queries (research, mleng, di, eng, product)

    result = fetch_voice_conversation(company_marker, conversation_id, team)

    if result:
        print(f"\n✅ Successfully fetched and saved conversation!")
        print(f"📁 File: {result}")
    else:
        print("\n❌ Failed to fetch conversation")
        sys.exit(1)
