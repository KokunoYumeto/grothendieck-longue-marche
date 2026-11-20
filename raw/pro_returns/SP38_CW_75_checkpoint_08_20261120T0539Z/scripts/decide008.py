from pathlib import Path
import json,copy
root=Path(__file__).resolve().parents[1]
rep={r:json.loads((root/'readings/scan008'/r/'report.json').read_text()) for r in ('R1','R2','R3')}
obs=json.loads((root/'decisions/scan008_main_observations.json').read_text())
fs=copy.deepcopy(rep['R1']['findings'])
r2=[1,3,2,9,4,5,9,6,7,44,8,16,16,16,10,11,12,13,13,14,14,14,15,44,44,17,18,20,19,21,22,23,24,25,26,27,28,29,31,30,32,33,34,35,35,36,37,37,38,38,38,39,40,41,42,43]
r3=['D01','N01','D02','N02','D03','D04','N04','D05','N05','N06','D06','N09','N09','N09','N08','D07','D08','D08','N10','N11','D09','N12','D10','N13','N14','D11','D12','N16','N15','N17','N18','N19','D13','N20','D14','D15','D16','N24','N23','N21','N25','D18','D19','D19','N27','D20','N28','N28','D21','D21','D21','N29','N30','D22','D23','D24']
def get(r,i):return next(f for f in rep[r]['findings'] if f['id']==i)
def rp(r,s):return f'readings/scan008/{r}/crops/{s}.png'
def mp(s):return f'crops/scan008/{s}.png'
paths=[rp('R3','01_opening_tte'),mp('01_quote'),rp('R3','02_under_sigma'),rp('R3','03_slanted_note'),rp('R3','03_slanted_note'),rp('R3','03_slanted_note'),rp('R3','03_slanted_note'),rp('R1','04_condition_label'),mp('02_condition_layout'),mp('02_condition_layout'),mp('03_omega'),mp('04_first_drawing'),mp('05_second_drawing'),mp('08_third_drawing'),mp('06_du_contour'),rp('R1','05_deleted_function'),rp('R1','05_deleted_function'),rp('R1','05_deleted_function'),mp('07_extremite'),rp('R2','06_origine_correction'),rp('R2','06_origine_correction'),rp('R1','22_origine_punctuation'),rp('R1','07_arc_word'),rp('R1','22_origine_punctuation'),mp('09_edge_bracket_layout'),rp('R1','08_automorphism_source_arrow'),rp('R1','08_automorphism_source_arrow'),mp('11_autom'),mp('10_left_brace'),mp('12_autom_punctuation'),rp('R2','10_fait_que'),mp('13_order_end'),rp('R2','11_fleche'),rp('R1','10_equivalence_abbreviation'),rp('R1','11_donc'),rp('R1','12_orientation_set'),rp('R1','13_avec'),rp('R1','13_avec'),mp('14_before_g'),rp('R1','14_conditions_close'),rp('R1','14_conditions_close'),rp('R1','15_group_abbreviation'),rp('R3','19_forme'),rp('R3','19_forme'),rp('R1','17_inserted_group'),rp('R1','17_inserted_group'),mp('16_orientes'),mp('16_orientes'),rp('R1','18_tuple_gloss'),rp('R1','18_tuple_gloss'),rp('R1','18_tuple_gloss'),rp('R2','20_bottom_deletion'),mp('15_added_bound'),rp('R2','21_ensemble'),rp('R2','22_element'),rp('R1','21_order_star')]
keys=['opening','quotes','origin_undertext','slanted_note','slanted_note','slanted_note','slanted_note','label','condition_layout','condition_layout','omega','drawings','drawings','drawings','du_contour','function','function','function','extremite','origine_correction','origine_correction','origine_punctuation','arc','origine_punctuation','edge_bracket','source_pair','source_pair','autom','left_brace','autom','fait','order_end','fleche','sss','donc','or','avec_ens','avec_ens','before_g','condition_close','condition_close','group_abbreviation','forme_le','forme_le','group_insert','group_insert','autom','orientes','gloss','gloss','gloss','bottom_deletion','bound','ensemble','element','order_mark']
for i,f in enumerate(fs):
 f['readers']={'R1':f['final'],'R2':get('R2',f'F{r2[i]:02d}')['final'],'R3':get('R3',r3[i])['final']}
 f['crop']=paths[i];f['evidence']=obs['observations'][keys[i]]
 f['decision']='Main inspected this crop and adopted the stated reading from the ink; the three independent readings are recorded here.'
