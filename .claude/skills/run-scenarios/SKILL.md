---
description: Run E2E scenario tests for a company, wait for completion, generate an HTML report, and classify failures.
arguments:
  - name: args
    description: "Format: <company-marker> [--branch <gacs-branch>] [--tags <tag>] [--output <dir>] — all optional except company-marker"
---

# Run Scenarios End-to-End

Run voice E2E scenarios for a company, monitor completion, generate an HTML report, and classify any failures.

## Step 1: Parse Arguments

Parse `$ARGUMENTS` to extract:
- `company-marker` (required, first positional arg, e.g. `assurantauto`)
- `--branch` (optional GACS branch, default: `draft`)
- `--tags` (optional tag filter, default: `e2e`)
- `--output` (optional output dir, default: `customer-scenario-outputs/<company-marker>/e2e_full_<YYYYMMDD>`)

Infer the scenarios directory as `customer-scenarios/<company-marker>/E2E`.

## Step 2: Run the Scenarios

All commands must be run from the `voice-genagent` repo. Set `VOICE_GENAGENT_DIR` in your `.env` if it is not at `~/code/voice-genagent`. Always prepend `env -u ALL_PROXY -u all_proxy` to avoid proxy interference.

**Try running this yourself first:**

```bash
_VG=${VOICE_GENAGENT_DIR:-$HOME/code/voice-genagent}
cd "$_VG" && env -u ALL_PROXY -u all_proxy poetry run python -m tools.scenario_runner.run voice \
  customer-scenarios/<company-marker>/E2E \
  --voice-provider vapi \
  --tr \
  --chunk 10 \
  --tags <tags> \
  --gacs-branch <branch> \
  --output <output-dir>
```

If the command fails (permission error, module not found, network error), present the exact command to the user and ask them to run it from their terminal, then wait for them to confirm it's running.

## Step 3: Identify Missing or Failed Scenarios

While the run is in progress or after it completes, check which scenarios are missing from the output vs. the scenario files. Run this Python script to find gaps:

```python
import json, os, glob, re

results_dir = '<output-dir>'
scenarios_dir = 'customer-scenarios/<company-marker>/E2E'

# Collect expected scenario IDs from YAML files (e2e-tagged only)
scenario_ids = []
for yaml_file in glob.glob(f'{scenarios_dir}/**/*.yaml', recursive=True):
    with open(yaml_file) as f:
        content = f.read()
    if '<tags>' not in content:
        continue
    m = re.search(r'^id:\s*(.+)', content, re.MULTILINE)
    if m:
        scenario_ids.append(m.group(1).strip())

# Collect ran IDs and check for errors
ran_ids = set()
errored = []
for result_dir in glob.glob(f'{results_dir}/*-run_0'):
    name = os.path.basename(result_dir).replace('-run_0', '')
    ran_ids.add(name)
    results_file = os.path.join(result_dir, 'results.json')
    if os.path.exists(results_file):
        with open(results_file) as f:
            r = json.load(f)
        if r.get('scenario_execution_status') != 'completed' and r.get('scenario_execution_status') != 'success':
            errored.append(name)

missing = [s for s in scenario_ids if s not in ran_ids]
print(f'Total expected: {len(scenario_ids)}, Ran: {len(ran_ids)}, Missing: {len(missing)}, Errored: {len(errored)}')
for m in missing:
    print(f'  MISSING: {m}')
for e in errored:
    print(f'  ERRORED: {e}')
```

Find the YAML file for each missing scenario and re-run it individually:

```bash
_VG=${VOICE_GENAGENT_DIR:-$HOME/code/voice-genagent}
cd "$_VG" && env -u ALL_PROXY -u all_proxy poetry run python -m tools.scenario_runner.run voice \
  <path-to-scenario.yaml> \
  --voice-provider vapi \
  --tr \
  --gacs-branch <branch> \
  --output <output-dir>
```

Run each missing scenario file as a separate command (the `file` argument only accepts one path at a time).

## Step 4: Monitor Completion

Periodically check if the run has finished by counting `state.json` files in the output directory:

```bash
find <output-dir> -name "state.json" | wc -l
```

Compare to the expected total. Re-check every few minutes. When the count matches expected (or stops growing), the run is complete.

## Step 5: Generate the HTML Report

Once all scenarios have completed, generate the HTML report using the **system Python** (not poetry) to avoid proxy issues:

```bash
env -u ALL_PROXY -u all_proxy python3 \
  generate_report.py \
  <output-dir> \
  --output customer-scenario-outputs/<company-marker>/draft_<YYYYMMDD>_report.html
```

Report the path of the generated HTML file to the user.

## Step 6: Classify Failures and Identify Improvements

Read each `results.json` in the output directory. For every failed evaluation rule (where `passed` is `false`), collect:
- Scenario ID
- The failed rule text
- The conversation context (from `simulated_conversation` in results.json or `state.json`)

Then classify each failure into one of three categories:

### (a) Better Instructions
The agent had the right capability but applied it incorrectly, missed a step, used wrong wording, or didn't follow a protocol. Fix: update the GACS task instructions.

Signs:
- Agent did something reasonable but not quite right
- Agent missed an explicit step in the task instructions
- Agent used a disallowed phrase or omitted a required one
- Agent escalated when it shouldn't, or vice versa

### (b) Improved Mocks
The agent tried to call a function but got an unexpected response because the mock in the scenario YAML wasn't set up for that call path.

Signs:
- Agent called a function not listed in `mock_responses`
- Agent called a function with parameters that didn't match any mock `params` pattern
- API returned a failure/empty response that caused the agent to stall or loop

### (c) Fixes in Evaluation Rules
The agent actually behaved correctly but the evaluation rule was too strict, ambiguous, or tested the wrong thing.

Signs:
- The rule uses phrasing that doesn't match what the agent said, but the intent was satisfied
- The rule tests an intermediate step that the agent achieved via a different valid path
- The applicability condition didn't fire when it should have (or fired when it shouldn't)
- The rule is checking something the scenario didn't actually set up

---

Present the classification as a table:

| Scenario | Failed Rule | Category | Suggested Fix |
|----------|------------|----------|---------------|
| ...      | ...        | (a/b/c)  | ...           |

Prioritize category (b) fixes first (mocks are easy wins), then (a), then (c).
