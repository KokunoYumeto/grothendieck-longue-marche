from pathlib import Path
import csv, json, re, sys, hashlib
from datetime import datetime, timezone
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'out'
PREFIX='SP14_CW_13+15+26+35+48+66+97+123+162'
W=ROOT/'source'/f'{PREFIX}_witnesses'
S=ROOT/'source'/f'{PREFIX}_scans'
ROWS=list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'))
COTES=['13','15','26','35','48','66','97','123','162-1','162-6']
ROWS.sort(key=lambda r:(COTES.index(r['cote']),int(r['our_scan'])))
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def row(cote,scan): return next(r for r in ROWS if r['cote']==str(cote) and int(r['our_scan'])==int(scan))
def name(r): return Path(r['codex_file']).stem
def witnesses(cote,scan):
    r=row(cote,scan)
    print('PAGE',r['cote'],r['our_scan'],'H status:',r['hua_has'])
    print('WITNESS C\n'+(W/r['codex_file']).read_text())
    if r['codex_file_run2']: print('WITNESS C RUN 2\n'+(W/r['codex_file_run2']).read_text())
    if r['hua_has']!='nothing':
        text=(W/r['hua_file']).read_text()
        m=re.search(r'\\page\{'+r['their_page']+r'\}',text)
        if m:
            rest=text[m.end():]; end=re.search(r'\\page\{',rest)
            print('WITNESS H\n'+rest[:end.start() if end else len(rest)])
        else: print('H has description, locate manually:',r['hua_file'])
def crop(cote,scan,label,box,scale=2):
    r=row(cote,scan); im=Image.open(S/(name(r)+'.jpg'))
    a=im.crop(tuple(box)); a=a.resize((int(a.width*scale),int(a.height*scale)))
    target=ROOT/'work/crops'/f'{name(r)}_{label}.png'; a.save(target)
    with (OUT/'crop_manifest.tsv').open('a') as f:
        f.write('\t'.join(map(str,[target.name,str(S/(name(r)+'.jpg')),','.join(map(str,box)),scale,0]))+'\n')
    print(str(target)); return str(target)
