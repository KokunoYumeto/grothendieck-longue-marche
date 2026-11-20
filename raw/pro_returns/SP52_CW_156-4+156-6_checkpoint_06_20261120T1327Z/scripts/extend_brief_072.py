from pathlib import Path
O=Path(__file__).resolve().parents[1]
if not any(s.startswith('scan 072 done ') and 'cote 156-4' in s for s in (O/'progress.log').read_text().splitlines()):raise SystemExit('Finalize072 before extending the brief.')
p=O/'briefs/brief_v09.md'
if p.exists():raise SystemExit('Brief v09 already exists.')
s=(O/'briefs/brief_v08.md').read_text().replace('# Independent reader brief v08 — first used 156-4 scan 072','# Independent reader brief v09 — first used 156-4 scan 073')
addition=r'''## Clarifications from scan 072

- The packet conventions remain exact: line-end hyphenated words are joined. A physical corre-/spond division establishes the letters of correspond; it is not an additional punctuation difference. Keep an actual word hyphen where it belongs.
- An old overwritten form encoded as deleted text just before its live replacement follows the prescribed convention; that macro sequence alone does not assert two separate positions in the manuscript. Distinguish actual extra letters from equivalent old-before-new notation. At a crossed initial inside a word, establish whether the following letters continue that same word before supplying another full initial and word.
- For an optional zero-width overprint, remember that rlap enters a text box: a mathcal/mathscr expression inside it needs its own math delimiters. Standard LaTeX only; no new macros and no compiler.
- Report an incompletely framed target with approximate original coordinates of the missing continuation. Include clear space beyond every endpoint, especially the bottom of a diagram or the end of a slanted line. A literal drawing can preserve a slant, loop and separate curve without deciding that they are a prime or one comma.
- Align a raised bracketed word with an H placeholder by the physical ink even if H put it at the end of the preceding paragraph. Count the actual word once. Keep report entries concise: use short exact snippets and named complete figure references instead of copying a long TikZ group into many rows.

'''
s=s.replace('## Final return\n',addition+'## Final return\n');p.write_text(s)
with (O/'brief_changes.md').open('a') as f:f.write('''
## v09 — first used 156-4 scan 073

Scan072 had one initial corrected letter misrepresented as an extra cancelled initial plus a full new word by one reader, and a raised [pleine] that another reader counted twice by following H's paragraph placement. Two readers identified the full bottom punctuation as multiple marks rather than a lone comma/prime. A slanted ending was clipped in the readers' crops; root used the reported missing coordinates for one new crop of that still-open endpoint. Root's own square crop clipped its low tails, which an overlapping existing reader crop covered without recropping. Root also withdrew an attempted physical corre-/spond division because convention7 explicitly requires joining, and clarified that convention4's old-before-new macros alone do not establish distinct positions. A math-mode rlap expression required explicit inner math delimiters. The new brief reinforces these source and framing distinctions, and concise named-figure reporting. Counts: readers17/18/18, root20existing+5new. No OCR, compilation, outside research or mathematical proof validation occurred.
''')
print(p)
