# Independent R6 elliptic audit

Current source root: `background/gt_tower_check_cp10`.
Proofs: `sections/part_E_elliptic_audit.tex`, statements E.110 onward.
Exact algebra and finite examples: `code/ghost_audit_elliptic.py` and
`code/ghost_audit_elliptic.out`, executed successfully in this run.

## New findings

0. **Exact local-three countermodel to a rigidity inference (E.122).**
   Compact-passing original ghosts may be constructed with ordinary
   local point exactly3 at Q₃ by maintaining separate errors for
   a_j/3 and b_j/(−2), and choosing their exact n_j-th target roots.
   The full profinite affine abelian section can then be adjusted by
   completed global norm-one elements so that its localization at3
   is the actual origin point section on Y, while its global proper
   class remains zero. The completion step uses an explicit compatible
   recursion with corrections in successive powers3^j, supported by
   the proved weak approximation of the boundary norm-one tori.
   E.121's three-primary class-three exclusion can be imposed at the
   same time. Thus proper MW rigidity plus exact affine-abelian local
   matching at3 cannot imply finite support or a full pro-three lift.
0. **New three-primary exclusion (E.121).** After any legal finite
   prefix of the compact-passing family, a later q_j may be chosen
   with e=v₃(q_j−1)>f=v₃(n_j). Multiplying the local n_j-th root
   that specifies r_j modulo q_j by a primitive 3^f-th root of unity
   cycles the integral primitive u modulo3 through all three values.
   The canonical global class-two reduction has fixed γ modulo3 and
   α≠0 modulo3. Two of those root choices force γ−q_j αu≠0 modulo3.
   Choosing later primes1 modulo q_j preserves this mismatch, so the
   third residue has valuation f<e and is detected modulo3^{f+1}.
   This is a genuine pro-three exclusion, retains all compact tests,
   and works after every legal prefix. By B.20 the locally excluded
   set is open and dense in the compact-passing family; its complement
   is a closed nowhere dense necessary remainder, whose emptiness is
   not proved. The cohomology agent independently checked the global
   normalization and the local root-steering calculation.
1. The actual three-isogeny descent is sound and proves **rank one** for
   E': y²=x³+9, with three-adic completion Z₃P₀⊕(Z/3)T. It does not
   supply a rank-zero target. The present proof includes every local
   Selmer condition through realization of all candidates by rational
   points, rather than trusting a numerical rank computation.
2. Stronger local detection: localization of that global completion to
   E'(Q₃)^∧3 is an isomorphism. The two classes 6 and 12 remain independent
   over Q₃: the valuation and the noncube unit 2 distinguish them. The
   quotient by three has size 9. This also proves phi:E'(Q₃)→E(Q₃)
   surjective and supplies a shorter exact proof of the absolute H¹
   calculation.
3. A fresh proof of the cubic model uses the pole divisor of its x
   coordinate. The denominator resultant is 12(u−1)³(3u³+2); the sole
   uncancelled pole is of order two at (1,1). This proves degree one
   without borrowing the prior inverse-map program.
4. C.3.5 proves a nonempty family passing **compact elliptic support
   tests**. It neither claims nor proves a full pro-three section.
   The phrase “passes every pro-three test” cannot mean all finite
   pro-three quotient tests; no such conclusion follows.
5. The full boundary norm calculation has no defect found and is
   independently proved in E.116–117: H¹(G,X)=H²(G,X)=0 for
   G=H₃⋊C₂, H=S₃, and the local image at three is the full G.
   Hence each boundary norm map at Q₃ is surjective, and no extra
   modulus 27 restriction is necessary.
6. Original A.44 uses n_j=(j+4)! in **both** updates a_{j+1}=a_jq_j^{n_j}
   and b_{j+1}=b_jr_j^{n_j}. The next-stage m_j=n_{j+1}=(j+5)! is the
   exponent of the next diagonal curve and its r-prime radical condition;
   it is not the exponent attached to r_j in B.

## Prior claims checked and current exact status

