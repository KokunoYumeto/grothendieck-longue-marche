from pathlib import Path
import json,re,hashlib
out=Path('/workspace/scratch/94548b74fbe0/out/readers/023/A')
groups={}

def graphic(gid,origin,rect,baseline,body,reading,qualifier=False,unit='.08mm',ownership='',observed=None):
    # Manual approximations from the single authorized visual inspections.
    # Pixel coordinate declarations perform no image matching or curve computation.
    lines=[f'% BEGIN {gid}',f'% full-scan origin: {origin}; local rectangle: {rect}; local baseline: {baseline}; x={unit}, y=-{unit}.',f'% reading/state: {reading}',f'% ownership: {ownership}']
    if qualifier: lines.append(r'\unsure{%')
    lines.append(r'\begin{tikzpicture}[x='+unit+',y=-'+unit+r',baseline={(0,'+str(baseline)+r')},line cap=round,line join=round]')
    lines.append(r'\path[use as bounding box] ('+str(rect[0])+','+str(rect[1])+') rectangle ('+str(rect[2])+','+str(rect[3])+');')
    lines.extend(body.strip().splitlines())
    lines.append(r'\end{tikzpicture}%')
    if qualifier: lines.append('}%')
    lines.append(f'% END {gid}')
    groups[gid]={'id':gid,'full_scan_origin':origin,'local_rectangle':rect,'baseline':[0,baseline],'coordinate_unit':unit,'y_direction':'down','observed_locus_bbox':observed,'reading':reading,'qualification_on_visible_group':qualifier,'ownership':ownership,'source_owner':'reading.tex','manual_approximation':True}
    return '\n'.join(lines)

