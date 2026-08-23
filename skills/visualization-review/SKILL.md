---
name: visualization-review
description: Critiques and improves existing data visualizations using a prioritized rule system (P0 accessibility and integrity, P1 clarity, P2 polish). Use when reviewing charts, auditing dashboards, checking accessibility compliance, or identifying anti-patterns.
allowed-tools: Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_contrast.py" *), Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_palette.py" *)
---

# Visualization Review

The user's request: "$ARGUMENTS"

Reviews existing visualizations (images, code, or descriptions) against the prioritized rule system in `references/review-rules.md`:
- **P0 (must-fix):** correctness, integrity, and accessibility failures that mislead or exclude.
- **P1 (strong warning):** perception, cognitive load, and narrative issues that reduce effectiveness.
- **P2 (polish):** style, consistency, and aesthetics.

Be systematic — check every rule at each level. Cite specific elements; always suggest concrete fixes, not just problems.

## Instructions

### Step 1: Receive the Visualization
Identify: what data relationship is communicated? Who is the audience? What medium (slide, report, dashboard, web)?

### Step 2: Run P0 → P1 → P2 Checks
Work through `references/review-rules.md` in priority order. Any P0 failure is a blocking issue.

For contrast and palette rules (P0 rules 4–5), verify deterministically when colors are known — do not eyeball:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_contrast.py" '#FG' '#BG'
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_palette.py" '#hex1,#hex2,...'
```

When the input is an image, first sample the actual hex values (title and label text, data marks, background) from the image, then run the scripts on those values. If the colors cannot be determined, report rules 4-5 as "not verified" instead of guessing a verdict.

### Step 3: Generate Report
Prioritized: P0 issues first with specific fixes, then P1 with suggested redesigns, then P2 polish suggestions. If a level is clean, state "No issues found."

### Step 4: Apply Fixes (if requested)
Apply the report's recommendations following the design rules in the data-visualization skill (`../data-visualization/references/design-principles.md` and `../../assets/core-standards.md`). Re-run the relevant checks afterward to verify resolution.

## Example

**User says:** "Review this dashboard for issues."
1. Examine the image systematically.
2. P0: pie chart with 12 slices (chart-task mismatch); red/green encoding with no labels (color-only).
3. P1: generic titles ("Q3 Sales" instead of insight-driven); legend-dependent line chart with 3 series.
4. P2: inconsistent font sizes across panels.
5. Report with specific fixes for each issue.
