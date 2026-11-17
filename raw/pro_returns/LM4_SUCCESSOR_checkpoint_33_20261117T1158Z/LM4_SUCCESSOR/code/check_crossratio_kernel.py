"""A nontrivial discrete loop killed by all 495 tetrahedral cross-ratio maps.

Let e_1,...,e_14 be meridians of the14 punctures of the ordered tetrahedral
parameter curve, with e_1...e_14=1.  Use a balanced iterated commutator in
all14 arguments.  Every one of the495 maps extends across at least two
punctures (degree<=4), so kills this word.  Nontriviality is certified both
by free reduction and by an explicit quotient SL(2,F_101).
"""
from pathlib import Path
import random

def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out
def inv(w):return [-a for a in reversed(w)]
def comm(a,b):return red(a+b+inv(a)+inv(b))
def tree(ws):
    if len(ws)==1:return ws[0]
    m=len(ws)//2
    return comm(tree(ws[:m]),tree(ws[m:]))
def substitute(word,images):
    ans=[]
    for a in word:ans=red(ans+(images[a-1] if a>0 else inv(images[-a-1])))
    return ans
def mm(a,b,p):
    A,B,C,D=a;E,F,G,H=b
    return ((A*E+B*G)%p,(A*F+B*H)%p,(C*E+D*G)%p,(C*F+D*H)%p)
def mi(a,p):
    A,B,C,D=a
    assert (A*D-B*C)%p==1
    return (D,-B%p,-C%p,A)
def evalw(word,ms,p):
    v=(1,0,0,1)
    for a in word:v=mm(v,ms[a-1] if a>0 else mi(ms[-a-1],p),p)
    return v

def main():
    raw=tree([[i] for i in range(1,15)])
    images=[[i] for i in range(1,14)]+[list(range(-13,0))]
    # The last list is e_13^{-1}...e_1^{-1}.
    word=substitute(raw,images)
    assert word
    for i in range(14):
        killed=[[j] if j!=i+1 else [] for j in range(1,15)]
        assert not substitute(raw,killed)
    rng=random.Random(20261116);p=101
    for trial in range(1,1001):
        ms=[]
        for _ in range(13):
            a,b,c=[rng.randrange(p) for j in range(3)]
            if a==0:a=1
            d=(1+b*c)*pow(a,-1,p)%p
            ms.append((a,b,c,d))
        value=evalw(word,ms,p)
        if value!=(1,0,0,1):break
    else:raise AssertionError('No nonidentity quotient value found')
    assert value!=(1,0,0,1)
    print('Formal commutator variables:',14)
    print('Raw length:',len(raw))
    print('Reduced length after e14=(e1...e13)^-1:',len(word))
    print('Kills to identity whenever any formal meridian is set to1:14/14 PASS')
    print('Nonempty free reduction: PASS')
    print('Finite certificate: SL(2,F_101), trial',trial)
    for i,m in enumerate(ms,1):print('e'+str(i),m)
    print('Value of word:',value)
    print('Nonidentity quotient certificate: PASS')
    out=Path(__file__).resolve().parents[1]/'data'
    out.mkdir(exist_ok=True)
    (out/'crossratio_common_kernel_word.txt').write_text(','.join(map(str,word))+'\n')
    print('Conclusion: (word,1) solves every paired cross-ratio equation.')
    print('This does not put its tetrahedral braid in the A5 centralizer.')

if __name__=='__main__':main()