G01=graphic('A023-G01',[260,230],[0,0,20,16],12,r'''
\fill (4,5) -- (12,2) -- (17,5) -- (14,11) -- (5,10) -- cycle;
''',r'complete opening mark: a primary; independent small lozenge/point alternative; no settled character or role',True,ownership='The reduced mark after que l\'on; owns no adjoining word and adds no second a.',observed=[262,232,279,244])
M01=graphic('A023-M01',[98,436],[0,0,11,15],12,r'''
\draw[gray,line width=.15pt] (4,6) -- (3,11);
\fill (3,3) -- (7,3) -- (5,7) -- (3,6) -- cycle;
''','tiny dark point with a faint downward tail; role, hand and surface origin unresolved',True,ownership='Mark only in the left margin; the adjacent E_beta remains outside.',observed=[100,438,106,448])
G02=graphic('A023-G02',[695,409],[0,0,96,128],70,r'''
\draw[line width=.45pt] (29,12) .. controls (29,48) and (30,72) .. (44,61) .. controls (56,75) and (64,36) .. (65,7);
\draw[line width=.35pt] (22,21) .. controls (32,37) and (40,51) .. (43,58) .. controls (47,63) and (52,62) .. (54,51);
\node[anchor=base,inner sep=0pt,outer sep=0pt] at (45,118) {$\scriptstyle\alpha\in K$};
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {$\phantom{\deleted{\bigvee}\bigcup}$};
''',r'complete states: \deleted{\bigvee}\bigcup indexed by alpha in K | retraced \bigcup indexed by alpha in K',True,ownership='Both cup runs, crossing diagonal and the one alpha-in-K limit; no adjoining X, V, equality, Sigma or comma.',observed=[693,416,790,534])
S01=graphic('A023-S01',[806,384],[0,0,96,97],76,r'''
\draw[line width=.4pt] (5,32) -- (41,31);
\draw[line width=.4pt] (12,33) -- (36,54) -- (12,74) -- (53,73);
\draw[line width=.45pt] (27,36) -- (28,73);
\draw[line width=.4pt] (40,17) -- (64,8) -- (84,22);
\draw[line width=.5pt] (66,45) -- (82,45) (74,37) -- (75,53);
\draw[line width=.4pt] (80,73) .. controls (72,77) and (65,83) .. (75,83) .. controls (80,82) and (82,74) .. (85,73) (78,78) -- (88,84);
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,76) {$\phantom{\widehat{\deleted{\unsure{I|E}}\Sigma}_\alpha^+}$};
''',r'complete states: \widehat{\deleted{I}\Sigma}_\alpha^+ | \widehat{\deleted{E}\Sigma}_\alpha^+ | \widehat{\Sigma}_\alpha^+ with an internal retrace',True,ownership='One head/body, the internal upright, roof, plus and lower alpha. The upright occurs once; the hidden annotation supplies no extra visible deletion rule.',observed=[810,390,895,469])
M02=graphic('A023-M02',[1115,558],[0,0,12,12],0,r'''
\fill[brown!70!black] (1,2) -- (7,5) -- (9,8) -- (5,8) -- (0,4) -- cycle;
''','short brown oblique fleck; role, hand and surface origin unresolved',True,ownership='Mark only; on a, en and fait belong to the surrounding G03.',observed=[1115,559,1124,568])
G03=graphic('A023-G03',[941,558],[0,0,477,116],74,r'''
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,74) {\unsure{on a}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (233,74) {en};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (337,74) {fait};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (174,0) {%
'''+M02+r'''
};
''',r'\unsure{on a} en fait, with the independent qualified fleck above the gap',ownership='Owns exactly on a en fait and M02; the preceding comma remains outside.',observed=[941,558,1418,665])
M03=graphic('A023-M03',[1099,859],[0,0,10,13],0,r'''
\fill (3,3) -- (5,4) -- (4,7) -- (3,6) -- cycle;
''','tiny short point below the right part of assertion; role, hand and surface origin unresolved',True,ownership='Mark only; l\'assertion belongs to G04.',observed=[1101,861,1106,867])
G04=graphic('A023-G04',[885,789],[0,0,248,88],40,r'''
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,40) {l'assertion};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (214,70) {%
'''+M03+r'''
};
''',"l'assertion with the qualified low point",ownership='Owns l\'assertion once and M03; the preceding verb and following dash remain outside.',observed=[885,789,1128,868])
G05=graphic('A023-G05',[376,1420],[0,0,43,61],39,r'''
\draw[line width=.4pt] (5,20) -- (31,18) (4,35) -- (33,31);
\draw[line width=.7pt] (21,11) .. controls (24,28) and (29,47) .. (20,53) -- (16,55);
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (0,39) {$\phantom{\unsure{\ne|\deleted{\ne}{,}}}$};
''',r'complete states: \ne | \deleted{\ne}{,}; first relation only',True,ownership='Owns both short bars and the heavy downward hook; the two alpha/beta glyphs stay outside. No second printed comma is added.',observed=[379,1429,411,1477])
S05=graphic('A023-S05',[1003,1387],[0,0,85,67],47,r'''
\draw[line width=.25pt] (4,10) -- (43,3) -- (55,7) -- (36,12);
\draw[line width=.4pt] (7,16) -- (39,17) -- (46,22) -- (9,44) -- (60,40) .. controls (58,46) and (49,51) .. (53,54) .. controls (60,55) and (66,47) .. (64,42);
\draw[line width=.4pt] (59,48) -- (75,54);
\draw[line width=.45pt] (65,13) -- (78,13) (73,7) -- (74,20);
''',r'\Sigma_\alpha^+ with a short detached/retraced head | \Sigma_\alpha^+ with an independent upper run; role unresolved, no operation assigned',True,ownership='Complete first intersection Sigma: separate upper return, body continuing into alpha, alpha exit and plus. First printed recurring head-role qualification on this page.',observed=[1006,1389,1084,1443])
S06=graphic('A023-S06',[1143,1385],[0,0,86,102],47,r'''
\draw[line width=.25pt] (4,9) -- (42,4) -- (48,7) -- (10,13);
\draw[line width=.4pt] (4,16) -- (30,18) -- (39,23) -- (8,44) -- (42,39) .. controls (52,42) and (42,84) .. (43,91) .. controls (45,85) and (45,63) .. (53,58) .. controls (66,44) and (72,68) .. (61,75);
\draw[line width=.45pt] (62,13) -- (76,13) (70,9) -- (71,22);
''',r'\Sigma_\beta^+; the short upper return has a pale break before the body. Head-retrace | independent upper-run role remains locally unresolved.',ownership='Complete second intersection Sigma and connected beta descent, upper return and plus. Recurring head-role doubt printed at S05; no second beta node.',observed=[1145,1388,1224,1482])
S07=graphic('A023-S07',[1306,1482],[0,0,97,83],58,r'''
\draw[line width=.35pt] (7,17) -- (42,14);
\draw[line width=.45pt] (7,23) -- (36,32) -- (11,58) -- (57,57);
\draw[line width=.5pt] (64,8) -- (86,8) (76,0) -- (76,19);
\draw[line width=.4pt] (77,67) .. controls (67,71) and (64,78) .. (73,77) .. controls (79,76) and (83,68) .. (85,66) (75,72) -- (89,79);
''',r'\Sigma_\alpha^+; clear gap separates the short head from the upper diagonal. Head-retrace | independent upper-run role remains locally unresolved.',ownership='Complete Sigma after the lemma union, with head, body, upper plus and low alpha. The union stays outside.',observed=[1311,1482,1395,1562])
S08=graphic('A023-S08',[1208,1586],[0,0,94,66],45,r'''
\draw[line width=.35pt] (10,10) -- (42,7);
\draw[line width=.4pt] (9,15) -- (37,24) -- (9,43) -- (59,42);
\draw[line width=.45pt] (67,12) -- (84,12) (75,4) -- (76,24);
\draw[line width=.4pt] (68,48) .. controls (60,51) and (55,58) .. (65,57) .. controls (70,56) and (73,49) .. (75,47) (66,52) -- (82,59);
''',r'\Sigma_\alpha^+; short head remains above the beginning of the diagonal with a visible pale interval. Head-retrace | independent upper-run role remains locally unresolved.',ownership='Complete lemma-conclusion Sigma, plus and alpha; final period stays outside.',observed=[1215,1591,1296,1645])
S09=graphic('A023-S09',[1361,1807],[0,0,80,68],50,r'''
\draw[line width=.35pt] (5,10) -- (43,8);
\draw[line width=.4pt] (6,17) -- (36,29) -- (9,47) -- (43,47) .. controls (47,47) and (49,51) .. (49,54);
\fill (48,30) circle[radius=.13mm];
\draw[line width=.4pt] (62,6) .. controls (55,8) and (54,14) .. (60,14) .. controls (66,14) and (67,7) .. (68,5) (61,10) -- (73,17);
''',r'\Sigma_i^\alpha; the body-foot returns into the low i hook and one high dot belongs to that index; raised alpha retained. Detached head role: head-retrace | independent upper run.',ownership='Owns only the family Sigma, raised alpha, low hook and its one dot. The parentheses and external alpha-in-K family index remain outside.',observed=[1365,1812,1436,1864])
M05=graphic('A023-M05',[1429,1910],[0,0,9,9],0,r'''
\fill (2,3) -- (5,2) -- (7,5) -- (3,5) -- cycle;
''','small point beside the upper end of the corollary plus; attachment/role, hand and surface origin unresolved',True,ownership='Point only; the plus stroke is owned by S10 and is drawn once.',observed=[1431,1912,1437,1916])
S10=graphic('A023-S10',[1341,1914],[0,-5,108,79],55,r'''
\draw[line width=.45pt] (7,11) -- (54,9) (8,12) -- (48,27) -- (6,52) -- (62,51);
\draw[line width=.5pt] (71,10) -- (89,10) (80,0) -- (83,26);
\draw[line width=.45pt] (78,51) -- (82,58) .. controls (80,65) and (75,72) .. (70,70) .. controls (65,68) and (68,59) .. (74,59) .. controls (79,60) and (79,68) .. (82,71);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (88,-4) {%
'''+M05+r'''
};
''',r'\Sigma_\alpha^+ with joined head/body, retraced alpha and one locally qualified point adjoining the plus',ownership='Complete corollary constituent Sigma, alpha, plus and M05; parentheses stay outside.',observed=[1346,1912,1440,1980])
S11=graphic('A023-S11',[1038,1998],[0,0,95,107],85,r'''
\draw[line width=.45pt] (11,29) -- (40,12) -- (67,31);
\draw[line width=.35pt] (8,49) -- (45,44);
\draw[line width=.45pt] (8,57) -- (39,66) -- (10,82) -- (48,82);
\draw[line width=.45pt] (61,58) -- (79,57) (71,49) -- (72,71);
\draw[line width=.4pt] (65,89) .. controls (57,91) and (55,98) .. (62,98) .. controls (69,97) and (70,89) .. (72,88) (63,93) -- (80,100);
''',r'\widehat{\Sigma}_\alpha^+; roof, separate short head and body form three local levels. Short-head role: head-retrace | independent upper run; roof itself firm.',ownership='Complete final hatted Sigma, roof, short head, body, plus and alpha. The shared f/cup strokes remain owned by G07; final period stays in G07.',observed=[1044,2006,1118,2101])
M04=graphic('A023-M04',[1601,1733],[0,0,16,20],15,r'''
\fill (9,3) -- (11,3) -- (10,6) -- (8,5) -- cycle;
\fill (3,10) -- (5,10) -- (5,12) -- (3,13) -- cycle;
''','two small diagonally arranged points at the right of the unfinished line; role, hand and surface origin unresolved',True,ownership='Mark cluster only. The preceding du remains outside and no colon or period is assigned.',observed=[1603,1735,1613,1747])

