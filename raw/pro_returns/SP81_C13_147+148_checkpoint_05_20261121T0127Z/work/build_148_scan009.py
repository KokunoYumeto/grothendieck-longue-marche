from pathlib import Path
import json

root=Path('/workspace/scratch/15c7af26487b/edition')
page='148_scan009'
packet=(root/'packets'/f'{page}.md').read_text()
C=packet.split('## Witness C',1)[1].split('```tex',1)[1].split('```',1)[0].strip()
H=packet.split('## Witness H',1)[1].split('```tex',1)[1].split('```',1)[0].strip()
coords={
 'heading':[215,28,1650,244], 'equivalence':[307,230,1635,365],
 'upper_identity':[606,576,1625,783], 'units_ring':[1030,773,1671,1016],
 'zeta_definition':[1030,1010,1430,1113], 'lattice_drawing':[148,888,575,1373],
 'corrected_pose':[680,1120,1100,1264], 'elliptic_base':[653,1270,1237,1390],
 'elliptic_twist':[648,1400,1320,1535], 'construction_start':[225,1535,1630,1661],
 'euclidean_clause':[240,1658,1550,1772], 'vector_origin':[236,1752,1594,1878],
 'network_sentence':[218,1883,1615,2103], 'final_quotient':[537,2107,1143,2204],
 'lower_numeral':[34,2270,92,2347]
}
def crop(name): return f'{page}_{name}.png'
def evidence(name,words): return words+f' Crop {crop(name)}, original box {coords[name]}.'

radical=r'''\begin{tikzpicture}[baseline=(rad.base)]
\node[inner sep=0pt] (rad) {$\sqrt[3]{1}$};
\draw[line width=.35pt] ([yshift=-1pt]rad.south west) -- ([yshift=-1pt]rad.south east) -- ++(-.025,.06);
\node[below=2pt,inner sep=0pt] at (rad.south) {$\zeta$};
\end{tikzpicture}'''
upper_identity=r'''\mathbb Z/6\mathbb Z\simeq\mu_6(\mathbb C)\simeq
\text{groupe des unités \inserted{\unsure{alg.}} de }Q\left('''+radical+r'''\right)'''
upper_identity_layout=upper_identity.replace(r'\simeq\mu_6',r'&\simeq\mu_6',1).replace(
    r'\text{groupe des unités ',r'\text{groupe des}\\'+'\n'+r'&\qquad\qquad\text{unités ',1)
de_fragment=r'\uline{\unsure{\deleted{de}}}'
cancelled_ring=r'\deleted{\mathbb Z[\zeta]\unsure{=}\mathbb Z[T]/}'
ring=r'\mathbb Z[\zeta]=\mathbb Z[T]/(1+T+T^2)'
zeta_definition=r'(\zeta=\exp 2i\pi/\unsure{3})'
pose=r'\deleted{\unsure{On pourra|On pose}} \inserted{On pose}'
base=r'\mathbb E\ell_1\deleted{(\unsure{S})}\simeq\mathbb C/\mathbb Z[\zeta]'
twist=r'\mathbb E\ell_1(S)\simeq\mathbb E\ell_1\mathbin{\wedge}_{\mathbb Z/6\mathbb Z}S'
contraction=r'\unsure{euclidiennem\textsuperscript{t}|euclidiennement}'
vector_origin=r'\unsure{vectoriel} euclidien $V_S$, \deleted{\unsure{centre}} \inserted{origine} étant'
network=r'le barycentre de $S$. On désigne par $V_S$ le \deleted{\unsure{lattice}} \inserted{réseau} engendré par $S$, et'
quotient=r'X_S=\mathbb E\ell_1(S)\simeq V_S/\Gamma_S'

