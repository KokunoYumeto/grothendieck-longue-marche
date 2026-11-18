#!/usr/bin/env python3
"""Assemble finalized post-freeze contributions and actual check-event ledgers.

Only notes, method/status records, and CHECK_EVENTS.tsv are written.
"""
from pathlib import Path
from collections import Counter
import csv
import re

ROOT = Path(__file__).resolve().parent.parent
R = ROOT/'records'

def read(name):
    return (R/name).read_text()

def section(text, start, end=None):
    assert text.count(start) == 1, start
    out = text.split(start,1)[1]
    if end:
        assert end in out, end
        out = out.split(end,1)[0]
    return out.strip()

def notes(text, prefix):
    return list(re.finditer(r'^### ('+prefix+r'\d+) — ([^\n]+)\n(.*?)(?=^### |^## |\Z)', text, re.M|re.S))

bt,ec,sc,op,hc = [read(name) for name in
    ['research_bt.md','research_euler.md','research_schwarzian.md','research_opers.md','research_context_s20.md']]

counts = {p:len(notes(t,p)) for p,t in [('BT',bt),('EC',ec),('SC',sc),('OP',op)]}
counts['S20'] = len(re.findall(r'^### S20-\d+ —',hc,re.M))
counts['HC'] = len(notes(hc,'HC'))
assert counts == {'BT':69,'EC':60,'SC':118,'OP':49,'S20':5,'HC':14}, counts

