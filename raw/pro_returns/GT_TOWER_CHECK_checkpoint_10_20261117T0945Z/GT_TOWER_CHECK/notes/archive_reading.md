# Cote 148: original scan audit

Reading date: 2026-11-17, 01:30--01:35 UTC.

Official source: https://grothendieck.umontpellier.fr/148.pdf . The source has 72 PDF pages and 35,287,128 bytes. The archive listing's displayed page count is not used for page indexing. Exact HTTP byte-range extraction is documented by code/fetch_archive_pages.py and its actual output, with metadata in archive_page_fetch.json. The downloaded scans, source-page PDF and raw byte ranges are excluded from the deliverable.

We visually inspected complete PDF pages 31, 32 and 33 (manuscript folios 30, 31 and 32), and high-resolution regions on pages 31 and 33. Folio 30 contains the five-point diagram and the total of 542 objects. Folio 32 records 180 + 420 + 1020 = 1620 arrows, with the handwritten correction to the final total. Its programme asks for a fundamental relation system and for expressions in terms of arrows coming from relative dimension at most one.

The lower arrow between the two last configurations on folio 30 has the fractional-twist annotation tw_(1/4). This is visible in the high-resolution source rendering; the first-pass transcription's denominator 3 at that occurrence is corrected. It agrees with the quarter-turn path used in the specified EXIT_TOWER B.25 realization. No source image is included in this archive.

These three scans do not give the exact affine pin coordinates, the transport paths through N+i N^2, or the complete relative homotopy classes stipulated in B.25. The audit proves all relations for that specified realization, and B.5.1 gives an explicit invertible typed change of arrow generators for every other choice. No zero discrepancy with an unstated original path convention is inferred merely from matching incidences, endpoint germs, or arrow counts. The subsequent comparisons below record the surrounding pages and the later marking operations.

## Context and marking operations: subsequent inspection

We visually inspected PDF pages 29, 30 and 34 (manuscript folios 28, 29 and 33). Page 29 is a blank verso, page 30 is the computer-printout wrapper, and page 34 records finite automorphism classifications. These pages contain no additional affine transport recipe for the 1620 arrows. The exact extraction record is archive_page_fetch_29_30_34.json.

We then opened and visually inspected all six original PDF pages 52–57 (manuscript folios 51–56, internally numbered 8–13). Page 52 defines erasure of a named subset of marking points. Page 53 formulates the corresponding groupoid and forgetting functors. Page 54 erases cutting circles and contracts graph edges. Page 55 caps boundary circles and describes mixed erasure. Page 56 inserts new points in the existing open marking intervals and states the resulting marked object up to its specified isomorphism. Page 57 gives the cyclic-torsor maps for uniform partial erasure and uniform additional marking. These readings concern the main legible text; the heavily corrected marginal note on page 53 is not used as a verified formula.

The exact functors in these pages retain the chosen surface and its marked subsets. A comparison with the concrete five-point path realization therefore needs an assignment of those marked surfaces and operations to that realization, followed by the relative-path comparison. The displayed cyclic-torsor maps supply part of that data but no computed word in the five free-by-free generators for each of the 1068 unfixed arrows. That comparison remains the precise B.5 source issue. We have not assigned zero discrepancy solely from the operation names. Extraction code and output: code/fetch_archive_operations.py and .out; metadata: archive_page_fetch_52_57.json. Source scans remain outside the deliverable.
