# La Longue Marche expert line: hunches

Things suspected but not proved by the expert, with reasons, the exact place in Grothendieck's text, and what a
prompt to GPT-6 Astra (effort Pro) should demand. Section 1: Claude Fable 5.2, effort max, 12 Nov 2026, from Part I
(cote 140-2) only. Numbered H1, H2, ...; never renumbered.

**H1. The "relation des lacets" of Part II is the pair of GT_0 relations; the pentagon is the missing third
equation, and Part I already contains its source.** Reasons: the group he computes in Part II is the centralizer of
S_3 in Autext_lac(Π̂_{0,3}), with cocycle conditions "sous ρ" (order 3) and "sous σ" (order 2) (table of contents,
3:sc3–5; 2:sc315–317: a lift commuting with ρ and a lift commuting with σ_0); that is the shape of Drinfeld's
relations (I) and (II) for a pair (λ, f). The pentagon comes from M_{0,5}; in Part I the corresponding condition is
(e) of §32 (2:sc396): N^!_{0,ν} normalizes the fibre subgroups π'_i ↪ 𝒯̂^{!+}_{0,ν}, and the subgroup H of §29
(2:sc367–369). Demand: (1) write the dictionary between his parameters for an element of Γ'_{0,3} and (λ,f), and
prove that his loop equation is equivalent to (I)+(II); (2) write condition (e) for (0,4) → (0,3) and for
(0,5) → (0,4) as equations on (λ,f) and prove that the second is the pentagon (III); (3) decide whether
his Γ'_{0,4} (normalizer definition, 2:sc345) equals GT, with a complete proof or the exact gap. Needs Part II
read in full first (not done in section 1). Where: LM3/LM3b territory; candidate for a prompt of its own
(`PRO_PROMPTS\LOOP_EQUATION_VS_GT`).

**H2. Grothendieck's hole-plugging map ψ_i: 𝒯̂̂(π)_i → 𝔖̂̂(π'_i) (2:sc347–349, 2:sc367) is injective but not surjective, and
its image on the N-level is cut out by finitely many levels.** Reasons: discretely it is an isomorphism (his §18
theorem = Birman); profinitely, automorphisms of π̂_{g,ν−1} have no reason to lift to the fibre group, while for the
FC-admissible outer automorphisms of configuration space groups Hoshi–Mochizuki prove injectivity of
Out^FC(Π_{n+1}) → Out^FC(Π_n) for all n ≥ 1 and bijectivity for n large (from memory: n ≥ 3, or n ≥ 2 affine).
Demand: prove injectivity of ψ_i for arbitrary loop-preserving outer automorphisms or exhibit the obstruction;
exhibit an element of Aut_lac(π̂_{0,3}) not in the image of ψ_i for (0,4) (for instance from an element of GT_0
outside GT, if one is known, or prove that the image is exactly the stabilizer of a suitable structure); then
restate his "fait admis" in its strongest true form.

**H3. With F1/F2 (FINDINGS), the whole programme I–III of §24 (2:sc292–294) is provable for discrete loop groups.**
Reasons: (I) bijectivity of (*) Φ(Π',Γ) ⊔ I'^! → Φ(Π,Γ) is the statement that the fixed points of the realized action
are the old fixed points plus the plugged ones; (II) full faithfulness of drilling is uniqueness of realization up
to equivariant isotopy (F1 + Birman–Hilden); (III) "a torsion-free extension of a finite group by a loop group is a
loop group" is the Nielsen realization theorem in its group-theoretic form (torsion-free virtually surface groups
are surface groups; with loops: peripheral structure preserved). Demand: complete proofs of I, II, III in his
formulation, for Γ = Γ^+ and then with orientation-reversing elements (dihedral stabilizers, his §33 theorem);
then his conjecture 2:sc286–287 (existence and uniqueness of (Π', I'^!)).

