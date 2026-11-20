"""Main reader's scan 030 decisions, following complete returns and 17 local views."""
from pathlib import Path
import json,copy,datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan030/R{i}/return.json').read_text()) for i in (1,2,3)]
mp2=list(range(1,16))+[14,16,17,18,18,20,19,21,22,23,23,24,26]
mp3=list(range(1,16))+[15,16,17,18,18,19,20,21,22,23,23,25,28]
r2c={int(p.name[:2]):str(p.relative_to(w)) for p in (w/'readers/scan030/R2').glob('*.png')}
cn=[1,2,3,4,5,6,7,7,8,9,10,11,12,7,7,7,0,0,0,0,0,0,0,0,0,10,0,12]
obs={
1:'The initial upright has a roof and baseline, followed by a tall stroke with a detached short cross-stroke and a low final run. Retain Item, Idem and Itou; no final letters are supplied from context.',
2:'Two tall joined t strokes share a crossing and lead to a short e-like return. Resolve the written abbreviation tte; no intervening o/u bodies are visible.',
3:'A long nearly horizontal shaft ends with a thick tip and a short downward spur. Keep the horizontal-stroke first reading and arrow alternative; no complete paired head is visible.',
4:'Two live groups precede images. The first has a tall looped l. The second begins with a small closed bowl below a separate rising stem, then runs to a downturned s. Resolve les des with R2; record R1/R3’s reduced-l alternative without dropping the second group.',
5:'A larger left upright and outer bowl survive beneath the heavy live O and r. The older D and its overwritten state remain uncertain together, as all three readers represent them.',
6:'A detached dark short oblique descends after the faint terminal of application, separated by blank paper. Resolve the comma.',
7:'The tiny angular mark after the index S has a bent rising stroke and short right branch. Its full arm count is not separable; retain star|plus.',
8:'A small low oval and detached accent survive under a distinct horizontal cancellation before live celle. Resolve cancelled à.',
9:'The looped d and low middle are followed by a further downturned terminal s. Resolve des.',
10:'Three connected curved movements, including a looped middle and descending final return, are visible without a separate final i-dot. Resolve sss.',
11:'Two crossed centres, one lighter and one darker, lie inside the inner pair of parentheses. Resolve the two-star label.',
12:'The lower t with its cross-stroke, compressed e and terminal l are traversed by a separate heavy cancellation. Live et is written above. There is no separate comma at the right. Retain cancelled tel followed by inserted et.',
13:'The connector has a tiny low loop-like onset, a flattened wavering run and a short downward end. Retain ou|dash; the letters are too reduced to resolve.',
14:'The raised wording contains only d and the short low ens run before the comparison signs. Preserve d’ens as an abbreviation.',
15:'The complete raised line reads d’ens followed directly by crossed comparison bars and a slashed oval. No separate word groups form deux à deux disjoints.',
17:'The short ens run ends before a blank interval leading to non. No abbreviation point follows it; the separate sentence-final point after vides is present.',
18:'The initial low avec groups lead to plus with its tall loop, de with a small bowl, and soin with a separate high i mark, followed by a comma. Adopt avec plus de soin.',
19:'After il donne, the accented beginning and flattened an/moin run end in a low s return. Adopt néanmoins.',
20:'The next line has ce, qu’on with a detached apostrophe and visible q descender, then veut with a raised final t. Adopt ce qu’on veut. The crop cuts the bottom tip of the long q descender but contains all letter bodies and word endings; the three half readings also agree.',
21:'The local context beside stricte has three connected s-shaped turns and no independent final i-dot. Preserve the second sss.',
22:'After the second tall crossed t, a separate low rightward curl and downturned finish support the terminal e. Preserve stricte.',
23:'Two low c/e groups and a final high i-dot sit above one separate underline. Read underlined ceci.',
24:'Underlined ceci is immediately followed by the opening parenthesis and plus. No intervening three-star label is written there.',
25:'The opening parenthesis is followed directly by the descending p and joined lus. No preceding en group is visible.',
26:'The next line begins with a tall descending crossed f, reduced or and terminal crossed t before que. Read fort.',
27:'A long horizontal cancellation crosses the original que, U_s=empty-set, comma and et. Above it stands the incident-edge clause with its comma after incidente. Preserve the cancelled predecessor before the inserted replacement; both comparison bars in the old equality and the extra crossing strokes in the live inequalities are retained.',
28:'The final slashed oval is followed by blank paper. No terminal period is supplied.'
}
d={'scan':30,'folder':'J81-04','their_page':29,'hua_has':'text','filename':'J81-04_81_scan030.tex','status':'decided','findings':[]}
for i,base in enumerate(rs[0]['findings'],1):
 if i==16:continue
 f=copy.deepcopy(base);sources=[base,rs[1]['findings'][mp2[i-1]-1],rs[2]['findings'][mp3[i-1]-1]]
 f['id']=f'SP41-030-{len(d["findings"])+1:03d}'
 f['readers']={f'R{k}':s['reading'] for k,s in enumerate(sources,1)}
 f['reader_source_ids']={f'R{k}':s['id'] for k,s in enumerate(sources,1)}
 f['marked_in_H']='yes' if f['marked_in_H'] in [True,'yes'] else 'no'
 f['crop']=r2c[cn[i-1]] if cn[i-1] else ''
 f['evidence']='Main reader, cited crop: '+obs[i]
 f['main_adjudication']='All three complete transcriptions and complete finding lists compared; main reader inspected the cited local crop.'
 if f['c_doubt_status']=='resolved':f['against_C']=True
 if i==4:f.update(reading='les des',c_doubt_status='resolved',against_C=True,confidence='medium')
 if i==5:f['against_C']=True
 if i==12:
  f['readers']['R3']=r'\deleted{tel} \inserted{et}; no following comma'
  f['reader_source_ids']['R3']='scan030-R3-F12, F24, F26 and reading.tex'
 if i==17:f['crop']='crops/scan030/main_ens_punctuation.png'
 if i in [18,19,20]:f['crop']='crops/scan030/main_empty_sets_wording.png'
 if i in [21,22]:f['crop']='readers/scan030/R3/crops/09_stricte.png'
 if i in [23,24,25]:f['crop']='crops/scan030/main_ceci_plus.png'
 if i==27:
  f['crop']='readers/scan030/R3/crops/12_lower_correction.png'
  f['reader_source_ids']['R2']='scan030-R2-F24, F25 and reading.tex'
  f['readers']['R2']=r'\deleted{que $U_s=\varnothing$, et} \inserted{$a\in A$ une arête incidente, on a}'
 if i==15:f['consequential']='The short insertion contains only d’ens ≠∅; H’s extra disjointness words are absent from the ink.'
 if i==24:f['consequential']='H’s extra (***) after ceci is absent; the separate lower (***) label remains in its written place.'
 if i==27:f['consequential']='The cancelled equality and the live incident-edge replacement retain their distinct written states and attachment.'
 d['findings'].append(f)
