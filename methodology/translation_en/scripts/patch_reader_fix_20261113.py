"""Patch build.py's reader command (13 Nov 2026, Claude Opus 5.5):
1. the mechanical LaTeX repairs only for the packages that need them (COMPILE.tsv says "after ... repairs"); applied to
   every package they turned LM_P07's \\inserted{$\\operatorname{int}(...)$} into a stray $$ (8 LaTeX errors);
2. glyphs Latin Modern lacks: his Cyrillic (Belyi's name), U+2243 in text (DejaVu Serif), U+27CB/U+27CD in math
   (STIX Two Math, range only).
usage: python -I -B patch_reader_fix_20261113.py"""
from pathlib import Path

BS = chr(92)
p = Path(__file__).resolve().parent / "build.py"
lines = p.read_text(encoding="utf-8").split("\n")
src = "\n".join(lines)
assert "REPAIRED" not in src and "FONTFIX" not in src, "already patched"
# module-level FONTFIX after WRAP = ...
i = next(k for k, l in enumerate(lines) if l.startswith("WRAP = "))
lines[i + 1:i + 1] = [
    "CYR = \"" + "".join(chr(c) for c in range(0x410, 0x450)) + "\"",
    "FONTFIX = (\"" + BS * 2 + "usepackage{newunicodechar}" + BS + "n" + BS * 2 + "newfontfamily" + BS * 2
    + "cyrfont{DejaVu Serif}[Scale=MatchLowercase]" + BS + "n\"",
    "           + \"\".join(\"" + BS * 2 + "newunicodechar{%s}{{" + BS * 2 + "cyrfont" + BS * 2 + "char\\\"%04X}}"
    + BS + "n\" % (c, ord(c)) for c in CYR)",
    "           + \"" + BS * 2 + "newunicodechar{" + BS + "u2243}{" + BS * 2 + "ensuremath{" + BS * 2 + "simeq}}" + BS + "n\"",
    "           + \"" + BS * 2 + "setmathfont{Latin Modern Math}" + BS + "n" + BS * 2
    + "setmathfont{STIX Two Math}[range={\\\"27CB,\\\"27CD}]" + BS + "n\")",
]
src = "\n".join(lines)
# after the hyperref line in cmd_reader
lines = src.split("\n")
j = next(k for k, l in enumerate(lines) if "hidelinks" in l and l.strip().startswith("pre +="))
lines[j + 1:j + 1] = ["    pre += FONTFIX  # glyphs Latin Modern lacks (13 Nov 2026)"]
k = next(k for k, l in enumerate(lines) if l.strip() == "missing = []")
lines[k + 1:k + 1] = [
    "    REPAIRED = {l.split(\"" + BS + "t\")[0] for l in T.read(os.path.join(B, \"COMPILE.tsv\")).splitlines()[1:]",
    "                if \"repairs\" in l}",
]
m = next(k for k, l in enumerate(lines) if l.strip() == "repaired_copy(src, cp)")
ind = lines[m][:len(lines[m]) - len(lines[m].lstrip())]
lines[m:m + 1] = [
    ind + "if pk[\"package\"] in REPAIRED:",
    ind + "    repaired_copy(src, cp)",
    ind + "else:",
    ind + "    shutil.copyfile(src, cp)  # compiles as it is; the repairs broke LM_P07 (13 Nov 2026)",
]
p.write_text("\n".join(lines), encoding="utf-8")
print("patched", p)
