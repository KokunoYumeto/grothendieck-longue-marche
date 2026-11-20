"""Record the primary reader's manual collation; no OCR or recognition code.

All readings/observations are supplied by the reader. This script only formats
records, makes image crops, timestamps completed work and packages deliverables.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, hashlib, zipfile, re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]
SOURCE = WORKSPACE / 'source' / 'SP68_C13_136+141_texts'
SCANS = WORKSPACE / 'source' / 'SP68_C13_136+141_scans'
PREFIX = 'SP68_C13_136+141'
ORDER = [('136',s) for s in [364,365,366,367,368,370,371,372,373,374,375,376]] + [('141',s) for s in range(2,15)]
ERROR_SHEET_CATEGORIES = [
    'Symbols and indices', 'Words', 'Omissions', 'Drawings and diagrams',
    'Readable ink left as illegible', 'Insertions put in wrong place',
    'Struck text', 'Abbreviations expanded/spelling modernised',
    'Text not on page', 'Other',
]
ERROR_KIND_CATEGORY = {
    'misread symbol or index': 'Symbols and indices',
    'misread word': 'Words',
    'omission': 'Omissions',
    'drawing or diagram': 'Drawings and diagrams',
    r'readable ink left as \ill{}': 'Readable ink left as illegible',
    'insertion or placement': 'Insertions put in wrong place',
    'deletion state': 'Struck text',
    'deletion state (struck given live or live given struck)': 'Struck text',
    'abbreviation expanded or spelling modernised': 'Abbreviations expanded/spelling modernised',
    'text not on the page': 'Text not on page',
    'other': 'Other',
}
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def key(c,s): return f'{c}_scan{int(s):03d}'
def log(s):
    with (ROOT/'progress.log').open('a') as f: f.write(s+'\n')
def write_table(path, fields, rows, delim='\t'):
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delim,extrasaction='ignore')
        w.writeheader();w.writerows(rows)
def md(s): return str(s).replace('|','&#124;').replace('\n','<br>')
def table(fields,rows):
    return '| '+' | '.join(fields)+' |\n| '+' | '.join(['---']*len(fields))+' |\n'+''.join('| '+' | '.join(md(r.get(x,'')) for x in fields)+' |\n' for r in rows)
def crop_register():
    """Reproduce every logged crop's source geometry, not just change crops."""
    path=ROOT/'progress.log'
    pattern=re.compile(r'^crop (\d+_scan\d+) (\S+) (\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)) rotation (\S+) width (\d+)$')
    rows=[]
    for line in path.read_text().splitlines() if path.exists() else []:
        if not line.startswith('crop '): continue
        match=pattern.fullmatch(line)
        if not match: raise ValueError('Malformed crop entry in progress.log')
        scan,tag,box,rotation,width=match.groups()
        rows.append({'scan':scan,'crop':tag,'original pixel box':box,'rotation (degrees)':rotation,'output width (pixels)':width})
    return rows
def combine_pages(rr):
    """Add editorial cote boundaries to the combined file only."""
    chunks=[];previous_cote=None
    for r in rr:
        fragment=(ROOT/'pages'/(r['key']+'.tex')).read_text().rstrip()
        cote=str(r['cote'])
        if cote!=previous_cote:
            before_scan=fragment.split(r'\scanpage',1)[0]
            marker=re.compile(r'(?m)^[ \t]*\\cotefile\s*\{\s*'+re.escape(cote)+r'\s*\}')
            if not marker.search(before_scan): fragment='\\cotefile{'+cote+'}\n'+fragment
        chunks.append(fragment);previous_cote=cote
    return '\n\n'.join(chunks)+'\n'
def marks(c,s):
    return [r for r in csv.DictReader((SOURCE/'MARKS.tsv').open(),delimiter='\t') if r['cote']==str(c) and int(r['scan'])==int(s)]
def prepare(c,s):
    from PIL import Image
    im=Image.open(SCANS/(key(c,s)+'.jpg'))
    w,h=im.size
    boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)] if h>=w else [(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
    for label,box in zip(('a','b'),boxes):
        p=WORKSPACE/'work'/'halves'/f'{key(c,s)}_{label}.png'
        if not p.exists(): im.crop(box).save(p)
    print('IMAGE',key(c,s),im.size,'HALVES',boxes)
    for label,path in [('C',SOURCE/'pages'/(key(c,s)+'.tex')),('H',SOURCE/'hua'/('hua_'+key(c,s)+'.tex'))]:
        print('\nWITNESS',label,'\n'+(path.read_text() if path.exists() else '[not supplied]'))
    print('\nMARKS')
    for r in marks(c,s): print(r['id'],r['the mark as written'])
def crop(c,s,tag,box,angle=0,width=2600):
    from PIL import Image, ImageOps, ImageFilter
    p=WORKSPACE/'work'/'crops'/f'{key(c,s)}_{tag}.png'
    if p.exists(): raise ValueError('Do not recrop an already inspected place')
    im=Image.open(SCANS/(key(c,s)+'.jpg')).crop(tuple(box))
    im=ImageOps.autocontrast(im)
    if angle: im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.4,percent=130,threshold=3));im.save(p)
    log(f'crop {key(c,s)} {tag} {tuple(box)} rotation {angle} width {width}')
    print(p)
    return p

