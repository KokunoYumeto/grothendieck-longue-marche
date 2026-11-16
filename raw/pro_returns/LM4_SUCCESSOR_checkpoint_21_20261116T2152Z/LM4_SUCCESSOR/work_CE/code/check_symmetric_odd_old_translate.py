#!/usr/bin/env python3
"""The two directions of the actual odd q=1 retained-module translate.

The canonical second-sheet source lasso is b*node*b^-1 and thus uses
geometric pullback alpha_b^-1.  Positive push alpha_b is compared through
the actual returned source generator b^2.  No conjugate-match shortcut
between a source defect and a single node relator is used.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_paired_fox_data.json',P/'symmetric_F_node_matching.json',
       P/'symmetric_full_source_data.json',P/'symmetric_source_node_alignment.json',
       ROOT/'work_DE/next_marginal_source/symmetric_old_actions_review.json']
raw=[p.read_bytes() for p in paths]
paired,matching,source,alignment,oldchecks=[json.loads(r) for r in raw]

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(i):tuple(w) for i,w in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]

F=mp(paired['paired_involution']);beta=mp(paired['retained_involution'])
to_pair=mp(paired['nodal_cut_basis_in_paired_basis'])
push=mp(paired['old_actions'][1]['geometric_push_paired'])
pull=mp(paired['old_actions'][1]['based_pullback_paired'])
kpush=sub(oldchecks['loops'][1]['F_commutator_inner_word'],to_pair)
kpull=sub(inv(kpush),pull)
ret=paired['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(ret)}
fill5={j:((hm[j],) if j in hm else ()) for j in range(1,22)}
meta={int(i):(tuple(r['retained_word']),r['paired_slot'])
      for i,r in paired['finite_used_common_R_basis'].items()}
idx={v:i for i,v in meta.items()}
def bid(g,i):
    if (g,i) not in idx:
        n=max(meta,default=0)+1;idx[g,i]=n;meta[n]=(g,i)
    return idx[g,i]
def rw(w):
    g=();out=[]
    for x in w:
        i=abs(x);sgn=1 if x>0 else -1
        if i in hm:g=red(g+(sgn*hm[i],))
        else:
            a=i<12;n=bid(g if a else sub(g,beta),i if a else i-10)
            out.append(sgn*(2*n-1 if a else 2*n))
    assert not g
    return red(out)
def isA(x):return abs(x)%2==1
def rid(x):return (abs(x)+1)//2
def proj(w,a):return red((1 if x>0 else -1)*rid(x) for x in w if isA(x)==a)
def cells(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x)
        if isA(x):
            an=red(a+(y,));av=a if y>0 else an;bp=()
            for z in b:
                bn=red(bp+(z,));bv=bp if z>0 else bn
                add(out,(av,bv,abs(y),abs(z)),-(1 if y>0 else -1)*(1 if z>0 else -1))
                bp=bn
            a=an
        else:b=red(b+(y,))
    assert not a and not b
    return dict(out)
def diagonal(c):
    out=defaultdict(int)
    for (u,v,i,j),n in c.items():
        if u==v and i==j:
            add(out,red(u+(i,)),n);add(out,u,-n)
    return {w:n%2 for w,n in out.items() if n%2}
def encode(c):
    return [{'A_vertex':u,'B_vertex':v,'A_generator':i,'B_generator':j,'coefficient':n}
            for (u,v,i,j),n in sorted(c.items())]

TAU,TAU1=101,102
def il(x):return x if x in (TAU,TAU1) else -x
def er(w):
    out=[]
    for x in w:
        if out and out[-1]==il(x):out.pop()
        else:out.append(x)
    return tuple(out)
def ei(w):return tuple(il(x) for x in reversed(w))
def emb(w):
    out=[]
    for x in w:
        i=abs(x);v=(TAU1,TAU) if i==1 else (i,) if i<=11 else (TAU,i-10,TAU)
        out.extend(v if x>0 else ei(v))
    return er(out)
def sch(w):
    par=0;out=[]
    for x in w:
        if x==TAU:par^=1
        elif x==TAU1:out.append(1 if par==0 else -1);par^=1
        else:out.append((1 if x>0 else -1)*(abs(x)+(10 if par else 0)))
    assert not par
    return red(out)
def half(g):
    z=er((TAU,)+emb(g));assert not er(z+z)
    p=[];core=z
    while len(core)>1 and core[0]==il(core[-1]):p.append(core[0]);core=core[1:-1]
    assert core in ((TAU,),(TAU1,))
    if core==(TAU1,):return core,None,p
    if sum(x in (TAU,TAU1) for x in p)%2:p=er(tuple(p)+(TAU,))
    h=sch(p);assert red(sub(h,F)+inv(h))==g
    return core,h,p

kept=source['first_family_F13_kept_paired_indices']
unfill13={i+1:(j,) for i,j in enumerate(kept)}
branch=next(r for r in source['old_source_generators'] if r['name']=='branch_square')
branch13=mp(branch['source_push_F13']);branch13inv=mp(branch['source_pullback_F13'])
witnesses=[]
for seed in source['source_peripheral_generators']:
    if seed['sheet']!=1:continue
    rho13=tuple(seed['positive_source_word_F13'])
    for power,A in [(0,None),(1,branch13),(-1,branch13inv)]:
        word13=rho13 if A is None else sub(rho13,A)
        word=rw(sub(word13,unfill13));assert not proj(word,False)
        witnesses.append({'critical_index':seed['critical_index'],'sheet':1,
                          'source_branch_square_power':power,'R_word':proj(word,True)})

nodes={(r['loop_index'],r['local_node_index']):r for r in paired['node_columns']}
rows=[];started=time.monotonic()
for direction,A,k in [('positive_push',push,kpush),('canonical_second_sheet_pullback',pull,kpull)]:
    # Independent full-basis check of the discrepancy used in coefficient transport.
    for j in range(1,22):
        assert sub(sub(A[j],F),{i:(i,) for i in range(1,22)})==red(k+sub(F[j],A)+inv(k))
    neutral=0
    for row in matching['rows']:
        if not row['fixed_physical_node']:continue
        key=tuple(row['node_index']);g=red(k+sub(row['conjugator_F21'],A))
        assert not red(sub(g,F)+g)
        core,h,prefix=half(g)
        rec={'direction':direction,'node_index':key,'translated_matching_conjugator_F21':g,
             'retained_cocycle':sub(g,fill5),'cone_core':core,'free_product_prefix':prefix,
             'neutral':h is not None}
        if h is None:
            rows.append(rec);continue
        neutral+=1
        rr=tuple(nodes[key]['paired_relator'])
        eps=row['A_first_orientation_signs'][0]
        if eps<0:rr=inv(rr)
        translated=sub(rr,A)
        assert sub(translated,F)==red(g+inv(translated)+inv(g))
        antiword=red(inv(h)+translated+h)
        assert sub(antiword,F)==inv(antiword)
        w=rw(antiword);assert not proj(w,True) and not proj(w,False)
        c=cells(w)
        assert c=={(v,u,j,i):n for (u,v,i,j),n in c.items()}
        psi=diagonal(c);found=[]
        if len(psi)==2:
            for s in psi:
                for source_row in witnesses:
                    rho=source_row['R_word']
                    for sign in (1,-1):
                        rho1=rho if sign>0 else inv(rho)
                        if set(psi)=={s,red(s+rho1)}:
                            found.append(dict(source_row,power=sign,left_coefficient_R=s,
                                              exact_identity='diagonal=s*(rho^power-1)'))
        rec.update({'free_product_half_h_F21':h,'coefficient_half_word_F21':inv(h),
                    'translated_A_first_relator':translated,'actual_integral_anti_word':antiword,
                    'actual_integral_anti_chain':encode(c),
                    'Tate_diagonal':[{'word':x,'coefficient_F2':n} for x,n in sorted(psi.items())],
                    'actual_source_zero_witnesses':found})
        rows.append(rec)
        print('CHECK odd translated anti-chain',direction,key,'word',len(antiword),'cells',len(c),
              'diagonal_terms',len(psi),'source_matches',[(x['critical_index'],x['source_branch_square_power'],x['power']) for x in found],flush=True)
    assert neutral==4

matched=all(r.get('actual_source_zero_witnesses') for r in rows if r['neutral'])
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'common_R_basis':{i:{'retained_word':g,'paired_slot':j} for i,(g,j) in meta.items()},
     'coefficient_formula':'a_translated=k_alpha*alpha(a_original)',
     'source_orientation':'canonical second-sheet b*node*b^-1 uses geometric pullback alpha_b^-1; positive alpha_b is compared using actual returned b^2 source action',
     'rows':rows,'all_eight_anti_chains_have_actual_source_witness':matched,
     'claims_excluded':['whole old-base orbit overlap vanishing','I=R'],
     'elapsed_seconds':time.monotonic()-started}
(P/'symmetric_odd_old_translate.json').write_text(json.dumps(out,indent=2)+'\n')
print(('PASS' if matched else 'PARTIAL'),'odd two-coset coefficient classification and eight exact anti-chains; source witnesses',matched,'elapsed',round(out['elapsed_seconds'],3),flush=True)
