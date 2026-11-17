# Optional TeX integration

The requested combined file is an immutable LaTeX fragment, with no preamble. The supplied driver defines the requested editorial macros and loads the mathematical/TikZ packages. It is a reading/checking layout, not a page-size facsimile.

A post-freeze integration review noticed that the three decorated Roman section labels on scan 115 use `\overline` in text position. The driver makes `\overline` safe in text or math mode; **no page or combined transcription file has been changed**. A host document using different definitions should provide the same math-mode handling for those labels.

The driver has not been compiled here: both available TeX executables lack their format files and the required package sources. Balanced braces/environments and marker/delimiter checks passed, but that is not a full TeX compilation. Colours distinguish editorial states in this optional driver; the frozen macros retain the actual diplomatic distinctions.

With a complete TeX installation, run from the package root:

```sh
pdflatex -interaction=nonstopmode -output-directory=verification verification/compile_driver.tex
```
