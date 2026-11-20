from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
r={k:json.loads((O/f'readings/scan005/{k}/report.json').read_text()) for k in ['R1','R2','R3']}
t=(O/'readings/scan005/R1/reading.tex').read_text()
reps=[(r'\deleted{\unsure{a|est}}',r'\deleted{a}'),(r'\unsure{v.\,ex.|p.\,ex.|v.\,a.}',r'\unsure{\text{v. ex.}|\text{p. ex.}|\text{v. a.}}'),(r'\overline{xy}',r'\overline{x,y}'),(r'\unsure{\operatorname{réll}|\operatorname{réel}|\operatorname{réal}}',r'\unsure{\operatorname{réll}|\operatorname{réel}}'),(r'\unsure{prolonge|pro\(\overset{?}{l}\)onge}',r'\unsure{pro\(\overset{?}{l}\)onge|prolonge}'),(r'\inserted{\unsure{conn.|connexes}}',r'\inserted{\unsure{conn|conn.|connexes}}')]
for old,new in reps:
 assert t.count(old)==1,(old,t.count(old));t=t.replace(old,new)
(O/'decisions/scan005_final.tex').write_text(t)
main={1:'01_arc_segment',2:'01_arc_segment',3:'02_comma',4:'03_il_f_et_s',6:'04_il_admet',12:'05_segm',21:'07_qui_nest_pas',24:'08_et_disjoints',25:'09_arrow_multi_layout',26:'09_arrow_multi_layout',27:'09_arrow_multi_layout',31:'10_components',32:'11_classification',33:'12_contour_nonempty',34:'13_isom',36:'14_cardinal'}
reader={5:('R3','01_before_soit'),7:('R3','02_overwritten_E'),8:('R3','03_raised_parenthesis'),9:('R1','07_margin_drawing'),10:('R3','04_before_xy'),11:('R3','05_distincts_insertion'),13:('R3','06_pair_condition'),14:('R1','16_realis_phrase'),15:('R1','16_realis_phrase'),16:('R2','06_existence_formula'),17:('R2','06_existence_formula'),18:('R3','09_before_prolonge'),19:('R1','09_prolonge'),20:('R1','10_connex_ending'),22:('R1','11_deleted_reunion'),23:('R1','11_deleted_reunion'),28:('R3','13_dualite'),29:('R3','14_deleted_donc'),30:('R3','15_conn_insertion'),35:('R1','14_connait'),37:('R3','16_strict_condition')}
fs=copy.deepcopy(r['R1']['findings'])
for i,f in enumerate(fs,1):
 f['crop']=f'crops/scan005/{main[i]}.png' if i in main else f'readings/scan005/{reader[i][0]}/crops/{reader[i][1]}.png'
 f['readers']={'R1':f['final'],'R2':'Same substantive reading; see independent reading.tex.','R3':'Same substantive reading; see independent reading.tex.'}
 f['decision']='Main crop inspection supports this reading and placement.'
 f['evidence']=f['evidence'].replace('Upper half:','Main crop:').replace('Lower half:','Main crop:').replace('Lower half has','Main crop has')
