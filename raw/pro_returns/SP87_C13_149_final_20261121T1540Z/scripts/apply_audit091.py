from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan091';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
oldK=r'\unsure{\mathcal E_{\widetilde K}|\mathcal E_{\widetilde U}}';newK=r'\mathcal E_{\widetilde K}'
tr=r'\unsure{tr.-scend|tr.-scendance}';ref=r'\unsure{réf|$N$}';cancel=r'\deleted{\unsure{de|d}}'
repls={r'\deleted{\unsure{le|sur}}':r'\deleted{\unsure{leur|le|sur}}',oldK:newK,r'\deleted{\unsure{?}}':cancel,'transcendance':tr,r'$\unsure{N}$':ref,r'\deleted{\unsure{peut}}':r'\deleted{\unsure{peut|permet}}'}
for a,b in repls.items():assert a in t,a;t=t.replace(a,b)
pp.write_text(t)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
def upd(place,box,**kw):next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{box}.png',box=mf[box]['coordinates'],**kw)
upd('struck_before_article','B003',final=r'\deleted{\unsure{leur|le|sur}}',evidence='A tall first l-like loop is followed by a low e turn, a longer joining stroke and an additional upward/right terminal return. Those extra strokes favor leur over the former le; the dense lower cancellation still permits le or sur. The live article to its right is separately retraced and remains le|de.',against_c=True,confidence='low')
ek='The subscript has a long left limb, sharp low junction, rising oblique branch and short returning right foot. The large K in deg tr K on this leaf provides the same structure; the opening U has a rounded basin, and the clear eta control on 102 has a longer left-returning descender. Cross-leaf and same-page handwriting settle this shape as K.'
upd('first_N_identification','B004',final=newK+r"=N_{s'}",evidence=ek)
upd('second_N_identification','B012',final=r"N_{s'}\simeq"+newK,evidence=ek)
ede='The crossed sublabel beneath the live isomorphism has a low oval leading into a tall returning stem, and a small independent rightward trace. These support de, with d alone possible if the last trace belongs to overworking. Replace the former editorial question-mark placeholder with the legible doubtful letters; no source question mark is asserted.'
upd('cancelled_under_equivalence','B006',final=r"T\underset{"+cancel+r"}{\simeq}I_{s'}",evidence=ede)
eref='After de, two small low turns precede a tall stroke that descends and returns left well below the line. That long f-like return supports the compressed abbreviation réf rather than a single capital N. The initial letters and accent are small enough that N remains an explicit alternative; there is no subscript zero. The following disons Q is clear.'
upd('corps_de_N','B009',final='de '+ref,evidence=eref,against_c=True,confidence='medium',kind='abbreviation expanded or spelling modernised')
upd('struck_peut','B017',final=r'\deleted{\unsure{peut|permet}} peut',evidence='The crossed first word has a p descender, a long low run and a final tall t-like stroke. Cancellation merges the internal turns, allowing peut or permet; neither is resolved. A second complete live peut follows, distinct from the cancellation.',confidence='low')
etr='A crossed t and low r are followed by a separate dark point and short horizontal dash, then s/c/e/n and tall d. A long low return follows d but does not expose enough independent letter turns to decide whether ance is written. Preserve the short form tr.-scend first, with tr.-scendance as an alternative; do not expand the initial tr. to tran.'
r['changes'].append(dict(place='short form tr.-scend',c=r'\unsure{transcendance}',h='transcendance',final=tr,evidence=etr,crop=f'crops/second_{p}_B007.png',box=mf['B007']['coordinates'],confidence='medium',kind='abbreviation expanded or spelling modernised',against_c=True,against_h=True,marked_in_h=False,consequential=False))
for m in r['marks']:
 if m['id']=='M1255':m.update(decision='undecided',reading=tr,evidence=etr,crop=f'crops/second_{p}_B007.png',box=mf['B007']['coordinates'],confidence='medium')
 if m['id']=='M1256':m.update(reading=ref,evidence=eref,crop=f'crops/second_{p}_B009.png',box=mf['B009']['coordinates'])
