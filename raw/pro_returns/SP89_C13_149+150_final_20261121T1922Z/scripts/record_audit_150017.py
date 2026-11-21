from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan017');S=A.c
ret={
'B00':'Both readings give the same numbered formula: E, simeq, dotted T, multiplication and the closed interval [0,1]. The difference is only surrounding math delimiters; the page already supplies display math.',
'B06':'After X-prime the looped d is followed by a compact but distinct a/n/s run, longer than de. The raised fermée and its curved attachment are separate from the main baseline. The first dans reading is retained.',
'B07':'The E has heavier horizontal arms over narrower upper and lower curved returns. A doubtful older B remains the appropriate overwritten layer; the second reading’s plain doubtful E loses this evidence. The following dash and homéom. abbreviation agree.',
'B08':'Two earlier right-hand bowls are visible beneath the heavy E bars, supporting B more securely here than in the prose occurrence. E is written directly over B, without a separate raised insertion site or leader. The existing deleted-B/live-E sequence is retained.',
'B13':'Two short opening ticks precede the cancelled word. The different quote encodings represent the same observed opening quotation. The cancelled compatibilité and raised transversalité remain locally doubtful at the clipped edge.',
'B14':'The old dans le cas has a continuous strike; cylindrique is live and followed by two closing ticks. N’est pas has a separate underline, crossed only by its p descender. TeX quotation and apostrophe encoding do not change this reading.',
'B18':'The formula is crossed throughout. E is retraced, but the small internal point does not establish an independent dot accent or earlier glyph. After the first brace/zero group, an epsilon-like body and a further closing-brace return are visible. The first explicit segmentation alternatives retain more of that ink than an unspecified final mark.',
'B20':'The two thin digits are 1 and 6, with a closed lower bowl on the latter. The page already uses the margin wrapper; the bare first box reading and wrapped second reading identify the same number.'}
changes={}
def revised(b,old,new,e):
 A.replace(old,new);changes[b]=(old,new,e)
