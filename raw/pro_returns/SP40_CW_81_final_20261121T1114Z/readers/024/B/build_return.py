import datetime
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[3]
GROUPS = {}

def group(gid, body, **meta):
    GROUPS[gid] = meta
    return '% BEGIN ' + gid + '\n' + body.strip() + '\n% END ' + gid + '\n'

parts = []
parts.append(group('B024-ADMIN', r'''\scanpage{24}
% Independent reader B; literal shapes below are manual approximations, without rendered or metric validation.
% Vertical bars inside unsure arguments separate editorial alternatives; they are not manuscript punctuation.''', owns='Administrative scan marker; no manuscript words', kind='administrative'))

parts.append(group('B024-P01', r'''\unsure{Considérons|Considerons} la partition $\Pi_I^{\unsure{\circ|0}}$ de $X\setminus\bigcup_{\unsure{\alpha'|i}\in I}E_{\alpha'}$, soit $S$ l'ens des classes, notées $U_s$ $(s\in S)$. \deleted{\unsure{On a|On}} Considérons la''', owns='Complete opening through the second Considérons la; both occurrences of Considérons are separate physical words.', kind='text', candidates=[r'Considérons',r'Considerons',r'\Pi_I^\circ',r'\Pi_I^0',r"\bigcup_{\alpha'\in I}",r'\bigcup_{i\in I}',r"E_{\alpha'}",r'E_i',r'\deleted{On a}',r'\deleted{On}']))

parts.append(group('B024-G01', r'''\figure{\begin{tikzpicture}[x=1ex,y=1ex,baseline=(oldlemma.base)]
\path[use as bounding box] (-.3,-1.1) rectangle (29,5.2);
\node[anchor=base west,inner sep=0,outer sep=0] (oldlemma) at (0,0) {\rlap{\uline{Lemme}}\phantom{\deleted{\uline{Lemme}}}};
\node[anchor=base west,inner sep=0,outer sep=0] (oldforall) at (12,1) {\rlap{$\forall i\in I,$}\phantom{\deleted{$\forall i\in I,$}}};
\node[anchor=base west,inner sep=0,outer sep=0] (newrelation) at (.4,3.5) {\inserted{Relation $R$ entre $S$ et $I$}};
\draw[line width=.55pt] (-.2,.3) -- (22.7,2.05);
\end{tikzpicture}}''', owns=r'Deleted underlined Lemme and deleted forall i in I comma; the whole inserted Relation R entre S et I. No adjoining Considérons or display text.', kind='drawing', observed_bbox=[300,395,1135,561], origin='oldlemma.base west at (0,0); manual layout origin near original (320,520)', parent_units='x=1ex, y=1ex; fixed local rectangle; nodes base-west with zero inner/outer separation', candidates=[r'\deleted{\uline{Lemme} $\forall i\in I,$}',r'\inserted{Relation $R$ entre $S$ et $I$}']))

precursor = group('B024-G02', r'''% The high point has unresolved role, hand and attachment; it is present once above the deleted glyph.
\overset{\hspace{-1ex}\unsure{\cdot}}{\deleted{\unsure{U|E}}}''', owns='Deleted precursor U/E and its one high point only; live opening parenthesis and s remain outside.', kind='math group', observed_bbox=[625,530,708,628], origin='standard mathematical overset above deleted precursor; point shifted left by 1ex', parent_units='standard math boxes; explicit point shift -1ex; no inferred attachment', candidates=[r'\deleted{U}',r'\deleted{E}',r'one high point with unresolved role/hand/attachment'])
arrow = group('B024-G03', r'''\mathrel{\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.25ex]
\path[use as bounding box] (0,-.45) rectangle (4.6,2.5);
\node[anchor=base,inner sep=0,outer sep=0] (deflabel) at (2.45,1.2) {\scriptsize def};
\draw[line width=.45pt] (.8,.95) .. controls (.25,.88) and (-.05,.28) .. (.08,.02) .. controls (.3,-.2) and (.8,-.16) .. (1.3,-.11) -- (4.45,.12);
\draw[line width=.45pt] (.09,.34) .. controls (1.7,.5) and (3.1,.45) .. (4.18,.35);
\draw[line width=.6pt] (4.04,.52) .. controls (4.5,.28) and (4.57,.1) .. (4.43,-.05) -- (4.14,-.23);
\end{tikzpicture}}''', owns='The label def and complete double-shaft arrow, with rounded left return and right head; no U expression.', kind='drawing', observed_bbox=[1010,510,1140,620], origin='local baseline 0; left return near (0,0)', parent_units='x=1ex, y=1ex, fixed bounding rectangle; def node base anchor', candidates=['def', 'double shaft with rounded left return and right pointed end; no newly assigned mathematical relation'])
parts.append(group('B024-DISPLAY', r'\['+'\n'+precursor+r'(s,i)\in R\ '+ '\n'+arrow+r'\ \overline{U_s}\cap E_i\ne\varnothing.'+'\n'+r'\]', owns='Complete definition display, including its final point, excluding no child-owned material from the page.', kind='display'))

tuple_group = group('B024-G04', r'''% Complete states: (S,I)\deleted{R}) | (S,I\deleted{)},R).
% The qualifier belongs to the whole right-hand correction, not to the already clear S,I letters alone.
\unsure{\begin{tikzpicture}[x=1ex,y=1ex,baseline=(tupleprefix.base)]
\path[use as bounding box] (0,-1.1) rectangle (8.9,2.7);
\node[anchor=base west,inner sep=0,outer sep=0] (tupleprefix) at (0,0) {$(S,I$};
\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\phantom{$(S,I)\deleted{R})$}};
\draw[line width=.6pt] (4.35,2.3) .. controls (4.55,1.2) and (4.3,.2) .. (3.9,-.55);
\draw[line width=.5pt] (5.25,1.95) -- (5.05,-.1) .. controls (5,-.2) and (4.95,-.3) .. (4.8,-.2);
\draw[line width=.5pt] (5.18,1.65) .. controls (5.9,2.35) and (6.4,2.0) .. (5.8,1.1) .. controls (5.35,.7) and (5.25,.45) .. (5.55,.2) -- (6.0,-.2);
\draw[line width=.55pt] (4.95,1.95) -- (6.65,2.5);
\draw[line width=.55pt] (4.8,1.0) -- (6.28,1.72);
\draw[line width=.55pt] (5.25,.52) -- (7.1,1.4) -- (5.7,.62);
\draw[line width=.55pt] (5.63,.2) .. controls (6.7,.2) and (8.45,.45) .. (8.0,-.1) .. controls (7.6,-.5) and (7.15,-.67) .. (7.42,-.95) .. controls (7.9,-1.1) and (8.55,-.1) .. (8.65,1.05) .. controls (8.7,1.6) and (8.55,2.1) .. (8.45,2.25);
\end{tikzpicture}}''', owns='Complete tuple (S,I plus the first closing stroke, R/cancellation cluster, long lower return and final close). Adjacent de remains outside.', kind='math group', observed_bbox=[1340,640,1625,780], origin='tupleprefix.base west=(0,0); manual right-cluster placement', parent_units='x=1ex, y=1ex; fixed rectangle; base-west nodes zero separation', candidates=[r'(S,I)\deleted{R})',r'(S,I\deleted{)},R)'], qualification='Whole corrected right cluster; no inferred writing chronology')
parts.append(group('B024-P02', r'\uline{Lemme} Cette relation fait de'+'\n'+tuple_group, owns='Lemma heading through its complete tuple.', kind='text'))

rule = group('B024-G05', r'''\llap{\begin{tikzpicture}[x=.18pt,y=-.18pt,baseline=(ruletop)]
\path[use as bounding box] (-10,0) rectangle (45,405);
\coordinate (ruletop) at (25,0);
\draw[line width=.45pt] (13,39) .. controls (18,28) and (18,11) .. (20,4) .. controls (23,-1) and (25,3) .. (25,15) .. controls (22,81) and (20,117) .. (23,163) .. controls (30,241) and (27,324) .. (29,396);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\unsure{\begin{tikzpicture}[x=.18pt,y=-.18pt,baseline=0pt]
\path[use as bounding box] (-10,0) rectangle (45,405);
\draw[black!65,line width=.25pt] (1,82) -- (-2,91) -- (-5,98);
\draw[black!55,line width=.3pt] (-7,103) -- (-8,107);
\end{tikzpicture}}};
\end{tikzpicture}\quad}''', owns='Left lemma rule, its hooked upper return, and separate two-piece pale trace only; no words.', kind='drawing', observed_bbox=[245,750,335,1195], origin='ruletop=(25,0); approximate original origin near (272,783)', parent_units='x=.18pt, y=-.18pt, fixed rectangle -10..45 by 0..405; nested trace uses identical units/origin', candidates=['continuous rule with hooked upper return', 'separate oblique run plus lower fleck: role/hand/surface origin unresolved'])
sommets = group('B024-G06', r'''\begin{tikzpicture}[x=1ex,y=1ex,baseline=(sommets.base)]
\node[anchor=base west,inner sep=0,outer sep=0] (sommets) at (0,0) {sommets};
\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\unsure{\begin{tikzpicture}[x=1ex,y=1ex,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (7,2.5);
\fill (5.05,1.8) -- (5.2,2.04) -- (5.32,1.97) -- (5.2,1.76) -- cycle;
\end{tikzpicture}}};
\end{tikzpicture}''', owns='Complete word sommets and its one high triangular point; comma remains outside.', kind='word group', observed_bbox=[635,905,935,977], origin='sommets.base west=(0,0); point relative to its e/t zone', parent_units='outer and nested x=1ex,y=1ex; fixed nested rectangle; zero separation base-west nodes', candidates=['sommets with high point of unresolved letter/independent-mark attachment, hand and role'])
leword = group('B024-G07', r'''% Complete word candidates: Le | Ce. The detached upper hooked run stays with the qualified word.
\unsure{\begin{tikzpicture}[x=.2pt,y=-.2pt,baseline=(lebase)]
\path[use as bounding box] (0,0) rectangle (85,65);
\coordinate (lebase) at (0,57);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,57) {\phantom{Le}};
\draw[line width=.6pt] (2,14) -- (7,55) .. controls (17,56) and (26,53) .. (31,57) .. controls (39,63) and (46,53) .. (53,49) .. controls (48,55) and (49,57) .. (58,56) -- (83,55);
\fill (14,15) -- (14,8) -- (25,0) -- (32,1) -- (36,0) -- (37,4) -- (33,6) -- (27,5) -- (18,13) -- cycle;
\end{tikzpicture}}''', owns='Only Le/Ce, including its upper detached run; adjoining graphe remains ordinary prose outside.', kind='word group', observed_bbox=[1098,965,1185,1038], origin='local observed word box upper-left near (1100,970); lebase=(0,57)', parent_units='x=.2pt,y=-.2pt; explicit rectangle; zero-separation annotation node', candidates=['Le','Ce'])
parts.append(group('B024-P03', r'\noindent'+'\n'+rule+r'un graphe strict ayant $S$ comme \unsure{ens des|ens de}'+'\n'+sommets+r", $I$ comme ens. \unsure{de |d'}\unsure{arêtes|arètes|aretes}.). \deleted{Cette relation}"+'\n'+leword+r'graphe est un \uline{arbre}', owns='Complete vertically marked lemma paragraph; all source groups own only their specified local components.', kind='text', candidates=['ens des','ens de','de arêtes','de arètes','de aretes',"d'arêtes","d'arètes","d'aretes",'.).']))

