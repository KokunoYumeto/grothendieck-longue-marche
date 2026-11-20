from pathlib import Path

out = Path(__file__).resolve().parents[1]

def append_once(name, marker, text):
    p = out / name
    s = p.read_text()
    if marker not in s:
        p.write_text(s.rstrip() + '\n\n' + text.strip() + '\n')

append_once('notation.md', '| Alphabets on scan 007 |', r'''
| Alphabets on scan 007 | M, D and the first N are plain; subsequent indexing N forms have barred returning uprights, mathbb N. The subobject-order symbol is mathbb J_n, with doubled contours and a lower left hook | 007 | Occurrences checked separately; no global alphabet imposed |
| Subobject map on scan 007 | Hom(D′,D) right-arrow to tilded plain D above u mapsto u(D′); M is below terminal m of Hom. Lower u is indented and its shaft starts farther left than the upper arrow | 007 | Literal two-row geometry; star label between row levels, far left |
| Phi and insertion on scan 007 | Closed oval with a bisecting stem resolves Phi; low D′. Small M- has a leader to the gap before isomorphes, not to Phi | 007 | Preserve the prefix as inserted text |
| Ambiguous forms on scan 007 | modèles/modéles and flèche/fléche retain accent-direction doubts; first reference is (i]/[i]/(i); leading quantifier forall/H remains unusual | 007 | Alternatives ordered by the local ink, including asymmetric brackets |
| Canceled forms on scan 007 | Short autom/autom. before raised end; de uncertain; barred old I resolved; e/s retained; old D under live M resolved; plui/plus, une canceled before inserted une | 007 | Detached dot favors plui without grammatical repair |
| Mark before cause on scan 007 | Reduced à/colon followed by a separate lower-right oblique stroke; cause de (ii), | 007 | Do not combine the separate stroke into a certain therefore sign |
| Other marks on scan 007 | Raised asterisk after classe n; no abbreviation stop after each ens or isom, nor after raised end; two-tick quotation pairs | 007 | Period after classification M retained; final identification D has none |
''')

append_once('abbreviations.md', '| autom / autom. |', r'''
| autom / autom. | Automorphisme | 007, canceled | Short written form retained; presence of a covered terminal stop remains uncertain |
| end | Endomorphisme | 007, raised replacement | No terminal stop visible; no expansion in transcription |
| isom | Isomorphisme | 007, twice | Both occurrences lack an abbreviation stop |
| ens / d'ens | Ensemble(s) / d'ensemble(s) | 007 | Each visible occurrence lacks an abbreviation stop |
''')

append_once('legibility.md', 'Scan 007 is a handwritten', r'''
Scan 007 is a handwritten text sheet with two formula displays and several interlinear changes. Most continuous text is legible. The least secure places are the nearly vertical accents, covered final stop of canceled autom, reduced par, canceled de and e/s, the compound quantifier, the two small marks before cause, and the dotted canceled plui/plus. The main crops resolved Phi, barred I, the old D beneath M, doubled J and several word doubts. H regularizes quotation marks and abbreviations, changes insertion states and misidentifies the final family; C is closer but its centered M and aligned arrow starts do not preserve the map's actual positions. A complete existing crop was needed for classes because the first planned neighboring crop did not include that whole word. No unseen lettering was reconstructed.
''')

append_once('workflow_assessment.md', '# Scan 007', r'''
# Scan 007

The main reader compared all 115 issue records and the three complete readings before viewing the adjudication crops. Twenty-six distinct crops were inspected: fifteen new and eleven reused. The first neighboring crop did not cover the whole classes locus; a complete existing reader crop was then viewed once for that still-undecided word. One tool delivery failed before an image was received; the identical existing file was redelivered, with no recropping or extra inspection. Main decisions preserved a mixed citation enclosure, a dotted canceled ending and separate oblique stroke that majority simplification could have lost. The map's terminal-m attachment and unequal arrow starts were refined from the main crop despite broad agreement on its two-row structure.

Two text-only helpers assembled the draft and consolidated the issue/inventory records. A separate text-only mathematical audit rechecked the already recorded proof and counterexample arguments without image access. All nine actual mathematical check events are retained, with the counterexample limited to an interpretation asserting uniqueness among arbitrary abstract order isomorphisms; the distinguished transport induced by the unique object isomorphism is a separate verified claim. None of these arguments changes the transcription.
''')

append_once('workflow_events.md', '## v07 — first used on scan 008', r'''
## v07 — first used on scan 008

Scan 007 required complete symbol/word coverage, precise leader attachments, mixed reference delimiters and attention to a detached dot over a canceled ending. The upper Hom label and lower arrow starts showed why a generic two-row description is insufficient. v07 adds these lessons and distinguishes an issue's approximate bounding box from the actual saved crop metadata. It also clarifies that a primary-page context-table label can include trailing descriptive text: exclude other-page rows even then. A failed image delivery is counted separately from a successful inspection, never as a second crop.
''')

old = out / 'briefs/brief_v06_scan007.md'
new = out / 'briefs/brief_v07_scan008.md'
if not new.exists():
    s = old.read_text().replace('v06 — first used on scan 007', 'v07 — first used on scan 008', 1)
    s += r'''

## Clarifications from scan 007

- A saved crop must include the complete disputed word or symbol, including its descender, accent, terminal point and deletion contour. Report the crop's actual bounding box as metadata, separately from an approximate issue box. If an intended locus falls outside an existing crop, say so rather than claiming it settled that locus.
- A label below an operator may attach to its last letter rather than the center of the whole operator. Preserve unequal row indentation, unequal arrow starts/lengths and a label between row levels; do not automatically align every arrow in one column.
- Check each end of a reference enclosure independently. A mixed opening parenthesis and closing bracket may be what the ink shows. A detached dot above a canceled ending may support a grammatically unusual reading; retain the ink-supported alternative first.
- Follow a small inserted prefix's leader to its exact landing gap; do not turn a displaced prefix into a formula subscript. Distinguish a long insertion leader from a local word underline.
- When filtering C contextual tables, the primary scan number may be followed by a comma or description. Other-page primary labels remain excluded. A delivery failure before an image was received permits redelivery of that exact existing file once; record it separately from actual views.
'''
    new.write_text(s)
print('Updated scan007 metadata and prepared brief_v07_scan008.md.')
