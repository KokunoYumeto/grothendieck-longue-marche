#!/usr/bin/env python3
"""Literal free-by-C4 source maps and integral class-two graph identities.

This is a new full-pro-three investigation after the frozen E69 finite
certificate. Rational polynomial identities here hold over Z_3 because
their only denominators are powers of two. Free words are reduced exactly.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import sympy as sp

HERE=Path(__file__).resolve().parent


def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return tuple(a)


def winv(w):return tuple(-x for x in reversed(w))
def wmul(a,b):return red(a+b)
def phi(w):return tuple(-2 if x==1 else 2 if x==-1 else 1 if x==2 else -1 for x in w)
def phipow(w,n):
    for _ in range(n%4):w=phi(w)
    return w


def mul(g,h):return (wmul(g[0],phipow(h[0],g[1])),(g[1]+h[1])%4)
def inv(g):return (phipow(winv(g[0]),-g[1]),-g[1]%4)
def power(g,n):
    if n<0:g,n=inv(g),-n
    a=((),0)
    while n:
        if n&1:a=mul(a,g)
        g=mul(g,g);n//=2
    return a
def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
def conj(g,h):return mul(mul(g,h),inv(g))


X=((1,),0);Y=((2,),0);d=((),1)
x=mul(X,d);y=mul(inv(Y),power(d,2));z=d
pairs=[(x,y),(y,x),(z,x),(x,z),(y,z),(z,y)]


def evalword(w,a,b):
    vals={1:a,2:b,-1:inv(a),-2:inv(b)};g=((),0)
    for t in w:g=mul(g,vals[t])
    return g


def logword(w):
    a=b=c=Q(0)
    for t in w:
        u=1 if t==1 else -1 if t==-1 else 0
        v=1 if t==2 else -1 if t==-2 else 0
        c+=Q(a*v-b*u,2);a+=u;b+=v
    return (a,b,c)


S=sp.Matrix([[0,1],[-1,0]])


def action(g,V):
    # Ad((w,d^e)) on the class-two free kernel.
    a,b,c=logword(g[0]);W=S**g[1]*sp.Matrix(V[:2])
    return (W[0],W[1],sp.expand(V[2]+a*W[1]-b*W[0]))


def A(V):return (-V[0],-V[1],sp.expand(V[2]-(V[0]+V[1])/2))
def B(V):return (-V[1],V[0],sp.expand(V[2]-(V[0]+V[1])/2))


def equal(a,b):return all(sp.expand(u-v)==0 for u,v in zip(a,b))


def main():
    one=((),0);c=comm(X,inv(Y))
    assert mul(mul(x,y),z)==one
    assert power(y,2)==power(z,4)==one
    assert power(x,4)==c
    assert mul(power(x,2),y)==X and mul(power(z,2),y)==Y
    assert conj(d,X)==inv(Y) and conj(d,Y)==X
    V=sp.symbols('v1 v2 vc')
    correspondence=[(2,3,A),(1,4,B),(0,5,B)]
    covariance=[];commutators=[]
    for i,j,T in correspondence:
        for gen in range(2):
            left=T(action(pairs[i][gen],V));right=action(pairs[j][gen],T(V))
            assert equal(left,right),(i,j,gen,left,right)
            covariance.append({'from':i+1,'to':j+1,'source_generator':gen+1,
                               'common_polynomial':[str(sp.expand(t)) for t in left]})
        ci=comm(*pairs[i]);cj=comm(*pairs[j])
        assert ci[1]==cj[1]==0
        li=logword(ci[0]);lj=logword(cj[0]);assert equal(T(li),lj)
        commutators.append({'from':i+1,'to':j+1,'from_word':list(ci[0]),
                            'to_word':list(cj[0]),'from_log':[str(t) for t in li],
                            'to_log':[str(t) for t in lj]})
    source_z=(-2,-1)
    x4=[power(a,4) for a,b in pairs]
    z4=[power(evalword(source_z,a,b),4) for a,b in pairs]
    assert x4==[c,one,one,c,one,one]
    assert z4==[one,one,one,one,c,conj(d,c)]
    # A genuinely nonzero class-three value distinguishes the full image
    # from the integral class-two graph. The commutators are exact free words.
    central_generators=[comm(c,X),comm(c,Y)]
    assert all(g[0] and g[1]==0 for g in central_generators)
    # Preserve a literal original-source witness as well: this word lies
    # in N' since x_source^6 is in N and N is normal in F.
    sx=(1,);a=sx*6
    wz=source_z*4
    w=red(wz+a+winv(wz)+winv(a))
    w=red(w+a+winv(w)+winv(a))
    values=[evalword(w,*p) for p in pairs]
    assert values[0]==one and values[5][0]
    # Full pro-three frames can be chosen with these exact class-two
    # coordinates. The central hy parameter is unrestricted; the hz
    # choice is precisely the graph equation, not just its mod3 shadow.
    q=sp.symbols('q')
    def cmul(u,v):
        return (u[0]+v[0],u[1]+v[1],sp.expand(u[2]+v[2]+(u[0]*v[1]-u[1]*v[0])/2))
    def cinv(u):return tuple(-a for a in u)
    norm_frames=[]
    for j in range(4):
        pj=mul(power(x,j),power(d,-j));vj=logword(pj[0])[:2]
        shifted=S**j*sp.Matrix([0,1])
        hy=(vj[0]-shifted[0]/2,vj[1]+(1-shifted[1])/2,q)
        hz=(vj[0],vj[1],(vj[0]+vj[1])/4)
        six=(cinv(hy),hy,hz,cinv(hz),cmul(cinv(hz),hy),cmul(cinv(hy),hz))
        assert equal(six[3],A(six[2]))
        assert equal(six[4],B(six[1]))
        assert equal(six[5],B(six[0]))
        norm_frames.append({'inner_x_power':j,'hy_class_two':[str(a) for a in hy],
                            'hz_class_two':[str(a) for a in hz],
                            'all_integral_graph_and_norm_equations':True})
    out={'status':'PASS_LITERAL_GAUSSIAN_PRO3_MAPS_AND_INTEGRAL_CLASS_TWO_GRAPH',
         'kernel_free_generators':['X','Y'],'deck_action':{'X':[-2],'Y':[1]},
         'peripheral_generators':{'x':[list(x[0]),x[1]],'y':[list(y[0]),y[1]],'z':[list(z[0]),z[1]]},
         'six_pairs':['xy','yx','zx','xz','yz','zy'],
         'primitive_boundary_c_word':list(c[0]),
         'x_source_fourth_values':[[list(a),e] for a,e in x4],
         'z_source_fourth_values':[[list(a),e] for a,e in z4],
         'integral_class_two_A':'(-v1,-v2,c-(v1+v2)/2)',
         'integral_class_two_B':'(-v2,v1,c-(v1+v2)/2)',
         'all_six_exact_covariance_polynomials':covariance,
         'all_three_normal_generator_comparisons':commutators,
         'gamma3_closed_normal_generators':[[list(a),e] for a,e in central_generators],
         'literal_source_graph_failure_word':list(w),
         'literal_source_graph_failure_values':[[list(a),e] for a,e in values],
         'literal_source_witness_membership':'[[z_source^4,x_source^6],x_source^6] lies in Nprime: x_source^6 in N, N normal in F.',
         'four_exact_integral_frame_families':norm_frames,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Exact source words and integral class-two identities. Full image and common quotients require the separately written compact/Frattini proof.'}
    (HERE/'bc_gaussian_pro3_maps.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