faint = group('B024-M04', r'''\rlap{\unsure{\begin{tikzpicture}[x=1ex,y=1ex,baseline=0pt]
\path[use as bounding box] (-1.5,-2.8) rectangle (0,0);
\draw[black!25,line width=.25pt] (-1.1,-.8) .. controls (-.55,-1.1) and (-.4,-1.8) .. (-.7,-2.1) -- (-1.2,-2.5) -- (-1.5,-2.5);
\end{tikzpicture}}}''', owns='Faint bent trace left below fait only; fait remains outside.', kind='mark', observed_bbox=[534,1286,563,1347], origin='manual position left below following fait; mark-only group', parent_units='x=1ex,y=1ex; fixed local rectangle', candidates=['faint bent trace, no character; role/hand/surface origin unresolved'])
quona = group('B024-G08', r'''% Whole phrase remains qualified. Complete states: qu'on a | qu'on followed by an independent point.
% The final point-shaped a has its own unresolved role/hand/attachment within that whole-phrase uncertainty.
\unsure{\begin{tikzpicture}[x=.12pt,y=-.12pt,baseline=(qubase)]
\path[use as bounding box] (0,0) rectangle (190,130);
\coordinate (qubase) at (0,35);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,35) {\phantom{qu'on a}};
\draw[line width=.45pt] (4,20) .. controls (-1,10) and (3,4) .. (11,11) .. controls (26,25) and (24,34) .. (10,30) .. controls (-2,26) and (-2,18) .. (4,20);
\draw[line width=.4pt] (20,29) .. controls (26,62) and (33,100) .. (39,123) .. controls (38,130) and (31,126) .. (29,122);
\draw[line width=.45pt] (20,29) -- (27,15) .. controls (43,21) and (53,17) .. (67,17) -- (72,2) -- (79,10);
\draw[line width=.4pt] (96,18) .. controls (119,17) and (129,17) .. (142,17) -- (148,20);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,35) {\unsure{\begin{tikzpicture}[x=.12pt,y=-.12pt,baseline=(pointbase)]
\path[use as bounding box] (0,0) rectangle (190,130);
\coordinate (pointbase) at (0,35);
\fill (181,13) -- (187,12) -- (190,15) -- (187,19) -- (181,18) -- cycle;
\end{tikzpicture}}};
\end{tikzpicture}}''', owns="Entire qu'on a phrase, including the final solid point-shaped a, exactly once; following un stays outside.", kind='phrase group', observed_bbox=[710,1225,910,1362], origin='qubase=(0,35), local origin near (714,1232); nested point shares origin/baseline', parent_units='outer and inner x=.12pt,y=-.12pt; fixed common rectangle; base-west zero separation', candidates=["qu'on a", "qu'on followed by an independent point"], qualification='whole phrase; final point independently qualifies role, hand and attachment')
ya = group('B024-G09', r'''\begin{tikzpicture}[x=1ex,y=1ex,baseline=(yword.base)]
\node[anchor=base west,inner sep=0,outer sep=0] (yword) at (0,0) {y};
\node[anchor=base west,inner sep=0,outer sep=0] (aword) at (3,0) {a};
\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\unsure{\begin{tikzpicture}[x=1ex,y=1ex,baseline=0pt]
\path[use as bounding box] (0,-.5) rectangle (4,1.2);
\draw[black!40,line width=.25pt] (1.45,.08) -- (1.95,.28);
\draw[black!45,line width=.25pt] (2.1,.34) -- (2.85,.59);
\end{tikzpicture}}};
\end{tikzpicture}''', owns='The whole live y a and the two pale entry runs between them; cancelled existe/ex and exactly wording outside.', kind='phrase group', observed_bbox=[1370,1330,1488,1405], origin='yword.base west=(0,0); aword at (3,0); nested runs share origin', parent_units='outer and inner x=1ex,y=1ex; base-west zero separation', candidates=['y a; two pale interrupted entry runs, role/attachment/hand unresolved'])
parts.append(group('B024-P04', r'\unsure{le|Le} '+faint+'fait\n'+quona+r'un graphe strict signifie que a) $\forall i\in I$, Il \deleted{\unsure{existe|ex}}'+'\n'+ya+r"exactement deux $U_s$ tels que $\overline{U_s}\cap E_i\ne\varnothing$, et b) $i$ est caractérisé par l'ens de ces deux $U_s$.", owns='Complete conditions paragraph a) and b). Each word-bearing child is exclusive at its local source occurrence.', kind='text', candidates=['le','Le',r'\deleted{existe}',r'\deleted{ex}']))

def sigma(gid, body, meta, qualify=False, annotation=r'\Sigma_i^-'):
    content = r'''\begin{tikzpicture}[x=.22pt,y=-.22pt,baseline=(sigbase)]
\path[use as bounding box] (0,0) rectangle (110,65);
\coordinate (sigbase) at (0,45);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,45) {\phantom{$'''+annotation+r'''$}};
'''+body+r'''
\end{tikzpicture}'''
    if qualify:
        content = r'\unsure{'+content+'}'
    return group(gid, content, kind='math glyph group', origin='sigbase=(0,45); all body, head, index and sign paths share one local origin', parent_units='x=.22pt,y=-.22pt; fixed rectangle (0,0)..(110,65), zero-separation annotation node', **meta)

