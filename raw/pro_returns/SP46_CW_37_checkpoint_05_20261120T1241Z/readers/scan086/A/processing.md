# Reader A — scan 086 processing and coverage log

## Scope and inputs

Read in full: `out/briefs/brief_v08.md`, `out/briefs/conventions.md`, `out/PREAMBLE.tex`, and the assigned scan086 packet (`meta.json`, `C.tex`, `H.tex`, `C_context.md`, `notation.json`). The long notation-table delivery was truncated in the tool output; its missing scan071 entries were subsequently read from the same permitted notation file. No other page image, source transcription, reader output, external text or OCR was accessed. H is description only, and all report rows use `h_reading: null` and `diff_h: false`.

## Source-image viewing order

1. `B37-04_37_scan086.jpg`, 1700 × 2150 px: one actual visual view, for layout.
2. `B37-04_37_scan086_a.jpg`, 1700 × 1155 px: one actual visual view, read line by line against the packet.
3. `B37-04_37_scan086_b.jpg`, 1700 × 1155 px: one actual visual view, read line by line against the packet.

The halves are top/bottom. Half a begins at whole-image y=0; half b begins at y=995, with a 160 px overlap. Dimensions were read with Pillow, without rendering extra views. No source image or half was reopened or enlarged.

## Half-a reading

Read and compared the typed pagination; entries 3.8, 3.9 and 3.10; §4 and entries 4.1–4.6; §5 and entries 5.1–5.4. The cropped bottom edge of 5.5 was completed using half b. Checked each acute/grave accent, apostrophe, hyphen, comma, full stop, decimal field, section sign and leader series. The live wording agrees with C. The capital S in 5.1 has a single ordinary typed outline. The dashes framing 541 are added to the pagination macro. The §4 low mark and the old letter under d in 5.3 remained open. A fine pale vertical trace crossing the leader interval also remained open as a possible nontextual surface feature.

## Half-b reading

Read the overlap and entries 5.5, §6 and 6.1–6.11, followed by the archive number. Checked the live words and their exact accents, singular/plural endings, hyphens, apostrophes, numeric labels and leader endings. Confirmed the unmarked C-context readings d under the first J, j under the second J, and j under n in Détermination; these were settled by the half and were not cropped. The old f-position character at 5.5, the overprint in schématique at 6.10 and the punctuation after schéma remained open. Two small dark diagonal marks above the 6.3 leaders were newly noted and remained open.

## Open loci listed after both halves

Seven loci were retained for one close view each:

| Crop | Whole-image bbox | Question before inspection |
|---|---|---|
| A086_01_section4_point.jpg | [1125, 318, 1285, 378] | Shape/material status of lower mark right of the §4 period |
| A086_02_de_underprint.jpg | [592, 966, 704, 1020] | Older a/e beneath live d in 5.3 |
| A086_03_valuatifs_underprint.jpg | [612, 1118, 829, 1171] | Older s/b beneath f in 5.5 |
| A086_04_schematique_underprint.jpg | [553, 1854, 788, 1912] | Older character beneath i in 6.10 |
| A086_05_schema_punctuation.jpg | [977, 1857, 1098, 1911] | Comma or period after schéma in 6.10 |
| A086_06_detached_pair.jpg | [1358, 1478, 1455, 1548] | Shape/material status of detached pair above 6.3 leaders |
| A086_07_vertical_trace.jpg | [749, 385, 867, 492] | Ink versus paper disruption between upper leader rows |

## Crop processing and delivery

All crops were created directly from the original whole-page JPEG, once each, by `make_crops.py`. Each was converted to grayscale, autocontrasted with a 0.3% cutoff, and resized with LANCZOS to 2600 px wide at the original aspect ratio. Rotation: 0°. No sharpening. JPEG quality: 97, no chroma subsampling. Exact output sizes and parameters are retained in `crop_manifest.json`.

Delivery/view sequence: crops 01–03 in a batch of three; crops 04–06 in a batch of three; crop 07 alone. Every requested image was actually delivered and inspected exactly once; there were no truncated image deliveries, repeat requests, replacement crops or recrops. The manifest records one delivery request and one visual view per crop.

## Outcomes

All five explicit C doubts are represented by decision rows. The a/e and s/b underprints and comma/period doubt remain unchanged. The low mark at §4 is represented by its small oblique oval and observed lower-right position rather than assigned punctuation. In schématique, the low surviving foot leaves j as an additional possible old letter; the retained alternatives are l/t/j. The detached point pair is reproduced in TikZ with its function and origin left uncertain. The fine vertical trace has a white central interruption and gray sides and cuts the existing typed leader; it is a crease or scratch and is excluded from the text.

The two minor graphic loci have no established attribution. The inventory's “unnamed hand” labels identify this absence of attribution; the transcription does not classify their material as handwriting. No mathematical proposition was tested or used: `check_events` is empty. The page contains headings only, not a mathematical argument.

## Post-writing verification

Only JSON/schema and source balance checks are performed. The check script and its output are retained here. No TeX engine, build, rendering or compilation was attempted.
