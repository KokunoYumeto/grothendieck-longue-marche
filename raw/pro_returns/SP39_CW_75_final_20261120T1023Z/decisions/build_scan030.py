#!/usr/bin/env python3
"""Materialize explicitly adjudicated scan-030 readings and marks."""
from pathlib import Path
from copy import deepcopy
import json
R=Path(__file__).resolve().parents[1]
raw={w:json.loads((R/f'readers/scan030/{w}/review.json').read_text()) for w in 'ABC'}
rows={w:raw[w]['loci'] for w in 'ABC'}
amap={1:1,2:10,3:11,4:12,5:2,6:3,7:4,8:8,9:7,10:5,11:14,12:13,13:9}
cmap={1:1,2:9,3:10,4:11,5:2,6:3,7:4,8:None,9:None,10:5,11:13,12:12,13:8}
crops={1:'B/postal_code.png',5:'B/opportu.png',6:'B/opportu.png',7:'B/raised_mark.png',8:'B/problemes.png',9:'B/nationale_end.png',10:'B/signature_ticks.png',11:'B/signature_ticks.png'}
loci=[]
for n,z in enumerate(rows['B'],1):
 x=deepcopy(z);x['id']=f'S030-{n:02}'
 cr=rows['C'][cmap[n]-1]['reading'] if cmap[n] else ('problèmes' if n==8 else 'No additional marks in returned transcription')
 x['readers']={'A':rows['A'][amap[n]-1]['reading'],'B':z['reading'],'C':cr}
 x['crop']='scan030/'+crops[n] if n in crops else None
 x['decision']='Root crop inspection confirms the stated local reading.' if n in crops else 'The three independent half readings agree on this retained locus; no witness discrepancy remains.'
 x['diff_H']=False;x['H']='No H text';x.pop('box',None);loci.append(x)
q={n:loci[n-1] for n in range(1,14)}
q[1].update(reading=r'\unsure{34060|34050}',diff_C=False,confidence='low',evidence='The fourth printed digit has a filled lower bowl, heavy left contour and flat-looking upper return. These leave 6 and 5 open in the main crop; 34060 remains first without using another sheet’s postal code.',decision='Retain A and C’s candidate order; B leads with 34050. Both alternatives remain explicit.')
q[7]['evidence']='The main crop shows a small open upper arc and a distinct lower descending hooked trace. Together those visible parts support ç, retained above and slightly left of the first s of soumettre. Its inscription method is unassigned.'
q[9]['evidence']='The typed comma is followed by two smaller detached dark spots, one lower-left and one higher-right. Their count and relative positions are preserved graphically. No textual punctuation function is supplied.'
q[10]['evidence']='Two separate hooked ticks sit below the initial and beginning of the surname. Each has a broad head and a descending leftward tail, with the left head heavier. Their geometry is drawn; the earlier uncertain apostrophe representation is replaced without assigning a purpose.'

def add(location,C,reading,evidence,crop,readers,kind='drawing or diagram',confidence='high',unresolved=False):
 x={'id':f'S030-{len(loci)+1:02}','location':location,'C':C,'H':'No H text','reading':reading,'diff_C':True,'diff_H':False,'kind':kind,'H_marked':False,'confidence':confidence,'evidence':evidence,'crop':'scan030/'+crop,'readers':readers,'decision':'Main reader adjudication on the cited crop.','unresolved':unresolved};loci.append(x);return x

