Data Communication & Storytelling AI Skills Repository
This repository contains a collection of modular AI skills designed to guide Claude (or other AI agents) in creating expert-level data visualizations, infographics, and data-driven narratives. By packaging these repeatable workflows into SKILL.md files, you can automate best practices for analytical communication and ensure consistent, high-quality outputs.
Repository Structure
To leverage the concept of "progressive disclosure" and keep token usage efficient, each skill is housed in its own directory alongside optional assets/ (for brand guidelines) and references/ (for deep-dive theories and principles):
skills/
├── infographic-creator/
│   ├── SKILL.md
│   ├── assets/
│   │   ├── brand-colors.md
│   │   └── brand-fonts.md
│   └── references/
│       ├── audience-context.md
│       └── visual-hierarchy.md
├── data-visualization/
│   ├── SKILL.md
│   └── references/
│       ├── medium-selection.md
│       ├── chart-types.md
│       └── design-principles.md
└── data-storyteller/
    ├── SKILL.md
    └── references/
        ├── narrative-arc.md
        ├── flow-and-repetition.md
        └── logic-validation.md

--------------------------------------------------------------------------------
1. Infographic Creator (infographic-creator)
This skill acts as a rigorous guide for designing, laying out, and coloring informative, data-driven infographics while strictly avoiding "fluffy" or shallow visual designs.
When to Use
Trigger this skill when you need to combine multiple data points into a single, cohesive visual narrative. Use it when the user requests to:
"Create an infographic"
"Design an information graphic"
"Visualize these facts"
"Apply our brand guidelines to an infographic"
How to Use
Initialize the Skill: Point the AI to the infographic-creator/SKILL.md file.
Provide Brand Assets: If corporate branding is required, populate the assets/brand-colors.md and assets/brand-fonts.md files with your specific hex codes and typography. The skill is programmed to conditionally check for these files and apply the "10% rule" to highlight data strategically without creating cluttered, "rainbow" charts.
Provide Data: Feed the AI your raw data. The skill will automatically evaluate the "3-minute story", storyboard the narrative flow, and select the appropriate charts before applying preattentive attributes to guide the audience's eyes.

--------------------------------------------------------------------------------
2. Data Visualization Expert (data-visualization)
This skill embeds the core rules of "graphicacy" and human visual perception, acting as an expert consultant to help you choose, design, and declutter individual charts and tables.
When to Use
Trigger this skill when you need to display specific data relationships effectively or fix a poorly designed graph. Use it when the user requests to:
"Visualize this data"
"Choose a chart type"
"Improve this graph"
"Reduce clutter"
How to Use
Initialize the Skill: Point the AI to the data-visualization/SKILL.md file.
Define the Goal: Provide the AI with your data and state whether the audience needs precise individual lookups (which triggers Table rules) or needs to see the "shape" and trends of the data (which triggers Graph rules).
Let the AI Refine: The skill will automatically ban ineffective charts (like 3D graphics, pie charts, and donut charts) and apply Gestalt principles of visual perception to maximize the data-ink ratio by removing heavy gridlines, borders, and background shading.

--------------------------------------------------------------------------------
3. Data Storyteller (data-storyteller)
This skill shifts the focus from exploratory analysis (simply presenting facts) to explanatory communication (crafting a persuasive narrative). It structures presentations and reports so that the audience is the protagonist and the data drives a specific call to action.
When to Use
Trigger this skill when you have a disjointed collection of charts or facts and need to build an architecture for a live presentation, a written report, or a slide deck. Use it when the user requests to:
"Tell a story with this data"
"Structure my presentation"
"Outline my slide deck"
"Improve my narrative flow"
How to Use
Initialize the Skill: Point the AI to the data-storyteller/SKILL.md file.
Define the Audience & Tension: Tell the AI who your target audience is and what is at stake.
Drafting: The AI will execute a "3-minute story" planning exercise to strip away non-essential details and clarify the core message. It will then output a structured three-act narrative (Beginning/Setup, Middle/Conflict, End/Resolution) with a clear, action-oriented executive summary.
Validation: The skill automatically applies "Horizontal Logic" (ensuring slide action titles alone tell the overarching story) and "Vertical Logic" (ensuring all content perfectly reinforces the title) to bulletproof the flow before you finalize the deck.