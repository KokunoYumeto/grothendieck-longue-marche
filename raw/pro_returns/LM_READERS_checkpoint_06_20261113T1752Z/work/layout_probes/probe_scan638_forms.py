from pathlib import Path
import json,sys,subprocess
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,fitz
from texenv import environment
D=Path('work/layout_probes');jobs=[]
for r in json.loads((D/'scan638_candidate.json').read_text()):
 lang=r['language'];new=r['new'];body,_,_=editorial.annotate(r'\scanpage{638}\diagram{'+new+'}',r['package'],lang)
 parts=[build_readers.preamble(lang,1),r'\begin{document}\LMcote{140-3}']
 for mode in (0,1,2): parts.append(f'\\clearpage\\LMform={mode}\n'+body)
 parts.append(r'\end{document}')
 target=D/f'scan638_forms_{lang}.tex';target.write_text('\n'.join(parts))
 jobs.append((lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
for lang,target,job in jobs:
 stdout,_=job.communicate();target.with_suffix('.console.txt').write_text(stdout);log=target.with_suffix('.log').read_text(errors='replace')
 print(lang,{'exit':job.returncode,'overfull':log.count('Overfull'),'missing':log.count('Missing character')},flush=True)
 if job.returncode:raise SystemExit(job.returncode)
 for i,page in enumerate(fitz.open(target.with_suffix('.pdf'))):page.get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(40,45,575,390)).save(D/f'scan638_forms_{lang}_{i}.png')
