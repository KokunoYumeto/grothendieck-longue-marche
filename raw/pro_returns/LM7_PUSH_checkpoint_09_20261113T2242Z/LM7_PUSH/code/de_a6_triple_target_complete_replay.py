#!/usr/bin/env python3
"""Freshly compile and completely replay every retained target chain.

This run does no subgroup search and changes no original certificate.
It checks every final Schreier relation, derived-generator membership,
the full normality gate for derived runs, and the orbit product. Runtime
and discovery scan totals are compared separately; the exact replay
normality count is required to equal the full rectangular gate size.
"""
from pathlib import Path
from hashlib import sha256
import json,subprocess,time
from de_a6_triple_source_certificate import report
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent


def main():
    started=time.time()
    stems=['de_a6_triple_target']+[
        f'de_a6_triple_target_derived{i}' for i in range(1,6)]
    names=['de_a6_schreier.cpp','de_a6_triple_target_replay.out']
    for stem in stems:names.extend([stem+'.bin',stem+'.out'])
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    engine=HERE/'de_a6_triple_target_independent_engine'
    subprocess.run(['g++','-std=c++17','-O3','de_a6_schreier.cpp','-o',str(engine)],
                   cwd=HERE,check=True)
    exempt={'seconds','total_discovery_relation_scans','selected_original_indices',
            'normal_conjugation_checks'}
    rows=[]
    for stem in stems:
        out=stem+'_independent.out';err=stem+'_independent.err';begin=time.time()
        with (HERE/out).open('w') as stdout,(HERE/err).open('w') as stderr:
            subprocess.run([str(engine),'--replay',stem+'.bin'],cwd=HERE,
                           stdout=stdout,stderr=stderr,check=True)
        baseline=stem+'.out' if stem!='de_a6_triple_target' else stem+'_replay.out'
        original=report(baseline);replayed=report(out)
        if stem=='de_a6_triple_target':
            legacy=report(stem+'.out')
            assert all(original[k]==v for k,v in legacy.items() if k not in exempt)
            assert original['derived_mode'] is False and original['normal_conjugation_checks']==0
        cert=read_certificate(HERE/(stem+'.bin'))
        expected_normal=len(cert['original'])*len(cert['strong']) if cert['derived'] else 0
        assert replayed['normal_conjugation_checks']==expected_normal
        assert original['normal_conjugation_checks']>=expected_normal
        assert {k:v for k,v in original.items() if k not in exempt}==\
               {k:v for k,v in replayed.items() if k not in exempt}
        row={'certificate':stem+'.bin','mathematical_report_baseline':baseline,'status':'PASS',
             'all_mathematical_report_fields_identical':True,
             'complete_final_Schreier_relations':replayed['complete_final_Schreier_relations'],
             'normal_conjugation_checks':replayed['normal_conjugation_checks'],
             'exact_complete_normality_gate_size':expected_normal,
             'discovery_provenance_fields':{k:original.get(k) for k in sorted(exempt)},
             'replay_provenance_fields':{k:replayed.get(k) for k in sorted(exempt)},
             'wall_seconds':round(time.time()-begin,3)}
        rows.append(row);print(json.dumps(row),flush=True)
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==v for n,v in hashes.items())
    result={'status':'PASS_ALL_SIX_COMPLETE_TARGET_CHAIN_REPLAYS',
            'all_original_certificates_and_discovery_logs_unchanged':True,
            'report_fields_with_typed_provenance_comparison':sorted(exempt),
            'normality_counts_checked_as_exact_original_times_strong_gate':True,
            'rows':rows,'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_target_complete_replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
