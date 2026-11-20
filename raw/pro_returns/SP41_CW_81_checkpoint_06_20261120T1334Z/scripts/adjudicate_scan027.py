from pathlib import Path
import json,csv,re,copy,datetime
w=Path(__file__).resolve().parents[1]
r1=json.loads((w/'readers/scan027/R1/return.json').read_text())
r2=json.loads((w/'readers/scan027/R2/return.json').read_text())
mp={1:1,2:2,3:3,4:4,5:5,6:6,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:20,20:21,21:23,22:24,23:25,24:26,25:27,26:28,27:29,28:31,29:32,30:33,31:34,32:35,33:36,34:37,35:38,36:39,37:40,38:41,39:42,40:43,41:44,42:45,43:46,44:47,45:48,46:49,47:50,48:51,49:52,50:53,51:54,52:55,53:56,54:57,55:58,56:59,57:60,58:61,59:22,60:22,61:62}
f2={int(f['id'].split('-')[-1]):f for f in r2['findings']}
d={'scan':27,'folder':'J81-04','their_page':26,'hua_has':'text','filename':'J81-04_81_scan027.tex','findings':copy.deepcopy(r1['findings']),'status':'AWAITING_R3_AND_FINAL_ADJUDICATION'}
idx=[x for x in csv.DictReader((w/'validation/C_doubt_index.tsv').open(),delimiter='\t') if x['scan']=='27']
for i,f in enumerate(d['findings'],1):
 f['id']=f'SP41-027-{i:03d}'
 f['reader_source_ids']={'R1':r1['findings'][i-1]['id']}
 f['readers']={'R1':f['reading']}
 if i in mp:
  f['reader_source_ids']['R2']=f2[mp[i]]['id'];f['readers']['R2']=f2[mp[i]]['reading']
 f['c_doubt_ids']=[x['source_doubt_id'] for x in idx if '\\'+x['macro']+'{'+x['content']+'}' in f['c']]
 f['confidence']=f.get('confidence','medium')
 f['crop']=f['crop'].replace(str(w)+'/','') if f.get('crop') else ''
 f['main_adjudication']='Pending third return and comparison.'
 if f.get('marked_in_H') is True:f['marked_in_H']='yes'
 elif f.get('marked_in_H') is False:f['marked_in_H']='no'
for num,reading in {59:'en termes des',60:'(Cela signifie',62:"s'ils le \\unsure{\\deleted{sont}|sont}, on dit que les",63:r'E_2=\varnothing (Cela signifie'}.items():
 d['findings'][num-1]['readers']['R2']=reading
(w/'decisions/scan027.pending').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print('Drafted',len(d['findings']),'loci; C doubt coverage',len({x for f in d['findings'] for x in f['c_doubt_ids']}),'of',len(idx))
# Main reader's final adjudication after all three independent returns and crop inspection.
r3=json.loads((w/'readers/scan027/R3/return.json').read_text())
mp3={1:1,2:2,3:3,4:4,5:5,6:6,7:8,8:9,9:10,10:11,11:12,12:13,13:14,14:16,15:17,16:18,17:19,18:20,19:21,20:22,21:25,22:26,23:27,24:28,25:29,26:30,27:31,28:33,29:34,30:35,31:36,32:37,33:38,34:39,35:40,36:41,37:42,38:43,39:44,40:45,41:46,42:47,43:49,44:50,45:51,46:52,47:53,48:54,49:55,50:56,51:57,52:58,53:59,55:60,56:61,57:62,58:64,59:24,60:23,61:48}
f3={int(f['id'].split('-f')[-1]):f for f in r3['findings']}
for i,f in enumerate(d['findings'],1):
 if i in mp3:
  ff=f3[mp3[i]];f['reader_source_ids']['R3']=ff['id'];f['readers']['R3']=ff['reading']
 f['main_adjudication']='All three returns compared. Final reading accepted from the cited crop, or unanimous half-image reading where no witness-reading disagreement remained.'
