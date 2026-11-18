# Targeted editorial audit of surgery notes S01–S34

**Reviewer:** GPT-6 Astra Pro; effort not exposed; subtask run `MPL_67_053-101/elliptic_research/surgery-editorial-audit`. **Date:** 18 November 2026 UTC. **Scope:** the supplied research texts `research/surgery/notes.md` and `research/surgery/proofs.md`, compared with the supplied `context/hua_project/67.modern.tex`, §§VI–X. No transcription, image, or surgery file was changed.

## Finding

**No substantive mathematical correction or incorrect attribution to Hua was identified in this targeted audit.** The notes consistently separate manuscript assertions, Hua's modernized interpretation, checked local arguments, and unresolved global claims. This conclusion is an editorial and targeted-proof review of the supplied material; it is not a new proof of the welding, uniformization, or moduli results cited as background.

The Hua attributions match their relevant sections: §VI supplies the circle/disc duality of S01; §VII supplies the two boundary sheaves, reflection hypotheses, cutting and welding distinctions of S02–S13; §VIII supplies shadows, admissibility, the disc exception, and the Koebe obstruction of S14–S22; §IX supplies the normalized slit maps and the unresolved interpretation of rectifiability in S23–S27; and §X supplies propagation tensors, stability, dimension counts, conditional inversion, and the later doubts in S28–S34. In particular, S20 explicitly credits Hua's §VIII obstruction rather than presenting it as a newly discovered refutation, while S33 correctly limits the fixed-coordinate plumbing observation in Hua §X.

## Mathematical scope checked

- **S03–S05:** the square-root example distinguishes the sheaves without refuting recovery of conformal charts; the real-linear reflection counterexample attacks only the isolated sentence without interior holomorphicity; and the leading-term sign argument proves the nonzero boundary derivative under the retained lemma's hypotheses.
- **S14–S16 and S20–S22:** equal shadows of arbitrary embedded discs do not refute injectivity on the admissible locus. The bound on conformal radius refutes only the unrestricted positive-radius target, conditional on the cited Koebe quarter theorem. The six-map metric average is functorial for the marked triple, but neither constant curvature nor admissibility is inferred.
- **S24–S30:** the boundary-triple uniqueness, monotone-graph length bound, conditional unstable-cut example, and stable-graph dimension identity are correct within their stated scopes. These checks do not establish an inverse welding theorem, permit arbitrary cuts in the intended category, or construct the proposed moduli spaces.
- **S31–S34:** fixed coordinate germs and a common plumbing overlap justify cutoff independence; tangent shadows alone do not provide those germs. The global inverse, geodesicity, and four-holed-sphere differential tests remain explicitly unresolved.

## Optional clarification and remaining limits

In **P-S14**, “in a fixed chart … for \(r>0\)” could be made fully local by saying **“choose \(r>0\) small enough that all displayed image discs lie in the chart”**, or by taking the ambient surface to be \(\mathbb C\). This is a harmless domain clarification to an otherwise valid existence example; no change to its conclusion is needed.

All five entries marked **own idea**—S03, S14, S21, S22, and S25—give both an explicit confidence level and its reason. The restricted confidence in S21 is appropriate: the proposed injectivity, local invertibility, and properness questions remain research directions. W1–W4 were carried as cited background after reading `research/surgery/web_sources.md`; their external sources were not reopened or independently proved in this audit. The accompanying event file records those limits and the actual local proof checks.