figure=r'''\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
% Exposed pale construction strokes and their interrupted ends.
\draw[gray,line width=.3pt] (172,921) -- (218,1011);
\draw[gray,line width=.3pt] (173,923) .. controls (181,928) and (191,941) .. (196,930);
\draw[gray,line width=.3pt] (238,1045) -- (338,925);
\draw[gray,line width=.3pt] (343,925) -- (387,1004);
\draw[gray,line width=.3pt] (339,925) -- (322,1093);
\draw[gray,line width=.3pt] (338,943) .. controls (342,950) and (352,963) .. (348,967)
  .. controls (342,968) and (338,947) .. (338,943);
\draw[gray,line width=.3pt] (321,1114) -- (320,1159);
\draw[gray,line width=.3pt] (251,1151) -- (279,1168);
\draw[gray,line width=.3pt] (325,1189) -- (372,1219);
\draw[gray,line width=.3pt] (390,1230) -- (539,1304);
\draw[gray,line width=.3pt] (250,1215) -- (307,1189);
\draw[gray,line width=.3pt] (328,1177) -- (383,1151);
\draw[gray,line width=.3pt] (468,1195) -- (539,1301);
\draw[gray,line width=.3pt] (400,1298) .. controls (430,1306) and (446,1291) .. (465,1299)
  .. controls (488,1306) and (511,1291) .. (531,1298);
\draw[gray,line width=.3pt] (420,1125) -- (528,1081);
% Outer sides: retain the gaps at the exposed junctions.
\draw[line width=.65pt] (227,1062) .. controls (215,1093) and (196,1157) .. (179,1178)
  .. controls (209,1182) and (263,1184) .. (294,1180)
  .. controls (303,1178) and (308,1180) .. (310,1182);
\draw[line width=.65pt] (182,1189) -- (232,1291);
\draw[line width=.65pt] (242,1297) .. controls (288,1291) and (342,1295) .. (384,1298);
\draw[line width=.65pt] (389,1285) -- (461,1194);
\draw[line width=.65pt] (395,1065) .. controls (410,1089) and (437,1142) .. (456,1177);
\draw[line width=.65pt] (310,1197) -- (385,1293);
\draw[line width=.65pt] (232,1297) -- (301,1203);
\draw[gray,line width=.4pt] (322,1180) -- (392,1068);
% Heavy top edge and its visible downward terminal curl.
\draw[line width=1pt] (238,1055) .. controls (285,1058) and (315,1059) .. (337,1058)
  .. controls (354,1058) and (369,1060) .. (380,1060)
  .. controls (382,1060) and (383,1062) .. (383,1064);
\draw[gray,line width=.35pt] (240,1062) -- (337,1060) -- (378,1063);
\node[above,inner sep=0pt,font=\scriptsize] at (382,1054) {\unsure{}};
% Two exposed directed heavy radii, drawn with their visible wings.
\draw[line width=1pt] (317,1184) -- (285,1133) -- (228,1057);
\draw[line width=.85pt] (232,1073) -- (228,1057) -- (242,1063);
\draw[line width=1pt] (329,1184) .. controls (359,1187) and (413,1188) .. (463,1186);
\draw[line width=.85pt] (448,1178) -- (461,1186) -- (449,1193);
% Inner triangular strokes, retaining their irregular paths.
\draw[line width=.45pt] (316,1111) -- (246,1210);
\draw[line width=.45pt] (329,1111) .. controls (351,1153) and (367,1195) .. (380,1216);
\draw[line width=.45pt] (250,1223) .. controls (292,1227) and (338,1229) .. (372,1226);
\draw[line width=.45pt] (250,1158) .. controls (272,1197) and (293,1235) .. (308,1255);
\draw[line width=.45pt] (318,1255) -- (386,1152);
\draw[line width=.55pt] (252,1140) .. controls (285,1139) and (326,1148) .. (347,1144)
  .. controls (365,1145) and (380,1143) .. (386,1145);
\draw[line width=.35pt] (319,1146) -- (350,1151) -- (365,1151);
% Individually visible marks on the dotted oblique and vertical strokes.
\foreach \x/\y/\r in {318/1173/1.3,324/1163/1.3,333/1155/1.1,359/1114/1.3,360/1103/1.2,370/1090/1.1,377/1082/1.3}{\fill (\x,\y) circle[radius=\r];}
\draw[line width=.6pt] (381,1076) -- (385,1070) -- (386,1076);
\draw[line width=.35pt] (393,1084) -- (393,1094) (392,1108) -- (392,1118) (391,1130) -- (391,1139);
% Exposed right-hand extension, parallel strokes, and short marks.
\draw[line width=.45pt] (465,1068) -- (479,1070);
\draw[line width=.45pt] (492,1069) .. controls (506,1070) and (519,1067) .. (527,1071);
\draw[line width=.6pt] (532,1072) -- (539,1070) -- (543,1072);
\draw[line width=.55pt] (479,1157) -- (541,1072);
\draw[line width=.45pt] (488,1144) -- (533,1082);
\draw[gray,line width=.35pt] (481,1166) -- (486,1158) (501,1138) -- (507,1130) (535,1092) -- (546,1081) (553,1073) -- (559,1067);
\draw[line width=.45pt] (562,1067) -- (567,1066);
\draw[line width=.4pt] (420,1126) -- (426,1122) -- (437,1120);
\draw[line width=.4pt] (467,1177) -- (471,1175);
% Six irregular ringed points with dark centers.
\draw[line width=.6pt] (321,1103) ellipse[x radius=9,y radius=10];
\fill (320,1104) ellipse[x radius=4.5,y radius=6];
\draw[line width=.6pt] (392,1145) ellipse[x radius=10,y radius=9];
\fill (392,1145) circle[radius=5.5];
\draw[line width=.55pt] (381,1225) ellipse[x radius=10,y radius=9];
\fill (381,1225) ellipse[x radius=4.5,y radius=5.5];
\draw[line width=.55pt] (310,1264) ellipse[x radius=9,y radius=10];
\fill (310,1265) ellipse[x radius=4.5,y radius=5.5];
\draw[line width=.55pt] (241,1221) ellipse[x radius=9,y radius=11];
\fill (241,1221) ellipse[x radius=4.5,y radius=7];
\draw[line width=.55pt] (243,1144) ellipse[x radius=10,y radius=9];
\fill (242,1144) ellipse[x radius=5,y radius=4.5];
% Filled marks and the three exterior marked points.
\fill (237,1179) circle[radius=2.8];
\fill (285,1130) ellipse[x radius=3.6,y radius=4];
\fill (350,1131) ellipse[x radius=3.8,y radius=4.5];
\draw[line width=.65pt] (350,1133) -- (355,1134);
\fill (382,1187) ellipse[x radius=3.8,y radius=3];
\draw[line width=.5pt] (380,1185) .. controls (383,1179) and (387,1183) .. (387,1187);
\fill (275,1237) circle[radius=2.6];
\fill (351,1243) circle[radius=3];
\fill (460,1113) ellipse[x radius=2.1,y radius=3];
\fill (409,1144) circle[radius=1.6];
\fill (317,1184) circle[radius=3.8];
\draw[line width=.5pt] (169,915) -- (173,914) -- (174,918) -- (171,918) -- cycle;
\draw[gray,line width=.4pt] (342,905) ellipse[x radius=3.3,y radius=2.4];
\fill (341,913) ellipse[x radius=3.5,y radius=2.8];
\draw[gray,line width=.3pt] (337,892) -- (340,895);
\fill (542,1305) ellipse[x radius=3.6,y radius=1.8];
\draw[gray,line width=.3pt] (542,1308) -- (548,1313);
% Written labels; the small central round label remains ambiguous.
\node[anchor=east,inner sep=1pt] at (222,1037) {$\zeta$};
\node[anchor=west,inner sep=1pt] at (402,1030) {$-\bar\zeta$};
\node[anchor=west,inner sep=1pt] at (481,1189) {$1$};
\node[anchor=east,inner sep=1pt] at (226,1324) {$\bar\zeta$};
\node[anchor=west,inner sep=1pt] at (393,1325) {$-\zeta$};
\node[inner sep=0pt,font=\scriptsize] at (315,1209) {$\unsure{0|o}$};
\node[inner sep=0pt,font=\scriptsize] at (478,1261) {\unsure{}};
\end{tikzpicture}}'''

