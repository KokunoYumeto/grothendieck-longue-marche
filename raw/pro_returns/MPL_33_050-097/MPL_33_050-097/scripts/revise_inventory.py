"""Expand grouped editorial elements and add graphic details recovered on audit.
Run once on the initial inventory; all resulting rows remain in source order.
"""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
p=root/'MPL_33_050-097_inventory.csv'
rows=list(csv.DictReader(p.open()))
changes={
'066.07':[('deletion','superscript ! after first f'),('deletion','subscript * after first f'),('deletion','superscript ! after second f'),('deletion','subscript * after second f')],
'066.13':[('deletion','morphisme'),('deletion','de')],
'068.05':[('deletion','(R!g)'),('deletion','! above R')],
'068.14':[('deletion','! above first R'),('deletion','σ before i'),('deletion','! above second R')],
'068.17':[('deletion','! above Rj'),('deletion','R!id')],
'068.20':[('deletion','(Ri!) after equals'),('deletion','Ri! before Rσ!'),('deletion','(a) under brace'),('deletion','Ri! in last parentheses')],
'092.08':[('deletion','* on first Lg'),('deletion','* on R!f replaced by prime'),('deletion','R* replaced by L'),('deletion','* on final R!f'),('deletion','* above first R_! in wavy box'),('deletion','* above second R_! in wavy box')],
'092.09':[('insertion','! above first R'),('insertion','prime on f'),('insertion','L replacing R*'),('insertion','! above final R')],
'093.07':[('deletion','et'),('deletion','blackened word before de même')],
'093.12':[('deletion','blackened word after fini'),('deletion','blackened word after radical de A')],
'094.15':[('insertion','finie'),('insertion',"F' loc. constant sur Y'")],
'094.16':[('deletion','first R before i_!'),('deletion','second R before i_!')],
'096.16':[('deletion','lower *'),('deletion','X under F')],
}
add_after={
'064.05':[('margin note','upper left emphasis','two parallel strokes')],
'066.04':[('margin note','upper left','marginal comparison diagram X‴ X X′ X″')],
'066.14':[('margin note','lower left','marginal square X X′ Y Y′')],
'076.03':[('margin note','left of upper paragraph','three parallel strokes')],
'080.04':[('deletion','upper prose between on and se servira','en')],
'087.23':[('drawing','condition f)','ellipse around gr(j) tensor 1')],
'087.24':[('drawing',"condition f')",'ellipse around gr(j) tensor 1')],
'090.09':[('deletion','third box, first direct-image operator','overwritten lower !'),('deletion','third box, second direct-image operator','overwritten lower !')],
'092.01':[('text','below opening continuation','isolated dash')],
'092.06':[('drawing','middle left margin','three branches beside à priori quelle ?')],
'094.18':[('deletion','margin beside cancelled filtration','si fini')],
}
out=[]
for r in rows:
 key=r['element']
 if key in changes:
  for k,words in changes[key]:
   q=r.copy();q.update(kind=k,first_words_or_objects=words);out.append(q)
 else:out.append(r)
 for k,pos,words in add_after.get(key,[]):
  q=r.copy();q.update(kind=k,position=pos,first_words_or_objects=words);out.append(q)
counts={}
for r in out:
 n=int(r['scan']);counts[n]=counts.get(n,0)+1;r['element']=f'{n:03d}.{counts[n]:02d}'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(out)
print(len(out),'inventory elements')
