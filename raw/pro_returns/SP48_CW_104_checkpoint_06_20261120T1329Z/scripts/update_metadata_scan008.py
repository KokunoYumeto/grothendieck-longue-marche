from pathlib import Path

out = Path(__file__).resolve().parents[1]

def append_once(name, marker, text):
    p = out / name
    s = p.read_text()
    if marker not in s:
        p.write_text(s.rstrip() + '\n\n' + text.strip() + '\n')

append_once('notation.md', '| Alphabets on scan 008 |', r'''
| Alphabets on scan 008 | Live subobject symbols are plain J, with one right stem and a low left return; the old canceled I has top and bottom bars. D is plain, including tilded D; N is barred/doubled | 008 | Preserve the local plain J even though scan007 has doubled J; no global alphabet substitution |
| Quantifier-shaped sign on scan 008 | Two separately ending near-upright legs joined by a crossbar: H/forall, H first | 008 | Medium; unlike scan007's locally preferred forall/H order; syntax does not join the legs |
| Type map and quotations | tau_n above J_n to mathbb N; separate tau_n, application opening two ticks type, without closing ticks. Opening ticks before D_n also remain unclosed | 008 | No supplied quotation closure or surrounding parentheses |
| Hom maps on scan 008 | First lower maps-to tail begins slightly right of the upper hook and ends slightly farther right; second target has flat lower brackets with J labels | 008 | Literal two-row displacement and bracket placement retained |
| High mark and lower relation | High 4/asterisk has triangular counter, transverse arm and descender, separate from n prime. Lower relation has a curled left vertical, straight right vertical and an upper-left point | 008 | Medium doubts; lower relation traced literally inside unsure; tall brackets enclose sign and Hom together |
| Double indices on scan 008 | Definition J_{n-prime,n}; final diagram J_{n,n-prime}; rho_{n,n-prime} at both arrows | 008 | Both orders confirmed and retained; type discrepancy belongs only to the notes |
| Detached strokes and final curve | One point after canceled I_{<=n} des; two points right/below second Hom, upper farther right. Final inclusion curve headless, curled left end, right endpoint below-left of final J | 008 | Preserve literal detached traces and gaps; no punctuation or arrowheads inferred |
''')

append_once('abbreviations.md', '| def |', r'''
| def | Définition | 008, equality label | Unaccented written form retained |
| bijec | Bijection | 008, canceled fragment | Fragment retained without completion |
| ens | Ensemble | 008, repeated | Each occurrence checked for absence of a terminal stop; no expansion in transcription |
''')

append_once('legibility.md', 'Scan 008 is a handwritten', r'''
Scan 008 is a handwritten text sheet with type and Hom maps, interlinear changes and a final commutativity diagram. Most live words and indices are legible. Least secure are the naming cluster, heavily overworked old capitals and parenthesis, the canceled article, the high 4/asterisk, the short relation trace, the final accent in commutativité and the locally H-shaped quantifier. C is closer in deletion states and literal diagrams; H sometimes supplies punctuation, repeated words, an extra de or ou, changes J to I and gives canceled words live. C also needs corrections: a new quantifier doubt, refined naming alternatives, absent final period in a cancellation, small points, unequal arrow positions and the scope of the lower brackets. The index reversal in the final diagram is manuscript evidence and remains uncorrected. No title, date or author folio is recovered; the archive number remains a comment.
''')

append_once('workflow_assessment.md', '# Scan 008', r'''
# Scan 008

The three complete readings and all 156 source issue records were compared before any main image. The main reader inspected 34 distinct crops, 20 new and 14 reused. A failed tool delivery returned neither of two images; the exact existing files were redelivered and inspected once each. A complete naming crop was selected because another reader's crop clipped the q descender. The main decisions retained a new H/forall doubt against unanimity, five naming alternatives, a literal relation trace and detached ink points. The lower brackets enclose both relation and Hom, and the final curve has detached endpoints; those spatial facts are not settled by a generic description of the diagram.

Two text-only helpers assembled the draft and comparison/inventory records from the main observations. Five actual mathematical proof/background events are recorded with their original time. Their later source confirmation is explicitly not an additional mathematical check. The definition and final diagram have opposite index orders; both are transcribed as written. No OCR, outside research, LaTeX compilation or rendering was used.
''')

append_once('workflow_events.md', '## v08 — first used on scan 009', r'''
## v08 — first used on scan 009

Scan008 exposed a clipped descender in one crop, a four-alternative report whose full reading had five, an H punctuation paraphrase not present in H itself, and disagreement over whether the lower brackets enclose the relation as well as Hom. Its curve was described as detached even when retained code attached it to a node. v08 asks readers to reconcile their prose with their actual transcription, use exact witness quotations in comparisons, preserve the complete enclosure and endpoint geometry, and inventory uncertain cancellation status once rather than creating a definite extra deletion. A new main doubt can remain even against all three readers.
''')

old = out / 'briefs/brief_v07_scan008.md'
new = out / 'briefs/brief_v08_scan009.md'
if not new.exists():
    s = old.read_text().replace('v07 — first used on scan 008', 'v08 — first used on scan 009', 1)
    s += r'''

## Clarifications from scan 008

- Reconcile your issue report with your final reading: if the full reading retains five alternatives, do not report only four. Quote the witness itself for each comparison; do not manufacture punctuation or doubt marks from a paraphrase of it.
- Crop boundaries must include full descenders and the entire deletion contour. Describe which elements a tall bracket encloses, including any sign above a lower formula. A bracket around two rows must not become a bracket around only the bottom row.
- Check that diagram code implements your stated geometry. If a curve endpoint is detached, leave a real gap to the object; do not end it at the node corner. Retain unequal starts and lengths of parallel rows.
- Distinguish a physically present cluster from its uncertain cancellation status. Inventory the cluster once, without presenting one disputed deletion interpretation as a definite extra physical element. Preserve isolated points and their relative positions without assigning punctuation functions from context.
- Neither consensus nor mathematical syntax removes a locally unresolved glyph. A literal traced sign may be placed inside unsure, with possible interpretations in the record, when a clean standard symbol would lose its distinctive strokes.
'''
    new.write_text(s)
print('Updated scan008 metadata and prepared brief_v08_scan009.md.')
