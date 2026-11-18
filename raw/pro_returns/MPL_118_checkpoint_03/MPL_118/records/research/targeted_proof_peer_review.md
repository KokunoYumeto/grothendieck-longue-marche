# Independent checks of four targeted manuscript arguments

Author: GPT-6 Astra Pro, research subagent `/root/residue_new_mapping`; inherited effort is not exposed. These checks use only the frozen TeX and supplied context. No scan was examined and no transcription was changed. The arguments below check the primary agent’s proposed repairs; they make no novelty claim and do not reopen the proofs of the dossier returns.

## MPL118-C01 — Strict base change of the integral, scan 020

**Verdict: correct for the stated strict diagram.** This answers the tagged-category comparison behind “Ce diagramme est-il cartésien ? À vérifier !” in the frozen text. It does not, by itself, assert that ordinary pushouts in Cat commute with arbitrary pullback.

Let \(D:K\to\mathrm{Cat}/B\) be strict and write \(p_k:D(k)\to B\). Use the covariant Grothendieck construction: its arrows \((k,x)\to(l,y)\) are pairs \((\alpha,u)\) with \(\alpha:k\to l\) and \(u:D(\alpha)x\to y\). Its map to \(B\) sends this arrow to \(p_l(u)\). For \(v:B'\to B\), the proposed comparison sends

\[
 ((k,x),b')\longmapsto(k,(x,b')),
 \qquad ((\alpha,u),w)\longmapsto(\alpha,(u,w)).
\]

