#!/usr/bin/env python3
"""Explicit main-reader decisions after all three scan 027 returns and 19 crops."""
from pathlib import Path
import copy,json
R=Path(__file__).resolve().parents[1]
D={r:json.loads((R/f'readers/scan027/{r}/report.json').read_text()) for r in ('r1','r2','r3')}
C=copy.deepcopy(D['r2']['changes'])
m1={0:13,1:1,3:2,4:3,5:4,7:5,8:6,10:7,12:8,13:9,14:10,15:11,17:12}
m3={0:0,1:1,3:2,5:3,7:4,8:5,10:6,11:7,12:8,13:9,14:10,15:11,16:12,17:13}
for i,c in enumerate(C):
    c['readers']={'r2':c['reading']}
    if i in m1:c['readers']['r1']=D['r1']['changes'][m1[i]]['reading']
    if i in m3:c['readers']['r3']=D['r3']['changes'][m3[i]]['reading']
    c['mathematical_consequence']=''
C[1]['readers']['r1']=r'\handwritten{\Psi}, in a tilted left oval'
for i in [2,6,9]:
    for r in ['r1','r3']:
        C[i]['readers'][r]=r'\handwritten{\unsure{\mu|\psi}}' if i==2 else (r'\handwritten{\mu}' if i==6 else r'\handwritten{\phi}(\handwritten{\mu}(x,y),\handwritten{\mu}(z,t))=\handwritten{\mu}(\handwritten{\phi}(x,z),\handwritten{\phi}(y,t))')
