# Notes while reading

These notes describe only the supplied pages. A description of what a page claims is not a proof check. Actual mathematical checks are separately recorded in CHECK_EVENTS.tsv.

## Scan 053

Continues a discussion of small-prime congruences. Defines t(n) from c(5^alpha n), gives the two congruences (7.1), and contrasts Ramanujan-type divisibility with multiplicative structure. The assertion for q=11 retains “the same reservations as for q=19”; the historical example is explicitly “to suppose what is in fact false”. Section 8, “Notes on computation”, begins a discussion of running time. The handwritten page number is 13; the archive number is 52. The covered running head is not completed from neighbouring pages.

Mathematical reading decision: the final O(N) is an asymptotic abbreviation because the preceding words define it as time approximately proportional to N; the round typed glyph alone would also admit 0. No congruence proof was checked here. The source’s snese and Foruier remain under their transposition marks; the added n, comma, i and x^n are retained at their indicated positions.

## Scan 054

Typescript page 14 discusses running times for sparse Euler/theta-series multiplication and general series multiplication, then the memory limit of Atlas. The source spells “millenium”. Its qualifications include “in practice”, “about” and “slightly slower”. No proof is offered on this page for the complexity claims.

The first handwritten estimate has short strokes before both log forms; the intended O(N log log N) is plausible, but the strokes remain in the diplomatic text. The cropped sum bound is retained as p<N. The footnote’s repeated looped sign is read as vartheta, and its rule accounts for the apparent dash in bn. The overflow restriction visibly has m=(N/6)^(1/2), though the sentence seems to require a product; the clear equals sign is kept.

A limited arithmetic check of the stated timing supports the corrected leading quarter: at 40,000 terms, N=40 and (1/4)40^(3/2)=63.245553 seconds, compatible with “about a minute”. This checks the internal example, not the program or the asymptotic claims. The inserted “from my Fortran version” and “and had to be avoided at all costs” stay at their keys.

## Scan 055

Typescript page 15 closes the discussion of computation. It records a practical limit N=43000, describes IJMODK and Dr. Don Russell’s implementation, asks for easier extraction of integer remainders, and says that programs run in 1964 exposed a low-probability timing fault. “timing” is inserted above the line. The word “hope” concerns computer design; there is no mathematical proof marked as unverified here. The manuscript provides no implementation from which the routine or hardware claims could be checked. The ambiguous second argument is not inferred from programming practice. The overwritten afft/e cell is read as t corrected to e, with the sequence of impressions less certain than their identity.

## Scan 057

Opening of CONGRUENCE HECKE OPERATORS, by A.O.L.ATKIN; section 1, Introduction. No source page numeral is visible; archive number 56. The author explicitly says “We give no proofs in this paper”, distinguishes proof from “conjecture(with overwhelming evidence)”, and proposes an analogy with a Gothic-p-adic Hecke theory. Three familiar partition congruences and p(206839n+2623) congruent 0 modulo 17 are given; their digits are read directly, not reconstructed. These statements were transcribed, not proved. The margin instruction “German ‘pee’” decides the Gothic alphabet, and “Cap. gamma” confirms Gamma. The overtyped indespensably is kept as written.

## Scan 058

Section 2, “The full modular group”, on atkin page 2. Defines Gamma, x=e^(2 pi iz), dimension k with exponent -k, and (M1), (M2), (M3a–c). Names C, C^+, C^0 and a Fourier series with finite lower index N. The author says (M1) and (M2) “seem insufficient” and ends “The author does not know of any number theory associated with modular forms which have poles inside H.”

A local check from the stated definitions confirms cuspform implies regular implies entire: zero at B removes poles there, and restriction from D to I preserves regularity. This supports the order of C^0, C^+, C. No dimension theorem or Eisenstein decomposition was proved. The unusual cusp-,forms and FS dash remain; three dots after the cusp expression are not normalised to a colon.

## Scan 059

Atkin page 3, clipped at the upper edge. Defines T_p in the z and Fourier variables, lists (H1)–(H4), gives the Petersson product, and states Theorem 1 (Hecke-Petersson) and relation (1). A marginal replacement changes the struck “group” to an uncertain first word followed by underlined “semi group!”. The note “*footnote on cover page” is transcribed at its key; the absent footnote is not reconstructed.

The displayed coefficient formula gives eigenvalue a(p) when a(1)=1, since a(1/p)=0; moving a(n)a(p) to the left yields exactly the plus sign on the last term of (1). A separate local linear-algebra check confirms the last criterion: if one commuting operator has distinct eigenvalues over C, each of its one-dimensional eigenspaces is preserved by all the others, giving a common eigenbasis. These checks do not prove modular invariance, convergence of the inner product or (H1)–(H4). The faint for and has distinct are supported by surviving letters, not supplied solely by this argument.

