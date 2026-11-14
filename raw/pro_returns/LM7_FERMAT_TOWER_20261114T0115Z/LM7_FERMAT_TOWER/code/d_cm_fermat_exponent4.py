#!/usr/bin/env python3
"""The actual exponent-four refinement retaining the D33 G6 conjugators."""
from pathlib import Path
import json,time
import numpy as np
import d_cm_fermat_mixed_compatible as c

started=time.time();OUT=Path(__file__).resolve().parent
g=c.g;m=c.m;n=c.n;size=c.size;C=c.C;nc=c.nc
F0=c.Fbase;E=c.E[nc];z=np.concatenate([c.b2,c.a2])
rng=np.random.default_rng(37123326);attempts=[]
dual=np.array(m.allrecords[0]['dual_coinvariant_rows'],dtype=np.int16)
assert not np.any(dual@F0%2)
for trial in range(1,129):
 if trial>1:z=c.solver(rng)
 err=E+F0@z;assert not np.any(err%2)
 rhs=-(err//2)%2;ob=(dual@rhs%2).tolist()
 if any(ob):attempts.append({'trial':trial,'upper_obstruction':ob});continue
 b2,a2=z[:n],z[n:]
 T2=g.kernel_matrix((c.edge0+C@(a2-b2))%2,2);rk=g.rank2(T2)
 attempts.append({'trial':trial,'upper_obstruction':ob,'kernel_rank':rk})
 if rk!=n:continue
 upper_solver,upper_rank,upper_dim=g.affine2(F0%2,rhs)
 upper=upper_solver(rng);assert not np.any((F0@upper-rhs)%2)
 z4=(z+2*upper)%4
 assert not np.any((E+F0@z4)%4)
 break
else:raise AssertionError('No compatible generating exponent-four lift found.')
b4,a4=z4[:n],z4[n:]
a12=(9*a4+4*c.a3)%12;b12=(9*b4+4*c.b3)%12
PA12=c.PA+C@a12;PB12=c.PB+C@b12
defect=PB12-m.act(PB12,c.ss)+m.act(PA12-m.act(PA12,c.rr)+m.act(m.path(m.hr),c.A),c.ss)-m.Pt
assert not np.any(defect%12)
assert not np.any((c.projection(PA12)-c.targetA2)%2)
assert not np.any((c.projection(PB12)-c.targetB2)%2)
assert not np.any(c.projection(PA12)%3)
assert not np.any((c.projection(PB12)-c.targetB3)%3)

def correction_word(coeff):
 w=[]
 for v,bw in zip(coeff,g.basiswords):
  v=int(v)
  if v>6:v-=12
  block=bw if v>=0 else g.inverse_word(bw)
  for j in range(abs(v)):w.extend(block)
 return w
Aw=correction_word(a12)+g.base_word(c.A)
Bw=correction_word(b12)+g.base_word(c.beta)
cusp=Bw+[0]+g.inverse_word(Bw)+Aw+[1]+g.inverse_word(Aw)+[2,0]
q,P=g.model(cusp);assert q==0 and not np.any(P%12)
gen=[g.model(Bw+[0]+g.inverse_word(Bw)),g.model(Aw+[1]+g.inverse_word(Aw))]
assert [q for q,P in gen]==[c.ss,c.rr]
gen.append((int(m.inverse[c.rr]),-m.act(gen[1][1],int(m.inverse[c.rr]))))
check=np.zeros((n,n),dtype=np.int16)
for j,w in enumerate(g.basiswords):
 q=0;P=np.zeros(size,dtype=np.int32)
 for letter in w:
  h,v=gen[letter];P+=m.act(v,q);q=m.mul(q,h)
 assert q==0;check[:,j]=P[nc]%12
T4=g.kernel_matrix((c.edge0+C@(a4-b4))%4,4)
assert np.array_equal(check%4,T4) and np.array_equal(check%3,c.T3)
assert g.rank2(T4)==n
P24=g.P24
assert np.any(P24%2) and np.any(P24%3)

# Exact affine abelianization gives the integral Ihara commutator gauge.
LS=np.array([[0,1],[1,0]],dtype=object)
LR=np.array([[0,-1],[1,-1]],dtype=object)
def affine(word):
 M=np.eye(2,dtype=object);v=np.zeros(2,dtype=object)
 for a in word:
  if a==0:M=M@LS
  elif a==1:v+=M@np.array([1,0],dtype=object);M=M@LR
  else:v+=M@np.array([1,1],dtype=object);M=M@(LR@LR)
 return M,np.array(v,dtype=np.int64)
M,bab=affine(Bw);assert np.array_equal(M,np.eye(2,dtype=object))
k=int(bab[1]-bab[0]);xword=[2,0,2,0]
Bprime=(xword*k if k>=0 else g.inverse_word(xword)*(-k))+Bw
fword=[0]+Bprime+[0]+g.inverse_word(Bprime)
Mf,fab=affine(fword)
assert np.array_equal(Mf,np.eye(2,dtype=object)) and not np.any(fab)

def mm(a,b):return m.mul(a[0],b[0]),(a[1]+m.act(b[1],a[0]))%12
def ii(a):
 h=int(m.inverse[a[0]]);return h,-m.act(a[1],h)%12
def eq(a,b):return a[0]==b[0] and not np.any((a[1]-b[1])%12)
S=(m.hs,np.zeros(size,dtype=np.int32));R=(m.hr,m.path(m.hr));U=ii(mm(S,R))
V=mm(mm(S,U),S);FF=g.model(fword);FF=(FF[0],FF[1]%12)
assert eq(mm(mm(mm(U,ii(FF)),V),FF),mm(ii(FF),mm(U,V)))
assert eq(mm(mm(mm(ii(FF),V),FF),U),mm(mm(V,U),FF))
assert eq(mm(FF,mm(mm(S,FF),S)),(0,np.zeros(size,dtype=np.int16)))

summary={'base_order':size,'free_kernel_rank':n,'quotient_order':'6912 * 12^1153',
 'cusp_order':288,'GT_shadow_Nord':144,'multiplier':1,
 'A_H':c.A,'beta_H':c.beta,'extra_CM_coset':True,
 'exact_D33_G6_conjugators_retained_before_common_Ihara_gauge':True,
 'exponent4_attempts':attempts,'retains_previous_J6_action':trial==1,
 'upper_correction_rank':upper_rank,'upper_affine_dimension':upper_dim,
 'kernel_generation_ranks':{'2':n,'3':n},
 'literal_cusp_word_length':len(cusp),'all_6912_edge_coordinates_checked':True,
 'all_1153_basis_images_checked':True,
 'beta_integral_F_abelianization':bab.tolist(),'Ihara_gauge_exponent':k,
 'gauged_f_abelianization':fab.tolist(),'both_m0_hexagons_checked':True,
 'scope':'Actual exponent12 mixed Fermat/congruence shadow; no full profinite lift or agreement beyond G6 is inferred.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'a_mod12':a12.tolist(),'beta_correction_mod12':b12.tolist(),
 'A_word':Aw,'beta_word':Bw}
(OUT/'d_cm_fermat_exponent4.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
