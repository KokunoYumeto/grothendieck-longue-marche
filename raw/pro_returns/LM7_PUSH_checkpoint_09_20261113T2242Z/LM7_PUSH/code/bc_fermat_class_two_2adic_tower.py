#!/usr/bin/env python3
"""Complete two-adic conic fibres and an actual P8-to-P16 obstruction."""
from pathlib import Path
from collections import Counter
import json,math
import numpy as np
import sympy as sp
import bc_fermat_class_two_integral_model as q
from bc_fermat_class_two_integral_extension import hall_coordinates

HERE=Path(__file__).resolve().parent

def rational_mod(a,m):
    a=sp.Rational(a);assert math.gcd(int(a.q),m)==1
    return int(a.p)*pow(int(a.q),-1,m)%m

def conic(u,v):return v+3*(u*u+u*v+v*v)

def main():
    old=np.load(HERE/"bc_fermat_class_two_3adic_norms.npz")
    B=old["abelian_norm_basis"];U=old["smith_left"]
    t1,t2,t3,u,v,w=sp.symbols("t1 t2 t3 u v w")
    F=t3-t2+3*(t1*t1+t2*t2+t3*t3+t1*t2+t1*t3-t2*t3)
    assert sp.expand(F.subs({t1:u-w,t2:w,t3:v+w})-conic(u,v))==0
    mon=sp.Matrix([t1*t1,t2*t2,t3*t3,t1*t2,t1*t3,t2*t3])
    errors=sp.Matrix(old["transformed_error_linear"])*sp.Matrix([t1,t2,t3])+sp.Matrix(old["transformed_error_quadratic"])*mon
    multiples=[]
    for i in range(37,90):
        quotient,remainder=sp.div(errors[i],F,t3,t2,t1)
        assert remainder==0 and not quotient.free_symbols
        assert int(quotient)%2==0
        multiples.append(int(quotient)//2)
    assert math.gcd(*multiples)==1 and multiples[63-37]==1
    source=json.loads((HERE/"bc_fermat_class_two_integral_family.json").read_text())["records"]
    residues=sorted({tuple(row["norm_torus_residue_mod4"]) for row in source})
    assert residues==[(0,0),(0,1),(2,0),(2,3),(3,1),(3,3)]
    for u0,v0 in residues:
        assert conic(u0,v0)%4==0
        assert ((1+3*(u0+2*v0))%2 if u0%2==0 else (3*(2*u0+v0))%2)==1
    counts=[]
    for n in range(2,9):
        modulus=2**n;central_modulus=2**(n-1)
        per_residue=[]
        for u0,v0 in residues:
            finite=0;liftable=0
            for a in range(u0,modulus,4):
                for b in range(v0,modulus,4):
                    value=conic(a,b)
                    finite+=value%central_modulus==0
                    liftable+=value%modulus==0
            finite*=modulus;liftable*=modulus # independent w-coordinate
            expected_finite=4 if n==2 else 2**(2*n-1)
            assert finite==expected_finite
            assert liftable==2**(2*n-2)
            per_residue.append([finite,liftable])
        central=2**(8*(n-1))
        counts.append({"n":n,"abelian_norm_values_per_source":per_residue[0][0],
            "abelian_values_lifting_to_every_level":per_residue[0][1],
            "central_correction_images_per_value":central,
            "finite_correction_images_per_source":per_residue[0][0]*central,
            "images_lifting_to_next_and_every_level":per_residue[0][1]*central})
    # The complete P8 test covers every source class and all abelian
    # residues relevant to the only remaining source congruence mod4.
    finite=json.loads((HERE/"bc_fermat_class_two_2adic_fibres.json").read_text())
    assert finite["source_points_with_lifts"]==432
    assert finite["passing_abelian_count_distribution"]=={"32":432}
    assert finite["complete_obstruction_value_count"]==1
    # Literal finite nonlifting shadow over E24 row0, parameters(0,0;0).
    data=np.load(HERE/"bc_fermat_class_two_2adic_source.npz")
    f=np.load(HERE/"bc_fermat_class_two_integral_family.npz")["source_word_logs"][0]
    K=data["integral_abelian_image"];generators=data["integral_K_basis_logs"]
    C=data["central_kernel_lattice"]
    words=np.load(HERE/"bc_fermat_class_two_2adic_words.npz")
    W=words["central_word_matrix"]
    comparison=sp.Matrix(words["comparison_to_integral_lattice"])
    hom=np.array(json.loads((HERE/"bc_cm_fermat_kernel_words.json").read_text())[
        "homogeneous_norm_kernel_basis"],dtype=np.int64)
    previous=json.loads((HERE/"bc_cm_fermat_kernel_boundary.json").read_text())["records"][0]
    delta=np.array([int(sp.Rational(x)) for x in previous["rational_boundary_correction"]],dtype=np.int64)
    target_v=f[:10]+delta+hom[:,0]
    target_residue=np.array([0,0,4,0,4,4,4,4,0,0],dtype=np.int64)
    assert np.array_equal(target_v%8,target_residue)
    rows=[0,1,3,4,5,7,8,9]
    coefficients=sp.Matrix(K[rows]).inv()*sp.Matrix((target_v-f[:10])[rows])
    assert all(a.q==1 for a in coefficients)
    c=np.array(coefficients,dtype=np.int64).reshape(8)
    lifted=f.copy()
    for a,g in zip(c,generators.T):lifted=q.multiply(lifted,int(a)*g)
    assert np.array_equal(lifted[:10],target_v)
    central_rows=np.r_[np.arange(10,55),np.arange(65,110)]
    norm=q.norm_errors(lifted)
    assert not np.any(norm[central_rows]%2)
    rhs=norm[central_rows]//2
    detector=np.load(HERE/"bc_fermat_class_two_2adic_norms.npz")["source_membership_detector"]
    numerator=detector@rhs;assert not np.any(numerator%4)
    source_central=3*(numerator//4)%4
    word_central=np.array([rational_mod(a,4) for a in comparison.inv()*sp.Matrix(source_central)],dtype=np.int64)
    assert np.array_equal(W@word_central%4,C@source_central%4)
    # Ninth powers kill all ternary source coordinates and retain the
    # literal exponent-eight image.  All these words are in the binary
    # source kernel already.
    actual=f%8
    for a,g in zip(c%8,generators.T):actual=q.multiply(actual,9*int(a)*g)%8
    actual=q.multiply(actual,np.r_[np.zeros(10,dtype=np.int64),18*(W@word_central)])%8
    assert not np.any(q.norm_errors(actual)%8)
    hall=hall_coordinates(actual)
    assert np.array_equal(hall[:10]%8,target_residue)
    assert conic(0,4)%8==4
    central_support=[{"indices":[int(i)+1,int(j)+1],"Hall_coefficient_mod4":int(a)}
        for i,j,a in zip(q.I,q.J,hall[10:]%4) if a]
    # A direct finite-precision Hensel graph in each of the six source
    # residue disks.  The chosen derivative is always a unit.
    hensel_examples=[]
    for u0,v0 in residues:
        alpha=7;ww=11
        a,b=(u0+4*alpha,v0) if u0%2==0 else (u0,v0+4*alpha)
        power=4
        for _ in range(2,12):
            assert conic(a,b)%power==0
            bit=(-conic(a,b)//power)%2
            if u0%2==0:b+=power*bit
            else:a+=power*bit
            power*=2
        assert conic(a,b)%power==0
        hensel_examples.append({"source_residue":[u0,v0],"u_v_mod4096":[a%4096,b%4096],
                               "t_mod4096":[(a-ww)%4096,ww,(b+ww)%4096]})
    result={"complete_two_adic_obstruction":"F=v+3(u^2+u*v+v^2)=0",
        "source_residue_pairs_mod4":[list(x) for x in residues],
        "source_residue_counts":{str(k):v for k,v in Counter(tuple(row["norm_torus_residue_mod4"]) for row in source).items()},
        "exact_source_parametrization":"If u0 is even: u=u0+4a and solve uniquely for v=v0 mod4. If u0 is odd: v=v0+4a and solve uniquely for u=u0 mod4. In both cases w is free and (t1,t2,t3)=(u-w,w,v+w).",
        "complete_central_source_condition":"Automatic on these actual source affine lattices, by the complete P8 image check and the mod4 detector.",
        "infinite_fibre":"Z2^10: the conic-disk parameter, w, and the eight primitive central norm-kernel coordinates.",
        "finite_counts":counts,
        "finite_lifting_criterion":"For n>=2, a finite norm image lifts to the next and every level exactly when F=0 mod2^n. At n=2 this holds for every image; at every n>=3 it selects exactly one half.",
        "nonlifting_point":{"source_index":0,"source_metadata":source[0],
            "target_abelianization_mod8":target_residue.tolist(),
            "target_Hall_central_support":central_support,
            "K_basis_word_exponents_before_ninth_powers_mod8":(c%8).tolist(),
            "central_basis_word_exponents_before_ninth_powers_mod4":word_central.tolist(),
            "word_rule":"Multiply the retained source word by the ordered ninth powers of the eight K-basis words, then by the ordered ninth powers of the forty-five actual zero-H-abelian central words, using the saved exponents.",
            "exact_P16_obstruction":"Every lift keeps (u,v)=(0,4) mod8, so F=4 mod8; the zero-Smith Hall norm row requires F=0 mod8 at P16."},
        "hensel_examples":hensel_examples,
        "all_integral_polynomial_finite_source_and_actual_word_checks_passed":True}
    (HERE/"bc_fermat_class_two_2adic_tower.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_2adic_tower.npz",nonlifting_Hall_target=np.r_[hall[:10]%8,hall[10:]%4],
        nonlifting_K_word_exponents=c%8,nonlifting_central_word_exponents=word_central)
    print("Source conic residue counts:",result["source_residue_counts"])
    print("Complete finite counts:",json.dumps(counts))
    print("Nonlifting P8 target:",np.r_[hall[:10]%8,hall[10:]%4].tolist())
    print("PASS: complete two-adic fibres, every finite lifting image, and an actual P8-to-P16 obstruction.")

if __name__=="__main__":main()
