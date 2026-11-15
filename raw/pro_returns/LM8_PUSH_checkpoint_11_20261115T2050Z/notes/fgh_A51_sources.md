# A.51 source checks and exact certificate

The historical draft is fgh_A51_draft.tex; the approved registered section is sections/A_heisenberg_fixed.tex. The exact cellular program fgh_heisenberg_polarization.py and its JSON/stdout are retained; the registered names, after audit, will be code/a_heisenberg_polarization.py/.json/.out. The JSON includes all four rational cellular cocycles, not only their final pairing matrix.

- **verified:** J. S. Milne, Shimura varieties and moduli, Handbook of Moduli II, Theorem4.4 p489 and Theorem7.12 p508. Primary author PDF https://www.jmilne.org/math/xnotes/svhIP.pdf . Opened refs turn760view0--2. The use is only classical full faithfulness for weight-one Hodge structures and algebraic abelian-variety homomorphisms; no conjectural motivic realization is involved.
- **verified in earlier A.44 source audit:** Serre--Tate, Good reduction of abelian varieties, Theorem6(a), and its specialization/endomorphism extension proof p503. A.51 repeats the faithful-module argument for an explicitly constructed quaternion algebra. The division property at3 is proved directly from the unit norm obstruction.
- **already proved:** A.42 and the primary Dupuy--Rabinoff Abel-map statement cited there turn equal special Abel images into a rational joining path. A.51 verifies every cusp difference separately using equation9(P_T-P_U)=q^*(3(T-U)).

DE independently passed the conceptual Hodge/quaternion and division-module/reduction steps, before the exact determinant was computed. Root and DE subsequently passed the full proof/source/code audits, including the topological identification; A.51 is registered.
