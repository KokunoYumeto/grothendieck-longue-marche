from pathlib import Path
import json, csv

base = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out = base/'edition/reader_reports'
crops = {x['name']:x for x in json.loads((out/'145_scan003_crop_manifest.json').read_text())}
changes=[]
def change(n, place, C, H, final, ink, confidence, kind, cc, hc, marked, crop, errors, consequence=''):
    obj={'id':f's003-{n:02d}','place':place,'C':C,'H':H,'final':final,'ink':ink,'confidence':confidence,'kind':kind,'c_changed':cc,'h_changed':hc,'marked_in_H':marked,'crop':crops[crop]['crop'],'box':crops[crop]['box'],'error_category':errors,'math_consequence':consequence}
    changes.append(obj)

change(1,'opening line, group identification',r'\hat\pi_{0,3}=\pi',r'\hat\Pi_{0,3} = \hat\pi',r'\hat\Pi_{0,3}=\pi',
 'The indexed letter has a straight top bar and two long upright shafts, with a distinct hat above it. The short group name after the equality has no visible hat. Capital Π is proposed for the indexed letter; the unindexed abbreviation is retained as π.', 'high','misread symbol or index',True,True,'no','opening',[1])
change(2,'opening line, between commutant and sigma-zero',r'à',r'\struck{\ill{}} à',r'\deleted{\unsure{à}}',
 'A compact dark knot of crossed strokes occupies one word position. A small upper loop could belong to à, but the body is overinked. There is no spatially separate live à between the knot and σ₀. The proposed cancellation and underlying à both require root adjudication.', 'low','deletion state',True,True,'yes','opening',[7,9])
change(3,'upper-right oblique marginal note',r'\uline{NB} on aura \[ u(l_0)=\operatorname{int}\bigl(\underbrace{g_1l_1^{-\gamma}\rho^{-1}(h_1)}_{g_0}\bigr)\cdot l_0^{p} \]',r'NB On aura $u(l_0) = \mathrm{int}\bigl(g_1\, l_1\, \rho^{-1}(h_1)\bigr).\, l_0^{p}$, avec $g_0$ \uncertain{sous} le premier facteur',r'\uline{NB} on aura \[ u(l_0)=\operatorname{int}\bigl(\underbrace{g_1l_1^{-\gamma}\rho^{-1}(h_1)}_{g_0}\bigr)\cdot l_0^{p} \]',
 'The superscript after l₁ has a short minus and looped γ. The brace runs under the entire product g₁ l₁^{-γ} ρ^{-1}(h₁), and g₀ is written beneath its central cusp. NB is underlined; on starts with a small o.', 'high','omission',False,True,'yes','margin_u_l0',[1,3,6],'Restores the factor l₁^{-γ} in the conjugating element g₀.')
change(4,'short left marginal note beside determination of beta and gamma',r'\uline{\unsure{et $=$ pas|et ne pas|et non pas}} \uline{$u$}!',r'\ill{} à \ill{} près ! \ill{}',r'\uline{et $\bar m$ pas} \uline{$u$}!',
 'The crop shows plain et, then a detached upper bar over a lower two-curved m, then p with a descender, a small a, and final s. The lower u and exclamation mark are clear. Root supplied comparative identification of this barred m as the abbreviation for même; the local two-curved lower letter supports it.', 'high','abbreviation expanded or spelling modernised',True,True,'yes','margin_et_pas',[2,5,8])
change(5,'long left marginal note beside the second relation',r'NB. On doit en fait avoir $\unsure{\beta=\gamma|\beta\ne\gamma}$ (\unsure{passer} à $(\pi_{0,3})_{\unsure{\mathrm{ab}}}$)',r'NB. On doit \ill{} \ill{} \uncertain{$\beta$} \ill{} $\Pi_{0,3}$ \ill{}',r'NB. On doit en fait avoir $\unsure{\beta=\gamma|\beta\ne\gamma}$ (passer à $(\Pi_{0,3})_{\mathrm{ab}}$)',
 'NB., On, doit, en fait and avoir can be followed as connected cursive. The indexed group letter has two upright shafts and a top bar, supporting Π. The comparison sign remains unresolved: the short strokes are oblique and crowded by β and γ. Passer has a tall p and low connected a/ss/e/r; the subscript has a small a followed by a looped b.', 'medium','readable ink left as \\ill{}',True,True,'yes','margin_beta_gamma',[1,2,5])
