---
name: designing-dashboards
description: Designs effective dashboard layouts with KPI hierarchy, component selection, and attention choreography. Use when creating dashboards, designing KPI displays, laying out monitoring screens, building executive summary views, or choosing between dashboard components like sparklines, bullet graphs, and scorecards.
---

# Dashboard Design

-# Performance Notes
- A dashboard is not a collection of charts — it is a single-screen narrative.
- Prioritize the 5-second test: can you extract the headline insight within 5 seconds?

The user's request: "$ARGUMENTS"

## Critical Constraints
- **One screen:** A dashboard should fit on one screen without scrolling. If it doesn't, split into multiple views or add drill-down.
- **Accessibility:** WCAG AA contrast for all text and data marks. CVD-safe palettes. No color-only encoding.
- **No decorative elements:** No 3D, no gauges (use bullet graphs instead), no ornamental icons that don't encode data.
- Bar charts must have zero baselines. Sparklines need context (min/max/target).

## Workflow Checklist

Copy and track progress:

```
- [ ] Step 1: Define audience and purpose
- [ ] Step 2: Identify and rank KPIs
- [ ] Step 3: Select component types
- [ ] Step 4: Design layout with attention choreography
- [ ] Step 5: Apply branding, color, and accessibility
- [ ] Step 6: Validate with 5-second test
- [ ] Step 7: Generate output
```

## Instructions

### Step 1: Define Audience and Purpose
- **Who** will use this dashboard? (executive, analyst, operations, public)
- **How often** will they check it? (real-time monitoring, daily review, weekly summary)
- **What decision** does it support? (operational response, strategic planning, performance tracking)
- **What is the single most important question** this dashboard should answer?

### Step 2: Identify and Rank KPIs
- List all metrics the dashboard should display.
- Rank by importance: which 1-3 metrics answer the primary question from Step 1?
- Group remaining metrics as supporting context.
- Identify targets, thresholds, or benchmarks for each KPI.
- Consult `references/kpi-components.md` for component-to-metric matching.

### Step 3: Select Component Types
Match each metric to the right display component:
- **KPI tile + trend sparkline:** Single metric with context (current value, change, mini trend).
- **Bullet graph:** Single metric vs. target with qualitative ranges (good/satisfactory/poor).
- **Bar chart (sorted):** Comparison across categories or ranking.
- **Line chart:** Trend over time (limit to 3 series).
- **Heatmap / highlight table:** Large matrix patterns (time × category, region × metric).
- **Simple text:** Single critical number displayed prominently.
- Consult `references/kpi-components.md` for detailed guidance.

### Step 4: Design Layout with Attention Choreography
The layout determines what the viewer sees first, second, and third.
- **Top row:** Primary KPIs (the headline numbers). Large, prominent, left-aligned.
- **Middle zone:** Supporting charts that explain the headline numbers.
- **Bottom / right:** Detail tables, secondary metrics, or drill-down entry points.
- Use consistent alignment across all panels. Align chart edges, baselines, and text.
- Consult `references/layout-patterns.md` for layout templates.

### Step 5: Apply Branding, Color, and Accessibility
- Check for `../../assets/brand-colors.md` and `../../assets/brand-fonts.md`.
- Default to CVD-safe palette from `../../assets/accessible-palettes.md`.
- **Traffic light encoding:** If using red/amber/green, always pair with icons or labels (not color alone).
- **10% rule:** Highlight at most 10% of the dashboard surface. Alert states (red) should be the only vivid color.
- Ensure all text meets WCAG AA contrast (4.5:1).

### Step 6: Validate — 5-Second Test
Look at the dashboard for 5 seconds, then look away.
- Can you state the single most important insight?
- Do you know which KPIs are on-track vs. off-track?
- **If not:** Simplify. Increase primary KPI prominence. Reduce visual noise.
- **If yes:** Proceed.

### Step 7: Generate Output
Produce the dashboard layout/code in the user's preferred tool or format.

## Examples

**Example 1: Executive weekly summary**
- **User says:** "Design a dashboard for our weekly exec meeting showing revenue, churn, and pipeline."
- **Actions:**
  1. Audience: executives, weekly review, strategic decisions.
  2. KPIs ranked: Revenue (primary), Churn rate (secondary), Pipeline value (supporting).
  3. Components: KPI tile + sparkline for revenue, bullet graph for churn vs. target, sorted bar for pipeline by stage.
  4. Layout: Revenue tile top-left (largest), churn bullet top-right, pipeline bar chart middle row.
  5. Color: grey baseline, red only for churn exceeding threshold.

## Troubleshooting

**"Add more metrics — we need everything on one screen":**
Each additional metric dilutes attention on every other metric. Push less critical items to a drill-down view or secondary dashboard.

**"Use gauges for the KPIs":**
Gauges waste space and are hard to compare. Use bullet graphs — they encode the same information (value vs. target) in a compact, comparable form.
