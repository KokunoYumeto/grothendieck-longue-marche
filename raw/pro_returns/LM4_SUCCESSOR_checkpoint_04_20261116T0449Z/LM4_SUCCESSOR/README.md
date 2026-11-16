# LM4_SUCCESSOR

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

Status: INCOMPLETE, research in progress. Both main decisions remain unresolved. The report begins with one row for each requested task and lead; the register gives every numbered statement with its complete scoped claim.

## Reading the package

Start with LM4_SUCCESSOR_report.md, then LM4_SUCCESSOR_paper.pdf. The source paper includes sections under sections/, work_A/, work_CE/ and work_DE/. The component reports retain attempted approaches and exact remaining obstructions. records/continuation_state.md states the current research priorities and timing rule.

## Rebuilding

With a standard LuaLaTeX installation, run python3 code/build_paper.py. It regenerates the register and bibliography, builds with LuaLaTeX/BibTeX, and checks overflow and undefined references. Alternatively run latexmk -lualatex LM4_SUCCESSOR_paper.tex. In this session only, a private TeX environment can be selected with --env ../tex_runtime/env.json; that runtime is not required on a normally configured system.

## Reproducing computations

records/computation_inventory.csv lists every Python program and the location of its retained output. Exact certificates are in code/ and in the self-contained work_A/, work_CE/code/ and work_DE/ component directories. Run each from the directory indicated by its own docstring or path setup. Some checks use SymPy, NumPy, SciPy or Pillow; TeX/image helpers also use PyMuPDF. The finite checks supplement the proofs in the paper; their stated scope never replaces a full profinite existence argument.

The supplied background archive is not duplicated. Checkpoint exclusion manifests explain omitted attachment excerpts, auxiliary caches, component preview PDFs and full third-party article copies. Bibliography entries and source logs retain authoritative locations and exactly what was checked.
