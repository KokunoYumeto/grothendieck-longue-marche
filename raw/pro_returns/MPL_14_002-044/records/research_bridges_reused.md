# Research record: explicit bridges and reused leaves

Prepared after the transcription freeze. No page file or combined fragment was edited. Line numbers below are lines of the frozen page files, not reconstructed physical ink lines. Context searches are recorded in `root_context_searches.md`; all context transcriptions and prior research conclusions retain the status assigned in `notes/RESULTS_STATE.md`.

## B01 — Tate Hom and anabelian Hom

**Location:** `pages/MPL_14_002-044_14_scan041.tex`, lines 4–24; scan 042, lines 2–10. **Kind:** unpursued implication. **Quote:** “La conj. de Tate”; “produit de deux courbes elliptiques”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 44, scan 008, Tate-module paragraph; `MPL_16+47+54+44_notes.md`, D10; delta: adds an invariant-theoretic statement to the earlier Tate-module programme. **Register:** WG2 §2.4 #3 [unchecked plan]; LM7 C.1 [Known, return's claim]; the Hom comparison itself occurs in `README.md`, bridges B3/B4, without a separate register ID.

Tate's finite-field theorem, for \(\ell\ne\operatorname{char}(k)\), identifies the map \(\operatorname{Hom}_k(A,B)\otimes\mathbf Z_\ell\to\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)\), while the full profinite version of Mochizuki's Theorem A identifies \(\operatorname{Hom}^{\rm dom}_k(X,Y)\to\operatorname{Hom}^{\rm open}_{G_k}(\Pi_X^{\rm prf},\Pi_Y^{\rm prf})/\operatorname{Inn}(\Delta_Y^{\rm prf})\) for hyperbolic curves over sub-\(p\)-adic fields, including number fields [Tate66, §1; Mochizuki99, Theorem A].
The concrete bridge is functorial abelianization of these full profinite geometric groups: a map \(f:X\to Y\) induces \((\Delta_X^{\rm prf})^{\rm ab,\ell}\to(\Delta_Y^{\rm prf})^{\rm ab,\ell}\), identified for smooth proper curves with \(T_\ell J_X\to T_\ell J_Y\), and this is the Tate-module map of the induced map of Jacobians.
For open curves the toric part of the generalized Jacobian supplies the cusp terms, with the exact sequence displayed in B04.
These formulas place the manuscript's linear claim in the requested comparison; scans 041–042 state no anabelian Hom theorem, and the two quoted theorems retain their stated base fields and domains of morphisms.

## B02 — Semisimplicity and centres, through the actual actions

**Location:** `pages/MPL_14_002-044_14_scan003.tex`, lines 4–19; scan 007, lines 6–21; scan 011, lines 13–17. **Kind:** own idea. **Quote:** “classes de rep.”; “G commutatif”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 16, scans 005 and 049; prior notes S13–S16; delta: adds an explicit comparison of centre actions to the correspondence-algebra semisimplicity programme. **Register:** WG2 §2.3 #7 and WG2 §2.4 #3 [unchecked plans]; MPL_7_061-072+8_001-078, scan 061 (§66) [first-pass observation]. **Confidence:** high, for the two explicit maps and the torus calculation; no claim that this finishes the manuscript's motivic programme.

The reconstruction map \(G\to\operatorname{Aut}^{\otimes}(\omega)\) acts by \(g\mapsto(\rho_V(g))_V\), and Deligne–Milne's Proposition 2.23 identifies semisimplicity with pro-reductivity for connected affine groups in characteristic zero [DM18].
For \(G=\mathbf G_m\), every representation is the sum of its character spaces \(V_n\), while its centre acts on \(V_n\) by \(t^n\); this explicit semisimple example has centre \(\mathbf G_m\).
For a geometric hyperbolic-curve group \(\Delta\) in characteristic zero, Mochizuki's Lemma 1.3.1 and Corollary 1.3.2 give the injective conjugation map \(\Delta\to\operatorname{Aut}(\Delta)\) and the exact sequence \(1\to\Delta\to\operatorname{Aut}(\Delta)\to\operatorname{Out}(\Delta)\to1\) [Mochizuki03].
Thus the precise comparison uses tensor automorphisms on one side and conjugation/outer action on the other, with abelianizations of finite covers entering Mochizuki's proof of centre-freeness; the displayed \(\mathbf G_m\) calculation prevents replacing the motivic semisimplicity assertion by a trivial-centre assertion.

