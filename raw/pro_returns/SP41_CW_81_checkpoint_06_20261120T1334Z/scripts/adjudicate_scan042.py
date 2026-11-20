"""Manual scan042 decisions; no image recognition or automatic reading choice."""
from pathlib import Path
import copy,datetime,json
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan042/R{k}/return.json').read_text()) for k in (1,2,3)]
base=copy.deepcopy(rs[1]['findings'])
base += [copy.deepcopy(rs[0]['findings'][30]),copy.deepcopy(rs[0]['findings'][38]),copy.deepcopy(rs[2]['findings'][3]),copy.deepcopy(rs[2]['findings'][43]),copy.deepcopy(rs[1]['findings'][43])]
maps={
1:list(range(1,28))+[30,None,32,33,49,35,36,37,38,40,43,44,41,42,45,46,28,47,48,None,None,31,39,None,None,29],
2:list(range(1,49))+[None,35,None,None,44],
3:[1,5,6,8,9,10,11,12,15,17,20,22,24,29,30,31,32,33,34,36,37,38,39,40,47,2,3,7,None,13,14,16,18,19,20,23,25,26,28,27,28,35,41,42,45,46,43,None,None,21,4,44,42]}
assert len(base)==53 and all(len(a)==53 for a in maps.values())
obs={
1:'The low speck before N has a dark centre within amber staining. Its comma function remains uncertain; no reading is supplied from the syntax.',
2:'Bi-, the circular beginning and long l are visible. A compressed group before the late tall t leaves circularisation/circulation open. The first reading remains the longer visible sequence.',
3:'The small numeral has an upper curl, long right-side descent and lower return. The missing separated middle turn leaves 3/2 open.',
4:'A thick independent underline lies below the crossed short heading. The first tall triangular shape favors A, followed by crossing strokes; Ax, Ax. and Déf. remain alternatives.',
5:'Low looped letters before segment lie beneath several cancelling horizontals. Ens remains an uncertain old word.',
6:'Several looped humps remain under the opening cancellation. Non/on remains open.',
7:'A dotted i and left-pointing wedge precede N beneath a separate long cancelling line. The wedge is preserved as less-than; the cancellation does not supply the two bars of H’s unequal sign.',
8:'Dotted i and membership e survive cancellation. Extra left strokes at N meet that cancellation, so double-stroke N/plain N remains open. The detached following comma is live, outside the strike.',
9:'The base below i-1 has two rounded hollows and a high middle join. W remains first, with u retained; the adjacent iterate formulas do not repair it.',
10:'The p descent, low joined letters, hyphen and tall t survive, but the tiny accent and compressed internal bodies leave the compound uncertain. R2’s resolution is not adopted.',
11:'The rotated heading has a P, joined low ro, a p descent and a short further turn before its point. Propr. is first with Prop. retained. A separate underline is clear and is missing from H’s heading.',
12:'A large initial S is visible beneath the cancellation. The crowded ending leaves Soit/Soient open; H’s lowercase initial is changed.',
13:'The lower slanted line retains an opening s/e group, long g-like descent and crossed terminal strokes. Segments remains uncertain, followed by a comma.',
14:'The long p descent and compressed connector group favor pris ds un contexte, while ds and the final noun remain crowded. Preserve full alternatives pris ds un contre-ex. and qui se rencontrent without supplying a mathematical phrase.',
15:'A detached lower curved comma stands before et. Its presence is resolved.',
16:'There is one high tick after the first T and two after the second T. Cup, crossed two-bar relation and S remain visible to the physical source edge. Preserve T-prime union T-double-prime unequal S.',
17:'The rotated abbreviation shows dotted i, an intervening point and e. The final return does not securely separate a terminal point. Keep i.e first and i.e. as an alternative against R2’s resolved final point.',
18:'The old word has initial r-like rise, high accent, joined low bowls and later high dot. The heavy line through it may cancel or reinforce the word. Identity and state remain jointly uncertain.',
19:'Two short parallel bars are traversed by a longer stroke, followed by a separate large S. The margin writes unequal S.',
20:'The opening d/i group and final tes are visible. Faint compressed middle strokes leave distinctes uncertain with R3, despite the other readers’ resolution.',
21:'A separate dark point lies in the wide gap after une before orientation. Its presence is resolved independently of grammatical function. The terminal point after orientation also survives.',
22:'The final dotted i is followed by white space and a detached comma. No further e body is visible. Read choisi.',
23:'Two numeral uprights are connected by a dark central trace. That trace does not isolate a hyphen securely. Keep 1-1/11.',
24:'A separate straight left upright stands beside the N diagonal and right rise below the interval. Read double-stroke N.',
25:'An open c and short return lead to a long looped l with a plain tail. Cel is first; a separate final a remains uncertain, and ceci lacks support from the tall l.',
26:'The complete Cardinal N group sits above the line with its curved placement leader. Large initial C is visible. No de stands in the group. H’s partial insertion and extra de are changed.',
27:'The opening ens ends in a connected low terminal stroke before fini, with no separate abbreviation point.',
28:'Card begins with a large open C beside the shorter low ar/d letters. Preserve capital C.',
29:'The first condition-b letter has an upper return, dark inward middle turn and lower loop. S/E remains uncertain; later s-zero occurrences supply no replacement stroke.',
30:'The parenthesis begins with a d loop and low onc-like continuation. Donc is confirmed.',
31:'On is followed by a spread a/u/r/a-like group before aussi. Aura is preserved against H’s a.',
32:'Two detached vertically separated marks follow réduites: a high short oval and a low dark point. Read a colon. The later non réduit separator has a joined body and remains à.',
33:'A faint round speck lies well to the right of the compound at baseline height. Its authorship/punctuation status remains uncertain. The R1 word crop ends before this speck; the wider R2 punctuation crop includes it.',
34:'The sloping strokes before les continue into the already represented cancelled left note. The local gap contains no independently isolated old word. H’s extra struck illegibility is not added.',
35:'Long cancelling loops traverse both lines of the slanted marginal statement. The complete note remains cancelled, with the older wording represented in its written order.',
36:'Two triangular A bodies, a high tick after the second, and the following deux are visible. A small low separator between the A bodies remains uncertain with R1. H’s partial A and illegibility are replaced by the fuller visible group.',
37:'The three abbreviations have returning s-like terminal strokes. The first has the least separated last hook and retains sss/ssi; the intersection and endpoint occurrences read sss. No independent final i dot is visible.',
38:'Both small intersection and union clauses occupy the gap between the larger complement and endpoint sentences, with attachment curves. Their whole-clause insertion state is preserved; H represents only their nested additions.',
39:'A left downward curve and a right raised curl frame the predicate. Their independent parenthesis role remains open because they meet the attachment rules. Both are retained with uncertainty.',
40:'The horizontal at the start is the capital I foot. No separate rule extends beneath the remaining letters of Intersection. Preserve the word without whole-word underline.',
41:'Two parallel source rules lie below contenus dans un segment. Their role remains open: double emphasis, one emphasis rule plus leader, or attachment rules. For the first representation, source upper rule maps to upper uuline rule and source lower rule to lower uuline rule; the inverse returns each displayed rule to the same source rule. Both other roles are explicit alternatives.',
42:'The gap between segment and s-zero contains no pair of punctuation points. The lower comma belongs between s-zero and t-zero; H’s colon is omitted.',
43:'A detached curved comma lies below-right of the large S before et in the NB. Preserve it.',
44:'The first NB ens ends in a connected low terminal stroke before des. No detached abbreviation point is present.',
45:'The first live S in deux segments de S-prime has a separate high upright tick. Preserve that prime along with the later S-prime; the earlier cancelled de S does not replace it.',
46:'Between contenus and S-prime, a tall looped d joins a short s-like return. Preserve ds without expanding it.',
47:'Three ellipsis marks precede the final u. There is no additional descending comma between the last ellipsis mark and u.',
48:'Two small separated dark marks lie below the final u, the right one higher. The source lower-left mark maps to the left baseline dot and upper-right mark to the raised right dot; the inverse maps each rendered dot back to its source position. Attribution and function remain uncertain; no mathematical meaning is assigned.',
49:'After the opening sentence’s definite full stop, a separate short low hooked mark survives. Preserve its uncertain comma-like shape.',
50:'After the marginal heading’s point, the next word begins with a large S. Broad intervening strokes belong to cancellation. No separate colon, extra word or comma is visible there.',
51:'The final l of polygonale/polygonal bends into the photographed right border, with a small low trace. The border does not settle a distinct final e. Preserve the ending uncertainty.',
52:'A narrow inner upright and upper bowl survive alongside the live initial S of Soit. An older P/S and reinforced S remain possible. Retain explicit uncertainty over the older glyph and its overwritten state.',
53:'The second NB ens before the display has a connected low ending followed by white space. No detached abbreviation point is present.'}
r1=lambda s:'readers/scan042/R1/'+s+'.png'
r2=lambda s:'readers/scan042/R2/crops/'+s+'.png'
r3=lambda s:'readers/scan042/R3/crops/'+s+'.png'
cr={1:r1('01_cardinal_insertion'),2:r1('02_bicircularisation'),3:r1('03_card_geq'),4:r1('04_cancelled_heading'),5:r1('05_cancelled_ens'),6:r1('06_condition_a'),7:r1('06_condition_a'),8:r1('07_condition_b'),9:r1('08_reversal_parenthesis'),10:r1('10_parties_aretes'),11:r1('11_cancelled_left_margin'),12:r1('11_cancelled_left_margin'),13:r1('11_cancelled_left_margin'),14:r1('12_dense_inserted_band'),15:r1('12_dense_inserted_band'),16:r1('12_dense_inserted_band'),17:r1('13_right_margin'),18:r1('13_right_margin'),19:r1('13_right_margin'),20:r2('06_middle_additions'),21:'crops/scan042/main_origine.png',22:r1('14_choisi'),23:r1('15_correlation_numerals'),24:r3('17_display'),25:r1('16_final_cel'),26:r1('01_cardinal_insertion'),27:r2('01_opening'),28:r1('03_card_geq'),29:r2('02_definition_cancellations'),30:r1('08_reversal_parenthesis'),31:r1('08_reversal_parenthesis'),32:r1('09_reduites_separator'),33:r2('12_second_example_punctuation'),34:'crops/scan042/main_examples_gap.png',35:r1('11_cancelled_left_margin'),36:r1('11_cancelled_left_margin'),37:r1('18_complement_ssi'),38:r2('06_middle_additions'),39:r2('06_middle_additions'),40:r2('06_middle_additions'),41:r2('06_middle_additions'),42:r2('06_middle_additions'),43:'crops/scan042/main_nb_ens.png',44:'crops/scan042/main_nb_ens.png',45:r2('10_final_S_prime_ds'),46:r2('10_final_S_prime_ds'),47:r2('13_display_punctuation'),48:r2('13_display_punctuation'),49:r1('03_card_geq'),50:r1('11_cancelled_left_margin'),51:r3('20_polygonale_edge'),52:r3('18_soit'),53:'crops/scan042/main_nb_ens.png'}
overrides={
2:dict(reading=r'\unsure{bi-circularisation|bi-circulation}',against_C=True),
8:dict(reading=r'\deleted{$i\in\unsure{\mathbb N|N}$},',c_doubt_status='retained'),
10:dict(reading=r'\unsure{parties-arêtes}',against_C=False,c_doubt_status='retained',confidence='medium'),
11:dict(against_H=True),
14:dict(reading=r'\unsure{pris ds un contexte|pris ds un contre-ex.|qui se rencontrent}'),
17:dict(reading=r'\unsure{i.e|i.e.}',against_C=True,against_H=True,c_doubt_status='retained',confidence='medium',kind='other'),
20:dict(reading=r'\unsure{distinctes}',against_C=False,c_doubt_status='retained'),
33:dict(reading=r'les \unsure{parties-arêtes}\unsure{.}'),
35:dict(reading=r"\margin{\deleted{\uline{\unsure{Propr.|Prop.}} \unsure{Soit|Soient} $A\unsure{,}A'$ deux \unsure{segments},}}"),
36:dict(reading=r"$A\unsure{,}A'$ deux",against_C=True,confidence='low'),
38:dict(reading='Both complete middle clauses are inserted, including the separately raised restriction and union conclusion.'),
39:dict(reading=r'\unsure{(}en est un sss il est $\ne\varnothing$\unsure{)}'),
41:dict(reading=r'\inserted{\unsure{\uuline{contenus dans un segment}|\uline{contenus dans un segment}|contenus dans un segment}}'),
44:dict(place='NB, first ens abbreviation point',c="l'ens des segments",h=r"l'ens.\ des segments",reading="l'ens des segments",bbox=[249,1503,449,1614]),
48:dict(reading=r'\underset{\unsure{\cdot\!{}^{\cdot}}}{u}^{i-1}'),
53:dict(place='NB, second ens abbreviation point',c="et l'ens",h="et l'ens.\\",reading="et l'ens",bbox=[1288,1484,1483,1556])}
fallback={
(1,29):r's_0, unmarked in complete reading.tex',
(3,29):r's_0, unmarked in complete reading.tex',
(1,47):r'\ldots u^{i-1}s_0, without extra comma in complete reading.tex',
(1,48):'No detached low marks in complete reading.tex',
(3,48):'No detached low marks in complete reading.tex',
(2,49):'Opening ends with full stop only in complete reading.tex',
(3,49):'Opening ends with full stop only in complete reading.tex',
(1,51):'polygonale, unmarked in complete reading.tex',
(2,51):'polygonale, unmarked in complete reading.tex',
(1,52):'Soit without older capital layer in complete reading.tex',
(2,52):'Soit without older capital layer in complete reading.tex'}
d={'scan':42,'folder':'J81-06','their_page':41,'hua_has':'text','filename':'J81-06_81_scan042.tex','status':'decided','findings':[]}
for i,f in enumerate(base,1):
 f.update(overrides.get(i,{}));f['id']=f'SP41-042-{i:03d}'
 f['marked_in_H']='yes' if f['marked_in_H'] in (True,'yes') else 'no'
 f['crop']=cr[i];f['evidence']='Main reader, personally viewed local crop: '+obs[i];f['main_adjudication']=obs[i]
 f['readers']={};f['reader_source_ids']={}
 for k in (1,2,3):
  j=maps[k][i-1]
  if j is None:f['readers'][f'R{k}']=fallback[k,i];f['reader_source_ids'][f'R{k}']=['reading.tex at this locus']
  else:
   q=rs[k-1]['findings'][j-1];f['readers'][f'R{k}']=q['reading'];f['reader_source_ids'][f'R{k}']=[q['id']]
 if i==8:
  f['reader_source_ids']['R1'].append(rs[0]['findings'][33]['id'])
  f['readers']['R1']+='; '+rs[0]['findings'][33]['reading']
 if i==37:f['additional_main_crops']=[r3('14_endpoints_ssi'),r2('06_middle_additions')]
 if i==32:f['additional_main_crops']=[r1('17_reduit_separator')]
 if i in (9,16,45):f['consequential']='Visible symbol/prime retained independently of the expected mathematical statement; no emendation supplied.'
 d['findings'].append(f)
