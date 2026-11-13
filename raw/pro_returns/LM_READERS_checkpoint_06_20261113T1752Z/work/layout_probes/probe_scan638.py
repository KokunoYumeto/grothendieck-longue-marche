from pathlib import Path
import sys,json,subprocess
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,editorial,fitz
from texenv import environment
D=Path('work/layout_probes'); records=[]
allrows=json.loads((D/'additional_label_candidates.json').read_text())
for lang in ('fr','en'):
 r=next(r for r in allrows if r['language']==lang and r['scan']==638)
 old=r['new']; before='uuuurr,dashed,leftrightarrow,bend right=20'; after='uuuurr,dashed,leftrightarrow,out=0,in=-36,out distance=78pt,in distance=59pt,start anchor=east,end anchor=south east'
 assert old.count(before)==1
 new=old.replace(before,after)
 new=new.replace(after+',\n    '+r'"{\unsure{\leftrightarrow}}"'+"'{description}]",after+',\n    '+r'"{\unsure{\leftrightarrow}}"'+"'{description,pos=.25}]")
 body,entries,meta=editorial.annotate(r'\scanpage{638}\diagram{'+new+'}',r['package'],lang)
 doc=build_readers.preamble(lang,1)+r'\begin{document}\LMcote{140-3}'+body+r'\end{document}'
 target=D/f'scan638_candidate_{lang}.tex';target.write_text(doc)
 p=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=D,env=environment(),capture_output=True,text=True)
 target.with_suffix('.console.txt').write_text(p.stdout)
 log=target.with_suffix('.log').read_text(errors='replace');print(lang,{'exit':p.returncode,'overfull':log.count('Overfull'),'missing':log.count('Missing character')},flush=True)
 if p.returncode:
  print('\n'.join(x for x in log.splitlines() if x.startswith('!') or 'Error' in x));raise SystemExit(p.returncode)
 pdf=fitz.open(target.with_suffix('.pdf'));pdf[0].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(40,45,575,390)).save(D/f'scan638_candidate_{lang}.png')
 records.append(dict(language=lang,package=r['package'],scan=638,old=old,new=new,reason='Route the existing dashed bidirectional map from the blue N object to the top N-star through the right-hand open gaps, avoiding the horizontal degree labels and intermediate objects; preserve every endpoint, arrow type, label, and original row and column size.'))
(D/'scan638_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
