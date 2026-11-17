#!/usr/bin/env python3
"""Independent replay of the seven literal transport identities."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/nonlinear_comb_transport_identities.json'
d=json.loads(p.read_text())
def reduce_word(w):
    answer=[]
    for letter in w:
        if answer and answer[-1]+letter==0:answer.pop()
        else:answer.append(letter)
    return answer
assert len(d['records'])==7
for rec in d['records']:
    assert reduce_word(rec['left_word'])==reduce_word(rec['right_word'])==rec['reduced_word']
    print('PASS independent',rec['name'])
out={'result':'PASS','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'identities':7,'producer_imports':False,
     'scope':'Literal complete free words; general cocycle follows from actual section associativity, not an extra executed test.'}
(Path(__file__).resolve().parent/'nonlinear_transport_independent_review20.json').write_text(json.dumps(out,indent=2)+'\n')
