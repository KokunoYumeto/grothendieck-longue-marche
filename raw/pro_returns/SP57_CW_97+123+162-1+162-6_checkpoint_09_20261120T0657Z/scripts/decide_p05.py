from pathlib import Path
import json,copy
O=Path('out'); stem='C123-01_123_scan017'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ['R1','R2','R3']}
r1=f'readers/{stem}/R1/';r2=f'readers/{stem}/R2/';r3=f'readers/{stem}/R3/';rc=f'decisions/rootcrops/{stem}/'
spec=dict(stem=stem,base_reader='R3',brief='reader_v05.md',main_new_crops=4,text_edits=[],difference_overrides={},additional_differences=[])
def edit(old,new):spec['text_edits'].append(dict(old=old,new=new))
# Preserve the slanted note's six source lines, with the written fraction rather than an expansion.
t1=(O/'readers'/stem/'R1'/'reading.tex').read_text();t3=(O/'readers'/stem/'R3'/'reading.tex').read_text()
m1=t1[t1.index('\\margin{'):t1.index('\nEnfin,')]
m1=m1.replace('split semi-direct','split fraction-direct').replace(r'\unsure{semi-|se-}',r'$\unsure{{}^{1}\!/\!_{2}}$-')
m3=t3[t3.index('\\margin{'):t3.index('\n$e\\handwritten')]
edit(m3,m1)
edit(r'\unsure{\mathfrak{g}(2)^*}',r'\unsure{\mathfrak{g}(2)^*|\ne0}')
# The underlying hyphen and bowed crossing mark are visible; their interpretation remains uncertain.
edit(r'(newcelui) at (.05,.60) {\inserted{%',r'(newcelui) at (.05,.60) {\inserted{\unsure{%')
edit(r'\end{tikzpicture}}};',r'\end{tikzpicture}}}};')
# Reproduce the visible upright l and superposed diagonal, without assigning correction order.
group=r'''\unsure{\begin{tikzpicture}[baseline=(sl.base)]
\node[inner sep=0pt] (sl) {$\operatorname{Sl}$};
\draw[line width=.55pt] ([xshift=-5pt,yshift=-6pt]sl.east) -- ([xshift=1pt,yshift=7pt]sl.east);
\end{tikzpicture}}'''
edit(r'\unsure{\operatorname{Sl}|\operatorname{SZ}}',group)
# Overrides are the main reader's crop decisions, not programmatic votes.
def ov(i,**kw):spec['difference_overrides'][f'R3-{i:02}']=kw
ov(1,readers=r'R1: \unsure{U\cap}; R2: \unsure{U\cap}; R3: U\unsure{\cap}. Root: definite U, doubtful intersection.',evidence='The two tall uprights and low returning bowl identify U. The adjoining smaller arch is heavily crossed, so only the intersection remains doubtful.',crop=r3+'01_top_group.png')
ov(2,readers=r'R1: en; R2: en; R3: \unsure{en}. Root retains the local doubt.',evidence='The heavy horizontal cancellation covers almost all of the two short opening letters; their lower blobs do not independently settle en.',crop=r3+'02_cancelled_note_connector.png',confidence='low')
ov(3,readers=r'R1: cU | subset U | compressed celui; R2: subset | c before U; R3: c | subset before U. Root: \unsure{c|\subset}U.',evidence='An open c-shaped curve stands before a separate tall U; its bottom coincides with the cancellation. The full letter sequence celui is not visible.',crop=r3+'02_cancelled_note_connector.png',confidence='low')
ov(4,readers='R1: drawing with note over qui est un groupe unipotent; R2: separate TikZ enclosure/leader; R3: inline drawing above unipotent and Enfin. Root uses R3’s relative placement and leaves the precise endpoint open.',crop=r3+'02_cancelled_note_connector.png')
ov(5,final=r'\unsure{cf.|cf} plus bas',c_changed=True,h_changed=True,readers=r'R1: \unsure{cf.|cf}; R2: \unsure{cf.|cf}; R3: cf. Root retains the punctuation doubt.',evidence='The small low terminal beside f may be a point or part of the letter; a separate punctuation dot is not secure.',crop=r3+'03_left_margin.png',confidence='medium')
ov(6,readers=r'R1: \simeq; R2: \simeq; R3: \simeq. Root confirms a wave above a separate straight lower stroke.',crop=r3+'03_left_margin.png')
ov(7,readers='All three retain o/0 at the first occurrence and use o at the later occurrence. Root retains this convention.',crop=r3+'03_left_margin.png')
ov(8,crop=r3+'03_left_margin.png',marked_in_H='yes')
ov(9,final=r'(produit $\unsure{{}^{1}\!/\!_{2}}$- / direct)',readers=r'R1: \unsure{semi-|se-}; R2 final: raised 1 / lower 2, definite; R3 final: doubtful 1/2. Root: doubtful slanted numeral fraction, then hyphen and next-line direct.',evidence='A short raised 1, long diagonal, lower curled 2-like component and separate hyphen follow produit. The following source line begins direct). No s-e-m-i sequence is written; the six-line slanted layout is retained in TikZ.',crop=r3+'03_left_margin.png',confidence='medium',kind='abbreviation expanded or spelling modernised')
ov(10,crop=r1+'04_centralizer_and_replacement.png')
ov(11,crop=r2+'06_cancelled_dans.jpg')
ov(12,readers=r'R1: unsure inner parentheses around final g; R2: no inner parentheses; R3: no inner parentheses. Root follows C: outer parentheses enclose the whole cancelled clause.',evidence='The narrow arch before the final g’s long descender is continuous with that glyph, not a separate opening parenthesis. The sole closing parenthesis closes the clause beginning (et on a.',crop=r3+'05_deleted_fil.png')
ov(13,crop=r2+'08_satisfasse_and_open.jpg')
ov(14,final=r'\inserted{\handwritten{\deleted{$\unsure{\mathfrak{g}(2)^*|\ne0}$}}}',c_changed=True,h_changed=True,readers=r'R1: doubtful g(2)*, certainly cancelled; R2: g(2)* | nonzero, certainly cancelled; R3: doubtful g(2)*, certainly cancelled. Root retains both graphic candidates under the certain cancellation.',evidence='Heavy slashes cover the raised group after dense. A rounded component and descending/slanting traces survive; they do not securely exclude the shorter alternative. The separate clear g(2)* is after l’ouvert.',crop=r1+'06_dense_insertion.png',confidence='low')
ov(15,crop=r2+'08_satisfasse_and_open.jpg')
ov(16,crop=rc+'elements_insertion.png',evidence='A small live handwritten e and its insertion stroke stand above/right of éléments. The heavily cancelled group is lower, over dense/de. No separate cancelled nonzero expression is visible at H’s stated location.',marked_in_H='no')
ov(17,crop=r3+'07_celui_ci.png')
ov(18,final='Inserted Celui-ci with an uncertain bowed stroke over the typed hyphen, plus the lower hooked connector, drawn in TikZ.',readers='R1: uncertain hyphen/left-parenthesis overlay, no lower connector in reading.tex; R2: Celui+ci | Celui-ci; R3: typed hyphen, bowed crossing stroke and lower connector. Root preserves the two strokes graphically with an in-place doubt on their interpretation.',evidence='The short horizontal hyphen is crossed by a full-height bowed stroke, rather than a straight plus stem. A separate lower curve runs beneath the raised replacement and descends after the deleted qui.',crop=r3+'07_celui_ci.png',kind='drawing or diagram',confidence='medium')
ov(19,crop=rc+'torseur_underline.png')
ov(20,crop=r1+'08_bour.png')
ov(21,readers='R1: doubtful cancelled comma; R2: definite cancelled comma; R3: definite cancelled comma. Root resolves the comma.',evidence='The low curved comma tail extends below the last x overstrike after (i); it is distinct from that x’s horizontal foot.',crop=r2+'12_clause_end.jpg',confidence='high')
ov(22,final=r'\deleted{0}1',readers=r'R1: definite handwritten 1 over 0; R2: \unsure{1|0} over 0; R3: definite serifed typewritten 1 over 0. Root: definite 1, with old 0 retained; typewriter form.',evidence='The round 0 surrounds a separate vertical 1 with top serif and broad foot. The digit’s regular serifed impression is typed; the adjacent inequality is handwritten.',crop=r3+'09_lie_u_bound.png',confidence='high',H=R['R3']['differences'][21]['H']+'; H note: corrigé à la main en « k≥1 »')
ov(23,crop=r1+'11_deleted_en.png')
ov(24,readers=r'R1: \unsure{u|a}; R2: live u after doubtful deleted a; R3: \unsure{u|a}. Root retains u/a without assigning a temporal order.',evidence='Two upright stems and a low bowl coexist with an enclosed upper chamber. Their overprinted contours do not securely identify a predecessor and successor.',crop=r1+'12_si_u.png')
ov(25,final='TikZ: upright Sl with a superposed rising diagonal over l; local doubt retained.',readers=r'R1: SZ | Sl; R2: Sl | SZ; R3: Sl | SZ. Root preserves the serifed l and crossing oblique stroke graphically; its purpose remains uncertain.',evidence='The l has a top serif, upright and low foot; a separate oblique stroke projects beyond it. A plain Sl would omit ink, while an unqualified SZ would collapse the visible overlay.',crop=r1+'13_group_name.png',kind='drawing or diagram')
ov(26,readers=r'R1: \unsure{aassi|aussi}; R2: a plus doubtful deleted a before ussi; R3: a\unsure{a|u}ssi. Root uses the local a/u doubt without inventing chronology.',evidence='Only the second letter has overlapping u-shaped uprights/bowl and an upper closed chamber. The first a and the following ssi are clear.',crop=r1+'14_aassi.png')
ov(27,crop=r3+'14_ie_semicolon.png')
ov(28,crop=rc+'H_product_point.png')
ov(29,crop=r1+'15_de_plus.png',readers=r'All three: \deleted{\unsure{A}}De. Root confirms the definite outer D and retains the covered predecessor as doubtful.')
ov(30,crop=r2+'20_une_deleted.jpg')
ov(31,crop=r3+'03_left_margin.png')
# H normalizes the second marginal subscript independently of the first one.
d=copy.deepcopy(next(d for d in R['R2']['differences'] if d['id']=='D07'))
d.update(id='ROOT-01',final=d.pop('reading'),crop=r3+'03_left_margin.png',readers='R1: Z_o; R2: Z_o; R3: Z_o, following the first-occurrence o/0 doubt.',marked_in_H='no')
spec['additional_differences'].append(d)
# Every C doubt has been reconsidered, including the literally retained affine expression.
cd=copy.deepcopy(R['R3']['c_doubts'])
for d in cd:
 p=d['place']
 if p=='Live affine expression':d['crop']=rc+'affine_expression.png';d['evidence']='The live a, plus, long-descending g, raised e, and the following convenable). are visible without cancellation.'
 if p=='Deleted insertion after dense':d.update(decision=r'Retain \unsure{\mathfrak g(2)^*|\ne0} under certain cancellation.',crop=r1+'06_dense_insertion.png')
 if p=='Sl/SZ(2,k)':d.update(decision='Preserve Sl and the diagonal overlay in TikZ with doubt; no chronological state inferred.',crop=r1+'13_group_name.png')
 if p=='Inserted Celui-ci':d['decision']='Preserve the typed hyphen, bowed crossing stroke, and lower connector in TikZ; mark interpretation doubtful.'
