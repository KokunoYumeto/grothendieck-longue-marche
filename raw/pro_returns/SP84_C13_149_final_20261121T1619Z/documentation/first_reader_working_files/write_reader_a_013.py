from pathlib import Path
import json
p=Path('/workspace/scratch/4644e52611c0')
tex=r'''\scanpage{13}
\mspage{6}
p.ex. que la dim coh. de $\pi_i$ est égale à $n$, celle de $E_i$ est $\leq n+2$ (pour des coeff. \deleted{$\neq2$} de $m$-torsion, quand $m$ est impair) --- et par passage à la limite, des majorations correspondantes pour les dim coh. de $\pi_{\bar K/K}$ et de $E_{\bar K/K}^{\unsure{\ell}}$
\[
(\unsure{14})\qquad \dim\operatorname{coh}\pi_{\bar K/K}\leq n,\qquad
\dim\operatorname{coh}_{\ell}E_{\bar K/K}\leq n+2\quad\text{si }\ell\neq2
\qquad(\ell\text{ nb premier})
\]
qui sont en fait même des \uline{égalités} (\unsure{sauf|s.f.} erreur), et \unsure{donnent|donnant} donc une description cohomologique simple du degré de transcendance absolu de $K$.

\uline{Théorème 1} Soit $K$ un corps \inserted{extension} de type fini de $\mathbb Q$. \deleted{Alors} $\bar K$ une clôture algébrique de $K$. Alors pour tout sous-groupe ouvert $\unsure{\mathcal E|\epsilon}$ de $E_{\bar K/K}$, son centralisateur dans $E_{\bar K/K}$ est réduit au groupe unité. Itou pour $\pi_{\bar K/K}$.

Démonstration. Soit \deleted{$\unsure{E'\subset E}$}\inserted{$\Gamma'\subset\Gamma\subset$}$\subset\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ l'image de $E$ dans $\Gamma$\inserted{$=\Gamma_{\bar K/K}$}, qui est donc un ss-groupe ouvert. \inserted{L'image dans $\Gamma$ du centralisateur de $\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}$ dans $\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}$ est contenue dans \unsure{le} centralisateur de $\Gamma'$ dans $\Gamma$.} \deleted{Si $g\in\Gamma_{\bar K/K}$ centralise $\unsure{\mathcal E|\epsilon}$, son image $\gamma$ dans $\Gamma$ centralise $\Gamma'\unsure{\subset}\Gamma_{\mathbb Q}$} Je dis qu'il est
\margin{12}
'''
(p/'edition/reviews/149_scan013.tex').write_text(tex,encoding='utf-8')
boxes={
'c01':[690,63,1040,146], 'c02':[272,277,803,364], 'c03':[1050,479,1435,571],
'c04':[399,599,602,702], 'c05':[270,655,1660,790], 'c06':[272,789,1635,1014],
'c07':[263,1197,1660,1371], 'c08':[292,1378,568,1460], 'c09':[1309,1423,1640,1510],
'c10':[1275,1629,1514,1710], 'c11':[1080,1802,1333,1993], 'c12':[318,1969,773,2102],
'c13':[320,2038,1655,2164], 'c14':[333,2144,1469,2242], 'c15':[315,2078,1647,2229],
'c16':[312,2197,970,2320], 'c17':[20,2305,79,2348], 'c18':[500,155,1290,273], 'c19':[730,0,930,75]}
def crop(c): return f'crops/149_scan013_{c}.png'
changes=[]
def change(i,place,C,H,final,evidence,c,confidence='high',against_C=False,against_H=True,kind='other',error_category='Other',marked_in_H=False,mathematical=False):
    changes.append(dict(id=f'c{i:02d}',place=place,C=C,H=H,final=final,evidence=evidence,crop=crop(c),box=boxes[c],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical))
