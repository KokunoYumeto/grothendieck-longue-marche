"""Main reader's explicit scan 029 decisions after comparing three returns and crops."""
from pathlib import Path
import json,copy,datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan029/R{i}/return.json').read_text()) for i in (1,2,3)]
mp2=list(range(1,29))+[43,29,30,31,32,36,37,38,39,42,40,41,34,33,4]
mp3=[4,5,7,8,9,10,12,14,15,16,17,18,19,20,21,22,24,25,26,30,32,33,36,37,38,39,40,41,1,2,3,13,23,27,28,28,29,31,34,35,11,8,8]
r2names={int(p.name[:2]):p for p in (w/'readers/scan029/R2').glob('*.png')}
cropnums=[1,1,3,3,3,4,3,5,5,5,6,7,8,8,9,9,9,10,11,12,12,13,13,13,14,14,15,16,17,2,2,0,9,11,0,0,0,12,13,13,4,3,3]
obs={
1:'Two dark crossed centres lie inside the enclosing curves, but the left centre merges into the boundary. Retain the two-star first reading and one-star alternative.',
2:'The initial e-like loop, deep descending middle stroke and low terminal curls leave the ending open. Retain exprime, expriment, exprimons and exigeons. The separate que, si and alors are visible in the rotated strip; H’s ensemble and donc do not describe these written groups.',
3:'A heavy horizontal cancellation crosses the old line. The q-like descender, si/s marks, low est/un groups and tall ending survive only partly. Retain the proposed phrase under an uncertainty mark; do not complete its final d’or.',
4:'Two compact crossed centres are separately visible at the start of the inserted line. Resolve this occurrence as (**); the independent marginal occurrence retains its own uncertainty.',
5:'The connected low ens strokes end before a blank interval and U_s. There is no separate abbreviation point.',
6:'A tall initial, low n and open c are followed by a distinct point, then à and s. Adopt inc. à s.',
7:'A thin line enters before f and crosses the body of façon, near the f cross-stroke and insertion leaders. Retain uncertainty between cancellation and live text.',
8:'Crossed curved strokes with curled terminals form script X. The supplied mathcal X represents that visible script form; no further font identity is inferred.',
9:'Under the cancellation, an ascending diagonal, tall right leg and transverse bar form A. Resolve A as R2/R3; retain the live X beside it. The stipulated old-form-before-replacement order is used, without adding an insertion leader that is absent at this glyph.',
10:'The tiny label contains esp. and top., each with its point, above a curved leader directed toward underlined Gamma.',
11:'The accent is a strong near-vertical slanted dash with a small weak lower trace. Retain arète|arête, with the single grave-like stroke first, as R1/R2. R3 places the circumflex first.',
12:'The first letter has a closed low loop and tall d stem; the following low run gives donner.',
13:'The raised mark has short radial arms crossing a central knot. Resolve the star as R1/R2; R3’s uncertainty is retained in the comparison record.',
14:'An internal diagonal returns inside the broad open curve. Retain membership first and inclusion second, as all three readers; no change is made from the expected set relation.',
15:'The short low corr group has no independent final point and no following letters spelling the expanded word.',
16:'An earlier upright and loop are crossed beside the live b. The overlap leaves a possible old i unseparated; retain b|bi as R1/R3, rather than resolving only b as R2.',
17:'A tall initial and final upright flank a flattened low middle beneath the cancellation. Retain the uncertain tout reading.',
18:'The p descender, separate t, looped d and low e remain visible under a straight cancellation. Resolve pt de.',
19:'Pour is above the line with its insertion leader. The baseline has two close tall t strokes and a small e, giving tte.',
20:'A small initial loop with two joined rises and a terminal tail gives aux; there is no tall initial d.',
21:'Two dark points are definite. A much paler aligned mark may be a third point; retain ..|....',
22:'One continuous l/e/s group is written. The terminal curl is thickly retraced, with no confidently separable cancellation. Preserve the common le once and mark the final s as live|deleted, as R1. R2 gives the same alternatives at word scope; R3 omits the visible s in its second candidate.',
23:'The two oblique cancellation strokes are clear, but the small original arch and terminal upright merge into them. Keep the old nt uncertain, as R1/R3; R2 resolves it.',
24:'A densely overwritten knot at superscript height retains short outward points and a tiny opening. Keep its star identity uncertain, as R1/R3; R2 resolves it.',
25:'Beside the apostrophe of d, two additional high ticks precede the accented e. Resolve an opening double-quote pair, represented by two backticks under the supplied convention. No closing pair is supplied.',
26:'A tall b stem with low bowl and a second short i upright survive the transverse cancellation. Resolve bi.',
27:'The first a has a single detached high stroke. The second has two joined angular turns and a descending right end. Retain a double prime first and a bent single prime second.',
28:'The crop separates s, the tall crossed t, a low following wave and a raised crossed t. The low wave does not separate all of r/i/c/t. Retain str with raised t first, as R1 and the main reading, followed by stric and strict with raised t. R2/R3 prefer stric. No ement is supplied.',
29:'The descending hook is continuously attached to the terminal low s stroke of plus. No independent comma mark is visible in the gap before si. Adopt De plus si, as R1/R3; R2 reads the attached hook as punctuation.',
30:'The decomposition glyphs have a long roof and two long near-upright legs. Use capital Pi first with pi as the retained case alternative at the first occurrence, consistently with the earlier notation record.',
31:'The initial tall b-like stroke, detached i dot and low en continuation support bien. Resolve bien as R2/R3. The final non elsewhere on this page does not alter this reading.',
32:'The short word has a low a, r, tall b stroke and final re before topologique. Adopt arbre.',
33:'A looped initial d, separated low n strokes and accented ending give donnée before avec.',
34:'The dominant crossed curved strokes give script X with a star. A thinner left upright, upper return and lower horizontal survive beneath it. Retain R3’s possible earlier underlined Gamma under an uncertainty mark that includes its cancelled state; R1/R2 transcribe only X. The live X follows the uncertain overwritten form without an added insertion leader.',
35:'After the comma, une is followed by exact- at the line end and ement at the next line start. There is no separate preceding a or written et une seule.',
36:'Two p descenders and the tall terminal strokes identify appartient, followed by a separate accented à and A-prime.',
37:'The long l, apostrophe, low autre group and separate accented à precede S. The à occupies H’s unreadable position.',
38:'A distinct separate horizontal bar is drawn beneath the last NB Gamma. H uses plain Gamma at this occurrence, outside the bold-Gamma encoding specified in its own note; record this missing bar.',
39:'The terminal s of points is blackened by crossing strokes; the common point and its t crossbar remain live.',
40:'A small a and high prime sit above the line, with a V-shaped leader into the space after point and before de.',
41:'The short rounded group following the comma has a detached accent and reads où before a,b.',
42:'The compact live est appears beneath the cancellation immediately before d’ordre 2.',
43:'The smaller replacement line begins with the starred label below the cancelled line and continues through the left margin. Its attachment is after faut exiger; H’s body interleaves the old cancellation among live words. Its editorial layout note is not added to the manuscript text.'
}
d={'scan':29,'folder':'J81-04','their_page':28,'hua_has':'text','filename':'J81-04_81_scan029.tex','status':'decided','findings':copy.deepcopy(rs[0]['findings'])}
for i,f in enumerate(d['findings'],1):
 sources=[rs[0]['findings'][i-1],rs[1]['findings'][mp2[i-1]-1],rs[2]['findings'][mp3[i-1]-1]]
 f['id']=f'SP41-029-{i:03d}'
 f['readers']={f'R{k}':s['reading'] for k,s in enumerate(sources,1)}
 f['reader_source_ids']={f'R{k}':s['id'] for k,s in enumerate(sources,1)}
 f['marked_in_H']='yes' if f['marked_in_H'] in [True,'yes'] else 'no'
 c=f['confidence'];f['confidence']=c if c in ['high','medium','low'] else 'medium' if c in ['medium-high','medium-low'] else 'low'
 if cropnums[i-1]:f['crop']=str(r2names[cropnums[i-1]].relative_to(w))
 f['evidence']='Main reader, cited crop: '+obs[i]
 f['main_adjudication']='Three complete readings and finding lists compared; final decision made by the main reader from the cited crop.'
 if f['c_doubt_status']=='resolved':f['against_C']=True