spec['c_doubts']=cd
rem=copy.deepcopy(R['R3']['remaining_doubts'])
# Normalize source reader fields if necessary; root adds/edits substantive residual doubts below.
for d in rem:
 if 'Group name' in d.get('place',''):
  d.update(reading='Sl with a superposed diagonal, drawn in TikZ',alternatives='purpose of diagonal; Z-like composite',confidence='medium')
 if 'dense' in d.get('place',''):
  d.update(reading='g(2)*',alternatives='nonzero token; covered internal strokes',confidence='low')
 if 'fraction' in d.get('place','').lower() or 'produit' in d.get('place',''):
  d.update(reading='raised 1 / lower 2',alternatives='compact fraction contours partly ambiguous',confidence='medium')
rem.extend([
 dict(place='Celui-ci graphic overlay',reading='typed hyphen with bowed crossing stroke',alternatives='interpretation and order of the superposed marks unresolved',confidence='medium'),
 dict(place='Slanted note: cf punctuation',reading='cf.',alternatives='cf with a low pen terminal only',confidence='medium'),
 dict(place='Top connected note leader',reading='lower curve returns and descends after unipotent',alternatives='exact attachment to punctuation or neighboring stroke unresolved',confidence='medium')])
spec['remaining_doubts']=rem
inv=copy.deepcopy(R['R3']['inventory'])
for d in inv:
 if isinstance(d['position'],list):d['position']='whole-image box '+str(d['position'])
 d['hand']=d['hand'].replace('handwritten','unnamed hand').replace('typewritten','typewriter')
 if d['element']=='Slanted marginal note':d['first_words_or_objects']='cf[.] plus bas ... Z simeq Z_o.Z+ ... (produit 1/2- / direct)'
 if d['element']=='Cancelled addition after dense':d['first_words_or_objects']='g(2)* / nonzero, tentative; certainly cancelled'
