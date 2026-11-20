from decision_helpers import *
import copy
r=load_reports(176)
diffs=[row(r,'A',i) for i in range(19)]
crops={1:'C/L5_cancelled_and_la_donnee.png',2:'C/L5_cancelled_and_la_donnee.png',3:'C/L6_dun_addition.png',4:'C/L6_dun_addition.png',5:'C/L6_F0_bar.png',6:'main/01_L8_operator.jpg',7:'C/L11_quici.png',8:'main/02_L11_inclusion_letter.jpg',10:'C/L13_cancelled_une.png',13:'B/d01_left_isolated_stroke.png',14:'C/L18_shorthand.png'}
for i,p in crops.items():diffs[i]['crop']='crops/scan176/'+p
for i in [0,6,8]:
 diffs[i]['evidence']+=' Main inspected this occurrence independently: the tall undotted stem and extended left-returning foot support A’s capital-like preferred reading, while j remains an alphabet alternative at L2.'
diffs[14]['evidence']='The lower stroke has an initial downward bowl, an upward return and a low rise beneath a separate bar, matching the clearer repeated shorthand in L19. These curved letter strokes distinguish it from a plain equals sign. Root selects A’s resolution to barred m over B/C’s retained equality alternative.'
diffs[13]['kind']='drawing or diagram'
# C and H are compared by preferred reading/state; merely spelling out the case
# of a secondary alternative is not a further change to the cancelled word.
comparisons=[
 {'place':'L2 operator, L8 operator, and L11 inclusion letter','A':r'\unsure{J|j} at L2; J thereafter','B':'j at all three occurrences','C':'j at all three occurrences','decision':'Select A’s preferred J with j retained. Main inspected A/l02_operator.png and two new tight crops independently. All three forms are undotted, extend high, and return broadly left at the bottom; L8 also has the high angled entry seen in the primed diagram labels. Case is not claimed certain.'},
 {'place':'L5 cancelled symbol-shaped alternatives','A':'Il / Il s’ / J; peut / peut se / J*','B':'Il / Il s’ / j; peut / peut se / j*','C':'Il / Il s’ / j; peut / peut se / j*','decision':'Retain the common preferred words and all alternative shapes. J in the secondary alternatives follows the live J/j convention marked at L2; it does not resolve the cancelled groups. The tall curved cap/stem and the next descender survive, but cancellation merges the following joins (C/L5_cancelled_and_la_donnee.png).'},
 {'place':'First diagram primed horizontal label','A':'J′; case doubt already at L2','B':r'\unsure{J|j}′','C':r'\unsure{J|j}′','decision':'All favour J but leave its case open. Use J′ here because the page’s first J/j doubt is now marked at L2. The crop has a high angled entry, broad lower loop, and one separate prime (A/diagram1.png).'},
 {'place':'L18 first shorthand','A':r'\overline m','B':r'\unsure{\overline m|=}','C':r'\unsure{\overline m|=}','decision':'Select A’s resolution. The lower curled entry and low rise are letter strokes, matching the immediately repeated shorthand; two simple equality rules do not account for them (C/L18_shorthand.png and A/l19_shorthand.png).'},
 {'place':'Isolated mark beside first lower target','A':'small bent stroke, origin uncertain','B':'small bent stroke, origin uncertain','C':'small bent stroke, origin uncertain','decision':'All agree on presence and uncertainty of origin. Main sees a coherent compact dark bent stroke distinct from pale grain (B/d01_left_isolated_stroke.png). Use C’s filled contour at an approximate left-of-X0 anchor; wrapper differences are typesetting only.'},
 {'place':'H editorial page-location note','A':'entire lower diagram visible here; exclude note from manuscript collation','B':'entire lower diagram visible here; editorial-difference row','C':'entire lower diagram visible here; editorial-only row','decision':'The main crop A/diagram2.png confirms the full upper row, both hooks, both labels and edge-adjacent target. Record the incorrect editorial location claim in notes, not as an extra manuscript collation row: H already supplies the same diagram at this location.'}
]
unresolved=copy.deepcopy(r['A']['unresolved'])
unresolved.append({'place':'D4a, left of first diagram lower target','reading':'compact bent dark stroke reproduced','alternatives':['authorial incidental ink','later or reproduction mark'],'confidence':'low','reason':'Its physical shape is distinct, but neither origin nor function is identifiable.'})
review=[]
for q in r['A']['C_doubt_review']:
 e=q['evidence']
 p=q.get('crop')
 mapping={
 'crops/scan176/A/l05_replacement.png':'crops/scan176/C/L5_cancelled_and_la_donnee.png',
 'crops/scan176/A/l06_article.png':'crops/scan176/C/L6_dun_addition.png',
 'crops/scan176/A/l06_f0.png':'crops/scan176/C/L6_F0_bar.png',
 'crops/scan176/A/l11_quici.png':'crops/scan176/C/L11_quici.png',
 'crops/scan176/A/l13_cancelled.png':'crops/scan176/C/L13_cancelled_une.png',
 'crops/scan176/A/l18_shorthand.png':'crops/scan176/C/L18_shorthand.png'}
 if p:e+=' Main inspected '+mapping.get(p,p)+'.'
 else:e+=' All three independent full-resolution half readings agree on these signs and placement.'
 review.append({'place':q['source_question'],'earlier':q['source_question'],'decision':q['status']+': '+q['final'],'evidence':e})
