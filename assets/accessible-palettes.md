# Accessible Color Palettes

Default color palettes for color-vision-deficiency (CVD) safety and WCAG compliance. Use these when no brand palette is defined, or as a starting point for accessible brand adaptations.

## Categorical (Unordered Groups)

**Okabe-Ito (8 colors, CVD-safe):**
`#E69F00` (orange), `#56B4E9` (sky blue), `#009E73` (bluish green), `#F0E442` (yellow), `#0072B2` (blue), `#D55E00` (vermillion), `#CC79A7` (reddish purple), `#000000` (black)

**Paul Tol Qualitative (up to 7 colors):**
`#332288`, `#88CCEE`, `#44AA99`, `#117733`, `#999933`, `#DDCC77`, `#CC6677`

Use categorical palettes when groups have no inherent order (e.g., product lines, regions).

## Sequential (Low-to-High)

**Viridis:** Perceptually uniform, CVD-safe, prints well in grayscale. Use for continuous quantitative scales (e.g., heatmaps, choropleths).

**Cividis:** Optimized specifically for deuteranopia and protanopia. Preferred when CVD safety is the primary concern.

Avoid rainbow/jet palettes — they create false perceptual boundaries and fail in grayscale.

## Diverging (Deviation from Midpoint)

**ColorBrewer RdBu (Red-Blue):** Use when data diverges from a meaningful center point (e.g., above/below target, positive/negative change).

**ColorBrewer BrBG (Brown-Blue-Green):** CVD-safe alternative for diverging scales.

Ensure the midpoint color is neutral (white or light grey) so it reads as "zero."

## Contrast Requirements (WCAG AA)

- **Text on background:** Minimum 4.5:1 ratio (3:1 for large text ≥18pt or bold ≥14pt)
- **Non-text elements** (chart lines, bars, data points): Minimum 3:1 ratio against background and adjacent colors
- **Color must not be the sole encoding:** Always pair color with labels, patterns, markers, or position

## When to Use Each

| Scenario | Palette type | Default recommendation |
|---|---|---|
| Comparing categories (≤8) | Categorical | Okabe-Ito |
| Heatmap / density | Sequential | Viridis |
| Above/below target | Diverging | ColorBrewer RdBu |
| Maximum CVD safety | Sequential | Cividis |
| Brand override available | Brand palette | Check CVD safety first |
