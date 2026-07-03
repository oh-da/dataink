#!/usr/bin/env python3
"""PostToolUse hook: detect when a chart-producing file is written and nudge
toward running the DataInk visualization-review skill.

Receives the Claude Code hook payload on stdin (JSON with tool_name and
tool_input). If the written/edited file is code that uses a charting library,
emits additionalContext suggesting a P0 review. Always exits 0 — a detector
must never block the session.
"""
import json
import re
import sys

CODE_EXTENSIONS = (
    ".py", ".ipynb", ".r", ".R", ".Rmd", ".jl",
    ".js", ".jsx", ".ts", ".tsx", ".mjs", ".svelte", ".vue",
    ".html", ".htm", ".json", ".vg.json", ".vl.json",
)

# word-ish signatures of charting libraries
SIGNATURES = re.compile(
    r"matplotlib|pyplot|seaborn|plotly|altair|bokeh|vega|echarts|highcharts"
    r"|recharts|chart\.js|chartjs|nivo|visx|ggplot|plotnine|d3\.(select|scale|axis)"
    r"|<svg[^>]*viewBox",
    re.IGNORECASE,
)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return

    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path") or ""
    if not file_path.endswith(CODE_EXTENSIONS):
        return

    # Prefer the just-written content from the payload; fall back to disk.
    text = tool_input.get("content") or tool_input.get("new_string") or ""
    if not text:
        try:
            with open(file_path, encoding="utf-8", errors="ignore") as f:
                text = f.read(200_000)
        except OSError:
            return

    if not SIGNATURES.search(text):
        return

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                f"{file_path} appears to render a data visualization. Before "
                "finishing, run the dataink visualization-review skill on it "
                "(P0 checks at minimum: chart-task fit, scales, color-only "
                "encoding, WCAG contrast via scripts/check_contrast.py, alt text)."
            ),
        }
    }))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
