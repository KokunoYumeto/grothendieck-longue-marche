from adjudication_helpers import *
d,rs,ts=start(9)
text=ts['R1'].replace('introduce connected',r'introduce conne\unsure{\deleted{f}c|\deleted{c}f}ted')
text=text.replace(r'\scanpage{9}',r'\scanpage{9}'+'\n'+r'\normalmarginpar')
cropmap={1:'readers/scan009/R3/crops/01_date.jpg',2:'crops/scan009/01_inserted_n.jpg',3:'readers/scan009/R2/crops/02_already.jpg',4:'readers/scan009/R1/crops/02_normality.jpg',5:'readers/scan009/R1/crops/04_really_edge.jpg',6:'readers/scan009/R1/crops/03_reference.jpg'}
for i in range(1,7):
 r=row_from(rs['R1'],i,crop=cropmap[i])
 r['readers']={k:rs[k]['differences'][i-1]['reading'] for k in ['R1','R2']}
 r['readers']['R3']=rs['R3']['differences'][(i if i<=3 else i+1)-1]['reading']
 if i==1:r['scan_shows']='The upper-right note is physically present. The crop shows thin upright/oblique traces, a crossed middle form and terminal 67-like strokes, but strongly amplified JPEG/chroma blocks obstruct precise separation. Main retains C/R1/R2’s whole-date doubt and all four candidates; R3’s narrower scope would imply greater security for the other characters than this evidence supports. No date is selected from chronology. The unsuccessful enhancement is retained and not repeated.'
 if i==2:r['scan_shows']='The six baseline cells read c-o-n-t-e-d. A separate raised serif n stands above the interval before d, completing contend. Its typewriter-like form is clear; H omits the insertion.'
 if i==3:r['scan_shows']='The open e is fourth and the closed a bowl fifth in A-l-r-e-a-d-y. There is no transposition mark; H reverses the two letters.'
 if i==4:r.update(confidence='low',scan_shows='A separate extra cell between i and t contains crossing diagonals and heavy upper/lower terminals. The x-like cancellation is clear; residual curved ink does not securely identify the original letter. C’s x/s uncertainty is retained, and H’s omission loses the cell.')
 if i==5:r['scan_shows']='The full y and its descender are visible, followed by a narrow strip of paper and its edge. No separate point or comma survives to the right or below the ending. H’s terminal period is unsupported.'
 if i==6:r['scan_shows']='The final numeral cell contains an angular 4-like diagonal/crossbar and a 5-like curved lower bowl, followed by a separate period. Main confirms both visible impressions and retains both correction orders. The stronger lower curve favours the displayed 5, but does not establish chronology. C’s doubt is retained.'
 d['rows'].append(r)
r=row_from(rs['R3'],4,crop='readers/scan009/R3/crops/05_connected_etale.jpg')
r['readers']={'R1':'connected','R2':'connected','R3':r['final']}
r['scan_shows']='The second c position contains a low open bowl and a distinct taller hooked impression that rises above it and descends through the cell. Main confirms R3’s additional f-like impression, which both witnesses and R1/R2 omit. The darker low c favours f-to-c correction, but the overprint does not securely establish order; both orders are retained locally.'
d['rows'].insert(3,r)
d['rows'].insert(5,dict(place='Paragraph 1, D subscript: prior C notation description',c=r'D_i [prior note calls the small stem dotless]',h=r'D_i',final=r'D_i [dotted i]',against_c=False,against_h=False,kind='other',marked_in_H=False,confidence='high',scan_shows='A separate compact dot lies above the lowered i stem, whose lower serif is also visible. Main confirms R1’s correction of the earlier descriptive note. The actual LaTeX D_i in both witnesses is already correct, so this is a notation-note confirmation rather than a transcription-change count.',crop='readers/scan009/R1/crops/05_subscript.jpg',readers={'R1':r'D_i; explicit dot observed','R2':r'D_i','R3':r'D_i'}))
d['doubts']=rs['R1']['remaining_doubts']+[rs['R3']['remaining_doubts'][1]]
d['inventory']=rs['R3']['inventory']
d['inventory'][0]['first_words_or_objects']='Faint date: 11/4/67 | 17/4/67 | 11.4.67 | 17.4.67'
d['inventory'][5]['kind']='text'
d['inventory'][5]['hand']='typewriter text; underline instrument not established'
d['inventory'][5]['first_words_or_objects']='not Galois, with single underline encoded in body'
d['notes']=rs['R3']['notes']
d['notes']['author_checks']=rs['R1']['notes']['author_checks']
d['notes']['math_reading_decisions']=[
 'D=0 has a plain typed D, two-bar equality and round zero. D_i has an explicitly dotted lowered i; main crop inspection corrects C’s earlier description of a dotless stem without changing its correct LaTeX index.',
 'The overtyped 7.4/7.5 reference retains both correction orders; no unavailable theorem is used to choose the numeral.',
 'R3 and the main reader separately checked the elementary field example Q(∛2)/Q. T³−2 is irreducible, and its derivative has no common root; the real extension misses the nonreal conjugates and is not Galois. Using the finite-separable/étale criterion gives a connected finite étale cover with D=0. Events 009-R3-M01 and 009-M01 record the limited example checks; 009-B01 separately records the geometric criterion used as unreproved background.',
 'This example establishes only the possibility of a connected non-Galois étale cover with empty divisor. The cited proofs of 7.1 and 10.1, the role of normality/reducedness, the proposed generalization and the Lefschetz appendix remain unverified page claims.',
 'The newly detected f/c overprint in connected is a physical reading decision. It is retained with both correction orders, independently of the mathematical expectation of the word connected.'
]
d['notes']['titles_dates_pages']=rs['R1']['notes']['titles_dates_pages']
d['check_events']=rs['R3']['check_events']+json.loads((OUT/'reviews/scan009/main_check_events.json').read_text())
d['slips']=['convienced, if would be safer and your\'s are retained as written.']
d['workflow']=dict(brief='brief_v006_scan009.md',r1_crops=5,r2_crops=5,r3_crops=5,main_crops=1,main_reader_crops_viewed=7,feedback='All three independent readings were compared. Main inspected seven existing reader crops and one new crop for the raised n. R3 alone detected the overprint in connected; main confirms it and retains both correction orders. Main retains whole-date uncertainty rather than R3’s narrowed scope because the enhanced date crop is artifact-dominated. All three formal C doubts remain, and the earlier dotless-i description is corrected without changing D_i. The faint-date enhancement failure prompted optional luminance-only cropping for later graphite targets; existing crops and returns remain unchanged. No OCR or compilation was used.')
d['main_adjudication_complete']=True
save(d,text)
