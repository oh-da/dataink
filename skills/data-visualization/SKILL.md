---
name: visualizing-data
description: Selects, designs, and refines data visualizations for clarity, accuracy, and accessibility. Use when choosing chart types, improving graphs, reducing clutter, applying brand colors, checking accessibility, or designing individual charts. Handles bar charts, line graphs, scatterplots, heatmaps, small multiples, and more.
---

# Data Visualization Expert

-# Performance Notes
- Take your time to do this thoroughly.
- Quality and accuracy are more important than speed.
- Do not skip validation steps.

The user's request: "$ARGUMENTS"

## Critical Constraints
- **Accessibility first:** Never use color as the sole encoding. Always pair with labels, patterns, or markers. Use CVD-safe palettes by default (see `../../assets/accessible-palettes.md`). Ensure WCAG AA contrast (4.5:1 text, 3:1 non-text marks).
- **Never** use 3D graphics or secondary (right-hand) y-axes.
- **Avoid** pie/donut charts. If the user insists, limit to ≤5 slices with direct labels, sorted by size, and suggest a sorted bar chart as the preferred alternative.
- Bar charts **must** have a zero baseline.
- Keep text horizontal — no diagonal labels.
- **Integrity:** Annotate uncertainty where applicable. Define metrics clearly. Do not imply causation from correlation.

## Workflow Checklist

Copy and track progress:

```
- [ ] Step 1: Determine medium (table vs. graph vs. simple text)
- [ ] Step 2: Choose chart type based on data relationship
- [ ] Step 3: Maximize data-ink ratio
- [ ] Step 4: Apply branding and color strategy
- [ ] Step 5: Focus attention — titles, annotations, hierarchy
- [ ] Step 6: Accessibility check
- [ ] Step 7: Validation — "where are your eyes drawn?"
- [ ] Step 8: Generate output
```

## Instructions

### Step 1: Determine the Medium
Decide if the data belongs in a table, graph, or simple text.
- Consult `references/medium-selection.md` for decision logic.

### Step 2: Choose the Chart Type
Match the data relationship to the appropriate visual form.
- Consult `references/chart-types.md` for the full selection matrix.

### Step 3: Maximize the Data-Ink Ratio
Strip non-data elements: borders, background fills, dense gridlines. Push axes and reference lines to light grey.
- Consult `references/design-principles.md` for application rules.

### Step 4: Apply Branding and Color Strategy
Check for brand assets before applying colors:
- **Look for** `../../assets/brand-colors.md` and `../../assets/brand-fonts.md`.
  - **If found:** Use the defined brand palette. Identify 1-2 brand-appropriate highlight colors; mute everything else.
  - **If not found:** Default to grey baseline + one vivid highlight color (blue). Use CVD-safe palette from `../../assets/accessible-palettes.md`.
- **10% rule:** Highlight at most 10% of the visual surface. Over-highlighting dilutes impact.

### Step 5: Focus Attention
- Write an **action title** (states the insight, not the topic).
- Label axes with units and time grain.
- Annotate the key pattern directly on the chart.
- Use direct labels instead of legends when ≤5 series.

### Step 6: Accessibility Check
- Verify color is not the only differentiator — add redundant encoding (labels, patterns, markers).
- Check contrast ratios: 4.5:1 for text, 3:1 for data marks against background.
- For web/BI output: draft alt text describing the chart's key insight.
- Consult `../../assets/accessible-palettes.md` if the current palette is not CVD-safe.

### Step 7: Validation
Run the "where are your eyes drawn?" test: look away, look back, note where your gaze lands.
- **If gaze hits the intended insight:** proceed.
- **If not:** return to Step 3 — reduce competing elements, strengthen the focal point, and re-check.

### Step 8: Generate Output
Produce the visualization in the user's preferred library or format, applying all design decisions from prior steps. If no preference is stated, ask or default to the most appropriate tool for the context.

## Examples

**Example 1: Applying Brand Colors**
- **User says:** "I want to compare revenue across regions, make it look good."
- **Actions:**
  1. Recommend a Horizontal Bar Chart for categorical comparison.
  2. Check `../../assets/brand-colors.md` — found, primary brand color is Forest Green.
  3. Make all baseline bars light grey; highlight the top-performing region in Forest Green.
  4. Ensure zero baseline, remove chart borders, verify contrast ratios.

## Troubleshooting

**Spaghetti graph (too many overlapping lines):**
- Highlight one key series in a vivid color, push the rest to grey.
- Or split into small multiples sharing the same axes.
