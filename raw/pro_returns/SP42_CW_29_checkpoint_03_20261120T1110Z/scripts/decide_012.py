from adjudication_helpers import *

d,rs,ts=start(12)
text=ts['R1'].rstrip()+'\n'
cropmap={1:'readers/scan012/R1/01_cancelled_B_equals.jpg',2:'crops/scan012/01_display_numerator.jpg',3:'crops/scan012/01_display_numerator.jpg',4:'readers/scan012/R1/02_deleted_fragment.jpg',5:'readers/scan012/R1/03_deleted_This_phrase.jpg',6:'readers/scan012/R1/04_cancelled_example_and_edge.jpg',7:'readers/scan012/R1/04_cancelled_example_and_edge.jpg',8:'crops/scan012/02_considred.jpg',9:'crops/scan012/03_group_bases.jpg',10:'crops/scan012/03_group_bases.jpg',11:'readers/scan012/R1/05_do_overprint.jpg'}
evidence={
1:'The cancelled start retains B’s two bowls and upright, then two horizontal equals strokes. The intervening x crosses the former space; it is a cancellation stroke rather than an additional underlying character. H omits the cancelled B=.',
2:'Clear paper separates A from the first T, and the final lowered r from the slash. Neither bracket position has a vertical or curved bracket stroke. Main confirms that H’s acknowledged editorial brackets have no ink counterpart.',
3:'The first punctuation run is a tailed comma, two separate round points, and a second tailed comma. Main confirms the literal two-point ellipsis; H expands it to three points.',
4:'Five crossed typewriter cells survive. The latter four show the n arch, open c curve, closed o and m strokes. In the first, the lower cup-like trace favours u, but cancellation prevents excluding i. Main agrees with all readers in narrowing C’s doubt to that first cell; no complete word is supplied beyond the five cells.',
5:'T, h, dotted i and s remain legible. After the crossed space, the next cell has the two low valleys and central rising stroke of w. The final x extends the cancellation beyond it. Main accepts R1’s single w and resolves C’s local doubt, at medium confidence; R2/R3 retain doubt, and H’s two-letter is has no separately visible dot-and-s sequence.',
6:'The suffix xample is readable through the cancellation: x/a low forms, m strokes, p descender, tall l and final e. The initial crossed cell has curved and serif-like fragments compatible with e or r. Main retains both candidates but narrows C’s doubt to that cell; preferred letters and deletion state already agree with H.',
7:'After the full a, only the upper-left serif, upright and lower foot of the next cell survive at the paper edge. Main retains r as a locally uncertain candidate for existing ink; its missing right shoulder is not restored.',
8:'The nine separate cells read c-o-n-s-i-d-r-e-d. The first d is followed immediately by r, with no intervening e. H and all three readers preserve the visible spelling; C adds an absent letter.',
9:'A lowered 1 precedes (U, blank), but the base position above/left of that 1 is empty. No pi strokes are visible. Both parentheses and the blank second argument are retained.',
10:'The second expression separately has a lowered 1 and empty base, U, comma and blank second argument. Its raised parenthesized lowercase p is clear. H again inserts an absent pi. A tiny isolated spot near the closing parenthesis does not form a separate legible sign and is not assigned a punctuation value.',
11:'A clear d precedes a cell containing a closed o ring, central i stem with foot, and detached dot. Both components are visible; no directional stroke establishes their order. Main follows R1/R3 in keeping the clear d outside the doubt while retaining both correction orders. H loses the i impression and its correction state.'
}
for i in range(1,12):
 row=row_from(rs['R1'],i,crop=cropmap[i],scan_shows=evidence[i])
 row['readers']={who:rs[who]['differences'][i-1]['reading'] for who in ['R1','R2','R3']}
 if i==5:row['confidence']='medium'
 if i==2:row['consequential']='Retains the unbracketed generator list; removes H’s supplied square brackets.'
 if i==9:row['consequential']='Retains the first empty group base and blank second argument; removes H’s supplied pi.'
 if i==10:row['consequential']='Retains the second empty group base and blank second argument with exponent (p); removes H’s supplied pi.'
 d['rows'].append(row)
d['doubts']=rs['R1']['remaining_doubts']
d['inventory']=rs['R1']['inventory']
d['notes']=rs['R1']['notes']
d['notes']['content']='The concluding typed page of the letter contains the continuation of the regularity claim, one displayed quotient expression, four body paragraphs and With best wishes, without a signature. It discusses the assumptions in 7.1, the use of 7.2, a short proof on page 32, the formulation of tame ramification in 9.4, and the groups in 10.2/10.3. All visible cancellations and the archival 11 are retained. The spellings lemme, analoguous, normalisty, whith and considred remain literal. A conditional main-reader regularity argument is recorded separately; the other cited results remain unverified.'
d['notes']['math_reading_decisions']=[
 'The numerator has no brackets and has two points in its first ellipsis. Both group bases and their second arguments are blank; only the second group carries raised (p). Main personally inspected these positions and supplied no conventional symbols.',
 '012-M01 gives an independent conditional proof of the regularity claim continued from scan011. Assuming positive integer exponents and interpreting the unbracketed expression as a polynomial quotient, monic division gives a finite free A-algebra. Modulo the maximal ideal, all T_i are nilpotent and the quotient is local. The resulting unique maximal ideal is generated by T_1,...,T_r and the remaining parameters, a total of dim A generators; integral dimension preservation then yields regularity.',
 'This argument does not require residue-characteristic coprimality. It does require explicit positive exponents and a polynomial-quotient interpretation, neither of which licenses restoring the absent relation signs or brackets in the diplomatic text. The proof and its limits are in reviews/scan012/main_mathematics.md.',
 '012-B01 and 012-B02 record the integral-extension, Noetherianity and dimension/generator facts used without a fresh proof. No computation or external research was performed. The three independent page readers made visual checks only and claimed no mathematical proof events.',
 'The normality/reducedness assertions concerning 7.1 and 7.2, the inertia-specialization assertion on scan011, the proof on page 32, and the group identifications in 10.2/10.3 remain unverified claims of the letter.'
]
d['check_events']=json.loads((OUT/'reviews/scan012/main_check_events.json').read_text())
d['slips']=['lemme, analoguous, normalisty, whith and considred are retained; cancelled fragments are not expanded into full expected words.']
d['workflow']=dict(brief='brief_v008_scan011.md',r1_crops=5,r2_crops=5,r3_crops=6,main_crops=3,main_reader_crops_viewed=5,feedback='Main compared all three complete returns, viewed the five R1 crops once, and made/viewed three new crops for the numerator, considred, and the two adjacent group expressions. R1’s resolved cancelled w is accepted at medium confidence; the other readers’ retained doubt remains visible in the comparison. Three other inherited doubts are localized but unresolved, and the cut r gains a local doubt. No image was re-viewed. The existing brief handled these differences; it remains unchanged. Main separately checked the regularity claim under explicit interpretation/positivity assumptions, with unreproved background facts separately recorded and no changes to missing ink.')
d['main_adjudication_complete']=True
save(d,text)
