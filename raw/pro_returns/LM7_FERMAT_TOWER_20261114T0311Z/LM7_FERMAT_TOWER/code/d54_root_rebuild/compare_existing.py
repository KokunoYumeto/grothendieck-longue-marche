"""Compare all completed fresh D54 runs, preserving complete stdout prefixes."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'D54_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=SOURCE/'ledger/d_doubled_class2_corrections_manifest.json'
manifest=json.loads(manifest_path.read_text())
for row in manifest['files']+manifest['runtime_inputs']:
    assert sha(SOURCE/row['path'])==row['sha256'],row['path']
comparisons=[]
for name in manifest['run_order']:
    assert sha(HERE/'code'/name)==sha(SOURCE/'code'/name)
    for ext in ['.json','.out']:
        original=SOURCE/'code'/Path(name).with_suffix(ext)
        rebuilt=HERE/'code'/Path(name).with_suffix(ext)
        texts=[p.read_text() for p in [original,rebuilt]]
        starts=[t.index('{') for t in texts]
        prefixes=[t[:i] for t,i in zip(texts,starts)]
        assert prefixes[0]==prefixes[1],(name,'stdout prefix')
        a,b=[json.loads(t[i:]) for t,i in zip(texts,starts)]
        aa,bb=[x['summary'] if ext=='.json' else x for x in [a,b]]
        elapsed=[aa.pop('elapsed_seconds'),bb.pop('elapsed_seconds')]
        assert a==b,original.name
        comparisons.append({'file':original.name,'source_sha256':sha(original),
                            'fresh_sha256':sha(rebuilt),'complete_prefix_equal':True,
                            'all_remaining_fields_equal':True,
                            'only_excluded_field':'/summary/elapsed_seconds' if ext=='.json' else '/elapsed_seconds',
                            'actual_elapsed_values':elapsed})
for row in manifest['runtime_inputs']:
    assert sha(HERE/'code'/Path(row['path']).name)==row['sha256']
record={'status':'PASS','section_sha256':sha(SOURCE/'sections/D_doubled_class2_corrections.tex'),
        'frozen_manifest_sha256':sha(manifest_path),
        'complete_comparisons':comparisons,'inputs':manifest['runtime_inputs'],
        'execution_provenance':'rebuild.py completed all three subprocesses with return code zero, then failed when attempting to parse the two non-JSON stdout progress lines; original failed driver and output retained. This comparison reads the completed fresh outputs and includes those two lines exactly.'}
(HERE/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
