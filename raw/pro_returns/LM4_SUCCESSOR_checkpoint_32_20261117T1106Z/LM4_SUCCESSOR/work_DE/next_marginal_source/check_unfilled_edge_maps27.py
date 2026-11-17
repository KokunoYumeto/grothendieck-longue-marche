#!/usr/bin/env python3
"""Literal marked branch calculation; no quotient or orbit enumeration."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'work_DE/next_marginal_source/annular_neck_reflection23.json'
data=json.loads(source.read_text())
eta={int(k):v for k,v in data['eta_adapted_K_basis_a_barb_d_e_f'].items()}
def red(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return out
def inv(w):return [-a for a in reversed(w)]
def mul(*w):return red([a for x in w for a in x])
def sub(w,d):return mul(*(d[abs(a)] if a>0 else inv(d[-a]) for a in w))
checks=[]
def check(n,x,y):
 assert x==y,(n,x,y)
 checks.append(n)
a,B,d,e,f=([i] for i in range(1,6))
ell=mul(a,f,inv(a))
P=mul(a,B,f,d,e,inv(d),inv(f),inv(d))
check('literal_eta_branch',eta[5],mul(P,inv(f),inv(P)))
w=mul(eta[1],P)
check('literal_w_in_old_K',w,mul(a,B,inv(a),f,d,e,inv(d),inv(f),inv(d)))
q=sub(ell,eta)
check('eta_ell_is_conjugate_f_inverse',q,mul(w,inv(f),inv(w)))
# New leaf basis a,d,e,V=f^-1 B f, f.  Indices a=1,d=2,e=3,V=4,f=5.
old_to_leaf={1:[1],2:[5,4,-5],3:[2],4:[3],5:[5]}
leaf_to_old={1:[1],2:[3],3:[4],4:[-5,2,5],5:[5]}
for i in range(1,6):
 check(f'basis_inverse_old_{i}',sub(old_to_leaf[i],leaf_to_old),[i])
 check(f'basis_inverse_leaf_{i}',sub(leaf_to_old[i],old_to_leaf),[i])
wl=sub(w,old_to_leaf)
check('alternating_actual_w',wl,[1,5,4,-5,-1,5,2,3,-2,-5,-2])
# B-blocks in H*_<k>(<k> x F(a,d,e,V)); H-blocks are f,+/-.
Bblocks=[[1],[4],[-1],[2,3,-2],[-2]]
assert all(red(v)==v and v for v in Bblocks)
check('all_leaf_blocks_nontrivial',len(Bblocks),5)
# Formal two-sheet conjugation identities, no regional rewriting assumed.
# a=1,C=2,k=3; C is an involution.
def orb(w):
 out=[]
 for z in w:
  if abs(z)==2:z=2
  if out and (out[-1]==-z or (z==2 and out[-1]==2)):out.pop()
  else:out.append(z)
 return out
def om(*ws):return orb([z for v in ws for z in v])
a1=[2,1,2];w0=om([1],inv(a1))
check('w0_C_equals_a_C_a_inverse',om(w0,[2]),[1,2,-1])
check('C_w0_inverse_equals_a_C_a_inverse',om([2],inv(w0)),[1,2,-1])
out={'status':'PASS','input':str(source.relative_to(ROOT)),'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'checks':checks,'ell':ell,'eta_ell':q,'P':P,'w_old_K':w,'w_leaf_basis':wl,'leaf_basis':['a','d','e','V=f^-1 B f','f'],'leaf_blocks':Bblocks,'scope':'Finite literal marking only. Uniform all-exponent amalgam normal-form and compact wreath arguments are proved in unfilled_edge_map_structure27.md.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(checks),'literal branch/basis/two-sheet identities; no finite target scan.')
print('w=a f V f^-1 a^-1 f(d e d^-1) f^-1 d^-1, all five displayed leaf blocks nontrivial.')
