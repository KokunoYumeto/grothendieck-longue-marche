"""Root's scan034 decisions; execute only after all detailed returns are compared."""
from pathlib import Path
import copy,json,datetime
w=Path(__file__).resolve().parents[1]
rs=[json.loads((w/f'readers/scan034/R{k}/return.json').read_text()) for k in (1,2,3)]
mp2=[24,25,1,26,27,2,28,3,4,29,29,5,6,7,8,9,10,11,12,13,14,15,16,17,30,31,18,19,20,21,22,23]
# Source IDs reviewed after root read all three complete detailed returns.
mp3=[24,25,1,26,27,2,28,3,4,29,30,5,6,7,8,9,10,11,12,13,14,15,16,17,31,32,18,19,20,21,22,23]
assert len(mp2)==len(mp3)==32
obs={
1:'The complete E2 expression shows a short low upright with a slight high hook under its first Sigma; the next Sigma has a curved 2 and clear right foot. Preserve the written first index 1, in agreement with all three readers and C.',
2:'The final low n-shaped wave ends before the separate de. No additional s body appears. Resolve singular inclusion, as all three readers do.',
3:'The diagonal branch has an arrowhead near E1 and dense zigzag cancellation. Its bottom glyph has an upright oval with flared feet, favouring Omega. The branch is clearly struck, but the glyph’s own cancellation boundary remains uncertain. Retain R1’s explicit identity and state alternatives.',
4:'A tall looped d is followed by a compressed low run and terminal hook. The final letters do not securely separate donc and donne; keep donc first.',
5:'The high sign after Sigma1 is one horizontal without a crossing upright. Preserve the written minus, despite H’s plus.',
6:'Both high groups contain a small closed ring followed by a separate minus. Retain circle/o/zero at the first occurrence and use circle for the recurrence.',
7:'Two separate connective groups occur at different heights. The upper e and crossed t precede the final marginal E1; the lower group belongs to cartésiens et cocartésiens. Keep the marginal et with R1/R3/C and record R2’s omission. Root compared all three existing margin crops.',
8:'The isolated low stroke after E2 and before equality is wider than it is high. Put dash first, retaining an elongated point.',
9:'The article has a tall l, small low enclosure and long returning terminal. Keep les|le with R1; R2/R3’s resolved les is recorded.',
10:'The two adjectives and the lower connective follow the main sentence baseline from left to right. No leader or separate interlinear cartésiens supports H’s stated placement after cocartésiens. Preserve the visible sequence without asserting writing chronology.',
11:'The final cocartésiens ends in its long connected terminal turn. No separate following comma appears. The separately written i.e. is retained at its next-line position.',
12:'The cancelled starter has E’s upright and three bars, plus a low vertical suffix with a short foot. The apparent cross belongs to the E base. Resolve E1 with R1/R2; record R3’s plus alternative.',
13:'The second cancelled E has a short low nub beside the next line’s tall d ascender. Its suffix remains uncertain. Keep E1|E with R1, recording R2’s E-first and R3’s resolved E1. H acknowledges a cancelled letter but does not transcribe its readable body.',
14:'Extra curved and heavy low strokes merge with the current 12. An earlier 2/1 is possible, but its contour and cancellation boundary cannot be separated fully. Preserve uncertainty over both identity and state.',
15:'A short upright and transverse stroke lie inside a denser crossed high knot. Keep the older plus/minus identity uncertain with R1/R3, recording R2’s resolved plus.',
16:'The second factor’s live low 2 has a broad rounded head and right foot. A lower oval and extra upright remain beneath it; retain older 12/1 without supplying a complete old contour.',
17:'Two low digits have curved shoulders, descending bends and rightward feet. Both are 2-shaped, unlike the nearby single upright 1. Resolve the written 22; no 12 is substituted from the other source formulas.',
18:'The raised older sign is crossed by oblique strokes and has a dense central bar with right return. The earlier plus/minus remains uncertain; the cancellation is visible.',
19:'Three horizontal bars are separately visible beneath the parenthesized (13), with light gaps between them. Resolve the three-bar relation.',
20:'The low final index has a short broad shoulder and down-right hook without a separately clear lower foot. Retain 2|1; H’s same primary 2 creates no uncertainty-only collation row.',
21:'A short older horizontal crosses the upper part of the live X. No complete separate Sigma body survives. Put dash first and retain older Sigma and uncertain written state.',
22:'The raised word has distinct P/r and compressed middle runs, so Prouvons/Prenons remains open. Its long bent leader attaches before La. Preserve the insertion and its attachment.',
23:'The light tall upright and broad low return favour capital La, but the leader crosses the head region. Retain La|la with R1/R2, recording R3’s resolved La.',
24:'The initial a is live and separate. The connected ending has a loop, low run, terminal rise and crossing horizontal. Preserve the shared a once and retain uncertainty over suffix identity and cancellation state.',
25:'The first cap joins two near-upright hanging legs with little foot curvature; the second occurrence repeats that structure. Keep Pi/pi uncertain at the first occurrence, Pi first, and use Pi subsequently. The second occurrence was viewed in a new main crop.',
26:'The word after en has a looped d, low e and long curled terminal s, without an x cross. Read des, as all three readers do.',
27:'The short low index is crossed by the cancellation of the inline formula. Its head and foot remain merged with those lines. Retain 1|2; H’s same primary 1 alone adds no collation difference.',
28:'After X and its diagonal separator, a short low horizontal survives beneath a separate raised minus. No full Sigma body, subscript 1 or plus cross is independently visible. Keep dash/Sigma uncertainty and the written high minus.',
29:'The verb after on has flattened separated runs and a terminal rising t. Its middle letters remain insufficiently separated. Retain aurait|avait, with no H difference based only on uncertainty.',
30:'The cancelled starter preserves Sigma, low 1 and an upper-right upright crossing a separate short horizontal. Resolve Sigma1-plus with R2/R3, recording R1’s retained minus alternative.',
31:'The separator after the final X visibly descends from left to right. Resolve setminus with R1/R3, recording R2’s uncertainty about a slanted minus.',
32:'The last low digit has a curved head, descending body and short rightward foot, complete above the page edge. Resolve 2, as all three readers do.'
}
d={'scan':34,'folder':'J81-04','their_page':33,'hua_has':'text','filename':'J81-04_81_scan034.tex','status':'decided','findings':[]}
for i,base in enumerate(rs[0]['findings'],1):
 f=copy.deepcopy(base)
 src=[base,rs[1]['findings'][mp2[i-1]-1],rs[2]['findings'][mp3[i-1]-1]]
 f['id']=f'SP41-034-{i:03d}'
 f['readers']={f'R{k}':s['reading'] for k,s in enumerate(src,1)}
 f['reader_source_ids']={f'R{k}':s['id'] for k,s in enumerate(src,1)}
 f['marked_in_H']='yes' if i==3 else 'no'
 f['crop']=str(Path(f['crop']).relative_to(w)) if f.get('crop') else ''
 f['evidence']='Main reader, cited local crop(s): '+obs[i]
 f['main_adjudication']='All three complete texts and detailed returns compared; root personally viewed the local evidence. See decisions/scan034_main_observations.md.'
 if i==1:f.update(crop='crops/scan034/main_eq13_E2.png',bbox=[1305,105,1660,205],consequential='The first factor in the written E2 definition is Sigma1-plus. H and S propose Sigma2-plus; the written 1 is preserved.')
 if i==13:f['h']=r'No letter in body; note: sous la formule, une lettre biffée.'
 if i in [14,16]:f['h']=r'Live index only; note: dans la première ligne de (15), les indices de $\Sigma_{12}$ sont récrits par-dessus d’autres.'
 if i==17:f['consequential']='The union term in (15) carries the written low index 22. The expected 12 is recorded as a witness proposal, without replacing the two curved digits.'
 if i==19:f['consequential']='The relation beneath the reference (13) has three bars; preserve equivalence rather than H’s two-bar equality.'
 if i==30:f.update(reading=r'\deleted{\Sigma_1^+}',against_C=True,c_doubt_status='resolved',confidence='medium')
 d['findings'].append(f)

