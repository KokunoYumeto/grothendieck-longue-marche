from adjudication_helpers import *

d,rs,ts=start(11)
text=ts['R1']
oldA=r'\unsure{AA|\deleted{A}A|\lambda A|\deleted{\lambda}A|\mathbb{A}}'
newA=r'\unsure{A|\lambda|\deleted{A}|\deleted{\lambda}}A'
text=text.replace(oldA,newA)
text=text.replace('% The two lower index strings', '% The faint first impression before A is separate; its identity and live/cancelled state remain uncertain.\n% The two lower index strings')
r2map={2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12}
r3map={2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12}
cropmap={1:'readers/scan011/R1/crops/01_reduced.jpg',2:'readers/scan011/R1/crops/12_mentionning.jpg',3:'readers/scan011/R2/crops/01_sections_par.jpg',4:'readers/scan011/R1/crops/02_ramification_edge.jpg',5:'readers/scan011/R1/crops/04_cancelled_the.jpg',6:'readers/scan011/R1/crops/05_is_prime_mark.jpg',7:'readers/scan011/R1/crops/06_characteeristic.jpg',8:'readers/scan011/R1/crops/07_by.jpg',9:'readers/scan011/R1/crops/08_local_ring_A.jpg',10:'readers/scan011/R1/crops/09_x_index_slots.jpg',11:'readers/scan011/R1/crops/10_n_index_slots.jpg',12:'readers/scan011/R1/crops/11_before_one.jpg',13:'readers/scan011/R1/crops/11_before_one.jpg'}
evidence={
1:'In the sixth cell, a tall right ascender and leftward top serif match the height of the following d. The lower body is dense and contains an e-like horizontal stroke. Main confirms the additional d-like form detected only by R1; plain reduced does not account for it. A single d and both d/e overprint orders remain alternatives, because the low body does not establish a unique decomposition or sequence.',
2:'Only two crowded cells lie between clear mention and final g. Each contains a raised dot and broad i-like foot as well as an n-like arch/right stem. Main accepts R1’s two-cell component analysis, with both orders independently retained in each cell; R2/C’s three consecutive nin letters do not fit the cells. R3’s additional single-impression alternatives are unnecessary once both dots and arches are accounted for. The expected spelling does not determine correction order.',
3:'A separate raised par. lies immediately above the cancelled sections. Its p descender, a bowl, r hook and point are visible. The baseline word is crossed by cancellation impressions. H retains the cancellation but omits the replacement abbreviation.',
4:'The final n is complete next to the narrow remaining paper strip. The crop includes the lower-right area and the physical edge; no separate point survives. Both witnesses add a period that cannot be transcribed from the visible fragment.',
5:'The three cancelled cells between that and if retain tall t and h strokes and an e body beneath crossing overtypes. Main confirms the readable cancelled the omitted by H.',
6:'Two small dark marks stand above the gap after is: a round lower-left point and a taller tapered upper-right mark. Main preserves their relative geometry using R1’s compact inline TikZ and a local doubt. No punctuation name, semantic function or hand/instrument is assigned.',
7:'The run after t has two distinct e-shaped cells: the first is pale and carries an acute, the second is dark and unaccented. H loses the second e. The extra cell is not merely the acute of a single letter.',
8:'The first cell b is clear. The next has a definite hooked y descender below the baseline and a heavily inked upper body with an e-like interior horizontal stroke. Main favours R1’s single-y-first encoding while retaining both possible e/y correction orders. Plain be cannot account for the descender; the second component and its sequence remain uncertain.',
9:'A pale two-legged angular impression occupies a separate cell to the left of the dark serif A. Its crossbar and any cancelling stroke are unresolved. Main adopts R3’s local A/lambda/live/cancelled alternatives, leaving the certain dark A outside the doubt. The full-cell separation does not support a single double-struck A; that earlier alternative is rejected. Faintness is not evidence of cancellation.',
10:'The lowered 1, separately dotted i and r have clean blank spaces between them. Neither relation slot contains the diagonal or horizontal strokes of H’s inequalities. Main independently confirms this first range from its crop.',
11:'The second lowered range again has 1, a dotted i and r with unmarked intervening spaces. It is checked separately from the x range. H supplies two absent inequalities.',
12:'The extra cell before g retains an r-like upper hook, while its lower strokes cross obliquely, unlike the ordinary later r. Main accepts R1’s possible cancellation, with a live r alternative retained. R2/C record it confidently live; R3 also leaves it live; H omits the extra impression entirely.',
13:'The space after the final s and before 1 is wide and blank; 1 and its following comma are clear. No greater-than stroke or equality line is visible. The separate uncertainty about the extra r is recorded in its own row.'
}
for i in range(1,14):
 row=row_from(rs['R1'],i,crop=cropmap[i],scan_shows=evidence[i])
 row['readers']={'R1':rs['R1']['differences'][i-1]['reading']}
 for who,mp in [('R2',r2map),('R3',r3map)]:
  row['readers'][who]='reduced' if i==1 else rs[who]['differences'][mp[i]-1]['reading']
 if i==4:row['final']='ramification'
 if i==9:row['final']=newA
 if i==10:row['consequential']='Retains two blank relation slots in the x-index range; removes H’s supplied inequalities.'
 if i==11:row['consequential']='Retains two blank relation slots in the n-index range; removes H’s supplied inequalities.'
 if i==13:
  row.update(c=r'\quad1',h=r'\geqslant 1',final=r'\quad1')
  row['consequential']='Retains the blank before 1; removes H’s supplied greater-than-or-equal sign.'
 d['rows'].append(row)
