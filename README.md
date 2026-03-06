# DataInk — AI Skills for Data Communication & Storytelling

> *"The greatest value of a picture is when it forces us to notice what we never expected to see."* — Edward Tufte

DataInk is a collection of modular AI skills that turn Claude (or any compatible AI agent) into an expert-level data communication consultant. Each skill encodes battle-tested principles from the fields of data visualization, information design, and narrative storytelling — so you get consistent, high-quality outputs every time, without having to re-prompt the fundamentals.

---

## Why DataInk?

Most data visualizations fail — not because the data is bad, but because the design is. Pie charts distort proportions. 3D graphics skew numbers. Cluttered graphs bury the signal in noise. And even well-designed charts fall flat when they lack a narrative that moves the audience to action.

DataInk solves this by packaging repeatable expert workflows into `SKILL.md` files that an AI agent can follow step-by-step. The result: every chart, infographic, and presentation you produce is grounded in the science of human visual perception, not guesswork.

---

## Repository Structure

Each skill lives in its own directory with optional `assets/` (for brand guidelines) and `references/` (for deep-dive theory). This "progressive disclosure" design keeps token usage efficient — the AI loads only the context it needs.

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

### 1. Infographic Creator

**What it does:** Guides the design, layout, color strategy, and narrative structure of data-driven infographics that actually inform — no fluff, no clip-art, no shallow "data decoration."

**When to use it:**
- "Create an infographic from these quarterly results"
- "Design an information graphic for our annual report"
- "Visualize these facts into a single cohesive visual"
- "Apply our brand guidelines to an infographic"

**How it works:**
1. **Context & Storyboard** — The skill starts by articulating the "3-minute story" (the concise "so-what" narrative), then storyboards a beginning, middle, and end.
2. **Chart Selection** — Chooses the right display for each data point (simple text, bar charts, line graphs) and strips away clutter to maximize the data-ink ratio.
3. **Branding & Color** — Automatically checks for `assets/brand-colors.md` and `assets/brand-fonts.md`. If they exist, it applies brand colors using the **10% Rule** (highlight at most 10% of the design). If they don't, it defaults to clean grey baselines with blue highlights.
4. **Attention & Annotation** — Uses preattentive attributes (color, size, position) to guide the viewer's eyes, adds action titles to every chart, and annotates key insights directly next to the data.

**Hard rules:** No 3D graphics. No pie charts. No donut charts. No secondary y-axes. No rainbow palettes.

---

### 2. Data Visualization Expert

**What it does:** Acts as an expert graphicacy consultant — helping you choose, design, and declutter individual charts and tables based on the science of human visual perception.

**When to use it:**
- "Visualize this data"
- "What chart type should I use?"
- "This graph is cluttered — help me improve it"
- "Should I use a table or a chart here?"
- "Reduce the clutter on this dashboard"

**How it works:**
1. **Medium Selection** — First determines whether a table or a graph is the right medium (tables for precise lookups; graphs for shapes and trends). Consults `references/medium-selection.md`.
2. **Chart Type Selection** — Maps the data relationship (time-series, ranking, part-to-whole, correlation, distribution) to the optimal chart type using the matrix in `references/chart-types.md`.
3. **Data-Ink Maximization** — Eliminates non-data ink: strips borders, background shading, heavy gridlines. Applies Gestalt principles (Proximity, Similarity, Closure) from `references/design-principles.md`.
4. **Branding** — Checks for brand assets. Applies brand colors as strategic highlights while keeping the baseline muted.
5. **Validation** — Runs the "Where are your eyes drawn?" test to confirm preattentive attributes direct focus to the intended narrative.

**Hard rules:** No 3D graphics. No pie or donut charts. No secondary y-axes. Bar charts must always start at zero. No diagonal text.

---

### 3. Data Storyteller

**What it does:** Shifts your communication from *exploratory* (presenting facts) to *explanatory* (crafting a persuasive narrative). Structures presentations, reports, and slide decks so the audience is the protagonist and the data drives a clear call to action.

**When to use it:**
- "Tell a story with this data"
- "Structure my presentation for the board"
- "Outline my slide deck"
- "Improve the narrative flow of this report"
- "I have a bunch of charts — help me tie them together"