| Prior ID | Exact source | In-run result | Status and scope |
|---|---|---|---|
| C.3.1 | `part_c_elliptic_target.tex` | E.110, E.119 | Proved actual pointed model and necessary full pro-three factorization; independently reconstructed the selected central-Frobenius prime and the local-fibre exclusion. |
| C.3.2 | `part_c_elliptic_arithmetic.tex`, first result and proof | E.111 | Complete independent isogeny descent, rank and three-primary Sha proof. |
| C.3.3 | same file, second result and proof | E.112 | Absolute continuous H¹ proof; strengthened to exact Q₃ detection. |
| C.3.4 | same file, third result and proof | E.113 | Necessary support tests proved with actual cover maps and full local boundary rigidity A.31. |
| C.3.5 | `part_c_elliptic_survival.tex` | E.114 | Chebotarev compatibility and finite-field group argument proved; no full pro-three existence claim. |
| C.3.6 | `part_c_generalized_jacobian.tex` | E.115 | Local quotient at two and all three rational sheets proved. |
| C.3.7 | same file | E.115 | Actual affine abelian quotient and exact three-primary norm image proved. |
| C.3.8 | `part_c_boundary_norms.tex` | E.116 | Galois groups, stabilizers, group cohomology, Hasse norm principle and weak approximation proved. |
| C.3.9 | same file | E.117 | Norm lift and continuous completed products proved; extra 27 condition superseded by E.116. |
| C.3.10 | `part_c_boundary_local_norm.tex` | E.116–117 | Local norm surjectivity at three and all-passing-family affine abelian lift proved. |
| C.3.11 | `part_c_prefix_class3.tex`, last result | E.118 | Proved quotient implication K''⊂Γ₄ and independently reconstructed its existential coefficient-five premise. This is not a pro-three exclusion. |
| C.1.20 | `part_c_prefix_class3.tex`, first result | E.118 | Proved the exact frozen coefficient-five class using integral local primitives before reduction. |
| C.2.7 | `part_c_prefix_class3.tex`, second result | E.118 | Reconstructed compatible Chebotarev automorphisms and the q₁ coefficient-five obstruction modulo25, retaining all noncube conditions. |
| C.2.6 | `part_c_class3_original.tex` | E.119 | Reconstructed selected q₀ with a coefficient-three obstruction modulo9; other class-two reductions fail at two. |

## Sources actually opened

- Milne, *Elliptic Curves*, 2nd ed., author PDF at
  https://www.jmilne.org/math/Books/EC2.pdf: II.1.5–1.8 (printed p.49),
  Chapter IV finite-basis statement (p.105), IV.2 (28)–(29).
- Milne, *Arithmetic Duality Theorems*, 2nd ed.,
  https://www.jmilne.org/math/Books/ADTnot.pdf: I.2.4 pp.28–29,
  I.3.3–3.5, and I.6.26(b), p.92. The latter is applied only after
  establishing vanishing of the three-primary Sha; no unsupported
  assertion about every primary component is used.
- Milne, *Class Field Theory*, v4.03, I.4.16, pp.49–50:
  https://www.jmilne.org/math/CourseNotes/CFT.pdf.
- Mochizuki (2012), *Topics in Absolute Anabelian Geometry I*,
  Prop. A.8(ii)–(iii), pp.232–234:
  https://www.ms.u-tokyo.ac.jp/journal/pdf/jms190201.pdf.
- Jordan–Ribet–Scholl (2024), §1.4, Prop.1.6, equation (1.4.1), p.954:
  DOI 10.1112/S0010437X23007662, publisher PDF opened.
- Macedo–Newton (2022), §2, Theorems2.1–2.3, equations (2.4),(2.6),
  Definition2.5, author pp.8–10 / journal pp.496–498:
  DOI 10.1017/S0305004121000268, Reading-hosted publisher PDF opened.

Web retrieval references for parent reuse (parent must open before citing):
`turn113294591view2` (EC isogenies), `turn744910566view0` (global duality),
`turn744910566view1` (local torus duality), `turn578140727view4` (KW),
`turn744910566view2` (Mochizuki A.8), `turn113294591view1` (generalized
Jacobian), `turn312644317view0` (norm principle comparison),
`turn354931780view0` and `turn354931780view1` (local elliptic duality and
formal structure), `turn354931780view2` and `turn960572961view1` (Selmer
exact sequences, pp.112–113).

## Remaining full pro-three gate

There is a continuous cocycle in the actual affine abelian cover quotient
with proper component zero for every pair in the compact-passing family.
The next necessary problem is its lift to nonabelian quotients of the
geometric group of Y, or a different affine abelian class that lifts.
The two-dimensional weight-two/three coordinates of the original U
cannot be replaced by a general theorem that separate triple Massey
products vanish: their defining systems must be compatible.

The new local-three isomorphism fixes the proper coefficient pair (a,b)
when a proper local class is prescribed. It does not force an ordinary
abelian local section of the punctured curve at Q₃ to be the section of
its ordinary point. The proven local boundary theorem A.31 applies at
q≠ell; applying it at q=ell=3 would be a new unsupported step. The exact
norm image allows toric classes to alter u and v independently at Q₃,
so proper rigidity alone does not remove this gap.

