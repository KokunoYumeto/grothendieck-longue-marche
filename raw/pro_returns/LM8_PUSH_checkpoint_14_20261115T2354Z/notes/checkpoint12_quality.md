# Checkpoint 12 typesetting and verification

The frozen paper has 474 pages and SHA-256
`0ead4086e0a919c6e4429cced6ed300368e9aa925f9a9a42c7b09a0a8e7609e9`.
The register has 263 numbered statements: 215 Proved, 8 Refuted, 10 Known,
and 30 Open. All 80 requested lead/task items remain mapped. The five
newly integrated fully audited statements are A.63, A.64, A.65, D.77,
and D.78. Their full proofs, primary-source checks, exact certificates
and independent audit ledgers are retained.

The first build stopped on the undefined `\Sha` notation in D.78.
All four occurrences were changed to the paper's existing
`\operatorname{Sha}` convention. The failed console and complete build
log are preserved under `notes/checkpoint12_build_attempt1`. The next
four-pass build completed successfully. Both before and after the
notation correction, the recorded passes have zero overfull boxes;
the final completed four passes each have zero overfull boxes, including
zero above 2 pt. The final log has zero warnings, unresolved references
or citations, and missing characters.

The seven unchanged BibTeX metadata warnings remain individually
identified: missing publisher `DE_Kato2004`; missing year
`A_LorenzRoquette`; missing journal `fghLuoWatanabe` and
`PBC_MilneCM2007`; simultaneous volume/number and missing publisher
`fghOlssonTangential`; and missing year `PBC_SchnepsSurvey`. No citation
is unresolved. All 139 bibliography entries have verification
annotations. The root and build PDFs are byte-identical, and all 86
frozen source/bibliography hashes match.

All 39 rendered final pages were actually viewed: 12 by root, 10 by
FGH, 11 by DE, and 6 by PBC. The independent ledgers include each PNG
hash and findings. Their disjoint union equals the complete rendered
selection. The selection covers every new proof, changed summaries,
a spread throughout the paper, and the final bibliography page. All
pages passed. FGH repeated its full selection in two-image calls to
remove ambiguity about its initial batch size. The initial review-union
script stopped on a workspace-relative path prefix in one ledger;
the retained assembly script normalizes that explicit prefix and checks
the actual image hashes. No image or review finding changed.

All 313 encoded historical/current PNGs were regenerated and compared
byte-for-byte against their exact source PDFs. Three unmatched earlier
images remain literal: `qa/checkpoint06/page_283.png`,
`qa/checkpoint06/page_294.png`, and `qa/checkpoint10/page_427.png`.
The source PDFs, reconstruction manifest, exact renderer version and
helper are retained. The seven previously named diagnostic PDF
supersessions remain accounted for; historical actual checkpoint copies
are additionally covered by the complete version index.

The source freeze is `2026-11-15T21:35:20.916208+00:00`. D.79 received
complete independent audits after this freeze but remains an
unregistered notes-only candidate in this checkpoint. D.80 and A.66 also completed full proof and exact-certificate audits
after the freeze and remain unregistered notes-only candidates. None of
these three candidates is counted in the frozen paper or register. Storage verification, history preservation and
research notes continue until the archive capture without changing the
frozen mathematical text.

The complete earlier checkpoint history is now materialized and
independently audited. Every one of 8,391 actual historical entries is
accounted for, using 1,761 distinct exact content objects and 169 exact
current-restoration references. Three obsolete numerical encodings and
the old ZIP wrappers have individual replacements and reasons in
`notes/final_history_preservation.md`. Complete restorations of
checkpoints 09 and 11 passed. The final archive gate additionally
checks every retained history object and all restoration dependencies.

## Completed proof-record preservation gates

Before capture, all numerical replacement gates completed. The main original-presentation trace was regenerated and compared byte-for-byte:172,524,978 records,7,961,213,979 decoded bytes, SHA-256`88131d7209403d3be6312da298482025717fdd6a5d7863b335d0af6407c72fc6`. Its795,416,393-byte source-leaf stream passed a complete lossless codec roundtrip. The old501,122,419-byte v1 trace was freshly compared against the full new trace's prefix, including its exact decoded hash. The primary3 trace and corrected suffix3 trace also passed complete byte comparisons; the first failed suffix3 experiment remains literal with its complete closed-gzip checks. The combined acceptance ledger is `notes/pbc_checkpoint12_replay_completion.json` and the detailed audit is `notes/pbc_checkpoint12_replay_audit.md`.

Root read all three portable restoration helpers in full and checked their archive-relative source, data, leaf and header dependencies and final complete hash/count checks. The primary3 transform initially omitted its required `kind` field; root identified it and the author corrected both retained transform ledgers before acceptance. The generic archive verifier now requires this field explicitly. No mathematical conclusion about C.31 is inferred from lossless storage verification; the relation question remains Open.
