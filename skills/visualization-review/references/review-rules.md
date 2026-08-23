# Review Rules — P0 / P1 / P2

## P0 — Correctness, Integrity, Accessibility (blocking)

Any P0 failure means the visualization is misleading, incorrect, or inaccessible.

### 1. Chart-Task Mismatch
- Lines used for unordered categories (implies false continuity)
- Pie/donut used for precise comparisons or >5 categories
- Bar chart used for time-series when trend matters more than discrete values
- Histogram bins inconsistent or misleading
- **Fix:** suggest the correct chart type from the relationship → chart mapping.

### 2. Misleading Scales
- Bar chart baseline truncated above zero (distorts magnitude comparison)
- Inconsistent axes across small multiples (prevents valid comparison)
- Dual y-axes without explicit justification (cognitive tax obscures the message)
- Aspect ratio distorts trends (e.g., compressed time axis exaggerates slopes)
- **Fix:** reset baseline to zero, standardize axes, split into stacked charts, or adjust aspect ratio.

### 3. Color-Only Encoding
- Color is the sole way to distinguish categories or values
- Red/green used without redundant encoding (fails for ~8% of the male population)
- **Fix:** add labels, patterns, markers, or line styles. Switch to a CVD-safe palette.

### 4. Text Contrast Failures
- Text on background below WCAG AA (4.5:1 normal text; 3:1 large text ≥18pt or bold ≥14pt)
- **Fix:** darken text, lighten background, or switch colors. Compute the ratio with `scripts/check_contrast.py` — do not estimate.

### 5. Non-Text Contrast Failures
- Data marks (lines, bars, points) blend into background or adjacent colors (below 3:1)
- Thin lines on similar-colored backgrounds are invisible
- **Fix:** increase line weight, adjust colors, add markers. Verify with `scripts/check_contrast.py`.
- **Exception:** deliberately de-emphasized context series (highlight-one-grey-rest) may sit below 3:1 when the message-bearing marks pass and the context stays visible — note it under P2 polish, not as a P0 failure.

### 6. Missing Text Alternative
- Web/BI/report visual has no alt text for screen readers
- **Fix:** draft alt text describing the chart type, key data pattern, and primary insight — not a mechanical description of visual elements.

### 7. Reversed or Garbled RTL Text
- Hebrew/Arabic strings rendered in reversed glyph order (e.g., "םילשורי" instead of "ירושלים") — matplotlib < 3.11 without bidi processing, or bidi processing double-applied on >= 3.11
- **Fix:** follow the version-gated handling printed by `scripts/check_rtl.py`; re-render and read one label back. Chart geometry staying left-to-right is CORRECT for Hebrew — numbers are LTR — so do not "fix" axis direction.

## P1 — Perception, Cognitive Load, Narrative (strong warnings)

These reduce comprehension, slow interpretation, or weaken the message.

### 8. Low-Precision Encodings for Fine Comparisons
- Angle or area used where position or length would be more accurate
- Bubble chart for precise value comparison
- **Fix:** switch to bar chart, dot plot, or other position-based encoding.

### 9. Overplotting and Crowding
- Too many series on one chart (>5 lines, >15 bars); unreadable labels; dense scatterplot without transparency or jitter
- **Fix:** small multiples, filter/aggregate, highlight-one-grey-rest, transparency.

### 10. No Clear Takeaway
- Generic/descriptive title ("Q3 Sales") instead of insight-driven ("Sales dropped 12% after stockout"); no annotation; no focal point
- **Fix:** action title, annotate the key insight, apply the 10% highlighting rule.

### 11. Legend Dependence
- Separate legend used when ≤5 series could be directly labeled
- **Fix:** direct-label series; remove legend.

### 12. Unclear Units and Definitions
- Axes missing units; ambiguous time grain; undefined metrics ("active users"?)
- **Fix:** add unit labels, time grain notes, and metric definitions in subtitle or footnote.

### 13. Missing Uncertainty or Misleading Framing
- Causal claim implied from correlation without disclaimer; forecasts without confidence intervals; undisclosed metric definitions (cherry-picked denominators)
- **Fix:** trend-line caveats, confidence bands, definition footnotes. State what is measured and what is inferred.

## P2 — Style, Consistency, Polish (suggestions)

### 14. Inconsistent Design Tokens
- Mixed fonts, sizes, or colors across a multi-chart report or dashboard; different chart styles for similar data
- **Fix:** standardize on a single type hierarchy, palette, and chart style.

### 15. Excess Non-Data Ink
- Heavy gridlines, borders, background shading; decorative gradients, shadows, 3D effects; chartjunk
- **Fix:** strip to essentials; render structure in light grey; reserve visual weight for data.

### 16. Palette Misuse
- Rainbow/jet for sequential data; categorical palette for ordered data; >8 distinct colors without grouping
- **Fix:** perceptually uniform sequential (viridis/cividis) or appropriate categorical (Okabe-Ito); group small categories into "other."

### 17. Layout Issues
- Diagonal text; center-aligned elements; cramped layout; misaligned panels
- RTL (Hebrew/Arabic) titles or annotations anchored left, away from where reading starts
- **Fix:** horizontal text only, left-justify (right-justify RTL text), add margins, align chart edges.
