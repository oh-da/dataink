---
name: infographic
description: Guides the design, layout, color strategy, and narrative structure of informative infographics. Use when the user asks to "create an infographic", "design an infographic", "visualize these facts", or "apply brand guidelines to an infographic".
---

# Infographic Creator

> *This skill draws on data visualization principles from Edward Tufte's* The Visual Display of Quantitative Information *(Graphics Press, 1983) and narrative/design techniques from Cole Nussbaumer Knaflic's* Storytelling with Data *(Wiley, 2015). The "3-minute story" framework is Knaflic's; the 10% highlighting guideline originates in Lidwell, Holden, and Butler's* Universal Principles of Design *(Rockport, 2003). See reference files for detailed attributions.*

-# Performance Notes
- Take your time to do this thoroughly.
- Quality and accuracy are more important than speed.
- Do not skip the context evaluation, storyboarding, or brand-checking steps.

## CRITICAL CONSTRAINTS
- **AVOID** "fluffy" designs, garish oversized numbers, or cartoonish graphics. Infographics must have substance and actually inform the audience.
- An infographic is **NOT** a disjointed collection of facts; it **MUST** tell a cohesive, structured story.
- **NEVER** recommend 3D graphics, Pie Charts, Donut Charts, or secondary y-axes.

## Instructions

### Step 1: Understand the Context and Storyboard
Before choosing charts or colors, articulate the "3-minute story" (Knaflic) — the concise narrative boiling down the "so-what". 
- Create a visual outline (storyboard) with a clear beginning (setup), middle (data evidence), and end (takeaway).
- Group related facts into "chunks" to avoid overwhelming the audience.

### Step 2: Choose Displays & Maximize Data-Ink
- Select appropriate charts: Simple Text for 1-2 key numbers, Bar Charts (zero baseline) for categorical comparisons, Line Graphs for continuous trends.
- Strip away clutter: Remove chart borders, background shading, heavy gridlines, and diagonal text.

### Step 3: Apply Branding and Color Strategy
Before applying colors and typography, check for the presence of brand guidelines.

* **Check for Brand Assets:** Look for `assets/brand-colors.md` and `assets/brand-fonts.md`. 
    * **If they exist:** Strictly utilize the specified brand typography and color palette. 
    * **If they do not exist:** Continue without them, defaulting to standard clean typography (like Arial or sans-serif) and a standard color palette (grey baseline with blue highlights).

* **Apply Color Best Practices:**
    1. **Highlight Strategically (The 10% Guideline — Lidwell et al.):** Identify 1-2 brand-appropriate colors to serve as "audience-look-here" cues. Reserve highlighting for at most 10% of the visual surface so the effect is not diluted.
    2. **Mute the Baseline:** Keep the remainder of the chart muted. Standardize on soft, natural colors (like light grey) to push non-essential data to the background.
    3. **Ensure Sufficient Contrast:** If the primary brand color is too light or washes out the visual, deviate slightly by using bold black or a complementary color to draw attention, provided it does not clash with the brand's logo.
    4. **Account for Dark Templates:** If the brand mandates a dark or black background, reverse the contrast rules: black becomes the baseline, grey stands out less, and white or bright colors (like yellow) become the highly attention-grabbing highlight colors.

### Step 4: Focus Attention and Apply Text
- Use preattentive attributes (color, size, spatial position) to guide the audience's eyes through the storyboard.
- Ensure every chart has an action title.
- Explicitly annotate key insights right next to the data.

## Examples

**Example 1: Designing an infographic with a light brand color**
* **User says:** "Turn these 5 regional sales stats into an infographic. Use our brand files."
* **Actions:** 
    1. Verify `assets/brand-colors.md` exists. (Result: Found. Primary brand color is light yellow; background is white).
    2. Apply Contrast Rule: Since light yellow on a white background lacks sufficient contrast, use a bold black or a complementary dark brand color for the data highlights instead. 
    3. Make all baseline bars light grey.
    4. Ensure the charts flow in a cohesive narrative rather than just a random list.

## Troubleshooting

**Error: User requests "make it look cool with 3D elements and lots of graphics."**
* **Cause:** The user believes aesthetic dazzle equals a better infographic.
* **Solution:** Politely advise that while aesthetics matter, 3D graphics physically skew numbers. Suggest using strategic brand colors, clean alignment, and high-quality typography to achieve a professional, aesthetic design instead.

**Error: The visual feels overwhelming and chaotic.**
* **Cause:** Too much of the infographic is highlighted.
* **Solution:** Revert to the 10% rule. Push more elements to the muted baseline color (grey) and ensure only the single most important data point in each section uses the brand's highlight color.