#!/usr/bin/env python3
"""Reconstruct based symmetric data from preserved chronological crossings.

The elementary positive crossing is the geometric push phi_i certified by
the separate exact PL calculation.  art() multiplies on the right, hence
push(W)=art(reverse(W)) and back(W)=art(negate_each(W)).  This producer does
not rerun or modify a crossing, path, or coefficient-isotopy certificate.
The originally mistaken transport arrays remain preserved and untouched.
"""
from pathlib import Path
import json, hashlib, time
import symmetric_node_braid as B

ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'next_symmetric_nodes'
started=time.monotonic()

def read(name): return json.loads((P/name).read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def push(w): return B.art(tuple(reversed(w)))
def back(w): return B.art(tuple(-x for x in w))
def compose(A,C): return {i:B.sub(C[i],A) for i in range(1,22)}
def inverse_check(A,Ai):
    for i in range(1,22):
        assert B.sub(A[i],Ai)==(i,)==B.sub(Ai[i],A)
    assert B.sub(tuple(range(1,22)),A)==tuple(range(1,22))
def write(name,d): (P/name).write_text(json.dumps(d,indent=2)+'\n')

provenance={
 'producer_sha256':sha(Path(__file__)),
 'raw_inputs':{s:sha(P/s) for s in ('symmetric_node_words.json',
                  'symmetric_old_base_words.json','symmetric_source_bridge.json')},
 'push_convention':'push(W)=art(reverse chronological W)',
 'pullback_convention':'back(W)=art(negate each chronological W)',
 'local_calibration':'work_DE/next_marginal_source/cut_Artin_convention.json',
 'local_calibration_sha256':sha(ROOT.parent/'work_DE/next_marginal_source/cut_Artin_convention.json'),
 'recomputed_geometry':False,
 'superseded_candidates_preserved':'pre_pullback_convention/',
}

D=read('symmetric_node_words.json')
rows=[]
for row in D['loops']:
    row=dict(row);W=tuple(row['whisker']);std=tuple(row['standard_local_braid'])
    beta=tuple(row['word']);A=back(W);Ai=push(W)
    inverse_check(A,Ai)
    actual=back(beta)
    assert actual==compose(A,compose(back(std),Ai))
    inverse_check(actual,push(beta))
    nodes=[]
    for old in row['nodes']:
        j,k=old['local_positions'];ca,ga=B.peel(A[j]);cb,gb=B.peel(A[k])
        physical=[D['initial_order'][ga-1],D['initial_order'][gb-1]]
        assert physical==old['physical_labels']
        assert {D['labels'][x]['kind'] for x in physical}=={'A','B'}
        nodes.append({'local_positions':[j,k],'physical_labels':physical,
            'meridians':[A[j],A[k]],'conjugators':[ca,cb],
            'cores':[ga,gb],'commutator':B.comm(A[j],A[k])})
    row['nodes']=nodes
    row['geometric_push_images']=push(beta)
    row['based_pullback_images']=actual
    rows.append(row)
    print('PASS corrected actual node transports',row['index'],'nodes',len(nodes),flush=True)
D.update({'loops':rows,'based_transport_provenance':provenance,
    'basepoint_scope':'Actual source-compatible far marking; corrected endpoint pullback along every chronological whisker.',
    'status':'Corrected geometric based transports; original crossing records unchanged.'})
write('symmetric_node_words_pullback_corrected.json',D)

D=read('symmetric_old_base_words.json');rows=[]
for row in D['loops']:
    row=dict(row);A=push(row['word']);Ai=back(row['word']);inverse_check(A,Ai)
    row.update({'images':A,'inverse_images':Ai,
        'geometric_push_images':A,'based_pullback_images':Ai})
    rows.append(row)
    print('PASS corrected old-base push and pullback',row['index'],row['name'],flush=True)
D.update({'loops':rows,'based_transport_provenance':provenance,
 'images_convention':'images = geometric push; inverse_images = based pullback',
 'actual_based_section':'Initial projected outer-real whisker 10 to 10^6, constant projected point 10^6 around the loop, inverse initial whisker.'})
write('symmetric_old_base_words_pullback_corrected.json',D)

D=read('symmetric_source_bridge.json');W=D['nodal_base_to_pairing_base_braid']
T=back(W);Ti=push(W);inverse_check(T,Ti)
D.update({'endpoint_generators_in_nodal_base':T,
    'nodal_generators_in_endpoint_base':Ti,
    'automorphism_transport_convention':'F_nodal = back(W) compose F_endpoint compose push(W)',
    'based_transport_provenance':provenance})
fixed_path=ROOT.parent/'work_DE/next_marginal_source/symmetric_fixed_basis.json'
fixed=json.loads(fixed_path.read_text())
Fend={int(i):tuple(w) for i,w in fixed['involution_images'].items()}
Fstart=compose(T,compose(Fend,Ti))
for i in range(1,22): assert B.sub(Fstart[i],Fstart)==(i,)
D.update({'nodal_involution_images':Fstart,'fixed_basis_sha256':sha(fixed_path)})
write('symmetric_source_bridge_pullback_corrected.json',D)
write('convention_status.json',{
 'status':'Chronological push/pull correction reconstructed and independently geometrically calibrated',
 'valid':'Original raw crossing paths, interval and deformation certificates, local types, linking/discriminant data',
 'superseded':'Original based whisker/bridge/action arrays and Fox columns; preserved untouched in pre_pullback_convention/',
 'correction':provenance,
 'node_output':'symmetric_node_words_pullback_corrected.json',
 'old_output':'symmetric_old_base_words_pullback_corrected.json',
 'bridge_output':'symmetric_source_bridge_pullback_corrected.json',
 'full_relation_module_computed':False,
})
print('PASS all18 local transports, all6 old actions, corrected actual source bridge and F square; elapsed',round(time.monotonic()-started,3),flush=True)