f=d['findings']
f[1]['reading']=r'\unsure{exprime|expriment|exprimons|exigeons} que si ... alors'
f[3].update(c_doubt_status='resolved',against_C=True,confidence='medium')
f[8].update(reading=r'\deleted{A}\mathcal{X}',c_doubt_status='resolved',against_C=True,confidence='medium')
f[12].update(c_doubt_status='resolved',against_C=True,confidence='medium')
f[27]['crop']='readers/scan029/R1/crops/19_strict_abbreviation.png'
f[28].update(against_C=True,against_H=False,confidence='medium')
f[30].update(reading='bien parallèles',against_C=False,against_H=True,confidence='high',crop='readers/scan029/R3/02_opening_and_interline.png')
f[31]['crop']='crops/scan029/main_arbre.png'
f[33].update(reading=r'\unsure{\deleted{\underline{\Gamma}}}\mathcal{X}^{\ast}',against_C=True,against_H=True,confidence='low',crop='readers/scan029/R3/11_pour_tte.png')
f[34]['crop']=f[35]['crop']='crops/scan029/main_nb_endpoint_clause.png'
f[36]['crop']='crops/scan029/main_autre_a_S.png'
f[22]['crop']=f[23]['crop']='readers/scan029/R1/crops/15_verb_gamma_correction.png'
f[42]['additional_crops']=['readers/scan029/R2/04_condition_margin.png']
f[42]['readers']={k:r'\inserted{(**) si s\in S ... inc. à s} attached after the cancelled continuation of faut exiger' for k in ['R1','R2','R3']}
f[42]['reader_source_ids']={'R1':'scan029-R1-f043 and reading.tex','R2':'reading.tex, inserted condition','R3':'reading.tex, inserted condition'}
extra=copy.deepcopy(rs[1]['findings'][43])
extra.update(id='SP41-029-044',readers={k:'No final period after s' for k in ['R1','R2','R3']},reader_source_ids={'R1':'reading.tex','R2':'scan029-R2-F044','R3':'reading.tex'},crop='readers/scan029/R2/04_condition_margin.png',marked_in_H='no',confidence='high',evidence='Main reader, R2 crop 04: the short clause ends at s with blank paper following; the distinct point after inc. is earlier in the line. No final period is supplied.',main_adjudication='All three complete readings compared; cited crop inspected.')
f.append(extra)
for i,txt in {14:'The relation after A-prime is retained as membership|inclusion, with the internal return stroke placing membership first.',31:'The opening reads bien parallèles; the closing non parallèles is also retained as written.',32:'The topological object is called arbre; H reads ensemble.',34:'The live NB object is script X-star, with a possible overwritten underlined Gamma retained explicitly; H gives underlined-Gamma through its bold encoding.'}.items():f[i-1]['consequential']=txt
# Literal complete text: only the explicitly adjudicated replacements below.
t=(w/'readers/scan029/R1/reading.tex').read_text()
t=t.replace(r'\unsure{exprime|exprimons|expriment}',r'\unsure{exprime|expriment|exprimons|exigeons}')
t=t.replace(r'\unsure{bien|non} parallèles','bien parallèles')
t=t.replace(r'\deleted{\unsure{A|\Gamma}}\mathcal{X}',r'\deleted{A}\mathcal{X}')
t=t.replace(r'tte arête de $\mathcal{X}^{\ast}$',r'tte arête de $\unsure{\deleted{\underline{\Gamma}}}\mathcal{X}^{\ast}$')
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[2]['inventory'])
for e in d['inventory']:
 if e['element'] in ['Replacement first-pair letter','Live replacement symbol in NB']:e['kind']='text'
 if e['element']=='Live replacement symbol in NB':e['first_words_or_objects']='script X with star, following uncertain overwritten Gamma'
 if e['element']=='Possible overwritten symbol in NB':e['first_words_or_objects']='possible cancelled underlined Gamma; state and identity uncertain'