def upd(n,**kwargs):fs[n-1].update(kwargs)
upd(1,final=r'\unsure{tte|toute}',confidence='medium',doubt_action='retain',decision='Choose R3: exclude les but retain tte and compressed toute; C doubt narrowed, not fully resolved.')
upd(3,final=r'\deleted{\unsure{\omega|o}}\sigma(a)',diff_c=True,confidence='low',decision='Choose R3 ordering omega|o, from two low loops under final sigma; cancellation prevents resolution.')
upd(6,final=r'\deleted{\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,}',diff_c=False,confidence='medium',doubt_action='retain',decision='R1 resolves s; R2/R3 retain s|a. Main retains C because the strike obscures the counter.')
upd(7,final='Left margin note with independent lower rule and a separated right stroke, itself slightly interrupted.',decision='R1 joins the strokes; R2 keeps only the lower rule; R3 separates them. Main keeps both without joining them. H only describes one separating trait and does not supply this geometry.',confidence='high',diff_h=True,kind='drawing or diagram')
upd(22,final=r'comme origine\unsure{.|}',diff_c=True,diff_h=False,confidence='low',decision='R1 reads a point; R2/R3 omit it. Main retains a point as primary with an empty alternative, since the final dark trace may be the compressed e. H primary is unchanged; confidence alone is not an H difference.')
upd(24,final='Two-line square bracket adjacent to the prose ending.',diff_c=True,decision='All readers preserve two rows but put a separate display below. Main restores its adjacent placement from the crop, retaining both rows.')
upd(25,final='Two-line bracket adjacent to prose: incidence and origin inequality above, i.e. and edge inequality below at right.',diff_c=True,decision='Main preserves the two rows and the bracket beside the prose ending, rather than a detached display.')
upd(27,diff_h=True,decision='Primary short dash has no secure arrowhead. H supplies an arrow; this is a substantive primary-reading difference, not only confidence.')
upd(33,final=r'\unsure{fleche|et}',diff_c=True,confidence='medium',decision='Choose R2 unaccented primary, with et retained. The crop shows no separate grave accent; do not modernize to flèche.')
upd(36,final=r'\operatorname{or}',diff_c=True,doubt_action='resolve',confidence='high',decision='Choose R2/R3 lowercase or: o is at the small r height and is distinctly below capitals in the following tuple.')
upd(40,final=r'$1^{\circ}$ \unsure{$-$|ou} $2^{\circ}\big\}$',confidence='medium',decision='Resolve the large closer as a right brace; retain the low connector with dash first, ou second. The additional short hook is recorded separately.')
upd(42,decision='R1 has grpe|gpe, R2/R3 gpe|grpe. Main retains grpe first because a short plateau after g permits r; no expansion.',confidence='medium')
upd(43,final=r'\deleted{formé}',diff_c=True,doubt_action='resolve',confidence='high',decision='Choose R2/R3 formé; the terminal acute remains visible beyond the cancellation.')
upd(44,final=r'\inserted{le}',diff_c=False,diff_h=True,confidence='high',kind='insertion or placement',decision='Choose R2/R3 clear added le, as C. H puts live le before the canceled word and does not record this insertion; the consolidated order is canceled formé followed by inserted le.')
upd(45,decision='Retain R1 grpe|gpe for the second compressed word; the curved leader inserts it and G before des autom. This is a whole-word ambiguity, not a second mark on the same recurring mathematical glyph.')
upd(48,evidence=obs['observations']['orientes']+' '+obs['observations']['gloss'],decision='Main inspected both 16_orientes and R1 18_tuple_gloss: orientés goes after autom, while the separate gloss follows the existing tuple.',crop=mp('16_orientes')+'; '+rp('R1','18_tuple_gloss'))
upd(49,final=r'\unsure{lire|les|i.e.} de S,A,R;\omega)',diff_c=True,confidence='low',decision='The compressed leading word remains unresolved. Keep lire and les, and R2’s i.e. alternative; none supplies an opening parenthesis.')
upd(50,final=r'S,A,R;\omega)',diff_c=False,diff_h=False,confidence='high',decision='R1 adds a missing-comma alternative; R2/R3 read a comma. Main sees the faint comma after S and retains C. This rejected new doubt is documented but not counted as a change.')
upd(52,final=r'\deleted{\unsure{Se|La} donner un}',diff_c=True,confidence='medium',decision='Choose R2 uncertainty on the first canceled word. Donner un is readable; do not adopt H donnée d’un.')
upd(54,final=r'\unsure{\deleted{où}à|à}',diff_c=True,confidence='low',decision='Choose R2’s uncertain state: possible overwritten où followed by final à, versus reinforced à alone. Neither state is silently asserted.')
upd(55,final='elément',diff_c=True,diff_h=True,confidence='high',decision='R1 reads élément, R2 elément, R3 élément|éléments. Main confirms R2: initial accent absent, second accent present, terminal singular t.',doubt_action='resolve')
extra=[]
for fid,path,key in [('N03',rp('R3','03_slanted_note'),'slanted_note'),('N07',rp('R3','26_condition_point'),'condition_point'),('N22',rp('R1','14_conditions_close'),'condition_close'),('N26',rp('R3','18_Z'),'quotient_alphabet'),('N31',rp('R1','18_tuple_gloss'),'gloss')]:
 f=copy.deepcopy(get('R3',fid));f['crop']=path;f['evidence']=obs['observations'][key]
 others={'N03':(r'\forall a\in A,',r'\forall a\in A,'),'N07':(r's=\sigma(a).',r's=\sigma(a).'),'N22':('no separate hook','no separate hook'),'N26':(r'\mathbb{Z}/n\mathbb{Z}',r'\mathbb{Z}/n\mathbb{Z}'),'N31':('plain S','plain S')}
 f['readers']={'R1':others[fid][0],'R2':others[fid][1],'R3':f['final']}
 f['decision']='Main adopts the indicated additional R3 reading after inspecting its location; see crop evidence.'
 extra.append(f)
