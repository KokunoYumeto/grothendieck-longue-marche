"""Run the two frozen F29 word verifiers in an isolated input directory.

Only the explicitly listed path fields are transported back for comparison.
All other serialized bytes, including every formula and count, must agree.
"""
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'work/part_a/code'
TARGET = ROOT / 'work/root/f29_independent_replay'
TARGET.mkdir(parents=True, exist_ok=True)
VERIFIERS = [
    ('affine_four_parameter_extension_independent_audit', 3246),
    ('affine_four_parameter_r1_independent_audit', 996),
]
CHARTS = [
    'affine_product_one_four_parameter_stage',
    'affine_product_one_deleted_first_stage',
    'affine_deleted_first_two_parameter_stage',
]
FILES = [name + '.py' for name, _ in VERIFIERS]
FILES += [name + suffix for name in CHARTS for suffix in ('.py', '_output.json')]
FILES += ['full_cross_source_stage/marginal_braids.json', 'affine_obstruction_stage_output.json']

def binding(path):
    return {'path': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size,
            'sha256': sha256(path.read_bytes()).hexdigest()}

copied = []
for name in FILES:
    source, target = SOURCE/name, TARGET/name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    assert source.read_bytes() == target.read_bytes()
    copied.append({'original': binding(source), 'copy': binding(target)})

comparisons = []
for name, count in VERIFIERS:
    completed = subprocess.run(['python', str(TARGET/(name+'.py'))],
                               cwd=TARGET, text=True, capture_output=True)
    (TARGET/(name+'_stdout.txt')).write_text(completed.stdout)
    (TARGET/(name+'_stderr.txt')).write_text(completed.stderr)
    assert completed.returncode == 0, completed.stderr
    original_path = SOURCE/(name+'_output.json')
    replay_path = TARGET/(name+'_output.json')
    original = json.loads(original_path.read_text())
    replay = json.loads(replay_path.read_text())
    assert replay['check_total'] == original['check_total'] == count
    mapping = {}
    if 'base_inputs' in replay:
        for key in replay['base_inputs']:
            mapping[key] = str(SOURCE/Path(key).relative_to(TARGET))
        for chart in replay['charts']:
            for key in ('symbolic_input', 'symbolic_producer'):
                mapping[chart[key]] = str(SOURCE/Path(chart[key]).relative_to(TARGET))
        replay['base_inputs'] = {mapping[k]: v for k, v in replay['base_inputs'].items()}
        for chart in replay['charts']:
            for key in ('symbolic_input', 'symbolic_producer'):
                chart[key] = mapping[chart[key]]
    if 'inputs' in replay:
        for key in replay['inputs']:
            mapping[key] = str(SOURCE/Path(key).relative_to(TARGET))
        replay['inputs'] = {mapping[k]: v for k, v in replay['inputs'].items()}
    assert len(mapping) == len(set(mapping.values()))
    assert replay == original
    transported = (json.dumps(replay, indent=2)+'\n').encode()
    assert transported == original_path.read_bytes()
    mapped_path = TARGET/(name+'_path_transport_output.json')
    mapped_path.write_bytes(transported)
    comparisons.append({'status': 'PASS', 'checks': count,
                        'original': binding(original_path), 'replay': binding(replay_path),
                        'raw_byte_identical': replay_path.read_bytes() == original_path.read_bytes(),
                        'exact_path_bijection': mapping,
                        'path_transported_output_byte_identical': True,
                        'path_transported_output': binding(mapped_path),
                        'stdout': binding(TARGET/(name+'_stdout.txt')),
                        'stderr': binding(TARGET/(name+'_stderr.txt'))})

result = {'status': 'PASS', 'check_total': sum(x['checks'] for x in comparisons),
          'copied_inputs': copied, 'verifiers': comparisons,
          'script': binding(Path(__file__).resolve()),
          'scope': 'Two exact word-verifier replays only; the full F29 proof requires separate review.'}
(TARGET/'comparison.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': result['status'], 'check_total': result['check_total'],
                  'verifiers': [{'checks': x['checks'], 'raw_byte_identical': x['raw_byte_identical'],
                                 'path_transported_output_byte_identical': True,
                                 'path_fields': len(x['exact_path_bijection']),
                                 'replay_sha256': x['replay']['sha256']} for x in comparisons]}, indent=2))
