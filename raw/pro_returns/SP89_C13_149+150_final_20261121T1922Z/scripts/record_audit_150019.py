from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan019');S=A.c
ret={
'B01':'The initial short word has a small rounded a body followed by a low u return. No separate hyphen joins it to dessus. The second en alternative is less consistent with that rounded opening. Both dotted T signs and the inclusion agree.',
'B03':'The crossed word retains the t and b/l ascenders, low u/a joins and terminal ire sequence sufficiently to read tubulaire. The raised replacement has its independent circumflex and cônique body; no different former word is supported.',
'B04':'The long word contains the equi/singulier sequence, including q/g descenders and the later tall l. It cannot be reduced to équi-plein. The separate p.r. abbreviation and accented à are visible; the awkward on dit / il est syntax remains literal.',
'B06':'Native orientation distinguishes the main implique ending and the following live que si from the diagonal note’s darker p.r. à group below. There is no independent crossed que between the main words. The apparent extra cancellation belongs to overlapping marginal writing.',
'B08':'The wider native context completes the connected a and tall l before the low o/r/s run and comma. Oblique marginal strokes cross that initial region but do not form a p belonging to the main word. The main-baseline reading is alors, not pleine.',
'B10':'The roof and descending stem identify T despite its overtraced upper return; there is no independent Y fork. The empty-set glyph has a long sloping stem through a small closed loop and is retained as the source phi convention. Ou is independently underlined. The difference in math/display wrappers does not change the ink.',
'B11':'The marginal word is the long équisingulier sequence, with its g descender and later l, not équi-plein. Strictement has a continuation beyond strict and its separate underline. The wider completed crop retains compatible, avec tous and les X_i below; those words were omitted by the narrower second reading, not contradicted.',
'B12':'The lower marginal statement again has the long équisingulier body. P.r. à and the parenthesized X_i are separate from crossing upright text; lambda T l’est strictement and the open interval are readable. The terminal small point is retained. The second équi-plein reading loses the internal singulier letters.',
'B16':'The large filled point is clearly separated above the single T roof. The much smaller fleck to its lower left is not aligned or proportioned as a second written accent point, so a double dot is not established. The cancelled de remains locally doubtful. The long following word is équisingulier.',
'B18':'The final word has the long équisingulier sequence, a descending g and a visible plural s. The two horizontal strokes after sont are the written equals abbreviation. The interval is open at both ends, and no wording is expanded.'}
changes={}
o=r'\deleted{globalement}';n=r'\deleted{\unsure{globalement}}'
e='The independent stroke crosses the word through its low bodies. The g descender and tall l/b/l members support globalement, but some central low joins remain hidden by the strike. The cancellation is certain while the word is now retained as a local doubt; its preferred reading does not change.'
A.replace(o,n);changes['B02']=(o,n,e);A.change('P02a',final=n,evidence=e,confidence='medium');A.inventory('E03',first_words_or_objects='doubtful globalement, certainly crossed through the word')
A.doubt('P02 cancelled word body',n,'globalement','The g and tall ascenders survive, while the stroke hides several low middle joins.','medium')
o=r'X_i\cap T\subset T';n=r'X_i\cap\unsure{T.|T_i}\subset T'
e='A detached dark point is present immediately at the lower right of the first T inside the parenthesis. Its formula position supports retaining it explicitly, while its lack of a distinct lower stem prevents a secure i index. A literal T followed by a point is preferred, with T_i secondary. The earlier pen-remnant dismissal is withdrawn; no mathematical role is supplied to the point.'
A.replace(o,n);changes['B05']=(o,n,e);A.change('P04c',place='Par rapport à and the detached point in its family formula',final=A.get('changes','id','P04c')['final'].replace(o,n),evidence=e,kind='misread symbol or index',against_c=True,against_h=True,confidence='medium',consequential=True,error_category='1')
A.replace('% P04: a tiny detached low point follows the first T inside the parenthesis; it has no established notational attachment and is treated as a pen remnant.','% P04: the detached low point after the first T is retained literally; an i-index remains an alternative, with no assigned mathematical role.')
A.inventory('E07',first_words_or_objects='detached low point after the first T, transcribed literally with a T_i alternative; role unresolved')
A.doubt('P04 point after first T',r'\unsure{T.|T_i}','T followed by point | T_i','The isolated dark point lies at the low right of T but has no clearly separated i stem.','medium')
A.update('notes','id','N07',text=A.get('notes','id','N07')['text'].replace('The tiny point after the first T in the P04 parenthesis has no secure notational attachment and is documented as a pen remnant, not converted into multiplication or a subscript.','The tiny point after the first T in the P04 parenthesis is retained explicitly after root inspection, with a T_i alternative. Its mathematical role remains unassigned; the earlier dismissal as a pen remnant is withdrawn.'))
o=r'\unsure{5}';n=r'\unsure{5|8}'
e='The broad zigzag crosses both the circled digit and its surrounding oval and continues into the upper dense loop. Thus the whole circled item is cancelled, with no separate earlier digit recoverable above it. Five remains preferred, but the crossed lower and upper bowls also permit eight; both are now explicit.'
A.replace(o,n);changes['B13']=(o,n,e);A.change('P10a',final=A.get('changes','id','P10a')['final'].replace(o,n),evidence=e);A.inventory('E13',first_words_or_objects='cancelled circled doubtful 5/8; cancellation continues into an upper loop')
A.update('doubts','place','P10 cancelled circled item',reading=r'\deleted{\textcircled{'+n+'}}',alternatives='5 | 8',reason='The zigzag obscures the junction between the upper and lower bodies and crosses the containing circle.')
o=r'p.r. \deleted{à}';n=r'p.r. \deleted{\unsure{à}}'
e='The accent survives above a heavily crossed short low body after p.r. The body is consistent with à but does not expose its full loop independently of the strike. The preferred cancelled preposition is retained with local uncertainty. The following family, dash, auquel cas and lambda T are unchanged.'
A.replace(o,n);changes['B17']=(o,n,e);A.change('P13a',final=A.get('changes','id','P13a')['final'].replace(o,n),evidence=e,confidence='medium');A.inventory('E18',first_words_or_objects='doubtful cancelled à; no aux replacement')
A.doubt('P13 crossed preposition',r'\deleted{\unsure{à}}','à','The raised accent is visible, but the low letter body merges with the strike.','medium')
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b in changes:
  o,n,e=changes[b];A.decide(b,e,S[b]['first'].replace(o,n))
 else:A.decide(b,ret[b])
Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan019.jpg').crop((120,580,850,1130)).save(W/'crops/150_scan019_root_native_context.png')
A.append('notes',id='N99',text='Independent audit: root inspected all 14 nonidentical boxes, the completed diagonal-note crop and a wider native context separating marginal strokes from main prose. Four boxes were revised. The detached point in the family formula is now transcribed with an index alternative; three other revisions add local uncertainty without changing their preferred readings. The immutable first/second readings are preserved.')
A.save()
