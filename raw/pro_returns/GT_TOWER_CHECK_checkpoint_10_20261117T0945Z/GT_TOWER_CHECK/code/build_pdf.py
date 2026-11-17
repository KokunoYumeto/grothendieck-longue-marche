#!/usr/bin/env python3
"""Build with LuaLaTeX, repairing the missing local format when necessary."""
from pathlib import Path
import os,subprocess,sys,atexit,hashlib,json,shutil
from datetime import datetime,timezone
from bootstrap_runtimes import tex
tex()
ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT.parent/".texruntime"
RUNTIME.mkdir(exist_ok=True)
(RUNTIME/"cache").mkdir(exist_ok=True)
env=os.environ.copy()
# This environment contains the TeX trees but omits the system ls-R and
# generated format links. Remove the database-only !! prefixes by setting
# the actual search trees, then build a private format.
env["TEXMF"]="{"+str(RUNTIME/"luatex/usr/share/texlive/texmf-dist")+",/usr/share/texlive/texmf-dist,/usr/share/texmf}"
(ROOT/"tex_cache").mkdir(exist_ok=True)
env["TEXMFCACHE"]="tex_cache"
env["TEXFORMATS"]=str(RUNTIME)+"//:"
# The system installation omits the generated outline-font map too.
font_maps=Path("/usr/share/texlive/texmf-dist/fonts/map/dvips")
map_names=["amsfonts/cm.map","amsfonts/cmextra.map","amsfonts/symbols.map","amsfonts/euler.map","amsfonts/latxfont.map","rsfs/rsfs.map"]
(RUNTIME/"pdftex.map").write_text("\n".join((font_maps/x).read_text() for x in map_names))
env["TEXFONTMAPS"]=str(RUNTIME)+"//:"

logs=ROOT/"notes"/"build"
logs.mkdir(parents=True,exist_ok=True)
history=logs/"history"/datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
history.mkdir(parents=True,exist_ok=False)
source_paths=sorted(set([ROOT/"GT_TOWER_CHECK_paper.tex",ROOT/"GT_TOWER_CHECK_references.bib"]+list(ROOT.glob("part_*.tex"))))
source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
(history/"source_hashes.json").write_text(json.dumps(source_hashes,indent=2)+"\n")
def retain_build_logs():
    for p in logs.iterdir():
        if p.is_file():shutil.copy2(p,history/p.name)
    p=ROOT/"GT_TOWER_CHECK_paper.log"
    if p.exists():shutil.copy2(p,history/p.name)
atexit.register(retain_build_logs)
if not (RUNTIME/"lualatex.fmt").exists():
    with (logs/"format_build.stdout").open("w") as f:
        result=subprocess.run(["luahbtex","-ini","-interaction=nonstopmode",
             "-halt-on-error","-jobname=lualatex","lualatex.ini"],
             cwd=RUNTIME,env=env,stdout=f,stderr=subprocess.STDOUT)
    if result.returncode:
        print((logs/"format_build.stdout").read_text()[-5000:])
        sys.exit(result.returncode)
    print("Private LuaLaTeX format built.",flush=True)
passes=int(sys.argv[1]) if len(sys.argv)>1 else 1
if passes>1 and (ROOT/"GT_TOWER_CHECK_paper.aux").exists():
    with (logs/"bibtex_prebuild.stdout").open("w") as f:
        subprocess.run(["bibtex","GT_TOWER_CHECK_paper"],cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
for n in range(passes):
    target=logs/f"lualatex_pass_{n+1}.stdout"
    with target.open("w") as f:
        result=subprocess.run(["lualatex","-interaction=nonstopmode",
             "-halt-on-error","-file-line-error","GT_TOWER_CHECK_paper.tex"],
             cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
    print("LuaLaTeX pass",n+1,"exit",result.returncode,flush=True)
    if result.returncode:
        print(target.read_text()[-6000:])
        sys.exit(result.returncode)
    if n==0 and passes>1:
        with (logs/"bibtex.stdout").open("w") as f:
            result=subprocess.run(["bibtex","GT_TOWER_CHECK_paper"],
                 cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
        print("BibTeX exit",result.returncode,flush=True)
        if result.returncode:
            print((logs/"bibtex.stdout").read_text()[-4000:])
            sys.exit(result.returncode)
manifest={"source_sha256":source_hashes,
          "pdf_sha256":hashlib.sha256((ROOT/"GT_TOWER_CHECK_paper.pdf").read_bytes()).hexdigest(),
          "passes":passes,"log_history":str(history.relative_to(ROOT))}
(logs/"current_build_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
print("Build complete; exact source hashes and every build log retained.")
