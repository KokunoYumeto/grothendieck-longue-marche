#!/usr/bin/env python3
"""Complete named pure-braid complexes of groups on P_2 for M_0,5 and M_0,6.

Words list crossings in traversal order, as in b_genus_zero.py.  Tree vertices
keep their indices from a_graphs_0_n.json.  A local letter [v,i,j,e] denotes
the signed A_ij generator of the zero-framed PB_q factor at vertex v.
The program imports only function definitions from B's exact Artin-action
and combing certificate; it does not execute or rewrite B's computations.
"""
from pathlib import Path
from itertools import combinations
from collections import deque
import ast,json

P=Path(__file__).resolve().parent
source=ast.parse((P/'b_genus_zero.py').read_text())
defs=ast.Module(body=[a for a in source.body if isinstance(a,ast.FunctionDef)],type_ignores=[])
exec(compile(defs,str(P/'b_genus_zero.py'),'exec'),globals())

def delete(n,w,keep):
    keep=set(keep);labels=list(range(1,n+1));out=[]
    for x in w:
        i=abs(x)-1
        if labels[i] in keep and labels[i+1] in keep:
            k=1+sum(a in keep for a in labels[:i])
            out.append(k if x>0 else -k)
        labels[i],labels[i+1]=labels[i+1],labels[i]
    assert labels==list(range(1,n+1))
    return red(out)

def positive_block_swap(a,b,offset=0):
    return tuple(offset+k for j in range(b) for k in range(a+j,j,-1))

def cable(w,sizes,offset=0):
    sizes=list(sizes);out=[]
    for x in w:
        i=abs(x)-1;s=offset+sum(sizes[:i]);a,b=sizes[i:i+2]
        z=positive_block_swap(a,b,s) if x>0 else inv(positive_block_swap(b,a,s))
        out.extend(z);sizes[i],sizes[i+1]=sizes[i+1],sizes[i]
    return red(out)

def cyclic(w):
    w=red(w)
    while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
    return min(z[i:]+z[:i] for z in (w,inv(w)) for i in range(len(z))) if w else ()

def tree(G):
    genera,legs,edges=G;n=len(legs);root=legs[-1];adj={v:[] for v in range(len(genera))}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    nodes={}
    def rec(v,parent):
        children=[{'leaf':i+1,'leaves':(i+1,)} for i,x in enumerate(legs[:-1]) if x==v]
        for u in adj[v]:
            if u!=parent:
                rec(u,v);children.append({'vertex':u,'leaves':nodes[u]['leaves']})
        children.sort(key=lambda x:min(x['leaves']))
        leaves=tuple(a for c in children for a in c['leaves'])
        nodes[v]={'children':children,'leaves':leaves,'q':len(children)}
    rec(root,None)
    order=nodes[root]['leaves'];perm=transport(order);m=n-1
    clusters={frozenset(z['leaves']) for v,z in nodes.items() if v!=root}
    curves={}
    ap=action(m,inv(perm))
    for c in clusters:
        ix=[i+1 for i,a in enumerate(order) if a in c]
        assert ix==list(range(min(ix),max(ix)+1))
        curves[c]=cyclic(subst(tuple(ix),ap))
    for v,z in nodes.items():
        z['offset']=order.index(z['leaves'][0])
    return {'root':root,'nodes':nodes,'order':order,'P':perm,'clusters':clusters,'curves':curves}

def round_generator(T,v,i,j):
    z=T['nodes'][v]
    return cable(A(i,j),[len(c['leaves']) for c in z['children']],z['offset'])

def expand_local(T,word):
    return red(a for v,i,j,e in word for a in (round_generator(T,v,i,j) if e>0 else inv(round_generator(T,v,i,j))))

