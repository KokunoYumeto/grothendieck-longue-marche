from pathlib import Path
import json, copy

O=Path('out'); stem='C123-01_123_scan018'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
T={r:(O/'readers'/stem/r/'reading.tex').read_text() for r in R}
r1=f'readers/{stem}/R1/crops/'; r2=f'readers/{stem}/R2/crops/'; r3=f'readers/{stem}/R3/crops/'; rc=f'decisions/rootcrops/{stem}/'
spec=dict(stem=stem,base_reader='R1',brief='reader_v06.md',main_new_crops=11,text_edits=[],difference_overrides={},additional_differences=[])
# R1 supplies the granular difference list; R3 supplies most of the physical text layouts.
# Every replacement below is an explicit root decision from the compared returns and viewed crops.
t=T['R3']
def replace(old,new):
 global t
 assert t.count(old)==1,(old,t.count(old))
 t=t.replace(old,new)
replace(r'G_{\unsure{o|0}}',r'G_o')
replace(r'\handwritten{\unsure{\Gamma\'|\Gamma}}'.replace("\\'","'"),r'\handwritten{\Gamma}')
spot=r'\unsure{\tikz[baseline=-.45ex]{\fill[rotate=-35] (0,0) ellipse (.35pt and .65pt);}}'
replace(r'associé \unsure{.} $\operatorname{Cent}',r'associé '+spot+r' $\operatorname{Cent}')
article=T['R2'][T['R2'].index('théorie des filtrations d')+len('théorie des filtrations '):T['R2'].index(' foncteurs fibres,')]
replace(r'\unsure{da|de}',article)
# Keep the two distinct lower traces of the ou encore enclosure.
old=t[t.index('\\begin{tikzpicture}[baseline=(p.base)'):t.index('\nil revient au même')]
new=T['R1'][T['R1'].index('pour $P$'):T['R1'].index(' il revient au même')]
assert new.startswith('pour ')
replace('pour\n'+old,new)
# Restore the source's two staggered handwritten rows and paired oblique strokes.
old=t[t.index('\\begin{tikzpicture}[baseline=(mark)'):t.index('\\deleted{(en fait,')]
new=T['R1'][T['R1'].index('\\inserted{\\handwritten{\\begin{tikzpicture}[baseline=(attach)]\n  \\node[anchor=west,inner sep=0pt,font=\\small] at (0,.42)'):T['R1'].index('\\deleted{(en fait,')]
replace(old,new)
# The typed replacement deux is physically above the cancelled un homo.
old=r'\deleted{un homo}\inserted{deux}'
start=T['R2'].index('\\begin{tikzpicture}[baseline=(old.base)')
end=T['R2'].index('morphismesde schémas',start)
replace(old,T['R2'][start:end])
spec['text_edits']=[dict(old=T['R1'],new=t)]

