"""Apply root decisions made on the actually viewed second-reading crops."""
from pathlib import Path
import csv,json
R=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work')
p=R/'reports/151_scan009.json';d=json.loads(p.read_text())
tpath=R/'reports/151_scan009.tex';t=tpath.read_text()
first={r['box']:r['first'] for r in csv.DictReader((R/'second/151_scan009_comparison.tsv').open(),delimiter='\t')}
boxes={r['box']:[int(r[k]) for k in ('x0','y0','x1','y1')] for r in csv.DictReader((R/'second/151_scan009_boxes.tsv').open(),delimiter='\t')}
def replace(a,b):
 global t
 assert a in t,a
 t=t.replace(a,b)
def update(i,final,evidence,box,dc=True):
 c=next(c for c in d['changes'] if c['id']==i)
 c.update(final=final,evidence=evidence,crop=f'crops/151_scan009_second_{box}.png',box=boxes[box],differs_C=dc)
def under(term,label,tick=False):
 return r'\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=0pt] (t) {$'+term+r'$};\draw ([xshift=-2pt,yshift=-2pt]t.south west)--([xshift=-2pt,yshift=-5pt]t.south west)--([xshift=2pt,yshift=-5pt]t.south east)--([xshift=2pt,yshift=-1pt]t.south east);'+(r'\draw ([xshift=4pt,yshift=-5pt]t.south)--++(0,2.5pt);' if tick else '')+r'\node[anchor=north,inner sep=0pt] at ([yshift=-7pt]t.south) {$'+label+r'$};\end{tikzpicture}'
