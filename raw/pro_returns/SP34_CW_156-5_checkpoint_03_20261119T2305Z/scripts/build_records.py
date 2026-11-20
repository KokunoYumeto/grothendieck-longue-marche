#!/usr/bin/env python3
"""Assemble adjudicated records only; never infer a reading from a witness."""
from pathlib import Path
import csv, json, re, collections

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SP34_CW_156-5'

def cell(s):
    return str(s).replace('|', r'\|').replace('\n','<br>')

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |', '| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])+'\n'

def write_tsv(name, headers, rows, delimiter='\t'):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter=delimiter);w.writerow(headers);w.writerows(rows)

def inventory_kind(kind):
    """Export the prompt's seven categories; detailed source labels stay in decisions."""
    if kind in ('text','display','diagram','drawing','margin note','insertion','deletion'):
        return kind
    k=kind.lower().replace('_',' ')
    if 'margin' in k:return 'margin note'
    if 'insertion' in k:return 'insertion'
    if 'delet' in k or 'cancel' in k or 'overwrite' in k:return 'deletion'
    if 'diagram' in k:return 'diagram'
    if 'drawing' in k or 'pen mark' in k or 'pen stroke' in k:return 'drawing'
    if 'display' in k:return 'display'
    if any(x in k for x in ('text','heading','page number','underline','word','annotation','formula')):return 'text'
    raise ValueError('Unmapped inventory kind: '+kind)

def main():
    pages=[json.loads(p.read_text()) for p in sorted((ROOT/'decisions').glob('scan*.json'))]
    summaries=[];collation=[];inventory=[];checks=[];consequential=[]
    changes=[];notes=[];doubts=[];notation=[];abbreviations={}
    for d in pages:
        n=d['scan']; rows=d['rows']; c=sum(bool(r.get('against_C')) for r in rows);h=sum(bool(r.get('against_H')) for r in rows)
        conf=collections.Counter(r['confidence'] for r in rows if r.get('against_C') or r.get('against_H'))
        summaries.append([n,c,h,conf['high'],conf['medium'],conf['low']])
        changes+=['## Scan %03d (manuscript %s)\n'%(n,d.get('manuscript',n-1)), d.get('overview','')+'\n']
        changes.append(table(['ID / place','C','H','R1','R2','R3','Final reading','Ink / crop / decision','Confidence','Change flags'],
          [[r['id']+' / '+r['place'],r.get('C',''),r.get('H',''),*(r.get('readers',['','',''])),r['final'],r['ink']+' '+r.get('crop',''),r['confidence'],
            ', '.join((['C'] if r.get('against_C') else [])+(['H'] if r.get('against_H') else [])+([r['review_type']] if r.get('review_type') else [])) or 'review retained'] for r in rows]))
        changes.append('### Still unresolved\n\n'+('\n'.join('- '+x for x in d.get('unresolved',[])) or 'None.')+'\n')
        for r in rows:
            if r.get('against_H'):
                kind=r.get('kind','other')
                if kind=='readable ink left as \\ill{}':kind='readable ink left as `\\ill{}`'
                collation.append([d['folder'],n-1,n,r['place'],r.get('H',''),r.get('C',''),r['final'],r['ink']+' '+r.get('crop',''),kind,r.get('marked_in_H','no'),r['confidence']])
            if r.get('consequential'):consequential.append('- '+r['id']+': '+r['consequential'])
        for i,e in enumerate(d['inventory'],1):
            inventory.append([n,e.get('sheet_kind','text'),e.get('hand','his hand'),e.get('element',i),inventory_kind(e['kind']),e['position'],e['first_words_or_objects'],'yes'])
        notes+=['## Scan %03d — manuscript %s\n'%(n,d.get('manuscript',n-1)),d['notes']+'\n']
        for r in d.get('doubts',[]):doubts.append([n,r['place'],r['reading'],r.get('alternatives',''),r['confidence'],r.get('reason','')])
        notation.extend(d.get('notation',[]));abbreviations.update(d.get('abbreviations',{}))
        for e in d.get('checks',[]):checks.append([e['statement_id'],e['date'],e.get('who','GPT-6 Astra Pro; inherited effort (not exposed); SP34 second pass /root'),e['type'],e['outcome']])
    totals=["TOTAL"]+[sum(r[i] for r in summaries) for i in range(1,6)]
    intro='# Changes and adjudications\n\nThe scans are the authority. Each scan was read independently by R1, R2, and R3 before the main reader compared their reports and adjudicated the enlarged ink. Reader files are preserved under `readers/`. The three reader columns quote the submitted reading at each locus; they are not a majority vote.\n\nCounts are locus counts. A locus differing from both witnesses counts in both witness columns and once in the confidence columns. Removal, addition, or alteration of an uncertainty mark counts against C; syntax-only conversion between macro sets does not count. Retained C doubts and S reviews appear as review rows but do not inflate change counts.\n\n'
    intro+=table(['Scan','Against C','Against H','High','Medium','Low'],summaries+[totals])
    intro+='\n## Consequential decisions\n\n'+('\n'.join(consequential) or 'None recorded yet.')+'\n\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(intro+'\n'.join(changes))
    write_tsv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    write_tsv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    (ROOT/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nThese notes concern only scans 26–49 supplied with the task. A transcription reading is not a proof check. Actual checks, background use, and refutations are distinguished in `CHECK_EVENTS.tsv`. Mathematical corrections below never replace the written text.\n\n'+'\n'.join(notes))
    nt=table(['Sign or abbreviation','Form in the ink and LaTeX','Evidence','Remaining ambiguity'],[[r['sign'],r['form'],r['evidence'],r.get('ambiguity','')] for r in notation])
    dt=table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)
    ab=table(['Abbreviation','Probable expansion (not inserted in transcription)'],sorted(abbreviations.items()))
    closing=(ROOT/'documentation/legibility.md').read_text() if (ROOT/'documentation/legibility.md').exists() else 'This assessment is being built page by page; unresolved ink is marked in place.'
    (ROOT/f'{PREFIX}_doubts.md').write_text('# Notation table\n\n'+nt+'\n## Remaining doubts\n\n'+dt+'\n## Abbreviations\n\n'+ab+'\n## Legibility and witness comparison\n\n'+closing+'\n')
    files=[ROOT/'pages'/d['filename'] for d in pages]
    if files:(ROOT/f'{PREFIX}_transcription.tex').write_text('\n\n'.join(p.read_text().rstrip() for p in files)+'\n')
    print(json.dumps({'pages':len(pages),'against_C':totals[1],'against_H':totals[2],'collation_rows':len(collation),'inventory_elements':len(inventory),'remaining_doubts':len(doubts),'check_events':len(checks)}))

if __name__=='__main__':main()
