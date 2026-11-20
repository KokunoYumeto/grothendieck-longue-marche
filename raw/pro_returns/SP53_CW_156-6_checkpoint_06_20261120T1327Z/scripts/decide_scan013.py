"""Main reader's crop-adjudicated scan013 decisions. Never rerun after commitment."""
import copy,json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan013.json'
if p.exists() and json.loads(p.read_text()).get('committed'):raise SystemExit('Already committed')
rs=[json.loads((O/f'readers/scan013/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
m1=list(range(17))+[None,17,18,19,20,21,22,None,None,None,None,None,23,24,25,26,27]
m2=list(range(19))+[19,19,20,21,22,None,None,None,None,None,24,25,None,26,27]
rows=[]
glyph=r'\mathrel{\tikz[baseline=0pt,x=1em,y=1em]{\draw (-.38,.62)--(.38,.25)--(-.43,-.10); \draw (.34,.62)--(-.32,.25)--(.38,-.10);}}'
for i,x in enumerate(c):
    r=copy.deepcopy(x);r['final']=r.pop('reading');r['mathematical']=False
    for k in ['crop_box','crop_source']:r.pop(k,None)
    r['readers']={'R1':a[m1[i]]['reading'] if m1[i] is not None else (glyph if i in range(24,29) else r'\substack{X\in\mathcal F\\X\ne\varnothing_{\mathcal F}}'),
                  'R2':b[m2[i]]['reading'] if m2[i] is not None else (glyph if i in range(24,29) else 'Narrow closed sloping frame with three hatches; label outside, as constructed in reading.tex.'),
                  'R3':x['reading']}
    rows.append(r)
def rp(reader,name):return f'readers/scan013/{reader}/crops/{name}.jpg'
def main(name):return f'crops/scan013/{name}.jpg'
def put(i,**kw):rows[i].update(kw)
put(0,crop=rp('R3','01_opening_correction'),evidence='Main sees a p descender, reduced r and small terminal loop under the strike; pre is slightly favored, but the last loop may be the cancellation return. The separate dotted i and tall l belong to live inclure. Retain pre/pr against R1/R2’s reverse ordering; H’s prendre merges canceled and live matter.')
put(1,crop=rp('R3','02_cancelled_b_prose'),evidence='The two-level ≤ sign remains readable under the cancellation. H leaves this readable sign as an unreadable token.')
put(2,crop=rp('R3','02_cancelled_b_prose'),evidence='The beginning and final ent course support déterminent, but the strike obscures the compressed middle. Main retains the word-level doubt rather than promoting H’s certainty.')
put(3,c=r'\unsure{déterminent} $\preccurlyeq$',against_C=False,crop=rp('R3','02_cancelled_b_prose'),evidence='The ink proceeds from the canceled verb directly to the curved order sign. No independent extra word survives between them; H’s additional unreadable token is not supported.')
put(4,crop=rp('R3','03_cancelled_equation_initial'),evidence='The initial letter has an arched upper course and lower bowl/return, not two F arms. Main resolves G as R2/R3, against R1’s retained G/F doubt.',confidence='high')
put(5,crop=rp('R3','04_124a_arrow'),evidence='Both end traces and crossing cancellation loops remain. A right head is clear, but the left return cannot be securely assigned to the earlier or live layer. Main retains C and all three readers’ two layered alternatives. H’s overwrite note is credited; its definite live equivalence is not established.')
put(6,crop=main('01_124a_empty_F'),evidence='At the right edge, the subscript has a straight stem and two rightward arms without a returning family foot. Main confirms ordinary F; the nearby dark page edge does not change those strokes.',mathematical='The empty-figure subscript in (1.24)a is literally ordinary F, not the family alphabet supplied by H.')
put(7,crop=rp('R3','05_124b_operator'),evidence='Live Sup and its ll index are clear. Extra covered bars and uprights support an older operator but do not separate Inf from S. Retain the canceled alternatives that H omits.')
put(8,crop=main('02_124b_criterion'),evidence='The final subscript in row b has a straight F stem and right arms, without the family’s returning foot. The same crop confirms a clear equivalence, Sup_ll(F,G) existe, et Inf_ll F,G, with no parentheses supplied after the latter Inf.',mathematical='The empty-figure subscript in (1.24)b is literally ordinary F, not the family alphabet supplied by H.')
put(9,crop=rp('R3','06_margin_verifier'),evidence='Adequate white space above the first e contains no acute; the tall later stroke is the f. Main resolves unaccented Verifier and preserves its rightward arrow.',confidence='high')
put(10,crop=main('03_NB_underline'),evidence='A separate horizontal rule runs beneath NB. Main confirms the underline, absent from H’s transcription.')
put(11,place='NB: first family-F subscript',c=r'\unsure{\mathcal{F}|\mathscr{F}}',h=r'\mathfrak{F}',final=r'\unsure{\mathcal{F}|\mathfrak{F}}',crop=rp('R3','07_NB_family_subscript'),evidence='A returned foot, crossed middle arm and broad cap distinguish the family letter. The exact printed alphabet is underdetermined. Main keeps the established mathcal/fraktur candidates, agreeing with all three readers rather than C’s mathscr alternative or H’s unqualified fraktur.')
rows[11]['readers']={k:r'\unsure{\mathcal{F}|\mathfrak{F}}' for k in ['R1','R2','R3']}
put(12,crop=rp('R3','08_NB_element_abbreviation'),evidence='The initial e has no detached acute, while the later acute is visible. The reduced middle could be abbreviated mt or compressed ment. Main retains elémt/elément as R2/R3, eliminating R1’s first-e-accent candidates.',confidence='medium')
put(13,crop=rp('R3','09_125_interventions'),evidence='Below the live membership sign, a separate basal bar survives beneath the small angle. Main resolves deleted ≤ as R2/R3, against R1’s ≤/< alternatives; H omits the old sign.',confidence='high')
put(14,crop=rp('R3','09_125_interventions'),evidence='Two upright tracks favor H. The central connection is crossed by a diagonal cancellation, so K cannot be excluded. Main retains H/K as R2/R3 against C/R1’s reverse preference.')
put(15,final='ens',against_C=True,crop=rp('R3','10_ens_abbreviation'),evidence='The low e-n-s course is legible, and the following gap contains no period. Main resolves ens as R1/R2 against R3/C’s doubt and H’s added point.',confidence='high')
put(16,crop=rp('R3','11_minimaux'),evidence='The initial retraced m, the dotted i positions and the au/x ending are separable. Main resolves minimaux; darkening of the m does not establish a distinct deletion.',confidence='high')
put(17,crop=main('04_126_stacked_conditions'),evidence='X in family F sits above X not equal to the empty family figure. There is no comma after the upper family F before the vertical separator. Main preserves the stack and absence of H’s added comma; the individual font occurrences are logged separately.')
put(18,crop=rp('R3','12_126_final_subscript'),evidence='The cap is looped and a crossbar survives, but the lower stem is comparatively straight without a secure returning family foot. Keep the local mathcal F/F/f alternatives; the meaning of the criterion does not decide the glyph.')
put(19,crop=rp('R3','13_un_lieu'),evidence='The short opening word is two low joined letters u-n, not the much longer Chaque. Main confirms un.')
put(20,crop=rp('R3','13_un_lieu'),evidence='After li-e, the final low return does not reliably distinguish u from n. Main retains lieu/lien despite the familiar mathematical word and H’s certain lieu.')
put(21,crop=rp('R3','14_figure_underline'),evidence='The low leftward line is continuously connected to the g descender; it is not a separate underline. Main adopts plain figure with C/R2/R3 against R1’s underline and H’s emphasis.')
put(22,crop=main('05_barred_m'),evidence='After elle and a hyphen there is one m with a detached bar above it, followed by the closing parenthesis and point. Preserve the written abbreviation instead of H’s expanded même.')
put(23,place='Canceled prose before first (1.27): initial word',c='Ceci',h='On',final='Ceci',against_C=False,crop=rp('R2','13_cancelled_ceci_dit'),evidence='A large curved C is followed by e-c-i, not O-n. Main confirms Ceci. The separate punctuation issue after dit is logged independently.')
rows[23]['readers']={k:'Ceci' for k in ['R1','R2','R3']}
for i,name in [(24,'06_canceled_prose_compatibility'),(26,'08_reservation_compatibility'),(27,'09_final_item_compatibility'),(28,'10_final_formula_compatibility')]:
    put(i,crop=main(name),evidence='Main sees two opposed zigzags crossing above and below an open central diamond, with four free ends and no enclosing horizontal caps. This is a geometry difference from H’s printed between glyph, not a macro-name difference. The same relational meaning is not disputed.')
put(25,crop=rp('R3','15_cancelled_127_initial'),evidence='Beside the initial F, the compatibility glyph has opposed zigzags, a central diamond and free diagonal ends. Preserve that drawn geometry despite the overlaid cancellation; H’s printed between form differs in geometry, not inferred relational meaning.')
put(29,crop=rp('R3','15_cancelled_127_initial'),evidence='A vertical stem and two right-facing arms survive the oblique hatch. Main resolves F as R2/R3, against C/R1’s F/G doubt.',confidence='high')
put(30,crop=rp('R2','15_cancelled_127_end'),evidence='The first character is a curly opening brace, not an existential sign. The following V has two oblique arms without an internal crossbar; the line crossing its vertex is the enclosure bottom. The taller neighboring descender belongs to implique above. Preserve the literal unfinished {V.',confidence='high',mathematical='The abandoned formula ends with literal opening brace and V. It is not an existential or universal quantified statement, and no completion is supplied.')
put(31,final='Wide sloping enclosure crossing the left part of the (1.27) label, with upper-left gap, four ascending hatches and top rule continuing through the preceding prose.',crop=main('07_cancellation_enclosure'),evidence='The frame extends left through the display label; its opening parenthesis protrudes outside the left boundary. A small upper-left gap is visible, and the top strike continues beyond the right side as the preceding prose cancellation. Four ascending oblique hatches remain distinct, including the one beside the prose descender. Adopt R3’s broad four-hatch construction, with explicit label-straddling placement; reject C/R2’s small formula-only frame and R1’s closed-corner reading. H is credited for explicitly reporting a box and hatching, but it does not reproduce them in a drawing.',confidence='high')
put(32,crop=rp('R3','17_circled_item'),evidence='The outer circle is secure. Its retraced central loop and bar remain compatible with e or a minus-in-circle form. Keep the alternatives. H’s explicit circling note is credited; only the uncertain inner mark differs.')
put(33,crop=rp('R3','18_final_arrow'),evidence='The left arrowhead is clear. The right end is a closed loop without a securely separate second head. Retain leftward/bidirectional alternatives rather than adopting H’s expected equivalence.')
comma=copy.deepcopy(b[23]);comma['final']=comma.pop('reading')
for k in ['crop_box','crop_source']:comma.pop(k,None)
comma.update(readers={'R1':'Ceci dit','R2':'Ceci dit','R3':'Ceci dit,'},c='dit,',h='dit',final='dit',against_C=True,against_H=False,confidence='high',crop=rp('R2','13_cancelled_ceci_dit'),mathematical=False,evidence='No separate comma follows dit. The nearby descending stroke belongs to the cancellation hatch. Main adopts R1/R2’s absence of a comma against C/R3.')
fontspec=[
 ('NB: family F after de',main('11_NB_de_family'),'Broad curved detached cap, crossing middle arm and left-returning foot.'),
 ('(1.25): family F after live membership',rp('R3','09_125_interventions'),'Cap, cross arm and returned foot of the domain family are visible beside the separate canceled capital.'),
 ('d): first family F, after inclusion',main('12_d_first_family'),'Looped sweeping cap, crossing middle arm and hooked foot distinguish the tall family F.'),
 ('d): family F before set difference',main('13_d_nonempty_family'),'Crossing middle arm and hooked foot are visible; the cap overshoots the tight crop, but the local shape comparison remains sufficient.'),
 ('d): empty-figure family subscript',main('13_d_nonempty_family'),'The small F has a broad cap, crossbar and sharply returned lower foot.'),
 ('(1.26): family F in upper X membership',main('04_126_stacked_conditions'),'The upper X-domain letter has a broad cap and crossed middle arm.'),
 ('(1.26): family subscript below X nonempty condition',main('04_126_stacked_conditions'),'The lower small F has a broad cap and a returned foot.'),
 ('(1.26): family F after Y membership',main('04_126_stacked_conditions'),'The Y-domain family has a broad cap, cross arm and returning foot.')]
fonts=[]
for place,crop,ink in fontspec:
    fonts.append(dict(place=place,c=r'\mathcal{F}',h=r'\mathfrak{F}',final=r'\mathcal{F}',against_C=False,against_H=True,kind='misread symbol or index',marked_in_H='no',confidence='medium',crop=crop,evidence=ink+' Use the first candidate of the explicit initial family-font uncertainty; no new letter identity is inferred.',readers={k:r'\mathcal{F}' for k in ['R1','R2','R3']},mathematical=False))
# One locus per occurrence, ordered with the local text rather than bundled font rows.
ordered=rows[:13]+[fonts[0]]+rows[13:14]+[fonts[1]]+rows[14:15]+[fonts[2]]+rows[15:17]+fonts[3:5]+rows[17:18]+fonts[5:]+rows[18:24]+[comma]+rows[24:]
assert len(ordered)==43
for i,r in enumerate(ordered,1):r['id']=f'013-{i:02}'
tex=(O/'readers/scan013/R3/reading.tex').read_text().replace(r"l'\unsure{ens}","l'ens").replace('Ceci dit,','Ceci dit')
# The label's left parenthesis straddles the enclosure boundary, as the local crop shows.
tex=tex.replace(r'\node[anchor=west] at (-.3,-.02)',r'\node[anchor=west,inner sep=0pt] at (-.3,-.02)')
(O/'decisions/scan013_final.tex').write_text(tex)
cd=copy.deepcopy(rs[2]['c_doubts'])
links=[0,2,4,5,5,7,9,11,12,13,14,15,16,18,20,29,30,32,33]
resolved={2,6,9,11,12,15,16}
for j,i in enumerate(links):
    r=rows[i];cd[j].update(reading=r['final'],evidence=r['evidence'],crop=r['crop'],disposition='resolved' if j in resolved else 'retained')
    for k in ['crop_box','crop_source']:cd[j].pop(k,None)
cd[3]['reading']=r'\deleted{\unsure{\Longleftrightarrow|\Longrightarrow}}'
cd[4]['reading']=r'\unsure{\Longrightarrow|\Longleftrightarrow}'
inv=copy.deepcopy(rs[2]['inventory'])
inv[21]['first_words_or_objects']='Ceci dit ≪ implique la relation'
inv[23]['first_words_or_objects']='Wide sloping frame; label straddles left boundary; upper-left gap; four hatches; top strike continues through prose'
assert len(inv)==29
notes={'content':rs[2]['notes']['content'],
 'math_reading_decisions':[
 'The live equivalence in (1.24)b is clear. Both the layered (1.24)a arrow and final (1.27) arrow remain graphically uncertain. Mathematical expectation does not settle them.',
 'The empty-figure subscripts in (1.24)a and b are ordinary F. The NB begins a distinct footed family glyph whose precise printed alphabet remains uncertain. The final empty-figure subscript in (1.26) retains its separate family-F/F/f ambiguity.',
 'The second Inf in (1.24)b is followed by bare F,G. The X-membership and X-nonempty conditions in (1.26) are stacked, without H’s extra comma after the first family F.',
 'The old sign beneath live membership in (1.25) is ≤. The canceled following capital remains H/K. The abandoned (1.27) begins with F and ends with literal opening brace and V; it is not completed to a quantified formula.',
 'S row SA21-K6-06 correctly identifies the literal criterion and authorial Verifier note. Main checked only the finite-order component of its proposed example, using an explicit four-element relation: the order is reflexive, antisymmetric and transitive; a and b have supremum c and infimum empty, while their defined compatibility is false. This establishes the stated order/compatibility facts in that structure, not satisfaction of At 1–At 10 or the full atelier construction.',
 'The broader sweep claims, including the Atens 2 sufficient condition and the surviving one-way criterion under atelier axioms, were read but not proved. No theorem repair enters the diplomatic text.',
 'No verification of the full reconstructions in (1.25), (1.26), or final (1.27) was performed.'
 ],'author_doubts':rs[2]['notes']['author_doubts'],
 'titles_dates_counts':rs[2]['notes']['titles_dates_counts']}
events=[]
for i,r in enumerate(rs,1):
    for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan013 R{i}'))
for sid in ['scan013-(1.24)a','scan013-(1.24)b','scan013-NB','scan013-(1.25)','scan013-(1.26)','scan013-final-(1.27)','scan013-S-SA21-K6-06-atelier-axiom-claims']:
    events.append({'statement_id':sid,'type':'carried as background without fault found','outcome':'Read as the author’s or supplied sweep’s assertion; no mathematical verification of this claim under the atelier axioms was performed.','who':'GPT-6 Astra Pro; effort not exposed; main reader; scan013'})
events.append({'statement_id':'scan013-S-SA21-K6-06-finite-order-component','type':'computation or formal certificate','outcome':'Exhaustive finite computation on empty,a,b,c checked reflexivity, antisymmetry and transitivity of the specified refinement order; a,b have unique common lower bound empty and unique common upper bound c, and are incompatible by the specified relation. Hence order existence/empty-infimum facts alone do not establish compatibility. At 1–At 10, the full atelier construction, the surviving forward criterion, and Atens 2 sufficiency were not checked. Script: scripts/check_scan013_order_example.py; results: working/scan013_order_example_check.json.','who':'GPT-6 Astra Pro; effort not exposed; main reader; scan013'})
s=[{'id':'SA21-K6-06','disposition':'partly confirmed','reading':'Literal (1.24)b equivalence and Verifier → confirmed; finite-order component of S’s example computed; broader atelier-axiom conclusions unverified.',
    'evidence':'Main crop confirms the written equivalence and both order conditions; the existing Verifier crop confirms the checking note. The explicit computation has exactly the limited scope recorded in CHECK_EVENTS and does not license replacing the manuscript equivalence.', 'crop':main('02_124b_criterion')}]
un=[{'place':r['place'],'reading':r['reading'],'alternatives':'Explicit unresolved alternatives in the transcription; the canceled verb remains a single doubtful reading.','confidence':'medium','evidence':r['evidence']} for r in cd if r['disposition']=='retained']
assert len(un)==12
d={'scan':13,'mspage':'12','folder':'J156-6-02','filename':'J156-6-02_156-6_scan013.tex','brief':'v006','committed':False,'adjudicated_all':True,'differences':ordered,'adjudications':[],'c_doubts':cd,'s_rows':s,'inventory':inv,'notes':notes,'check_events':events,'unresolved':un,'abbreviations':rs[2]['abbreviations']}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('scan013 draft:',len(ordered),'difference loci;',sum(r['against_C'] for r in ordered),'against C;',sum(r['against_H'] for r in ordered),'against H;',len(inv),'inventory;',len(un),'remaining doubts')
