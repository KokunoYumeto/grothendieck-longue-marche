#!/usr/bin/env python3
"""Record root's visual decisions for scan 078; no text recognition."""
from pathlib import Path
import json,copy
b=Path('/workspace/scratch/b9993b8b5640');o=b/'out';p='A57-02_57_scan078';rp=o/'readers'/p;ap=o/'adjudication'/p
r={n:json.loads((rp/n/'report.json').read_text()) for n in ['R1','R2','R3']}
m2=[0,1,1,2,3,4,5,6,7,8,9,10,11,12,13,None,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
m3=[0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
fn=['02_top_left','01_top_right','01_top_right','02_top_left','01_top_right','03_separator','04_deleted_ab',None,'05_field_because','05_field_because',None,None,None,'06_orr_deletion',None,None,None,'06_orr_deletion','06_orr_deletion',None,'07_problem_suffix',None,None,None,'08_empty_whether','08_empty_whether','09_product','09_product','09_product','09_product','10_cancelled_x',None]
paths=[str(rp/'R1/crops'/(x+'.png')) if x else None for x in fn]
for i,name in [(7,'affine_period'),(10,'affine_exclamation'),(19,'second_couterexample'),(21,'finite_morphism_transposition'),(22,'finite_morphism_transposition'),(23,'finite_morphism_transposition'),(31,'final_comma')]:paths[i]=str(ap/(name+'.png'))
for i in [11,14,15]:paths[i]=str(rp/'R2/crops/06_simple_insertion.png')
paths[12]=str(rp/'R3/crops/c05_valuation.png');paths[16]=str(rp/'R2/crops/05_margin.png')
small_oval=r'\draw (-0.18,0.13) arc[start angle=135,end angle=480,x radius=0.25cm,y radius=0.18cm];'
large_oval=r'\draw (12.10,-0.236) arc[start angle=320,end angle=670,x radius=2.48cm,y radius=0.43cm];'
amb_or=r'\unsure{orx|or\deleted{r}|orr}'
shows=[
 'The single underline ends beneath the final y of Corollary. The typed 2 has no underline. H includes the numeral inside its emphasis.',
 'There is an upper point and a lower comma-like curved component after condition. The lower tail favors a semicolon but is not clean enough to exclude a colon beside the dense cancellation. The cancelled next character starts immediately after the punctuation without a blank typewriter position.',
 'The typed x cancellation leaves parts of a, the raised prime, closing parenthesis, for and every. Dense overlap and clipping at the right edge leave the entire proposed clause uncertain.',
 'The crossed left continuation retains candidate any and X prime at its beginning and a legible terminal for. Between them the overstruck bodies remain unreadable. No blank separating the tentative X prime from the following unreadable run can be established, so the C/R3 boundary is retained.',
 'The visible word reaches exist at the dark right edge. The last t is partly clipped, and the image cannot settle whether a further s followed. Exist is the first supported reading; exists remains explicit.',
 'Between X prime and S_1 the pen stroke is upright, with only a slight rightward bend at its lower end. The vertical-bar reading is resolved from this shape.',
 'The cancellation line crosses the B and ends in a rounded short terminal above the letter baseline. There is no separate baseline full stop after B.',
 'The paired closing quotation strokes are followed by one empty typewriter position before a separate full stop.',
 'The middle letter bodies are overprinted and have small high cap/diagonal remnants. The first raised mark favors the acute-like reading, with the grave-like alternative still possible. The C/R1/R3 order fiéèd, fièèd, field is retained; individual chronological layers cannot be recovered.',
 'The second letter in because has a curved body and internal horizontal bar, supporting e. It is followed by the open c; the H bccause reading is not followed.',
 'A full blank typewriter position separates the terminal e of affine from the upright and detached point of the exclamation mark.',
 'The o of over occupies the next typewriter position after the comma following say; there is no intervening blank.',
 'Beneath the x cancellation the v/a shapes, tall l, u/a, crossed t, dotted i and terminal o/n bodies support valuation. The word is recoverable.',
 'After the hand-drawn closing square bracket, the comma occupies a later position with a visible blank between. The handwritten brackets themselves are retained.',
 'A handwritten oval surrounds simple. It is reproduced in TikZ; H mentions the circling in its editorial note but gives only the word in its transcription.',
 'A curved bracket runs below the raised projective and, and a slanted stroke descends to the left of the circled simple. Both strokes and the relative positions of the typed words are reproduced; neither has an arrowhead.',
 'The small marginal reference is one oval-shaped stroke with a visible opening at its upper-left portion. The final drawing preserves this opening and the note at the left margin. C/R1/R3 draw a closed ellipse; R2 records an open arc, and H uses two parentheses.',
 'The o and first r after the comma are clear and remain live. The third character has crossing x-like diagonals, with a possible underlying r. Root places the visible orx first and retains cancelled-r and live doubled-r alternatives. H strikes the complete or; that does not represent the uncrossed first two letters.',
 'The crossed phrase retains i/f, a capital X with a raised trace, and parts of finite. Dense x overtyping still obscures several bodies, so the C uncertainty remains.',
 'After provide a the letters are c-o-u-t-e-r-e-x-a-m-p-l-e. The t follows u directly; there is no n position.',
 'A nearly solid blackened cell follows the legible m of problem. Its cancellation is visible, while an underlying s remains only tentative.',
 'The phrase for a finite morphism is typed at the right after descent. Its drawn return line turns down at the boundary immediately after problem and before raised. The final TikZ keeps the physical right-hand position and shows this attachment.',
 'An elongated oval surrounds for a finite morphism, with a small visible opening at the lower-right. The final open arc preserves this detail; neither witness draws the enclosure.',
 'The long pen line runs left above raised in my first talk on descent and turns down after problem. Its right end meets the left portion of the circled phrase; no arrowhead is visible.',
 'The final o bowl and r shoulder of or remain visible under the x cancellation after the empty. H omits these cancelled letters.',
 'After set an upper point stands above a separate lower comma-shaped tail: a semicolon.',
 'Six typewriter positions read w-h-e-t-e-r. The sole tall stem between the first e and the second e belongs to t; there is no intervening second h. Root follows R2 and H on wheter.',
 'The product character after X is a lowercase serifed typewriter x at the baseline, followed by a lowered S. This records the visible glyph without changing the mathematical claim.',
 'After F the congested sign has a rounded upper curve, a diagonal middle and a broad low foot favoring 2 visually. Crossing internal traces remain, so x and tensor-sign alternatives are retained. A definite tensor sign is not established by the ink.',
 'The final S prime is followed by a blank typewriter position before the full stop. The product-sign uncertainty is recorded separately.',
 'Under the pen cancellation the typed upper serifs and diagonal remnants support X. Root follows R1/R3 and H, at medium confidence because the lower part is heavily covered.',
 'The final punctuation has a rounded upper body and a descending curved tail below the baseline. The page ends with a comma.'
]
conf=['high','low','low','low','medium','high','high','high','low','high','high','high','high','high','high','high','high','low','low','high','low','high','high','high','high','high','high','high','low','high','medium','high']
finals={1:r'condition\unsure{;|:}\deleted{\unsure{a\prime) for every}}',3:r"\deleted{\unsure{any $X'$}\illegible{2} for}",16:small_oval,17:'birational,'+amb_or,22:large_oval,26:'wheter'}
# Preserve the literal prose prime in the displayed record as in the transcription.
finals[1]=r"condition\unsure{;|:}\deleted{\unsure{a') for every}}"
changes=[]
for i in range(32):
 reads={'R1':r['R1']['changes'][i]['reading'],'R3':r['R3']['changes'][m3[i]]['reading']}
 if m2[i] is not None:reads['R2']=r['R2']['changes'][m2[i]]['reading']
 else:reads['R2']=r'curved insertion bracket under projective and; descending slanted stroke left of simple (drawn in reading.tex)'
 if i==2:reads['R2']=r"\deleted{\unsure{a') for every}}"
 if i==3:reads['R3']=r"\deleted{\unsure{any $X'$}\illegible{2} for}"
 x={'source':['R1',i],'reader_readings':reads,'evidence':paths[i],'crop':paths[i],'scan_shows':shows[i],'confidence':conf[i],'mathematical_consequence':None}
 if i in finals:x['final']=finals[i]
 if i==16:x['differs_c']=True
 if i==26:x.update(differs_c=True,differs_h=False)
 if i in [14,15,16,21,22,23]:x['h_marked']='no'
 if i==28:x['mathematical_consequence']='The F base-change operator is unresolved between the visible 2-like impression, x and a tensor sign; H supplies a definite tensor sign.'
 changes.append(x)
margin_show='The handwritten exclamation shaft and its detached point are separated from the end of smooth by a visible gap. Root follows R2 on smooth space exclamation, at medium confidence because handwritten spacing is uneven.'
changes.insert(17,{'source':['R2',15],'reader_readings':{'R1':'$X$ smooth!','R2':'$X$ smooth !','R3':'$X$ smooth!'},'final':'$X$ smooth !','evidence':paths[16],'crop':paths[16],'scan_shows':margin_show,'confidence':'medium','mathematical_consequence':None})
cd=copy.deepcopy(r['R1']['c_doubts'])
for d,i in zip(cd,[2,3,3,4,5,8,18,20,28,30]):d.update(evidence=shows[i],crop=paths[i],confidence=conf[i])
remaining=[]
for j,d in enumerate(copy.deepcopy(r['R1']['remaining_doubts'])):
 if j==9:continue
 i=[1,2,3,3,4,8,17,18,20,26,28][j]
 d.update(reason=shows[i],crop=paths[i],confidence=conf[i])
 if j==6:d.update(place='L15, third character after or and cancellation state',reading=amb_or,alternatives=['orx',r'or\deleted{r}','orr'])
 remaining.append(d)
inv=copy.deepcopy(r['R1']['inventory'])
inv[12]['first_words_or_objects']='nearly closed oval reference with upper-left opening'
inv[13]['first_words_or_objects']='impossible if / X smooth !'
inv[20].update(kind='text',first_words_or_objects='or followed by uncertain live x / cancelled r / live r')
inv[25]['first_words_or_objects']='elongated oval with small lower-right opening'
inv.insert(34,{'sheet_kind':'letter','hand':'another unnamed hand','element':'pending','kind':'insertion','position':'L24, coherent F prime','first_words_or_objects':'handwritten raised prime after typed F','transcribed':'yes'})
notes={'summary':'The page continues the letter with Corollary 2, a statement about the Picard prescheme after shrinking the base. Its N.B. records a limitation of the preceding proof, requests a counterexample in specified settings, and links the request to the effectivity problem for a finite morphism. A marginal annotation objects beside the word simple. The lower paragraph describes Problem A through a flatness functor and refers to the author\'s Hilbert-scheme existence argument. These are attributed descriptions of the page; no proof verification was performed.',
 'reading_decisions':[{'place':'L05, X prime and S_1','readings':r'\mid versus /','reason':shows[5]},{'place':'L18, finite-morphism phrase','readings':'phrase after descent versus attachment after problem','reason':shows[21]},{'place':'L22, base-change expressions','readings':r'X\mathbin{x}_S S\prime and F\unsure{2|x|\otimes}_S S\prime','reason':shows[27]+' '+shows[28]}],
 'author_checks':[{'place':'N.B., L10–L11','quote':r"The proof does not give any evidence towards the fact that in the theorem, one could replace ``quasi-affine'' by ``affine'' ."},{'place':'L13','quote':'It would be interesting to have a couterexample'},{'place':'Left margin','quote':'impossible if / $X$ smooth !'}],
 'titles_dates_pagination':copy.deepcopy(r['R2']['notes']['titles_dates_pagination']),
 'layers':'The cancelled opening, field overprint, disputed character after or, cancelled if-X-prime-finite phrase, blackened suffix of problem and F-product retain their unresolved readings. The six-letter wheter and the cancelled X are resolved from their visible letters. The hand-drawn prime after coherent F is identified as handwriting; its glyph was already present in both witnesses.',
 'drawing_encoding':'The raised projective and, its bracket and connector, the circled simple, the marginal open oval, and the circled finite-morphism phrase with its return line are reproduced in TikZ. The transposed phrase remains at its physical right-hand position while the line records its attachment after problem. The marginal note is placed at the left.'}
notation=copy.deepcopy(r['R1']['notation'])
notation += [{'sign':'small marginal reference oval','latex':small_oval,'place':'Left margin beside L14','visible_shape':shows[16],'alternatives':[]},{'sign':'finite-morphism enclosing oval','latex':large_oval,'place':'L18','visible_shape':shows[22],'alternatives':[]},{'sign':'handwritten prime on typed F','latex':r"F\handwritten{'}",'place':'L24, coherent F','visible_shape':'A thick slightly curved raised hand stroke follows the typed F; its texture and shape differ from the rectangular typed primes visible nearby.','alternatives':[]}]
prior=copy.deepcopy(r['R1']['prior_flags']);prior[2]['finding']=shows[17]
repl=[(r'condition\unsure{;|:} \deleted',r'condition\unsure{;|:}\deleted'),(r"\unsure{any $X'$} \illegible",r"\unsure{any $X'$}\illegible"),(r'\draw (0,0) ellipse (0.25cm and 0.18cm);',small_oval),('smooth!','smooth !'),(r'\margin{\handwritten{\figure',r'\reversemarginpar'+'\n'+r'\margin{\handwritten{\figure'),(r'\noindent over',r'\normalmarginpar'+'\n'+r'\noindent over'),(r'or\deleted{\unsure{r}}',amb_or),(r'\draw (10.20,0.04) ellipse (2.48cm and 0.43cm);',large_oval),(r'\unsure{whether|wheter}','wheter'),("coherent $F'$",r"coherent $F\handwritten{'}$")]
cfg={'base_reader':'R1','replacements':[{'old':a,'new':z} for a,z in repl],'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inv,'notes':notes,'notation':notation,'prior_flags':prior,'adjudicated_crops':list(dict.fromkeys(paths)),'reader_only_decisions':[{'place':'L24, prime after coherent F','reader_readings':{'R1':r"F'",'R2':r"F\handwritten{'}",'R3':r"F'"},'final':r"F\handwritten{'}",'evidence':paths[30],'scan_shows':'The same raised prime is transcribed by every reader and witness. R2 identifies its manuscript provenance; root follows that wrapper from the curved thick hand stroke. No glyph difference is counted.'}],
 'rejected_difference_rows':[{'source':'R2 changes 16–17; R3 changes 18–20','reason':'The overlapping word, cancellation and comma-boundary entries are represented together by the single adjudicated birational,or... place; the three letters and no-space boundary are not counted repeatedly.'},{'source':'R3 changes 3–4','reason':'The initial and terminal recoverable parts of one cancelled continuation are included in the full continuation row, with the intervening unreadable text preserved.'}]}
(ap/'decision.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2))
with (o/'notation.md').open('a') as f:
 f.write('\n## Evidence added at cote 57, scan 078\n\n| Sign | Reading | Place | Visible form / residual alternatives |\n|---|---|---|---|\n')
 for n in notation:f.write('| '+n['sign']+' | `'+n['latex'].replace('|',r'\|')+'` | '+n['place']+' | '+n['visible_shape'].replace('|',r'\|')+' |\n')
brief=(o/'briefs/reader_brief_v07.md').read_text().replace('brief v07','brief v08',1).replace('First used: cote 57, scan 078.','First used: cote 57, scan 079.',1)
brief+='\n\n## Clarifications introduced in v08\n\n- Reproduce a visible opening in an oval rather than automatically closing the curve. On scan 078, the marginal oval and the finite-morphism enclosure have small openings. Preserve the side of marginal notes with standard LaTeX placement controls when needed.\n- A possible cancellation of one extra character must not force a cancellation of the adjacent live word. Keep character identity and cancellation-state alternatives explicit when the overprint does not separate them.\n- In comparing full readings, inspect compact typewriter spellings by their visible character positions; do not let a familiar spelling supply a missing letter.\n'
(o/'briefs/reader_brief_v08.md').write_text(brief)
f=o/'records/brief_changes.json';v=json.loads(f.read_text());v.append({'version':'v08','first_page':'A57-02_57_scan079','reasons':['Scan-078 readers varied between a closed marginal oval and an open arc; root also preserved the opening in the finite-morphism enclosure. Placement and visible gaps in drawing strokes are explicit.','Readers disagreed on the extra character after or and on wheter/whether. The brief now emphasizes independent character/cancellation alternatives and visible typewriter positions.']});f.write_text(json.dumps(v,ensure_ascii=False,indent=2))
print('Page 078: 33 change rows, '+str(len(remaining))+' doubts, '+str(len(inv))+' inventory elements, '+str(len(set(paths)))+' root-viewed crops.')
