"""Reproducible LuaLaTeX build; repair the missing local format without admin access."""
from pathlib import Path
import os, subprocess, shutil, sys, hashlib, json

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent / 'work' / 'texformat'
WORK.mkdir(parents=True, exist_ok=True)
env = os.environ.copy()
# The installed TeX trees are complete, but their ls-R symlink is dangling.
# Omitting the database-only (!!) prefix restores ordinary file discovery.
env['TEXMF'] = ('{' + str(WORK / 'texmf') + ',' + str(WORK / 'texmf' / 'texmf-dist')
                + ',/usr/share/texlive/texmf-dist,/usr/share/texmf}')
env['TEXFORMATS'] = str(WORK) + ':'
env['TEXMFVAR'] = str(WORK / 'var')
env['TEXMFCONFIG'] = str(WORK / 'config')
def run(args, cwd, name):
    result = subprocess.run(args, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (ROOT / 'records' / name).write_text(result.stdout)
    print(name, 'exit', result.returncode, flush=True)
    if result.returncode:
        print(result.stdout[-6000:])
        raise SystemExit(result.returncode)

if not (WORK / 'lualatex.fmt').exists():
    run(['luahbtex', '-ini', '-interaction=nonstopmode', '-halt-on-error',
         '-jobname=lualatex', 'lualatex.ini'], WORK, 'latex_format_build.log')
if '--format-only' in sys.argv:
    raise SystemExit(0)
def source_inventory():
    paths = [ROOT / 'FERMAT_SUCCESSOR_paper.tex', ROOT / 'FERMAT_SUCCESSOR_references.bib']
    paths += sorted((ROOT / 'sections').glob('*.tex'))
    paths += sorted((ROOT / 'tables').glob('*.tex'))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in paths}
before = source_inventory()
aux_path = ROOT / 'FERMAT_SUCCESSOR_paper.aux'
if aux_path.exists() and all(token in aux_path.read_text() for token in (r'\bibdata', r'\bibstyle')):
    run(['bibtex', 'FERMAT_SUCCESSOR_paper'], ROOT, 'bibtex_prebuild.log')
for passno in range(3):
    run(['lualatex', '-interaction=nonstopmode', '-halt-on-error',
         'FERMAT_SUCCESSOR_paper.tex'], ROOT, f'latex_pass_{passno + 1}.log')
    if passno == 0:
        run(['bibtex', 'FERMAT_SUCCESSOR_paper'], ROOT, 'bibtex_build.log')
after = source_inventory()
if before != after:
    raise SystemExit('Source changed during the build; rerun before publication QA.')
pdf = ROOT / 'FERMAT_SUCCESSOR_paper.pdf'
(ROOT / 'records' / 'build_inputs.json').write_text(json.dumps({
    'sources': after,
    'sources_sha256': hashlib.sha256(json.dumps(after, sort_keys=True).encode()).hexdigest(),
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'sources_stable_during_build': True
}, indent=2) + '\n')
print('PDF:', ROOT / 'FERMAT_SUCCESSOR_paper.pdf')
