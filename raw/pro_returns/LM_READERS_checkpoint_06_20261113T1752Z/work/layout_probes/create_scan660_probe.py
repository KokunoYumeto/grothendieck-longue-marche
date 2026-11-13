from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path('work/scripts').resolve()))
import build_readers,mechanical_repairs,layout_repairs,editorial
D=Path('work/layout_probes');rs=[]
for lang in ['fr','en']:
 pkg='LM_C3-644-662';t=build_readers.raw_package(pkg,lang);t,_=mechanical_repairs.repair(t,pkg,lang);t,_=layout_repairs.repair(t,pkg,lang)
 a,b=next((a,b) for n,a,b in layout_repairs._scan_ranges(t) if n==660);t=t[a:b]
 d=next(x[0] for x in re.finditer(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',t,re.S) if '(31)' in x[0]);old=r'\arrow[dr,hook]\&\\';new=old+'[12pt]';assert d.count(old)==1
 rs.append(dict(language=lang,package=pkg,scan=660,id='140-3-660-L1',old=old,new=new,reason='Equation (31): add 12pt only after the second matrix row to separate the heads of the two diagonal maps that target the live sharp object and the cancelled object in the following row; retain both endpoints and all cancelled-content markers.'))
 d=d.replace(old,new);body=r'\scanpage{660}\diagram{'+d+'}';body,_,_=editorial.annotate(body,pkg,lang)
 parts=[build_readers.preamble(lang,1),r'\begin{document}']
 for form in ([0,1,2] if lang=='fr' else [1,2]):parts += [r'\clearpage\LMform='+str(form),r'\LMcote{140-3}',body]
 parts += [r'\end{document}'];(D/f'scan660_candidate_{lang}.tex').write_text('\n'.join(parts))
Path('work/layout_probes/scan660_candidate.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n')
