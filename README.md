
# DataInk

AI Skills for Data Communication and Storytelling

> "The greatest value of a picture is when it forces us to notice what we never expected to see."  
Edward Tufte

DataInk is a collection of modular skills designed to help AI systems produce clear and effective data communication.

Each skill captures established practices from data visualization, information design, and narrative communication. Instead of repeatedly explaining these practices to an AI system, they are packaged into structured `SKILL.md` workflows.

These workflows guide an AI system through chart design, infographic creation, and narrative construction so that every output follows sound communication principles.

Repository:  
https://github.com/oh-da/dataink.git

---

# Why DataInk

Many data visualizations fail not because the data is incorrect but because the communication is weak.

Common problems include:

- pie charts that distort proportions  
- 3D charts that skew values  
- dashboards overloaded with visual noise  
- presentations that show numbers without explaining why they matter  

DataInk addresses these issues by encoding expert workflows into reusable AI skills.

These workflows guide an AI system through the steps required to design charts, construct narratives, and communicate insights clearly.

---

# DataInk Workflow

The skills can be used independently or combined into a full communication workflow.

```mermaid
flowchart LR

A[Raw Data or Analysis] --> B[Data Visualization Expert]

B --> C[Clear Individual Charts]

C --> D[Infographic Creator]

D --> E[Structured Visual Summary]

E --> F[Data Storyteller]

F --> G[Presentation or Report]

style B fill:#d4f4dd
style D fill:#d4e6f4
style F fill:#f4e1d4
```

### Step 1: Data Visualization Expert

Transforms raw data into clear charts.

Examples:

- choose appropriate chart type  
- remove clutter  
- apply visual design principles  

Output: clear charts.

---

### Step 2: Infographic Creator

Combines insights into a visual summary.

Examples:

- infographic layout  
- highlighting key data  
- visual storytelling  

Output: structured infographic.

---

### Step 3: Data Storyteller

Builds a narrative around the visuals.

Examples:

- presentation structure  
- narrative arc  
- decision framing  

Output: presentation or report.

---

# Use Cases

DataInk is useful whenever data must be communicated clearly.

## Business reporting

Examples:

- quarterly performance presentations  
- strategy updates  
- board reports  
- KPI dashboards  

Recommended workflow:

data-visualization → data-storyteller

---

## Dashboard and chart design

Examples:

- redesign cluttered dashboards  
- choose the correct chart type  
- remove visual noise  

Recommended workflow:

data-visualization

---

## Data storytelling and presentations

Examples:

- product analytics presentations  
- marketing performance reviews  
- operations reports  
- research presentations  

Recommended workflow:

data-storyteller

---

## Infographics and visual reports

Examples:

- annual reports  
- research summaries  
- educational visualizations  
- policy reports  

Recommended workflow:

infographic-creator

---

# Design Philosophy

DataInk is built on the idea that data visualization is a communication discipline.

Charts often fail because they prioritize visual decoration instead of clarity and narrative structure. Effective data communication requires understanding the audience, identifying the key insight, and presenting information in a way that guides attention.

The workflows in this repository translate these principles into repeatable steps that an AI system can follow.

## Communication before visualization

Before selecting a chart type, it is important to answer:

- Who is the audience  
- What decision must be made  
- What insight matters most  

For this reason the workflows begin with narrative framing.

---

## Explanatory analysis

Exploratory analysis helps analysts discover insights.

Explanatory analysis communicates those insights to others.

The workflows in this repository focus on explanatory communication by removing unnecessary analysis and highlighting the insights that matter.

---

## Visual simplicity

Effective charts:

- maximize the data ink ratio  
- remove unnecessary visual elements  
- highlight only a small portion of the visual  
- guide the viewer's attention  

---

## Narrative structure

Data becomes persuasive when presented as part of a narrative.

The storytelling workflows follow a simple structure:

1. Setup  
2. Conflict  
3. Resolution  

---

## Modular workflows

Each skill focuses on a specific communication task.

- **data-visualization** helps design charts  
- **infographic-creator** helps build visual summaries  
- **data-storyteller** helps structure narratives  

These skills can be used independently or combined.

---

# Repository Structure

Each skill lives in its own directory with optional `assets` and `references` folders.

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

# Skill Architecture

```mermaid
flowchart TD

A[AI Agent] --> B[SKILL.md Instructions]

B --> C[Workflow Steps]
B --> D[Assets]
B --> E[References]

D --> F[Brand Colors]
D --> G[Brand Fonts]

E --> H[Visualization Principles]
E --> I[Storytelling Methods]
```

The AI loads instructions first and consults assets or references only when necessary.

---

# Getting Started

Clone the repository:

```bash
git clone https://github.com/oh-da/dataink.git
```

Point your AI system to a skill:

```
Follow the instructions in dataink/data-visualization/SKILL.md
to visualize the attached dataset.
```

Customize brand assets if needed:

```
assets/brand-colors.md
assets/brand-fonts.md
```

---

# Roadmap

Future additions may include:

### Dashboard Design

- dashboard layout guidelines  
- KPI prioritization  
- interaction design  

### Annotation and Insight Highlighting

- annotation strategies  
- insight callouts  
- explanation patterns  

### Accessibility in Visualization

- color blind safe palettes  
- contrast validation  
- font readability  

### Visualization Review

A skill that critiques charts and suggests improvements.

---

# Contributing

Contributions are welcome.

To add a new skill:

1. Create a directory  
2. Add a `SKILL.md`  
3. Include references if needed  
4. Add assets for brand customization  

---

# License

See the LICENSE file for details.

---

# Acknowledgments

This repository draws on widely recognized principles in data visualization and analytical storytelling.

## Cole Nussbaumer Knaflic

Some narrative concepts are inspired by the work presented in *Storytelling with Data*.

These include:

- defining a three minute story  
- identifying a clear central message  
- structuring communication around a narrative arc  
- guiding attention using preattentive attributes  
- validating communication using logical structure  

These ideas influence the data-storyteller and infographic-creator skills.

## Edward Tufte

Several visualization ideas reflect concepts discussed in *The Visual Display of Quantitative Information*.

These include:

- maximizing the data ink ratio  
- removing non data elements  
- prioritizing clarity over decoration  

## Visual Perception Research

The design principles used in the skills are also informed by research from the Gestalt school of visual perception.

Relevant concepts include:

- proximity  
- similarity  
- closure  
- visual hierarchy  

## Disclaimer

This repository does not reproduce material from the referenced works. It applies widely known visualization and storytelling principles to create structured workflows for charts, infographics, and data narratives.
