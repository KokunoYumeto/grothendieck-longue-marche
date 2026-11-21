import json
from pathlib import Path
base=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
page=base/'readers/149_scan102'
packet=json.loads((page/'input.json').read_text())
manifest=json.loads((page/'crop_manifest.json').read_text())
draft=r"""\scanpage{102}
Ce qui signifie aussi que tt \inserted{(ou un)} scindage
de 31 --- p.ex. défini par un pt de $U_\eta$
rat/$K$ --- induit un hom $T\longrightarrow\pi$)

\noindent c) L'action de $T$ sur $\pi_{\mathrm{ab}}=H_1(U_{\bar\eta})$ est
triviale.

\noindent d) Item pour $H_1(U_{\bar\eta},T_\ell)$, \unsure{où|si} $\ell$ est premier
à la car. résiduelle. (\uline{NB} \deleted{\unsure{Pour car.} $p\unsure{>0}$} \inserted{$\ell=p>0$},
on doit pouvoir l'exprimer par un critère
sur le groupe $p$-divisible\ldots)

\noindent e) (En termes d'une section de (30),
définissant une extension de $\mathcal E_k$ par $\pi$,
et supposant maintenant $k$ de type
fini sur $\mathbf Q$) La dite extension est
admissible (quitte à passer à un
sous groupe ouvert \inserted{de $\mathcal E_k$,} au besoin), i.e.
peut être défini par une courbe alg.
sur \inserted{$k$, ou sur} une extension finie de $k$.

\noindent f) (En termes d'une section de (30)
et d'une de (31)., permettant de
faire opérer $\mathcal E_k$ sur $\pi$) : Cette
action \inserted{n'}est \inserted{pas trop} loufoque (à définir convenablement !)% The end of convenablement continues on a short lower baseline; no hyphen is written.
\margin{101}
"""
(page/'draft.tex').write_text(draft)
changes=[]
def add(place,c,h,final,evidence,name,confidence='high',kind='misread word',against_c=False,against_h=True,marked=False,consequential=False):
 changes.append(dict(place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/149_scan102_{name}.png',box=manifest[name][0],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked,consequential=consequential))
add('opening_no_parenthesis','Ce','(Ce','Ce','The upper line begins with the large open C followed directly by the small e. The blank area to its left contains no independent opening parenthesis. The closing parenthesis after the T-to-pi homomorphism is nevertheless present and is preserved.','opening_start',kind='text not on the page')
add('opening_tt',r'\unsure{tt|$\forall$}','$H$','tt','Two upright stems have separate hooked feet and one shared crossbar. Their lower ends do not join into the V-shaped apex required by a universal quantifier. The paired t structure can also be compared locally with quitte in the e_quitte crop; no extra e follows the abbreviation.','opening_revision',confidence='medium',kind='misread symbol or index',consequential=True)
add('opening_inserted',r'\inserted{(ou un)}',r'(\uncertain{seul} \add{(\ill{} \ill{})}',r'\inserted{(ou un)}','The raised line has its own opening and closing parentheses; within them are a small o/u group and a separate two-hump un. No tall l supports seul. A separate long curved leader below the raised words returns to the gap after tt and before scindage; that leader is not an extra textual parenthesis.','opening_revision',kind='insertion or placement',marked=True,consequential=True)
add('opening_scindage','scindage',r'\uncertain{dans} \ill{}','scindage','The baseline word has initial s, open c, dotted i, a compressed n, an ascending d, then the a and a long g descender with the final e return. The beginning is not the d of dans, and the g is independently visible.','opening_revision',marked=True)
add('opening_U_eta',r'U_\eta',r'U_{\bar\xi}',r'U_\eta','After U the low index has a single hump and a long descending right leg curling left. No independent upper bar is present. The clear barred eta forms in c) and d) provide direct local comparisons for both the letter and the missing bar here.','point_U',kind='misread symbol or index',consequential=True)
add('rat_without_stop','rat.',r'\ill{}','rat','The short form before the slash has a low r/a run and a high final t with a short cross-return. The substantial gap between that ending and the slash is blank: there is no independent abbreviation point.','rat_K',confidence='medium',kind=r'readable ink left as \ill{}',against_c=True,marked=True)
add('hom_short_form','hom','homom.','hom','A tall h is followed by the low o/m run and a terminal down-turn. Blank paper separates that ending from T; there is neither another om group nor a stop.','induit_hom',kind='abbreviation expanded or spelling modernised')
add('c_bar_eta',r'\pi_{\mathrm{ab}}=H_1(U_{\bar\eta})',r'\pi_{\mathrm{ab}}=H_1(U_{\bar\xi})',r'\pi_{\mathrm{ab}}=H_1(U_{\bar\eta})','The subscript after U has one low n-like hump and a long curved descending right leg, with a separate horizontal bar above it. There are no stacked turns of xi. The small 1 after H and the ab after pi are also visible.','c_formula',kind='misread symbol or index',consequential=True)
add('d_Item','Idem','Item','Item','After the serifed capital I stands a single tall stem with a crossbar extending on both sides and a hooked foot. It has no low oval bowl or looped ascender of d; the following compressed e/m run completes Item.','d_Idem',against_c=True,against_h=False)
add('d_bar_eta',r'H_1(U_{\bar\eta},\unsure{T_\ell|\mathbf Z_\ell})',r'H_1(U_{\bar\xi},T_\ell)',r'H_1(U_{\bar\eta},T_\ell)','The index under U again has one hump and one descending right leg under a separate bar. The coefficient has a straight vertical stem beneath a long top bar, followed by the low looped ell: T_ell. It has no diagonal joining a top and bottom stroke as Z would.','d_formula',kind='misread symbol or index',consequential=True)
add('d_cancelled',r'\deleted{\unsure{Pour car.} $p>0$}',r'\struck{\ill{}}',r'\deleted{\unsure{Pour car.} $p\unsure{>0}$}','A horizontal cancellation crosses the baseline after underlined NB. Above and below it remain an initial large looped P-like form, an o/u/r-like run, a low c/a/r-like group and a p descender. The low final relation and numeral overlap the cancellation and the stem of the raised replacement p, so >0 is retained only as a doubtful primary reading. The internal letters of Pour car. are likewise not all separable through the strike.','d_revision',confidence='low',kind=r'readable ink left as \ill{}',marked=True,consequential=True)
add('d_replacement_comma',r'\inserted{$\ell=p>0$},',r'\add{$\ell=p>0$}',r'\inserted{$\ell=p>0$},','The raised replacement has a looped ell, two separate equals bars, p, the two strokes of >, and a rounded 0. Below/right of the 0 a separate curved descending mark supplies the comma before the next-line on. It is not the final closing parenthesis of the NB remark, which occurs later.','d_revision',kind='omission')
add('d_le_groupe','les groupes','le groupe','le groupe','The article ends with one low e return after l and then a clear gap. The noun has the descending g, compressed r/ou run, a p descender and one final e return; neither word has an additional independent terminal s-shaped stroke before its following gap.','d_plural',confidence='medium',against_c=True,against_h=False)
add('d_divisible','divisibles','divisible','divisible','After the two dotted i strokes, s, b and tall l, the word ends with a single low e return. The following blank gap precedes three distinct ellipsis dots; there is no extra s between the e and those dots.','d_plural',confidence='medium',against_c=True,against_h=False)
add('e_opening',"En termes d'une",r'\uncertain{Etant} \uncertain{donnée} une',"En termes d'une",'The initial E is followed by a low n. The next word starts with a tall crossed t and continues as the low e/r/m/e/s run; the following d and apostrophe precede une. There is no second initial d and doubled n/e sequence to support donnée.','e_start',marked=True)
add('e_La_dite','Ladite','La dite','La dite','The capital L ends in a small attached a. A conspicuous blank gap separates that group from the next d bowl and looped ascender; the remaining i/t/e strokes form the second word. The source division La dite is retained.','e_ladite',confidence='medium',kind='abbreviation expanded or spelling modernised',against_c=True,against_h=False)
add('e_un','un','une','un','After the second accented à, the final group consists of the low u/n humps and a short down-turn. No further e return follows before the line ends.','e_quitte')
add('e_sous_groupe','sous-groupe','sous-groupe','sous groupe','The end of sous and the descending initial g of groupe are separated by blank paper. There is no independent horizontal hyphen in that intervening gap; the earlier low horizontal strokes belong to sous itself.','e_subgroup',confidence='medium',kind='text not on the page',against_c=True)
add('e_inserted_de',r'ouvert, \inserted{de $\mathcal E_k$,}',r'\add{\uncertain{ext.} de $\mathcal E_k$,} ... sous-groupe ... ouvert',r'ouvert \inserted{de $\mathcal E_k$,}','The raised text is a looped d/e group followed by E with low k and its own comma. There is no ext. before de. Its curved leader lands after ouvert and before au besoin. Before that leader, after the terminal t of ouvert, no separate comma is visible; the only comma belonging to this join is the one written after the inserted E_k.','e_subgroup',confidence='medium',kind='insertion or placement',against_c=True,marked=True,consequential=True)
add('e_au_besoin','au besoin',r'\ill{} \ill{} \uncertain{sous-groupe} \ill{} \uncertain{ouvert}','au besoin','Following the insertion leader, two low strokes give au, then a tall initial b, low e/s/o strokes, dotted i and final n give besoin, before the closing parenthesis. The words sous groupe ouvert are on the earlier part of this same baseline, before the leader.','e_subgroup',kind=r'readable ink left as \ill{}',marked=True)
add('e_no_toujours','i.e. peut',r'i.e. \ill{}, \uncertain{toujours} \ill{} peut','i.e.\npeut','The baseline ends with dotted i, low e and their abbreviation stops; the next line begins directly with the descending p of peut. No extra comma or word with the tall t and j descender of toujours occupies the intervening space.','e_subgroup',kind='text not on the page',marked=True)
add('e_defini','définie','défini','défini','The ending after the tall f and compressed n is a short i stroke with its separate dot above. Blank paper follows before par; there is no final e loop or return. The written masculine form is retained without repairing agreement with extension.','e_definie',against_c=True,against_h=False)
add('e_field_insertion',r'sur \inserted{$k$, ou sur} une extension finie de $k$.',r'\uncertain{sur} \uncertain{une} \add{$k$, \ill{} \uncertain{sur}} extension finie de $k$.',r'sur \inserted{$k$, ou sur} une extension finie de $k$.','On the upper line are k, a comma, the short o/u group, and sur with its initial s and low u/r. The long slanting leader returns to the gap after baseline sur and before baseline une; une itself remains on the lower writing line, followed by extension finie de k. There is no extra baseline une before the raised k.','e_field',kind='insertion or placement',marked=True,consequential=True)
add('f_opening',"(En termes d'une section de (30)",r'Cette \uncertain{dernière} \uncertain{dans} \ill{} d\'une section de (30)',"(En termes d'une section de (30)",'The initial curved opening parenthesis is followed by a distinct capital E and low n; termes has an initial tall t and low r/m run. The source does not contain the initial Cette or the descending sequence of dernière/dans at this position. The following d’une section de (30) is clear.','f_start',marked=True)
add('f_31_stops','(31),','(31).,','(31).,','After the closing parenthesis is a distinct round dot; farther right is a separate curved comma. Both marks stand apart from the parenthesis and from the initial p of permettant.','f_31',kind='omission',against_c=True,against_h=False)
add('f_no_par',r'faire opérer $\mathcal E_k$',r'faire \uncertain{opérer} \add{\uncertain{par} \ill{}} $\mathcal E_k$',r'faire opérer $\mathcal E_k$','The baseline goes from the dotted/short-stroked ending of opérer directly to the large cursive E with low k. The small words below opérer belong to the separate pas trop insertion and its leader toward the next line; there is no baseline par between opérer and E_k.','f_operer',kind='text not on the page',marked=True)
add('f_negative_condition',r"\inserted{n'}est \inserted{pas trop} loufoque",r'\uncertain{doit} \uncertain{être}',r"\inserted{n'}est \inserted{pas trop} loufoque",'The baseline has the low e/s and tall crossed t of est, then loufoque with its looped l, tall f descender and separate q descender. A raised n with apostrophe has a V-shaped leader into the gap before est. The separate raised pas trop has p descenders and crossed t; its long curved leader lands between est and loufoque. Neither insertion is cancelled.','f_end',kind='insertion or placement',marked=True,consequential=True)
add('f_caution','à définir convenablement',r'\uncertain{(remarque} (où \uncertain{définition} \uncertain{commence} \uncertain{seulement}','à définir convenablement','After a single opening parenthesis is a small a with detached accent, then définir with a d loop, f descender, dotted i and short final r. The visible initial segment convenab at the right continues on the short lower baseline as lement; no written hyphen is supplied. One exclamation and the closing parenthesis complete the remark. There is no extra remarque or second opening parenthesis.','f_end',marked=True,consequential=True)
add('folio101',r'\margin{101}','(nothing)',r'\margin{101}','The lower-left folio has two tall 1 strokes, each with an oblique entry, around one closed oval 0: 101. The number is separate from the main prose.','folio101',kind='omission')
marks=[
 dict(id='M1297',decision='first',reading='tt',evidence='The two uprights have separate hooked feet and a shared crossbar, with no common lower V apex. The paired t structure in quitte supplies a local comparison. The abbreviation is retained without expansion.',crop='crops/149_scan102_opening_revision.png',box=manifest['opening_revision'][0],confidence='medium'),
 dict(id='M1298',decision='first',reading='K',evidence='After the slash, the left tall stroke and the high right branch occupy capital height; the right branch descends separately from its upper tip. Both are appreciably larger and more extended than the small k forms in the e_field crop. The letter is read as uppercase K.',crop='crops/149_scan102_rat_K.png',box=manifest['rat_K'][0],confidence='high'),
 dict(id='M1299',decision='first',reading=r'T_\ell',evidence='One long top bar crosses a single straight upright stem, followed by a separate low looped ell. There is no diagonal or lower horizontal member of Z.',crop='crops/149_scan102_d_formula.png',box=manifest['d_formula'][0],confidence='high'),
 dict(id='M1300',decision='undecided',reading=r'\unsure{où|si}',evidence='After the comma, a short oblique low stroke precedes a flattened horizontal return with one detached upper mark. The first small form cannot be securely distinguished as o or compressed s; the detached mark can be an accent or i dot. Où remains the preferred reading, but si is retained.',crop='crops/149_scan102_d_ou.png',box=manifest['d_ou'][0],confidence='medium')
]
def inv(element,kind,position,first_words,hand='main authorial hand'):
 return dict(element=element,kind=kind,position=position,first_words_or_objects=first_words,sheet_kind='text',hand=hand,transcribed='yes')
inventory=[
 inv('opening','text','top three main baselines, y70–390','Ce qui signifie aussi que tt ... T→pi)'),
 inv('opening_addition','insertion','above first main line, leader after tt','(ou un)'),
 inv('condition_c','text','two main baselines, y401–590','c) L’action de T sur pi_ab=H_1(U_bar_eta) est triviale.'),
 inv('condition_d','text','four main baselines, y590–995','d) Item pour H_1(U_bar_eta,T_ell) ... sur le groupe p-divisible...'),
 inv('cancelled_NB_clause','deletion','after underlined NB, near y710',r'\unsure{Pour car.} p\unsure{>0}'),
 inv('replacement_l_equals_p','insertion','above cancelled NB clause, near y680–705','ell=p>0'),
 inv('condition_e','text','eight main baselines, y1005–1953','e) (En termes d’une section de (30) ...'),
 inv('group_addition','insertion','above sous groupe ouvert / au besoin, leader after ouvert','de E_k,'),
 inv('field_addition','insertion','above final line of e), leader after sur','k, ou sur'),
 inv('condition_f','text','bottom four main lines plus short lower continuation, y1950–2354','f) (En termes d’une section de (30) ... action ... loufoque'),
 inv('negative_n','insertion','above final main line, before est',"n'"),
 inv('negative_pas_trop','insertion','separate upper phrase and leader before loufoque','pas trop'),
 inv('folio','margin note','very bottom-left corner','101','pagination hand; no secure separate writer inferred')
]
spans=[
 ('opening_start','text','Ce qui signifie aussi que'),
 ('opening_revision','insertion',r'tt \inserted{(ou un)} scindage'),
 ('ref31','text','de 31 --- p.ex.'),
 ('point_U','text',r'pt de $U_\eta$'),
 ('rat_K','text',r'rat/$K$'),
 ('induit_hom','text',r'induit un hom $T\longrightarrow\pi$)'),
 ('c_formula','formula',r'\pi_{\mathrm{ab}}=H_1(U_{\bar\eta})'),
 ('d_Idem','text','Item'),
 ('d_formula','formula',r'H_1(U_{\bar\eta},T_\ell)'),
 ('d_ou','text',r'\unsure{où|si}'),
 ('d_revision','deletion and insertion',r'(\uline{NB} \deleted{\unsure{Pour car.} $p\unsure{>0}$} \inserted{$\ell=p>0$},'),
 ('d_on','text','on doit'),
 ('d_plural','text',r'sur le groupe $p$-divisible\ldots)'),
 ('e_start','text',"(En termes d'une section de (30),"),
 ('e_ladite','text','La dite'),
 ('e_quitte','text','quitte à passer à un'),
 ('e_subgroup','insertion',r'sous groupe ouvert \inserted{de $\mathcal E_k$,} au besoin), i.e.'),
 ('e_definie','text','peut être défini par une courbe alg.'),
 ('e_field','insertion',r'sur \inserted{$k$, ou sur} une extension finie de $k$.'),
 ('f_start','text',"f) (En termes d'une section de (30)"),
 ('f_31','text',"et d'une de (31)., permettant de"),
 ('f_operer','text',r'faire opérer $\mathcal E_k$ sur $\pi$)'),
 ('f_end','insertion',r"action \inserted{n'}est \inserted{pas trop} loufoque (à définir convenablement !)"),
 ('folio101','margin note',r'\margin{101}')
]
second=[]
for i,(name,kind,reading) in enumerate(spans,1):
 x0,y0,x1,y1=manifest[name][0]
 if name=='f_end':
  y0=2204 # Encloses both interlinear additions, whose first-pass evidence is shared by f_operer and f_end.
 assert reading in draft,(name,repr(reading))
 second.append(dict(box=f'102-B{i:02d}',kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
notes=("This leaf continues a list of conditions involving the inertia action: c) triviality on the abelianization identified with H_1; d) a prime-to-residual-characteristic coefficient version with a tentative p-divisible-group remark for ell=p; e) admissibility of an extension obtained from a section; and f) a deliberately provisional requirement that an action not be too loufoque. The opening connects a section of (31) with a homomorphism T→pi, but its governing condition is not stated on this leaf. The author explicitly says that the p case should be expressible by a criterion and that f) still requires a suitable definition. "
"Whole source and both supplied halves were each viewed once, and every line, including C/H agreements, was compared with the ink. Twenty-four unique crops were then inspected. They were autocontrasted, LANCZOS-upscaled to 2200 pixels wide and lightly sharpened; none was recropped. Source coordinates are unrotated. The second box for the final clause encloses y2204–2354 so that both upper additions are complete; its first-pass image evidence is shared between the existing f_operer and f_end crops, with no new crop generated. "
"Line count 29 counts 22 main writing baselines, including the short continuation of convenablement at the foot, six separately positioned interlinear writing fragments, and the folio 101. The cancelled NB phrase shares one of the main baselines and is not counted again. All six additions, the cancelled passage, both complete c/d formula spans, all handwritten references 30/31, and folio 101 occur in exact-draft second-box readings. The final word convenablement continues on a short lower baseline; a TeX comment records this without supplying a hyphen. "
"The first line has no opening parenthesis before Ce; its later closing parenthesis is preserved without balancing it from expectation. The initial form is the short form tt, not an expanded word. Rat and hom have no stops. The first U_eta is unbarred; the c/d eta indices each have a visible bar. Item has a crossed t and no d bowl. The source reads the singular le groupe p-divisible, La dite with a visible division, and défini without an agreement e. Sous groupe has no separate hyphen. The only comma at the de E_k join is the one in the raised addition, and the field addition belongs between baseline sur and une. The f) reference literally has (31)., with separate period and comma. The n’ and pas trop additions have separate leaders and are live. "
"M1297, M1298 and M1299 are resolved to tt, K and T_ell; M1300 remains où|si. The struck Pour car. and the final >0 of its baseline formula remain doubtful because cancellation and replacement strokes obscure the letter/relation boundaries. Font choices for the same E/Q symbol, NB emphasis encoding, uncertainty alternatives that do not alter a primary reading, scan metadata, and H’s editorial notes are not independent lexical collation places. No OCR, external research, other-page witness reading, compilation, or blind second reading was used.")
check_events=[
 dict(statement_id='149.102.inner-action-to-abelianization',type='targeted proof check',who='reader A (/root/reader_a)',outcome="Conditional implication checked explicitly: suppose each element t of T acts on pi by an inner automorphism, so for some a_t in pi one has t(x)=a_t*x*a_t^{-1}. In the abelianization, [a_t*x*a_t^{-1}]=[a_t]+[x]-[a_t]=[x]. Equivalently, t(x)*x^{-1} is the commutator [a_t,x], which dies in pi/[pi,pi], and also dies in the profinite abelianization pi/closure([pi,pi]). Thus the induced T action on pi_ab is trivial. More generally, inner automorphisms act trivially on abelianization, so an outer action has a well-defined induced action there. This verifies the innerness-to-c) implication if that is the premise of the earlier condition b); b) itself was not read because it is outside this packet. No converse, geometric good-reduction criterion, or separate proof of pi_ab=H_1 is claimed."),
 dict(statement_id='149.102.sections-and-admissibility',type='carried as background without fault found',who='reader A (/root/reader_a)',outcome="The opening section/homomorphism assertion depends on a preceding condition not present in this packet. The H_1 identification and the admissibility discussion are retained as authorial/background material; the supplied leaf alone does not prove their geometric hypotheses or any equivalence among the listed conditions."),
 dict(statement_id='149.102.authorial-cautions',type='carried as background without fault found',who='reader A (/root/reader_a)',outcome="The p-divisible-group sentence is explicitly tentative (on doit pouvoir l’exprimer), and the final loufoque condition is explicitly left to be defined convenablement. These qualifications are preserved; neither passage is promoted to a proved criterion in this run.")
]
hand_observations=[
 dict(habit='Two t stems can share a crossbar while retaining separate hooked feet.',pages='102',evidence='opening_revision shows two separate uprights and feet; e_quitte has a local paired-t comparison. The lower ends of the opening form do not meet as a V.',witness_errors='H reads a capital H; C leaves tt versus a universal quantifier uncertain. The short form tt is retained at medium confidence.'),
 dict(habit='A capital serifed I followed by a tall crossed t can be mistaken for Idem.',pages='102',evidence='d_Idem crop has no d bowl; the second letter has a long crossbar across a straight upright.',witness_errors='C reads Idem where the source supports H’s Item.'),
 dict(habit='Short terminal e returns should not be expanded into unseen plural s or agreement e.',pages='102',evidence='d_plural has a single final e return on le, groupe and divisible; e_definie ends at a dotted i with a blank gap before par.',witness_errors='C supplies plural s in the d) phrase and a feminine e in définie.'),
 dict(habit='Insertion leaders can resemble punctuation or an extra word at the wrong baseline.',pages='102',evidence='e_subgroup has one raised comma after E_k, with the curved leader returning after ouvert; f_operer and f_end separate the raised pas trop from the preceding main-text line.',witness_errors='C adds a comma before the e) leader; H places the e) insertion incorrectly and treats the final upper words as par near opérer.'),
 dict(habit='An unusual pair of punctuation marks can be independently written and should remain literal.',pages='102',evidence='f_31 shows one round dot and one curved comma, separated from each other and from the preceding parenthesis.',witness_errors='C removes the period; H retains the source sequence (31).,')
]
notation_additions=[dict(written='two independent upright t stems with a shared crossbar and separate hooked feet',transcription='tt',evidence='149_scan102_opening_revision: two feet remain distinct and no lower V apex joins them; the short form is not expanded. Local comparison is the paired t in quitte on this leaf.')]
abbreviations=[
 dict(form='tt',expansion='tout (in tt scindage)'),dict(form='p.ex.',expansion='par exemple'),
 dict(form='pt',expansion='point'),dict(form='rat',expansion='rationnel'),dict(form='hom',expansion='homomorphisme'),
 dict(form='car.',expansion='caractéristique'),dict(form='NB',expansion='nota bene'),
 dict(form='i.e.',expansion='id est'),dict(form='alg.',expansion='algébrique')
]
unresolved=[
 dict(place='d_where_or_if',reading=r'\unsure{où|si}',alternatives='où preferred; si remains possible because the small initial form and detached upper stroke do not settle o/accent versus s/i-dot.',confidence='medium'),
 dict(place='d_cancelled_words',reading=r'\unsure{Pour car.}',alternatives='Pour car. preferred, but the strike and retracing hide internal letters and the abbreviation point; no expansion is supplied in the transcription.',confidence='low'),
 dict(place='d_cancelled_relation',reading=r'p\unsure{>0}',alternatives='p>0 preferred; the final sign and numeral are not independently separable from the cancellation and the raised replacement p stem.',confidence='low')
]
coverage=[]
def cov(d,place=None,reason=''):
 coverage.append(dict(diff_id=d,disposition='substantive' if place else 'macro/editorial only',change_place=place or '',reason=reason))
cov('D0560','opening_no_parenthesis','H supplies an opening parenthesis absent from the source. The scan102 label and H’s preceding note about a prior leaf are editorial, not source text.')
cov('D0561','opening_tt','The two-stem short form is tt; H gives H. Resolution of the supplied C mark is also recorded under M1297.')
cov('D0562','opening_inserted','Raised (ou un) and its attachment are directly visible; seul and extra parentheses are not a faithful transcription.')
cov('D0563','opening_scindage','The baseline word has the letters and g descender of scindage.')
cov('D0564','opening_U_eta','The first curve index is unbarred eta. The same aggregated row also includes rat, recorded separately at rat_without_stop.')
cov('D0565',reason='Both full witnesses give K after the slash; the diff row arises from C’s uncertainty alternative k and marker syntax. M1298 resolves K, without creating a substantive symbol change against either primary witness reading.')
cov('D0566','hom_short_form','The source short form is hom without a stop, not homom.')
cov('D0567','c_bar_eta','The barred index in c) is eta rather than xi.')
cov('D0568','d_Item','The source crossed stem supports Item against C’s Idem.')
cov('D0569','d_bar_eta','The barred index in d) is likewise eta.')
cov('D0570',reason='Both primary readings are T_ell. C’s alternative Z_ell and uncertainty marker produce this diff; M1299 resolves the primary reading without a separate collation change.')
cov('D0571',reason='The primary reading où is shared. C’s si alternative is retained as a genuine unresolved choice under M1300; uncertainty alone does not change the shared primary reading.')
cov('D0572','d_cancelled','The cancelled baseline has partially recoverable words and p>0; the doubtful portions remain explicitly marked.')
cov('D0573','d_replacement_comma','A separate source comma follows the upper ell=p>0 replacement.')
cov('D0574','d_le_groupe','The source supports singular le groupe, agreeing with H.')
cov('D0575','d_divisible','The source ending is singular divisible. TeX ldots versus the ellipsis character is only encoding; the final s is the substantive difference.')
cov('D0576','e_opening','The letters read En termes d’une rather than Etant donnée une.')
cov('D0577','e_La_dite','The source has a visible space between La and dite.')
cov('D0578','e_un','The baseline word is un, followed on the next line by sous groupe ouvert. The absence of a hyphen is separately recorded at e_sous_groupe; the raised de E_k and its attachment/commas are recorded at e_inserted_de.')
cov('D0579','e_au_besoin','Au besoin occurs after the insertion. H moves sous-groupe ouvert into this position; its correct earlier placement is covered by e_inserted_de.')
cov('D0580','e_no_toujours','No additional comma/toujours phrase occurs between i.e. and peut.')
cov('D0581','e_defini','The source ends at the dotted i of défini, agreeing with H; no agreement e is supplied.')
cov('D0582','e_field_insertion','No extra une occurs before the raised k; the baseline une follows the insertion attachment.')
cov('D0583','e_field_insertion','The upper insertion clearly includes ou between k, and sur.')
cov('D0584','e_field_insertion','Une is visibly on the main line before extension, after the insertion, not absent from that position.')
cov('D0585','f_opening','The source opens the clause (En termes; H’s Cette dernière dans is not present here.')
cov('D0586','f_31_stops','Both period and comma are independently written after (31), agreeing with H.')
cov('D0587','f_no_par','The small upper text belongs to the pas trop insertion on the next line; there is no par between opérer and E_k.')
cov('D0588','f_negative_condition','The main est/loufoque and the separate live n’ and pas trop additions are all visible.')
cov('D0589','f_caution','The parenthetical words read à définir convenablement, with the final word continuing on a short lower baseline.')
cov('D0590','folio101','The source folio101 is present. H’s note about earlier formulas is an editorial addition and is not transcribed as source prose.')
for entry in changes:
 entry['h']=entry['h'].replace("\\'", "'")
report=dict(scan=102,line_count=29,changes=changes,marks=marks,inventory=inventory,second_boxes=second,notes=notes,check_events=check_events,hand_observations=hand_observations,notation_additions=notation_additions,abbreviations=abbreviations,unresolved=unresolved,diff_coverage=coverage)
(page/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert {x['id'] for x in marks}=={x['id'] for x in packet['marks']}
assert {x['diff_id'] for x in coverage}=={x['diff_id'] for x in packet['differences']}
assert all((base/x['crop']).is_file() for x in changes+marks)
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in changes)
assert draft.count('{')==draft.count('}')
print(json.dumps({'changes':len(changes),'against_C':sum(x['against_c'] for x in changes),'against_H':sum(x['against_h'] for x in changes),'marks':len(marks),'diff_rows':len(coverage),'substantive_rows':sum(x['disposition']=='substantive' for x in coverage),'inventory':len(inventory),'second_boxes':len(second),'crops':len(manifest),'line_count':report['line_count'],'unresolved':len(unresolved)},ensure_ascii=False))
