"""Append final actual QA and measured accounting without changing prior prose."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
estimate=json.loads((root/'records/checkpoint36_size_estimate.json').read_text())
assert estimate['estimated_total_with_allowance']<536870912
assert estimate['header_manifest_retention_late_text_allowance_bytes']==5000000
visual=json.loads((root/'records/checkpoint36_visual_review.json').read_text())
assert visual['visual_review']=='PASS'
report=root/'LM4_SUCCESSOR_report.md';old=report.read_bytes()
assert old.splitlines()[0]==b'INCOMPLETE'
preserved=root/'records/checkpoint36_before_qa_append/LM4_SUCCESSOR_report.md'
preserved.parent.mkdir(exist_ok=False)
with preserved.open('xb') as stream:stream.write(old)
text='''\n## Checkpoint36 final typesetting and actual size evidence\n\nThe final695-page PDF contains383statements (339Proved,19Refuted,19Open,6Known),117references and49task rows. MainA, MainB and actual CM parity remain Open. Overflow counts: before36integration0; first36build0; final0. The build succeeded on its first36attempt. Final engine log and stabilized stdout have no warnings, unresolved references or errors.\n\nEvery new mathematical page was individually inspected:27pages, plus4mandatory legacy editorial pages, giving30distinct required pages. In total36individual pages were inspected,51pages rendered and6contact sheets opened separately. There are23underfull notices in each final log,19inherited and4new. Three concern the wrapped A120provenance paths on page215; one concerns B170inline-formula spacing on page600. Both pages were inspected individually and their content is legible without clipping. The exact notices and all page-specific observations remain in the visual receipts. The corrected A119andE52citation spacing and the added bibliography entry were also individually checked.\n\nThe initial complete128MiB image estimate exited1 only at its final cap assertion. Its complete genuine report/stdout/stderr and all22predicted historical rows are preserved under records/checkpoint36_first_size_estimate. No failed build is attributed to that failure. The separate256MiB image measurement used exactly the same606720000-byte standard TAR and independently decoded every byte, with matching SHA256andCRC, decoderEOF and no unused tail. Its actual payload430320787saved7682657bytes, which alone still left629676bytes above the cap including the unchanged5MBallowance. The final accounting below uses only completed actual component measurements with exact input identities and retains every original payload and evidence file.\n\n'''
text+='| Component | Dictionary bytes | Actual compressed bytes | TAR bytes |\n|---|---:|---:|---:|\n'
for kind,row in estimate['prospective_bundles'].items():
    text+=f'| {kind} | {row["dictionary_bytes"]} | {row["compressed_bytes"]} | {row["metrics"]["bundle_bytes"]} |\n'
text+=f'\nFinal conservative total before allowance:{estimate["estimated_before_allowance"]}bytes. The unchanged allowance is5000000bytes. Total including allowance:{estimate["estimated_total_with_allowance"]}bytes; cap536870912bytes; remaining estimated headroom:{estimate["estimated_headroom_bytes"]}bytes. The actual immutable archive size remains authoritative. No test or duplicate ZIP is used.\n\n'
text+='The exact standard mixed-reflection control and its prescribed D8certificate have now received two complete independent reviews. It proves the whole pointed derived-cohomology space for that standard action, not the value of the actual general GT-involution/CM class. The current main research continues with the whole Brunnian fiber and all original signed-node relations. Late notes retain their own proof/review boundaries and do not change the frozen383-statement formal edition.\n'
report.write_bytes(old+text.encode())
assert report.read_bytes().startswith(old)
audit=root/'records/checkpoint36_computation_audit_state.md'
with audit.open('a') as stream:
    stream.write('\n## Later completed accounting and proof reviews\n\n'+text.split('## Checkpoint36 final typesetting and actual size evidence\n\n',1)[1])
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),previous_report_sha256=hashlib.sha256(old).hexdigest(),
 preserved_previous_report=str(preserved.relative_to(root)),appended_bytes=len(text.encode()),
 new_report_sha256=hashlib.sha256(report.read_bytes()).hexdigest(),
 final_size_report_sha256=hashlib.sha256((root/'records/checkpoint36_size_estimate.json').read_bytes()).hexdigest())
with (root/'records/checkpoint36_final_report_append.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
