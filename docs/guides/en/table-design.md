# Making a Table (table-design)

**What it does:** lays out numbers in a table people can actually read — the
right sort order, clean alignment, no visual clutter.

**Use it when:** your readers need to look up *exact* values: a price list, a
budget breakdown, quarterly results for an appendix. If they only need the
overall pattern ("sales are growing"), a chart is better — and the skill will
tell you that and hand you over.

## A realistic use case

Finance asked for the quarterly numbers per region — revenue, cost, and
margin — for the back of the board pack. People will scan it for specific
figures, so precision matters more than pretty.

## Try it now (copy-paste and edit)

```
/dataink:table-design Make a reference table for our board pack appendix.
Regions: North, South, East, West. For each: Q1 and Q2 revenue, cost, and
margin %. Readers will look up exact values. Here's the data: ...
```

## What happens next

1. Claude puts the things you compare (regions) in rows and the measures
   (revenue, cost, margin) in columns — scanning down a column is the fastest
   way to compare.
2. It sorts rows in an order that means something (biggest first), not
   alphabetically by default.
3. Numbers get lined up on the right with the same number of decimals, and the
   € / $ / % symbols move into the column header so the cells stay clean.
4. Instead of a cage of gridlines, it separates groups with white space and,
   at most, thin light lines.
5. Totals get a bold row at the bottom so they're easy to find.

## How to know you got a good one

- You can run your eye down a column and compare numbers without effort.
- Decimals line up; nothing is centered.
- The units appear once (in the header), not in every cell.
- It looks calm — the numbers stand out, not the lines around them.

## One warning it will give you

Don't put a big table on a live presentation slide. The moment it appears,
everyone stops listening to you and starts reading. Tables belong in
documents and appendices; slides get one chart or one big number.
