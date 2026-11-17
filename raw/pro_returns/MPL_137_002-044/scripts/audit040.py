from audit_support import revise
revise(40,replacements=[(r'\unsure{strictement} $k$-linéaire',r'\unsure{structure|strictement} $k$-linéaire')],
doubts=[('description of A','structure k-linéaire','strictement k-linéaire','medium')],
notation=[('solid raised dot for complex on 040',r'C^\bullet','The raised mark in the opening and (C,C-dot) is solid and round, unlike the star-plus-exclamation marks on 038; do not globally normalize it.')],
note='Second audit against whole scan and enlarged bands through the faint last lines. Rechecked all three Hom cases, finite-sum insertion, conditions on chain complexes, two displayed degree labels and differential components. Compared the left-hand pen exercises with their manual TikZ paths; retained the explicit crop-candidate qualification for approximation.')