## B03 — Polarizations and real structures

**Location:** `pages/MPL_14_002-044_14_scan011.tex`, lines 5–15; scan 013, lines 8–20. **Kind:** unpursued implication. **Quote:** “définissant une polarisation, modulo action de G(R)”; “Ker ε est compact”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 44, scans 002 and 009; notes D13; delta: adds real-form data to the earlier positivity question. **Register:** WG2 §2.3 #12 and WG2 §2.4 #3 [unchecked plans]; `README.md`, bridge B3/B4.

Deligne–Milne's realization of a polarization uses \(\psi^C(x,y)=\psi(x,Cy)>0\), with \(C^2\) central and the inner twist defined by \(C\) giving a compact real form [DM18, 4.22–4.23].
For a smooth proper real curve of genus at least two, the real-section map sends a component of \(X(\mathbf R)\) to a conjugacy class of splittings of \(1\to\pi_1(X_{\mathbf C})\to\pi_1(X)\to\operatorname{Gal}(\mathbf C/\mathbf R)\to1\); Pál's Theorem 1.3 and Example 5.8 give its bijectivity [Pal11].
Abelianizing a splitting gives complex conjugation \(c\) on \(T_\ell J_X\), and the real principal polarization gives the exact compatibility \(e_\ell(cv,cw)=\chi_\ell(c)e_\ell(v,w)=-e_\ell(v,w)\), from Galois equivariance of the Weil pairing and \(c(\zeta)=\zeta^{-1}\).
This is a concrete common realization of the two structures; the manuscript's question about recovering effectivity from a cocharacter still requires the effectivity data specified on scans 009–011.

## B04 — Weights and cyclotomic normalizers

