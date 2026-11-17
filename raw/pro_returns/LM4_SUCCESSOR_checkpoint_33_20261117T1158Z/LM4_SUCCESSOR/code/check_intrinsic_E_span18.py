#!/usr/bin/env python3
"""Exact monomial elimination for the E-span of 64 actual columns and F images.

E=R x R; coefficients are integral group-ring elements. This bounded
submodule includes arbitrary E coefficients, but no assertion that all
retained-deck/old-base translates lie in it is made. Every basis change
uses a displayed unit monomial and is reversible over Z[E].
"""
from pathlib import Path
from collections import defaultdict
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json'
raw=INPUT.read_bytes();data=json.loads(raw)
OUT=ROOT/'records/intrinsic_E_span18.json'

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def mul(a,b):return red(a[0]+b[0]),red(a[1]+b[1])
def inverse(a):return inv(a[0]),inv(a[1])
ONE=((),())
def add(d,k,n):
    if n:
        d[k]=d.get(k,0)+n
        if not d[k]:del d[k]
def grmul(a,b):
    out={}
    for g,m in a.items():
        for h,n in b.items():add(out,mul(g,h),m*n)
    return out
def scaled_sub(col,q,pivot):
    for row,p in pivot.items():
        target=col.setdefault(row,{})
        for g,n in grmul(q,p).items():add(target,g,-n)
        if not target:del col[row]
def parse(xs):
    out={}
    for x in xs:
        row=(int(x['A_generator']),int(x['B_generator']))
        g=(tuple(x['A_vertex']),tuple(x['B_vertex']))
        add(out.setdefault(row,{}),g,int(x['coefficient']))
    return {r:p for r,p in out.items() if p}
def flip(col):
    return {(j,i):{(b,a):-n for (a,b),n in p.items()} for (i,j),p in col.items()}
def clone(c):return {r:dict(p) for r,p in c.items()}
def encode_gr(p):return [{'A_word':a,'B_word':b,'coefficient':n} for (a,b),n in sorted(p.items())]
def encode_col(c):return [{'row':r,'terms':encode_gr(p)} for r,p in sorted(c.items())]
def size(c):return sum(len(p) for p in c.values())
def unit(p):return len(p)==1 and abs(next(iter(p.values())))==1

started=time.monotonic()
seed=[parse(r['fox_cells']) for r in data['node_columns']]
assert len(seed)==64
assert all(flip(c)==parse(r['F_fox_cells']) for c,r in zip(seed,data['node_columns']))
original=seed+[flip(c) for c in seed]
columns={j:clone(c) for j,c in enumerate(original)}
representations={j:{j:{ONE:1}} for j in columns}
pivots=[];zero=[];steps=[];limit=500000
print('Start128 actual columns over Z[R x R]; terms',sum(size(c) for c in columns.values()),flush=True)
while columns:
    for j in list(columns):
        if not columns[j]:
            zero.append((j,representations.pop(j)));del columns[j]
    if not columns:break
    support=defaultdict(int)
    for c in columns.values():
        for row in c:support[row]+=1
    choices=[]
    for j,c in columns.items():
        for row,p in c.items():
            if unit(p):choices.append((support[row],size(c),size(representations[j]),j,row))
    if not choices:break
    _,_,_,j,row=min(choices)
    pivot=columns.pop(j);rep=representations.pop(j)
    monomial,sign=next(iter(pivot[row].items()))
    uinv={inverse(monomial):sign}
    changes=[]
    for k,c in columns.items():
        if row not in c:continue
        q=grmul(c[row],uinv)
        changes.append({'column':k,'left_multiplier':encode_gr(q)})
        scaled_sub(c,q,pivot);scaled_sub(representations[k],q,rep)
        assert row not in c
    pivots.append((j,row,monomial,sign,pivot,rep))
    steps.append({'pivot_column':j,'row':row,'pivot_monomial':monomial,'sign':sign,'changes':changes})
    term_count=sum(size(c) for c in columns.values())+sum(size(c) for c in representations.values())
    print('Pivot',len(pivots),'column',j,'row',row,'remaining',len(columns),'zero',len(zero),'active terms',term_count,flush=True)
    if term_count>limit:
        print('STOP exact term budget',limit,flush=True);break

# Verify every retained basis/kernel expression directly in the original matrix.
def evaluate(rep):
    out={}
    for j,p in rep.items():
        neg={g:-n for g,n in p.items()}
        scaled_sub(out,neg,original[j])
    return out
for j,row,m,s,c,rep in pivots:assert evaluate(rep)==c
for j,rep in zero:assert not evaluate(rep)
for j,c in columns.items():assert evaluate(representations[j])==c

def decode_gr(p):return {(tuple(t['A_word']),tuple(t['B_word'])):int(t['coefficient']) for t in p}
def cyclic_core(w):
    w=tuple(w)
    while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
    return w
private_support=defaultdict(list)
for j,c in columns.items():
    for row in c:private_support[row].append(j)
