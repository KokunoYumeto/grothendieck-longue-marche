# Mechanical transcription QA

Completed 2026-11-17 22:58:19 UTC.

## Scope

These checks concern TeX syntax, file structure, and mechanical extraction of recorded doubts. They do not certify handwriting readings, visual completeness, or mathematical assertions. The auxiliary tooling reader did not view the manuscript images or open the context archive, and did not edit page or combined transcription files.

## Compilation

XeLaTeX compiled an exact snapshot of the combined fragment with exit code 0 and no TeX errors. All 38 scan markers, 002 through 039, were reached. The combined source remained unchanged during compilation.

Snapshot SHA-256: `f5b4a21fa7e2d5bcac3f2f42e655abe0cbd277b4c3442b07e9c0438abf5a7932`.

The temporary output was XDV, not a deliverable PDF. The harness supplies neutral diplomatic macros; `\diagram` retokenizes its argument so TikZ matrix ampersands retain the necessary category codes and admits bare mathematical arrays. Installed amsmath, amssymb, mathtools, array, tikz-cd, and TikZ libraries were loaded. Since ulem was unavailable, the harness supplied underline fallbacks. These definitions are for syntax checking, not an editorial rendering specification.

The reusable sources are `records/run_tex_harness.py` and `records/tex_harness_template.tex`. Their engine products are written exclusively to temporary scratch space.

## Structural validation

The validator reported 38 page files, 761 inventory rows, zero errors, and zero warnings in its pre-research mode. It confirmed exact ordered page concatenation, allowed inventory kinds, page markers, balanced structures, and the saved page/audit log structure. There were 0 duplicate inventory element identifiers and 0 exact duplicate inventory rows when the element identifier was excluded. This does not establish semantic uniqueness of visually distinct elements.

The delimiter checker was tested with synthetic nested mathematics inside text macros, p-columns, and nested arrays. Those legitimate cases passed. Deliberately unmatched nested dollars and dollars in an ordinary math column were rejected.

## Doubts assembly

`records/assemble_doubts.py` assembled 333 current unsure markers, four illegible spans with a recorded total estimate of nine words, 224 retained page-record doubts, and 73 abbreviation/expansion pairs. The 183 historical records without an exact current-marker match remain in a separate history table; absence of an exact string match does not imply resolution.

The primary reader supplied and reviewed the notation preamble and legibility prose. The explicitly authorized default confidence was low: it was applied to 296 current unsure markers without one exact recorded confidence match. No conflicting exact recorded confidences were found. The assembler preserves distinct proposed abbreviation expansions without selecting between them.

No mathematical check events were added by these mechanical operations. The primary reader controls the subsequent freeze and context opening.
