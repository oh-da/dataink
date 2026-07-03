#!/usr/bin/env python3
"""WCAG 2.x contrast ratio checker.

Usage:
    python3 check_contrast.py '#333333' '#FFFFFF'

Prints the contrast ratio and pass/fail verdicts for the WCAG AA thresholds
used throughout the DataInk skills:
  - normal text        : >= 4.5:1
  - large text         : >= 3.0:1  (>=18pt, or >=14pt bold)
  - non-text data marks: >= 3.0:1  (bars, lines, points vs. background)

Exit code 0 if the pair passes at least the non-text threshold, 1 otherwise.
"""
import sys


def parse_hex(color: str) -> tuple:
    h = color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) != 6:
        raise ValueError(f"not a hex color: {color!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def channel_to_linear(c: int) -> float:
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple) -> float:
    r, g, b = (channel_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = relative_luminance(parse_hex(fg))
    l2 = relative_luminance(parse_hex(bg))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    fg, bg = argv[1], argv[2]
    try:
        ratio = contrast_ratio(fg, bg)
    except ValueError as e:
        print(f"error: {e}")
        return 2

    def verdict(threshold):
        return "PASS" if ratio >= threshold else "FAIL"

    print(f"contrast ratio {fg} on {bg}: {ratio:.2f}:1")
    print(f"  AA normal text   (>=4.5:1): {verdict(4.5)}")
    print(f"  AA large text    (>=3.0:1): {verdict(3.0)}")
    print(f"  AA non-text mark (>=3.0:1): {verdict(3.0)}")
    return 0 if ratio >= 3.0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
