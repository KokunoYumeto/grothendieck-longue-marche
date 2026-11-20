"""Consolidate page 10 from the three returns and root's viewed local crops."""
from pathlib import Path
import json, copy

O=Path('out'); stem='C123-02_123_scan023'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
T={r:(O/'readers'/stem/r/'reading.tex').read_text() for r in R}
r1=f'readers/{stem}/R1/';r2=f'readers/{stem}/R2/';root=f'decisions/rootcrops/{stem}/'
t=T['R1']
def change(old,new):
 global t
 assert t.count(old)==1,(old,t.count(old))
 t=t.replace(old,new)
def d(reader,n):return next(x for x in R[reader]['differences'] if x['id']==f'{reader}-D{n:02}')

be=d('R2',1)['reading'].replace(r'\draw[line width=.25pt] (e.north) -- ++(0,2.5);',r'\draw[line width=.20pt] (e.north) -- ++(0,2.30);'+'\n  '+r'\draw[line width=.35pt] ([yshift=2.30ex]e.north) -- ++(0,.20);')
start=t.index(r'\begin{tikzpicture}');end=t.index(r'\end{tikzpicture}',start)+len(r'\end{tikzpicture}')
change(t[start:end],be)
cancel_this=r'''\begin{tikzpicture}[baseline=(th.base),x=1em,y=1ex]
\node[anchor=base west,inner sep=0pt] (th) at (0,0) {\deleted{this}};
\node[anchor=base west,inner sep=0pt] at ([xshift=.10em]th.base east) {\texttt{x}};
\end{tikzpicture}'''
change(r'\deleted{this}',cancel_this)
# R2's D cell preserves an independently visible lower-right projection.
old=t[t.index(r'\mathrm{D}_{'):t.index(r'\mathrm{E}_{')]
new=d('R2',12)['reading'].replace(r'\end{tikzpicture}}}},',r'\end{tikzpicture}}|\mathbb{r}}},')
change(old,new)
dim=r'''dim\begin{tikzpicture}[baseline=(de.base),x=1em,y=1ex]
\node[anchor=base,inner sep=0pt] (de) at (0,0) {e};
\node[anchor=base,inner sep=0pt] at (.035,.62) {\unsure{o|e}};
\draw[line width=.25pt] (-.16,-.14)--(-.20,-.50);
\draw[line width=.25pt] (.13,-.12)--(.12,-.43);
\draw[line width=.25pt] (.12,.90)--(.26,.58);
\end{tikzpicture}nsion'''
a=t.index(r'dim\unsure{');b=t.index('nsion of the set',a)+len('nsion')
change(t[a:b],dim)
oo=d('R2',27)['reading'].replace(r'\unsure{*|\mathrm{t}}',r'\unsure{\mathrm{t}|*}')
change(r"\underline{\mathrm{O}}_{\mathrm{F}'}^{\deleted{\unsure{\mathrm{t}|*}}}",oo)
w=r'''\text{\begin{tikzpicture}[baseline=(ww.base),x=1em,y=1ex]
\node[anchor=base,inner sep=0pt] (ww) at (0,0) {$\mathrm{W}$};
\node[inner sep=0pt] at (.20,-.48) {\unsure{\begin{tikzpicture}[x=1em,y=1ex]\fill (0,0) circle (.20pt);\end{tikzpicture}}};
\end{tikzpicture}}'''
change(r'/\mathrm{W}$ (resp.', '/'+w+'$ (resp.')
change(r'\draw[line width=.25pt] (0,.48)--(0,.41);',r'\fill (0,.53) circle[radius=.008cm];'+'\n'+r'\draw[line width=.25pt] (0,.48)--(0,.41);')
t+='\n% The extra x following cancelled this is a cancellation impression, not a live word.\n% Dimension retains two lower projections and an upper internal diagonal without an inferred predecessor.\n% The small isolated point below the later W is drawn with origin/function uncertainty; it is not assigned as punctuation or an index.\n'

