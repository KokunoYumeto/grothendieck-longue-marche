from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan018');S=A.c
ret={
'B01':'The digit has the angular open upper form of 4 followed by a separate closing parenthesis. The difference is only the wrapper; the page uses mspage for this author number.',
'B02':'The raised letter has an upright and two right-hand bowls joined at mid-height, supporting B. De X is on the same raised baseline with its curved attachment before est. The second crop also includes the following physical line; those words are already in the source.',
'B04':'The opening parenthesis is independent. At the other end, the possible closing arc meets the descending y of main-line cylindrique and cannot be separated securely. The existing uncertainty is retained; the second reading’s closed parenthesis is not established more strongly by the ink.',
'B05':'The upper slanted line has utiliser plutôt and a compact trailing la group; the next line has terminologie de. The apparent extra low fragments beyond de follow the upright main-text orientation. The article is not moved to after de. Transversalité is underlined and has no distinct terminal full stop.',
'B07':'Strictement is visibly raised and underlined with a separate curved insertion leader. Compatible remains on the lower baseline; the narrower second reading stops before that baseline word rather than contradicting it.',
'B08':'Avec is completed by the adjacent context of B09. The small lower index has its dot and short body, supporting i; the X and subset relation are clear. The second reading’s omission at the crop edge does not delete the preceding word.',
'B11':'The source physically ends the first line at seule- and begins the next with ment. The first transcription records that division. The final X_i-star has a clear multipointed star, unlike the compact signs in the preceding formulas.',
'B12':'The small note is crossed by several independent broad strokes. Surviving descending p-like members, a tall loop and the extended second-word run support the existing doubtful appeler transversalité candidate. The terminal question-like body and extra dot remain unresolved; the second de ce reading does not recover a more secure complete phrase.',
'B14':'The short first modifier has a separate underline below a strike through its bodies. Its tall t members and compressed middle still permit strictement, but do not justify a secure word. Replacing the whole candidate by an unreadable count would discard those recoverable parts.',
'B17':'The first small word has a tall looped d and compressed low continuation before two distinct colon points, fitting the existing dire/désir alternatives. The following long word has t-like uprights and an extended body; rencontre is not supported by its opening or length. The existing first transversalité candidate remains doubtful.',
'B19':'The leading horizontal is genuinely marginal and separate from the zero-image equality. The lower closure formula is already transcribed as the next line; its appearance in this wider second crop does not create another copy. Dot, both indices, equality and intersection agree.',
'B20':'The opening consists of a short i-like stem with point, e and another distinct point, supporting i.e. The closure bar spans the right-hand set expression. The adjacent large cross and lower descending stroke are upright main-text X_i and ment, confirmed in the native page, not marginal arrows or additional symbols.',
'B21':'A small lower curled body after T is crossed by a separate horizontal and remains an uncertain epsilon-like cancelled index. It is not absorbed into the T stem. The circled 4, separate point, cancelled Soit and live Un agree.',
'B22':'The underlined word has the extended equi/singulier sequence, including the descending g and tall l, with a separate initial acute. It is too long and differently formed for équi-plein or quasi-plein. The relation retains an independent short upper dash and a longer lower shaft with uncertain terminal head.',
'B23':'The second underlined word again contains the long equisingulier sequence and descending g, not quasi-plein. Its initial e has no independent acute, unlike the first occurrence. The existing spelling distinction is retained.',
'B24':'The final underline begins under the tail of de and continues below plus; it does not include si. The other two underlined phrases and the family T_i subset T remain unchanged.',
'B25':'The first variable has an open fork and descending stem, without a horizontal T roof. It is Y_i. The later dotted T_i has a distinct full roof and dot, and its arrow has a clear head. No mathematical normalization changes the literal first letter.',
'B26':'Both readings identify the same separate horizontal dash, et and doubtful même with overworked initial strokes. The TeX dash encoding does not establish a different source punctuation mark.'}
changes={}
o=r'\dot T-)$, et si}';n=r'\dot T-)$, \uline{et} si}'
e='The raised et has a separate short underline beneath its letter bodies, in addition to the t crossbar. Its si follows in the insertion zone and attaches to the main dotted T. The terminal horizontal in the formula is baseline after T, not a lowered index. The existing formula order and grouping remain literal.'
A.replace(o,n);changes['B09']=(r', et si',r', \uline{et} si',e)
A.change('P06_e',place='Raised and underlined et si attachment',final=r', \uline{et} si}',evidence=e,kind='other',against_c=True,against_h=True,error_category=10)
A.inventory('E09',first_words_or_objects='elle est compatible … (X_i∩T=I.X_i∩dotT-), underlined et, si')
o=r'''$X^*=X\setminus\mathring T$, compatible avec la famille des
$X_i^*=X^*\cap X_i$. Donc cela implique que'''
n=o.replace('X^*',r'X^{\unsure{*}}').replace('X_i^*',r'X_i^{\unsure{*}}')
e='All three raised signs in these two formulas are very small angular/forked bodies, less fully multipointed than the clear star on the next line. Star remains the preferred local reading, but these occurrences are now explicitly doubtful. The open circle over T is distinct and is retained.'
A.replace(o,n)
changes['B10']=(None,None,e)
A.doubt('P07 three compact raised signs',r'X^{\unsure{*}},\ X_i^{\unsure{*}}','star preferred; no secure alternative glyph','The tiny angular bodies do not separately show the full arms of the clearer star on the following line.','medium')
o=r'\unsure{On dira}';n=r'\unsure{On dira|déf$^{n}$}'
e='The compressed opening before que contains linked rounded and tall members. It does not securely distinguish On dira from a def-like abbreviation with a raised ending. The inherited On dira remains preferred, with the independent abbreviation candidate explicit. Que has a separate q descender; the small group after X_i fits est better than a separately constructed inequality with zero.'
A.replace(o,n);changes['B13']=(o,n,e);A.change('P10_a',final=n+' que',evidence=e)
A.update('doubts','place','P10 opening',reading=n,alternatives='On dira | déf with raised n',reason='Linked rounded and tall strokes do not securely separate the opening words from an abbreviated form.')
A.inventory('E12',first_words_or_objects='Doubtful On dira/déf with raised n, que X_i est … final closure formula')
o=r'\deleted{compatible \unsure{avec $T$|avec $\bar T$}}';n=r"\deleted{\unsure{compatible|c'est plus} \unsure{avec $T$|avec $\bar T$}}"
e='The live underlined word has a long transvers- body and terminal l, so it is not the short bord. The following crossed phrase contains loops and tall/descending members that do not securely distinguish compatible from c’est plus. Compatible remains preferred but is now doubtful. The crowded following T/barred-T group retains its earlier alternatives.'
A.replace(o,n);changes['B15']=(o,n,e);A.change('P10_e',final=n,evidence=e)
A.update('doubts','place','P10 cancelled following group',reading=n,alternatives='compatible | c’est plus; followed by avec T | avec barred T',reason='The long crossing stroke masks the central joins and does not distinguish the first phrase securely.')
A.inventory('E14',first_words_or_objects='doubtful compatible/c’est plus, followed by doubtful avec T/barred T, all cancelled')
o=r'0.\unsure{\dot X_i|X_i}';n=r'0.\unsure{X_i|\dot X_i}'
e='The cancelled equality has clear si, X_i cap Y, equals and zero point. Above its right X, the nearby dark point is entangled with the return from the line above and is less securely attached than the explicit dot in the live equality below. Plain X_i is now preferred, with dotted X_i retained as an alternative. The continuous deletion stroke remains certain.'
A.replace(o,n);changes['B16']=(o,n,e);A.change('P10_f',final=A.get('changes','id','P10_f')['final'].replace(o,n),evidence=e,against_c=False,against_h=True,confidence='medium')
A.update('doubts','place','P10 right-hand X in cancelled equality',reading=n,alternatives='0.X_i | 0.dot X_i',reason='The high point is entangled with the return from above; a separately attached dot is less secure than in the live equality below.')
A.inventory('E15',first_words_or_objects='si X_i∩Y=0.(X_i|dot X_i), cancelled')
o=r'\deleted{stricte} \unsure{transversalité} :';n=r'\unsure{strict|\deleted{stricte}} \unsure{transversalité|transversif|transversal} :'
e='In the lower marginal adjective, the long horizontal follows the connected letter bodies and is not securely separable as an independent strike. A live strict is now preferred; the earlier cancelled-stricte reading remains an explicit alternative. The following long word is distinct from the preceding transversalité candidate, but its final tall descending stem permits transversif or transversal as well as the inherited transversalité. The colon remains. Native orientation confirms that the apparent lower arrow is the main-text ment continuation, not another marginal drawing.'
A.replace(o,n);changes['B18']=(o,n,e)
A.change('P10_i',place='Lower marginal strict/stricte and uncertain deletion state',final=r'\unsure{strict|\deleted{stricte}}',evidence='The horizontal joins the letter bodies and is not independently established as a cancellation. Live strict is preferred; the previous deleted stricte remains an alternative because the final return and crossing state are compressed.',against_c=True,against_h=False,confidence='low')
A.change('P10_j',final=r'\unsure{transversalité|transversif|transversal} :',evidence='The separate long live word has a tall initial t-like body and final descending stem. Its flattened middle/ending permit transversalité, transversif or transversal; the original candidate remains preferred. Two detached colon points follow.',confidence='low')
A.inventory('E16',kind='text',position='large margin between the two long word candidates; state uncertain',first_words_or_objects='live strict preferred; cancelled stricte alternative')
A.doubt('P10 lower adjective state',r'\unsure{strict|\deleted{stricte}}','live strict | cancelled stricte','The long horizontal is not distinguishable from the connected letter joins; the final e/exit is also uncertain.','low')
A.update('doubts','place','P10 second transversalité; M0345',reading=r'\unsure{transversalité|transversif|transversal}',alternatives='transversalité | transversif | transversal',reason='The final tall descending stem and flattened middle do not uniquely fix the word ending.')
A.update('decisions','id','M0345',reading=r'\unsure{transversalité|transversif|transversal}',evidence='The separate long word retains the original candidate, but the final descending stem also permits transversif/transversal; the root crop does not resolve the ending.',confidence='low')
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b in changes:
  o,n,e=changes[b]
  f=S[b]['first'].replace('X^*',r'X^{\unsure{*}}').replace('X_i^*',r'X_i^{\unsure{*}}') if b=='B10' else S[b]['first'].replace(o,n)
  assert f!=S[b]['first'],b
  A.decide(b,e,f)
 else:A.decide(b,ret[b])
Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan018.jpg').crop((0,780,700,1660)).save(W/'crops/150_scan018_root_native_margin.png')
A.append('notes',id='N99',text='Independent audit: root personally inspected all 24 nonidentical boxes, the full slanted-margin crops and a wider native-orientation context. Six boxes were revised. The raised et underline is restored; the cancelled equality now prefers plain right-hand X_i; the lower adjective now prefers live strict with its earlier deletion reading retained as an alternative. Other new alternatives retain the earlier preferred text and do not create primary C corrections. Fixed first/second readings remain unchanged.')
A.save()
