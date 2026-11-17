# LaTeX validation before freeze

The root reader compiled the combined fragment successfully with pdfTeX 1.40.26 and TeX Live 2025/dev. All 44 scan sections were processed. The temporary validation wrapper generated 45 output pages because its cote heading occupied one preliminary page; this does not add a manuscript scan.

Packages: amsmath, amssymb, tikz, tikz-cd, graphicx, T1 font encoding and Latin Modern. The final successful log contained no LaTeX errors, missing-character reports, overfull or underfull boxes. A private format and explicit font maps were needed because the container's system TeX database was incomplete.

The QA wrapper treated the editorial macros as content-preserving identity macros, with simple headings for cote and scan. This validates TeX syntax and diagram labels; it is not a styled critical-edition rendering. The requested deliverable remains a preamble-free fragment with the user's editorial macros.

Pre-freeze syntax repairs: 58 tikz-cd matrices received an explicit ampersand replacement and protected separators, and scan 027 received the missing closing math delimiter at the end of an insertion. These repairs did not change manuscript readings. The second visual audit, notation comparison, positioned doubts and inventory supply the separate visual record.

Infrastructure assistance was confined to the TeX runtime and structural validator. The root reader alone read the scans, transcribed and visually audited them, checked notation, and later read the research context.
