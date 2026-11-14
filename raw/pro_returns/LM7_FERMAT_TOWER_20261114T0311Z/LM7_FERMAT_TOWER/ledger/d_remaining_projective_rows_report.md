# D.61: a further actual arithmetic lift and the surviving self-wedge classes

## Proved result and exact scope

D.61 constructs a continuous peripheral automorphism of the actual marked source

\[
X_{61}=X/\mathcal J_{61},\qquad
X=\widehat B/(R_{50}\cap L_2).
\]

It retains the complete D.57 action, its compatible normalized conjugators, the prescribed `W_h` action, the literal normalized parameter, and every metabelian and CM comparison already proved through that projection. Its multiplier is one, it fixes the marked cusp `t`, and it induces the identity on the actual finite arithmetic group `G=G3`.

The homology action is replaced only on the two size-twelve character orbits pulled back from `A_*`. The precise replacement is `T61=(1-e)T60+e`. It has the identities `f_i T61=f_i` and `T61 f_i=f_i+(1-e)T60 f_i`. These equations prove preservation of the required projector kernels. The statement does not replace them with an unsupported assertion that the projector images are fixed or that the chosen old representative extends unchanged.

The new retained central direct summand has dimension **22,016** and **50 coinvariants**. It consists of seven previous self blocks and twelve new cross blocks. Its norm and compactification maps are injective, so D.55's exact arithmetic orientation identity proves that its actual boundary class is zero. The specified small-character residual decreases from `353792/612` to **`331776/562`**, where the two entries are module and coinvariant dimensions.

The full profinite realization problem remains unresolved. This statement makes no cofinality assertion and does not infer a full profinite lift from the new quotient.

## Literal arithmetic matrices and integral maps

The input is the frozen D.60 order-46656 marked quotient `A_* semidirect Q`, with its actual map to the solved order-3888 quotient. D.60.10 identifies these coefficient blocks with those of the full arithmetic source by odd-kernel homology. The source to which the theorem applies is therefore the original `G3` source, with those exact maps.

The first program checks the obstruction to reusing the previous whole-module projectivity argument. For each size-twelve orbit, the oriented stabilizer is `S4=V4 semidirect S3` and its Sylow-two subgroup is `D8`. Source affine, cusp and compact dimensions over `F4` are respectively `96,48,48`, with Sylow norms of ranks `10,6,4`; projectivity of all three would require `12,6,6`. The target compact module has dimension four and zero norm. The compact ambient module is thus proved nonprojective.

The actual projective part is nevertheless explicit. Four nontrivial `C3`-eigenvectors in the twelve-dimensional `V4` top are chosen using the semilinear trace-one involution. Their induced eight-column submodules give a rank-32 projective compact submodule. The program retains all embeddings, affine lifts, the exact small-image zero, all cusp annihilations, and every stabilizer action. Four coinduced eigenfunctionals give a retraction; a trace-one semilinear correction makes it commute with the exchange. The remaining sixteen-dimensional compact module has zero complete `D8` norm and therefore no projective direct summand.

Each included projective module is defined integrally by the same induction and exchange formulas. Projectivity lifts its prescribed finite compact inclusion. The inclusion is saturated because its reduction is injective. The dual of this projective lattice is projective, so the specified finite dual retraction lifts; inversion of its composite gives an exact integral splitting with precisely the recorded reduction. This argument does not assume that the ambient compact lattice is projective.

Every equivariant map from these projective summands to the small affine module vanishes: the generators have nontrivial `C3` eigenvalue while `C3` acts trivially on the target. Integral separatedness and projective lifting of Hom reduction give the same vanishing over `Z2`. Projectivity then lifts the compact inclusions to the prescribed affine columns, adjusting by twice a lifted error. The resulting integral idempotents kill cusps, inject under compactification, and have zero small image. Each global summand has `Z2` rank `12*2*8=192`; there are eight summands.

## Why the row replacement is an automorphism

Write the actual compact lattice as `P=E direct-sum M`, using the constructed splitting. The reduction of `M` has no projective direct summand. Any endomorphism of that reduction factoring through a projective module is nilpotent: its invertible Fitting summand would split off from a projective module and hence itself be projective.

For the old automorphism and its inverse, the lower-right block multiplication gives `D'D=1-C'B`. The correction `C'B` factors through the projective `E`, so the right side is invertible modulo two. Thus `D` is invertible integrally. The affine complementary diagonal fixes the cusp lattice and induces `D` on the compact quotient, so it too is invertible. In the affine splitting, the new row-replaced map is exactly the triangular matrix with blocks `1,0,C,D`.

Its difference from the old action is the actual homology map `e(1-T60)`, taking values in a projective active-character lattice and killing cusps. Odd averaging gives the full inflation-restriction isomorphism. The local order-two, order-three and cusp cyclic norm sequences give actual conjugator corrections with zero cusp derivation. These lie in the exact kernel of `Y -> X_*`, and hence retain the original D.57 conjugators. This proves realization and generation on the full homology source, beyond a derivation calculation.

## Central lift and comparison kernels

The seven old self blocks have dimension 512 each and two coinvariants each, with norm rank two. Every new cross block has dimension 1536 and three coinvariants, with norm rank three. They are explicit equivariant summands inside the previous remaining kernel. The new left projector identity implies `Pi61 exterior-square(T61)=Pi61`. After compactification, D.55's orientation equation therefore makes the selected norm zero. Both norm and compactification are injective on these summands, so the actual arithmetic coinvariant boundary is zero.

Actual central conjugator corrections in the augmentation image kill its representative while preserving the full homology and D.57 maps. The source map factors through the class-two quotient and is an automorphism by its invertible Frattini action. Alignment on the actual common quotient with the retained full homology and `W_h` component gives the stated fibre-product source.

