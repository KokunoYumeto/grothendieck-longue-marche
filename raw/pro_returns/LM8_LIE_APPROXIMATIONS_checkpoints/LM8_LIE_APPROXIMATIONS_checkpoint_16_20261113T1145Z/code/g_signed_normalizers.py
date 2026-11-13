#!/usr/bin/env python3
"""Exact finite certificates for B.35, plus the q2 invariant line.

The finite modular extension is reconstructed from the executed integral
B.24a cocycle.  Coordinate formulas are independently evaluated on every
group element; these are reductions of the proved profinite images, not
claims that arbitrary finite signed shadows lift.
"""
from pathlib import Path
from math import gcd,lcm
from itertools import product
import hashlib,json
import sympy as sp

HERE=Path(__file__).resolve().parent
source=HERE/'g_signed_fermat2_model.json'
raw=source.read_bytes();data=json.loads(raw)
reps=data['minimal_representatives'];acts=data['minimal_actions']
hmul=data['minimal_multiplication'];coc=data['minimal_cocycle']
hi=reps.index([]);hr=reps.index([1]);hs=reps.index([2])
hinv=[next(j for j in range(12) if hmul[i][j]==hi) for i in range(12)]

def mv(A,v):return tuple(sum(a*b for a,b in zip(row,v)) for row in A)