inv.extend([
 dict(sheet_kind='typescript',hand='typewriter and unnamed hand',element='Superposed diagonal in group name',kind='drawing',position='(iv), f: Sl/SZ(2,k)',first_words_or_objects='Sl with projecting diagonal over l',transcribed='yes'),
 dict(sheet_kind='typescript',hand='typewriter overprints',element='Overprinted u/a contours',kind='text',position='Si u/a and donc aassi/aussi',first_words_or_objects='u/a; a[a/u]ssi',transcribed='yes'),
 dict(sheet_kind='typescript',hand='typewriter with unnamed hand fills',element='Literal affine expression retained',kind='text',position='after revised additive acting algebra',first_words_or_objects='a+g^e, pour un a in g convenable).',transcribed='yes')])
inv.extend([dict(sheet_kind='typescript',hand='typewriter with unnamed hand additions',element='First orbit isomorphism prose',kind='text',position='between the two orbit-map displays',first_words_or_objects='est un[e] isomorphisme de U avec x+Fil¹g ... et l’application',transcribed='yes'),dict(sheet_kind='typescript',hand='typewriter',element='Replacement digit in Lie U bound',kind='insertion',position='over old zero under sum in Lie U',first_words_or_objects='1',transcribed='yes')])
for d in inv:
 if d['element']=='Agreement ending removed':d['hand']='typewriter letters and x overstrikes'