s1=sigma('B024-S01', r'''% Complete primary Sigma_i^+; detached head/retrace/independent-rule role unresolved here.
\draw[line width=.6pt] (14,14) -- (13,7) .. controls (20,2) and (37,3) .. (58,2);
\draw[line width=.25pt] (3,17) -- (7,18);
\draw[black!50,line width=.25pt] (8,18) -- (17,19);
\draw[line width=.6pt] (21,20) -- (45,25) .. controls (53,28) and (35,35) .. (5,46) -- (62,43);
\draw[line width=.6pt] (73,29) -- (74,51);
\fill (72,20) -- (75,21) -- (75,24) -- (73,25) -- cycle;
\draw[line width=.65pt] (84,0) -- (84,16);
\draw[line width=.65pt] (76,7) -- (92,7);''', dict(owns='First complete Sigma_i^+ only; following comma outside.', observed_bbox=[612,1758,711,1826], candidates=[r'\Sigma_i^+ with bent detached upper run: head/retrace or independent-rule role unresolved']), True, r'\Sigma_i^+')
s2=sigma('B024-S02', r'''% Local upper run remains detached; same primary printed under the first-occurrence rule.
\draw[line width=.55pt] (10,4) -- (39,1);
\draw[line width=.5pt] (4,12) -- (28,18) .. controls (40,22) and (23,36) .. (5,45) .. controls (3,49) and (30,43) .. (40,46) .. controls (46,47) and (45,54) .. (44,58);
\draw[line width=.6pt] (52,30) .. controls (54,33) and (54,37) .. (52,40);
\draw[line width=.6pt] (66,3) -- (87,3);''', dict(owns='Second complete Sigma_i^- only; following les outside.', observed_bbox=[736,1758,812,1825], candidates=[r'\Sigma_i^- with separate short upper run: head/retrace or independent-rule role unresolved']), False)
uplus=group('B024-G10', r'''% Complete candidates U_{s_+} | U_{s_-}; no inferred earlier state of the filled sign.
\unsure{\begin{tikzpicture}[x=.18pt,y=-.18pt,baseline=(ubase)]
\path[use as bounding box] (0,0) rectangle (115,120);
\coordinate (ubase) at (0,73);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,73) {\phantom{$U_{s_+}$}};
\draw[line width=.6pt] (2,16) .. controls (8,-3) and (15,1) .. (22,27) .. controls (24,40) and (24,59) .. (29,63) .. controls (34,69) and (48,22) .. (50,7) .. controls (50,37) and (47,64) .. (53,70) .. controls (62,80) and (70,65) .. (78,63);
\draw[line width=.45pt] (78,63) .. controls (83,58) and (87,61) .. (79,67) .. controls (77,70) and (84,82) .. (86,83) -- (90,87) -- (80,90);
\fill (91,96) -- (95,92) -- (104,92) -- (105,89) -- (107,92) -- (115,92) -- (115,97) -- (109,102) -- (113,104) -- (114,108) -- (95,109) -- (91,106) -- cycle;
\node[anchor=base west,inner sep=0,outer sep=0] at (0,73) {\unsure{\begin{tikzpicture}[x=.18pt,y=-.18pt,baseline=(unearbase)]
\path[use as bounding box] (0,0) rectangle (115,120);
\coordinate (unearbase) at (0,73);
\draw[black!35,line width=.6pt] (101,80) -- (103,77);
\fill[black!45] (110,77) circle (.9);
\end{tikzpicture}}};
\end{tikzpicture}}''', owns='First signed U, its low s, filled plus/minus candidate and two pale neighbouring marks; contenu outside.', kind='math glyph group', observed_bbox=[935,1965,1035,2060], origin='ubase=(0,73); nested unearbase same origin/baseline', parent_units='outer/inner x=.18pt,y=-.18pt; common fixed rectangle; zero separation', candidates=[r'U_{s_+}',r'U_{s_-}', 'two neighbouring pale marks: role/hand/attachment/surface origin unresolved'])
s3=sigma('B024-S03', r'''% Complete candidates Sigma_i^+ | Sigma_i^-; filled raised sign remains qualified locally.
\draw[line width=.65pt] (3,7) .. controls (25,3) and (36,4) .. (58,4);
\draw[line width=.6pt] (22,7) .. controls (54,18) and (41,19) .. (8,40) .. controls (-2,48) and (35,43) .. (60,46) .. controls (66,48) and (66,55) .. (63,58);
\draw[line width=.65pt] (72,25) .. controls (75,21) and (74,30) .. (72,35);
\fill (82,5) -- (87,5) -- (88,3) -- (90,5) -- (95,5) -- (97,9) -- (97,16) -- (83,16) -- (80,12) -- cycle;''', dict(owns='Complete first chosen-side Sigma_i with its filled raised plus/minus candidate; following tel outside.', observed_bbox=[1450,1961,1567,2016], candidates=[r'\Sigma_i^+',r'\Sigma_i^-'], qualification='raised sign only; local head visibly joined/crowded with the body'), True, r'\Sigma_i^{+|-}')
s4=sigma('B024-S04', r'''\draw[line width=.5pt] (2,2) -- (56,7);
\draw[line width=.55pt] (19,7) .. controls (47,16) and (45,23) .. (11,43) .. controls (3,49) and (35,47) .. (59,51) .. controls (65,52) and (65,57) .. (62,60);
\draw[line width=.6pt] (70,34) -- (67,46);
\draw[line width=.5pt] (83,9) -- (103,11);''', dict(owns='Parenthetical complete Sigma_i^- immediately before the comma; following reduced word outside.', observed_bbox=[1448,2070,1547,2130], candidates=[r'\Sigma_i^-'], qualification='local head/body crowded join; no separate outer closure rule supplied'))
definit=group('B024-G11', r'''% Complete word definit (no accent); the final i body is dotless so its two observed upper pieces are not duplicated.
\begin{tikzpicture}[x=1ex,y=1ex,baseline=(definitword.base)]
\node[anchor=base west,inner sep=0,outer sep=0] (definitword) at (0,0) {defin\i{}t};
\node[anchor=base west,inner sep=0,outer sep=0] at (0,0) {\unsure{\begin{tikzpicture}[x=1ex,y=1ex,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (6.2,2.4);
\draw[black!45,line width=.25pt] (4.95,1.16) -- (4.84,1.66);
\fill (4.78,1.64) circle (.07);
\fill (5.2,1.55) -- (5.25,1.28) -- (5.4,1.24) -- (5.34,1.46) -- cycle;
\end{tikzpicture}}};
\end{tikzpicture}''', owns='Complete word definit, with dotless final i plus the two upper pieces once; following un outside.', kind='word group', observed_bbox=[355,2190,544,2282], origin='definitword.base west=(0,0); explicit mark placement over final i', parent_units='outer/inner x=1ex,y=1ex; shared base-west origin, zero separation', candidates=['definit', 'final i upper pair: both pieces as its dot/entry or one independent fleck; attachment and hand unresolved locally'])
s5=sigma('B024-S05', r'''% This complete local form was settled on half b, not reopened for a crop.
\draw[line width=.5pt] (12,3) -- (54,0);
\draw[line width=.5pt] (5,12) -- (33,18) .. controls (43,21) and (24,34) .. (6,43) -- (57,43);
\draw[line width=.5pt] (70,31) -- (70,45);
\fill (69,23) circle (.9);
\draw[line width=.5pt] (84,4) -- (103,4);''', dict(owns='Complete final Sigma_i^- after subset, including its separate upper run; following tel outside.', observed_bbox=[909,2167,1003,2228], candidates=[r'\Sigma_i^- with detached upper run: head/retrace or independent-rule role unresolved']), False)
parts.append(group('B024-P05', r'\unsure{Soient|Soit} '+'\n'+s1+', '+s2+r'les deux comp. \unsure{conn|connexes} de $X\setminus E_i$, alors a) se \unsure{prècise|précise|prêcise} en : il y a \unsure{exactemt|exactement} \uline{un} '+'\n'+uplus+r'contenu dans '+'\n'+s3+r'tel que $\overline{U_{s_+}}\cap E_i\ne\varnothing$ (et de $=$ pour '+'\n'+s4+r', \unsure{de|dé|qui} '+'\n'+definit+r'un $U_{s_-}\subset$ '+'\n'+s5+r'tel que $\overline{U_{s_-}}\cap E_i\ne\varnothing$),', owns='Complete final paragraph, both signed cases and closing comma; all child glyphs and words are exclusive locally.', kind='text', candidates=['Soient','Soit','conn','connexes','prècise','précise','prêcise','exactemt','exactement','de','dé','qui']))
parts.append(group('B024-ARCHIVE', '% archive sheet number: 23', owns='Archive numeral 23, recorded in a comment only; hand undetermined.', kind='administrative', observed_bbox=[27,2305,75,2344]))

mark_scopes={
 'B024-G02':[{'scope':'high point, first overset argument','role':'unresolved','hand':'undetermined hand','attachment':'unresolved relative to precursor; position above-left retained'},{'scope':'deleted U/E and its cancellation','role':'deleted precursor','hand':'his hand','attachment':'at live opening parenthesis'}],
 'B024-G05':[{'scope':'main long path including upper hook','role':'left statement rule','hand':'his hand','attachment':'lemma statement'},{'scope':'two pale left components','role':'unresolved','hand':'undetermined hand','attachment':'unresolved; separate from main rule','surface_origin':'unresolved'}],
 'B024-G06':[{'scope':'sommets node','role':'word','hand':'his hand','attachment':'lemma prose'},{'scope':'one high triangular point','role':'letter component or independent point, unresolved','hand':'undetermined hand','attachment':'e/t zone, unresolved'}],
 'B024-G07':[{'scope':'lower L/e run','role':'Le/Ce word body','hand':'his hand','attachment':'whole qualified word'},{'scope':'detached upper hook','role':'upper letter run/retrace or independent hook, unresolved','hand':'undetermined hand','attachment':'whole Le/Ce group; local role remains unresolved'}],
 'B024-M04':[{'scope':'entire pale bent path','role':'unresolved','hand':'undetermined hand','attachment':'separate from fait descender','surface_origin':'unresolved'}],
 'B024-G08':[{'scope':'four main dark phrase runs','role':'whole reduced qu-on phrase, qualified','hand':'his hand','attachment':'whole phrase'},{'scope':'final solid small form','role':'a or independent point','hand':'undetermined hand','attachment':'locally unresolved; whole phrase remains qualified separately'}],
 'B024-G09':[{'scope':'y and a nodes','role':'two live words','hand':'his hand','attachment':'conditions prose'},{'scope':'two pale entry runs','role':'entry/independent traces, unresolved','hand':'undetermined hand','attachment':'toward a, unresolved','surface_origin':'unresolved'}],
 'B024-G10':[{'scope':'U, s and filled low sign','role':'complete U_s plus/minus candidates','hand':'his hand','attachment':'low sign below s; sign identity unresolved'},{'scope':'two pale neighbouring marks','role':'unresolved','hand':'undetermined hand','attachment':'beside s, unresolved','surface_origin':'unresolved'}],
 'B024-G11':[{'scope':'complete definit word node with dotless final i','role':'unaccented verb','hand':'his hand','attachment':'final prose line'},{'scope':'pale upright/dot plus adjacent dark fleck','role':'two-part i dot/entry or one independent fleck','hand':'undetermined hand','attachment':'locally unresolved final i zone'}]
}
for gid in ['B024-S01','B024-S02','B024-S05']:
    mark_scopes[gid]=[{'scope':'body, index and raised sign','role':'complete locally inspected signed Sigma','hand':'his hand','attachment':'one complete glyph group'},{'scope':'separate upper run','role':'head/retrace or independent rule, unresolved','hand':'undetermined hand','attachment':'local upper-run/body relationship remains qualified'}]
for gid in ['B024-S03','B024-S04']:
    mark_scopes[gid]=[{'scope':'body and joined/crowded upper run with index','role':'complete Sigma glyph','hand':'his hand','attachment':'local joined/crowded head/body'},{'scope':'raised sign','role':'plus/minus unresolved' if gid.endswith('03') else 'minus','hand':'his hand','attachment':'raised on this Sigma'}]
for gid,scopes in mark_scopes.items():
    GROUPS[gid]['separate_mark_scopes']=scopes

tex='\n'.join(parts)
(ROOT/'reading.tex').write_text(tex)

# The source map is a literal source audit. It performs no image or geometric comparisons.
stack=[]
spans={}
for m in re.finditer(r'% (BEGIN|END) (B024-[A-Z0-9]+)\n?',tex,re.M):
    action,gid=m.group(1),m.group(2)
    if action=='BEGIN':
        stack.append((gid,m.start(),m.end(),stack[-1][0] if stack else None))
    else:
        old,start,body_start,parent=stack.pop()
        assert old==gid
        spans[gid]=(start,m.end(),body_start,m.start(),parent)
assert not stack

def spanrec(start,end):
    return {'char_start':start,'char_end_exclusive':end,'utf8_byte_start':len(tex[:start].encode()),'utf8_byte_end_exclusive':len(tex[:end].encode()),'line_start':tex.count('\n',0,start)+1,'line_end':tex.count('\n',0,max(start,end-1))+1,'exact_tex':tex[start:end]}

