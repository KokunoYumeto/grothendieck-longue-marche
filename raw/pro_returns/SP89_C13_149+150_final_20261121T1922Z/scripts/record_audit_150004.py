"""Serialize the main reader's explicit, visually adjudicated decisions."""
from pathlib import Path
import json, subprocess, sys
W=Path(__file__).resolve().parents[1]; page='150_scan004'
C={r['box']:r for r in json.loads((W/'second'/f'{page}_comparison.json').read_text())}
R=json.loads((W/'reports'/page/'report.json').read_text())
rows=[]; E={'source_replacements':[],'report_updates':[],'report_appends':{}}
def decision(box,evidence,outcome,changes=(),crop=None):
    final=C[box]['first']
    for a,b in changes:
        assert a in final,(box,a)
        final=final.replace(a,b)
    d=dict(box=box,decision='revise' if changes else 'retain',evidence=evidence,outcome=outcome)
    if changes:d['final']=final
    if crop:d['crop']=crop
    rows.append(d)
def replace(a,b): E['source_replacements'].append(dict(old=a,new=b,count=1))
def update(collection,key,value,**fields):
    assert sum(x.get(key)==value for x in R[collection])==1,(collection,value)
    E['report_updates'].append(dict(collection=collection,match={key:value},set=fields))
def change(id,**fields):update('changes','id',id,**fields)
def doubt(place,reading,alternatives,reason,confidence='low'):
    fields=dict(reading=reading,alternatives=alternatives,reason=reason,confidence=confidence)
    if any(x['place']==place for x in R['doubts']):update('doubts','place',place,**fields)
    else:E['report_appends'].setdefault('doubts',[]).append(dict(place=place,**fields))
def newchange(box,id,place,c,h,final,evidence,kind,category,confidence='medium',consequential=False):
    coords=next(x['xyxy'] for x in R['audit_boxes'] if x['box']==box)
    E['report_appends'].setdefault('changes',[]).append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{page}_second_{box}.png',box=coords,confidence=confidence,kind=kind,against_c=True,against_h=True,marked_in_h=False,consequential=consequential,error_category=category))

# Every differing crop has been inspected by the main reader; wider original
# crops resolve the three explicitly noted scope limitations.
oldcancel=r'\unsure{X_\varphi\text{ est fidèle}}'
newcancel=r'\unsure{X_\varphi\text{ est fidèle}|X_j\text{ est fermé}}'
indexmark=r'\unsure{\underline{j}|\underset{\sim}{j}|j}'
oldpre=r'\unsure{une|\deleted{une}} : une relation'
newpre=r"$=$ : \unsure{d'une|une} relation"
oldparent=r'\unsure{($\forall i,j$, $X_i^*=X_i$)|\deleted{(telle que $X_i^*=X_i$)}}'
newparent=r'\unsure{($\forall i$, i.e. $\unsure{X_i^*|\overline{X_i^*}}=X_i$)|(i.e. $\overline{X_i^*}=X_i$)}'
olddef="3°) $\\forall i$, $X_i^*\\ne\\phi$\n``déf\\unsure{''} $X_i\\setminus\\bigcup_{j<i}X_j$"
newdef=r'3°) $\forall i$, $\underset{\substack{\Vert\,\mathrm{déf}\\X_i\setminus\bigcup_{j<i}X_j}}{X_i^*}\ne\phi$'
newdiagram=r'''\margin{\diagram{\begin{tikzpicture}[x=0.65cm,y=0.65cm]
\node at (0,0) {$\overline{\unsure{J|I}}$};
\node at (1,0) {$\unsure{J|I}$};
\draw (1.65,-0.65)--(1.65,0.8);
\node at (2.6,0) {$y<x$};
\node at (2.18,1.45) {$\unsure{J|\supset}$};
\node at (2.18,0.8) {$\unsure{\Downarrow|\notin}$};
\node at (3.03,0.8) {$\in J$};
\draw (1.94,-0.4)--(2.09,-0.4);
\node at (5.2,0) {$x\in J$};
\end{tikzpicture}}}'''

