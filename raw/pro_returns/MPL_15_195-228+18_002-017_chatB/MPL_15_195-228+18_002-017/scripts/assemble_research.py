#!/usr/bin/env python3
"""Assemble research only; never modify a frozen transcription file."""
from pathlib import Path
import re, json, hashlib
ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / 'records'
PREFIX = ROOT.name
def read(name):
    return (REC / name).read_text(encoding='utf-8')
def between(s, start, end=None):
    a = s.index(start) + len(start)
    b = len(s) if end is None else s.index(end, a)
    return s[a:b].strip()
def clean(s):
    s = s.replace('**Kind:** own calculation, verifying an earlier lead.', '**Kind:** own idea (calculation verifying an earlier lead).')
    s = s.replace('**Kind:** own calculation, checking an earlier claim.', '**Kind:** own idea (calculation checking an earlier claim).')
    s = s.replace('**Kind:** own calculation.', '**Kind:** own idea (calculation).')
    s = s.replace('**Kind / comparison:** own calculation', '**Kind / comparison:** own idea (calculation)')
    s = s.replace('**Kind / comparison:** own deduction', '**Kind / comparison:** own idea (deduction)')
    s = s.replace('a claim of flawless OCR', 'a claim of flawless text extraction')
    s = s.replace('[DM,', '[DM12,').replace('[Deu41]', '[Deuring41]')
    s = s.replace('| Deu41 |', '| Deuring41 |')
    s = s.replace("Located at the responsible reader's request for the separate P15/207 real-realization calculation.", 'Used for the real-realization calculation R11.')
    s = re.sub(r' Retrieval refs?:[^\n]+', '', s)
    s = re.sub(r'^The retrieval references are an internal handoff aid;.*$', '', s, flags=re.M)
    s = re.sub(r'(?m)^> ?', '', s)
    s = s.replace(r'\(H^{\unsure{2|1}}(\mathbf Q_\ell,G_\ell^{\circ(\alpha)})\)', r'`H^{\unsure{2|1}}(\mathbf Q_\ell,G_\ell^{\circ(\alpha)})`')
    for v in ('Housh|Harish', 'Rauch', 'Saavedra'):
        s = s.replace('\\(\\unsure{' + v + '}\\)', '`\\unsure{' + v + '}`')
    return s.strip()
root = clean(read('research_root.md'))
additional = clean(read('research_additional.md'))
period = read('research_periods_galois.md')
keys = {'R1':'DM12','R2':'Kahn24','R3':'BostCharles16','R4':'Kawabe26','R5':'KSV26','R6':'BrownDupont21','R7':'DanielsLozano','R8':'Waldschmidt06','R9':'CG17'}
period = re.sub(r'\bR[1-9]\b', lambda m: keys[m.group()], period)
period = period.replace('Appendix A', 'Calculation P-A').replace('Appendix B', 'Calculation P-B').replace('Appendix C', 'Calculation P-C')
period = re.sub(r'(?m)^### A\.', '### P-A.', period)
period = period.replace('No conclusion from M23 or M28a about pure semisimplicity has been added here without checking its missing full source.', 'R37 checks the pure rational Nori–André equivalence in a primary source; the unavailable full M23/M28a returns retain their register status.')
period = clean(period)
lefschetz = read('research_lefschetz.md')
for n in range(2,7):
    lefschetz = re.sub(r'Section '+str(n)+r'\b', 'Section L'+str(n), lefschetz)
    lefschetz = re.sub(r'(?m)^## '+str(n)+r'\.', '### L'+str(n)+'.', lefschetz)
    lefschetz = re.sub(r'(?m)^### '+str(n)+r'\.', '#### L'+str(n)+'.', lefschetz)
lefschetz = re.sub(r'\b(in|of|by) §([2-6])', r'\1 §L\2', lefschetz)
lefschetz = lefschetz.replace('and §6 make', 'and §L6 make').replace('; §4 records', '; §L4 records')
lefschetz = lefschetz.replace('what is and is not established here', 'the available evidence')
lefschetz = clean(lefschetz)
bridges = clean(read('research_bridges_oda.md'))
bridges = bridges.replace('(Z(G))', '$Z(G)$').replace('(Q(x,Cy))', '$Q(x,Cy)$')

