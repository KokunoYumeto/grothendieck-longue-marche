from pathlib import Path
import sys,json,subprocess
sys.path.insert(0,str(Path('work/scripts').resolve()))
from texenv import environment
out=Path('work/layout_probes'); records=[]
for lang in ('fr','en'):
 rec=next(r for r in json.loads(Path('work/data/layout_repairs_applied.json').read_text()) if r.get('id')=='140-3-557-T1' and r['language']==lang)
 old=rec['new'];new=old
 replacements=[
  (r'\arrow[dddrr,dashed,"\delta_Z"]',r'\arrow[dddrr,dashed,"\delta_Z"{pos=.17,xshift=2pt}]'),
  (r'\arrow[ddr,dashed,"\delta_\rho"]',r'\arrow[ddr,dashed,"\delta_\rho"{pos=.34,xshift=3pt}]'),
  (r'\arrow[dr,dashed,"\delta_\sigma"]',r'''\arrow[dr,dashed,"\delta_\sigma"{pos=.55,xshift=5pt}]'''),
  (r'\arrow[uur,"{(\chi_\gamma,\varepsilon_{\gamma,\rho},\varepsilon_{\gamma,\sigma})}"]',r'''\arrow[uur,"{(\chi_\gamma,\varepsilon_{\gamma,\rho},\varepsilon_{\gamma,\sigma})}"'{pos=.6,xshift=8pt}]'''),
 ]
 for before,after in replacements:
  assert new.count(before)==1,(lang,before)
  new=new.replace(before,after)
 pre=(out/f'scan520_forms_{lang}.tex').read_text().split('\\begin{document}')[0]
 probe_new=new.replace('&',r'\&').replace(r'\begin{tikzcd}[',r'\begin{tikzcd}[ampersand replacement=\&,',1)
 doc=pre+'\\begin{document}\\LMcote{140-3}\\scanpage{557}\n\\[\\tag{45}\\diagram{'+probe_new+'}\\]\n\\end{document}\n'
 target=out/f'scan557_candidate_{lang}.tex';target.write_text(doc)
 records.append({'language':lang,'package':'LM_C3-549-567','scan':557,'old':old,'new':new,'reason':'Separate labels of the three dashed convergent maps by placing them at distinct positions and sides, and put the unchanged character-tuple map label on the outer side of its arrow. Preserve diagram dimensions, type size, endpoints and all arrow styles.'})
 r=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-halt-on-error',target.name],cwd=out,env=environment(),capture_output=True,text=True)
 (out/f'scan557_candidate_{lang}.console.txt').write_text(r.stdout)
 log=target.with_suffix('.log').read_text(errors='replace');print(lang,{'exit':r.returncode,'overfull':log.count('Overfull'),'missing':log.count('Missing character')})
 if r.returncode:
  print('\n'.join(z for z in log.splitlines() if z.startswith('!') or 'Error' in z));raise SystemExit(r.returncode)
 import fitz
 pdf=fitz.open(target.with_suffix('.pdf'));page=pdf[0];box=fitz.Rect(45,55,575,310)
 page.get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=box).save(out/f'scan557_candidate_{lang}.png')
(out/'scan557_candidate.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
