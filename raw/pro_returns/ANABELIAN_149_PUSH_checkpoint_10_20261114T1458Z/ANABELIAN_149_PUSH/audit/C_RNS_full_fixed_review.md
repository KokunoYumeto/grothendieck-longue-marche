# C.7h: exact RNS uniqueness and full local fixed groups

Status: Proved; root and topos independently reviewed the exact source and complete deduction. Integrated after explicit root approval.

## Claim and scope

For every finite extension K/Q_p, every smooth geometrically connected hyperbolic curve U/K, and every open subgroup H′ of H=G_{K(μ∞)}, the full geometric fundamental group has fixed group 1 under an ordinary K-point section and full cusp inertia Zhat(1) under a K-rational tangential section. This covers all hyperbolic types, p=2 and p=3, proper and affine curves, good and bad reduction, arbitrary nonzero tangent coefficients, and specifically the Q5 tripod point2 and tangent coefficient1. It is a deduction from an exact theorem of Mochizuki–Tsujimura, with the auxiliary valuation and group arguments written out. There is no priority or novelty assertion.

Integrated proof: `sections/C_RNS_full_fixed_extension.tex`, claim C.7h.

## Primary sources actually opened

1. Mochizuki, S., & Tsujimura, S. (2024, March 30 revision). *Resolution of nonsingularities, point-theoreticity, and metric-admissibility for p-adic hyperbolic curves*. RIMS Preprint1974. Existing bibliography key `D_MochizukiTsujimura2024`.

   https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf

   Opened the complete 107-page author PDF, especially:

   - Introduction pp2–4: arithmetic geometrically pro-Σ group convention; Theorem A at printedp4. For K finite/Qp and Σ all primes, every hyperbolic U satisfies Σ-RNS.
   - Definition2.2(i), printedp30: p-valuation ring R has R∩K=O_K; primitive means the maximal ideal is the only prime ideal containingp. There is no rank-one condition.
   - Definition2.2(ii)–(v), pp30–32: Ω is the completed algebraic closure, but the algebraic universal-cover function field K(Xtilde) is the field used by the valuation/center-chain correspondence.
   - Proposition2.3(v), printedp37: all p-valuations of K(Xtilde) correspond bijectively to VE(Xtilde), and primitive valuations correspond to VEprim. This clause has no properness hypothesis and is not restricted to ordinary points of the open curve.
   - Proposition2.3(vii), pp38–39, was distinguished from (v): its classification of all primitive valuations by real/point-theoretic types assumes properness, and is not needed.
   - Proof of Proposition2.3(v)/(vii), pp43–45: recovering the horizontal valuation ring by inverting constants; primitiveness using the horizontal evaluation kernel divisible byp. The candidate supplies these arguments explicitly for a cuspidal lift as well as an ordinary lift.
   - Proposition2.4(vii), printedpp51–52: for a closed J⊂G_K with J∩I_K admitting a surjection onto Z_l, l∈Σ\{p}, a section J→Π_U^(Σ) fixes at most one element of VEprim. Neither normality of J nor open cyclotomic image is an assumption of uniqueness. Open cyclotomic image is an additional hypothesis only for existence.
   - Its full proof, printedp54: existence comes from Proposition2.3(xi); uniqueness instead uses Proposition2.4(iv), TopicsIV Corollary1.15(iv), and Proposition2.3(ix). These are explicitly separated in the source.

   Local temporary copies: `tmp/RNS_Mochizuki_Tsujimura.pdf` and `.txt`, outside the deliverable bundle. Opened web refs include turn511view0 and earlier turn503view0, turn505view0–2. The printed pagination above is one greater than the zero-based PDF page index.

