"""Convert the rational compatible lift into actual finite group words.

All word descriptions use integer powers of generators, commutators, and
standard Lyndon weight-three commutators.  Collection is verified in the
free nilpotent Lie algebra of class3 by the exact BCH formula.  This
avoids any inference from rational membership to unproved integral
membership, and it includes the source-abelian correction directions.
"""
from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
import sympy as s
from nilpotent_derivations import *
HERE=Path(__file__).resolve().parent;start=time.time()

def bch(A,B):
 a,b,c=A;x,y,z=B
 comm=poly_bracket(a,x)
 return (add(a,x),add(b,y,scale(comm,Q(1,2))),
         add(c,z,scale(poly_bracket(a,y),Q(1,2)),scale(poly_bracket(b,x),Q(1,2)),
             scale(poly_bracket(a,comm),Q(1,12)),scale(poly_bracket(x,scale(comm,-1)),Q(1,12))))
def free_collect(n,linear,binary):
 xs=[{(i,):1} for i in range(n)]
 pairs=list(itertools.combinations(range(n),2))
 target1=add(*(scale(xs[i],a) for i,a in enumerate(linear)))
 target2=add(*(scale(poly_bracket(xs[i],xs[j]),a) for (i,j),a in zip(pairs,binary)))
 current=({}, {}, {})
 for i,a in enumerate(linear):
  if a:current=bch(current,(scale(xs[i],a),{},{}))
 residual=add(target2,scale(current[1],-1))
 exponents=[residual.get((i,j),0) for i,j in pairs]
 assert all(Q(x).denominator==1 for x in exponents)
 exponents=[int(x) for x in exponents]
 assert add(*(scale(poly_bracket(xs[i],xs[j]),a) for (i,j),a in zip(pairs,exponents)))==residual
 for (i,j),a in zip(pairs,exponents):
  if a:
   two=poly_bracket(xs[i],xs[j])
   three=scale(poly_bracket(add(xs[i],xs[j]),two),Q(1,2))
   current=bch(current,({},scale(two,a),scale(three,a)))
 assert current[0]==target1 and current[1]==target2
 residual=scale(current[2],-1);ternary=[]
 for w in lyndon_words(n,3):
  c=residual.get(w,0)
  assert Q(c).denominator==1,('nonintegral Hall coordinate',w,c)
  c=int(c)
  if c:
   p=lyndon_bracket(w,xs,poly_bracket)
   assert p[w]==1 and min(p)==w
   residual=add(residual,scale(p,-c))
   ternary.append((w,c))
 assert not residual
 check=add(current[2],*(scale(lyndon_bracket(w,xs,poly_bracket),c) for w,c in ternary))
 assert not check
 return {'generator_powers':[{'index':i+1,'exponent':int(a)} for i,a in enumerate(linear) if a],
  'commutator_powers':[{'indices':[i+1,j+1],'exponent':a} for (i,j),a in zip(pairs,exponents) if a],
  'standard_Lyndon_triple_powers':[{'indices':[i+1 for i in w],'exponent':c} for w,c in ternary]}

A=json.loads((HERE/'degree3_actual_correction_certificate.json').read_text())
R=json.loads((HERE/'degree3_rigid_obstruction_certificate.json').read_text())
assert R['outcome']=='COMPATIBLE_OVER_Q'
v=[s.Rational(x) for x in R['rational_correction_coefficients']]
nt=len(A['T_correction_names']);relation=s.zeros(91,1)
for name,c in zip(A['T_correction_names'],v[:nt]):
 if c:
  assert name[0]=='lower_relation','this exact solution uses no additional T ternary column'
  relation+=c*s.Matrix(A['lower_null_basis'][name[1]])
D=int(s.ilcm(*[x.q for x in list(relation)+v[nt:]]))
scaled=relation*D;assert all(x.q==1 for x in scaled)
integers=[int(x) for x in scaled]
lower=s.Matrix(A['lower_matrix']);assert lower*s.Matrix(integers)==s.zeros(lower.rows,1)
linear=[24*x for x in integers[:13]];binary=[24*x for x in integers[13:]]
word=free_collect(13,linear,binary)
print('PASS universal free-class3 BCH collection of the tetrahedral correction into integer powers',flush=True)
print('Integral common multiplier D:',D,flush=True)
print('T correction generator/commutator/triple factors:',*[len(word[k]) for k in word],flush=True)

# Check the image of the collected word by its universally proved logarithm.
U=s.Matrix(A['T_correction_matrix']);V=s.Matrix(A['I5_matrix'])
ut=U*s.Matrix(v[:nt])*D;vf=V*s.Matrix(v[nt:])*D
assert all(x.q==1 for x in ut) and all(x.q==1 for x in vf)
delta=s.Matrix(A['delta_coefficients']);assert ut+vf==D*delta
rows=R['source_projection_rows'];alpha=s.Matrix(R['projected_a_grade3'])
assert ut[rows,:]==D*alpha
free6=lyndon_words(6,3)
cyclic=[]
for w,x in zip(free6,v[nt:]):
 a=x*D;assert a.q==1
 if a:cyclic.append({'indices':list(w),'exponent':int(a)})
print('PASS exact990-coordinate common-image identity and70-coordinate rigid vanishing',flush=True)
print('Cyclic weight3 correction factors:',len(cyclic),flush=True)
print('Common class2 image is',2*D,'times the primitive vector w, hence nonzero.',flush=True)

# Universal interpretation of Lyndon triples, supplied explicitly.
def tree(w,shift=0):
 if len(w)==1:return int(w[0]+shift)
 for i in range(1,len(w)):
  v=w[i:]
  if all(v<v[j:]+v[:j] for j in range(1,len(v))):return ['commutator',tree(w[:i],shift),tree(v,shift)]
 raise AssertionError(w)
for row in word['standard_Lyndon_triple_powers']:
 row['word_tree']=tree(row['indices'])
for row in cyclic:row['word_tree']=tree(row['indices'])
out={'description':__doc__,'multiplier_D':D,'common_class2_coefficient':2*D,
 'commutator_convention':'[x,y]=xyx^-1y^-1; products in the displayed order',
 'T_generators':'e1,...,e13 in the certified geometric meridian basis; transported to the common base',
 'C5_generators':'f0,...,f5 at0,1,zeta,...,zeta^4, with the certified fan paths and common-base transport',
 'a_source_word':[1,-2,3,5,-3,2,-1,-5],
 'b0_commutator_factors':[{'indices':[i,j],'exponent':c} for i,j,c in [(0,1,-2),(0,2,-1),(0,3,-1),(0,4,-1),(0,5,-1),(1,2,1),(1,5,1)]],
 'combined_lower_relation_coefficients':integers,
 'T_correction_word_U':word,'C5_correction_word_V':cyclic,
 'common_lift_T':{'formula':'a^D U^-1','D':D},
 'common_lift_C5':{'formula':'b0^(2D) V','2D':2*D},
 'T_correction_grade3':[int(x) for x in ut],
 'C5_correction_grade3':[int(x) for x in vf],
 'rigid_projected_T_correction':[int(x) for x in ut[rows,:]],
 'scope':'These two actual finite words have equal nonzero images in P/gamma4P; their common image dies in all twelve rigid-seven class3 quotients. They do not coincide in P, since HT intersect H5=1. No element of the actual full-profinite K is constructed.'}
(HERE/'class3_common_lift_words.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL EXACT CHECKS PASS; elapsed',round(time.time()-start,2),'seconds',flush=True)
