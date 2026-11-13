from pathlib import Path
import sys,json,subprocess
sys.path.insert(0,str(Path('work/scripts').resolve()))
from texenv import environment
out=Path('work/layout_probes');records=[];jobs=[]
for lang in ('en','fr'):
 src=Path('sources/fr/texts/LM_P017.tex' if lang=='fr' else 'sources/en/packages/LM_P017_en.tex').read_text()
 a=src.index(r'\deleted{\diagram{',src.index(r'\scanpage{165}'));a=src.index(r'\begin{tikzcd}',a);b=src.index(r'\end{tikzcd}',a)+len(r'\end{tikzcd}')
 old=src[a:b];new=old.replace('row sep=3em,column sep=4em','row sep=5em,column sep=8em')
 new=new.replace('from=1-2,to=2-3,phantom','from=2-2,to=2-3,phantom').replace("\"'{pos=0.65,xshift=-1.9em,yshift=-0.5em}", '\"{description,xshift=-1.5em,yshift=2.2em}')
 new=new.replace('description,yshift=-1.3em','description,xshift=-.8em,yshift=-1.3em')
 before=r'\arrow[from=oldr,to=oldl,bend right=20,"\deleted{\unsure{\illegible{1}}}"]'
 after=r'\arrow[from=oldr,to=oldl,bend right=20,"\deleted{\unsure{\illegible{1}}}"{pos=.8,xshift=-1.5em,yshift=-.2em}]'
 assert new.count(before)==1;new=new.replace(before,after)
 pre=(out/f'scan520_forms_{lang}.tex').read_text().split('\\begin{document}')[0]
 body=r'\begin{document}\LMcote{140-2}'+'\n'
 for mode in (0,1):
  body+=f'\\clearpage\\LMform={mode}\\scanpage{{165}}\n'
  original=r'\deleted{\diagram{'+new+'}}'
  if mode==0:body+=original
  else:body+=r'\begin{LMapparatus}\LMentry{140-2-s165-D003}{deletion}{'+original+'}{omitted}{cancelled diagram}{}\\end{LMapparatus}'
  body+='\n'
 target=out/f'scan165_candidate_{lang}.tex';target.write_text(pre+body+r'\end{document}'+'\n')
 records.append({'language':lang,'package':'LM_P017','scan':165,'old':old,'new':new,'reason':'Give the cancelled diamond diagram separate triangular label areas; widen columns and rows, place the two-line pseudo-commutativity label wholly inside its triangle, and move the lower illegibility marker off the central vertical arrow. Preserve all cancellation wrappers, uncertainty fragments, maps and endpoints.'})
 jobs.append((lang,target,subprocess.Popen(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=out,env=environment(),stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)))
for lang,target,job in jobs:
 stdout,_=job.communicate();(out/f'scan165_candidate_{lang}.console.txt').write_text(stdout)
 log=target.with_suffix('.log').read_text(errors='replace');print(lang,{'exit':job.returncode,'overfull':log.count('Overfull'),'missing':log.count('Missing character')},flush=True)
 if job.returncode:
  print('\n'.join(z for z in log.splitlines() if z.startswith('!') or 'Error' in z));raise SystemExit(job.returncode)
 import fitz
 pdf=fitz.open(target.with_suffix('.pdf'))
 for i,page in enumerate(pdf):
  page.get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(45,55,565,440)).save(out/f'scan165_candidate_{lang}_{i}.png')
(out/'scan165_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
