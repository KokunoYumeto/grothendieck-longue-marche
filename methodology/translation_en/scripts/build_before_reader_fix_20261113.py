"""Compile the English of each package, and build the reader: the whole English translation as one book.

packages: each translation/packages/<package>_en.tex is compiled with LuaLaTeX in the transcription's check wrapper
  (answers/fixed/build/wrap.tex, byte for byte) as the second pass compiled the French: first as it is; if that
  fails, a copy after the reader build's mechanical LaTeX repairs (fix_tikzcd_in_macros.py,
  unwrap_gathered_diagrams.py, normalize_reader_text.py of longue_marche_pro_pilot_20261104, run as they are on the
  copy; content unchanged), the procedure of second_pass/work_close_20261112/retry_failed.py. Results:
  build/COMPILE.tsv (package, the French's status in CURRENT_TEXT_INDEX.tsv, the English's status, pages, first error).
reader: reader/LaLongueMarche_English.tex, one LaTeX file: the wrapper's preamble and macros, a title page, a note on
  the text and on how it was made, the credits and rights, the contents, then cote by cote each package (its English
  after the mechanical repairs, as the reader build of the French does); LuaLaTeX, two runs (--no-shell-escape).
usage: python -I -B build.py packages [PKG ...] | reader
"""
import concurrent.futures as cf
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
B = os.path.join(T.ROOT, "build")
REPAIRS = ("fix_tikzcd_in_macros.py", "unwrap_gathered_diagrams.py", "normalize_reader_text.py")
WRAP = T.read(T.WRAP)


def lualatex(d, name, halt=True, runs=1, timeout=1800):
    for _ in range(runs):
        args = ["lualatex", "--no-shell-escape", "-interaction=nonstopmode"] + (["-halt-on-error"] if halt else []) + \
               [name + ".tex"]
        subprocess.run(args, cwd=d, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       timeout=timeout)
    log = T.read(os.path.join(d, name + ".log")) if os.path.exists(os.path.join(d, name + ".log")) else ""
    m = re.search(r"Output written on .*?\((\d+) page", log)
    errs = re.findall(r"^! .*", log, re.M)
    return (int(m.group(1)) if m else 0), errs, log


def repaired_copy(src, dst):
    shutil.copyfile(src, dst)
    for s in REPAIRS:
        subprocess.run([sys.executable, "-I", "-B", os.path.join(T.LM, s), dst], capture_output=True)


def compile_package(pk):
    name = pk["package"]
    src = os.path.join(T.ROOT, "translation", "packages", name + "_en.tex")
    d = os.path.join(B, "packages", name)
    os.makedirs(d, exist_ok=True)
    body = os.path.join(d, "body.tex")
    shutil.copyfile(src, body)
    T.write(os.path.join(d, "en.tex"), WRAP.replace("BODYFILE", "body.tex"))
    pages, errs, log = lualatex(d, "en")
    if pages and not errs:
        status = "OK"
    else:
        repaired_copy(src, os.path.join(d, "body_repaired.tex"))
        T.write(os.path.join(d, "en_repaired.tex"), WRAP.replace("BODYFILE", "body_repaired.tex"))
        pages, errs, log = lualatex(d, "en_repaired")
        status = "OK after the reader build's mechanical LaTeX repairs" if pages and not errs else "FAIL"
    first = ""
    if status == "FAIL":
        m = re.search(r"^! .*(?:\n.*){0,3}", log, re.M)
        first = re.sub(r"\s+", " ", m.group(0))[:200] if m else "no PDF"
    for f in os.listdir(d):
        if f.endswith((".aux", ".pdf")):
            os.remove(os.path.join(d, f))
    return name, pk["compile_second_pass"], status, pages, first