d['reader_finding_coverage']={}
for k in (1,2,3):
 used={a for f in d['findings'] for a in f['reader_source_ids'][f'R{k}'] if a.startswith('scan042-')};expected={f['id'] for f in rs[k-1]['findings']}
 assert used==expected,(k,expected-used)
 d['reader_finding_coverage'][f'R{k}']={'raw_findings':len(expected),'mapped_findings':len(used),'all_mapped':True}
tex=(w/'decisions/drafts/scan042_proposed_text.tex').read_text()
d['inventory']=copy.deepcopy(rs[1]['inventory'])+[copy.deepcopy(rs[2]['inventory'][28])]
for e in d['inventory']:
 if e['element']=='opening':e['position'][2]=1691
 if e['element']=='union_clause':e['position'][2]=1691
 if e['element']=='right_note':e['first_words_or_objects']='i.e / i.e. de réunion, state uncertain, unequal S'
 if e['element']=='contained_in_segment':e['first_words_or_objects']='contenus dans un segment, two parallel rules and uncertain attachment/emphasis'
 if e['element']=='display_low_marks':e['first_words_or_objects']='two detached marks: lower-left point and higher-right point, attribution uncertain'
# Exact uncertainty arguments are extracted without changing, recognizing or normalizing text.
tokens=[];p=0
while True:
 p=tex.find('\\unsure{',p)
 if p<0:break
 start=p+8;depth=1;j=start
 while depth:
  if tex[j] in '{}':
   n=0;k=j-1
   while k>=0 and tex[k]=='\\':n+=1;k-=1
   if not n%2:depth+=1 if tex[j]=='{' else -1
  j+=1
 tokens.append(tex[start:j-1]);p=j
