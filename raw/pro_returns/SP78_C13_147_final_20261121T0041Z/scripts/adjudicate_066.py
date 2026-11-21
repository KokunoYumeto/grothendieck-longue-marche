from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan066'
c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B01':'The32, two hats, bang on the first M only and underline agree. The low terminal hook of de still does not exclude des, so retain the first uncertainty.',
'B02':'The first C reaches ascender height while the later c forms are low. Both arrows cross dividers; the small gap to the right of the central filled point is visible. Retain that geometry. The last raised label remains densely overworked: IV is preferred but the prime alternatives are not securely excluded.',
'B03':'The initial Dans and separate looped de/le word remain as first read. The expanded rotated crop joins the sloping tuple to the left-margin Isom expression: inside the braces are a small oval0, a separate upright1 and a tiny two-lobed infinity, followed by I with two primes. They are not two a-prime entries. Remove this material from the prose insertion and attach it to the marginal formula. The canceled relation/P trial remains doubtful; a raised1 cannot be certified under the crossing.',
'B04':'The long bounding stroke belongs to the inserted precision, not to the underlying ayant comme on avait vu, whose y-descender, low m groups and final t are traceable. The two P uprights,0,3 and looped S3 of the canceled trial remain partial evidence only; retain its whole-expression doubt. The inserted M and double P/Z agree.',
'B05':'Et, the closing parenthesis, trois points à l’infini and dash agree. The compressed middle of avait/aurait remains unresolved.',
'B06':'The rotated complete margin crop shows double P/Z, def without an accent, and the lower S3 beside the wedge. The last factor is Isom: a capped I followed by reduced s/o/m strokes, not a tilde and primes. Its parenthesized arguments continue along the same sloping baseline into B03 and read({0,1,infinity},I double-prime). This restores the whole marginal expression without supplying it from the construction.',
'B07':'The abbreviation pts, separate nb, both tall t strokes in total, numerator30, denominator2, result15 and comma agree.',
'B08':'Correspondant aux partitions and I(5) are visible; final de has no separate s. Only math delimiters differ.',
'B09':'The inserted I has one raised prime and an insertion tick leading to the gap before de. The tuple2,2,1 and the remaining prose agree.',
'B10':'Both primes, the membership sign, subscript2 and the final comma agree. The P has an angular folded bowl and long straight stem, matching the local fraktur-P convention, rather than requiring an alphabet change from the alternative script encoding.',
'B11':'The three joined s-hooks precede the independently crossed elles. The empty-set glyph is a small oval high on a long sloping stem, with a long lower extension, supporting phi rather than a balanced slashed circle.',
'B12':'The short word after i.e. has joined s-hooks without an i dot; its possible crossing still remains a state uncertainty. Forment has an f-crossbar and continuous letter joins, while justement begins with a deep j and contains two tall end strokes. These are not independently canceled words. Keep both live and retain the complete complement and2,2,1 tuple.',
'B14':'The first verb begins choisis- but its last compressed strokes do not securely separate -sant from -sons. Retain choisissant first with choisissons as an alternative. The repeated icosaèdre, orienté and ou encore un remain readable.',
'B15':'The word has a deep initial g, low au/c forms, then an independent tall h and short e. The angular stroke beneath its middle belongs to the hat of the next-line M, not to a p-descender. This separates gauche from graphe; no final d-loop supports grand.',
'B16':'The number10 is on the prose baseline after les, without an insertion guide. All visible words agree.',
'B17':'The hat, bare exponent position, inserted10 and folded P2 agree. The focused word crop shows e, tall l, a compressed low middle, then t and s; no independent acute accent is visible. The written short form is retained as elmts|elts rather than expanded to éléments.',
'B18':'The first two small words are independently crossed and remain tentatively en ordre. The next live addition has a closed o with low u, then an opening parenthesis and a long descending p followed by ar: ou(par. The lower crossed c/o-led continuation and final dash remain tentative correspon-.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
oldtuple=r" \inserted{$(\unsure{\{a',a''\}},I'')$}"
oldrhs=r"\unsure{\mathbb P^1_{\mathbb Z}\wedge_{\mathfrak S_3}\widetilde{I''}}"
newrhs=r"\mathbb P^1_{\mathbb Z}\wedge_{\mathfrak S_3}\operatorname{Isom}(\{0,1,\infty\},I'')"
repls={'B03':(oldtuple,''),'B06':(oldrhs,newrhs),'B14':('choisissant',r'\unsure{choisissant|choisissons}'),'B15':(r'\unsure{gauche|graphe}','gauche'),'B17':('éléments',r'\unsure{elmts|elts}')}
for b,(a,z) in repls.items():assert a in c[b]['first'];d[b].update(changed=True,final=c[b]['first'].replace(a,z,1))
for b in ('B03','B06'):d[b]['crop']=f'{page}_second_root_B03_B06_margin.png'
d['B17']['crop']=f'{page}_second_root_B17_word.png'
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text()
for a,z in repls.values():assert a in t;t=t.replace(a,z,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
rows={x['id']:x for x in r['changes']}
rows['066-08'].update(place='Sloping continuation of the marginal Isom formula (M1045)',final=r"\margin{$\operatorname{Isom}(\{0,1,\infty\},I'')$}",evidence=ev['B03'],crop=f'{page}_second_root_B03_B06_margin.png',box=[20,480,690,890],confidence='high',against_C=True,against_H=True,kind='insertion or placement',error_sheet_kind='insertions put in wrong place')
rows['066-27'].update(final=newrhs,evidence=ev['B06'],crop=f'{page}_second_root_B03_B06_margin.png',box=[20,480,690,890],confidence='high',against_C=True)
rows['066-29'].update(final='gauche',evidence=ev['B15'],crop=f'{page}_second_B15.png',confidence='medium')
rows['066-32']['final']=rows['066-32']['final'].replace('éléments',r'\unsure{elmts|elts}')
rows['066-32']['place']='Final main line, inserted10 before the abbreviated elements word'
r['changes'].append({'id':'066-36','place':'Final main baseline, word after inserted10','C':'éléments','H':'éléments','final':r'\unsure{elmts|elts}','evidence':ev['B17'],'crop':f'{page}_second_root_B17_word.png','box':[880,2248,1130,2340],'confidence':'low','against_C':True,'against_H':True,'kind':'abbreviation expanded or spelling modernised','marked_in_H':False,'error_sheet_kind':'abbreviations expanded spelling modernised','consequential':False})
for x in r['decisions']:
 if x['id']=='M1045':x.update(decision='other',reading=r'\{0,1,\infty\}',ink=ev['B03'],crop=f'{page}_second_root_B03_B06_margin.png (20,480,690,890), rotated -23 degrees',confidence='high')
 if x['id']=='M1047':x.update(decision='other',reading=newrhs,ink=ev['B06'],crop=f'{page}_second_root_B03_B06_margin.png (20,480,690,890), rotated -23 degrees',confidence='high')
 if x['id']=='M1050':x.update(decision='alternative',reading='gauche',ink=ev['B15'],crop=f'{page}_second_B15.png (315,2189,746,2313)',confidence='medium')
r['doubts']=[x for x in r['doubts'] if not any(k in x['place'] for k in ('M1045','M1047','M1050'))]
r['doubts'] += [{'place':'Lower paragraph, first verb','reading':r'\unsure{choisissant|choisissons}','alternatives':'choisissant; choisissons','confidence':'low','reason':ev['B14']},{'place':'Final baseline, abbreviated elements word','reading':r'\unsure{elmts|elts}','alternatives':'elmts; elts','confidence':'low','reason':ev['B17']}]
r['notes'][3]='The left marginal definition reads P^1_{I″} def = P^1_Z wedge_subS3 Isom({0,1,infinity},I″). The blind audit and a complete rotated crop establish that the sloping tuple continues this marginal formula; it is not an independent prose insertion. The capped I and following s/o/m strokes replace the first tentative tilde-I reading. These are source-reading corrections; the associated construction has not been proved.'
r['notes'][4]=r['notes'][4].replace('unresolved word gauche|graphe','word gauche, resolved in the blind audit').replace('ten elements of P_2(I)','ten elements of P_2(I), using the uncertain written abbreviation elmts|elts')
r['notes'][5]='Remaining limits include de/des, de/le, the overworked final graph index, avait/aurait, both canceled formula trials, the possible cancellation of the second sss, choisissant/choisissons, the final elmts/elts abbreviation, and the crossed en ordre/correspon-. The full Isom margin expression and gauche are now resolved. The unmatched closing parenthesis after gauche and unfinished ou(par are retained.'
r['notes'].append('Blind audit completed: all17 differing boxes, the auditor’s existing left-phrase and right-word crops, and two focused root crops were personally examined. Five boxes change. M1045 and M1047 are resolved to other readings and M1050 to its listed alternative gauche. No new mathematical check was performed during these source adjudications.')
r['inventory'][4].update(kind='margin note',position='sloping continuation of the left-margin formula above l’infini',first_words_or_objects='Isom arguments({0,1,infinity},I″), continuing the marginal definition')
r['inventory'][8]['first_words_or_objects']='P^1_{I″} def = P^1_Z wedge_subS3 Isom, continued by the sloping arguments({0,1,infinity},I″)'
r['inventory'][18]['first_words_or_objects']=r['inventory'][18]['first_words_or_objects'].replace('choisissant','choisissant|choisissons')
r['inventory'][19]['first_words_or_objects']=r['inventory'][19]['first_words_or_objects'].replace('gauche|graphe','gauche')
for i in (21,22):
 for k in ('first_words_or_objects','position'):r['inventory'][i][k]=r['inventory'][i][k].replace('éléments','elmts|elts')
r['unresolved']=[x['place']+': '+x['reading'] for x in r['doubts']]
r['root_review_notes']='First-pass review is superseded at the three resolved margin/word decisions by the complete blind-audit crop review. All17 differing boxes and the supplemental crops were viewed. The tuple is attached to Isom in the margin, and two additional prose uncertainties are explicitly retained.'
r['witness_comparison']='The consolidated page retains all recorded C/H comparisons. The blind audit corrects both drafts at the attachment of the marginal Isom arguments and the expanded final elements word. H’s0,1,infinity set is supported once its full sloping context is seen, but its prefixed equivalence and attachment are not. The canceled trials and other remaining doubts stay qualified.'
r['abbreviations'].append({'written':'elmts|elts','expansion':'éléments (the compressed written short form remains uncertain)'})
r['notation'].append({'sign':'capped I followed by reduced s/o/m','reading':r'\operatorname{Isom}(\{0,1,\infty\},I\prime\prime)','evidence':ev['B06'],'scope':'066 complete sloping marginal definition; supersedes the tentative tilde-I reading'})
r['hand_log'].append({'habit':'A sloping marginal formula can continue through an apparent interlinear insertion','pages':[66],'all_occurrences':'Complete rotated margin crop joins Isom to its0,1,infinity arguments; this is a local attachment finding.','witness_misreadings':'C splits off a tentative primed pair; H partly recognizes the set but prefixes an unsupported equivalence. The first consolidated reading repeated the split and is corrected in the blind audit.'})
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['66']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_B03_left.png',f'{page}_second_B12_right.png',f'{page}_second_root_B03_B06_margin.png',f'{page}_second_root_B17_word.png'],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
