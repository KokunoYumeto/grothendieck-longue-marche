import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(34,17,r'''
\scanpage{17}
\mspage{15}
\[
(3.\unsure{15}.1)\qquad I'_t=\prod_{\ell\ne p}(I'/(I',I'))(\ell)\simeq\prod_{\ell\ne p}\mathbf Z_\ell(1).
\]
\deleted{Ceci posé, on constate aussitôt que les opérations de $\pi$ \inserted{(Bien entendu, $I'$ opère trivialement \unsure{sur} $I'_{\unsure{ab}}$, donc c'est le groupe $\pi/I'$ qui opère sur $I'_{\unsure{ab}}$ et à fortiori sur $I'_t$.)} Ceci posé, on constate que $I/I'$ opère trivialement sur (3.16.1), et que l'opération de $\pi/I\simeq\pi_0$ sur $I_t$ \unsure{ainsi}}

\deleted{\unsure{Or}} l'isomorphisme \deleted{de $\pi$} (3.16.1) respecte les opérations de $\pi$ sur les deux mbs, où l'opération sur le deuxième mb. \deleted{est} se fait via $\pi_0$ comme expliqué déjà plus haut.

Ceci en fait exprime le fait que l'isom canonique (\unsure{2.15.1|3.15.1}) est compatible aux ``transport de structure''.

En particulier, on trouve que $I\deleted{/I'}$ opère trivialement sur $I'_t$, en d'autres termes

\uline{Corollaire} $3.\unsure{16}$. Pour tt ss-groupe \inserted{ouvert} invariant $I'$ \deleted{d'indice fini} de $I$, l'extension naturelle de $I/I'$ par le quotient $I'_t\simeq\prod_{\ell\ne p}\mathbf Z_\ell(1)$ de $I'$ est une extension \uline{centrale}.
''',[
('text','top right','15'),('display','top','(3.15.1) I prime t product abelianizations'),
('deletion','upper block','Ceci posé, on constate aussitôt'),('insertion','within upper cancelled block','Bien entendu, I prime opère trivialement'),
('deletion','left before live paragraph','Or'),('text','middle','l’isomorphisme (3.16.1) respecte'),('deletion','middle first line','de pi'),('deletion','middle third line','est'),
('text','below middle','Ceci en fait exprime le fait'),('text','lower','En particulier, on trouve'),('deletion','lower formula','/I prime'),
('text','lower','Corollaire 3.16. Pour tt ss-groupe'),('insertion','above invariant','ouvert'),('deletion','before de I','d’indice fini')
],remarks='The upper paragraph is cancelled in its entirety and contains an inserted parenthesis; its crossed and faint connectors and abelianization subscripts remain uncertain. The displayed label is overwritten. The later reference appears to begin with 2, retained with an alternative; the two references to (3.16.1) are retained as written. The quotient after I in the penultimate paragraph is cancelled.')