extra=copy.deepcopy(rs[2]['findings'][26])
extra.update(id='SP41-030-028',readers={'R1':'E_a','R2':'E_a','R3':r'E_{\unsure{c|a}}'},reader_source_ids={'R1':'reading.tex, final display','R2':'reading.tex, final display','R3':'scan030-R3-F27'},marked_in_H='no',crop='readers/scan030/R3/crops/12_lower_correction.png',evidence='Main reader, R2 crop 12 and R3 lower-correction crop: the small subscript has an upper stroke and lower return meeting at the left, with an open right side and no separate closing upright. Retain c|a, with c first as R3; R1/R2 give a. The earlier quantified a does not supply a missing closing stroke.',main_adjudication='All three texts compared; the two existing local crops were inspected.',consequential='The final displayed E subscript is retained as c|a from its open curve; the earlier E-family still has written index a.')
d['findings'].append(extra)
t=(w/'readers/scan030/R1/reading.tex').read_text().replace(r'\unsure{les des|les les}','les des').replace(r'\ E_a\ne\varnothing',r'\ E_{\unsure{c|a}}\ne\varnothing')
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[2]['inventory'])
d['unresolved']=[copy.deepcopy(u) for u in rs[2]['unresolved'] if u['place']!='Two groups before images']
for u in d['unresolved']:
 if u['confidence'] not in ['high','medium','low']:u['confidence']='medium'
d['notation']=copy.deepcopy(rs[2]['notation'])
d['notation'].append({'scan':30,'form':'Possible older D at Or','evidence':'A larger upright and outer bowl survive beneath the live capital; identity and overwritten state stay uncertain.','reading':r'\unsure{\deleted{D}}Or'})
d['abbreviations']=copy.deepcopy(rs[2]['abbreviations'])
d['notes']=copy.deepcopy(rs[2]['notes'])
d['notes'][2]['text']='The author writes that the case of empty component sets is “à examiner avec plus de soin”. The continuation reads “il donne néanmoins ce qu’on veut” and cites (*) and (**). The same paragraph writes non-parallélisme stricte, sss, and underlined ceci, followed by plus fort que (**). The author’s instruction for further examination is recorded as such; no proof check was performed.'
d['notes'].append({'id':'scan030-note-07','text':'H’s explicit editorial note describes the interlinear attachment and includes the nonempty relation in the added material. Consequently its narrower add macro is not separately counted as an insertion-state difference. The expanded abbreviation and the extra disjointness words receive their own collation entries. Every C doubt is decided: eight resolved and five retained. The final open E subscript adds one unresolved locus.'})
d['check_events']=[{'statement_id':a['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan030','type':'carried as background without fault found','outcome':'Source-account event only: three independent readings and local ink crops compared. No independent proof, re-proof, computation or formal certificate was performed.'} for a in d['notes']]
d['excluded_macro_only']=[{'reader_finding':'scan030-R1-F016','reason':'H’s explicit editorial note attributes the nonempty relation to the interlinear addition. Its narrower add-macro boundary is covered by that note; words and abbreviation are separately collated.'}]
d['main_crop_views']={'R2':list(range(1,13)),'R3':[9,12],'main_new':3,'total':17}
d['crop_counts']={'R1':12,'R2':12,'R3':12,'main':3,'total':39}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan030.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'scan':30,'findings':len(d['findings']),'C_changes':sum(f['against_C'] for f in d['findings']),'H_changes':sum(f['against_H'] for f in d['findings']),'uncertainty_macros':t.count('\\unsure{'),'unresolved':len(d['unresolved'])}))
