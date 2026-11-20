from pathlib import Path
import json, copy
from datetime import datetime, timezone
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan076/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
ds=[]
for i in range(10):
    d=copy.deepcopy(B[i]);d['id']=f'M076-{i+1:02}'
    d['readers']={'A':A[i]['reading'],'B':B[i]['reading'],'C':C[i if i<9 else 10]['reading']}
    d['marked_in_H']='no'
    if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
    ds.append(d)
paths=['B/B076_09_insertion_connector.jpg','A/A076_01_transition.jpg','A/A076_02_source_index.jpg','B/B076_03_target_index.jpg','B/B076_04_tels_correction.jpg','A/A076_05_donne.jpg','A/A076_06_remark_heading.jpg','A/A076_07_itou.jpg','B/B076_07_cancelled_heading.jpg','B/B076_08_detached_pair.jpg']
for d,p in zip(ds,paths):d['crop']='readers/scan076/'+p
ds[0]['scan_shows']='The raised U has a separate upper prime and a small low i. Beneath it a broad curved left arm descends to a low point in the extensions/de gap, then rises to the right and ends with a short near-horizontal terminal. Main chooses B’s connector and position; A/C reproduce the pointer but simplify its right terminal. C had the inserted label without this visible connector.'
ds[1].update(reading=C[1]['reading'],diff_c=True,alternatives='cursive n; gamma excluded by the two distinct linked stems',confidence='medium',scan_shows='The first glyph has a high curved entry, a first descending stem, an upward link and a second longer descending stem. The suffix ij is lowered, with the j descending. Main accepts C’s eta/n alternatives: the two successive stems do not support the converging single fork of gamma retained by A/B. The preferred eta remains uncertain. Later copies follow the first-occurrence convention.')
ds[1]['math_uncertainty']='The recurring transition alphabet remains eta or cursive n; gamma is removed from the alternatives on the two-stem construction.'
ds[2]['scan_shows']='The source suffix has a short upper entry followed by a long descending loop, extending well below the short i in the adjacent restriction. Main agrees with all readers that this is j, not i; the C doubt is resolved from its own stroke shape.'
ds[3].update(confidence='low',scan_shows='A dark short upright has a rightward upper spur and a broad retraced low loop/foot enclosing white space. Main retains B/C’s i/j/k alternatives: the short foot favors i, while the low loop permits a compressed j and the upper branch permits k. A retains only i/j. No independently readable superseded index or stroke order can be separated, and the expected transition direction does not decide the ink.')
ds[3]['math_uncertainty']='The target extension subscript remains i/j/k. The conditional composition diagnostic uses i but does not establish that reading.'
ds[4].update(confidence='medium',scan_shows='The tall initial stem is crossed at mid-height and has a closed low bowl on its left. The bowl favors a d overwritten by t, as A/C read, but its path merges with the live stem and adjoining stroke. Main retains B’s alternative of a retraced t because the crop does not securely establish two successive letters. The live els is readable; no hidden letter is inferred from syntax.')
ds[5]['scan_shows']='After the two n forms there is one final e loop with an acute above it and a short rising exit. There is no second e loop before par. Main agrees with all three readers on donné, retaining the writer’s non-agreement with L’obstruction.'
ds[6]['scan_shows']='After Rmq and beyond the end of its underline stands one short detached upright. It has no upper and lower turns of s. The two separate points of the following colon remain live. Main resolves the character to 1 with all readers.'
ds[7]['scan_shows']='A short dotted i joins a tall t with a separate crossbar; the next letter is a closed o and the final two low strokes form u with a rising exit. Main agrees with all readers on itou and removes the doubt.'
ds[8].update(confidence='medium',scan_shows='Rmq is readable beneath repeated ascending cancellation strokes and above its surviving underline. The following crowded mark has a curved upper part and a low rightward foot favoring 2, but its crossings leave the plural-ending s alternative possible. Main retains Rmq 2/Rmqs with all readers; the separate colon at the right is not crossed out. No remark body follows it.')
ds[9]['scan_shows']='Two detached dark irregular lobes lie on an ascending left-to-right diagonal: the lower has a pointed low lobe and the upper is wider with an uneven raised top. Main uses B’s lobed contours rather than A’s ellipses or C’s round-and-oval simplification. The surrounding pale halo does not establish further authored marks. Their origin and function remain unresolved; no colon or signature character is assigned.'
s=(O/'readers/scan076/B/reading.tex').read_text()
s=s.replace(B[1]['reading'],ds[1]['reading'])
s=s.replace("d'extensions\\makebox", "d'extensions \\makebox").replace('}}}}de ', '}}}} de ')
(O/'pages/H37-01_37_scan076.tex').write_text(s)
inv=copy.deepcopy(R['B']['inventory'])
inv[5]['first_words_or_objects']=inv[5]['first_words_or_objects'].replace(r'\eta|n|\gamma',r'\eta|n')
notes="""Continuation and ending of the letter, signed ‘P. Deligne’. There is no title, date, salutation, own page number or total count on this sheet; archive 75 is retained only as a comment. The writer represents a global class by local extensions on an affine cover, introduces transition isomorphisms, and states that the obstruction to their cocycle relation ‘est donné par d_2 eta’. He gives the displayed differential and says ‘La même construction marche dans le cas analytique’ and ‘on conclut par une nouvelle application de GAGA’. The live ‘Rmq 1’ begins ‘itou’ and lists algebraic spaces, rigid analytic spaces and formal schemes. Only the next remark heading is cancelled; its colon is live and no body follows. There is no explicit author question or stated doubt on this page.

The writer’s ‘donné’ is retained after ‘L’obstruction’. The opening class is named e, but the later expression is d_2 eta; all three readers distinguish the later two-stem glyph from the initial looped e. This notation tension is preserved without declaring an error. A local source/target calculation, conditional on the preferred target subscript i, confirms that the written transition indices compose consistently. It does not decide the obscured index or verify the asserted obstruction formula, analytic construction or GAGA application. All nine explicit C doubts have decisions; the five remaining uncertain places concern the transition alphabet, target index, possible d-to-t overwrite, cancelled heading, and detached graphic pair. H has description only and no collation rows."""
math=copy.deepcopy(R['C']['math_reading_decisions'])
math += ['The source/target diagnostic is conditional: a map j to i composed with k to j has source k and target i, matching the written ij, jk, ik pattern. This use of the preferred i is not evidence for its obscured strokes; the consolidated target remains i/j/k.', 'The first class e lies in the H^0 Ext^1 group displayed as the domain of d_2. The subsequent d_2 eta was read from half a at whole-image [357, 539, 442, 585]; no settled locus was reopened. This is an internal notation comparison, not a proof that either written symbol is an error.']
notation=copy.deepcopy(R['C']['notation'])
notation[-1]=copy.deepcopy(R['B']['notation'][-1])
events=[]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for a in 'ABC':
    for i,e in enumerate(R[a]['check_events']):
        events.append(dict(statement_id='S076-COCYCLE-TYPING' if i==0 else 'S076-OBSTRUCTION-NOTATION',date=now,who=f'GPT-6 Astra Pro; effort not exposed; independent scan076 reader {a}',type='used and rechecked in this run',outcome=e['outcome']+' Recorded here under the permitted event type; this was a local diagnostic, not an independent proof of the obstruction theorem.'))
