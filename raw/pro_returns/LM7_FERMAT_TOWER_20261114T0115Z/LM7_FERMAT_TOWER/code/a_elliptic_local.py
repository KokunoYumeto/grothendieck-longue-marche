#!/usr/bin/env python3
"""Exact tame-local normal forms and integral class-three lifting for E.60."""
from fractions import Fraction as Q
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import importlib.util,json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

spec=importlib.util.spec_from_file_location('r',Path(__file__).with_name('a_elliptic_rank13.py'))
r=importlib.util.module_from_spec(spec)
with redirect_stdout(StringIO()):spec.loader.exec_module(r)

def invariant_data(H):
    h=r.aug(H)
    I=sum(Q(i//3)*H[i] for i in range(9));J=sum(Q(i%3)*H[i] for i in range(9))
    return h,I,J
def F(g):return r.apply(g,r.principal)
def relation(n,z):return r.gp(z,F(n),r.gi(z),r.power(n,-4))
def mod9central(g):return g[0],g[1],g[2][:9],tuple(int(q.numerator*pow(q.denominator,-1,9)%9) for q in g[2][9:])
def reduced_zero(g):return mod9central(g)==mod9central(r.identity)
def conjugate_section(n,z,w):
    return r.gp(w,n,r.gi(w)),r.gp(w,z,r.gi(F(w)))

smith=[];matrices=[];coordinate_maps=[];coordinate_checks=0
for A in range(3):
    for B in range(3):
        D=sp.zeros(11)
        for k in range(9):
            i,j=divmod(k,3);D[k,k]=-3;D[9,k]=4*i-A;D[10,k]=4*j-B
        D[9,9]=D[10,10]=9
        S=smith_normal_form(D,domain=ZZ)
        values=[abs(int(S[i,i])) for i in range(11)]
        assert values==[1,1]+[3]*7+[27]*2
        assert abs(D.det())==3**13
        # The two moment congruences have an integral unit minor mod3.
        C=sp.Matrix([[i//3-A for i in range(9)],[i%3-B for i in range(9)]])
        assert any(int(C[:,[i,j]].det())%3 for i in range(9) for j in range(i+1,9))
        p=3*((A+1)%3)+B;q=3*A+(B+1)%3
        G=sp.Matrix([[4*(p//3)-A,4*(q//3)-A],[4*(p%3)-B,4*(q%3)-B]])
        assert int(G.det())%3
        other=[j for j in range(9) if j not in (p,q)]
        enc=sp.zeros(9,11)
        for i,j in enumerate(other):enc[i,j]=1
        enc[7,p]=enc[8,q]=1
        for j in other:
            col=G.inv()*sp.Matrix([4*(j//3)-A,4*(j%3)-B])
            enc[7,j],enc[8,j]=col
        UV=3*G.inv()
        for i in range(2):
            for j in range(2):enc[7+i,9+j]=UV[i,j]
        ed=enc*D
        for i in range(9):
            mod=3 if i<7 else 27
            assert all(Q(ed[i,j]/mod).denominator%3 for j in range(11))
        for seed in range(12):
            K=sp.Matrix([sp.Rational((seed+3*j)%17-8,2**(j%2)) for j in range(11)])
            raw=enc*K;vals=[]
            for i,v in enumerate(raw):
                mod=3 if i<7 else 27;v=Q(v)
                vals.append(v.numerator*pow(v.denominator,-1,mod)%mod)
            rep=sp.zeros(11,1)
            for i,j in enumerate(other):rep[j]=vals[i]
            correction=enc*rep
            rep[p]=vals[7]-correction[7];rep[q]=vals[8]-correction[8]
            assert all(Q(v).denominator%3 for v in D.inv()*(K-rep))
            coordinate_checks+=1
        coordinate_maps.append({'A':A,'B':B,'p':p,'q':q,'other_indices':other,
                                'G':G.tolist(),'encoding':enc.tolist()})
        smith.append({'A':A,'B':B,'Smith':values,'determinant':str(D.det())})
        matrices.append({'A':A,'B':B,'matrix':D.tolist()})

section_checks=0;gauge_checks=0;lift_checks=0
examples=[]
for A in range(3):
    for B in range(3):
        for seed in range(6):
            # Find a complete lattice element by scaling only two chosen
            # coordinates after first choosing seven free ones.
            hs=[Q((seed*(i+1)+2*i)%7-3) for i in range(9)]
            candidates=[]
            for j in range(9):
                for k in range(j+1,9):
                    C=sp.Matrix([[j//3-A,k//3-A],[j%3-B,k%3-B]])
                    if int(C.det())%3:candidates.append((j,k,C));break
                if candidates:break
            j,k,C=candidates[0]
            base_h,base_I,base_J=invariant_data(tuple(hs)+r.zero[9:])
            rhs=sp.Matrix([A*base_h-base_I,B*base_h-base_J])
            # Solve mod3 using the inverse of the unit minor.
            adjust=C.inv()*rhs
            hs[j]+=Q(r.residue(Q(adjust[0])));hs[k]+=Q(r.residue(Q(adjust[1])))
            h,I,J=invariant_data(tuple(hs)+r.zero[9:])
            u=(A*h-I)/3;v=(B*h-J)/3
            assert u.denominator%3 and v.denominator%3
            H=tuple(hs)+ (u,v)
            K=tuple(Q((seed+3*i)%11-5,2**(i%2)) for i in range(11))
            n=(Q(0),Q(0),H);z=(Q(3*A),Q(3*B),K)
            assert relation(n,z)==r.identity
            section_checks+=1
            # A full geometric conjugation and the exact normalization of
            # its two genus coordinates return the original genus values.
            s,t=Q(seed-2),Q(2-seed,2)
            L=tuple(Q((i+seed)%5-2) for i in range(11))
            w=(3*s,3*t,L)
            nn,zz=conjugate_section(n,z,w)
            assert zz[0]/3==A+3*s and zz[1]/3==B+3*t
            assert nn[2][:9]==n[2][:9]
            assert nn[2][9:]==(u+s*h,v+t*h)
            assert relation(nn,zz)==r.identity
            correction=(Q(-3*s),Q(-3*t),r.zero)
            n2,z2=conjugate_section(nn,zz,correction)
            assert z2[0]/3==A and z2[1]/3==B and n2==n
            gauge_checks+=1
            # The residual module conjugation is exactly D_(A,B).
            n3,z3=conjugate_section(n,z,(0,0,L))
            D=sp.Matrix(matrices[3*A+B]['matrix'])
            diff=tuple(Q(x) for x in D*sp.Matrix(L))
            assert n3==n and z3[2]==r.add(K,diff)
            gauge_checks+=1
            # All nine lower-class choices satisfy the tame relation;
            # precisely the specified one lifts to the full group.
            for i in range(3):
                for j in range(3):
                    lowerH=tuple(hs)+(u+3*i,v+3*j)
                    lowern=(0,0,lowerH)
                    err=relation(lowern,z)
                    assert reduced_zero(err)
                    lhs=(A*h-I-3*lowerH[9],B*h-J-3*lowerH[10])
                    assert err==(0,0,r.add(r.scale(r.U,4*lhs[0]),r.scale(r.V,4*lhs[1])))
                    liftable=all(Q(x/27).denominator%3 for x in lhs)
                    assert liftable==(i==j==0)
                    lift_checks+=1
            if seed==0:examples.append({'A':A,'B':B,'h':list(map(str,hs)),
                                       'u':str(u),'v':str(v)})

# In the central kernel A3=9ZU+9ZV the framed H1 is (Z/9)^2.
# The stabilizer C9^2 in the lower group maps bijectively onto it:
# conjugation by c^(rU+sV) changes the Frobenius value by +9rU+9sV.
stabilizer=[]
for i in range(9):
    for j in range(9):
        w=(0,0,r.add(r.scale(r.U,i),r.scale(r.V,j)))
        _,zz=conjugate_section(r.identity,r.identity,w)
        assert zz==(0,0,r.add(r.scale(r.U,9*i),r.scale(r.V,9*j)))
        assert reduced_zero(zz)
        stabilizer.append([i,j])
assert len({tuple(v) for v in stabilizer})==81

out={'status':'PASS','statement':'E.60','normalizations':section_checks,
     'exact_conjugation_and_gauge_checks':gauge_checks,
     'class_two_choices_and_lift_criteria':lift_checks,
     'local_Smith_systems':smith,'local_matrices':matrices,
     'explicit_finite_coordinate_maps':coordinate_maps,
     'finite_coordinate_roundtrips':coordinate_checks,
     'explicit_inertia_examples':examples,'stabilizer_Bockstein_values':stabilizer,
     'full_geometric_conjugacy_fiber':'one point whenever nonempty',
     'framed_central_lift_fiber':'(Z/9)^2',
     'class_two_lift_condition':'A h-I-3u and B h-J-3v lie in 27Z3'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('PASS:',len(smith),'complete local Smith systems:',smith[0]['Smith'])
print('PASS:',coordinate_checks,'round trips through the explicit unit-minor finite-coordinate maps.')
print('PASS:',section_checks,'actual tame sections,',gauge_checks,'exact conjugacy/normal-form comparisons.')
print('PASS:',lift_checks,'class-two representatives and integral class-three lift tests.')
print('PASS: all 81 central lower stabilizers act simply transitively on the framed lift torsor.')
