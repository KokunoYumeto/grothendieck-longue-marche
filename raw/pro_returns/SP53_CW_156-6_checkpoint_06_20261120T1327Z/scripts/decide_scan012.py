"""Main reader's ink-based scan012 decisions. Do not rerun after commitment."""
import copy,json,re
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan012.json'
if p.exists() and json.loads(p.read_text()).get('committed'):raise SystemExit('Already committed')
rs=[json.loads((O/f'readers/scan012/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
m1=[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,23,24,24,25,26,27,28,29,29,30,31,32,33,34,35,36,37]
m3=[0,1,None,2,3,4,5,6,7,8,9,10,11,12,13,None,14,15,16,17,18,19,20,20,21,21,22,23,24,25,26,26,27,28,29,30,31,32,33,34]
rows=[]
for i,x in enumerate(b):
    r=copy.deepcopy(x);r['final']=r.pop('reading');r['mathematical']=False
    r['readers']={'R1':a[m1[i]]['reading'],'R2':x['reading'],'R3':c[m3[i]]['reading'] if m3[i] is not None else 'Two opposed zigzags with four free diagonal tips, as in reading.tex.'}
    rows.append(r)
def rp(reader,name):return f'readers/scan012/{reader}/{name}.jpg'
def main(name):return f'crops/scan012/{name}.jpg'
def put(i,**kw):rows[i].update(kw)
margin=rp('R1','crops/03_slanted_correction')
glyph=rp('R1','crops/02_diagram_compatibility')
bottom=rp('R3','09_bottom_redaction')
put(0,crop=rp('R1','crops/01_diagram_frame'),evidence='Main sees clear white gaps at both left corners, between tapered ends, and a short top-edge overrun beyond the right side. R1/R2 preserve the overhang; R3 omits it in the construction. Adopt R2 geometry. H is credited for its explicit enclosure note, which does not assert closed corners.')
put(1,c='Two opposed zigzags, without an upright.',final='Two opposed zigzags with a heavy extra upright; explicit live/canceled alternatives for the upright, overlaid at its observed position.',crop=glyph,evidence='Four free diagonal ends and central crossings remain visible around a thick almost vertical additional stroke. Retracing does not establish whether that upright is live or canceled. Main retains R1/R3 state alternatives against R2’s resolved live upright and uses R3’s overlaid construction; no earlier letter is invented.',mathematical='The diagram occurrence retains an extra upright of uncertain live/canceled state; the two prose occurrences do not have it.')
put(2,crop=main('01_body_compatibility'),evidence='Main sees two opposed zigzags enclosing a small diamond, with four free diagonal ends. There are no horizontal caps and no upright. The local form agrees with C and the readers, rather than H’s between sign.')
put(3,crop=margin,evidence='The compressed c and ar course is visible after non réflexive. Main confirms car, which H omits.')
put(4,crop=margin,evidence='The membership sign has an open curved body and middle bar. The detached upper curve aligns with punctuation on the preceding slanted line, not with a prime attached to membership. Main resolves ordinary membership as R2/R3, against R1’s retained alternative.')
put(5,crop=margin,evidence='A broad curved entry rises through two peaks and a rounded trough. The letter is M but the printed ordinary/calligraphic alphabet remains underdetermined. All readers’ first-occurrence alternatives are retained.')
put(6,crop=margin,evidence='No independent point follows M before Pour starts on the next slanted line. Main confirms C and the readers against H’s supplied period.')
put(7,crop=margin,evidence='The compressed a/v/o course and final i/r are recoverable between Pour and une. Main confirms avoir against H’s unreadable marker.')
put(8,crop=margin,evidence='The tall l and t and continuing ion course spell the full relation. It does not stop at rel.; main keeps the full written word.')
put(9,crop=margin,evidence='The il and f stems, reduced faudrait and accented écrire course are visible. Main confirms il faudrait écrire, not H’s unreadable opening and avoir écrit.')
put(10,crop=margin,evidence='An F stem and arms and a separate left-pointing triangular wedge survive under the cancellation. Main resolves both signs and preserves their struck state.')
put(11,crop=margin,evidence='Two separate rules run beneath ou. Main keeps the double underline already recorded by C.')
put(12,crop=margin,evidence='A distinct isolated point follows the final F=F. Main confirms the terminal punctuation omitted by H.')
put(13,crop=margin,evidence='Only one live F trianglelefteq F occurs, as the beginning of the complete proposed definition. The crop includes the end of the note; no second standalone copy appears below it. H’s specific assertion of a duplicate is not supported.',mathematical='The marginal proposed definition literally uses F in every operand position; no G is supplied.')
put(14,confidence='high',crop=rp('R3','03_la_relation_start'),evidence='A large live L followed by a is intact. Neighboring oblique strokes belong to the slanted marginal note; no independently canceled Les belongs to the body opening.')
put(15,crop=main('02_reflexive_compatibility'),evidence='Main sees four free diagonal ends around a central diamond. The crossing is dark but has no extra upright and no horizontal caps. The opposed-zigzag form is preserved.')
put(16,final=r'\inserted{\unsure{de plus|de plus,}}',against_C=True,against_H=True,confidence='medium',crop=rp('R3','04_de_plus_insertion'),evidence='The long curved leader attaches the inserted words. A detached short final curl could finish s or form a comma; its letter-height position favors no comma first. Main retains R3’s alternatives against R1’s resolved omission and R2’s resolved comma.')
put(17,crop=rp('R3','05_family_f'),evidence='A long left-swept curved cap, crossing middle arm and bent foot identify the recurring family F. The exact typeface is uncertain. Main retains the established mathcal/fraktur pair as R1/R2, having compared R3’s additional mathscr candidate; no different drawn form warrants a new alphabet here.')
put(18,confidence='medium',crop=rp('R3','06_element_abbreviation'),evidence='Two accents, a tall l, a flattened extended middle and terminal upright are visible. The middle cannot be segmented securely as abbreviated mt or fully reduced ment. Main retains the explicit alternatives without expansion.')
put(19,crop=rp('R3','06_element_abbreviation'),evidence='Below the small slashed oval, the family F has the recurring curved cap, crossed middle and bent stem. Main uses the first candidate of the explicit initial alphabet doubt. Emptyset versus varnothing alone is not counted as a reading difference.')
put(20,crop=main('03_emptyset_display_subscript'),evidence='The F subscript has a long top arm extending left across its stem, a middle cross-stroke and a bent leftward foot, unlike the adjacent ordinary F. Use the first family-alphabet candidate. Emptyset/varnothing syntax is not itself a discrepancy.')
put(21,crop=rp('R1','crops/07_remarques_initial'),evidence='The initial L has a tall straight upright and a basal rightward foot, followed by reduced es. Main confirms capital Les against H’s lowercase word.')
put(22,crop=main('04_remarques_family'),evidence='The M has a long curved entry, two peaks and a rounded trough, repeating the first uncertain alphabet form. Main uses its first candidate here.')
put(23,crop=main('04_remarques_family'),evidence='The family F has a sloping cap extended across its stem, a middle crossbar and a bent lower tip. Main uses the first candidate of the marked family-alphabet alternatives.')
put(24,crop=rp('R2','06_display_120'),evidence='The initial M has the long rising entry and two peaks of the recurring form. Main uses the first candidate of its first-occurrence alphabet doubt.')
put(25,crop=rp('R2','06_display_120'),evidence='The family F after membership has a crossed upper course and short curled foot, distinct from ordinary F_i later in the display. Main uses the established first alphabet candidate.')
put(26,crop=rp('R2','06_display_120'),evidence='The t is visibly raised after str and a distinct point follows. Main preserves str with superscript t and point, without expanding it to H’s strict.')
put(27,crop=rp('R2','06_display_120'),evidence='A high S loop begins the operator, followed by reduced u and descending p; a dotted i is centered below. Main confirms capital Sup. The i indices and terminal X≤F_i are also clear; retracing does not establish a distinct canceled predecessor, and H’s surcharge note is credited.')
put(28,crop=rp('R1','crops/09_deleted_before_dautre'),evidence='An E-like curve and crossed following upright favor Et. Dense strokes still permit En. The group is too short for H’s whole D’autre. Main retains the canceled alternatives, with low confidence.')
put(29,crop=main('05_before_121_M'),evidence='The long curled entry rises into two tall peaks and a rounded low trough. Main confirms the recurring M and uses its first alphabet candidate.')
put(30,crop=main('06_display_121_family'),evidence='The initial M has a curved entry, two peaks and rounded trough. Main keeps the first candidate of the first-occurrence alphabet uncertainty.')
put(31,crop=main('06_display_121_family'),evidence='The family F has a looped cap, a crossing middle arm and a bent lower stem. It repeats the established form, represented by the first alphabet candidate.')
put(32,crop=main('07_before_122_family'),evidence='The nearby ordinary F has right-facing arms. The family F has a looped cap crossing the stem and a hooked lower course. Main keeps the first family-alphabet candidate.')
put(33,crop=rp('R2','08_deployement'),evidence='The long medial y descender is clear. Adequate blank space above the initial e shows no separate acute; the nearby tall loop is connected to d. Main adopts R2’s unaccented deployement against R1/R3’s accented reading from the halves, without modernizing y to i.')
put(34,crop=main('08_display_122_M'),evidence='Two tall peaks, a narrow deeper trough and long rising entry identify the same M, here more heavily retraced. No index or bar is present. Main uses the first alphabet candidate.')
put(35,kind='other',crop=rp('R2','09_final_family_f'),evidence='The broad arched cap, crossed middle and fully closed lower foot identify the family F, not an ordinary operand. Main resolves C’s local letter-identity doubt; the separate initial font doubt still governs typography. H’s note accurately records the literal collection letter, but its displayed formula emends it to ordinary F. The note is credited and the display difference recorded.',mathematical='The last operand of (1.22) is the family F in the ink, despite the preceding prose introducing deployment of an ordinary F. No expected mathematical correction is substituted.')
put(36,crop=rp('R2','10_label_123'),evidence='The separator is a short descending comma; the final numeral has two rightward bows and reads 3. Main resolves the literal label (1,23).')
put(37,final=r'\unsure{équivalent|equivalent}',against_C=True,crop=bottom,evidence='The q descender and later l/t course support the word, but the cancellation rule and inserted writing above obstruct a separately attributable acute. Main retains R1’s accent/no-accent alternatives against R3’s resolved word and R2’s unelaborated doubt.')
put(38,confidence='medium',crop=bottom,evidence='The inserted adjective is a short low sequence of humps and terminal curls. The ending can be a or es, and there is no tall l or sufficiently long course for H’s minimales. Main retains minima/minimes with the whole replacement above the struck clause.')
put(39,crop=rp('R2','12_final_dy'),evidence='The looped d has a long low exit; a separate raised apostrophe precedes y, whose two short upper arms lead into a long descending tail. There is no intervening e or s. Main confirms d’y.')
# Separate the individual alphabet occurrences bundled in R1/R3's rows.
for i in [22,24,29,30,34]:rows[i]['readers']={k:r'\mathcal{M}' for k in ['R1','R2','R3']}
for i in [23,25,31,32,35]:rows[i]['readers']={k:r'\mathcal{F}' for k in ['R1','R2','R3']}
rows[4]['readers']['R3']=r'\in'
rows[13]['readers']['R3']='Only one final formula beginning F trianglelefteq F; no second independent copy.'
extra=copy.deepcopy(a[2]);extra['final']=extra.pop('reading');extra['readers']={'R1':extra['final'],'R2':'F','R3':'F'}
extra.update(crop=glyph,mathematical=False,evidence='Two distinct vertical tracks enclose a narrow white channel and join below. Main retains R1’s ordinary retraced F/blackboard F alternatives, ordinary F first, against C/H/R2/R3’s resolved F.',confidence='medium')
ordered=rows[:2]+[extra]+rows[2:]
for i,r in enumerate(ordered,1):r['id']=f'012-{i:02}'
# R3 supplies explicit overlaid state alternatives and correct ordinary spacing;
# R2 supplies the observed frame overhang. These are representations of decisions above.
tex=(O/'readers/scan012/R3/reading.tex').read_text()
bt=(O/'readers/scan012/R2/reading.tex').read_text()
start=tex.index('execute at end picture={');end=tex.index('}]',start)+2
bs=bt.index('execute at end picture={');be=bt.index('}]',bs)+2
tex=tex[:start]+bt[bs:be]+tex[end:]
diagram,rest=tex.split('\nParmi',1)
diagram=diagram.replace(r'\draw (-.38',r'\draw[line width=.6pt] (-.38').replace(r'\draw (.34',r'\draw[line width=.6pt] (.34').replace(r'\draw (-.12',r'\draw[line width=.6pt] (-.12')
assert '}}} F \\&' in diagram
diagram=diagram.replace('}}} F \\&',r'}}} \unsure{F|\mathbb{F}} \&')
tex=diagram+'\nParmi'+rest
tex=tex.replace(r'\unsure{\mathcal{F}|\mathfrak{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}')
tex=tex.replace('son déployement','son deployement')
tex=tex.replace(r'\deleted{la structure, il est équivalent}',r'\deleted{la structure, il est \unsure{équivalent|equivalent}}')
(O/'decisions/scan012_final.tex').write_text(tex)
cd=copy.deepcopy(rs[1]['c_doubts'])
links=[4,10,17,18,28,33,35,36,37,38]
for j,i in enumerate(links):
    r=rows[i];cd[j].update(reading=r['final'],evidence=r['evidence'],crop=r['crop'],disposition='retained' if j in [2,3,4,8,9] else 'resolved')
inv=copy.deepcopy(rs[0]['inventory'])
inv[17]['first_words_or_objects']='puis, pour F in family F, son deployement'
inv[8]['first_words_or_objects']='de plus / de plus,'
inv.insert(5,copy.deepcopy(rs[1]['inventory'][4]))
frame=copy.deepcopy(rs[2]['inventory'][2]);frame['element']='oblique enclosure within implication diagram';frame['first_words_or_objects']='Two left-corner gaps and small top-right overhang'
inv.insert(2,frame)
assert len(inv)==26
notes={'content':'The page presents six relations in implication diagram (1.18), initially classes four as orders and two as symmetric, and discusses reflexivity. A slanted authorial correction rejects incidence as an order on the whole family. Formula (1.19) characterizes self-parallelism by the empty figure. Remark a) describes recovery of incidence from order by strict irreducibles and (1.17), then recovery of the distinguished family, deployment and order from incidence through (1.21), (1.22) and the comma-numbered (1,23). The concluding sentence revises its wording toward the data fixing an atelier and continues off the sheet.',
'math_reading_decisions':['All five double arrows point downward. The enclosure has two left-corner gaps and an upper-right overhang. The diagram compatibility sign has an additional upright of uncertain live/canceled state; both prose signs have only the opposed zigzags.','The marginal membership is ordinary in; the apparent upper prime belongs to the preceding slanted line. The proposed reflexive repair literally repeats F in every operand position, and no G is supplied.','Main performed a limited conditional check using the committed definition (1.17): if A triangleleft B means A≤B and A in M, and ≤ is an order, then incidence is transitive and F triangleleft F iff F in M. It is reflexive on M and on the entire family iff M is that family. Properness of M and the order axioms themselves were not established.','R3 and main checked that the literal F/F disjunction in the proposed repair is true on the diagonal because F=F. The displayed formula does not by itself specify a relation on unequal operands. This does not authorize a textual repair.','The final letter of (1.22) is visibly the family F with a closed returning foot. H’s explanatory note observes this literal form, while its display substitutes ordinary F. The transcription preserves the literal family letter.','Capital Sup, raised t in str^t., all i indices, the final X≤F_i and the open inclusion in (1,23) are preserved. H’s note about retracing of the final inequality in (1.20) is credited; no separate canceled predecessor is established.','No proof of the full implication diagram, self-parallelism criterion, strict-irreducibility reconstruction, deployment reconstruction or order/inclusion equivalence was performed.'],
'author_doubts':["Non, triangleleft n’est pas rel. d’ordre, elle est transitive mais non réflexive, car F triangleleft F iff F in M.","Pour avoir une relation d’ordre il faudrait écrire [canceled F triangleleft] F trianglelefteq F déf iff F triangleleft F ou F=F.",'No separate à vérifier or question mark qualifying a proof is reported on this page.'],
'titles_dates_counts':'Manuscript page 11. Underlined Remarques, subdivision a). Display labels (1.18), (1.19), (1.20), (1.21), (1.22), literal (1,23), and internal reference (1.17). The text counts six relations and initially four orders, challenged by its margin. No date, title sheet, total page-count statement or legible archive pencil number is reported.'}
events=[]
for i,r in enumerate(rs,1):
    for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan012 R{i}'))
for sid in ['scan012-(1.18)','scan012-(1.19)','scan012-(1.20)-(1,23)']:
    events.append({'statement_id':sid,'type':'carried as background without fault found','outcome':'Read as the author’s assertion; no mathematical verification of this displayed claim or reconstruction was performed.','who':'GPT-6 Astra Pro; effort not exposed; main reader; scan012'})
events.append({'statement_id':'scan012-margin-transitivity-and-diagonal','type':'targeted proof check','outcome':'Using committed (1.17), A triangleleft B iff A≤B and A in M, and assuming ≤ is an order: from A triangleleft B and B triangleleft C obtain A≤C and A in M, hence A triangleleft C. Reflexivity of ≤ gives F triangleleft F iff F in M. Thus incidence is reflexive on M and on the entire family iff M equals it. The assumed order properties and properness of M were not proved.','who':'GPT-6 Astra Pro; effort not exposed; main reader; scan012'})
events.append({'statement_id':'scan012-margin-proposed-order-diagonal','type':'targeted proof check','outcome':'The literal disjunction F triangleleft F or F=F is true for every F by equality reflexivity. Its equivalence defines only diagonal values; no off-diagonal relation follows from this formula alone. No F/G correction was made.','who':'GPT-6 Astra Pro; effort not exposed; main reader; scan012'})
unrows=[rows[i] for i in [1,5,16,17,18,28,37,38]]+[extra]
un=[{'place':r['place'],'reading':r['final'],'alternatives':'The unresolved letter, alphabet, punctuation or live/canceled-state alternatives are explicit in the transcription.','confidence':r['confidence'],'evidence':r['evidence']} for r in unrows]
d={'scan':12,'mspage':'11','folder':'J156-6-02','filename':'J156-6-02_156-6_scan012.tex','brief':'v006','committed':False,'adjudicated_all':True,'differences':ordered,'adjudications':[],'c_doubts':cd,'s_rows':[],'inventory':inv,'notes':notes,'check_events':events,'unresolved':un,'abbreviations':rs[0]['abbreviations']}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert len(json.loads((O/'decisions/scan012_main_views.json').read_text()))==23
print(json.dumps({'scan':12,'loci':len(ordered),'C':sum(r['against_C'] for r in ordered),'H':sum(r['against_H'] for r in ordered),'inventory':len(inv),'C_doubts':len(cd),'resolved':sum(x['disposition']=='resolved' for x in cd),'remaining':len(un)},ensure_ascii=False))
