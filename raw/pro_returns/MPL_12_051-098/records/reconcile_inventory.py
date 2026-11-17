#!/usr/bin/env python3
"""Reconcile parent-reviewed manual blocks with current TeX state macros.

Uses only the supplied BANDS/SPECIAL physical assignments. No scan or context
access, reading inference, checkpoint creation, or main-inventory modification.
"""
from __future__ import annotations
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re

from rebuild_inventory import parse_page
from inventory_region_bands import BANDS, SPECIAL

BASE = Path(__file__).resolve().parents[1]
PREFIX = "MPL_12_051-098"
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
STATE_KINDS = {"deletion", "insertion", "margin note"}
EXPECTED = {"text":224,"display":97,"diagram":25,"drawing":16,"deletion":156,"insertion":89,"margin note":21}


def write_csv(path, columns, rows):
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer=csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader(); writer.writerows(rows)


def source_only(position):
    return bool(re.fullmatch(r'(?:within page\s*;?\s*)?(?:TeX|source)\s+lines?\b.*', position.strip(), flags=re.I))


def rank_region(scan, region):
    value=region.lower().replace('–','-')
    for spaced,hyphenated in [('upper middle','upper-middle'),('middle lower','middle-lower'),('lower middle','lower-middle')]:
        value=value.replace(spaced,hyphenated)
    if value.startswith('whole '): return -100.0
    if scan==58:
        if 'rotated block' in value:
            for i,word in enumerate(['first row','second row','upper right','middle','lower','bottom']):
                if word in value: return 30.0+i*10
        if 'middle portrait' in value: return 20.0
    if scan==72:
        for i,word in enumerate(['bottom of original','lower original','middle original','middle through upper original']):
            if word in value: return float(i*10)
    # Longer compound regions must be tested before their single-word parts.
    for expression,rank in [('upper-middle',20),('middle-lower',40),('lower-middle',40),('top',0),('bottom',60),('upper',10),('lower',50),('middle',30),('central',30)]:
        if expression in value: return float(rank)
    if value=='below second diagram row': return 30.0
    if value=='below display': return 40.0
    return None


def physical_assignment(scan, tag, start_line):
    eligible=[(line,region) for line,region in BANDS[scan] if line<=start_line]
    if not eligible: raise ValueError(f'No band for scan {scan} line {start_line}')
    anchor,band=eligible[-1]
    key=(scan,tag,start_line)
    return SPECIAL.get(key,band), {'source':'SPECIAL' if key in SPECIAL else 'BANDS','band_start_line':anchor,'band_region':band,'special_key':list(key) if key in SPECIAL else None}


