# Chart Selection Matrix

To select the most effective chart, you must first identify the specific data relationship you are trying to communicate. Use the following matrix to match the data relationship with the appropriate visual display, and adhere to the strict design rules for each chart type.

## 1. Map the Relationship to the Chart

*   **Time-Series (Changes over time):** Use **Line Graphs** or **Vertical Bar Charts**. Lines emphasize the overall trend and nature of change. Vertical bars are better if you need to emphasize individual values for specific months/years.
*   **Nominal Comparison (Comparing independent categories):** Use **Bar Charts** (vertical or horizontal). Never use a line graph, as the slope connecting the points would falsely imply a continuous change between independent items.
*   **Ranking (Comparing categories sequentially by value):** Use **Bar Charts**. Sort the bars in descending or ascending order to emphasize high or low values.
*   **Part-to-Whole (How parts make up a total):** Use **Stacked Bar Charts** or standard **Bar Charts** (with a title explicitly stating they sum to 100%). *Never use Pie Charts.* 
*   **Deviation (Difference from a plan or reference point):** Use **Bar Charts** or **Line Graphs** paired with a clear reference line. The reference line should typically be set to zero, with bars extending up for positive and down for negative deviations.
*   **Correlation (Relationship between two variables):** Use **Scatterplots** (points) or points with trend lines.
*   **Distribution (Frequency of occurrence within ranges):** Use **Vertical Bar Charts** (histograms) or Box Plots (bars and lines).

## 2. Rules for Specific Chart Types

**Simple Text**
*   **Use when:** You only have one or two numbers to share.
*   **Design Rule:** Make the number as prominent as possible with a few supporting words. Do not force a single data point into a graph.

**Line Graphs**
*   **Use when:** Displaying continuous data, such as units of time (days, months, years) or frequency distributions. 
*   **Design Rule:** Never use line graphs for categorical (nominal) data.

**Slopegraphs**
*   **Use when:** You have exactly two time periods or two points of comparison and want to quickly show relative increases, decreases, or differences across categories.

**Bar Charts (Vertical and Horizontal)**
*   **Use when:** Plotting categorical data, rankings, or nominal comparisons.
*   **Design Rules:** 
    *   **Zero Baseline:** Because bars encode value by length, they **must always begin at a value of zero**.
    *   **Orientation:** Default to **Horizontal Bar Charts** if your category names are long; the text is written from left to right, making it much easier for the audience to read without turning their heads.

**Stacked Bar Charts**
*   **Use when:** You must compare totals across categories while also showing the subcomponent pieces.
*   **Design Rules:** Be cautious, as subcomponents (anything above the bottom baseline) are hard to compare accurately. For survey data (like a Likert scale from Disagree to Agree), use a **100% Stacked Horizontal Bar Chart** to provide a consistent baseline on both the left and right sides.

**Waterfall Charts**
*   **Use when:** You need to pull apart the pieces of a stacked bar chart to show a starting point, positive and negative changes, and the resulting ending point (e.g., headcount changes over a year). 

**Scatterplots**
*   **Use when:** You need to show the relationship between two things by encoding data simultaneously on a horizontal x-axis and vertical y-axis.

## 3. Visuals to ALWAYS Avoid

*   **Pie and Donut Charts:** Human visual perception is notoriously bad at comparing angles and 2D areas. Donut charts simply add a hole to a pie chart and ask the audience to compare arc lengths, which is equally difficult. Use a bar chart instead.
*   **3D Graphics:** Never use 3D to plot a single dimension. 3D elements add zero value, physically skew the numbers, and make the graph almost impossible to interpret accurately
*   **Secondary Y-Axes:** Displaying data against a second right-hand y-axis forces the audience to do the mental work of figuring out which data goes with which axis. Instead, either label the data points directly in the chart, or pull the graphs apart vertically into two separate graphs that share the same horizontal x-axis.