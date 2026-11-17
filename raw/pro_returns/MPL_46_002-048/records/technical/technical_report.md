# Technical compilation and final static check

Final static-check time: 2026-11-17 11:42:21 UTC

## Concrete syntax findings

No concrete syntax error was detected.

## Scope and checks

All 42 page files were inspected solely as TeX source. The check covered balanced unescaped braces; nested begin/end environments; matching explicit math delimiters; paired left/right delimiters; approved diplomatic macro arguments; recognized control sequences; and balanced optional arguments and double-quoted labels for 136 TikZ-cd arrows.

The checker recognizes LaTeX text wrappers when checking explicit math nesting. It also checks that aligned/gathered/split environments occur within explicit math or a TikZ-cd cell. This is a static syntax check, not a proof that every TeX package will process or render the source successfully.

Combined fragment scan order: correct.
Combined fragment equals the documented ordered page concatenation: yes.
Concurrent page changes detected during check: none.

Combined SHA-256 at this check: aa8e2f5bf970597718314eefde3cdfe9d82a2855d08c06a469ecebfbfb1d7273.

## Compiler availability

The earlier compiler attempt remains valid as an environment finding: XeLaTeX, LuaLaTeX and pdfLaTeX binaries are present, but no LaTeX format, core source, document class, or required package files were discoverable. XeLaTeX stopped before manuscript input with 'I can't find the format file xelatex.fmt!'. The exact attempt is preserved in compiler_attempt.txt. Compilation was not repeated, and no TeX installation was attempted.

## Harness and limitations

compile_harness.tex defines the approved diplomatic macros and preserves their ambient math/text mode. It retokenizes diagram bodies for TikZ-cd ampersands inside macro arguments. The harness is disposable technical support; it does not alter the transcription.

No manuscript image or context archive was opened. No page, combined transcription, inventory, doubts file, core archive script, or progress log was modified. Visual accuracy, interpretation, completeness, and final rendered appearance are outside this technical check.

An earlier apparent \X command was a regex false positive: the source has valid row separators followed by X. No change was required.
