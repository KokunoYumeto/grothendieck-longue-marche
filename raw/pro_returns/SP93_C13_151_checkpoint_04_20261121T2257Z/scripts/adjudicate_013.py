from pathlib import Path
import csv,json
R=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work')
p=R/'reports/151_scan013.json';d=json.loads(p.read_text());tp=R/'reports/151_scan013.tex';t=tp.read_text()
f={r['box']:r['first'] for r in csv.DictReader((R/'second/151_scan013_comparison.tsv').open(),delimiter='\t')}
b={r['box']:[int(r[k]) for k in ('x0','y0','x1','y1')] for r in csv.DictReader((R/'second/151_scan013_boxes.tsv').open(),delimiter='\t')}
assert 'carrés commutatifs de $A$' in t;t=t.replace('carrés commutatifs de $A$','carrés commutatifs dans $A$')
old=r'\inserted{$\widehat A\longrightarrow\mathcal X$} commutant'
new=r'''\begin{tikzpicture}[baseline=(w.base)]
\node[anchor=west,inner sep=0pt] (w) at (0,0) {commutant};
\node[anchor=west,inner sep=0pt] at (-.12,.54) {\inserted{$\widehat A\longrightarrow\mathcal X$}};
\draw (-.14,-.12)..controls(-.18,.24)and(.2,.31)..(.52,.3)..controls(1.12,.28)and(1.6,.39)..(1.84,.44)..controls(1.96,.48)and(1.98,.54)..(1.94,.62);
\end{tikzpicture}'''
assert old in t;t=t.replace(old,new)
d['changes'].append(dict(id='C013-A01',place='After carrés commutatifs',C='de',H='de',final='dans',evidence='The word has a tall initial d, joined low a/n strokes and a separate terminal s bend. It is longer than de, whose expected final e does not account for the separated s. The initial regardant ends in an angled t return, not the rounded s of regardons.',confidence='high',kind='misread word',crop='crops/151_scan013_second_B005.png',box=b['B005'],differs_C=True,differs_H=True,marked_in_H='no',consequential=''))
c=next(c for c in d['changes'] if c['id']=='C013-15');c.update(final=new,evidence=c['evidence']+' The final encoding now also draws that continuous attachment: it rises before commutant, runs beneath the inserted formula, and curls upward on its right.',crop='crops/151_scan013_second_B012.png',box=b['B012'],differs_C=True)
d['notes'].append('Independent image-only audit: B005 changes de A to dans A because the d, low middle strokes and terminal s are visible. B012 adds the visible insertion leader, separately from the formula it attaches. The ambiguous central slice-arrow mark and the canceled à/et remain unresolved; no new mathematical repair is introduced.')
e={
'B001':'The dark numeral has the two rounded right lobes of 3. The mspage wrapper already occurs in the consolidated page; there is no textual difference.',
'B002':'The wording and all indices agree. Splitting the inline math across a physical line in the second encoding does not change alpha_n or the preceding ellipsis.',
'B003':'The underline is concentrated beneath Hyp. and ends by the beginning of 2, without extending beneath the whole 2-prime. The arrow shaft overlaps the small loop/upright that may be phi; no separate cancellation stroke is established. The existing phi-labelled/twoheaded/plain-arrow alternatives therefore remain. The small two-part mark before Hyp 2 still admits à/colon rather than a secure colon.',
'B004':'The cospan has alpha_1 and alpha_2 above alpha_0 and both shafts directed toward alpha_0, followed by the comma. The readings differ in TikZ matrix syntax and spacing only.',
'B005':'A tall d and joined a/n are followed by a separate s bend: dans, not the first reading de. Regardant has a final stepped t, so the second reader’s regardons alternative is not adopted. Carrés, commutatifs and le complètent en remain.',
'B006':'The four objects gamma, alpha_1, alpha_2, alpha_0 and all four downward diagonal maps agree; the separate comma remains. Matrix separators and spacing do not change the diagram.',
'B008':'The small retraced index has the same looped gamma form as the upper object in B006. Its two open upper courses and lower loop remain identifiable; no new uncertainty is required. The target factors and base U_alpha0 agree.',
'B009':'The hypothesis numbers are 1, 2, 2-prime with two commas. Moving them into math mode changes no reading.',
'B010':'Joliment has a descending initial j, a rounded join into the tall looped l, a distinct i dot, and the low ment ending with terminal t. Its letters are sufficiently visible to retain the plain reading.',
'B011':'Phi has a lower exclamation index, followed by the colon, A-hat, right arrow and calligraphic X. Extra grouping braces in the second reading are syntax only.',
'B012':'Both readers locate the same raised formula after foncteur. The crop also shows its continuous curved leader entering that gap before commutant and curling upward at the right; this is now drawn. The short struck word has a low return and upright under the strike, leaving à/et unresolved, not secure à.',
'B013':'Ce sont and respectivement remain legible: the long final word has the initial r/e/s, descending p, compact ecti and low vement ending. It is not physically unreadable. The right-pointing arrow beneath lim agrees with varinjlim; foliation 12 is separate and unchanged.'}
m={k:dict(changed=k in ('B005','B012'),evidence=v) for k,v in e.items()}
m['B005']['final']=f['B005'].replace('commutatifs de $A$','commutatifs dans $A$')
m['B012']['final']=f['B012'].replace(old,new)
(R/'reviews/151_scan013_manual.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');tp.write_text(t)
