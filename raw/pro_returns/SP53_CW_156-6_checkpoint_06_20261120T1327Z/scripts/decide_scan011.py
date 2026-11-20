"""Main reader's ink-based scan011 decisions. Do not rerun after commitment."""
import copy,json
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan011.json'
if p.exists() and json.loads(p.read_text()).get('committed'):raise SystemExit('Already committed')
rs=[json.loads((O/f'readers/scan011/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
m1=[0,1,2,3,4,2,5,6,7,8,9,2,10,10,3,11,12,12,13,2,2,18,14,15,2,16,17,None,19,3,20,21,2,22,None,23,24,25,3]
m2=[0,1,2,3,4,2,5,6,7,8,9,2,10,11,3,12,13,14,15,2,2,16,17,18,2,19,20,None,21,3,22,23,2,24,None,25,26,27,3]
rows=[]
for i,x in enumerate(c):
 r=copy.deepcopy(x);r['final']=r.pop('reading');r['mathematical']=False
 r['readers']={'R1':a[m1[i]]['reading'] if m1[i] is not None else ('F' if i==34 else 'Editorial bridge excluded'), 'R2':b[m2[i]]['reading'] if m2[i] is not None else ('F' if i==34 else 'Editorial bridge excluded'), 'R3':x['reading']}
 rows.append(r)
def r3(s):return 'readers/scan011/R3/'+s+'.jpg'
def main(s):return 'crops/scan011/'+s+'.jpg'
def put(i,**kw):rows[i].update(kw)
put(0,crop=r3('01_ens_stop'),evidence='Main sees an open e and reduced n/s run, followed by a clear blank interval before de. All readers resolve ens; no abbreviation point is inked.')
put(1,final=r"\unsure{ds|d'} une",confidence='medium',crop=r3('02_ds_une'),evidence='The second sign after d is a substantial curved hook reaching toward the baseline, favoring reduced s. Its lower return is not clear enough to exclude an apostrophe. Main retains R1’s alternatives against R2/R3’s resolved ds, without using grammar.')
put(2,crop=r3('03_family_F_M'),evidence='Main sees the long sloping top, crossed middle arm and bent stem/foot of the family F. All readers retain calligraphic/fraktur alternatives; the printed alphabet remains underdetermined, with the first candidate used later.')
put(3,crop=r3('03_family_F_M'),evidence='The broad curved entry, two high peaks and rounded low trough identify M. Its ordinary versus calligraphic typeface is not settled by the handwriting. All readers’ first-occurrence alphabet doubt is retained.')
put(4,crop=r3('04_donnees'),evidence='Main sees the looped d, flattened medial groups, small separate accent and reduced es ending of données. H’s unreadable marker is replaced by this recoverable word.')
put(5,crop=main('01_later_F'),evidence='The family F has a long sloping upper arm with a hooked tip, a bent stem and a middle stroke crossing to the left. Main confirms the recurring form and applies the first candidate of the initial explicit alphabet doubt.')
put(6,crop=r3('05_plus_sophistiquees'),evidence='The p descender, l loop and low u/s survive the cancellation. Main resolves plus as all three readers do; H already preserves its struck state.')
put(7,final=r'\unsure{sophistiquées|sophistiqués}',against_C=False,confidence='medium',crop=r3('05_plus_sophistiquees'),evidence='A detached e-like turn after the accented group favors an additional e, but the compressed preceding course prevents secure letter counting. R1 reverses C’s priority, R2 resolves the masculine ending and R3 the feminine. Main retains C’s order and both alternatives; grammar does not decide.')
put(8,crop=r3('06_essentiels'),evidence='Main sees reduced initial ess/en, a tall t, i point and l/ending. These strokes support essentiels rather than H’s uncertain naturels.')
put(9,final=r'\unsure{entre|reste}',against_C=True,confidence='low',crop='readers/scan011/R2/03_entre_plus_ou_moins.jpg',evidence='The rounded open entry and flattened middle before t favor en-, as R2 reads. The compressed course does not safely exclude res-. Main reverses C/R1/R3’s priority but keeps both words.')
put(10,crop='readers/scan011/R2/03_entre_plus_ou_moins.jpg',evidence='Between plus and moins a tiny closed mark and short return are visible. Main confirms ou and resolves the whole group plus ou moins, in agreement with all readers.')
put(11,crop=main('02_after_dans_F'),evidence='Main sees the long top arm, curved upright and returned foot of the recurring family F. The explicit first alphabet alternatives govern its later first-candidate representation.')
put(12,crop=r3('08_le_transparent'),evidence='The l ends in a low e exit before the gap to plus. No s follows and there is no preceding et. Main confirms the singular le without grammatical repair.')
put(13,crop=r3('08_le_transparent'),evidence='The adjective ends at the raised terminal t with a white interval following it. No extra s is visible. Main retains literal transparent as all readers do.')
put(14,crop=main('03_pareil_M'),evidence='The M has a rounded rising entry, two tall strokes and a curved trough, matching the first occurrence. Main uses the first candidate of that alphabet doubt; the question mark and parenthesis remain.')
put(15,crop=main('04_Sur_underline'),evidence='One continuous underline begins under S and ends below the family F. H represents only Sur as underlined. Main confirms C’s full span; the family F is a heavier looped version of the recurring glyph.')
put(16,final=r"(\unsure{20-juin|20. juin})",against_C=True,confidence='low',crop='readers/scan011/R2/05_dated_note.jpg',evidence='A short horizontal rectangular mark separates 20 from juin. It favors a hyphen, as R2 proposes, but may be an elongated point. Main retains both alternatives against R1/R3’s resolved point and H’s omission.')
put(17,crop='readers/scan011/R2/05_dated_note.jpg',evidence='Main sees the p stems in par and point, reduced mon/nouveau and de/vue, then the lower implique plus ending in two left angles. The complete phrase resolves C’s doubt and contradicts H’s que pour. The pointer leads leftward to b); no terminal point is supplied.',mathematical='The dated note says the proposed structure b) no longer implies ll under the author’s new viewpoint. This is a literal attribution, not a proof of the objection.')
put(18,crop=r3('10_cancelled_sign'),evidence='Dense oblique hatching obscures an old stem and cross-arms. F is plausible but its exact alphabet is not recoverable. Main retains all readers’ canceled F/family-F alternatives; H is credited for explicitly recording the canceled sign.')
put(19,crop=main('05_map_brace'),evidence='Before the rightward arrow, the family F has a broad upper arm, short middle arm and returned lower stem. Main keeps the first alphabet candidate established at the marked first occurrence.')
put(20,crop=main('05_map_brace'),evidence='P has one plain upright and a single upper bowl. The argument inside its parentheses has the small looped top and crossed middle of the recurring family F. Main retains plain upright P and the first family-alphabet candidate.')
put(21,crop=main('05_map_brace'),evidence='The underbrace’s left end begins directly below et, well to the right of ll and the canceled sign. Its right end reaches beneath P(F). Main confirms C’s span; H credits the brace but extends it too far left.',mathematical='The incidence gloss is visually attached beneath et and the map, not beneath the preceding ll.')
put(22,crop='readers/scan011/R1/09_notation_deployement.jpg',evidence='Main sees no/t followed by the marked e ending, without an i/o/n continuation. The word is notée. The adjacent map bar and tilde are also clear.')
put(23,crop='readers/scan011/R1/09_notation_deployement.jpg',evidence='After o a long descending y stroke precedes ement. Main resolves literal déployement, without modernizing to déploiement.')
put(24,crop='readers/scan011/R1/09_notation_deployement.jpg',evidence='The same existing crop covers the terminal family F in the closing parenthesis. Its heavier retracing does not supply an additional ordinary doubled operand; main preserves the recurring first alphabet candidate.')
put(25,c=r'\deleted{i.e. la \unsure{description|désignation} ...}',final=r'\deleted{i.e. la \deleted{\unsure{description|désignation}} ...}',against_C=True,crop=r3('13_cancelled_gloss'),evidence='A local stroke cancels the lower noun separately from the stroke crossing the whole gloss and its raised replacement. C’s encompassing cancellation omits that nested local state; H already represents it. The masked noun remains description/désignation, with a late descender favoring description. All readers preserve the nested cancellation.')
put(26,crop=r3('13_cancelled_gloss'),evidence='The raised relation is followed by d, apostrophe and compressed i/n/c, without type or written idence. The isolated raised final trace may be a point or part of the crossing. Main retains R2/R3’s stop/no-stop alternatives against R1’s resolved point, and the raised insertion remains within the later whole-gloss cancellation. H’s supplied expansion is credited as editorial, but is not added to the manuscript letters.')
put(27,against_H=False,crop=r3('13_cancelled_gloss'),evidence='H’s semicolon and sous c) bridge introduce its description of layout. Main sees no such continuation of the canceled gloss. R1/R2 exclude it as editorial; R3 identifies the same fact but lists a witness difference. Main excludes this representation-only bridge from difference counts and from manuscript text.')
put(28,crop=main('06_gloss_quotes_M'),evidence='Two raised short strokes precede F and two follow G; the opening pair joins near its base. There are no lateral chevrons. Main keeps literal paired quotation strokes, represented by two backticks and apostrophes.')
put(29,crop=main('06_gloss_quotes_M'),evidence='The small M after the membership sign has the rounded entry and two tall peaks of the recurring form. The first candidate of the initial alphabet doubt is used. The conjunction et is separately underlined.')
put(30,crop=r3('14_Je_ces_points'),evidence='J’s stem and foot and the adjacent e remain visible beneath the cancellation. Main resolves canceled Je; both witnesses already preserve its physical state.')
put(31,crop=r3('14_Je_ces_points'),evidence='Small terminal courses favor plural ces points, but separate final s strokes cannot be securely counted. Main retains R1/R3’s plural/singular alternatives against R2’s resolved plural; reference and grammar do not decide.')
put(32,crop=main('07_lower_F'),evidence='The family F has a long leftward entry into its looped upper arm, a crossing middle arm and a bent lower stem. Main confirms the recurring form and uses the first candidate of the initial alphabet doubt.')
put(33,confidence='high',crop=r3('15_en_ecrivant'),evidence='Main sees open e/n, a separate acute, é/c, the reduced r/i/v/a/n course and a tall final t. These resolve en écrivant against C’s first candidate on écrira and H’s uncertain incluant.')
put(34,crop=r3('17_variable_F'),evidence='Two upper vertical strokes merge below the middle arm into one lower stem. Main retains R3’s ordinary-F/doubled-F alternatives, with ordinary retraced F first, against C/H/R1/R2’s resolved ordinary operand. No deletion is inferred.')
put(35,crop=r3('16_definition_arrow'),evidence='A d loop is followed by a descending f and compact n. Main resolves dfn, without supplying an accented e or expanding the abbreviation.')
put(36,crop=r3('16_definition_arrow'),evidence='Below the left arrowhead there is a p-like elongated loop and small partly merged strokes. Main retains all readers’ tentative par instead of omitting the real inscription as H does; overlap alone does not establish cancellation.')
put(37,crop=main('08_definition_quotes'),evidence='Main sees paired raised strokes before F and after G. They are not lateral guillemets. The grave mark over à is separately visible.')
put(38,crop=main('09_final_M'),evidence='The final M has a long rising entry, two tall peaks and a rounded trough. Main keeps the first candidate of the initial alphabet doubt. There is no extra index, bar or condition at the photographed edge.')
# Normalize recurring glyph reports to the actual corresponding occurrence.
for i in [5,11,19,24,32]:rows[i]['readers']={k:r'\mathcal{F}' for k in ['R1','R2','R3']}
rows[20]['readers']={k:r'\mathrm{P}(\mathcal{F})' for k in ['R1','R2','R3']}
for i in [14,29,38]:rows[i]['readers']={k:rows[i]['final'] for k in ['R1','R2','R3']}
rows[12]['readers']={k:'le' for k in ['R1','R2','R3']}
rows[13]['readers']={k:'transparent' for k in ['R1','R2','R3']}
rows[16]['readers']['R1']='(20. juin)'
rows[17]['readers']['R1']=rows[17]['final']
ordered=[r for i,r in enumerate(rows) if i!=27]
for i,r in enumerate(ordered,1):r['id']=f'011-{i:02}'
tex=(O/'readers/scan011/R3/reading.tex').read_text()
tex=tex.replace('de base ds une',r"de base \unsure{ds|d'} une")
tex=tex.replace(' sophistiquées sur',r' \unsure{sophistiquées|sophistiqués} sur')
tex=tex.replace(r'\unsure{reste|entre}',r'\unsure{entre|reste}')
tex=tex.replace('(20. juin)',r'(\unsure{20-juin|20. juin})')
(O/'decisions/scan011_final.tex').write_text(tex)
cd=copy.deepcopy(rs[2]['c_doubts'])
links=[0,1,2,6,7,9,10,12,13,18,23,25,26,17,30,33,36,35]
for j,i in enumerate(links):
 r=rows[i];cd[j].update(reading=r['final'],evidence=r['evidence'],crop=r['crop'],disposition='retained' if j in [1,2,4,5,9,11,12,16] else 'resolved')
inv=copy.deepcopy(rs[2]['inventory'])
inv[3]['first_words_or_objects']="On peut prendre pour ens de base ds/d' une axiomatique des ateliers"
inv[9]['first_words_or_objects']="(20-juin / 20. juin) Non, par mon nouveau point de vue ça n'implique plus ≪"
inv[18]['first_words_or_objects']="relation d'inc. / d'inc (inserted, then canceled with whole gloss)"
notes={'content':'The continued sentence is followed by Axiomes, discussing possible underlying sets for an axiomatization of ateliers: the family F, M or L. It contrasts simplicity of the data with transparency of the essential axioms and asks whether the case of M may be similar. Display (1.16) gives three proposed structures on F. A dated objection points to choice b). Choice c) includes a map to P(F), a deployment notation, and an incidence gloss attached below et and the map. A canceled right-hand gloss retains a locally canceled noun and raised replacement. The closing paragraph announces a diagram of six fundamental relations, then defines incidence in (1.17); the diagram itself is not drawn on this page.',
'math_reading_decisions':['The dated note literally denies that b) still implies ll under the author’s new viewpoint. The objection is transcribed, not mathematically proved.','The underbrace begins below et and spans the map. Its placement does not include the earlier ll. The map arrow is rightward; the element notation has a mapsto bar and tilde.','Plain upright P is locally clear. The family F and cursive M keep explicit first-occurrence alphabet doubts. The first F operand in (1.17) has a retraced/doubled upper stem, retained as ordinary F versus blackboard F.','The closed left-pointing incidence triangle and defining equivalence are preserved. Clear dfn remains above, and uncertain par below. The two written incidence conjunctions agree in their content, but this text comparison is not a proof check.','Literal singular le plus transparent is preserved. The word endings and date separator remain uncertain where the ink does not decide them.'],
'author_doubts':['“(ou peut-être pareil pour M ?)” asks whether the same comparison holds for M.','The dated note reads “Non, par mon nouveau point de vue ça n\'implique plus ≪”; its date separator remains hyphen/point.','No additional à vérifier or sauf erreur request is present on this page.'],
'titles_dates_counts':'Manuscript page 10; underlined Axiomes and Sur F. Date 20-juin / 20. juin, with no written year. Two display labels, (1.16) and (1.17); choices a), b), c); six fundamental relations are announced. No separate diagram, drawing, archive pencil number, footer or typed text is reported by the readers.'}
events=[]
for i,r in enumerate(rs,1):
 for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan011 R{i}'))
for e in rs[2]['check_events']:events.append(dict(e,who='GPT-6 Astra Pro; effort not exposed; main reader; scan011'))
un=[{'place':rows[i]['place'],'reading':rows[i]['final'],'alternatives':'Remaining letter, sign, alphabet or punctuation alternatives are explicit in the transcription.','confidence':rows[i]['confidence'],'evidence':rows[i]['evidence']} for i in [1,2,3,7,9,16,18,25,26,31,34,36]]
d={'scan':11,'mspage':'10','folder':'J156-6-02','filename':'J156-6-02_156-6_scan011.tex','brief':'v005','committed':False,'adjudicated_all':True,'differences':ordered,'adjudications':[rows[27]],'c_doubts':cd,'s_rows':[],'inventory':inv,'notes':notes,'check_events':events,'unresolved':un,'abbreviations':rs[2]['abbreviations']}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
vp=O/'decisions/scan011_main_views.json';seen=json.loads(vp.read_text())
for x in sorted((O/'crops/scan011').glob('*.jpg')):
 if str(x) not in seen:seen.append(str(x))
assert len(seen)==25,len(seen)
vp.write_text(json.dumps(seen,indent=2)+'\n')
print('Prepared scan011: 38 difference loci, one editorial adjudication, 18 C doubts (10 resolved / 8 retained), 12 final doubts, 22 inventory items, 25 successful main crop views.')
