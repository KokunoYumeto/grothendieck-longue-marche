# The actual coarse annular bundle and its entire height kernel

Status: proved discrete comparison and completed selected-source comparison,
retained as research after the 283-statement formal freeze. Both main decisions
remain Open. We do not complete an infinitely generated height kernel here.

## 1. The actual filling map

We retain the based one-neck annular domain U_ann of B114, with both old
annular base generators. Its fundamental group is the discrete free group
F2. Filling both actual A/B puncture families gives the F-equivariant map
from the original free-swap quotient to

    Q_b,U = {(q,t): q in U_ann, t in P1, t != +1,-1, q t^2 != 1}.

Here F(q,t)=(q,-t), with two distinct constant fixed sections t=0 and
t=infinity. Since U_ann avoids q=0,1 and infinity, the four removed points
{+1,-1,+q^(-1/2),-q^(-1/2)} remain distinct. Locally choosing a square root
exhibits a locally trivial four-punctured-sphere bundle, including the
former A/B critical fibers. Its ordinary fiber group N is F3.

The filling induces the quotient by the normal closure of the filled
meridians. This follows by the usual local disk filling and van Kampen:
each smooth divisor stratum adds its meridian relation, intersections add
no further generator to that kernel, and a transverse perturbation of
paths gives surjectivity. This is the same actual filling construction
already used in B87 and B89; it requires no asphericity claim for the
unfilled total space.

In the common-neck orbifold fiber, the based presentation before filling
is C2(c_-) * C2(c_+) * F5. Four common K meridians are the A-family
peripherals; their cone conjugates supply the B family. Killing their
normal closure leaves exactly

    E_b = C2(c_-) * C2(c_+) * Z(f).

Both cones are the actual selected gap cones. The branch letter
f=d O5 d^(-1) becomes the literal retained branch meridian after d is
filled. Thus the displayed simultaneous marking is inherited from the
common fiber; it is not a choice of unrelated cone conjugacy classes.
The ordinary F3 fiber is the orientation kernel of E_b. The orientation
sends both c_- and c_+ to 1 in C2 and f to 0.

## 2. Two different base splittings

The actual geometric section loops k_- and k_+ project to a free basis
of pi1(U_ann)=F2. Consequently their assignment extends to a splitting
of the orbifold bundle group onto that free base. We obtain an exact
discrete decomposition

    G_b,U = E_b semidirect F2(k_-,k_+).

This splitting generally acts nontrivially on both cone representatives.
In particular, we do not identify it with the fixed-section splitting.
The constant fixed section t=0 instead gives a based subgroup H0=F2
that commutes with its actual order-two cone. In ordinary groups it gives

    Pi_b,U = N semidirect H0,  N=F3.

The involution F fixes H0 pointwise. The constant section at infinity
gives its own corresponding based statement.

## 3. The true coarse height kernel

Choose the sign of the branch height so that lambda(f)=1. Both cones
and both geometric loops k_- and k_+ have height zero. The action of
the base preserves this character because it is the restriction of
the actual global height character. Bass--Serre normal form, or a
Reidemeister--Schreier rewriting with transversal {f^n:n in Z}, gives

    ker(E_b -> Z)
      = *_{n in Z} ( C2(f^n c_- f^(-n)) * C2(f^n c_+ f^(-n)) ).

Because the chosen base section has height zero, the entire actual
coarse height kernel is the discrete group

    ker(lambda:G_b,U -> Z)
      = [ *_{n in Z} (C2(f^n c_- f^(-n))
                     * C2(f^n c_+ f^(-n))) ]
          semidirect F2(k_-,k_+).

The semidirect action is the actual braid action, including its inner
corrections. It is not asserted to be a permutation or a shift of the
listed cone factors. This statement includes every height translate of
both cross-relations. No completion of this infinite free product or
its kernel has been substituted for a subgroup of a full completion.

The tempting smaller group

    (Z(k_-) x C2(c_+)) * (Z(k_+) x C2(c_-))

is false as the whole height kernel. CE's exact signed height-operator
check gives nonzero reduced syllable counts 17,9,9,17 for the four
first positive/negative translates of the two cross-relators, although
the untranslated relations vanish. We retain the rejected proposal and
its genuine calculation in work_CE/annular_neck_height_kernel23.txt,
work_CE/code/check_annular_coarse_height23.py and its output/certificate.
The geometric bundle comparison supplies the correct whole-orbit group.

## 4. Full profinite fixed-source comparison after filling

The selected fixed section identifies H0 with the actual source group.
In E_b, the centralizer of its selected cone is exactly that C2 factor,
both discretely and in the full profinite completion. Discretely this
is the free-product normal-form theorem. The completed statement is
the free-profinite-product torsion centralizer theorem in the precise
form already checked and applied in B87 (Herfort--Ribes Theorem B').
Intersecting with the ordinary orientation kernel gives N^F=1 and
(N-hat)^F=1.

For completeness, the ordinary semidirect product has the required full
completion. Every finite-index subgroup of finitely generated free N
contains a characteristic finite-index subgroup L. Its quotient action
H0 -> Aut(N/L) has finite image. The finite semidirect target
(N/L) semidirect image(H0) detects N/L, proving the full induced topology
on N. Intersecting the finite kernel on H0 with an arbitrary finite-index
kernel in H0 gives cofinal finite semidirect quotients of the whole group.
Thus completion gives the exact split extension

    Pi_b,U-hat = N-hat semidirect H0-hat.

Since F fixes H0-hat, the unique semidirect decomposition shows directly
that (Pi_b,U-hat)^F=H0-hat, and Pi_b,U^F=H0. The orbifold centralizers
are therefore H0 x C2 and H0-hat x C2 respectively. This is a regional
application of the already established B87/B106 method, not a claim
about the unfilled annular group.

The original selected source cover is governed by sqrt(1-q). Its
character on F2 is nonzero on the outer base generator and zero on the
inner one. The source cover is connected and has group F3 by the
index-two Schreier formula. The actual open-subgroup comparison from
B106 transfers the corresponding selected-source equality to that
filled cover. This does not supply the unfilled F11 source-image claim.

## 5. Verification and next gate

Root developed this comparison after reading the complete B87 proof and
the complete CE whole-height and failed-coarse calculation. CE and DE
independently checked the four punctures, actual common-fiber marking,
filling kernel, free base splitting and branch-height kernel; both
reported PASS. Their saved precise action formulas should be used for
any later algebraic elimination. The next unresolved gate is a whole
comparison for the actual unfilled nine-generator presentation, or its
equivalent eight-generator mirror extension. We do not infer a RAAG
description from transverse divisor intersections alone.