def factor(T,w):
    """Exact decomposition of a round-system stabilizer into its PB factors."""
    out=[]
    def rec(v,w):
        z=T['nodes'][v];sizes=[len(c['leaves']) for c in z['children']];m=sum(sizes)
        starts=[];s=1
        for a in sizes:starts.append(s);s+=a
        outer=delete(m,w,starts)
        aw=comb(len(sizes),outer)
        out.extend((v,i,j,e) for i,j,e in aw)
        residual=red(inv(cable(outer,sizes))+w)
        for c,start,a in zip(z['children'],starts,sizes):
            if 'vertex' in c:
                rec(c['vertex'],delete(m,residual,range(start,start+a)))
        assert eq(m,outer,expand(aw))
    rec(T['root'],w)
    assert eq(len(T['order']),w,expand_local(T,out))
    return out

def pure_relators(q):
    rel=[]
    for ell in range(3,q+1):
        for i,j in combinations(range(1,ell),2):
            for k in range(1,ell):
                h=A(i,j);u=A(k,ell);image=comb(ell,h+u+inv(h))
                assert all(b==ell for a,b,e in image)
                rel.append([(i,j,1),(k,ell,1),(i,j,-1)]+[(a,b,-e) for a,b,e in reversed(image)])
    for r in rel:assert eq(q,expand(r),())
    return rel

