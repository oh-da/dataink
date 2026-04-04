# P2 Rules — Style, Consistency, Polish

These are suggestions for improving professionalism, consistency, and aesthetics.

## 13. Inconsistent Design Tokens
- Mixed fonts, sizes, or colors across a multi-chart report or dashboard
- Different chart styles for similar data within the same document
- **Fix:** Standardize on a single type hierarchy, color palette, and chart style.

## 14. Excess Non-Data Ink
- Heavy gridlines, borders, or background shading that compete with data
- Decorative gradients, shadows, or 3D effects
- Chartjunk that adds no analytical value
- **Fix:** Strip to essentials. Render structure in light grey. Reserve visual weight for data.

## 15. Palette Misuse
- Rainbow/jet palette for sequential data (false perceptual boundaries)
- Categorical palette for ordered/continuous data
- Too many distinct colors (>8 categories without grouping)
- **Fix:** Switch to perceptually uniform sequential (viridis/cividis) or appropriate categorical (Okabe-Ito). Group small categories into "other."

## 16. Layout Issues
- Diagonal text labels
- Center-aligned text elements
- Poor white space — cramped layout with no breathing room
- Misaligned chart elements across panels
- **Fix:** Horizontal text only. Left-justify. Add margins. Align chart edges.
