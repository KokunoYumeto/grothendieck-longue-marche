"""Explicit root decisions for the contents-sheet blind audit."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan003';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repl=[('la MDT-structure',r'la \unsure{MDT|MOT}-structure'),('Structure MDT analytique',r'Structure \unsure{MDT|MPT} analytique'),('déploiement','déployement'),('des groupoïdes fondamentaux',r'\unsure{des|du} \unsure{groupoïde|groupoïdes} \unsure{fondamental|fondamentaux}')]
for a,b in repl:assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
tp.write_text(t)
bxs={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
r['changes'].append(dict(place='entry11: déployement spelling',C='déploiement',H='déploiement',final='déployement',evidence='After déplo the letter has a distinct descending y tail, then e/m/e/n/t. It is not a short dotted i. Preserve the written déployement.',crop=f'crops/{pg}_second_B12.png',box=bxs['B12'],confidence='high',against_C=True,against_H=True,kind='abbreviation expanded or spelling modernised',marked_in_H='no',consequential=False))
r['changes'].append(dict(place='entry11: groupoid phrase endings',C='des groupoïdes fondamentaux',H='des groupoïdes fondamentaux',final=r'\unsure{des|du} \unsure{groupoïde|groupoïdes} \unsure{fondamental|fondamentaux}',evidence='The small article ends in a compressed join that can be des or du. Groupoïde has no independently clear final s after its low e; fondamental has a tall returned terminal favoring l, not the clearly crossed x seen in normaux just above. Singular noun and adjective are preferred, but their compressed endings remain uncertain. The article is not regularized to match them.',crop=f'crops/{pg}_second_B12.png',box=bxs['B12'],confidence='low',against_C=True,against_H=True,kind='misread word',marked_in_H='no',consequential=False))
newd=[('entry9 acronym',r'\unsure{MDT|MOT}',['MDT','MOT'],'B10: the middle letter has a closed oval with an internal/left upright; D is favored by the repeated label, but the loop can also read O.'),('entry10 acronym',r'\unsure{MDT|MPT}',['MDT','MPT'],'B11: the middle letter has a clear upright with an upper bowl; its low continuation makes D/P ambiguous. No independent round O is established in this occurrence.'),('entry11 article',r'\unsure{des|du}',['des','du'],'B12: compressed terminal after d admits es or u; no grammatical repair is used.'),('entry11 noun ending',r'\unsure{groupoïde|groupoïdes}',['groupoïde','groupoïdes'],'B12: no independent final s is secure after the low e; singular is preferred but the tiny exit remains ambiguous.'),('entry11 adjective ending',r'\unsure{fondamental|fondamentaux}',['fondamental','fondamentaux'],'B12: a tall returned final stroke favors l; the compact lower turn does not completely exclude the ending read by both witnesses.')]
for place,reading,alt,reason in newd:r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence='low',reason=reason))
r['notes'].append('Independent audit: both witnesses modernize the clear y in déployement to i. The last phrase of entry 11 has uncertain article and word endings; singular groupoïde and fondamental are preferred without forcing the preceding article to agree. Acronym middle letters remain locally doubtful in entries 9 and 10. Small point clusters beside the page-number column recur as irregular vertical artifacts; they are not transcribed as extra ditto signs. The substantial upright ticks after 16 and 29 remain primes. This is a contents-list reading, not a check of the listed mathematical results.')
r['notation'].append(dict(form=r'\unsure{MDT|MOT}; \unsure{MDT|MPT}',meaning_or_use='The repeated prose acronym has an ambiguous middle capital in these two occurrences; preferred MDT is retained, with the local loop/bowl alternatives recorded.',places='147_scan003 entries 9 and 10; second B10/B11'))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B02':('high','The internal d has a loop and ascender, whereas the terminal has an upright and rightward crossing stroke: standart, not standard. Item and page number are both 1. Table versus hfill layout is equivalent.'),
'B03':('high','Final t again differs from internal looped d. Maquettes is a continuation below the first line. The tiny pair near the right column is among irregular scattered point clusters also visible by 6, 15, 16-prime and 37; it does not establish a deliberate ditto or colon. No extra text is added from those points.'),
'B04':('high','Courbes stables, et MD-graphes and the numeral 6 agree; only table/layout wrappers differ. The comma after stables and hyphen in MD-graphes are visible.'),
'B05':('low','The capital L and very compressed lower terminal do not separate e from a. Keep Le/La doubt; théorie has dotted i and no m of théorème. Name and numeral 10 agree.'),
'B06':('high','The item numeral has an upper horizontal and lower bowl, giving 5. The d joins a low extended e without a separate final s before MD; retain de. Right numeral is 15.'),
'B07':('high','Générisation and maquettes are legible. After 16 the separate short upright starts high and has no digit-1 head or foot; retain a prime. Macro layout and line break do not change the reading.'),
'B08':('low','The whole hatted-M expression and inequality were checked. Both readings retain the uncertain g,nu/g subscript; hats and line-wrap hyphen in détermination are encoding/layout differences. Numeral 25 is clear.'),
'B09':('high','Both readings agree on the words and inequality <=4. The isolated raised tick after 29 has no independent digit head or foot; retain a prime. Table layout differs only.'),
'B10':('low','Variables has low v/a/r/i, then tall b/l and -es, without the p descender needed by compactes or complètes. In the acronym the middle closed oval and upright permit D/O, now explicitly doubtful. Transcendant, générisation and page 37 agree.'),
'B11':('low','The middle acronym letter has a vertical with an upper bowl and low continuation, permitting D/P; add the local alternative. Action and normalisation remain plain and differ from H as already logged. MD-graphes and 45 agree.'),
'B12':('low','A clear y descends in déployement. The final article and endings are compressed: retain des/du, prefer singular groupoïde and fondamental with plural alternatives, without forcing agreement. Normaux above has a clearly crossed x, unlike the final tall return. Page 52 agrees.'),
'B13':('low','The detached terminal after leur can be its r or an additional s after a compressed r; keep their existing doubt. Dévissage has no extra s before en. Paired quote ticks surround types élémentaires and raised locales; insertion attaches before générales. All reference numbers agree.')}
out=[]
for b,(c,e) in ev.items():
 final=first[b]
 for a,z in repl:final=final.replace(a,z)
 d=dict(box=b,changed='yes' if final!=first[b] else 'no',confidence=c,evidence=e)
 if final!=first[b]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
