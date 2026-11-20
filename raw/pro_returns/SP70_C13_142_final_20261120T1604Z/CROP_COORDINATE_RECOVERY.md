# Supplementary crop provenance

This register concerns image-processing provenance only. It makes no new manuscript reading decisions. The supplementary register lists named tight crops; the routine top and bottom halves are excluded. No images are included in the deliverable.

## Coordinates recovered from the reader's preserved command history

On 20 November 2026 the root reader supplied these exact original-image pixel rectangles from preserved command records:

| Crop filename | Rectangle `(x0, y0, x1, y1)` | Rotation | Provenance |
|---|---|---:|---|
| `045_un.png` | `(290, 1245, 690, 1330)` | 0° | Root reader's preserved exact command coordinates; absent from the original changes/decision crop fields. |
| `047_identified.png` | `(1290, 650, 1555, 745)` | 0° | Root reader's preserved exact command coordinates; reader also identified the page-047 note as supporting documentation. |
| `045_prenant.png` | `(475, 1385, 885, 1500)` | 0° | Root reader's preserved run summary, corroborated by `CHANGES.tsv:045-06` and `decisions.tsv:M0120`. |
| `047_minus3.png` | `(1050, 1370, 1190, 1515)` | 0° | Root reader's preserved run summary, corroborated by `CHANGES.tsv:047-05`. |

## Filename associations inferred from existing records

For the other already documented rectangles, `scripts/build_crop_register.py` associates filenames with the matching labels and places in the changes or decisions registers. These associations are explicitly marked `inferred_from_label`; they are not represented as saved crop-command receipts. The rectangle values themselves are copied exactly from the cited records, never estimated. A blank rotation field means that the selected coordinate record does not document an angle, rather than an assertion that no rotation occurred.

## Exact numerical recovery

If present, `CROP_PIXEL_RECOVERY.tsv` records a rectangle recovered by pixel template matching and verified by reconstructing the documented `crop.py` transformations. Acceptance requires identical decoded RGB pixels, not an approximate similarity score. The recovery script does not display images, perform OCR, or interpret text.

## Unknown coordinates

Any unmatched crop remains in `CROPS.tsv` with blank coordinates and `coordinate_status = unknown`. The build/check script reports it explicitly rather than supplying an inferred rectangle.

### Scan 030 numerical recovery

The initial filename-to-place inference assigned `030_cancelledQ.png` to a rectangle that actually belongs to `030_parameter.png`. Numerical matching corrected this association without any image viewing or manuscript interpretation:

| Crop filename | Verified rectangle | Decoded RGB bytes matched | SHA-256 of decoded RGB bytes |
|---|---|---:|---|
| `030_parameter.png` | `(685, 1970, 1385, 2100)` | 4,368,000 | `743d016735b6b0a9f8664295f9264d857c1e311ec26495fe6743cc4c3b3a4f05` |
| `030_cancelledQ.png` | `(155, 350, 275, 435)` | 16,657,200 | `716a7d9861a58bd78b6f87d8a1c83d4a30efecce37bad37c08c21ea093aedd60` |

Both use zero rotation. The parameter rectangle was already present in change rows, but lacked its filename association; the cancelled-Q rectangle was absent from the original coordinate fields. Candidate rectangles were located by multiscale normalized pixel correlation and accepted only after exact reconstruction. Approximate correlation scores were never accepted as coordinate proof.

The subsequent batch verification reconstructs each logged rectangle and rotation against its named crop file. Successful equality checks supersede label-based filename inferences in `CROPS.tsv`, with individual hashes in `CROP_PIXEL_RECOVERY.tsv`. This verification creates no new image files or visual readings.

### Earlier scan-026 enhancement recipe

The eight scan-026 crops have 2600-pixel output width. Their dimensions agree with the rectangles recorded for scan 026, but substituting that width into the later `crop.py` recipe did not reproduce identical pixels. The earlier enhancement parameters were not recovered in this mechanical task. Their original documented coordinates and label-based filename associations remain explicitly identified as such; no exact-pixel verification is claimed for those eight crops.

