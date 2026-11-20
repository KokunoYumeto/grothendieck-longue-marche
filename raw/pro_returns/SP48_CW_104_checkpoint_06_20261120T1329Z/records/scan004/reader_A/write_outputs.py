from pathlib import Path
import json
from datetime import datetime, timezone
out=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan004/reader_A')
src=Path('/workspace/scratch/7178efd1cfac/reader_inputs/scan004/C.tex')
s=src.read_text()
old=r'''\mathrm{Ob}\,C_{\unsure{4|1}}\arrow[rr,line width=.8pt]\arrow[rr,bend left=7,dash,"\deleted{\unsure{\leftarrow|{-}}}" description,pos=.52] \& \& \mathrm{Fl}_0(\unsure{C_1|C_n})\\
{\bigl(\mathrm{Fl}\,C_1\times\mathrm{Ob}\,C_2\bigr)}
 \arrow[u,shift left=.55ex]\arrow[u,shift right=.55ex]
 \& {\deleted{\unsure{\amalg}}\;\deleted{\unsure{\mathrm{Fl}_0 C_1\times}}\;
 \inserted{\unsure{\mathbb F|F}\mathrm l_0(C_1)\times\mathrm{Ob}\,C_2}} \&'''
new=r'''\mathrm{Ob}\,C_4
 \arrow[rr,phantom,"{\tikz[baseline=-.4ex,x=.008cm,y=-.008cm,line cap=round,line join=round]{
  \draw[line width=.8pt] (606,136)--(855,170)--(1027,176);
  \draw[line width=.35pt] (611,163)..controls(650,135)and(850,125)..(1023,174)
   (609,137)--(659,146)--(996,171) (607,136)--(617,145)
   (839,165)--(864,184)
   (844,169)..controls(903,188)and(974,188)..(1021,178)
   (998,151)--(1026,174)--(978,193)
   (994,162)--(1025,173)--(964,203);
  \fill (999,162)--(1031,172)--(1008,187)--(1013,174)--cycle;
 }}" description,pos=.54] \& \& \mathrm{Fl}_0(\unsure{C_1|C_n})\\
{\bigl(\mathrm{Fl}\,C_1\times\mathrm{Ob}\,C_2\bigr)}
 \arrow[u,shift left=.55ex]\arrow[u,shift right=.55ex]
 \& {\begin{aligned}
 &\deleted{\amalg}\;\deleted{\unsure{\mathrm{Fl}_0 C_1\times}}\\[-.3ex]
 &\qquad\inserted{\mathbb F\mathrm l_0(C_1)\times\mathrm{Ob}\,C_2}
 \end{aligned}} \&'''
assert old in s
s=s.replace(old,new)
s=s.replace(r'\end{tikzcd}}',r'''\end{tikzcd}}
% The heavy arrow certainly points right. Its multiple shafts and left spur
% are traced without asserting a separately cancelled earlier left arrow.''',1)
s=s.replace(r'\mathrm{Fl}(C_2)\times\deleted{\unsure{\mathrm{Fl}}}\mathrm{Ob}\,C_3',r'\mathbb F\mathrm l(C_2)\times\deleted{\unsure{F|\mathrm{Fl}}}\mathrm{Ob}\,C_3')
s=s.replace(r'(1304,286)--(1293,435) (1363,279)--(1355,435)',r'(1304,286)--(1293,435) (1363,279)--(1355,435)--(1351,417)')
s=s.replace(r'(1497,288)..controls(1505,316)and(1495,357)..(1490,432) (1598,263)--(1572,441);',r'''(1497,288)..controls(1505,316)and(1495,357)..(1490,432)--(1485,424)
 (1594,270)..controls(1597,261)and(1599,264)..(1598,267)--(1572,441);
\draw[line width=.3pt] (1298,365)--(1435,281)
 (1363,292)..controls(1400,288)and(1460,292)..(1493,290);''')
