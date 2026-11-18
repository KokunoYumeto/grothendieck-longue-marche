# Method record

## Diplomatic phase

The root assistant alone visually read, transcribed, reread, and audited all 42 supplied scan pages in ascending scan order. For every page it inspected the whole image and both supplied overlapping halves; enlarged crops were used for small or ambiguous writing. No OCR was used on the supplied scans. Page files, the element inventory, and the progress log were written incrementally. A support agent handled structural validation, compilation machinery, and packaging only during this phase; manuscript reading was not delegated.

The notation table was maintained across the package and reconciled before the freeze, including repeated quotation conventions, exponents, doubled alphabets, and script letters. After the initial page-by-page rereading, the root made a separate image-to-text audit of every page. The corresponding `done` and `audited` entries are in `progress.log`; `visual_audit.md` records the targeted comparisons. Typed and reused pages, cancellations, insertions, marginal writing, diagrams, and drawings were transcribed as page content.

The final syntax check compiled all 42 fragments under a disposable wrapper. It was a syntax check, not a claim that editorial macros had an authoritative visual rendering: the returned transcription remains a fragment without a preamble, as requested. The per-page files and combined fragment have 43 SHA-256 records in both `progress.log` and `frozen_transcription.sha256`.

## Freeze and context boundary

The transcription was frozen at **2026-11-18 10:49:51 UTC**. Context ZIP member contents were first opened at **10:49:56 UTC**, after the freeze. During initial attachment inventory only its ZIP directory metadata had been listed; member contents remained unread. No page, combined transcription, inventory reading, or doubt marker was changed as a consequence of the context or research.

## Post-freeze research

Research work was delegated only after the freeze. The three contributors worked from the frozen transcription and inventory, the supplied context, and external sources; none inspected or transcribed the supplied manuscript images. The root handled projective-bundle calculations and wider-context synthesis, read the complete supplied results-state register and Hua modernization, reviewed the research contributions, and opened the primary sources used in the final synthesis. One contributor visually collated a separately downloaded published reference book for the typescript identification; that was not a source for changing any manuscript reading.

Every research note has a context comparison, with actual keyword-search registers retained. Earlier result-state entries are identified as prior-run claims or leads, not automatically established results. Mathematical improvements and expected readings are confined to research notes. Exact short quotes were checked against the frozen TeX; normalization of whitespace for that check does not alter the transcription.

`CHECK_EVENTS.tsv` records the actual work: targeted checks, independent arguments, exact computations, cited statements checked within their source hypotheses, background carried without a new proof, and explicit refutations. The `who` field identifies GPT-6 Astra Pro, the inherited effort setting (no separate effort value exposed), the run, and the responsible root or research contributor. Source collation is distinguished from theorem proof. Symbolic and finite computations are not represented as proof-assistant certification.

Independent post-freeze peer review covered the Euler/Postnikov arguments, the Schwarzian signs and coefficients, the monic-algebra descent argument, and the projective first-jet and characteristic-two claims. Review outcomes and their limits are retained in the check ledger. Broader classification, global existence, conical triangulation, and arithmetic-realization questions remain open where the supplied argument or this run did not settle them.

## Packaging and persistence

The hourly checkpoint ZIPs contain the deliverables and work documentation present at their preparation time, without input scans, supplied context, downloaded source PDFs, or earlier checkpoint ZIPs. They were saved at the requested hourly cadence; their records are in `progress.log`. The final archive uses the same input exclusions and contains all completed deliverables and research records. The final validation rechecks the 43 frozen hashes, exact page concatenation, inventory completeness, note IDs and event coverage, and ZIP CRC. It does not claim that mechanical validation proves every reading or every mathematical assertion.
