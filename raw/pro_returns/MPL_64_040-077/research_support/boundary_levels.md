# Research support: modular boundary and congruence levels

Prepared after transcription freeze, 2026-11-17 23:04:47 UTC. Model: GPT-6 Astra Pro; effort not exposed. Only saved transcription and supplied context were read; no images were inspected and no transcription was modified. Context statuses remain unreviewed return claims unless this report explicitly records a fresh check.

## Proposed note items

### BL01 — The announced place at infinity is not constructed here

**Cote/scan:** 64/058–077, especially 071, 075, 077. **Kind:** reading question. **Source words:** “un morphisme lisse de dim relative 1”; “image de l'élément $0_E$”; “épinglage de Legendre”. **Context:** `context/MPL_149_091-136_notes.md`, RN099-03 and RN100-01, reporting 149/099–101; `context/LM_140-3_text.tex`, 025. **Registers:** README's B5/place-at-infinity planning question, unchecked; **LM6 F.43**, Proved in its unreviewed return.

The tangent line in these pages belongs to a marked ramification point on a smooth curve, and in the elliptic application it is $T_{E,0}$, whereas a modular cusp requires degeneration of the elliptic curve and a parameter on its moduli base. No nodal family, Tate parameter, or modular-cusp inertia calculation is constructed in the inspected 64/058–077 pages; the branch label $\infty$ in their projective-line formulas does not supply one. RN099-03 proposes a Tate-cusp test for the question it reports at 149/099–100, and LM 140-3/025 explicitly names the “point à l'infini de $M_{1,1,\mathbb Q}$”, but that is a target rather than a result of this excerpt. These pages therefore do not fulfill the announcement, although 071–077 provide finite-cover and tangent-rigidification tools that could contribute to a later construction.

### BL02 — A concrete bridge to the earlier tangent-splitting problem

**Cote/scan:** 64/071–074. **Kind:** unpursued implication. **Source words:** “via l'hom norme locale”; “une équivalence de catégories”. **Context:** `context/LM_140-2_text.tex`, 073, 077–079; `context/MPL_149_091-136_notes.md`, RN095-01 and RN096-01. **Registers:** **LM6 F.43**, Proved in its return, not independently re-proved; **WG2 §1.1 #6**, unchecked plan.

The data $T'^{\otimes n}\simeq T$ and $\mu_n\hookrightarrow G$ give a concrete relative formulation to compare with LM 140-2/077–079, where first-order parameters determine a geometric subfamily of Kummer splittings. This is particularly close to 140-2/078's deferred request to explicate behavior under morphisms and “la relation avec la norme des 1-formes différentielles”. The current equivalence-of-categories assertion does not construct a compatible inverse system over all $n$ or identify the local functor with LM6 F.43's global boundary system. Tangent/conormal duality must be respected: the earlier source uses $\mathfrak m/\mathfrak m^2$, whereas these pages write tangent lines.

### BL03 — A precise next test for the modular-cusp question

**Cote/scan:** 64/075–077. **Kind:** own idea. **Confidence:** high as a proposed distinction and test, because the tangent data live on different geometric objects; no comparison theorem claimed. **Source words:** “$t\in\Sigma_J^*=\Sigma_J\setminus D_J$”; “pour $E$ variable”. **Context:** `context/LM_140-2_text.tex`, 517–520; `context/MPL_149_091-136_notes.md`, RN099-03, reporting 149/099–100. **Registers:** **LM6 F.43** (Proved claim); **EXIT_TOWER E.24** (Open).

One can test the announced cusp by allowing the fourth branch point $t$ to approach $D_J$, constructing the nodal or generalized elliptic family, and comparing a nonzero normal parameter at its boundary with the smooth-locus pinning $\kappa:T_0\to T_{E,0}$. This would add the missing base-degeneration comparison; the Tate model proposed by RN099-03 is a separate local model against which to test it. Neither $\kappa$ nor a primitive fourth root already specifies a nodal smoothing parameter, so an actual map between these torsors is required. The proposal does not prove LM6 F.43 or determine the image in EXIT_TOWER E.24.