def as_scope(gid,source,shift):
    # Required source-coordinate embedding, with no nested unanchored picture box.
    first=source.index('\\begin{tikzpicture}')
    body_start=source.index('\n',source.index('\\path[use as bounding box]',first))+1
    body_end=source.rfind('\\end{tikzpicture}%')
    comments=source[:first]
    groups[gid]['placement']={'kind':'scope','parent':'A023-G07','translation':list(shift)}
    return comments+'\\begin{scope}[shift={('+str(shift[0])+','+str(shift[1])+')}]\n'+source[body_start:body_end]+'\\end{scope}\n% END '+gid+'\n'
S10_scope=as_scope('A023-S10',S10,(1091,14))
S11_scope=as_scope('A023-S11',S11,(788,98))

# The lower block is a single connected group: its f descender and cup right side share one run.
G07=graphic('A023-G07',[250,1900],[0,0,1400,248],230,r'''
% G07-RULE: upper pale run, short interruption, lower run.
\draw[gray,line width=.2pt] (20,39) .. controls (18,88) and (21,109) .. (21,126);
\draw[line width=.25pt] (21,131) .. controls (22,173) and (25,209) .. (36,238);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (53,138) {la};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (158,135) {partition};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (441,116) {$\Pi_K^{\unsure{\circ|0}}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (590,102) {est};
% G07-FCUP-01: shared main f upright, continuing through the right cup side and its rounded bottom.
\draw[line width=.4pt] (728,48) .. controls (734,80) and (736,111) .. (737,139) .. controls (741,170) and (738,192) .. (717,202) .. controls (697,211) and (691,194) .. (688,166) -- (686,152);
% G07-FCUP-02: the f cross/left returning loop; the main upright is not redrawn here.
\draw[line width=.35pt] (735,96) .. controls (718,102) and (702,99) .. (690,110) .. controls (695,121) and (714,135) .. (737,139);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (744,99) {ormée};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (937,82) {des};
'''+S10_scope+r'''
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1225,75) {$(\alpha\in K)$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (73,230) {et de};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (446,214) {$V=$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (593,202) {$X\setminus$};
% G07-FCUP-03: definite upper cross-run of the union; no algebraic operation assigned to this run.
\draw[line width=.45pt] (683,160) -- (729,159);
\node[anchor=base,inner sep=0pt,outer sep=0pt] at (729,232) {$\scriptstyle\alpha\in K$};
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at (685,211) {$\phantom{\bigcup_{\alpha\in K}}$};
'''+S11_scope+r'''
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (934,208) {.};
''',r'la partition \Pi_K^{\circ|0} est formée des \Sigma_\alpha^+ (\alpha\in K) et de V=X\setminus[union with high cross-run]_{\alpha\in K}\widehat{\Sigma}_\alpha^+.',ownership='Entire two-line corollary body and its left rule. Owns la partition, Pi/K/ring, est, the complete word formée (literal f plus ormée node), des, S10, (alpha in K), et de, V=, X-setminus, the one shared f/cup run and high cross-run, the cup limit, S11 and final period. Corollaire/Avec heading remains outside.',observed=[267,1912,1634,2139])

