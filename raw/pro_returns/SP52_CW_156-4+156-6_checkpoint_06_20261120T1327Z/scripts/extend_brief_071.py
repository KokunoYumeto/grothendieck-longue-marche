from pathlib import Path
O=Path(__file__).resolve().parents[1]
log=(O/'progress.log').read_text()
if not any(s.startswith('scan 071 done ') and 'cote 156-4' in s for s in log.splitlines()):raise SystemExit('Finalize071 before extending the brief.')
p=O/'briefs/brief_v08.md'
if p.exists():raise SystemExit('Brief v08 already exists.')
s=(O/'briefs/brief_v07.md').read_text().replace('# Independent reader brief v07 — first used 156-4 scan 071','# Independent reader brief v08 — first used 156-4 scan 072')
addition='''## Clarifications from scan 071

- Quote C and H from the actual packet, including punctuation and paragraph boundaries. A summary can lose a blank line or shorten a source scope. A physical line beginning at the same left edge does not by itself prove or disprove a new handwritten paragraph.
- Keep overwritten folios at their actual number of digit positions. An old digit under a later digit must not become a third successive digit. A broadly cancelled block does not prove its number is crossed: inspect where the long strokes begin and end.
- A long stroke crossing a baseline word may also connect an insertion. If cancellation versus connector function remains uncertain, retain both states and reproduce the stroke; grammar does not settle the state.
- For a complete continuous cancellation drawing, reproduce its boundary and separate strokes with the text once. Rotating TikZ coordinates alone does not rotate node lettering: use node rotation or transform shape where the text must turn with the geometry. Do not replace the drawn cancellation by a prose comment.
- Verify every local alphabet occurrence separately and cite evidence that actually contains that occurrence. A broad crop of the right side does not cover a low-left F just because it belongs to the same corollary.
- Crowded punctuation at a scan edge may be best preserved as a doubt-marked drawing rather than a confident guessed brace or semicolon. Keep every visible curve and short arm, without inferring the continuation beyond the scan edge.

'''
s=s.replace('## Final return\n',addition+'## Final return\n')
p.write_text(s)
with (O/'brief_changes.md').open('a') as f:f.write('''
## v08 — first used 156-4 scan 072

Scan071 exposed uncertainty in whether an insertion arm cancelled de; readers encoded an overwritten two-position folio as three successive digits and broadly cancelled the number although the long strokes began below it. The complete lower drawing required node lettering to rotate with its geometry. A text audit found a local family-F occurrence outside every root-viewed crop, so root made one additional crop rather than cite unrelated evidence. The actual packet also corrected a paragraph-break statement lost in a compacted summary; no false C change was retained. The brief now emphasizes exact source scope, local crop coverage, layer positions, explicit rotation and literal edge punctuation. Reader counts were14/20/16; root saw23existing crops and made3. No OCR, compilation, outside research or mathematical verification occurred.
''')
print(p)