extra.append(dict(place='Paragraph boundary after the order sentence',c='Paragraph break after est n',h='Same paragraph continues Donc ...',final='Same paragraph continues after est n, without an added period.',evidence=obs['observations']['paragraph_boundary'],confidence='medium',kind='other',marked_in_H=False,diff_c=True,diff_h=False,bbox=[270,1517,1650,1705],crop=mp('18_paragraph_boundary'),doubt_action='',s_id='',math_note='',readers={r:'Paragraph break after est n' for r in rep},decision='Main joins the ordinary manuscript line boundary; paragraphing follows the visible spacing, while wording and absent point remain unchanged.'))
fs+=extra
text=(root/'readings/scan008/R1/reading.tex').read_text()
replacements=[
 (r'\margin{\begin{tikzpicture}[scale=.43,transform shape]',r'\margin{\figure{\begin{tikzpicture}[scale=.43,transform shape]'),
 (r'\end{tikzpicture}}'+'\n\n% The condition label',r'\end{tikzpicture}}}'+'\n\n% The condition label'),
 ('pour tte arête',r'pour \unsure{tte|toute} arête'),
 (r'\deleted{\unsure{o|\omega}}',r'\deleted{\unsure{\omega|o}}'),
 (r'$\forall a\in A,\ \deleted',r'$\forall a\in A\quad\deleted'),
 (r'\deleted{$\forall s\in S,\exists1\,a\in A,$}',r'\deleted{$\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,$}'),
 (r'\draw[line width=.5pt] (0,-.15)--(5.35,-.15)--(5.35,2.25);',r'\draw[line width=.5pt] (0,-.15)--(4.95,-.15) .. controls (5.05,-.15) and (5.1,-.1) .. (5.15,-.05);'+'\n'+r'\draw[line width=.5pt] (5.35,.15)--(5.35,1.1);'+'\n'+r'\draw[line width=.5pt] (5.35,1.22)--(5.35,2.25);'),
 ('comme origine.\n\\[\n',r'comme origine\unsure{.|} $'),
 (r'u_{\omega}(s)&\ne s\end{aligned}\right]'+'\n\\]',r'u_{\omega}(s)&\ne s\end{aligned}\right]$'),
 ("l'extrémité de $a$\n\\[\n",r"l'extrémité de $a$ $"),
 (r'\end{aligned}\right]'+'\n\\]',r'\end{aligned}\right]$'),
 (r'\unsure{flèche|et}',r'\unsure{fleche|et}'),
 (r'\unsure{\operatorname{or}|{\rm Or}}',r'\operatorname{or}'),
 (r'\unsure{ou|$-$} $2^{\circ}\big\}$',r'\unsure{$-$|ou} $2^{\circ}\unsure{)}\big\}$'),
 (r'\simeq\mathbb{Z}/n\mathbb{Z}',r'\simeq\unsure{Z|\mathbb{Z}}/nZ'),
 (r'\deleted{\unsure{formé|form}} \inserted{\unsure{le}}',r'\deleted{formé} \inserted{le}'),
 (r'\unsure{lire|les}',r'\unsure{lire|les|i.e.}'),
 (r'\unsure{S,A|S\,A}',r'S,A'),
 (r'. $S$ et $A$',r'. $\underset{\unsure{\circ}}{S}$ et $A$'),
 (r'\deleted{Se donner un}',r'\deleted{\unsure{Se|La} donner un}'),
 (r'\deleted{\unsure{où}}à',r'\unsure{\deleted{où}à|à}'),
 ('$n$ élément muni','$n$ elément muni'),
 ('est $n$\n\n\\unsure{fleche|et}','est $n$ \\unsure{fleche|et}')
]
for old,new in replacements:
 assert text.count(old)==1,(old,text.count(old))
 text=text.replace(old,new)
