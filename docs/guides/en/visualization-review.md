# Checking a Chart (visualization-review)

**What it does:** inspects a chart you already have and tells you exactly
what's wrong, what's risky, and what's just cosmetic — each with a concrete
fix.

**Use it when:** you (or a colleague, or an old report) made a chart and you
want to be sure it isn't misleading, unreadable, or embarrassing before it
goes out.

## A realistic use case

Marketing sent you a slide with a 12-slice pie chart, red-green coloring, and
the title "Market Share". It goes on the public website tomorrow. Something
feels off but you can't name it.

## Try it now (copy-paste, attach the chart)

```
/dataink:visualization-review Review this chart before we publish it on our
website tomorrow. [paste the image, the chart code, or just describe it]
```

It works with a screenshot, the code that made the chart, or even a plain
description.

## What happens next

Claude checks the chart against a fixed rule list, in three levels of
seriousness, and reports them in order:

1. **Must fix** — things that mislead people or lock them out: the wrong kind
   of chart for the job, bars that don't start at zero (they exaggerate
   differences), meaning carried by color alone (invisible to roughly 1 in 12
   men, who are color-blind), text too faint to read, no text alternative for
   screen readers.
2. **Should fix** — things that make it slow or fuzzy: a vague title, too many
   overlapping lines, a legend where direct labels would do, missing units.
3. **Nice to fix** — polish: inconsistent fonts, leftover decoration.

For color problems it doesn't eyeball anything — it reads the actual color
values and runs a checking tool on them. If it can't get at the colors, it
says "not verified" instead of guessing.

## How to know it worked

- Every problem comes with a specific fix ("replace the 12-slice pie with a
  sorted bar chart"), not just a complaint.
- The must-fix list is what you deal with today; the rest can wait.
- If a level is clean, it says so — no invented problems.

## Bonus

Ask "now apply the fixes" and it will rebuild the chart following its own
report, then re-run the checks to prove the problems are gone.
