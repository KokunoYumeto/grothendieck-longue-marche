# Root review: actual modulo-three symplectic centralizer test

Reviewed 2026-11-16, approximately05:51–05:57UTC. Accepted in its exact
finite-quotient scope. The independent program
code/verify_B62_symplectic.py and its actual stdout are retained.

## Geometric representation

The connected double cover of the sphere branched over the twelve
vertices is defined by the homomorphism sending every puncture meridian
to1 in C2. Every orientation-preserving mapping class preserves this
homomorphism, and thus lifts to the branched cover. The two lift choices
differ by the deck involution, whose action on integral first homology
is−I. Isotopies lift as well. Hence the projective homology action defines
a genuine homomorphism from the full twelve-point sphere mapping class
group to PSp10(F3). Its kernel is therefore A5-invariant.

Removing the disk containing the twelfth branch point identifies this
with the eleven-strand Burau representation at−1, after the invariant
line is removed. Capping the one lifted boundary changes no H1. The full
twist acts by−I, so projectivization kills exactly the relevant scalar
ambiguity. The computation uses the ACTUAL common-base braid words
certified in B61, including their relative transport.

Primary checks: Gambaudo and Ghys(2005), Braids and Signatures,
Bulletin de la Societe mathematique de France133(4),541–579,
DOI10.24033/bsmf.2496, https://www.numdam.org/article/BSMF_2005__133_4_541_0.pdf,
Section2.2 Proposition2.1 and the integral chain computation in2.3;
Brendle, Margalit and Putman(2015), Inventiones mathematicae200,263–310,
DOI10.1007/s00222-014-0537-9, the introduction's Hyperelliptic Torelli vs
Burau passage. Both were opened. The latter explicitly gives the
integral splitting and the full-twist action. No index or image theorem
for the integral symplectic group is needed.

## Independent finite computation

The root program starts from the original common-base braid words and
uses the invariant alternating-covector hyperplane in Z^11, rather than
the discovery program's quotient by the all-ones vector. These models
are integrally isomorphic because that covector evaluates to1 on the
fixed vector. The explicit basis change is checked only after the new
group enumeration.

All braid/inverse relations and full twist=-I pass. Direct independent
enumeration gives tetrahedral image order144, cyclic image order1440,
common subgroup C3, and tetrahedral derived subgroup order24. The common
C3 meets that derived subgroup trivially. All19 matrices then match the
discovery program through the explicit integral basis change. An initial
review assertion tested cube=I as a matrix rather than projectively;
it was corrected to cube=±I before the successful run. This changed no
computed group or mathematical claim.

## Integral homology and completion

B58 gives zero in the completed ambient pure-group abelianization,
which is Zhat^55 modulo the full-twist all-ones vector. The chosen
tetrahedral lifts have identically zero pair-linking in row(4,6).
Therefore their zero class in the quotient forces the full55-coordinate
linking vector itself to vanish. This removes the central ambiguity;
it must not be omitted from the proof.

The55-by13 matrix has a primitive integral kernel of rank7, with an
identity minor on its free source coordinates. Root recomputed that
basis and evaluated all seven corresponding actual words. Their finite
images belong to the order24 derived subgroup. Finite free-module
exactness after tensoring with Zhat identifies the completed kernel;
the finite abelianization consequently vanishes on that whole kernel.
An element of K therefore maps both into the derived subgroup and the
common C3, and is trivial in this finite quotient.

The image is genuinely nonnilpotent: the order144 subgroup has derived
order24, whereas a nilpotent group of order2^4*3^2 has abelian Sylow3 and
derived subgroup of2-power order. The accepted result is q(K)=1 and the
corresponding B52 two-factor refinements containing ker(q). It does not
prove K=1, a3-adic statement or arbitrary refined-product closure.
