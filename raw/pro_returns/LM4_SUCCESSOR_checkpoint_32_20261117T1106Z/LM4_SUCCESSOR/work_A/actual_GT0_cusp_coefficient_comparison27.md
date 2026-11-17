# The canonical cusp coefficient is C44's actual relative Alexander unit

Research, checkpoint 27. This note supplements the frozen V4/Fox proof and the separately reviewed half-rotation and canonical-frame notes. It identifies the remaining coefficient with an already proved full unit. It does not prove equality with the dihedral multiplier or decide Main A.

## 1. Exact authoritative dependencies and normalization

The formal source `work_A/A_involutions.tex`, statement A.45, equations (A.45.1) and (A.45.2), defines the actual universal-dihedral value by

    pi(x)=a, pi(y)=a T, pi(u)=T^k,
    k in 2 Zhat, d_alpha=2k+1 in Zhat^times.

The statement and its complete proof explicitly give `(d_alpha)_2 = 1 mod 4`. This is the exact input used in Section 2 of `actual_GT0_canonical_cusp_frame27.md`; its SHA256 is `4b415cab71ac49b4de0af2de00512c3b94a6360f4b0e01195fc4a6e6dee8b794`. The formal proof was reread in full for this binding. In particular the dihedral exponent k is not the abelianization coordinate introduced below.

Retain the actual negative-GT0 data, z=(xy)^-1, v=Inn(u^-1)iota and tau=alpha v. The unique zero-abelianization cusp transporter h0 satisfies

    tau(z)=h0^-1 z^-1 h0,
    h0 tau=q tau q^-1,
    q_ab=(t,-t).

Here q is unique by the actual regular-pants section theorem and its trivial F-centralizer. Write

    r=h0 tau,   sigma=Inn(h0) tau,
    e=(xu)v,    j=q v q^-1.

The symbol r is a group element in the actual semidirect extension and sigma is its conjugation action on F. The elements e and j both have v-head, so their product belongs to F. These are actual full-group elements, not chosen representatives in a metabelian quotient.

## 2. An explicit instance of C44's unique equation

The half-rotation proof gives

    r e r^-1=e^-1,   e^2=xy=z^-1.

Because r=q tau q^-1 and tau commutes with v, the element j commutes with r. Also j^2=1. Consequently the actual even word

    g=e j=(xu)v q v q^-1 = x u v(q) q^-1

satisfies

    sigma(g)g^-1
      = (e^-1 j)(j e^-1)
      = e^-2
      = z.

The normalized sigma is a regular negative pants involution and sends z to z^-1 literally. Thus this is exactly equation (C.44.1), with the same sign and multiplication order, in `work_CE/C44_regular_Alexander.tex` (also included in `work_CE/C_further.tex`). Its complete proof supplies uniqueness of g and says that the image of g in F/normal-closure(z), with generator the image of x, is a full profinite unit. No change of peripheral marking or assumption of full generation is inserted.

## 3. Exact coefficient calculation

On F_ab, v is the coordinate swap and u has zero image. Hence

    g_ab=(1,0)+(-t,t)-(t,-t)=(1-2t,2t).

Killing z imposes y=x^-1. Therefore C44's actual relative Alexander unit for this specific normalized sigma is

    a_reg=1-4t in Zhat^times.

In particular this proves that 1-4t is a full unit, not just a dyadic unit. It follows from the actual all-head Alexander argument in C44; no maximal pro-p substitution is made here.

The canonical full word from the preceding note is

    Omega_alpha=(x^d v)(q^-1 e q)^(-d),   d=d_alpha.

Its abelianization can now be written as

    (Omega_alpha)_ab=((d-a_reg)/2, -(d-a_reg)/2).

Both d and a_reg are 1 modulo 4 at two, so the displayed divisions are defined uniquely in Zhat. The necessary coefficient condition for the exact full cusp criterion is precisely

    a_reg=d_alpha.

This equates two explicitly defined actual full units: the universal-dihedral value of canonical u and the relative Alexander value of the unique regular cusp equation. The equality has not been deduced here. In particular one must not identify the dihedral rotation exponent k with the abelianization coordinate t of q. C44's pronilpotent relative conjugacy does not preserve the three original peripheral markings and cannot by itself supply that comparison.

## 4. End-state and exact remaining gate

The complete actual marked criterion is the single literal equality Omega_alpha=1. Its first coefficient vanishes exactly when a_reg=d_alpha. The present argument proves that both sides are actual full units and identifies a_reg by a literal full-group solution of C44, but it proves neither their equality nor the subsequent nonlinear vanishing. The accepted dyadic square relation involving c2(u) for full GT involutions is not promoted to other primes or to negative-GT0 data in general. No counterexample, generic ring construction, finite census, or all-P conclusion is asserted.