s=s.replace(r'\fill (1305,287) circle[radius=3.8];',r'''\fill (1305,287) circle[radius=3.8] (1367,283) circle[radius=3];
\draw (1718,101)--(1724,101);
\fill (1353,439) circle[radius=1.1] (1446,313) circle[radius=1.0];
% The detached dash and two small points are traced without assigning meaning.''')
s=s.replace(r'\,\unsure{<|\times}\,\mathrm{Fl}\,\unsure{l_3|C_3}',r'\,<\,\mathrm{Fl}\,l_3')
s=s.replace(r'''\mathbb F_n\mathrel{\unsure{=|2}}\mathbb F\mathrm l\,C_1
\times\mathrm{Fl}\,C_2''',r'''\mathbb F_n\mathrel{\unsure{2|=}}\mathbb F\mathrm l.C_1
<\mathrm{Fl}\,C_2''')
s=s.replace(r'\foreach \x/\y in {1539/818,1683/803,1681/948,1535/957}{\draw (\x,\y) circle[radius=4.2];}',r'''\fill (1531,815)--(1538,813)--(1545,808)--(1551,812)--(1551,819)
 --(1542,825)--(1530,824)--cycle;
\fill (1680,803) ellipse[x radius=7,y radius=5.5];
\fill (1680,948) ellipse[x radius=6.5,y radius=5.5];
\fill (1536,956) ellipse[x radius=6.7,y radius=7.4];
\fill[white] (1546,812) circle[radius=1.5]
 (1680,803.5) circle[radius=1.9] (1679.5,946.6) circle[radius=1.7]
 (1537.1,954.7) circle[radius=1.25];
\fill[white] (1533.2,960.8) ellipse[x radius=1.8,y radius=2.7];
\fill (1542,927)--(1548,929)--(1548,932)--(1542,932)--cycle;''')
old=r'''\tikz[baseline=(markletters.base)]{
 \node[inner sep=0pt] (markletters) {\(\unsure{X_0|X_{\varnothing}}\qquad\unsure{X_1}\)};
 \draw[line width=.32pt] ([xshift=.29em,yshift=-.28em]markletters.west)
 ..controls ([xshift=1.5em,yshift=-.75em]markletters.west) and ([xshift=-1.65em,yshift=.40em]markletters.east)
 ..([xshift=-.63em,yshift=.06em]markletters.east);}'''
new=r'''\tikz[baseline=(markletters.base)]{
 \node[inner sep=0pt] (markletters) {\(\unsure{X_0|X_{\varnothing}}\qquad X_1\)};
 \draw[line width=.32pt] ([xshift=.75em,yshift=-.4em]markletters.west)
 ..controls ([xshift=1.4em,yshift=.5em]markletters.west) and ([xshift=-1.05em,yshift=.6em]markletters.east)
 ..([xshift=-1em,yshift=-.05em]markletters.east)
 ..controls ([xshift=-.95em,yshift=-.6em]markletters.east) and ([xshift=-.5em,yshift=-.5em]markletters.east)
 ..([xshift=-.1em,yshift=0em]markletters.east)
 ..controls ([xshift=.1em,yshift=.2em]markletters.east) and ([xshift=.15em,yshift=.2em]markletters.east)
 ..([xshift=.2em,yshift=-.1em]markletters.east);
 \draw[line width=.25pt] ([xshift=.35em,yshift=.02em]markletters.west)
 --([xshift=.72em,yshift=.5em]markletters.west);
 \draw[line width=.4pt] ([xshift=-.8em,yshift=.95em]markletters.east)
 --([xshift=-.78em,yshift=.85em]markletters.east);}
% The connecting trace and detached upper tick are not assigned an arrow
% or cancellation function. The crossed first index remains uncertain.'''
assert old in s
s=s.replace(old,new)
s=s.replace(r'\deleted{O}\unsure{\dot F|\hat F}\subset F',r'\deleted{O}\unsure{\hat F|\dot F}\subset\mathbb F')
s=s.replace(r'''\mathbb F_1\times\text{---}\ \times\mathbb F_n\times(\unsure{-}\,?)''',r'''\mathbb F_1\times\text{---}\
\mathbin{\tikz[baseline=(tickcross.base)]{
 \node[inner sep=0pt] (tickcross) {\(\times\)};
 \draw[line width=.3pt] ([xshift=.12em,yshift=.36em]tickcross.north)
 ..controls ([xshift=.2em,yshift=.23em]tickcross.north) and ([xshift=.18em,yshift=.13em]tickcross.north)
 ..([xshift=.08em,yshift=.08em]tickcross.north);}}
\mathbb F_n
\mathbin{\tikz[baseline=(dotcross.base)]{
 \node[inner sep=0pt] (dotcross) {\(\times\)};
 \fill ([xshift=.12em,yshift=.12em]dotcross.north east) circle[radius=.45pt];}}
(-\,?)
% Detached curved tick above the second cross and dot above-right of the
% third cross are reproduced literally; their linguistic status is unknown.''')
s=s.replace(r'\unsure{F_n|F_3}',r'\unsure{F_n|F_3|F_{n+1}}')
s=s.replace(r'(F\times I)\mathbin{\amalg}_{\deleted{O}\dot F\times I}\deleted{O}\dot F',r'(F\times I)\mathbin{\amalg}_{\deleted{O}\dot F\times I}\deleted{O}\hat F')
(out/'reading.tex').write_text(s)
manifest=json.loads((out/'crop_manifest.json').read_text())
for c in manifest['crops']:
 c['viewed']=True
 c['view_count']=1
manifest['view_order']=[c['path'] for c in manifest['crops']]
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex; recorded all 14 crop views.')
