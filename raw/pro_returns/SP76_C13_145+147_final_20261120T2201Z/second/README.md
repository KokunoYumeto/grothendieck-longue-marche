# Independent image-only reading records

All 24 first readings were complete before this stage began. `first_readings_manifest.json` fixes the SHA-256 hashes of the 24 box lists and the 24 first-reading tables. These historical tables are not rewritten when the final transcription changes.

For each page, `*_boxes.tsv` gives native scan coordinates and neutral coverage labels. `*_first.tsv` records the main reading before the independent pass. A fresh reader receives only the original scan, this box list, the second-reading protocol and macro definitions. The reader saves one enlarged crop per box, writes `*_second.tsv` and image-only observations, and returns before seeing any comparison.

The comparison script tokenizes TeX commands, words, digit sequences and remaining non-space characters. Thus changes in punctuation, wrappers and context span are reported as well as different letters or words. `*_comparison.tsv` preserves the complete script output. The main reader inspects every mismatch on its second-pass crop and writes `*_adjudications.tsv`; the changes log includes both readings, the final decision, crop coordinates and evidence. A token mismatch can leave the transcription unchanged when the ink supports the first reading or when only encoding or the copied context span differs.

The original scans and witnesses are not duplicated in this deliverable. Every second-pass crop is included under `crops/`. No OCR, external research or TeX compilation is used.
