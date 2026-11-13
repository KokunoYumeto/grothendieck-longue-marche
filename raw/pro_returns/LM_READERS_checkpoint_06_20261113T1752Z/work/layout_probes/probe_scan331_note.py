from pathlib import Path
import sys,subprocess,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import mechanical_repairs,layout_repairs,editorial
from texenv import environment
out=Path('work/layout_probes')
records=[]
for lang in ('fr','en'):
 src=Path('sources/fr/texts/LM_P034.tex' if lang=='fr' else 'sources/en/packages/LM_P034_en.tex').read_text()
 src,_=mechanical_repairs.repair(src,'LM_P034',lang);src,_=layout_repairs.repair(src,'LM_P034',lang)
 before=r'\text{\parbox[t]{105pt}{\footnotesize\rule{28pt}{.3pt}\\\textit{\LMnotelabel.}\enspace '
 after=r'\text{\parbox[t]{105pt}{\footnotesize\noindent '
 assert src.count(before)==1
 src=src.replace(before,after)
 records.append({'language':lang,'package':'LM_P034','scan':331,'before_wrapper':before,'after_wrapper':after,'reason':'Remove the redundant manually supplied marginal-note rule and heading; the unchanged margin call supplies one runtime note heading, rule and reference inside the same prose cell.'})
 a=src.index(r'\diagram{'); b=editorial.brace_end(src,a+len(r'\diagram'))+1
 diagram=src[a:b]
 diagram,entries,meta=editorial.annotate(diagram,'LM_P034',lang)
 pre=(out/f'scan520_forms_{lang}.tex').read_text().split('\\begin{document}')[0]
 body='\\begin{document}\\LMcote{140-2}\n'
 for mode in (0,1,2):body+=f'\\clearpage\\LMform={mode}\\scanpage{{331}}\n'+diagram+'\n'
 target=out/f'scan331_note_candidate_{lang}.tex';target.write_text(pre+body+'\\end{document}\n')
 r=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=out,env=environment(),capture_output=True,text=True)
 (out/f'scan331_note_candidate_{lang}.console.txt').write_text(r.stdout)
 print(lang,'returncode',r.returncode,'overfull',r.stdout.count('Overfull'),'missing',r.stdout.count('Missing character:'))
 if r.returncode:raise SystemExit(r.returncode)
 import fitz
 pdf=fitz.open(target.with_suffix('.pdf'))
 for i,page in enumerate(pdf):page.get_pixmap(matrix=fitz.Matrix(1.7,1.7),clip=fitz.Rect(55,55,570,310)).save(out/f'scan331_note_candidate_{lang}_{i}.png')
(out/'scan331_note_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
