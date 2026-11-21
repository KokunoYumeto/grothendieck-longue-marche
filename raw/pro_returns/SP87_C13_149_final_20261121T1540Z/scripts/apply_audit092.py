from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan092';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
ex=r"\unsure{de extension|d'extension}";ent=r'\unsure{entre|dentre}';target=r'{\deleted{\unsure{\operatorname{Gal}}}\inserted{\mathcal E}}_{k(s)}'
a="En termes de sections d'extension,";b='En termes de sections '+ex+',';assert a in t;t=t.replace(a,b)
a='cette correspondance entre sections';b='cette correspondance '+ent+' sections';assert a in t;t=t.replace(a,b)
a=r'\unsure{\mathcal E_{k(s)}}';assert a in t;t=t.replace(a,target);pp.write_text(t)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
def upd(place,box,**kw):next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{box}.png',box=mf[box]['coordinates'],**kw)
eex='The d has a low loop and tall stem, then a connected rounded return before the separate initial e of extension. That connected return favors a written e rather than a detached apostrophe, so de extension is preferred, with d’extension still possible. The singular ending n has no additional s before the comma.'
upd('extension_singular','B006',final=ex,evidence=eex,against_c=True,against_h=True,confidence='medium')
upd('entre_live','B011',final=ent,evidence='The initial overworking includes a low loop and tall stroke before the e/n-like run. It may be retracing of the initial e or an extra d, so retain entre first with dentre possible. No separately readable cancelled word is asserted. The crossed t and final r/e are clear.',confidence='medium')
et='The live E is clear at the left of the crowded target. Behind and to its right are a broad lower curved remnant, a small oval and a short upright/return, with crossing strokes through them. These permit a tentative earlier Gal beneath the replacement E. Preserve that older name under doubt and mark the live E as replacement; k(s) remains legible below both layers.'
r['changes'].append(dict(place='29 overwritten target name',c=r'\unsure{\mathcal E_{k(s)}|E_{k(s)}}',h=r'\mathcal E_{k(s)}',final=target,evidence=et,crop=f'crops/second_{p}_B021.png',box=mf['B021']['coordinates'],confidence='low',kind='deletion state',against_c=True,against_h=True,marked_in_h=False,consequential=True))
for m in r['marks']:
 if m['id']=='M1267':m.update(reading=target,evidence=et,crop=f'crops/second_{p}_B021.png',box=mf['B021']['coordinates'],confidence='low')
for u in r['unresolved']:
 if u['place']=='29_target_overdraw':u.update(reading=target,alternatives='earlier Gal tentative under crossing/replacement E; k(s) clear',confidence='low')
r['unresolved'] += [dict(place='de extension / d’extension',reading=ex,alternatives='connected e-like return or apostrophe after d',confidence='medium'),dict(place='initial retracing of entre',reading=ent,alternatives='entre / dentre; initial overworking may include d',confidence='medium')]
r['inventory'] += [dict(element='29_cancelled_target',kind='deletion',position='under and right of final group name in (29)',first_words_or_objects=r'\unsure{\operatorname{Gal}}',sheet_kind='text',hand='his hand',transcribed='yes'),dict(element='29_replacement_target',kind='insertion',position='over earlier final group name in (29)',first_words_or_objects=r'\mathcal E',sheet_kind='text',hand='his hand',transcribed='yes')]
r['notes'] += '\n\nBlind adjudication gives the target correction in (29) two explicit layers: tentative cancelled Gal beneath the live replacement E, with shared k(s). The underlying letters remain low confidence, but their broader curved remnant, small oval and upright make a candidate possible; this supersedes the first-stage decision to leave the whole target undifferentiated. The singular extension remains; a connected e-like return after d now favors the literal de extension, with d’extension retained as an alternative. The heavily retraced initial of entre also admits dentre. The raised correction remains préciser, since the accented e, open c and i are visible without the l/g of prolonger. Both occurrences of l’ens remain the written short form; no abbreviation point is supplied. The barred K and headless first connector of (29) are retained. All twelve differing boxes were inspected.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B001':'The initial isolated horizontal stroke is separate from the two small following letter traces. It has no n hump; keep dash plus ou, followed by the single connected seulement and comma. Non would absorb that independent dash without a visible initial n shape.',
'B002':'The second word begins with a looped d, then low ou, a tall t and final e. Keep doute. The preceding few faded strokes do not establish every letter of sans, so keep its existing doubt. On admet would require a separate low a and an m sequence absent before that d.',
'B003':'After the l and apostrophe are a small e-like bowl, n-like rise and long s return, matching the later l’ens and the final s return of des. Keep the short form ens, not un; pts has the independent p descender and crossed t.',
'B006':eex,
'B010':'The live upper word has p/r, an accented e, open c and a separate i, followed by s/e/r. It has no tall l or g descender to support prolonger: retain préciser. In the lower cancelled word the early dotted i, t-like upright and middle p-shaped descent favor interpréter; several intervening letters remain crossed, so the existing doubt stays. Ainsi remains live at right.',
'B011':'A low loop and high initial retracing precede the n/t/r/e run. The extra loop may belong to a d or to an overwritten initial e, so keep entre first with dentre admitted; no distinct additional cancelled word is recoverable.',
'B016':'The same low e/n/s run as the upper l’ens has a terminal downward s return matching des to its right. Keep l’ens with no point before des; the blind un collapses two distinct low turns.',
'B017':'Both readings preserve clôture normale and the underlined O with S,s below. Macro/font wrappers only differ. The open upper part of O is the local-ring form, and its underline is independent ink.',
'B019':'The barred letter has a sharp low junction, rising oblique branch and short descending/right foot, matching K on this leaf and the neighboring controls. The U forms have a rounded basin. Keep K and its independent top bar, including any mathematical tension caused by that written bar.',
'B020':'After s-prime the d loop and tall stem lead into one small e-like return, then a long exit. There are no independently formed a/n/s turns. Keep de, the following S-prime with subscript s, and comma.',
'B021':et+' The complete display retains label 29, both endpoint 1s, a headless first shaft and the next three headed links; the s-primes remain attached to I and N.',
'B022':'The thin lower-left foliation is 91: a looped 9 and separate sloping 1. Its hand and edge position differ from author head pagination; keep margin 91.'}
changed=['B006','B011','B021'];d={b:dict(evidence=v,changed=b in changed) for b,v in e.items()};d['B006']['final']=ex+',';d['B011']['final']=ent;d['B021']['final']=cs['B021']['first'].replace(r'\unsure{\mathcal E_{k(s)}}',target)
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
