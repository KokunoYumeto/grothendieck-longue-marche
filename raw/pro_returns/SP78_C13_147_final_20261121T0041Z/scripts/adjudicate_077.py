from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan077'
ev={
'B01':'No opening curve precedes en; the line begins with its small low e/n body. The later closing parenthesis and colon are clear. Retain the unmatched closing parenthesis and underline rather than supply an opening one.',
'B02':'The objects, equality/isomorphism signs and vertical placement agree. The M factor has a distinct two-arm roof over I. The upper Teichmüller factor has bare I, and the lower factor has bare nu, with no detached roofs over either. Preserve those local differences, alongside upper plus and lower bang-plus; equivalent formula encodings do not alter them.',
'B03':'The sloping margin has T with a separate bang stem/dot and plus, lower g/nu, and the words groupes de Teichmüller. The two small umlaut marks belong to this local spelling. Only script order differs.',
'B04':'The initial L is a capital. The raised Gamma mark has a heavy upright, low point and lateral/retraced stroke; retain bang/natural/canceled-bang uncertainty instead of reducing it to a certain bang. The underlined G and Pi M group agree.',
'B05':'The M is overworked but retains its two tall sides and central return. Its G is underlined, while the following Gamma’s G has no independent underline. Preserve that local difference. Only math delimiters differ between readings.',
'B07':'The first canceled cluster begins with a d loop, but the thick horizontal strike merges its low ending, so de becomes a qualified candidate. Par remains doubtful under the second strike. Dans and une occupy the raised row directly above the two canceled clusters; extend the insertion to both words. The following structure d’extension continues from that raised row. S’insère remains the existing uncertain live candidate.',
'B08':'The two nontrivial pi1 terms are literally repeated with the same underlined G arguments. The line before the terminal Gamma ends bluntly without an independent arrowhead; retain the headless shaft. The terminal Gamma G is bare. The different shaft macros encode the same observed line.',
'B09':'The last short word has a d loop and low e/s continuation with a terminal return; retain des. The only raised phrase is sorte de with its curved guide, while variance remains on the main baseline.',
'B10':'Two short quotation ticks are visible at both ends of morphismes. The Pi/M and MD-graph G underlines, à and terminal period agree. Preserve the established double-quote encoding.',
'B11':'The word composée has its accent and final e, and both occurrences read variance. The underline extends through variance pour isomorphismes across the line break. The short quote marks occur in pairs; apostrophe and quote macro differences are equivalent.',
'B12':'The apostrophes in j’admets and qu’il, paired quotes around triviale, closing parenthesis and new opening double quotes before variance de are visible. No reading change is required.',
'B13':'The quotient candidate begins with a q descender, but its ending is heavily overwritten by a closed retraced loop. Keep the existing whole-word doubt. The following de MD-graphes, two closing ticks and period are distinct.',
'B14':'The pale76 is in the lower-left corner in pencil-like strokes, separate from the main pen text. Retain it as a marginal foliation, not an authorial manuscript page heading.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
a=r'\deleted{de \unsure{par}} \inserted{dans} une';b=r'\deleted{\unsure{de} \unsure{par}} \inserted{dans une}'
assert a in first['B07'];d['B07'].update(changed=True,final=first['B07'].replace(a,b))
p=w/'pages'/f'{page}.tex';t=p.read_text();assert first['B07'] in t;t=t.replace(first['B07'],d['B07']['final']);p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
r['changes'][17].update(final=r'\deleted{\unsure{de} \unsure{par}}',confidence='low',evidence='The first canceled word has a visible d loop, but its short ending merges with the thick strike; de remains the preferred uncertain candidate. The second cluster has a p descender and buried a/r bodies, so par remains uncertain. Both strikes are preserved in the contiguous deleted span.')
r['changes'][18].update(place='Raised dans une above the canceled trials',final=r'\inserted{dans une}',against_C=True,against_H=False,evidence='Dans and une are both on the raised row directly above the two canceled clusters. Une lies above the crossed par, while the original s’insère/de/par row lies lower. The blind audit therefore extends the insertion wrapper through une. The following structure d’extension continues along the raised row.')
for x in r['inventory']:
 s=x['first_words_or_objects'];s=s.replace(r'\deleted{de \unsure{par}}',r'\deleted{\unsure{de} \unsure{par}}').replace(r'\inserted{dans} une',r'\inserted{dans une}')
 if s==r'\inserted{dans}':s=r'\inserted{dans une}'
 x['first_words_or_objects']=s
r['doubts'].append({'place':'First canceled word before raised dans une, blind B07','reading':r'\deleted{\unsure{de}}','alternatives':'de preferred; ending buried under strike','confidence':'low','reason':ev['B07']})
r['unresolved'].append('The first canceled de candidate has an obscured ending and remains qualified.')
r['notes'][4]=r['notes'][4].replace('struck par, and quotient retain the four explicit doubts','struck de/par, and quotient retain explicit doubts')
r['notes'][5]='N6. The two visible cancellations are the separate struck words, retained as doubtful de and par in one deleted span. Dans and une are both raised above these two crossed clusters; the blind audit extends the insertion through une. In the later paragraph only sorte de is above the line: its curved connector rises from the gap after une to the right of the raised phrase. Variance is on the same main baseline as une and des, so it is outside that inserted wrapper.'
r['notes'][6]=r['notes'][6].replace('four retained doubts','five retained doubts after the audit')
r['notes'].append('Blind audit: all thirteen differing boxes were inspected by the main reader. The canceled de was qualified and the raised insertion extended to dans une. The source check of95 confirms hatted I only in the M factor, with bare I in the upper Teichmüller factor and bare nu in the lower one. This local notation differs from the hatted-nu M factors on072 and is preserved. Repeated terms and the headless shaft in96, the isolated bare Gamma-G indices, unmatched parenthesis and pencil foliation remain as written. No proof or computation was added.')
r['root_review_notes']=r.get('root_review_notes','')+' All thirteen differing blind boxes inspected. B07 has one certainty qualification and an insertion-extent correction. The local I/nu accent differences in95 were specifically checked from B02 for the cross-page notation review.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['77']={'crops':[f'{page}_second_{k}.png' for k in ev],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
