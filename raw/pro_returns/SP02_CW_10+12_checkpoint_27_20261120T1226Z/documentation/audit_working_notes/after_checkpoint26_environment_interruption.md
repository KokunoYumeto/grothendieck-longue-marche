# Execution interruption after checkpoint 26

Recorded during the interruption, before any transcription freeze or opening of the context.

## Verified durable base

Checkpoint 26 was created at 2026-11-20T11:25:35.745440+00:00 and saved at 2026-11-20T11:26:46.764718+00:00. Its exact retained file IDs are libfile_3818bc6a2f6c8191937b0e504d27a17e and file_000000003dc4821095766e3d2e75c81a. The restored archive has 5,886,807 bytes, 1,105 members and SHA-256 c99a7436d991eae0bd6db5fcfa16e2443eced0a85bc63b40b1fedf13085c5072. The hash, member count and every ZIP CRC were checked on the restored bytes.

That archive contains all 106 first-pass page files, 24 finalized audits (033–056), and active audit 057. It excludes the original scans, witnesses and context, as instructed. Those input files have not yet become available again. This snapshot does not claim that the later audit work has been replayed.

## Interruption and actual status

The original execution directory became unavailable at approximately 2026-11-20 12:10:12 UTC. The attempted lexical-check/finalize call for audit 062 failed before any command ran. Page 062 was therefore NOT finalized. The latest successful 062 operation was the dry-run record preview, with candidate page SHA-256 6134d71ec98050db24678b06a1f4d75216140a0d6ce79ebbac0967dfcc6695bc.

Independent new execution calls did not retain created files between calls. A long-lived Python process did retain its private files, permitting the exact checkpoint to be downloaded with the current Library helper and verified. No permission boundary was changed. The original source paths continue to be retried. The checkpoint-27 due time was 2026-11-20T12:10:35.745440+00:00; the interruption prevented the scheduled package from being created at that time.

No frozen transcription exists. The context remains unopened. CHECK_EVENTS.tsv still has only its header; transcription reading has not been counted as mathematical checking.

## Work after checkpoint 26 to redo from the scans

The conversation records the following successful audit finalizations before the interruption. Their files are absent from checkpoint 26 and must be redone/replayed in order against the original images before proceeding:

- 057: finalized 11:26:57 UTC; page SHA e362ed69040a689b92326aa34c0185aa1a871b0f651a958568d4dcf47e81d146. Root viewed all 75 fresh crops. 16 edits, 10 upserts, 39 loci, 22 against C, 38 against H, 47 inventory rows, 105 total recipes, 16 remaining doubts, 6,175 bytes. Mechanical QA passed.
- 058: finalized 11:32:06 UTC; page SHA de04c8c8fc2532fe5eb8fbdf546125284c7e563790db338ffa7919dde80c2f62. Root viewed all 22 fresh crops. Two edits, seven upserts, 13 loci, eight against C, 13 against H, ten inventory rows, 31 total recipes, eight doubts, 2,099 bytes. Mechanical QA passed.
- 060: finalized 11:46:46 UTC; page SHA fda4a7a8cafb9a96dc82ac9269a52aaa22f31ca5e23264b0a825c9c7b42c10b0. Root viewed all 66 fresh crops, including reissuing four images whose earlier output had been truncated. 20 edits, 21 upserts, 47 loci, 32 against C, 45 against H, 86 inventory rows, 102 total recipes, ten doubts, 7,830 bytes. Mechanical QA passed.
- 061: finalized 12:00:43 UTC; page SHA 24a694e0e275e6eb696b86bb38db736c302bb559e49ff881527df74ae3403295. Root viewed all 64 fresh crops. 25 edits, 23 upserts, 47 loci, 30 against C, 45 against H, 68 inventory rows, 101 total recipes, 17 doubts, 6,830 bytes. Mechanical QA passed.

Scan 059 is outside the supplied scope. These historical observations are recovery leads, not substitutes for the required replay. Do not add finalized-audit progress lines for them until the restored page/record revisions have actually been rebuilt and checked.

### 060 decisions retained from the conversation

Preserve internal space e ssentiellement; the clipped cancelled p and uncertain e after res before pectant; clipped cancelled n and uncertain e after homogè before nes; physical divisions diagonali/sable (no hyphen), iso-/typique, exacte-/ment and or-/dre. The generator membership sign was not visible: the reading was ({}_i)_{i I}, without an inferred membership sign. Azymy has overlapping y/u in its third cell; Choisissant has terminal s/t overlap. Draw both forms without assigning their order. The summation sign has a rounded 2-like body and a detached upper bar. The first D parameter has typed I and two handwritten horizontal rightward bars: its possible Gamma/F/T identity remains qualified. The operation word remained droit/direct/tensl/tensoriel, with low confidence and preference based on the final dot, not expected mathematics. The long note has left chevrons, and six insertion hooks were placed beneath their phrases. Typed M/script M and parenthesis/bracket overlaps did not show separate cancellation strokes. Preserve daas and the literal Gamma/order/incomplete grammar and E_i/End M_i discrepancy.

### 061 decisions retained from the conversation

