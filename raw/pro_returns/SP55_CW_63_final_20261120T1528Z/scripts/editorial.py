"""Editorial bookkeeping only. All readings, crops, and decisions are supplied by the human-facing primary model; no OCR."""
from pathlib import Path
import csv, json, collections, hashlib
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'input' / 'SP55_CW_63_witnesses'
PREFIX = 'SP55_CW_63'
ORDER = list(range(21,35)) + list(range(41,53))
ERROR_SHEET_CATEGORIES = (
    'Symbols and indices',
    'Words',
    'Omissions',
    'Drawings and diagrams',
    'Readable ink left as illegible',
    'Insertions put in the wrong place',
    'Struck text',
    'Abbreviations expanded, spelling modernised',
    'Text that is not on the page',
    'Other',
)
ROW_KIND_TO_ERROR_SHEET = {
    'misread symbol or index': 'Symbols and indices',
    'misread word': 'Words',
    'omission': 'Omissions',
    'drawing or diagram': 'Drawings and diagrams',
    'drawing': 'Drawings and diagrams',
    r'readable ink left as \ill{}': 'Readable ink left as illegible',
    r'readable ink left as `\ill{}`': 'Readable ink left as illegible',
    'insertion or placement': 'Insertions put in the wrong place',
    'deletion state (struck given live or live given struck)': 'Struck text',
    'deletion state': 'Struck text',
    'abbreviation expanded or spelling modernised': 'Abbreviations expanded, spelling modernised',
    'text not on the page': 'Text that is not on the page',
    'other': 'Other',
}
MAP = {int(r['our_scan']):r for r in csv.DictReader((SOURCE/'page_map.tsv').open(), delimiter='\t')}

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def log(s):
    with (ROOT/'progress.log').open('a') as f: f.write(s+'\n')

def row(place,c,h,final,evidence,confidence='high',kind='other',against_c=True,against_h=False,crop=None,consequential=False):
    kind={'drawing':'drawing or diagram'}.get(kind,kind)
    return dict(place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,crop=crop,consequential=consequential)

def commit(scan, *, replacements=(), tex=None, changes=(), doubts=(), certainty=(), inventory=(), notes='', notation=(), hand=(), checks=(), crops=(), sheet_kind='typescript', default_hand='typewriter'):
    m=MAP[scan]
    if tex is None:
        tex=(SOURCE/m['codex_file']).read_text()
        for before, after in replacements:
            if before not in tex: raise ValueError(f'scan {scan}: replacement absent: {before}')
            tex=tex.replace(before,after)
    if scan==ORDER[0] and '\\cotefile{63}' not in tex: tex='\\cotefile{63}\n'+tex
    if scan!=ORDER[0]: tex=tex.replace('\\cotefile{63}\n','')
    tex=tex.replace('\\makeatletter\\tagsleft@true\\makeatother\n','')
    p=ROOT/'pages'/Path(m['codex_file']).name
    p.write_text(tex.rstrip()+'\n')
    record=dict(scan=scan,map=m,changes=list(changes),doubts=list(doubts),certainty=list(certainty),inventory=list(inventory),notes=notes,notation=list(notation),hand=list(hand),checks=list(checks),crops=list(crops),sheet_kind=sheet_kind,default_hand=default_hand,done=utc())
    (ROOT/'records'/f'scan{scan:03}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    build()
    log(f'scan {scan:03} done {record["done"]}')
    print(f'scan {scan:03} saved; {len(changes)} comparison rows, {len(doubts)} unresolved entries')

def esc(s):
    return str(s).replace('|','&#124;').replace('\n','<br>')

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(esc(x) for x in r)+' |' for r in rows])+'\n'

def write_tsv(path, headers, rows):
    with path.open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n'); w.writerow(headers); w.writerows(rows)

def error_sheet_counts(rows):
    """One principal error-sheet category per logged place, with zero rows retained."""
    counts={category:[0,0,0] for category in ERROR_SHEET_CATEGORIES}
    for record,change in rows:
        kind=change['kind']
        if kind not in ROW_KIND_TO_ERROR_SHEET:
            raise ValueError(f'Unmapped error-sheet kind: {kind!r}')
        category=ROW_KIND_TO_ERROR_SHEET[kind]
        counts[category][0]+=1
        counts[category][1]+=bool(change.get('against_c'))
        counts[category][2]+=bool(change.get('against_h'))
    result=[[category,*counts[category]] for category in ERROR_SHEET_CATEGORIES]
    result.append(['TOTAL',*[sum(row[column] for row in result) for column in (1,2,3)]])
    return result