notes=r'''**S176-notes.** The page identifies the gluing operation as \(\varphi(F_1)\simeq p_*J^*(\widetilde F_1)\), with the second sheaf obtained by restriction. It states that this restriction is an equivalence for the locally constant sheaves under discussion. It then rewrites the gluing datum as \(F_0,\widetilde F_1,\widetilde u:p^*F_0\to J^*\widetilde F_1\). The letter-case choice is diplomatic: the undotted tall hooked forms favour J, with j retained at the first occurrence.

All three readers made the limited adjunction check **S176-adjoint-datum**. Conditional on the displayed identification and \(p^*\dashv p_*\), put \(G=J^*\widetilde F_1\). The map u corresponds to \(\epsilon_G\circ p^*u\), and the inverse assignment is \(p_*\widetilde u\circ\eta_{F_0}\). The triangle identities make these assignments inverse. A/B explicitly wrote these maps; C checked the corresponding Hom adjunction. This does not establish the claimed restriction equivalence or geometric hypotheses. The apparent bar on F_0 prompted visual review, but plain F_0 is chosen because the crop contains only the letter’s two arms, with its upper arm detached.

The author recalls that p is a genuine fibration and the other map an inclusion, with the boundary-of-a-manifold interpretation qualified by “et pratiquement, – cas X_0, X_1 lisses –”. He offers another span “Si on préfère”, describing it as “un peu moins joli (mais un peu plus canonique)”, then proposes replacing X_0 by T because X_0 is a deformation retract. These assertions were not proved. The three readers’ **S176-diagram-sources-targets** checks only compare the common source, unchanged right target, and proposed replacement of the lower target. They do not establish a homotopy equivalence and do not settle the foot glyph’s T/I ambiguity.

Root resolves qu’ici, cas, plain F_0 and the first barred-m shorthand. The two cancelled groups, the lower e-like addition, the cancelled une and the edge-adjacent T/I remain doubtful. The baseline un is live; the pointed lower attachment is not treated as a strike through it. One separate dark bent stroke is reproduced without assigned meaning or authorship. The crowded start of pratiquement was independently reviewed by A/C as joined or retraced letters, with no additional cancelled word; all three complete readings agree.

The diagram crops place p′ and p″ to the right of their downward arrows. The first diagram has ordinary arrows and the second has two source hooks. H’s editorial assertion that most of the lower diagram lies on the next author page is contradicted by the complete configuration visible here; this editorial error is recorded here rather than counted as manuscript text. Author page **31**, archive pencil **176**, bears no title or date. There are 21 main baselines (including two displays), eight diagram rows, and two additions. A new paragraph starts at Si on préfère; the opening haut continues the preceding sentence. No explicit authorial mathematical doubt is stated.
'''
text=(ROOT/'records/scan176/A/reading.tex').read_text()
ctext=(ROOT/'records/scan176/C/reading.tex').read_text()
start=text.index('% Small isolated bent mark');end=text.index('X_0 \\&',start)
cstart=ctext.index('% Small isolated dark stroke');cend=ctext.index('X_0 \\&',cstart)
text=text[:start]+ctext[cstart:cend]+text[end:]
viewed=['C/L5_cancelled_and_la_donnee.png','C/L6_dun_addition.png','C/L6_F0_bar.png','C/L11_quici.png','A/l12_cas.png','C/L13_cancelled_une.png','A/l02_operator.png','A/diagram1.png','A/diagram2.png','C/L18_shorthand.png','A/l19_shorthand.png','B/d01_left_isolated_stroke.png','main/01_L8_operator.jpg','main/02_L11_inclusion_letter.jpg']
d=write_decision(176,'A',[],diffs,comparisons,unresolved,r['A']['inventory'],notes,r['A']['abbreviations'],review,['crops/scan176/'+p for p in viewed],brief='briefs/brief_v07_scan176.md',workflow_note='Three fresh readers completed whole/a/b once each, all 21 main baselines, eight diagram rows, two additions, cancellations and page numbers. A made 13 crops, B 10, C 10. Main reused twelve saved crops and made two targeted crops for separate J/j disagreements. All fourteen main images displayed successfully once. The explicit no-compilation rule was followed by all three readers. H’s incorrect editorial page-location claim is kept in notes, not counted as manuscript collation.',text_override=text)
for e in d['check_events']:
 if e['statement_id'] in ['176-adjoint-datum','MS176.ADJ','176-L2-L8-adjunction-reexpression']:e['statement_id']='S176-adjoint-datum'
 if e['statement_id'] in ['176-diagram-sources-targets','MS176.DIAGRAM-TARGETS','176-D1-D2-source-target-replacement']:e['statement_id']='S176-diagram-sources-targets'