def ov(n,**kw):fs[n-1].update(kw)
ov(5,final=r'\deleted{a}',diff_c=True,doubt_action='resolve',confidence='medium',evidence='The cancellation crosses one small closed bowl with a short upright. There is no surviving sequence of three letter bodies for est.',readers={'R1':r'\deleted{\unsure{a|est}}','R2':r'\deleted{\unsure{a|est}}','R3':r'\deleted{a}'},decision='Choose R3: the one-letter shape is readable despite its crossing stroke.')
ov(8,final=r'\inserted{$(\simeq\mathbb{R}^{3},\ \unsure{\text{v. ex.}|\text{p. ex.}|\text{v. a.}})$}',decision='All readers retain the three candidates; the pointed first letter favours v. Text/math styling is not a separate difference.')
ov(9,c=fs[8]['c']+' The drawing appears in the body rather than in the margin.',readers={'R1':'Open lower oval; detached lower stroke; irregular middle patch; terminal stroke.','R2':'Open lower oval with short downward tail; irregular middle mark; terminal stroke.','R3':'Open lower oval and detached lower stroke; irregular patches; upper terminal mark.'},decision='Use R1 geometry in the left margin. The dark lower core is separated by a light interval, though faint connecting grey cannot be categorically excluded. No graph-theoretic meaning is assigned to these marks.')
ov(16,final=r'\unsure{\operatorname{réll}|\operatorname{réel}}',evidence='After ré the crop shows two tall narrow loops, without the low closed bowl needed for a. The first loop may instead be an elongated e.',readers={'R1':'réll | réel | réal','R2':'réll | réel | réal','R3':'réll | réel'},decision='Choose R3 alternatives; réll is first on the visible tall loops. Preserve the spelling difference from the opening réal.')
ov(19,final=r'\unsure{pro\(\overset{?}{l}\)onge|prolonge}',readers={'R1':r'\unsure{prolonge|pro\(\overset{?}{l}\)onge}','R2':r'\unsure{prolonge\textsuperscript{?}|prolonge}','R3':r'\unsure{prolonge|prolonge\textsuperscript{?}}'},decision='Prefer the question-mark alternative, placed over l as R1 records. The dark hook lies over a lighter upright, but contact with the letter prevents certainty; retain the plain-word alternative.')
ov(20,evidence='Main crop crops/scan005/06_geom.png has no detached point after géom. R1 crop 10 shows crossed x followed by a flat exit; a reduced final e cannot be excluded.')
ov(25,readers={'R1':'Curved arrow in left margin from NB toward Graphe; left margin explicitly selected.','R2':'Curved arrow from NB toward Graphe; margin macro.','R3':'Curved arrow from NB toward Graphe; margin macro.'},decision='The arrowhead is beside Graphe, below and left of multi. Use R1 left-margin placement.')
ov(26,readers={'R1':'Circled multi, actual TikZ oval.','R2':'Circled multi, actual TikZ oval.','R3':'multi insertion; its enclosure is recorded in a comment rather than drawn.'},decision='Keep the visible oval as R1/R2 reproduce it; H records the circle in a note, so this is not counted as an H omission.')
ov(27,readers={'R1':'Two-column array with heading and condition on same baseline.','R2':'Heading followed by separate display.','R3':'Heading followed by separate display.'},decision='Choose R1 layout: Graphe polygonal and the bracketed degree condition occupy the same row; the synonym sits above the condition.')
ov(30,final=r'\inserted{\unsure{conn|conn.|connexes}}',evidence='Small enclosed insertion has initial co followed by compressed horizontal strokes; no separate terminal point is secure. The connector runs down after composantes.',readers={'R1':'conn. | connexes','R2':'conn | conn. | connexes','R3':'conn | conn. | connexes'},decision='Choose the R2/R3 alternatives with conn first; neither an abbreviation point nor a fully written ending is clear.')
ov(31,evidence='The main paragraph crop shows sont at the end of the first line, then canceled polygonales. at the start of the next, followed by live des contours. R3 crop 18 separately shows the canceled terminal point.')
# Distinct additional loci reported by R3, all adjudicated on inspected crops.
for num,crop,decision in [(11,'readings/scan005/R3/crops/04_before_xy.png','A detached low blue comma lies between x and y under the bar. Choose R3 over the unpunctuated pair in R1 and R2.'),(32,'crops/scan005/11_classification.png','The replacement contours lies above the canceled designation, not on its baseline.'),(34,'crops/scan005/12_contour_nonempty.png','The replacement contour is above the canceled words; preserve insertion state.')]:
 f=copy.deepcopy(next(x for x in r['R3']['findings'] if x['id']==f'005-R3-{num:02d}'));f.update(crop=crop,decision=decision)
 if num==11:f['readers']={'R1':r'\overline{xy}','R2':r'\overline{xy}','R3':r'\overline{x,y}'}
 else:f['readers']={k:f['final'] for k in r}
 fs.append(f)
# Meaningful consequences, not normalizations of notation.
for n in [17,18,21]:fs[n-1]['consequential']=True
un=copy.deepcopy(r['R3']['unresolved'])
for u in un:
 if u['place']=='Upper stroke of prolonge':u.update(reading='prolonge with a possible question mark over l',alternatives='plain prolonge; the hook may belong to l')
inv=copy.deepcopy(r['R1']['inventory'])
for x in inv:
 x['first_words_or_objects']=x['first_words_or_objects'].replace('a|est','a').replace('overline xy','overline x,y').replace('réll|réel|réal','réll|réel').replace('conn.|connexes','conn|conn.|connexes')
 if x['element']=='Disjointness addition':x['position']='below right end of NB, surrounded by a curved insertion enclosure'
 if x['element']=='Connectedness insertion':x['position']='above components sentence in an enclosure, connector after composantes'
