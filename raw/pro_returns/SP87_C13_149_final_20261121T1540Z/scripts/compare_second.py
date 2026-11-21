from pathlib import Path
import csv,json,re,difflib,sys,hashlib
from datetime import datetime,timezone
ROOT=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
def tokens(s):
    return re.findall(r'\\[A-Za-z]+|\\.|[\wÀ-ÿ]+|[^\s]',s)
def read(path):return list(csv.DictReader(path.open(),delimiter='\t'))
def compare(page):
    target=ROOT/'second'/f'{page}_comparison.tsv'
    if target.exists():raise ValueError('Comparison already saved; do not replace the frozen evidence record')
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    hashes={x:hashlib.sha256((ROOT/'second'/f'{page}_{x}.tsv').read_bytes()).hexdigest() for x in ['first','second']}
    baseline=json.loads((ROOT/'review/blind_stage_start_hashes.json').read_text())
    if hashes['first']!=baseline[f'second/{page}_first.tsv']:raise ValueError('First reading changed after the blind stage began')
    first=read(ROOT/'second'/f'{page}_first.tsv');sec=read(ROOT/'second'/f'{page}_second.tsv');sm={r['box']:r['reading'] for r in sec}
    if len(sm)!=len(sec) or [r['box'] for r in first]!=[r['box'] for r in sec]:raise ValueError('Mismatched, repeated, or reordered box IDs '+page)
    out=[]
    for r in first:
        a=r['reading'];b=sm[r['box']];ta=tokens(a);tb=tokens(b)
        if ta==tb:continue
        edits=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(a=ta,b=tb,autojunk=False).get_opcodes():
            if tag!='equal':edits.append(f'{tag}: {" ".join(ta[i:j])} => {" ".join(tb[k:l])}')
        out.append({'box':r['box'],'first':a,'second':b,'token_differences':' || '.join(edits)})
    with (ROOT/'second'/f'{page}_comparison.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['box','first','second','token_differences'],delimiter='\t');w.writeheader();w.writerows(out)
    (ROOT/'second'/f'{page}_comparison_hashes.json').write_text(json.dumps({'compared_utc':stamp,**hashes},indent=2)+'\n')
    print(page,'boxes',len(first),'token-different',len(out))
    return out
if __name__=='__main__':
    for p in sys.argv[1:]:compare(p)