def cmd_packages(want):
    pks = [p for p in T.manifest()["packages"]
           if os.path.exists(os.path.join(T.ROOT, "translation", "packages", p["package"] + "_en.tex"))
           and (not want or p["package"] in want)]
    rows = {}
    tsv = os.path.join(B, "COMPILE.tsv")
    if os.path.exists(tsv):
        for line in T.read(tsv).splitlines()[1:]:
            f = line.split("\t")
            rows[f[0]] = f
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for name, fr, st, pages, first in ex.map(compile_package, pks):
            rows[name] = [name, fr, st, str(pages), first]
            print(name, "|", st, pages, first, flush=True)
    order = [p["package"] for p in T.manifest()["packages"]]
    T.write(tsv, "package\tfrench_second_pass\tenglish\tpages\tfirst_error\n" +
            "".join("\t".join(rows[k]) + "\n" for k in order if k in rows))


TITLE = r"""\begin{titlepage}
\centering
{\Large Alexander Grothendieck\par}
\vspace{1.5em}
{\huge La Longue Marche à travers la théorie de Galois\par}
\vspace{0.8em}
{\large (1981)\par}
\vspace{2.5em}
{\LARGE English translation\par}
\vspace{1.5em}
{\large AI-translated by GPT-6.1 Sol (OpenAI, effort max)\\ from the AI-transcribed text checked by Claude Opus 5.5 (Anthropic)\par}
\vspace{2.5em}
{\large Cotes 140-1 to 140-4 of the Grothendieck archive, Université de Montpellier\\ 1,588 scans\par}
\vfill
{\large Translation of 12 November 2026\par}
\end{titlepage}
"""

NOTE = r"""\section*{A note on this text}
\addcontentsline{toc}{section}{A note on this text}

These are Alexander Grothendieck's research notes \emph{La Longue Marche à travers la théorie de Galois}, written in
1981, kept in the Grothendieck archive of the Université de Montpellier as cotes 140-1 (37 scans), 140-2 (575), 140-3
(696) and 140-4 (280). This book is an English translation of our diplomatic LaTeX transcription of the manuscript:
what he wrote, as he wrote it, with his deletions, insertions, marginal notes, underlining and the transcriber's
marks of doubt. Nothing has been completed, corrected or smoothed.

\subsection*{How to read it}
\begin{itemize}
\item {\footnotesize\textcolor{gray}{[scan $n$]}} marks the start of scan $n$ of the cote;
  {\footnotesize\textcolor{gray}{[p.~$n$]}} is his own page number.
\item Words he struck out are in {\color{gray}grey}; words he added between the lines are in {\color{teal}teal};
  readings the transcriber is not sure of are in {\color{blue}blue}, and where two readings are possible they are
  separated by a bar, A|B; {\textcolor{red}{[illeg.~$n$]}} stands for $n$ words that could not be read. Notes he wrote
  in the margin are set in the margin (in square brackets where they stand inside a formula or a box). His
  underlining is kept.
\item The formulas are the transcription's, character for character: his notation, including his own forms (Sl, Gl,
  Autext, the doubled $\Gamma$), is not normalized, and readings of a symbol that the scans do not settle are given as
  two readings.
\item His abbreviations (hom., isom., ss-groupe, tt, ssi, ext.\ \dots) are written out; his shorthand for
  ``même'', an m with a bar, is written out as ``same'', ``even'' or ``itself''. The comment lines of the LaTeX
  source (the transcriber's notes on where a passage stands on the sheet) are not printed.
\item Terms follow one glossary for the whole manuscript, built on Grothendieck's own English (\emph{Pursuing Stacks})
  and on the English \emph{Sketch of a Programme}: groupe à lacets is ``group with loops'' (not ``loop group''),
  action extérieure ``outer action'', multiplicité modulaire ``modular multiplicity'', topos ``topoi'' in the plural;
  spelling is American, as in his English.
\end{itemize}

\subsection*{How it was made}
\begin{itemize}
\item Transcription, first pass: GPT-6 Astra (OpenAI, ChatGPT Pro mode), one package of scans at a time, from
  contrast-enhanced images; one package (cote 140-2, scans 561--570) through the OpenAI API (GPT-6 Astra).
\item Transcription, second pass: Claude Opus 5.5 (Anthropic), every line checked against the archive images at full
  resolution and collated with the earlier transcriptions listed below where they cover the text.
\item Translation: GPT-6.1 Sol (OpenAI), reasoning effort max, through the OpenAI API, in units of a few scans, with
  the glossary's terms in every request.
\item Checks, by script, of every unit against its French: the formulas identical, the scan and page anchors in
  order, the marks of the transcription the same on every scan, every paragraph present and of comparable length, no
  French left, the glossary's terms used. Claude Opus 5.5 (Anthropic) wrote the prompts and the checks, made the fixes
  and built this book.
\end{itemize}

\subsection*{Sources and earlier work}
The scans: Université de Montpellier, Institut Montpelliérain Alexander Grothendieck, archives Grothendieck,
\texttt{https://grothendieck.umontpellier.fr/archives-grothendieck/}. Earlier transcriptions, consulted in the second
pass of the transcription as witnesses and not reproduced here: Mateo Carmona's edition of the first part, transcribed
from the typescript, and the typeset text deciphered and transcribed by Mateo Carmona with the collaboration of
Matthias Künzer (\texttt{agrothendieck.github.io}); the draft edition of the Centre for Grothendieckian Studies
(Grothendieck Institute, Mondovì), February 2026; the table of contents compiled by Grothendieck himself, as published
by the Grothendieck Circle.

\subsection*{Rights}
The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights,
in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain
under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.
"""