## Scan 060

The typescript is headed “atkin page 4” (archive number 59). It contrasts the finite-dimensional cusp-form theory with spaces containing poles, introduces the displayed j-function expansion, and asks for an analogue of the coefficient recurrence in finite rings. It states results for q=2,3,5,7,13 and all alpha, with only finitely many parameters otherwise; the theorem continues on scan 61. The author says “nothing identical is possible” and describes the range mainly pursued as positive and zero dimension.

The constant 744 in the j expansion is consistent with its displayed product: (1+240x+...)^3=1+720x+..., while the reciprocal product contributes 1+24x+..., giving 720+24=744. For a form whose leading pole is x^{-m}, the second part of T_p has pole order pm, while the first has at most m/p; iteration produces strictly growing leading pole orders and hence linearly independent iterates. This checks the pole argument under the page’s entire-form setting, not a new theorem about arbitrary interior poles.

The wording “any commutative ring with identity” leaves a qualification unstated: p^{-1} is defined only when p is a unit. For example it is undefined at p=q in Z/q^alpha Z. The later restriction p different from q must be distinguished from the unqualified wording here; no correction is inserted. The last faint parameter is retained as a|alpha rather than silently regularised. The marginal symbol name is capitalised “Sigma”; the separate name “alpha” is lowercase. No date appears.

## Scan 061

Archive number 60, no running page number or date. Conjecture 1 defines a(n)=c(q^alpha n)/c(q^alpha) for primes q<=23, p other than q, and positive alpha,n. It gives separate p- and q-recurrences. The paragraph lists the sharper Ramanujan-type divisibilities for q=2,3,5,7,11 and beta=3alpha+8,2alpha+3,alpha+1,alpha,alpha. These are transcribed as claims, not independently proved here.

The explanation of division is coherent after cancelling q-powers: assuming q^beta divides every numerator and exactly divides the denominator, write numerator=q^beta v and denominator=q^beta u with u prime to q. The quotient is v u^{-1} modulo any q^theta. This does not mean that the zero or nonunit denominator can simply be inverted before cancellation. The explicit p other than q restriction supplies the unit condition missing in the broad wording of scan 60.

Conjecture 2 treats q=29 or 31 by lambda a(n)+bar(lambda) bar(a(n)) in a quadratic extension E and uses = in E. The short bar over the second lambda has been checked against both its physical position and the explicit conjugates line; it is not absorbed into the long underline above. For q>=37, the author says “appears to be” and “this is somewhat speculative” about a congruence-space dimension given by the integral part of q/12. No proof of either conjecture is claimed. The final paragraph moves to Gamma_0(q); the faint arrow agrees with the map notation on scan 58. Source sp ecial and the insertion into Hwever are preserved.

## Scan 062

Archive number 61. This begins by completing the sentence from scan 61, then gives section 3, “The subgroup Gamma_0(q) for q prime.” It replaces T_q by U_q, describes the two cusps, discards the old cuspforms G(z),G(qz), and formulates (H1q)–(H4q) and Theorem 2 for newforms. The text expressly says U_q is not hermitian and that “a little extra work” is needed to deal with it; no inference that the four listed properties alone prove simultaneous diagonalisation is made here.

The averaging formula for U_q is checked termwise: summing exp(2 pi i m lambda/q) over lambda=0,...,q-1 kills m not divisible by q and multiplies the surviving terms by q. Multiplication by q^-1 leaves sum a(nq)x^n. For a normalized eigenform the coefficient of x is the U_q eigenvalue a(q), and coefficient comparison gives a(nq)=a(n)a(q), as displayed. The p relation has exponent -k-1 and p different from q.

The final value a(q)=plus-or-minus q^(-k/2-1) and the announcement of a paper with Joseph Lehner are retained as statements, without proof or external lookup. The cancelled heading Theorem is recoverable. The erased character after typica looks rounded rather than like a straight l; its first doubtful reading is changed to o while l remains possible. The final insertion is an extension, replacing a partly unreadable a form. No date is given.

## Scan 063

Running head “atkin page 7”, archive number 62; no date. Conjecture 3 gives a compatible family F_alpha on Gamma_0(q), q<=23, with congruence multiplicativity, compatibility modulo q^alpha, and an eventual U_q statement for arbitrary integral Fourier series. The insertion “for all alpha>=1” belongs after “we have” in (iv). The inserted constant k+ in its formula is matched by “k and”, are, and the plural s below. The displayed right side ends F_alpha(z), although F(x) is on the left; this source notation is preserved.

