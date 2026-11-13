"""The readers' typesetting pass (13 Nov 2026, Claude Fable 5.2): nothing runs off the page, and every doubtful or
illegible reading links to its scan. Used by build.py (the English reader) and by lm_publish/rebuild_readers.py (the
four French readers); the texts themselves are not touched.

PREAMBLE goes at the end of the reader's preamble (after hyperref). It does five things, all at typesetting level:
1. Line breaking: \\tolerance 1000 and \\emergencystretch 3em, so that TeX breaks before an unbreakable formula
   instead of letting the line run into the margin.
2. Displays (LuaTeX callback post_mlist_to_hlist_filter): a display wider than the line (less its \\tag) is scaled
   down to the line width; one that would have to go below 70 % is turned onto its side (rotated 90 degrees, at most
   92 % of the text height) instead.
3. Lines of text (callback post_linebreak_filter): a line that is still too wide (a diagram, a table, a formula
   without a breakpoint) is scaled to the line width; below 70 % a line that holds only boxes (a diagram) is turned
   onto its side, a line with words is scaled all the same and listed.
4. Marginal notes: a note goes in the margin when it fits there (its widest line at most 18 % wider than the margin,
   at most three lines, so that a note beside the last line of a page stays above the page number); every other note is set in the text block, flush right, small, with a grey rule at its left,
   below the line it belongs to. In the 20 mm margin long notes ran off the foot and the side of the page.
5. \\unsure{...} and \\illegible{...} are links to the page of the archive's own viewer that shows the scan they
   stand on (grothendieck.umontpellier.fr, viewer.html?file=../<cote>.pdf#page=<scan>); so is the [scan n] mark.
   The archive file of a cote is one PDF whose page n is scan n (the files have the byte sizes of the PDFs the
   transcription was made from). The marks set a LuaTeX attribute; the link annotations are made when a page is
   shipped out, one for each run of marked material in a line or box.

Every change the pass makes is written to the log as a line "LMFIT ..." (kind, scale, input line); the TeX
"Overfull \\hbox" lines that remain in the log are the boxes the pass did not repair.

fit_report(log) reads those lines back. FIXES lists the per-place repairs (package, old, new, count, why), applied by
apply_fixes() to a build's copy of a package text.
"""
import re

ARCHIVE_VIEWER = "https://grothendieck.umontpellier.fr/web/viewer.html?file=../%s.pdf#page=%d"

