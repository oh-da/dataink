# Chart Selection Matrix

## Step 0: Table, Graph, or Simple Text?

Before choosing a chart type, determine the right medium:

- **Individual values needed → Table.** Reader scans rows/columns for specific numbers; best when precision matters. Use the table-design skill for structure, alignment, and formatting. Avoid tables in live presentations — they pull audiences into reading mode.
- **Patterns and comparisons → Graph.** Viewer perceives trends, clusters, and outliers pre-attentively; best when the message is in the relationships. Continue below.
- **Just 1–2 numbers → Simple text.** Display prominently with a supporting phrase. No chart wrapper needed.

## Relationship → Chart Mapping

Identify the data relationship first, then match to the appropriate visual form. This matrix is organized by Stephen Few's seven-category relationship taxonomy.

| Relationship | Primary charts | When to use alternatives |
|---|---|---|
| **Time-series** | Line graph, vertical bar chart | Line for trends; bars for discrete time points. Small multiples if >3 series |
| **Nominal comparison** | Bar chart (horizontal for long labels) | Dot plot / lollipop for many categories (higher data-ink) |
| **Ranking** | Sorted bar chart | Sort descending; horizontal bars for readability |
| **Part-to-whole** | Stacked bar, 100% stacked bar | Use sorted bar + "sums to 100%" title. Treemap for many segments (overview only) |
| **Deviation** | Bar chart or line + reference line at zero | Bars extend up/down from baseline; waterfall for sequential contributions |
| **Distribution** | Histogram, box plot | Violin/strip + box for technical audiences; quantile bands for mainstream |
| **Correlation** | Scatterplot | Add trend line with caveats; transparency/jitter for overplotting |

## Chart-Specific Rules

**Simple Text** — Use when you have 1-2 numbers. Display prominently with supporting phrase. No chart wrapper needed.

**Line Graphs** — Continuous data over time. Never use for categorical data. Limit to 3 series; beyond that, use small multiples or highlight-one-grey-rest.

**Slopegraphs** — Comparing exactly 2 time points across multiple categories. Filter to key series if label collisions occur.

**Bar Charts** — Zero baseline always. Horizontal for long labels. Sort by value unless a natural order exists.

**Stacked Bar Charts** — Segments above the first lack a shared baseline, reducing precision. For Likert/survey data, use 100% stacked horizontal bars.

**Waterfall Charts** — Decompose a total into sequential positive/negative contributions.

**Dot Plot / Lollipop** — Higher data-ink efficiency than bars for ranking many categories. Add clear baseline/reference line.

**Scatterplot** — Correlation, clusters, outliers. Add transparency/jitter for dense data. Annotate key points.

**Histogram** — Distribution of one continuous variable. Use consistent bin widths. Facet by group for comparisons.

**Box Plot** — Distribution comparison across groups. Non-technical audiences may misread — consider violin/strip overlay or quantile bands.

**Heatmap / Highlight Table** — Large matrix patterns. Use perceptually uniform sequential color scale. Provide legend. Allow sorting for pattern detection.

**Bullet Graph** — Single measure vs. target with qualitative ranges. Use for KPI dashboards instead of gauges.

**Treemap** — Part-to-whole with many nested segments. Area comparison is imprecise — prefer sorted bars for precision; treemap for overview + drill-down.

**Choropleth Maps** — Spatial patterns. Always normalize (per capita/area, not raw counts). Use sequential/diverging palettes. Note projection limitations.

## Visuals to Avoid

- **Pie / Donut:** Angle/area judgment is low-precision. If user insists: ≤5 slices, direct labels, sorted, and always suggest a bar chart alternative.
- **3D Graphics:** Distorts values with no analytical benefit.
- **Secondary Y-Axes:** Cognitive tax of mapping data to two scales. Use direct labels or split into stacked charts sharing the same x-axis.
- **Rainbow/Jet Palettes:** False perceptual boundaries, poor grayscale conversion. Use perceptually uniform scales.
