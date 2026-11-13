#!/usr/bin/env python3
"""Actual J48 seed for the full homology tower, with the exact odd lifts."""
from pathlib import Path
import hashlib,json,time
import numpy as np
import d_cm_fermat_homology_lift as J

OUT=Path(__file__).resolve().parent;started=time.time();MOD=48
for name in ('D','R','V','OLD','C','nc','d','size','A','beta','PA','PB',
             'Pr','Pt','hs','hr','ht','ss','rr','mul','inverse','act',
             'projectionQ','projection4','kernel_matrix','rank2'):
 globals()[name]=getattr(J,name)
basiswords=json.loads((OLD/'d_cm_fermat_mixed_generate.json').read_text())['basis_words']
rs=np.array(D['right_s'],dtype=np.int32)
rtrans=np.array(D['right_r'],dtype=np.int32);rtrans2=rtrans[rtrans]
def invword(w):return [0 if a==0 else 3-a for a in reversed(w)]
def base_word(h):
 out=[]
 while h:h,a=D['parent'][h];out.append(a)
 return list(reversed(out))
def model(w):
 h=0;P=np.zeros(size,dtype=np.int32)
 for a in w:
  if a==0:h=int(rs[h])
  else:
   k=int(rtrans[h] if a==1 else rtrans2[h]);P[h]+=1;P[k]-=1;h=k
 return h,P

# The selected finite base action is precisely inner conjugation by x^6.
xword=[2,0,2,0];x6word=xword*6
hx6,Px6=model(x6word);assert hx6==A
assert all(J.alpha[h]==mul(mul(hx6,h),int(inverse[hx6])) for h in range(size))
hc=mul(int(inverse[hx6]),beta)
assert mul(hc,hs)==mul(hs,hc)
csword=base_word(hc);cc,Pc=model(csword);assert cc==hc
delta=Pc-act(Pc,hs)
assert np.array_equal(C@delta[nc],delta)
assert np.array_equal(act(delta,hs),-delta)

# Averaging is integral at every odd prime.  This is one rational formula
# with denominator2, hence supplies all odd components simultaneously.
# The stored arrays are twice their exact path/coordinate values.
PAodd2=2*Px6
PBodd2=2*Px6+act(Pc+act(Pc,hs),hx6)
aodd2=(PAodd2-2*PA)[nc];bodd2=(PBodd2-2*PB)[nc]
assert np.array_equal(C@aodd2,PAodd2-2*PA)
assert np.array_equal(C@bodd2,PBodd2-2*PB)
assert np.array_equal(PBodd2-act(PBodd2,ss),
                      2*(Px6-act(Px6,ss)))
assert np.array_equal(PAodd2-act(PAodd2,rr)+2*act(Pr,A),
                      2*(Px6-act(Px6,rr)+act(Pr,hx6)))
odd_cusp=PBodd2-act(PBodd2,ss)+act(
 PAodd2-act(PAodd2,rr)+2*act(Pr,A),ss)-2*Pt
assert not np.any(odd_cusp)

# The integral two-adic solution retains the recorded seed modulo16.
# CRT with the actual odd formula gives one literal J48 representative.
a16=J.a%16;b16=J.b%16
a3=2*aodd2%3;b3=2*bodd2%3
a48=(33*a16+16*a3)%48;b48=(33*b16+16*b3)%48
PA48=PA+C@a48;PB48=PB+C@b48
defect=PB48-act(PB48,ss)+act(PA48-act(PA48,rr)+act(Pr,A),ss)-Pt
assert not np.any(defect%48)
def correction_word(coeff):
 out=[]
 for v,w in zip(coeff,basiswords):
  v=int(v)
  if v>MOD//2:v-=MOD
  block=w if v>=0 else invword(w)
  for _ in range(abs(v)):out.extend(block)
 return out
Aw=correction_word(a48)+base_word(A)
Bw=correction_word(b48)+base_word(beta)
cusp=Bw+[0]+invword(Bw)+Aw+[1]+invword(Aw)+[2,0]
q,P=model(cusp);assert q==0 and not np.any(P%MOD)
print('Full J48 cusp word:',len(cusp),'letters; every coordinate zero.',flush=True)

# Independent generator substitution checks every kernel basis image.
gens=[model(Bw+[0]+invword(Bw)),model(Aw+[1]+invword(Aw))]
assert [q for q,p in gens]==[ss,rr]
gens.append((int(inverse[rr]),-act(gens[1][1],int(inverse[rr]))))
check=np.zeros((d,d),dtype=np.int16)
for j,w in enumerate(basiswords):
 q=0;P=np.zeros(size,dtype=np.int32)
 for a in w:
  h,v=gens[a];P+=act(v,q);q=mul(q,h)
 assert q==0;check[:,j]=P[nc]%MOD
edge0=PA-PB;edge0[A]+=1
T16=kernel_matrix((edge0+C@(a48-b48))%16,16)
assert np.array_equal(check%16,T16)
assert rank2(T16)==d
Todd=act(C,hx6)[nc]%3
assert np.array_equal(check%3,Todd)
assert np.array_equal(Todd@(act(C,int(inverse[hx6]))[nc]%3)%3,np.eye(d,dtype=np.int16))

def affine(w):
 M=np.eye(2,dtype=np.int64);v=np.zeros(2,dtype=np.int64)
 LS=np.array([[0,1],[1,0]],dtype=np.int64)
 LR=np.array([[0,-1],[1,-1]],dtype=np.int64)
 for a in w:
  if a==0:M=M@LS
  elif a==1:v+=M[:,0];M=M@LR
  else:v+=M[:,0]+M[:,1];M=M@(LR@LR)
 return M,v
