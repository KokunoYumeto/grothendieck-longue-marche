from pathlib import Path
import csv, json, os

ROOT=Path('/workspace/scratch/b12af914b284')
OUT=ROOT/'edition/reader_returns'
index=json.loads((ROOT/'edition/scripts/150_scan067_crop_index.json').read_text())
boxes=index['crops']
boxes['p24_isolated']=[625,1225,730,1310]

edge=r'''\margin{\figure{\begin{tikzpicture}[x=1mm,y=1mm]
% Unassigned thin broken stroke at the right paper edge; provenance uncertain.
\draw[black!55,line width=.2pt] (0,0)--(.8,.15);
\draw[line width=.23pt] (1.1,.18)--(2.3,.3);
\draw[line width=.23pt] (2.6,.32)--(4.6,.5);
\draw[line width=.23pt] (4.9,.53)--(6.9,.72);
\draw[line width=.23pt] (7.1,.74)--(9.5,.95);
\end{tikzpicture}}}'''

margin=r'''\margin{On voudra que de $=$ les $\Sigma_{ij}$ soient des variétés à bord, que le
bord soit la réunion des $\Sigma_{kij}$ et $\Sigma_{ikj}$ --- mais
c'est sans doute une conséquence de la condition précédente..-}'''

source_map=r'\unsure{\Sigma_{ik}|\Sigma_{i\deleted{j}k}|\Sigma_{ij}}'
Imark=r'\unsure{I_{(\deleted{\unsure{0}}\uline{\Sigma})}|I(\deleted{\unsure{0}}\uline{\Sigma})|I_{(0)}}'
compo=r'\unsure{\text{cpl.}|\text{compl.}}'

cases=r'''\uline{Cas équisingulier} : les $s_{ij}$ sont fibrants propres

\uline{Cas non singulier} : les $\Sigma_i$ sont des variétés
% The dotted i in this first Sigma subscript is locally reworked;
% no independently recoverable underlying letter is supplied.
topologiques\unsure{,|;} le bord de $\Sigma_i$ est la réunion
% The comma is clear; a tiny separate point above it has uncertain attachment
% and provenance, so the semicolon alternative remains local and explicit.
des $\Sigma_{ji}$ pour $j<i$ \deleted{(NB il suffit
de prendre pour $j$}
''' + margin + r'''

\uline{Cas} \uline{équisingulier}-\uline{non singulier}
$s_{ij}:''' + source_map + r'''\longrightarrow\Sigma_j$ est
% The source's upper k-like form lies over a long hooked lower trace.
% Alternatives retain both the literal ik and an uncertain overwritten j layer.
une fibration propre, à fibres des variétés
''' + edge + r'''
à bord, le fibré des bords est réunion
des $\Sigma_{ijk}$ pour $i<\deleted{\unsure{j}}\inserted{j}<k$.
% The cancelled central glyph lies below/through the higher rewritten j;
% the older glyph's reading as j is tentative, not a recovered certainty.
'''

definition=r'''\diagram{\begin{tikzcd}[column sep=5mm,arrows={line width=.6pt},execute at end picture={
% The lower connector ends in the observed dense short upright/stub.
\fill ([xshift=-2.8pt,yshift=-1.35pt]s67pairtarget.west) --
([xshift=-1.4pt,yshift=-2.2pt]s67pairtarget.west) --
([xshift=-1.8pt,yshift=-3.5pt]s67pairtarget.west) --
([xshift=-3.0pt,yshift=-3.2pt]s67pairtarget.west) -- cycle;
}]
{\uline{\Sigma}=(\Sigma_{(0)}=\operatorname{Ob}(\uline{\Sigma}),\quad\Sigma_{(1)}=\operatorname{Fl}(\uline{\Sigma}),}
& \Sigma_{(1)}\arrow[r,shift left=2.5,"\uline{s}"]\arrow[r,shift right=2.5,dash,"\uline{b}"',end anchor=west,shorten >=2pt]
& |[alias=s67pairtarget]|\Sigma_{(0)},
\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=10mm,arrows={line width=.6pt},execute at end picture={
% Definition connector: the upper bar is shorter and detached from the
% lower shaft's single right head.  Two dark points below it remain unassigned.
\draw[->,line width=.75pt,line cap=round] ([xshift=2pt,yshift=-1pt]s67product.east) -- ([xshift=-2pt,yshift=-1pt]s67two.west);
\draw[line width=.55pt,line cap=round] ([xshift=2pt,yshift=3pt]s67product.east) -- ([xshift=-5pt,yshift=3pt]s67two.west);
\fill ([xshift=-7pt,yshift=-5pt]s67two.west) circle[radius=.27pt];
\fill ([xshift=-7.7pt,yshift=-6.5pt]s67two.west) circle[radius=.23pt];
}]
|[alias=s67product]|(\Sigma_{(1)},b)\times_{\Sigma_{(0)}}(\Sigma_{(\unsure{1})},s)\arrow[r,phantom,"\text{déf}"]
& |[alias=s67two]|\Sigma_{(2)}\arrow[r,"''' + compo + r'''","\substack{\text{comp.}\\\text{des flèches}}"']
& \Sigma_{(1)}
\end{tikzcd}}
), et supposons
'''

bottom=r'''\diagram{\begin{tikzcd}[column sep=15mm,row sep=9mm,arrows={line width=.6pt},execute at end picture={
% A central thickening/possible earlier head remains on the extended shaft.
\path (s67lastsource.east) -- coordinate[pos=.52] (s67shaftmid) (s67lasttop.west);
\fill ([xshift=-2.7pt,yshift=.6pt]s67shaftmid) --
([xshift=-.6pt,yshift=1.0pt]s67shaftmid) --
([xshift=1.3pt]s67shaftmid) --
([xshift=-.6pt,yshift=-.9pt]s67shaftmid) --
([xshift=-2.7pt,yshift=-.5pt]s67shaftmid) -- cycle;
% Vertical marker: a reworked wavy left component and a straight right
% upright, placed under the left part of the target.  No vertical arrow supplied.
\draw[line width=.7pt,line cap=round] ([xshift=8.5pt,yshift=-2pt]s67lasttop.south west)
.. controls +(2pt,-.2pt) and +(.3pt,1pt) .. ([xshift=10pt,yshift=-4.7pt]s67lasttop.south west)
.. controls +(-.6pt,-1.4pt) and +(.7pt,-1pt) .. ([xshift=8.7pt,yshift=-3.6pt]s67lasttop.south west)
.. controls +(.4pt,-2pt) and +(-.4pt,0pt) .. ([xshift=10.2pt,yshift=-5.6pt]s67lasttop.south west);
\draw[line width=.65pt,line cap=round] ([xshift=11.6pt,yshift=-2pt]s67lasttop.south west) -- ([xshift=12.2pt,yshift=-5.7pt]s67lasttop.south west);
}]
|[alias=s67lastsource]|\pi_0(\Sigma_{(1)})\arrow[r,"{\pi_0(\uline{s},\uline{b})}"]
& |[alias=s67lasttop]|\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})\\
&\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})
\end{tikzcd}}'''

