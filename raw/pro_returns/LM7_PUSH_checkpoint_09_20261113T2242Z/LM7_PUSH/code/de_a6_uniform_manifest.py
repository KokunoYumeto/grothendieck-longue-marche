#!/usr/bin/env python3
"""Freeze the E57 additions and verify every reused E54 artifact unchanged."""
from pathlib import Path
import ast, hashlib, json, re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EXT = {'.py', '.cpp', '.json', '.npz', '.bin', '.input', '.out', '.err'}
OMIT = {'de_a6_uniform_manifest.json', 'de_a6_uniform_manifest.out', 'de_a6_uniform_manifest.err'}


def main():
    records = {}; queue = []; seen = set()

    def add(path, role):
        path = Path(path)
        if not path.is_file() or path.parent != HERE or path.suffix not in EXT or path.name in OMIT:
            return
        name = str(path.relative_to(ROOT))
        records.setdefault(name, {'roles': set()})['roles'].add(role)
        if path.suffix in {'.py', '.json'} and path not in seen:
            queue.append(path)

    frozen = json.loads((HERE / 'de_a6_gl_manifest.json').read_text())
    protected = {}
    for name, value in frozen['records'].items():
        path = ROOT / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == value['sha256'], name
        protected[name] = digest
        add(path, 'Unchanged E54 dependency')
    for path in HERE.glob('de_a6_uniform_*'):
        add(path, 'E57 addition or explicitly preserved preliminary attempt')

    def hashes(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, str) and re.fullmatch(r'[0-9a-f]{64}', v):
                    add(HERE / Path(k).name, 'Named supplied-data hash dependency')
                else:
                    hashes(v)
        elif isinstance(obj, list):
            for value in obj:
                hashes(value)

    while queue:
        path = queue.pop()
        if path in seen:
            continue
        seen.add(path)
        if path.suffix == '.json':
            try:
                hashes(json.loads(path.read_text()))
            except json.JSONDecodeError:
                pass
            continue
        for node in ast.walk(ast.parse(path.read_text(), filename=str(path))):
            modules = []
            if isinstance(node, ast.Import):
                modules = [v.name.split('.')[0] for v in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module.split('.')[0]]
            for module in modules:
                add(HERE / (module + '.py'), 'Local import dependency, supplied read-only')
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                value = node.value
                if '\n' in value or len(value) > 180:
                    continue
                name = Path(value).name
                if re.fullmatch(r'(?:de|bc|a|e)_[A-Za-z0-9_.-]+', name):
                    if (HERE / name).is_file():
                        add(HERE / name, 'Literal data dependency')
                    elif '.' not in name:
                        for p in HERE.glob(name + '.*'):
                            add(p, 'Literal data-stem dependency')

    for name, value in records.items():
        data = (ROOT / name).read_bytes()
        value.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data),
                     roles=sorted(value['roles']))
    docs = ['sections/E_a6_uniform_agent.tex', 'research/DE_a6_uniform.md',
            'research/DE_a6_uniform_replay.md']
    audits = []
    for name in ['audit_a6_joint_chains_root.json', 'audit_a6_joint_quotients_resume_root.json']:
        p = HERE / name
        if p.is_file():
            raw = json.loads(p.read_text())
            audits.append({'file': 'code/' + name, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                           'all_passed': raw.get('all_passed'),
                           'note': 'Root E54 replay; representational generator-list resolution is retained in its own certificate.'})
    out = {
        'status': 'PASS_FROZEN_E57_PACKAGE',
        'scope': 'Full E55 family with the complete A6 refinement; exact source and target products through every modulus prime to six',
        'new_programs_in_replay_order': [
            'de_a6_uniform_comparison.py', 'de_a6_uniform_target_prepare.py',
            'de_a6_schreier_fast --replay de_a6_uniform_target.bin',
            'de_a6_uniform_target_certificate.py'],
        'replay_guide': 'research/DE_a6_uniform_replay.md',
        'old_E54_manifest_sha256': hashlib.sha256((HERE / 'de_a6_gl_manifest.json').read_bytes()).hexdigest(),
        'all_E54_artifacts_unchanged': True, 'E54_protected_file_count': len(protected),
        'previous_root_audits': audits,
        'records': dict(sorted(records.items())),
        'documents': {n: {'sha256': hashlib.sha256((ROOT / n).read_bytes()).hexdigest(),
                           'bytes': (ROOT / n).stat().st_size} for n in docs},
        'file_count': len(records), 'total_bytes': sum(v['bytes'] for v in records.values()),
        'replay_rule': 'Isolated copy; four displayed steps only. Reuse unchanged accepted E54/E52 dependencies. Preserve originals; compare mathematics and exact arrays, allowing elapsed-time/provenance changes.',
    }
    (HERE / 'de_a6_uniform_manifest.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['status', 'scope', 'all_E54_artifacts_unchanged',
                                        'E54_protected_file_count', 'file_count', 'total_bytes']}, indent=2))


if __name__ == '__main__':
    main()
