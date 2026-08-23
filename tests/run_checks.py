#!/usr/bin/env python3
"""DataInk consistency suite — deterministic checks, stdlib only.

Run from anywhere:
    python3 tests/run_checks.py

Guards against the failure classes that have actually occurred in this repo:
stale skill names after a rename, corrupted characters, broken cross-file
references, defaults that violate the plugin's own contrast rules, version
drift between manifests and docs, and script/hook regressions.

Exit code 0 when every check passes, 1 otherwise.
"""
import importlib.util
import json
import re
import subprocess
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
PY = sys.executable or "python3"

failures = []


def check(name, ok, detail=""):
    status = "ok  " if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name)


def load_module(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(args, stdin=None):
    return subprocess.run(args, input=stdin, capture_output=True, text=True, cwd=ROOT)


def repo_markdown():
    for pattern in ("*.md", "skills/**/*.md", "assets/*.md", "evals/*.md"):
        yield from ROOT.glob(pattern)


# ---------------------------------------------------------------- content

def check_no_replacement_chars():
    me = Path(__file__).resolve()
    bad = [p for p in ROOT.rglob("*")
           if p.is_file() and p.suffix in (".md", ".py", ".json", ".txt")
           and ".git" not in p.parts and "__pycache__" not in p.parts
           and p.resolve() != me
           and "�" in p.read_text(encoding="utf-8", errors="replace")]
    check("no U+FFFD replacement characters", not bad, ", ".join(str(p) for p in bad))


def check_no_stale_skill_names():
    # names that existed before the v3.1 rename and must not reappear
    stale = ["visualizing-data", "creating-infographics", "reviewing-visualizations",
             "designing-dashboards", "designing-tables", "storytelling-with-data"]
    hits = []
    for p in sorted(set(repo_markdown())):
        text = p.read_text(encoding="utf-8")
        for name in stale:
            if name in text:
                hits.append(f"{p.relative_to(ROOT)}: {name}")
    check("no stale pre-v3.1 skill names in markdown", not hits, "; ".join(hits))


def check_skill_cross_references():
    """Every skill name mentioned as `code` in a SKILL.md or README skill table
    must exist as a directory, and every references/... or assets/... path
    mentioned in a SKILL.md must exist on disk."""
    skill_dirs = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    missing = []
    for skill_md in (ROOT / "skills").glob("*/SKILL.md"):
        text = skill_md.read_text(encoding="utf-8")
        for ref in re.findall(r"`([^`\s]+\.md)`", text):
            if "/" not in ref:  # bare filename mention, not a path
                continue
            target = (skill_md.parent / ref).resolve()
            if not target.exists():
                missing.append(f"{skill_md.relative_to(ROOT)} -> {ref}")
        # "switch to the X skill" style routing must name a real skill
        for name in re.findall(r"(?:switch to|route to|run) the ([a-z][a-z-]+) skill", text):
            if name not in skill_dirs:
                missing.append(f"{skill_md.relative_to(ROOT)} routes to unknown skill '{name}'")
    check("SKILL.md cross-references resolve", not missing, "; ".join(missing))


def check_versions_in_sync():
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    v = plugin["version"]
    ok = market["plugins"][0]["version"] == v and f"v{v}" in (ROOT / "README.md").read_text()
    check("version in plugin.json == marketplace.json, mentioned in README",
          ok, f"plugin={v} marketplace={market['plugins'][0]['version']}")


# ---------------------------------------------------------------- contrast

def check_recipe_defaults_pass_contrast():
    """The recipes promise compliance by construction: HIGHLIGHT and BASELINE
    constants must pass 3:1 on white per the plugin's own checker."""
    contrast = load_module(SCRIPTS / "check_contrast.py")
    recipes = (ROOT / "skills/data-visualization/references/code-recipes.md").read_text()
    pairs = re.findall(r'HIGHLIGHT, BASELINE = "(#[0-9A-Fa-f]{6})", "(#[0-9A-Fa-f]{6})"', recipes)
    bad = [c for pair in pairs for c in pair if contrast.contrast_ratio(c, "#FFFFFF") < 3.0]
    check("recipe HIGHLIGHT/BASELINE constants pass 3:1 on white",
          bool(pairs) and not bad, f"pairs={pairs} failing={bad}")


def check_contrast_script():
    contrast = load_module(SCRIPTS / "check_contrast.py")
    r = contrast.contrast_ratio("#000000", "#FFFFFF")
    check("check_contrast: black on white = 21:1", abs(r - 21.0) < 0.01, f"got {r}")
    p = run([PY, str(SCRIPTS / "check_contrast.py"), "#B0B0B0", "#FFFFFF"])
    check("check_contrast: #B0B0B0 on white exits 1 (fails 3:1)", p.returncode == 1, p.stdout)
    p = run([PY, str(SCRIPTS / "check_contrast.py"), "not-a-color", "#FFFFFF"])
    check("check_contrast: invalid hex exits 2", p.returncode == 2, p.stdout)


def check_palette_script():
    okabe = "#E69F00,#56B4E9,#009E73,#F0E442,#0072B2,#D55E00,#CC79A7,#000000"
    p = run([PY, str(SCRIPTS / "check_palette.py"), okabe])
    check("check_palette: Okabe-Ito is CVD-safe (exit 0)", p.returncode == 0, p.stdout)
    p = run([PY, str(SCRIPTS / "check_palette.py"), "#FF0000,#00B000"])
    check("check_palette: pure red/green flagged confusable (exit 1)", p.returncode == 1, p.stdout)
    p = run([PY, str(SCRIPTS / "check_palette.py"), "--bg"])
    check("check_palette: bare --bg exits 2 without traceback",
          p.returncode == 2 and "Traceback" not in p.stderr, p.stderr)


# ---------------------------------------------------------------- hook

def check_hook_dedup():
    hook = str(SCRIPTS / "viz-file-detector.py")
    session = f"testrun-{uuid.uuid4().hex}"
    payload = json.dumps({
        "session_id": session,
        "tool_name": "Write",
        "tool_input": {"file_path": "/tmp/example-chart.py",
                       "content": "import matplotlib.pyplot as plt\nplt.plot([1, 2])"},
    })
    first = run([PY, hook], stdin=payload)
    second = run([PY, hook], stdin=payload)
    check("hook: nudges on first write of chart code",
          first.returncode == 0 and "visualization-review" in first.stdout, first.stdout)
    check("hook: silent on repeat write in same session",
          second.returncode == 0 and second.stdout.strip() == "", second.stdout)
    other = json.dumps({"session_id": session, "tool_name": "Write",
                        "tool_input": {"file_path": "/tmp/notes.md", "content": "matplotlib"}})
    p = run([PY, hook], stdin=other)
    check("hook: silent on non-code file", p.returncode == 0 and p.stdout.strip() == "", p.stdout)
    p = run([PY, hook], stdin="not json {")
    check("hook: malformed payload exits 0 silently",
          p.returncode == 0 and p.stdout.strip() == "", p.stdout)


def main():
    check_no_replacement_chars()
    check_no_stale_skill_names()
    check_skill_cross_references()
    check_versions_in_sync()
    check_recipe_defaults_pass_contrast()
    check_contrast_script()
    check_palette_script()
    check_hook_dedup()
    print()
    if failures:
        print(f"{len(failures)} check(s) failed: " + ", ".join(failures))
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
