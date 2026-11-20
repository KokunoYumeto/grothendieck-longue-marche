from decision_helpers import *
import copy
r=load_reports(175)
diffs=[row(r,'C',i) for i in range(25)]
for i,p in [(2,'01_au_dessus_L9.jpg'),(4,'02_au_dessus_L10.jpg'),(22,'03_vertical_diagram.jpg')]:diffs[i]['crop']='crops/scan175/main/'+p
for i in [2,4]:diffs[i]['evidence']='The main-reader crop shows a clean word space between au and dessus, without a lexical hyphen.'
diffs[9].update(final=r'\to',differs_C=True,differs_H=False,evidence='The right end of the shaft rises and returns to form a distinct small closed loop, a terminal head rather than a plain line ending. Root selects A/B’s resolved arrow over C’s retained plain-line alternative.',confidence='medium')
diffs[11].update(final=r'\mathrel{\unsure{\mapsto|\vdash}}',differs_C=False,differs_H=True,evidence='The initial vertical bar is secure. The right end is a compact diamond-like thickening without separately discernible wings; it cannot securely be distinguished from a heavy pen stop. Root retains A’s mapsto/turnstile doubt against B/C’s resolution.',confidence='medium')
diffs[18].update(final=r'\unsure{du|des}',differs_C=False,differs_H=True,evidence='The d is followed by a connected low bowl and curled exit. Their merged joins do not securely distinguish u from an e-s sequence. Root retains A/B’s du/des doubt against C’s resolution; singular diagramme is not used as evidence.',confidence='medium')
diffs[22]['evidence']='The vertical shaft has a downward head over X_0. Fibration is physically to its left and p to its right, rather than a combined label on one side. The parenthetic comparison is a separate annotation left of the source object.'
for i in [0,10,16]:diffs[i]['kind']='drawing or diagram'
comparisons=[
 {'place':'L5 isolated left point','A':'omitted','B':'omitted','C':'nontext point reproduced','decision':'Select C. A compact dark oval/wedge is detached left of les, with a density comparable to the nearby pen strokes and distinct from faint grain. Its origin remains uncertain (C/l05_left_mark.png).'},
 {'place':'L14 first boundary relation','A':r'\to','B':r'\to','C':r'\unsure{\to|-}','decision':'Select A/B. The closed loop at the right tip is a distinct terminal decoration, unlike an undecorated shaft (C/l14_first_arrow.png).'},
 {'place':'L14 relation after x','A':r'\unsure{\mapsto|\vdash}','B':r'\mapsto','C':r'\mapsto','decision':'Retain A’s uncertainty. The left bar is clear, but the small right-end diamond-like thickening lacks independently separable arrow wings and can be a heavy pen stop (C/l14_mapsto.png).'},
 {'place':'L15 projection relation','A':r'\unsure{-|\to}','B':r'\unsure{\to|-}','C':r'\unsure{-|\to}','decision':'Select A/C’s order. The long shaft ends in an upright thick tick, without the clear looped head seen in the first relation. Keep the possible compressed arrow as the second candidate (C/l15_projection_arrow.png).'},
 {'place':'L22 article','A':r'\unsure{du|des}','B':r'\unsure{du|des}','C':'du','decision':'Retain A/B. The final connected belly and loop do not let u and e-s be separated securely (C/l22_du.png).'},
 {'place':'Diagram letter above horizontal arrow','A':r'\unsure{j|J}','B':r'\unsure{j|J}','C':r'\unsure{J|j}','decision':'Select C’s preferred order while retaining both cases. The high angled entry, broad returning lower loop and cross-stroke, without a detached dot, favour the capital form; an undotted cursive j remains possible (C/diagram_j.png).'},
 {'place':'Three nontext-mark wrappers','A':'two marks, zero-width wrappers','B':'two marks, zero-width wrappers','C':'three marks, zero-width wrappers','decision':'Retain all three physically distinct marks, with coordinate comments and uncertain origins. Wrapper differences are typesetting only; use one consistent zero-width form. No mark becomes an index, multiplication sign or punctuation.'},
 {'place':'Line numbering after diagram','A':'physical final baseline L27; prose-only L24 also supplied','B':'final baseline L25, counting one diagram object row','C':'final prose baseline L24; diagram D1–D5','decision':'Use C’s prose-only L1–L24 with separately named diagram places in the consolidated record. All three cover the same 24 prose baselines, replacement and complete diagram; this is an indexing difference, not omitted text.'}
]
unresolved=copy.deepcopy(r['A']['unresolved'])
for x in unresolved:
 if x['place']=='Diagram horizontal letter':x.update(reading='J',alternatives=['j'],reason='High angled entry and broad lower loop favour capital J, but an undotted cursive j is not excluded.')
