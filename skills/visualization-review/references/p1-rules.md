# P1 Rules — Perception, Cognitive Load, Narrative

Strong warnings. These issues reduce comprehension, slow interpretation, or weaken the message.

## 7. Low-Precision Encodings for Fine Comparisons
- Angle or area used where position or length would be more accurate (e.g., pie chart for 4 similar-sized segments)
- Bubble chart for precise value comparison
- **Fix:** Switch to bar chart, dot plot, or other position-based encoding.

## 8. Overplotting and Crowding
- Too many series on one chart (>5 lines, >15 bars)
- Unreadable labels (overlapping, truncated, or too small)
- Dense scatterplot with no transparency or jitter
- **Fix:** Use small multiples, filter/aggregate, highlight-one-grey-rest, add transparency.

## 9. No Clear Takeaway
- Title is generic/descriptive ("Q3 Sales") instead of insight-driven ("Sales dropped 12% after stockout")
- No annotation highlighting the key pattern
- No focal point — all elements equally weighted
- **Fix:** Write an action title, annotate the key insight, apply the 10% highlighting rule.

## 10. Legend Dependence
- Separate legend used when ≤5 series could be directly labeled
- Reader must scan back and forth between legend and data
- **Fix:** Direct-label series. Remove legend.

## 11. Unclear Units and Definitions
- Axes missing units (currency? percentage? count?)
- Time grain ambiguous (daily? monthly? rolling average?)
- Metric not defined (what counts as "active users"?)
- **Fix:** Add unit labels, time grain notes, and metric definitions in subtitle or footnote.

## 12. Missing Uncertainty or Misleading Framing
- Chart implies causal claim from correlation without disclaimer
- Forecasts or projections shown without confidence intervals or caveats
- Metric definitions not disclosed (cherry-picked denominators)
- **Fix:** Add trend line caveats, confidence bands, definition footnotes. State what is measured and what is inferred.
