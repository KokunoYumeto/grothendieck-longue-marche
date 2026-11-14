#!/usr/bin/env python3
"""Write the E.59 immutable manifest once; existing manifests are not replaced."""
from pathlib import Path
import ast,hashlib,json

ROOT=Path(__file__).resolve().parent.parent
CODE=ROOT/'code';OUT=ROOT/'research/E59_authoritative_manifest.json'
if OUT.exists():raise SystemExit('Manifest already exists; preserve it before a reviewed replacement.')
names=['model','source','induced','corrections','generation','periodic','cm_labels','replay']
inputs={CODE/('a_cm_sl23_'+name+'.py') for name in names}
queue=list(inputs)
for path in queue:
    tree=ast.parse(path.read_text())
    for node in ast.walk(tree):
        mods=[]
        if isinstance(node,ast.Import):mods=[a.name.split('.')[0] for a in node.names]
        elif isinstance(node,ast.ImportFrom) and node.module:mods=[node.module.split('.')[0]]
        for module in mods:
            other=CODE/(module+'.py')
            if other.exists() and other not in inputs:inputs.add(other);queue.append(other)
inputs|={CODE/'de_a6_schreier.cpp',CODE/'de_ferrari_fibres.json',CODE/'de_ferrari_sl2_5_N.json'}
files=set(inputs)
for path in CODE.glob('a_cm_sl23*'):
    if path.is_file():files.add(path)
    elif path.is_dir():files.update(p for p in path.rglob('*') if p.is_file())
files|={ROOT/'sections/E_sl23_ferrari_agent.tex',ROOT/'research/A_SL23_Ferrari.md',
        ROOT/'research/E59_REPLAY.md',ROOT/'research/A_E58_independent_review.md',
        CODE/'de_a6_schreier_fast'}
for path in (ROOT/'research').glob('E59*'):
    if path.is_file():files.add(path)
    elif path.is_dir():files.update(p for p in path.rglob('*') if p.is_file() and 'texmf' not in str(p))
def rel(p):return str(p.relative_to(ROOT))
def role(p):
    name=rel(p)
    if p in inputs:return 'replay_input'
    if any(s in name for s in ('failed','interrupted','initial','before_Q')):return 'preserved_prior_attempt'
    if 'generation_certificates' in name:return 'authoritative_generation_certificate'
    if name.startswith('sections/'):return 'authoritative_proof'
    if name.startswith('research/'):return 'research_or_typesetting_record'
    return 'authoritative_output_or_auxiliary_source_check'
manifest={'statement':'E.59','status':'FROZEN_COMPLETE_FINITE_SL23_TEST',
          'scope':'Complete512-element correction fibres above24 specified E17 G6 points; every CM matrix pair represented; no full profinite pentagon claim.',
          'input_files':sorted(map(rel,inputs)),
          'semantic_json_outputs':['code/a_cm_sl23_'+name+'.json' for name in names if name!='replay'],
          'semantic_npz_outputs':['code/a_cm_sl23_'+name+'.npz' for name in
             ('model','source','induced','corrections','quaternion_projections')],
          'files':{rel(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                           'bytes':p.stat().st_size,'role':role(p)} for p in sorted(files)}}
OUT.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'status':'FROZEN','manifest':rel(OUT),
                  'manifest_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
                  'input_files':len(inputs),'protected_files':len(files)},indent=2))
