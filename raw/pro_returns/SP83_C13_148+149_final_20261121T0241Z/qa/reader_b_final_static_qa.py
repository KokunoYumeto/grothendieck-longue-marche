"""Read-only final QA of accepted text, records, and generated output consistency.

No manuscript image is opened. No OCR, TeX compilation, external lookup, or
accepted-data mutation occurs. Aggregate regeneration is isolated in a temporary
directory; symlinked accepted records/pages are read only.

Run only when the main reader authorizes the final snapshot:
  python result/qa/reader_b_final_static_qa.py --final
Optional reviewed diagnostic dispositions:
  ... --final --dispositions result/qa/reader_b_final_static_dispositions.json
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import contextlib
import csv
import hashlib
import importlib.util
import io
import json
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'result'
ID = 'SP83_C13_148+149'
csv.field_size_limit(16*1024*1024)


def sha(data): return hashlib.sha256(data).hexdigest()
def ws(s): return re.sub(r'\s+',' ',s).strip()
def tsv(p):
    with p.open(newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
def macro_args(s,names=('unsure',)):
    result=[]
    for m in re.finditer(r'\\('+'|'.join(map(re.escape,names))+r')\s*\{',s):
        start=m.end();pos=start;depth=1
        while pos<len(s) and depth:
            n=0;j=pos-1
            while j>=0 and s[j]=='\\':n+=1;j-=1
            if not n%2:
                if s[pos]=='{':depth+=1
                elif s[pos]=='}':depth-=1
            pos+=1
        if depth==0: result.append({'macro':m[1],'start':m.start(),'end':pos,'arg':s[start:pos-1]})
    return result
def first_alt(s):
    depth=0
    for i,ch in enumerate(s):
        n=0;j=i-1
        while j>=0 and s[j]=='\\':n+=1;j-=1
        if n%2: continue
        if ch=='{':depth+=1
        elif ch=='}':depth-=1
        elif ch=='|' and depth==0:return s[:i]
    return s
def strip_certainty(s):
    for _ in range(30):
        matches=macro_args(s,('unsure','uncertain'))
        if not matches:return s
        outer=[]
        for m in matches:
            if not any(a['start']<=m['start']<a['end'] for a in outer):outer.append(m)
        for m in reversed(outer):s=s[:m['start']]+first_alt(m['arg'])+s[m['end']:]
    return s
def norm(s): return ws(strip_certainty(s))
def macro_norm(s):
    s=strip_certainty(s)
    for old,new in [('struck','deleted'),('add','inserted')]:
        s=re.sub(r'\\'+old+r'(?=\W|$)',r'\\'+new,s)
    for _ in range(20):
        matches=macro_args(s,('text','textrm','mathrm','mbox'))
        if not matches:break
        outer=[]
        for m in matches:
            if not any(a['start']<=m['start']<a['end'] for a in outer):outer.append(m)
        for m in reversed(outer):s=s[:m['start']]+m['arg']+s[m['end']:]
    return ws(s.replace('\\(','').replace('\\)','').replace('$',''))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--final',action='store_true',required=True)
    ap.add_argument('--dispositions')
    args=ap.parse_args()
    order=(OUT/'page_order.txt').read_text().splitlines()
    required=[ID+s for s in ['_transcription.tex','_changes.md','_collation.tsv','_doubts.md',
                            '_inventory.csv','_notes.md','_sheet_feedback.md','_hand_log.md']]
    required+=['decisions.tsv','CHECK_EVENTS.tsv','progress.log']
    inputs=[OUT/'pages'/f'{p}.tex' for p in order]+[OUT/'records'/f'{p}.json' for p in order]
    inputs += [OUT/n for n in required if n!='progress.log']
    inputs += [OUT/n for n in ['notation_final.md','notation_working.md','legibility_note.md',
                              'editorial_metadata_notes.md','sheet_feedback_details.md']]
    before={str(p.relative_to(OUT)):sha(p.read_bytes()) for p in inputs if p.is_file()}
    records={p:json.loads((OUT/'records'/f'{p}.json').read_text()) for p in order}
    texts={p:(OUT/'pages'/f'{p}.tex').read_text() for p in order}
    errors=[];candidates=[];checks=[];large_wrapper_checks=[]
    large_mapping_path=OUT/'qa/reader_b_final_large_wrapper_mappings.json'
    large_mappings=json.loads(large_mapping_path.read_text())['wrappers'] if large_mapping_path.exists() else []
    def error(code,**data):errors.append({'code':code,**data})
    def candidate(kind,**data):
        key=kind+':'+sha(json.dumps(data,sort_keys=True,ensure_ascii=False).encode())[:14]
        candidates.append({'id':key,'kind':kind,**data})
    for name in required:
        if not (OUT/name).is_file():error('missing_deliverable',path=name)
    if {p.stem for p in (OUT/'pages').glob('*.tex')}!=set(order):error('page_set_mismatch')
    if len(order)!=23 or len(set(order))!=23:error('page_order_not_23_unique')
    noteids=[n['id'] for r in records.values() for n in r['notes'] if isinstance(n,dict)]
    changeids=[];decisionids=[];allchanges=[]
    kinds={'misread word','misread symbol or index','omission','text not on the page',
        'deletion state (struck given live or live given struck)','insertion or placement',
        'abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
    event_types={'targeted proof check','independent re-proof','computation or formal certificate',
        'used and rechecked in this run','carried as background without fault found',
        'refuted, with the refined statement id'}
    inv_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
    sheet_kinds={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
    for page,r in records.items():
        if r['page']!=page:error('record_page_mismatch',page=page)
        for key in ['reader','lines_read','changes','decisions','doubts','inventory','notes','check_events','notation','abbreviations','second_boxes']:
            if key not in r:error('missing_record_field',page=page,field=key)
        if not r.get('audit'):error('unfinished_audit',page=page)
        for c in r['changes']:
            changeids.append(c['id']);allchanges.append(c)
            for k in ['id','place','c','h','final','diff_c','diff_h','kind','error_kind','evidence','crop','box','confidence','marked_in_h','consequential']:
                if k not in c:error('missing_change_field',id=c['id'],field=k)
            if c['kind'] not in kinds:error('invalid_collation_kind',id=c['id'],kind=c['kind'])
            if c['confidence'] not in ['high','medium','low']:error('invalid_confidence',id=c['id'])
            for w in ['c','h']:
                if not isinstance(c['diff_'+w],bool):error('nonboolean_difference_flag',id=c['id'],witness=w)
                if c['diff_'+w] and macro_norm(c['final'])==macro_norm(c[w]):
                    candidate('possible_nonmaterial_difference',page=page,change_id=c['id'],witness=w,
                              original=c[w],final=c['final'],evidence=c['evidence'])
        page_uncertainties=macro_args(texts[page],('unsure','illegible'))
        page_args={ws(x['arg']) for x in page_uncertainties}
        doubt_text='\n'.join(str(d.get(k,'')) for d in r['doubts'] for k in ['reading','alternatives','reason','place'])
        for d in r['decisions']:
            decisionids.append(d['id'])
            if d['decision'] not in ['first','alternative','other','undecided']:error('invalid_decision',id=d['id'])
            for m in macro_args(d['reading']):
                if ws(m['arg']) in page_args:continue
                matches=[x['arg'] for x in page_uncertainties if norm(first_alt(x['arg']))==norm(first_alt(m['arg']))]
                if matches:candidate('decision_uncertainty_mismatch',page=page,mark_id=d['id'],
                                     decision_argument=m['arg'],page_same_primary_forms=matches)
        for u in page_uncertainties:
            if len(u['arg'])>2000:
                matches=[m for m in large_mappings if m['page']==page and m['argument_sha256']==sha(u['arg'].encode())]
                if matches:
                    m=matches[0]
                    if r['doubts'][m['record_doubt_index_1_based']-1]['place']!=m['record_doubt_place']:
                        error('large_wrapper_mapping_changed',page=page,mapping=m)
                    else:large_wrapper_checks.append(m)
                else:candidate('large_doubt_wrapper_review',page=page,argument_sha256=sha(u['arg'].encode()),length=len(u['arg']))
                continue
            if ws(u['arg']) not in ws(doubt_text):
                candidate('doubt_mapping_review',page=page,macro=u['macro'],argument=u['arg'],
                    context=texts[page][max(0,u['start']-60):min(len(texts[page]),u['end']+60)])
        for n,d in enumerate(r['doubts'],1):
            if d['confidence'] not in ['high','medium','low']:error('invalid_doubt_confidence',page=page,index=n)
        for e in r['check_events']:
            if e['statement_id'] not in noteids: candidate('check_event_target_review',page=page,event=e)
            if e['type'] not in event_types:error('invalid_check_event_type',page=page,event=e)
        for i in r['inventory']:
            if i['kind'] not in inv_kinds or i['sheet_kind'] not in sheet_kinds or i['transcribed']!='yes':
                error('invalid_inventory_row',page=page,element=i)
        if re.search(r'\\(?:documentclass|usepackage|includegraphics)\b|\\begin\{document\}',texts[page]):
            error('nonfragment_or_raster_command',page=page)
    for name,ids in [('change',changeids),('decision',decisionids),('note',noteids)]:
        dup=[x for x,n in Counter(ids).items() if n>1]
        if dup:error('duplicate_ids',kind=name,ids=dup)
    marks=tsv(ROOT/'source/SP83_C13_148+149_texts/MARKS.tsv')
    exported=tsv(OUT/'decisions.tsv')
    if [x['id'] for x in exported]!=[x['id'] for x in marks]:error('mark_coverage_or_order')
    if set(decisionids)!={x['id'] for x in marks}:error('record_mark_coverage')
    for row in tsv(OUT/'CHECK_EVENTS.tsv'):
        for key in ['statement_id','date','who','type','outcome']:
            if not row.get(key):error('empty_check_event_field',statement=row.get('statement_id'),field=key)

    # Use the production renderer on a temporary tree to check every aggregate,
    # without writing any accepted file or taking a new manuscript decision.
    spec=importlib.util.spec_from_file_location('reader_b_aggregate_renderer',OUT/'scripts/assemble.py')
    renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(renderer)
    aggregate_files=[ID+s for s in ['_transcription.tex','_changes.md','_collation.tsv','_doubts.md',
                        '_inventory.csv','_notes.md','_sheet_feedback.md','_hand_log.md']]
    aggregate_files+=['decisions.tsv','CHECK_EVENTS.tsv','notation_working.md']
    aggregate_checks=[]
    with tempfile.TemporaryDirectory(prefix='reader_b_static_render_',dir=ROOT) as temp:
        temp=Path(temp)
        for name in ['records','pages']:(temp/name).symlink_to(OUT/name,target_is_directory=True)
        for name in ['notation_final.md','legibility_note.md','editorial_metadata_notes.md','sheet_feedback_details.md']:
            if (OUT/name).exists():(temp/name).write_bytes((OUT/name).read_bytes())
        renderer.OUT=temp
        with contextlib.redirect_stdout(io.StringIO()):renderer.assemble()
        for name in aggregate_files:
            expected=(temp/name).read_bytes();actual=(OUT/name).read_bytes()
            same=expected==actual
            aggregate_checks.append({'path':name,'matches_current_records_and_pages':same,
                                     'expected_sha256':sha(expected),'actual_sha256':sha(actual)})
            if not same:error('stale_aggregate',path=name)
    validation=subprocess.run([sys.executable,str(OUT/'scripts/validate.py'),'--final'],capture_output=True,text=True)
    try:validation_result=json.loads(validation.stdout)
    except json.JSONDecodeError:validation_result={'stdout':validation.stdout,'stderr':validation.stderr}
    if validation.returncode:error('production_static_validation_failed',result=validation_result)
    after={str(p.relative_to(OUT)):sha(p.read_bytes()) for p in inputs if p.is_file()}
    changed=[name for name in before if before[name]!=after.get(name)]
    if changed:error('inputs_changed_during_audit',paths=changed)
    dispositions=json.loads(Path(args.dispositions).read_text()) if args.dispositions else {}
    for c in candidates:
        if c['id'] in dispositions:c['review']=dispositions[c['id']]
    unresolved=[c for c in candidates if not c.get('review')]
    counts={'pages':len(order),'finalized_audits':sum(bool(r.get('audit')) for r in records.values()),
            'material_places':sum(bool(c['diff_c'] or c['diff_h']) for c in allchanges),
            'against_C':sum(c['diff_c'] for c in allchanges),'against_H':sum(c['diff_h'] for c in allchanges),
            'marks':len(exported),'inventory_elements':sum(len(r['inventory']) for r in records.values()),
            'doubt_entries':sum(len(r['doubts']) for r in records.values()),
            'in_place_unsure_occurrences':sum(len(macro_args(t)) for t in texts.values()),
            'check_events':len(tsv(OUT/'CHECK_EVENTS.tsv'))}
    report={'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Final read-only static output/metadata audit. No image rereading, OCR, outside research, or TeX compilation.',
        'counts':counts,'errors':errors,'diagnostic_candidates':candidates,'unreviewed_candidates':len(unresolved),
        'aggregate_byte_checks':aggregate_checks,'production_validator':validation_result,
        'large_wrapper_metadata_mappings':large_wrapper_checks,
        'input_hashes':before,'inputs_unchanged_during_audit':not changed,
        'method_audit_owner':'reader_a; separate final method/provenance report',
        'notation_summary_review_owner':'reader_c; separate final notation/documentation review',
        'final_freeze_and_packaging_owner':'main reader; this script does not write progress or freeze hashes'}
    target=OUT/'qa/reader_b_final_static_findings.json'
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    lines=['# Reader B: final static QA','',f"Snapshot: {report['generated_at_utc']}",'',report['scope'],'',
           '## Counts','', '| Measure | Count |','|---|---:|']
    lines += [f'| {k} | {v} |' for k,v in counts.items()]
    lines += ['', '## Output consistency','',f'{len(aggregate_checks)} aggregate files were independently regenerated in a temporary directory and compared byte-for-byte with the deliverables.',
        f"Production static validator: {len(validation_result.get('errors',[]))} errors, {len(validation_result.get('warnings',[]))} warnings.",
        f'Confirmed static errors: {len(errors)}. Diagnostic candidates awaiting manual disposition: {len(unresolved)}.',
        '', '## Confirmed errors','']
    lines += [json.dumps(e,ensure_ascii=False) for e in errors] or ['None.']
    lines += ['', '## Diagnostic review','']
    for c in candidates:
        lines += [f"- **{c['id']}** ({c['page'] if 'page' in c else c['kind']}): "+
                  (c.get('review',{}).get('reason','Pending manual metadata review; this is not an ink-reading judgment.'))]
    lines += ['', '## Limits and preservation','',
        f'{len(large_wrapper_checks)} large figure uncertainty wrappers have separately reviewed links to their existing connectivity/state doubt entries. Literal checks and these dispositions found no confirmed missing mapping; they are metadata checks, not a new proof of visual transcription completeness.',
        'All accepted page/record and aggregate input hashes were checked again after the audit. '+
        ('They were unchanged.' if not changed else 'A concurrent input change was detected; rerun before relying on this snapshot.'),
        'No accepted data were edited. The separate reader_a method/provenance report covers independent-reading chronology, frozen TSV continuity, crop provenance and checkpoint preservation. The reader_c report covers final notation-summary consistency. The main reader owns the final transcription freeze and package.',
        'Earlier QA reports are retained as historical snapshots; their former pending-audit counts are not current totals.', '']
    target.with_suffix('.md').write_text('\n'.join(lines))
    print(json.dumps({'report':str(target),'counts':counts,'errors':errors,
                      'candidate_counts':dict(Counter(c['kind'] for c in candidates)),
                      'unreviewed_candidates':len(unresolved)},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
