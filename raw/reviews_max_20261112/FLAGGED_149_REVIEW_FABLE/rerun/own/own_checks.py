# Own checks for the intake of FLAGGED_149 (Claude Fable 5.2). Written from the paper, not from the return's code.
import itertools, sympy as sp
x,t,z=sp.symbols('x t z')
out=[]
# F17.2: discriminant of (x^3-t^6)(x^3-1)
d=sp.factor(sp.discriminant(sp.expand((x**3-t**6)*(x**3-1)),x)); out.append(('F17.2 disc',str(d)))
# F17.8: discriminant of x^6-3x^2-2+t
d=sp.factor(sp.discriminant(x**6-3*x**2-2+t,x)); out.append(('F17.8 disc',str(d)))
out.append(('F17.8 expansion',sp.expand((x**2+1)**2*(x**2-2))==x**6-3*x**2-2))
# Z142e: factorizations and critical values
h=z**3-3*z+t
out.append(('Z142e fact1',sp.expand(h-(t-2)-(z-1)**2*(z+2))==0))
out.append(('Z142e fact2',sp.expand(h-(t+2)-(z+1)**2*(z-2))==0))
c=sp.symbols('c'); out.append(('Z142e disc',str(sp.factor(sp.discriminant(h-c,z)))))
# B14: finite fields F_3^n as polynomials mod irreducible
def mk(p,mod):  # mod: monic coefficient list low->high of degree n
    n=len(mod)-1
    def add(a,b): return tuple((u+v)%p for u,v in zip(a,b))
    def mul(a,b):
        r=[0]*(2*n-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b): r[i+j]=(r[i+j]+u*v)%p
        for k in range(2*n-2,n-1,-1):
            co=r[k]
            if co:
                for i in range(n): r[k-n+i]=(r[k-n+i]-co*mod[i])%p
                r[k]=0
        return tuple(r[:n])
    els=list(itertools.product(range(p),repeat=n))
    one=tuple([1]+[0]*(n-1)); zero=tuple([0]*n)
    return els,add,mul,one,zero
def count_D(p,mod):
    els,add,mul,one,zero=mk(p,mod)
    sq={}
    for e in els: sq.setdefault(mul(e,e),0); sq[mul(e,e)]+=1
    def neg(a): return tuple((-u)%p for u in a)
    tot=0
    for tt in els:
        t2=mul(tt,tt); t4=mul(t2,t2); t8=mul(t4,t4)
        rhs=add(add(add(one,neg(t2)),neg(t4)),neg(t8))
        tot+=sq.get(rhs,0)
    minus1=neg(one)
    inf=2 if minus1 in sq and minus1!=zero else 0
    return tot,inf
out.append(('B14 #D(F3) affine,inf',count_D(3,[1,1])))            # F_3 = F_3[a]/(a+1) trivial model
out.append(('B14 #D(F9) affine,inf',count_D(3,[1,0,1])))          # a^2+1
out.append(('B14 #D(F27) affine,inf',count_D(3,[2,2,0,1])))       # a^3-a-1 = a^3+2a+2
# B14: E(F_3): w^2 = u^4+u^3+2u^2+u+2
E3=[(u,w) for u in range(3) for w in range(3) if (w*w-(u**4+u**3+2*u*u+u+2))%3==0]; out.append(('B14 E(F3) affine',E3))
# B15: E(F_5): w^2 = x^4+2x^3+2x^2-x-1 ; factorization
E5=[(a,w) for a in range(5) for w in range(5) if (w*w-(a**4+2*a**3+2*a*a-a-1))%5==0]; out.append(('B15 E(F5) affine',E5))
out.append(('B15 factorization',sp.Poly(sp.expand((x-1)*(x**4+2*x**3+2*x**2-x-1)-(x**5+(x**2+1)**2)),x,modulus=5).is_zero))
# B7: E/F_5: y^2=x^3+3x+2
out.append(('B7 E(F5) affine',[(a,b) for a in range(5) for b in range(5) if (b*b-(a**3+3*a+2))%5==0]))
# B9: hyperplane incidence in F_2^4
G=list(itertools.product(range(2),repeat=4))
H=[f for f in G if any(f)]
cnt={g:sum(1 for f in H if sum(a*b for a,b in zip(f,g))%2==0) for g in G}
out.append(('B9 incidence',sorted(set((('id' if not any(g) else 'non-id'),v) for g,v in cnt.items()))))
# ZCF4: branch-value checks for F on (P^1)^3, B={0,1,-1,i,-i,inf}
I=sp.I
def F(a,b,c): return 1+7*a+3*b+2*c+13*a*b+11*a*c+5*b*c+19*a*b*c
B=[0,1,-1,I,-I]
x1,x2,x3=sp.symbols('x1 x2 x3')
Fp=sp.Poly(F(x1,x2,x3),x1,x2,x3)
def val(pt):  # pt entries in B or 'inf': evaluate the trihomogeneous form
    e=Fp.as_expr(); 
    for v,s in zip(pt,(x1,x2,x3)):
        if v=='inf': e=sp.expand(e).coeff(s,1)
        else: e=e.subs(s,v)
    return sp.simplify(e)
bad=[pt for pt in itertools.product(B+['inf'],repeat=3) if val(pt)==0]
out.append(('ZCF4 zero values at 216 branch triples',len(bad)))
for k,v in out: print(k,':',v)