for i,v in {54:'No extra cancelled item after X in the horizontal paragraph.',62:r"s'ils le \unsure{\deleted{sont}|sont}, \unsure{on|c.-à-d.} dit que les",63:r'E_2=\varnothing (Cela signifie'}.items():d['findings'][i-1]['readers']['R3']=v
for k in ['R2','R3']:d['findings'][5]['readers'][k]=r"ce que l'on \inserted{a} exclu"

# Exact selected readings; uncertainty remains where the ink does not settle a stroke.
choices={4:r'\deleted{\unsure{son|sont|se}}',16:r'\deleted{E}\Sigma_{12}',17:r'\unsure{bien pas|non pas}',21:r'(\Sigma_{\unsure{1|t}}^+,\Sigma_1^-)',25:r'\overset{\leftarrow}{\Sigma}',34:r"n'exige pas",39:r'\deleted{ens.}',46:r'\deleted{\unsure{\Pi|\Sigma}}',58:r'\unsure{floppées|floppés}',60:r'(\unsure{cela|Cela} signifie',63:r'E_2=\varnothing (\unsure{cela|Cela} signifie'}
for i,s in choices.items():d['findings'][i-1]['reading']=s
main_crops={1:'crops/scan027/main_01_equal_sign.png',3:'readers/scan027/R2/crops/02_cancel_part_son.png',5:'readers/scan027/R2/crops/02_cancel_part_son.png',8:'crops/scan027/main_02_upper_chain.png',17:'readers/scan027/R3/crops/13_margin_line_beginnings.png',21:'readers/scan027/R3/crops/11_margin_middle.png',25:'readers/scan027/R3/crops/11_margin_middle.png',33:'readers/scan027/R3/crops/12_margin_lower.png',34:'readers/scan027/R3/crops/12_margin_lower.png',36:'readers/scan027/R3/crops/12_margin_lower.png',37:'readers/scan027/R3/crops/12_margin_lower.png',39:'readers/scan027/R3/crops/12_margin_lower.png',40:'readers/scan027/R3/crops/12_margin_lower.png',41:'readers/scan027/R3/crops/12_margin_lower.png',42:'readers/scan027/R3/crops/12_margin_lower.png',60:'readers/scan027/R3/crops/11_margin_middle.png'}
for i,p in main_crops.items():d['findings'][i-1]['crop']=p
explanations={
 1:'Main crop: two detached horizontal bars precede si; retain the literal sign. The lower bar is heavier and slightly upturned at its left end. All readers choose the sign.',
 2:'Main inspection of R1 crop 01: tall looped initial and low covered remainder support donc; cancellation still permits alors. The following p, h and y/p descenders support par hyp. R2 prefers alors; preserve both alternatives.',
 3:'Main inspection of R2 crop 02: p descender, low ar, tall terminal t and abbreviation point remain under the cancellation. Resolve C’s doubt.',
 4:'Main inspection of R1 crop 02 and R2 crop 02: s-like initial, rounded low middle and covered ending. Son is the first reading; cancellation prevents exclusion of sont or se. All three alternatives are retained.',
 5:'Main inspection of R2 crop 02: small initial oval is followed by a separate tall l and a low ors continuation. Adopt alors; R2’s donc alternative is recorded in the three-reader column.',
 8:'Main crop shows a clear left arrowhead and returning hook on the E1 side. The other arrows leave E1/E2 toward their Sigma neighbours. H’s upper body has superset; its later note acknowledges the hook.',
 12:'Main inspection of R1 crop 05: left outline surrounds a pale centre. Final TikZ reproduces the oval, rather than choosing a mathematical vertex label. The upward slope and relative alignment follow the visible stroke.',
 13:'Main inspection of R1 crop 05: central black mark has an irregular upper edge and downward tip; the right mark is round and filled. Final TikZ preserves these outlines and the small break beside the middle mark.',
 16:'Main inspection of R1 crop 06: an additional straight left upright and middle horizontal remain under the rewritten angular Sigma. These support the earlier E. R1 retained a doubt; R2 and R3 resolved it. Main adopts deleted E.',
 17:'Main inspection of R3 crop 13: a tall initial and detached dark point favour bien; the compressed remainder also permits non. The next group has a descending p and low as. Retain bien pas|non pas; do not choose from the ni ... mais syntax. R1/R2 chose non pas.',
 21:'Main inspection of R3 crop 11: small lowered upright has a sideways head. 1 is the preferred reading; t remains possible and a separately attached i dot is not resolved. R1/R2 resolved 1; R3 retained 1|t.',
 25:'Main inspection of R3 crop 11: a short horizontal shaft ends in a left-pointing head formed by meeting oblique strokes. Adopt the left over-arrow, separately from the high oval after the comma. R1/R2 retained circle|arrow; R3 read the arrow.',
 33:'Main inspection of R3 crop 12: cancelled initial group has a low n-like start and compressed rounded continuation; nous is preferred and mais remains possible. The crossing stroke is clear. All readings are retained in the record.',
 34:'Main inspection of R3 crop 12: exige runs into the separate descending p of pas without a securely written ons group. Adopt n’exige pas. R1’s exigeons reading is recorded; R2/R3 read exige pas.',
 39:'Main inspection of R3 crop 12: low e, n/s continuation and abbreviation point remain under the crossing. Adopt deleted ens.; R1 kept a doubt, R2/R3 resolved it.',
 41:'Main inspection of R3 crop 12: the crowded qualification is crossed. The str sequence and following uprights survive, but the abbreviated ending is partly merged. Retain sont strictmt|sont strict. inside deletion; H’s live strict. is not adopted.',
 45:'Main inspection of R1 crop 08: live initial indi-like sequence, low c/e strokes, close tall l strokes and és-like ending. Retain indicellés|indiciellés. The uncertain spelling is not repaired to an expected indexed-family word.',
 46:'Main inspection of R1 crop 08: the cancelled initial symbol is crossed by diagonals; its surviving top/left strokes permit Pi and Sigma. Retain Pi|Sigma. R1’s reversed preference is recorded; no confident capital is supplied.',
 47:'Main inspection of R1 crop 08: a horizontal roof and two straight legs support capital Pi as first form, with lowercase pi retained. R2 chooses Pi; R3 chooses pi|Pi. The page’s repeated family glyph follows this provisional notation without a mathematical identification.',
 49:'Main inspection of R1 crop 08: repeated cancellation leaves an angular Sigma-like outline and high dotted i; the lower alpha is partly buried. Retain the uncertainty that R3 resolved.',
 55:'Main inspection of R1 crop 09: the long cross stroke belongs to initial t and does not continue as a separate cancellation through the whole word. Adopt live très, as R1/R3; R2’s deletion-state alternative is retained in the record.',
 58:'Main inspection of R1 crop 09: f/l opening and two deep p descenders support floppées over H’s exemples. The faint e sequence does not settle floppées versus floppés, so C’s ending doubt is retained, as R3.',
 60:'Main inspection of R3 crop 11: initial open curve is low beside the taller el strokes; lowercase cela is preferred. Handwritten size does not securely exclude capital Cela. Retain a new case doubt; R2/R3 choose capital, R1 lowercase.',
}
for i,e in explanations.items():d['findings'][i-1]['evidence']=e
resolved={1,3,6,7,9,10,11,12,13,16,23,24,25,30,31,32,34,35,37,38,39,40,42,43,48,52,55,57}
retained={2,4,15,17,21,22,26,27,28,33,36,41,45,46,49,50,53,56,58}
for i,f in enumerate(d['findings'],1):
 if i in resolved:f['c_doubt_status']='resolved'
 elif i in retained:f['c_doubt_status']='retained'
 if i in resolved and f['c_doubt_ids']:f['against_C']=True
 if i in {4,17,21,25,33,41,45,47,51,60}:f['against_C']=True
 if i in {34,46}:f['against_C']=(i==34) # 34 resolves an existing C doubt; 46 retains C verbatim.
 if i in {53,56}:f['against_H']=False # same primary reading, only uncertainty differs
 if i in {17,21,33,41,45,46,47,49,50,53,58,60}:f['confidence']='low'
 if i in {16,25,34,39,55}:f['confidence']='medium'
 if i in {1,3,5,6,7,8,9,10,11,12,13}:f['confidence']='high'
 if f['crop']=='':f['crop']='source half a; unanimous reader inspection'
 f['evidence']=f['evidence'].replace('Half a:', 'All three half-a readings report:') if i==7 else f['evidence']
