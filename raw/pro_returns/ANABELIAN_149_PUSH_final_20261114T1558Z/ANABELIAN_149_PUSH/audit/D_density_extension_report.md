# D.25 integration report

**Status: Proved, independently reviewed by root.** Integrated in `sections/D_density_extension.tex`; the result register is `audit/D_density_extension_results.json`.

The new conclusion is density-one and asymptotic integrality for every noncuspidal continuous full arithmetic section of the three-punctured line over Q, and for every geometrically connected finite étale cover of that line. A birational lift is not assumed. The proof uses the local theorem D.6/D.19 to make every such section Selmer, then eliminates the exceptional triangular alternative in Stix's Legendre dichotomy.

The central arithmetic point is a compatible, all-moduli statement: a completed rational Kummer class which is an nth power locally at almost every prime for every n is trivial. A single modulus does not suffice, as the explicit example 16 modulo eighth powers shows. The central geometric point is the unique cyclotomically normalized line: an exact cuspidal local section may have trivial arithmetic inertia, but it still normalizes nontrivial geometric cusp inertia. The split case therefore gives the same canonical line, without an unsupported nonzero-transvection assumption about the section image.

The fixed cusp line forces one cusp at almost every prime. A global unit regular and equal to 1 at that cusp gives a trivial completed Kummer class and excludes every finite-local interior point. The corrected finite-place finite-support argument then makes the section cuspidal. Real points are treated only through the connected-component convention.

For a finite étale cover, pushforward of a noncuspidal section is noncuspidal by the actual cusp decomposition intersection. Integral local points lift integrally through the finite normalization outside finitely many primes. The finite set of boundary ramification indices also transfers asymptotic divisibility. This is an argument for the specified finite étale cover class; it does not extend automatically to arbitrary maps or twists.

## Remaining global obstruction

Density one permits infinitely many nonintegral primes. Asymptotic integrality says that their boundary multiplicities tend to zero in the profinite topology; it supplies no bound forcing them to vanish. D.20 already gives continuous Kummer classes with exactly this numerical phenomenon. The new theorem therefore does not establish cofinite adelicity, canonical central-lift compatibility across all finite étale neighbourhoods, or the unrestricted global section conjecture. D.24's norm obstruction still prevents the proposed arbitrary-choice transition argument.

## Checks

The exact primary passages were opened before use, root independently reviewed the complete proof and the finite étale extension, and the small symbolic/residue certificate was executed. No new shared LuaLaTeX build was run by this agent; assembly and build remain root-owned.

## D.26: number-field extension

The extension was independently reviewed and approved by root, and is now integrated after D.25. The original rational-field proof is preserved. The new compatible Kummer lemma uses the cyclicity of odd-primary cyclotomic groups and the cyclic subgroup congruent to 1 modulo 4 of index at most two in the 2-primary group. Each exceptional finite class is therefore killed by two; compatibility reduces the completed class to ±1, and primitive 2-power roots exclude −1. This avoids assuming single-level almost-everywhere injectivity.

The Legendre proof, real component convention, finite-place support argument, and finite normalization transfer are all checked over every number field. The resulting class consists of the three-punctured line and its geometrically connected finite étale covers over arbitrary number fields. Density one and asymptotic divisibility remain weaker than cofinite integrality.
