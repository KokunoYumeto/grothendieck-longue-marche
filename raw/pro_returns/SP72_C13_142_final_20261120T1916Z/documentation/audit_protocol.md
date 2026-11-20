# Second-reading protocol

The second-reading phase starts only after all 24 first-reading pages have been adjudicated and written. The assigned auditor must differ from that page's first reader. The main reader assigns one page at a time.

Read the assigned page completely against its image, giving first attention to the error-sheet categories and then checking every word, sign, index, punctuation mark, deletion, insertion, margin note, display and diagram. Use the same reader protocol and conventions. View the whole image once and the existing native halves once each for this second reading. Do not regenerate halves. Reuse saved crops for existing loci; make a single new crop only for a genuinely new unresolved locus. No OCR, external research or TeX compilation.

The audit packet contains the current consolidated page, its inventory and apparatus, the current notation table, source paths, both witnesses, and a manifest of existing crops for this page. Read only the assigned page. Treat both earlier readings and the current consolidated text as proposals, not as evidence.

Write `audit/scanNNN/report.json` with:

- `scan`, `auditor`, `first_reader`, `full_page_seen`, `halves_seen`;
- `complete_page_read`: true only after the complete second reading;
- `inventory_checked`: true only after every listed element is accounted for and the page has been checked for missing elements;
- `changes`: each newly proposed correction or uncertainty, with a unique audit id, exact `before` and `after` LaTeX fragments, `place`, `scan_shows`, `box`, `crop`, `confidence`, and both C/H readings where affected;
- `confirmed_doubts`: each still-uncertain place explicitly considered, and the evidence for retaining or narrowing it;
- `new_inventory`: any missing elements;
- `notation_findings`, `hand_log_additions`, and `notes`;
- `check_events`: actual mathematical events only, using the canonical types in reader_protocol.md. A second transcription reading alone is not an independent re-proof.

Write an optional proposed.tex only if changing the page, so the main reader can inspect the exact proposed edit. Do not change the consolidated page, shared reports or progress log. Return a clear completion statement, number of proposed corrections, and all crop paths needing adjudication. The main reader inspects each proposed change on the scan, resolves or marks it, updates all apparatus, and only then logs the page as audited.
