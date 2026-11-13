#!/usr/bin/env python3
"""Exhaust all lower s-centralizer freedom for the recorded T2 action.

Centralizers are constructed exactly through successive central extensions.
Every stored generator belongs to a full polycyclic sequence, not merely a
generating set for its linearization. Descending-index elimination produces
the complete kernel at each connecting homomorphism.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np
import d_cm_degree8_magnus as G
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):L=runpy.run_path(str(OUT/'d_cm_degree8_linear.py'))
R=L['R'];solve=R['solve'];ech=R['echelon'];invw=R['inverse']
def read(word):
    q,w=R['collapse'](word);assert q==R['e']
    P=R['poly'](w,8)
    return (0,)+tuple(R['bitpoly'](P[i]) for i in range(1,9))

# Check the exact involution words and the full polynomial substitution.
assert [R['collapse']([0]+w+[0])[1] for w in R['Kwords']]==[[-1],[-2],[-4],[-3]]
for w in R['Nwords'][:12]:
    p=read(w);assert G.involution(p)==read([0]+w+[0])
    assert G.mul(p,G.inverse(p))==G.UNIT

def kernel_relations(columns,descending=False):
    bas={};rels=[]
    order=range(len(columns)-1,-1,-1) if descending else range(len(columns))
    for j in order:
        v=columns[j];cert=1<<j
        while v:
            k=v.bit_length()-1
            if k not in bas:bas[k]=(v,cert);break
            v^=bas[k][0];cert^=bas[k][1]
        if not v:rels.append(cert)
    if descending:rels.reverse()
    return bas,rels

relpol=[read(w) for w in R['relwords']]
firstcols=[g[2]^G.involution(g)[2] for g in relpol]
_,fixed=kernel_relations(firstcols)
C=[G.selected_product(z,relpol) for z in fixed]
rows=[{'quotient_D':3,'centralizer_log2_order':len(C),
       'leading_dimensions':G.leading_independence(C)}]
print('Starting N/D3 centralizer:',len(C),flush=True)

for n in range(3,8):
    Z,labels=G.layer(n)
    Sz=[G.involution(z) for z in Z]
    cols=[z[n]^s[n] for z,s in zip(Z,Sz)]
    cb,fix=kernel_relations(cols)
    targets=[]
    for g in C:
        p=G.mul(g,G.inverse(G.involution(g)))
        assert all(not p[k] for k in range(1,n))
        _,_,rem=solve(p[n],cb);targets.append(rem)
    db,rels=kernel_relations(targets,descending=True)
    CC=[]
    for mask in rels:
        g=G.selected_product(mask,C)
        p=G.mul(g,G.inverse(G.involution(g)))
        good,sol,rem=solve(p[n],cb);assert good and not rem
        g=G.mul(G.selected_product(sol,Z),g)
        assert all(not (g[k]^G.involution(g)[k]) for k in range(1,n+1))
        CC.append(g)
    CC += [G.selected_product(mask,Z) for mask in fix]
    assert len(CC)==len(C)-len(db)+len(fix)
    dimensions=G.leading_independence(CC)
    C=CC
    row={'quotient_D':n+1,'layer_dimension':len(Z),
         'central_correction_rank':len(cb),'central_fixed_dimension':len(fix),
         'connecting_rank':len(db),'centralizer_log2_order':len(C),
         'leading_dimensions':dimensions}
    rows.append(row);print(row,flush=True)

# The degree-eight defects give a group homomorphism from this full finite
# centralizer to the cokernel of all central corrections. The right beta
# conjugator changes by these generators; beta lies in K, so its conjugation
# on degree eight is the identity. The order-three centralizer lifts by the
# coprime theorem and therefore supplies no additional obstruction classes.
bas=dict(L['bas']);rank_before=len(bas);nbase=2*len(L['Z'])+1
def add(v,cert):
    while v:
        k=v.bit_length()-1
        if k not in bas:bas[k]=(v,cert);return
        v^=bas[k][0];cert^=bas[k][1]
defects=[]
for j,g in enumerate(C):
    p=G.mul(g,G.inverse(G.involution(g)))
    assert all(not p[k] for k in range(1,8))
    defects.append(p[8]);add(p[8],1<<(nbase+j))
good,sol,rem=solve(L['target'],bas)
functional=None
if not good:
    # solve() stops at its first missing pivot; lower bits need not yet be
    # reduced. Its highest remaining bit is the certified free coordinate.
    j=rem.bit_length()-1
    functional=1<<j
    for k in sorted(bas):
        if (functional&bas[k][0]).bit_count()%2:functional^=1<<k
    assert all((functional&v[0]).bit_count()%2==0 for v in bas.values())
    assert all((functional&v).bit_count()%2==0 for v in defects)
    assert (functional&L['target']).bit_count()%2==1
summary={'centralizer_construction':rows,
 'complete_lower_centralizer_generators':len(C),
 'central_and_multiplier_rank':rank_before,
 'rank_after_all_lower_s_centralizer_defects':len(bas),
 'recorded_T2_action_has_torsion_conjugate_peripheral_lift_to_T3':good,
 'retained_G2_is_a_quotient_of_T2':True,
 'annihilating_functional_verified':functional is not None,
 'scope':'Complete same-lower-action torsion-conjugator test for the recorded T2 action, retaining its G6 data; no exclusion of every arbitrary finite automorphism lift or every action with the same CM pair.',
 'elapsed_seconds':round(time.time()-started,3)}
payload={'summary':summary,'remainder':hex(rem),'solution':hex(sol) if good else None,
 'separating_functional':hex(functional) if functional is not None else None,
 'full_centralizer_generators':[[hex(x) for x in g] for g in C],
 'full_degree8_defects':[hex(x) for x in defects]}
(OUT/'d_cm_degree8_centralizer.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
