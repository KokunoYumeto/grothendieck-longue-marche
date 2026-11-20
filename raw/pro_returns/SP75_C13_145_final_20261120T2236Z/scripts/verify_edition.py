"""Required final completeness checks; no OCR and no TeX compilation."""
from pathlib import Path
import csv,json,re,hashlib

E=Path(__file__).resolve().parents[1];ROOT=E.parent
expected=[3]+list(range(5,28))
def tsv(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
reports=[json.loads((E/'reader_reports'/f'145_scan{n:03d}_reviewed.json').read_text()) for n in expected]
assert sorted(int(p.stem[-3:]) for p in (E/'pages').glob('145_scan*.tex'))==expected
assert all(r.get('main_reader_reviewed') and r.get('audit') for r in reports)
source_marks=tsv(ROOT/'source/SP75_C13_145_texts/MARKS.tsv')
assert [x['id'] for x in tsv(E/'decisions.tsv')]==[x['id'] for x in source_marks]
sealed=tsv(E/'second/FIRST_READINGS_SHA256.tsv')
assert len(sealed)==24
for entry in sealed:
    assert hashlib.sha256((E/'second'/entry['file']).read_bytes()).hexdigest()==entry['sha256']
with (ROOT/'source/SP75_C13_145_C_H_differences.tsv').open() as f:
    raw=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
for r in reports:
    n=r['scan'];stem=f'145_scan{n:03d}'
    assert r['audit']['reader'].split('/')[-1]!=r['reader'].split('/')[-1]
    assert not (r['audit']['reader'].split('/')[-1]=='reader_b' and n in [25,26,27])
    assigned=json.loads((E/'second'/(stem+'_audit_assignment.json')).read_text())
    assert assigned['reader'].split('/')[-1]==r['audit']['reader'].split('/')[-1]
    count=sum(x['page']==stem for x in raw)
    assert [x['row'] for x in r['diff_coverage']]==list(range(1,count+1)),stem
    for c in r['changes']:
        assert isinstance(c['c_changed'],bool) and isinstance(c['h_changed'],bool)
        # Both-false rows are published noncounted observations; their evidence remains required.
        assert (E/c['crop']).is_file() and len(c['box'])==4
    assert all(x['transcribed']=='yes' for x in r['inventory'])
    b=tsv(E/'second'/(stem+'_boxes.tsv'));f=tsv(E/'second'/(stem+'_first.tsv'));s=tsv(E/'second'/(stem+'_second.tsv'))
    ids=[x['box'] for x in b]
    receipt=json.loads((E/'second'/(stem+'_reading_receipt.json')).read_text())
    for suffix in ['first','second']:
        assert hashlib.sha256((E/'second'/(stem+'_'+suffix+'.tsv')).read_bytes()).hexdigest()==receipt[suffix+'_sha256']
    assert hashlib.sha256((E/'second'/(stem+'_boxes.tsv')).read_bytes()).hexdigest()==receipt['boxes_sha256']
    assert [x['box'] for x in f]==ids==[x['box'] for x in s]
    assert len(b)==r['audit']['boxes_read']
    assert all(x['adjudication']!='PENDING' for x in tsv(E/'second'/(stem+'_comparison.tsv')))
    assert all((E/x['crop']).is_file() for x in r['audit']['differences'])
    text=(E/'pages'/(stem+'.tex')).read_text()
    assert f'\\scanpage{{{n}}}' in text
    # TeX grouping braces, ignoring literal escaped braces and comments.
    clean=re.sub(r'(?<!\\)%[^\n]*','',text)
    clean=re.sub(r'\\[{}]','',clean)
    depth=0
    for c in clean:
        if c=='{':depth+=1
        elif c=='}':depth-=1
        assert depth>=0,(stem,'unbalanced group')
    assert depth==0,(stem,'unclosed group')
    assert '\\documentclass' not in text and '\\begin{document}' not in text
combined=(E/'SP75_C13_145_transcription.tex').read_text()
assert [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',combined)]==expected
assert '\\documentclass' not in combined and '\\begin{document}' not in combined
assert combined=='\\cotefile{145}\n\n'+'\n\n'.join((E/'pages'/f'145_scan{n:03d}.tex').read_text().rstrip() for n in expected)+'\n'
collation=tsv(E/'SP75_C13_145_collation.tsv')
assert len(collation)==sum(sum(c['h_changed'] for c in r['changes']) for r in reports)
assert len(tsv(E/'decisions.tsv'))==117
with (E/'SP75_C13_145_inventory.csv').open() as stream:
    inventory=list(csv.DictReader(stream))
assert len(inventory)==sum(len(r['inventory']) for r in reports)
assert all(row['transcribed']=='yes' for row in inventory)
result={'pages':len(reports),'marks':len(source_marks),'raw_difference_rows':len(raw),'substantive_loci':sum(sum(c['c_changed'] or c['h_changed'] for c in r['changes']) for r in reports),'noncounted_observations':sum(sum(not (c['c_changed'] or c['h_changed']) for c in r['changes']) for r in reports),'published_reading_records':sum(len(r['changes']) for r in reports),'against_C':sum(sum(c['c_changed'] for c in r['changes']) for r in reports),'against_H':len(collation),'inventory_elements':len(inventory),'remaining_doubts':sum(len(r['doubts']) for r in reports),'second_boxes':sum(r['audit']['boxes_read'] for r in reports),'second_differing_boxes':sum(len(r['audit']['differences']) for r in reports),'second_changed_boxes':sum(sum(x['changed'] for x in r['audit']['differences']) for r in reports),'verification':'All required coverage, first-reading seal, audit, grouping, reference, source-order, exact combined-fragment and derived-count checks passed; no TeX compilation.'}
(E/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result))
