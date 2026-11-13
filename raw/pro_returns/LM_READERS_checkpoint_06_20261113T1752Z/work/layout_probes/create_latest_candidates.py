from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes');candidates=[]
for lang in ['fr','en']:
 parts=[build_readers.preamble(lang,1),r'\begin{document}']
 for pkg,scan in [('LM_C3-435-453',446),('LM_C3-511-529',525),('LM_C3-606-624',619),('LM_C3-530-548',545)]:
  t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
  a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==scan);t=t[a:b]
  ds=list(re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S))
  if scan==446:
   d=next(x[0] for x in ds if 'quotient' in x[0]);new=d.replace('row sep=32pt','row sep=14pt').replace('{yshift=-12pt}','').replace(r'\& \&',r'\&[18pt] \&',1)
  elif scan==525:
   d=next(x[0] for x in ds if r'"\chi"' in x[0]);needle=r'N_{1,1}^{\sim}\arrow[r,no head]\arrow[d,';i=d.index(needle);e=d.index(r'\&',i)+2;old=d[i:e];newpart=old+'[20pt]';new=d.replace(old,newpart)
   candidates.append(dict(language=lang,package=pkg,scan=scan,old=old,new=newpart,id='140-3-525-L1',reason='Equation (6): add 20pt only between the middle and right columns so the middle epimorphism label and the right-hand chi label occupy separate clear areas, without changing the diagram height.'))
  elif scan==545:
   d=next(x[0] for x in ds if r'\varepsilon_{2,3}:x\longmapsto' in x[0]);old=r'\& \{\pm1\}\times\{\pm1\}';newpart=r'\&[85pt] \{\pm1\}\times\{\pm1\}';assert d.count(old)==1;new=d.replace(old,newpart)
   candidates.append(dict(language=lang,package=pkg,scan=scan,old=old,new=newpart,id='140-3-545-L1',reason='Equation (59): add 85pt between the two columns so the full epsilon-map label fits between the unchanged source and target objects, without changing the diagram height.'))
  else:
   d=next(x[0] for x in ds if '130' in x[0]);label='hom ' if lang=='fr' else 'homomorphism ';old=r'\arrow[r,"\text{'+label+r'}(130)"]'+'\n '+r'\&N^*_{\rho}/\{\pm1\}';newpart=old.replace(r'\&N',r'\&[60pt]N');assert d.count(old)==1;new=d.replace(old,newpart)
  annotated,_,_=editorial.annotate(r'\scanpage{'+str(scan)+'}'+r'\diagram{'+new+'}',pkg,lang)
  parts += [r'\clearpage\LMcote{140-3}',annotated]
 parts += [r'\end{document}'];(D/f'latest_label_candidates_{lang}.tex').write_text('\n'.join(parts))
Path('work/layout_probes/scan525_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2)+'\n')
