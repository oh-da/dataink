# DataInk

## AI Skills for Data Communication and Storytelling

> *"The greatest value of a picture is when it forces us to notice what we never expected to see."*
> — Edward Tufte

DataInk is a collection of modular skills designed to help AI systems produce clear, effective data communication.

Each skill captures established practices from data visualization, information design, and narrative communication. Instead of repeatedly explaining these practices to an AI system, they are packaged into structured `SKILL.md` workflows.

The result is consistent output for charts, infographics, and presentations that follows sound communication principles.

---

## Why DataInk

Many data visualizations fail not because the data is incorrect but because the communication is weak.

Common problems include:
- pie charts that distort proportions
- 3D charts that skew values
- dashboards overloaded with visual noise
- presentations that show numbers without explaining why they matter

DataInk addresses these issues by encoding expert workflows into reusable AI skills.

These workflows guide an AI system through the steps required to design charts, construct narratives, and communicate insights clearly.

---

## Use Cases

DataInk can be applied in many situations where data must be communicated clearly.

### Business reporting

Transform analysis into clear executive communication.

Examples include:
- quarterly performance presentations
- strategy updates
- board reports
- KPI dashboards

Recommended workflow: `data-visualization` → `data-storyteller`

### Dashboard and chart design

Improve charts created in tools such as Excel, Tableau, Power BI, or Python.

Examples include:
- redesigning cluttered dashboards
- selecting the correct chart type
- removing unnecessary visual elements

Recommended workflow: `data-visualization`

### Data storytelling and presentations

Structure presentations so the data supports a clear argument.

Examples include:
- product analytics presentations
- marketing performance reviews
- operations reports
- research presentations

Recommended workflow: `data-storyteller`

### Infographics and visual reports

Combine multiple insights into a single visual explanation.

Examples include:
- annual reports
- research summaries
- educational visualizations
- public policy reports

Recommended workflow: `infographic-creator`

---

## Design Philosophy

DataInk is built on the idea that data visualization is a communication discipline.

Charts often fail because they prioritize visual decoration instead of clarity and narrative structure. Effective data communication requires understanding the audience, identifying the key insight, and presenting information in a way that guides attention.

The workflows in this repository translate these principles into repeatable steps that an AI system can follow.

### Communication before visualization

Effective visual communication begins with context.

Before selecting a chart type, the following questions must be answered:
- Who is the audience?
- What decision must be made?
- What insight matters most?

The workflows therefore begin with narrative framing rather than chart design.

### Explanatory analysis

Exploratory analysis helps analysts discover insights.

Explanatory analysis communicates those insights to others.

The workflows in this repository focus on explanatory communication by removing unnecessary analysis and highlighting the insights that matter.

### Visual simplicity

Human perception processes information more effectively when visuals are simple and structured.

Effective charts:
- maximize the data ink ratio
- remove unnecessary visual elements
- highlight only a small portion of the visual
- guide the viewer's attention

### Narrative structure

Data becomes persuasive when it is presented as part of a narrative.

The storytelling workflows use a simple structure:
1. Setup
2. Conflict
3. Resolution

This structure ensures that data supports a clear message rather than appearing as isolated facts.

### Modular workflows

Each skill focuses on a specific communication task.
- `data-visualization` focuses on chart design
- `infographic-creator` focuses on visual summaries
- `data-storyteller` focuses on narrative structure

These skills can be used independently or combined into larger workflows.

---

## Repository Structure

Each skill lives in its own directory with optional `assets/` and `references/` folders.

This design follows a progressive disclosure approach so the AI loads only the context it needs.

```
dataink/
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
│   ├── assets/
│   │   ├── brand-colors.md
│   │   └── brand-fonts.md
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
```

---

## The Skills

### Infographic Creator

**Purpose:** Design informative infographics that communicate insights rather than decorate data.

**Typical prompts:**
- Create an infographic from these results
- Design an information graphic for a report
- Visualize several facts in one visual
- Apply brand guidelines to an infographic

**Workflow:**
1. Define the narrative using a three minute story
2. Create a storyboard with beginning, middle, and end
3. Select chart types and remove visual clutter
4. Apply brand assets if available
5. Highlight key insights using the ten percent rule
6. Annotate important observations