text=r'''\cotefile{148}
\scanpage{9}
\mspage{3}

B) Courbes \inserted{ell.} anharmoniques de type hexagonal.

La catégorie de ces courbes équivalente : celle des hexagones orientés,
i.e. des torseurs $S$ sous
\[
\begin{aligned}
'''+upper_identity_layout+r'''\\
&\simeq\text{groupe des unités}\\
&\qquad\text{'''+de_fragment+r'''}\quad '''+cancelled_ring+r'''\\
&\qquad '''+ring+r'''\\
&\qquad '''+zeta_definition+r'''
\end{aligned}
\]

'''+figure+'\n\n'+pose+'\n'+r'\['+'\n'+base+'\n'+r'\]'+'\n'+r'\['+'\n'+twist+'\n'+r'\]'+r'''

\uline{Construction} On réalise l'hexagone comb. $S$ '''+contraction+r''' (canonique), dans '''+vector_origin+r''' '''+network+r'''
\[
'''+quotient+r'''
\]
La structure euclidienne \uline{orientée} de $V_S$ définit la structure complexe de $X_S$.

\margin{8}
'''
(root/'work'/f'{page}.tex').write_text(text)

changes=[]
def change(place,Cfrag,Hfrag,final,name,words,kind,sheet,confidence='high',diffC=True,diffH=True,markedH=False,conseq=False):
    changes.append({'id':f'{page}-{len(changes)+1:02d}','place':place,
      'C':Cfrag,'H':Hfrag,'final':final,'evidence':evidence(name,words),
      'crop':crop(name),'box':coords[name],'confidence':confidence,'kind':kind,
      'error_sheet_kind':sheet,'differs_C':diffC,'differs_H':diffH,
      'marked_in_H':markedH,'consequential':conseq})
change('Opening prose, after équivalente',r'\unsure{:|à}','à',':','equivalence',
       'Two detached marks stand one above the other at the end of the baseline. No closed a-body is exposed. C’s first punctuation reading is retained. No est is added.',
       'other','Other',diffC=False)
change('Upper group identity, cubic radical and attached lower label',
       r'Q(\underbrace{\sqrt[3]{1}}_{\zeta})',r'\mathbf{Q}(\sqrt[3]{1})',
       r'Q\left('+radical+r'\right)','upper_identity',
       'Below the radical is a short nearly horizontal line ending in an upward right tip, with a separate ζ directly beneath. The contour and lower label are retained directly; H does not transcribe the lower ζ.',
       'drawing or diagram','Drawings and diagrams')
change('Cancelled units-ring line, including the initial de and final slash',
       r'\text{groupe des unités de} \deleted{\mathbb Z[\zeta]\unsure{=}\mathbb Z[T]/}',
       r'groupe des unités \struck{de $\mathbf{Z}[\zeta] = \mathbf{Z}[T]$},',
       r'\text{'+de_fragment+r'}\quad '+cancelled_ring,
       'units_ring',
       'The long cancellation touches the terminal portion of de, with a separate low stroke below the word. Its precise deletion scope remains doubtful and is marked in place. The algebraic sequence is crossed through, while a rising slash remains visible after the closing bracket. The cancelled equality is still uncertain under the crossing.',
       'deletion state','Struck text','medium')
Cfig=C[C.index(r'\figure{'):C.index(r'\deleted{\unsure{On pourra|On pose}}')].strip()
Hfig=H[H.index(r'\drawing{'):H.index(r'\struck{On pose}')].strip()
change('Left lattice drawing, all visible strokes, points and labels',Cfig,Hfig,figure,
       'lattice_drawing',
       'Six irregular rings with filled centers, six additional marks on the main rays, two small exterior marks beside the right ray, the central point and three upper/lower exterior marks were inspected. The top heavy edge ends in a downward curl; a distinct two-wing head is not exposed there, so the observed contour carries a local doubt. Both outer junction gaps and the dotted oblique and right vertical strokes are retained. Pale construction lines are drawn as their visible segments instead of completing idealized connections. The small round central label remains 0|o.',
       'drawing or diagram','Drawings and diagrams','medium')
