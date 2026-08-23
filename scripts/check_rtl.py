#!/usr/bin/env python3
"""RTL text helper: detect Hebrew/Arabic in chart text and print the correct
handling for the current environment.

DataInk's RTL policy is text-only RTL: the text renders right-to-left, but
chart geometry (bars, category order, time axes, value axis) stays
left-to-right — numbers are written left-to-right in Hebrew and Arabic too.

Usage:
    python3 check_rtl.py 'תל אביב הובילה את המכירות'
    python3 check_rtl.py 'Revenue by region'

Exit codes: 0 = no RTL characters (nothing to do), 3 = RTL text detected
(follow the printed instructions), 2 = usage error.
"""
import re
import sys
import unicodedata


def count_rtl(text):
    return sum(1 for ch in text if unicodedata.bidirectional(ch) in ("R", "AL"))


def matplotlib_advice():
    try:
        import matplotlib
    except ImportError:
        return (
            "matplotlib (not installed here — check the version in the target environment):\n"
            "  >= 3.11: pass logical-order strings AS-IS (native bidi support).\n"
            "           Do NOT apply bidi.get_display() — it double-reverses into garble.\n"
            "  <  3.11: apply bidi.algorithm.get_display() (pip install python-bidi)\n"
            "           to every displayed string: title, tick/axis labels, annotations."
        )
    version = matplotlib.__version__
    major_minor = tuple(int(x) for x in re.findall(r"\d+", version)[:2])
    if major_minor >= (3, 11):
        return (
            f"matplotlib {version} (>= 3.11, native bidi):\n"
            "  pass logical-order strings AS-IS.\n"
            "  Do NOT apply bidi.get_display() — it double-reverses into garble."
        )
    return (
        f"matplotlib {version} (< 3.11, no bidi):\n"
        "  apply bidi.algorithm.get_display() (pip install python-bidi) to every\n"
        "  displayed string: title, tick/axis labels, annotations."
    )


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    text = argv[1]
    n = count_rtl(text)
    if n == 0:
        print("No RTL characters detected — no special handling needed.")
        return 0

    print(f"RTL text detected ({n} Hebrew/Arabic characters).")
    print()
    print("Rules (text-only RTL — never mirror the chart):")
    print("  - Chart geometry stays left-to-right: bars, category order, time axes,")
    print("    value axis on the left. Numbers are LTR in Hebrew/Arabic too.")
    print("  - Anchor RTL titles right: matplotlib loc='right', plotly x=1 +")
    print("    xanchor='right', vega-lite title anchor 'end'. Right-justify")
    print("    multi-line RTL annotations.")
    print("  - Browser renderers (plotly, vega-lite, HTML, SVG): pass strings AS-IS —")
    print("    browsers apply the bidi algorithm natively. Never pre-reverse.")
    print("  - " + matplotlib_advice().replace("\n", "\n    "))
    print()
    print("Verify by rendering a test image — reversed glyph order is invisible in code:")
    print(f"  correct reads as:   {text}")
    print(f"  garbled looks like: {text[::-1]}")
    return 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))
