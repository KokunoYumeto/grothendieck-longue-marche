"""Manual scan040 decisions after all full returns and eighteen actual local views."""
from pathlib import Path
import copy,datetime,json
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan040/R{k}/return.json').read_text()) for k in (1,2,3)]
maps={1:list(range(1,30))+[None],2:list(range(1,23))+[None,23,24,25,26,27,29,28],3:list(range(1,10))+[None,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,25,27,29,28]}
assert all(len(v)==30 for v in maps.values())
obs={
1:'The common Soi is clear. A long low cancellation covers small older loops before the tall final t. Ent/t remains open; H supplies only the live word.',
2:'The noun has a long q descent and two crossed t stems. Its first vowel is compressed and dark, leaving maquette/moquette open. The short reader crops clip the lowest q continuation; the complete descent is visible in the separately made statement crop for S.',
3:'The complete une is followed by a gap and the live noun. No independent cancelled word lies in that interval. The later high horizontal crosses the two t stems inside the noun.',
4:'Two tall joined t stems with a connecting crossbar stand before x. No intervening o/u bodies are present. Preserve tt.',
5:'Live les stands before the cancellation, and a separate live ens. follows it. The strike crosses only the low middle group. Its surviving humps and final turn leave ens./sous uncertain.',
6:'The first displayed set ends with its complete tall closing brace, followed by blank paper. H’s comma is absent. The second formula is on the next line.',
7:'Baseline tot has a separate underline. The raised narrow letter has a bent foot but no securely separated crossbar. Retain t/l. H explicitly states the written abbreviation in its note; R1’s proposed H difference is declined under that declared mapping.',
8:'The lower article has a looped l and a dark hooked e/a ending. The long diagonal crosses the l and rises beneath inserted pour. Retain cancelled le first, live le and cancelled la alternatives. The cancellation/leader function remains uncertain.',
9:'The old word above premier has initial n-like downstrokes, a low rounded body, tall t and a compressed final return under a long strike. Notons remains first with noter retained, explicitly recording R1’s reversed preference. Its raised position is preserved.',
10:'A detached black point lies immediately before the old crossed word, apart from its cancellation. Preserve the point with uncertainty over its punctuation function. R3 omits this mark.',
11:'The crossed first word has a tall looped capital S and final t. The following d-like loop and low compressed remnants leave donc uncertain. Preserve capital Soit.',
12:'An open c, low e and looped l lead into a plain low tail, without a separately isolated final a. Cel is first, with cela retained.',
13:'The faint beginning and joined low terminal turns favor aussi, with a high final dot before the colon. Retain R2/R3’s aussi/ceci uncertainty against R1’s resolved aussi.',
14:'The initial S has a long upper sweep and a lower loop, beside the much shorter i. Capital Si is confirmed in a new local crop.',
15:'There are solid marks at lower centre, upper centre and upper right; labels x below, z upper left and y upper right; four rising arrowheads and three detached shaft fragments. R1’s coordinate drawing preserves these objects and the observed bends. C already encodes all objects, so the representation change alone is not counted against C. H’s prose omits the upper-centre dot and two tips.',
16:'The word has a faint con beginning, one long g descent and short rus continuation. Congrus is resolved; the longer accented sequence in H is absent.',
17:'The connector begins with an a body and a high grave, then cause and a tall d with low e at the right edge. The complete phrase à cause de is visible.',
18:'The bracket’s reference line starts directly with 28, then a) and the final comma. No opening parenthesis precedes 28.',
19:'The terminal punctuation has a compact dark head and a downward-left tail before the closing square bracket. The comma is resolved.',
20:'An extra middle crossing lies on the long descent of live y. An older x is favored, but its identity and separate overwritten state remain coupled. R1’s outer uncertainty is retained; H acknowledges rewriting without supplying the old glyph.',
21:'Live z has its own upper and lower horizontals. An additional long diagonal descends beneath it, with a small upper branch. The possible old y and its overwritten state remain jointly uncertain.',
22:'The opening in connects into the word’s own baseline contours. No independent underline lies below that prefix. H’s extra emphasis is removed.',
23:'A detached high point stands above-right of a lower comma stroke after incomparables. The two-mark punctuation is read as a semicolon with R3, against R1’s retained alternative and R2’s comma.',
24:'The short word after On has a p-shaped descending initial and compressed low turns. Peu stays first, with pas and ne retained. The later contradiction wording supplies no replacement letters.',
25:'The comparison after z has an upper diagonal and two low horizontal traces separated by a narrow pale interval, with an independently projecting basal end. Read leq with R1/R3 against R2’s less-than-first uncertainty.',
26:'The comparison after x repeats the upper diagonal and two separately edged lower horizontals, with visible ends and a lighter intervening strip. Read leq with R1/R3 against R2’s less-than.',
27:'A compact detached dark point stands after on before the gap leading to aurait. Its visible form is resolved with R2/R3; this does not assign a grammatical function to it.',
28:'The new local crop shows an opening parenthesis, 28, a closing parenthesis, separate a), and a point. Preserve the two closing parentheses in (28) a).',
29:'One isolated thick stroke falls to the right after sigma z and the strict angle. There is no crossing arm or continuation. Retain the literal backslash-shaped first reading and the unfinished-x alternative with R1/R2 against R3’s resolution; no operand is completed.',
30:'The lower ne peut avoir group is crossed by a long separate line. The n/e beginning, p descent and final avoir forms survive, but the medial letters merge with the strike. Retain R2/R3’s uncertainty against R1’s resolution. The entire aurait donc stands above as the replacement.'
}
R1=lambda s:'readers/scan040/R1/'+s+'.png'
R2=lambda s:'readers/scan040/R2/crops/'+s+'.png'
cr={1:R1('01_soit'),2:R1('02_maquette'),3:R1('02_maquette'),4:'crops/scan040/main_statement.png',5:R1('03_les_ens'),6:'crops/scan040/main_statement.png',7:R1('04_tot'),8:R2('05_prouver_pour_le'),9:R2('06_notons'),10:R2('06_notons'),11:R1('06_cela_aussi'),12:R1('06_cela_aussi'),13:R1('06_cela_aussi'),14:'crops/scan040/main_display_si.png',15:R1('07_drawing'),16:R1('08_bracket_yz'),17:R1('08_bracket_yz'),18:R1('08_bracket_yz'),19:R1('08_bracket_yz'),20:R1('08_bracket_yz'),21:R1('08_bracket_yz'),22:R1('09_incomparables'),23:R1('09_incomparables'),24:R1('10_peu_and_orders'),25:R1('10_peu_and_orders'),26:R1('10_peu_and_orders'),27:R1('11_on_point'),28:'crops/scan040/main_final_reference.png',29:R1('13_final_stroke'),30:R1('12_aurait_revision')}
base=copy.deepcopy(rs[0]['findings'])+[copy.deepcopy(rs[1]['findings'][27])]
overrides={7:dict(against_H=False),8:dict(reading=rs[1]['findings'][7]['reading'],confidence='low'),9:dict(reading=r'\deleted{\unsure{notons|noter}}',against_C=False),13:dict(reading=r'signifie \unsure{aussi|ceci} :',against_C=True),23:dict(reading='incomparables; on aurait',confidence='high'),27:dict(reading='car on. aurait',against_C=True,c_doubt_status='resolved',confidence='high')}
d={'scan':40,'folder':'J81-05','their_page':39,'hua_has':'text','filename':'J81-05_81_scan040.tex','status':'decided','findings':[]}
fallback={(1,30):r'\deleted{ne peut avoir}; resolved in reading.tex and note 05',(2,23):'incomparables, on aurait in reading.tex',(3,10):'No detached point before the cancelled word in reading.tex'}
for i,f in enumerate(base,1):
 f.update(overrides.get(i,{}));f['id']=f'SP41-040-{i:03d}'
 f['marked_in_H']='yes' if f['marked_in_H'] is True or f['marked_in_H']=='yes' else 'no'
 f['crop']=cr[i];f['evidence']='Main reader, personally viewed local crop: '+obs[i];f['main_adjudication']=obs[i]
 f['readers']={};f['reader_source_ids']={}
 for k in (1,2,3):
  j=maps[k][i-1]
  if j is None:f['readers'][f'R{k}']=fallback[k,i];f['reader_source_ids'][f'R{k}']=['reading.tex at this locus']
  else:
   q=rs[k-1]['findings'][j-1];f['readers'][f'R{k}']=q['reading'];f['reader_source_ids'][f'R{k}']=[q['id']]
 if i==2:f['additional_main_crops']=['crops/scan040/main_statement.png']
 if i in (25,26):f['consequential']='The lower comparison is read as less-than-or-equal from its two visible lower strokes; the written form is preserved independently of the attempted proof.'
 d['findings'].append(f)
