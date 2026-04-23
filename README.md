# AssurantAuto — Testing & Analysis

This repository contains everything needed to run E2E scenario tests, analyze production conversations, and iteratively improve the AssurantAuto GenAgent voice agent.

It is designed to be used with **Claude Code** (the ASAPP-configured CLI), which provides AI-assisted workflows via Claude skills and MCP tool servers.

---

## Contents

```
assurantauto-testing/
├── scenarios/E2E/              # 87 E2E scenario YAML definitions (by caller type)
│   ├── contract_holder/        #   customer journeys (mechanical, claim status, etc.)
│   ├── repair_facility/        #   repair shop journeys
│   ├── dealership/             #   dealer journeys
│   └── edge_cases/             #   edge cases & safety scenarios
├── scenario-runs/              # Stored runs from the past week (no model_input.json)
│   ├── e2e_full_20260420/      #   full E2E run, Apr 20
│   ├── e2e_full_20260421/      #   full E2E run, Apr 21
│   ├── e2e_full_20260423/      #   full E2E run, Apr 23
│   └── sandbox_random_20260423/ #  random sandbox sample, Apr 23
├── reports/                    # Pre-generated HTML reports for stored runs
├── scripts/
│   ├── fetch_conversation.py   # Fetch a production conversation from Athena
│   └── generate_report.py      # (also at repo root — canonical location)
├── generate_report.py          # Generate HTML report from a scenario run directory
├── core/                       # Shared utilities (conversation merging, etc.)
├── .claude/
│   ├── settings.json           # MCP server permissions + pre-approved commands
│   └── skills/                 # Claude Code slash commands (see Skills section)
├── .mcp.json                   # MCP server definitions (point to optimization-mcp)
└── .env-sample                 # Environment variable template
```

---

## Prerequisites

### 1. Dependent repositories

Clone these three repos — they can live anywhere on your machine:

| Repo | Purpose |
|------|---------|
| `voice-genagent` | Scenario runner (`tools/scenario_runner/`) |
| `generative-agent-optimization-mcp` | MCP server implementations (scenarios, GACS, data-sampling, prompt-renderer) |
| `generative-agent-time-inspector` | Timing analysis library used by `generate_report.py` |

```bash
git clone git@github.com:ASAPPinc/voice-genagent.git
git clone git@github.com:ASAPPinc/generative-agent-optimization-mcp.git
git clone git@github.com:ASAPPinc/generative-agent-time-inspector.git
```

### 2. Python environments

**voice-genagent** uses Poetry + Python 3.10:
```bash
cd /path/to/voice-genagent
pyenv install 3.10.x          # if not already installed
poetry install
```

**generative-agent-optimization-mcp** uses `uv`:
```bash
cd /path/to/generative-agent-optimization-mcp
uv sync
```

### 3. Environment variables

```bash
cp .env-sample .env
```

Edit `.env` and fill in at minimum:
- `LITELLM_API_KEY` — from 1Password ("LiteLLM")
- `VAPI_API_KEY` — for voice scenario runner
- `OPENAI_API_KEY` — alternative voice provider (optional)

**If your repos are not all in the same parent directory**, also set the path variables. By default every tool assumes the three repos above are siblings of this repo (i.e. `../voice-genagent`, `../generative-agent-optimization-mcp`, `../generative-agent-time-inspector`). If yours are elsewhere, uncomment and set these in `.env`:

```bash
MCP_REPO_DIR="/your/path/to/generative-agent-optimization-mcp"
VOICE_GENAGENT_DIR="/your/path/to/voice-genagent"
TIME_INSPECTOR_DIR="/your/path/to/generative-agent-time-inspector"
GENERATIVE_AGENT_DIR="/your/path/to/generative-agent"   # only needed for chat conversation fetching
```

These env vars are read by `generate_report.py`, `scripts/fetch_conversation.py`, `.mcp.json`, and the Claude skills — so setting them once in `.env` covers everything.

The `.env` file is gitignored — never commit it.

