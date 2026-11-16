#!/usr/bin/env python3
"""Assemble post-freeze research notes; never reads or writes transcription text."""
from pathlib import Path
import re
import json

BASE = Path(__file__).resolve().parents[1]
REC = BASE / 'records'

def read(name):
    return (REC / name).read_text(encoding='utf-8')

def body(text):
    return text.split('\n', 1)[1].lstrip()

def between(text, start, stop=None):
    a = text.index(start)
    b = text.index(stop, a) if stop else len(text)
    return text[a:b].strip() + '\n'

def demote(text, levels=1):
    return re.sub(r'^(#{1,5})(?= )', lambda m: '#' * min(6, len(m[1]) + levels), text, flags=re.M)

root = read('research_root_notes.md')
guide = '''## Reading guide

The itemized manuscript notes are **C106-01–20**, **RQ-01–14**, **O1–O4**, **R1–R11**, **H01–H13**, **SP-L01–07**, and **R106-V1**. Each keeps a short substantive note separate from provenance and, where needed, a longer verification appendix. Standing registers give the manuscript's own unverified steps and its title/count evidence. The 255-row dossier concordance and 15-entry NEW_RESULTS concordance are complete comparison registers, with supplied statements and statuses preserved.

| Section | Contents |
|---|---|
| A–B | Cote 106 itemized notes and post-freeze reading questions |
| C–D | Every explicit self-flag recorded; titles, counts, numbering, reused-stock dates |
| E–F | Main findings; conditional modern verification of the short-fraction and section claims |
| G | Relative Hom, copowers, external-product failures, and exact companion parallels |
| H | All 15 NEW_RESULTS records; sequential colimits, relative-square criterion, counterexamples, verification appendices, and primary references |
| I | Bounded first-appearance leads for strong W(7), total asphericity, and relative Theorem A |
| J | All 255 dossier statements, including exact supplied status/locator and per-row absence or relation |
| K | Completion, validation limits, and recovery-record guide |

The longer proofs in F and H are explicitly our conditional verifications or applications of known results; the short manuscript notes remain one to four sentences. Appendix letters in **H** are local to that section. The reference-comparison entries **C1–C11** in G are a source index used by O1–O4 and R1–R11, not a second set of manuscript claims.

'''
root = root.replace('## A. Cote 106:', guide + '## A. Cote 106:', 1)

fraction = body(read('research_106_literature_review.md'))
fraction = re.sub(r'^This review used only.*?\n\n', '', fraction, flags=re.M)
fraction = fraction.replace('Root’s separate verification', 'The principal reader’s separate verification')
fraction = fraction.replace('Brown’s original article was checked separately by root, not independently reopened in this review: ', '')
fraction = fraction.replace('Root records a December', 'The primary PDF has a December')
fraction = re.sub(r'^Web retrievals available to root.*$', 'The proof in §§3–5 is an explicit deduction under the stated axioms, independent of the unreviewed companion runs.', fraction, flags=re.M)
fraction = fraction.replace('**Location:** 106/012–016', '**Kind:** own idea / conditional verification of a standard consequence. **Location:** 106/012–016', 1)

br = read('research_bisite_residue.md')
relative = between(br, '## Own audit observations: ordinary external products')
relative = relative.replace('**Kind:** own audit observation;', '**Kind:** own idea / audit observation;')
kind_prefixes = {
    'cancelled formulation and unfinished check.': 'withdrawn in the same text (cancelled 107/003, revised at 107/004); unfinished check.',
    'active ordinary definition and evaluation argument.': 'unpursued implication / contextual link from an ordinary definition and evaluation argument.',
    'active generalization with explicit test for representability.': 'unpursued implication / contextual link from an ordinary generalization and representability test.',
    'conditional closure assertion.': 'unproved claim / conditional closure assertion.',
    'representability warning and asserted necessary-and-sufficient condition.': 'unproved claim / representability warning and asserted necessary-and-sufficient condition.',
    'ordinary copower construction and adjunction assertion.': 'unpursued implication / contextual link from the ordinary copower construction and adjunction.',
    'recapitulation of ordinary evaluation and external-product notation.': 'unpursued implication / contextual link from the recapitulated ordinary evaluation and external product.',
    'asserted proposition and corollary with a failed continuity argument.': 'unproved claim / asserted proposition and corollary with a failed continuity argument.',
    'unfinished simplicial matching-object scratch work.': 'self-flagged / unfinished simplicial matching-object scratch work.',
    'valid ordinary corollary followed by invalid mixed specialization.': 'unproved claim / invalid mixed specialization following a valid ordinary corollary.',
    'ordinary universal-extension and opposition calculation with a cancelled proposal.': 'withdrawn in the same text / cancelled proposal within an ordinary universal-extension and opposition calculation.'
}
for a,b in kind_prefixes.items():
    assert relative.count('**Kind:** ' + a) == 1, a
    relative = relative.replace('**Kind:** ' + a, '**Kind:** ' + b)

