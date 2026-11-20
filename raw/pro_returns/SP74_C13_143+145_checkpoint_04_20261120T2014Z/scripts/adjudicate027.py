from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work'); p=R/'reviews/143_scan027_readerB.json'; d=json.loads(p.read_text()); t=R/'reviews/143_scan027_readerB.tex'; s=t.read_text()
assert len(d['changes'])==40
mapping={7:('separator',[755,630,945,690]),12:('family_words',[1095,1190,1645,1285]),13:('family_words',[1095,1190,1645,1285]),19:('negative',[330,1420,1560,1690]),27:('fibre_predicate',[325,1900,1650,2040]),28:('fibre_predicate',[325,1900,1650,2040]),29:('dim_rel',[330,2040,820,2135]),39:('number26',[20,2290,95,2355])}
for i,(n,b) in mapping.items():d['changes'][i].update(crop=f'crops/143_scan027_main_{n}.png',box=b)
d['changes'][8].update(crop='crops/143_scan027_readerB_heading_revisions.png',box=[430,844,1528,1101])
d['changes'][28]['ink']+=' Main-reader crop includes only the lower portion of this ascending line; the complete phrase was seen in the original and by the first reader in the native lower half. No second crop was made.'
d['excluded_rendering_differences']=[dict(d['changes'][i],reason='Same manuscript graph; bold/blackboard/plain font choice alone is not a material reading difference.') for i in [11,18,36]]
d['changes']=[r for i,r in enumerate(d['changes']) if i not in [11,18,36]]
first=r'''\begin{tikzpicture}[baseline=(words.base)]
\node[anchor=base west,inner sep=0] (words) at (0,0) {pour les};
\node[anchor=base west,inner sep=0] at (0.05,.62) {\inserted{$(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}$}};
\draw[line width=.3pt] (-.14,-.06) .. controls (-.43,.30) and (-.20,.42) .. (1.65,.40);
\end{tikzpicture}'''
s=s.replace(r'\inserted{$(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}$} pour les',first)
old=r'''\[
B_{\operatorname{GP}(1)},\quad B_{\operatorname{Aff}(1)},\quad B_{G_m},\quad\inserted{B_e=e}
\]
dont les'''
last=r'''\figure{\begin{tikzpicture}[baseline=(list.base)]
\node[anchor=base west,inner sep=0] (list) at (0,0) {$B_{\operatorname{GP}(1)},\quad B_{\operatorname{Aff}(1)},\quad B_{G_m}$};
\node[anchor=base west,inner sep=0] at (6.0,0) {dont les};
\node[anchor=base west,inner sep=0] at (6.0,.62) {$\inserted{B_e=e}$};
\draw[line width=.3pt] (5.85,-.08) .. controls (5.58,.28) and (6.0,.44) .. (7.5,.43) .. controls (7.74,.47) and (7.73,.58) .. (7.55,.54);
\end{tikzpicture}}'''
assert old in s;s=s.replace(old,last);t.write_text(s)
for place,final,crop,box,ink,after in [
('Heading A, curved insertion guide',r'\draw[line width=.3pt] (-.14,-.06)', 'heading_revisions',[430,844,1528,1101],'A thin curved call descends beside pour les and sweeps underneath the raised moduli formula. It is separate from the formula parentheses and is reproduced without adding an arrowhead.','Heading A, inserted moduli-topos formula and attachment'),
('Final classifying list, curved insertion guide',r'\draw[line width=.3pt] (5.85,-.08)','last_classifying_insertion',[943,2140,1513,2319],'A fine curved call bends up from before dont les, runs beneath the raised B_e=e and ends in a small loop. The curve is reproduced with the text in its relative position, without treating it as another mathematical sign.','Inserted fourth classifying topos')]:
 row=dict(place=place,C='[insertion text but no drawn guide]',H='[no drawn guide]',final=final,against_C=True,against_H=True,kind='drawing or diagram',ink=ink,confidence='high',crop=f'crops/143_scan027_readerB_{crop}.png',box=box,marked_in_H=False,consequential=False)
 ix=next(i for i,r in enumerate(d['changes']) if r['place']==after);d['changes'].insert(ix+1,row)