E.121 further shows that even three-primary class-three survival is not
automatic in the compact-passing family, and gives an open dense set of
   counterexamples to that stronger reading. It does not prove that the
remaining closed nowhere dense set is empty. The original C.3.5 theorem,
read as its stated compact-test survival assertion, remains correct.

The additional E.122 construction shows that even forcing the affine
abelian localization at the coefficient prime to equal the actual point
section is insufficient. The missing gate is therefore not supplied by
proper localization rigidity plus a single coefficient-prime point
condition. It is the simultaneous integral nonabelian matching at all
support primes and subsequent compatible higher obstructions.
# New coefficient-three remainder: E.123--E.124

## E.128--E.129: arbitrary finite cusp data, and a selected compact failure

E.128 proves the finite radical compatibility needed for higher matching conditions. Over the full CRT cyclotomic field, the intersection of the finite three-primary point/action field with a cyclic radical field is a pure three-power root line. If the cyclotomic multiplier is minus one modulo three, its affine action on the root indices has a unique fixed point. This fixed root can be extended to a full radical root compatibly with the independently fixed square root. The actual cusp-one path coordinate is retained in the arithmetic data field; its top coordinate must not be inferred only from the preceding conjugation action. The finite-class image argument applies to any integral class-r section with the two independent inertia vectors at five and eleven, including rational-base representatives used in the new class-four normalization.

E.129 supplies an exact selected obstruction beyond the strong class-two gate. For the actual ninth-Heisenberg cover, use `X^9=t`, `Y^9=1-t`, `Z^9=Theta(X)` with `Theta=product_(i=1)^8 (1-zeta9^i X)^i`. Independent Kummer valuations and the exact deck lifts identify the marked quotient. For primes minus one modulo nine the based arithmetic action is `Z -> H(X)/Z`, with `H=(1-X^9)/(1-X)`. Comparing point three with the actual cusp-one branch gives the ratio in E.129.3. The cusp factor is explicitly `zeta9^(-eta(Frob))`, including the nonzero shift.

At the auxiliary prime 6551, in `F_p[s]/(s^2-17)`, the certificate uses `zeta9=6318+4878s`, `X=5423`, `Theta(X)=2167+4130s`, `Theta(1)=6536+617s`, and `H=940`. The two central factors agree and equal `3275+1508s=zeta9^6`; eta is three modulo nine. Yet `[728](3,-6)=(0,-3)` on `Y^2=X^3+9`, so `P0-T` has nonzero three-primary order three in a cyclic three-primary group of order nine. The actual code now checks these identities, rather than leaving the marked-cover comparison as an exploratory assumption.

To make an infinite ordinary output, at the first stage choose the old three-adic B root to be the integer 6551 and solve for the A root. Their shells remain exactly one and two. The finite joint field of the Heisenberg quotient and the ninth-division torsor is a three-extension over Q(mu3), unramified outside two and three, and its maximal abelian field is cyclotomic of three-power conductor. E.128 therefore extends its witness Frobenius class through all old CRT and radical conditions to an arbitrarily large actual B-support prime. Continuing E.123 yields ordinary ghosts with support-matched classes two and three and global class-four lifts, but the elliptic support identity excludes every full pro-three section.

The number 6551 is only the auxiliary Frobenius witness. It is not claimed to be the actual recursive prime. The result excludes selected variants of E.123; it neither eliminates every such output nor settles the E.125 family. The stronger claim that these examples already fail class-four boundary matching is being checked separately and has not been asserted in E.129.

## E.125--E.126: all support denominators minimal, and actual higher image

E.125 now constructs the further family based at `(5/16,11/16)`, with both exponents `(j+11)!`. The old support is `{2,5,11}`, and both fresh support types have `v_3(p^2-1)=1`. At three, both coefficients are units, so the root derivative no longer creates an extra B digit. The rational denominator is handled explicitly with four extra CRT digits at two and multiplication of the local polynomial by sixteen. The radical quadratic fields have conductors five and forty-four; the old near-one roots fix them. The old infinity-type inertia at two is `h(T)=4(alpha-beta)+8`, so the finite-to-integral normalization remains valid. The construction gives support-matched class two and three and a global class-four lift.

For this family, every even-weight global-to-support localization map is an isomorphism. The remaining condition is equality of the pulled-back local discrepancy vectors. If that equality fails for a specified preceding matched section and global lift, two support places witness failure, and one can be taken to be two. This removes the extra local image condition in E.124; it does not establish equality of all those vectors.

