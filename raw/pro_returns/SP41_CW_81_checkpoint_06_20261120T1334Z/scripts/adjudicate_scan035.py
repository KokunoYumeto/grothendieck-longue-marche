"""Root's scan035 decisions. Run only after all detailed returns have been compared."""
from pathlib import Path
import copy, json, datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan035/R{k}/return.json').read_text()) for k in (1,2,3)]
mapping=json.loads((w/'decisions/drafts/scan035_reader_mapping.json').read_text())
obs={
1:'A short horizontal remains beneath the broad descending replacement. Preserve deleted minus followed by setminus, with R1/R2, recording R3’s retained live-operator doubt.',
2:'The first word has a clear looped d and very compressed level continuation. Retain donc uncertain, with all readers.',
3:'The low index is heavily overwritten. A dark upright and lower foot favour live 1; curved side material remains, and neither the live 1/2 nor the older 2/1 separates securely. Retain both uncertainties with R3. H expressly records rewriting and live 1; its same primary reading and acknowledged state add no H collation row.',
4:'The cap and two Pi legs survive the cancelling strokes. The low suffix is crossed and filled; retain Pi2/Pi1. H leaves the readable group as struck illegible.',
5:'The live final suffix has two successive rounded turns and a downward terminal, while the nearby ordinary 2 has one turn and a rightward foot. Resolve the written 3 with all readers. No 2 is supplied from the preceding pair definitions.',
6:'Two detached small dots lie one above the other before l’. No low connected a-body appears. Resolve colon.',
7:'The tall h, descending y/p strokes and compressed later run support hypothèse first. The small final letters and accent remain open. Retain hypothèse/hypothese, recording R2’s reversed preference.',
8:'Soi is visible, including its detached dot; the terminal run is contracted and crossed. Keep Soient/Soit with R1/R3, recording R2’s Soit-first reading.',
9:'The separator has a distinct upper short mark and a curved lower comma body. Resolve semicolon with all readers.',
10:'The adjective has a long p descent, low middle runs, a tall h and a raised accent before the final s-shaped return. Resolve panachées with all readers.',
11:'The first exponent has a horizontal cap and descending stem. The second has an upright projecting above its crossbar. Keep top/plus at the first exponent, top first, with all readers.',
12:'Both low forms have two rounded lower bowls and raised outer ends. Resolve omega with R2/R3, recording R1’s w alternative.',
13:'The target capital has a long straight stem, broad upper bar, angular right bowl and leftward lower hook. The fraktur/calligraphic rendering remains uncertain.',
14:'The subscript starts with looped f, has compressed low shoulders, a distinct late dot, and an s-shaped terminal return. Put finies first with R2/R3 and retain fermés/fermé. R1 puts fermés first. No mathematical interpretation settles these compressed letters.',
15:'The earlier horizontal cap and long descending right segment of 7 remain distinguishable beside the later two-loop 8. Resolve the old 7. H acknowledges rewriting but does not give the older readable numeral.',
16:'The live oval-headed 9 and its descent overlay an additional lower loop and side return from 8. Resolve the older 8 with R2/R3, recording R1’s retained doubt.',
17:'The low e-loop joins a tall t with a visible crossbar. Resolve et, with all readers and H.',
18:'The inline 8 has a large lower loop, an older high curved cap and an additional horizontal crossbar. The earlier figure’s body remains merged. Retain uncertain 7 with R1/R2, recording R3’s resolved 7.',
19:'The initial dotted i, n run, long j descender, middle e/c, tall t loop, second dotted i and final ve are visible. Resolve injective with all readers.',
20:'The initial small open body is followed by a tall l and low terminal o/r/s run. Read alors, with all readers and C. H gives donc here.',
21:'Proposition stands above the crossed Corollaire. A single long underline lies beneath Corollaire; no separate underline lies beneath Proposition. H expressly describes the replacement placement, which maps to the insertion macro. Its emphasis scope is separately different; its preamble states that emph represents the author’s own emphasis.',
22:'The upper rule has complete endpoints beside the binaires/Alors lines. A second shorter rule has complete endpoints beside tel. Preserve both distinct rules. H’s note mentions a singular marginal stroke and omits the separate lower one.',
23:'The complete slashed oval is followed by clear paper, without a detached terminal point. Preserve the unpunctuated formula ending. H’s exact display appends a point.',
24:'A horizontal crosses both upper arms of the little X, with distinct outer ends. It may be an older horizontal or the surviving bar of a former Sigma; its identity and state remain uncertain. Keep the explicit uncertain older remnant before the live X.',
25:'An additional upright extends above the second Pi’s cap and below its normal left-leg endpoint, with a dark lateral projection. Preserve the visible upright under uncertainty covering revision versus reinforcement; no complete older letter is supplied.'
}
d={'scan':35,'folder':'J81-05','their_page':34,'hua_has':'text','filename':'J81-05_81_scan035.tex','status':'decided','findings':[]}
for i,base in enumerate(rs[0]['findings'],1):
 f=copy.deepcopy(base)
 f['id']=f'SP41-035-{i:03d}'
 f['readers']={'R1':base['reading']}
 f['reader_source_ids']={'R1':base['id']}
 for k in (2,3):
  ids=mapping[str(i)][f'R{k}']
  matches=[x for x in rs[k-1]['findings'] if x['id'] in ids]
  assert len(matches)==len(ids),(i,k,ids)
  f['readers'][f'R{k}']='; '.join(x['reading'] for x in matches) if ids else mapping[str(i)][f'R{k}_text']
  f['reader_source_ids'][f'R{k}']=ids or ['reading.tex, same locus']
 f['marked_in_H']='yes' if i==4 else 'no'
 f['crop']=str(Path(f['crop']).relative_to(w)) if f.get('crop') else ''
 f['evidence']='Main reader, personally viewed local crop(s): '+obs[i]
 f['main_adjudication']='All three complete texts and detailed returns compared. See decisions/scan035_main_observations.md.'
 if i==3:f.update(reading=r'\Sigma_{\unsure{\deleted{2|1}}\unsure{1|2}}^-',c_doubt_status='retained',confidence='low')
 if i==5:f['consequential']='The source writes Pi1=Pi3 after displaying the Pi1 and Pi2 pairs. Its two-turn 3 is preserved; H prints 2.'
 if i==6:f['crop']='readers/scan035/R1/05_hypothese.png'
 if i==7:f.update(reading=r'\unsure{hypothèse|hypothese}',against_C=True)
 if i==10:f['consequential']='The proposition reads non panachées. H substitutes non parallèles; the visible p/h/é letter sequence is retained.'
 if i==11:f['consequential']='The first ordered-pair superscript is T-shaped. Preserve top as first reading with plus retained, without supplying an upper stroke.'
 if i==12:f.update(reading=r'\omega_1',against_C=True,c_doubt_status='resolved')
 if i==14:f.update(reading=r'\unsure{\text{finies}|\text{fermés}|\text{fermé}}',against_C=True,against_H=True)
 if i==16:f.update(reading=r'\tag*{(1\deleted{8}9)}',against_C=True,c_doubt_status='resolved')
 if i==18:f['crop']='readers/scan035/R3/crops/14_inline18.png'
 if i==20:f.update(crop='crops/scan035/main_alors.png',bbox=[248,682,397,765])
 if i==21:f.update(crop='crops/scan035/main_heading.png',bbox=[240,860,535,1005])
 if i==22:f.update(crop='crops/scan035/main_emphasis_upper.png',additional_crop='crops/scan035/main_emphasis_lower.png')
 if i==23:f.update(crop='crops/scan035/main_intersection_end.png',bbox=[865,1415,1045,1540])
 if i==24:f.update(reading=r'\unsure{\deleted{{-}|\Sigma}}X\setminus\Sigma_1^+')
 d['findings'].append(f)

