---
name: data-visualization
description: Selects, designs, and refines data visualizations for clarity, accuracy, and accessibility. Use when choosing chart types, improving graphs, reducing clutter, applying brand colors, or designing individual charts.
allowed-tools: Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_contrast.py" *), Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_palette.py" *)
---

# Data Visualization Expert

The user's request: "$ARGUMENTS"

## Critical Constraints

All shared rules in `../../assets/core-standards.md` apply — accessibility (no color-only encoding, WCAG AA contrast, CVD-safe palettes), integrity (zero-baseline bars, no 3D, no dual y-axes, avoid pies), the 10% highlighting rule, and action titles. Read that file before designing.

## Instructions

### Step 1: Determine the Medium
Table, graph, or simple text — use the decision logic at the top of `references/chart-types.md`. If a table is the right medium, switch to the table-design skill.

### Step 2: Choose the Chart Type
Match the data relationship to the visual form using the selection matrix in `references/chart-types.md`.

### Step 3: Maximize the Data-Ink Ratio
Strip non-data elements (borders, background fills, dense gridlines); push axes and reference lines to light grey. Apply the rules in `references/design-principles.md`.

### Step 4: Apply Branding and Color
Follow the branding workflow in `../../assets/core-standards.md`: brand assets if present, otherwise grey baseline + one CVD-safe highlight.

### Step 5: Focus Attention
Action title, axis units and time grain, annotate the key pattern directly on the chart, direct labels instead of legends (≤5 series).

### Step 6: Accessibility Check
Verify deterministically — do not eyeball contrast:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_contrast.py" '#FG' '#BG'
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_palette.py" '#hex1,#hex2,...'
```
Add redundant encoding where color carries meaning; draft alt text for web/BI output.

### Step 7: Validate
Run the "where are your eyes drawn?" test (see core-standards). If the gaze misses the insight, return to Step 3.

### Step 8: Generate Output
Produce the chart in the user's preferred library, starting from the matching theme in `references/code-recipes.md` (matplotlib, plotly, vega-lite) so defaults comply by construction. After generating, run the visualization-review skill on the output (P0 checks at minimum).

## Troubleshooting

**Spaghetti graph (too many overlapping lines):** highlight one key series in a vivid color and push the rest to grey, or split into small multiples sharing the same axes.