num=r'\begin{tikzpicture}[baseline=(n.base)]\node[inner sep=0pt] (n) at (0,0) {4};\draw (-.32,.15)..controls(-.4,-.2)and(-.2,-.43)..(.02,-.43)..controls(.3,-.42)and(.4,-.2)..(.38,.15);\end{tikzpicture}'
replace(r'\mspage{\textcircled{4}}',r'\mspage{'+num+'}')
u23=under(r'p_{12}\rho',r'p_{23}',True);u31=under(r'p_{12}\rho^2',r'p_{31}')
replace(r'\underbrace{p_{12}\rho}_{p_{23}}',u23);replace(r'\underbrace{p_{12}\rho^2}_{p_{31}}',u31)
frame=r'''\begin{tikzpicture}[baseline=(r.base)]
\node[inner sep=6pt] (r) {$\begin{gathered}\delta_0p_0(x)=1\\\sigma(x).x=1\\[.5em]p_{12}(z)p_{23}(z)p_{31}(z)=1\end{gathered}$};
\draw ([xshift=3pt,yshift=2pt]r.north west)--([xshift=-3pt,yshift=2pt]r.north east);
\draw ([yshift=-2pt]r.north west)--(r.south west)--(r.south east)--([yshift=-2pt]r.north east);
\end{tikzpicture}'''
oldframe=r'''\boxed{\begin{gathered}
\delta_0p_0(x)=1\\
\sigma(x).x=1\\[.5em]
p_{12}(z)p_{23}(z)p_{31}(z)=1
\end{gathered}}'''
replace(oldframe,frame)
u1=under(r'\delta_0p_0(x)',r'\substack{\Vert\\1}')
replace(r'\underbrace{\delta_0p_0(x)}_{\substack{\Vert\\1}}',u1)
insertion=r'''\begin{tikzpicture}[baseline=(w.base)]
\node[anchor=west,inner sep=0pt] (w) at (0,0) {qui ne};
\node[anchor=west,inner sep=0pt] at (-.15,.52) {\inserted{\unsure{sous|de} $\unsure{\mathcal G_3|\mathfrak S_3}$}};
\draw (-.15,-.12)..controls(-.16,.25)and(-.05,.3)..(.3,.3)--(1.58,.34)--(1.59,.43);
\end{tikzpicture}'''
replace(r'\inserted{sous $\unsure{\mathcal G_3|\mathfrak S_3}$} qui ne',insertion)
start=t.index(r'\diagram{');end=t.index(r'\[(x,y)\mapsto y\]',start)
diagram=r'''\diagram{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (-.6,0) {$\delta_1$};
\node (top) at (1.8,0) {$F\times F\times F$};
\node at (1.8,1.45) {$\sigma_1$};
\draw (1.53,.63)..controls(1.15,.9)and(1.72,1.37)..(2.13,1.16)..controls(2.6,.96)and(2.24,.68)..(2.05,.61);
\draw (1.53,.63)--(1.58,.68);\draw (2.05,.61)--(2.01,.74);
\draw[line width=.7pt] (1.58,-.42)..controls(1.52,-.3)and(1.56,-.95)..(1.58,-1.12);
\draw[line width=.7pt] (1.46,-1.01)--(1.58,-1.12)--(1.7,-1.02);
\node at (1.08,-.7) {$p_{12}$};
\draw[line width=.7pt] (2.14,-.37)..controls(2.03,-.25)and(2.08,-.93)..(2.13,-1.1);
\draw (2.13,-1.1)--(2.12,-.31)--(2.29,-.44);
\draw[line width=.7pt] (2,-.98)--(2.13,-1.1)--(2.28,-.99);
\node at (2.7,-.7) {$p_{13}$};
\draw (top.east)..controls(4.1,.24)and(6,.38)..(8.2,.4);
\draw (4.13,-.03)..controls(5.65,.37)and(6.9,.17)..(7.53,.18)--(7.48,.27);
\node at (6.5,-.9) {$\alpha\in E_1$};
\node at (-.2,-1.7) {$F_\alpha$};\node at (.7,-1.7) {$\subset$};
\node at (1.8,-1.7) {$F\times F$};
\draw (1.83,-2.08)--(1.86,-2.95);\draw (1.72,-2.82)--(1.86,-2.95)--(2,-2.83);
\node at (2.36,-2.45) {$\mathrm{pr}_0$};\node at (1.86,-3.25) {$F$};
\end{tikzpicture}}
'''
t=t[:start]+diagram+t[end:]
oldover=r'\overbrace{p_{12}^{-1}(\alpha)\cap p_{13}^{-1}(\alpha)}^{E_2(\alpha)\ni\delta_1(\alpha)=\delta_1\sigma(\alpha)}'
over=r'''\begin{tikzpicture}[baseline=(t.base)]
\node[inner sep=0pt] (t) {$p_{12}^{-1}(\alpha)\cap p_{13}^{-1}(\alpha)$};
\draw ([xshift=-1pt,yshift=2pt]t.north west)--([xshift=0pt,yshift=5pt]t.north west)--([xshift=0pt,yshift=6pt]t.north east)--([xshift=2pt,yshift=2pt]t.north east);
\node[anchor=south,inner sep=0pt] at ([xshift=10pt,yshift=8pt]t.north) {$E_2(\alpha)\ni\delta_1(\alpha)=\delta_1\sigma(\alpha)$};
\end{tikzpicture}'''
replace(oldover,over)
replace('les pts fixes',r'les p\textsuperscript{ts} fixes')
replace(r'\Longleftrightarrow\sigma x=\alpha',r'\Longleftrightarrow\overset{!}{\sigma}x=\alpha')
update('P009-001',"ACADEMIE D'AIX-MARSEILLE / INSPECTION ACADEMIQUE / DE VAUCLUSE; "+r'\mspage{'+num+'}', 'The printed letterhead is unchanged. The dark 4 has a diagonal, upright and crossbar. Its large enclosing cup rises on both sides but leaves the entire top open; a closed circle would add ink absent from the crop.', 'B002')
update('P009-002',u23+r'\delta_1(x)','The p23-labelled line spans p12 rho only. It is a nearly straight lower bracket with upward ends and a small upward interior tick, not a downward-cusped brace. The delta stem begins beyond its right end.','B003')
update('P009-003',u31+r'\delta_1(x)','The p31-labelled line spans p12 rho squared only. Its lower bar is flat with upward ends and has no central brace cusp. Delta_1 lies beyond the right end.','B003')
update('P009-007',frame,'The three relations are surrounded by a separate top stroke and a connected left-bottom-right course. Both upper corners have visible white gaps. The multiplication point is low; all three final factors and their indices agree between the two readings.','B005')
update('P009-008',u1,'The factor has a flat lower bar with two short upward ends, without a central cusp. Under it two upright strokes stand above a separate numeral 1; neither their orientation nor their vertical stacking is an equals sign beside 1.','B006')
update('P009-012',insertion,'The short word above the gap after orbite is crossed/overlapped by the descender and foot of the canceled word above. Its small initial bends favor sous, but do not independently establish all four letters or exclude de. The indexed capital remains G/S. The continuous leader curls upward before qui and passes above qui ne, ending in a right upturn; qui ne rencontre pas stays live.','B007')
next(c for c in d['changes'] if c['id']=='P009-012')['confidence']='low'
c=next(c for c in d['changes'] if c['id']=='P009-010');c['evidence']='The curved attachment rises before qui and passes above qui ne beneath the insertion, without crossing rencontre or pas. The inserted short word is now explicitly uncertain sous/de; this does not change the live state of the clause.'
update('P009-015',diagram.strip(),'The isolated delta_1, loop sigma_1, three F objects, F_alpha inclusion, pr_0 and alpha in E1 are present. Both p12 and p13 have complete lower heads. At the upper end of p13 a retraced narrow loop and one thin descending-right spur are visible, not a full second arrowhead. The long upper course touches the final F. The lower course is detached at its left and ends in only an upper wing at the right. The loop above has a bent single terminal wing. These partial ends and gaps are drawn separately rather than completed into standard arrows.','B008')
update('P009-019',over,'A straight bracket above both inverse-image terms has downturned ends and no central brace cusp. The whole E2(alpha) contains delta1(alpha) equals delta1 sigma(alpha) annotation is above it, shifted toward its right half. The two upright legs and broad bar of the initial Pi remain the capital reading.','B010')
for ident,place,C,H,final,evidence,kind,conf in [
 ('P009-A01','Raised abbreviation before fixes','pts','pts',r'p\textsuperscript{ts}','The t and s are compact and raised relative to the p body and descender. The abbreviation is preserved as written, without expansion.','insertion or placement','medium'),
 ('P009-A02','Small annotation above sigma in the final equivalence',r'\Longleftrightarrow\sigma x=\alpha',r'\iff\sigma x=\alpha',r'\Longleftrightarrow\overset{!}{\sigma}x=\alpha','A short dark upright and a distinct dark dot immediately below it stand in the gap above this sigma. They form an exclamation mark; they are separate from the sigma in each adjacent line.','omission','high')]:
 d['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=evidence,confidence=conf,kind=kind,crop='crops/151_scan009_second_B014.png',box=boxes['B014'],differs_C=True,differs_H=True,marked_in_H='no',consequential=''))
d['doubts'].append(dict(place='Interlinear word after par orbite',reading='sous',alternatives=['de'],confidence='low',reason='The descender/foot of the cancellation above overlies the middle of the inserted word; the small surviving bends do not settle all its letters. Second-reading crop B007.'))
d['notes'][0]=d['notes'][0].replace('dark circled 4','dark 4 in an open-topped cup')
d['notes'].append('The independent audit changed graphic readings at B002/B003/B005/B006/B008/B010: the page-number cup is open, the annotation bars are flat, the enclosure has two upper gaps, and the diagram keeps its partial ends and detached course. It also records the insertion leader and sous/de uncertainty, the raised ts abbreviation, and a dark stem-plus-dot exclamation above sigma in the final equivalence (B014). These are readings of ink, not mathematical emendations.')
for v in d['inventory']:
 if v['element']=='Author page number':v['first_words_or_objects']='4 in an open-topped cup'
d['inventory'].append(dict(element='Exclamation above sigma in the final equivalence',kind='insertion',position='lower prose implication, above sigma',first_words_or_objects='!',transcribed='yes',hand='main mathematical hand'))
manual={
 'B001':dict(changed=False,evidence='The three printed uppercase lines and the long then short rules agree. Centering, boldface and rule lengths in the second encoding do not change the reading.'),
 'B002':dict(changed=True,final=r'\mspage{'+num+'}',evidence='A dark 4 stands in a broad cup open across its entire top. The closed text circle of the first reading adds an absent upper course.'),
 'B003':dict(changed=True,final=first['B003'].replace(r'\underbrace{p_{12}\rho}_{p_{23}}',u23).replace(r'\underbrace{p_{12}\rho^2}_{p_{31}}',u31),evidence='Both annotation bars are flat with upward ends, not central-cusped braces. The upper bar has one short interior upward tick. Both stop before delta_1; formula letters and indices agree.'),
 'B004':dict(changed=False,evidence='The rounded indexed capital with an inward return remains compatible with the run\'s G/S homography. The p descender and round lower index support p_0, despite overlap; no additional p_0 doubt is needed. The rest agrees, with margin/line wrapping only.'),
 'B005':dict(changed=True,final=frame,evidence='Both upper corners contain white gaps between the separate top stroke and the connected other three edges. All formula glyphs agree.'),
 'B006':dict(changed=True,final=r'\sigma(x)'+u1+'x=1',evidence='The lower annotation is a flat bar with upward ends. The double upright and 1 below it are separate stacked text signs; the original brace cusp is absent.'),
 'B007':dict(changed=True,final=first['B007'].replace(r'\inserted{sous $\unsure{\mathcal G_3|\mathfrak S_3}$} qui ne',insertion),evidence='The struck par/pour remains unresolved: middle strokes lie in the strike. The inserted short word is overlapped by the canceled p descender/foot, so neither confident sous nor confident de is justified; sous/de is marked. Its leader rises before qui and passes above qui ne. The indexed group remains G/S.'),
 'B008':dict(changed=True,final=diagram.strip()+first['B009'],evidence='Both vertical lower heads are complete. The p13 upper end has a narrow retraced loop and one thin right spur, not a complete upward head. The long lower right course starts detached and ends with one upper wing; the upper course starts on F and is blunt. These ends, loop and gap are now drawn explicitly. The lower coordinate formulas remain (also adjudicated in B009).'),
 'B009':dict(changed=False,evidence='The tiny base below the multiplication cross is a curved low hook rather than a clear F stem/bar; y/x stays doubtful. The high mark after the next x is crossed, leaving prime/plus open. No opening parenthesis precedes that x. The canceled right-hand y retains its fork and sweeping descender, so its letter is readable. Mapsto length and gathered layout alone do not change the reading.'),
 'B010':dict(changed=True,final=first['B010'].replace(oldover,over),evidence='The overbar is straight with downturned ends, without a central cusp; the annotation lies above it. The initial Pi has a broad bar and two essentially upright legs, supporting the capital retained across the page; it is not changed to the blind reader\'s lowercase pi.'),
 'B011':dict(changed=False,evidence='The title ends in c+h, a/m joins, a p descender and terminal s: champs. The small dense cancellation has remnants consistent with tél but not all letters are secure, so the existing doubt remains. All eight digits agree; grouping spaces do not change the number. The box crosses descenders of petit/coq and is not cancellation of their words.'),
 'B012':dict(changed=False,evidence='The last letter has a long sweeping descender like the first y; the middle x has the shorter left leg and right return. Both commas are distinct. The reading y,x,y is retained.'),
 'B014':dict(changed=True,final=first['B014'].replace('les pts fixes',r'les p\textsuperscript{ts} fixes').replace(r'\Longleftrightarrow\sigma x=\alpha',r'\Longleftrightarrow\overset{!}{\sigma}x=\alpha'),evidence='The compact ts is raised above the p body. A dark upright plus a separate lower dot above the later sigma is an exclamation mark. The word dans has a looped d followed by the joined low strokes; it remains live. Each cancellation still obscures some letters, and the tall initial loop favors the existing faut candidate over secure donc. The first cancellation is a small word group, not three independently distinguishable unreadable words.'),
 'B015':dict(changed=False,evidence='The verb retains a descending j and joined ou/e despite its initial retrace, followed by le rôle de. The first delta index has an angled head and broad right foot, distinct from the simple upright 1 of the next delta. Hence joue and delta_2 remain secure; underline macro choice has no lexical effect.'),
 'B016':dict(changed=False,evidence='The pale two-loop 8 agrees; the margin wrapper is already present in the page and does not change the reading.')}
(R/'reviews/151_scan009_manual.json').write_text(json.dumps(manual,ensure_ascii=False,indent=2)+'\n')
tpath.write_text(t);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Applied 009 crop adjudications; immutable first/second TSVs untouched.')