spec=dict(stem=stem,base_reader='R1',brief='reader_v10.md',main_new_crops=9,text_edits=[dict(old=T['R1'],new=t)],difference_overrides={},additional_differences=[])
def ov(n,**kw):spec['difference_overrides'].setdefault(f'R1-D{n:02}',{}).update(kw)
for n,c in {2:'first_map.png',3:'where_g.png',4:'cartan_h.png',5:'orbit_g.png',14:'caracteristic.png',18:'x_in_g.png',21:'second_map.png',22:'rational_quotes.png'}.items():ov(n,crop=root+c)
ov(6,crop=r2+'02_analoguous.png')
ov(1,final=be,readers='R1: no blank and a uniform raised trace; R2: trace anchored above e; R3: same attachment with a darker short upper segment. Root retains the e attachment and darker upper segment.',evidence='The consecutive typewriter cells have no blank. A thin upright rises above e, with a darker short upper end; it is drawn at that attachment.')
ov(8,final=cancel_this,c_changed=True,evidence='The cancelled t,h,i,s remain readable. An additional typewriter x occupies the blank cell immediately after the word; it continues the cancellation run and is drawn separately.',readers='R1: deleted this, report notices extra x but text omits it; R2: deleted this only; R3: deleted this only. Root retains this and the extra cancellation impression.')
ov(9,readers='R1: raised n-, medium unresolved, leader and low point drawn; R2: same glyphs, typed medium favoured, leader and point drawn; R3: typed medium favoured, leader drawn, low point wrapped in doubt. Root keeps the definite n- and point, medium and point function unresolved.',evidence=d('R1',9)['evidence']+' Root sees a definite separate low point, without assigning it punctuation. H explicitly describes n- as handwritten in its editorial note.')
ov(11,readers='R1: uncertain n/r overlay with same-letter r alternative explicit; R2: uncertain n/r overlay, same-letter alternative in report; R3: uncertain r/n overlay, same-letter alternative in report. Root retains R1’s local alternatives without deciding strike order.')
ov(12,final=new.rstrip(','),readers='R1: n/r overlay with same-letter r alternative but no separate tail; R2: n/r overlay with lower-right tail; R3: r/n overlay, tail described but not separately drawn. Root retains R2’s tail geometry and R1’s explicit same-letter alternative.',evidence='Rounded and shouldered contours overlap without a datable order. A short independent low-right diagonal/terminal is visible and retained; n/r and repeated-r interpretations remain uncertain.')
ov(15,readers=r'R1: \deleted{a}; R2: \deleted{a}; R3: \deleted{\unsure{a|u}}. Root chooses a: a closed lower bowl and surviving upper contour remain beneath the crossing strokes.')
ov(16,readers='All three see paired upright quotations. R1/R2 resolve the enclosed cancelled letter to a; R3 retains a/u, separately adjudicated in D15. No extra letter correction is counted in this quotation row.')
ov(17,final=dim,readers='R1: two alternative complete e/o and e/e drawings; R2: definite lower e and uncertain raised o/e; R3: uncertain e/o drawing, e/e permitted in report. Root localizes doubt to the raised contour and adds the two lower projections and upper internal diagonal that the reader drawings omit.',evidence='The baseline e crossbar/bowl is definite. A second higher rounded contour admits o or e. Two short lower projections and a diagonal within the upper area also survive; none establishes a chronological predecessor.')
ov(27,final=oo,crop=r2+'12_R_formula.png',c_changed=True,kind='insertion or placement',readers='R1: cancelled t|* in superscript syntax; R2: cancelled *|t beside O and above F-prime in an explicit local layout; R3: cancelled *|t in superscript syntax. Root retains t|* at low confidence, with R2’s observed placement.',evidence='Short upper prongs, a central stem-like remnant and a rightward arm survive under cancellation; t is a tentative first candidate, star remains possible. The cluster sits directly above the lowered F-prime at roughly the middle height of O, not as a high mathematical exponent.')
ov(28,readers='R1: w with drawn rounded enclosing contour, u alternative; R2: w|u without the separate contour; R3: overlaid w/u. Root uses R1’s visible broad U-like contour, without asserting a predecessor or strike order.')
ov(29,readers='R1: definite e with extra upright drawn; R2: e-plus-trace enclosed in unsure although prose calls e identifiable; R3: same whole composite enclosed in unsure although prose calls e definite. Root keeps e definite and the upright present, with its medium/function unresolved.')
ov(33,final=t[t.index(r'\figure{'):t.index('% The raised line')].strip(),readers='R1: closing and signature in one positional drawing; R2: signature shifted right by 60 percent of line width; R3: closing slightly indented and signature shifted by 62 percent. Root uses R1’s relative-position drawing; all agree the signature is substantially right and lower.')
ov(34,readers='R1: raised signature point drawn and inventoried; R2: high speck reported but omitted from text/inventory; R3: omitted. Root retains the point above the early surname region, not as a period after A.')
ov(35,final='Five main short vertical segments plus the small upper point, drawn with origin/function uncertainty.',confidence='low',readers='R1: five segments, no upper point; R2: upper point plus six segments; R3: four segments. Root sees five main separated segments and the small upper point, using R1 geometry plus that point.',evidence='Five principal dark near-vertical segments and a tiny separate upper point are visible beside a pale edge. Ink versus surface origin and function are unresolved; no letter or arrow is supplied.')
spec['additional_differences'].append(dict(id='ROOT-01',place='Line 20, isolated point beneath later W',C=r'\mathrm{W}',H='W',final=w,evidence='The existing root second_map crop shows a separate small dark point just below the right side of the typed W. It is drawn with origin/function doubt and no punctuation or index role.',confidence='low',kind='drawing or diagram',marked_in_H='no',c_changed=True,h_changed=True,crop=root+'second_map.png',bbox=[1254,1442,1262,1451],bbox_source='source/SP57_CW_97+123+162-1+162-6_scans/'+stem+'.jpg',readers='R1: omitted; R2: omitted; R3: omitted. Root retains the visible point separately from the definite W.'))

