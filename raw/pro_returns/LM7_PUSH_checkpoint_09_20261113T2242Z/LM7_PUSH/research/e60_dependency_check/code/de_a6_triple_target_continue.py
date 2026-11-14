#!/usr/bin/env python3
"""Complete the remaining literal target derived-word chain.

Every stage runs its full Schreier certificate. Equal consecutive orders
are meaningful only with the retained word inclusion; the separate final
certificate verifies the actual small-quotient kernel and normality.
"""
from pathlib import Path
import json,subprocess,time
from de_a6_triple_source_certificate import report

HERE=Path(__file__).resolve().parent

def run(command,stem):
    with (HERE/(stem+'.out')).open('w') as out,(HERE/(stem+'.err')).open('w') as err:
        subprocess.run(command,cwd=HERE,stdout=out,stderr=err,check=True)

def main():
    started=time.time();full=int(report('de_a6_triple_target_replay.out')['order'])
    stages=[]
    for stage in range(3,9):
        parent=f'de_a6_triple_target_derived{stage-1}';stem=f'de_a6_triple_target_derived{stage}'
        assert not (HERE/(stem+'.bin')).exists()
        run(['python','de_a6_triple_target_mix.py',parent+'.bin',stem,
             '--quotient-input',parent+'_input.npz'],stem+'_prepare')
        run([str(HERE/'de_a6_triple_target_engine'),'--derived',stem+'.input',stem+'.bin'],stem)
        result=report(stem+'.out');order=int(result['order']);previous=int(report(parent+'.out')['order'])
        row={'stage':stage,'order':str(order),'index':full//order,
             'equal_to_containing_parent_order':order==previous,
             'complete_final_Schreier_relations':result['complete_final_Schreier_relations']}
        stages.append(row);print(json.dumps(row),flush=True)
        if order==previous:break
    else:raise AssertionError('No stable derived-word subgroup within eight stages')
    out={'status':'PASS_COMPLETE_RETAINED_TARGET_DERIVED_WORD_CHAIN',
         'new_stages':stages,'final_stage':stages[-1]['stage'],
         'final_index':stages[-1]['index'],
         'small_quotient_comparison_and_normality_are_separate_certificate':True,
         'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_target_continue.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
