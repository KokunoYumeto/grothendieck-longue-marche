"""Structural validation of the manually transcribed TeX; no scan reading."""
from pathlib import Path
import re,json,csv
ROOT=Path(__file__).resolve().parent
EXPECT=[x for x in range(77,116) if x not in (79,89)]
def unescaped(text,pos):
    n=0; i=pos-1
    while i>=0 and text[i]=='\\':n+=1;i-=1
    return n%2==0
def check():
    fs=sorted((ROOT/'pages').glob('*.tex'))
    assert [int(re.search(r'scan(\d+)',f.name)[1]) for f in fs]==EXPECT
    assert [json.loads(x)['scan'] for x in (ROOT/'audit_records.jsonl').read_text().splitlines()]==EXPECT
    for f,s in zip(fs,EXPECT):
        t=f.read_text()
        assert re.findall(r'\\scanpage\{(\d+)\}',t)==[str(s)]
        stack=[]
        for kind,env in re.findall(r'\\(begin|end)\{([^}]+)\}',t):
            if kind=='begin':stack.append(env)
            else: assert stack and stack.pop()==env,(s,kind,env)
        assert not stack,(s,stack)
        depth=0
        for line in t.splitlines():
            for i,c in enumerate(line):
                if not unescaped(line,i): continue
                if c=='%':break
                if c=='{':depth+=1
                elif c=='}':depth-=1
                assert depth>=0,(s,'negative brace depth')
        assert depth==0,(s,'brace balance')
        assert sum(c=='$' and unescaped(t,i) for i,c in enumerate(t))%2==0,(s,'dollar parity')
        tokens=re.findall(r'\\(?:[A-Za-z]+|.)',t)
        assert tokens.count(r'\[')==tokens.count(r'\]'),(s,'display delimiters')
        assert r'\includegraphics' not in t
        assert r'\mspage' not in t
    rows=list(csv.DictReader((ROOT/'MPL_129_077-115_inventory.csv').open()))
    assert list(rows[0])==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
    assert all(x['transcribed']=='yes' for x in rows)
    assert sorted(set(int(x['scan']) for x in rows))==EXPECT
    assert len({x['element'] for x in rows})==len(rows)
    combined='\n'.join(f.read_text().rstrip() for f in fs)+'\n'
    assert combined.startswith('\\cotefile{129}\n\\scanpage{77}')
    target=ROOT/'MPL_129_077-115_transcription.tex'
    if (ROOT/'frozen_hashes.json').exists(): assert target.read_text()==combined
    else: target.write_text(combined)
    print(f'PASS: {len(fs)} pages, {len(rows)} inventory elements, 37 audit records; {len(combined)} characters combined.')
    return len(rows)
if __name__=='__main__':check()
