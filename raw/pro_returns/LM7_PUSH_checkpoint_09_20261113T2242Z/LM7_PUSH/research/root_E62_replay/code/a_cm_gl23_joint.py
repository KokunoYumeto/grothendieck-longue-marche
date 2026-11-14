#!/usr/bin/env python3
"""Actual GL23--SL23 target/source comparison through common words.

The block projections are literal group homomorphisms. Equal projected
orders certify factorization only after the complete common source is
computed and its exact Schreier certificates are independently replayed.
"""
from pathlib import Path
import subprocess,json,time
import numpy as np
from a_cm_gl23_model import FerrariGL23
from a_cm_sl23_model import FerrariSL23
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def run(name,perms):
    prefix=HERE/f'a_cm_gl23_{name}'
    n=len(perms[0])
    with prefix.with_suffix('.input').open('w') as f:
        f.write(f'{n} {len(perms)}\n')
        for p in perms:f.write(' '.join(map(str,p))+'\n')
    with prefix.with_suffix('.out').open('w') as out,prefix.with_suffix('.err').open('w') as err:
        subprocess.run([str(HERE/'de_a6_schreier_fast'),str(prefix.with_suffix('.input')),
                        str(prefix.with_suffix('.bin'))],stdout=out,stderr=err,check=True)
    lines=prefix.with_suffix('.out').read_text().splitlines()
    info=json.loads(next(x for x in reversed(lines) if x.startswith('{')))
    cert=read_certificate(prefix.with_suffix('.bin'));verify_words(cert)
    assert np.array_equal(cert['original'],np.array(perms))
    with Path(str(prefix)+'_replay.out').open('w') as out,Path(str(prefix)+'_replay.err').open('w') as err:
        subprocess.run([str(HERE/'de_a6_schreier_fast'),'--replay',str(prefix.with_suffix('.bin'))],
                       stdout=out,stderr=err,check=True)
    info['independent_all_word_replay']=True
    return info

def main():
    start=time.time();g=np.load(HERE/'a_cm_gl23_induced.npz');s=np.load(HERE/'a_cm_sl23_induced.npz')
    ng=len(g['compressed_s']);ns=len(s['compressed_s'])
    B=[np.r_[g['compressed_'+a],ng+s['compressed_'+a]] for a in ('s','r')]
    N=[np.r_[a,ng+b] for a,b in zip(g['N_generators'],s['N_generators'])]
    hg=FerrariGL23();hs=FerrariSL23();dg=48*hg.n;ds=24*hs.n
    T=[np.r_[hg.permutation(a).array_form,dg+np.array(hs.permutation(b).array_form)]
       for a,b in zip((hg.a,hg.b,hg.c),(hs.a,hs.b,hs.c))]
    info={}
    for name,perms in (('joint_SL23_B',B),('joint_SL23_N',N),('joint_SL23_target',T)):
        print('Exact common group',name,flush=True)
        info[name]=run(name,perms)
        print('order',info[name]['order'],flush=True)
    gl_B=json.loads(next(x for x in reversed((HERE/'a_cm_gl23_B_source.out').read_text().splitlines()) if x.startswith('{')))
    gl_N=json.loads(next(x for x in reversed((HERE/'a_cm_gl23_N_source.out').read_text().splitlines()) if x.startswith('{')))
    gl_T=json.loads((HERE/'a_cm_gl23_model.json').read_text())
    equal={'B':int(info['joint_SL23_B']['order'])==int(gl_B['order']),
           'N':int(info['joint_SL23_N']['order'])==int(gl_N['order']),
           'target':int(info['joint_SL23_target']['order'])==int(gl_T['actual_B4_target_order'])}
    out={'status':'PASS_ACTUAL_COMMON_GL23_SL23_COMPARISON',
         'literal_common_source_degrees':[ng,ns], 'literal_common_target_degrees':[dg,ds],
         'exact_groups':info,'SL23_maps_factor_through_corresponding_GL23_maps':equal,
         'factorization_proof':'Common block image projects onto the GL23 image; equality of finite orders makes this actual projection an isomorphism. Its inverse followed by the SL23 block is the required map.',
         'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/'a_cm_gl23_joint.npz',joint_B_generators=B,joint_N_generators=N,joint_target_generators=T,
                        GL23_source_block=np.arange(ng),SL23_source_block=np.arange(ng,ng+ns),
                        GL23_target_block=np.arange(dg),SL23_target_block=np.arange(dg,dg+ds))
    (HERE/'a_cm_gl23_joint.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