change('Cancelled and replacement introduction to the elliptic formulas',
       pose,r'\struck{On pose} On pose',pose,'corrected_pose',
       'The lower text has an initial On and a longer crossed second word whose exposed stem and low returns favor pourra, but medial letters remain under the cancellation. On pose is separately written above it. The full C alternatives remain; the replacement is explicitly inserted.',
       'misread word','Struck text','low',diffC=False)
change('First elliptic formula, crossed argument after the subscripted name',
       base,r'\mathbb{E}\mathrm{l}_1 \simeq \mathbf{C}/\mathbf{Z}[\zeta] ; \note{dans la première formule, un argument biffé après $\mathbb{E}\mathrm{l}_1$}',
       base,'elliptic_base',
       'The parenthesized argument is visibly present after the lowered 1. Its upper portion is crossed; the lower curves support S but leave uncertainty. The parentheses and doubtful S are retained at the actual argument position. The separate short top stroke beside the final ζ belongs to the left square bracket’s detached cap.',
       'omission','Omissions','medium',diffC=False,markedH=True)
change('Second elliptic formula, group written beneath the wedge',
       twist,r'\mathbb{E}\mathrm{l}_1(S) \simeq \mathbb{E}\mathrm{l}_1 \wedge^{\mathbf{Z}/6\mathbf{Z}} S',
       twist,'elliptic_twist',
       'The wedge lies on the formula baseline, while Z/6Z is written lower and to its right, with final S back on the upper baseline. Both lowered 1s and the 6 were checked with the whole formula.',
       'misread symbol or index','Symbols and indices',diffC=False,conseq=True)
change('Underlined Construction label',r'\uline{Construction}',r'\emph{Construction.}',r'\uline{Construction}',
       'construction_start','The underline runs under the final letters. The following space before On contains no separate period.',
       'text not on the page','Text that is not on the page',diffC=False)
