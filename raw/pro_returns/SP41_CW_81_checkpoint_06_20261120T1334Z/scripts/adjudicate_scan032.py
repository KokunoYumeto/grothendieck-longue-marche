"""Root adjudication of scan 032 after all three complete returns and 21 local views."""
from pathlib import Path
import json,copy,datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan032/R{k}/return.json').read_text()) for k in (1,2,3)]
mp1=list(range(1,20)) # R1 complete return read; same locus order as R3
mp2=[1,2,3,13,14,4,15,5,6,7,8,9,10,11,16,18,17,19,12]
assert len(mp1)==19
obs={
1:'A small isolated grey mark follows the terminal title letter. It is far paler than the main ink; retain the uncertain point.',
2:'A tall crossed t and compressed low following returns leave the number of ending e bodies open. Retain notée|noté without using agreement with paire to supply a letter.',
3:'The upper word run exposes i/n, tall d, dotted i strokes, c and doubled l; the lower continuation is ment. Resolve indiciellement and join the written line break.',
4:'The first-display letter has one roof, two hanging legs and an outward right foot below the height of Sigma. The second occurrence has the same roof and right-curved leg in main_second_pi.png. Retain pi|Pi at first occurrence and pi in (2′).',
5:'R1 crop 04 shows two vertically separated marks following ens: an upper round dot and a short low stroke with a right tail, without a closed a bowl. Use colon|à, retaining the compressed-à alternative. No additional abbreviation point is separately visible. The abbreviation and following sign form one coherent punctuation locus.',
6:'A detached elevated stroke accompanies the short de body. Its precise placement and relation to the preceding cancellation leave accent/apostrophe status open; retain dé|de|d’e. R2 resolves dé; the other readings and the main reader retain the alternatives.',
7:'A short separate low a group appears between l’on and supposé. A detached acute stands after the final verb body. Preserve a supposé.',
8:'Additional crossed diagonals occupy the live Sigma body. Their older identity and whether they are separately recoverable remain uncertain together; keep the possible X|Sigma layer before the live replacement.',
9:'Two bars and a thick crossing make the live inequality readable. Dense extra ink prevents isolation of an older crossing or separation from reinforcement. Keep the possible earlier =|inequality with uncertainty over its state.',
10:'R1 crop 08 shows the same upper return, inward middle and downward lower bend in the final primed glyph and the preceding primed epsilon. Resolve epsilon-prime with R1/R2; R3’s r-prime alternative is retained in the comparison record. The high prime is independently visible.',
11:'The central label is an angular peaked body beside the enclosing curve, without two separated lobes. Retain 3|s|wedge; the numbering sequence does not supply missing strokes.',
12:'R1 crop 10 and R3 crop 08 show a very short nearly upright second accent whose top is slightly right of its foot. Put the acute reading first with R3, hémisphéres|hémisphères, retaining grave. The rest of the word and its single underline are visible.',
13:'R1 crop 11 exposes a tall looped l and a closed low bowl with a short right-hand finish, under a separate cancellation. Resolve cancelled la with R1/R3; retain R2’s le alternative in the comparison record.',
14:'The old lower form has two low cups distinct from the taller live epsilon and matching the omega to its right. Resolve the overwritten omega with R1/R3; record R2’s remaining identity/state uncertainty.',
15:'The Sigma superscript consists of two joined low cups at one height, matching omega in the adjacent index. Retain written Sigma^omega. H’s formula prints epsilon while its note explicitly reports omega; both parts of H are recorded.',
16:'The short group before aurait has a low rounded onset and n-like return, with no separate tall l. Resolve on with R1/R3, recording R2’s alternative l’on. The actual high speck is not used to invent an absent l body.',
17:'The crop exposes dotted i, low n, tall d with a bowl, another i dot, and q-u-e. Read indique. The lower tip of the q descender is clipped in both reader verb crops inspected by the main reader; the decisive bodies and dots are visible, and the readers report the full descender in half b. No second crop was made.',
18:'The curved insertion leader descends into the baseline gap after sont and before à. Preserve that attachment. H’s editorial note identifies the whole phrase as added; the difference concerns its placement in the running text.',
19:'A clear d ascender and rounded foot lead into a heavily compressed low run. Keep uncertain donc because the final c is not independently separated; R2’s resolved reading is recorded.'
}
d={'scan':32,'folder':'J81-04','their_page':31,'hua_has':'text','filename':'J81-04_81_scan032.tex','status':'decided','findings':[]}
for i,base in enumerate(rs[2]['findings'],1):
 f=copy.deepcopy(base)
 sources=[rs[0]['findings'][mp1[i-1]-1],rs[1]['findings'][mp2[i-1]-1],base]
 f['id']=f'SP41-032-{i:03d}'
 f['readers']={f'R{k}':s['reading'] for k,s in enumerate(sources,1)}
 f['reader_source_ids']={f'R{k}':s['id'] for k,s in enumerate(sources,1)}
 f['marked_in_H']='yes' if i in [2,13] else 'no'
 f['confidence']={'medium-high':'medium','medium-low':'medium'}.get(f['confidence'],f['confidence'])
 f['crop']=str(Path(f['crop']).relative_to(w)) if f.get('crop') else ''
 f['evidence']='Main reader, cited local crop(s): '+obs[i]
 f['main_adjudication']='All three complete transcriptions, finding lists and inventories compared; main reader personally inspected the cited local crop evidence.'
 if f['c_doubt_status']=='resolved':f['against_C']=True
 if i==4:
  f['against_C']=True
  f['additional_crop']='crops/scan032/main_second_pi.png'
  f['evidence']+=' Second-occurrence evidence: crops/scan032/main_second_pi.png.'
 if i==5:
  f.update(c=r"(\omega\ \text{ens à deux éléments})",h=r"(\omega\text{ ens.\ à deux éléments})",reading=r"(\omega\ \text{ens \unsure{:|à} deux éléments})",against_C=True,kind='other',confidence='medium',crop='readers/scan032/R1/04_ens_a.png')
  f['readers']['R1']=r'ens à deux éléments'
  f['readers']['R3']=r'ens à deux éléments'
 if i==7:f['crop']='readers/scan032/R1/06_puisque_suppose.png'
 if i in [8,9]:f['against_C']=True
 if i==10:f.update(reading=r"\varepsilon'",c_doubt_status='resolved',against_C=True,crop='readers/scan032/R1/08_formula3_indices.png',mathematical_note='Resolved from the directly matching primed epsilon earlier in the same line; no mathematical assertion supplies the glyph.')
 if i==12:f.update(reading=r'\uline{\unsure{hémisphéres|hémisphères}}',crop='readers/scan032/R1/10_hemispheres.png')
 if i==13:f['crop']='readers/scan032/R1/11_cancelled_la.png'
 if i==15:
  f['kind']='misread symbol or index'
  f['consequential']='Formula (4) preserves the written omega exponent. H’s displayed epsilon and S’s proposed epsilon are recorded separately from the ink; H itself acknowledges omega in its note.'
 if i==16:f['crop']='readers/scan032/R2/crops/13_final_additions.png'
 if i==17:f['crop']='readers/scan032/R2/crops/12_final_verb.png'
 d['findings'].append(f)
