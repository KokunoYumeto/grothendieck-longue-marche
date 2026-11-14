# Reproducing this research return

The six requested deliverables are at the ZIP root. The paper source is
self-contained; compile it with LuaLaTeX, then BibTeX, then LuaLaTeX twice.
The LaTeX packages are standard TeX Live packages listed in its preamble.

All executed mathematical programs and their actual outputs are in code/.
They use Python 3 with numpy and sympy where imported. Run an individual
program from any directory; outputs are written beside the program.
The document-rendering utility additionally uses pypdf and pdftoppm.

The modular writing state and exact input manifest are in research/.
To resume the assembly utilities, make a working directory, copy research/*
into it, place code/ beside sections/, and create deliverable/. Copy the
six root deliverables into that deliverable/ directory. The scripts
assemble.py, build_pdf.py and build_registers.py then use the same layout
as the executed working state. The supplied inputs are identified by the
manifest; they are not duplicated in this ZIP.

Finite computations certify only the finite claims stated in their outputs.
The infinite mathematical assertions are proved in the paper. A source
marked verified was opened; that flag does not certify all of its proofs.
This return is INCOMPLETE, as explained in the report and each Open row.