intro = r'''# MPL_93_047-091 — Research notes

**Alexander Grothendieck, Montpellier archive, cote 93, scans 047–091.** This report accompanies the diplomatic transcription of all 42 supplied nonblank pages; blank scans 071, 079, and 085 were not supplied. It contains **315 itemized notes**, with separate documentary registers and proof records.

The transcription was completed, independently reread by the same primary reader against every page image, reconciled for notation, and frozen at **2026-11-18 10:49:51 UTC**. Context contents were first opened at **10:49:56 UTC**. All mathematical comparisons, source identifications, counterexamples, and proposed reading alternatives below are post-freeze work; they do not revise the transcription. The primary reader alone transcribed and visually audited the pages in ascending scan order. Research contributors subsequently used only the frozen text and inventory, the supplied context, and external sources.

The supplied earlier research and Michel Hua's AI-produced modernized reading are **credited leads, not established results**. The root read the complete supplied `notes/RESULTS_STATE.md` and `hua_project/93.modern.tex`; no proof-assistant files reported by that context were available or executed. Hua's page number is one less than the PDF scan number. References to his later pages identify his supplied interpretation, never an original manuscript image inspected here.

## Main findings and limits

- **The typed leaves have several sources.** Scans 047–048 have a direct published parallel in *Groupes de Barsotti-Tate et cristaux de Dieudonné*, pp. 118–120. The later crystalline supplements, the two cancelled Banach-analysis exercise sheets, and the six administrative sheets require separate identifications; authorship or a full title remains unverified where the evidence does not supply it [typed-sheet census; BT-S1; BT01–BT69; EC42–EC46].
- **The integral projective formula survives small characteristic in its divided-derivative form.** The independent three-jet computation verifies the integral cocycle and the factor (G=12G_0). The further rigidity proof is confined to the specified monic local algebras, with an explicit descent argument and hypotheses; it is not an unrestricted global classification theorem [SC16–SC26, SC110–SC115; proof record C1–C8].
- **Several literal formulas need qualifications or counterstatements.** The research notes retain the frozen signs, targets, and denominators while checking the wrong squared-coordinate test, failed epimorphisms, and the reused exercise counterexamples. Full universal-recipient and operator-classification assertions remain unproved where stated [BT29–BT36, BT45–BT53; SC23, SC41, SC51, SC69, SC103–SC109].
- **Characteristic two changes the geometric algebra.** Explicit matrices show why Killing duality, inner derivations, and unrestricted Lie-connection equivalences need the stated restrictions. The restricted first-jet triple on 091 is canonical under its hypotheses; full connections extending it form a quadratic-differential torsor, and their global existence is not established here [OP06–OP10, OP20, OP27, OP30–OP46; proof checks A–E].
- **Finite ordinary cohomology alone does not imply the initial fibration formula.** A locally compact telescope counterexample explains the later restriction on the base. The conical-space finiteness and uniqueness route remains conditional where its topology has not been proved; local and compact global triangulation claims are separately recorded [EC15–EC41, EC55–EC60].
- **The loop-space question has different answers after one and two deloopings.** The notes give an explicit reduced-quadratic-module example for a nonzero first Postnikov invariant after one delooping, using a cited realization theorem. The double-loop vanishing statement uses Arlettaz's theorem within its checked scope, and an ambient cohomology group can still be nonzero [EC47–EC54; EUL-S4–S5].
- **S20 is supported as a programme, with a missing concrete identification.** The pages sustain both projective-connection and crystalline strands. They do not identify a particular projective connection as Gauss–Manin for a specified family or compute its p-curvature; cotes 159 and 64 are not supplied. The wider Hua context supplies more specific comparison targets, all with their provenance retained [S20-01–S20-05, HC01–HC14].

## Report map and verification status

| Notes | Count | Current manuscript range and subject |
| --- | ---: | --- |
| BT01–BT69 | 69 | 047–054: Barsotti–Tate programme, supplements, and reused analysis exercises |
| EC01–EC60 | 60 | 055–070 and 083: Euler characteristics, conical ends, administrative sheets, covers, and the loop-space question |
| SC01–SC118 | 118 | 072–078, 080–082, 084: differential invariants and projective coordinates; later context is explicitly separated |
| OP01–OP49 | 49 | 086–091: projective bundles, Lie algebras, flags, and transverse connections |
| S20-01–S20-05; HC01–HC14 | 19 | Cross-cluster and later-context comparisons |

“Unproved claim” describes what is supplied on the sheet, not a claim that the statement is false or unknown today. “Own idea” identifies this run's proposed implication, counterexample, or comparison and includes confidence and a reason; it makes no novelty claim. A reading question stays a reading question after a mathematically expected formula is calculated. The notes' main commentaries are one to four sentences; metadata, context locations, and proof records are kept separate where needed.

`CHECK_EVENTS.tsv` records actual checks by statement ID, including imported background and refutations with a refined statement ID. “Carried as background without fault found” never means “proved here”; the outcome specifies an unresolved assertion where applicable. The executable calculations are symbolic or finite computations, not formal proof-assistant certificates. Detailed context-search registers are in `records/`; a keyword hit is a lead, and the note states the substantive relation.

## Typed-sheet census

There are **14 typed sheets: 6 `typed` and 8 `reused_typed`**. The other inventory classes are 25 `text` sheets and 3 `cover` sheets. A cancelled reused sheet remains `reused_typed`; cancellation is recorded separately. Handwritten corrections can be present without their writer being independently authenticated.

### Crystalline programme, supplements, and analysis sheets

'''

typed_bt = section(bt,'## Typed-sheet census and source identifications','## Individual notes')
typed_ec = section(ec,'## Typed-sheet census in this range','## Title sheets and written page counts in this range')
title_ec = section(ec,'## Title sheets and written page counts in this range','## Authorial self-flags, qualifications, and withdrawals')

