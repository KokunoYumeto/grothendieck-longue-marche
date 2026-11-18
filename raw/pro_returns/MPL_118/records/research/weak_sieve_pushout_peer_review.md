# MPL118-C12 — Applying the existing XII weak-sieve counterexample to scan 023

**Check by:** GPT-6 Astra Pro, research subagent `/root/residue_new_mapping`; inherited effort is not exposed. This is a targeted application check of an existing example, not a new counterexample or a full re-audit of its supplied homotopy calculation. No image was read and no frozen text was changed.

## The two assertions must remain separate

In an ordinary pushout with top arrow \(i:Y\hookrightarrow X\), left arrow \(g:Y\to Y'\), bottom arrow \(i':Y'\to X'\), and right arrow \(f:X\to X'\), scan 023 discusses both

\[
 i\in W_\infty\Longrightarrow i'\in W_\infty,
 \qquad
 g\in W_\infty\Longrightarrow f\in W_\infty.
\]

Its displayed double-cone construction visibly addresses the second implication. The separate margin “Si \(i\in\underline W\), a-t-on pourtant \(i'\in\underline W\) ? … Non” is an assertion, not by itself an additional exhibited counterexample. Nevertheless, the first implication is also false, even when \(i\) is a full sieve and a weak equivalence; the supplied later XII appendix has an example that applies exactly.

## Existing example and the property checked here

Use the example in `context/companion/chunks/DER_XIIapp.tex`, manuscript pp. 14–15 and comment p15, **“The pushout is a three-sphere”** (dgrb657). Its top inclusion is

\[
 V=(0\to a,\;0\to b)
 \quad\hookrightarrow\quad
 \overline V=V^{\triangleright_t}.
\]

Here \(\overline V\) is the four-object commutative square \(0<a,b<t\). The **specific application check** is immediate but essential: \(V\) is full, and no arrow from its complement \(\{t\}\) enters \(V\); hence the inclusion is a sieve (the source’s “immersion ouverte”). Moreover, \(V\) has initial object \(0\), and \(\overline V\) has terminal object \(t\). Their nerves are contractible, so this attaching inclusion itself belongs to \(W_\infty\).

The other leg is the existing \(p:V\to V'\) of the appendix. The supplied calculation identifies \(V'\) as contractible and the pushout

\[
 Q=\overline V\amalg_VV'
\]

as having classifying space \(S^3\). Thus the bottom map \(i':V'\to Q\) is not a weak homotopy equivalence. This is precisely a counterexample to **preservation of the attaching weak sieve itself**, not merely to preservation of an unrelated weak map pushed along a sieve. The existing example actually defeats both displayed implications. Taking opposite categories preserves the pushout and the homotopy types and turns the sieve into a cosieve, giving the closed-immersion case as well.

The entire sphere calculation is **credited to the supplied companion and carried as background**, not claimed as newly derived here. Its direct nerve calculation also avoids the faulty converse-excision argument in the historical source. All relevant categories still have trivial fundamental groupoid, so this example is consistent with C07’s positive conclusion for 1-equivalences.

## Public primary confirmation and the historical error

The edited primary text confirms the example and its intended conclusion:

- **Grothendieck, Les Dérivateurs, XII §V.2, Proposition 11, manuscript p. 107** (section-5 PDF, printed p. 74): it explicitly asserts \(i,p\in W_\infty\) and \(i',q\notin W_\infty\).
- **XII appendix, manuscript pp. 14–15**, printed pp. 10–11: it explicitly calls \(V\hookrightarrow\overline V\) an open immersion, states the two input weak equivalences and two output failures, and gives the finite presentation.

Both texts were opened through the editor’s [Dérivateurs source page](https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html). The checked PDF filenames are `Der-ChXIIb-012.pdf` and `Der-ChXIIapp-19-06-03.pdf` in that page’s `ps/` directory.

The appendix’s printed claim \(\pi_1(V'_0)\cong\mathbb Z\) is erroneous. The supplied companion corrects this to \(BV'_0\simeq S^2\) and \(BQ\simeq S^3\), and warns that the stated extension to every \(W\subseteq W_1\) does not follow. This review confirms applicability for **ordinary weak homotopy equivalences**; it neither imports that broader claim nor relies on the erroneous fundamental-group sentence.

## Supplied-state cross-reference and review scope

`context/notes/RESULTS_STATE.md`, line 397, **POLES H.5**, status **Proved (the return’s claim)**, records the related general boundary for all sieves/object-injective maps to be cofibrations, with references to **TOTASPH F.25, F.28–F.30**. The selected state excerpt is truncated and does not give this finite example or its proof. The specific accessible source is the companion paragraph above, also paralleled in `DER_XIIb-a.tex`, comment p107, **“Two cones and the two failures of pushout invariance”** (dgrb534).

The source policy in `context/README.md` says the companion is AI-written and reviewed only in part; these paragraphs do not identify an item-specific full-effort review. Accordingly, this event records the checked **sieve/weak-equivalence identification and application**, with the existing pushout homotopy computation carried as explicitly attributed background. No prior-run status is upgraded.

Recorded 2026-11-18T03:15:42+00:00.
