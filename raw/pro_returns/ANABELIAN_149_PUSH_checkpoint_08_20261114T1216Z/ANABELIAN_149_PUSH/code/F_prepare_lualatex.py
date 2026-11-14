#!/usr/bin/env python3
"""Prepare the local LuaLaTeX runtime used for this return, without root access.

The workspace has TeX binaries and most macro/font files, but lacks generated
formats, font maps, file-name databases, and luaotfload.  This script extracts
the official Debian texlive-luatex data package into a private directory;
it does not install a system package or change any HOME variable.

Examples, from the bundle directory:
    python code/F_prepare_lualatex.py
    python code/F_prepare_lualatex.py --compile ANABELIAN_149_PUSH_paper.tex

The second command runs LuaLaTeX, BibTeX, and two further LuaLaTeX passes.
Logs are saved under build/.  A normal complete TeX Live installation can
instead compile the source by the usual LuaLaTeX/BibTeX sequence.
"""

from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import json
import os
import subprocess
import urllib.request


PACKAGE_NAME = "texlive-luatex_2024.20250309-1_all.deb"
PACKAGE_URL = "https://deb.debian.org/debian/pool/main/t/texlive-base/" + PACKAGE_NAME
PACKAGE_SHA256 = "c6601d6856af0b9cd25c64fcdab4a219a6ce7fd7a37724f532305add28fc72ff"


def run_logged(command, cwd, env, log_path):
    with log_path.open("w", encoding="utf-8") as out:
        subprocess.run(command, cwd=cwd, env=env, stdout=out,
                       stderr=subprocess.STDOUT, check=True)


def environment(runtime):
    env = os.environ.copy()
    trees = [runtime / "localtexmf",
             runtime / "runtime/usr/share/texlive/texmf-dist",
             Path("/usr/share/texlive/texmf-dist"), Path("/usr/share/texmf"),
             Path("/etc/texmf"), Path("/var/lib/texmf")]
    # Without !!, kpathsea searches the available trees even when ls-R is absent.
    env["TEXMF"] = "{" + ",".join(str(p) for p in trees) + "}"
    # A relative path is needed by the installed engine's write-path checks.
    env["TEXMFCACHE"] = "build/texcache"
    return env


def prepare(runtime):
    runtime.mkdir(parents=True, exist_ok=True)
    package = runtime / PACKAGE_NAME
    marker = runtime / "runtime/usr/share/texlive/texmf-dist/tex/luatex/luaotfload/luaotfload-main.lua"
    if not marker.exists():
        if not package.exists():
            temporary = package.with_suffix(".download")
            with urllib.request.urlopen(PACKAGE_URL, timeout=60) as response, temporary.open("wb") as out:
                while chunk := response.read(1024 * 1024):
                    out.write(chunk)
            if sha256(temporary.read_bytes()).hexdigest() != PACKAGE_SHA256:
                raise RuntimeError("Downloaded TeX data package does not match the recorded SHA256")
            temporary.replace(package)
        if sha256(package.read_bytes()).hexdigest() != PACKAGE_SHA256:
            raise RuntimeError("TeX data package does not match the recorded SHA256")
        subprocess.run(["dpkg-deb", "-x", str(package), str(runtime / "runtime")], check=True)

    maps = sorted(Path("/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts").glob("*.map"))
    maps.append(Path("/usr/share/texmf/fonts/map/dvips/lm/lm.map"))
    if len(maps) < 2 or not all(p.exists() for p in maps):
        raise RuntimeError("The base AMS/Latin Modern font maps are missing")
    map_path = runtime / "localtexmf/fonts/map/pdftex/local/pdftex.map"
    map_path.parent.mkdir(parents=True, exist_ok=True)
    map_path.write_text("\n".join(p.read_text() for p in maps), encoding="utf-8")

    env = environment(runtime)
    (runtime / "build/texcache").mkdir(parents=True, exist_ok=True)
    fmt = runtime / "lualatex.fmt"
    if not fmt.exists():
        run_logged(["luahbtex", "--ini", "--interaction=nonstopmode", "--halt-on-error",
                    "--jobname=lualatex", "--progname=lualatex", "lualatex.ini"],
                   runtime, env, runtime / "format-build.log")
    return fmt, env


def main():
    parser = ArgumentParser(description=__doc__)
    default_runtime = Path(__file__).resolve().parents[2] / "tmp/F_build"
    parser.add_argument("--runtime-dir", type=Path, default=default_runtime)
    parser.add_argument("--compile", type=Path, metavar="SOURCE_TEX")
    args = parser.parse_args()
    runtime = args.runtime_dir.resolve()
    fmt, env = prepare(runtime)
    result = {"runtime": str(runtime), "format": str(fmt),
              "package_url": PACKAGE_URL, "package_sha256": PACKAGE_SHA256,
              "TEXMF": env["TEXMF"], "TEXMFCACHE": env["TEXMFCACHE"]}
    if args.compile:
        source = args.compile.resolve()
        cwd = source.parent
        logs = cwd / "build"
        (logs / "texcache").mkdir(parents=True, exist_ok=True)
        latex = ["lualatex", "--fmt=" + str(fmt), "-interaction=nonstopmode",
                 "-halt-on-error", source.name]
        # A bibliography corrected after a failed run must not be blocked by
        # its stale generated .bbl before BibTeX can regenerate that file.
        source.with_suffix(".bbl").unlink(missing_ok=True)
        run_logged(latex, cwd, env, logs / "lualatex-pass1.log")
        run_logged(["bibtex", source.stem], cwd, env, logs / "bibtex.log")
        run_logged(latex, cwd, env, logs / "lualatex-pass2.log")
        run_logged(latex, cwd, env, logs / "lualatex-pass3.log")
        passes = 3
        # Long tables and the table of contents can require one further pass
        # after additions change the pagination. Do not publish stale labels.
        while any(message in (logs / f"lualatex-pass{passes}.log").read_text()
                  for message in ("Label(s) may have changed", "Rerun to get")):
            if passes >= 6:
                raise RuntimeError("Cross-references did not stabilize after six passes")
            passes += 1
            run_logged(latex, cwd, env, logs / f"lualatex-pass{passes}.log")
        (logs / "lualatex-final.log").write_text(
            (logs / f"lualatex-pass{passes}.log").read_text())
        result.update({"pdf": str(source.with_suffix(".pdf")), "logs": str(logs),
                       "engine": "LuaHBTeX/LuaLaTeX", "passes": passes})
    Path(__file__).with_name('F_prepare_lualatex_output.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