### 4. AWS credentials

Most tools require AWS SSO access (Athena queries, GACS config fetching):

```bash
aws sso login --profile dev-sso-gen-agent-ro
```

Your `~/.aws/config` must have the `dev-sso-gen-agent-ro` profile. Ask a teammate for the SSO configuration if you don't have it.

### 5. Claude Code

Install Claude Code and open this repo as the working directory:

```bash
npm install -g @anthropic-ai/claude-code   # or follow ASAPP internal install docs
cd ~/code/assurantauto-testing
claude
```

The `.mcp.json` and `.claude/settings.json` files are picked up automatically.

---

## Running Scenarios

### With Claude (recommended)

From within a Claude Code session in this repo:

```
/run-scenarios assurantauto --branch draft
```

This will:
1. Run all `e2e`-tagged scenarios against the `draft` GACS branch
2. Save results to `scenario-runs/<run-name>/`  *(note: this writes to the voice-genagent repo's output dir by default — see skill for details)*
3. Generate an HTML report
4. Classify any failures

Options: `--branch <name>` (default: `draft`), `--tags <tag>` (default: `e2e`), `--output <dir>`

### Manually (without Claude)

Run from the **voice-genagent** repo root (set `VOICE_GENAGENT_DIR` in `.env` if it's not a sibling of this repo):

```bash
_VG=${VOICE_GENAGENT_DIR:-$(dirname $(pwd))/voice-genagent}
cd "$_VG"
env -u ALL_PROXY -u all_proxy \
  poetry run python tools/scenario_runner/run.py voice \
    /path/to/assurantauto-testing/scenarios/E2E \
    --tr \
    --voice-provider vapi \
    --chunk 10 \
    --tags e2e \
    --gacs-branch draft \
    --output /path/to/assurantauto-testing/scenario-runs/e2e_full_$(date +%Y%m%d)
```

### Generating an HTML report

```bash
# From this repo root:
python3 generate_report.py scenario-runs/e2e_full_20260423 \
    --output reports/e2e_full_20260423_report.html

open reports/e2e_full_20260423_report.html
```

The report includes per-scenario pass/fail status, turn timelines, dead-air analysis, and links to individual scenario details.

---

## Inspecting Production Conversations

### With Claude

```
/inspect-conversation 2209534218-1045828081-2391966186-2917985560 assurantauto
```

This fetches the conversation from Athena, merges the talker+reasoner parts, and provides an interactive Q&A about what the agent did.

### Manually

Edit `scripts/fetch_conversation.py` — set `company_marker` and `conversation_id` at the bottom, then:

```bash
uv run python scripts/fetch_conversation.py
```

The merged JSON is saved to `fetched_conversations/platform::assurantauto::<id>::<customer-id>.json`.

> **Note:** fetched conversations may contain PII and are gitignored.

---

## Analyzing Conversations

```
/analyze-conversation
```

Analyzes conversation files in `fetched_conversations/` or a path you specify. Detects issues like Jinja rendering failures, empty instructions, wrong task routing, Single Question Rule violations, and escalation flow problems.

---

## Iterative Improvement (sim-and-improve)

```
/sim-and-improve
```

Runs iterative test-improve cycles: simulate conversations, analyze results, identify issues, apply prompt/code fixes, and repeat. Useful for rapid iteration on specific failure modes before running a full E2E suite.

---

## Claude Skills Reference

Skills are slash commands available in Claude Code sessions. They are defined in `.claude/skills/`.

| Skill | Command | What it does |
|-------|---------|-------------|
| **run-scenarios** | `/run-scenarios assurantauto [--branch <b>]` | Run E2E voice scenarios, generate report, classify failures |
| **inspect-conversation** | `/inspect-conversation <id> assurantauto` | Fetch + analyze a specific production conversation |
| **analyze-conversation** | `/analyze-conversation` | Batch analyze conversation files for issues |
| **sim-and-improve** | `/sim-and-improve` | Iterative simulate → analyze → fix cycles |
| **create-integration-from-conversation** | `/create-integration-from-conversation` | Convert a production conversation into an integration test case |

---

## MCP Tools Reference

MCP tools are used by Claude automatically during skill execution. They are served by the `generative-agent-optimization-mcp` repo.

| Server | Key tools |
|--------|-----------|
| `scenarios` | Run voice/chat simulations, evaluate results, aggregate metrics |
| `gacs` | Fetch task instructions, diff branches, compare configurations |
| `data-sampling` | Sample and fetch conversations from Athena |
| `genagent-prompt-renderer` | Render Jinja prompt templates, analyze prompt evolution |

MCP servers are configured in `.mcp.json` and require the `generative-agent-optimization-mcp` repo to be present at `~/code/generative-agent-optimization-mcp`.

---

## Scenario File Format

Scenarios are YAML files in `scenarios/E2E/`. Each file defines a scripted customer conversation:

```yaml
id: e2e_journey1_basic_mechanical_repair
name: "Journey 1: Basic Mechanical Repair Claim"
tags: [e2e]
company_marker: assurantauto
gacs_branch: draft
voice_provider: vapi

turns:
  - customer: "Hi, I'm calling about my warranty claim"
    expected:
      - contains: "contract number"
  - customer: "My contract number is 12345678"
    ...
```

To add a new scenario, copy an existing YAML from the same category and adjust. Use `tags: [e2e]` for scenarios to be included in full runs, or a custom tag for targeted subsets.

---

## Stored Scenario Runs

The `scenario-runs/` directory contains results from the past week. Each run directory has:

```
scenario-runs/<run-name>/
├── summary.json                    # Pass/fail counts, scenario list
└── <scenario-id>-run_0/
    ├── results.json                # Evaluation scores and pass/fail per criterion
    ├── state.json                  # Full conversation state (actions, variables)
    └── index.html                  # Per-scenario HTML report
```

> **`model_input.json` is excluded** from this repo (too large; regenerate by re-running the scenario).

Pre-generated HTML reports are in `reports/`. To regenerate from stored runs:

```bash
python3 generate_report.py scenario-runs/e2e_full_20260423 \
    --output reports/e2e_full_20260423_report.html
```

---

## Key AssurantAuto Context

- **Company marker**: `assurantauto` (prod), `assurantauto-sandbox` (sandbox)
- **Agent type**: Voice, Talker-Reasoner (TR) architecture — two LLMs cooperating
  - **Talker**: handles speech, manages customer interaction
  - **Reasoner**: decides what to do, calls APIs, selects tasks
- **GACS branch for active development**: `draft` (or branch-specific: `bobby`, `CarRentalInquiry-Chat`, etc.)
- **Production deployment**: `3f079f65-0788-456c-8a5b-558a57a6edf6`
- **Caller types**: Contract Holder, Repair Facility (RF), Dealership — each has distinct task flows
- **Key tasks**: CallerIdentification, ContractHolderIssues, RepairFacilityIssues, DealershipIssues, and subtasks for claims, payments, escalation

---

## Troubleshooting

**`ImportError` when running `generate_report.py`**
The script needs the `generative-agent-time-inspector` repo. Set `TIME_INSPECTOR_DIR=/your/path/to/generative-agent-time-inspector` in `.env`.

**AWS authentication failures**
Run `aws sso login --profile dev-sso-gen-agent-ro` and try again.

**Scenario runner fails with proxy errors**
Always prepend `env -u ALL_PROXY -u all_proxy` to scenario runner commands.

**MCP server not starting**
Ensure `uv sync` has been run in `generative-agent-optimization-mcp`. If the repo is not a sibling of this one, set `MCP_REPO_DIR` in `.env`.

**`fetch_conversation.py` fails with import errors**
Run from this repo root with `uv run python scripts/fetch_conversation.py`. If `generative-agent-optimization-mcp` is not a sibling repo, set `MCP_REPO_DIR` in `.env`.