change(6,'word introducing the definition of h-one',r'avec',r'où',r'avec',
 'A low joined a-v-e-c sequence is visible at the left of the definition. The terminal c is open; there is no initial round o followed by a u with grave.', 'high','misread word',False,True,'no','avec_definition',[2])
change(7,'punctuation after the definition of h-one',r'h_1=\sigma_0(g_1)^{-1}g_1.',r'h_1 = \sigma_0(g_1)^{-1}\, g_1',r'h_1=\sigma_0(g_1)^{-1}g_1',
 'The subscript 1 of the final g₁ is dark and distinct. No separate sentence dot is visible after it within the crop.', 'medium','text not on the page',True,False,'no','avec_definition',[9])
change(8,'rewritten second relation, first factor after the equals sign',r'l_\infty^\gamma',r'\struck{l_\infty} l_\infty^{\gamma}',r'l_\infty^\gamma',
 'There is one l-stem with the infinity subscript and γ exponent. The dark crossing at its base meets the equals sign; no spatially separate earlier l∞ appears. Retain C without a duplicated deleted factor.', 'high','text not on the page',False,True,'no','second_relation_rewrite',[7,9])
change(9,'rewritten second relation, exponent immediately before beta on l-zero',r'l_0^\beta',r'l_0^{\beta}',r'l_0^{\deleted{\unsure{\gamma|\alpha}}\beta}',
 'A small black crossed cluster stands at exponent height immediately left of the clear β. Its top is looped, and a darker horizontal cancellation passes through it. γ or α is plausible; the original symbol is not fully recoverable. Both witnesses omit this inscription.', 'low','omission',True,True,'no','second_relation_rewrite',[1,3,7])
change(10,'prose introducing relation one-prime',r'et en portant dans la première relation, celle-ci peut se récrire',r'et en portant dans la première relation celle-ci prend la forme',r'et en portant dans la première relation, celle-ci peut se récrire',
 'A dark comma follows relation at the right end of the first line. In the following line, peut begins with a long p descender and ends in t; a small se follows. Récrire has the accented initial ré and repeated r/i strokes. The space and letter sequence do not support prend la forme.', 'high','misread word',False,True,'no','peut_se_recrire',[2])
change(11,'NB paragraph, replacement of h-one',r'en $h_1\prime=l_\infty^{-\mu}h_1l_1^\mu$,',r'par \[ h\prime_1 = l_\infty^{-\mu}\, h_1\, l_1^{\mu} \]',r'en $h_1\prime=l_\infty^{-\mu}h_1l_1^\mu$,',
 'The line starts with a short two-humped en; there is no tall p stem for par. A comma is visible after the final l₁^μ in the half-page reading. Prime placement in h′₁ is only typographic.', 'high','misread word',False,True,'no','remplace_en',[2])
change(12,'NB paragraph, clause before the last displayed formula',r'en lui appliquant',r'\uncertain{avec}',r'en lui appliquant',
 'Three word groups are visible. En is low and joined; lui has a tall looped l; appliquant has paired long p descenders and the final connected ant. The crop cannot be read as the single word avec.', 'high','misread word',False,True,'yes','en_lui_appliquant',[2])
change(13,'last display, overwritten h-one in the first inner automorphism',r'\operatorname{int}(\deleted{\unsure{h_1}}h_1\prime)',r'\mathrm{int}(\uncertain{h\prime_1})',r'\operatorname{int}(\deleted{\unsure{h_1}}h_1\prime)',
 'The first argument is overwritten. A live h with a small 1 and a distinct high prime can be read, while additional lighter and crossed strokes remain under it. The underlying h₁ remains doubtful; not every letter under the overwrite is plain.', 'medium','deletion state',False,True,'yes','final_formula',[7])
change(14,'last display, parentheses around l-one to the p',r'\operatorname{int}(\deleted{\unsure{h_1}}h_1\prime)l_1^{p}',r'\mathrm{int}(\uncertain{h\prime_1})(l_1^{p})',r'\operatorname{int}(\deleted{\unsure{h_1}}h_1\prime)(l_1^{p})',
 'A terminal closing curve after l₁^p is clear. The initial curve close to the l-stem is read as its matching opening parenthesis, as in H; because the two strokes touch, root should confirm this medium-confidence departure from C.', 'medium','omission',True,False,'no','final_formula',[3])