def cmd_reader():
    pre = WRAP[:WRAP.index("\\begin{document}")]
    pre = pre.replace("\\documentclass[11pt]{article}", "\\documentclass[11pt]{article}\n% The English reader of "
                      "La Longue Marche (translation_en_20261112/scripts/build.py); preamble and macros: the "
                      "transcription's check wrapper answers/fixed/build/wrap.tex")
    pre += "\\usepackage[hidelinks]{hyperref}\n\\setcounter{tocdepth}{2}\n\\raggedbottom\n"
    out = [pre, "\\begin{document}\n", TITLE, "\\tableofcontents\n\\clearpage\n", NOTE, "\\clearpage\n"]
    rd = os.path.join(B, "reader")
    os.makedirs(rd, exist_ok=True)
    cur = None
    man = T.manifest()
    missing = []
    for pk in man["packages"]:
        src = os.path.join(T.ROOT, "translation", "packages", pk["package"] + "_en.tex")
        if not os.path.exists(src):
            missing.append(pk["package"])
            continue
        if pk["cote"] != cur:
            cur = pk["cote"]
            n = sum(p["n_scans"] for p in man["packages"] if p["cote"] == cur)
            out.append("\\clearpage\n\\section*{Cote %s}\n\\addcontentsline{toc}{section}{Cote %s (%d scans)}\n" % (
                cur, cur, n))
        cp = os.path.join(rd, pk["package"] + ".tex")
        repaired_copy(src, cp)
        a, b = pk["scans"].split("-")
        head = "Scans %s--%s" % (a, b)
        out.append("\\subsection*{%s}\n\\addcontentsline{toc}{subsection}{%s}\n%% package %s\n" % (
            head, head, pk["package"]))
        out.append(T.read(cp).strip("\n") + "\n\n")
    out.append("\\end{document}\n")
    tex = os.path.join(T.ROOT, "reader", "LaLongueMarche_English.tex")
    T.write(tex, "".join(out))
    pages, errs, log = lualatex(os.path.join(T.ROOT, "reader"), "LaLongueMarche_English", halt=False, runs=2,
                                timeout=5400)
    und = len(re.findall(r"Reference .* undefined|There were undefined references", log))
    miss = len(re.findall(r"Missing character", log))
    over = len(re.findall(r"^Overfull \\hbox", log, re.M))
    print("reader: %d pages; LaTeX errors %d; undefined references %d; missing characters %d; overfull boxes %d; "
          "packages left out (not translated): %s" % (pages, len(errs), und, miss, over, missing or "none"))
    for e in errs[:20]:
        print("  ", e)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "packages":
        cmd_packages(set(a[1:]))
    elif a and a[0] == "reader":
        cmd_reader()
    else:
        print(__doc__)