def command_end(start,limit):
    depth=0
    j=start
    while j<limit:
        c=tex[j]
        if c=='%' and (j==0 or tex[j-1]!='\\'):
            k=tex.find('\n',j)
            j=limit if k<0 else k+1
            continue
        if c in '{}':
            nback=0;k=j-1
            while k>=0 and tex[k]=='\\':
                nback+=1;k-=1
            if nback%2==0:
                depth += 1 if c=='{' else -1
        if c==';' and depth==0:
            return j+1
        j+=1
    raise ValueError('Unterminated TikZ command at source offset '+str(start))

def macro_end(start,arity):
    j=start
    for _ in range(arity):
        while j<len(tex) and tex[j]!='{':
            j+=1
        depth=1;j+=1
        while depth:
            if tex[j]=='%' and tex[j-1]!='\\':
                j=tex.index('\n',j)+1
                continue
            if tex[j] in '{}' and tex[j-1]!='\\':
                depth += 1 if tex[j]=='{' else -1
            j+=1
    return j

mapped=[]
for gid,(start,end,bs,be,parent) in sorted(spans.items(),key=lambda q:q[1][0]):
    d={'id':gid,'parent_group':parent,**GROUPS[gid],'source_span':spanrec(start,end),'body_span':spanrec(bs,be),'literal_components':[]}
    for n,m in enumerate(re.finditer(r'\\(?:draw|fill|path|node|coordinate)\b',tex[bs:be]),1):
        cs=bs+m.start();ce=command_end(cs,be)
        d['literal_components'].append({'component_id':gid+'-K'+str(n).zfill(2),**spanrec(cs,ce)})
    d['wrappers']=sorted(set(re.findall(r'\\(?:unsure|deleted|inserted|uline|phantom|rlap|llap|overset|figure|mathrel)\b',tex[bs:be])))
    d['wrapper_spans']=[]
    for m in re.finditer(r'\\(unsure|deleted|inserted|uline|phantom|rlap|llap|overset|figure|mathrel)\b',tex[bs:be]):
        cs=bs+m.start()
        # Comment-only candidate notation is retained in the enclosing source excerpt, not treated as a live wrapper.
        line_start=tex.rfind('\n',0,cs)+1
        if '%' in tex[line_start:cs]:
            continue
        ce=macro_end(cs,2 if m.group(1)=='overset' else 1)
        d['wrapper_spans'].append({'macro':m.group(1),**spanrec(cs,ce)})
    d['child_groups']=[g for g,s in spans.items() if s[4]==gid]
    mapped.append(d)

mapped_byid={m['id']:m for m in mapped}
for g in mapped:
    for component in g['literal_components']:
        cs=component['char_start'];ce=component['char_end_exclusive']
        owner=min((m for m in mapped if m['body_span']['char_start']<=cs and ce<=m['body_span']['char_end_exclusive']),key=lambda m:m['body_span']['char_end_exclusive']-m['body_span']['char_start'])
        canonical=next(c for c in owner['literal_components'] if c['char_start']==cs and c['char_end_exclusive']==ce)
        component['canonical_component_id']=canonical['component_id']
        component['owner_group']=owner['id']
        component['parent_units']=owner.get('parent_units','ordinary TeX text/math layout')
        component['origin']=owner.get('origin','ordinary TeX text/math layout')
        containers=[c for c in owner['literal_components'] if c['char_start']<cs and ce<=c['char_end_exclusive']]
        component['containing_component']=min(containers,key=lambda c:c['char_end_exclusive']-c['char_start'])['component_id'] if containers else None
        cmd=re.match(r'\\([A-Za-z]+)',component['exact_tex']).group(1)
        component['command_kind']=cmd
        component['visibility']='nonprinting bounds/anchor' if cmd in ['path','coordinate'] else 'visible path' if cmd in ['draw','fill'] else 'node with complete literal contents; phantom portions nonprinting'

source_map={'scan':'024','reader':'B','reading_path':'reading.tex','reading_sha256':hashlib.sha256(tex.encode()).hexdigest(),'offset_convention':'Unicode character and UTF-8 byte offsets are zero based; ends exclusive. Line numbers are one based. Each excerpt is literal current source. Parent regions include child spans; local ownership remains exclusive as stated.','coordinates':'Declared manual TikZ coordinates and dimensions only. No coordinate transformation, curve-extrema, alignment, image-difference or metric validation was computed. The image crop bboxes are observations/planned crop bounds, not path-extrema claims.','groups':mapped}
(ROOT/'source_map.json').write_text(json.dumps(source_map,indent=2,ensure_ascii=False)+'\n')

# Report: every original uncertainty-row identity remains separate from local physical counting.
audit=json.loads((ROOT/'view_audit.json').read_text())
crop_events=[e for e in audit['events'] if e['kind']=='deep_crops' and e['status']=='success']
crop_by_num={int(Path(e['image_path']).name[4:6]):e for e in crop_events}
diffs=[]

def D(did, location, C, H, reading, evidence, confidence='medium', kind='other', dc=False, dh=False, status=None, crop=None, bbox=None, rows=None, groups=None, physical=None, hmarked=False, alternatives=None):
    ev=crop_by_num.get(crop)
    item={'id':did,'location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':Path(ev['image_path']).name if ev else None,'bbox':{'origin':'original full scan','coordinates':ev['bbox'] if ev else bbox},'mathematical_consequence':None,'C_source_doubt_rows':rows or [],'source_groups':groups or [],'physical_locus':physical or did,'marked_in_H':hmarked,'alternatives':alternatives or []}
    item['source_spans']=[{'group':g,**spanrec(spans[g][0],spans[g][1])} for g in (groups or [])]
    diffs.append(item)