(root/'decisions/scan008_final.tex').write_text(text)
inv=copy.deepcopy(rep['R2']['inventory'])
inv[2]['first_words_or_objects']='omega/o beneath final sigma'
inv[7]['first_words_or_objects']='lower rule and separate interrupted right stroke'
inv[21]['position']='adjacent to prose ending, two rows, x1230–1570 y820–927'
inv[24]['position']='adjacent to prose ending, two rows, x779–1633 y984–1125'
inv[32]['element']='continuation of order and comparison paragraph'
inv[32]['first_words_or_objects']='fleche/et … sss n≠2 … or(S,A,R)'
inv[33]['element']='continuation through cyclic group and torsors'
inv[33]['first_words_or_objects']='Et le grpe/gpe cyclique … des autom … torseurs'
inv[36]['first_words_or_objects']='grpe/gpe G raised zero/circle, leader before des'
inv[40]['first_words_or_objects']='Torseur sous Z/nZ = ensemble … n elément … Se donner un contour'
inv.insert(33,dict(sheet_kind='text',hand='his hand',element='small hook before closing brace',kind='insertion',position='after 2°, x1320–1350 y1810–1850',first_words_or_objects='short parenthesis-like hook, intent uncertain',transcribed='yes'))
inv.insert(40,dict(sheet_kind='text',hand='his hand',element='detached loop below S',kind='insertion',position='below S in S et A, x1090–1158 y1998–2060',first_words_or_objects='small oval retained under S; purpose uncertain',transcribed='yes'))
events=json.loads((root/'pending_events/scan008.json').read_text())
for e in events:
 e['who']=e['who'].replace(' preliminary check','')
 if e['statement_id']=='M008-E':e['outcome']=e['outcome'].replace('This check is conditional on the readers confirming the stated conditions in the ink.','All three readers confirm the individual conditions 1° and 2° as written; their equivalence is not imposed on the transcription.')
