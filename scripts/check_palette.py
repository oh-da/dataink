#!/usr/bin/env python3
"""Palette checker: pairwise distinguishability under normal vision and
simulated color-vision deficiency (CVD).

Usage:
    python3 check_palette.py '#E69F00,#56B4E9,#009E73,#0072B2'
    python3 check_palette.py '#E69F00,#56B4E9' --bg '#FFFFFF'

For every pair of palette colors, computes the CIE76 delta-E distance under
normal vision and under simulated protanopia, deuteranopia, and tritanopia
(Machado et al. 2009 severity-1.0 matrices). Pairs closer than DELTA_E_MIN
in any condition are flagged as confusable. With --bg it also reports the
WCAG contrast of each color against the background (3:1 non-text threshold).

Exit code 0 if the palette is CVD-safe (no confusable pairs), 1 otherwise.
"""
import sys

DELTA_E_FAIL = 12.0  # below this, colors are genuinely confusable (pure red/green scores ~10)
DELTA_E_WARN = 20.0  # 12-20: distinguishable but tight — redundant encoding recommended

# Machado, Oliveira & Fernandes (2009), severity 1.0, applied in linear RGB
CVD_MATRICES = {
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}


def parse_hex(color):
    h = color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) != 6:
        raise ValueError(f"not a hex color: {color!r}")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def to_srgb(c):
    c = min(1.0, max(0.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def simulate(rgb, matrix):
    lin = tuple(to_linear(c) for c in rgb)
    sim = tuple(sum(m * c for m, c in zip(row, lin)) for row in matrix)
    return tuple(to_srgb(c) for c in sim)


def rgb_to_lab(rgb):
    r, g, b = (to_linear(c) for c in rgb)
    # sRGB D65 -> XYZ
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(rgb1, rgb2):
    l1, l2 = rgb_to_lab(rgb1), rgb_to_lab(rgb2)
    return sum((a - b) ** 2 for a, b in zip(l1, l2)) ** 0.5


def contrast(rgb1, rgb2):
    def lum(rgb):
        r, g, b = (to_linear(c) for c in rgb)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    l1, l2 = lum(rgb1), lum(rgb2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    bg = None
    if "--bg" in argv:
        i = argv.index("--bg")
        if i + 1 >= len(argv):
            print("error: --bg requires a color argument")
            return 2
        bg = argv[i + 1]
        if bg in args:
            args.remove(bg)
    if len(args) != 1:
        print(__doc__)
        return 2

    names = [c.strip() for c in args[0].split(",") if c.strip()]
    if len(names) < 2:
        print("error: need at least 2 colors")
        return 2
    try:
        colors = [parse_hex(c) for c in names]
    except ValueError as e:
        print(f"error: {e}")
        return 2

    conditions = {"normal": None}
    conditions.update(CVD_MATRICES)

    confusable, borderline = [], []
    for cond, matrix in conditions.items():
        sim = colors if matrix is None else [simulate(c, matrix) for c in colors]
        worst = None
        for i in range(len(sim)):
            for j in range(i + 1, len(sim)):
                de = delta_e(sim[i], sim[j])
                if worst is None or de < worst[0]:
                    worst = (de, names[i], names[j])
                if de < DELTA_E_FAIL:
                    confusable.append((cond, names[i], names[j], de))
                elif de < DELTA_E_WARN:
                    borderline.append((cond, names[i], names[j], de))
        de, a, b = worst
        print(f"{cond:<13} closest pair: {a} vs {b}  deltaE={de:.1f}")

    if bg is not None:
        print(f"\ncontrast vs background {bg} (non-text threshold 3.0:1):")
        bg_rgb = parse_hex(bg)
        for name, rgb in zip(names, colors):
            ratio = contrast(rgb, bg_rgb)
            print(f"  {name}: {ratio:.2f}:1 {'PASS' if ratio >= 3.0 else 'FAIL'}")

    if confusable:
        print(f"\nNOT CVD-safe — confusable pairs (deltaE < {DELTA_E_FAIL:.0f}):")
        for cond, a, b, de in confusable:
            print(f"  [{cond}] {a} vs {b}  deltaE={de:.1f}")
        print("Replace one color of each pair, or do not rely on color to separate them.")
        return 1
    if borderline:
        print(f"\nCVD-safe with warnings — tight pairs (deltaE {DELTA_E_FAIL:.0f}-{DELTA_E_WARN:.0f}):")
        for cond, a, b, de in borderline:
            print(f"  [{cond}] {a} vs {b}  deltaE={de:.1f}")
        print("Distinguishable, but pair these with redundant encoding (labels/patterns/markers).")
        return 0
    print(f"\nCVD-safe: all pairs clearly distinguishable (deltaE >= {DELTA_E_WARN:.0f}) in all conditions.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
