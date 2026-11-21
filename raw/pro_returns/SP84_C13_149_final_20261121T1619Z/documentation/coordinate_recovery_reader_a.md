# Coordinate recovery — reader_a

Recorded 2026-11-21 15:10:40 UTC.

## Scope and result

Six original first-reading crop rectangles were requested. One is recovered exactly; five remain unavailable from the preserved provenance checked. No estimated rectangle was entered, and no source reading or frozen reading file was changed.

| Crop | Result | Original rectangle (x0, y0, x1, y1) | Provenance |
|---|---|---|---|
| 149_scan005_c18.png | recovered exactly | (27, 2280, 95, 2351) | reviews/149_scan005.json, audit_boxes entry b29; independently verified by exact pixel reproduction |
| 149_scan005_c19.png | unavailable | — | Filename survives in root_reviewed_crops, but no associated rectangle found |
| 149_scan010_c14.png | unavailable | — | Filename survives in root_reviewed_crops, but no associated rectangle found |
| 149_scan010_c15.png | unavailable | — | An existing rectangle has matching resized dimensions, but did not reproduce the saved pixels; not accepted |
| 149_scan010_c16.png | unavailable | — | Filename survives in root_reviewed_crops, but no associated rectangle found |
| 149_scan018_c10.png | unavailable | — | An existing rectangle has matching resized dimensions, but did not reproduce the saved pixels; not accepted |

## Exact support for scan005 c18

The preserved review metadata explicitly records b29 as x0=27, y0=2280, x1=95, y1=2351. This is an existing coordinate record, not a visually inferred location. Opening the assigned JPEG as RGB, applying that rectangle, and resizing with Pillow LANCZOS to `(2600, round(71*2600/68))`, i.e. 2600 × 2715 pixels, produces every RGB pixel of the saved c18 PNG exactly. `ImageChops.difference(reproduced, saved).getbbox()` returns `None`. This proves that the preserved rectangle reproduces the original crop; no position search or coordinate adjustment was performed.

- Source SHA-256: `b95c557ab9ec40378cbbe1745ca2698065d1d3feb5e753d6d26882afaeea16ac`
- Saved crop SHA-256: `72b11aa30152e8d974f0193c52f891198bc5ae12f066186623123fb2c9e56053`
- Saved/reproduced RGB pixel SHA-256: `8c762e69a50cd793fd63f3ea6421d01ca07ddd37c1c30e4d40e6588bdb83e314`
- Metadata reference: `reviews/149_scan005.json`, `audit_boxes` entry whose `box` is `b29`.
- Coordinate table entry added: `crops/149_scan005_c18.png`.

## Search and rejected evidence

Exact filename searches across the preserved work scripts, review JSON, and documentation found the six names only in their reviews' root_reviewed_crops lists. The six PNG files have empty embedded metadata dictionaries. The saved reader_a working scripts concern later scans and provide no matching original rectangle for these missing entries. No local session-history file was available in the session directory, and the workspace has no Git history.

Existing audit-box metadata was checked only as an explicit coordinate candidate source. Its rectangles were not moved, enlarged, fitted, or inferred from aspect ratio. Two records happened to have the same dimensions after a 2600-pixel-wide resize:

- scan010 audit b16: (272, 2184, 741, 2289), producing 2600 × 582 pixels, the dimensions of c15;
- scan018 audit b11: (280, 1411, 624, 1525), producing 2600 × 862 pixels, the dimensions of c10.

Neither record reproduced the saved crop pixels with any of Pillow's standard resize filters (NEAREST, BOX, BILINEAR, HAMMING, BICUBIC, LANCZOS), using RGB source and target. Matching dimensions alone is not provenance for the rectangle, so neither was entered. These failed checks do not prove what the original rectangles were.

The five unavailable rectangles remain unresolved. Recovering them would require the original crop commands or another exact preserved record; the present documentation does not claim recovery from an estimated location.
