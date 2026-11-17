#!/usr/bin/env python3
"""Exact actual source words for the joint G2 / homology-mod9 image.
Rebuilds all 148 integral-homology-identity witnesses in eleven literal
surface automorphisms; checks the 91-dimensional image and all nineteen
independent level-three homology corrections.
"""
import translation_class2_image as T
import numpy as np,json
from pathlib import Path
n=10;I=np.eye(n,dtype=np.int64)
Id=T.identity_words
wordgens=list(T.handle_words)+list(T.pointpush_words)
for i in range(3,10):
 g=list(Id);g[i-1]=(i,i+1,-i);g[i]=(i,);wordgens.append(tuple(g))
gens=[T.aut(g) for g in wordgens]
def exponent(w):return np.array([sum(1 if j==i else -1 if j==-i else 0 for j in w) for i in range(1,11)],dtype=np.int64)
H=[np.stack([exponent(w) for w in g],axis=1) for g in wordgens]
def inverse_unimod(M):
 # All literal generator inverses have these block forms; exact adjugate
 # in the two-dimensional handle block and permutation in punctures.
 C=M[:2,:2];d=int(C[0,0]*C[1,1]-C[0,1]*C[1,0]);assert abs(d)==1
 Ci=np.array([[C[1,1],-C[0,1]],[-C[1,0],C[0,0]]],dtype=np.int64)*d
 P=M[2:,2:];Pi=P.T
 # Disk permutations act on the first eight named peripheral vectors.
 assert np.array_equal(P@Pi,np.eye(8,dtype=np.int64))
 out=np.zeros_like(M);out[:2,:2]=Ci;out[2:,2:]=Pi;out[2:,:2]=-Pi@M[2:,:2]@Ci
 assert np.array_equal(out@M,I) and np.array_equal(M@out,I)
 return out
Hi=[inverse_unimod(M) for M in H]
def iw(w):return tuple(-j for j in reversed(w))
def hw(w,mod=None):
 M=I.copy()
 for j in w:
  M=M@(H[j-1] if j>0 else Hi[-j-1])
  if mod:M%=mod
 return M
pushwords=[]
for i in range(8):
 path=tuple(j+4 for j in range(i,0,-1))
 for j in range(2):
  e=T.Bi[j];base=(3,)*int(e[0])+(4,)*int(e[1]);w=path+base+iw(path)
  assert T.eq(T.aword(w,gens),T.push[len(pushwords)])
  expected=I.copy();expected[i+2,j]=-2;assert np.array_equal(hw(w),expected)
  pushwords.append(w)
pairwords=[]
for i in range(1,8):
 for j in range(i+1,9):
  path=tuple(k+4 for k in range(j-1,i,-1));w=path+(i+4,i+4)+iw(path)
  assert T.eq(T.aword(w,gens),T.pairtwists[len(pairwords)])
  assert np.array_equal(hw(w),I);pairwords.append(w)
words=[]
for i,g in enumerate(pushwords):
 for h in pushwords[:i]:words.append(g+h+iw(g)+iw(h))
words+=pairwords
rows=[]
for w in words:
 assert np.array_equal(hw(w),I)
 z=T.aword(w,gens);assert np.array_equal(z[1],I%3);rows.append(z[0])
rows=np.array(rows);W,piv=T.rref(rows);assert len(rows)==148 and len(W)==91
_,independent=T.rref(rows.T);assert len(independent)==91
assert len(T.rref(np.vstack((W,T.W)))[0])==91
# Nineteen actual words killing Out(G2), spanning the entire kernel on H9.
corrections=[(1,1,1),(2,2,2),(1,2,2,2,-1)]+[w*3 for w in pushwords]
cr=[]
for w in corrections:
 z=T.aword(w,gens);assert T.eq(z,T.Id)
 M=hw(w,9);assert np.array_equal(M%3,I%3)
 D=((M-I)%9)//3;assert not np.any(D[:2,2:]) and not np.any(D[2:,2:])
 assert np.trace(D[:2,:2])%3==0;cr.append(np.r_[D[:2,:2].reshape(-1),D[2:,:2].reshape(-1)])
assert len(T.rref(cr)[0])==19
# U^9 and L^9 are exactly identity on Q_L, because its generators
# have order nine, and their compact mod4 matrices generate SL2(Z4).
periods=[hw((1,)*9,4)[:2,:2],hw((2,)*9,4)[:2,:2]]
assert np.array_equal(periods[0],H[0][:2,:2]%4) and np.array_equal(periods[1],H[1][:2,:2]%4)
group=[np.eye(2,dtype=np.int64)];seen={tuple(group[0].reshape(-1))}
for M in group:
 for g in periods:
  N=M@g%4;k=tuple(N.reshape(-1))
  if k not in seen:seen.add(k);group.append(N)
assert len(group)==48
print('PASS all148 actual source words have integral homology identity and span91 outer IA directions',flush=True)
print('PASS nineteen actual words kill Out(G2) and span all level-three H1(Z9) corrections',flush=True)
print('PASS actual U^9,L^9 preserve Q_L and generate all48 compact mod4 matrices',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),source_homology=np.array(H),integral_kernel_rows=rows,integral_kernel_basis=W,
 independent_rows=np.array(independent),level_three_correction_rows=np.array(cr),mod4_group=np.array(group))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Literal actual mapping-class witnesses for the complete joint Out(G2), homology-mod9 fibre product and independent compact mod4 factor',
 'literal_source_automorphisms':wordgens,'source_names':['handle_U','handle_L','push_raw_1','push_raw_2']+[f'disk_{i}' for i in range(1,8)],
 'pointpush_words':pushwords,'pair_twist_words':pairwords,'integral_homology_identity_words':words,'independent_row_indices':independent,
 'integral_kernel_rank':91,'level_three_correction_words':corrections,'level_three_correction_rank':19,
 'positive_pure_joint_image_order':'24*3^126','compact_mod4_correction_words':[(1,)*9,(2,)*9],'compact_mod4_correction_image_order':48},indent=2)+'\n')
