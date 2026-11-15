#!/usr/bin/env python3
"""Assemble the post-freeze research notes; never writes transcription files.

The component records remain available for audit. The assembled notes file is
the authoritative reader-facing version. All source images and context inputs
are external to this deliverable directory and are not repackaged.
"""
from pathlib import Path
from datetime import datetime, timezone
import json,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def read(name):return (HERE/name).read_text()
def between(text,start,end=None):
    assert start in text,start
    part=text.split(start,1)[1]
    if end is not None:
        assert end in part,end
        part=part.split(end,1)[0]
    return part.strip()
def lower_note_headers(t):
    return re.sub(r'^## (?=[EL]\d{3}\.\d+)', '### ',t,flags=re.M)
def h2_to_h3(t):return re.sub(r'^## ', '### ',t,flags=re.M)

early=read('research_early.md')
late=read('research_late.md')
late_regs=read('research_late_registers.md')
typed=read('research_typed.md')
typed_regs=read('research_typed_registers.md')
root=read('research_root.md')
e_notes=early[early.index('## E146.1'):early.index('## Detailed derivation supporting E170.4–E170.5')].strip()
l_notes=late[late.index('## L172.1'):].strip()
t_notes=between(typed,'## Itemized notes')
assert not re.search(r'^## ',t_notes,re.M),'Move typed registers to their separate file before assembling'
root_notes=between(root,'## The requested conic–Azumaya–SO(3) bridge (B12)','## Primary bibliography and verification limits')
root_notes=root_notes.replace('## Literature comparisons, separated from manuscript claims\n\n','')
bibliography=between(root,'## Primary bibliography and verification limits')
root_scope=between(root,'## Evidence and scope','## The requested conic–Azumaya–SO(3) bridge (B12)')
pagination=between(typed_regs,'## Complete leaf and pagination register','## Titles, note headings, and internal references')
t_titles=between(typed_regs,'## Titles, note headings, and internal references','## Chronology of the typescript and its retrospective events')
t_chronology=between(typed_regs,'## Chronology of the typescript and its retrospective events','## Complete pair enumeration and later reassignment')
t_pairs=between(typed_regs,'## Complete pair enumeration and later reassignment','## Enumeration parameters, totals, and recomputability')
t_counts=between(typed_regs,'## Enumeration parameters, totals, and recomputability','## Context status and scope boundaries')
t_context=between(typed_regs,'## Context status and scope boundaries','## Self-checks, withdrawals, and later corrections')
t_checks=between(typed_regs,'## Self-checks, withdrawals, and later corrections')

# The standing self-check index includes the author's short words as well as
# the item reference. The full frozen source location remains in each item.
typed_quotes={}
for m in re.finditer(r'^### (T\d{3}\.\d+) [^\n]+\n(.*?)(?=^### |\Z)',t_notes,re.M|re.S):
    quote=re.search('“([^”]+)”',m.group(2))
    assert quote,m.group(1)
    typed_quotes[m.group(1)]=quote.group(1)
def quoted_check_row(m):
    note_id=m.group(1)
    return '| '+note_id+' |'+m.group(2)+' | “'+typed_quotes[note_id]+'” |'
t_checks=t_checks.replace('| Note ID | Scan/source lines | Kind | Point checked or revised |',
                         '| Note ID | Scan/source lines | Kind | Point checked or revised | Brief words |')
t_checks=t_checks.replace('|---|---|---|---|','|---|---|---|---|---|')
t_checks=re.sub(r'^\| (T\d{3}\.\d+) \|(.*?)\s*\|$',quoted_check_row,t_checks,flags=re.M)
e_proof=between(early,'## Detailed derivation supporting E170.4–E170.5','## Hua claim assessment restricted to scans 146–170')
hua=between(early,'## Hua claim assessment restricted to scans 146–170','## Self-flagged and completed checks in mathematical scans 146–170')
e_checks=between(early,'## Self-flagged and completed checks in mathematical scans 146–170','## Table and enumeration register for mathematical scans 146–170')
e_tables=between(early,'## Table and enumeration register for mathematical scans 146–170','## Titles and page counts in the assigned mathematical interval')
e_titles=between(early,'## Titles and page counts in the assigned mathematical interval')
l_checks=between(late_regs,'## Authorial checks, qualifications, questions, revisions, and unfinished computations','## Titles and page counts in this assigned subset')
l_tables=between(late_regs,'## Tables and enumerations','## Numerical recomputation report')
l_computation=between(late_regs,'## Numerical recomputation report','## Authorial checks, qualifications, questions, revisions, and unfinished computations')
l_titles=between(late_regs,'## Titles and page counts in this assigned subset')
chi=read('chi_groupoid_derivation.md').split('\n',1)[1].strip()