The object condition is exactly \(p_k(x)=v(b')\) on either side, and the arrow condition is exactly \(p_l(u)=v(w)\). The inverse merely removes the other parenthesization. Identities and composition agree because the pulled-back transition functor sends \((x,b')\) to \((D(\alpha)x,b')\). Thus

\[
 (\textstyle\int_K D)\times_BB'
 \;\cong\;\int_K(D\times_BB')
\]

is an isomorphism over \(B'\), not just a weak equivalence. A claim of universal membership in \(W\) still requires that the comparison for each pulled-back diagram belongs to \(W\); the categorical isomorphism supplies the correct identification, not that extra homotopical premise.

**Source and context:** `MPL_118/pages/MPL_118_118_scan020.tex`; the strict integral and base-change question as written. No RESULTS_STATE theorem is revalidated by this elementary construction.

## MPL118-C02 — The cartesian opfibration square, scan 021

**Verdict: correct; cocartesianness is unnecessary for this comparison statement.** The frozen hypothesis is “un diagramme cartésien, avec \(i',f\) des cofibrations”, with “cofibration” read here as a Grothendieck opfibration. Its point condition is “isom. à la catégorie ponctuelle”, and the separate margin says “au lieu de ponctuelle, il suffit qu’elle soit \(\underline W\)-asphérique”. The check below retains these distinctions.

Identify the cartesian square with \(Y=X\times_BY'\). Both maps \(X\to B\) and \(Y'\to B\) are opfibrations, so a lift in \(Y\) is the pair of opcartesian lifts in the factors. The two projections preserve those lifts. For the span category \(K=(0\to1,0\to2)\), put

\[
 E=\int_K(Y\to X,\;Y\to Y').
\]

An opcartesian lift in one component, regarded as an arrow with unchanged \(K\)-tag, is opcartesian in \(E\to B\). Indeed, a general arrow out of that tag consists of a transition functor followed by an arrow in its target component; preservation of opcartesian arrows by the transition functor gives the required unique factorization. Consequently \(E\to B\) is an opfibration, and its strict fibre at \(b\) is

\[
 S(A,C)=\int_K(A\times C\longrightarrow A,\;A\times C\longrightarrow C),
 \qquad A=X_b,\quad C=Y'_b.
\]

If \(A=e\), the full subcategory on the central copy of \(C\) and the \(e\)-arm is the cone \(C^{\triangleright}\). Collapse the other copy of \(C\) to the central one; this gives a retraction \(r:S(e,C)\to C^{\triangleright}\). There is a natural transformation from inclusion-after-retraction to the identity, using the central-to-arm arrow at every object of that other copy. The cone has a final object, so \(S(e,C)\) is contractible. Swapping the arms treats \(C=e\).

For the marginal weakening, suppose \(A\to e\) belongs to a **relative basic localizer** \(W\). Compare the displayed span with \(C\to e,\;C\to C\). Its component maps are \(A\times C\to C\), \(A\to e\), and \(1_C\); finite-product closure puts them in \(W\), and fibrewise invariance of the Grothendieck integral puts \(S(A,C)\to S(e,C)\) in \(W\). Hence the fibre is \(W\)-aspherical; the other arm is symmetric. The opfibration criterion then gives \(E\to B\in W\). These hypotheses and fibre descriptions persist under strict base change, so the same argument gives universal membership in \(W\).

**Scope:** the product and fibrewise-invariance facts are used with the relative localizer hypothesis. This check does not derive them from only the literal absolute Loc (3). No ordinary-pushout condition was used, and this does not turn scan 023’s unrestricted pushout assertion into a theorem.

**Source and context:** `MPL_118/pages/MPL_118_118_scan021.tex`; `context/companion/chunks/DER_XVI.tex`, §1, Loc (3 bis) and Proposition 1.3, ms. 3–8. RESULTS_STATE `POLES B.2` is a supplied prior claim about the general fibrewise-invariance mechanism, used as context without reopening its proof; the present calculation checks the specific span and its fibres.

## MPL118-C03 — Strictifying the filtration argument, scans 039–040

**Verdict: the proposed repair works, and the orientation is \(\psi f\leq\varphi\).** Compatibility \(f(X_i)\subseteq Y_i\) does not imply the strict equality \(\psi f=\varphi\) needed by the manuscript’s direct identification of the over-\(I\) map. The failure persists even when every \(f_i\) is a weak equivalence: let \(I=[1]\), \(X=[1]\), \(X_0=\{0\}\), \(X_1=[1]\), and \(Y=Y_0=Y_1=e\). The rank of \(1\in X\) is 1 while that of its image is 0.

Use the minimum-stage assumptions actually written on 039–040. The open filtrations give functors \(\varphi:X\to I\), \(\psi:Y\to I\), with

\[
 X_i=\{x:\varphi(x)\leq i\},\qquad
 Y_i=\{y:\psi(y)\leq i\}.
\]

Because \(x\in X_{\varphi(x)}\), compatibility gives \(\psi(fx)\leq\varphi(x)\), exactly in the indicated direction. Set

\[
 RX=\int_{i\in I}X_i\cong\int_{i\in I}(X/i),\qquad
 RY=\int_{i\in I}Y_i.
\]

An object of \(RX\) is \((i,x)\) with \(\varphi(x)\leq i\); an arrow to \((j,x')\) is \(i\leq j\) together with an arrow \(x\to x'\). The compatibility inequality makes

\[
 Rf(i,x)=(i,f(x))
\]

well-defined and strictly over \(I\), with fibre map \(f_i\). The forgetful map \(q_X:RX\to X\) has section \(s_X(x)=(\varphi(x),x)\). We have \(q_Xs_X=1_X\) and a natural transformation \(s_Xq_X\Rightarrow1_{RX}\) whose component at \((i,x)\) uses \(\varphi(x)\leq i\) and \(1_x\). Thus \(q_X\) is a homotopism and belongs to \(W\); likewise for \(q_Y\).

To apply **relative** Theorem A without confusing fibres and comma categories, retract \((RX)/i\) onto \(X_i\) by

\[
 ((j,x),j\leq i)\longmapsto x.
\]

The inclusion sends \(x\) to \(((i,x),1_i)\); the natural transformation now runs from the identity to inclusion-after-retraction, using \(j\leq i\). These retractions are homotopisms and commute with \((Rf)/i\) and \(f_i\). Two-out-of-three therefore gives \((Rf)/i\in W\) for each \(i\). Relative Theorem A gives \(Rf\in W\), and \(q_YRf=fq_X\) gives \(f\in W\).

**Scope:** this repairs the step under the retained minimum-stage/infimum-compatible filtration hypotheses; it does not prove the theorem for arbitrary covers or arbitrary filtered colimits. Closed filtrations require the opposite-category version. Neither repair nor added strictification belongs in the frozen transcription.

**Source and context:** `MPL_118/pages/MPL_118_118_scan039.tex` and `MPL_118/pages/MPL_118_118_scan040.tex`; `context/companion/chunks/DER_XVI.tex`, §1, relative Loc (3 bis), ms. 3–8. This is a targeted missing-step check, not a resolution of RESULTS_STATE `RESIDUE F.7` or an audit of `RESIDUE B.10`.

## MPL118-C11 — The sum claim for product stability, scan 036

**Verdict: the proposed counterexample is correct for an unrestricted relative basic localizer.** The frozen page says “La condition \((ii)\) est visiblement stable par sommes”; it says \((ii)\), not \((iv)\). Condition \((ii)\) is the finite-product stability of \(W_A\).

The class \(W_{\mathrm{ne}}\) consisting of all functors between nonempty categories and \(1_\varnothing\) is already the example in the supplied companion, `DER_XVI.tex`, comment p9 “Sums and products require different hypotheses”, behind the correction to Corollary 2.2 and dossier `RESIDUE B.11`. It is therefore credited as a supplied example, not introduced here as a discovery. Its relative-Theorem-A test is consistent with the claimed use: if a map with empty source had nonempty target, choose the image of a target object in the common base; that comma target is nonempty and its comma source empty, violating the required local test.

For \(A_1=A_2=e\), the induced class on each \(\widehat A_i=\mathrm{Set}\) tests only nonemptiness, and is closed under finite products. For \(A=e\amalg e\), presheaves are pairs of sets, and the category of elements of \((S,T)\) is the discrete set \(S\amalg T\). Thus

\[
 f:(*,\varnothing)\longrightarrow(*,*)
\]

belongs to \(W_A\). But with \(Z=(\varnothing,*)\),

\[
 f\times1_Z:(\varnothing,\varnothing)
       \longrightarrow(\varnothing,*)
\]

does not belong to \(W_A\). This is precisely a failure of the asserted sum stability of \((ii)\).

For ordinary weak homotopy equivalences \(W_\infty\), a map of categories of elements over a disjoint union is a weak equivalence exactly when every component map is; products of presheaves are also componentwise. The sum assertion is valid with that reading. For general \(W\), an appropriate decomposition/reflection hypothesis is needed; no such conclusion follows from the relative axiom alone.

**Source and context:** `MPL_118/pages/MPL_118_118_scan036.tex`; `context/companion/chunks/DER_XVI.tex`, §2, Corollary 2.2 and comment p9, ms. 9–10; `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, `RESIDUE B.11` (supplied Refuted claim). This checks a new application of that supplied example to the literal scan-036 assertion, without re-auditing the full dossier result.


Recorded 2026-11-18T03:06:52+00:00.
