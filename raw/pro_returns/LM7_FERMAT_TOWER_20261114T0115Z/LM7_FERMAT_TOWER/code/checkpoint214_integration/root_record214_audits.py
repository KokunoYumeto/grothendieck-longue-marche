"""Record the root's completed proof/program reviews and their actual replay evidence."""
from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2,ensure_ascii=False)+'\n'
specs=[
('E.111','research_e111','E_nonunit_seventeen.tex','6123d12fe7403acc23b0e970447f71b78ccdb019abeb1484d387de9d392cf5d2',
 ['Both local character matrices and their explicit inverse columns; common-root norm/corestriction at every height.',
  'Actual Hilbert90 S-capitulation and invariant-class sequences, finite S-unit Herbrand quotient27, and all-level zero S-class induction.',
  'Restricted divisor norm limit, compact fibre inverse, Kato one-three-place projection and countably infinite unit dual basis.',
  'All nonzero multiples of kappa3(17), both positional decompositions, pure-factor compensation and actual toric inverse.'],
 'a_e111_audit/audit.json'),
('E.113','research_e113','E_quartic_compact_cups.tex','3c20ef8d4f8a4afa987cc5b1a67dcd60eeb594f340b0e725d1bdf347a1ee2f16',
 ['Bad-two odd-torsion exclusion, finite local duality, all good-prime inertia maps and the actual real two-primary transition.',
  'Global Brauer reciprocity and compatible primitive alignment using the surjective Kummer H1 transitions.',
  'Six determinant and three CM Tate coefficient maps; full nonlinear gauge, filling and central-shift signs.',
  'Every projected arithmetic off-diagonal cocycle is retained; all nine Tate obstruction coordinates have explicit primitives.'],
 'bc_e113_audit/audit.json'),
('E.114','research_e114','E_inert_prime_tail.tex','328fdc236fdd56dc50d224f14d5c25418875ec355e510e88dc33df7bffcc5008',
 ['Exact cyclotomic and vertical local degrees; completed principal prime generators from prime-to-three class powers.',
  'Regular prime orbit, augmentation-zero character and both group-ring inverse products.',
  'Higher3-power characters with their actual roots and norm-projection formula; all S-class and unit-norm maps.',
  'Restricted coherent divisor splitting, compact character inverse and exact lower-factor norm coupling; explicit Chebotarev class.'],
 None),
('D.60','D60_EXPERIMENTS','D_stabilizer_projective_lift.tex','e96647a11389f65cfc4d8ebd7e304181b9aba93387b98d7d9c60f2c586fdc126',
 ['Both actual marked quotient maps and kernels; odd-kernel homology comparison and literal twisted edge/cusp modules.',
  'All four Hermitian kernels and norm maps, including the actual compact norm kernel.',
  'Semilinear projectivity, full integral idempotent and affine-section lifting, exact small-image removal.',
  'Projective-cover lift of the retained D57 homology action; cyclic2/3/36-to12 comparisons and actual cusp-fixed derivation.',
  'Twelve full norm injections, unquotiented orientation transfer, actual central conjugator corrections and exact remaining source kernels.'],
 None)]
for ident,folder,section,digest,checks,peer in specs:
 source=R/folder/'sections'/section;assert sha(source)==digest
 target=R/('root_'+ident.lower().replace('.','')+'_audit');target.mkdir(exist_ok=True)
 record=dict(statement=ident,status='PASS',reviewer='/root',reviewed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 proof_sha256=digest,proof_lines_read=len(source.read_text().splitlines()),full_proof_read=True,
 full_mathematical_program_sources_read=True,mathematical_review=checks,
 mathematical_corrections=[],method='Full proof and program inspection; exact execution comparisons are separate evidence, not a substitute for the all-level proofs.')
 if peer:
  p=R/peer;q=json.loads(p.read_text());assert q.get('status',q.get('result'))=='PASS'
  record['received_independent_review']=dict(path=peer,sha256=sha(p),scope=q['scope'])
 if ident=='E.111':
  record['root_fresh_program_replay']=False
  record['actual_fresh_replay']='The received full independent a_structure audit includes a complete fresh GP/Python rebuild, full text equality, entire deserialized five-component PARI equality and independent arithmetic checks. Root does not claim an additional replay.'
  record['source_review']='The exact Kato, Milne and Lemmermeyer applications were checked in the already retained root E110 source review and the independent E111 primary-source audit. No new source-read claim is added here.'
  record['presentation_amendment']='Leading literal commas in exponent braces will be removed by a separately recorded author-requested presentation integration.'
 else:
  rp=target/('verification.json' if ident=='D.60' else 'replay_result.json')
  replay=json.loads(rp.read_text());assert replay['status']=='PASS'
  record['root_fresh_program_replay']=True
  record['execution_evidence']=dict(path=str(rp.relative_to(R)),sha256=sha(rp),scope=replay.get('method',replay.get('scope')))
 if ident=='E.113':
  record['source_review']='Author primary-source evidence records the exact local-duality/Euler and Brauer proofs. Root checked their use in the full proof and retained the independently checked cochain signs; the corroborating Cremona source was not newly re-opened by root.'
 if ident=='E.114':
  bp=target/'compare_binary.out'
  b=[json.loads(x) for x in bp.read_text().splitlines() if x.startswith('{')]
  assert len(b)==1 and b[0]['full_GEN_equal']==1 and b[0]['component_count']==4 and b[0]['component_equal']==[1]*4 and b[0]['base_component_equal']==[1]*5
  p=R/folder/'code/e_inert_tail_orbit.bin';q=target/'replay/code/e_inert_tail_orbit.bin'
  record['binary_comparison']=dict(actual_compare_exit_code=0,source_sha256=sha(p),replay_sha256=sha(q),
   raw_byte_equal=p.read_bytes()==q.read_bytes(),full_deserialized_exact_identity=True,all_four_components_identical=True,
   all_five_embedded_base_components_identical=True,compare_output_sha256=sha(bp))
  record['source_review']='The same proved Milne norm/cup, S-unit Herbrand, Hasse norm and Chebotarev maps, Lemmermeyer ideal sequence and Kato one-prime norm projection are used with their stated data. Existing original-source evidence is retained; no inaccessible Ihara/Coleman proof is upgraded.'
 if ident=='D.60':
  record['actual_programs_read']=4
  record['proof_transfer_limit']='The D59 homology representative changes on exactly the two stated orbits. The unchanged D57 and W_h projections are retained. The353792-dimensional residual with612 coinvariants and the full profinite realization remain unevaluated.'
 (target/'audit.json').write_text(enc(record))
 prose='# Root proof and computation review: '+ident+'\n\nVerdict: PASS on the exact proof SHA256 '+digest+'.\n\n'
 prose+='The entire proof and all its mathematical program sources were read. The review checked:\n\n'+'\n'.join('- '+c for c in checks)+'\n\n'
 prose+='No mathematical correction was requested. Execution and primary-source review scopes, including every limitation, are recorded in audit.json. The original unrestricted task remains active wherever this statement retains a kernel or lower norm system.\n'
 (target/'audit.md').write_text(prose)
 print(enc(dict(statement=ident,status='PASS',proof_lines=record['proof_lines_read'],audit_sha256=sha(target/'audit.json'))),end='')

