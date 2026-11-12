#!/usr/bin/env python3
"""Assemble the supplied section sources, registers, and self-contained paper.

Run from any directory.  This is an editorial build, not a mathematical test.
Pandoc is required.  The resulting TeX uses ordinary LuaLaTeX packages and Type 1
Latin Modern fonts.  No source manuscript or external network is required.
"""
from pathlib import Path
from collections import Counter
import csv
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "sections"
ID = "LM3b_TEICHMULLER_PUSH"


def read(name):
    return (SEC / name).read_text()


def normalize(s):
    s = re.sub(
        r"(?m)^\*\*([A-H]\.\d+) — (Proved|Refuted|Known|Open)(?:, [^.\n]*)?\. (.*?)\*\* ?",
        lambda m: f"## {m[1]}. {m[2]} — {m[3].rstrip(chr(46))}\n\n", s)
    s = re.sub(r"(?m)^### ([A-H]\.\d+\.) ", r"## \1 ", s)
    s = re.sub(r"(?m)^(## [A-H]\.\d+\. (?:Proved|Refuted|Known|Open))"
               r"(?:, with reduction|, with complete reduction)?[:.] ",
               r"\1 — ", s)
    # Convert only the section-sign command; never alter commands such as Sigma.
    s = re.sub(r"\\S(?![A-Za-z])", "§", s)
    # Preserve the transcription macro without requiring the source packages.
    return s


ab = normalize(read("AB.md"))
ceh = normalize(read("CEH.md"))
dg = normalize(read("DG.md"))
c, eh = ceh.split("# E. ", 1)
e, h = ("# E. " + eh).split("# H.1. ", 1)
d, g = dg.split("# G. ", 1)
g = "# G. " + g
h = "# H. Congruence and higher categorical completion\n\n" + h.split("\n", 1)[1]
g8 = re.sub(r"\A# .*?\n", "", normalize(read("G008.md")), count=1)
h6 = re.sub(r"\A# .*?\n", "", normalize(read("Higher.md")), count=1)
intro = read("Introduction.md")
paper = intro + "\n\n\\clearpage\n\\tableofcontents\n\\clearpage\n\n" + \
    "\n\n".join([ab, c, d, e, normalize(read("F.md")), g, g8, h, h6])

# Metadata supplied by the independent work streams.
meta = {}
for filename in ("AB_results.csv", "CEH_statements.csv", "DG_results.csv"):
    with (SEC / filename).open(newline="") as fp:
        for row in csv.DictReader(fp):
            row = {
                ("manuscript_passages" if k.startswith("manuscript_passages")
                 else "depends_on_doubtful_reading"
                 if k.startswith("depends_on_doubtful_reading") else k): v
                for k, v in row.items()
            }
            meta[row["id"]] = row

for i in range(1, 8):
    row = meta.setdefault(f"G.{i}", {})
    if not row.get("manuscript_passages"):
        row["manuscript_passages"] = ("Auxiliary audit of modern manuscripts 019 and 031; connection to §34, folios 245-247, scans 483-488, and LM3 D.7/D.13; no verbatim 1981 counterpart")

f_deps = {
    1:"A.2; explicit tangential coefficient comparison",
    2:"F.1; Drinfeld1990 Proposition5.7; BarNatan1998 Theorem5; Brown2012 Theorem1.1; exact/modular matrices",
    3:"A.1; A.11; F.1; F.2; coprime fixed-point lifting",
    4:"A.4; F.1-F.3; finite-symmetry and full-profinite lifting obstruction",
    5:"Cyclotomic surjectivity; DolgushevLeLorenz2024 TheoremB.2 and RemarkB.3",
    6:"F.5; F.13; DolgushevLeLorenz2024 Theorem3.8; actual-versus-formal shadow distinction",
    7:"Integral binomial valuations; direct residue-ring enumeration",
    8:"F.7; Hochschild-Serre five-term sequence; exhaustive Q8 character certificate",
    9:"HainMatsumoto2003 Theorems7.3/8.4, Lemma8.5, Remark8.6; Brown2012; G.10",
    10:"BarNatan1998 Definition2.4, Claim2.6, Proposition5.3, Theorems4/5",
    11:"F.5; LM3 E.22 compactness criterion",
    12:"F.7-F.9; integral filtration and transgression obligations",
    13:"Defining GT automorphism formula; cyclotomic surjectivity; code/quaternion_shadow.py; direct Belyi-cover identities",
}
g_deps = {
    8:"OpenAI2026DD Proposition3.2; independent filtered rewriting proof",
    9:"G.8; integral deletion representation; residual-kernel induction",
    10:"Willwacher2026After Theorems1.1/2.2 and Proposition3.2; Brown2012 Theorem1.1; saturated reduction",
    11:"G.8-G.10; F.2; direct comparison of proof dependencies",
}
h_deps = {
    6:"LM3 F.1; Jansen2023 Construction3.18 and Theorems6.6/6.7; finite-congruence cofinality",
    7:"H.6; free/cyclic goodness; homotopy-pushout cochain calculation",
    8:"H.6-H.7; BarwickGlasmanHaine2020 Example2.6.4, Theorem2.7.4, Construction2.8.8, equation2.8.9, Proposition10.5.1, Corollary12.6.7",
    9:"H.8; decollage reconstruction; additional chain-stabilizer comparison",
}
for i in range(1,14):
    meta[f"F.{i}"] = {
        "depends_on": f_deps[i],
        "manuscript_passages":
            "§26; folios 163-166 (328 folio doubtful); scans 323-329; "
            "§27; folio 172 verso; scan 341; §§33bis-35; folios 242 verso-256; "
            "scans 479,487-488,496-505; auxiliary modern equation/finite-quotient calculation",
        "depends_on_doubtful_reading": "",
    }