def run(n):
    data=json.loads((P/f'a_graphs_0_{n}.json').read_text());graphs=data['graphs'];m=n-1;d=n-3
    indices=[i for i,G in enumerate(graphs) if len(G[2])>=d-2]
    tt={i:tree(graphs[i]) for i in indices};vertices=[];nlocal=0;ncentral=0
    for i in indices:
        T=tt[i];gens=[];localrels=[];fullword=[]
        for v,z in sorted(T['nodes'].items()):
            q=z['q'];assert q>=2
            for a,b in combinations(range(1,q+1),2):
                rnd=round_generator(T,v,a,b);globalword=red(T['P']+rnd+inv(T['P']))
                k,norm=normalized(m,globalword)
                gens.append({'name':[v,a,b],'round_braid':rnd,'global_braid':globalword,'central_power':k,'moduli_word':norm})
            localrels.extend([[(v,a,b,e) for a,b,e in r] for r in pure_relators(q)])
            fullword.extend((v,a,b,1) for b in range(2,q+1) for a in range(1,b))
        assert eq(m,expand_local(T,fullword),full(m));ncentral+=1
        for a,b in combinations(gens,2):
            if a['name'][0]!=b['name'][0]:
                assert eq(m,a['round_braid']+b['round_braid'],b['round_braid']+a['round_braid'])
                va,ia,ja=a['name'];vb,ib,jb=b['name']
                localrels.append([(va,ia,ja,1),(vb,ib,jb,1),(va,ia,ja,-1),(vb,ib,jb,-1)])
        nlocal+=len(gens)
        vertices.append({'graph_index':i,'graph':graphs[i],'root_vertex':T['root'],'leaf_order':T['order'],'permutation_braid':T['P'],
                         'factors':{v:{'q':z['q'],'children':[c['leaves'] for c in z['children']]} for v,z in T['nodes'].items()},
                         'generators':gens,'relators':localrels+[fullword], 'central_diagonal_relation':fullword})
    ar={};arrows=[];ninjections=0;nzero=0
    for g in indices:
        G=tt[g]
        for h in data['contractions'][g]:
            if h==g or h not in tt:continue
            H=tt[h];assert H['clusters']<G['clusters']
            relorder=tuple(H['order'].index(a)+1 for a in G['order'])
            B=transport(relorder)
            for c in H['clusters']:
                ih=tuple(i+1 for i,a in enumerate(H['order']) if a in c)
                ig=tuple(i+1 for i,a in enumerate(G['order']) if a in c)
                assert cyclic(subst(ih,action(m,B)))==cyclic(ig)
            q=red(H['P']+B+inv(G['P']))
            assert permutation(m,q)==tuple(range(1,m+1))
            same=all(G['curves'][c]==H['curves'][c] for c in H['clusters'])
            if same:q=();nzero+=1
            inj=[]
            for z in vertices[indices.index(g)]['generators']:
                x=z['global_braid'];image=red(q+x+inv(q))
                rnd=red(inv(H['P'])+image+H['P']);local=factor(H,rnd)
                inj.append({'source_generator':z['name'],'target_local_word':local})
                ninjections+=1
            k,norm=normalized(m,q)
            z={'source':g,'target':h,'braid':q,'moduli_word':norm,'central_power':k,'injections':inj}
            arrows.append(z);ar[g,h]=q
    # Prefer an entirely zero-transporter maximal tree.  This makes all local
    # embeddings and every A_ij inverse generator literal, without gauges.
    adj={i:[] for i in indices}
    for (g,h),q in ar.items():
        if not q:adj[g].append(h);adj[h].append(g)
    root=indices[0];seen={root};todo=deque([root]);spanning=[]
    while todo:
        g=todo.popleft()
        for h in sorted(adj[g]):
            if h not in seen:seen.add(h);todo.append(h);spanning.append([g,h])
    assert seen==set(indices),('zero-tree disconnected',n,len(seen),len(indices))
    triangles=[]
    for g,h in ar:
        for j in data['contractions'][h]:
            if (h,j) not in ar:continue
            f=red(ar[h,j]+ar[g,h]+inv(ar[g,j]));T=tt[j]
            loc=factor(T,red(inv(T['P'])+f+T['P']))
            k,norm=normalized(m,f)
            triangles.append({'vertices':[g,h,j],'target_local_word':loc,'braid':f,'moduli_word':norm,'central_power':k})
    inverse=[]
    for a,b in combinations(range(1,m+1),2):
        if (a,b)==(1,2):continue
        g=next(i for i,T in tt.items() if T['clusters']=={frozenset((a,b))})
        T=tt[g];v=next(v for v,z in T['nodes'].items() if set(z['leaves'])=={a,b})
        w=red(T['P']+round_generator(T,v,1,2)+inv(T['P']))
        assert eq(m,w,A(a,b))
        inverse.append({'A':[a,b],'graph_index':g,'local_generator':[v,1,2]})
    identities=[]
    if n==6:
        # Adjoin the empty multicurve (graph zero), the unique dimension-three
        # stratum.  Its transporters are all identity.  The following records
        # are the tetrahedral cocycle identities on every complete flag.
        for z in triangles:
            g,h,j=z['vertices'];left=red(ar[h,j]+ar[g,h]);right=red(z['braid']+ar[g,j])
            assert eq(m,left,right)
            identities.append({'flag':[g,h,j,0],
                'formula':'f(h,j,0) f(g,h,0) = psi(j,0)(f(g,h,j)) f(g,j,0)',
                'left_braid':left,'right_braid':right,
                'left_moduli_word':normalized(m,left)[1],
                'right_moduli_word':normalized(m,right)[1]})
    counts={'vertices':len(vertices),'arrows':len(arrows),'triangles':len(triangles),'local_generators':nlocal,
            'edge_generator_images':ninjections,'zero_transport_arrows':nzero,'tree_edges':len(spanning),
            'central_identities':ncentral,'inverse_generators':len(inverse),
            'dimension_three_flag_identities':len(identities)}
    print('M0,%s complete P2 certificate:'%n,counts,flush=True)
    return {'type':[0,n],'word_convention':'crossings in traversal order; arrow injection x -> q x q^-1',
            'counts':counts,'vertices':vertices,'arrows':arrows,'triangles':triangles,'maximal_tree':spanning,
            'inverse_moduli_generators':inverse,'dimension_three_identities':identities}

if __name__=='__main__':
    out=[run(n) for n in (5,6)]
    (P/'d_p2_genus_zero.json').write_text(json.dumps(out,indent=2)+'\n')
