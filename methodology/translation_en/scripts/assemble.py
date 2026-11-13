"""Write the English units and the English of each package.

translation/units/<package>/<unit>.tex: the translation that came back (runs/out/<unit>.tex), with the fixes of
checks/FIXES.jsonl for that unit applied in order. Nothing else is changed.
translation/packages/<package>_en.tex: the English units of the package joined as the French units are joined (the
blank lines at the cuts are the French's, source/MANIFEST.json "lead" and "trail"), a body like the French current text
(no preamble; the transcription's check wrapper answers/fixed/build/wrap.tex sets it). Written only for a package
whose units are all translated.

checks/FIXES.jsonl, one fix per line (the format of the Dérivateurs translation):
  {"unit": U, "kind": "replace", "old": "...", "new": "...", "count": n, "reason": "...", "by": "...", "date": "..."}
  {"unit": U, "kind": "regex", "pattern": "...", "repl": "...", "count": n, "scope": "prose"|"all", ...}
"count" is the number of places the fix must find (the script stops if it finds another number); "scope": "prose"
applies a regex outside formulas and comment lines only.
usage: python -I -B assemble.py [UNIT ...]
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
FIXES = os.path.join(T.ROOT, "checks", "FIXES.jsonl")
SEG = re.compile(r"(?<!\\)%[^\n]*|\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\begin\{(" +
                 T.GC.MATH_ENVS + r")\}.*?\\end\{\1\}", re.S)


def fixes():
    if not os.path.exists(FIXES):
        return []
    return [json.loads(x) for x in T.read(FIXES).splitlines() if x.strip()]


def sub_prose(pattern, repl, text):
    """re.subn outside formulas and comments."""
    out, i, n = [], 0, 0
    for m in SEG.finditer(text):
        part, k = re.subn(pattern, repl, text[i:m.start()])
        out += [part, m.group(0)]
        n += k
        i = m.end()
    part, k = re.subn(pattern, repl, text[i:])
    out.append(part)
    return "".join(out), n + k


def apply_fixes(unit, text):
    for f in [x for x in fixes() if x["unit"] == unit]:
        if f["kind"] == "replace":
            n = text.count(f["old"])
            if n != f["count"]:
                raise SystemExit("%s: fix %r found %d times, expected %d" % (unit, f["old"][:60], n, f["count"]))
            text = text.replace(f["old"], f["new"])
        elif f["kind"] == "regex":
            if f.get("scope") == "prose":
                text, n = sub_prose(f["pattern"], f["repl"], text)
            else:
                text, n = re.subn(f["pattern"], f["repl"], text)
            if n != f["count"]:
                raise SystemExit("%s: regex fix %r applied %d times, expected %d" % (unit, f["pattern"][:60], n,
                                                                                    f["count"]))
        else:
            raise SystemExit("unknown fix kind " + f["kind"])
    return text


def write_if_changed(path, text):
    """Write only when the content differs (files that did not change keep their date: since 12 Nov, while a review
    reads the pilot's units, nothing it reads is rewritten)."""
    if os.path.exists(path) and T.read(path) == text:
        return False
    T.write(path, text)
    return True


def main():
    want = set(sys.argv[1:])
    us = T.units()
    done = 0
    for u in us:
        if want and u["id"] not in want:
            continue
        p = os.path.join(T.ROOT, "runs", "out", u["id"] + ".tex")
        if not os.path.exists(p):
            continue
        text = apply_fixes(u["id"], T.read(p).strip("\n") + "\n")
        write_if_changed(os.path.join(T.ROOT, "translation", "units", u["package"], u["id"] + ".tex"), text)
        done += 1
    npk = 0
    for pk in T.manifest()["packages"]:
        parts = []
        for uid in pk["units"]:
            u = T.unit_map()[uid]
            p = os.path.join(T.ROOT, "translation", "units", u["package"], uid + ".tex")
            if not os.path.exists(p):
                parts = None
                break
            parts.append(u["lead"] + T.read(p).strip("\n") + u["trail"])
        if parts is None:
            continue
        write_if_changed(os.path.join(T.ROOT, "translation", "packages", pk["package"] + "_en.tex"), "".join(parts))
        npk += 1
    print("English units written: %d; packages complete: %d of %d" % (done, npk, len(T.manifest()["packages"])))


if __name__ == "__main__":
    main()
