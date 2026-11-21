from pathlib import Path
import json,re,hashlib
from datetime import datetime,timezone
R=Path(__file__).parent
G=[]
def tikz(gid,origin,rect,baseline,paths,reading,candidates=None,qualifier=False,owns='',role='',hand='his hand',crop=None,components=None):
    opts='x=0.01cm,y=-0.01cm,line cap=round,line join=round,baseline=(base)'
    lines=[r'\tikz['+opts+']{',f'\\coordinate (base) at (0,{baseline});',f'\\useasboundingbox (0,0) rectangle ({rect[0]},{rect[1]});']
    lines += paths
    if reading:
        lines += [f'\\node[overlay,anchor=base west,inner sep=0,outer sep=0] at (0,{baseline}) {{\\phantom{{{reading}}}}};']
    lines += ['}']
    body='\n'.join(lines)
    if qualifier: body='\\unsure{'+body+'}'
    annotations=''.join('% Complete candidate: '+c+'\n' for c in (candidates or ([reading] if reading else [])))
    annotations += '% Ownership: '+owns+'\n% Qualification: '+role+'\n% Hand: '+hand+'\n'
    block=f'% {gid} begin\n'+annotations+body+f'\n% {gid} end\n'
    G.append({'id':gid,'source':block,'origin_full':origin,'drawing_rectangle_local':[0,0,*rect],'baseline_local':[0,baseline],'units':'x=0.01 cm per full-scan pixel; y=-0.01 cm per full-scan pixel','mapping':'full x = origin_full[0] + local x; full y = origin_full[1] + local y','reading':reading,'complete_candidates':candidates or [reading],'printed_qualifier':qualifier,'owns':owns,'role_and_attachment':role,'hand':hand,'crop':crop,'components':components or paths,'approximation':'Manually specified visible-path approximation; no rendering or metric/image matching performed.'})
    return block

g01=tikz('C025-G01',[285,70],[405,70],60,[
 r'\node[anchor=base west,inner sep=0,outer sep=0] at (0,60) {\rlap{Soit en effet}\phantom{\deleted{Soit en effet}}};',
 r'\draw[line width=.6pt] (5,59) .. controls (85,42) and (225,42) .. (400,36);'
],None,['\\deleted{Soit en effet}'],owns='Soit en effet and its one long cancellation only',crop='01_opening.png')
s01=tikz('C025-S01',[830,120],[100,82],65,[
 r'\draw[line width=.85pt] (10,11) .. controls (21,9) and (34,11) .. (46,12);',
 r'\draw[line width=.65pt] (11,19) .. controls (20,20) and (34,27) .. (43,32) .. controls (41,39) and (16,54) .. (5,59) .. controls (23,60) and (48,60) .. (61,62) .. controls (65,63) and (65,67) .. (65,71);',
 r'\draw[line width=.5pt] (12,20) .. controls (7,22) and (8,26) .. (8,29);',
 r'\draw[line width=.5pt] (15,23) .. controls (18,35) and (20,47) .. (19,59);',
 r'\draw[line width=.45pt] (14,17) .. controls (27,21) and (35,26) .. (42,31);',
 r'\draw[line width=.65pt] (66,10) .. controls (73,9) and (80,11) .. (87,11);',
 r'\draw[line width=.7pt] (74,38) .. controls (73,41) and (76,44) .. (77,46);'
],r'$\deleted{\unsure{E|I}}\Sigma_{\unsure{i|\prime}}^-$',[
 r'\deleted{E}\Sigma_i^- with short head/retrace',r'\deleted{I}\Sigma_i^- with short head/retrace',r'\deleted{E}\Sigma_{\prime}^- with short head/retrace',r'\deleted{I}\Sigma_{\prime}^- with short head/retrace',r'\deleted{E}\Sigma_i^- with independent upper run',r'\deleted{I}\Sigma_i^- with independent upper run',r'\deleted{E}\Sigma_{\prime}^- with independent upper run',r'\deleted{I}\Sigma_{\prime}^- with independent upper run'],True,'Complete overwritten Sigma, old upright, short head, minus and small index; following comma outside','Head/retrace versus independent upper run unresolved; i/prime-like index unresolved. First printed qualifier for recurring detached Sigma heads and undotted short Sigma indices.','his hand for body and signs; undetermined hand for independent-upper-run candidate','02_first_sigma.png')