titles = r'''

## Title sheets, internal headings, and written page counts

The following register distinguishes titles and printed internal pagination from later archive foliation. No authorial statement of a total number of manuscript pages was identified in this package; the number 42 is the supplied scan count, not a manuscript page-total claim. No `\mspage` value was introduced from archival foliation.

| Scan | Additional title or numbering evidence | Interpretation and limit |
| --- | --- | --- |
| 047–048 | Continuation of the Barsotti–Tate programme; 048 begins “3)” | Internal section numbering; published parallel is pp. 118–120, not a handwritten page count. |
| 049 | “Rabiots pour l'exposé précédent” | Supplement title; continues on 051 without a supplied page total. |
| 050 | “−36−”; “n°395” | Printed exercise-sheet identifiers; continuation of 052, not the archive's numbering or a total. |
| 052 | “−35−”; “n°393” | Printed exercise-sheet identifiers; the exercise proof continues on 050. |
| 053 | “Sur un théorème de Tate.” | Internal title; continuation on 054, with no written total. |
| 086–091 | “1.1. Données équivalentes”, “1.2.”, “1.3.”, “1.4 suite” | Section/subsection labels in a continuing projective-bundle development, not a cover title or page total. |

'''+title_ec+r'''

The unresolved cover heading on 069 is preserved in the frozen text as `\unsure{Thévenet|Théorème} / \unsure{Contre-Conière|Contre-Courant}`; it is not silently assigned a mathematical title. Scan 070 is an address-bearing reverse cover. Scan 084 continues the squared logarithmic-difference formula and a cancelled quotient fragment; it is **not** a title sheet.

## Steps the manuscript itself marks as unverified

The registers below retain the author's words or marks and point to the itemized discussion. Reader uncertainty by itself is not authorial doubt. A later check in this report does not erase the provisional status of the source. Separate cancelled claims and later restrictions are identified by both locations where the supplied text permits that comparison.

### Typed mathematical sheets and supplements

'''

flags_bt = section(bt,'## Author self-flags and local continuations','## Primary-source register and verification limits')
flags_ec = section(ec,'## Authorial self-flags, qualifications, and withdrawals','## Reproducible checks and proof details')

def cell(s):
    return s.replace('|',r'\|').replace('\n',' ')

flags_sc = ['| Scan | Author words or frozen mark | Item and follow-through |', '| --- | --- | --- |']
for m in notes(sc,'SC'):
    kind = re.search(r'\*\*Kind:\*\* ([^.]+)',m[3])[1]
    if kind not in {'self-flagged','withdrawn in the same text'}:
        continue
    scan = re.search(r'\*\*File/location:\*\* cote 93, scan ([^.]+)',m[3])[1]
    quote = re.search(r'\*\*Short quote:\*\* (.+?)\. \*\*Kind:',m[3])[1]
    flags_sc.append('| '+cell(scan)+' | '+cell(quote)+' | '+cell(m[1]+' — '+m[2])+' |')
flags_sc = '\n'.join(flags_sc)

flags_op = ['| Scan | Author words or frozen mark | Item and follow-through |', '| --- | --- | --- |']
for m in notes(op,'OP'):
    kind = re.search(r'\*\*Kind:\*\* ([^.]+)',m[3])[1]
    if kind not in {'self-flagged','withdrawn in the same text'}:
        continue
    q = re.search(r'\*\*Short quote \(frozen TeX, scan (\d+)\):\*\* `(.+?)`',m[3])
    scan = q[1]+'–090' if m[1]=='OP30' else q[1]
    flags_op.append('| '+scan+' | `'+cell(q[2])+'` | '+cell(m[1]+' — '+m[2])+' |')
flags_op = '\n'.join(flags_op)

bt_items = section(bt,'## Individual notes','## Author self-flags and local continuations')
ec_items = section(ec,'## Itemized research notes','## Typed-sheet census in this range')
sc_items = section(sc,'## Statement-level notes','## Separate author-unverified and withdrawn list')
op_items = op.split('### OP primary-source register',1)[0].strip()
op_items = op_items.split('\n',1)[1].strip()  # Drop contribution's heading only.

bt_scope = section(bt,'## Scope and evidentiary status','## Typed-sheet census and source identifications')
ec_scope = section(ec,'## Scope and context conventions','## Itemized research notes')
sc_scope = sc.split('## Statement-level notes',1)[0].split('\n',1)[1].strip()