**H4. The profinite analogue of §§15–18, 24, 31 holds for actions that stabilize a discretization and fails
without that hypothesis only through "non-geometric" finite subgroups.** Reasons: for a finite G ⊂ 𝒯(π_0) ⊂ 𝒯̂̂(π̂_0)
the extension Ê is the completion of a Fuchsian group, where torsion is conjugate to discrete torsion (F9); for an
arbitrary finite subgroup of Out(π̂_{g,ν}) nothing forces it into a conjugate of 𝒯 (his own remark 2:sc384:
"ce n'est sans doute pas automatique"). Demand: (a) for G ⊂ 𝒯(π_0): prove π̂^G = 1, the bijection of splitting
classes of E and Ê, and the profinite versions of his (c), (d), (e) (2:sc197–198); (b) decide whether every finite
subgroup of Out_lac(π̂_{g,ν}) is conjugate into 𝒯(π_0) for small types ((0,3): finite subgroups of Out_lac(F̂_2);
(1,1)), or construct one that is not.

**H5. For number fields, "admissible" sections in his sense (2:sc431–433: germs of splittings normalizing no loop
subgroup) are exactly the sections that are not cuspidal, and his axioms (1)–(6) of §32 are equivalent to the
section conjecture for all open subcurves at once.** Reasons: his (5)(c) says every section of the plugged curve
other than the canonical point P lifts to the punctured curve: this is the section conjecture for the affine curve
given the one for the proper curve plus the description of cuspidal sections; (b) is injectivity. Demand: prove the
precise equivalences between his axioms and the standard formulations (birational, affine with cuspidal sections,
proper); prove what is unconditional (injectivity statements (25), (27)(b); (6) uniqueness from L^{Γ'} = 1); with
019 as a hypothesis, derive the p-adic counterparts of (1)–(6), in particular the affine case (5), which 019 does
not treat.

**H6. The canonical discretization attached to a rational point (2:sc489–490) is the image of the topological
fundamental group at a complex embedding, and its independence of choices is false as stated.** Reasons: a
discretization inside π_1(U_Q̄, x) is the image of π_1^top(U(C), x) for an embedding Q̄ ⊂ C; it depends on the
embedding (Galois conjugates of the lattice differ: the lattices σ(π_0) for σ ∈ Γ_Q are in general not conjugate),
which he half-notes ("Γ n'opère pas sur ce groupoïde"). What is canonical is the Γ-orbit, i.e. the strict
prediscretization for each archimedean place. Demand: prove the correct statement and decide the stabilizer of the
lattice in Γ_K (expected: trivial or generated by complex conjugation), which is a statement about elements of
Gal acting "geometrically" on a discretization (compare (30) of §29, 2:sc377).

**H7. His count of arithmetic data in §29: P_a/±1 ≃ {elements of order 2 of Γ_a} ≃ archimedean valuations of Q̄
(2:sc377–378) extends to a characterization of the real places of number fields by "real" discretizations**, and
gives, with §33 (π_0(U^σ) ≃ classes of splittings over ⟨σ⟩), the real section conjecture in his language. Reasons:
§33's theorem is exactly the real section conjecture for π_1^top; the profinite version is known (Mochizuki; Pál;
Wickelgren, from memory). Demand: state and prove the real section conjecture in the form
π_0(X(R)) ≃ {π-classes of splittings of the extension by Gal(C/R)} for his loop groups, including the cuspidal
packets at real cusps, and compute the fixed groups π̂^{σ_i} (his (7), (14): trivial for a line component, Ẑ for an
oval).

## Successor's notes on H1-H7 (12 Nov 2026)

Written 12 Nov 2026, 14:08 UTC (clock read) by fork D of the successor (Claude Fable 5.2, effort max), from the
literature read by forks A, B1, B2 and by the main agent before 13:55 UTC (FINDINGS section E has the citations).
The hunches above are unchanged; these notes say what the reading does to each. Nothing here uses the LM3/LM3b
returns or Part II of the manuscript.

**H1.** The first half has a primary-text footing: Drinfeld himself (1990, §4, pp. 166–167) identifies the pairs
`(λ, f)` satisfying (4.3), (4.4) with the endomorphisms of the profinite completion of `B_3`/centre that keep the
subgroup generated by `σ_1` and act trivially on `S_3`, and says that (4.10) is necessary and sufficient for
extension from `T̂_{0,4}` to `T̂_{0,5}`; Harbater–Schneps prove `Out^♯_4 ≅ GT_0`, `Out^♯_n ≅ GT` (n ≥ 5), with
Theorem A: (I) ⇔ `[θ, F] = inn(f)`, (II) ⇔ `[ω, F] = inn(y^m f)`. So "his cocycle conditions under ρ and σ are (I),
(II)" is now a precise statement to prove once Part II is read. New, unproved (this fork's reasoning; asked in LM4
E (b)): his necessary condition of 2:sc315–317 (a lift commuting with `σ_0`, a lift commuting with `ρ`) should hold
for every element of the centralizer as far as `σ_0` goes (one fixed point of `z ↦ 1 − z` in `U`, hence one class
of lifts of order 2, by Bridson–Conder–Reid Thm 5.1), and should cut out a subgroup of index at most 2 as far as
`ρ` goes (two fixed points `e^{±iπ/3}`, two classes of lifts of order 3, exchanged exactly by the elements that do
not fix `√−3`). If so, his "il se pourrait qu'il n'y ait aucune restriction" is right for `σ_0` and wrong by index
2 for `ρ`.

