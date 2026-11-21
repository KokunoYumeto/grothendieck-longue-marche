from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan064';c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B02':'The opening d-apostrophe has one compressed ou group and an accent, not a separately dotted ici sequence. The next word has low m, a rounded o, an i-mark and ns-like tail: moins, not même. The following short au and d-led dessus are visible, without the h/r sequence of dehors. Retain d’où, au moins au dessus de and double-stroked Z[1/2].',
'B03':'Both live capitals have a transverse top extending to both sides of the stem, and match the local Tate T(1) notation; retain T rather than introducing J. The live fractions,79, grouping brace, hat/infinity decoration and downward equality1/2 agree. Both crossed trials remain whole-expression doubts: the denominator and several internal strokes are buried, so the alternative12/2 and2/alpha suggestions cannot certify a replacement.',
'B05':'Bare M1,1, a rightward arrow, doubled E and raised numeral1 agree; only display wrappers differ.',
'B06':'The short live word after cancelled et begins with a small e-like loop, not a closed o. The d-led verb has the p descender and continued ant strokes after it; retain en découpant. The E1, S0, two sections and parenthetical curve wording agree.',
'B07':'Harmonique and the quotient Z/4Z agree. The short automorphism abbreviation has d-apostrophe, au/t and compressed joined low strokes; the tail does not securely separate the m of automs from autos. Retain automs first but mark the shorter alternative.',
'B08':'The overwritten S has a small crossed old subscript body beside a distinct live1, so retain the tentative deleted0. The cancelled relation/Z-like group remains too crossed to establish a slash3. The parenthetical courbe ell., bonne and avec un bon remain crowded; the first doubts are retained, including the short bon-like group before gr. that the blind reading omits.',
'B09':'The same compressed automs/autos ending remains ambiguous here; mark it consistently without expanding it. Z/6Z, the two point numbers2 and3, and the surrounding words agree.',
'B10':'The source has sauf erreur, à des groupes and the same short automs/autos ambiguity. Keep the author’s qualification and mark the compressed abbreviation ending.',
'B11':'The crossed E-like glyph before U has two close parallel uprights under the diagonal cancellation, matching the live doubled E at the start. Preserve the crossed-letter uncertainty but represent those paired stems as mathbb E. The two based amalgamation signs, later plain cups, primes, point indices and24/12 agree.',
'B12':'The brace’s upper tip begins below the U equation and groups only the intersection and primed-section definitions. Move the U equation above the braced group. The sign after E1 remains a crossed plus/set-minus doubt; its preferred order is unchanged. The focused first removed-point index has an angular upper turn and compressed lower return, leaving2/3 uncertain; do not derive2 from the set identity. The second index and both indices in the S1-prime definition remain as first read. After où, two rounded bodies, a low comma and subscript-like trace support the qualified a1,a0 rather than words on a. Car2 has no point, car.3 has one.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
oldabbr="d'automs";newabbr=r"d'\unsure{automs|autos}"
for b in ('B07','B09','B10'):d[b].update(changed=True,final=c[b]['first'].replace(oldabbr,newabbr))
oldE=r'\deleted{\unsure{E}}';newE=r'\deleted{\unsure{\mathbb E}}'
d['B11'].update(changed=True,final=c['B11']['first'].replace(oldE,newE))
oldgroup=c['B12']['first']
newgroup=oldgroup.replace(r'\left\{\begin{aligned}'+'\nU&=',r'\begin{gathered}'+'\nU=')
newgroup=newgroup.replace(r'(S_0\cup S_1)\\',r'(S_0\cup S_1)\\'+'\n'+r'\left\{\begin{aligned}')
newgroup=newgroup.replace(r"S'_0&=S_0\smallsetminus\{a_2,a_3\}",r"S'_0&=S_0\smallsetminus\{a_{\unsure{2|3}},a_3\}")
newgroup=newgroup.replace(r'\end{aligned}\right.',r'\end{aligned}\right.'+'\n'+r'\end{gathered}')
d['B12'].update(changed=True,final=newgroup,crop=f'{page}_second_root_B12_index.png')
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text();assert t.count(oldabbr)==3;t=t.replace(oldabbr,newabbr);assert oldE in t;t=t.replace(oldE,newE,1);assert oldgroup in t;t=t.replace(oldgroup,newgroup,1);p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
for rid,b in [('064-10','B07'),('064-18','B09'),('064-21','B10')]:
 row=next(x for x in r['changes'] if x['id']==rid);row.update(final=newabbr,evidence=ev[b],confidence='low',crop=f'{page}_second_{b}.png');row['box']={'B07':[240,1003,1603,1121],'B09':[240,1230,1640,1445],'B10':[253,1467,1499,1573]}[b]
row=next(x for x in r['changes'] if x['id']=='064-23');row.update(final=newE,evidence=ev['B11'],against_C=True,crop=f'{page}_second_B11.png',box=[263,1577,1652,1798])
r['changes'].append({'id':'064-29','place':'Final definitions, vertical extent of the left brace','C':'U equation and two following rows within the brace','H':'U equation and two following rows within the brace','final':'U equation above the brace; brace groups the intersection and primed-section definitions','evidence':ev['B12'],'crop':f'{page}_second_B12.png','box':[276,1852,1436,2211],'confidence':'high','against_C':True,'against_H':True,'kind':'insertion or placement','marked_in_H':False,'error_sheet_kind':'insertions put in wrong place','consequential':False})
for x in r['doubts']:
 if x.get('reading')==oldE:x.update(reading=newE,reason=ev['B11'])
r['doubts'] += [{'place':'Three automorphism abbreviations','reading':newabbr,'alternatives':'automs; autos','confidence':'low','reason':'All three tails consist of compressed low joined strokes; the medial m is not securely separable after the blind comparison.'},{'place':'S0-prime definition, first removed-point index','reading':r'a_{\unsure{2|3}}','alternatives':'2;3','confidence':'low','reason':ev['B12']}]
r['unresolved'] += ['All three automs/autos abbreviation endings.','First removed-point subscript in S0-prime definition:2/3.']
r['notes'].append('Blind audit: all ten differing boxes and a focused pair-of-indices crop were personally viewed. The U equation stands above the lower brace; this placement is restored. The cancelled E candidate now preserves its paired upright strokes. Three abbreviated automorphism words and one point index receive uncertainty marks; no set identity or expected group order is used to supply ink.')
r['root_review_notes']=r.get('root_review_notes','')+' Ten differing blind boxes and focused B12 index crop viewed; five boxes changed (including certainty changes).'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['64']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_B12_index.png'],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