change(15,'last display, struck factor before l-infinity',r'\deleted{\unsure{l_1^\mu}}',r'\struck{\ill{}}',r'\deleted{\unsure{l_1^\mu}}',
 'A short crossed factor is present. Its left tall stroke resembles l; a small lower stroke and crowded right upper strokes permit l₁^μ, but the cancellation prevents a full secure recovery. Retain C’s doubt rather than turning the whole factor into an unqualified illegible.', 'low','readable ink left as \\ill{}',False,True,'yes','final_formula',[5,7])
change(16,'last display, small superscript on rho',r'\rho^{\unsure{1|-1}}',r'\rho^{-1}',r'\rho^{\unsure{\deleted{-1}|-1|1}}',
 'The superscript is a tiny black angular overwrite rather than a clean upright 1 or a clean minus-one. Its shape may be a cancellation of −1. This deletion state is proposed only as the first uncertain reading; live −1 and live 1 remain alternatives. Root adjudication is required.', 'low','deletion state',True,True,'yes','final_formula',[1,7],'A live inverse on ρ differs from a cancelled inverse; the corrected relation cannot be settled from the expected algebra.')
change(17,'parenthetical equality after the last display, cancelled additive term',r'\uline{$\gamma\prime=\gamma\deleted{\unsure{+2\mu|+\mu}}$}',r'\uncertain{(i.e. $\gamma\prime = \gamma \ill{}$)}',r'\uline{$\gamma\prime=\gamma\deleted{\unsure{+2\mu|+\mu}}$}',
 'The live γ′ = γ is distinct. A dense cancellation follows γ: a cross-like sign and a final μ-like form are visible, but the intervening 2 is not securely separable. The underline continues under the entire equality and the cancelled term.', 'low','deletion state',False,True,'yes','final_corrections',[5,7])
change(18,'closing prose between the parenthetical equality and la relation',r'et on a la relation',r'et on a \uncertain{aussi} la relation',r'et on a la relation',
 'Et, the low on, and a small filled a precede la relation. There is no further word group that could contain aussi.', 'high','text not on the page',False,True,'yes','final_corrections',[9])
change(19,'closing prose immediately before the reference to relation two',r'correspondante $(2)_2$',r'correspondante (2),',r'correspondante à $(2)_2$',
 'Between correspondante and the opening parenthesis are a short grave stroke and a small dark a-shaped body. This is proposed as à, omitted by both witnesses; its compact form merits root confirmation.', 'medium','omission',True,True,'no','final_corrections',[3])
change(20,'closing reference to relation two',r'$(2)_2$',r'(2),',r'$(2)_2$',
 'A small 2 is written below and to the right of the closing parenthesis. It is not a comma: the upper turn and lower diagonal are visible. Retain the author’s doubled-looking reference without mathematical normalization.', 'high','misread symbol or index',False,True,'no','final_corrections',[1])
change(21,'closing beta-prime equality, overwritten initial beta',r'\deleted{\unsure{\beta}}\beta\prime=\beta',r'\beta\prime = \beta',r'\deleted{\unsure{\beta}}\beta\prime=\beta',
 'The initial β is overwritten by dark angular loops, and a clear prime stands to the right. An earlier β is plausible but its full outline is not plain beneath the cancellation. C’s doubt is retained; H omits the overwritten state.', 'medium','deletion state',False,True,'no','final_corrections',[7])

decisions=[]
def decision(id, choice, reading, ink, crop, confidence):
    decisions.append({'id':id,'decision':choice,'reading':reading,'ink':ink,'crop':crops[crop]['crop'],'box':crops[crop]['box'],'confidence':confidence})
decision('M0759','other',r'et $\bar m$ pas','A detached horizontal bar lies over a lower two-curved m. Plain et and pas surround it. Root’s comparative notation update identifies barred m as même; the local letter agrees.','margin_et_pas','high')
decision('M0760','undecided',r'\unsure{\beta=\gamma|\beta\ne\gamma}','The short comparison strokes are slanted and crowded. Their precise crossing does not separate = from ≠ securely. The author’s On doit en fait avoir is preserved without using the expected abelianized relation to decide the strokes.','margin_beta_gamma','low')
decision('M0761','first','passer','A tall p is followed by low joined a, double-s turns, e and a final r-like upstroke. The word is sufficiently recoverable, although its compressed middle is less distinct than the initial p.','margin_beta_gamma','medium')
decision('M0762','first',r'\mathrm{ab}','A small a-shaped stroke and a narrow looped b sit below the closing parenthesis of the group name. The letters are compressed but recognizable as ab.','margin_beta_gamma','medium')
decision('M0763','undecided',r'\unsure{\gamma\prime|\gamma-\mu}','The exponent is thick and partly overwritten. A looped gamma-like stroke and a high right stroke can be read as γ′, but the remnant is also compatible with γ−μ. Neither is separated sufficiently by the ink.','final_formula','low')
decision('M0764','other',r'\unsure{\deleted{-1}|-1|1}','The small angular black superscript may be a cancelled −1. No clean live digit is visible, so deletion of −1 is added as an uncertain first reading, with live −1 and 1 retained as alternatives.','final_formula','low')
decisions[-1]['decision']='undecided'

