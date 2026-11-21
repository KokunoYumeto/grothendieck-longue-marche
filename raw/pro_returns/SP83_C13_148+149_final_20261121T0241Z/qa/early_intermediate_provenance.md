# A15: provenance of four retained early intermediate crops

**All four original rectangles are now recovered exactly.** This standalone addendum resolves the missing-coordinate finding in `reader_a_method_findings.md`; that earlier report remains unchanged as its original **19-finalized-audit snapshot**. The later adjudications remain the main reader's work.

## Recovered geometry

Coordinates use the original JPEG pixels and Pillow's `[left, top, right, bottom]` convention: left/top inclusive, right/bottom exclusive. The source is `source/SP83_C13_148+149_scans/148_scan051.jpg` for the first row and `148_scan053.jpg` for the other three.

| Retained crop | Exact original box | Clockwise rotation | Final size | Unsharp percent |
| --- | --- | ---: | ---: | ---: |
| `148_scan051_r_arrow.png` | `[631, 1612, 1023, 1745]` | 0° | 2300 × 780 | 115 |
| `148_scan053_cela.png` | `[356, 1627, 1032, 1714]` | 0° | 3000 × 386 | 105 |
| `148_scan053_margin3.png` | `[20, 720, 746, 1409]` | 52° | 3000 × 3021 | 105 |
| `148_scan053_margin4.png` | `[20, 1166, 657, 1812]` | 54° | 3000 × 2990 | 105 |

After cropping, rotated images use Pillow BICUBIC rotation with `expand=True` and white fill. Every image then uses a LANCZOS resize to the stated final size, followed by `UnsharpMask(radius=1.2, percent=<table>, threshold=3)`. The rotated intermediate sizes are 990 × 997 for `margin3` and 899 × 896 for `margin4`.

## Evidence and limits of the recovery

The original first-pass generator files for these four intermediates were not located in the retained proposal/scripts work. The later 053 `crop_transforms` entries document different, superseding clause strips and do not supply these two early rotated rectangles. The missing geometry was therefore recovered by pixel matching: normalized grayscale cross-correlation located the unrotated crops; boundary geometry and scale/rotation registration located the rotated ones; integer rectangles were refined against the source image. No OCR, textual recognition, or mathematical reading was used.

The final verification reconstructs the candidates **in memory only** and compares every RGB channel against the existing crop files. All four have **zero differing pixels, zero differing channels, and zero maximum channel error**. Default PNG encoding of each in-memory candidate is also byte-identical to its retained PNG: **true**. This supports exact source rectangles and output transformations, not merely approximate locations.

This is an empirically exact reconstruction, **not a claim that the original command log survived**. Local-crop and full-source autocontrast are identity operations on these four pixel regions, so their historical inclusion cannot be distinguished from omission. No additional coordinates remain missing among the four A15 files.

## Evidence role and preservation

**None of these four retained intermediates is final mandatory evidence.** At this check, each appears in its accepted record only in the `main_reader_crops` registry; no accepted change, supplied-mark decision, implicit decision, or final audit evidence field cites it. The JSON companion records those reference locations and the accepted-record hashes at the time of this check. The report does not alter those records.

No crop, source scan, half image, accepted page/record, aggregate, or frozen reading was written, replaced, regenerated on disk, or deleted. Candidate arrays and temporary PNG encodings existed only in memory. Before/after SHA256 values for every retained crop match:

| Retained crop | Unchanged SHA256 |
| --- | --- |
| `148_scan051_r_arrow.png` | `8e2b293dd11a0885753829af6c173972011316585b729c01d4ba254f3bbcb4f8` |
| `148_scan053_cela.png` | `48b4b965daa68af816ff1f7ec3c9530cc3c8ef14f86605ae2f2ba78e3ad3caa5` |
| `148_scan053_margin3.png` | `cc3bce9c4d3090b4463116a49a58513bbce5a99c69a8d66a009f5214a68c0220` |
| `148_scan053_margin4.png` | `9a8a89e3d9bfce41ca99fd3b7a7caa92dcbae72abe93795d60c4417301c72a38` |

The original method Markdown/JSON reports and their generator retain their recorded hashes. They were not rerun or updated to a later adjudication count.

## Reproducible documentation

- `result/qa/early_intermediate_provenance.json` contains complete boxes, transformations, source/crop hashes, RGB comparison counts, PNG-byte comparisons, and evidence-role checks.
- `result/qa/early_intermediate_provenance.py` verifies all four recipes without writing image files; it writes only this addendum and its JSON companion.
- `result/qa/early_small_crop_recovery.py` and its JSON/search outputs retain the two small-crop recovery process.
- `result/qa/early_margin_crop_recovery.py` and `early_margin_crop_registration.json` retain the two rotated-crop registration process.

Verification UTC: `2026-11-21T02:19:00.168541+00:00`. Pillow version: `13.0.0`.
