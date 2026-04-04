---
name: creating-infographics
description: Designs the layout, color strategy, and narrative structure of data-driven infographics. Use when creating infographics, designing visual summaries, combining multiple data points into a single visual, applying brand guidelines to informational graphics, or building one-page data reports.
---

# Infographic Creator

-# Performance Notes
- Take your time to do this thoroughly.
- Quality and accuracy are more important than speed.
- Do not skip context evaluation, storyboarding, or brand-checking steps.

The user's request: "$ARGUMENTS"

## Critical Constraints
- An infographic **must** tell a cohesive, structured story — not a disjointed collection of facts.
- **Avoid** fluffy designs, garish oversized numbers, or cartoonish graphics. Infographics must inform.
- **Never** use 3D graphics or secondary y-axes.
- **Avoid** pie/donut charts. If the user insists, limit to ≤5 slices with direct labels.
- **Accessibility:** Never rely on color alone. Ensure WCAG AA contrast (4.5:1 text, 3:1 non-text). Use CVD-safe palettes by default.
- **Integrity:** Define metrics clearly. Annotate uncertainty. Do not imply causation from correlation.
- **Memorability tradeoff:** For public-facing infographics where recall matters more than precision, selective embellishment (icons, distinctive forms) is acceptable — but data encoding must remain accurate and unambiguous.

## Workflow Checklist

Copy and track progress:

```
- [ ] Step 1: Understand context and storyboard
- [ ] Step 2: Choose displays and maximize data-ink
- [ ] Step 3: Apply branding and color strategy
- [ ] Step 4: Focus attention, apply text and annotations
- [ ] Step 5: Accessibility check
- [ ] Step 6: Validation
- [ ] Step 7: Generate output
```

## Instructions

### Step 1: Understand Context and Storyboard
Before choosing charts or colors, articulate the "3-minute story" — the concise narrative distilling the "so-what."
- Create a visual outline (storyboard) with a clear beginning, middle, and end.
- Group related facts into chunks to avoid overwhelming the audience.
- Consult `references/audience-context.md` for the context-capture framework.

### Step 2: Choose Displays and Maximize Data-Ink
- Select appropriate displays: Simple Text for 1-2 key numbers, Bar Charts (zero baseline) for comparisons, Line Graphs for trends.
- Strip clutter: remove borders, background shading, heavy gridlines, diagonal text.
- For public-facing infographics: allow recognizable icons and selective embellishment that aid memorability, but ensure data encodings (bar lengths, positions, line slopes) remain accurate.

### Step 3: Apply Branding and Color Strategy
Check for brand assets before applying colors:
- **Look for** `../../assets/brand-colors.md` and `../../assets/brand-fonts.md`.
  - **If found:** Use the defined brand palette.
  - **If not found:** Default to clean sans-serif typography and grey baseline with blue highlights. Use CVD-safe palettes from `../../assets/accessible-palettes.md`.
- **10% rule:** Highlight at most 10% of the visual surface.
- **Mute the baseline:** Soft, neutral colors for non-essential elements.
- **Contrast:** If the brand color is too light on the background, use bold black or a complementary dark color instead.
- **Dark backgrounds:** Reverse the contrast rules — black baseline, white/bright highlights.

### Step 4: Focus Attention and Apply Text
- Use preattentive attributes (color, size, position) to guide the audience through the storyboard.
- Every chart gets an **action title** (states the insight).
- Annotate key data points directly next to the data.
- Structure as panels: 1 insight per panel, consistent margins, icon slot, caption slot.

### Step 5: Accessibility Check
- Verify color is not the sole differentiator — add labels, patterns, or markers.
- Check contrast ratios: 4.5:1 for text, 3:1 for data marks.
- For web output: draft alt text for each visual panel.
- Consult `../../assets/accessible-palettes.md` if the palette is not CVD-safe.

### Step 6: Validation
Run the "where are your eyes drawn?" test on each panel and the infographic as a whole.
- **If gaze hits the intended focal point:** proceed.
- **If not:** return to Step 4 — reduce competing elements, strengthen the focal point, and re-check.

### Step 7: Generate Output
Produce the infographic in the user's preferred format, applying all design decisions from prior steps.

## Examples

**Example 1: Infographic with a light brand color**
- **User says:** "Turn these 5 regional sales stats into an infographic. Use our brand files."
- **Actions:**
  1. Check `../../assets/brand-colors.md` — found, primary is light yellow on white.
  2. Contrast problem: use bold black for highlights instead of light yellow.
  3. Grey baseline bars, cohesive narrative flow, action titles per panel.
  4. Accessibility: verify contrast ratios, add redundant encoding.

## Troubleshooting

**"Make it cool with 3D elements and lots of graphics":**
Advise that 3D skews data. Suggest strategic brand colors, clean alignment, and quality typography instead.

**Overwhelming and chaotic:**
Revert to the 10% rule. Push more to muted baseline. Only the single most important data point per section gets the highlight color.
