from pathlib import Path
import json,copy,datetime,re
O=Path(__file__).resolve().parents[1]; B=O/'readers/156-4_065'; K='156-4_065'
r=[json.loads((B/f'R{i}/report.json').read_text()) for i in [1,2,3]]
m=json.loads((O.parent/'page_packets'/K/'metadata.json').read_text())
t=(B/'R3/reading.tex').read_text().replace(r'le\deleted{\unsure{s}}',r'\unsure{le\deleted{s}|les}').replace(r'les figures \deleted{\unsure{de}}',r'les figures \deleted{\unsure{de|des}}').replace('pour pres que tout',r'pour \unsure{pres|près|prés} que tout')
filename=Path(m['codex_file']).name
(O/'pages'/filename).write_text(t)
P='readers/156-4_065/R3/crops/'
A='crops/156-4_065/'
p={1:'01_opening_deletion.png',2:'02_question_final_F.png',3:'03_le_les_cas.png',4:'04_c4_letters_des.png',5:'05_inserted_necessity.png',6:'06_cor1_pres.png',7:'07_cor1_sauf.png',8:'08_cor2_heading.png',9:'09_cor2_les.png',10:'10_cor2_fini.png',11:'11_canceled_b_dash.png',12:'12_cor3_first_de.png',13:'13_cor3_parenthesis.png',14:'14_cor3_meme_de.png',15:'15_cor3_last_map.png',16:'16_cor3_pres_que.png',17:'17_comp_punctuation.jpg'}
def cp(n):return P+p[n]
D=copy.deepcopy(r[1]['differences'])
mapcrop={1:A+'a01_donnons.jpg',2:cp(1),3:cp(1),4:A+'a02_family_question.jpg',5:A+'a02_family_question.jpg',6:A+'a02_family_question.jpg',7:A+'a03_i_composante.jpg',8:cp(2),9:A+'a04_faudrait_sauf.jpg',10:cp(3),11:A+'a05_sont.jpg',12:A+'a06_on_va.jpg',13:cp(4),14:cp(4),15:cp(17),16:cp(5),17:cp(5),18:cp(5),19:cp(5),20:A+'a09_cor1_map.jpg',21:cp(7),22:cp(6),23:cp(6),24:cp(8),25:cp(8),26:cp(8),27:cp(9),28:cp(10),29:cp(10),30:cp(10),31:cp(10),32:cp(10),33:A+'a10_cancelled_cases.jpg',34:A+'a10_cancelled_cases.jpg',35:cp(11),36:cp(12),37:cp(14),38:cp(13),39:cp(13),40:cp(14),41:cp(14),42:cp(14),43:cp(15),44:cp(16),45:cp(16)}
for i,x in enumerate(D,1):
 x['id']=f'{K}-D{i:03d}';x['crop']=mapcrop[i];x['readers']='R1/R2/R3 agree on the literal reading unless a disagreement is recorded below.'
 x['scan_shows']=re.sub(r'^(First half|Second half): ','',x['scan_shows'])
 x['math_consequential']=i in [8,21,23,43]
 if i==13:x['crop']+='; '+A+'a07_c4_final_variables.jpg'
 if i==19:x['crop']+='; '+A+'a08_cancelled_cor.jpg'
 for f in ['bbox','bbox_image']:x.pop(f,None)
