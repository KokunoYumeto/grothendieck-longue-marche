"""Manual scan039 adjudication after all three full returns and 24 actual local views."""
from pathlib import Path
import copy,datetime,json
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan039/R{k}/return.json').read_text()) for k in (1,2,3)]
maps={1:list(range(1,51))+[None,None],
2:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,[21,41],22,22,23,24,23,25,26,27,28,29,30,31,32,33,35,36,34,34,34,39,None,38,42,43,45,44,None,40,47,37,46],
3:[1,2,4,5,8,9,10,11,15,17,18,19,20,21,[22,23],24,29,30,31,33,34,35,36,37,38,39,41,42,43,48,49,3,6,[7,27],12,14,16,13,25,50,28,None,26,47,46,51,45,44,32,40,None,None]}
assert all(len(x)==52 for x in maps.values())
obs={
1:'Both marks have an upper arch and three downward open ends directed toward the lower omega. The clockwise-rotated membership is resolved. H explicitly describes the same vertical layout.',
2:'The letter below x has two rounded low bowls with raised outer ends and a separate lower alpha. The corresponding beta occurrence repeats that shape. Omega is resolved.',
3:'Crossed diagonals and a dense adjoining zigzag obscure the older group after i.e. X remains tentative. H explicitly quotes the annotation but supplies no cancelled group.',
4:'The slanted word has tall t strokes and an accented ending, while its middle intersects the main-line Alors. Transitivité remains uncertain in agreement with all three readers.',
5:'The arrow label has a small right loop, an open left return and a long central stem. R2/R3’s varphi/phi uncertainty is retained against R1’s resolution.',
6:'The capital has a downstem, broad upper bar, sloped right bowl and lower return hook. The font remains uncertain. Its component correspondence with earlier sampled capitals is recorded in the ongoing notation audit.',
7:'The suffix has a long looped f, shallow joined medial shoulders, one late high dot or accent and a short terminal hook. Finies remains first with fermés, fermé and foncier retained; the compressed sequence does not settle the alternatives. R2’s fermé-first reading is explicitly recorded. No property of the map determines this choice.',
8:'Two tall l loops lead into a long low terminal stroke with a downward hook. Elles remains first, with elle retained. The separately written singular soit is preserved.',
9:'The word has p descent, low ana/c, a tall h and a final accented e. The following short low mark is detached. Panaché and the period are adopted with all three readers; both witnesses contain the period.',
10:'The angular initial I, looped d and deep p are visible, but the medial sequence is very flat and compressed. R3’s uncertainty on Indépendamment is retained against R1/R2’s resolution. The p tip reaches the selected crop edge.',
11:'Low initial bodies lead to a long q descender and two tall t strokes. The compact first vowel remains dark, leaving maquette/moquette open.',
12:'Extra looped material and a tall d-like stroke merge with the beginning of live ordonnée. R2/R3’s outer uncertainty is retained for both the older de identity and its overwritten state. H acknowledges rewriting but supplies no earlier letters.',
13:'After the rewritten opening, the d, low paired n bodies and accented final ee sequence are legible. Live ordonnée is resolved.',
14:'The retraced initial d/é, low com, p descender, crossed t and ending ions can be followed in the complete word. Décompositions is resolved; no additional old word is supplied.',
15:'A separate horizontal stands between the low first glyph and aires, resolving C’s hyphen doubt. The first glyph has one shallow shoulder and elongated return, leaving n/nu open as R1/R3 record.',
16:'The older o/r bodies, distinct d upright, low n shoulders and final accent survive a long separate cancellation below fini. Ordonné is resolved with R2/R3 against R1’s retained doubt.',
17:'The noun’s crossed t and small high accent are visible, but its low ending does not separate a final s. Propriété remains first, with propriétés retained. The already viewed R2 crop includes the p descender clipped by R1/R3.',
18:'The final crossed t runs into a short hooked ending before a separate colon. The ending leaves suivante/suivantes open, independently of the article la.',
19:'A low loop and right curve remain beneath broad zigzag cancellation. The first a) starter stays uncertain.',
20:'The sigma-x group, comparison bars and y descent intersect the long cancellation. The relation’s oblique crossing remains inseparable from that cancellation. Both proposed relations remain recorded.',
21:'Non is visible before the short congrus-shaped group. One g descent and low terminal strokes survive the cancellation, but some medial strokes merge with it. R3’s retained congrus uncertainty is adopted against R1/R2’s resolution. H’s omitted non and doubtful conjugués are both recorded here.',
22:'The third line has non followed by c/o/n-like bodies, a long g descent and low ending strokes. The cancellation still joins several bodies. R3’s retained congrus uncertainty is adopted.',
23:'Low m/o and a tall d are followed by a large open capital C and a detached comma. Mod C, is resolved. The separate marginal mod sigma is preserved at its own location.',
24:'An upright, rounded body and neighbouring curve are crossed by several thick strokes. The first older b) remains uncertain. H’s general numbering note supplies no reading for this starter.',
25:'A low e loop and tall crossed t remain separately traceable under the oblique cancellation. Et is resolved with R2/R3 against R1’s retained doubt.',
26:'The second older starter has an upright, a lower loop and a curved right edge, all joined by later crossings. R2/R3’s b) uncertainty is retained against R1’s resolution.',
27:'The slanted word ends after a short r-like return with a detached point. Compar. is resolved; the longer ending printed by H is absent.',
28:'The low beginning, g-like descent and compressed terminal strokes are heavily retraced where the nearby number crosses them. R2/R3’s congrus uncertainty is retained against R1’s resolution.',
29:'The black cancelled group preserves a left crossing, short middle bars and a right descending terminal under dense hatching. The tentative formula x ne y is retained with uncertainty.',
30:'A 2-like curve and two-lobed 8 remain under intersecting marginal letters. R1/R3’s uncertainty on 28 is retained against R2’s resolution. The complete surviving label is visible in the lower-margin crop, beyond the clipped left part of the numbering crop.',
31:'The final verb has a densely rewritten initial group, tall middle loop and long q descent. Indique/implique remains open. Its low descender reaches the photographed boundary.',
32:'One cap spans two descending legs. Pi remains first with pi retained at the first occurrence; later corresponding forms follow Pi. This assigns no mathematical identity.',
33:'C’est is readable before the last slanted line. That line has the initial i, low repeated m-like strokes, a looped d and terminal t, but the last group intersects main-line sans. R3’s uncertainty on immédiat is retained against R1/R2’s resolution.',
34:'Both point abbreviations have a long p and a smaller crossed t raised to its upper right. The first is confirmed by a new local crop; the second was already visible in R1’s sigma/point crop. Both are preserved as p with raised t.',
35:'The connector has a tiny initial body, short angled middle and open terminal return. The compressed ink leaves avec/sur open. Avec is first on the small body and angled middle, while R3’s sur is retained; the three readings and witnesses remain explicitly distinguishable in the record.',
36:'Il ends the preceding line; the next begins with one long f, separate et and short s with a low point before que. The written abbreviation il f et s. is preserved.',
37:'The inspected strictement line and the separate non panaché crop show no independent underline under this qualification. H’s emphasis is removed; the word difference is recorded separately.',
38:'The low ens ending is followed by open space before ordonnés. There is no detached abbreviation point.',
39:'Un ens consists of two low groups followed by blank separation before the cancelled ordonné. No detached point appears after ens.',
40:'The final ens ending is followed by blank space before ordonné. The last C is visible above the photographed bottom band. No abbreviation point is supplied.',
41:'The article has one tall looped l and one low a body, with no separate final s. La is preserved independently of the next-line ending uncertainties.',
42:'Two detached dark points stand after la, one above and slightly right of the other. Both are inside R1’s existing sigma/point crop, which was displayed again specifically for this newly identified punctuation. The colon after suivante is also retained; C, H, R2 and R3 omit the earlier colon.',
43:'A small raised arch/loop stands above a long curved diagonal leader entering the gap after involution. The placement is clear; R3’s uncertainty on the small sigma-shaped glyph is retained against R1/R2’s plain sigma.',
44:'The cancelled comparables, et sigma y<sigma x line belongs beneath the a) continuation. Non comparables is raised above it. The long strike begins near b) and crosses the older upper line while leaving the lower live implication intact. All three readings agree; H’s explicit editorial note already records this placement.',
45:'A low e loop and tall crossed t immediately precede sigma y in the cancelled continuation. Et is legible; H’s doubtful donc is replaced.',
46:'Both live branches begin with a tall looped S and separately dotted i. Capital Si is preserved in both positions.',
47:'Three connected low s-shaped turns precede sigma x,y. The last has its own return and no separate i dot. Sss is preserved.',
48:'A left curved brace/leader joins raised x,y comparables above the cancelled sigma-x,y / x,sigma-y pair. R3’s vertical group with its visible left brace is adopted. C supplies the insertion but omits the brace; H supplies the brace but does not explicitly mark this upper group as inserted. Its separate replacement note concerns non comparables.',
49:'The first cancelled trial ends at y, followed by open space and the continuation of the cancellation. No three-dot group is present. H’s ellipsis is omitted.',
50:'The lower slanted note has the low initial group, tall l loop, q descent and low ue of implique before a separate que. Implique is legible in the rotated crop.',
51:'A detached short comma-like hook lies above and to the left of the inserted f, separate from the later high marks of fini. R2’s uncertain apostrophe-like mark is preserved; its function stays open. C, H, R1 and R3 omit this trace.',
52:'The inserted non comparables ends in a low s return and blank space. The detached comma belongs to the cancelled line below, after comparables. H’s comma after the live replacement is omitted.'
}
R1=lambda name:'readers/scan039/R1/crops/'+name+'.png'
R2=lambda name:'readers/scan039/R2/crops/'+name+'.png'
R3=lambda name:'readers/scan039/R3/crops/'+name+'.png'
cr={1:'crops/scan039/main_memberships.png',2:'crops/scan039/main_memberships.png',3:R2('01_rhs_annotation'),4:R1('02_upper_margin'),5:R2('03_map'),6:R2('03_map'),7:R2('03_map'),8:R1('04_elles'),9:R2('05_panache'),10:R3('05_panache_independamment'),11:R1('07_defined_term'),12:R1('07_defined_term'),13:R1('07_defined_term'),14:R2('07_decompositions'),15:R2('07_decompositions'),16:R2('08_fini'),17:R2('10_property'),18:R2('10_property'),19:R2('11_numbering'),20:R2('12_cancelled_trials'),21:R2('12_cancelled_trials'),22:R2('12_cancelled_trials'),23:R2('12_cancelled_trials'),24:R2('11_numbering'),25:R2('11_numbering'),26:R2('11_numbering'),27:R2('13_lower_margin'),28:R2('13_lower_margin'),29:R1('12_live_conditions'),30:R2('13_lower_margin'),31:R1('15_last_nb'),32:R2('01_rhs_annotation'),33:R1('02_upper_margin'),34:'crops/scan039/main_first_pt.png',35:R1('05_avec'),36:'crops/scan039/main_abbreviations_emphasis.png',37:'crops/scan039/main_abbreviations_emphasis.png',38:'crops/scan039/main_abbreviations_emphasis.png',39:R1('08_decompositions_fini'),40:R1('15_last_nb'),41:R1('10_propriete'),42:R1('09_sigma_pt'),43:R1('09_sigma_pt'),44:R1('12_live_conditions'),45:R1('12_live_conditions'),46:R1('12_live_conditions'),47:R1('12_live_conditions'),48:R2('14_live_clauses'),49:R2('12_cancelled_trials'),50:R2('13_lower_margin'),51:R2('08_fini'),52:R2('14_live_clauses')}
base=copy.deepcopy(rs[0]['findings'])+[copy.deepcopy(rs[1]['findings'][36]),copy.deepcopy(rs[1]['findings'][45])]
overrides={
5:dict(reading=r'\unsure{\varphi|\phi}',against_C=False,c_doubt_status='retained'),
7:dict(reading=r'\unsure{\text{finies}|\text{fermés}|\text{fermé}|\text{foncier}}'),
10:dict(reading=r'\unsure{Indépendamment}',against_C=False,c_doubt_status='retained',confidence='medium'),
12:dict(reading=r'\unsure{\deleted{de}}',against_C=True),
16:dict(reading=r'\deleted{ordonné}',against_C=True,c_doubt_status='resolved',confidence='high'),
21:dict(reading=r'non \unsure{congrus} sous $\sigma$',against_C=False,c_doubt_status='retained'),
22:dict(reading=r'non \unsure{congrus}',against_C=False,c_doubt_status='retained'),
25:dict(reading=r'\deleted{et}',against_C=True,c_doubt_status='resolved',confidence='high'),
26:dict(reading=r'\deleted{\unsure{b)}}',against_C=False,c_doubt_status='retained',confidence='low'),
28:dict(reading=r'\unsure{congrus}',against_C=False,c_doubt_status='retained'),
33:dict(reading=r"c'est \unsure{immédiat}",against_C=True),
35:dict(reading=r'\unsure{avec|sur} son image',against_C=True,confidence='low'),
43:dict(reading=r'\inserted{$\unsure{\sigma}$}',against_C=True),
44:dict(reading=rs[2]['findings'][46]['reading']),
46:dict(kind='other'),
48:dict(reading=rs[2]['findings'][43]['reading'],against_C=True,against_H=True),
51:dict(reading=r"\inserted{\unsure{'}fini}")
}
fallback={(1,51):'No detached mark before fini in reading.tex',(3,51):'No detached mark before fini in reading.tex',(1,52):'non comparables, without a following comma in reading.tex',(3,52):'non comparables, without a following comma in reading.tex',(2,42):'No colon after la in reading.tex',(3,42):'No colon after la in reading.tex',(2,48):r'\deleted{\sigma x,y\text{ et }x,\sigma y}\ \inserted{x,y\text{ comparables}}; no inner brace in reading.tex'}
d={'scan':39,'folder':'J81-05','their_page':38,'hua_has':'text','filename':'J81-05_81_scan039.tex','status':'decided','findings':[]}
for i,f in enumerate(base,1):
 f.update(overrides.get(i,{}));f['id']=f'SP41-039-{i:03d}'
 f['marked_in_H']='yes' if f['marked_in_H'] is True or f['marked_in_H']=='yes' else 'no'
 f['crop']=cr[i];f['evidence']='Main reader, personally viewed local crop: '+obs[i];f['main_adjudication']=obs[i]
 f['readers']={};f['reader_source_ids']={}
 for k in (1,2,3):
  sel=maps[k][i-1]
  if sel is None:
   f['readers'][f'R{k}']=fallback[k,i];f['reader_source_ids'][f'R{k}']=['reading.tex at this locus']
  else:
   sel=sel if isinstance(sel,list) else [sel];ff=[rs[k-1]['findings'][a-1] for a in sel]
   f['readers'][f'R{k}']=' ; '.join(a['reading'] for a in ff);f['reader_source_ids'][f'R{k}']=[a['id'] for a in ff]
 if i==34:f['additional_main_crops']=[R1('09_sigma_pt')]
 if i==37:f['additional_main_crops']=[R2('05_panache')]
 if i==48:f['additional_main_crops']=[R2('12_cancelled_trials'),R1('12_live_conditions')]
 if i==9:f['consequential']='The written qualification is strictement non panaché; H prints strictement non parallèle. The transcription preserves the observed h and accented ending.'
 if i==44:f['consequential']='The cancelled comparables, et sigma y<sigma x continuation is restored beneath a), with non comparables as its interlinear replacement; the live b) implication remains below the strike.'
 d['findings'].append(f)
