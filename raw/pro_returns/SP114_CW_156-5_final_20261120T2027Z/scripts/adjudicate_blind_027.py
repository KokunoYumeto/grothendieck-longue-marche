"""Explicit main-reader audit of all seventeen scan027 differences."""
from pathlib import Path
import hashlib,json,csv
r=Path(__file__).resolve().parents[1];p=r/'pages/J156-5-04_156-5_scan027.tex'
rec=json.loads((r/'review/scan027_adjudicated.json').read_text());comp=json.loads((r/'second/J156-5-04_156-5_scan027_comparison.json').read_text())
edits=[
 {'old':r'\inserted{par C5}','new':r'\inserted{par \unsure{C1|C5|C4}}'},
 {'old':r'sur les supports par $','new':r'sur les supports \unsure{par|$\vdash$} $'},
 {'old':r'\uline{\unsure{C$8_0$|C$\phi_0$}} trivial','new':r'\uline{C}$\unsure{2_0|8_0|\phi_0}$ trivial'}]
def tr(s):
 for e in edits:s=s.replace(e['old'],e['new'])
 return s
O={
2:('19:51:17','The cancelled word has a large A and a tall second stroke, favouring Alors. The thick horizontal strike masks the middle and final run. Retain the existing Alors/Ainsi alternatives; the blind reading does not make every cancelled letter plain.','low',False),
4:('19:51:17','The word de is followed by two parallel strokes standing for même. All three order signs and the terminal question mark are visible. Only line wrapping and nonbreaking-space notation differ; retain the same text.','high',False),
6:('19:51:17','NB has its separate underline. The first inequality has straight bars, the second a curved lower bar, and the implication has two shafts. Both readings give the same letters and signs; spacing commands differ only.','high',False),
7:('19:51:25','The initial Il-like group is densely retraced, so its existing doubt remains. Toute has a horizontal stroke through its upper letter bodies and a separate lower underline. Retain both cancellation and underline, with the compressed middle letters still doubtful.','medium',False),
8:('19:51:25','The raised addition starts with a tall letter stroke followed by a small mark and a g-like loop with a sweeping return. Two horizontal equals bars and a distinct detached zero are not present. Retain the figure/fig. word alternatives. Non vide has a separate underline below, not a strike through its bodies.','medium',False),
11:('19:51:25','The short group before est has a looped first letter and a tall angular second, admitting on or OK. Ramené has the low initial r/a, joined m/n run and final accent, so no extra doubt is needed there. The old H≪G and comma remain cancelled.','medium',False),
12:('19:51:54','The terminal disjointe stroke has a short low return after t; retain the first wording. The inserted comp. has a compressed m/p ending consistent with the repeated compatibility abbreviation; no distinct v is secured. Both empty signs have a loop on a long slanting stem, the page’s phi-shaped empty sign, not a normalized slashed circle. The insertion has an opening parenthesis but no visible closing one.','medium',False),
13:('19:51:54','In the old formula the leading capital has a vertical stem with a projecting upper bowl/leg, supporting R rather than an enclosure bar. The lower hooked letter and the following curved delimiters survive under two crossing lines. Retain the existing R_G(H) alternatives; an equality of two bar-enclosed supports is not individually established. The live formula below is outside the shorter blind excerpt.','low',False),
14:('19:52:15','The complete proof was checked: both disjointe endings have a small return after t, the old formula remains crossed, and the final empty sign is phi-shaped. In the inserted reference, the narrow straight stroke immediately after C has a small foot; the larger loop to its right belongs partly to the descender of disjointe above. Prefer C1, keeping C5/C4 as alternatives, and preserve attachment after G-prime.','medium',True),
15:('19:52:15','The tight crop separates a narrow near-vertical stroke with a small lower foot after C from the long looping descender of the word above. This favours the blind C1 over the former certain C5. Overlap prevents a secure digit, so retain C5 and C4 alternatives rather than infer the reference from the argument.','medium',True),
16:('19:52:15','Famille has an F, a low a/m group and two adjacent tall l strokes. The following word has the i/n/t and -section sequence under the zigzag cancellation, with its final s unresolved. Retain the readable heading and its separate underlying broken underline; the second word is not physically illegible throughout.','low',False),
17:('19:52:40','The q loop, en, est-il, autres and axiomes letter groups are readable, as are the two final colon points. The two strings differ only by wrapping and the nonbreaking space before the colon.','high',False),
18:('19:52:40','The first connective after F has two low s-like turns and a separate i mark, supporting ssi, not est. Si starts with the larger S shape. After supports the high vertical and rightward low stroke can be a highly compressed par or a turnstile-like mark; retain par as preferred but add the visible-sign alternative. The entire formula has H-prime, both pairs of bars and a phi-shaped empty sign.','medium',True),
20:('19:52:59','After the overwritten capital, the low u, b-like upright/curve, d loop and successive dotted/low groups continue across one word into -sion. The following word has the in-dui-te strokes, not the longer repeated-m group required by immédiat. Retain Subdivision induite and the uncertain underlying capital. The pronoun has a low a return; retain la.','medium',False),
21:('19:52:59','The thick initial is a superposition with a vertical and two surviving loops. The following low u joins the b/d/i/v/i/s/i/o/n sequence; the apparent parentheses in the blind reading arise from tall curved letter strokes. No distinct complete Bon/Som word precedes a separate parenthetical disj. Retain the local overwritten-letter uncertainty.','low',False),
22:('19:52:59','After vérifiera the compressed terminal sequence has possible to/polo-like groups, a descending loop and dotted short stroke, but cannot be read letter by letter. Retain topologique/topologiquement/de tte façon as unresolved; the blind ch./qfs. groups do not securely establish another word. The lower label is also in this crop and is revised in B23.','low',True),
23:('19:52:59','After the clear underlined C, the numeral-like mark has an open upper curved head and a descending return into a small lower loop. This favours 2 over a fully closed two-loop 8, but 8 and phi-like forms remain possible. A distinct small circle sits lower to its right. Only the C underline is securely visible before the page edge; revise to underlined C with the doubtful lowered-zero label.','low',True)
}
dec=[]
for x in comp:
 if not x['different']:continue
 k=int(x['box'][-2:]);tm,ev,conf,ch=O[k];v=tr(x['first'])
 if k==22:v+=' '+r'\uline{C}$\unsure{2_0|8_0|\phi_0}$ trivial'
 dec.append({'box':x['box'],'changed':ch,'final':v,'evidence':ev,'confidence':conf,'crop':f'crops/second_scan027_{x["box"]}.png','viewed_utc':f'2026-11-20 {tm} UTC'})
