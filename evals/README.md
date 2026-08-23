# DataInk Evals

Behavioral eval scenarios for the six skills. The deterministic checks in
`tests/run_checks.py` guard the parts a script can verify (contrast math,
cross-references, hook behavior); these cases guard the parts only a model
run can verify — that each skill actually produces what it promises.

## Format

`cases.json` holds one case per skill:

- **prompt** — what to ask, with the relevant skill invoked (`/dataink:<skill>` or auto-triggered).
- **must** — every item must be satisfied by the output for the case to pass.
- **must_not** — any item present fails the case.

## Running

Manually: run each prompt in a Claude Code session with the plugin installed,
then score the transcript against the checklist. Judge items on substance,
not wording — "sorted bar chart" passes however it is phrased or coded.

LLM-judged: paste the case's prompt output together with its `must` /
`must_not` lists and ask a model to return pass/fail per item with a quoted
justification for each. Fail the case on any unjustified pass.

## When to run

- Before a release that changes any SKILL.md, shared asset, or reference file.
- After renaming skills or restructuring references (alongside `tests/run_checks.py`).
- When adding a new skill: add a case here in the same shape first.
