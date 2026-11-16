# A183 primary-source and map audit

Source: `sections/two_inert_first_weight_vanishing.tex`.
Certificate: `code/two_inert_first_weight_certificate.py`, retained output/data.

Opened the author's Milne *Arithmetic Duality Theorems*, second edition,
https://www.jmilne.org/math/Books/ADTnot.pdf:

- I Corollary 4.15, printed page 62 (PDF page 69): finite cohomology for a finite module with its order inverted and a finite omitted set.
- II Proposition 2.1 and its proof, printed pages 163–165 (PDF pages 170–172): exact Brauer invariant sequence for an open ring of integers. A183 uses one finite omitted prime and complex archimedean places to get zero Brauer group on O_F[1/3].
- II Proposition 2.9 and its proof, printed pages 170–171 (PDF pages 177–178): group/etale comparison. A183 supplies the exact degree-two injection independently using the universal finite-etale pro-cover and torsor-killing of its H1; it does not assume a K(pi,1) assertion.

Opened Uwe Jannsen, *Continuous etale cohomology*, institutional primary scan,
https://epub.uni-regensburg.de/26684/1/jannsen12.pdf:

- (1.6), (2.1), Theorem (2.2), (3.1): continuous cochain/derived inverse-limit comparison, retaining the H1 lim1 term until finite-group Mittag–Leffler removes it.
- (3.6), (3.8), (3.15)–(3.16): localization/support and inverse-limit maps. The arithmetic discrete-valuation-ring purity calculation itself is supplied in A183 from the strict-henselian tame pro-three inertia Z3(1). No smooth-over-a-field hypothesis from the later purity example is imported into the arithmetic scheme.

Existing bibliography keys BIR_MilneADT and BIR_Jannsen1988 already identify these exact primary texts.

The finite certificate executed successfully:

- 3 exact cubic factorizations, 9 added primes and all three residue-size valuations v3(Q-1)=1;
- 9,837 finite procyclic/transfer elements;
- 6,860 literal truncated coefficient actions and 256 cup-cocycle identities;
- exact integral division of T^14 by L2, with remainder divisible by 9;
- T^13 congruent to -3T^7 modulo (9,L2);
- 126 nonzero integral inertia determinants and the order-nine support-kernel calculation.

Root and Birational independently audited the complete proof and the explicit s<=14 argument. Both requested two literal TeX repairs and a clearer quantifier for the detecting index; all are applied. The final statement proves o_1=0 and o_14 !=0, so the least detecting weight index lies between 2 and 14. It does not determine that least index.
