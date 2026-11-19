#!/usr/bin/env python3
"""Record actual root mathematical checks and separately attributed background.

No inherited sweep event is relabelled as a new proof. No visual transcription
or ordinary source reading is recorded as an independent proof.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
WHO='GPT-6 Astra Pro; effort setting not exposed; run SP33_CW_156-5; root'
notes=json.loads((ROOT/'records/research_notes.json').read_text())['notes']
proofmeta=json.loads((ROOT/'records/mathematical_proofs.json').read_text())
proof_time=proofmeta['recorded_utc'];review_time=proofmeta['reviewed_and_extended_utc']
rows=[]
def event(id,typ,outcome,date=now,who=WHO):
    rows.append([id,date,who,typ,outcome])
proofs={
 'P00':('targeted proof check','The explicit support-based model and strict-boundary/weak-union conventions were checked against elementary examples. Literal ambient-point equivalence and a globally weak boundary fail. Refined statement P01-SUPPORT; no transcription emendation.'),
 'P01':('independent re-proof','Proved least-member iff alpha+beta iff gamma+delta+eta iff gamma+delta-prime on the support, with stated inclusion conventions; eta is genuinely used in the last implication.'),
 'P02':('independent re-proof','Proved artinian beta and artinian gamma=>eta; explicitly calculated an infinite gamma+delta/not-eta family. Does not identify it with unavailable GF VIII pages44-45.'),
 'P03':('independent re-proof','Proved admissible-family/poset-surjection equivalence and arbitrary nonprincipal-downset additions; proved complete irreducibility=principal and gave an infinite counterexample to ordinary irreducibility=principal.'),
 'P04':('independent re-proof','Proved locally closed=order convex and finite Boolean-generated=saturated; singleton family on N refutes the unrestricted Boolean-generated claim.'),
 'P05':('independent re-proof','Proved subfigure/induced-partition criterion, all compatibility formulations a,a-prime,b,c,d, unchanged strata, compatible support rigidity, bounded and pairwise-compatible unions, and C1-C3. Saturation already follows from raw subfamily inclusion.'),
 'P06':('independent re-proof','Proved {L} isolated for all nonempty L and incompatible cross-component point figure for |L|>=2; connectedness and C4 refuted. Proved exact n+2 finite component classification for n>=3, with n=1,2 separately.'),
 'P07':('targeted proof check','Separated literal product ranges from ranges enlarged by empty choices; literal product may be admissible but fails factor inclusion and the displayed boundary/stratum formulas, whereas enlarged mixed members have empty stratum. Natural flattened scan013 bridge also fails.'),
 'P08':('independent re-proof','Proved supports=P(L), elementary atom recovery, reconstruction from closed compatible multistrates, and conditional clopen/regular-open support identities; ordinary Stone representation remains background.'),
 'P09':('independent re-proof','Proved density/incidence equivalence for closed members, stability of member-local restrictions, finite-union local finiteness and explicit infinite-union failure; clarified finite principal-multistrate interpretation.'),
 'P10':('independent re-proof','Constructed finite-poset closed pieces |N(down i)| and downset correspondence; tripod refutes an automatic regular-ball interpretation. No register exit theorem re-proved.'),
 'P11':('independent re-proof','Proved least-container/closed-intersection, monotone stratum, marginal-lemma, preorder-preservation and continuity formulations equivalent; proved refinement order laws and local principal-multistrate test.'),
 'P12':('independent re-proof','Proved arbitrary compatible unions of refinements and maximal-refinement iff full support, including marginal c,d with their hypotheses. Literal minimality fails; refined statement P12-MAXIMAL.'),
 'P13':('independent re-proof','Proved square/refinement correspondence and saturated inverse-image property; raw family inclusion and unconditional closed direct image have explicit counterexamples. Infinite singleton/parity example refutes unrestricted finite-Boolean inverse-image preservation; refined statement P13-SATURATED.')
}
for pid,(typ,outcome) in proofs.items():event(pid,typ,outcome,review_time if pid in ['P05','P08','P11','P13'] else proof_time)

refutations={
 'N002-1':('P01-SUPPORT','Ambient-point condition as literally written is not equivalent to the support conditions.'),
 'N002-2':('P00-INCLUSION-CONVENTIONS','No single strict/weak convention works for every displayed inclusion; boundary and union conventions must be distinguished.'),
 'N003-2':('P01-THREE-CONDITIONS','Gamma+delta alone does not prove leastness in general; eta is used.'),
 'N004-2':('P02-ARTINIAN','The withdrawn finite gamma+delta/not-eta counterexample cannot work; the general nonredundancy claim survives.'),
 'N005-2':('P03-ARBITRARY-ADDITIONS','A general finite restriction on redundant members is false; the uncertain ink is not settled mathematically.'),
 'N005-3':('P03-COMPLETE-IRREDUCIBILITY','Ordinary irreducible closed need not be principal on an infinite poset; complete irreducibility is the refined claim.'),
 'N006-2':('P04-FINITE-BOOLEAN','The unrestricted infinite Boolean-generated=saturated extension fails; the finite insertion is essential.'),
 'N010-1':('P05-COMPATIBILITY','Equal support and equal partition alone do not imply compatibility.'),
 'N013-1':('P06-EXTRA-POINT-BRIDGE','The natural flattened proposed bridge has empty top stratum; literal extra braces remain untouched.'),
 'N014-1':('P06-COMPONENTS','Connectedness fails for |L|>=2; exact finite classification supplied.'),
 'N014-2':('P06-ISOLATED-OBSTRUCTION','C4 fails already on two points and by the isolated-node argument on every |L|>=2.'),
 'N015-1':('P07-LITERAL-VS-ENLARGED','Literal product need not be inadmissible, but does not contain its factors as claimed.'),
 'N015-2':('P07-LITERAL-VS-ENLARGED','With empty choices adjoined, mixed members have empty stratum, so the intended bounding product fails.'),
 'N015-3':('P07-CORRECT-BOUNDARIES','The written boundary and stratum identities fail on explicit literal-range examples.'),
 'N019-2':('P09-PRINCIPAL-FINITENESS','Underlying subset cardinality does not characterize a finite figure; finite principal multistrates give the valid criterion.'),
 'N019-4':('P10-CLOSED-PIECES','Regular closed-ball meaning is not forced by the finite-poset construction; tripod example.'),
 'N023-3':('P12-MAXIMAL','Literal minimality is false; full support characterizes maximality under subfigure extension.'),
 'N024-2':('P12-EXTENSION-DIRECTION','Initial reversed subfigure direction is inconsistent with the displayed support chain and the proved maximality criterion.'),
 'N025-2':('P13-GENERAL-REFINEMENT-SQUARE','The square does not impose raw family inclusion.'),
 'N025-3':('P13-SATURATED','Unrestricted finite-Boolean constructibility interpretation fails in the infinite parity example; saturated and finite-figure versions hold.'),
 'N025-4':('P13-CONTINUOUS-NOT-CLOSED','Unconditional closed-image extension fails; the unfinished manuscript sentence is not asserted to make that false claim.')
}
for n in notes:
    if n['id'] in refutations:
        refined,why=refutations[n['id']]
        event(n['id'],"refuted, with the refined statement's id",f'Refined statement id {refined}. {why} Written check {n["proof"]}; manuscript place156-5/{n["scan"]:03d}, {n["place"]}.')
    elif n['proof']:
        event(n['id'],'used and rechecked in this run',f'The precisely qualified claim is used after the root proof review in {n["proof"]}; see the numbered proof and note for hypotheses. Manuscript place156-5/{n["scan"]:03d}, {n["place"]}. Reading questions do not amend frozen text.')
    else:
        event(n['id'],'carried as background without fault found',f'Documentary/contextual comparison or unproved lead, not a new mathematical proof: {n["kind"]},156-5/{n["scan"]:03d}, {n["place"]}. Context relation reviewed and limits stated in note; no register status upgraded.')

# Actual computation execution records, not their later integration timestamps.
a=json.loads((ROOT/'records/finite_figures_check.json').read_text())
b=json.loads((ROOT/'records/finite_figures_n4_components.json').read_text())
assert hashlib.sha256((ROOT/'scripts/finite_figures_check.py').read_bytes()).hexdigest()==a['provenance']['script_sha256']
assert hashlib.sha256((ROOT/'scripts/finite_figures_n4_components.py').read_bytes()).hexdigest()==b['script_sha256']
CWHO='GPT-6 Astra Pro; effort setting not exposed; run SP33_CW_156-5; ancillary independent computation from root definitions, root-reviewed'
compdate=a['provenance']['executed_finished_utc']
event('COMP-FAMILIES-1-3','computation or formal certificate','All4,16,256 subset-families enumerated from scratch for n=1,2,3; admissible counts2,7,45 including empty family. Full catalogue and source hash retained.',compdate,CWHO)
event('N013-3; N014-1; N014-2','computation or formal certificate','n=1,2,3 multistrates1,5,28; components1,3,5 with sizes1 /2,2,1 /21,2,2,2,1. Incompatible ordered cross-component pairs0,14,324; complete memberships and pairs retained.',compdate,CWHO)
event('P11; N020-2; N023-2','computation or formal certificate','Refinement a/b agree for all4+49+2025 admissible ordered pairs;3,26,549 true pairs. Order laws hold;4,70,3601 composable chains checked. Finite scope only.',compdate,CWHO)
event('P12; N024-1','computation or formal certificate','All54 admissible target figures for n=1,2,3: full-support refinements equal maximal refinements under subfigure order. Actual relation tables retained.',compdate,CWHO)
event('N013-3; P06-FINITE-CLASSIFICATION','computation or formal certificate','Focused n=4 run:65,536 families;500 admissible;231 multistrates; six components222,2,2,2,2,1. Exact predicted component partition agrees. No n=4 refinement/compatibility-pair claims.',b['executed_finished_utc'],CWHO)
event('COMP-CODE-REVIEW','targeted proof check','Root reviewed least (not just minimal) implementation, boundary exclusion, down-closed subfamily, two refinement criteria, exhaustive pair/chain loops and component traversal; original script hashes match execution records. No source implementation or sweep code was consulted.',now)

# Every used register id is carried under its own id. Underlying full proofs were
# not supplied; their abbreviated status is never recast as this run's proof.
extra_ids=['MPL_150_001-043 Q4b','MPL_151_032-075 Q4-02','MPL_151_032-075 Q4-03','MPL_121_049-073+153+155 R121-08','WG2 §3.1 #2','LM4 C.12','RESIDUE E.6','EXIT_ONE_TYPE P3c-general','PATHS C.10','RESIDUE C.8','RESIDUE F.6','RESIDUE I.7','RESIDUE J.2','RESIDUE J.3']
ids=sorted(set(extra_ids+[i for n in notes for i in n['results_ids']]))
rs=(ROOT.parent/'source/SP33_CW_156-5_context/notes/RESULTS_STATE.md').read_text()
for id in ids:
    line=next((line for line in rs.splitlines() if f'**{id}**' in line),None)
    assert line, f'Unknown register id {id}'
    status=line.split('**',2)[2].split(']',1)[0].strip()+' ]'
    uses=[n['id'] for n in notes if id in n['results_ids']]
    event(id,'carried as background without fault found',f'Supplied RS status {status}; row read, not its underlying full proof. '+('Compared in '+', '.join(uses)+'. ' if uses else 'Used only in programme-scope section. ')+'No proof/referee status upgraded; open items remain open. Source SP33_CW_156-5_context/notes/RESULTS_STATE.md.')
for id in ['S14','B10']:
    event('PLAN-'+id,'carried as background without fault found',f'Unchecked planning guess from MPL_156-5/README.md. Scans002-025 supply elementary models/refinements only; no pro-object reconstruction or tame/PL equivalence is proved. See programme-scope table.')
for id,pid in [('SA21-R5-01','P01'),('SA21-R5-02','P02'),('SA21-R5-03','P02'),('SA21-R5-04','P03;P04'),('SA21-R5-05','P05'),('SA21-R5-06','P05'),('SA21-R5-07','P05'),('SA21-R5-08','P06;P07'),('SA21-R5-09','P08'),('SA21-R5-10','P11'),('SA21-R5-11','P12')]:
    event('S-COMPARISON-'+id,'used and rechecked in this run',f'Compared the earlier event with this run\'s written check {pid}; earlier timestamps and computation are not inherited. Qualifications in notes include support normalization, strong irreducibility, literal/enlarged product, and maximality where applicable.')
event('BACKGROUND-STRATA-STONE','carried as background without fault found','Ordinary Stone representation and general categorical/geometric background are used only as attributed background; elementary atom recovery and conditional regular-open calculation were proved separately in P08. No external literature theorem independently certified.')
event('BACKGROUND-E119','carried as background without fault found','Supplied unchecked API transcription, scans119/27-41 and119/57-59: stratified reconstruction, attachments, tame axioms, choice contractibility, and compact comparison read as context. Not image-verified or treated as proof of register claims.')
event('BACKGROUND-STUDY-OUTSIDE','carried as background without fault found','STUDY comparisons with156-4,156-6,156-7 and S5 later scans are contextual leads only. No visual or independent proof check of outside-scope statements, including S correction scans026/049 or SA21-R5-12--16, is claimed.')
with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(rows)
(ROOT/'records/check_event_summary.json').write_text(json.dumps({'written_utc':now,'events':len(rows),'types':{t:sum(r[3]==t for r in rows) for t in sorted(set(r[3] for r in rows))},'register_ids':ids,'mathematical_proof_source_sha256':proofmeta['source_sha256']},ensure_ascii=False,indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:f.write(f'check-event ledger written {now}; {len(rows)} actual-check/background events; no inherited proof status promoted\n')
print(json.dumps({'events':len(rows),'register_ids':len(ids),'written_utc':now}))
