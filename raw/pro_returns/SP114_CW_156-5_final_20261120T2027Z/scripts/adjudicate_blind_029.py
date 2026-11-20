"""Main-reader visual decisions for all sixteen scan029 token differences."""
from pathlib import Path
import csv,hashlib,json
r=Path(__file__).resolve().parents[1];p=r/'pages/J156-5-04_156-5_scan029.tex'
rec=json.loads((r/'review/scan029_adjudicated.json').read_text());comp=json.loads((r/'second/J156-5-04_156-5_scan029_comparison.json').read_text())
edits=[
 {'old':r'\deleted{Alors}','new':r'\deleted{\unsure{Alors}}'},
 {'old':r'\deleted{\unsure{y|l}}','new':''},
 {'old':r'\deleted{\unsure{inter.|intersection}}','new':r'\deleted{\unsure{quand|inter.|intersection}}'},
 {'old':r'\unsure{\mathfrak P|\mathscr P|\mathbb P}(L)','new':r'\unsure{\mathfrak P|\mathscr P|\mathbb P}(\unsure{L,|L_1|L})'},
 {'old':r"\unsure{s'apparente|l'apparente}",'new':r"\unsure{l'apparente|s'apparente}"}]
def tr(s):
 for e in edits:s=s.replace(e['old'],e['new'])
 return s