decision('B01','Both bowls of the folio 3 are visible.','Retain the folio macro; the second reading omits only that wrapper.')
decision('B02','After plus the short group has f, a tall t, and a terminal e; separate o/r bodies cannot be traced. The raised pour/phi group, continue, and the underlined surjection/ouverte remain supported.','Prefer the abbreviated fte, with forte retained as an alternative; keep the existing revision states.', [('Condition plus forte',r'Condition plus \unsure{fte|forte}')])
decision('B03','The cancelled X-subscript group and f-opening survive, but the strike hides the medial and final letters. The vertical pairs align with the two sides of the first equality.','Retain the formulas and preferred cancelled wording while adding the independently proposed fermé reading as a local alternative.',[(oldcancel,newcancel)])
decision('B04','The line below loc. finie curves continuously into its attachment. The separate emphasis under the index-order word begins after pré, beneath ordonné. The application word has a long p/l sequence.','Retain the insertion and application; restrict the independent underline to ordonné.',[(r'\uline{préordonné}',r'pré\uline{ordonné}')])
decision('B05','The overwritten numeral still admits 2/4. Quotient and the final t are visible. The two L-shaped capitals also admit rounded U. Both close parentheses are independent ink.','Keep the numeral, equivalence and literal punctuation; qualify both L/U capitals without changing the preferred L.',[(r'X_L^*',r'X_{\unsure{L|U}}^*'),(r'\Rightarrow L\text{ ouvert}',r'\Rightarrow\unsure{L|U}\text{ ouvert}')])
decision('B06','The small degree label after i.e. has an ambiguous curved upper stroke and foot. The double upward arrow is distinct.','Keep 1° preferred and add 2° as a local uncertainty.',[('i.e. 1°',r'i.e. \unsure{1°|2°}')])
decision('B07','Hooked j descenders distinguish the written indices. Two crossed t strokes support tt. A separate short wavy stroke lies below the lower union-index j.','Preserve the literal index mismatch and restore the lower mark, uncertain between underline and tilde-like stroke.',[(r'\bigcup_{j\leq i}',r'\bigcup_{'+indexmark+r'\leq i}')])
decision('B08','The surj ending has no independent stop; the empty-set sign has the phi loop and stem. Two slanted rules are already represented by the adjacent first-reading figure.','Retain, without duplicating the separate rules.')
decision('B09','The second numeral has a level upper stroke and angular descending leg, favoring 7 over 3; the preceding comma does not bar I. After the last formula there is one dash and two points.','Prefer 7° with alternatives, retain relat uncertainty, and record the visible dash/point sequence instead of supplying three points.',[(r'\unsure{3°|7°}',r'\unsure{7°|3°|2°}'),(r'\ldots',r'$\unsure{\mathinner{-\cdot\cdot}|\ldots}$')])
decision('B10','The precolon item consists of two separate horizontal bars, with no letter bodies. After the colon a high d-like loop and apostrophe precede une, though the cramped join remains uncertain.','Read the equality sign and prefer d’une, preserving une as an alternative.',[(oldpre,newpre)])
decision('B11','The crossed phrase has a c/l group and the later soient stem; it lacks the repeated tall descenders needed for éléments de.','Retain the existing cancelled classes/fermés alternatives.')
decision('B12','Quotient has a descending q and final crossed t, with no independent abbreviation stop. Pré is written above ordre. The short live group after the cancellation has l, apostrophe, and ens.','Retain the first reading and its unreadable cancelled group.')
decision('B13','The wider original shows the opening parenthesis and forall i,j beyond the second box. The right member remains unstarred X_i; both closure bars are visible.','Retain; the omitted opening is a neutral-box scope difference.',crop='crops/150_scan004_root_P10wide.png')
decision('B14','Rare has four low letter bodies, distinct from rencontre. Croissante is attached by a curved leader. The wider color crop shows loc immediately followed by finie, with no detached stop after loc.','Retain the formulas and insertions; remove the unwritten abbreviation point.',[('famille loc. finie','famille loc finie')],crop='crops/150_scan004_root_loc.png')
decision('B15','The first line has Dans le and comment. In the doubtful short phrase after formée, the q descender is followed by a low ue ending without a separate i point. The cancelled majorent-like group has one j-like descender.','Prefer celles que; preserve the other existing wording and revision-state uncertainties.',[(r'\unsure{celles qui|telles que}',r'\unsure{celles que|celles qui|telles que}')])
decision('B16','The angular 4 and separate closing parenthesis are clear.','Retain the authorial folio wrapper.')
decision('B17','Rotating the original marginal group by 180 degrees gives y<x and x∈J, plus a barred J/I and J/I to the left of a vertical rule. Above y a curved J/superset-like sign and a compact double downward/crossed sign remain ambiguous. A short separate stroke lies below its left foot.','Replace the upside-down interpretation by an upright diagram, preserving all small signs and their unresolved forms.',[(C['B17']['first'],newdiagram)])
decision('B18','Partition indexée is raised; loc. finie stays live before the cancellation. The old second line contains a dotted i.e. sequence before une, not the letters d-o-n-c.','Correct that cancelled abbreviation while preserving the uncertain cancelled phrase and its labelled arrow.',[('donc une','i.e. une')])
decision('B19','Est saturé precedes the strike and remains live. The upper and lower cancelled phrases are too crossed to resolve their old wording fully.','Retain the first reading and its explicit uncertainties.')
decision('B20','The wider original shows forall i∈I, a serifed I without an extra bar, and a union bound j∈bar i, with a separate bar over the final i.','Retain the live une and quantifier; correct the union bound from an inequality to the membership/barred-index expression.',[(r'\bigcup_{j\leq i}',r'\bigcup_{j\in\overline i}')],crop='crops/150_scan004_root_P20wide.png')
decision('B21','Relation is certainly cancelled; the possible strike at cette remains inseparable from its t crossbar. The closing mark after the first inclusion has two angular lobes, unlike the smooth parenthesis after the second.','Keep the cancellation uncertainty and prefer a right brace, with parenthesis as an alternative.',[(r'\overline{X_j^*})\n',r'\overline{X_j^*}\unsure{\rbrace|)}\n')] if False else [("\\overline{X_j^*})\n", "\\overline{X_j^*}\\unsure{\\rbrace|)}\n")],crop='crops/150_scan004_root_P20wide.png')
decision('B22','The live wording reads est celle / associée à, with two l ascenders in celle. Qui est aussi and the compressed topologie remain visible.','Retain the first reading; the second conjecture canonical wording is not supported.')
decision('B23','The independent lower line under stratifiante does not traverse its bodies. The crowded earlier parenthesis and the initial blob before loc. finie remain covered by leaders and ascender/descender crossings.','Retain the first reading, including its local wording and state uncertainties; the second excerpt is incomplete.')
decision('B24','Correspondance has two independent lower emphasis strokes. Stratifiantes is raised with an attachment leader, and the sur X / à fibres loc. fermées insertion remains visible.','Retain the double underline, insertions and l’ens des familles wording.')
decision('B25','The raised loc. fini ends with an i and stop/comma, and lies under the index-order description. In the later numbered phrase the last low turns of famille and croissante do not securely establish s; their singular forms are favored.','Retain the attachment of loc. fini and the cancelled et, but qualify the two endings with singular preferred.',[('1°) familles',r'1°) \unsure{famille|familles}'),(r'\uline{croissantes} de parties',r'\uline{\unsure{croissante|croissantes}} de parties')])
decision('B26','A separate long lower stroke runs beneath fermées, distinct from the curved insertion attachment on its left.','Retain the inserted underlined word.')
decision('B27','The cancelled subscript after 4° has a stem with two angled branches, favoring k. Rare and dans each have separate underlines; an additional crossed group precedes X_j. The lower parenthetical contains i.e., but its opening and whether the long upper leader also bars X_i* remain uncertain. Under the later X_i* are two vertical strokes beside déf and the defining expression.','Correct the local wording/marks, retain uncertainty in the crowded parenthetical, and align the vertical definition below X_i* instead of treating its two strokes as quotation marks.',[(r'\unsure{X_\alpha|X_k}',r'\unsure{X_k|X_\alpha}'),('$X_j$ rare dans $X_i$',r'\deleted{\illegible{1}} $X_j$ \uline{rare} \uline{dans} $X_i$'),(oldparent,newparent),(olddef,newdef)],crop='crops/150_scan004_root_P25wide.png')
decision('B28','The slanted label has a 3, b/i/s sequence and a closing curve after bis; no independent degree mark occurs there. The large divider crosses the X subscript, which remains uncertain.','Resolve the label to 3 bis); retain the rest, including the uncertain subscript.',[(r'\unsure{3 bis)|3° bis}','3 bis)')])
decision('B29','The recursive formula has a visible star on the union summand. The abbreviation has a p body and stop, without a secure separate s. After fermés there is an upper point and lower comma.','Retain the literal recursive formula and les, prefer p. with ps. as an alternative, and restore the semicolon.',[('une ps. partition',r'une \unsure{p.|ps.} partition'),('fermés, celle-ci','fermés; celle-ci')])
decision('B30','The raised phrase begins with a p-descender and ou/r group, followed by l’ordre donné and a short accented à. A separate comma follows stricte. The compact ssi remains supported.','Read pour l’ordre donné à I and restore the comma; retain the three underlined words and ssi.',[(r'\uline{stricte} \inserted{avec l\'ordre donné de $I$}',r'\uline{stricte}, \inserted{pour l\'ordre donné à $I$}')] if False else [("\\uline{stricte} \\inserted{avec l'ordre donné de $I$}","\\uline{stricte}, \\inserted{pour l'ordre donné à $I$}")])
decision('B31','The small condition numerals are retraced and admit either ordering. Stricte under the upper underline lacks the long f required for fidèle; the later fidèle has two pairs of quotation ticks. The last adjective after Partitions is compressed after stratif, the relation has a definite left arrowhead but insecure right head, and the final stricte has no secure extra s.','Retain the clear upper wording and quotes; reopen the numbered order, prefer the short stratif. form and leftward relation, and qualify final plurality.',[('Conditions 1°) et 2°).',r'Conditions \unsure{1°) et 2°)|2°) et 1°)}.'),('Partitions stratifiantes',r'Partitions \unsure{stratif.|stratifiantes}'),(r'$\Longleftrightarrow$ strat. strictes',r'$\unsure{\Longleftarrow|\Longleftrightarrow}$ strat. \unsure{stricte|strictes}')],crop='crops/150_scan004_root_summary.png')
decision('B33','The supplied second box clips the displayed intersection formula and mainly contains the following 4° line. The wider original shows X_i∩X_j, the union, and k∈bar i∩bar j beneath it.','Retain the intersection formula; record the box-scope limitation rather than treating omitted ink as a contrary reading.',crop='crops/150_scan004_root_P25wide.png')