coverage={}
for k in (1,2,3):
 used={v for f in d['findings'] for v in f['reader_source_ids'][f'R{k}'] if v.startswith('scan039-')};expected={f['id'] for f in rs[k-1]['findings']}
 assert used==expected,(k,expected-used,used-expected)
 coverage[f'R{k}']={'raw_findings':len(expected),'mapped_findings':len(used),'all_mapped':True}
d['reader_finding_coverage']=coverage
tex=(w/'readers/scan039/R3/reading.tex').read_text()
replacements={r'de $C$ sur son image':r'de $C$ \unsure{avec|sur} son image',r'\inserted{fini}':r"\inserted{\unsure{'}fini}",r'ayant la \unsure{propriété|propriétés}':r'ayant la : \unsure{propriété|propriétés}'}
for a,b in replacements.items():
 assert tex.count(a)==1,(a,tex.count(a));tex=tex.replace(a,b)
assert r'\clearpage' not in tex
tex+='\n\\clearpage\n'
d['inventory']=copy.deepcopy(rs[2]['inventory'])
for e in d['inventory']:
 e['position']={'description':e['position'],'bbox':e['bbox']}
 if e['element']=='scan039-inv-13':e['first_words_or_objects']='fini preceded by an uncertain detached apostrophe-like hook'
 if e['element']=='scan039-inv-10':e['first_words_or_objects']='On appelle maquette ordonnée ... ayant la : propriété suivante :'
