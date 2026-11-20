"""Explicit main adjudication of the three scan015 readings, after 26 local views."""
from adjudication import Page,O
import copy,json
p=Page(15,brief='v06')
first=r'e\unsure{\uline{s}|s}\uline{t algébriquement équivalent à zér}o'
second=r'\uline{est cohomologiquement équiva}le\unsure{\uline{n}|n}\uline{t à zéro}'
grif=r'\mathrm{Grif}\unsure{\handwritten{(}|\deleted{t}\handwritten{(}|t}'
p.text('R1',[
 (r'\deleted{Sous}',r'\deleted{Sousx}'),
 (r'Y_{\bar{\unsure{s|\deleted{t}s|\deleted{s}t}}}',r'Y_{\bar s}'),
 (r'\unsure{\uline{générique}|g\uline{énérique}}',r'gén\uline{érique}'),
 (r'a) \uline{et} b) \uline{de} 2)',r'a) e\uline{t} b) d\uline{e} 2)'),
 (r'\deleted{(Alors pour On suppose de plus $m=2n$}',r'\deleted{(Alors pour On suppose de plus $m=2n$x}'),
 (r'\uline{est algébriquement équivalent à zéro}',first),
 (r'\uline{est cohomologiquement équivalent à zéro}',second),
 (r'\mathrm{Grif}\unsure{\handwritten{(}|t}',grif),
 (r'Y_{\bar s_{\deleted{x}}}',r'Y_{\bar s_{\deleted{\unsure{x|k}}}}'),
 (r'\unsure{tensorisé}',r'tensoris\unsure{é}'),
 ('% The interlinear insertion is typed; a pen guide brings it before "soit".',
  '% The interlinear insertion is typed; a pen guide brings it before "soit".\n% The first Y-subscript repeats the s/t-shaped overlap marked at "soit"; later clean s cells do not inherit that overlap. The final x in each of Sousx and the cancelled m=2nx records a visible cancellation cell, not a recovered old lexical letter.'),
])
maps={
 1:(1,1,1),2:(2,2,2),3:(3,7,3),4:(4,8,4),5:(5,3,5),6:(6,9,6),
 7:(7,10,'peu importe; no point recorded'),8:(8,11,7),9:(9,13,9),10:(10,14,10),
 11:(11,4,11),12:(12,5,12),13:(13,6,13),14:(14,15,15),15:(15,16,14),
 16:(16,17,16),17:(17,18,17),18:(18,19,18),19:(19,20,19),20:(20,21,20),
 21:(21,22,21),22:(22,23,22),23:(23,24,23),24:(24,25,24),
 25:(25,27,r'\deleted{(Alors pour On suppose de plus $m=2n$x} (R3 rows25–26 together)'),
 26:(26,28,27),27:(27,29,28),28:(28,29,31),29:(29,30,30),30:(30,31,33),
 31:(31,32,34),32:(32,33,r'\mathrm{Grif}\handwritten{(}'),33:(33,34,35),
 34:(34,35,36),35:(35,36,37),36:(36,37,38),37:(37,38,39)
}
rows=[p.row(f'R1-015-{j:02d}',[f'{rr}-015-{v:02d}' if isinstance(v,int) else v for rr,v in zip(('R1','R2','R3'),tr)]) for j,tr in maps.items()]
def u(j,**kw):rows[j-1].update(kw)
u(1,confidence='medium',evidence='crops/scan015/R3/first_coefficient.jpg',decision='Main crop confirms a single underlined typed Q and a crossed, hooked machine subscript. The glyph is not wholly pen ell as C marks it. Chi is the closest literal approximation, with ell retained as an alphabetic alternative. H’s explicit global convention is credited.')
for j,fn in [(2,'display1_coefficient'),(5,'display2_coefficient'),(11,'induced_left_coefficient'),(12,'induced_middle_coefficient'),(13,'induced_right_coefficient')]:
 u(j,evidence=f'crops/scan015/MAIN/{fn}.jpg',decision='This individual coefficient crop confirms the same mechanical hooked/crossed subscript, and a clean single Q with a low rule. Apply the first-occurrence chi/ell convention, preserving the visible typed layer; H’s global convention is equivalent.')