The first Fourier display visibly has a separate x followed by a sum starting at n=1. Its coefficient of x is therefore 1+a_alpha(1). This may be an indexing or normalisation slip when compared with the earlier normalized eigenform formulas, but neither n=2 nor a new condition on a_alpha(1) is supplied. The original n=1 is clear.

Condition (iii) does support a coefficientwise q-adic limit: for each n, the successive differences are divisible by q^alpha, so the sequence is Cauchy in the q-adic integers. This checks only the compatibility-to-limit step, not the existence, uniqueness or modular nature of that limit. The author’s own reservations are explicit: “It seems possible” that F_alpha is unique, “can see no approach to prove this”, “One may hope for some deeper method of proof”, and “it seems likely” concerning integral Fourier series on congruence subgroups. These qualifications remain in the transcription. The deleted character before true is a recoverable t; the overwritten is and p|i remain doubtful.

## Scan 064

Running head “atkin page 8”, archive number 63. The conclusion identifies two proof obstacles: obtaining a finite-dimensional congruence space for all alpha (the available method is stated only for genus zero), and simultaneous diagonalisation when q>=29. It proposes the simple-spectrum condition (H3q*) by analogy with (H3*) in section 2. Its phrase “Our proofs(where available)” and the restriction to “a few fixed values of alpha” for remaining q are preserved.

The narrow elementary point about distinctness is valid conditionally: two lifted eigenvalues whose reductions modulo q differ cannot coincide modulo q^alpha. This checks persistence of distinctness only, not existence of lifts, diagonalisation over the relevant ring, or the claims about genus.

Nine references are present, followed by a very faint institutional address. Dates read in the references are 1967 (items 1–3, with a 1966 conference in item 2), 1962 (4), 1949 (5–6), 1965 (7), 1964 (8), and 1954 (9). Clear page spans are 14-32, 442-459, the inserted 136-148, 373-386, and 305-308. These are readings from the sheet, not verified bibliographic metadata. The old range under 136-148 is physically covered. The start of the address remains The Atlas Computer with doubt marks; Chilton and the terminal colon are readable. No external reference or institutional address was consulted.

## Scan 078

AVANT-PROPOS, page - 1 -, I. This typescript states the programme of Weil cohomology through étale topology, torsion prime to residual characteristics, and passage to l-adic coefficients. It lists spectral sequences, finiteness, Künneth, duality and Lefschetz, and announces comparison over C. The inserted references are SGA 1964/65 and SGA 1965; they are references on the sheet, not a separately supplied date. The page ends mid-sentence. The footnote expressly says « il n’est pas prouvé » that Frobenius eigenvalues are algebraic integers, « ni à fortiori » that their absolute values equal q^(i/2); no later result is imported. Source forms « dûs », « A partir », singular « coefficient » and the visible dots remain. The repeated l-adic notation decides the l/1 ambiguity; the repeated limiting index decides nu/v. The long diagonal is reproduced continuously; its intended cancellation scope remains uncertain, and the text beneath it is fully transcribed. No theorem asserted here has been proved in this reading.

## Scan 080

X-1, first leaf of the titled « Liste des courbes elliptiques à multiplication complexe dont l’invariant modulaire j est rationnel ». It lists imaginary quadratic fields, allowable conductors for class-number-one orders, and the use of Weber’s functions to compute j. Two entries are given: 1.1. has j(i)=2^6 3^3 and automorphism order 4; 1.2 has j(2i)=(2.3.11)^3. The displayed products evaluate to 1728 and 287496; this arithmetic does not verify the CM identities. The stated conductor lists contain 13 known (d,f) pairs, with an extra hypothetical d_? retained. The source explicitly says « plus peut-être une autre valeur d_? » and « (s’il existe) »; no later classification is substituted. The reader’s note « les d sont premiers ! » is false if applied to every displayed d, because 1 occurs. The note is preserved unchanged. The overbrace covers the first five d values; its quoted label remains doubtful only at its final s. H’s only independently set source text here is the marginal NB note; its surrounding notes are editorial descriptions and are not collated as omitted typescript. No date appears on this leaf.

## Scan 081

X-2 continues X-1 with eleven known entries and one hypothetical d_?.1 row whose value is explicitly j=?. The body consists of a table with Weber references and a closing ***. The abbreviation « autom.d’ordre » remains as typed. The four ditto quotes refer visually to the reference column. The d value in 3.3 is overtyped; both old and new layers retain 3/6 doubt. Row 11.1 has two adjacent digits in -11 but a radical roof that stops over the first; the short roof is reproduced. No date appears. Direct evaluation of the eleven written right-hand sides, in order 2.1 through 163.1, gives 8000, 0, 54000, -12288000, -3375, 16581375, -32768, -884736, -884736000, -147197952000, -262537412640768000. This is arithmetic only and does not prove any listed complex-multiplication value or completeness claim. Together with X-1 the written known cases number 13. Source punctuation, including the ambiguous separator in 7.2 and detached mark after the 43.1 arrow, is not regularised.

