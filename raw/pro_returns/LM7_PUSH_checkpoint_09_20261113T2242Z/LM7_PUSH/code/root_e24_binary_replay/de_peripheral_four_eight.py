#!/usr/bin/env python3
"""Construct peripheral exponent-four points and test their full eight lifts.

Uses all old homology witness freedoms. First corrects the sixteen central
coinvariants using actual s-centralizer homology words, then solves the
entire central cusp equation by changes of both conjugators. The resulting
torsion generators are conjugates by construction. Their complete gentle
fibres at exponent eight, with both multipliers, are then calculated.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):e=runpy.run_path(str(here/'de_class2_eight.py'))
g=e['g'];d=e['d'];base=e['base'];v=e['v'];n=97;m=4753;up=e['up']
records=e['records'];collect=e['collect'];kernel=e['kernel'];start=time.time()
def invword(w):
    out=[]
    for t in reversed(w):
        if isinstance(t,tuple):
            a,z=t;out.append((-a, -z-np.outer(a,a)[up]))
        else:out.append(-t)
    return out
def from_v(a):
    out=[]
    for c,w in zip(a,base['Nwords']):
        if c>=0:out+=w*int(c)
        else:out+=base['binv'](w)*int(-c)
    return out
def four_error(w):
    a,z=collect(w);assert not np.any(a%2)
    return np.concatenate(((a//2)%2,z%2))
targets=[];changed=[]
for j,rec in enumerate(records):
    wb=rec['base_beta_word_B'];wa=rec['base_A_word_B']
    w=wb+[0]+invword(wb)+wa+[1]+invword(wa)+[-1,0]
    ob=four_error(w)@d['invariants']%2
    RR,pp=d['rref'](np.column_stack((d['var_s'],ob)))
    assert d['var_s'].shape[1] not in pp
    c=np.zeros(d['var_s'].shape[1],dtype=np.int64);c[pp]=RR[:len(pp),-1]
    vs=3*(d['fix_s']@c%2);wb=wb+from_v(vs)
    w=wb+[0]+invword(wb)+wa+[1]+invword(wa)+[-1,0]
    err=four_error(w);assert not np.any(err@d['invariants']%2)
    targets.append(err);changed.append((wb,wa,vs))
matrix=np.column_stack((d['D'].T,np.stack(targets,axis=1))).astype(np.uint8)
piv=np.zeros(min(matrix.shape),dtype=np.int32)
rank=d['gf'](matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,
             piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
pp=piv[:rank].tolist();assert all(i<2*m for i in pp)
prepared=[];worddata=[]
for j,(rec,(wb,wa,vs)) in enumerate(zip(records,changed)):
    sol=np.zeros(2*m,dtype=np.int64);sol[pp]=matrix[:rank,2*m+j]
    B,A=sol[:m],sol[m:];B=(B+d['D'][m:].T.astype(np.int64)@A)%2
    Kb=(6*B[:n],3*B[n:]);Ka=(6*A[:n],3*A[n:])
    bw=[Kb]+wb;aw=[Ka]+wa
    err=four_error(bw+[0]+invword(bw)+aw+[1]+invword(aw)+[-1,0])
    assert not np.any(err)
    fw=base['fword'](wb);ab=np.array([sum((1 if c==t else -1 if c==-t else 0) for c in fw) for t in (1,2)])
    ab=ab+6*g['abel']@B[:n];gauge=int(ab[1]-ab[0]);cg=e['bpower'](e['x'],gauge)
    # The matrix is written before the cusp gauge.  Restore that gauge
    # only when constructing the final commutator f, as in E.11.
    s0=bw+[0]+invword(bw)
    assert all(not np.any(c) for c in collect(s0*2))
    errors=[kernel((s0+e['t']*(1+144*h))*3) for h in range(2)]
    prepared.append((s0,errors));worddata.append({'beta_base_word_B':wb,'A_base_word_B':wa,
      'beta_central_kernel_vector':B.tolist(),'A_central_kernel_vector':A.tolist(),
      'integral_cusp_gauge':gauge,'s_centralizer_homology_change':vs.tolist()})
matrix=np.zeros((2*m+2,m+48),dtype=np.uint8);matrix[:,:m]=g['original']
for j,(s0,errors) in enumerate(prepared):
    for h in range(2):matrix[m:2*m,m+2*j+h]=errors[h]
piv=np.zeros(min(matrix.shape),dtype=np.int32)
rank=d['gf'](matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,
             piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
pp=piv[:rank].tolist();dom=[i for i in pp if i<m];ra=len(dom);result=[]
for j,(rec,(s0,errors)) in enumerate(zip(records,prepared)):
    choices=[]
    for h in range(2):
        col=m+2*j+h;success=not np.any(matrix[ra:,col]);row={'lambda_mod288':1+144*h,'passes':success}
        if success:
            k=np.zeros(m,dtype=np.int64);k[dom]=matrix[:ra,col];K=(4*k[:n],2*k[n:])
            assert all(not np.any(c) for c in collect((s0+[K])*2))
            assert all(not np.any(c) for c in collect(([K]+s0+e['t']*(1+144*h))*3))
            row['correction_kernel_sparse']={str(i):int(c) for i,c in enumerate(k) if c}
        choices.append(row)
    row={'certificate_index':j,'missing_coset':rec['missing_coset'],'some_eight_lift_exists':any(a['passes'] for a in choices),
         'peripheral_four_witness':worddata[j],'multiplier_choices':choices}
    result.append(row);print(json.dumps({k:row[k] for k in ('certificate_index','missing_coset','some_eight_lift_exists')}),flush=True)
out={'all_24_CM_fibres_have_peripheral_four_witnesses':True,'eight_pass_counts':[
     sum(r['some_eight_lift_exists'] and r['missing_coset']==c for r in result) for c in (False,True)],
     'coefficient_rank':ra,'augmented_rank':rank,'elapsed_seconds':round(time.time()-start,3),'records':result,
     'scope':'Exact complete exponent-eight gentle fibres above these specified peripheral exponent-four witnesses; not an exhaustion of any CM matrix fibre.'}
(here/'de_peripheral_four_eight.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
