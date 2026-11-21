from pathlib import Path
import json,csv
w=Path(__file__).resolve().parents[1];page='147_scan076'
ev={
'B01':'The number37 and title underlines are present. The final title word begins with low m bodies and continues through d/u/l/e/s, supporting modules, not variables. The raised espaces modulaires de and its guide are readable. No separate pair of umlaut dots is visible over Teichmuller; retain the local unaccented spelling.',
'B02':'The final noun has initial g with a descending loop, the short accented e/n/e sequence and the r/i/s/a/t/i/o/n continuation. There is no additional m/e/t/r cluster for géométrisation. Retain générisation.',
'B03':'There are two short quotation strokes both before and after an, and both before and after analytique. Retain both closing double quotes. The formulas, comma, M roof, superscript an, dash, and traîner accent agree; the different TeX dash length and script order do not change the reading.',
'B04':'The live first catégorie is not canceled by the guide for grosse. The later catégorie is struck and groupoïde is raised above it. The canoniq candidate has a long q descender and tiny raised ending, retained as an uncertain abbreviated t, not expanded. The pronoun before remplacer has a tall l loop and a compressed flat final return that does not securely distinguish a/e; qualify la/le. The Pi and underlined G agree.',
'B06':'The middle G has an additional upright with a small oblique branch through its upper part, independently visible above the G body. Preserve the uncertain drawn trace rather than omit it or invent a buried letter. The G underline, crossed l’équivalence and raised dans celui-ci agree.',
'B07':'Le groupe remains live above the long rising lower stroke. The lower stroke carries small loops/hooks, so it cannot securely be reduced to an ordinary underline or to a known canceled word; retain the uncertain drawn pattern. Display94 has Gamma with underlined G, equals, Aut and a second underlined G.',
'B08':'The action clause lies below94. The scan edge cuts the final word after its l’/a/c/t/i-like strokes and low continuation; action remains a plausible candidate but its ending is not fully visible. Qualify that word. Opère, et que, the equivalence clause and the separate de ce groupe with final period remain readable.'}
first={r['box']:r['reading'] for r in csv.DictReader((w/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
repls={'B04':('comment la remplacer',r'comment \unsure{la|le} remplacer'),'B08':("l'action",r"l'\unsure{action}")}
p=w/'pages'/f'{page}.tex';t=p.read_text()
for k,(a,b) in repls.items():
 assert a in first[k];d[k].update(changed=True,final=first[k].replace(a,b));assert first[k] in t;t=t.replace(first[k],d[k]['final'])
p.write_text(t)
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
for x in r['changes']:
 x['final']=x['final'].replace("l'action",r"l'\unsure{action}")
r['changes'][26]['evidence']+=' The last word action is now qualified because its ending runs into the scan edge; the physical placement below94 is secure.'
r['inventory'][8]['first_words_or_objects']=r['inventory'][8]['first_words_or_objects'].replace('comment la remplacer',r'comment \unsure{la|le} remplacer')
r['inventory'][21]['first_words_or_objects']=r['inventory'][21]['first_words_or_objects'].replace("l'action",r"l'\unsure{action}")
r['doubts'].extend([
 {'place':'Pronoun before remplacer, blind B04','reading':r'\unsure{la|le}','alternatives':'la; le','confidence':'low','reason':ev['B04']},
 {'place':'Final word at right scan edge below94, blind B08','reading':r'\unsure{action}','alternatives':'action preferred; ending clipped','confidence':'medium','reason':ev['B08']}
])
r['unresolved'].extend(['The compressed final vowel of la/le before remplacer remains uncertain.','Action remains a qualified candidate because its ending is cut by the right scan edge.'])
r['notes'].append('Blind audit: all seven differing boxes were viewed by the main reader. The compressed pronoun before remplacer and the clipped ending of action acquired certainty qualifications. The title modules, unaccented Teichmuller, générisation, both pairs of closing quotation marks, abbreviated raised canoniqt, extra trace at G and unresolved lower stroke beneath live le groupe were retained. No new mathematical check was claimed.')
r['root_review_notes']=r.get('root_review_notes','')+' All seven differing blind boxes inspected; two certainty-only qualifications. Focused crops inspected the compressed pronoun and clipped action ending.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['76']={'crops':[f'{page}_second_{k}.png' for k in ev]+[f'{page}_second_root_B04_pronoun.png',f'{page}_second_root_B08_edge.png'],'extra_boxes':{'B04_pronoun':[1420,1080,1530,1175],'B08_edge':[1500,1920,1689,2070]},'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
