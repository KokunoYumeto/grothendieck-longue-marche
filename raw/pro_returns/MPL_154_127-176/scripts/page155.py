from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{155}
{\ttfamily
* \unsure{LE NIVEAU DU SYSTEME MVS/SP 1.1} SERA MIS EN SERVICE SUR LE *\\
* 3081 LE 21 AOUT 1982. *\\
*\hfill *\\
******************************************************************}
'''
s+=start()+paths('p,opacity=.4','1.8,2.97 4.87,3.03 5.71,2.26 6.14,3.17 8.38,3.26;1.79,3.2 3.64,3.32 4.39,4.33 5.05,3.4 8.38,3.44;6.25,1.83 6.89,1.56 7.65,1.92 8.25,2.11;9.83,2.22 10.19,2.07 10.41,1.63;10.14,3.11 12.17,3.16 12.64,2.84;10.14,3.35 12.25,3.47 13.44,3.36 14.48,4.2 15.27,3.47 18.29,3.39;13.46,2.8 14.03,3.17 15.05,3.18 15.63,2.52 16.15,3.21 18.28,3.17;19.74,3.39 20.77,3.41 21.43,2.92 22.71,2.84 23.81,3.39 25.9,3.36 26.77,3.99 27.6,3.83;19.74,3.66 20.93,3.7 21.6,4.36 23.4,4.41 24.16,3.7 26.35,3.76 26.83,4.59 27.62,4.48')+end()
s+=r'''balayages élémentaires de positions relatives
'''
s+=start()
# I_1
s+=paths('w','2.87,7.0 4.16,6.92 4.4,6.48 4.83,6.15 5.18,6.38 5.49,6.91 6.99,6.91;2.88,7.22 5.02,7.11 7.29,7.1')+path('green!40!black,line width=1.8pt','2.98,7.11 5.0,7.04 7.22,7.04')
s+=paths('p','4.6,5.69 4.83,6.15 5.62,7.79;5.07,5.35 4.83,6.15 4.09,7.79;4.82,5.46 4.83,6.15 4.97,7.79;4.58,6.67 4.98,6.48;4.48,6.82 5.08,6.63;4.4,6.98 5.18,6.79')
s+=paths('k,dashed','3.65,6.32 3.67,7.75;6.19,6.19 6.22,7.82')+dots('w','4.83,6.15','.08')+labels([('5.06,6.03','a'),('7.2,5.39',r'(I_1)'),('7.25,6.79','2'),('7.43,7.26','1')])
s+=path('k','3.99,8.56 4.06,8.66 4.7,8.65 4.94,8.81 5.16,8.65 5.93,8.6 6.16,8.51')
s+=r'\node[anchor=north west,align=left,text width=4.7cm] at (3.95,8.98) {pas d\textquotesingle autres sommets de $\Sigma$ ici que $a$, ni d\textquotesingle autres traces des droites de $\Sigma$ que \deleted{\unsure{celles}} marquées (passant par $a$)};'+'\n'
s+=r'\node[anchor=north west,align=left,text width=4.7cm] at (3.25,14.25) {\uline{assymétrique}, la position 1, n\textquotesingle est \uline{pas} \deleted{\unsure{jamais}} p.r. critique};'+'\n'
# I_2
s+=paths('w','9.32,6.88 10.43,6.81 11.48,6.24 13.76,6.08 14.45,6.25 15.32,6.85 16.38,6.9;9.32,7.25 10.38,7.25 11.42,7.64 12.48,7.67 14.46,7.64 15.32,7.2 16.38,7.18')+path('green!40!black,line width=1.8pt','9.37,7.05 10.4,6.98 13.0,7.05 16.35,7.08')
s+=paths('p','10.76,5.5 12.48,7.67 13.0,8.3;11.77,5.47 12.48,7.67 12.12,8.68;12.89,5.6 12.48,7.67 11.62,8.45;13.11,7.97 13.76,6.08 14.01,5.32;13.33,5.61 13.76,6.08 15.32,8.6;13.72,5.49 13.76,6.08 13.93,7.97;14.22,5.55 13.76,6.08 12.48,7.67')
s+=paths('p','12.98,6.87 14.17,6.73;13.1,6.74 14.06,6.6;13.23,6.59 13.95,6.46;12.0,7.14 12.77,7.05;12.14,7.31 12.7,7.19;12.29,7.48 12.58,7.37')
s+=path('w,<->,line width=1.7pt','12.6,7.52 13.62,6.23')+paths('k,dashed','9.98,5.82 9.92,8.13;16.08,5.87 15.87,8.57')+dots('w','13.76,6.08 12.48,7.67','.09')+labels([('14.23,5.98','a'),('12.17,7.86','b'),('13.91,4.96',r'(I_2)'),('16.58,6.94','2'),('16.67,7.39','1')])
s+=path('k','10.73,9.2 10.84,9.3 12.34,9.3 12.85,9.56 13.12,9.39 15.67,9.29 15.83,9.23')
s+=r'\node[anchor=north west,align=left,text width=4.8cm] at (10.96,9.7) {pas d\textquotesingle autres sommets de $\Sigma$ que $a$ et $b$, ni d\textquotesingle autres traces des droites de $\Sigma$ que celles marquées (passant par $a,b$)};'+'\n'
s+=r'\node[anchor=north west,align=left,text width=4.8cm] at (11.56,14.2) {\uline{symétrique}, la position 1 est critique ssi la position 2 l\textquotesingle est};'+'\n'
# I_3
s+=paths('w','18.2,7.01 19.21,6.92 19.67,6.22 21.24,5.76 25.06,5.89 25.75,6.04 26.65,6.8 27.43,6.83;18.16,7.29 19.18,7.27 19.83,7.9 21.1,8.04 23.58,7.81 26.29,7.79 26.88,7.2 27.52,7.18')+path('green!40!black,line width=1.8pt','18.32,7.14 21.7,7.01 25.0,6.96 27.44,6.96')
s+=paths('p','20.79,5.47 21.24,5.76 23.58,7.81 24.1,8.21;21.58,5.42 21.24,5.76 19.23,8.22;21.26,5.42 21.24,5.76 21.7,8.21;21.43,5.43 21.24,5.76 19.92,8.7;22.51,5.2 23.58,7.81 24.02,9.26;24.0,4.9 23.58,7.81 23.35,9.26;24.5,5.23 25.06,5.89 26.94,8.48;25.19,5.3 25.06,5.89 24.47,8.41;25.52,5.32 25.06,5.89 23.58,7.81 22.98,8.51;24.99,5.29 25.06,5.89 25.7,8.17')
s+=paths('p','20.26,6.82 22.3,6.58;20.43,6.64 22.09,6.4;20.61,6.43 21.83,6.24;20.85,6.18 21.57,6.05;22.84,7.07 24.0,6.93;23.0,7.25 23.86,7.1;23.21,7.44 23.74,7.32;24.44,6.76 25.59,6.59;24.59,6.57 25.48,6.42;24.77,6.34 25.3,6.21')
s+=path('w,->','23.38,7.6 21.4,5.93')+path('w,<->','23.71,7.65 24.86,6.13')+paths('k,dashed','18.62,6.23 18.62,8.43;27.4,5.91 27.34,8.5')+dots('w','21.24,5.76 25.06,5.89 23.58,7.81','.09')+labels([('21.75,5.58','a'),('25.66,5.66','b'),('23.26,7.98','c'),('21.57,4.57',r'(I_3)')])
s+=path('k','19.1,9.42 19.52,9.55 22.58,9.5 22.94,9.73 23.0,9.61 25.5,9.42 27.0,9.16 27.2,9.03')
s+=r'\node[anchor=north west,align=left,text width=5.9cm] at (19.64,9.97) {pas d\textquotesingle autres sommets de $\Sigma$ ici que $a,b,c$, ni d\textquotesingle autres traces de droites de $\Sigma$ que celles marquées (passant par $a,b,c$)};'+'\n'
s+=r'\node[anchor=north west,align=left,text width=5.8cm] at (20.44,14.37) {\uline{assymétrique}, néanmoins 1 est critique ssi 2 l\textquotesingle est};'+'\n'
s+=path('k','14.27,17.01 15.26,17.19 18.65,17.16 19.34,17.38 19.5,17.55 19.73,17.25 21.85,16.99 23.99,16.61')
s+=r'\node[anchor=north west,align=left,text width=5cm] at (17.1,17.76) {balayages élémentaires de p.r. critiques \unsure{l\textquotesingle une} \unsure{autre}};'+'\n'
# I_n, n=7, all seven vertices and pencil fans.
s+=paths('w','9.65,20.41 10.82,20.34 11.29,19.82 12.36,19.62 14.47,19.55 16.81,19.53 18.75,19.77 19.55,20.26 20.59,20.33;9.72,20.65 10.75,20.66 11.21,21.04 13.43,21.01 15.6,21.2 17.94,21.08 19.35,21.09 20.05,20.64 20.8,20.66')+path('green!40!black,line width=1.8pt','9.77,20.55 13.59,20.48 16.1,20.53 21.26,20.48')+path('k,dashed','10.36,19.72 10.36,21.55')
verts=[(12.36,19.62),(13.43,21.01),(14.47,19.55),(15.6,21.2),(16.81,19.53),(17.94,21.08),(18.75,19.77)]
s+=path('p,line width=1.3pt',' '.join(f'{x},{y}' for x,y in verts),False)
for x,y in verts:
 for dx in [-.43,-.13,.18,.52]:
  s+=path('p',f'{x-dx*.4},{y-.5} {x},{y} {x+dx},{y+1.9}' if y<20 else f'{x-dx},{y-2.1} {x},{y} {x+dx*.3},{y+.5}')
 for k in range(3):
  yy=y+(.34+.16*k)*(1 if y<20 else -1)
  s+=path('p',f'{x-.17-.12*k},{yy} {x+.2+.11*k},{yy-.1}',False)
s+=dots('w',' '.join(f'{x},{y}' for x,y in verts),'.075')+labels([('23.54,20.08',r'(I_n)'),('26.36,20.23',r'(n=7)')])
s+=r'\node[anchor=west] at (23.0,21.18) {Cas \unsure{assymétrique} cas $n$ impair};'+'\n'
s+=end()+r'\margin{154}'+'\n'
(root/'pages/MPL_154_127-176_154_scan155.tex').write_text(s)
commit(155,[('text','printed upper right through paper','LE NIVEAU DU SYSTEME; 3081 LE 21 AOUT 1982'),('drawing','faint top strip','three faint swept strips'),('text','upper left title','balayages élémentaires de positions relatives'),('drawing','left column I1','a; 1; 2; pencil fan; brace'),('text','under I1','pas d’autres sommets; assymétrique; position1'),('deletion','under I1','celles; jamais'),('drawing','middle column I2','a; b; 1; 2; opposite arrows; brace'),('text','under I2','pas d’autres sommets; symétrique'),('drawing','right column I3','a; b; c; arrows and brace'),('text','under I3','pas d’autres sommets; assymétrique; néanmoins'),('drawing','middle lower','brace joining I2 and I3 captions'),('text','above bottom figure','balayages élémentaires de p.r. critiques'),('drawing','bottom','I_n; n=7; seven vertices and transverse fans'),('text','bottom right','Cas assymétrique cas n impair'),('margin note','bottom left','154')],sheet_kind='reused_typed',observations='Whole, both halves, mirrored enlarged printed heading and enlarged lower caption read visually. All four sweep drawings, their braces and seven bottom vertices reproduced. The source writes assymétrique with apparent doubled s, retained with doubt on bottom pencil occurrence. Lower joining-brace caption has uncertain final words. Very faint upper reverse marks reproduced as separate strokes. Printed version and initial words remain doubtful.')
