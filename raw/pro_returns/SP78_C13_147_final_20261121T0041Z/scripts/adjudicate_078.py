from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan078'
ev={
'B03':'The quotient display has an underlined G-prime, equals, underlined G divided by C and a detached final period. The difference is only placement of the prime relative to the underline macro.',
'B05':'The live left vertical trace has an upper hook and blunt lower endpoint, without two arrowhead arms. The canceled right trace has an upper hook and a distinct downward head beneath the hatching. Preserve that unequal geometry and the multiple cancellation zigzags. The upper roofs remain uncertain; the lower M roofs and horizontal arrow are clear.',
'B06':'The marginal first word has a d loop, accented e, one p descender, tall l, then a long y descender and reduced er. Retain déployer; neither distinguer nor déplacer fits that tall-l/long-y sequence. The abbreviated déf., underlined indices, raised bang and terminal exclamation agree.',
'B07':'The two Gamma formulas have distinct bang stems and detached dots, and the indicated G underlines. The first additional index is C and the second is underlined G-prime. The rest agrees; prime and script macro ordering differ only.',
'B08':'The first short word has low a/u, a raised t stroke and final m-like returns, supporting autom, not ceux. The final repetition sign has two horizontal strokes after lui-; retain the literal equals sign without expanding même.',
'B09':'The initial l and subsequent word are overlapped by marginal strokes. A detached upper stroke could be an accent of flèche or an apostrophe before a compressed hom. The full group is therefore retained as la flèche versus l’hom., unresolved; the article cannot be isolated with the earlier confidence. The crossed adjective remains a whole uncertain verticale candidate. The raised horizontale has the long h, medial tall t/l and terminal return.',
'B10':'A distinct angular, looped trace lies below de. Its crossing stems do not securely recover a letter or establish a deletion state. Retain the uncertain drawn trace, not merely the live de (97) se factorise wording.',
'B11':'The canceled word has a d loop and extended low run beneath a thick strike; it remains the doubtful donc candidate. The whole une is raised above it. No independent en stands between se factorise and this revision; do not supply the missing grammatical link.',
'B12':'Two separate dark dots stand after98, supporting the colon. The pair of objects, roofs, underlines and Gamma bang agree. The map has a left hook and a right arrowhead.',
'B13':'The small il has its dot and tall l; the following me has low joined humps and terminal return. The final phrase contains the accented v/e/r/i run and a long f ascender/descender, supporting à vérifier rather than à voir. Retain the underline on locales and the trailing ellipsis.',
'B14':'Germe de and multiplicité form the underlined phrase across the physical line break. The named M has a distinct roof and both G indices are underlined. Defini, inclusion98 and final comma agree; separate underline macros do not change the observed span.',
'B16':'The Gamma’s lower stem has a looped return, but no independently formed middle bar establishing E. Retain Gamma, the same locally written family form. Its two G indices are both bare while the adjacent M indices are underlined. The separate bang, hook and target roof are visible.',
'B17':'The underline begins beneath immersion, after l’, and continues through locale. The map target’s possible roof overlaps the par descender and remains unresolved. Only the first Gamma index is underlined. Its small raised mark is retraced and does not separate a clean stem and detached dot, so qualify the bang. The reduced et ce sera groups remain visible beneath a crossing and must not be omitted; their existing uncertainty stays. The final M has two underlined indices and no terminal period.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
repls={'B09':(r'la \unsure{flèche}',r"\unsure{la flèche|l'hom.}"),'B17':(r"\Gamma^!_{\underline G,G'}",r"\Gamma^{\unsure{!}}_{\underline G,G'}")}
p=w/'pages'/f'{page}.tex';t=p.read_text()
for k,(a,b) in repls.items():
 assert a in first[k];d[k].update(changed=True,final=first[k].replace(a,b));assert first[k] in t;t=t.replace(first[k],d[k]['final'])
p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
phrase=repls['B09'][1]
r['changes'][10].update(place='Before doubtful noun: absent alors and compressed article',final=phrase,confidence='low',evidence='There is no independent preceding word for alors. The article and following noun overlap marginal ink and now remain one unresolved la flèche/l’hom. group; no certain a/e contrast is asserted.')
r['changes'][11].update(final=phrase,evidence=ev['B09'])
a,b=repls['B17']
for x in r['changes']:x['final']=x['final'].replace(a,b)
for x in r['inventory']:
 x['first_words_or_objects']=x['first_words_or_objects'].replace(*repls['B09']).replace(a,b)
for x in r['decisions']:
 if x['id']=='M1072':x.update(reading=phrase,ink=ev['B09'],crop='147_scan078_second_root_B09_noun.png and (285,1405,625,1518); full context 147_scan078_second_B09.png and (285,1360,1000,1518)')
r['doubts'][2].update(reading=phrase,alternatives="la flèche; l’hom. (abbreviated noun)",reason=ev['B09'])
r['doubts'].append({'place':'Gamma raised mark in third margin, blind B17','reading':r'\unsure{!}','alternatives':'bang preferred; retraced raised mark','confidence':'low','reason':ev['B17']})
r['notation'][1]['sign']=b;r['notation'][1]['evidence']+=' Its small raised bang candidate remains qualified after the blind audit.'
r['unresolved'][1]='M1072 is now the whole la flèche/l’hom. group, including its compressed article; the canceled verticale also remains uncertain.'
r['unresolved'].append('The Gamma bang in the third margin is retraced and remains qualified.')
r['notes'][6]=r['notes'][6].replace('flèche and et ce sera','the whole la flèche/l’hom. group and et ce sera')
r['hand_log'][1]['witness_misreadings']=r['hand_log'][1]['witness_misreadings'].replace('Flèche, et ce sera','The la flèche/l’hom. group, et ce sera')
r['abbreviations'].append({'written':'hom. (unresolved alternative)','expansion':'homomorphisme, if the l’hom. reading is correct'})
r['notes'].append('Blind audit: all thirteen differing boxes were inspected by the main reader. The article/noun before the canceled adjective now remains a whole la flèche/l’hom. alternative, and the small raised Gamma bang in the third margin is qualified. Déployer, literal autom and lui-=, diagram97’s unequal lower endpoints, the independent trace under de, raised une, absent en, the colon after98, à vérifier, and locally missing Gamma-index underlines were retained. No new proof or computation was performed.')
r['root_review_notes']=r.get('root_review_notes','')+' All thirteen differing blind boxes inspected; two certainty refinements broaden the M1072 group and qualify the third-margin Gamma mark. The noun/article was also inspected on a focused crop.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['78']={'crops':[f'{page}_second_{k}.png' for k in ev]+[f'{page}_second_root_B09_noun.png'],'extra_boxes':{'B09_noun':[285,1405,625,1518]},'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
