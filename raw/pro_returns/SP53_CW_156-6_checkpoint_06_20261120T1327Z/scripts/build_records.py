"""Render adjudicated records. Never decides a manuscript reading."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,csv,re,hashlib,sys

OUT=Path(__file__).resolve().parents[1]
PREFIX='SP53_CW_156-6'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def cell(v):
    if isinstance(v,(list,dict)): v=json.dumps(v,ensure_ascii=False)
    return str(v if v is not None else '—').replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(cell(x) for x in row)+' |' for row in rows])+'\n'
def write_tsv(path,fields,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore'); w.writeheader();w.writerows(rows)
def reports(n):
    return [json.loads((OUT/f'readers/scan{n:03}/R{i}/report.json').read_text()) for i in range(1,4)]

def explicit_alternatives(u):
    """Expose existing candidates in the table; never infer a new reading."""
    s=u['reading']; groups=[]; pos=0
    while True:
        start=s.find(r'\unsure{',pos)
        if start<0:break
        j=start+len(r'\unsure{'); begin=j; depth=0; parts=[]; part=j
        while j<len(s):
            ch=s[j]; escaped=j>0 and s[j-1]=='\\'
            if ch=='{' and not escaped:depth+=1
            elif ch=='}' and not escaped:
                if depth==0:
                    parts.append(s[part:j]);break
                depth-=1
            elif ch=='|' and depth==0:
                parts.append(s[part:j]);part=j+1
            j+=1
        if j==len(s):break
        groups.append(parts);pos=j+1
    if groups:
        if len(groups)==1:
            return ' / '.join(groups[0][1:]) if len(groups[0])>1 else 'No alternative reading securely recovered.'
        return '; '.join(g[0]+': '+(' / '.join(g[1:]) if len(g)>1 else 'no alternative securely recovered') for g in groups)
    if 'extra upright' in s and 'live/canceled' in s:
        return 'Extra upright live / extra upright canceled (both drawn at the same position).'
    return u.get('alternatives','—')

def build():
    ds=[json.loads(p.read_text()) for p in sorted((OUT/'decisions').glob('scan[0-9][0-9][0-9].json')) if json.loads(p.read_text()).get('committed')]
    changes=['# Consolidated changes — cote 156-6, scans 006–033','',
      'Each row records one locus. Counts exclude equivalent LaTeX syntax. The high/medium/low columns count distinct loci; a locus may differ from both C and H and is counted only once in those confidence columns. Removing or changing a doubt mark is counted against C; retained doubts are recorded separately. Reader disagreements are retained in the reader columns. The manuscript remains the authority, including where its literal wording appears mathematically mistaken.','']
    counts=[]; total=Counter(); consequential=[]; coll=[]; inv=[]; doubts=[]; notes=['# Notes while reading','','These notes concern only the supplied pages and attached evidence. A synopsis of an assertion is not a verification of it. CHECK_EVENTS.tsv distinguishes the actual work performed.','']; events=[]; abbrev={}; crops=[]
    for d in ds:
        n=d['scan']; rows=d.get('differences',[]); c=Counter({'C':sum(bool(r.get('against_C')) for r in rows),'H':sum(bool(r.get('against_H')) for r in rows)})
        c.update(r.get('confidence','medium') for r in rows);total.update(c)
        counts.append([f'{n:03}',c['C'],c['H'],c['high'],c['medium'],c['low']])
        for r in rows:
            if r.get('mathematical'): consequential.append(f"- Scan {n:03}, {r['place']}: {r.get('mathematical') if isinstance(r.get('mathematical'),str) else r['final']}.")
            if r.get('against_H'):
                coll.append({'folder':d['folder'],'their_page':n-1,'our_scan':n,'line':r['place'],'their_reading':r.get('h',''),'codex_reading':r.get('c',''),'final_reading':r['final'],'scan_shows':r['evidence']+((' [crop: '+str(r['crop'])+']') if r.get('crop') else ''),'kind':r.get('kind','other'),'marked_in_H':r.get('marked_in_H','no'),'confidence':r.get('confidence','medium')})
        inv.extend([dict(scan=n,**x) for x in d['inventory']])
        for u in d.get('unresolved',[]): doubts.append([f'{n:03}',u['place'],u['reading'],explicit_alternatives(u),u.get('confidence','medium'),u.get('evidence','')])
        for a in d.get('abbreviations',[]): abbrev[a['form']]=a['expansion']
        no=d['notes']; notes.extend([f'## Scan {n:03} — manuscript page {d.get("mspage",n-1)}','',no.get('content',''),''])
        for field,title in [('math_reading_decisions','Mathematics and reading decisions'),('author_doubts','Authorial checks and reservations'),('titles_dates_counts','Titles, dates and counts')]:
            val=no.get(field,'None.'); notes.extend([f'**{title}.** '+ ('; '.join(val) if isinstance(val,list) else str(val)),''])
        for e in d.get('check_events',[]): events.append(dict(statement_id=e['statement_id'],date=e.get('date',d['finished_utc']),who=e.get('who',f'GPT-6 Astra Pro; effort not exposed; main reader; scan {n:03}'),type=e['type'],outcome=e['outcome']))
        rp=reports(n); nums=[len(list((OUT/f'readers/scan{n:03}/R{i}').rglob('*.jpg')))+len(list((OUT/f'readers/scan{n:03}/R{i}').rglob('*.png'))) for i in range(1,4)]
        main=len({p.resolve() for base in [OUT/f'crops/scan{n:03}',OUT/f'main_crops/scan{n:03}'] for ext in ['*.jpg','*.png'] for p in base.rglob(ext)})
        crops.append([f'{n:03}',d.get('brief','v001'),*nums,main,sum(nums)+main])
    counts.append(['Total',total['C'],total['H'],total['high'],total['medium'],total['low']])
    changes.extend([table(['Scan','Against C','Against H','High','Medium','Low'],counts),'## Consequential corrections','',*consequential,''])
    for d in ds:
        n=d['scan']; changes.extend([f'## Scan {n:03} — manuscript page {d.get("mspage",n-1)}',''])
        tab=[]
        for r in d.get('differences',[]):
            rr=r.get('readers',{});e=r['evidence']+((' Crop: `'+str(r['crop'])+'`.') if r.get('crop') else '')
            tab.append([r['place'],r.get('c','—'),r.get('h','—'),r['final'],rr.get('R1','—'),rr.get('R2','—'),rr.get('R3','—'),e,r.get('confidence','medium')])
        changes.extend([table(['Place','C','H','Final','Reader 1','Reader 2','Reader 3','Ink / decision','Confidence'],tab) if tab else 'No substantive difference.',''])
        if d.get('adjudications'):
            changes.extend(['### Reader disagreements without a final witness change','',table(['Place','Reader 1','Reader 2','Reader 3','Final','Ink / decision'],[[x['place'],x['readers'].get('R1','—'),x['readers'].get('R2','—'),x['readers'].get('R3','—'),x['final'],x['evidence']+((' Crop: `'+x['crop']+'`.') if x.get('crop') else '')] for x in d['adjudications']]),''])
        if d.get('c_doubts'):
            changes.extend(['### Witness C doubt marks reviewed','',table(['Place','C','Final','Status','Evidence'],[[x['place'],x.get('c',''),x['reading'],x['disposition'],x['evidence']+((' Crop: `'+x['crop']+'`.') if x.get('crop') else '')] for x in d['c_doubts']]),''])
        if d.get('s_rows'):
            changes.extend(['### Witness S rows reviewed','',table(['S row','Decision','Literal reading','Evidence'],[[x['id'],x['disposition'],x['reading'],x['evidence']] for x in d['s_rows']]),''])
        changes.extend(['### Unresolved places','',table(['Place','Reading','Alternatives','Confidence'],[[u['place'],u['reading'],explicit_alternatives(u),u.get('confidence','medium')] for u in d.get('unresolved',[])]) if d.get('unresolved') else 'None.',''])
    (OUT/f'{PREFIX}_changes.md').write_text('\n'.join(changes))
    write_tsv(OUT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    write_tsv(OUT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
    (OUT/f'{PREFIX}_notes.md').write_text('\n'.join(notes))
    doubt_text=(OUT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Evidence'],doubts)+'\n## Abbreviations\n\nExpansions here are explanatory only and do not replace manuscript abbreviations.\n\n'+table(['Form','Likely expansion'],sorted(abbrev.items()))
    leg=(OUT/'legibility.md');doubt_text+='\n## Legibility and witnesses\n\n'+(leg.read_text() if leg.exists() else 'Assessment in progress; see the page-specific decisions and remaining doubts.\n')
    (OUT/f'{PREFIX}_doubts.md').write_text(doubt_text)
    write_tsv(OUT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    workflow=['# Reading workflow','','Three independent fresh subagents were used for each committed page, in scan order. Each received only that page’s packet, the conventions and the current notation table. The main reader compared their complete returns and adjudicated disagreements from targeted crops. Page finalization preceded the next set of readers. No OCR or outside research was used.','','## Brief versions','']
    for b in sorted((OUT/'briefs').glob('v*.md')):workflow.extend([f'### {b.name}','',b.read_text(),''])
    revisions=OUT/'briefs/changes.md'
    if revisions.exists():workflow.extend(['## Reasons for revisions','',revisions.read_text(),''])
    workflow.extend(['## Actual crops per page','','Counts include separate crops made independently by different readers. Supplied whole pages and halves are not crops in this table. The main reader may adjudicate from a reader’s existing crop without creating another.','',table(['Scan','Brief','R1','R2','R3','Main','Total'],crops),''])
    review=OUT/'workflow_review.md'
    if review.exists():workflow.extend(['## What worked and what did not','',review.read_text()])
    (OUT/f'{PREFIX}_workflow.md').write_text('\n'.join(workflow))
    (OUT/f'{PREFIX}_transcription.tex').write_text('\\cotefile{156-6}\n\n'+'\n\n'.join((OUT/'pages'/d['filename']).read_text().strip() for d in ds)+'\n')
    print(json.dumps({'committed_scans':[d['scan'] for d in ds],'against_C':total['C'],'against_H':total['H'],'inventory_elements':len(inv),'remaining_doubts':len(doubts)},ensure_ascii=False))

def commit(n):
    p=OUT/f'decisions/scan{n:03}.json';d=json.loads(p.read_text())
    if d.get('committed'): raise SystemExit('Already committed')
    rp=reports(n)
    for r in rp:
        assert int(r['scan'])==n
        assert r.get('status')=='complete', (n,r.get('reader'),'incomplete report')
        assert (OUT/f"readers/scan{n:03}/{r['reader']}/reading.tex").exists()
    prior=sorted(int(x.stem[4:]) for x in (OUT/'decisions').glob('scan[0-9][0-9][0-9].json') if json.loads(x.read_text()).get('committed'))
    assert prior==list(range(6,n)),prior
    assert all(x['transcribed']=='yes' for x in d['inventory'])
    assert d.get('adjudicated_all'), 'Main reader has not signed off all loci'
    for row in d.get('differences',[]):
        assert isinstance(row['against_C'],bool) and isinstance(row['against_H'],bool),row['id']
        assert row['confidence'] in ('high','medium','low'),row['id']
        assert row.get('marked_in_H') in ('yes','no'),row['id']
        assert all(k in row.get('readers',{}) for k in ('R1','R2','R3')),row['id']
        assert row.get('crop') and (OUT/row['crop']).exists(),row['id']
    final=(OUT/f'decisions/scan{n:03}_final.tex').read_text()
    assert f'\\scanpage{{{n}}}' in final
    (OUT/'pages'/d['filename']).write_text(final)
    d['committed']=True;d['finished_utc']=utc();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    build()
    with (OUT/'progress.log').open('a') as f:f.write(f'scan {n:03} done {d["finished_utc"]}\n')

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='commit':commit(int(sys.argv[2]))
    else:build()
