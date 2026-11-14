#!/usr/bin/env python3
"""Create the exact E71 replay manifest without changing mathematical files."""
from pathlib import Path
import argparse
import hashlib
import json

ROOT=Path(__file__).resolve().parent.parent
STAGES=['a_cm_kn23_'+s for s in ['model','source','ab_lattice','full','fibres','witnesses',
                               'nprime_comparison','coefficient','numeric_summary']]
CERTIFICATES=['a_cm_kn23_'+s for s in ['N','N_derived','projected','old_kernel',
                                     'full_projected','full_old_kernel']]


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true')
    args=parser.parse_args()
    inputs=[s+'.py' for s in STAGES]+[
        'a_cm_fixed_base.cpp','de_a6_schreier.cpp','de_a6_schreier_certificate.py',
        'a_cm_distribution_e62.py','a_cm_distribution_orbifold.py','a_cm_gl23_pc.py',
        'de_ferrari_a6_source_data.py','de_ferrari_sl2_5_N.json','de_ferrari_fibres.json',
        'a_cm_gl23_model.npz','a_cm_sl23_model.npz',
        'a_cm_distribution_orbifold.npz','a_cm_distribution_orbifold.json',
        'a_cm_distribution_orbifold_projected.bin',
        'bc_orbifold_CM_export.json','bc_orbifold_CM_export.npz',
        'a_cm_gl23_joint_pentagon.json','a_cm_gl23_joint_pc.npz']
    inputs += [f'a_cm_gl23_joint_pc_certificates/prefix_{i:02d}.bin' for i in range(19)]
    assert len(inputs)==len(set(inputs))
    protected={ROOT/'code'/n for n in inputs}
    protected.update(p for p in (ROOT/'code').glob('a_cm_kn23_*') if p.is_file())
    protected.update(p for p in (ROOT/'research/A_Kn23_failed_elementary_quotient').iterdir()
                     if p.is_file())
    if args.final:
        protected.update(ROOT/n for n in ['sections/E_kn_matrix_agent.tex',
                         'research/E71_REPLAY.md','research/A_Kn23_matrix_test.md'])
        for n in ['research/BC_E71_independent_audit.md']:
            if (ROOT/n).exists():protected.add(ROOT/n)
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(protected)}
    out={'status':'FROZEN_E71_AUTHORITATIVE_BATCH' if args.final else 'E71_DRAFT_FIXED_MATHEMATICAL_BATCH',
         'minimal_input_files':inputs,'mathematical_stage_stems':STAGES,
         'complete_certificate_stems':CERTIFICATES,'sha256':hashes,
         'actual_origin_source':'de_ferrari_fibres.json, exact E17 origins retained by E62/E68',
         'exact_domain':'K6 intersect F-prime, via the explicit integral kernel lattice',
         'finite_fibre_count':18432,'source_word_generator_count':97,
         'source_degree':11691,'projected_degree':7501,
         'verified_dynamic_hash_rule':'Check every input hash against its actual file; omit only generated-JSON input hashes from mathematical equality after verification.',
         'preserved_failed_step':'research/A_Kn23_failed_elementary_quotient',
         'replay_guide':'research/E71_REPLAY.md'}
    target=ROOT/'research'/('E71_authoritative_manifest.json' if args.final else 'E71_draft_manifest.json')
    if target.exists():raise SystemExit('Manifest destination already exists: '+str(target))
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'path':str(target.relative_to(ROOT)),
                      'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                      'input_files':len(inputs),'protected_files':len(hashes)},indent=2))


if __name__=='__main__':main()
