# Direct cote 145 audit, 2026-11-16

Official source: https://grothendieck.umontpellier.fr/145.pdf, 10,752,928 bytes, SHA-256 43fed9b7b11b4eeaf1bc6a067de1f4ceb07a16645349d5216cca2ab119846f3d. The archive's cover identifies the manuscript as *Autour de la « Longue Marche » à travers la théorie de Galois*, spring 1981 old redaction, cote 145, 37 manuscript pages. The PDF has 38 pages including that cover. Here a scan number is its one-based PDF position, matching the supplied note; the printed archive/manuscript page number is one less. Raw scans and rendered image crops are excluded from research archives; retrieval code and this reading record are preserved.

## Opened and visually read

Root inspected scans 1, 7–12, 22, 27–29, including higher-resolution crops of 11, 12, 22 and 28. A second auditor independently inspected 7, 8, 11, 12, 22, 27–29. No OCR transcription is treated as authority.

- Scan 7: the uncancelled equations are u(l0)=l0^p and u rho=Int(g) rho u.
- Scan 8: rho sends l0 to l1 and l1 to linfinity, with l0 l1 linfinity=1. It is the order-three cycle, not a transposition. The displayed formulas explicitly give u(l1)=g l1^p g^-1. The same scan gives the gauge g -> l0^a g l1^-a.
- Scans 9–10: outer commutation with the transposition sigma_infinity gives g l1^q sigma_infinity(g)=l0^r. Its abelianization forces q=-r. The complex-conjugation example has p=-1, g=l1, q=-1 and r=1.
- Scan 11: gamma is the orbit of g for the displayed action phi(a)g=l0^a g l1^-a; chi is the cyclotomic character. Thus the raw pair is ([g],p), not literally ([g^-1],p). Inversion changes the gauge to f -> l1^a f l0^-a. The function beta is distinct from any frame primitive.
- Scan 12: the uncancelled top relation reads sigma_infinity(g^-1)=l0^beta g l1^beta. The lower derivation is crossed out and is not used. This top relation gives beta=-e0(g)-e1(g). The inverse on the left is visible in the high-resolution original crop.
- Scan 22, equations (11)–(12): the sign-graph copy of S3 in S3 times C2 fixes the equianharmonic point P and has a canonical lift to the extension. This is the precise finite isotropy splitting; its orientation-preserving subgroup is the elliptic order-three subgroup.
- Scans 27–28: the harmonic points are 2, -1, 1/2, also named 0',1',infinity'. Their stabilizers include the transposition and complex conjugation; their canonical lifts are described. Their orientation-preserving subgroups are the elliptic order-two subgroups. Scan 29 continues the corresponding fixed-locus discussion.

## Exact normalization, beyond the supplied note

Write x=l0, y=l1 and g_ab=(A,B) in Zhat^2. The raw conjugator f0=g^-1 satisfies u(y)=f0^-1 y^p f0. It need not lie in F': for complex conjugation, g=y and f0=y^-1, while the usual commutator-normalized GT coordinate is 1.

Normalize the outer representative by u'=Int(x^-A)u. Its commutator-normalized conjugator is

f_GT = y^B g^-1 x^A in F'.

Indeed g'=x^-A g y^A, and g' y^-(A+B)=x^-A g y^-B=f_GT^-1. The last right multiplication centralizes y, so it changes no automorphism value. This f_GT is exactly invariant under the manuscript gauge. Thus the manuscript pair corresponds to the normalized GT pair through this explicit formula; merely saying 'up to gauge' conceals both inversion and peripheral-centralizer normalization.

For the class-two check let c=[x,y] and use normal forms x^a y^b c^d, with multiplication d+d'-a'b. Then rho(y)=x^-1 y^-1 c^-1, u(y)=y^p c^(Ap), and u(c)=c^(p^2). The intertwining equation on y gives

u rho(y)=x^-p y^-p c^(-Ap-p^2),

Int(g) rho u(y)=x^-p y^-p c^(Bp-p(p+1)/2).

Hence A+B=(1-p)/2 and beta=(p-1)/2. All formulas are integral in Zhat: p is a unit and therefore odd, the binomial expression is an ordinary integral continuous polynomial, and Zhat has no additive torsion. The coefficient at two is included. This identifies beta as the cyclotomic half-difference. It supplies no formula equating it to a frame coordinate.

## Frame comparison

For a fixed splitting j:H->E, a frame A_frame satisfies u composed with j=Int(A_frame) composed with j (with the specified automorphism of H, when present). Its ambiguity is right multiplication by the geometric centralizer of j(H). For rho, the actual cocycle is g=A_frame rho(A_frame)^-1. The same construction applies to the order-three and order-two orientation-preserving isotropy splittings found in the scans. It does not identify a finite quotient of g with a finite quotient of its primitive frame.

The main identification is now based on the original scans and is no longer conditional on EXPERT_ON_INTAKE_11. The supplied note's literal gamma=f identification is corrected by inversion and the displayed normalization. The earlier conditional D1 is superseded, not evidence that the scans had been read earlier.