**How it works:**
1. **Audience & Tension** — Identifies the protagonist (your audience) and the conflict between "what is" and "what could be."
2. **Three-Act Arc** — Organizes the communication into Beginning (setup & imbalance), Middle (data as evidence, options, solution), and End (specific call to action). Consults `references/narrative-arc.md`.
3. **Flow & Repetition** — Chooses between chronological flow (to build credibility) or leading with the ending (for busy executives). Applies the "Bing, Bang, Bongo" repetition principle. Consults `references/flow-and-repetition.md`.
4. **Logic Validation** — Stress-tests the structure with three checks from `references/logic-validation.md`:
   - **Horizontal Logic:** Reading only the slide titles tells the complete story.
   - **Vertical Logic:** Every element on a page reinforces its title.
   - **Reverse Storyboarding:** The main point of each page matches the original intended flow.

**Hard rules:** The audience is always the hero. Every story must have a call to action. Every slide must use an action title, not a descriptive one.

---

## Getting Started

### Prerequisites

- An AI agent that supports skill/instruction files (e.g., Claude with custom instructions, or any agent that can ingest markdown prompts).

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/dataink.git
   ```

2. **Point the AI to a skill:** When starting a conversation, instruct the AI to follow the relevant `SKILL.md` file. For example:
   ```
   Follow the instructions in dataink/data-visualization/SKILL.md
   to help me visualize the attached sales data.
   ```

3. **Customize brand assets (optional):** Edit the `assets/brand-colors.md` and `assets/brand-fonts.md` files with your corporate hex codes, font families, and sizes. The skills automatically detect and apply these when present.

4. **Provide your data:** Feed the AI your raw data, chart drafts, or presentation outlines. The skill handles the rest — evaluating context, selecting displays, applying design principles, and validating the output.

### Combining Skills

The skills are designed to work independently or together. A typical end-to-end workflow might look like:

1. **Data Visualization Expert** — Design each individual chart with the right type, clean layout, and brand colors.
2. **Infographic Creator** — Combine multiple charts into a single cohesive infographic with narrative flow.
3. **Data Storyteller** — Structure the infographic (or a series of visuals) into a presentation with a three-act arc and validated logic.

---

## Customizing Brand Assets

The `assets/` folders contain template files you can customize for your organization:

**`brand-colors.md`** — Define your color palette:
- Primary highlight color (hex code)
- Secondary highlight color
- Baseline/muted colors
- Background color (light or dark)

**`brand-fonts.md`** — Define your typography:
- Primary and secondary typefaces
- Sizes for titles, labels, and footnotes

When these files are populated, the skills automatically enforce your brand while following best practices (the 10% highlight rule, sufficient contrast checks, dark-template adjustments).

---

## Core Principles

Every skill in DataInk is built on these foundational ideas:

| Principle | What It Means |
|---|---|
| **Data-Ink Ratio** | Maximize the share of ink devoted to actual data. Remove everything else. |
| **The 10% Rule** | Highlight at most 10% of the visual. Over-highlighting dilutes everything. |
| **Preattentive Attributes** | Use color, size, and position to guide attention before conscious thought kicks in. |
| **Gestalt Perception** | Leverage proximity, similarity, and closure to reduce cognitive load. |
| **Action Titles** | Every chart and slide gets a title that states the insight, not just the topic. |
| **Audience as Protagonist** | The story is about them — their problem, their stakes, their call to action. |
| **Zero-Baseline Bars** | Bar charts encode value by length. A non-zero baseline lies. |
| **No Pie Charts** | Humans are bad at comparing angles and areas. Use bars instead. |

---

## Contributing

Contributions are welcome. If you have a new skill to add (e.g., dashboard design, annotation strategy, accessibility checks), follow the existing structure:

1. Create a new directory under the root with a descriptive name.
2. Add a `SKILL.md` with frontmatter (name, description, metadata), instructions, examples, and troubleshooting.
3. Add `references/` files for any deep-dive theory the skill consults.
4. Add `assets/` files if the skill supports brand customization.

---

## License

This project is open source. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

The principles encoded in these skills draw heavily from the work of **Cole Nussbaumer Knaflic** (*Storytelling with Data*), **Edward Tufte** (*The Visual Display of Quantitative Information*), and the **Gestalt school of visual perception**. DataInk operationalizes their teachings into repeatable, AI-executable workflows.
