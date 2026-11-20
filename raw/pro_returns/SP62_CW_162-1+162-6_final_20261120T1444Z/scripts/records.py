"""Build the apparatus from the reader's explicit, image-grounded decisions.

This script performs no OCR, inference, witness alignment, or reading decisions.
The records are an editable documentary ledger; generated tables are not
independent evidence for the readings.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, collections

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP62_CW_162-1+162-6'

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def page(cote, scan):
    folder = 'H162-01' if cote == '162-1' else 'H162-02'
    return dict(cote=cote, scan=scan, folder=folder, their_page=scan-1,
                filename=f'{folder}_{cote}_scan{scan:03d}.tex',
                changes=[], doubts=[], certainty=[], inventory=[], notation=[],
                hand=[], abbreviations=[], notes=[], checks=[], audit=[])

def change(p, place, c, h, final, shows, kind, confidence='high', against='CH', marked_h='no', error_kind=None):
    p['changes'].append(dict(place=place, c=c, h=h, final=final, shows=shows,
                            kind=kind, confidence=confidence, against=against,
                            marked_h=marked_h, error_kind=error_kind or kind))

def inventory(p, kind, position, text, sheet_kind='list', hand='his hand'):
    p['inventory'].append(dict(kind=kind, position=position, text=text, sheet_kind=sheet_kind, hand=hand))

def doubt(p, place, reading, alternatives, confidence, reason):
    p['doubts'].append([place, reading, alternatives, confidence, reason])

def certainty(p, place, before, after, reason):
    p['certainty'].append([place,before,after,reason])

def save(p, tex=None, done=True):
    if tex is not None:
        (ROOT/'pages'/p['filename']).write_text(tex.rstrip()+'\n', encoding='utf-8')
    if done and 'done' not in p:
        p['done'] = utc()
        with (ROOT/'progress.log').open('a') as f:
            f.write(f"scan {p['scan']:03d} done {p['done']} cote {p['cote']}\n")
    (ROOT/'records'/f"{p['cote']}_{p['scan']:03d}.json").write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
    build()

def esc(v):
    return str(v).replace('|','&#124;').replace('\n','<br>')

def table(head, rows):
    return '\n'.join(['| '+' | '.join(map(esc,head))+' |', '| '+' | '.join(['---']*len(head))+' |']+
                     ['| '+' | '.join(map(esc,r))+' |' for r in rows])+'\n'

def write_tsv(path, headers, rows, delim='\t'):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,delimiter=delim); w.writerow(headers); w.writerows(rows)

def build():
    pages=[json.loads(x.read_text()) for x in sorted((ROOT/'records').glob('*.json'))]
    if not pages: return
    changes=['# Changes against witnesses C and H\n',
             'Counts refer to localized substantive differences, including wording, source punctuation, and deletion or placement. A row may differ from both witnesses. Multiple letter corrections within one tightly connected passage form one place. Certainty-only decisions are listed in the doubts file and are not counted here. Macro syntax and editorial metadata are excluded. Confidence concerns the final reading, not witness reliability. Scan labels include the cote to disambiguate repeated scan numbers. Pixel boxes refer to the supplied whole-page JPG, origin at its upper left. Where the halves decided a reading, no crop was made.\n']
    counts=[]; totals=collections.Counter(); witness_counts=[]; witness_totals=collections.Counter()
    for p in pages:
        rows=p['changes']; n=collections.Counter(x['confidence'] for x in rows)
        nc=sum('C' in x['against'] for x in rows); nh=sum('H' in x['against'] for x in rows)
        counts.append([f"{p['cote']}/{p['scan']:03d}",len(rows),nc,nh,n['high'],n['medium'],n['low']])
        totals.update(dict(places=len(rows),C=nc,H=nh,**n))
        wc=collections.Counter((w,x['confidence']) for x in rows for w in 'CH' if w in x['against'])
        witness_counts.append([f"{p['cote']}/{p['scan']:03d}"]+[wc[(w,c)] for w in 'CH' for c in ['high','medium','low']])
        witness_totals.update(wc)
    counts.append(['Total',totals['places'],totals['C'],totals['H'],totals['high'],totals['medium'],totals['low']])
    changes.append(table(['Scan','Places','Against C','Against H','High','Medium','Low'],counts))
    witness_counts.append(['Total']+[witness_totals[(w,c)] for w in 'CH' for c in ['high','medium','low']])
    changes.append(table(['Scan','C high','C medium','C low','H high','H medium','H low'],witness_counts))
    consequences=ROOT/'consequential.txt'
    changes.append('## Consequential corrections\n\n'+(consequences.read_text() if consequences.exists() else 'No mathematical inference has been corrected. Bibliographic numerals, technical terms, and source deletion states are documented below.\n'))
    crops=list(csv.DictReader((ROOT/'crop_register.tsv').open(),delimiter='\t')) if (ROOT/'crop_register.tsv').exists() else []
    collation=[]; inv=[]; doubts=[]; certainty_rows=[]; notation=[]; hand=[]; abbr=[]; notes=['# Notes made while reading\n\nThese notes use only the supplied scans and witnesses; no outside source was consulted. A title or assertion recorded in a list is not independently verified. The few conditional mathematical checks are stated explicitly, with their assumptions and limits, and recorded separately in CHECK_EVENTS.tsv. Reading the ink is not a proof check.\n']; checks=[]; audit=['# Second reading\n']
    for p in pages:
        label=f"{p['cote']}/{p['scan']:03d}"
        changes.append(f'## {label}\n')
        changes.append(table(['ID / place','C','H','Final','What the scan shows / crop','Confidence'],[
            [f"{label}-{i:02d}: {x['place']}",x['c'],x['h'],x['final'],x['shows'],x['confidence']]
            for i,x in enumerate(p['changes'],1)]))
        changes.append('### Remaining unresolved places\n\n'+('\n'.join(f"- {x[0]}: `{x[1]}`; alternatives: {x[2]}. {x[4]}" for x in p['doubts']) or 'None.')+'\n')
        pc=[x for x in crops if x['source']==p['filename'].replace('.tex','.jpg')]
        changes.append('### Crop register\n\nEach listed place was cropped once from the supplied whole-page image. Reinspection during the second reading used the existing crop. Coordinates are (x0, y0, x1, y1); rotation is counterclockwise. These are an evidence register, not additional counted differences.\n\n'+table(['Place','Original-pixel box','Rotation (degrees)','Created (UTC)'],[[x['place'],'('+','.join(x[k] for k in ['x0','y0','x1','y1'])+')',x['rotation_ccw_degrees'],x['time_UTC']] for x in pc]))
        for x in p['changes']:
            if 'H' in x['against']:
                collation.append([p['folder'],p['their_page'],p['scan'],x['place'],x['h'],x['c'],x['final'],x['shows'],x['kind'],x['marked_h'],x['confidence']])
        for i,x in enumerate(p['inventory'],1):
            inv.append([label,x['sheet_kind'],x['hand'],f"{label}-E{i:02d}",x['kind'],x['position'],x['text'],'yes'])
        doubts.extend([[label]+x for x in p['doubts']]); certainty_rows.extend([[label]+x for x in p['certainty']])
        notation.extend([[label]+x for x in p['notation']]); hand.extend([[label]+x for x in p['hand']]); abbr.extend([[label]+x for x in p['abbreviations']])
        notes.append(f'## {label}\n\n'+'\n\n'.join(f"**{label}-N{i:02d}.** {x}" for i,x in enumerate(p['notes'],1))+'\n')
        for i,x in enumerate(p['notes'],1):
            sid=f'{label}-N{i:02d}'
            if not any(e[0]==sid for e in p['checks']):
                checks.append([sid,p.get('done','').split(' ')[0], 'GPT-6 Astra Pro; effort not exposed; SP62 second pass; /root', 'carried as background without fault found','Documentary account from this scan; no independent verification of a borrowing, bibliographic identity, or mathematical assertion is claimed. '+x])
        checks.extend(p['checks'])
        if p['audit']: audit.append(f'## {label}\n\n'+'\n\n'.join(p['audit'])+'\n')
    (ROOT/f'{PREFIX}_changes.md').write_text('\n'.join(changes))
    write_tsv(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    write_tsv(ROOT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
    readability=ROOT/'readability.txt'
    d=['# Notation table\n',table(['Scan','Sign or convention','Reading and visible basis'],notation),'## Remaining doubts\n',table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts),'## Certainty-only decisions against C\n\nThese do not create changes-log or collation rows when the underlying reading is unchanged.\n',table(['Scan','Place','C doubt','Disposition','Ink'],certainty_rows),'## Abbreviations\n\nExpansions are interpretive and are confined to this table.\n',table(['Scan','Written form','Possible expansion'],abbr),'## Legibility and comparison of witnesses\n',readability.read_text() if readability.exists() else 'Assessment in progress; remaining uncertainty is explicitly recorded above.\n']
    (ROOT/f'{PREFIX}_doubts.md').write_text('\n'.join(d))
    (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand and notation log\n\nScope statements concern only the indicated observed occurrences; they are not claims about all of Grothendieck’s writing.\n\n'+table(['Scan(s)','Habit','Extent / exceptions','Witness errors or risks'],hand))
    (ROOT/f'{PREFIX}_notes.md').write_text('\n'.join(notes))
    write_tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    (ROOT/f'{PREFIX}_audit.md').write_text('\n'.join(audit))
    taxonomy={'misread symbol or index':1,'misread word':2,'omission':3,'drawing or diagram':4,'readable ink left as \\ill{}':5,'insertion or placement':6,'deletion state (struck given live or live given struck)':7,'abbreviation expanded or spelling modernised':8,'text not on the page':9,'other':10}
    ec=collections.Counter(); locations=collections.defaultdict(list)
    for p in pages:
        for i,x in enumerate(p['changes'],1):
            k=taxonomy.get(x['error_kind'],10); ec[k]+=1; locations[k].append(f"{p['cote']}/{p['scan']:03d}-{i:02d}")
    labels=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertion placement','Struck text / deletion state','Expansion / spelling modernization','Text not on the page','Other']
    feedback='# Feedback on the error sheet\n\nOne primary class per substantive localized difference is counted below. These are counts against either witness, not an estimate of all defects in either complete witness. An entire omitted entry is one place; recoverable words explicitly left illegible are class 5. Certainty-only changes are excluded. Source marks such as boxed numerals are distinguished from cancellation.\n\n'+table(['Class','Kind','Places','Locations'],[[i,labels[i-1],ec[i],'; '.join(locations[i]) or 'none'] for i in range(1,11)])
    feedback+='\n## Additional recurring patterns\n\nNo new error family outside the supplied ten classes was established. The following recurring subcases deserve explicit attention:\n\n- Serif caps and feet misclassified as cancellation: 162-1/005 (XXI), 162-1/008 (VII/XII), 162-1/009 (XVIII). A bar through the numeral must be distinguished from its top and bottom strokes.\n- Familiar names or titles substituted for the actual outline: 162-1/006 (Woodshole, Finiteness Theorems), 162-1/007 (Bon/Bou/Bass, Theodoros, Bardach), 162-1/010 (Lascou, Gèbres, Brieskorin). These remain word/normalization errors, not bibliographic identifications.\n- Faint text falsely described as outside the sheet: 162-6/003 (bottom product and equals sign), 162-6/006 (complete bottom parenthesis and lower jotting). Both positions contain visible writing inside the page boundary.\n- Editorial prose substituted for source geometry: 162-6/002 (field labels and divider), 162-6/003 (bracket and oval), 162-6/004 (norm-arrow endpoint and open contour), 162-6/006 (diagonals and equality connection). These are counted under the existing drawing/diagram or omission classes.\n'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
    # Assembly has no preamble and retains each page's original name.
    combined=[]; last=None
    for p in pages:
        if p['cote']!=last: combined.append('\\cotefile{'+p['cote']+'}\n'); last=p['cote']
        combined.append((ROOT/'pages'/p['filename']).read_text())
    (ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(combined))

if __name__=='__main__': build()