ids=[]
for src in [e_notes,l_notes,t_notes,root_notes]:
    ids+=re.findall(r'^#{2,3} ([ELT]\d{3}\.\d+|R\d{2})\b',src,re.M)
assert len(ids)==len(set(ids))
assert len(ids)==208,(len(ids),'Unexpected research item count')

intro=r'''# Research notes — Montpellier cote 84, scans 146–193

## 1. Scope, sources, and the distinction between reading and interpretation

The complete diplomatic transcription was frozen at **2026-11-15 11:56:21 UTC**, before the context archive was opened at **11:56:32 UTC**. All 48 scans were visually transcribed in one sequential stream and then audited against their images; the subsequent research analysis uses that frozen text. The main transcription contains no changes prompted by the context or by the calculations in these notes.

This report contains **208 individually identified items**: 38 early mathematical notes (E146.1–E170.5), 39 later mathematical notes (L172.1–L192.4), 118 notes on reused typescript (T147.1–T193.5), and 13 comparisons or editorial investigations (R01–R13). Source references identify the exact per-scan file; approximate line numbers refer to the frozen TeX rather than physical manuscript lines. Diplomatic doubt macros reproduced in quotations retain their editorial meaning: a `\unsure` is not automatically an uncertainty expressed by the author, and a cancelled claim is not live text.

The interpretation of a doubtful sign is explicitly conditional wherever a computation chooses one alternative. A missing hypothesis in these continuation pages is a proof obligation for this interval, not proof that the author never supplied it elsewhere. The named products \(E_1\wedge E_2\) and \(E_1\vee E_2\) are treated as the manuscript's operations; they are not silently replaced by ordinary exterior powers or direct sums.

The archive has two distinct textual layers. Claims about psychology, culture, medicine, or history in the reused typescript are recorded as the author's assertions, interpretations, reports, or revisions, not adopted as empirical results. “Own idea” in the mathematical/editorial items means a proposal or calculation made in this report, with its confidence and reason stated; the typed sequence's conceptual proposals are labelled authorial.

### Principal findings and their exact limits

- **A precise local algebraic result:** scans 172 and 192 give a quadratic-algebra product whose relation and discriminant formula check over the integer polynomial ring; its local formula matches Voight (2016, Construction 3.14) after an explicit generator shift (L172.1–L172.2, R05).
- **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
- **A positive all-χ local model:** the rank-one coordinate groupoid admits the multiplication \(a\star b=a\sigma+\tau b+\chi ab\), and an object is invertible precisely when \((\tau,\chi)=R\); this supports local parts of Hua's claim but does not prove its full global identification (R11–R13).
- **A separate sign obstruction:** for the explicitly fixed endpoint conventions, the pushout and pullback extension cocycles are opposite; a χ=0 elliptic-curve example prevents an isomorphism fixing both ends (E170.4–E170.5). This does not refute a sign-twisted interpretation or the whole ellipsized Hua entry.
- **No explicit B12 construction in the supplied interval:** no form of P¹, conic, rank-four central Azumaya algebra, or ternary-form/SO(3) identification is constructed here (R01–R04). The folder plan's B5 regular-polyhedron/congruence questions likewise receive no demonstrated step (R09).
- **Concrete archival counts and revisions:** the coefficient tables on scans 154 and 164 have 16 and 12 data cells respectively; the typed lists give \(6+6+2=14\) pairs and \(2^6=64\) sign sequences, while the eighteen groups and eighteen meditation leaves are separately reported counts (table registers below).
'''

context_intro=r'''## 2. Supplied context and the audit of its direct claim

Each numbered item has a context comparison. The actual searches, including negative and incidental lexical matches, are preserved in `records/context_queries_early.json`, `context_queries_late.json`, `context_queries_typed.json`, and `context_queries_root.json`. The searches cover all three supplied context files; they do not purport to search the absent source files merely named in the results register.

The principal direct entry is **Hua, findings register, 84-chi-trivialised-extension-product**, reproduced in `notes/RESULTS_STATE.md` under “Findings of another project.” Its status is an AI-produced conjectural candidate, with an intake saying that this cote's package was still awaited, not a mathematical referee verdict. The aggregate interval attached to it includes reused typed leaves, but those leaves do not contain the extension-product assertion; other cited mathematical ranges are outside this packet. The following verdicts are consequently restricted to the evidence supplied here and the explicitly identified local calculations.
'''