def upd(i,**kw):D[i-1].update(kw)
valid=r'\unsure{validité|\deleted{val}idité}'
upd(15,reading='comp',confidence='medium',scan_shows='The end is an attached p-like down-and-up hook. No detached abbreviation point is visible; preserve comp without a supplied point.',readers=r'R1 comp.; R2 \unsure{comp|comp.}; R3 comp. Final: R3.')
upd(17,reading=valid,scan_shows='A single word-sized group has reinforced val-like initial strokes and an idité-like ending. There is no separate old word followed by a second complete validité. Whether the initial val is crossed or retraced remains uncertain.',readers=r'R1 \unsure{validité|\deleted{déd} validité|\deleted{val} validité}; R2 \unsure{validité}; R3 '+valid+'. Final: R3.')
insertline=r"\deleted{Cor} \inserted{C'est néc et suffisant pour la "+valid+' des}'
upd(19,reading=insertline,c=r"\deleted{Cor} \inserted{C'est \unsure{néc|néc.} et suffisant pour la \deleted{\unsure{déd|val}} \unsure{validité|déduction} des}",h=r"C'est nécessaire et suffisant pour la \ill{} des \ill{}; \struck{Cor}",scan_shows='The crossed Cor is at the left below a two-line interlinear note. Its large C and crossed or strokes remain visible. The inserted note ends at des; the placement is retained.')
fig=re.search(r'(\\figure\{.*?\\end\{tikzpicture\}\})',t,re.S).group(1)
upd(24,reading=fig,change_c=True,kind='drawing or diagram',marked_in_h='yes',h=r'\emph{Cor. 2}; editorial note describing a cadre',scan_shows='The added, underlined Cor. 2 is above the old donc. The open angular enclosure has a top stroke, a long left side, and an arm extending down-left toward the continuation. Its shape is reproduced in TikZ.',readers='R1/R2 transcribe the heading and describe the connector in a comment. R3 reproduces it in TikZ. Final: R3 graphic representation.')
upd(25,reading=r'\deleted{\unsure{donc}}',change_c=False,confidence='low',scan_shows='A lower-case d-like loop survives below the inserted heading; the following compressed letters are heavily crossed. Keep donc as the best reading with its doubt.',readers=r'R1/R2 \deleted{donc}; R3 \deleted{\unsure{donc}}. Final: R3; certainty is not supported by the cancellation.')
article=r'\unsure{le\deleted{s}|les}'
upd(27,reading=article,scan_shows='One article-sized cluster follows dans, with an l loop, an e-like continuation and a darkened final s-like stroke. There are not two separate complete words. The final s may be cancelled; that state remains uncertain.',readers=r'R1 \unsure{le\deleted{s}|les}; R2 \unsure{le|les}; R3 le\deleted{\unsure{s}}. Final: R1.')
upd(28,location='Corollaire 2, extent of I est fini insertion',c=r'\inserted{$I$ est} fini.',h='$I$ est fini',reading=r'\inserted{$I$ est fini.}',change_c=True,scan_shows='I est fini occupies one raised line above the cancelled suivants. The entire phrase, including fini and its final point, belongs to the insertion.',readers=r'R1/R3 \inserted{$I$ est fini.}; R2 limits insertion to I est. Final: R1/R3.')
upd(29,reading='',change_c=True,change_h=False,kind='text not on the page',confidence='medium',scan_shows='The tall crossed stem belongs to the t and terminal strokes of suivants. It is not a separate abandoned f between suivants and the inserted fini.',readers=r'R1 \deleted{\unsure{suivants|suivants f}}; R2 retains separate \deleted{\unsure{f}}; R3 has only \deleted{suivants}. Final: R3.')
upd(30,reading=r'\deleted{suivants} \inserted{$I$ est fini.}',change_c=False,scan_shows='The cancelled suivants is on the old lower line, with I est fini above it. H places the cancelled word after the completed live phrase. The old-to-new sequence is retained; the specific insertion extent and absent extra f are counted separately.',readers='R1/R3 include all of I est fini in the insertion; R2 separates fini and an alleged old f. Final: R3, as decided at the adjoining loci.')
upd(31,scan_shows='No two-dot colon follows the crossed suivants. The tall nearby strokes are the end of that cancelled word, rather than punctuation.')
upd(34,c='Toute',h='toute',reading='Toute')
upd(36,readers=r'R1/R2 \deleted{\unsure{de|des}}; R3 \deleted{\unsure{de}}. Final: include the possible terminal s.')
upd(41,reading=r'\deleted{\unsure{de}}',change_c=False,confidence='low',scan_shows='A separate small d-like loop survives before pour, but the ending is largely hidden by the thick strike. Keep the best de reading uncertain.',readers=r'R1/R3 \deleted{\unsure{de}}; R2 \deleted{de}. Final: R1/R3.')
upd(43,reading=r'\mathcal F\unsure{\text{---}|\longrightarrow}\prod\mathcal F_i',change_c=False,confidence='medium',scan_shows='The connector is a horizontal stroke with one short downward terminal turn. Unlike the first two maps, it has no complete two-branch head. A reduced arrow remains possible, so retain the dash/arrow alternative.',readers='R1/R3 retain the dash/arrow doubt; R2 gives a plain dash. Final: retain the unresolved graphic distinction.')
upd(45,reading=r'\unsure{pres|près|prés} que',change_c=True,confidence='low',scan_shows='A word-sized gap separates pres and que. A tiny isolated mark above pres may be an accent or a stray point; it has no secure direction. Preserve the two groups and mark the accent doubt.',readers='R1 records pres/près/prés; R2/R3 read unaccented pres. Final: preserve the unresolved tiny mark in the alternatives.')
extra=copy.deepcopy(next(x for x in r[0]['differences'] if x['id']=='R1-D13'));extra.update(id=K+'-D046',crop=A+'a04_faudrait_sauf.jpg',readers='All three full readings give sauf; R1 additionally records removal of H’s doubt.');extra.pop('bbox',None);extra.pop('bbox_image',None);D.insert(10,extra)
for x in D:
 if x['math_consequential']:
  x['consequence']={'Opening, terminal overwritten F and low mark':'The possible subscript 0 is retained rather than silently identifying the terminal object with F.','Corollaire 1, sauf deletion state':'H gives a cancelled exception word as live, changing the displayed condition.','Corollaire 1, ending after cancelled pres':'H supplies a finite-exception formulation where the visible live ending is que tout i; the cancelled pres is preserved.','Corollaire 3, final map alphabets and separator':'The final map connector is not a secure arrow; the uncertainty is preserved instead of silently completing a map.'}.get(x['location'],x['scan_shows'])