lower=r'''$\Sigma,\Sigma^{\unsure{*|<}}(1)\subset\Sigma\times\unsure{\Sigma|\overline{\Sigma}}$, sans donnée de $I$. Plus
% The last Sigma has a detached upper bar.  The four-stroke construction
% favours a pen-lift within Sigma; an additional overline remains an alternative.
généralement, considérons une \uline{catégorie topologique}
''' + definition + r'''que $\uline{s}:\Sigma_{(1)}\unsure{\longrightarrow|-}\Sigma_{(0)}$ soit \uline{fibrant}. Je dis
% The short filled terminal of this shaft is pointed but densely inked.
qu'alors $\pi_0(\Sigma_{(0)})='''+Imark+r'''$ est \uline{un ens. }\inserted{pré\deleted{\unsure{filtré}}}\uline{ordonné},
% The I expression has a compact, lowered-looking parenthesised overwork:
% a Sigma-like form and zero-like residual loops.  Both layer and vertical
% placement remain uncertain in the explicit alternatives.
% Live pré lies to the left of the crossed interlinear filtré candidate;
% the common curved leader enters before the live baseline ordonné.
% The continuous baseline underline spans un ens. and ordonné.
en prenant comme graphe de la relation
d'ordre l'image de
''' + bottom + '\n'

opening=r'''Enfin, la condition d) signifie que cette structure
\inserted{d'espace top. ordonné}
% The initial d is reworked but live.  The parenthesis-like curve before
% satisfait belongs to the continuous insertion leader beneath ordonné.
satisfait la condition c) du Scholie (p. $27$).
'''
heading=r'''13. \uline{Une digression} Revenons au cas de
'''
tex=r'''\scanpage{67}
\mspage{29}
'''+opening+'\n'+cases+'\n'+heading+lower+r'''% Pale bottom-left foliation in another hand.
\margin{66}
'''

changes=[]
def ch(place,C,H,final,aC,aH,kind,cat,conf,crop,evidence,marked=False,consequence=''):
    changes.append(dict(id=f'067-{len(changes)+1:02}',place=place,C=C,H=H,final=final,against_C=aC,against_H=aH,kind=kind,error_category=cat,marked_in_H=marked,confidence=conf,evidence=evidence,crop=f'crops/150_scan067_{crop}.png',box=boxes[crop],mathematical_consequence=consequence))
