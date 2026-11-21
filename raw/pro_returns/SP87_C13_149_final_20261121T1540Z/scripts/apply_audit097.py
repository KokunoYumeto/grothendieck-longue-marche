from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan097';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
for a,b in [(r'composant\unsure{.}','composant.'),(r'\unsure{dernières|derniers}','derniers')]:
 assert a in t,a
 t=t.replace(a,b)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
e={
'B001':'The large upper number has the angular open 4 and two joined loops of 8. Keep author page48; the difference is the wrapper in the excerpt.',
'B003':'The parenthesis is followed by one capital M, with two tall sides and a central valley, and a separate short horizontal bar above it. Both readings agree on the visible abbreviation; retain the text-macron convention. The apostrophe in ailleurs is a detached stroke, unchanged.',
'B006':'The large looped E has a small k with a tall left member and low right branch. There is no separate prime, and the comma is detached at right. The mathcal/plain difference is typographical.',
'B008':'After en the tall looped l flows into one small closed a body, without an independent final s, so retain la over les. A separate dense round point lies after the final t of composant, in punctuation position with white paper on each side. Resolve the former doubtful point as a full stop; the following avec remains as written despite the interruption.',
'B010':'The small index has a taller left stem and a lower sharp right return, matching the k in the adjacent E_k occurrences rather than an equal-height n. A distinct short oblique prime lies above-right of it, separated from the longer dash further right. Retain k-prime; the blind excerpt missed the separate prime.',
'B011':'The Gamma has its own detached prime; the following open left-facing curve is subset, then looped E and low k. There is no prime after this k. Both readings agree on the ink, with only a font wrapper difference.',
'B012':'The inserted definie par (29) is above the baseline. Its long leader turns down before the existing body comma; the right hook is continuous with the leader and is not another comma. Before the dark d of definissant, the proposed le/re consists of extremely pale hollow double outlines unlike the filled live strokes. These do not establish a live word or a recoverable cancelled word; retain no added word and document the trace uncertainty. Font wrappers do not change the formula.',
'B015':'After the dotted i the ending has one low e return, a pointed r shoulder and the final s, followed by a separate comma. No extra e body follows r, and no grave accent stands above e. Read derniers, not dernieres; this decision is from the strokes, not gender agreement.',
'B016':'The index k(s) and the n-apostrophe-apparaissent sequence agree. The apostrophe is a separate dark mark after the low n, and the two long p descenders are clear. Only apostrophe encoding differs.',
'B018':'The O is oval with a separate horizontal underline, followed by small s, a slash, three peaked m strokes and small s. The two readings agree on every visible part; preserve the established mathcal O and mathfrak m typography.',
'B020':'The lower f stem and two i dots survive the strike, but the joined bodies remain obscured, so cancelled finie stays doubtful. The additional crop audit_149_scan097_final_insertion.png (1280,2140,1570,2340) restores the tops clipped by B020. The raised replacement has a short r/e entry, looped tall l, the compressed a/t/i middle and low v/e ending, followed by a separate upright numeral1. The proposed qlconq has neither a final q descender nor a place for this distinct numeral. Retain inserted relative1; the long descending stroke crossing its beginning belongs to the cancelled f below, not an initial q.',
'B021':'The small lower-left digits show a looped9 with a long descender and an open-top6 with a closed lower bowl. Keep margin96 in the thinner foliation hand.'}
def upd(place,b,**kw):
 next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{b}.png',box=mf[b]['coordinates'],**kw)
upd('composant_stop','B008',final='.',evidence=e['B008'],confidence='high')
upd('dernieres_derniers','B015',final='derniers',evidence=e['B015'],confidence='high',against_c=True,against_h=False)
upd('second_later_Ek_prime','B010',evidence=e['B010'])
upd('no_ou_before_definissant','B012',evidence=e['B012'])
r['unresolved']=[u for u in r['unresolved'] if u['place'] not in ['composant_stop','dernieres_derniers']]
r['notes']=r['notes'].replace('The dark oval after composant is provisionally a doubtful full stop; no stop, if this is an isolated pen deposit, is the alternative.','The blind audit resolves the separate dense round point after composant as a full stop.').replace('Dernières is preferred but derniers remains possible because the final low humps are compressed.','The blind audit resolves derniers: one e return, r shoulder and final s are visible without an additional e body or grave accent.')
r['notes']+='\n\nBlind adjudication: all twelve token-different boxes were inspected. The barred capital M, uneven prime presence, insertion attachment and underlined O quotient remain. La is retained against les; the stop after composant is now resolved. Derniers replaces the former feminine-first doubt. The pale hollow outlines before definissant remain undocumented as a word: they do not establish live le/re/ou. The raised relative 1 was checked in an extra crop because B020 clipped its ascenders; the distinct final numeral and absence of a terminal q descender exclude qlconq. The cancelled finie remains doubtful.\n'
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
f={'B008':'en la composant.','B015':'ces derniers,'}
d={b:dict(evidence=v,changed=b in f,**({'final':f[b]} if b in f else {})) for b,v in e.items()};assert set(d)==set(cs)
pp.write_text(t);rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
