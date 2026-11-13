#!/usr/bin/env python3
"""Independent read-only audit of the root's 96-point Hurwitz quotient.

Reconstructs every tuple and generator, verifies the actual Aut(A5)=S5
comparison through the five Sylow-four subgroups, and replays the pure
three-cycle certificate with its right-action word convention.  No
generic permutation-group order algorithm or slow search is invoked.
"""
from pathlib import Path
from itertools import permutations,product,combinations
import hashlib,json,math,time
import numpy as np

HERE=Path(__file__).resolve().parent

def cycles(g):
    unseen=set(range(len(g)));out=[]
    while unseen:
        x=min(unseen);cycle=[]
        while x in unseen:
            unseen.remove(x);cycle.append(x);x=int(g[x])
        out.append(cycle)
    return out

def power(g,n):
    out=np.arange(len(g))
    for _ in range(n):out=g[out]
    return out

def word_value(word,letters):
    out=np.arange(len(next(iter(letters.values()))))
    for letter in word:out=letters[letter][out]
    return out

def cycle_array(c,n=96):
    out=np.arange(n)
    for i,x in enumerate(c):out[x]=c[(i+1)%len(c)]
    return out

def main():
    start=time.time()
    protected=[HERE/(base+suffix) for base in (
        "e_hurwitz_five_a5_model_root","e_hurwitz_five_a5_order_root",
        "e_hurwitz_five_a5_order_pure_root") for suffix in (".py",".json",".npz",".out")]
    protected +=[HERE/"e_hurwitz_five_a5_verify_root.py"]
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in protected if p.exists()}
    model=json.loads((HERE/"e_hurwitz_five_a5_model_root.json").read_text())
    arrays=np.load(HERE/"e_hurwitz_five_a5_model_root.npz")
    original=json.loads((HERE/"e_hurwitz_five_a5_order_root.json").read_text())
    pure=json.loads((HERE/"e_hurwitz_five_a5_order_pure_root.json").read_text())
    permutations5=list(permutations(range(5)));ids={p:i for i,p in enumerate(permutations5)}
    mul=np.array([[ids[tuple(a[i] for i in b)] for b in permutations5] for a in permutations5])
    inv=np.array([int(np.flatnonzero(row==0)[0]) for row in mul])
    assert np.array_equal(mul,arrays["S5_mul"]) and np.array_equal(inv,arrays["S5_inv"])
    even=[i for i,p in enumerate(permutations5) if sum(p[a]>p[b]
                for a,b in combinations(range(5),2))%2==0]
    involutions=[i for i in even if i and mul[i,i]==0]
    conjugates=np.array([[mul[mul[c,g],inv[c]] for g in range(120)] for c in range(120)])
    assert len(even)==60 and len(involutions)==15
    sylow4=sorted({tuple(sorted({0,a,b,int(mul[a,b])})) for a,b in combinations(involutions,2)
                   if mul[a,b]==mul[b,a]})
    assert len(sylow4)==5 and all(len(v)==4 for v in sylow4)
    sylow_ids={v:i for i,v in enumerate(sylow4)}
    sylow_actions=[tuple(sylow_ids[tuple(sorted(int(conjugates[c,g]) for g in v))]
                           for v in sylow4) for c in range(120)]
    assert len(set(sylow_actions))==120
    assert len({sylow_actions[c] for c in even})==60
    # Every automorphism acts on these characteristic Sylow subgroups;
    # faithfulness follows from the faithful inner A5 action.  All 120
    # resulting permutations are realized by the displayed S5 conjugations.
    representatives=[tuple(r) for r in model["tuple_representatives"]]
    assert len(representatives)==96
    def subgroup(gs):
        found={0};todo=[0]
        for x in todo:
            for g in gs:
                y=int(mul[x,g])
                if y not in found:found.add(y);todo.append(y)
        return found
    coordinates={}
    for i,rep in enumerate(representatives):
        assert len(subgroup(rep))==60
        for c in range(120):
            gs=tuple(int(conjugates[c,g]) for g in rep)
            assert gs not in coordinates
            coordinates[gs]=(i,c)
    involution_set=set(involutions);all_count=generating_count=0
    nongenerating_orders={}
    for prefix in product(involutions,repeat=4):
        g=0
        for x in prefix:g=int(mul[g,x])
        last=int(inv[g])
        if last not in involution_set:continue
        all_count+=1;gs=prefix+(last,)
        if gs in coordinates:generating_count+=1
        else:
            order=len(subgroup(gs));assert order<60
            nongenerating_orders[order]=nongenerating_orders.get(order,0)+1
    assert all_count==11820 and generating_count==11520==len(coordinates)
    sig=[];transporters=[]
    for i in range(4):
        images=[];trans=[]
        for rep in representatives:
            hs=list(rep);g,h=hs[i:i+2]
            hs[i:i+2]=[int(mul[mul[g,h],inv[g]]),g]
            orbit,c=coordinates[tuple(hs)];images.append(orbit);trans.append(c)
        assert sorted(images)==list(range(96))
        sig.append(np.array(images));transporters.append(trans)
    sig=np.stack(sig)
    assert np.array_equal(sig,arrays["sigma"])
    assert transporters==model["Hurwitz_transporters"]
    one=np.arange(96)
    letters={i+1:g for i,g in enumerate(sig)}
    letters.update({-i:np.argsort(g) for i,g in list(letters.items())})
    for i in range(1,4):
        assert np.array_equal(word_value([i,i+1,i],letters),word_value([i+1,i,i+1],letters))
    for i,j in combinations(range(1,5),2):
        if j-i>1:assert np.array_equal(word_value([i,j],letters),word_value([j,i],letters))
    assert np.array_equal(word_value([1,2,3,4,4,3,2,1],letters),one)
    assert np.array_equal(word_value([1,2,3,4]*5,letters),one)
    pure_words=[];pure_arrays=[]
    for i in range(1,5):
        for j in range(i+1,6):
            h=list(range(j-1,i,-1));word=h+[i,i]+[-a for a in reversed(h)]
            pure_words.append(word);pure_arrays.append(word_value(word,letters))
    assert np.array_equal(np.stack(pure_arrays),arrays["pure"])
    pure_lookup={tuple(pair):value for pair,value in zip(model["pure_generator_pairs"],pure_arrays)}
    A12,A13,A23,A24,A34=[pure_lookup[pair] for pair in ((1,2),(1,3),(2,3),(2,4),(3,4))]
    # Right-action multiplication p*q is the array q[p].
    pair_x=[A12,A23[A13],A23,A13[A12],A12]
    pair_y=[A24[A23],A34,A34,A34[A24],A23]
    for i in range(2,5):
        yword=list(range(i-1,0,-1))+list(range(1,i))
        pair_x.append(word_value(yword,letters))
        pair_y.append(word_value([i,i],letters))
    assert np.array_equal(np.stack(pair_x),arrays["x"])
    assert np.array_equal(np.stack(pair_y),arrays["y"])
    square_letters={i:g[g] for i,g in letters.items()}
    word=pure["three_cycle_word_in_signed_squares"]
    value=word_value(word,square_letters)
    c=power(value,int(pure["isolating_power"]))
    assert [v for v in cycles(c) if len(v)>1]==[[17,26,43]]
    assert all(sum(len(v)-1 for v in cycles(g))%2==0 for g in sig)
    assert np.array_equal(sig,np.load(HERE/"e_hurwitz_five_a5_order_pure_root.npz")["sigma"])
    reached=set();induction=[]
    for record in pure["conjugate_records"]:
        g=word_value(record["conjugator_word"],square_letters)
        # This array is g^{-1} c g in the right-action word convention.
        d=g[c[np.argsort(g)]]
        nontrivial=[v for v in cycles(d) if len(v)>1]
        assert nontrivial==[record["three_cycle"]]
        support=set(nontrivial[0]);assert sorted(support)==record["support"]
        if not reached:
            reached|=support;induction.append({"case":"initial A3","support":sorted(support)});continue
        intersection=support&reached;new=support-reached
        assert len(intersection) in (1,2) and new
        if len(intersection)==2:
            induction.append({"case":"two shared vertices","support":sorted(support),
                              "added":sorted(new)})
        else:
            x=next(iter(intersection));y,z=sorted(reached-{x})[:2]
            old_cycle=cycle_array([x,y,z])
            derived=d[old_cycle[np.argsort(d)]]
            derived_support=set(np.flatnonzero(derived!=one).tolist())
            assert len(derived_support&reached)==2 and len(derived_support-reached)==1
            expanded=reached|derived_support
            assert len(support&expanded)==2 and len(support-expanded)==1
            induction.append({"case":"one shared vertex, two exact two-vertex steps",
                "support":sorted(support),"old_cycle":[x,y,z],
                "derived_cycle":next(v for v in cycles(derived) if len(v)==3),
                "added":sorted(new)})
        reached|=support
    assert reached==set(range(96))
    assert len(pure["conjugate_records"])==72
    assert len(original["conjugate_records"])==62
    assert pure["pure_target_order"]==pure["full_target_order"]==math.factorial(96)//2
    assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in protected if p.exists()}
    out={"tuple_count":all_count,"generating_tuple_count":generating_count,
        "nongenerating_tuple_subgroup_orders":nongenerating_orders,
        "actual_Aut_A5_equals_S5_comparison":"faithful action on the five Sylow-four subgroups; all120 permutations realized",
        "free_Aut_orbit_count":96,"all_original_generator_arrays_reconstructed":True,
        "all_tuple_transporters_reconstructed":True,"all_Artin_and_sphere_relations_replayed":True,
        "all_eight_pentagon_and_NS_action_pairs_reconstructed":True,
        "right_action_word_convention":"append a generator by array new=generator[old]",
        "recorded_conjugator_convention":"g[c[g^-1]] equals the word g^-1 c g",
        "pure_isolating_power":pure["isolating_power"],"isolated_cycle":[17,26,43],
        "pure_square_conjugate_count":72,"earlier_unsquared_conjugate_count":62,
        "support_induction":induction,"exact_pure_and_full_group":"A96",
        "order":math.factorial(96)//2,"generic_order_algorithm_used":False,
        "protected_input_hashes":hashes,"protected_inputs_unchanged":True,
        "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_hurwitz_five_a5_audit.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k not in ("support_induction","protected_input_hashes")},indent=2))
    print("PASS: independent complete Hurwitz tuple/action audit and constructive pure A96 proof.")

if __name__=="__main__":main()