accent_source_id='scan034-R3-F033'
assert accent_source_id
accent=next(f for f in rs[2]['findings'] if f['id']==accent_source_id)
f=copy.deepcopy(accent)
f.update(id='SP41-034-033',reading=r'\unsure{derniêre|dernière}',against_C=True,against_H=True,
 kind='abbreviation expanded or spelling modernised',marked_in_H='no',confidence='medium',
 crop='readers/scan034/R1/11_prouvons_La.png',c_doubt_status='none',c_doubt_ids=[],
 readers={'R1':'dernière','R2':'dernière','R3':accent['reading']},
 reader_source_ids={'R1':'reading.tex, sentence after (16)','R2':'reading.tex, sentence after (16)','R3':accent['id']},
 evidence='Main reader, R1 crop 11: the accent has two short joined legs forming a little roof. Keep R3’s derniêre first, with dernière retained; R1/R2 read dernière without doubt.',
 main_adjudication='Root viewed the complete word and its accent in the existing crop; no new crop was made.')
d['findings'].append(f)

label=copy.deepcopy(rs[2]['findings'][33])
label.update(id='SP41-034-035',against_C=False,against_H=False,marked_in_H='no',
 crop='crops/scan034/main_diagram_label.png',bbox=[180,440,290,532],
 readers={'R1':r'\tag*{(14)}','R2':r'\tag*{(14)}','R3':r'\tag*{(14)}'},
 reader_source_ids={'R1':'reading.tex, diagram (14)','R2':'reading.tex, diagram (14)','R3':'scan034-R3-F034'},
 evidence='Main crop shows both parentheses, a straight 1 and crossed 4. H explicitly calls this diagram formula (14); that exact reference supplies the same number attached to the same diagram. The rendering from that note to the diagram tag adds no new reading. Root excludes R3’s proposed H placement row on that explicit mapping, while retaining the written tag.',
 main_adjudication='Root personally viewed the written label and compared the explicit H note. The lower cancelled branch is separately collated in finding 003.')
