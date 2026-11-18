# Reproduction and scope

The mathematical certificates are in `finite_checks/code/` and
`arithmetic_notes/`; the immutable blind proof and comparison are in
`configuration/`. `CHECK_EVENTS.tsv` distinguishes full proof readings,
finite computations, and background carried without a completed check.

`code/assemble_paper.py` assembles the supplied checkpoint-03 source and
the new proof sections. It requires the separately supplied background ZIP,
extracted at `background/` beside this working tree. The assembled paper
is self-contained and can be compiled without those historical inputs.
`code/build_paper.py` builds it with LuaLaTeX and BibTeX, performs three
passes and records undefined references and every overfull box.

The supplied programs rerun by `finite_checks/code/rerun_carried.py`
remain in the user's original background ZIP. Copies that have exactly
the same SHA256 are mapped to that input by the checkpoint manifest.
New outputs, independent programs, and rerun logs are retained. Python
programs use Python 3, SymPy, and, where explicitly imported, python-flint;
C++ census programs use a C++17 compiler. Runtime binary wheels and
compiled executables can be regenerated and are not packaged.

The source documents opened for theorem checks are cited in the source
records and bibliography; they are not repackaged. TeX support files are
included for reproducible compilation in this workspace. Rendered pages
used for layout inspection are excluded as requested.
