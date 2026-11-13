from pathlib import Path
import sys,json,subprocess
sys.path.insert(0,str(Path('work/scripts').resolve()))
from texenv import environment
out=Path('work/layout_probes'); records=[]
for lang in ('fr','en'):
 path=Path('sources/fr/texts/LM_P042.tex' if lang=='fr' else 'sources/en/packages/LM_P042_en.tex')
 src=path.read_text(); s=src.index('\\scanpage{417}'); start=src.index('\\begin{tikzcd}',s); end=src.index('\\end{tikzcd}',start)+len('\\end{tikzcd}')
 old=src[start:end];new=old.replace('ampersand replacement=\\&]','ampersand replacement=\\&,row sep=6em]')
 phrase=r'\unsure{\uline{non}|\uline{pas}} \unsure{comm.?}' if lang=='fr' else r'\unsure{\uline{not}|\uline{not}} \unsure{commutative?}'
 stacked=phrase.replace(' \\unsure{',r'\\\unsure{',1)
 new=new.replace(r'\text{'+phrase+'}',r'\text{\shortstack{'+stacked+'}}')
 new=new.replace('description, near start] \\&','description, near start] \\&[65pt]')
 small='comm.' if lang=='fr' else 'commutative'
 new=new.replace(r'\arrow[d, "\text{\unsure{'+small+r'}}"\']',r'\arrow[d, "\text{\unsure{'+small+r'}}"\',pos=.75]') if False else new
 before='\\arrow[d, "\\text{\\unsure{'+small+'}}"\']'
 after='\\arrow[d, "\\text{\\unsure{'+small+'}}"\',pos=.75]'
 assert before in new
 new=new.replace(before,after)
 pre=(out/f'scan520_forms_{lang}.tex').read_text().split('\\begin{document}')[0]
 doc=pre+'\\begin{document}\\LMcote{140-2}\\scanpage{417}\n\\diagram{'+new+'}\n\\end{document}\n'
 target=out/f'scan417_candidate_{lang}.tex';target.write_text(doc)
 records.append({'language':lang,'package':'LM_P042','scan':417,'sourcepath':str(path.relative_to('sources')),'old':old,'new':new,'reason':'Increase row separation and the third column gap; put the unchanged uncertain noncommutativity annotation on two lines in the upper triangle and the unchanged commutativity label lower inside the right triangle.'})
 r=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=out,env=environment(),capture_output=True,text=True)
 (out/f'scan417_candidate_{lang}.console.txt').write_text(r.stdout)
 print(lang,r.returncode,r.stdout[-1200:])
 if r.returncode:raise SystemExit(r.returncode)
 import fitz
 pdf=fitz.open(target.with_suffix('.pdf'));page=pdf[0];blocks=page.get_text('blocks');box=fitz.Rect(55,55,545,230)
 pix=page.get_pixmap(matrix=fitz.Matrix(2,2),clip=box);pix.save(out/f'scan417_candidate_{lang}.png')
(out/'scan417_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