The exact kernels are

\[
\ker(X_{61}\to X_{60})=\mathcal C_{61},
\quad
\ker(X\to X_{61})=\mathcal J_{61},
\]

\[
\ker(X_{61}\to Y)
=(1-e_\Delta)\mathcal K\oplus\mathcal C_{59}
\oplus\mathcal C_{60}\oplus\mathcal C_{61}.
\]

In the full source,

\[
S_{61}=\{b\in R_{50}:\operatorname{im}_{\mathcal T_2}(b)
\in\mathcal J_{61}\},\qquad
S_{61}/(R_{50}\cap L_2)=\mathcal J_{61}.
\]

A nonzero vector in the stated residual and its actual preimage under `R50 -> Z` prove that this source kernel remains nonzero.

## Proved additional cover maps and their tested limitation

The remaining old self block has four coinvariants and norm rank two. Its two kernel classes are `H05(1)` and `H05(zeta3)`. Each new self block has three coinvariants and zero norm. For each of its four copies, the first size-twelve orbit has basis `H00,H02(1),H05(1)`; the other has basis `H00,H01(zeta3),H05(1)`. Thus the named self-wedge norm kernel has dimension `2+4*3+4*3=26`.

For each of the four actual involution classes of `Q`, the proof constructs an integral intermediate-cover homology map. An order-two lift exists over the odd kernel. Transfer, the projective integral norm isomorphism, and coinvariants give

\[
B_a^{\mathrm{ab},(2)}\longrightarrow U^{H_a}
\longrightarrow E^{H_a}\xrightarrow{\nu_E^{-1}}E_{H_a}.
\]

No division by two occurs. This map restricts to `q_a e` on `K3`, kills cusps and torsion, factors through the actual `Y` subgroup, and is fixed by the constructed action. Its free Kurosh generators lift to a free class-two exponent-four target; all finite factors are sent to one. The target kills `L2`, hence gives an actual map from the corresponding subgroup of `X`. Herfort–Ribes Theorem A-prime proves that the conjugated torsion words are killed as well. The oriented cover relation then proves that the actual boundary is annihilated by

\[
D_a([z])=(\bigwedge^2\bar q_a)\sum_{H_a\backslash G}g z.
\]

The calculation uses the full induced homology modules of ranks128 and192, every cyclic coinvariant column, and every relative-coset-sum column. It verifies the invariant Hermitian-to-exterior identification on all64 columns against every stabilizer action. All four involution classes are included, with sizes `36,3,3,1` and marked representatives `1,314,572,573`.

On the old four-dimensional coinvariant block the divided-norm ranks are `2,2,1,2`, and their joint rank together with the ordinary norm is still two. On every new three-dimensional self block all four maps vanish. Consequently all26 named norm-kernel classes survive these tested, source-defined maps. Their actual arithmetic boundary coordinates are not evaluated by D.61. The next square/commutator exponent-eight investigation must retain this exact remaining kernel.

## Programs, provenance and verification

The four complete programs, with their actual `.out` and `.json` files, are:

1. `d_orbit12_projectivity.py`: exact Sylow projectivity comparison for both actual arithmetic orbits.
2. `d_self_wedge_norm.py`: all eight old self modules, full norms, coinvariant representatives and kernel lifts.
3. `d_orbit12_projective_kernel.py`: all compact/affine inclusions, retractions, finite idempotents, small and cusp maps, full stabilizer actions, all twelve cross norms and eight self norms.
4. `d_self_wedge_divided_norms.py`: all four actual intermediate-cover divided norms on the remaining self modules.

Every program was rerun in its own copied-source directory with exact frozen input certificates. All four complete JSON certificates and complete stdout match after excluding only numeric `elapsed_seconds`. The replay source, stdout and full verification record are in `audit/d61_author_rebuild/`. Every owned script and all inputs remained unchanged during replay. The upstream D.60 arithmetic inputs retain their frozen identities and were independently replayed during the D.60 audits.

The original successful divided-norm run that emitted a Python docstring escape warning is retained under `code/d61_trials/divided_norm_docstring/`. The final source differs only by making that docstring raw; its complete rerun passed. There is no discarded mathematical failure or unrecorded search in this bundle. The Sylow nonprojectivity and undetected self classes are retained as exact limitations.

The final isolated proof uses the main paper's exact preamble, two LuaLaTeX passes, and the existing verified format. All six final110dpi pages were actually viewed. No clipping, overlap, bad equation placement, missing glyph, overfull box or underfull box remains. The 21 equation tags and all statement/proof/display delimiters passed the control lint. The original primary-source Theorem A-prime page was reopened as an actual image, and its complete proof was reread in the retained original OCR.

The full arithmetic source proof is symbolic where the actual group is enormous; the programs verify the exact coefficient matrices supplied by the proved quotient and transfer maps. The program outputs are not presented as a direct enumeration of that enormous group. Parent and peer audit status remains separate from this author verification.

## Integrated review and original-task scope

D.61 constructs the integral projective homology replacement on the two size-twelve character orbits and retains the complete D57 and W_h projections. Seven old self and twelve new cross blocks have injective norm and compactification, so their actual orientation boundary vanishes. The lift retains22016 additional central coordinates and50 coinvariants; its residual has dimension331776 and562 coinvariants. All four actual involution-cover divided norms leave the stated26 self-wedge classes undetected; their remaining arithmetic boundary and full profinite realization remain active.

Exact complete-proof, fresh-execution and primary-source reading scopes are retained in the attached root and peer audits. These original tasks remain explicit in the opening coverage table.
