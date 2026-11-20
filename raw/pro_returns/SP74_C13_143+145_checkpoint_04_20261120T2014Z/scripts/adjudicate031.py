from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
p=R/'reviews/143_scan031_readerC.json';d=json.loads(p.read_text());t=p.with_suffix('.tex');s=t.read_text()
assert len(d['changes'])==41 and 'main_adjudication' not in d
mapping={0:('opening',[110,20,1650,365]),2:('tag5',[155,380,275,500]),13:('ou_encore',[120,1120,650,1310]),25:('nb_geometric',[270,1820,855,1980]),30:('sans',[1460,1870,1635,1960]),31:('nb_live_words',[210,1940,1660,2140]),32:('nb_live_words',[210,1940,1660,2140]),40:('footer',[40,2180,470,2362])}
for i,(n,b) in mapping.items():d['changes'][i].update(crop=f'crops/143_scan031_main_{n}.png',box=b)
d['changes'][30]['ink']+=' Main sans crop checks the first word; main nb_live_words crop checks doute on the following line.'
d['changes'][40]['ink']+=' The main footer crop shows the zero and part of the 3; the original and the native lower half show the complete 30.'
d['changes'][2]['ink']+=' The main tag crop shows its right parenthesis before the initial 1; the complete 5 was checked in the original.'
guideG=r'''\begin{tikzpicture}[baseline=(base.base)]
\node[anchor=base west,inner sep=0] (base) at (0,0) {du};
\node[anchor=base west,inner sep=0] at (-.04,.48) {\inserted{$G_{g,\nu}$}};
\draw[line width=.3pt] (-.18,-.13) .. controls (-.24,.20) and (.01,.30) .. (.40,.29) .. controls (.70,.30) and (.97,.38) .. (1.09,.46);
\end{tikzpicture}'''
old=r'\inserted{$G_{g,\nu}$} du';assert old in s;s=s.replace(old,guideG)
guideIm=r'''\begin{tikzpicture}[baseline=(base.base)]
\node[anchor=base west,inner sep=0] (base) at (0,0) {$\mathfrak S_\nu$};
\node[anchor=base west,inner sep=0] at (-.17,.48) {$\inserted{\operatorname{Im}}$};
\draw[line width=.3pt] (-.11,-.18) .. controls (-.24,.06) and (-.04,.35) .. (.15,.45) .. controls (.31,.54) and (.35,.66) .. (.32,.74);
\end{tikzpicture}'''
old=r'\inserted{\operatorname{Im}}\mathfrak S_\nu';assert old in s;s=s.replace(old,guideIm)
for idx,g in [(22,guideG),(28,guideIm)]:
 d['changes'][idx].update(final=g,against_C=True,kind='insertion or placement')
 d['changes'][idx]['ink']+=' The main reader also reproduces the physical curved attachment in TikZ; C marked the insertion but omitted this guide.'
for target,pos in [('E12','before du, under the raised G label'),('E14','between the equality sign and S_nu, beneath raised Im')]:
 i=next(i for i,x in enumerate(d['inventory']) if x['element']==target)
 d['inventory'].insert(i+1,dict(sheet_kind='text',hand='his hand',element=target+'a',kind='drawing',position=pos,first_words_or_objects='curved insertion guide without an arrowhead',transcribed='yes'))
for i,x in enumerate(d['inventory'],1):x['element']=f'E{i:02}'
d['notes'].append(dict(id='143_scan031-N8',text='The two NB insertions G and Im each have a curved attachment guide, now reproduced rather than treated as extra parentheses. A suspected bracket beneath the diagram alias was checked on the original-coordinate crop: the strokes belong to the following prose « un peu plus riche », not to an extra mathematical decoration. No bracket is added there.'))
d['check_events'].append(dict(statement_id='143_scan031-N8',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='carried as background without fault found',outcome='Visual attachment and text-layout check only; no mathematical theorem checked.'))
d['main_adjudication']=dict(original_seen=True,existing_crops_seen=17,main_crops_seen=8,native_lower_half_seen_once=True,decision='All differing and open loci checked; accepted the two-column diagram, literal punctuation and local doubts. Added both visible NB insertion curves. Apparent alias underbracket is following prose, so no extra drawing supplied.')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2));t.write_text(s)
(R/'reviews/143_scan031_main.md').write_text('''# Main-reader adjudication — 143_scan031

The original, all seventeen reader crops, eight saved main crops and the existing native lower half were inspected. The lower half was used once for the complete pencil 30, Sans at the end of the preceding line, and the NB block layout; the small footer crop clips the left of the 3. The tag crop clips the left part of (5), but establishes its position immediately before the first 1; the full tag was seen in the original. No second enlarged crop of a decided locus was made.

The first link has a small triangular endpoint. The central four expressions are arranged in two offset columns with separate vertical equality pairs and horizontal equalities. The full-sized xi in the left column has low comma separators; the reduced right-column form remains xi/j. The suspected extra bracket below the lower-right alias is actually the following prose un peu plus riche. The opening on a/suspension, faite/fait, à/colon, joined gnu/comma, four small basepoints, canceled est, crossed closing sign and clipped marginal words remain local doubts.

The three puncture-list continuations are single strokes. The second display has an upper-right completion wedge; the third tilde-T index has no comma and only one closing parenthesis survives before the final period. The final question uses a centered hat, a square underbracket beneath the whole parenthesized argument, and only the left brace for its two alternatives. No closing punctuation is invented in the margin. The two NB insertion guides are reproduced with their visible attachment to du and to the S term. The lighter ink alone is not assigned to another hand. No conjectural mathematical assertion on this page was independently proved.
''')
