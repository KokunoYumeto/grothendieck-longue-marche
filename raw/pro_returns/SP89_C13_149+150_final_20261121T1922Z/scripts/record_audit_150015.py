from audit_record import AuditRecord,W
from PIL import Image
A=AuditRecord('150_scan015');S=A.c
ret={
'B01':'The first line has a horizontal strike through On dit and an independent raised Soit with its tall S opening, dot and final t. The cancellation and replacement are separate writing layers, not a continuous On définit. Tubulaire and its raised conique replacement also agree.',
'B02':'The formula distinguishes the open circle over the first T from the filled dot over the last T. In the cancelled prose, a looped d and a tall final t support dit; no separate s opening supports sait.',
'B03':'Prop has a separate underline and a doubtful terminal point at its end. Whether the TeX underline encloses that doubtful point is not a distinct source reading. The where/given clause and partie-bord are unchanged.',
'B04':'The opening word on the second line is avec, and lui is followed by a hyphen and two clear equality strokes, not written même. An enlarged view of the target prefix shows the apparent opening-parenthesis curve sharing the cancelled lambda-like cluster, without a separable intact parenthesis. The first unmatched closing parenthesis remains literal.',
'B07':'The opening is a tall narrow l followed by a separate apostrophe, not a rounded d body. The final isomorphisme has no plural s; compatible is singular and the detached roof over o in côniques is retained.',
'B08':'Despite the crossing diagonal marginal line, the main baseline reads On dit alors que: dit has its d/t stems, and alors has a separate tall l and low ending. There is no independent p-descender word peut on that baseline. Tub. is crossed, conique live, and strict underlined.',
'B12':'The final voisinages has a small terminal low s after its g/e sequence; the source does not end at the g descender. The lower tubulaires/coniques replacement and stricts are distinct and remain unchanged.'}
old5='induit';new5=r'\unsure{induit|induise}'
A.replace("l'homéomorphisme induit l'identité", "l'homéomorphisme "+new5+" l'identité")
e5='The enlarged verb has the dotted i, n, tall d, low u and second dotted i. Its final joined body is too compressed to separate a short t from an s/e continuation securely. Induit remains the preferred ink reading, with induise now explicit; the grammatical expectation alone does not resolve it.'
A.change('P05_a',final="que l'homéomorphisme "+new5+" l'identité",evidence=e5,confidence='medium',against_c=False,against_h=True)
A.inventory('E13',first_words_or_objects=r'Comme b, mais ... \unsure{induit|induise} l’identité')
A.doubt('P05 verb ending',new5,'induit | induise','The final compact body does not cleanly separate a short t cross from two low s/e joins.','medium')
old6=r'\unsure{a}';new6=r'\unsure{a|\alpha}'
A.replace(r'\deleted{tel que et \unsure{a}}',r'\deleted{tel que et \unsure{a|\alpha}}')
e6='Tel que and et remain recoverable through the strike: et has a low e and tall t. The last looped crossed token may be a or alpha; the original a preference is retained with that alternative. The live tel que and equality are separate.'
A.change('P06_b',final=r'\deleted{tel que et \unsure{a|\alpha}}',evidence=e6,confidence='medium')
A.update('doubts','place','P06 cancelled final token',reading=r'\deleted{tel que et \unsure{a|\alpha}}',alternatives='a | alpha',reason='The loop and right tail remain visible, but the strike prevents separating Latin a from alpha.')
A.inventory('E17',first_words_or_objects='tel que et; a/alpha-like final token')
old9=r'\unsure{-R_{>0}}';new9=r'\unsure{-R_{>0}|-\text{lors}}'
A.replace(old9,new9)
e9='The rotated note shows les and the terminal low joins of voisinages/côniques; the underlined word has a small continuation after germe, supporting germes. The verb has no independent accent recoverable above its e. Des and the strict(s) ending remain uncertain. After the larger-neighbourhood T, a horizontal and looped/lowered group are present, but their separation as R with >0 or as a compressed word lors cannot be fixed; the existing mathematical candidate remains preferred with the textual alternative explicit.'
A.change('P09_d',final=A.get('changes','id','P09_d')['final'].replace(old9,new9),evidence='The (1+epsilon)T portion is clear. The following horizontal and looped lower group support the existing doubtful -R_{>0} candidate, but a compressed -lors also fits its joins; neither is promoted to a secure reading.',confidence='low')
A.update('doubts','place','P09 marginal final mathematical group',reading=new9,alternatives='-R_{>0} | -lors',reason='The loop, lower marks and horizontal are visible, but do not securely distinguish a formula from a compressed textual continuation.')
A.update('decisions','id','M0332',reading=r'(1+\varepsilon)T'+new9,decision='undecided',evidence='The first candidate is retained, but the independent second reading identifies a plausible textual -lors outline; the root crop does not separate its letter joins from the supposed index marks.',confidence='low')
old11=r'\deleted{il est}';new11=r"\deleted{\unsure{il est|l'on}}"
A.replace(old11,new11)
e11='The crossed group after Si begins with a tall l-like stroke and compressed low continuation. It does not securely distinguish il est from l’on; the former remains preferred, with the uncertainty restored. The separate A-like triangular body has its own crossbar and uncertain cancellation/marking function, while T is visibly inserted above. No est un is supplied.'
A.change('P11_a',final=A.get('changes','id','P11_a')['final'].replace(old11,new11),evidence=e11,confidence='low')
A.inventory('E24',first_words_or_objects=r"\unsure{il est|l'on}")
A.doubt('P11 cancelled opening',r"\unsure{il est|l'on}",'il est | l’on','The strike covers the low middle bodies; only the early tall stroke and short continuation are separable.','low')
for row in A.comp:
 b=row['box']
 if row['token_equal']:continue
 if b=='B05':A.decide(b,e5,S[b]['first'].replace(old5,new5))
 elif b=='B06':A.decide(b,e6,S[b]['first'].replace(old6,new6))
 elif b=='B09':A.decide(b,e9,S[b]['first'].replace(old9,new9))
 elif b=='B11':A.decide(b,e11,S[b]['first'].replace(old11,new11))
 else:A.decide(b,ret[b])
for b,fr in [('B04',(.78,.15,1,1)),('B05',(.52,.29,.75,.60))]:
 im=Image.open(W/f'crops/150_scan015_second_{b}.png');box=tuple(int(v*(im.width if i%2==0 else im.height)) for i,v in enumerate(fr));im.crop(box).save(W/f'crops/150_scan015_root_{b}_detail.png')
A.append('notes',id='N99',text='Independent audit: root inspected all 11 nonidentical second-reading crops and two enlarged target details. Four boxes gain narrowly stated uncertainty alternatives; their preferred readings are retained. No uncertainty-only addition has been promoted into a new primary C correction. The first/second readings remain fixed.')
A.save()
