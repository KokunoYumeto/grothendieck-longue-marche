from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes');records=[]
for lang in ['fr','en']:
 parts=[build_readers.preamble(lang,1),r'\begin{document}']
 for pkg,scan in [('LM_P057',568),('LM_C3-511-529',519),('LM_C3-530-548',536),('LM_C3-435-453',448)]:
  t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
  a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==scan);t=t[a:b];ds=list(re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S))
  if pkg=='LM_P057':
   d=next(x[0] for x in ds if 'M_{1,1}[4]' in x[0]);old='\\&\nM_{1,1}[2]';newpart='\\&[60pt]\nM_{1,1}[2]';assert d.count(old)==1;new=d.replace(old,newpart);reason='Equation (67): add 60pt only before the third column so the unchanged Galois degree-two label clears both the arrowhead and target object; retain matrix height.';cote='140-2'
  elif scan==519:
   d=next(x[0] for x in ds if 'shorten >=55pt' in x[0]);old=r'"\unsure{1}"{pos=.43}';newpart=r'"\unsure{1}"{pos=.43,yshift=4pt}';assert d.count(old)==1;new=d.replace(old,newpart);reason='Equation (77): raise the existing uncertain1 label by 4pt at its original position so it clears the extra shortened arrowhead; preserve both diagonal arrows and their endpoints.';cote='140-3'
  elif scan==536:
   d=next(x[0] for x in ds if r'\delta_B' in x[0]);old=r'\arrow[r,"{\delta_B}"]\arrow[d,hook]\&';newpart=old+'[15pt]';assert d.count(old)==1;new=d.replace(old,newpart)
   old=r'\arrow[d,"{\unsure{\chi_\gamma}}"'+"']";newpart=old[:-1]+r'{xshift=-4pt}]';assert new.count(old)==1;new=new.replace(old,newpart);reason='Equation (31): add 15pt between the last two nontrivial group columns so both delta-label subscripts clear their horizontal arrowheads, and shift the existing uncertain chi-gamma label 4pt left to clear the downward arrowhead; preserve matrix height and every endpoint.';cote='140-3'
  else:
   d=next(x[0] for x in ds if r'\det_{T_\rho}' in x[0]);new=d
   for label in [r'\delta_\rho=\det_{T_\rho}',r"\delta'_\sigma=\det_{T_\sigma}"]:
    old=r'\arrow[r,"{'+label+r'}"]';newpart=old[:-1]+r'{yshift=3pt}]';assert new.count(old)==1;new=new.replace(old,newpart)
   reason='Equation (134): raise only the two determinant-of-T labels by 3pt so their nested rho/sigma subscripts clear the horizontal arrowhead tips; keep the upper determinant-of-G label, all endpoints and matrix dimensions unchanged.';cote='140-3'
  records.append(dict(id=f'{cote}-{scan}-L1',language=lang,package=pkg,scan=scan,old=d,new=new,reason=reason))
  body=r'\scanpage{'+str(scan)+'}'+r'\diagram{'+new+'}';body,_,_=editorial.annotate(body,pkg,lang);parts += [r'\clearpage\LMcote{'+cote+'}',body]
 parts += [r'\end{document}'];(D/f'final_label_clearances_{lang}.tex').write_text('\n'.join(parts))
Path('work/layout_probes/final_label_clearances.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