d['inventory'].insert(20,{'element':'Possible cancelled s in article','kind':'deletion','position':'x442–529, y1774–1827','first_words_or_objects':'le with final s live|deleted','sheet_kind':'text','hand':'his hand','transcribed':'yes'})
d['unresolved']=[copy.deepcopy(u) for u in rs[0]['unresolved'] if u['place'] not in ['opening comparison','old letter beside first script X']]
for u in d['unresolved']:
 if u['place']=='upper-left verb':u['alternatives']=['expriment','exprimons','exigeons']
d['unresolved'].append({'place':'Older layer beneath NB script X-star','reading':r'\unsure{\deleted{\underline{\Gamma}}}\mathcal{X}^{\ast}','alternatives':['retracing belonging to the live X'],'confidence':'low','reason':'A thin left upright, upper return and lower horizontal lie beneath the heavier X; their identity and cancellation state remain uncertain.'})
d['notation']=copy.deepcopy(rs[0]['notation'])
d['notation'].append({'scan':29,'form':'Old layer beneath NB script X-star','evidence':'A thin left upright, upper return and low horizontal survive beneath the heavy crossed X.','reading':r'\unsure{\deleted{\underline{\Gamma}}}\mathcal{X}^{\ast}'})
d['abbreviations']=copy.deepcopy(rs[0]['abbreviations'])
d['notes']=[
 {'id':'scan029-note-01','text':'The opening says bien parallèles and qualifies the statement with “à cela près qu’il faut exiger”. A cancelled first formulation precedes the inserted condition (**), which continues into the left margin. The independent slanted note connects distinct a,b with distinct decomposition symbols. Its verb and label remain uncertain. The closing non parallèles drew attention to the opening bien; the crop supports retaining both written phrases.'},
 {'id':'scan029-note-02','text':'The construction paragraph introduces an arbre topologique represented by the pair (underlined Gamma,S). The small inserted label esp. top. points toward the underlined Gamma. It describes choosing a point on each edge and writes the barycentric-subdivision pair, with S amalg A-prime underbraced and labelled S-star. The cancelled original first letter is read A, followed in the transcription convention by its live replacement script X.'},
 {'id':'scan029-note-03','text':'After that pair the relation sign has an inner diagonal return, so membership precedes inclusion in the retained alternatives. The mathematical role of A-prime prompted the crop but did not remove that stroke. The following words are the abbreviation corr, biunivoque with an uncertain cancelled prefix, and donnée; H’s correspondance and canonique are not substituted.'},
 {'id':'scan029-note-04','text':'The bracketed NB states that the added vertices have degree 2 and gives the wording “une exactement des deux extrémités appartient à” A-prime, followed by “l’autre à” S. It calls this “une description complète”. The object after arête de is script X-star; a possible overwritten underlined Gamma is retained with its identity and cancellation state both uncertain. No truth claim about the characterization is certified here.'},
 {'id':'scan029-note-05','text':'The last paragraph describes the cut at a-prime, two connected components, their closures, a binary decomposition and its equator {a-prime}. The plural s of point is cancelled, a-prime is inserted above the line, and the ending after coupe and the high mark on Gamma are cancelled but partly obscured. The article’s final s remains live|cancelled; its state is not supplied from agreement with those neighbouring revisions.'},
 {'id':'scan029-note-06','text':'The final comparison retains uncertainty in the second prime count and in the abbreviated modifier before non parallèles. The main crop separates str and a raised crossed t; stric and strict with a raised t remain alternatives. The extra opening double quotes before équateur are preserved without a supplied closing pair. These are visual reading decisions, without proof or computation checks.'},
 {'id':'scan029-note-07','text':'The sheet has no observed title, date, authorial question mark or explicit instruction to verify a step. Its light pencil 28 is recorded as archive numbering. There is no drawing or arrow diagram. H’s note explicitly maps handwritten underlined Gamma to bold Gamma: that declared mapping is excluded from collation, while its final plain NB Gamma loses a visible underline and receives a row.'}
]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan029','type':'carried as background without fault found','outcome':'Source-account event only: three independent readings and local ink crops inspected. No independent proof, re-proof, computation or formal certificate was performed for the described mathematical claims.'} for n in d['notes']]
d['main_crop_views']={'R2':list(range(1,18)),'R1':[1,3,14,15,19],'R3':[2,4,8,11],'main_new':3,'total':29}
d['crop_counts']={'R1':19,'R2':17,'R3':15,'main':3,'total':54}
d['convention_mapping']='H explicitly encodes underlined Gamma as bold Gamma in its editorial note; those mapped occurrences are macro-only. Its unbold final NB occurrence remains a missing underline.'
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan029.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'scan':29,'findings':len(f),'C_doubt_ids':len({x for a in f for x in a['c_doubt_ids']}),'uncertainty_macros':t.count('\\unsure{'),'unresolved':len(d['unresolved']),'inventory':len(d['inventory'])}))
