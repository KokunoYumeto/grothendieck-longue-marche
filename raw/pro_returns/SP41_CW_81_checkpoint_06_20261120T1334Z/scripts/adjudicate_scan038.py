"""Manual scan038 decisions after three complete returns and 18 local views."""
from pathlib import Path
import copy, datetime, json

w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan038/R{k}/return.json').read_text()) for k in (1,2,3)]
maps={
1:[1,2,None,3,[4,5],7,8,9,10,None,11,12,13,14,15,16,17,18,19,20,21,22,19,23,24,25,27,26,28,[29,30],30,31,32,33,34,35,36,37,6,25],
2:[1,2,3,4,5,6,7,7,7,None,8,None,9,10,11,12,13,14,15,16,17,[18,19],15,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,None,23],
3:list(range(1,39))+[None,26]
}
obs={
1:'Two tall t strokes follow the low ce opening and precede the final e return. Cette is resolved.',
2:'An additional low curved horizontal crosses the live Pi legs and projects left. The older complete glyph and its layer remain inseparable. Sigma/E and the possible deleted state remain uncertain.',
3:'The live glyph has one cap and two downward legs. Pi is first; the page does not supply a separate case contrast that settles Pi/pi. R2/R3’s first-occurrence uncertainty is retained.',
4:'The complete word has a long p descender, low ana, an open c, a tall h and an accented plural ending. Panachées is legible.',
5:'The crop separates on, the low r/e/s group and tall t of reste, en, then p descender, l loop, a and n. The terminal comma is visible. On reste en plan is resolved with all three readers.',
6:'The first omega has two low rounded bowls and raised outer ends, matching the second. Its lower 1 is separate. The C omega/w doubt is resolved.',
7:'The epsilon body has two stacked open returns, recurring in the same display and the diagram. Varepsilon is resolved independently of the superscript reading.',
8:'The first high sign has a short cap and a descending stem. Only a tiny thickening rises above the junction. Top is first with plus retained, following R1/R3.',
9:'The third high sign has the same cap and downward stem without a separately resolved upper arm. It follows the first occurrence’s top reading; the recurring plus alternative is recorded there.',
10:'The short low ou-shaped group has no separately resolved accent. R3’s ou first, où alternative is retained against R1/R2’s resolved où.',
11:'The cancelled lower-left label has a two-turn epsilon, a high crossed plus and a low hooked suffix. A rounded shoulder and foot favor 2, but the cancellation joins the suffix. R3’s 2/1 uncertainty is retained against the other readers’ resolved 2.',
12:'Four filled dots occupy two rows. Both diagonals point from a lower dot toward the opposite upper dot. The lower-left to upper-right shaft is continuous; the other has a gap at the crossing. H’s note supplies the four points and cancellation, but does not supply this crossing decoration.',
13:'The outer and middle capitals have a downstem, angular cap and right bowl with a lower return. Fraktur/calligraphic rendering remains open at the first occurrence.',
14:'Two surplus diagonal strokes cross inside the inner capital and merge with its live contours. The old X/cross identity and its cancellation state remain uncertain.',
15:'The inner capital has a long left stem, rectangular bowl and thickened right side. P remains first with calligraphic P and square alternatives; no expected formula determines the font.',
16:'A closing parenthesis immediately follows the inner capital; an opening curve then leads to X, followed by two closing curves. The observed final sequence is )(X)).',
17:'The nearby low wavy group is the horizontal main-line une/un, as the margin and revision crops jointly show. It is not an additional marginal word. The preliminary observation calling it a leader is corrected here. H’s trailing illegibility marker has no separate marginal text corresponding to it.',
18:'The initial une/un remains live. The heavy cancellation begins at famille. No separately added second un stands before ens. The final low turn of the first word remains ambiguous.',
19:'The raised replacement begins with a small e loop, joined low n/s bodies and a detached abbreviation point. Ens. is resolved.',
20:'The compact short word has a compressed opening, a tall crossed t and an ambiguous terminal return/high mark. Écrit remains first, with écrite and noté retained in R2’s order. Neither the terminal e nor the short prefix is securely separated.',
21:'Initial indi and the later tall paired loops are visible, but the intervening compressed bodies remain insufficiently separated. R2’s indiciellement/individuellement uncertainty is retained against R1/R3’s resolution.',
22:'A looped d and low e form one live de. The thin insertion leader passes above the bodies. No separate final s, cancelled de or duplicated de is visible.',
23:'Ens. and the entire parenthesis stand on the raised line over the cancelled famille. H marks only its separately supplied un as added, without an explicit note for this replacement group. This observed placement is recorded independently of its individual word readings.',
24:'The cancelled group begins with q and its long descender, then u, an apostrophe and two tall l loops followed by es. Qu’elles is legible beneath the cancellation.',
25:'The low abbreviation has a tall final stem whose cross is not securely separated; a smaller crossed t is raised, followed by a point. R2’s mut/mul uncertainty is retained. H’s supplied expansion and baseline ending do not reproduce the written abbreviation.',
26:'The right-edge word has p descent, low ana/c, a tall h and accented plural ending. Panachées is legible. Terminal punctuation is treated in a separate finding because both C and H contain a period there.',
27:'The value has one shallow arch and an elongated return, repeated before -aire. This does not securely separate n from nu. R1/R3’s uncertainty is retained against R2’s resolution.',
28:'Card begins with a large open C, followed by low a/r and tall d. The capital is legible.',
29:'The slanted note ends with the p-descender, low ana, h ascender and accented ending of panachée, followed by de and X. The entire target is included.',
30:'The heading is raised and underlined. No terminal point follows its f, resolving C’s point doubt. The high accent is compact and dot-like; R3’s dotted e is first and the acute remains possible. The diagonal placement leader passes above the live On.',
31:'One O/n group precedes dit, with no additional older group. The placement leader passes above its bowl. H’s extra cancelled On is unsupported.',
32:'The a/l/o/r/s bodies have a distinct cancellation through their lower portion. Alors is cancelled; que continues live.',
33:'The final dark return of panachée does not securely separate an additional s. R2/R3’s singular/plural uncertainty is retained against R1’s resolution. A distinct sentence point follows.',
34:'The complete parenthetical word has p descent, low ana, c/h and the final accented ending. Panachée is supported. The target word is complete in the crop; the following parenthesis lies partly outside it and is agreed in all three half-image readings.',
35:'Two small s forms give ss. The t after p is visibly raised. R1’s p with raised t is adopted against the two baseline renderings; no expansion is inserted.',
36:'Two detached curved commas follow qui and the omega-alpha respectively. Both are visible in the already inspected involution crop and both occur in all three complete readings. H contains neither.',
37:'A dense black initial body, compressed loops and overlapping zigzags conceal the cancelled word below transposition. One physically unreadable cancelled word remains; no word is supplied.',
38:'The terminal n of transposition is followed by blank space. The next main-line et lies below and to the left. H’s comma has no corresponding detached mark. Its note already acknowledges the whole passage’s added state.',
39:'After ens. two detached small hooks remain, without a securely closed low a body. R1’s colon-first reading with à retained is adopted; R2/R3’s resolved à is recorded.',
40:'The crop reaches the source’s physical right edge. A small dark nub joins the black edge band just after and below the word ending. Its independent identity is lost. R2’s uncertain period is retained; R1/R3 omit it. C and H both actually contain the period, correcting the incomplete C quotations in R1/R3’s combined word findings.'
}
crop_names={
1:'crops/scan038/main_cette.png',2:'readers/scan038/R3/01_opening_pi.png',3:'readers/scan038/R3/01_opening_pi.png',4:'crops/scan038/main_opening_panachees.png',5:'readers/scan038/R3/02_reste_en_plan.png',6:'readers/scan038/R3/03_display17.png',7:'readers/scan038/R3/03_display17.png',8:'readers/scan038/R3/03_display17.png',9:'readers/scan038/R3/03_display17.png',10:'readers/scan038/R3/04_ou.png',11:'readers/scan038/R2/04_diagram.png',12:'readers/scan038/R2/04_diagram.png',13:'readers/scan038/R3/06_first_margin.png',14:'readers/scan038/R3/06_first_margin.png',15:'readers/scan038/R3/06_first_margin.png',16:'readers/scan038/R3/06_first_margin.png',17:'readers/scan038/R3/06_first_margin.png',18:'readers/scan038/R3/07_revised_family.png',19:'readers/scan038/R3/07_revised_family.png',20:'readers/scan038/R3/07_revised_family.png',21:'readers/scan038/R3/07_revised_family.png',22:'readers/scan038/R3/07_revised_family.png',23:'readers/scan038/R3/07_revised_family.png',24:'readers/scan038/R1/crop08_quelles.png',25:'readers/scan038/R1/crop13_mut_panachees.png',26:'readers/scan038/R1/crop13_mut_panachees.png',27:'readers/scan038/R3/08_second_margin.png',28:'readers/scan038/R3/08_second_margin.png',29:'readers/scan038/R3/08_second_margin.png',30:'readers/scan038/R3/09_definition_heading.png',31:'readers/scan038/R3/09_definition_heading.png',32:'readers/scan038/R3/09_definition_heading.png',33:'readers/scan038/R3/10_definition_ending.png',34:'crops/scan038/main_parenthetical_panachee.png',35:'readers/scan038/R3/11_involution_insertion.png',36:'readers/scan038/R3/11_involution_insertion.png',37:'readers/scan038/R3/11_involution_insertion.png',38:'readers/scan038/R3/11_involution_insertion.png',39:'readers/scan038/R1/crop04_ens_a.png',40:'crops/scan038/main_eq24_terminal_edge.png'}

