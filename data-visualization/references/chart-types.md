# Chart Selection Matrix

To select the most effective chart, first identify the data relationship you are trying to communicate, then match it to the appropriate visual form.

> *The seven-category relationship taxonomy (time-series, nominal comparison, ranking, part-to-whole, deviation, distribution, correlation) used to organize this matrix originates in Stephen Few's* Show Me the Numbers *(Perceptual Edge, 2004). Chart selection guidance and specific design rules are also adapted from Cole Nussbaumer Knaflic's* Storytelling with Data *(Wiley, 2015), Chapter 2. Recommendations against pie charts, 3D graphics, and secondary y-axes reflect a broad consensus shared by Few, Knaflic, and Edward Tufte.*

## 1. Map the Relationship to the Chart

*   **Time-Series (Changes over time):** Use **Line Graphs** or **Vertical Bar Charts**. Lines emphasize the overall trend and rate of change. Vertical bars work better when the focus is on specific discrete values at individual time points.
*   **Nominal Comparison (Comparing independent categories):** Use **Bar Charts** (vertical or horizontal). Avoid line graphs for categorical data — the connecting slope falsely implies continuity between unrelated items.
*   **Ranking (Ordering categories by value):** Use **Bar Charts** sorted from highest to lowest (or vice versa) so the ranking is visually obvious.
*   **Part-to-Whole (How parts compose a total):** Use **Stacked Bar Charts** or standard **Bar Charts** with a title that explicitly states the parts sum to 100%. *Never use Pie Charts.*
*   **Deviation (Difference from a baseline or target):** Use **Bar Charts** or **Line Graphs** paired with a reference line at zero. Bars should extend upward for positive deviations and downward for negative ones.
*   **Correlation (Relationship between two variables):** Use **Scatterplots**, optionally with a trend line to make the direction and strength of the relationship clearer.
*   **Distribution (How values spread across a range):** Use **Histograms** (vertical bar charts with continuous bins) or **Box Plots**.

## 2. Rules for Specific Chart Types

**Simple Text**
*   **Use when:** You have only one or two numbers to communicate.
*   **Design Rule:** Display the number prominently with a brief supporting phrase. Do not wrap a lone data point in a chart — the chart adds overhead without adding insight.

**Line Graphs**
*   **Use when:** Showing continuous data over an ordered dimension — typically time (days, months, years) or frequency.
*   **Design Rule:** Never plot categorical (nominal) data as a line.

**Slopegraphs**
*   **Use when:** Comparing exactly two time periods or two conditions, and you want to show relative change across multiple categories at once.

**Bar Charts (Vertical and Horizontal)**
*   **Use when:** Plotting categorical data, rankings, or nominal comparisons.
*   **Design Rules:**
    *   **Zero Baseline:** Bars encode magnitude through their length, so they **must always start at zero**. Truncating the baseline distorts the visual comparison.
    *   **Orientation:** Default to **Horizontal Bar Charts** when category labels are long — horizontal text is far easier to read than rotated or diagonal labels.

**Stacked Bar Charts**
*   **Use when:** You need to compare totals across categories while also revealing subcomponent composition.
*   **Design Rules:** Subcomponents above the first segment are difficult to compare precisely because they lack a shared baseline. For survey data (e.g., a Likert scale), a **100% Stacked Horizontal Bar Chart** provides consistent baselines on both the left and right edges.

**Waterfall Charts**
*   **Use when:** You need to decompose a total into sequential positive and negative contributions — for example, showing how headcount changed from a starting value to an ending value over a year.

**Scatterplots**
*   **Use when:** Exploring the relationship between two quantitative variables by plotting each observation as a point along two axes.

## 3. Visuals to ALWAYS Avoid

*   **Pie and Donut Charts:** Humans judge angles and areas poorly, making it hard to compare slice sizes. Donut charts compound the problem by asking readers to compare arc lengths. A simple bar chart communicates the same data far more accurately.
*   **3D Graphics:** Adding a third visual dimension to encode a single data dimension distorts values and makes accurate reading nearly impossible. There is no analytical benefit.
*   **Secondary Y-Axes:** A right-hand y-axis requires the reader to constantly check which data maps to which scale — a cognitive tax that obscures rather than reveals. Instead, label data points directly, or split the data into two vertically stacked charts that share the same x-axis.