#!/usr/bin/env python3
"""One actual Z/8 continuation preserving the entire degree-eight action."""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import chain
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):H=runpy.run_path(str(OUT/'d_cm_degree8_stable.py'))
R=H['R'];pairs=H['pairs'];d=97;cdim=4753
ii=np.array([i for i,j in pairs]);jj=np.array([j for i,j in pairs]);diag=ii==jj
one,qs,qr,qr2,qm,ix=(R[k] for k in ('one','qs','qr','qr2','qm','ixQ'))
ch={j:i for i,j in enumerate(R['chN'])};Nwords=R['Nwords']
def inverse(w):return bytes(0 if a==0 else 3-a for a in reversed(w))
def inviter(w):return (0 if a==0 else 3-a for a in reversed(w))
def bits(v):return int.from_bytes(np.packbits(np.asarray(v%2,dtype=np.uint8),bitorder='little').tobytes(),'little')
def evaluate(word,mod=8,startq=one,collapse=False):
    q=startq;nw=[];v=np.zeros(d,dtype=np.int16);w=np.zeros((d,d),dtype=np.int16)
    def append(edge,sign):
        i=ch.get(edge)
        if i is None:return
        a=sign*(i+1)
        if nw and nw[-1]==-a:nw.pop()
        else:nw.append(a)
    for a in word:
        if a==0:q=qm(q,qs)
        else:
            qq=qm(q,qr if a==1 else qr2);append(ix[q],1);append(ix[qq],-1);q=qq
    for a in nw:
        i=abs(a)-1;sgn=1 if a>0 else -1
        w[:,i]=(w[:,i]+sgn*v)%mod
        if sgn<0:w[i,i]=(w[i,i]+1)%mod
        v[i]=(v[i]+sgn)%mod
    return q,v,w,len(nw)
from d_cm_degree8_reconstruct import joint_words
JW=joint_words(R);beta,A,lam=(JW[k] for k in ('beta','A','lambda'))
def cusp(b,a,ll):return chain(b,[0],inviter(b),a,[1],inviter(a),[2,0]*ll)
q,v,w,nlength=evaluate(cusp(beta,A,lam))
assert q==one and not np.any(v) and not np.any(w%4) and np.array_equal(w,w.T)
target=bits(w[ii,jj]//4)
print('Exact initial Z8 cusp target:',target.bit_count(),'coordinates;',nlength,'N letters',flush=True)

q,v288,w288,_=evaluate([0,1]*288)
assert q==one and not np.any(v288) and not np.any(w288%4)
c2=bits(w288[ii,jj]//4)
columns=H['F1']+H['F2']+[c2]
bas=R['echelon'](columns);assert len(bas)==4738
duals=[]
for j in range(cdim):
    if j in bas:continue
    e=1<<j
    for k in sorted(bas):
        if (e&bas[k][0]).bit_count()%2:e^=1<<k
    assert all(not ((e&b[0]).bit_count()%2) for b in bas.values());duals.append(e)
assert len(duals)==15
ob=sum(((e&target).bit_count()%2)<<i for i,e in enumerate(duals))
BJ=json.loads((OUT/'d_cm_degree8_stable.json').read_text())['basis_certificates']
bb={int(k):(v['image'],int(v['new_high_basis_relation'],16)) for k,v in BJ.items()}
good,z,rem=R['solve'](ob,bb);assert good and not rem

# Exact C2=(Z/4)^4753 action, using the same actual retained G2 data.
J=json.loads((OUT/'d_cm_quadratic_search.json').read_text())['witness']
def nword(mask):
    ans=[]
    while mask:
        bit=mask&-mask;ans+=Nwords[bit.bit_length()-1];mask^=bit
    return ans
qb=R['D']['canon'](tuple(J['beta']))
short=nword(int(J['homology_beta_cycles'],16))+R['reps'][qb]
fixed=json.loads((OUT/'d_cm_class2_two.json').read_text())['s_centralizer_basis']
right=int(J['beta_right_s_centralizer_coefficients'],16)
for j,vv in enumerate(fixed):
    if (right>>j)&1:short+=nword(int(vv,16))
sw=short+[0]+list(inverse(short));tw=[0,1]
NJ=json.loads((OUT/'d_cm_degree8_high.json').read_text())
new=NJ['actual_Nielsen_basis_B_words'];hp=NJ['high_C1_pairs']
def data(g,qexpected):
    q,vg,_,_=evaluate(g,4);assert q==qexpected
    M=[];W=[]
    for ww in new:
        q,v,z,_=evaluate(ww,4,startq=qexpected);assert q==qexpected
        z=(z+np.outer(vg,v)-np.outer(v,vg))%4
        M.append(v);W.append(z)
    return np.stack(M,axis=1),np.stack(W)
AD=data([],one);AS=data(sw,qs);AT=data(tw,qm(qs,qr))
def column(i,j,D):
    M,W=D
    if i==j:C=(2*W[i]+3*np.outer(M[:,i],M[:,i]))%4
    else:C=(np.outer(M[:,i],M[:,j])-np.outer(M[:,j],M[:,i]))%4
    ans=C[ii,jj].copy();ans[diag]=3*ans[diag]%4
    return ans
c=np.array([2*((target>>i)&1) for i in range(cdim)],dtype=np.int64)
for j in range(9416):
    if (z>>j)&1:
        i,k=hp[j%4708]
        sc=column(i,k,AS)
        c+=column(i,k,AD)-sc if j<4708 else sc-column(i,k,AT)
c%=4;assert not np.any(c%2)
good,up,rem=R['solve'](bits(c//2),bas);assert good and not rem

def comm(a,b):return a+b+inverse(a)+inverse(b)
def correction(mask,words,pp,power):
    ans=bytearray();words=[bytes(w) for w in words]
    while mask:
        bit=mask&-mask;i,j=pp[bit.bit_length()-1]
        ans.extend((words[i]*2 if i==j else comm(words[i],words[j]))*power);mask^=bit
    return bytes(ans)
m=(1<<cdim)-1;hm=(1<<4708)-1
bcor=correction(up&m,Nwords,pairs,4)+correction(z&hm,new,hp,2)
acor=correction((up>>cdim)&m,Nwords,pairs,4)+correction(z>>4708,new,hp,2)
ll=lam+288*(up>>(2*cdim));b=bcor+beta;a=acor+A
q,v,w,finalN=evaluate(cusp(b,a,ll));assert q==one and not np.any(v) and not np.any(w)
for cw in (bcor,acor,bytes([0,1]*288)):
    q,kw=R['collapse'](cw);assert q==R['e']
    assert all(not p.any() for p in R['poly'](kw,8)[1:])
summary={'restricted_Bockstein_rank':15,'upper_image_rank':len(bas),
 'initial_Z8_target_support':target.bit_count(),'initial_N_cusp_word_length':nlength,
 'full_corrected_Z8_identity_checked':True,
 'degree8_action_retained_exactly':True,
 'lower_word_K_degree_at_least':10,'upper_word_K_degree_at_least':16,
 'upper_multiplier288_in_D16_K':True,'lambda':ll,
 'corrected_B_cusp_word_length':2*(len(a)+len(b))+2+2*ll,
 'corrected_N_cusp_word_length':finalN,'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_stable_word.json').write_text(json.dumps({'summary':summary,
 'witness':{'lower_high_beta':hex(z&hm),'lower_high_A':hex(z>>4708),
 'upper_beta':hex(up&m),'upper_A':hex((up>>cdim)&m),
 'upper_multiplier288':up>>(2*cdim)}},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