base=copy.deepcopy(rs[2]['findings'])
base.extend([copy.deepcopy(rs[0]['findings'][5]),copy.deepcopy(rs[1]['findings'][22])])
overrides={
20:dict(reading=r'\unsure{écrit|écrite|noté}',against_C=True,confidence='low'),
21:dict(reading=r'\unsure{indiciellement|individuellement}',against_C=False,c_doubt_status='retained'),
23:dict(reading=r'\inserted{ens. (\unsure{écrit|écrite|noté} \unsure{indiciellement|individuellement})}'),
25:dict(reading=r'\unsure{mut|mul}\textsuperscript{t}.',against_C=True,confidence='medium'),
26:dict(c='non panachées',h='non parallèles',reading='non panachées'),
30:dict(kind='other'),
35:dict(reading=r'ss p\textsuperscript{t} fixe',against_C=True),
40:dict(against_C=True,against_H=False,confidence='low',bbox=[1580,1600,1683,1730])
}
text_fallback={
(1,3):r'\Pi_1',(1,10):'où',(2,10):'où',(2,12):r'\bullet \arrow[ur,crossing over]',(2,39):'à',(3,39):'à'
}
d={'scan':38,'folder':'J81-05','their_page':37,'hua_has':'text','filename':'J81-05_81_scan038.tex','status':'decided','findings':[]}
for i,f in enumerate(base,1):
    f.update(overrides.get(i,{}));f['id']=f'SP41-038-{i:03d}'
    f['marked_in_H']='yes' if f['marked_in_H'] is True or f['marked_in_H']=='yes' else 'no'
    f['crop']=crop_names[i]
    f['evidence']='Main reader, personally viewed local crop: '+obs[i]
    f['main_adjudication']=obs[i]
    f['readers']={};f['reader_source_ids']={}
    for k in (1,2,3):
        sel=maps[k][i-1]
        if sel is None:
            f['readers'][f'R{k}']=text_fallback[(k,i)]
            f['reader_source_ids'][f'R{k}']=['reading.tex at this locus']
        else:
            ids=sel if isinstance(sel,list) else [sel]
            ff=[rs[k-1]['findings'][q-1] for q in ids]
            f['readers'][f'R{k}']=' ; '.join(z['reading'] for z in ff)
            f['reader_source_ids'][f'R{k}']=[z['id'] for z in ff]
    if i==36:
        for k in (1,2,3):
            f['readers'][f'R{k}']=r'qui, sur chaque $\omega_\alpha$, induit'
            f['reader_source_ids'][f'R{k}'].append('reading.tex, both commas')
    if i==40:
        f['readers'].update(R1='No terminal period in reading.tex',R3='No terminal period in reading.tex')
    d['findings'].append(f)