tex=r'''\scanpage{23}
Soit maintenant $\beta\in I\setminus K$, prouvons que l'on
'''+G01+r'''
\ $\overline V\cap E_\beta=\varnothing$. En effet, $V$ ne \deleted{contient} \inserted{rencontre} aucun $E_i$ $(i\in I)$ donc
\reversemarginpar\margin{%
'''+M01+r'''
}\normalmarginpar
$E_\beta\subset X\setminus V=
'''+G02+'\n'+r'\;'+'\n'+S01+r'''
$, \deleted{\unsure{donc si}} je dis que si $\beta\in I\setminus K$,
'''+G03+r'''
\[
E_\beta\subset\bigcup\Sigma_\alpha^+\qquad\text{(ouvert disjoint de }V\text{)}
\]
% slanted; all three note lines belong to this independent marginal note.
\reversemarginpar\margin{\makebox[\linewidth][r]{\rotatebox{24}{\shortstack[l]{C'est trivial, \deleted{\illegible{1}}\\du fait que les $E_i$ $(i\in\unsure{I|J})$\\sont disjoints}}}}\normalmarginpar
\unsure{qui|ce qui} \unsure{prouvera|prouve}
'''+G04+r'''
\ -- mieux, je dis que $\exists\alpha\in K$ tel que $E_\beta\subset\Sigma_\alpha^+$. Cela revient \unsure{au}

\uline{Lemme} Soit $K\subset I$, \deleted{tel que les} \deleted{et} des $\Sigma_\alpha^+$ $(\alpha\in K)$ \unsure{tels} que
\[
\alpha\mathrel{%
'''+G05+r'''
}\beta\in K,\ \alpha\ne\beta\ \Rightarrow
'''+S05+r'''
\cap
'''+S06+r'''
=\varnothing.
\]
Soit $i\in I\setminus K$ tel que $E_i\subset\bigcup
'''+S07+r'''
$, alors \deleted{$E_i$ est \unsure{contenu|contenue}} \inserted{$\exists\alpha\in K$ tel que} $E_i\subset
'''+S08+r'''
$.

Cela \deleted{signifie que} \unsure{precise|précise|provient|precise le|précise le} du\hspace{2em}\raisebox{-1ex}{%
'''+M04+r'''
}

\uline{Corollaire} Avec les hyp. \unsure{préc.} sur $(
'''+S09+r'''
)_{\alpha\in K}$,
\figure{%
'''+G07+r'''
}

\unsure{Immédiat|Immèdiat|Immediat} par \unsure{récurrence|rècurrence|recurrence} sur $\operatorname{card} K\geqslant 0$.
% archive sheet number: 22
'''
(out/'reading.tex').write_text(tex,encoding='utf-8')
(out/'graphics_initial.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote reading.tex and initial graphics registry; report and source-only audit follow.')