events.append(dict(statement_id='S076-COCYCLE-TYPING',date=now,who='GPT-6 Astra Pro; effort not exposed; main second-pass run',type='used and rechecked in this run',outcome='Rechecked only the conditional source/target calculation: (j to i) composed after (k to j) yields (k to i). The obscured target subscript remains i/j/k. No assertion of existence, gluing, obstruction vanishing or GAGA was proved.'))
out=dict(scan=76,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=R['C']['abbreviations'],slips=R['B']['slips'],check_events=events,main_crops=[],main_views=['readers/scan076/'+p for p in paths],delivery_note='A request for the source- and target-index images was truncated before visible delivery. The same retained files were subsequently delivered individually for their first actual main inspection; neither was recropped.')
(O/'decisions/scan076.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nScan 076: all three readers made nine crops. Main inspected ten existing crops, with no new crop; the insertion pointer had been settled by A/C from the half and cropped by B. Source/target image requests lost to truncation were recovered from the identical files for first actual viewing. Main restricted eta/n/gamma to eta/n, retained the added k target alternative and material-state uncertainty in tels, and chose the more faithful B graphical contours. The d_2 eta expression was already settled by all three halves and was not recropped. Readers reported useful conditional composition diagnostics but used nonstandard event labels; version 8 clarifies classification without inflating them into theorem proofs.\n')
print('Wrote scan 076: 10 mandatory decisions, 9 C doubts, 5 unresolved loci.')
