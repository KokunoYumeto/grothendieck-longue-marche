# Scan 007: focused mathematical audit

**Auditor:** `/root/scan007_math_check`; model inherited/not exposed; effort inherited/not exposed.  
**Input reading:** 2026-11-20 12:14:19 UTC.  
**Proof checks completed:** 2026-11-20 12:15:07 UTC.

The content inputs were `reader_inputs/scan007/C.tex`, `reader_inputs/scan007/H.tex`, and `SP48_CW_104/records/scan007/math_checks.json`. This is a separately reasoned audit of those proposed arguments, not a blind audit. No image, crop, PDF, OCR, web source, other page, independent-reader return, or additional agent was used. No transcription or ink decision is made.

## Result

The requested arguments pass. No correction to the existing proofs is required. The counterexample refutes only uniqueness among **all abstract poset isomorphisms**; it does not refute the canonical transport statement or establish that the author intended the stronger reading of “à isom unique près”.

## Actual check events

All events below were completed at **2026-11-20 12:15:07 UTC**. Their individual records, including the inherited/not-exposed model and effort fields, are in `math_audit.json`.

### 007-INJECTIVE — independent re-proof

Use the usual definition of subobjects as monomorphisms modulo isomorphism of domains. Hypothesis (i) ensures that every arrow \(u:D'\to D\) represents a subobject. Equality of the subobjects represented by \(u\) and \(v\) supplies an isomorphism \(a:D'\to D'\) with \(u=v\circ a\). By (ii), \(a=1_{D'}\); hence \(u=v\).

The image description also follows: a subobject represented by \(m:X\to D\), with \(X\cong D'\), is represented by \(m\circ b\) for an isomorphism \(b:D'\to X\). The injectivity step only needs trivial automorphism groups; (ii) is sufficient.

### 007-CLASS-ORDER — independent re-proof

Define \([A]\le[B]\) by the existence of an arrow \(A\to B\). Composing with isomorphisms makes this independent of representatives. Identities and composition provide reflexivity and transitivity. If \(f:A\to B\) and \(g:B\to A\) exist, (ii) gives

\[
g\circ f=1_A,\qquad f\circ g=1_B.
\]

Thus \(f\) and \(g\) are inverse isomorphisms, giving \([A]=[B]\). This proves antisymmetry and uses no monicity assumption.

### 007-CANONICAL-TRANSPORT — independent re-proof

If \(a,b:A\to B\) are isomorphisms, then \(b^{-1}\circ a\) is an endomorphism of \(A\), so (ii) gives \(a=b\). Existence of this isomorphism comes from membership in the same isomorphism class.

For the unique isomorphism \(a\), define

\[
T_a([m:X\to A])=[a\circ m:X\to B].
\]

Composition with an isomorphism preserves monicity, equivalence of representatives, and the factorization order. The map \(T_{a^{-1}}\) is its inverse. Moreover \(T_1=1\) and \(T_{b\circ a}=T_b\circ T_a\), giving coherent transport as representatives change. This supplies a distinguished induced order isomorphism; it does not assert uniqueness among arbitrary order isomorphisms.

### 007-SUBOBJECT-ALL-ISOS — targeted counterexample verification

Take precisely the objects \(A,B\), their identities, two distinct arrows \(f,g:A\to B\), and no arrows \(B\to A\). Only identity compositions occur, so the category axioms hold. Its endomorphisms are exactly its identities. Both \(f\) and \(g\) are monic because every \(\operatorname{Hom}(X,A)\) has at most one member; the identities are also monic.

The only subobjects of \(B\) are \([f],[g],[1_B]\). They are distinct: the only automorphism of \(A\) is its identity, and \(A\) is not isomorphic to \(B\). The first two lie below \([1_B]\), but a relation \([f]\le[g]\) would require \(f=g\circ h\) for an endomorphism \(h\) of \(A\), forcing \(f=g\). The reverse relation fails likewise.

Consequently the permutation exchanging \([f]\) and \([g]\) and fixing the greatest element is a nonidentity poset automorphism. The canonical transport from \(1_B\) is the identity. Thus the stronger uniqueness interpretation is false while the canonical interpretation remains valid.

## Scope qualifications

These conclusions use the supplied endomorphism hypothesis and the usual subobject and reachability definitions. They do not choose a textual reading or settle authorial intention.

The arguments operate at the text's stated size level. Hypotheses (i) and (ii) alone do not establish that all object isomorphism classes or all subobjects form sets; literal set assertions require a suitable size convention or a separate smallness/well-poweredness assumption. This is a qualification of the ambient setup, not a defect in the four local arguments.
