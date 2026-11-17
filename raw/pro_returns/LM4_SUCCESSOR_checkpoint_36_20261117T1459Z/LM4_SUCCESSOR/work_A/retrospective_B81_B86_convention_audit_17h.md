# Retrospective convention audit of B81–B86

Date: 2026-11-16. Status: **PASS for the existing intrinsic Birman marking.**

This is a bounded audit of the concrete chronology issue discovered in the
new symmetric-family computation. It does not reprove unrelated topology,
normal-generation statements, or any syzygy conclusion. No old certificate
or accepted formal fragment was modified.

## 1. The two conventions must not be identified

For a chronological list of crossings (W), the directly calibrated
geometric push is

\[
 \operatorname{Push}(W)=\operatorname{art}(\operatorname{rev}W),
 \qquad
 \operatorname{Pull}(W)=\operatorname{art}(-W).
\]

Here (-W) negates each crossing without reversing its order. The helper
`art` postcomposes its current images by each elementary Artin map. Thus
`art(W)` is not the geometric push in the calibrated positive-cut basis.
The newly constructed symmetric package originally mixed these conventions
when comparing a geometrically defined endpoint involution with converted
braid actions. Its initially converted arrays require the already recorded
correction; its raw crossing lists, signs, paths, and exact endpoint geometry
remain unchanged.

The older B81 and w-pencil packages do something different. They **define
their fiber coordinates** using the inverse of a distinguished-meridian
conjugator in the faithful Artin representation. They do not identify
`art(W)` with geometric push in the positive-cut basis. That deliberate
coordinate choice compensates for the order convention.

## 2. Intrinsic Birman marking and its groupoid naturality

Let (W) be a braid path with distinguished source strand going from
position (s_0) to position (s_1). Write (A_W=\operatorname{art}(W)),
viewed algebraically as a map from the endpoint meridian group to the
initial meridian group. If

\[
 A_W(x_{s_1})=h_Wx_{s_0}h_W^{-1},
\]

let (q_W) be (h_W) after deleting the initial distinguished generator.
Its value is independent of the harmless ambiguity of multiplying (h_W)
by a power of (x_{s_0}). Let \(\overline A_W\) be the induced map after
deleting the distinguished generator at each endpoint. Set

\[
 \Phi(W)=q_W^{-1},\qquad
 T_W=\operatorname{Inn}(q_W^{-1})\overline A_W.
\]

For composable chronological paths (W,V), the literal Artin composition
gives

\[
 q_{WV}=\overline A_W(q_V)q_W,
 \qquad
 \Phi(WV)=\Phi(W)\overline A_W(\Phi(V)).
\]

On the strand-deletion kernel, \(\overline A_W=1\), so **\(\Phi\) is a
homomorphism**. The old producers verify that its values on the standard
pure kernel braids form a Nielsen basis of the rank (n-1) free group.
Consequently this is an isomorphism of the actual Birman kernel: the kernel
is free of rank (n-1), the displayed images give surjectivity, and a
surjective endomorphism of a finite-rank free group is injective.

For any endpoint kernel loop (P\), the same identity gives

\[
 \boxed{\ \Phi(WPW^{-1})=T_W(\Phi(P)).\ }
\]

This is exactly the action and local-prefix transport formula used by
`extract_tangent_bundle_fiber.py`, `extract_w_pencil_fiber.py`, and
`extract_w_local_markings.py`. It holds for changing distinguished
positions as well as for closed source braids. Therefore the local
whiskers are not a place where an uncorrected geometric-push convention
reenters the older calculation.

There is also an explicit comparison with the calibrated geometric
coordinates. For a pure kernel braid (P\), take the distinguished
conjugator in \(\operatorname{Push}(P)\), delete the source generator,
and denote the resulting geometric fiber word by \(\Psi(P)\). The two
kernel isomorphisms determine a Nielsen map (C_s\) at every source
position, with (C_s\Psi(P)=\Phi(P)\). If (G_W\) is actual geometric
back-transport normalized at the moving source point, then

\[
 C_{s_0}G_W=T_WC_{s_1}.
\]

The new verifier checks this entire equality on every fiber generator for
every old w-pencil local whisker. It is not a search over conventions.

## 3. Exact scope of the new independent certificate

Producer:

`work_A/code/audit_old_birman_groupoid_convention.py`

Genuine output and complete data:

`work_A/code/audit_old_birman_groupoid_convention.out`