hom = body(read('research_new_and_homotopy.md'))
new_data = json.loads(read('research_new_and_homotopy_mapping.json'))
new_exact = ['### D.1 Exact supplied NEW_RESULTS statements and declared connections', '',
    'These are the supplied result statements and “Bears on” cells, quoted for comparison only; their truth and checking status remain those specified in the preceding metadata table and the 15-entry concordance.', '',
    '| NEW ID | Exact supplied result statement | Exact supplied “Bears on” cell |',
    '|---|---|---|']
for row in new_data['numbered_results']:
    cells = [row['id'], row['result'], row['bears_on']]
    new_exact.append('| ' + ' | '.join(c.replace('|', r'\|').replace('\n', '<br>') for c in cells) + ' |')
hom = hom.replace('## Appendix E. Additional verifications for H12–H13', '\n'.join(new_exact) + '\n\n## Appendix E. Additional verifications for H12–H13', 1)
hom = hom.replace('the research agent did not view manuscript scans, transcribe, or change the frozen text.', 'the research comparison did not alter that text or supply replacement readings.')
hom = hom.replace('**Kind:** Own application', '**Kind:** Own idea / application')
hom = hom.replace('**Kind:** Own verified implication', '**Kind:** Own idea / verified implication')
hom = hom.replace('**Kind:** Own explicit counterexample', '**Kind:** Own idea / explicit counterexample')
hom = hom.replace('**Kind:** Own clarification', '**Kind:** Own idea / clarification')
hom = hom.replace('**Kind:** Assessment', '**Kind:** Own idea / assessment')
hom = hom.replace('**Kind:** Register relation', '**Kind:** Own idea / register relation')
hom = hom.replace('**Kind:** Manuscript claim', '**Kind:** Unproved claim or abbreviated manuscript argument')
for ident, reason in {
    'H05': 'the frozen wording, cited tower theorem, and counterexample are checked separately in this section.',
    'H08': 'the frozen margin supplies the “iff” and Appendix C proves the scoped criterion.',
    'H09': 'the two displayed cylinder inclusions have different lifting properties under the stated model-category axioms.',
    'H10': 'the selected entries and their different hypotheses are explicitly compared, without changing their statuses.'
}.items():
    pattern = r'(### ' + ident + r' — .*?\n)(.*?)(?=\n### |\n## |\Z)'
    m = re.search(pattern, hom, flags=re.S)
    assert m, ident
    block = m[0]
    meta = re.search(r'(?m)^- \*\*RESULTS_STATE:\*\* [^\n]*', block)
    assert meta, ident
    pos = meta.end()
    block = block[:pos] + '\n- **Confidence:** **High** for the bounded comparison: ' + reason + block[pos:]
    hom = hom[:m.start()] + block + hom[m.end():]

sp = read('research_strata_paths.md')
leads = between(sp, '## Strong W(7), total asphericity, and bounded first-appearance leads', '## Search record and evidence boundaries')
lead_reasons = {
    'SP-L01': ('high', 'the complete frozen packet was searched and compared; this is bounded absence, not archive-wide absence'),
    'SP-L02': ('high', 'the cited manuscript-text layer contains the two explicit axioms; first composition and underlying scans were not verified'),
    'SP-L03': ('high', 'the original-text theorem and editorial counterclaim are explicitly separated in the supplied file'),
    'SP-L04': ('high', 'both quoted formulations occur at the cited supplied textual markers; their historical composition order is not established'),
    'SP-L05': ('high', 'the reported status and review fields are read directly from the supplied registers, without mathematical re-verification'),
    'SP-L06': ('medium', 'the contents headings identify promising sections, but their full text was not supplied or inspected'),
    'SP-L07': ('high', 'the bounded absence and absence of an autograph date follow from the packet; no broader historical conclusion is inferred')
}
for ident,(confidence,reason) in lead_reasons.items():
    pattern = r'(### ' + ident + r' — [^\n]*\n)'
    addition = '\n**Kind:** own idea / bounded contextual comparison. **Confidence:** ' + confidence + '; ' + reason + '.\n'
    leads,n = re.subn(pattern, lambda m: m[1] + addition, leads)
    assert n == 1

sp_intro = between(sp, '## Scope, status, and completeness', '## Statement-by-statement mapping')
sp_intro = re.sub(r'^Parent reported.*?\n\n', '', sp_intro, flags=re.M)
sp_table = between(sp, '## Statement-by-statement mapping', '## Strong W(7), total asphericity, and bounded first-appearance leads')
sp_tail = between(sp, '## Search record and evidence boundaries')

