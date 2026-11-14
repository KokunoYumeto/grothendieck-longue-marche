#!/usr/bin/env python3
"""Compile a separate QA wrapper without editing the source transcription."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys


def run_logged(command: list[str], directory: Path, env: dict[str, str], log: Path) -> int:
    result = subprocess.run(command, cwd=directory, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.write_text(result.stdout, encoding="utf-8")
    print(f"Exit {result.returncode}; log: {log}")
    print(result.stdout[-3500:])
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Source TeX fragment; never modified")
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parents[2] / "tex-qa" / "build")
    args = parser.parse_args()
    source = args.input.resolve(strict=True)
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    wrapper = Path(__file__).resolve().with_name("qa-wrapper.tex")
    # These trees exist; removing !! bypasses broken system ls-R symlinks.
    env = os.environ.copy()
    env["TEXMF"] = "{/usr/local/share/texmf,/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
    env["TEXMFVAR"] = str(output / "texmf-var")
    env["TEXMFCONFIG"] = str(output / "texmf-config")
    env["TEXMFOUTPUT"] = str(output)
    env["TEXFORMATS"] = str(output) + "//:"
    env["TEXINPUTS"] = str(source.parent) + ":" + str(wrapper.parent) + ":"
    if not (output / "xelatex.fmt").is_file():
        rc = run_logged(["xelatex", "-ini", "-etex", "-no-shell-escape",
                         "-interaction=nonstopmode", "-halt-on-error",
                         "-jobname=xelatex", "xelatex.ini"], output, env,
                        output / "bootstrap-console.log")
        if rc:
            return rc
    # Paths are passed as one subprocess argument, without shell interpolation.
    tex_command = r"\def\QAInputFile{" + str(source) + r"}\input{" + str(wrapper) + "}"
    rc = run_logged(["xelatex", "-no-shell-escape", "-no-pdf", "-interaction=nonstopmode",
                     "-halt-on-error", "-file-line-error", "-jobname=qa-check",
                     tex_command], output, env, output / "qa-console.log")
    if rc:
        return rc
    # The system's generated pdftex.map is absent. The installed LM map is
    # required for correct lmsy10 encoding; without it xdvipdfmx can abort.
    located = subprocess.run(["kpsewhich", "lm.map"], env=env, text=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    fontmap = located.stdout.strip()
    if located.returncode or not fontmap or not Path(fontmap).is_file():
        print("Required installed Latin Modern font map could not be located.")
        return 1
    return run_logged(["xdvipdfmx", "-f", fontmap, "-o", "qa-check.pdf", "qa-check.xdv"],
                      output, env, output / "pdf-backend.log")


if __name__ == "__main__":
    sys.exit(main())