O={
2:('20:01:57','The cancelled word exposes A legs, the l loop and a low rounded middle, with an r-like end followed by s. The thick stroke hides parts of those bodies, so retain Alors with doubt. Ainsi is written on its own full-sized baseline below, without an insertion sign; it is the replacement line, not a raised insertion.','medium',True),
3:('20:01:57','The proposition letters, plain F/G, double less-than, on and quoted name are visible. The alleged old y/l before the live l is a disconnected brown vertical patch with ragged pale halos and separate rounded spots, unlike the continuous black pen strokes; no independent cancellation crosses it. Supplemental brown-mark crop inspected at20:02:08 confirms this. Prefer a nontextual surface mark and omit the conjectured deleted glyph, recording the physical uncertainty in notes.','medium',True),
6:('20:02:08','The left cluster has a small closed bowl with a descending stroke, more q-like than a short dotted i. Low middle strokes and a taller ascending form survive under the heavy horizontal strike. Quand is a plausible blind reading, now preferred, but its letters are not all exposed; retain inter./intersection as alternatives rather than resolve the cancellation.','low',True),
7:('20:02:08','The first group is a low looped e followed by an n run. The next compact s/e group is separate. The final word shows the two long p descenders and a tall l loop, supporting en se rappelant. Car à supposer would require different initial groups and lacks this l.','high',False),
8:('20:02:34','Two horizontal F arms remain inside the overdrawn G, so retain the old F. The P alphabet remains doubtful; L has an angular stem and foot. A separate dark short curved mark lies low after the first L but before its closing parenthesis; preserve it provisionally as a comma-like mark, with subscript1 and no-mark alternatives. The later G subset P(L) remains crossed.','low',True),
9:('20:02:34','The article before F.G has a tall l and a short open terminal return, without a closed a bowl. Retain le. En fait and the low ça marche groups are visible; the blind difference concerns only le/la.','medium',False),
10:('20:02:34','Both support bars, the wedge, equality, cap and the two i-in-I index groups are visible, followed by a detached dark stop. The two readings differ only in display delimiters and spacing.','high',False),
11:('20:02:56','The initial letter is a tall almost straight stroke with a small hooked foot, favouring l over s; retain s as alternative because the lower return is compressed. Double p descenders and the separated a/r/en run support apparente, not the adjacent double-l sequence that appellera requires. Prefer l’apparente without repairing its grammar.','medium',True),
12:('20:02:56','The cancelled phrase retains a looped initial l/a, a p descender, dotted medial material and a terminal accented t/e group. La propriété remains preferred, but the horizontal strike obscures enough of the middle to retain la présentation.','low',False),
13:('20:02:56','The cancelled phrase is left of the live continuation. The supplemental middle context inspected at20:03:52 shows the small base mark and its accent immediately before une propriété de. Retain à and the existing cancelled-word alternatives; its absence from the shorter blind excerpt does not establish omission in the ink.','medium',False),
14:('20:03:14','The initial low m humps and o movement precede a looped ascending d, an accent and the r/a/t/i/on run. The word is modération. No distinct co- prefix and second direction word are established. A continuous underline lies below it, with paired quote ticks.','high',False),
15:('20:03:14','The heading ends in the short accented -té group of Propriété, not the -sition sequence. Both order signs have bowed parallel lower strokes. The nested crossed fragment has low letter-like groups and a d-like loop, without secure separate G-prime/order/G symbols. The parenthesis and final underlined induite are resolved in their tight crops; the entire block remains obliquely cancelled.','medium',False),
16:('20:03:30','The lower strokes of both relation signs are curved, unlike straight less-or-equal bars. Retain preceq at both sites. Under the local cancellation after F, the comma-like left curve, small middle strokes and final d-like ascent do not establish the blind G-prime ≤ G; keep the existing doubtful , et des.','medium',False),
17:('20:03:30','Immédiat has its initial I, two m runs, accented e, looped d and terminal t. The next short group starts with an s-like curve then a low u/r run: sur. Supports begins with s/u and two p descenders and ends with the r/t/s run, not the longer surprenant sequence. No extra mais/un word or comma is secured.','high',False),
18:('20:03:30','The apparent p stem is the long oblique block-cancellation crossing a short s-like hook. The next low cup and rightward return are u/r, not a closed a bowl. Retain sur.','high',False),
19:('20:03:30','A dotted initial i and flattened n precede the looped d, low u/i and tall crossed t with final e. The underline is separate below. This reads induite, without a separate s apostrophe or ch pair.','high',False)
}
with (r/'second/J156-5-04_156-5_scan029_boxes.tsv').open(newline='') as f:bs={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
def ev(k):
 b=bs[f'S029-{k:02}'];return {'evidence':O[k][1],'crop':f'crops/second_scan029_S029-{k:02}.png','box':[int(b[z]) for z in ('x0','y0','x1','y1')],'main_decision':'Main-reader decision after independent blind reading; see first/second/final audit.'}
dec=[]
for x in comp:
 if not x['different']:continue
 k=int(x['box'][-2:]);tm,e,c,ch=O[k]
 dec.append({'box':x['box'],'changed':ch,'final':tr(x['first']),'evidence':e,'confidence':c,'crop':f'crops/second_scan029_{x["box"]}.png','viewed_utc':f'2026-11-20 {tm} UTC'})
updates=[]
def up(id,k,**kw):updates.append({'id':id,'fields':{**kw,**ev(k)}})
up('029-04',3,final='no deleted letter: probable nontextual surface mark',against_C=True,against_H=False,confidence='medium',kind='text not on the page')
up('029-10',6,final=r'\deleted{\unsure{quand|inter.|intersection}}',against_C=True,against_H=True,confidence='low')
up('029-19',11,final=r"\unsure{l'apparente|s'apparente}",against_C=True,against_H=False,confidence='medium')
new=[{'id':'029-BL01','place':'first P(L), low mark between L and closing parenthesis','C':'L','H':r'\mathcal L','final':r'\unsure{L,|L_1|L}','confidence':'low','kind':'omission','against_C':True,'against_H':True,'H_marked':False,'certainty_only':False,'consequential':False,'rotation_degrees':0,**ev(8)}]
u=[]
for x in rec['unresolved']:
 x=dict(x)
 if x['place']=='proposition, cancelled glyph immediately before l’appelle':continue
 if x['place']=='warning, cancelled word after F cap G':x.update(reading='quand',alternatives=['inter.','intersection'],reason=O[6][1])
 if x['place']=='lower paragraph, s’apparente':x.update(place='lower paragraph, l’apparente/s’apparente',reading="l'apparente",alternatives=["s'apparente"],reason=O[11][1])
 u.append(x)
u.extend([
 {'place':'cancelled opening word','reading':'Alors','alternatives':[],'reason':O[2][1],'confidence':'medium'},
 {'place':'first P(L), low mark after L','reading':'L,','alternatives':['L_1','L'],'reason':O[8][1],'confidence':'low'},
 {'place':'surface mark before live l’appelle (excluded from text)','reading':'nontextual surface mark','alternatives':['rubbed old y/l ink'],'reason':O[3][1],'confidence':'medium'}])
inv=[]
for q in rec['inventory']:
 q=dict(q)
 if q['element']=='029-I05':continue
 if q['element']=='029-I02':q['first_words_or_objects']=r'\unsure{Alors}'
 if q['element']=='029-I08':q['first_words_or_objects']=r'\unsure{quand|inter.|intersection}'
 inv.append(q)
out={'scan':29,'page_before_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'edits':edits,'decisions':dec,'record_updates':updates,'new_changes':new,'unresolved_replace':u,'inventory_replace':inv,'changed_loci':['029-Alors-certainty','029-04','029-10','029-BL01','029-19'],'notes_append':['The blind audit prefers l’apparente, with s’apparente retained, from the tall initial stem. This potentially awkward syntax is not repaired. The crossed word after F cap G now prefers quand, with the earlier inter./intersection alternatives retained. A low mark within the first P(L) is preserved as a doubtful comma-like mark/subscript1, with absence also possible. The conjectural old y/l before live l’appelle is omitted: its disconnected brown patches and pale ragged halo favour a surface artefact. Rubbed old ink remains a physical alternative in the doubts record; no definite authorial cancellation is asserted there.']}
(r/'second/scan029_adjudication_input.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(dec),'decisions;',len(edits),'edits')
