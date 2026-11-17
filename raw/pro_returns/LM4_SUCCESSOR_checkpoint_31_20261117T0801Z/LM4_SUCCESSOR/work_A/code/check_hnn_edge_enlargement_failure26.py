#!/usr/bin/env python3
"""Exact universal words for the actual failed HNN edge extension."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*w):return red(x for a in w for x in a)
def conj(g,w):return mul(g,w,inv(g))
def comm(a,b):return mul(a,b,inv(a),inv(b))
# First alphabet a=1,B=2: exact actual reflection and conjugated word.
a=(1,);B=(2,)
eta_a=mul(a,B,inv(a),inv(B),inv(a))
v=mul(inv(a),eta_a,a)
assert v==mul(B,inv(a),inv(B))
# Second alphabet A=1,q=p(a1)=2,z=p(b)=3,k=4.
A=(1,);q=(2,);z=(3,);k=(4,)
v0=mul(A,inv(q));s=conj(inv(v0),k)
sigma_a1=mul(q,z,inv(q),inv(z),inv(q))
left=conj(inv(q),comm(s,sigma_a1))
right=comm(conj(inv(A),k),conj(z,inv(q)))
assert left==right
assert mul(inv(q),sigma_a1,q)==conj(z,inv(q))
out={'status':'PASS_EXACT_WORD_IDENTITIES','eta_a':eta_a,'a_inverse_eta_a_a':v,
     'target_after_q_conjugation':left,'reduced_amalgam_factors':['A^-1 k A','p(C B a^-1 B^-1 C)','inverse first','inverse second'],
     'scope':'The actual nontriviality uses the complete retraction/winding/amalgam normal-form proof, not a quotient evaluator.'}
(ROOT/'work_A/hnn_edge_enlargement_failure26.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact actual eta(a) and v=B a^-1 B^-1')
print('PASS complete conjugated target commutator identity')
print('PASS exact p(C v C) word z q^-1 z^-1')
print('SCOPE normal-form nontriviality is the structural proof with both factors outside the actual edge')
