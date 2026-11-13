from pathlib import Path
import sys,re
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes')
for lang in ['fr','en']:
 pkg='LM_C1-001-019';t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
 a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==10);t=t[a:b]
 d=next(x[0] for x in re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S) if 'pr}_1' in x[0]);body=r'\scanpage{10}\diagram{'+d+'}';body,_,_=editorial.annotate(body,pkg,lang)
 parts=[build_readers.preamble(lang,1),r'\begin{document}']
 for form in ([0,1,2] if lang=='fr' else [1,2]):parts += [r'\clearpage\LMform='+str(form),r'\LMcote{140-1}',body]
 parts += [r'\end{document}'];(D/f'scan10_projection_{lang}.tex').write_text('\n'.join(parts))
