"""Compare independently recorded box readings; never adjudicate handwriting.

Whitespace is ignored, but words, every TeX command, punctuation and braces
are retained as tokens. Differences of notation or formatting therefore still
appear and must be classified by the human-facing editorial record.
"""
from pathlib import Path
import argparse, csv, difflib, json, re

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'\\[A-Za-z@]+|\\[^\s]|[^\W\d_]+|\d+|[^\s]', re.UNICODE)

def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        rows=list(csv.DictReader(f, delimiter='\t'))
    ids=[r['box'] for r in rows]
    if len(set(ids)) != len(ids): raise ValueError(f'Duplicate box ID: {path}')
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('scan',type=int);a=ap.parse_args()
    stem=f'150_scan{a.scan:03}'
    boxes=read(ROOT/'second'/f'{stem}_boxes.tsv')
    first={r['box']:r['reading'] for r in read(ROOT/'second'/f'{stem}_first.tsv')}
    second={r['box']:r['reading'] for r in read(ROOT/'second'/f'{stem}_second.tsv')}
    expected={r['box'] for r in boxes}
    if set(first)!=expected or set(second)!=expected:
        raise ValueError({'expected':sorted(expected),'first':sorted(first),'second':sorted(second)})
    rows=[]
    for b in boxes:
        key=b['box']; f=first[key];s=second[key];ft=TOKEN.findall(f);st=TOKEN.findall(s)
        edits=[]
        for op,i0,i1,j0,j1 in difflib.SequenceMatcher(None,ft,st,autojunk=False).get_opcodes():
            if op!='equal':edits.append({'op':op,'first_tokens':ft[i0:i1],'second_tokens':st[j0:j1]})
        rows.append({'box':key,'different':'yes' if edits else 'no','first':f,'second':s,
                     'token_changes':json.dumps(edits,ensure_ascii=False),
                     'adjudicated_reading':'','decision':'','evidence':'','crop':''})
    out=ROOT/'second'/f'{stem}_comparison.tsv'
    if out.exists():raise FileExistsError(f'Will not overwrite adjudications: {out}')
    with out.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]) if rows else ['box','different','first','second','token_changes','adjudicated_reading','decision','evidence','crop'],delimiter='\t')
        w.writeheader();w.writerows(rows)
    print(json.dumps({'scan':a.scan,'boxes':len(rows),'differences':sum(r['different']=='yes' for r in rows),'output':str(out)}))

if __name__=='__main__':main()
