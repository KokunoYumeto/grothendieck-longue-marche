"""Exact finite-word membership in the certified rigid-seven kernel.

Input: a JSON array of signed indices in the geometric basis e1,...,e13.
Example: python membership_rigid7.py '[6,11,-6,-5]'

The thirteen braid images are in all13_braid_words.json. Their geometric
certification is the separate all13_exact_certificate.json and its script.
A pure six-strand braid dies on the seven-puncture sphere precisely when
it is an integral power of the central full twist. Artin's faithful action
and the exponent sum give an exact membership algorithm. Word growth in
the free-group action can be large; no polynomial complexity is claimed.
"""
from pathlib import Path
import argparse
import itertools
import json

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'all13_braid_words.json').read_text())
BRAIDS={row['index']:tuple(row['word']) for row in DATA['basis']}

def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)
def inverse(w):return tuple(-a for a in reversed(w))
def multiply(*ws):return reduce_word(itertools.chain.from_iterable(ws))
def substitute(w,images):
    return multiply(*(images[a] if a>0 else inverse(images[-a]) for a in w))
def artin(w,n=6):
    images=[(j+1,) for j in range(n)]
    for a in w:
        j=abs(a)-1;u,v=images[j:j+2]
        images[j:j+2]=[multiply(u,v,inverse(u)),u] if a>0 else [v,multiply(inverse(v),u,v)]
    return tuple(images)
def exponent(w):return sum(1 if a>0 else -1 for a in w)
def central_braid(w):
    total=exponent(w)
    if total%30:
        return {'central':False,'reason':'exponent sum is not divisible by30','exponent_sum':total}
    m=total//30
    boundary=tuple(range(1,7))
    conjugator=(boundary if m>=0 else inverse(boundary))*abs(m)
    expected=tuple(multiply(conjugator,(j,),inverse(conjugator)) for j in range(1,7))
    actual=artin(w)
    return {'central':actual==expected,'reason':'exact faithful Artin action comparison',
            'exponent_sum':total,'candidate_full_twist_power':m,
            'artin_image_lengths':[len(x) for x in actual]}
def in_kernel(source_word):
    assert all(isinstance(a,int) and 1<=abs(a)<=13 for a in source_word)
    w=substitute(source_word,BRAIDS)
    total=exponent(w)
    if total:
        return {'source_word':list(source_word),'braid_length':len(w),
                'central':False,'reason':'normalized fixed-pair linking forces any central power to be zero',
                'exponent_sum':total}
    return {'source_word':list(source_word),'braid_length':len(w),**central_braid(w)}
def balanced_commutator(ws):
    if len(ws)==1:return ws[0]
    m=len(ws)//2
    a=balanced_commutator(ws[:m]);b=balanced_commutator(ws[m:])
    return multiply(a,b,inverse(a),inverse(b))

def self_test():
    full_twist=(1,2,3,4,5)*6
    assert central_braid(full_twist)['central']
    assert central_braid(inverse(full_twist))['central']
    assert central_braid(full_twist*2)['central']
    assert not central_braid((3,3))['central']
    h=(6,11,-6,-5)
    assert in_kernel(h)['central']
    print('Full-twist convention and faithful Artin center check: PASS')
    print('h=e6 e11 e6^-1 e5^-1:',json.dumps(in_kernel(h)))
    for i in range(1,14):
        ans=in_kernel([i])
        assert not ans['central']
        print('basis',i,':',json.dumps(ans))
    infinity=tuple(range(-13,0))
    assert not in_kernel(infinity)['central']
    print('infinity meridian:',json.dumps(in_kernel(infinity)))
    formal=balanced_commutator([(i,) for i in range(1,15)])
    source_images={i:(i,) for i in range(1,14)}
    source_images[14]=infinity
    w=substitute(formal,source_images)
    k=multiply(h,w,inverse(h),inverse(w))
    assert w and k
    assert all(sum(1 if a==i else -1 if a==-i else 0 for a in w)==0 for i in range(1,14))
    for j in range(1,15):
        killed={i:() if i==j else (i,) for i in range(1,15)}
        assert not substitute(formal,killed)
    (HERE/'all13_source_words.json').write_text(json.dumps({'h':h,'w':w,'k':k,'infinity':infinity},indent=2)+'\n')
    print('Geometric-basis source words: h length',len(h),'; w length',len(w),'; k length',len(k))
    print('w dies on deleting any of14 formal meridians; w and k have nonempty exact free reductions: PASS')
    print('No Artin expansion of the long w/k words is claimed by this self-test.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('word',nargs='?',help='JSON array of signed source generator indices')
    args=parser.parse_args()
    if args.word is None:self_test()
    else:print(json.dumps(in_kernel(json.loads(args.word)),indent=2))
