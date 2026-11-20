from pathlib import Path
import json
from datetime import datetime,timezone
root=Path('/workspace/scratch/2b715fe259c4/SP35_CW_156-7/readers/R3')
src=Path('/workspace/scratch/2b715fe259c4/source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan005.tex')
s=src.read_text()
repl=[
(r'\deleted{\unsure{$\mathscr F$}}',r'\deleted{$\mathscr F$}'),
(r'\textcircled{\scriptsize\unsure{f}}',r'\textcircled{\scriptsize f}'),
(r'\deleted{\unsure{éléments}}',r'\deleted{\uline{\unsure{éléments}}}'),
(r'\deleted{\unsure{At 1}}',r'\deleted{\unsure{At 1|At 4}}'),
(r'\deleted{\unsure{et|4}}',r'\deleted{\unsure{4|et}}'),
(r'Si $F,\unsure{C|G}\in\mathscr F$',r'Si $F,C\in\mathscr F$'),
(r'F\unsure{\mathrel{\tikz[baseline=-.45ex,x=.7em,y=.45em]{\draw (0,-.44)--(0,.44) (0,0)--(1.2,0) (1.2,-.44)--(1.2,.44);}}|\mapsto}\widetilde F',r'F\mathrel{\tikz[baseline=-.45ex,x=.7em,y=.45em]{\draw (0,-.44)--(0,.44) (0,0)--(1.2,0) (1.2,-.44)--(1.2,.44);}}\widetilde F'),
(r'\unsure{\mathscr F|\mathscr P}(M)',r'\mathscr F(M)'),
(r'\Phi\unsure{\in|+}\widetilde{\mathscr F}',r'\Phi\unsure{+|\in}\widetilde{\mathscr F}'),
(r'\unsure{un|une} ens',r'un ens'),
(r'\unsure{\overline{\mathscr F}|\widetilde{\mathscr F}}',r'\overline{\mathscr F}'),
(r'\text{plus petit élément }\deleted{\unsure{F}}',r'\text{plus petit élément }\deleted{F}'),
(r'\unsure{toute|toutes}',r'\unsure{toutes|toute}'),
(r'\unsure{défn|defn}',r'\unsure{dfn|defn}'),
(r'\{F,G\}\ \text{majoré',r'\{F,\unsure{C|G}\}\ \text{majoré'),
(r'&\unsure{X|\forall}\ ',r'&X\ '),
]
# The literal lower label contains a TeX math prime, not a Python escape.
repl=[x for x in repl if not x[0].startswith('\\text{\\unsure{a|c}')]
repl.append(("\\text{\\unsure{a|c}$'$)}", "\\text{a$'$)}"))
for a,b in repl:
 if a not in s: raise SystemExit('Missing replacement: '+a)
 s=s.replace(a,b,1)
old=r'\margin{$\widetilde{\mathscr F}\neq\varnothing$ automatique si $M\neq\varnothing$ et dans tous les cas, \unsure{équivaut} à $\varnothing\in\widetilde{\mathscr F}$}'
new=r'''% An oblique connector rises to the right from the marginal note, ending left of the upper conditions; it does not end beside c).
\margin{$\widetilde{\mathscr F}\neq\varnothing$ automatique si $M\neq\varnothing$ et dans tous les cas, \unsure{équivaut} à $\varnothing\in\widetilde{\mathscr F}$\quad\tikz[x=.65em,y=.65em]{\draw[->] (0,0) .. controls (.65,.05) and (1.8,.7) .. (2.9,1.7);}}'''
assert old in s
s=s.replace(old,new)
(root/'scan005.tex').write_text(s)
manifest=json.loads((root/'scan005_crops.json').read_text())
for x in manifest:
 if 'path' in x:
  x['file']='SP35_CW_156-7/readers/R3/crops/'+Path(x['path']).name
  x['rotation_degrees']=x.pop('rotate')
  x.pop('path');x['source']='H156-01_156-7_scan005.jpg'
