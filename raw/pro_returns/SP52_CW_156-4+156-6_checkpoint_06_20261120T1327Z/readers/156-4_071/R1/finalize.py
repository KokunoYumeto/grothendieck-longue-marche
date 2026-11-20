from pathlib import Path
import json,re
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R1')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_071')
p=out/'reading.tex'
s=p.read_text().replace(r'\begin{scope}[rotate=180]',r'\begin{scope}[rotate=180,transform shape]')
p.write_text(s)
r=json.loads((out/'report.json').read_text())
h=(packet/'H.tex').read_text()
lastnote=h[h.index(r'\note{la moitié'):].strip()
firstnote=h[h.index(r'\page{70}'):h.index('Il revient')].strip()
for row in r['differences']:
 if row['location']=='upper folio':row['h']=firstnote
 if row['location']=='inverted folio':
  row['h']=lastnote
  row['scope_note']='Folio evidence in H is an editorial note; only its 55 and unspecified overload are compared here.'
 if row['location']=='inverted draft, boundary and cancellation geometry':
  row['h']=lastnote
  row['scope_note']='The H note describes a line and oblique cancellations; the difference is their drawn geometry, not omission of its editorial prose.'
 if row['location']=='inverted parenthesis, element':
  row['c']='x';row['h']='X';row['reading']='x'
 if row['location']=='corollary, state and placement of de':
  row['scope_note']='Only de state and position are compared in this row; the raised F alphabet has its own following row.'
 if row['location']=='restatement, quotation marks':
  row['scope_note']='Only opening and closing quotation strokes are compared; the F alphabet and word accent have separate rows.'
r['finished_utc']='2026-11-20T11:47:30Z'
r['notes']['structural_checks']='JSON parsed; brace depth was balanced; begin/end environments matched; every crop path existed; boolean fields had JSON boolean types; each remaining-doubt reading or figure reference occurred in reading.tex. No LaTeX compiler or OCR was invoked.'
(out/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
evidence={
1:'Overlaid upper digits remain 69/79 below 70/79; first repetition sign is visibly two strokes.',
2:'Donnons nous retains a reduced-middle doubt; the second repetition sign is a horizontal pair.',
3:'Both irregular marginal columns are reproduced literally as fragments, with the lower-left/upper-right offset.',
4:'The baseline de is crossed beneath the raised phrase; the reduced inserted F alphabet remains open. Formula endpoint is a low comma.',
5:'The contraction seult/seulemt remains open; the first order sign has a straight lower bar.',
6:'The second sign resolves to preceq; first contrée/contrie remains open; Phi, inclusion and final looped F are clear.',
7:'The worked t in itou stays doubtful; ce qu’on appelle is readable. No separate old word is supplied.',
8:'Two opening quote strokes, no separate closing pair, uncertain accent in saturee/saturée, and crowded comma/closing/forked marks at right.',
9:'automatiquemt/automatiquement and the separate crossed f-like loop remain doubtful.',
10:'Surface folio 55; earlier 4/3 unresolved. Worked Phi has uncertain earlier-F state. un and de resolved; parenthesis retained.',
11:'Plain M, reduced x, and blunt application link. The extreme end after inclusion is partly clipped, so punctuation stays doubtful.',
12:'Two distinct internally cancelled groups, Dém without a secure stop, and final union indices read. The last high point belongs to i.',
13:'A p, tiny medial mark, large descending g and final stroke support page/pge; H p. omits visible letters.',
14:'Geometry only: open continuous boundary with one inward jog, and thirteen distinct oblique/curved cancellation strokes; the scan-edge continuation remains open.'}
lines=['# Inspection log — 156-4 / scan 071 — R1','','Read only assignment.md, brief_v07.md, the six assigned packet text files, the notation snapshot, and the three assigned source images. No other reader material, preceding scan, OCR, external source, or LaTeX compiler was used.','','## Image views in order','',f'1. `{r["image_views"][0]}` — whole page once, untransformed; layout, inverted lower block, margins, insertions and deletions inventoried.',f'2. `{r["image_views"][1]}` — supplied upper half once, untransformed; all upright lines and their small marks compared with C and H.',f'3. `{r["image_views"][2]}` — supplied lower half once, untransformed; remaining upright text, inverted draft and long graphical marks examined.','','All following crops are R1’s own. Coordinates below are on the original whole source image, not on either half. Each crop was viewed once. Images were emitted in batches of no more than three; no display was truncated.','']
for i,c in enumerate(r['crops'],1):
 lines += [f'{i+3}. `{c["path"]}`',f'   - Source: `{c["source"]}`; bbox `{c["bbox"]}`; rotation `{c["rotation"]}°`; scale `{c["scale"]:.9f}`.', '   - Transform order: crop; rotate when specified; autocontrast; PIL LANCZOS resize to 2500 pixels across; sharpness factor 1.25; JPEG quality 94.',f'   - Target: {c["reason"]}.',f'   - Evidence: {evidence[i]}','']
lines += ['## Open-place list used for crop selection','','The initial list comprised: upper folio; Donnons nous; both marginal columns; formula punctuation and insertion/deletion; seult; bowed order sign and first sous-contrée; itou; quote and closing punctuation; abbreviated automatic ending and cancelled loop; rotated folio/opening; rotated middle/application; rotated internal deletions and final formula. The reference word needed its own added crop because the prior text crops did not frame it. The remaining continuous boundary and complete cancellation strokes then received one geometric target crop. No decided text locus was recropped for a second reading.','','## Framing limits','','Crop 11 does not fully frame the extreme terminal continuation after inclusion, approximately original x=20–35, y=2025–2090; the possible comma remains marked. Crop 14 clips the scan-edge continuation of the boundary near original x=1680, y=1805; the figure keeps that endpoint open. No missing accent or stop was established from a clipped target.','','## Necessary consistency checks','','Parsed report.json; checked fragment brace balance and environment pairing, crop existence, required boolean types, and presence of every remaining-doubt snippet or figure reference in reading.tex. The inverted text scope uses transform shape so its text follows the 180° orientation. No compilation or optional mathematical validation. check_events is empty.','']
(out/'inspection_log.md').write_text('\n'.join(lines))
print('final files written')
print('differences:',len(r['differences']),'remaining doubts:',len(r['remaining_doubts']),'crops:',len(r['crops']))
