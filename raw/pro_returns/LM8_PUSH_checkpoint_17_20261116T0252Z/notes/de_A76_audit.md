# Independent A76 audit

**PASS, relative to the explicitly audited A75 dependency.** Entire proof and complete exact certificate read; independent run matches the whole author JSON.

Draft SHA-256 `b271501e3966da29889faf5297c0a4654c59acc72ab2aeef968dbea59bd88f87`.

## Checked proof gates

1. The cyclic-index-two normal presentation is the actual extension. The two consistency congruences and generator change h -> h+(1+k)b are exact. The four roots modulo2^a and every normalization are proved, with cyclic/abelian, D8, Q8 and smaller orders explicitly retained.
2. Quotients again have cyclic index at most two; coprime subgroup and normal-kernel decompositions give the actual product closure and subgroup, rather than an abstract genus identification.
3. The odd abelian factor kills peripheral commutators and is an actual odd elliptic isogeny. Its field is linearly disjoint from the actual two-power intermediate, so the indicated fibre product is connected and is the requested cover.
4. The four geometric-family results provide the stronger reduction/path input, not only fixed-group equalities. A75 is an explicit dependency and has separately passed a full DE proof/source/certificate audit.
5. The actual map to E extends through the compact-type Abel map and the actual Jacobian homomorphism. The odd isogeny extends finite etale. Compact type of the pullback is proved separately from the nilpotent total closure and actual norm, without inferring it from finite etaleness.
6. Every chosen rational joining subtree maps constantly to O and pulls back as literal disjoint copies indexed by the good etale odd kernel. The selected copy contains a distinct companion, and rational contractions preserve the required path. No new special-rank-zero assertion is made for the odd pullback.
7. The final A42/A59 conclusions retain all actual intermediates, packet/base-point and restriction scopes. There is no cofinality or fixed-element lifting claim.

## Sources and execution

- verified: Lehr–Matignon Theorem6.13, https://arxiv.org/pdf/math/0411059, freshly opened as turn1194view0 for the preceding A75 audit.
- verified: Dupuy–Rabinoff Theorem1.1 and Proposition3.2, https://arxiv.org/pdf/1705.03034, exact scope reused from independent DE A74 source check turn1188view0/1/2.

The literal certificate exhausts3101 consistent presentations through cyclic subgroup order1024, including the small orders. The actual model/path argument is proved separately. Retained independent outputs are `notes/de_A76_certificate_rerun.json` and `.out`. Source SHA-256 `185baad9a7af3bec5d8954a23a70e3dbf1ef5769d839c6dbb1f1575808315c02`; output SHA-256 `de60bb36f2fb0d19d1487d1420e7c69bb6096f2688b6942413372a01e504cb25`.

No canonical source, bibliography or registered row was changed.
