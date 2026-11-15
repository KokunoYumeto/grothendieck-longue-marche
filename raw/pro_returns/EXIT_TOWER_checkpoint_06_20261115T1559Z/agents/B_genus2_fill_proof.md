# Exact genus-two compact-relator certificates

The executed implementation is `code/b_genus2_fill.py`. Its interface is precisely `RELS, fill, expanded, conjugate, inverse, reduce_sequence, red, cat, inv`, used by `d_positive_genus_peiffer.py --genus-two`. The compact presentation has the five generators sigma1,...,sigma5 and seventeen relators: the ten Artin pairs, the five commutators [W,sigma_i], W² and omega6, with

    W=1234554321, omega_n=(1...n-1)^n.

Every certificate is a tuple `(conjugator, relator_index, sign)`. Its literal free-group expansion is the product of the corresponding conjugates of the seventeen fixed relators. Thus correctness of a saved certificate can be verified without a braid or mapping-class word-problem oracle.

## 1. Braid cells, with signs and actual conjugators

Right reversing replaces `-i,j` by `j,-i` for distant indices and by `j,i,-j,-i` for adjacent indices; `-i,i` cancels. Left reversing replaces `i,-j` by `-j,i` or by `-j,-i,j,i`; `i,-i` cancels. For each of the finitely many noncancellation rules, the program computes `lhs rhs^-1` as an explicit cyclic conjugate of the appropriate fixed Artin relator or its inverse. It stores the exact conjugator and sign and checks that equality freely. Applying a rewrite after prefix p conjugates that cell by p. A sequence of rewrites therefore expands to initial_word final_word^-1 by telescoping. A right pass followed by a left pass ends at the empty word for a braid identity.

The completeness input is Patrick Dehornoy and Bert Wiest, *On word reversing in braid groups*, International Journal of Algebra and Computation16(5) (2006),941–957, §1 Proposition4, Lemma5 and the following Remark, PDF pp3–4. Primary text opened at https://dehornoy.lmno.cnrs.fr/Papers/Dhg.pdf ; arXiv:math/0407333. The Remark states the one-pass positive and two-pass arbitrary braid word problems. For the finite outputs here, each certificate is also freely expanded, so even its correctness does not depend on trusting termination or a decision procedure.

## 2. The six spherical star words

Let A_ij be the standard pure Artin generators. Put t_i=sigma_(i-1)...sigma1, with t_1=1. The exact B6 equalities

    W_i=t_i W t_i^-1 = product_(j≠i, increasing j) A_min(i,j),max(i,j)

are each certified by the braid-cell procedure. The added centralizer relators then give a certificate for W_i W^-1. For a word g, the certificate for [g,W] is constructed letter by letter using

    [ab,W] = a[b,W]a^-1 [a,W],
    [sigma_j,W]=[W,sigma_j]^-1,
    [sigma_j^-1,W]=sigma_j^-1[W,sigma_j]sigma_j.

For i≤5 write W_i=L_i A_i6, where L_i is the star product over the other labels1,...,5. Conjugating the certificate for L_i A_i6 W^-1 by L_i^-1 gives exactly a certificate for

    A_i6 (L_i^-1 W)^-1.

The negative-generator replacement is obtained by conjugating the inverse certificate by A_i6^-1. All signs are preserved.

## 3. The residual central word

Pure braid combing supplies an explicit A_ij word for the original word w. The equality between this expansion and w is itself certified by double reversing; the combing algorithm is not used as an unexplained equality oracle. Replace each A_i6 by L_i^-1 W with the above cells. For a product of replacements g_i→h_i, conjugate the i-th replacement certificate by h_1...h_(i-1); their product expands to `(product g_i)(product h_i)^-1`.

An internal symbol6 denotes W only while collecting it to the right. Every interchange W^e sigma_j^d→sigma_j^d W^e, e,d=±1, uses the exact commutator certificate from Section2, with the appropriate prefix. The result is V W^e, where V is a pure B5 word. Its central exponent k is its linking number on strands1,2. The equality V=omega5^k is again certified by double reversing, rather than inferred from linking number alone.

The B6 identity omega6=omega5 W6 has a braid certificate. Together with W6=W and the compact omega6 relator it gives a certificate for omega5 W, i.e. omega5=W^-1. Substitution with its signed powers reduces the residual word to W^(e-k). That exponent is even for the inputs under consideration; the final cells are exactly signed copies of the compact W² relator. The final returned sequence is freely checked against w. No residual central sign is accepted merely because a sphere quotient vanishes.

## 4. Executed outputs and geometric scope

The standalone test verifies all17 fixed relators, all6 star identities and5 signed central-power cases:28 certificates and19672 factors. The full generic driver then produces:

- 20 objects including the open stratum,155 oriented one-cells and136 generators after the19-edge tree collapse;
- 550 source relators:17 compact,200 local,178 sewing,89 open-arrow,42 open-face and24 triangle relators;
- 62 distinct compact certificates containing24823 conjugate-relator factors;
- all24 cone identities and402 boundary two-cell prisms, with every free expansion and target Peiffer cancellation checked.

The target words of the24 boundary triangles freely cancel with the actual stored twists; their compact certificates are empty. This alone would not provide the required cellular comparison. The driver also retains the200 local and178 sewing relators with their full compact disks, all lower-cell mapping-cylinder prisms, and the simultaneous inverse-coherence disk choices. This is the same specified mapping-cylinder construction already used in D30. Its identities map literally to T followed by inverse(T), hence have the displayed Peiffer cancellations. The outputs do not assert a finite basis of the entire positive-genus identity module and do not omit the other local BG/product three-cells.

Files: `code/b_genus2_fill.py/.json/.out`, `code/d_genus_two_peiffer.json/.out`, and the shared `code/d_positive_genus_peiffer.py`. The source and certificate data remain separate from the independent serialized verifier being run by D.