doubts=[
 {'place':'opening, word between commutant and sigma-zero','reading':r'\deleted{\unsure{à}}','alternatives':['a live overwritten à','a cancelled illegible word with no surviving à'],'confidence':'low','reason':'Dense crossed knot; neither the underlying letter nor cancellation state can be fully distinguished.'},
 {'place':'first display, argument of u','reading':r'u(l_{\unsure{1|0}})','alternatives':['1','0'],'confidence':'low','reason':'The index is an opaque teardrop of ink. The target l₁^p suggests 1, but that is not a recovery of the individual strokes.'},
 {'place':'long left marginal note','reading':r'\unsure{\beta=\gamma|\beta\ne\gamma}','alternatives':[r'\beta=\gamma',r'\beta\ne\gamma'],'confidence':'low','reason':'The comparison sign is oblique and crowded by adjacent letters.'},
 {'place':'rewritten second relation, crossed exponent before beta','reading':r'\deleted{\unsure{\gamma|\alpha}}','alternatives':[r'\gamma',r'\alpha','another overwritten exponent'],'confidence':'low','reason':'The crossed loop has no fully recoverable outline; omitted by both witnesses.'},
 {'place':'last display, underlying first argument of int','reading':r'\deleted{\unsure{h_1}}','alternatives':['h₁','another overwritten argument'],'confidence':'low','reason':'Additional strokes under the live h₁′ are present, but every letter is not plain.'},
 {'place':'last display, cancelled factor before l-infinity','reading':r'\deleted{\unsure{l_1^\mu}}','alternatives':[r'l_1^\mu','another cancelled factor'],'confidence':'low','reason':'The cancellation crosses the small index and exponent; do not resolve C’s struck-text doubt.'},
 {'place':'last display, exponent of l-infinity','reading':r'\unsure{\gamma\prime|\gamma-\mu}','alternatives':[r'\gamma\prime',r'\gamma-\mu'],'confidence':'low','reason':'Thick overwrite and insufficient separation of high strokes.'},
 {'place':'last display, rho superscript','reading':r'\unsure{\deleted{-1}|-1|1}','alternatives':[r'\deleted{-1}','-1','1'],'confidence':'low','reason':'The angular overwritten superscript may be a cancellation, but its deletion state is not secure.'},
 {'place':'parenthetical gamma-prime equality, cancelled term','reading':r'\deleted{\unsure{+2\mu|+\mu}}','alternatives':[r'+2\mu',r'+\mu'],'confidence':'low','reason':'The possible 2 cannot be separated from the diagonal cancellation.'},
 {'place':'closing beta-prime equality, underlying symbol','reading':r'\deleted{\unsure{\beta}}','alternatives':[r'\beta','another overwritten symbol'],'confidence':'low','reason':'The live prime is clear, but the earlier complete β outline is not recoverable.'}
]

inventory=[]
def item(element,kind,position,words,box):
    inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'box':box,'sheet_kind':'handwritten mathematical notes','hand':'one apparent principal cursive hand; no firm attribution beyond this page','transcribed':'yes'})
