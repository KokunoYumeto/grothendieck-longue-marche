"""Attach omitted explicit raw-finding references to already recorded decisions.

The manual mapping below changes metadata only. Exact before/after values make
the edit reversible; hashes prove that all page and combined text bytes remain.
"""
from pathlib import Path
import datetime, hashlib, json
w=Path(__file__).resolve().parents[1]
audit=w/'validation/early_reader_traceability.json'
assert not audit.exists(), 'This one-time audit has already been recorded.'
paths=list((w/'pages').glob('*.tex'))+[w/'SP41_CW_81_transcription.tex']
before_hashes={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
additions={
27:{6:{2:['scan027-R2-007'],3:['scan027-R3-f07']},12:{3:['scan027-R3-f15']},51:{2:['scan027-R2-063']},57:{3:['scan027-R3-f63']}},
29:{2:{3:['scan029-R3-F006']},19:{2:['scan029-R2-F035']},43:{1:['scan029-R1-f043']}},
30:{12:{3:['scan030-R3-F12','scan030-R3-F24','scan030-R3-F26']},14:{1:['scan030-R1-F016']},26:{2:['scan030-R2-F24','scan030-R2-F25']}}
}
edits=[];coverage={}
for n in [27,28,29,30,32,33,34,35]:
    p=w/f'decisions/scan{n:03d}.json';d=json.loads(p.read_text())
    for pos,readers in additions.get(n,{}).items():
        f=d['findings'][pos-1]
        for k,ids in readers.items():
            old=f['reader_source_ids'][f'R{k}']
            new=list(old) if isinstance(old,list) else [old]
            new.extend(q for q in ids if q not in new)
            f['reader_source_ids'][f'R{k}']=new
            edits.append({'scan':n,'finding':f['id'],'reader':f'R{k}','before':old,'after':new})
    per={}
    for k in (1,2,3):
        raw=json.loads((w/f'readers/scan{n:03d}/R{k}/return.json').read_text())['findings']
        refs=[]
        for f in d['findings']:
            v=f['reader_source_ids'].get(f'R{k}',[]); refs.extend(v if isinstance(v,list) else [v])
        rejected={x['reader_id'] for x in d.get('rejected_candidates',[])}
        matched={f['id'] for f in raw if any(f['id'] in r for r in refs)}
        rejected_here={f['id'] for f in raw if f['id'] in rejected}
        expected={f['id'] for f in raw}
        assert matched|rejected_here==expected,(n,k,expected-matched-rejected_here)
        per[f'R{k}']={'raw_findings':len(expected),'mapped_findings':len(matched),'explicitly_rejected_candidates':sorted(rejected_here),'all_accounted_for':True}
    d['reader_finding_coverage']=per;coverage[str(n)]=per
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
after_hashes={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
assert before_hashes==after_hashes
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
result={'UTC':now,'scope':'Metadata references on completed scans27–35; no ink or transcription decision changed','edits':edits,'coverage':coverage,'transcription_sha256_before':before_hashes,'transcription_sha256_after':after_hashes,'all_transcription_bytes_unchanged':True,'inverse':'For each edit, restore exactly its before value at the named scan/finding/reader. The original compound strings remain as entries of the after array.'}
audit.write_text(json.dumps(result,ensure_ascii=False,indent=2))
with (w/'progress.log').open('a') as f:f.write('post-read metadata QA '+now+'; early reader-finding references completed; all page and combined transcription hashes unchanged.\n')
print(json.dumps({'edits':len(edits),'coverage':coverage,'transcription_unchanged':True}))
