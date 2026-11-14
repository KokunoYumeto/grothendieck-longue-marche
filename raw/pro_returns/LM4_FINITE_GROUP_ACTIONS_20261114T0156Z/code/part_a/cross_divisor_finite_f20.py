#!/usr/bin/env python3
"""Exact F20 finite source-action tests, using only the geometric certificate.

No numerical braid discovery file is read.  Group and module computations
are exact.  The assertions concern the specified finite quotient maps.
"""
from pathlib import Path
from itertools import permutations, combinations
from collections import deque, Counter
from functools import lru_cache
import json
import numpy as np
import cross_divisor_monodromy_f20 as geometry
nf=geometry.nf

def group_table(name):
    degree=int(name[1:]);even=name[0]=='A'
    elements=[]
    for p in permutations(range(degree)):
        parity=sum(p[i]>p[j] for i in range(degree) for j in range(i+1,degree))%2
        if not even or not parity:elements.append(p)
    index={p:i for i,p in enumerate(elements)};n=len(elements)
    mul=np.empty((n,n),dtype=np.int16)
    for i,p in enumerate(elements):
        for j,q in enumerate(elements):mul[i,j]=index[tuple(p[q[k]] for k in range(degree))]
    inverse=np.array([next(j for j in range(n) if mul[i,j]==0) for i in range(n)],dtype=np.int16)
    return elements,mul,inverse

def evaluation(word,triples,mul,inverse):
    value=np.zeros(len(triples),dtype=np.int16)
    for a in word:
        b=triples[:,abs(a)-1]
        if a<0:b=inverse[b]
        value=mul[value,b]
    return value

def generating_triples(n,mul,inverse):
    @lru_cache(None)
    def adjoin(mask,x):
        members=[i for i in range(n) if mask>>i&1]
        gens=members+[x,int(inverse[x])]
        seen=set(members);stack=members[:]
        while stack:
            a=stack.pop()
            for b in gens:
                c=int(mul[a,b])
                if c not in seen:seen.add(c);stack.append(c)
        return sum(1<<i for i in seen)
    pairs=[[adjoin(adjoin(1,a),b) for b in range(n)] for a in range(n)]
    full=(1<<n)-1
    values=[(a,b,c) for a in range(n) for b in range(n) for c in range(n)
            if adjoin(pairs[a][b],c)==full]
    return np.array(values,dtype=np.int16)

def orbit_sizes(perms):
    n=perms.shape[1];seen=np.zeros(n,dtype=bool);sizes=[]
    for seed in range(n):
        if seen[seed]:continue
        seen[seed]=True;frontier=np.array([seed],dtype=np.int32);size=1
        while len(frontier):
            targets=np.unique(perms[:,frontier].reshape(-1))
            frontier=targets[~seen[targets]]
            seen[frontier]=True;size+=len(frontier)
        sizes.append(int(size))
    return sorted(sizes)

class LinearSpan:
    def __init__(self, dimension, p):
        self.dimension=dimension; self.p=p; self.rows={}

    def reduce(self, vector):
        v=np.array(vector,dtype=np.int64,copy=True)%self.p
        for pivot,row in sorted(self.rows.items()):
            if v[pivot]: v=(v-v[pivot]*row)%self.p
        return v

    def add(self, vector):
        v=self.reduce(vector)
        inds=np.flatnonzero(v)
        if not len(inds): return False
        pivot=int(inds[0]);v=v*pow(int(v[pivot]),-1,self.p)%self.p
        for old,row in list(self.rows.items()):
            if row[pivot]:self.rows[old]=(row-row[pivot]*v)%self.p
        self.rows[pivot]=v
        return True

    def basis(self): return [v for k,v in sorted(self.rows.items())]
    def __len__(self): return len(self.rows)

def closure(gens,mul,iv):
    found={0};todo=[0]
    gg=list(gens)+[int(iv[a]) for a in gens]
    for a in todo:
        for b in gg:
            c=int(mul[a,b])
            if c not in found:found.add(c);todo.append(c)
    return found

