from pathlib import Path
import json
out=Path('/workspace/scratch/94c948875852/SP42_CW_29/readers/scan006/R2')
diffs=[]
def add(place,c,h,reading,ac,ah,kind,confidence,evidence,bbox,crop=None,math_note=''):
 diffs.append(dict(id=f'R2-006-{len(diffs)+1:02d}',place=place,c=c,h=h,reading=reading,against_c=ac,against_h=ah,kind=kind,marked_in_H=False,confidence=confidence,evidence=evidence,bbox=bbox,crop=crop,math_note=math_note))
add('Authorial page number at top centre',r'\mspage{2.}','omission',r'\mspage{2.}',False,True,'omission','high','Half a and crop 01: dark curved 2 with a pale separate point at its lower right; this is distinct from the archival 5 at the bottom left.',[738,33,778,65],'crops/01_folio.jpg')
add('Underlined p.19 label',r'\uline{p.19 etc}','p.19 etc',r'\uline{p.19 etc}',False,True,'omission','high','Half a: a continuous dark underline runs below p.19 etc and ends before the separated colon. H omits the underline.',[204,147,324,210])
add('Exclamation mark beside the p.19 label',r'subtle (but this could be expected).\n\margin{!}','omission',r'\margin{!}\uline{p.19 etc}',True,True,'insertion or placement','high','Half a: a long near-vertical dark stroke and a detached lower dot stand in the left margin beside the beginning of the p.19 paragraph, not beside its final line. The mark is retained and anchored at that label; H omits it.',[134,168,160,225])
add('Cancelled sign after an easier one',r'one\deleted{\unsure{?}}.','one.',r'one\deleted{\unsure{?}}.',False,True,'omission','medium','Crop 03: above the following live baseline point is a curved hook with dense intersecting transverse and oblique strokes. A question-shaped original is possible but not fully recoverable. The cancellation itself is certain and cannot be omitted. Whether the lower point was reused from the cancelled punctuation cannot be established.',[647,208,690,268],'crops/03_cancelled_sign.jpg')
add('Scope of underline in the line 3 condition',r'irreducible in \uline{Zariski topology}',r'\emph{irreducible in Zariski topology}',r'irreducible in \uline{Zariski topology}',False,True,'other','high','Half a: the underline begins beneath the Z of Zariski and continues through topology. There is no corresponding underline beneath irreducible in. This is a difference in emphasis extent, not merely the use of emph rather than uline.',[684,414,1117,479])
add('Separator after p.33,34 etc',r'p.33,34 etc \unsure{..|:}\quad',r'p.33, 34 etc.\ ---',r'p.33,34 etc \unsure{..|:}\quad',False,True,'misread symbol or index','medium','Crop 04: two separate short dark points lie close together, the second slightly lower and to the right. Their horizontal displacement exceeds their vertical displacement. No long dash is present and no point immediately follows the c of etc. Two baseline points are preferred, with an oblique colon retained as an alternative.',[351,649,506,713],'crops/04_p33_separator.jpg')
add('Gap after theor.9.4',r'p.43 theor.9.4\quad You',r'p.43 theor.\ 9.4 --- You',r'p.43 theor.9.4\quad You',False,True,'text not on the page','high','Half a: the label is followed by blank space and then You. There is no horizontal dash in that gap.',[324,736,497,801])
add('Lowercase for after satisfactory',r'satisfactory . for instance','satisfactory. For instance',r'satisfactory . for instance',False,True,'misread word','high','Crop 06: for begins with a long narrow stem and a small loop at its top, matching the lowercase f inside the immediately preceding satisfactory. The faint detached period between the words is visible.',[1379,734,1580,804],'crops/06_for_instance.jpg')
add('Compressed word after constant',r'\unsure{fibres|fibers}','fibers',r'\unsure{fibres|fibers}',False,True,'misread word','medium','Crop 05: f, i, the tall b and the final s are visible. Between b and s the connected low strokes include a short rising shoulder and a shallow curl; these favour r-e but do not completely exclude e-r. The preferred diplomatic reading is fibres, while fibers remains an explicit alternative. This is not a conclusive rejection of H.',[792,807,874,863],'crops/05_fibres.jpg')
add('Gap after p.45. line 5 etc.',r'p.45. line 5 etc.\quad Is',r'p.45. line 5 etc.\ --- Is',r'p.45. line 5 etc.\quad Is',False,True,'text not on the page','high','Halves a and b: the point after etc is followed by open paper before Is. No dash crosses the gap.',[341,946,591,1020])
margin_drawing=r'\margin{\figure{\begin{tikzpicture}\draw (0,0)--(-.05,.8);\draw (.12,-.05)--(.09,.65);\end{tikzpicture}}}'
add('Two marginal strokes beside the Lefschetz appendix paragraph',margin_drawing,'omission',margin_drawing,False,True,'drawing or diagram','high','Half b: two separate thin near-vertical strokes stand in the left margin, slanting slightly right toward their lower ends. The left stroke starts higher; the right stroke reaches a little lower. They are reproduced as a marginal drawing, without assigning a mathematical meaning.',[260,1081,307,1211])
add('Narrowing the signature doubt',r'\unsure{J.P. Murre}','J. P. Murre.',r'J.P. Mu\unsure{rre}',True,False,'other','high','Crop 09: J and P are individually formed and each has its own detached point. The tall three-stroke M and the following low u are legible. Only the final connected rre sequence remains compressed. C doubt is narrowed to those letters; H preferred letters are unchanged in this row, and its terminal period is addressed separately.',[990,1813,1145,1874],'crops/09_signature.jpg')
add('No separate full stop after the signature surname',r'\unsure{J.P. Murre}','J. P. Murre.',r'J.P. Mu\unsure{rre}',False,True,'text not on the page','high','Crop 09: the surname ends in a connected low horizontal flourish. There is no separate period at the right or in the lower-right area below its ending; the only clear detached dots belong to the initials.',[1090,1831,1155,1880],'crops/09_signature.jpg')

