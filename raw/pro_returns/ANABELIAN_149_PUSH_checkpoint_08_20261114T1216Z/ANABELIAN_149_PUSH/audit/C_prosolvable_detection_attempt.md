# Prosolvable detection by rational covers: exact remaining gap

This note is a failed-route audit. C4 is now completely determined by C.7h through primitive valuation uniqueness; the abstract prosolvable-cofinality question below remains a limitation of this separate detection method, not an unresolved C4 obligation.
The integrated C.7d proves that the full ordinary cyclotomic fixed group
acts trivially in every finite covering monodromy representation whose
covering curve has genus-zero compactification. Write N0 for the common
kernel of those representations. C.7d also proves N0 is nontrivial by
the missing-simple-composition-factor argument. That fact does not decide
the image of N0 in the maximal prosolvable quotient, and does not construct
an arithmetic fixed element.

## The required statement is cofinal, with the given generators

For a specified finite solvable quotient phi:Fhat2→Q, the desired
conclusion N0⊂ker(phi) is equivalent, by compactness, to the existence
of finitely many genus-zero monodromy quotients whose kernels have
intersection contained in ker(phi). Realizing an abstract group
containing Q, or embedding Q into a wreath product, is insufficient:
the maps out of the specified free profinite group must be compatible.
Residual detection of discrete words is also insufficient.

## A cyclic wreath step and the repeated-prime obstruction

Let f:P1→P1 be a rational Belyi cover, and let c be an unramified point
above1. Place a boundary point over infinity at infinity in the source.
One can compose f with z↦z^q+c. In the Galois closure of f, the divisors
of the conjugate functions x_i−c have coordinate-supported valuations
at places above1. However, the nonzero coefficient is the ramification
index of the NORMAL CLOSURE above1, not1. If q is coprime to that index,
these valuations prove the necessary Kummer independence, and in the
clean case q∤|H| the construction gives the full wreath C_q wr H.

This argument cannot be iterated with one fixed prime p without a new
step. After an earlier p-cover ramifies above1, the normal-closure
ramification index there is divisible by p. The coordinate-supported
valuation then becomes zero modulo p and gives no independence.

There is a decisive independent group check. For a finite transitive
permutation group H, the abelianization of C_p wr H is
C_p×H_ab. Therefore the third repeated full wreath
C_p wr(C_p wr C_p) has abelianization C_p^3. It requires at least three
generators and cannot be a quotient of Fhat2. Thus a claim that rational
tripod covers supply all repeated full-p wreath groups is false.

The elementary abelianization formula follows by taking coinvariants
of the base module F_p^Omega under the transitive H-action: the sum
of coordinates identifies the coinvariant module with F_p. The quotient
to H remains, giving the displayed direct product.

This coefficient error was independently caught and acknowledged in
the exchange between degeneration and topos. New-prime steps remain
valid, but do not settle repeated-prime embedding problems, nor the
compatibility of the two distinguished generators in an arbitrary
solvable quotient.

## Status

No cofinal prosolvable detection theorem has been established here.
No conclusion about the prosolvable image of N0, or about the residual
full fixed group at point2 or tangent coefficient1, is promoted.
The full maximal-pro-p image results C.7a–C.7c remain intact.