### BL04 — The quotient leaves a residual sign gerbe

**Cote/scan:** 64/058–063, 075. **Kind:** unpursued implication. **Source words:** “à isom (non unique) près loc. pour la top. étale”; “équivalence de catégories-groupoïdes”. **Context:** `context/LM_140-2_text.tex`, 518–520, especially 519's “presque une équivalence”. **Registers:** **LM2 C.r3** (Proved claim, unreviewed); **EXIT_TOWER E.24** (Open).

The quotient $E\to E/\{\pm1\}$, the three nonzero two-torsion images, and $t$ restate the four-pointed-line construction of LM 140-2/518, while the tangent square root on 64/075 adds data sensitive to the remaining sign. The qualification “non unique” on 063 agrees with 140-2/519's explanation that inversion acts trivially on the quotient object, necessitating a distinction between the elliptic groupoid and its $\pm1$-rigidification. This supports keeping actual, projective, and outer actions separate as LM2 C.r3 claims, but computes none of their arithmetic images. The comparison is between supplied passages, not a proof of the register result.

### BL05 — A direct construction of the zero-sum lift torsor

**Cote/scan:** 64/066–068, (40)–(47). **Kind:** own idea, checked reconstruction. **Confidence:** high from the reference module and basis calculation below. **Source words:** “un torseur”; “à trace nulle”. **Context:** `context/LM_140-2_text.tex`, 518–520, 567; `context/LM_140-3_text.tex`, 022–024. **Registers:** **LM2 C.d1** (Known claim), not proved by this calculation; **LM4_SUCCESSOR B.38** (Open).

For $J=M_0\setminus\{0\}$, define $R_J=\ker(\sum:(\mathbb Z/4)^J\to\mathbb Z/4)$ and $r_j=3e_j-\sum_{k\in J}e_k$; the reduction of $R_J$ identifies canonically with $M_0$, the $r_j$ sum to zero, and any two form a basis. A zero-sum lift $j\mapsto m_j$ therefore defines a unique isomorphism $R_J\simeq M$ inducing the identity on $M_0$, whose relative automorphism group is $1+2\operatorname{End}_{\mathbb F_2}(M_0)$. This proves the claimed relative torsor description by an étale-local calculation equivariant under permutations of $J$, and explains why the absolute marking (42) additionally requires a trivialization of $J$. It provides a finite level-four construction, not invariance of arbitrary congruence kernels.

### BL06 — The face forgets simultaneous sign

**Cote/scan:** 64/068–069, (47)–(48). **Kind:** unpursued implication, checked. **Source words:** “(48) définit une face”. **Context:** `context/LM_140-2_text.tex`, 519–520, 567; `context/LM_140-3_text.tex`, 176–178. **Registers:** **LM2 C.r3** (Proved claim).

For $M=(\mathbb Z/4)^2$ with the three nonzero reductions fixed, there are sixteen zero-sum lifts $J\to M$ but eight faces of $(M\setminus M_0)/\{\pm1\}$, with exactly two lifts per face. If $P+Q+R=0$, changing signs preserves the equality only when no signs or all signs are changed, because the only zero-sum subsets of the three nonzero vectors of $\mathbb F_2^2$ are the empty set and the whole set. Thus a face remembers the relative marking modulo simultaneous inversion: the forward assertion on 069 is correct, but a converse identifying a face with the full frame (42) on fixed $M$ would require qualification. Exhaustive enumeration in `level4_certificate.py` checks these counts and fibers.

### BL07 — Full, symplectic, and projective markings differ