ch('opening, before satisfait','(satisfait','(satisfait','satisfait',True,True,'insertion or placement','Insertions put in the wrong place','high','p01_openinsertion','The apparent opening parenthesis is the left bend of the continuous leader running below the inserted words; no independent text parenthesis is present there.')
ch('opening reference ending','(p. $27$).','(p.~27)).','(p. $27$).',False,True,'text not on the page','Text that is not on the page','high','p02_reference','The source has a single closing parenthesis after the digits 2 and 7, then a separate full stop.')
ch('Cas non singulier, after topologiques','topologiques;','topologiques,',r'topologiques\unsure{,|;}',True,False,'misread symbol or index','Symbols and indices','low','p04_topologiques','The curved comma is clear. A tiny separate dark point lies above it near source (750,613); its attachment to the punctuation and its provenance are uncertain. Comma leads, while a semicolon remains explicit because of that point.')
ch('cancelled NB clause','il suffit','il en suffit','il suffit',False,True,'misread word','Words','high','p05_cancelNB','The dotted i and looped l are followed by a short low movement into the beginning of suffit before the tall ff strokes. No separate e/n group is recoverable; the rereading supports il suffit.')
ch('second cancelled line','de prendre pour j',r'\ill{}','de prendre pour $j$',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','medium','p06_cancelnext','The initial de loop, long p descender of prendre, low intervening strokes, second p and the final long hooked j remain readable beneath the horizontal strike.',True)
ch('margin, after On voudra que','les', 'les',r'de $=$ les',True,True,'omission','Omissions','high','p07_margin','Before les are a separate de group and a two-stroke horizontal equality-like shorthand. Both strokes are visible in the rotated crop; the words are not expanded in the transcription.',True)
ch('margin, after à bord,','que le bord soit','par', 'que le bord soit',False,True,'misread word','Words','high','p07_margin','The upper line ends que le; the next starts bord soit. The looped q, following ue, separate le, and the two live words on the next line are legible.',True)
ch('margin, second Sigma term',r'et $\Sigma_{ikj}$ ---',r'\ldots',r'et $\Sigma_{ikj}$ ---',False,True,'omission','Omissions','high','p07_margin','A live et and a second Sigma with consecutive i, k and long-descending j stand after Sigma_kij, followed by one dash. The long j descender crosses the later word doute without cancelling it.',True,'The manuscript’s second indexed Sigma term is restored.')
ch('margin, after mais',"c'est sans doute une conséquence de",r'\ill{} des',"c'est sans doute une conséquence de",False,True,r'readable ink left as \ill{}','Readable ink left as illegible','high','p07_margin','c’est sans doute une is written on one oblique baseline; conséquence de continues below. Their letter groups are readable. The dense crossing near doute is the preceding j descender.',True)
ch('margin ending words','la condition précédente',r'conditions \ill{}','la condition précédente',False,True,'misread word','Words','high','p07_margin','The separate article la and singular condition are followed by the legible accented précédente on the last line.',True)
ch('margin continuation marks',r'\ldots',r'\ldots','..-',True,True,'misread symbol or index','Symbols and indices','high','p07_margin','After précédente are exactly two small points followed by a short horizontal stroke.',True)
ch('combined-case heading, underline spans',r'\uline{Cas équisingulier-non singulier}',r'\emph{Cas équisingulier-non singulier}',r'\uline{Cas} \uline{équisingulier}-\uline{non singulier}',True,True,'other','Other','high','p08_headingmap','The source has three separated underline strokes, beneath Cas, équisingulier, and non singulier; the interword gaps and joining hyphen are outside those strokes.')
ch('combined-case map, source',r'\Sigma_{ik}',r'\Sigma_{ij}',source_map,False,True,'misread symbol or index','Symbols and indices','low','p08_headingmap','The upper right index form has a visible k-like stem and branches over a long hooked lower trace. Literal ik leads, an overwritten j-to-k layer remains possible, and ij is retained as the alternative witness reading.',True,'The source’s reworked index remains explicit rather than being reassigned by the expected map.')
ch('combined-case map, target M0611',r'\unsure{\Sigma_i|\Sigma_j}',r'\Sigma_i',r'\Sigma_j',True,True,'misread symbol or index','Symbols and indices','high','p08_headingmap','The target index has a separate dot, a long descending stem and a low left hook. Dense retracing does not hide this j outline.',False,'The written target is Sigma_j.')
ch('right edge beside variétés','(nothing)','(nothing)',edge,True,True,'omission','Drawings and diagrams','medium','p10_edge','A thin, broken, near-horizontal dark stroke runs separately from variétés to the paper edge. It is reproduced as unassigned drawn ink; whether it is authorial incidental ink or another surface mark remains uncertain.')
ch('i<j<k, crossed old trace and rewritten j','i<j<k','i<j<k; note: le j est biffé puis récrit',r'i<\deleted{\unsure{j}}\inserted{j}<k',True,False,'deletion state','Struck text','low','p09_ijk','A long strike crosses an older central glyph. A higher j with a descending hooked stem is live. The old glyph is only tentatively read as j; H’s note already records the crossing and rewrite.')
ch('section heading punctuation',r'\uline{Une digression}',r'\emph{Une digression}.',r'\uline{Une digression}',False,True,'text not on the page','Text that is not on the page','high','p11_sectionheading','The underline ends beneath the final n, followed by blank space before Revenons. No independent full stop follows the heading. The earlier 13. has its own clear point.')
ch('sans donnée de I','donnée','données','donnée',False,True,'misread word','Words','high','p13_donnee','The last e-shaped stroke ends before the blank preceding de; there is no subsequent s-shaped return.')

groups=[
('first category-definition row',r'\Sigma_{(0)},\Sigma_{(1)}',r'\Sigma(0),\Sigma(1)',r'\Sigma_{(0)},\Sigma_{(1)}','p15_def1','Both parenthesised numerals sit below/right of their Sigma bodies; the 0 and 1 are smaller and lowered.'),
('paired s/b connectors',r'\Sigma_{(1)},\Sigma_{(0)}',r'\Sigma(1),\Sigma(0)',r'\Sigma_{(1)},\Sigma_{(0)}','p16_pair','The parenthesised 1 and 0 are placed below/right of their respective Sigmas.'),
('product expression',r'(\Sigma_{(1)},b)\times_{\Sigma_{(0)}}(\Sigma_{(1)},s)',r'(\Sigma(1),\underline b)\times_{\Sigma(0)}(\Sigma(1),\underline s)',r'(\Sigma_{(1)},b)\times_{\Sigma_{(0)}}(\Sigma_{(\unsure{1})},s)','p17_product','All three argument groups are low beside their Sigmas; the base Sigma is itself below the product cross. The second 1 is overdrawn and remains locally doubtful.'),
('composition connector endpoints',r'\Sigma_{(2)},\Sigma_{(1)}',r'\Sigma(2),\Sigma(1)',r'\Sigma_{(2)},\Sigma_{(1)}','p18_composition','The looped 2 and footed 1 sit in low parenthesised groups; both numerals are legible.'),
('fibrant s map',r'\Sigma_{(1)},\Sigma_{(0)}',r'\Sigma(1),\Sigma(0)',r'\Sigma_{(1)},\Sigma_{(0)}','p19_fibrantmap','The parenthesised 1 and small 0 are below/right of the Sigma bodies.'),
('pi-zero equality, Sigma argument',r'\pi_0(\Sigma_{(0)})',r'\pi_0(\Sigma(0))',r'\pi_0(\Sigma_{(0)})','p20_I','The Sigma’s parenthesised 0 is visibly lower than its body; the outer pi-zero parentheses enclose it.'),
('last diagram, parenthesised Sigma arguments',r'\Sigma_{(1)},\Sigma_{(0)}',r'\Sigma(1),\Sigma(0)',r'\Sigma_{(1)},\Sigma_{(0)}','p22_bottomdiagram','The 1 and four 0 arguments have low local placement beside the Sigmas in the three expressions. The source and both displayed targets retain that placement.')]
for place,C,H,F,p,e in groups:
    ch(place+', argument placement',C,H,F,False,True,'misread symbol or index','Symbols and indices','high',p,e)
ch('category Sigma underline count',r'\uline{\Sigma}',r'\underline{\Sigma}; note: souligné deux fois',r'\uline{\Sigma}',False,True,'other','Other','high','p15_def1','At each of the three categorical Sigmas in this row, one added horizontal line lies below the Sigma’s own bottom stroke. H’s code is compatible with one underline; its note counts two. This row concerns that explicit note, not wrapper syntax.')
ch('paired connectors, lower endpoint',r'\arrow[r,shift right=2,"\uline{b}"\']',r'\rightrightarrows','lower shaft with the source’s short dense terminal stub',True,True,'drawing or diagram','Drawings and diagrams','medium','p16_pair','The top shaft ends in a clear right head. The lower shaft ends in a short dense upright/protruding stub, whose contour is preserved by a custom filled endpoint instead of adding a clean V.')
ch('product, b label','b',r'\underline b','b',False,True,'text not on the page','Text that is not on the page','high','p17_product','The factor’s b has a stem and bowl, with no separate underline beneath it.')
ch('product, s label','s',r'\underline s','s',False,True,'text not on the page','Text that is not on the page','high','p17_product','The second factor’s s is plain; no detached horizontal underline occurs below it.')
ch('definition connector geometry',r'\arrow[r,Rightarrow,"\text{déf}"]',r'\overset{\text{déf}}{\Longrightarrow}','short upper bar above a longer lower rightward arrow',True,True,'drawing or diagram','Drawings and diagrams','high','p17_product','The upper horizontal stroke stops before the lower shaft’s single terminal head. They remain separate paths in the proposed drawing.')
ch('below definition connector','(nothing)','(nothing)','two unassigned dark points below the connector',True,True,'omission','Drawings and diagrams','medium','p17_product','Two small distinct dark points lie below the lower shaft, one lower and slightly left of the other. They are retained without assigning punctuation or a mathematical function; provenance is uncertain.')
ch('upper composition label, M0613',r'\unsure{\text{cpl.}|\text{compl.}|\text{appl.}}',r'\text{compl.}',compo,False,True,'misread word','Words','low','p18_composition','An open initial c, central p-like descent, tall final l and a separate stop are visible. The central return is compressed, so compl. remains open. The initial c permits removal of appl. as a candidate; cpl. is the leading literal reading.',True)
ch('lower composition label',r'\text{comp. des flèches}',r'\text{compos.\ des flèches}',r'\text{comp. des flèches}',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','p18_composition','After the low comp group, a single p descender is followed directly by a distinct stop. des flèches is on the line below; there is no written os group after comp.')
ch('I expression, M0614',r'\unsure{I_{(0)}|I}',r'I(\underline{\Sigma})',Imark,True,True,'misread symbol or index','Symbols and indices','low','p20_I','Capital I and parenthesis strokes are clear. Inside the compact low group, a Sigma-like overwork crosses residual zero-like loops. The lower placement and the overwritten layer are both uncertain. The proposal preserves a tentative old 0 plus Sigma layer, a baseline-argument alternative, and the original I_(0) reading.',False,'The written name and its overwritten argument remain unresolved; no expected invariant has been substituted.')
ch('cancelled interlinear word after live pré','(nothing)','note: un mot biffé',r'\inserted{pré\deleted{\unsure{filtré}}}',True,True,'omission','Struck text','low','p21_pre','Live pré stands to the left of the crossed word. The cancelled word shows an f-like initial stroke/descent, a short i-like stroke, a tall l-like upright and a final accent; the intervening low strokes remain obscured. filtré is a tentative reading. The common leader enters before baseline ordonné.',True)
ch('last diagram, lower expression',r'\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})',r'\pi_0(\Sigma(0))\times\pi_0(\Sigma(0))',r'\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})',False,True,'misread symbol or index','Symbols and indices','high','p22_bottomdiagram','The lower expression has one written pi-zero before a parenthesised product of two Sigmas. A second pi-zero is not written between the product sign and the second Sigma. The repetition of the upper expression is retained literally.',False,'The source’s repeated single pi-zero expression is preserved.')
ch('last diagram, vertical connector',r'\arrow[d,"\sim"]',r'\simeq; note: écrit vertical','wavy/reworked left component beside one straight right upright',True,True,'drawing or diagram','Drawings and diagrams','high','p22_bottomdiagram','The short vertical marker comprises a hooked/wavy left trace and a separate straight upright on its right. No secure downward arrowhead is visible. The return draws those observed components at the left part of the targets.')
ch('last diagram, horizontal shaft',r'\arrow[r,"{\pi_0(\uline{s},\uline{b})}"]',r'\xrightarrow{\ \pi_0(\underline s,\underline b)\ }','rightward shaft with central dark thickening and terminal head',True,True,'drawing or diagram','Drawings and diagrams','high','p22_bottomdiagram','A dark pointed thickening remains near the middle of the long shaft as well as the clear terminal head. The middle trace may be an earlier head, but its history is not assigned; the literal thickening is drawn.')
ch('bottom foliation',r'\mspage{66}','(nothing)',r'\margin{66}',True,True,'other','Other','high','p23_folio','Two pale 6 figures sit at the bottom-left paper edge in another hand. They are retained as separate foliation, while the dark top 29 is the authorial page number.')
ch('paired map, trailing comma',r'\Sigma_{(0)}',r'\Sigma(0),',r'\Sigma_{(0)},',True,False,'omission','Omissions','high','p16_pair','A separate curved comma follows the closing parenthesis of the target argument. H retains it; C omits it.')
ch('margin, before Sigma_kij',r'des $\Sigma_{kij}$',r'des \ill{} $\Sigma_{kij}$',r'des $\Sigma_{kij}$',False,True,'text not on the page','Text that is not on the page','high','p07_margin','The line ending des is followed by the next line beginning Sigma_kij. The gap contains no additional foreground word corresponding to H’s illegible placeholder.',True)

# Keep quotations literal, including the relevant witness notes.  The grouped
# placement rows quote each complete local formula rather than artificial
# comma-joined lists of its separated terms.
quoted={c['place']:c for c in changes}
quoted['second cancelled line']['C']=r'de prendre pour $j$'
quoted['i<j<k, crossed old trace and rewritten j']['H']=r"L'indice $ij$ de la source est surchargé, et le « $j$ » de « $i<j<k$ » est biffé puis récrit."
quoted['category Sigma underline count']['H']=r'$\underline{\Sigma}$ est souligné deux fois.'
quoted['cancelled interlinear word after live pré']['H']="Le « pré » d'« ens. préordonné » est écrit au-dessus d'un mot biffé."
quoted['last diagram, vertical connector']['H']=r'Le $\simeq$ final est écrit vertical, sous $\pi_0(\Sigma(0)\times\Sigma(0))$.'
quoted['first category-definition row, argument placement'].update(
 C=r'\Sigma_{(0)}=\operatorname{Ob}(\uline{\Sigma}),\quad\Sigma_{(1)}=\operatorname{Fl}(\uline{\Sigma}),',
 H=r'\Sigma(0)=\mathrm{Ob}(\underline{\Sigma}),\ \Sigma(1)=\mathrm{Fl}(\underline{\Sigma}),',
 final=r'\Sigma_{(0)}=\operatorname{Ob}(\uline{\Sigma}),\quad\Sigma_{(1)}=\operatorname{Fl}(\uline{\Sigma}),')
quoted['paired s/b connectors, argument placement'].update(
 C=r'''\Sigma_{(1)}\arrow[r,shift left=2,"\uline{s}"]\arrow[r,shift right=2,"\uline{b}"']&\Sigma_{(0)}''',
 H=r'\Sigma(1)\overset{\underline s}{\underset{\underline b}{\rightrightarrows}}\Sigma(0)',
 final=r'''\Sigma_{(1)}\arrow[r,shift left=2.5,"\uline{s}"]\arrow[r,shift right=2.5,dash,"\uline{b}"',end anchor=west,shorten >=2pt] & |[alias=s67pairtarget]|\Sigma_{(0)},''')
quoted['composition connector endpoints, argument placement'].update(
 C=r'''\Sigma_{(2)}\arrow[r,"\unsure{\text{cpl.}|\text{compl.}|\text{appl.}}","\text{comp. des flèches}"'] & \Sigma_{(1)}''',
 H=r'\Sigma(2)\xrightarrow[\text{compos.\ des flèches}]{\text{compl.}}\Sigma(1)',
 final=r'''\Sigma_{(2)}\arrow[r,"\unsure{\text{cpl.}|\text{compl.}}","\substack{\text{comp.}\\\text{des flèches}}"'] & \Sigma_{(1)}''')
quoted['fibrant s map, argument placement'].update(
 C=r'\uline{s}:\Sigma_{(1)}\longrightarrow\Sigma_{(0)}',
 H=r'\underline s : \Sigma(1)\to\Sigma(0)',
 final=r'\uline{s}:\Sigma_{(1)}\unsure{\longrightarrow|-}\Sigma_{(0)}')
quoted['last diagram, parenthesised Sigma arguments, argument placement'].update(
 C=r'''\pi_0(\Sigma_{(1)})\arrow[r,"{\pi_0(\uline{s},\uline{b})}"]&\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})\arrow[d,"\sim"]\\
&\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})''',
 H=r'\pi_0(\Sigma(1))\xrightarrow{\ \pi_0(\underline s,\underline b)\ }\pi_0(\Sigma(0)\times\Sigma(0))\simeq\pi_0(\Sigma(0))\times\pi_0(\Sigma(0))',
 final=r'''|[alias=s67lastsource]|\pi_0(\Sigma_{(1)})\arrow[r,"{\pi_0(\uline{s},\uline{b})}"]
& |[alias=s67lasttop]|\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})\\
&\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})''')

decisions=[
dict(id='M0611',decision='alternative',reading=r'\Sigma_j',evidence='Separate dot, descending stem and low left hook distinguish the written j through its retracing.',crop='crops/150_scan067_p08_headingmap.png',box=boxes['p08_headingmap'],confidence='high'),
dict(id='M0612',decision='undecided',reading=r'\Sigma^{\unsure{*|<}}(1)',evidence='The raised dark mark is compact; its short branches do not securely separate star and angle forms. The leading star is retained without resolution.',crop='crops/150_scan067_p12_sigmatup.png',box=boxes['p12_sigmatup'],confidence='low'),
dict(id='M0613',decision='undecided',reading=compo,evidence='Initial open c, central p-like descent, final tall l and stop are visible. The middle join remains compressed, retaining cpl. and compl.; appl. is excluded by the initial c.',crop='crops/150_scan067_p18_composition.png',box=boxes['p18_composition'],confidence='low'),
dict(id='M0614',decision='undecided',reading=Imark,evidence='I, parenthesis traces, Sigma-like overwork and zero-like residual loops are visible. Both the layer sequence and lowered versus baseline argument placement remain uncertain.',crop='crops/150_scan067_p20_I.png',box=boxes['p20_I'],confidence='low')]

doubts=[]
def db(place,reading,alternatives,reason):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence='low',reason=reason))
db('punctuation after topologiques',r'\unsure{,|;}','comma; semicolon','The comma is clear. A tiny distinct upper point near source (750,613) may belong to the punctuation or be an incidental/surface point. Its provenance and attachment remain uncertain; comma leads.')
db('combined-case source',source_map,'ik; old j overwritten by k after i; ij','An upper k-like form sits over a hooked lower trace; literal reading and overwritten layer are distinguished as alternatives.')
db('crossed central glyph before rewritten j',r'\deleted{\unsure{j}}','j; another unreadable crossed glyph','The higher live j is legible, but the older glyph under the strike is not securely recoverable.')
db('M0612',r'\Sigma^{\unsure{*|<}}(1)','*; <','The small raised mark has dense, merged branches.')
db('final Sigma in first product',r'\unsure{\Sigma|\overline{\Sigma}}',r'\Sigma; \overline{\Sigma}','A detached upper bar plus three zigzag/foot strokes makes a four-stroke Sigma construction; the corresponding pen-lift pattern at the page bottom favours plain Sigma. An additional overline remains an explicit local alternative pending notation review. Both witnesses read plain Sigma, so this certainty-only addition has no change row.')
db('second product factor argument',r'\Sigma_{(\unsure{1})}','1; unresolved overwritten numeral','The numeral is darkly overworked. The upright 1 candidate is retained without inventing an underlying digit; C and H both give 1.')
db('M0613',compo,'cpl.; compl.','Visible c and l bound a compressed central p-like group; no independent om group is securely isolated.')
db('fibrant s map terminal',r'\unsure{\longrightarrow|-}','rightward arrow; unheaded shaft with a terminal thickening','The small filled terminal is pointed but densely inked. Arrow leads; its exact contour remains uncertain. C and H both read an arrow, so this added doubt alone is not a textual change.')
db('M0614',Imark,'lowered parenthesised overwritten 0/Sigma group; baseline parenthesised group; I_(0)','The Sigma-like and zero-like strokes overlap, and the parenthesis contours span more than one vertical level. The uncertainty of both state and placement remains in the text.')
db('cancelled interlinear word after pré',r'\deleted{\unsure{filtré}}','filtré; incompletely recovered f/i/l...é word','Initial f-like descent, short i-like stroke, tall l-like upright and final accent are visible; middle letters are crossed.')

