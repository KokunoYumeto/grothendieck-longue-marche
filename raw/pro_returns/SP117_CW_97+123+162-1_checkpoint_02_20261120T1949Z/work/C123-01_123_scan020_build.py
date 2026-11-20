from pathlib import Path
import json

root=Path('/workspace/scratch/d27bd2a88bca')
page='C123-01_123_scan020'
work=root/'out'/'work'
meta=json.loads((work/f'{page}_cropmeta.json').read_text())
principal=r'\unsure{princi\deleted{a}p\deleted{p}ale|princi\deleted{p}a\deleted{a}ple}'
last_la=r'\deleted{\unsure{\$|S}}la'
tex=(root/'packets'/page/'C.tex').read_text()
tex=tex.replace(r'\handwritten{\unsure{\mathfrak{g}|\mathscr{G}}}',r'\handwritten{\mathfrak{g}}')
tex=tex.replace(r'\unsure{principale}',principal)
tex=tex.replace(r'Z_{\unsure{o|0}}',r'Z_o')
tex=tex.replace(r'\unsure{la}',last_la)
(work/f'{page}_draft.tex').write_text(tex)

changes=[]
def change(id,line,c,h,final,scan_shows,crop,confidence,kind,changed_C,changed_H,marked_in_H=False,consequential=False,certainty_only=False):
    changes.append(dict(id=id,line=line,c=c,h=h,final=final,scan_shows=scan_shows,crop=meta[crop]['crop'],box=meta[crop]['box'],confidence=confidence,kind=kind,changed_C=changed_C,changed_H=changed_H,marked_in_H=marked_in_H,consequential=consequential,certainty_only=certainty_only))

change('r01','L03',r'\handwritten{\unsure{\mathfrak{g}|\mathscr{G}}}(2)^{\handwritten{*}}+\operatorname{Fil}^{\handwritten{3}}(\handwritten{\mathfrak{g}})',r'\mathfrak{g}(2)^*+\operatorname{Fil}^3(\mathfrak{g})',r'\handwritten{\mathfrak{g}}(2)^{\handwritten{*}}+\operatorname{Fil}^{\handwritten{3}}(\handwritten{\mathfrak{g}})',"After 'où e parcourt', both handwritten letters have the same narrow upper cup, tall right stroke and long returning descender. The first is the lower-case fraktur g, not a script capital G. The whole formula, its star, plus sign and exponent 3 are visible.",'b02','high','misread symbol or index',True,False,certainty_only=True)
change('r02','L05–L06',r'(\exp(e)\handwritten{\mid}e\handwritten{\in}a+\operatorname{Fil}^{\handwritten{3}}(\handwritten{\mathfrak{g}},))',r'(\exp(e)\,|\,e\in a+\operatorname{Fil}^{3}(\mathfrak{g}))',r'(\exp(e)\handwritten{\mid}e\handwritten{\in}a+\operatorname{Fil}^{\handwritten{3}}(\handwritten{\mathfrak{g}},))',"In 'aux ensembles de la forme', the wrapped set expression has a distinct low typed comma after handwritten g and before the inner closing parenthesis. Both closing parentheses are present; the comma is preserved as a source slip.",'b03','high','omission',False,True,consequential=True)
change('r03','L06',r'quelconque.\deleted{de}','quelconque.',r'quelconque.\deleted{de}',"Immediately after 'un élément quelconque.' two cancelled letters remain: d has its ascender and rounded bowl, e has a middle crossbar and lower curve. Typed x characters cancel both letters. H omits the cancelled fragment.",'b13','high','omission',False,True)
change('r04','L07',r"Pour qu'on ait\hspace{1.5em}$(1)=0$",r"Pour qu'on ait \ill{}$(1)=0$",r"Pour qu'on ait\hspace{1.5em}$(1)=0$","After the underlined heading 'Cas principal.', the typewriter left a blank between 'ait' and '(1)=0'. The space contains no supplied letter or other unreadable ink. H's own editorial note recognizes the blank; its ill marker is therefore not transcribed.",'b04','high','text not on the page',False,True,marked_in_H=True,consequential=True)
change('r05','L07',r"que \deleted{l'homomor}",'que',r"que \deleted{l'homomor}","At the right end of the line 'il faut et suffit que', the incomplete typed fragment l'homomor is cancelled with x overstrikes. Its l, apostrophe, h, o, m, o, m, o, r remain distinguishable. The fragment is not expanded to a complete word.",'b05','high','omission',False,True)
change('r06','L08',r'f:\operatorname{Sl}(2,k)\hspace{1.5em}G',r'f\colon\mathrm{Sl}(2,k)\to G',r'f:\operatorname{Sl}(2,k)\hspace{1.5em}G',"In 'la classe d’homomorphismes', the typed formula reads f: Sl(2,k), then an unfilled space, then G. The space has no shaft, arrowhead or handwritten addition. H's arrow is not on the page.",'b06','high','text not on the page',False,True,consequential=True)
change('r07','L08',r'\unsure{principale}','principale',principal,"After 'envisagée soit', the two positions between princi and le each contain both p and a strokes: a descender and bowl belonging to p, with an a-shaped loop/stem superposed. The probable ap→pa correction is not securely ordered by the ink. Both orders are preserved as alternatives instead of reducing the clusters to plain pa.",'b07','medium','deletion state (struck given live or live given struck)',True,True)
change('r08','L08',"``principale''",'« principale »',"``"+principal+"''","The quotation marks flanking the overtyped word after 'soit' are pairs of vertical typed strokes, not angle-shaped guillemets. The separate letter-state change is r07.",'b07','high','other',False,True)
change('r09','L11',r'Z_{\unsure{o|0}}',r'Z_0',r'Z_o',"In 'le groupe Z… est le groupe unité', the lowered loop is o-height and matches the round lower-case o in the adjacent typewritten words. It is shorter and rounder than the tall baseline zero in '(1)=0' on L07. The complete Z and Dyn_c context is included; no mathematical normalization is used.",'b09','high','misread symbol or index',True,True,consequential=True)
change('r10','L11',r'\unsure{la}','la',last_la,"Before the line-end 'réci-', the first live letter has the top serif, upright stem and baseline foot of l. A separate curved character is overtyped underneath it, with upper and lower curved portions and short projecting strokes. Dollar-sign and capital-S readings remain plausible; the underlying character is not silently discarded.",'b10','low','deletion state (struck given live or live given struck)',True,True)
change('r11','M01',r'Cas $A_2,A_4$ les paraboliques',r'Cas $A_2$, $A_4$\,: les paraboliques',r'Cas $A_2,A_4$ les paraboliques',"In the left marginal note, 'Cas A₂,A₄' is followed by a line break and 'les paraboliques'. The comma between A₂ and A₄ is visible, but no colon follows A₄. The full slanted note is supplied upright in the saved crop.",'b11','high','text not on the page',False,True)
change('r12','M01',"``sous-réguliers''",'« sous-réguliers »',"``sous-réguliers''","The marginal words 'sous-réguliers' are enclosed by two pen ticks at each end. They are double quotation marks rather than the angle strokes of guillemets.",'b11','high','other',False,True)

