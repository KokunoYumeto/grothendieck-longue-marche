# B.62 component QA

The accepted formal source B_symplectic_refinements.tex is included in B_separability_review.tex. After bibliography generation and two final LuaLaTeX passes, the component has27 pages and218251 bytes, with zero overfull boxes and no LaTeX citation/reference warnings. Logs: B62_final_build_0.out and B62_final_build_1.out.

The three pages containing B.62 (23–25) were rasterized at90dpi and opened for visual inspection. The theorem, integral matrices, finite character, seven-word table, completion argument, margins, and citations are legible. The initial prose overflows of7.35712pt and13.9563pt were removed by ordinary sentence reflow.

The finite certificate was rerun after adding the explicit fixed-pair row check. All finite-group, primitive-kernel, character and seven-word checks passed. Root independently recomputed the whole finite calculation in the invariant-hyperplane basis: code/verify_B62_symplectic.py/.out. The formal statement does not infer anything about higher3-power levels or arbitrary finite quotients.
