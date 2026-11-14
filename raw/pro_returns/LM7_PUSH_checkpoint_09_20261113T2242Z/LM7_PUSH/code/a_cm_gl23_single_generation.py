#!/usr/bin/env python3
"""Exact target generation at every GL23-only pentagon point."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,subprocess,time
import numpy as np
from a_cm_gl23_model import FerrariGL23
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();H=FerrariGL23()
    folder=HERE/'a_cm_gl23_single_generation_certificates';folder.mkdir(exist_ok=False)
    gentle=json.loads((HERE/'a_cm_gl23_single_gentle.json').read_text())['records']
    final=json.loads((HERE/'a_cm_gl23_single_pentagon.json').read_text())['records']
    values=np.load(HERE/'a_cm_gl23_single_pentagon.npz')
    expected=json.loads((HERE/'a_cm_gl23_model.json').read_text())['actual_B4_target_order']
    jobs=[]
    for row,fr in zip(gentle,final):
        good=set(fr['all_surviving_correction_coordinates']);i=row['index']
        for j,c in enumerate(row['all_gentle_coordinates']):
            if c not in good:continue
            v=values[f'point_{i:02d}_gl23_all_gentle_values'][j]
            images=H.braid_images(v);H.check_braids(images)
            jobs.append((i,j,c,[np.array(H.permutation(g).array_form,dtype=np.uint16) for g in images]))
    def run(job):
        i,j,c,gs=job;prefix=folder/f'target_{i:02d}_{j:02d}';n=len(gs[0])
        with prefix.with_suffix('.input').open('w') as f:
            f.write(f'{n} 3\n')
            for g in gs:f.write(' '.join(map(str,g))+'\n')
        with prefix.with_suffix('.out').open('w') as out,prefix.with_suffix('.err').open('w') as err:
            subprocess.run([str(HERE/'de_a6_schreier_fast'),str(prefix.with_suffix('.input')),
                            str(prefix.with_suffix('.bin'))],stdout=out,stderr=err,check=True)
        info=json.loads(next(s for s in reversed(prefix.with_suffix('.out').read_text().splitlines()) if s.startswith('{')))
        d=read_certificate(prefix.with_suffix('.bin'));verify_words(d)
        assert np.array_equal(d['original'],np.array(gs))
        return {'G6_index':i,'actual_correction_coordinate':c,'actual_order':int(info['order']),
                'generates_whole_target':int(info['order'])==expected,
                'complete_final_Schreier_relations':info['complete_final_Schreier_relations'],
                'all_strong_words_independently_replayed':True}
    with ThreadPoolExecutor(max_workers=2) as pool:answers=list(pool.map(run,jobs))
    out={'status':'PASS_COMPLETE_GL23_ONLY_TARGET_GENERATION','complete_target_order':expected,
         'all_96_target_points_generate':all(r['generates_whole_target'] for r in answers),
         'complete_point_count':len(answers),'points':answers,'seconds':round(time.time()-start,3)}
    (HERE/'a_cm_gl23_single_generation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='points'},indent=2),flush=True)

if __name__=='__main__':main()
