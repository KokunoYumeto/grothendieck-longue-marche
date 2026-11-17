# First build: genuine overflow and its source repair

The first complete checkpoint22 build compiled its TeX passes but failed
the mandatory final overflow assertion. The log reports one overfull box,
231.64224pt, in B109's computation-record paragraph at source lines292–303.
The long unbreakable typewriter path caused it. We replaced the three
program names in that paragraph by the existing hyperref path command,
which permits line breaks at path punctuation. No mathematics changed.

The preceding PDF, complete final log and both formal source files are
retained in records/pdf_qa/checkpoint22_before_overflow_repair/. The full
build-pass directory and failing driver output remain. The independent
mathematical reviews apply to the same mathematical proof; the integrated
B109 source now differs from its isolated draft only in these path commands.
The subsequent build and visible page inspection determine whether the
repair succeeds; no outcome is claimed in advance.