item('T01','text','top, three lines','Les autom. ... sont donnés par',[175,89,1290,307])
item('I01','insertion','above opening line, between autom. and de','à lacets',[432,42,579,118])
item('D01','deletion','opening line, between commutant and sigma-zero',r'\deleted{\unsure{à}}',[1141,87,1180,127])
item('F01','display','first main display','u(l₁) = int(g₁) l₁^p',[440,300,891,381])
item('F02','display','second main display, with underbrace label','u(l∞) = int(σ₀(g₁)) l∞^p; g∞',[446,382,965,506])
item('MN01','margin note','upper right, oblique, two lines and brace label','NB on aura; u(l₀); g₀',[1060,30,1533,475])
item('T02','text','parameter paragraph, three lines','avec g₁ ∈ π mod L₁ ... déterminés par g₁,p',[195,477,1408,755])
item('MN02','margin note','left of parameter paragraph, oblique, two lines',r'et $\bar m$ pas; u!',[33,649,210,826])
item('F03','display','boxed relation (1), number at left','(1) l∞^p · int(h₁)(l₁^p) ... = 1',[225,737,1453,922])
item('T03','text','left before second boxed relation','et',[216,963,280,1012])
item('F04','display','boxed relation (2), number at left','(2) ρ(h₁)(l∞^{-γ} · h₁l₁^{-γ}) ... = l₀^β',[298,886,1308,1100])
item('MN03','margin note','left, oblique, about four lines','NB. On doit en fait avoir β ... γ (passer à (Π₀,₃)ab)',[30,1003,356,1496])
item('T04','text','left of h-one definition','avec',[266,1190,404,1244])
item('F05','display','definition below relation (2)','h₁ = σ₀(g₁)^{-1} g₁',[677,1111,1120,1238])
item('T05','text','line before rewritten relation','La deuxième relation s’écrit aussi',[267,1238,1253,1355])
item('F06','display','rewritten relation (2), unboxed','h₁l₁^{-γ}ρ^{-1}(h₁) = l∞^γρ(h₁)^{-1}l₀^β',[315,1318,985,1475])
item('D02','deletion','superscript on final l-zero in rewritten relation',r'\deleted{\unsure{\gamma|\alpha}}',[872,1319,909,1356])
item('T06','text','two lines between rewritten (2) and (1-prime)','et en portant ... celle-ci peut se récrire',[278,1370,1505,1610])
item('F07','display','boxed relation (1-prime), number at left',r'(1\prime) l∞^p · int(h₁)(l₁^p) ... = 1',[194,1561,1389,1782])
item('T07','text','NB paragraph, three slanting lines','NB Si on change g₁ ... en lui appliquant int(l∞^{-μ}) :',[295,1731,1455,1999])
item('F08','display','last unboxed display, heavily corrected','l∞^p · int(h₁′)(l₁^p) ... = 1',[441,1911,1455,2057])
item('D03','deletion','first int argument of last display',r'\deleted{\unsure{h_1}}',[644,1960,729,2036])
item('D04','deletion','second int argument of last display, before l-infinity',r'\deleted{\unsure{l_1^\mu}}',[985,1940,1040,1999])
item('D05','deletion','rho superscript in last display, cancellation state uncertain',r'\unsure{\deleted{-1}|-1|1}',[1140,1938,1178,1960])
item('T08','text','closing two lines, with underlined parenthetical equality','(i.e. γ′ = γ ...) et on a la relation correspondante à (2)₂ avec β′ = β.',[309,2006,1455,2203])
item('D06','deletion','cancelled additive term after gamma in closing equality',r'\deleted{\unsure{+2\mu|+\mu}}',[623,2057,710,2122])
item('D07','deletion','overwritten beta in closing equality',r'\deleted{\unsure{\beta}}',[1001,2083,1050,2169])
item('P01','text','lower-left page corner','2',[53,2120,112,2185])