with (r/'second/J156-5-04_156-5_scan027_boxes.tsv').open(newline='') as f:bs={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
updates=[]
def up(id,k,**kw):
 b=bs[f'scan027-B{k:02}'];kw.update(evidence=O[k][1],crop=f'crops/second_scan027_scan027-B{k:02}.png',box=[int(b[z]) for z in ('x0','y0','x1','y1')],main_decision='Main-reader decision after independent blind reading; see first/second/final audit.')
 updates.append({'id':id,'fields':kw})
up('027-23',15,final=r'\inserted{par \unsure{C1|C5|C4}}',against_C=True,against_H=True,confidence='medium',consequential=True)
up('027-24',15,final=r'\unsure{C1|C5|C4}',certainty_only=False,review_only=True,merged_into='027-23',against_C=False,against_H=False,confidence='medium')
up('027-35',18,final=r'\unsure{par|$\vdash$}',confidence='medium')
up('027-45',23,final=r'\uline{C}$\unsure{2_0|8_0|\phi_0}$',confidence='low')
u=[]
for x in rec['unresolved']:
 x=dict(x)
 if x['place']=='bottom label':x.update(reading='C2_0',alternatives=['C8_0',r'C\phi_0'],reason=O[23][1])
 u.append(x)
u.extend([{'place':'inserted axiom reference after G-prime','reading':'C1','alternatives':['C5','C4'],'reason':O[15][1],'confidence':'medium'}, {'place':'C5 connector before support formula','reading':'par','alternatives':[r'\vdash'],'reason':O[18][1],'confidence':'medium'}])
inv=[]
for q in rec['inventory']:
 q={k:tr(v) if isinstance(v,str) else v for k,v in q.items()};inv.append(q)
out={'scan':27,'page_before_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'edits':edits,'decisions':dec,'record_updates':updates,'unresolved_replace':u,'inventory_replace':inv,'changed_loci':['027-23','027-35-certainty','027-45'],'notes_append':['The independent audit makes the raised axiom reference after G-prime doubtful: C1 is now the preferred visible digit, with C5 and C4 retained. The earlier live prose reference to C5 is unchanged; it does not license correcting the raised reference. The lowest label is preferred as C2_0, with C8_0 and a phi-like form retained; the numerical sequence is not used to force 8. The mark before the support-intersection formula is retained as doubtful compressed par/turnstile.']}
(r/'second/scan027_adjudication_input.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(dec),'decisions;',len(edits),'edits')
