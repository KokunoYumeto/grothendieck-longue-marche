#!/usr/bin/env python3
"""Exact integral doubled-log coordinates for the odd-primary H class-two tower.

Coordinates (v,Z) use Z=2*log_central.  They lie in Z_3^10 x Z_3^45;
the multiplication is (v+w,Z+T+v wedge w).  Every displayed matrix
is integral, and reduction modulo 3^n gives the actual exponent-3^n
class-two H quotient after the invertible change Z=2z.
"""
from pathlib import Path
import json
import numpy as np
import de_fermat_schreier as f

HERE=Path(__file__).resolve().parent
I,J=f.UP
ZERO=np.zeros(55,dtype=np.int64)

def wedge(v,w):
    return v[I]*w[J]-v[J]*w[I]

def multiply(g,h):
    out=g+h
    out[10:]+=wedge(g[:10],h[:10])
    return out

def collect_signed(word):
    letters=np.asarray(word,dtype=np.int64)
    if not len(letters):return ZERO.copy()
    ix=np.abs(letters)-1;signs=np.where(letters>0,1,-1)
    v=np.zeros(10,dtype=np.int64);columns=np.zeros((10,10),dtype=np.int64)
    for i in range(10):
        entries=signs*(ix==i);v[i]=entries.sum();prefix=np.cumsum(entries)-entries
        for j in range(10):
            mask=ix==j;columns[i,j]=prefix[mask]@signs[mask]
    return np.r_[v,(columns-columns.T)[I,J]]

def literal(word):return collect_signed(f.schreier(word))

def substitute(word,images):
    image={1:images[0],2:images[1]}
    image[-1]=f.inverse_word(image[1]);image[-2]=f.inverse_word(image[2])
    return [letter for source in word for letter in image[source]]

def exterior(a):
    return np.stack([wedge(a[:,i],a[:,j]) for i,j in zip(I,J)],axis=1)

def action(images):
    columns=np.stack([literal(substitute(w,images)) for w in f.NWORDS],axis=1)
    out=np.zeros((55,55),dtype=np.int64)
    out[:,:10]=columns;out[10:,10:]=exterior(columns[:10])
    return out

S=action(([2],[1]))
R=action(([2],[-2,-1]))
assert np.array_equal(S@S,np.eye(55,dtype=np.int64))
assert np.array_equal(R@R@R,np.eye(55,dtype=np.int64))

def norm_errors(g):
    return np.r_[multiply(S@g,g),multiply(multiply(-g,R@(-g)),R@R@(-g))]

if __name__=="__main__":
    import bc_fermat_class_two as finite
    scale=np.diag([1]*10+[2]*45)
    assert np.array_equal(S@scale%3,scale@finite.S%3)
    assert np.array_equal(R@scale%3,scale@finite.R%3)
    for w in f.NWORDS+list(f.CUSP_WORDS.values()):
        assert np.array_equal(literal(w)%3,scale@finite.literal(w)%3)
    np.savez_compressed(HERE/"bc_fermat_class_two_integral_model.npz",S=S,R=R)
    result={"coordinates":"(v,Z), Z twice the BCH central coordinate",
            "all_action_matrices_integral":True,
            "literal_s_squared_r_cubed_exact_over_Z":True,
            "exact_mod3_coordinate_comparison_checked":True}
    (HERE/"bc_fermat_class_two_integral_model.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    print("PASS: exact integral odd-primary class-two action and doubled-log comparison.")