**Cote/scan:** 64/066, 069. **Kind:** own idea, checked. **Confidence:** high from exhaustive enumeration and the determinant rule for pairings. **Source words:** “la donnée d'un iso”; “une section de $\mu_4^*$”. **Context:** `context/LM_140-2_text.tex`, 519–520, 567–570; `context/LM_140-3_text.tex`, 022–026, 176–178. **Registers:** **LM2 C.r1**, **C.r3** (Proved claims); **C.r2** (Refuted claim, corrected square-class assertion).

Frames on a fixed $M$ form a torsor under $\operatorname{GL}_2(\mathbb Z/4)$ of order $96$, while prescribing a primitive alternating-pairing value gives a torsor under $\operatorname{SL}_2(\mathbb Z/4)$ of order $48$; quotienting the respective frame sets by $\pm1$ gives $48$ and $24$. Over a fixed mod-two marking the corresponding counts are $16,8,8,4$, so the inserted $\mu_4^*$ on 069 must be interpreted as a pairing/cyclotomic datum with the object being counted specified. Since $\det(-I)=1$, a primitive pairing value does not recover the sign forgotten by a face. These are frame counts on fixed $M$: in the moduli groupoid allowing elliptic-curve isomorphisms, $(E,\alpha)$ and $(E,-\alpha)$ are isomorphic via $[-1]$, consistent with 140-2/567's action through $\Gamma'_4=\Gamma_4/\{\pm1\}$.

### BL08 — Finite level-four geometry does not prove B5 at all levels

**Cote/scan:** 64/065–069. **Kind:** reading question. **Source words:** “le morphisme $f_{2^n}^t$”; “Détermination de $M_{11}(4)$”. **Context:** `context/LM_140-3_text.tex`, 022–026, 176–178; wider ranges are locators in `context/LM2_CONGRUENCE_ROWS.md`. **Registers:** **LM2 C.d1** (Known claim), **C.r1**, **C.r3** (Proved claims), **C.r2** (Refuted claim), all unreviewed.

The pages geometrize two- and four-torsion and observe that iterated multiplication-by-two quotients yield $2^n$-torsion information, but do not define a $GT_0$ action, formulate preservation of every projective congruence kernel, or construct compatible full markings for arbitrary $N$. The inspected LM §39 passages distinguish the full profinite modular group from its congruence quotient and the cyclotomic character from its outer square-class image. Therefore the current finite geometry neither establishes nor refutes LM2 C.d1 or C.r1–C.r3, whose supplied statuses remain unchanged. A primitive fourth root records only the relevant mod-four cyclotomic datum, not an entire adelic multiplier.

### BL09 — B.38 and the other open image problems remain open

**Cote/scan:** 64/066–069. **Kind:** reading question. **Source words:** “$M={}_4E$”; “module loc. libre de rg 2”. **Context:** `context/LM_140-3_text.tex`, 024–026, 176–178; `context/notes/RESULTS_STATE.md`, rows below. **Registers:** **LM4_SUCCESSOR B.38**, **EXIT_TOWER E.24**, **LM4 D.12**, all Open claims.

The exact B.38 row calls $\mathcal K_5=1$ “the main unresolved assertion” and leaves the level-seven and level-eleven kernels undecided, with quotient compactifications of genera three and twenty-six. The level-four construction does not settle any of them, since the relevant higher levels and profinite centralizers do not occur in the excerpt. It likewise does not determine EXIT_TOWER E.24's arithmetic outer image or LM4 D.12's torsion in full $\widehat{GT}_0$. LM 140-3/178 expressly leaves characterization of the arithmetic subgroup inside the larger loop-automorphism group for later.

### BL10 — Legendre pinning detects the central sign

**Cote/scan:** 64/075–077. **Kind:** unpursued implication, checked at the line level. **Source words:** “deux, différant par le signe”; “$T=T_{E,0}\xleftarrow{\kappa}T_0$”. **Context:** `context/LM_140-2_text.tex`, 519; `context/LM_140-3_text.tex`, 176–178. **Registers:** **LM2 C.r3** (Proved claim, not re-proved).

