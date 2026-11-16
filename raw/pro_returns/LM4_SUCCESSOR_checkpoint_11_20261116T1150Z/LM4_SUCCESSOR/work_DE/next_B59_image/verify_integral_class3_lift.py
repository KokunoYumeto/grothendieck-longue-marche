"""Independently evaluate the displayed integer correction words.

This reads the collected generator/commutator/triple exponents and
evaluates their actual common-base Artin logarithms, instead of trusting
the free BCH collection target or a rational-span assertion.
"""
from pathlib import Path
import json,itertools,time
import sympy as s
from nilpotent_derivations import *
from magnus4 import product_log_parts4
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;start=time.time()
words=json.loads((HERE/'class3_common_lift_words.json').read_text())
logs=json.loads((HERE/'T_generator_log3.json').read_text())
upper=json.loads((HERE/'degree3_upper_obstruction_certificate.json').read_text())
T={r['index']:(decode_derivation(r['D1']),decode_derivation(r['twiceD2']),decode_derivation(r['24D3'])) for r in logs['generators']}
F={int(i):(decode_derivation(r['D1']),decode_derivation(r['twiceD2'])) for i,r in upper['generator_log_parts']['C5'].items()}
n=11;basis=grade3_basis(n);D=words['multiplier_D']
U=words['T_correction_word_U']
parts=[]
for row in U['generator_powers']:
 parts.append(tuple(deriv_scale(v,row['exponent']) for v in T[row['index']]))
one,two,three=product_log_parts4(parts)
assert not any(one)
for row in U['commutator_powers']:
 i,j=row['indices'];c=row['exponent']
 x,y=commutator_parts(T[i][:2],T[j][:2])
 two=deriv_add(two,deriv_scale(x,2*c))
 three=deriv_add(three,deriv_scale(y,12*c))
assert not any(two)
print('PASS actual evaluation of13 generator powers and78 commutator powers; layers1,2 vanish',flush=True)

# Use the exact rank-six H1 factorization to evaluate all728 triple powers.
h=json.loads((BASE/'full_pair_linking_certificate.json').read_text())
M=s.Matrix(h['full_matrix_rows_pairs_columns_basis']);_,cols=M.rref();cols=list(cols)
_,rows=M[:,cols].T.rref();rows=list(rows)
C=M[rows,cols].inv()*M[rows,:];assert M[:,cols]*C==M
linear=[{(i,):C[i,j] for i in range(6) if C[i,j]} for j in range(13)]
poly={}
for row in U['standard_Lyndon_triple_powers']:
 w=tuple(i-1 for i in row['indices'])
 poly=add(poly,scale(lyndon_bracket(w,linear,poly_bracket),row['exponent']))
q=[T[i+1][0] for i in cols]
for w in lyndon_words(6,3):
 c=poly.get(w,0)
 if c:
  p=lyndon_bracket(w,[{(i,):1} for i in range(6)],poly_bracket)
  poly=add(poly,scale(p,-c))
  three=deriv_add(three,deriv_scale(lyndon_bracket(w,q,bracket),24*c))
assert not poly and all(s.Rational(c).q==1 and int(c)%24==0 for p in three for c in p.values())
Uder=[{w:int(c)//24 for w,c in p.items()} for p in three]
Uvec=extract_grade3(Uder,n,basis,reconstruct=True)
assert Uvec==words['T_correction_grade3']
print('PASS all728 actual T triple powers; exact990-coordinate U image matches the certificate',flush=True)

Vder=deriv_zero(n)
f=[F[i][0] for i in range(6)]
for row in words['C5_correction_word_V']:
 Vder=deriv_add(Vder,deriv_scale(lyndon_bracket(tuple(row['indices']),f,bracket),row['exponent']))
Vvec=extract_grade3(Vder,n,basis,reconstruct=True)
assert Vvec==words['C5_correction_grade3']
print('PASS39 actual cyclic triple powers and full graded reconstruction',flush=True)

negative=lambda x:(deriv_scale(x[0],-1),deriv_scale(x[1],-1))
t=product_log_parts([T[1][:2],negative(T[2][:2]),T[3][:2]])
a2,a3two=commutator_parts(t,T[5][:2])
b2=deriv_zero(n);b3two=deriv_zero(n)
for row in words['b0_commutator_factors']:
 i,j=row['indices'];c=row['exponent'];x,y=commutator_parts(F[i],F[j])
 b2=deriv_add(b2,deriv_scale(x,c));b3two=deriv_add(b3two,deriv_scale(y,c))
A2=deriv_scale(a2,D);B2=deriv_scale(b2,2*D)
A3twice=deriv_add(deriv_scale(a3two,D),deriv_scale(Uder,-2))
B3twice=deriv_add(deriv_scale(b3two,2*D),deriv_scale(Vder,2))
assert A2==B2 and A3twice==B3twice and any(A2)
rig=json.loads((HERE/'degree3_rigid_obstruction_certificate.json').read_text())
assert [Uvec[i] for i in rig['source_projection_rows']]==[D*x for x in rig['projected_a_grade3']]
print('PASS independently evaluated actual words a^D U^-1 and b0^(2D)V agree through class3',flush=True)
print('PASS their common class2 image is nonzero; their rigid class3 image is zero',flush=True)
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
