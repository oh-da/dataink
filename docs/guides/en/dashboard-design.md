# Making a Dashboard (dashboard-design)

**What it does:** designs a single screen that answers "how are we doing?" in
five seconds.

**Use it when:** someone (maybe you) will check the same numbers every day or
week and needs to spot problems fast — a business overview, a service monitor,
a sales tracker.

## A realistic use case

You run a small online shop. You want one screen you open every Monday that
shows this week's revenue, orders, and returns — and makes it obvious when
something needs attention.

## Try it now (copy-paste and edit)

```
/dataink:dashboard-design Design a weekly dashboard for my online shop.
Metrics I track: revenue, orders, returns, average order value, top products,
traffic, conversion rate, support tickets. I check it Monday mornings to
decide what needs attention this week.
```

## What happens next

1. Claude asks the key question first: which one to three numbers actually
   answer "is this a good week?" Those become big tiles in the top row.
2. Everything else becomes supporting context lower down — or gets cut. It
   will push back if you ask for fifteen equally-sized numbers, because then
   nothing stands out.
3. Each metric gets the right little display: a big number with a mini trend
   line behind it, a compact bar showing progress toward a target, a short
   ranked list for top products.
4. It arranges the screen the way people read: most important top-left,
   details toward the bottom, everything lined up on a grid.
5. Red is reserved for one job only: "this needs attention" — and always with
   a label, never as the only clue.

## How to know you got a good one

- The five-second test: look at it, look away — can you say whether the week
  is fine and what (if anything) is off-track? That's the whole job.
- It fits on one screen with no scrolling.
- Exactly one place (or zero) is shouting for attention.

## Things it will refuse to do (and why)

- **Gauges and speedometer dials** — they take a lot of space to show one
  number badly. You'll get a compact bar-vs-target instead.
- **Cramming every metric on screen** — each extra number steals attention
  from all the others. Less important metrics move to a detail view.