g02=tikz('C025-G02',[1100,150],[45,40],30,[
 r'\draw[line width=.55pt] (5,18) -- (30,17);',
 r'\draw[line width=.55pt] (5,27) -- (29,28);',
 r'\draw[line width=.8pt] (11,27) .. controls (23,4) and (34,7) .. (39,31);'
],r'$\deleted{\unsure{=}}\cap$',[r'\deleted{=}\cap',r'\cap with unidentified crossed predecessor',r'\cap with two transverse retraces'],True,'The old/current relation only; barred U and following E outside','Two short transverse strokes present; old-equals versus retrace allocation unsettled.',crop='03_intersection.png')
e01=tikz('C025-E01',[1160,133],[72,60],43,[
 r'\draw[line width=.4pt] (11,9) .. controls (18,4) and (29,4) .. (37,10);',
 r'\draw[line width=.65pt] (5,11) -- (7,36) .. controls (9,39) and (21,39) .. (28,40);',
 r'\draw[line width=.6pt] (8,25) -- (27,24);',
 r'\fill (57,25) -- (59,24) -- (58,28) -- (56,29) -- cycle;',
 r'\draw[line width=.55pt] (48,41) .. controls (51,45) and (51,49) .. (47,51);'
],r'$E_{\unsure{i|j}}$',[r'E_i with detached top arm',r'E_j with detached top arm',r'E_i with independent upper curve',r'E_j with independent upper curve'],True,'Complete E, detached top curve, index body and its single high point','Index i/j unresolved; upper curve top-arm versus independent-run role unresolved. Point belongs to the qualified index group, no second dot supplied.','his hand for E/body; undetermined hand for independent-upper-curve candidate','03_intersection.png')
g03=tikz('C025-G03',[1408,140],[132,60],43,[
 r'\node[anchor=base west,inner sep=0,outer sep=0] at (0,42) {\rlap{et si}\phantom{\deleted{et si}}};',
 r'\draw[line width=.55pt] (4,23) .. controls (30,32) and (87,42) .. (123,50);'
],None,[r'\deleted{et si}'],False,'et si and its down-right cancellation; alors outside',crop='04_cancelled_connective.png')
g04=tikz('C025-G04',[295,280],[145,28],19,[
 r'\fill (6,15) -- (8,13) -- (12,14) -- (8,17) -- (6,19) -- cycle;',
 r'\draw[line width=.45pt] (31,16) .. controls (43,14) and (55,9) .. (62,15);',
 r'\draw[line width=.55pt] (128,15) .. controls (131,12) and (134,14) .. (137,15);'
],r'\unsure{on a}',['on a','three reduced separate strokes without established lexical reading'],True,'Complete proposed on a only; no duplicate printed on a','Whole phrase reading is uncertain; the three shapes are preserved.','his hand proposed for phrase; undetermined hand under nonlexical-strokes alternative','05_on_a.png')
g05=tikz('C025-G05',[848,270],[82,78],66,[
 r'\draw[line width=.65pt] (16,4) .. controls (18,11) and (19,20) .. (20,29) .. controls (22,47) and (24,66) .. (39,68) .. controls (57,70) and (72,48) .. (72,17);',
 r'\draw[line width=.7pt] (24,18) .. controls (26,34) and (24,55) .. (35,64) .. controls (47,73) and (68,54) .. (68,22);',
 r'\draw[line width=.45pt] (5,17) .. controls (20,5) and (28,16) .. (30,30);',
 r'\draw[line width=.65pt] (7,22) -- (52,21);',
 r'\draw[line width=.45pt] (69,16) .. controls (75,20) and (76,35) .. (70,42);'
],r'$\unsure{\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup|\deleted{\bigcap}\bigcup}$',[r'\rlap{\raisebox{.65ex}{$\scriptstyle-$}}\bigcup',r'\deleted{\bigcap}\bigcup'],True,'Operator body, high cross, upper arch and doubled bowl only; limit alpha in K outside','High cross presence firm; complete earlier-intersection/union state remains unresolved.',crop='06_main_operator.png')
s02=tikz('C025-S02',[968,252],[105,100],78,[
 r'\draw[line width=.55pt] (26,18) -- (45,7) .. controls (54,17) and (59,20) .. (66,22);',
 r'\draw[line width=.55pt] (7,41) -- (55,35);',
 r'\draw[line width=.55pt] (7,41) .. controls (65,55) and (41,59) .. (6,77) .. controls (25,79) and (45,72) .. (56,81);',
 r'\draw[line width=.65pt] (77,35) -- (78,52);',
 r'\draw[line width=.65pt] (70,44) -- (91,43);',
 r'\draw[line width=.55pt] (79,61) .. controls (78,76) and (72,89) .. (65,88) .. controls (57,88) and (59,72) .. (66,73) .. controls (75,72) and (75,87) .. (89,89);',
 r'\fill (72,65) -- (75,66) -- (74,69) -- (71,67) -- cycle;',
 r'\draw[gray,line width=.25pt] (68,56) -- (70,57);'
],r'$\widehat{\Sigma}_\alpha^+$',[r'\widehat{\Sigma}_\alpha^+ with upper alpha traces attached to index',r'\widehat{\Sigma}_\alpha^+ with independent dark point and faint short slash'],True,'Complete hatted Sigma, joined head/body, plus, alpha and two upper-alpha traces','Two tiny traces retain unresolved index/independent-mark attachment and hand; neither is duplicated by a separate printed index.','his hand for main glyph; undetermined hand for small upper-alpha traces','06_main_operator.png')
g06=tikz('C025-G06',[1220,295],[66,32],25,[
 r'\fill (5,25) -- (9,20) -- (12,21) -- (10,24) -- cycle;',
 r'\draw[line width=.5pt] (23,25) .. controls (32,22) and (42,23) .. (49,24);',
 r'\draw[line width=.55pt] (39,7) -- (41,12);'
],r'\unsure{où}',['où','ou with separate upper stroke'],True,'Complete reduced où including its high stroke; i in K outside','Word and raised-stroke attachment remain qualified.','his hand for proposed word; undetermined hand for independent-upper-stroke alternative','07_ou.png')
s03=tikz('C025-S03',[1243,357],[100,56],40,[
 r'\draw[line width=.5pt] (10,12) -- (59,8);',
 r'\draw[line width=.5pt] (10,12) .. controls (52,22) and (50,23) .. (7,40) -- (57,40);',
 r'\draw[line width=.6pt] (76,7) -- (78,18);',r'\draw[line width=.6pt] (69,12) -- (85,11);',
 r'\draw[line width=.55pt] (75,38) .. controls (66,51) and (59,48) .. (60,45) .. controls (63,42) and (76,46) .. (84,47);'
],r'$\Sigma_\alpha^+$',owns='Complete condition Sigma with its joined head, alpha and plus',role='Head/body join seen locally; no separate head-role uncertainty added.',crop='08_right_condition.png')
e02=tikz('C025-E02',[1497,352],[59,48],39,[
 r'\draw[line width=.45pt] (8,8) .. controls (15,6) and (22,8) .. (28,8);',
 r'\draw[line width=.5pt] (3,8) -- (2,34) -- (23,34);',r'\draw[line width=.5pt] (4,22) -- (22,22);',
 r'\draw[line width=.5pt] (48,28) .. controls (40,43) and (31,41) .. (31,36) .. controls (33,31) and (41,36) .. (49,40);'
],r'$E_\alpha$',[r'E_\alpha with detached top arm',r'E_\alpha with independent upper run'],False,'Complete E_alpha in pi0 argument, all three arms and alpha','Local top-arm/independent-run alternative retained under first E qualifier at E01.','his hand for E; undetermined hand for independent-upper-run alternative','08_right_condition.png')
g07=tikz('C025-G07',[1597,345],[72,62],47,[
 r'\draw[line width=.5pt] (12,5) -- (14,46) .. controls (20,44) and (25,38) .. (30,33);',
 r'\draw[line width=.5pt] (5,25) -- (36,9) .. controls (36,18) and (25,23) .. (19,30);',
 r'\draw[line width=.55pt] (19,30) .. controls (28,37) and (35,37) .. (41,25);',
 r'\draw[line width=.55pt] (54,22) .. controls (49,29) and (49,37) .. (48,43);',
 r'\draw[line width=.6pt] (23,35) -- (68,34);'
],r'\deleted{\unsure{les|K|tel}}',[r'\deleted{les}',r'\deleted{K}',r'\deleted{tel}'],True,'Entire crossed endpoint cluster; no separate comma','Letter sequence remains obscured by crossing; H tel preserved as a complete alternative.',crop='08_right_condition.png')
g08=tikz('C025-G08',[1105,437],[56,79],63,[
 r'\draw[line width=.45pt] (6,13) .. controls (7,31) and (5,56) .. (17,62) .. controls (32,73) and (46,47) .. (45,10);',
 r'\draw[line width=.5pt] (13,25) -- (44,14) -- (26,40) -- (45,39);',
 r'\draw[line width=.55pt] (32,62) .. controls (30,75) and (41,73) .. (47,65);'
],r'$\deleted{\unsure{U\Sigma|\bigcup\Sigma|U}}$',[r'\deleted{U\Sigma}',r'\deleted{\bigcup\Sigma}',r'\deleted{U}',r'U\Sigma',r'\text{et}'],True,'Entire pre-les cluster only; live les is outside','Original three cancelled candidates retained; live U Sigma and live et remain whole-state alternatives because no independent strike is isolated.',crop='09_before_les.png')
s04=tikz('C025-S04',[1288,437],[77,54],39,[
 r'\draw[line width=.5pt] (13,7) -- (37,8);',
 r'\draw[line width=.5pt] (8,15) .. controls (36,18) and (42,15) .. (6,36) .. controls (17,39) and (30,38) .. (40,36) .. controls (49,31) and (51,35) .. (48,40) .. controls (41,48) and (37,42) .. (42,40) .. controls (48,39) and (56,43) .. (58,44);',
 r'\draw[line width=.55pt] (58,7) -- (60,20);',r'\draw[line width=.55pt] (48,11) -- (64,10);'
],r'$\Sigma_\alpha^+$',[r'\Sigma_\alpha^+ with detached head/retrace',r'\Sigma_\alpha^+ with independent upper run'],False,'Complete disjointness Sigma, head, plus and alpha joined into foot','Local role retained under S01 first qualifier; joined foot/alpha stroke occurs once.','his hand for body; undetermined hand for independent-upper-run candidate','10_mut_disjoints.png')
g09=tikz('C025-G09',[875,485],[190,157],130,[
 r'\node[anchor=base west,inner sep=0,outer sep=0] at (0,58) {\rlap{$K\setminus\{i\}$}\phantom{$\inserted{K\setminus\{i\}}$}};',
 r'\node[anchor=base west,inner sep=0,outer sep=0] at (83,133) {\rlap{$K$}\phantom{$\deleted{K}$}};',
 r'\draw[line width=.5pt] (103,149) -- (127,83);',
 r'\draw[line width=.35pt] (88,82) -- (122,65) .. controls (123,74) and (110,90) .. (101,103) .. controls (103,114) and (119,108) .. (123,119);',
 r'\draw[gray!75,line width=.35pt] (50,140) .. controls (42,106) and (71,93) .. (92,85) .. controls (122,73) and (153,61) .. (183,45) -- (178,44);'
],r'$\deleted{K}\inserted{K\setminus\{i\}}$',[r'\deleted{K}\inserted{K\setminus\{i\}} with long curved insertion guide',r'\deleted{K}\inserted{K\setminus\{i\}} with extended curved cancellation'],True,'Deleted K, raised replacement K setminus braced i and all local crossing/curved runs; et les outside','Replacement attachment firm. The long curved run guide/cancellation role remains unresolved.',crop='11_K_revision.png')
s05=tikz('C025-S05',[1236,552],[88,65],47,[
 r'\draw[line width=.45pt] (9,8) -- (49,9);',
 r'\draw[line width=.45pt] (13,18) .. controls (53,24) and (40,28) .. (5,46) -- (40,46);',
 r'\draw[line width=.5pt] (67,9) -- (69,22);',r'\draw[line width=.5pt] (59,15) -- (75,15);',
 r'\draw[line width=.5pt] (65,43) .. controls (57,57) and (44,56) .. (45,51) .. controls (48,46) and (61,53) .. (69,56);'
],r'$\Sigma_\alpha^+$',[r'\Sigma_\alpha^+ with detached head/retrace',r'\Sigma_\alpha^+ with independent upper run'],False,'Complete prose Sigma; following parenthetical outside','Local role retained under S01 first qualifier.','his hand for body; undetermined hand for independent-upper-run candidate','12_prose_sigma.png')
s06=tikz('C025-S06',[293,818],[110,78],64,[
 r'\draw[line width=.3pt] (4,17) -- (5,17);',
 r'\draw[line width=.4pt] (9,16) -- (62,8);',
 r'\draw[line width=.5pt] (17,23) .. controls (78,25) and (65,35) .. (5,68) .. controls (33,65) and (57,58) .. (76,56) -- (78,64);',
 r'\draw[line width=.6pt] (92,8) -- (95,22);',r'\draw[line width=.6pt] (84,14) -- (102,14);',
 r'\draw[line width=.55pt] (78,36) -- (82,39);'
],r'$\Sigma_i^+$',[r'\Sigma_i^+ with detached head/retrace',r'\Sigma_{\prime}^+ with detached head/retrace',r'\Sigma_i^+ with independent upper run',r'\Sigma_{\prime}^+ with independent upper run'],False,'Complete lower first Sigma, interrupted head entrance, body, plus and short index; i.e. outside','Local head and i/prime alternatives retained under first printed S01 qualifier.','his hand for body; undetermined hand for independent-upper-run candidate','14_lower_sigmas.png')
s07=tikz('C025-S07',[550,807],[101,69],52,[
 r'\draw[line width=.4pt] (7,15) -- (45,11);',
 r'\draw[line width=.45pt] (6,27) .. controls (64,29) and (41,39) .. (13,53) .. controls (39,48) and (54,47) .. (64,57);',
 r'\draw[line width=.55pt] (70,8) -- (91,8);',r'\draw[line width=.55pt] (66,43) -- (67,47);'
],r'$\Sigma_i^-$',[r'\Sigma_i^- with detached head/retrace',r'\Sigma_{\prime}^- with detached head/retrace',r'\Sigma_i^- with independent upper run',r'\Sigma_{\prime}^- with independent upper run'],False,'Complete lower second Sigma, head, minus and short index; following point outside','Local head and i/prime alternatives retained under first printed S01 qualifier.','his hand for body; undetermined hand for independent-upper-run candidate','14_lower_sigmas.png')
s08=tikz('C025-S08',[1171,902],[100,65],48,[
 r'\draw[line width=.45pt] (5,14) .. controls (17,10) and (29,10) .. (39,9);',
 r'\draw[line width=.4pt] (5,14) .. controls (4,19) and (26,19) .. (35,23) .. controls (50,26) and (24,38) .. (3,47) -- (44,46);',
 r'\draw[line width=.6pt] (66,9) -- (94,6);',
 r'\draw[line width=.55pt] (84,34) .. controls (76,57) and (56,57) .. (56,49) .. controls (55,40) and (77,47) .. (95,53);'
],r'$\Sigma_\alpha^-$',owns='Complete final Sigma with joined left return, minus and alpha; no closing brace',role='Joined head/body faint curl seen; alpha retained as written.',crop='15_final_sigma.png')

