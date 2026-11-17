import sys
from pathlib import Path
sys.path.insert(0,'/workspace/scratch/74077fe5e995/MPL_31_002-051_work/scripts')
from save_page import save
head=Path('MPL_31_002-051_work/pages/MPL_31_002-051_31_scan037.tex').read_text().split('Il résulte')[0].replace('\\scanpage{37}','\\scanpage{38}')
text=head+r'''\uuline{Dém}. $G/S$ opère sans point fixe sur $E/S$ : si
\[
gx=s_0x,\quad g=s_0s\text{ avec }sx=x\quad\Rightarrow\quad g\in S.
\]
Si $g\notin S$, $g$ transforme tout sommet de $E$ en un sommet distinct, donc tout simplexe en un simplexe disjoint. $E/G=E/S\big/G/S$.

---

\uline{Le Théorème 1} \deleted{\unsure{en}} résulte de ce lemme et de ce qui a été vu précédemment.

\deleted{$\unsure{p_*\pi_1(B)|p_*\pi_1(E)}$}

\margin{37}
'''
elements=[('text','upper left','UNIVERSITÉ DE PARIS'),('drawing','letterhead first separator','rule dot rule'),('text','upper left','ÉCOLE NORMALE SUPÉRIEURE'),('drawing','letterhead second separator','rule dot rule'),('text','upper left','45, RUE D’ULM'),('text','upper left','ODÉON 06·45'),('drawing','letterhead third separator','rule dot rule'),('text','upper right','Dém. G/S opère'),('display','under heading','gx=s0x, g=s0s'),('text','upper middle','Si g∉S, g transforme'),('display','end of paragraph','E/G=E/S / G/S'),('text','middle separator','—'),('text','middle','Le Théorème 1 résulte'),('deletion','after Théorème 1','en'),('deletion','under conclusion','p_*π1(B)|p_*π1(E)'),('margin note','bottom left','37')]
save(38,text,elements,observations='Whole page and both supplied halves read. Formula index 0 checked at enlarged scale. The short cancellation before résulte and the cancelled formula below the conclusion remain low-confidence readings. The displayed quotient is written as successive slashes, preserved without silently adding grouping parentheses.')
