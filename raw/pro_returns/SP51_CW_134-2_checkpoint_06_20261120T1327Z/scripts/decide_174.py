from decision_helpers import *
import copy
r=load_reports(174)
diffs=[row(r,'C',i) for i in range(19)]
diffs[6].update(final='i',differs_C=True,differs_H=False,C_doubt_status='resolved to i',evidence='The high stroke is an elongated dot aligned above and slightly right of the i stem, without a separate dot plus prime. Its shape resembles the long i-dot visible in the L7 abbreviation crop. Root selects A’s plain i over B/C’s retained prime alternative from this geometry, not from the expected functor.',confidence='medium')
for i,p in [(14,'01_cela_accent.jpg'),(15,'02_schematique_underline.jpg'),(16,'03_voisinage_quotes.jpg')]:diffs[i]['crop']='crops/scan174/main/'+p
diffs[14]['evidence']='The crop shows a detached dark stroke descending rightward above the final vowel: a grave accent. Preserve celà rather than modernizing it.'
diffs[15]['evidence']='A nearly horizontal dark rule runs directly beneath schématique. The lower curved attachment stroke rises separately to the destination after contexte; the underline is not that leader.'
diffs[16]['evidence']='Both ends of voisinage tubulaire étale have two short raised pen strokes, rather than angular guillemets.'
diffs[17]['evidence']+=' Main inspected both crops/scan174/C/l22_topos_adjective_start.png and crops/scan174/C/l23_topos_adjective_end.png.'
comparisons=[
 {'place':'L7 point after il','A':'il. f et s.','B':'il f et s.','C':'il. f et s.','decision':'Select A/C: the compact separate black point after the l is independent of the i-dot and the f (C/l07_necessity_abbreviation.png). Its presence does not establish an intended grammatical function.'},
 {'place':'L12 second i','A':'i','B':r'\unsure{i|i\prime}','C':r'\unsure{i|i\prime}','decision':'Select A. The raised long mark aligns with the i stem and has no separate accompanying dot. Compare the similarly elongated i-dot at L7. The functor expected from the mathematics did not determine the decision (C/l12_composite_and_phi.png; C/l07_necessity_abbreviation.png). The lower star/comma remains doubtful.'},
 {'place':'L7 diagram placement and size','A':'left marginal diagram, own spacing','B':'left marginal diagram, own spacing','C':'left marginal diagram, narrower column spacing','decision':'The same objects, labels and hooked arrows are present in all three readings. Keep a fit-to-margin diagram with explicit left-margin placement. Neither the different TeX spacing nor H’s editorial location note is an ink doubt (C/l07_margin_inclusions.png).'},
 {'place':'L24 page-final word break','A':'para% with continuation-hyphen comment','B':'para-%','C':'para% with continuation-hyphen comment','decision':'All readers saw the same physical para- at the page foot. Preserve the visible break in a comment and suppress the line-continuation hyphen in the joined transcription. This typesetting-only difference is excluded from witness counts.'},
 {'place':'L15 possible final cancelled letter','A':r'\unsure{d}','B':r'\unsure{d}','C':r'\unsure{d}','decision':'Keep the explicitly doubtful d, but record that the low loop may instead belong to the descender of live types. No independent letter can be resolved from the crossed area (C/l15_interlinear_correction.png).'}
]
unresolved=[copy.deepcopy(x) for x in r['C']['unresolved'] if x['place']!='L12, second i']
for x in unresolved:
 if x['place']=='L15, possible cancelled d':x['alternatives']=['no independent letter: part of the live types descender']