For the remaining 108 named crops through scan 048, reconstruction verified the filename-to-rectangle association by exact RGB equality. The corrected filename associations on scans 031, 033, 034, and 044 are bookkeeping corrections in this supplementary register only: no page transcription, existing change row, or reading decision was altered.

## Command-confirmed additions for scans 049 and 050

The root reader supplied the following exact filename-to-command mappings on 20 November 2026. All rotations are 0°. Existing change/decision references, where present, are added automatically to `CROPS.tsv`.

| Crop filename | Rectangle `(x0, y0, x1, y1)` |
|---|---|
| `049_articles.png` | `(275, 275, 650, 375)` |
| `049_partant.png` | `(905, 575, 1535, 680)` |
| `049_le.png` | `(600, 1385, 680, 1475)` |
| `049_cette.png` | `(1430, 1450, 1615, 1550)` |
| `050_ring0.png` | `(110, 580, 380, 835)` |
| `050_ring1.png` | `(680, 600, 905, 815)` |
| `050_ringinf.png` | `(340, 450, 590, 655)` |
| `050_topP.png` | `(515, 125, 590, 205)` |
| `050_cancelled16.png` | `(1060, 300, 1215, 385)` |
| `050_definition.png` | `(1075, 635, 1660, 785)` |
| `050_margin19.png` | `(20, 1050, 720, 1660)` |
| `050_boundarysentence.png` | `(315, 1115, 1070, 1260)` |
| `050_nb.png` | `(20, 1640, 335, 1985)` |
| `050_orientation.png` | `(310, 1740, 1630, 1950)` |
| `050_cancelledblock.png` | `(330, 1930, 1640, 2345)` |

All 15 additions for scans 049–050 subsequently passed exact reconstructed-RGB verification. The register through scan 050 therefore covers 131 named tight crops: 123 filename/rectangle associations verified by exact pixels, plus the eight explicitly documented scan-026 associations described above. No crop coordinate remains unknown in this coverage range.

## Command-confirmed additions for scan 051

The root reader supplied these exact mappings on 20 November 2026. The register builder includes them only once scan 051 is marked done, and the changes document is refreshed after that completion.

| Crop filename | Rectangle `(x0, y0, x1, y1)` | Rotation |
|---|---|---:|
| `051_margintop.png` | `(15, 180, 940, 610)` | −32° |
| `051_rep.png` | `(15, 600, 395, 1045)` | −40° |
| `051_number20.png` | `(315, 85, 420, 180)` | 0° |
| `051_dispose.png` | `(1050, 70, 1310, 150)` | 0° |
| `051_arcs.png` | `(1090, 390, 1210, 445)` | 0° |
| `051_deduit.png` | `(1460, 670, 1640, 740)` | 0° |
| `051_destination.png` | `(820, 1010, 935, 1115)` | 0° |
| `051_explicite.png` | `(955, 1195, 1310, 1290)` | 0° |
| `051_dec24.png` | `(1350, 1250, 1665, 1455)` | 0° |
| `051_decbody.png` | `(770, 1640, 1295, 1765)` | 0° |
| `051_formula27.png` | `(175, 1990, 950, 2125)` | 0° |
| `051_margin27.png` | `(20, 2105, 345, 2335)` | 0° |

All 12 scan-051 mappings, including the two rotated crops, passed exact reconstructed-RGB verification after scan 051 was marked complete. The complete 24-page crop register now contains 144 named tight crops, all with known original rectangles: 136 exact-pixel associations and the eight explicitly documented scan-026 associations. The per-scan “Inspected crops” subsections in the changes document are generated from this register without adding divergence rows or changing divergence counts.


## Additional final-notation crop on scan 028

The root reader recorded the exact command `crop.py 28 audit_roman 1490 1240 1660 1410` and confirmed that this crop had been visually inspected. The supplementary mechanical task records `028_audit_roman.png` at original rectangle `(1490, 1240, 1660, 1410)`, rotation 0°. The coordinate provenance is this explicit command plus `scripts/crop.py`; its reading decision remains the root reader's responsibility. Numerical reconstruction is recorded separately in `CROP_PIXEL_RECOVERY.tsv`. This addition brings the complete register to 144 crops, with 136 exact-pixel associations and the eight documented scan-026 cases.
