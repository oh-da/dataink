---
name: reviewing-visualizations
description: Critiques and improves existing data visualizations using a prioritized rule system. Use when reviewing charts, auditing dashboards, checking accessibility compliance, identifying anti-patterns, improving visualization effectiveness, or giving feedback on graphs and data displays.
---

# Visualization Review

-# Performance Notes
- Be thorough and systematic — check every rule at each priority level.
- Cite specific elements when flagging issues.
- Always suggest concrete fixes, not just problems.

The user's request: "$ARGUMENTS"

## How This Skill Works

This skill reviews existing visualizations (images, code, or descriptions) against a prioritized rule system. Issues are categorized by severity:

- **P0 (must-fix):** Correctness, integrity, and accessibility failures that mislead or exclude.
- **P1 (strong warning):** Perception, cognitive load, and narrative clarity issues that reduce effectiveness.
- **P2 (polish):** Style, consistency, and aesthetic issues.

## Workflow Checklist

Copy and track progress:

```
- [ ] Step 1: Receive and understand the visualization
- [ ] Step 2: Run P0 checks (correctness, integrity, accessibility)
- [ ] Step 3: Run P1 checks (perception, cognitive load, narrative)
- [ ] Step 4: Run P2 checks (style, consistency, polish)
- [ ] Step 5: Generate prioritized report with fixes
- [ ] Step 6: Apply fixes (if requested)
```

## Instructions

### Step 1: Receive the Visualization
Examine the visualization — image, code output, or description. Identify:
- What data relationship is being communicated?
- Who is the intended audience?
- What medium is this for (slide, report, dashboard, web)?

### Step 2: P0 Checks — Correctness, Integrity, Accessibility
Consult `references/p0-rules.md` and check for:
- Chart-task mismatch (e.g., line for unordered categories, pie for precise comparisons)
- Misleading scales (truncated bar baselines, inconsistent axes, unjustified dual axes)
- Color-only encoding (no redundant labels/patterns/markers)
- Text contrast failures (< 4.5:1 for normal text, < 3:1 for large text)
- Non-text contrast failures (data marks blending into background, < 3:1)
- Missing text alternative for web/BI/screen-reader contexts

**Any P0 failure must be flagged as a blocking issue.**

### Step 3: P1 Checks — Perception, Cognitive Load, Narrative
Consult `references/p1-rules.md` and check for:
- Low-precision encodings used for fine comparisons (angle/area where position/length is available)
- Overplotting / crowding (too many series, unreadable labels)
- No clear takeaway (generic title, no annotation, no highlighted pattern)
- Legend dependence when direct labels would reduce search (≤5 series)
- Unclear units, time grain, or metric definitions
- Missing uncertainty annotation where applicable
- Implied causation from correlation without disclaimer

### Step 4: P2 Checks — Style, Consistency, Polish
Consult `references/p2-rules.md` and check for:
- Inconsistent design tokens across a report/dashboard (fonts, colors, spacing)
- Excess non-data ink (heavy gridlines, borders, decorative gradients)
- Palette misuse (rainbow for sequential data, categorical palette for ordered data)
- Diagonal text or center-aligned elements
- Poor white space usage

### Step 5: Generate Report
Produce a prioritized report:
1. List all P0 issues first with specific fix recommendations.
2. List P1 issues with suggested redesigns.
3. List P2 issues as polish suggestions.
4. If no issues found at a level, state "No issues found."

### Step 6: Apply Fixes
If the user requests fixes, apply them following the recommendations from the report. Re-run the relevant checks after applying fixes to verify resolution.

## Examples

**Example 1: Reviewing a dashboard screenshot**
- **User says:** "Review this dashboard for issues."
- **Actions:**
  1. Examine the image systematically.
  2. P0: Flag a pie chart with 12 slices (chart-task mismatch), red/green encoding with no labels (color-only).
  3. P1: Flag generic titles ("Q3 Sales" instead of insight-driven), legend-dependent line chart with 3 series.
  4. P2: Flag inconsistent font sizes across panels.
  5. Report with specific fixes for each issue.