spec['inventory']=inv
spec['notes']='''Continuation of a corrected typescript on Dynkin data, with handwritten formulas and a slanted marginal note. The first paragraph replaces the acting group by Z+=Z∩U and the additive acting algebra by Lie(Z+)=g^e∩Fil¹(g). The margin gives Z≃Z_o.Z+ and Z_o=Z∩L=Cent(f); its written fraction followed by -direct is preserved, with the possible expansion “semi-direct” confined to the abbreviation list. Item (iii) states an open dense homogeneous space in g(2), with torseur cancelled in favor of espace homogène. Item (iv) defines P, U and L by their weight subspaces, asserts that P and associated data depend only on u, and states orbit-map isomorphism/surjectivity claims.

**Ink decisions prompted by mathematics.** The live phrase “est de la forme a+g^e” remains exactly as written, despite the corrected acting algebra and the cancelled inclusion g^e⊂Fil¹(g). The main-reader affine crop confirms that no replacement or cancellation changes it. In the concrete group SL₂×SL₂, take e=(E₁₂,0), x=(diag(1,−1),0) and v=(0,diag(1,−1)). Then v centralizes e, but x+v is not in the image of ad(e), whose second component is always zero. It therefore fails condition c) on scan 16. This refutes the unrestricted live affine description in that setting; the positive centralizer is the refined direction. The same example refutes the *cancelled* inclusion; no historical motive for its cancellation is inferred. The separate exact certificate is math_checks/123_017_orbits_certificate.json. R1 also computed the 2×2 commutators independently and considered an added central summand, without claiming to verify all surrounding hypotheses.

The corrected lower bound in Lie U is a definite 1 over an old 0. R2 and R3 independently substituted 1 into the written definition of Fil, obtaining Lie U=Fil¹(g); that formal substitution did not decide the digit. The general orbit-map mechanism was checked conditionally by positive-weight recursion: Ad(exp(v))x−x has weight-k term −k v_k plus lower-weight polynomial terms, giving a polynomial inverse in characteristic zero. The analogous recursion for e uses surjectivity of ad(e):g(k)→g(k+2), k≥1. An exact SL₃ calculation verifies the orbit formulas and first inverse in a concrete case. The exponential identification and the decomposition into SL₂ strings are background inputs, explicitly separated from these checks in math_checks/123_017_graded_orbit_argument.md. No general proof of reductivity, existence of P/U/L, the full open-orbit assertion, or independence of P,H and i mod U was performed.

**Source revisions, slips, and metadata.** The source carries the literal “Bour” and “i.e;”. It cancels “nt” in satisfassent, “qui”, the underlined “torseur”, an extra “en|un”, and the e in une. The handwritten top note is itself cancelled, and the two connected graphic marks are retained. The overprinted u/a and aassi/aussi are not silently corrected by grammar. “Sous-groupe de Lévi de G” is retained without treating that conventional phrasing as an error. There is no explicit “à vérifier”, “sauf erreur”, “je présume”, or authorial question mark on this sheet; the remaining question marks in the edition mark reading uncertainty. No title, composition date, signature or total page count is written here. The lower-left 16 is recorded as an archive-sheet comment, not an authorial page count. No external sources were researched.'''
who='GPT-6 Astra Pro; inherited effort (not exposed); root run'
spec['check_events']=[
 dict(statement_id='123-017-affine-literal',who=who,type='refuted, with refined statement 123-017-affine-positive-centralizer',outcome='Ink confirms live a+g^e. In SL2×SL2, adding (0,h) centralizes e=(E,0) but violates x in Im(ad e); the same vector refutes the explicitly cancelled inclusion g^e⊂Fil¹g. Transcription remains literal.'),
 dict(statement_id='123-017-affine-positive-centralizer',who=who,type='targeted proof check',outcome='Positive-weight centralizer is bracket closed and stable under ad x. The already-recorded graded recursion gives its affine orbit, conditionally on exponential identification.'),
 dict(statement_id='123-017-general-structural-claims',who=who,type='carried as background without fault found',outcome='General open homogeneous orbit, reductivity, parabolic/Levi structure, and independence of P,H and i mod U are source claims, not proved in this run.'),
 dict(statement_id='123-017-affine-direction-comparison',who='GPT-6 Astra Pro; inherited effort (not exposed); '+stem+'/R1',type='computation or formal certificate',outcome='Reader independently computed [E,aH+bE+cF]=cH−2aE and compared the centralizer after adding a central summand; scope of surrounding hypotheses explicitly left open.')]