def commit(cote,scan,data):
    r=row(cote,scan); target=OUT/'pages'/Path(r['codex_file']).name
    assert not target.exists(), 'Use a documented audit revision for existing page.'
    remaining=[x for x in ROWS if not (OUT/'pages'/Path(x['codex_file']).name).exists()]
    assert remaining[0]==r, 'Pages must be processed in archive order.'
    text=(W/r['codex_file']).read_text()
    for a,b in data.get('replace',[]):
        assert a in text, repr(a)
        text=text.replace(a,b)
    if 'text' in data: text=data['text']
    text=re.sub(r'\\cotefile\{[^}]+\}\s*','',text)
    if not any(x['cote']==r['cote'] for x in ROWS[:ROWS.index(r)]): text='\\cotefile{'+r['cote']+'}\n'+text
    target.write_text(text)
    data.update(cote=r['cote'],scan=r['our_scan'],folder=r['folder'],their_page=r['their_page'],hua_has=r['hua_has'],filename=target.name,done=now())
    (OUT/'decisions'/(target.stem+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (OUT/'progress.log').open('a') as f:f.write(f"cote {cote} scan {int(scan):03d} done {now()}\n")
    render()
    print('Committed',target.name,'pages',len(list((OUT/'pages').glob('*.tex'))))
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
def uncertainty_marks(text):
    results=[]
    for m in re.finditer(r'\\unsure\{',text):
        level=1; end=m.end()
        while level and end<len(text):
            if text[end]=='{' and (end==0 or text[end-1]!='\\'):level+=1
            elif text[end]=='}' and (end==0 or text[end-1]!='\\'):level-=1
            end+=1
        value=text[m.end():end-1]
        parts=value.split('|')
        results.append(dict(place='LaTeX line '+str(text.count('\n',0,m.start())+1),reading=parts[0],alternatives=' | '.join(parts[1:]),confidence='low' if len(parts)>1 else 'medium'))
    return results
def render():
    decisions=[]; combined=[]
    for r in ROWS:
        p=OUT/'pages'/Path(r['codex_file']).name
        if p.exists():
            combined.append(p.read_text()); d=json.loads((OUT/'decisions'/(p.stem+'.json')).read_text())
            d['doubts']=uncertainty_marks(p.read_text())
            decisions.append(d)
    (OUT/f'{PREFIX}_transcription.tex').write_text('\n\n'.join(combined))
    ch=['# Changes against the witnesses\n','Counts include substantive reading differences and changes in explicit uncertainty, not macro-only differences. Against C means the first run; the independent B15-02 second run is counted separately. Confidence columns count logged decisions, including retained doubts; these counts are not error rates. H-absent pages have no collation rows.\n','| Cote / scan | Against C | Against C run 2 | Against H | High | Medium | Low |','|---|---:|---:|---:|---:|---:|---:|']
    totals=[0]*6
    for d in decisions:
        changes=d.get('changes',[])
        counts=[sum(x.get('against_c',False) for x in changes),sum(x.get('against_c2',False) for x in changes),sum(x.get('against_h',False) for x in changes)]+[sum(x.get('confidence')==c for x in changes) for c in ['high','medium','low']]
        totals=[a+b for a,b in zip(totals,counts)]
        ch.append('| '+d['cote']+' / '+d['scan']+' | '+' | '.join(map(str,counts))+' |')
    ch.append('| **Total** | '+' | '.join(map(str,totals))+' |\n')
    ch.append('## Consequential corrections\n')
    for d in decisions:
        for x in d.get('changes',[]):
            if x.get('consequential'):ch.append('- '+d['cote']+'/'+d['scan']+' '+x['place']+': '+x['consequential'])
    co=[]; inv=[]; doubts=['# Notation and remaining doubts\n','## Notation table\n']
    with (OUT/'notation.tsv').open() as f:
        reader=csv.reader(f,delimiter='\t'); headers=next(reader)
        doubts+=['| '+' | '.join(headers)+' |','|'+'---|'*len(headers)]
        doubts+=['| '+' | '.join(esc(x) for x in row)+' |' for row in reader]
    doubts+=['\n## Remaining doubts\n','| Cote / scan | Place | Reading | Alternatives | Confidence |','|---|---|---|---|---|']
    for d in decisions:
        ch+=['\n## Cote '+d['cote']+', scan '+d['scan']+'\n','H coverage: '+d['hua_has']+'.\n','| Place | C | H | Final | Ink and crop | Confidence |','|---|---|---|---|---|---|']
        for x in d.get('changes',[]):
            ch.append('| '+' | '.join(esc(x.get(k,'')) for k in ['place','c','h','final','ink','confidence'])+' |')
            if x.get('against_h') and d['hua_has']=='text':
                co.append([d['folder'],d['their_page'],d['scan'],x['place'],x.get('h',''),x.get('c',''),x['final'],x['ink'],x.get('kind','other'),x.get('marked_in_H','no'),x['confidence']])
        if not d.get('changes'):ch.append('| All text | — | — | C retained after visual reading | '+esc(d.get('observations',''))+' | high |')
        ch.append('\nUnresolved: '+('; '.join(x['place']+': '+x['reading'] for x in d.get('doubts',[])) or 'none')+'\n')
        for x in d.get('doubts',[]): doubts.append('| '+' | '.join(esc(v) for v in [d['cote']+'/'+d['scan'],x['place'],x['reading'],x.get('alternatives',''),x.get('confidence','medium')])+' |')
        for i,x in enumerate(d.get('inventory',[]),1):
            inv.append([d['cote']+'/'+d['scan'],d.get('sheet_kind','text'),x.get('hand',d.get('hand','his hand')),i,{'marginnote':'margin note'}.get(x['kind'],x['kind']),x['position'],x['text'],'yes'])
    (OUT/f'{PREFIX}_changes.md').write_text('\n'.join(ch)+'\n')
    (OUT/f'{PREFIX}_doubts.md').write_text('\n'.join(doubts)+'\n')
    for filename,header,rows in [
        (f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],co),
        (f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv)]:
        with (OUT/filename).open('w',newline='') as f:
            writer=csv.writer(f,delimiter='\t' if filename.endswith('.tsv') else ',');writer.writerow(header);writer.writerows(rows)
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='witnesses': witnesses(*sys.argv[2:4])
    elif cmd=='crop': crop(sys.argv[2],sys.argv[3],sys.argv[4],list(map(int,sys.argv[5:9])),float(sys.argv[9]) if len(sys.argv)>9 else 2)
    elif cmd=='commit': commit(sys.argv[2],sys.argv[3],json.load(sys.stdin))
    elif cmd=='render':render()