d['reader_finding_coverage']={}
for k in (1,2,3):
 used={a for f in d['findings'] for a in f['reader_source_ids'][f'R{k}'] if a.startswith('scan040-')};expected={f['id'] for f in rs[k-1]['findings']}
 assert used==expected,(k,expected-used)
 d['reader_finding_coverage'][f'R{k}']={'raw_findings':len(expected),'mapped_findings':len(used),'all_mapped':True}
tex=(w/'decisions/drafts/scan040_proposed.tex').read_text()
d['inventory']=copy.deepcopy(rs[1]['inventory'])
for e in d['inventory']:
 if e['element']=='Arrow diagram at left':e['kind']='drawing';e['element']='Arrow sketch at left, reproduced with explicit coordinates'
 if e['element']=='Proof continuation':e['first_words_or_objects']='Si y et z étaient incomparables; on aurait ...'
u=[copy.deepcopy(x) for x in rs[1]['unresolved'] if x.get('c_doubt_ids')!=['C040-D012']]
for x in u:
 if x.get('c_doubt_ids')==['C040-D009']:x.update(reading=r'\deleted{x}',alternatives=['crossing or reinforcement of live y'],reason=obs[20])
 if x.get('c_doubt_ids')==['C040-D010']:x.update(reading=r'\deleted{y}',alternatives=['additional strokes of rewritten z'],reason=obs[21])
