# Original-source access and convention audit

## Anderson 1989: complete original obtained

The official Göttingen archive supplies the complete article at

https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0095/LOG_0011.pdf

The volume manifest is

https://manifests.sub.uni-goettingen.de/iiif/presentation/PPN356556735_0095/manifest

The downloaded PDF has 5,365,119 bytes and SHA-256
`bf656f919b6fb70b372b08a19beff97bcd1c0c89df715df09fa8fd1881f9bc67`.
Its first page is the archive cover. PDF page2 is printed page63, and PDF page70 is printed page131. The source was rendered and OCRed for inspection; only the article's relevant statements and proofs are reported as read. The complete PDF, rendered scans and complete OCR remain research inputs excluded from the deliverable archive.

The exact original anchors are:

| Result used | Original location | Inspection |
|---|---|---|
| Completed coefficient rings, cyclotomic action | §§1.3–1.4, pp.67–68 | Text |
| Unique adelic beta cocycle | Theorem1 and supplement, p.69 | Original scan |
| All-degree Fermat torsion representation | §§5.3–5.5, Proposition5.5.1, pp.86–89 | Text and original p.88 scan |
| Gamma coefficient ring and branches | §§7.1–7.4, pp.95–97; §3.1, p.73 | Text and original p.73 scan |
| Reciprocity and multiplication | Theorem2, p.98; proof pp.101–102; Corollary8.6.3, p.103 | Original theorem and corollary scans; proof text |
| Logarithmic derivative | Theorem5 and proof, pp.116–117 | Original scans and proof text |
| Kummer moments and power series | §11.6, p.117; Proposition11.6.1, p.118 | Original scans |
| Gauss sums | Theorem6, p.118; proof §§12.2–12.8, pp.119–124 | Original theorem scan; full proof text |
| Fundamental-group comparison | §13.1, p.125; Proposition13.3.2, p.126; §§13.4–13.6, pp.127–129 | Original statement and map scans; text |
| Odd moment expansion | §13.7, equation(13.7.3), p.130 | Original scan |

The source makes the coefficient/base-group scope explicit: its beta cocycle is defined on all of G_Q with values in Zhat[[Zhat(1)^2]]^×, and its gamma branches have coefficients in the product of the Witt-vector rings of the algebraic closures of the residue fields. Proposition5.5.1 supplies the semilinear action on torsion of every Fermat Jacobian. Theorem6 then gives the stated Gauss-sum interpolation. Proposition13.3.2 supplies the precise odd-prime fundamental-group comparison, retaining its basis coboundary; RemarkII supplies the cyclotomic-kernel equality also at two.

## Multiplication convention, derived explicitly

Use the compatible positive real roots of a positive integer n and the roots of unity exp(2πi/N), as in the manuscript. Define kappa_n(g) by the quotient of the Galois translate of n^(1/N) and n^(1/N).

In Corollary8.6.3 put a=ns. Its product indexed by nb=a is then the product indexed by b=s+c, nc=0. Division by Gamma_g(ns) and the product of Gamma_g(c) gives

\[
\frac{\prod_{nc=0}\Gamma_g(s+c)/\Gamma_g(c)}{\Gamma_g(ns)}
 =\exp(-2\pi i\,ns\,\kappa_n(g))\otimes1.
\]

Indeed, the exponent in Anderson's real power is the least nonnegative representative of −ns. It differs from −ns by an integer; the corresponding integer power of n is rational and fixed by g. The Galois quotient therefore has exactly the displayed negative exponent. The ratio is independent of the chosen representative of s, since changes are integral multiples of n kappa_n(g).

Anderson evaluates in Qbar⊗W. Ihara II, p.9, evaluates in W⊗Qab. The explicit ring isomorphism z⊗w ↦ w⊗z carries the preceding factor to 1⊗exp(−2πi ns kappa_n(g)). Ihara's character is fixed by (n^(−r))^(g−1)=exp(2πi r Psi_n^(0)(g)), hence Psi_n^(0)=−kappa_n. These two maps account for the tensor placement and sign in D.20.