# Source changes are exact, once-only replacements in the current page.
for d in rows:
    if d['decision']=='revise':
        a=C[d['box']]['first']; b=d['final']
        replace(a,b)
# Update any stored final excerpt touched by a local replacement, preserving
# historical c/h witnesses and the fixed first/second readings.
local_pairs=[(oldcancel,newcancel),(r'\uline{préordonné}',r'pré\uline{ordonné}'),(r'X_L^*',r'X_{\unsure{L|U}}^*'),(r'\Rightarrow L\text{ ouvert}',r'\Rightarrow\unsure{L|U}\text{ ouvert}'),('i.e. 1°',r'i.e. \unsure{1°|2°}'),(r'\unsure{3°|7°}',r'\unsure{7°|3°|2°}'),(oldpre,newpre),(r'\unsure{celles qui|telles que}',r'\unsure{celles que|celles qui|telles que}'),('donc une','i.e. une'),(r'\unsure{X_\alpha|X_k}',r'\unsure{X_k|X_\alpha}'),(oldparent,newparent),(olddef,newdef),(r'\unsure{3 bis)|3° bis}','3 bis)')]
for c in R['changes']:
    f=c['final']; n=f
    for a,b in local_pairs:n=n.replace(a,b)
    if n!=f:change(c['id'],final=n)

