from pathlib import Path
import json
R=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work');p=R/'reviews/143_scan028_readerC.json';d=json.loads(p.read_text());t=R/'reviews/143_scan028_readerC.tex';s=t.read_text();assert len(d['changes'])==20
mapping={0:('opening_add',[1200,35,1670,120]),1:('first_display',[525,155,940,275]),2:('first_display',[525,155,940,275]),9:('schema',[260,405,585,510]),11:('completion_guide',[1000,585,1650,730]),13:('quotation',[440,865,1110,1000]),14:('quotation',[440,865,1110,1000]),17:('black_marks',[865,1370,1240,1560]),19:('number27',[20,2280,100,2360])}
for i,(n,b) in mapping.items():d['changes'][i].update(crop=f'crops/143_scan028_main_{n}.png',box=b)
old=r"\inserted{le complété profini d'}un groupe"
new=r'''\begin{tikzpicture}[baseline=(base.base)]
\node[anchor=base west,inner sep=0] (base) at (0,0) {un groupe};
\node[anchor=base west,inner sep=0] at (-1.4,.62) {\inserted{le complété profini d'}};
\draw[line width=.3pt] (-.18,-.10) .. controls (-.18,.28) and (-.14,.38) .. (.08,.38) -- (2.7,.43) .. controls (2.95,.45) and (3.1,.52) .. (3.05,.61);
\end{tikzpicture}'''
assert old in s;s=s.replace(old,new);t.write_text(s)
d['changes'][11]['final']=r"\inserted{le complété profini d'}"
d['changes'].insert(12,dict(place='Profinite-completion addition, curved guide',C='[inserted text; guide not reproduced]',H='[no guide]',final=r'\draw[line width=.3pt] (-.18,-.10)',against_C=True,against_H=True,kind='drawing or diagram',ink='A thin line descends immediately before the baseline un, bends right beneath the added completion phrase, then turns up at the far right. It is drawn separately from the apostrophe and the added letters; there is no arrowhead.',confidence='high',crop='crops/143_scan028_main_completion_guide.png',box=[1000,585,1650,730],marked_in_H=False,consequential=False))
ix=next(i for i,r in enumerate(d['inventory']) if r['element']=='E13');d['inventory'].insert(ix+1,dict(sheet_kind='text',hand='his hand',element='E13a',kind='drawing',position='beneath the profinite-completion addition and before baseline un',first_words_or_objects='thin curved attachment guide with upward right end',transcribed='yes'))
for i,r in enumerate(d['inventory'],1):r['element']=f'E{i:02}'
d['notes'].append(dict(id='143_scan028-N7',text='Local coordinate check: for an ordered configuration of nu distinct points of a projective line with nu >= 3, the unique fractional-linear change sending three chosen labeled points to infinity, 0 and 1 leaves nu-3 mutually distinct coordinates in the complement of those three points. For nu=3 no coordinates remain; for nu=4 one coordinate remains in that complement. This verifies the local count and the punctured-line expression in the corrected description, conditional on labeled markings. It neither proves the topos equivalence or the fundamental-group assertions nor changes the manuscript letter E to another convention.'))
d['check_events'].append(dict(statement_id='143_scan028-N7',who='GPT-6 Astra Pro; inherited effort not exposed; SP74 second pass; main reader',type='targeted proof check',outcome='Normalized three distinct labeled points by their unique fractional-linear transformation; the remaining nu-3 coordinates avoid 0,1,infinity and one another. Only this coordinate count and complement were checked.'))
d['main_adjudication']={'original_seen':True,'existing_crops_seen':8,'main_crops_seen':7,'decision':'Accepted the proposed readings and one unresolved index comma; reproduced the visible completion insertion guide. The H heading is absent from the whole original page.'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'reviews/143_scan028_main.md').write_text('''# Main-reader adjudication — 143_scan028

The original was inspected once, all eight reader crops and seven main-reader crops were inspected. The main reader confirms en apparence, the unseparated first 0-nu index, no comma after the first display’s zero, no terminal point after its 3, Topos, and the canceled est le gros topos fibré with its live replacement above. Gros is an insertion inside the canceled phrase. Schéma stands above the canceled étale de. The punctured-line display has a short first minus and a diagonal second set-minus; the right-hand letter is visibly E with a doubled left stroke, not A.

En tant is accepted at medium confidence; the pair of quotation ticks and extérieur are clear. Du is a continuous addition with the barred-Q expression before on fait opérer; the tiny index comma in that addition remains uncertain. The baseline and final topos indices have their own visible commas. Five opaque black marks are reproduced, without assigning an intention or named hand. Pencil 14 and 27 remain unnamed. The H conjecture heading, its underline and reported circled 9 are absent from the original page. The curved guide beneath le complété profini d’ is added in TikZ. N7 records the limited coordinate check and does not claim to prove the fundamental-group or topos assertions.
''')