r['unresolved']=[x for x in r['unresolved'] if x['place'] not in {'first_N_identification','second_N_identification'}]
for u in r['unresolved']:
 if u['place']=='struck_before_article':u.update(reading=r'\deleted{\unsure{leur|le|sur}}',alternatives='leur / le / sur, the extra terminal return favors leur')
 if u['place']=='cancelled_under_equivalence':u.update(reading=cancel,alternatives='de / d under cancellation; no editorial placeholder remains')
 if u['place']=='corps_de_N':u.update(reading=ref,alternatives='compressed réf / capital N')
 if u['place']=='struck_peut':u.update(reading=r'\deleted{\unsure{peut|permet}}',alternatives='peut / permet, internal letters crossed',confidence='low')
r['unresolved'].append(dict(place='short form tr.-scend',reading=tr,alternatives='terminal ance or long final d return; initial tr.- is secure',confidence='medium'))
for h in r['hand_observations']:
 if h['habit'].startswith('A sharply angular K'):h.update(evidence=ek,witness_errors='C fixes U in both N-identifications; H has K. The blind eta reading is excluded by the short foot and same-page K control.')
r['hand_observations'].append(dict(habit='A long final pen return must not be expanded into an entire expected word ending.',pages='091',evidence=etr,witness_errors='Both witnesses and first consolidation expanded the abbreviated form to transcendance.'))
r['abbreviations'] += [dict(form='tr.-scend',expansion='transcendance; the possible terminal ance is uncertain'),dict(form='réf',expansion='référence, proposed short form in corps de réf; N remains an alternative')]
for i in r['inventory']:
 for a,b in repls.items():i['first_words_or_objects']=i['first_words_or_objects'].replace(a,b)
r['notes'] += '\n\nBlind adjudication preserves the abbreviated tr.-scend form: point and dash follow tr, while the long final d return leaves ance uncertain. The earlier full transcendance resolution is withdrawn. The form previously proposed as N after corps de now favors the compressed short form réf, from the low initial turns and long f-like descender, with N still explicit as an alternative. Both subgroup indices resolve to K from the same-page deg tr K and the cross-leaf short-foot controls, rather than U or eta. Cancelled leur is preferred before the live le/de; the sublabel below the isomorphism now reads doubtful de/d rather than an editorial question-mark placeholder. Cancelled peut also admits permet. All fourteen differing boxes were inspected.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B001':'Angular 4 and top-bar/curved-foot 5 are clear. The head position and main hand support author page 45, already represented by mspage.',
'B002':'The word before equals starts with an open n-like turn and ends beneath a detached dot over its right-hand stroke: ni, not a closed o followed by u. Keep the two-level equals short form. The local-ring oval below a wave is O, with no numeral role; the preceding U has only its own tilde and no extra nested O.',
'B003':'The tall first l-like loop, small e turn, longer low joining run and final upward return support leur, though overworking still allows le or sur. Prefer leur under doubt. The live article has a thick retraced base and stays le|de; the blind confident le does not separate the overwritten junction.',
'B004':ek,
'B006':ede,
'B007':etr,
'B008':'The large letter has the same sharp left junction, rising branch and short right return as the subgroup K. N would require a distinct second upright and diagonal structure not present here. Keep literal deg tr K minus 1, with no abbreviation points supplied.',
'B009':eref,
'B012':ek+' Retain the equality/isomorphism orientation, N_s-prime, plongé, and the normalizer indexed by E_Xs; the extra right context is already present.',
'B014':'All source words agree: the two group terms, long dash, mais de, underlined deuxième and espèce with its stop. Calligraphic wrappers and the line break are encoding differences only.',
'B016':'The crop plainly includes the tall crossed f and low de at left, as well as U above S separated by a horizontal bar. Preserve all of them; the narrower blind excerpt is a scope difference, not an omission in the manuscript.',
'B017':'A p-shaped descent and tall terminal t survive the first cancellation. The internal stroke is long and merged; permit peut/permet under doubt while retaining the separate live peut. No complete additional letters are claimed.',
'B018':'The first s is small relative to the full capital S elsewhere in the line. Parcourt has a long p then low a/r/c/o/u/r turns and tall t; prenant would omit visible intermediate turns. After l-apostrophe a small e turn, n hump and terminal s return support l’ens. Keep the short form without a stop.',
'B020':'A thin looped 9 with descending tail and an oval 0 stand at the lower edge. Keep marginal foliation 90, distinct from author page 45.'}
changed=['B003','B004','B006','B007','B009','B012','B017'];d={b:dict(evidence=v,changed=b in changed) for b,v in e.items()}
for b in changed:
 f=cs[b]['first']
 for a,z in repls.items():f=f.replace(a,z)
 d[b]['final']=f
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
