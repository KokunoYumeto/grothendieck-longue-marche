from pathlib import Path
import json
w=Path(__file__).resolve().parents[1]; page='147_scan061'
c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B01':'The raised pairs at both ends of élémentaires are quotation strokes, not guillemets. The two encodings denote the same word and quotes; retain the prescribed backticks/apostrophes.',
'B02':'The initial letter of the live lower word has a low oval to the left of its ascending loop, establishing d rather than a simple l. Its low continuation ends in the s return: des. The guide passes above it and descends into the preceding gap, without cancelling des.',
'B03':'Both M letters have independent peaked hats; the second alone has a superscript upright with its separate dot. Both g,nu indices and terminal point agree; math wrappers/order of exponent only differ.',
'B04':'Number8, inequality less-than-or-equal2 and detached terminal point are visible. Each physical heading line has an underline; the split versus single uline encoding does not change the reading.',
'B05':'Cas has a separate underline and et another; neither M is underlined. Both hats, the first dotted exclamation and both0,4 indices are visible. After the d the compressed low tail could be e or es, so the blind de does not remove the existing de/des doubt.',
'B06':'Commençons has the successive low m strokes and the c/cedilla form; par and the hat-M with dotted exclamation and0,4 agree. No substantive difference.',
'B07':'The diagram has one isolated point under I(4), two filled endpoints under I-prime(2) and I-double-prime(2), and a right arrow labelled3 crossing the vertical rule. The left brace, Codim capitals and76 agree. One and two raised strokes are visible, not dotted exclamations; the reader’s separate encoding addendum correctly identifies the intended primes. Retain the first source-traced geometry.',
'B08':'The interlinear se and p/t/looped-g sequence are recoverable. The low strokes beyond g, a nearby descending stroke from the upper line, and a small raised return leave the full ending less secure than the first report claimed. Retain se partageant first but restore uncertainty against se partage. The curved lower line ends in its own hook, not a separate comma. In the main line quelc. has q, low ue, tall l, short c and point; no full quelconque or distinct longer abbreviation is established.',
'B09':'I has one raised short stroke in the first partition and two in the second; cardinal2 is plain. The reader’s prime addendum resolves only the encoding, and the first apostrophe notation is retained.',
'B10':'Chacun ends in low n followed by comma; donne has d plus low joined strokes and no final tall t. The numeral3 and spécialisations différentes agree. Only math wrappers differ.',
'B11':'The word begins maxi and continues in compressed low strokes. There is no tall l/e sequence for maximale, but the terminal small return does not securely distinguish the full maxima from maxim. Restore uncertainty on this ending; the separate following dash remains.',
'B12':'Sûr has a short circumflex; aux ends in an angled x; pts is abbreviated. U has subscript0,3. No extra word or comma follows the formula. The differences are apostrophe and math encodings only.',
'B13':'After on the joined a-u-r-a strokes continue well beyond a; no independent v word division establishes on a vu. Retain on aura. The first M alone has a hat, both have dotted exclamations; the doubled P/Z forms,1 exponents,0,4 and0,3 indices and removed0,1,infinity set agree.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
old=r'\inserted{se partageant}'; new=r'\inserted{\unsure{se partageant|se partage}}'
d['B08'].update(changed=True,final=c['B08']['first'].replace(old,new),crop=f'{page}_second_root_B08_word.png')
old2='de la strate maxima ---'; new2=r'de la strate \unsure{maxima|maxim.} ---'
d['B11'].update(changed=True,final=c['B11']['first'].replace(old2,new2))
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex'; t=p.read_text()
for a,b in [(old,new),(old2,new2)]: assert a in t; t=t.replace(a,b,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json'; r=json.loads(p.read_text())
row=next(x for x in r['changes'] if x['id']=='061-11'); row.update(final=r'\unsure{maxima|maxim.}',evidence=ev['B11'],confidence='low',crop=f'{page}_second_B11.png',box=[283,1775,1662,1902])
mark=next(x for x in r['decisions'] if x['id']=='M1034'); mark.update(decision='undecided',reading=r'\unsure{se partageant|se partage}',ink=ev['B08'],crop=f'{page}_second_root_B08_word.png (650,1420,1040,1515)',confidence='low')
r['doubts'] += [
{'place':'Interlinear addition before suivant','reading':r'\unsure{se partageant|se partage}','alternatives':'se partageant; se partage','confidence':'low','reason':ev['B08']},
{'place':'de la strate maxima','reading':r'\unsure{maxima|maxim.}','alternatives':'maxima; maxim.','confidence':'low','reason':ev['B11']}]
r['unresolved'] += ['Interlinear se partageant/se partage: compressed ending near an upper-line descender.','Strate maxima/maxim.: full final a versus abbreviation remains uncertain.']
r['notes'].append('Blind audit: all thirteen differing boxes were personally rechecked, with a focused enlargement of the interlinear ending. The first-stage resolution of M1034 is superseded: se partageant/se partage remains uncertain. Maxima/maxim. is also qualified; neither suffix is completed from the mathematical argument. Primes in I-prime/I-double-prime are confirmed directly; the blind reader supplied a separate notation addendum without altering the frozen TSV.')
r['root_review_notes']+=' All thirteen differing second-reading boxes and the focused B08 crop personally viewed; two certainty changes retained in the audit history.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json'; v=json.loads(p.read_text()); v['61']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_B08_word.png'],'observations':ev}; p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