change(1,'Opening paragraph, first dim coh.', 'dim coh.','dim. coh.','dim coh.', 'The dot over i is above the word; the space after the final m is blank. A separate low dot follows coh. only.','c01')
change(2,'Opening paragraph, cancelled condition after coeff.',r'\deleted{$\neq2$}',r'\struck{\ill{}}',r'\deleted{$\neq2$}', 'Under the cancellation, two horizontal relation strokes and an oblique inequality stroke precede the curved top and lower foot of 2. The two signs are recoverable, although crossed.','c02',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True,mathematical=True)
change(3,'Opening paragraph, second dim coh.','dim coh.','dim. coh.','dim coh.', 'After the long low final m there is no punctuation; the low round stop is after coh. The isolated upper point belongs to i.','c03')
change(4,'Opening paragraph, raised mark on final E expression',r'E_{\bar K/K}^{\unsure{\ell}}',r'E_{\overline K/K}',r'E_{\bar K/K}^{\unsure{\ell}}', 'A distinct raised looped stroke is present to the right of the extension index. Its retraced lower loop prevents a secure identification as ell, but it cannot be omitted.','c04',confidence='medium',kind='omission',error_category='Omissions',mathematical=True)
change(5,'Paragraph after display, parenthetic phrase','sauf','s.f.',r'\unsure{sauf|s.f.}', 'There is an initial s-like stroke, a very reduced middle run, and a tall final looped f. The middle run does not securely distinguish written au from abbreviation punctuation. The leading C reading is provisional; H remains an explicit alternative.','c06',confidence='low',kind='misread word',error_category='Words')
change(6,'Paragraph after display, verb after et','donnent','donnant',r'\unsure{donnent|donnant}', 'The d and final t are distinct, while the intervening low connected strokes flatten the vowel before nt. Neither e nor a is decisive. The leading C reading is provisional; H remains an explicit alternative.','c06',confidence='low',kind='misread word',error_category='Words')
change(7,'Theorem, subgroup symbol after ouvert',r'\unsure{\mathcal E|\epsilon}',"E'",r'\unsure{\mathcal E|\epsilon}', 'The glyph has two rounded open lobes, rather than the upright and three bars of the proof\'s plain E. No separate upper-right prime is visible in the clear space beside this occurrence. Script capital E versus epsilon remains unresolved.','c09',confidence='medium',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change(8,'Theorem, short word after groupe unité.','Idem','Itou','Itou', 'After the large I, the next letter has a straight tall stem and short cross stroke; the following rounded o runs into a low terminal u. There is no looped d or final m.','c10',against_C=True,against_H=False,kind='misread word',error_category='Words')
change(9,'Proof opening, hatched-out chain',r"\deleted{$\unsure{E'\subset E}$}",r'\struck{\ill{}}',r"\deleted{$\unsure{E'\subset E}$}", 'The left symbol retains an E-like upper bar, left stem and lower bar, with a separate raised prime; a second barred E-like symbol appears at the right. The intervening inclusion curve is crossed by heavy hatching. C\'s tentative chain is retained without claiming complete recovery.','c11',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True,mathematical=True)
change(10,'Proof opening, raised replacement chain',r"\inserted{$\Gamma'\subset\Gamma\subset$}$\Gamma_{\overline{\mathbb Q}/\mathbb Q}$",r"$\Gamma'$ \add{$\Gamma'\subset\Gamma_{\overline{\mathbb Q}/\mathbb Q}}$",r"\inserted{$\Gamma'\subset\Gamma\subset$}", 'The upper row contains Gamma with a separate prime, an open inclusion curve, a second unprimed Gamma, and another inclusion curve. The indexed Gamma is on the lower baseline; H duplicates or relocates parts of this two-level chain.','c11',kind='insertion or placement',error_category='Insertions put in the wrong place',marked_in_H=True,mathematical=True)
change(11,'Proof opening, extra baseline inclusion before indexed Gamma','(omitted)','(omitted)',r'\subset', 'Besides the final inclusion in the raised chain, a separate open inclusion curve remains on the baseline after the hatched-out E chain and before the indexed Gamma. Both levels are retained. Whether this lower sign was meant to be cancelled with the preceding chain is not plain; it has no decisive cancellation through its body.','c11',confidence='medium',against_C=True,against_H=True,kind='omission',error_category='Omissions',mathematical=True)
change(12,'Proof, l’image de ... dans Gamma',r'\unsure{E|\mathcal E}',"E'",'E', 'The glyph has one upright stem and distinct upper, middle and lower rightward bars. The upper-right space is blank: no prime is attached. This also resolves C mark M0984 to its first reading.','c12',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change(13,'Proof, first small interlinear line',r"\inserted{L'image dans $\Gamma$ du centralisateur de $\unsure{\mathcal E|\epsilon}$ dans $\unsure{\mathcal E|E}$ est contenue ...}",r"\struck{L'image dans $\Gamma$ du centralisateur de $E'$ \ill{} $E'$ est \ill{}}",r"\inserted{L'image dans $\Gamma$ du centralisateur de $\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}$ dans $\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}$ est contenue ...}", 'The small writing occupies a distinct interlinear baseline. The straight cancellation runs through the larger Si g... line below, not through this text. The word dans is visible between the two rounded symbols. Each symbol has a small upright nearby, but those strokes overlap descenders from the upper live line, so prime versus neighbouring descender is left open. The full centralisateur has continuing letters after its reduced middle run, not a secure abbreviation stop.','c13',confidence='medium',kind='deletion state',error_category='Struck text',marked_in_H=True,mathematical=True)
change(14,'Proof, continuation of small interlinear insertion',r"\inserted{contenue dans le centralisateur de $\Gamma'$ dans $\Gamma$.}",r"\add{\ill{} centralisateur de $\Gamma'$ dans $\Gamma_{\mathbb Q}$}",r"\inserted{contenue dans \unsure{le} centralisateur de $\Gamma'$ dans $\Gamma$.}", 'Crop c13 supplies conte-; c14 begins nue and continues on the small interlinear baseline. After dans, the putative le overlaps the large extension index from the struck line above, so that word remains doubtful. Centralisateur, de, Gamma-prime, dans and the final small Gamma are readable. No Q subscript is securely attached to that final small Gamma; its low following mark is taken as the stop.','c14',confidence='medium',kind='insertion or placement',error_category='Insertions put in the wrong place',marked_in_H=True,mathematical=True)
change(15,'First large struck proof line, subgroup after centralise',r'\unsure{\mathcal E|\epsilon}',"E'",r'\unsure{\mathcal E|\epsilon}', 'The large ruled-out line has an open double-lobed glyph after centralise. There is no separate raised prime in its own spacing. Its two curves resemble the theorem\'s uncertain script E/epsilon form, not the plain barred E of l\'image de E.','c15',confidence='medium',kind='misread symbol or index',error_category='Symbols and indices',marked_in_H=True,mathematical=True)
change(16,'First large struck proof line, son image ... dans',r'\gamma','g',r'\gamma', 'After image the sign has a forked upper entry and a single descending curved leg. It lacks the closed bowl and returning descender of the Latin g earlier in the same struck line. Dans follows on that same large baseline; the small centralisateur phrase belongs to the interlinear insertion.','c15',kind='misread symbol or index',error_category='Symbols and indices',marked_in_H=True,mathematical=True)
change(17,'Second large struck proof line, tail after centralise',r"\Gamma'\subset\Gamma_{\mathbb Q}",r"\Gamma'\ \ill{}",r"\Gamma'\unsure{\subset}\Gamma_{\mathbb Q}", 'A separate prime stands to the right of the first Gamma. An open inclusion-like curve is crossed by slanted cancellation strokes, so its reading is kept doubtful. The following Gamma and lowered Q are visible. This is part of the large struck row, not the small inserted final Gamma.','c16',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True,mathematical=True)
change(18,'Lower-left marginal numbering',r'\margin{12}','(not transcribed)',r'\margin{12}', 'A narrow first digit with angled entry is followed by a curved 2 with a broad horizontal foot. The number is separate from the main proof and must be retained. H\'s nearby prose note is editorial, not a substitute for this number.','c17',kind='omission',error_category='Omissions')

def decision(id,decision,reading,evidence,c,confidence):
    return dict(id=id,decision=decision,reading=reading,evidence=evidence,crop=crop(c),box=boxes[c],confidence=confidence)
four=r"\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}"
decisions=[
decision('M0982','undecided',r'\unsure{\ell}','A raised looped sign is certain, but the retraced upper and lower curves do not decisively identify ell. Its presence is retained against H\'s omission.','c04','medium'),
decision('M0983','undecided',r'\unsure{\mathcal E|\epsilon}','The glyph is rounded and unprimed; its two open lobes can represent script capital E or epsilon. Shape alone does not securely choose between those alphabets.','c09','medium'),
decision('M0984','first','E','A straight left stem carries three separate rightward bars, with no upper-right prime. The clear middle bar and angular left side distinguish this occurrence from the curved symbols.','c12','high'),
decision('M0985','undecided',four,'The two-lobed curved form remains script E/epsilon. A short nearby upper stroke may be a prime or a descender belonging to the line above, so both primed and unprimed forms remain explicit.','c13','low'),
decision('M0986','undecided',four,'The lower and upper lobes are curved, unlike the plain barred E in c12. Script E/epsilon and the nearby possible prime remain unresolved because the upper live line overlaps this insertion.','c13','low')]

inventory=[]
def inv(element,kind,position,first,hand='main manuscript hand'):
    inventory.append(dict(scan=13,sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('e01','text','top centre','6')
inv('e02','text','upper six manuscript lines','p.ex. que la dim coh.')
inv('e03','deletion','opening paragraph after coeff.',r'\neq2')
inv('e04','display','upper-middle, two physical rows',r'(\unsure{14}) dim coh; (ell nb premier)')
inv('e05','text','four lines below display','qui sont en fait même des égalités')
inv('e06','text','middle six baseline lines','Théorème 1 Soit K un corps')
inv('e07','insertion','above de type in first theorem line','extension')
inv('e08','deletion','start of second theorem line','Alors')
inv('e09','text','lower proof paragraph, including final live fragment','Démonstration. Soit')
inv('e10','deletion','after Soit, below raised replacement chain',r"\unsure{E'\subset E}")
inv('e11','insertion','above the cancelled proof chain',r"\Gamma'\subset\Gamma\subset")
inv('e12','insertion','above Gamma in second proof baseline',r'=\Gamma_{\bar K/K}')
inv('e13','insertion','two small interlinear lines in lower proof','L’image dans Gamma du centralisateur')
inv('e14','deletion','two larger baseline lines under/between small addition',r'Si g in Gamma; Gamma centralise Gamma-prime')
inv('e15','margin note','extreme lower-left margin','12','hand not established from this small number')

notes=[
'Folio 6; scan 13. The page continues a cohomological-dimension discussion, gives display (14), and starts the underlined Théorème 1 and its proof. No date is visible. The proof ends mid-sentence with Je dis qu’il est.',
'The main text, agreed readings and complete displayed formulas were read against the full image and both supplied halves. All 26 supplied difference rows and all five packet marks were then checked. The line count 29 includes the folio and marginal number, the separately placed parenthetical formula row, three raised short insertions, and both small interlinear lines.',
'The c06 alternatives remain local doubts. Leading sauf and donnent are retained provisionally, with H’s s.f. and donnant explicitly printed as alternatives. Those two low-confidence collation rows record the continuing C/H word disagreements; they are not assertions that H has been disproved.',
'The proof opening visibly contains both the upper Γ′⊂Γ⊂ chain and a separate lower inclusion sign before the indexed Gamma. The extra lower sign is preserved literally. Its intended cancellation or replacement status is not certain; no mathematical expectation was used to collapse the duplicated relation.',
'The small centralizer sentence is a live interlinear insertion. The two larger lines beginning Si g and Gamma centralise are struck out. The reading order keeps those states separate. The small words overlap large cancelled subscripts, especially le; this is marked rather than supplied confidently.',
'The two small curved group symbols retain four local alternatives to expose the separate script-E/epsilon and prime/descender questions. The theorem’s corresponding symbol and the larger struck symbol have clear unprimed spacing. The plain E in l’image de E is graphically distinct and resolved without importing an expected group relation.',
'The extra doubt on display label 14, the doubt on le, and the added doubt on the struck inclusion sign are certainty-only changes: they have no substantive changes rows of their own. C’s nested doubt on the cancelled E′⊂E is also retained.',
'All 19 saved crops were personally inspected. Crops c13–c15 are rotated 3.2 degrees clockwise after enlargement to separate the slanted writing visually; their recorded boxes are in original source coordinates. Crops c18–c19 check agreed numbers and do not support substantive changes.',
'No OCR, external research, other page text, other reader report, TeX compilation or mathematical proof/check was used. Model identification: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149.'
]
hand=[
 dict(habit='The abbreviation dim has no following stop at either prose occurrence; coh has a low separate stop.',pages=[13],consistency='Both local occurrences agree (c01, c03).',misread='An upper i dot must not be moved to the end of dim.'),
 dict(habit='Plain capital E can have a straight upright and three distinct horizontal bars, while other group symbols have two rounded open lobes.',pages=[13],consistency='Clear local contrast between c12 and c09/c13/c15.',misread='The curved form alone does not resolve script capital E versus epsilon.'),
 dict(habit='Rapid vowel sequences flatten into low nearly horizontal runs.',pages=[13],consistency='Visible in the two disputed words in c06 and in centralisateur in the small insertion.',misread='The run does not securely distinguish au from abbreviation punctuation or e from a in c06.'),
 dict(habit='Small interlinear writing is placed above and between larger crossed-out lines.',pages=[13],consistency='The two small centralizer lines are distinct from the ruled-out Si g and Gamma centralise baselines.',misread='Descenders from the upper line can imitate primes beside small group symbols.')]
notation=[
 dict(written=r'E_{\bar K/K}',rendering=r'E_{\bar K/K}',meaning='Extension-indexed E used in the dimension assertion and theorem.',evidence='The first subscript K has an overbar and the two K letters are separated by a near-upright slash.'),
 dict(written=r'\pi_{\bar K/K}',rendering=r'\pi_{\bar K/K}',meaning='The pi object named alongside E; no fresh definition on this page.',evidence='Opening paragraph, display and final line of theorem; low two-legged pi with the full extension index.'),
 dict(written=r'\Gamma_{\overline{\mathbb Q}/\mathbb Q}',rendering=r'\Gamma_{\overline{\mathbb Q}/\mathbb Q}',meaning='Indexed Gamma at the end of the proof’s opening inclusion chain.',evidence='c11: unstruck baseline Gamma followed by lowered Qbar/Q; the upper replacement chain is separate.'),
 dict(written='two open curved lobes',rendering=r'\unsure{\mathcal E|\epsilon}',meaning='Unresolved letter form used for a subgroup/centralizer argument in the text.',evidence='c09 and c15 are unprimed; c13 additionally has uncertain nearby upper strokes.'),
 dict(written=r'\dim\operatorname{coh}_{\ell}',rendering=r'\dim\operatorname{coh}_{\ell}',meaning='Written dimension notation in the second bound of the display.',evidence='c05: ell sits below coh; no redefinition or mathematical repair is supplied.')]
abbreviations=[
 dict(form='p.ex.',expansion='par exemple',place='opening of page'),
 dict(form='dim',expansion='dimension',place='opening paragraph and display'),
 dict(form='coh.',expansion='cohomologique',place='two prose occurrences in opening paragraph'),
 dict(form='coeff.',expansion='coefficients',place='opening paragraph'),
 dict(form='nb',expansion='nombre',place='display parenthesis'),
 dict(form='ss-groupe',expansion='sous-groupe',place='second proof baseline'),
 dict(form='s.f. (uncertain alternative)',expansion='sauf',place='parenthesis after égalités')]
doubts=[
 dict(place='Opening final E expression, c04',reading=r'\unsure{\ell}',alternatives=['ell','unidentified raised retraced sign'],confidence='medium',reason='The raised sign is distinct, but its looped retracing is not decisive.'),
 dict(place='Display label, c05',reading=r'\unsure{14}',alternatives=['14','K-like joined shape'],confidence='medium',reason='The tall leading stroke and following angular form can be read as joined 1 and 4, but the literal outline is also K-like. No numbering sequence is used to settle it.'),
 dict(place='Parenthetic phrase after égalités, c06',reading=r'\unsure{sauf|s.f.}',alternatives=['sauf','s.f.'],confidence='low',reason='The reduced middle run lacks decisive vowel or stop boundaries.'),
 dict(place='Verb after erreur), et, c06',reading=r'\unsure{donnent|donnant}',alternatives=['donnent','donnant'],confidence='low',reason='The vowel before nt is flattened in a connected low run.'),
 dict(place='Theorem subgroup, c09',reading=r'\unsure{\mathcal E|\epsilon}',alternatives=[r'\mathcal E',r'\epsilon'],confidence='medium',reason='Two open curved lobes; no prime visible, but alphabet remains ambiguous.'),
 dict(place='Cancelled proof opening, c11',reading=r"\unsure{E'\subset E}",alternatives=[r"E'\subset E",'partly obscured chain'],confidence='medium',reason='Heavy diagonal hatching crosses the middle relation and letter bodies.'),
 dict(place='Proof opening additional baseline relation, c11',reading=r'\subset',alternatives=['retained baseline inclusion','uncancelled remnant of the cancelled chain'],confidence='medium',reason='The sign is visible separately from the raised inclusion, but its intended state cannot be proved from the cancellation boundary.'),
 dict(place='First small inserted group symbol, c13',reading=four,alternatives=[r'\mathcal E',r'\epsilon',r"\mathcal E'",r"\epsilon'"],confidence='low',reason='Curved letter form and a possible prime overlap upper-line descenders.'),
 dict(place='Second small inserted group symbol, c13',reading=four,alternatives=[r'\mathcal E',r'\epsilon',r"\mathcal E'",r"\epsilon'"],confidence='low',reason='Curved letter form; short upper stroke may belong to the preceding line.'),
 dict(place='Small insertion, word after dans before centralisateur, c14',reading=r'\unsure{le}',alternatives=['le','obscured short word'],confidence='low',reason='The large K/K index from the struck line crosses the small writing here.'),
 dict(place='Large struck subgroup symbol, c15',reading=r'\unsure{\mathcal E|\epsilon}',alternatives=[r'\mathcal E',r'\epsilon'],confidence='medium',reason='The double-lobed unprimed form is clear but script versus Greek is not.'),
 dict(place='Second large struck line, relation after Gamma-prime, c16',reading=r'\unsure{\subset}',alternatives=[r'\subset','relation obscured by cancellation'],confidence='medium',reason='The open curve is crossed by diagonal strokes; certainty alone has been reduced.')]
audit=[]
def ab(i,kind,b,reading):
    audit.append(dict(box=f'b{i:02d}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
ab(1,'handwritten number',[800,29,842,74],r'\mspage{6}')
ab(2,'prose',[710,64,972,140],'dim coh.')
ab(3,'formula',[565,170,1020,239],r'$E_i$ est $\leq n+2$')
ab(4,'deletion',boxes['c02'],r'\deleted{$\neq2$} de $m$-torsion,')
ab(5,'prose',[1055,480,1323,568],'dim coh.')
ab(6,'formula',boxes['c04'],r'$E_{\bar K/K}^{\unsure{\ell}}$')
ab(7,'formula',boxes['c05'],r'(\unsure{14})\quad \dim\operatorname{coh}\pi_{\bar K/K}\leq n,\quad \dim\operatorname{coh}_{\ell}E_{\bar K/K}\leq n+2\quad\text{si }\ell\neq2\quad(\ell\text{ nb premier})')
ab(8,'prose',boxes['c06'],r'qui sont en fait même des \uline{égalités} (\unsure{sauf|s.f.} erreur), et \unsure{donnent|donnant} donc une description')
ab(9,'handwritten number',[270,1260,606,1370],r'\uline{Théorème 1}')
ab(10,'insertion',[1120,1195,1385,1307],r'\inserted{extension}')
ab(11,'deletion',[299,1387,475,1452],r'\deleted{Alors}')
ab(12,'formula',[1565,1435,1627,1505],r'$\unsure{\mathcal E|\epsilon}$')
ab(13,'prose',[1325,1633,1486,1700],'Itou')
ab(14,'formula',boxes['c11'],r"\deleted{$\unsure{E'\subset E}$}\inserted{$\Gamma'\subset\Gamma\subset$}$\subset\Gamma_{\overline{\mathbb Q}/\mathbb Q}$")
ab(15,'insertion',boxes['c12'],r'$E$ dans $\Gamma$\inserted{$=\Gamma_{\bar K/K}$}, qui')
ab(16,'insertion',boxes['c13'],r"\inserted{L'image dans $\Gamma$ du centralisateur de $\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}$ dans $\unsure{\mathcal E|\epsilon|\mathcal E'|\epsilon'}$ est conte-}")
ab(17,'insertion',boxes['c14'],r"\inserted{nue dans \unsure{le} centralisateur de $\Gamma'$ dans $\Gamma$.}")
ab(18,'deletion',boxes['c15'],r'\deleted{Si $g\in\Gamma_{\bar K/K}$ centralise $\unsure{\mathcal E|\epsilon}$, son image $\gamma$ dans}')
ab(19,'deletion',boxes['c16'],r"\deleted{$\Gamma$ centralise $\Gamma'\unsure{\subset}\Gamma_{\mathbb Q}$}")
ab(20,'margin note',boxes['c17'],r'\margin{12}')

diff=[]
def dc(row,cl,cid,reason): diff.append(dict(row=row,classification=cl,change_id=cid,reason=reason))
dc(1,'editorial-only',None,'C scan header and H page-note wrapper are metadata, not differing manuscript words.')
dc(2,'editorial-only',None,'H’s de l’auteur is editorial; the source folio 6 is retained.')
dc(3,'material','c01','Only coh. has a following stop in this occurrence.')
dc(4,'material','c02','The struck relation and digit are recoverable; H leaves them illegible.')
dc(5,'macro-only',None,'C --- and H -- encode the same handwritten continuation dash.')
dc(6,'material','c03','No stop follows the second dim either.')
dc(7,'material','c04','The raised sign is present though its ell reading stays doubtful.')
dc(8,'macro-only',None,'Operator and spacing tokenization of dim/coh; no extra manuscript word.')
dc(9,'macro-only',None,'Operator/spacing tokenization in the two display clauses.')
dc(10,'editorial-only',None,'H’s numbering explanation is not manuscript text. The 14/K-shaped label itself is inspected in c05 and kept doubtful without a certainty-only changes row.')
dc(11,'material','c05','The source middle strokes remain ambiguous between the two witness readings; both alternatives are preserved.')
dc(12,'material','c06','The flattened vowel remains ambiguous; both verb forms are preserved.')
dc(13,'material','c07','Curved unprimed form; script E versus epsilon remains open.')
dc(14,'material','c08','The straight crossed t, round o and low u support Itou.')
dc(15,'material','c09','The cancelled chain is partially recoverable and retained under doubt.')
dc(16,'material','c10','The full raised chain has two inclusion signs and an intervening Gamma.')
dc(17,'material','c10','The first raised Gamma is primed and the second is not; H’s different placement causes the token mismatch.')
dc(18,'material','c12','This occurrence is plain E with no prime.')
dc(19,'material','c13','The live small line contains dans and two curved glyphs; possible primes remain open because of upper-line overlap.')
dc(20,'material','c14','The second small line completes contenue and the centralizer phrase; le is obscured and marked.')
dc(21,'material','c15','The large struck glyph is rounded and unprimed; alphabet remains doubtful.')
dc(22,'material','c16','The larger struck row reads son image gamma dans. The small centralisateur words belong to the separate insertion (c14).')
dc(23,'material','c14','The prime belongs to the small insertion’s Gamma-prime; H interleaves that line with the larger gamma clause.')
dc(24,'material','c14','The small insertion ends with plain Gamma and a stop; the larger struck Gamma_Q is on the following baseline.')
dc(25,'material','c17','The large struck tail retains the inclusion-like sign under doubt and the indexed Gamma_Q.')
dc(26,'material','c18','The marginal 12 is real source text; H’s prose description is editorial and excluded.')
report=dict(scan=13,reader='reader_a',lines_read=29,changes=changes,decisions=decisions,inventory=inventory,notes=notes,checks=[],hand=hand,notation=notation,abbreviations=abbreviations,doubts=doubts,audit_boxes=audit,diff_coverage=diff)
(p/'edition/reviews/149_scan013.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'tex':'edition/reviews/149_scan013.tex','json':'edition/reviews/149_scan013.json','changes':len(changes),'C_departures':sum(c['against_C'] for c in changes),'decisions':len(decisions),'inventory':len(inventory),'audit_boxes':len(audit),'diff_rows':len(diff)},ensure_ascii=False))
