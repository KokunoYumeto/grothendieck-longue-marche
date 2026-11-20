from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-02',12,123,'typescript')
title=r'''\mbox{\begin{tikzpicture}[x=1em,y=1em,baseline=(b.base)]
\node[anchor=base west,inner sep=0] (b) at (0,0) {\uline{\rlap{\deleted{U}}\handwritten{u}n morphisme projectif et lisse}};
\node[anchor=base west,inner sep=0,rotate=1] at (-.1,1.65) {\inserted{\handwritten{\uline{Trivialite cohomologique d'}}}};
\draw[line width=.35pt] (-.65,-.4) .. controls (-1.0,.55) and (-.65,1.0) .. (.0,1.05) .. controls (6,1.05) and (12.6,.9) .. (14.8,1.3) .. controls (15.3,1.4) and (15.6,1.65) .. (15.45,1.9);
\end{tikzpicture}}'''
en=r'''\mbox{\begin{tikzpicture}[x=1em,y=1em,baseline=(b.base)]
\node[anchor=base west,inner sep=0] (b) at (0,0) {\deleted{trivial (i.e.}};
\node[anchor=base west,inner sep=0,rotate=2] at (-2.1,1.05) {\inserted{\handwritten{En d'autres termes,}}};
\end{tikzpicture}}'''
addition=r'''\mbox{\resizebox{\linewidth}{!}{\begin{tikzpicture}[x=1em,y=1em,font=\small]
\node[anchor=base west,inner sep=0] at (31,0) {dégénère\deleted{)}.};
\node[anchor=base west,inner sep=0] at (40,0) {\deleted{Un cas très}};
\node[anchor=base west,inner sep=0] at (38.5,1.15) {\handwritten{\deleted{\unsure{E}}}};
\draw[line width=.45pt] (38.8,.95) -- (38.8,.6) -- (39.4,.6) -- (39.4,.15) -- (40,.15);
\node[anchor=base west,inner sep=0,rotate=1] at (40,1.15) {\inserted{\handwritten{Ce théorème est}}};
\node[anchor=base west,inner sep=0,rotate=1] at (0,-1.5) {\inserted{\handwritten{prouvé par Deligne modulo le ``Th\unsure{ê|é}or\unsure{ê|è}me de Lefschetz'' pour la cohomologie des fibres.}}};
\node[anchor=base west,inner sep=0] at (0,-3.05) {\rlap{\deleted{\unsure{D|S}}}\handwritten{S}a démonstration s'applique également dans le contexte des variétés};
\node[anchor=base west,inner sep=0] at (0,-4.05) {\deleted{particulier de ce résultat}};
\end{tikzpicture}}}'''
ait=r'''\mbox{\begin{tikzpicture}[x=1em,y=1em,baseline=(b.base)]
\node[anchor=base west,inner sep=0] (b) at (0,0) {\deleted{e} le};
\node[anchor=base west,inner sep=0] at (-.45,1.05) {\inserted{ait}};
\draw[line width=.35pt] (.15,-.4) .. controls (-.1,.25) and (.3,.65) .. (1.1,.7) .. controls (1.8,.75) and (2.7,1) .. (2.7,1.5);
\end{tikzpicture}}'''
rapporteur=r'''\mbox{\begin{tikzpicture}[x=1em,y=1em,baseline=(b.base)]
\node[anchor=base west,inner sep=0] (b) at (0,0) {\deleted{rédacteur}};
\node[anchor=base west,inner sep=0,rotate=1] at (-.05,1.1) {\inserted{\handwritten{rapporteur}}};
\end{tikzpicture}}'''
nombreux=r'''\mbox{\begin{tikzpicture}[x=1em,y=1em,baseline=(b.base)]
\node[anchor=base west,inner sep=0] (b) at (0,0) {ingrédients};
\node[anchor=base west,inner sep=0,rotate=1] at (-.8,1.4) {\inserted{\handwritten{nombreux}}};
\draw[line width=.35pt] (-.25,-.35) .. controls (-.7,-.1) and (-.5,.75) .. (-.1,.9) .. controls (1.4,1.0) and (3.1,.75) .. (3.9,.95) .. controls (4.7,1.05) and (4.9,1.25) .. (4.7,1.5);
\end{tikzpicture}}'''
indispensables=r'''\mbox{\begin{tikzpicture}[x=1em,y=1em,baseline=(b.base)]
\node[anchor=base west,inner sep=0] (b) at (0,0) {\deleted{nécessaires}};
\node[anchor=base west,inner sep=0,rotate=1] at (.05,1.05) {\inserted{\handwritten{indispensables}}};
\end{tikzpicture}}'''
arith=r'arithmét\unsure{\rlap{q}i|\rlap{i}q}\unsure{\rlap{i}q|\rlap{q}i}ues'
somme=r'\unsure{\rlap{s}c|\rlap{c}s}omme'
riemann=r'R\rlap{\deleted{e}}\handwritten{i}\rlap{\deleted{i}}\handwritten{e}mann'
tordus=r'tord\unsure{\rlap{d}u|\rlap{u}d}s'
sera=r'\handwritten{s}e\rlap{\deleted{\unsure{s}}}\handwritten{\unsure{r}}\rlap{\deleted{\unsure{t}}}\handwritten{a}'
r.edit(r"\inserted{\handwritten{\uline{\unsure{Trivialite|Trivialité} cohomologique d'}}}\uline{\unsure{Un|un} morphisme projectif et lisse}",title)
r.edit(r"\deleted{est toujours cohomologiquement trivial (i.e.} \inserted{\handwritten{En d'autres termes,}}",r'\deleted{est toujours cohomol\unsure{o}giquement} '+en)
r.edit(r'\deleted{l}\handwritten{L}a',r'\rlap{\deleted{l}}\handwritten{L}a')
r.edit(r'''dégénère\deleted{)}. \deleted{Un cas très particulier de ce résultat}\inserted{\handwritten{\deleted{\unsure{E}}Ce théorème est prouvé par Deligne modulo le ``Théorème de \unsure{Lefschetz}'' pour la cohomologie des fibres.}} \handwritten{S}a démonstration s'applique également dans le contexte des variétés''',addition)
r.edit(r'\deleted{e}\inserted{ait} le',ait)
r.edit(r'\deleted{\unsure{en top}}',r'\deleted{en top}')
r.edit(r'\deleted{Par exemple, le}',r'\deleted{Par exemple, l\unsure{a|e}} ')
r.edit(r'\deleted{\unsure{et}}',r'\deleted{et}')
r.edit(r'\handwritten{C}e sont',r'\rlap{\deleted{\unsure{c}}}\handwritten{C}e sont')
r.edit('arithmétiques',arith)
r.edit(r'\deleted{rédacteur}\inserted{\handwritten{rapporteur}}',rapporteur)
r.edit(r'\unsure{somme|comme}',somme)
r.edit(r'\unsure{Reimann|Riemann}',riemann)
r.edit(r'$\handwritten{\ell}$-adique',r'$\handwritten{\unsure{\ell|l}}$-adique')
r.edit('tordus',tordus)
r.edit(r'\inserted{\handwritten{nombreux}} ingrédients',nombreux)
r.edit(r'\deleted{nécessaires}\inserted{\handwritten{indispensables}}',indispensables)
r.edit(r'\handwritten{\unsure{sera}}',sera)
r.change('added title, final e',r'\unsure{Trivialite|Trivialité}','Trivialité','Trivialite','The last letter is a looped e with a clear blank area above it. No detached acute is present; the terminal t stem belongs to the preceding letter. C’s qualification is resolved without adding the accent used by H.','titleword;titlelast;titleplace;title rot',kind='misread word',against_C=True)
r.change('title placement and curved insertion leader','inline added underlined title','marginal title; editorial note says above line',title,'The underlined added words lie above the first typed line. A separate long curved leader runs below the title, descends on the left before the opening word and curls upward at its right. Both words and leader are reproduced in relative position.','titleplace;titlerot',kind='insertion or placement',against_C=True)
r.change('opening Un corrected to un',r'\unsure{Un|un}','Un; editorial note acknowledges lowercase correction',r'\rlap{\deleted{U}}\handwritten{u}n','A small handwritten cup and upright form a lowercase u across the taller typed U; the two forms occupy the same position. This is a correction with surviving old ink, not a choice between two independently printed words.','Un;titleplace',kind='deletion state',against_C=True)
r.change('cancelled cohomologiquement, glyph between l and g','cohomologiquement','cohomologiquement',r'cohomol\unsure{o}giquement','The position between l and g is covered by a dense black blot with a rounded lower outline and an upright remnant above. It supports an o-shaped body but does not let the complete glyph or any earlier impression be read securely. The position is qualified instead of being silently supplied from the word.','cancelclause1;blob',kind='misread word',confidence='low',against_C=True)
r.change('En d’autres termes placement',r"\inserted{\handwritten{En d'autres termes,}}",r"\marginal{En d'autres termes,}",en,'E-n, d-apostrophe-autres, termes and the final comma are legible on a slightly rising line above the cancelled end of the clause, with En beginning to the left of trivial. The addition is interlinear, not in the margin or consecutive on the base line.','En;Enrot;Enplace;cancelclause2',kind='insertion or placement',against_C=True)
r.change('La suite, l beneath L',r'\deleted{l}\handwritten{L}a','la',r'\rlap{\deleted{l}}\handwritten{L}a','The old short serifed l remains under a larger looped handwritten L. They share one type position, and the new capital is followed by the typed a.','La',kind='deletion state',against_C=True)
r.change('first adique label',r'\handwritten{\unsure{\ell|l}}',r'\ell',r'\handwritten{\unsure{\ell|l}}','A typed serifed l is crossed or reworked by an oblique pen stroke extending below its base. An upper loop is not securely separated from the old upright, so C’s ell/l doubt is retained.','ell1',kind='misread symbol or index',confidence='medium',consequential=True)
r.change('cancelled extra glyph in first coéfficients',r'coéffi\deleted{\unsure{s}}cients','coéfficients',r'coéffi\deleted{\unsure{s}}cients','An extra type position before c has upper and lower curved fragments under the pen cancellation. They support s but do not expose the whole shape; the old glyph and its qualification remain.','coeff1',kind='omission',confidence='low')
r.change('base field alphabet','$C$',r'$\mathbb{C}$','$C$','The character is a single typewritten curved C with two terminal serifs. No second vertical or doubled contour is drawn.','Cparen',kind='misread symbol or index',consequential=True)
r.change('cancelled closing parenthesis after C',r'\deleted{)}','omitted',r'\deleted{)}','A typed curved right parenthesis lies immediately after C under crossing pen strokes; the following short hyphen remains live.','Cparen',kind='omission')
r.change('cancelled closing parenthesis after dégénère',r'\deleted{)}','omitted',r'\deleted{)}','The upright curved parenthesis is crossed several times just before the live full stop. The mark is not part of the accent or final e.','degparen',kind='omission')
r.change('cancelled Un cas très / particulier de ce résultat',r'\deleted{Un cas très particulier de ce résultat}',r'two \struck{\ill{}} fragments','Un cas très cancelled at right; particulier de ce résultat cancelled below the Sa line','All the typed words remain distinguishable beneath x strikes: U-n, cas, très at the right end of the upper typed line, and particulier de ce résultat on a lower line beneath Sa démonstration. The two readable fragments retain their physical relation to the interleaved live line.','Uncas;particulier;addsentence',kind=r'readable ink left as \ill{}',against_C=True,marked_in_H=True)
r.change('initial E-like mark before added Ce',r'\deleted{\unsure{E}}','omitted',r'\deleted{\unsure{E}} with short bent tail','The heavily retraced mark has a left vertical and several rightward strokes, supporting an E-like false start; a short bent continuation drops toward the cancelled Un. It may instead be a retraced insertion sign, so the lexical reading stays qualified and the visible continuation is drawn.','Estart;addsentence',kind='omission',confidence='low',against_C=True)
r.change('added sentence physical layout','entire sentence inserted inline','entire sentence in marginal macro; placement described in editorial note',addition,'Ce théorème est is above the cancelled upper-right Un cas très; the handwritten continuation begins at the left on the next interline. The typed Sa démonstration line and the lower cancelled particulier fragment are interleaved beneath it. The drawing preserves this order and placement.','Ce;prouve;modulo;theoreme;Lefschetz;pourla;fibres;addsentence;prouverot;fibresrot',kind='insertion or placement',against_C=True)
r.change('quoted second theorem, case and quotation signs',r"``Théorème de Lefschetz''",'« théorème de Lefschetz »',r"``Th\unsure{ê|é}or\unsure{ê|è}me de Lefschetz''",'The second theorem word begins with a tall capital T and a long top crossbar. Two short strokes open the quoted phrase and two close it; no angular guillemets are present. Accent qualifications are recorded separately.','theoreme;modulo;Lefschetz;pourla',kind='abbreviation expanded or spelling modernised')
r.change('second theorem, first accent','é','é',r'\unsure{ê|é}','Above the first e, a faint rising left stroke meets a shorter dark descending right stroke, making a peaked mark. A small hooked acute cannot be excluded, so the circumflex-shaped reading is preferred but qualified.','theoreme;accent1',kind='misread word',confidence='medium',against_C=True)
r.change('second theorem, second accent','è','è',r'\unsure{ê|è}','Above the second e is a broad arch with both ends descending. Its rounded circumflex shape is clearer than a single grave stroke, but the faint left limb prevents certainty. The accent is not normalized from the word.','theoreme;accent2;accent2full',kind='misread word',confidence='medium',against_C=True)
r.change('Lefschetz in added sentence',r'\unsure{Lefschetz}','Lefschetz','Lefschetz','The enlarged and rotated name separates the initial L, e, crossed looped f, s curve, open c, tall h, e, t and terminal descending z. The crowding does not prevent the letters being read; C’s doubt is removed.','Lefschetz;prouverot',kind='misread word',against_C=True,against_H=False)
r.change('under handwritten S of Sa',r'\handwritten{S}a','Sa',r'\rlap{\deleted{\unsure{D|S}}}\handwritten{S}a','Beneath the new S there is a typewritten left upright, a broad lower bowl and a basal foot. These favour an older D, but the crossing S obscures enough of the outline that an old S remains possible. The underlying ink omitted by both witnesses is kept qualified.','Sa;Sabase',kind='omission',confidence='low',against_C=True)
r.change('typed ait insertion and leader',r'\deleted{e}\inserted{ait} le',r'\struck{e}\marginal{ait} le',ait,'The replacement a-i-t is typewritten immediately above the cancelled final e of constitue. A pen leader runs below ait, drops left to the old e and curves upward on the right; the base le remains below and to its right.','ait;aitplace',kind='insertion or placement',against_C=True)
r.change('cancelled en top after Deligne',r'\deleted{\unsure{en top}}','omitted',r'\deleted{en top}','The x strikes leave e and n, then the t ascender/crossbar, rounded o and descending p separately visible. C’s doubt is resolved and H’s omission restored.','entop',kind='omission',against_C=True)
r.change('cancelled Par exemple, last article',r'\deleted{Par exemple, le}',r'\struck{par exemple, la}',r'\deleted{Par exemple, l\unsure{a|e}}','The first letter has a tall stem and upper P bowl, so the capital is secure. After the comma and l, the cancelled last vowel has a lower closed bowl and a right foot favouring a, but crossing strokes leave e possible; neither witness’s unqualified ending is adopted.','Parexemple;lastle',kind='misread word',confidence='medium',against_C=True)
r.change('cancelled et',r'\deleted{\unsure{et}}',r'\struck{et}',r'\deleted{et}','A small e loop/opening and a separate t with upper stem and cross-stroke remain beneath the pen strike. Both letters are readable; C’s doubt is removed.','etcancel',kind='misread word',against_C=True,against_H=False)
r.change('under handwritten capital C in Ce sont',r'\handwritten{C}e','Ce',r'\rlap{\deleted{\unsure{c}}}\handwritten{C}e','The large handwritten C overlays a smaller typewritten curved body at the same baseline as e. The small form is consistent with c, but its opening is masked by the new C; its reading remains qualified.','Ce2;Ce2base',kind='omission',confidence='medium',against_C=True)
r.change('two overlapping type positions in arithmétiques','arithmétiques','arithmétiques',arith,'At each of the two positions after arithmét, a dotted i form coexists with a q bowl and descender. Both positions visibly contain both impressions. Their order of printing is not recoverable securely, so the paired overlays are preserved with qualified alternatives.','arith;arithpair',kind='omission',confidence='medium',against_C=True)
r.change('rapporteur above cancelled rédacteur',r'\deleted{rédacteur}\inserted{\handwritten{rapporteur}}',r'\struck{rédacteur}\marginal{rapporteur}',rapporteur,'Every letter of the struck rédacteur remains legible. The handwritten r-a-p-p-o-r-t-e-u-r is directly above it, with both p descenders and the tall crossed t distinct after rotation. There is no marginal displacement.','redacteur;rapporteur;rapporteurrot;rapporteurplace',kind='insertion or placement',against_C=True)
r.change('overprinted initial before omme',r'\unsure{somme|comme}','comme',somme,'The first type position contains an open c-shaped left curve and the upper/lower curves and central crossing of s. The forms are superposed; the image does not establish which impression was last. Both are represented at one position instead of choosing a whole word from syntax.','somme',kind='insertion or placement',confidence='medium',against_C=True)
r.change('Reimann corrected by pen',r'\unsure{Reimann|Riemann}','Riemann',riemann,'After the typed R, the first old vowel retains an e eye and lower curve beneath a smaller added i. The next old typewritten i retains its dot and serifs beneath a low handwritten e loop. The corrections are spatially distinct from the old ei and give ie; both layers are kept.','Reimann',kind='insertion or placement',against_C=True)
r.change('second adique label',r'\handwritten{\ell}',r'\ell',r'\handwritten{\unsure{\ell|l}}','The second occurrence again shows a serifed typed l with an added diagonal pen stroke and a lower continuation. As in the first occurrence, no securely separate upper loop settles ell against reworked l; the same local uncertainty is marked at both places.','ell2;ell1',kind='misread symbol or index',confidence='medium',against_C=True,consequential=True)
r.change('end of cancelled restent valables sous une',r'\deleted{restent valables sous une}',r'\struck{restent valables sous}',r'\deleted{restent valables sous une}','After sous and a struck space, the typewritten u sides, n shoulder and final e eye remain visible through the x strikes. The cancelled une is present and readable.','restent',kind='omission')
r.change('overprint at final vowel of tordus','tordus','tordus',tordus,'The position after tord contains the ascender and bowl of d as well as the two uprights/cup of u. The preceding d is a separate normal typed letter. The two forms in the final vowel position overlap and their printing order is left uncertain.','tordus;du',kind='omission',confidence='medium',against_C=True)
r.change('nombreux with curved leader',r'\inserted{\handwritten{nombreux}} ingrédients',r'\marginal{nombreux} ingrédients',nombreux,'The n-o-m-b-r-e-u-x forms are legible above the left part of ingrédients. A long curved leader below the word descends to the gap before ingrédients and curls upward over the middle of that typed word. Both the raised addition and the leader are retained.','nombreux;nombreuxrot;nombreuxplace',kind='insertion or placement',against_C=True)
r.change('indispensables above cancelled nécessaires',r'\deleted{nécessaires}\inserted{\handwritten{indispensables}}',r'\struck{nécessaires}\marginal{indispensables}',indispensables,'The single pen strike crosses all of nécessaires while leaving its letters and acute readable. The replacement indispensables is written directly above, with i dots, d ascender, p descender and b/l rises distinguishable in the rotated enlargement.','necessaires;indispensables;indispensablesrot;indispensablesplace',kind='insertion or placement',against_C=True)
r.change('quotation signs around théorie des motifs',r"``théorie des motifs''",'« théorie des motifs »',r"``théorie des motifs''",'Two high short typewriter strokes occur at each end of the phrase. The o of motifs is a filled round type impression without separable earlier letter strokes; no additional letter is inferred.','motifs',kind='abbreviation expanded or spelling modernised')
r.change('last word, handwritten replacement over old type',r'\handwritten{\unsure{sera}}',r'se\ill{}',sera,'A long handwritten s precedes a clean typed e. The following dark position has an upper running hand stroke and a downstroke supporting r over an older two-curved s-like body; the last position has a looped handwritten a and rightward tail over a taller crossed t-like remnant. The r and both old letters remain qualified, while the visible s, e and final a are retained.','sera;seralayers;serafull',kind=r'readable ink left as \ill{}',confidence='low',against_C=True,marked_in_H=True)
for line,reading,alt,conf,why in [
('cancelled cohomologiquement, after l','o','','low','Rounded lower outline survives within a dense blot; the whole typeform is not exposed.'),
('first adique label','ell','plain/reworked l','medium','Diagonal pen stroke over a serifed typed l; upper loop not secure.'),
('extra cancelled glyph in coéfficients','s','','low','Curved fragments remain under cancellation.'),
('before added Ce théorème','E','retraced graphical insertion mark','low','Vertical and horizontal strokes are heavily retraced; a bent continuation is reproduced.'),
('second theorem word, first accent','ê','é','medium','Peaked two-arm mark, with a faint left limb.'),
('second theorem word, second accent','ê','è','medium','Broad arch rather than a single diagonal, but faint left side.'),
('under S of Sa','D','S','low','Old upright/bowl/foot partly hidden by the new S.'),
('cancelled Par exemple, article','la','le','medium','Closed bowl and right foot favour a; crossing strokes leave e possible.'),
('under C of Ce sont','c','','medium','Smaller old curved typeform partly hidden by new C.'),
('arithmétiques, two middle positions','overlapping q/i then i/q','reverse printing orders','medium','Both glyphs are visible at each position; sequence of impressions cannot be recovered.'),
('before une conjecture','superposed s and c before omme','printing order reversed','medium','Both typeforms share one position.'),
('second adique label','ell','plain/reworked l','medium','Same unresolved composite glyph as the first occurrence.'),
('tordus, position after tord','superposed d/u','printing order reversed','medium','Separate d ascender/bowl and u cup coexist.'),
('last word, live third letter','r','','low','Running top stroke and downward stroke are partly merged with older ink.'),
('last word, under r','s','','low','Two-curved old type body is heavily obscured.'),
('last word, under a','t','','low','Old tall stem and cross-stroke remain but are overlaid.')]:r.doubt(line,reading,alt,conf,why)
r.notation('adique label reworked over typed l',r'\unsure{\ell|l}','12:123 both occurrences: serifed l with a crossing oblique hand stroke; no secure upper loop.','unresolved')
r.notation('typed field C','$C$','12:123 after corps de base: single curved typewritten C, no doubled contour.')
r.notation('literal spelling and accents','Trivialite; coéfficients; kählériennes; frobénius','12:123 unaccented title ending; typed acute in both coefficient occurrences, ä and é in kählériennes, lowercase accented frobénius.')
r.notation('overprinted typeforms with uncertain sequence',r'\unsure{\rlap{a}b|\rlap{b}a}','12:123 arithmétiques, somme/comme and tordus: both impressions retained without claiming printing order.','partly unresolved')
r.r['abbreviations']=[dict(abbreviation='i.e.',expansion='id est',attestations='12:123 inside cancelled introductory clause; abbreviation kept as typed')]
r.r['inventory_overrides']={f'123-{i:02d}':dict(hand='another unnamed hand') for i in [1,3,5,7,8,13,14,15,20,22,23,25,27,29,31,32]}
for i in [4,6,9,10,11,16,24,30]:r.r['inventory_overrides'][f'123-{i:02d}']=dict(hand='typewriter')
r.r['inventory_overrides']['123-12']=dict(hand='typewriter',position='Un cas très at upper right; particulier de ce résultat below live Sa line')
r.r['inventory_overrides']['123-14']=dict(hand='another unnamed hand',position='Ce théorème est at right above Un cas très; continuation across next interline',first_words_or_objects='Ce théorème est prouvé...; second theorem accents qualified')
r.r['inventory_overrides']['123-17']=dict(hand='typewriter',position='ait above cancelled e; curved pen leader')
r.r['inventory_overrides']['123-21']=dict(hand='typewriter',first_words_or_objects='Par exemple, l(a/e), cancelled')
r.r['inventory_overrides']['123-27']=dict(hand='another unnamed hand',first_words_or_objects='qualified ell / l')
r.r['inventory_overrides']['123-32']=dict(hand='typewriter and another unnamed hand',first_words_or_objects='hand s, typed e, qualified hand r and hand a over old qualified s/t')
extra=[('drawing','below added title','long curved insertion leader','another unnamed hand'),('deletion','opening word','typed U under handwritten u','typewriter'),('insertion','opening word','handwritten u over U','another unnamed hand'),('drawing','below initial E-like mark','short bent continuation toward cancelled Un','another unnamed hand'),('deletion','under Sa capital','qualified older D/S','typewriter'),('drawing','below ait','curved leader to old e','another unnamed hand'),('deletion','under Ce capital','qualified older c','typewriter'),('text','arithmétiques, two positions after arithmét','overlapping i/q and q/i impressions, sequence uncertain','typewriter'),('text','before une conjecture','overlapping s/c before omme, sequence uncertain','typewriter'),('deletion','Reimann before -Weil','old typed e and i beneath handwritten i and e','typewriter'),('insertion','same two vowel positions','handwritten i and e','another unnamed hand'),('text','tordus, after tord','overlapping d/u impressions, sequence uncertain','typewriter'),('drawing','below nombreux','curved leader to gap before ingrédients','another unnamed hand'),('deletion','last word beneath hand r/a','qualified old s and t','typewriter'),('margin note','bottom left','archive folio122 retained as comment','another unnamed hand')]
r.r['inventory_extra']=[dict(scan='12:123',sheet_kind='typescript',hand=h,element=f'123-R{i:03d}',kind=k,position=p,first_words_or_objects=w,transcribed='yes') for i,(k,p,w,h) in enumerate(extra,1)]
r.r['crops']=json.loads(Path('work/crops12_123.json').read_text())
r.r['inspection_note']='Root alone viewed the whole supplied scan and both actual supplied halves before C, the full H slice, all11 C doubts, all3 spelling-slip entries and all32 C inventory elements. Every agreed word and sign was checked against the ink line by line; both actual halves were reread after the detailed decisions. All74 recorded crops were actually viewed, including rotated title/interlinear additions/replacement words and the final overprint, all cancellations and margins, arrow/field/ell labels, accents, punctuation, underlines and every C doubt. Trivialite, en top, et and Lefschetz are resolved from the ink; opening U/u and Reimann/Riemann preserve both layers. Both witnesses flatten internal overprints and omit old letters beneath the large S/C and final replacement. The two ell/l forms, two arched accents, several old letters and printing orders remain qualified. The E-like initial mark may be graphical; its visible bent tail is drawn without asserting a word. The trailing H section Divers types de Q-ell-faisceaux introduces a different sheet and has no corresponding writing on this page; it is treated as a source-boundary heading, not an omitted manuscript passage or collation item. Handwritten elements are attributed only to another unnamed hand. Archive122 remains a comment. No mathematical claim has been checked, no ordered second audit is claimed, and context remains sealed.'
# Correct the crop identifier in the title-word decision without touching any source.
r.r['changes'][0]['crop']='titleword;titlelast;titleplace;titlerot'
r.save('work/record12_123.json')