## Scan 083

B-1, titled COURBES ELLIPTIQUES : BIBLIOGRAPHIE, has three numbered sections: elliptic/modular functions; complex multiplication by analytic methods; and algebraic function fields of one variable. It contains ten bibliographical entries. Dates printed on this leaf are 1964 (4ème édition), 1922, 1908, 1924, 1927, 1927 and 1931 for Hasse’s two parts, 1957-1958, 1958, 1951 and 1963. The Hasse ranges are p.115-139 in volume 157 and p.64-88 in volume 165; these are transcribed ranges, not independently verified publication data. The damaged Fueter title reads Multiplik.tion at the visible surface; its normal spelling is not supplied in the transcription. The original overtyped letter in Gauthier remains doubtful. No mathematical assertion is argued or checked on this bibliography leaf, and no external catalogue was consulted.

## Scan 084

B-2 continues the bibliography with sections 4–7: algebraic curves; algebraic theory of elliptic curves; modular schemes; and abelian varieties/abelian schemes. Twelve references are listed. The dated entries read 1948, 1959, 1936, 1949, three times 1959 for Igusa, then 1948, 1959, 1957-62 for the Bourbaki extracts, 1964 and 1965. The source gives Deuring p.32-47; Igusa p.453-476, p.436-452 and p.561-577; Grothendieck exp.232 et 236; Neron n°21; and Lang n°7. These are source bibliographical statements, not catalogue verification. Three pencil ticks point to the two Weil entries and Lang. The heading « théorie algebrique » in section 6 lacks the accent found in section 5 and is left so. A faint possible acute in the section 7 Weil title is now preferred but remains doubtful. No mathematical proof or external bibliographic check was performed.

## Scan 085

B-3 concludes the bibliography with sections 8–10: algebraic complex multiplication; other arithmetic questions on elliptic curves; and « Multiplication complexe "formelle" ». Ten references are listed. Source dates/ranges: Deuring 1949, p.32-47; Shimura and TAN1YAMA n°6, 1961; Weil 1955, p.9-22; Deuring I–IV with 1953, 1955, 1956, 1957; Lang n°11, 1962; Cassels 1962, p.234-246; Serre 1964; Tate 1961; and the two final entries 1965. The page ends with ***. No publication data were checked externally. The digit-like 1 in TAN1YAMA is retained as typed; no missing A is supplied. The l in l-adiques is settled by the same slashed-letter notation already seen on scan 78. The overwritten heading number retains doubt, and the raised v in curves is kept with the colon-shaped older ink. There is no mathematical argument on this list to check.

## Scan 087

T-1 opens COURBES ELLIPTIQUES - FORMULAIRE, subtitled « Traduction libre d’un manuscrit inédit de TATE ». No translator or date is supplied. Section 1 chooses a Weierstrass equation from an elliptic curve, origin O and nonzero differential pi, with local x=t^-2+... and y=-t^-3+.... The word forms « telles que », « morphique ailleurs » and « Homogénéite » are retained. The named point resolves the O/0 notation; the surviving foot and the same local parameter in dt and y decide t rather than a plus in the x expansion. Every monomial of (*) has total weight 6 under weights y=3, x=2, a_i=i. The four b-invariant lines are mutually consistent: expanding the two alternative b8 expressions and the -4b8 identity gives zero residuals. These are polynomial checks; the geometric existence assertion has not been reproved. The faint fork below the subtitle is reproduced as a drawing without assigning it a word.

## Scan 088

T-2 defines c4, c6, Delta and j, and writes the differential through F_x and F_y. Polynomial expansion verifies both Delta expressions and c4^3-c6^2=1728Delta using T-1’s b definitions. Direct differentiation verifies the displayed partial derivatives. On the overlap where the fractions are defined, dF=F_x dx+F_y dy=0 gives dx/F_y=-dy/F_x; the final denominator is -F_x, so the plus sign before the dy fraction is correct. The classical g2/g3 normalization is stated by the page, not independently proved here. The annotations give the intended integer factorizations 12=2^2*3, 216=2^3*3^3, 1728=2^6*3^3, but a separate upright beside the first exponent is now preserved as a doubtful prime-like tick. The last j ratio needs its denominators invertible, beyond Delta invertible alone. For a1=a2=a3=a6=0 and a4=-1 over Q, Delta=64, c4=48, c6=0 and j=1728; that ratio is undefined. This domain qualification belongs only in the notes. No date is supplied and no authorial verification request appears.

