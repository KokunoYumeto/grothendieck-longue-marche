from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan014');S=A.c
ret={
'B01':'The numeral has a descending curved main stroke turning into a substantial rightward foot, followed by a separate closing parenthesis. That form supports 2 rather than the narrow 1 alternative; the first folio is retained.',
'B06':'The old opening begins with an O-like loop and n, followed by di with its ascender and dot, but the struck ending is incomplete; On dira remains uncertain rather than changing to certain On dit. The raised isolated capital has two right limbs and a separate upper accent-like stroke, supporting É/E rather than a plain arrow. Before dire, a descender and compressed joins do not establish the second reader’s clean On dira; the first enfin de remains explicitly doubtful. Slanted margin ink is not expanded into Évitons.',
'B07':'A thin original Z has top and bottom horizontals; a heavier Y fork and long stem overwrite it. The order deleted Z then live Y is visible, not reversible.',
'B09':'The initial cylindrique letter is heavily retraced where its underline meets the old line. It cannot be separated as a new independently readable Z/xi word. Collier is crossed and underlined below the raised cylindrique. The overwritten variable again has the old Z bars and heavy live Y.',
'B11':'The abbreviation ends at homéom, with no independent final stop, followed by one long dash. Three TeX hyphens and a Unicode em dash represent the same observed dash.',
'B13':'The small crossed group before the live T has a narrow stem and loop but is not fully readable. De remains a tentative recovery, rather than becoming an unspecified newly certain word. The live T and following prose agree.',
'B14':'Formula (9) has a wave over a short horizontal, a single-roof T, Y and a heavy serif I. Differences are only spacing/wrapper syntax.',
'B15':'The triangle has Y, T and Y×I, one hooked rightward top arrow and one down-right arrow labelled y maps to (y,0). The vertical identification consists of a wave-like stroke beside a separate straight stroke, without an arrowhead. Both readings recover that geometry; the first phantom connector with a wr/vertical pair is retained.',
'B16':'The product has a Y fork; the small dark point is within/at the fork rather than a separate mark above it. A dotted Y is not established. Compatible avec has its p descender and later t/l strokes. The lower upper-row target is literally [0,1]; its head remains uncertain. The first two-row arrangement and literal uncorrected target are retained.',
'B17':'The word cônique has a detached roof over o. The inserted absolu has its own paired curved boundaries and a separate attachment leader. The struck tout remains tentative; the source’s sous-espace bord ending is intact.',
'B18':'The initial d loop is clear but the low nc continuation is strongly compressed, so the first donc uncertainty is retained. The dotted T with lower lambda is independently visible and no extra connective is supplied.'}
old4=r'T\deleted{\unsure{_\lambda}}';new4=r'T\deleted{\unsure{\lambda|Y}}'
A.replace(old4,new4)
A.replace(r'\unsure{pour|avec}',r'\unsure{pour|p.ex.|avec}')
A.replace('% P02: crossed group after T; the lambda reading and lowered attachment remain uncertain.','% P02: crossed group after T occupies the main baseline; its lambda/Y identity remains uncertain.')
e4='The crossed token starts at approximately the T roof and descends below its stem, so the whole token is not a lowered subscript. Lambda remains tentative, with the forked Y alternative admitted. The next word has a p-like descender but compressed middle strokes; pour remains preferred, with p.ex. and avec unresolved. The final oval is the written 0.'
A.change('P02d',final='X='+new4,evidence='The crossed token begins near the live T roof and extends below it. It is retained on the baseline, with lambda/Y unresolved, rather than encoded as a definite lowered attachment.',against_c=True,against_h=True,confidence='low')
A.change('P02e',final=r'\unsure{pour|p.ex.|avec}',evidence='A p-like loop and descender lead into compressed retraced strokes. Pour remains the first candidate; the apparent separated middle strokes also admit p.ex., while avec remains less favored. No grammatical completion settles it.',confidence='low')
A.inventory('E04',first_words_or_objects=r'crossed baseline token \unsure{\lambda|Y}')
for d in A.r['doubts']:
 if d['reading']==r'\unsure{pour|avec}':A.update('doubts','place',d['place'],reading=r'\unsure{pour|p.ex.|avec}',alternatives='pour | p.ex. | avec',reason='The p-like beginning is clearer than the compressed retraced middle; none of the complete candidates is secure.')
 if '_\\lambda' in d.get('reading',''):A.update('doubts','place',d['place'],reading=r'\deleted{\unsure{\lambda|Y}}',alternatives='lambda | Y; baseline token',reason='The root crop places its top near the T roof and its bottom below the T stem, so a wholly lowered subscript is not supported.')
