# Independent DE audit of C.48

**Verdict: PASS.** The complete 217-line refined candidate was read, and its primary relation-module source was independently reopened. This is a structural proof; no finite numerical check is being substituted for the closed-subgroup or compactness arguments. Canonical sources remain frozen.

## Exact source check

Grunewald–Jaikin-Zapirain–Pinto–Zalesskii, *Normal Subgroups of Profinite Groups of Non-negative Deficiency*, §2.2, printed page 13, displayed (2.1), https://arxiv.org/pdf/0810.2027. Independently opened references: turn1254view0, turn1254view1, turn1255view0. The paragraph begins with an arbitrary finitely generated profinite quotient, takes a free profinite presentation, identifies the compact relation module by Shapiro, decomposes its prime-primary factors, and obtains the integral completed-group-ring embedding. It does not require the relation subgroup to be open or finitely generated. For the actual derived quotients used here the minimal number of generators is exactly two, as required by that source's presentation convention. The candidate also gives the homological construction for its stated free rank-two presentation.

## Proof gates checked

1. **Integral peripheral invariants.** For each finite quotient D and prime p, the refinement into D times Z/p^(k+v_p(n)) gives actual y-orbit length np^k. The group-ring transition sums coefficients over fibres. An invariant coefficient in the upper quotient therefore pushes to a multiple of p^k at every lower point. Arbitrarily large k forces zero in Z_p[D]. This is valid for nonabelian D and uses the integral inverse limit, not a rational or normalized Haar measure.

2. **Derived induction.** Once f is in F^(d-1), its class in the compact relation module is fixed by y. The equivariant embedding and the preceding injectivity kill every prime-primary component. Their product is the entire profinite abelian relation module. Thus f is in F^(d). No finite-index approximation of the derived subgroup is assumed.

3. **Full centralizers.** Every integral Heisenberg pro-p quotient kills F'' and detects the unwanted abelian coordinate of an element centralizing x (or y). Removing the remaining genuine procyclic power puts the element in F', where the induction applies. The powers are copies of Z-hat because abelianization is unchanged. This proves the full centralizer, not only its intersection with the commutator subgroup.

4. **Outer versus literal normalization.** An inner representative fixing x must be x^a. The equality f^-1 y f=x^a y x^-a makes f x^a a power of y. The free abelianization and f in F' force both exponents to vanish. For arbitrary multiplier, an outer-trivial action is trivial on abelianization, hence its multiplier is exactly one. The same kernel statement therefore covers the full gentle group.

5. **Sharp parity depth.** The outer kernel at derived depth four is precisely the kernel already killed by the retained-pair character in C.47. The actual C.46 element with f in F^(3) and parity one supplies the sharp lower bound. This uses the previously audited actual full element, not a finite compatible pair.

6. **Topology and finite detector.** The characteristic-quotient topology makes the automorphism group of this finitely generated profinite group profinite. Its inner subgroup is compact and closed. The actual outer image is compact. Simultaneous innerness on all finite characteristic quotients supplies a common conjugator by the finite-intersection property. The product of finite outer groups is the correct target: no unsupported transition maps between arbitrary outer automorphism groups are used. Applying the same compactness to parity-one elements produces one actual finite characteristic quotient detecting parity. No size bound or explicit all-multiplier evaluator follows.

## Scope and editorial note

The full-group character conclusion and sharp depth four pass. The proof does not identify the full outer image, and does not claim that C.47's already constructed explicit pair quotient is itself the new outer detector. The author corrected the reported literal square typo and normalized its second spacing variant. The exact two-line editorial diff was independently read; it makes no mathematical change. No correction remains.

Audited candidate SHA256: `64052b4435aa83d96f5616f0c77c2d928053fc21dadcc2a3fba1f8a02212617e`.