for place,shape in [('L5 left margin','small dark point'),('L14 above first relation','small triangular point'),('L20 below source object','short dark tick')]:
 unresolved.append({'place':place,'reading':shape+' reproduced','alternatives':['pen mark','reproduction artefact'],'confidence':'low','reason':'The physical shape is distinct, but its origin and intended role cannot be identified.'})
review=[]
for item in r['C']['C_doubt_review']:
 dec=item['decision']; final=item['final']
 if item['place']=='L14 first relation':dec='resolved';final=r'\to'
 if item['place']=='L14 relation after x':dec='retained';final=r'\mapsto|\vdash'
 if item['place']=='L22':dec='retained';final='du|des'
 review.append({'place':item['place'],'earlier':item['C'],'decision':dec+': '+final,'evidence':'Main inspected '+item['crop']+'; stroke evidence and three-reader choices appear above.'})
review.append({'place':'L12, cone base','earlier':'T sur X, possibly X_0','decision':'Retain T sur X, as all three independent readers saw; no subscript is supplied.','evidence':'All three full-resolution half readings distinguish this unindexed X from the preceding X_0. The mathematics raises a base-convention issue but does not authorize a repair.'})
review.append({'place':'L3–4, L8–15, L19–20, diagram and final phi','earlier':'Double-stroke C; minus signs; amalgamation index; interval endpoint; tilde X and ring T; hook; comparison signs; labels and phi form','decision':'All three retain the observed double-stroke capital, signs, indices, [0,1[, tilde X, ringed T, inclusion hook and varphi. Both diagram signs have two waves over one rule; label positions are restored.','evidence':'All three coverage records agree. Main additionally inspected crops/scan175/C/l19_definition_tilde.png, crops/scan175/C/diagram_left_equivalence.png, crops/scan175/C/diagram_right_equivalence.png and crops/scan175/main/03_vertical_diagram.jpg. The math-triggered definition has a clear minus and separate small circle over T.'})
inv=copy.deepcopy(r['C']['inventory'])
inv=[x for x in inv if x['element']!='Emphasis rule']
order=['Author page number','Main prose block before diagram','Left isolated point','Cancelled phrase replaced above','Replacement phrase','Point above relation','Cancelled symbol','Cancelled expression','Subline isolated tick','Three-object diagram','Closing prose continuation','Archive sheet number']
inv.sort(key=lambda x:order.index(x['element']))
notes=r'''**S175-notes.** The page gives a topological picture behind equisingularity over the complex base field, under the simplifying phrase “en supposant pour fixer les idées”. It describes a tubular neighbourhood T retracting onto X_0, local triviality of the pair, a boundary fibration, and a fibrewise cone model. It explicitly writes the attaching face as x mapped to (x,1), then the punctured part as \(\mathring T=T-X_0\simeq\partial T\times[0,1[\), and claims an X_0-homotopy to the boundary. The smoothness assertion is conditional: “Si X_0 et X_1 sont non singuliers”. It further claims that the inclusion of the modified X_1 is a homotopy equivalence and reconstructs X from the displayed span “à homéomorphisme près”. No explicit authorial doubt or question mark occurs here; transcription doubts are editorial.

The narrow checks have explicit limits. Given the displayed quotient with its t=1 face attached to X_0, deletion of X_0 leaves the parameter interval [0,1[ (**S175-cone-endpoint**, readers B/C). On that product, H_s(b,t)=(b,(1-s)t) remains in the interval, fixes t=0 and preserves p(b), proving the stated homotopy over X_0 under the model (**S175-product-homotopy**, readers A/B/C). These checks do not prove that the required tubular neighbourhood exists.

There is also a literal boundary compatibility problem (**S175-boundary-inclusion**, readers A/B/C and main). In that same model, the outer boundary copy at t=0 belongs to T-X_0. The written definition \(\widetilde X_1=X_1-\mathring T\) removes it, whereas the following diagram labels the map from that boundary into \(\widetilde X_1\) as an inclusion. For a nonempty boundary copy, these literal identifications require an additional interior/collar convention that the page does not state. This is a local compatibility finding, not a refutation of the intended gluing construction. The definition crop clearly shows the minus and ringed T; neither was repaired. Likewise, “T sur X” is preserved: the second X is unindexed even though the displayed gluing projection targets X_0 (**S175-cone-base**, reader B).

Root resolves the first small arrow from its closed terminal loop, but retains the two weaker relation endings. The diagram keeps both comparisons as two waves over a line, the horizontal letter above its arrow and inclusion below, and p right / fibration left of the downward arrow. The letter remains J/j, with J preferred from its undotted broad loop. The complete raised phrase si ∂T est le replaces the old cancellation. Cancelled dev. is readable; the neighbouring cancelled symbols remain doubtful. The acute in réconstitue, spaced au dessus and final semicolon are retained. Three detached dark marks are drawn without assigning them mathematical or textual meanings.

Author page **30**, archive pencil **175**, has no title or date. It is a continuous letter passage interrupted by its diagram. The opening phraser joins the preceding para fragment; the final plus continues the sentence on the next page. Consolidated references count 24 prose baselines and identify diagram positions separately; readers A and B used different diagram-inclusive counts, mapped in the comparison table.
'''
notes=notes.replace('\\\\','\\')
repl=[(r'\mathrel{\unsure{\to|-}}\partial T\times I',r'\mathrel{\to}\partial T\times I'),(r'x\mapsto(x,1)',r'x\mathrel{\unsure{\mapsto|\vdash}}(x,1)'),('à partir du diagramme',r'à partir \unsure{du|des} diagramme')]
text=(ROOT/'records/scan175/C/reading.tex').read_text()
text=text.replace('$\\partial T$%\n% Compact isolated point','$\\partial T%\n% Compact isolated point').replace('$\\mathrel{\\unsure{\\to|-}}\\partial T\\times I','\\mathrel{\\unsure{\\to|-}}\\partial T\\times I')
text=text.replace('$\\widetilde X_1$%\n% Short isolated','$\\widetilde X_1%\n% Short isolated').replace('$\\hookrightarrow X_1','\\hookrightarrow X_1')
viewed=[x['path'] for x in r['C']['crops']]+['crops/scan175/main/'+x for x in ['01_au_dessus_L9.jpg','02_au_dessus_L10.jpg','03_vertical_diagram.jpg']]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
extra=[{'statement_id':'S175-boundary-inclusion','date':now,'who':'GPT-6 Astra Pro; inherited effort not separately exposed; /root','type':'targeted proof check','outcome':'Under the written cone model, a boundary point (b,0) belongs to T minus X_0 and hence is excluded from X_1 minus mathring T. For a nonempty such boundary copy, the later arrow cannot literally be its inclusion into that complement without an additional convention. Main derived this set-membership obstruction while reading and verified the minus/ringed-T ink in C/l19_definition_tilde.png. No global gluing claim was refuted and no text repaired.'}]
d=write_decision(175,'C',repl,diffs,comparisons,unresolved,inv,notes,r['A']['abbreviations'],review,viewed,brief='briefs/brief_v06_scan175.md',workflow_note='Three fresh readers viewed whole/a/b exactly once and completed all text, replacement, cancellations and diagram labels. A made 15 crops, B 13, C 19. Main reused all nineteen C crops and made three targeted crops; every main display succeeded once. The records normalize diagram-inclusive line numbering to 24 prose baselines plus named diagram places. Readers A/B attempted a prohibited TeX compile because the brief had omitted the inherited explicit prohibition; both attempts stopped for missing pdflatex.fmt before document processing. No PDF was inspected and no further compilation was run. Their reports preserve the deviation, and the next brief prohibits all TeX-engine attempts explicitly.',extra_events=extra,text_override=text)
ids={'175-M1':'S175-product-homotopy','175-M2':'S175-boundary-inclusion','175-B-M1-cone-endpoint':'S175-cone-endpoint','175-B-M2-product-homotopy':'S175-product-homotopy','175-B-M3-literal-boundary-inclusion':'S175-boundary-inclusion','175-B-M4-cone-base':'S175-cone-base','175.diagram-boundary-inclusion':'S175-boundary-inclusion'}
events=[]
for e in d['check_events']:
 if e['statement_id']=='175.local-punctured-cylinder':
  e1=copy.deepcopy(e);e1['statement_id']='S175-cone-endpoint';e1['outcome']='Endpoint subcheck of reader C’s combined recorded check: in Q=((partial T × [0,1]) disjoint union X_0)/((b,1)~p(b)), removing X_0 leaves partial T × [0,1[. This is conditional on the written quotient model.';events.append(e1)
  e2=copy.deepcopy(e);e2['statement_id']='S175-product-homotopy';e2['outcome']='Homotopy subcheck of reader C’s combined recorded check: H_s(b,t)=(b,(1-s)t) stays in [0,1[, fixes t=0 and preserves p(b), giving an X_0-deformation retraction under the stated product model.';events.append(e2)
 else:e['statement_id']=ids.get(e['statement_id'],e['statement_id']);events.append(e)
