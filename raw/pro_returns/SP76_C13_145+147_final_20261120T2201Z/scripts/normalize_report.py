from pathlib import Path
import json,sys
W=Path(__file__).resolve().parents[1]
page=sys.argv[1]
p=W/'reports'/f'{page}.json'
r=json.loads(p.read_text())
mapping={'words':'misread word','symbols and indices':'misread symbol or index','punctuation':'other','abbreviations':'abbreviation expanded or spelling modernised','omissions':'omission','struck text':'deletion state','insertions':'insertion or placement'}
for x in r['changes']:
    x['kind']=mapping.get(x['kind'],x['kind'])
    if x['kind']=='omission' and ('\\ill{' in x['H'] or '\\illegible{' in x['H']):x['kind']='readable ink left as \\ill{}'
    if any(q in x['H'] for q in ['\\ill{','\\uncertain{','\\unsure{','\\illegible{']):x['marked_in_H']='yes'
for x in r['inventory']:
    if x['sheet_kind']=='handwritten mathematical notes':x['sheet_kind']='text'
    if x['hand']=='main manuscript hand':x['hand']='his hand'
    if x['kind']=='page_number':x['kind']='text'
    if x['kind']=='formula':x['kind']='display'
for field in ['notation','abbreviations','hand_habits']:
    for x in r.get(field,[]):
        places=x.get('places',[])
        if isinstance(places,list):x['places']='; '.join(page+' '+str(y) if page not in str(y) else str(y) for y in places)
        elif page not in str(places):x['places']=page+' '+str(places)
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(page,'schema normalized')