u(3,evidence='crops/scan015/R3/reference_I.jpg',decision='The symmetric top and bottom bars and straight upright give the literal capital-I form. Retain C’s I); no numeral is substituted from the reference’s mathematical function.')
u(4,evidence='crops/scan015/MAIN/griffiths_quotes.jpg',decision='Both pairs are two straight elevated typewriter strokes, not angle-shaped guillemets. C and all readers retain the source form.')
u(6,evidence='crops/scan015/R1/parenthetic_cancel_and_end.jpg',decision='The exposed right upright and bowl favour the a-shaped reading of R1 over the e-first readings of R2/R3. The x-outs do not fully separate a from e, so both remain and no old sentence is reconstructed.')
u(7,evidence='crops/scan015/R1/parenthetic_cancel_and_end.jpg',decision='R1/R2 retain the visible small baseline dot; R3 omits it. Main retains it as a doubtful period because it may be incidental ink. This is an added visible mark, not merely uncertainty about the unchanged word peu.')
u(8,confidence='medium',evidence='crops/scan015/R1/parenthetic_cancel_and_end.jpg',decision='No period is visible between the closing curve and the clipped right scan edge. Omit H’s supplied period from the visible transcription; this does not establish what may have been outside the scan.')
u(9,evidence='crops/scan015/R2/dailleurs_cancelled.jpg',decision='Retain the recoverable l-h-o-m and the apostrophe/t ambiguity under x-outs. All three agree with C’s unresolved cancellation; H omits it.')
u(10,against_C=True,C=r'comma after \end{tikzcd}}\noindent, outside the diagram',final='typed comma in the triangle, lower-right of S',kind='insertion or placement',evidence='crops/scan015/MAIN/triangle_comma.jpg',decision='The comma is on the lower diagram baseline to the right of S. All three move it into the bottom-right cell; main confirms that placement. C’s closing the displayed diagram before a separate noindent comma moves it to the following text line; H omits it. This records physical placement, not a change of macro name.')
u(14,evidence='crops/scan015/MAIN/image_inverse_assertion.jpg',decision='The first long underline ends at de. The second begins at est and reaches beneath zéro, leaving Im i* outside. H’s emphasis convention is credited but its continuous extent is not the source’s extent.')
u(15,evidence='crops/scan015/MAIN/image_inverse_assertion.jpg',decision='The small raised star has fine crossing pen strokes distinct from the typed i. Mark the layer in C-format; H’s missing handwriting wrapper alone is not a reading error.')
u(16,against_C=True,final=r'\deleted{Sousx}',evidence='crops/scan015/R2/section_start.jpg',ink='Sous is readable under mechanical cancellations and a separate final crossed cell follows its s.',decision='Follow R2/R3 in retaining the additional visible x-out cell. The x is cancellation ink and is not asserted to recover an old lexical x. R1 describes this extra cell but leaves it out of its complete text; H leaves the whole deletion illegible.')
u(17,confidence='low',evidence='crops/scan015/R2/generic_insertion.jpg',decision='The dominant s shares its cell with a distinct t-like upright and cross component. There is no detached bar: the long nearby stroke is the insertion guide. Keep s first and both possible correction orders without deciding chronology or restoring H’s geometric-point bar.',consequential='The prose point-name is visibly unbarred and has an unresolved s/t overprint; H’s detached overbar is not supplied from the expected geometric-point notation.')
u(18,against_H=True,confidence='low',final=r'Y_{\bar s}, with s governed by the identical first s/t-overprint uncertainty',evidence='crops/scan015/R3/immersion_tensor.jpg',decision='Below the separate bar the same upright/cross component recurs, unlike the clean s later in k(bar s). Use first-occurrence shorthand for this identical local structure, as R2/R3 do; record the physical component omitted by both witnesses, not just a new doubt wrapper. R1 repeats the same uncertainty in place.')
u(19,evidence='crops/scan015/R3/immersion_tensor.jpg',decision='Main follows R1/R3: the serifed lowercase x is typed; the regular enclosing oval favours a typed O, with pen-circle alternative. R2’s certain pen-circle attribution is too strong. The literal composite is preserved rather than replaced by a modern uniform tensor glyph.')
u(20,final='immersion formula outside the two prose underline spans',C='immersion formula outside underline',H='immersion formula inside the long emph span',evidence='crops/scan015/R3/immersion_tensor.jpg',decision='The formula has no underline. The changes to its symbols are recorded at their separate loci; this row concerns only the gap between the two prose rules.')
u(21,evidence='crops/scan015/R3/de_la_underline.jpg',decision='The rule starts beneath d in de and continues under la section hyperplane. C omits the first word from its underline; H includes it, so this local scope is not itself an H error.')
u(22,against_H=True,final=r'gén\uline{érique}',confidence='medium',evidence='crops/scan015/R3/condition_underlines.jpg',ink='The continuous main stroke begins beneath the second accented e of générique. An isolated faint trace farther left does not connect to this underline.',decision='Follow R2/R3 and resolve the broader alternatives of R1. Preserve the visibly unruled gén; both witness scopes cover the whole word.')
u(23,evidence='crops/scan015/R3/condition_underlines.jpg',decision='The letters d-a-n-s remain recoverable under the x-outs. C and all three preserve the cancellation; H omits it.')
u(24,place='Partial underline in satisfasse aux conditions',C=r'\uline{satisfasse aux conditions}',H=r'\emph{... satisfasse aux conditions ...}',final=r's\uline{atisfasse aux conditions}',evidence='crops/scan015/R3/condition_underlines.jpg',ink='The long rule begins beneath a, after the initial s, and ends after conditions.',decision='All three identify the initially unruled s, confirmed by the main crop. The separate short rules and unruled reference labels are collated at the next locus.')
u(25,final=r'\deleted{(Alors pour On suppose de plus $m=2n$x}',evidence='crops/scan015/R2/cancelled_condition.jpg',decision='Main reads (Alors pour On, with capital O and n, then suppose de plus m=2n across the two old lines. The final extra x-out cell recorded by R2/R3 is visible. Resolve C’s On/où uncertainty; retain the missing old closing parenthesis and the abandoned words literally.')
u(26,evidence='crops/scan015/R2/cancelled_condition.jpg',decision='The rule stops at tout and resumes at dont, leaving the z-membership formula unruled. The added membership sign remains a pen intervention.')
u(27,C=r'$Y_{\bar s}$ outside the rule',H=r'$Y_{\bar s}$ inside the emph span',final=r'$Y_{\bar s}$ outside the rule',evidence='crops/scan015/R3/equivalence_left.jpg',decision='The Y and its subscript have no underline. The following partial-word predicate rule is recorded separately, avoiding a duplicate count of its endpoints.')
u(28,C='isolated z outside the rule',H='isolated z inside the emph span',final='isolated z outside the rule',evidence='crops/scan015/R3/equivalence_right.jpg',decision='The lone z between the two predicates is visibly unruled. This row concerns only that formula token; the predicate endpoints are recorded separately.')
u(29,evidence='crops/scan015/R3/equivalence_left.jpg',decision='The visible t is followed by a space and à, with no feminine ending. C/H and all three already preserve it; this diagnostic confirmation is not counted as a witness change.')
u(30,evidence='crops/scan015/R2/before_Par_suite.jpg',decision='The last occupied cancellation cell contains the shoulder of r and no further e cell follows before Par. Resolve C’s alternatives to En d’autr, as all three readers do.')
u(31,evidence='crops/scan015/MAIN/mod_torsion_deleted.jpg',decision='All letters of mod torsion are recoverable beneath the x-outs, including the final n. H’s illegibility mark is replaced by the readable cancelled text.')
u(32,final=grif,evidence='crops/scan015/R2/bottom_grif.jpg',decision='The curved opening mark is clearest, but a t-like transverse component remains. Retain the pen-parenthesis candidate first, then the possible old t with pen parenthesis and the literal t alternative. No chronology is asserted. H has the same preferred parenthesis, so uncertainty alone is not counted as an H error.')
u(33,against_C=False,final=r'Y_{\bar s_{\deleted{\unsure{x|k}}}}',confidence='low',evidence='crops/scan015/R2/bottom_grif.jpg',ink='A small crossed lower cell remains beneath the final Y subscript. Its exposed diagonal/vertical components do not securely separate an underlying x from k.',decision='Follow C/R2/R3 in retaining x/k uncertainty; R1’s certain x records cancellation ink but over-resolves the possible underlying symbol. H omits the lower cancelled cell.')
u(34,evidence='crops/scan015/R2/bottom_grif.jpg',decision='The eight letters of contient remain legible through the x-outs after the surviving comma. Preserve the cancellation omitted by H.')
u(35,against_C=True,final=r'tensoris\unsure{é}',evidence='crops/scan015/R1/clipped_endings.jpg',decision='The prefix tensoris is readable. Only the terminal e-body and acute are clipped enough to remain doubtful, so narrow C/R1/R2’s whole-word doubt. R3’s complete resolution is too strong; H has the same preferred word and is not counted for uncertainty alone.')
u(36,evidence='crops/scan015/R1/clipped_endings.jpg',decision='The clipped final s retains recoverable left lobes and lower curve. Follow the three readers in resolving C’s whole-word doubt to classes.')
u(37,decision='All three half-readings and both witnesses retain the unfinished vectoriel qui a. It is left incomplete without a supplied noun; the H dash encoding alone is not counted as an error. No extra crop was required for this agreed confirmation.')
extras={
 8:[p.row('R2-015-12',['continuous paragraph','R2-015-12','R3-015-08'],evidence='crops/scan015/MAIN/paragraph_boundary.jpg',decision='The parenthesis and D’ailleurs have the same left margin and ordinary successive baseline spacing. Follow all three continuous readings. C’s paragraph break is not supported by a blank baseline or indentation; H’s separate terminal punctuation is adjudicated above.')],
 24:[p.row('R2-015-26',[r'a) \uline{et} b) \uline{de} 2)','R2-015-26',r'a) e\uline{t} b) d\uline{e} 2)'],final=r'a) e\uline{t} b) d\uline{e} 2)',evidence='crops/scan015/R3/condition_underlines.jpg',ink='The two short strokes are under t of et and e of de. The reference labels a), b), and 2) are not underlined.',decision='Main follows R3’s partial-word scopes and resolves R2’s table alternatives. R2’s complete text uses the preferred t/e scopes without those table doubt wrappers; this return inconsistency is recorded rather than concealed. R1 extends each short rule across its whole word.')],
 27:[p.row('R3-015-29',[r'\uline{est algébriquement équivalent à zéro}',r'es\uline{t algébriquement équivalent à zéro}','R3-015-29'],final=first,evidence='crops/scan015/R3/equivalence_left.jpg',decision='Follow R3. Initial e lies outside the rule; its faint start permits s or t as the onset. The line ends under r in zéro, leaving its final o unruled. Preserve that endpoint even though both earlier readers span the whole zéro.')],
 28:[p.row('R3-015-32',[r'\uline{est cohomologiquement équivalent à zéro}',r'\uline{est cohomologiquement équivalent à zéro}','R3-015-32'],final=second,evidence='crops/scan015/R3/equivalence_left.jpg; crops/scan015/R3/equivalence_right.jpg',ink='The first source line is ruled through est cohomologiquement équiva. On its continuation, l/e lie left of the stroke and the fading n/t onset remains uncertain; the stroke reaches beneath the o of the later zéro.',decision='Keep R3’s internal start uncertainty on the continuation, but reject its exclusion of the later final o: this stroke reaches under o, unlike the previous clause’s rule. Join the source line-end hyphen without extending the underline over the unruled l/e.')],
}
ordered=[]
for j,r in enumerate(rows,1):ordered.append(r);ordered.extend(extras.get(j,[]))
rows=ordered
inv=p.inventory('R1')
for x in inv:
 if x['element']=='015-35':x.update(first_words_or_objects='Sousx; final x is visible cancellation ink beyond the recoverable old word',detail='The final cell is retained, not claimed as an old lexical x.')
 if x['element']=='015-38':x['detail']='The s/t-looking overlap has no detached bar; both possible correction orders remain uncertain.'
 if x['element']=='015-41':x['detail']='Same overlapped form as after soit, under a separate bar; first-occurrence uncertainty applies to this cell, not to later clean s.'
 if x['element']=='015-46':x.update(first_words_or_objects='partial underline beneath érique of générique',detail='The principal connected stroke begins at the second accented e; initial gén is unruled.')
 if x['element']=='015-49':x['first_words_or_objects']='short underline below t in et'
 if x['element']=='015-50':x['first_words_or_objects']='short underline below e in de'
 if x['element']=='015-51':x['first_words_or_objects']='(Alors pour On suppose de plus m=2nx; final x is a cancellation cell, no recovered old closing parenthesis'
 if x['element']=='015-57':x.update(first_words_or_objects='partial rule e[s/t algébriquement équivalent à zér]o',detail='Initial e and final o are unruled; s/t onset remains doubtful.')
 if x['element']=='015-58':x.update(position='[1091,1696,1647,1717]',first_words_or_objects='rule under est cohomologiquement équiva',detail='First source-line rule; continuation is separately inventoried.')
 if x['element']=='015-64':x['detail']='Both Y subscripts and surviving punctuation retained; only terminal é in tensorisé remains edge-clipped and doubtful.'
 if x['element']=='015-66':x.update(hand='pen curve preferred; possible typed t layer uncertain',first_words_or_objects='opening parenthesis, possible underlying t with pen parenthesis, or literal t')
 if x['element']=='015-67':x.update(hand='machine-looking cancellation; underlying glyph uncertain',first_words_or_objects='lower crossed x/k cell beneath final Y subscript',detail='C uncertainty retained; original letter not securely resolved.')