o=r't\mapsto(t,0)';n=r't\unsure{\leftrightarrow|\mapsto}(t,0)'
e='The diagram has three objects, two directed structural shafts, two terminal heads and one hook, plus an unheaded vertical identification. In the small element label, the left end of the short horizontal has two oblique branches and favors a left arrowhead rather than a simple mapsto bar. The right head is distinct. The label is therefore kept as a doubtful two-headed correspondence, with mapsto secondary; its mathematical intention does not choose the glyph.'
revised('B01',o,n,e);A.change('P01',final=A.get('changes','id','P01')['final'].replace(o,n),evidence=e,confidence='medium');A.inventory('E03',first_words_or_objects=A.get('inventory','element','E03')['first_words_or_objects'].replace(o,n))
A.doubt('P01 element-label relation',r'\unsure{\leftrightarrow|\mapsto}','leftrightarrow | mapsto','Two oblique branches at the left end resemble a small arrowhead, but the compact join also permits a heavy mapsto bar.','medium')
o=r'\unsure{*|\varepsilon}';n=r'\unsure{k|*|\varepsilon}'
e='The prime is clearly raised, while the second mark is at the lower right of X. Its compact upright and two right branches favor a k-like body over a multipointed star; epsilon remains possible under the heavy joins. A t would require a more distinct crossing bar. The low placement is retained and the uncertain candidates reordered from the visible shape.'
revised('B02',o,n,e);A.change('P02b',final=A.get('changes','id','P02b')['final'].replace(o,n),evidence=e,confidence='low');A.inventory('E04',first_words_or_objects=A.get('inventory','element','E04')['first_words_or_objects'].replace(o,n))
A.update('doubts','place','P02 low mark beside X prime',reading=r"X'_{"+n+'}',alternatives='k | star | epsilon',reason='A compact upright and two right branches favor k, but the dark joins do not fix the mark securely.',confidence='low')
o='bord stricte';n=r'bord \unsure{stricte|strict}'
e='Bord has its separate tall d return. After the adjective’s final tall crossed t, a short terminal return can be an e or the t exit itself. Stricte remains preferred, with strict now explicit; the ending is not supplied from agreement.'
revised('B04',o,n,e);A.change('P03',final='partie '+n,evidence=e,confidence='medium');A.inventory('E05',first_words_or_objects='Soit B une partie bord stricte/strict … définition de compatible avec E')
A.doubt('P03 adjective ending',r'\unsure{stricte|strict}','stricte | strict','The short terminal return is not cleanly separable from the final t.','medium')
o=r'\unsure{absolu de}';n=r'\unsure{absolu de|autour de}'
e='The old phrase is crossed by a heavy horizontal. A rounded opening, tall inner stem and low joins survive; these do not uniquely distinguish absolu from autour. The separate de is crossed and replaced by a clear raised de. The earlier candidate remains preferred with the independent alternative explicit.'
revised('B05',o,n,e);A.change('P04',final=A.get('changes','id','P04')['final'].replace(o,n),evidence=e);A.inventory('E06',first_words_or_objects=r'\deleted{'+n+'}')
A.update('doubts','place','P04 old absolu de',reading=r'\deleted{'+n+'}',alternatives='absolu de | autour de',reason='The heavy strike hides the low middle joins and does not distinguish the tall inner letter securely.')
o=r'(où néc$^t$. on a';n=r'(où néc$^t$. \unsure{on a}'
e='The raised t and baseline abbreviation stop are clear. The short bodies between that stop and B-prime are very compressed and faint; on a remains the candidate but is not fully secure. The opening parenthesis is present in the wider source context, and the closing parenthesis/period are clear.'
revised('B10',o,n,e);A.change('P08',final=A.get('changes','id','P08')['final'].replace(o,n),evidence=e,confidence='medium');A.inventory('E12',first_words_or_objects='si X-prime cap E s’identifie à B-prime×[0,1] (où néc with raised t, doubtful on a, B-prime=X-prime cap B).')
A.doubt('P08 compressed on a',r'\unsure{on a}','on a','The short low bodies remain faint and do not separate all letters.','medium')
o=r'\uline{transversale}';n=r'\uline{\unsure{transversale|transversal}}'
e='Plutot has no independent accent above the o in this crop. The final punctuation is an upright and detached dot, hence an exclamation mark. The underlined adjective has a tall final l with a short right return that may or may not make a separate e. Transversale remains preferred; transverse lacks the visible a/l sequence.'
revised('B11',o,n,e);A.change('P09',final=A.get('changes','id','P09')['final'].replace(o,n),evidence=e,confidence='medium');A.inventory('E13',first_words_or_objects=A.get('inventory','element','E13')['first_words_or_objects'].replace(o,n))
A.doubt('P09 terminal e',r'\unsure{transversale|transversal}','transversale | transversal','The short return after the tall l does not establish a separate e securely.','medium')
o="sous-espace bord de $X'$";n=r"sous-espace \unsure{bord|à bord} de $X'$"
e='The marginal sentence and its final X-prime are legible, with no terminal full stop. Near the junction after sous-espace, a compact looped body and the beginning of bord overlap in the slanted writing. The crop does not securely settle whether a separate à precedes bord. The prior bord reading remains preferred, with the second reader’s à bord as an explicit local alternative.'
revised('B12',o,n,e);A.change('P10',final=A.get('changes','id','P10')['final'].replace(o,n),evidence=e,confidence='medium');A.inventory('E14',first_words_or_objects=A.get('inventory','element','E14')['first_words_or_objects'].replace(o,n))
A.doubt('P10 junction before bord',r'\unsure{bord|à bord}','bord | à bord','The compact loop at this junction cannot be isolated securely as an independent à.','low')
o='particulier de celle dans la';n='particulier de celle de la'
e='The enlarged source junction after celle contains a looped d followed by a short e return. It lacks the additional a/n/s bodies needed for dans. The next article is la, with a rounded a after the tall l. The small crossed token, raised compatibilité, accented cônique and underlined mais est retain their earlier readings.'
revised('B15',o,n,e);A.change('P13a',place='de la before the short crossed word',final='celle de la',evidence=e,against_c=True,against_h=True,confidence='high');A.inventory('E19',position='After de la, P13')
o=r'\unsure{dans ce cas}';n=r'\unsure{demande en f|dans ce cas}'
e='The lower crossed introduction has an initial looped d, a longer joined middle sequence and a final tall crossed stem. Those surviving bodies fit demande en f more closely than the short dans ce cas, but the continuous strike prevents a secure full reading. The inserted plus/exigeant(e), separately crossed que-like group, colon and T-prime cap Y formula remain distinct writing layers.'
revised('B16',o,n,e);A.change('P14b',final=n,evidence=e,against_c=True,against_h=True,confidence='low');A.inventory('E24',first_words_or_objects=A.get('inventory','element','E24')['first_words_or_objects'].replace(o,n))
A.update('doubts','place','P14 old introduction',reading=r'\deleted{'+n+'}',alternatives='demande en f | dans ce cas',reason='The long joined middle and final tall stem favor the first candidate, but the strike obscures several letter bodies.')
o=r'\unsure{lui}';n=r"\unsure{lui|l'on}"
e='The last verb reads devait: d/e/v/a/i/t are present, without a separate r after v or the m/n run needed for demandait. The preceding short group is crossed by a descender from the line above, so lui remains preferred with l’on now explicit. The page already places this clause within the insertion wrapper.'
revised('B17',o,n,e);A.change('P15',final=A.get('changes','id','P15')['final'].replace(o,n),evidence=e);A.inventory('E21',first_words_or_objects=A.get('inventory','element','E21')['first_words_or_objects'].replace(o,n));A.update('decisions','id','M0341',reading=n+' devait',evidence=e,confidence='medium')
A.update('doubts','place','P15 pronoun/remnant before devait',reading=n+' devait',alternatives='lui | l’on; devait resolved',reason='The short pronoun group intersects the descender from above, preventing separation of its internal low strokes.')
o='On définit de';n='On definit de'
e='The wider original bottom view has no independent accent above the e in definit; the neighbouring tall stroke is the f body. The unaccented spelling is retained literally. The two strokes after de are an equals sign, not written même; the crossed de and plural parties remain readable.'
revised('B19',o,n,e);A.new_change('A01','B19','Unaccented final verb','On définit','On définit','On definit',e,'abbreviation expanded or spelling modernised',True,True,'medium',error_category='8');A.inventory('E25',first_words_or_objects='On definit de = la compatibilité pour une famille … parties …')
A.update('notes','id','N04',text=A.get('notes','id','N04')['text'].replace('star/epsilon alternatives','k/star/epsilon alternatives, with k preferred after root inspection'))
A.update('notes','id','N07',text=A.get('notes','id','N07')['text']+' The final verb is unaccented definit on the wider original view. The marginal bord/à bord junction and adjective endings now retain explicit local alternatives.')
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b in changes:
  o,n,e=changes[b]
  f=S[b]['first']
  if b=='B10':f=f.replace('on a',r'\unsure{on a}')
  elif b=='B15':f=f.replace('celle dans la','celle de la')
  else:f=f.replace(o,n)
  assert f!=S[b]['first'],b
  A.decide(b,e,f)
 else:A.decide(b,ret[b])
im=Image.open(W.parent/'source/SP89_C13_149+150_scans/150_scan017.jpg')
im.crop((160,2100,1685,2362)).save(W/'crops/150_scan017_root_bottom_wide.png')
A.append('notes',id='N99',text='Independent audit: root personally inspected all 19 nonidentical boxes, enlarged the de/la junction and slanted marginal junction, and checked the wider original bottom lines. Eleven boxes were revised. Alternative-only doubts retain their first preferred readings and do not generate new primary C corrections. All fixed first/second readings remain unchanged.')
A.save()