review=[]
items=[('L7 alphabet',r'\mathcal P|P','retained','l07_partition_capital.png'),('L12 shorthand',r'\overline m|=','resolved: barred m','l12_meme_shorthand.png'),('L12 second i','i|i′','resolved: i','l12_composite_and_phi.png'),('L12 low attachment','*|,','retained','l12_composite_and_phi.png'),('L13 verb','intéressent','retained','l13_interessent_cancelled_end.png'),('L13 cancelled suffix','s|t','retained','l13_interessent_cancelled_end.png'),('L14 cancelled word','fonction','retained','l14_cancelled_fonction.png'),('L15 cancelled phrase','i.e. de la|i.e. de leurs','retained','l15_interlinear_correction.png'),('L15 possible letter','d','retained; alternatively part of live types descender','l15_interlinear_correction.png'),('L22–23 adjective','intéressant|satisfaisant','resolved: intéressant','l23_topos_adjective_end.png'),('L24 verb','fait|fais','resolved: fait','l24_fait_fais.png'),('L11 plural','équisingularités|équisingularité','resolved: plural s','l11_equisingularites.png')]
for place,earlier,decision,p in items:review.append({'place':place,'earlier':earlier,'decision':decision,'evidence':'Main inspected crops/scan174/C/'+p+'; stroke evidence is in the changes table.'})
review.append({'place':'L16 accent','earlier':'celà|cela','decision':'resolved: celà','evidence':'Main inspected crops/scan174/main/01_cela_accent.jpg; distinct descending-right grave stroke.'})
review.append({'place':'L2, L4–6, L7, L12/L18, L14–19, L21–23 earlier structural questions','earlier':'Minus versus set difference; parentheses and star heights; marginal arrow labels; phi form; correction levels; ambient X versus X_1','decision':'All three independent readers retain the minus-like dash, parenthesized restriction additions, first composite with low pushforward star, single i_0 arrow label, consistent varphi, observed corrections, and ambient X.','evidence':'All three whole/half readings and coverage records agree. The main reader also inspected the marginal diagram, composite and interlinear corrections in the crops listed above. No unsupported correction from mathematical expectation was made.'})
notes='''**S174-notes.** For two strata, closed X_0 and complement X_1, the page states Artin dévissage as sheaves F_0 and F_1 together with a map F_0 to i_0^*i_{1*}(F_1). It states constructibility in terms of locally constant restrictions, with “plus des conditions de finitude accessoires…”. Under the equisingularity hypotheses, it claims corresponding local constancy for the repeated composite named φ. It then expresses the category through locally constant sheaves on the strata, or their homotopy types, with the explicit reservation “à celà près qu'il faut encore expliciter la nature du foncteur exact à g. φ”.

The proposed construction is qualified by “Je pense que ceci est possible” and “techniquement assez sophistiqué”. In the underlined schematic setting it would use a “voisinage tubulaire étale” of X_0 in X, described as a topos not associated with a scheme. These source claims were recorded, not proved. All three readers performed only the narrow source/target check indexed **S174-local-source-target**: the preferred i_{1*} maps sheaves on X_1 to X, after which i_0^* gives a sheaf on X_0, matching F_0. This is not a proof of dévissage, the local-constancy assertions, or the proposed construction.

That mathematical context prompted close attention to the stars and the second i. Root resolves the second i from its elongated dot’s alignment, agreeing with A against B/C’s retained prime alternative; the small lower attachment remains star/comma. The open two-lobed φ is kept consistently. The right inclusion is unlabelled in the manuscript, and no i_1 label is supplied. The independent literal point in “il. f et s.” is retained. The crossed suffix, fonction, the old underlined phrase and its possible final d remain uncertain; that possible d may instead be part of the live types descender. The replacement and nested seuls are placed by their guides. The accented celà and underline beneath schématique are preserved.

This is author page **29**, archive pencil **174**, without title or date, a continuous letter paragraph. The marginal diagram accounts for the local indentation. The page ends with a physical continuation hyphen after para; a comment records it while the text remains ready to join the next page’s continuation. The adjective intéressant is read from both physical fragments, and fait from its short crossed terminal upright, without grammatical repair.
'''
viewed=list(dict.fromkeys(x['crop'] for x in diffs))
viewed.insert(viewed.index('crops/scan174/C/l23_topos_adjective_end.png'),'crops/scan174/C/l22_topos_adjective_start.png')
repl=[(r"\unsure{i|i'}",'i')]
repl += [(r'\margin{\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=0.6em]',r'\margin{\diagram{\resizebox{\linewidth}{!}{\begin{tikzcd}[ampersand replacement=\&,column sep=1.2em]'),(r'\end{tikzcd}}}%',r'\end{tikzcd}}}}%')]
text=(ROOT/'records/scan174/C/reading.tex').read_text()
text=text.replace('% A continuation hyphen','% The possible cancelled d at L15 may instead be the descender of live types.\n% A continuation hyphen')
abbr=[{'written':x['written_form'],'expansion':x['possible_expansion']} for x in r['C']['abbreviations']]
d=write_decision(174,'C',repl,diffs,comparisons,unresolved,r['C']['inventory'],notes,abbr,review,viewed,brief='briefs/brief_v05_scan174.md',workflow_note='Three fresh readers each inspected whole/a/b once, with 24 main baselines and eight addition/diagram coverage entries. Main compared all returns, reused twelve reader crops and made three new crops. The attempted batch display of the three new crops was truncated before inspection; the same saved files were then displayed successfully without recropping. Reader B removed an erroneous claimed archive-comment omission after a text-only correction; no image was reopened. The page-final hyphen and diagram spacing were normalized as typesetting, not counted as ink changes.',text_override=text)
for e in d['check_events']:
 if e['statement_id']!='S174-notes':e['statement_id']='S174-local-source-target'
(ROOT/'records/scan174/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Two-stratum inclusion diagram',r'X_0 \hookrightarrow X \hookleftarrow X_1; i_0 on left arrow only','174 L7 margin: both heads point to X, both outer tails hooked; no enclosing parentheses.'),
 ('Necessity and sufficiency', 'il. f et s.','174 L7: literal separate point after il; only s has an abbreviation stop.'),
 ('Barred même',r'\overline m','174 L12: lower entry turn and rounded rise distinguish this occurrence from plain equals; 170 remains doubtful.'),
 ('Repeated composite',r'i_0^*i_{1\unsure{*|,}}(F_1)=\varphi(F_1)','174 L12: elongated dot over second i; lower attachment unresolved. Same open two-lobed varphi at L18.'),
 ('Nonstandard accent','celà','174 L16: detached grave accent over final vowel, retained.')
])
register_note_statements(174,[
 {'place':'L1–6; notes paragraph 1','statement':'Two-strata Artin dévissage describes F by its restrictions and a gluing map to i_0^*i_{1*}(F_1).'},
 {'place':'L7–10; notes paragraph 1','statement':'Constructibility is characterized by locally constant restrictions, subject to accessory finiteness conditions.'},
 {'place':'L11–12; notes paragraph 1','statement':'Equisingularity hypotheses imply the required local constancy of the composite φ(F_1).'},
 {'place':'L13–18; notes paragraph 1','statement':'The category is expressed through the strata’s homotopy types, but the left exact functor φ remains to be specified.'},
 {'place':'L18–24; notes paragraph 2','statement':'The author proposes a schematic étale tubular neighbourhood topos of X_0 in X, not associated with a scheme; feasibility is explicitly conjectural here.'}
])