2. Hoshi, Y., & Mochizuki, S. *Topics surrounding the combinatorial anabelian geometry of hyperbolic curves IV: Discreteness and sections*. Author PDF header July2022; served filename identifies revision2023-12-15.

   https://www.kurims.kyoto-u.ac.jp/~motizuki/Combinatorial%20Anabelian%20Topics%20IV.pdf

   Opened Corollary1.15 in full, pp36–42. Global setup requires H∩I_K to have open image in the pro-Σ† inertia quotient, for Σ† avoidingp. With Σ†={l}, our stronger explicit tame-image calculation meets this. Part(iii), an existence assertion, adds l-cyclotomic fullness. Part(iv), the bounded-distance assertion used by RNS uniqueness, does not add it: it considers two elements of the previously defined Stab(s). Its proof at p41 invokes Lemma1.11(ii), separately from the proof of(iii). Thus the reference to the definition of Stab(s) does not import the existence hypothesis.

   Temporary copies: `tmp/pdf_text/HM_Topics_IV.pdf` and `.txt`. Opened web refs turn515view0, turn516view0. This revisits the earlier failed application of Theorem1.13: that theorem's existence conclusion really does require cyclotomic fullness, whereas the uniqueness clause used now does not.

## Complete comparison chain

1. Work with the algebraic field L=K(U_tilde), the union of connected finite arithmetic etale-cover function fields. Its constant field contains Kbar. The arithmetic group E_U acts on L; Π is the subgroup fixing Kbar.
2. A chosen point/tangent basepoint determines a compatible horizontal place w of L, with residue Kbar, and its section preserves w.
3. Let A=O_w and I=m_w. The composite R=ev_w^{-1}(O_Kbar) is a valuation ring restricting to O_K. It is primitive because I=pI⊂pR and R/I=O_Kbar has sqrt(p)=m_Kbar.
4. R[1/p]=A, because every algebraic residue has finite p-adic valuation. Thus preserving R preserves the actual horizontal lift, not merely a special-fibre reduction.
5. Every open H′⊂H meets the RNS subgroup hypothesis. The cyclotomic kernel contains the closed commutator subgroup of G_K. In G_K/P_K=T⋊Zhat, Frobenius acts byq, so that commutator subgroup maps onto a subgroup containing(q−1)T. Therefore H has open nonzero image in every Z_l(1), l≠p, and its open H′ does too. An open image is isomorphic to Z_l; the theorem asks for a surjection to Z_l, not a prescribed coordinate generator.
6. If g centralizes the chosen section on H′, then R and gR are both fixed primitive valuations. Exact RNS uniqueness gives gR=R and hence gA=A.
7. The geometric stabilizer of an interior lift is trivial in every finite geometric Galois quotient, because the map is etale and residues are algebraically closed. The geometric stabilizer of a cusp is precisely full cusp inertia. The latter is fixed by H′ because its conjugation character is cyclotomic.

No finite-level fixed element is lifted through a quotient. No cofinality of genus-zero or genus-one covers, no nilpotent detection theorem, and no equality of profinite groups inferred from their pro-p images enters this proof.

## Consequences for earlier attempts

C.7h supersedes only the remaining *unresolved status* of the full-group question. C.7a–g remain valid independent results and methods, with their precise intrinsic limitations retained. The nontrivial common genus-zero monodromy kernel of C.7d remains nontrivial; RNS proves that the arithmetic fixed subgroup in it is trivial for ordinary sections. The finite exceptional sets in C.7f remain legitimate bounds attached to that method; they no longer constitute an unresolved obstruction to the full theorem.

Earlier C.7g literature searches (root) included “cyclotomic punctured elliptic sections”, “elliptic Green function Kummer fundamental group”, and “cyclotomic point-separation elliptic”. No exact matching publication was located in those searches. Nearby opened sources concerned pro-p reduction type or preservation of decomposition groups under isomorphisms. This is a record of search scope, not an inference of novelty. The present exact RNS theorem supplies a stronger general uniqueness mechanism.

No numerical test is needed for the valuation argument. Its decisive checks are exact theorem hypotheses, equivariance, localization R[1/p]=A, and geometric stabilizers, all explicitly proved or matched to opened sources above.

The integrated statement also includes every continuous cuspidal section with image in the chosen arithmetic cusp decomposition group. Such a section fixes the horizontal place regardless of its Kummer cocycle, and conjugation on cusp inertia is always cyclotomic. Thus no restriction to tangent coefficients in K* is needed for that part.