report = intro+typed_bt+'\n\n### Reused administrative sheets\n\n'+typed_ec+titles+flags_bt
report += '\n\n### Euler-characteristic and loop-space leaves\n\n'+flags_ec
report += '\n\n### Differential-invariant leaves\n\n'+flags_sc
report += '\n\nQualifications and revisions, without an assertion of authorial doubt, are separately discussed in SC22, SC24, SC26, SC35, SC50, and SC103. Additional cancelled fragments, unfinished diagrams, and announced-but-unproved claims are itemized in SC01–SC118; the full documentary checklist is retained in `records/research_schwarzian.md`. Questions on 081 are treated individually.\n'
report += '\n### Projective-bundle leaves\n\n'+flags_op
report += '\n\nThe isolated “faux” on 087 has an unresolved attachment (OP22). The characteristic restriction on 090 qualifies the unrestricted inner-derivation assertion on 089 (OP30). Neither is generalized into a retraction of the entire programme.\n'
report += '\n## BT — Programme, supplements, and reused analysis\n\n'+bt_scope+'\n\n'+bt_items
report += '\n\n## EC — Euler characteristics, conical ends, and the loop-space question\n\n'+ec_scope+'\n\n'+ec_items
report += '\n\n## SC — Differential invariants and projective coordinates\n\n'+sc_scope+'\n\n'+sc_items
report += '\n\n## OP — Projective bundles and transverse connections\n\n'+op_items
report += '\n\n'+hc
report += '\n\n## Primary sources and exact use\n\n### BT sources\n\n'+section(bt,'## Primary-source register and verification limits')
report += '\n\n### Euler and homotopy sources\n\n'+section(ec,'## Primary-source register')
report += '\n\n### Differential-invariant sources\n\n'+section(sc,'## Primary-source register and actual reading scope')
report += '\n\n### Projective-bundle sources\n\n'+section(op,'### OP primary-source register')
report += r'''

## Supporting proof records and reproducibility

| Record | What was checked | Boundary |
| --- | --- | --- |
| `records/research_euler.md`, “Reproducible checks and proof details” | Telescope counterexample; explicit Postnikov cocycle and reduced quadratic module; budget arithmetic | The realization theorem and double-loop vanishing theorem remain cited external inputs. |
| `scripts/check_euler_postnikov.py`; `records/research_euler_computation.txt` | Exact finite group/cochain identities and numerical arithmetic | Finite algebra checks do not themselves construct a topological realization. |
| `records/research_schwarzian_proofs.md`, C1–C11 | Integral jet cocycle, signs and coefficients, local analytic ODE, Frobenius kernels, monic-model rigidity/descent, and conditional genus count | No universal operator classification, unrestricted global descent theorem, or historical novelty claim. |
| `records/schwarzian_checks.py`; `records/schwarzian_checks_output.json` | Exact symbolic identities and exhaustive small-ring diagnostics | Enumeration is supplementary to the written general proof. |
| `records/projective_proof_checks.md`, A–E | Lie brackets, characteristic-two counterexamples, Borel transitions, first jets, and restricted transverse data | Global full connections form a torsor if nonempty; their existence is not inferred from restricted-data uniqueness. |
| `scripts/check_projective_algebra.py`; `records/projective_algebra_certificate.json` | Exact matrix, derivation, Smith-form, and transition calculations | Symbolic computation, not proof-assistant certification. |
| `records/research_root_context_search.tsv`, `records/research_bt_context_search.tsv`, `records/research_euler_context_search.tsv`, `records/research_schwarzian_context_queries.tsv` | Actual per-note context searches | Lexical matches do not establish mathematical equivalence; exact comparisons are in each note. |
| `CHECK_EVENTS.tsv` | Merged statement, source, context, computation, and peer-review events | Types describe actual work; unresolved claims remain unresolved. |

The current report preserves all doubt markers and deleted material in the accompanying transcription. Its strongest negative conclusions are backed by explicit counterexamples; its positive conclusions state the category, characteristic, locality, and topology used. The separate doubts file remains the place to assess the visual confidence of a reading.
'''

