# Structural repairs without compilation

The supplied deleted macro passes text to ulem strikeout. Paragraphs, displayed formulas, and the supplied paragraph-level diagram macro need a paragraph container inside that argument. The listed complete outer arguments were placed, byte-for-byte, inside a standard minipage and mbox within the existing deleted wrapper. Every nested local deletion, insertion, formula, and diagram remains inside the same outer cancellation boundary. This is a syntax change and adds no collation row. Each block is now an unbreakable box with the outer strike crossing its middle. It does not attempt to reproduce the precise slope of a manuscript cancellation. No TeX compilation or rendered-layout check was performed.

| Page file | Starting line before repair | Nested local deletions preserved |
|---|---|---|
| 15_scan142.tex | 10 | 2 |
| 15_scan147.tex | 48 | 0 |
| 15_scan148.tex | 18 | 6 |
| 15_scan163.tex | 13 | 4 |
| 15_scan163.tex | 19 | 1 |
| 15_scan177.tex | 3 | 0 |
| 15_scan177.tex | 9 | 0 |
| 15_scan179.tex | 2 | 6 |

The small TikZ fragments in math undersets on scans 173 and 177 use a text box instead of the paragraph-level figure wrapper; their drawn paths are unchanged.
