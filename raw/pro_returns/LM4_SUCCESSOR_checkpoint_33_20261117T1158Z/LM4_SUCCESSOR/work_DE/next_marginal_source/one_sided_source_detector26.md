# The actual one-sided free-seven quotient and its six-source limitation

DE, 2026-11-17. Research only. The complete six-source injection question is not decided by this quotient.

## 1. A quotient of the complete two-operator presentation

Use the actual B123 ordinary fiber
\[
 F=F(a,B,d,e,f,\bar a,\bar B,\bar d,\bar e,g,x)
\]
and the source operators \(m,m^{-1},v,v^{-1}\), with actual ordinary group \(G_0=W\rtimes S\), \(S=F(m,v)\), \(W=F/N\). The subgroup N includes every retained conjugate and every signed source translate of all forty actual node seeds.

The complete peripheral-factor certificate shows that **every one of the forty nodes has one core in \(\{a,B,d,e\}\) and one in \(\{\bar a,\bar B,\bar d,\bar e\}\)**. Their full nonlinear conjugators remain present. Let Bnorm be the normal closure in F of the four barred basis generators. Killing a barred core kills the entire corresponding commutator, irrespective of its conjugator. Each of the four signed source maps takes every barred core to a conjugate of that same positive barred core. Thus Bnorm is invariant under the source group, contains every seed, and contains all its retained/source translates. Consequently
\[
 N\subseteq Bnorm,
 \qquad W\longrightarrow F_7=F(a,B,d,e,f,g,x)
\]
is an actual quotient, and it extends to
\[
 G_0\longrightarrow F_7\rtimes S.
\]
The four induced seven-generator automorphisms and both inverse compositions are literal free-word identities; the independent producer checks all twenty-eight compositions. This is a statement about the whole two-operator annular presentation, not only a simply connected regional vertex.

## 2. The exact source marking in this quotient

Let \(s_1,s_2,s_3,s_4\) be the actual contact words \(\beta_{11},\beta_{22},\beta_{33},\beta_{44}\), in that order. Filling the barred half in their complete raw B123 words gives
\[
\begin{aligned}
 s_1&=aB^{-1}a^{-1},\\
 s_2&=fde^{-1}d^{-1}f^{-1},\\
 s_3&=s_1^{-1}s_2^{-1}d^{-1}s_2s_1,\\
 s_4&=s_1^{-1}a^{-1}s_1.
\end{aligned}
\]
The fifth and sixth actual source generators remain respectively v and m, with no fiber correction in the source-adapted splitting.

The tuple \((s_1,s_2,s_3,s_4,f,g,x)\) is a literal free basis of F7. Its inverse is
\[
\begin{aligned}
 a&=s_1s_4^{-1}s_1^{-1},\\
 B&=a^{-1}s_1^{-1}a,\\
 d&=s_2s_1s_3^{-1}s_1^{-1}s_2^{-1},\\
 e&=d^{-1}f^{-1}s_2^{-1}fd,
\end{aligned}
\]
with f,g,x unchanged. These are triangular word formulas, not an abelian-rank argument. All fourteen free inverse substitutions are checked exactly.

## 3. Why this quotient does not detect a free six-source group

The actual induced m-action fixes a,d,e literally. In particular it fixes
\[
 A_s=s_1s_4^{-1}s_1^{-1}=a.
\]
Therefore the nonempty reduced word
\[
 [m,s_1s_4^{-1}s_1^{-1}]
\]
of length eight in the abstract free source group on the four contacts,v,m maps to the identity in \(F_7\rtimes S\). The sign convention for writing the semidirect action does not affect this conclusion: both signed m-actions fix a.

The second displayed inverse also supplies another source word expressing d, likewise fixed by m in this quotient. One explicit kernel word suffices to show that this proposed detector cannot prove six-source injection.

For clarity, the corresponding **actual pre-node F11 residue** \(\alpha_m(A_s)A_s^{-1}\), using the complete raw source words, has free-reduced length258. It is recorded in the certificate and becomes trivial after this one-sided filling. Being nontrivial in the generic free group does not prove that it survives the actual all-orbit node quotient. Conversely, being killed by the one-sided quotient does not prove an actual source relation. Its membership in N is left unresolved here; no quotient word oracle or finite census is used.

## 4. Comparison with earlier one-family statements

The earlier `work_CE/paired_regional_retractions_22h.txt` fills a family over a simply connected slit base and identifies the target with a single F7 fiber; its carefully retained scope explicitly excludes the full annular base. B108's corresponding geometric disk gives a free-factor detector for a specified first-neck F5. The current result instead uses the complete B123 forty-node input and all signed source operators and retains the two actual source base generators. Its target is the actual marked free-seven-by-free-two quotient, with the explicit failed six-source detector above.

The earlier `actual_filling_kernel_freeness_gate20.md` concerns a different global symmetric-surface one-family kernel and the injectivity of punctured divisor sections. It does not provide source-six injection here. None of these comparisons is replaced by a generic-fiber or normal-generation shortcut.

## 5. Reproducible certificate

Files:
- `check_one_sided_source_detector26.py/.out/.err`
- `one_sided_source_detector26.json`

The complete independent producer reads only stable JSON. It checks all40 cross-half node pairs and their filled factor words, all16 signed discarded-generator images, all28 induced free7 inverse compositions, all14 source-basis inverse substitutions, and the actual nonempty generic residue of the displayed source word. No orbit-depth iteration is needed: invariance of the entire barred normal subgroup handles every translate uniformly.