class Page:
    def __init__(self,c,s):
        self.c=str(c);self.s=int(s);self.k=key(c,s)
        self.tex=(SOURCE/'pages'/(self.k+'.tex')).read_text()
        self.r=dict(cote=self.c,scan=self.s,key=self.k,changes=[],decisions=[],extra_decisions=[],inventory=[],notes=[],hand=[],notation=[],doubts=[],abbreviations=[],checks=[],audit=[])
    def replace(self,old,new):
        if old not in self.tex: raise ValueError('Absent replacement: '+old)
        self.tex=self.tex.replace(old,new)
    def change(self,place,c,h,final,shows,kind='other',confidence='high',against_c=True,against_h=True,crop='page',math=False):
        self.r['changes'].append(dict(place=place,C=c,H=h,final=final,scan_shows=shows,crop=crop,confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,math=math,phase='first reading',marked_in_H=('yes' if any(t in h for t in ['\\?','\\ill','\\uncertain','\\unsure']) else 'no')))
    def decision(self,id,decision,reading,shows,crop='page',confidence='high'):
        self.r['decisions'].append(dict(id=id,cote=self.c,scan=f'{self.s:03d}',decision=decision,reading=reading,**{'what the ink shows':shows},crop=crop,confidence=confidence))
    def extra_decision(self,place,decision,reading,shows,crop='page',confidence='high',original_mark='',id=None):
        """Record a cancelled-text/other doubt omitted from supplied MARKS.tsv.

        These rows go only to the additional doubts table, never decisions.tsv
        or the substantive-change counts. Add a change separately if required.
        """
        rows=self.r.setdefault('extra_decisions',[])
        id=id or f'X-{self.k}-{len(rows)+1:02d}'
        if any(d['id']==id for d in rows+self.r['decisions']): raise ValueError('Duplicate decision id')
        rows.append(dict(id=id,cote=self.c,scan=f'{self.s:03d}',place=place,original_mark=original_mark,decision=decision,reading=reading,**{'what the ink shows':shows},crop=crop,confidence=confidence))
    def element(self,kind,position,words,sheet_kind='text',hand='his hand'):
        self.r['inventory'].append(dict(scan=self.k,sheet_kind=sheet_kind,hand=hand,element=len(self.r['inventory'])+1,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
    def note(self,s): self.r['notes'].append(s)
    def habit(self,s): self.r['hand'].append(s)
    def notation(self,sign,reading): self.r['notation'].append(dict(scan=self.k,sign=sign,reading=reading))
    def doubt(self,line,reading,alternatives,confidence='low'):
        self.r['doubts'].append(dict(scan=self.k,line=line,reading=reading,alternatives=alternatives,confidence=confidence))
    def abbr(self,a,b): self.r['abbreviations'].append(dict(abbreviation=a,expansion=b,scan=self.k))
    def check(self,id,type,outcome):
        self.r['checks'].append(dict(statement_id=id,date=utc(),who='GPT-6 Astra Pro; primary reader; effort not exposed; SP68 second pass',type=type,outcome=outcome))
    def save(self):
        expected=[r['id'] for r in marks(self.c,self.s)]
        actual=[r['id'] for r in self.r['decisions']]
        if expected!=actual: raise ValueError(f'Mark order mismatch {expected} != {actual}')
        done=[key(c,s) for c,s in ORDER if (ROOT/'records'/(key(c,s)+'.json')).exists()]
        if self.k not in done and key(*ORDER[len(done)])!=self.k: raise ValueError('Pages must be read in order')
        (ROOT/'pages'/(self.k+'.tex')).write_text(self.tex.rstrip()+'\n')
        self.r['done_utc']=utc()
        (ROOT/'records'/(self.k+'.json')).write_text(json.dumps(self.r,ensure_ascii=False,indent=2)+'\n')
        rebuild();log(f'scan {self.s:03d} done {utc()} cote {self.c}')
        print('Saved',self.k,'changes',len(self.r['changes']),'decisions',len(actual))

def records():
    return [json.loads(p.read_text()) for c,s in ORDER if (p:=ROOT/'records'/(key(c,s)+'.json')).exists()]
def rebuild():
    rr=records();counts=[];allchanges=[];collation=[];decisions=[];extra_decisions=[];inventory=[];notes=[];hand=[];notation=[];doubts=[];abbr=[];checks=[]
    for r in rr:
        cc=r['changes'];conf=Counter(x['confidence'] for x in cc)
        counts.append({'scan':r['key'],'against C':sum(x['against_c'] for x in cc),'against H':sum(x['against_h'] for x in cc),'high':conf['high'],'medium':conf['medium'],'low':conf['low'],'places':len(cc)})
        for x in cc:
            allchanges.append(dict(scan=r['key'],**x))
            if x['against_h']:
                collation.append(dict(folder=r['cote'],their_page=r['scan']-1,our_scan=f"{r['scan']:03d}",line=x['place'],their_reading=x['H'],codex_reading=x['C'],final_reading=x['final'],scan_shows=x['scan_shows']+'; '+x['crop'],kind=x['kind'],marked_in_H=x['marked_in_H'],confidence=x['confidence']))
        decisions+=r['decisions'];extra_decisions+=r.get('extra_decisions',[]);inventory+=r['inventory'];notation+=r['notation'];doubts+=r['doubts'];abbr+=r['abbreviations'];checks+=r['checks']
        notes+=['## '+r['key']+'\n\n'+'\n\n'.join(r['notes'])+('\n\nAudit: '+' '.join(r['audit']) if r['audit'] else '')]
        hand+=['## '+r['key']+'\n\n'+('\n\n'.join(r['hand']) or 'No additional general habit established on this page.')]
    total={x:sum(r[x] for r in counts) for x in ['against C','against H','high','medium','low','places']};total['scan']='TOTAL';counts.append(total)
    report='# Changes and collation\n\nSubstantive places only. Macro-only differences and certainty-only resolutions are excluded from these counts. A place differing from both witnesses contributes once to places and once to each witness count. Evidence marked `page` was settled in the whole-page/native-half views; crop boxes use original-image pixels.\n\n'+table(['scan','against C','against H','places','high','medium','low'],counts)
    report+='\n## Consequential corrections\n\n'+('\n'.join('- '+x['scan']+', '+x['place']+': '+x['final']+' — '+x['scan_shows'] for x in allchanges if x['math']) or 'None recorded.')+'\n'
    for r in rr:
        report+='\n## '+r['key']+'\n\n'
        items=[dict(place=x['place'],C=x['C'],H=x['H'],final=x['final'],evidence=x['scan_shows']+'; '+x['crop'],confidence=x['confidence']) for x in r['changes']]
        report+=table(['place','C','H','final','evidence','confidence'],items) if items else 'No substantive difference recorded.\n'
        report+='\nUnresolved: '+('; '.join(x['line']+': '+x['reading']+' ['+x['alternatives']+']' for x in r['doubts']) or 'none.')+'\n'
    report+='\n## Complete crop register\n\nEvery crop logged during this run is listed in creation order, including crops used only for certainty decisions and any crop on a page still being read. Boxes are (x0, y0, x1, y1) in the original image; rotation and output width describe the inspection copy. This register adds no substantive-change rows.\n\n'+table(['scan','crop','original pixel box','rotation (degrees)','output width (pixels)'],crop_register())
    (ROOT/(PREFIX+'_changes.md')).write_text(report)
    write_table(ROOT/(PREFIX+'_collation.tsv'),['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    write_table(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    write_table(ROOT/(PREFIX+'_inventory.csv'),['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    write_table(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    (ROOT/(PREFIX+'_notes.md')).write_text('# Notes while reading\n\nThese notes report the supplied pages only. Mathematical checks are limited to the events in CHECK_EVENTS.tsv; transcription is not a proof check.\n\n'+'\n\n'.join(notes)+'\n')
    (ROOT/(PREFIX+'_hand_log.md')).write_text('# Hand log\n\nHabits are local observations, not a license to overwrite a clear contrary letter. Each entry states its observed range; exceptions and witness errors are identified where found.\n\n'+'\n\n'.join(hand)+'\n')
    end=(ROOT/'scripts'/'legibility.txt').read_text() if (ROOT/'scripts'/'legibility.txt').exists() else 'Reading in progress; final assessment will be written after the second reading.'
    decisionrows=[dict(id=d['id'],page=key(d['cote'],d['scan']),decision=d['decision'],reading=d['reading'],evidence=d['what the ink shows'],crop=d['crop'],confidence=d['confidence']) for d in decisions]
    extrarows=[dict(id=d['id'],page=key(d['cote'],d['scan']),place=d['place'],original_mark=d.get('original_mark',''),decision=d['decision'],reading=d['reading'],evidence=d['what the ink shows'],crop=d['crop'],confidence=d['confidence']) for d in extra_decisions]
    (ROOT/(PREFIX+'_doubts.md')).write_text('# Notation table\n\n'+table(['scan','sign','reading'],notation)+'\n# Certainty/decision record\n\nOne row per recorded MARKS decision, in the supplied order. This includes certainty-only resolutions and retained doubts; these rows do not add to the substantive-change counts.\n\n'+table(['id','page','decision','reading','evidence','crop','confidence'],decisionrows)+'\n# Additional certainty decisions (outside MARKS)\n\nCancelled-text and other doubts omitted from the supplied MARKS list are recorded separately here. X identifiers are local record identifiers, not supplied M identifiers. These rows do not enter decisions.tsv or increase the substantive-change counts. A substantive difference, if present, is recorded separately in the changes log.\n\n'+table(['id','page','place','original_mark','decision','reading','evidence','crop','confidence'],extrarows)+'\n# Remaining doubts\n\n'+table(['scan','line','reading','alternatives','confidence'],doubts)+'\n# Abbreviations (expansions only here)\n\n'+table(['abbreviation','expansion','scan'],abbr)+'\n# Legibility and witnesses\n\n'+end+'\n')
    combined=combine_pages(rr)
    (ROOT/(PREFIX+'_transcription.tex')).write_text(combined)
    category=lambda x: ERROR_KIND_CATEGORY.get(x['kind'].replace('`',''),'Other')
    kinds_all=Counter(category(x) for x in allchanges)
    kinds_c=Counter(category(x) for x in allchanges if x['against_c'])
    kindsrows=[{'error-sheet category':k,'against C':kinds_c[k],'all witness differences':kinds_all[k]} for k in ERROR_SHEET_CATEGORIES]
    feedback_path=ROOT/'scripts'/'sheet_feedback.txt'
    feedback_end=feedback_path.read_text() if feedback_path.exists() else 'See the hand log for local forms and the changes log for all locations. Final synthesis follows the completed audit.'
    (ROOT/(PREFIX+'_sheet_feedback.md')).write_text('# Error-sheet feedback\n\nAll ten error-sheet categories appear in their supplied order, including zero counts. Counts are substantive collation places: “against C” counts places that change witness C; “all witness differences” also includes places differing only from H. A place differing from both witnesses is counted once in the latter column. Certainty-only decisions are separately enumerated in decisions.tsv and the doubts file’s certainty/decision record, and do not increase these counts. Overlapping phenomena are assigned the principal kind for counting.\n\n'+table(['error-sheet category','against C','all witness differences'],kindsrows)+'\n## Further recurring phenomena\n\n'+feedback_end.rstrip()+'\n')

def audit(c,s,comment):
    p=ROOT/'records'/(key(c,s)+'.json');r=json.loads(p.read_text());r['audit'].append(comment);r['audited_utc']=utc();p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');rebuild();log(f'scan {int(s):03d} audited {utc()} cote {c}')
def freeze():
    rr=records()
    assert len(rr)==25 and all('audited_utc' in r for r in rr)
    paths=[ROOT/'pages'/(r['key']+'.tex') for r in rr]+[ROOT/(PREFIX+'_transcription.tex')]
    data={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    for p,h in data.items():log(f'SHA-256 {h} {p}')
    (ROOT/'scripts'/'frozen_hashes.json').write_text(json.dumps(data,indent=2)+'\n')
    log('transcription frozen '+utc())
def verify_frozen():
    data=json.loads((ROOT/'scripts'/'frozen_hashes.json').read_text())
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data.items())
    log('frozen hashes unchanged '+utc()+f' ({len(data)} files)')
def package(name):
    dst=ROOT.parent/name
    if dst.exists(): raise ValueError('Never overwrite an existing archive')
    files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() not in ['.png','.jpg','.jpeg','.webp','.gif','.zip','.pyc']]
    with zipfile.ZipFile(dst,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(files):z.write(p,p.relative_to(ROOT))
    print(dst,len(files),dst.stat().st_size)
    return dst

if __name__=='__main__':
    import sys
    if sys.argv[1]=='prepare': prepare(sys.argv[2],int(sys.argv[3]))
    elif sys.argv[1]=='rebuild':rebuild()
    elif sys.argv[1]=='freeze':freeze()
    elif sys.argv[1]=='verify':verify_frozen()
    elif sys.argv[1]=='package':package(sys.argv[2])
