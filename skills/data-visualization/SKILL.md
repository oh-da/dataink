---
name: visualize
description: Guides users in selecting, designing, and refining effective data visualizations. Use when the user asks to "visualize data", "choose a chart type", "improve a graph", "reduce clutter", or "tell a story with data".
---

# Data Visualization Expert

> *This skill draws on the data-ink ratio concept from Edward Tufte's* The Visual Display of Quantitative Information *(Graphics Press, 1983), on chart selection and relationship taxonomy from Stephen Few's* Show Me the Numbers *(Perceptual Edge, 2004), and on design and validation techniques from Cole Nussbaumer Knaflic's* Storytelling with Data *(Wiley, 2015). The 10% highlighting guideline originates in Lidwell, Holden, and Butler's* Universal Principles of Design *(Rockport, 2003). See reference files for detailed attributions.*

-# Performance Notes
- Take your time to do this thoroughly.
- Quality is more important than speed.
- Do not skip validation steps.

## CRITICAL CONSTRAINTS
- **NEVER** recommend or use 3D graphics, Pie Charts, or Donut Charts.
- **NEVER** recommend secondary (right-hand) y-axes.
- Bar charts **MUST ALWAYS** have a zero baseline.
- Avoid diagonal text or elements; keep text horizontal.

## Instructions

### Step 1: Determine the Medium (Table vs. Graph)
Before choosing a chart, determine if the data should be displayed as a table or a graph. 
* Consult `references/medium-selection.md` for the exact rules on when to use each.

### Step 2: Choose the Appropriate Visual Display
If a graph is the correct medium, select the chart type that best highlights the specific data relationship.
* Consult `references/chart-types.md` for the matrix of continuous, categorical, and relational data mappings.

### Step 3: Maximize the Data-Ink Ratio
Evaluate the chosen visual to eliminate clutter and remove "non-data ink". 
* Strip away chart borders, background shading, and heavy gridlines.
* Push necessary but non-message-impacting elements (like axes) to the background using light grey.
* Consult `references/design-principles.md` to apply Gestalt principles (Proximity, Similarity, Closure).

### Step 4: Apply Branding and Color Strategy
Before applying colors and fonts, check for the presence of brand guidelines.
* **Brand Assets Check:** Look for `assets/brand-colors.md` and `assets/brand-fonts.md`. 
    * **If they exist:** Strictly utilize the primary/secondary brand colors and fonts defined in those files. Identify one or two brand-appropriate colors to use as "audience-look-here" cues, and keep the rest of the palette muted.
    * **If they do not exist:** Continue without them. Standardize on soft, muted colors (like grey) for baseline data, and reserve a single vivid color (like blue) strictly for highlighting the most important information (a strategy described by Stephen Few in *Show Me the Numbers*).
* **The 10% Guideline (Lidwell et al.):** Reserve highlighting for at most 10% of the visual surface. Over-highlighting dilutes the effect.

### Step 5: Focus Attention and Tell a Story
Think like a designer to guide the audience's eyes. 
* Ensure every graph has a clear title, labeled axes, and actionable text (e.g., an action title replacing a descriptive title).

### Step 6: Validation Check (Knaflic)
Run the "where are your eyes drawn?" test.
* Simulate looking away and looking back at the graph.
* Verify that the strategic use of preattentive attributes (color, size, position) immediately directs focus to the intended narrative without distractions.

## Examples

**Example 1: Applying Brand Colors**
* **User says:** "I want to compare revenue across regions, make it look good."
* **Actions:** 
    1. Recommend a Horizontal Bar Chart for categorical data.
    2. Check `assets/brand-colors.md`. (Result: Found. Primary brand color is Forest Green).
    3. Make all baseline bars light grey, and highlight the top-performing region's bar in Forest Green.
    4. Ensure the baseline starts at zero and remove chart borders.

## Troubleshooting

**Error: The user's graph is overwhelmingly cluttered (a "spaghetti graph").**
* **Cause:** Too many categories are plotted on a single line graph, creating a tangled mess.
* **Solution:** Either emphasize a single line with a bright color (or brand color) and push the rest to the background using grey, or pull the graphs apart into multiple smaller graphs ("small multiples") that share the same axes.