cd=copy.deepcopy(r[2]['c_doubts'])
for x in cd:
 x['crop']=str(Path(x['crop']).relative_to(O)) if x.get('crop') else None
 x['scan_shows']=re.sub(r'^Image: .*?\.jpg\. ','',x['scan_shows']);x.pop('bbox',None)
 if 'canceled de after figures' in x['location']:x.update(reading=r'\deleted{\unsure{de|des}}',status='revised',scan_shows='The short terminal group is crossed; de is best, but an s cannot be excluded.')
 if 'final pres que' in x['location']:x.update(reading=r'\unsure{pres|près|prés} que',status='revised',scan_shows='The gap is clear. A tiny mark above pres cannot be securely identified as an accent or excluded as stray ink.')
dis=[]
for i,rs in [(15,['comp.',r'\unsure{comp|comp.}','comp']),(17,[r'\unsure{validité|\deleted{déd} validité|\deleted{val} validité}',r'\unsure{validité}',valid]),(24,['heading + connector comment','heading + connector comment','heading with TikZ enclosure']),(25,[r'\deleted{donc}',r'\deleted{donc}',r'\deleted{\unsure{donc}}']),(27,[article,r'\unsure{le|les}',r'le\deleted{\unsure{s}}']),(28,[r'\inserted{$I$ est fini.}',r'\inserted{$I$ est} fini.',r'\inserted{$I$ est fini.}']),(29,[r'\deleted{\unsure{suivants|suivants f}}',r'\deleted{suivants} \deleted{\unsure{f}}',r'\deleted{suivants}']),(36,[r'\deleted{\unsure{de|des}}',r'\deleted{\unsure{de|des}}',r'\deleted{\unsure{de}}']),(41,[r'\deleted{\unsure{de}}',r'\deleted{de}',r'\deleted{\unsure{de}}']),(43,[r'\unsure{\text{---}|\longrightarrow}',r'\text{---}',r'\unsure{\text{---}|\longrightarrow}']),(45,[r'\unsure{pres|près|prés} que','pres que','pres que'])]:
 x=next(x for x in D if x['id']==f'{K}-D{i:03d}');dis.append(dict(location=x['location'],r1=rs[0],r2=rs[1],r3=rs[2],final=x['reading'],evidence=x['scan_shows']+' ['+x['crop']+']'))