C[4]['readers']['r3']=r'\unsure{,}'
C[11]['readers']['r1']=r'la section unité de $E$ considéré'
C[16]['readers']['r1']=r'e_{E\deleted{\unsure{/S|/P|/Q}}}'
def p3(s):return f'readers/scan027/r3/crops/{s}.jpg'
def p2(s):return f'readers/scan027/r2/crops/{s}.jpg'
def pm(s):return f'crops/scan027/{s}.jpg'
paths={0:pm('01_cancellation_paths'),1:p3('01_margin_psi'),2:p2('03_initial_second_law'),3:p3('03_deleted_j'),4:p3('04_abandoned_formula'),5:p3('04_abandoned_formula'),6:pm('02_prose_second_law'),7:p3('05_ces'),8:p2('07_interchange_graphic'),9:p2('07_interchange_graphic'),10:p3('07_E_correction'),11:pm('03_symmetric_comma'),12:p3('10_Groupe'),13:p3('11_De_plus_Ces'),14:p3('11_De_plus_Ces'),15:pm('04_de_underline'),16:p3('12_eE_revision'),17:p3('13_deleted_phrase')}
ev={
0:'The main body-graphic crop shows six separate long paths, including the bowed left near-vertical stroke and the curved right-hand lower stroke. The r3 common-coordinate drawing preserves their crossings and endpoints around the complete text; there is no rectangular border. This crop was for page-spanning geometry, not a repeated reading of settled glyphs.',
1:'The main margin crop shows the trident-like sign inside a tall sloping oval to the LEFT of the partial-law line. Three upper branches and a descending central stem establish psi/Psi, but the isolated hand form does not securely establish case. Main retains C and r2/r3 case uncertainty, while adopting the actual left placement and oval geometry.',
2:'The main opening-law crop shows a typed u-shaped cup traversed through its interior by an oblique pen shaft, extending above the cup and below its bottom. Main reads psi, as r2, rather than a mu with a merely lengthened left leg. The marginal sign is not used to force this identification.',
3:'The enlarged cancelled opening retains a separate dot above the descending j and the following tall left parenthesis under the typed x strikes. j( is resolved.',
4:'After the first g phi(x,y), a separate low bent punctuation tail remains below the closing parenthesis and the horizontal cancellation. Main resolves the first comma, agreeing with r1/r2. Both equality slots remain uncertain independently.',
5:'The same abandoned-formula crop shows a second low comma after the second g phi(x,y), before the terminal phi(. All three readers add it. The last phi( is left incomplete.',
6:'The unique prose-law crop independently shows the u-shaped cup and the oblique shaft through its interior, with upper and lower projections. Main reads psi here; this is not supplied from the opening occurrence.',
7:'The initial slot visibly contains both the rounded c contour and the upper/lower s strokes, followed by clear es. Main retains the overprint and both possible strike orders; plain ces/ses alone loses the correction layer.',
8:'The local formula crop shows two distinct curves: the upper sloping curve ends in a short upward stroke, while the lower hooked curve ends in a short downward stroke. The equation number is above-left of the equation. Main adopts r3 source-relative paths and the raised left label.',
9:'Each of the three second-law glyphs in the interchange display has its own u-shaped cup crossed centrally by an oblique shaft. All three are read independently as psi, agreeing with r2. The x,y,z,t placement and all phi signs are unchanged.',
10:'The crop shows repeated E contours in one slot and a separate following t with its crossbar and low foot under cancellation. Main resolves t and retains same-letter doubling of E without inventing an earlier unrelated letter.',
11:'A separate long, curved, tapering comma is visible after E before considéré. Main includes it and marks it handwritten; r1 omits the comma, while r2/r3 include it without that hand distinction.',
12:'Both a full-height G with its inner bar and a lower-case g with a loop below the baseline are visible. Their chronological order is not established. Main retains both overprint orders.',
13:'Typed De plus, lies above a band of cancelled cursive writing, with a separate long curved insertion call. The thin cursive remains cannot be assembled into a secure word in the unique enlarged crop. One unreadable prose word is estimated and the cancellation is retained.',
14:'The initial of Ces contains both a high capital-C contour and a lower c contour before clear es. Main preserves the overprint without selecting a strike chronology.',
15:'The main crop shows a short thick horizontal line immediately below de, bounded before and after that word. It does not run beneath either adjacent product. The separate underline is retained.',
16:'The main final-formula crop shows the slash and surviving upper terminal and lower curve of S in the cancelled subscript. Main agrees with r2 that /S is supported, at medium confidence; P and Q are not retained there. The separately cancelled Gamma-argument tail remains unresolved.',
17:'The main bottom crop shows a distinct low comma followed by surviving letter contours spelling et une conséquence, including the acute and the q descender. Main resolves the word run at medium confidence, as r2, retaining the whole phrase within the cancellation.'}
tex=(R/'readers/scan027/r3/reading.tex').read_text()
replacements=[
 (r'\handwritten{\unsure{\mu|\psi}}',r'\handwritten{\psi}'),
 (r'\handwritten{\mu}',r'\handwritten{\psi}'),
 (r'\phi}(x,y)\unsure{,}',r'\phi}(x,y),'),
 (r'la section unité de $E$, considéré',r'la section unité de $E$\handwritten{,} considéré'),
 (r'e_{E\deleted{\unsure{/S|/Q}}}',r'e_{E\deleted{/S}}'),
 (r'annoncée\deleted{,\unsure{et une conséquence}}',r'annoncée\deleted{, et une conséquence}')]
for a,b in replacements:
    assert a in tex,a
    tex=tex.replace(a,b)
for i,c in enumerate(C):c.update(crop=paths[i],evidence=ev[i])
for i in [2,6,9,11,16,17]:C[i]['confidence']='medium'
C[0]['reading']=tex[tex.index(r'\draw[line width=.65pt] (1495,351)'):tex.index(r'\end{tikzpicture}')].strip()
C[1]['reading']=tex[tex.index(r'\node[anchor=center] at (107,374)'):tex.index('% Two small isolated')].strip()
C[8]['reading']=tex[tex.index(r'\draw[line width=.45pt] (301,1005)'):tex.index(r'\node at (230,1039)')].strip()
C[11]['reading']=r'la section unité de $E$\handwritten{,} considéré'
C[16]['reading']=r'e_{E\deleted{/S}}'
C[17]['reading']=r'\deleted{, et une conséquence}'
dot=copy.deepcopy(D['r3']['changes'][14]);dot.update(reading='\\fill (237,633) circle[radius=.014cm];\n\\fill (233,640) circle[radius=.014cm];',crop=p3('04_abandoned_formula'),evidence='The main abandoned-formula crop also shows two distinct tiny black dots to its left, offset downward and slightly leftward. Main retains r3’s two drawn points without interpreting them as punctuation or a mathematical sign.',readers={'r1':'No separate dots in complete reading','r2':'No separate dots in complete reading','r3':'Two isolated ink dots, drawn separately'},mathematical_consequence='')
C.insert(4,dot)
# Inventory in physical source order, using the most complete independent list.
inv=copy.deepcopy(D['r3']['inventory'])
for q in inv:
    for k in ['first_words_or_objects','position']:
        q[k]=q[k].replace('mu/psi','psi').replace('en mu','en psi').replace('phi(mu(x,y),mu(z,t))=mu(phi(x,z),phi(y,t))','phi(psi(x,y),psi(z,t))=psi(phi(x,z),phi(y,t))')
    if q['first_words_or_objects']=='Cancelled /S or /Q tail':q['first_words_or_objects']='Cancelled /S tail, resolved'
    if q['first_words_or_objects']=='Comma and doubtful et une conséquence':q['first_words_or_objects']='Cancelled comma and et une conséquence, resolved'
