"""Independent free-word/Schreier/Fox check of the B.9 metabelian witness.

The input is the endomorphism of F(x,y,z), not its predicted Jacobian.
This supplementary review does not edit the parent-owned Part B.
"""
from pathlib import Path
import json
import sympy as S

def inv(w):
    return tuple(-i for i in reversed(w))

def mul(*words):
    r=[]
    for word in words:
        for i in word:
            if r and r[-1]==-i:
                r.pop()
            else:
                r.append(i)
    return tuple(r)

def comm(u,v):
    return mul(inv(u),inv(v),u,v)

X,Y,Z=(1,),(2,),(3,)
w=comm(comm(X,Y),comm(X,Z))
psi_y=mul(Y,w)

def schreier(word,m):
    # a=1; y_i=2+i; z_i=2+m+i.
    coset=0
    out=[]
    for letter in word:
        if letter==1:
            if coset==m-1: out.append(1)
            coset=(coset+1)%m
        elif letter==-1:
            if coset==0: out.append(-1)
            coset=(coset-1)%m
        elif abs(letter)==2:
            out.append((2+coset)*(1 if letter>0 else -1))
        elif abs(letter)==3:
            out.append((2+m+coset)*(1 if letter>0 else -1))
    assert coset==0
    return mul(out)

def fox_y_specialized(word,m,t):
    # Specialize a=y_i=1 and z_i=t^i, during an actual Fox derivative.
    prefix=0
    row=[S.Integer(0)]*m
    for letter in word:
        gen=abs(letter)
        if 2<=gen<2+m:
            row[gen-2]+=(1 if letter>0 else -1)*t**prefix
        elif 2+m<=gen<2+2*m:
            prefix+=(gen-2-m)*(1 if letter>0 else -1)
    return [S.expand(x) for x in row]

def main():
    t=S.Symbol('t')
    rows=[]
    for m in range(2,25):
        J=S.zeros(m)
        for i in range(m):
            word=schreier(mul(X*i,psi_y,(-1,)*i),m)
            exps=[sum((1 if j>0 else -1) for j in word if abs(j)==k)
                  for k in range(1,2*m+2)]
            assert exps==[1 if k==2+i else 0 for k in range(1,2*m+2)]
            row=fox_y_specialized(word,m,t)
            R=t**((m-1) if i==0 else -1)
            expected=[S.Integer(0)]*m
            expected[i]=R
            expected[(i-1)%m]-=R-1
            assert all(S.expand(a-b)==0 for a,b in zip(row,expected))
            for j,c in enumerate(row): J[i,j]=c
        expected_det=S.expand(1-(t**(m-1)-1)*(t**-1-1)**(m-1))
        if m<=8:
            assert S.cancel(J.det()-expected_det)==0
        poly=S.Poly(S.expand(expected_det*t**(m-1)),t)
        assert poly.nth(0)!=0 and poly.degree()==2*(m-1)
        rows.append({'m':m,'actual_Schreier_words_and_Fox_rows_checked':True,
                     'abelianization_identity':True,'min_exponent':-(m-1),
                     'max_exponent':m-1,'full_determinant_checked':m<=8})
    report={'input_y_image':psi_y,'commutator_convention':'u^-1 v^-1 u v',
            'cyclic_degrees_2_through_24':rows,
            'conclusion':'The actual word gives the stated nonunit determinant; B.9 metabelian witness verified.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