inv=copy.deepcopy(r[1]['inventory']);inv=[x for x in inv if x['element']!='Corollaire 2 abandoned initial']
for x in inv:
 x['sheet_kind']='text';kind=x['kind'];x['kind']='deletion' if 'deletion' in kind else ('text' if kind in ['page number','text block','underlined heading','retraced text'] else kind)
 if x['element']=='Corollaire 2 I est':x.update(element='Corollaire 2 I est fini',first_words_or_objects='I est fini.',position='whole raised phrase above cancelled suivants')
 if x['element']=='Corollaire 2 heading and angular connector':x.update(element='Corollaire 2 heading',position='interlined right of Corollaire 1 ending')
 if x['element']=='Crowded word in note':x.update(kind='deletion',first_words_or_objects='validité; possible cancellation of val marked in place')
 if x['element']=='Corollaire 2 article correction':x.update(kind='deletion',first_words_or_objects='le with possibly cancelled s / les')
inv.insert(16,dict(element='Angular insertion enclosure',kind='drawing',position='around Cor. 2, extending down-left toward continuation',first_words_or_objects='open angular line with top, left side and lower-left arm',sheet_kind='text',hand='his hand',transcribed='yes'))
remaining=[]
for loc,reading,alts,reason,conf in [
 ('Opening, cancelled formula',r'\unsure{F_i\in|F_i}',['F_i with membership','F_i alone'],'The cancellation merges the following C-shaped trace with a possible opening parenthesis.','low'),
 ('Opening, left parenthesis',r'\unsure{(}',['opening parenthesis','trace belonging to cancelled formula'],'Closing parenthesis is definite; the independent opening is not.','low'),
 ('Opening, overwritten family symbol',r'\deleted{\unsure{\mathcal F}}',['overwritten family F','retracing of F'],'Superimposed upper and middle strokes obscure the earlier full form.','low'),
 ('Opening, terminal index',r'\unsure{F_0|F}',['F_0','F with low nonindex mark'],'The low loop is visible, but its status is not secure.','low'),
 ('Déjà, article',r'\unsure{le|les}',['le','les'],'Retracing obscures the terminal s.','medium'),
 ('Inserted necessity note',valid,['validité','val cancelled within validité'],'The first group may be crossed or retraced; no independent second word is visible.','low'),
 ('Corollaire 1, crossed pres',r'\deleted{\unsure{pres}}',['pres','crossed p-initial group'],'Multiple strokes obscure the small interior letters.','low'),
 ('Corollaire 2, crossed donc',r'\deleted{\unsure{donc}}',['donc','unresolved crossed d-initial group'],'Following letters are heavily cancelled.','low'),
 ('Corollaire 2, article',article,['le with cancelled s','les'],'One word-sized group; final-letter cancellation is uncertain.','low'),
 ('Corollaire 3, first crossed de',r'\deleted{\unsure{de|des}}',['de','des'],'The rightmost stroke can be a final s or cancellation.','low'),
 ('Corollaire 3, crossed de before pour',r'\deleted{\unsure{de}}',['de','unresolved crossed group'],'The d-like loop survives but the ending is obscured.','low'),
 ('Corollaire 3, final connector',r'\unsure{\text{---}|\longrightarrow}',['horizontal stroke','reduced arrow'],'Only one downward terminal turn is visible; no full head.','medium'),
 ('Corollaire 3, final pres que',r'\unsure{pres|près|prés} que',['pres','près','prés'],'Tiny possible accent has no secure orientation.','low')]:remaining.append(dict(location=loc,reading=reading,alternatives=alts,reason=reason,confidence=conf))