def ov(n,**kw):spec['difference_overrides'].setdefault(f'D{n:02}',{}).update(kw)
root_crops={1:'heading',2:'heading',7:'conjugacy_insertion',9:'deleted_un',11:'Hom_T_index',13:'maximal_tore_G_index',14:'outer_automorphism_formula',15:'outer_automorphism_formula',16:'outer_automorphism_formula',24:'orbit_addition_layout',26:'orbit_addition_layout',40:'Dynkin_i_index',49:'de_G_insertion'}
for n,name in root_crops.items():ov(n,crop=rc+name+'.png')
ov(3,final="et ``exactes',cette",c_changed=False,h_changed=True,readers="R1: two closing strokes; R2: one; R3: one. Root: one closing apostrophe, following C.",evidence="Two opening strokes are visible. The comma in the typed line above descends beside the closing quotation; it is not a second closing apostrophe. The lower comma after the single closing stroke is separate. The asymmetric source quotation is retained.",crop=r2+'01_exactes_derniere.png')
ov(4,readers=r'R1: \unsure{dernière}; R2: same; R3: same. Root retains the whole-word doubt, including crowded ending/accent.',evidence='The terminal impressions and the accent region overlap other ink. The word remains a tentative reading; neither a clean accent nor a separately readable predecessor is asserted.')
ov(5,readers='R1: enclosure and leader drawn after a linearized body; R2: enclosure drawing; R3: addition above the tensoriel body label with joined leader. Root preserves the latter relative layout.')
ov(7,readers='R1, R2 and R3: typed conjugacy addition with a handwritten lower curve. Root confirms the connected curve and mixed medium.',evidence='Uniform serifed typewriter letters spell conjugaison, rationelle sur k, de. The thin line runs below them, turns upward after de, and drops at the left before telles. H’s blanket handwritten description does not fit these words.')
ov(8,final=r'i plus a doubtful o/l overlay, followed by \deleted{\unsure{n}}',readers=r'R1: o/l overlay and unidentified crossed impression; R2: o/l overlay plus cancelled illegible character; R3: o/l overlay plus cancelled tentative n. Root retains the tentative n and does not order the o/l impressions.',evidence='The i is separate. A tall l stem and low o oval coexist in the next cell. At the right, x strokes mask a separate cell with n-like upright and shoulder remnants; its reading remains low confidence.',confidence='low')
ov(10,readers=r'R1: G_o; R2: G_{\unsure{o|0}}; R3: G_{\unsure{o|0}}. Root resolves the typed o.',evidence='The ring has lowercase height, matching the o in ordinary typed words. The source’s full-height numeral 0 in car.k=0 is taller; the typewriter subscripts are lowered, not reduced type. This is a shape comparison, not a numerical inference.')
ov(11,readers='All three use T_o; R2/R3 carry an o/0 family doubt from the first occurrence. Root resolves this typed ring as lowercase o.',evidence='The lowered ring has the same x-height as the o in Hom, and is shorter than the capital T. The formula retains the underlined G_m, quotient slashes and W=M/W.')
ov(12,final=r'T_o=M\mathbin{\text{\textcircled{x}}}\underline{G}_m',readers=r'R1: circled x | otimes; R2: circled x; R3: circled x. Root resolves the serifed x over an oval; the typed index is o.',evidence='The x has projecting serifed feet and crossing diagonals, independently visible within the oval. The sign is reproduced literally as circled x; the adjacent lowered o is lowercase-sized.',confidence='high')
ov(13,readers='All three: G_o, with R2/R3 carrying the earlier index doubt. Root resolves the lowercase-sized typed o.',evidence='A lowered lowercase-height oval follows G. Its height is visibly less than the capital’s; no numeral-zero normalization is used.',confidence='high')
ov(14,evidence='The raised Gamma has a horizontal head with a descending attached terminal. A distinct long curve descends before de and turns up beside the glyph. The curve is retained in TikZ.')
ov(15,evidence='The separate typewriter cells read A-u-e-x-t. There is no t between u and e; the final t is clear.')
ov(16,readers='R1: G_o=E_o; R2/R3: same first candidate under their initial o/0 doubt. Root resolves both typed o indices.',evidence='Both lowered rings have lowercase x-height, matching the typed o in the other cropped formulas. Their shapes are not those of the taller numeral 0.',confidence='high')
ov(18,readers='All three: serifed circled x and separately underlined Z,R. Root confirms both local forms.',evidence='The sign combines an oval and a crossing typewriter x with serifs. Separate low rules lie under the ordinary Z and R. H’s bold letters omit those rules.')
ov(19,final=r'\handwritten{\Gamma}',c_changed=True,h_changed=False,readers=r'R1: \unsure{\Gamma|\Gamma\prime}; R2: Gamma; R3: \unsure{\Gamma\prime|\Gamma}. Root resolves plain Gamma.',evidence='The downward right stroke is continuously attached to the horizontal head. No detached prime is present. The page’s separately written c-primes have detached marks, unlike this terminal.',confidence='high')
ov(20,final=r'\unsure{schéma}',c_changed=False,h_changed=True,readers=r'R1: schéma resolved; R2: \unsure{schéma}; R3: \unsure{schéma}. Root retains the edge doubt.',evidence='The last a meets the dark image boundary and loses its rightmost contour. The visible left contour supports schéma but does not make the clipped letter complete.',confidence='medium')
ov(21,readers=r'R1: underlined varnothing; R2: \unsure{\underline{\varnothing}|\underline{\phi}}; R3: underlined varnothing. Root resolves the slashed-oval physical form.',evidence='A closed oval is crossed by a distinct oblique slash extending below-left and above-right; the underline is separate. There is no vertical phi stem. The chosen glyph describes the form without assigning an empty-set meaning.')
ov(23,readers='R1, R2 and R3: raised wavy sim plus separate nearby insertion strokes. Root keeps the wavy stroke, short slanting bar and S-shaped connector distinct.',evidence='The raised wave lies above a short rising line crossed by the separate thin curved leader. They are not collapsed into a new simeq sign.')
ov(24,evidence='The typed addition has one n in rationelle. It is not changed to the doubled n in H.')
ov(26,evidence='The interlinear body is typed, with handwritten il, raised sim and soit c-prime. Its long lower curve turns down just after the live semicolon following paraboliques and curls up after the inserted comma. The physical relation is reproduced in TikZ.')
ov(28,readers='R1: underlined slashed oval plus two lower curved traces; R2: same preferred glyph with first-occurrence phi doubt, one curve drawn; R3: definite slashed oval, one curve drawn. Root preserves both visible traces.',evidence='The glyph has an oblique slash through an oval and an independent underline. Beneath the words, a dark lower enclosure and a fainter parallel trace are both visible; their correction order is not assigned.')
ov(31,final='A doubtful small oblique spot before Cent(i), drawn in TikZ; the following full stop and handwritten parenthesis are retained.',readers=r'R1: \unsure{.}; R2: doubtful graphic spot, unclassified; R3: \unsure{.}. Root preserves the graphic without declaring punctuation.',evidence='The isolated tiny oblique mark before C is lighter, smaller and higher than the definite round full stop after Cent(i). Its function remains uncertain.',crop=r2+'13_cent_point.png',confidence='low')
ov(33,readers='All three identify raised typed deux; R2 explicitly places it over cancelled un homo in TikZ. Root uses that vertical placement.',evidence='The regular serifed word deux is on a raised line above the cancelled un homo; morphismesde remains on the baseline.')
ov(35,readers='R1/R3: underlined slashed oval; R2: same form with its first-occurrence alphabet doubt. Root resolves the physical glyph consistently with the other two occurrences.',evidence='The first arrow points right to an oval crossed diagonally with an independent underline. The commas, including the final display comma, already present in both witnesses are retained and are not counted as differences.')
ov(37,final='d followed by a doubtful a/e overlay in TikZ, with no impression order asserted.',c_changed=True,h_changed=True,readers=r'R1: \unsure{da|du}; R2: a/e overlay after d; R3: \unsure{da|de}. Root preserves the overlapping a/e contours graphically.',evidence='The second cell has a closed upper counter, an e-like horizontal trace and a lower a-like bowl/right foot. A clean open u is not supported. The apparent two contours are preserved with doubt, without deciding their temporal order.',crop=r3+'15_da_foncteurs.jpg',confidence='medium')
ov(40,readers='All three use fi_o; R2/R3 carry their earlier o/0 family doubt. Root resolves this lowered typed ring as o.',evidence='The ring below i has ordinary lowercase height relative to the tall f/i, matching the other typed o subscripts; it is not resized zero.',confidence='high')
ov(41,final='Baseline non vide, with the separately raised et non réduit à un point, and its connector.',readers='R1 serializes the baseline comma after the inserted phrase; R2 retains it before the insertion; R3 draws it on the non vide baseline. Root keeps R3’s physical baseline position.',evidence='The typed comma immediately follows vide below the start of the curved enclosure. The added phrase has its own terminal comma. The connector does not cancel either mark.')
ov(46,readers=r'R1: first handwritten Z_{\unsure{o|0}}; R2/R3: Z_o under their first typed-index doubt. Root distinguishes handwriting from resolved typewriter o and retains this local doubt.',evidence='The pen-written small ring has no typewriter-height comparator that determines o versus zero. Its first occurrence in the handwritten note carries the residual doubt.')
ov(47,readers='All three use the first candidate Z_o at this recurrence. Root carries the handwritten-ring doubt from the first Z in the same note.',evidence='A small handwritten ring sits below Z after ces. It matches the first handwritten index, whose o/0 uncertainty is marked once.')
ov(48,crop=r1+'19_homogene_stabilisateur.png',readers='R1/R2 preserve two staggered handwritten rows; R3 linearizes the words and draws the pair of strokes separately. Root restores the two rows and both entry strokes.',evidence='The note begins to the right over the first cancelled line; dimension, semi-simplicité). resumes much farther left above the next line. Two oblique strokes stand after G. Existing R1 crops 19, 20 and 21 jointly show the complete arrangement.')
ov(49,evidence='The handwritten de G sits above the unipotents/dont gap. A thin line runs below it, turns up at the right, and curves down at the left before dont.')