E.126 proves a full geometric image lemma for the actual point cocycle at `t=5/16`. The actual tangentially based pro-three action is unramified outside three. On its kernel the point cocycle is a homomorphism, whose compact image contains the two mod-Frattini basis vectors supplied by inertia at five and eleven. A closed subgroup surjecting to the Frattini quotient is the whole free pro-three group. Thus the joint image is `Pi semidirect rho(G_Q)`, retaining the complete higher arithmetic action. This gives arbitrary finite geometric coordinates over any occurring arithmetic element. It does not supply a prime meeting infinitely many conditions or a compatible global ghost tower.

The based-action ramification premise was independently verified from Wojtkowiak (2007), *On the Galois Actions on Torsors of Paths I, Descent of Galois Representations*, Definition 2.0 and Theorem 2.1, printed pp.198--200. Primary PDF: https://www.ms.u-tokyo.ac.jp/journal/pdf/jms140203.pdf . The precise statement is an action into `Aut`, explicitly includes tangential points, and applies to the unit tangent at zero at every prime other than the coefficient prime. The author also states this specific tripod case on printed p.178. The local paper bibliography key is `AuditWojtkowiak2007`, marked Verified.

The cohomology agent independently read and checked both E.125 and E.126, including the old infinity support, fixed-root fields, and actual-action source. Actual finite logs add 26 unit-coefficient three-adic root checks, 13 two-adic denominator checks, 120 old-support even-weight order checks and nine finite conjugate-generator checks. All passed.

The modified recursion in E.123 constructs ordinary infinite-support pairs with actual class-two boundary matching at every support place other than the coefficient prime three. This is a new construction, not an output of the original A.44 complete-splitting recursion. Both coordinate exponents are `(j+7)!`.

The decisive change is to prescribe the old three-adic roots as `xi_3=2` and `eta_3=-((1-a*2^n)/b)^(1/n)`. Their distances from minus one have valuations one and two. At two, `eta_2=-1` and the near-one `xi_2` root make the two radical square-root conditions compatible. The new primes therefore have `v_3(q_j^2-1)=1` and `v_3(r_j^2-1)=2` uniformly. Complete radical splitting is replaced by fixing one radical root. The latter has an exact compatibility criterion: the cyclotomic automorphism must fix the radical's square root.

The fixed point-three quotient is the actual `H_9 semidirect (Z/9)^*` field, with maximal abelian field `Q(mu_9)`. Over the whole CRT cyclotomic field, its intersection with either cyclic radical field is exactly the corresponding ninth-root Kummer line. Thus one may impose the actual point-three Frobenius coordinates `(0,0,0)` at the A primes and `(0,0,eta)` at the B primes. The CRT field includes `mu_27`, which is essential: the value of `eta=(chi^2-1)/24` modulo nine is not determined by `chi` modulo nine.

The integral class-two reduction modulo nine can be normalized to the point-three cochain because all fresh inertia values are divisible by nine, the place-two primitive has no division loss, and the remaining finite cocycle is unramified away from three. The proved fixed-ramification H2 vanishing makes that finite cocycle the reduction of the integral order-three class. The two exact B.24 boundary ratios are then integral at every fresh support, and the old place two also matches. The divided third-residue sequences satisfy the strict `c_0` condition, so a global integral class-three lift follows.

E.124 proves that every such class-three lift is still boundary matched: at a support prime congruent to minus one modulo three, odd weight local integral H1 is zero. E.66 then gives a global class-four lift. At weight `2k`, the global torsor has exponent `3^(1+v_3(k))`; its local image is all of the torsor at two and the A primes, and has index three at every B prime. The old place two pins the unique possible even-weight twist. Compatibility of that same twist at every other support remains an actual condition. The preceding odd global lift can vary; no proof that some odd choice solves every next even test has been supplied.

Independent targeted reviews: the parent checked the whole E.123 construction; the cohomology agent checked the finite-to-integral normalization, exact A/B local formulas including the eta correction, and the cyclic radical intersection. No material gap was found in those explicit proofs. Matching at the coefficient prime three itself has not been asserted.

Actual finite verification is in `code/ghost_audit_boundary_matching.py` and its recorded output. It constructs the full groups of orders 729 and 4374, verifies the derived subgroup and geometric exponent nine, checks all 324 eta cocycle pairs modulo 27, checks 26 local root shells at precision `3^7`, and verifies 316 parity/order identities. These finite calculations do not stand in for the Chebotarev argument or the infinite lifting proof.

The proposed original-A.44 minimal-root route remains unresolved: its B-support denominator is one digit beyond the stage exponent, and its new central cochain modulo that digit depends on the new B prime. E.123 bypasses that dependence by a different recursion; it does not certify the corresponding original family.



## E.133: a dense class-four matching failure