Ic,cab=affine(csword);assert np.array_equal(Ic,np.eye(2,dtype=np.int64))
odd_beta_ab2=[12+int(sum(cab)),int(sum(cab))]
assert odd_beta_ab2[1]-odd_beta_ab2[0]==-12
Ib,bab=affine(Bw);assert np.array_equal(Ib,np.eye(2,dtype=np.int64))
k=int(bab[1]-bab[0])
assert k%6==0 and (k+6)%9==0

def mm(a,b):return mul(a[0],b[0]),(a[1]+act(b[1],a[0]))%MOD
def ii(a):
 h=int(inverse[a[0]]);return h,-act(a[1],h)%MOD
def conj(a,b):return mm(mm(a,b),ii(a))
def eq(a,b):return a[0]==b[0] and not np.any((a[1]-b[1])%MOD)
identity=(0,np.zeros(size,dtype=np.int32))
def power(a,n):
 out=identity
 while n:
  if n&1:out=mm(out,a)
  a=mm(a,a);n//=2
 return out
X=model(xword);S=(hs,np.zeros(size,dtype=np.int32));RR=(hr,Pr)
assert eq(power(X,576),identity)
assert not eq(power(X,288),identity) and not eq(power(X,192),identity)
assert not eq(power(X,144),identity)
Xk=power(X,k%576)
newA=(A,PA48%MOD);newB=(beta,PB48%MOD)
newBp=mm(Xk,newB);FF=mm(mm(mm(S,newBp),S),ii(newBp))
U=ii(mm(S,RR));VV=mm(mm(S,U),S)
assert eq(mm(mm(mm(U,ii(FF)),VV),FF),mm(ii(FF),mm(U,VV)))
assert eq(mm(mm(mm(ii(FF),VV),FF),U),mm(mm(VV,U),FF))
assert eq(mm(FF,conj(S,FF)),identity)
newS=conj(Xk,conj(newB,S));newR=conj(Xk,conj(newA,RR))
assert newS[0]==hs and newR[0]==hr
assert not np.any(newS[1]%3)
assert not np.any((newR[1]-Pr)%3)

# Compare the actual normalized maps with the retained D38 action.
old=json.loads((OLD/'d_cm_fermat_degree8_joint.json').read_text())
oldPA=PA+C@np.array(old['a_mod12'],dtype=np.int32)
oldPB=PB+C@np.array(old['beta_correction_mod12'],dtype=np.int32)
oldX=power(X,old['summary']['Ihara_gauge_exponent']%576)
oldS=conj(oldX,conj((beta,oldPB%MOD),S))
oldR=conj(oldX,conj((A,oldPA%MOD),RR))
comparison={}
for name,new,previous in [('s',newS,oldS),('r',newR,oldR)]:
 assert new[0]==previous[0]
 diff=(new[1]-previous[1])%MOD
 assert not np.any(projectionQ(diff)%6)
 comparison[name]={'same_normalized_G6':True,
   'replaces_J3':bool(np.any(diff%3)),
   'J3_difference_support':int(np.count_nonzero(diff%3)),
   'replaces_J12':bool(np.any(diff%12))}
assert all(c['replaces_J3'] and c['replaces_J12'] for c in comparison.values())
assert (k-old['summary']['Ihara_gauge_exponent'])%48==0

# The exact common conjugator equations remain those of C8.
diffA=(projection4(PA48)-V.targetA[1])[R.nc]%8
diffB=(projection4(PB48)-V.targetB[1])[R.nc]%8
assert R.W['contains'](diffA) and R.W['contains'](diffB)
summary={'finite_seed':'J48 fiber product over C8 with T3',
 'J48_cusp_word_length':len(cusp),'all6912_coordinates_checked':True,
 'all1153_basis_images_checked':True,'kernel_generation_rank_mod2':d,
 'odd_kernel_map_is_exact_inner_x6':True,
 'base_action_is_exact_inner_x6_on_all6912_states':True,
 'odd_centralizer_average_checked_over_Z[1/2]':True,
 'odd_beta_abelianization_times2':odd_beta_ab2,'odd_gauge':-6,
 'finite_beta_abelianization':bab.tolist(),'finite_gauge_exponent':k,
 'T3_cusp_inner_exponent':-k//3,
 'both_m0_hexagons_checked':True,
 'normalized_entire_J3_action_is_identity':True,
 'normalized_previous_comparison':comparison,
 'same_normalized_D38_T3_action':True,
 'difference_of_T3_gauges':k-old['summary']['Ihara_gauge_exponent'],
 'x144_survives_new_seed':True,
 'exact_T3_common_conjugator_images_checked':True,
 'finite_seed_order':'2^15771 * 3^1156',
 'kernel_seed_to_J48_order':'2^11151',
 'kernel_seed_to_T3_order':'2^4202 * 3^1154',
 'cusp_order':1152,'N_ord':576,
 'A_word_length':len(Aw),'beta_word_length':len(Bw),
 'A_word_sha256':hashlib.sha256(bytes(Aw)).hexdigest(),
 'beta_word_sha256':hashlib.sha256(bytes(Bw)).hexdigest(),
 'scope':'Actual finite seed retained by the integral full homology construction. The full free profinite source remains unlifted.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'a_mod48':a48.tolist(),
 'beta_correction_mod48':b48.tolist(),'A_base_word':base_word(A),
 'beta_base_word':base_word(beta),'odd_A_correction_times2':aodd2.tolist(),
 'odd_beta_correction_times2':bodd2.tolist(),
 'odd_centralizer_base_word':csword,
 'A_common_difference_mod8':diffA.tolist(),'beta_common_difference_mod8':diffB.tolist()}
(OUT/'d_cm_fermat_homology_seed.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
