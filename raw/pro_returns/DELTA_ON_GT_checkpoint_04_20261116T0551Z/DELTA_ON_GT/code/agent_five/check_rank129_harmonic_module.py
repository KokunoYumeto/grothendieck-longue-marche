"""The actual16-dimensional harmonic orbit as an abelian F3 extension.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json,sys
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129_blocks.npz');D=np.load(ROOT/'ferrari_rank129_boundary.npz')
second='--second' in sys.argv
orb=(8,14,27,29)if second else(1,7,18,20);n=4;offset=F['offsets'];perms=F['x_permutations'];I2=(1,0,0,1)
Q0=tuple(range(n))+I2*n+I2*n;V0=(0,)*16
def m2(a,b):
    aa,bb,cc,dd=a;e,f,g,h=b
    return((aa*e+bb*g)%3,(aa*f+bb*h)%3,(cc*e+dd*g)%3,(cc*f+dd*h)%3)
def inv2(a):
    aa,b,c,d=a;det=(aa*d-b*c)%3;assert det
    return(det*d%3,-det*b%3,-det*c%3,det*aa%3)
def qm(g,h):
    pg,ph=g[:4],h[:4];B=[];P=[]
    for j in range(n):
        k=ph[j];B.extend(m2(g[4+4*k:8+4*k],h[4+4*j:8+4*j]));P.extend(m2(g[20+4*k:24+4*k],h[20+4*j:24+4*j]))
    return tuple(pg[ph[j]]for j in range(n))+tuple(B)+tuple(P)
def qi(g):
    p=g[:4];ip=tuple(p.index(j)for j in range(4));B=[];P=[]
    for j in range(n):
        k=ip[j];B.extend(inv2(g[4+4*k:8+4*k]));P.extend(inv2(g[20+4*k:24+4*k]))
    return ip+tuple(B)+tuple(P)
def act(g,v):
    out=[0]*16
    for j in range(n):
        k=g[j];value=m2(m2(g[4+4*j:8+4*j],v[4*j:4*j+4]),inv2(g[20+4*j:24+4*j]))
        out[4*k:4*k+4]=value
    return tuple(out)
def am(g,h):
    v,q=g;w,r=h;qw=act(q,w)
    return(tuple((v[i]+qw[i])%3 for i in range(16)),qm(q,r))
def ai(g):
    v,q=g;r=qi(q);rv=act(r,v)
    return(tuple(-x%3 for x in rv),r)
def ap(*gg):
    g=(V0,Q0)
    for h in gg:g=am(g,h)
    return g
def comm(g,h):return ap(g,h,ai(g),ai(h))
def basis(rows):
    piv={}
    for vv in rows:
        v=list(vv)
        for j,w in sorted(piv.items()):
            z=v[j]
            if z:v=[(x-z*y)%3 for x,y in zip(v,w)]
        nz=[j for j,x in enumerate(v)if x]
        if nz:
            j=nz[0];u=v[j];piv[j]=tuple(u*x%3 for x in v)
    return[piv[j]for j in sorted(piv)]
gens=[]
for k in (0,1):
    M=D['X'][k];pg=[];B=[];P=[];v=[0]*16
    for j,mask in enumerate(orb):
        target=int(perms[k,mask]);l=orb.index(target);pg.append(l)
        aa,bb=offset[mask];cc,dd=offset[target]
        block=M[cc:dd,aa:bb];assert block.shape==(4,4)and not np.any(block[2:,:2])
        Bj=tuple(map(int,block[:2,:2].ravel()));Pj=tuple(map(int,block[2:,2:].ravel()));Cj=tuple(map(int,block[:2,2:].ravel()))
        B.extend(Bj);P.extend(Pj);v[4*l:4*l+4]=m2(Cj,inv2(Pj))
    gens.append((tuple(v),tuple(pg)+tuple(B)+tuple(P)))
for g in gens:assert ap(g,ai(g))==(V0,Q0)

sec={Q0:V0};todo=[Q0];pos=0
while pos<len(todo):
    q=todo[pos];pos+=1
    for g in gens:
        v,r=am((sec[q],q),g)
        if r not in sec:sec[r]=v;todo.append(r)
    if len(todo)>250000:raise RuntimeError('Base exceeds250000; use structural reduction before proceeding')
loops=[]
for q,v in sec.items():
    for g in gens:
        h=am((v,q),g);z=am(h,ai((sec[h[1]],h[1])))
        assert z[1]==Q0;loops.append(z[0])
W=basis(loops)
for g in gens:
    for w in W:assert len(basis(W+[act(g[1],w)]))==len(W)

def qclosure(gg):
    G=[Q0];seen={Q0}
    for q in G:
        for g in gg:
            r=qm(q,g)
            if r not in seen:seen.add(r);G.append(r)
    return G
def qc(g,h):return qm(qm(qm(g,h),qi(g)),qi(h))
base_series=[];G=todo;gg=[g[1]for g in gens]
while True:
    base_series.append(len(G))
    if len(G)==1:break
    gg=list({qc(g,h)for g in G for h in gg});G=qclosure(gg)
    if len(base_series)>6:break
np.savez_compressed(ROOT/('ferrari_harmonic16_second_module.npz'if second else'ferrari_harmonic16_module.npz'),base=np.array(todo,dtype=np.int16),
                    sections=np.array([sec[q]for q in todo],dtype=np.int16),
                    kernel_basis=np.array(W,dtype=np.int16),
                    generator_bases=np.array([g[1]for g in gens],dtype=np.int16),
                    generator_translations=np.array([g[0]for g in gens],dtype=np.int16))
print(json.dumps({'character_orbit':orb,'representation_dimension':16,
 'boundary_dimension':8,'proper_dimension':8,'ambient_extension_module_dimension':16,
 'actual_base_order':len(todo),'actual_kernel_dimension':len(W),
 'actual_harmonic_pair_order':len(todo)*3**len(W),'base_derived_series':base_series,
 'kernel_basis':W,'generator_bases':[g[1]for g in gens],
 'generator_translations':[g[0]for g in gens],
 'scope':'Exact Schreier module of the literal two-generator image; no f-parameter enumeration.'},indent=2))
