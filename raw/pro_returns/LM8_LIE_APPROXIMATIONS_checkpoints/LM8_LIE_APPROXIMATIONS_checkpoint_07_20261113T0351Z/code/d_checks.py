"""Exact word and divided-power checks for LM8 Parts D and E.

No group package or floating point is used.  Words act on the left; an
automorphism product f*g means f after g.  Magnus truncation is over Q.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from math import factorial,lcm
from pathlib import Path
import json
import sympy as s

def red(w):
    out=[]
    for t in w:
        if out and out[-1]==-t: out.pop()
        else: out.append(t)
    return tuple(out)
def inv(w): return tuple(-i for i in w[::-1])
def mul(*ws): return red(sum(ws,()))
def wpow(w,n): return mul(*((w if n>=0 else inv(w),)*abs(n)))
def sub(w,a): return mul(*(a[i] if i>0 else inv(a[-i]) for i in w))
def compose(a,b): return {i:sub(b[i],a) for i in b}
def apow(a,n):
    assert n>=0
    out={i:(i,) for i in a}
    for _ in range(n): out=compose(a,out)
    return out
def inner(w,r=2): return {i:mul(w,(i,),inv(w)) for i in range(1,r+1)}
def add(a,b):
    out=dict(a)
    for w,c in b.items():
        out[w]=out.get(w,Q(0))+c
        if not out[w]: del out[w]
    return out
def pmul(a,b,d):
    out={}
    for w,c in a.items():
        for v,e in b.items():
            if len(w+v)<=d:out[w+v]=out.get(w+v,Q(0))+c*e
    return {w:c for w,c in out.items() if c}
def magnus(w,d):
    out={():Q(1)}
    for i in w:
        if i>0: z={():Q(1),(i,):Q(1)}
        else:z={(abs(i),)*j:Q((-1)**j) for j in range(d+1)}
        out=pmul(out,z,d)
    return out
def magnus_matrix(a,r,d):
    words=[w for k in range(d+1) for w in product(range(1,r+1),repeat=k)]
    index={w:i for i,w in enumerate(words)}
    images={i:add(magnus(a[i],d),{():Q(-1)}) for i in a}
    mat=s.zeros(len(words))
    for j,w in enumerate(words):
        im={():Q(1)}
        for i in w:im=pmul(im,images[i],d)
        for v,c in im.items():mat[index[v],j]=s.Rational(c.numerator,c.denominator)
    return mat,words
def divided_powers(T):
    N=T-s.eye(T.rows);power=N;X=s.zeros(T.rows);k=1
    while power!=s.zeros(T.rows):
        X+=s.Rational((-1)**(k+1),k)*power
        power=power*N;k+=1
        if k>3*T.rows:raise RuntimeError('not unipotent')
    out=[];power=s.eye(T.rows)
    for j in range(k+2):
        den=lcm(*(int(x.q) for x in (power/s.factorial(j))))
        out.append(den);power=power*X
        if power==s.zeros(T.rows):break
    return X,k,out

def main():
    A={1:(1,),2:(2,1)}
    B={1:(1,-2),2:(2,)}
    Ai={1:(1,),2:(2,-1)};Bi={1:(1,2),2:(2,)}
    R={1:(2,),2:(1,)}
    c=(1,2,-1,-2)
    z=apow(compose(A,B),3)
    z2=compose(z,z)
    exact={
      'A_fixes_c':sub(c,A)==c,'B_fixes_c':sub(c,B)==c,
      'braid':compose(compose(A,B),A)==compose(compose(B,A),B),
      'reflection_A':compose(compose(R,A),R)==Bi,
      'reflection_B':compose(compose(R,B),R)==Ai,
      'z2_inner_c':z2==inner(c),'z2_inner_c_inverse':z2==inner(inv(c)),
      'z_images':{str(k):list(v) for k,v in z.items()}}
    assert all(exact[k] for k in ['A_fixes_c','B_fixes_c','braid','reflection_A','reflection_B'])
    assert exact['z2_inner_c'] or exact['z2_inner_c_inverse']
    nilpotent=[]
    for d in range(1,5):
        MA,_=magnus_matrix(A,2,d);MB,_=magnus_matrix(B,2,d);MR,_=magnus_matrix(R,2,d)
        nilpotent.append({'class':d,'dimension':MA.rows,
            'braid':MA*MB*MA==MB*MA*MB,'reflection':MR*MA*MR==MB.inv(),
            'center_square':(MA*MB)**6==magnus_matrix(z2,2,d)[0]})
    twist=[]
    # Four-punctured sphere: full twist of the first two punctures.
    p=(1,2)
    T04={1:mul(p,(1,),inv(p)),2:mul(p,(2,),inv(p)),3:(3,)}
    for name,aut,r in [('torus_A',A,2),('sphere_T12',T04,3)]:
        for d in [1,2]:
            M,words=magnus_matrix(aut,r,d);X,k,dens=divided_powers(M)
            least=next(n for n in range(1,25) if all((n**j*x).q==1 for j in range(k+1) for x in (X**j/s.factorial(j))))
            twist.append({'name':name,'truncation':d,'dimension':M.rows,
                'nilpotency_index_M_minus_I':k,'divided_power_denominators':dens,
                'least_positive_power_integral':least,
                'log_sparse':[[i,j,str(X[i,j])] for i in range(X.rows) for j in range(X.cols) if X[i,j]],
                'word_basis':[''.join(map(str,w)) or '1' for w in words]})
    N=s.zeros(5)
    for i,v in enumerate([1,2,3,2]):N[i,i+1]=v
    X,k,dens=divided_powers(s.eye(5)+N)
    counter={'N':list(map(list,N.tolist())),'log':list(map(list,X.tolist())),
      'denominators':dens,'fourth_divided_power_15':str((X**4/s.factorial(4))[0,4]),
      'N2_divisible_by2':all(int(v)%2==0 for v in N**2),
      'N3_divisible_by3':all(int(v)%3==0 for v in N**3)}
    out={'exact_free_word_checks':exact,'classes_1_to_4':nilpotent,'twists':twist,'rank5_counterexample':counter,
       'nilpotent_quotient_B3':{'classes':[1,2,3,4],'all_equal_to':'Z','reason':'the braid relation kills the degree-two commutator; gamma2=gamma3'}}
    path=Path(__file__).with_name('d_checks.json');path.write_text(json.dumps(out,indent=2,default=int)+'\n')
    print(json.dumps(out,indent=2,default=int))
if __name__=='__main__':main()
