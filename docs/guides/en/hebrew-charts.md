# Charts in Hebrew (hebrew / RTL text)

**The problem:** ask most AI tools for a chart in Hebrew and the labels come
out mirror-reversed — "תל אביב" becomes "ביבא לת". The code looks perfectly
fine; only the rendered picture is broken, so nobody notices until it's on a
slide in front of people who read Hebrew.

**The rule DataInk follows:** only the *text* is right-to-left. The chart
itself stays left-to-right — bars, category order, time axes, and the numbers —
because numbers are written left-to-right in Hebrew too. Nothing gets mirrored;
the title simply moves to the right edge, where Hebrew reading starts.

## Try it now (copy-paste and edit)

```
/dataink:data-visualization צור גרף עמודות של מכירות לפי עיר: תל אביב 61,
ירושלים 48, חיפה 39, באר שבע 27. תל אביב היא הסיפור.
```

## What happens next

1. Claude detects the Hebrew text and checks how your charting tool handles
   it — this genuinely differs by library *and version*. Older matplotlib
   (before 3.11) reverses Hebrew unless the text is pre-processed; 3.11 and
   newer handle it by itself, and pre-processing there *creates* the garble.
   The plugin ships a small checker (`check_rtl.py`) that prints the right
   move for your environment, so nothing is guessed.
2. Web-based charts (plotly, HTML) get the text as-is — browsers handle
   Hebrew correctly on their own.
3. The title anchors to the right edge. Bars, axes, and numbers stay exactly
   where they'd be in an English chart.
4. Claude renders a test image and reads a label back before finishing,
   because reversed text is invisible in the code.

## How to know it worked

- Pick one word — a city name — and read it in the final image, letter by
  letter. Correct: ירושלים. Broken: םילשורי.
- The bars run left-to-right and the axis numbers read normally.
- The title sits at the top-right.

## If you got garbled text anyway

Run the review skill on the image ("Review this chart — the labels are in
Hebrew"). Reversed Hebrew is a must-fix finding there, with the exact repair
steps for your library version.
