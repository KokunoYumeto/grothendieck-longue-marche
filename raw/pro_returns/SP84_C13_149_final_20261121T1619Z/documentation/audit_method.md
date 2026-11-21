# Independent reading and adjudication records

The independent phase starts only after every first-reading page has been finalized. Each target goes to a reader who did not perform its first reading. That reader receives the original image and the neutral coordinate list, without either witness, the consolidated text, the first box readings, the notes, or the first reader's report.

`crop_boxes.py` enlarges the listed original pixel rectangles with Pillow, LANCZOS, autocontrast and sharpening. It reads no witness text and performs no recognition. It refuses to overwrite existing audit crops. A slanted passage can be rotated for reading; the crop manifest records that rotation. The independent reader inspects every crop and writes its own complete `box, reading` TSV before comparison.

`compare_second.py` compares the two TSVs lexically. It keeps words, commands, digits, braces and punctuation as tokens and ignores only whitespace. Consequently the difference file includes differences of TeX representation as well as manuscript readings. No normalization silently suppresses a symbol, word, index or uncertainty.

The main reader inspects a crop for every differing box and records an adjudication covering every token span within that box. The adjudication identifies the two readings, the adopted reading, visible evidence, its crop and original pixel coordinates, and whether the first consolidated text changed. Equivalent TeX representations can be retained after this review, with the reason recorded. A genuinely unresolved manuscript difference stays doubtful.

In the progress line, `B` counts all independently read boxes, `D` counts boxes with one or more lexical differences, and `K` counts boxes whose adopted transcription changes. The adjacent accounting line records the number of token-difference spans; the complete spans remain in the TSV. These are not error rates.

The first and second TSVs are preserved unchanged after comparison. Corrections are made in the consolidated page and its evidence report. `finish_audit.py` only validates the already written adjudication records and logs completion; it does not select readings. The consolidated transcription is assembled again, then structurally checked without TeX compilation. Its final hashes are frozen only after all audits and the notation review.

Before the first token comparison, the script records the SHA-256 of the neutral boxes, first readings and already written second readings in a per-page comparison provenance file. Audit completion checks those exact inputs remained unchanged. This documents the preserved comparison inputs; it does not substitute for visual adjudication.
