"""Bind the thirteen current operational sources and exact review scopes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

root=Path(__file__).resolve().parents[1]
expected={
 'code/package_checkpoint.py':'dc1684913e6b9061aded4dbdb378e1cbe89a977a0cff6e9ad50f16829509fbb2',
 'code/checkpoint_data_tar.py':'9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb',
 'code/preserve_checkpoint35_versions_inductive.py':'5f2203fe56aedf3237b3671f1cfb498ce724574f2819d9e4ff0a9b2c4d2a3f33',
 'code/verify_checkpoint35_inductive_retention.py':'b6ae3f0d76d78c33454c171a1d1b006b2e3b4b3155ce3e9110307455bf9273cb',
 'code/build_checkpoint35_parent_anchor.py':'63755c5b2bdab1bc9527c9c2b31b3f7ac36773785d5e4716c9a288c422d6442b',
 'code/estimate_checkpoint35_size.py':'b03dc9f2ac77c08bfc9ecc0f3bcc7ff0bdcedcc398b512262508815e46e04815',
 'code/verify_checkpoint35_system_tars.py':'6fb98bfd7824e0145d2186d37fafb942b3294c6d23600e94cbf7fb2e91f366cd',
 'code/check_checkpoint35_preconditions.py':'c9ec7a6b0a81daa64ac86a84c2173d41d648bbb8f16ee40caf3b5c11fe6ee4c2',
 'code/capture_checkpoint35.py':'533bf2a30a06444128e07bd23e6d60e468fac8281c76d86c015d36d8bf3a499f',
 'code/render_checkpoint35_pdf.py':'f899d7e720deaf46bdb0da1ddde16e2be22049d5c5ee0bf214da8c3b0980d128',
 'code/audit_checkpoint35_final_pdf.py':'f71f763df7aef78dacd3eb362636d04189399092eee585a1362da73761ecb887',
 'code/finalize_checkpoint35_visual_record.py':'0489387197f0c04187ed90cca4a93fb02779385f0e81c3a73dd8e698f2e78bc4',
 'code/publish_checkpoint35_readiness.py':'e54dfcd869ef7e70c58a586e6e767059db6ea15de8fb90dfbcca6dbd0bcf8638',
}
pairs=[('work_A/review_checkpoint35_operational_helpers','md'),
 ('work_A/review_checkpoint35_capture_readiness_helpers','md'),
 ('work_DE/review_document_dictionary_measurement35','md'),
 ('work_CE/review_checkpoint35_render_audit_sources','txt'),
 ('work_CE/review_checkpoint35_visual_finalizer','txt')]
def bound(rel):
    p=root/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
sources=[bound(p) for p in expected]
for row in sources:assert row['sha256']==expected[row['path']],row['path']
reviews=[bound(base+'.'+ext) for base,kind in pairs for ext in (kind,'json')]
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),result='PASS_COMPLETE_SOURCE_REVIEW',reviewer='/root',
 sources=sources,independent_reviews=reviews,
 scope='Root read all current operational source bodies, or the complete unchanged predecessor plus its entire precise adaptation. Root read every complete listed independent review and JSON. The package change is only the independently reviewed document-dictionary difference; the shared compressor body was also freshly read in full. All thirteen exact current hashes are bound. This is source review, not an assertion that the capture or any future verifier ran.',
 runtime_scope='Actual parent-anchor completion, document-dictionary measurement/installation, final build/metrics/render/log audit/visual record, final size estimate and eventual writer pauses have separate evidence. No ZIP is created by this recorder.',
 storage_configuration=dict(images_dictionary_bytes=67108864,documents_dictionary_bytes=67108864,data_dictionary_bytes=67108864,
    cap_bytes=536870912,scheduled_capture='2026-11-17T13:49:30+00:00',next_slot='2026-11-17T14:49:30+00:00'),
 retained_scope='All predecessor sources and failed35 build artifacts remain preserved. Current formal source bindings include both exact line-break corrections. Minor citation spacing remains explicitly recorded for the next typesetting pass.')
with (root/'records/checkpoint35_operational_source_review.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print('Bound13 current operational sources and10 complete independent review records; no archive created.')
