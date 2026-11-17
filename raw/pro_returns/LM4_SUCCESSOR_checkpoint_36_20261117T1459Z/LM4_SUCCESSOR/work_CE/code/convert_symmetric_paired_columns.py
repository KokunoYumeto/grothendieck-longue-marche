#!/usr/bin/env python3
"""Actual paired marking and 64 exact product-tree Fox columns.

Uses only the corrected geometric pullback along the certified source
bridge.  Both directions of each finite Nielsen map are checked.  The
Schreier indices are words in the actual retained free group F5.  The B
index is twisted by its involution, making F literally swap the common
R indices.  The six old actions are retained as operators; their full
infinite orbit closure and the node-relation syzygies are not computed.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes';D=ROOT/'work_DE/next_marginal_source'
files={'nodes':P/'symmetric_node_words_pullback_corrected.json',
       'bridge':P/'symmetric_source_bridge_pullback_corrected.json',
       'old':P/'symmetric_old_base_words_pullback_corrected.json',
       'fixed':D/'symmetric_fixed_basis.json'}
raw={k:p.read_bytes() for k,p in files.items()};data={k:json.loads(v) for k,v in raw.items()}
start=time.monotonic()
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def asmap(d):return {int(i):tuple(w) for i,w in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]

T=asmap(data['bridge']['endpoint_generators_in_nodal_base'])
Ti=asmap(data['bridge']['nodal_generators_in_endpoint_base'])
EF={i+1:tuple(r['word']) for i,r in enumerate(data['fixed']['paired_basis'])}
EI=asmap(data['fixed']['inverse_basis'])
forward={i:sub(w,T) for i,w in EF.items()}
inverse={i:sub(w,EI) for i,w in Ti.items()}
Fnodal=asmap(data['bridge']['nodal_involution_images'])
Fpair={1:(-1,)}
Fpair.update({i:(i+10,) for i in range(2,12)})
Fpair.update({i:(i-10,) for i in range(12,22)})
for i in range(1,22):
    assert sub(forward[i],inverse)==(i,)==sub(inverse[i],forward)
    assert sub(sub(forward[i],Fnodal),inverse)==Fpair[i]
retained=data['fixed']['retained_paired_indices'];assert retained==[1,4,9,14,19]
hmap={j:i+1 for i,j in enumerate(retained)}
hinverse={i:j for j,i in hmap.items()}
fillmap={j:((hmap[j],) if j in hmap else ()) for j in range(1,22)}
beta={i:sub(Fpair[j],fillmap) for i,j in hinverse.items()}
for i in range(1,6):assert sub(beta[i],beta)==(i,)
slots=[i for i in range(2,12) if i not in retained]
assert len(slots)==8
print('PASS actual paired Nielsen basis, all42 inverse substitutions, F axis inverse/ten pair swaps, retained F5.',flush=True)

# A common free basis of R indexed by (retained word, right paired slot).
# Kernel letters2*r-1 and2*r distinguish its A and B copies.
idx={};meta={}
def basis_id(g,i):
    key=(g,i)
    if key not in idx:
        r=len(idx)+1;idx[key]=r
        meta[r]={'retained_word':g,'paired_slot':i,
                 'paired_name':data['fixed']['paired_basis'][i-1]['name']}
    return idx[key]
def family(j):return 'A' if abs(j)%2 else 'B'
def rid(j):return (abs(j)+1)//2
def rword(w):return tuple((1 if x>0 else -1)*rid(x) for x in w)
def Fkernel(w):return tuple((1 if x>0 else -1)*(abs(x)+1 if abs(x)%2 else abs(x)-1) for x in w)
def rewrite(w):
    head=();out=[]
    for x in w:
        j=abs(x);sgn=1 if x>0 else -1
        if j in hmap:head=red(head+(sgn*hmap[j],))
        else:
            side='A' if j<12 else 'B';slot=j if side=='A' else j-10
            assert slot in slots
            g=head if side=='A' else sub(head,beta)
            r=basis_id(g,slot);out.append(sgn*(2*r-1 if side=='A' else 2*r))
    assert not head,('not in actual retained filling kernel',head)
    return red(out)
def expand(w):
    out=[]
    for x in w:
        m=meta[rid(x)];g=tuple(m['retained_word']);i=m['paired_slot']
        if family(x)=='B':g=sub(g,beta);i+=10
        g=tuple((1 if y>0 else -1)*hinverse[abs(y)] for y in g)
        v=mul(g,(i,),inv(g));out.extend(v if x>0 else inv(v))
    return red(out)
def proj(w,side):return red(x for x in w if family(x)==side)
def edge_cycle(w):
    a=b=();out=defaultdict(int)
    for x in w:
        if family(x)=='A':
            aa=red(a+(x,));apos=a if x>0 else aa
            add(out,('A',apos,b,abs(x)),1 if x>0 else -1);a=aa
        else:
            bb=red(b+(x,));bpos=b if x>0 else bb
            add(out,('B',a,bpos,abs(x)),1 if x>0 else -1);b=bb
    assert not a and not b
    return dict(out)
def fill(w):
    a=b=();out=defaultdict(int)
    for x in w:
        if family(x)=='A':
            aa=red(a+(x,));apos=a if x>0 else aa;sx=1 if x>0 else -1;bp=()
            for y in b:
                bn=red(bp+(y,));bpos=bp if y>0 else bn
                add(out,(apos,bpos,abs(x),abs(y)),-sx*(1 if y>0 else -1));bp=bn
            a=aa
        else:b=red(b+(x,))
    assert not a and not b
    return dict(out)
def boundary(cells):
    out=defaultdict(int)
    for (a,b,i,j),n in cells.items():
        add(out,('A',a,b,i),n);add(out,('A',a,red(b+(j,)),i),-n)
        add(out,('B',red(a+(i,)),b,j),n);add(out,('B',a,b,j),-n)
    return dict(out)
def normalized(cells):
    return {(rword(a),rword(b),rid(i),rid(j)):n for (a,b,i,j),n in cells.items()}
def encoded(cells):
    return [{'A_vertex':a,'B_vertex':b,'A_generator':i,'B_generator':j,'coefficient':n}
            for (a,b,i,j),n in sorted(cells.items())]

rows=[]
for loop in data['nodes']['loops']:
    for ni,node in enumerate(loop['nodes']):
        mer=[sub(w,inverse) for w in node['meridians']]
        rel=sub(node['commutator'],inverse)
        assert all(sub(w,forward)==tuple(old) for w,old in zip(mer,node['meridians']))
        assert sub(rel,forward)==tuple(node['commutator'])
        rr=rewrite(rel);mm=[rewrite(w) for w in mer]
        assert expand(rr)==rel and all(expand(w)==v for w,v in zip(mm,mer))
        assert rr==mul(mm[0],mm[1],inv(mm[0]),inv(mm[1]))
        assert not proj(rr,'A') and not proj(rr,'B')
        ff=rewrite(sub(rel,Fpair));assert ff==Fkernel(rr)
        cells=fill(rr);assert boundary(cells)==edge_cycle(rr)
        fcells=fill(ff);assert boundary(fcells)==edge_cycle(ff)
        nc=normalized(cells);nfc=normalized(fcells)
        assert nfc=={(b,a,j,i):-n for (a,b,i,j),n in nc.items()}
        rows.append({'loop_index':loop['index'],'local_node_index':ni,
            'physical_labels':node['physical_labels'],'paired_meridians':mer,
            'paired_relator':rel,'kernel_meridians':mm,'kernel_relator':rr,
            'fox_cells':encoded(nc),'F_fox_cells':encoded(nfc),
            'two_chain_terms':len(cells),'negative_swap_verified':True})
    print('PASS paired actual node columns and literal negative-swap action',loop['index'],flush=True)

actions=[]
for loop in data['old']['loops']:
    A=asmap(loop['geometric_push_images']);Ai=asmap(loop['based_pullback_images'])
    AP={i:sub(sub(forward[i],A),inverse) for i in range(1,22)}
    AI={i:sub(sub(forward[i],Ai),inverse) for i in range(1,22)}
    for i in range(1,22):assert sub(AP[i],AI)==(i,)==sub(AI[i],AP)
    ahead={i:sub(AP[j],fillmap) for i,j in hinverse.items()}
    aihead={i:sub(AI[j],fillmap) for i,j in hinverse.items()}
    for i in range(1,6):assert sub(ahead[i],aihead)==(i,)==sub(aihead[i],ahead)
    for i in range(1,22):
        if i not in hmap:assert not sub(AP[i],fillmap) and not sub(AI[i],fillmap)
    actions.append({'index':loop['index'],'name':loop['name'],
        'geometric_push_paired':AP,'based_pullback_paired':AI,
        'retained_push':ahead,'retained_pullback':aihead})
    print('PASS paired old action',loop['index'],'and exact retained F5 restriction.',flush=True)

out={'scope':__doc__,'input_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'paired_basis_forward_in_nodal_cut_basis':forward,
 'nodal_cut_basis_in_paired_basis':inverse,'paired_involution':Fpair,
 'retained_paired_indices':retained,'retained_involution':beta,
 'deleted_right_slots':slots,'finite_used_common_R_basis':meta,
 'kernel_letter_convention':'2*r-1 is A_r, 2*r is B_r; F swaps these. Common B index twists its retained head by beta.',
 'node_columns':rows,'old_actions':actions,
 'total_columns':len(rows),'total_two_chain_terms':sum(r['two_chain_terms'] for r in rows),
 'claims_excluded':['full old-base/deck orbit matrix','node-relation syzygy computation','Tate obstruction evaluation','nonabelian fixed lifting','completed coefficient identification'],
 'elapsed_seconds':time.monotonic()-start}
(P/'symmetric_paired_fox_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual paired64-column package;',len(meta),'finite used R indices;',out['total_two_chain_terms'],'cells; elapsed',round(out['elapsed_seconds'],3),flush=True)