computation_intro=r'''## 10. Reproducible calculations and their scope

These scripts reproduce editorial checks, not missing manuscript text. They do not read images or alter transcription files. The symbolic calculations use Python 3 and SymPy (version 1.14.0 in this run); the typed counting script uses the Python standard library. Run the commands from the extracted package directory:

```bash
python records/early_formula_checks.py
python records/recompute_quadratic_algebras.py
python records/recompute_chi_groupoid.py
python records/recompute_typed_counts.py
```

Each writes its named JSON report beside the script. The early matrix calculation verifies a chosen interpretation of the parameters, including residuals rather than only successful equations; the later algebra calculation proves universal polynomial/matrix identities and then illustrates them with finite cases. A finite enumeration is never used here to infer a global categorical theorem. The local χ-groupoid laws and the extension-sign calculation received independent mathematical reviews recorded in `chi_groupoid_review_early.json` and `extension_sign_review_late.json`.

### 10.1. Later quadratic-algebra formula: finite illustrations of universal identities
'''

parts=[intro,root_scope,context_intro,hua,
 '### 2.1. Context boundaries for the reused typescript\n\n'+t_context,
 '## 3. Mathematical research items, scans 146–170\n\n'+lower_note_headers(e_notes),
 '## 4. Mathematical research items, scans 172–192\n\n'+lower_note_headers(l_notes),
 '## 5. Research items from every reused typed leaf\n\n'+t_notes,
 '## 6. B12, literature comparisons, and additional local investigations\n\n'+root_notes,
 '## 7. Standing question: which steps the author marks, checks, changes, or leaves unfinished\n\nEditorial uncertainty and authorial uncertainty are distinguished throughout these registers. Emphasis, an asserted qualification, a completed “OK,” and a literal question mark have different evidentiary force.\n\n### 7.1. Mathematical scans 146–170\n\n'+e_checks,
 '### 7.2. Mathematical scans 172–192\n\n'+l_checks,
 '### 7.3. Reused typescript: self-checks and dated revisions\n\n'+t_checks,
 '## 8. Standing question: title sheets, page counts, and pagination\n\n### 8.1. Mathematical leaves\n\n'+e_titles+'\n\n'+l_titles,
 '### 8.2. Complete reused-typescript pagination\n\n'+pagination,
 '### 8.3. Titles, note headings, and internal references\n\n'+t_titles,
 '### 8.4. Chronology and the limits of dating reused sheets\n\n'+t_chronology,
 '## 9. Tables and enumerations across the packet\n\n### 9.1. Mathematical scans 146–170\n\n'+e_tables,
 '### 9.2. Scans 172–192\n\n'+l_tables,
 '### 9.3. Complete typed pair enumeration and later reassignment\n\n'+t_pairs,
 '### 9.4. Typed enumeration parameters, totals, and recomputability\n\n'+t_counts,
 computation_intro,l_computation,
 '### 10.2. Detailed sign and splitting calculation supporting E170.4–E170.5\n\n'+e_proof,
 '### 10.3. Detailed local χ-groupoid calculation supporting R11–R13\n\n'+chi,
 '## 11. Primary bibliography and verification limits\n\n'+bibliography]
out='\n\n'.join(p.strip() for p in parts)+'\n'

# Quoted diplomatic macros are manuscript-source notation, not KaTeX macros.
# Keep those formula excerpts in code spans so Markdown viewers display the
# literal uncertainty state instead of raising an unknown-macro error.
def literal_diplomatic_math(m):
    body=m.group(1)
    if re.search(r'\\(?:unsure|deleted|inserted|margin|uline|uuline)\{',body):
        return '`'+body+'`'
    return m.group(0)
out=re.sub(r'\\\((.*?)\\\)',literal_diplomatic_math,out)

# Escape data pipes inside inline code/math in Markdown table rows only.
def table_safe(line):
    if not line.startswith('|'):return line
    def safe(m):return re.sub(r'(?<!\\)\|',r'\\|',m.group(0))
    line=re.sub(r'`[^`]*`',safe,line)
    line=re.sub(r'\\\(.*?\\\)',safe,line)
    return line
out='\n'.join(table_safe(line) for line in out.splitlines())+'\n'

dest=ROOT/'MPL_84_146-193_notes.md'
dest.write_text(out)
report={'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'notes':len(ids),'ids':ids,'words':len(out.split()),'file':dest.name,
        'inputs':['research_early.md','research_late.md','research_late_registers.md','research_typed.md','research_typed_registers.md','research_root.md','chi_groupoid_derivation.md'],
        'transcription_written':False}
(HERE/'notes_assembly.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='ids'},ensure_ascii=False))