`work_A/code/audit_old_birman_groupoid_convention.err` (empty)

`work_A/old_birman_groupoid_convention_audit.json`

The evaluator does not import or execute a crossing producer. It composes
elementary substitutions independently by reverse reading and left
substitution, and hashes every stored input. It reads the actual raw braid
paths and existing fiber/local/source data without changing them.

The completed run checks:

- **576** intrinsic kernel-generator naturality identities: all twelve
  generators in both directions for all twenty-four local prefixes;
- **288** geometric/Nielsen transport identities: all twelve generators
  for those same twenty-four prefixes;
- **264** actual old/filled source-action identities: all twelve kernel
  generators, both directions, for all eleven old or filled base loops;
- all **thirteen** literal source-crossing fiber words;
- both inverse Nielsen changes for every distinguished endpoint position
  occurring in those paths;
- the exact local positive (q\)-meridian. Its raw braid is
  \(\sigma_{10}^2\), its intrinsic local word is \(x_{10}^{-1}\), and
  common-prefix transport followed by the source-adapted basis gives
  **\(b^{-1}\)**.

Elapsed time in the genuine run: 19.739682 seconds. These checks confirm
the geometric interpretation of the already stored algebra, rather than
merely repeating its action/inverse identities.

The companion DE audit is
`work_DE/next_marginal_source/check_B81_pointed_compensation.py`, with
genuine `.out` and `B81_pointed_compensation.json`. It independently
supplies the same explicit Nielsen compensation for B81's
last-source-strand tangent-bundle model: eighty-four action/inverse
comparisons, four actual source meridians, and fourteen inverse Nielsen
compositions all pass. In
particular, the geometric distinguished conjugators of its seven standard
source braids give the geometric cut basis, whereas the old inverse
conjugators give its stored negative triangular Nielsen basis. The old
actions intertwine these bases. That audit is separate from the present
all-prefix w-model certificate.

## 4. Which formal assertions use these words

| Formal statement | Convention-dependent input | Audit conclusion |
| --- | --- | --- |
| B81 | Four source seeds, six source actions, all literal orbit/free-factor computations, in the intrinsic seven-generator fiber marking | The inverse-conjugator map is the intended Birman isomorphism. The separate geometric cut comparison requires its Nielsen change; no stored word reversal is called for. |
| B82 | Ordered two-sheet source lifts, the even old operators, opposite-family source conjugations, and source witnesses inherited from B81 | These use the same intrinsic marking consistently. Cover characters and geometric filling maps are independent of the geometric-push identification. |
| B83 | Actual w-source words, all three selected based restrictions and their signed (b\)-conjugators, actual local (w=1\) marking | Full intrinsic and geometric/Nielsen comparisons pass. The detector sign \(\chi_b=-\operatorname{wind}((vw-1)/(w-1)^2)\) remains correct because the positive local loop is literally (b^{-1}\). |
| B84 | Literal source corrections (v_3,v_4\), both basis substitutions, and all five corrected positive source operators | Every input lies in the same verified w-marking; the chronology issue does not alter the corrections or their source membership. |
| B85 | Identification of the selected tangential local inertia with (b\), and arithmetic translates of the B83/B84 subgroups | The local (q\)-loop comparison was rechecked through the actual common prefix. Its orientation and hence the literal cyclotomic (b\)-formula are unchanged. The geometric tangential-basepoint proof is independently unaffected. |
| B86 | The four retained product source words, normalized negative-node relations, positive-triple source corrections, and resulting strips | These derive from the same actual local groupoid transport, not from an uncorrected geometric push. All local transports and source actions used in their derivation are unchanged. |

The related B88 zero-source calculation also inherits the same w-marking,
so this particular convention risk does not invalidate its inputs.
Statements proved from topology without these converted braid words—such
as the actual filled-surface fixed subgroup and the intersection/compact
fiber-product comparisons—are independent of this risk in any event.

## 5. Required separation for future computations

The current corrected symmetric package uses a **geometric cut marking**.
The earlier B81–B86 packages use the **intrinsic inverse-conjugator
marking**. A comparison between them must insert the explicit Nielsen
change; raw arrays in the two markings must not be equated.

The initial symmetric converted arrays remain preserved as failed
convention artifacts. Only their corrected descendants should enter new
paired Fox or old-action computations. Nothing in this retrospective
audit computes the complete old-base/deck translated node module, its
syzygies, the map \(\kappa\), or the main source-kernel equality.
