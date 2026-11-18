# Review of C03: Hua's orange-slice obstruction

Reviewer: `/root/research_surgery`,18 November2026. Files read: `records/research_checks.md`, C03, and the draft N01–N24/T02 in `records/assemble_research.py`. The reviewer made no changes to those root-owned files and inspected no original scan images. The review concerns the concrete argument written in C03, not any entire register, proposed radius theorem, or later source packet.

## Verdict

**C03's contradiction for the actual pair of pants C(32,0,0) is valid.** The matrix gives the intended symmetric cell, the fixed annulus avoids that cell and the other two marked points, its core belongs to the boundary free-homotopy class, and the upper and lower extremal-length bounds have the stated direction. The final inequalities are strict. Hua's project already supplies the obstruction by this method; C03 provides an explicit annulus and a concrete boundary length for that credited argument.

Two editorial improvements were sent to root: correct the McMullen section number, and make the conformal capping construction explicit in one paragraph. Neither changes the mathematical conclusion. Detailed checks follow.

## 1. Metric, equal distances, and the cell

For A0=[[1,−1/2],[−1/2,1]], the two Möbius matrices for1−z and1/z preserve the form. The three marked vectors v0=(0,1), v1=(1,1), v∞=(1,0) have squared norm1, and every pair has absolute Hermitian overlap1/2. Under the Möbius coordinate change associated to a matrix B with B*B=A0, the corresponding central spherical angles are all2 arccos(1/2)=2π/3. Thus the three labeled points are equidistant on the indicated great circle. This directly verifies the geometry used by the model.

The two overlap differences in C03 are correctly expanded. Their common nonnegative region is precisely |z|≤1 and Re z≤1/2. The two boundary arcs meet at e^{±iπ/3}. The metric normalization changes all distances by the same factor and leaves this cell unchanged.

**Citation correction:** McMullen, *From Conformal Invariants to Percolation* (30April2021), printed p.44 is in **§4, “Curvature”**, whose first page is41. His §7 is “Random walks on a lattice,” starting p.68. The cell formula and EL passages were opened at the URL below; the table of contents was reopened during this review. Use “p.44, §4” or simply “p.44.”

## 2. Annulus containment and homotopy class

On Q0, |z+1/2|²≤7/4. The first strict separation follows from7/4<16/9, equivalently63<64. The remaining comparisons4/3<7/5<3/2 are also strict. The annulus centered at−1/2 consequently misses the closed Q0, the point1, and infinity.

Every core circle contains Q0 in its bounded component. The model's cap D0 is a topological disc containing0 and contained in Q0. The closed region between D0 and such a core circle contains no other puncture; its interior is an annulus, which identifies the core's free-homotopy class with that of the cap boundary. The two remaining labels are on the exterior side. Thus the homotopy-class assertion is stronger than a mere picture of separation: it is given by the annular region between the two nested disc boundaries.

The conformal logarithm modulo2πi identifies the displayed round annulus with a cylinder of circumference2π and height log(21/20). C03's length-area computation gives its core extremal length2π/log(21/20). W01 below independently confirms the same convention and formula.

## 3. The actual cap and an explicit collar coordinate

Mirzakhani's cited §3 includes C(32,0,0) directly: zero lengths are allowed, and §2 declares zero length to mean a cusp. The positive boundary is a real-analytic geodesic. The cone disc in the letter can be attached by normalized arclength with a conformal atlas; the following coordinate makes that attachment concrete.

For a geodesic of length L=32, put its lifted axis on the positive imaginary axis in the upper half-plane, with deck map ζ↦e^Lζ. Write log ζ=t+iθ, and choose the collar side of the pants as θ<π/2. The holomorphic coordinate

\[
w=\exp(\pi^2/L)\exp\bigl(2\pi i\log\zeta/L\bigr)
\]

is invariant under the deck map. Its boundary value has |w|=1 and is w=e^{2πit/L}; the pants collar has |w|>1. Along the axis the hyperbolic arclength is dt. Attaching |w|≤1 across that circle therefore extends the complex atlas and identifies the disc's standard circle action with the boundary action from normalized hyperbolic arclength. Multiplying w by a unit complex number changes only the disc coordinate and gives the same pointed conformal filling up to its specified boundary identification. The two cusp neighborhoods have punctured-disc coordinates and acquire their missing center points. The resulting compact genus-zero conformal surface is normalized to the sphere by its three labeled centers.

This gives an actual admissible system attached to P, in exactly the definition used by the letter. It does not assert the proposed global Teichmüller retraction, its fibers, or any radius parametrization. Root may include this paragraph or its shorter version to make the witness independent of an unproved global capping-functor claim.

## 4. Area and the lower extremal-length bound

