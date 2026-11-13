#!/usr/bin/env python3
"""Check document/ledger/archive consistency without claiming to verify proofs."""
from pathlib import Path
from collections import Counter
import csv,gzip,hashlib,json,re,sys,zipfile
from pypdf import PdfReader
from package_files import distribution_files

ROOT=Path(__file__).resolve().parents[1]
PREFIX='LM8_LIE_APPROXIMATIONS'
AUDIT=ROOT/'audit'
errors=[]
def check(condition,message):
    if not condition:errors.append(message)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
with (ROOT/(PREFIX+'_results.csv')).open(newline='') as h:
    reader=csv.DictReader(h);rows=list(reader);headers=reader.fieldnames
expected=['id','statement','status','where_proved','depends_on',
          'manuscript_passages (section; folio; scan)',
          'depends_on_doubtful_reading (scan, alternatives)','notes']
check(headers==expected,'Results CSV headers differ from the requested schema.')
ids=[r['id'] for r in rows]
check(len(ids)==len(set(ids)),'Duplicate statement IDs in the results ledger.')
source_ids=[]
for p in (ROOT/'sections').glob('*.tex'):
    source_ids+=re.findall(r'\\begin\{statement\}\{([^}]+)\}',p.read_text())
check(sorted(ids)==sorted(source_ids),'Paper statement IDs and ledger rows differ.')
counts=Counter(r['status'] for r in rows)
summary=json.loads((AUDIT/'package_summary.json').read_text())
check(summary['statements']==len(rows),'Stale statement total.')
check(summary['status_counts']==dict(counts),'Stale status counts.')
report=(ROOT/(PREFIX+'_report.md')).read_text()
if counts.get('Open'):
    check(report.splitlines()[0]=='INCOMPLETE','An unresolved return is not marked INCOMPLETE.')
typ=json.loads((AUDIT/'typesetting.json').read_text())
for name in ['over_2pt_after','undefined_citations','undefined_references',
             'missing_characters','rerun_required','undefined_warning']:
    check(not typ.get(name),f'Typesetting gate not clear: {name}.')
check(typ.get('sources_unchanged_during_build') is True,'No stable-source build certificate.')
for name,value in typ.get('source_sha256',{}).items():
    check((ROOT/name).exists() and sha(ROOT/name)==value,'Source changed since compilation: '+name)
pdf=ROOT/(PREFIX+'_paper.pdf')
pdf_hash=sha(pdf)
check(typ.get('pdf_sha256')==pdf_hash,'PDF differs from the logged build.')
pages=len(PdfReader(pdf).pages)
qa=json.loads((AUDIT/'visual_qa.json').read_text()) if (AUDIT/'visual_qa.json').exists() else {}
check(qa.get('pdf_sha256')==pdf_hash,'Visual QA belongs to a different PDF.')
check(qa.get('visual_review_status')=='passed','Final rendered-page review is not recorded as passed.')
check(set(qa.get('overflow_source_pages',[]))<=set(qa.get('detail_pages_inspected',[])),
      'A former-overflow page lacks detailed image inspection.')
check(len(qa.get('detail_pages_inspected',[]))>=8,'Too few detailed page inspections recorded.')

documented_partial={
 'code/e_b3_all_quotients.json':
 'Truncated unsuccessful preliminary quotient export; authoritative complete data are in e_b3_quotients_complete.json.'}
partial_seen=[];parsed=0
for p in distribution_files(ROOT):
    if p.suffix!='.json' and not p.name.endswith('.json.gz'):continue
    rel=str(p.relative_to(ROOT))
    try:
        data=gzip.decompress(p.read_bytes()) if p.name.endswith('.gz') else p.read_bytes()
        json.loads(data);parsed+=1
    except Exception as exc:
        if rel in documented_partial:
            partial_seen.append({'path':rel,'status':'retained failed attempt',
                                 'reason':documented_partial[rel],'parse_error':str(exc)})
        else:errors.append('Undocumented invalid JSON: '+rel+'; '+str(exc))
with (AUDIT/'checkpoint_changes.csv').open(newline='') as h:
    changes={(r['checkpoint'],r['file']):r for r in csv.DictReader(h)}
checkpoint_entries=0
for zp in sorted((ROOT.parent/'checkpoints').glob(PREFIX+'_checkpoint_*.zip')):
    with zipfile.ZipFile(zp) as z:
        for name in z.namelist():
            if name.endswith('/'):continue
            rel=name.split('/',1)[-1];checkpoint_entries+=1
            row=changes.get((zp.name,rel))
            check(row is not None,'Checkpoint file absent from change ledger: '+zp.name+':'+rel)
            if row:check('must review' not in row['reason'].lower(),'Unreviewed checkpoint omission: '+rel)
result={'validation':'passed' if not errors else 'failed',
        'scope':'Artifact consistency and publication checks; not an automated proof checker.',
        'statements':len(rows),'status_counts':dict(counts),'pdf_pages':pages,
        'pdf_sha256':pdf_hash,'valid_json_artifacts':parsed,
        'documented_partial_artifacts':partial_seen,'checkpoint_entries_audited':checkpoint_entries,
        'errors':errors}
(AUDIT/'package_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if errors:raise SystemExit(1)
