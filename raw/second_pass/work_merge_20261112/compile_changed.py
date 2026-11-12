"""Compile each changed second-pass file in the check wrapper (answers/fixed/build/wrap.tex); with --before, the dated
copies instead. usage: python -I compile_changed.py [--before] PKG..."""
import pathlib, re, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent; SP = W.parent; L = SP.parent
WRAP = (L / "answers" / "fixed" / "build" / "wrap.tex").read_text(encoding="utf-8")
BD = W / "build"; BD.mkdir(exist_ok=True)
before = "--before" in sys.argv
for pkg in [a for a in sys.argv[1:] if not a.startswith("--")]:
    body = (W / f"{pkg}_checked_fixed_before_20261112.tex") if before else (SP / f"{pkg}_checked_fixed.tex")
    name = ("before_" if before else "") + pkg
    (BD / f"{name}.tex").write_text(WRAP.replace("BODYFILE", body.as_posix()), encoding="utf-8")
    subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"], cwd=BD,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
    log = (BD / f"{name}.log").read_text(encoding="utf-8", errors="replace")
    ok = "Output written on" in log
    err = re.findall(r"^! .*", log, re.M)[:1] + re.findall(r"^l\.\d+.*", log, re.M)[:1]
    pages = re.search(r"Output written on .*?\((\d+) page", log)
    print(name, "OK" if ok else "FAIL", pages.group(1) + " pp" if pages else "", err)
