"""Record completed root readings of the late exact annular comparisons."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
expected = {
 'work_A/actual_elliptic_X_cubic_negative_frame37.md': '75f055e0125ec23b8034b0a69850acc94219552c9f57317b37f35df3d5fb65f7',
 'work_DE/actual_annular_X_frame_modular_comparison37.md': '7f758ffb26d35e042df5ec051f91f86f2852906f57a2d4f21ea15bd7357abdf3',
 'work_DE/actual_annular_original_Theta_frame_upgrade37.md': 'a3c81a99997cfec37ab4e3cbeee89d44a6aaa93d42d69e5843c660cf4997603d',
 'work_A/actual_annular_forgetting_pure_extension_obstruction37.md': 'a0b3ef4f4d41667394c1852a8fc88aa9905148e3a1e1d5569b829e710ceda8ce',
 'work_DE/A132_negative_hexagon_base_transporter_proposed.tex': '343ef45c0b4b07c9c79d6f74f20898b0a56145ed2c9ead72654f699b3c4e81af',
 'work_A/A133_full_elliptic_involution_transporter_proposed.tex': 'adac30c1f88a9bf90c834da37dd7485f0a5f19316602f234326034fe6bfdcc3d',
}
def bind(rel):
    raw = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
sources = [bind(rel) for rel in expected]
assert all(row['sha256'] == expected[row['path']] for row in sources)
peers = [bind(rel) for rel in [
 'work_DE/review_X_cubic_negative_frame37.md',
 'work_A/review_annular_X_frame_comparison37.md',
 'work_A/review_A132_full_source37.md',
 'work_DE/review_A133_full_source37.md',
 'work_CE/review_A132_A133_full_sources37.txt',
 'work_CE/review_full_elliptic_involution_transporter37.txt',
]]
record = {
 'recorded_at': datetime.now(timezone.utc).isoformat(),
 'result': 'PASS_COMPLETE_ROOT_SYMBOLIC_SOURCE_REVIEW',
 'sources': sources, 'complete_independent_review_texts': peers,
 'root_complete_source_read_chunks': ['6f2eda', '6b8264', '6c54db', '012889'],
 'root_complete_peer_text_read_chunks': ['6f2eda', '6b8264', '822537'],
 'new_no_extension_peer_scope': 'Root has checked the entire proof; separate peer responses are pending and are not preclaimed.',
 'independent_root_checks': [
  'The actual type-B source is distinguished from both images. R^3, the two source maps and the original generator marking hold literally.',
  'The pure source is F3 semidirect F2 with full finite-target topology; its actual configuration action has two isolated three-cycle fixed points and no transposition fixed points. The bounded cellular cohomology argument and the previously audited prime-order comparison have the stated source, not an infinite-index image.',
  'The tau-to-s normalization is the RIGHT product J_s=J_tau R. Its modular image is the original J_1^alpha, not J_1^alpha r^{-1}.',
  'The actual source gauge H_S=r_S theta_T(r_S)^{-1} has the two required images h1 and phi. The original-Theta external modular image must be phi times the external alpha involution. The designated reflection then maps exactly to (J_1^alpha)^{-1}alpha.',
  'For any continuous rho:F->H, extension of the specified PURE annular pullback to elliptic P forces rho(y)=1 by K=[Y,X], then rho(x)=1 by [Y,X2^{-1}]=a. The converse is the trivial map. The signed q3 is typed only on F.',
  'Both complete proposed formal proofs A132 and A133 preserve the ordered cycles, original norm, whole Brunnian kernel, explicit cobounders and the distinct X/Y normalizer types.'
 ],
 'primary_read_scope': {
  'Schneps2006': 'Root freshly opened complete Definition1.1, normalized composition and equation1.3 context in turn1281view0; no fresh full general-action proof is claimed.',
  'Enriquez2014': 'Root freshly opened Proposition2.20 statement/full-profinite continuation and entire part(1), author version1003.1012v3, in turn1283view0; previous complete part(2) reading is separately recorded.'
 },
 'scope': 'Supplemental exact full-group research and reviewed next-cycle TeX only. The frozen37 PDF, formal register, bibliography and render remain unchanged. Both main decisions, the canonical positive CM comparison and the specified boundary equation remain Open.'
}
with (ROOT / 'records/checkpoint37_annular_root_review.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
addition = '''
## Further late exact annular comparisons, after the formal37 freeze

The actual X-direction cubic R=X sigma tau has exact order three and
full normalizer S3 in the original elliptic involution extension. Its
normalizer differs from the C6 normalizer of the corrected Y-direction
cubic. The actual annular source (B4/Z(B4)) times_{S4} S3 has two based
maps, to the elliptic group and to the ORIGINAL modular group. Its full
profinite source action, topology and torsion comparison are proved
separately from its image. The correct normalized transporter is
J_s=J_tau R. A source gauge with images h1 and phi gives the comparison
even for the ORIGINAL elliptic Theta: the modular external involution
must map to phi times the original alpha involution, and the specified
reflection maps exactly to (J_1^alpha)^{-1}alpha. These are isomorphisms
on the two finite S3 frames, not a map from the whole elliptic image
back to the modular group.

A separate exact obstruction shows why simply extending the signed
modular representation cannot finish the CM comparison. For ANY
continuous rho:F->H, its pullback to the pure annular source extends to
the full elliptic pure group if and only if rho is trivial. The original
relations K=[Y,X] and [Y,X2^{-1}]=sigma^2 force rho(y)=rho(x)=1. The
signed q3 is used only on its actual domain F. Thus the common-source
frame comparison remains valid, while the direct extension route is
closed by a complete presentation-level argument. The canonical
positive-frame/source-kernel compatibility, original CM sign, boundary
condition and both main decisions remain Open.

The complete root source and independent review scope is bound in
records/checkpoint37_annular_root_review.json. Proposed A132 and A133
also received complete current-source root and independent reviews.
No formal37 statement count, source, PDF or render was changed.
'''
report = ROOT / 'records/thirty_seventh_hour_research_report.md'
assert '## Further late exact annular comparisons' not in report.read_text()
with report.open('a') as stream:
    stream.write(addition)
print(json.dumps({'result': record['result'], 'sources': len(sources),
                  'peer_texts': len(peers), 'formal37_changed': False}))
