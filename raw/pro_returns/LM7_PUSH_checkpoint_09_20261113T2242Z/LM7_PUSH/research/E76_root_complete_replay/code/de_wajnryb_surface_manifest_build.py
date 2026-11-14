#!/usr/bin/env python3
"""Build the exact E76 manifest without modifying mathematical artifacts."""
from pathlib import Path
from hashlib import sha256
import ast
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SEEDS = ['de_wajnryb_free_model.py', 'de_wajnryb_s3_model.py',
         'de_wajnryb_s3_source.py', 'de_wajnryb_s3_fibres.py',
         'de_wajnryb_s4_model.py', 'de_wajnryb_s4_source.py',
         'de_wajnryb_s4_fibres.py']


def main():
    pending, closure = list(SEEDS), set()
    while pending:
        name = pending.pop()
        if name in closure:
            continue
        closure.add(name)
        for node in ast.walk(ast.parse((HERE/name).read_text())):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module]
            for module in modules:
                local = module.split('.')[0]+'.py'
                if (HERE/local).is_file() and local not in closure:
                    pending.append(local)
    paths = {Path('code')/n for n in closure}
    paths.update(Path('code')/n for n in [
        'de_ferrari_sl2_5_N.json', 'de_ferrari_fibres.json',
        'de_ferrari_two_lift.json', 'de_ferrari_degree6_kernel.json',
        'de_ferrari_two_degree6_module.json',
        'de_wajnryb_surface_replay.py', 'de_wajnryb_surface_manifest_build.py',
        'de_wajnryb_s4_engines_prepare.json'])
    outputs = ['de_wajnryb_free_model.json']
    for suffix in ('.json', '.out', '.err'):
        paths.add(Path('code')/('de_wajnryb_free_model'+suffix))
    steps = [{'label': 'free_model', 'arguments': ['de_wajnryb_free_model.py'],
              'outputs': ['de_wajnryb_free_model.json']}]
    for group, genus in [('s3', 2), ('s3', 3), ('s4', 2)]:
        stem = f'de_wajnryb_{group}_g{genus}'
        model_outputs = [stem+'.json', stem+'.npz', stem+'_target.input']
        source_outputs = [stem+'_source.json', stem+'_source.npz',
                          stem+'_source_raw.npz', stem+'_source.input']
        fibre_outputs = [stem+'_fibres.json', stem+'_fibres.npz']
        for kind, new in [('model', model_outputs), ('source', source_outputs), ('fibres', fibre_outputs)]:
            args = [f'de_wajnryb_{group}_{kind}.py', '--genus', str(genus)]
            steps.append({'label': f'{group}_g{genus}_{kind}', 'arguments': args, 'outputs': new})
            outputs.extend(new)
            paths.update(Path('code')/name for name in new)
            logstem = stem if kind == 'model' else stem+'_'+kind
            paths.update(Path('code')/(logstem+ext) for ext in ('.out', '.err'))
    documents = ['sections/E_wajnryb_surface_covers_agent.tex',
                 'research/A_Wajnryb_nonlinear_independent_audit.md',
                 'research/DE_E76_replay.md']
    paths.update(map(Path, documents))
    for name in ['research/E72_nonlinear_initial_boundary_sign',
                 'research/E74_S4_initial_engine_metadata']:
        paths.update(p.relative_to(ROOT) for p in (ROOT/name).rglob('*') if p.is_file())
    files = {}
    for name in sorted(paths):
        actual = ROOT/name
        assert actual.is_file(), ('missing frozen artifact', str(name))
        files[str(name)] = {'sha256': sha256(actual.read_bytes()).hexdigest(), 'bytes': actual.stat().st_size}
    result = {'status': 'FROZEN_COMPLETE_E76_BATCH',
              'statement': 'E.76', 'local_import_closure': sorted(closure),
              'steps': steps, 'files': files,
              'scope': 'Complete free/capped surface models and all fixed-G6 fibres for S3 genus2/3 and S4 genus2.',
              'excluded_next_batch': 'All de_wajnryb_a5_* artifacts.'}
    (HERE/'de_wajnryb_surface_manifest.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'file_count': len(files),
                      'steps': len(steps), 'bytes': sum(r['bytes'] for r in files.values()),
                      'local_python_modules': len(closure)}, indent=2))


if __name__ == '__main__':
    main()