# A solitary amorphous blot is not promoted into a source drawing or punctuation.
graphic=S['B05']['first']
A.replace(graphic,'')
A.replace('% P02: isolated vertical ink point below faux, to the right of the parenthesis; linguistic status unclear.','% P02: isolated amorphous dark blot in the blank gap below faux; not a recoverable letter, punctuation mark, or figure. Omitted from diplomatic content; crop retained in the audit.')
e5='The tight crop contains only an irregular filled vertical blob, with no separable pen path, letter structure, connector, second point or alignment with a prose/formula baseline. Its location is in the blank gap below faux and right of the parenthesis. There is no evidence for assigning it a mathematical bullet or a figure; the invented standalone TikZ graphic is removed, while this observation and the crop remain in the audit.'
A.ed['report_removals'] += [{'collection':'changes','match':{'id':'P02f'}},{'collection':'inventory','match':{'element':'E05'}}]
old12=r"\deleted{\unsure{i.e.} tel que l'on}"
new12=r"\deleted{\unsure{s'il|i.e.|soit} tel que l'on}"
A.replace(old12,new12)
e12='Under the strike, the opening has a low s-like entry, a detached high apostrophe-like stroke and a later tall l, favoring s’il over i.e. The strike still obscures some joins, so the competing readings remain explicit. Tel que l’on is readable and the following live s’il existe is separate.'
A.change('P07a',final=new12,evidence=e12,against_c=True,against_h=False,confidence='medium')
A.inventory('E14',first_words_or_objects=r"doubtful s'il | i.e. | soit, then tel que l’on")
for d in A.r['doubts']:
 if 'i.e.' in d.get('reading',''):A.update('doubts','place',d['place'],reading=new12,alternatives="s’il | i.e. | soit",reason='High apostrophe-like stroke and tall l favor s’il, but the crossing masks several letter joins.',confidence='medium')
new19=S['B19']['first'].replace(r'\unsure{\varepsilon|\delta}',r'\unsure{\varepsilon|\delta|\lambda}').replace(r'\deleted{Dans}',r'\deleted{\unsure{Donc|Dans}}')
A.replace(r'\unsure{\varepsilon|\delta}',r'\unsure{\varepsilon|\delta|\lambda}')
A.replace(r'\deleted{Dans}',r'\deleted{\unsure{Donc|Dans}}')
e19='The first parameter has several retraced curves, admitting lambda as well as the retained epsilon/delta alternatives. The strip operator has a true E overbar and baseline parenthesized T; the high roof of T does not raise the whole argument. In the crossed word after the period, an O-like round body and a final open c favor Donc over Dans, but the strike prevents certainty.'
A.inventory('E26',first_words_or_objects=r'\deleted{\unsure{Donc|Dans}}')
A.new_change('A01','B19','Cancelled transition before Si X',r'\deleted{Dans}',r'\struck{Dans}',r'\deleted{\unsure{Donc|Dans}}','The initial capital is followed by a rounded o-like body and low joins ending in an open c; these favor Donc, while the strike leaves Dans possible.','misread word',True,True,confidence='medium',error_category='2')
A.doubt('P13 cancelled transition',r'\deleted{\unsure{Donc|Dans}}','Donc | Dans','The rounded body after D and final open c favor Donc, but cancellation masks the middle.', 'medium')
for d in A.r['doubts']:
 if d.get('reading')==r'\varepsilon|\delta' or r'\unsure{\varepsilon|\delta}' in d.get('reading',''):
  A.update('doubts','place',d['place'],reading=d['reading'].replace(r'\varepsilon|\delta',r'\varepsilon|\delta|\lambda'),alternatives='epsilon | delta | lambda',reason='Retracing makes both a looped delta and an angular lambda possible; epsilon remains preferred.')
old21='le sont';new21=r'le \unsure{sont}'
A.replace('ssi les $Y_i$ le sont','ssi les $Y_i$ '+new21)
e21='The union index has a lower hook favoring J but still admitting I; the earlier independent index I does not force normalization. At the paper edge the final word is clipped after compressed s/on/t-like strokes. Sont remains the candidate but is now explicitly uncertain; no stop is supplied beyond the edge.'
A.change('P14c',final=new21,evidence=e21,confidence='low')
A.doubt('P14 clipped last word',r'\unsure{sont}','sont; incomplete final strokes','The word meets the physical paper edge, which prevents a secure complete t ending.','low')
n9=A.get('notes','id','N09')['text'].replace('The isolated filled oval below faux is preserved as a graphic with no assigned punctuation attachment.','Root audit identifies the isolated irregular blot below faux as lacking a recoverable linguistic or geometric structure; the draft graphic is removed and its crop remains available.').replace('The final le sont reaches','The final le sont, with sont now explicitly uncertain, reaches')
A.update('notes','id','N09',text=n9)
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b=='B04':A.decide(b,e4,S[b]['first'].replace(old4,new4).replace(r'\unsure{pour|avec}',r'\unsure{pour|p.ex.|avec}'))
 elif b=='B05':A.decide(b,e5,'',outcome='No diplomatic token: isolated amorphous blot excluded; invented figure and primary correction withdrawn, evidence retained.')
 elif b=='B12':A.decide(b,e12,S[b]['first'].replace(old12,new12))
 elif b=='B19':A.decide(b,e19,new19)
 elif b=='B21':A.decide(b,e21,S[b]['first'].replace(old21,new21))
 else:A.decide(b,ret[b])
im=Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan014.jpg')
im.crop((190,270,880,525)).save(W/'crops/150_scan014_root_opening_wide.png')
A.append('notes',id='N10',text='Independent root audit personally inspected all 16 nonidentical crops, including the isolated blot and the complete triangle/marginal map, and a wider native-image opening. Five boxes were revised. First/second readings and their hashes remain fixed; final adjudications record the exclusion of the nonsemantic blot separately from actual source changes.')
A.save()
