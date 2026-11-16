#!/usr/bin/env python3
"""Independent exact PB4 coefficient certificate for the low Ihara action.

Uses the new Magnus engine, evaluates the actual group pentagon on its
free rank3 fibre, and determines both degree4 coefficients symbolically
in the arbitrary degree2 coefficient r. The degree3 parameter is retained.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import de_tame_hall as m


class RightAction:
    def __init__(self, images):
        self.images = images
        self.cache = {():m.ONE}
    def apply(self, p):
        def word(w):
            if w not in self.cache:
                self.cache[w] = m.mul(word(w[:-1]), self.images[w[-1]])
            return self.cache[w]
        return m.add(*(m.scalar(word(w), c) for w,c in p.items()))
    def delta(self,p):
        return m.add(self.apply(p),m.scalar(p,-1))
    def log(self,p):
        out={}
        for k in range(1,6):
            p=self.delta(p)
            out=m.add(out,m.scalar(p,Q((-1)**(k+1),k)))
        return out
    def inverse(self):
        ans=[]
        for i in range(len(self.images)):
            p={(i,):Q(1)}
            out=dict(p)
            for k in range(1,6):
                p=self.delta(p)
                out=m.add(out,m.scalar(p,(-1)**k))
            ans.append(out)
        return RightAction(ans)


def compose(*actions):
    # Right conjugation p -> g^-1 p g is an antihomomorphism.
    images=[{(i,):Q(1)} for i in range(len(actions[0].images))]
    for a in actions:
        images=[a.apply(p) for p in images]
    return RightAction(images)


def inner(g):
    return RightAction([m.add(m.prod(m.power(g,-1),m.add(m.ONE,{(i,):Q(1)}),g),{():-1}) for i in range(3)])


def pb4_fibre():
    u,v,w=[m.add(m.ONE,{(i,):Q(1)}) for i in range(3)]
    iu,iv,iw=[m.power(z,-1) for z in (u,v,w)]
    uvw=m.comm(u,w)
    A=RightAction([m.add(m.prod(u,v,u,iv,iu),{():-1}),m.add(m.prod(u,v,iu),{():-1}),{(2,):Q(1)}])
    B=RightAction([{(0,):Q(1)},m.add(m.prod(v,w,v,iw,iv),{():-1}),m.add(m.prod(v,w,iv),{():-1})])
    D=RightAction([m.add(m.prod(u,w,u,iw,iu),{():-1}),m.add(m.prod(uvw,v,m.power(uvw,-1)),{():-1}),m.add(m.prod(u,w,iu),{():-1})])
    U,V,W=[inner(z) for z in (u,v,w)]
    central=compose(A,D,B)
    for z in (A,B,D):
        assert compose(central,z).images==compose(z,central).images
    checks=[(A,U,compose(U,V,U,V.inverse(),U.inverse())),
            (A,V,compose(U,V,U.inverse())),(A,W,W),
            (B,U,U),(B,V,compose(V,W,V,W.inverse(),V.inverse())),
            (B,W,compose(V,W,V.inverse())),
            (D,U,compose(U,W,U,W.inverse(),U.inverse())),
            (D,V,compose(compose(U,W,U.inverse(),W.inverse()),V,
                         compose(U,W,U.inverse(),W.inverse()).inverse())),
            (D,W,compose(U,W,U.inverse()))]
    for z,p,expected in checks:
        assert compose(z.inverse(),p,z).images==expected.images
    return A,B,D,U,V,W


def pb4_artin():
    generators=[m.add(m.ONE,{(i,):Q(1)}) for i in range(4)]
    positive=[]
    negative=[]
    for i in range(3):
        a,b=generators[i:i+2]
        pi=list(generators);ni=list(generators)
        pi[i]=m.prod(a,b,m.power(a,-1));pi[i+1]=a
        ni[i]=b;ni[i+1]=m.prod(m.power(b,-1),a,b)
        positive.append(RightAction([m.add(z,{():-1}) for z in pi]))
        negative.append(RightAction([m.add(z,{():-1}) for z in ni]))
    identity=[{(i,):Q(1)} for i in range(4)]
    for s,t in zip(positive,negative):assert compose(s,t).images==identity
    for i in (0,1):
        a,b=positive[i:i+2]
        assert compose(a,b,a).images==compose(b,a,b).images
    assert compose(positive[0],positive[2]).images==compose(positive[2],positive[0]).images
    def pure(i,j):
        word=[positive[k] for k in range(j-1,i,-1)]
        word += [positive[i],positive[i]]
        word += [negative[k] for k in range(i+1,j)]
        a=compose(*word)
        assert [{w:c for w,c in z.items() if len(w)==1} for z in a.images]==identity
        return a
    return pure(0,1),pure(1,2),pure(0,2),pure(0,3),pure(1,3),pure(2,3)


C=m.bracket(m.X,m.Y)
U,V=m.bracket(m.X,C),m.bracket(m.Y,C)
E1,E2,E3=m.bracket(m.X,U),m.bracket(m.Y,U),m.bracket(m.Y,V)


def log_operator(F,A,B,p):
    out={}
    for word,co in F.items():
        value=p
        for letter in word:
            value=(A,B)[letter].log(value)
            if not value:break
        out=m.add(out,m.scalar(value,co))
    return out


def f_operator(F,A,B,p):
    d=log_operator(F,A,B,p)
    dd=log_operator(F,A,B,d)
    return m.add(p,d,m.scalar(dd,Q(1,2)))


def main():
    A,B,D,UU,VV,W=pb4_fibre()
    pairs=[(B,W),(compose(A,D),compose(VV,W)),(A,B),
           (A,compose(B,VV)),(compose(D,B),W)]
    def defect(r,h,c,d):
        F=m.add(m.scalar(C,r),m.scalar(m.add(U,V),h),
                m.scalar(m.add(E1,E3),c),m.scalar(E2,d))
        result={}
        for i in range(3):
            left=right={(i,):Q(1)}
            for k in range(3):left=f_operator(F,*pairs[k],left)
            for k in range(3,5):right=f_operator(F,*pairs[k],right)
            for w,co in m.add(left,m.scalar(right,-1)).items():result[(i,)+w]=co
        return result
    rp,rm=defect(Q(1),0,0,0),defect(Q(-1),0,0,0)
    linear=m.scalar(m.add(rp,m.scalar(rm,-1)),Q(1,2))
    square=m.scalar(m.add(rp,rm),Q(1,2))
    hcol=defect(0,Q(1),0,0)
    ccol,dcol=defect(0,0,Q(1),0),defect(0,0,0,Q(1))
    assert not hcol
    # c=-r/30-2r²/5; d=-r/20-r²/10.
    assert not m.add(linear,m.scalar(ccol,Q(-1,30)),m.scalar(dcol,Q(-1,20)))
    assert not m.add(square,m.scalar(ccol,Q(-2,5)),m.scalar(dcol,Q(-1,10)))
    # Repeat in the direct Artin representation; it is independent of
    # the rank3 free-fibre presentation used above.
    A4,B4,D4,U4,V4,W4=pb4_artin()
    artin_pairs=[(B4,W4),(compose(A4,D4),compose(V4,W4)),(A4,B4),
                 (A4,compose(B4,V4)),(compose(D4,B4),W4)]
    def artin_defect(r,h,c,d):
        F=m.add(m.scalar(C,r),m.scalar(m.add(U,V),h),
                m.scalar(m.add(E1,E3),c),m.scalar(E2,d))
        result={}
        for i in range(4):
            left=right={(i,):Q(1)}
            for k in range(3):left=f_operator(F,*artin_pairs[k],left)
            for k in range(3,5):right=f_operator(F,*artin_pairs[k],right)
            for w,co in m.add(left,m.scalar(right,-1)).items():result[(i,)+w]=co
        return result
    ap,am=artin_defect(Q(1),0,0,0),artin_defect(Q(-1),0,0,0)
    al=m.scalar(m.add(ap,m.scalar(am,-1)),Q(1,2))
    aq=m.scalar(m.add(ap,am),Q(1,2))
    ac,ad=artin_defect(0,0,Q(1),0),artin_defect(0,0,0,Q(1))
    assert not artin_defect(0,Q(1),0,0)
    assert not m.add(al,m.scalar(ac,Q(-1,30)),m.scalar(ad,Q(-1,20)))
    assert not m.add(aq,m.scalar(ac,Q(-2,5)),m.scalar(ad,Q(-1,10)))
    artin_words=sorted(set(ac)|set(ad))
    artin_minor=None
    for i,w in enumerate(artin_words):
        for z in artin_words[i+1:]:
            det=ac.get(w,0)*ad.get(z,0)-ad.get(w,0)*ac.get(z,0)
            if det:
                artin_minor={'rows':[w,z],'matrix':[[str(ac.get(t,0)),str(ad.get(t,0))] for t in (w,z)],
                             'determinant':str(det),
                             'linear_r':[str(al.get(t,0)) for t in (w,z)],
                             'quadratic_r':[str(aq.get(t,0)) for t in (w,z)]}
                break
        if artin_minor:break
    assert artin_minor
    # These two rows are deliberately retained with their nonunitdet=-5.
    w1=(0,0,0,0,1,2)
    w2=(0,0,0,0,2,1)
    matrix=[[ccol.get(w,0),dcol.get(w,0)] for w in (w1,w2)]
    determinant=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    assert determinant==-5
    # Independent symbolic hexagon, including the term determining r.
    from sympy.polys.rings import ring
    from sympy.polys.domains import QQ
    rr,q,h,r=ring('q,h,r',QQ)
    xx,yy=m.exponential(m.X),m.exponential(m.Y)
    zz=m.power(m.mul(xx,yy),-1)
    Z=m.logarithm(zz)
    def ff(A,B,r0,c0,d0):
        C0=m.bracket(A,B)
        U0,V0=m.bracket(A,C0),m.bracket(B,C0)
        E10,E20,E30=m.bracket(A,U0),m.bracket(B,U0),m.bracket(B,V0)
        return m.exponential(m.add(m.scalar(C0,r0),m.scalar(m.add(U0,V0),h),
                                  m.scalar(m.add(E10,E30),c0),m.scalar(E20,d0)))
    def hexagon(r0,c0,d0):
        mm=(q-1)/2
        return m.prod(m.power(xx,mm),ff(Z,m.X,r0,c0,d0),
                      m.power(zz,mm),ff(m.Y,Z,r0,c0,d0),
                      m.power(yy,mm),ff(m.X,m.Y,r0,c0,d0))
    quadratic=hexagon(r,0,0).get((0,1),0)
    assert quadratic==3*r-(q*q-1)/8
    hexvalue=hexagon((q*q-1)/24,-(q**4-1)/1440,-(q*q-1)*(q*q+11)/5760)
    assert {w:c for w,c in hexvalue.items() if len(w)<=4}==m.ONE
    rows=[]
    for w in sorted(set(linear)|set(square)|set(ccol)|set(dcol)):
        rows.append({'word':w,'r':str(linear.get(w,0)),'r2':str(square.get(w,0)),
                     'c':str(ccol.get(w,0)),'d':str(dcol.get(w,0))})
    out={'status':'all exact identities passed','PB4_relations_checked':12,
         'pentagon_degree_bound':5,'h_column_zero':True,
         'selected_rows':[w1,w2],'minor':[[str(z) for z in row] for row in matrix],
         'determinant':str(determinant),
         'hexagon_quadratic_equation':str(quadratic),
         'full_hexagon_verified_through_degree':4,
         'direct_Artin_B4_check':artin_minor,
         'solutions':{'r':'(q^2-1)/24','c':'-(q^4-1)/1440',
                      'd':'-(q^2-1)*(q^2+11)/5760'},
         'all_nonzero_rows':rows}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='all_nonzero_rows'},indent=2))


if __name__=='__main__':main()
