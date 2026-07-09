---
name: dashboard-design
description: Designs dashboard layouts with KPI hierarchy, component selection, and attention choreography. Use when creating dashboards, KPI displays, monitoring screens, or executive summary views.
allowed-tools: Bash(python3 *)
---

# Dashboard Design

The user's request: "$ARGUMENTS"

A dashboard is not a collection of charts — it is a single-screen narrative that must pass the 5-second test.

## Critical Constraints

All shared rules in `../../assets/core-standards.md` apply. Dashboard-specific additions:
- **One screen:** no scrolling. If it doesn't fit, split into multiple views or add drill-down.
- **No gauges** — use bullet graphs. No ornamental icons that don't encode data.
- Sparklines need context (min/max/target). Traffic-light red/amber/green always pairs with icons or labels.

## Instructions

### Step 1: Define Audience and Purpose
Who uses it (executive, analyst, operations)? How often (real-time, daily, weekly)? What decision does it support? What is the single most important question it must answer?

### Step 2: Identify and Rank KPIs
List all metrics; rank by which 1–3 answer the primary question. Group the rest as supporting context. Identify targets, thresholds, or benchmarks for each.

### Step 3: Select Component Types
Match each metric to a component (KPI tile + sparkline, bullet graph, sorted bar, line ≤3 series, heatmap, simple text) using `references/kpi-components.md`.

### Step 4: Design Layout with Attention Choreography
Top row: primary KPIs, large and left-aligned. Middle: supporting charts. Bottom/right: detail tables and drill-down. Align all panel edges and baselines. Use the templates in `references/layout-patterns.md`.

### Step 5: Apply Branding, Color, and Accessibility
Follow the branding workflow in `../../assets/core-standards.md`. On dashboards, alert states (red) should be the only vivid color. Verify contrast deterministically:
```bash
python3 "${CLAUDE_SKILL_DIR}/../../scripts/check_contrast.py" '#FG' '#BG'
python3 "${CLAUDE_SKILL_DIR}/../../scripts/check_palette.py" '#hex1,#hex2,...'
```

### Step 6: Validate — 5-Second Test
Look for 5 seconds, look away. Can you state the headline insight and which KPIs are off-track? If not: simplify, enlarge primary KPIs, cut noise.

### Step 7: Generate Output
Produce the layout/code in the user's preferred tool. After generating, run the visualization-review skill on the output (P0 checks at minimum).

## Troubleshooting

**"Add more metrics — we need everything on one screen":** each added metric dilutes attention on every other metric. Push less critical items to a drill-down or secondary view.

**"Use gauges for the KPIs":** gauges waste space and resist comparison. Bullet graphs encode the same information (value vs. target) in a compact, comparable form.