for i in range(8,12):
    meta[f"G.{i}"] = {
        "depends_on": g_deps[i],
        "manuscript_passages":
            "Auxiliary audit of manuscript 008; connection to §§26-27, folios 163-172 verso, scans 323-341, "
            "and LM3 E.26; no verbatim counterpart of the modern proposition in 1981",
        "depends_on_doubtful_reading": "",
    }
for i in range(6,10):
    meta[f"H.{i}"] = {
        "depends_on": h_deps[i],
        "manuscript_passages":
            "§26; folios 165-166 (328 folio doubtful); scans 326-329; "
            "§29; folios 187 verso-188; scans 370-371; "
            "auxiliary higher-completion comparison attached to LM3 F.18",
        "depends_on_doubtful_reading": "",
    }

pat = re.compile(r"(?m)^## ([A-H]\.\d+)\. (Proved|Refuted|Known|Open)"
                 r"(?:, with complete reduction|, with reduction)?(?: — |: )(.*)$")
matches = list(pat.finditer(paper))
print("Detected", Counter(m[1][0] for m in matches))
assert len(matches) >= 85, ("Missing numbered claims", len(matches))
ids = [m[1] for m in matches]
assert len(ids) == len(set(ids)), "Duplicate statement identifiers"
rows = []
additions = []
for k, m in enumerate(matches):
    sid, status, title = m.groups()
    end = matches[k+1].start() if k+1 < len(matches) else len(paper)
    body = paper[m.end():end].strip()
    beforeproof = re.split(
        r"\n(?:\*\*(?:Proof|Reduction|The group|The finite|Status)|"
        r"\*(?:Proof|Attack)|# )", body, maxsplit=1)[0].strip()
    # For Open rows the first paragraph is the assertion; the full attack remains
    # in the paper, and the register's notes point to that proof obligation.
    if status == "Open" and sid != "B.11":
        beforeproof = beforeproof.split("\n\n", 1)[0]
    md = meta.get(sid, {})
    statement = md.get("statement", "")
    if not statement or statement.rstrip(".") == title.rstrip(".") or sid.startswith(("A.","B.","C.","E.","H.")):
        statement = title + ". " + beforeproof
    statement = re.sub(r"\s+", " ", statement).strip()
    locus = md.get("manuscript_passages", "")
    assert locus, ("Missing manuscript locus", sid)
    refs = sorted(set(re.findall(r"\b[A-H]\.\d+\b", body))-{sid})
    depends = md.get("depends_on") or "; ".join(refs)
    if depends == "See proof and named theorem inputs":
        depends = "; ".join(refs) + "; named primary theorem inputs in the proof"
    notes = md.get("notes","")
    if status == "Open":
        notes = (notes+" Exact remaining implication, attempted route and smallest undecided instance are stated in the numbered text.").strip()
    rows.append(dict(
        id=sid, statement=statement, status=status,
        where_proved=f"{ID}_paper.tex; statement {sid}",
        depends_on=depends, manuscript_passages=locus,
        depends_on_doubtful_reading=md.get("depends_on_doubtful_reading",""),
        notes=notes))
    additions.append((m.end(), "\n\n*Manuscript connection: " + locus +
                      ".*\n\n\\nopagebreak[4]\n"))