inventory=[]
def el(kind,pos,reading,hand='his hand',**kw):
    row=dict(element=f'E{len(inventory)+1:02}',kind=kind,position=pos,first_words_or_objects=reading,sheet_kind='text',hand=hand,transcribed='yes');row.update(kw);inventory.append(row)
el('margin note','top left',r'\mspage{29}')
el('text','top two main baselines','Enfin, la condition d) signifie ... satisfait la condition c) du Scholie (p.27).')
el('insertion','between those two baselines',r"\inserted{d'espace top. ordonné}",attachment='Continuous leader bends before satisfait. Initial d is reworked but live; no separate cancelled letter is assigned.')
el('text','first case paragraph',r'\uline{Cas équisingulier} : les s_ij sont fibrants propres')
el('text','second case paragraph',r'Cas non singulier ... topologiques\unsure{,|;} ... des Sigma_ji pour j<i',details='The first dotted Sigma_i subscript is reworked, with no independently recovered old letter. The clear comma and separate tiny upper point retain a local punctuation/provenance doubt.')
el('deletion','end of the second case paragraph, across two baselines',r'\deleted{(NB il suffit de prendre pour j}',details='Opening parenthesis remains unclosed as written. The second line is legible below the strike; no separate en is recoverable after il.')
el('margin note','oblique left margin beside the two lower cases',margin,details='Literal de =, the two indexed Sigma terms, the author’s sans doute and the terminal two dots plus dash are retained. The long j descender crosses doute without a separate cancellation.')
el('text','combined-case paragraph, four main baselines',r'Cas équisingulier-non singulier; s_ij: [reworked source] -> Sigma_j est une fibration propre ...',details='Three separate heading underlines; source layer alternatives retained; target j read from dot, stem and hook.')
el('drawing','right paper edge beside variétés',edge,details='Unassigned thin broken stroke; authorial/incidental/surface provenance uncertain.')
el('deletion','central glyph in i<j<k',r'\deleted{\unsure{j}}',details='Old crossed trace below/through the rewritten j; exact old letter remains doubtful.')
el('insertion','higher live central letter in i<j<k',r'\inserted{j}',attachment='Rewritten above the older crossed trace; dot/stem/hook read locally.')
el('text','section heading and opening digression paragraph','13. Une digression Revenons au cas de ... sans donnée de I. Plus généralement, considérons une catégorie topologique',details='Heading has no final point. Sigma superscript and last Sigma’s detached upper-bar construction remain explicit local doubts.')
el('display','first row of category definition',r'\uline{\Sigma}=(\Sigma_{(0)}=Ob(\uline{\Sigma}),\Sigma_{(1)}=Fl(\uline{\Sigma}),',details='One added underline per categorical Sigma; parenthesised arguments lowered locally.')
el('diagram','right of the first definition row',r'\Sigma_{(1)} [two horizontal connectors labelled underlined s and b] \Sigma_{(0)},',details='Upper terminal head clear; lower dense stub retained literally.')
el('diagram','second definition row','Product of the two Sigma_(1) factors over Sigma_(0), definition connector, Sigma_(2), labelled composition connector, Sigma_(1)',details='Factor b and s plain. Upper definition bar shorter than headed lower shaft. Two unassigned dark points below it. Composition labels cpl.|compl. and comp. des flèches.')
el('text','below the definition, through the final graph description','et supposons que ... soit fibrant. Je dis qu’alors ... est un ens. ... ordonné, en prenant comme graphe ...',details='I expression retains overwritten-layer and vertical-position alternatives. The source’s assertion is transcribed without a proof claim.')
el('insertion','above baseline ordonné',r'\inserted{pré}',attachment='Live pré lies left of the cancelled interlinear word; common leader enters before ordonné.')
el('deletion','same interline, immediately after live pré',r'\deleted{\unsure{filtré}}',details='Candidate f/i/l...é word, with obscured middle letters. Kept in source spatial order after pré.')
el('diagram','bottom right','pi_0(Sigma_(1)) to pi_0(Sigma_(0) times Sigma_(0)); repeated same target below',details='Label pi_0(underlined s, underlined b). Horizontal shaft has central thickening and terminal head. Vertical marker has wavy/reworked left part and straight right upright; no vertical arrow supplied.')
el('margin note','bottom left',r'\margin{66}','another unnamed hand',details='Pale foliation, separate from authorial top29.')

