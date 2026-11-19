from work import *
c,h=witnesses(2)
t=r'''\cotefile{156-3}
\scanpage{2}
\mspage{1}

\uline{Réseaux}\ldots\ via découpages.

(8 Juin 86)

% slanted; within the drawn corner enclosure
\margin{GF\,\uline{III}}

% slanted
\margin{\deleted{Ensembles} Parties \unsure{finies} de lieux \unsure{modérés|modérées}}

Je voudrais définir une autre axiomatique des \deleted{réseaux,}
\deleted{\unsure{l}}\unsure{la|a} structures de réseaux
sur un ens. $\mathcal L$ (\deleted{\unsure{d}}ens. des ``lieux'').

\textcircled{\scriptsize a}\quad $S_0\deleted{\unsure{(L)|L}}\subset P_2(L)$ l'ens des \uline{0-sphères}
\uline{plongées}, ou des \uline{paires} \deleted{\unsure{mod.}} (de
lieux) modérées. \inserted{si $\{a,b\}\in S_0$ ; on dit aussi que $a,b$ st \uline{disjoints} ou en position relative modérée.}

% slanted
\margin{Mais, on dit aussi que $a,b$ en position rel. modérée si $a=b$ \uline{ou} $\{a,b\}\in S_0$}

[En termes de l'axiomatique par les segments,
\unsure{cela|celà} signifie que \deleted{$a,b$ \unsure{sont} ou bien} \inserted{(à part $a,b$ \uline{distincts}},
\unsure{contenu} dans $\{a,b\}\in\deleted{\unsure{S_0}}P_2(\mathcal L)$, que
ou bien $\{a,b\}\cap\mathcal L_s\ne\varnothing$ ($a$ ou $b$ est un
nœud \unsure{sg$_r$|sg} du réseau) \uline{ou} \uline{bien} \deleted{$a,b$}
(si \deleted{\unsure{st|sont}} \inserted{$a,b$} réguliers) que $a,b$ \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient} :
des lignes différentes, \unsure{soit|sont}, s'ils sont
dans une $\bar{=}$ ligne, que $\{a,b\}=\partial I$,
pour $I\in S$].

\deleted{\unsure{b)}} Une partie \uline{finie} \inserted{$T$} est dite \deleted{admissible} \inserted{``\uline{modérée}''}
si \deleted{$\forall\,a,b\in T$, \unsure{on a} $a,b$} $P_2(T)\subset S_0$
i.e. deux éléments quelc. de $T$ sont en
position relative modérée (\deleted{des} 2 à 2 ``disjoints'').

% paper watermark; faint outline impression
\rotatebox{90}{\textsc{\unsure{xtra Strong Ext}}}
'''
R=[]
def a(*args,**kw):R.append(row(*args,**kw))
a('title punctuation',r'\unsure{\ldots}','no dots',r'\ldots','Three separated rising pen dots after Réseaux.','002_header.jpg','omission')
a('upper-right enclosure',r'\unsure{CF|CH|Cf|Ch}','GF III','GF III','Rotated enlargement shows the inward foot of G, two strokes of F and three uprights.','002_corner.jpg','other',C=True,H=False)
a('slanted upper-left note',r'\deleted{\unsure{Les ensembles}} \unsure{Parties|Ensembles} \deleted{\unsure{des}} de lieux \unsure{modérés|modérées}',r'\struck{\ill{}}',r'\deleted{Ensembles} Parties \unsure{finies} de lieux \unsure{modérés|modérées}','The crossed top word begins with a large E; below it Parties and lieux are live. The short intervening word has a tall loop but is still uncertain.','002_margin_top.jpg','readable ink left as \\ill{}','medium',marked=True)
a('opening: des',r'\deleted{des réseaux,}','des \\struck{réseaux,}','des \\deleted{réseaux,}','The cancellation begins at réseaux; the left-hand des has no line through it.','002_opening.jpg','deletion state',H=False)
a('opening: revised article and noun',r'\deleted{\unsure{l}}la structure de réseaux',r'\struck{\ill{}} structures de réseau',r'\deleted{\unsure{l}}\unsure{la|a} structures de réseaux','A dense overwritten upright precedes a separate a; the terminal strokes of structures and réseaux are present. The overwritten article cannot be settled.','002_opening.jpg','misread word','medium',marked=True)
a('opening set letter',r'\unsure{\mathcal L|L}',r'\mathcal L',r'\mathcal L','A looped lower sweep crosses the rising stroke; not the angular L in the next line.','002_opening.jpg','misread symbol or index',H=False)
a('ens. parenthesis',r'\deleted{\unsure{d}}ens.',r'ens.',r'\deleted{\unsure{d}}ens.','A small heavy overwritten ascender stands at the start of ens.; retain C’s uncertainty about the underlying letter.','002_opening.jpg','omission','medium',C=False)
a('(a) initial set symbols',r'S_0\deleted{\unsure{(L)|L}}\subset\unsure{P|\mathcal P}_2(L)',r'\mathfrak S_0\struck{\ill{}}\subset\mathfrak P_2(\mathcal L)',r'S_0\deleted{\unsure{(L)|L}}\subset P_2(L)','Plain rounded S; P has one staff and an angular bowl; argument L is a plain right angle. The crossed parenthetic letter remains uncertain.','002_a.jpg','misread symbol or index','medium',marked=True)
a('(a) l’ens',r'\unsure{l\x27ens}',"l'ens.","l'ens",'The small l and apostrophe are visible; no separate period after ens.','002_a.jpg','other')
a('(a) plongées',r'\uline{plongées}',r'\struck{plongées}',r'\uline{plongées}','Horizontal line lies below the baseline, crossing only the descending g loop; the word remains live.','002_a.jpg','deletion state',C=False)
a('(a) ou des paires',r'ou des \uline{paires}',r'ou \uncertain{des} \struck{paires}',r'ou des \uline{paires}','Des is readable; the horizontal line is below paires rather than through its letter bodies.','002_a.jpg','deletion state',C=False,marked=True)
a('(a) cancelled mod.',r'\deleted{\unsure{mod.}}',r'\struck{\ill{}}',r'\deleted{\unsure{mod.}}','The crossed word has an initial low wave and final tall stem; mod. remains a plausible but unresolved reading.','002_a.jpg','readable ink left as \\ill{}','low',C=False,marked=True)
a('(a) interlinear definition',r'si {a,b}∈S_0 ; on dit aussi que a,b \unsure{st} disjoints ou en position relative \unsure{modérée}',r'Si {a,b}∈S_0, on dit \struck{\ill{}} que a,b sont disjoints ou en position relative modérée',r'si {a,b}∈S_0 ; on dit aussi que a,b st disjoints ou en position relative modérée','The added text has a semicolon, a live aussi and the abbreviated st; no line cancels aussi.','002_a.jpg','abbreviation expanded or spelling modernised',marked=True)
a('slanted middle margin',r'Mais, \unsure{on} dit aussi que a,b en position rel. modérée si a=b ou {a,b}∈S_0',r'Mais on dit \uncertain{aussi} que a,b \uncertain{sont en} position rel. modérée si a=b ou {a,b}∈S_0',r'Mais, on dit aussi que a,b en position rel. modérée si a=b ou {a,b}∈S_0','Rotated note has a short on after the comma; between b and position there is en, without a separate sont.','002_margin_mid.jpg','text not on the page','medium',marked=True)
a('segment paragraph: cela',r'cel\unsure{a|à|}','cela',r'\unsure{cela|celà}','Final a is compressed and a detached accent cannot be securely distinguished from the preceding ink. Empty alternative removed, ambiguity retained.','002_segments.jpg','other','medium',H=False)
a('segment paragraph: cancellation and insertion',r'\deleted{a,b \unsure{sont} ou bien} \inserted{(à \unsure{part} a,b distincts}',r'\struck{(c’est-à-dire a,b distincts, a,b \ill{} ou bien)}',r'\deleted{a,b \unsure{sont} ou bien} \inserted{(à part a,b distincts}','Upper à part a,b distincts is live above the ruled-through line; the letters are not c’est-à-dire.','002_segments.jpg','deletion state','medium',marked=True)
a('segment paragraph: contenu dans',r'\unsure{contenu} dans',r'\ill{} que',r'\unsure{contenu} dans','Second word has a tall d and a final wave; first word is still not entirely resolved.','002_segments.jpg','readable ink left as \\ill{}','medium',C=False,marked=True)
a('segment paragraph: overwritten P',r'\in\deleted{\unsure{S_0}}P_2(\mathcal L)',r'\in\mathfrak P_2(\mathcal L)',r'\in\deleted{\unsure{S_0}}P_2(\mathcal L)','A looped cancelled form lies over the upright P; cannot settle its underlying subscript.','002_segments.jpg','omission','medium',C=False)
a('segment paragraph: intersection',r'\{a\unsure{;|,}b\}\cap\mathcal L_s',r'\{a,b\}\cap\mathcal L_S',r'\{a,b\}\cap\mathcal L_s','Comma is a short descending mark; subscript is small lower-case s, not an enlarged capital.','002_segments.jpg','misread symbol or index')
a('segment paragraph: nœud qualifier',r'nœud \unsure{sg$_r$|sg} du réseau',r'\uncertain{nœud} du réseau',r'nœud \unsure{sg$_r$|sg} du réseau','Nœud is followed by two compact strokes with a possible lowered r; the qualifier is present but unresolved.','002_segments.jpg','omission','medium',C=False,marked=True)
a('segment paragraph: regular lieux and placement',r'\uline{ou} \uline{bien} \deleted{a,b} (si \deleted{\unsure{st|sont}} \inserted{a,b} réguliers) que a,b \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient}',r'ou bien \add{dit} a,b (si a,b \struck{sont} \uncertain{lignes}) \ill{}',r'\uline{ou} \uline{bien} \deleted{a,b} (si \deleted{\unsure{st|sont}} \inserted{a,b} réguliers) que a,b \inserted{\unsure{doivt|doit}} \unsure{appartiennent|appartient}','The crossed a,b follows bien; réguliers has its descending g. The raised short verb belongs before appartiennent, whose ending remains compressed.','002_segments.jpg','insertion or placement','medium',C=False,marked=True)
a('segment paragraph: alternatives',r'des lignes différentes, \unsure{soit|sont|sauf}',r'\uncertain{sur des} lignes différentes, sont',r'des lignes différentes, \unsure{soit|sont}','The line begins des, without sur; after the comma no f descender supports sauf. Soit/sont remains unresolved.','002_segments.jpg','misread word','medium',marked=True)
a('segment paragraph: same-line shorthand',r'dans une $\unsure{\bar{=}|=}$ ligne, \unsure{pour|que}',r'\uncertain{sur une même} ligne, \ill{}',r'dans une $\bar{=}$ ligne, que','Dans is visible; the same-line mark consists of three horizontal strokes. Following word has q descender and closed ue.','002_segments.jpg','readable ink left as \\ill{}','medium',marked=True)
a('final paragraph: label',r'\deleted{\unsure{b)}}','(b)',r'\deleted{\unsure{b)}}','The circled label is heavily scribbled through; it is not a live (b).','002_b.jpg','deletion state','medium',C=False)
a('final paragraph: T and admissible',r'\inserted{T} ... \deleted{\unsure{admissible}} \inserted{modérée}',r'T ... modérée \struck{\ill{}}',r'\inserted{T} ... \deleted{admissible} \inserted{modérée}','T sits above the line with an insertion stroke; admissible is crossed below the added quoted modérée.','002_b.jpg','readable ink left as \\ill{}','medium',marked=True)
a('final paragraph: cancelled quantifier',r'\deleted{∀a,b∈T, \unsure{on a} \unsure{a,b}}',r'\struck{∀a,b∈T,\ill{}}',r'\deleted{∀a,b∈T, \unsure{on a} a,b}','After on a two variable strokes a,b are visible under the long cancellation; on a itself remains obscured.','002_b.jpg','readable ink left as \\ill{}','medium',marked=True)
a('final paragraph: P₂(T)',r'P_2(T)\subset S_0',r'\mathfrak P_2(T)\subset\mathfrak S_0',r'P_2(T)\subset S_0','Same single-staff angular P and rounded plain S as in (a).','002_b.jpg','misread symbol or index',C=False)
a('final paragraph: éléments',r'\unsure{éléments|élémts|elements}','éléments','éléments','The extended letter group contains the intervening en and final ts; an acute stroke is visible.','002_b.jpg','other',H=False)
a('final paragraph: pairwise shorthand',r'(\deleted{\unsure{des}} \unsure{2 st|sont} ``disjoints\x27\x27)',r'(\uncertain{sont} 2 à 2 « disjoints »)',r'(\deleted{des} 2 à 2 ``disjoints\x27\x27)','There is a dark cancelled des and then 2 à 2; there is no live sont before the figures. Double pen quotes flank disjoints.','002_b.jpg','deletion state','medium',marked=True)
a('paper watermark',r'\unsure{x}tra Strong Ext','omitted',r'\unsure{xtra Strong Ext}','Faint outline impression is much less legible in these derivative JPEGs than the pen text. Keep the full C candidate doubtful rather than certify the previously unmarked letters.','002_watermark.jpg','omission','low')
blocks=[('text','top','Réseaux… via découpages. (8 Juin 86)'),('text','upper body','Je voudrais définir une autre axiomatique'),('text','(a)','S_0 ⊂ P_2(L) l’ens des 0-sphères'),('text','middle','En termes de l’axiomatique par les segments'),('text','bottom','Une partie finie T est dite'),('text','paper background','xtra Strong Ext (uncertain watermark)')]
d=['Title dots resolved; corner initials resolved to GF by the rotated crop.','Upper-left: Les removed from the crossed word; Ensembles and Parties resolved; finies remains uncertain; modérés/modérées retained.','Opening: the overwritten l and d remain uncertain; L resolved as looped script; revised article marked la/a.','(a): crossed (L)/L retained; P resolved as plain P; l’ens, st and modérée resolved; crossed mod. retained.','Middle margin on resolved.','cela/celà remains uncertain; crossed sont retained; part resolved; contenu retained; underlying S_0 retained.','Comma in {a,b} resolved; sg_r/sg retained; crossed st/sont, inserted doivt/doit and appartiennent/appartient retained.','soit/sont retained with unsupported sauf dropped; three-stroke same-line sign and que resolved.','Crossed label b) retained; admissible resolved; crossed on a retained; a,b and éléments resolved; crossed des and 2 à 2 resolved.','Watermark uncertainty extended to its entire faint reading.']
save(2,t,R,blocks,d,'Whole image and both supplied halves read. Enlargements include all difficult deletions, the mathematical bracketed paragraph, and both slanted margins rotated upright. The wording is preserved even where the revision leaves a defective construction.')
(OUT/'records/notation.md').write_text(r'''# Notation and remaining doubts

## Notation table

| Sign / usage | Reading | Image evidence | Alternatives / limits |
|---|---|---|---|
| Set of lieux | $\mathcal L$ or $L$ as locally drawn | Scan 2 opening has a looped lower stroke; argument of the first $P_2$ is angular L | Do not replace every L by script automatically |
| Pairs and 0-spheres | $P_2$, $S_0$ | Scan 2 (a) and final paragraph; single-staff angular P, rounded plain S | H’s Gothic letters are not supported by these forms |
| Boundary | $\partial I$ | Scan 2 bracketed paragraph; curved partial followed by capital I | Different from later dotted frontier |
| Same / même shorthand | $\bar{=}$ | Scan 2 lower paragraph: three horizontal strokes | Preserve symbol, do not expand to même |
| Quotes | two backticks and two apostrophes | Scan 2 lieux, modérée, disjoints | Do not substitute guillemets |
| Underline / deletion | below baseline / through letter bodies | Scan 2 plongées and paires are underlined; réseaux is struck | Descenders can cross an underline without cancelling the word |
''')
(OUT/'records/abbreviations.md').write_text('ens. / l’ens — ensemble; rel. — relative; st — sont; quelc. — quelconques; i.e. — id est; mod. — modérée (when the cancelled word is so read); doivt — doivent (uncertain inserted abbreviation).\n')
rebuild()
