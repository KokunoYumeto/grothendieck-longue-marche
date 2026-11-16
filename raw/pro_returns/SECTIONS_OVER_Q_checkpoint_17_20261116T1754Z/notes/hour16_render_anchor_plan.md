# CP16 render anchor plan

Prepared script: `code/render_hour16_qa.py`. It has passed Python syntax compilation and has not been executed. Rendering waits for the parent's final-PDF confirmation.

The script reads all correction records from hours 7 through 16. It resolves every recorded repaired horizontal overflow above 2 pt in the current PDF, with statement bounds to exclude later citations. It also requires the A194 certificate paragraph despite its 1.20303 pt overflow. Historical page numbers are not used for these targets.

| Correction record | Required source anchor |
|---|---|
| Hour 7 | A.103.1; A.108.7; A.109.11 |
| Hour 8 | A.116.3 |
| Hour 9 | A.128.1; A.128.22; A.130.S5; A.132.2 |
| Hour 10 | A.144.3 |
| Hour 11 | A150's three certificate-path lines; A.154.1 |
| Hour 12 | A.160.2 |
| Hour 13 | A.179.1 |
| Hour 14 | A.181.1; full front matter/TOC |
| Hour 15 | A.189. [Proved], including its repaired statement display |
| Hour 16 | A194's `ninth_root_subfield_unit_certificate.py` paragraph; A.196.1 |

For hour 7, whose JSON lacks equation-level keys, the exact anchors were recovered from the saved overflow logs and the corrected source. For A150 all three repaired path lines are resolved, including multiple pages if the paragraph moves across a page break.

The final execution requires actual statement headings A193 through A204. It renders every page from A193 to Part B, all reference pages, the complete front matter/TOC, and distributed earlier samples. Every historical repair page receives a separate scale-2 full-resolution image, together with all new statement opening pages and selected detailed formulas. The contact sheets use scale-1.35 source images.

The live mapping will be saved as `notes/hour16_render_anchor_map.md` with the PDF hash, all resolved page numbers in the JSON render record, and explicit visual-review-pending status. The script cannot certify actual image review; the parent performs that review.