idx=next(i for i,q in enumerate(inv) if q['first_words_or_objects']=='phi(gx,y) ... terminal phi(')
extra=copy.deepcopy(inv[idx]);extra.update(kind='deletion',first_words_or_objects='Typed x overstrike and long horizontal cancellation across abandoned formula');inv.insert(idx+1,extra)
idx=next(i for i,q in enumerate(inv) if q['first_words_or_objects'].startswith('et de façon symétrique'))
extra=copy.deepcopy(inv[idx]);extra.update(kind='insertion',hand='another named or unnamed hand',position='After E before considéré in the symmetric-extension line',first_words_or_objects='Handwritten comma');inv.insert(idx+1,extra)
for i,q in enumerate(inv,1):q['element']=f'027-{i:02d}'
cd=copy.deepcopy(D['r2']['c_doubts'])
cm={1:1,2:2,3:3,5:4,7:7,8:10,9:12,10:16,12:17}
# cm refers to the original r2 ordering, before the dot row was interleaved.
for q in cd:
    ids=[int(i[1:]) for i in q.get('c_mark_ids',[])]
    if len(ids)==1 and ids[0] in cm:
        j=cm[ids[0]];q.update(crop=paths[j],evidence=ev[j])
    if ids==[4,6]:q.update(crop=p3('04_abandoned_formula'),evidence='Both equality slots are overlapped by x strokes and horizontal cancellation. Main retains each tentative equality independently; neither complete pair of bars can be isolated securely.')
    if ids==[11]:q.update(crop=p3('12_eE_revision'),evidence='The replacement close after E is distinct, while the former Gamma-argument tail is covered by typed x marks and pen hatching. S/P/Q cannot be distinguished securely there; it is not inferred from the resolved lower subscript.')
    if not ids:
        if 'associativité' in q['locus']:q.update(crop=pm('01_cancellation_paths'),evidence='All three full readings preserve the cancelled a between l and the apostrophe; the body crop also shows it. No grammatical normalization is made.')
        else:q.update(crop=p3('04_abandoned_formula'),evidence='The abandoned row ends with phi and an opening parenthesis; no following argument or close is present.')
