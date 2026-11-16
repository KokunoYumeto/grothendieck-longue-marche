# D.80 source and scope ledger

**Notes-only, unregistered during checkpoint12 freeze.** Full proof: `notes/de_sha_unrestricted_draft.tex`; exact CRT certificate: `notes/de_sha_unrestricted_certificate.py/.json/.out`. No diagnostic PDF.

**verified:** Milne, *Arithmetic Duality Theorems*, I.Corollary2.3, printed p28/PDFp35, freshly reopened as `turn1039view0` (Theorem2.1 also reopened as `turn1039view1`). URL: https://www.jmilne.org/math/Books/ADTnot.pdf . It gives the finite local perfect H1 pairing and finiteness used in the exact compact/discrete dual passage. The local fields here have characteristic zero, and all coefficient modules are finite five-primary modules.

D43 was reread in full: its integral local H1 vanishing holds for every nonzero abelian inertia vector and does not require a metabelian lift. Finite local H0 is Mittag--Leffler, so compact H1 is the inverse limit of finite H1. Finite Tate duality and Pontryagin duality of finite limits then identify the discrete Cartier H1 with its dual direct limit, which is zero. This does not assert any prime-uniform coefficient bound by itself.

Uniformity instead comes from the finite residual inertia support. At every other prime, the same ten-dimensional module M10 from D78 is unramified since t_i^(5c)=1 modulo(5,I^4). Its explicit Frobenius primitives work there even if the full module has infinite ramification. Only finitely many remaining local classes need a larger coefficient level; taking their maximum gives one genuine finite global coefficient module. No direct limit is interchanged with the infinite product of local groups.

D78/D79 supply the actual semidirect image, coinduction and complete local connecting-kernel calculation once two residual prime vectors span F5² and the local unit-log vector is primitive. The unrestricted completed Kummer valuation description proves both the image claim and finiteness of the residual support. D77 gives the exact remaining compact factors. D74 is applied only to the explicitly finite-support rational-point examples.

The CRT formula is proved for every positive integer d≥1 and independently checked at ranks1–30. It forces valuation1 at prime2 in t and at prime3 in1−t, and exact local logarithm depth d at5. The d=0 order-five case is t=−2 separately; no d=0 CRT assertion is made. General section existence, arbitrary infinite-ramification H1 ranks, and the general nonseparated kernel stay Open.

## Integration after checkpoint12

D.80 is now Proved in `sections/D_alexander_unrestricted_units.tex` after root, FGH, and PBC full independent proof/source/exact-certificate audits. Canonical certificate: `code/de_sha_unrestricted.py` with adjacent JSON/stdout. The original candidate and all audit versions remain unchanged. No diagnostic PDF was created.