ids={'R1':['M008-D','M008-TYPE','M008-INV'],'R2':['M008-TYPE','M008-INV','M008-PAIR'],'R3':['M008-TYPE','M008-INJ','M008-INV']}
for r in rep:
 for i,sid in enumerate(ids[r]):
  c=rep[r]['checks'][i]
  events.append(dict(statement_id=sid,date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited/not exposed; scan008 {r}',type='targeted proof check',outcome=c['statement']+' '+c['reasoning']+' '+c['outcome']))
unresolved=[
 ('Opening contracted determiner','tte','toute','medium'),('Overwritten origin sign',r'\omega','o','low'),('Canceled existential in margin',r'\exists1',r'\exists','medium'),('Canceled lower margin first variable',r'\forall s\in S',r'\forall a\in S','medium'),('Condition label','O','0','medium'),('First canceled function',r'\omega(s)','w(s)','medium'),('Second canceled function',r'u_\omega','u','low'),('Canceled word after qui ait','comme','undertext still obscured','low'),('Point after origine','.','no point','low'),('Overwritten pair letter','R','B','medium'),('Shaft between pairs','-',r'\to','medium'),('Transition word','fleche','et','medium'),('Word after n≥3','donc','alors','medium'),('Link after orientation set','avec','sur','medium'),('Connector between 1° and 2°','-','ou','medium'),('Hook before right brace',')','uninterpreted short hook','low'),('First group abbreviation','grpe','gpe','medium'),('Second group abbreviation','grpe','gpe','medium'),('Raised mark on G','0',r'\circ','medium'),('Alphabet in first quotient','Z',r'\mathbb{Z}','medium'),('First word of gloss','lire','les; i.e.','low'),('Loop below S',r'\circ','uninterpreted pen loop; purpose uncertain','low'),('Canceled final lead-in','Se','La','medium'),('State before à',r'\deleted{où}à','à alone','low'),('Raised mark before circulaire',r'^{\times}',r'^{*}','medium')]
notes="""The title is “Orientation d’un contour.” No date or authorial page number appears; archive foliation 7 is recorded only as a comment. The page defines an orientation by an incident origin map σ:A→S with exactly one outgoing edge at each vertex, states that a connected contour has two orientations, defines successor maps on vertices and edges, and describes the resulting cyclic action and torsors. It begins a comparison between a Z/nZ torsor and a circular order, continuing off the page. The explicit added bound there is n≥1.

The three margin drawings, the slanted note with its tilde and canceled clauses, the separate separator strokes, and the insertion leaders are retained. Crop adjudication keeps the literal abbreviated forms, the absence of an initial accent in elément, the unmatched closing brace and gloss parenthesis, a small hook before the brace, and a detached loop beneath S. These last small marks have uncertain purpose. The canceled function attempts, compressed transition and gloss words, and possible overwritten où remain doubtful. Main inspection joins the ordinary line boundary after the order sentence; both small two-row brackets are kept beside their prose endings. Every original C doubt has an explicit retained or resolved outcome; new doubts and rejected new doubts are distinguished from them.

Actual checks are recorded individually in CHECK_EVENTS.tsv. The uniqueness condition makes σ bijective. Degree two then forces one incoming edge as well, so the successor is invertible and reversing orientation gives its inverse. Propagation of an edge direction gives exactly two orientations on a nonempty connected contour. For a finite connected contour, the successor has order n, and the orientation-preserving automorphisms form a cyclic group acting simply transitively on vertices and edges. The infinite bilateral case instead has infinite cyclic successor group. The order argument gives u=u⁻¹ iff n divides 2; the manuscript’s equivalence with n=2 uses the contour bound n≥2. At n=2 the two orientations induce the same automorphism; the subsequent bijection is valid with the preceding n≥3 qualification, so no unconditional error is asserted there.

The asserted equivalence of the two adjacency conditions does fail: on C4, the vertex permutation (0 1)(2 3) with induced edge permutation (1 3) satisfies condition 1 but not 2; the reflection fixing vertices 0 and 2 satisfies condition 2 but not 1. The exact finite certificate is retained. For distinct adjacency, their conjunction gives the two successor directions (one at n=2), as checked separately. Finally, “arc de S” is visibly written even though a belongs to A; this type mismatch triggered a crop and S is preserved. Reading or bracket inspection alone is not recorded as a proof event."""
dec=dict(base='R1',text_file='decisions/scan008_final.tex',findings=fs,inventory=inv,notes=notes,events=events,unresolved=[dict(place=p,reading=x,alternatives=a,confidence=c) for p,x,a,c in unresolved],abbreviations=rep['R1']['abbreviations'],main_crop_count=18,main_crop_views=obs['main_crop_views'])
(root/'decisions/scan008.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
assert len(obs['main_crop_views'])==44
assert len(events)==20
print({'findings':len(fs),'inventory':len(inv),'events':len(events),'unresolved':len(unresolved),'main_views':len(obs['main_crop_views'])})
