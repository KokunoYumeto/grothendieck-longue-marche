# Final algebra review of the assembled notes

**Scope:** A01–A24 and S01–S03, S06–S07 in `MPL_60_036-070_notes.md`; frozen TeX witnesses only. No scan images were consulted and no frozen or main-note file was edited. Line numbers below refer to the assembled notes as reviewed.

The substantive algebraic examples, characteristic claims, Tor/Ext signs and cited Stacks locators pass this review. The following concrete fixes remain; the two scope qualifications concern the notes' own formulations, not corrections to the transcription.

## 1. Restore lost math delimiters

- **S02, lines411–412:** replace the formula-bearing plain parentheses with `\(...\)`: `\(A=k[X,Y]\)`, `\(x=(X,Y)\in A^2\)`, `\(A^2/Ax\cong(X,Y)\)`, `\(Ax\)`, `\(a,b\in A\)`, `\(aX+bY=1\)`, and `\((a,b)\mapsto -Ya+Xb\)`. The mathematical example and map are correct. The quotation “facteur direct” is present in frozen050, line10, so it needs no quotation correction.
- **S03, lines418–419:** restore `\(L_1\)`, `\(n-1\)`, `\(M\cong A^{n-1}\oplus I\)` and `\(I\)`.
- **Bibliography, line580:** render the Serre condition as `\((S_2)\)`.
- **Bibliography, line583:** replace `(operatorname{Fitt}_0\Omega)` with `\(\operatorname{Fitt}_0(\Omega_{B/A})\)`. Both the opening backslash of `\operatorname` and the math delimiters have been lost. Tag0BVW and Definition49.7.1 are the correct citation.

## 2. State the nonempty-family qualification in A07

**Location:** A07, line234; witness frozen068, line5. Start the deduction “For a nonempty family, inside the dual vector space, …”. A nonempty family guarantees that the sum of dual lattices spans the full dual vector space, which is needed to identify its module dual with the intersection inside the original vector space. Under the usual empty-intersection convention, the empty family's intersection is the entire fraction-field vector space, generally not a finite lattice; for example, it is \(k(X)\) when \(A=k[X]\) and \(V=k(X)\). This is an endpoint qualification to the editorial proof, with no claim about the underlying source's family convention. **Confidence: high.**

## 3. State positive rank for the Steinitz formula in S03

**Location:** S03, lines418–419; witnesses frozen048, line14, and frozen046, line4. Introduce “For \(n=\operatorname{rank}M\ge1\), …” before the conclusion involving a free summand of rank \(n-1\), and retain the rank-zero case separately as \(M=0\). The formula \(M\cong A^{n-1}\oplus I\) with \(I\) a nonzero ideal has that positive-rank hypothesis; the source explicitly handles \(n\le1\) as its base case. This avoids an undefined negative free rank without changing the intended reduction argument. **Confidence: high.**