d['check_events']=events
(ROOT/'records/scan175/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Compressed local-triviality wording',r'\unsure{loclement|localement}; later loc without stop','175 L9–10: no separable a before tall l; following loc has an open final c and no detached point.'),
 ('Small boundary relations',r'\to; \unsure{\mapsto|\vdash}; \unsure{-|\to}','175 L14–15: first looped head resolved; the other two terminal thickenings remain ambiguous.'),
 ('Ringed tubular neighbourhood',r'\mathring T=T-X_0; \widetilde X_1=X_1-\mathring T','175 L15/L19: separate circle over T and ordinary minus. Preserve the observed notation despite the boundary-convention problem.'),
 ('Diagram comparison',r'\underline{\approx}','175 diagram, both parentheses: two wavy strokes above one straight rule; distinguish inline one-wave simeq.'),
 ('Boundary inclusion label',r'\unsure{J|j}','175 diagram: undotted high angled entry and broad lower return favour J, with cursive j retained. Recheck fresh occurrences independently.'),
 ('Three-stroke gluing diagram label positions','J/j above, inclusion below; p right, fibration left','175 diagram: labels stand on opposite sides, with no parentheses around inclusion.')
])
register_note_statements(175,[
 {'place':'L1–12; notes paragraph 1','statement':'The author proposes a complex-topological tubular neighbourhood and locally trivial pair/boundary fibration as the intuition behind equisingularity.'},
 {'place':'L13–16; notes paragraphs 1–2','statement':'The cone quotient model gives the punctured-cylinder formula and claimed homotopy over X_0.','status':'source assertion; conditional endpoint and product-homotopy checks indexed separately as S175-cone-endpoint and S175-product-homotopy'},
 {'place':'L16–18; notes paragraph 1','statement':'If X_0 and X_1 are nonsingular, the punctured neighbourhood and boundary are asserted to be topologically smooth fibrations over X_0.'},
 {'place':'L19–20; notes paragraphs 1 and 3','statement':'The manuscript asserts the inclusion of modified X_1 into X_1 is a homotopy equivalence.','status':'source assertion not proved; a separate boundary-compatibility issue is recorded as S175-boundary-inclusion'},
 {'place':'L21–24 and diagram; notes paragraphs 1 and 3','statement':'The manuscript reconstructs X, up to homeomorphism, as the amalgamated sum of the displayed span.','status':'source assertion not proved; literal boundary convention remains unresolved'}
])
