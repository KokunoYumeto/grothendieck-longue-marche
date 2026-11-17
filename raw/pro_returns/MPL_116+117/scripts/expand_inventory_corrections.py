"""Root inventory reconciliation of already audited explicit correction macros."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
p=root/'MPL_116+117_inventory.csv'
with p.open(newline='') as f:
 rd=csv.DictReader(f);cols=rd.fieldnames;rows=list(rd)
def split(e,entries):
 i=next(i for i,r in enumerate(rows) if r['element']==e);base=rows.pop(i)
 for n,(kind,words) in enumerate(entries):
  r=base.copy();r['element']=e+f'-{n+1}';r['kind']=kind;r['first_words_or_objects']=words;rows.insert(i+n,r)
split('117-004-20',[('deletion','g)'),('insertion','f)')])
split('117-004-22',[('deletion','h)'),('insertion','g)')])
split('117-005-06',[('deletion','j)'),('insertion','h)')])
split('117-005-09',[('deletion','des'),('insertion','une')])
split('117-006-04',[('insertion','petite'),('deletion','petite')])
split('117-006-08',[('deletion','H [uncertain]'),('deletion',', = si A l’est')])
split('117-008-08',[('text','Pour'),('deletion','toute'),('deletion','A petite, i.e. A ∈ Ob Cat, on donne')])
for r in rows:
 if r['element']=='117-008-09':r['kind']='insertion'
 if r['element']=='117-020-08':r['first_words_or_objects']='une définition|relation'
 if r['element']=='117-021-21':r['first_words_or_objects']='pas dur|pas abs., donc'
 if r['element']=='117-022-10':r['first_words_or_objects']='qui est envisagée|conséquence car p₀i=p'
i=next(i for i,r in enumerate(rows) if r['element']=='117-018-05');base=rows[i]
for n,(kind,words) in enumerate([('insertion','M as exponent of f'),('deletion','A as subscript of f'),('insertion','M as exponent of g'),('deletion','A as subscript of g')]):
 r=base.copy();r['element']='117-018-05-c'+str(n+1);r['kind']=kind;r['position']='middle diagram arrow label';r['first_words_or_objects']=words;rows.insert(i+1+n,r)
split('117-020-05',[('deletion','Pour'),('deletion','S’il y en a')])
split('117-020-06',[('insertion','Pour deux tels'),('insertion','(M₁,W₁),(M₂,W₂)')])
split('117-021-23',[('insertion','complexes de'),('insertion','transforme')])
split('117-021-37',[('insertion','sont'),('insertion','l’une de l’autre')])
split('117-022-04',[('deletion','droite'),('deletion','gauche')])
i=next(i for i,r in enumerate(rows) if r['element']=='117-022-18');r=rows[i].copy();r['element']='117-022-18-c1';r['kind']='deletion';r['first_words_or_objects']='variants';rows.insert(i+1,r)
for r in rows:
 if r['element']=='audit curved annotations' or (r['cote']=='117' and r['scan']=='2' and 'audit' in r['element']):r['element']='117-002-audit-curves'
with p.open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=cols);wr.writeheader();wr.writerows(rows)
print('Inventory rows:',len(rows))
