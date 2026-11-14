#!/usr/bin/env python3
"""Freeze E54 and distinguish its new checks from unchanged root E48 gates."""
from pathlib import Path
import ast, hashlib, json, re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXTENSIONS = {'.py', '.cpp', '.json', '.npz', '.out', '.err', '.input', '.bin'}
EXCLUDED = {'de_a6_gl_manifest.json', 'de_a6_gl_manifest.out', 'de_a6_gl_manifest.err'}


def main():
    records = {}; queue = []; seen = set()

    def add(path, role):
        path = Path(path)
        if not path.is_file() or path.suffix not in EXTENSIONS or path.name in EXCLUDED:
            return
        assert path.parent == HERE
        name = str(path.relative_to(ROOT))
        records.setdefault(name, {'roles': set()})['roles'].add(role)
        if path.suffix in {'.py', '.json'} and path not in seen:
            queue.append(path)

    def family(stem, role):
        for p in sorted(HERE.glob(stem + '*')):
            add(p, role)

    family('de_a6_gl_', 'E54 new authoritative program, input, result, or preserved attempt')
    family('de_a6_a5_common_source', 'E54 actual A6/A5 base and compression maps')
    for name in ['de_a6_schreier.cpp', 'de_a6_schreier_certificate.py',
                 'de_a6_schreier_mix.py', 'de_a6_subgroup_checks.cpp']:
        add(HERE / name, 'Complete engine and independent word support')
    old_manifest = json.loads((HERE / 'de_a6_e48_manifest.json').read_text())
    for name in old_manifest['records']:
        add(ROOT / name, 'Supplied E48 dependency, already root-audited where indicated')

    def hash_dependencies(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str) and re.fullmatch(r'[0-9a-f]{64}', value):
                    p = HERE / Path(key).name
                    if p.is_file():
                        add(p, 'Named hash dependency in supplied data')
                else:
                    hash_dependencies(value)
        elif isinstance(obj, list):
            for value in obj:
                hash_dependencies(value)

    while queue:
        path = queue.pop()
        if path in seen:
            continue
        seen.add(path)
        if path.suffix == '.json':
            try:
                hash_dependencies(json.loads(path.read_text()))
            except json.JSONDecodeError:
                pass
            continue
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name.split('.')[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module.split('.')[0]]
            for module in modules:
                add(HERE / (module + '.py'), 'Transitive local Python dependency; main is not invoked')
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                value = node.value
                if '\n' in value or len(value) > 180:
                    continue
                name = Path(value).name
                if re.fullmatch(r'(?:de|bc|a|e)_[A-Za-z0-9_.-]+', name):
                    if (HERE / name).is_file():
                        add(HERE / name, 'Literal data or support dependency')
                    elif '.' not in name:
                        for p in HERE.glob(name + '.*'):
                            add(p, 'Literal data-stem dependency')

    for name, record in records.items():
        data = (ROOT / name).read_bytes()
        record.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data),
                      roles=sorted(record['roles']))

    prior = []
    for filename in ['audit_a6_full_chains_root.json', 'audit_a6_full_quotients_root.json']:
        raw = json.loads((HERE / filename).read_text())
        assert raw['all_passed'] and raw['original_artifacts_unchanged']
        matches = []
        for name, digest in raw['protected_sha256'].items():
            if name in records:
                matches.append({'file': name, 'recorded_sha256': digest,
                                'unchanged': records[name]['sha256'] == digest})
        assert all(r['unchanged'] for r in matches)
        prior.append({'audit': 'code/' + filename,
                      'audit_sha256': hashlib.sha256((HERE / filename).read_bytes()).hexdigest(),
                      'all_passed': True, 'matching_reused_inputs': matches})

    docs = ['sections/E_a6_joint_agent.tex', 'research/DE_a6_gl.md',
            'research/DE_a6_gl_replay.md', 'research/DE_Steinberg.bib',
            'research/DE_a6_gl_before_target_reconstructed.tex',
            'research/DE_a6_gl_prefreeze_changes.json']
    documents = {name: {'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest(),
                        'bytes': (ROOT / name).stat().st_size} for name in docs}
    chains = ['de_a6_a5_common_source.bin', 'de_a6_gl_lower_chain.bin',
              'de_a6_gl_A5_source.bin', 'de_a6_gl_target.bin']
    chains += [f'de_a6_gl_target_derived{j}.bin' for j in range(1, 5)]
    result = {
        'status': 'PASS_FROZEN_E54_PACKAGE',
        'scope': 'Exact A6/GL source, perfect residual, all old D23 fibres, specified nilpotent H boundaries, and exact joint four-strand target; no uniform symplectic extension yet',
        'new_complete_chain_replay_order': chains,
        'new_complete_presentation_evaluators': [
            'de_a6_gl_kernel: all1154659 actual joint-base relations',
            'de_a6_gl_kernel on lower control: all128833 relations',
            'de_a6_gl_epikernels on full A6: all865049 relations',
            'de_a6_gl_epikernels on A5: all23945 relations',
            'de_a6_gl_central: all720615 relations plus10 original normal-form relations',
            'de_a6_subgroup_checks: all747 target normality conjugations'],
        'replay_guide': 'research/DE_a6_gl_replay.md',
        'existing_root_audits': prior,
        'primary_bibliography': {
            'DE_Steinberg1967': {
                'status': 'Primary original PDF independently opened and verified by root and agent',
                'location': 'Section7 Theorem10 and Corollary2(b); explicit SL_n to PSL_n universal map',
                'url': 'https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf',
                'corollary_PDF_page_indices': [88, 89]}},
        'records': dict(sorted(records.items())), 'documents': documents,
        'file_count': len(records), 'total_bytes': sum(r['bytes'] for r in records.values()),
        'replay_rule': 'Use isolated copies. Compile supplied C++ sources and replay saved complete chains, not discovery. Compare mathematical records and exact arrays; elapsed times and their dependent provenance hashes can differ. Preserve all original source artifacts.',
    }
    (HERE / 'de_a6_gl_manifest.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'scope', 'file_count', 'total_bytes']}, indent=2))
    print(json.dumps({'unchanged_prior_root_inputs': [
        {'audit': p['audit'], 'count': len(p['matching_reused_inputs'])} for p in prior]}, indent=2))


if __name__ == '__main__':
    main()
