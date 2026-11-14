#!/usr/bin/env python3
"""Freshly compile and replay all five complete binary target chains."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import time
from de_a6_triple_source_certificate import report
from de_a6_schreier_certificate import read_certificate

HERE = Path(__file__).resolve().parent


def main():
    started = time.monotonic()
    stems = ['e_a6_double_target_root'] + [f'e_a6_double_target_derived{i}_root' for i in range(1, 5)]
    names = ['de_a6_schreier.cpp']
    for stem in stems:
        names += [stem+'.bin', stem+'.out']
    hashes = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    engine = HERE/'e_a6_double_target_independent_engine_root'
    with (HERE/'e_a6_double_target_independent_compile_root.out').open('w') as out, (HERE/'e_a6_double_target_independent_compile_root.err').open('w') as err:
        subprocess.run(['g++', '-std=c++17', '-O3', 'de_a6_schreier.cpp', '-o', str(engine)],
                       cwd=HERE, stdout=out, stderr=err, check=True)
    provenance = {'seconds', 'total_discovery_relation_scans',
                  'selected_original_indices', 'normal_conjugation_checks'}
    rows = []
    for stem in stems:
        begin = time.monotonic()
        out_name, err_name = stem+'_independent.out', stem+'_independent.err'
        with (HERE/out_name).open('w') as out, (HERE/err_name).open('w') as err:
            subprocess.run([str(engine), '--replay', stem+'.bin'], cwd=HERE,
                           stdout=out, stderr=err, check=True)
        original, actual = report(stem+'.out'), report(out_name)
        cert = read_certificate(HERE/(stem+'.bin'))
        normal = len(cert['original'])*len(cert['strong']) if cert['derived'] else 0
        assert actual['normal_conjugation_checks'] == normal
        assert original['normal_conjugation_checks'] >= normal
        assert {k:v for k,v in original.items() if k not in provenance} == \
               {k:v for k,v in actual.items() if k not in provenance}
        row = {
            'certificate':stem+'.bin', 'status':'PASS',
            'all_mathematical_report_fields_identical':True,
            'complete_final_Schreier_relations':actual['complete_final_Schreier_relations'],
            'exact_complete_normality_gate_size':normal,
            'discovery_provenance_fields':{k:original[k] for k in sorted(provenance)},
            'replay_provenance_fields':{k:actual[k] for k in sorted(provenance)},
            'seconds':round(time.monotonic()-begin, 3),
        }
        rows.append(row)
        print(json.dumps(row), flush=True)
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n,h in hashes.items())
    result = {
        'status':'PASS_ALL_FIVE_COMPLETE_DOUBLE_A6_TARGET_CHAIN_REPLAYS',
        'all_original_certificates_and_discovery_logs_unchanged':True,
        'report_fields_with_typed_provenance_comparison':sorted(provenance),
        'normality_counts_checked_as_exact_original_times_strong_gate':True,
        'total_complete_final_Schreier_relations':sum(r['complete_final_Schreier_relations'] for r in rows),
        'rows':rows, 'input_sha256':hashes,
        'seconds':round(time.monotonic()-started, 3),
    }
    (HERE/'e_a6_double_target_complete_replay_root.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