(ROOT/'records/scan176/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Undotted inclusion/pullback letter',r'\unsure{J|j} at first occurrence; J, J^*, J′ subsequently','176 L2/L8/L11 and both diagrams: tall undotted stem and broad left return, sometimes with high angled entry. Root separately cropped the two later disputed unprimed occurrences; do not infer case from mathematical convention.'),
 ('F with detached upper arm',r'F_0, without overbar','176 L6: only two horizontal arms in total; the disconnected top stroke is the upper arm, not a third stroke.'),
 ('Barred-m shorthand',r'\overline m','176 L18–19: initial lower bowl, upward return and low rise distinguish the shorthand from two plain equality bars; both occurrences resolved.'),
 ('Downward span labels','p′ and p″ on right of shaft','176 both diagrams: first arrow plain, second hooked; prime counts and right-side positions visible.')
])
register_note_statements(176,[
 {'place':'L2–L5; notes paragraph 1','statement':'The manuscript identifies the gluing functor with p_*J^* after restriction, and asserts equivalence of the relevant locally constant sheaf categories under restriction.'},
 {'place':'L6–L10; notes paragraphs 1–2','statement':'The gluing map can be expressed as p^*F_0 to J^*Ftilde_1.','status':'source assertion; conditional adjunction correspondence checked separately as S176-adjoint-datum'},
 {'place':'L11–L14; notes paragraph 3','statement':'The manuscript calls p a genuine fibration and J an inclusion, with a boundary-manifold description in the smooth case.'},
 {'place':'L15–L21 and both diagrams; notes paragraph 3','statement':'The alternative spans are said to use homotopic spaces, and X_0 may be replaced by T because it is a deformation retract.','status':'source assertion not proved; local configuration check indexed separately as S176-diagram-sources-targets'}
])