d['findings'].append(label)
f=copy.deepcopy(rs[1]['findings'][31])
f.update(id='SP41-034-034',c=r'$E_2\subset\Sigma_1^{\circ-}$',
 reading=r'$E_2\subset\Sigma_1^{\circ-}$',against_C=False,against_H=True,marked_in_H='no',
 crop='readers/scan034/R2/03_margin_and_cocartesiens.png',
 readers={'R1':'No comma after the second marginal inclusion.','R2':f['reading'],'R3':'No comma after the second marginal inclusion.'},
 reader_source_ids={'R1':'reading.tex, marginal NB','R2':f['id'],'R3':'reading.tex, marginal NB'},
 evidence='Main reader compared all three existing margin crops. The second inclusion ends with its ring-minus and low 1, with no detached comma after or below the term. Preserve that ending; H appends a comma.',
 main_adjudication='Complete reader texts agree on the absence of the comma; root verified the local line ending.')
d['findings'].append(f)

d['findings'].sort(key=lambda f:f['id'])
t=(w/'decisions/drafts/scan034_main_draft.tex').read_text()
(w/'pages'/d['filename']).write_text(t)
d['inventory']=copy.deepcopy(rs[0]['inventory'])
for e in d['inventory']:
 e['first_words_or_objects']=e['first_words_or_objects'].replace('La dernière relation',r'La \unsure{derniêre|dernière} relation')
 if e['element']=='Cancelled starter in final display':e['first_words_or_objects']=r'\Sigma_1^+'
d['inventory'].sort(key=lambda e:(e['position'][1],e['position'][0]))
d['unresolved']=[]
for f in d['findings']:
 if f['c_doubt_status']=='retained' or f['id'].endswith(('-004','-025','-033')):
  d['unresolved'].append({'place':f['place'],'reading':f['reading'],'alternatives':'The retained reading gives the alternatives, including uncertain written state where applicable; all three readers are recorded in the changes table.','confidence':f['confidence'],'reason':f['evidence'],'finding_id':f['id']})
d['notation']=copy.deepcopy(rs[0]['notation'])
d['notation'].extend([
 {'scan':34,'form':'Cancelled bottom starter','evidence':'R1 crop 16: an upright crosses a short horizontal at the right of the cancelled Sigma, beside its low 1.','reading':r'\deleted{\Sigma_1^+}'},
 {'scan':34,'form':'Accent in derniêre/dernière','evidence':'R1 crop 11: two short joined legs form a small roof above the letter.','reading':r'\unsure{derniêre|dernière}'},
 {'scan':34,'form':'Two adjacent et groups','evidence':'All three existing margin crops: separate upper e/t before the NB’s E1 and lower main-line connective between the two adjectives.','reading':'Retain et in the NB and et in cartésiens et cocartésiens.'}])
for a in d['notation']:
 if a['form']==r'\Pi|\pi':a['evidence']+=' Root also viewed the full second occurrence in crops/scan034/main_second_Pi.png.'
