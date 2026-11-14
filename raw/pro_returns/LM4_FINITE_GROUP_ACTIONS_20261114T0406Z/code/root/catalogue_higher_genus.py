#!/usr/bin/env python3
"""Exact section data for the published oriented genus-two/three census.

Input: Karabas--Nedela--Skyvova, arXiv:2203.05812v6, accompanying
2023 JSON data at https://www.savbb.sk/~karabas/science/discactions.html.
The input attribution and provenance are retained in research_data/.
The code verifies presentations, orders, Euler characteristics and every
section invariant independently.  In planar signatures it recomputes the
full colored-braid orbit equivalence, including mirror equivalence.  It
also computes all invariant puncture decorations in genus two, nu<=2.
"""
from pathlib import Path
from itertools import product
from collections import deque, Counter
from fractions import Fraction
import json, csv, hashlib

BASE=Path(__file__).resolve().parent
DATA=BASE/'research_data'
OUT=BASE/'higher_genus_output'
OUT.mkdir(exist_ok=True)

def pmul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def pinv(a):
    z=[0]*len(a)
    for i,j in enumerate(a):z[j]=i
    return tuple(z)

class Group:
    def __init__(self,perms):
        self.identity=tuple(range(len(perms[0])))
        todo=deque([self.identity]); gs={self.identity}
        while todo:
            a=todo.popleft()
            for b in perms:
                c=pmul(a,b)
                if c not in gs:gs.add(c);todo.append(c)
        self.el=sorted(gs);self.ids={a:i for i,a in enumerate(self.el)}
        self.n=len(gs);self.one=self.ids[self.identity]
        self.mul=[[self.ids[pmul(a,b)] for b in self.el] for a in self.el]
        self.inv=[self.ids[pinv(a)] for a in self.el]
        self.powers=[];self.orders=[]
        for a in range(self.n):
            ps=[self.one];b=self.mul[self.one][a]
            while b!=self.one:ps.append(b);b=self.mul[b][a]
            self.powers.append(ps);self.orders.append(len(ps))

    def ids_of(self,perms):
        # Magma exports right-acting permutations.  Inversion is the exact
        # isomorphism from that opposite multiplication to our left action.
        return tuple(self.ids[pinv(tuple(x-1 for x in p))] for p in perms)
    def prod(self,seq):
        a=self.one
        for b in seq:a=self.mul[a][b]
        return a
    def conj(self,a,b):return self.mul[self.mul[a][b]][self.inv[a]]
    def comm(self,a,b):return self.prod([a,b,self.inv[a],self.inv[b]])
    def tuple_key(self,vec):
        """Rooted colored Cayley graph, canonical under Aut(G)."""
        seen={self.one:0};els=[self.one]
        for x in els:
            for a in vec:
                y=self.mul[x][a]
                if y not in seen:seen[y]=len(els);els.append(y)
        assert len(els)==self.n
        return tuple(seen[self.mul[x][a]] for x in els for a in vec)
    def cosets(self,h):
        rem=set(range(self.n));out=[]
        while rem:
            x=min(rem);c=frozenset(self.mul[x][a] for a in h)
            out.append((x,c));rem-=c
        return out
    def subgroup(self,gens):
        seen={self.one};els=[self.one]
        for x in els:
            for a in gens:
                y=self.mul[x][a]
                if y not in seen:seen.add(y);els.append(y)
        return frozenset(seen)
    def all_subgroups(self):
        trivial=frozenset([self.one]);seen={trivial};todo=[trivial]
        for h in todo:
            for x in range(self.n):
                if x in h:continue
                k=self.subgroup(tuple(h)+(x,))
                if k not in seen:seen.add(k);todo.append(k)
        return sorted(seen,key=lambda h:(len(h),sorted(h)))

def braid(G,vec,dec,i,sign):
    v=list(vec);d=list(dec);a,b=v[i:i+2]
    if sign==1:v[i:i+2]=[G.conj(a,b),a]
    else:v[i:i+2]=[b,G.conj(G.inv[b],a)]
    d[i],d[i+1]=d[i+1],d[i]
    return tuple(v),tuple(d)

def mirror(G,vec):
    v=[];p=G.one
    for a in vec:
        v.append(G.conj(p,G.inv[a]));p=G.mul[p][a]
    assert p==G.one
    return tuple(v)

def braid_generators(orders):
    r=len(orders);gens=[]
    for i in range(r-1):
        if orders[i]==orders[i+1]:gens.append([(i,1)])
    for i in range(r):
        for j in range(i+1,r):
            move=[(k,1) for k in range(j-1,i,-1)]
            gens.append(move+[(i,1),(i,1)]+[(k,-s) for k,s in reversed(move)])
    return gens

