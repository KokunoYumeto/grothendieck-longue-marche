from pathlib import Path
R=Path(__file__).resolve().parents[1]
with (R/'notation.md').open('a') as f:f.write(r'''
| P alphabets | `\mathbb P` in the two left expressions; plain `P` in the products and central/lower inclusions | Scan011, distinct doubled uprights versus single stems, root crops | Preserve each local alphabet reading |
| Looped E | `\mathscr E` | Scan011, final top argument and smaller curled arguments | Final top doubt resolved; H's described looped capital maps to the same E reading |
| Rounded and angular Z | First rounded `\unsure{Z|2}`; angular live `Z` at top-right and lower overwritten factor | Scan011, each local crop | Rounded recurrences carry the first per-page qualification |
| Oblique paired separators | `\mathrel{/\!/}` at their separate levels | Scan011, beside crossed Hom and above central P line | Both slanted strokes and their placement retained |
| Qualified diagram forms | Arrow-side `\unsure{H|U}`; index `\unsure{Y|V}`; lower `\unsure{V|W}` | Scan011, crossing strokes and subscript descender | Supported alternative glyphs retained; no intended map supplied |
| Overwritten right diagram object | Thin `H` beneath heavy `\Gamma` | Scan011, crossbar/right stem under top/left replacement strokes | Both glyphs resolved and overlapped in place |
| Glyph and cancellation scope | Raised M/U; recovered R with deleted/live alternatives | Scan011, crossed Hom cluster | Glyph confidence and uncertain cancellation target recorded separately at the same physical form |
''')
p=R/'legibility_note.md';s=p.read_text().replace('scans 002–008 and 010 have been decided','scans 002–008 and 010–011 have been decided')
s+='\nScan011 combines fairly readable formulas with heavily crossed predecessors and intricate drawings. Six of its fifteen original C doubt rows resolve completely. Rounded Z/2, the e/E and t/1 predecessors, O/0, raised M/U, cancellation scope, H/U, Y/V and V/W remain qualified. Fine paths and detached marks are preserved graphically with uncertain attribution or role. H describes the sketches and diagram but omits several local paths and overwritten states; each whole physical drawing/diagram is counted once against that description.\n';p.write_text(s)
p=R/'workflow_assessment.md';s=p.read_text();s+='\nScan011: all150 reader proposal rows and46 reader doubt entries were mapped. A/B represented the right diagram through free TikZ; the final uses tikz-cd with local TikZ overlays. Distinct glyph/state proposals for one raised form receive one physical-locus count per witness, while both qualifications stay explicit. Root crops exposed extra small traces and endpoint continuations; each has a path, inventory entry and record. The changes summary now separates confidence counts for C and H.\n';p.write_text(s)
s=(R/'briefs/brief_v09_scan011.md').read_text().replace('# Independent reader brief v09 — first used on scan 011','# Independent reader brief v10 — first used on scan 012',1)
s+=r'''

## Revision v10 after scan 011

Use genuine tikz-cd for a diagram, with standard local TikZ nodes or end-picture overlays for overwritten letters, detached strokes and retraced arrows. Free TikZ belongs inside the figure macro for drawings. Keep the diagram's observed detached pieces detached; preserve their entire supported endpoints without inferred connections.

A readable glyph and its cancellation target can have separate confidence. Record both, including explicit cancelled/live alternatives where the strokes leave the target open. The correction count for a shared physical glyph/state cluster is one per witness; cross-reference the additional local qualification and retain it in the changes log. The original C source-row map remains separate from this physical-locus count.

Tiny detached strokes newly observed in a crop require their own graphical representation and inventory item. A supported path can have high shape confidence while its role, hand or surface origin remains unknown. Inspect thin continuations, gaps and lower ends within the planned crop. Give every report difference and every remaining doubt an explicit local entry with its exact location, evidence and source-row identity. Keep reading.tex and report.json synchronized before returning.
'''
(R/'briefs/brief_v10_scan012.md').write_text(s)
print('Notation, legibility, workflow and v10 brief updated.')