# Avoid carrying stage-specific relative paths into ambiguous links: all references
# are plain archive-relative paths, and original contribution records remain intact.
ids = re.findall(r'^### ((?:BT|EC|SC|OP|HC)\d+|S20-\d+) —',report,re.M)
assert len(ids)==315 and len(set(ids))==315, Counter(ids)
(ROOT/'MPL_93_047-091_notes.md').write_text(report.rstrip()+'\n')

events = []
for name in ['research_bt_events.tsv','research_euler_events.tsv','research_schwarzian_events.tsv','research_root_events.tsv']:
    with (R/name).open(newline='') as f:
        rows = list(csv.DictReader(f,delimiter='\t'))
    for row in rows:
        original = row['who']
        if not original.startswith('GPT-6 Astra Pro;'):
            row['who'] = 'GPT-6 Astra Pro; effort inherited/not separately exposed; run MPL_93_047-091; '+original
        events.append(row)

peer = [
('ROOT-PEER-EC55-60','/root','Read the six final separated low-dimensional and cross-reference notes; conditional compact-link dependencies and unresolved global triangulation claims retained.'),
('ROOT-PEER-SC61-118','/root/research_bt','Read-only peer review of SC61–SC118 and C4–C5: independently checked connection sign, c_n coefficients, tensor powers, mixed cocycle, delta formulas, exponential identity and counterexamples under local analytic/nonvanishing hypotheses; SC93 mu0 refinement incorporated. No images, external SC source recheck, or C6–C8 review.'),
('ROOT-PEER-OP-A-E','/root/packaging_support','Read-only review of OP notes and proof A–E, especially relative-jet splitting, characteristic-2 quotient/dual example, and OP43–46. No substantive error found; fixed-i variation and global torsor wording refined by root.'),
('ROOT-PEER-S20-QUOTES','/root/research_bt','Read-only review independently matched all49 OP frozen-text quotations, checked the typed census against inventory, and reviewed S20/HC scope. Corrected Hua IV title, torsors-with-connection wording, and avoidance-of-2-and-3-division wording; HC06 algebra and HC14 provenance checked.'),
('ROOT-PEER-SC-INTEGRATION','/root/research_schwarzian','Reviewed assembled SC summaries, all118 IDs/event coverage, and authorial table. Distinguished six qualifications/revisions from explicit authorial uncertainty; Kind metadata corrected without mathematical or quotation changes.'),
]
for statement,agent,outcome in peer:
    events.append(dict(statement_id=statement,date='2026-11-18',who='GPT-6 Astra Pro; effort inherited/not separately exposed; run MPL_93_047-091; '+agent,
                       type='targeted proof check',outcome=outcome))

valid_types = {'targeted proof check','independent re-proof','computation or formal certificate',
               'used and rechecked in this run','carried as background without fault found',
               "refuted, with the refined statement's id"}
for row in events:
    # Earlier contributions sometimes supply the refined ID in the type itself.
    if row['type'].startswith('refuted') and row['type'] not in valid_types:
        row['outcome'] += ' Original event label: '+row['type']
        row['type'] = "refuted, with the refined statement's id"
    assert row['type'] in valid_types, row
covered = {row['statement_id'] for row in events}
assert set(ids) <= covered, set(ids)-covered
with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(events)

(R/'research_assembly_check.txt').write_text(
    f'Itemized note counts: {counts}\nTotal unique notes: {len(ids)}\n'
    f'Merged events: {len(events)}; all {len(ids)} notes have event coverage.\n'
    'Every event uses an allowed type; all who fields identify model, disclosed effort state, and run.\n'
    'No transcription file is written by this assembler.\n')
print(f'Assembled {len(ids)} notes and {len(events)} events.')
