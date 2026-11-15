from pathlib import Path
import csv
from datetime import datetime,timezone
r=Path(__file__).resolve().parents[1];p=r/'MPL_14_002-044_inventory.csv'
with p.open(newline='') as f:rd=csv.DictReader(f);fields=rd.fieldnames;rows=list(rd)
byid={x['element']:x for x in rows}
byid['038-13']['kind']='drawing';byid['038-13']['position']='left end of theorem implication arrow'
byid['038-13']['first_words_or_objects']='Pencil reverse chevron, uncertain < / left arrow'
byid['028-04']['first_words_or_objects']='la / les (uncertain)'
byid['035-11']['first_words_or_objects']='φ:A_Y^(0 / *)(k)→A^i_alb(X)'
byid['035-18']['first_words_or_objects']='(0) Forment un k-groupe / s-groupe (uncertain)'
byid['039-01']['first_words_or_objects']='u_Z=0 ⇐ / ⇔ u_Z′=0 (head uncertain)'
for key in ['027-12','027-13']:byid[key]['first_words_or_objects']='X − / → Y (head uncertain)'
byid['027-14']['first_words_or_objects']='X × T ⇔ / ⇒ Y × T; both to T (head uncertain)'
# Place audit additions with their parent element, maintaining a page's physical reading sequence.
after={
'019-25':'019-03','019-26':'019-06','019-27':'019-26',
'26-audit-callout':'026-03','28-audit-rule-margin':'028-09','28-audit-rule':'28-audit-rule-margin',
'30-audit-callout':'030-11','32-audit-check-margin':'032-01','32-audit-check':'32-audit-check-margin',
'32-audit-circle':'032-06','35-audit-circle':'035-07','36-audit-circle':'036-02','37-audit-rule':'037-01',
'38-audit-deleted-x':'038-24'}
for moving,anchor in after.items():
 row=byid[moving];rows.remove(row);rows.insert(rows.index(byid[anchor])+1,row)
# Move the small product diagrams to the height of the surrounding proof, before the bottom computation.
for block,anchor in [(['026-18','026-19'],'026-11'),(['027-12','027-13','027-14','027-15','027-16'],'027-06')]:
 parts=[byid[k] for k in block]
 for x in parts:rows.remove(x)
 i=rows.index(byid[anchor])+1;rows[i:i]=parts
# The pencil ring around the inserted alb subscript is itself visible.
new=dict(cote='14',scan='31',sheet_kind='text',element='31-audit-alb-circle',kind='drawing',position='inserted subscript in first cycle group',first_words_or_objects='Circled alb',transcribed='yes')
rows.insert(rows.index(byid['031-06'])+1,new)
# Stable sequential element identifiers make each page easy to check from top to bottom.
counts={}
for row in rows:
 n=int(row['scan']);counts[n]=counts.get(n,0)+1;row['element']=f'{n:03}-{counts[n]:02}'
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
with (r/'progress.log').open('a') as f:f.write('inventory reconciled '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+f'; {len(rows)} elements, all transcribed=yes; audit additions placed with their page elements\n')
print(f'{len(rows)} inventory elements over {len(counts)} scans')