cd=copy.deepcopy(R['R1']['c_doubts'])
for x in cd:
 if x['place'].startswith('D subscript'):x['decision']='Unordered n/r overlay with explicit same-letter r alternative and low-right projection.'
 if x['place']=='Crowded vowel in dimension':x['decision']='Definite lower e, uncertain raised o/e contour, two lower projections and an upper internal diagonal; chronology unassigned.'
 if x['place']=='Cancelled sign above O subscript':x.update(decision='Retain cancelled t|* with low confidence; place beside O directly above the lowered F-prime, not as a high exponent.',crop=r2+'12_R_formula.png')
spec['c_doubts']=cd
rd=copy.deepcopy(R['R1']['remaining_doubts'])
for x in rd:
 if x['place']=='D subscript':x['reading']='unordered n/r overlay with low-right projection; repeated r remains an alternative'
 if x['place']=='Dimension vowel':x['reading']='definite lower e plus higher o/e and three additional short traces'
 if x['place']=='Bottom interrupted trace':x.update(reading='five principal short vertical segments plus an upper point',confidence='low')
rd.append(dict(place='Low point beside n- leader',reading='separate visible point',alternatives=['unassigned ink point','surface trace; no punctuation function established'],confidence='low'))
rd.append(dict(place='Point below later W',reading='small isolated point drawn',alternatives=['unassigned ink point','surface/scan trace; no punctuation or index attachment established'],confidence='low'))
spec['remaining_doubts']=rd
inv=copy.deepcopy(R['R1']['inventory'])
for x in inv:
 if 'handwritten' in x['hand'] and x['hand']!='archival handwriting':x['hand']=x['hand'].replace('handwritten','unnamed handwriting')
 if x['element']=='D subscript overprint':x.update(kind='drawing',first_words_or_objects='overlapping n/r or restruck r; separate low-right projection')
 if x['element']=='Dimension vowel overprint':x.update(kind='drawing',first_words_or_objects='definite lower e, raised o/e contour, two lower projections and upper diagonal')
 if x['element']=='Interrupted lower vertical trace':x['first_words_or_objects']='five principal short segments and small upper point'
inv.insert(next(i for i,x in enumerate(inv) if x['element']=='Raised n-'),dict(sheet_kind='letter',hand='typewriter cancellation impression',element='Extra x after cancelled this',kind='drawing',position=[1572,542,1608,581],first_words_or_objects='x continuing the cancellation in the following blank cell',transcribed='yes'))
inv.insert(next(i for i,x in enumerate(inv) if x['element']=='Repeated Steinberg arrow'),dict(sheet_kind='letter',hand='ink or surface trace, unresolved',element='Isolated point below later W',kind='drawing',position=[1254,1442,1262,1451],first_words_or_objects='small point below right side of W',transcribed='yes'))
spec['inventory']=inv
spec['notes']=(O/'decisions'/f'{stem}_notes.md').read_text()
spec['consequential']=[
'The letter literally expects rank < r-1 in the other root-length cases. The crop confirms the strict <; an internal C2/PSp4 calculation refutes that universal expectation without changing the source.',
'Underlined ordinary g, h and O are preserved; neither Fraktur nor script is substituted. The cancelled O-adjacent t/star remains local and has no assigned mathematical role.',
'The raised n- is certain and yields n-r-2 with the baseline r-2; its medium is uncertain. Both leaders, cancellation layers and unresolved subscript overlays remain.']
spec['check_events']=[dict(statement_id='123-023-reader-dimension-substitution',who='GPT-6 Astra Pro; inherited effort (not exposed); fresh '+reader+' page 10',type='targeted proof check',outcome='The independent reader reported substituting 2N=n-r and i=1 into 2N-2i to obtain n-r-2. This checks internal arithmetic only, not orbit dimensions, rank or medium.') for reader in ('R1','R2','R3')]
spec['workflow_note']='Three fresh readers used v10, with 14/15/14 targeted crops. Root compared every complete reading and report, viewed all fourteen R1 crops, R2 crops 02 and 12, and made nine new local crops: eight half-settled witness differences plus the strict inequality rechecked after the matrix counterexample. One attempted first_map image output failed at the context boundary and was then displayed from the same saved file; no failed output counted as an observation. One combined report output was truncated; the missing sections were subsequently read in bounded output. The H packet originally included the next unassigned cover; it was corrected, readers notified, and the excluded material preserved as packet-boundary evidence rather than counted as an H error. The text-only union audit found omissions in reported graphics: the extra cancellation x, one signature point, and the D-index tail. Root restored these and the observed dimension traces, and reconciled the lower trace to five main segments plus an upper point. Nine mathematical check events had already been recorded at 03:45:54; only the readers’ actual arithmetic check is appended on finalization. v11 makes the report-to-drawing audit more concrete and asks that distinct extra cancellation impressions and points remain separately accounted for.'
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(json.dumps({'loci':len(R['R1']['differences'])+1,'inventory':len(inv),'remaining':len(rd)}))