**H2.** The thresholds are now exact (Hoshi–Mochizuki 2011, Theorem B, read by fork B2): for the pro-Σ
configuration space groups of a hyperbolic curve, `Out^FC(Π_{n+1}) → Out^FC(Π_n)` is injective for n ≥ 1 and
bijective for n ≥ 3 (affine) or n ≥ 4 (proper). For the tripod, Hoshi–Minamide–Mochizuki, Corollary C:
`Out(Π_n) = GT × S_{n+3}` for n ≥ 2 with no admissibility condition. So for genus 0 the image of his hole-plugging
map on the levels above (0,4) is all of `GT`, and the first level where surjectivity can fail is
`Out^FC(Π_2) → Out^FC(Π_1)`, i.e. (0,5) → (0,4) → (0,3): `GT → GT_0`. H2's "not surjective" is therefore the
question whether `GT ≠ GT_0`, which no text read here settles for the profinite groups. Note that these theorems
concern FC-admissible (or all) outer automorphisms of configuration space groups, not his full `𝒯̂̂(π)_i → 𝔖̂̂(π')`
for a single curve group; that comparison is still to be written.

**H3.** (III) for ν = 0 is a theorem independent of realization (Eckmann–Müller 1980, Corollary 2; the extension
may be a non-orientable surface group, so his statement needs that case added); for ν ≥ 1 it rests on Stallings
and on the pair version (Eckmann–Müller, Theorem 2), with one step from memory. (II) is F1, classical (Harvey 1971;
MacLachlan–Harvey 1975). Existence for punctured surfaces is still from memory (Kerckhoff 1983 not obtained).

**H4.** (a) is settled for orientation-preserving `G` (Bridson–Conder–Reid, Theorem 5.1, for the splittings;
the centralizer condition for `π̂^G = 1`: Minasyan–Zalesskii with Minasyan in the cocompact case, the free case
from memory); open in the texts read: groups with reflections and dihedral subgroups. (b) splits in two layers.
For finite subgroups of the *completion* of the mapping class group in genus ≤ 2, Boggi (arXiv:2408.12486v2,
Theorem C, unrefereed) states: classes of solvable finite subgroups of the discrete group and of the completion
correspond, torsion elements are conjugacy distinguished, and centralizers of finite subgroups in the completion
are the closures of the discrete ones; Boggi–Zalesskii (Bull. LMS 57 (2025)) is the paper behind it (title only
read). For finite subgroups of the full `Autext_lac(π̂)` outside the completion nothing was found; for (0,3) it is a
question about torsion in `GT_0`.

**H5.** Confirmed in substance (fork B1): admissible = non-cuspidal over fields that distinguish tori from abelian
varieties (Stix, Corollaries 12, 22, after Nakamura); ⑤ from the proper case is the neighbourhood argument. One
correction: `π^Γ = 1` holds for cuspidal sections too; the condition that excludes cusps is that the fixed group of
`Ker χ` be trivial (his own PS of 1983; 2:sc433), conjectural for point sections. With 019 the p-adic affine case
is no longer a hunch (F24).

**H6.** Not touched by this reading.

**H7.** Confirmed and corrected (F18): the real section statement is a theorem (Mochizuki 2003; Bresciani–Vistoli),
and over R the cuspidal sections are not extra classes: a real packet has two elements, the classes of the adjacent
components. Still to prove: the profinite fixed groups (1 for a line, `Ẑ` for an oval); for the moduli stacks the
profinite statement with centralizers is known for g ≤ 2 only (Mochizuki 2003, Cor. 3.15).
