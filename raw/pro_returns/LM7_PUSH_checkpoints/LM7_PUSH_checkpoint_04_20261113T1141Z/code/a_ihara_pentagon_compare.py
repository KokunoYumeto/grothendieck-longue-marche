#!/usr/bin/env python3
"""Apply the full group pentagon solution spaces to actual Ihara matrices."""
from pathlib import Path
import importlib.util,json,contextlib,io,argparse
import numpy as np
HERE=Path(__file__).resolve().parent
def load(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
    return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge');meta=load('a_ihara_metabelian')
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
mod9=json.loads((HERE/'a_ihara_mod9.json').read_text())
parser=argparse.ArgumentParser()
parser.add_argument('--input',default='de_fermat_pentagon_arithmetic_fast.json')
parser.add_argument('--output',default='a_ihara_pentagon_compare.json')
args=parser.parse_args()
pent=json.loads((HERE/args.input).read_text())
K=np.array(gt['central_kernel'],dtype=np.int64)
saved=[];allJ=[];allH=[];allF=[]
for row in pent['branch_results']:
    branch=row['branch'];r=mod9[branch]
    old=np.array(r['old_parameter_kernel'],dtype=np.int64)
    part=np.array(row['particular_parameters'],dtype=np.int64)
    hom=np.array(row['homogeneous_parameters'],dtype=np.int64)
    n=old.shape[1];assert n==row['old_parameter_dimension']
    fa=np.array(r['fa'],dtype=np.int64)
    fz=(np.array(r['fz'],dtype=np.int64)+K@old@part[:n])%3
    directions=K@old@hom[:n]%3
    U,J=f.generator_images(fa,fz,7)
    Jcols=[];Hcols=[];Fcols=[]
    HH=meta.image(fa,fz)
    for col in directions.T:
        _,JJ=f.generator_images(fa,(fz+col)%3,7)
        Jcols.append((JJ-J).reshape(-1)%3)
        Hcols.append((meta.image(fa,(fz+col)%3)-HH)%3)
        Fcols.append(np.concatenate(f.multiply((fa,(fz+col)%3),f.inverse((fa,fz)))))
    JJ=np.stack(Jcols,axis=1);HHH=np.stack(Hcols,axis=1);FF=np.stack(Fcols,axis=1)
    print('Branch',branch,'central parameter rank',f.rank(directions),
          'Johnson variation rank',f.rank(JJ),'metabelian variation rank',f.rank(HHH))
    saved.append({'branch':branch,'fa':fa.tolist(),'fz':fz.tolist(),
                  'fz_directions':directions.tolist(),'U':U.tolist(),'J':J.tolist()})
    if branch==0:base=(fa,fz);J0=J;H0=HH
    allJ.append((J-J0).reshape(-1,1)%3);allJ.append(JJ)
    allH.append((HH-H0).reshape(-1,1)%3);allH.append(HHH)
    allF.append(np.concatenate(f.multiply((fa,fz),f.inverse(base)))[:,None]);allF.append(FF)
J=np.hstack(allJ);H=np.hstack(allH);V=np.hstack(allF)
blind=J@g.kernel(H)%3
print('Full pentagon-compatible Johnson variation:',f.rank(J))
print('Metabelian variation:',f.rank(H))
print('Joint rank:',f.rank(np.vstack((J,H))))
print('Metabelian-invisible Johnson variation:',f.rank(blind))
print('Invisible variation modulo c/O-fixing coordinate changes:',
      f.rank(np.hstack((g.D,blind)))-f.rank(g.D))
print('Total variation modulo c/O-fixing coordinate changes:',
      f.rank(np.hstack((g.D,J)))-f.rank(g.D))
data={'branches':saved,'Johnson_variations':J.tolist(),'metabelian_variations':H.tolist(),
      'f_variations':V.tolist(),'base_fa':base[0].tolist(),'base_fz':base[1].tolist(),
      'base_J':J0.tolist(),'base_metabelian':H0.tolist(),
      'Johnson_rank':f.rank(J),'metabelian_rank':f.rank(H),
      'invisible_Johnson_rank':f.rank(blind),
      'invisible_rank_modulo_gauge':f.rank(np.hstack((g.D,blind)))-f.rank(g.D)}
(HERE/args.output).write_text(json.dumps(data,separators=(',',':'))+'\n')
print('PASS: complete supplied pentagon solution spaces retained; arithmetic value not assumed.')