**Rules:** No pie charts. No donut charts. No 3D graphics. No rainbow color palettes. No secondary axes.

---

### Data Visualization Expert

**Purpose:** Provide guidance for designing clear charts and tables.

**Typical prompts:**
- Visualize this dataset
- Which chart type should I use
- Improve this graph
- Reduce clutter on this dashboard

**Workflow:**
1. Decide whether a table or graph is appropriate
2. Select the correct chart type based on the data relationship
3. Maximize the data ink ratio
4. Apply visual perception principles
5. Validate attention flow

**Rules:** No pie charts. No 3D charts. No secondary axes. Bar charts must start at zero. Avoid diagonal labels.

---

### Data Storyteller

**Purpose:** Transform collections of charts into structured narratives.

**Typical prompts:**
- Tell a story with this data
- Structure my presentation
- Outline my slide deck
- Improve the narrative flow

**Workflow:**
1. Identify the audience and central tension
2. Structure the story using a three act arc
3. Choose narrative flow
4. Apply repetition techniques
5. Validate structure using logic checks

Logic checks include:
- horizontal logic
- vertical logic
- reverse storyboarding

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/your-org/dataink.git
```

### Point your AI system to a skill

Example prompt:

```
Follow the instructions in dataink/data-visualization/SKILL.md
to help visualize the attached dataset.
```

### Customize brand assets

Edit the files:
- `assets/brand-colors.md`
- `assets/brand-fonts.md`

If these files are populated, the skills will automatically apply the brand settings.

### Combining Skills

A common workflow looks like this:

1. **Data Visualization Expert** — Design individual charts.
2. **Infographic Creator** — Combine charts into a visual summary.
3. **Data Storyteller** — Structure the visuals into a presentation narrative.

---

## Core Principles

| Principle | Meaning |
|---|---|
| Data ink ratio | Maximize ink devoted to data |
| Ten percent rule | Highlight only a small portion of the visual |
| Preattentive attributes | Use color, size, and position to guide attention |
| Gestalt perception | Organize information using proximity and similarity |
| Action titles | Titles state insights rather than topics |
| Audience as protagonist | The story focuses on the audience |
| Zero baseline bars | Bar charts encode values by length |
| Avoid pie charts | Humans compare angles poorly |

---

## Roadmap

Future additions planned for DataInk include:

### Dashboard Design

Guidelines for building dashboards that support decision making.

Potential features include:
- dashboard layout structure
- KPI prioritization
- interaction design
- cognitive load reduction

### Annotation and Insight Highlighting

Methods for clearly explaining what charts show.

Possible capabilities:
- annotation strategies
- insight callouts
- explanation patterns

### Accessibility and Inclusive Visualization

Practices that improve readability and accessibility.

Potential topics include:
- color blind safe palettes
- contrast validation
- font readability
- visual hierarchy for accessibility

### Visualization Review

A skill that critiques existing charts and suggests improvements.

Possible capabilities include:
- clutter detection
- misleading chart detection
- design improvement suggestions

---

## Contributing

Contributions are welcome.

To add a new skill:
1. Create a new directory
2. Add a `SKILL.md`
3. Include reference files if needed
4. Add asset files if brand customization is required

---

## License

See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

This repository draws on widely recognized principles in data visualization and analytical storytelling.

### Cole Nussbaumer Knaflic

Several narrative concepts in this repository are inspired by the methods described in *Storytelling with Data*.

These include:
- defining a three minute story
- identifying a clear central message
- structuring communication around a narrative arc
- guiding attention using preattentive attributes
- validating communication through logical structure

These ideas influence the `data-storyteller` and `infographic-creator` skills.

### Edward Tufte

Some visualization principles used in this repository reflect ideas discussed in *The Visual Display of Quantitative Information*.

These include:
- maximizing the data ink ratio
- removing non data elements
- prioritizing clarity over decoration

### Visual Perception Research

The design principles used in the skills are also informed by research from the Gestalt school of visual perception.

Relevant concepts include:
- proximity
- similarity
- closure
- visual hierarchy

---

**Disclaimer:** This repository does not reproduce material from the referenced works. It applies widely known visualization and storytelling principles to create structured workflows for charts, infographics, and data narratives.
