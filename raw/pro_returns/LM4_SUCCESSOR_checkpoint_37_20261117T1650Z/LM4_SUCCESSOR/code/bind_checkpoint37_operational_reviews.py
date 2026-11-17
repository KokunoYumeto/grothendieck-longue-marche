"""Bind complete current source reviews; this does not certify runtime results."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
 'code/package_checkpoint.py': '120ee05572f01704d6fb23557af5ed8afbdaa896ce84f859e14d7945e25cc931',
 'code/checkpoint_data_tar.py': '9e149cc79ca9790fc55a3147a4664c0886cbe1dc0b981727459a26bac35badbb',
 'code/checkpoint_image_tar.py': 'e6019666bfc8486f3de4355c4f78dd297532e3c764114a450be1fcd4d43fb885',
 'code/checkpoint_document_tar.py': 'c5b791f3906be7bd74d471076560c75d52833eb6d76a02ec171e5e5eb9dc4025',
 'code/checkpoint_image37_tar.py': '055fa383e1bacef045f2351df86fa4d50464956c8d6c1367d78c53cf7b7cd4b5',
 'code/checkpoint_document37_tar.py': 'e9d3e34a645bfa149b6eabe6ec26ca0e025907263be72f56e3a5467a5e0df3d3',
 'code/preserve_checkpoint37_versions_inductive.py': 'f3df65e316af567c2e50061d55fd42492f4daf25a1c0bf0682d9260673994b36',
 'code/verify_checkpoint37_inductive_retention.py': 'b2ec57ec2009cdf057bae9b9d56111c14864798112a3587a5c1e0d7a374ffcb1',
 'code/build_checkpoint37_parent_anchor.py': '8b679510c49182904db9bf2ecd169014420509bfc679ac2c11b4305ded9baef9',
 'code/estimate_checkpoint37_size.py': '6d001c5d77a7f8d18a7b00fb8906a1edc1b618f1783e6cc9883560418dc2b145',
 'code/verify_checkpoint37_system_tars.py': '1933548b27be9a27c5822cb75b3fdff4752496a023bb12cff6048d87af7891d2',
 'code/check_checkpoint37_preconditions.py': '012d63c1f595ad5af25ee0320af8c694415855967604824a36c3ebe1962962b2',
 'code/capture_checkpoint37.py': '3a13b6c369a19463d93587cbac2f86f8dcada677053fa5a7a3b796ea44abcc5d',
 'code/render_checkpoint37_pdf.py': '133248f910bd2283df583827a88e233bdb6145b5ff2276f640dde100de550c43',
 'code/audit_checkpoint37_final_pdf.py': 'c4b5d3295b634b682fffab6978c90feb4631df17cfda4f7b7790c399adb82317',
 'code/finalize_checkpoint37_visual_record.py': '1681c01a2384e15d014c77aa1913eefc05ed5117695af508cfcc0aeef80e3d23',
 'code/publish_checkpoint37_readiness.py': '4e46eae842176a53551d4a13da7dc5c3c4f046015a36f15b5bc477a566f9ad4b',
 'code/checkpoint_standard_tar.py': '8d3253e1fcdb406c94f7aa1ca3a2a2ffeb4ab59bd9c44ed54958b9d13de2e2df',
 'code/checkpoint_archive_io.py': 'e508fa3bae0cb845b5d02a0623aea6643a9981a7ade822fe87e7c539140e21e4',
}
REVIEWS = [
 'work_A/review_checkpoint37_retention_helpers.md',
 'work_A/review_checkpoint37_retention_helpers.json',
 'work_CE/review_checkpoint37_codec_packager.txt',
 'work_CE/review_checkpoint37_codec_packager.json',
 'work_A/review_checkpoint37_size_estimator.md',
 'work_A/review_checkpoint37_size_estimator.json',
 'work_A/review_checkpoint37_memory_roundtrip.md',
 'work_A/review_checkpoint37_memory_roundtrip.json',
 'work_DE/review_checkpoint37_five_helpers.md',
 'work_DE/review_checkpoint37_five_helpers.json',
 'work_A/review_checkpoint37_readiness_publisher.md',
 'work_A/review_checkpoint37_readiness_publisher.json',
]

def bind(rel):
    data = (ROOT/rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

sources = [bind(rel) for rel in EXPECTED]
for row in sources:
    assert row['sha256'] == EXPECTED[row['path']], row['path']
record = {
 'recorded_at': datetime.now(timezone.utc).isoformat(),
 'result': 'PASS_COMPLETE_SOURCE_REVIEW',
 'reviewer': '/root',
 'sources': sources,
 'independent_reviews': [bind(rel) for rel in REVIEWS],
 'root_source_read_chunks': ['8d311c', '6519b2', '681c94', '66e2c2', 'cd2456', '34d8e1', '1ac2c2', '3c508d', '635403'],
 'root_final_memory_diff_and_review_read': '3a14c3',
 'root_other_independent_review_reads': ['9dd975', '97503f', 'e7dd94', 'd767e9', '722ff2', '3ebba3', 'a69b57'],
 'scope': 'Root read the entire current source bodies or the complete unchanged predecessor and every exact adaptation. The final memory packager and estimator were both reread completely. The nineteen current bindings include the seventeen readiness helpers and their unchanged standard TAR/archive-reader dependencies. All listed complete independent reviews were read. This is source review only.',
 'runtime_scope': 'Actual build, metrics, renders, image observations, encoding, capture and verifier exits must be separately observed; none is inferred here.',
 'storage_configuration': {'images_dictionary_bytes': 536870912,
                           'documents_dictionary_bytes': 268435456,
                           'data_dictionary_bytes': 67108864,
                           'cap_bytes': 536870912,
                           'unchanged_allowance_bytes': 5000000,
                           'scheduled_capture': '2026-11-17T15:49:30+00:00',
                           'next_slot': '2026-11-17T16:49:30+00:00'},
 'install_receipts': [bind('records/checkpoint37_codec_policy_install.json'),
                      bind('records/checkpoint37_memory_policy_install.json')],
 'retained_scope': 'All predecessors, failed attempts, proposals, original PNGs and logical evidence bytes remain retained. No archive is created by this binder.',
}
out = ROOT/'records/checkpoint37_operational_source_review.json'
with out.open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps({'result': record['result'], 'sources': len(sources),
                  'independent_review_files': len(REVIEWS), 'output': str(out.relative_to(ROOT))}))