def fbox(b):return next(x['final'] for x in rows if x['box']==b)
change('P01_a',final=r'Condition plus \unsure{fte|forte}',evidence='A short f/t/e group follows plus; independent o/r bodies are not secure. The abbreviation is preferred without expansion.',against_c=True,confidence='medium')
change('P05_b',final=next(x['final'] for x in R['changes'] if x['id']=='P05_b').replace(r'\bigcup_{j\leq i}',r'\bigcup_{'+indexmark+r'\leq i}'),evidence='The hooked indices remain j. A separate wavy lower mark beneath the union-bound j is restored, with underline/tilde alternatives; the written j/i mismatch is retained.',confidence='medium')
change('P07_a',against_c=True,confidence='low',evidence='The numeral has a flat upper stroke and angled leg, favoring 7 over 3; 2 remains a less likely independent proposal. No mathematical expectation decides the digit.')
change('P08_c',final=newpre,evidence='Two horizontal bars form the precolon equals sign. A high d-like loop and apostrophe favor d’une after the colon, with une retained as an alternative.',kind='misread symbol or index',error_category=1,confidence='medium')
change('P14_c',evidence='After the q descender the ending is low ue, with no independent i point. Celles que is preferred while the earlier alternatives remain.',confidence='medium')
change('P17_a',final=newdiagram,evidence=next(x['evidence'] for x in rows if x['box']=='B17'),crop='crops/150_scan004_second_B17.png',confidence='low')
change('P18_b',evidence='Dotted i.e. precedes the small une-like group under the cancellation. The surrounding old description remains doubtful; the phi-labelled arrow is retained.')
change('P20_c',final=next(x['final'] for x in R['changes'] if x['id']=='P20_c').replace(r'\overline{X_j^*})\quad',r'\overline{X_j^*}\unsure{\rbrace|)}\quad'),evidence='The closing mark immediately after the first barred X_j* has two angular lobes and is preferred as a right brace; a parenthesis remains an alternative. The next equivalence has its own smooth parentheses.',confidence='medium')
change('P25_b',against_c=True,confidence='low',evidence='A stem and two angled branches favor the k subscript under the cancellation; alpha remains a local alternative.')
change('P25_c',final=fbox('B27'),evidence=next(x['evidence'] for x in rows if x['box']=='B27'),confidence='medium')
change('P25_d',final=newparent,evidence='I.e. is readable in the lower parenthetical. The initial quantified group and the status of the long upper stroke as a closure bar remain uncertain; the leader does not establish cancellation.',confidence='low')
change('P25_e',place='Vertical definition below X_i*',final=newdef,against_c=True,evidence='Two parallel upright strokes stand between X_i* and the expression below it, beside déf. They function as a vertical equality; no independent closing quotation ticks occur.',kind='insertion or placement',error_category=6,confidence='medium')
change('P26_b',evidence='The slanted label has 3 bis followed by a closing curve, with no separate degree mark. The unstarred X subscript still meets the divider and remains doubtful.',confidence='medium')
change('P28_b',final=r"\inserted{pour l'ordre donné à $I$}",evidence='The insertion begins p/ou/r, followed by l’ordre donné and accented à. Its surrounding curve is a leader, not parentheses.',confidence='medium')
change('P29_a',final=r'Conditions \unsure{1°) et 2°)|2°) et 1°)}.',evidence='The two tiny numerals are retraced; their ordering cannot be securely resolved after the second reading. The first preferred order is retained under uncertainty.',against_c=False,confidence='low')
change('P29_c',final=r'Partitions \unsure{stratif.|stratifiantes}',evidence='The noun retains its terminal plural return. The next group is secure through stratif but its compressed ending does not support certain expansion; the short form is preferred.',against_h=True,confidence='low')
change('P29_d',final=r'strat. \unsure{stricte|strictes}',evidence='The final word has the t and e loop, with no securely distinct final s; singular is preferred and no terminal full stop is supplied.',confidence='medium')

