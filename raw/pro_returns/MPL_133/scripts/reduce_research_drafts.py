#!/usr/bin/env python3
"""One-time archival integration: keep notes in main, calculations in supplements.

Run only after all candidate notes and references have been integrated and
reviewed. This script never reads or writes any frozen TeX file.
"""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
r=root/'research'
main=(root/'MPL_133_notes.md').read_text()
ids=re.findall(r'^### ([WPFBGJM]\d\d)\b',main,re.M)
assert len(ids)==len(set(ids))==76

def clean(s):
    s=re.sub(r'genui.*?','',s)
    s=re.sub(r'^- Retrieval references.*\n?', '', s, flags=re.M)
    s=re.sub(r'\s+Retrieval:.*?(?=\n\n|\Z)','',s,flags=re.S)
    s=s.replace('This counterexample was proposed by root and checked here against the cited family and torus-extension results.', 'This calculation was checked against the cited family and torus-extension results.')
    return s

f=(r/'finite_sets.md').read_text()
proof=f[f.index('## Independent calculations and precise limits'):f.index('## Primary literature, APA references, and verification locators')]
loc=f[f.index('## Primary literature, APA references, and verification locators'):f.index('## Integration priorities')]
# Keep access and locator evidence, with the canonical APA entries in main.
for para in re.split(r'\n\n',loc):
    if para.startswith(('Bouc,','Dress,','Joyal,','Kannan,')):
        loc=loc.replace(para+'\n\n','')
(r/'finite_sets.md').write_text('# Finite-set calculations and source locators\n\nThe canonical notes F01–F16 are in [MPL_133_notes.md](../MPL_133_notes.md); this supplement preserves the longer independent calculations and source-access qualifications. It contains no revision of the frozen transcription.\n\n'+clean(proof+loc))

g=(r/'formal_groups.md').read_text()
context=g[g.index('## Context search record'):g.index('## Both Hua entries checked explicitly')]
proof=g[g.index('## Appendix A'):g.index('## APA references and exact checked locators')]
(r/'formal_groups.md').write_text('# Formal and algebraic group proof supplement\n\nThe canonical notes G01–G21, exact Hua-ID reconciliation, APA references, and source/version qualifications are in [MPL_133_notes.md](../MPL_133_notes.md). This supplement preserves the full mathematical checks and the per-note context table. All assertions concern the explicit categories and hypotheses stated here; none changes the frozen transcription.\n\n'+clean(context+proof))

b=(r/'binomial_bridge.md').read_text()
context=b[b.index('## Context-search record'):b.index('### Two contextual cautions for synthesis')]
(r/'binomial_bridge.md').write_text('# Binomial-bridge context supplement\n\nThe canonical notes B01–B11 and the checked primary-source versions and references are in [MPL_133_notes.md](../MPL_133_notes.md). This table preserves the per-item contextual comparison; the executed query ledger is records/context_searches.jsonl. The contextual basis overstatement is treated in B11, and the dimension-two quadratic splitting in W16.\n\n'+clean(context))

(r/'quadratic_and_misc.md').write_text('# Integration record: quadratic and miscellaneous notes\n\nNotes W01–W16, P01–P05, J01–J05, and M01–M02, including their context comparisons and references, have been consolidated in [MPL_133_notes.md](../MPL_133_notes.md). The independent mathematical checks are in [quadratic_proof_checks.md](quadratic_proof_checks.md). This integration did not alter any frozen transcription.\n')
(r/'synthesis_and_registers.md').write_text('# Integration record: synthesis and registers\n\nThe evidence conventions, answers to the planning questions, standing register of unverified or withdrawn steps, title-sheet/page-count register, and results-state reconciliation have been consolidated in [MPL_133_notes.md](../MPL_133_notes.md). The canonical report retains all their source locators and qualifications.\n')
print('76 canonical notes retained; research supplements reduced to nonduplicative proof and source records.')