un=copy.deepcopy(D['r2']['unresolved'])
notes=[
 {'id':'s027-note01','text':'Cancelled typescript draft, manuscript page 19, sections 2.1.1–2.2.3, with the added title Sections unité. The final sentence ends at on note. No date or total page count appears. The archive number is 26 in the opposite orientation, retained only in a comment. H supplies a description only, so this page has no H collation rows; its tentative 92 is an orientation issue in that description.','basis':'Three full readings; main archive-number crop; source conventions.'},
 {'id':'s027-note02','text':'The page describes two partially defined composition laws on a G_(P×Q)-torsor E, states equivariance and interchange formulas, and introduces two unit sections followed by a common neutral section. The abandoned scalar formula is preserved through its unfinished phi(. These are reports of source content, not proofs of the full biextension definition.','basis':'Opening, (2.1.1.1), (2.1.1.2), and 2.2; all three complete readings and main discrepancy crops.'},
 {'id':'s027-note03','text':'Main reads the second-law sign as psi at the opening, in the following prose, and at all three occurrences in the interchange formula, from the pen shaft through the interior of each typed u-shaped cup. r2 agrees; r1/r3 retain mu/psi initially and use mu at the recurrences under the recurring-sign convention. The separate circled marginal psi/Psi remains uncertain as to case. The mathematical form of the law does not decide these glyphs.','basis':'Main opening-law, prose-law, interchange, and marginal crops, each viewed once.'},
 {'id':'s027-note04','text':'The c/s, G/g, and C/c initial overprints retain both possible strike orders. The repeated E and its separately cancelled t are distinguished. In the final display the cancelled lower tail is resolved as /S, but the separately cancelled argument tail remains /S), /P), or /Q). The words et une conséquence and their leading comma remain cancelled and are resolved from the surviving type.','basis':'Main enlarged correction and final-formula crops; no earlier draft is reconstructed.'},
 {'id':'s027-note05','text':'The six page-wide cancellation paths, two local hooked curves, left oval, small isolated dots, and the insertion placements are drawn. A cancelled unreadable cursive word below typed De plus, is retained. Main also distinguishes the handwritten comma after the second unit paragraph’s E. No words on this page explicitly mark a mathematical step as unverified; the cancelled state by itself is not a refutation.','basis':'Main graphic and local crops, plus all three complete inventories.'},
 {'id':'s027-note06','text':'The source explicitly pairs 1_P×Q with e_(E/P), and P×1_Q with e_(E/Q), although its preceding displays give e_(E/P)∈Hom_P(P,E) and e_(E/Q)∈Hom_Q(Q,E). The main mathematical domain check prompted a crop of the pairings; the ink confirms both. All source pairings and indices are retained unchanged.','basis':'Main unit-display crops and 05_axis_pairings; this note establishes what the source says.'},
 {'id':'s027-note07','text':'A targeted coordinate check of the interchange display passes under the page’s stated partial group-law conventions. With x,y,z,t over (p,q),(p,q′),(p′,q),(p′,q′), both phi(psi(x,y),psi(z,t)) and psi(phi(x,z),phi(y,t)) are defined over (pp′,qq′). This checks domains and indices only; it does not prove existence of a biextension structure.','basis':'Actual direct main-reader coordinate check, decisions/scan027_math_work.md, connected to the observed display.','event_type':'targeted proof check','event_outcome':'Passed conditionally: all inner and outer operations have matching required coordinates, and both sides lie over (pp′,qq′). No existence or full-axiom theorem proved.'},
 {'id':'s027-note08','text':'Under the extension conventions stated immediately above, the source’s two named unit sections are paired with the opposite axes. For a concrete test, let S be a point, P=Z/2, Q=Z/3, G trivial, E=P×Q. Then e_(E/P)(p)=(p,0_Q) lies on P×1_Q and has domain P; it cannot be the named section over 1_P×Q, whose domain is Q. The second pairing is reversed in the same way. This refutes the literal pairing under those conventions, without changing the transcription or using an external version.','basis':'Actual main-reader domain argument and explicit finite-group counterexample in decisions/scan027_math_work.md; refined statement s027-note09.','event_type':"refuted, with the refined statement's id",'event_outcome':'Literal named-section/axis pairing is refuted under the page’s own extension conventions by E=(Z/2)×(Z/3), G trivial. Refined statement: s027-note09.'},
 {'id':'s027-note09','text':'The refined conditional statement pairs e_(E/P) with P×1_Q and e_(E/Q) with 1_P×Q. Each follows directly by composing the relevant group-extension unit with its projection. Equivalently, one may keep the source’s axes in their order and interchange the names of the two sections. This is a research note only.','basis':'Main-reader check of unit-domain and projection definitions; does not replace the source wording.','event_type':'targeted proof check','event_outcome':'Passed conditionally from the stated extension projections: the unit over P projects to (p,1_Q), and the unit over Q projects to (1_P,q).'},
 {'id':'s027-note10','text':'A limited targeted proof confirms equality of the two units on the common-origin fibre from interchange and the unit axioms. If a is the phi-unit and b the psi-unit there, then a=phi(a,a)=phi(psi(a,b),psi(b,a))=psi(phi(a,b),phi(b,a))=psi(b,b)=b. This does not supply the missing continuation after on note or verify the whole construction.','basis':'Actual main-reader argument in decisions/scan027_math_work.md.','event_type':'targeted proof check','event_outcome':'Passed conditionally on the displayed interchange identity and two unit axioms, restricted to the common-origin fibre; each equality follows from a unit identity or interchange.'},
 {'id':'s027-note11','text':'The partial group structures, their units, their projection maps, and the asserted interchange identity are assumptions for these limited checks. Their existence and the full biextension axioms were not independently proved in this run.','basis':'Explicit scope of the main mathematical checks.','event_type':'carried as background without fault found','event_outcome':'Stated partial group structures and interchange used conditionally as hypotheses; no independent existence or axiomatization proof.'}
]
nt=copy.deepcopy(D['r2']['notation'])
nt[0].update(evidence='Main separately inspected the opening cup-and-shaft form, the prose occurrence, and all three interchange occurrences; each supports psi. Marginal glyph case remains uncertain.',alternatives='Marginal sign only: psi or Psi.')
nt.append({'sign':'Handwritten punctuation after typed E','latex':r'$E$\handwritten{,}', 'locus':'Symmetric unit-section prose','evidence':'Main crop 03: a long curved tapering comma, separate from the typewriter glyphs.','alternatives':'None for the comma; hand attribution is medium confidence.'})
ad=[{'locus':'Unit sections and both axes in En particulier paragraph','readers':{r:'1_P×Q par e_(E/P); P×1_Q par e_(E/Q)' for r in D},'reading':'1_P×Q par e_(E/P); P×1_Q par e_(E/Q)','evidence':'The mathematical domain mismatch triggered main inspection of both unit displays and the axis paragraph. The crop confirms exactly the unanimous source reading; the refined mathematical statement is confined to notes.','crop':pm('05_axis_pairings')},
 {'locus':'Ordinary insertion calls for Sections unité, De plus, and donc','readers':{'r1':'Attachments encoded; De plus placed in a local figure','r2':'All three calls drawn with the page geometry','r3':'All three calls drawn with the page geometry'},'reading':'r3 common-coordinate drawing and source attachments','evidence':'The body graphic and De plus crop confirm the three short calls. Ordinary attachment versus explicit call drawing is not counted as a new textual difference by itself.','crop':pm('01_cancellation_paths')}]
