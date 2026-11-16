# A62 independent PBC full audit — PASS

Completed 2026-11-15 at approximately20:34 UTC. I read the entire candidate
`notes/fgh_A62_draft.tex`, inspected the complete exact certificate, reran
all three cases without changing the owner's files, and reopened the
primary elliptic-curve statements. No mathematical gap was found.

## Actual translation and isogeny comparison

The ordinary Hasse coefficient is nonzero. A Gaussian factor with unit
differential gives the actual étale degree-p isogeny over `Z_p`, whose
special kernel is the reduced p-torsion group. Its kernel sections become
rational over a finite unramified extension. The divisor of the actual
division-function translation ratio is `p^2(O)-p^2(-T)`; the chosen
function with divisor `p(O)-p(-T)` therefore gives the exact pth-power
ratio, up to a constant. Normalizing its Gauss valuation is legitimate
because this unramified Gauss DVR has value group `Z` and uniformizer p.
Both division functions are units at its generic point, so the remaining
constant is a unit. Frobenius injectivity gives `q_T=1 mod p`, and its pth
power is `1 mod p^2`. Dividing the actual identity by p then proves that
the reductions of the two `H_0` functions differ by a constant. Thus
`D H_0` is invariant under the actual translations, not merely under an
abstract isomorphic group or modulo an unspecified additive error.

The division differential identity gives `DF=-DU` with the displayed
sign. The logarithmic derivative of the translated g-ratio has no pole:
its possible simple residues are multiples of p. Hence `DU` descends and
lies in the two-dimensional `L(2O)` downstairs. The quarter-rotation
eliminates the constant. The leading coefficient at O gives exactly
`DU=-mu^2 x(alpha)` and `Df=mu x`. Only the first local terms are required;
no characteristic-p logarithm is being used.

The descended f has exactly one pole of order p and is odd. At `(0,0)`
its derivative has a double zero, so its zero has order three because
`3<p`. Every other zero is simple. Thus all critical points of the
actual differential are accounted for: p triple zeros and p(p-3) simple
zeros, away from the reduced torsion. The primitive orders4 and2 are
strictly less than p, so there is no undetected lower pth-power Taylor
term.

## Actual charts, stable model, and marks

The main substitution gives the full radicial degree-p function field,
with an ordinary elliptic normalization. The binomial tail equations are
exact. At each centre, unramified lifting makes every lower Taylor
coefficient divisible by p; the stated valuation inequalities eliminate
all degrees except4 or2. At two-torsion, the y-parameter and the displayed
elliptic equation give the same conclusion. The two unit partial
derivatives prove that these are actual smooth special charts.

The Artin–Schreier uniformizer calculation gives the stated different,
genus, and zero p-rank. The positive-genus divisorial valuations persist
by the same already audited regular-resolution argument as A61. Their
genera exhaust the generic genus, forcing a tree and rational remaining
components. The main already carries the entire degree-p map to the good
elliptic model; every other component therefore maps constantly. Ordinary
connected/étale p-torsion yields p clusters, each containing p marks.
Their images avoid all positive-genus tails. Since marks cannot coincide
with an attachment node, each cluster lies on a rational marked tree.
Every selected cusp has a second cusp in its own cluster, so A42's
rational-path hypothesis holds. A59 supplies the normalizer conclusion.
There is no cofinality claim for arbitrary finite covers.

## Exact execution and primary sources

Independent execution is retained in
`notes/pbc_A62_independent_rerun.json` and `.out`. Every output row agrees
with the owner's JSON, including the actual reduced Verschiebung curve
identity, the differential/isogeny identity, every critical multiplicity,
the valuation inequalities, and genus exhaustion. The cases are:

| p | triple centres | simple centres | total genus |
|---|---:|---:|---:|
|5|5|10|51|
|13|13|130|1015|
|17|17|238|2313|

I reopened Silverman's *Arithmetic of Elliptic Curves*, V.4.1(a), printed
p.148, and III.6.1/6.2(a,c,d), printed pp.81–83, at
`https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf`.
Retrieval references are `turn975view0`, `turn975view1`, `turn976view0`,
and `turn976view1`. III.6.2 explicitly supplies the additivity of duals
and the dual of integer multiplication, making the Gaussian-conjugation
description immediate from the dual of `[i]`. The division-polynomial,
stable-reduction, and Crew inputs were independently opened during the
A61 audit and their scopes do not change here.

Two literal exponent-comma TeX typos were reported to the owner. These do
not affect the proof. **Verdict: complete proof and certificate PASS.**
