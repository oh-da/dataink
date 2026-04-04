# Design Principles — Application Rules

These are the opinionated application rules for data visualization design. They specify how to apply well-known design principles to chart-making decisions.

## Data-Ink Ratio
- Strip: chart borders, background fills, dense gridlines, decorative gradients.
- De-emphasize: render axes, tick marks, and reference lines in light grey.
- Context-sensitive: strict for analytic/decision charts; slightly looser for public-facing infographics where memorability matters.

## Grouping and Labeling
- Position data labels directly beside their marks — eliminate legend-scanning when ≤5 series.
- Color-code labels to match their corresponding marks.
- Remove unnecessary borders and boxes — the viewer perceives chart boundaries through closure.
- Use subtle background shading to group related elements (e.g., actual vs. forecast).

## Hierarchy and Focus
- **10% rule:** Highlight at most 10% of the visual. Over-highlighting = no highlighting.
- Make the key number physically large.
- Place the most important message in the top-left zone (Z-pattern reading).
- Use bold color sparingly for the focal point; mute everything else to grey.

## Layout
- Left-justify all text (titles, labels, annotations) — no center alignment.
- No diagonal text — horizontal always.
- Use white space intentionally — generous margins draw attention to content.

## Validation: "Eyes Drawn" Test
Look away, look back. Where does your gaze land?
- **First:** Should be the key insight.
- **Second:** Should be the supporting context.
- **Third:** Should be the structural elements (axes, labels).
- **If wrong:** Return to the design and reduce competing elements.