The final E.133 proof is in `sections/part_E_elliptic_audit.tex`. For every legal E.125 finite prefix, the nine possible odd-parameter classes after the even twist is pinned at2 can be excluded at one new A-support prime. On a finite arithmetic-data kernel, the point section maps onto the full finite class4 group Q; all candidate differences become central homomorphisms. Its commutator subgroup therefore supplies a common arbitrary displacement in Gamma4(Q)=F3^3 while fixing every cyclotomic field. At most nine of27 displacements permit one of the nine candidates. The joint-field conductor proof and E.128 realize an allowed displacement in the original recursion. The independent cohomology-agent second read checked the commutator image, preservation of CRT and relative cocycles, and finite-to-integral comparison.

This rules out a support-matched class4 lift and hence a full pro3 section, but retains global class4 lifts and the already matched classes2/3. It does not use a local point-section hypothesis at3. The open dense failure set has a nonempty closed nowhere dense complement by E.132. Every consistent prefix has both kinds of finite-layer continuations. This does not decide the all-depth gate.


## E.134: compact failure is visible at the fourth matching layer

For E.123 all A-support compact tests are forced already by the actual H3 point lift: their elliptic three-primary group has order3. At a B-support, that group is cyclic of order9. If P0−T is nonzero, it lies in its order3 subgroup; every rational MW class vanishes locally modulo3, but a boundary lift R has order9 and nonzero Kummer class.

The finite geometric comparison is constructed explicitly: Delta=<x,y|x^3=y^3=(xy)^3=1> is Z3[zeta3] semidirect C3, Gamma3=3O and Gamma5=9O. Thus Delta/Gamma5 has order243 and class4, with Eprime[3] as the actual pointed compact kernel over H3. A global integralclass4 section matched at2 produces a finite compact class which is unramified at all q>3 and is Kummer at2. Reciprocity and the proved MW completion isomorphism at3 kill the remaining Weil–Chatelet localization; Sha[3]=0 makes the class rational Kummer. This contradicts the B-support boundary class. Hence the E129 outputs already fail support matching at class4, while retaining globalclass4. No local point-section hypothesis at3 is used.

Actual code/output: `code/ghost_audit_triangle.py` and `.out`. Finite group orders243,27,9,3,1 and the E133 729-matrix displacement count were enumerated successfully.

## E152-E154: relative approximation, 2026-11-18 06:52 UTC

The finite relative theorem is proved in `sections/part_E_relative_approximation.tex`. It does not itself solve the integral all-prime class-two support-matching problem. The exact extra arithmetic datum is a Frobenius class with cyclotomic residue outside plus/minus1 and an independent Kummer line. Its invisible dual characters pair only with the first Kummer coordinate and are killed by global reciprocity for globally compatible local first coordinates.

Primary source checked: J. S. Milne, *Arithmetic Duality Theorems*, second edition (2006), I.4.9-I.4.10, printed pages56-57, https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf . **Verified**: opened the theorem, the preceding local pairing definitions, and the finite properness argument; web refs turn758633863view1 and turn481404959view0. Author-site ADT.pdf returned an access error; the Stanford copy is the author text.

The coefficient5 obstruction is specific to preserving the5/16 first coordinate at a B-support. It does not impose the same square condition at an A-support, whose first unit part is free. The23/64 base removes that specific collision. The accompanying matrix certificate is an algebra check, not a substitute for Poitou-Tate or a completed-pair construction.


## E.171–174: the all-coefficient class-two support gate

The new source `sections/part_E_all_prime_class_two.tex` proves a finite-to-integral comparison, an ordinary arithmetic advance, a once-per-coefficient relative repair, and a diagonal existence theorem. The base is (23/64,41/64). Two and three use one fixed actual finite point section, with a single global C24 normalization. Every coefficient at least five is treated once; all later support primes are nonexceptional at that coefficient. The resulting pair is ordinary at every place, has frozen ordinary integer valuations and infinite support, and has one integral all-prime class-two section matching every off-diagonal support point. It consequently has a global class-three lift. It does not supply coefficient-prime matching, zero-support matching, class-three matching, or a full pronilpotent section.

Root and cohomology independently checked E171. Root checked E172 and E173, with two precise wording corrections now applied: actual class-two arithmetic marks are cyclotomic, and allowed geometric conjugation preserves local Kummer classes rather than literally every marked high root. Root and cohomology subsequently completed positive full independent reviews of E174; cohomology also fully re-read E152–154 and E170. Root independently reran the finite certificate successfully. The saved finite certificate checks the relevant arithmetic and finite-group identities and explicitly does not replace the infinite existence proof.