# A separate live connective omitted behind H's illegibility marker.
f={'id':'SP41-027-064','place':'Slanted note, live connective before symetrique','c':'et la relation','h':r'\ill{}','reading':'et la relation','against_C':False,'against_H':True,'kind':r'readable ink left as \ill{}','marked_in_H':'yes','confidence':'high','evidence':'Main inspection of R1 crop 07 and R3 crop 11: et, separate la, and the long l/t strokes and dotted i of relation remain live after the cancelled ou. These words are outside that cancellation.','bbox':[295,1600,545,1970],'crop':'readers/scan027/R3/crops/11_margin_middle.png','c_doubt_status':'none','readers':{'R1':'et la relation','R2':'et la relation','R3':'et la relation'},'reader_source_ids':{'R1':'reading.tex, marginal sentence; f27 evidence','R2':'scan027-R2-030','R3':'scan027-R3-f32'},'c_doubt_ids':[],'main_adjudication':'All three returns compared; live words confirmed in crop.'}
d['findings'].append(f)
for i,text in {18:'The first positive-parts comparison is a plain equality; H supplies a crossed comparison.',19:'The margin writes équivaut à before E1=Sigma12; H substitutes implique.',25:'The marginal Sigma carries a left over-arrow, omitted by H and left circle/arrow-uncertain by C.'}.items():d['findings'][i-1]['consequential']=text

