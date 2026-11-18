# Checkpoint05 build repairs

The first expanded build on18November2026 stopped at a plain-text check-record expression, `mate c^{-1}`, because the caret was outside mathematics. The arithmetic metadata and builder now say “the inverse of c.” No mathematical statement changed.

A missing-glyph warning was then made fatal by enabling `tracinglostchars=3`. It located an older token in `finite_checks/b5_fourbranch.tex`: the étale cohomology subscript used a math acute accent inside a roman wrapper, producing a missing U+0013 accent. That token now uses the explicit text subscript “ét.” The corrected page is included in the checkpoint05 visual sample. Earlier visual samples did not notice this accent; their statements that no missing glyph was observed describe those observations, not a successful missing-glyph log gate. The new build gate checks it directly.

The B145 final statement was also clarified before the final build. All seven twists have the exact relative-class-number unit test. The pointed split twists over F27 are1 at the four original F3 markings and0,4,6 at the twenty-four new markings. Twists2,3,5 are not called pointed witnesses over F27. This correction changes no equation, finite certificate, field-first minimum, general criterion or status.

The final three-pass build and actual page inspection are recorded separately in `build/BUILD_STATUS.json` and `notes/PDF_QA.json` after completion; no inspection is inferred from this repair log.

The root visual inspection also caught literal “quad” text in the older B80 display of the ranks12,96,256, on page175. The intended TeX spacing commands are restored. All90 selected pages are compared pixel-for-pixel after this final rebuild; a previous visual reading is carried only for exact rendered-pixel matches, and every changed page is viewed again.
