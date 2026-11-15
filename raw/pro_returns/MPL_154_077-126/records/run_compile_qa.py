#!/usr/bin/env python3
"""Build a private XeLaTeX format if needed, then compile the QA harness.

This launcher does not alter manuscript page files, the combined transcription,
the inventory, or progress.log. It writes support files and TeX output only
beneath records/. It must be run by the reviewing parent; no compilation was
performed while preparing it.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "records"
BUILD = RECORDS / "qa-build"
SUPPORT = RECORDS / "qa-texmf"


def prepare_environment() -> dict[str, str]:
    BUILD.mkdir(parents=True, exist_ok=True)
    config = SUPPORT / "tex" / "generic" / "config"
    config.mkdir(parents=True, exist_ok=True)
    (config / "language.dat").write_text(
        "% QA-only format setup; French text remains Unicode.\n"
        "english hyphen.tex\n", encoding="ascii")
    driver_config = SUPPORT / "dvipdfmx"
    driver_config.mkdir(parents=True, exist_ok=True)
    (driver_config / "dvipdfmx.cfg").write_text(
        "% QA-only local config: retain the driver's built-in defaults.\n",
        encoding="ascii")

    env = dict(os.environ)
    # Omitting !! permits recursive on-disk search despite broken system ls-R
    # links. Include our small private tree before the installed package trees.
    env["TEXMF"] = (
        "{" + str(SUPPORT)
        + ",/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}"
    )
    env["TEXMFVAR"] = str(BUILD / "texmf-var")
    env["TEXMFCONFIG"] = str(BUILD / "texmf-config")
    env["TEXMFCACHE"] = str(BUILD / "texmf-cache")
    env["TEXFORMATS"] = str(BUILD) + "//:"
    env["TEXMFOUTPUT"] = str(BUILD)

    # These are installation support data, not manuscript content. Supplying
    # the available basic maps also permits legacy-font fallback in the driver.
    maps = SUPPORT / "fonts" / "map" / "qa"
    maps.mkdir(parents=True, exist_ok=True)
    chunks = ["% Private QA font-map collection.\n"]
    for name in ("cm.map", "cmextra.map", "amsfonts.map", "latxfont.map", "lm.map"):
        found = subprocess.run(
            ["kpsewhich", name], env=env, text=True, capture_output=True, check=False,
        ).stdout.strip()
        if found and Path(found).is_file():
            chunks.append("% Source map: " + name + "\n")
            chunks.append(Path(found).read_text(encoding="utf-8", errors="replace"))
            chunks.append("\n")
    map_text = "".join(chunks)
    for name in ("pdftex.map", "psfonts.map"):
        (maps / name).write_text(map_text, encoding="utf-8")
    return env


def run(command: list[str], env: dict[str, str]) -> int:
    print("Running:", " ".join(command), flush=True)
    return subprocess.run(command, cwd=ROOT, env=env, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first", type=int, default=77)
    parser.add_argument("--last", type=int, default=126)
    parser.add_argument("--rebuild-format", action="store_true")
    parser.add_argument("--keep-going", action="store_true", help="Do not halt at the first TeX error")
    args = parser.parse_args()
    if not (77 <= args.first <= args.last <= 126):
        parser.error("Require 77 <= first <= last <= 126; blank scan 99 is skipped")
    if args.first == args.last == 99:
        parser.error("Scan 99 was omitted as blank")
    for name in ("xetex", "xelatex", "kpsewhich", "xdvipdfmx"):
        if shutil.which(name) is None:
            parser.error(f"Required executable is unavailable: {name}")

    env = prepare_environment()
    fmt = BUILD / "qa-xelatex.fmt"
    if args.rebuild_format or not fmt.is_file():
        status = run([
            "xetex", "-ini", "-etex", "-progname=xelatex",
            "-jobname=qa-xelatex", "-interaction=nonstopmode", "-halt-on-error",
            "-no-shell-escape", "-output-directory=" + str(BUILD), "xelatex.ini",
        ], env)
        if status != 0 or not fmt.is_file():
            print("Private format initialization failed; inspect records/qa-build/qa-xelatex.log", file=sys.stderr)
            return status or 1

    entry = (
        r"\def\QAFirstScan{" + str(args.first)
        + r"}\def\QALastScan{" + str(args.last)
        + r"}\input{records/qa_compile.tex}"
    )
    command = [
        "xelatex", "-fmt=qa-xelatex", "-interaction=nonstopmode", "-file-line-error",
        "-no-shell-escape", "-output-directory=" + str(BUILD),
        f"-jobname=qa-scans-{args.first:03d}-{args.last:03d}",
    ]
    if not args.keep_going:
        command.append("-halt-on-error")
    command.append(entry)
    return run(command, env)


if __name__ == "__main__":
    raise SystemExit(main())
