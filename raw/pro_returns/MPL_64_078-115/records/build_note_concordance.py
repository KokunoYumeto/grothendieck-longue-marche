#!/usr/bin/env python3
import csv,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]
notes=(p/'MPL_64_078-115_notes.md').read_text()
ids=re.findall(r'^### (.+?) — ',notes,re.M)
events=list(csv.DictReader((p/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
allids=[x['statement_id'] for x in events]
mapping={
 'RC05':['Hua/64/mu4star-AutplusQ0'],
 'RC04':['Hua/64/Q0-x4-minus4'],
 'RC06':['MPL64/080/(23)/tensor-square','Hua/64/tensor-square'],
 'R05 / RC03':['R05;','Hua/64-legendre-pinning-moduli','Conrad/Level-structures/2.1'],
 'RC10d':['Hua/64/lambda-equals-t-convention'],
 'ALG01':['ALG01-'], 'ALG02a':['ALG02-'], 'ALG02b':['ALG02-R'],
 'RC08':['Hua/64/n-invertible-kernel-constants','ALG02-F'],
 'ALG03':['ALG03-R','Hua/64/principal-part-normalization'],
 'ALG03b':['ALG02-S','ALG03-R'],
 'ALG04a':['ALG04-R'], 'ALG04b':['ALG04-R'],
 'RC09':['Hua/64/coefficients-determined-by-delta'],
 'ALG05':['ALG05-R'], 'ALG06':['ALG06-R','Hua/64/distinct-point-collinearity'],
 'ALG07a':['ALG07-R'], 'ALG07b':['ALG07-R'], 'ALG08':['ALG08-R'],
 'B5-01':['MPL_64_078-115 B5-01'], 'B5-01b':['MPL_64_078-115 B5-01','LM2 C.r2'],
 'B5-02':['MPL_64_078-115 B5-02','LM2 C.d1'],
 'B5-03a':['MPL_64_078-115 B5-03','LM_140-2 LM_P053 S09'],
 'B5-03b':['LM_140-2 LM_P053 S06','LM_140-2 LM_P053 S09'],
 'B5-03c':['LM2 C.d1','LM2 C.r1','LM2 C.r2','LM2 C.r3'],
 'B5-04':['LM4 D.12'], 'B5-05':['EXIT_TOWER E.24'], 'B5-06':['LM4_SUCCESSOR B.38'],
 'RC01':['S20/local-scope/64-078-115'],
 'RC13a':['MPL64/RC13/Legendre-exact-differential','RC13a/char0-scope','MPL64/RC13/deRham-scope'],
 'RC13b':['MPL64/RC13/Hasse-polynomial-ODE','MPL64/RC13/Hasse-prime-checks','MPL64/RC13/Cartier-coefficient']
}
rows=[]
for ident in ids:
    prefixes=mapping.get(ident,[ident])
    matches=sorted({sid for sid in allids if any(sid==prefix or (prefix.endswith((';','-')) and sid.startswith(prefix)) for prefix in prefixes)})
    if not matches and ident.startswith('R'):
        matches=sorted({sid for sid in allids if sid.startswith(ident+';')})
    if not matches:raise RuntimeError(f'No check/use mapping for {ident}')
    rows.append({'note_id':ident,'event_statement_ids':' | '.join(matches),
                 'scope':'Read each event type/outcome: documentary and background uses are not mathematical proof checks.'})
with (p/'records'/'note_event_concordance.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['note_id','event_statement_ids','scope'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print(f'All{len(rows)} individual notes have explicit check/use-event links')
