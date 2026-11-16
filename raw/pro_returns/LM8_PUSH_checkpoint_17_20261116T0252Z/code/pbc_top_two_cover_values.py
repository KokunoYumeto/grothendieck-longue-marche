#!/usr/bin/env python3
"""Evaluate actual central-cover images of the target and genuine frames.

The two values are coordinates for the chosen splitting. Without a separately
verified G86 quotient identity they are NOT a full obstruction calculation.
"""
from pathlib import Path
import hashlib,itertools,json,time
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=CODE/'pbc_iterated_shortcut_v2_original_source.json';s=json.loads(source.read_text())
cp=CODE/'pbc_two_top_certificate.json';c=json.loads(cp.read_text())
sp=CODE/'pbc_top_two_section.json';sec=json.loads(sp.read_text())
ap=CODE/'pbc_top_two_cover_actions.json';acts=json.loads(ap.read_text())
assert c['source_sha256']==sec['source_sha256']==acts['source_sha256']==sha(source)
d=72;C={(i,j):w for i,j,w in s['conjugates']}
def tail(w):return sum((e%2)<<(i-105) for i,e in zip(w[::2],w[1::2]))
M={g:[tail(C[i,g]) for i in range(105,177)] for g in range(1,105)}
A={g:int(sec['quotient_generator_corrections_hex'][str(g)],16) for g in range(1,105)}
def action(v,mat):
    z=0
    while v:
        b=v&-v;v^=b;z^=mat[b.bit_length()-1]
    return z
def quad(v,rows):
    z=0;w=v
    while w:
        b=w&-w;w^=b;z^=(rows[b.bit_length()-1]&v).bit_count()&1
    return z
pairs=list(itertools.combinations(range(d),2));out=[];start=time.time()
for fi,(hh,qr,ac) in enumerate(zip(c['invariant_alternating_forms_hex'],c['quadratic_refinements'],acts['covers']),1):
    B=int(hh,16);ql=int(qr['linear_part_hex'],16);crow=[0]*d
    for i in range(d):
        if ql>>i&1:crow[i]|=1<<i
    for k,(i,j) in enumerate(pairs):
        if B>>k&1:crow[i]|=1<<j
    def cocycle(v,w):
        z=0
        while v:
            b=v&-v;v^=b;z^=(crow[b.bit_length()-1]&w).bit_count()&1
        return z
    Q={};L={g:int(ac['linear_action_corrections_hex'][str(g)],16) for g in range(1,105)}
    for g in range(1,105):
        rows=[0]*d
        for i,j in pairs:
            if cocycle(M[g][i],M[g][j])^((crow[i]>>j)&1):rows[i]|=1<<j
        Q[g]=rows
    def value(w):
        v=z=0
        for i,e in zip(w[::2],w[1::2]):
            assert 1<=i<=176 and isinstance(e,int) and e>=0
            for _ in range(e):
                if i<=104:
                    z^=quad(v,Q[i])^((L[i]&v).bit_count()&1)
                    v=action(v,M[i]);a=A[i]
                else:a=1<<(i-105)
                z^=cocycle(v,a);v^=a
        return v,z
    def central_difference(w1,w2):
        v1,z1=value(w1);v2,z2=value(w2);assert v1==v2
        return z1^z2
    ss,rr=s['s'],s['r'];aa,bb=s['s_image'],s['r_image']
    bs,br=s['left_s_frame'],s['left_r_frame']
    components=[central_difference(bs+ss,aa+bs),central_difference(br+rr,bb+br),central_difference(aa+bb,ss+rr)]
    sframes=[central_difference(w+ss,ss+w) for w in s['s_centralizers']]
    rframes=[central_difference(w+rr,rr+w) for w in s['r_centralizers']]
    assert not any(rframes)
    out.append(dict(form_index=fi,target_components=components,target_value=sum(components)%2,
                    s_frame_values=sframes,r_frame_values=rframes,
                    s_frame_nonzero_positions=[i+1 for i,v in enumerate(sframes) if v]))
report=dict(status='Computed actual central-cover values; quotient identity still required',
            source_sha256=sha(source),module_certificate_sha256=sha(cp),section_sha256=sha(sp),
            cover_action_sha256=sha(ap),checker_sha256=sha(__file__),covers=out,
            seconds=time.time()-start,
            scope='These two covers detect the top homology kernel. Their values do not by themselves prove the G86 quotient target is zero. The old G86 source replay failed; C31 remains Open.')
(CODE/'pbc_top_two_cover_values.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