binomial_witnesses=[]
for j,c in columns.items():
    found=None
    for row,p in sorted(c.items()):
        if private_support[row]!=[j] or len(p)!=2:continue
        (g,m),(h,n)=sorted(p.items())
        if abs(m)!=1 or n!=-m:continue
        shift=mul(h,inverse(g))
        assert shift!=ONE
        axis=0 if shift[0] else 1
        core=cyclic_core(shift[axis]);assert core
        found={'column':j,'row':row,'binomial':encode_gr(p),
          'right_translation':shift,'nontrivial_coordinate':axis,'cyclically_reduced_core':core,
          'injectivity_proof':'a(g-h)=0 implies a=a*h*g^-1; a finite support cannot be invariant under an infinite-order right translation.'}
        break
    if found:binomial_witnesses.append(found)
closed=len(binomial_witnesses)==len(columns)
print('Private infinite-order binomial witnesses',len(binomial_witnesses),'of',len(columns),flush=True)

def domainF(rep):return {(j+64)%128:{(b,a):n for (a,b),n in p.items()} for j,p in rep.items()}
def final_coordinates(rep):
    out=clone(rep)
    for step in steps:
        j=step['pivot_column']
        for change in step['changes']:
            k=change['column']
            if k not in out:continue
            extra=grmul(out[k],decode_gr(change['left_multiplier']))
            target=out.setdefault(j,{})
            for g,n in extra.items():add(target,g,n)
            if not target:del out[j]
    return out

image_entries=[(j,c,rep) for j,_,_,_,c,rep in pivots]+[(j,c,representations[j]) for j,c in columns.items()]
image_ids={j:k for k,(j,_,_) in enumerate(image_entries)}
zero_ids={j:k for k,(j,_) in enumerate(zero)}
Fmatrix=[];kernel_Fmatrix=[];monomial_F=True;kernel_monomial=True
if closed:
    for k,(j,c,rep) in enumerate(image_entries):
        full=final_coordinates(domainF(rep))
        coeff={image_ids[i]:p for i,p in full.items() if i in image_ids}
        rebuilt={}
        for i,p in coeff.items():scaled_sub(rebuilt,{g:-n for g,n in p.items()},image_entries[i][1])
        assert rebuilt==flip(c)
        Fmatrix.append(coeff)
        if len(coeff)!=1 or not unit(next(iter(coeff.values()))):monomial_F=False
    for k,(j,rep) in enumerate(zero):
        full=final_coordinates(domainF(rep))
        assert not (set(full)&set(image_ids))
        coeff={zero_ids[i]:p for i,p in full.items()}
        kernel_Fmatrix.append(coeff)
        if len(coeff)!=1 or not unit(next(iter(coeff.values()))):kernel_monomial=False
    # F is semilinear: check its exact square on each free module.
    for matrix in (Fmatrix,kernel_Fmatrix):
        for k,coeff in enumerate(matrix):
            out={}
            for j,p in coeff.items():
                fp={(b,a):n for (a,b),n in p.items()}
                for l,q in matrix[j].items():
                    d=out.setdefault(l,{})
                    for g,n in grmul(fp,q).items():add(d,g,n)
                    if not d:del out[l]
            assert out=={k:{ONE:1}}

result={'scope':__doc__,'input_sha256':hashlib.sha256(raw).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'column_labels':[[r['loop_index'],r['local_node_index'],'seed'] for r in data['node_columns']]+[[r['loop_index'],r['local_node_index'],'F_image'] for r in data['node_columns']],
 'common_R_basis':data['finite_used_common_R_basis'],
 'input_columns':128,'pivot_rank':len(pivots),'free_image_rank':len(image_entries) if closed else None,'zero_kernel_generators':len(zero),
 'remaining_columns':len(columns),'term_limit':limit,'complete_free_image_basis':closed,
 'elimination_steps':steps,
 'image_basis':[{'original_column':j,'pivot_row':row,'chain':encode_col(c),'expression':encode_col(rep)} for j,row,m,s,c,rep in pivots],
 'kernel_basis':[{'original_column':j,'expression':encode_col(rep)} for j,rep in zero],
 'uneliminated':[{'original_column':j,'chain':encode_col(c),'expression':encode_col(representations[j])} for j,c in columns.items()],
 'private_binomial_witnesses':binomial_witnesses,
 'free_image_original_ids':[j for j,_,_ in image_entries],
 'F_matrix_in_free_image_basis':[encode_col(c) for c in Fmatrix],
 'F_matrix_in_kernel_basis':[encode_col(c) for c in kernel_Fmatrix],
 'F_action_monomial':monomial_F if closed else None,
 'kernel_F_action_monomial':kernel_monomial if closed else None,
 'elapsed_seconds':time.monotonic()-started,
 'claims_excluded':['all old-base/deck translates exhausted','global kappa vanishing','I equals R','nonlinear fixed lifting']}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact basis changes: unit rank',len(pivots),'free image rank',len(image_entries) if closed else None,'kernel',len(zero),'residual independent',len(binomial_witnesses),'monomial image/kernel F',monomial_F if closed else None,kernel_monomial if closed else None,'seconds',round(result['elapsed_seconds'],3),flush=True)
