#!/usr/bin/env python3
"""Exact Levi principal minors; the infinite-fibre proof is P5b3."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp


def main():
    lines=[];data=[]
    for n in (5,6):
        d=n-3;normals=[];forms=[]
        for i in range(d):
            v=[0]*d;v[i]=1
            normals.extend([v[:],v[:]])
            forms.extend(["z"+str(i+1),"z"+str(i+1)+"-1"])
        for i,j in combinations(range(d),2):
            v=[0]*d;v[i]=1;v[j]=-1
            normals.append(v);forms.append("z"+str(i+1)+"-z"+str(j+1))
        weights=sp.symbols("w1:"+str(len(normals)+1),positive=True)
        levi=sp.eye(d)
        for w,v in zip(weights,normals):
            a=sp.Matrix(v);levi+=w*a*a.T
        minors=[]
        for q in range(1,d+1):
            for subset in combinations(range(d),q):
                p=sp.Poly(sp.expand(levi.extract(subset,subset).det()),*weights)
                assert all(c>0 for c in p.coeffs())
                assert p.eval(dict.fromkeys(weights,0))==1
                minors.append({"indices":subset,"monomials":len(p.terms())})
        count=len(sp.Poly(sp.expand(levi.det()),*weights).terms())
        assert count==(14 if n==5 else 93)
        lines += ["M_0,"+str(n)+": dimension "+str(d)+", forms "+str(len(forms)),
                  "  all "+str(len(minors))+" principal minors have positive coefficients and constant1",
                  "  determinant monomials: "+str(count),
                  "  Levi matrix: "+str(levi)]
        data.append({"n":n,"forms":forms,"normals":normals,"levi":str(levi),
                     "principal_minors":minors,"determinant_monomials":count})
    lines += ["Exhaustion: sum |z_i|^2 + sum |ell|^-2.",
              "Properness, finite Morse set, and end/fibre argument are proved in P5b3.",
              "No finite stable-tree quotient certifies the infinite fibre."]
    here=Path(__file__).resolve().parent
    (here/"levels_stein_output.txt").write_text("\n".join(lines)+"\n")
    (here/"levels_stein_output.json").write_text(json.dumps(data,indent=2)+"\n")
    print("\n".join(lines))


if __name__=="__main__":main()