second_boxes=[]
def sb(n,kind,coords,reading): second_boxes.append({'box':f'B{n:02d}','kind':kind,'coords':coords,'reading':reading})
sb(1,'insertion; uncertain deletion; group-letter disagreement',[165,40,1300,162],r'Les autom. \inserted{à lacets} de $\hat\Pi_{0,3}=\pi$ commutant \deleted{\unsure{à}} $\sigma_0$,')
sb(2,'proposed doubt in overwritten index; whole formula',[440,300,891,381],r'u(l_{\unsure{1|0}})=\operatorname{int}(g_1)l_1^p')
sb(3,'entire upper-right marginal note',[1060,30,1533,475],r'\uline{NB} on aura $u(l_0)=\operatorname{int}(\underbrace{g_1l_1^{-\gamma}\rho^{-1}(h_1)}_{g_0})\cdot l_0^p$')
sb(4,'entire short left marginal note; resolved C mark',[33,649,210,826],r'\uline{et $\bar m$ pas} \uline{$u$}!')
sb(5,'handwritten formula number and complete numbered display',[225,737,1453,922],r'(1)\quad\boxed{l_\infty^p\cdot\operatorname{int}(h_1)(l_1^p)\cdot\operatorname{int}(h_1l_1^{-\gamma}\rho^{-1}(h_1))(l_0^p)=1}')
sb(6,'handwritten formula number and complete numbered display',[216,886,1308,1100],r'\text{et}\quad(2)\quad\boxed{\rho(h_1)(l_\infty^{-\gamma}\cdot h_1l_1^{-\gamma})\rho^{-1}(h_1)=l_0^\beta}')
sb(7,'entire left marginal note; unresolved and resolved C marks',[30,1003,356,1496],r'NB. On doit en fait avoir $\unsure{\beta=\gamma|\beta\ne\gamma}$ (passer à $(\Pi_{0,3})_{\mathrm{ab}}$)')
sb(8,'lexical disagreement avec/où and omitted sentence dot',[266,1110,1130,1250],r'avec $h_1=\sigma_0(g_1)^{-1}g_1$')
sb(9,'new cancelled exponent; disputed duplicated factor; whole formula',[315,1318,985,1475],r'h_1l_1^{-\gamma}\rho^{-1}(h_1)=l_\infty^\gamma\rho(h_1)^{-1}l_0^{\deleted{\unsure{\gamma|\alpha}}\beta}')
sb(10,'word disagreement; punctuation',[278,1370,1505,1610],r'et en portant dans la première relation, celle-ci peut se récrire')
sb(11,'handwritten formula number and complete numbered display',[194,1561,1389,1782],r'(1\prime)\quad\boxed{l_\infty^p\cdot\operatorname{int}(h_1)(l_1^p)\cdot\operatorname{int}(l_\infty^\gamma\rho(h_1)^{-1})(l_0^p)=1}')
sb(12,'word disagreement en/par',[293,1863,590,1952],r'en $h_1\prime=$')
sb(13,'word disagreement en lui appliquant/avec',[315,1870,1048,2001],r'en lui appliquant $\operatorname{int}(l_\infty^{-\mu})$ :')
sb(14,'all cancellations and C/proposed doubts in last display; whole formula',[441,1911,1455,2057],r'l_\infty^p\cdot\operatorname{int}(\deleted{\unsure{h_1}}h_1\prime)(l_1^p)\cdot\operatorname{int}(\deleted{\unsure{l_1^\mu}}l_\infty^{\unsure{\gamma\prime|\gamma-\mu}}\rho^{\unsure{\deleted{-1}|-1|1}}({h_1\prime}^{-1}))(l_0^p)=1')
sb(15,'closing cancellations; word disagreement; omitted à; handwritten reference',[309,2006,1455,2203],r'(\uline{i.e.} \uline{$\gamma\prime=\gamma\deleted{\unsure{+2\mu|+\mu}}$}) et on a la relation correspondante à $(2)_2$ avec $\deleted{\unsure{\beta}}\beta\prime=\beta$.')
sb(16,'handwritten manuscript page number',[53,2120,112,2185],r'\mspage{2}')
sb(17,'complete second defining display, including numeric subscripts and brace label',[446,382,965,506],r'u(l_\infty)=\operatorname{int}(\underbrace{\sigma_0(g_1)}_{g_\infty})l_\infty^p')
sb(18,'complete parameter paragraph, including all numeric subscripts',[195,477,1408,755],r'avec $g_1\in\pi\bmod L_1$, $p\in\hat{\mathbb Z}^{*}$ satisfaisant la condition (où $\beta,\gamma\in\hat{\mathbb Z}$ sont uniquement déterminés par $g_1,p$)')
sb(19,'complete lower NB paragraph, including numeric subscripts and formula reference',[295,1731,1455,1999],r'\uline{NB} Si on change $g_1$ en $g_1\prime=g_1l_1^\mu$, $h_1$ est remplacé en $h_1\prime=l_\infty^{-\mu}h_1l_1^\mu$, et la relation $(1\prime)$ donne, en lui appliquant $\operatorname{int}(l_\infty^{-\mu})$ :')

