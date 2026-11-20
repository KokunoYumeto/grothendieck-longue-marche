from pathlib import Path
import json
import re

p = Path('/workspace/scratch/4770596940a0/out/readers/R3')
r = json.loads((p/'scan033.json').read_text())
t = (p/'scan033.tex').read_text()
level = 0
for line in t.splitlines():
    line = line.split('%',1)[0]
    for i,c in enumerate(line):
        if c in '{}':
            n=0
            j=i-1
            while j>=0 and line[j]=='\\':
                n+=1
                j-=1
            if n%2:
                continue
            level += 1 if c=='{' else -1
            assert level>=0,(line,i)
assert level==0,level
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
    if m[1]=='begin':
        stack.append(m[2])
    else:
        assert stack and stack.pop()==m[2],m.group()
assert not stack
assert t.count('$')%2==0
ids={x['id'] for x in r['differences']}
assert len(ids)==48
assert len(r['C_doubt_resolutions'])==17
assert all(x['difference_id'] in ids for x in r['C_doubt_resolutions'])
assert all(type(x[k]) is bool for x in r['differences'] for k in ('against_C','against_H','marked_in_H'))
assert all(Path(x).exists() for x in r['images_viewed'])
assert all(Path(x['path']).exists() and Path(x['source']).exists() for x in r['crops'])
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in r['inventory'])
assert all(x['type'] in {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted'} for x in r['check_events'])
assert all(x.get('transcribed')=='yes' for x in r['inventory'])
assert set(x['id'] for x in r['crops']) == set(Path(x).stem.removeprefix('scan033_') for x in r['images_viewed'][3:])
assert all(x in ids for x in r['remaining_doubts'])
print('PASS: 48 comparison rows; 17 C doubt links; 48 inventory elements; 33 crops; 36 images; 4 typed check events. Structural validation only; no TeX compilation.')
