"""Preserve first saved outage texts, genuine JS output and late scoped research bindings."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
metadata=json.loads((root/'records/environment_recovery32/recovered_conversation_metadata.json').read_text())
original=metadata['values']['checkpoint32_outage_source_manifest']
entries=[]
for item in original['entries']:
    rel=item['planned_path'];data=(root/rel).read_bytes()
    entries.append({'memory_key':item['key'],'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'filesystem_materialized':True})
for rel in ['work_A/actual_affine_pentagon_signed_hexagon32_recovered.md','work_A/actual_all_congruence_hexagon32_root.md','work_A/outage32_abelian_noncentral_centralizers_extension.md']:
    data=(root/rel).read_bytes();entries.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'filesystem_materialized':True})
out=root/'code/outage32_square_normal_CM_witness_genuine_tool_result.json'
assert not out.exists()
out.write_text(json.dumps({'execution_kind':'Genuine pure JavaScript functions execution during outage; not an OS process','historical_execution_time':'2026-11-17 09:01:27 UTC','os_exit_code':None,'original_tool_result':metadata['values']['checkpoint32_square_normal_CM_witness_output'],'scope':'Original result preserved; no replay or canonical-realization assertion.'},indent=2)+'\n')
reviews=['work_A/recovery32_conversation_review_receipts.md','work_DE/review_actual_affine_pentagon_recovered32.md','work_CE/review_affine_pentagon_signed_hexagon_recovered32.txt']
record={'recorded_at':datetime.now(timezone.utc).isoformat(),'source_entries':entries,'genuine_JS_result':{'path':str(out.relative_to(root)),'sha256':sha(str(out.relative_to(root)))},'source_review_records':{p:sha(p) for p in reviews},'formal_promotion':False,'formal_statement_count':347,'scope':'Seventeen complete outage source/program texts materialized, plus the saved uniform affine theorem, its all-congruence strengthening, and the previously proved abstract centralizer extension. Original conversation-only headers remain historical text; this record supplies actual materialization status.','all_congruence_audit':'Root derivation and complete independent CE/DE conversation-only symbolic audits PASS; no tools or mathematical execution by either reviewer. Saved source is a fresh first text, not an old byte hash.','supersessions':['The saved uniform affine theorem settles the actual full-GT signed mod3/mod12 hexagon image formerly left open in the earlier signed-phase sources.','The new integral order-three conjugator strengthens that to every signed congruence quotient.','The complete-dihedral correction withdraws the earlier isolated finite D6 nonzero-phi branch.','The correct filled cohomology gate is equality with the whole contact connecting image; injectivity is refuted by the actual D-contact class.','Only the canonical even-power CRT lift was proved to have cube1; an arbitrary opposite lift need not.'],'main_A':'Open','main_B':'Open','actual_CM_parity':'Open'}
p=root/'records/checkpoint32_late_proof_bindings.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n')
addendum='\n## Late complete congruence strengthening at checkpoint32\n\nThe new complete source work_A/actual_all_congruence_hexagon32_root.md proves that the actual ordered hexagon vanishes in EVERY signed congruence quotient SL2(Z/m), equivalently in the full specified image in SL2(Zhat). It uses the integral order-three J=[[0,-1],[1,-1]], the exact ordered cube (U X^k J^-1)^3, symmetry of U and the already proved d U11=1. Its trace is exactly-1 and determinant1, so Cayley–Hamilton proves the cube is1 over every modulus without division. Root and two independent conversation-only audits checked all steps. This strengthens the earlier mod3/mod12 research conclusion; it is unpromoted research in this capture, with the reviewed611-page formal paper unchanged. The full-word/congruence-kernel distinction and the separately normalized CM-frame comparison remain Open. The previously derived direct-target theorem for abelian noncentral-element centralizers is now also materialized in full.\n'
for rel in ['records/thirty_second_hour_research_report.md','LM4_SUCCESSOR_report.md']:
    p=root/rel
    backup=root/'records/environment_recovery32/before_all_congruence_addendum'/rel
    backup.parent.mkdir(parents=True,exist_ok=True);assert not backup.exists();backup.write_bytes(p.read_bytes())
    p.write_text(p.read_text()+addendum)
print('Preserved',len(entries),'complete late source/program texts and genuine JS tool result; full congruence strengthening separately scoped.',flush=True)
