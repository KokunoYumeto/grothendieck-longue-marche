"""Apply explicitly reviewed decisions to an independent candidate reading.

Input is a per-page instruction JSON authored by the main reader. This program
does not choose readings; it transcribes the main reader's supplied choices.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,argparse,subprocess
OUT=Path(__file__).resolve().parents[1];ROOT=OUT.parent
p=argparse.ArgumentParser();p.add_argument('instruction');a=p.parse_args()
i=json.loads(Path(a.instruction).read_text());stem=i['stem'];base=i.get('base','r1')
meta=json.loads((ROOT/'work'/stem/'meta.json').read_text())
rdir=OUT/'readers'/stem/base
r=json.loads((rdir/'report.json').read_text())
text=(rdir/'reading.tex').read_text()
for old,new in i.get('replacements',[]):
 if old not in text:raise RuntimeError('Replacement not found: '+old)
 text=text.replace(old,new)
if 'reading_text' in i:text=i['reading_text']
prefix='readers/'+stem+'/'+base+'/'
def src(s):
 if s.startswith('crops/') and not (OUT/s).exists():return prefix+s
 if s in ['half_a','half_b','whole']:return 'source image '+s+' (see assigned meta.json in source provenance)'
 return s
diff=[]
for d in r['differences']:
 if d['id'] in i.get('exclude',[]):continue
 d=dict(d)
 if d['id'] in i.get('overrides',{}):d.update(i['overrides'][d['id']])
 d['source']=src(d.get('source',''))
 if 'readers' not in d:d['readers']={rid:d['reading'] for rid in ['r1','r2','r3']}
 if '\\ill' in d.get('H','') or '\\uncertain' in d.get('H','') or d.get('H_doubt_note'):d['marked_in_H']='yes'
 else:d['marked_in_H']='no'
 diff.append(d)
diff.extend(i.get('add_differences',[]))
cd=i.get('c_doubts',r.get('c_doubts',[]))
for d in cd:
 d['source']=src(d.get('source',''))
 for ov in i.get('doubt_overrides',[]):
  if d['place']==ov['place']:d.update(ov)
u=i.get('unresolved',r.get('unresolved',[]))
for x in u:x['source']=src(x.get('source',''))
rows=json.loads((ROOT/'work/page_map.json').read_text());order=[Path(x['codex_file']).stem for x in rows].index(stem)
page={'order':order,'stem':stem,'filename':stem+'.tex','scan':meta['cote']+'/'+meta['our_scan'].zfill(3),'folder':meta['folder'],'their_page':meta['their_page'],'our_scan':meta['our_scan'],'brief':i['brief'],'agents':i['agents'],'differences':diff,'c_doubts':cd,'unresolved':u,'inventory':i.get('inventory',r['inventory']),'notes':i['notes'],'slips':i.get('slips',[]),'abbreviations':i.get('abbreviations',[]),'checks':i.get('checks',[]),'main_crops':i.get('main_crops',[]),'main_views':i.get('main_views',[]),'adjudication':i.get('adjudication',''),'completed_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}
if order==0:
 if not text.lstrip().startswith('\\cotefile{29}'):text='\\cotefile{29}\n'+text
elif meta['cote']=='32' and rows[order-1]['cote']!='32':
 text=text.replace('\\cotefile{32}\n','');text='\\cotefile{32}\n'+text
else:
 import re
 text=re.sub(r'^\\cotefile\{\d+\}\s*','',text)
(OUT/'pages'/page['filename']).write_text(text.rstrip()+'\n')
(OUT/'decisions'/(stem+'.json')).write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n')
with (OUT/'progress.log').open('a') as f:f.write(f"scan {int(meta['our_scan']):03} done {page['completed_utc']} cote {meta['cote']}\n")
subprocess.run(['python',str(OUT/'scripts/build_records.py')],check=True)
print('Adjudicated',page['scan'])
