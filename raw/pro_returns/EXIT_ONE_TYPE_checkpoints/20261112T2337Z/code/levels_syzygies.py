#!/usr/bin/env python3
"""Exact expansion of all44 first identities. Term [w,j,e]=w R_j^e w^-1.
All indices are one-based. Completeness is proved in P5c3--P5c4.
"""
from pathlib import Path
import json


def red(word):
    out=[]
    for x in word:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)


def inv(w):return tuple(-x for x in reversed(w))
def mul(*words):return red(x for w in words for x in w)
def sub(w,a):return mul(*(a[x-1] if x>0 else inv(a[-x-1]) for x in w))
def identity(n):return tuple((i,) for i in range(1,n+1))
def compose(a,b):return tuple(sub(w,a) for w in b)


def artin_generator(n,t):
    a=list(identity(n));i=abs(t)
    if t>0:a[i-1],a[i]=(i,i+1,-i),(i,)
    else:a[i-1],a[i]=(i+1,),(-(i+1),i,i+1)
    return tuple(a)


def artin(n,w):
    a=identity(n)
    for t in w:a=compose(a,artin_generator(n,t))
    return a


def pure(i,j):
    return tuple(range(j-1,i,-1))+(i,i)+tuple(-a for a in range(i+1,j))


def c(u,v):return mul(inv(v),inv(u),v,u)
def conjugate(w,v):return mul(w,v,inv(w))


def expand_family(nb,nf,base_relators,actions,inverse_actions):
    def embed(w):return tuple((abs(x)+nb)*(1 if x>0 else -1) for x in w)
    relators=list(base_relators)
    for h in range(1,nb+1):
        for u in range(1,nf+1):
            relators.append(mul((h,),embed((u,)),(-h,),inv(embed(actions[h-1][u-1]))))
    def invert_terms(terms):return [(w,j,-e) for w,j,e in reversed(terms)]
    def conjugate_terms(w,terms):return [(mul(w,v),j,e) for v,j,e in terms]
    def letter_d(h,v):
        if h<0:
            inside=letter_d(-h,sub(v,inverse_actions[-h-1]))
            return conjugate_terms((h,),invert_terms(inside))
        terms=[];prefix=()
        for u in v:
            image=actions[h-1][abs(u)-1]
            local=() if u>0 else inv(image)
            j=len(base_relators)+(h-1)*nf+abs(u)
            terms.append((embed(mul(prefix,local)),j,1 if u>0 else -1))
            prefix=mul(prefix,image if u>0 else inv(image))
        return terms
    def word_d(w,v):
        terms=[];image=v
        for h in reversed(w):
            terms=conjugate_terms((h,),terms)+letter_d(h,image)
            image=sub(image,actions[h-1] if h>0 else inverse_actions[-h-1])
        return terms,image
    identities=[]
    for i,relator in enumerate(base_relators):
        for u in range(1,nf+1):
            terms,image=word_d(relator,(u,))
            assert image==(u,),("nonidentity action",i+1,u)
            terms=[((),i+1,1),(embed((u,)),i+1,-1)]+invert_terms(terms)
            evaluated=()
            for w,j,e in terms:
                r=relators[j-1]
                evaluated=mul(evaluated,w,r if e>0 else inv(r),inv(w))
            assert not evaluated,("identity expansion failure",i+1,u)
            identities.append({"base_relator":i+1,"fibre_generator":u,"terms":terms})
    return {"base_generators":nb,"fibre_generators":nf,"relators":relators,"identities":identities}


def main():
    x,y,z=(3,),(4,),(5,)
    images=((mul(inv(z),x,z),conjugate(c(x,z),y),mul(c(x,z),z)),
            (x,mul(inv(z),y,z),mul(c(y,z),z)))
    relators=[mul((h,u,-h),inv(images[h-1][u-3])) for h in (1,2) for u in (3,4,5)]
    braids=(pure(1,3),pure(2,3),pure(1,4),pure(2,4),pure(3,4))
    actions=[artin(4,tuple(-t for t in w)) for w in braids]
    negative=[artin(4,inv(tuple(-t for t in w))) for w in braids]
    cube=[(a,b,-a,-b) for a in (1,2) for b in (3,4)]
    data={
        "Gamma06":expand_family(5,4,relators,actions,negative),
        "Gamma05_times_F2":expand_family(5,2,relators,[identity(2)]*5,[identity(2)]*5),
        "F2_cubed":expand_family(4,2,cube,[identity(2)]*4,[identity(2)]*4)}
    data["Gamma06"]["generator_names"]=list("abxyzpqrs")
    data["Gamma05_times_F2"]["generator_names"]=["a","b","x","y","z","t1","t2"]
    data["F2_cubed"]["generator_names"]=["a1","a2","b1","b2","c1","c2"]
    expected={
        "Gamma06":(26,24,[36,64,16,26,366,640,168,144,92,178,44,52,18,42,36,12,8,36,16,26,10,92,44,52],171),
        "Gamma05_times_F2":(16,12,[8,8,14,14,10,10,6,6,8,8,10,10],11),
        "F2_cubed":(12,8,[6]*8,4)}
    lines=[]
    for name,family in data.items():
        counts=[len(o["terms"]) for o in family["identities"]]
        longest=max(len(t[0]) for o in family["identities"] for t in o["terms"])
        actual=(len(family["relators"]),len(family["identities"]),counts,longest)
        assert actual==expected[name]
        lines += [name+": "+str(actual[0])+" relators, "+str(actual[1])+" expanded identities",
                  "  conjugate-factor counts: "+str(counts),
                  "  maximum conjugator length: "+str(longest),
                  "  all products freely reduce to the empty word: PASS"]
    lines += ["Total expanded first identities checked:44",
              "Term [w,j,e] denotes w R_j^e w^-1; indices one-based.",
              "Completeness/free-basis statements are proved in P5c3--P5c4."]
    here=Path(__file__).resolve().parent
    (here/"levels_syzygies_output.txt").write_text("\n".join(lines)+"\n")
    (here/"levels_syzygies_expanded_python.json").write_text(json.dumps(data,indent=2)+"\n")
    print("\n".join(lines))


if __name__=="__main__":main()