class Quotient:
    def __init__(self,mul,iv,aut,triple,p):
        self.mul=mul;self.iv=iv;self.aut=aut;self.gen=list(triple);self.p=p
        self.n=len(mul);self.dim=3*self.n
        self.shifts=np.array([[i*self.n+int(mul[a,j]) for i in range(3) for j in range(self.n)] for a in range(self.n)])
        self.identity=(np.zeros(self.dim,dtype=np.int64),0)

    def shift(self,v,a):
        out=np.zeros_like(v);out[self.shifts[a]]=v;return out

    def times(self,x,y):
        v,a=x;w,b=y
        return (v+self.shift(w,a))%self.p,int(self.mul[a,b])

    def inverse(self,x):
        v,a=x;b=int(self.iv[a]);return -self.shift(v,b)%self.p,b

    def word(self,w):
        v=np.zeros(self.dim,dtype=np.int64);a=0
        for letter in w:
            i=abs(letter)-1
            if letter>0:v[i*self.n+a]+=1;a=int(self.mul[a,self.gen[i]])
            else:a=int(self.mul[a,self.iv[self.gen[i]]]);v[i*self.n+a]-=1
        return v%self.p,a

    def action(self,row):
        images=[self.word(w) for w in row['old']['base_automorphism']]
        target=np.array([a for v,a in images])
        indices=np.flatnonzero(np.all(self.aut[:,self.gen]==target,axis=1));assert len(indices)==1
        sigma=self.aut[int(indices[0])]
        j=np.column_stack([self.shift(images[i][0],int(sigma[a])) for i in range(3) for a in range(self.n)])%self.p
        vp,ap=self.word(row['old']['conjugator']);vq,aq=self.word(row['new']['conjugator'])
        ip=int(self.iv[ap]);iq=int(self.iv[aq])
        la=np.column_stack([self.shift(j[:,i],iq) for i in range(self.dim)])
        ls=np.column_stack([self.shift(j[:,i],ip) for i in range(self.dim)])
        def affine(x):
            v,a=x;b=int(self.mul[iq,sigma[a]])
            return (la@v-self.shift(vq,iq)+self.shift(vp,b))%self.p,int(self.mul[b,ap])
        def psi(x):
            v,a=x;b=int(self.mul[ip,sigma[a]])
            return (ls@v-self.shift(vp,ip)+self.shift(vp,b))%self.p,int(self.mul[b,ap])
        return affine,psi,ls

    def subgroup(self,gens):
        selected=[];base={0}
        for g in gens:
            if g[1] not in base:
                selected.append(g);base=closure([x[1] for x in selected],self.mul,self.iv)
        reps={0:self.identity};todo=deque([0])
        while todo:
            a=todo.popleft()
            for g in selected:
                z=self.times(reps[a],g)
                if z[1] not in reps:reps[z[1]]=z;todo.append(z[1])
        assert set(reps)==base
        span=LinearSpan(self.dim,self.p)
        for v,a in gens:span.add(v-reps[a][0])
        for r in reps.values():
            for g in selected:
                z=self.times(r,g);span.add(z[0]-reps[z[1]][0])
        while True:
            before=len(span)
            for v in span.basis():
                for _,a in selected:span.add(self.shift(v,a))
            if len(span)==before:break
        return reps,span

    def boundary(self,v):
        out=np.zeros(self.n,dtype=np.int64)
        for i in range(3):
            w=v[i*self.n:(i+1)*self.n]
            out[self.mul[:,self.gen[i]]]+=w;out-=w
        return out%self.p

    def validate(self,x):
        v,a=x;t=np.zeros(self.n,dtype=np.int64);t[a]+=1;t[0]-=1
        assert np.array_equal(self.boundary(v),t%self.p)

