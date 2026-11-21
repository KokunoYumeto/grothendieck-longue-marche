from pathlib import Path
from datetime import datetime,timezone
import json
root=Path(__file__).resolve().parents[1]; page='147_scan137'
p=root/'pages'/f'{page}.tex';t=p.read_text()
subs=[(r'\unsure{\uline{induit}}',r'\unsure{\uline{induit}|\uuline{induit}}'),
 (r'\uline{isomorphisme local}',r'iso\uline{morphisme local}'),
 (r"s'identifie \unsure{à} :",r"s'identifie \unsure{à|\inserted{can.}} :"),
 (r'où \deleted{$d$}',r"où \deleted{$\unsure{d|d'}$}")]
for a,b in subs:
 assert a in t,a
 t=t.replace(a,b)
p.write_text(t)
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text())
coords={x['file']:x['box'] for x in map(json.loads,(root/'work'/f'{page}_crops.jsonl').read_text().splitlines())}
for c in r['changes']:
 for a,b in subs:c['final']=c['final'].replace(a,b)
 if c['id'].endswith('-03'):
  c['evidence']+=' The blind crop shows two short looping strokes beneath the beginning of induit; single/double emphasis remains open, as does the possibility of earlier overwritten ink.'
  c['crop']=page+'_second_B03.png';c['box']=coords[c['crop']];c['confidence']='medium'
 if c['id'].endswith('-04'):
  c['evidence']='The long underline starts beneath the first m, after the initial iso, and continues to the end of local. The second crop exposes the left endpoint clearly.'
  c['differs_C']=True;c['crop']=page+'_second_B05.png';c['box']=coords[c['crop']];c['confidence']='high'
 if c['id'].endswith('-06'):
  c['evidence']+=' The small high loop and long low continuation above the middle of the crossed verb also permit a compressed raised can.; its letters and attachment are not settled. This is retained as an alternative to the prior doubtful à, with no lexical reading resolved.'
  c['confidence']='low'
 if c['id'].endswith('-08'):
  c['final']=r"\deleted{$\unsure{d|d'}$}"
  c['evidence']+=' A tiny slanted stroke at the upper right of the crossed letter permits a prime; the d/d-prime alternative remains open.'
  c['confidence']='medium'
for d in r['doubts']:
 if d['place']=='first prose baseline, ink under induit':
  d['reading']=r'\unsure{\uline{induit}|\uuline{induit}}'
  d['alternatives']='single or double emphasis; possible remnants of cancelled earlier ink beneath the live word'
 if d['place']=='upper long cancelled baseline, before colon':
  d['reading']=r'\unsure{à|\inserted{can.}}'
  d['alternatives']='à; a raised compressed can.; upper strokes belonging to the cancelled verb'
  d['reason']='The high loop and horizontal run are crossed and compressed; separate c/a/n letters and the attachment cannot be settled.'
r['doubts'].append(dict(place='after où, right of (227)',reading=r"\deleted{$\unsure{d|d'}$}",alternatives='cancelled d; cancelled d-prime',confidence='medium',reason='A tiny upper-right oblique can be a prime or part of the crossing stroke. The lower d-loop is visible.'))
r['notes']+=' Blind audit corrects the underline span to iso + underlined morphisme local. It adds local alternatives for the looping emphasis under induit, a raised word inside the cancelled line, and a possible prime on the crossed d beside (227). The two short tuple separator strokes are retained literally. The short inline connector and the first horizontal connector of (229) each end with one small terminal tick; the distinct paired head arms of the right connector of (229) are absent at those two ends. Four objects, two horizontal shafts and the separate two-stroke vertical relation in (229) were recounted. No mathematical claim was checked in this audit.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text())
ev={
'B01':('The first star sits on the raised d baseline, not below it. All three upper d-shaped letters are retraced. The rightmost thin 1 and adjoining cross-stroke leave d+1/d1 open. The indices, backslash and unaccented def agree.','medium'),
'B02':('The word has a p descender, compressed ri, low v and accented e, with two raised quotation marks at either side. The codimension letter has a final tall d stem over a lower loop. Privé and d are retained.','high'),
'B03':('The short verb begins with the curling s/a group and ends in a tall crossed t: sait is retained. Two short looping strokes lie under the start of induit, so single/double underlining remains explicit as alternatives.','medium'),
'B05':('The underline begins under m, after iso, and continues through local. Its left endpoint is distinctly to the right of the first three letters.','high'),
'B06':('The live Theta exponent has d and star aligned as upper symbols. The cancelled object has a legible primed-d-star index but intersecting strokes obscure whether its main capital was D or Theta. Both underlined short words and the final period agree.','medium'),
'B07':('Two long strokes cancel the Theta expression, s’identifie and the final colon. The upper d/star are on one raised baseline. The small high loop and horizontal run above the verb admit can. as an uncertain inserted alternative to the former doubtful à, without enough exposed letters to resolve it.','low'),
'B08':('The long and zigzag cancellations cover the middle of the tuple. Its visible separator is a horizontal stroke, retained literally. One exposed point lies between the objects; a second may be covered. The small upper mark and right-end baseline remnants leave the final où doubtful.','low'),
'B09':('Two objects, one thick left arrow with two head arms and a tilde were checked. The numeral 7 is retraced, so its uncertainty is retained. At the right, the cancelled d has a small upper-right oblique that allows a prime; this local alternative is added.','medium'),
'B10':('The tuple has two separate short horizontal strokes between the second and last entries. The four d forms, both primes, all indices and parentheses agree; the raw separator is retained instead of a three-dot glyph.','high'),
'B11':('The final abbreviation has a low m-like run after iso, extending to a hooked finish. No final point follows it. The first isom. has its visible point.','high'),
'B12':('The 228 label, two objects, both superscript stars, prime/star indices, single right shaft, two head arms, tilde and closing comma agree. Only mathematical layout syntax differs.','high'),
'B13':('The single connector ends in a small near-vertical down tick. No separate opposing oblique arm is exposed, unlike the explicit arrow in B12. The headless shaft reading is retained; both objects and (223) agree.','high'),
'B14':('Four objects and two horizontal shafts are present. The first shaft has a small terminal tick; the second has an explicit two-arm right head. The vertical relation is a curved left stroke and straight right stroke without arrowheads. The lower star is heavily crossed and remains doubtful; no upper D has a superscript star.','medium'),
'B15':('The raised word has a low e/s run and a separate tall crossed t, supporting est. The curved stroke stays mainly above d’un, leaving cancellation and replacement attachment unresolved. The rest of the line agrees.','medium'),
'B16':('All words, indices and punctuation agree. The final D superscript star is exposed in the neighboring B15 crop. Only prime serialization and math delimiters differ.','high')}
choices=[]
for d in comp['differences']:
 b=d['box'];final=d['first']
 for a,z in subs:final=final.replace(a,z)
 if b=='B09':final=final.replace(r"\deleted{$d$}",r"\deleted{$\unsure{d|d'}$}")
 it=dict(box=b,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[b][0],confidence=ev[b][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_c',choices=choices),ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'work/root_views.tsv').open('a') as out:
 for d in comp['differences']:out.write(stamp+'\t'+page+'_second_'+d['box']+'.png\troot personally inspected the displayed disagreement crop\n')
