"""Exact completeness check for the missing other-family inner operators.

This proves only integral affine-index saturation, not orbit transitivity or source equality.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
P=Path(__file__).resolve().parent
e=json.loads((P/'tangent_even_family_actions.json').read_text())
o=json.loads((P/'tangent_partial_source_words.json').read_text())
qwords={int(j):tuple(x-4 if x>0 else x+4 for x in w if abs(x)>4) for j,w in o['other_family_V_in_ordered_basis'].items()}
def ab(w):
 a=[0]*9
 for x in w:a[abs(x)-1]+=1 if x>0 else -1
 return s.Matrix(a)
opp={j:ab(w) for j,w in qwords.items()}
for pos,j in enumerate([1,2,4,6]):assert opp[j]==s.eye(9)[:,pos]
print('Actual four opposite-family source words have the four complementary-meridian H1 vectors: PASS')
rows={}
for j in [1,2,4,6]:
 i=[1,2,4,6].index(j);partner=i^1
 # This primitive pair spans the full annihilator of the rank7 lattice.
 c=s.zeros(2,9);c[0,partner]=1;c[0,5]=2
 c[1,i]=-1;c[1,partner]=1;c[1,5]=1;c[1,6]=1;c[1,8]=1
 L=s.Matrix(e['affine_H1_shift_lattices'][str(j)]['basis'])
 assert c*L==s.zeros(2,7)
 assert abs(c[:,[i,partner]].det())==1
 # L is primitive rank7 and lies in ker(c), so the two lattices agree.
 assert hermite_normal_form(L)==L and e['affine_H1_shift_lattices'][str(j)]['Smith']==[1]*7
 values=s.Matrix.hstack(*(c*opp[k] for k in [1,2,4,6]))
 complete=hermite_normal_form(s.Matrix.hstack(L,*opp.values()))
 assert complete==s.eye(9)
 print('label',j,'primitive annihilators',c.tolist(),'values on O1,O2,O4,O6',values.tolist(),'completed lattice Z^9: PASS')
 rows[j]={'primitive_annihilator_rows':c.tolist(),'values_on_opposite_words':values.tolist(),'completed_Hermite_basis':complete.tolist(),'separating_pair_of_opposite_indices':[i,partner]}
out={'description':__doc__,'opposite_quotient_words':qwords,'opposite_H1_vectors':{j:v.tolist() for j,v in opp.items()},'selected_label_checks':rows,'scope':'The exact other-family inner source operators fill both missing directions integrally. No remaining affine-index character from this test survives. This does not prove a transitive full free-group index action, normality, or I=R.'}
(P/'tangent_even_source_lattice_completion.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