# Extra loci and their exact source IDs are reviewed and supplied in the mapping file.
for entry in mapping['extra']:
 f=copy.deepcopy(entry)
 d['findings'].append(f)

t=(w/'decisions/drafts/scan035_main_draft.tex').read_text()
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[0]['inventory'])
for e in d['inventory']:
 x=e['first_words_or_objects']
 x=x.replace(r'\unsure{\deleted{2}} before live 1',r'\unsure{\deleted{2|1}} before \unsure{1|2}')
 x=x.replace(r'\unsure{\deleted{-}}X',r'\unsure{\deleted{{-}|\Sigma}}X')
 x=x.replace(r'\unsure{fermés|finies|foncier}',r'\unsure{finies|fermés|fermé}')
 x=x.replace(r'\deleted{\unsure{8}} before 9',r'\deleted{8} before 9')
 e['first_words_or_objects']=x
d['inventory'].append({'element':'Possible earlier horizontal at annotation separator','kind':'deletion','position':[709,627,757,655],'first_words_or_objects':r'X\unsure{\deleted{-}}\setminus\Sigma_1^+','sheet_kind':'text','hand':'his hand','transcribed':'yes'})
d['unresolved']=[]
for f in d['findings']:
 if r'\unsure{' in f['reading']:
  d['unresolved'].append({'place':f['place'],'reading':f['reading'],'alternatives':'Alternatives and uncertain state are explicit in the retained reading; all three independent readings are recorded in the changes table.','confidence':f['confidence'],'reason':f['evidence'],'finding_id':f['id']})
