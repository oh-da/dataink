# P0 Rules — Correctness, Integrity, Accessibility

These are blocking issues. Any P0 failure means the visualization is misleading, incorrect, or inaccessible.

## 1. Chart-Task Mismatch
- Lines used for unordered categories (implies false continuity)
- Pie/donut used for precise comparisons or >5 categories
- Bar chart used for time-series when trend matters more than discrete values
- Histogram bins are inconsistent or misleading
- **Fix:** Suggest the correct chart type from the relationship → chart mapping.

## 2. Misleading Scales
- Bar chart baseline truncated above zero (distorts magnitude comparison)
- Inconsistent axes across small multiples (prevents valid comparison)
- Dual y-axes without explicit justification (cognitive tax obscures the message)
- Aspect ratio distorts trends (e.g., compressing time axis exaggerates slopes)
- **Fix:** Reset baseline to zero, standardize axes, split into stacked charts, or adjust aspect ratio.

## 3. Color-Only Encoding
- Color is the sole way to distinguish categories or values
- Red/green used without redundant encoding (fails for ~8% of male population)
- **Fix:** Add labels, patterns, markers, or line styles. Switch to CVD-safe palette.

## 4. Text Contrast Failures
- Text on background below WCAG AA threshold (4.5:1 for normal text, 3:1 for large text ≥18pt or bold ≥14pt)
- **Fix:** Darken text, lighten background, or switch colors. Compute contrast ratio.

## 5. Non-Text Contrast Failures
- Data marks (lines, bars, points) blend into background or adjacent colors (below 3:1 ratio)
- Thin lines on similar-colored backgrounds are invisible
- **Fix:** Increase line weight, adjust colors, add markers.

## 6. Missing Text Alternative
- Web/BI/report visual has no alt text for screen readers
- **Fix:** Draft alt text that describes the chart type, key data pattern, and primary insight — not a mechanical description of visual elements.