PREAMBLE = r"""
% ---- typesetting pass of the readers (reader_typeset.py, 13 Nov 2026): fit to the page; links to the scans ----
\usepackage{luacode}
\newattribute\LMattr
\newcount\LMscanvalue
\tolerance=1000 \emergencystretch=3em \tracinglostchars=3
\begin{luacode*}
LMFIT = LMFIT or {}
local F = LMFIT
F.measure = false   -- a trial setting of a marginal note: record the widths, change nothing
F.maxw = 0          -- widest natural line of the trial (sp)
F.inpar = false
F.A = luatexbase.registernumber("LMattr")
F.n = {scaled_display = 0, rotated_display = 0, scaled_line = 0, rotated_line = 0, small_line = 0}
local HLIST, GLUE, KERN, WHATSIT, GLYPH = node.id("hlist"), node.id("glue"), node.id("kern"), node.id("whatsit"), node.id("glyph")
local SETMATRIX = node.subtype("pdf_setmatrix")
local MINSCALE = 0.70
local function note(kind, s, extra)
  F.n[kind] = (F.n[kind] or 0) + 1
  texio.write_nl("log", string.format("LMFIT %s scale %.3f at input line %d%s", kind, s, tex.inputlineno, extra or ""))
end
local function matrix(a, b, c, d)
  local n = node.new(WHATSIT, SETMATRIX)
  n.data = string.format("%.8f %.8f %.8f %.8f", a, b, c, d)
  return n
end
local function kern(w)
  local k = node.new(KERN, 1)
  k.kern = w
  return k
end
local function chain(...)
  local t = {...}
  for i = 1, #t do
    t[i].prev = t[i - 1]
    t[i].next = t[i + 1]
  end
  return t[1]
end
-- b: a box at its natural width. Returns a list that draws b scaled by s (about its reference point) and takes up
-- the scaled width; the matrix is undone at the same point, so colours that run on after the box are kept.
local function scaled(b, s)
  return chain(matrix(s, 0, 0, s), b, kern(-b.width), matrix(1 / s, 0, 0, 1 / s), kern(math.floor(s * b.width)))
end
-- b turned 90 degrees counter-clockwise and scaled by s: width s(h+d), height s*w
local function rotated(b, s, left)
  return chain(kern(left + math.floor(s * b.height)), matrix(0, s, -s, 0), b, kern(-b.width), matrix(0, -1 / s, 1 / s, 0),
               kern(math.floor(s * b.depth)))
end
local function rotscale(w)
  local room = 0.92 * tex.vsize
  if room < 100 * 65536 then room = 600 * 65536 end
  return math.min(1, room / w)
end

local function fit_lines(head)
  F.inpar = false
  for line in node.traverse_id(HLIST, head) do
    if line.subtype == 1 and line.head and line.width > 10 * 65536 then
      local nw = node.dimensions(line.head)
      if F.measure and nw > F.maxw then F.maxw = nw end
      if nw > line.width + 6554 then
        local shrink, inf, glyphs = 0, false, false
        for n in node.traverse(line.head) do
          if n.id == GLUE then
            if n.shrink_order > 0 and n.shrink ~= 0 then inf = true else shrink = shrink + n.shrink end
          elseif n.id == GLYPH then
            glyphs = true
          end
        end
        if not inf and nw - shrink > line.width + 6554 and not F.measure then
          local s = line.width / nw
          local b = node.hpack(line.head)
          node.unset_attribute(b, LMFIT.A)
          if s >= MINSCALE or glyphs then
            line.head = scaled(b, s)
            if s >= MINSCALE then note("scaled_line", s) else note("small_line", s) end
          else
            local r = rotscale(nw)
            local w2 = r * (b.height + b.depth)
            line.head = rotated(b, r, math.max(0, math.floor((line.width - w2) / 2)))
            line.height = math.floor(r * nw)
            line.depth = 0
            note("rotated_line", r)
          end
          line.glue_set, line.glue_sign, line.glue_order = 0, 0, 0
        end
      end
    end
  end
  return head
end

local prev = {}
local function fit_display(head, display_type, need_penalties)
  if not head then return head end
  if display_type ~= "display" then
    prev.text = true
    prev.w = node.dimensions(head)
    return head
  end
  local z = tex.displaywidth
  local w = node.dimensions(head)
  local q = 0
  local tag = token.get_macro("df@tag")
  if tag and tag ~= "" and prev.text then q = prev.w + tex.getmath("quad", "text") end
  prev.text = false
  if F.measure then
    if w + q > F.maxw then F.maxw = w + q end
    return head
  end
  if z < 10 * 65536 or w <= z - q + 6554 then return head end
  local shrink = 0
  for n in node.traverse_id(GLUE, head) do
    if n.shrink_order > 0 and n.shrink ~= 0 then return head end
    shrink = shrink + n.shrink
  end
  if w - shrink <= z - q then return head end
  local target = z - q
  if target / w < MINSCALE then target = z end   -- the tag goes on a line of its own
  local s = target / w
  local b = node.hpack(head)
  node.unset_attribute(b, LMFIT.A)
  local h, d = b.height, b.depth
  local nb
  if s >= MINSCALE then
    nb = node.hpack(scaled(b, s))
    nb.width, nb.height, nb.depth = math.floor(target) - 2, math.floor(s * h) + 1, math.floor(s * d) + 1
    note("scaled_display", s)
  else
    local r = rotscale(w)
    nb = node.hpack(rotated(b, r, 0))
    nb.width, nb.height, nb.depth = math.floor(r * (h + d)) + 1, math.floor(r * w) + 1, 0
    note("rotated_display", r)
  end
  return nb
end

luatexbase.add_to_callback("pre_linebreak_filter", function(head) F.inpar = true return head end, "lmfit.pre")
luatexbase.add_to_callback("post_linebreak_filter", fit_lines, "lmfit.lines")
luatexbase.add_to_callback("hpack_filter", function(head) F.inpar = false return head end, "lmfit.hpack")
luatexbase.add_to_callback("post_mlist_to_hlist_filter", fit_display, "lmfit.display")
-- TeX reports an overfull line while it breaks the paragraph, before the line is repaired above: such reports are
-- dropped; every other overfull box is reported in TeX's words.
luatexbase.add_to_callback("hpack_quality", function(incident, detail, head, first, last)
  if incident == "overfull" and not F.inpar and not F.measure then
    texio.write_nl("log", string.format("Overfull \\hbox (%.5fpt too wide) not repaired, at lines %d--%d", detail / 65536, first, last))
  end
end, "lmfit.quality")

-- Links to the scans. \unsure and \illegible set the attribute LMattr to (number of the cote) * 10000 + scan; when a
-- page is shipped out, every run of marked material inside one line or box becomes one link annotation. (A link made
-- with \href cannot hold a paragraph break and must start and end in the same box; these marks do neither.)
local A = luatexbase.registernumber("LMattr")
local VLIST, PENALTY, MATH = node.id("vlist"), node.id("penalty"), node.id("math")
local STARTLINK, ENDLINK, ACTION = node.subtype("pdf_start_link"), node.subtype("pdf_end_link"), node.subtype("pdf_action")
local inert = {[GLUE] = true, [KERN] = true, [PENALTY] = true, [WHATSIT] = true, [MATH] = true}
F.cotes = {}
F.links = 0
function F.at(cote, scan)
  local n = string.match(scan, "^%s*(%d+)")
  if cote == "" or not n then return end
  local k
  for i, c in ipairs(F.cotes) do if c == cote then k = i end end
  if not k then F.cotes[#F.cotes + 1] = cote k = #F.cotes end
  tex.setcount("global", "LMscanvalue", k * 10000 + tonumber(n))
end
local function url(v)
  return "https://grothendieck.umontpellier.fr/web/viewer.html?file=../" .. F.cotes[v // 10000] .. ".pdf#page=" .. (v % 10000)
end
local link_lists
local function link_runs(box)
  local n = box.head
  while n do
    local v = node.has_attribute(n, A)
    if v and v > 0 and not inert[n.id] then
      local last, m = n, n.next
      while m do
        if inert[m.id] then
        elseif node.has_attribute(m, A) == v then last = m
        else break end
        m = m.next
      end
      local w, h, d = node.dimensions(box.glue_set, box.glue_sign, box.glue_order, n, last.next)
      local s = node.new(WHATSIT, STARTLINK)
      s.width, s.height, s.depth = w, h, d
      local a = node.new(WHATSIT, ACTION)
      a.action_type = 3
      a.data = "/Subtype/Link/Border[0 0 0]/A<</Type/Action/S/URI/URI(" .. url(v) .. ")>>"
      s.action = a
      local e = node.new(WHATSIT, ENDLINK)
      box.head = node.insert_before(box.head, n, s)
      node.insert_after(box.head, last, e)
      F.links = F.links + 1
      n = e.next
    else
      if n.id == HLIST then link_runs(n) elseif n.id == VLIST then link_lists(n) end
      n = n.next
    end
  end
end
link_lists = function(box)
  for n in node.traverse(box.head) do
    if n.id == HLIST then link_runs(n) elseif n.id == VLIST then link_lists(n) end
  end
end
luatexbase.add_to_callback("pre_shipout_filter", function(box)
  if box.id == HLIST then link_runs(box) elseif box.id == VLIST then link_lists(box) end
  return true
end, "lmfit.links")
function F.summary()
  for k, v in pairs(F.n) do texio.write_nl("log", "LMFIT-SUMMARY " .. k .. " " .. v) end
  texio.write_nl("log", "LMFIT-SUMMARY links " .. F.links)
end
\end{luacode*}
\makeatletter
\AtEndDocument{\directlua{LMFIT.summary()}}
% a \simeq or \Gamma that stands outside a formula (a diagram label set as text) is set as mathematics: the text font
% has neither sign
\AtBeginDocument{\let\LMsimeq\simeq \protected\def\simeq{\ifmmode\LMsimeq\else$\LMsimeq$\fi}%
  \let\LMGamma\Gamma \protected\def\Gamma{\ifmmode\LMGamma\else$\LMGamma$\fi}}
% the page number and the placing of marginal notes are not part of a marked passage that runs over a page break
\output\expandafter{\expandafter\unsetattribute\expandafter\LMattr\the\output}
% -- links to the scans
\gdef\LMcotename{}
\newcommand\LMcote[1]{\gdef\LMcotename{#1}}
\newcommand\LMmark{\ifnum\LMscanvalue>0 \LMattr=\LMscanvalue\relax\fi}
\renewcommand{\scanpage}[1]{\directlua{LMFIT.at("\luaescapestring{\LMcotename}", "\luaescapestring{\detokenize{#1}}")}%
  \par\medskip\noindent{\footnotesize\LMmark\textcolor{gray}{[scan #1]}}\par}
\renewcommand{\unsure}[1]{{\color{blue}\LMmark #1}}
\renewcommand{\illegible}[1]{{\LMmark\textcolor{red}{[illeg.~#1]}}}
% -- marginal notes
\newsavebox\LMmbox
\newdimen\LMmw
\newdimen\LMmh
\newcommand\LMmarginstyle{\footnotesize\rightskip=0pt plus 2.5em\relax\parfillskip=0pt plus 1fil\relax\hyphenpenalty=50\relax
  \def\margin##1{{[##1]}}}
\newcommand\LMtrial[2]{% #1 a width, #2 the note: \LMmw its widest natural line, \LMmh its height
  \directlua{LMFIT.measure = true LMFIT.maxw = 0}%
  \setbox\LMmbox\vbox{\hsize=#1\relax\@parboxrestore\LMmarginstyle #2\par}%
  \directlua{LMFIT.measure = false tex.setdimen("LMmw", LMFIT.maxw)}%
  \LMmh=\dimexpr\ht\LMmbox+\dp\LMmbox\relax}
\newcommand\LMblock{\nobreak\vskip 3pt\moveright\@totalleftmargin\hbox to\linewidth{\hfill
  {\color{gray}\vrule width .6pt}\hskip 5pt\box\LMmbox}\vskip 3pt}
\newcommand\LMinblock[1]{%
  \LMtrial{.62\linewidth}{#1}%
  \ifdim\LMmw>.62\linewidth
    \ifdim\LMmw>\dimexpr\linewidth-6pt\relax \LMmw=\dimexpr\linewidth-6pt\relax \fi
  \else \advance\LMmw 0.5pt \fi
  \setbox\LMmbox\vbox{\hsize=\LMmw\@parboxrestore\LMmarginstyle #1\par}%
  \ifhmode \@bsphack\vadjust{\LMblock}\@esphack \else \LMblock \fi}
\newcommand\LMmargin[1]{\begingroup
  \LMtrial{\marginparwidth}{\rightskip=5pt plus 2.5em\relax #1}%
  \ifdim\LMmw>1.18\marginparwidth \LMinblock{#1}%
  \else\ifdim\LMmh>35pt \LMinblock{#1}%
  \else \marginpar{\LMmarginstyle\rightskip=5pt plus 2.5em\relax #1}%
  \fi\fi
  \endgroup}
\renewcommand{\margin}[1]{\ifinner{\footnotesize[#1]}\else\ifmmode{\footnotesize[#1]}\else\LMmargin{#1}\fi\fi}
\makeatother
% ---- end of the typesetting pass ----
"""

# Per-place repairs of the readers (never of the working texts): (package, old, new, count, why). A repair is applied
# to a build's copy of the package text when `old` occurs `count` times there; apply_fixes reports what it applied.
FIXES = [
]


def apply_fixes(package, text):
    done = []
    for pkg, old, new, count, why in FIXES:
        if pkg == package and text.count(old) == count:
            text = text.replace(old, new)
            done.append((pkg, old, new, count, why))
    return text, done


def fit_report(log):
    """counts of the pass's changes and of the overfull boxes left, from a reader's log"""
    kinds = {}
    for m in re.finditer(r"^LMFIT (\w+) scale ([\d.]+) at input line (\d+)", log, re.M):
        kinds.setdefault(m.group(1), []).append((float(m.group(2)), int(m.group(3))))
    left = [(float(m.group(1)), m.group(2)) for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\)([^\n]*)", log)]
    return kinds, left