newchange('B04','S_B04_emphasis','Underline begins after pré',r'\uline{préordonné}','préordonné',r'pré\uline{ordonné}','The separate lower emphasis stroke begins below ordonné, not below the written pré prefix.','other','10')
newchange('B09','S_B09_marks','Dash and two points after barred X_i*',r'\ldots',r'\ldots',r'$\unsure{\mathinner{-\cdot\cdot}|\ldots}$','One horizontal dash followed by two detached points is visible; an ellipsis is retained only as an alternative.','misread symbol or index',1)
newchange('B14','S_B14_stop','No stop after loc in family description','famille loc. finie','famille loc. finie','famille loc finie','The wider original shows no independent point between loc and finie.','text not on the page',9)
newchange('B20','S_B20_bound','Union bound in right condition b)',r'\bigcup_{j\leq i}',r'\bigcup_{j\le i}',r'\bigcup_{j\in\overline i}','The lower bound has an E-shaped membership sign and a separate bar over i.','misread symbol or index',1,consequential=True)
newchange('B25','S_B25_endings','Numbered family phrase endings',r'familles \uline{croissantes}',r'familles \emph{croissantes}',r'\unsure{famille|familles} \uline{\unsure{croissante|croissantes}}','The low endings do not securely show added s; the visibly shorter singular readings are preferred.','misread word',2,confidence='low')
newchange('B29','S_B29_abbrev','Abbreviation before partition','ps. partition','ps. partition',r'\unsure{p.|ps.} partition','The short group has a p body and stop, without a clearly separate s.','misread word',2,confidence='low')
newchange('B29','S_B29_stop','Punctuation after fermés','fermés, celle-ci','fermés, celle-ci','fermés; celle-ci','An upper point and separate lower comma form a semicolon.','misread symbol or index',1)
newchange('B30','S_B30_comma','Comma after stricte',r'\uline{stricte} \inserted',r'\emph{partition stratifiante stricte} \add',r'\uline{stricte}, \inserted','A detached comma follows the underlined adjective before the insertion.','omission',3)
newchange('B31','S_B31_arrow','Direction of final relation',r'\Longleftrightarrow',r'\Longleftrightarrow',r'\unsure{\Longleftarrow|\Longleftrightarrow}','The left head is definite; the right end is rounded and lacks a secure outward head.','misread symbol or index',1,confidence='low',consequential=True)