t=(w/'readers/scan032/R1/reading.tex').read_text()
t=t.replace(r'\text{ens à deux éléments}',r'\text{ens \unsure{:|à} deux éléments}')
t=t.replace(r'\unsure{hémisphères|hémisphéres}',r'\unsure{hémisphéres|hémisphères}')
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[2]['inventory'])
d['inventory'][3]['first_words_or_objects']='pi=(Sigma^epsilon)_{epsilon in omega}; omega ens colon/à deux éléments'
d['unresolved']=[copy.deepcopy(u) for u in rs[2]['unresolved'] if u['place']!='Final primed glyph in (3)']
d['unresolved'].append({'place':'Two marks after ens','reading':':','alternatives':['à'],'confidence':'medium','reason':'Two separate vertically aligned marks remain compatible with a colon and a very compressed accented letter; the first follows their visible dot/stroke form.'})
d['notation']=copy.deepcopy(rs[2]['notation'])
for a in d['notation']:
 if a['form']==r"\varepsilon'|r'":a.update(form=r"\varepsilon'",evidence='R1 crop 08 and R3 crop 06: upper turn and downward lower return match the preceding primed epsilon; the high prime is separate.',reading=r"\varepsilon' resolved")
 if a['form']=='Acute/grave in hémisphères':a['reading']=r'\unsure{hémisphéres|hémisphères}'