d['abbreviations']=copy.deepcopy(rs[0]['abbreviations'])
notes=[
 'This wholly handwritten working sheet begins “Posons” and has labels (13), (14), (15) and (16). The light pencil 33 is retained as archive numbering. The three readers observed no date, independent title or author page number.',
 'Display (13) defines Sigma12, E1 and E2. Its E2 expression visibly begins with Sigma1-plus. H gives Sigma2-plus, and S SA01-K81-04 proposes that replacement while acknowledging that its earlier crop did not settle the index. Root’s full local expression crop confirms the written 1. The source diagram below places E2 beneath Sigma2-plus and Sigma12; this discrepancy prompted viewing and remains in the source transcription.',
 'The source calls (14) a diagram of inclusions of closed parts of X. The three readers agree on its eight live objects and ten upward arrows. An additional lower arrow toward E1 is crossed by a zigzag and ends at a glyph read first as Omega, with identity and cancellation state uncertain. That tail is typeset. Root also viewed the written label (14), which H explicitly identifies in an editorial note; there is no missing-number finding.',
 'The NB records the intersection of the positive Sigma terms, two more empty intersections, two ring-minus inclusions and the final E1/E2 intersection. The E2 intersection visibly carries Sigma1-minus. Ring identity and the extra dash/point before the last equals remain uncertain. Two separate et groups appear where the margin approaches the main sentence, so both are retained. R2’s proposal to omit the marginal connective is recorded and rejected from the local crops.',
 'The author writes cartésiens et cocartésiens on the main sentence line. H’s note describing cartésiens as above and after cocartésiens is not supported by the observed placement. Two cancelled E starters are preserved: the first is resolved as E1; the second retains E1/E uncertainty. The unnumbered display and (15) give the written intersection and union expressions. Several older indices and raised signs survive beneath retouching.',
 'In (15), the right-hand union term has two 2-shaped low digits, and the relation beneath the reference (13) has three separate bars. These written forms are preserved. S SA01-K81-04’s proposed index 12 is recorded as a proposed mathematical repair, not inserted into the transcription. The low index of the final intersection term and an older horizontal/Sigma under the live X remain uncertain. No proof check of the displayed identities was performed.',
 'Display (16) lists three nonempty intersections. The added word before the following sentence is Prouvons/Prenons uncertain, with its bent leader attached before La. The sentence contains “les deux premières étant évidentes”, the author’s own assessment. Its preceding word retains the visibly roof-shaped accent as derniêre/dernière. This source wording does not certify the relations.',
 'The final paragraph records the author’s argument beginning “Si on a…” and continuing through the two empty E terms, the two named partitions and the live complement formulas. The word partitions is underlined. The phrase reads “en des parties non vides”. The shared a is retained once with uncertainty over the following ending and its cancellation. The abandoned inline formula is preserved with a horizontal remnant under a high minus; the later live formula did not supply missing characters. The cancelled display starter is resolved as Sigma1-plus, and the final separator and low 2 are resolved from their visible strokes.',
 'All 23 C doubts have a recorded decision: six resolved and seventeen retained. Twenty uncertainty loci remain overall, including the marginal connector, the first family glyph’s Pi/pi case and the accent. Root compared all three complete texts, detailed findings, inventories and notes, and viewed 22 local crops. Source-account notes and glyph decisions are recorded as such; no OCR, outside research, compilation or mathematical proof check was performed on this page.'
]
d['notes']=[{'id':f'scan034-note-{i:02d}','text':x} for i,x in enumerate(notes,1)]
d['check_events']=[{'statement_id':x['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan034','type':'carried as background without fault found','outcome':'Source-account note and local ink/witness comparison only; no independent mathematical verification is claimed.'} for x in d['notes']]
d['sweep']=[{'id':'SA01-K81-04 (scan 034 portion)','s':r"Records (13) E_2 = Sigma_1^+ cap Sigma_2^- and (15) Sigma_22, proposing Sigma_2^+ and Sigma_12; says the earlier 150 dpi crop does not settle (13).",'decision':'Confirm the reported written forms: first factor Sigma1-plus in (13), and index 22 in (15). The new local ink views settle those characters. Preserve them in the diplomatic text; neither proposed replacement is adopted as an ink reading. Scan 032’s portion is separately recorded at that page.','evidence':'crops/scan034/main_eq13_E2.png; readers/scan034/R1/08_formula15_right.png. All three independent readers agree on both written indices. No mathematical correction is asserted as a new theorem.'}]
d['main_crop_views']={'R1':list(range(1,18)),'R2':[3],'R3':[3],'main_new':3,'total':22}
d['crop_counts']={'R1':17,'R2':15,'R3':16,'main':3,'total':51}
d['decided_utc']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(w/'decisions/scan034.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'scan':34,'findings':len(d['findings']),'against_C':sum(f['against_C'] for f in d['findings']),'against_H':sum(f['against_H'] for f in d['findings']),'uncertainties':t.count('\\unsure{'),'unresolved':len(d['unresolved'])}))
