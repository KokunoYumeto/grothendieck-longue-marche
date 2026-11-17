#!/usr/bin/env python3
"""Compile a snapshot to temporary XDV; never modify transcription files.

Run from any directory. All engine products go to --work-dir or a newly created
temporary directory, never into the deliverable. This is syntax checking only.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument("--work-dir",type=Path)
    args=parser.parse_args()
    root=args.root.resolve()
    work=(args.work_dir or Path(tempfile.mkdtemp(prefix="mpl64_texcheck_"))).resolve()
    work.mkdir(parents=True,exist_ok=True)
    source=root/"MPL_64_002-039_transcription.tex"
    source_bytes=source.read_bytes()
    snapshot=work/"transcription_snapshot.tex"
    snapshot.write_bytes(source_bytes)
    template=(Path(__file__).parent/"tex_harness_template.tex").read_text()
    (work/"harness.tex").write_text(template.replace("@@TRANSCRIPTION@@",str(snapshot)))
    env=os.environ.copy()
    env.update({
        "max_print_line":"1000",
        "TEXINPUTS":".:/usr/share/texlive/texmf-dist/tex/latex//:"
                    "/usr/share/texlive/texmf-dist/tex/generic//:"
                    "/usr/share/texlive/texmf-dist/tex/xelatex//:"
                    "/usr/share/texlive/texmf-dist/tex/plain//:/usr/share/texmf/tex//:",
        "TEXFORMATS":str(work)+"//:",
        "TFMFONTS":"/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:",
        "ENCFONTS":"/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:",
        "TEXFONTMAPS":"/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:",
        "T1FONTS":"/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:",
        "OPENTYPEFONTS":"/usr/share/texlive/texmf-dist/fonts/opentype//:/usr/share/texmf/fonts/opentype//:",
        "TTFONTS":"/usr/share/texlive/texmf-dist/fonts/truetype//:/usr/share/texmf/fonts/truetype//:",
        "TEXMFVAR":str(work/"texmf-var"),"TEXMFCACHE":str(work/"texmf-cache"),
        "VARTEXFONTS":str(work/"fonts"),
    })
    if not (work/"xelatex.fmt").is_file():
        with (work/"format-console.txt").open("w") as output:
            format_result=subprocess.run(
                ["xelatex","-ini","-etex","-jobname=xelatex","-interaction=nonstopmode",
                 "-halt-on-error","xelatex.ini"],cwd=work,env=env,
                stdout=output,stderr=subprocess.STDOUT)
        if format_result.returncode:
            print(json.dumps({"status":"format_failed","work_dir":str(work),
                              "exit_code":format_result.returncode}))
            return format_result.returncode
    console=work/"harness-console.txt"
    with console.open("w") as output:
        result=subprocess.run(
            ["xelatex","-fmt="+str(work/"xelatex.fmt"),"-interaction=nonstopmode",
             "-file-line-error","-no-shell-escape","-no-pdf","harness.tex"],
            cwd=work,env=env,stdout=output,stderr=subprocess.STDOUT)
    log=console.read_text(errors="replace")
    errors=list(dict.fromkeys(re.findall(r"[^\n]*\.tex:\d+:\s*[^\n]+",log)))
    report={
        "scope":"Syntax compilation only; no visual or mathematical validation.",
        "exit_code":result.returncode,"scans_reached":re.findall(r"MPL-SCAN:(\d+)",log),
        "errors":errors,"snapshot_sha256":hashlib.sha256(source_bytes).hexdigest(),
        "source_unchanged_during_check":source.read_bytes()==source_bytes,
        "work_dir":str(work),"output_format":"XDV",
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return result.returncode

if __name__=="__main__":
    raise SystemExit(main())
