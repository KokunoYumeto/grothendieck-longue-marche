"""Structural validation of the documentary deliverables; never compiles TeX."""
from pathlib import Path
import csv,hashlib,json,re,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
def rows(path,delimiter='\t'):
    with path.open() as f:return list(csv.DictReader(f,delimiter=delimiter))

def main(final=False):
    reports=[json.loads(p.read_text()) for p in sorted((ROOT/'reviews').glob('149_scan*.json'))]
    reports=[r for r in reports if r.get('root_approved')]
    ns=[r['scan'] for r in reports]
    if final:assert ns==list(range(5,28)),ns
    expected=[r['id'] for r in rows(BASE/'source/SP84_C13_149_texts/MARKS.tsv') if int(r['scan']) in ns]
    dec=rows(ROOT/'decisions.tsv')
    assert [d['id'] for d in dec]==expected,'Mark coverage/order differs'
    for d in dec:
        assert d['decision'] in ('first','alternative','other','undecided')
        if d['decision']!='undecided':assert d['crop']!='page'
    for r in reports:
        n=r['scan'];p=ROOT/f'pages/149_scan{n:03d}.tex';s=p.read_text()
        assert f'\\scanpage{{{n}}}' in s
        # Check brace balance while excluding escaped brace symbols and comments.
        clean='\n'.join(re.split(r'(?<!\\)%',line)[0] for line in s.splitlines())
        depth=0
        for token in re.findall(r'\\[{}]|[{}]',clean):
            if token=='{':depth+=1
            elif token=='}':depth-=1
            assert depth>=0,(p,'unbalanced closing brace')
        assert depth==0,(p,'unbalanced braces')
        begins=re.findall(r'\\begin\{([^}]+)\}',s);ends=re.findall(r'\\end\{([^}]+)\}',s)
        assert sorted(begins)==sorted(ends),(p,'environment mismatch')
        for c in r.get('changes',[]):
            assert (ROOT/c['crop']).is_file()
            assert len(c['box'])==4 and c['box'][0]<c['box'][2] and c['box'][1]<c['box'][3]
        inventory=r.get('inventory',[])
        assert inventory and all(x['transcribed']=='yes' for x in inventory)
        assert all(x['sheet_kind'] in ('text','reused_typed','typescript','letter','list','cancelled_draft','cover') for x in inventory),(n,'invalid sheet kind')
        assert all(x['kind'] in ('text','display','diagram','drawing','margin note','insertion','deletion') for x in inventory),(n,'invalid element kind')
        packet=BASE/f'work/packets/149_scan{n:03d}/differences.tsv'
        if packet.exists():
            assert [x['row'] for x in r['diff_coverage']]==list(range(1,len(rows(packet))+1)),(n,'difference row coverage')
        boxes=rows(ROOT/f'second/149_scan{n:03d}_boxes.tsv')
        first=rows(ROOT/f'second/149_scan{n:03d}_first.tsv')
        assert [x['box'] for x in boxes]==[x['box'] for x in first]
        assert len(set(x['box'] for x in boxes))==len(boxes)
        if final:
            second=rows(ROOT/f'second/149_scan{n:03d}_second.tsv')
            assert [x['box'] for x in second]==[x['box'] for x in first]
            diffs=rows(ROOT/f'second/149_scan{n:03d}_token_differences.tsv')
            adj=rows(ROOT/f'second/149_scan{n:03d}_adjudications.tsv')
            assert {x['box'] for x in diffs}<={x['box'] for x in adj},(n,'unaudited discrepancy')
            assert r.get('audited') and r.get('second_reader')!=r['reader'],(n,'blind reader provenance')
    combined='\\cotefile{149}\n\n'+'\n'.join((ROOT/f'pages/149_scan{n:03d}.tex').read_text().rstrip()+'\n' for n in ns)
    assert combined==(ROOT/'SP84_C13_149_transcription.tex').read_text(),'combined file differs'
    h={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'pages').glob('*.tex'))+[ROOT/'SP84_C13_149_transcription.tex']}
    print(json.dumps({'pages':len(ns),'marks':len(dec),'status':'passed','sha256':h},indent=2))
    return h

if __name__=='__main__':main('--final' in sys.argv)