continuation=dict(sheet_kind='typescript',hand='pen, hand not independently attributed',element='',kind='insertion',position='[214,1771,431,1791]',first_words_or_objects='continuation rule le[n/t à zéro], with l/e unruled and final o included',transcribed='yes')
inv.insert(58,continuation)
for j,x in enumerate(inv,1):x['element']=f'015-{j:02d}'
def doubt(place,reading,alternatives,confidence,reason):return dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason)
unresolved=[
 doubt('first coefficient; identical repeated subscripts',r'\chi',[r'\ell'],'medium','The mechanical crossed shape is secure; its alphabetic interpretation is not established by expected cohomological notation.'),
 doubt('cancelled words after mais','nous at',['nous et'],'low','The exposed vowel favours a, but the crossing strokes also permit e.'),
 doubt('between peu and importe','doubtful period',['incidental ink/scan mark'],'low','Small baseline spot is visible; punctuation status remains uncertain.'),
 doubt('cancelled text after D’ailleurs',"l'hom",['lthom'],'low','The high mark in the second cell is obscured by cancellation.'),
 doubt('generic-point cell; identical overlap in first barred Y subscript','s',[r'\deleted{t}s',r'\deleted{s}t'],'low','Extra upright/cross component is visible; correction order is not established. The first Y cell repeats it; later clean s cells do not.'),
 doubt('oval around the typed x tensor core',r'\mathrm{O}',[r'\handwritten{\bigcirc}'],'medium','Regular oval favours typed O; an added pen circle cannot be excluded.'),
 doubt('first equivalence predicate: onset within est',r'e\uline{st}',[r'es\uline{t}'],'medium','Initial e is outside; the rule fades in at the s/t boundary. Its final endpoint before o of zéro is resolved.'),
 doubt('second equivalence predicate: onset in continuation lent',r'le\uline{nt}',[r'len\uline{t}'],'medium','The l/e are outside; fading rule begins at n/t. The later zéro has its final o included.'),
 doubt('opening mark after Grif',r'\handwritten{(}',[r'\deleted{t}\handwritten{(}','t'],'low','Curved opening stroke and t-like cross component coexist; old/live order cannot be established.'),
 doubt('cancelled lower glyph under final Y subscript','x',['k'],'low','Crossed lower cell remains too crowded to resolve the original glyph.'),
 doubt('right edge, final letter of tensorisé','é',[],'low','Readable prefix tensoris; terminal body and acute partly clipped at the scan edge.'),
]
notation=copy.deepcopy(p.R['R2']['notation'])
for x in notation:
 x['convention']=x.pop('latex')
 if x['sign']=='coefficient parameter':x['evidence']='crops/scan015/R3/first_coefficient.jpg; crops/scan015/MAIN/induced_middle_coefficient.jpg'
 if x['sign']=='rational coefficient':x['evidence']='crops/scan015/R3/first_coefficient.jpg; crops/scan015/MAIN/induced_right_coefficient.jpg'
 if x['sign']=='generic-point token':x['evidence']='crops/scan015/R2/generic_insertion.jpg; crops/scan015/R3/immersion_tensor.jpg'
 if x['sign']=='tensor/product sign':x.update(appearance='Typed serifed x core inside a regular oval, typed O preferred, pen circle possible',convention=r'\mathbin{\ooalign{\hfil$\mathrm{x}$\hfil\cr\hfil$\unsure{\mathrm{O}|\handwritten{\bigcirc}}$\hfil\cr}}',evidence='crops/scan015/R3/immersion_tensor.jpg',ambiguous=True)
 if x['sign']=='reference I)':x['evidence']='crops/scan015/R3/reference_I.jpg'
 if x['sign']=='Griffiths group name':x.update(convention=grif,evidence='crops/scan015/R2/bottom_grif.jpg')
 if x['sign']=='partial-word rules':x.update(appearance='Different local rule starts and endpoints, with faint s/t and n/t boundaries; first final o outside, second final o inside',convention=r'gén\uline{érique}; s\uline{atisfasse}; e\uline{t}; d\uline{e}; '+first+'; '+second,evidence='crops/scan015/R3/condition_underlines.jpg; crops/scan015/R3/equivalence_left.jpg; crops/scan015/R3/equivalence_right.jpg')
