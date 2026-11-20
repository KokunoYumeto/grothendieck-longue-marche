from pathlib import Path
out=Path(__file__).resolve().parents[1]
def append_once(name, marker, text):
    p=out/name
    s=p.read_text()
    if marker not in s:p.write_text(s.rstrip()+'\n\n'+text.strip()+'\n')
append_once('notation.md','| D and I alphabets on scan 006 |',r'''
| D and I alphabets on scan 006 | Isolated upper D has a long internal returning stem; mathbb D. Domain N retains mathscr N/N. The downward-map I and both upper-note I forms have separate returning stems; mathbb I. Other D and lower I forms remain plain | 006 | Occurrence-specific; script/plain N remains uncertain |
| Map labels on scan 006 | Sideways chain begins J; u_eta/g/y and u_xi/f/x remain crowded; both vertical memberships open downward. Live lower map is k/kappa/K; older oval-and-stem letter resolves phi | 006 | First live occurrence carries each shared doubt; cleaner repetitions do not resolve case/alphabet independently |
| Relation and index details on scan 006 | Long calculation dash stays unbroken. Large lower opening relation has right-converging strokes, >/=; final equals has two parallel bars. The x/y comparisons are strict <. Image index is <=n | 006 | Literal signs; no correction from the expected computation |
| Subset symbol and F chain on scan 006 | Two-lobed upper form with central stem resolves Phi; n-prime,n. F0 is plain; F1 and F2 have separated returning stems, mathbb F. Footer is pi_0(F_*,x) | 006 | Each resolved locally; pi_0 is not changed to pi_1 |
| Canceled and ambiguous forms on scan 006 | Upper old I_n/D_n, old image qualifier in n/<n, crossed connector downarrow/I/=, opening Soit/Sinon, old tilded D_n-prime/D_n and B/mathbb B/mathscr B remain uncertain | 006 | Cancellation extent retained; no live connector added beneath the canceled cluster |
| Graphic geometry on scan 006 | Common D sits between membership rows; n-double-prime crosses the upper arc; lower arc has a break. Open loop has separate ends and lower returns. First lower F-pair head is detached. Additional points and short traces are literal paths | 006 | Preserve positions and gaps without assigned mathematical roles |
''')
append_once('abbreviations.md','| str. |',r'''
| Gr-stacks | Gr-stacks / group stacks | 006 typed strip | Possible interpretation only; exact written hyphenated form retained |
| ens / d'ens | Ensemble(s) / d'ensemble(s) | 006 | No final stop supplied; number is not inferred from an abbreviation |
| str. | Strictement | 006 | Separate terminal stop visible |
| croiss. | Croissante / croissant | 006 | Separate terminal stop visible; no extra comma supplied |
| hom.topie. | Homotopie | 006 | Both internal and terminal stops are visible and retained in the text |
''')
append_once('legibility.md','Scan 006 combines',r'''
Scan 006 combines readable sideways type with a densely annotated handwritten working sheet. The type is complete, including completion signs and an unfilled n–N gap. Clear stems resolve several D/I/F alphabets, but the overwritten map labels, older qualifiers, B alphabet and canceled opening remain least secure. The lower calculation relation remains >/= from its converging strokes even though all three readers and both witnesses had equals. H omits much of the margin and small geometry, expands or abbreviates the footer differently, closes the open loop, and moves the separate right map. C preserves far more detail but leaves some resolvable doubts, regularizes several placements and omits small detached marks. These marks have been recorded without assigning them mathematical meaning.
''')
append_once('workflow_assessment.md','# Scan 006',r'''
# Scan 006

The main reader compared three complete independent returns before viewing 25 distinct crops (13 reused reader crops, 12 new crops). A report-only consensus was insufficient for a doubled F2, the canceled left connector, common-D placement and the lower calculation relation. A's doubled F2, B's wholly canceled connector and open loop, and C's common-D placement each survived local adjudication; other minority readings did not. The main crop introduced >/= and several detached marks where every return had inherited an omission or an ordinary equals. No full/half scan was viewed by the main reader.

A stray doubt-table row explicitly labelled scan 7 was removed from the scan-6 text packet and all three readers acknowledged its exclusion. H's drawing header correctly identified scan 6. One crop return was truncated before delivery; the same existing file was redelivered once, not recropped. Three text-only helpers assembled the page, normalized records and audited implementation; they did not view images, decide readings or perform mathematical proof checks.
''')
append_once('workflow_events.md','## v06 — first used on scan 007',r'''
## v06 — first used on scan 007

Scan 006 exposed a stray other-page C doubt-table row, an entirely canceled connector represented by some readers as a live line plus a struck sign, displaced shared labels, a gapped head and several additional points. v06 requires excluding explicitly different primary-page rows, separating surviving live strokes from canceled clusters, and preserving shared-label/arc overlap geometry. It reiterates exact TeX comparison of rotated signs and complete local alphabet inspection, and clarifies shared uncertainty versus independent resolution. The larger lower relation remains >/= from the crop despite all three equals readings; the brief again makes majority agreement subordinate to the ink. Twenty-five main crops were inspected once (12 new, 13 reused), with one delivery failure retried unchanged.
''')
print('Updated scan006 notation, abbreviations, legibility and workflow text.')