u=copy.deepcopy(rs[2]['unresolved'])
u += [{'place':'Connector before son image','reading':'avec','alternatives':['sur'],'confidence':'low','reason':obs[35]},{'place':'Before inserted fini','reading':"'",'alternatives':['unassigned detached ink mark'],'confidence':'low','reason':obs[51]}]
assert tex.count(r'\unsure{')==len(u),(tex.count(r'\unsure{'),len(u))
d['unresolved']=u
d['notation']=[{'scan':39,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [1,2,5,6,7,12,15,32,34,35,42,43,47,48,51]]
d['abbreviations']=copy.deepcopy(rs[0]['abbreviations'])
notes=[
'The handwritten working sheet has displays (26), (27), and uncertain (28), two slanted marginal notes, an underlined Définition and a final underlined NB. Pencil archive number 38 is retained only as a comment. No authorial date or separate manuscript page number was observed.',
'Display (26) carries vertically written memberships beneath x and y. The opening membership direction and omega are resolved. The indexed comparison has Pi/pi uncertainty at its first occurrence and an underbrace to an added i.e. intersection annotation. The old cancelled x-like group remains uncertain. H’s explicit account of the vertical layout and annotation is credited in the collation.',
'The upper margin says “il faut vérifier la transitivité de cette relation -- c’est immédiat”, with transitivité and immédiat uncertain where slanted and main-line strokes intersect. This records the author’s check request and own response; no proof of transitivity was performed in this reading.',
'The opening prose calls sigma an antiautomorphism and writes involutif sans p with raised t fixe. Display (27) gives its map and element assignment. The arrow letter, P font and compressed target suffix remain uncertain. Finies is first with fermés, fermé and foncier retained. No mathematical property of the target resolves that suffix.',
'The paragraph after (27) keeps elles/elle before the separately written soit, d’ens without a point, avec/sur son image, and il f et s. The final qualification is plain strictement non panaché. The h and accented ending support panaché; H’s parallèle and emphasis are changed. This is an ink decision, without an independent verification of the stated criterion.',
'Indépendamment remains uncertain. The definition contains maquette/moquette ordonnée, possible older de with uncertainty on identity and state, décompositions n/nu-aires, and cancelled ordonné replaced by fini. A small detached mark before fini remains uncertain. The raised sigma-like mark and its leader are preserved. The source writes la followed by an additional colon before the next-line propriété/propriétés suivante/suivantes and its colon. The article does not settle the ending uncertainties.',
'Two discarded formulations occupy three cancelled lines. Their old labels and sigma-x comparison remain uncertain. Both congrus occurrences retain doubt, and the last line reads mod C, with a capital C and comma. The separate lower margin reads NB implique que x,y compar. implies x,y non congrus mod sigma, with congrus uncertain. Both written terminal symbols remain at their own locations.',
'The live a)/b) display retains its left brace. Raised x,y comparables and the cancelled pair below have their own curved left brace/attachment. The written abbreviation is sss. The crossed comparables, et sigma y<sigma x continuation belongs to a), with non comparables inserted above. The strike rising from b) leaves its final implication live. H’s explicit editorial note supports this already transcribed placement, while its connective donc and comma after the upper replacement differ from the ink.',
'The final NB keeps indique/implique, ens without a point and the final C. Its lowest descender portions meet the photographed lower boundary. No missing continuation or terminal point is supplied.',
'All three complete readings and every detailed return field were read. All 50/47/51 raw findings are mapped. Ten C doubts are resolved and twenty-one retained; the final text has twenty-seven uncertainty loci. Root made three local crops and inspected twenty-three distinct local crops, with one additional display of an existing crop for the newly identified colon: twenty-four actual views, no whole image or half. No OCR, outside research or compilation was used.'
]
d['notes']=[{'id':f'scan039-note-{i:02d}','text':x} for i,x in enumerate(notes,1)]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan039','type':'carried as background without fault found','outcome':'Source-account and ink/witness comparison only; no independent mathematical verification claimed.'} for n in d['notes']]
d['sweep']=[]
d['crop_counts']={'R1':15,'R2':15,'R3':14,'main':3,'total':47}
d['main_crop_views']={'R1':[2,4,5,7,8,9,10,12,15],'R2':[1,3,5,7,8,10,11,12,13,14],'R3':[5],'main_new':3,'distinct_total':23,'additional_existing_view':{'crop':R1('09_sigma_pt'),'reason':'New colon target at the lower-right edge; no new crop'},'total':24}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
obsfile=w/'decisions/drafts/scan039_actual_crop_observations.json';o=json.loads(obsfile.read_text())
more=[('crops/scan039/main_memberships.png',obs[1]+' '+obs[2]),('crops/scan039/main_first_pt.png',obs[34]),('crops/scan039/main_abbreviations_emphasis.png',obs[36]+' '+obs[37]+' '+obs[38]),(R1('09_sigma_pt'),obs[42]),(R1('08_decompositions_fini'),obs[39]),(R2('14_live_clauses'),obs[52])]
assert len(o['actual_views'])==18
for crop,ob in more:o['actual_views'].append({'crop':crop,'observation':ob})
o.update(status='Decided after all complete texts and all detailed return fields were read.',count=24,main_new_crops=3,distinct_local_crops_viewed=23,complete_text_review={f'R{k}':'Complete reading.tex and every detailed return field personally read.' for k in (1,2,3)},final_findings='decisions/scan039.json')
o['corrections_to_preliminary_observations']=[obs[9],obs[16],obs[25],obs[42],obs[48],obs[51]]
obsfile.write_text(json.dumps(o,ensure_ascii=False,indent=2))
record='# Scan039 main-reader local observations\n\nAll three complete texts and every detailed return field were read. Twenty-three distinct local crops were viewed, with one repeat display for the newly identified colon; no whole image or half was viewed by root.\n\n'
record+='\n\n'.join(f'{i}. {obs[i]}\n\n   Crop: `{cr[i]}`' for i in range(1,53))
record+='\n\nR1/R3 property crops clip the initial p descent; the already viewed R2 property crop contains that target. The lower-revision crops clip portions of the raised x,y comparables line; its lettering is present in the already viewed cancelled-trials crop, and its brace and replacement relation in the lower-revision crops. The source bottom itself cuts final descenders. These limitations are recorded without supplying unseen ink. R2’s long rest return was initially truncated in the display; the omitted unresolved and C-coverage fields were then printed separately and fully read.\n'
(w/'decisions/scan039_main_observations.md').write_text(record)
(w/'pages'/d['filename']).write_text(tex)
(w/'decisions/scan039.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'findings':len(d['findings']),'against_C':sum(f['against_C'] for f in d['findings']),'against_H':sum(f['against_H'] for f in d['findings']),'unresolved':len(u),'coverage':coverage}))
