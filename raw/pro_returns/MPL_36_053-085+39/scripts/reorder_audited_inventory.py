#!/usr/bin/env python3
"""Apply root-specified inventory-only changes after the visual second audit.

Original element IDs below refer to the pre-reorder record. Guard assertions
make this a one-use migration. It does not read or write transcription pages.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT=Path(__file__).resolve().parent.parent
BASE='MPL_36_053-085+39'
changes={
    '36_056':[(24,'before',6,'ce above le composé','Calculons le composé'),(25,'after',4,'pointer from inutile note to bracket','inutile pour définir Delta*')],
    '36_062':[(43,'after',24,'small bracket by generic H^1 term of (7)','(7) 0 to H^1(X,Z_l(1)) to H^1 invariants to R tensor Z_l to 0')],
    '36_071':[(27,'after',10,'curved open outline around R tensor Z_ell cases','N.B. R tensor Z_l cases')],
    '36_074':[(34,'after',26,'grâce à xi (doubtful)','T_l S and T_l T product phi_xi')],
    '36_079':[(29,'before',19,'two vertical emphasis strokes','En particulier Corollaire 2')],
    '39_010':[(28,'before',19,'1 in A_0, etc','Le morphisme différence et produit'),(29,'before',10,'vertical emphasis stroke','On suppose; (a) Les opérations simpliciales'),(30,'before',12,'vertical emphasis stroke','(b) Le composé de deux A_*-morphismes')],
    '39_012':[(22,'after',5,'double implication','Cor. 1'),(23,'before',3,'vertical emphasis stroke','Condition hensélienne'),(24,'before',5,'two vertical emphasis strokes','Cor. 1'),(25,'before',18,'vertical emphasis stroke','Cor. 2 Soit')],
    '39_013':[(20,'start',None,'vertical emphasis stroke',None),(21,'before',7,'vertical emphasis stroke','Plus généralement; Cor 3'),(22,'after',14,'curved vertical boundary and baseline','a) b) c) d) impliquent-ils que S_n est fid. plat')],
    '39_014':[(19,'after',5,'Considérons','Considérons; voit; alors')],
    '39_019':[(23,'start',None,'vertical emphasis stroke',None),(24,'before',5,'vertical emphasis stroke','Alors F est un élément régulier')],
    '39_020':[(16,'after',11,'square-ended underline bracket','(Gr A)^N times (Gr A)[[Z]] to (Gr A)[[Z]]')],
}
replacements={
    '36_078':[(3,'928 48-53','928 48.53')],
    '39_006':[(5,'de V0⊗k0 k','de frak g0⊗k0 k'),(7,'V0','frak g0'),(9,'Wbar(V0)×Wbar(V0)–Wbar(V0)','Wbar(frak g0)×Wbar(frak g0)–Wbar(frak g0)'),(13,'et si V0–h0 est un hom; Utilisant le th. d’Ado','et si frak g0–h0 est un hom; Utilisant le th. d’Ado')],
    '39_015':[(17,'D’où un foncteur M_A*','D’où un foncteur M (notation doubtful)')],
}

def main():
    pending=[];report=[]
    for key in sorted(set(changes)|set(replacements)):
        path=ROOT/'records'/f'{key}.json'
        before=path.read_bytes();record=json.loads(before)
        entries=[{'original_id':i,'element':item} for i,item in enumerate(record['elements'],1)]
        by_id={item['original_id']:item for item in entries}
        for source_id,placement,anchor_id,expected_source,expected_anchor in changes.get(key,[]):
            source=by_id[source_id]
            assert source['element'][2]==expected_source,(key,source_id,'source mismatch')
            if anchor_id is not None:
                anchor=by_id[anchor_id]
                assert anchor['element'][2]==expected_anchor,(key,anchor_id,'anchor mismatch')
                assert sum(item['element'][2]==expected_anchor for item in entries)==1,(key,'ambiguous anchor')
            entries.remove(source)
            destination=0 if placement=='start' else entries.index(anchor)+(placement=='after')
            entries.insert(destination,source)
        for element_id,old,new in replacements.get(key,[]):
            assert by_id[element_id]['element'][2]==old,(key,element_id,'replacement mismatch')
            by_id[element_id]['element'][2]=new
        moved_ids={item[0] for item in changes.get(key,[])}
        assert [item['original_id'] for item in entries if item['original_id'] not in moved_ids]==[
            n for n in range(1,len(entries)+1) if n not in moved_ids
        ],(key,'unrequested ordering changed')
        record['elements']=[item['element'] for item in entries]
        after=(json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode()
        pending.append((path,before,after))
        report.append({'record':key,'original_ids_in_new_order':[item['original_id'] for item in entries],
                       'moves':len(changes.get(key,[])),'replacements':len(replacements.get(key,[])),
                       'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest()})
    # Validate every original record before mutating any of them.
    for path,before,after in pending:assert path.read_bytes()==before,('concurrent record change',path)
    for path,before,after in pending:path.write_bytes(after)
    with (ROOT/f'{BASE}_inventory.csv').open('w',newline='') as stream:
        writer=csv.writer(stream)
        writer.writerow(['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        for path in sorted((ROOT/'records').glob('*.json')):
            record=json.loads(path.read_text())
            for n,(kind,position,words) in enumerate(record['elements'],1):
                writer.writerow([record['cote'],record['scan'],record['sheet_kind'],n,kind,position,words,'yes'])
    result={'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'scope':'Root-directed inventory changes only; transcription files untouched.',
            'changes':report,'skipped':[]}
    (ROOT/'qa'/'inventory_reorder.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
