#!/usr/bin/env python3
"""Nonabelian index presentations and exact rational sharpness checks."""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json
from levels_braids import red, inv


def substitute(word,g,replacement):
    out=[]
    for x in word:
        out.extend(replacement if x==g else inv(replacement) if x==-g else (x,))
    return red(out)


def index_presentation(m,depth):
    vertices=[frozenset(c) for q in range(1,depth+1) for c in combinations(range(m),q)]
    chains=[[(v,) for v in vertices]]
    while True:
        nxt=[c+(v,) for c in chains[-1] for v in vertices if c[-1]<v]
        if not nxt: break
        chains.append(nxt)
    edges=chains[1] if len(chains)>1 else []
    triangles=chains[2] if len(chains)>2 else []
    adjacency={v:[] for v in vertices}
    for a,b in edges:
        adjacency[a].append(b); adjacency[b].append(a)
    seen={vertices[0]}; queue=[vertices[0]]; tree=set()
    for a in queue:
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b);queue.append(b);tree.add(frozenset((a,b)))
    assert len(seen)==len(vertices)
    gens={}
    for a,b in edges:
        if frozenset((a,b)) not in tree: gens[(a,b)]=len(gens)+1
    def edge(a,b):
        if frozenset((a,b)) in tree: return ()
        return (gens[(a,b)],) if (a,b) in gens else (-gens[(b,a)],)
    rels=[red(edge(a,b)+edge(b,c)+edge(c,a)) for a,b,c in triangles]
    remaining=set(gens.values()); eliminations=[]
    while True:
        found=None
        for rel in rels:
            for g in sorted(remaining):
                positions=[i for i,x in enumerate(rel) if abs(x)==g]
                if len(positions)==1:
                    p=positions[0];left,right=rel[:p],rel[p+1:]
                    replacement=red(inv(left)+inv(right)) if rel[p]>0 else red(right+left)
                    found=(g,replacement);break
            if found:break
        if not found:break
        g,replacement=found
        rels=[substitute(w,g,replacement) for w in rels]
        rels=[w for w in rels if w]
        remaining.remove(g);eliminations.append([g,replacement])
    return {"depth":depth,"f_vector":[len(c) for c in chains],
            "initial_index_generators":len(gens),"triangle_relators":len(triangles),
            "tietze_eliminations":eliminations,
            "remaining_generators":sorted(remaining),"remaining_relators":rels}


def rank(matrix):
    if not matrix or not matrix[0]:return 0
    a=[[Fraction(x) for x in r] for r in matrix];p=0
    for col in range(len(a[0])):
        row=next((i for i in range(p,len(a)) if a[i][col]),None)
        if row is None:continue
        a[p],a[row]=a[row],a[p];q=a[p][col];a[p]=[x/q for x in a[p]]
        for i in range(len(a)):
            if i!=p and a[i][col]:
                q=a[i][col];a[i]=[x-q*y for x,y in zip(a[i],a[p])]
        p+=1
        if p==len(a):break
    return p


def sphere(k):
    cells=[list(combinations(range(k+2),j+1)) for j in range(k+1)]
    ranks=[0]
    for j in range(1,k+1):
        rows={s:i for i,s in enumerate(cells[j-1])}
        matrix=[[0]*len(cells[j]) for _ in cells[j-1]]
        for col,s in enumerate(cells[j]):
            for t in range(j+1):matrix[rows[s[:t]+s[t+1:]]][col]=(-1)**t
        ranks.append(rank(matrix))
    ranks.append(0)
    betti=[len(cells[j])-ranks[j]-ranks[j+1] for j in range(k+1)]
    betti[0]-=1
    assert betti==[int(j==k) for j in range(k+1)]
    return {"k":k,"f_vector":[len(c) for c in cells],"reduced_betti":betti}


def main():
    results=[index_presentation(3,r) for r in (2,3)]
    assert results[0]["f_vector"]==[6,6] and len(results[0]["remaining_generators"])==1
    assert results[1]["f_vector"]==[7,12,6] and not results[1]["remaining_generators"]
    assert all(not r["remaining_relators"] for r in results)
    spheres=[sphere(k) for k in range(5)]
    lines=[]
    for r in results:
        lines += ["depth <= "+str(r["depth"])+": f-vector "+str(r["f_vector"]),
                  "  spanning-tree generators: "+str(r["initial_index_generators"]),
                  "  triangle relators: "+str(r["triangle_relators"]),
                  "  Tietze eliminations: "+str(len(r["tietze_eliminations"])),
                  "  remaining index generators: "+str(len(r["remaining_generators"]))]
    lines += ["Depth <=2 bicategorical groupoid colimit: Z^3 x F1 = Z^4.",
              "Depth <=3 with all flag triangles: Z^3.",
              "Strict group colimits are a different construction."]
    lines += ["Sharpness k="+str(s["k"])+": reduced Betti="+str(s["reduced_betti"]) for s in spheres]
    here=Path(__file__).resolve().parent
    (here/"levels_colimit_output.txt").write_text("\n".join(lines)+"\n")
    (here/"levels_colimit_output.json").write_text(json.dumps({"presentations":results,"spheres":spheres},indent=2)+"\n")
    print("\n".join(lines))


if __name__=="__main__":main()
