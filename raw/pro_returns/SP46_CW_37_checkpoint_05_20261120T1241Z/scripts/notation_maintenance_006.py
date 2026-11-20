from pathlib import Path
import json,hashlib,datetime
O=Path(__file__).resolve().parents[1]
paths=sorted((O/'pages').glob('*.tex'))+[O/'SP46_CW_37_transcription.tex']
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
p=O/'decisions/scan055.json';d=json.loads(p.read_text())
old=[x for x in d['notation'] if x['sign']=='Marginal point pair']
assert len(old)==1 and any(x['sign']=='Detached marginal point pair' for x in d['notation'])
d['notation']=[x for x in d['notation'] if x['sign']!='Marginal point pair']
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=O/'decisions/scan069.json';d=json.loads(p.read_text())
for sign,idx in [('Uncertain detached point',10),('Uncertain detached pair',12)]:
 x=next(x for x in d['notation'] if x['sign']==sign)
 x['latex']=d['decisions'][idx]['reading']
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# A line-locator dot is documented but no change of mathematical meaning is established.
p=O/'decisions/scan054.json';d=json.loads(p.read_text())
x=d['decisions'][25];assert 'line indicator' in x['place'];x.pop('consequential',None)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
t=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (O/'progress.log').open('a') as f:f.write('notation record maintenance '+t+': removed superseded scan055 colon rendering, aligned scan069 small-graphic wrappers with final page, and classified scan054 dotted locator as documentary rather than a proved mathematical change; all six page hashes and combined hash unchanged\n')
print('Updated metadata only; all six page files and combined transcription unchanged.')