d['notation'].append({'scan':32,'form':'Two marks after ens','evidence':'Upper round dot and short low stroke with right tail; no closed low bowl or separate abbreviation point.','reading':r'ens \unsure{:|à} deux éléments'})
d['abbreviations']=copy.deepcopy(rs[2]['abbreviations'])
d['notes']=copy.deepcopy(rs[2]['notes'])
d['notes'][1]['text']='The page introduces a “décomposition binaire” through a pair of closed distinct parts. The first family symbol retains pi/Pi uncertainty, with pi first from its lower cap and curved right foot. Omega’s parenthesis uses ens, followed by two vertically paired marks retained as colon|à and then deux éléments. The cancelled ensembles is represented before parties; the elevated mark in dé/de/d’e remains unresolved. The complete word indiciellement is resolved.'
d['notes'][3]['text']='The word distinctes and the later distinctness display helped locate the live inequality. The crop retains uncertainty about the older marks under the first Sigma and comparison. The final epsilon-prime is resolved from the matching upper return and downward lower bend in the preceding primed epsilon, with the prime independently visible. R3’s r-prime alternative is recorded in the apparatus. The compact display label remains 3|s|wedge; sequence alone does not decide it.'
d['notes'][5]['text']='The word hémisphéres/hémisphères and équateur are underlined. The tiny second accent favours acute by its slight rightward rise, while grave remains possible. The cancelled article is resolved as la. In (4), a low omega is overwritten by a taller epsilon in the lower index, and the Sigma superscript is visibly omega. H’s note reports this omega, although its displayed formula uses epsilon. S row SA01-K81-04 proposes epsilon from the definitions. This run confirms the written omega and does not insert that proposed correction. The mismatch between the family’s epsilon indices and the omega exponent prompted crop inspection; no mathematical proof was performed.'
d['notes'][7]['text']='No explicit author question, dated check or separate verification note was reported in the three readings. The page has been read independently three times, all complete returns compared, and every reader/witness disagreement adjudicated from local crops. C’s twelve doubts are covered: four resolved and eight retained. The family-case and ens punctuation loci add two uncertainties. No OCR, external research, compilation or proof check was performed.'
d['check_events']=[{'statement_id':a['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan032','type':'carried as background without fault found','outcome':'Source-account and local notation/ink comparison only. No independent proof, re-proof, computation or formal certificate was performed.'} for a in d['notes']]
d['sweep']=[{'id':'SA01-K81-04, scan 32 formula (4)','s':r'Lists E=intersection Sigma^omega and proposes Sigma^epsilon from the definitions.','decision':r'Confirmed the listed written Sigma^omega; the proposed epsilon is not an ink reading adopted by this transcription.','evidence':'R3 crop 10: the superscript has two low joined cups matching omega. H’s displayed epsilon and its explicit note reporting omega are both recorded. The scan 34 parts of the same S row are adjudicated with that page.'}]
d['main_crop_views']={'R3':list(range(1,13)),'R1':[4,6,8,10,11],'R2':[11,12,13],'main_new':1,'total':21}
d['crop_counts']={'R1':13,'R2':13,'R3':12,'main':1,'total':39}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan032.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'scan':32,'findings':len(d['findings']),'C_changes':sum(f['against_C'] for f in d['findings']),'H_changes':sum(f['against_H'] for f in d['findings']),'uncertainties':t.count('\\unsure{')}))
