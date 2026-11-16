# D77 candidate audit ledger

## Status and scope

The complete candidate is notes/de_local_boundary_draft.tex, 374 lines. It remains unregistered and notes-only during the checkpoint11 canonical freeze. No diagnostic PDF exists.

The claim evaluates the whole local-at-five group L5, the global invariant dual T_s, and their actual map, for every completed abelian pair including infinite ramification. Consequently K_s is continuously isomorphic to S_s times the explicit three-axis free factor Z(d). The inverse limit S_s of finite global localization kernels remains unevaluated. No arbitrary-pair section existence or explicit first higher-derived obstruction is claimed.

## Root review

Root read the complete374-line candidate and reported that its mathematical proof looks sound, with fresh NSW(1.1)–(1.2) primary check turn981view0 and Milne I2.1/I2.3 turn984view0/1. The coefficient κ3/48 was independently confirmed. Root requested that the certificate derive the first-jet matrix from the actual three multipliers rather than merely enter it. This extension has now been made: the first two multipliers are t^a chi S_chi(t), t^b chi S_chi(t); the diagonal multiplier is chi S_chi(t)t^(a−b+(1−chi)/2). The relation coordinates and full matrix are then derived symbolically, including the half-coboundary gauge.

## FGH full independent audit: PASS

FGH read the whole proof, independently derived the jet matrix, reread canonical D63, and freshly opened NSW(1.1)–(1.2) and Milne I2.1/I2.3. The local Kummer primitivity, actual compact-image projector, uvw times unit annihilator, unique k-fixed lift, polynomial defect elimination, natural global/local comparison, and continuous splitting all passed.

During archive capture the detailed ledger and independent rerun were written outside LM8_PUSH in checkpoint11_external_audits/fgh_D77_audit.md and the accompanying certificate files. FGH reports that an initial help invocation rewrote the deterministic original JSON with identical bytes; the separate outside-tree rerun confirmed byte identity. No source or mathematical change occurred.

## PBC full independent audit: PASS

PBC read the complete proof and independently derived the first-jet matrix, the unique fixed-lift argument, and all coefficient equations7A0,3B0,C0. A read-only rerun of the complete certificate computation, stopping before writes, matched every original JSON field. Fresh NSW(1.1)–(1.2) source ref turn985view0. The exact invariant sum is natural for the global-to-local inclusion, and S_s remains explicitly retained.

## Author checks

The exact certificate verifies all24 nontrivial Kummer combinations in the Eisenstein ring, the raw unit identity, the integral projector on the actual image, the independently derived jet action and its Cartier determinant−3/16, the integral diagonal gauge, and order20 of2 modulo25. The complete proof uses actual continuous images, exact integral coefficients, and genuine duality. It does not replace an actual subgroup by a formal assignment of coefficients or discard a derived-limit term.

The extended certificate rerun initially compared two algebraically equal symbolic matrices by structural expression equality; that assertion was corrected to simplify their difference entry by entry. The corrected exact derivation passes. This was a symbolic-expression comparison issue, not a change to the displayed matrix or proof.

## Promotion

Root approved integration after the successful checkpoint11 save at21:00:45UTC. The complete proof is now sections/D_alexander_local_boundary.tex, with the final executed certificate code/de_local_boundary.py/.json/.out and a registered owner row. The original unregistered draft is preserved.
