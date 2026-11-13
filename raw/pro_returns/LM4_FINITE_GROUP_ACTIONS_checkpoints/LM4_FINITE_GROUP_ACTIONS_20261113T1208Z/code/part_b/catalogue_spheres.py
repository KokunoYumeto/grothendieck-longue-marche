#!/usr/bin/env python3
"""Spherical-orbifold classification and exact section data for 3<=nu<=6.

The quotient orbifold, decorated by its removed point orbits, is the complete
conjugacy invariant.  The proof is in B.26.  Finite permutation groups provide
certificates of the spherical presentations.  Mirror circles are obtained from
the finite coset incidence graph, retaining all reflection intersections.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product, permutations
from pathlib import Path
import csv
import json

OUT = Path(__file__).resolve().parent

def pmul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def pinv(a):
    z=[0]*len(a)
    for i,j in enumerate(a):
        z[j]=i
    return tuple(z)

def ppow(a,n):
    if n<0:
        return ppow(pinv(a),-n)
    z=tuple(range(len(a)))
    for _ in range(n):
        z=pmul(z,a)
    return z

def cyc(n):
    return tuple((i+1)%n for i in range(n))

def perm(n,*cycles):
    a=list(range(n))
    for c in cycles:
        for x,y in zip(c,c[1:]+c[:1]):
            a[x]=y
    return tuple(a)

def direct(a,b):
    return a+tuple(len(a)+x for x in b)

def dihedral(n):
    el=list(product(range(n),range(2)))
    ix={x:i for i,x in enumerate(el)}
    def mul(x,y):
        return ((x[0]+(-1)**x[1]*y[0])%n,x[1]^y[1])
    return tuple(ix[mul((1,0),x)] for x in el),tuple(ix[mul((0,1),x)] for x in el)

def closure(gens,identity):
    h={identity};todo=list(gens)
    while todo:
        x=todo.pop()
        if x in h:
            continue
        h.add(x)
        for y in tuple(h):
            for z in (pmul(x,y),pmul(y,x)):
                if z not in h:
                    todo.append(z)
    return frozenset(h)

class Orbifold:
    def __init__(self,name,kind,gens,signs,cones=(),corners=(),refs=(),boundary=None,order=None,cover_chi=2):
        self.name=name;self.kind=kind
        self.identity=tuple(range(len(gens[0])))
        self.gens=tuple(gens)
        self.group=closure(gens,self.identity)
        assert len(self.group)==order,(name,len(self.group),order)
        self.order=order
        self.elements=sorted(self.group)
        self.ids={g:i for i,g in enumerate(self.elements)}
        self.inv={g:pinv(g) for g in self.group}
        self.orientation={self.identity:1}
        todo=[self.identity]
        while todo:
            x=todo.pop()
            for g,sg in zip(gens,signs):
                y=pmul(x,g);val=self.orientation[x]*sg
                if y in self.orientation:
                    assert self.orientation[y]==val
                else:
                    self.orientation[y]=val;todo.append(y)
        self.cones=tuple(cones)
        self.corner_orders=tuple(corners)
        self.refs=tuple(refs)
        self.boundary=boundary if boundary is not None else self.identity
        self.cone_groups=[closure([c],self.identity) for c in cones]
        self.cone_orders=[len(h) for h in self.cone_groups]
        if kind=='disc':
            k=len(corners)
            assert len(refs)==max(k,1)
            end=pmul(pmul(self.boundary,refs[0]),self.inv[self.boundary])
            ext=list(refs)+[end]
            self.corner_rotations=[pmul(ext[j],ext[j+1]) for j in range(k)]
            self.corner_groups=[closure(ext[j:j+2],self.identity) for j in range(k)]
            assert [len(h) for h in self.corner_groups]==[2*n for n in corners]
            assert [self.elem_order(r) for r in self.corner_rotations]==list(corners)
            z=self.identity
            for c in cones:
                z=pmul(z,c)
            assert pmul(z,self.boundary)==self.identity
            if not corners:
                assert end==refs[0]
            assert all(self.elem_order(r)==2 and self.orientation[r]==-1 for r in refs)
        else:
            self.corner_rotations=[];self.corner_groups=[]
        if kind=='sphere':
            z=self.identity
            for c in cones:
                z=pmul(z,c)
            assert z==self.identity
        if kind=='RP2':
            assert len(gens)==1 and signs==[-1]
            z=ppow(gens[0],2)
            for c in cones:
                z=pmul(z,c)
            assert z==self.identity
        assert all(self.orientation[c]==1 for c in cones)
        underlying_chi={'sphere':2,'disc':1,'RP2':1}[kind]
        self.orbifold_chi=Fraction(underlying_chi)
        self.orbifold_chi-=sum((1-Fraction(1,m) for m in self.cone_orders),Fraction())
        self.orbifold_chi-=sum(((1-Fraction(1,m))/2 for m in self.corner_orders),Fraction())
        # Together with all local-group injections and the orientation character,
        # this certifies that the presentation kernel is the fundamental group
        # of a closed orientable cover of Euler characteristic 2, hence is 1.
        assert self.order*self.orbifold_chi==cover_chi

    def elem_order(self,g):
        z=self.identity
        for n in range(1,self.order+1):
            z=pmul(z,g)
            if z==self.identity:
                return n
        raise AssertionError(g)

    def conj(self,g,x):
        return pmul(pmul(g,x),self.inv[g])

    @lru_cache(None)
    def cosets(self,h):
        remaining=set(self.group);ans=[]
        while remaining:
            g=min(remaining);c=frozenset(pmul(g,x) for x in h)
            ans.append(c);remaining-=c
        return tuple(ans)

    @lru_cache(None)
    def coset(self,g,h):
        return frozenset(pmul(g,x) for x in h)

    @lru_cache(None)
    def all_subgroups(self):
        hs={frozenset({self.identity})};frontier=set(hs)
        while frontier:
            new={closure(tuple(h)+(g,),self.identity) for h in frontier for g in self.group-h}-hs
            hs|=new;frontier=new
        return tuple(sorted(hs,key=lambda h:(len(h),sorted(h))))

    def canonical(self,cselect,kselect,edges,regular):
        if self.kind=='sphere':
            cs=list(cselect)
            for order in set(self.cone_orders):
                ix=[i for i,n in enumerate(self.cone_orders) if n==order]
                for i,v in zip(ix,sorted(cs[i] for i in ix)):
                    cs[i]=v
            return tuple(cs),tuple(kselect),tuple(edges),regular
        if self.kind!='disc' or len(kselect)==0:
            return tuple(cselect),tuple(kselect),tuple(edges),regular
        k=len(kselect);forms=[]
        for epsilon in (1,-1):
            for a in range(k):
                cp=[(a+epsilon*j)%k for j in range(k)]
                ep=[(a+i)%k if epsilon==1 else (a-i+1)%k for i in range(k)]
                if any(self.corner_orders[cp[j]]!=self.corner_orders[j] for j in range(k)):
                    continue
                kp=[0]*k;ee=[0]*k
                for j in range(k):
                    kp[cp[j]]=kselect[j];ee[ep[j]]=edges[j]
                forms.append((tuple(cselect),tuple(kp),tuple(ee),regular))
        return min(forms)

    def patterns(self,nu):
        ans=set()
        for cs in product(range(2),repeat=len(self.cones)):
            a=sum(t*self.order//m for t,m in zip(cs,self.cone_orders))
            for ks in product(range(2),repeat=len(self.corner_orders)):
                b=a+sum(t*self.order//(2*m) for t,m in zip(ks,self.corner_orders))
                if b>nu:
                    continue
                ne=max(1,len(ks)) if self.kind=='disc' else 0
                maxedge=(nu-b)//(self.order//2) if ne else 0
                for es in product(range(maxedge+1),repeat=ne):
                    used=b+sum(es)*(self.order//2)
                    if used<=nu and (nu-used)%self.order==0:
                        ans.add(self.canonical(cs,ks,es,(nu-used)//self.order))
        return sorted(ans)

    def analyse(self,pattern,class_id,nu):
        cs,ks,es,regular=pattern
        nodes=[];descs={};stabs={};acts={};removed=set();critical={};graph={}
        def add_orbit(tag,h,puncture=False,rotation=None,m=None):
            result={}
            for c in self.cosets(h):
                key=(tag,c)
                idx=len(nodes);nodes.append(key);descs[key]=idx
                result[c]=key
                g=min(c)
                stabs[key]=frozenset(self.conj(g,x) for x in h)
                if puncture:
                    removed.add(key)
                if rotation is not None:
                    critical[key]=(g,rotation,m)
            return result
        cone_nodes=[add_orbit(('cone',j),h,bool(cs[j]),self.cones[j],self.cone_orders[j])
                    for j,h in enumerate(self.cone_groups)]
        corner_nodes=[add_orbit(('corner',j),h,bool(ks[j]),self.corner_rotations[j],self.corner_orders[j])
                      for j,h in enumerate(self.corner_groups)]
        mirror_groups=[closure([r],self.identity) for r in self.refs]
        if self.kind=='disc':
            k=len(ks)
            if not k:
                anchor=add_orbit(('anchor',0),mirror_groups[0])
            for i,h in enumerate(mirror_groups):
                interior=[]
                for j in range(es[i]+1):
                    interior.append(add_orbit(('edge',i,'segment',j,0),h))
                    interior.append(add_orbit(('edge',i,'segment',j,1),h))
                    if j<es[i]:
                        interior.append(add_orbit(('edge',i,'puncture',j),h,True))
                for c in self.cosets(h):
                    g=min(c)
                    if not k:
                        start=anchor[c]
                        end=anchor[self.coset(pmul(g,self.inv[self.boundary]),h)]
                    elif i==0:
                        start=corner_nodes[0][self.coset(g,self.corner_groups[0])]
                        end=corner_nodes[-1][self.coset(pmul(g,self.inv[self.boundary]),self.corner_groups[-1])]
                    else:
                        start=corner_nodes[i-1][self.coset(g,self.corner_groups[i-1])]
                        end=corner_nodes[i][self.coset(g,self.corner_groups[i])]
                    path=[start]+[d[c] for d in interior]+[end]
                    for x,y in zip(path,path[1:]):
                        graph.setdefault(x,set()).add(y)
                        graph.setdefault(y,set()).add(x)
        for j in range(regular):
            add_orbit(('regular_puncture',j),frozenset({self.identity}),True)
        assert len(removed)==nu,(self.name,pattern,len(removed),nu)
        def act_node(g,key):
            tag,c=key
            return (tag,frozenset(pmul(g,x) for x in c))
        for g in self.group:
            acts[g]={x:act_node(g,x) for x in nodes}
            assert set(acts[g].values())==set(nodes)
        mirror_cache={}
        def fixed_components(h):
            if len(h)==1:
                return [('surface',frozenset())]
            if any(self.orientation[g]==1 and g!=self.identity for g in h):
                return [('point',frozenset({x})) for x in critical if x not in removed and h<=stabs[x]]
            assert len(h)==2
            r=next(g for g in h if g!=self.identity)
            if r not in mirror_cache:
                full={x for x in graph if r in stabs[x]}
                # Every fixed circle is represented by a genuine subdivision.
                assert all(len(graph[x]&full)==2 for x in full),(self.name,r)
                remaining=full-removed;components=[]
                while remaining:
                    todo=[min(remaining,key=lambda x:descs[x])];comp=set()
                    while todo:
                        x=todo.pop()
                        if x in comp:
                            continue
                        comp.add(x);todo.extend((graph[x]&full)-removed-comp)
                    remaining-=comp
                    kind='line' if any(graph[x]&full&removed for x in comp) else 'oval'
                    components.append((kind,frozenset(comp)))
                mirror_cache[r]=components
            return mirror_cache[r]
        sections=[(h,kind,pts) for h in self.all_subgroups() if len(h)>1
                  for kind,pts in fixed_components(h)]
        sections.sort(key=lambda c:(len(c[0]),sorted(c[0]),c[1],sorted(descs[p] for p in c[2])))
        sid={c:i for i,c in enumerate(sections)}
        def included(c,d):
            return c[0]<d[0] and d[2]<=c[2]
        maxima=[c for c in sections if not any(included(c,d) for d in sections)]
        def act(g,c):
            h,kind,pts=c
            return frozenset(self.conj(g,x) for x in h),kind,frozenset(acts[g][x] for x in pts)
        def mu(g,c):
            if g==self.identity:
                return Fraction(0)
            if self.orientation[g]==-1:
                assert self.elem_order(g)==2
                return Fraction(1,2)
            assert c[1]=='point'
            q,r,m=critical[next(iter(c[2]))]
            y=self.conj(self.inv[q],g)
            powers={ppow(r,i):i for i in range(m)}
            assert y in powers
            return Fraction(self.orientation[q]*powers[y],m)%1
        remainder=set(maxima);orbits=[]
        while remainder:
            c=next(iter(remainder));orb={act(g,c) for g in self.group}
            assert orb<=set(maxima)
            remainder-=orb;orbits.append(sorted(sid[x] for x in orb))
        records=[];multi=0
        for c in sections:
            h,kind,pts=c
            maxover=[d for d in maxima if d==c or included(c,d)]
            if any(self.orientation[g]==1 and g!=self.identity for g in h):
                assert len(maxover)==1
            elif len(maxover)>1:
                multi+=1
            mus={self.ids[g]:str(mu(g,c)) for g in sorted(h)}
            for g in h:
                val=mu(g,c);assert val.denominator==self.elem_order(g)
                for k in range(self.elem_order(g)+1):
                    assert mu(ppow(g,k),c)==(k*val)%1
            stab=[g for g in self.group if act(g,c)==c]
            if c in maxima and kind=='point':
                assert frozenset(stab)==h
            records.append({'section_id':sid[c], 'image_elements':[self.ids[g] for g in sorted(h)],
                'fixed_component_kind':kind,'fixed_component_nodes':sorted(descs[x] for x in pts),
                'centralizer_in_surface_group':'Z' if kind=='oval' else '1',
                'mu_by_element_id':mus,'maximal':c in maxima,
                'strict_extensions':[sid[d] for d in sections if included(c,d)],
                'maximal_overgroups':[sid[d] for d in maxover],
                'Gamma_stabilizer_elements':[self.ids[g] for g in sorted(stab)]})
        row={'type':f'(0,{nu})','class_id':class_id,'orbifold':self.name,
             'order':self.order,'positive_order':sum(self.orientation[g]==1 for g in self.group),
             'selected_cones':','.join(map(str,cs)), 'selected_corners':','.join(map(str,ks)),
             'mirror_edge_puncture_orbits':','.join(map(str,es)), 'regular_puncture_orbits':regular,
             'full_splitting_classes':len(fixed_components(self.group)),
             'nontrivial_partial_splitting_classes':len(sections),
             'maximal_partial_classes_Phi':len(maxima),'Gamma_orbits_on_Phi':len(orbits),
             'oval_section_classes':sum(c[1]=='oval' for c in sections),
             'line_section_classes':sum(c[1]=='line' for c in sections),
             'reflection_classes_with_multiple_maximal_extensions':multi}
        data={'class_id':class_id,'orbifold':self.name,'pattern':pattern,
              'orbifold_euler_characteristic':str(self.orbifold_chi),
              'cover_euler_characteristic':str(self.order*self.orbifold_chi),
              'group_elements':[{'id':self.ids[g],'permutation':g,'orientation':self.orientation[g]}
                                for g in self.elements],
              'generators':[self.ids[g] for g in self.gens],
              'cone_generators':[self.ids[g] for g in self.cones],
              'mirror_reflections':[self.ids[g] for g in self.refs],
              'boundary_element':self.ids[self.boundary],
              'corner_rotations':[self.ids[g] for g in self.corner_rotations],
              'nodes':[{'id':descs[x],'stratum':x[0],
                        'coset_elements':[self.ids[g] for g in sorted(x[1])],
                        'stabilizer_elements':[self.ids[g] for g in sorted(stabs[x])],
                        'removed_puncture':x in removed} for x in nodes],
              'mirror_graph_edges':sorted({tuple(sorted((descs[x],descs[y]))) for x in graph for y in graph[x]}),
              'sections':records,'Phi_orbits':sorted(orbits)}
        return row,data

def orbifolds(max_n=6):
    ans=[]
    ans.append(Orbifold('sphere','sphere',[(0,)],[1],order=1))
    c2=cyc(2)
    ans.append(Orbifold('disc_mirror','disc',[c2],[-1],refs=[c2],order=2))
    ans.append(Orbifold('RP2','RP2',[c2],[-1],order=2))
    for n in range(2,max_n+1):
        r=cyc(n);ii=tuple(range(n))
        ans.append(Orbifold(f'sphere({n},{n})','sphere',[r],[1],cones=[r,pinv(r)],order=n))
        a,b=dihedral(n)
        ans.append(Orbifold(f'sphere(2,2,{n})','sphere',[a,b],[1,1],
            cones=[b,pmul(b,a),pinv(a)],order=2*n))
        ans.append(Orbifold(f'disc*({n},{n})','disc',[a,b],[1,-1],
            corners=[n,n],refs=[b,pmul(b,a)],order=2*n))
        x=direct(r,(0,1));z=direct(ii,c2)
        ans.append(Orbifold(f'disc({n};*)','disc',[x,z],[1,-1],
            cones=[x],refs=[z],boundary=pinv(x),order=2*n))
        rr=cyc(2*n)
        ans.append(Orbifold(f'RP2({n})','RP2',[rr],[-1],cones=[ppow(rr,-2)],order=2*n))
        ida=tuple(range(len(a)))
        aa=direct(a,(0,1));bb=direct(b,(0,1));zz=direct(ida,c2)
        # r0=b, r1=z, r2=b*a: adjacent corner orders 2,2,n.
        ans.append(Orbifold(f'disc*(2,2,{n})','disc',[aa,bb,zz],[1,-1,-1],
            corners=[2,2,n],refs=[bb,zz,pmul(bb,aa)],order=4*n))
        aa,bb=dihedral(2*n)
        r0=pmul(aa,bb)
        ans.append(Orbifold(f'disc(2;*{n})','disc',[aa,bb],[-1,1],
            cones=[bb],corners=[n],refs=[r0],boundary=bb,order=4*n))
    a=perm(4,(0,1),(2,3));b=perm(4,(0,1,2))
    ans.append(Orbifold('sphere(2,3,3)','sphere',[a,b],[1,1],
        cones=[a,b,pinv(pmul(a,b))],order=12))
    a=perm(4,(0,1));b=perm(4,(1,2,3))
    ans.append(Orbifold('sphere(2,3,4)','sphere',[a,b],[1,1],
        cones=[a,b,pinv(pmul(a,b))],order=24))
    r0=perm(4,(0,1));r1=perm(4,(2,3));r2=perm(4,(1,2))
    ans.append(Orbifold('disc*(2,3,3)','disc',[r0,r1,r2],[-1,-1,-1],
        corners=[2,3,3],refs=[r0,r1,r2],order=24))
    x=direct(perm(4,(0,1,2)),(0,1))
    rr=direct(perm(4,(0,1),(2,3)),c2)
    ans.append(Orbifold('disc(3;*2)','disc',[x,rr],[1,-1],cones=[x],
        corners=[2],refs=[rr],boundary=pinv(x),order=24))
    r0=perm(6,(0,3));r1=perm(6,(1,2),(4,5));r2=perm(6,(0,1),(3,4))
    ans.append(Orbifold('disc*(2,3,4)','disc',[r0,r1,r2],[-1,-1,-1],
        corners=[2,3,4],refs=[r0,r1,r2],order=48))
    return ans

if __name__=='__main__':
    models=orbifolds()
    summaries=[]
    for nu in range(3,7):
        cases=[(o,p) for o in models for p in o.patterns(nu)]
        cases.sort(key=lambda z:(z[0].order,z[0].name,z[1]))
        rows=[];details=[]
        for j,(o,p) in enumerate(cases,1):
            row,data=o.analyse(p,f'S{nu}_{j:03}',nu)
            rows.append(row);details.append(data)
        if nu in (3,4):
            assert len(rows)=={3:10,4:30}[nu],(nu,len(rows))
        path=OUT/f'type_0_{nu}_orbifold_catalogue.csv'
        with path.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
        (OUT/f'type_0_{nu}_orbifold_sections.json').write_text(json.dumps(details,indent=2)+'\n')
        summary={'type':f'(0,{nu})','conjugacy_classes':len(rows),
                 'by_group_order':dict(sorted(Counter(r['order'] for r in rows).items())),
                 'table':rows}
        summaries.append(summary)
        print(f'type (0,{nu}): {len(rows)} finite subgroup classes; orders {summary["by_group_order"]}',flush=True)
    (OUT/'catalogue_spheres_output.json').write_text(json.dumps(summaries,indent=2)+'\n')
    # Independent enumeration by a 12-element permutation group for nu=3 and
    # by the finite-vertex amalgam in B.25 for nu=4.  Compare all six columns,
    # retaining multiplicity, so this also checks the computed section posets.
    fields=['order','positive_order','full_splitting_classes',
            'nontrivial_partial_splitting_classes','maximal_partial_classes_Phi',
            'Gamma_orbits_on_Phi']
    crosschecks=[]
    for nu in (3,4):
        old=list(csv.DictReader((OUT/f'type_0_{nu}_finite_subgroups.csv').open()))
        new=summaries[nu-3]['table']
        assert Counter(tuple(int(r[k]) for k in fields) for r in old)==Counter(
            tuple(r[k] for k in fields) for r in new)
        crosschecks.append({'type':f'(0,{nu})','independent_catalogue_rows':len(old),
                            'compared_fields':fields,'multisets_equal':True})
    (OUT/'spherical_independent_crosscheck.json').write_text(json.dumps(crosschecks,indent=2)+'\n')
