from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan019.json').read_text())
def fix(v):
    if isinstance(v,str): return v.replace(r"\inftyl_1",r"\infty l_1")
    if isinstance(v,list): return [fix(x) for x in v]
    if isinstance(v,dict): return {k:fix(x) for k,x in v.items()}
    return v
r=fix(r)
r['reader']='/root/reader_c'
r['main_reader_reviewed']=True
r['crop_count']=14
r['root_review']={'whole_image':True,'crops_viewed':'All fourteen saved crops inspected against C/H. Root adjudicated all five cancelled exponents, three overwritten current indices, dotted rho and i.e without final stop, revised NB, plural produits, literal unfinished placeholders, the four readable post-rho factors, accent on Eliminant, unresolved definition ending and page number. All substantive loci, original marks, inventory and full second-box readings reviewed. One missing TeX command delimiter in infinity followed by l1 was corrected before finalization; no ink was changed by that syntax repair.'}
a=json.loads((E/'scripts/root_additions_019.json').read_text())
r['notes'].extend(a['notes'])
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan019_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan019.tex').write_text(fix((E/'reader_reports/145_scan019.tex').read_text()))
