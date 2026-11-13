#!/usr/bin/env python3
"""Exact finite checks for LM8 A. No external group-theory package.

Scope: all 24 abstract finite groups of order <=12; all faithful,
orientation-preserving actions on a CLOSED genus-2 surface, recorded by
orbifold signature and generating vectors (not by Hurwitz orbit).
Also every normal subgroup of those 24 groups, so ineffective actions are
recovered by pullback from the displayed quotient actions. The catalogue
itself is supplied explicitly; associativity and the group axioms are checked.
The signature list separately enumerates h<=2, s<=3, <=3 cone points,
each cone order in [2,12]. It is NOT an enumeration with unbounded punctures.
"""
from fractions import Fraction
from itertools import product, permutations, combinations_with_replacement
from pathlib import Path
import json, csv

OUT=Path(__file__).resolve().parent

class Group:
    def __init__(self,name,labels,operation):
        self.name=name; self.labels=list(labels); self.n=len(labels)
        lookup={x:i for i,x in enumerate(self.labels)}
        self.tab=[[lookup[operation(x,y)] for y in self.labels] for x in self.labels]
        self.e=next(e for e in range(self.n) if all(self.tab[e][x]==x==self.tab[x][e] for x in range(self.n)))
        self.inv=[next(y for y in range(self.n) if self.tab[x][y]==self.e==self.tab[y][x]) for x in range(self.n)]
        assert all(self.tab[self.tab[a][b]][c]==self.tab[a][self.tab[b][c]] for a,b,c in product(range(self.n),repeat=3))
        self.orders=[]
        for x in range(self.n):
            y=self.e
            for k in range(1,self.n+1):
                y=self.tab[y][x]
                if y==self.e:self.orders.append(k);break
    def mul(self,x,y):return self.tab[x][y]
    def prod(self,seq):
        x=self.e
        for y in seq:x=self.mul(x,y)
        return x
    def comm(self,x,y):return self.prod([x,y,self.inv[x],self.inv[y]])
    def generated(self,gens):
        reached={self.e};todo=[self.e]
        while todo:
            x=todo.pop()
            for y in gens:
                z=self.mul(x,y)
                if z not in reached:reached.add(z);todo.append(z)
        return frozenset(reached)
    def normals(self):
        subs={frozenset([self.e])};todo=list(subs)
        while todo:
            h=todo.pop()
            for x in range(self.n):
                if x not in h:
                    k=self.generated(list(h)+[x])
                    if k not in subs:subs.add(k);todo.append(k)
        return sorted((h for h in subs if all(self.prod([g,x,self.inv[g]]) in h for g in range(self.n) for x in h)),key=lambda h:(len(h),sorted(h)))
    def quotient(self,k):
        cosets=[];unused=set(range(self.n))
        while unused:
            g=min(unused);c=frozenset(self.mul(g,x) for x in k);cosets.append(c);unused-=c
        def op(a,b):
            x=self.mul(min(a),min(b));return next(c for c in cosets if x in c)
        return Group(self.name+'/K'+','.join(map(str,sorted(k))),cosets,op)

def abelian(moduli):
    return Group('x'.join('C'+str(n) for n in moduli) or '1',list(product(*(range(n) for n in moduli))),lambda x,y:tuple((a+b)%n for a,b,n in zip(x,y,moduli)))
def dihedral(n):
    return Group('D'+str(2*n),list(product(range(n),range(2))),lambda x,y:((x[0]+(-1)**x[1]*y[0])%n,(x[1]+y[1])%2))
def dicyclic(n):
    return Group('Q8' if n==2 else 'Dic3',list(product(range(2*n),range(2))),lambda x,y:((x[0]+(-1)**x[1]*y[0]+n*x[1]*y[1])%(2*n),(x[1]+y[1])%2))
def alternating4():
    es=[p for p in permutations(range(4)) if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0]
    return Group('A4',es,lambda x,y:tuple(x[y[i]] for i in range(4)))

GROUPS=[abelian([]),abelian([2]),abelian([3]),abelian([4]),abelian([2,2]),abelian([5]),abelian([6]),dihedral(3),abelian([7]),abelian([8]),abelian([4,2]),abelian([2,2,2]),dihedral(4),dicyclic(2),abelian([9]),abelian([3,3]),abelian([10]),dihedral(5),abelian([11]),abelian([12]),abelian([6,2]),dihedral(6),alternating4(),dicyclic(3)]
assert len(GROUPS)==24

def genus2_signatures(g):
    d=g.n; divisors=sorted(set(g.orders)-{1}); ans=[]
    for h in range(3):
        for r in range(7):
            for ms in combinations_with_replacement(divisors,r):
                if Fraction(2,d)==2*h-2+sum((1-Fraction(1,m) for m in ms),Fraction(0)):
                    ans.append((h,ms))
    return ans

