from adjudication_helpers import *
d,rs,ts=start(8)
text=ts['R1'].replace(r'section\deleted{\unsure{x|r}}',r'section\raisebox{-.45ex}{\deleted{\unsure{x|r}}}')
text=text.replace(rs['R1']['differences'][9]['reading'],'isomorphism'+rs['R2']['differences'][8]['reading'])
newcrops={2:'01_ont',5:'02_H_e_gap',7:'03_H_H_gap',9:'04_H_Y_gap',13:'05_tautological',14:'06_fot',15:'07_irreductible'}
for i in range(1,16):
 r=row_from(rs['R1'],i)
 r['readers']={'R1':rs['R1']['differences'][i-1]['reading'],'R2':rs['R2']['differences'][i-2]['reading'] if i>1 else r'Thank\unsure{s|x}','R3':rs['R3']['differences'][i-1]['reading']}
 r['crop']='crops/scan008/'+newcrops[i]+'.jpg' if i in newcrops else normal_crop(8,'R1',r['crop'])
 if i==1:r.update(confidence='medium',scan_shows='The final cell has curved s-like residual ink under an x-shaped impression with crossing diagonals and heavy top/bottom terminals. Comparison with the separately inspected cancelled cell after morphism supports cancellation, as R1. Main rejects R2’s unqualified live state and R3’s live-state alternatives, while retaining s/x uncertainty for the obscured letter. This is a decision from the crossed impressions, not a grammatical correction of Thanks you.')
 elif i==3:r['scan_shows']='The y is clear. The preceding cell has a tall left stem, lower bowl and crowded internal upright; b is favoured, but h remains possible. All readers and main narrow C’s uncertainty to this one letter without inventing an overtyping chronology.'
 elif i==4:r.update(confidence='low',scan_shows='A separate extra cell after the last m contains crossing diagonals over residual curved strokes. Its cancelled state is definite, but the original character remains s/x. The C doubt is retained, and H’s omission loses the cancelled cell.')
 elif i==6:r.update(final=r'section\raisebox{-.45ex}{\deleted{\unsure{x|r}}}',confidence='low',scan_shows='The extra cell is distinctly lower than the section baseline. Two crossing diagonals and broad serif-like terminals make x the strongest visible shape; an underlying r cannot be isolated securely. Main adopts R1/R3’s candidate order and the lowered placement recorded by R2/R3, retaining the alternative.')
 elif i==8:r.update(place='Paragraph 2, initial 3 of 3.6',scan_shows='The numeral has a flat/angular upper stroke, inward diagonal and rounded lower hook, with a worn type-like impression at a regular numeral position. The other three references, inspected in crop08, repeat this form. All readers favour typed 3 over handwritten 3 but retain physical-state uncertainty. The numerical value is certain; C’s candidate order is changed. The three later physical-state changes are recorded separately below.',crop=r['crop']+'; readers/scan008/R1/crop08_later_3s.jpg')
 elif i==10:r.update(final='isomorphism'+rs['R2']['differences'][8]['reading'],scan_shows='A round baseline point has the form and ink of surrounding typed periods. A separate oblique stroke rises to its right, crosses its left portion and extends below it. The final preserves the typed point and the added stroke with inline TikZ. C attributes the entire ! to handwriting; H omits the added stroke. All readers identify the composite; proportional overlay differences are not separate reading changes.')
 elif i==11:r.update(confidence='high',scan_shows='A faint but separate n cell follows e, with two upright remnants and an upper shoulder in the next regular typewriter position. No cancellation crosses it. Main and all three readers resolve C’s then/the doubt to then, despite the resulting wording.')
 elif i==12:r.update(confidence='high',scan_shows='The crossed fragment contains p, r, o, o and meets the photographed paper edge. No f stroke or additional cell is visible beyond the last o. Main and all readers retain only proo and document the physical cutoff. This does not assert what was once present beyond the captured edge.')
 else:r['scan_shows']='Main crop confirms: '+r['scan_shows'].replace('Half a: ','').replace('Half b: ','')
 if i in [5,7,9]:r['consequential']='H supplies a right arrow in this formula; the scan has an empty slot. The consolidated diplomatic text retains the blank and does not determine an arrow from the mathematical argument.'
 d['rows'].append(r)