## Moment convention, derived explicitly

Fix an odd prime ell and g in G_{Q(mu_{ell^infinity})}. Let c(g,zeta) be the Kummer exponent appearing in Anderson §11.6. Its underlying algebraic number is 1−zeta^(−1). Since

\[
1-\zeta^{-1}=\zeta^{-1}(\zeta-1),
\]

and every ell-power root of zeta is fixed by g, this Kummer character equals the character of zeta−1. Changing a root branch multiplies it by a root of unity fixed by this same group. This is the exact branch comparison used here.

For m>1 set

\[
S_n=\sum_{0<i<\ell^n}i^{m-1}c(g,\zeta_{\ell^n}^{i}),\qquad
U_n=\sum_{\substack{0<i<\ell^n\\\ell\nmid i}}
                  i^{m-1}c(g,\zeta_{\ell^n}^{i}).
\]

The terms with i=ell j give the exact identity

\[
S_n=U_n+\ell^{m-1}S_{n-1}.
\]

The limit of S_n is Anderson's beta_m. Modulo ell^n, U_n is the Kummer character of the product defining the manuscript's epsilon_n^(m); its limit is kappa_m. Therefore

\[
\kappa_m=(1-\ell^{m-1})\beta_m.
\]

Substitution into Anderson (13.7.3) gives the coefficient kappa_m/((1−ell^(m−1))m!) in D.8. The argument identifies characters rather than comparing a few polynomial coefficients.

For a general g, the comparison of series still retains the two cyclotomic factors S_g(u)S_g(v) and the basis ratio

\[
Q((1+u)^{\chi(g)}-1,(1+v)^{\chi(g)}-1)/Q(u,v)
\]

from Proposition13.3.2. On the cyclotomic kernel these factors are one. The inversion of the map on printed p.125 is explicitly corrected in Ihara II's Supplement, p.12; the same supplement states the inverse relation of the deck-action convention on Anderson p.85 to Ihara1986. Neither correction is omitted from the source comparison.

## Ihara 1986: original full text not obtained

The official article record, https://annals.math.princeton.edu/1986/123-1/p03 , confirms the article and pp.43–106 but supplied no full-text link. The author's official bibliography, https://www.kurims.kyoto-u.ac.jp/en/emeritus/ihara/papers.html , lists it as item25 without a file link. Crossref routes the DOI to JSTOR. OpenAlex and Semantic Scholar both returned no open full-text location.

The AMS Digital Mathematics Registry was opened at https://mathscinet.ams.org/dmr/JournalListA.html . Its Annals entries direct the historical run to JSTOR and list the Princeton and EMIS runs starting in2003 and1998, respectively. The Bielefeld digitization registry agrees on the historical repository; no official GDZ volume123 source was located. These catalogue results are evidence about the routes checked, not a proof that no open copy exists anywhere.

The original IharaII correction was obtained and read independently. It verifies its own correction statements, not an inspection of the unavailable1986 pages.

## Coleman 1989: original full text not obtained

The Mathematical Society of Japan's volume list and Crossref identify the official chapter at DOI10.2969/aspm/01710055. OpenAlex and Semantic Scholar both point to the Project Euclid chapter PDF. That provider's access challenge was not bypassed.

The current Berkeley author page failed, and the archived author preprint list was opened. The public Wayback CDX inventory of the author's site yielded no corresponding named research file. The Kyoto repository match was inspected and resolved to the unrelated one-page1986 item *Ramified Torsion Points on Curves*; it is not recorded as the requested paper.

Internet Archive's public catalogue identifies the full ASPM17 volume as `algebraicnumbert0000unse_g7s7`. Its public metadata explicitly marks the item access-restricted and the PDF/OCR private. Those files were not requested. This path therefore did not supply the original chapter either.

The access outcomes and machine-readable source URLs are retained in `a_original_source_access.json`. Anderson is now an original-source check; Ihara1986 and Coleman1989 remain explicitly unread originals.