checks=p.checks()
checks.extend([
 dict(statement_id='N015.4-quotient-map-conditional',type='targeted proof check',outcome='Main reader checked the elementary conditional identity: for a linear map T:V→W, a subspace U⊂W, and the quotient q:W→W/U, ker(q∘T)={v:T(v)∈U}=T^{-1}(U). Hence T^{-1}(U)=0 is equivalent to injectivity of q∘T; under that assumption T(v)∈U implies v=0. This verifies only the formal equivalence/implication, not the geometric injectivity asserted on the page, blow-up computations, (LV), local condition (A), or any printed statement.'),
 dict(statement_id='N015.5-S-hypothesis-warning',type='carried as background without fault found',outcome='Supplied sweep row 36/15 (n°4) [A36-01] says the printed Griffiths-map injectivity result requires (LV) and local condition (A), citing XVIII 5.8.4, 5.8.7 and a failure example in 5.9. This remains attributed background from S, not an independently checked theorem/reference; no external text was consulted. The source’s own assertion and its triviaux wording are preserved.'),
 dict(statement_id='N015.6-restriction-and-containment',type='carried as background without fault found',outcome='The section5 restriction implication and the asserted containment of the primitive algebraic cohomology subspace in the rationalized Griffiths quotient are reported as source claims. Geometric injectivity, representative-independence, and the full containment were not proved by the elementary quotient identity or by glyph inspection.'),
])
notes=[
 'Annotated typescript, manuscript page 6, archive sheet number 14 in a comment. Three displays and a triangular diagram occur. The lower section is numbered 5. There is no title, date, or total page count on this sheet.',
 'The page defines P^m(X) as the kernel of the displayed composite through the blow-up, Y, and H^0(S,R^m f_*(Q_chi)). It next writes the homomorphism called “de Griffiths” into H^1(S,R^{m−1}f_*(Q_chi)). The repeated mechanical coefficient sign is retained as chi with ell alternative at first occurrence. These are source definitions/assertions, not a reconstructed theory.',
 'The triangle has i:Y→X_S, f:Y→S and g:X_S→S. Its induced i* map is displayed, followed by the assertion that the inverse image of Im i* under the Griffiths homomorphism is reduced to zero. The source parenthesis says “en fait, on y pourrait remplacer S par P^1_k, mais ... peu ... importe ici”; its cancelled words and doubtful dot remain visible in the transcription.',
 'A limited formal check was made: for T:V→W and a subspace U, the quotient map q has ker(q∘T)=T^{-1}(U). Thus the zero-preimage statement would give injectivity of the quotient-valued map, and under that assumption membership in U forces zero. This does not prove the actual Griffiths-map assertion or any geometric hypothesis required for it.',
 'The source says “Ceci se fait par des calculs explicites essentiellement triviaux, compte tenu de la structure cohomologique connue d’une variété éclatée.” The entire claim is visible and retained. Supplied S row 36/15 (n°4) [A36-01] warns that the printed statement needs (LV) and local condition (A), with references and a failure example. Those external claims were not researched or verified here; the warning is attributed to S, and no missing hypothesis is inserted into the manuscript.',
 'Section 5 combines 3) and 4), inserts supposant m=2n, and assumes a) and b) of 2) for the generic hyperplane immersion. It states that algebraic triviality of the restriction of a cycle implies cohomological triviality modulo torsion, then claims that the Griffiths quotient tensorized with underlined Q contains P^{2n}_{alg}(X). These geometric claims and any representative-independence are not independently established here.',
 'Mathematical diagnostics directed attention to the point-name and tensor glyph. The prose s has no detached bar, but an overlapping t-like component; the first barred Y-subscript repeats that structure, whereas later k(bar s) is clean. The tensor-like cell consists of a typed x and an oval, with typed O preferred over a pen circle. No expected geometric-point notation or tensor typography determines the reading.',
 'The source masculine équivalent after restriction and the unfinished final “- vectoriel qui a” remain unrepaired. Cancelled Alors pour On and both placements of m=2n are retained. The visible terminal x-out cells after Sous and the cancelled m=2n record cancellation marks, not recovered lexical letters. Other uncertainties concern nous at/et, l’hom/lthom, Grif’s opening mark, a lower x/k cell, and the clipped final é of tensorisé; classes is resolved.',
 'Underline scope is local: de belongs to the rule before la section, gén is unruled in générique, s is unruled in satisfasse, and only t/e receive the small rules in et/de. The first equivalence clause ends its underline before the o of zéro; the second reaches beneath that o. Fading starts inside est and the continued lent remain doubtful. H’s general emph convention is credited, while these actual extent differences are recorded. The parenthesis and D’ailleurs share a continuous paragraph; the diagram comma sits at lower-right beside S.',
]
work=json.loads((O/'validation/scan015_main_working.json').read_text())
views=work['viewed_once']
additional=['R2/before_Par_suite','R2/bottom_grif','R1/clipped_endings','MAIN/display1_coefficient','MAIN/display2_coefficient','MAIN/induced_left_coefficient','MAIN/induced_middle_coefficient','MAIN/induced_right_coefficient','MAIN/griffiths_quotes','MAIN/triangle_comma','MAIN/paragraph_boundary','MAIN/image_inverse_assertion','MAIN/calculation_claim','MAIN/mod_torsion_deleted']
for a in additional:
 v='crops/scan015/'+a+'.jpg'
 if v not in views:views.append(v)
