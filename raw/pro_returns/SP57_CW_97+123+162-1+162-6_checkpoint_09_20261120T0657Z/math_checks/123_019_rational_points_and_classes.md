# Targeted checks prompted by 123/019

The supplied witness texts locate claims for checking; the final transcription is decided separately from the scan. These arguments use elementary constructions, with no outside research.

## The rational-point step over an infinite field

Let k be infinite and U a nonempty k-open subscheme of affine n-space. Choose a nonzero polynomial f whose principal open D(f) is nonempty and lies in U. A nonzero polynomial over an infinite field does not vanish at every k-point: induct on n, choosing values for the first n−1 variables for which a nonzero coefficient in the last variable remains nonzero, then choose the last value outside the finitely many roots. Thus D(f)(k), and hence U(k), is nonempty. Characteristic-zero fields are infinite. This proves the elementary step used after the source's assertion that the compatible e form a dense open in g(2); it does not prove that orbit assertion or the existence of the needed Levi subgroup over k.

## What the semilocal extension requires for this step

Let R be semilocal with finitely many maximal ideals and infinite residue fields. Suppose an open U in affine n-space over R meets each closed fiber in a nonempty open. The preceding argument supplies a point in each such residue-field open. The Chinese remainder theorem lifts their coordinates simultaneously to a point of R^n. The inverse image of the closed complement of U is a closed subset of Spec R containing no maximal ideal, hence is empty. The lifted point lies in U(R).

This proves the elementary open-affine step under the stated fiber and residue-field hypotheses. It does not prove the complete semilocal group-theoretic assertion in the source. In particular, the literal condition char(R)=0 alone does not imply that residue fields are infinite: take R=Z localized at (2), and U=D(t²−t). This is a nonempty open even in the closed fiber as a scheme, but U(R) is empty because every residue in F₂ satisfies t²−t=0, so t²−t is never a unit. If the source's provisional characteristic-zero condition means a Q-algebra, the residue fields are indeed infinite. No intended interpretation is silently imposed on the transcription.

## Explicit noninjectivity examples for c to c-prime

For each positive d, the polynomial representation Sym^(d−1)(k²) has SL₂ diagonal weights d−1,d−3,...,1−d. In the monomial basis the matrices E,F,H in the companion script satisfy [H,E]=2E, [H,F]=−2F, [E,F]=H exactly. The degree is zero in determinant: the weight sum is zero; the elementary unipotents are unipotent. These polynomial actions therefore give homomorphisms into SL_n for direct sums of total dimension n.

The weight cocharacter defines a parabolic preserving the descending weight flag. Two sorted weight multisets with identical ordered multiplicities give the same parabolic type; choosing compatible ordered bases makes their flags equal. Distinct multisets give nonconjugate cocharacters because their eigencharacters differ. This supplies explicit examples without needing a classification theorem.

- A₂ (n=3): partitions 3 and 2+1 give weights (2,0,−2) and (1,0,−1); both give the full flag, so the parabolic map is not injective.
- A₃ (n=4): partitions 3+1 and 2+1+1 give weights (2,0,0,−2) and (1,0,0,−1); both give the flag of dimensions 1 and 3, so the map is also not injective here.
- A₄ (n=5): partitions 5 and 3+2 give weights (4,2,0,−2,−4) and (2,1,0,−1,−2); both give the full flag, again noninjectively.

The script enumerates all partitions of 3,4,5 solely as a convenient finite collection of these constructions and records every collision it finds. It does not claim to have proved that the partition list exhausts the source's classes.

The margin's grammatical reference is not fixed by this calculation. If its “cela l'est pour A₃” were interpreted as injectivity of c to c-prime on all these Dynkin classes, the explicit A₃ pair would contradict that interpretation. The page may refer to another preceding property; the transcription and apparatus must retain that ambiguity rather than change the written rank or assertion to match this check.

## Scope left as background

The general reductive-group representability and descent statements, rational Levi existence in the source's generality, Deligne's construction, the full Kostant correspondence, equivalence of the displayed rational-point conditions, the quasi-split implication under its intended stabilizer hypotheses, and the outer-automorphism stabilizer question are not proved by these checks. The handwritten stabilizer square is read as ink independently of the expected group or Lie-algebra interpretation of its lower-right letter.
