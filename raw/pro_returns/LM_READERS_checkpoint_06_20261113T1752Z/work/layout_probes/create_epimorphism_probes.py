from pathlib import Path
import re,sys
sys.path.insert(0,str(Path('work/scripts').resolve()))
import mechanical_repairs,layout_repairs,build_readers
D=Path('work/layout_probes')
for lang in ['fr','en']:
 parts=[build_readers.preamble(lang,1),r'\begin{document}']
 for pkg,scan in [('LM_C3-530-548',542),('LM_C3-549-567',556),('LM_C3-568-586',568)]:
  t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,rs=layout_repairs.repair(t,pkg,lang)
  a,b=next((a,b) for s,a,b in layout_repairs._scan_ranges(t) if s==scan);t=t[a:b]
  ds=list(re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S));selected=[x[0] for x in ds if (r'Z_\sigma\arrow[r]\arrow[d' in x[0] if scan==556 else '[30pt]' in x[0])]
  assert len(selected)==1,(pkg,scan,len(selected));d=selected[0]
  parts += [r'\clearpage\LMcote{140-3}\scanpage{'+str(scan)+'}',r'\diagram{'+d+'}']
 parts += [r'\end{document}'];(D/f'epimorphism_clearance_{lang}.tex').write_text('\n'.join(parts))
 print(lang,'written')