for r in ['R2','R3']:
 spec['check_events'].append(dict(statement_id='123-017-fil1-definition',who='GPT-6 Astra Pro; inherited effort (not exposed); '+stem+'/'+r,type='targeted proof check',outcome='Actually substituted k=1 in the displayed Fil definition and renamed the summation index, obtaining the displayed corrected Lie U expression. No group existence or orbit theorem is thereby verified.'))
 spec['check_events'].append(dict(statement_id='123-017-affine-direction-comparison',who='GPT-6 Astra Pro; inherited effort (not exposed); '+stem+'/'+r,type='used and rechecked in this run',outcome='Compared the corrected acting algebra with the untouched a+g^e and the cancelled inclusion. Recorded their mismatch without claiming a counterexample or a general theorem proof.'))
spec['abbreviations']=[copy.deepcopy(x) for x in R['R3']['abbreviations'] if 'tfrac' not in x['form']]
spec['abbreviations'].append(dict(form='written raised 1 / lower 2, followed by -direct',expansion='Editorial interpretation: semi-direct; the written fraction is not expanded in the transcription.'))
spec['consequential']=['123/017: the live a+g^e survives the correction to Lie(Z+); its explicit SL₂×SL₂ counterexample is recorded separately, without emending the source.','123/017: the corrected Lie U lower bound 1 is resolved from the overprinted digit, with old 0 preserved.','123/017: the marginal relation is ≃, and the written fraction before -direct replaces both witnesses’ expansion semi-direct.']
spec['workflow_note']='All three independent readers completed the entire page. Root compared their full texts and reports and viewed all disputed loci on existing reader crops or four new local crops. R2 and R3 initially followed the witnesses’ expansion semi-direct; a neutral request for the exact visible strokes in the already-viewed margin crop led them independently to report a fraction. R1’s contrary return is retained in the decision record. No new crop or other reader text was supplied to them. This prompted a brief refinement against expanding a sign into a plausible word. Root also distinguished uncertain reading from uncertain chronology of overprints. One initial affine-crop display was truncated; it was displayed successfully on resumption and only that successful view supports the decision. R3 attempted an optional TeX compile but lualatex.fmt was unavailable; no compiled verification is claimed.'
path=O/'decisions'/f'{stem}_spec.json';path.write_text(json.dumps(spec,ensure_ascii=False,indent=2))
t=t3
for e in spec['text_edits']:
 assert t.count(e['old'])==1,(e['old'],t.count(e['old']))
 t=t.replace(e['old'],e['new'])
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(path)
print('Root specification and preview saved; not finalized.')
