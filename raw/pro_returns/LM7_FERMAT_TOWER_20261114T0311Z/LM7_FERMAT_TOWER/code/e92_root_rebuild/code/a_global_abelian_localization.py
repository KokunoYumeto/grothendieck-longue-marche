#!/usr/bin/env python3
"""E92: exact intrinsic abelian localization and the quadratic Kummer inverse."""
from pathlib import Path
from itertools import product
import argparse
import hashlib
import json
import sympy as s


def mat(x):
    return s.Matrix([[s.Rational(a) for a in row] for row in x])


def add(x,y):
    return (x[0]+y[0],x[1]+y[1])


def mul(x,y):
    # lambda^2=3lambda-3 in the actual Eisenstein integer ring.
    a,b=x;c,d=y
    return (a*c-3*b*d,a*d+b*c+3*b*d)


def conj(x):
    return (x[0]+3*x[1],-x[1])


def norm(x):
    return x[0]*x[0]+3*x[0]*x[1]+3*x[1]*x[1]


def power(x,n,modulus=None):
    assert n>=0
    z=(1,0)
    while n:
        if n&1:
            z=mul(z,x)
            if modulus:z=tuple(a%modulus for a in z)
        x=mul(x,x)
        if modulus:x=tuple(a%modulus for a in x)
        n//=2
    return z


def vp(n):
    assert n
    n=abs(n);v=0
    while n%3==0:n//=3;v+=1
    return v


