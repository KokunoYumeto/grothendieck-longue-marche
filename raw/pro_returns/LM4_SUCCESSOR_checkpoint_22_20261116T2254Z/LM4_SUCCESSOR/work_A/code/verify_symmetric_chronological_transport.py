#!/usr/bin/env python3
"""Independent chronological push/pull audit for the actual symmetric family.
Reads CE/DE raw words and the exact endpoint involution without modifying them.
The convention follows the exact PL single-half-twist calibration:
positive chronological crossing is geometric push phi_i, whereas art()
postcomposes its current images by phi_i. Hence push(W)=art(reverse W)
and pull(W)=art(negate W). No convention search is performed.
"""
from pathlib import Path
import json, hashlib, time

ROOT=Path(__file__).resolve().parents[2]
INPUTS={
 "bridge":ROOT/"work_CE/next_symmetric_nodes/symmetric_source_bridge.json",
 "endpoint":ROOT/"work_DE/next_marginal_source/symmetric_fixed_basis.json",
 "old":ROOT/"work_CE/next_symmetric_nodes/symmetric_old_base_words.json",
 "single_crossing":ROOT/"work_DE/next_marginal_source/cut_Artin_convention.json",
}
raw={k:p.read_bytes() for k,p in INPUTS.items()}
data={k:json.loads(v) for k,v in raw.items()}
N=21
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)
def inv(w): return tuple(-x for x in reversed(w))
def sub(w,A):
    return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
def art(w):
    A={i:(i,) for i in range(1,N+1)}
    for x in w:
        i=abs(x);a,b=A[i],A[i+1]
        A[i],A[i+1]=(red(a+b+inv(a)),a) if x>0 else (b,red(inv(b)+a+b))
    return A
def push(w): return art(tuple(reversed(w)))
def pull(w): return art(tuple(-x for x in w))
def inner_word(E):
    conj={}
    for j,e in E.items():
        left,right=0,len(e)
        while right-left>1 and e[left]==-e[right-1]:
            left+=1;right-=1
        assert e[left:right]==(j,),("not conjugate to generator",j,e[left:right])
        conj[j]=e[:left]
    v=red(inv(conj[1])+conj[2]);n=0;k=0
    while k<len(v) and abs(v[k])==1:
        n+=v[k];k+=1
    tail=v[k:]
    assert not tail or all(x==tail[0] and abs(x)==2 for x in tail),tail
    g=red(conj[1]+((1,)*n if n>=0 else (-1,)*(-n)))
    assert all(E[j]==red(g+(j,)+inv(g)) for j in range(1,N+1))
    return g

start=time.monotonic()
assert data["single_crossing"]["images"][0]["image"]==[1,2,-1]
assert data["single_crossing"]["images"][1]["image"]==[1]
W=data["bridge"]["nodal_base_to_pairing_base_braid"]
P,Q=push(W),pull(W)
assert all(sub(P[j],Q)==(j,)==sub(Q[j],P) for j in range(1,N+1))
assert data["bridge"]["rational_pairing_base_order"]==data["endpoint"]["original_generator_physical_order"]
Fend={int(k):tuple(v) for k,v in data["endpoint"]["involution_images"].items()}
Fstart={j:sub(sub(P[j],Fend),Q) for j in range(1,N+1)}
assert all(sub(Fstart[j],Fstart)==(j,) for j in range(1,N+1))
print("PASS: exact PL elementary push convention; chronological push reverses the stored list, pull negates it.")
print("PASS: all42 bridge inverse compositions and all21 transported involution squares.")
rows=[]
for row in data["old"]["loops"]:
    w=row["word"];A,Ai=push(w),pull(w)
    assert all(sub(A[j],Ai)==(j,)==sub(Ai[j],A) for j in range(1,N+1))
    assert sub(tuple(range(1,N+1)),A)==tuple(range(1,N+1))
    comm={j:sub(sub(sub(Ai[j],Fstart),A),Fstart) for j in range(1,N+1)}
    g=inner_word(comm)
    rows.append({"index":row["index"],"name":row["name"],
                 "raw_crossing_count":len(w),
                 "commutator_convention":"F A F A^-1",
                 "exact_inner_conjugator":list(g),
                 "all_21_images_verified":True,
                 "literal_commutation":not g})
    print("PASS: old loop",row["name"],"commutes with F up to the exact inner word",list(g),flush=True)
out={
 "scope":__doc__,
 "input_sha256":{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},
 "producer_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 "bridge_raw_word":W,
 "push_formula":"art(reverse chronological word)",
 "pull_formula":"art(negate each chronological crossing)",
 "transport_formula":"F_start = pull(W) compose F_endpoint compose push(W)",
 "F_at_nodal_base":{str(k):list(v) for k,v in Fstart.items()},
 "old_actions":rows,
 "elapsed_seconds":time.monotonic()-start,
 "claims_excluded":["source-ideal equality","syzygy vanishing","fixed lifting","compact coefficient comparison"],
}
(ROOT/"work_A/symmetric_chronological_transport_verification.json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS: all6 actual old-base actions; no input artifact modified.")
print("Elapsed seconds",round(out["elapsed_seconds"],6))