recipient=add('recipient, second line',"l'Education Nationale, live",r"\unsure{\deleted{l'Education Nationale}}",'The two long strokes meet the Education word. One passes through the u region, turns above the word and descends by t; the other reaches the baseline by t. The physical intersection is clear, while cancellation scope remains qualified. No assertion about authorship or dispatch is made.','main/01_recipient_crossing.png',{'A':rows['A'][5]['reading'],'B':"l'Education Nationale, live; crossing curves drawn",'C':"l'Education Nationale, live; crossing curves drawn"},kind='deletion state',confidence='low',unresolved=True)
date=add('left of the typed dateline','(absent)','Two detached compact marks, right one higher, drawn in TikZ','The root crop shows two compact dark ovals in the blank area left of Villecun, separated and rising toward the right. Their positions are preserved without a verbal reading.','C/dateline_ticks.png',{'A':'Absent from returned transcription','B':'Absent from returned transcription','C':rows['C'][5]['reading']})
edge=add('upper-right physical edge','(absent)','Angular dark trace and detached compact mark, drawn in TikZ','The edge crop shows a heavier left limb, a bent lower foot and a short right return with a detached compact mark. Nearby flecks and blur leave the textual status unresolved. The visible trace receives a small geometric approximation; no letter or numeral is supplied.','C/top_right_mark.png',{'A':'Absent from returned transcription','B':'Absent from returned transcription','C':rows['C'][6]['reading']},confidence='low',unresolved=True)

inv=[]
newdate=deepcopy(raw['C']['inventory'][4]);newedge=deepcopy(raw['C']['inventory'][5])
inv.append(newedge)
for i,z in enumerate(raw['B']['inventory']):
 if i in (18,19):continue
 x=deepcopy(z)
 if i==2:x['first_words_or_objects']=x['first_words_or_objects'].replace('34050|34060','34060|34050')
 inv.append(x)
 if i==5:inv.append(newdate)
 if i==7:
  inv.append(deepcopy(raw['A']['inventory'][8]))
  inv.extend(deepcopy(raw['B']['inventory'][18:20]))

doubts=[{'location':q[n]['location'],'reading':a,'alternatives':b,'confidence':q[n]['confidence'],'reason':q[n]['evidence']} for n,a,b in [(1,'34060','34050'),(5,'underlying m','underlying n; impression order unresolved'),(6,'live n','live m; impression order unresolved')]]
doubts += [{'location':recipient['location'],'reading':r"\unsure{\deleted{l'Education Nationale}}",'alternatives':'crossing of the line is clear; scope of cancellation remains open','confidence':'low','reason':recipient['evidence']},{'location':edge['location'],'reading':'angular trace, drawn','alternatives':'textual status and origin unassigned','confidence':'low','reason':edge['evidence']}]
notes=(R/'decisions/scan030_notes.md').read_text().replace('The handwritten signature reads','A small angular trace at the upper-right physical edge is also drawn, with its textual status unresolved. The handwritten signature reads')
rec={'scan':30,'loci':loci,'inventory':inv,'doubts':doubts,'notes':notes,'check_events':[{'statement_id':'N030.1','date':'2026-11-20','who':'GPT-6 Astra Pro; effort not exposed; root/scan030','type':'carried as background without fault found','outcome':'The letter’s own subject, names and dates are reported from the supplied page. No independent legal/historical verification or mathematical proof was performed.'}],'abbreviations':[{'abbr':a,'expansion':e,'scans':[30]} for a,e in [('M.','Monsieur'),('U.S.T.L.','Université des Sciences et Techniques du Languedoc'),('CEDEX','courrier d’entreprise à distribution exceptionnelle')]],'consequential':['The crossing of the recipient’s Education line is recorded with a qualified deletion state. No inferred status of the letter is supplied.','Three groups of detached small marks and the upper-right trace are represented geometrically; the raised ç is resolved from its lower hook.']}
(R/'decisions/scan030.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
page=(R/'readers/scan030/C/page.tex').read_text()
assert "l'Education Nationale\\\\\n" in page
page=page.replace("l'Education Nationale\\\\\n",r"\unsure{\deleted{l'Education Nationale}}"+'\\\\\n',1)
bpage=(R/'readers/scan030/B/page.tex').read_text()
start=bpage.index(r'Nationale,\mbox')
end=bpage.index(' des problèmes de votre',start)
mark=bpage[start:end]
assert 'Nationale, des problèmes de votre' in page
page=page.replace('Nationale, des problèmes de votre',mark+' des problèmes de votre',1)
(R/'pages/J75-04_75_scan030.tex').write_text(page)
print(json.dumps({'loci':len(loci),'inventory':len(inv),'doubts':len(doubts),'changes_C':sum(x['diff_C'] for x in loci),'changes_H':sum(x['diff_H'] for x in loci)}))
