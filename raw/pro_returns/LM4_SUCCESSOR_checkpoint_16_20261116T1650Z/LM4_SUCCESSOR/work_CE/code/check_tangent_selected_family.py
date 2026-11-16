"""Literal cover-character and peripheral-family audit for the ordered fiber.

The analytic whisker calibration is proved in research_tangent_selected_family.txt.
This checks its exact word-parity transfer and the actual source braid character.
"""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
raw=json.loads((P/'tangent_bundle_fiber_data.json').read_text())
mark=json.loads((P/'tangent_infinity_action.json').read_text())
nodes=json.loads((P/'tangent_node_strips.json').read_text())
words=json.loads((P/'tangent_bundle_words.json').read_text())
def red(w):
    o=[]
    for x in w:
        if o and o[-1]==-x:o.pop()
        else:o.append(x)
    return tuple(o)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(x for j in w for x in (A[j] if j>0 else inv(A[-j])))
def chi(w):return sum(abs(x) in (3,5) for x in w)%2
def peripheral(w):
    w=tuple(w);i=0
    while len(w)-2*i>1:
        assert w[i]==-w[-i-1]
        i+=1
    assert len(w)-2*i==1
    return abs(w[i]),w[:i]
# 0=constant v=u, 1=moving v=q/u, at the specified larger-root base lift.
standard={};seed_rows=[]
for k,w in raw['new_fiber_words'].items():
    j,g=peripheral(inv(w))
    standard[j]=1^chi(g)
    seed_rows.append({'source_index':int(k),'core':j,'conjugator':g,
                      'conjugator_character':chi(g),'standard_family':standard[j]})
assert standard=={4:1,1:0,2:0,6:0}
newold={int(i):tuple(w) for i,w in mark['basis_new2_in_original'].items()}
V={int(i):tuple(w) for i,w in nodes['V_basis_in_new2'].items()}
V_rows=[]
for j in (1,2,4,6):
    w=sub(V[j],newold);core,g=peripheral(w)
    family=standard[core]^chi(g)
    assert family==1
    V_rows.append({'V_index':j,'original_word':w,'core':core,
                   'conjugator_character':chi(g),'family':'moving'})
braid_rows=[]
for row in words['loops']:
    labels=list(words['initial_order']);cross=0
    for b in row['word']:
        k=abs(b)-1;a,c=labels[k:k+2]
        if (a==5 and c in (6,7)) or (c==5 and a in (6,7)):
            cross+=1 if b>0 else -1
        labels[k],labels[k+1]=labels[k+1],labels[k]
    assert cross%2==0
    parity=(cross//2)%2
    assert parity==(1 if row['name']=='old_root_0' else 0)
    braid_rows.append({'name':row['name'],'signed_source_root_crossings':cross,
                       'ordered_cover_character':parity})
out={'scope':__doc__,'base_lift':'v=1+sqrt(99/100), w=1-sqrt(99/100)',
     'seed_calibration':'All original cross seeds are moving; exact analytic proof in note.',
     'standard_peripheral_rows':seed_rows,'V_rows':V_rows,'actual_braid_characters':braid_rows,
     'input_hashes':{name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
       ['tangent_bundle_fiber_data.json','tangent_infinity_action.json','tangent_node_strips.json','tangent_bundle_words.json']},
     'conclusion':'J is contained in N_mov; alpha1 exchanges N_mov and N_const.',
     'not_proved':['J=N_mov','J normal in F13','I=R']}
(ROOT/'work_CE/tangent_selected_family_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('Four literal seed conjugators calibrate x1,x2,x6 constant and x4 moving: PASS.')
print('All four actual V words are moving-family peripherals: PASS.')
print('All ten source braids: only the q=1 old loop has odd ordered-cover character: PASS.')