**Location:** `pages/MPL_14_002-044_14_scan003.tex`, lines 14–19; scan 007, lines 15–21; scan 011, line 19; scan 041, lines 6–18. **Kind:** unpursued implication. **Quote:** “motifs effectifs de poids i”; “éléments de Frobenius”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 16, scan 052, Kummer paragraph; cote 44, scan 008; delta: adds the explicit character comparison requested by the planning document. **Register:** LM7 C.1 [Known, return's claim]; LM6 A.22 [Open, return's claim]; LM6 A.50 [Proved, return's claim]; `README.md`, B3/B4.

For a geometrically connected hyperbolic curve \(U=X\setminus D\) in characteristic zero with smooth proper compactification \(X\), abelianization gives \(\widehat{\mathbf Z}(1)\xrightarrow{\Delta}\widehat{\mathbf Z}(1)[D(\bar k)]\to\pi_1(U_{\bar k})^{\rm ab}\to\pi_1(X_{\bar k})^{\rm ab}\to0\), with diagonal \(\Delta\) and each cusp summand mapping through its inertia group [Stix12, (3.1)].
At a rational cusp, \(I\simeq\widehat{\mathbf Z}(1)\), \(N_{\pi_1(U)}(I)=D_I\), and \(g\tau g^{-1}=\tau^{\chi(g)}\) for \(g\in D_I\); this character is the Tate realization's weight \(-2\) character, while the Jacobian Tate module carries weight \(-1\).
Over number fields, Stix's Definitions 26 and 29 and Theorem 30 characterize nontrivial closed pro-\(\ell\) subgroups contained in inertia through an open normalizer image with cyclotomic conjugation action, using \(\operatorname{Hom}_{G_k}(\mathbf Z_\ell(1),T_\ell A)=0\); maximality recovers the full inertia groups in Corollary 31 [Stix12, §§5.1–5.2].
For LM6 A.22 the necessary comparison is explicitly \(N\to\operatorname{Aut}(C)\) against \(\chi\circ p\); the excerpt supplied in the register states openness of \(p(N)\) but supplies no equality of these two characters, so this note records a method and leaves that row's status unchanged.

## B05 — Scope of the open register items

**Location:** `pages/MPL_14_002-044_14_scan011.tex`, lines 15–19; scan 041, lines 6–24. **Kind:** reading question. **Quote:** “propriétés arithmétiques plus profondes”; “éléments de Frobenius”. **Context:** `notes/RESULTS_STATE.md`, open and settled rows named below; `MPL_16+47+54+44_transcription.tex`, cote 44, scan 008; delta: adds a linear realization method, with no supplied section-fibre calculation. **Register:** LM7 E.23, FLAGGED_149 B9 and LM6 A.22 [Open, returns’ claims]; LM7 C.5 [Proved, return’s claim]; LM7 C.8 [Refuted, return’s claim]; LM7_PUSH E.67 [reviewed, with the qualification recorded below].

LM7 E.23 concerns the image and every fibre of section maps for specified metabelian/depth-two quotients, FLAGGED_149 B9 concerns prime-to-\(p\) point detection, and LM6 A.22 concerns a closed procyclic subgroup with an open normalizer image; all three are explicitly Open in the supplied register.
The maps in B01 and B04 send geometric fundamental-group data to Tate modules and cyclotomic characters, but neither the four supplied context cotes nor cote 14 supplies the omitted definitions and calculations of those three rows, so no new verdict on them follows from this package.
LM7 C.5 [Proved, return's claim] and C.8 [Refuted, return's claim] already record respectively a specific generalized-Jacobian extension calculation and failure of an identification with all weight splittings; the present comparison uses the displayed generalized-Jacobian sequence and does not repeat either conclusion as a newly proved result.
The refereed LM7_PUSH E.67 row concerns a Gaussian norm comparison, and searches of the present pages and context identify no corresponding formula in cote 14.

## R01 — Bibliographic identity of the English reused leaves

**Location:** `pages/MPL_14_002-044_14_scan006.tex`, lines 2–12; scans 004, 008, 010, 012, 014, 016. **Kind:** reading question. **Quote:** “The Brauer group of a ringed space.” **Context:** `MPL_16+47+54+44_transcription.tex`, cote 16, scans 021, 023, 028, 030; notes R8; delta: adds an English sheaf-algebra witness alongside the earlier Kummer/Brauer material. **Register:** no matching result row; searches `Brauer|ringed space|Auslander|separable`.

The title is also the title of B. Auslander's 1966 paper, independently attested in Vitale's published bibliography [Vitale96, reference 1], but the accessible bibliographic record does not establish identity of these particular typescript leaves or their revision.
Their own internal sequence is II.9, III.4–III.7, IV and IV.2, running through scans 016, 014, 012, 010, 008, 006, 004, with unrepresented intervening leaves.
That sequence supplies a provenance question and a reading order for the reused text; the diplomatic fragment retains archive scan order.

## R02 — The missing prime in the first sentence of IV.1's proof

**Location:** `pages/MPL_14_002-044_14_scan004.tex`, line 6; scan 006, lines 6–12. **Kind:** reading question. **Quote:** “if L is in C_1 … L is equivalent to A”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 16, scans 021 and 023; delta: adds a concrete distinction inside the Brauer construction, witnessed by the quotient map sending a central separable algebra to its Brauer class. **Register:** no matching result row; search R02.

The statement of IV.1 on scan 006 uses \(\mathcal C'_1\), while the first proof sentence on scan 004 uses \(\mathcal C_1\); the next displayed stabilization is the proof of the former formulation.
For the real quaternion algebra \(\mathbb H\), the corner algebras at primitive idempotents of \(M_r(\mathbb H)\) and \(M_s(\mathbf R)\) are respectively \(\mathbb H\) and \(\mathbf R\), of real dimensions four and one; an algebra isomorphism preserves these corners, proving that these stabilizations have no isomorphism.
Thus the literal proof sentence would kill a demonstrably nonzero Brauer class, and the internal prime discrepancy remains a reading question rather than a silent correction.

## R03 — External dependencies in the stalk criterion

**Location:** `pages/MPL_14_002-044_14_scan014.tex`, lines 6–30; scan 012, lines 6–28; scan 010, lines 4–19. **Kind:** unproved claim. **Quote:** “we see immediately”; “Theorem III.1”; “[5, Theorem A.2]”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote16 scans021 and023, Brauer passages; the exact local-separability/stalk criterion was not found in the searched context. **Delta:** adds a typed Brauer-theoretic fragment with essential referenced hypotheses outside the supplied leaves. **Register:** no matching result row; searches R03 and R03-exact.

The equivalence between local separability and finite presentation plus central-separable stalks cites III.1, and the proof of separability of \(\operatorname{End}_A(M)\) cites an absent appendix and a tensor-projectivity result.
The actual map printed here is \(M^\vee\otimes_A M\to\operatorname{End}_A(M)\), \(f\otimes m\mapsto[n\mapsto f(n)m]\), where the last multiplication is the scalar-action map \(A\otimes_A M\to M\); this accounts for the source's parenthesized \(f(n)(m)\).
The later tensor-product and base-change arguments apply these stalk identifications, so an edition checking the claims needs the missing III.1, II.2 and references [4], [5], [7], including their finite-presentation hypotheses.

## R04 — The sheaf double-commutant map and the cut-off proof

**Location:** `pages/MPL_14_002-044_14_scan008.tex`, lines 4–16. **Kind:** unproved claim. **Quote:** “is easily seen”; “Since … it is finitely presented”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 16, scan 005, commutant of the graded projectors; delta: adds a sheaf version of a commutant construction with its own explicit morphism. **Register:** no matching result row; search R04.

The proposed isomorphism is \(g:\mathcal L\to\underline{\operatorname{Hom}}_{\mathfrak M^e}(\mathfrak M,\mathcal L\otimes\mathfrak M)\), whose local formula sends \(p\) to \([q\mapsto p\otimes q]\).
Its proof stops during the finite-presentation justification, before the stalkwise comparison needed to apply the cited ordinary-ring double-commutant result.
The earlier context's commutant of the projectors is obtained by \([u,\pi_i]=0\), so both passages can be compared through endomorphisms commuting with a specified algebra action, without identifying their rings or hypotheses.

## R05 — Tensor-Hom and Morita evaluation on the unjoined leaves

**Location:** `pages/MPL_14_002-044_14_scan016.tex`, lines 7–33; scan 004, lines 13–17. **Kind:** unpursued implication. **Quote:** “is an isomorphism for every x”; “the induced map of sheaves, α”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 16, scans 003–005 and 049; delta: adds explicit tensor/Hom evaluation maps beside the earlier endomorphism-algebra constructions. **Register:** WG2 §2.4 #3 [unchecked plan], only as a related algebraic construction; search R05.

The maps are \(\operatorname{End}(M)\otimes\operatorname{End}(N)\to\operatorname{End}(M\otimes N)\), \(f\otimes g\mapsto[m\otimes n\mapsto f(m)\otimes g(n)]\), and \(\operatorname{Hom}_{\operatorname{End}(M_1)}(M_1,M_2)\otimes M_1\to M_2\), \(h\otimes m\mapsto h(m)\).
These formulas explain how the finite-projective hypotheses on the typed leaves feed the Brauer equivalence relation and can be compared with the projectors and matrix blocks in cote 16.
The incomplete definition of \(\psi'\) at the end of scan 016 and the incomplete local-projectivity sentence on scan 004 require further leaves for a complete typescript proof; no category of motives is constructed in either fragment.

## R06 — A shared typescript number with incompatible simple page ordering

**Location:** `pages/MPL_14_002-044_14_scan022.tex`, lines 4–22; scan 020, lines 4–18. **Kind:** reading question. **Quote:** “n° 391”; “5. Chambres dans un espace affine.” **Context:** `MPL_16+47+54+44_transcription.tex`, cote 54, scan 008, “−13−”, “n° 391”, Corollaries 2–3; notes D15; delta: adds an exact local join and a pagination question. **Register:** no matching result row; search R06.

Scan 022 ends with \(s'(x)-t=s(x-t)=s(x)+t\), and scan 020 begins with its consequence \(s'(x)=s(x)+2t\), so these two leaves join in the order 022→020.
The context's cote 54 scan 008 shares “n° 391” but its typed “−13−” already gives consequences of Proposition 10, whereas cote 14 “−14−” and “−15−” contain Proposition 9 and the opening chamber lemma.
Which version or pagination accounts for these facts remains a provenance question; the common number and subject alone do not establish a three-leaf consecutive typescript.

## R07 — The two reflection formulas have an explicit common affine map

**Location:** `pages/MPL_14_002-044_14_scan022.tex`, lines 11–22; scan 020, lines 6–8. **Kind:** own idea. **Quote:** “s's est la translation 2t”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 54, scan 008; notes D15; delta: adds the reflection formula preceding the context's chamber assertions. **Register:** no matching result row; search R07. **Confidence:** high, from the displayed calculation using the source's stated nonisotropic normal vector.

With origin on \(H\), choose a normal vector \(u\), and write \(t=bu\), \(x=h+au\), where \(h\in H\); the two reflections are \(s(h+au)=h-au\) and \(s'(h+au)=h+(2b-a)u\).
Their composite sends \(h+au\) to \(h+(a+2b)u=x+2t\), including \(b=0\), exactly the translation asserted across scans 022–020.
This calculation fixes the direction of the composite through the actual maps and adds no reflection-group hypothesis to the locally finite arrangements on the neighbouring typed page.

## R08 — The chamber lemma's unfinished intersection argument

**Location:** `pages/MPL_14_002-044_14_scan020.tex`, lines 12–18. **Kind:** own idea. **Quote:** “C=∩D_H(C)”; “Pour tout H … il est clair”. **Context:** `MPL_16+47+54+44_transcription.tex`, cote 54, scan 008, first two paragraphs; notes D15; delta: adds an explicit completion of the earlier step used by the context's wall corollaries. **Register:** no matching result row; search R08. **Confidence:** high, from convexity and the stated locally finite real hyperplane arrangement.

Fix \(x\in C\); for every \(y\in\bigcap_H D_H(C)\), the segment \([x,y]\) lies in each convex open half-space \(D_H(C)\), hence avoids every hyperplane and connects \(y\) to \(C\) inside the complement.
This proves the reverse inclusion to the immediate \(C\subseteq\bigcap_H D_H(C)\), completing the cut-off argument on the stated real affine space.
The source's \(S'\) in the statement and \(S\) in its proof remain literal, and the context's later wall argument is compared by this exact inclusion.

## Root primary bibliography and verification scope

- **Tate66:** Tate, J. (1966). *Endomorphisms of abelian varieties over finite fields*. Inventiones Mathematicae 2, 134–144. https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf — §1, main theorem; §3, divisor correspondence comparison. Opened/read through the primary PDF, web refs turn17view0, turn34view1.
- **Mochizuki99:** Mochizuki, S. (1999). *The local pro-p anabelian geometry of curves*. Inventiones Mathematicae 138, 319–423. https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf — introduction Theorem A; Corollary 15.5; distinction of full profinite and geometrically pro-p notation checked. Web refs turn17view1, turn30view4.
- **Mochizuki03:** Mochizuki, S. (2003). *The absolute anabelian geometry of hyperbolic curves*. https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf — Lemma 1.3.1 and Corollary 1.3.2; the use of finite-cover Jacobians was read, not inferred from a title. Web refs turn30view1, turn34view4.
- **DM18:** Deligne, P., & Milne, J. S. (1982; corrected and updated text dated 2018). *Tannakian categories*. https://www.jmilne.org/math/xnotes/tc2018.pdf — 2.8, 2.11, 2.23, 4.22–4.23, 5.1; updated edition identified as such. Web refs turn44view0, turn45view3, turn49view0; searchable parallel primary text turn17view2.
- **Pal11:** Pál, A. (2011). *The real section conjecture and Smith's fixed-point theorem for pro-spaces*. Journal of the London Mathematical Society 83, 353–367. https://arxiv.org/pdf/0905.1205 — primary author manuscript v2, Theorem 1.3 and Example 5.8; used only for the stated proper curves. Web refs turn34view0, turn42view3.
- **Stix12:** Stix, J. (2012 author manuscript). *On cuspidal sections of algebraic fundamental groups*. https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf — (3.1), Proposition 16, Definitions 26 and 29, Theorem 30; characteristic-zero scope read at the opening. Web refs turn45view0, turn46view0, turn46view1, turn46view3.
- **Vitale96:** Vitale, E. M. (1996). *The Brauer and Brauer-Taylor groups of a symmetric monoidal category*. Cahiers de Topologie et Géométrie Différentielle Catégoriques 37, 91–122. https://www.numdam.org/item/CTGDC_1996__37_2_91_0/ — bibliography entry 1 only, as an independently published bibliographic lead; Auslander's article itself was not available for textual collation. Web ref turn44view1.
