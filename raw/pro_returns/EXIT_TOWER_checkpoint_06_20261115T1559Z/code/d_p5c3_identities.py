#!/usr/bin/env python3
"""Twenty-four exact identity sequences for the 26-relator M0,6 presentation.

Generators1..5 are a,b,x,y,z, and6..9 are p,q,r,s.  Relators0..5
are the six base relators;6+4*(h-1)+(u-1) is h u h^-1 phi_h(u)^-1.
Each identity is a list of (conjugator,relator_index,exponent) whose
expanded product freely reduces to the empty word. No quotient word
problem or numerical homology is used in the final verification.
"""
from pathlib import Path
import json,ast
P=Path(__file__).resolve().parent
src=ast.parse((P/'b_genus_zero.py').read_text())
exec(compile(ast.Module(body=[x for x in src.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'b_genus_zero.py','exec'),globals())
B=json.loads((P/'b_genus_zero.json').read_text())['compact']
base=[tuple(w) for w in B['M05_relators']]
acts=[[tuple(w) for w in f] for f in B['M06_actions']]
acts_inv=[[tuple(w) for w in f] for f in B['M06_inverse_actions']]

def global_fibre(w):return tuple((abs(x)+5)*(1 if x>0 else -1) for x in w)
def phi(h,v):return subst(v,acts[h-1] if h>0 else acts_inv[-h-1])
def action_base(w,v):
    for h in reversed(w):v=phi(h,v)
    return v
rels=base[:]
for h in range(1,6):
    for u in range(1,5):rels.append((h,u+5,-h)+inv(global_fibre(phi(h,(u,)))))
assert len(rels)==26

def conjugate(c,seq):return [(red(c+p),j,e) for p,j,e in seq]
def inverse(seq):return [(p,j,-e) for p,j,e in reversed(seq)]
def positive(h,v):
    """h v h^-1 phi_h(v)^-1 for h positive, v an arbitrary fibre word."""
    out=[];prefix=()
    for x in v:
        i=abs(x);im=phi(h,(i,));idx=6+4*(h-1)+(i-1)
        if x>0:out.append((global_fibre(prefix),idx,1))
        else:out.append((global_fibre(red(prefix+inv(im))),idx,-1))
        prefix=red(prefix+phi(h,(x,)))
    return out
def letter(h,v):
    if h>0:return positive(h,v)
    return conjugate((h,),inverse(positive(-h,phi(h,v))))
def certificate(w,v):
    if not w:return []
    h=w[0];tail=w[1:]
    return conjugate((h,),certificate(tail,v))+letter(h,action_base(tail,v))
def expansion(seq):
    return red(x for c,j,e in seq for x in c+(rels[j] if e>0 else inv(rels[j]))+inv(c))

out=[]
for j,R in enumerate(base):
    for u in range(1,5):
        v=(u,);image=action_base(R,v);assert image==v
        seq=certificate(R,v)
        expected=red(R+global_fibre(v)+inv(R)+inv(global_fibre(image)))
        assert expansion(seq)==expected
        seq += [(global_fibre(v),j,1),((),j,-1)]
        assert expansion(seq)==()
        out.append({'base_relator':j,'fibre_generator':u+5,
                    'identity_sequence':[{'conjugator':c,'relator':r,'exponent':e} for c,r,e in seq],
                    'conjugate_factor_count':len(seq),
                    'freely_reduced_product':[]})
counts={'identities':len(out),'defining_relators':len(rels),
        'conjugate_factors':sum(x['conjugate_factor_count'] for x in out),
        'largest_identity':max(x['conjugate_factor_count'] for x in out)}
data={'generators':['a','b','x','y','z','p','q','r','s'],'relators':rels,'identities':out,'counts':counts}
(P/'d_p5c3_identities.json').write_text(json.dumps(data,indent=2)+'\n')
print('Exact P5c3 identity certificate:',counts)
print('Every one of the24 expanded products is freely the empty word on the nine generators.')
print('Base-relator/fibre-generator factor counts:')
for i in range(6):print(i,[x['conjugate_factor_count'] for x in out if x['base_relator']==i])
