#!/usr/bin/env python3
"""Simultaneous noncentral lifts of the D38 cross-factor involution equations.

All arithmetic is over F5 and all groups are specified by exact cocycles.
No finite surviving coordinate is asserted to lift to the full GT_0.
"""
from itertools import product
from pathlib import Path
from collections import defaultdict, Counter
import json
import numpy as np
import a5_involution_quotient as a
import a5_schur_refinement as s


def rref(A, rhs=None):
    A = np.array(A,dtype=np.int64)%5
    n=A.shape[1]
    if rhs is not None:
        A=np.column_stack((A,np.array(rhs,dtype=np.int64)%5))
    row=0;piv=[]
    for col in range(n):
        inds=np.flatnonzero(A[row:,col])
        if len(inds)==0:continue
        k=row+int(inds[0]);A[[row,k]]=A[[k,row]]
        A[row]=A[row]*pow(int(A[row,col]),-1,5)%5
        multiples=A[:,col].copy();multiples[row]=0
        A=(A-multiples[:,None]*A[row][None,:])%5
        piv.append(col);row+=1
        if row==len(A):break
    if rhs is None:return A,piv
    if any(np.any(r[:n])==False and r[n]!=0 for r in A):
        return None,None,piv
    z=np.zeros(n,dtype=np.int64)
    for i,c in enumerate(piv):z[c]=A[i,n]
    free=[j for j in range(n) if j not in piv]
    B=np.zeros((n,len(free)),dtype=np.int64)
    for j,c in enumerate(free):
        B[c,j]=1
        for i,pc in enumerate(piv):B[pc,j]=-A[i,c]%5
    return z,B,piv