assert len(u)==tex.count(r'\unsure{')==15
d['unresolved']=u
d['notation']=[{'scan':40,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [4,7,8,12,15,20,21,23,25,26,27,28,29]]
d['abbreviations']=copy.deepcopy(rs[1]['abbreviations'])
notes=json.loads((w/'decisions/drafts/scan040_notes_pending.json').read_text())['notes']
notes[7]+=' Graph traversal after each deleted edge independently computes the same six displayed subsets.'
notes.append('All three complete texts and every detailed return field were personally read. All 29 findings from each reader are mapped into thirty final loci. Three C doubts are resolved and eleven retained; fifteen uncertainty loci remain in the text. Root inspected eighteen distinct local crops, including three new crops, and never viewed a whole page or half. R1’s H difference for the expanded tot is declined because H explicitly supplies the abbreviation mapping. Each short noun crop clips the q descent; the independently required statement crop includes it. No OCR, outside research or compilation was used.')
d['notes']=[{'id':f'scan040-note-{i:02d}','text':s} for i,s in enumerate(notes,1)]
who='GPT-6 Astra Pro; inherited effort not exposed; main reader scan040'
d['check_events']=[]
for i,n in enumerate(d['notes'],1):
 computed=i in (8,9,10,11)
 d['check_events'].append({'statement_id':n['id'],'date':'2026-11-20','who':who,'type':'computation or formal certificate' if computed else 'carried as background without fault found','outcome':('Exact finite computation in scripts/scan040_tripod_check.py and validation/scan040_tripod_certificate.json: explicit cut/subset bijection and inverse, six graph-component traversals, 36 source-relation and clause checks, 216 transitivity triples, all cones and twelve intervals. This note reports only that finite computation.' if computed else 'Source-account and ink/witness comparison only; no independent proof is claimed for this source-account note.')})
d['check_events'].append({'statement_id':'scan040 opening proposition, principal upper and lower sets totally ordered','date':'2026-11-20','who':who,'type':"refuted, with the refined statement's id",'outcome':'Concrete refutation recorded as scan040-note-10 / SP41-scan040-tripod-finite-certificate: the explicitly mapped six-element structure passes the enumerated written conditions while its upper set at 1L and lower set at 1R each contain two incomparable entries. No general replacement theorem or unwritten continuation is asserted.'})
d['sweep']=[{'id':'SA01-K81-02','s':'Quotes the two principal sets and tot with raised t assertion; reports a tripod refutation and a larger tree computation.','decision':'The quoted written assertion is confirmed by the statement crop. A new exact six-element tripod certificate confirms the concrete refutation. The reported larger enumeration and general refinements are not certified by this run. The unfinished manuscript remains unchanged.','evidence':'crops/scan040/main_statement.png; readers/scan040/R1/13_final_stroke.png; scripts/scan040_tripod_check.py; validation/scan040_tripod_certificate.json. The cited c81checks.py is absent from the supplied package.'}]
d['crop_counts']={'R1':13,'R2':17,'R3':14,'main':3,'total':47}
d['main_crop_views']={'R1':list(range(1,14)),'R2':[5,6],'R3':[],'main_new':3,'distinct_total':18,'total':18}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
p=w/'decisions/drafts/scan040_actual_crop_observations.json';o=json.loads(p.read_text());assert len(o['actual_views'])==16
o['actual_views'] += [{'crop':'crops/scan040/main_display_si.png','observation':obs[14]},{'crop':'crops/scan040/main_final_reference.png','observation':obs[28]}]
o.update(status='Decided after all complete texts and every detailed return field were read.',count=18,complete_text_review={f'R{k}':'Complete reading.tex and every detailed return field personally read.' for k in (1,2,3)},final_findings='decisions/scan040.json')
o['corrections_to_preliminary_observations']=[obs[8],obs[13],obs[23],obs[25],obs[26],obs[27],obs[29],obs[30]]
p.write_text(json.dumps(o,ensure_ascii=False,indent=2))
(w/'decisions/scan040_main_observations.md').write_text('# Scan040 main-reader observations\n\nAll three complete readings and all detailed return fields were read; eighteen distinct local crops were viewed, including three main-reader crops. No whole page or half was viewed by root.\n\n'+'\n\n'.join(f'{i}. {obs[i]}\n\n   Crop: `{cr[i]}`' for i in range(1,31))+'\n\nThe early failed tool display for R1 crops 07/08 delivered no images and is excluded from the actual-view count. The later successful displays are counted once. The short noun crops clip q; the separate complete-statement crop required for witness S contains its whole descent.\n')
(w/'pages'/d['filename']).write_text(tex)
(w/'decisions/scan040.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'findings':30,'C':sum(f['against_C'] for f in d['findings']),'H':sum(f['against_H'] for f in d['findings']),'unresolved':len(u),'inventory':len(d['inventory'])}))