br_intro = body(br).split('## Direct manuscript material relevant to the comparison')[0]
br_intro = br_intro.replace('No scans were viewed and no transcription files were edited by this research agent. ', '')
br_table = between(br, '## Every supplied BISITE and RESIDUE statement', '## Own audit observations: ordinary external products')

closing = '''## K. Completion, validation limits, and recovery records

The package contains all **41 page fragments**, in the requested order (106/002–017, then 107/002–026), and their combined preamble-free fragment. The inventory has **1,202 rows**, each marked `yes`; the doubts register has **342 entries**, preceded by the recurring-notation table and followed by abbreviation and legibility information. All 41 scans received a separate visual audit before the freeze. The scans, attached archives, and supplied context are excluded from the delivered ZIP.

The final integrity check compares all **42 SHA-256 values** (41 page fragments and the combined transcription) with the record made at the **2026-11-16 13:43:19 UTC** freeze. The final check result and its UTC time are recorded in `progress.log` and `records/final_validation.json`. The context was opened only after the freeze; post-freeze changes concern research notes and their supporting records.

**Typesetting limitation:** structural validation found balanced braces, environments, and math delimiters in all page fragments, with the combined text matching the ordered fragments. A full LaTeX compilation could not be performed: the available XeTeX executable lacked `xelatex.fmt`, `latex.ltx`, `tikz-cd.sty`, and `fontspec.sty`. The attempted runs and the environment failure are retained in `records/latex_validation.json`; no successful compilation or rendered-page verification is claimed. The requested deliverable remains a LaTeX fragment with the user-specified state macros, without a preamble.

An independent research-only validation compared the two dossier JSON records against all **255** source rows: every ID, statement, supplied status, locator, and recorded source line matched, with no omissions or duplicates. It also checked the **12** numbered NEW_RESULTS entries, all **60** non-ID metadata cells, and the **3** concluding notices. The dossier comparison classifications are **212 absent**, **37 thematic links**, **1 direct partial form**, and **5 partial underived precursors**; none is a full attestation of the complete supplied modern statement. The supplied statuses remain **146 Proved**, **33 Known**, **57 Refuted**, and **19 Open**, each explicitly a supplied return claim rather than a new verdict in this report.

The supporting `records/` and `scripts/` directories are included for provenance and recovery. The historical `page_*.py` scripts contain the first-pass page texts; **do not rerun them over the frozen files**, because the later visual corrections are recorded in `audit_changes.diff` and already incorporated in `pages/`. `manuscript_leads.md` is likewise a first-pass working record, superseded where the audit or final notes correct it. `frozen_sha256.json`, `visual_audit.md`, `notation_audit.md`, and `structural_validation.json` record the freeze boundary; the research JSONs preserve exact concordance data. `context_search_root.md` and its JSON preserve bounded search locators without redistributing the supplied source files.

The manuscript's unresolved claims, the supplied registers' statuses, and our explicitly scoped mathematical verifications remain separate. Neither a successful modern proof nor a contradictory contextual parallel has changed a letter of the frozen transcription.
'''

parts = [root.rstrip(),
    '## F. Conditional verification of the cote 106 fraction and section claims\n\n' + demote(fraction),
    '## G. Cote 107: relative Hom, external products, and contextual parallels\n\n' + demote(relative),
    '## H. NEW_RESULTS concordance and the sequential-colimit and rectification questions\n\n' + demote(hom),
    '## I. Strong W(7), total asphericity, and bounded first-appearance leads\n\n' + demote(leads),
    '''## J. Complete dossier concordance: 255 supplied statements

Every row is a bounded contextual-comparison note (**kind: own idea / comparison; confidence: high for the stated presence/absence and scope distinction**, based on the complete frozen text and the exact supplied statement). That confidence is not an independent endorsement of the supplied mathematical status, and it does not remove any uncertainty mark on a quoted manuscript reading. A “partial” form and a thematic link are explicitly distinguished from an attestation of the entire supplied statement.

### J.1 STRATA and PATHS: 86 statements

''' + demote(sp_intro + '\n' + sp_table + '\n' + sp_tail, 2),
    '### J.2 BISITE and RESIDUE: 169 statements\n\n' + br_intro + '\n' + demote(br_table, 2),
    closing]

out = '\n\n'.join(part.strip() for part in parts) + '\n'
out = out.replace('`MPL_106+107/MPL_106+107_transcription.tex`', '`MPL_106+107_transcription.tex`')
(BASE / 'MPL_106+107_notes.md').write_text(out, encoding='utf-8')
print(f'Assembled {len(out.encode("utf-8")):,} bytes; {len(out.split()):,} whitespace-delimited words.')