for place,value in [('reference 3.7','3.7.'),('first reference 3.8','3.8.'),('second reference 3.8, in the parenthesis','3.8.')]:
 d['rows'].append(dict(place='Paragraph 2, '+place,c=r'\handwritten{3}'+value[1:],h=value,final=value+' [typewriter-first state; doubt declared at 3.6]',against_c=True,against_h=False,kind='other',marked_in_H=False,confidence='medium',scan_shows='This 3 has the same angular top, inward diagonal, lower hook and type-like wear as the first reference. Main inspected this occurrence in the shared two-line crop. The first-occurrence state doubt governs this recurrence; the change is in the explicit physical-state attribution, not the numeral value or a merely equivalent macro wrapper.',crop='readers/scan008/R1/crop08_later_3s.jpg',readers={k:value+' [same typewriter-first state convention as 3.6]' for k in rs}))
later_references=d['rows'][-3:]
d['rows']=d['rows'][:-3]
d['rows'][10:10]=later_references
d['doubts']=rs['R1']['remaining_doubts']
for u in d['doubts']:
 if 'morphism' in u['place']:u['confidence']='low'
 if 'section' in u['place']:
  u['confidence']='low';u['reading']=r'\raisebox{-.45ex}{\deleted{\unsure{x|r}}}'
d['inventory']=rs['R3']['inventory']
for x in d['inventory']:
 if x['element']=='E03':x['first_words_or_objects']='Cancelled s/x cell after Thank; original letter uncertain, cancellation retained'
# Split the recurring reference element into its four actual locations, interleaving the punctuation addition.
refs=d['inventory'][7];stroke=d['inventory'][8]
parts=[]
for j,(pos,label) in enumerate([('paragraph 2, y979–1020','3.6.'),('paragraph 2, y1197–1236','3.7.'),('paragraph 2, y1266–1309, left','first 3.8.'),('paragraph 2, y1262–1308, right','second 3.8.')]):
 parts.append(dict(refs,position=pos,first_words_or_objects=label+'; numeral 3, typewriter-first with handwritten-state alternative'))
 if j==0:parts.append(stroke)
d['inventory']=d['inventory'][:7]+parts+d['inventory'][9:]
for i,x in enumerate(d['inventory'],1):x['element']=f'E{i:02d}'
d['notes']=rs['R2']['notes']
d['notes']['math_reading_decisions']=[
 'The literal primes, superscript n, equality/minus signs and two D_i subscripts are retained. The three blank arrow slots remain blank; H explicitly says that it supplied arrows editorially. The absent brackets in Y T/(T^n-a) are also not supplied.',
 'Each reader performed the conditional substitution check T=b, a=b^n, giving T^n-a=0. These are three separate targeted checks, recorded as 008-R1-M01, 008-R2-M01 and 008-R3-M01; none verifies the unseen numbered propositions or their hypotheses.',
 'Main check 008-M01 supplies a limited concrete instance: with A=Q[x], b=x and n=2, evaluation gives a section of A[T]/(T²−x²), but the equivariant map from two copies of Spec A is not an isomorphism. In the coordinate map to A×A, both components agree at x=0, so (1,0) is not in the image. This checks the described obstruction where b vanishes; it does not assert failure for every b or verify the hypotheses of 1.16 or 3.6. The written blank slots remain unfilled.',
 'The assertions about 3.7, 3.8, 6.4, regular divisors, normal crossings, inertia groups and the proposed étale-local tameness condition are reported as the author’s claims, without further proof or outside research.',
 'The edge fragment proo is transcribed only to the visible paper boundary. The readable then and the spellings ont, affraid, where too sketchy, intertia, fot and irreductible are preserved without grammatical or mathematical repair.'
]
d['check_events']=[e for r in rs.values() for e in r.get('check_events',[])]+[json.loads((OUT/'reviews/scan008/main_check_event.json').read_text())]
d['abbreviations']=rs['R2']['abbreviations']
d['slips']=['ont; affraid (three occurrences); where too sketchy; then; intertia; fot; irreductible are retained as written.']
d['workflow']=dict(brief='brief_v005_scan008.md',r1_crops=8,r2_crops=11,r3_crops=10,main_crops=7,main_reader_crops_viewed=8,feedback='All three independent returns were compared before main crop adjudication. Main inspected eight existing R1 crops and seven new crops, each once. The same two-line existing crop shows the later three reference numerals; each was inspected and gets a separate state-attribution row. Main adopts R1’s cancellation decision after Thank, R1/R3’s x-first cancelled character after section with its lowered placement, the shared typewriter-first numeral-state uncertainty, and R2’s geometric encoding of composite punctuation. The edge fragment contains no visible final f; all readers agree and main confirms. Brief v006 adds a physical-edge rule and explicit separate records for repeated physical-state changes. No compilation or OCR was used.')
d['main_adjudication_complete']=True
save(d,text)