substantive={6:3,9:4,18:5,20:7,21:3,24:8,27:10,28:10,35:11,39:11,40:12,42:13,43:13,44:14,45:14,46:15,49:16,50:17,51:18,52:20,53:21}
special={
 6:'The token alignment relocates the upper-right marginal note; its content is covered by s003-03.',
 18:'This long alignment combines the long marginal note (s003-05) and avec/où (s003-06).',
 20:'The real terminal-dot disagreement is s003-07. H’s note about the index is editorial, but its observed overwritten ink is independently retained as a doubt in F01/B02.',
 21:'Relocated marginal-note material. Content is covered by s003-03, s003-04 and s003-05; H’s comments about placement are editorial.',
 32:'Prime attached to g versus after its subscript: same g-one-prime.',33:'Prime placement after/before subscript is typographic.',
 36:'Prime placement after/before subscript is typographic; the en/par disagreement is s003-11.',
 47:'Only unresolved alternative notation: H’s gamma-minus-mu is retained as an alternative in M0763; no alternative is newly selected.',
 48:'TeX thin-space punctuation adjacent to the unresolved exponent; no source comma.',
 54:'C’s manuscript page 2 is preserved as P01/B16. H’s closing description of corrections is editorial and not part of the manuscript.'
}
diff_coverage=[]
rows=list(csv.DictReader((base/'packets/145_scan003/differences.tsv').open(),delimiter='\t'))
for i,row in enumerate(rows,1):
    if i in substantive:
        o={'row':i,'status':'substantive','change_id':f's003-{substantive[i]:02d}'}
        if i in special:o['explanation']=special[i]
    else:
        o={'row':i,'status':'macro/editorial','explanation':special.get(i,'Display/aligned boundaries, TeX thin spacing, or token separation; no independent difference in the source inscription.')}
    diff_coverage.append(o)

