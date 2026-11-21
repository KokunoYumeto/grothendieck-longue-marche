from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan012')
S=A.c
ret={
'B00':'The upper token is 1 followed by a large closing parenthesis; the separate lower enclosure contains a serif Roman I. The difference is margin markup, not a different numeral.',
'B02':'The inserted conique is above the cancelled tubulaire and has its own underline. Its last strokes meet the paper edge and are overworked; the first reading keeps that residual doubt rather than making the whole word certain.',
'B03':'The upper absolu and ou cône sur Y groups are inserted, with leaders over de and the cancelled Y. The crossed Y still has a branching upper body. The second crop ends during espace; its shorter ending is a scope difference, not evidence for deleting topologique from the complete line.',
'B04':'The small crossed token is lower and to the right of T; its remaining fork supports a Y-like subscript without permitting certain recovery. The first uncertainty is retained.',
'B05':'The word has the tall initial t, low u, second tall b and terminal e of tube, with a separate underline; the article is le. The alternative base does not account for these two ascenders.',
'B06':'The crossed low word has humps and a final upright, but the middle letters are covered by the strike. Ouvert is a possible outline, not a recoverable complete reading. The explicit cancelled unreadable word is retained.',
'B08':'The interval is followed by a small filled cluster and a short return. Neither a star nor a leftward arrow can be isolated securely from that overworked mark; the present but unidentified token is retained.',
'B09':'The left formula has a mapping bar and a right end; the separate I×T connector ends in a small dark right terminal. Its locally compressed head does not establish a separate headless reading. Formula number and arguments agree.',
'B10':'The right brace encloses a) and b). Before the live T in b), the strike crosses a T-like roof and stem; whether an additional bar belonged to the cancelled glyph remains unresolved. The baseline dot is preserved literally.',
'B12':'The rotated note has sous, a compressed sa/la, forme faible, and the distinct q descender and two l stems of à qui celle-ci donne un sens. The lower word has the en/tr/acc accented sequence of entraînent. It does not contain the alternative ce qui est affirmé reconstruction.',
'B13':'Application has the long pp descenders and later t/i/on under the horizontal strike. Diagramme continues on the same writing line after it, rather than forming an independently raised insertion; the following applications has a final low s.',
'B14':'The inspected square has four objects. The middle crossed label lies on the existing top shaft, not at a new object. That shaft has two rightward heads. The left vertical has upper and lower angular heads, not a lower hook; the right vertical has a lower hook and upper head. The overworked argument and g/f label remain uncertain.',
'B16':'The heavily retraced letter after identifie has a full T roof and descending stem. It is the same overworked T form used in the nearby formula, so the X alternative is not adopted.',
'B17':'The argument of f has a closed a-like counter while the RHS x is crossed, so a|x remains explicitly unresolved. The T in (4) has a roof above its overtraced stem. Formula punctuation and numbering remain as in the first reading.',
'B18':'The cancelled token precedes the separate live T and remains T-like but uncertain. After the span, the continuous cor-res-pond-ent sequence includes a p descender and later d ascender; there is no separate tall l opening a second word lesquelles.',
'B19':'The long strike leaves an initial looped d, low u-like join and final f loop. The proposed du cône f is still only a doubtful recovery; the second reader also cannot recover the middle word, so it does not justify replacing the first candidate.',
'B21':'After l apostrophe, the low o joins a p with a descending return, followed by a separate stop. This supports op. rather than éq.; triviale is intact.',
'B22':'The beginning has the low au/ss/i sequence of aussi. The two outer hooks and their shafts are visible but there are no independent central heads. The I×T connector is a short plain horizontal. Literal geometry is retained.',
'B23':'Two vertically separated dots follow isomorphe, with no a body; the written colon is retained. The curled C and the single unheaded f connector agree with the first reading.',
'B24':'A wider original-image crop restores the area cut off above the second box: a separate dot is plainly above the first T. The word is opération, with an initial round o and p descender; the cancelled comme on remains uncertain. The rest of connu quand on connaît agrees with the first letter sequence.',
'B25':'The formulas have a small open ring over the first T and a filled dot over the removed boundary T. The text after et has the compressed no/t/on/s sequence, followed by que on a lower line; no independent r termination establishes noter. The interval ends with an open bracket.',
'B26':'Two thin numeral-1 strokes form the lower marginal 11. The second margin wrapper does not change the reading.',
'B27':'The compressed middle curve favors the formula number 2; its poor separation still leaves the earlier b alternative possible. It occurs once beside the square, not as an extra token in the rotated NB.',
'B28':'The full paragraph has repeated serif I forms and the same curled C(f). The final abbreviation is op. with a descending p, as in the overlapping B21. Les axiomes begins outside the first selected span and is already present once in the source.',
'B29':'The supplied box actually covers Soit. A wider original-image crop visibly contains a separate circled 1 immediately to its left, followed by Soit. This is a box-scope mismatch; neither token is duplicated or removed.'}
# Targeted enlarged views were personally inspected before serialization.
im=Image.open(W/'crops/150_scan012_second_B15.png')
for name,box in [('openleft',(0,.35,.64,.62)),('openright',(.48,.36,1,.64))]:
 b=tuple(int(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(box))
 im.crop(b).save(W/f'crops/150_scan012_root_{name}.png')
im.crop((1270,640,1860,900)).save(W/'crops/150_scan012_root_bij.png')
im=Image.open(W/'crops/150_scan012_second_B11.png')
im.crop((1620,390,2200,815)).save(W/'crops/150_scan012_root_retraction.png')
im=Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan012.jpg')
im.crop((208,2097,1670,2285)).save(W/'crops/150_scan012_root_B24wide.png')
new11=S['B11']['first'].replace('les pts','les p$^{\\mathrm{ts}}$')
A.replace('laissant les pts','laissant les p$^{\\mathrm{ts}}$')
e11='The full word rétraction has a dotted i and a low on-like continuation, rather than a separate raised o abbreviation. In the following abbreviation, however, the t/s strokes sit above the p body; that visible raised placement is restored. The au group before cours and the rest of the note remain supported.'
A.change('P11',final=new11,evidence=e11,confidence='medium')
A.inventory('E17',first_words_or_objects=new11)
oldf=r'\xrightarrow{\substack{\mathrm{bij.}\\\sim}}'
newf=r'\xrightarrow{\substack{\deleted{\unsure{homéo}}\\\mathrm{bij.}\\\sim}}'
oldtext="et qu'une partie de $T$ est ouverte ssi\n\\deleted{\\unsure{son intersection}} \\inserted{\\unsure{ses images}}\n\\unsure{et} \\unsure{dans $Y$ et ses images dans $\\mathbf{I}\\times\\dot T$}"
newtext="et qu'une partie de $T$ est \\unsure{ouverte|ouvert} ssi ses\n\\deleted{\\unsure{son intersection|intersection}} \\inserted{\\unsure{images}}\n\\unsure{inverses|inverse} dans $\\mathbf{I}\\times\\dot T$ et dans $Y$ le sont"
new15=S['B15']['first'].replace(oldf,newf).replace(oldtext,newtext)
assert new15!=S['B15']['first'] and newtext in new15
A.replace(oldf,newf)
A.replace(oldtext,newtext)
e15='The enlarged rotated note shows a crossed h-leading label above bij., with homéo retained only tentatively. Beneath the formula, ses is on the live baseline before the crossed group; images is raised above the strike. The next line at the left reads inverses/inverse dans I×dot T, and its continuation at the right reads et dans Y le sont. These visible bodies and line positions correct the first reconstruction of the order and its claimed unfinished ending. The final e of ouverte and the last s of inverses remain uncertain; no grammatical completion is supplied from the quotient-topology argument.'
A.change('P15a',final=A.get('changes','id','P15a')['final'].replace(oldf,newf),evidence='The bold serif I and its lower interval, single-roof T, rightward head, bij. and wave are retained. A separate crossed h-leading word lies above bij.; the visible first ascender and low joins suggest homéo without resolving all letters. That cancelled label is restored explicitly.',confidence='medium')
A.change('P15b',place='Star note: revised openness sentence and its line order',final=newtext+'}',evidence=e15,confidence='medium')
A.inventory('E24',first_words_or_objects=new15)
A.inventory('E25',first_words_or_objects=r'\deleted{\unsure{son intersection|intersection}}')
A.inventory('E26',first_words_or_objects=r'\inserted{\unsure{images}}')
base=A.get('inventory','element','E25').copy();base.update(element='E37',position='star note, above bijection arrow',first_words_or_objects=r'\deleted{\unsure{homéo}}');A.append('inventory',**base)
A.update('decisions','id','M0312',reading=r'ses \inserted{\unsure{images}}',decision='undecided',evidence='The root enlarged crop separates live baseline ses from the raised images replacement. The placement is now clear, but all letters of the raised word remain less than certain.',confidence='medium')
A.update('decisions','id','M0313',reading=r'\unsure{inverses|inverse} dans $\mathbf I\times\dot T$ et dans $Y$ le sont',decision='undecided',evidence='The enlarged crop gives the left-to-right continuation inverses/inverse dans I×dot T, then et dans Y le sont. The final s of inverses remains uncertain. The old proposed clause order and absent-predicate claim are withdrawn.',confidence='medium')
A.update('doubts','place','P15 cancelled lower phrase',reading=r'\deleted{\unsure{son intersection|intersection}}',alternatives='son intersection | intersection',reason='The long strike covers most of the old word bodies; the live ses before it does not settle the cancelled wording.')
A.update('doubts','place','P15 raised replacement',reading=r'\inserted{\unsure{images}}',alternatives='images',reason='Images is the raised group; ses is visibly separate on the baseline before the deletion. Some low joins within images remain crowded.')
A.ed['report_removals'].append({'collection':'doubts','match':{'place':'P15 short group before dans Y'}})
A.update('doubts','place','P15 final slanted clause',reading=r'\unsure{inverses|inverse} dans $\mathbf I\times\dot T$ et dans $Y$ le sont',alternatives='inverses | inverse',reason='The enlarged crop resolves the line order and final le sont. Only the final s in inverses remains insecure.',confidence='medium')
A.doubt('P15 crossed label above bij.',r'\deleted{\unsure{homéo}}','homéo; partially unreadable cancelled label','The initial h and following low bodies survive but the strike prevents a complete recovery.')
A.doubt('P15 openness adjective',r'\unsure{ouverte|ouvert}','ouverte | ouvert','The final e cannot be isolated cleanly after the tall t; grammatical agreement is not used to settle it.','medium')
A.update('notes','id','N06',text='Main-reader targeted quotient-topology check: a subset of the pushout is open exactly when its inverse images in Y and I×dot T are open. Root audit of the enlarged rotated note resolves the visible continuation as inverses/inverse dans I×dot T et dans Y le sont; the final predicate is present in the ink. The previous draft claim that it was missing is withdrawn. This independently recovered wording agrees with the quotient-topology check; the check itself did not supply the reading. The crossed label above bij. is recorded separately as doubtful homéo.')
n8=A.get('notes','id','N08')['text'].replace('and the incomplete marginal endings are preserved','and the incomplete NB ending are preserved; the star note has a visible final le sont')
A.update('notes','id','N08',text=n8)
old20=r'\operatorname{source}\unsure{(}f\unsure{)}'
new20=r'\operatorname{source}f'
A.replace(old20,new20)
e20='The crop shows but(f), both inward heads and outer hooks, and the curled C(f). After source the f begins directly; no separate opening parenthesis is visible. The closing side is clipped at the physical edge. Only source f is transcribed, and hypothetical surrounding parentheses are no longer encoded as present ink.'
A.change('P20',final=A.get('changes','id','P20')['final'].replace(old20,new20),evidence=e20,against_c=True,confidence='medium')
A.inventory('E28',first_words_or_objects='Dans cette identification ... applications canoniques ... but(f) ... source f')
A.update('doubts','place','P20 source at physical right edge',reading=new20,alternatives='Possible lost material beyond the physical right edge is not transcribed',reason='Source and the f stem/crossbar are visible, with no independent opening parenthesis; the edge cannot prove what may have been clipped beyond f.',confidence='medium')
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b=='B11':A.decide(b,e11,new11)
 elif b=='B15':A.decide(b,e15,new15)
 elif b=='B20':A.decide(b,e20,S[b]['first'].replace(old20,new20))
 elif b=='B24':A.decide(b,ret[b],crop='crops/150_scan012_root_B24wide.png')
 elif b=='B29':A.decide(b,ret[b],crop='crops/150_scan012_root_opening.png',outcome='Circled 1 retained after wider original-image inspection; the second box itself covers Soit, which is already transcribed.')
 else:A.decide(b,ret[b])
A.append('notes',id='N11',text='Independent second-reading audit: root personally inspected every nonidentical box, plus targeted enlarged portions of the homotopy/star notes and wider original-image crops for B24 and B29. B24 clipped the dot above T; B29 covered Soit rather than the circled 1. The fixed first and second readings are preserved, and final changes are recorded separately.')
A.append('check_events',statement_id='150012_audit',type='independent_reading_adjudication',outcome='28 nonidentical boxes personally inspected; 3 revised; geometric, cancellation and box-scope differences adjudicated.')
A.save()