# Assemble the complete diplomatic page from the inspected R1 text, with explicit adjudicated substitutions.
t=(w/'readers/scan027/R1/reading.tex').read_text()
replacements={
 r'\deleted{\unsure{son|sont}}':r'\deleted{\unsure{son|sont|se}}',
 r'\deleted{\unsure{E}}\Sigma_{12}':r'\deleted{E}\Sigma_{12}',
 r'(non pas $':r'(\unsure{bien pas|non pas} $',
 r'(cela signifie':r'(\unsure{cela|Cela} signifie',
 r'(\Sigma_1^+,\Sigma_1^-)$ que':r'(\Sigma_{\unsure{1|t}}^+,\Sigma_1^-)$ que',
 r'\overset{\unsure{\circ|\leftarrow}}{\Sigma}':r'\overset{\leftarrow}{\Sigma}',
 "n'exigeons pas":"n'exige pas",
 r'\deleted{\unsure{ens.}}':r'\deleted{ens.}',
 r'\deleted{\unsure{\Sigma|\Pi}}':r'\deleted{\unsure{\Pi|\Sigma}}',
 'des floppées.':r'des \unsure{floppées|floppés}.'
}
for a,b in replacements.items():
 if a not in t:raise SystemExit('Missing intended substitution '+a)
 t=t.replace(a,b)
fig2=re.search(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}',(w/'readers/scan027/R2/reading.tex').read_text(),re.S).group(0)
t=re.sub(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}',lambda m:fig2,t,flags=re.S)
t=t.replace('\\margin{Ceci', '% slanted\n\\margin{Ceci')
(w/'pages'/d['filename']).write_text(t)

# Inventory categories follow the requested schema, retaining raw reader inventories unchanged.
inv=copy.deepcopy(r1['inventory'])
for e in inv:
 e['kind']={'text block':'text','underlining':'text','margin':'margin note','numbering':'text'}.get(e['kind'],e['kind'])
 e['sheet_kind']='text';e['hand']='another unnamed hand (archive pencil)' if 'pencil' in e['hand'].lower() else 'his hand'
 e['position']='whole-scan pixels '+str(e['position'])
 if e['element']=='Diagonal cancelled word':e['first_words_or_objects']='nous|mais (uncertain; cancelled)'
 if e['element']=='Study paragraph':e['first_words_or_objects']='Je me propose d’étudier les ensembles finis indicellés|indiciellés'
 if e['element']=='Closing sentence':e['first_words_or_objects']='Voici une façon très générale d’ [en cancelled] obtenir des floppées|floppés'
