"""Apply explicit main-reader decisions after visual comparison; never choose readings.

The main reader writes second/scanNNN_adjudication_input.json after inspecting
every differing crop. Sealed first and independent second TSVs are never edited.
"""
from pathlib import Path
import argparse,csv,hashlib,json

root=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--scan',required=True,type=int)
ap.add_argument('--utc',required=True)
args=ap.parse_args();n=args.scan;stem=f'J156-5-04_156-5_scan{n:03}'
inp=root/'second'/f'scan{n:03}_adjudication_input.json'
d=json.loads(inp.read_text())
comparison=json.loads((root/'second'/f'{stem}_comparison.json').read_text())
diffs={x['box']:x for x in comparison if x['different']}
decisions={x['box']:x for x in d['decisions']}
assert len(decisions)==len(d['decisions']),'Duplicate decision'
assert set(decisions)==set(diffs),f'Unadjudicated or extra differences: {set(decisions)^set(diffs)}'
page=root/'pages'/f'{stem}.tex';before=page.read_text();sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
assert sha(before)==d['page_before_sha256'],'Page changed after decision preparation'
recpath=root/'review'/f'scan{n:03}_adjudicated.json';rec=json.loads(recpath.read_text())
assert not rec.get('second_audit_complete'),'Already audited; do not reapply'
after=before
for e in d.get('edits',[]):
 expected=e.get('count',1)
 assert after.count(e['old'])==expected,f'Edit anchor count {after.count(e["old"])} != {expected}: {e["old"]}'
 after=after.replace(e['old'],e['new'],expected)
with (root/'second'/f'{stem}_boxes.tsv').open(newline='') as f:
 boxes={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
audit=[]
for box,dec in decisions.items():
 assert dec.get('viewed_utc') and dec.get('evidence'),'Every differing crop requires an actual visual decision'
 crop=dec['crop'];assert (root/crop).exists(),crop
 co=[int(boxes[box][v]) for v in ('x0','y0','x1','y1')]
 final=dec.get('final',diffs[box]['first'])
 a={**dec,'first':diffs[box]['first'],'second':diffs[box]['second'],'final':final,'source_box':co}
 a['decision']=('Changed. ' if dec.get('changed') else 'First reading retained. ')+dec['evidence']+f' Final: {final}. Crop: `{crop}`; original-image box {co}; inspected {dec["viewed_utc"]}.'
 audit.append(a)
lookup={c['id']:c for c in rec['changes']}
for upd in d.get('record_updates',[]):
 assert upd['id'] in lookup,upd['id'];lookup[upd['id']].update(upd['fields'])
for c in d.get('new_changes',[]):
 assert c['id'] not in lookup,c['id'];rec['changes'].append(c);lookup[c['id']]=c
for key in ('unresolved','notes','hand_habits','inventory','check_events','abbreviations'):
 if key+'_replace' in d:rec[key]=d[key+'_replace']
 if key+'_append' in d:rec.setdefault(key,[]).extend(d[key+'_append'])
rec['audit_changes']=audit
rec['second_audit_complete']=True
rec['second_audit_utc']=args.utc
rec['second_page_hashes']={'before':sha(before),'after':sha(after)}
rec['second_audit_summary']={'boxes':len(comparison),'differences':len(diffs),'changed_loci':len(d.get('changed_loci',[])),'changed_locus_ids':d.get('changed_loci',[])}
page.write_text(after);recpath.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
out={'scan':n,'adjudicator':'main reader, GPT-6 Astra Pro','utc':args.utc,'summary':rec['second_audit_summary'],'page_hashes':rec['second_page_hashes'],'decisions':audit}
(root/'second'/f'{stem}_adjudication.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (root/'progress.log').open('a') as f:
 s=rec['second_audit_summary'];f.write(f'scan {n:03} audited {args.utc}: {s["boxes"]} boxes read, {s["differences"]} differences, {s["changed_loci"]} changed\n')
print(json.dumps(out['summary']))
