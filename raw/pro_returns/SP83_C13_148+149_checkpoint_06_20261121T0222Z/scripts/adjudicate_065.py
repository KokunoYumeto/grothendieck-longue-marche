from pathlib import Path
import csv,json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan065'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='6ee97d80e25a445b5e547eb162408bfbc5f9ca40b3dea2accbc0f0043ce77f98'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B03':'The crop shows an ordinary S, loop-headed T, top with a descending p, and a plus above a separate minus. The two readings have identical letters, indices and exponent; braces alone differ.',
'B04':'The full crop and parenthesis helper were viewed. The opening low repeated m/n strokes, long middle run and terminal nt support moyennant. The second word begins with a looped d and has a long f descender, middle r/m strokes and t/i/on ending, supporting deformations, not repetition. The lower word begins with crossed t and has a second tall t before its e/s ending: toutes. Two distinct underline strokes cover toutes and les cordes. The original parenthetical insertion and these spans remain.',
'B05':'The l loop is clear but its long flat exit does not separately expose a closed a or an open e. The existing la/le doubt remains; the noun that follows is not used to force its gender.',
'B06':'The entire lower passage and upper-right and lower-word helpers were viewed. Foulee has one tall l loop, then an accent-like dot and low ending; the extra ll/i/s of fouillis is not established. The next low run supports avec, and the article before modele has no separate s. The raised modeles des is attached between baseline des and Pi-one by the long curved insertion leader; the existing insertion macro represents that attachment without adding a mathematical graph. Pi-one has a comma between X and R. Dependance fonctorielle and the final (X,R) are clear. The upper-right verb has a d-like beginning and compressed interior turns that can look like a second d; desire/deduit is now left doubtful. No secure accent above its first e is supplied, and no comma is added after it.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
v=C['B06']['first'].replace('desire',r'\unsure{desire|déduit}')
D['B06'].update(choice='reading',reading=v)
pp=R/'pages'/f'{p}.tex';s=pp.read_text();assert C['B06']['first'] in s;s=s.replace(C['B06']['first'],v);pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
for x in r['changes']:
 n=int(x['id'].rsplit('-',1)[1]);b={2:'B04',3:'B04',4:'B05',5:'B06',6:'B06',7:'B06',8:'B06',9:'B06'}.get(n)
 if b:x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b])
 if n in (8,9):x.update(final=r'\unsure{desire|déduit}',confidence='low')
for x in r['decisions']:
 if x['id']=='M0783':x.update(decision='undecided',reading=r'\unsure{desire|déduit}',evidence=E['B06'],crop=f'crops/{p}_second_B06.png',box=boxes['B06'],confidence='low')
r['doubts'].append(dict(place='Verb after qu’on',reading=r'\unsure{desire|déduit}',alternatives='desire; déduit',confidence='low',reason=E['B06']))
r['notes'].append(dict(id=p+'-N-audit',text='All four unequal boxes were reviewed after the independent TSV was frozen. The inserted parenthesis remains moyennant deformations, the lower noun remains foulee, and the article before it stays la/le. The compressed verb after qu\'on is reopened as desire/deduit; the mathematics of obtaining a model does not decide its letters. The insertion leader supplies the attachment of modeles des, not an additional mathematical diagram. No model-existence assertion was proved. This audit adds a certainty qualification, not a new material witness-error row.'))
extra=[f'crops/{p}_second_{z}.png' for z in ('B04_parenthetical','B06_upper_right','B06_lower_words')]
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
