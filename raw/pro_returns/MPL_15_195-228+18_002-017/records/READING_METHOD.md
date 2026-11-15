# Reading record

## Transcription phase

The root reader alone inspected and transcribed all 49 pages, in the requested cote and scan order. For each page the root reader viewed the whole image first and then both supplied halves; all 147 supplied images were inspected. Additional crops or rotations were used only for visual inspection. No OCR was used, and manuscript reading was not divided among agents.

The context archive's central directory was listed at intake with the user prompt, but no member contents were read during transcription. The context remained unextracted until every page had been written, inventoried, reread and audited; the package-wide notation review also preceded the freeze. Page files, inventory additions and actual UTC completion records were saved before moving to the next page.

Main inventory rows came from the primary reader's visual comparison. Insertion, deletion and margin rows derived from the explicit state macros were added mechanically, with their contents checked in the visual reading. The shared notation table and 332 uncertainty entries are in the doubts file. A mechanical helper checked file structure without reading the images or supplying manuscript readings.

## Freeze and research phase

The 49 page files and combined transcription were frozen at **2026-11-15 13:53:15 UTC**, with 50 SHA-256 records in `progress.log` and `records/frozen_manifest.json`. The context was first opened at **13:53:25 UTC**. These frozen files were not changed thereafter.

Only after the freeze did research agents read the frozen TeX, supplied context and external mathematical literature. Their work consisted of research comparisons, source verification, bibliography, locators and metadata audits; they did not inspect manuscript images or amend frozen readings. The root reader reviewed their findings and retained responsibility for the canonical notes.

A post-freeze review reordered inventory metadata to place insertion/deletion/margin rows beside their parent elements, and added separate rows for visible pagination and an internal heading. The root reader revisited selected whole-page images for layout only. This did not change a transcription reading or a frozen file. The inventory review's records preserve its input, mapping and result; the final inventory contains 705 rows, all marked `yes`.

## Verification limits

Mechanical checks establish page coverage, ordering, macro syntax, inventory schema, completion/audit records and preservation of the frozen hashes. They do not prove reading accuracy or inventory exhaustiveness. Braces and environments were checked, but a PDF rendering was not validated because the available TeX executable lacked its format, document class and required packages. The deliverable is the requested preamble-free LaTeX fragment, not a compiled PDF.

Scripts and intermediate reports in `records/` document the actual process. Some historical scripts reproduce earlier stages and would overwrite later metadata if rerun; they are provenance, not an instruction to rebuild the frozen transcription.
