from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan093';rp=w/'review'/f'{p}_reviewed.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text()
strict=r'\deleted{\inserted{\unsure{ou}}}\deleted{\unsure{pas|non}}';corp=r'\deleted{est celui \unsure{du|qui} \unsure{correspond|corps de|complété}}';pi=r'\unsure{\pi|T}';prete=r'\unsure{prete|prète|préter}';ainsi=r'\deleted{\unsure{Ainsi|Aussi}}';defi=r'\unsure{definie|définie}'
for a,b in [(r'\deleted{\illegible{2}}',strict),(r'\deleted{est celui du \unsure{corps de|complété}}',corp),(r'\mathcal E_{U_{\unsure{\eta|K}}}',r'\mathcal E_{U_K}'),(r'dans $\pi$',r'dans $'+pi+'$'),(r'\unsure{prète|préter}',prete),(r'\deleted{\unsure{Alors}}',ainsi),(r"l'image \unsure{réciproque|inverse}","l'image inverse"),('définie si',defi+' si')]:
 assert a in t,a;t=t.replace(a,b)
pp.write_text(t)
mf={x['box']:x for x in json.loads((w/'second'/f'{p}_crop_manifest.json').read_text())}
def upd(place,box,**kw):next(x for x in r['changes'] if x['place']==place).update(crop=f'crops/second_{p}_{box}.png',box=mf[box]['coordinates'],**kw)
es='The upper crossed fragment has a small round o and a following u-like return; the lower fragment has a long descending loop followed by a low a-like loop and terminal s return. Tentatively read upper inserted ou and lower pas, with non possible where the heavy obliques cross. Both fragments remain cancelled. Replace the two-word illegibility placeholder with these explicit tentative layers.'
ec='The cancelled phrase begins est celui. The next tall loop, partly confluent with the inserted f above, favors du over qui. The following low c/o/r-like run, long p descent and late tall d favor correspond; the crossed low interior can also support corps de, while complété is less secure because an independent middle l is not apparent. Preserve all under doubt.'
ek='The nested small letter has a sharp low junction, rising branch and short right foot, matching the larger K at the left and the K controls on leaves 086, 088, 090, 091 and 096. It lacks the long left-returning descender of the eta on leaf102. Read K. The two connectors are horizontal shafts with slight terminal hooks but no independently formed two-sided heads. The final U has a rounded basin; it is not eta.'
epi='The small final sign has a horizontal top and a thick narrow downward body with crowded feet. Pi remains possible from two close uprights, but the body is also compatible with T. Preserve both rather than select the mathematically expected name.'
epr='The second line starts p/r, a compressed low vowel, tall crossed t and low e-like return with a terminal hook. There is no clear detached accent over the first vowel. Prefer prete, with prète retained for a faint accent and préter retained for an uncertain extra terminal r. The preceding s’inter line-end join is unchanged.'
ea='The cancelled opening has a large A, a low interior with repeated small turns, and a clear final dotted i. The i-dot and terminal i rule against Alors. Read Ainsi|Aussi, with the interior sequence still obscured by crossing strokes.'
ei='The word after image has only low i/n/v/e/r/s/e-like turns and a terminal return; it has no descending p or q and no middle dotted i of réciproque. Read inverse, agreeing with the blind reading and H.'
ed='The first e after looped d has no clearly detached acute accent. A faint trace may be lost against the tall following f, so prefer definie with définie retained. The g inequality, S, dimension 1 and three trailing points remain unchanged.'
upd('strict_parentheses','B003',final='('+strict+' strict)',evidence=es,against_c=True,against_h=True,confidence='low')
upd('crossed_corps_de','B004',final=corp,evidence=ec,against_c=True,against_h=True,confidence='low')
r['changes']=[x for x in r['changes'] if x['place']!='composite_nested_index']
upd('a_priori_placement','B008',final=r"s'annule sur $I_{s'}$ \inserted{(a priori, il envoie $I_{s'}$ dans $"+pi+'$)}',evidence='The raised parenthesis remains attached above the gap after I_s-prime. '+epi,confidence='medium')
upd('interpretation_ending','B014',final=prete,evidence=epr,against_c=True,against_h=True,confidence='medium')
upd('cancelled_Alors','B015',final=ainsi,evidence=ea,against_c=True,against_h=True,confidence='low')
upd('reciprocal_word','B017',final='inverse',evidence=ei,against_c=True,against_h=False,confidence='high')
r['changes'].append(dict(place='definie_accent',c='définie',h='(no corresponding word)',final=defi,evidence=ed,crop=f'crops/second_{p}_B019.png',box=mf['B019']['coordinates'],confidence='medium',kind='misread word',against_c=True,against_h=False,marked_in_h=False,consequential=False))
for m in r['marks']:
 if m['id']=='M1270':m.update(reading=prete,evidence=epr,crop=f'crops/second_{p}_B014.png',box=mf['B014']['coordinates'])