def build():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
    rows=[(r,c) for r in records for c in r['changes']]
    combined='\n'.join((ROOT/'pages'/Path(r['map']['codex_file']).name).read_text().rstrip() for r in records)+'\n'
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
    counts=[]
    for r in records:
        c=r['changes']; conf=collections.Counter(x['confidence'] for x in c)
        counts.append([r['scan'],sum(x['against_c'] for x in c),sum(x['against_h'] for x in c),len(c),conf['high'],conf['medium'],conf['low']])
    totals=['TOTAL']+[sum(v[i] for v in counts) for i in range(1,7)]
    out='# SP55_CW_63 — changes from the witnesses\n\nThe images are the authority. Rows count substantive reading or state/placement differences. A row can differ from both witnesses; the distinct-place total is therefore not the sum of the two witness columns. Certainty-only resolutions are recorded in the doubts file, not counted here. H descriptions are not source transcriptions and have no collation rows. No OCR or outside text was used.\n\n## Counts\n\n'
    out+=table(['Scan','Against C','Against H','Distinct places','High','Medium','Low'],counts+[totals])
    out+='\n## Consequential corrections\n\nThe list includes mathematical content absent from H on its partially transcribed pages. Such omissions do not mean that C had the same gap. The source’s own mathematical slips are preserved and discussed in the notes.\n\n'
    consequential=[f'- Scan {r["scan"]}, {c["place"]}: {c["final"]}. {c["evidence"]}' for r,c in rows if c.get('consequential')]
    out+='\n'.join(consequential) if consequential else 'No consequential correction recorded.'
    collation=[]
    for r in records:
        out+=f'\n\n## Scan {r["scan"]:03} ({r["map"]["folder"]}; H page {r["map"]["their_page"]}; H {r["map"]["hua_has"]})\n\n'
        tab=[]
        for c in r['changes']:
            e=c['evidence']+(f'; crop scan {r["scan"]} original pixels {tuple(c["crop"])}' if c.get('crop') else ('; settled during the second image reading' if c.get('stage') else '; settled from the full-resolution halves'))
            tab.append([c['place'],c['c'],c['h'],c['final'],e,c['confidence']])
            if c['against_h']:
                collation.append([r['map']['folder'],r['map']['their_page'],r['scan'],c['place'],c['h'],c['c'],c['final'],e,c['kind'],c.get('marked_in_h','no'),c['confidence']])
        out+=table(['Place','C','H','Final','What the scan shows','Confidence'],tab) if tab else 'No substantive difference recorded.\n'
        
        if r.get('crops'): out+='\nCrops used (original whole-page pixels): '+('; '.join(str(x) for x in r['crops']))+'\n'
        out+='\nUnresolved: '+('; '.join(str(d[0])+': '+str(d[1]) for d in r['doubts']) if r['doubts'] else 'none.')+'\n'
        if r.get('audited'):
            out+='\nSecond image reading ('+r['audited']+'): '+r.get('audit_note','Completed.')+'\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(out)
    write_tsv(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    inv=[]
    for r in records:
        for i,e in enumerate(r['inventory'],1):
            kind,pos,first=e[:3]; hand=e[3] if len(e)>3 else r['default_hand']
            inv.append([r['scan'],r['sheet_kind'],hand,i,kind,pos,first,'yes'])
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']); w.writerows(inv)
    out='# SP55_CW_63 — doubts and notation\n\n## Notation table\n\n'
    global_notation=ROOT/'notation_global.json'
    notation_rows=json.loads(global_notation.read_text()) if global_notation.exists() else []
    out+=table(['Scan(s)','Sign or form','Reading and evidence'],notation_rows+[[r['scan'],*n] for r in records for n in r['notation']])
    out+='\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],[[r['scan'],*d] for r in records for d in r['doubts']])
    out+='\n## Certainty-only decisions\n\n'+table(['Scan','Place / former doubt','Decision and image evidence'],[[r['scan'],*c] for r in records for c in r['certainty']])
    extra=ROOT/'doubts_addendum.md'
    if extra.exists(): out+='\n'+extra.read_text()
    (ROOT/f'{PREFIX}_doubts.md').write_text(out)
    out='# SP55_CW_63 — notes made while reading\n\nThese notes describe these sheets only. A report of what a sheet states is not a proof check. Check events below are classified by what was actually done.\n'
    for r in records: out+=f'\n## Scan {r["scan"]:03}\n\n'+r['notes']+'\n'
    (ROOT/f'{PREFIX}_notes.md').write_text(out)
    checks=[]
    for r in records:
        for e in r['checks']: checks.append([e[0],r['done'][:10],'GPT-6 Astra Pro; effort not exposed; SP55_CW_63 second pass',*e[1:]])
    write_tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    out='# SP55_CW_63 — hand and machine log\n\nEntries are observations local to the specified pages, not assumptions about all manuscripts. Typewriter forms and manual additions are distinguished.\n\n'+table(['Scan(s)','Habit','Scope / exceptions','Witness consequences'],[[r['scan'],*h] for r in records for h in r['hand']])
    (ROOT/f'{PREFIX}_hand_log.md').write_text(out)
    out='# SP55_CW_63 — feedback on the error sheet\n\nCounts refer to distinct logged places, with exactly one principal error-sheet category per place. All ten categories are shown, including zeros. A place may differ from both witnesses, so Against C and Against H are not additive. Certainty-only decisions are reported separately in the doubts file.\n\n'+table(['Error-sheet kind','Places','Against C','Against H'],error_sheet_counts(rows))
    extra=ROOT/'sheet_feedback_addendum.md'
    if extra.exists(): out+='\n'+extra.read_text()
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(out)

if __name__=='__main__': build()