for pos, insertion in reversed(additions):
    paper = paper[:pos] + insertion + paper[pos:]

# Publish the exact requested column names.
columns = ["id","statement","status","where_proved","depends_on",
           "manuscript_passages (section; folio; scan)",
           "depends_on_doubtful_reading (scan, alternatives)","notes"]
with (ROOT/f"{ID}_results.csv").open("w",newline="") as fp:
    w=csv.DictWriter(fp,fieldnames=columns)
    w.writeheader()
    for row in rows:
        row[columns[5]]=row.pop("manuscript_passages")
        row[columns[6]]=row.pop("depends_on_doubtful_reading")
        w.writerow(row)

reading_rows=[]
for filename in ("AB_readings.csv","CEH_readings.csv","DG_readings.csv"):
    with (SEC/filename).open(newline="") as fp:
        for row in csv.reader(fp):
            if row and row[0] != "package":
                reading_rows.append(row)
reading_rows=list(dict.fromkeys(tuple(x) for x in reading_rows))
with (ROOT/f"{ID}_readings.csv").open("w",newline="") as fp:
    w=csv.writer(fp)
    w.writerow(["package","scan","the \\unsure or \\illegible place",
                "what the mathematics supports","how strongly"])
    w.writerows(reading_rows)

# Merge bibliography entries, retaining the most complete opened-source entry.
entries={}
for filename in ("AB_refs.bib","CEH_refs.bib","DG_refs.bib","Root_refs.bib"):
    for entry in re.findall(r"@\w+\{.*?^\}",read(filename),re.S|re.M):
        key=re.match(r"@\w+\{([^,]+),",entry)[1]
        if key not in entries or len(entry)>len(entries[key]):
            entries[key]=entry
# These are the same source with two stream-local keys.
if "BoggiZalesskii2019BC" in entries:
    entries.pop("BoggiZalesskii2019", None)
bibpath=ROOT/f"{ID}_references.bib"
bibpath.write_text("% All entries marked verified were opened at the cited loci.\n"
                   "% Verification does not imply a complete independent audit.\n\n"
                   +"\n\n".join(entries.values())+"\n")
csl=json.loads(subprocess.check_output(
    ["pandoc","-f","biblatex","-t","csljson",str(bibpath)],text=True))
(ROOT/"audit"/"references.json").write_text(json.dumps(csl,indent=2,ensure_ascii=False))

def initials(s):
    return " ".join(p[0]+"." for p in re.split(r"[\s-]+",s) if p)

def name(n):
    return n.get("literal") or n.get("family","") + \
        (", "+initials(n.get("given","")) if n.get("given") else "")

def author_string(e):
    ns=[name(x) for x in e.get("author",[])]
    if len(ns)<=1: return "".join(ns)
    return ", ".join(ns[:-1])+", & "+ns[-1]

def year(e):
    return str(e.get("issued",{}).get("date-parts",[["n.d."]])[0][0])

def title_clean(s):
    return re.sub(r"</?[^>]+>", "",s).replace(r"\(","$").replace(r"\)","$")

csl.sort(key=lambda e:(author_string(e).casefold(),year(e),e.get("title","").casefold()))
same=Counter((author_string(e),year(e)) for e in csl)
seen=Counter()
references=[]
for e in csl:
    a,y=author_string(e),year(e)
    pair=(a,y)
    if same[pair]>1:
        y+=chr(97+seen[pair]);seen[pair]+=1
    title=title_clean(e.get("title",""))
    title={
      "Brown2012":r"Mixed Tate motives over $\mathbb Z$",
      "Drinfeld1990":r"On quasitriangular quasi-Hopf algebras and on a group that is closely connected with $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$",
      "HainMatsumoto2003":r"Weighted completion of Galois groups and Galois actions on the fundamental group of $\mathbb P^1-\{0,1,\infty\}$",
    }.get(e["id"],title)
    container=title_clean(e.get("container-title",""))
    if container:
        rest=f"{title}. *{container}*"
        if e.get("volume"): rest+=f", *{e['volume']}*"
        if e.get("issue"): rest+=f"({e['issue']})"
        if e.get("page"): rest+=", "+e["page"].replace("--","–")
        rest+="."
    else:
        rest=f"*{title}*."
        if e.get("genre"): rest+=" "+e["genre"]+"."
        if e.get("publisher"): rest+=" "+e["publisher"]+"."
    url="https://doi.org/"+e["DOI"] if e.get("DOI") else e.get("URL","")
    if url: rest+=f" <{url}>."
    note=e.get("note","").strip()
    if note: rest+="\n\n*Source check:* "+title_clean(note)
    references.append(f"{a} ({y}). {rest}")
