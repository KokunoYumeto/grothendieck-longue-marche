"""Record the honest reconstructed seventh-hour contribution after recovery."""
from pathlib import Path
import csv
H=Path(__file__).resolve().parent
path=H/'B_separability_results.csv'
with path.open(newline='') as f:
    rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
assert not any(r['id'] in {'B.65','B.66'} for r in rows)
rows += [dict(zip(fields,[
 'B.65','The actual pure cyclic centralizer H5 also centralizes the dihedral group J=D5; two rigid-seven restrictions vanish and the other ten have one exactly specified discrete and completed kernel, ker(theta5) and ker(theta5-hat).',
 'Proved','work_DE/B_dihedral_rigid.tex; next_joint_rigid_symplectic/check_B65_reconstructed.py/.out and B65_reconstructed_certificate.json',
 'B.28; B.60; B.61 actual common marking and original braid words; finite group actions and isotopy extension',
 'B.4(a) and B.4(c): actual cyclic joint rigid-kernel reduction',
 'Family r_u(z)=u/z proves actual discrete commutation; closure transfers it using B28. Literal r in T, intersection C2, all ten transports, six deleted words and fixed-pair linking freshly rechecked after environment loss. Transport d^2r sends omitted point2 to11, explaining distinct further homology quotients. H5 itself is free rank6, not dihedral. Injectivity and completed-kernel closure remain open.'
 ])),dict(zip(fields,[
 'B.66','For every prime ell a nonzero common Q_ell-prounipotent line with degree-two vector w is in both actual source images, fixed by A5, and killed by all full rigid-seven maps and their smaller factors.',
 'Proved','work_DE/B_prounipotent_persistence.tex',
 'B.59 primitive fixed vector and rigid vanishing; B.60 actual source words; B.61 common ordered algebraic base; DE_Stacks2026; DE_HainMatsumoto2003 Appendix A',
 'B.4(c): the full rational prounipotent route retains a nonzero common direction',
 'Strict pointed number-field diagram gives one arithmetic automorphism with distinct scalar alpha^d on graded pieces. Polynomial eigenprojections give compatible preimages in both source Lie algebras, not just finite-stage image membership. Denominators are not uniformly controlled, so no compact pro-ell or actual K element follows. Full accepted proof reconstructed from retained conversation and primary sources rechecked after loss; no numerical stdout invented.'
 ]))]
with path.open('w',newline='') as f:
    wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(rows)
