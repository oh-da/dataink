# Code Recipes — Library Themes That Comply by Construction

Start every generated chart from the matching theme below. Each encodes the DataInk defaults: no chart borders, no background fills, light-grey structure, horizontal text, direct labels over legends, grey baseline + one highlight, zero-baseline bars.

Highlight color: brand primary if `assets/brand-colors.md` is filled in, otherwise `#0072B2` (CVD-safe blue). Baseline grey for de-emphasized series: `#949494` (the lightest grey that passes the 3:1 non-text check on white); structure (axes, ticks): `#B0B0B0`; text: `#606060`.

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

HIGHLIGHT, BASELINE = "#0072B2", "#949494"
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
HIGHLIGHT, BASELINE = "#0072B2", "#949494"
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
    "bar": {"color": "#949494"},
    "line": {"color": "#949494"},
    "font": "sans-serif"
  }
}
```
Direct labels: add a `text` mark layer at the series' last point. Highlight one series with a conditional color: `{"condition": {"test": "datum.region === 'A'", "value": "#0072B2"}, "value": "#949494"}`. Bars: quantitative scale gets `"scale": {"zero": true}`.

## RTL text (Hebrew, Arabic)

Only the text is RTL — keep the geometry exactly as the themes above produce it: bars and time axes left-to-right, value axis on the left. Numbers are LTR in Hebrew too; never mirror the chart. What changes:

- **Title anchor moves right:** matplotlib `ax.set_title(..., loc="right")`; plotly `title=dict(x=1, xanchor="right")`; vega-lite `"title": {"anchor": "end"}`.
- **Glyph order is matplotlib-version-dependent** — run `check_rtl.py '<text>'` (see SKILL.md) for the current environment. The rule it encodes:

```python
import re, matplotlib
if tuple(int(x) for x in re.findall(r"\d+", matplotlib.__version__)[:2]) >= (3, 11):
    fix = lambda s: s                        # native bidi: pass logical order as-is
else:
    from bidi.algorithm import get_display   # pip install python-bidi
    fix = get_display
# wrap EVERY displayed string: ax.set_title(fix(title), loc="right"),
# tick labels, ax.set_ylabel(fix(...)), annotations
```

- **plotly / vega-lite / HTML:** pass strings as-is — browsers apply bidi natively. Never pre-reverse.
- **Font:** must have Hebrew/Arabic glyphs (matplotlib's default DejaVu Sans covers Hebrew; verify brand fonts).
- **Verify by rendering:** save a test image and read one label back. Correct: `ירושלים` — garbled: `םילשורי`.

## After generating

1. Verify colors: `check_contrast.py` and `check_palette.py` (see SKILL.md Step 6).
2. Add redundant encoding where color carries meaning (labels, markers, line styles).
3. Draft alt text for web/BI output.
4. Run the visualization-review skill (P0 checks at minimum).
