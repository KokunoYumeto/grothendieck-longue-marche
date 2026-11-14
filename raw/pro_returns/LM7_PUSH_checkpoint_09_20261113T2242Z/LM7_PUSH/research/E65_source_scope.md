# E65: exact source scope and independent reviews

The proved result is a continuous quadratic character on the full gentle
profinite group. Its restriction to full profinite GT is not evaluated.
The explicit map is E65.6, with the multiplier-one finite formula E65.4.
The E3 comparison uses the actual sequence F -> F sigma^(-1) -> H^3,
which preserves the character and produces V12=q12(f)=I and an actual
automorphism of the specified G6. No Kummer-surjectivity hypothesis enters.

## Primary sources reopened

- Ivan Marin, *Characters of the Grothendieck--Teichmüller group through
  rigidity of the Burau representation*, author PDF
  <https://www.lamfa.u-picardie.fr/marin/arts/gtrig.pdf>, version dated
  13 June 2007, PDF pages 7--8, Section 4, Lemmas 4.1--4.3. Published in
  Annales de la Faculté des Sciences de Toulouse 17(4) (2008), 765--780,
  DOI <https://doi.org/10.5802/afst.1202>.
  The displayed equations in Lemma 4.3 give v=lambda in its w=0 branch;
  the printed proof's v=1 is a typographical error. E65 uses the equations
  themselves and the nonabelian branch, with the exact normalized matrix
  [[lambda,lambda*u],[0,1]]. Both root and arithmetic reopened this source.
- Nakamura--Schneps, *On a subgroup of the Grothendieck--Teichmüller group
  acting on the tower of profinite Teichmüller modular groups*, Inventiones
  141 (2000), 503--560, author PDF
  <https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf>, Definition 5.1,
  Lemma 5.1 and Corollary 5.2. The rho2 frame and its cocycle are defined
  on full GT. The later additional relations are not imposed on GT here.
- Lochak--Schneps, *Open problems in Grothendieck--Teichmüller theory*,
  <https://webusers.imj-prg.fr/~leila.schneps/farb.pdf>, Question 1.2.
  It asks whether the cyclotomic map is the entire abelianization of full
  profinite GT. It gives no vanishing theorem for the E65 character.
- Furusho, *Geometric and arithmetic subgroups of the
  Grothendieck--Teichmüller group*, Math. Res. Lett. 10 (2003), 97--108,
  <https://www.math.nagoya-u.ac.jp/~furusho/paper/GTA-mrl.pdf>, Theorem 3.1
  and Theorem 3.4. The duplication argument uses the additional harmonic
  relation IV; those conclusions are not transferred to every full-GT
  element in this work.
- Enriquez, *Quasi-reflection algebras and cyclotomic associators*,
  <https://arxiv.org/pdf/math/0408035>, Theorem 8.1 and Remark 8.6, are the
  actual full-GT cyclic-cover comparisons retained in D5. They are a
  potential further finite test, not a proved value of the E65 character.
- Nakamura--Tsunogai, RIMS Kokyuroku 1267 (2002), 197--208,
  <https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1267-18.pdf>,
  Theorems 1--2 on printed page 199, explicitly place the harmonic and
  equianharmonic identities on the Galois image. Their stated source is
  retained.

## Proof reviews and preserved source

Geometry read the entire E65 proof, including the arbitrary-multiplier
frame cosets and covariance, signed transport and compact extension, and
passed it. Its two requested changes were the missing backslash in E65.13
and the explicit cube in the final E3 comparison. The earlier source is
preserved in `E65_initial_reviewed_draft.tex`.

Root read the final proof and every line of the standard-library finite
certificate and passed them. Root also reopened Marin's exact displayed
equations. The finite certificate checks every product and normalizer
conjugation in the displayed Cartans, not a selected sample. It does not
represent a finite enumeration of the whole GT group.

The remaining unresolved quantity is exactly the image of
Delta restricted to full profinite GT. No primary result found in this
source audit assigns that image, and no nonvanishing or vanishing claim
is inferred from a prounipotent realization.