def uncomment(s):
    return '\n'.join(line for line in s.splitlines() if not line.lstrip().startswith('%'))
audit=[]
def ab(kind,box,reading):
    audit.append(dict(box=f'B{len(audit)+1:02}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading.strip()))
ab('handwritten number',boxes['p00_head29'],r'\mspage{29}')
ab('insertion',boxes['p01_openinsertion'],r'''\inserted{d'espace top. ordonné}
satisfait la
% Continuous leader bends into the apparent parenthesis before satisfait.
% The box also clips lower portions of the preceding main baseline above,
% and contains the cut-off beginning of condition after satisfait la at its
% right boundary. These are neighbouring main text,
% not part of the inserted wording; the reworked initial d remains live.''')
ab('handwritten number',boxes['p02_reference'],r'''du Scholie (p. $27$).
% Any clipped upper-edge continuation belongs to the preceding main baseline.''')
ab('doubtful formula',boxes['p03_sigmai'],r'''$\Sigma_i$
% The dotted i is locally reworked; no underlying letter is assigned.''')
ab('lexical disagreement',boxes['p04_topologiques'],r'''topologiques\unsure{,|;}
% A clipped descender from the preceding line's singulier enters at the top.
% The tiny point above the clear comma has uncertain provenance/attachment.''')
ab('struck passage',boxes['p05_cancelNB'],r'\deleted{(NB il suffit}')
ab('struck passage',boxes['p06_cancelnext'],r'\deleted{de prendre pour $j$}')
ab('margin note',boxes['p07_margin'],margin+r'''
% Slanted marginal text is complete. Along the right boundary are clipped
% portions of neighbouring main-body writing, including topologiques,
% the following des, the cancelled line's beginning, Cas, and later line
% beginnings. They remain part of those main lines, not of this note.''')
ab('doubtful formula',boxes['p08_headingmap'],r'''\uline{Cas} \uline{équisingulier}-\uline{non singulier}
$s_{ij}:'''+source_map+r'''\longrightarrow\Sigma_j$ est
% The bottom of the preceding cancelled line's j reaches the upper boundary.''')
ab('struck passage',boxes['p09_ijk'],r'''$\Sigma_{ijk}$ pour $i<\deleted{\unsure{j}}\inserted{j}<k$.
% At the upper edge, clipped descenders belong to the preceding line.
% The older crossed central trace and the higher live j are separate layers.''')
ab('medium-confidence departure',boxes['p10_edge'],edge+r'''
% The upper-left part also contains the clipped end of the word variétés.
% The thin broken stroke itself continues to the right paper edge.''')
ab('handwritten number',boxes['p11_sectionheading'],r'13. \uline{Une digression}')
ab('doubtful formula',boxes['p12_sigmatup'],r'$\Sigma,\Sigma^{\unsure{*|<}}(1)\subset\Sigma\times\unsure{\Sigma|\overline{\Sigma}}$,')
ab('lexical disagreement',boxes['p13_donnee'],'sans donnée de')
ab('lexical disagreement',boxes['p14_generalement'],'généralement,')
ab('handwritten number',boxes['p15_def1'],r'''$\uline{\Sigma}=(\Sigma_{(0)}=\operatorname{Ob}(\uline{\Sigma}),\quad\Sigma_{(1)}=\operatorname{Fl}(\uline{\Sigma}),$
% The lower edge clips the top of the following row's déf label.''')
ab('handwritten number',boxes['p16_pair'],r'''\diagram{\begin{tikzcd}[execute at end picture={
\fill ([xshift=-2.8pt,yshift=-1.35pt]s67auditpair.west) --
([xshift=-1.4pt,yshift=-2.2pt]s67auditpair.west) --
([xshift=-1.8pt,yshift=-3.5pt]s67auditpair.west) --
([xshift=-3.0pt,yshift=-3.2pt]s67auditpair.west) -- cycle;
}]
\Sigma_{(1)}\arrow[r,shift left=2.5,"\uline{s}"]\arrow[r,shift right=2.5,dash,"\uline{b}"',end anchor=west,shorten >=2pt]
& |[alias=s67auditpair]|\Sigma_{(0)},
\end{tikzcd}}''')
ab('doubtful formula',boxes['p17_product'],r'''\diagram{\begin{tikzcd}[column sep=10mm,execute at end picture={
\draw[->,line width=.75pt,line cap=round] ([xshift=2pt,yshift=-1pt]s67auditproduct.east) -- ([xshift=-2pt,yshift=-1pt]s67audittwo.west);
\draw[line width=.55pt,line cap=round] ([xshift=2pt,yshift=3pt]s67auditproduct.east) -- ([xshift=-5pt,yshift=3pt]s67audittwo.west);
\fill ([xshift=-7pt,yshift=-5pt]s67audittwo.west) circle[radius=.27pt];
\fill ([xshift=-7.7pt,yshift=-6.5pt]s67audittwo.west) circle[radius=.23pt];
}]
|[alias=s67auditproduct]|(\Sigma_{(1)},b)\times_{\Sigma_{(0)}}(\Sigma_{(\unsure{1})},s)\arrow[r,phantom,"\text{déf}"]
& |[alias=s67audittwo]|\Sigma_{(2)}
\end{tikzcd}}
% At the upper edge are clipped low parts of the preceding definition row.
% The two dark points beneath the definition connector remain unassigned.''')
ab('doubtful formula',boxes['p18_composition'],r'''\diagram{\begin{tikzcd}
\Sigma_{(2)}\arrow[r,"\unsure{\text{cpl.}|\text{compl.}}","\substack{\text{comp.}\\\text{des flèches}}"']&\Sigma_{(1)}) ,
\end{tikzcd}}
% Upper-edge fragments belong to the preceding definition row.
% Left-edge fragments belong to the adjacent definition connector.''')
ab('doubtful formula',boxes['p19_fibrantmap'],r'''$\uline{s}:\Sigma_{(1)}\unsure{\longrightarrow|-}\Sigma_{(0)}$
% The upper-right edge clips a descender from the composition caption above.''')
ab('doubtful formula',boxes['p20_I'],r'$\pi_0(\Sigma_{(0)})='+Imark+'$')
ab('insertion',boxes['p21_pre'],r'''\uline{un ens. }\inserted{pré\deleted{\unsure{filtré}}}\uline{ordonné},
% Live pré stands left of the crossed interlinear word; their leader enters
% before ordonné. Clipped upper-edge strokes belong to Je dis above.''')
ab('doubtful formula',boxes['p22_bottomdiagram'],bottom+r'''
% The upper edge also clips the end of the preceding prose line, from
% the latter part of graphe through de la relation. The map label's highest
% strokes at that boundary were read in the full-resolution lower half.''')
ab('handwritten number',boxes['p23_folio'],r'\margin{66}')
ab('medium-confidence departure',boxes['p24_isolated'],r'''% Compact irregular dark surface fleck, with gray halo and no recoverable
% connected letter or stroke sequence. Origin uncertain. Excluded from the
% manuscript text; retained here for inspection of provenance only.''')

purposes={
'p00_head29':'Authorial top number29.',
'p01_openinsertion':'Inserted d’espace top. ordonné, reworked initial d, leader versus literal parenthesis before satisfait.',
'p02_reference':'Scholie reference, handwritten27, number of closing parentheses and full stop.',
'p03_sigmai':'Reworked dotted i subscript in the first non-singular-case Sigma.',
'p04_topologiques':'Clear comma and contested separate upper point after topologiques; comma/semicolon uncertainty.',
'p05_cancelNB':'Cancelled NB clause; il suffit retained after checking H’s additional en.',
'p06_cancelnext':'Second cancelled line read as de prendre pour j, versus H illegible.',
'p07_margin':'Complete oblique marginal note, rotated−40°; words, indices, unrecorded de =, and terminal ..-.',
'p08_headingmap':'Full combined-case heading/map; source reworking, target M0611 and underline spans.',
'p09_ijk':'Sigma_ijk and inequality with old crossed central trace and live rewritten j.',
'p10_edge':'Unassigned thin broken dark stroke extending to the right paper edge.',
'p11_sectionheading':'Section13., heading underline and absence of a heading-final point.',
'p12_sigmatup':'Whole first Sigma/product expression, M0612 and the last Sigma’s detached upper bar.',
'p13_donnee':'donnée/données lexical ending.',
'p14_generalement':'Full word généralement, checking compressed/retraced ending and possible short form; retained full word.',
'p15_def1':'First category-definition row, underline counts, operators and lowered parenthesised arguments.',
'p16_pair':'Paired s/b connectors, endpoints, underlines and arguments1/0.',
'p17_product':'Product factors, plain b/s, definition connector, dark points and digits1/0/1/2.',
'p18_composition':'Whole composition map with M0613 and comp. des flèches caption.',
'p19_fibrantmap':'Whole s map, arguments1/0 and dense filled terminal.',
'p20_I':'Whole pi-zero equality and overwritten I expression, M0614.',
'p21_pre':'Live inserted pré, cancelled candidate filtré, leader, baseline ordonné and underline.',
'p22_bottomdiagram':'Bottom horizontal and vertical connectors, repeated target expression, digits0/1, underlined labels and central shaft thickening.',
'p23_folio':'Other-hand bottom foliation66.',
'p24_isolated':'Unassigned compact dark surface fleck in the blank interval; origin uncertain, excluded from manuscript text.'}

record=dict(scan='067',reader='reader_b',line_count=21,changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,
 notes=[
  dict(id='150-067-N01',text='The author states that condition d) makes the indicated ordered topological-space structure satisfy condition c) of the Scholie, referring to p.27. The next three case paragraphs describe the written s_ij as fibrants propres, describe boundaries of the Sigma_i in the nonsingular case, and give a fibration/boundary description in the combined case. These are reports of the manuscript, not independent theorem statements or verified conclusions.'),
  dict(id='150-067-N02',text='The marginal note asks for the Sigma_ij to be manifolds with boundary and gives the boundary as the union of the written Sigma_kij and Sigma_ikj. It then says c’est sans doute une conséquence de la condition précédente. That qualification is the author’s own. The note begins with the literal de = shorthand and ends with two points and a dash; neither feature is expanded or normalised in the page text.'),
  dict(id='150-067-N03',text='Section13 is headed Une digression. The author returns to the Sigma/product setting without a given I, introduces the displayed topological-category data, and states a preorder claim for pi_0 of the object space under the written fibrancy supposition. The image of the displayed pi_0 map is proposed as the relation’s graph. The last lower expression repeats the single pi_0 of a product; that literal repetition is retained instead of H’s product of two pi_0 expressions. Reading these statements was not a proof check.'),
  dict(id='150-067-N04',text='The authorial number29 is at the head; pale foliation66 at the foot is in another hand. Reference27 and section13 are written numerals. Twenty-one main text/display baselines are counted, including the second cancelled line and lower target expression, with slanted margin and interlinear writing inventoried separately. No expected mathematical formula was used to replace a source or target index.'),
  dict(id='150-067-N05',text='M0611 is resolved to the visibly dotted and descending target j. M0612, M0613 and M0614 remain undecided. M0613 is narrowed to cpl.|compl. because the initial c is visible. M0614 retains both the uncertain overwritten 0/Sigma layer and the uncertainty of lowered versus baseline placement. The tentative cancelled filtré preserves visible f/i/l and final-accent evidence while leaving its middle uncertain.'),
  dict(id='150-067-N06',text='The first insertion leader supplies the apparent parenthesis before satisfait; no extra text parenthesis is retained. The initial d of d’espace and the first Sigma_i subscript are reworked but have no independently recovered old letter. A detached upper bar in the first product’s final Sigma is consistent with a pen lift in a four-stroke Sigma; the same construction occurs in the final lower Sigma on this sheet. Its local overline alternative remains explicit for later notation review.'),
  dict(id='150-067-N07',text='The two dark points under the definition connector and the thin broken stroke at the right paper edge are reproduced without assigning linguistic or mathematical meaning. Their provenance is uncertain. The last vertical marker is drawn from its wavy/reworked left component and straight right upright; the horizontal shaft retains its middle thickening, whose possible history as an earlier head remains unassigned.'),
  dict(id='150-067-N08',text='Individual audit rectangles follow the saved crop locations for each insertion, cancellation, marginal passage, numeral, lexical disagreement, doubtful formula and uncertain drawn trace. Position comments identify clipped neighbouring strokes without attaching them to the audited phrase. The separate point above the clear comma after topologiques has uncertain provenance and punctuation attachment; comma leads the retained comma/semicolon alternatives.'),
  dict(id='150-067-N09',text='A compact irregular dark fleck in the blank interval below the case paragraphs was inspected in crop p24_isolated, source box [625,1225,730,1310]. Its dark core has a gray halo, with no recoverable connected letter or stroke sequence. It is recorded as an excluded unassigned surface fleck of uncertain origin, without adding a linguistic token or manuscript figure.')
 ],check_events=[],
 notation=[
  dict(form=r'\Sigma_i,\Sigma_{ji},\Sigma_{ij},\Sigma_{kij},\Sigma_{ikj},\Sigma_{ijk}',meaning='Indexed Sigma expressions used in the author’s case and boundary descriptions.',evidence='Letter indices are visible in the body and oblique note; the combined-case source has an independent reworking doubt.',places='three case paragraphs and margin'),
  dict(form=r'\Sigma_{(0)},\Sigma_{(1)},\Sigma_{(2)}',meaning='Object, arrow and composition-data expressions in the author’s category display, with local lowered argument placement.',evidence='Small parenthesised numerals lie below/right of the Sigma bodies throughout the lower display and following formulas.',places='category definition and subsequent pi-zero formulas'),
  dict(form=r'\uline{\Sigma}',meaning='The author’s underlined category symbol.',evidence='One added underline is visible below the Sigma’s own lower stroke in each of the three definition-row occurrences.',places='start of category tuple; arguments of Ob and Fl'),
  dict(form=r'\Sigma^{\unsure{*|<}}(1)',meaning='Unresolved local superscript in the author’s return to the Sigma setting.',evidence='Dark merged short branches above the second Sigma.',places='M0612, opening of section13'),
  dict(form=r'\pi_0(\Sigma_{(0)}\times\Sigma_{(0)})',meaning='The literal target expression repeated on two levels of the last diagram.',evidence='One pi-zero before a product of two indexed Sigmas on each level.',places='last diagram, both target levels'),
  dict(form='vertical wavy/straight two-component marker',meaning='The source’s connector between the two displayed target levels; no independently verified identification is asserted.',evidence='Reworked wavy left component beside a straight right upright, with no secure vertical head.',places='last diagram'),
  dict(form='de =',meaning='The literal written shorthand in the marginal sentence.',evidence='A separate de followed by two short horizontal strokes before les.',places='margin, second slanted baseline')
 ],
 abbreviations=[
  dict(written='top.',expansion='topologique',places='top insertion'),
  dict(written='NB',expansion='nota bene',places='cancelled clause'),
  dict(written='de =',expansion='de même',places='margin; expansion not substituted into the transcription'),
  dict(written='déf',expansion='définition',places='label above definition connector; no written stop'),
  dict(written='cpl.|compl.',expansion='unresolved',places='upper composition-map label, M0613'),
  dict(written='comp.',expansion='composition',places='lower composition-map label'),
  dict(written='ens.',expansion='ensemble',places='preorder phrase'),
  dict(written='Ob',expansion='objets',places='category definition'),
  dict(written='Fl',expansion='flèches',places='category definition')
 ],
 hand_log=[
  dict(habit='A broad insertion leader can resemble an independent opening parenthesis.',places='before satisfait',scope='The single top insertion on this sheet; continuous path traced on its crop.',witness_errors='C and H both retain a literal opening parenthesis; H adds an extra closing one.'),
  dict(habit='Index letters are locally reworked, leaving hooked lower traces that should not be assigned by the expected formula.',places='first Sigma_i; combined-case source and target; j in i<j<k',scope='Each place read independently; source and older crossed central glyph remain doubtful.',witness_errors='H reads source ij and target i; C doubts the target and omits the crossed/replaced central trace.'),
  dict(habit='The bottom stroke of a capital Sigma can be counted as an underline, while its detached top bar can look like an overline.',places='three categorical Sigmas; last Sigma in first product; lower final Sigma',scope='One added underline is secure in the definition row; detached upper-bar state remains explicitly doubtful in the first product.',witness_errors='H’s note says the category Sigma is double-underlined; source shows one added line. Both witnesses give plain Sigma in the product.'),
  dict(habit='A long descender from an index crosses a later word without cancelling it.',places='margin Sigma_ikj descender crossing doute',scope='This particular crossing.',witness_errors='H leaves the surrounding words illegible; C’s live wording is supported.'),
  dict(habit='Short forms and continuation marks have locally written point counts.',places='top.; comp.; ens.; cpl./compl.; terminal ..-',scope='Every listed stop read independently; no general expansion applied.',witness_errors='H gives compos.; C and H both replace the margin’s two points and dash with an ellipsis.'),
  dict(habit='Arrow-like connectors may have unequal bars, dense stubs, interior thickenings or vertical reworked components.',places='paired connectors; definition connector; fibrant s map; final diagram',scope='Each connector retains its local observed geometry and any uncertainty.',witness_errors='Both witnesses use generic arrow forms; C supplies a vertical arrow under the last target.'),
  dict(habit='Live and cancelled interlinear text can share a leader and baseline.',places='pré and cancelled filtré candidate above ordonné',scope='One insertion on this sheet.',witness_errors='C omits the crossed word; H notes a crossed word without transcribing its surviving letters.')
 ],audit_boxes=audit,
 crops=[dict(file=f'crops/150_scan067_{name}.png',box=box,purpose=purposes[name]) for name,box in boxes.items()],
 unresolved=[d['place']+': '+d['reading'] for d in doubts],
 coverage=dict(whole_image_viewed=True,halves_viewed=['top','bottom'],all_tokens_read=True,all_C_insertions_deletions_checked=True,differences_considered=len(list(csv.DictReader((ROOT/'edition/packets/150_scan067/diffs.tsv').open(),delimiter='\t'))),macro_only_differences_ignored='Equivalent underline/emphasis and insertion/deletion wrappers; editorial H section markup and historical/page-reference notes; TeX environment/alias/layout syntax. H’s notes already acknowledge authorial29 and the crossed/replaced j, so those acknowledgements are considered in comparisons. A local certainty-only addition at the detached Sigma bar, second-factor numeral or filled map endpoint has no counted change row.'))

def fix_quote_escapes(v):
    if isinstance(v,str): return v.replace(chr(92)+chr(39),chr(39))
    if isinstance(v,list): return [fix_quote_escapes(x) for x in v]
    if isinstance(v,dict): return {k:fix_quote_escapes(x) for k,x in v.items()}
    return v
record=fix_quote_escapes(record)

# Required structural checks only; no TeX compilation or mathematical test.
assert len(boxes)==25 and all((ROOT/'edition'/c['file']).is_file() for c in record['crops'])
assert all(x['transcribed']=='yes' for x in inventory)
assert {d['id'] for d in decisions}=={'M0611','M0612','M0613','M0614'}
assert all(c['against_C'] or c['against_H'] for c in changes)
assert len({c['id'] for c in changes})==len(changes)
assert tex.count('\\begin{tikzcd}')==tex.count('\\end{tikzcd}')==3
assert r'\mspage{29}' in tex and r'\margin{66}' in tex and r'\mspage{66}' not in tex
payload=json.dumps(record,ensure_ascii=False,indent=2)+'\n'
json.loads(payload)
OUT.mkdir(exist_ok=True)
for dest,content in [(OUT/'150_scan067.tex',tex),(OUT/'150_scan067.json',payload)]:
    tmp=dest.with_name(dest.name+'.tmp');tmp.write_text(content);os.replace(tmp,dest)
print(json.dumps(dict(scan='067',changes=len(changes),against_C=sum(c['against_C'] for c in changes),against_H=sum(c['against_H'] for c in changes),doubts=len(doubts),inventory=len(inventory),audit_boxes=len(audit),crops=len(boxes))))