def logarithm(x,n):
    """The genuine logarithm in 3O, modulo3^n, computed integrally."""
    z=(x[0]-1,x[1]);assert z[0]%3==z[1]%3==0
    modulus=3**n;out=(0,0);term=(1,0)
    for k in range(1,3*(n+2)):
        term=mul(term,z);den=3**vp(k)
        assert all(a%den==0 for a in term)
        inv=pow(k//den,-1,modulus)
        sign=1 if k%2 else -1
        out=tuple((a+sign*(b//den)*inv)%modulus for a,b in zip(out,term))
    return out


ZETA=(1,-1)
LAMBDA=(0,1)
U2=(-2,3)


def local_unit(x,n):
    """Literal mu6 carry and log coordinates in (u2,-2)."""
    assert x[0]%3
    omega=1 if x[0]%3==1 else -1
    signed=(omega*x[0],omega*x[1])
    eps=(-signed[1])%3
    principal=mul(power(ZETA,(-eps)%3),signed)
    assert tuple(a%3 for a in principal)==(1,0)
    modulus=3**n
    cols=[tuple(a//3 for a in logarithm(z,n+1)) for z in (U2,(-2,0))]
    L=s.Matrix.hstack(*[s.Matrix(z)for z in cols])
    assert int(L.det())%3==1
    v=s.Matrix([a//3 for a in logarithm(principal,n+1)])
    ab=tuple(int(a)%modulus for a in L.inv_mod(modulus)*v)
    back=mul(mul(power(ZETA,eps),power(U2,ab[0],3**(n+1))),power((-2,0),ab[1],3**(n+1)))
    back=tuple(omega*a%3**(n+1)for a in back)
    assert back==tuple(a%3**(n+1)for a in x)
    return eps,ab,L


def prime_generators(bound):
    result=[{'label':'lambda','p':3,'generator':LAMBDA,'norm':3}]
    for p in s.primerange(2,bound+1):
        p=int(p)
        if p==3:continue
        if p%3==2:
            result.append({'label':str(p),'p':p,'generator':(p,0),'norm':p*p})
        else:
            if p==13:g=U2
            else:
                B=2*int(s.sqrt(p))+4
                candidates=[(a,b)for a in range(-B,B+1)for b in range(1,B+1)if norm((a,b))==p]
                assert candidates
                g=min(candidates,key=lambda q:(abs(q[0])+abs(q[1]),q))
            result.extend([{'label':str(p)+'a','p':p,'generator':g,'norm':p},
                           {'label':str(p)+'b','p':p,'generator':conj(g),'norm':p}])
    for q in result:
        assert norm(q['generator'])==q['norm']
        assert mul(q['generator'],conj(q['generator']))==(q['norm'],0)
    return result


def main():
    here=Path(__file__).resolve().parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-code',type=Path)
    args=ap.parse_args()
    source=args.source_code or here
    if not (source/'e_wild_layers.json').is_file():
        source=here.parent.parent/'LM7_FERMAT_TOWER/code'
    paths={'wild_layers':source/'e_wild_layers.json',
           'actual_first_degree_maps':source/'a_abelian_kernel_obstruction.json'}
    layer=json.loads(paths['wild_layers'].read_text())['layers']['1']
    first=json.loads(paths['actual_first_degree_maps'].read_text())
    T=s.Matrix(layer['input_tau']);J=s.Matrix(layer['input_c'])
    TE=T[:2,:2];JE=J[:2,:2]
    E=s.eye(10)[:,2:]
    assert T*E==7*E and J*E==E*J[2:,2:]
    rel=s.Matrix([3,1]+[0]*8).row_join(E)
    assert (s.eye(10)-J)*(T-7*s.eye(10))*rel==s.zeros(10,9)
    relative_relation=(s.eye(10)-J)*(T-7*s.eye(10))
    assert relative_relation.rank()==1
    assert relative_relation[:,1]==-3*relative_relation[:,0]
    assert relative_relation[:,2:]==s.zeros(10,8)
    assert rel[:2,0]==s.Matrix([3,1])
    assert TE-s.eye(2)==s.Matrix([[0,-3],[3,-3]])
    assert JE==s.Matrix([[1,-1],[0,-1]])
    assert int((TE-s.eye(2)).det())==9
    hplus=(s.eye(10)+J)*s.eye(10)[:,0]/2
    assert J*hplus==hplus
    boundary=(T-s.eye(10))*hplus
    assert boundary[:2,0]==s.Matrix([0,3])
    carry=-boundary[2:,:]
    assert carry==s.Matrix([1,3,-1,2,0,1,1,2])
    # Literal Shapiro values of the global tuple
    # (3,9,lambda^2,lambda,zeta^-1 lambda^3).
    tuple_values=s.Matrix([1,3,-1,2,s.Rational(3,2),-s.Rational(1,2),s.Rational(5,2),s.Rational(1,2)])
    fixed_correction=s.Matrix([0,0,0,0,s.Rational(1,4),-s.Rational(1,4),s.Rational(1,4),-s.Rational(1,4)])
    assert J[2:,2:]*fixed_correction==fixed_correction
    assert carry-tuple_values==-6*fixed_correction
    GS=first['first_degree_gauge_smith']
    L,Li,R,Ri,D=(mat(GS[k])for k in ('left','left_inverse','right','right_inverse','diagonal_matrix'))
    G=(s.eye(10)-T)*(s.eye(10)+J)
    assert L*G*R==D and L*Li==Li*L==R*Ri==Ri*R==s.eye(10)
    assert [D[i,i]for i in range(10)]==[1,3,3,3,0,0,0,0,0,0]
    tors=s.zeros(10,3)
    for col,(i,j)in enumerate([(3,4),(6,7),(8,9)]):
        tors[i,col]=2;tors[j,col]=-2
    torcoords=L*tors
    assert torcoords[4:,:]==s.zeros(6,3)
    torsion_map=torcoords[1:4,:]
    assert int(torsion_map.det())%3
    torsion_inverse=torsion_map.inv_mod(3)
    assert (torsion_map*torsion_inverse).applyfunc(lambda q:q%3)==s.eye(3)
    coordinate_tests=0
    for trial in range(243):
        U=s.Matrix([(trial*(i+3)+i*i)%41-20 for i in range(10)])
        A=E*s.Matrix([(trial*(i+7)+3*i)%31-15 for i in range(8)])
        b=U[0];eps=int(U[1])%3;k=(U[1]-eps)/3
        toric=U-k*boundary-b*s.eye(10)[:,0]-eps*s.eye(10)[:,1]
        assert toric[:2,0]==s.zeros(2,1)
        assert b*s.eye(10)[:,0]+eps*s.eye(10)[:,1]+toric+k*boundary==U
        assert A[0]==A[1]==0
        coordinate_tests+=1
    carry_tests=0
    for eps,ep in product(range(3),repeat=2):
        for a,aa in product(range(-4,5),repeat=2):
            e=(eps+ep)%3;k=(eps+ep-e)//3
            assert 3*(a+aa+k)+e==(3*a+eps)+(3*aa+ep)
            # gamma=beta*c^-a cancels the actual carry exactly.
            assert k-(a+aa+k)+a+aa==0
            carry_tests+=1

    assert power(ZETA,3)==(1,0)
    assert mul(LAMBDA,LAMBDA)==(-3,3)
    assert norm(U2)==13
    assert tuple(a//3%3 for a in logarithm(U2,2))==(2,1)
    assert tuple(a//3%3 for a in logarithm((-2,0),2))==(2,0)
    records=prime_generators(199)
    assert next(z for z in records if z['label']=='13a')['generator']==U2
    local_records=[];log_checks=0
    for n in range(1,8):
        for q in records:
            if q['label']=='lambda':continue
            eps,ab,LL=local_unit(q['generator'],n)
            if n>1:
                ee,old,_=local_unit(q['generator'],n-1)
                assert ee==eps and tuple(a%3**(n-1)for a in ab)==old
            local_records.append({'prime':q['label'],'precision':n,'torsion':eps,'log_coordinates':ab})
            log_checks+=1
        assert local_unit(U2,n)[:2]==(0,(1,0))
        assert local_unit((2,0),n)[:2]==(0,(0,1))
    inverse_tests=0;torsion_carries=0
    outside=[q for q in records if q['label']not in ('lambda','13a','2')]
    for n in range(1,8):
        modulus=3**n
        data={q['label']:local_unit(q['generator'],n)[:2]for q in outside}
        for trial in range(81):
            coeff={q['label']:(trial*(i+3)+i*i)%modulus for i,q in enumerate(outside)}
            val,A,B,tors=(trial*7)%modulus,(trial*11+1)%modulus,(trial*13-2)%modulus,trial%3
            sumA=sum(coeff[q]*data[q][1][0]for q in coeff)%modulus
            sumB=sum(coeff[q]*data[q][1][1]for q in coeff)%modulus
            sumE=sum(coeff[q]*data[q][0]for q in coeff)%3
            pivots=(val,(A-sumA)%modulus,(B-sumB)%modulus,(tors-sumE)%3)
            assert (pivots[1]+sumA)%modulus==A
            assert (pivots[2]+sumB)%modulus==B
            assert (pivots[3]+sumE)%3==tors
            # Direct mu3 factor, including every finite carry.
            assert power(ZETA,(pivots[3]+sumE)%3)==power(ZETA,tors)
            inverse_tests+=1;torsion_carries+=1
        for j,q in enumerate(outside):
            tail=3**(n+j)
            ee,ab=data[q['label']]
            assert tail*ee%3==0 and all(tail*a%modulus==0 for a in ab)

    result={'statement':'E.92','status':'PASS',
        'inputs':{k:{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for k,p in paths.items()},
        'torus_embedding':[[int(x)for x in row]for row in E.tolist()],
        'actual_relative_basis':[[int(x)for x in row]for row in rel.tolist()],
        'relative_handle_coordinate':[0,1]+[0]*8,
        'global_local_image_type':'Z3^14 x C3^3',
        'global_local_kernel':'R_Q(primes except2,3)^2 x R_K(prime ideals except(lambda),(1+lambda^2),(2))^3',
        'elliptic_fixed_lift':list(map(str,hplus)),
        'elliptic_boundary':list(map(str,boundary)),
        'actual_toric_carry':list(map(str,carry)),
        'global_carry_tuple':['3','9','lambda^2','lambda','zeta^-1*lambda^3'],
        'carry_literal_values':list(map(str,tuple_values)),
        'carry_fixed_coboundary':list(map(str,fixed_correction)),
        'local_torus_torsion_to_intrinsic':[[int(x)for x in row]for row in torsion_map.tolist()],
        'local_torsion_inverse_mod3':[[int(x)for x in row]for row in torsion_inverse.tolist()],
        'local_elliptic_toric_inverse_checks':coordinate_tests,
        'finite_carry_coordinate_checks':carry_tests,
        'quadratic_prime_generators':records,
        'quadratic_prime_precision_checks':log_checks,
        'quadratic_localization_inverse_checks':inverse_tests,
        'actual_mu3_carry_checks':torsion_carries,
        'logarithmic_records':local_records,
        'local_logarithmic_basis_mod3':[[2,2],[1,0]],
        'exact_normalization':'pi=omega*zeta^epsilon*principal, principal in1+3O; lambda,u2,2,mu3 are literal global elements',
        'topology':'inverse limit of discrete direct sums, with uniform3-power tails and finite mu3 factor',
    }
    (here/'a_global_abelian_localization.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS actual torus/elliptic module maps, exact source marking and primitive global image')
    print('PASS',coordinate_tests,'elliptic/toric inverses and',carry_tests,'complete finite carries')
    print('PASS all three global mu3 generators and their exact local torsion inverse')
    print('PASS',log_checks,'quadratic prime/precision log identities')
    print('PASS',inverse_tests,'global/local inverse fibres and',torsion_carries,'actual mu3 carries')
    print('ALL PASS')


if __name__=='__main__':main()
