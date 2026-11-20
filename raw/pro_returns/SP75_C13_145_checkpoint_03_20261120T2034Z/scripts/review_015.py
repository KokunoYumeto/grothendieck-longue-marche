from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan015.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=14
r['root_review']={'whole_image':True,'crops_viewed':'All fourteen saved crops inspected, including the two added punctuation loci; final report and TeX checked. Accepted the sigma shape in the upper underbrace attempt, its local cancellation, inverse marginal exponents, donc, tirer, sigma1, barred m and manuscript14. Accepted first discrets with s, later profini without s, and final discret without s; remaining blackened indices and the optional prime remain doubtful.'}
r['unlisted_decisions']=[]
for uid,mark,decision,reading,cid,confidence in [
 ('U015-01',r'\unsure{stable}','undecided',r'\deleted{\unsure{stable}}','s015-02','low'),
 ('U015-02',r'\unsure{fixé}','first','fixé','s015-03','high'),
 ('U015-03',r'\unsure{\rho|\varphi}','first',r'\rho','s015-03','high'),
 ('U015-04',r'\unsure{l_1l_\infty|l_\infty}','other',r'\inserted{\deleted{l_{\unsure{1}}\sigma_\infty}}','s015-05','medium')]:
 c=next(c for c in r['changes'] if c['id']==cid)
 r['unlisted_decisions'].append(dict(id=uid,source_mark=mark,decision=decision,reading=reading,ink=c['ink'],crop=c['crop'],box=c['box'],confidence=confidence))
a=json.loads((E/'scripts/root_additions_013_015.json').read_text())['15']
r['notes']=[n.replace('No mathematical verification was performed.','The first page reader performed no mathematical verification; separate main-reader checks are recorded below.').replace('No mathematical check was performed.','The first page reader performed no mathematical check; separate main-reader checks are recorded below.') for n in r['notes']]
r['notes'].extend(a['notes'])
r['notes']=[n.replace('No OCR, external research, other page, TeX compilation or mathematical check was used.','The first page reader used no OCR, external research, other page, TeX compilation or mathematical check. The main reader’s separate computations are recorded below.') for n in r['notes']]
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan015_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan015.tex').write_text((E/'reader_reports/145_scan015.tex').read_text())
