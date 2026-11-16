# D94 complete independent proof and code audit — PASS

I read the entire stable candidate, the entire owner certificate and source ledger, canonical D91's exact stabilizer/limit/map argument through D91.25, and the complete D93 integral norm-extension addendum. The initial broad dependency search was truncated; the exact D91 passage was subsequently read in a bounded, complete call. This audit reuses the prior complete D93 and Smith-addendum audits, rather than inferring the new result from finite matrices.

## Actual arithmetic and natural compact map

The two non-fifth-power arguments are valid. For c=d^5 the second factor of (d+1)(d^4-d^3+d^2-d+1) has valuation exactly one at five and is larger than five, contradicting a pure power of five. Disjoint nonempty prime supports therefore give the exact closed lattice 5^r Z5 × Z5. Both five-valuations vanish. The local first depth is N; the second and diagonal depths are zero because 1-c^(5^r)=2 modulo25. Thus the separate D77 free boundary factor has rank N-r.

Eliminating the local relation with unit beta gives the literal ideals PR=u^2q_N R and J=q_rR. The source retains q_r as generator, so no unit or induced action is discarded. Exact tame averaging removes the low jets, including their possible torsion. The two remaining finite free modules have precisely the displayed B and C actions, and their actual map is multiplication by q_r. The target coinvariants are integrally torsion-free: the norm kernel of multiplication by u^3 has nontrivial tame weight, and the fixed basis vector at zero supplies the required surjection on first homology. The Fourier-orbit calculation proves rational injectivity on every free source orbit j>r. Consequently the entire compact kernel is exactly the finite torsion of B_Gamma, not merely a rank comparison.

## New first-homology gate

For every actual invariant f of A, q_r f is an ordinary substitution invariant. On each nonzero residue coset modulo5^r its coefficients are constant and their cyclic-difference sum is zero; torsion-freeness makes them zero. Reduction to R_r has action chi times a finite permutation and no invariants. Hence the coefficients of f on each such coset are constant with zero sum, and f is literally supported on the subgroup5^r Z/5^N.

Writing f=F(t^(5^r)), exact tame averaging puts F in (Q-1)^3R_h. The lift through u^3 is S_(5^r)(t)^3 B(t^(5^r)). From the invariant equation at Q=1, v5(B(1))>=h-1. The resulting norm-boundary coefficient has valuation at least2r, so is zero modulo five. This proves the vanishing of the entire H1-to-norm map. It is not a check on a selected finite invariant basis. The h=0 case is separately handled by the absence of invariants. Thus the norm class has exact order five in the short exact sequence.

## Exact norm transfer and elementary divisors

The polynomial F_(r,N)=q_N/q_r is fixed by substitution, satisfies S_chi(t^(5^r))F=chi F, and sends the old norm generator literally to the new norm generator. Both module intertwiners and the u^3 diagram therefore commute integrally.

The identification of A_Gamma uses precisely D91.25 with old parameters (r,m,N_old)=(r,N,infinity). Its nonzero residue blocks are retained. On each block, the permutation-kernel coinvariant has order5^(N-r), by the actual stabilizer inclusion on first homology. Right exactness and the three exact finite orders show that norm transfer injects C_(5^j) as5^(N-r) times C_(5^(N-r+j)). This supplies the required natural map; no abstract rank argument substitutes for it.

The D93 largest lift therefore transfers to a lift y with 5^N times a unit times y equal to the nonzero new norm class. Its exact order is5^(N+1). The smaller factors split by the valid mixed-order triangular replacements y_j-c_j5^(r-j)y_r. Their orders multiply to the exact extension order, and the finite free quotient splits continuously. This proves all elementary divisors for every N>=r>=1.

The actual point supplies a full section and a nonempty metabelian fibre. D74 supplies the stated product translation group at finite support. The two independent global Kummer coordinates exclude all cusp lines, and the rational sign equations leave exactly the stated ordinary point. No higher-derived or arbitrary-pair conclusion is introduced.

## Executed independent replay

I read every line of the owner program. The modular Smith operations are exact in int64: all intermediate products are bounded by5^20<2^63. Every rationally nonzero pivot is found below precision, and the leftover nullity is independently proved by the Fourier calculation. The six finite source/A/target Smith cases therefore certify their stated elementary divisors. The actual norm intertwiners, q_r target map, u^3 diagram, literal norm generator, and thirty arithmetic residue/logarithm cases all pass.

The retained independent runner is `code/fgh_D94_certificate_rerun.py`. It calls the owner's read-only run(), compares the entire serialized JSON byte for byte, and verifies that the owner source, JSON and stdout remain unchanged. Outputs and exact hashes are in `notes/fgh_D94_certificate_rerun.json`, `.out`, and `_metadata.json`.

No correction is needed. No canonical source or register was edited. No new external theorem is used beyond the exact already verified D91/D93 and their primary cohomological inputs.