c_doubts=[
 {'place':'After an easier one','c':r'\deleted{\unsure{?}}','reading':r'\deleted{\unsure{?}}','resolved':False,'evidence':'Crop 03 confirms crossing-out and a surviving upper hook, but the original sign is obscured. The question-mark candidate is retained without inventing a second candidate. The lower baseline point is visible and live.','bbox':[647,208,690,268],'crop':'crops/03_cancelled_sign.jpg'},
 {'place':'After p.33,34 etc','c':r'\unsure{..|:}','reading':r'\unsure{..|:}','resolved':False,'evidence':'Crop 04 shows two close diagonally arranged points. The almost horizontal arrangement favours two periods, but a steeply slanted colon cannot be excluded. No dash is visible.','bbox':[450,674,474,695],'crop':'crops/04_p33_separator.jpg'},
 {'place':'Theor.9.4 comment, after constant','c':r'\unsure{fibres|fibers}','reading':r'\unsure{fibres|fibers}','resolved':False,'evidence':'Crop 05 secures f-i-b and the final s. The tiny connected interior strokes favour r-e, but their compressed joins do not decisively rule out e-r.','bbox':[792,807,874,863],'crop':'crops/05_fibres.jpg'},
 {'place':'Signature','c':r'\unsure{J.P. Murre}','reading':r'J.P. Mu\unsure{rre}','resolved':False,'evidence':'Crop 09 resolves J, P, both initial points, M and u. The final rre remains a compressed connected flourish; doubt is therefore retained only on that suffix. No other page or external identity was used.','bbox':[990,1813,1145,1874],'crop':'crops/09_signature.jpg'},
]
remaining=[
 {'place':'Cancelled sign after an easier one','reading':r'\deleted{\unsure{?}}','alternatives':[],'confidence':'low','reason':'The crossing strokes obscure the lower structure of the original upper sign; no second complete stroke-compatible candidate is secure.'},
 {'place':'Separator after p.33,34 etc','reading':'..','alternatives':[':'],'confidence':'medium','reason':'Two points are clear, but their intended grouping as two periods or a very oblique colon is not uniquely determined.'},
 {'place':'Word after constant in the theor.9.4 comment','reading':'fibres','alternatives':['fibers'],'confidence':'medium','reason':'The r/e order is compressed into connected low strokes.'},
 {'place':'Signature surname suffix','reading':'rre','alternatives':[],'confidence':'medium','reason':'The suffix after the clear Mu is compressed; no competing complete surname is established from this page.'},
]
inv=[]
def item(element,kind,position,words,hand='unnamed other hand (main handwritten letter)'):
 inv.append({'sheet_kind':'letter','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
item('E01','text','top centre, approximately (740,35)',r'Authorial folio 2., encoded as \mspage{2.}')
item('E02','text','upper left, y=80–116','word to use else.')
item('E03','text','upper block, y=145–331',r'\uline{p.19 etc} : I expected lemma 4.3; through the lemma 4.4 comment')
item('E04','margin note','left margin beside the p.19 label, y=174–219','!','unnamed other hand (heavy upright marginal mark; identity not established)')
item('E05','deletion','after an easier one, approximately (660,228)',r'\deleted{\unsure{?}}')
item('E06','text','upper middle, y=351–409','p.26. line 1: I shall try to find a precise reference.')
item('E07','text','upper middle, y=416–520',r'line 3 : the condition : irreducible in \uline{Zariski topology}')
item('E08','text','middle, y=547–596',r'last line in 3) : it seems necessary to mention also the points $s\prime$')
item('E09','text','middle, y=647–704',r'p.33,34 etc \unsure{..|:} I did not see an easier proof for prop 7.4.')
item('E10','text','middle, y=738–923',r'p.43 theor.9.4 You have mentioned; including constant \unsure{fibres|fibers}')
item('E11','text','middle, y=951–1014','p.45. line 5 etc. Is this indication sufficient?')
item('E12','text','below centre, y=1054–1171','I have not written an appendix on the Lefschetz theory.')
item('E13','drawing','left margin beside the appendix paragraph, x=270–299, y=1089–1204','Two thin vertical/slightly slanting strokes; reproduced with marginal TikZ drawing','unnamed other hand (thin marginal strokes; identity and medium not established)')
item('E14','text','lower block, y=1247–1656','It is not necessary to return the manuscript; through date of your first volume.')
item('E15','deletion','inside parenthesis in lower block, x=1450–1520, y=1405–1451',r'\deleted{foto}, followed by live photo')
item('E16','text','lower right, y=1668–1795',r'With best regards,\\ Sincerely yours,\\')
item('E17','text','lower right, y=1815–1869',r'J.P. Mu\unsure{rre}; no final detached period')
item('E18','text','bottom-left edge, approximately (29,1993)','Archival 5, represented only by % archive sheet number: 5','unnamed other hand (pale archival numeral)')

report={
 'scan':6,'reader':'R2',
 'started_utc':'not captured; earliest actual recorded clock: 2026-11-20 09:42:59 UTC',
 'finished_utc':'pending final validation',
 'views':['whole','half_a','half_b']+[f'crops/{n}' for n in ['01_folio.jpg','02_opening_word.jpg','03_cancelled_sign.jpg','04_p33_separator.jpg','05_fibres.jpg','06_for_instance.jpg','07_copy_initial.jpg','08_manuscript_initial.jpg','09_signature.jpg']],
 'differences':diffs,'c_doubts':c_doubts,'s_rows':[],
 'remaining_doubts':remaining,'inventory':inv,
 'notation':[
  {'place':'last line in 3)','visible':'small cursive s followed by one upper-right prime','latex':"$s'$",'uncertainty':'none; no capital, subscript or second prime is visible'},
  {'place':'p.33,34 label separator','visible':'two low points, second slightly lower and farther right','latex':r'\unsure{..|:}','uncertainty':'two periods preferred; very oblique colon remains possible'},
  {'place':'p.19 label and line 3 condition','visible':'underline beneath p.19 etc; underline beneath Zariski topology only','latex':r'\uline{p.19 etc}; \uline{Zariski topology}','uncertainty':'none in underline extent'},
  {'place':'appendix paragraph left margin','visible':'two thin, nearly vertical strokes','latex':margin_drawing,'uncertainty':'meaning and hand attribution not established; treated as a drawing, not as mathematical parallel notation'},
 ],
 'abbreviations':[
  {'form':'p.','expansion':'page; expansion provided only here'},
  {'form':'etc / etc.','expansion':'et cetera; manuscript punctuation retained at each occurrence'},
  {'form':'prop','expansion':'proposition; no extra period introduced'},
  {'form':'theor.','expansion':'theorem; no expansion in the transcription'},
 ],
 'notes':{
  'content':'Handwritten continuation of a letter, carrying authorial page number 2. and archival numeral 5. It comments on proofs, a Zariski-topology irreducibility condition, primed points, a theorem involving constant fibres and crossings, a possible Lefschetz appendix, and manuscript production/deadline arrangements. The page closes with regards and a signature. All ordinary prose, punctuation, underlines, margins and cancellations were read against the image, including witness agreements. The main hand is not externally attributed. Crops 02, 07 and 08 reconsidered tall initial letter strokes in word, copy and manuscript; these were read as the letter’s cursive lowercase forms, and the witnesses’ case readings were retained. The two clear cancellations are the upper question-shaped sign and foto. No additional insertion, diagram, display, stamp, letterhead, title or date is visible. S.json is the empty array, so there are no S rows to adjudicate.',
  'author_checks':[
   'I expected lemma 4.3 to be almost trivial but when I tried to write a proof I did not see an easier one',
   'the proof of lemma 4.4 is kind of subtle (but this could be expected).',
   'I shall try to find a precise reference.',
   'the condition : irreducible in Zariski topology is unpleasant but I have not been able to avoid it.',
   "it seems necessary to mention also the points s'.",
   'I did not see an easier proof for prop 7.4.',
   "However I don't see how to get a satisfactory statement.",
   'Is this indication sufficient?',
   'I have not written an appendix on the Lefschetz theory. If you think this is useful then I can still try.'
  ],
  'titles_dates_pages':['No title or date visible.','Authorial folio: 2.','Archival sheet numeral: 5, included only as a comment.','Cited pages: 19; 26; 33,34; 43; 45.','Cited identifiers: lemma 4.3; lemma 4.4; prop 7.4; theor.9.4.'],
  'math_reading_decisions':['The inline point notation is lowercase s with one prime, read visually.','No proposition, lemma or theorem is stated with enough hypotheses here to support a proof check. The mathematical comments are carried as the author’s unverified background claims, not as independently established results.','The word-order and grammar of arbitrary crossings escapes are retained. No mathematically expected correction was made.','No actual mathematical proof, computation, formal certificate or reuse/recheck occurred during this reading. Pure visual checks are not entered as mathematical check_events.']
 },
 'check_events':[],
 'brief_feedback':['The brief gives no special case criterion for tall initial strokes in connected cursive. These were judged using the repeated letterforms on this page, without importing casing from another page.','The original cancelled question-shaped sign and the live baseline point may share punctuation history; the visible cancellation and live point can be preserved, but their chronological relationship is not recoverable.'],
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# Independent reading — scan 006, R2','',
 '## Scope and view record','',
 'Only the authorized scan 006 packet, brief, crop helper, and this reader’s own files were used. No OCR, external research, other page, or other reader’s material was inspected. The whole image was viewed once, half a once, and half b once. Nine tight crops were made and viewed once each: **3 source views + 9 crop views = 12 image views**. No place was recropped or re-viewed. Crop JPEGs and one JSON transform record for each are in `crops/`; `views_metadata.json` records the dimensions and half offsets. The whole image is 1678 × 2036; half a begins at y=0 and half b at y=938. All report bounding boxes use whole-image coordinates.',
 '',
 'The exact task-start clock was not captured. The earliest actual recorded clock was 2026-11-20 09:42:59 UTC.',
 '',
 '## Complete reading','',
 'The complete diplomatic page is `reading.tex`. It contains every text block, the authorial folio, the archival-number comment, both underlined stretches, both marginal marks, both cancellations, the inline primed point, and the three closing/signature lines. It preserves the original wording, abbreviations and grammar. There are no freestanding mathematical displays or diagrams on this sheet.',
 '',
 f'## Discrepancies ({len(diffs)})','',
 f'{sum(x["against_c"] for x in diffs)} rows are against C; {sum(x["against_h"] for x in diffs)} are against H. A row can count against both. H contains no uncertainty flag at these places. Equivalent markup alone is not counted. The C changes are the placement of the exclamation mark at the p.19 label and narrowing the signature doubt to the compressed suffix.',
 '']
for d in diffs:
 lines += [f'### {d["id"]} — {d["place"]}','',f'- **C:** `{d["c"]}`',f'- **H:** `{d["h"]}`',f'- **Reading:** `{d["reading"]}`',f'- **Flags:** against C = {d["against_c"]}; against H = {d["against_h"]}; kind = {d["kind"]}; confidence = {d["confidence"]}.',f'- **Evidence:** {d["evidence"]}',f'- **Whole-image box:** `{d["bbox"]}`; crop: `{d["crop"] or "none; settled from the halves"}`.','']
lines += ['## C doubt dispositions and retained doubts','',
 'All four inherited C doubt places were inspected. None is fully resolved at every letter/sign. The signature is substantially narrowed: J.P. and Mu are clear; only rre remains marked. The point after the surname supplied by H is absent.','']
for d in c_doubts:
 lines += [f'- **{d["place"]}:** `{d["reading"]}`. {d["evidence"]}']
lines += ['',
 'The four remaining doubt loci are the cancelled question-shaped sign, the two-point separator, fibres/fibers, and the final rre of the surname. S.json is empty; there are no S rows.',
 '',
 '## Inventory','',
 '| Element | Kind | Position | Content/state |',
 '|---|---|---|---|']
for v in inv:
 lines.append(f'| {v["element"]} | {v["kind"]} | {v["position"]} | {v["first_words_or_objects"].replace("|","/")} |')
lines += ['',
 'Every inventory item is represented in `reading.tex`; separate rows identify the actual cancellations. There are no claimed hand-added accents, typed words, or additional insertion states. All body text is handwritten. The hand or medium of the marginal marks is not identified beyond their visible contrast with the cursive main text.',
 '',
 '## Notes and mathematical status','',report['notes']['content'],'',
 'The author’s explicit doubts and promised work include the difficulty of finding shorter proofs for lemma 4.3 and prop 7.4, the subtlety of lemma 4.4, an outstanding reference, the undesirable irreducibility condition, adding points s′, the unsatisfactory formulation of theorem 9.4, the sufficiency of an indication, and the unwritten Lefschetz appendix. These remain authorial statements. No independent proof or computation was performed; `check_events` is intentionally empty. The only mathematical notation decision is the visually clear lowercase s with one prime.',
 '',
 'The page has no title or date. Its own folio is 2.; the archival numeral is 5. The cited manuscript pages are 19, 26, 33,34, 43 and 45.',
 '',
 '## Crop record','',
 '| Crop | Target | Result |',
 '|---|---|---|',
 '| 01_folio.jpg | Folio punctuation | 2. retained; point is pale but separate. |',
 '| 02_opening_word.jpg | Initial letter of word | Lowercase reading retained from the cursive ductus. |',
 '| 03_cancelled_sign.jpg | Crossed sign after one | Cancellation certain; ? remains uncertain. |',
 '| 04_p33_separator.jpg | Two-point separator | Two points clear; periods/oblique-colon interpretation retained. |',
 '| 05_fibres.jpg | Compressed r/e order | fibres preferred, fibers still possible. |',
 '| 06_for_instance.jpg | Lowercase f and preceding point | for, with lowercase looped f; faint period present. |',
 '| 07_copy_initial.jpg | copy at manuscript line start | Lowercase reading retained. |',
 '| 08_manuscript_initial.jpg | manuscript at line start | Lowercase reading retained by its repeated cursive form. |',
 '| 09_signature.jpg | Initials, surname and final punctuation | J.P. Mu clear; suffix rre doubtful; no separate terminal point. |',
 '',
 '## Main-reader adjudication','',
 'The four retained doubt loci warrant adjudication from their saved evidence. The interpretation of the two low diagonal points as periods or colon is unresolved at the level of intended punctuation, although the physical two-point form is clear. The cancelled sign’s dot may have been reused as the live period; the image does not determine that chronology. No mathematical correction is proposed.',
 '']
(out/'report.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'differences':len(diffs),'against_c':sum(x['against_c'] for x in diffs),'against_h':sum(x['against_h'] for x in diffs),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),'inventory':len(inv),'crops':9}))