m01=tikz('C025-M01',[450,1305],[40,50],40,[
 r'\draw[gray!50,line width=.2pt] (18,6) .. controls (26,8) and (26,14) .. (29,19);',
 r'\draw[gray!55,line width=.2pt] (30,22) .. controls (33,28) and (32,32) .. (29,35);',
 r'\draw[gray!40,line width=.2pt] (28,39) .. controls (24,45) and (20,42) .. (13,44);'
],None,['faint interrupted curve; no character supplied'],True,'Faint lower-sheet curve only','Role, hand and surface origin unresolved.','undetermined hand','16_faint_curve.png')
m02=tikz('C025-M02',[1590,1714],[18,23],18,[
 r'\fill (9,5) -- (11,4) -- (10,7) -- (8,7) -- cycle;',
 r'\fill (4,12) -- (6,11) -- (6,13) -- (3,15) -- cycle;'
],None,['two small dark lower-right flecks; no character supplied'],True,'Two lower-right dark flecks only','Role, hand and surface origin unresolved.','undetermined hand',None)

text=r'''\scanpage{25}
'''+g01+r'''Si on a $U_s\subset
'''+s01+r'''$, $\overline{U_s}
'''+g02+e01+r'''\ne\varnothing$,
'''+g03+r'''alors
'''+g04+r'''
\[
\begin{aligned}
U_s=X\setminus\mathop{
'''+g05+r'''}\limits_{\alpha\in K}
'''+s02+r'''&\qquad\text{
'''+g06+r'''}\quad i\in K\subset I\\
&\forall\alpha\in K\qquad
'''+s03+r'''\in\pi_0(X\setminus
'''+e02+r''')\quad\text{
'''+g07+r'''}\\
&
'''+g08+r'''\ \text{les }
'''+s04+r'''\ \text{mut\textsuperscript{t}. disjoints}
\end{aligned}
\]
Il faut voir que
'''+g09+r'''et les $
'''+s05+r'''$ $(\alpha\in K\setminus\{i\})$ sont \unsure{determinés|déterminés|determines} en termes de $i$ et de $
'''+s06+r'''$ i.e. $
'''+s07+r'''$. Je dis que
\[
K\setminus\{i\}=\bigl\{\alpha\in I\mid E_\alpha\subset
'''+s08+r'''
\]
% Lower-sheet graphical traces; each inner origin is mapped below.
\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(base)]
\coordinate (base) at (0,0);
\useasboundingbox (0,0) rectangle (1160,450);
\node[anchor=base west,inner sep=0,outer sep=0] at (0,40) {
'''+m01+r'''};
\node[anchor=base west,inner sep=0,outer sep=0] at (1140,427) {
'''+m02+r'''};
\end{tikzpicture}}
% archive sheet number: 24
'''
# Comments keep their newline; empty physical lines inside math are forbidden.
text=text.replace('\n\n','\n')
(R/'reading.tex').write_text(text)
for g in G:
    g['source']=g['source'].replace('\n\n','\n')
    start=text.index(g['source']);end=start+len(g['source'])
    g['char_offsets']=[start,end];g['byte_offsets_utf8']=[len(text[:start].encode()),len(text[:end].encode())]
    g['line_start']=text[:start].count('\n')+1;g['line_end']=text[:end].count('\n')
    g['literal_source']=text[start:end]
    g['observed_bbox_full']=next((c['bbox'] for c in json.loads((R/'crops.json').read_text()) if c['path']==g['crop']),[1586,1712,1610,1735])
    del g['source']
