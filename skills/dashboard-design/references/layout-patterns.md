# Dashboard Layout Patterns

## Attention Choreography

The layout controls the viewing sequence. Design it deliberately.

**Z-Pattern:** Viewers of left-to-right languages scan top-left → top-right → bottom-left → bottom-right. Place the most critical information in the top-left.

**Inverted Pyramid:** Most important first (top), supporting detail below, drill-down at the bottom. Matches how busy users consume dashboards — many will only see the top row.

## Layout Templates

### Template 1: KPI Summary (Executive)
```
┌──────────┬──────────┬──────────┐
│  KPI #1  │  KPI #2  │  KPI #3  │  ← Primary metrics (tiles + sparklines)
├──────────┴──────────┴──────────┤
│         Supporting Chart        │  ← Chart explaining the KPIs
├────────────────┬────────────────┤
│  Detail Chart  │  Detail Table  │  ← Drill-down context
└────────────────┴────────────────┘
```

### Template 2: Operational Monitor
```
┌──────────────────────────────────┐
│        Alert Banner (if any)      │  ← Only visible when threshold breached
├──────────┬──────────┬─��──────────┤
│  Status  │  Status  │   Status   │  ← Bullet graphs (metric vs. target)
├──────────┴──────────┴────────────┤
│          Trend Over Time          │  ← Line chart with threshold lines
├──────────────────────────────────┤
│         Detail Table / Log        │  ← Recent events or breakdowns
└──────────────────────────────────┘
```

### Template 3: Comparison Dashboard
```
┌──────────────────────────────────┐
│        Headline Comparison        │  ← Sorted bar chart (primary ranking)
├────────────────┬─────────────────┤
│  Small Mult 1  │  Small Mult 2   │  ← Faceted views of same metric
├────────────────┴─────────────────┤
│          Heatmap / Table          │  ← Cross-dimensional detail
└──────────────────────────────────┘
```

## Spacing and Alignment Rules

- **Consistent gutters** between all panels (8-16px or equivalent).
- **Align chart edges** across columns — misaligned edges create visual noise.
- **Left-align** all text elements within panels.
- **One screen:** If the user must scroll, the dashboard is too dense. Split or add drill-down.
