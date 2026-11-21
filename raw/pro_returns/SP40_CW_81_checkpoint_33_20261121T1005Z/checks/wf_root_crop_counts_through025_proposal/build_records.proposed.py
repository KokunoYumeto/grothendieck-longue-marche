"""Build delivery tables from main-reader decisions, without altering transcription."""
from pathlib import Path
import csv,json,collections,re
ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP40_CW_81'
def esc(x):
    if x is None:return '—'
    if isinstance(x,(dict,list)):x=json.dumps(x,ensure_ascii=False)
    return str(x).replace('|','\\|').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(esc(x) for x in row)+' |\n' for row in rows)
def write_csv(name,fields,rows,delimiter=','):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
decisions=[(r,d) for r in records for d in r['decisions']]
changes=['# SP40_CW_81 — consolidated reading decisions\n',
    'Every reading rests on the supplied scan. Three independent proposed readings are retained under `readers/`; main-reader decisions are retained under `records/`. Rows resolving or retaining a C doubt are included even when the final reading has no textual change. Counts refer to decision loci, not changed tokens; macro syntax alone is excluded. H has no collation rows on scans with no transcribed text.\n',
    '## Counts\n']
countrows=[];tot=collections.Counter()
for r in records:
    cs=collections.Counter()
    for d in r['decisions']:
        cs['C']+=bool(d.get('diff_C'));cs['H']+=bool(d.get('diff_H'))
        for witness in ('C','H'):
            if d.get('diff_'+witness):cs[witness+'_'+d['confidence']]+=1
        if d.get('diff_C') or d.get('diff_H'):cs[d['confidence']]+=1
    tot.update(cs);countrows.append([f"{r['scan']:03d}",cs['C'],cs['C_high'],cs['C_medium'],cs['C_low'],cs['H'],cs['H_high'],cs['H_medium'],cs['H_low'],len(r.get('doubts',[]))])
countrows.append(['Total',tot['C'],tot['C_high'],tot['C_medium'],tot['C_low'],tot['H'],tot['H_high'],tot['H_medium'],tot['H_low'],sum(len(r.get('doubts',[])) for r in records)])
changes.append(table(['Scan','Against C','C high','C medium','C low','Against H','H high','H medium','H low','Remaining doubt loci'],countrows))
changes.append('\n## Consequential corrections\n')
con=[f"- Scan {r['scan']:03d}, {d['location']}: {d['mathematical_consequence']}" for r,d in decisions if d.get('mathematical_consequence') and (d.get('diff_C') or d.get('diff_H'))]
changes.append('\n'.join(con) if con else 'None recorded on the pages decided so far.')
collation=[];inventory=[];doubts=[];notes=['# SP40_CW_81 — notes while reading\n\nThese notes report only the supplied pages. Reading and collating a mathematical statement does not certify its proof. Actual checks are distinguished in CHECK_EVENTS.tsv.\n'];events=[]
for r in records:
    n=r['scan'];changes.append(f'\n## Scan {n:03d}\n')
    dr=[]
    for d in r['decisions']:
        readers=d.get('readers',{})
        readertext='; '.join(f'{k}: {v}' for k,v in readers.items()) if isinstance(readers,dict) else str(readers)
        evidence=d.get('evidence','')
        if d.get('qualification'):evidence+=' '+d['qualification']
        if d.get('crop'):evidence+=' Image: '+str(d['crop'])+'.'
        if d.get('C_doubt_status'):evidence+=' C doubt: '+d['C_doubt_status']+'.'
        if d.get('S_id'):evidence+=' Witness S '+d['S_id']+': '+d.get('S_status','reviewed')+'.'
        if d.get('diff_C') or d.get('diff_H') or d.get('C_doubt_status') or d.get('S_id') or d.get('log_decision'):
            dr.append([d['id'],d['location'],d.get('C'),d.get('H'),d['final'],readertext,evidence,d['confidence']])
        if d.get('diff_H') and r['hua_has']=='text':
            collation.append({'folder':r['folder'],'their_page':r['their_page'],'our_scan':n,'line':d['location'],'their_reading':d.get('H',''),'codex_reading':d.get('C',''),'final_reading':d['final'],'scan_shows':evidence,'kind':d['kind'],'marked_in_H':d.get('marked_in_H','no'),'confidence':d['confidence']})
    changes.append(table(['ID','Place','Witness C','Witness H','Final','Three readings','What the scan shows / decision','Confidence'],dr) if dr else 'No reading differences found.\n')
    changes.append('\n### Still unresolved\n')
    rd=r.get('doubts',[])
    changes.append(table(['Place','Reading','Alternatives','Confidence','Reason'],[[d['location'],d['reading'],d.get('alternatives','—'),d['confidence'],d.get('reason','')] for d in rd]) if rd else 'None.\n')
    for d in rd:doubts.append([f'{n:03d}',d['location'],d['reading'],d.get('alternatives','—'),d['confidence'],d.get('reason','')])
    for i in r.get('inventory',[]):inventory.append({'scan':n,**i})
    notes.append(f'\n## Scan {n:03d}\n\n'+r.get('notes','')+'\n')
    for e in r.get('check_events',[]):events.append(e)