report={
 'scan':3,'reader':'/root/reader_a','lines_read':34,
 'layout':'One upright handwritten sheet, manuscript page 2 at lower left. Three opening prose lines, two defining displays with one underbrace label, a three-line parameter paragraph, boxed numbered relations (1) and (2), an h₁ definition, a rewritten relation, two linking prose lines, boxed (1′), and a three-line NB paragraph followed by a corrected display and two closing prose lines. There are three separate oblique marginal notes, one interlinear insertion, several overwritten/cancelled symbols, and no independent diagram or drawing. The line count includes the insertion, marginal-note lines, underbrace labels, and manuscript page number.',
 'changes':changes,'decisions':decisions,'doubts':doubts,'inventory':inventory,'second_boxes':second_boxes,
 'notation':[
  {'observation':r'The overbar over a two-curved m in the short left margin is the abbreviation $\bar m$ for même.','observed_places':['MN02'],'qualification':'Comparative identification was supplied by root after it reviewed this same crop; the local overbar and double-curved lower letter support it.'},
  {'observation':'An indexed capital Π and an unindexed π are used in the opening group identification; the indexed marginal group again has the tall two-shaft Π form.','observed_places':['T01','MN03'],'qualification':'No uniformity beyond this page is asserted; the second opening π has no visible hat.'},
  {'observation':'Conjugation is written int(·), sometimes followed by a parenthesized target and sometimes directly by the target generator.','observed_places':['F01','F02','F03','F04','F07','F08','MN01'],'qualification':'The exact touching parentheses in F08 remain a medium-confidence reading.'},
  {'observation':'Underbraces name g∞ and g₀ beneath the conjugating expressions.','observed_places':['F02','MN01'],'qualification':'The g₀ brace includes the full three-factor product.'},
  {'observation':'The closing reference is written (2)₂.','observed_places':['T08'],'qualification':'Preserved literally; no normalization of the apparent duplicated 2.'}
 ],
 'hand':[
  {'habit':'Short cursive en has very low joined strokes and can resemble a single horizontal wave.','affected_places':['T07: remplacé en','T07: en lui appliquant'],'universal_on_page':'Observed consistently in these clauses; not claimed for every en.','witness_misreadings':'H reads par in the first clause and avec for the longer second clause.'},
  {'habit':'The gamma has a long loop and can resemble a rounded delta or a crossed flourish, especially in small exponents.','affected_places':['F03','F04','F06','F07','F08','MN01','MN03'],'universal_on_page':'Broad pattern recurring on this page; crowded corrections remain unresolved.','witness_misreadings':'C and H disagree about the small corrected final exponent; no automatic replacement is made.'},
  {'habit':'Letters and exponents are sometimes overwritten in place, without a spatially separate replacement.','affected_places':['T01 before σ₀','F01 argument index','F06 exponent before β','F08 h₁ and ρ superscript','T08 β′'],'universal_on_page':'Observed at named places only.','witness_misreadings':'Both witnesses omit the exponent before β; H invents a separate deleted l∞ in F06 and omits some final overwrite states.'},
  {'habit':'A small à can have a filled a-shaped body below a detached grave.','affected_places':['T08 before (2)₂'],'universal_on_page':'Single proposed occurrence; medium confidence.','witness_misreadings':'Both witnesses omit this proposed word.'},
  {'habit':'The abbreviation barred m has a detached upper stroke and a lower double-curved letter.','affected_places':['MN02'],'universal_on_page':'Only one occurrence on this page.','witness_misreadings':'C offers equality sign / ne / non; H leaves fragments illegible.'}
 ],
 'abbreviations':[
  {'form':'autom.','expansion':'automorphismes','place':'opening'},
  {'form':'int','expansion':'automorphisme intérieur / conjugaison','place':'throughout displayed formulas'},
  {'form':'mod','expansion':'modulo','place':'parameter paragraph'},
  {'form':'NB','expansion':'nota bene','place':'upper-right note, long left note, lower NB paragraph'},
  {'form':r'$\bar m$','expansion':'même','place':'short left marginal note'},
  {'form':'ab','expansion':'abélianisé / abélianisation','place':'long left marginal note'},
  {'form':'i.e.','expansion':'id est','place':'closing parenthetical equality'}
 ],
 'notes':[
  'The page describes, in the author’s formulation, automorphisms à lacets of the indicated completed fundamental group that commute with σ₀ and commute externally with ρ. It parameterizes their images of l₁ and l∞ by g₁ and p, states two boxed conditions on h₁ and the exponents β and γ, and defines h₁ = σ₀(g₁)^{-1}g₁. These are transcribed claims, not independently established results in this report.',
  'The upper-right marginal note supplies the image of l₀ and names its conjugating element g₀. The short left note reads et barred-m pas u!, with barred m identified as the abbreviation même. The longer left note states On doit en fait avoir followed by the unresolved β/γ comparison and an instruction to pass to the abelianization. The wording On doit en fait avoir is retained; no additional authorial question mark or explicit doubt phrase was confidently recovered.',
  'The author rewrites the second relation and substitutes it in the first to obtain (1′). In the final NB paragraph he changes the representative g₁ to g₁l₁^μ and records the corresponding h₁′. The heavily corrected last display and underlined equality lead to the surviving assertion γ′ = γ, with a cancelled additive term, and the final β′ = β. No targeted proof check, independent re-proof, or formal computation was completed.',
  'The expected transformation of the final conjugating term motivated attention to the small ρ superscript, but was not used to supply or erase any symbol. The ink permits a cancelled −1 as well as live superscript alternatives. Root must adjudicate this along with the small exponent before β, the opening overwritten word, and the touching parentheses in the last display.',
  'C’s four explicit cancelled items in the final display and closing equalities have all been individually inspected: underlying h₁, the factor proposed as l₁^μ, the term proposed as +2μ or +μ, and underlying β. Their doubts remain because not every struck letter is plain. The à lacets insertion is above the first line and attaches after autom. Two further possible cancellation sites are recorded: the opening overwritten word and the final ρ exponent. A clear omitted cancellation stands before β in the unboxed rewritten relation.',
  'The manuscript page number is 2. No date was found. The reference (2)₂ and the unusual phrase remplacé en are preserved as written. No clear mathematical authorial slip is asserted solely from the transcription. No other page, external publication, OCR, or recognition software was used.'
 ],
 'check_events':[],
 'diff_coverage':diff_coverage
}

for el in report['inventory']:
    el['sheet_kind']='text'
    el['hand']='his hand'
for ch in report['changes']:
    if ch['kind'].startswith('readable ink left as'):
        ch['kind']='readable ink left as '+chr(92)+'ill{}'
def exact_primes(obj):
    if isinstance(obj,str): return obj.replace(chr(92)+'prime',"'")
    if isinstance(obj,list): return [exact_primes(x) for x in obj]
    if isinstance(obj,dict): return {k:exact_primes(v) for k,v in obj.items()}
    return obj
report=exact_primes(report)
(out/'145_scan003.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(out/'145_scan003.json'),'changes':len(changes),'decisions':len(decisions),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second_boxes),'diff_rows':len(diff_coverage),'crops':len(crops)},indent=2))