D('B024-C01','Opening Pi exponent',r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0',r'\Pi_I^{\unsure{\circ|0}}','Small high hollow rounded loop; its circle/zero reading remains unresolved. H zero survives as an alternative, not a conclusively disproved reading.',dc=False,dh=True,status='retained',crop=2,rows=['C024-R01'],groups=['B024-P01'],alternatives=[r'\Pi_I^0'])
D('B024-C02a','Opening union limit',r'\bigcup_{\unsure{\alpha\prime|i}\in I}',r'\bigcup_{i\in I}',r'\bigcup_{\unsure{\alpha\prime|i}\in I}','Low hooked loop and a separate high mark; alpha-prime primary, dotted i retained. This local limit is recorded independently of the following E index. H i remains an alternative.',confidence='low',dh=True,status='retained',crop=2,rows=['C024-R02'],groups=['B024-P01'],alternatives=[r'\bigcup_{i\in I}'])
D('B024-C02b','Opening E subscript',r'E_{\alpha\prime}',r'E_i',r'E_{\alpha\prime} (local alternative E_i)','Independent low hooked form plus high mark after E. First-occurrence printing leaves this recurrence unmarked in TeX while its complete E_i alternative remains here. The original compound source row covers both index loci.',confidence='low',dh=True,status='retained',crop=2,rows=['C024-R02'],groups=['B024-P01'],alternatives=[r'E_i'])
D('B024-C03',"Opening after S l'",r"l'\unsure{ens|ens.}",r"l'ens.","l'ens",'The complete gap after ens and before des contains no detached abbreviation point.',confidence='high',dc=True,dh=True,status='resolved',bbox=[580,215,815,310],rows=['C024-R03'],groups=['B024-P01'])
D('B024-C04','Cancelled cluster before second Considérons',r'\deleted{\unsure{On a}}',r'\struck{On}',r'\deleted{\unsure{On a|On}}','Rounded initial, lower fragments and thick terminal wedge beneath the strike. Terminal wedge can belong to a or the strike end. Complete On a/On alternatives share the same deletion state; H On remains an alternative.',confidence='low',dh=True,status='retained',crop=4,rows=['C024-R04'],groups=['B024-P01'],alternatives=[r'\deleted{On}'])
D('B024-C05','At opening parenthesis of definition',r'\deleted{\unsure{U|E}}','[absent]',r'\deleted{\unsure{U|E}}','Crossed vertical, horizontal and diagonal strokes preserve a precursor, but do not isolate U from E. Live (s,i) follows separately.',confidence='low',kind='omission',dh=True,status='retained',crop=6,rows=['C024-R05'],groups=['B024-G02'],alternatives=[r'\deleted{E}'])
D('B024-C06','Definition-arrow label',r'\unsure{def|déf}','déf','def','The looped d, reduced e and tall f are complete; no separate accent appears above e.',confidence='high',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,status='resolved',crop=6,rows=['C024-R06'],groups=['B024-G03'])
D('B024-C07','Lemma tuple correction',r'(S,I\unsure{)\deleted{R})|\deleted{)}{,}R)}',r'(S,I,R)',r'\unsure{(S,I)\deleted{R})|(S,I\deleted{)},R)}','Clean first closing stroke, crossed R cluster and large final lower return favour the first complete state. The second retains a cancelled earlier close and live comma/R/final close. No chronology is inferred. Literal source preserves the right cluster once.',confidence='low',kind='deletion state (struck given live or live given struck)',dh=True,status='retained',crop=7,rows=['C024-R07'],groups=['B024-G04'],physical='tuple',alternatives=[r'(S,I\deleted{)},R)'])
D('B024-C08','Before sommets',r'\unsure{ens des|ens de}',r'ens.\ de',r'\unsure{ens des|ens de}','Continuous low run ends in a d/e-like loop and reduced tail; final s remains unresolved. No detached abbreviation point separates ens and de(s). H de is retained as an alternative; its point is not seen.',confidence='low',dh=True,status='retained',crop=8,rows=['C024-R08'],groups=['B024-P03'],alternatives=['ens de'])
D('B024-C09a','Arêtes word and accent',r'\unsure{arêtes|arètes|aretes}','arêtes',r'\unsure{arêtes|arètes|aretes}','Tall trace beside the t cannot securely allocate circumflex, grave or absent accent to the reduced preceding letter. All three complete noun spellings survive. The original row also names punctuation; C09b records that separate local part.',confidence='low',status='retained',crop=9,rows=['C024-R09'],groups=['B024-P03'],physical='aretes',alternatives=['arètes','aretes'])
D('B024-C09b','Endpoint after arêtes',r'.)',r'.',r'.).','Heavy point, high closing curve and separate short point to its right all survive. The last point is additional to C; H lacks the closing curve and final point. These are manuscript marks, not editorial alternative separators.',confidence='medium',kind='omission',dc=True,dh=True,status='resolved',crop=9,rows=['C024-R09'],groups=['B024-P03'],physical='aretes-punctuation')
D('B024-C10','Deleted word after Il',r'\deleted{\unsure{existe|ex}}',r'\struck{il y a}',r'\deleted{\unsure{existe|ex}}','Low upright beginnings and a thick long cross-run obscure the full ending. Il at the left and y a at the right are live and separate. The cancellation is clear; existe/ex remain complete local candidates.',confidence='low',kind='misread word',dh=True,status='retained',crop=13,rows=['C024-R10'],groups=['B024-P04'],alternatives=[r'\deleted{ex}'])
D('B024-C11','Final paragraph initial',r'\unsure{Soient|Soit}','Soient',r'\unsure{Soient|Soit}','Looped initial S, dotted i zone and almost flat final run ending in a raised hook. The middle/end contractions do not settle Soient versus Soit.',status='retained',crop=14,rows=['C024-R11'],groups=['B024-P05'],alternatives=['Soit'])
D('B024-C12','Lower adverb before underlined un',r'\unsure{exactement|exactemt}','exactement',r'\unsure{exactemt|exactement}','Compact intermediate run and high crossed triangular ending favour the contraction exactemt; the complete exactement candidate remains. The triangular crossing is not assigned a deletion state.',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,status='retained',crop=17,rows=['C024-R12'],groups=['B024-P05'],alternatives=['exactement'])
D('B024-C13','First U low sign',r'U_{s_{\unsure{+|-}}}',r'U_{s_+}',r'U_{s_+}|U_{s_-}, literal filled sign','Filled notched block below s with a small upper nub. Plus is primary and minus retained; no predecessor or writing chronology is supplied. The following barred U has a separately seen definite plus on half b.',confidence='low',status='retained',crop=18,rows=['C024-R13'],groups=['B024-G10'],alternatives=[r'U_{s_-}'])
D('B024-C14','Raised sign on chosen-side Sigma',r'\Sigma_i^{\unsure{+|-}}',r'\Sigma_i^+',r'\Sigma_i^+|\Sigma_i^-, literal filled sign','Raised horizontal dark block with a short upper nub; plus/minus remains unresolved. Complete body, locally joined head and low index stay with this sign. H primary plus is unchanged, so added editorial qualification alone has no H count.',confidence='low',status='retained',crop=19,rows=['C024-R14'],groups=['B024-S03'],alternatives=[r'\Sigma_i^-'])
D('B024-C15','Reduced word just before definit',r'\unsure{dé|qui}',r'\ill{}',r'\unsure{de|dé|qui}','Tall looped first form and low final loop favour de, but do not settle the complete reduced word or its accent. C dé and qui remain candidates. The one H ill placeholder covers this word only.',confidence='low',kind='readable ink left as \\ill{}',dc=True,dh=True,status='retained',crop=20,rows=['C024-R15'],groups=['B024-P05'],hmarked=True,alternatives=['dé','qui'])
D('B024-C16','Before graphe est un arbre',r'\unsure{Le|Ce}','Ce','Le|Ce, whole literal word','Square upright/lower e run with detached upper hook. Both complete Le/Ce readings remain under one qualifier; the upper hooked run is present once within that group. H Ce remains an alternative.',dh=True,status='retained',crop=10,rows=['C024-R16'],groups=['B024-G07'],alternatives=['Ce'])
D('B024-C17','Before fait',r'\unsure{le|Le}','Le',r'\unsure{le|Le}','Short upright and low turn favour lowercase le; capitalization remains unresolved locally. H Le remains an alternative.',dh=True,status='retained',crop=12,rows=['C024-R17'],groups=['B024-P04'],alternatives=['Le'])
D('B024-C18','After comp.',r'\unsure{connexes}',r'conn.',r'\unsure{conn|connexes}','Three flattened groups favour conn; the more expanded connexes remains supported by the reduced interior strokes. There is a point after comp., but no point after this word.',confidence='low',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,status='retained',crop=15,rows=['C024-R18'],groups=['B024-P05'],alternatives=['connexes'])

D('B024-D01','First Considérons accent','Considérons','Considérons',r'\unsure{Considérons|Considerons}','Tall post-d stroke stays attached to the low letter run; accent versus attached letter run remains open. The second Considérons has its own clear raised accent and stays unqualified.',dc=True,crop=1,groups=['B024-P01'],alternatives=['Considerons'])
D('B024-D02a','Old upper start',r'\deleted{\uline{Lemme}}',r'\struck{relation R entre}',r'\deleted{\uline{Lemme}}','Old tall L and low emme run lie beneath the new Relation phrase, with a distinct underline below. This is the old word recovered from its own ink.',confidence='high',kind='misread word',dh=True,crop=5,groups=['B024-G01'],physical='upper-revision')
D('B024-D02b','Raised replacement capitalization','Relation',r'\add{relation R entre}','Relation','The initial has a tall loop and leg, giving capital R in Relation.',confidence='high',kind='misread word',dh=True,crop=5,groups=['B024-G01'],physical='upper-revision')
D('B024-D02c','Whole raised replacement scope',r'\inserted{Relation R entre S et I}',r'\add{relation R entre} S et I',r'\inserted{Relation R entre S et I}','S et I lies on the same raised sloping replacement row as Relation R entre, above the old forall i in I. The full replacement is retained in one insertion scope.',kind='insertion or placement',dh=True,crop=5,groups=['B024-G01'],physical='upper-revision')
D('B024-D02d','Upper cancellation geometry','generic deleted span','two struck spans','one long rising crossing path over the two old components','The stroke runs from the left L area across the old quantified clause and ends at the right. Invisible deletion annotations retain the old state without adding a generic second strike.',kind='drawing or diagram',dc=True,dh=True,crop=5,groups=['B024-G01'],physical='upper-revision')
D('B024-D03','High point above overwritten display glyph','[absent]','[absent]',r'\overset{\unsure{\cdot}}{\deleted{\unsure{U|E}}}','Small discrete point above and left of the crossed precursor. Presence is clear; character, role, hand and attachment are unestablished.',kind='omission',dc=True,dh=True,crop=6,groups=['B024-G02'],physical='definition-high-point')
D('B024-D04','Definition arrow geometry',r'\Longleftrightarrow',r'\Longleftrightarrow','literal rounded left return, two shafts and right pointed end','Left end turns through a rounded lower return; upper and lower shaft runs are retained separately with the right end. Def label belongs to this complete group once. No mathematical equivalence is inferred from the drawing.',kind='drawing or diagram',dc=True,dh=True,crop=6,groups=['B024-G03'],physical='definition-arrow')
D('B024-D05','High point at sommets ending','[absent]','[absent]','sommets plus one qualified high triangular point','Separate high triangular point above the e/t zone of the complete word. Its attachment to a letter or an independent mark, its role and its hand remain unresolved.',kind='omission',dc=True,dh=True,crop=8,groups=['B024-G06'],physical='sommets-high-point')
D('B024-D06',"Prefix before arêtes",r"d'",r"d'",r"\unsure{de|d'}",'Raised final loop is joined continuously to the d return; de is primary, while d-prime remains an alternative. Complete noun spellings remain qualified independently.',confidence='low',kind='misread word',dc=True,dh=True,crop=9,groups=['B024-P03'],physical='aretes-prefix',alternatives=["d'"])
D('B024-D07','Left lemma rule',r'one tabular vertical rule','[absent]','literal long rule with hooked upper return','Narrow hook at the top joins the long downward rule. Its complete lower endpoint was read on half a; crop11 only targets the upper hook and adjacent trace. No second straight table rule remains.',kind='drawing or diagram',dc=True,dh=True,crop=11,groups=['B024-G05'],physical='lemma-rule')
D('B024-D08','Pale trace left of lemma rule','[absent]','[absent]','one short oblique run and lower short fleck','Two separate dark/pale components stand left of the rule. Their shape is supported; hand, role, attachment and surface origin remain unresolved.',kind='omission',dc=True,dh=True,crop=11,groups=['B024-G05'],physical='rule-left-trace')
D('B024-D09','After arbre','no point','arbre.','arbre with underline, no final point','Half a shows the underline ending beneath arbre and clear adjoining paper to the right, without H final punctuation.',confidence='high',kind='text not on the page',dh=True,bbox=[625,1100,1055,1200],groups=['B024-P03'],physical='arbre-endpoint')
D('B024-D10','Phrase after fait',"qu'on a","c'est",r"whole qualified qu'on a; final a/independent-point role qualified locally",'Complete q loop and long descender precede reduced horizontal runs; final a-shaped form is a solid point. The whole phrase remains qualified independently of the final point role and hand. Complete alternative: qu-on followed by an independent point.',confidence='low',kind='misread word',dc=True,dh=True,crop=12,groups=['B024-G08'],physical='quon-a',alternatives=["qu'on followed by an independent point"])
D('B024-D11','Below-left of fait','[absent]','[absent]','qualified faint bent trace','One pale bent trace is separate from the dark f descender. No letter is supplied; its role, hand, attachment and surface origin remain unresolved.',confidence='low',kind='omission',dc=True,dh=True,crop=12,groups=['B024-M04'],physical='fait-pale-trace')
D('B024-D12','Before cancelled existe/ex','Il','il','Il','Capital I has a high horizontal cap and lower fork; the following l is a separate tall loop.',confidence='high',kind='misread word',dh=True,crop=13,groups=['B024-P04'],physical='Il')
D('B024-D13','Live y a entry','ordinary y a','ordinary y a','y a with two pale intervening entry runs','Interrupted pale run extends toward the a; it is kept once between the two complete word nodes. Role/attachment and hand remain local, without supplying an extra letter.',kind='omission',dc=True,dh=True,crop=13,groups=['B024-G09'],physical='ya-pale-entry')
D('B024-D14',"Condition b after par",r"l'ens de",r"l'une de",r"l'ens de",'Low connected e/n/s run follows the apostrophe. The complete following de and ces deux U_s remain as written; no final abbreviation point after ens.',confidence='high',kind='misread word',dh=True,bbox=[1250,1555,1550,1655],groups=['B024-P04'],physical='condition-b-ens')
D('B024-D15','First lower Sigma head',r'\Sigma_i^+',r'\Sigma_i^+','complete S01 with bent detached head and interrupted upper-arm start','Bent short upper run is separated from the main arm. A small detached start and pale continuation precede the dark arm. All are retained with the complete i and plus; head/retrace/independent-rule role remains qualified at this first occurrence.',kind='omission',dc=True,dh=True,crop=14,groups=['B024-S01'],physical='sigma-S01')
D('B024-D16','Second lower Sigma head',r'\Sigma_i^-',r'\Sigma_i^-','complete S02 with separate short upper run','A short upper horizontal lies separately above the curved body arm. Local head/retrace/independent-rule alternatives survive in the record, while the first-occurrence printing convention leaves this primary unmarked.',kind='omission',dc=True,dh=True,crop=14,groups=['B024-S02'],physical='sigma-S02')
D('B024-D17','Précise accent','précise','précise',r'\unsure{prècise|précise|prêcise}','Raised short arc descends at its right end; grave primary, acute and circumflex alternatives retained. All candidates are complete words. The small higher i-zone point is not duplicated as a new independent mark.',confidence='low',kind='misread word',dc=True,dh=True,crop=16,groups=['B024-P05'],physical='precise',alternatives=['précise','prêcise'])
D('B024-D18','After précise','en :','ainsi :','en :','One low e turn and long n run precede two separate colon points.',confidence='high',kind='misread word',dh=True,crop=16,groups=['B024-P05'],physical='en')
D('B024-D19','Before first signed U',r'\uline{un}',r'\struck{une} une',r'\uline{un}','One live short word has a single separate underline. No preceding struck word or final e is visible in the complete target.',confidence='high',kind='deletion state (struck given live or live given struck)',dh=True,crop=17,groups=['B024-P05'],physical='underlined-un')
D('B024-D20','Two small marks right of first signed U','[absent]','[absent]','one pale slant/spot and one small point','Two discrete pale neighbours lie beside the low s above the filled sign. Both have their own local role, hand, attachment and surface-origin uncertainty. Diffuse lower shading yields no supplied character.',confidence='low',kind='omission',dc=True,dh=True,crop=18,groups=['B024-G10'],physical='signed-u-neighbours')
D('B024-D21','After first signed U','contenu','contenue','contenu','Final low u run ends before the gap preceding dans; no separate terminal e.',confidence='high',kind='misread word',dh=True,bbox=[1025,1945,1415,2050],groups=['B024-P05'],physical='contenu')
D('B024-D22','Before first barred-U equation','tel que','telle que','tel que','Tall t and l bound the short word; following que has its own long descender. No extra le group.',confidence='high',kind='misread word',dh=True,bbox=[330,2070,565,2210],groups=['B024-P05'],physical='first-tel')
D('B024-D23','Parenthetical after et de',r'de $=$','de même',r'de $=$','Two horizontal strokes stand where H expands a word. The sign is preserved without a verbal substitution.',confidence='high',kind='abbreviation expanded or spelling modernised',dh=True,bbox=[1020,2060,1420,2150],groups=['B024-P05'],physical='de-equals')
D('B024-D24','Final-line verb','définit','définit','definit','Complete d/e/f region has no acute over e. Full f descender and both i zones are preserved. No grammatical repair is made to the preceding reduced word.',confidence='high',kind='misread word',dc=True,dh=True,crop=21,groups=['B024-G11'],physical='definit')
D('B024-D25','Final i upper pair in definit','ordinary i dot','ordinary i dot','dotless i plus pale upright/dot and adjacent dark fleck','The final i zone contains two upper components. Both are kept once with unresolved allocation to the i dot/entry or an independent fleck, and unresolved local hand; no extra dot from an ordinary i node is present.',confidence='medium',kind='omission',dc=True,dh=True,crop=21,groups=['B024-G11'],physical='definit')
D('B024-D26','After definit','un','une','un','One low u/n run before U_s-minus; no final e group.',confidence='high',kind='misread word',dh=True,bbox=[595,2175,720,2260],groups=['B024-P05'],physical='last-un')
D('B024-D27','Final Sigma head',r'\Sigma_i^-',r'\Sigma_i^-','complete S05 with separate upper run','On half b the upper run stands above the body arm with a visible white interval. The i and minus are preserved; head/retrace/independent-rule role remains local and unmarked under the first-occurrence convention.',kind='omission',dc=True,dh=True,bbox=[909,2167,1003,2228],groups=['B024-S05'],physical='sigma-S05')
D('B024-D28','Before final barred-U equation','tel que','telle que','tel que','Short t/l word and separate que precede the final equation; no extra le group appears.',confidence='high',kind='misread word',dh=True,bbox=[1020,2145,1220,2265],groups=['B024-P05'],physical='last-tel')

# Literal witness quotations: grouping and internal math delimiters are retained as supplied.
byid={d['id']:d for d in diffs}
literal_updates={
 'B024-C01':{'H':r'\Pi_{I}^{0}'},
 'B024-C02a':{'C':r"\bigcup_{\unsure{\alpha'|i}\in I}",'H':r'\bigcup_{i\in'+'\n'+r'I}','reading':r"\bigcup_{\unsure{\alpha'|i}\in I}"},
 'B024-C02b':{'C':r"E_{\alpha'}",'H':r'E_{i}','reading':r"E_{\alpha'} (local alternative E_i)"},
 'B024-C13':{'H':r'U_{s_{+}}'},
 'B024-C14':{'H':r'\Sigma_{i}^{+}'},
 'B024-C15':{'kind':r'readable ink left as \ill{}'},
 'B024-D02a':{'C':r'\deleted{\uline{Lemme} $\forall i\in I$,}','H':r'\struck{relation $R$ entre}'},
 'B024-D02b':{'H':r'\add{relation $R$ entre}'},
 'B024-D02c':{'C':r'\inserted{Relation $R$ entre $S$ et $I$}','H':r'\add{relation $R$ entre} $S$ et $I$'},
 'B024-D02d':{'C':r'\deleted{\uline{Lemme} $\forall i\in I$,}','H':r'\struck{relation $R$ entre} \struck{$\forall'+'\n'+r'i\in I$,}'},
 'B024-D07':{'C':r'\noindent\begin{tabular}{@{}|p{.94\linewidth}@{}}'},
 'B024-D09':{'C':r'\uline{arbre}','H':r'\emph{arbre}.'},
 'B024-D12':{'C':r'Il \deleted{\unsure{existe|ex}} y a','H':r'\struck{il y a} il y a','reading':r'Il \deleted{\unsure{existe|ex}} y a','kind':'insertion or placement','evidence':'The capital I has a high cap and lower fork, followed by a separate tall l. The live Il precedes the cancelled existe/ex; H places its live il after its different cancelled phrase. Capitalization and placement are both retained in this complete local cluster.','physical_locus':'Il-existe-ya'},
 'B024-D13':{'C':'y a','H':'y a'},
 'B024-D15':{'H':r'\Sigma_{i}^{+}'},
 'B024-D16':{'H':r'\Sigma_{i}^{-}'},
 'B024-D25':{'C':'définit','H':'définit'},
 'B024-D27':{'H':r'\Sigma_{i}^{-}'},
 'B024-D28':{'H':'telle\nque'}
}
for did,updates in literal_updates.items():
    byid[did].update(updates)
byid['B024-C10']['physical_locus']='Il-existe-ya'
byid['B024-D06']['complete_phrase_candidates']=['de arêtes','de arètes','de aretes',"d'arêtes","d'arètes","d'aretes"]
byid['B024-C09a']['complete_phrase_candidates']=byid['B024-D06']['complete_phrase_candidates']

source_doubts=(BASE/'packets/024/C_doubts.txt').read_text().splitlines()
original_rows=[]
in_doubts=False
for line_no,line in enumerate(source_doubts,1):
    if line.startswith('## Doubtful readings'):
        in_doubts=True
    elif in_doubts and line.startswith('| 24 |'):
        rid='C024-R'+str(len(original_rows)+1).zfill(2)
        related=[d for d in diffs if rid in d['C_source_doubt_rows']]
        original_rows.append({'id':rid,'source_path':'packets/024/C_doubts.txt','source_line':line_no,'exact_source_row':line,'local_decisions':[d['id'] for d in related],'local_statuses':{d['id']:d['C_doubt_status'] for d in related},'count_original_row_once':True})
assert len(original_rows)==18

inv0=json.loads((BASE/'packets/024/C_inventory.json').read_text())
inventory=[]
inv_updates={
'024.01':('opening, through second Considérons la','Considérons|Considerons la partition … notées U_s; second Considérons la', ['B024-P01']),
'024.02':('after (s in S)','deleted On a|On', ['B024-P01']),
'024.03':('upper former lemma row','deleted underlined Lemme and forall i in I comma', ['B024-G01']),
'024.04':('whole raised replacement row','inserted Relation R entre S et I', ['B024-G01']),
'024.05':('definition display','(s,i) in R; def over rounded-return double shaft; barred U_s cap E_i nonempty, point', ['B024-DISPLAY']),
'024.06':('definition beginning','deleted U|E', ['B024-G02']),
'024.07':('lemma and vertically marked statement','Lemme Cette relation fait de … ens des|ens de sommets, I comme ens. de|d-prime arêtes|arètes|aretes .). … Le|Ce graphe est un arbre', ['B024-P02','B024-P03']),
'024.08':('lemma tuple right cluster','complete (S,I) deleted R final close | (S,I deleted first close comma live R final close', ['B024-G04']),
'024.09':('lemma before Le/Ce','deleted Cette relation', ['B024-P03']),
'024.10':('conditions a and b','le|Le fait [qualified qu-on-a] … Il … l-ens de ces deux U_s.', ['B024-P04']),
'024.11':('after Il','deleted existe|ex', ['B024-P04']),
'024.12':('final paragraph, both signed cases','Soient|Soit … comp. conn|connexes … prècise|précise|prêcise en … exactemt|exactement … de|dé|qui definit un … tel que … ),', ['B024-P05'])}
for item in inv0:
    pos,words,gs=inv_updates[item['element']]
    inventory.append({'sheet_kind':'text','hand':'his hand','element':item['element'],'kind':item['kind'],'position':pos,'first_words_or_objects':words,'transcribed':'yes','source_groups':gs,'provenance_C_inventory':item})

extra_inventory=[
('B024.I13','drawing','upper correction','single rising cancellation path','his hand',['B024-G01']),
('B024.I14','drawing','above deleted definition precursor','one high point','undetermined hand',['B024-G02']),
('B024.I15','drawing','definition arrow','rounded return and double shafts with def label','his hand',['B024-G03']),
('B024.I16','drawing','tuple right cluster','crossed R and long lower return with complete state qualifier','his hand',['B024-G04']),
('B024.I17','drawing','left of lemma statement','continuous long rule with narrow upper hook','his hand',['B024-G05']),
('B024.I18','drawing','left of rule upper section','oblique run and lower short fleck','undetermined hand',['B024-G05']),
('B024.I19','drawing','sommets e/t zone','small high triangular point; word is his hand, point attribution unresolved','undetermined hand',['B024-G06']),
('B024.I20','text','before graphe','complete Le|Ce with detached upper hook','his hand',['B024-G07']),
('B024.I21','drawing','left below fait','faint bent trace','undetermined hand',['B024-M04']),
('B024.I22','text','after fait','whole qualified qu-on-a phrase','his hand',['B024-G08']),
('B024.I23','drawing','end of qu-on-a phrase','solid point-shaped a; its separate role and hand remain unresolved','undetermined hand',['B024-G08']),
('B024.I24','drawing','between live y and a','two pale entry runs; adjoining words his hand','undetermined hand',['B024-G09']),
('B024.I25','drawing','first signed Sigma','complete S01, detached bent head, interrupted arm, i and plus','his hand',['B024-S01']),
('B024.I26','drawing','second signed Sigma','complete S02, detached upper run, body hook, low i and minus','his hand',['B024-S02']),
('B024.I27','text','lower un','single underline beneath live un','his hand',['B024-P05']),
('B024.I28','drawing','first chosen U','complete U_s and filled plus|minus sign','his hand',['B024-G10']),
('B024.I29','drawing','right of low s in first chosen U','two pale neighbouring marks; hand separate from main U','undetermined hand',['B024-G10']),
('B024.I30','drawing','chosen-side Sigma','complete S03 with locally joined head and filled raised plus|minus sign','his hand',['B024-S03']),
('B024.I31','drawing','parenthetical Sigma','complete S04, crowded head/body join, i, minus, lower hook','his hand',['B024-S04']),
('B024.I32','text','last verb','definit, unaccented e, final dotless i with two supplied upper components','his hand',['B024-G11']),
('B024.I33','drawing','last verb final i upper zone','two upper components, allocation and hand unresolved locally','undetermined hand',['B024-G11']),
('B024.I34','drawing','after subset','complete S05, separate upper run, i and minus','his hand',['B024-S05']),
('B024.I35','text','lower left archive corner','archive numeral 23, comment only','undetermined hand',['B024-ARCHIVE'])]
extra_inventory.extend([
('B024.I36','drawing','first Sigma upper run','bent detached upper run; local role and hand separately unresolved','undetermined hand',['B024-S01']),
('B024.I37','drawing','second Sigma upper run','separate short upper run; local role and hand separately unresolved','undetermined hand',['B024-S02']),
('B024.I38','drawing','final Sigma upper run','separate upper run; local role and hand separately unresolved','undetermined hand',['B024-S05']),
('B024.I39','drawing','Le/Ce upper hook','detached upper hook; complete word remains Le|Ce, local role/hand separately unresolved','undetermined hand',['B024-G07'])])
for el,kind,pos,words,hand,gs in extra_inventory:
    inventory.append({'sheet_kind':'text','hand':hand,'element':el,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes','source_groups':gs})

inventory_order=['024.01','024.02','024.04','024.03','B024.I13','024.05','B024.I14','024.06','B024.I15','024.07','024.08','B024.I16','B024.I17','B024.I18','B024.I19','024.09','B024.I20','B024.I39','024.10','B024.I22','B024.I23','B024.I21','024.11','B024.I24','024.12','B024.I25','B024.I36','B024.I26','B024.I37','B024.I27','B024.I28','B024.I29','B024.I30','B024.I31','B024.I32','B024.I33','B024.I34','B024.I38','B024.I35']
inventory.sort(key=lambda d:inventory_order.index(d['element']))

doubt_items=[]
for d in diffs:
    if d['C_doubt_status']=='retained' or d['alternatives'] or any(w in d['evidence'].lower() for w in ['unresolved','unestablished','remains open']):
        doubt_items.append({'id':d['id'],'location':d['location'],'reading':d['reading'],'alternatives':d['alternatives'],'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop'],'C_source_doubt_rows':d['C_source_doubt_rows'],'source_groups':d['source_groups']})

notation=[
{'location':'opening Pi','sign':'raised small hollow loop','latex':r'\Pi_I^{\unsure{\circ|0}}','status':'retained circle/zero; no expected formula used'},
{'location':'opening union and E index, separately inspected','sign':'low hooked loop plus high short mark','latex':r"\bigcup_{\unsure{\alpha'|i}\in I}E_{\alpha'}",'local_alternatives':[r"\bigcup_{\alpha'\in I}",r'\bigcup_{i\in I}',r"E_{\alpha'}",r'E_i'],'status':'first-occurrence printed qualifier; second local alternative retained in report'},
{'location':'opening, lemma before sommets, lemma before arêtes, condition b','sign':'ens punctuation varies','latex':['ens','ens des|ens de','ens.',"l'ens"],'status':'each local occurrence independently read; no harmonization'},
{'location':'definition label','sign':'def without accent','latex':r'\text{def}','status':'C024-R06 resolved'},
{'location':'all four nonempty conditions','sign':'bar over U, cap, E with i, crossed empty-set sign','latex':r'\overline{U_s}\cap E_i\ne\varnothing','status':'display, condition a, chosen plus U, final minus U read independently; signed subscripts retained at their own occurrences'},
{'location':'first and last barred signed U','sign':'plus below first repeated s; minus below final s','latex':[r'\overline{U_{s_+}}',r'\overline{U_{s_-}}'],'status':'first plus seen on half b; final bar separately verified above U and below pour p descender in crop22'},
{'location':'five Sigma occurrences','sign':'local upper runs, bodies, indices and raised signs','latex_groups':['B024-S01','B024-S02','B024-S03','B024-S04','B024-S05'],'status':'S01/S02/S05 upper run role retained locally; first printed qualifier on S01. S03 head visibly joined/crowded, S04 locally crowded/joined. S03 filled raised sign keeps plus/minus independently.'},
{'location':'first chosen U','sign':'solid low notched sign','latex_group':'B024-G10','local_alternatives':[r'U_{s_+}',r'U_{s_-}'],'status':'complete decorated alternatives retained, no inferred overwritten predecessor'},
{'location':'parenthetical et de','sign':'two horizontal strokes','latex':r'de $=$','status':'written sign kept without expansion'},
{'location':'lower components and adverb','sign':'comp. point, following unpointed reduced word, triangular adverb ending','latex':[r'comp. \unsure{conn|connexes}',r'\unsure{exactemt|exactement}'],'status':'abbreviation candidates retained explicitly'},
{'location':'final verb','sign':'unaccented e and final i two-component upper zone','latex_group':'B024-G11','status':'definit; dotless final i prevents duplication of the two explicit upper components'}]

source_choices=[{'id':m['id'],'owns':m['owns'],'candidates':m.get('candidates',[]),'qualification':m.get('qualification'),'separate_mark_scopes':m.get('separate_mark_scopes',[]),'source_span':m['source_span'],'literal_component_ids':[k['component_id'] for k in m['literal_components']],'reading_flags':{'diff_C':any(d['diff_C'] and m['id'] in d['source_groups'] for d in diffs),'diff_H':any(d['diff_H'] and m['id'] in d['source_groups'] for d in diffs)},'note':'Exact current source selection. Pure representation choices are not promoted into an independent witness correction.'} for m in mapped]

report={
'scan':'024','reader':'B','start_utc':'2026-11-21 03:40:17 UTC','end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
'differences':diffs,'doubts':doubt_items,'inventory':inventory,'notation':notation,
'original_C_doubt_rows':original_rows,'source_choices':source_choices,
'notes':{
 'page_content':"The manuscript introduces the partition and its classes U_s, writes an incidence definition using the closure of U_s and E_i, then labels the next assertion Lemme. It writes that the resulting graph is strict and an arbre. It states exactly two U_s in a), and characterizes i by l'ens de ces deux U_s in b). The final paragraph writes one U on each signed side, with the local first signs remaining qualified in this reading. These are attributed manuscript assertions, not proof-check conclusions.",
 'authors_own_uncertainty':{'observed':'none','exact_words':[],'note':'The uncertainty markers in this return are editorial. No written à vérifier, question mark or similar author qualification was observed on this sheet.'},
 'title_date_page_counts':'No title, date or manuscript page count observed. Archive numeral 23 appears in the lower-left corner and is a comment only. H page 23 is the supplied witness page label for scan 24.',
 'mathematics_led_reading_decisions':'No mathematical repair, proof check, computation or mathematical correspondence was used. Distinct signed local glyphs, bars and the equals-like prose sign were read from their own strokes. The final U bar was checked against the p descender immediately above it and retained separately.',
 'legibility':'The erased/crossed starts, tuple state, two filled signs, compressed prose endings and several small detached marks remain the least secure loci.'},
'check_events':[],
'crops':[{'path':Path(e['image_path']).name,'bbox':e['bbox'],'coordinate_origin':'original full scan','rotation':e['rotation'],'purpose':e['purpose'],'successful_views':1,'processing':{'helper':'out/scripts/crop.py','output_width':1000 if int(Path(e['image_path']).name[4:6])==11 else 1800 if int(Path(e['image_path']).name[4:6]) in [18,19] else 2600,'autocontrast':True,'resize':'PIL LANCZOS','unsharp_mask':{'radius':1.1,'percent':120,'threshold':3}}} for e in crop_events],
'brief_feedback':[
 'The source row before arêtes names both accent and punctuation; it needs separate local statuses within its original identity. This return retains the three word spellings and resolves the visible point/close/point sequence separately.',
 'Several ordinary-looking words contain a detached component that can belong to a letter. Complete word or phrase ownership is necessary: sommets, Le/Ce, qu-on-a and definit each retain their own group boundary, while the faint trace beside fait remains mark-only.',
 'The first chosen U and Sigma contain filled sign shapes. This return preserves complete decorated plus/minus alternatives without inventing earlier states from the density of ink.',
 'Some pale marks have clear local shapes but unsettled origin or hand. Their graphical confidence and role/hand questions are kept separate.'
],
'provenance':{
 'brief_path':'out/briefs/brief_v22_scan024.md','brief_sha256':'5f3f3b2bb77e2a76700ae767a85d3c9152a1f8dc2448b1adf9648d300963e474',
 'read_in_full':['packets/024/C.tex','packets/024/H.tex','packets/024/metadata.json','packets/024/C_doubts.txt','packets/024/C_notes.txt','packets/024/notation.md','packets/024/C_inventory.json','source/SP40_CW_81_witnesses/codex/J81-03/PREAMBLE.tex','source/SP40_CW_81_witnesses/codex/J81-03/PROMPT.md','out/briefs/brief_v22_scan024.md'],
 'brief_delivery_note':'The initial long textual brief result was truncated in the middle; lines 100-176 were then read explicitly, covering the missing passage. No image delivery failed.',
 'image_dimensions':{'whole':[1682,2360],'a':[1682,1260],'b':[1682,1260]},'half_origins':{'a':[0,0],'b':[0,1100]},
 'viewing_counts':audit['viewing_counts'],'reopens':0,'failed_unseen_image_deliveries':0,
 'checkpoint_pause':audit.get('checkpoint_pause'),'resume_utc':audit.get('resume_utc'),'visual_read_completed_utc':audit['visual_read_completed_utc'],
 'process':'Actual UTC was recorded before packet reading. Whole image once for layout, a once, b once, then 22 distinct planned local crops, each displayed once. During the checkpoint pause the displayed b image was retained; no image was reopened. No other reader or root-decision files, other page images, OCR, internet, external research, installation, TeX compilation/rendering, geometric or image-difference computation were used. PIL crop/enlargement/autocontrast/sharpening and image dimension reads were processing operations only.',
 'known_crop_boundaries':'Crop11 deliberately shows the rule top and adjacent trace while its long continuation leaves the crop; the rule endpoint was already inspected on half a. Some crops include clipped adjoining context, but each deciding target retains its own full ascenders, descenders and endpoint space. Crop21 retains the full f descender; the preceding-line que descender is context only.',
 'physical_count_convention':'Each original C doubtful row is counted once in original_C_doubt_rows. Differences may contain multiple independent local parts with that source identity. Local reading and punctuation components have separate physical_locus keys; shared upper-revision parts and the definit accent/upper-pair records retain one physical cluster when unique locus counts are used. H local marked_in_H is true only for the actual ill placeholder before definit.',
 'ordinary_confirmations':['la partition; de X; soit S; des classes and notées with its own acute; U_s (s in S) and point; second accented Considérons la; old forall i in I comma; display E_i, cap, crossed empty set and final point; Lemme underline and Cette relation fait de; un graphe strict ayant S comme; I comme ens. with point; deleted Cette relation; graphe est un underlined arbre with no point; signifie que a), forall i in I comma; first exactement deux U_s tels que and nonempty condition comma; et b), i est caractérisé par, ces deux U_s point; les deux, comp. with point, de X setminus E_i comma, alors a) se, il y a; contenu dans; tel que and first signed barred-U condition; opening parenthesis, et de equals pour; final un and subset, tel que, final barred-U nonempty formula, close and comma; archive 23'],
 'administrative_source_choices':'scanpage 24 only; no cotefile inserted on this sheet, no mspage 23, archive 23 only in a comment. C_inventory omitted a separate archive item, which is supplied here. H page 23 is witness apparatus, not extra manuscript text.'
}}
(ROOT/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')

md=['# Independent reading B — scan 024','',report['notes']['page_content'],'',
    'The complete page has been visually read. Unresolved places remain explicitly qualified; no mathematical proof check was performed.','',
    '## Line-by-line audit','',
    '| Physical line/region | Reading audit |','| --- | --- |',
    '| Opening line | Considérons/Considerons remains locally qualified; la partition, de X and the final comma are read. Pi ring/zero and both low index/high-mark groups retain their own complete candidates. |',
    "| Opening second line | soit S l’ens des classes, notées: no point after ens; the acute in notées is clear. |",
    '| Opening third line | U_s (s in S).; deleted On a/On; second Considérons la has a separate visible accent. |',
    '| Upper revision | Deleted underlined Lemme and forall i in I comma; full raised insertion Relation R entre S et I; one long rising cancellation. |',
    '| Definition | Deleted U/E with one separate high point; live (s,i) in R; def without accent; rounded-return double shaft; barred U_s cap E_i nonempty and final point. |',
    '| Lemma heading | Underlined Lemme; Cette relation fait de; complete two-state tuple correction with first close, crossed R and long lower return. |',
    '| Lemma body 1 | un graphe strict ayant S comme. |',
    '| Lemma body 2 | ens des/ens de sommets, I comme ens.; the high triangular point in the sommets ending is separately qualified. |',
    "| Lemma body 3 | de/d’ arêtes/arètes/aretes .).; deleted Cette relation; whole Le/Ce word with detached upper hook; graphe. |",
    '| Lemma body 4 | est un underlined arbre; no final point. Long left rule has an upper hook and a separate two-piece pale trace. |',
    '| Conditions line 1 | le/Le fait; whole reduced qu’on a phrase qualified, final point-shaped a independently qualified; un graphe strict. Pale bent trace below-left of fait retained separately. |',
    '| Conditions line 2 | signifie que a), forall i in I comma; capital Il; deleted existe/ex; live y a with two pale entry runs. |',
    '| Conditions line 3 | exactly written exactement deux U_s tels que, then barred U_s cap E_i nonempty comma. |',
    '| Conditions lines 4–5 | et b), i est caractérisé par l’ens de ces deux U_s. No l’une substitution or ens point. |',
    '| Final paragraph line 1 | Soient/Soit; complete first and second signed Sigma glyphs; les deux comp. conn/connexes de. Their upper runs remain locally recorded. |',
    '| Final paragraph line 2 | X setminus E_i comma, alors a) se prècise/précise/prêcise en colon, il y. |',
    '| Final paragraph line 3 | a exactemt/exactement, one live underlined un; full first U_s plus/minus block and two pale neighbours; contenu dans; complete Sigma_i plus/minus block. |',
    '| Final paragraph line 4 | tel que; first barred signed U has a visible plus; cap E_i nonempty; (et de equals pour; complete Sigma_i-minus comma; de/dé/qui. |',
    '| Final paragraph line 5 | definit without acute; final i dot/body allocation retained locally; un U_s-minus subset complete final Sigma_i-minus; tel que; final barred U_s-minus cap E_i nonempty), comma. Bar is separate from preceding pour descender. |',
    '| Foot | Archive 23, comment only; hand undetermined. |','',
    '## Complete unresolved local readings','',
    'Vertical bars in the TeX are editorial separators. The following entries preserve complete local candidates, including alternatives carried by graphical comments or invisible annotations.','']
for d in doubt_items:
    md += ['- **'+d['id']+' — '+d['location']+':** '+d['reading']+('. Alternatives: '+ '; '.join(d['alternatives']) if d['alternatives'] else '')+'. '+d['reason']]
    related=byid[d['id']]
    if related.get('complete_phrase_candidates'):
        md += ['  Complete adjoining-phrase candidates: '+ '; '.join(related['complete_phrase_candidates'])+'.']
md += ['', '## Source groups and additional retained qualifications','']
for m in mapped:
    if m['id'].startswith(('B024-G','B024-S','B024-M')):
        md += ['- **'+m['id']+':** '+m['owns']+' Candidates/states: '+ '; '.join(m.get('candidates',[]))+'.']
        for scope in m.get('separate_mark_scopes',[]):
            if scope['hand']=='undetermined hand':
                md += ['  '+scope['scope']+': '+scope['role']+'; '+scope['hand']+'; '+scope['attachment']+'.']
md += ['', '## Witness differences','', '| ID | Complete local reading | C differs | H differs | Original C status |', '| --- | --- | --- | --- | --- |']
for d in diffs:
    md += ['| '+d['id']+' | '+d['reading'].replace('|',' / ').replace('\n',' ')+' | '+str(d['diff_C']).lower()+' | '+str(d['diff_H']).lower()+' | '+str(d['C_doubt_status'] or '—')+' |']
md += ['', '## Limits and checks','', 'No author-written uncertainty, title, date or page count was observed. Archive 23 is recorded separately. The exact source ownership, literal paths, local candidates, original C row identities, processing provenance and viewing events are in report.json, source_map.json and view_audit.json. No compilation or rendering was attempted. Source-only checks are recorded in report.json.']
(ROOT/'reading.md').write_text('\n'.join(md)+'\n')
