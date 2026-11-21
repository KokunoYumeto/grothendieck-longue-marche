from pathlib import Path
import json,re
r=Path('/workspace/scratch/8759b8008681')
page='150_scan020'
out=r/'work/reports'/page
C=(r/'packets'/page/'C.tex').read_text()
H=(r/'packets'/page/'H.tex').read_text()
D=(out/'draft.tex').read_text()
boxes=json.loads((out/'crop_boxes.json').read_text())
changes=[]
def sub(s,a,b):
 i=s.index(a); return s[i:s.index(b,i)+len(b)]
def add(id,p,place,c,h,final,evidence,confidence='high',kind='other',ac=True,ah=True,cat='10',mh=False,con=False):
 changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{page}_{p}.png',box=boxes[p],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=mh,consequential=con,error_category=cat))
add('P00','P00','Upper-left author number',r'\mspage{5}','« 5) »',r'\mspage{5)}','The digit has a short top cap and curved lower bowl; the separate long right parenthesis turns underneath it. That lower curve belongs to the parenthesis, not an independent underline. H quotes the complete number in an editorial note.',kind='omission',ac=True,ah=False,cat='3')
add('P01','P01','First system tuple, old closing delimiter',sub(C,'$(X,Y,',')$ où').removesuffix(' où'),r'$(X,Y,(X_i)_{i\in I},T)$',sub(D,'$(X,Y,',')$ où').removesuffix(' où'),'The entire tuple was read: X, Y, indexed (X_i), comma and one-roof T. Between the index I and the comma is a tall crossed curly group with upper/lower turns. A closing brace is plausible but overtracing prevents certain orientation and segmentation. It is retained as a doubtful cancellation rather than omitted as in H.',confidence='low',kind='omission',ac=False,ah=True,cat='3',con=True)
add('P02','P02','Conical-neighbourhood adjective and overwritten opening','conique',r'\struck{conique} \add{\uncertain{conique}}','cônique','Only one continuous word body is present: the descending q and following u/e are not crossed by a separate strike, and there is no second complete copy. A broad detached curved accent lies above the o region. The initial c/o/n region contains a tall additional stroke and heavy retracing, but no earlier complete word can be recovered. The accent and one-body reading are retained; revision chronology remains in doubts.',confidence='medium',kind='abbreviation expanded or spelling modernised',cat='8',mh=True)
add('P03','P03','Base glyph after de',r'$\unsure{Y|X_i}$',r'\struck{$Y$} \add{\uncertain{$Y$}}',r'$\unsure{Y|X_i}$','Two large diagonal arms meet at a dark centre, while the lower-right region is almost filled and has small loops/returns. Those strokes admit Y over an earlier X_i or a retraced X_i but do not isolate two independent Y tokens. C\'s candidate order is retained, and H\'s certain two-state duplication is not adopted.',confidence='low',kind='deletion state (struck given live or live given struck)',ac=False,ah=True,cat='7',mh=True,con=True)
add('P05','P05','Family endpoint and isomorphism parenthesis',r'$(X_i)$. (pour les iso),',r'$(X_i)$ (morphismes les iso),',r'$(X_i)$. (pour les iso),','A separate dark period follows the closing family parenthesis. The following short word has one p descender and low joined our strokes; it cannot accommodate the repeated tall/descending strokes of morphismes. The following les, dotted i, short s, closed o, closing parenthesis and comma are distinct.',kind='misread word',ac=False,ah=True,cat='2',con=True)
add('P06a','P06','Second system tuple, extra old delimiter before Y',r'(X_i^*),Y,',r'(X_i^{*}),Y,',r'(X_i^*),\deleted{\unsure{\}}}Y,','Immediately before the live forked Y is an additional tall curly stroke: a top hook, middle turn and lower loop survive, partly overlain by Y. Its relation to the live Y is overwriting, with a closing brace the preferred old token. The old-token shape remains explicitly doubtful rather than being supplied with certainty.',confidence='low',kind='omission',cat='3',con=True)
add('P06b','P06','Second tuple, cancelled token before final dotted X',r'\deleted{\unsure{f}}\dot X\longrightarrow Y',r'\ \dot X\to Y',r'\deleted{\unsure{f}}\dot X\unsure{\longrightarrow|\mathrel{\relbar\joinrel\relbar}}Y','A separate curled/crossed token precedes the final dotted X. It has an upper slant and a heavily blackened lower return, so f remains a candidate rather than a resolved letter. The full formula was checked, including both stars and dots. The final connector has a very small filled triangular-looking right termination; arrow is preferred, with headless alternative retained as a new certainty doubt only.',confidence='low',kind='omission',ac=False,ah=True,cat='3',con=True)
add('P06c','P06','End of second tuple',r'\longrightarrow Y)\n\]'.replace('\\n','\n'),r'\dot X\to Y)$,',r'\dot X\unsure{\longrightarrow|\mathrel{\relbar\joinrel\relbar}}Y)','The closing parenthesis ends the tuple. The saved crop includes its complete right edge and blank space below/right; no independent comma follows it. H adds such a comma.',kind='text not on the page',ac=False,ah=True,cat='9')
add('P07a','P07','Topological-spaces abbreviation','espaces top.,','espaces top.,',r'espaces top\textsuperscript{s},','After the low top body is a small raised curved s-like shape, followed by an independent baseline comma. The raised glyph is not a round period. Both witnesses flatten it to top.; the written superscript ending is retained.',confidence='medium',kind='abbreviation expanded or spelling modernised',cat='8')
add('P07b','P07','Comma after second-category family',r'$\dot X$ et $X_i^*$, parties',r'$\dot X$ et $X_i^{*}$ parties',r'$\dot X$ et $X_i^*$, parties','A separate descending comma follows X_i^* before parties. The dotted X, the family star and the final unstarred X of the line are all separately visible.',kind='omission',ac=False,ah=True,cat='3')
add('P08','P08','Start of equivalence assertion','Les deux\ncatégories','Ces deux catégories','Ces deux\ncatégories','The first capital is an open curved C with a continuous low exit into es, without the tall stem and lower foot of L. The preceding application continue ends with a distinct period.',kind='misread word',ac=True,ah=False,cat='2')
add('P09a','P09','Raised Si clause',r'\inserted{Si $\bar T$ voisinage conique strict}',r'\add{Si $T$ voisinage conique \emph{strict}}',r'\inserted{Si $T$ voisinage cônique strict}','The raised T has one roof joined to a stem, not an extra overbar. A detached arch appears over o in cônique. The long line below the clause extends far beyond strict and turns at both ends as a leader/bracket; there is no separate word-only underline beneath strict.',kind='insertion or placement',cat='6',con=True)
add('P09b','P09','Live Pour que T soit strictement under the Si insertion','Pour que $\\bar T$\nsoit \\uline{strictement}',r'\struck{Pour que $T$ soit strictement}','Pour que $T$\nsoit \\uline{strictement}','The Si leader crosses only the upper stem of P, then runs above the bodies of Pour que T. Those words have no independent cancellation. The T again has only one roof. On the next line soit is live and the straight stroke lies below strictement rather than through it. H\'s broad cancellation is therefore not retained.',kind='deletion state (struck given live or live given struck)',cat='7',con=True)
add('P10','P10','Compatibility wording replaced by transversality',sub(C,r'\deleted{compatible avec les}',r'\inserted{transversal aux}'),sub(H,r'\add{\uncertain{transversal}}',r'\add{\uncertain{aux}}'),sub(D,r'\deleted{compatible avec les}',r'\inserted{transversal aux}'),'The old compatible has the low opening joins, p descender and tall t/b/l strokes; the following avec and les remain under their separate continuation strikes. Above them the short raised line reads transversal aux, with a final cross in aux. The old les is readable and belongs after avec; H replaces part of this old sequence by illegibility and omits les.',confidence='medium',kind='readable ink left as \\ill{}',ac=False,ah=True,cat='5',mh=True,con=True)
add('P11a','P11','First sufficiency short form',r'il faut s. que $\dot X$',r'il faut et il suffit que $\dot X$',r'il f. \unsure{et|t} s. que $\dot X$','There is a tall descending f, a separate dark stop, then a small low entry leading into a taller t-like return, followed by s and its stop. No separate au body supplies faut. The small middle group is best read et, but its e is compressed enough to retain t as a local alternative. Neither witness preserves this actual short sequence.',confidence='medium',kind='abbreviation expanded or spelling modernised',cat='8',con=True)
add('P11b','P11','Boundary-subspace term','un sous-espace bord\nde','un sous-espace bordant de','un sous-espace bord\nde','The word has initial tall b, a low joined or body and terminal d turn; the line ends after that d. There is no following ant body before de begins on the next line. H\'s bordant expands the written term.',kind='abbreviation expanded or spelling modernised',ac=False,ah=True,cat='8',con=True)
add('P12a','P12','Decorated X-star in boundary condition',r'de $X^*$,',r'de $X^{*}$,',r'de $\unsure{\dot X^*|X^*}$,','A separate dark oblique point lies above X, apart from the star at its upper right. It is comparable in position to the page\'s dotted X forms, but elongated into a short slash. Preferred dot X-star retains the mark; plain X-star is left as an interpretation alternative rather than silently deleting that ink. A mathematical expectation of X-star does not remove it.',confidence='medium',kind='omission',cat='3',con=True)
add('P12b','P12','Cancelled underlined word before compatible',r'\deleted{\unsure{strict}}','(nothing)',r'\deleted{\uline{\unsure{strict}}}','The short old word has a separate straight underline below its body as well as several diagonal cancellation strokes through it. Initial s/t-like and final t-like forms support strict, but central letters cannot all be isolated from the strike, so C\'s doubt remains. H omits the whole old word; C omits its underline.',confidence='low',kind='omission',cat='3',con=True)
add('P13','P13','T in equisingularity condition',r'Pour que $\bar T$ soit équisingulier pour',r'Pour que $T$ soit équisingulier pour',r'Pour que $T$ soit équisingulier pour','The glyph has one long horizontal roof. The stem below it is retraced with a curved return, but no second independent roof/bar can be separated. It is transcribed T, without inventing either an additional bar or a recoverable prior C.',confidence='medium',kind='misread symbol or index',ac=True,ah=False,cat='1',con=True)
add('P14a','P14','Second sufficiency short form',r'$(X_i)$, il faut s. que',r'$(X_i)$, il faut et il suffit que',r'$(X_i)$, il f. \unsure{et|t} s. que','Again the long f is followed by a detached dot and a short upward group ending in t, then s with a stop. There are no clear au humps. The small initial stroke of the middle group supports et but does not settle it beyond doubt; the local et|t alternative is retained.',confidence='medium',kind='abbreviation expanded or spelling modernised',cat='8',con=True)
add('P14b','P14','Complete three-object fibration diagram',sub(C,r'\diagram{\[',r'\]}'),sub(H,r'\[',r'\]'),sub(D,r'\diagram{\[',r'\]}'),'Counted twice: three written objects, one horizontal right-pointing connector with a small dark terminal head, and one separate upward-open cup between the two left objects. There is no vertical arrow shaft. A distinct comma follows Y. C omits this comma; H\'s single centred array does not retain the cup\'s alignment directly beneath dot X. The family object has both outer parentheses and a dot above X.',kind='drawing or diagram',cat='4',con=True)
add('P15','P15','Local-triviality abbreviation','localement','localement',r'localem\textsuperscript{t}','The ending t stands distinctly above the low baseline of the compressed preceding m strokes. The intervening full ent of an expanded localement is not separately written. The elevated terminal letter is preserved as the abbreviation localem with raised t.',confidence='medium',kind='abbreviation expanded or spelling modernised',cat='8')
add('P16','P16','Thin lower-left foliation',r'\margin{19}','(nothing)',r'\margin{19}','The lower-left thin marks are a straight 1 with an entry slant and a closed upper bowl/long descending return of 9. They differ in weight from the main writing; hand attribution remains uncertain. H\'s commentary about the blank lower sheet does not transcribe this foliation.',kind='omission',ac=False,ah=True,cat='3')