bib=H/'B_separability_references.bib'
assert 'DE_HainMatsumoto2003' not in bib.read_text()
with bib.open('a') as f:f.write(r'''
@article{DE_HainMatsumoto2003,
  author = {Hain, Richard and Matsumoto, Makoto},
  title = {Weighted Completion of {Galois} Groups and {Galois} Actions on the Fundamental Group of {$\mathbb P^1-\{0,1,\infty\}$}},
  journal = {Compositio Mathematica},
  year = {2003},
  volume = {139},
  number = {2},
  pages = {119--167},
  doi = {10.1023/B:COMP.0000005077.42732.93},
  url = {https://arxiv.org/pdf/math/0006158},
  note = {Verified: primary Appendix A, Theorem A.6, Lemma A.7 and Corollary A.11 opened and rechecked after runtime recovery; publisher confirms November 2003 print date, volume and pages. The 2007 online date is not the print year}
}
@misc{DE_Stacks2026,
  author = {{The Stacks Project Authors}},
  title = {The {Stacks} Project: Fundamental groups and geometric--arithmetic comparison},
  year = {2026},
  url = {https://stacks.math.columbia.edu/tag/0BQ8},
  note = {Verified: Theorem 58.6.2(3), tag 0BQ8, gives exact based functoriality; Lemma 58.14.3, tag 0BTX, gives the geometric--arithmetic exact sequence. Both primary pages reopened after runtime recovery on 16 November 2026}
}
''')
with (H/'B_separability_source_log.md').open('a') as f:f.write('''

## B65--B66 reconstructed after execution-environment replacement

The original seventh-hour versions were not included in checkpoint06 and are not represented as byte-preserved. Complete mathematical proofs have been reconstructed from retained conversation. B65's finite data were freshly evaluated against the verified checkpoint06 original common-base braid words by next_joint_rigid_symplectic/check_B65_reconstructed.py; its actual .out and complete JSON are retained. The Q/Birman action was likewise freshly evaluated by reconstruct_Q_birman.py, including its antihomomorphism correction.

For B66, the following primary sources were reopened on 16 November 2026 after recovery. Hain--Matsumoto, https://arxiv.org/pdf/math/0006158, Appendix A: TheoremA.6 (PDF p35), LemmaA.7 and proof (p36), CorollaryA.11 (p37). These give the canonical discrete/pro-ell/full-unipotent comparison and rational-point based Galois action. Web refs turn552view0, turn553view1/2/3. Publisher https://www.cambridge.org/core/journals/compositio-mathematica/article/weighted-completion-of-galois-groups-and-galois-actions-on-the-fundamental-group-of-p1-01/94239BA21D3B20D154B3D024CB3C8996 independently confirms 139(2),119--167, November2003 and DOI10.1023/B:COMP.0000005077.42732.93; the online2007 date is distinct (turn554search0/6). The DOI resolver itself was inaccessible in this retry, so no success is claimed for that URL.

Stacks https://stacks.math.columbia.edu/tag/0BQ8, Theorem58.6.2(3), explicitly makes the pointed functor diagram strictly commutative; https://stacks.math.columbia.edu/tag/0BTX, Lemma58.14.3, gives the geometric--arithmetic exact sequence. Both primary pages reopened completely (turn552view1/2). The remaining B66 eigenprojection argument is supplied in full in the reconstructed proof; it is not attributed as a published theorem about this configuration.
''')
with (H/'report_DE.md').open('a') as f:f.write('''

## Seventh-hour recovery: B65 and B66

The execution environment failed around07:43UTC before the checkpoint07 archive existed. Root restored verified checkpoint06 into the replacement environment. The two complete proofs are now reconstructed as B_dihedral_rigid.tex and B_prounipotent_persistence.tex, explicitly identified as reconstructions in source comments. Their register rows and the two verified B66 bibliography entries have been restored mathematically. No byte identity with the unavailable original seventh-hour files is claimed.

B65 proves that the free rank-six pure cyclic centralizer also centralizes the actual D5 generated by its C5 and a named involution r in T. The two D-stable rigid-seven maps are zero; all ten remaining full maps have the same kernel after their actual transports. The exact six-image map theta5 into PB6 has that discrete kernel and its completed map has that completed kernel. Fixed-pair linking removes the center in both categories. The transport d^2r sends omitted branch point2 to11, so two distinct genus-two homology tests need not agree. The freshly rerun check_B65_reconstructed.py/.out verifies every permutation, subset, source-word deletion and linking assertion against checkpoint06 inputs.

B66 uses the actual common K-rational ordered point and strict based Galois functoriality. A single arithmetic element acts as alpha^d on every lower-central graded piece. Its explicit polynomial weight-two eigenprojections give compatible actual source preimages of a nonzero common prounipotent element with degree-two vector w, fixed by A5 and killed by all full rigid tests. This closes the rational prounipotent separation route for the existing line. Unbounded possible denominators prevent an inference of any compact pro-ell or full profinite element.

The newer exact Q/Birman note and action certificate were also reconstructed and freshly rerun: next_joint_rigid_symplectic/Q_Birman_reconstructed_note.md, reconstruct_Q_birman.py/.out and Q_birman_reconstructed_certificate.json. They establish an intermediate factorization through Z2*Z2*Z, an exact F3 base, and an explicit rank-four free-fiber action. Q injectivity and the final theta5 comparison remain Open. The last-conjugator extraction is explicitly antihomomorphic; inversion corrects it. Full recovery provenance and losses are listed in recovery_ledger_DE.md.
''')
print('Added B65/B66 register rows; verified primary bibliography; source log; recovery report.')