change('Construction paragraph, word following S',r'\unsure{euclidiennement}','euclidiennement',contraction,
       'euclidean_clause','After the exposed euclidienn- strokes, the compressed ending extends in a long terminal return that rises above the body. The intervening letters are not all separately exposed. The visibly contracted reading with raised t is therefore placed first, with the full-word reading retained as an explicit alternative; no expansion is settled.',
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','medium')
change('Construction paragraph, overworked initial word and origin correction',
       vector_origin,
       r'\struck{\ill{}} \uncertain{vectoriel} euclidien $V_S$, \add{origine en}\note{« origine » en interligne, au-dessus d’un mot biffé}',
       vector_origin,'vector_origin',
       'The initial v region is overworked, leaving vectoriel doubtful; an independent cancelled word before it is not securely separable. The broad cancellation after V_S overlies the proposed centre. Origine is written above that cancellation. The following word has the raised t and further linked body strokes of étant, retained as exposed. The cancelled centre remains uncertain.',
       'misread word','Words','medium',diffC=False,markedH=True)
change('Network-designation sentence, cancelled word below réseau',
       r'\deleted{\unsure{lattice}} \inserted{réseau}',
       r'\add{réseau}\note{« réseau » en interligne, au-dessus d’un mot biffé}',
       r'\deleted{\unsure{lattice}} \inserted{réseau}',
       'network_sentence','A tall initial loop and further vertical strokes remain under the strike beneath réseau. Lattice is kept as a doubtful reading of that crossed word. The insertion is attached there. The earlier V_S is visibly retained in the prose.',
       'omission','Omissions','medium',diffC=False,markedH=True)
change('Extreme lower-left marginal numeral',r'\margin{8}','[not transcribed]',r'\margin{8}',
       'lower_numeral','Two closed lobes meet at a narrow middle crossing, giving 8. It belongs to the lighter lower-margin hand.',
       'omission','Omissions',diffC=False)

D=[]
def decision(mark,status,reading,name,words,conf):
 D.append({'id':mark,'decision':status,'reading':reading,'evidence':words,
           'crop':f'{crop(name)} {coords[name]}','confidence':conf})
decision('M0089','first','anharmoniques','heading','The initial an-, tall h, linked middle sequence, descending q and final plural ending are exposed in the heading. Raised ell. has its separate insertion leader.','high')
decision('M0090','first','équivalente','equivalence','The accented initial e, descending q, linked middle and tall terminal t support équivalente. No separate est appears before it.','high')
decision('M0091','first',':','equivalence','Two detached marks occupy the punctuation position; there is no exposed a-loop.','high')
decision('M0092','undecided',r'\unsure{alg.}','upper_identity','The raised insertion has a compressed first mark, looped tall stroke and descending last letter. Alg. remains plausible, but the initial and terminal punctuation are too compressed to remove the doubt.','medium')
decision('M0093','undecided',r'\unsure{0|o}','lattice_drawing','The small label below the central point is a rounded loop; the numeral/letter distinction is not secured by this shape. Both readings are retained locally.','medium')
decision('M0094','undecided',contraction,'euclidean_clause','The long terminal return rises above the letter body, while the preceding compressed ending does not separately expose every letter. The contracted form is first and the full form remains an alternative.','medium')
decision('M0095','first','dans','euclidean_clause','A looped initial d, followed by the linked low a-n-s sequence, is visible after the comma.','high')
decision('M0096','undecided',r'\unsure{vectoriel}','vector_origin','The first letter region is overworked. The following e-c-t-o-r-i-e-l outline supports vectoriel, but the initial joins remain doubtful.','medium')
U=[
 {'place':'Cancelled units-ring equality','decision':'undecided','reading':r'\unsure{=}','evidence':evidence('units_ring','One equality bar is merged with the cancellation while the other is exposed.'),'confidence':'medium'},
 {'place':'Cancelled introduction before the first elliptic formula','decision':'undecided','reading':r'\unsure{On pourra|On pose}','evidence':evidence('corrected_pose','The longer lower second word favors pourra, but its medial letters remain crossed.'),'confidence':'low'},
 {'place':'Cancelled argument in the first elliptic formula','decision':'undecided','reading':r'\unsure{S}','evidence':evidence('elliptic_base','The lower double curve is exposed, but cancellation crosses the upper part.'),'confidence':'medium'},
 {'place':'Cancelled word beneath origine','decision':'undecided','reading':r'\unsure{centre}','evidence':evidence('vector_origin','The broad strike merges several low letter bodies; the proposed reading cannot be made fully secure.'),'confidence':'low'},
 {'place':'Cancelled word beneath réseau','decision':'undecided','reading':r'\unsure{lattice}','evidence':evidence('network_sentence','The tall loops and verticals survive, but the strike hides the medial and final joins.'),'confidence':'low'}
]

doubts=[
 {'place':'Raised insertion in the upper units identity','reading':r'\inserted{\unsure{alg.}}','alternatives':'alg. retained provisionally','confidence':'medium','reason':'Initial mark and final punctuation are compressed in the insertion.'},
 {'place':'de before the cancelled ring expression','reading':de_fragment,'alternatives':'Word included in the cancellation; or word remaining live with a touching strike and low line','confidence':'medium','reason':'The strike reaches the terminal part of the word, while its initial part is exposed. A separate low stroke is retained.'},
 {'place':'Equality in the cancelled ring expression','reading':r'\unsure{=}','alternatives':'= retained provisionally','confidence':'medium','reason':'Cancellation crosses the upper bar.'},
 {'place':'Denominator in the parenthesized ζ expression','reading':r'\unsure{3}','alternatives':'3 retained provisionally','confidence':'medium','reason':'The rounded return and lower hook are visible, but the medial waist is compressed.'},
 {'place':'Drawing, small round label below the central point','reading':r'\unsure{0|o}','alternatives':'0 | o','confidence':'medium','reason':'Its exposed loop does not secure numeral versus letter.'},
 {'place':'Drawing, right end of the top heavy edge','reading':r'\unsure{}','alternatives':'Downward terminal curl; arrow interpretation unresolved','confidence':'medium','reason':'The contour is reproduced directly; a separately exposed two-wing head is unavailable at that endpoint.'},
 {'place':'Drawing, pale lower-right construction strokes','reading':r'\unsure{}','alternatives':'Exact continuities beneath darker crossings remain unresolved','confidence':'medium','reason':'Visible pale segments are retained without completing hidden junctions.'},
 {'place':'Cancelled lower introduction before the elliptic formulas','reading':r'\deleted{\unsure{On pourra|On pose}}','alternatives':'On pourra | On pose','confidence':'low','reason':'The cancellation crosses the medial letters of the longer word.'},
 {'place':'First elliptic formula, crossed parenthesized argument','reading':r'\deleted{(\unsure{S})}','alternatives':'S retained provisionally inside the parentheses','confidence':'medium','reason':'The upper part is overwritten by cancellation.'},
 {'place':'Construction, compressed adverb after S','reading':contraction,'alternatives':r'euclidiennem\textsuperscript{t} | euclidiennement','confidence':'medium','reason':'The raised terminal return is visible, but the preceding contracted ending does not expose every letter.'},
 {'place':'Construction, initial word before euclidien','reading':r'\unsure{vectoriel}','alternatives':'vectoriel retained provisionally','confidence':'medium','reason':'The initial region is overworked; a separate cancelled word cannot be securely read there.'},
 {'place':'Cancelled word beneath origine','reading':r'\deleted{\unsure{centre}}','alternatives':'centre retained provisionally','confidence':'low','reason':'Several letter bodies merge with the cancellation.'},
 {'place':'Cancelled word beneath réseau','reading':r'\deleted{\unsure{lattice}}','alternatives':'lattice retained provisionally','confidence':'low','reason':'The strike hides the medial and final joins.'}
]

inventory=[]
def inv(kind,pos,first,hand='his hand'):
 inventory.append({'sheet_kind':'text','hand':hand,'element':f'E{len(inventory)+1:02d}','kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'})
inv('margin note','Top center','3')
inv('text','L01, heading','B) Courbes ... anharmoniques de type hexagonal.')
inv('insertion','Above Courbes/anharmoniques in L01','ell., with its insertion leader')
inv('text','L02–L04, opening prose','La catégorie de ces courbes équivalente : celle des hexagones orientés, i.e. des torseurs S sous')
inv('display','L05–L06, upper identity','Z/6Z ≃ μ_6(C) ≃ groupe des unités ... de Q(cubic radical)')
inv('insertion','Between upper identity baselines','alg., doubtful')
inv('drawing','Below the cubic radical','Short horizontal stroke with upturned right tip and ζ beneath')
inv('display','L07, continuation','≃ groupe des unités')
inv('deletion','L08, initial word of the cancelled continuation','de, deletion scope doubtful, with low stroke')
inv('deletion','L08, cancelled ring expression','Z[ζ] = Z[T]/, equality doubtful')
inv('display','L09, replacement ring expression','Z[ζ]=Z[T]/(1+T+T²)')
inv('display','L10, parenthesized expression','(ζ=exp 2iπ/3), denominator doubtful')
inv('drawing','Left middle','Hexagonal outline, inner triangular strokes, six ringed points, other filled marks, dotted rays, exterior pencil extensions, ζ labels, 1 and doubtful 0|o')
inv('deletion','L11, below the drawing’s upper half','On pourra|On pose, doubtful crossed lower text')
inv('insertion','Above L11 cancellation','On pose')
inv('display','L12, first elliptic formula','Eℓ_1 with cancelled parenthesized argument ≃ C/Z[ζ]')
inv('deletion','Within L12','Parenthesized S, doubtful under cancellation')
inv('display','L13, next formula','Eℓ_1(S) ≃ Eℓ_1 wedge with lowered Z/6Z and S')
inv('text','L14, construction opening',"Construction, underlined; On réalise l'hexagone comb.")
inv('text','L15, continuation','S euclidiennem with raised terminal return, (canonique), dans')
inv('text','L16, vector space clause','vectoriel, doubtful initial, euclidien V_S')
inv('deletion','L16, before étant','centre, doubtful')
inv('insertion','Above the L16 cancellation','origine')
inv('text','End of L16 through L17','étant le barycentre de S. On désigne par V_S')
inv('deletion','L18, after le','lattice, doubtful')
inv('insertion','Above the L18 cancellation','réseau')
inv('text','Remainder of L18','engendré par S, et')
inv('display','L19, final formula','X_S=Eℓ_1(S) ≃ V_S/Γ_S')
inv('text','L20–L21, final sentence','La structure euclidienne orientée de V_S définit la structure complexe de X_S.')
inv('margin note','Extreme lower-left margin','8','unattributed lighter hand')

second=[]
def box(kind,b,reading):
 second.append({'box':f'B{len(second)+1:02d}','kind':kind,'x0':b[0],'y0':b[1],'x1':b[2],'y1':b[3],'reading':reading})
box('Heading, raised insertion and top manuscript numeral; following prose descenders or ascenders are context only',
    [215,28,1650,270],r'\mspage{3}'+'\n'+r'B) Courbes \inserted{ell.} anharmoniques de type hexagonal.')
box('First prose baseline only; crossing descenders from the heading are context and excluded',
    [307,230,1635,373],'La catégorie de ces courbes équivalente :')
box('Complete upper group identity, including the raised insertion and attached radical note; lower continuation is context only',coords['upper_identity'],upper_identity)
box('Continuation of the group expression, cancelled line and replacement ring formula; upper radical-label tail is context only',
    coords['units_ring'],r'\simeq\text{groupe des unités}'+'\n'+r'\text{'+de_fragment+r'}\quad '+cancelled_ring+'\n'+ring)
box('Complete parenthesized expression below the ring formula',coords['zeta_definition'],zeta_definition)
box('Complete left drawing, including all labels, marked points, pale extensions and dotted strokes',coords['lattice_drawing'],figure)
box('Cancelled lower introduction and its raised replacement; complete words and cancellation',coords['corrected_pose'],pose)
box('Complete first elliptic formula, including the cancelled argument',[653,1268,1237,1393],base)
box('Complete following elliptic formula and its lowered group expression',coords['elliptic_twist'],twist)
box('Construction heading and its following opening baseline; complete underline and wording',coords['construction_start'],r"\uline{Construction} On réalise l'hexagone comb.")
box('Second construction baseline, including the whole compressed word; lower interlinear correction is context only',
    [240,1658,1550,1785],r'$S$ '+contraction+' (canonique), dans')
box('Third construction baseline with its cancellation and replacement; preceding-baseline descender is context only',
    coords['vector_origin'],vector_origin)
box('Two consecutive construction baselines including the crossed word and raised replacement; all wording in scope',
    [218,1870,1615,2103],network)
box('Complete final quotient formula; preceding prose is excluded',[537,2095,1149,2207],quotient)
box('Lower-left handwritten marginal numeral only; paper border is context',coords['lower_numeral'],r'\margin{8}')

coverage=[]
def cov(row,msg): coverage.append({'row':row,'disposition':msg})
cov(439,'Archive scan marker versus H editorial page marker; the visible manuscript 3 is retained by mspage and B01. Same page metadata, no source-word change.')
cov(440,'H de l’auteur is editorial page attribution, not source wording.')
cov(441,'148_scan009-01: retain the visible colon after équivalente; M0091 resolved to C’s first reading.')
cov(442,'Aligned environment syntax and line arrangement only.')
cov(443,'Display boundary syntax only; the entire upper identity is retained.')
cov(444,'148_scan009-02: preserve the radical’s attached line and lower ζ, absent from H’s formula.')
cov(445,'148_scan009-03: crossed sequence retains the final slash; de deletion scope stays explicitly doubtful.')
cov(446,'Aligned environment closure only.')
cov(447,'148_scan009-04: direct complete drawing replaces H’s descriptive drawing placeholder.')
cov(448,'148_scan009-04: coordinate and scale tokens belong to the drawing implementation, not additional source prose.')
cov(449,'148_scan009-04: all visible drawing labels and geometric strokes are included; token alignment crosses drawing code and H’s synopsis.')
cov(450,'148_scan009-04: same complete drawing evidence; no inferred extra label is introduced from H’s synopsis.')
cov(451,'148_scan009-04 and -05: complete drawing plus crossed lower introduction and raised On pose. C’s long code stretch is checked against the actual drawing; the cancelled word remains doubtful.')
cov(452,'Lowercase-letter typesetting difference after E: the exposed looped form is retained as ell. 148_scan009-06 separately records the physically present cancelled argument.')
cov(453,'148_scan009-06: parenthesized crossed argument retained in place, with S doubtful.')
cov(454,'Lowercase-letter typesetting difference only; looped ell retained. Complete formula is in B09.')
cov(455,'Same looped lowercase-letter convention as row 454; no additional physical locus.')
cov(456,'148_scan009-07: group expression is below the wedge, not in H’s raised position.')
cov(457,'H’s prose note describes the cancelled argument editorially. Actual argument is transcribed in 148_scan009-06 and B08; the editorial sentence is not copied as source ink.')
cov(458,'148_scan009-08: Construction is underlined without a following period.')
cov(459,'148_scan009-10: proposed centre retained under the actual cancellation, with doubt.')
cov(460,'148_scan009-10: raised origine followed by visible étant; H editorial placement commentary is not source prose.')
cov(461,'V_S is visibly written in the prose and retained. H sic explanation is editorial; the later formula retains its written Γ_S. No corrective substitution.')
cov(462,'148_scan009-11: doubtful lattice retained beneath the réseau insertion.')
cov(463,'H editorial insertion note; actual réseau insertion is retained with its crossed word in 148_scan009-11 and B13.')
cov(464,'Lowercase-letter typesetting difference only; source looped ell retained in the complete quotient formula B14.')
cov(465,'148_scan009-12: lighter marginal 8 retained from its own crop.')

report={
 'page':page,'reader':'reader_b','line_count':21,
 'layout':'Upright handwritten mathematical page, numbered 3 at top center. The heading carries a raised ell. insertion. Opening prose occupies three broad lines; its group expression steps rightward into two upper baselines, a continuation, a crossed line, a replacement and a parenthesized expression. The detailed lattice drawing occupies the left middle beside these displays and the corrected On pose. Two elliptic formulas follow at center-right. A lower construction paragraph contains two further cancelled-word/replacement pairs and a final quotient formula, ending in a two-line sentence. A lighter 8 stands at lower left. The count covers 21 principal prose/formula baselines, including the crossed introduction line; interlinear insertions, marginal numbers and drawing labels are inventoried separately.',
 'changes':changes,'decisions':D,'unnumbered_decisions':U,'inventory':inventory,
 'doubts':doubts,
 'notation':[
  {'form':r'\mathbb Z/6\mathbb Z\simeq\mu_6(\mathbb C)','meaning':'The written group expression introduced after torseurs S sous. This records the source expression.','evidence':evidence('upper_identity','Both lowered sixes and the double-stroked Z forms are exposed.'),'scope':'Upper identity and the lowered group in the second elliptic formula checked.'},
  {'form':r'\mathbb Z[\zeta]=\mathbb Z[T]/(1+T+T^2)','meaning':'The replacement ring expression written beneath the cancelled version.','evidence':evidence('units_ring','Active lower line has clear brackets, equality, quotient slash, 1, plus signs, T and raised 2.'),'scope':'Active line and the corresponding bracketed term in the first elliptic formula.'},
  {'form':r'\mathbb E\ell_1;\quad\mathbb E\ell_1(S)','meaning':'Names in the two middle formulas and final quotient formula; the first carries a cancelled parenthesized argument.','evidence':'elliptic_base, elliptic_twist and final_quotient crops: double-stroked E, looped lowercase letter and lowered 1.','scope':'All occurrences on this page.'},
  {'form':r'\mathbin{\wedge}_{\mathbb Z/6\mathbb Z}','meaning':'The written wedge with the group below it in the second elliptic formula.','evidence':evidence('elliptic_twist','Group is lower than both wedge and final S.'),'scope':'This occurrence only.'},
  {'form':r'V_S\text{ in the prose};\quad V_S/\Gamma_S\text{ in the final formula}','meaning':'Literal forms preserved in their separate written positions. The prose calls V_S the generated réseau; the final formula uses Γ_S as denominator.','evidence':'network_sentence and final_quotient crops.','scope':'Every exposed V_S and the final Γ_S on this page checked; no intended replacement imposed.'}
 ],
 'abbreviations':[
  {'form':'ell.','expansion':'elliptiques (tentative)'},
  {'form':'alg.','expansion':'algébriques (tentative; the written insertion remains doubtful)'},
  {'form':'i.e.','expansion':'id est (tentative)'},
  {'form':'comb.','expansion':'combinatoire (tentative)'},
  {'form':r'euclidiennem\textsuperscript{t}','expansion':'euclidiennement (tentative alternative only; the compressed written ending is not settled)'},
  {'form':'exp','expansion':'exponentielle (tentative)'}
 ],
 'hand':[
  {'habit':'Reduced low joining strokes compress interior letters; tall ascenders and descenders remain clearer. A long terminal return can rise above the word body.','places':'équivalente, the compressed euclidean word, vectoriel and both occurrences of groupe','scope':'Only these exposed occurrences on this page','witness_errors':'Both witnesses give the full euclidean word; change 09 retains the contracted/full alternatives. The first vectoriel region stays doubtful.'},
  {'habit':'The left square bracket can have a detached short upper cap, set above and left of ζ.','places':'Active ring expression and first elliptic formula','scope':'Both exposed bracketed ζ terms checked','witness_errors':'No extra overbar is added to the ζ inside these brackets.'},
  {'habit':'The lowercase letter after the double-stroked E has a tall loop with a curved lower return.','places':'Both middle elliptic formulas and final quotient','scope':'All four exposed names on this page','witness_errors':'C’s looped ell form is retained; H’s roman-l macro differences are treated as typesetting, while the cancelled argument and lowered group receive substantive rows.'},
  {'habit':'Cancellation lines traverse complete mathematical spans but can touch only the terminal part of an adjacent word.','places':'de before the cancelled ring expression; corrected introduction; centre and lattice cancellations','scope':'Each correction inspected independently','witness_errors':'The de deletion boundary and crossed lexical readings remain explicitly uncertain.'},
  {'habit':'Lattice strokes mix heavy black radii, thinner black polygon lines, small discrete marks and very pale construction traces.','places':'Left-middle drawing','scope':'All six ringed points, the additional filled marks, endpoint shapes and visible dotted segments counted and inspected twice','witness_errors':'C’s completed polygon and top-edge arrowhead are replaced by the exposed broken contours; H’s synopsis is replaced by a direct drawing.'},
  {'habit':'The lighter lower-margin numeral has two closed lobes.','places':'Lower-left 8','scope':'This numeral only','witness_errors':'H omits the marginal numeral.'}
 ],
 'legibility':'The main handwriting is dark with broad spacing, and most prose and active formulas can be followed in the prepared halves. Medial cursive joins are compressed in several words. The crossed introduction, the cancelled argument, and the words beneath origine and réseau retain genuine letter uncertainty; de also retains uncertainty in cancellation scope. The radical attachment is clearly exposed, while the denominator in the following parenthesized expression has a compressed 3-like return. The lattice drawing has strong labels and six clear ringed points, with darker radii crossing much lighter construction traces; several thin junctions cannot be followed continuously beneath those crossings. The opening colon and the group’s lowered position are supported by their crops. C and H agree on much of the prose, but H’s definite à, raised wedge group, Construction period and shortened or unnamed cancelled readings are adjusted or retained as doubts according to this page. Both witnesses’ expanded euclidean word is replaced by a local contracted/full alternative. The final V_S and Γ_S forms are preserved exactly at their written positions.',
 'notes':'L01 names Courbes ell. anharmoniques de type hexagonal, with ell. added above the line. L02–L04 present the category wording and describe oriented hexagons as torseurs S under the following written group; the source has équivalente : and no inserted est. L05–L10 give the group and ring expressions, including the cancelled line, the radical’s lower ζ annotation and the doubtful final denominator. These are reported source claims and notation, not a checked equivalence or a new theorem. The left drawing is reproduced from its visible strokes: six inner ringed points, further filled marks, two exposed heavy directed radii, a heavy top edge with an unresolved endpoint interpretation, dotted strokes and pale exterior constructions. The crossed introduction below it remains On pourra|On pose, with On pose inserted above. L12–L13 write the two elliptic formulas. L14–L19 describe an oriented Euclidean realization of the combinatorial hexagon, give its barycenter as origin, name the generated réseau with V_S in the prose, and then write X_S=Eℓ_1(S) ≃ V_S/Γ_S. The prose and formula letter choices are retained without correction. L20–L21 state that the oriented Euclidean structure supplies the complex structure; this is an attribution to the manuscript, not an independently checked mathematical result. No proof or computation was performed. Whole scan and both prepared halves were inspected, then all fifteen tight crops. Some neighboring descenders enter narrow text regions, so neutral blind-box scopes explicitly identify the target baseline and exclude crossing context. The heading and network boxes extend beyond the initial crop bounds to include complete exposed ascenders/descenders already seen in the whole/half views; no decided locus was recropped. Every handwritten numeral, insertion, cancellation, source/current doubtful formula and C/H lexical disagreement has a localized complete target.',
 'check_events':[],
 'second_boxes':second,'diff_coverage':coverage,
 'deletion_insertion_check':'Raised ell. attaches between Courbes and anharmoniques. Raised alg., still doubtful, attaches between unités and de in the upper identity. The radical carries its own short lower line and ζ note. The units-ring cancellation covers the algebraic sequence; its contact with de has explicitly doubtful scope, and the separate low stroke under de is preserved. The longer lower On phrase is cancelled and replaced by On pose above. The first elliptic formula has a cancelled parenthesized argument after the lowered 1. The initial vectoriel region is overworked; no independent extra cancelled word is securely separable. After V_S, the crossed proposed centre is replaced by origine above, followed by visible étant. After le, the crossed proposed lattice is replaced by réseau above. Each exposed cancellation and attachment has its own inventory entry and blind target; crossed letters stay doubtful where the strike hides them.'
}
(root/'work'/f'{page}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print({'written':page,'changes':len(changes),'decisions':len(D),'unnumbered_decisions':len(U),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(coverage),'crops':len(coords)})
