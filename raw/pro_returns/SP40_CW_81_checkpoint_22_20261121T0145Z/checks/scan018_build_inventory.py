#!/usr/bin/env python3
"""Assign pending inventory identities; no selection or hand adjudication."""
from pathlib import Path
import json
import hashlib
import copy
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
U=json.loads((OUT/'scan018_source_union.json').read_text())
R=json.loads((OUT/'scan018_record_draft.json').read_text())
raw=U['candidate_inventory']
BY={r:{} for r in ['witness C','A','B','C']}
for x in raw:BY[x['reader']][x['original']['value']['element']]=x['original']
# ID, kind, position/name, witness C, A, B, reader C, related locus numbers
S=[
(1,'text','opening paragraph','018.01','018.A.01','018.01','C018.01',[1,2,3]),
(2,'text','Ceci posé paragraph','018.02','018.A.02','018.02','C018.02',[4,5,7,44]),
(3,'insertion','raised (unique)','018.03','018.A.03','018.03','C018.03',[4,5,6]),
(4,'drawing','unique insertion guide','','018.A.04','B.G01','C018.G01',[6]),
(5,'text','two-line lemma','018.04','018.A.05','018.04','C018.04',[8,9,11]),
(6,'drawing','lemma underline and separate left rule','018.04','018.A.06','B.G02','C018.G02',[10]),
(7,'deletion','lemma sign after J','018.05','018.A.07','018.05','C018.05',[9]),
(8,'text','proof paragraph','018.06','018.A.08','018.06','C018.06',list(range(12,44))),
(9,'deletion','la below qu’une','018.07','018.A.09','018.07','C018.07',[13]),
(10,'insertion','raised qu’une','018.08','018.A.10','018.08','C018.08',[13]),
(11,'drawing','qu’une guide and la cancellation','','018.A.11','B.G03a','C018.G03 C018.07',[13]),
(12,'insertion','raised U name and Pi','018.09','018.A.12','018.09','C018.09',[14,15]),
(13,'drawing','U-name insertion guide','','018.A.13','B.G03b','C018.G04',[16]),
(14,'drawing','hook at U-name guide junction','','018.A.13','B.G03b','C018.M01',[17]),
(15,'deletion','first corrected E_i predecessor','018.10','018.A.14','018.10','C018.10',[19]),
(16,'drawing','upper rule above first corrected E_i','','018.A.15','B.G04','C018.B01',[20]),
(17,'deletion','second corrected E predecessor and index context','018.11','018.A.16','018.11','C018.11',[23,24]),
(18,'deletion','choisi/choisie','018.12','018.A.17','018.12','C018.12',[25]),
(19,'drawing','cancellation across chosen-word candidate','','018.A.18','018.12','C018.12',[26]),
(20,'drawing','two chosen-word endpoint points','','018.A.19','B.G05','C018.M02',[27]),
(21,'deletion','first est preceding live word','018.13','018.A.20','018.13','C018.13',[29]),
(22,'insertion','raised (soit Sigma_i^-)','018.14','018.A.21','018.14','C018.14',[34]),
(23,'drawing','soit insertion guide','','018.A.22','B.G06','C018.G06',[34]),
(24,'deletion','deux beneath raised card','018.15','018.A.23','018.15','C018.15',[35]),
(25,'insertion','raised card I=2','018.16','018.A.24','018.16','C018.16',[36]),
(26,'drawing','bottom cancellation path','','018.A.25','018.15','C018.15',[36]),
(27,'drawing','lower hook in card correction','','','','C018.G07',[37]),
(28,'deletion','cancelled word before fortiori','018.17','018.A.26','018.17','C018.17',[38]),
(29,'drawing','final OK and transverse stroke','','018.A.27','B.G08','',[41,42]),
(30,'drawing','faint point beyond final punctuation','','018.A.28','','',[43]),
(31,'text','archive numeral 17 as comment','','018.A.29','B.ARCH','C018.18',[]),
]
inventory=[];cross={r:{} for r in BY}
for n,kind,label,c,a,b,rc,loci in S:
    el=f'018.I{n:02d}'
    ids={r:s.split() for r,s in zip(['witness C','A','B','C'],[c,a,b,rc])}
    sources={r:[copy.deepcopy(BY[r][i]) for i in ids[r]] for r in BY}
    for r in BY:
        for i in ids[r]:cross[r].setdefault(i,[]).append(el)
    inv=dict(cote='81',scan='18',sheet_kind='text',hand=None,element=el,kind=kind,
        position=label,first_words_or_objects=label,transcribed='no',
        selected=None,selection_status='pending root; transcribed becomes yes only for selected source content',
        hand_status='pending root; actual source attributions preserved in source_rows',
        kind_status='pending root final inventory representation; actual source kinds preserved',
        source_rows=sources,related_decision_ids=[f'L018-{v:02d}' for v in loci],
        main_approved=False,final_source_attachment=[])
    inventory.append(inv)
for r in BY:assert set(cross[r])==set(BY[r]),(r,set(BY[r])-set(cross[r]))
U['pending_consolidated_inventory']=inventory;U['raw_inventory_to_pending_elements']=cross
(OUT/'scan018_source_union.json').write_text(json.dumps(U,ensure_ascii=False,indent=2)+'\n')
R['inventory']=inventory;R['raw_inventory_to_pending_elements']=cross
R['source_union_sha256']=hashlib.sha256((OUT/'scan018_source_union.json').read_bytes()).hexdigest()
(OUT/'scan018_record_draft.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
M=dict(scan=18,status='pending root selections',items=inventory,raw_inventory_to_pending_elements=cross)
(OUT/'scan018_inventory_map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
F=json.loads((OUT/'scan018_source_fingerprints.json').read_text())
for p in ['scan018_source_union.json','scan018_record_draft.json','scan018_inventory_map.json']:
    F['prepared_files'][p]=dict(sha256=hashlib.sha256((OUT/p).read_bytes()).hexdigest())
(OUT/'scan018_source_fingerprints.json').write_text(json.dumps(F,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(pending_inventory_elements=len(inventory),raw_source_inventory_rows=len(raw),all_raw_inventory_rows_mapped=True,root_approval_flags=False)))
