"""Independent Hall-coordinate replay of A's one exact retained-residue test.

No producer is imported. Source permutations are reconstructed from literal
F11 images/conjugators; degree two is computed by collecting into ordered
Hall form, rather than by the producer's Magnus coefficient recurrence.
"""
from pathlib import Path
from collections import defaultdict, deque
import json,hashlib

ROOT=Path(__file__).resolve().parents[2]
FP=ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
SP=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
AP=ROOT/'work_A/D_source_full_retained_class2_26.json'
F=json.loads(FP.read_text());S=json.loads(SP.read_text());A=json.loads(AP.read_text())
COL=(1,2,3,4,6,7,8,9); IX={c:n for n,c in enumerate(COL)}
RETAINED={5:1,10:2,11:4}

def red(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x:ans.pop()
        else:ans.append(x)
    return ans
def inv(w):return [-x for x in reversed(w)]
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,im):return mul(*(im[abs(x)] if x>0 else inv(im[abs(x)]) for x in w))
def bits(w):
    r=0
    for x in w:r^=RETAINED.get(abs(x),0)
    return r
def vid(c,t):return 8*IX[c]+t
def pair(x,y):return tuple(sorted((x,y)))

permutations={};factor_checks=0
for name,op in F['all_four_signed_source_operators'].items():
    images={int(k):v for k,v in S['source_ordinary_actions'][name].items()}
    columns=[bits(images[i]) for i in (5,10,11)]
    p=[]
    for c in COL:
        r=op['family_images'][str(c)];h=r['conjugator_F11']
        assert r['signed_core']==c
        assert mul(h,[c],inv(h))==red(images[c])
        factor_checks+=1
        for t in range(8):
            lin=0
            for j in range(3):
                if t&(1<<j):lin^=columns[j]
            p.append(vid(c,lin^bits(h)))
    assert sorted(p)==list(range(64))
    permutations[name]=p
for op in ('m','v'):
    p,q=permutations[op],permutations[op+'_inverse']
    assert all(p[q[i]]==q[p[i]]==i for i in range(64))
for n,shift in enumerate((1,2,4)):
    permutations['deck_'+str(n)]=[vid(c,t^shift) for c in COL for t in range(8)]
assert permutations==A['all_seven_permutations']

seedpairs=[]
for row in F['all40_node_factor_pairs']:
    vv=[]
    for key in ('first_factor','second_factor'):
        r=row[key];h=r['conjugator_F11'];core=r['signed_core']
        assert mul(h,[core],inv(h))==red(r['word_F11'])
        factor_checks+=1
        vv.append(vid(abs(core),bits(h)))
    seedpairs.append(pair(*vv))
assert len(seedpairs)==40
assert [list(x) for x in seedpairs]==A['forty_seed_pairs']
edges=set(seedpairs); todo=deque(edges)
while todo:
    ij=todo.popleft()
    for p in permutations.values():
        image=pair(p[ij[0]],p[ij[1]])
        if image not in edges:edges.add(image);todo.append(image)
assert len(edges)==512
assert edges=={tuple(x) for x in A['complete_allowed_pairs']}
assert all(pair(p[i],p[j]) in edges for p in permutations.values() for i,j in edges)

def hall(word):
    """Collect x0^a0 ... x63^a63 times commutators [xi,xj], i<j."""
    t=0;exps=[0]*64;central=defaultdict(int)
    for x in word:
        if abs(x) in RETAINED:
            t^=RETAINED[abs(x)]
            continue
        i=vid(abs(x),t);sgn=1 if x>0 else -1
        # Moving the appended xi left through higher-index powers gives
        # [xi,xj]^(-sgn*aj), independently of Magnus expansions.
        for j in range(i+1,64):
            if exps[j]:central[i,j]-=sgn*exps[j]
        exps[i]+=sgn
    assert t==0
    return exps,{ij:v for ij,v in central.items() if v}

raw=[x['fiber11'] for x in S['actual_six_source_normal_forms'][:4]]
Ds=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]))
U=mul(raw[0],inv(raw[3]),inv(raw[0]))
results=[]
for label,w in [('D_s',Ds),('U_known',U)]:
    for op in ('m','m_inverse'):
        im={int(k):v for k,v in S['source_ordinary_actions'][op].items()}
        defect=mul(sub(w,im),inv(w))
        ab,coords=hall(defect)
        assert not any(ab)
        survivor={ij:v for ij,v in coords.items() if ij not in edges}
        ref=next(r for r in A['results'] if r['word']==label and r['operator']==op)
        assert defect==ref['defect_F11']
        assert [[i,j,v] for (i,j),v in sorted(coords.items())]==ref['all_degree2_upper_coordinates']
        assert [[i,j,v] for (i,j),v in sorted(survivor.items())]==ref['surviving_upper_coordinates']
        mod3={ij:v%3 for ij,v in survivor.items() if v%3}
        if label=='D_s':assert len(survivor)==len(mod3)==8
        else:assert not survivor
        results.append({'word':label,'operator':op,'raw_length':len(defect),
                        'independent_Hall_coordinates':[[i,j,v] for (i,j),v in sorted(coords.items())],
                        'surviving_coordinates':[[i,j,v] for (i,j),v in sorted(survivor.items())],
                        'surviving_mod3':[[i,j,v] for (i,j),v in sorted(mod3.items())]})
        print(label,op,'Hall survivors',len(survivor),'mod3 survivors',len(mod3))

out={'status':'PASS_NONZERO_ACTUAL_D_SOURCE_DEFECT',
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (FP,SP,AP)},
     'literal_factor_checks':factor_checks,'complete_permutations':7,'complete_seed_count':40,
     'complete_allowed_pair_count':len(edges),'results':results,
     'scope':'Independent literal-input/permutation replay and ordered Hall collection. All-source/all-deck normal-closure and finite-quotient arguments are supplied in the companion review, not inferred from bounded word depth.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all112 literal factors, all7 permutations, all40 seeds and full512-pair closure.')
print('Both actual D_s defects are nonzero integrally and mod3; known U controls vanish.')
