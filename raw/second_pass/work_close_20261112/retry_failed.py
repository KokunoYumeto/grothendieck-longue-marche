"""For the current texts that fail in the check wrapper: compile (a) the text as it is in wrap_alt.tex (the wrapper the
P10 pass used), and (b) a copy after the reader build's mechanical LaTeX repairs (fix_tikzcd_in_macros.py,
unwrap_gathered_diagrams.py, normalize_reader_text.py; content unchanged) in the check wrapper. The texts themselves
are not changed. Writes retry_failed.tsv. usage: python -I retry_failed.py KEY..."""
import pathlib
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
SP = W.parent
L = SP.parent
BD = W / "build" / "retry"
BD.mkdir(parents=True, exist_ok=True)
WRAP = (L / "answers" / "fixed" / "build" / "wrap.tex").read_text(encoding="utf-8")
ALT = (W / "wrap_alt.tex").read_text(encoding="utf-8")


def run(name, wrap, body):
    (BD / f"{name}.tex").write_text(wrap.replace("BODYFILE", body.as_posix()), encoding="utf-8")
    subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"], cwd=BD,
                   capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
    log = (BD / f"{name}.log").read_text(encoding="utf-8", errors="replace")
    m = re.search(r"Output written on .*?\((\d+) page", log)
    for ext in (".aux", ".pdf"):
        (BD / f"{name}{ext}").unlink(missing_ok=True)
    if m:
        return "OK " + m.group(1) + " pp"
    return "FAIL " + " ".join((re.findall(r"^! .*", log, re.M) or [""])[:1] + (re.findall(r"^l\.\d+.*", log, re.M) or [""])[:1])


rows = ["package\tcurrent_text\talt_wrapper\tafter_reader_repairs"]
for k in [a for a in sys.argv[1:] if not a.startswith("--")]:
    base = "LM_P057api" if k == "LM_P057" else k
    f = SP / f"{base}_checked_fixed.tex"
    f = f if f.exists() else SP / f"{base}_checked.tex"
    a = run(f"alt_{k}", ALT, f)
    c = BD / f"rep_{k}_body.tex"
    shutil.copyfile(f, c)
    for s in ("fix_tikzcd_in_macros.py", "unwrap_gathered_diagrams.py", "normalize_reader_text.py"):
        subprocess.run([sys.executable, "-I", "-B", str(L / s), str(c)], capture_output=True)
    b = run(f"rep_{k}", WRAP, c)
    rows.append(f"{k}\t{f.name}\t{a}\t{b}")
    print(k, "| alt wrapper:", a, "| after repairs:", b, flush=True)
(W / "retry_failed.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