(ROOT/f'{PREFIX}_changes.md').write_text('\n'.join(changes)+'\n')
write_csv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation,'\t')
write_csv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory)
global_events=ROOT/'checks'/'global_check_events.json'
if global_events.exists():events.extend(json.loads(global_events.read_text()))
write_csv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events,'\t')
(ROOT/f'{PREFIX}_notes.md').write_text('\n'.join(notes))
abbr=[]
for r in records:
    for a in r.get('abbreviations',[]):abbr.append([r['scan'],a['form'],a['expansion']])
leg=(ROOT/'legibility_note.md').read_text() if (ROOT/'legibility_note.md').exists() else 'Assessment in progress; the record currently covers only the scans listed above.'
notation=(ROOT/'notation.md').read_text()
# Escape alternative separators for Markdown tables, retaining raw reader notation separately.
notation=re.sub(r'(?<!`)`([^`\n]+)`(?!`)',lambda m:'`'+re.sub(r'(?<!\\)\|',r'\\|',m.group(1))+'`',notation)
notation=re.sub(r'\|\n(?:[ \t]*\n)+(?=\|)', '|\n', notation)
(ROOT/f'{PREFIX}_doubts.md').write_text(notation+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations\n\nExpansions appear only in this list.\n\n'+table(['Scan','As written','Probable expansion'],abbr)+'\n## Legibility and witnesses\n\n'+leg+'\n')
(ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join((ROOT/'pages'/r['filename']).read_text().rstrip()+'\n' for r in records))
# Historical counts retain their named evidence; no root_crop_audit is invented.
HISTORICAL_ROOT_CROP_COUNTS = {
    2: (2, 0, 2, 'Historical reported totals; records/scan002.json /workflow_note'),
    3: ('not fully recorded', 12, 'not fully recorded', 'Partial historical report; checks/scan003_main_decisions.md:3,31 and crops/003/manifest.json; total/reused not fully recorded'),
    4: (35, 16, 19, 'Historical reported totals; records/scan004.json /workflow_note and checks/scan004_main_decisions.md:3'),
    5: (12, 2, 10, 'Historical journal path enumeration; checks/scan005_main_decisions.md Viewed crop table; corroborated by records/scan005.json'),
    6: (25, 5, 20, 'Historical successful-path list; checks/scan006_main_decisions.md Successfully viewed evidence; corroborated by records/scan006.json'),
    7: (3, 1, 2, 'Historical successful-path sentence; checks/scan007_main_decisions.md:3; corroborated by records/scan007.json'),
    8: (15, 3, 12, 'Historical journal path enumeration; checks/scan008_main_decisions.md Crop table; corroborated by records/scan008.json'),
    10: (17, 2, 15, 'Historical crop-manifest enumeration; crops/010/manifest.json and checks/scan010_main_decisions.md:3'),
    11: (20, 6, 14, 'Historical crop-manifest enumeration; crops/011/manifest.json and checks/scan011_main_decisions.md:32'),
    12: (32, 18, 14, 'Historical crop-manifest enumeration; crops/012/manifest.json, records/scan012.json /workflow_note, and checks/scan012_main_decisions.md'),
}

def root_crop_counts(scan):
    audit_path = ROOT/'checks'/f'scan{scan:03d}_root_crop_audit.json'
    if not audit_path.exists():
        return HISTORICAL_ROOT_CROP_COUNTS.get(
            scan, ('not recorded', 'not recorded', 'not recorded',
                   'No formal root crop audit or reviewed historical count; observations retained.'))
    audit = json.loads(audit_path.read_text())
    if audit.get('scan') != scan:
        raise ValueError(f'Root crop audit scan mismatch: {audit_path}')
    fields = [key for key in ('images', 'viewed_once') if key in audit]
    if len(fields) != 1 or not isinstance(audit[fields[0]], list):
        raise ValueError(f'Root crop audit needs one recognized success array: {audit_path}')
    seen = {}
    for row in audit[fields[0]]:
        count = row.get('successful_display_count')
        if type(count) is not int or count < 0:
            raise ValueError(f'Unspecified successful-display count: {audit_path}')
        if count == 0:
            continue
        crop = row['path']
        if crop.startswith(f'crops/{scan:03d}/') or crop.startswith(f'crops/scan{scan:03d}_'):
            owner = 'root'
        elif crop.startswith(f'readers/{scan:03d}/'):
            owner = crop.split('/')[2]
            if owner not in ('A', 'B', 'C'):
                raise ValueError(f'Unclassified recorded reader crop: {crop!r}')
        else:
            raise ValueError(f'Unclassified exact recorded root crop path: {crop!r}')
        if 'created_by_root' in row and (
                type(row['created_by_root']) is not bool
                or row['created_by_root'] != (owner == 'root')):
            raise ValueError(f'Conflicting crop creator field: {crop!r}')
        identity = (row.get('sha256'), owner)
        if crop in seen and seen[crop] != identity:
            raise ValueError(f'Conflicting repeated crop-path record: {crop!r}')
        seen[crop] = identity
    totals = collections.Counter(owner for _, owner in seen.values())
    total = len(seen)
    for key in ('total_distinct', 'successful_distinct_crops'):
        if key in audit and audit[key] != total:
            raise ValueError(f'Declared root crop total differs from successful paths: {audit_path}')
    reused = sum(totals[role] for role in ('A', 'B', 'C'))
    evidence = (f'Formal audit: checks/{audit_path.name}; {fields[0]} successful paths; '
                f'reused A {totals["A"]}, B {totals["B"]}, C {totals["C"]}.')
    return total, totals['root'], reused, evidence

workflow=['# SP40_CW_81 — reading workflow\n',
    'Scans are processed in the page-map order. Each scan has three fresh readers (A, B, C-reader), started without conversation history and restricted to that scan, its two witnesses, conventions, and the current notation snapshot. C-reader is a role name; witness C is the prior Codex transcription. Each reader views the whole image once and each supplied half once, then crops unresolved loci. The main reader compares returns and views crops for adjudication. No OCR or external research is used. Root retains returns and adjudication crops. Reader directories preserve the independent page proposals, evidence, and crop metadata.\n',
    '## Model and effort\n\nMain reader and subreaders: GPT-6 Astra Pro / inherited model configuration. The runtime does not expose a separately verifiable numerical reasoning-effort setting; none is invented in this record.\n',
    '## Per-page record\n',
    'Root crop columns count distinct successfully displayed local crop paths. Formal audit rows require a positive successful_display_count; each exact recorded path contributes once. Recorded crops/NNN/ and crops/scanNNN_ paths identify root-created crops, and readers/NNN/A, B or C paths identify reused reader crops; an explicit created_by_root field must agree. Failed unseen attempts contribute no successful path, and their later successful retries contribute that path once. Earlier entries retain their named historical report, journal or manifest basis; incomplete totals remain explicit. The existing observations, brief texts and assessment retain their historical wording.\n']
wrows=[]
for r in records:
    counts={}
    for role in ['A','B','C']:
        path=ROOT/'readers'/f"{r['scan']:03d}"/role/'report.json'
        if path.exists():counts[role]=len(json.loads(path.read_text()).get('crops',[]))
    root_total,root_created,root_reused,root_basis=root_crop_counts(r['scan'])
    wrows.append([r['scan'],r.get('brief_version','v01'),counts.get('A','?'),counts.get('B','?'),counts.get('C','?'),root_total,root_created,root_reused,root_basis,r.get('workflow_note','')])
workflow.append(table(['Scan','Brief','A crops','B crops','C-reader crops','Root crops shown (distinct)','Root-created shown','Reader crops reused by root','Root count evidence','Observations'],wrows))
workflow.append('\n## Brief versions\n')
for p in sorted((ROOT/'briefs').glob('brief*.md')):workflow.append(f'\n### {p.name}\n\n'+p.read_text())
if (ROOT/'workflow_assessment.md').exists():workflow.append('\n## Assessment\n\n'+(ROOT/'workflow_assessment.md').read_text())
(ROOT/f'{PREFIX}_workflow.md').write_text('\n'.join(workflow)+'\n')
print(json.dumps({'decided_scans':[r['scan'] for r in records],'C_loci':tot['C'],'H_loci':tot['H'],'inventory_rows':len(inventory),'doubt_loci':len(doubts)},ensure_ascii=False))
