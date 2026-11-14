#!/usr/bin/env python3
"""Exact central norm Smith map on the full binary source lattice."""
from pathlib import Path
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from de_ferrari_two_core import Span2
from bc_fermat_class_two_integral_extension import hall_coordinates

HERE=Path(__file__).resolve().parent
source=np.load(HERE/"bc_fermat_class_two_2adic_source.npz")
central=source["central_kernel_lattice"]
old=np.load(HERE/"bc_fermat_class_two_3adic_norms.npz")
norm=old["central_norm"]
M=norm@central
S=smith_normal_form(sp.Matrix(M),domain=ZZ)
factors=[abs(int(S[i,i])) for i in range(45)]
assert factors==[1]*31+[2]*4+[12]*2+[0]*8
hom=sp.Matrix(old["smith_right"][:,37:])
inverse=sp.Matrix(central).inv()
source_hom=inverse*hom
assert all(a.q==1 for a in source_hom)
assert sp.Matrix(M)*source_hom==sp.zeros(90,8)
homsmith=smith_normal_form(hom,domain=ZZ)
hf=[abs(int(homsmith[i,i])) for i in range(8)]
assert all(a%2 for a in hf)
domain=smith_normal_form(sp.Matrix(central),domain=ZZ)
df=[abs(int(domain[i,i])) for i in range(45)]
assert df==[1]*39+[2]*4+[4]*2
# Use the already verified small integral decomposition of the ambient
# norm map.  Its only nonunit denominator is3, a two-adic unit.
ambient_V=sp.Matrix(old["smith_right"])
ambient_U=sp.Matrix(old["smith_left"])
ambient_S=sp.Matrix(old["smith"])
particular3=-3*ambient_V[:,:37]*sp.diag(*[
    1/ambient_S[i,i] for i in range(37)])*ambient_U[:37,:]
assert all(a.q==1 for a in particular3)
detector=4*inverse*particular3
assert all(a.q==1 for a in detector)
assert all(int(a)%4==0 for a in detector*sp.Matrix(M))
assert all(a.q==1 for a in 4*inverse)
span=Span2(45)
for column in central.T:span.add(column%2,None)
assert len(span.basis)==39
generators=source["integral_K_basis_logs"]
for i in (0,1):
    g=hall_coordinates(generators[:,i])
    expected=np.zeros(10,dtype=np.int64);expected[i]=12
    assert np.array_equal(g[:10],expected)
    span.coordinates(g[10:]%2)
out={"source_central_lattice_smith":df,
     "source_central_norm_smith":factors,
     "integral_norm_kernel_embedding_smith":hf,
     "norm_kernel_rank":8,
     "finite_homogeneous_correction_images_at_central_modulus_2^m":"2^(8m), for every m>=0",
     "every_finite_homogeneous_correction_image_lifts_compatibly":True,
     "finite_abelian_ambiguities_absorbed":"The first two K-basis words have abelian values12e1,12e2 and central values in C+2Z^45. Their2^(n-2) powers account for all K coefficient ambiguities modulo2^n and lie in C modulo2^(n-1).",
     "complete_source_congruence":"On the saturated ambient norm image, h is in MC Z2^45 exactly when detector*h=0 mod4.",
     "detector_formula":"detector=4*C^(-1)*particular3, where particular3*h is three times an ambient solution of M*z+h=0.",
     "ambient_kernel_contained_in_source_lattice_integrally":True,
     "exact_integer_Smith_factors_and_coordinate_maps_verified":True}
(HERE/"bc_fermat_class_two_2adic_norms.json").write_text(json.dumps(out,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_2adic_norms.npz",
    norm=M,smith=np.array(S,dtype=np.int64),
    ambient_particular_times3=np.array(particular3,dtype=np.int64),
    source_membership_detector=np.array(detector,dtype=np.int64),
    homogeneous_central_basis=np.array(hom,dtype=np.int64),
    homogeneous_source_coefficients=np.array(source_hom,dtype=np.int64))
print(json.dumps(out,indent=2))
print("PASS: complete binary central norm, exact finite-image comparison, and integral kernel.")
