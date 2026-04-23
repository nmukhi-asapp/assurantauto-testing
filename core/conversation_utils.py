"""
Utilities for merging and processing conversation data.

This module provides functions for merging voice conversation data from external
and internal sources (id and id_int conversations).
"""

import json
from pathlib import Path
from typing import Dict, List, Optional


def extract_conversation_id(filename: str) -> str:
    """
    Extract the conversation ID from filename, removing _int suffix if present.

    Example:
        platform::assurantauto::490879A9C04311F0960399B06691BFB2_int::.json
        -> 490879A9C04311F0960399B06691BFB2

    Args:
        filename: The filename to extract the conversation ID from

    Returns:
        The conversation ID without any _int suffix
    """
    # Remove platform prefix and .json suffix
    parts = filename.replace(".json", "").split("::")
    if len(parts) >= 3:
        convo_id = parts[2]
        # Remove _int suffix if present
        return convo_id.replace("_int", "")
    return filename


def load_json_file(filepath: Path) -> Dict:
    """
    Load and return JSON data from file.

    Args:
        filepath: Path to the JSON file

    Returns:
        Dictionary containing the JSON data
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(filepath: Path, data: Dict) -> None:
    """
    Save JSON data to file with proper formatting.

    Args:
        filepath: Path to save the JSON file
        data: Dictionary to save as JSON
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def sort_actions(actions: List[Dict]) -> List[Dict]:
    """
    Sort actions by timestamp.

    Args:
        actions: List of action dictionaries to sort

    Returns:
        Sorted list of actions by timestamp
    """
    sorted_actions = actions.copy()
    sorted_actions.sort(key=lambda x: x["timestamp"])
    return sorted_actions


def merge_actions(base_actions: List[Dict], int_actions: List[Dict]) -> List[Dict]:
    """
    Merge and sort actions from both base and internal files by timestamp.

    Args:
        base_actions: Actions from the base conversation file
        int_actions: Actions from the _int conversation file

    Returns:
        Combined and chronologically sorted list of actions
    """
    all_actions = base_actions + int_actions
    all_actions.sort(key=lambda x: x["timestamp"])
    return all_actions


def merge_conversation_data(base_data: Dict, int_data: Optional[Dict] = None) -> Dict:
    """
    Merge conversation data from base and internal sources.

    If only base_data is provided, returns the base data with sorted actions.
    If both are provided, merges the actions and returns combined data.

    Args:
        base_data: The base conversation data dictionary
        int_data: The internal conversation data dictionary (optional)

    Returns:
        Merged conversation data with sorted actions
    """
    # Start with base data structure
    merged_data = base_data.copy()

    if int_data is None:
        # Just sort the actions if no int data
        merged_data["model_input"]["actions"] = sort_actions(
            base_data["model_input"]["actions"]
        )
    else:
        # Merge actions from both sources
        base_actions = base_data["model_input"]["actions"]
        int_actions = int_data["model_input"]["actions"]
        merged_actions = merge_actions(base_actions, int_actions)
        merged_data["model_input"]["actions"] = merged_actions

        # Ensure external_conversation_id doesn't have _int suffix
        base_convo_id = base_data["model_input"]["external_conversation_id"]
        merged_data["model_input"]["external_conversation_id"] = base_convo_id.replace(
            "_int", ""
        )

    return merged_data


def merge_conversations_from_directory(
    input_dir: Path, output_dir: Path
) -> Dict[str, int]:
    """
    Merge conversation files from input directory and save to output directory.

    This function processes all JSON conversation files in the input directory,
    groups them by conversation ID, and merges paired base/_int files.

    Args:
        input_dir: Directory containing JSON conversation files
        output_dir: Directory to save merged conversation files

    Returns:
        Dictionary with statistics about the merge operation:
        - processed_count: Total conversations processed
        - merged_count: Number of merged (base + int) conversations
        - base_only_count: Number of base-only conversations
        - int_only_count: Number of int-only conversations
    """
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get all JSON files
    json_files = list(input_dir.glob("*.json"))

    # Group files by conversation ID
    conversations: Dict[str, Dict[str, Path]] = {}

    for filepath in json_files:
        filename = filepath.name
        convo_id = extract_conversation_id(filename)

        if convo_id not in conversations:
            conversations[convo_id] = {}

        # Determine if this is an _int file
        if "_int::" in filename:
            conversations[convo_id]["int"] = filepath
        else:
            conversations[convo_id]["base"] = filepath

    # Process each conversation
    stats = {
        "processed_count": 0,
        "merged_count": 0,
        "base_only_count": 0,
        "int_only_count": 0,
    }

    for convo_id, files in conversations.items():
        has_base = "base" in files
        has_int = "int" in files

        if has_base and has_int:
            # Merge both files
            base_data = load_json_file(files["base"])
            int_data = load_json_file(files["int"])
            merged_data = merge_conversation_data(base_data, int_data)

            # Extract company marker from filename
            base_filename = files["base"].name
            company_marker = (
                base_filename.split("::")[1] if "::" in base_filename else "unknown"
            )

            # Save merged file
            output_filename = f"platform::{company_marker}::{convo_id}::.json"
            output_path = output_dir / output_filename
            save_json_file(output_path, merged_data)

            stats["merged_count"] += 1

        elif has_base:
            # Copy base file only (with sorted actions)
            data = load_json_file(files["base"])
            merged_data = merge_conversation_data(data)

            # Extract company marker
            base_filename = files["base"].name
            company_marker = (
                base_filename.split("::")[1] if "::" in base_filename else "unknown"
            )

            output_filename = f"platform::{company_marker}::{convo_id}::.json"
            output_path = output_dir / output_filename
            save_json_file(output_path, merged_data)

            stats["base_only_count"] += 1

        elif has_int:
            # Copy int file only (clean up _int suffix and sort actions)
            data = load_json_file(files["int"])
            data["model_input"]["external_conversation_id"] = convo_id
            merged_data = merge_conversation_data(data)

            # Extract company marker
            int_filename = files["int"].name
            company_marker = (
                int_filename.split("::")[1] if "::" in int_filename else "unknown"
            )

            output_filename = f"platform::{company_marker}::{convo_id}::.json"
            output_path = output_dir / output_filename
            save_json_file(output_path, merged_data)

            stats["int_only_count"] += 1

        stats["processed_count"] += 1

    return stats
