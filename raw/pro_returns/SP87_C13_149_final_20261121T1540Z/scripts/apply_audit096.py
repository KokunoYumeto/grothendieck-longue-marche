from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan096';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
g=r'\unsure{g_i|g}';clip=r'\unsure{distingu|disting}';could=r'\unsure{pouvait|pourrait}';prefix=r'\unsure{(f_K)_*|\mathcal E f_K|f_K}'
for a,b in [('question pour des','question pour, des'),(r'\unsure{g|g_i}',g),('section distingu %','section '+clip+' %'),('pouvait déjà',could+' déjà'),(r'\unsure{\mathcal E f_K|f_K}',prefix)]:assert a in t,a;t=t.replace(a,b)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
e={
'B001':'There is an isolated descending curved mark after the final r of pour. The added context crop audit_149_scan096_pour_context.png, original (900,45,1260,180), confirms a white gap before the independent d of des, so this mark is a comma, not the next word. Retain pour, des despite the unusual punctuation.',
'B002':'The word globales has an independent underline and a separate hooked comma at right. Both are already present in the page. The frozen first box omitted the comma only from its excerpt; no text change is required.',
'B003':'The letter after the slash has a tall looped left member plus two returning right lobes. The standalone S alternative would omit that left member. Keep X/B, without selecting from mathematical expectation.',
'B004':'The g loop and long descender are clear. At its upper-right exit there is a short downstroke and separate dot, which favor a small i index; they could still belong to a g flourish with a stray point. Prefer g_i with plain g retained. The preceding section in the second excerpt is already in the page.',
'B006':'The paper edge cuts the word after the g descender and a short low right return. That return may begin u or may only be the g exit, so retain distingu first with disting admitted. No lost é or ée is supplied.',
'B008':'The tall d flows continuously into a large upturned e-like loop before the separate une. The loop is connected and much larger than the detached apostrophes elsewhere. Keep the literal de une, not normalized d’une.',
'B009':'After the dotted i there are two separate low terminal elements, one hooked and one slanted beneath the accent. They support two e letters, so keep associée. The small pale strokes justify the existing medium confidence, not deletion of the final e.',
'B010':'Both nested and simple indices have a low sharp junction, upward branch and short right foot, matching the large K in the following sur K and neighboring K controls. They lack the long descending left-returning stroke of eta on leaf102. Keep E_UK and E_K.',
'B011':'The f and U indices match the K form in B010 and the full-size K at the end of this same crop. Keep those Ks. The rationnel ending has one tall l and a low return that may hide compressed l/e, so the existing rationnel|rationnelle uncertainty remains. Pt is already present before the first excerpt.',
'B013':'After p/o the low middle consists of two long shallow returns before the clear a/i/t ending. The second return favors v, but two compressed r strokes cannot be excluded. Keep pouvait first and add pourrait rather than select by tense.',
'B014':'The crossing above tant can be the broad shared t crossbar; an additional cancelling role remains uncertain. Keep the existing live/cancelled alternatives. The extra preceding lequel U_K is already in the page; its K has the same sharp branch and short foot as B010.',
'B015':'The upper relatif belongs to the preceding baseline and is already written in the page. Its f descender reaches the small d below, but the d bowl and e exit remain live. Both readings agree on section de; no duplicate relatif is inserted.',
'B016':'The crowded prefix has a faint opening curve before f, a small K, a return at its right and a tiny crossed trace near the subscript level. These permit (f_K)_* and make that the preferred tentative reading; E f_K and plain f_K remain possible in the overworking. The following equals, psi, colon, E_K, rightward arrow and E_UK are clear. All indices match K controls, not eta. Label29 is on the same raised insertion tier; its inclusion in the insertion wrapper is retained. The la dite crop overhang is already in the main text.',
'B017':'The paired uprights and shared crossbar match the tt short form on leaf102; the local longer terminal hook still allows tte, but does not warrant changing the form to capital H. The next word matches the complete section in B004 and B015: s/e/c, tall t, paired high and low marks for i and its dot, and a long low o/n run. The last hook is joined to that n, not an independent comma. Keep full section rather than the proposed sect-superscript abbreviation.',
'B018':'The two Qs have closed bodies and crossing diagonal tails; bold/plain wrappers are typography. The following short ou has two separate low members and no added point after Gamma_Q. Keep ou sur; the blind en alternative has no independently visible e loop or n shoulder.',
'B020':'The narrow lower-left digits are 95, with looped9 and horizontal-top5. Their edge position and thin hand distinguish the foliation from author pagination, so retain margin95.'}
def upd(place,box,**kw):next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{box}.png',box=mf[box]['coordinates'],**kw)
upd('initial_pour','B001',final='pour,',evidence=e['B001'],against_c=True,against_h=True)
upd('section_g','B004',final='$'+g+'$',evidence=e['B004'],against_c=True,against_h=False,confidence='medium')
upd('clipped_distingu','B006',final=clip,evidence=e['B006'],confidence='low')
upd('pouvait_word','B013',final=could,evidence=e['B013'],confidence='medium')
for place in ['formula_placement','formula_reading']:
 x=next(x for x in r['changes'] if x['place']==place);upd(place,'B016',final=x['final'].replace(r'\unsure{\mathcal E f_K|f_K}',prefix),evidence=e['B016'],against_c=True,against_h=True,confidence='medium')
for m in r['marks']:
 if m['id']=='M1284':m.update(reading=prefix,evidence=e['B016'],crop=f'crops/second_{p}_B016.png',box=mf['B016']['coordinates'])
for u in r['unresolved']:
 if u['place']=='section_g':u.update(reading=g,alternatives='tiny right downstroke and dot favor g_i; g flourish remains possible')
 if u['place']=='clipped_distingu':u.update(reading=clip,alternatives='last visible low return can begin u or belong to g; no ending beyond paper edge supplied')
 if u['place']=='formula_initial':u.update(reading=prefix,alternatives='opening/closing curves and small crossed trace favor (f_K)_*; E f_K or f_K remain possible')
r['unresolved'].append(dict(place='pouvait_word',reading=could,alternatives='low v-like return or two compressed r strokes',confidence='medium'))
r['notes'] += '\n\nBlind adjudication restores a separate comma after the first pour, verified in a broader root crop so it cannot be confused with the following d of des. The section label now favors g_i but retains g. The clipped word is distinguished only through distingu|disting; no unseen ending is supplied. Pouvait|pourrait remains tense-uncertain from the flattened middle. The crowded formula prefix now favors (f_K)_*, retaining E f_K|f_K; its label and insertion placement remain. All small indices retain K after comparison with the same-line full-size K and the distinct eta control on leaf102. The paired-t abbreviation remains tt|tte. The following section is written in full, matching its same-page controls, and has no separately visible comma; no sect-superscript abbreviation is introduced. All sixteen differing boxes were inspected.\n'
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
f={'B001':'pour,','B004':'$'+g+'$,','B006':'section '+clip,'B013':could,'B016':cs['B016']['first'].replace(r'\unsure{\mathcal E f_K|f_K}',prefix)}
d={b:dict(evidence=v,changed=b in f,**({'final':f[b]} if b in f else {})) for b,v in e.items()};assert set(d)==set(cs)
pp.write_text(t);rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
