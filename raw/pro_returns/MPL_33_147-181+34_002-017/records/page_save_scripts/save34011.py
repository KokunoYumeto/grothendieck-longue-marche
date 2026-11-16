import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{11}
\mspage{9}

cette opération, via l'isomorphisme (2.4.2), \deleted{n'est} n'est autre que celle qui provient de \deleted{l'isomorphisme de} \inserted{l'opération naturelle} de $\pi_0$ sur les facteurs $\mathbf Z_\ell(1)$, via l'expression (2.3.3) de $\mathbf Z_\ell(1)$.

Bien entendu, pour tout $\ell$ \uline{il existe} \unsure{des} isomorphismes
\[
\mathbf Z_\ell(1)\simeq\mathbf Z_\ell,
\]
dont le choix revient au choix d'un syst. cohérent de racines \inserted{primitives} $\ell^\nu$-ièmes de 1 dans $\bar K$; Mais on fera attention qu'il n'y a pas de façon naturelle de faire ce choix, et que c'est l'expression intrinsèque (2.4.2) qui seule \deleted{\unsure{peut}} tient compte des opérations naturelles de $\pi_0$ sur le premier membre.
\margin{10}
'''
e=[('text','top','cette opération via l’isomorphisme'),('deletion','top line 2','n’est'),('deletion','top line 3','l’isomorphisme de'),('insertion','above deletion','l’opération naturelle'),('text','middle','Bien entendu pour tout ℓ'),('display','middle','Zℓ(1) ≃ Zℓ'),('text','middle-lower','dont le choix revient'),('insertion','above ℓ^ν-ièmes','primitives'),('deletion','lower','peut'),('margin note','bottom left','10')]
save_page(34,11,tex,e,remarks='The horizontal stroke under il existe is treated as underlining, not as deletion of those clearly live elevated words. The word before isomorphismes is dark and uncertain. The lower half of the sheet is blank apart from the archival number and reverse-side show-through.')
