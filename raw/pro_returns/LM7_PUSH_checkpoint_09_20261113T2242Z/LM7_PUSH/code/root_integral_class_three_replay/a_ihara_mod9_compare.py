#!/usr/bin/env python3
"""Exact metabelian/gauge comparison after all mod9 lifting constraints."""
from pathlib import Path
import importlib.util,json,contextlib,io
import numpy as np
HERE=Path(__file__).resolve().parent

def load(name):
 spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
 m=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
 return m
f=load('de_fermat_schreier');meta=load('a_ihara_metabelian');gauge=load('a_ihara_gauge')
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
rows=json.loads((HERE/'a_ihara_mod9.json').read_text())
K=np.array(gt['central_kernel'],dtype=np.int64)
base=rows[0];ba=np.array(base['fa'],dtype=np.int64);bz=np.array(base['fz'],dtype=np.int64)
_,J0=f.generator_images(ba,bz,7);H0=meta.image(ba,bz)
jcols=[];hcols=[];vcols=[]
for r in rows:
 fa=np.array(r['fa'],dtype=np.int64);fz=np.array(r['fz'],dtype=np.int64)
 old=np.array(r['old_parameter_kernel'],dtype=np.int64)
 candidates=[fz]+[(fz+K@col)%3 for col in old.T]
 for zz in candidates:
  _,J=f.generator_images(fa,zz,7);H=meta.image(fa,zz)
  jcols.append((J-J0).reshape(-1)%3);hcols.append((H-H0)%3)
  vcols.append(np.concatenate(f.multiply((fa,zz),f.inverse((ba,bz)))))
J=np.stack(jcols,axis=1);H=np.stack(hcols,axis=1);V=np.stack(vcols,axis=1)
blind=J@gauge.kernel(H)%3
print('Mod9-liftable Johnson uncertainty:',f.rank(J))
print('Its metabelian coefficient variation:',f.rank(H))
print('Joint rank:',f.rank(np.vstack((J,H))))
print('Invisible Johnson uncertainty:',f.rank(blind))
D=gauge.D
print('Total Johnson uncertainty modulo c/O-fixing gauge:',f.rank(np.hstack((D,J)))-f.rank(D))
print('Invisible uncertainty modulo c/O-fixing gauge:',f.rank(np.hstack((D,blind)))-f.rank(D))
fil=json.loads((HERE/'a_ihara_filtration.json').read_text())
for degree in (5,6,7,8,9):
 DD=np.array(fil['D_bases'][str(degree)],dtype=np.int64)
 top=np.vstack((np.hstack((V,DD)),np.hstack((H,np.zeros((25,DD.shape[1]),dtype=np.int64)))))
 kk=gauge.kernel(top);bs=J@kk[:J.shape[1],:]%3
 print('Invisible D',degree,'rank',f.rank(bs),'modulo gauge',f.rank(np.hstack((D,bs)))-f.rank(D))
(HERE/'a_ihara_mod9_compare.json').write_text(json.dumps({'f_variations':V.tolist(),
 'Johnson_variations':J.tolist(),'metabelian_variations':H.tolist()},indent=2)+'\n')
print('PASS')