def main():
    current=BASE/f'{PREFIX}_inventory.csv'
    with current.open(encoding='utf-8-sig', newline='') as handle: originals=list(csv.DictReader(handle))
    physical_manual=[(i+2,row) for i,row in enumerate(originals) if not source_only(row['position'])]
    removed_manual=[{'csv_line':line,**row} for line,row in physical_manual if row['kind'] in STATE_KINDS]
    removed_auto=[{'csv_line':i+2,**row} for i,row in enumerate(originals) if source_only(row['position'])]
    items=[]; label_updates=[]; mismatches=[]; sources={}; states=[]; figures=[]; used_special=set()
    for manual_index,(line,old) in enumerate(physical_manual):
        if old['kind'] in STATE_KINDS: continue
        row=dict(old); scan=int(row['scan'])
        row['kind']={'title':'text','formula':'display'}.get(row['kind'],row['kind'])
        if scan==96 and row['sheet_kind']=='title_only': row['sheet_kind']='cover'
        before=row['first_words_or_objects']
        if scan==58 and row['element']=='5':
            row['first_words_or_objects']='H_Y^{j|i}(X) -- H^{j|i}(X) -- H^{j|i}(U) -- H_Y^{j+1|i+1}(X)'
        elif scan==73 and row['element']=='2':
            row['first_words_or_objects']='M motif ct tordu | et tordu de poids ρ'
        elif scan==80 and row['element']=='1':
            row['first_words_or_objects']='Noter | Notons que'
        elif scan==89 and row['element']=='4':
            row['first_words_or_objects']='De (iv) et (vi) | (vii) résulte que si rho=0'
        elif scan==90 and row['element']=='14':
            row['first_words_or_objects']='vrai pour ∀ P, irréd. ou non !'
        if row['first_words_or_objects']!=before:
            label_updates.append({'scan':scan,'original_csv_line':line,'old':before,'new':row['first_words_or_objects'],'authority':'explicit primary-reader instruction; inventory label only'})
        rank=rank_region(scan,row['position'])
        if rank is None:
            mismatches.append({'type':'manual_order_region_unranked','scan':scan,'csv_line':line,'position':row['position']})
            rank=30.0
        items.append({'row':row,'scan':scan,'rank':rank,'within':(0,manual_index,0),'origin':'manual','original_csv_line':line,'original_element':old['element'],'physical_region':old['position']})

    for page in sorted((BASE/'pages').glob(f'{PREFIX}_12_scan*.tex')):
        scan=int(re.search(r'scan(\d{3})\.tex$',page.name).group(1)); raw=page.read_text()
        sources[page.name]=hashlib.sha256(page.read_bytes()).hexdigest()
        events,diagnostics=parse_page(raw)
        mismatches.extend({'scan':scan,'type':'source_structure',**d} for d in diagnostics)
        sheet=next((row['sheet_kind'] for row in originals if int(row['scan'])==scan),'text')
        if scan==96: sheet='cover'
        for event in events:
            is_state=event.kind in STATE_KINDS and event.tag in {'deleted','inserted','margin'}
            is_new_figure=scan in {90,91} and event.tag=='figure'
            if not (is_state or is_new_figure): continue
            first=raw.count('\n',0,event.start)+1; last=raw.count('\n',0,event.end-1)+1
            region,assignment=physical_assignment(scan,event.tag,first)
            if assignment['special_key']: used_special.add(tuple(assignment['special_key']))
            if is_new_figure and scan==90: region='top-left; author-number enclosure'
            if is_new_figure and scan==91: region='upper-left margin; frame and curved leader'
            rank=rank_region(scan,region)
            if rank is None:
                mismatches.append({'type':'source_order_region_unranked','scan':scan,'macro':event.tag,'source_line':first,'region':region});rank=30.0
            span=f'TeX lines {first}-{last}; chars {event.start+1}-{event.end}'
            attachment={'deletion':'deletion at','insertion':'insertion attached at','margin note':'margin note attached at','drawing':'drawing at'}[event.kind]
            prefix=re.sub(r'\s+',' ',raw[event.start:event.end]).strip()[:220]
            row={'cote':'12','scan':str(scan),'sheet_kind':sheet,'element':'','kind':event.kind,'position':f'{region}; {attachment} {span}','first_words_or_objects':prefix,'transcribed':'yes'}
            detail={'scan':scan,'macro':event.tag,'kind':event.kind,'source_start_line':first,'source_end_line':last,'source_start_char':event.start+1,'source_end_char':event.end,'physical_region':region,'assignment':assignment,'source_file':page.name,'prefix':prefix}
            within=(1,event.start,0)
            if is_new_figure and scan==90:
                number_item=next(item for item in items if item['origin']=='manual' and item['scan']==90 and item['original_element']=='1')
                within=(0,number_item['within'][1],1)
            item={'row':row,'scan':scan,'rank':rank,'within':within,'origin':'current_state' if is_state else 'new_drawing','physical_region':region,'source':detail}
            items.append(item)
            (states if is_state else figures).append(detail)
    required_special={key for key in SPECIAL if key[1] in {'deleted','inserted','margin'}}
    for key in sorted(required_special-used_special):
        mismatches.append({'type':'unused_state_SPECIAL','key':list(key),'region':SPECIAL[key]})
    items.sort(key=lambda item:(item['scan'],item['rank'],item['within']))
    per_scan=Counter(); final=[]; provenance=[]
    for item in items:
        per_scan[item['scan']]+=1; row=item['row'];row['element']=str(per_scan[item['scan']]);final.append(row)
        if 'source' in item: item['source']['final_element']=row['element']
        provenance.append({key:value for key,value in item.items() if key not in {'row','within'}}|{'final_element':row['element'],'order_key':[item['rank'],*item['within']]})
    counts=Counter(row['kind'] for row in final)
    if dict(counts)!=EXPECTED: mismatches.append({'type':'count_mismatch','expected':EXPECTED,'actual':dict(counts)})
    records=BASE/'records'
    target=records/f'{PREFIX}_inventory_reconciled_candidate.csv'
    write_csv(target,COLUMNS,final)
    write_csv(records/f'{PREFIX}_inventory_original_manual_rows.csv',COLUMNS,[row for _,row in physical_manual])
    write_csv(records/f'{PREFIX}_inventory_manual_blocks.csv',COLUMNS,[item['row'] for item in items if item['origin']=='manual'])
    state_columns=['scan','final_element','macro','kind','source_file','source_start_line','source_end_line','source_start_char','source_end_char','physical_region','prefix']
    write_csv(records/f'{PREFIX}_inventory_current_state_rows.csv',state_columns,[{k:item[k] for k in state_columns} for item in sorted(states,key=lambda x:(x['scan'],x['source_start_char']))])
    report={'candidate':str(target),'original_inventory_sha256':hashlib.sha256(current.read_bytes()).hexdigest(),'source_sha256':sources,'manual_nonstate_retained':sum(item['origin']=='manual' for item in items),'manual_state_rows_replaced':removed_manual,'old_automatic_rows_replaced_count':len(removed_auto),'current_state_rows':len(states),'new_drawings':figures,'total_rows':len(final),'counts_by_kind':dict(counts),'counts_by_scan':dict(per_scan),'label_updates':label_updates,'mismatches':mismatches,'row_provenance':provenance,'ordering_method':'Physical region ranks; manual order retained within a region; state macros follow source order within a region and have explicit source attachment. Scans 058 and 072 use the supplied rotated reading order. Scan 090 enclosure follows its separate manual number row.','source_parser_issue_not_imported':{'scan':52,'candidate_element':'e012','issue':'pure fbox/diagram wrapper plus period creates a redundant source-parser text row; reconciled inventory uses the original manual blocks and does not import this row.'},'metadata_policy':'No extra mspage rows added, as instructed. Author number 090 remains a separate original manual text row alongside its enclosure drawing.'}
    (records/'inventory_reconciliation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'candidate':str(target),'manual_nonstate':report['manual_nonstate_retained'],'manual_state_replaced':len(removed_manual),'old_auto_replaced':len(removed_auto),'current_state':len(states),'new_drawings':len(figures),'rows':len(final),'counts':dict(counts),'mismatches':mismatches},ensure_ascii=False,indent=2))


if __name__=='__main__': main()
