#!/usr/bin/env python3
"""Exact notes-only quotient data for the full order-64 wreath cover.
The actual divisor/Picard comparisons require the accompanying proof note;
no fixed-subgroup or monodromy theorem is inferred from this calculation.
"""
from pathlib import Path
import hashlib,json
import sympy as S
s,X,Z,J=S.symbols('s X Z J');M=s**4+2*s*s+2

def red(f):
    n,d=S.cancel(f).as_numer_denom()
    return S.expand(S.rem(n*S.invert(d,M,s),M,s))
i=-1-s*s;q=3+2*s+2*s*s;yQ=-2*s*q
q0=red((q-1)**2/(4*q));y0=red(yQ*(1-q*q)/(8*q*q))
assert red(q0*q0+1)==0
assert red(y0*y0-(q0**3-q0))==0
slope=red((3*q0*q0-1)/(2*y0))
x2=red(slope*slope-2*q0);y2=red(-y0+slope*(q0-x2))
assert x2==0 and y2==0
qp=red(1/q)
assert qp==q.subs(s,-s)
# Translation by T=(0,0) sends x to 1/x on E4.
assert red(q*qp)==1
# The actual isogeny represents its dual-kernel character by target x-1.
source_cubic=X**3-6*X**2+X
assert S.factor((X-1)**2/(4*X)-1-source_cubic/(4*X**2))==0
assert S.rem(S.together((X-1)**2-4*X),X**2-6*X+1,X)==0
# Every odd-parity vector is cyclic for the actual four-coordinate rotation.
odd_cyclic=[]
for mask in range(16):
    if mask.bit_count()%2==0:continue
    vectors=[];v=mask
    for _ in range(4):
        vectors.append(v);v=((v<<1)&15)|(v>>3)
    piv={}
    for v in vectors:
        while v:
            b=v.bit_length()-1
            if b in piv:v^=piv[b]
            else:piv[b]=v;break
    assert len(piv)==4
    odd_cyclic.append({'odd_vector':mask,'rotations':vectors,'rank_over_F2':4})
# Divisors are recorded at kQ for k in Z/8, R=2Q,T=4Q.
def add(v,w):return [a+b for a,b in zip(v,w)]
def div_a(j):
    v=[0]*8
    v[(2-2*j)%8]+=1;v[(-2*j)%8]+=1;v[(1-2*j)%8]-=2
    return v
