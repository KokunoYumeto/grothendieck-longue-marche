"""Verify exhaustive supplied-ID coverage and root quotation anchors."""
from pathlib import Path
import re,json,collections,hashlib

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'deliverable/work_records'
notes=(ROOT/'deliverable/MPL_108+112+113+114+115_notes.md').read_text()
source=(ROOT/'context/DOSSIER_STATEMENTS_WITH_STATUS.md').read_text()
pat=r'^\|\s*((?:STRATA|PATHS|BISITE|RESIDUE)\s+[A-Z0-9]+\.[A-Z0-9.]+)\s*\|'
expected=re.findall(pat,source,re.M)
found=re.findall(r'^\|\s*((?:STRATA|PATHS|BISITE|RESIDUE)\s+[A-Z0-9]+\.[A-Z0-9.]+)(?:\s+—|\s*\|)',notes,re.M)
counts=collections.Counter(found)
missing=[x for x in expected if counts[x]==0]
duplicates={k:v for k,v in counts.items() if v!=1}
extras=sorted(set(found)-set(expected))
newsource=(ROOT/'context/NEW_RESULTS.md').read_text()
newexpected=[int(n) for n in re.findall(r'^\|\s*(\d+)\s*\|',newsource,re.M)]
newfound=[int(n) for n in re.findall(r'^\|\s*NEW_RESULTS #(\d+)\s+—',notes,re.M)]
newcounts=collections.Counter(newfound)
quote_errors=[]
queries_bad=[]
rootnotes=json.loads((WORK/'research_root.json').read_text())
for r in rootnotes:
    text='\n'.join((ROOT/'deliverable/pages'/f'MPL_108+112+113+114+115_{r["cote"]}_scan{n:03}.tex').read_text() for n in r['scans'])
    if r['quote'] not in text:quote_errors.append(r['id'])
    if r['context_search_exit']>1:queries_bad.append(r['id'])
hua=json.loads((WORK/'research_residue_hua.json').read_text())['hua_coverage_ids']
hua_missing=[x for x in hua if x not in notes]
page115=json.loads((WORK/'research_115_page_notes.json').read_text())
page115_errors=[]
allowed_kinds={'conjecture','unproved claim','unpursued implication','own idea','reading question','self-flagged','withdrawn in the same text'}
for r in page115:
    path=ROOT/r['literal_quote_source']
    raw=path.read_bytes()
    if r['literal_quote'] not in raw.decode('utf-8'):
        page115_errors.append(r['id']+': literal cue missing')
    if hashlib.sha256(raw).hexdigest()!=r['literal_quote_validation']['source_sha256']:
        page115_errors.append(r['id']+': source hash differs')
    if r['kind'] not in allowed_kinds:
        page115_errors.append(r['id']+': invalid kind')
    if len(re.findall(r'^### '+re.escape(r['id'])+r'\b',notes,re.M))!=1:
        page115_errors.append(r['id']+': heading missing or duplicated')
    if r.get('note') and r['note'] not in notes:
        page115_errors.append(r['id']+': analysis missing')
root_kinds_bad=[r['id'] for r in rootnotes if r['kind'] not in allowed_kinds]
report=dict(dossier_expected=len(expected),dossier_by_group=dict(collections.Counter(x.split()[0] for x in expected)),dossier_found=len(found),missing=missing,duplicates=duplicates,extras=extras,new_expected=newexpected,new_found=newfound,new_missing=[x for x in newexpected if newcounts[x]!=1],hua_expected=hua,hua_missing=hua_missing,root_notes=len(rootnotes),root_quote_errors=quote_errors,root_search_errors=queries_bad,scope='Coverage and literal root anchors only; comparison judgments reviewed separately.')
report.update(cote115_notes=len(page115),cote115_errors=page115_errors,root_kind_errors=root_kinds_bad,scope='All supplied result/dossier IDs, all 149 page/comparison-note literal cues, the cited cote 115 source hashes, enum kind labels and inclusion. Mathematical judgments reviewed separately.')
report['ok']=not any([missing,duplicates,extras,report['new_missing'],hua_missing,quote_errors,queries_bad,page115_errors,root_kinds_bad])
(WORK/'research_coverage_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(0 if report['ok'] else 1)