inv.sort(key=lambda x:(int(re.search(r'\[\d+, (\d+)',x['position']).group(1)),x['element']))
d['inventory']=inv
# Only source-based notes: no proof check is claimed for this page.
d['notes']=copy.deepcopy(r1['notes'])
d['notes'][2]['text']='The diagonal note discusses equalities among four signed Sigma sets, writes “qui équivaut à” before E_1=Sigma_12 and “et entraîne” before E_2=empty set, and then “On ne veut pas exclure ce cas”. The parenthesis before the first equality remains bien pas|non pas from its tall initial and compressed continuation. The overmark on the later Sigma is a visible left arrow. The ending n’exige pas is adopted after comparison with R1’s exigeons pas. Cancellation of sont and the crowded abbreviated qualification remain uncertain. These are reading decisions; the mathematical equivalence was not independently proved.'
d['notes'][3]['text']='The lower paragraph proposes studying finite indexed families of pairwise non-parallel binary decompositions of X. The written adjective indicellés|indiciellés is retained. The live family glyph is Pi|pi, with Pi first from the horizontal roof and straight legs. Cancelled mathematical drafts remain included, including an unfinished opening set brace. The last word has initial fl and two p descenders; floppées|floppés preserves the faint ending.'
d['notes'][4]['text']='The faint lower-left 26 is recorded as archive numbering. No title, date, authorial page number or total page count is visible on this sheet. The page carries no explicit proof-check request. The three readers excluded the accidental folder-wide notes footer from their evidence.'
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
d['check_events']=[{'statement_id':x['id'],'date':now,'who':'GPT-6 Astra Pro; inherited effort not exposed; main run scan027','type':'carried as background without fault found','outcome':'Source account grounded in three independent readings and the documented crop adjudications. No independent mathematical proof check is claimed; the note reports the manuscript and the actual reading decisions.'} for x in d['notes']]
d['notation']=[{'scan':27,'form':x['forms'],'evidence':x['place']+': '+x['observation'],'reading':x['forms']} for x in r1['notation']]
d['notation'][4]={'scan':27,'form':r'\Sigma_2^{\dot{-}|-}; \overset{\leftarrow}{\Sigma}_1^{-,\circ|0}','evidence':'Slanted complement formula: detached point above minus remains uncertain; the overmark has left-pointing head and horizontal shaft (R3 crop 11, main adjudication); high oval after comma remains circle/zero-uncertain.','reading':r'\Sigma_2^{\unsure{\dot{-}|-}}; \overset{\leftarrow}{\Sigma}{}_1^{-,\unsure{\circ|0}}'}
d['abbreviations']=[{'scan':27,'form':x['form'],'expansion':x['likely_expansion']} for x in r2['abbreviations']]
d['unresolved']=[]
for f in d['findings']:
 if '\\unsure{' in f['reading'] and f['id'] not in ['SP41-027-062','SP41-027-063']:
  d['unresolved'].append({'place':f['place'],'reading':f['reading'],'alternatives':'As explicitly listed in the in-place doubt macro; a single candidate remains tentative where no alternative is securely legible.','confidence':f['confidence'],'reason':f['evidence']})
d['crop_counts']={'R1':9,'R2':9,'R3':13,'main_new':2,'main_existing_crops_viewed':13,'total_created':33}
d['reader_returns_compared']=['readers/scan027/R1/return.json','readers/scan027/R2/return.json','readers/scan027/R3/return.json']
d['status']='decided';d['decided_utc']=now
d['sweep']=[]
(w/'decisions/scan027.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print('Decided scan 027 with',len(d['findings']),'loci and',len(d['unresolved']),'unresolved loci.')
