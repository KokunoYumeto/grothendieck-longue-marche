# Independent audit of D.68

**Result: PASS.** I read the full current proof, metadata, and exact producer, and independently reran the producer. No mathematical correction is needed.

## Exact input and labelled basis

The actual order-four lift is the D.46 lift. D.55 supplies both the square action \(A_p(a)^2=-I\) and the unit two-primary cusp exponent for the positive involution. If \(A_2(a)\) were identity modulo two, its square would be identity modulo four. Its reduction is therefore the nonidentity unipotent matrix, with one fixed nonzero dual character.

All three rows of D.68f have actual inverse free-word substitutions. I separately checked the less immediate second row \(x=XYX^{-1}, y=X^{-1}\): its inverse is \(X=y^{-1},Y=yxy^{-1}\), and the commutator remains exactly \([X,Y]\). The third row also preserves the commutator literally. Thus the cusp is not silently conjugated or rescaled.

## Actual double cover and the norm obstruction

The Schreier basis is \(u=x^2,B=y,C=xyx^{-1}\), and \(c=CB^{-1}\). Deck conjugation fixes \(u\), takes \(B\) to \(C\), and takes \(C\) to \(uBu^{-1}\). The displayed integral inclusion matrix and its kernel \(\widehat{\mathbb Z}([C]-[B])\) follow directly.

For a cusp-normalizer element \(v\) above the order-four label, \(v^2\) lies over the positive square, so D.55 applies to the literal relation \(v^4=c^\kappa\) and gives \(\kappa_2\) odd. Conjugation by \(v\) commutes with the deck action on homology because \(vxv^{-1}\) has the same nonzero character as \(x\). On the rational handle summand its square is \(-I\), and on the boundary line its square is \(+I\). Hence \(T^2=-J\) holds rationally at each prime, and torsion-freeness makes this the stated integral identity.

At two the boundary action is \(+1\). Therefore the fourth norm is exactly \(2(I-J)\), with image \(2\mathbb Z_2 b\). Writing \(v=ns\) under the hypothetical zero character gives the actual norm formula for \(v^4\); its boundary coefficient contradicts the odd coefficient \(\kappa_2\). This proves the nonzero character label.

Once the label is known, the inner factor \(f_0\) of \(v=f_0s\) acts on the cover homology by the deck matrix \(J\), so \(T=JS\) and \(S=JT\). I checked the sign on the boundary: \(Sb=-\lambda b\).

The full matrix D.68n is uniquely determined by \(TJ=JT\), \(Tb=\lambda b\), and \(IT=A(a)I\). Its half coefficients are integral for the stated exact mod-two character. No integral eigenspace splitting at two is used.

## Full quotient and finite labels

The character \(\ell(u)=0,\ell(B)=1,\ell(C)=-1\) is a character of the actual cover group. Deck conjugation negates it, and the computed matrix gives \(\ell\alpha=-\lambda\ell\). Its kernel is therefore normal in \(F\) and invariant under the actual automorphism in both directions.

The map \(x\mapsto t,y\mapsto r\) identifies its kernel with the exact normal closure of \(x^2,(xy)^2\). Both presentation maps are given, and their composites fix the named generators. The full rotation subgroup is \(\widehat{\mathbb Z}\), detected by the surjective character. The cusp image is exactly \(r^{-2}\).

The induced formulas \(r\mapsto r^{-\lambda}\), \(t\mapsto r^jt\) give square translation \((1-\lambda)j\). Fourth order upstairs forces twice that translation to vanish; multiplication by two in \(\widehat{\mathbb Z}\) is injective, proving the displayed equation. In the actual semidirect quotient the square of \(r^mts\) is \(r^{(1+\lambda)m-j}s^2\); its fourth power and the cusp relation give \(j=(1+\lambda)m+\kappa\). In particular \(j_2\) is odd.

At an odd negative coordinate, \((1-\lambda_q)j_q=2j_q=0\) gives \(j_q=0\) in \(\mathbb Z_q\), so both named generators of the actual \(D_{2q}\) quotient are fixed. At a positive coordinate the rotation is inverted and the quotient action has exact order two. The displayed finite maps are obtained from the full quotient, not inferred from matrix models.

## Producer and scope

The producer's word reduction, Schreier rewriting, integral matrix operations, and finite dihedral multiplication conventions agree with the proof. The exact rerun returned PASS:

- 32 integral double-cover models;
- 1,112 finite dihedral models;
- 147,860 total exact checks.

The total comprises the recorded free-word inverse and cusp checks, the actual geometric control, matrix and norm identities, finite automorphism-square checks, and the labelled cusp-root formula.

The result and metadata retain the actual conclusion: the dihedral action has order two, although the source representative has order four. Neither a negative scalar full action nor its exclusion is inferred from the finite models. No full section-generation or conjugacy assertion is added.
