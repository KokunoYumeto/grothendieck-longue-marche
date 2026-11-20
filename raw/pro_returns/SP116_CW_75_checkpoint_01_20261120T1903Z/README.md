# SP116_CW_75 — consolidated diplomatic transcription

Scope: Montpellier archive, Alexander Grothendieck, cote 75, scans 002–015 (14 pages). The operative instructions are the attached `PROMPT(20261120-181640).md`. The two earlier prompt snapshots were not used to supersede it.

Source images and witnesses are the user's supplied package. Witness C comprises the J75-01 and J75-02 page drafts. Witness H is the Commutator project of Michel Hua, commit `aef7db2`, with page number one less than the scan. Witness S consists of the supplied sweep correction rows SA01-K75-01 and SA01-K75-02. All are treated as drafts, with the source image deciding readings.

The main deliverables are the ordered LaTeX fragment and `pages/`, changes, H collation, doubts, inventory, reading notes, error-sheet feedback, hand log, check events, and progress log. The source preamble remains in the supplied witnesses; no new notation macros are defined here. Source images, source witnesses and previous checkpoints are excluded.

`readers/` retains first-reader proposals and detailed observations. `records/` retains the main reader's approved evidence and the machine-readable audit results. `second/` holds the coordinate lists, first readings fixed before the independent readings, independent image-only readings, and the token comparison with adjudications. `crops/` holds the inspected detail images. Coordinates always refer to the original full supplied scan, before rotation or enlargement.

Three first readers receive successive single pages in scan order. The main reader checks their disputed and unresolved places in the images. A different reader then reads each page's specified difficult boxes without access to either witness or the consolidated reading. No OCR, PDF text layer, outside transcription or TeX compilation is used. Mathematical checks are distinguished from reading verification in `CHECK_EVENTS.tsv`.

The scripts assemble the approved records, compare second-reading tokens, check LaTeX balance and package files. They do not recognize source text. A SHA-256 freeze is recorded in `progress.log` after the page readings are final.
