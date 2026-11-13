"""Exact free-word computations for the Fadell--Neuwirth presentations.
No group recognizer is used: inverse and braid identities are checked in free groups.
"""
from pathlib import Path
import json

def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(x for w in ws for x in w)
def subst(w,A):return mul(*(A[x-1] if x>0 else inv(A[-x-1]) for x in w))
def compose(A,B):return tuple(subst(w,A) for w in B)
def ident(n):return tuple((i,) for i in range(1,n+1))
def sigma(n,i,sgn=1):
    A=list(ident(n))
    if sgn==1:A[i-1]=(i,i+1,-i);A[i]=(i,)
    else:A[i-1]=(i+1,);A[i]=(-(i+1),i,i+1)
    return tuple(A)
def braid_aut(n,w):
    A=ident(n)
    for s in w:A=compose(A,sigma(n,abs(s),1 if s>0 else -1))
    return A
def pure_word(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-x for x in range(i+1,j))
def wordstr(w,names):
    return ' '.join(names[abs(x)-1]+('^-1' if x<0 else '') for x in w) or '1'
def comm(a,b):return mul(a,b,inv(a),inv(b))

def main():
    out=[]; data={}
    for n in (3,4):
        checks=0
        for i in range(1,n):
            assert compose(sigma(n,i),sigma(n,i,-1))==ident(n);checks+=1
            assert compose(sigma(n,i,-1),sigma(n,i))==ident(n);checks+=1
        for i in range(1,n-1):
            assert braid_aut(n,(i,i+1,i))==braid_aut(n,(i+1,i,i+1));checks+=1
        for i in range(1,n):
            for j in range(i+2,n):
                assert braid_aut(n,(i,j))==braid_aut(n,(j,i));checks+=1
        out.append(f'Artin action rank {n}: {checks} exact inverse/braid checks PASS')
        names=('x','y','z') if n==3 else ('p','q','r','s')
        pairs=[(1,3),(2,3)] if n==3 else [(1,3),(2,3),(1,4),(2,4),(3,4)]
        data[str(n)]={}
        for i,j in pairs:
            w=pure_word(i,j);A=braid_aut(n,tuple(-s for s in w))
            # Positive conjugation of the standard kernel A_{k,n+1}
            # is the Artin action of the mirror of the base braid.
            for k,u in enumerate(A,1):
                ew=()
                for x in u:
                    kw=pure_word(abs(x),n+1)
                    ew += kw if x>0 else inv(kw)
                lhs=braid_aut(n+1,w+pure_word(k,n+1)+inv(w))
                assert lhs==braid_aut(n+1,ew)
            assert subst(tuple(range(1,n+1)),A)==tuple(range(1,n+1))
            # Pure braids induce the identity on abelianization.
            for k,u in enumerate(A):
                ab=[sum((1 if x>0 else -1) for x in u if abs(x)==l) for l in range(1,n+1)]
                assert ab==[int(l==k) for l in range(n)]
            data[str(n)][f'A{i}{j}']=[list(u) for u in A]
            out.append(f'A{i}{j} = braid {w}; '+'; '.join(f'{names[k]} -> {wordstr(u,names)}' for k,u in enumerate(A)))
        out.append(f'rank {n}: all pure actions preserve boundary word and abelianization PASS')
        out.append(f'rank {n}: {len(pairs)*n} conjugation relators checked in the Artin action of B_{n+1} PASS')
    basepairs=[(1,3),(2,3),(1,4),(2,4),(3,4)]
    syzygies=[]
    for h,ij in enumerate([(1,3),(2,3)],1):
        acts=data['3'][f'A{ij[0]}{ij[1]}']
        for k,u in enumerate(acts,3):
            shifted=tuple((1 if t>0 else -1)*(abs(t)+2) for t in u)
            rel=red((h,k,-h)+inv(shifted))
            bw=()
            for t in rel:
                pword=pure_word(*basepairs[abs(t)-1])
                bw += pword if t>0 else inv(pword)
            A=braid_aut(4,tuple(-t for t in bw))
            assert A==ident(4)
            syzygies.append(list(rel))
    out.append('M0,6: six base relators each fix all four fibre generators; 24 exact syzygy compatibility checks PASS')
    data['M05_relators_for_24_syzygies']=syzygies
    out.extend(['M0,5: generators=5, semidirect conjugation relators=2*3=6',
                'M0,6: generators=9, semidirect conjugation relators=6+5*4=26',
                'Poincare M0,5=(1+2t)(1+3t)=1+5t+6t^2',
                'Poincare M0,6=(1+2t)(1+3t)(1+4t)=1+9t+26t^2+24t^3'])
    print('\n'.join(out))
    Path(__file__).with_name('levels_braids_actions.json').write_text(json.dumps(data,indent=2)+'\n')
if __name__=='__main__':main()
