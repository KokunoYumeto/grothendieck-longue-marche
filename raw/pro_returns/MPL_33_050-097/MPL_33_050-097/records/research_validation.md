# Research-note validation

The final notes contain 72 ordered items, N01–N72, followed by the two requested standing sections, a comparison with every supplied results-register row and a primary-source bibliography. Each numbered item has a cote/scan locator, a classification, a brief source quotation and its own actual context search; all 14 own-idea items state confidence and its reason. The note bodies were kept to one through four sentences, with locator/context/confidence metadata separate.

The supplied context consists of two files. No full source file merely listed by its register was treated as present, read or reviewed. `scripts/search_context.py` and `records/context_queries.md` record all 72 searches, including negative results and the distinction between broad lexical hits and a corresponding theorem. The original context files themselves are not copied into this package.

Direct exact arithmetic in `scripts/research_checks.py` confirms the coordinate calculations used in N43–N46 and N70 and the matrix compatibility used in the two-point sheaf test N66. The latter is conditional on the standard sheaf interpretation visible in the excerpt, with missing-definition qualifications retained in the note. A fresh visual look at the upper half of scan 051 confirmed the literal typed Hom formula during the research phase; no transcription was altered.

The 181 inline mathematical spans in the Markdown notes were extracted to a disposable TeX file and compiled successfully with XeLaTeX, with no TeX errors. This verifies mathematical syntax, not the truth of every discussed source claim. `verify_notes.py` checks the item sequence, per-item search coverage, metadata, source-quote presence, own-idea confidence fields, standing sections, inline delimiter pairing and reference URL syntax; the final run passes.

Literature verification limits are stated in the notes, including failed full-PDF retrieval for published EGA and failed chapter retrieval for Fujiwara. The source comparisons do not authorize any revision of the frozen manuscript. No claim of a complete collation against all published texts or of new resolution of an arithmetic register entry is made.

