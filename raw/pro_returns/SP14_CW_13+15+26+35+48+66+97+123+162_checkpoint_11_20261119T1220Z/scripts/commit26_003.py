import sys
sys.path.insert(0,'out/scripts')
from work import commit
T=r'''\clearpage
\scanpage{3}

A) \uline{Descente et passage au quotient}

\S\,1\quad Descente fidèlement plate

\S\,2\quad \deleted{Passage \unsure{au|aux} quoti\unsure{ent|.} \unsure{Généralités} sur les foncteurs sur} \inserted{Topologies sur $(\mathrm{Sch})_{/S}$. Propriétés générales des foncteurs sur $(\mathrm{Sch})_{/S}$.} \margin{[Intervertir \uline{1} et \uline{2} ??]}
\par\noindent\hfill\deleted{$(\mathrm{Sch})_{/S}$}

\S\,3\quad Passage au quotient plat.

\S\,4\quad Descente non plate\quad [\unsure{Application|Applications|Applicat.} : \unsure{Ram.|Rau.|Rem.} Samuel \unsure{généralisé} \ldots

\inserted{Appl. à platitude d'une adh. \unsure{schématique} et lemme de \deleted{\unsure{H}}Hironaka.}

\S\,5\quad Passage au quotient non plat. [\unsure{Passage} \unsure{aux|au} \unsure{quots|quot.} en gén]

\S\,6\quad Descente de schémas, relatifs étales, ----

[\unsure{Év\textsuperscript{t}|Éu\textsuperscript{t}}. descente des \deleted{\unsure{morphismes}}\inserted{faisceaux} étales ?? \ldots]

B) \deleted{\uline{Propriétés générales des foncteurs sur} $(\mathrm{Sch})_{/S}$.}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (-1.3,0) {\deleted{\S\,7}};
\node[anchor=west] at (0,0) {Méthodes};
\node[anchor=west] at (2.2,0) {non projectives};
\node (construction) at (7.8,.08) {\inserted{de construction}};
\draw (construction.center) ellipse (2.15cm and .45cm);
\draw[->] (5.65,.3) -- (5.65,.62) -- (2.2,.62) -- (2.2,.05);
\draw (0,-.3) -- (9.65,-.3);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (-1.3,0) {\deleted{\S\,7}};
\node[anchor=west] at (0,0) {\deleted{Propriétés générales \unsure{de|des} \unsure{foncteurs}, et propriétés}};
\node[anchor=west] at (.4,-.65) {\deleted{de permanence}};
\node[anchor=west] at (4.1,.58) {\deleted{\inserted{\unsure{diverses}}}};
\draw (-1.35,.36) -- (4.0,.36) -- (6.5,.55) -- (6.5,.92) -- (4.0,.86);
\draw (-1.35,.36) -- (-1.05,-.94) -- (4.5,-.77) -- (4.6,-.2) -- (10.9,.16);
\end{tikzpicture}}

\S\,7\quad \uline{Proreprésentabilité}: (et variantes).

\tikz[baseline=(p.base),remember picture]{\node[inner sep=1pt] (p) {\S\,\deleted{\unsure{8}}9};}\quad
\uline{Invariants différentiels} \deleted{\unsure{de|du} \unsure{div.}} \inserted{\uline{\unsure{tangts|tang.} et normaux}}

\tikz[baseline=(q10.base)]{\node[inner sep=1pt] (q10) {\S\,10};\draw (q10.center) ellipse (1.25em and .9em);}\quad
\margin{\fbox{Après \S\,12 ??}}Propriétés générales de foncteurs, \uline{propriétés de permanence}
\margin{$\left\{\begin{gathered}\text{Foncteurs \uline{excellent} sur S}\\ \text{morphismes excellent}\\ \text{??}\end{gathered}\right.$}

\tikz[baseline=(q11.base),remember picture]{\node[inner sep=1pt] (q11) {\S\,\deleted{\unsure{10|11}}11};\draw (q11.center) ellipse (1.65em and .9em);}\quad
\margin{\tikz[remember picture]{\node[draw,inner sep=2pt] (m11) {\parbox{.90\marginparwidth}{\raggedright Commun au \unsure{par.} \unsure{20|2e|éd} ? Cas Greenberg ?}};}}
Représentabilités ``élémentaires'' du type $\prod_{\deleted{X}Y/S}X/Y$.

\inserted{cf SGAD $\underline{\overline{\mathrm{VIII}}}$ 6 et $\underline{\overline{\mathrm{XI}}}$ 6.8.}

\tikz[baseline=(r.base),remember picture]{\node[draw,rounded corners,inner sep=1pt] (r) {\S\,8\deleted{\unsure{1|11}}};}
\quad Construction de Modules cohérents
\figure{\begin{tikzpicture}[remember picture,overlay]\draw[->] (r.north west) to[out=125,in=190] (p.north);\draw (q11.east) -- (m11.west);\end{tikzpicture}}

\S\,12\quad \deleted{\unsure{Représentabilité}}\inserted{Foncteurs} \unsure{repr.} par morphismes \inserted{\uline{\unsure{séparés|xprés}}} loc. pr. \unsure{f|fi}

\S\,13\quad Applications : des \unsure{th\textsuperscript{es}|th\textsuperscript{s}} \deleted{de} représentabilité relatifs. (y compris \unsure{(}pour les es foncteurs étales\ldots\unsure{,|)}

% archive sheet number: 2
'''
L=[]
def a(p,c,h,f,ink,conf='high',ac=True,ah=True,k='other',mh='no',con=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if con:d['consequential']=con
 L.append(d)
a('A heading underline','underlined','not underlined','underlined','A: a continuous separate rule runs from Descente through quotient.',ac=False,k='omission')
a('§2 cancelled au/aux','au','aux',r'\unsure{au|aux}','twoold: cancelling strokes cross the short terminal stroke; au is the primary visible form but a separate x cannot be ruled out.','low',k='misread word')
a('§2 cancelled quoti ending',r'quoti\unsure{ent|.}',r'quoti\ill{}',r'quoti\unsure{ent|.}','twoold: quoti is visible before overlapping black strokes; the ending ent versus abbreviation point remains unresolved.','low',False,True,'readable ink left as \\ill{}','yes')
a('§2 cancelled Généralités',r'\unsure{Généralités}','Généralités',r'\unsure{Généralités}','twoold: G and later tall strokes survive, but the superposed cancellation crosses the small middle letters. Doubt retained.','low',False,True,'other')
a('§2 Intervertir numbers','1 and 2 underlined','1 and 2 without underlines','1 and 2 underlined','one_two: a short separate horizontal rule is visible below each numeral.',ac=False,k='omission')
a('§2 cancelled category',r'\unsure{(Sch)/S|(Ens)/S}','(= Sch)/S','(Sch)/S, cancelled','oldsch: S curve, c bowl and h ascender are distinguishable. The long stroke through the initial parenthesis and letters is cancellation, not an independent equals sign.',k='misread symbol or index')
a('§4 application word','Application','Applications',r'\unsure{Application|Applications|Applicat.}','appl4: Applicat- is visible, but the compressed ending is a small rising stroke and nearly horizontal continuation; neither full ending nor abbreviated form is settled.','low',k='misread word')
a('§4 separator',r'\unsure{à|:}',':',':','appl4: two separated short marks are vertically arranged; there is no a bowl or separate accent.',ah=False)
a('§4 Ram. abbreviation',r'\unsure{Ram.|Rau.|Rem.}','Ram.',r'\unsure{Ram.|Rau.|Rem.}','appl4: R is clear; following low joined humps do not settle m/u or the small a/e bowl.','low',False,True,'other')
a('§4 Samuel',r'\unsure{Samuel|Serreil}','Samuel','Samuel','appl4: S, a, joined m/u humps, e and final tall l are visible; there is no doubled r sequence.',ah=False)
a('§4 généralisé',r'\unsure{généralisé}','généralisé',r'\unsure{généralisé}','appl4: the word runs into the right edge; the very small ending remains compressed.','low',False,True)
a('§4 ellipsis',r'\unsure{\ldots|---}',r'\ldots',r'\ldots','appl4: three separate dark points occur at the right after the ending; no three horizontal dashes.',ah=False)
a('§4 blue addition adh.',r'\unsure{adh.}',r'\uncertain{relation}','adh.','appl4: a bowl, d ascender, h and a point are present; the much longer sequence relation is not visible.','medium',k='misread word',mh='yes')
a('§4 blue addition schématique',r'\unsure{schématique}',r'\uncertain{schématique}',r'\unsure{schématique}','appl4: the ending is a compressed continuous wave; both witnesses’ uncertainty retained.','low',False,False,mh='yes')
a('§4 blue addition lemme',r'\unsure{lemme}','lemme','lemme','appl4: l ascender, small e and two joined m humps can be traced.','medium',ah=False)
a('§4 cancelled initial H',r'\deleted{\unsure{H}}','omitted',r'\deleted{\unsure{H}}','appl4: a dense crossed initial precedes the live Hironaka; the older letter remains uncertain under overprinting.','low',False,True,'omission')
a('§4 blue addition Hironaka',r'\unsure{Hironaka}','Hironaka','Hironaka','appl4: after the heavy initial, i with point, r/o, n, a, k and final a are separately traceable.','medium',ah=False)
a('§5 bracket Passage',r'\unsure{Passage}','Passage',r'\unsure{Passage}','note5: P and descending g are visible but intermediate letters overlap; C doubt retained.','low',False,True)
a('§5 bracket aux/au',r'\unsure{aux|au}','aux',r'\unsure{aux|au}','note5: the rightward terminal is compressed and does not settle a separate x.','low',False,True)
a('§5 quotient abbreviation',r'\unsure{quot.|quotients}',r'\uncertain{quots}',r'\unsure{quots|quot.}','note5: the final small hooked stroke fits s better than a single point; the letters ients are not separately written.','low',k='abbreviation expanded or spelling modernised',mh='yes')
a('§5 word after quotient abbreviation',r'\unsure{cat.|catég.}',r'\uncertain{en}','en','note5: two low connected forms are visible, with no tall t or g descender required by cat./catég.','medium',True,False,mh='yes')
a('§5 last abbreviation',r'\unsure{gén}',r'\uncertain{gén.}','gén','gen5: g loop and descender, raised short acute and low n continuation are visible; no separate full stop follows before the bracket.','medium',k='abbreviation expanded or spelling modernised',mh='yes')
a('§6 de/des',r'\unsure{de|des}','de','de','dedes6: d loop is followed by one short e form; no additional s is separately present.','medium',ah=False)
a('§6 after schémas','schémas relatifs','schémas relatifs','schémas, relatifs','schemasend: a detached dark hook curves downward after the final small s form. This comma is omitted by both witnesses.',k='omission')
a('§6 after étales','four dashes','ellipsis','four dashes','six: four short horizontal strokes, separated by clear spaces, follow the comma.',ac=False,k='misread symbol or index')
a('§6 opening short form',r'\unsure{Év\textsuperscript{t}}',r'\uncertain{Évt}',r'\unsure{Év\textsuperscript{t}|Éu\textsuperscript{t}}.','evt: raised t and a separate point below/right are visible. The rounded low v/u form remains ambiguous.','low',k='omission',mh='yes')
a('§6 cancelled morphismes',r'\unsure{morphismes}',r'\ill{}',r'\unsure{morphismes}','oldmorph: a long ascender and several joined low letter bodies survive cancellation, enough for a tentative morphismes, not for a confident resolution.','low',False,True,'readable ink left as \\ill{}','yes')
a('§6 replacement faisceaux','inserted faisceaux','live faisceaux without insertion state','inserted faisceaux','six/oldmorph: faisceaux lies on the line above the struck older word.',ac=False,k='insertion or placement')
a('B cancelled heading','cancelled full heading','described only in a note','cancelled full heading transcribed','B: the underlined heading Propriétés générales des foncteurs sur (Sch)/S remains visible under cancelling strokes.',ac=False,k='omission')
a('B replacement heading order','Méthodes [de construction] non projectives','Méthodes non projectives de construction','Méthodes [de construction] non projectives, with oval and leader','B: the oval phrase at the right has an angular line ending in a downward arrow immediately after Méthodes, before non projectives.',ac=False,k='insertion or placement',con='The construction phrase belongs after Méthodes, as the insertion leader shows.')
a('B oval and leader','words and insertion only','drawing described in a note','TikZ oval, angular leader, underline','B: de construction is surrounded by an oval; the leader turns left above the line and ends after Méthodes. The heading underline runs underneath all three regions.',k='drawing or diagram')
a('B cancelled heading number',r'\deleted{\unsure{\S 7}}','not transcribed','cancelled §7','oldheadingnum: the section-sign loops and upper angular/long descending form of 7 remain beneath the bars.','medium',k='omission')
a('B old paragraph number','cancelled §7',r'cancelled §\ill{}','cancelled §7','old7: the angular upper bar, crossing stroke and long descending limb of 7 are visible.',ac=False,k='readable ink left as \\ill{}',mh='yes')
a('B old paragraph de/des',r'\unsure{de}','des',r'\unsure{de|des}','oldarticle/old7line: the boundary between the end of générales and the following f is crossed by heavy strokes; no separate s is secure. Retained tentative de with des alternative.','low',k='misread word')
a('B old paragraph foncteurs',r'\unsure{foncteurs}','foncteurs',r'\unsure{foncteurs}','old: the tall f and t are visible; several middle bodies merge with the enclosing/cancelling line. Doubt retained.','low',False,True)
a('B old paragraph inserted diverses',r'\deleted{\inserted{\unsure{diverses}}}','omitted',r'\deleted{\inserted{\unsure{diverses}}}','diverses: d and dotted i are visible above the cancelled paragraph; the remaining low letters are crossed and uncertain.','low',False,True,'omission')
a('B old paragraph punctuation','foncteurs, et','foncteurs et','foncteurs, et','old: a detached downward curved comma appears after foncteurs.',ac=False,k='omission')
a('B old paragraph enclosure','no enclosure drawn','enclosure described in note','stepped enclosing/cancelling lines reproduced in TikZ','old/old7line: the upper line steps around the inserted word, the lower line runs beneath de permanence and turns up; these lines are distinct from ordinary glyphs.',k='drawing or diagram')
a('§7 underline','Proreprésentabilité underlined','no underline','underlined','rep7: a separate long rule lies beneath the word.',ac=False,k='omission')
a('§7 punctuation',r'\unsure{:|.}','no punctuation',':','rep7: two vertically placed dark components follow the final é.',k='omission')
a('§9 old number',r'\deleted{\unsure{8}}','old 8 only described in a note',r'\deleted{\unsure{8}}','nine_ten: the upper number is overprinted and lower curved remains suggest 8; old shape not fully recoverable.','low',False,True,'omission')
a('§9 new number',r'\unsure{9}','9','9','nine_ten: one upper loop and a long descending curved stroke distinguish the live 9.',ah=False)
a('§9 cancelled words',r'\unsure{de|du} \unsure{div.}','de',r'\unsure{de|du} \unsure{div.}','tang: two crossed units remain beneath tangts; the first has a d-like ascender and low end, the second starts with a separate ascender. Endings remain hidden.','low',False,True,'omission')
a('§9 inserted tangts',r'\uline{\unsure{tangts|tang.} et normaux}','tangents et normaux',r'\inserted{\uline{\unsure{tangts|tang.} et normaux}}','tang: the live phrase is interlined above the cancelled words and underlined. After tang- the ending is contracted; ents is not spelled out separately.','low',True,True,'abbreviation expanded or spelling modernised')
a('§9 heading underline','underlined Invariants différentiels','no underline','underlined','nine_ten: a long faint rule lies beneath Invariants différentiels.',ac=False,k='omission')
a('§10 after générales',r'\unsure{de|des}','de','de','tenarticle: a looped d and one low attached e tail are visible; no independent s follows.','medium',ah=False)
a('§10 circle, box and underline','circle §10, framed Après, underlined permanence phrase','drawing described in a note, underline omitted','circle, framed note and underline reproduced','nine_ten: circle surrounds only §10; Après §12 ?? is in a separate pencil frame; the two-line permanence phrase has a separate rule.',ac=False,k='drawing or diagram')
a('§10 first excellent',r'\unsure{excellent|excellents}','excellents','excellent','note10_upright: terminal t and its crossing stroke are visible; no s follows before sur S. Singular form retained.',k='misread word')
a('§10 margin second-line subject',r'\unsure{morphismes|impliquent}','morphismes','morphismes','note10_upright: initial m humps, round o, descending p, tall h and following low waves can be traced. No initial dotted i corresponding to impliquent.','medium',ah=False)
a('§10 second excellent','excellent','excellents','excellent','note10_upright: the second ending also stops at t, without a separate s.',ac=False,k='misread word')
a('§10 margin layout and underline','braced three lines; excellent underlined','inline with semicolon, no underline','braced three lines; excellent underlined','note10_upright: brace at left, first excellent underlined, second phrase below, ?? on a separate third line; no semicolon written.',ac=False,k='insertion or placement')
a('§11 old number',r'\unsure{10|11}','10',r'\unsure{10|11}','num11: dense black crossing hides the older digits; only portions of two upright/rounded bodies survive.','low',False,True)
a('§11 margin first words',r'\unsure{Commun au|Convient au}','Comme cas','Commun au','margin11full_upright: C followed by rounded o and repeated humps, then separate a/u. No dotted i or crossed t for Convient; no second c for cas.','medium',k='misread word')
a('§11 margin second-line abbreviation',r'\unsure{par.}',r'\ill{}',r'\unsure{par.}','margin11full_upright: a long p descender and small joined following strokes survive; the abbreviation remains uncertain.','low',False,True,'readable ink left as \\ill{}','yes')
a('§11 margin second-line last unit',r'\unsure{20|éd}',r'\ill{}',r'\unsure{20|2e|éd}','margin11full_upright: first curved closed/open form and second small loop with a raised mark remain ambiguous; the whole note is framed and has its own question mark.','low',True,True,'readable ink left as \\ill{}','yes')
a('§11 note frame and line','framed note without connection','parenthetical text and descriptive note','framed note connected to circled §11','whole/eleven/margin11full_upright: a short sloping line joins the circle around §11 to the left edge of the note’s frame. There is no direct line from §11 to §10; the separate long left arrow runs from §8 toward §9.',k='drawing or diagram')
a('§11 quotation marks','double quotes around élémentaires','no quotes','double quotes','elementaires: paired short quotation strokes flank the word; the lines underneath belong to the Roman numerals, not an underline of élémentaires.',ac=False,k='omission')
a('§11 type article',r'\unsure{des|du}','du','du','article11/elementaires: d loop/ascender and one attached u-shaped low continuation, without separate e/s.',ah=False)
a('§11 product old index',r'\deleted{\unsure{X}}Y/S','Y/S with old X described in note',r'\deleted{X}Y/S','prod: crossed diagonal strokes of the old X remain below the live Y; the reading is from this crop, without using the later sheet cited by H.','medium',k='omission')
a('§11 SGAD reference rules','VIII and XI overlined and underlined','VIII and XI without rules','VIII and XI overlined and underlined','elementaires/eleven: each Roman numeral has a separate horizontal stroke above and below.',ac=False,k='omission')
a('§8 new number',r'\unsure{8}','8','8','num8: two separate enclosed loops make the live numeral 8 clear.',ah=False)
a('§8 old number',r'\deleted{\unsure{1|11}}','old number left untranscribed',r'\deleted{\unsure{1|11}}','num8: a tall surviving upright with a lower foot stands to the right of 8; overprinting leaves 1/11 unresolved.','low',False,True,'omission')
a('§8 frame and arrow','frame and arrow to §9','drawing described in note','frame and arrow to §9','whole/nine_ten/num8: the long curve starts at the upper left of the §8 box and terminates with an arrowhead above §9, passing left of the other numbered circles.',ac=False,k='drawing or diagram')
a('§12 cancelled Représentabilité',r'\unsure{Représentabilité}','Représentabilité',r'\unsure{Représentabilité}','last12: the tall initial R and several later ascenders are visible, but black cancellation merges the small letters; C doubt retained.','low',False,True)
a('§12 short repr.',r'\unsure{repr.}','représ.',r'\unsure{repr.}','last12: short r/e bodies precede p and a small terminal curl/point; a fully written és is not visible.','low',False,True,'abbreviation expanded or spelling modernised')
a('§12 interlined modifier',r'\inserted{\unsure{séparés|xprés}}','représ. described above repr.',r'\inserted{\uline{\unsure{séparés|xprés}}}','last12: the short form lies above the gap after morphismes and is underlined, with a downward curve toward that gap, not above repr. The opening crossed strokes and compressed ending remain uncertain.','low',True,True,'insertion or placement',con='The interlined modifier belongs after morphismes; H attaches it to the earlier abbreviation.')
a('§12 abbreviation after loc.',r'\unsure{pres.}','pr.','pr.','last12: a p descender, short r shoulder and separate point are visible; no written es follows.','medium',ah=False)
a('§12 final short form',r'\unsure{fi|finie}','f.',r'\unsure{f|fi}','last12end: long f loop and mid-height bar, with a small point above the bar; a separate i body is not clear, and no letters nie or baseline full stop are visible.','low',k='abbreviation expanded or spelling modernised')
a('§13 raised short ending',r'\unsure{th\textsuperscript{es}|th\textsuperscript{s}}','ths',r'\unsure{th\textsuperscript{es}|th\textsuperscript{s}}','ths: a small raised curved stroke and point follow th; e/s separation remains unresolved.','low',False,True,'other')
a('§13 de state','cancelled de','live de','cancelled de','last13_upright/last13tail: a heavy horizontal strike crosses the small de between the abbreviation and représentabilité.',ac=False,k='deletion state (struck given live or live given struck)')
a('§13 second opening parenthesis',r'\unsure{(}pour',r'\uncertain{pour}',r'\unsure{(}pour','last13tail: two long neighbouring strokes precede the ou/r; one can be a separate parenthesis, but overlap with the p prevents certainty.','low',False,True,'omission','yes')
a('§13 short form after les',r'\unsure{esp.|es}','omitted','es','last13tail: a small e-like loop and terminal s hook occur between les and the tall f of foncteurs; no separate p descender or abbreviation point.','medium',k='omission')
a('§13 final punctuation',r'\unsure{,|)}',')',r'\unsure{,|)}','last13tail: after the dots a detached diagonal stroke descends toward the sheet edge; its short visible part does not settle comma versus closing parenthesis.','low',False,True,'misread symbol or index')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','top','A) Descente et passage au quotient, underlined')
i('text','§1','Descente fidèlement plate')
i('text','§2','Topologies sur (Sch)/S. Propriétés générales des foncteurs sur (Sch)/S.')
i('deletion','§2 under and right of replacement','Passage au/aux quoti... Généralités sur les foncteurs sur (Sch)/S')
i('insertion','§2 above/below cancelled line','Topologies... foncteurs sur (Sch)/S')
i('margin note','right of §2','[Intervertir underlined 1 et underlined 2 ??]')
i('text','§3','Passage au quotient plat.')
i('text','§4','Descente non plate [Application... Ram. Samuel généralisé...')
i('insertion','under §4','Appl. à platitude d’une adh. schématique et lemme de Hironaka.')
i('deletion','§4 Hironaka initial','uncertain old H')
i('text','§5','Passage au quotient non plat. [Passage aux quots en gén]')
i('text','§6','Descente de schémas, relatifs étales, four dashes')
i('text','below §6','[Év/Éu raised t. descente des faisceaux étales ?? ...]')
i('deletion','inside §6 bracket','uncertain morphismes')
i('insertion','above old morphismes','faisceaux')
i('text','middle','B)')
i('deletion','old B heading','Propriétés générales des foncteurs sur (Sch)/S, underlined')
i('drawing','replacement B heading','Méthodes; non projectives; oval de construction with angular arrow after Méthodes; underline')
i('insertion','B heading oval','de construction')
i('deletion','left of replacement B heading','§7')
i('deletion','boxed old §7 paragraph','Propriétés générales de/des foncteurs, et propriétés de permanence')
i('insertion','above old §7 paragraph','cancelled uncertain diverses')
i('drawing','around old §7 paragraph','stepped enclosing and cancelling lines')
i('text','new §7','underlined Proreprésentabilité: (et variantes).')
i('text','§9','underlined Invariants différentiels; inserted underlined tangts et normaux')
i('deletion','§9 number and phrase','old 8; de/du div.')
i('insertion','above cancelled de/du div.','tangts/tang. et normaux')
i('drawing','§10','circle around §10')
i('margin note','above §10','framed Après §12 ??')
i('text','§10','Propriétés générales de foncteurs, underlined propriétés de permanence')
i('margin note','right of §10','brace: Foncteurs excellent sur S; morphismes excellent; ??')
i('drawing','§11 number and note','circle around old number and live 11, connected to framed slanted note')
i('deletion','§11 number','old 10/11')
i('margin note','above §11 phrase','Commun au par. 20/2e/éd ? Cas Greenberg ?')
i('text','§11','Représentabilités double-quoted élémentaires du type product X/Y')
i('deletion','product lower index','old X overwritten by Y')
i('insertion','below §11 phrase','cf SGAD barred VIII 6 et barred XI 6.8.')
i('drawing','§8 and left margin','framed §8 with cancelled old 1/11; long arrow to §9')
i('text','§8','Construction de Modules cohérents')
i('text','§12','Foncteurs repr. par morphismes séparés/xprés loc. pr. f/fi')
i('deletion','start of §12','Représentabilité')
i('insertion','above old Représentabilité','Foncteurs')
i('insertion','after morphismes in §12','underlined séparés/xprés')
i('text','§13 and final line','Applications : des th raised es/s de représentabilité relatifs. (y compris (pour les es foncteurs étales...)')
i('deletion','§13 before représentabilité','de')
commit(26,3,dict(text=T,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole and both supplied halves viewed before C/H; all agreed text read visually. Dense revised handwritten plan with darker ink, blue additions and pencil circles/boxes. Every C doubt and C/H difference enlarged; slanted notes rotated in margin11full_upright, note10_upright and last13_upright. All category/product letters read from this page; later sheet cited in H was not used. Diagram geometry reproduces separate circled §10/§11, §11-to-note line and §8-to-§9 arrow, not H’s inferred links among all numbers. Heading and old paragraph drawing coordinates approximate shape and relative placement, without adding semantic arrows. Archive pencil2 comment only. No watermark reading added. Context remains unopened.'))