# Explicit outer map for lower paired trace groups.
for g in G:
    if g['id']=='C025-M01':g['outer_placement']={'outer_full_origin':[450,1305],'node_local':[0,40],'node_anchor':'base west','inner_baseline':[0,40],'inner_origin_full':[450,1305]}
    if g['id']=='C025-M02':g['outer_placement']={'outer_full_origin':[450,1305],'node_local':[1140,427],'node_anchor':'base west','inner_baseline':[0,18],'inner_origin_full':[1590,1714]}
spans=[]
for key,needle in [('word_determines',r'\unsure{determinés|déterminés|determines}'),('abbreviation',r'\text{mut\textsuperscript{t}. disjoints}'),('final_equation_start',r'K\setminus\{i\}=\bigl\{\alpha\in I\mid E_\alpha\subset'),('archive',r'% archive sheet number: 24')]:
    p=text.index(needle);spans.append({'id':key,'char_offsets':[p,p+len(needle)],'byte_offsets_utf8':[len(text[:p].encode()),len(text[:p+len(needle)].encode())],'literal_source':needle})
(R/'source_map.json').write_text(json.dumps({'scan':25,'reader':'C','source_file':'reading.tex','sha256':hashlib.sha256(text.encode()).hexdigest(),'offset_convention':'zero-based Unicode code-point and UTF-8 byte offsets; end exclusive','groups':G,'text_spans':spans},ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and source_map.json with',len(G),'complete literal groups.')
