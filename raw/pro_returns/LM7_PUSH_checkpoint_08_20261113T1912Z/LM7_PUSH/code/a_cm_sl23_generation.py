#!/usr/bin/env python3
"""Literal three/four-strand generation in every complete SL2(F3) fibre.

All gentle corrections and every pentagon correction are tested.  Each exact
Schreier certificate retains its original generators and word DAG, and those
words are independently replayed by the Python array reader.  This program
does not write any prior Ferrari or CM artifact.
"""
from pathlib import Path
import hashlib,json,subprocess,time
import numpy as np
from a_cm_sl23_model import FerrariSL23
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent
OUT=HERE/'a_cm_sl23_generation_certificates'

def main():
    started=time.time();OUT.mkdir(exist_ok=True)
    H=FerrariSL23();d=load_data();W=InducedCombined(H,d)
    old=np.load(HERE/'a_cm_sl23_induced.npz')
    orig_s,orig_r=old['original_s'],old['original_r']
    points=old['retained_original_points'];inverse=np.full(len(orig_s),-1,dtype=np.int64)
    inverse[points]=np.arange(len(points));source_order=48922361856;target_order=43486543872
    raw=np.load(HERE/'a_cm_sl23_corrections.npz');C=raw['corrections']
    pairs=raw['selected_N_commutators'];parents=raw['word_parents']
    selected_words=[]
    for i,j in pairs:
        a,b=d['Nwords'][int(i)],d['Nwords'][int(j)]
        selected_words.append(a+b+d['binv'](a)+d['binv'](b))
    cwords=[[]]
    for parent,letter in parents[1:]:cwords.append(cwords[int(parent)]+selected_words[int(letter)])
    assert len(cwords)==512
    corrected=json.loads((HERE/'a_cm_sl23_corrections.json').read_text())['records']
    records=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    hd=24*H.n
    def permutation(e):
        return np.concatenate([hd*(6*int(e[0][q])+i)+
            np.asarray(H.permutation(e[1][q,i]).array_form,dtype=np.int64)
            for q in range(6) for i in range(6)])
    def certify(name,perms):
        path=OUT/(name+'.input');cert=OUT/(name+'.bin')
        with path.open('w') as f:
            f.write(f'{len(perms[0])} {len(perms)}\n')
            for p in perms:f.write(' '.join(map(str,p))+'\n')
        proc=subprocess.run([str(HERE/'de_a6_schreier_fast'),str(path),str(cert)],
                            check=True,text=True,capture_output=True)
        (OUT/(name+'.out')).write_text(proc.stdout)
        (OUT/(name+'.err')).write_text(proc.stderr)
        result=json.loads(next(line for line in reversed(proc.stdout.splitlines()) if line.startswith('{')))
        assert result['status']=='PASS'
        certificate=read_certificate(cert);verify_words(certificate)
        assert np.array_equal(certificate['original'],np.array(perms))
        return result
    # An actual product decomposition of the correction group is recorded
    # through three of the retained evaluation-coordinate homomorphisms.
    chosen=[];partitions=[];current=[() for _ in C]
    projection_data=[]
    for q in range(6):
        for i in range(6):
            keys=[a[q,i].astype(np.uint8).tobytes() for a in C]
            distinct=list(dict.fromkeys(keys))
            if len(distinct)!=8:continue
            ids={k:j for j,k in enumerate(distinct)}
            labels=[ids[k] for k in keys]
            joined=[a+(b,) for a,b in zip(current,labels)]
            if len(set(joined))==len(set(current)):continue
            values=np.array([C[keys.index(k),q,i] for k in distinct])
            table=np.array([[ids[H.mul(a,b).astype(np.uint8).tobytes()] for b in values] for a in values])
            one=ids[H.one.astype(np.uint8).tobytes()]
            square=table[np.arange(8),np.arange(8)]
            involutions=[j for j in range(8) if j!=one and square[j]==one]
            assert len(involutions)==1
            neg=involutions[0]
            ij=next((a,b) for a in range(8) for b in range(8)
                    if square[a]==square[b]==neg and table[a,b]!=table[b,a])
            a,b=ij
            assert table[a,b]==table[neg,table[b,a]]
            generated={one};todo=[one]
            for g in todo:
                for h in ij:
                    v=int(table[g,h])
                    if v not in generated:generated.add(v);todo.append(v)
            assert len(generated)==8
            projection_data.append({'coset':q,'evaluation':i,'multiplication_table':table.tolist(),
                                    'identity':one,'minus_identity':neg,'quaternion_generators':[a,b]})
            chosen.append((q,i));partitions.append(labels);current=joined
            if len(set(current))==512:break
        if len(set(current))==512:break
    assert len(chosen)==3 and len(set(current))==512
    all_rows=[]
    for record,corr in zip(records,corrected):
        ix=corr['index'];base=W.word(d['to_B'](record['actual_commutator_word_f']))
        row={'index':ix,'missing_coset':record['missing_coset'],'gentle_points':[]}
        for ci in corr['all_gentle_indices']:
            corrected_f=H.mul(base[1],C[ci])
            wordf=record['actual_commutator_word_f']+list(d['fword'](cwords[ci]))
            assert sum((a==1)-(a==-1) for a in wordf)==0
            assert sum((a==2)-(a==-2) for a in wordf)==0
            assert np.array_equal(W.word(d['to_B'](wordf))[1],corrected_f)
            assert np.array_equal(H.word(wordf),corrected_f[W.root])
            pf=permutation((W.id,corrected_f));cf=inverse[pf[points]]
            assert np.all(cf>=0)
            S=cf[old['compressed_s']]
            R=old['compressed_r'][np.argsort(cf)]
            assert np.array_equal(S[S],np.arange(len(S)))
            assert np.array_equal(R[R[R]],np.arange(len(R)))
            source=certify(f'p{ix:02d}_c{ci:03d}_source',(S,R))
            source_full=int(source['order'])==source_order
            pentagon=ci in corr['all_gentle_pentagon_braid_indices']
            point={'correction_index':ci,'source_order':int(source['order']),
                   'onto_complete_source':source_full,'pentagon':pentagon,
                   'literal_commutator_word_f':wordf}
            if pentagon:
                a,b,c=H.braid_images(corrected_f[W.root]);H.check_braids((a,b,c))
                target=certify(f'p{ix:02d}_c{ci:03d}_target',
                    [np.array(H.permutation(g).array_form) for g in (a,b,c)])
                point['four_strand_target_order']=int(target['order'])
                point['onto_complete_four_strand_target']=int(target['order'])==target_order
            row['gentle_points'].append(point)
        print('Point',ix,'source orders',[p['source_order'] for p in row['gentle_points']],
              'pentagon target orders',[p['four_strand_target_order'] for p in row['gentle_points'] if p['pentagon']],flush=True)
        all_rows.append(row)
    out={'status':'PASS_COMPLETE_SL23_GENERATION',
         'actual_three_strand_source_order':source_order,'actual_four_strand_target_order':target_order,
         'complete_correction_group':'Q8^3 through the three displayed actual evaluation maps',
         'quaternion_projections':projection_data,
         'combined_projection_is_bijective':True,
         'all_gentle_points_generate_source':all(p['onto_complete_source'] for row in all_rows for p in row['gentle_points']),
         'all_pentagon_points_generate_target':all(p['onto_complete_four_strand_target'] for row in all_rows for p in row['gentle_points'] if p['pentagon']),
         'all_literal_words_have_zero_integral_F_abelianization':True,
         'all_strong_words_independently_replayed':True,
         'Schreier_program_sha256':hashlib.sha256((HERE/'de_a6_schreier.cpp').read_bytes()).hexdigest(),
         'Schreier_executable_sha256':hashlib.sha256((HERE/'de_a6_schreier_fast').read_bytes()).hexdigest(),
         'records':all_rows,'seconds':round(time.time()-started,3)}
    (HERE/'a_cm_sl23_generation.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'a_cm_sl23_quaternion_projections.npz',
                       selected_coordinates=np.array(chosen),all_correction_projection_coordinates=np.array(partitions).T)
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','quaternion_projections')},indent=2),flush=True)

if __name__=='__main__':main()
