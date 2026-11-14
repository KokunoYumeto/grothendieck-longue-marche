#!/usr/bin/env python3
"""Actual simultaneous E6 distribution / frozen E62 correction comparison.

All maps start with the identical 97 N_B words. The five distribution
maps retain the exact c_N modulo six, their actual induced source and
the one common correction word. No legacy main program is executed.
"""
from pathlib import Path
from itertools import product
from hashlib import sha256
import json
import time
import subprocess
import numpy as np

from de_ferrari_a6_source_data import load_data
from de_a6_schreier_certificate import read_certificate,verify_words
from a_cm_gl23_pc import ClassTwoCoordinates,Sifter

HERE=Path(__file__).resolve().parent
NS=(2,3,4,6,12)


class Distribution:
    def __init__(self):
        self.unit=(1,0,0,1)
        self.X=(1,2,0,1)
        self.Y=(1,0,10,1)
        def mm(a,b,m=12):
            return tuple(t % m for t in
                         (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                          a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
        self.mm=mm
        vals=[self.unit];at={self.unit:0}
        for a in vals:
            for b in (self.X,self.Y):
                c=mm(a,b)
                if c not in at:
                    at[c]=len(vals);vals.append(c)
        assert len(vals)==96
        self.H=vals;self.at=at;self.hm=[[at[mm(a,b)] for b in vals] for a in vals]
        self.hi=[at[(a[3],-a[1]%12,-a[2]%12,a[0])] for a in vals]
        self.x=(at[self.X],0);self.y=(at[self.Y],1);self.one=(0,0)
        self.V4=[(1,0,0,1),(1,2,0,1),(1,0,2,1),(1,2,2,1)]
        self.vectors=[a for a in product(range(3),repeat=2) if a!=(0,0)]
        self.perms={(h,c):self._aper(h,c) for h in range(96) for c in range(6)}
        assert len({tuple(p) for p in self.perms.values()})==576
        for a in (self.x,self.y,self.ai(self.x),self.ai(self.y)):
            for b in self.perms:
                assert np.array_equal(self.perms[self.am(a,b)],self.perms[b][self.perms[a]])
        self.sources={}
        for n in NS:
            one=(0,(self.one,)*n)
            x=(1,(self.one,)*(n-1)+(self.x,))
            y=(0,(self.y,)+(self.one,)*(n-1))
            self.sources[n]=(one,{1:x,2:y,-1:self.wi(x,n),-2:self.wi(y,n)})
        self.degree=17*sum(NS)
        self.starts=[];offset=0
        for n in NS:
            self.starts.append(offset);offset+=17*n
        self.projected_points=np.array([o+j for o in self.starts for j in range(17)])

    def am(self,a,b):
        return self.hm[a[0]][b[0]],(a[1]+b[1])%6

    def ai(self,a):
        return self.hi[a[0]],-a[1]%6

    def apower(self,a,n):
        v=self.one
        for _ in range(n):v=self.am(v,a)
        return v

    def _aper(self,h,c):
        m=self.H[h]
        four=tuple(a%4 for a in m)
        assert four in self.V4
        p=[self.V4.index(self.mm(a,four,4)) for a in self.V4]
        for u,v in self.vectors:
            p.append(4+self.vectors.index(((u*m[0]+v*m[2])%3,(u*m[1]+v*m[3])%3)))
        p += [12+(i+c)%2 for i in range(2)]
        p += [14+(i+c)%3 for i in range(3)]
        return np.array(p,dtype=np.uint16)

    def wm(self,a,b,n):
        return ((a[0]+b[0])%n,
                tuple(self.am(a[1][j],b[1][(j+a[0])%n]) for j in range(n)))

    def wi(self,a,n):
        return (-a[0]%n,tuple(self.ai(a[1][(j-a[0])%n]) for j in range(n)))

    def word(self,w,n):
        v,letters=self.sources[n]
        for a in w:v=self.wm(v,letters[a],n)
        return v

    def source(self,w):
        out=[];offset=0
        for n in NS:
            k,a=self.word(w,n)
            out.extend(np.r_[tuple(offset+17*((j+k)%n)+self.perms[a[j]] for j in range(n))])
            offset+=17*n
        return np.array(out,dtype=np.uint16)

    def ordinary(self,w):
        a=0
        for c in w:
            z=self.x[0] if abs(c)==1 else self.y[0]
            a=self.hm[a][z if c>0 else self.hi[z]]
        return a

    def projected(self,values):
        return np.concatenate([17*j+self.perms[a] for j,a in enumerate(values)])


def certify(name,gens,greedy=False,derived=False):
    assert not (greedy and derived)
    prefix=HERE/name
    with prefix.with_suffix('.input').open('w') as f:
        f.write(f'{len(gens[0])} {len(gens)}\n')
        for g in gens:f.write(' '.join(map(str,g))+'\n')
    cmd=[str(HERE/'de_a6_schreier_fast')]
    if greedy:cmd.append('--greedy')
    if derived:cmd.append('--derived')
    cmd += [str(prefix.with_suffix('.input')),str(prefix.with_suffix('.bin'))]
    with prefix.with_suffix('.out').open('w') as out,prefix.with_suffix('.err').open('w') as err:
        subprocess.run(cmd,stdout=out,stderr=err,check=True)
    d=read_certificate(prefix.with_suffix('.bin'));verify_words(d)
    assert np.array_equal(d['original'],gens)
    info=json.loads(next(x for x in reversed(prefix.with_suffix('.out').read_text().splitlines()) if x.startswith('{')))
    with Path(str(prefix)+'_replay.out').open('w') as out,Path(str(prefix)+'_replay.err').open('w') as err:
        subprocess.run([str(HERE/'de_a6_schreier_fast'),'--replay',str(prefix.with_suffix('.bin'))],stdout=out,stderr=err,check=True)
    return info,d


def main():
    start=time.monotonic();D=Distribution();data=load_data()
    Nwords=[list(data['fword'](w)) for w in data['Nwords']]
    DN=np.array([D.source(w) for w in Nwords])
    assert DN.shape==(97,459)
    old=np.load(HERE/'a_cm_gl23_joint.npz')['joint_N_generators']
    n0=old.shape[1]
    common=np.array([np.r_[a,n0+b] for a,b in zip(old,DN)])
    info,ncert=certify('a_cm_distribution_e62_N',common,greedy=True)
    print('Common N image',info['order'],'selected',len(info['selected_original_indices']),flush=True)
    indices=info['selected_original_indices']
    cinfo,ccert=certify('a_cm_distribution_e62_N_derived',common[indices],derived=True)
    print('Full common N derived',cinfo['order'],flush=True)
    points=np.r_[np.arange(n0),n0+D.projected_points]
    inverse=np.full(n0+D.degree,-1,dtype=np.int64);inverse[points]=np.arange(len(points))
    projected=inverse[ccert['strong'][:,points]]
    assert np.all(projected>=0)
    jinfo,jcert=certify('a_cm_distribution_e62_projected',projected,greedy=True)
    print('Actual C x five-zero-coordinate image',jinfo['order'],flush=True)
    js=Sifter(jcert)
    dinfo,dcert=certify('a_cm_distribution_e62_distribution',projected[:,n0:]-n0,greedy=True)
    assert int(dinfo['order'])==int(json.loads((HERE/'de_distribution_joint.json').read_text())['joint_correction_group_order'])
    P=ClassTwoCoordinates('joint')
    for g in jcert['strong']:
        assert P.chains[-1].contains(g[:n0])
    assert P.r+P.k==24
    overlap=2**24*int(dinfo['order'])//int(jinfo['order'])
    assert 2**24*int(dinfo['order']) % int(jinfo['order'])==0
    base=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    finals=json.loads((HERE/'a_cm_gl23_joint_pentagon.json').read_text())['records']
    rows=[]
    for rec,fin in zip(base,finals):
        f=rec['actual_commutator_word_f'];qf=D.ordinary(f)
        values=[D.word(f,n) for n in NS]
        assert all(k==0 for k,v in values)
        original=[v[0] for k,v in values]
        candidates=[]
        for a,b in product(range(6),repeat=2):
            coeff=(a,b,2*a%6,(a+b)%6,(2*a+b)%6)
            target=[]
            for oldv,c in zip(original,coeff):
                hc=D.hm[D.apower((D.y[0],0),c)[0]][qf]
                target.append(D.am(D.ai(oldv),(hc,c)))
            candidates.append((coeff,D.projected(target)))
        survives=[]
        for c in fin['all_surviving_correction_coordinates']:
            cp=P.element(c);allowed=[]
            for coeff,target in candidates:
                value=np.r_[cp,n0+target]
                if js.contains(value):allowed.append(coeff)
            survives.append({'E62_actual_PC_coordinate':c,'admissible_distribution_coefficient_tuples':allowed,
                             'count':len(allowed),'passes':bool(allowed)})
        row={'index':fin['index'],'missing_coset':rec['missing_coset'],
             'E62_final_count':len(survives),'simultaneously_passing_E62_final_count':sum(r['passes'] for r in survives),
             'actual_single_source_correction_fibres':survives}
        rows.append(row)
        print('Point',fin['index'],'E62 finals',len(survives),'simultaneous',row['simultaneously_passing_E62_final_count'],flush=True)
    out={'status':'PASS_ACTUAL_SIMULTANEOUS_E6_E62_SOURCE_COMPARISON',
         'N_values':NS,'distribution_source_degree':459,'E62_source_degree':n0,
         'common_N_source':info,'common_N_derived_source':cinfo,
         'common_projected_correction_image':jinfo,'five_distribution_correction_image':dinfo,
         'E62_correction_order':2**24,'exact_common_quotient_order':overlap,
         'same_97_original_N_words_and_same_actual_derived_DAG':True,
         'all_correction_memberships_are_in_one_actual_common_image':True,
         'records':rows,
         'scope':'The complete four E62 finite final values joined to all five E6 distribution equations and coefficient multiplicativity; generation in the added distribution refinement is not asserted.',
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in (
             'de_ferrari_a6_source_data.py','de_ferrari_sl2_5_N.json','de_ferrari_fibres.json',
             'a_cm_gl23_joint.npz','a_cm_gl23_joint_pentagon.json','de_distribution_joint.json',
             'a_cm_gl23_joint_pc.npz','a_cm_gl23_pc.py','de_a6_schreier.cpp')},
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_distribution_e62.npz',distribution_N=DN,
                        common_N=common,projected_derived_generators=projected,
                        retained_projection_points=points)
    (HERE/'a_cm_distribution_e62.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)


if __name__=='__main__':
    main()