Famille has two a/m overprinted cells, drawn without chronology. In the first constraints word the initial crowded cell after a is i/n (m also possible), followed by two n/t overlaps. Rotated margin reads attention à / contrainte de / commutativité. The nonfree Gamma consists of a typed I and one handwritten roof extending right and turning down at the end, with no T alternative needed. Preserve physical divisions Karoubie/nne and derniè/re without hyphens, margin A explici-/ter ! and d'/exiger. The final e of désigne is outside the scan: retain désign then line break, with no e supplied. Preserve a high apostrophe-like mark after the second rang, with its function uncertain. Underline only u in tout. Système has a t/è overprint followed by a separate live è. Rendant has a/d superposed. The disputed x stays raised in both live/cancelled alternatives. Soit before the basis label has an uncertain initial s/e overprint. The first e in interprété and final de have extra upper vertical marks; draw them without a definite hidden i or independent strike. The final contraintes has o plus a tall stem/head, identity d/l uncertain. The second Hom gamma-like argument has a lower loop and crossing bar, reproduced without assigning an underlying letter. Four brackets were placed relative to their inserted text. The right tensor factor and exponent 2 are handwritten. Archive 60 is a comment.

The crop helper was corrected during 061 to resolve bare scan filenames only by the exact basename inside source/SP02_CW_10+12_scans, and to record the normalized source path. It does not guess another image. Helper SHA after that change was 2a9313603e07d57012b3d5e944eef49ad2488c53bf72ae0a3b53a29063a518af. The earlier grayscale/autocontrast/contrast fix remains required; pending 048 previews and the 043 metadata followup still block freeze.

## 062: observed but unfinalized

Audit ID B10-04_10_scan062_audit001; began 12:00:52 UTC. Baseline page SHA 818f7503d1a568a9dd9238f21d444babec4810f71cc59ffd709ef9428ba7e5fd; baseline record SHA ecf4172cfbd88224eea011d3c363c6ce7c424d71586242a829e418d4a17a52bd.

Root viewed whole, actual _a, actual _b in order before text. Image-first receipt was recorded at 12:01:29.201506 UTC (SHA f1c78be247cc8bc5fd33964422e4e39a140fd921bed60433e29ade2cf704174a); text opened at 12:01:29.458320 UTC (SHA 89b482463227a3c812751b2a1797fd398536cb8c7e5527635a514cd44eb4d8ed). Current text, both witnesses, all C doubts, all 31 loci and 56 inventory elements were read. All 51 fresh recipes were viewed. Orbit/bottom images whose first combined output was truncated were reissued and personally viewed; the original wrong La microcrop was corrected and re-viewed.

The candidate had 18 text edits, 20 upserted loci and ten remaining doubts. These are retained decisions to verify again, not an applied audit:

1. In ainsi, both final cells contain i and s. Draw each overlap in place, qualify ordering, and do not assign a sequential deletion order.
2. Objet has i and o superposed; draw both and qualify ordering.
3. Composé has o with a tall middle upright and a short leftward head. Draw the strokes; d/l identity and layer order remain uncertain.
4. Vrai/verified correction: typed v survives; typed rai is overlaid by smaller handwritten èrifié/érifié. No separate strike was visible. Draw the layers together; retain first-accent doubt.
5. Prefer eu over ou in the qualified live connective because of the medial bar. The cancelled i before it is a separate cell.
6. Place the slanting punctuation stroke across the left edge of the stop after k, not as an independent following glyph.
7. Façon has two crowded cells after fa. First: rounded c-like left bowl, upper bar, diagonal arms and a low left-turning tail, identity y/ç/c unresolved; draw its actual form. Second: a c-shaped bowl crossed by x. The previous reading assigned a live ç to this second cell; the new candidate cancels this second c and leaves the first cell qualified.
8. Preserve semi-/simple at the physical break, conju-/guées, and nécessaire/ment without a hyphen in the last case.
9. The two inserted inequality signs have slanted lower strokes and are handwritten; digits/i/r are typed. Place their bracket beneath their own formula.
10. M-prime-i insertion has a prime above and the distinct dot of its lowered i, not an exclamation mark. Place its curved attachment below-left and rising right.
11. Place the long bracket beneath the entire inserted semisimplicity clause.
12. Initial La: draw the typed L and a narrow handwritten loop over its left stem. It may be a correcting l; there is no separate strike.
13. Brauer argument: typed k under handwritten Z, same position, no separate strike. Its sigma/gamma subscript remains uncertain.
14. Place the class-sigma insertion slash beside its raised sigma, landing after classe.
15. Final simple-object M has an additional upper-left loop and a rounded lower bowl. Draw those extra strokes without inferring a blackboard alphabet. Possible S/U overprinting versus reinforcement is unresolved.
16. Final End argument has possible typed S beneath thick handwritten M. Draw the overlap, qualify S, and do not supply a separate strike.
17. Preserve repeated sss, enn (second n faint but complete), composantsisotypiques, correspondants, unaccented Etude and connait, four terminal stops, literal de S la, and the incomplete parenthetical au cas n'est pas supposé simple. Do not supply où or M.
18. The right-edge e of sous-catégorie is partly visible and remains; this differs from the wholly absent e of désigne on 061. Both lowercase pi forms, every base-change prime and all indices were checked from their own strokes.
19. Archive 61 remains only a comment. Parfaite is typed and has a handwritten rule; retain that distinction in the inventory.

The mechanical support agent retained the 062 baseline digest 8e4433d849833b0d0808a4a24375cc294c1fe9be73a7e90e1178f5a114f74bd8 for 214 protected file hashes plus five active-audit hashes. It has not read scans, witnesses or context, and has not made semantic transcription decisions.

## Continuation constraints

Restore the original attached input ZIP when it is accessible, without opening the context. Keep the old checkpoint untouched. Replay 057, 058, 060, 061, then 062 in the ordered root stream, with fresh personal image inspection and actual-time recording. Do not turn these recovery notes into final page readings or claim mathematical checks. Finish all 106 audits, notation reconciliation and metadata/processing followups before assembly/freeze. Open context README and RESULTS_STATE only after the 107-hash freeze. Full research notes and final readiness remain required. Only the completed final ZIP is to be offered as a download.