update('decisions','id','M0264',decision='other',reading='$=$',evidence='Two separate horizontal bars occur before the colon, without letter bodies.',confidence='high')
update('decisions','id','M0270',reading=r'\unsure{celles que|celles qui|telles que}',evidence='The ending after q has low ue strokes and no secure i point.',confidence='medium')
update('decisions','id','M0271',decision='other',reading='y<x',evidence='The marginal group is written 180 degrees from the main text. In its own orientation the hooked y and crossed x flank a less-than sign.',confidence='high')
update('decisions','id','M0272',decision='other',reading=r'\in J',evidence='After rotation the formerly cap-like pair is a membership sign followed by J above x; the separate curved sign above y is recorded independently.',confidence='medium')
update('decisions','id','M0282',decision='undecided',reading=r'\unsure{1°) et 2°)|2°) et 1°)}',evidence='The retraced small digit bodies do not fix the ordering securely.',confidence='low')
update('decisions','id','M0283',decision='undecided',reading=r'Partitions \unsure{stratif.|stratifiantes}',evidence='The word after Partitions is secure through stratif; the compressed final strokes do not establish the full expansion.',confidence='low')
update('decisions','id','M0284',decision='undecided',reading=r'strat. \unsure{stricte|strictes}',evidence='The final e loop is visible but a separate terminal s is insecure; no final stop occurs.',confidence='medium')