for after,pos,words in [('E10','beneath the raised heading formula, curling toward pour les','thin curved insertion guide'),('E21','beneath B_e=e, curling before dont les','fine insertion guide with terminal loop')]:
 ix=next(i for i,r in enumerate(d['inventory']) if r['element']==after)
 d['inventory'].insert(ix+1,dict(sheet_kind='text',hand='his hand',element=after+'a',kind='drawing',position=pos,first_words_or_objects=words,transcribed='yes'))
for i,r in enumerate(d['inventory'],1):r['element']=f'E{i:02}'
d['notes'].append(dict(id='143_scan027-N7',text='Targeted check of the geometric stabilizer dimensions only: over a geometric field an automorphism of the projective line is z -> (az+b)/(cz+d), with ad-bc nonzero and scalar matrices identified, giving dimension 3. Fixing infinity forces c=0 and yields z -> az+b, a nonzero, dimension 2; also fixing 0 forces b=0, giving G_m of dimension 1; also fixing 1 forces a=1, giving the identity. Any ordered distinct triple can be taken to infinity, 0, 1. Thus the dimensions 3-nu for nu=0,1,2 and a trivial stabilizer for three markings fit the surrounding list. This explains the expected variable nu but does not settle the 2-like/nu count glyph, nor license replacing the written GP(1). It is not a proof of the general-base Isom scheme assertions or the non-etendue statement.'))
d['check_events'].append(dict(statement_id='143_scan027-N7',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='targeted proof check',outcome='Explicit fractional-linear parameter calculation gives dimensions 3,2,1 and identity stabilizer for 0,1,2,3 fixed distinct points over a geometric field. The calculation is conditional on the projective-line interpretation and does not resolve the ink or prove the general topos claim.'))
d['main_adjudication']={'existing_crops_seen':12,'main_crops_seen':6,'decisions':'Preserve all stated local doubts, literal GP(1), rank 1, and 2/nu uncertainty; add both insertion guides; exclude three font-only rows.','limitation':'The fibre_predicate crop partially clips the upward-sloping est lisse; that phrase was visible in the original and reader native half. The different-reader audit will check its complete native-half context.'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'reviews/143_scan027_main.md').write_text('''# Main-reader adjudication — 143_scan027

The original, twelve reader crops and six main-reader crops were inspected. All open and differing loci were adjudicated. The final preserves the literal two-letter GP(1), rank 1, the four-point suspensions, the underlined n’est, singular modulaire after canceled des, and the unsmoothed plural/singular syntax. The canceled adjective, par, article, canceled comparisons, canceled nu and canceled Néanmoins remain local doubts. The marked-section count remains 2/nu: the ink has a rounded upper hook, descending diagonal and heavy foot, but possible retouching prevents a unique decision. Both insertion calls are reproduced as thin curves, with the text above their baseline attachment. Three Q/G font-only comparisons are retained in the review record but excluded from material change counts.

The fibre-predicate crop partially clips est lisse because the line rises to the right; the complete phrase was visible in the original and reader’s lower half. No second crop was made. The later different-reader audit must explicitly check that complete phrase. A direct projective-line stabilizer calculation is recorded as N7 and honestly distinguished from proof of a general Isom-scheme or topos claim.
''')
with (R/'notation.md').open('a') as f:f.write('''\n## Additional shared readings through scan 027\n\n| Manuscript form | Encoding / reading | Scope and evidence |\n| --- | --- | --- |\n| Small ring above an indexed product symbol | literal circle exponent | Scan026; its NB explains reversal of the action. Do not normalize it to a numerical zero. |\n| Two vertically aligned wavy strokes | rotated approximate-sign shape | Scan026; retain the physical orientation beside the diagram arrow. |\n| Geometric classifying group name | literal GP(1) | Scan027 has a clear G followed by P and argument 1. PGL(2) is not the written reading. |\n| Modular-topos letter | retain C’s calligraphic T | Scan027 onward, with genus and marking indices, distinct in mathematical role from the preceding object-set letter; font alone is not a separate correction. |\n\nThe flag-topped object-set and rounded action-group uncertainties continue through scans025–027. The low cross-like stroke below scan025’s final set equality is attached to the equality as a whole, not supplied as a tau subscript.\n''')
