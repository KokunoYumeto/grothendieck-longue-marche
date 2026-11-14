#!/usr/bin/env python3
"""Freeze the complete E.62 proof and finite computation exactly once."""
from pathlib import Path
import ast,hashlib,json

ROOT=Path(__file__).resolve().parent.parent;CODE=ROOT/'code'
OUT=ROOT/'research/E62_authoritative_manifest.json'
if OUT.exists():raise SystemExit('E62 manifest exists; preserve it before any reviewed replacement.')
names=['group','model','source','induced','structure','joint','pc','gentle','pentagon',
       'projections','generation','single_generation','replay']
inputs={CODE/('a_cm_gl23_'+name+'.py') for name in names};queue=list(inputs)
for path in queue:
    for node in ast.walk(ast.parse(path.read_text())):
        mods=[]
        if isinstance(node,ast.Import):mods=[v.name.split('.')[0] for v in node.names]
        elif isinstance(node,ast.ImportFrom) and node.module:mods=[node.module.split('.')[0]]
        for module in mods:
            other=CODE/(module+'.py')
            if other.exists() and other not in inputs:inputs.add(other);queue.append(other)
inputs |= {CODE/name for name in ('de_a6_schreier.cpp','de_ferrari_fibres.json','de_ferrari_sl2_5_N.json',
    'a_cm_sl23_model.npz','a_cm_sl23_model.json','a_cm_sl23_induced.npz',
    'a_cm_sl23_corrections.npz','a_cm_sl23_corrections.json','a_cm_sl23_B_source_chain.out')}
files=set(inputs)
for path in CODE.glob('a_cm_gl23*'):
    if path.is_file():files.add(path)
    elif path.is_dir():files.update(p for p in path.rglob('*') if p.is_file())
files |= {ROOT/'sections/E_gl23_ferrari_agent.tex',ROOT/'research/A_GL23_Ferrari.md',
          ROOT/'research/E62_REPLAY.md',CODE/'de_a6_schreier_fast'}
for path in (ROOT/'research').glob('E62*'):
    if path.is_file():files.add(path)
    elif path.is_dir():files.update(p for p in path.rglob('*') if p.is_file() and 'texmf' not in str(p))
for path in (ROOT/'research').glob('A_GL23*'):
    if path.is_file():files.add(path)
def rel(path):return str(path.relative_to(ROOT))
def role(path):
    name=rel(path)
    if path in inputs:return 'replay_input'
    if any(s in name for s in ('failed','initial','before_')):return 'preserved_prior_attempt'
    if 'generation_certificates' in name:return 'authoritative_generation_certificate'
    if 'pc_certificates' in name:return 'authoritative_coordinate_certificate'
    if name.startswith('sections/'):return 'authoritative_proof'
    if name.startswith('research/'):return 'research_or_typesetting_record'
    return 'authoritative_output_or_structure_check'
jsons=['group','model','source','induced','joint','single_pc','joint_pc','single_gentle','joint_gentle',
       'single_pentagon','joint_pentagon','projections','generation','single_generation','preimages',
       'N_small_map','joint_N_small_map']
arrays=['group','model','source','induced','joint','C_generators','single_pc','joint_pc',
        'single_gentle','joint_gentle','single_pentagon','joint_pentagon']
chains=['B_source','N_source','N_derived','N_small_derived','C_derived',
        'joint_SL23_B','joint_SL23_N','joint_SL23_target','joint_SL23_N_derived',
        'joint_SL23_N_greedy','joint_N_small_derived']
chain_files=['code/a_cm_gl23_'+n+'.out' for n in chains]
for folder in ('a_cm_gl23_single_pc_certificates','a_cm_gl23_joint_pc_certificates',
               'a_cm_gl23_generation_certificates','a_cm_gl23_single_generation_certificates'):
    chain_files += [rel(p) for p in sorted((CODE/folder).glob('*.out'))]
m={'statement':'E.62','status':'FROZEN_COMPLETE_FINITE_GL23_SL23_JOINT_TEST',
   'scope':'Complete2^21 and2^24 correction fibres above24 specified E17 G6 points at multiplier1; four final common points in every CM matrix fibre; no full profinite pentagon conclusion.',
   'input_files':sorted(map(rel,inputs)),
   'semantic_json_outputs':['code/a_cm_gl23_'+name+'.json' for name in jsons],
   'semantic_npz_outputs':['code/a_cm_gl23_'+name+'.npz' for name in arrays],
   'semantic_chain_outputs':chain_files,
   'files':{rel(p):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'role':role(p)}
            for p in sorted(files)}}
OUT.write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps({'status':'FROZEN','manifest':rel(OUT),'manifest_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
                  'input_files':len(inputs),'protected_files':len(files),'chain_outputs':len(chain_files)},indent=2))