def main():
    pm,gl=s.aisomorphism()
    basis=((1,0,0,4),(0,1,0,0),(0,0,1,0))
    def adj(g):
        cols=[]
        for b in basis:
            v=s.conjugate(g,b);cols.append((v[0],v[1],v[2]))
        return np.array(cols,dtype=np.int64).T%5
    rep=[adj(pm[g]) for g in range(60)]
    cocdata=json.loads(Path(__file__).with_name('a5_cross_module_output.json').read_text())
    cc=[np.array(v,dtype=np.int64) for v in cocdata['selected_cocycle_values']]
    gg,hh=cocdata['triangle_generators']
    I3=np.eye(3,dtype=np.int64)

    pairs=[];lookup={}
    for x in range(60):
        for y in range(60):
            if (x,y) in lookup or a.generated(x,y)!=60:continue
            i=len(pairs);pairs.append((x,y))
            for gi,co in enumerate(a.CONJ):lookup[co[x],co[y]]=(i,gi)
    acts={
        'theta':[lookup[y,x] for x,y in pairs],
        'omega':[lookup[y,a.INV[a.MUL[x][y]]] for x,y in pairs],
        'delta':[lookup[a.INV[x],a.INV[y]] for x,y in pairs],
    }
    blockset={(6,8)};queue=[(6,8)]
    for i,j in queue:
        for name in ('theta','omega'):
            pair=(acts[name][i][0],acts[name][j][0])
            if pair not in blockset:blockset.add(pair);queue.append(pair)
    blocks=sorted(blockset);assert len(blocks)==6
    selected=sorted({i for pair in blocks for i in pair});assert len(selected)==9
    N=9*len(blocks);Id=np.eye(N,dtype=np.int64)
    qb=tuple(a.ID for _ in range(19))
    X=tuple(pairs[i][0] if i in selected else a.ID for i in range(19))
    Y=tuple(pairs[i][1] if i in selected else a.ID for i in range(19))
    def qm(q,r):return tuple(a.MUL[x][y] for x,y in zip(q,r))
    def qi(q):return tuple(a.INV[x] for x in q)
    def qa(name,q):return tuple(a.CONJ[gi][q[j]] for j,gi in acts[name])
    Z=qi(qm(X,Y));Xi=qi(X);Yi=qi(Y)
    assert qa('theta',X)==Y and qa('omega',X)==Y and qa('omega',Y)==Z
    def rho(q):
        R=np.zeros((N,N),dtype=np.int64)
        for k,(i,j) in enumerate(blocks):R[9*k:9*k+9,9*k:9*k+9]=np.kron(rep[q[i]],rep[q[j]])%5
        return R
    def beta(q,r):
        return np.concatenate([np.outer(cc[q[i]],rep[q[j]]@cc[r[j]]%5).ravel()%5
                               for i,j in blocks])

    corrections={}
    for name in ('theta','omega'):
        for i in selected:
            gi=acts[name][i][1]
            if gi in corrections:continue
            raw=adj(gl[gi]);co=a.CONJ[gi];found=[]
            for k in range(1,5):
                L=raw*k%5
                for bv in product(range(5),repeat=3):
                    b=np.array(bv,dtype=np.int64)
                    if all(np.array_equal(cc[co[g]],(L@cc[g]+(rep[co[g]]-I3)@b)%5)
                           for g in (gg,hh)):
                        found.append((k,L,b))
            assert len(found)==1
            k,L,b=found[0]
            assert all(np.array_equal(cc[co[g]],(L@cc[g]+(rep[co[g]]-I3)@b)%5)
                       for g in range(60))
            corrections[gi]=(L,b,k)

    Ls={}
    def J(name,q):
        out=[]
        for i,j in blocks:
            si,gi=acts[name][i];sj,gj=acts[name][j]
            Li,bi,_=corrections[gi];Lj,bj,_=corrections[gj]
            ci=Li@cc[q[si]]%5;cj=Lj@cc[q[sj]]%5
            aqj=a.CONJ[gj][q[sj]]
            rbj=rep[aqj]@bj%5
            B=np.outer(bi,cj)-np.outer(ci,rbj)+np.outer(bi,rbj-bj)
            out.append((-B).ravel()%5)
        return np.concatenate(out)
    for name in ('theta','omega'):
        L=np.zeros((N,N),dtype=np.int64)
        for k,(i,j) in enumerate(blocks):
            si,gi=acts[name][i];sj,gj=acts[name][j]
            l=blocks.index((si,sj))
            L[9*k:9*k+9,9*l:9*l+9]=np.kron(corrections[gi][0],corrections[gj][0])%5
        Ls[name]=L
    # Check the automorphism-cocycle identity on all pairs of named generators
    # and their inverses; the displayed cup/cochain formula proves it generally.
    sample=[qb,X,Y,Z,Xi,Yi,qi(Z)]
    for name,L in Ls.items():
        for q,r in product(sample,repeat=2):
            assert np.array_equal((L@beta(q,r)+J(name,qm(q,r)))%5,
                                  (J(name,q)+rho(qa(name,q))@J(name,r)+beta(qa(name,q),qa(name,r)))%5)

    RX,RY,RZ,RXi,RYi=map(rho,(X,Y,Z,Xi,Yi))
    Lt,Lw=Ls['theta'],Ls['omega']
    O=np.zeros((N,N),dtype=np.int64)
    A=np.block([[Lt,-Id,Id-RY,O],
                [-Id,Lt,Id-RX,O],
                [Lw,-Id,O,Id-RY],
                [RZ,Lw+RZ@RX,O,Id-RZ]])%5
    rhs=np.concatenate([-J('theta',X),-J('theta',Y),-J('omega',X),
                         -J('omega',Y)-RZ@(beta(X,Y)+beta(qm(X,Y),Z))])%5
    # Gauge the simultaneous inner M-conjugation of X,Y.
    inner=np.vstack((Id-RX,Id-RY))%5
    _,gauge=rref(inner.T);assert len(gauge)==N
    gauge_rows=np.zeros((N,4*N),dtype=np.int64)
    for i,j in enumerate(gauge):gauge_rows[i,j]=1
    A=np.vstack((A,gauge_rows));rhs=np.concatenate((rhs,np.zeros(N,dtype=np.int64)))
    base,variation,piv=rref(A,rhs)
    assert base is not None and variation.shape==(4*N,9)
    assert np.all((A@base-rhs)%5==0) and np.all(A@variation%5==0)

    # Exact D38 component propagation restricted to the nine selected factors.
    graph=defaultdict(list)
    allowed={i:{t for t in range(60) if a.MUL[t][t]==a.ID and
                    a.MUL[a.MUL[t][X[i]]][t]==a.INV[X[i]] and t not in (a.ID,X[i])}
             for i in selected}
    for i in selected:
        j,w=acts['omega'][i];k,th=acts['theta'][i]
        iw=a.inverse(a.S5[w]);forward={}
        for t in range(60):
            value=a.MUL[a.INV[Y[i]]][a.CONJ[th][t]]
            forward[t]=a.INDEX[a.multiply(a.multiply(iw,a.A5[value]),a.S5[w])]
        graph[k].append((j,forward));graph[j].append((k,{v:u for u,v in forward.items()}))
    used=set();components=[];solutions=[]
    for root in selected:
        if root in used:continue
        comp={root};queue=[root]
        for v in queue:
            for w,_ in graph[v]:
                if w not in comp:comp.add(w);queue.append(w)
        used|=comp;ss=[]
        for value in sorted(allowed[root]):
            d={root:value};pending=[root];ok=True
            for v in pending:
                for w,fn in graph[v]:
                    z=fn[d[v]]
                    if z not in allowed[w] or (w in d and d[w]!=z):ok=False;break
                    if w not in d:d[w]=z;pending.append(w)
                if not ok:break
            if ok:ss.append(d)
        components.append(sorted(comp));solutions.append(ss)
    assert np.prod([len(ss) for ss in solutions])==300
    dt=tuple(a.INDEX[a.S5[gi]] for j,gi in acts['delta'])
    unitallowed={}
    for mu in (1,7,11,13,17,19,23,29):
        sign=0 if mu%5 in (1,4) else 1
        unitallowed[mu]={i:{a.CONJ[gi][dt[i]] for gi,g in enumerate(a.S5)
                             if a.parity(g)==sign and a.CONJ[gi][X[i]]==a.power(X[i],mu)}
                         for i in selected}
    stats=Counter();rows=[];direct_checks=0
    def emul(A,B):
        q,v=A;r,w=B
        return qm(q,r),(v+rho(q)@w+beta(q,r))%5
    def einv(A):
        q,v=A;r=qi(q)
        return r,(-rho(r)@(v+beta(q,r)))%5
    def eq(A,B):return A[0]==B[0] and np.array_equal(A[1]%5,B[1]%5)
    neutral=(qb,np.zeros(N,dtype=np.int64))
    for number,choices in enumerate(product(*solutions),1):
        tv=list(qb)
        for choice in choices:
            for i,v in choice.items():tv[i]=v
        t=tuple(tv);tht=qa('theta',t);wt=qa('omega',t)
        assert wt==qm(Yi,tht)
        Rt=rho(t);Rth=rho(tht);Rw=rho(wt)
        C=np.block([[O,O,O,O],
                    [Rt+RXi,O,O,O],
                    [O,RYi,-RYi@(Id-Rth),Id-Rw]])%5
        D=np.vstack((Id+Rt,Id-RXi,Lw-RYi@Lt))%5
        target=np.concatenate((-beta(t,t),
            -beta(t,X)-RXi@beta(X,Xi)+beta(Xi,t),
            -J('omega',t)+RYi@J('theta',t)-RYi@beta(Y,Yi)+beta(Yi,tht)))%5
        small=np.column_stack((C@variation,D))%5
        target=(target-C@base)%5
        particular,kernel,piv=rref(small,target)
        mus=[mu for mu in unitallowed if all(t[i] in unitallowed[mu][i] for i in selected)]
        kind='D38_conjugate' if mus else 'D38_nonconjugate'
        if particular is None:
            stats[(kind,'excluded')]+=1;dimension=None
        else:
            dimension=kernel.shape[1]
            assert np.all((small@particular-target)%5==0) and np.all(small@kernel%5==0)
            stats[(kind,'survives')]+=1
            data=(base+variation@particular[:9])%5
            xv,yv,bt,bw=np.split(data,4)
            EE=(X,xv);FF=(Y,yv);TT=(t,particular[9:])
            def aut(name,A):
                q,v=A;aq=qa(name,q);b=bt if name=='theta' else bw
                return aq,(Ls[name]@v+J(name,q)+(Id-rho(aq))@b)%5
            assert eq(aut('theta',EE),FF) and eq(aut('theta',FF),EE)
            assert eq(aut('omega',EE),FF)
            ZZ=einv(emul(EE,FF));assert eq(aut('omega',FF),ZZ)
            assert eq(emul(TT,TT),neutral)
            assert eq(emul(emul(TT,EE),einv(TT)),einv(EE))
            assert eq(aut('omega',TT),emul(einv(FF),aut('theta',TT)))
            f=emul(aut('theta',TT),einv(TT))
            assert eq(emul(aut('theta',f),f),neutral)
            assert eq(emul(f,emul(emul(TT,f),einv(TT))),neutral)
            ii=neutral
            for term in (aut('omega',aut('omega',f)),einv(ZZ),aut('omega',f),einv(FF),f,einv(EE)):
                ii=emul(ii,term)
            assert eq(ii,neutral)
            direct_checks+=1
        rows.append({'t_on_selected_factors':[t[i] for i in selected],
                     'finite_pure_conjugator_units':mus,'lift_affine_dimension':dimension,
                     'lift_kernel_parameter_dimension':None if kernel is None else len(rref(kernel[:9,:])[1])})
        if number%25==0:print('checked',number,dict(stats),flush=True)
    out={
        'module_pairs':blocks,'selected_A5_factors':selected,'module_dimension':N,
        'base_Q_factors':len(selected),'base_group_order':60**len(selected),
        'extension_kernel_order':5**N,'extension_group_order':60**len(selected)*5**N,
        'cohomology_corrections':{str(gi):{'scalar':k,'coboundary':b.tolist()}
                                  for gi,(L,b,k) in corrections.items()},
        'theta_omega_lift_kernel_affine_dimension':variation.shape[1],
        'triangle_component_indices':components,'triangle_component_counts':[len(s) for s in solutions],
        'base_tuples_checked':len(rows),
        'direct_group_equation_checks':direct_checks,
        'simultaneous_lift_counts':{' / '.join(k):v for k,v in stats.items()},
        'lift_dimension_histogram':dict(Counter(str(r['lift_affine_dimension']) for r in rows)),
        'lift_kernel_parameter_dimension_histogram':dict(Counter(str(r['lift_kernel_parameter_dimension']) for r in rows)),
        'tuples':rows,
        'scope':'Exact simultaneous finite theta, omega, norm, and x-inversion lift equations in the named nonsplit cross-module quotient. No surviving finite coordinate is asserted to lift to the full GT_0.'
    }
    Path(__file__).with_name('a5_cross_peripheral_lifts_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('tuples','cohomology_corrections')},indent=2))


if __name__=='__main__':main()
