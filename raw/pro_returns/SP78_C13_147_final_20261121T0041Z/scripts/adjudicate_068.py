from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan068'
ev={
'B03':'The raised infinity has two lobes and the lower index is 0,I. The following de is ordinary neighboring baseline text already present in the page, not part of this insertion. Keep the first attachment without duplicating de.',
'B05':'The first noun has the short c-ou-r group and tall b before e, not the longer croiseur sequence. Standart ends in a high angular crossed t without a d loop. The inserted last e/ee remains compressed and doubtful; doubled Z is clear. Retain the written spelling and qualified ending.',
'B07':'The repeated name has accented e, c, a and accented e before dre; no separately dotted i is visible in the proposed dodi- alternative. Retain dodecaedre with its source accents and gauche.',
'B08':'The opening M has a separate hat and the shaft has a small two-arm right head. After lisse the word has t-like ends and a compressed middle; the first et tout/et tant doubt stays. Il en is distinguishable, while the next short va-like group is still unresolved, not a secure est or Id. In the later formula the first M is bare and the second has a short bent raised stem and detached dot, not an independent hat over M. Retain the exclamation, nu, doubled N and joined quelque. Equivalent arrow/ellipsis encodings do not change this reading.',
'B09':'Irreduc-/tibles is a physical line division, not a lexical hyphen. The comp. abbreviation, comma before capital Il and the raised lieu de mettre with its guide remain as in the first reading.',
'B10':'The cancellation crosses the small index and other parts of M0I, so the whole-formula uncertainty remains. The separate inserted numeral10 and surrounding composantes text are clear.',
'B11':'The three low returns after the u support une, including the short terminal e. The infinity and serifed I agree; superscript/subscript ordering is equivalent TeX.',
'B12':'The first word again has the compact courbe form, including its b ascender, rather than croiseur. The crossed word exposes initial st and later upright strokes but does not securely show the two d loops of standard; keep stable qualified as a whole. The following a with accent and maximal are live.',
'B14':'After the p there is a short dotted i, low e and a looped d before s, without the o and separate n/t of points. Retain pieds, numeral3 and the closing parenthesis with period.',
'B15':'The large group letter has the same looped upper return and inward middle stroke as the established symmetric-group letter in scan057 B04, personally compared here; keep mathfrak S rather than a newly introduced G. The I has two serifs and the raised plus crosses. The Aut insertion, dodecaedre accents, gauche, infinity and connector agree.',
'B16':'The looped group letter repeats the preceding symmetric-group form, including its inward middle stroke; retain mathfrak S_I. The canceled tout has crossed internal letters and remains qualified. The final dash has no textual change.',
'B17':'A focused second-pass crop shows that the t foot is on the baseline of the following du; it is tall, not a small raised ending. The p descender makes the adjoining t appear higher. Retain baseline pt and the full il faudrait le comprendre wording.',
'B18':'The inserted gauche groups each have a long g descender and h shoulder with their guides. The repeated name has the same accented e/c/a sequence. The small ca group has the lower cedilla stroke and short a-return; retain ca with cedilla rather than adding a ce alternative. Ellipsis, ordinary parenthesis and dash agree.',
'B19':'The final delimiter has a curved upper and outer stroke but an angular leftward foot. It does not securely distinguish a closing parenthesis from a square bracket. Preserve the preferred parenthesis with bracket alternative; the underline covers bi-icosaedre only and there is no added full stop.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
final=first['B19'][:-1]+r'\unsure{)|]}'
d['B19'].update(changed=True,final=final)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text();assert first['B19'] in t;t=t.replace(first['B19'],final);p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
r['changes'][32]['final']=r['changes'][32]['final'][:-1]+r'\unsure{)|]}'
r['changes'][32]['evidence']='The underline ends with bi-icosaedre; gauche has the same g-au-ch-e form as the other occurrences. Combinatoire has no preceding opening delimiter. The final closing stroke is curved above with an angular leftward foot, leaving ) versus ] uncertain. No separate full stop is present.'
r['changes'][32]['confidence']='medium'
r['doubts'].append({'place':'Final closing delimiter after combinatoire, blind box B19','reading':r'\unsure{)|]}','alternatives':') ; ]','confidence':'low','reason':ev['B19']})
r['notes'][4]=r['notes'][4].replace('unmatched final closing parenthesis after combinatoire','unmatched final closing delimiter after combinatoire, now qualified as ) or ]')
r['notes'][5]=r['notes'][5].replace('No OCR, web research, TeX compilation, or second reading was performed.','No OCR, web research or TeX compilation was performed. This paragraph records the first-reading workflow; the subsequent blind audit is recorded below.')
r['notes'].append('Blind audit: all fourteen differing boxes were personally checked. The final delimiter acquired a parenthesis/bracket doubt. The apparent raised t in pt was checked on a focused crop and remains baseline: its foot aligns with du while p descends below. The looped symmetric-group letters were compared with scan057 B04 and retained. No mathematical argument was used to fill or normalize ink.')
r['root_review_notes']=r['root_review_notes'].replace('unmatched final parenthesis','unmatched final closing delimiter')+' All fourteen differing blind boxes personally checked; one certainty change in the final delimiter. The focused pt crop supports the baseline abbreviation.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['68']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_B17_pt.png','147_scan057_second_B04.png'],'extra_boxes':{'B17_pt':[1260,1730,1460,1850]},'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
