"""Bind final reviews actually read by root; does not modify formal sources."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
sources={
 'work_A/A106_central_congruence_hexagon_proposed.tex':'7da2b23a1c970fd1dfb38423d3d43b9c7391ec866828eaf0c20685115139d97b',
 'work_A/A107_relative_central_modular_conjugacy_proposed.tex':'27289531e4c5bfff0e2fa950892d656a812ca8cc830a75ed8a86b0351d53a660',
 'work_A/A108_central_quotient_factor_transporter_proposed.tex':'eb01b6017808a8ea08b789300d62a0e360c40e1d91fe038bbde3b23cad0e263c',
 'work_DE/A109_derived_cyclic_cohomology_proposed.tex':'caf3f5d1711a8e249c4f5bbeef97faf58c7d0d9218335fe7e9e285280fe976b0',
 'work_DE/A110_quotient_frame_ambiguity_proposed.tex':'32a44b0a03f01f7cc55d2e5bd9dd2a1127fae6951845b3436d7ea10e7219d61b',
 'work_root/A111_coherent_C2_CM_proposed.tex':'6eb5def140f375f616d9f2ba56d02d260fc58f5bb4d06cdedfcee29a545f0ebc',
 'work_CE/B165_entire_deleted_kernel_cohomology_proposed.tex':'2b35c67cf3452f646aa1c51bbd5464331cc17b055e5b15b726861e5ecb6842bb',
 'work_CE/B166_entire_filling_cohomology_proposed.tex':'7dd113a2fb9db4f23b82705ace9141a9cbaa030f7c27cdb46d8f992601148d09',
}
pairs=[
 ('work_CE/review_A106_A107_A108_formal34','txt'),
 ('work_CE/review_A109_formal34','txt'),
 ('work_A/review_A110_quotient_frame_ambiguity34','md'),
 ('work_A/review_A110_final_certificate34','md'),
 ('work_DE/review_A111_full_source34','md'),
 ('work_DE/review_B165_B166_full_source34','md'),
]
paths=[base+'.'+extension for base,kind in pairs for extension in (kind,'json')]
reviews={p:sha256((root/p).read_bytes()).hexdigest() for p in paths}
all_text='\n'.join((root/p).read_text() for p in paths)
for p,h in sources.items():
    assert sha256((root/p).read_bytes()).hexdigest()==h
    assert h in all_text
out=dict(status='PASS_FINAL_SOURCES',recorded_at=datetime.now(timezone.utc).isoformat(),
         root_read_all_complete_reviews=True,source_hashes=sources,reviews=reviews,
         scope='Root read every complete listed review and its JSON. A110 final provenance-only difference is covered by the preserved full proof review plus exact final-diff/producer/output audit. Root read every complete final mathematical proof and the exact notation/provenance differences.')
with (root/'records/checkpoint34_independent_review_manifest.json').open('x') as stream:
    json.dump(out,stream,indent=2);stream.write('\n')
print('Bound8 final source hashes and12 fully read independent review records.')
