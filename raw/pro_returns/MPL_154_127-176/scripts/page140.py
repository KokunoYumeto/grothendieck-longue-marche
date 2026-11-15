from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{140}
\unsure{1} sommet\\
1 face\\
2 arêtes\\
\unsure{4} repères, correspondent\\
aux rives des arêtes $a,b$

\deleted{$\sigma_0,\ \unsure{\sigma_1}\ \unsure{\hat a}$}

$\sigma_0=\sigma_2$ échangent $a^+,a^-$ et $b^+,b^-$\\
$\sigma_1$ échange \deleted{$\unsure{a^+\text{ et }a^-}$} $a^+$ et $b^+$, $a^-$ et $b^-$\\
$\sigma$ échange $a^+$ et $b^-$, $b^+$ et $a^-$

\[\underbrace{\sigma_1,\sigma},\underbrace{\sigma_2,\sigma_0}_{\substack{\Vert\\\sigma'}}\]
subdivision barycentrique

$\sigma_0=\sigma_2$ soit $\sigma'$, commute à $\sigma$\\
$\sigma_1=\sigma\sigma'$,\\
\deleted{$\unsure{\sigma=\sigma_1\sigma'}$}

\[\underbrace{\sigma\sigma'}_{\sigma_1},\underbrace{\sigma}_{\sigma},
\underbrace{\underbrace{\sigma'}_{\sigma_2},\underbrace{\sigma'}_{\sigma_0}}\]
\[\underbrace{\sigma\sigma'}_{\sigma'_0},\underbrace{\sigma'}_{\sigma'_1},\underbrace{\sigma}_{\sigma'_2}\]
'''
s+=start()+comment('Upper-left segments and overdrawn segment.')
s+=path('k,line width=2pt','3.0,1.15 5.3,1.15',False)+dots('k','4.25,1.15','.08')
s+=labels([('2.75,1.37','-1'),('5.5,1.37','+1'),('4.27,1.4','0'),('3.5,.9','a^+'),('4.85,.9','b^+'),('3.5,1.55','a^-'),('4.85,1.55','b^-')])
s+=paths('k','3.03,2.22 4.7,2.21 5.88,2.27 6.84,2.36;2.9,2.42 3.55,2.1 3.25,2.59 4.77,2.07 4.05,2.58 5.05,2.21 4.82,2.67 5.24,2.61',False)
s+=dots('k','3.27,2.22 4.7,2.22 4.23,2.45 5.86,2.28','.07')
s+=labels([('4.2,1.97','a^+'),('5.3,1.97','b^+'),('5.4,2.51','b^-'),('6,2.5',r'\unsure{-1}')])
s+=paths('k,->','2.1,1.98 2.8,1.95;4.3,3.22 5.0,3.19',False)
s+=comment('Upper pencil globes.')
s+=path('p','12.35,6.9 13.1,4.55 15.0,3.1 17.4,3.05 19.2,4.5 20.1,7.1 17.67,8.18 15.93,8.5 13.92,8.46',close=True)
s+=paths('p','13.92,8.46 14.2,5.6 15.83,3.56 17.0,5.0 17.67,8.18;15.83,3.56 15.57,6.1 15.93,8.5;17.39,3.17 17.45,5.5 17.67,8.18;17.39,3.17 18.8,3.15 21.15,3.1;17.39,3.17 18.9,4.3 21.15,3.1;21.15,3.1 20.0,4.5 19.75,6.4 20.75,8.1 23.0,8.6 25.1,8.35 27.1,7.4 27.35,5.6 26.0,3.7 24.0,2.9 21.15,3.1;24.0,2.9 23.1,5.0 23.0,8.6;24.0,2.9 25.5,3.4 26.3,6.4 25.5,7.7 23.0,8.6')
s+=dots('p','13.92,8.46 15.83,3.56 15.93,8.5 17.39,3.17 17.67,8.18 21.55,6.45 24.0,2.9 26.3,6.4 23.0,8.6')
s+=labels([('18.9,3.12',r'\unsure{0}'),('11.25,8.45',r'\sigma_1'),('21.1,6.45','-1'),('26.5,6.4','+1'),('23.07,8.88','0')])
s+=comment('Large left ink ellipse with pencil construction.')
s+=path('p','2.55,11.35 3.0,9.35 4.05,7.7 5.9,6.98 7.9,8.2 9.55,11.14 8.6,12.35 5.88,12.88 3.5,12.35',close=True)
s+=path('k,line width=2.1pt','2.56,11.36 3.7,12.4 5.88,12.88 8.4,12.45 9.55,11.14')
s+=path('k,line width=2.1pt,dashed','2.56,11.36 2.6,10.55 4.1,9.62 6.0,9.4 8.7,9.55 9.55,10.45 9.55,11.14')
s+=path('k,line width=2.1pt','5.9,6.98 5.74,8.2 5.72,10.6 5.88,12.88')
s+=path('k,line width=2pt,dashed','5.9,6.98 6.12,8.0 6.0,9.4')
s+=dots('k','2.56,11.36 9.55,11.14 5.88,12.88 6.0,9.4','.07')
s+=labels([('2.1,11.82','-1'),('9.9,11.35','+1'),('5.9,13.15','0'),('6.25,9.1',r'\infty')])
s+=comment('Faint lower-left globe.')
s+=labels([('5.1,13.8',r'\unsure{p\ \text{nouveau}}'),('6.2,14.22','0'),('6.0,20.18',r'\unsure{0|\infty}')])
s+=paths('p','6.0,14.35 3.4,14.85 2.4,16.6 2.7,18.4 4.0,19.7 6.0,20.18 8.1,19.5 8.95,17.0 8.5,15.2 6.0,14.35;6.0,14.35 5.0,15.3 4.94,17.6 5.04,19.4 6.0,20.18;6.0,14.35 4.2,15.5 3.9,17.6 4.5,19.35 6.0,20.18;6.0,14.35 3.7,15.4 2.95,17.65 3.35,19.0 6.0,20.18;6.0,14.35 7.5,15.4 8.1,17.0 7.65,19.0 6.0,20.18;2.5,17.0 4.0,15.15 6.0,14.35 8.0,15.0 8.9,16.0')
s+=comment('Lower central oval with dashed meridian and faint surrounding constructions.')
s+=paths('p','12.5,11.6 10.2,12.8 9.4,15.0 10.2,17.0 12.4,17.99 14.7,16.7 15.5,14.5 14.3,12.5 12.5,11.6;12.5,11.6 10.5,12.5 9.6,14.0 9.6,15.8 10.8,17.6 12.4,17.99;10.4,15.4 9.4,14.8 10.0,14.2 12.0,14.0 14.0,14.5 15.3,15.0 14.5,15.34;12.5,11.6 12.75,13.0 12.7,14.3')
s+=paths('k,line width=2.2pt','10.4,15.4 10.55,13.95 11.2,12.5 12.5,11.6 13.8,12.4 14.4,13.8 14.5,15.34;14.5,15.34 14.0,16.7 12.4,17.99 11.1,17.5 10.5,16.5 10.4,15.4')
s+=path('k,line width=2.1pt,dashed','12.5,11.6 12.95,12.5 13.05,14.8 12.95,16.5 12.4,17.99')
s+=dots('k','10.4,15.4 14.5,15.34 12.4,17.99','.065')
s+=labels([('12.5,11.35','0'),('12.4,18.25',r'\infty'),('10.2,15.6',r'\unsure{+1}'),('14.85,15.55','-1')])
s+=end()+r'\margin{139}'+'\n'
(root/'pages/MPL_154_127-176_154_scan140.tex').write_text(s)
commit(140,[('text','upper centre','1 sommet; 1 face; 2 arêtes; 4 repères'),('drawing','upper left','segment a+ b+ a− b−; overdrawn segment; arrows'),('deletion','upper left below segments','σ0, σ1, â'),('text','upper middle','σ0=σ2 échangent; σ1 échange; σ échange'),('deletion','σ1 line','a+ et a−'),('display','left middle','σ1,σ,σ2,σ0; σ′'),('text','left middle','subdivision barycentrique'),('display','middle','σ0=σ2 soit σ′; σ1=σσ′'),('deletion','middle below equation','σ=σ1σ′'),('display','right middle','σσ′,σ,σ′,σ′'),('display','right lower middle','σσ′,σ′,σ'),('drawing','upper right','two pencil globes'),('drawing','left middle','ink ellipse; dashed arcs; −1,+1,0,∞'),('drawing','lower left','pencil globe; faint label'),('drawing','lower centre','ink oval; dashed meridian; 0,∞,±1'),('margin note','bottom left','139')],observations='The four printed-list numerals have overdrawn first and fourth entries, marked uncertain. Explicit label exchanges read visually; no algebraic inference used to supply deleted formula. The faint text above the lower-left globe is unresolved and tentatively rendered p nouveau. Pencil constructions retained. First and second regrouped sequences have primes on σ and on the lower indexed σ labels respectively. Page contains a small scribbled-over segment, reproduced geometrically rather than deciphered by its expected combinatorics.')