for p in ['P08 precolon item','P17 top disputed sign','P17 first lower-left sign','P17 second lower-left sign','P25 déf closing ticks','P26 bis label']:
 E.setdefault('report_removals',[]).append(dict(collection='doubts',match={'place':p}))
doubt('P01 short heading',r'\unsure{fte|forte}','fte preferred; forte possible','The short f/t/e sequence does not separate an o/r pair.','medium')
doubt('P01 cancelled remnants',r'\deleted{\unsure{celle de}}; \deleted{'+newcancel+'}','fidèle or fermé with uncertain subscript','The strike covers the small letter bodies.')
doubt('P04 L/U capitals',r'\unsure{L|U}','L preferred; U possible','Rounded bases admit both forms.','medium')
doubt('P05 marginal degree',r'\unsure{1°|2°}','1° preferred; 2° possible','The upper hook and lower foot are not cleanly separable.','medium')
doubt('P05 lower index mark',indexmark,'underline, tilde-like mark, or inseparable continuation','A distinct wavy lower stroke occurs beneath the union-bound j.','medium')
doubt('P07 second NB digit',r'\unsure{7°|3°|2°}','7° preferred; 3° and 2° possible','The flat top and angled leg favor 7 but the small body is not secure.')
doubt('P07 final dash/points',r'\unsure{\mathinner{-\cdot\cdot}|\ldots}','dash plus two points; possible ellipsis','The actual horizontal and dot forms are preserved.','medium')
doubt('P08 postcolon article',r"\unsure{d'une|une}",'d’une preferred; une possible','A high loop and detached apostrophe-like stroke precede une.','medium')
doubt('P14 following phrase',r'\unsure{celles que|celles qui|telles que}','celles que preferred','The q ending has no secure i point.','medium')
doubt('P17 upright symbols',r'\overline{\unsure{J|I}},\unsure{J|I};\unsure{J|\supset};\unsure{\Downarrow|\notin}','J/I, J/superset, double downward arrow/notin','Orientation is secure; the individual compact symbols remain ambiguous.')
doubt('P18 cancelled original description',r'\deleted{\unsure{de parties disjointes de $X$, de réunion $X$, i.e. une $X\xrightarrow{\varphi}I$}}','i.e. preferred; other crossed wording remains provisional','Independent points support i.e.; cancellation still obscures other letters.')
doubt('P20 closing mark',r'\unsure{\rbrace|)}','right brace preferred; closing parenthesis possible','The two angular lobes differ from the later smooth parenthesis.','medium')
doubt('P24 family endings',r'\unsure{famille|familles},\unsure{croissante|croissantes}','singular forms preferred','No independent s is securely present in either low ending.')
doubt('P25 cancelled subscript',r'\deleted{$\unsure{X_k|X_\alpha}$}','k preferred; alpha possible','The branches are crossed by the cancellation.')
doubt('P25 lower parenthetical',newparent,'initial forall group and closure bar uncertain','I.e. is visible; the long leader overlaps the position of a possible closure bar.')
doubt('P27 abbreviation',r'\unsure{p.|ps.}','p. preferred; ps. possible','A separate s cannot be isolated.')
doubt('P29 summary numerals',r'\unsure{1°) et 2°)|2°) et 1°)}','first order preferred','Small retraced bodies prevent secure ordering.')
doubt('P29 short adjective',r'\unsure{stratif.|stratifiantes}','short form preferred','The terminal group is compressed.')
doubt('P29 final relation',r'\unsure{\Longleftarrow|\Longleftrightarrow}','leftward arrow preferred','Right endpoint does not securely form an outward arrowhead.')
doubt('P29 final adjective',r'\unsure{stricte|strictes}','singular preferred','The final e is clear but a following s is not.','medium')

