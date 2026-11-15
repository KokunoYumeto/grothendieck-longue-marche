# Root research record

- 2026-11-15 09:57 UTC: intake of prompt and archive.
- 10:01 UTC: assigned B, D and E in parallel; root owns A/C and integration.
- 10:03 UTC: read RESIDUE H.3 normalization proof; checking source-quotient conventions and residual stabilizers independently.
- Primary reference located: Mikala Ørsnes Jansen, arXiv:2308.09551; source and exact theorem check in progress.

## 10:30–10:50 UTC review and integration

- Reviewed E.8–E.10 extension pullback, mixed-braid quotient, deck descent, and the exact Hoshi–Mochizuki 6.13(ii) centralizer statement. Requested explicit deck descent computation; supplied by E.
- Read the entire D.8–D.10 projective proof and requested three local clarifications: Cartier pullback supports on a general slice, simultaneous valuation ideals at special triple points, and relative toroidal weak factorization. D supplied them.
- Added A.13, the genus-three two-component fixed-flag counterexample and ran code/a_flag_components.py. Added A.14 (ordinary criterion derivation) and A.15 (exact domain of normalization/contraction interchange).
- Opened and read Hatcher Appendix B Theorem B.1 and complete proof; replaced an unverified Earle–Eells citation with this checked proof. Added C.9 nonorientable/real quotient comparison and retained the exceptional groups explicitly.
- Inspected original cote150 scans39–40 and transcriptions39–42. The variable-extension family needs fixed base Sigma_d; recorded both subscript readings without finalizing handwriting.
- Built exact statement/readings/bibliography registers and a full coverage table. Corrected metadata-key aliases so every reading row has its complete mathematical assessment.
- The local TeX installation had executables but no generated formats/font maps. A system apt install could not acquire its lock under the existing user; no escalation was requested. Downloaded and extracted unmodified Debian texlive-luatex 2024.20250309-1 and fonts-texgyre 20180621-6 into an isolated runtime, generated lualatex.fmt and a font map from installed AMS/LM maps. The second compilation produced a61-page LuaLaTeX PDF.
- First complete text pass found3 overfull boxes >2pt (21.02907,10.02666,66.51782); split the lattice display, displayed the profinite generating tuple separately, and made the code filename breakable. A later build caught an in-progress B display bracket typo, corrected by B before the next pass.
- Current harder E.4 issue is the node-branch index-two character in A3/Z and the associated Kummer-type conjugacy equation; not treated as automatically solved by E.9.
