# AssurantAuto — Testing & Analysis

This repo hosts E2E scenarios, conversation analysis, and iterative-improvement
tooling for the AssurantAuto GenerativeAgent voice agent. See `README.md` for
setup, dependencies, and per-skill usage.

## GenerativeAgent ADRs

For any work involving GenerativeAgent design decisions, task-instruction
interpretation, scenario design, conversation analysis, or task routing,
consult the ADRs at:

  `../generative-agent/asapp/generative_agent/tools/workbench/docs/adrs/`

(Assumes `generative-agent` is a sibling of this repo. Override via the
`GENERATIVE_AGENT_DIR` env var if it lives elsewhere.)

Read the relevant ADR before recommending changes in these areas — design
rationale lives there, not in code comments. Skim the file index first to
find what's applicable, then read the specific ADR(s) in full.
