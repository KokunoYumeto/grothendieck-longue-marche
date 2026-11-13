#!/usr/bin/env python3
"""Freeze the E48 replay package without changing any mathematical input.

The manifest separates previously root-audited unchanged inputs, the new
complete source chains, support code, replay records, and retained history.
It deliberately excludes the subsequent A6/A5 and A6/GL joint-source work.
"""
from pathlib import Path
import ast
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXTENSIONS = {'.py', '.cpp', '.json', '.npz', '.out', '.input', '.bin'}

PROGRAMS = [
    'de_ferrari_a6_model', 'de_ferrari_a6_source_verified',
    'de_ferrari_a6_N_quotient', 'de_ferrari_a6_abelian_compare',
    'de_ferrari_a6_target_derived', 'de_ferrari_a6_residual_certificate',
    'de_ferrari_a6_metabelian', 'de_ferrari_a6_metafibres',
    'de_ferrari_a6_metageneration', 'de_ferrari_a6_metawords',
    'de_ferrari_a6_solvable', 'de_ferrari_a6_solvable_lift',
    'de_ferrari_a6_solvable_endomorphisms', 'de_ferrari_a6_common',
    'de_ferrari_a6_common_words', 'de_ferrari_a6_kummer_labels',
]
CHAINS = [
    'de_a6_schreier_full_ordered', 'de_a6_schreier_N',
    'de_a6_schreier_Fprime', 'de_a6_schreier_Fprimecompact',
    'de_a6_schreier_Nprime', 'de_a6_schreier_Fprimeprime',
    'de_a6_schreier_residual', 'de_a6_schreier_residual_derived',
    'de_a6_schreier_Nielsenprime', 'de_a6_schreier_Nielsencompact',
    'de_a6_schreier_Nielsenprimeprime',
]
SUPPORT = [
    'de_a6_schreier', 'de_a6_schreier_certificate',
    'de_a6_schreier_prepare', 'de_a6_schreier_mix',
    'de_a6_subgroup_checks', 'de_a6_quotient', 'de_a6_module',
    'de_a6_binary_module', 'de_a6_residual_module_prepare',
    'de_ferrari_a6_source', 'de_ferrari_a6_source_data',
]
INPUT_PREFIXES = [
    'de_a6_schreier_F', 'de_a6_schreier_N',
    'de_a6_schreier_residual', 'de_a6_module_basis',
    'de_a6_binary_module', 'de_a6_residual_quotient',
    'de_a6_source_mod_N', 'de_ferrari_a6_source_',
    'de_ferrari_a6_module_annihilator',
]
CONTROL_PREFIXES = [
    'de_a6_schreier_control', 'de_a6_module_control',
    'de_a6_quotient_control',
]