def decoration_orbits(G,action,nu,include_mirror=True):
    ms=action['bd'];r=len(ms);N=G.n
    reps=[G.ids_of(v) for v in action['autgreps']]
    keys={G.tuple_key(v):i for i,v in enumerate(reps)}
    assert len(keys)==len(reps)
    decorations=[]
    for c in product((0,1),repeat=r):
        weight=sum(N//m*b for m,b in zip(ms,c))
        if weight<=nu and (nu-weight)%N==0:
            decorations.append((c,(nu-weight)//N))
    states={(i,c,a) for i in range(len(reps)) for c,a in decorations}
    gens=braid_generators(ms)
    orbit_list=[]
    while states:
        first=min(states);orb={first};todo=[first]
        for i,c,a in todo:
            neighbors=[]
            for word in gens:
                w,d=reps[i],c
                for k,s in word:w,d=braid(G,w,d,k,s)
                assert [G.orders[x] for x in w]==ms
                neighbors.append((keys[G.tuple_key(w)],d,a))
            if include_mirror:neighbors.append((keys[G.tuple_key(mirror(G,reps[i]))],c,a))
            for st in neighbors:
                if st not in orb:orb.add(st);todo.append(st)
        assert orb<=states
        states-=orb;orbit_list.append(sorted(orb))
    return orbit_list

def section_data(G,vec,orders,removed,regular,nu):
    points=[]
    for j,(x,m,rem) in enumerate(zip(vec,orders,removed)):
        if rem:continue
        h=frozenset(G.powers[x])
        for rep,coset in G.cosets(h):
            stabilizer=frozenset(G.conj(rep,a) for a in h)
            local=G.conj(rep,x)
            mu={str(a):str(Fraction(k,m)) for k,a in enumerate(G.powers[local])}
            points.append({'id':len(points),'cone':j,'coset':sorted(coset),
                           'stabilizer':sorted(stabilizer),'positive_generator':local,
                           'mu':mu})
    subs=G.all_subgroups()
    counts=[];sections=[]
    for sid,h in enumerate(subs):
        if len(h)==1:continue
        fixed=[p for p in points if h<=set(p['stabilizer'])]
        cyclic=any(set(G.powers[a])==h for a in h)
        assert cyclic or not fixed
        counts.append({'id':sid,'elements':sorted(h),'order':len(h),'cyclic':cyclic,
                       'sections':len(fixed)})
        for p in fixed:
            sections.append({'id':len(sections),'subgroup':sid,'point':p['id'],
                             'centralizer':'1','mu':{str(a):p['mu'][str(a)] for a in sorted(h)}})
    inclusions=[]
    for s in sections:
        h=subs[s['subgroup']]
        for t in sections:
            if s['point']==t['point'] and h<subs[t['subgroup']]:
                inclusions.append([s['id'],t['id']])
    maxids=[s['id'] for s in sections if not any(i==s['id'] for i,j in inclusions)]
    assert len(maxids)==len(points)
    # Every nontrivial section has one maximal extension, at its fixed point.
    for s in sections:
        containing=[t for t in maxids if sections[t]['point']==s['point']]
        assert len(containing)==1
    actions=[]
    index={(p['cone'],tuple(p['coset'])):p['id'] for p in points}
    for a in range(G.n):
        perm=[]
        for p in points:
            c=tuple(sorted(G.mul[a][b] for b in p['coset']))
            perm.append(index[(p['cone'],c)])
        actions.append(perm)
    expected=sum(G.n//m*(sum(m%d==0 for d in range(2,m+1))) for m,c in zip(orders,removed) if not c)
    assert expected==len(sections)
    full=next((row['sections'] for row in counts if row['order']==G.n),1 if G.n==1 else 0)
    punctures=[{'cone':j,'orbit_size':G.n//m,'stabilizer_order':m}
               for j,(m,c) in enumerate(zip(orders,removed)) if c]
    punctures += [{'regular_orbit':j,'orbit_size':G.n,'stabilizer_order':1} for j in range(regular)]
    assert sum(p['orbit_size'] for p in punctures)==nu
    return {'points':points,'group_action_on_phi':actions,'partial_section_classes':sections,
            'subgroup_section_counts':counts,'inclusions':inclusions,'maximal_sections':maxids,
            'punctures':punctures,'full_sections':full,'total_nontrivial_partial_sections':len(sections)}

def main():
    tables=[];summary={};full=[];checks=[]
    for genus in (2,3):
        path=DATA/f'actions-genus{genus}.json'
        ds=json.loads(path.read_text())['actions']
        counts=Counter()
        for ai,action in enumerate(ds,1):
            raw=action['topreps'][0]
            G=Group([tuple(x-1 for x in p) for p in raw])
            assert G.n==action['group']['order']
            ms=action['bd'];r=len(ms);gamma=action['gamma']
            chi=Fraction(2-2*gamma)-sum((1-Fraction(1,m) for m in ms),Fraction())
            assert G.n*chi==2-2*genus
            for rawvec in action['autgreps']:
                vec=G.ids_of(rawvec)
                assert [G.orders[x] for x in vec[:r]]==ms
                assert G.tuple_key(vec)
                comms=[G.comm(vec[r+2*j],vec[r+2*j+1]) for j in range(gamma)]
                # The exported data use either right permutation multiplication
                # or its opposite.  Both explicit conventions are verified.
                rels=[G.prod(comms+list(vec[:r])),G.prod(list(vec[:r])+comms)]
                comms_op=[G.prod([G.inv[vec[r+2*j]],G.inv[vec[r+2*j+1]],vec[r+2*j],vec[r+2*j+1]]) for j in range(gamma)]
                rels += [G.prod(comms_op+list(vec[:r])),G.prod(list(vec[:r])+comms_op)]
                assert G.one in rels,(genus,ai,'relation')
            if gamma==0:
                positive_orbits=decoration_orbits(G,action,0,False)
                extended_orbits=decoration_orbits(G,action,0,True)
                assert len(positive_orbits)==action['enums']['top'],(genus,ai,'braid count')
                assert len(extended_orbits)==len(positive_orbits),(genus,ai,'mirror fusion')
                checks.append({'source':f'O{genus}.{ai}','autg':len(action['autgreps']),
                               'positive_braid_orbits':len(positive_orbits),
                               'with_mirror':len(extended_orbits)})
            nus=(0,1,2) if genus==2 else (0,)
            for nu in nus:
                if gamma==0:
                    orbits=decoration_orbits(G,action,nu,True)
                    decorated=[(G.ids_of(action['autgreps'][orb[0][0]]),orb[0][1],orb[0][2],len(orb)) for orb in orbits]
                elif G.n==1:
                    decorated=[(G.ids_of(raw),(),nu,1)]
                elif genus==2:
                    # Only O2.2=(1;2,2), G=C2.  Both branch monodromies are
                    # the unique involution.  Their exchange lifts; SL2Z and
                    # point pushes connect the four handle vectors in the input.
                    assert G.n==2 and ms==[2,2] and gamma==1
                    decorated=[]
                    for c in ((0,0),(0,1),(1,1)):
                        w=sum(c)
                        if w<=nu and (nu-w)%2==0:
                            decorated.append((G.ids_of(raw),c,(nu-w)//2,1))
                else:
                    decorated=[(G.ids_of(v),(0,)*r,0,1) for v in action['topreps']]
                for di,(vec,removed,regular,orbsize) in enumerate(decorated,1):
                    cid=f'G{genus}N{nu}-O{ai}-{di}'
                    inv=section_data(G,vec,ms,removed,regular,nu)
                    row={'id':cid,'genus':genus,'punctures':nu,'source_pair':f'O{genus}.{ai}',
                         'order':G.n,'small_group_code':action['group']['code'],
                         'quotient_genus':gamma,'cone_orders':','.join(map(str,ms)),
                         'removed_cones':','.join(str(i+1) for i,c in enumerate(removed) if c),
                         'removed_regular_orbits':regular,'phi_points':len(inv['points']),
                         'phi_orbits':sum(not c for c in removed),
                         'full_sections':inv['full_sections'],
                         'nontrivial_partial_sections':inv['total_nontrivial_partial_sections'],
                         'decorated_braid_orbit_size':orbsize}
                    tables.append(row);counts[nu]+=1
                    full.append({'summary':row,'group_elements':[list(p) for p in G.el],
                                 'identity':G.one,'multiplication':G.mul,
                                 'generating_vector':list(vec),**inv})
        summary[str(genus)]={'classes_by_punctures':dict(counts),'source_pairs':len(ds)}
    with (OUT/'oriented_higher_genus_catalogue.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(tables[0]));w.writeheader();w.writerows(tables)
    (OUT/'oriented_higher_genus_sections.json').write_text(json.dumps(full,separators=(',',':'))+'\n')
    report={'summary':summary,'rows':len(tables),'planar_braid_checks':checks,
            'data_sha256':{f'actions-genus{g}.json':hashlib.sha256((DATA/f'actions-genus{g}.json').read_bytes()).hexdigest() for g in (2,3)},
            'checked':'All group orders, every input generating-vector relation, local orders, Riemann-Hurwitz, colored braid orbits, mirror action for planar signatures, all subgroup fixed-point counts, multipliers and unique positive maximal section extensions.'}
    (OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'summary':summary,'rows':len(tables),'planar_braid_checks':len(checks)},indent=2))

if __name__=='__main__':main()
