from adjudication_helpers import *
d,rs,ts=start(5)
text=ts['R1'].replace('mentioning it because','mentioning it, because').replace("`new numbering'",r"\unsure{`|``}new numbering'").replace('ordinary group : same reason',r'ordinary group \unsure{.:|:} same reason')
map2={**{i:i for i in range(1,18)},18:19,20:23,21:20,22:21,23:22,24:24}
map3={**{i:i for i in range(1,19)},20:22,21:19,22:20,23:21,24:23}
new={1:'01_heading.jpg',2:'01_heading.jpg',10:'02_underline.jpg',12:'03_you.jpg',13:'04_hyp_gap.jpg',14:'05_subtle.jpg',17:'06_p5_label.jpg'}
existing={4:('R2','crops/02_in_stead.jpg'),5:('R2','crops/02_in_stead.jpg'),6:('R2','crops/14_it_comma.jpg'),11:('R2','crops/06_numbering_quotes.jpg'),16:('R3','crops/08_hyp1.jpg'),18:('R2','crops/09_same_reason.jpg')}
for i in range(1,25):
 r=row_from(rs['R1'],i)
 r['readers']={'R1':rs['R1']['differences'][i-1]['reading'],'R2':rs['R2']['differences'][map2[i]-1]['reading'] if i in map2 else 'with','R3':rs['R3']['differences'][map3[i]-1]['reading'] if i in map3 else 'with'}
 if i in new:r['crop']='crops/scan005/'+new[i]
 elif i in existing:r['crop']=normal_crop(5,*existing[i])
 else:r['crop']=normal_crop(5,'R1',r['crop'])
 r['scan_shows']=r['scan_shows'].replace('Half A:','Main crop:').replace('Half B:','Main crop:')
 if i==6:r.update(final='without mentioning it, because',against_c=True,against_h=False,scan_shows='A detached curved descending stroke lies below and to the right of it, separate from the t. Main inspection supports R2 and H against C/R1/R3: the comma is present.',confidence='high')
 if i==7:r['confidence']='low'
 if i==11:r.update(final=r"\unsure{`|``}new numbering'",against_c=True,against_h=True,confidence='medium',scan_shows='Each raised quotation cluster has one dominant stem with a short side branch. Main inspection favors a single hooked quote, as R1/R3, but two fused ticks, as R2, cannot be ruled out. Both multiplicities are retained locally, single first; the closing mark follows that first candidate.')
 if i==18:r.update(c='same reason [no terminal period]',h='same reason.',final='same reason [no terminal period]',scan_shows='The final n ends in a connected upward/rightward exit. No separate final period follows it. The earlier same/some doubt is adjudicated separately below.')
 if i==19:r['scan_shows']+=' Main comparison with the smaller w of word favors the capital first while retaining case uncertainty.'
 if i==20:r['scan_shows']+=' Main inspection confirms the internal point and localizes remaining doubt to the terminal mark. The oval and note are kept beside Originally; R2’s end-of-paragraph placement is not adopted.'
 if i==21:r['scan_shows']+=' Main inspection favors the visibly low oval point, while allowing a very short low hyphen.'
 if i==23:r['confidence']='low'
 d['rows'].append(r)
r=row_from(rs['R2'],18,confidence='low',crop='readers/scan005/R2/crops/09_same_reason.jpg')
r['readers']={'R1':':','R2':r'\unsure{.:|:}','R3':':'}
r['scan_shows']='In addition to the two vertically aligned colon points, a separate faint baseline point lies to their left. Main inspection confirms the physical mark, but its status as punctuation rather than an incidental touch is unresolved. Retain .:|:, low confidence.'
d['rows'].insert(17,r)
d['rows'].insert(19,dict(place='p.5 comment: same/some doubt in C',c=r'\unsure{same|some}',h='same',final='same',against_c=True,against_h=False,kind='other',marked_in_H=False,confidence='high',scan_shows='After s, the open a has a bowl and lower-right tail, followed by clear m and e. All readers and main inspection resolve the C doubt to same; this row records removal of the doubt mark even though the preferred letters are unchanged.',crop='readers/scan005/R2/crops/09_same_reason.jpg',readers={k:'same' for k in rs}))
d['doubts']=rs['R1']['remaining_doubts']+[
 dict(place='Quotation marks around new numbering',reading=r"\unsure{`|``}new numbering'",alternatives=["``new numbering''"],confidence='medium',reason='The small branches can be parts of single hooked quotes or fused paired ticks; single is the ink-favoured reading.'),
 dict(place='p.5 comment: point before colon',reading=r'\unsure{.:|:}',alternatives=[':'],confidence='low',reason='A faint additional baseline point is visible to the left of the clear colon, but may be an incidental pen touch.')]
# Inventory retains all text, correction and drawing elements, in vertical order.
inv=rs['R1']['inventory']
order=['E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','E11','E12','E13','E14','E16','E17','E15','E18','E19']
inv=sorted(inv,key=lambda x:order.index(x['element']))
for i,x in enumerate(inv,1):
 x['element']=f'E{i:02d}';x['transcribed']='yes'
 if 'same reason' in x['first_words_or_objects']:x['first_words_or_objects']=r'p.5. line 6 below: the emphasis on H ordinary group \unsure{.:|:} same reason'
 if 'O.K plus' in x['first_words_or_objects']:x['first_words_or_objects']=r'O.K\unsure{-|.}'
d['inventory']=inv
d['notes']=rs['R3']['notes'];d['notes'].pop('workflow',None)
d['notes']['author_checks']=rs['R2']['notes']['author_checks']+['Final unfinished phrase: I don’t see what.']
d['notes']['math_reading_decisions']=[
 'The page attributes results on quotients by ordinary finite groups to the cited seminar material, invokes the purity theorem as a bibliographic reference, and distinguishes a translation of revêtement from covering in a topology. These are the author’s claims and questions; this run does not verify those results or references.',
 'The three readers independently retain the visible series letters SGA X, SGA D and TDTE III and the plain group letter H; no expected bibliographical numbering or group alphabet is supplied.',
 'The singular reason and the word same are resolved from visible endings/vowel strokes, not from the logic of the cross-reference. The cancelled f-like remnant and several punctuation/case details remain explicitly doubtful.'
]
d['check_events']=[]
d['abbreviations']=rs['R1']['abbreviations']
d['slips']=['in stead, made freely references, one notable misleading and is a misleading are retained as written.', 'SGA D is retained from the written letterform; no bibliographic repair is made.']
d['workflow']=dict(brief='brief_v003_scan005.md',r1_crops=12,r2_crops=14,r3_crops=15,main_crops=6,main_reader_crops_viewed=16,feedback='All three whole/half readings and all crop views were independent and single-view. Main compared every returned text, then inspected 16 reader crops and six new crops. One extra reader crop concerned assumption rather than the targeted subtle punctuation; both are documented. R2 alone found the clear comma after it and the possible point before a colon; R1 alone qualified initial W and the name separator. The final keeps ink-supported uncertainty rather than voting. All four formal C doubts receive explicit rows; resolution of same changes the doubt encoding and is counted against C. The circled marginal note remains beside Originally. Brief v004 clarifies doubt-change counting and crop/punctuation handling; original returns are unchanged.')
d['main_adjudication_complete']=True
save(d,text)