events=json.loads((O/'pending_events/scan005.json').read_text())
ids={'R1':['M005-P','M005-I'],'R2':['M005-I'],'R3':['M005-X','M005-I']}
for who in r:
 for check,sid in zip(r[who]['checks'],ids[who]):
  events.append({'statement_id':sid,'date':r[who]['end_utc'][:10],'who':f'GPT-6 Astra Pro; effort inherited/not exposed; scan005 {who}','type':'targeted proof check','outcome':check['statement']+' '+check['reasoning']+' '+check['outcome']})
notes="""The page continues the definition of a rectilinear realization and states that a finite graph admits one precisely when it is strict, with realization in R³. Two vertex-position conditions exclude unwanted points on segments and intersections between segments with four distinct endpoints. It then defines connectedness and graph sums, introduces polygonal graphs/contours through the degree-two condition, labels a duality, and states classification of nonempty connected contours by cardinality 2 ≤ c ≤ aleph₀, with strictness excluding 2. Archive sheet number 4 is recorded only as a comment; no date is written here.

The opening word is arc, not H's arête; ∃1 has an uninterrupted numeral stroke, not an exclamation mark. The first barred endpoint pair contains a comma, as do the added four-point pairs. The existence-line operator is left as réll | réel and its relation to E is a hook with a blunt shaft, not a completed right arrow. The letter after qui is f. These readings were decided on their strokes; the expected realization map did not decide them. Four earlier C doubts are resolved: canceled a, the blunt hooked shaft, f, and Dualité. Nine earlier doubtful loci remain, and sss | ssi is newly marked. The connectedness insertion is conn | conn. | connexes; grammar does not supply its ending.

A dark hook over the l of prolonge may be an authorial question mark. That alternative is preferred but not asserted as certain, and is located over l rather than after the whole word. No other explicit check phrase or question was found. The circled multi, the shared heading/formula baseline, and the left-margin arrow and pencil drawing are preserved. Insertion enclosures at et disjoints and conn are recorded as insertion cues. Small patches in the drawing are reproduced without interpreting them as graph vertices.

Mathematical checks: R1 checked the equivalence of the first pair condition with no three distinct points being collinear (M005-P). R3 checked that the two conditions exclude unintended straight-edge intersections, including the shared-endpoint case (M005-X). Each reader checked the final cardinal comparison c ≠ 2 iff c ≥ 3 within the written range (M005-I). These checks did not settle an ambiguous glyph.

The main reader separately tested the uniqueness interpretation (M005-U/M005-A). If the preceding definition requires only an embedding whose edge images are segments, uniqueness as a parametrized map is false: t and t² on [0,1] fix the endpoints and have the same segment image. If the map must be affine on each coordinate edge, interpolation uniquely determines it; the stated nonintersection conditions make it injective, and finiteness gives the compact-to-Hausdorff embedding conclusion. This is a conditional qualification, not a definitive claim that the author intended the weaker definition, and no affine condition is inserted into the text. The main reader also checked the connected degree-two classification (M005-C), under the preceding distinct-endpoint convention: following the unique continuation gives a finite cycle, including the two-parallel-edge case, or a two-sided infinite path; connectedness exhausts the graph. The remaining existence assertion and duality heading were read, not independently proved. Full check types and arguments are in CHECK_EVENTS.tsv.

H's declared number-field encoding by bold macros is equivalent to C's blackboard style and produces no collation row. Likewise the archive-page offset is not a textual discrepancy."""
views=[f'readings/scan005/R3/crops/{s}.png' for s in ['01_before_soit','02_overwritten_E','03_raised_parenthesis','04_before_xy','05_distincts_insertion','06_pair_condition']]
views+=['readings/scan005/R2/crops/06_existence_formula.png','readings/scan005/R3/crops/09_before_prolonge.png']
views += [f'readings/scan005/R1/crops/{s}.png' for s in ['09_prolonge','16_realis_phrase','10_connex_ending','07_margin_drawing','11_deleted_reunion']]
views += [f'readings/scan005/R3/crops/{s}.png' for s in ['13_dualite','14_deleted_donc','15_conn_insertion','16_strict_condition','18_polygonales_ending']]
views+=['readings/scan005/R1/crops/14_connait.png']
views += [str(p.relative_to(O)) for p in sorted((O/'crops/scan005').glob('*.png'))]
assert len(views)==33 and len(set(views))==33
D={'base':'R1','text_file':'decisions/scan005_final.tex','findings':fs,'inventory':inv,'notes':notes,'events':events,'unresolved':un,'main_crop_count':14,'main_crop_views':views}
(O/'decisions/scan005.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
print('scan005 decision:',len(fs),'loci;',len(un),'unresolved;',len(events),'events')