a=[div_a(j) for j in range(4)]
norm=[sum(v[k] for v in a) for k in range(8)]
assert norm==[2,-2,2,-2,2,-2,2,-2]
half=[z//2 for z in norm]
assert sum(k*z for k,z in enumerate(half))%8==4
adj=add(a[0],a[1]);opp=add(a[0],a[2])
assert adj==[2,-2,1,0,0,0,1,-2]
assert opp==[1,-2,1,0,1,-2,1,0]
# The complementary triple differs from the branch line with half-point Q+T by a square.
triple=[norm[k]-a[0][k] for k in range(8)]
a_QT=[0]*8;a_QT[0]=a_QT[2]=1;a_QT[5]=-2
hd=[(triple[k]-a_QT[k])//2 for k in range(8)]
assert all((triple[k]-a_QT[k])%2==0 for k in range(8))
assert sum(hd)==0 and sum(k*z for k,z in enumerate(hd))%8==0
# Complete N-character dimension table.
chars=[]
for mask in range(1,16):
    div=[sum(a[j][k] for j in range(4) if mask>>j&1) for k in range(8)]
    branches=[k for k,z in enumerate(div) if z%2]
    genus=1+len(branches)//2
    chars.append({'mask':mask,'selected_edges':[j for j in range(4) if mask>>j&1],
                  'divisor_at_kQ':div,'branch_indices':branches,'quotient_genus':genus,'prym_dimension':genus-1})
assert sum(z['prym_dimension'] for z in chars)+1==17
# Adjacent quotient z^2=x-1, and the D0 quotient with q0^2=-1.
def prym(qv,a2,b2):
    A=red(3*qv+a2);B=red(3*qv*qv+2*a2*qv+b2);C=red(qv**3+a2*qv*qv+b2*qv)
    f=X**3+B*X**2+red(A*C)*X+red(C*C)
    disc=red(S.discriminant(f,X));j=red(256*(B*B-3*A*C)**3/disc)
    return [B,red(A*C),red(C*C)],f,disc,j
adjcoef,adjf,adjdisc,adjj=prym(S.Integer(1),-6,1)
dcoef,df,ddisc,dj=prym(q0,0,-1)
assert adjcoef==[-8,12,16] and adjj==10976
assert dcoef==[-4,6,-4] and dj==128
extra=S.expand((Z*Z+q0)*(Z*Z+q0+1));extraB=red(2*q0+1);extraC=red(q0*(q0+1))
extraI=red(extraB*extraB+12*extraC)
extradisc=red(16*extraC*(extraB*extraB-4*extraC)**2)
extraj=red(256*extraI**3/extradisc)
assert red(extraj-(-11528-118792*q0))==0
# Literal biquadratic identity: v=u*w, u^2=z^2+q0-1, w^2=(z^2+q0)(z^2+q0+1).
assert red(S.expand((Z*Z+q0-1)*extra-((Z*Z+q0)**3-(Z*Z+q0))))==0

def squarefree(d):
    out=-1 if d<0 else 1
    for p,e in S.factorint(abs(d)).items():
        if e%2:out*=int(p)
    return out

def count_curve(p,coeff,degree):
    vals=[];count=1 if degree==3 else 2
    for x in range(p):
        val=(x**3+coeff[0]*x*x+coeff[1]*x+coeff[2])%p if degree==3 else (x**4+coeff[0]*x*x+coeff[1])%p
        chi=0 if val==0 else (1 if pow(val,(p-1)//2,p)==1 else -1)
        vals.append(chi);count+=1+chi
    tr=p+1-count;d=tr*tr-4*p
    return {'prime':p,'coefficients':coeff,'degree':degree,'points_at_infinity':1 if degree==3 else 2,
            'quadratic_character_values':vals,'point_count':count,'trace':tr,'frobenius_discriminant':d,
            'ordinary':tr%p!=0,'field_squarefree_radicand':squarefree(d)}

def find_distinct(name):
    tested=[];selected=[];fields=set()
    for p in list(S.primerange(5,200)):
        if name=='extra':
            roots=[a for a in range(p) if (a*a+1)%p==0]
            if not roots:continue
            z=roots[0];coef=[(1+2*z)%p,(z*(z+1))%p];degree=4
            f=Z**4+coef[0]*Z*Z+coef[1]
        else:
            vals=adjcoef if name=='adjacent' else dcoef
            coef=[int(x)%p for x in vals];degree=3;z=None
            f=Z**3+coef[0]*Z*Z+coef[1]*Z+coef[2]
        disc=int(S.discriminant(f,Z))%p
        if not disc:continue
        row=count_curve(p,coef,degree);row['polynomial_discriminant_mod_p']=disc
        if z is not None:row['q0_residue']=z
        tested.append(row)
        if row['ordinary'] and row['field_squarefree_radicand'] not in fields:
            fields.add(row['field_squarefree_radicand']);selected.append(row)
        if len(fields)==2:break
    assert len(fields)==2
    return {'tested':tested,'selected_distinct_ordinary_fields':selected}
counts={name:find_distinct(name) for name in ('adjacent','D0_prym','extra')}
result={'status':'PASS_EXACT_NOTES_ONLY_JACOBIAN_DATA','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'field_polynomial':str(M),'q':str(q),'q0_phi_Q':str(q0),'y0_phi_Q':str(y0),'twice_phi_Q':['0','0'],
 'q_prime_Q_plus_T':str(qp),'norm_half_divisor_class_multiple_Q':4,'actual_dual_isogeny_square_identity':True,'odd_rotation_cyclic_vectors':odd_cyclic,'divisor_a_j':a,
 'adjacent_divisor':adj,'opposite_divisor':opp,'triple_square_correction_half_divisor':hd,
 'all_character_quotients':chars,'total_Jacobian_dimension':17,
 'adjacent_prym':{'coefficients':[str(z) for z in adjcoef],'j':str(adjj),'cubic_discriminant':str(adjdisc)},
 'D0_prym':{'coefficients':[str(z) for z in dcoef],'j':str(dj),'cubic_discriminant':str(ddisc)},
 'extra_elliptic':{'quartic':str(extra),'quartic_B':str(extraB),'quartic_C':str(extraC),'j':str(extraj),'j_in_q0':'-11528-118792*q0','quartic_discriminant':str(extradisc)},
 'ordinary_reduction_certificates':counts,
 'scope':'Exact actual divisor classes, quotient identities and ordinary finite-field data. The isogeny decomposition, valuation/model and all-weight fixed-subgroup arguments require separately written proofs; this program promotes none.'}
if __name__=='__main__':
    data=json.dumps(result,indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(data);print(data,end='')