d['rows'].insert(4,dict(place='Paragraph 1, final s of variants at physical right edge: retained C doubt',c=r'variant\unsure{s}',h='variants',final=r'variant\unsure{s}',against_c=False,against_h=False,kind='other',marked_in_H=False,confidence='low',scan_shows='The t reaches the edge. A narrow curved dark remnant immediately to its right is compatible with part of s but merges with the exterior. Main retains the local s doubt; no full hidden letter is reconstructed. All three readers retain this uncertainty.',crop='readers/scan011/R1/crops/03_variants_edge.jpg',readers={who:r'variant\unsure{s}' for who in ['R1','R2','R3']}))
d['doubts']=rs['R1']['remaining_doubts']
d['doubts'][2]['confidence']='low'
d['doubts'][5]=rs['R3']['remaining_doubts'][4]
d['inventory']=rs['R1']['inventory']
# Put all elements in physical reading order; inline formulas remain part of their text blocks.
d['inventory']=[d['inventory'][i] for i in [0,5,6,7,3,2,1,4,8,9,10,11,12,13]]
for i,inv in enumerate(d['inventory'],1):
 inv['element']=f'E{i:02d}';inv['sheet_kind']='letter';inv['transcribed']='yes'
d['inventory'][-1]['kind']='margin note'
d['inventory'][10]['first_words_or_objects']='Separate faint A/lambda-like cell followed by clear dark A; first cell alone uncertain'
d['notes']=rs['R1']['notes']
d['notes']['content']='Continuation of the preceding letter to Murre, in two typed prose paragraphs. The upper paragraph discusses the proposed arrangement, a normality assertion, general ramification and its variants. The lower paragraph proposes a broader formulation of theorem 6.4, makes a residue-characteristic/specialization assertion, and begins a regular-local-ring setup that continues beyond the page. These are reported as unverified claims of the letter. The typed par. replacement, cancelled sections and the, crowded correction cells, two raised spots of uncertain origin and archival 10 are all retained. No title, date, signature, authorial foliation, separate display or diagram is present.'
d['notes']['author_checks']=rs['R1']['notes']['author_checks']+['I doubt however it will be much simpler','This statement is non empty only when s is of char. zero, of course — authorial qualification, not independently verified here.']
d['notes']['math_reading_decisions']=[
 'The normality and inertia/specialization assertions remain unverified page content. The local-ring sentence is incomplete on this page; no continuation or missing hypothesis is supplied.',
 'Main personally inspected both lower ranges and the slot before 1. All five relation positions are blank. The missing signs are retained as spacing, despite H’s conventional completions.',
 'The faint first impression before A is separate and unresolved. It is not suppressed to produce a conventional ring name, and it is not encoded as one double-struck A.',
 'Plain S, V, Z, D, x, n, s and k, separately underlined n and a on Z, and dotted i indices are recorded consistently with the earlier notation observations. No alphabet change is inferred from mathematical expectation.',
 'No targeted proof, re-proof, computation or background theorem was used to establish a mathematical claim on this page. Visual notation checks are not counted as mathematical check events.'
]
d['check_events']=[]
d['slips']=['affraid, developped, reamrk, charactéeristic and noecessarily retained. The sixth cell of reduced, two medial cells of mentioning, and extra r in intergers carry physical-state uncertainty rather than normalized spelling.']
d['workflow']=dict(brief='brief_v008_scan011.md',r1_crops=12,r2_crops=7,r3_crops=8,main_crops=0,main_reader_crops_viewed=13,feedback='Main compared all complete returns and viewed all twelve R1 crops plus R2’s raised-par. crop, once each. No new crop or repeated view was needed. R1 alone detected the d-like ascender in reduced and possible cancellation of the extra r; both are retained under doubt after main inspection. R1/R3 detected the two overprinted n/i cells. R3’s narrower uncertainty for the separate faint A/lambda component is adopted. All three original C doubts remain unresolved, with scope/alternatives updated only where supported. The tiny raised spots are represented geometrically with unknown origin. Inventory is reordered top-to-bottom and identified as a letter continuation using the already decided preceding page. No new brief rule is required: v008 directly addressed the remaining component/order and uncertain-origin issues.')
d['main_adjudication_complete']=True
save(d,text)
