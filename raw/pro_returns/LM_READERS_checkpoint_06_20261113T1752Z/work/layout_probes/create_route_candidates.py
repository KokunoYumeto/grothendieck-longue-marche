from pathlib import Path
import sys,re
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes')
for lang in ['fr','en']:
 for pkg,scan in [('LM_C3-549-567',561),('LM_C3-625-643',637)]:
  t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
  a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==scan);t=t[a:b]
  if scan==561:
   t=t.replace(r'\mathrm{II}',r'|[yshift=-3pt]| \mathrm{II}',1)
   d=re.search(r'\\begin\{landscape\}.*?\\end\{landscape\}',t,re.S)[0]
  else:
   d=re.search(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S)[0];d=d.replace('start anchor=north west,end anchor=south west','start anchor=north west,end anchor=south west,bend left=25')
   d=r'\diagram{'+d+'}'
  t=r'\scanpage{'+str(scan)+'}'+d;t,_,_=editorial.annotate(t,pkg,lang)
  parts=[]
  for form in ([0,1,2] if lang=='fr' else [1,2]):parts+=[r'\clearpage\LMform='+str(form),r'\LMcote{140-3}',t]
  (D/f'scan{scan}_route_{lang}.tex').write_text(build_readers.preamble(lang,1)+r'\begin{document}'+'\n'.join(parts)+r'\end{document}')
