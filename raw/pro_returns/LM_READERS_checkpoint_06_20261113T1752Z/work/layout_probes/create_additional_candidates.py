from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes');candidates=[]
for lang in ['fr','en']:
 parts=[build_readers.preamble(lang,1),r'\begin{document}']
 for pkg,scan in [('LM_C3-549-567',562),('LM_C3-568-586',573),('LM_C3-568-586',574),('LM_C3-625-643',638),('LM_C3-625-643',628)]:
  t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
  a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==scan);t=t[a:b]
  ds=list(re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S))
  if scan==562:
   d=next(x[0] for x in ds if 'shift left=.7ex' in x[0]);new=d.replace('shift left=.7ex','shift left=2.5ex').replace('shift right=.7ex','shift right=2.5ex')
  elif scan==573:
   d=next(x[0] for x in ds if r'\mathrm{Aut}(\widehat' in x[0]);old=r'\& \mathrm{Aut}(\widehat';newpart=old.replace(r'\& ',r'\&[110pt] ');assert d.count(old)==1;new=d.replace(old,newpart)
  elif scan==574:
   d=next(x[0] for x in ds if 'bend left=27' in x[0]);old=r'\& \{\pm1\}';newpart=old.replace(r'\& ',r'\&[50pt] ');assert d.count(old)==1;new=d.replace(old,newpart)
  elif scan==628:
   d=next(x[0] for x in ds if 'gerbe' in x[0]);new=d.replace('}\"]\\arrow[dr]','}\"'+"'"+']\\arrow[dr]');assert new!=d
  else:
   d=ds[0][0];new=d.replace(r'L_{\rho}\arrow[uuuuu,hook,dashed]',r'L_{\rho}\arrow[uuuuu,hook,dashed,bend left=20]').replace(r'\mathbb{D}_{\rho}\arrow[uuuuu,hook,dashed]',r'\mathbb{D}_{\rho}\arrow[uuuuu,hook,dashed,bend right=20]').replace(r'1\arrow[uuu,hook]',r'1\arrow[uuu,hook,bend right=50]').replace('uuuurr,dashed,leftrightarrow,bend left=20','uuuurr,dashed,leftrightarrow,bend right=20')
  candidates.append(dict(language=lang,package=pkg,scan=scan,id=f'140-3-{scan}-L1',old=d,new=new))
  annotated,_,_=editorial.annotate(r'\scanpage{'+str(scan)+'}'+r'\diagram{'+new+'}',pkg,lang)
  parts += [r'\clearpage\LMcote{140-3}',annotated]
 parts += [r'\end{document}'];(D/f'additional_label_candidates_{lang}.tex').write_text('\n'.join(parts))
Path('work/layout_probes/additional_label_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