viewed=[p3(s) for s in ['01_margin_psi','03_deleted_j','04_abandoned_formula','05_ces','07_E_correction','10_Groupe','11_De_plus_Ces','12_eE_revision','13_deleted_phrase','08_membership_P','09_membership_Q']]+[p2(s) for s in ['03_initial_second_law','07_interchange_graphic','01_archive_number']]+[pm(s) for s in ['01_cancellation_paths','02_prose_second_law','03_symmetric_comma','04_de_underline','05_axis_pairings']]
assert len(viewed)==len(set(viewed))==19
for c in C:assert set(c['readers'])=={'r1','r2','r3'},c['locus']
cfg=dict(approved_by_main_reader=True,scan=27,base_reader='r3',brief_version='v010',changes=C,c_doubts=cd,unresolved=un,inventory=inv,notes=notes,notation=nt,abbreviations=D['r3']['abbreviations'],complete_tex=tex,main_crop_count=len(viewed),main_viewed_crops=viewed,adjudications=ad,workflow_observation='Three fresh independent readers used v010 and the cumulative notation snapshot. All three complete readings and reports were compared. Main viewed 14 existing crops and five new crops, once each. The new body crop targets page-spanning cancellation geometry; other new crops target distinct prose glyph, comma, underline, and mathematically suspicious axis pairings. Rotated whole/half derivatives were moved outside the deliverable tree after an identical operational reminder, without reopening; v011 records that storage rule. No source view was repeated and no OCR or external research was used.',adjudication_note='r3 supplies the complete page geometry and physical-order inventory. Main adopts r2 psi readings and the resolved lower /S and bottom phrase, adds the handwritten state of the comma, and retains marginal case and Gamma-tail uncertainty. H has description only and contributes no collation rows. Mathematical checks and their assumptions are explicitly separated from the ink decisions.')
(R/'decisions/approved_scan027_config.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(C),'inventory':len(inv),'c_marks':sum(len(q.get('c_mark_ids',[])) for q in cd),'resolved_marks':sum(len(q.get('c_mark_ids',[])) for q in cd if q['decision']=='resolved'),'main_views':len(viewed)},indent=2))
