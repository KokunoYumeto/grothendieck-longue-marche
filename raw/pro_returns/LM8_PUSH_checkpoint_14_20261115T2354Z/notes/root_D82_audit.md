# Root audit of D.82: valuation and unit vectors at five

**Verdict: PASS; approved for integration.** The root read the complete 438-line draft and the entire finite certificate, checked the actual-action arguments rather than a formal arithmetic substitute, and reran the certificate independently. The complete author and root certificate JSON objects are equal. The exact hashes are retained in `root_D82_rerun_verification.json`.

## Statement and scope

The hypothesis is that the reductions of the away-five valuation vectors span both coordinates. The five-adic valuation vector and the local principal-unit vector may each be arbitrary. The classification is therefore conditional on a stated global image hypothesis; it is not a claim about every Kummer pair or about the existence of a section above every pair. The local two-vector rank, and the three distinguished boundary lines, give the finite factor. The three local divisibility depths give the divisible factor by D.77.

## Actual Kummer-five descent

The defining Soulé formula was reopened in the primary Nakamura–Sakugawa–Wojtkowiak paper, https://arxiv.org/pdf/1410.1045, equations (1.1) and (1.2), printed page 2 (root retrieval `turn1073view2`). On the kernel of the actual beta representation all odd Soulé characters vanish by the exact raw formula, whose denominator is a five-adic unit. For each r, choose m=1+4*5^(r-1). The exponents in the defining cyclotomic product are 1 modulo 5^r, so its Kummer character on the cyclotomic kernel equals that of the product of all primitive cyclotomic factors, namely 5. This proves the claimed descent of kappa(5); compactness gives continuity. Locally the valuation of 5 over Q_5(zeta_5) distinguishes its residual Kummer class from the cyclotomic one, giving the saturated translation coordinate. This is an actual quotient of the inertia image.

## Upper bound and exclusions

The local image retains the kappa(5)-graph complement. After coinduction the coefficient action is the beta action multiplied by its actual translation; the argument never silently replaces it by the untwisted module. The tame weight projector separates the weight-one Kummer-five and weight-three Soulé coordinates integrally, and produces the required primitive beta difference on the kernel N_1. The two N_1-invariant modules and the four-term sequence have the stated connecting term. The auxiliary H^0 and H^1 vanishings follow from their tame weights, including the translation Hom term of weight -2. This bounds the entire kernel by order five, not just a selected cocycle.

Divisibility of the local invariant dual, established in D.77 for arbitrary pairs, justifies an order-five representative detecting P. The independent local vectors force its vanishing in the rank-two case. In the primitive boundary case the proof applies the finite-functional form of D.79 to the actual untwisted element of cyclotomic multiplier 2. If only the valuation vector is primitive, the quotient of its defining ideal by its product with the augmentation ideal has weight 3; the difference 2^3-2 is a unit, so the functional descends to the same boundary quotient. This covers both possible primitive columns and does not assume an integral domain when the local vector is nonprimitive.

## Lower bounds and global localization

For the zero residual local plane, all translations vanish on the fixed ten-dimensional quotient and D.81's primitive applies. On a nonboundary line the explicit four-dimensional quotient has nonzero cubic P coefficient. The three lower tame weights give a unique correction; all twenty residual action elements and all pullback translations are checked. The globally nonzero class follows from the full away-five translation lattice. D.80 supplies a common finite level for the finitely many exceptional local places, with the five-adic primitive preserved; this is a global locally trivial class, not merely a list of local classes.

## Executed certificate

The independent root script imports the canonical finite-action implementation. It checks the cyclotomic product moments through r=6, all three nonboundary lines, the full residual affine actions, all 625 local two-by-two matrices, and the actual t=10 example. The strata have sizes 1,72,72,480, with 73 matrices in the order-five case. The root rerun completed successfully and the complete JSON equals the author output byte for byte (SHA-256 809b41ef23bdfccfe21415bb5cf6154e6fb347d952684081edcdb1f03225947f).

FGH and PBC also supplied complete independent proof audits and complete certificate matches. Their ledgers are retained separately. No part of the residual-dependent global-image problem is promoted by this audit.