report=dict(page=page,reader='reader_b',line_count=len(D.splitlines()),changes=changes)
report['decisions']=[dict(id='M0352',cote='150',scan='20',decision='undecided',reading=r'\unsure{Y|X_i}',evidence='P03 shows crossing upper arms and a filled lower-right group with small looped returns; it does not separate a clear final Y from possible X_i remains or establish two independent states. Retain both candidates, Y first, without an asserted duplicate deletion/insertion.',crop=f'crops/{page}_P03.png',box=boxes['P03'],confidence='low')]
inv=[]
def item(kind,pos,text,hand='his hand'):
 inv.append(dict(scan=page,sheet_kind='text',hand=hand,element=f'E{len(inv)+1:02}',kind=kind,position=pos,first_words_or_objects=text,transcribed='yes'))
item('text','Upper-left [35,25,120,100]','5)')
item('text','Upper main paragraph, y95–365',r'\uline{Proposition} Considérons la cat. des systèmes')
item('deletion','First tuple after family index, P01',r'\deleted{\unsure{\}}}')
item('text','Conical adjective at y410–495, P02','cônique; opening retraced, earlier token unrecoverable')
item('text','Overworked base glyph, P03',r'\unsure{Y|X_i}')
item('deletion','First compatible on baseline, P04',r'\deleted{compatible}')
item('insertion','Above first compatible, P04',r'\inserted{compatible}')
item('text','Parenthesis line y510–585, P05','(pour les iso), et la catégorie')
item('display','Second system tuple y600–735, P06',r'(X^*,\dot X,(X_i^*),Y,\dot X\longrightarrow Y) with recorded old tokens')
item('deletion','Before Y in second tuple, P06',r'\deleted{\unsure{\}}}')
item('deletion','Before final dotted X in second tuple, P06',r'\deleted{\unsure{f}}')
item('text','Second-category data y745–840, P07',r'X^*,Y espaces top\textsuperscript{s}; dot X et X_i^*, parties fermées de X')
item('text','Map and application prose y870–950, P08',r'\dot X\longrightarrow Y application continue. Ces deux')
item('text','Equivalence conclusion y1000–1060','catégories sont équivalentes.')
item('insertion','Raised right-side two-line clause y950–1020, P09',r'Si T voisinage cônique strict')
item('text','Main condition y1010–1170, P09–P10',r'Pour que T soit \uline{strictement}')
item('deletion','Old compatibility condition y1110–1160, P10',r'\deleted{compatible avec les}')
item('insertion','Above old compatibility condition, P10',r'\inserted{transversal aux}')
item('text','Boundary condition y1200–1395, P11–P12',r'il f. \unsure{et|t} s. que dot X soit un sous-espace bord de \unsure{dot X^*|X^*}')
item('deletion','Underlined crossed word y1325–1390, P12',r'\deleted{\uline{\unsure{strict}}}')
item('text','Equisingularity condition y1430–1635, P13–P14','Pour que T soit équisingulier pour (X_i), il f. et s. que')
item('diagram','Right lower main text y1545–1725, P14',r'\dot X\longrightarrow Y, with (\dot X_i) below dot X and a vertical cup')
item('text','Final two lines y1730–1940, P15',r'soit une fibration localem\textsuperscript{t} triviale simultanée (où on pose \dot X_i=X_i\cap\dot X)')
item('margin note','Thin lower-left foliation [20,2280,90,2345]','19','uncertain hand')
report['inventory']=inv

