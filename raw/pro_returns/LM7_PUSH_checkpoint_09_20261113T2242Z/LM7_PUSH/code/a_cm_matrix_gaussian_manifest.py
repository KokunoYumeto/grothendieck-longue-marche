#!/usr/bin/env python3
"""Freeze the exact E74 source, dependency and replay manifest."""
from pathlib import Path
import argparse
import hashlib
import json


ROOT=Path(__file__).resolve().parent.parent
STAGES=['a_cm_matrix_gaussian_join','a_cm_matrix_gaussian_witnesses']
PYTHON_INPUTS=[
    'a_cm_distribution_e62.py','a_cm_distribution_orbifold.py',
    'a_cm_gl23_pc.py','a_cm_kn23_fibres.py','a_cm_kn23_model.py',
    'a_cm_kn23_witnesses.py','a_cm_matrix_gaussian_join.py',
    'a_cm_matrix_gaussian_witnesses.py','bc_gaussian_heisenberg_model.py',
    'bc_gaussian_heisenberg_source.py','bc_gaussian_heisenberg_structure.py',
    'bc_hyperelliptic_sewing.py','bc_orbifold_CM_characters.py',
    'bc_orbifold_CM_six.py','de_a6_schreier_certificate.py',
    'de_ferrari_a6_source_data.py']
DATA_INPUTS=[
    'a_cm_kn23_model.json','a_cm_kn23_model.npz','a_cm_kn23_source.npz',
    'a_cm_kn23_witnesses.npz','a_cm_kn23_fibres.npz',
    'bc_gaussian_heisenberg_joint.json','bc_gaussian_heisenberg_joint.npz',
    'bc_gaussian_heisenberg_model.json','bc_gaussian_heisenberg_source.json',
    'bc_orbifold_CM_export.json','de_ferrari_fibres.json']


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true')
    args=parser.parse_args();inputs=PYTHON_INPUTS+DATA_INPUTS
    assert len(inputs)==len(set(inputs))
    protected={ROOT/'code'/n for n in inputs}
    protected.update(p for p in (ROOT/'code').glob('a_cm_matrix_gaussian_*')
                     if p.is_file() and p.name not in {
                         'a_cm_matrix_gaussian_manifest.out',
                         'a_cm_matrix_gaussian_manifest.err'})
    protected.update(p for p in (ROOT/'research/A_matrix_gaussian_unsigned_failure').iterdir()
                     if p.is_file())
    preserved=ROOT/'research/E74_initial_build'
    if preserved.exists():protected.update(p for p in preserved.iterdir() if p.is_file())
    protected.update(ROOT/n for n in [
        'sections/E_matrix_gaussian_joint_agent.tex',
        'research/A_E71_E69_join.md','research/A_matrix_gaussian_join_manifest.json'])
    if args.final:
        protected.add(ROOT/'research/E74_REPLAY.md')
        peer=ROOT/'research/BC_E74_independent_audit.md'
        if peer.exists():protected.add(peer)
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(protected)}
    result={'status':'FROZEN_E74_AUTHORITATIVE_BATCH' if args.final else 'E74_DRAFT_REPLAY_BATCH',
            'minimal_input_files':inputs,'mathematical_stage_stems':STAGES,
            'sha256':hashes,'whole_domain':'K6 intersect F-prime',
            'actual_origin_source':'de_ferrari_fibres.json: literal E17 words retained by E71',
            'joint_group':'P_E71 times_(M_E67) L_E69',
            'group_order_factorization':{'2':105,'3':20},
            'finite_joint_value_count':55296,
            'central_word_full_source_orders':[4,1,1],
            'central_word_powers':[4,1,1],
            'verified_dynamic_hash_rule':
                'Verify every input hash against actual input bytes; remove only the witness-stage input hash of a_cm_matrix_gaussian_join.json, whose measured runtime changes, from mathematical equality.',
            'preserved_failed_attempt':'research/A_matrix_gaussian_unsigned_failure',
            'replay_guide':'research/E74_REPLAY.md'}
    target=ROOT/'research'/('E74_authoritative_manifest.json' if args.final else 'E74_draft_manifest.json')
    if target.exists():raise SystemExit('Refusing to replace manifest: '+str(target))
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'path':str(target.relative_to(ROOT)),
                      'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                      'minimal_inputs':len(inputs),'protected_files':len(hashes)},indent=2))


if __name__=='__main__':main()
