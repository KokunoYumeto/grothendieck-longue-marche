"""Token-by-token comparison of independently written crop transcriptions."""
from pathlib import Path
import csv, difflib, hashlib, json, re, sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]

def read(path):
    with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))

def tokens(s):
    # Retain words, commands, math punctuation, braces, digits and accent marks.
    # Whitespace alone is not a manuscript disagreement.
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]',s)

def compare(n):
    page=f'149_scan{n:03d}'
    paths={kind:ROOT/f'second/{page}_{kind}.tsv' for kind in ('boxes','first','second')}
    hashes={kind:hashlib.sha256(path.read_bytes()).hexdigest() for kind,path in paths.items()}
    provenance=ROOT/f'second/{page}_comparison_provenance.json'
    if provenance.exists():
        assert json.loads(provenance.read_text())['sha256']==hashes, 'An already compared reading changed'
    else:
        provenance.write_text(json.dumps({'scan':n,'comparison_started_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'sha256':hashes},indent=2)+'\n')
    first=read(ROOT/f'second/{page}_first.tsv')
    second=read(ROOT/f'second/{page}_second.tsv')
    expected=[r['box'] for r in first]
    assert [r['box'] for r in second]==expected,'Missing, extra, or reordered second-reading boxes'
    rows=[]; differing=set()
    for a,b in zip(first,second):
        aa=tokens(a['reading']);bb=tokens(b['reading'])
        sm=difflib.SequenceMatcher(None,aa,bb,autojunk=False)
        for tag,i,j,k,l in sm.get_opcodes():
            if tag=='equal':continue
            differing.add(a['box'])
            rows.append({'box':a['box'],'operation':tag,'first_start':i,'first_end':j,'second_start':k,'second_end':l,'first_tokens':' '.join(aa[i:j]),'second_tokens':' '.join(bb[k:l]),'first_reading':a['reading'],'second_reading':b['reading']})
    path=ROOT/f'second/{page}_token_differences.tsv'
    fields=['box','operation','first_start','first_end','second_start','second_end','first_tokens','second_tokens','first_reading','second_reading']
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    print(json.dumps({'scan':n,'boxes':len(first),'different_boxes':len(differing),'token_difference_spans':len(rows),'boxes_to_decide':sorted(differing)},ensure_ascii=False))

if __name__=='__main__':
    for n in map(int,sys.argv[1:]):compare(n)
