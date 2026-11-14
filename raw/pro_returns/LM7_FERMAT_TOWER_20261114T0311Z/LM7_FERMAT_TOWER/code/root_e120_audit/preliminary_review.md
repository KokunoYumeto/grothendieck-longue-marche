# Root preliminary review of the active E120 work

This is a review of work in progress, not approval of a frozen E120 statement.
The root assistant read the complete current notes `elliptic_symbols.md`,
`based_translation_handles.md` and `orbifold_cover.md` on 14 November 2026.
No full mathematical-program replay is claimed here.

## Direct cochain sign check

For the stated semidirect-product law and Tate-square coefficients, write
`a_i(n,g)=l_i(v_n)`, `b=L(z_n)` and `s=a_i*a_j/2`. Direct substitution gives

```
d(b+s) = -cross(L c) - a_i cup a_j.
dB_t = cross(dt),  B_t(n,g)=t(v_n).
```

For the constant symbol, the cup is the cross cochain
`kappa_lambda(g) l_u(A_g v')`. Hence the proposed symbol and corrected
cross cochain have the literal identity

```
cup(6{f_i,f_j}-{lambda,u})
  = Inf(cross(reg)) + d(B_t-6b-6s).
```

The signs follow from the inhomogeneous differential, without a rational
regulator normalization. The map `p j_* = 3` then gives
`3 reg = -6 L c j_* - d(t j_*)`. Its factor three remains in the formula.
The direct values on the two chosen filling lifts supply the integral
coordinates. The stated injectivity on H1 uses the actual coefficient
sequence and the vanishing of the cyclotomic quotient's invariants.

The author has been asked to retain the proper regulator comparison through
the actual filling/localization maps, with the geometric H2 and arithmetic
base components explicitly controlled. The finite frame and tame-symbol
calculations have not yet been replayed by root. The reported Smith factors
are still awaiting the final source-and-certificate audit.

## Primary-source reading

Root opened Guido Kings, *Eisenstein classes, elliptic Soule elements and the
l-adic elliptic polylogarithm*, arXiv:1304.7161v2,
<https://arxiv.org/pdf/1304.7161>. The full text of Sections 4.4--4.7 was read
through retrievals turn1089view0--3, turn1091view0--2 and turn1092view0--1.
This includes the proofs of Proposition 4.4.1, Theorems 4.5.2 and 4.5.5,
Proposition 4.5.8, Theorem 4.6.3 and Theorem 4.7.1.

The integral logarithm-sheaf isomorphism precedes the rational splitting
used by `comp`. The moment comparison retains `1/N^k`. The theta-unit
comparison requires `gcd(c,6*l*N)=1`. These readings do not identify the
current cusp symbols with Kings's Eisenstein classes.

The printed unrestricted formulation of Proposition 4.5.3 needs its scope
checked. The application here is to a sheaf with nilpotent augmentation.
For comparison, a rank-one F3 local system with a nontrivial degree-two
elliptic character retains that character under every `[3^s]`: the induced
map on its C2 quotient is multiplication by `3^s=1 mod2`. Thus the proof's
claimed trivialization by an l-power isogeny needs the pro-l/unipotent
scope in this application. No unrestricted version is being used here.

The screenshot calls turn1090view0--2 returned textual image placeholders
to this runtime. They are not counted as visual source inspection; the
reading above used the complete extracted text.
