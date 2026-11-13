#!/usr/bin/env python3
"""Multi-boundary finite NEC coset incidence model.  The fixed-component
algorithm is the same as B26, with one independently closed mirror cycle
per quotient boundary component, retaining every dihedral intersection.
"""
from pathlib import Path
from fractions import Fraction
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from catalogue_genus3_hyperelliptic import SurfaceOrbifold,pmul,pinv,ppow,closure

class MultiBoundaryOrbifold(SurfaceOrbifold):
    def __init__(self,name,G,orientation,cones,cycles,gens,chi=-4):
        self.name=name;self.kind='general';self.identity=G.el[G.one]
        self.group=frozenset(G.el);self.order=G.n;self.gens=tuple(G.el[q] for q in gens)
        assert closure(self.gens,self.identity)==self.group
        self.elements=sorted(self.group);self.ids={g:i for i,g in enumerate(self.elements)}
        assert self.elements==G.el
        self.inv={g:pinv(g) for g in self.group}
        self.orientation={G.el[q]:s for q,s in enumerate(orientation)}
        for g in self.group:
            for h in self.gens:
                assert self.orientation[pmul(g,h)]==self.orientation[g]*self.orientation[h]
        self.cones=tuple(G.el[q] for q in cones)
        self.cone_groups=[closure([q],self.identity) for q in self.cones]
        self.cone_orders=[len(h) for h in self.cone_groups]
        self.boundary_cycles=[(tuple(G.el[q] for q in refs),tuple(ms),G.el[e]) for refs,ms,e in cycles]
        self.refs=tuple(r for refs,ms,e in self.boundary_cycles for r in refs)
        self.corner_orders=tuple(m for refs,ms,e in self.boundary_cycles for m in ms)
        self.boundary=self.identity
        self.corner_rotations=[];self.corner_groups=[]
        for refs,ms,e in self.boundary_cycles:
            assert len(refs)==max(1,len(ms))
            end=pmul(pmul(e,refs[0]),self.inv[e]);ext=list(refs)+[end]
            if not ms:assert end==refs[0]
            for i,m in enumerate(ms):
                z=pmul(ext[i],ext[i+1]);h=closure(ext[i:i+2],self.identity)
                assert self.elem_order(z)==m and len(h)==2*m
                self.corner_rotations.append(z);self.corner_groups.append(h)
        assert all(self.orientation[c]==1 for c in self.cones)
        assert all(self.orientation[r]==-1 and self.elem_order(r)==2 for r in self.refs)
        self.orbifold_chi=-sum((1-Fraction(1,m) for m in self.cone_orders),Fraction())
        self.orbifold_chi-=sum(((1-Fraction(1,m))/2 for m in self.corner_orders),Fraction())
        assert self.order*self.orbifold_chi==chi

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
        for cycle_index,(cycle_refs,cycle_corners,cycle_boundary) in enumerate(self.boundary_cycles):
            k=len(cycle_corners)
            corner_start=sum(len(c[1]) for c in self.boundary_cycles[:cycle_index])
            ref_start=sum(len(c[0]) for c in self.boundary_cycles[:cycle_index])
            if not k:
                anchor=add_orbit(('anchor',cycle_index),mirror_groups[ref_start])
            for local_i in range(len(cycle_refs)):
                i=ref_start+local_i;h=mirror_groups[i]
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
                        end=anchor[self.coset(pmul(g,self.inv[cycle_boundary]),h)]
                    elif local_i==0:
                        start=corner_nodes[corner_start][self.coset(g,self.corner_groups[corner_start])]
                        end=corner_nodes[corner_start+k-1][self.coset(pmul(g,self.inv[cycle_boundary]),self.corner_groups[corner_start+k-1])]
                    else:
                        start=corner_nodes[corner_start+local_i-1][self.coset(g,self.corner_groups[corner_start+local_i-1])]
                        end=corner_nodes[corner_start+local_i][self.coset(g,self.corner_groups[corner_start+local_i])]
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
        data['boundary_cycles']=[{'mirror_reflections':[self.ids[r] for r in refs],
             'corner_orders':ms,'boundary_element':self.ids[e]}
             for refs,ms,e in self.boundary_cycles]
        return row,data