coverage={}
for k in (1,2,3):
    used={s for f in d['findings'] for s in f['reader_source_ids'][f'R{k}'] if s.startswith('scan038-')}
    expected={f['id'] for f in rs[k-1]['findings']}
    assert used==expected,(k,expected-used,used-expected)
    coverage[f'R{k}']={'raw_findings':len(expected),'mapped_findings':len(used),'all_mapped':True}
d['reader_finding_coverage']=coverage

t=(w/'readers/scan038/R3/reading.tex').read_text()
replacements={
"l'ens. à quatre":r"l'ens. \unsure{:|à} quatre",
r'\unsure{écrit|écrite} indiciellement':r'\unsure{écrit|écrite|noté} \unsure{indiciellement|individuellement}',
r'\text{sont mut\textsuperscript{t}. non panachées}':r'\text{sont \unsure{mut|mul}\textsuperscript{t}. non panachées\unsure{.}}',
r'ss pt fixe':r'ss p\textsuperscript{t} fixe'
}
for a,b in replacements.items():
    assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
d['inventory']=copy.deepcopy(rs[2]['inventory'])
for e in d['inventory']:
    if e['element']=='Interlinear replacement':e['first_words_or_objects']='ens. (écrit/écrite/noté indiciellement/individuellement)'
    if e['element']=='Formula (24)':e['first_words_or_objects']='forall alpha,beta in A, alpha ne beta; mut/mul with raised t; non panachées; uncertain terminal point'
    if e['element']=='Involution annotation':e['first_words_or_objects']='avec l’involution ss p with raised t fixe sigma'
