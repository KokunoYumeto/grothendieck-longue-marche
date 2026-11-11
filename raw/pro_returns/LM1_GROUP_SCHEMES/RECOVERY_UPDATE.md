# Recovery update: C.12 and the additional Python output

This update supplements the complete text-file edition already delivered.
It does not claim that the full paper has been compiled or that a final
PDF or ZIP has been made available.

## Mathematical amendment

C.12 proves

    im(A_p(Z/4) -> PGL2(Z/4)) = PSL2(Z/4),

with image order 24. The class [diag(3,1)] does not lift. The 24
nonsquare-determinant classes already enumerated by the computation are
exactly the missing points of the full sheaf image.

The proof uses the big fppf site. An Artinian local fpqc refinement
preserves reduced words in local rings of overlaps. Unique constant-C4
insertions descend a finite etale torsor and affine word coordinates.
Equality is descended in the representable matrix target. No fpqc sheaf
property for the amalgam is assumed.

This resolves the Z/4 image uncertainty in the earlier C.11 discussion.
It does not change the proved countable infinitude of A_p(Z/4).

C.11 remains Open in the register for the following residual:
full abstract descriptions of the descended Artinian source groups, and
the comparison of A_s(Z) and A_p(Z) with their ordinary integral word
subgroups, have not been proved here.

The Part C.d and Item 2 outcomes remain partly settled for those broader
questions. The Z/4 image question must be removed from their residual
lists. C.10's square-determinant image conclusions now extend to Z/4 by
C.12.

The earlier program output's “24 or 48” limitation remains an authentic
record of what that bounded search alone established. It is superseded
mathematically by C.12 and must not be reported as the final uncertainty.

## Final statement register

The integrated edition has 98 numbered statements:

| Status | Count |
|---|---:|
| Proved | 72 |
| Refuted | 16 |
| Known | 4 |
| Open | 5 |
| Unfinished | 1 |
| Total | 98 |

The five Open entries are C.11, D.8, E.11, E.21, and E.27.
A.10 remains Unfinished.

These are statuses of this investigation. An Open entry does not by
itself assert that the corresponding question is open in the literature.

The manuscript-reading register remains at 57 rows. C.12 adds no new
manuscript transcription or pixel-reading claim. Five checked Stacks
Project references supplement the bibliography.

## Fresh execution evidence

The retained source code/e_additional.py was rerun under Python with
SymPy in the recovered execution service. It exited with status 0;
standard error was empty. Its complete fresh stdout is supplied as
code/e_additional.out: 1,723 ASCII/UTF-8 bytes including the final newline.

This is newly executed output. It is not a purported recovery of the
inaccessible original stdout bytes.

All three Part E JavaScript programs also ran successfully under Node.
Their outputs matched the retained outputs, allowing only terminal
newline normalization. The Part D JavaScript rerun reproduced its
retained output byte for byte, including its final newline.

The six replacement JavaScript sources and their previously delivered
actual outputs remain part of the edition. Together with the recovered
Python source and its fresh output, they provide seven executable
computation files with actual outputs.

The older inaccessible Python sources and ancillary files listed in
report.md have not thereby been recovered. Their provenance limitations
remain in force.

## Execution and delivery limits

The original workspace directory was absent in the restarted service.
Ordinary execution calls did not preserve newly written files across
calls. A continuing shell retained its own files, but those files were
not visible to the separate file-viewing tool.

The full paper source already delivered in chat remains the authoritative
reconstruction. Reconstructing it again from compressed summaries would
not preserve its exact wording.

No completed full-paper LuaLaTeX build, full-paper visual validation,
final PDF, or final ZIP is claimed. The earlier D-only temporary build
does not validate this complete edition.

## Integration

Place these additions beside the files already delivered:

- sections/C12_addendum.tex
- evidence/C12_references.bib
- evidence/C12_result.json
- code/e_additional.out
- RECOVERY_UPDATE.md
- integrate_and_build_recovery.py

The new helper integrates C.12 into the main LaTeX input, appends its
references to the main bibliography, updates C.11 and C.10 metadata,
and inserts C.12 into results.csv. It places this update after the
initial outcome table in report.md, preserving the requirement that
the report begin with all task, Item, Lead, and followup outcome rows.

The helper also applies the three previously disclosed transcription
repairs: A.2's pointwise-identity wording, F.1's missing math delimiter,
and the redundant repeated predicate in the D program.

The helper is supplied as unexecuted source. It has not been run against
the complete recovered paper. Its --build option checks statement and
reading registers, reruns all seven computations against the supplied
outputs, runs LuaLaTeX/BibTeX, and creates an archive only after these
checks succeed. Its --render option produces page images for subsequent
visual inspection; rendering alone does not constitute visual approval.

Use this helper for the 98-statement edition. The earlier
build_reconstruction.py belongs to the 97-statement edition and is
retained only as part of the recovery history.
