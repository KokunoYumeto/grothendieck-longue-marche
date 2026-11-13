from pathlib import Path
import sys,re
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes');targets=[]
for lang in ['fr','en']:
 pkg='LM_C3-435-453';t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
 a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==446);t=t[a:b];t,_,_=editorial.annotate(t,pkg,lang)
 d=re.search(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S)[0]
 old=d;d=d.replace('row sep=14pt','row sep=32pt')
 # Both quotient labels remain below their original horizontal arrows.
 d=d.replace('}"\'','}"\'{yshift=-12pt}')
 assert d.count('yshift=-12pt')==2
 body=[]
 for form in ([0,1,2] if lang=='fr' else [1,2]):body += [r'\clearpage\LMform='+str(form),r'\LMcote{140-3}\scanpage{446}',r'\[(133)\qquad\diagram{'+d+r'}\]']
 (D/f'scan446_candidate_{lang}.tex').write_text(build_readers.preamble(lang,1)+r'\begin{document}'+'\n'.join(body)+r'\end{document}')