# Two endpoint curves are separately encoded, so their entries both point to locus 39.
uncertain_loci=[1,51,2,3,49,4,5,6,29,8,9,10,33,11,12,36,13,37,41,39,39,14,17,18,20,23,48,52,25]
assert len(tokens)==len(uncertain_loci),(len(tokens),tokens)
d['unresolved']=[]
for content,locus in zip(tokens,uncertain_loci):
 # The whole literal remains available even where the bar is nested in a macro.
 parts=[r'\deleted{P}',r'\deleted{S}'] if content==r'\deleted{P|S}' else content.split('|')
 f=d['findings'][locus-1]
 d['unresolved'].append({'place':f['place'],'reading':parts[0],'alternatives':parts[1:],'literal_uncertainty_content':content,'confidence':f['confidence'],'reason':obs[locus],'finding_id':f['id']})
notes=json.loads((w/'decisions/drafts/scan042_notes_working.json').read_text())['notes']
notes[5]='No authorial date or title is reported by the three complete readings. Pencil archive number 41 is retained only as a comment. The source begins the NB with a square bracket and supplies no closing mate on this page.'
notes.append('Three s-like equivalence abbreviations are retained, with the first sss/ssi uncertain. The first example writes a colon after réduites; the later non réduit phrase writes à. The isolated point after une and the end of choisi are resolved from ink, without grammatical repair.')
notes.append('Two parallel rules and framing curves in the intersection addition retain their uncertain emphasis/attachment roles. Two low marks below the final displayed u are reproduced as a lower-left and higher-right pair, with uncertain attribution and no assigned mathematical meaning. The old initial P/S layer at final Soit remains uncertain.')
notes.append('All three complete texts and every detailed return field were personally read. All 49 R1, 48 R2 and 47 R3 findings are mapped into 53 final loci. Seven C doubts are resolved and eighteen retained. The root made 32 actual local-crop views, including three new crops; it viewed no whole page or half. The narrower R1 compound-word crop omitted the distant point, and one R3 crop did not contain the separately targeted example gap; those limitations are recorded. No OCR, outside research, compilation or mathematical proof check was performed.')
d['notes']=[{'id':f'scan042-note-{i:02d}','text':s} for i,s in enumerate(notes,1)]
d['check_events']=[{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan042','type':'carried as background without fault found','outcome':'Source-account and ink/witness comparison only. Reading the recorded assertion is not presented as a proof check.'} for n in d['notes']]
d['notation']=[{'scan':42,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [3,7,8,9,16,17,24,28,29,32,37,39,41,45,48,52]]
d['abbreviations']=copy.deepcopy(rs[1]['abbreviations'])
d['sweep']=[]
d['crop_counts']={'R1':18,'R2':13,'R3':20,'main':3,'total':54}
d['main_crop_views']={'R1':list(range(1,19)),'R2':[1,2,6,10,12,13],'R3':[9,14,17,18,20],'main_new':3,'distinct_total':32,'total':32}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
op=w/'decisions/drafts/scan042_actual_crop_observations.json';o=json.loads(op.read_text());assert len(o['actual_views'])==32
o.update(status='Decided after all three complete texts and every detailed return field were personally read.',complete_text_review={f'R{k}':'Complete reading.tex and every detailed return field personally read.' for k in (1,2,3)},final_findings='decisions/scan042.json')
op.write_text(json.dumps(o,ensure_ascii=False,indent=2))
(w/'decisions/scan042_main_observations.md').write_text('# Scan042 main-reader observations\n\nAll three complete readings and detailed returns were personally read. Root viewed 32 distinct local crops; no whole page or half.\n\n'+'\n\n'.join(f'{i}. {obs[i]}\n\n   Crop: `{cr[i]}`' for i in range(1,54))+'\n\nThe earlier image-output truncation delivered no image and is excluded from the count. A later truncated detailed-return output delivered no findings 17–47; those were subsequently read in bounded outputs. No additional page-image pass was made.\n')
(w/'pages'/d['filename']).write_text(tex)
(w/'decisions/scan042.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'findings':53,'C':sum(f['against_C'] for f in d['findings']),'H':sum(f['against_H'] for f in d['findings']),'unresolved':len(tokens),'inventory':len(d['inventory'])}))