# Two loci absent from R1's difference list were independently reported by R2 and R3.
for source_id,new_id,crop in [('D07','ROOT-01','initial_c_caret.png'),('D13','ROOT-02','first_deleted_homomorphisme.png')]:
 d=copy.deepcopy(next(x for x in R['R2']['differences'] if x['id']==source_id))
 d.update(id=new_id,final=d.pop('reading'),crop=rc+crop,marked_in_H='no')
 if source_id=='D07':
  d.update(readers='R1 retains raised c but omits its graphic leader; R2 and R3 draw the bent V-shaped leader. Root confirms and retains the latter.',evidence='The open c stands above a curved left arm descending to the word gap and a long rising right arm. The joined insertion mark is drawn, not replaced by a bare insertion macro.')
 else:
  d.update(readers='R1, R2 and R3 all retain deleted homomorphisme in their complete readings. R1 omitted this locus from its difference list. Root confirms the cancellation.',evidence='The h ascender, successive o/m forms, descender of p, second h, dotted i and final s/m/e remain legible beneath the full row of x overstrikes. H omits this first cancelled word, separately from the later cancelled map.')
 spec['additional_differences'].append(d)

cd=copy.deepcopy(R['R1']['c_doubts'])
for d in cd:
 p=d['place']
 if 'After stable par'==p:d.update(decision=r'Resolve \Gamma without prime.',evidence=spec['difference_overrides']['D19']['evidence'])
 if 'Right-edge' in p:d.update(decision=r'Retain \unsure{schéma}.',evidence=spec['difference_overrides']['D20']['evidence'],confidence='medium')
 if 'quotation' in p:d.update(decision="Retain et ``exactes',cette.",evidence=spec['difference_overrides']['D03']['evidence'],crop=r2+'01_exactes_derniere.png')
 if 'da|' in d['C']:
  d.update(decision='d plus a doubtful a/e overlay; no chronological order.',evidence=spec['difference_overrides']['D37']['evidence'],crop=r3+'15_da_foncteurs.jpg')
 if 'tensor-like' in p:d.update(decision=r'Resolve \mathbin{\text{\textcircled{x}}}.',evidence=spec['difference_overrides']['D12']['evidence'],confidence='high')
 if p=='rat/k); il':d.update(decision=r'Preserve i and o/l overlay, followed by \deleted{\unsure{n}}.',evidence=spec['difference_overrides']['D08']['evidence'],confidence='low')
 if p=='Automorphism name':d['crop']=rc+'outer_automorphism_formula.png'
 if p=='Three rationelle spellings':d['crop']=rc+'orbit_addition_layout.png';d['evidence']+=' Root also viewed the conjugacy and orbit-insertion crops; the agreed third occurrence was independently read in all three halves.'
 if p=='Opening Supposons fixé une classe':d['crop']=r2+'01_exactes_derniere.png'
