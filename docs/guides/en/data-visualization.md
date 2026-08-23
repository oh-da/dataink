# Making a Chart (data-visualization)

**What it does:** turns your numbers into one clear chart that makes its point
in seconds.

**Use it when:** you have data in a spreadsheet, a report, or your head, and
you need a chart for a slide, a document, or a message to your team.

## A realistic use case

You run a small team. Sales have been climbing since the new website launched
in May, and you want tomorrow's meeting to open with a chart that shows it.

## Try it now (copy-paste and edit the numbers)

```
/dataink:data-visualization Monthly sales for 2025: Jan 42k, Feb 45k, Mar 41k,
Apr 48k, May 52k, Jun 58k, Jul 61k, Aug 57k. Sales took off after our new
website launched in May. Make a chart for my team meeting slide.
```

## What happens next

1. Claude checks a chart is even the right tool (sometimes a table or a single
   big number works better — it will say so).
2. It picks the chart type that fits your data — numbers over time get a line,
   comparisons get bars, and so on.
3. It removes everything that isn't your data: borders, backgrounds, heavy
   gridlines.
4. It colors only the important part (the jump after May) and keeps the rest
   quiet grey, so your eye goes straight to the point.
5. It runs a small tool that mathematically checks the colors are readable —
   including for color-blind readers — instead of guessing.
6. It writes the chart title as the takeaway ("Sales up 40% since the website
   launch"), not a label ("Monthly Sales").

## How to know you got a good one

- You look at it for three seconds and can say the point out loud.
- The title already says that point.
- One color stands out; everything else is grey.
- Bars (if any) start at zero — so differences look as big as they really are.

## Things it will refuse to do (and why)

- **Pie charts with lots of slices** — human eyes are bad at comparing slice
  sizes. You'll get a sorted bar chart instead, which reads instantly.
- **3D charts** — the tilt distorts the numbers.
- **A rainbow of colors** — when everything stands out, nothing does.