update('inventory','element','E35',first_words_or_objects='upright after 180-degree rotation: barred J/I, J/I, vertical separator, y<x with ambiguous upper signs and short lower stroke, x∈J')
update('hand','habit','The digit 3 may have an angular upper body resembling 7.',consistency='The clear 3 elsewhere does not resolve the ambiguous left NB digit; its flat top and angular leg now favor 7, with 3/2 alternatives.',witness_errors='C and H give different digits; no mathematical sequence is used to settle the ink.')
update('notation','form',r'\Uparrow,\ \Updownarrow',evidence='P05 and P11 show double-shaft marginal arrows. The P17 group is oriented 180 degrees from the main text and its compact downward sign remains qualified.')
update('notation','form','paired upper quotation ticks',meaning='source quotation marks around fidèle only',evidence='P29 has two independent tick pairs. The P25 pair is instead vertical equality between X_i* and its definition below.')
update('notes','id','N04',text='The vertical déf annotation below X_i* gives X_i minus the union over j<i of X_j, with no star on its summand. The later Moyennant sentence explicitly uses X_j* in that union. Both forms are retained; no equivalence is supplied by editorial emendation.')
update('notes','id','N06',text='The landscape sheet has a central pen divider, two slanted left separator strokes and a horizontal left separator. The isolated upper-right group is written at 180 degrees to the main text and is reproduced upright, preserving uncertain J/I and upper symbols. The authorial numbers are 3 and 4); a thinner lower-left 3 has indeterminate attribution. No date is visible. Pale reversed/show-through matter is excluded.')
update('notes','id','N07',text='The quotient criterion has an extra closing parenthesis after X_L* ouvert. In the right uniqueness display the first closing mark is brace-like and remains qualified as brace/parenthesis; the next equivalence has separate parentheses. Curved leaders at loc. finie, croissante, stratifiantes and pour l’ordre donné à I are not separate underlines or parentheses. Fermées has an independent underline.')
E['report_appends'].setdefault('notes',[]).append(dict(id='N11',text='Independent-reading scope check: B13 clipped the opening quantifier, and B33 clipped most of the intersection formula. The main reader inspected wider original crops P10wide and P25wide and retained those readings. The fixed second reading is not altered. The upright marginal diagram was a substantive orientation correction.'))
E['report_appends'].setdefault('notation',[]).append(dict(form=r'\mathinner{-\cdot\cdot}',meaning='literal dash followed by two points, possible ellipsis',evidence='Left NB after the barred X_i*; the visual sequence is retained with an ellipsis alternative rather than supplying three unwritten dots.'))
E['report_appends'].setdefault('check_events',[]).append(dict(statement_id='150_scan004.audit',type='independent visual audit',outcome='Root inspected every differing second crop, plus wider original scope/orientation details, before explicit adjudication; no OCR, external research or TeX compilation used.',who='main reader; GPT-6 Astra Pro; inherited effort'))
# Category values remain numeric in the reporting schema.
for x in E['report_appends'].get('changes',[]):x['error_category']=int(x['error_category'])
assert [x['box'] for x in rows]==[x['box'] for x in C.values() if not x['token_equal']]
assert not (W/'second'/f'{page}_root_decisions.json').exists()
(W/'second'/f'{page}_root_decisions.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(W/'second'/f'{page}_edits.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':page,'decisions':len(rows),'revisions':sum(x['decision']=='revise' for x in rows),'new_changes':len(E['report_appends']['changes'])}))