def quotient_orbit(q,rows,limit):
    actions=[q.action(r) for r in rows]
    # Check the semilinear substitution on deterministic source words.
    inv,red,subst=nf.wi,nf.red,nf.substitute
    words=[[1],[2],[3],[1,2,-1,3,-2],[3,1,-3,2,1,-2]]
    for row,(affine,psi,mat) in zip(rows,actions):
        p=row['old']['conjugator'];qq=row['new']['conjugator'];alpha=row['old']['base_automorphism']
        for w in words:
            x=affine(q.word(w));y=q.word(inv(qq)+subst(w,alpha)+p)
            assert x[1]==y[1] and np.array_equal(x[0],y[0])
            x=psi(q.word(w));y=q.word(inv(p)+subst(w,alpha)+p)
            assert x[1]==y[1] and np.array_equal(x[0],y[0])
    gens=[q.word(r['old']['conjugator']) for r in rows if r['old']['base_automorphism']==[[1],[2],[3]] and not r['new']['conjugator']]
    history=[]
    while True:
        reps,span=q.subgroup(gens)
        history.append({'base_order':len(reps),'kernel_dimension':len(span)})
        added=[]
        for affine,psi,mat in actions:
            added.extend(psi(x) for x in reps.values())
            if len(span):
                images=(mat@np.column_stack(span.basis()))%q.p
                added.extend((images[:,i],0) for i in range(images.shape[1]))
        stable=True
        for v,a in added:
            if a not in reps or np.any(span.reduce(v-reps[a][0])):stable=False;break
        if stable:break
        gens=list(reps.values())+[(v,0) for v in span.basis()]+added
    for x in reps.values():q.validate(x)
    for v in span.basis():q.validate((v,0))
    canonical_base={a:min(int(q.mul[a,b]) for b in reps) for a in range(q.n)}
    spans={}
    for a in set(canonical_base.values()):
        ss=LinearSpan(q.dim,q.p)
        for v in span.basis():ss.add(q.shift(v,a))
        spans[a]=ss
    def canonical(x):
        v,a=x;a0=canonical_base[a];b=int(q.mul[q.iv[a],a0])
        vv=(v+q.shift(reps[b][0],a))%q.p
        return spans[a0].reduce(vv),a0
    def key(x):return x[1],tuple(map(int,x[0]))
    codim=2*q.n+1-len(span);expected=(q.n//len(reps))*q.p**codim
    start=canonical(q.identity);seen={key(start)};todo=deque([start])
    while todo and len(seen)<limit:
        x=todo.popleft()
        for affine,psi,mat in actions:
            y=canonical(affine(x));kk=key(y)
            if kk not in seen:seen.add(kk);todo.append(y)
    return {'right_subgroup_history':history,'kernel_codimension':codim,'right_coset_count':expected,
            'orbit_reached':len(seen),'orbit_complete':not todo,'transitive':len(seen)==expected,
            'semilinear_word_checks':2*len(rows)*len(words)}


def main():
    certificate=json.loads(Path(__file__).with_name('cross_divisor_monodromy_f20_output.json').read_text())
    assert certificate['source_generator_count']==11 and certificate['certified_crossings']==172
    rows=certificate['pairs']
    signs_before=nf.SIGN_COUNT
    s0=nf.C(0,nf.THETA**2-2)*nf.ZETA;square=s0*s0
    assert (s0*s0.conjugate()).re==nf.THETA**2-1
    assert ((s0*s0.conjugate()).re-1).sign()>0
    assert (3*s0.re+2).sign()<0
    assert (3*s0.im+6-6).sign()>0
    radial=[]
    for j,u in enumerate(nf.ROOTS):
        if j==1:continue
        aa=u*(2*nf.ZETA-u);cross=(aa*square.conjugate()).im
        ss=cross.sign();assert ss
        assert (9-(aa*aa.conjugate()).re).sign()>0
        radial.append({'root_exponent':j,'cross_product':cross.encoded(),'sign':ss})
    newpoint=geometry.point_at_base(False);direction=newpoint-geometry.REFERENCE
    old_avoidance=[]
    for j,u in enumerate(nf.ROOTS):
        value=(u-geometry.BASE)*geometry.cinv(u+geometry.BASE);value=value*value
        cross=((value-geometry.REFERENCE)*direction.conjugate()).im;ss=cross.sign();assert ss
        old_avoidance.append({'root_exponent':j,'cross_product':cross.encoded(),'sign':ss})
    basepoint_checks={'vertices':[x.encoded() for x in [s0,3*s0,3*s0+nf.C(0,6),nf.C(6,6),geometry.BASE]],
                      'outer_root_radial_clearance':radial,'new_transport_old_point_avoidance':old_avoidance,
                      'exact_number_field_sign_checks':nf.SIGN_COUNT-signs_before}
    filled=[i for i,r in enumerate(rows) if r['old']['base_automorphism']==[[1],[2],[3]] and not r['new']['conjugator']]
    assert filled==[1,3,4,5,6,8,9,10]
    base_braids=[]
    for row in rows:
        labels=list(range(4));word=[]
        for letter in row['old']['braid']:
            i=abs(letter)-1;a,b=labels[i],labels[i+1]
            if a!=3 and b!=3:
                j=sum(x!=3 for x in labels[:i])+1
                word.append(j if letter>0 else -j)
            labels[i],labels[i+1]=labels[i+1],labels[i]
        word=nf.red(word);assert nf.artin(word,n=3)==row['old']['base_automorphism']
        base_braids.append(word)
    assert base_braids==[[1,1,-2,-2,-1,-1],[],[-1,-1,-1,-1],[],[],[],[],[1,1,2,2,1,1,2,2],[],[],[]]
    perimeter=[1,2,3];k=perimeter+[1,2,1];t=perimeter+[1,2,-1]
    expected_p=[nf.red([1,2,1,-2,-1]+nf.wi(perimeter)),[-1,-1],[],[],
                nf.red(k+[-2]+nf.wi(k)),[],perimeter+perimeter,nf.red(t+[-3,-1]),[],[1,-2,-1],[]]
    expected_q=[[-3,1,-2,-1],[],[-2,-1],[],[],[],[],t,[],[],[]]
    assert [r['old']['conjugator'] for r in rows]==expected_p
    assert [r['new']['conjugator'] for r in rows]==expected_q
    kernel_images=[]
    for i in range(1,4):
        prefix=list(range(3,i,-1));word=prefix+[i,i]+nf.wi(prefix)
        v=nf.artin(word,n=4)[3];conjugator=[]
        while len(v)>1 and v[0]==-v[-1]:conjugator.append(v[0]);v=v[1:-1]
        assert v==[4]
        kernel_images.append(nf.wi(nf.red([a for a in conjugator if abs(a)!=4])))
    assert kernel_images==[[-3,-2,-1,2,3],[-3,-2,3],[-3]]
    assert [nf.substitute(w,kernel_images) for w in kernel_images]==[[1],[2],[3]]
    elements,mul,iv=group_table('A5');n=len(elements);element_index={p:i for i,p in enumerate(elements)}
    aut=[]
    for a in permutations(range(5)):
        ia=tuple(a.index(i) for i in range(5))
        aut.append([element_index[tuple(a[x[ia[j]]] for j in range(5))] for x in elements])
    aut=np.array(aut,dtype=np.int16)
    conjugacy_classes=[];unseen=set(range(n))
    while unseen:
        a=min(unseen);cc={int(mul[mul[g,a],iv[g]]) for g in range(n)}
        conjugacy_classes.append(cc);unseen-=cc
    class_sizes=sorted(map(len,conjugacy_classes));assert class_sizes==[1,12,12,15,20]
    nonidentity_sizes=[len(c) for c in conjugacy_classes if 0 not in c]
    normal_union_orders=[]
    for mask in range(1,2**len(nonidentity_sizes)-1):
        size=1+sum(s for i,s in enumerate(nonidentity_sizes) if (mask>>i)&1)
        if n%size==0:normal_union_orders.append(size)
    assert not normal_union_orders
    triples=generating_triples(n,mul,iv);count=len(triples)
    full_index=np.full(n**3,-1,dtype=np.int32)
    codes=triples[:,0].astype(np.int32)*n*n+triples[:,1].astype(np.int32)*n+triples[:,2]
    full_index[codes]=np.arange(count,dtype=np.int32)
    factor=np.full(count,-1,dtype=np.int32);reps=[]
    for i in range(count):
        if factor[i]>=0:continue
        tt=aut[:,triples[i]]
        ids=full_index[tt[:,0].astype(np.int32)*n*n+tt[:,1].astype(np.int32)*n+tt[:,2]]
        assert len(set(map(int,ids)))==120
        factor[ids]=len(reps);reps.append(i)
    reptriples=triples[reps]
    factor_actions=[]
    for row in rows:
        tt=np.column_stack([evaluation(w,reptriples,mul,iv) for w in row['old']['base_automorphism']])
        ids=full_index[tt[:,0].astype(np.int32)*n*n+tt[:,1].astype(np.int32)*n+tt[:,2]]
        assert np.all(ids>=0)
        perm=factor[ids];assert len(set(map(int,perm)))==len(reps)
        factor_actions.append(perm)
    stable=[i for i in range(len(reps)) if all(int(a[i])==i for a in factor_actions)]
    singles=[];permutations_by_factor=[];nonfilled=[]
    for index in stable:
        triple=list(map(int,reptriples[index]));t=np.array([triple],dtype=np.int16);pp=[];descent=[]
        for row in rows:
            target=np.array([int(evaluation(w,t,mul,iv)[0]) for w in row['old']['base_automorphism']])
            sigma_index=np.flatnonzero(np.all(aut[:,triple]==target,axis=1));assert len(sigma_index)==1
            sigma=aut[int(sigma_index[0])]
            p=int(evaluation(row['old']['conjugator'],t,mul,iv)[0])
            q=int(evaluation(row['new']['conjugator'],t,mul,iv)[0])
            pp.append(mul[iv[q],mul[sigma,p]])
            descent.append({'automorphism_index':int(sigma_index[0]),'old_word_value':p,'new_word_value':q})
        pp=np.array(pp,dtype=np.int16);sizes=orbit_sizes(pp);assert sizes==[60]
        singles.append({'factor':index,'triple':triple,'triple_permutations':[elements[a] for a in triple],
                        'source_generator_descent':descent,'orbit_sizes':sizes})
        permutations_by_factor.append(pp)
        fourth=int(mul[mul[triple[0],triple[1]],triple[2]])
        if all(triple) and fourth:nonfilled.append((index,triple))
    pair_histogram=Counter();pair_count=0
    for i,j in combinations(range(len(stable)),2):
        pp=(permutations_by_factor[i][:,:,None].astype(np.int32)*n+
            permutations_by_factor[j][:,None,:]).reshape(len(rows),n*n)
        sizes=orbit_sizes(pp);assert sizes==[3600]
        pair_histogram[tuple(sizes)]+=1;pair_count+=1
    print(json.dumps({'stage':'A5 factors and paired factors','epimorphism_triples':count,
                      'factor_count':len(reps),'stable_factors':len(stable),'paired_quotients':pair_count}),flush=True)
    covers=[]
    for index,triple in nonfilled:
        quotient=Quotient(mul,iv,aut,triple,2)
        result=quotient_orbit(quotient,rows,100000)
        assert result['kernel_codimension']==2 and result['right_coset_count']==4
        assert result['transitive'] and result['orbit_complete']
        assert result['right_subgroup_history'][-1]=={'base_order':60,'kernel_dimension':119}
        result.update({'factor':index,'triple':triple,'cover_order':60*2**121})
        covers.append(result);print(json.dumps({'stage':'noncentral homology cover',**result}),flush=True)
    assert count==200160 and len(reps)==1668 and len(stable)==82 and pair_count==3321 and len(covers)==6
    out={'scope':'exact finite source-action tests read from the independent F20 geometric certificate',
         'source_generator_count':len(rows),'reference_order':certificate['segments'][0]['initial_order'],
         'original_basepoint_transport':basepoint_checks,
         'base_braid_words':base_braids,'point_pushing_kernel_basis_images':kernel_images,
         'A5_order':n,'automorphism_count':len(aut),'epimorphism_triples':count,'epimorphism_kernel_count':len(reps),
         'A5_conjugacy_class_sizes':class_sizes,'proper_normal_union_orders':normal_union_orders,
         'source_filling_kernel_generators':filled,
         'stable_factor_count':len(stable),'single_factor_cases':singles,'paired_quotient_count':pair_count,
         'paired_orbit_histogram':{str(list(k)):v for k,v in pair_histogram.items()},
         'nonfilled_stable_factors':len(nonfilled),'noncentral_homology_cover_cases':covers,
         'semilinear_word_checks':sum(x['semilinear_word_checks'] for x in covers)}
    Path(__file__).with_name('cross_divisor_finite_f20_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('single_factor_cases','noncentral_homology_cover_cases')},indent=2),flush=True)


if __name__=='__main__':main()
