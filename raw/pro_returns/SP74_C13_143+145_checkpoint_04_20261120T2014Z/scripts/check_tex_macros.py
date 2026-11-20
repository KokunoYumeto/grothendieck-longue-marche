#!/usr/bin/env python3
"""Static control-sequence/environment check; never runs a TeX engine.

The lexer consumes each control word or control symbol as one token. In
particular, two backslashes form one linebreak token; the following E in
r"\\E" is ordinary text, not an invocation of a command named E.

Comments and literal payloads are masked without moving line/column positions.
The registry is explicit and package-scoped, not a permissive name-prefix test.
This is a name check, not a full expansion, catcode, key, option, or scope check.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Iterable


def names(value: str) -> set[str]:
    return set(value.split())


# An explicit catalog of public names, plus TeX primitives used by LaTeX.
# Names are stored without their initial backslash. No prefix is auto-approved.
CORE_COMMANDS = names(r"""
 documentclass usepackage RequirePackage LoadClass LoadClassWithOptions
 NeedsTeXFormat ProvidesClass ProvidesPackage ProvidesFile
 begin end newcommand renewcommand providecommand DeclareRobustCommand
 newenvironment renewenvironment newtheorem newcounter newlength newsavebox
 NewDocumentCommand RenewDocumentCommand ProvideDocumentCommand DeclareDocumentCommand
 NewDocumentEnvironment RenewDocumentEnvironment ProvideDocumentEnvironment DeclareDocumentEnvironment
 DeclareMathAlphabet DeclareSymbolFont DeclareSymbolFontAlphabet
 DeclareMathSymbol DeclareMathDelimiter DeclareMathAccent DeclareTextCommand
 DeclareTextSymbol DeclareTextAccent DeclareTextCompositeCommand
 def gdef edef xdef let futurelet long outer global protected newif
 newcount newdimen newskip newmuskip newbox newtoks newread newwrite
 if ifcat ifnum ifdim ifodd ifvmode ifhmode ifmmode ifinner ifvoid ifhbox ifvbox
 ifx ifeof iftrue iffalse ifcase ifdefined ifcsname unless else or fi
 csname endcsname expandafter noexpand relax the number romannumeral
 string meaning detokenize unexpanded expanded scantokens
 catcode mathcode lccode uccode sfcode delcode chardef mathchardef countdef
 dimendef skipdef muskipdef toksdef advance multiply divide afterassignment aftergroup
 begingroup endgroup bgroup egroup makeatletter makeatother ExplSyntaxOn ExplSyntaxOff
 cs_new:Npn cs_new:Nn cs_new:Npx cs_new:Npe cs_new_protected:Npn
 cs_set:Npn cs_set:Nn cs_set:Npx cs_set:Npe cs_set_protected:Npn
 cs_gset:Npn cs_gset:Nn cs_gset:Npx cs_gset:Npe cs_gset_protected:Npn
 input include includeonly endinput openin closein read openout closeout write
 immediate message errmessage errhelp typeout typein show showthe showbox showlists
 jobname time day month year hbadness vbadness tolerance pretolerance
 par indent noindent newline linebreak nolinebreak pagebreak nopagebreak newpage
 clearpage cleardoublepage smallskip medskip bigskip vspace hspace addvspace
 vskip hskip mskip kern mkern hfill vfill hfil vfil hss vss
 strut mathstrut null phantom hphantom vphantom smash llap rlap raise lower
 raisebox makebox mbox fbox framebox parbox minipage rule vrule hrule
 hbox vbox vtop unhbox unvbox copy box setbox lastbox unskip unkern unpenalty
 penalty insert vadjust leaders cleaders xleaders halign valign omit span cr crcr noalign
 font fontname fontdimen fontencoding fontfamily fontseries fontshape selectfont usefont
 fontsize tiny scriptsize footnotesize small normalsize large Large LARGE huge Huge
 normalfont rmfamily sffamily ttfamily mdseries bfseries upshape itshape slshape scshape
 textnormal textrm textsf texttt textmd textbf textup textit textsl textsc emph
 textsuperscript textsubscript underline textcircled textsuperscript
 textbackslash textasciicircum textasciitilde textbar textless textgreater
 textbraceleft textbraceright textunderscore textquotedbl textquotesingle
 textquoteleft textquoteright textquotedblleft textquotedblright
 textendash textemdash textellipsis textbullet textdagger textdaggerdbl
 copyright pounds dag ddag S P AA aa AE ae OE oe O o L l ss i j
 LaTeX TeX LaTeXe today verb verbatim
 label ref pageref cite nocite bibliography bibliographystyle bibitem
 footnote footnotemark footnotetext thanks marginpar marginparwidth
 setlength addtolength settowidth settoheight settodepth
 value setcounter addtocounter stepcounter refstepcounter
 arabic roman Roman alph Alph fnsymbol
 item list usecounter addcontentsline addtocontents contentsline
 tableofcontents listoffigures listoftables
 hline cline vline multicolumn shortstack tabularnewline arraystretch tabcolsep arraycolsep
 caption centering raggedright raggedleft raggedbottom flushbottom
 pagenumbering pagestyle thispagestyle markboth markright
 protect ensuremath mathchoice mathpalette mathversion
 mathrm mathnormal mathit mathbf mathsf mathtt mathcal boldmath unboldmath
 mathop mathord mathbin mathrel mathopen mathclose mathpunct mathinner
 displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits displaylimits
 left right middle big Big bigg Bigg bigl Bigl biggl Biggl bigr Bigr biggr Biggr
 over atop above overwithdelims atopwithdelims abovewithdelims
 frac sqrt root of overline underline overbrace underbrace
 hat check breve acute grave tilde bar vec dot ddot widehat widetilde
 alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda
 mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
 Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
 aleph hbar imath jmath ell wp Re Im partial infty prime emptyset nabla surd top bot
 angle triangle backslash forall exists neg lnot flat natural sharp clubsuit diamondsuit
 heartsuit spadesuit
 sum prod coprod int oint bigcap bigcup bigsqcup bigvee bigwedge biguplus
 bigodot bigotimes bigoplus
 pm mp times div ast star circ bullet cdot cap cup uplus sqcap sqcup vee wedge
 setminus wr diamond bigtriangleup bigtriangledown triangleleft triangleright
 lhd rhd unlhd unrhd oplus ominus otimes oslash odot dagger ddagger amalg
 leq le geq ge equiv prec succ sim preceq succeq simeq ll gg asymp
 subset supset approx subseteq supseteq cong sqsubset sqsupset sqsubseteq sqsupseteq
 neq ne doteq in ni owns notin vdash dashv models perp mid parallel bowtie smile frown
 propto not
 leftarrow gets rightarrow to leftrightarrow Leftarrow Rightarrow Leftrightarrow
 longleftarrow longrightarrow longleftrightarrow Longleftarrow Longrightarrow Longleftrightarrow
 mapsto longmapsto hookleftarrow hookrightarrow leftharpoonup leftharpoondown
 rightharpoonup rightharpoondown rightleftharpoons nearrow searrow swarrow nwarrow
 uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
 relbar Relbar joinrel lhook rhook
 lbrace rbrace lbrack rbrack langle rangle lfloor rfloor lceil rceil lvert rvert lVert rVert vert Vert
 ldots cdots vdots ddots dots
 arccos arcsin arctan arg cos cosh cot coth csc deg det dim exp gcd hom inf ker
 lg lim liminf limsup ln log max min Pr sec sin sinh sup tan tanh
 quad qquad thinspace negthinspace enspace enskip
 baselineskip lineskip lineskiplimit parskip parindent textwidth textheight linewidth
 columnwidth paperwidth paperheight topsep itemsep parsep partopsep
 kill a b c d H k r t u v
 """)
CORE_SYMBOLS = set("\\{}%#$&_ |,;:!/>\"'`^~=.()-+[]@") | {" "}
CORE_ENVIRONMENTS = names("""
 document math displaymath equation eqnarray eqnarray* array tabular tabular* tabbing
 center flushleft flushright quote quotation verse itemize enumerate description list
 trivlist minipage picture verbatim verbatim* thebibliography titlepage
 """)
CLASS_COMMANDS = {
    "article": names("part section subsection subsubsection paragraph subparagraph appendix title author date maketitle abstract figure table"),
    "report": names("part chapter section subsection subsubsection paragraph subparagraph appendix title author date maketitle abstract figure table"),
    "book": names("part chapter section subsection subsubsection paragraph subparagraph appendix title author date maketitle frontmatter mainmatter backmatter figure table"),
}
CLASS_ENVIRONMENTS = {key: names("abstract figure figure* table table*") for key in CLASS_COMMANDS}
CLASS_ENVIRONMENTS["book"].discard("abstract")

AMS_COMMANDS = names(r"""
 text textrm textsf texttt textnormal textup textit textsl textsc textmd textbf
 operatorname DeclareMathOperator operatornamewithlimits
 boldsymbol pmb dfrac tfrac cfrac binom dbinom tbinom genfrac
 overset underset sideset substack subarray
 xleftarrow xrightarrow stackrel
 dddot ddddot mathring
 boxed tag tagform@ notag nonumber intertext
 numberwithin eqref allowdisplaybreaks displaybreak raisetag
 hdotsfor shoveleft shoveright
 injlim projlim varinjlim varprojlim varliminf varlimsup
 lvert rvert lVert rVert
 dotsc dotsb dotsm dotsi dotso
 iint iiint iiiint idotsint
 alignat gathered aligned alignedat split cases
 """)
AMS_SYMBOLS = names(r"""
 mathbb mathfrak frak Bbb
 varnothing nexists eth digamma varkappa beth gimel daleth hslash Finv Game
 complement mho Bbbk circledS
 blacksquare square Box Diamond blacktriangle blacktriangledown blacktriangleleft
 blacktriangleright vartriangle triangledown lozenge blacklozenge circledcirc circledast
 circleddash boxplus boxminus boxtimes boxdot intercal divideontimes dotplus smallsetminus
 ltimes rtimes leftthreetimes rightthreetimes curlywedge curlyvee veebar barwedge doublebarwedge
 Cap Cup centerdot
 therefore because measuredangle sphericalangle
 leqq geqq leqslant geqslant eqslantless eqslantgtr lesssim gtrsim lessapprox gtrapprox
 approxeq backsim backsimeq risingdotseq fallingdotseq circeq triangleq bumpeq Bumpeq
 lessdot gtrdot lll ggg llless gggtr lessgtr gtrless lesseqgtr gtreqless lesseqqgtr gtreqqless
 preccurlyeq succcurlyeq curlyeqprec curlyeqsucc precsim succsim precapprox succapprox
 Subset Supset subseteqq supseteqq sqsubset sqsupset
 vartriangleright vartriangleleft trianglerighteq trianglelefteq
 vDash Vdash Vvdash smallsmile smallfrown shortmid shortparallel
 nless ngtr nleq ngeq nleqslant ngeqslant nleqq ngeqq lneq gneq lneqq gneqq
 lvertneqq gvertneqq lnsim gnsim lnapprox gnapprox
 nprec nsucc npreceq nsucceq precneqq succneqq precnsim succnsim precnapprox succnapprox
 nsim ncong nmid nparallel nshortmid nshortparallel
 nvdash nvDash nVdash nVDash ntriangleleft ntriangleright ntrianglelefteq ntrianglerighteq
 nsubseteq nsupseteq nsubseteqq nsupseteqq subsetneq supsetneq varsubsetneq varsupsetneq
 subsetneqq supsetneqq varsubsetneqq varsupsetneqq
 leftleftarrows rightrightarrows leftrightarrows rightleftarrows Lleftarrow Rrightarrow
 twoheadleftarrow twoheadrightarrow leftarrowtail rightarrowtail looparrowleft looparrowright
 leftrightharpoons rightleftharpoons curvearrowleft curvearrowright circlearrowleft circlearrowright
 Lsh Rsh upuparrows downdownarrows upharpoonleft upharpoonright downharpoonleft downharpoonright
 rightsquigarrow leftrightsquigarrow dashrightarrow dashleftarrow
 nleftarrow nrightarrow nleftrightarrow nLeftarrow nRightarrow nLeftrightarrow
 leadsto restriction multimap thickapprox thicksim
 """)
# Do not blanket-accept names such as mathbbm, llbracket or proof: their packages
# are not present in this project's preamble.
PACKAGE_COMMANDS = {
    "iftex": names("ifLuaTeX ifPDFTeX ifXeTeX ifpTeX ifupTeX ifVTeX ifTeX ifTUTeX RequirePDFTeX RequireLuaTeX RequireXeTeX"),
    "fontspec": names("fontspec setmainfont setsansfont setmonofont newfontfamily newfontface addfontfeatures addfontfeature defaultfontfeatures IfFontExistsTF IfFontFeatureActiveTF fontspec_if_fontspec_font:TF"),
    "fontenc": names("DeclareFontEncoding DeclareFontSubstitution DeclareFontFamily DeclareFontShape DeclareErrorFont DH dh TH th NG ng DJ dj guillemotleft guillemotright guilsinglleft guilsinglright"),
    "inputenc": names("inputencoding DeclareInputText DeclareInputMath UseRawInputEncoding"),
    "amsmath": AMS_COMMANDS,
    "amstext": names("text"),
    "amsopn": names("operatorname DeclareMathOperator"),
    "amsbsy": names("boldsymbol pmb"),
    "amssymb": AMS_SYMBOLS,
    "amsfonts": AMS_SYMBOLS,
    "mathrsfs": names("mathscr"),
    "tikz": names(r"""tikz tikzset tikzstyle usetikzlibrary usepgflibrary
       path draw fill filldraw shade shadedraw clip node coordinate matrix graph pic
       scope endscope scoped foreach
       pgfkeys pgfkeysalso pgfkeysvalueof pgfkeysgetvalue pgfkeyssetvalue
       pgfmathparse pgfmathresult pgfmathsetmacro pgfmathsetlengthmacro pgfmathtruncatemacro
       pgfmathsetcount pgfmathsetlength pgfmathrandominteger pgfmathrandomitem pgfmathprintnumber
       pgfpoint pgfpointxy pgfpointpolar pgfpointanchor pgfpointorigin
       pgfpathmoveto pgfpathlineto pgfpathcurveto pgfpathclose pgfpathrectangle pgfpathcircle
       pgfusepath pgfsetlinewidth pgfsetfillcolor pgfsetstrokecolor
       pgfsetfillopacity pgfsetstrokeopacity pgfsetdash pgfsetroundcap pgfsetbuttcap
       pgfdeclarelayer pgfsetlayers pgftransformshift pgftransformrotate pgftransformscale
       pgftransformxscale pgftransformyscale pgftext pgfnode pgfnodealias
       pgfextractx pgfextracty pgfgetlastxy pgfresetboundingbox pgfinterruptboundingbox
       pgfdeclaredecoration pgfdeclarearrow pgfsetarrows pgfsetarrowsstart pgfsetarrowsend
       pgfdeclareimage pgfuseimage pgfaliasimage pgfdeclarepatternformonly
       pgfdeclarehorizontalshading pgfdeclareverticalshading pgfdeclareradialshading
       tikzlastnode tikzparentnode tikzchildnode tikzleveldistance tikzsiblingdistance
       pgflinewidth pgfactualjobname
    """),
    "tikz-cd": names("arrow ar tikzcdset tikzcdmatrixname tikzcdrow tikzcdcolumn"),
    "enumitem": names("setlist setlistdepth newlist renewlist AddEnumerateCounter SetLabelAlign SetEnumitemKey SetEnumitemValue SetEnumitemSize"),
    "ulem": names("uline uuline uwave sout xout dashuline dotuline normalem ULforem ULon ULoff markoverwith useunder ULdepth ULthickness"),
    "xcolor": names("color textcolor colorbox fcolorbox pagecolor nopagecolor definecolor providecolor colorlet definecolorset providecolorset preparecolor preparecolorset definecolors selectcolormodel convertcolorspec extractcolorspec extractcolorspecs definecolorseries resetcolorseries blendcolors maskcolors"),
}
PACKAGE_ENVIRONMENTS = {
    "amsmath": names("equation* align align* alignat alignat* xalignat xalignat* xxalignat gather gather* multline multline* flalign flalign* split aligned alignedat gathered cases matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix smallmatrix subarray subequations"),
    "tikz": names("tikzpicture scope pgfpicture pgfscope pgfonlayer pgfinterruptboundingbox pgfinterruptpath pgfinterruptpicture"),
    "tikz-cd": names("tikzcd"),
}
# Public names exported by transitive dependencies are attributed to the loading
# package in the report; we do not recursively search arbitrary filesystem code.
DEPENDENCIES = {"amsmath": {"amstext", "amsopn", "amsbsy"}, "amssymb": {"amsfonts"}, "tikz-cd": {"tikz"}}
VERBATIM_ENVIRONMENTS = {"verbatim", "verbatim*"}


@dataclass(frozen=True)
class Token:
    name: str
    start: int
    end: int
    line: int
    column: int
    is_word: bool

    @property
    def command(self) -> str:
        return "\\" + self.name


@dataclass
class Scan:
    tokens: list[Token]
    masked: str
    comment_count: int
    literal_count: int
    warnings: list[dict]


def skip_space_comments(text: str, pos: int) -> int:
    while pos < len(text):
        if text[pos].isspace():
            pos += 1
        elif text[pos] == "%":
            end = text.find("\n", pos)
            pos = len(text) if end < 0 else end + 1
        else:
            break
    return pos


def read_group(text: str, pos: int, opening: str = "{", closing: str = "}"):
    pos = skip_space_comments(text, pos)
    if pos >= len(text) or text[pos] != opening:
        return None
    start = pos + 1
    depth = 1
    pos += 1
    while pos < len(text):
        char = text[pos]
        if char == "\\":
            # Consume a control symbol or the first character of a word. In
            # either case an escaped brace must not affect group depth.
            pos += 2
            continue
        if char == "%":
            end = text.find("\n", pos)
            pos = len(text) if end < 0 else end + 1
            continue
        if char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                return text[start:pos], pos + 1, start, pos
        pos += 1
    return None


def lex_tex(text: str) -> Scan:
    tokens: list[Token] = []
    masked = list(text)
    line_starts = [0] + [m.end() for m in re.finditer("\n", text)]
    comment_count = 0
    literal_count = 0
    warnings = []
    at_letter = False
    expl_letters = False
    pos = 0

    def location(offset: int):
        line = bisect_right(line_starts, offset)
        return line, offset - line_starts[line - 1] + 1

    def mask(start: int, end: int):
        for index in range(start, end):
            if masked[index] not in "\r\n":
                masked[index] = " "

    def letter(char: str):
        return (char.isascii() and char.isalpha()) or (at_letter and char == "@") or (expl_letters and char in "_:")

    def control_end(start: int):
        end = start + 1
        if end >= len(text):
            return end, "", False
        if letter(text[end]):
            end += 1
            while end < len(text) and letter(text[end]):
                end += 1
            return end, text[start + 1:end], True
        end += 1
        symbol = text[start + 1:end]
        return end, " " if symbol.isspace() else symbol, False

    while pos < len(text):
        if text[pos] == "%":
            end = text.find("\n", pos)
            end = len(text) if end < 0 else end
            mask(pos, end)
            comment_count += 1
            pos = end
            continue
        if text[pos] != "\\":
            pos += 1
            continue
        end, name, is_word = control_end(pos)
        line, column = location(pos)
        tokens.append(Token(name, pos, end, line, column, is_word))
        if not name:
            warnings.append(dict(line=line, column=column, reason="Dangling backslash at end of file."))
        pos = end
        if name == "makeatletter":
            at_letter = True
        elif name == "makeatother":
            at_letter = False
        elif name == "ExplSyntaxOn":
            expl_letters = True
        elif name == "ExplSyntaxOff":
            expl_letters = False
        elif name == "verb":
            literal_start = pos
            if pos < len(text) and text[pos] == "*":
                pos += 1
            if pos >= len(text) or text[pos] in "\r\n":
                warnings.append(dict(line=line, column=column, reason="Missing verb delimiter."))
                continue
            delimiter = text[pos]
            close = text.find(delimiter, pos + 1)
            newline = text.find("\n", pos + 1)
            if close < 0 or (newline >= 0 and newline < close):
                close = len(text) if newline < 0 else newline
                warnings.append(dict(line=line, column=column, reason="Unterminated verb payload on its line."))
                mask(literal_start, close)
                pos = close
            else:
                mask(literal_start, close + 1)
                pos = close + 1
            literal_count += 1
        elif name == "begin":
            group = read_group(text, pos)
            if group and group[0].strip() in VERBATIM_ENVIRONMENTS:
                environment = group[0].strip()
                pattern = re.compile(r"\\end\s*\{" + re.escape(environment) + r"\}")
                match = pattern.search(text, group[1])
                if match:
                    mask(group[1], match.start())
                    pos = match.start()  # The actual end token is still checked.
                else:
                    mask(group[1], len(text))
                    pos = len(text)
                    warnings.append(dict(line=line, column=column, reason=f"Unterminated {environment} environment."))
                literal_count += 1
        elif name == "detokenize":
            group = read_group(text, pos)
            if group:
                mask(group[2], group[3])
                pos = group[1]
                literal_count += 1
        elif name in {"string", "meaning", "ifdefined", "ifx"}:
            # These inspect tokens without invoking them. Undefined command
            # names in these positions are not undefined-control invocations.
            count = 2 if name == "ifx" else 1
            for _ in range(count):
                pos = skip_space_comments(text, pos)
                if pos >= len(text):
                    break
                target_end = control_end(pos)[0] if text[pos] == "\\" else pos + 1
                mask(pos, target_end)
                pos = target_end
                literal_count += 1
    return Scan(tokens, "".join(masked), comment_count, literal_count, warnings)


COMMAND_DECLARATIONS = names("""
 newcommand renewcommand providecommand DeclareRobustCommand
 NewDocumentCommand RenewDocumentCommand ProvideDocumentCommand DeclareDocumentCommand
 DeclareMathOperator DeclareMathAlphabet DeclareSymbolFontAlphabet DeclareMathSymbol
 DeclareMathDelimiter DeclareMathAccent DeclareTextCommand DeclareTextSymbol DeclareTextAccent
 DeclareTextCompositeCommand
 def gdef edef xdef let newlength newsavebox newcount newdimen newskip newmuskip
 newbox newtoks newread newwrite newif
 cs_new:Npn cs_new:Nn cs_new:Npx cs_new:Npe cs_new_protected:Npn
 cs_set:Npn cs_set:Nn cs_set:Npx cs_set:Npe cs_set_protected:Npn
 cs_gset:Npn cs_gset:Nn cs_gset:Npx cs_gset:Npe cs_gset_protected:Npn
 """)
ENVIRONMENT_DECLARATIONS = names("""
 newenvironment renewenvironment NewDocumentEnvironment RenewDocumentEnvironment
 ProvideDocumentEnvironment DeclareDocumentEnvironment newtheorem
 """)


def declarand(scan: Scan, token: Token):
    pos = skip_space_comments(scan.masked, token.end)
    if pos < len(scan.masked) and scan.masked[pos] == "*":
        pos = skip_space_comments(scan.masked, pos + 1)
    group = read_group(scan.masked, pos)
    if group:
        value = group[0].strip()
    else:
        match = re.match(r"\\([A-Za-z@_:]+|.)", scan.masked[pos:], re.S)
        value = match.group(0) if match else ""
    return value


def declarations(scan: Scan):
    commands, environments = set(), set()
    for token in scan.tokens:
        if token.name in COMMAND_DECLARATIONS:
            value = declarand(scan, token)
            match = re.fullmatch(r"\\([A-Za-z@_:]+|.)", value, re.S)
            if match:
                command = match.group(1)
                commands.add(command)
                if token.name == "newif" and command.startswith("if"):
                    commands.update({command[2:] + "true", command[2:] + "false"})
        elif token.name in ENVIRONMENT_DECLARATIONS:
            value = declarand(scan, token)
            if value and not any(c in value for c in "\\{}"):
                environments.add(value)
                commands.update({value, "end" + value})
        elif token.name == "newcounter":
            value = declarand(scan, token)
            if value and not any(c in value for c in "\\{}"):
                commands.update({"the" + value, "c@" + value, "p@" + value})
    return commands, environments


def package_and_class_names(scan: Scan):
    packages, classes = set(), set()
    for token in scan.tokens:
        target = packages if token.name in {"usepackage", "RequirePackage"} else classes if token.name in {"documentclass", "LoadClass", "LoadClassWithOptions"} else None
        if target is None:
            continue
        pos = skip_space_comments(scan.masked, token.end)
        optional = read_group(scan.masked, pos, "[", "]")
        if optional:
            pos = optional[1]
        group = read_group(scan.masked, pos)
        if group:
            target.update(part.strip() for part in group[0].split(",") if part.strip())
    return packages, classes


def registry(packages: Iterable[str], classes: Iterable[str]):
    command_sources = defaultdict(set)
    environment_sources = defaultdict(set)
    for name in CORE_COMMANDS | CORE_SYMBOLS:
        command_sources[name].add("LaTeX kernel / TeX primitives")
    for name in CORE_ENVIRONMENTS:
        environment_sources[name].add("LaTeX kernel")
    expanded_packages = set(packages)
    pending = list(expanded_packages)
    while pending:
        for dependency in DEPENDENCIES.get(pending.pop(), set()):
            if dependency not in expanded_packages:
                expanded_packages.add(dependency)
                pending.append(dependency)
    for class_name in classes:
        for name in CLASS_COMMANDS.get(class_name, set()):
            command_sources[name].add(f"document class {class_name}")
        for name in CLASS_ENVIRONMENTS.get(class_name, set()):
            environment_sources[name].add(f"document class {class_name}")
    for package in expanded_packages:
        for name in PACKAGE_COMMANDS.get(package, set()):
            command_sources[name].add(f"package {package}")
        for name in PACKAGE_ENVIRONMENTS.get(package, set()):
            environment_sources[name].add(f"package {package}")
    return command_sources, environment_sources, expanded_packages


def check_fragment(path: Path, commands, environments):
    raw = path.read_text(encoding="utf-8")
    scan = lex_tex(raw)
    local_commands, local_environments = declarations(scan)
    unknown_commands = []
    unknown_environments = []
    dynamic_environments = []
    environment_names = Counter()
    command_counts = Counter(token.name for token in scan.tokens)
    for token in scan.tokens:
        if token.name not in commands and token.name not in local_commands:
            unknown_commands.append(dict(command=token.command, line=token.line, column=token.column, token_kind="control_word" if token.is_word else "control_symbol", explanation="No declaration was found in the supplied preamble or this fragment, and this name is absent from the explicit registry for the document class and loaded packages. Review it; this static check does not prove that TeX would reject it."))
        if token.name not in {"begin", "end"}:
            continue
        group = read_group(scan.masked, token.end)
        environment = group[0].strip() if group else None
        if environment is None or any(char in environment for char in "\\{}#"):
            dynamic_environments.append(dict(command=token.command, line=token.line, column=token.column, argument=environment, explanation="Environment name is missing or nonliteral; not statically resolved."))
        else:
            environment_names[environment] += 1
            if environment not in environments and environment not in local_environments:
                unknown_environments.append(dict(environment=environment, command=token.command, line=token.line, column=token.column, explanation="Environment is neither declared by the preamble/fragment nor recognized in the active class/package registry."))
    return dict(file=str(path), sha256=hashlib.sha256(raw.encode("utf-8")).hexdigest(), control_sequence_tokens=len(scan.tokens), distinct_commands=len(command_counts), commands={"\\" + key: value for key, value in sorted(command_counts.items())}, environments=dict(sorted(environment_names.items())), local_command_definitions=sorted("\\" + name for name in local_commands), local_environment_definitions=sorted(local_environments), comments_masked=scan.comment_count, literal_payloads_masked=scan.literal_count, unknown_commands=unknown_commands, unknown_environments=unknown_environments, unresolved_environment_names=dynamic_environments, lexical_warnings=scan.warnings)


def self_test():
    def tokens(value):
        return [token.name for token in lex_tex(value).tokens]
    assert tokens(r"\\E") == ["\\"]
    assert tokens(r"\\\E") == ["\\", "E"]
    assert tokens("\\% \\alpha % \\Ghost\n\\beta") == ["%", "alpha", "beta"]
    assert tokens("\\\\% \\Ghost\n\\beta") == ["\\", "beta"]
    assert tokens(r"\verb|\Ghost%{x}| \alpha") == ["verb", "alpha"]
    assert tokens("\\begin{verbatim}\n\\Ghost% text\n\\end{verbatim}\\beta") == ["begin", "end", "beta"]
    assert tokens(r"\detokenize{\Ghost{a}\Other}\alpha") == ["detokenize", "alpha"]
    assert tokens(r"\string\Ghost \meaning\Other \ifdefined\Maybe \fi") == ["string", "meaning", "ifdefined", "fi"]
    assert tokens(r"\ifx\First\Second\fi") == ["ifx", "fi"]
    scan = lex_tex(r"\newcommand{\Custom}[1]{\text{#1}}\newenvironment{customenv}{}{}")
    assert declarations(scan) == ({"Custom", "customenv", "endcustomenv"}, {"customenv"})
    scan = lex_tex(r"\makeatletter\def\custom@macro{}\custom@macro\makeatother")
    assert "custom@macro" in declarations(scan)[0]
    scan = lex_tex(r"\ExplSyntaxOn\cs_new:Npn\custom_name:n#1{#1}\custom_name:n{a}\ExplSyntaxOff")
    assert "custom_name:n" in declarations(scan)[0]
    masked = lex_tex("a% comment\nb\\%c").masked
    assert len(masked) == len("a% comment\nb\\%c") and masked.count("\n") == 1
    return 13


def main():
    work = Path(__file__).resolve().parents[1]
    root = work.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages-dir", type=Path, default=work / "pages")
    parser.add_argument("--preamble", type=Path, action="append", help="Repeat for additional explicit preamble files; default is the supplied source PREAMBLE.tex.")
    parser.add_argument("--report", type=Path, default=work / "workflow" / "tex_macro_check.json")
    parser.add_argument("--self-test", action="store_true", help="Run the in-memory lexer regression cases before scanning the fragments.")
    parser.add_argument("--strict", action="store_true", help="Return exit status 1 when unknown command/environment names are found.")
    args = parser.parse_args()
    tests_run = self_test() if args.self_test else None
    preambles = args.preamble or [root / "source" / "SP74_C13_143+145_texts" / "PREAMBLE.tex"]
    packages, classes, custom_commands, custom_environments = set(), set(), set(), set()
    preamble_info = []
    for path in preambles:
        raw = path.read_text(encoding="utf-8")
        scan = lex_tex(raw)
        new_packages, new_classes = package_and_class_names(scan)
        defined_commands, defined_environments = declarations(scan)
        packages.update(new_packages)
        classes.update(new_classes)
        custom_commands.update(defined_commands)
        custom_environments.update(defined_environments)
        preamble_info.append(dict(file=str(path.resolve()), sha256=hashlib.sha256(raw.encode("utf-8")).hexdigest(), packages=sorted(new_packages), document_classes=sorted(new_classes), command_definitions=sorted("\\" + name for name in defined_commands), environment_definitions=sorted(defined_environments)))
    commands, environments, expanded_packages = registry(packages, classes)
    for name in custom_commands:
        commands[name].add("supplied preamble definition")
    for name in custom_environments:
        environments[name].add("supplied preamble definition")
    paths = sorted(args.pages_dir.glob("*.tex"))
    files = [check_fragment(path.resolve(), commands, environments) for path in paths]
    observed_commands = Counter()
    observed_environments = Counter()
    for file in files:
        observed_commands.update(file["commands"])
        observed_environments.update(file["environments"])
    unknown_command_occurrences = sum(len(file["unknown_commands"]) for file in files)
    unknown_environment_occurrences = sum(len(file["unknown_environments"]) for file in files)
    unknown_names = sorted({item["command"] for file in files for item in file["unknown_commands"]})
    unknown_env_names = sorted({item["environment"] for file in files for item in file["unknown_environments"]})
    report = dict(
        generated_at_utc=datetime.now(timezone.utc).isoformat(), checker=str(Path(__file__).resolve()),
        mode="static lexical name check; no TeX engine or compilation", pages_directory=str(args.pages_dir.resolve()),
        preambles=preamble_info, explicitly_loaded_packages=sorted(packages), packages_with_transitive_exports=sorted(expanded_packages),
        unrecognized_package_catalogs=sorted(package for package in expanded_packages if package not in PACKAGE_COMMANDS),
        unrecognized_class_catalogs=sorted(class_name for class_name in classes if class_name not in CLASS_COMMANDS),
        summary=dict(files_checked=len(files), control_sequence_tokens=sum(file["control_sequence_tokens"] for file in files), distinct_control_sequences=len(observed_commands), distinct_environments=len(observed_environments), unknown_command_occurrences=unknown_command_occurrences, unknown_environment_occurrences=unknown_environment_occurrences, unknown_command_names=unknown_names, unknown_environment_names=unknown_env_names, unresolved_environment_occurrences=sum(len(file["unresolved_environment_names"]) for file in files), lexical_warnings=sum(len(file["lexical_warnings"]) for file in files)),
        lexer_self_tests=dict(cases_run=tests_run, passed=True) if tests_run is not None else dict(cases_run=0, passed=None),
        observed_command_sources={command: sorted(commands.get(command[1:], {"fragment-local definition or unresolved"})) for command in sorted(observed_commands)},
        observed_environment_sources={environment: sorted(environments.get(environment, {"fragment-local definition or unresolved"})) for environment in sorted(observed_environments)},
        files=files,
        interpretation="No unrecognized command or environment names were found in this snapshot." if not unknown_names and not unknown_env_names else "The unknowns below need manual review against the intended macro/package definitions; no transcription has been changed.",
        limitations=[
            "The explicit registry covers standard LaTeX/TeX names and public names of this preamble's packages. It is a static catalog, not an exhaustive expansion of an installed TeX distribution. kpsewhich resolved no installed source files during preparation; no TeX engine was invoked.",
            "Conditional preamble branches are combined, so fontspec and the pdfLaTeX encoding packages are all recognized. No engine branch is executed.",
            "Definitions are recognized lexically, without expansion, conditional execution or group-scope validation. Custom catcode assignments other than makeatletter/makeatother and ExplSyntaxOn/Off are not interpreted.",
            "Unknown means absent from the active explicit registry and supplied declarations, not a proved undefined-control-sequence error. TikZ keys, arrow styles, argument arity, math correctness, layout and package option requirements are outside this check.",
            "Only pages/*.tex files present when this run read the directory are checked. SHA-256 hashes identify the exact read snapshot; later fragment additions or changes require rerunning the checker.",
            "Source images, readings, acceptance records and transcription files were not modified or audited."
        ]
    )
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"report": str(args.report.resolve()), **report["summary"], "self_tests_passed": tests_run}, ensure_ascii=False, indent=2))
    for file in files:
        for unknown in file["unknown_commands"] + file["unknown_environments"]:
            name = unknown.get("command", "") if "environment" not in unknown else "environment " + unknown["environment"]
            print(f"{file['file']}:{unknown['line']}:{unknown['column']}: {name}: {unknown['explanation']}")
    return 1 if args.strict and (unknown_command_occurrences or unknown_environment_occurrences) else 0


if __name__ == "__main__":
    raise SystemExit(main())
