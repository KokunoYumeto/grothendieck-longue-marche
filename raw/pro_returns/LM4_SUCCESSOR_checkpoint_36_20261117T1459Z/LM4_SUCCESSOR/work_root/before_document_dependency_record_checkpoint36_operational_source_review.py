"""Bind exact current reviewed operational sources; no execution claim."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--additional-reviews',nargs='+',required=True);args=parser.parse_args()
expected={
 'code/package_checkpoint.py':'7c753ea7355dcb2dc511ee31f6e3814121784835fe987fb0cd2df37cf3abb447',
 'code/checkpoint_data_tar.py':'9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb',
 'code/checkpoint_image_tar.py':'e6019666bfc8486f3de4355c4f78dd297532e3c764114a450be1fcd4d43fb885',
 'code/checkpoint_document_tar.py':'c5b791f3906be7bd74d471076560c75d52833eb6d76a02ec171e5e5eb9dc4025',
 'code/preserve_checkpoint36_versions_inductive.py':'5f20c6b1d8a5c3345556228525b0e581dfd034805b9fb840bba6026e03fabd14',
 'code/verify_checkpoint36_inductive_retention.py':'54182640fbdbb9c7f7121e39b6efd69dc3b5a3dd646b6f975d62131b1b68b6e8',
 'code/build_checkpoint36_parent_anchor.py':'324e2b6fbcea54162a30900cf8a424802c3a54de38fd88eed9d8ef7e7a5d5d42',
 'code/estimate_checkpoint36_size.py':'293e093f5d0cdc7ed8d841182b2c33e09f0c38bde414724891ea7a3d50bc0e47',
 'code/verify_checkpoint36_system_tars.py':'7f88c4a0c2c02f3eff1de787aae63bbd93ae3879cf47ab2d0ec7aa2bdcbf9a37',
 'code/check_checkpoint36_preconditions.py':'56aab1c260f7949dd94a98a8862d8411210d1b77666ae8b7fbd1605ae8bd1374',
 'code/capture_checkpoint36.py':'942e5923e0841dd6ab15c02f48e1eb94ee9937b66c043c5e9044adc74f4096d4',
 'code/render_checkpoint36_pdf.py':'ea9aec4230cf73675106381cec1d21a4888f907f7c087d3da1a30fc4f5acfa7f',
 'code/audit_checkpoint36_final_pdf.py':'d387d06bb01545afd8d24160f10fa7df11e1b7ce9f32d6892bcb712781a91dea',
 'code/finalize_checkpoint36_visual_record.py':'2c5c4944412c7a2da425ef257c6b041b3966ad76c049a1ee04522a63fd285826',
 'code/publish_checkpoint36_readiness.py':'ddbf69d4fcf97b035c4e9c356d1a305cdffefc4d63645277beeeb71322ea20e3',
 'code/measure_checkpoint36_prospective_image256.py':'33fe2d1d463b774ff65032c5cd2924af8e036592ec76c44aaa5aa77107949197',
 'code/measure_checkpoint36_prospective_document128.py':'f063ce24764aa7e077757ecdffc81f784a5c4aa010b98e671dfbe32c6312c9f9',
 'code/combine_checkpoint36_dual_dictionary_size_evidence.py':'1eaf88134fef27eec2675c5ed1cce8595094a1256da8fbf68ab4ceee410f9d06',
}
def bound(rel):
    p=root/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
sources=[bound(p) for p in expected]
for row in sources:assert row['sha256']==expected[row['path']],row['path']
bases=['work_A/review_checkpoint36_retention_helpers','work_DE/review_checkpoint36_image_packaging',
 'work_A/review_checkpoint36_size_estimator','work_A/review_checkpoint36_capture_helpers',
 'work_A/review_checkpoint36_prospective_image256','work_A/review_checkpoint36_image256_policy_and_combiner',
 'work_A/review_checkpoint36_prospective_document128']
paths=[base+'.'+ext for base in bases for ext in ('md','json')]+args.additional_reviews
assert len(paths)==len(set(paths))
reviews=[bound(p) for p in paths]
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),result='PASS_COMPLETE_SOURCE_REVIEW',reviewer='/root',
 sources=sources,independent_reviews=reviews,
 scope='Root read every current operational source body, or its entire previously read unchanged predecessor plus every exact adaptation. Root authored the complete final accounting source and read all listed complete independent reviews. The exact18current hashes include the canonical final publisher, both measured candidate sources, independent document helper and combined accounting. This is source review; capture and future verifier success are not inferred.',
 runtime_scope='Actual completed build/metrics/render/log audit/visual record, all compression candidates, their decoded identities, the final accounting and explicit pauses have separate observed receipts. All source-only alternatives and original failed estimate remain retained.',
 storage_configuration=dict(images_dictionary_bytes=268435456,documents_dictionary_bytes=134217728,data_dictionary_bytes=67108864,
   cap_bytes=536870912,unchanged_allowance_bytes=5000000,scheduled_capture='2026-11-17T14:49:30+00:00',next_slot='2026-11-17T15:49:30+00:00'),
 retained_scope='All previous canonical helpers and proposals survive. No paper, PNG or historical evidence is removed; the exact image/document stream identity was checked before and after each measurement and freshly at final accounting.')
with (root/'records/checkpoint36_operational_source_review.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(f'Bound{len(sources)}exact current operational sources and{len(reviews)}complete independent review files; no archive created.')
