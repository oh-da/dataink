# Code Recipes — Library Themes That Comply by Construction

Start every generated chart from the matching theme below. Each encodes the DataInk defaults: no chart borders, no background fills, light-grey structure, horizontal text, direct labels over legends, grey baseline + one highlight, zero-baseline bars.

Highlight color: brand primary if `assets/brand-colors.md` is filled in, otherwise `#0072B2` (CVD-safe blue). Baseline grey: `#B0B0B0`; text/axes grey: `#606060`.

## matplotlib

```python
import matplotlib.pyplot as plt

DATAINK = {
    "figure.facecolor": "white", "axes.facecolor": "white",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.spines.left": False,                      # y-gridline-free charts keep bottom spine only
    "axes.edgecolor": "#B0B0B0", "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.titlelocation": "left", "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.labelcolor": "#606060", "axes.labelsize": 10,
    "xtick.color": "#606060", "ytick.color": "#606060", "xtick.labelsize": 10, "ytick.labelsize": 10,
    "text.color": "#333333",
    "legend.frameon": False,                        # prefer direct labels via ax.annotate / ax.text
    "font.family": "sans-serif",
}
plt.rcParams.update(DATAINK)

HIGHLIGHT, BASELINE = "#0072B2", "#B0B0B0"
# usage: color the key series HIGHLIGHT, all others BASELINE;
# action title: ax.set_title("Sales dropped 12% after stockout", loc="left")
# direct labels: ax.text(x[-1], y[-1], "Region A", color=HIGHLIGHT, va="center")
# bars: ax.bar(...); ax.set_ylim(bottom=0)   # zero baseline, always
```

## plotly

```python
import plotly.graph_objects as go

DATAINK_LAYOUT = dict(
    template="none",
    plot_bgcolor="white", paper_bgcolor="white",
    font=dict(family="sans-serif", color="#333333", size=13),
    title=dict(x=0, xanchor="left", font=dict(size=16)),   # left-aligned action title
    xaxis=dict(showgrid=False, linecolor="#B0B0B0", ticks="outside",
               tickcolor="#B0B0B0", tickfont=dict(color="#606060"), tickangle=0),
    yaxis=dict(showgrid=False, linecolor="#B0B0B0", rangemode="tozero",  # zero baseline
               tickfont=dict(color="#606060")),
    showlegend=False,        # direct-label with annotations instead
    margin=dict(l=60, r=120, t=60, b=40),  # right margin for end-of-line labels
)
HIGHLIGHT, BASELINE = "#0072B2", "#B0B0B0"
# fig = go.Figure(layout=DATAINK_LAYOUT)
# direct label: fig.add_annotation(x=..., y=..., text="Region A", showarrow=False,
#                                  font=dict(color=HIGHLIGHT), xanchor="left")
```

## vega-lite

```json
{
  "config": {
    "background": "white",
    "view": {"stroke": null},
    "axis": {
      "domainColor": "#B0B0B0", "tickColor": "#B0B0B0",
      "labelColor": "#606060", "titleColor": "#606060",
      "grid": false, "labelAngle": 0
    },
    "title": {"anchor": "start", "fontSize": 16, "fontWeight": "bold", "color": "#333333"},
    "legend": {"disable": true},
    "bar": {"color": "#B0B0B0"},
    "line": {"color": "#B0B0B0"},
    "font": "sans-serif"
  }
}
```
Direct labels: add a `text` mark layer at the series' last point. Highlight one series with a conditional color: `{"condition": {"test": "datum.region === 'A'", "value": "#0072B2"}, "value": "#B0B0B0"}`. Bars: quantitative scale gets `"scale": {"zero": true}`.

## After generating

1. Verify colors: `check_contrast.py` and `check_palette.py` (see SKILL.md Step 6).
2. Add redundant encoding where color carries meaning (labels, markers, line styles).
3. Draft alt text for web/BI output.
4. Run the visualization-review skill (P0 checks at minimum).