The two-cusp, one-boundary pants has Euler characteristic−1. Truncating its cusps by horocycles and applying Gauss–Bonnet gives area2π in the limit: the geodesic boundary has zero geodesic curvature and the horocycle terms tend to zero. This is the finite area used in C03.

A representative of the boundary free-homotopy class lifts to a path from a point to its translate under a conjugate of the boundary deck transformation. The translation length is32, so every representative has hyperbolic length at least32. Curves lying strictly inside the surface approach the geodesic boundary, so using the open interior in the extremal-length definition causes no boundary-attainment problem. The hyperbolic metric is an allowed finite-area test metric, giving Ext_P≥1024/(2π).

## 5. Direction of the upper bound and strict contradiction

The model's claimed containment places the fixed annulus conformally inside the pants interior. The inclusion carries its core family into the boundary free-homotopy class. For a density on P, restriction decreases total area and restricts the curve family over which the infimum is taken. Consequently the quotient for the full family on P is bounded above by the corresponding quotient for the annular core family. Taking the supremum gives precisely Ext_P≤Ext_A, as written in C03. Zero restriction area gives no positive contribution and does not reverse the inequality.

The lower estimate log(21/20)>1/21 follows from the strictly decreasing integrand1/t over the interval[1,21/20]. The rational comparison1024/21>4(22/7)² is correct, and22/7>π supplies the final strict inequality. Thus1024 log(21/20)>4π² and the two extremal-length bounds cannot both hold.

The conclusion is exactly that the cap of this particular pants does not satisfy the fixed-cell containment required by the stated orange-slice model with two degenerate discs. The argument gives no verdict on injectivity of the admissible-radius assignment, its complete image, or the independent collar-metric question.

## 6. Primary sources actually opened

| Source | Exact checked scope | URL |
|---|---|---|
| Weber–Hoffman–Wolf, *An embedded genus-one helicoid*, Annals169(2009) | §2.5, printed368–369; Definition5, Example5, Definitions6–7, Proposition5 and following explanation | https://math.rice.edu/~mwolf/whw09.pdf |
| Mirzakhani, *Simple geodesics and Weil-Petersson volumes of moduli spaces of bordered Riemann surfaces*, Invent.math.167(2007) | §2 printed186, cusp convention; §3 printed190, C(x1,x2,x3), vanishing lengths and hexagon construction | https://www.labri.fr/perso/vdelecro/toprint/mirzakhani1-pdf2up.pdf |
| McMullen, *From Conformal Invariants to Percolation*,30April2021 | Contents; §4 printed44, symmetric cell; §6 printed61–62, length-area definition | https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/219/course/course.pdf |

Tool references available to root: WHW `turn645974289view0`; Mirzakhani `turn932431709view0`/`turn932431709view1`; McMullen contents `turn756491645view0`, earlier cell passage `turn909591910view1`. Root must open sources itself before placing final web citations.

## 7. Draft-note audit N01–N24 and T02

The draft preserves Hua credit, frozen-reading differences, the limited Q1-07 availability, and the letter's staged qualifications. T02's page/provenance data match the public PDF checked in `context_surgery.md`, W04. N19 correctly locates the shadow without claiming to rederive the registered map. N20/N22/N24 keep the distinct source questions attributed and unresolved at their appropriate scope.

Three small edits or citation improvements were suggested to root:

1. **N02:** the boundary identification transports the gluing relation and defines the new surface. Avoid implying that the page already gives a global conformal map X→X*. “Construction of the resulting reglued surface” is precise.
2. **N10/N11:** LM4_SUCCESSOR E.10 is the register's open six-case involution/congruence-kernel calculation. Its relevance to the early elliptic list is only through later real-structure material. The direct references for the lists are LM§37, `LM_140-2_text.tex` scans533–538, and the lattice/Jacobi dictionary in `LM_140-3_text.tex` scans019–020. No result-state row is required merely to attach a remote open problem to every note.
3. **N12:** add the author's own notation in `LM_140-3_text.tex`, scan019, equation26 (`GP(1,R)=Gl(2,R)/R*` with the fractional-linear action), and `LM_140-2_text.tex`, scan232, identifying GP(1,C) with the sphere's conformal automorphism group. This supports the projective interpretation while preserving the explicit GP-versus-Hua-Gl reading difference.

N17's label “withdrawn in the same text” is limited by its body to the original scaling/coordinate intuition. The body correctly says that the complete orange model remains a question to Bers. Keep that limitation attached wherever the label is repeated.

## Suggested check-event classification

**C03.orange_containment: used and independently reviewed in this run, no mathematical fault found in the stated concrete witness.** Review scope includes cell geometry, annulus inclusion, class identification, actual conformal cap, area, both extremal-length comparisons, and the strict inequality. One bibliographic section-number correction was identified. This is a targeted check of Hua's already credited method, without any novelty claim or change to the status of the other radii and capping questions.