notes=dict(summary='The opening asks when a family of component figures F_i arises from one global figure. C4 asserts compatibility for elements in disjoint connected components of M. The inserted note calls this necessary and sufficient for the following corollaries. Corollary 1 concerns the image of the component map and contains a revised, still awkward support condition. Corollary 2 is revised to the finite-index case. Corollary 3 states a finite-type (respectively finite) inheritance assertion and describes the image by an eventual-empty condition.',math_reading_decisions=['The component question might suggest a plain terminal F, but a low loop remains visible; the F_0/F uncertainty is retained.','The two bars after en est de are literally transcribed as =; their likely verbal function is recorded only in the abbreviation table.','The third component-map connector lacks a complete head. Expected map notation does not justify converting it to a definite arrow.','The cancelled pres in Corollary 1 creates an awkward live ending. H’s replacement un nb fini d’i was rejected because those letters are absent; no mathematical repair was made.','The page does not supply the preceding definitions or proof details needed to validate the corollaries. No independent proof or computation was performed.'],author_checks=["The explicit question is: « quand peut-on dire qu'il existe F … ? » (the complete wording is retained in the transcription).","The interlinear phrase reads « C'est néc et suffisant pour la [validité, state uncertain] des »; this is an author assertion, not a verified implication in this run.","Two draft cases are struck: « a) I est fini » and « b) Toute figure est de t.f. -- alors ». The replacement Cor. 2 keeps the finite-index case."],title_dates_pagination='Scan 065 bears manuscript page 64. No title or date is written on this leaf.')
d=dict(key=K,cote=m['cote'],scan=int(m['our_scan']),folder=m['folder'],their_page=int(m['their_page']),filename=filename,brief_version='v01',differences=D,c_doubts=cd,disputes=dis,remaining_doubts=remaining,inventory=inv,abbreviations=r[1]['abbreviations'],notes=notes,check_events=[],reader_crop_counts={'R1':15,'R2':15,'R3':17},adjudicator_crop_count=10,workflow_note='Three independent full readings, each whole and two halves once. Root inspected 17 existing R3 crops plus 10 new crops for witness differences otherwise settled by halves. A first attempt to display the 10 root crops was truncated and was not counted as inspection; they were then successfully displayed in groups of three, three, three, one. Main did not view whole/half images. Graphic connector, correction extent and uncertainty conventions required brief clarification.')
(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(O/'crops'/K/'inspection_log.md').write_text('# Adjudicator inspection — 156-4 / 065\n\nInspected the 17 R3 crops listed in that reader’s manifest, and the 10 new crops in this directory’s manifest. No whole page or half was displayed by the adjudicator.\n\nThe initial batched attempt to display all 10 new crops exceeded the output context limit; it is not counted as a successful visual inspection. Existing crop files were then displayed successfully in batches a01–a03, a04–a06, a07–a09 and a10. No place was recropped. Decisions and visible strokes are in decisions/156-4_065.json.\n')
(O/'notation.md').write_text(r'''# Notation table

The table records observed graphic forms, not normalized mathematical notation. A future mismatch must be decided in its own ink.

| Sign / form | Transcription | Observed appearance and first page |
| --- | --- | --- |
| Individual figure | `$F$, $F_i$` | Straight upper and middle arms; 156-4/065. |
| Family of figures | `$\mathcal F$, $\mathcal F_i$` | Broad bent or looped top, curved stem; distinguished from plain F. 156-4/065. |
| Ambient set | `$M$` | Single plain peaked capital, not a separate calligraphic alphabet; 156-4/065. |
| Elements | `$x,y$` | Small crossed x and descending y; 156-4/065. |
| Index set and index | `$I$, $i$` | I has top/bottom bars; i is short and dotted. 156-4/065. |
| Empty set | `$\varnothing$` | Oval with long diagonal slash; 156-4/065. Equivalent H empty-set macro alone is not a collation difference. |
| Component-map arrow | `$\to$` | Two earlier maps on 156-4/065 have a full right head. The last has only a short downward end: retain its local dash/arrow doubt. |
| Repetition sign | `$=$` | Two stacked bars after en est de, 156-4/065; preserve literal form. |
| Underline and angular enclosure | `\uline`, TikZ in `\figure` | Underlines and insertion connectors are separate marks; the open enclosure at Cor. 2 is reproduced. |
| Abbreviations | `nb`, `comp`, `néc`, `Cor`, `Cor.`, `t.f.`, `resp.`, `ens` | Keep observed points or absence; do not add a point from the usual abbreviation. 156-4/065. Expansions are in the doubts file only. |

''')
(O/'legibility.md').write_text('After scan 065: ordinary running text is mostly legible. Confidence is lowest in overlapping corrections, heavily crossed small words, the low mark beside the opening terminal F, and the reduced final map stroke. C preserves the page’s wording and correction history more closely here; H expands several abbreviations, replaces some prose, and gives a cancelled exception word as live. C nevertheless requires changes to segmentation, insertion extent, punctuation and the drawn connector. These observations concern the page read so far, not an extrapolated error rate.')
print(json.dumps({'page':K,'difference_rows':len(D),'inventory_rows':len(inv),'remaining_doubts':len(remaining),'disputes':len(dis)}))