At fixed $J,t,Q_0,\alpha$, compatible isomorphisms of the square-root lines differ by $-1$, and inversion on $E$ induces $-1$ on $T_{E,0}$. A chosen $\kappa$ therefore detects the central inversion invisible to the four-pointed quotient and the Weil-pairing value. The source itself adds “formant un torseur sous $\mu_2$”, giving the correct general-base interpretation of “exactement deux” as a torsor or geometric-fiber statement rather than two guaranteed global sections. No canonical identification with modular-cusp tangential sections is supplied here.

### BL11 — The two trace-zero conditions are different

**Cote/scan:** 64/066–068, (41), (44), (47). **Kind:** reading question, checked algebraically. **Source words:** “qui soit à trace nulle (rel. à $S$)”. **Context:** `context/LM_140-2_text.tex`, 568 (68), “matrices à trace nulle”; `context/LM_140-2_notes.md`, R14, a prior claim. **Registers:** **LM2 C.d1** (Known, unchanged); **LM4_SUCCESSOR B.38** (Open, unchanged).

On 64/068, “trace nulle” means the sum of a $J$-indexed triple in $M$, whose lifts form a sixteen-element torsor under all of $\operatorname{End}_{\mathbb F_2}(M_0)$. In LM 140-2/568 it means $\operatorname{tr}(A)=0$ for a matrix, since $\det(I+2A)=1+2\operatorname{tr}(A)\pmod4$, giving an order-eight determinant-one congruence kernel. Quotienting that kernel by $\pm I$ gives order four, matching the four faces at fixed primitive pairing value and mod-two marking. Identifying the two uses of “trace zero” directly would therefore conflate full and symplectic level structures.

### BL12 — The earlier Jacobi–conic question remains partly unanswered

**Cote/scan:** 64/066–069, 075–077. **Kind:** unpursued implication. **Source words:** “Détermination de $M_{11}(4)$”; the ellipsis ending 069. **Context:** `context/LM_140-2_text.tex`, 569–570 (70)–(73), “Pour bien faire, il faudrait expliciter la relation”; `context/LM_140-2_notes.md`, R16–R23, S6–S8, prior claims. **Registers:** B5 unchecked plan; **LM2 C.d1**, Known claim; **LM4_SUCCESSOR B.38**, Open.

LM 140-2/569 asks for the equivariant trace-zero quotient, expects the order-24 octahedral group and a Fermat conic, and 570 asks to relate unit solutions modulo common scaling to Jacobi rigidifications with $e_1\wedge e_2=[i]^{-1}$. The current torsor and face construction supplies a geometric part of that relation, with counts matching 140-2/567–568 and the primitive-root insertion matching the base $\mathbb Z[1/2][i]$. It does not in 066–069 exhibit the universal open-conic isomorphism, fix the convention $[i]^{-1}$, or prove the proposed canonicity; the face-to-frame sign must be interpreted at the correct moduli-groupoid level. This is an exact B5 bridge but changes none of the all-level or higher-kernel statuses.

## Elementary proof supplement

For BL05, work étale-locally with $J=\{1,2,3\}$. In
$$
R=\ker((\mathbb Z/4)^3\xrightarrow{\sum}\mathbb Z/4)
$$
take $r_1=(2,-1,-1)$, $r_2=(-1,2,-1)$, $r_3=(-1,-1,2)$. They sum to zero; the first two have determinant $4-1=3\bmod4$ in the basis $(e_1-e_3,e_2-e_3)$ and form a basis. The mod-two sum-zero plane complements the diagonal line of $\mathbb F_2^J$. Under $\mathbb F_2^J/\mathrm{diag}\to M_0$, $e_j\mapsto j$, the reduction of $r_j$ maps to $\sum_{k\ne j}k=j$. Thus the identification is canonical, and each zero-sum lift determines a unique relative isomorphism $R\to M$. Permutations of $J$ permute the $r_j$, which gives descent.

