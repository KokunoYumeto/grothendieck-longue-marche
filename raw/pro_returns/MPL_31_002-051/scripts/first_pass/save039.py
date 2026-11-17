import sys
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/74077fe5e995/MPL_31_002-051_work/scripts')
from save_page import save
head=Path('MPL_31_002-051_work/pages/MPL_31_002-051_31_scan037.tex').read_text().split('Il résulte')[0].replace('\\scanpage{37}','\\scanpage{39}')
text=head+r'''\deleted{\unsure{En particulier si $E$ est}}

\uuline{Th 2} : Si $G$ est un groupe fini d'ordre $n$, l'image de
\[
p_*:H_*(E)\longrightarrow H_*(B)
\]
contient tous les éléments \deleted{\unsure{d'ordre $n$}} divisibles par $n$ dans $H_*(B)$.

\uuline{Dém} : Soit $\zeta$ \deleted{\unsure{un cycle}}$=\sum_{i\in I}a_i\sigma_i$ un cycle de $B$, où $\sigma_i$ sont des simplexes.
Pour tout $\sigma_i$, soit $\tau_i$ simplexe de $E$ tel que $p\tau_i=\sigma_i$. Alors
\[
\theta=\sum_{g\in G,\,i\in I}ga_i\tau_i
\]
est un cycle de $E$, et $p(\theta)=\deleted{\unsure{\zeta}}n\zeta$ \deleted{\illegible{1}}. D'où le Th 2.

\uuline{Th 3} : Si \deleted{\unsure{l'espace}} $E$ est \deleted{\illegible{1}} contractile, $S=$ ss-groupe engendré par les stabilisateurs fini d'ordre $n$, $\pi_i(B)$ est un groupe \deleted{\unsure{fini}} dont \inserted{tous les éléments sont} d'ordre qui divise une puissance de $n$ pour $i>1$

\uuline{Dém} : \deleted{\unsure{D'après}} D'après le Th. 1, $E/S$ est le revêtement universel de $B$, d'où $\pi_i(B)=\pi_i(E/S)$. D'après le Th. 2,

\deleted{\unsure{tous}} les $H_i(E/S)$

\margin{38}
'''
elements=[('text','upper left','UNIVERSITÉ DE PARIS'),('drawing','letterhead first separator','rule dot rule'),('text','upper left','ÉCOLE NORMALE SUPÉRIEURE'),('drawing','letterhead second separator','rule dot rule'),('text','upper left','45, RUE D’ULM'),('text','upper left','ODÉON 06·45'),('drawing','letterhead third separator','rule dot rule'),('deletion','upper right','En particulier si E est'),('text','upper middle','Th 2 : Si G est un groupe fini'),('display','upper middle','p_*:H_*(E)→H_*(B)'),('text','following display','contient tous les éléments'),('deletion','after éléments','d’ordre n'),('text','middle','Dém : Soit ζ'),('deletion','after ζ','un cycle'),('display','middle inline','ζ=∑a_iσ_i'),('text','middle','un cycle de B, où σ_i'),('text','middle','Pour tout σ_i, soit τ_i'),('display','middle','θ=∑ga_iτ_i'),('text','middle','est un cycle de E'),('display','middle right','p(θ)=nζ'),('deletion','before nζ','ζ'),('deletion','after nζ','unreadable word'),('text','middle right','D’où le Th 2'),('text','lower middle','Th 3 : Si E est contractile'),('deletion','after Si','l’espace'),('deletion','after est','unreadable word'),('deletion','after groupe','fini'),('insertion','left margin before d’ordre','tous les éléments sont'),('text','lower','Dém : D’après le Th. 1'),('deletion','after Dém','D’après'),('display','lower inline','π_i(B)=π_i(E/S)'),('text','lower','D’après le Th. 2'),('deletion','last line before les','tous'),('text','last line','les H_i(E/S)'),('margin note','bottom left','38')]
save(39,text,elements,observations='Whole page and both supplied halves read and compared. All cancelled passages enlarged. Two single words remain physically obscured by dense strokes: the word after nζ (attempted reading d’où) and the adjective before contractile (attempted reading acyclique); both are counted as illegible words. No continuation has been supplied after the bottom H_i(E/S). The marginal phrase tous les éléments sont is inserted before d’ordre.')