front = read('research_frontmatter.md')
table = '| Requested pair | ' + between(bridges, '| Requested pair |', '## Note candidates')
root = root.replace('## Current manuscript: realizations, points, and reconstruction', '## Atomic notes: current cote 15')
root = root.replace('## Reused typescripts: mathematical checks and documentary connections', '## Atomic notes: reused typescripts')
root = root.replace('## Current cote 18: specialization, twists, and fundamental classes', '## Atomic notes: current cote 18 and reading questions')
period_notes = between(period, '## Atomic note candidates', '## Calculation P-A')
lef_notes = between(lefschetz, '## 1. Atomic note candidates', '### L2.')
lef_notes = lef_notes[lef_notes.index('### RL01'):]
bridge_notes = between(bridges, '## Note candidates', '## Supporting calculations and source scopes')
bridge_notes = bridge_notes[bridge_notes.index('### B01'):]
period_calc = '## Calculation P-A ' + between(period, '## Calculation P-A', '## Verified external references')
lef_calc = '### L2. ' + between(lefschetz, '### L2.', '## 7. Search and verification log')
bridge_calc = between(bridges, '## Supporting calculations and source scopes', '## Primary references checked')
period_search = '| Search ID | ' + between(period, '| Search ID |', 'In particular,')
lef_search = between(lefschetz, '## 7. Search and verification log', '## 8. Primary bibliography and retrieval references')
lef_search = lef_search.replace('### Local searches', '#### Lefschetz context searches').replace('### Primary-source browsing', '#### Lefschetz primary-source access record')
period_limits = between(period, '## Search audit and remaining limits')
period_bib = between(period, '## Verified external references', '## Search audit and remaining limits')
lef_bib = between(lefschetz, '## 8. Primary bibliography and retrieval references')
lef_bib = re.sub(r'§L([2-6])', r'§\1', lef_bib).replace('§§L', '§§')
bridge_bib = between(bridges, '## Primary references checked')
standing = clean(read('research_standing.md')) if (REC/'research_standing.md').exists() else '## Standing sections\n\n[Assembly awaits the completed standing-section audit.]'
standing = standing.replace('# Standing documentary sections', '## Standing documentary survey').replace('](../pages/', '](pages/')
parts = [front, table, root, additional,
         '## Atomic notes: periods and arithmetic motivic groups\n\n'+period_notes,
         '## Atomic notes: Lefschetz rings and the context programme\n\n'+lef_notes,
         '## Atomic notes: the four comparisons and Oda\n\n'+bridge_notes,
         standing, '## Supporting calculations: correspondences, operators, and lettering\n\n'+lef_calc,
         period_calc, '## Supporting calculations: the four comparisons and Oda\n\n'+bridge_calc,
         read('research_register_delta.md'), '### Period context search sets\n\n'+period_search,
         lef_search, '### Period-source audit and limits\n\n'+period_limits,
         '## Bibliography and precise source locators\n\n### Periods and arithmetic groups\n\n'+period_bib,
         '### Lefschetz correspondences and standard conjectures\n\n'+lef_bib,
         '### Linear/nonlinear comparisons and Oda\n\n'+bridge_bib, read('research_additional_bibliography.md')]
out = '\n\n'.join(p.strip() for p in parts) + '\n'
out = re.sub(r'\n{4,}', '\n\n\n', out)
out = out.replace('four-row comparison below', 'four-row comparison above').replace('four-row table below', 'four-row table above')
target = ROOT / f'{PREFIX}_notes.md'
target.write_text(out, encoding='utf-8')
note_ids = re.findall(r'^### ((?:R|PG|RL|B|O)\d{2}) —', out, flags=re.M)
assert len(note_ids) == 78, (len(note_ids), note_ids)
assert len(set(note_ids)) == 78
assert not any(ord(c)<32 and c not in '\n\t\r' for c in out)
report={'note_count':len(note_ids),'note_ids':note_ids,'words':len(out.split()),'bytes':len(out.encode()),'sha256':hashlib.sha256(out.encode()).hexdigest(),'standing_complete':(REC/'research_standing.md').exists()}
(REC/'research_assembly_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