inventory=[]
def inv(element,kind,position,first,hand='typewriter with handwritten mathematical additions and corrections'):
    inventory.append(dict(scan='20',sheet_kind='typescript',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('i01','text','L01–L02, top of body',"nier (ou, ce qui revient au même, c) est bien déterminée. Les unipotents…")
inv('i02','insertion','Above the beginning of L03, attaching after sont on L02',r'\inserted{ceux}','typewritten insertion with handwritten placement hook')
inv('i03','text','L03',r'de la forme $\exp(e)$, où $e$ parcourt… Ils forment une classe')
inv('i04','insertion','L03, mathematical fill-ins',r'$\mathfrak{g}$, superscript *, superscript 3, $\mathfrak{g}$','handwritten mathematical characters on typescript')
inv('i05','text','L04',r"de conjugaison d'éléments de $U$ \uline{par} $P$ (NB mais pas par $U$), les classes de")
inv('i06','text','L05',r"conjugaison \uline{par} $U$ s'identifiant aux ensembles de la forme $(\exp(e)\mid e\in a+$")
inv('i07','insertion','L05, right end of set expression',r'$\mid$ and $\in$','handwritten mathematical signs on typescript')
inv('i08','text','L06',r'$\operatorname{Fil}^{3}(\mathfrak{g},))$, où $a\in\mathfrak{g}(2)^*$ est un élément quelconque.')
inv('i09','insertion','L06, mathematical fill-ins',r'superscript 3, $\mathfrak{g}$, $\in\mathfrak{g}$, superscript *','handwritten mathematical characters on typescript')
inv('i10','deletion','L06, after quelconque.',r'\deleted{de}','typewritten word cancelled by x overstrikes')
inv('i11','text','L07, paragraph heading',r'\uline{Cas principal}.','typewritten underlined heading')
inv('i12','text','L07, following heading',r"Pour qu'on ait\hspace{1.5em}$(1)=0$, il faut et suffit que")
inv('i13','deletion','L07, right line end',r"\deleted{l'homomor}",'typewritten unfinished word cancelled by x overstrikes')
inv('i14','text','L08',r"la classe d'homomorphismes $f:\operatorname{Sl}(2,k)\hspace{1.5em}G$ envisagée soit… au")
inv('i15','deletion','L08, two overtyped positions in the quoted word',principal,'typewriter correction with uncertain ordering of a/p overlays')
inv('i16','text','L09',r'sens de Dynkin-Kostant. Alors le parabolique associé $P$ est un Borel (la')
inv('i17','margin note','Left margin alongside L09–L12',r'\uline{ex} Cas $A_2,A_4$ les paraboliques associés aux unipotents ``sous-réguliers\'\' sont des \unsure{Borels|borels} !','handwritten marginal annotation; no author attribution established from this page')
inv('i18','text','L10',r"réciproque n'étant pas vraie… , cf table de Dynkin), et le")
inv('i19','deletion','L10, after vraie',r'\deleted{sans doute}','typewritten words crossed out by a handwritten stroke')
inv('i20','text','L11',r'groupe $Z_o$ est le groupe unité (i.e. $\operatorname{Dyn}_c$ est un torseur sous $G$), … réci-')
inv('i21','deletion','L11, overtyped initial of la',last_la,'typewriter correction; underlying curved character uncertain')
inv('i22','text','L12, final body line',r"proque n'étant pas vraie sans doute.")
inv('i23','margin note','Lower left corner of otherwise blank lower half','% archive sheet number: 19','archive pencil foliation; not treated as the text’s own numbering')

boxes=[]
def box(id,kind,xy,reading):
    boxes.append(dict(box=id,kind=kind,x0=xy[0],y0=xy[1],x1=xy[2],y1=xy[3],reading=reading))
box('s01','insertion',[280,253,402,337],r'\inserted{ceux} de la')
box('s02','whole formula with handwritten additions',[915,267,1232,359],r'$\handwritten{\mathfrak{g}}(2)^{\handwritten{*}}+\operatorname{Fil}^{\handwritten{3}}(\handwritten{\mathfrak{g}})$.')
box('s03','wrapped whole formula, handwritten signs and deletion',[280,410,1630,563],r"conjugaison \uline{par} $U$ s'identifiant aux ensembles de la forme $(\exp(e)\handwritten{\mid}e\handwritten{\in}a+\operatorname{Fil}^{\handwritten{3}}(\handwritten{\mathfrak{g}},))$, où $a\handwritten{\in\mathfrak{g}}(2)^{\handwritten{*}}$ est un élément quelconque.\deleted{de}")
box('s04','heading and unfilled formula blank',[285,555,1010,605],r"\uline{Cas principal}. Pour qu'on ait\hspace{1.5em}$(1)=0$,")
box('s05','deletion',[1360,550,1620,610],r"que \deleted{l'homomor}")
box('s06','whole formula with unfilled arrow space',[783,615,1065,673],r'$f:\operatorname{Sl}(2,k)\hspace{1.5em}G$')
box('s07','typed-over word and quotation marks',[1335,611,1565,677],"``"+principal+"''")
box('s08','deletion',[814,749,1023,805],r'\deleted{sans doute},')
box('s09','whole formula context and uncertain-source index',[280,812,1470,879],r'groupe $Z_o$ est le groupe unité (i.e. $\operatorname{Dyn}_c$ est un torseur sous $G$),')
box('s10','overtyped letter',[1480,812,1630,882],last_la+' réci-')
box('s11','margin note',[18,709,300,957],r'\margin{\handwritten{\uline{ex}\quad Cas $A_2,A_4$ les paraboliques associés aux unipotents ``sous-réguliers\'\' sont des \unsure{Borels|borels} !}}')
box('s12','handwritten archive number',[45,2050,130,2127],'% archive sheet number: 19')
box('s13','live final qualification',[280,882,965,940],r"proque n'étant pas vraie sans doute.")

report=dict(
    page=page,
    line_count=12,
    changes=changes,
    doubts=[
        dict(line='L08',reading=principal,alternatives=[r'princi\deleted{a}p\deleted{p}ale',r'princi\deleted{p}a\deleted{a}ple'],confidence='medium',reason='Both adjacent positions contain p/a composites. Their shapes establish overtyping but do not securely establish the chronology of the two letter pairs. The usual word is not used to suppress the alternative order.'),
        dict(line='L11',reading=last_la,alternatives=[r'\deleted{\$}la',r'\deleted{S}la'],confidence='low',reason='The live l and following a are clear, but the curved underlying character cannot be securely distinguished between a dollar-sign-like glyph and capital S. Short strokes below and above the l foot leave the first candidate plausible.'),
        dict(line='M01',reading=r'\unsure{Borels|borels}',alternatives=['Borels','borels'],confidence='medium',reason='The tall initial has a dark upper portion and one clear lower bowl. The upper portion may be a compact capital-B bow or the loop of lower-case b; the margin crop does not decide the case.'),
        dict(line='L05–L06',reading=r'\operatorname{Fil}^{3}(\mathfrak{g},)',alternatives=[],confidence='high',reason='Source slip: a typed comma is present inside the parentheses. Its mathematical motivation has not been assessed; it remains in the transcription.'),
        dict(line='L07',reading=r"ait\hspace{1.5em}$(1)=0$",alternatives=[],confidence='high',reason='Source blank before (1)=0. Nothing was inserted into it, so an expected function or letter is not supplied.'),
        dict(line='L08',reading=r'f:\operatorname{Sl}(2,k)\hspace{1.5em}G',alternatives=[],confidence='high',reason='Source blank between (2,k) and G; there is no visible arrow.'),
        dict(line='L07',reading=r"\deleted{l'homomor}",alternatives=[],confidence='high',reason='The cancelled typed word is unfinished. No completion is supplied.'),
    ],
    inventory=inventory,
    notes=[
        'Only the assigned scan020 packet, its page-specific prior_questions.md, the shared conventions/errors and the supplied preamble were consulted. No other page result or second-reading file was inspected.',
        'The whole scan was read for layout, then the upper half line by line against both witnesses. The first lower-half tool output was truncated before inspection; its replacement display was inspected and showed only blank paper and archive folio 19.',
        'Thirteen evidence crops were saved and displayed. The lower bounds of b02 and b03 were corrected to retain the full handwritten descenders. The tight cancelled-word crop b13 was necessary because the wrapped-formula crop leaves that small word too small for a letter-state decision.',
        'Evidence crops use original full-image coordinates, LANCZOS enlargement to a 2500-pixel long edge, autocontrast at cutoff 0.4 and a modest unsharp mask. The margin crop b11 is rotated 18 degrees clockwise to make its writing upright; original coordinates remain in crop_transforms.',
        'The neutral s-series boxes are for the subsequent blind audit and may be tighter than the saved b-series evidence crops. Each reading gives the complete target contents, with partial neighbouring body letters at the edge of the marginal box treated as context rather than part of the note.',
        'Every handwritten formula character, pen numeral, insertion, deletion, marginal note and unresolved overtyped word is covered by a blind-audit box. The two marginal pen indices 2 and 4 and archive numeral 19 are included.',
        'The page begins with the continuation fragment nier; no preceding letters are reconstructed. The final réci-/proque line break is joined in the candidate as required by the conventions.',
        'The title and both occurrences of par are underlined. H’s emphasis/heading macros, handwriting wrappers, page marker and explanatory note are not counted as independent substantive text changes. Source double quotation marks, however, are kept distinct from H’s guillemets.',
        'The phrase sans doute inside the Borel parenthesis is cancelled; the final sans doute after the unit-stabilizer statement is live. The comma after the cancelled phrase remains live. The source abbreviation cf has no period here.',
        'No diagram or drawing occurs. No mathematical proof, calculation or formal certificate was performed. Formula reinspection resolved transcription details only; no clear source slip was repaired from the mathematics.'
    ],
    reading_notes=[
        'The first paragraph describes the unipotent elements defining a given filtration as exponentials with exponent in g(2)* + Fil³(g), states that they form a conjugacy class under P, and describes the U-conjugacy classes by affine sets a + Fil³(g). These are source claims, not mathematical results checked in this reading.',
        'The paragraph headed “Cas principal.” relates an incompletely typed condition “(1)=0” to a principal Dynkin–Kostant homomorphism class. It then states that the associated parabolic is a Borel and that Z_o is the unit group, with Dyn_c a torsor under G.',
        'The source cancels “sans doute” in its parenthesis about the converse to the Borel assertion and refers to Dynkin’s table. Its final qualification “la réciproque n’étant pas vraie sans doute” remains live after the unit-stabilizer assertion. Neither converse claim was independently assessed here.',
        'A handwritten marginal example names A₂ and A₄ and says that the parabolics associated with “sous-réguliers” unipotents are Borels. The capital B/lower-case b reading remains uncertain; the assertion is reported without validation.',
        'Preserved source irregularities include the comma inside Fil³(g,), the empty slot before (1)=0, the missing map arrow, the unfinished cancelled fragment l’homomor, and the p/a and curved-character typewriter overlays. No expected mathematical content has been inserted.',
        'This is one annotated typescript sheet with 12 main body lines, one short inserted word and a five-line marginal note. “Cas principal.” is the only local heading. No date or original text page number is visible. Archive folio 19 appears at the lower left; the lower half is otherwise blank.'
    ],
    check_events=[],
    visual_audit_events=[
        dict(statement_id='scan020-layout',type='visual transcription audit',outcome='Whole-image layout and both halves inspected; 12 body lines, insertion, marginal note, cancellations and archive number inventoried. No mathematical check is implied.'),
        dict(statement_id='scan020-formulas',type='visual transcription audit',outcome='Whole formulas in b02, b03, b04, b06 and b09 inspected for characters, indices, punctuation and genuine blank spaces. This is ink verification only.'),
        dict(statement_id='scan020-states',type='visual transcription audit',outcome='Each cancelled span and both overtyped places inspected on its saved crop; ambiguous overtyping retained. Live and cancelled sans doute distinguished.'),
        dict(statement_id='scan020-margin',type='visual transcription audit',outcome='Upright margin crop checked word by word, including A₂, A₄, quotation marks, absent colon and unresolved Borels/borels case.')
    ],
    notation=[
        '123/020: The handwritten lower-case fraktur g has a narrow upper cup, tall right stroke and long returning descender. All four occurrences on this sheet were checked; the first C alternative script capital G is rejected on its saved whole-formula crop.',
        '123/020: The two superscript stars and both handwritten Fil exponents 3 are visible. The set separator is a vertical bar, and both membership signs are handwritten ∈.',
        '123/020: Z has a lowered typewriter lower-case o, with o-height distinct from the full-height zero in (1)=0. Do not normalize it to 0.',
        '123/020: Sl is typed capital S and lower-case l. The source leaves the space before G empty; it is not an arrow.',
        '123/020: The source’s double quotation marks are paired strokes, typed around the overtyped principale and handwritten around sous-réguliers. They are not guillemets.',
        '123/020: Keep NB, i.e. and cf as typed. The noun Borels/borels in the margin remains unresolved at its only occurrence.'
    ],
    hand_log=[
        '123/020, four handwritten g glyphs: the right stem descends far below the baseline and returns in a long loop. This form matches the supplied running notation and can be mistaken for a script capital G; C marked the first occurrence doubtful. Every occurrence on this page was inspected.',
        '123/020, marginal Borels/borels: the initial’s dark upper loop does not securely distinguish capital B from cursive lower-case b. The existing C doubt is retained; H’s capital is only one plausible reading.',
        '123/020, typewriter corrections: both adjacent positions in the quoted princ…le contain p/a composites. Typewriter overstrikes can preserve two letters without making their chronological order recoverable; the candidate records both orders.',
        '123/020, before final la: a curved S/$-like character remains under the live l. A familiar word must not cause that cancelled character to disappear.',
        '123/020, cancelled words: typed x overstrikes cancel de and l’homomor; a pen stroke cancels sans doute. Their punctuation and the separate live final sans doute are not cancelled.'
    ],
    boxes=boxes,
    metadata=dict(full_image_size=[1669,2149],line_count_basis='12 main typewritten body lines; inserted word and five marginal lines counted separately in reading_notes',crop_transforms=meta,source_reading_status='first-reader candidate for parent adjudication; not a committed page')
)
# Remove accidental escaping of apostrophes in the two raw double-quote strings.
def clean(obj):
    if isinstance(obj,str): return obj.replace("\\'", "'")
    if isinstance(obj,list): return [clean(x) for x in obj]
    if isinstance(obj,dict): return {k:clean(v) for k,v in obj.items()}
    return obj
report=clean(report)
(work/f'{page}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'draft':str(work/f'{page}_draft.tex'),'report':str(work/f'{page}_report.json'),'changes':len(changes),'doubts':len(report['doubts']),'inventory':len(inventory),'boxes':len(boxes),'crops':len(meta)},ensure_ascii=False))