paper+="\n\n# References\n\n"+ "\n\n".join(references)+"\n"
(ROOT/f"{ID}_paper.md").write_text(paper)

tex=subprocess.check_output([
    "pandoc","-f","markdown+tex_math_single_backslash+raw_tex",
    "-t","latex","--ascii","--wrap=none",str(ROOT/f"{ID}_paper.md")
],text=True)
tex=tex.replace("§",r"\S{}")
# Add stable labels to every numbered heading, including headings that Pandoc
# wraps in texorpdfstring because they contain mathematics.
def label_heading(match):
    line=match[0]
    sid=re.search(r"\b([A-H])\.(\d+)\.",line)
    if not sid:
        return line
    return (r"\Needspace{11\baselineskip}"+"\n"+line+
            f"\\label{{stmt-{sid[1]}-{sid[2]}}}")
tex=re.sub(r"(?m)^\\subsection\{.*$",label_heading,tex)
assert tex.count(r"\label{stmt-")==len(rows)
# Keep the short mathematical tables together.  The introductory prose tables
# already fit their designated pages and are left to longtable's own layout.
start=tex.index(r"\section{A.")
def reserve_table_space(match):
    block=match[0]
    body=block.split(r"\endlastfoot",1)[-1]
    count=len(re.findall(r"\\\\\s*\n",body))
    if 0<count<=20:
        return f"\\Needspace{{{count+6}\\baselineskip}}\n"+block
    return block
tex=tex[:start]+re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}",
                      reserve_table_space,tex[start:],flags=re.S)
header=r"""\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools}
\usepackage[margin=22mm,headheight=14pt]{geometry}
\usepackage{array,booktabs,longtable}
\usepackage{graphicx}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{xurl}
\usepackage{hyperref}
\usepackage{bookmark}
\usepackage{fancyhdr}
\usepackage{etoolbox}
\usepackage{needspace}
\hypersetup{colorlinks=true,linkcolor=blue!40!black,urlcolor=blue!40!black,
  pdftitle={LM3b Teichmuller Push: normalizers, fillings and arithmetic recognition},
  pdfauthor={AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)}}
\urlstyle{same}
\setcounter{secnumdepth}{-2}
\setcounter{tocdepth}{1}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt plus 1pt minus 1pt}
\setlength{\emergencystretch}{2em}
\setlength{\LTpre}{6pt}
\setlength{\LTpost}{6pt}
\renewcommand{\arraystretch}{1.13}
\newcommand{\tightlist}{\setlength{\itemsep}{1pt}\setlength{\parskip}{0pt}}
\newcommand{\unsure}[1]{\langle\text{\normalfont\ttfamily #1}\rangle}
\newcommand{\ad}{\operatorname{ad}}
\newcommand{\Out}{\operatorname{Out}}
\newcommand{\Aut}{\operatorname{Aut}}
\newcommand{\Gal}{\operatorname{Gal}}
\newcommand{\Inn}{\operatorname{Inn}}
\newcommand{\Lie}{\operatorname{Lie}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small LM3b: Teichmüller tower}
\fancyhead[R]{\small 11 November 2026}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\AtBeginEnvironment{longtable}{\small}
\makeatletter
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}{-2.8ex plus -1ex minus -.2ex}{1.2ex plus .2ex}{\normalfont\large\bfseries\raggedright}}
\makeatother
\pdfextension mapfile{}
\pdfextension mapfile{+lm.map}
\pdfextension mapfile{+cm.map}
\pdfextension mapfile{+symbols.map}
\pdfextension mapfile{+euler.map}
\begin{document}
\begin{center}
{\Large\bfseries The Teichmüller tower: normalizers, fillings,\\
arithmetic recognition, and completion}\\[5pt]
{\small LM3b\_TEICHMULLER\_PUSH \quad | \quad 11 November 2026}
\end{center}
"""
header=header.replace("Teichmüller",r'Teichm\"uller')
(ROOT/f"{ID}_paper.tex").write_text(header+tex+"\n\\end{document}\n")
stats={"statements":len(rows),"statuses":dict(Counter(r["status"] for r in rows)),
       "readings":len(reading_rows),"references":len(csl),
       "statement_ids":ids}
(ROOT/"audit"/"assembly.json").write_text(json.dumps(stats,indent=2))
print(json.dumps({k:v for k,v in stats.items() if k!="statement_ids"},indent=2))