r['unresolved']=[x for x in r['unresolved'] if x['place'] not in ['composite_nested_index','reciprocal_word']]
for u in r['unresolved']:
 if u['place']=='strict_cancelled_fragments':u.update(reading=strict,alternatives='cancelled raised ou and cancelled lower pas|non; two layers tentative')
 if u['place']=='crossed_corps_de':u.update(reading=corp,alternatives='du|qui and correspond|corps de|complété beneath cancellation',confidence='low')
 if u['place']=='interpretation_ending':u.update(reading=prete,alternatives='prete without visible accent preferred; prète and préter remain possible')
 if u['place']=='cancelled_Alors':u.update(reading=ainsi,alternatives='Ainsi|Aussi; final dotted i rejects earlier Alors')
r['unresolved'] += [dict(place='a_priori_target',reading=pi,alternatives='crowded two-legged pi or single-stem T',confidence='medium'),dict(place='definie_accent',reading=defi,alternatives='no detached accent clear above initial e',confidence='medium')]
for x in r['inventory']:
 if x['element']=='strict_cancelled_fragments':x['first_words_or_objects']=strict
 if x['element']=='Ns_deleted_phrase':x['first_words_or_objects']=corp
 if x['element']=='a_priori_parenthetical':x['first_words_or_objects']='(a priori, il envoie I_s′ dans π|T)'
 if x['element']=='Alors_deletion':x['first_words_or_objects']='Ainsi|Aussi, cancelled and doubtful'
r['notes'] += '\n\nBlind adjudication: both cancelled fragments before strict are now tentatively recoverable as raised ou and lower pas|non; both remain deleted. The cancelled phrase after N_s′ favors correspond but retains corps de|complété, with du|qui separately doubtful. The nested index is K after comparison with the same-leaf large K and neighboring controls, withdrawing the earlier eta preference; the headless connectors remain. The parenthetic target is π|T, left doubtful from crowded strokes. The broken-line continuation is prete|prète|préter, preserving accent and final-r uncertainty. A final dotted i changes cancelled Alors to Ainsi|Aussi. The live word after image is inverse: no p/q descender supports réciproque. Definie retains accent doubt; tantot retains no circumflex because the full relevant upper area shows none. All fourteen differing boxes were inspected.\n'
# Withdraw superseded glyph examples in local hand/notation descriptions while preserving the audit history.
for key in ['hand_observations','notation_additions']:
 for x in r.get(key,[]):
  for k,v in list(x.items()):
   if isinstance(v,str) and ('η preferred' in v or 'eta preferred' in v):x[k]=v+' [Superseded by blind adjudication: nested K; see B007.]'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={'B001':'The struck est le groupe lies on the principal baseline. Both the equivalence sign and E with single-tilded K sit above that baseline beside the curved replacement leader. Keep the full equivalence as an insertion; the blind transcription merely places the sign outside its wrapper and includes the surrounding I_s-prime already present in the page.','B003':es,'B004':ec,'B007':ek,'B008':epi,'B009':'The initial p loop descends below the strike and a small o-like basin remains under the line; the u/r interior and ending are covered. Pour remains the likely word, but the original uncertainty is justified and is retained.','B010':'The first que has a horizontal stroke through its low letters and an angular q descender; cancellation remains preferred but unresolved. The following s-prime, membership sign and S-prime are distinguishable, with three trailing points. The blind uncertainty does not reveal a competing symbol to replace them.','B012':'The left small branched letter has the same compact k form as neighboring k(s) controls. Keep lowercase k; the local-ring O and tilde are clear, and font wrappers do not alter the reading. Rightward head and the leftward isomorphism head are visible. The source comma is already present after the display in the page.','B013':'The cancelled word has the p descent, a low e/u run and a final tall crossed t; passe would require a lower double-s sequence absent here. Keep peut. The curved leader inserts donc before s’inter, whose crop overhang is already in the page.','B014':epr,'B015':ea,'B017':ei,'B019':ed,'B020':'The complete area over the o has no separate circumflex. Three tall t forms and the low o support tantot, and the comma is separate. Keep the unaccented written form rather than supply tantôt.'}
f={'B003':'('+strict+' strict)','B004':corp+r" \inserted{s'identifie de $=$ à}",'B007':cs['B007']['first'].replace(r'U_{\unsure{\eta|K}}','U_K'),'B008':cs['B008']['first'].replace(r'\pi',pi),'B014':prete+' comme','B015':ainsi+' On a vu que','B017':"l'image inverse du diviseur",'B019':cs['B019']['first'].replace('définie',defi)}
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps({b:dict(evidence=v,changed=b in f,**({'final':f[b]} if b in f else {})) for b,v in e.items()},ensure_ascii=False,indent=2)+'\n')
