from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan013');S=A.c
ret={
'B01':'The two upper prose lines are crossed. The old parenthesized number is heavily overworked and its cancellation state remains unresolved; neither a clean 5 nor a clean live 6 replaces that uncertainty. NB is underlined and the indexed family and closed interval agree.',
'B02':'The first croissante has compressed middle joins but its terminal te sits on the word baseline; no independently raised suffix is secure. The first definition label has d/e/f bodies without a separate accent, unlike the lower accented label. The cancelled lambda subscript is present; the second reading stops before the continuation Si lambda, already transcribed once.',
'B03':'Two long nearly parallel emphasis strokes are present. In the native page they run vertically beside the interior paragraph. The rotated crop does not change their source orientation; Vert records those two bars without assigning a relation to the prose.',
'B07':'The first E has its roof, middle arm and baseline joined to one upright; the small upper loop does not establish an independent overbar. The second plain E provides a local comparison. The Ep display, underbrace and interval agree.',
'B09':'The inclusion mark has a curved left hook followed by a long shaft and no right head. The second underline visibly begins under Y and extends through dans; it does not begin only at dans.',
'B10':'The operation reference (1) is visibly above the line before I×T. The live raised faisant ... absolu de Y phrase replaces the crossed conditions line; within it tub. is cancelled and coniq. is raised. The final crossed word remains dites./id. rather than the unsupported longer ci-dessus.'}
old4=r'\inserted{top.}'
new4=r'\inserted{\unsure{top.|top}}'
A.replace(old4,new4)
e4='Topologique is inserted with a curved leader over de, which remains live. The second insertion reads top, but its final point cannot be separated securely from the leader and p return; top.|top preserves that narrow punctuation uncertainty without changing the preferred abbreviation.'
A.change('P03_b',final=A.get('changes','id','P03_b')['final'].replace(old4,new4),evidence=e4,confidence='medium')
A.inventory('E07',first_words_or_objects=r'\unsure{top.|top}')
A.doubt('P03 inserted abbreviation stop',r'\unsure{top.|top}','top. | top','A separate final point cannot be isolated from the insertion leader and terminal p return.','medium')
old5=r'\unsure{\deleted{_1}|_1}'
new5=r'\unsure{\deleted{_1}|_1|\deleted{_\lambda}}'
A.replace(old5,new5)
e5='The low token after the circled T has a stem and several retraced bends. The first 1 reading and its uncertain deletion state remain preferred, while a cancelled lambda is a genuine residual possibility in the blurred lower strokes. The phi empty-set form and final Y=T are clear.'
A.change('P04_b',final=A.get('changes','id','P04_b')['final'].replace(old5,new5),evidence=e5,confidence='low')
A.update('doubts','place','P04 overwritten subscript',reading=new5,alternatives='cancelled 1 | live 1 | cancelled lambda',reason='Several low bends and overtracing prevent separation of original subscript and cancellation; no semantic repair settles it.')
A.inventory('E08',first_words_or_objects='Subscript 1 preferred, cancellation state uncertain; cancelled lambda also possible')
old6=r'\deleted{\unsure{E}}';new6=r'\deleted{\unsure{E|\xi}}'
A.replace(old6,new6)
A.replace(r'\text{du bord $\dot T$ de $T$}',r'\text{du bord $\dot T$ dans $T$}')
e6='The phrase after du bord dotted T has d/a/n/s bodies, so dans T replaces de T. The crossed leading symbol has looping portions that also admit xi; E stays the preferred unresolved candidate. The lower thick union-like sign still does not securely distinguish amalg from cup. The first def is unaccented and the lower déf has a separate mark.'
A.change('P05_b',final=A.get('changes','id','P05_b')['final'].replace(old6,new6),evidence='Single-roof T and Ep with raised (T) remain visible. The cancelled initial glyph is E-like but its looped overtracing also admits xi; the candidate is retained with that uncertainty.',confidence='medium')
A.change('P05_c',final=A.get('changes','id','P05_c')['final'].replace('de $T$','dans $T$'),evidence='The word after dotted T has the d ascender followed by distinct low a/n/s joins. It reads dans, agreeing with H at this word; C de is corrected. The paired quotation ticks and epsilon remain unchanged.',against_c=True,against_h=False,confidence='high')
A.update('doubts','place','P05 cancelled E',reading=new6,alternatives='E | xi',reason='The cancelling stroke and loops obscure the upright and arms; neither underlying glyph is fully recovered.')
A.inventory('E11',first_words_or_objects='Crossed doubtful E | xi')
A.inventory('E12',first_words_or_objects='Paired-tick épaississement d’indice epsilon; du bord dotted T dans T')
new8=S['B08']['first'].replace('compact, et les','compact, ? et les').replace(r'\inserted{ouverts}',r"\inserted{\unsure{d'ouverts|ouverts}}").replace(r'\unsure{ainsi que voisinages} tubulaires absolus',r'en tant que voisinages tubulaires \unsure{et} absolus')
A.replace('compact, et les','compact, ? et les')
A.replace(r'\inserted{ouverts}',r"\inserted{\unsure{d'ouverts|ouverts}}")
A.replace(r'\unsure{ainsi que voisinages} tubulaires absolus',r'en tant que voisinages tubulaires \unsure{et} absolus')
e8='The native page and rotated enlargement were both inspected. The apparent crossed symbol after forment is the main-text formula number (6), rotated into this crop; it is not duplicated in the margin. A separate question mark after compact belongs to the marginal line and is restored. The raised replacement over fermés begins with a d/apostrophe-like prefix, hence d’ouverts|ouverts. The parenthesis begins en tant que voisinages, with two t ascenders in tant, then tubulaires and a doubtful et before absolus de Y. The isolated plus/plein : T fragment remains unresolved.'
A.change('P07_b',final=A.get('changes','id','P07_b')['final'].replace('compact, et les','compact, ? et les'),evidence='The crossed les before alors remains tentative; alors T compact is legible. A separate question mark follows the compact comma before the next marginal line et les T_epsilon. T has one roof.',confidence='medium')
A.change('P07_e',final=r"\deleted{\unsure{fermés}}\inserted{\unsure{d'ouverts|ouverts}}.",evidence='The crossed fermés remains tentative. Above it the live ouverts is legible, preceded by a d/apostrophe-like pair, which is retained as d’ouverts|ouverts. The revision remains visibly an insertion over cancellation.',against_c=True,against_h=True,confidence='medium')
A.change('P07_g',final=r'(en tant que voisinages tubulaires \unsure{et} absolus de $Y$)',evidence='The opening is en tant que: the two t ascenders around the low an distinguish it from ainsi que. Voisinages follows on the same line. After tubulaires, a small et-like group precedes the continuation absolus de Y at the far left. The large neighbouring NB is main text and is not inserted as a marginal symbol.',against_c=True,against_h=True,confidence='medium')
A.inventory('E15',first_words_or_objects=new8)
A.inventory('E19',first_words_or_objects=r"\unsure{d'ouverts|ouverts}")
A.update('decisions','id','M0321',reading=r"\inserted{\unsure{d'ouverts|ouverts}}",decision='undecided',evidence='Ouverts is readable, but the d/apostrophe-like prefix now remains an explicit uncertainty in the inserted group.',confidence='medium')
A.update('decisions','id','M0322',reading='en tant que voisinages',decision='other',evidence='The enlarged crop shows en followed by tant with two tall t strokes and then que; these bodies exclude the former ainsi que candidate.',confidence='medium')
A.update('decisions','id','M0323',reading=r'en tant que voisinages tubulaires \unsure{et} absolus de Y',decision='other',evidence='The native-page scope excludes the neighbouring main-text NB. The parenthetical words continue through tubulaires and the doubtful et to absolus de Y.',confidence='medium')
A.update('doubts','place','P07 parenthetical opening',reading=r'en tant que voisinages tubulaires \unsure{et}',alternatives='et-like short group after tubulaires',reason='The former opening doubt is resolved as en tant que voisinages; the small last connective remains doubtful.',confidence='medium')
A.doubt('P07 inserted prefix',r"\unsure{d'ouverts|ouverts}","d’ouverts | ouverts",'A short loop and detached mark stand before ouverts, but their cramped contact with the old cancellation makes the prefix less than certain.','medium')
A.new_change('A01','B08','Question mark after marginal compact','compact, et les','compact, et les','compact, ? et les','A separate curved hook and lower point occur after the comma, aligned with the marginal compact line; original orientation confirms they are not part of a main-text numeral.','other',True,True,confidence='high',error_category='10')
n3=A.get('notes','id','N03')['text']+' Root audit confirmed this source attribution directly in the native page; the tempting rotated cancellation is still excluded. The separate question mark after compact is marginal and has been restored.'
A.update('notes','id','N03',text=n3)
A.update('notes','id','N10',text=A.get('notes','id','N10')['text'].replace('The marginal word ouverts is nevertheless retained because its letters and insertion state are visible','The marginal word ouverts, now with an uncertain d’ prefix, is nevertheless retained because its letters and insertion state are visible'))
old11=r'T_\lambda=\lambda T\text{ dans }X.'
new11=r'T_\lambda\unsure{=|:}\lambda T\text{ dans }X.'
A.replace(old11,new11)
e11='The final relation between T_lambda and lambda T has two very short stacked strokes. The upper stroke is horizontal but the lower approaches a point, so equals remains preferred with colon explicitly possible. The preceding boundary equation has a clearer equals; no grammatical or mathematical normalization settles the final mark.'
A.change('P10_b',final=A.get('changes','id','P10_b')['final'].replace(old11,new11),evidence=e11,confidence='medium')
A.inventory('E29',first_words_or_objects=r'Overworked (8); dotted T_lambda=lambda dotted T, asserted frontier of T_lambda \unsure{=|:} lambda T in X')
A.doubt('P10 final frontier relation',r'\unsure{=|:}','equals | colon','Two very short stacked strokes are visible; the lower one is nearly point-like. Equals remains preferred.','medium')
A.update('notes','id','N04',text=A.get('notes','id','N04')['text'].replace('T_lambda=lambda T dans X','T_lambda [=|:] lambda T dans X'))
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b=='B04':A.decide(b,e4,S[b]['first'].replace(old4,new4))
 elif b=='B05':A.decide(b,e5,S[b]['first'].replace(old5,new5))
 elif b=='B06':A.decide(b,e6,S[b]['first'].replace(old6,new6).replace('du bord $\\dot T$ de $T$','du bord $\\dot T$ dans $T$'))
 elif b=='B08':A.decide(b,e8,new8)
 elif b=='B11':A.decide(b,e11,S[b]['first'].replace(old11,new11))
 else:A.decide(b,ret[b])
im=Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan013.jpg')
im.crop((1190,2170,1685,2345)).save(W/'crops/150_scan013_root_last_formula.png')
im.crop((0,840,400,2050)).save(W/'crops/150_scan013_root_margin_scope.png')
A.append('notes',id='N11',text='Independent audit: root inspected all 11 nonidentical boxes, then the native page and targeted margin/formula enlargements. The overlap of the margin with the main formula number and NB was explicitly checked, preventing duplicate transcription of those neighbouring elements. Five boxes have revised final records; fixed independent readings are unchanged.')
A.save()
