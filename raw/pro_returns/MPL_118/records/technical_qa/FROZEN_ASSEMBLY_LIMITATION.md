# Frozen combined-file assembly limitation

After the transcription was frozen and the research context was opened, a mechanical check found two consecutive `\cotefile{118}` markers at the beginning of `MPL_118_transcription.tex`. The first page fragment already contained that marker, and the assembly script prepended another one. The individual page fragments are unaffected.

The duplicate marker is an assembly defect. It is deliberately preserved because the user expressly prohibited all transcription changes after opening the context. No corrected alternative transcription is substituted. The final verification must match every page and the combined file to `records/frozen_sha256.json`, including this defect.

Static checks of the page fragments do not establish the correctness of the combined-file opening, and they do not constitute rendered visual verification. The attempted LaTeX compilation could not run to completion because the available TeX runtime lacks the required format/packages/fonts; see `compile_attempt.txt` and `runtime_manifest.json`.
