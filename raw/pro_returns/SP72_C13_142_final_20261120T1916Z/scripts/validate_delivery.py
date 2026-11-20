"""Mechanical completeness checks only; deliberately does not compile TeX."""
from pathlib import Path
import csv,json,re,hashlib

out=Path(__file__).resolve().parents[1]
root=out.parent
expected=list(range(77,101))
pages=sorted((out/'pages').glob('142_scan*.tex'))
assert [int(re.search(r'scan(\d+)',p.name)[1]) for p in pages]==expected
with (root/'source/SP72_C13_142_texts/MARKS.tsv').open() as f:marks=list(csv.DictReader(f,delimiter='\t'))
with (out/'decisions.tsv').open() as f:decisions=list(csv.DictReader(f,delimiter='\t'))
assert [m['id'] for m in marks]==[d['id'] for d in decisions]
assert len({d['id'] for d in decisions})==175
for d in decisions:
    assert d['decision'] in {'first','alternative','other','undecided'}
    assert d['confidence'] in {'high','medium','low'}
    assert d['reading'] and d['what the ink shows'] and d['crop']
with (out/'SP72_C13_142_inventory.csv').open() as f:inv=list(csv.DictReader(f))
assert {int(r['scan']) for r in inv}==set(expected)
assert all(r['transcribed']=='yes' for r in inv)
assert all(r['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for r in inv)
assert all(r['sheet_kind'] in {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'} for r in inv)
with (out/'SP72_C13_142_collation.tsv').open() as f:coll=list(csv.DictReader(f,delimiter='\t'))
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for c in coll:
    assert c['kind'] in allowed,c
    assert int(c['their_page'])+1==int(c['our_scan'])
    assert c['marked_in_H'] in {'yes','no'}
reports=[json.loads((out/'documentation/decided'/f'scan{n:03}.json').read_text()) for n in expected]
with (out/'documentation/assignments.tsv').open() as f:
    assignments={int(row['scan']):row for row in csv.DictReader(f,delimiter='\t')}
view_ledger=json.loads((out/'documentation/root_view_ledger.json').read_text())
event_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
def uncertainty_commands(text,name):
    """Inspect authored TeX structure only; this is not image recognition."""
    for match in re.finditer(r'\\'+name+r'\{',text):
        index,depth=match.end(),1
        while depth:
            if text[index]=='{' and text[index-1]!='\\':depth+=1
            elif text[index]=='}' and text[index-1]!='\\':depth-=1
            index+=1
        yield text[match.start():index]
for r in reports:
    assert r['main_review_complete'] and r['inventory_review_complete'] and r['audit_complete']
    assert assignments[r['scan']]['first_reader'] != re.search(r'reader_[abc]',r['audit_reader'])[0]
    assert assignments[r['scan']]['audit_reader'] == re.search(r'reader_[abc]',r['audit_reader'])[0]
    first=json.loads((out/'readers'/f"scan{r['scan']:03}"/'report.json').read_text())
    assert first['full_page_seen'] and set(first['halves_seen'])=={'top','bottom'}
    audit=json.loads((out/'audit'/f"scan{r['scan']:03}"/'report.json').read_text())
    assert audit['complete_page_read'] and audit['inventory_checked']
    assert audit['full_page_seen'] and set(audit['halves_seen'])=={'top','bottom'}
    assert audit['first_reader'] == assignments[r['scan']]['first_reader']
    assert re.search(r'reader_[abc]',audit['auditor'])[0] == assignments[r['scan']]['audit_reader']
    assert r['audit_review_complete'] and r.get('audit_adjudication')
    assert {c['id'] for c in audit.get('changes',[])} <= {a.get('id') for a in r['audit_adjudication']}
    assert view_ledger[str(r['scan'])]['whole_page_seen']
    page=(out/'pages'/f"142_scan{r['scan']:03}.tex").read_text()
    quoted_doubts=[d['reading'] for d in r['doubts']]
    assert all(q in page for q in quoted_doubts),('doubt table differs from page',r['scan'])
    for name in ['unsure','illegible']:
        for mark in uncertainty_commands(page,name):
            assert any(mark in q for q in quoted_doubts),('unlisted in-place doubt',r['scan'],mark)
    assert len({c['id'] for c in r['changes']})==len(r['changes']),('duplicate comparison id',r['scan'])
    for entry in r.get('hand_log',[]):
        assert all(entry.get(k) for k in ['habit','pages','scope','witness_errors']),('incomplete hand log',r['scan'],entry)
    for c in r.get('changes',[]):
        assert c.get('scan_shows')
        if c.get('crop') and c['crop']!='page':
            assert (out/c['crop']).is_file(),c['crop']
            assert c['crop'] in view_ledger[str(r['scan'])]['crops_seen'],('unviewed change crop',c['crop'])
    for e in r.get('check_events',[]):
        assert e['type'] in event_types or e['type'].startswith('refuted, with the refined statement'),e
        assert all(e.get(k) for k in ['statement_id','date','who','outcome'])
with (out/'documentation/source_doubt_coverage.tsv').open() as stream:
    source_doubts=list(csv.DictReader(stream,delimiter='\t'))
assert len(source_doubts)==260
assert sum(d['state_in_C']=='live text' for d in source_doubts)==175
assert sum(d['state_in_C']=='inside deleted text' for d in source_doubts)==85
assert len(coll)==sum(c.get('h_changed',False) for r in reports for c in r['changes'])
combined=(out/'SP72_C13_142_transcription.tex').read_text()
assert combined=='\\cotefile{142}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in pages)+'\n'
for p in pages:
    s=p.read_text()
    assert '\\documentclass' not in s and '\\begin{document}' not in s
    level=0
    for m in re.finditer(r'(?<!\\)[{}]',s):
        level+=1 if m[0]=='{' else -1
        assert level>=0,(p,'closing brace')
    assert level==0,(p,'unbalanced braces',level)
    assert s.count('\\[')==s.count('\\]'),p
log=(out/'progress.log').read_text()
for n in expected:
    assert f'scan {n:03} done ' in log and f'scan {n:03} audited ' in log
print(json.dumps({'pages':len(pages),'decisions':len(decisions),'collation_rows':len(coll),'inventory_elements':len(inv),'audit_readers_different':True,'no_TeX_compilation':True,'status':'complete mechanical checks passed'},indent=2))
