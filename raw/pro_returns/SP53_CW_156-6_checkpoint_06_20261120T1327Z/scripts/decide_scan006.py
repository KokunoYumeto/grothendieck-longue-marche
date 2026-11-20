from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={f'R{i}':json.loads((O/f'readers/scan006/R{i}/report.json').read_text()) for i in range(1,4)}
D={k:{int(x['id'].split('D')[-1]):x for x in r['differences']} for k,r in R.items()}
map2=[1,2,3,4,5,6,8,7,9,10,11,11,12,13,12,14,15,17,16,15,None,18,19,20,21,22,23]
map3=[1,2,3,4,5,6,7,8,9,10,11,11,12,13,12,14,15,16,11,15,18,19,20,21,22,23,24]
rows=[]
for j,x in enumerate(R['R1']['differences']):
    x=copy.deepcopy(x);x['final']=x.pop('reading');x['readers']={'R1':x['final'],'R2':D['R2'][map2[j]]['reading'] if map2[j] else r'\operatorname{multomb}(F); retouching, no separate deletion','R3':D['R3'][map3[j]]['reading']}
    x['confidence']='high' if x['confidence']>=.85 else 'medium' if x['confidence']>=.65 else 'low'
    x['marked_in_H']='yes' if j+1 in [9,27] else 'no'
    # These differences concern graphically distinct letters/signs; do not claim a proved change of mathematical object.
    x['mathematical']=False
    rows.append(x)
def setrow(i,**kw):rows[i-1].update(kw)
setrow(3,final=r'\deleted{\unsure{de|la}}',against_C=True,confidence='low',evidence='Main crop decision: the low oval adjoining a tall loop favours de, as in R2/R3; the strike masks the join, so R1’s la remains possible. The longer dans of H has no recoverable n/s continuation. No certainty is claimed.')
setrow(4,mathematical='The doubled F in the opening definition is preserved as \\mathbb{F}; H prints ordinary F. The literal distinction is certain, but no change of mathematical object is inferred.')
setrow(5,crop='crops/scan006/01_deleted_On.jpg',confidence='high',evidence='Main crop shows the large open-topped O with its lower curved return and a low n trace under the straight cancellation. Read On, retaining its cancellation and removing C’s doubt.')
setrow(6,confidence='medium')
setrow(7,crop='crops/scan006/02_deployement.jpg',confidence='high',evidence='Main crop shows the long descending y after déplo, followed by the compressed ement sequence. Preserve déployement, without modernization to déploiement.')
setrow(8,crop='readers/scan006/R3/crops/15_insertion_comma_anchor.png',confidence='high',evidence='Main reader viewed R3’s crop: the thin insertion connector drops immediately after M, to the left of the separately written comma. The inserted indexing clause therefore precedes the comma.')
setrow(9,crop='readers/scan006/R2/05_inserted_jusqua_sentence.png',confidence='high',evidence='The crop shows Jusqu’à, then présent with p descender, accented vowel and raised ending; no q descender in that word. The sweeping line returns from the right below the sentence as an insertion connector, not as a pair of textual parentheses. A stop follows L.')
setrow(11,final=r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}',against_C=True,confidence='low',evidence='Main crop confirms P: long upright stem, broad angular bowl and a lower-left return. Its handwritten shape does not settle a specific typographic alphabet. R3’s wider candidate set is retained; mathcal remains the first candidate. This is alphabet uncertainty, not uncertainty about the letter P.')
setrow(12,confidence='low')
setrow(13,crop='crops/scan006/03_inverse_endings.jpg',confidence='high',evidence='Main crop contains the two closing parentheses and the adjacent blank space. No comma occurs after the upper inverse-image map; its line is separate from the Fig map below.')
setrow(14,confidence='high',evidence='Main crop confirms a horizontal shaft with one short upper barb and no lower barb. Encode the literal mark as rightharpoonup; its use as an application does not authorize adding an unseen lower barb.')
setrow(15,crop='crops/scan006/03_inverse_endings.jpg',confidence='high',evidence='The lower closing parenthesis has blank space to its right. H’s comma has no corresponding ink. The two inverse-image maps remain on separate manuscript lines.')
setrow(16,confidence='high')
setrow(17,final=r'\unsure{\mathcal{F}|\mathfrak{F}}',against_C=True,confidence='medium',evidence='Main crop shows an ornamental F with a loop at the top of the single stem, a broad left-running top flourish and a crossing middle stroke. The letter is F; a precise calligraphic/fraktur rendering is not settled. Retain the alternatives of R2/R3 at this first occurrence.')
setrow(18,confidence='medium',against_H=False,evidence='Main crop shows a rounded remnant at the shaft’s left end beneath oblique cancelling strokes. Those diagonals create the apparent leftward point. Read a cancelled hook, not a left arrow. H’s explicit note about overwritten hooks is credited as the same physical reading.')
setrow(19,crop='readers/scan006/R3/crops/10_first_mapping_arrow.png',confidence='low',evidence='Main reader inspected the target P in R3’s crop. Its upright, angular bowl and left-returning lower stroke match the earlier P. The primary mathcal encoding follows the first marked occurrence; alphabet uncertainty is not silently resolved here.')
setrow(20,confidence='medium',evidence='The second domain F has the same broad returning top arm and single stem. Use the first candidate after the first marked F on this page. The second cancelled hook is also visible; C and H’s explanatory note already preserve that state.')
setrow(21,confidence='low',evidence='Main crop shows a dense rising zigzag across the t between clear mul and omb; a vertical stem and cross-stroke survive. R1 reads live-or-deleted t, R2 retouching, R3 a doubtful live t. The ink does not settle the physical state: retain R1’s explicit alternatives, live t first, without inventing a previous letter.')
setrow(22,confidence='medium',evidence='Main crop shows a looped l with a very short low continuation; the final looped d has a trailing stroke favouring seconde. The article’s vowel is too reduced to decide la versus le confidently. Retain R1’s la seconde|le second, first candidate favoured by visible ending, without resolving it from grammatical agreement.')
setrow(23,confidence='high')
setrow(24,final=r'\deleted{on ne rien}',against_C=True,confidence='medium',evidence='Main crop shows an oval and low n-like ending, then a low n/e group, before the clear dotted-i word rien. There is no p descender or extra i-dot sequence supporting a priori. The main reading agrees with R2/R3; R1’s alternative is rejected from those strokes. Inserted capital On is separate above.')
setrow(25,h=r'\struck{de} (in \struck{de même})',confidence='high')
setrow(26,h=r'\struck{même}',confidence='high')
setrow(27,h=r'\uncertain{de}',kind='misread word',marked_in_H='yes',confidence='high',evidence='Main crop shows a separate long p descender followed by the low our group between barred m and multomb. This is pour. R1 aligns it with H’s uncertain de; R2/R3 call it an omission. The main collation records the actual substitution at the corresponding position, without adding a duplicate omission row.')
# The complete reading keeps the physical t-state and gender uncertainty; other decisions are applied explicitly.
s=(O/'readers/scan006/R1/reading.tex').read_text()
s=s.replace(r'\deleted{\unsure{la|de}}',r'\deleted{\unsure{de|la}}')
s=s.replace(r'\unsure{\mathcal{P}|\mathscr{P}}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}')
s=s.replace(r'\text{a)}\quad \mathcal{F}',r'\text{a)}\quad \unsure{\mathcal{F}|\mathfrak{F}}')
s=s.replace(r'\deleted{\unsure{on ne|a priori} rien}',r'\deleted{on ne rien}')
(O/'decisions/scan006_final.tex').write_text(s)
cd=copy.deepcopy(R['R2']['c_doubts'])
for c in cd:
    if 'After Multomb' in c['place']:c.update(evidence=rows[2]['evidence'],crop=rows[2]['crop'])
    elif c['c']==r'\unsure{\mathcal{P}|\mathscr{P}}':c.update(reading=r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}',evidence=rows[10]['evidence'],crop=rows[10]['crop'])
    else:
        matches=[x for x in rows if c['c'] in x['c']]
        if matches:c.update(evidence=matches[0]['evidence'],crop=matches[0].get('crop'))