def main():
    records = {}
    queue = []
    visited = set()

    def add(path, role):
        path = Path(path)
        if not path.is_file() or path.suffix not in EXTENSIONS:
            return
        if any(part.startswith('root_') for part in path.parts):
            return
        name = str(path.relative_to(ROOT))
        rec = records.setdefault(name, {'roles': set()})
        rec['roles'].add(role)
        if path.suffix == '.py' and path not in visited:
            queue.append(path)

    def family(stem, role, broad=False):
        pattern = stem + ('*' if broad else '.*')
        for path in sorted(HERE.glob(pattern)):
            add(path, role)

    for stem in PROGRAMS:
        family(stem, 'E48 authoritative program and outputs')
    for stem in CHAINS:
        family(stem, 'E48 exact source/target chain', broad=True)
    for stem in SUPPORT:
        family(stem, 'E48 support code and model provenance')
    for stem in INPUT_PREFIXES:
        family(stem, 'E48 exact input or quotient record', broad=True)
    for stem in CONTROL_PREFIXES:
        family(stem, 'Optional independently replayed finite control', broad=True)
    family('de_ferrari_a6_kernels', 'Accepted E45 epikernel model')
    family('de_ferrari_a6_kernel_targets', 'Accepted E45 target record')
    family('de_ferrari_a6_model_failed_initial_field', 'Retained metadata failure')
    family('de_ferrari_a6_abelian_compare_failed_initial_field', 'Retained metadata failure')
    add(Path(__file__), 'Manifest generator')

    # Static local-import closure plus literal filenames. These are supplied
    # inputs, not permission to rerun their legacy main programs.
    while queue:
        path = queue.pop()
        if path in visited:
            continue
        visited.add(path)
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name.split('.')[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module.split('.')[0]]
            for module in modules:
                add(HERE / (module + '.py'), 'Transitive local Python dependency')
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                value = node.value
                if '\n' in value or len(value) > 160:
                    continue
                filename = Path(value).name
                if re.fullmatch(r'(?:de|bc|a|e)_[A-Za-z0-9_.-]+', filename):
                    if (HERE / filename).is_file():
                        add(HERE / filename, 'Literal input/output dependency')
                    elif '.' not in filename:
                        family(filename, 'Literal stem dependency')

    # The two broad N/F chain families above are intentional; unrelated
    # common-source explorations must never enter this frozen package.
    assert not any('de_a6_a5_' in n or 'de_a6_gl_' in n for n in records)

    for name, rec in records.items():
        data = (ROOT / name).read_bytes()
        rec['sha256'] = hashlib.sha256(data).hexdigest()
        rec['bytes'] = len(data)
        rec['roles'] = sorted(rec['roles'])

    previous = []
    for name in ('audit_a6_kernel_resolution_root.json',
                 'audit_threeadic_a6_root.json'):
        raw = json.loads((HERE / name).read_text())
        checked = []
        for field in ('protected_sha256', 'dependency_sha256'):
            for basename, digest in raw.get(field, {}).items():
                rel = 'code/' + basename
                if rel in records:
                    checked.append({'file': rel, 'record': field,
                                    'recorded_sha256': digest,
                                    'unchanged': records[rel]['sha256'] == digest})
        previous.append({'audit': 'code/' + name,
                         'all_passed': raw['all_passed'],
                         'audit_sha256': hashlib.sha256((HERE/name).read_bytes()).hexdigest(),
                         'matching_package_inputs': checked})

    document_paths = ['sections/E_a6_full_agent.tex',
                      'research/DE_a6_replay.md',
                      'research/DE_a6_E48_before_proof_intro.tex']
    documents = {name: {'sha256': hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),
                        'bytes': (ROOT/name).stat().st_size}
                 for name in document_paths}
    result = {
        'status': 'PASS',
        'scope': 'E48 full A6 + D23 only; subsequent joint G_L work excluded',
        'program_replay_order': [p + '.py' for p in PROGRAMS],
        'complete_chain_replay_order': [s + '.bin' for s in CHAINS],
        'new_source_chain_root_replays': [],
        'new_source_chain_root_replay_note':
            'No prior root-specific full E48 chain replay was found. Existing fresh replays are agent replays, explicitly recorded separately.',
        'previous_root_audits': previous,
        'records': dict(sorted(records.items())),
        'documents': documents,
        'file_count': len(records),
        'total_bytes': sum(r['bytes'] for r in records.values()),
        'replay_rule': 'Compile C++ sources; replay supplied chains instead of repeating discovery. Compare mathematical JSON fields and literal arrays; elapsed-time fields may differ. Do not execute legacy dependency mains.',
    }
    (HERE/'de_a6_e48_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('status','scope','file_count','total_bytes')}))
    print(json.dumps({'previous_root_matches': [
        {'audit': r['audit'], 'matches': sum(v['unchanged'] for v in r['matching_package_inputs']),
         'changed': [v['file'] for v in r['matching_package_inputs'] if not v['unchanged']]}
        for r in previous]}))


if __name__ == '__main__':
    main()
