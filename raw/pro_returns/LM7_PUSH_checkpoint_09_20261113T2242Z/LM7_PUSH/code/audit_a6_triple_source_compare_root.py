#!/usr/bin/env python3
"""Finish comparison after the completed isolated mathematical replay.

The original wrapper and its final-comparison failure are preserved.
Its eleven JSON, seven NPZ and six binary comparisons had passed.  This
program repeats every comparison without rerunning the mathematical batch.
The only additional comparison map concerns two explicit discovery-history
fields in the base stdout.  The unchanged saved certificates retain both
original generators, all strong words, and the entire final chain.
"""
import json
import time
import numpy as np
from audit_a6_triple_source_root import (ROOT, MANIFEST, DEST, JSON_OUTPUTS,
    NPZ_OUTPUTS, BYTE_OUTPUTS, sha, stable, final_report)
from de_a6_schreier_certificate import read_certificate, verify_words


def main():
    started = time.monotonic()
    manifest_hash = sha(MANIFEST)
    manifest = json.loads(MANIFEST.read_text())
    protected = {**manifest['records'], **manifest['documents']}
    for name, record in protected.items():
        assert sha(ROOT / name) == record['sha256'], name
    code = DEST / 'code'
    commands = json.loads((DEST / 'commands.json').read_text())
    expected = ['compile_de_a6_schreier', 'compile_de_a6_triple_affine',
        'compile_de_a6_triple_kernel', 'compile_de_a6_triple_central',
        'de_a6_triple_affine_prepare', 'de_a6_triple_affine_factor',
        'de_a6_triple_base_prepare', 'de_a6_triple_base',
        'de_a6_triple_modular_prepare', 'de_a6_triple_modular',
        'de_a6_triple_kernel_prepare', 'de_a6_triple_kernel',
        'de_a6_triple_kernel_replay', 'de_a6_triple_central_prepare',
        'de_a6_triple_central', 'de_a6_triple_central_replay',
        'de_a6_triple_source_certificate']
    assert [r['name'] for r in commands] == expected
    assert all(r['exit_code'] == 0 for r in commands)
    compared, changed_hashes = [], []
    dynamic = set(JSON_OUTPUTS+NPZ_OUTPUTS+BYTE_OUTPUTS+
                  ['de_a6_triple_base.out', 'de_a6_triple_modular.out'])
    for name in JSON_OUTPUTS:
        old = json.loads((ROOT / 'code' / name).read_text())
        new = json.loads((code / name).read_text())
        assert set(old) == set(new), name
        if 'input_sha256' in old:
            assert set(old['input_sha256']) == set(new['input_sha256']), name
            for dependency, old_hash in old['input_sha256'].items():
                new_hash = new['input_sha256'][dependency]
                assert sha(ROOT / 'code' / dependency) == old_hash, (name, dependency)
                assert sha(code / dependency) == new_hash, (name, dependency)
                if old_hash != new_hash:
                    assert dependency in dynamic, (name, dependency)
                    changed_hashes.append({'output': name, 'verified_dependency': dependency,
                        'original_sha256': old_hash, 'replay_sha256': new_hash})
            # The actual maps from both hash lists to verified files are checked above.
            old['input_sha256'] = new['input_sha256'] = sorted(old['input_sha256'])
        assert stable(old) == stable(new), ('mathematical JSON', name)
        compared.append(name)
    for name in NPZ_OUTPUTS:
        with np.load(ROOT / 'code' / name) as old, np.load(code / name) as new:
            assert set(old.files) == set(new.files), name
            for key in old.files:
                assert old[key].dtype == new[key].dtype, (name, key, 'dtype')
                assert old[key].shape == new[key].shape, (name, key, 'shape')
                assert np.array_equal(old[key], new[key]), (name, key, 'value')
        compared.append(name)
    for name in BYTE_OUTPUTS:
        assert (ROOT / 'code' / name).read_bytes() == (code / name).read_bytes(), name
        compared.append(name)
    provenance = []
    for stem, original_scans in [('de_a6_triple_base', 1995837),
                                  ('de_a6_triple_modular', 1746926)]:
        name = stem+'.out'
        old, new = final_report(ROOT / 'code' / name), final_report(code / name)
        # These exact two differences arise from initialize/discover versus
        # Engine::replay: replay calls pass(false) once and never initialize.
        assert old['selected_original_indices'] == [0, 1]
        assert new['selected_original_indices'] == []
        assert old['total_discovery_relation_scans'] == original_scans
        assert new['total_discovery_relation_scans'] == new['complete_final_Schreier_relations'] == 873463
        cert_name = stem+'.bin'
        assert (ROOT / 'code' / cert_name).read_bytes() == (code / cert_name).read_bytes()
        certificate = read_certificate(code / cert_name)
        assert len(certificate['original']) == 2
        verify_words(certificate)
        original_indices = sorted(set(int(a) for op, a, b in certificate['nodes'] if op == 1))
        assert original_indices == [0, 1]
        for j in range(2):
            assert any(int(w) == j+1 and np.array_equal(g, certificate['original'][j])
                       for w, g in zip(certificate['words'], certificate['strong']))
        fields = ('selected_original_indices', 'total_discovery_relation_scans')
        provenance.append({'report': name, 'old_values': {k: old[k] for k in fields},
                           'replay_values': {k: new[k] for k in fields},
                           'saved_original_generator_indices': original_indices,
                           'certificate_sha256': sha(code / cert_name),
                           'both_original_generators_present_in_strong_chain': True})
        for k in fields:
            del old[k], new[k]
        assert stable(old) == stable(new), ('complete final mathematical chain', name)
        compared.append(name)
    for name, record in protected.items():
        assert sha(ROOT / name) == record['sha256'], name
    assert sha(MANIFEST) == manifest_hash
    result = {'status': 'PASS_ISOLATED_COMPLETE_TRIPLE_SOURCE_ROOT_REPLAY',
        'manifest_sha256': manifest_hash, 'all_mathematical_outputs_identical': True,
        'all_mathematical_batch_exit_codes_zero': True,
        'complete_lifted_base_relations': 873463, 'complete_lifted_C_relations': 720615,
        'original_C_to_normal_form_links': 10, 'kernel_dimension': 79,
        'C_preimage_abelianization_dimension': 3, 'perfect_residual_kernel_dimension': 76,
        'protected_original_files_unchanged': len(protected), 'compared_outputs': compared,
        'verified_dynamic_dependency_hashes': changed_hashes,
        'explicit_discovery_to_replay_provenance_comparison': provenance,
        'preserved_initial_wrapper_failure': 'code/audit_a6_triple_source_root.err',
        'batch_command_seconds': round(sum(r['seconds'] for r in commands), 3),
        'comparison_seconds': round(time.monotonic()-started, 3)}
    assert not (DEST / 'result.json').exists()
    (DEST / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in
                     ('compared_outputs', 'verified_dynamic_dependency_hashes',
                      'explicit_discovery_to_replay_provenance_comparison')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
