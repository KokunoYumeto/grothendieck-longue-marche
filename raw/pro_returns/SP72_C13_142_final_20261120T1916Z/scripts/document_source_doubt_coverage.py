"""Document the main reader's explicit crosswalk of every C doubt mark.

This parses supplied TeX only. It does no OCR, ink reading or new adjudication.
The deleted-mark crosswalk was compared manually against existing decisions.
Run again after the audits to carry their final decision texts into the table.
"""
from pathlib import Path
import csv
import json
import re

OUT = Path(__file__).resolve().parents[1]
SRC = OUT.parent/'source/SP72_C13_142_texts'

DELETED_REFS = {
    77: ['C077-deleted-chemins','C077-deleted-yx','C077-deleted-ff'],
    78: ['C078-extra-grace','C078-extra-u','C078-extra-en_l'],
    79: ['unassigned-deleted-les','unassigned-deleted-underbrace','unassigned-deleted-donc'],
    80: ['C080-unassigned-deleted-ou','C080-unassigned-deleted-un','C080-unassigned-deleted-vient'],
    81: ['C081-D1','C081-D2'],
    82: ['C082-D1','C082-D2'],
    83: [],
    84: ['C084-D01','C084-D02'],
    85: [],
    86: ['086-D01'],
    87: ['C087-D01','C087-D02'],
    88: ['C088-deleted-X','C088-deleted-La','C088-deleted-on','C088-inserted-action'],
    89: ['C089-D01','C089-D02'],
    90: ['090-D01','090-D02','090-D03','090-D04'],
    91: ['C091-continuité','C091-et'],
    92: [f'C092-D{i:02}' for i in range(1,6)],
    93: ['C093-esp','C093-prolong','C093-un','C093-dans','C093-aux','C093-comment','C093-equation-zero','C093-puisque'],
    94: [f'094-D{i:02}' for i in range(1,22)],
    95: ['C095-D01','C095-D02',['C095-D03','C095-D04'],'C095-D05'],
    96: ['D096-01','D096-02'],
    97: ['097-D01','097-D02'],
    98: [f'C098-D{i:02}' for i in range(1,8)],
    99: ['D099-01'],
    100: ['100-C-extra-paraît','100-C-extra-deleted-pour-les'],
}

def commands(text, name):
    for match in re.finditer(r'\\'+name+r'\{', text):
        index, depth = match.end(), 1
        while depth:
            if text[index] == '{' and text[index-1] != '\\':
                depth += 1
            elif text[index] == '}' and text[index-1] != '\\':
                depth -= 1
            index += 1
        yield match.start(), index, text[match.start():index]

with (SRC/'MARKS.tsv').open() as stream:
    marks = list(csv.DictReader(stream, delimiter='\t'))
rows=[]
for scan in range(77,101):
    source=(SRC/'pages'/f'142_scan{scan:03}.tex').read_text()
    deleted=list(commands(source,'deleted'))
    uncertain=sorted([item for name in ['unsure','illegible'] for item in commands(source,name)])
    live_marks=[m for m in marks if int(m['scan'])==scan]
    report=json.loads((OUT/'documentation/reviews'/f'scan{scan:03}'/'report.json').read_text())
    decisions={d['id']:d for d in report['decisions']}
    live_index=deleted_index=0
    for ordinal,(start,end,mark) in enumerate(uncertain,1):
        in_deleted=any(a<start<b for a,b,_ in deleted)
        if in_deleted:
            refs=DELETED_REFS[scan][deleted_index]
            refs=refs if isinstance(refs,list) else [refs]
            deleted_index+=1
        else:
            original=live_marks[live_index]
            assert original['the mark as written']==mark,(scan,mark,original)
            refs=[original['id']]
            live_index+=1
        for ref in refs:
            assert ref in decisions,(scan,ref)
        rows.append({
            'scan':f'{scan:03}', 'source_order':ordinal,
            'state_in_C':'inside deleted text' if in_deleted else 'live text',
            'source_mark':mark, 'decision_refs':'; '.join(refs),
            'final_recorded_reading':' ; '.join(decisions[ref]['reading'] for ref in refs),
            'record':'supplementary decisions in doubts.md' if in_deleted else 'decisions.tsv',
            'note':('C’s one doubtful phrase is separated into an upper cancelled il considère and a lower cancelled il y a l’action de. The additional il y a remains doubtful; l’action de is legible and cancelled. See 095-15/16.'
                    if scan==95 and in_deleted and deleted_index==3 else '')
        })
    assert live_index==len(live_marks),(scan,live_index,len(live_marks))
    assert deleted_index==len(DELETED_REFS[scan]),(scan,deleted_index)

path=OUT/'documentation/source_doubt_coverage.tsv'
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)
counts={state:sum(r['state_in_C']==state for r in rows) for state in ['live text','inside deleted text']}
assert counts=={'live text':175,'inside deleted text':85},counts
print(json.dumps({'source_C_doubt_marks':len(rows),'coverage':counts,'crosswalk':str(path)},indent=2))