d['notation']=[{'scan':35,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [1,3,5,6,9,11,12,13,14,15,16,18,24,25,26,27]]
d['abbreviations']=copy.deepcopy(rs[0]['abbreviations'])
notes=[
'This handwritten continuation begins d’où. The readers observed no date, independent title or author page number. The pencil 34 is retained as archive numbering. There is no separate drawing or diagram; the arrow belongs to the canonical-application display.',
'The opening source passage gives the complement expression, a disjoint-sum formula and two Pi pairs. Its conclusion begins alors and visibly writes Pi1=Pi3, although the preceding pairs bear indices 1 and 2. That mismatch prompted local inspection; the two-turn 3 is preserved. The separator after contrairement consists of two stacked dots, recorded as a colon.',
'The annotation beneath the second member of Pi1 contains parallel strokes and a complement expression. Its rewritten low index and older layer remain uncertain. An older horizontal or Sigma remnant survives across X, and a further horizontal crosses the following separator. These marks are retained with uncertainty over identity or written state. H explicitly acknowledges rewriting of the low index, so no state-only omission is claimed at that subscript.',
'The heading Corollaire is crossed and underlined; Proposition is added above it. The source text reads non panachées and underlines unique. It displays an ordered pair whose first superscript is T-shaped, retained as top/plus, followed by the empty-intersection formula. The source presents this as a proposition. Its truth has not been independently checked here. Two separate left marginal emphasis strokes and the unpunctuated formula ending are preserved.',
'The lower passage labels the displayed definition of C as (17), calls it l’ensemble somme, qui a quatre éléments, and introduces an application canonique and the four written signed Sigma entries. Both low rounded forms in (17) are read as omega. The target capital remains fraktur/calligraphic P uncertain. Its subscript is retained as finies first, with fermés and fermé; the late dot and compressed letter run govern this reading. No statement about the intended class of subsets is substituted for those letters.',
'The left label (18) has a readable older 7 and the left label (19) a readable older 8. The final inline citation retains an uncertain older 7 beneath 8. H acknowledges rewritten labels but does not transcribe the older numerals. At (17), the visible crossed 7 provides no separately readable earlier digit; the general H note does not supply one. The final line reads et laquelle on l’identifie si … est injective, i.e., and the source sentence continues beyond this page.',
'All twenty C doubt IDs have been decided: eleven resolved and nine retained. Additional local uncertainty preserves the Pi/pi case and surviving older strokes. The root compared all three complete texts, detailed findings, inventories and notes and viewed 23 local crops. These notes report source statements and ink comparisons. No mathematical proof check, OCR, external research or compilation was performed.'
]
d['notes']=[{'id':f'scan035-note-{i:02d}','text':x} for i,x in enumerate(notes,1)]
d['check_events']=[{'statement_id':x['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan035','type':'carried as background without fault found','outcome':'Source-account note and local ink/witness comparison only; no independent mathematical verification is claimed.'} for x in d['notes']]
d['sweep']=[]
d['main_crop_views']={'R1':list(range(1,16)),'R2':[3,11],'R3':[14],'main_new':5,'total':23}
d['crop_counts']={'R1':15,'R2':15,'R3':15,'main':5,'total':50}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan035.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'scan':35,'findings':len(d['findings']),'against_C':sum(f['against_C'] for f in d['findings']),'against_H':sum(f['against_H'] for f in d['findings']),'uncertainties':t.count('\\unsure{'),'unresolved':len(d['unresolved'])}))
