---
name: creating-infographics
description: Designs the layout, color strategy, and narrative structure of data-driven infographics. Use when creating infographics, visual summaries, one-page data reports, or combining multiple data points into a single visual.
allowed-tools: Bash(python3 *)
---

# Infographic Creator

The user's request: "$ARGUMENTS"

## Critical Constraints

All shared rules in `../../assets/core-standards.md` apply. Infographic-specific additions:
- An infographic **must** tell a cohesive, structured story — not a disjointed collection of facts.
- No fluffy designs, garish oversized numbers, or cartoonish graphics. Infographics must inform.
- **Memorability tradeoff:** for public-facing infographics where recall matters more than precision, selective embellishment (icons, distinctive forms) is acceptable — but data encodings (bar lengths, positions, slopes) must remain accurate.

## Instructions

### Step 1: Understand Context and Storyboard
Articulate the "3-minute story" — the narrative distilling the "so-what." Storyboard with a beginning, middle, and end; chunk related facts. Use the context-capture framework in `references/audience-context.md`.

### Step 2: Choose Displays and Maximize Data-Ink
Simple text for 1–2 key numbers, zero-baseline bars for comparisons, lines for trends. Strip clutter. Apply the hierarchy rules in `../data-visualization/references/design-principles.md`.

### Step 3: Apply Branding and Color
Follow the branding workflow in `../../assets/core-standards.md` (brand assets, light-color substitution, dark-background reversal, 10% rule).

### Step 4: Focus Attention and Apply Text
Use preattentive attributes (color, size, position) to guide the audience through the storyboard. One insight per panel, action title per chart, annotations next to the data, consistent margins.

### Step 5: Accessibility Check
Verify deterministically — do not eyeball contrast:
```bash
python3 "${CLAUDE_SKILL_DIR}/../../scripts/check_contrast.py" '#FG' '#BG'
python3 "${CLAUDE_SKILL_DIR}/../../scripts/check_palette.py" '#hex1,#hex2,...'
```
Add redundant encoding; draft alt text per panel for web output.

### Step 6: Validate
Run the "where are your eyes drawn?" test on each panel and the whole. If the gaze misses the focal point, return to Step 4.

### Step 7: Generate Output
Produce the infographic in the user's preferred format. After generating, run the visualization-review skill on the output (P0 checks at minimum).

## Troubleshooting

**"Make it cool with 3D elements and lots of graphics":** 3D skews data. Offer strategic brand colors, clean alignment, and quality typography instead.

**Overwhelming and chaotic:** revert to the 10% rule — only the single most important data point per section gets the highlight color.