spec['c_doubts']=cd
spec['remaining_doubts']=[
 dict(place='Exactness addition',reading='dernière',alternatives='crowded accent and terminal impressions; no separate predecessor recovered',confidence='medium'),
 dict(place='After rat/k); second cell',reading='o and l contours superposed',alternatives='chronology and intended live letter unresolved',confidence='low'),
 dict(place='After rat/k); next cancelled cell',reading='n',alternatives='underlying shoulders partly covered by x strokes',confidence='low'),
 dict(place='Cancelled homomorphism into T',reading='rightward arrow',alternatives='head covered by x overstrikes',confidence='medium'),
 dict(place='Right-edge schéma',reading='schéma',alternatives='final a clipped at image boundary',confidence='medium'),
 dict(place='Before Cent(i)',reading='small oblique graphic spot',alternatives='punctuation or incidental ink; unclassified',confidence='low'),
 dict(place='Before foncteurs',reading='d with a/e overlay',alternatives='a over e or e over a; order unresolved',confidence='medium'),
 dict(place='First handwritten Z in stabilizer note',reading='o',alternatives='0; recurrence uses o',confidence='medium')]

inv=copy.deepcopy(R['R3']['inventory'])
for d in inv:
 d['hand']=d['hand'].replace('handwritten','unnamed hand').replace('typed','typewriter')
 if d['element']=='Stable-par Gamma fill':d['first_words_or_objects']='Gamma, attached terminal without separate prime'
 if d['element']=='Isolated point before Cent':d.update(kind='drawing',first_words_or_objects='small oblique spot of uncertain function')
 if d['element']=='Stabilizer and structure note':d['first_words_or_objects']='de stabilisateur Z_o ...; / dimension, semi-simplicité). — two staggered rows'
 if d['element']=='Ou encore enclosure':d['first_words_or_objects']='dark enclosure and faint parallel trace, attached after P'
inv.extend([
 dict(sheet_kind='typescript',hand='typewriter',element='Live baseline comma after non vide',kind='text',position=[606,1718,624,1742],first_words_or_objects=', distinct from added phrase comma',transcribed='yes'),
 dict(sheet_kind='typescript',hand='typewriter overlapping impressions',element='Unresolved a/e overprint before foncteurs',kind='text',position=[1150,1370,1209,1414],first_words_or_objects='d with doubtful a/e overlay',transcribed='yes'),
 dict(sheet_kind='typescript',hand='unnamed hand',element='Grave accent in où',kind='insertion',position=[1375,1102,1398,1123],first_words_or_objects='grave above u',transcribed='yes')])
