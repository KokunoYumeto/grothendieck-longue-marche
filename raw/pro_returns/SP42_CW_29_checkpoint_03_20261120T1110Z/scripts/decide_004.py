from adjudication_helpers import *
d,rs,ts=start(4,'R3')
text=ts['R3'].replace(r'definit\handwritten{\inserted{e}}',r'definit\handwritten{e}')
r=row_from(rs['R1'],1,crop='crops/scan004/01_page_number.jpg')
r['readers']={k:r'\mspage{2.}' for k in rs};r['scan_shows']='The main crop shows a black typed 2, with rounded top, descending waist and flat foot, followed by a separate black full stop. This is an authorial/typed page label, distinct from archival foliation.'
d['rows'].append(r)
r=row_from(rs['R1'],2,crop='readers/scan004/R3/crops/02_signature.jpg')
r.update(c='no surname-final period',h='surname followed by period',final='no surname-final period',scan_shows='Main inspection shows that the low joined surname stroke ends in a rightward flourish. The following area is blank: no separate period is present. The two dots earlier in the signature follow the initials. This high-confidence row concerns punctuation only; the surname remains doubtful.',readers={k:'no surname-final period' for k in rs})
d['rows'].append(r)
d['rows'].append(dict(place='Signature: scope of C doubt',c=r'\handwritten{\unsure{J.P. Murre}}',h='J. P. Murre.',final=r'\handwritten{J.P. \unsure{Murre}}',against_c=True,against_h=False,kind='other',marked_in_H=False,confidence='medium',scan_shows='The long descending first initial with its top sweep reads J, and the following looped stem reads P; each has a separate point. The large M is followed by compressed low humps and an ending sweep, compatible with Murre but not fully letter-separated. Main inspection supports R3 in restricting the doubt to the surname. H has the same candidate letters; its extra terminal period is recorded in the preceding row.',crop='readers/scan004/R3/crops/02_signature.jpg',readers={'R1':r'\unsure{J.P. Murre}','R2':r'\unsure{J.P. Murre}','R3':r'J.P. \unsure{Murre}'}))
d['rows'].append(dict(place='Last body line: handwritten e in definite',c=r'definit\handwritten{e}',h='definite',final=r'definit\handwritten{e}',against_c=False,against_h=False,kind='other',marked_in_H=False,confidence='high',scan_shows='The main crop shows black typed definit, followed by a separate blue loop-and-return e. There is no readable underlying typed e or deliberate accent. C already marks the handwriting at the correct place. Additional inserted wrappers in the reader returns are equivalent encoding choices, and H retains the same letter sequence; neither is a substantive collation difference.',crop='readers/scan004/R1/crops/crop01_definite.jpg',readers={'R1':r'definit\handwritten{\inserted{e}}','R2':r'definit\inserted{\handwritten{e}}','R3':r'definit\handwritten{\inserted{e}}'}))
d['doubts']=[dict(place='Signature surname',reading=r'\unsure{Murre}',alternatives=[],confidence='medium',reason='The initial M is distinct but the joined lower strokes do not independently separate every remaining surname letter. No competing full surname is supported. J.P. and the absence of a final period are resolved.')]
d['inventory']=rs['R1']['inventory']
for x in d['inventory']:
 x['transcribed']='yes'
 if 'signature' in x['position'].lower() or 'Murre' in x['first_words_or_objects']:x['first_words_or_objects']='J.P. followed by doubtful surname Murre; no terminal period'
d['notes']=rs['R1']['notes']
d['notes']['math_reading_decisions']=['No mathematical derivation or formal claim is checked or used on this page. The request for clarification is retained as prose, not treated as a proof-check event.']
d['notes']['content']='Continuation and closing of an English letter: the writer asks for a reply only if the questions reveal a misconception, proposes a preliminary manuscript for discussion at Bures, plans to arrive June 2, and hopes to finish the definite version during the stay (body paragraph). The typed page label is 2.; the blue signature reads J.P. with the surname Murre still qualified. No year is supplied on this sheet.'
d['slips']=['The wording as good as I can is retained; definite is not modernized to definitive.']
d['check_events']=[]
d['workflow']=dict(brief='brief_v002_scan004.md',r1_crops=2,r2_crops=2,r3_crops=2,main_crops=1,feedback='All three read whole + halves once and made two crops each. Main viewed the final-e crop, signature crop and one newly made page-number crop. The signature doubt is narrowed to the compressed surname. H archival foliation and line-layout omissions are excluded from substantive counts; the archive numeral remains a comment and inventory element. Handwritten e versus inserted+handwritten e is equivalent correctly placed encoding. Brief v003 makes these distinctions explicit and permits an honestly uncaptured reader start time; no inferred timestamp is substituted in R3’s original report.')
d['workflow']['main_reader_crops_viewed']=2
d['main_adjudication_complete']=True
save(d,text)