A=[]
def audit(p,kind,reading,xy=None):
 A.append(dict(box=f'B{len(A)+1:02}',kind=kind,xyxy=xy or boxes[p],reading=reading))
audit('P00','handwritten number','5)')
audit('P01','struck passage; doubtful formula',sub(D,'$(X,Y,',')$ où').removesuffix(' où'))
audit('P02','C/H different words; less than high confidence departure','cônique')
audit('P03','doubtful formula',r'\unsure{Y|X_i}')
audit('P04','insertion; struck passage',r'\deleted{compatible}\inserted{compatible} avec')
audit('P05','C/H different words',r'$(X_i)$. (pour les iso), et la catégorie')
audit('P06','struck passage; doubtful formula; less than high confidence departure',sub(D,'(X^*,',r'Y)'))
audit('P07','C/H different words; less than high confidence departure',r'$X^*,Y$ espaces top\textsuperscript{s}, $\dot X$ et $X_i^*$, parties fermées de $X$,')
audit('P08','C/H different words',r'$\dot X\longrightarrow Y$ application continue. Ces deux')
audit('P09','insertion; C/H different words',r'\inserted{Si $T$ voisinage cônique strict} Pour que $T$')
audit('P10','insertion; struck passage; C/H different words',r'soit \uline{strictement} \deleted{compatible avec les}\inserted{transversal aux} $X_i$,')
audit('P11','C/H different words; less than high confidence departure',r'il f. \unsure{et|t} s. que $\dot X$ soit un sous-espace bord')
audit('P12','struck passage; doubtful formula; less than high confidence departure',r'de $\unsure{\dot X^*|X^*}$, \deleted{\uline{\unsure{strict}}} compatible avec les $X_i^*$.')
audit('P13','doubtful formula; less than high confidence departure',r'Pour que $T$ soit équisingulier pour')
audit('P14','C/H different words; less than high confidence departure',r'$(X_i)$, il f. \unsure{et|t} s. que '+sub(D,r'\diagram{\[',r'\]}'))
audit('P15','C/H different words; less than high confidence departure',r'soit une fibration localem\textsuperscript{t} triviale simultanée (où on pose $\dot X_i=X_i\cap\dot X$)')
audit('P16','handwritten number; margin note','19')
report['audit_boxes']=A
report['doubts']=[
 dict(place='P01 old delimiter',reading=r'\deleted{\unsure{\}}}',alternatives='closing brace; exact old curly token unresolved',confidence='low',reason='The cancellation crosses the narrow upper/lower turns, preventing secure segmentation.'),
 dict(place='P02 overwritten opening of cônique',reading='cônique',alternatives='unrecoverable earlier initial stroke(s); no second complete word',confidence='medium',reason='The tall initial remnant and filled c/o region are real, but no earlier full reading or complete-word cancellation can be separated. The final live body and accent are legible.'),
 dict(place='P03 base glyph',reading=r'\unsure{Y|X_i}',alternatives='Y; X_i; chronology of lower-right overwork',confidence='low',reason='The lower-right body is filled, with several loops that may belong to overwritten index/letter or retracing. No two independently readable Y tokens are present.'),
 dict(place='P06 old delimiter before Y',reading=r'\deleted{\unsure{\}}}Y',alternatives='closing brace; other overwritten curly stroke',confidence='low',reason='Additional top/middle/lower curls survive to the left of Y, but Y crosses their lower return.'),
 dict(place='P06 cancelled token before final dotted X',reading=r'\deleted{\unsure{f}}',alternatives='f; unreadable old mathematical token',confidence='low',reason='A curled top and dark lower return remain, but the strike fills the letter body.'),
 dict(place='P06 final tuple connector',reading=r'\unsure{\longrightarrow|\mathrel{\relbar\joinrel\relbar}}',alternatives='right arrow; unheaded horizontal connector',confidence='medium',reason='A very small filled triangular termination favors the arrow, but independent head arms are not secure at this size. This is added uncertainty, not a changed preferred reading against either witness.'),
 dict(place='P11 first sufficiency short form',reading=r'f. \unsure{et|t} s.',alternatives='f. et s.; f. t s.',confidence='medium',reason='The stop after f is separate. The next group has a short entry and tall t-like ending; the small e may be compressed into that entry.'),
 dict(place='P12 decoration above X-star',reading=r'\unsure{\dot X^*|X^*}',alternatives='dotted X-star; plain X-star with an unassigned oblique mark',confidence='medium',reason='An independent dark oblique mark is certain; its interpretation as a dot is preferred by position but its slash-like shape leaves doubt. The plain alternative does not deny the physical mark.'),
 dict(place='P12 cancelled underlined word',reading=r'\deleted{\uline{\unsure{strict}}}',alternatives='strict; middle letters unresolved',confidence='low',reason='Separate underline and cancellation are clear. Every letter cannot be isolated under the diagonal strikes, so the old C doubt is not resolved.'),
 dict(place='P13 retraced T body',reading='T',alternatives='earlier token/chronology unrecoverable; no separately certain C or overbar',confidence='medium',reason='One long roof is secure, but the looped/retraced stem should not be converted into an invented additional letter or second bar.'),
 dict(place='P14 second sufficiency short form',reading=r'f. \unsure{et|t} s.',alternatives='f. et s.; f. t s.',confidence='medium',reason='The f and its dot are separate from the next short upward body; the latter can carry a compressed e before t but cannot prove every letter.'),
]
report['notes']=[
 dict(id='N01',text='The leaf is headed Proposition and is numbered 5), with a later thin 19 in the lower-left margin. It asserts an equivalence between the category of systems (X,Y,(X_i),T), explicitly restricted by the parenthesis (pour les iso), and a category of exterior/boundary data (X*, dot X, (X_i*), Y, dot X to Y). The final two assertions concern strict transversality and equisingularity. This paragraph reports the source; it is not a proof of the equivalence.'),
 dict(id='N02',text='Literal source states and apparent slips are retained. The added Si T voisinage cônique strict does not visibly cancel the live Pour que T soit strictement beneath it, so the resulting prose remains syntactically unreconciled. The second-category sentence calls dot X and X_i* closed parts of X, not X*. In the later boundary condition an independent oblique upper mark gives preferred dot X* where the argument would normally call for X*. The final definition uses dot X_i = X_i intersect dot X, with no star on its right-hand X_i. None of those forms has been repaired from the intended construction.'),
 dict(id='N03',text='Main-reader deduction, checked here on the specified example: under a broad compatibility convention allowing a full-ray subcone S=(A times I) union C with f(A) contained in C, exterior family data need not determine the base subset C. Let Y={a,b} be discrete, X=T=Y times [0,1], base Y times {0}, boundary dot T=Y times {1}, and X*=dot T. Compare a one-member family X_i=empty with X_i={(a,0)}. Both are closed, action-invariant subcones under that broad convention, and both have X_i*=empty. Their exterior data (X*,dot X,(X_i*),Y,f) coincide, with f the two-point identity under the evident identifications, but the first-category systems cannot be isomorphic because an isomorphism cannot carry the empty family member to a nonempty one. Thus the canonical exterior-data assignment is not an equivalence under that interpretation. A strict/full-base condition C=f(A), or an equivalent hypothesis retaining the base subsets, excludes this example. The assigned leaf does not itself specify enough definitions to decide which interpretation was intended.'),
 dict(id='N04',text='Main-reader deduction, independently checked on the described graph: suppose conical neighbourhood means only a closed conical subspace that is a neighbourhood of its base, without a further ambient gluing/interior condition. Let X be the horizontal interval [0,1] with a vertical interval attached at q=3/8, let Y={0}, and let T=[0,1/2] on the horizontal interval, with dot T={1/2} and its ordinary radial interval action. T is a closed conical neighbourhood of Y. The exterior X*=X minus [0,1/2) consists of the horizontal [1/2,1] and the punctured vertical branch; the attachment point q has been removed. Those two components are disconnected in X*. Gluing T to X* only at dot T reconstructs a horizontal interval disjoint from that punctured branch, whereas the original graph X is connected. Therefore the canonical reconstruction fails under this broad neighbourhood interpretation even with no family. If the earlier definition requires the ambient gluing property or openness of the stated interior, this example is excluded; that assumption is not supplied on the present leaf.'),
 dict(id='N05',text='Targeted conditional check by this reader: if T and X*=X minus the designated interior are both closed in X, cover X, and intersect exactly in dot T, then their subspace topologies recover X as the pushout along dot T. Indeed a subset F of X is closed whenever F intersect T and F intersect X* are closed in those two spaces, because they are then closed in X and F is their finite union. This proves the final-topology/gluing assertion under the stated extra hypotheses. It does not resolve the independent family-information loss in N03 and is not claimed as a verification that the source hypotheses already imply these conditions.'),
 dict(id='N06',text='The page records a boundary-subspace criterion for strict transversality and a simultaneous local-triviality criterion for equisingularity. The three-object diagram places (dot X_i) below dot X with an upward-open cup, and maps dot X to Y. Definitions sufficient for an independent proof of these two equivalences are not supplied on the assigned leaf, so they are carried as source assertions without a claimed proof check.'),
]
report['check_events']=[
 dict(statement_id=page+'.N01',type='carried as background without fault found',outcome='Source proposition and category data transcribed; no proof is claimed by this event. Qualifications and counterexamples to broad interpretations are recorded separately in N03–N05.'),
 dict(statement_id=page+'.N02',type='used and rechecked in this run',outcome='All literal decorations, short forms and revision scopes in this note were checked against the saved crops; no mathematical repair was made.'),
 dict(statement_id=page+'.N03',type='targeted proof check',outcome='Checked the main-reader two-point example under the explicitly stated full-ray compatibility convention: both exterior families are empty, while empty and nonempty original family members cannot be related by an isomorphism.'),
 dict(statement_id=page+'.N04',type='targeted proof check',outcome='Checked the main-reader branching example: the punctured vertical branch is separated from the horizontal exterior, the gluing at 1/2 does not reattach it at q, and connectedness distinguishes the reconstruction from X.'),
 dict(statement_id=page+'.N05',type='independent re-proof',outcome='Proved the conditional finite-closed-cover pushout criterion by testing closed subsets and taking a finite union. This is conditional on the written extra hypotheses, not a proof of the unqualified source proposition.'),
 dict(statement_id=page+'.N06',type='carried as background without fault found',outcome='Transversality and simultaneous-fibration criteria are source reports only; absent definitions prevent an independent equivalence proof on this leaf.'),
]
report['notation']=[
 dict(form=r'T',meaning='Conical-neighbourhood object, retaining the locally visible single roof',evidence='P01, P09 and P13; the lower T has retracing but no second independent bar.'),
 dict(form=r'X^*,\dot X,(X_i^*)',meaning='Exterior/boundary/family data listed in the second category',evidence='P06 complete tuple and P07 closed-subsets sentence; no extra definition imported as source text.'),
 dict(form=r'\dot X_i=X_i\cap\dot X',meaning='Definition in the final parenthesis, preserving the unstarred right-hand X_i',evidence='P15 shows separate dots on the first and final X, lowered i on the first two X forms, and an intersection arch.'),
 dict(form=r'\cup written between stacked objects',meaning='Vertical containment of (dot X_i) in dot X, with no arrow shaft',evidence='P14 three-object diagram: cup directly beneath dot X.'),
 dict(form=r'\unsure{\dot X^*|X^*}',meaning='Locally decorated ambient symbol in the boundary condition; preferred dot retained without semantic normalization',evidence='P12 independent dark oblique upper mark and separate star at upper right.'),
]
report['abbreviations']=[
 dict(form='cat.',expansion='catégorie'),
 dict(form='top.',expansion='topologique'),
 dict(form=r'top\textsuperscript{s}',expansion='topologiques'),
 dict(form='iso',expansion='isomorphismes'),
 dict(form=r'f. \unsure{et|t} s.',expansion='Preferred reading f. et s.: faut et suffit; the middle group remains locally uncertain'),
 dict(form=r'localem\textsuperscript{t}',expansion='localement'),
]
report['hand']=[
 dict(habit='Single detached or connected roof can be misread as an added bar on T',places='P01 first tuple; P09 both T forms; P13 equisingularity T',consistency='One long roof at every reviewed occurrence; P13 stem is additionally retraced',witness_errors='C adds bars in the raised and later prose T forms.'),
 dict(habit='A broad detached accent is sometimes quite flat, and cônique retains that accent',places='P02 and P09',consistency='Both adjective occurrences on this leaf have separate upper accent ink',witness_errors='Both witnesses give conique without the accent; H also duplicates the first word as deletion/addition.'),
 dict(habit='Short forms keep raised endings and disconnected dots',places='P07 top with raised s; P11/P14 f. et s.; P15 localem with raised t',consistency='Each instance was checked locally; no automatic expansion used',witness_errors='Both witnesses flatten raised s/t and expand or missegment the sufficiency abbreviation.'),
 dict(habit='A long insertion leader can cross a capital ascender without cancelling the sentence',places='P09 Si clause over Pour que T',consistency='The stroke is continuous beneath the raised clause and does not cut the lower word bodies',witness_errors='H marks Pour que T soit strictement struck.'),
 dict(habit='Curly old delimiters can survive as crowded strokes adjacent to live tuple symbols',places='P01 before comma/T; P06 before Y',consistency='Closing-brace interpretation remains doubtful at both places',witness_errors='H omits P01; both witnesses omit the additional old curve before Y in P06.'),
 dict(habit='Thin foliation differs visibly in weight from body numbering',places='P00 dark5) versus P16 thin19',consistency='Hand identity is not inferred from the weight difference alone',witness_errors='C drops the author number\'s closing parenthesis; H does not transcribe thin19.'),
]
report['diff_coverage']=[
 dict(row=1,disposition='Editorial page/heading metadata; actual author 5) covered by P00. H\'s explanatory sentence is not source prose.'),
 dict(row=2,disposition='Editorial explanation omitted from transcription; physical closing parenthesis of 5) retained by P00.'),
 dict(row=3,disposition='P02: one live cônique body with unresolved opening overwork, not two complete word states.'),
 dict(row=4,disposition='P03/M0352: Y|X_i remains unresolved; H\'s two-Y state inference not adopted.'),
 dict(row=5,disposition='P05: dark period after (X_i) retained.'),
 dict(row=6,disposition='P05: short pour, not morphismes.'),
 dict(row=7,disposition='Display-delimiter/macro difference only; the source tuple itself reviewed in P06.'),
 dict(row=8,disposition='P06b: cancelled doubtful f retained; not omitted.'),
 dict(row=9,disposition='Display closing syntax itself is macro-only; P06c records the material absence of H\'s post-tuple comma.'),
 dict(row=10,disposition='P07b: comma after X_i* retained.'),
 dict(row=11,disposition='P08: Ces, with open capital C, accepted against C\'s Les.'),
 dict(row=12,disposition='P09b/P10: strictement remains live/underlined, transversal aux is raised replacement of cancelled compatible avec les.'),
 dict(row=13,disposition='P10: complete cancelled words and replacement attachment retained; H\'s old les omission/illegibility rejected.'),
 dict(row=14,disposition='P11a: literal f. et|t s. retained; neither faut s. nor expanded et il suffit.'),
 dict(row=15,disposition='P11b: bord ends at d; bordant not written.'),
 dict(row=16,disposition='P12b: cancelled underlined doubtful strict retained.'),
 dict(row=17,disposition='P14a: same short sufficiency sequence as first instance, with local et|t doubt.'),
 dict(row=18,disposition='P14b: complete three-object diagram set in tikz-cd; source positions preserved rather than a centred one-column array.'),
 dict(row=19,disposition='P14b: both source/witnesses give a right connector; tiny terminal arrowhead checked locally.'),
 dict(row=20,disposition='P14b: comma after Y added against C, and cup aligned directly beneath dot X.'),
 dict(row=21,disposition='P14b: vertical cup preserved without an arrow shaft; macro syntax otherwise not an extra reading.'),
 dict(row=22,disposition='P16 records physical thin19. H\'s long explanatory note is editorial, not source. Its interpretation of the revision is superseded by P09–P10; its literal-X observation is preserved in N02.'),
]
report['deletion_insertion_review']=[
 dict(text=r'\deleted{\unsure{\}}} in first tuple',scope_attachment='Old delimiter immediately after family index and before comma/T; no other tuple symbol cancelled',evidence='P01 complete formula; curly turns crossed locally.'),
 dict(text='cônique',scope_attachment='One live word with unresolved initial overwork; no asserted second complete word or whole-word cancellation',evidence='P02 descending q/u/e remain continuous and unstruck; upper accent separate.'),
 dict(text=r'\unsure{Y|X_i}',scope_attachment='One overworked base position; no separately established pair of deleted/inserted Y tokens',evidence='P03 lower-right mass masks the old/new components.'),
 dict(text=r'\deleted{compatible}\inserted{compatible}',scope_attachment='First old baseline word struck; same word repeated immediately above it; avec remains live',evidence='P04 straight strike through baseline word and separate raised lettering.'),
 dict(text=r'\deleted{\unsure{\}}}Y in second tuple',scope_attachment='Additional old curly group immediately before/under Y; no cancellation of the whole Y',evidence='P06 top/middle/lower turns are partly crossed by live Y; old token doubtful.'),
 dict(text=r'\deleted{\unsure{f}}',scope_attachment='Short crossed token after Y comma and before the final dotted X; not an arrow label',evidence='P06 overworked curled group on the tuple baseline.'),
 dict(text=r'\inserted{Si $T$ voisinage cônique strict}',scope_attachment='Raised clause attached before live Pour que T; bracket/leader is not a broad strike and does not underline only strict',evidence='P09 line passes below the raised phrase, crosses only the high P stem, and turns at both ends.'),
 dict(text=r'soit \uline{strictement}',scope_attachment='Both words live; only strictement underlined',evidence='P10 independent straight lower stroke, without strike across letter bodies.'),
 dict(text=r'\deleted{compatible avec les}\inserted{transversal aux}',scope_attachment='Baseline phrase cancelled in three word groups; raised transversal aux replaces it before live X_i',evidence='P10 full revision and attachment inspected.'),
 dict(text=r'\deleted{\uline{\unsure{strict}}}',scope_attachment='Only the short old underlined word before compatible is cancelled; compatible avec les X_i* remains live',evidence='P12 diagonal crossing strokes and separate low underline do not extend through the following phrase.'),
]
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Built',len(changes),'changes,',len(report['decisions']),'mark,',len(inv),'inventory elements,',len(A),'audit boxes,',len(report['doubts']),'doubts,',len(report['diff_coverage']),'diff dispositions')