(root/'scan005_crops.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
cm={Path(x['file']).stem:x for x in manifest}
rows=[];aud=[]
def add(place,C,H,reading,evidence,kind='other',conf='high',crop=None,dc=False,dh=True,marked=False,doubt='not applicable',math=None):
 id=f'R3-005-{len(rows)+1:02}'
 rows.append(dict(id=id,place=place,C=C,H=H,reading=reading,diff_C=dc,diff_H=dh,kind=kind,marked_in_H=marked,confidence=conf,evidence=evidence,crop=('readers/R3/crops/'+crop+'.png') if crop else None,crop_coordinates=cm[crop]['box'] if crop else None,C_doubt_status=doubt,math_consequence=math))
 return id
def audit(n,place,C,reading,status,evidence,crop,row):
 aud.append(dict(number=n,place=place,C=C,reading=reading,status=status,evidence=evidence,crop=('readers/R3/crops/'+crop+'.png') if crop else None,crop_coordinates=cm[crop]['box'] if crop else None,difference_id=row))
def da(n,place,C,H,reading,evidence,crop,dc=False,dh=True,conf='medium',status='retained',kind='other',marked=False,math=None):
 row=add(place,C,H,reading,evidence,kind,conf,crop,dc,dh,marked,('resolved' if status=='resolved' else 'retained'),math)
 audit(n,place,C,reading,status,evidence,crop,row)

da(1,'overwritten manuscript page number',r'\deleted{\unsure{3}}4','described as an overwritten digit; no literal reading',r'\deleted{\unsure{3}}4','The live long downward stroke and angled top form 4; the heavily overdrawn older curved lobes can be 3 but do not settle it.','005_page_quote',conf='low',kind='omission',marked=True)
da(2,'first circled table label',r'\unsure{e}','(e), with a note that the sign is circled',r'\textcircled{\scriptsize\unsure{e}}','The circle overlaps a small loop and several dark strokes; e remains possible but is not secured by sequence alone.','005_e_M_script',conf='low',kind='drawing or diagram',marked=True)
da(3,'table and recurring M alphabet',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}','The capital has two high stems and a rounded central trough; the degree of cursive shaping does not determine a named math alphabet.','005_e_M_script',kind='misread symbol or index')
da(4,'opening quotation mark before figures',r'\unsure{``}','«',r'\unsure{``}','The opening area meets the overwritten page number and the long initial f; distinct paired opening ticks cannot be isolated, unlike the closing pair.','005_page_quote',conf='low')
da(5,'recurring figure-set alphabet',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}','The capital has a looped top arm and separate middle cross-stroke, with no Gothic angular body. The two script fonts remain a representational ambiguity.','005_e_M_script',kind='misread symbol or index')
add('position of subset symbol in entry e','figures ⊂𝓕 élémentaires','figures élémentaires … multistrates ⊂𝔉','figures ⊂𝓕 élémentaires','The subset sign and set letter sit immediately after figures, above the following continuation; H relocates them after multistrates.','insertion or placement',crop='005_e_M_script')
add('opening left marginal definition','strates; déployement; strates, all underlined where shown','strates plain; déploiement; final strates plain','underlined strates; underlined déployement; underlined strates','The first word and the later strates have independent baseline rules. The spelling has a descending y in déployement.','abbreviation expanded or spelling modernised')
add('left marginal bracket and line punctuation','bracket reproduced; no semicolon after F or stop after displayed set','bracket described; semicolon after F and full stop after displayed set','drawn bracket; no added semicolon or full stop','The marginal block is connected to entry e by a bent bracket. Its definition lines end at F and the closing brace with no separate punctuation dots.','drawing or diagram')
da(6,'upper-right gloss, cancelled set letter',r'\deleted{\unsure{$\mathscr F$}}','omitted',r'\deleted{$\mathscr F$}','The crossed group has one vertical stem and two rightward arms, the middle arm closed into a small loop: F survives the strike.','005_top_right_deleted',dc=True,status='resolved',conf='high',kind='omission')
add('end of upper-right gloss','dans 𝓕 without terminal semicolon','dans 𝔉 ;','dans 𝓕','There is no separate semicolon after the last figure-set letter.','text not on the page')
da(7,'second circled table label',r'\unsure{f}','(f), circled sign described',r'\textcircled{\scriptsize f}','The enclosed character shows the high hooked stroke and a horizontal crossbar of f, distinct from the outer circle.','005_f_deleted',dc=True,status='resolved',conf='high',kind='drawing or diagram')
da(8,'entry f, L alphabet',r'\unsure{L|\mathcal L}',r'\mathcal L',r'\unsure{L|\mathcal L}','The tall stem curls into a low loop and long foot. The handwritten form does not choose uniquely between ordinary cursive L and a calligraphic font.','005_f_deleted',kind='misread symbol or index')
da(9,'entry f, cancelled first word',r'\deleted{\unsure{éléments}}','unread cancelled and underlined word described in note',r'\deleted{\uline{\unsure{éléments}}}','The thick cancellation obscures most body letters, so éléments remains doubtful; a separate unbroken underline lies below the cancelled baseline. That underline belongs to the older word, not inserted lieux.','005_f_deleted',dc=True,conf='low',status='changed',kind='deletion state (struck given live or live given struck)',marked=True)
da(10,'entry f, cancelled second word',r'\deleted{\unsure{minimaux}}','omitted',r'\deleted{\unsure{minimaux}}','A long cancellation leaves short humps, a dotted stem and an ending compatible with minimaux; most of the letters remain covered.','005_f_deleted',conf='low',kind='omission')
add('entry f, inserted lieux and link','inserted lieux; long drawn connector; no colon or terminal stop','underlined lieux : elements …; terminal stop; connector described','inserted “lieux” without its own underline; drawn connector; no colon or terminal stop','The inserted word sits above the cancellation. The lower underline belongs to the old word; the long line runs toward the right gloss. No colon follows the inserted word.','insertion or placement',crop='005_f_deleted')
add('quotation shapes across page','paired backtick/apostrophe strokes','guillemets around figures élémentaires, lieux, sine qua non','paired quotation strokes, opening before figures still uncertain','The certain quote groups consist of small paired vertical/sloping ticks, not angle-shaped guillemets.','other',crop='005_f_deleted')
add('axioms introduction, first three','Les premiers trois [inserted At 1 - At 3] ne concernent que (𝓕,≤)','Les premiers trois [inserted concernent] (At 1 – At 3) [unread deletion] (𝔉,≤)','Les premiers trois [inserted At 1 - At 3] ne concernent que (𝓕,≤)','The live line contains ne concernent que. At 1 - At 3 sits above it as the insertion; no parentheses surround those labels.','insertion or placement')
da(11,'intro, first cancelled axiom label',r'\deleted{\unsure{At 1}}','note reads cancelled At 4',r'\deleted{\unsure{At 1|At 4}}','The A/t-like strokes are crossed heavily. The final tall angular digit has a low crossing stroke; both 1 and 4 remain possible without relying on axiom sequence.','005_intro_deleted',dc=True,status='changed',conf='low',kind='misread symbol or index',marked=True)
da(12,'intro, next cancelled group',r'\deleted{\unsure{et|4}}','omitted',r'\deleted{\unsure{4|et}}','Below the dense cancellation a tall right stem and diagonal left approach give 4 the stronger literal reading; the upper covered portion still permits et.','005_intro_deleted',dc=True,status='changed',conf='low',kind='omission')
add('axioms introductory paragraph ending','ends at ≪, without stop','ends at ≪.','no full stop after ≪','The last inequality is followed by blank paper, without a punctuation dot.','text not on the page')
add('At 1 sloping marginal heading','Axiomes des underlined sommes majorées de figures','Axiome des sommes majorées de figures','Axiomes des underlined sommes majorées de figures','The heading has a terminal s; the following phrase is ruled beneath, whereas H removes both the plural and that emphasis.','misread word')
da(13,'At 2 margin, first paired figure letter',r'F,\unsure{C|G}','F,G','F,C','The second capital is an open C-shaped curve with no internal bar; the G in the next line has a distinct inward hooked stroke.','005_At2_margin',dc=True,status='resolved',conf='high',kind='misread symbol or index',math='The initial pair is F,C, but the following equivalence uses G. Retain the literal mismatch.')
add('At 2 marginal prose','équivaut à : Si … Critère d’inclusion de figures par strates','équivalent à : si … — Critère d’inclusion des figures par strates','équivaut à : Si … Critère [underlined d’inclusion de figures par strates]','The verb ends in vaut, the conditional starts with capital S, and de has no terminal s. The rule begins under inclusion, not Critère; there is no inserted dash between the formula and Critère.','misread word',crop='005_At2_margin')
da(14,'At 2, overwritten letter before est',r'\deleted{\unsure{d}}est','est only',r'\deleted{\unsure{d}}est','A high stem and extra loop precede/overlap est; a d is plausible, but its exact former contour is obscured by the live e.','005_At2_deleted',conf='low',kind='omission')
da(15,'Scholie, mapping-looking sign',r'\unsure{double-tick horizontal|\mapsto}',r'\mapsto','horizontal stroke terminated by two vertical ticks','Both ends of the shaft end in short near-vertical strokes. No diagonal arrowhead exists at the right end.','005_scholie_mapping',dc=True,status='resolved',conf='high',kind='misread symbol or index',math='The syntax suggests a mapping, but the literal drawn mark is retained rather than normalized to mapsto.')
da(16,'Scholie, set letter before (M)',r'\unsure{\mathscr F|\mathscr P}(M)',r'\mathfrak F(\mathcal M)',r'\mathscr F(M)','The capital before (M) has an independent middle cross-stroke below the looped top, making F rather than P.','005_scholie_set',dc=True,status='resolved',conf='high',kind='misread symbol or index',math='Keep F(M); do not replace it with the expected powerset P(M).')
add('Scholie, axiom labels and order phrase','At portions separately underlined; ens ordonné (pour ≤)','At labels plain; ens. ordonné (par ≤)','underlined At 1 et At 2; ens ordonné (pour ≤)','The short strokes underline At, not the numeral. The preposition has the long ou sequence of pour. There is no abbreviation dot after ens.','misread word')
da(17,'Scholie condition a, Greek letter',r'\unsure{\Phi|\varphi}',r'\Phi',r'\unsure{\Phi|\varphi}','The closed loop is crossed by a vertical stem ending below it; the top is too joined to decide capital Phi against the handwritten lowercase alternative.','005_condition_a',kind='misread symbol or index')
add('Scholie condition a, adjective','fermés',r'\uncertain{fermées}','fermés','After the acute-bearing e, the word ends in s with no additional e loop.','misread word',crop='005_condition_a',marked=True)
add('Scholie condition b opening','Si','si','Si','The clause starts with a capital S.','other')
da(18,'under cancelled c formula',r'\deleted{\unsure{(et}}','unread parenthetical word described in note',r'\deleted{\unsure{(et}}','An opening parenthesis remains at left, with a heavily struck short group and surviving tall stroke compatible with t. The e is hidden.','005_condition_c',conf='low',kind='omission',marked=True)
da(19,'c, union subscript',r'\unsure{\in|+}',r'\in',r'\unsure{+|\in}','The small mark between Φ and the figure-set letter appears as a straight crossing with an upright arm. A compressed membership sign cannot be excluded, but no clean curved left side is visible.','005_condition_c',dc=True,status='changed',conf='low',kind='misread symbol or index',math='A literal plus-like mark would make this an unconventional union index; no normalization from set theory is made.')
da(20,'c, last verb of sloping note',r'\unsure{équivaut}','et donc / unread fragments',r'\unsure{équivaut}','The initial é/q/ui is present; the final faint joined run is compatible with vaut but does not permit certainty.','005_c_margin',kind=r'readable ink left as \ill{}',marked=True)
add('c, complete marginal note apart from uncertain verb','𝓕̃≠∅ automatique si M≠∅ et dans tous les cas, [équivaut] à ∅∈𝓕̃','𝔉̃≠∅ [unread] [unread] et donc ∅∈𝔉̃','𝓕̃≠∅ automatique si M≠∅ et dans tous les cas, [équivaut] à ∅∈𝓕̃','The sloped lines visibly contain automatique si M≠∅, et dans tous les cas, and à before the last formula. These are not two unread blocks or et donc. The doubtful final verb is separately audited.','readable ink left as \\ill{}',conf='medium',crop='005_c_margin',marked=True)
add('connector from c-side sloping note','no connector reproduced','arrow described as going toward c','thin curved arrow rising to the right, ending left of the upper conditions','The arrow ends substantially above the written c), near the space left of a)/b). Its upward slant and arrowhead are visible; H’s precise destination c is not supported by the geometry.','drawing or diagram',crop='005_c_connector',dc=True)
da(21,'transition, article before ens',r'\unsure{un|une}','un',r'un','The short article has two joined humps and a terminal downstroke; no separate final e loop is visible.','005_un_ens',dc=True,dh=False,status='resolved',conf='high')
add('transition and b-prime abbreviations','ens; l’ens, without points','ens.; l’ens.','ens; l’ens, without points','The short words end in a continuous low stroke. No detached punctuation dot follows either occurrence.','other',crop='005_bprime')
add('b-prime variable case',r'\forall x,\ \widetilde{\mathscr F}^{x},\ x\in\Phi',r'\forall X,\ \widetilde{\mathfrak F}^{X},\ X\in\Phi',r'\forall x,\ \widetilde{\mathscr F}^{x},\ x\in\Phi','All three variable crosses are small compared with M and the explicitly named capital X with tilde on the next line.','misread symbol or index',crop='005_bprime')
da(22,'b-prime first cancelled symbol in braces',r'\deleted{\unsure{F}}\Phi','Φ only',r'\deleted{\unsure{F}}\Phi','The extra crossed stem and arms under the live Φ remain visible, but overlap prevents a secure complete letter. F remains the first candidate.','005_bprime',conf='low',kind='omission')
da(23,'b-prime set after membership',r'\unsure{\overline{\mathscr F}|\widetilde{\mathscr F}}',r'\widetilde{\mathfrak F}',r'\overline{\mathscr F}','The mark is a single straight rising rule; the tilde over the earlier set has a distinct dip and rising right curl.','005_bprime',dc=True,status='resolved',conf='high',kind='misread symbol or index',math='Retain the bar despite neighboring tilded occurrences of the same apparent set.')
da(24,'b-prime after élément',r'\deleted{\unsure{F}}','omitted',r'\deleted{F}','A dark vertical stem and upper and middle arms survive the cancellation; the symbol is F.','005_bprime',dc=True,status='resolved',conf='high',kind='omission')
da(25,'lower primed condition label',r'\unsure{a|c}\prime','d′','a′','The small enclosed bowl is closed and has a right foot; it is an a shape, not an open c and not a tall-stemmed d.','005_aprime',dc=True,status='resolved',conf='high',kind='misread symbol or index')
da(26,'before Dans in lower primed clause',r'\deleted{\unsure{\forall|F}}',r'cancelled \forall described in note',r'\deleted{\unsure{\forall|F}}','Two slanted upper strokes suggest an inverted A, but a vertical stem and crossing arms remain entangled with the cancellation.','005_aprime',conf='low',kind='deletion state (struck given live or live given struck)',marked=True)
da(27,'lower primed clause before famille',r'\unsure{toute|toutes}','toute',r'\unsure{toutes|toute}','The terminal hook after the second t/e-like run looks like an additional s. Because the cursive joining is compressed, toute remains possible; singular famille is not used to force the article.','005_aprime',dc=True,status='changed',kind='misread word')
add('left connector between primed clauses','upward curved arrow','described as a brace','upward curved arrow from lower primed clause toward b′','The left stroke has a directional point at its upper end and curves upward; it is not a symmetric grouping brace.','drawing or diagram')
add('Relation heading','Relation, plain','underlined Relation','Relation, plain','No baseline rule appears under the heading.','other')
da(28,'annotation above compatibility equivalence',r'\unsure{défn|defn}','déf',r'\unsure{dfn|defn}','The annotation begins with a rounded d, has a tall f-like stem, and ends in a low n-like run. No separate accent is visible; a distinct e cannot be confidently isolated.','005_compatibility_def',dc=True,status='changed',kind='misread word')
add('compatibility defining join','F∨C','F∨G','F∨C','The second operand is an open crescent with its lower tip bent down, unlike the closed inward arm in the preceding G.','misread symbol or index',crop='005_compatibility_def',math='The letter differs from the F,G pair on the left; it is retained as written.')
add('compatibility displayed set pair','{F,G}','{F,G}',r'\{F,\unsure{C|G}\}','The second set entry is also an open curve with a low rightward tip, without the inward bar of the earlier G. A hastily formed G remains possible, so the new doubt is marked.','misread symbol or index',conf='medium',crop='005_compatibility_def',dc=True,math='Both witnesses read G confidently; the visible form warrants C|G rather than silently imposing the matching variable.')
add('compatibility display punctuation','existe i.e.; figures compatibles without following stop','existe, i.e.; figures compatibles.','existe i.e.; figures compatibles without following stop','No comma lies between existe and i.e.; the underlined caption is not followed by a full stop.','text not on the page',crop='005_compatibility_def')
da(29,'before se reconstitue',r'\deleted{\unsure{est}}',r'\struck{\ill{}}',r'\deleted{\unsure{est}}','The short crossed run permits est, with a surviving final upright; the earlier letters remain hidden under the multiple diagonal strokes.','005_bottom_deleted',conf='low',kind=r'readable ink left as \ill{}',marked=True)
add('inserted qualification before se reconstitue','avec At 1, At 2, At 3','avec (At 1, At 2, At 3)','avec At 1, At 2, At 3, attached by bent insertion connector','The apparently parenthetical curve before At 1 is the long descending f of figures in the line above. There is no separate closing parenthesis after At 3; the lower long stroke is the insertion connector.','insertion or placement',crop='005_bottom_insertion')
da(30,'final brace, first line initial symbol',r'\unsure{X|\forall}',r'X\between X',r'X\text{ [compatibility sign] réflexive symétrique}','Two diagonals cross without a horizontal bar: the initial sign is X. There is no second X between the compatibility sign and réflexive.','005_final_brace',dc=True,status='resolved',conf='high',kind='text not on the page',math='The first line is not completed to the expected reflexivity formula; the missing right operand is left missing.')
add('final brace adjective punctuation','réflexive symétrique','réflexive, symétrique','réflexive symétrique','The two adjectives are separated by blank space with no comma stroke.','text not on the page',crop='005_final_brace')

coverage=[
'Overwritten manuscript page number; entry e with circled label, alphabet, quotes, every underline, and subset placement.',
'Left strates/déployement/incidence block, all quantifiers and braces, its underlines and connecting bracket.',
'Right irreducibility gloss and induced relations, subscripts M, cancellation and terminal punctuation.',
'Entry f, circled label, L⊂M, abbreviation, two cancelled words, underline under first word, inserted lieux, long pointer, right-hand minimal-elements gloss and null-set subscript.',
'Axiomes heading; I) sine qua non paragraph; insertion At1–At3, live ne concernent que, pair of cancelled groups, At4–At7 and both order signs.',
'At1 complete formula including capital index I and parenthetic I quelconque; sloping sums margin.',
'At2 complete prose/display, overwritten initial letter, Sup subscript X∈F̃, where-clause and set builder.',
'Entire rotated At2 margin: title, equivalence verb, Si F,C, quantifiers, every X/Y and tilde, final inclusion criterion and its underline.',
'Scholie entire sentence, axiom-label underlines, double-tick sign, F(M), M alphabet, ens abbreviation and pour.',
'Clauses a,b,c including Greek-letter forms, adjective endings, cancelled nonemptiness equivalence, cancelled short group, union index, live nonemptiness.',
'Entire rotated c margin and its oblique arrow, kept without falsely precise c endpoint.',
'Order-free transition and both primed conditions in their written order; every case, exponent, tilde/bar, braces, cancellations, prime label, family ending and underlined et.',
'Upward curved arrow between lower primed clause and b′.',
'Relation heading, every compatibility glyph, defining arrow/annotation, F∨C, ambiguous set-pair letter, i.e. punctuation, compatibility caption and underlines.',
'Final reconstruction prose: induced relation, M, finite-type abbreviation t.f., cancelled est, inserted axiom qualification and bent connector.',
'Final reconstruction tuple and relation conditions: initial isolated X, no supplied right operand, no comma between adjectives; second line has all primes, inequalities, comma separation and implication.'
]
notation=[
{'symbol':'M, L','reading':r'\unsure{M|\mathcal M}, \unsure{L|\mathcal L}','evidence':'Continue the handwritten-cursive alphabet uncertainty from earlier pages; do not force a separate calligraphic alphabet from H.'},
{'symbol':'figure set F','reading':r'\unsure{\mathscr F|\mathcal F}','evidence':'Looped top and middle bar, not Gothic. The F before (M) is resolved against P.'},
{'symbol':'F to F̃ sign','reading':'horizontal line with vertical ticks at both ends','evidence':'Both terminal ticks visible; no arrowhead.'},
{'symbol':'b′ F̄','reading':r'\overline{\mathscr F}','evidence':'Straight rule contrasts with the neighboring wave marks.'},
{'symbol':'compatibility','reading':'crossed double chevrons reproduced in TikZ','evidence':'The complete crossing glyph is larger than a simple ×; all occurrences compared on this page.'},
{'symbol':'C/G','reading':'literal C in At2 first margin pair and in F∨C; new C|G in displayed set pair','evidence':'Open curves compared directly with the fully inward-hooked G earlier in the same formula.'},
{'symbol':'Greek loop letter','reading':r'\unsure{\Phi|\varphi}','evidence':'Closed loop with descending stem; case remains uncertain at first occurrence.'},
{'symbol':'definition label','reading':r'\unsure{dfn|defn}','evidence':'No accent visible; final n visible; separate e not secure.'}
]
math_notes=[
{'id':'R3-S005-N1','type':'reading summary, not a proof check','content':'The page finishes the data list with multistrates M, strata/deployment F̃ and incidence X triangleleft F, then loci L via minimal nonempty figures for refinement.'},
{'id':'R3-S005-N2','type':'reading summary, not a proof check','content':'At1 requires a nonempty figure collection closed under bounded suprema. At2 states that a figure is the supremum of its strata. The Scholium describes collections of lower subsets and an order-free reformulation.'},
{'id':'R3-S005-N3','type':'reading summary, not a proof check','content':'The bottom defines compatibility through the existence of a join and boundedness, and states finite-type reconstruction from M with order and compatibility under At1, At2, At3.'},
{'id':'R3-S005-N4','type':'ink-based parse warning, not a theorem check','content':'The syntax via F … F̃ suggests a mapping but the ink is a double-tick shaft; the set letter F(M) has an explicit middle bar. Neither was normalized to an expected mapsto or powerset P(M).'},
{'id':'R3-S005-N5','type':'ink-based variable/decoration warning, not a theorem check','content':'Literal C in the At2 marginal first pair and in F∨C contrasts with following G. The displayed bounded pair has a new C|G doubt. Clause b′ has a visibly straight bar where tildes occur nearby. These are retained.'},
{'id':'R3-S005-N6','type':'ink-based parse warning, not a theorem check','content':'The union index favors a plus-like mark but remains +|∈. The first final condition has X followed by the compatibility sign and the adjectives, with no second operand. No expected reflexivity formula was supplied.'}
]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
out=dict(reader='R3',scan=5,start_utc='2026-11-19 21:30:40 UTC',end_utc=end,model='GPT-6 Astra Pro; effort setting not exposed; run R3',
 images_viewed=['H156-01_156-7_scan005.jpg','H156-01_156-7_scan005_a.jpg','H156-01_156-7_scan005_b.jpg']+[x['file'] for x in manifest],
 workflow='Whole and two supplied halves read once. Twenty tight crops were created: eighteen initially open textual loci plus two distinct still-open connector/insertion-punctuation loci. All were actually viewed. A batched image response was truncated before usable display; the crops were then displayed in small groups, without recreating them.',
 coverage=coverage,notation=notation,math_notes=math_notes,author_qualifications=['Dans le cas où les figures sont de t.f.','avec At 1, At 2, At 3'],
 unresolved=[{'place':x['place'],'reading':x['reading'],'confidence':next(r['confidence'] for r in rows if r['id']==x['difference_id'])} for x in aud if x['status']!='resolved']+[{'place':'compatibility bounded pair','reading':r'\{F,\unsure{C|G}\}','confidence':'medium'}],differences=rows,C_doubt_audit=aud,
 content_omitted_by_both_witnesses=[{'place':'compatibility bounded pair','observation':'Both witnesses give G; this reading marks a newly observed C|G uncertainty. This is a changed reading, not new extra text.'}],
 proof_checks_performed=[])
(root/'scan005.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
lines=['# R3 independent reading — scan 005 (manuscript page 4)','','Complete proposed page: `scan005.tex`. Structured collation and all 30 C-doubt dispositions: `scan005.json`. Twenty crop records: `scan005_crops.json`.','',f'Start: {out["start_utc"]}. End: {end}. Model: {out["model"]}.','','## Principal findings','',
'- Retain the double-tick horizontal mark in the Scholium; the right end is not an arrowhead. The following set letter is F(M), with a visible middle cross-stroke.',
'- Resolve the At2 marginal first pair to F,C; preserve F∨C in the compatibility display. Add a new C|G doubt in its bounded pair {F,C|G}: both witnesses had G.',
'- Clause b′ uses lowercase x, has a straight bar above the set letter after membership, and contains two cancelled F-like letters. The second cancelled F is resolved; the first remains obscured.',
'- Resolve the lower primed clause label to a′. Its final word before famille favors toutes|toute; do not settle it from grammar. The left connection is an upward arrow.',
'- Preserve the cancelled word éléments with its separate underline. The inserted lieux does not inherit that underline. The top-right cancelled script F and circled f are resolved.',
'- Keep the complete marginal notes. The extra oblique arrow from the c-side note points upward to the right, not precisely at c); it was absent from C’s drawing inventory.',
'- The inserted qualification reads avec At 1, At 2, At 3. The apparent opening parenthesis in H is the descending f of figures above; no separate parenthesis pair is present.',
'- The final brace starts with X and the compatibility glyph, then réflexive symétrique, without a second X or comma. No reflexivity formula is supplied.',
'- The small defining label favors dfn|defn, without a visible accent; the separate e is not certain. The union subscript favors +|∈. Both remain marked.',
'', '## Detailed differences', '', '| ID | Place | C | H | R3 | Confidence | Evidence |', '|---|---|---|---|---|---|---|']
for r in rows:
 vals=[r[k] for k in ['id','place','C','H','reading','confidence','evidence']]
 lines.append('| '+' | '.join(str(v).replace('|','\\|').replace('\n',' ') for v in vals)+' |')
lines+=['','## C-doubt audit','','| No. | Place | C reading | R3 reading | Status |','|---:|---|---|---|---|']
for a in aud:
 lines.append('| '+' | '.join(str(a[k]).replace('|','\\|') for k in ['number','place','C','reading','status'])+' |')
lines+=['','## Notes while reading','']+[f'- **{x["type"]}:** {x["content"]}' for x in math_notes]+['','No targeted proof check or independent re-proof was performed; these are transcription and notation observations only.','']
(root/'scan005.md').write_text('\n'.join(lines))
print(json.dumps({'written':['scan005.tex','scan005.json','scan005.md','scan005_crops.json'],'differences':len(rows),'C_doubts':len(aud),'crops':len(manifest),'end_utc':end},ensure_ascii=False))
