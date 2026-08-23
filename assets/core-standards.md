# Core Standards — Shared Rules for All DataInk Skills

These rules apply to every chart, dashboard, infographic, table, and report. Individual skills reference this file instead of restating them.

## Accessibility (non-negotiable)

- Never use color as the sole encoding — always pair with labels, patterns, markers, or position.
- WCAG AA contrast: **4.5:1** for text (3:1 for large text ≥18pt or bold ≥14pt); **3:1** for message-bearing data marks (the highlighted series, and every series in a chart with no de-emphasis) against background and adjacent colors.
- Deliberately de-emphasized context series (highlight-one-grey-rest) may sit below 3:1, but must stay clearly visible and must never be the only place the insight lives. Axis lines, ticks, and gridlines are structure, not data marks — keep them light. On white, `#949494` is the lightest grey that still passes 3:1, so use it for muted marks that carry meaning.
- Default to CVD-safe palettes — see `accessible-palettes.md`. Verify programmatically with `check_palette.py '#hex1,#hex2,...'` from the plugin's `scripts/` directory (each SKILL.md gives the exact invocation path).
- For web/BI/screen-reader contexts, draft alt text stating the chart type, key pattern, and primary insight.

## Integrity (non-negotiable)

- Bar charts always have a zero baseline.
- Never use 3D graphics or secondary (right-hand) y-axes.
- Avoid pie/donut charts. If the user insists: ≤5 slices, direct labels, sorted by size — and suggest a sorted bar chart as the preferred alternative.
- Annotate uncertainty where applicable. Define metrics clearly. Never imply causation from correlation.

## Emphasis and hierarchy

- **10% rule:** highlight at most 10% of the visual surface; mute everything else to grey. Over-highlighting = no highlighting.
- **Action titles:** state the insight ("Sales dropped 12% after stockout"), not the topic ("Q3 Sales").
- Direct-label series instead of legends when ≤5 series. Label axes with units and time grain.
- Horizontal text only — no diagonal labels. Left-justify text — no center alignment.

## Branding workflow

1. Check `brand-colors.md` and `brand-fonts.md` (this directory).
2. **If found:** use 1–2 brand highlight colors; mute everything else. If the brand color is too light against the background, substitute bold black or a complementary dark color.
3. **If not found:** grey baseline + one vivid highlight (blue), from the CVD-safe palettes in `accessible-palettes.md`.
4. Dark backgrounds reverse the contrast rules: dark baseline, white/bright highlights.

## Validation

- **"Where are your eyes drawn?" test:** look away, look back — your gaze must land on the intended insight first. If not, reduce competing elements and strengthen the focal point.
- Verify contrast deterministically with `check_contrast.py '#FG' '#BG'` from the plugin's `scripts/` directory (each SKILL.md gives the exact invocation path).