The relative automorphism group consists of $I+2A$, with $(I+2A)(I+2B)=I+2(A+B)$, hence is the additive group $\operatorname{End}(M_0)$. Direct expansion gives $\det(I+2A)=1+2\operatorname{tr}(A)\pmod4$. The full lift torsor therefore has sixteen elements; a determinant-one restriction has eight. This verifies BL11 without using a prior note's proof as established.

For BL06, each nonzero reduction has four lifts, two modulo sign. The first two entries freely determine a zero-sum triple, giving sixteen possibilities. For any face choose representatives $P_j$; their sum lies in $2M$, and changing signs changes the sum by $2\sum_{j\in A}P_j$. The map $\mathbb F_2^3\to M_0$ on sign choices is surjective with kernel the simultaneous-sign line, so every face has exactly two zero-sum lifts. Hence the face quotient is $P_M/\{\pm1\}$.

For BL07, an alternating pairing satisfies $e(gP,gQ)=e(P,Q)^{\det g}$. Six mod-two bases with sixteen lifts each give $|\operatorname{GL}_2(\mathbb Z/4)|=96$, half with determinant one. The central $-I$ has determinant one and acts freely on frames, giving quotient orders $48$ and $24$. In the elliptic moduli groupoid, $[-1]$ identifies $(E,\alpha)$ with $(E,-\alpha)$; it is not a nontrivial automorphism of a fixed fully marked object when the marking is fixed pointwise. No global representability or congruence-kernel theorem is claimed.

For BL10, differentiating $m\circ(\mathrm{id},[-1])=0$ at the identity of the group law gives $1+d[-1]=0$, hence $d[-1]=-1$. For two square-root lines, the sheaf of isomorphisms compatible with specified square identifications is a $\mu_2$-torsor; geometric fibers have two elements, whereas global sections require the torsor to be trivial.

## Exact LM2 register assumptions

Every row below is explicitly an unreviewed return claim in `context/LM2_CONGRUENCE_ROWS.md`. No row changes status in this subtask.

| ID | Return status | Exact assertion used | Supplied source locator |
|---|---|---|---|
| LM2 C.r1 | Proved | Arithmetic outer congruence image is units modulo squares at every level | LM 140-3 §39, scans022–024 |
| LM2 C.r2 | Refuted | Unique multiplier is lost on outer congruence actions; corrected square-class statement | LM 140-3 §39, scans025–026 |
| LM2 C.r3 | Proved | Genuine and outer arithmetic actions have different correctly typed images | LM 140-3 §§39,45, scans022–026,176–178 |
| LM2 C.d1 | Known | Every actual GT0 loop automorphism preserves all projective congruence kernels | LM 140-3 §39/021–030; §44/150–168; §46/198–202,218–219 |

## Coverage limits

- The original cote149 text/images were not supplied in context; `MPL_149_091-136_notes.md` is a secondary record and lead. Its Tate-cusp and good-reduction claims were not re-certified.
- Primary working-text passages actually read: `LM_140-2_text.tex` scans073,077–079,517–522,567–570; `LM_140-3_text.tex` scans021–026,176–178,198,202,218–219. The table's wider §44 range and unread portions of §§39,46 are locator-only, not a full proof audit.
- Earlier notes R12–R23 and S5–S8 in `LM_140-2_notes.md` were inspected after the primary text; their proof and canonicity claims remain distinguished from this report's fresh checks.
- Current frozen text read: 058–069 and 071–077. The algebra of 064–065 was read for scope only and not recomputed; root owns those checks. The combined text was searched for cusp, infinity, degeneration, modular, level, and congruence language. Root's visual reading controls transcription; this agent inspected no image.
- B.38's exact supplied row was reread: it explicitly leaves $\mathcal K_5=1$ unresolved and levels seven/eleven undecided. No status change is claimed.
- The actual exhaustive finite-module certificate is `level4_certificate.py` with output `level4_certificate.txt`. Events are in `boundary_levels_checks.tsv`; none were added to the shared main check log by this agent.
