# Initial official-mirror probes

This is a faithful recovery note from the observed tool results, not a
saved raw-console transcript. Before the successful documented runtime
producer, two bounded curl probes failed:

1. HEAD/follow probe to mirrors.ctan.org/macros/luatex/generic/luaotfload.zip
   returned the official307 redirect to mirror.math.princeton.edu and then
   timed out; observed exit28. No package payload was used.
2. Direct ctan.math.illinois.edu/macros/luatex/generic/luaotfload.zip probe
   timed out after the configured connection limit; observed exit28.

The actual runtime producer then downloaded all four packages successfully
from mirrors.mit.edu/CTAN. Every downloaded length and SHA is IDENTICAL to
the archived official_ctan_archives.json inputs. Its genuine command logs,
docstrip outputs, format output, and package metadata are retained beside
this note. No fake font loader or substitution package was introduced.

The initial pdfTeX fallback format attempt omitted --etex and genuinely
failed with 'LaTeX requires e-TeX'. Its full source/stdout/stderr/result
record remains. The separately named corrected --etex producer then
completed exit0 and generated the real pdflatex.fmt. Neither attempt
built or edited the main paper.