def epsilon8(mu):return ((mu*mu-1)//8)%2

def model(n):
    one=(hi,0,0);rho=(hr,0,0);sigma=(hs,0,0)
    def mul(g,h):
        q,r=g[0],h[0];v=mv(acts[q],h[1:]);c=coc[q][r]
        return hmul[q][r],(g[1]+v[0]+c[0])%n,(g[2]+v[1]+c[1])%n
    def inv(g):
        q=g[0];r=hinv[q]
        v=mv(acts[r],(-g[1]-coc[q][r][0],-g[2]-coc[q][r][1]))
        return r,v[0]%n,v[1]%n
    def power(g,k):
        if k<0:return power(inv(g),-k)
        ans=one
        while k:
            if k&1:ans=mul(ans,g)
            g=mul(g,g);k//=2
        return ans
    def conj(c,g):return mul(mul(c,g),inv(c))
    def word(w,r=rho,s=sigma):
        gs={1:r,2:s,-1:inv(r),-2:inv(s)};ans=one
        for a in w:ans=mul(ans,gs[a])
        return ans
    omega=power(rho,3);e0=mul(sigma,rho);e1=mul(rho,sigma)
    a=inv(e0);b=inv(e1)
    x=mul(omega,power(e0,2));y=mul(omega,power(e1,2))
    assert x==(hi,1%n,0) and y==(hi,0,1%n)
    els=[(h,u,v) for h in range(12) for u in range(n) for v in range(n)]
    idx={g:i for i,g in enumerate(els)};ir=idx[rho];iss=idx[sigma]
    generators=[rho,sigma,inv(rho),inv(sigma)]
    modulus=lcm(8,12*n)
    units=[mu for mu in range(modulus) if gcd(mu,modulus)==1]
    smaps={};hmaps={};edges=0
    rho_auts=set();sigma_auts=set()
    for mu in units:
        ap,bp=power(a,mu),power(b,mu)
        rp=mul(ap,bp);spow=inv(mul(mul(ap,bp),ap))
        rep_images=[word(w,rp,spow) for w in reps]
        images=[mul(mul(power(x,mu*g[1]),power(y,mu*g[2])),rep_images[g[0]]) for g in els]
        sm={g:h for g,h in zip(els,images)}
        assert len(set(images))==len(els)
        for g in els:
            for z in generators:
                assert sm[mul(g,z)]==mul(sm[g],sm[z]);edges+=1
        e2=1 if mu%4==1 else -1
        assert sm[sigma]==power(sigma,e2)
        e3=1 if mu%3==1 else -1;v3=(1-e3)//2
        amu=(e3*mu-1)//6
        hc=mul(power(mul(x,inv(y)),amu),power(sigma,v3))
        hp=tuple(idx[conj(hc,sm[g])] for g in els)
        assert els[hp[ir]]==power(rho,e3)
        hmaps[mu]=hp;smaps[mu]=tuple(idx[sm[g]] for g in els)
        for j in range(3):
            rj=power(rho,j)
            perm=tuple(idx[conj(rj,els[hp[idx[g]]])] for g in els)
            rho_auts.add(perm)
        for t in range(2*n):
            if t%2!=epsilon8(mu):continue
            for e in range(2):
                cc=mul(power(mul(x,y),t),power(sigma,e))
                perm=tuple(idx[conj(cc,sm[g])] for g in els)
                assert els[perm[iss]]==power(sigma,e2)
                sigma_auts.add(perm)
    rho_law_checks=0
    for mu,nu in product(units,repeat=2):
        p,q=hmaps[mu],hmaps[nu];target=hmaps[mu*nu%modulus]
        assert (p[q[ir]],p[q[iss]])==(target[ir],target[iss])
        rho_law_checks+=1
    # All candidates are established automorphisms, so equality on these two
    # generators certifies the group law.  Exhaust closure of the reduced sets.
    closure_checks={}
    for name,autos in [('rho',rho_auts),('sigma',sigma_auts)]:
        keys={(p[ir],p[iss]) for p in autos};checks=0
        for p,q in product(autos,repeat=2):
            assert (p[q[ir]],p[q[iss]]) in keys;checks+=1
        closure_checks[name]=checks
    return {'n':n,'quotient_order':len(els),'multiplier_test_modulus':modulus,
      'complete_s_mu_generator_edge_checks':edges,
      'rho_section_law_checks':rho_law_checks,
      'rho_image_order':len(rho_auts),'sigma_image_order':len(sigma_auts),
      'normalizer_image_closure_checks':closure_checks,
      's_mu_sigma_power_verified':True}

finite=[model(n) for n in range(1,9)]
parity=[]
for m in [2,4,8,16,32,64]:
    pairs=[(k,t) for k,t in product(range(m),repeat=2) if (2*t+k*k)%m==0]
    ks={k for k,t in pairs};assert ks==set(range(0,m,2))
    parity.append({'modulus':m,'solution_pairs':len(pairs),'allowed_k':sorted(ks)})
# The nonsplitting already appears in translation modulo4, multiplier modulo8.
units8=[1,3,5,7]
Q=[(t,mu) for mu in units8 for t in range(4) if t%2==epsilon8(mu)]
def qm(a,b):return ((a[0]+a[1]*b[0])%4,a[1]*b[1]%8)
assert all(qm(a,b) in Q for a,b in product(Q,repeat=2))
lifts3=[g for g in Q if g[1]==3];lifts7=[g for g in Q if g[1]==7]
checks=[]
for a,b in product(lifts3,lifts7):
    commute=qm(a,b)==qm(b,a)
    assert not commute
    checks.append({'lift3':a,'lift_minus1':b,'commute':False})
# Exact q2 matrices, retained for the subsequent arithmetic-line calculation.
r48=data['representatives'].index([1]);s48=data['representatives'].index([2])
R=sp.Matrix(data['actions'][r48]);S=sp.Matrix(data['actions'][s48]);J=S*R
P=sp.Matrix(data['projection_linear']);w=sp.Matrix([-1,1,0,1,0])
assert (J-sp.eye(5))*w==sp.zeros(5,1) and P*w==sp.zeros(2,1)
assert sp.Matrix.vstack(J-sp.eye(5),P).nullspace()==[w]
diff=(sp.eye(5)-R)*w
assert diff==(sp.eye(5)-S)*w==sp.Matrix([-1,1,1,1,-1])
# y deck action = (rho sigma)^2 because omega acts trivially.
Y=(R*S)**2
assert Y*w==-w
result={'status':'Proved','integral_model_input':source.name,
 'integral_model_sha256':hashlib.sha256(raw).hexdigest(),
 'finite_normalizer_images':finite,'class_two_parity_certificates':parity,
 'nonsplit_finite_extension':{'order':len(Q),'base_units_mod8':units8,
  'translation_modulus':4,'all_four_pairs_of_generator_lifts':checks},
 'q2_primitive_line':{'w':list(w),'e0_fixed_rank':len((J-sp.eye(5)).nullspace()),
  'joint_fixed_projection_kernel_rank':1,'rho_and_sigma_coboundary':list(diff),
  'y_acts_on_w':-1},
 'scope':'Finite tables verify reductions of the proved source images. Arithmetic realization uses the midpoint Kummer proof in B.35; no finite shadow is assumed to lift.'}
# Sympy integers are exact but need explicit conversion for JSON.
def serial(z):
 if isinstance(z,sp.Integer):return int(z)
 raise TypeError(type(z).__name__)
out=json.dumps(result,indent=2,default=serial)+'\n'
(HERE/'g_signed_normalizers.json').write_text(out)
(HERE/'g_signed_normalizers.out').write_text(out)
print(out)