def generating_vectors(g,h,ms):
    count=0; examples=[]
    # The only possible h=2 row has trivial quotient; still use general code.
    for handles in product(range(g.n),repeat=2*h):
        z=g.prod(g.comm(handles[2*i],handles[2*i+1]) for i in range(h))
        if not ms:
            if z==g.e and len(g.generated(handles))==g.n:
                count+=1
                if not examples:examples.append(list(handles))
            continue
        lists=[[x for x in range(g.n) if g.orders[x]==m] for m in ms[:-1]]
        for cs in product(*lists):
            last=g.inv[g.mul(z,g.prod(cs))]
            if g.orders[last]!=ms[-1]:continue
            v=handles+cs+(last,)
            if len(g.generated(v))!=g.n:continue
            count+=1
            if not examples:examples.append(list(v))
    return count,examples

def catalogue(g):
    rows=[]
    for h,ms in genus2_signatures(g):
        count,examples=generating_vectors(g,h,ms)
        rows.append({'quotient_group':g.name,'order':g.n,'base_genus':h,'cone_orders':list(ms),'generating_vector_count':count,'first_vector':examples[0] if examples else None,'realizable':bool(count)})
    return rows

def main():
    faithful=[]; ineffective=[];catalogues={}
    for g in GROUPS:
        rows=catalogue(g);faithful.extend(rows)
        catalogues[g.name]=[r for r in rows if r['realizable']]
        for k in g.normals():
            if len(k)==1:continue
            q=g.quotient(k)
            for row in catalogue(q):
                if row['realizable']:
                    ineffective.append({'acting_group':g.name,'group_order':g.n,'ineffective_kernel_elements':sorted(k),'effective_order':q.n,'base_genus':row['base_genus'],'cone_orders':row['cone_orders'],'vector_count_in_labelled_quotient':row['generating_vector_count'],'first_quotient_vector':row['first_vector']})
    sig=[]
    for h,s,r in product(range(3),range(4),range(4)):
        for ms in combinations_with_replacement(range(2,13),r):
            chi=2-2*h-s-sum((1-Fraction(1,m) for m in ms),Fraction(0))
            bad=h==s==0 and ((r==1) or (r==2 and ms[0]!=ms[1]))
            sig.append({'base_genus':h,'punctures':s,'cone_orders':';'.join(map(str,ms)),'chi_orb':str(chi),'hyperbolic_L':chi<0,'finite_curve_quotient':not bad})
    with (OUT/'a_small_signatures.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(sig[0]));w.writeheader();w.writerows(sig)
    # Verify the six epimorphisms C2*C3 -> S3 form one conjugation orbit.
    s3=next(g for g in GROUPS if g.name=='D6')
    pairs=[(a,b) for a,b in product(range(6),repeat=2) if s3.orders[a]==2 and s3.orders[b]==3 and len(s3.generated([a,b]))==6]
    a,b=pairs[0];orbit={(s3.prod([u,a,s3.inv[u]]),s3.prod([u,b,s3.inv[u]])) for u in range(6)}
    assert len(pairs)==6 and set(pairs)==orbit
    # C2*C4 -> C4, a ->2, b ->1; cusp ab has order4.
    q=abelian([4]);a=q.labels.index((2,));b=q.labels.index((1,))
    assert q.orders[a]==2 and q.orders[b]==4 and q.orders[q.mul(a,b)]==4
    counterexample={'orbifold_signature':[0,[2,4],1],'group':'C2*C4','abelianization_order':8,'PSL2Z_abelianization_order':6,'index4_surface_genus':1,'index4_surface_punctures':1,'cusp_order_in_C4':4,'orientation_preserving_outer_L_group_order':1,'last_claim_proof':'Paper A.7, not inferred from finite computation'}
    result={'scope':__doc__,'finite_groups':[{ 'name':g.name,'order':g.n,'element_orders':g.orders,'multiplication_table':g.tab,'identity':g.e} for g in GROUPS],'faithful_genus2_signatures':faithful,'ineffective_genus2_signatures':ineffective,'small_signature_counts':{'total':len(sig),'hyperbolic':sum(r['hyperbolic_L'] for r in sig),'bad_orbifolds':sum(not r['finite_curve_quotient'] for r in sig)},'s3_surjections':{'count':len(pairs),'inner_orbits':1},'rigidity_counterexample':counterexample}
    (OUT/'a_small_actions.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All 24 group tables pass identity, inverse, associativity checks.')
    print('Faithful closed genus-2 action signature rows:')
    for row in faithful:
        if row['realizable']:print(row['quotient_group'],row['order'],'h=',row['base_genus'],'cones=',row['cone_orders'],'vectors=',row['generating_vector_count'])
    print('RH-admissible rows checked:',len(faithful),'realizable:',sum(r['realizable'] for r in faithful))
    print('Ineffective pullback rows:',len(ineffective))
    print('Small signature counts:',result['small_signature_counts'])
    print('S3 epimorphisms:',result['s3_surjections'])
    print('Characterization counterexample:',counterexample)

if __name__=='__main__':main()