inv.sort(key=lambda d:(d['position'][1],d['position'][0]))
for d in inv:d['position']='whole-image box '+str(d['position'])
spec['inventory']=inv
spec['abbreviations']=R['R3']['abbreviations']
notes=(O/'decisions'/f'{stem}_pending_notes.md').read_text()
notes=notes[notes.index('The typescript turns'):notes.index('\nFinal notes must add')]
notes=notes.replace('Their check events are already logged and must not be duplicated on finalization.','The actual checks and their limits are recorded in CHECK_EVENTS.tsv.')
spec['notes']=notes+'''

**Ink decisions and literal forms.** The later Gamma has an attached descending terminal, not a detached prime. The three filtration glyphs have a closed oval crossed by an oblique slash with a separate underline, transcribed as underlined varnothing without an assertion that it denotes the empty set. Both tensor-like signs are visibly a typewriter x over an oval. Typed lowercase o indices are distinguished by height from the full-height numeral 0; the handwritten Z indices retain their own o/0 doubt. Mathematical familiarity did not decide these shapes. The “ou encore” addition attaches after P in the following explanatory parenthesis, as its curve shows. The exactness quotation has two opening strokes but one closing stroke; the nearby comma of the line above is not a second closing apostrophe. The baseline comma after “non vide” and the insertion’s own comma are both retained.

The source’s “fixé une classe”, three “rationelle” spellings, “Auext”, “morphismesde”, plural “foncteurs”, unaccented “fibres”, and “où un sous-groupe” remain literal. The l/o and a/e contours are preserved as doubtful overlays without a supplied chronology. A tentative cancelled n follows the former. The deleted “un homo” and d before en are resolved from their surviving strokes. The old homomorphisme passages, heading ending, underlined torseur and celle de remain transcribed beneath their cancellations. The two-row stabilizer question, its two oblique entry strokes and all connecting curves are preserved graphically. The small oblique spot before Cent(i) is not assigned a definite punctuation function.

The underlined heading is “Interprétations en termes de filtrations du foncteur oubli”, continuing with deleted “sur la catégorie”. This is an amended typescript with both typed interlinear text and pen additions, not a uniformly handwritten set of additions as H’s collective note says. No composition date, signature or total page count is visible. All three readers record the lower-left 17 as an archive-sheet number, retained only in a comment. The unfinished final sentence continues after “par la correspondance”. No external material was researched.
'''
spec['check_events']=[dict(statement_id='123-018-map-notation-consistency',who='GPT-6 Astra Pro; inherited effort (not exposed); '+stem+'/R2',type='used and rechecked in this run',outcome='Reader compared the displayed source/target names with the preceding definitions of ST_c, class-c filtrations and class-c-prime Levi pairs. This is a local notation comparison only, not a proof of representability or of either asserted canonical isomorphism.')]
# The eight actual root checks were logged at the time performed and are not duplicated.
spec['consequential']=[
 '123/018: Gamma-prime is resolved to Gamma by its connected terminal; the three filtration symbols are resolved as underlined slashed ovals.',
 '123/018: ou encore belongs after P in the explanatory parenthesis, rather than in the preceding class sentence as H places it.',
 '123/018: the stabilizer’s semi-simplicity is an authorial question; an explicit SL3 example gives a one-dimensional torus. The cancelled Isom-torsor claim fails in the separately checked product example.']
spec['workflow_note']='All three fresh readers completed the whole page and both halves once. A tool interruption paused them; each resumed the same page with retained context and explicitly reported no whole/half reload or lost context. Root compared the three complete texts and reports, viewed all 22 R1 crops, two existing R2 crops and one R3 crop, and made eleven new local crops only for loci not already cropped. One initial root heading display was truncated at the context boundary; the existing crop was successfully displayed on resumption, without recropping. A text-only auxiliary audit found the initial c leader and first cancelled homomorphisme missing from R1’s difference list; root independently inspected and included both. The baseline comma’s physical position and two-row stabilizer note required comparison of the complete readings, not just the row lists. The next brief clarifies that definite same-letter double striking follows the required mathbb convention, whereas mere darkness does not; quotation strokes must be separated from intrusive marks from adjacent lines. R1/R2/R3 performed reading checks only, not mathematical proofs; root’s separately documented checks are not credited to them.'

path=O/'decisions'/f'{stem}_spec.json'
path.write_text(json.dumps(spec,ensure_ascii=False,indent=2))
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(path)
print('Main-reader specification and preview saved; not yet finalized.')
