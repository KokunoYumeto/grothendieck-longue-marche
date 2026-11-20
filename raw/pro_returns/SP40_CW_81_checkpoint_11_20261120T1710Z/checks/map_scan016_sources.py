"""Source-only map prepared before the independent scan016 returns."""
from pathlib import Path
import json
import hashlib

BASE = Path(__file__).resolve().parents[2]
packet = BASE / 'packets/016'
lines = (packet / 'C_doubts.txt').read_text().splitlines()
categories = {}
heading = None
for number, line in enumerate(lines, 1):
    if line.startswith('## '):
        heading = line[3:]
        categories.setdefault(heading, [])
    elif line.startswith('| 16 |'):
        categories[heading].append(dict(line=number, literal=line))

local = {
 1: ['opening second Sigma: predecessor 2 beneath live 1'],
 2: ['opening cancelled sera|sont'],
 3: ['opening connexe'],
 4: ['right insertion slash|setminus', 'right insertion E subscript 2'],
 5: ['cancelled c\'est after donc'],
 6: ['opening conclusion cqfd|qfd'],
 7: ['first partition E predecessor under Sigma_1^+',
     'five-term partition E predecessor under Sigma_12',
     'lower Car argument E predecessor under Sigma_12',
     'lower Car argument Sigma predecessor under E_1'],
 8: ['O predecessor under Dans initial'],
 9: ['raised conclurait'],
 10: ['small à|colon after égale', 'donc|d\'où before opening inclusion'],
 11: ['raised en|on'],
 12: ['first join under final overbar: older amalg and live cup|amalg',
      'second join under final overbar: older amalg and live cup|amalg, qualified by original C doubt table even though C.tex prints plain cup'],
 13: ['right-edge closing bracket'],
}
rows = categories['Doubtful readings']
assert len(rows) == 13
for number, row in enumerate(rows, 1):
    row.update(source_row=number, local_loci=local[number], status='awaiting independent returns and root crop decisions')
result = dict(scan=16, folder='J81-02', their_page=15, hua_has='text',
              categories=categories, original_C_doubt_rows=13,
              mapped_primary_loci=sum(map(len, local.values())),
              compound_row_policy='Source row identities remain unchanged. Join clusters retain separately variable predecessor/live components in later decisions.',
              source_inventory_rows=len(json.loads((packet/'C_inventory.json').read_text())),
              source_files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in packet.iterdir() if p.is_file()},
              S=dict(id='SA01-K81-06', where='81/15-22',
                     sweep_evidence='Argument-based inference; S explicitly records no scan viewed.',
                     scan016_targets=['Three closure rows: five individual overbar occurrences, including the two strict-inclusion outer rows',
                                      'Notons display: two Sigma_12 overbars',
                                      'Car argument: two overbars, on the corrected Sigma_12 and on Sigma_1^-',
                                      'Final bracketed equality: five overbars, including the long bar and the later two Sigma_12 occurrences'],
                     source_overline_commands=14,
                     current_witnesses='Both current C and H already carry these bars. Root will inspect local ink and record confirmation or overturning without inventing a current-witness omission.',
                     status='pending root crops'),
              independent_readers=dict(A='/root/scan016_a',B='/root/scan016_b',C='/root/scan016_c',
                                       brief='briefs/brief_v14_scan016.md',fork_turns='none',model_override=False),
              root_image_policy='Only returned adjudication crops; no whole scan or supplied half views.')
(BASE/'out/checks/scan016_source_map.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['scan','original_C_doubt_rows','mapped_primary_loci','source_inventory_rows']}))
