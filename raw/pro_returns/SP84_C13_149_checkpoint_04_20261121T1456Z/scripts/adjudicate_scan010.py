"""Single-use application of visual independent-audit decisions for scan010."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];ch={}
def c(k,e,s='first',final=None):
 ch[k]={'personally_inspected':True,'selection':s,'evidence':e,'changed':'no' if s=='first' else 'yes'}
 if final is not None:ch[k]['final']=final
c('b02','The indexed field letter has a full-height stem, upper loop/arm and separate descending diagonal, supporting capital K with the small zero. The preceding short group has the tall l and a compact rounded low mark, but does not isolate an apostrophe securely from a possible le ending; mark l’a/le. The full rational indices, bars and commas are unchanged.','custom',r"sous-groupe ouvert de $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$, qui, on \unsure{l'a|le} vu, correspond au sous-corps $K_0$ de $\overline{\mathbb Q}/\mathbb Q$,")
c('b03','Two hooked strokes stand before the separate e of extension. They meet at low level like a looped u but could also be two opening quotation hooks. Unlike the detached high pair before lisses in b13, their connection is not separable. Retain uncertainty and add the quotation alternative; no closing quotation is supplied. The slash and double-stroked Q are secure.','custom',r'\unsure{u|``} extension finie $/\mathbb Q$')
c('b06','The initial two-leg sign is small and begins below the E capital roof, matching the kernel pi introduced on scan009; retain lowercase pi. The Gamma roof has two close dark terminal strokes, one possibly a prime, so the existing Gamma/Gamma-prime doubt remains. The downward connector has a curved hook at its top and a distinct V-shaped head below; retain the hook omitted by the second reading. The first horizontal connector is a capped shaft, the three subsequent heads are visible, and all bars, indices and 1s agree.')
c('b07','The three compressed units before K are bent/looped s strokes; the last has a descending return and no separate dot, unlike nearby dotted i. Retain literal sss. After Q the i has a high dot, followed by a low stop, open e and another low terminal mark: i.e., not ici. The small angular kernel sign matches b06 and scan009 and remains pi. NB is underlined; both equal bars, (1), alg. stop, all Q signs and full index are present.')
c('b09','The parenthesized numeral is 9. The K, both equality bars, rightward lower limit arrow, its dotted i index and A_i agree. Display dollars and spacing are representation only.')
c('b13','Two detached dark high ticks stand immediately before the l ascender, distinct from the low U_i index dot and the clipped descenders above. They are opening quotation marks and were missed in the first reading. Add them; there is no closing pair before slash-Q or the comma. Retain the inserted status and complete words and formula.','custom',r'\inserted{i.e. les $U_i$ ``lisses$/\mathbb Q$,}')
c('b14','The left end curves upward into a short hook, while the main lower shaft extends much farther right. There is no matching long upper branch of a subset sign and no independent arrowhead at the thick right end. Keep the literal left-hooked shaft. Both U indices are visible, descending j at left and dotted i at right.')
c('b16','Both parentheses, f with dotted i and descending j, membership, A_i, diagonal setminus, braces and zero are present. Moving the parentheses inside or outside math dollars is syntax only.')
c('b17','The thin foliation has a closed upper oval and long descending stem curving left: 9. It is a separate marginal number, not an author-page heading; keep the margin wrapper.')
(R/'documentation/149_scan010_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan010.tex';s=p.read_text().replace("on l'a vu",r"on \unsure{l'a|le} vu").replace(r'\unsure{K_0|k_0}','K_0').replace(r'\unsure{u} extension',r'\unsure{u|``} extension').replace(r'\inserted{i.e. les $U_i$ lisses',r'\inserted{i.e. les $U_i$ ``lisses');p.write_text(s)
p=R/'reviews/149_scan010.json';r=json.loads(p.read_text());cs={x['id']:x for x in r['changes']}
def upd(i,b,final,**kw):
 x=cs[i];x.update(final=final,evidence=ch[b]['evidence'],crop=f'crops/149_scan010_second_{b}.png',**kw)
 q=next(q for q in r['audit_boxes'] if q['box']==b);x['box']=[q[k] for k in ('x0','y0','x1','y1')]
upd('c01','b02',r"on \unsure{l'a|le} vu",confidence='medium')
upd('c18','b02','K_0',confidence='high')
upd('c02','b03',r'\unsure{u|``}',confidence='medium')
upd('c13','b13',r'\inserted{i.e. les $U_i$ ``lisses$/\mathbb Q$,}',against_C=True,against_H=True,confidence='high')
r['doubts']=[d for d in r['doubts'] if d['place']!='main line 3, indexed field name']
for d in r['doubts']:
 if d['place']=='main line 4, cluster before extension':d.update(reading=r'\unsure{u|``}',alternatives=['u','opening quotation pair'],reason=ch['b03']['evidence'])
r['doubts'].append({'place':'main lines 2–3, short group before vu','reading':r"\unsure{l'a|le}",'alternatives':["l'a",'le'],'confidence':'medium','reason':ch['b02']['evidence']})
for d in r['decisions']:
 if d['id']=='M0975':
  d.update(reading=r'\unsure{u|``}',evidence=ch['b03']['evidence'],crop='crops/149_scan010_second_b03.png')
  q=next(q for q in r['audit_boxes'] if q['box']=='b03');d['box']=[q[k] for k in ('x0','y0','x1','y1')]
r['notes'].append('Independent audit: all9 differing boxes were inspected. K_0 is resolved as capital K; l’a/le and the u/opening-quotation cluster remain explicitly doubtful. Two opening ticks before lisses were added to the insertion, with no unwritten closing pair. The small angular pi is kept by comparison with its introduction on scan009; the upper Gamma prime remains doubtful. The downward hook, literal sss and i.e. are retained from their strokes.')
# Earlier notes are reading-history statements; qualify two now superseded claims.
for i,t in enumerate(r['notes'][:-1]):
 if 'K_0' in t and ('doubt' in t.lower() or 'uncertain' in t.lower()):r['notes'][i]=t+' The independent audit subsequently resolves this indexed field letter as capital K.'
r['hand'].append({'habit':'Two detached high ticks before an inserted word can be lost among adjacent descenders.','pages':[10],'consistency':'The pair before lisses is detached and dark; the lower connected cluster before extension remains uncertain and is not forced into the same reading.','misread':'Both witnesses and the first consolidated reading omitted the opening pair before lisses.'})
for d in r['diff_coverage']:
 if d.get('change_id') in ('c01','c02','c13','c18'):d['reason']='Updated by independent image-only audit; see final change and second-reading adjudication.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
