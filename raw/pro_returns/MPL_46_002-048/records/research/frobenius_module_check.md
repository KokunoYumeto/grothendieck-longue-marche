# Proof check: Frobenius-periodic finite modules

**Verdict:** Both observations (A) and (B) are correct. The essential boundary is **finite presentation versus finite generation over an arbitrary base**, with the Frobenius **linearization** required to be an isomorphism.

## A. Finite presentation forces finite local freeness

Let \(R\) be a commutative \(\mathbb F_p\)-algebra, let \(M\) be finitely presented, and suppose
\[
F_R^*M:=M\otimes_{R,F_R}R\simeq M.
\]
For every \(i\), put \(I_i=\operatorname{Fitt}_i^R(M)\). Fitting ideals commute with arbitrary base change, so the given isomorphism gives
\[
I_i=I_i^{[p]},\qquad
I^{[p]}:=(a^p\mid a\in I).
\]
Each \(I_i\) is finitely generated because \(M\) is finitely presented.

Localize at any prime \(\mathfrak p\), writing \(A=R_{\mathfrak p}\) and \(\mathfrak m=\mathfrak pA\). The displayed identity persists under localization. If \(J=I_iA\) is proper, then \(J\subseteq\mathfrak m\), and
\[
J=J^{[p]}\subseteq\mathfrak mJ\subseteq J,
\]
since \(a^p=a^{p-1}a\) and \(a^{p-1}\in\mathfrak m\) for \(a\in J\). Nakayama's lemma applied to the finitely generated \(A\)-module \(J\) gives \(J=0\). Thus every localized Fitting ideal is either \(0\) or \(A\).

Choose the least \(r\ge0\) with \(I_rA=A\); it exists because \(M\) is finite, and \(\operatorname{Fitt}_{-1}=0\) handles \(r=0\). Then \(I_{r-1}A=0\) and \(I_rA=A\), so the Fitting criterion makes \(M_{\mathfrak p}\) free of rank \(r\). Finite generation of the relevant ideals lets both identities hold on a neighbourhood of \(\mathfrak p\), where the same criterion gives finite local freeness. Hence \(M\) is finite locally free.

No Noetherian, reducedness, perfection or Frobenius-flatness assumption is needed. Equivalently, the stable finitely generated ideals are idempotent: \(I=I^{[p]}\subseteq I^2\subseteq I\).

## B. A cyclic counterexample without finite presentation

Inside \(\mathbb F_p(t^{1/p^\infty})\), set
\[
R=\bigcup_{n\ge0}\mathbb F_p[t^{1/p^n}],\quad
I=(t^{1/p^n}:n\ge0),\quad M=R/I.
\]
The ring \(R\) is a domain and is perfect. Evaluation of every \(t^{1/p^n}\) at zero identifies \(R/I\) with \(\mathbb F_p\), so \(M\) is nonzero and cyclic.

Every generator of \(I\) is the \(p\)-th power of the next generator; hence \(I=I^{[p]}\), and
\[
F_R^*M\simeq R/I^{[p]}=R/I=M.
\]
This supplies precisely the nondegenerate \(p\)-structure required in scan 008. Nevertheless \(tM=0\), while \(t\ne0\) in the domain \(R\). At the maximal ideal \(I\), the nonzero module \(M_I=\mathbb F_p\) is therefore not free over the domain \(R_I\); consequently \(M\) is not locally free.

There is no conflict with (A): \(I\) is the strictly increasing union
\[
(t)\subsetneq(t^{1/p})\subsetneq(t^{1/p^2})\subsetneq\cdots .
\]
Strictness follows from the \(t\)-valuation, and any finite set of elements of \(I\) lies in one term. Thus \(I\) is not finitely generated and the cyclic module \(R/I\) is not finitely presented. Here \(\operatorname{Fitt}_0(M)=I\), displaying exactly why the finite-generation step in Nakayama fails.

## Relation to the manuscript and limits

Cote 46 scan 008 defines a nondegenerate \(p\)-structure as an isomorphism \(E^{(p)}\to E\); scan 009 asks whether “les hypothèses de locale liberté et de type fini” are necessary. Observation (A) permits replacement of finite local freeness by local finite presentation, and on a locally Noetherian base finite type already suffices. Observation (B) shows that retaining only finite type does **not** force local freeness on arbitrary bases, even perfect ones.

These observations concern removal of the **local-freeness** hypothesis while retaining a finiteness condition. They do not settle every possible version of removing the **finite-type** hypothesis, and should not be presented as doing so. For the fixed GL(n) classification, retain rank n, or separate the resulting open-and-closed rank strata. The classification retains a chosen Frobenius isomorphism as data; the abstract existence of one suffices only for the freeness conclusion in (A).

## Contextual method link and sources

The supplied context transcription, cote 16 scan 052, §2 n°1, introduces “Idéaux de \(\unsure{Filting|Fitting}\) d'un module”; n°2 records their change-of-ring use for the Kähler different. The corresponding first-pass notes are 16:52:1, 16:52:4 and R14. This supplies a concrete **methodological link** to (A), not evidence that the Frobenius argument itself is written in that earlier sheet.

The Stacks Project Authors. (2026). *Frobenius action*, Lemma 51.17.1, [Tag 0EBU](https://stacks.math.columbia.edu/tag/0EBU); and *Fitting ideals*, Lemma 15.8.4(3)–(4) and Lemma 15.8.8, [Tag 07Z6](https://stacks.math.columbia.edu/tag/07Z6). The first cited lemma states the Noetherian local finite-module case; the arbitrary-ring finite-presentation argument above is an editorial deduction from the cited Fitting properties, not a stronger statement attributed verbatim to that lemma.

**Confidence:** high for both conclusions, by the explicit ideal argument and explicit domain counterexample. No transcription file was changed.

