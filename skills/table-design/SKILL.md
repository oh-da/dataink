---
name: table-design
description: Designs clear, readable data tables — structure, alignment, number formatting, grouping, and summary rows. Use when presenting exact values, building reference or lookup tables, formatting tabular reports, or when a chart is the wrong medium.
allowed-tools: Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_contrast.py" *)
---

# Table Design

The user's request: "$ARGUMENTS"

Tables communicate through reading, not perception: use them when the audience needs to look up individual values, compare precise numbers, or see multiple units of measure side by side. If the message is a pattern, trend, or comparison, switch to the data-visualization skill.

## Critical Constraints

All shared rules in `../../assets/core-standards.md` apply (contrast, no color-only encoding, left-justified text, integrity). Table-specific additions:
- The data must dominate — structure (rules, fills, borders) stays in the background.
- Never center-align numbers or their headers.
- Avoid tables in live presentations — they pull audiences into reading mode.

## Instructions

### Step 1: Confirm the Medium
Verify a table is right: individual values, precise lookup, mixed units, or audit/appendix detail. Otherwise route to data-visualization.

### Step 2: Structure Rows and Columns
- Put the items being compared in **rows**, the measures in **columns** (scanning down a column compares values fastest).
- Sort rows by a meaningful order — value descending, natural sequence, or the reader's lookup key. Alphabetical only when readers look up by name.
- Group related columns under spanner headers; group related rows with white space, not boxes.

### Step 3: Format Numbers
- Consistent precision per column; round to the precision the decision needs (2–3 significant digits usually) — extra decimals are noise.
- Thousands separators; align on the decimal point.
- Put units, currency symbols, and % in the column header, not in every cell.
- Use tabular (fixed-width) figures so digits align vertically.

### Step 4: Align
- **Right-align numbers** and their headers. **Left-align text** and its headers. Never center either.
- Dates: align consistently (right or left) with a fixed format.

### Step 5: Delineate Lightly
- White space first; light rules (thin, light grey) only when spacing can't separate groups; full grids and heavy borders never.
- Zebra striping only for wide tables where the eye loses the row; keep the fill barely visible.
- Bold summary rows (totals, averages) and separate them with a single light rule.

### Step 6: Highlight (optional)
- To add at-a-glance magnitude without losing precision, overlay a heatmap fill or embed bars/sparklines — follow the branding workflow and 10% rule in `../../assets/core-standards.md`.
- Verify fill/text contrast:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_contrast.py" '#TEXT' '#FILL'
```

### Step 7: Accessibility and Output
- HTML output: real `<th>` header cells with `scope`, a `<caption>`, no layout-only tables.
- Ensure highlight fills are not the only encoding (pair with the value itself — always true in tables — but check conditional icons/colors carry labels).
- Produce the table in the user's preferred format (HTML, markdown, spreadsheet, LaTeX).

## Troubleshooting

**"Make the table pop with colors and borders":** structure competing with data slows lookup. Offer bold summary rows, a single accent for the key column, and white-space grouping instead.

**Too many columns to scan:** split into multiple tables by theme, or move secondary measures to an appendix table.
