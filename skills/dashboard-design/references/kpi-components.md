# KPI Component Selection

Match each metric type to the most effective dashboard component.

## Component Guide

**KPI Tile + Sparkline**
- Shows: current value, period-over-period change, mini trend line.
- Use for: headline metrics (revenue, active users, NPS).
- Design: large number + small delta indicator + sparkline showing recent trend. Include context: min, max, or target line on the sparkline.

**Bullet Graph**
- Shows: single measure vs. target, with qualitative ranges (poor/satisfactory/good).
- Use for: goal tracking (quota attainment, SLA compliance, budget utilization).
- Design: horizontal bar with comparative marker (target) and background bands. Much more space-efficient and comparable than gauges.

**Bar Chart (Sorted)**
- Shows: comparison or ranking across categories.
- Use for: revenue by product, headcount by department, pipeline by stage.
- Design: sorted descending. Horizontal for long labels. Zero baseline always.

**Line Chart**
- Shows: trend over time.
- Use for: daily/weekly/monthly metric trends.
- Design: limit to 3 series. Beyond that, use small multiples or highlight-one-grey-rest. Add reference lines for targets or thresholds.

**Heatmap / Highlight Table**
- Shows: patterns across two dimensions.
- Use for: performance by region × time, feature usage by segment, risk matrices.
- Design: perceptually uniform sequential palette. Provide legend. Allow sorting.

**Simple Text**
- Shows: one critical number.
- Use for: the single most important metric when it stands alone (e.g., "99.97% uptime").
- Design: large font, supporting context phrase, no chart wrapper.

## When NOT to Use

- **Gauges / dials:** Waste space, hard to compare, imprecise. Use bullet graphs instead.
- **Pie charts on dashboards:** Space-inefficient, imprecise. Use sorted bars.
- **3D charts:** No analytical benefit, distorts values.
