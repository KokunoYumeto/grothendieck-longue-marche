# Cote 145: independent scan and normalization audit

Date: 2026-11-16. Auditor: `/root/c_lifting_audit`. No root manuscript file was edited.

## Directly inspected sources

I opened the official local page images `work/primary/cote145_page_07.png`, `_08.png`, `_09.png`, `_10.png`, `_11.png`, `_12.png`, `_22.png`, `_27.png`, `_28.png`, `_29.png`; the detail crops `cote145_detail_11.png`, `_22.png`, `_28.png`; and the high-resolution uncancelled top-line crop `cote145_relation12.png`. These are PDF scan ordinals. The printed footer is one less. The earlier reading and its explicitly superseded beta uncertainty are preserved in `work/c_cote145_independent_audit.md`.

## Reading verdict

* Scan 7 has `u(x)=x^p` and `u rho=int(g) rho u`.
* Scan 8 explicitly uses `rho(x)=y` and `rho(y)=l_infty`; rho cycles the three labels and is not a transposition.
* Scan 11 defines gamma as the orbit of g under `g -> x^a g y^{-a}`, while chi is cyclotomic. Thus in the unnormalized convention `u(y)=f^{-1}y^p f`, the literal relation is `g=f^{-1}`, not `g=f`.
* Scans 9–10 state the additional manuscript-domain condition `g y^q sigma_infty(g)=x^r`, where sigma_infty swaps x and y. Scan 10 explicitly checks complex conjugation with `g=y`, `q=-1`, `r=1`.
* The high-resolution uncancelled top line of scan 12 reads `sigma_infty(g^{-1})=x^beta g y^beta`. The inverse is on the left; the right-hand g is un-inverted. The crossed-out lower argument is not used.
* Scan 22 displays the sign graph `S_3 -> S_3 x C_2`, `sigma -> (sigma,sgn(sigma))`, and its canonical isotropy lift at the equianharmonic point P.
* Scans 27–28 identify canonical isotropy lifts at 2, -1, 1/2; scan 28 labels these `0'=2`, `1'=-1`, `infty'=1/2`. Scan 29 continues their lift comparison.

## Independent exact normalization

Write the abelianization of g as `(A,B)` in the x,y basis. Applying the action equation to x gives

\[
u(y)=g y^p g^{-1}.
\]

Define

\[
f_0=y^B g^{-1}x^A.
\]

Then `f_0` has zero abelianization. Under the allowed gauge, the coordinates become `(A+a,B-a)` and

\[
y^{B-a}(x^a g y^{-a})^{-1}x^{A+a}
=y^B g^{-1}x^A.
\]

Thus the normalized f_0 is literally gauge-invariant. Put `u_0=int(x^{-A})u`. Its y-conjugator is `x^{-A}g`, whereas `f_0^{-1}=x^{-A}g y^{-B}`; the two differ by a right y-power. Therefore

\[
u_0(x)=x^p,\qquad u_0(y)=f_0^{-1}y^p f_0.
\]

For complex conjugation the manuscript has `g=y`, so `(A,B)=(0,1)` and `f_0=1`, exactly as the standard normalized pair requires. The unnormalized `g^{-1}=y^{-1}` would not be in the commutator subgroup.

## Independent class-two calculation

Use `c=[x,y]=xyx^{-1}y^{-1}` and the normal form `x^a y^b c^k`, so `yx=xy c^{-1}`. The three-cycle has

\[
\rho(x)=y,\qquad \rho(y)=(xy)^{-1}=x^{-1}y^{-1}c^{-1},
\qquad \rho(c)=c.
\]

Since `u(y)=y^p c^{Ap}` modulo class three,

\[
u\rho(y)=x^{-p}y^{-p}c^{-Ap-p^2}.
\]

On the other side, `(x^{-1}y^{-1}c^{-1})^p` has central exponent `-p(p+1)/2`; applying rho to `c^{Ap}` adds `Ap`, and conjugating by g adds `p(B-A)`. Hence

\[
\operatorname{int}(g)\rho u(y)
=x^{-p}y^{-p}c^{pB-p(p+1)/2}.
\]

Equality and the fact that p is a profinite unit give

\[
A+B=(1-p)/2.
\]

The half is well-defined in the profinite integers because every unit is odd at the 2-adic component; multiplication by 2 is injective. This derivation uses only the displayed three-cycle compatibility.

On the additional manuscript domain of the sigma_infty relation, abelianizing `g y^q sigma_infty(g)=x^r` gives

\[
r=A+B,\qquad q=-A-B.
\]

Inverting the relation yields `sigma_infty(g^{-1})=x^{-r}g y^q`, identifying beta with q. Consequently

\[
\boxed{\beta=-A-B=(p-1)/2}.
\]

This agrees with the manuscript's complex-conjugation check `beta=-1`. It does not turn beta into a coordinate of a frame primitive.

## Scope and frame distinction

For a transported isotropy lift, `A rho A^{-1}=A rho(A)^{-1}rho` gives the multiplicative coboundary `g=A rho(A)^{-1}`. A is the frame/conjugator; g is the resulting cocycle. This is independent of the above normalization of the peripheral representative. The normalized pair is a GT-style pair, but the displayed equations do not establish the pentagon or membership in full GT. The sigma_infty equation must be restricted to the manuscript's stated domain, rather than inferred for every three-cycle-compatible automorphism.

Final verdict communicated to root: the normalized dictionary, three-cycle correction, canonical isotropy identifications, and beta formula are independently confirmed. The corresponding root exact class-two program is `deliverable/code/d_cote145_normalization.py`; my calculation above was derived independently rather than inferred from that output.