inv=copy.deepcopy(R['R2']['inventory'])
inv.insert(20,{'element':'I20b','kind':'deletion','position':'(1.9)b, crowded t in multomb','first_words_or_objects':'t: live/retraced versus deleted state explicitly uncertain','sheet_kind':'text','hand':'his hand','transcribed':'yes'})
for x in inv:
    if x['element']=='I21':x['first_words_or_objects']=x['first_words_or_objects'].replace('la seconde','la seconde|le second')
notes={'content':R['R2']['notes']['content'],'math_reading_decisions':[
'The doubled F is kept literally; the ordinary F suggested by the surrounding sentence does not replace two visible stems.',
'The inverse-image Fig arrow has only an upper barb. Both (1.9) maps retain their cancelled injection hooks. The qualified injectivity language prompted attention to the hooks; it did not settle their shapes.',
'The P and domain-F alphabets remain uncertain at their first occurrences. Ordinary F, doubled F and the domain family are kept distinct.',
'The t in displayed multomb has a surviving stem and cross-stroke under dense ink; live/retraced and deleted states remain explicit alternatives. No prior letter is reconstructed.',
'The barred m in de barred-m pour is a verbal abbreviation, not an equality sign. It is not expanded in the transcription.'
],'author_doubts':["“dont la première n'a aucune raison d'être injective, la seconde par contre a une tendance à l'être” (article/ending of la seconde remains doubtful). A cross follows; no attached note occurs on this page.","“quand une confusion semble exclue” qualifies use of the shorter name ombre."],'titles_dates_counts':'Manuscript number 5. Formula label (1.9); reference 1.6 a)b). No title, date, or explicit page count.'}
unresolved=[]
for i in [3,10,11,17,21,22]:
    x=rows[i-1];unresolved.append({'place':x['place'],'reading':x['final'],'alternatives':x['final'],'confidence':x['confidence'],'evidence':x['evidence']})
checks=[{'statement_id':'SP53-006-N1','type':'carried as background without fault found','outcome':'Opening assertion: Multomb(F) is faithfully indexed by tilde F and determines F. Read as the author’s assertion; no mathematical verification performed.'},{'statement_id':'SP53-006-N2','type':'carried as background without fault found','outcome':'The two maps (1.9) are presented as inverse-image composites, with qualified injectivity. The expressions were parsed and the cancelled hooks compared with the prose; no proof of injectivity or non-injectivity was attempted.'}]
d={'scan':6,'mspage':'5','folder':'J156-6-01','filename':'J156-6-01_156-6_scan006.tex','brief':'v001','committed':False,'adjudicated_all':False,'differences':rows,'c_doubts':cd,'s_rows':[],'inventory':inv,'notes':notes,'check_events':checks,'unresolved':unresolved,'abbreviations':[{'form':r'\overline m','expansion':'même'},{'form':'Fig','expansion':'figure(s)'},{'form':'omb / Omb','expansion':'ombre'},{'form':'multomb / Multomb','expansion':'multiombre'}]}
(O/'decisions/scan006.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Prepared main decision draft: 27 locus rows, 12 C doubt decisions, 6 unresolved loci. Awaiting R3 completion before commit.')