assert len(views)==26
work.update(status='all complete readings, difference lists, inventories, notes and actual crop decisions consolidated; see decisions/scan015.json',viewed_once=views,delivery_exception='The first two-image return of MAIN induced_left_coefficient and induced_middle_coefficient was truncated before either image could be inspected. The SAME saved images were resent individually and then inspected once; no recropping.')
(O/'validation/scan015_main_working.json').write_text(json.dumps(work,ensure_ascii=False,indent=2)+'\n')
p.write(rows,inv,unresolved,notation,notes,views,
 overview='Three fresh independent full-page readings, their complete texts, all difference rows and all inventories were compared. The main reader inspected 15 existing local crops and 11 new crops; no whole page or half was opened by the main reader.',
 abbreviations=p.R['R1']['abbreviations'],check_events=checks,
 legibility='Ordinary type and most cancellations are readable. The least secure loci are overprinted s/t and the Grif delimiter, a/e under x-outs, the lower x/k cell, faint underline onsets, and the clipped é. Both witnesses omit a small baseline mark and trailing cancellation cells; H additionally leaves several readable deletions illegible and overextends emphasis. No mathematical emendation is made.',
 workflow_observation='42 reader crops (12/13/17); main reused 15 and made 11. Two new coefficient images had a truncated initial delivery before inspection and were resent unchanged, one at a time. R2’s table and complete text disagreed about marking two small underline endpoints. v07 will require in-place and table doubts to agree, and will clarify identical-overprint shorthand and localizing clipped-word doubt.',
 sweep=[dict(where='36/15 (n°4) [A36-01]',S='S warns that the stated injectivity modulo the fixed part needs (LV) and local condition (A) in the printed result, citing XVIII 5.8.4, 5.8.7 and a failure example in 5.9.',ink='crops/scan015/MAIN/image_inverse_assertion.jpg shows the zero-preimage assertion. crops/scan015/MAIN/calculation_claim.jpg clearly reads calculs explicites essentiellement triviaux and the blow-up cohomology explanation; no additional local hypotheses are written in those lines.',disposition='Confirm the literal draft wording. Carry S’s proposed mathematical qualification as attributed background, not as a verified external theorem and not as an emendation. The elementary quotient-kernel identity was checked separately and does not prove geometric injectivity.')])
