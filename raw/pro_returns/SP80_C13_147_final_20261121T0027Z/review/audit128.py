from edition.scripts.root_audit import Audit

a=Audit(128)
oldtuple=r'D_{d_0,d_1,\ldots,d_r}'
opening=r'D_{d_0,d_1\mathord{-\, -},d_r}'
oldrange=r'\geq\cdots\geq d_r'
newrange=r'\geq\mathord{\cdot\,-}\geq d_r'
f=a.comparison['B03']['first'].replace(oldtuple,opening).replace(oldrange,newrange)
a.change('B03',f,'In the first D tuple, two detached horizontal strokes follow d_1 without an intervening comma, and a comma precedes d_r. In the inequality chain the continuation is one point followed by one short dash. The small digit after the first inequality has a curved head and low return, favoring2 while retaining1. All inequality lower bars are visible; no comma follows0.')
a.replace('de drapeaux $'+oldtuple,'de drapeaux $'+opening)
a.replace(oldrange,newrange)
a.update_row(1,'B03',final=r'$d_0\geq \unsure{d_2|d_1}\geq\mathord{\cdot\,-}\geq d_r\geq0$')
a.add_row('B03','Opening D tuple, continuation and adjacent commas',oldtuple,r'D_{d_0,d_1,\dots,d_r}',opening,'high','symbol','normalized continuation and supplied comma',True,True)
a.keep('B06','The short cross-stroke meets the apex of Delta; it is not a detached bar above the letter. The triangular body, lower r, interval0,r, intersection and doubled left N stem are clear. The first plain Delta reading is retained.')
a.keep('B07','The crop includes the preceding de, which is already present immediately before dim in the page. There is no point after dim; the separate point follows r. The difference is the recorded span boundary, with no omitted de in the transcription.')
a.keep('B10','The verb has a descending p after its initial d/e, supporting dépend rather than devient. The longer following word has the tall l pair and extended ending of fonctoriellement. The I subscript has a stem and two bars. The first reading is retained.')
oldcancel=r'\deleted{\unsure{D_{\Delta_I}|D_{\Delta_r}}}'
newcancel=r'\deleted{\unsure{D_{\Delta_I}|D_{\Delta_r}|D_{I_r}}}'
f=a.comparison['B13']['first'].replace(oldcancel,newcancel)
f=f.replace(r'(d_0,\ldots,d_r)',r'(d_0,\mathord{-\,\cdot},d_r)')
f=f.replace(r'd_0>d_1\cdots>d_r',r'd_0>d_1\mathord{\cdot\,\cdot\,-}>d_r')
f=f.replace(oldtuple,r'D_{d_0,d_1,\mathord{-},d_r}')
a.change('B13',f,'The lower alias is written on two lines, and the other replacement sits above the crossed old term. In that crossed lower cluster, Delta_I, Delta_r and I_r cannot be securely separated. The coproduct index tuple has a dash followed by a point; the inequality continuation has two points followed by a dash; the right-hand D tuple has one continuous dash between commas. N has exponent r alone. No extra inequality occurs after d_1 and no point ends the display.')
a.replace(a.comparison['B13']['first'],f)
a.update_row(10,'B13',final=f)
a.doubt('cancelled old term in (204)',newcancel,'Delta_I, Delta_r or I_r: crossing strokes prevent secure separation of the lower cluster.','low',replace_place='cancelled old term in (204)')
a.keep('B14','The canceled fragment has a large D and a final clear d_r after a comma. A d-like upright and low oval favor the first d_0 index, but crossed angular strokes prevent excluding the existing Delta_r alternative. The first uncertainty is retained.')
component=r'D_{d_0,d_1,\unsure{,}\mathord{-},d_r}'
f=a.comparison['B15']['first'].replace(oldtuple,component)
a.change('B15',f,'This additionally inspected box had matching first and blind readings. The image nevertheless has one continuous horizontal continuation stroke, not three points. Immediately after d_1 there are two small descending curves at different heights: one comma is clear and the apparent second comma is retained with uncertainty. A separate comma precedes d_r.')
a.replace(a.comparison['B15']['first'],f)
a.add_row('B15','La composante tuple, continuation and apparent doubled comma',oldtuple,r'D_{d_0,d_1,\dots,d_r}',component,'medium','symbol','continuation shape and punctuation',True,True)
a.doubt('Apparent second comma after d_1 in La composante tuple',r'\unsure{,}','A second small descending stroke lies below/right of the clear comma; its independence from the preceding subscript finish remains uncertain.','medium')
a.keep('B16','Only the shortened revê/t-like group is visible; there are no separate ment letters to justify expanding it. The final verb has a descending f and extended following joins, supporting s-identifiant over the shorter s-identifie. The first abbreviated uncertainty is retained.')
f=r'\unsure{:|à} '+a.comparison['B17']['first']
a.change('B17',f,'Before the display are two detached marks, an oblique upper tick and a lower short stroke, favoring colon while an extremely compressed accented à remains possible. In (205), the D exponent is a detached upright plus point, the group is beneath the wedge, and the flag letter has a closed angular P bowl. The crossed old argument, live baseline I, underbrace, inserted drapeaux, unpointed ens forms, paired quotation ticks and detached terminal hook retain their first readings.')
a.replace('\nà\n\\[\n\\tag{205}','\n'+r'\unsure{:|à}'+'\n\\[\n\\tag{205}')
a.add_row('B17','Two isolated marks immediately before (205)','à','à',r'\unsure{:|à}','medium','punctuation','two detached marks',True,True)
a.doubt('Two isolated marks before (205)',r'\unsure{:|à}','An upper oblique tick and lower short mark favor colon; the lower mark could be a very compressed a.','medium')
f=a.comparison['B18']['first'].replace(r'D^*_{d_0,d_1,\ldots,d_r}',r'D^*_{d_0,d_1,\mathord{-}d_r}')
a.change('B18',f,'After the comma following d_1 there is one short horizontal stroke, then d_r without another comma. The high star is clear; the lowercase on and following prose remain as first read. The local continuation and punctuation are copied without normalizing them to the earlier tuple.')
a.replace(a.comparison['B18']['first'],f)
a.add_row('B18','Final paragraph starred D tuple, continuation and comma',r'D^*_{d_0,d_1,\ldots,d_r}',r'D^{*}_{d_0,d_1,\dots,d_r}',r'D^*_{d_0,d_1,\mathord{-}d_r}','high','symbol','normalized continuation and supplied comma',True,True)
a.keep('B19','The upper star, lower d_0 and following comma are visible. The prose is the same in both readings; only the ordering of subscript and superscript commands differs.')
a.keep('B20','The short word after the Delta expression has the d loop followed by a low u join, without a separate e/s sequence. The final diviseur ending has no independent added s. The angular Delta and single continuous index dash remain clear; du diviseur is retained.')
a.keep('B21','A closed oval and middle horizontal bar establish the current Theta form over older angular traces. Those earlier fragments do not form an independently recoverable deleted letter. The following D has lower d_0 and a separate terminal point. The first live Theta reading is retained.')
a.keep('B22','The first word has a p descender and tall l loop followed by low u/s joins. The second has the dotted i, m/p group and compressed l/e ending; a short dark horizontal stroke is visible immediately before the right scan border. Plus simple- is retained without completing the clipped continuation.')
for e in a.report['inventory']:
 if e['element']=='E05': e['first_words_or_objects']=next(c['final'] for c in a.choices if c['box']=='B13').removeprefix('\\[\n').removesuffix('\n\\]')
 if e['element']=='E07': e['first_words_or_objects']=newcancel
 if e['element']=='E10': e['position']='between (204) and (205), with isolated two-mark form before (205)'
a.report['notes'][0]=a.report['notes'][0].replace('including the isolated à','including the isolated two-mark form, now retained as colon/à')
a.report['notation'].append(dict(notation=r'\mathord{-\, -}; \mathord{\cdot\,-}; \mathord{-\,\cdot}; \mathord{\cdot\,\cdot\,-}; \mathord{-}',meaning_or_form='Literal continuation strokes and nearby commas vary by occurrence. These graphical sequences are not asserted to be arithmetic operators.',places='Opening tuple and inequalities; (204); La composante tuple; final starred tuple.'))
a.report['unresolved']=[f"{d['place']}: {d['reading']} — {d['alternatives']}" for d in a.report['doubts']]
a.note('Blind audit: all13 differing boxes and the equal-reading B15 were inspected. Five boxes changed: occurrence-specific continuation strokes and punctuation in the opening, (204), component tuple and final starred tuple; an additional I_r alternative in the canceled old term; and colon/à before (205). B15 demonstrates that matching independent strings did not prevent correction against ink. The exponent N^r, inequality omissions, J/I distinctions, shortened revêt, bang, lower group, P flag symbol, final Theta and simple- remain literal.')
a.finish()