u=copy.deepcopy(rs[2]['unresolved'])
for z in u:
    if z['place']=='Interlinear parenthesis before indiciellement':
        z.update(alternatives=['écrite','noté'],confidence='low',reason=obs[20])
u.extend([
{'place':'Opening after ens.','reading':':','alternatives':['à'],'confidence':'low','reason':obs[39]},
{'place':'Interlinear parenthesis, longer word','reading':'indiciellement','alternatives':['individuellement'],'confidence':'medium','reason':obs[21]},
{'place':'(24), abbreviation body','reading':'mut','alternatives':['mul'],'confidence':'medium','reason':obs[25]},
{'place':'(24), terminal point at physical right edge','reading':'.','alternatives':[],'confidence':'low','reason':obs[40]}
])
d['unresolved']=u
assert t.count(r'\unsure{')+t.count(r'\illegible{')==len(u),(t.count(r'\unsure{'),len(u))
d['notation']=[{'scan':38,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [2,3,6,7,8,9,11,13,14,15,16,25,27,30,35,39,40]]
d['abbreviations']=copy.deepcopy(rs[2]['abbreviations'])
for z in d['abbreviations']:
    if z['form']=='pt':z['form']=r'p\textsuperscript{t}'
    if z['form']==r'mut\textsuperscript{t}.':z['form']=r'\unsure{mut|mul}\textsuperscript{t}.'
notes=[
'The handwritten sheet carries section 1.3, display labels (17), (22), (23), (24), (25), and pencil archive number 37. No authored date, separate page number, title, question mark or explicit verification instruction was observed.',
'The opening source sentence writes non panachées and on reste en plan, followed by l’ens. and an uncertain colon/à. Display (17) gives the four-member expression. The first and third high marks have cap-and-downstem forms; top is first with plus retained at the first occurrence. Clearly crossed plus marks elsewhere retain plus. These shape comparisons assign no algebraic identity.',
'The source then gives the two strict comparisons in (22). The diagram has four filled points and arrows from each lower point to the opposite upper point, with a gap in one shaft at the crossing. The cancelled lower-left label retains epsilon2-plus first and epsilon1-plus as an alternative. H’s note acknowledges the points and cancellation; the crossing decoration and recovered label are the recorded differences.',
'Section 1.3 begins with a cancelled family phrase, followed by (23). Below it, une/un remains live, famille is cancelled, and ens. with the entire parenthesis is inserted above. Écrit/écrite/noté and indiciellement/individuellement remain open. One live de follows; qu’elles is cancelled after on suppose. The indexed family is a contextual cue only and does not resolve the compressed words.',
'The first oblique margin has three P-shaped capitals, an uncertain older crossed trace and the written final parenthesis sequence )(X)). The nearby wavy low group belongs to the horizontal une/un clause. The margin has no additional word corresponding to H’s trailing illegibility marker. No parentheses are moved to impose a different formula.',
'Display (24) writes the pairwise quantified condition with the abbreviation mut/mul and a raised t. Non panachées is legible. At the source’s physical right edge a possible terminal point merges with the dark band and remains uncertain. Both witnesses contain that period; uncertainty alone creates no H collation row.',
'The second slanted note writes Card A=n/nu and the underlined décomposition and n-aire terminology. The following definition has an inserted underlined dot-accent/acute heading, one live On and cancelled alors. Its final panachée/panachées ending remains uncertain; the parenthetical panachée is legible.',
'Display (25) gives the indexed disjoint sum. Its added passage names an involution ss p with raised t fixe sigma and states that it induces a transposition on each omega-alpha. Commas follow qui and omega-alpha; no comma follows transposition. One cancelled word remains physically unreadable. The sheet ends with a. These are accounts of the written statements, without an independent mathematical proof check.',
'All three complete readings and all detailed findings, inventories, notes and metadata were compared. Every raw finding is mapped. Seven C doubts are resolved and eleven retained. There are seventeen uncertainty macros plus one physically unreadable cancelled word, represented by eighteen unresolved entries. Root inspected eighteen local crops and no whole image or half. No OCR, outside research or compilation was performed.'
]
d['notes']=[{'id':f'scan038-note-{i:02d}','text':x} for i,x in enumerate(notes,1)]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan038','type':'carried as background without fault found','outcome':'Source-account and ink/witness comparison only; no independent mathematical verification claimed.'} for n in d['notes']]
d['sweep']=[]
d['main_crop_views']={'R1':[4,8,13],'R2':[4],'R3':[1,2,3,4,6,7,8,9,10,11],'main_new':4,'total':18}
d['crop_counts']={'R1':13,'R2':11,'R3':11,'main':4,'total':39}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
o=json.loads((w/'decisions/drafts/scan038_actual_crop_observations.json').read_text())
o['status']='All three full texts and all detailed return fields read; final decisions recorded.'
o['corrections_to_preliminary_observations']=[obs[17],obs[39]]
(w/'decisions/drafts/scan038_actual_crop_observations.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
record='# Scan038 main-reader local observations\n\nAll three complete texts and every detailed return field were read. Root viewed only the eighteen listed local crops.\n\n'
record+='\n\n'.join(f'{i}. {obs[i]}\n\n   Crop: `{crop_names[i]}`' for i in range(1,41))
record+='\n\nThe extra right-edge crop was made for the terminal point left open by the readers’ clipped boxes. The point merges with the photographed edge. R3’s heading crop clips adjacent leader continuation, but contains its target letters and descender. The parenthetical word crop contains the full word while some following punctuation lies beyond it. No settled target was recropped.\n'
(w/'decisions/scan038_main_observations.md').write_text(record)
(w/'pages'/d['filename']).write_text(t)
(w/'decisions/scan038.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'findings':len(d['findings']),'against_C':sum(f['against_C'] for f in d['findings']),'against_H':sum(f['against_H'] for f in d['findings']),'unsure':t.count(r'\unsure{'),'unresolved':len(u),'coverage':coverage}))
