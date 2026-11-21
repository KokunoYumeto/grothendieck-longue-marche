from pathlib import Path
import json
import re

R=Path('/workspace/scratch/8759b8008681')
P='150_scan016'
O=R/'work/reports'/P
C=(R/'packets'/P/'C.tex').read_text()
H=(R/'packets'/P/'H.tex').read_text()
D=(O/'draft.tex').read_text()
DC='\n'.join(l for l in D.splitlines() if not l.lstrip().startswith('%'))
B=json.loads((O/'crop_boxes.json').read_text())

def span(t,a,b):
 i=t.index(a)
 return t[i:t.index(b,i)+len(b)]

changes=[]
def ch(id,crop,place,c,h,f,e,ac=False,ah=True,confidence='high',kind='misread word',cat='2',mh=False,con=False):
 assert c in C,(id,'C',c)
 assert h in H,(id,'H',h)
 assert f in D,(id,'final',f)
 changes.append(dict(id=id,place=place,c=c,h=h,final=f,evidence=e,
  crop=f'crops/{P}_{crop}.png',box=B[crop],confidence=confidence,kind=kind,
  against_c=ac,against_h=ah,marked_in_h=mh,consequential=con,error_category=cat))

ch('P01a','P01','Author number at upper left',r'\mspage{3}','« 3) »',r'\mspage{3)}',
 'The angular upper bend and lower rounded lobe form 3. A separate long closing parenthesis sweeps beneath and to the left of the digit; it is not an independent underline. Only the written number is retained from H’s editorial foliation note.',True,False,kind='omission',cat='3')
ch('P02a','P02','Cancelled opening words',r'$X$ muni de sous-espaces',r'$X$ \ill{} de \ill{} espaces',
 r'$X$ \unsure{muni de sous-espaces}',
 'After the second X the low m/u/n sequence and a separate i dot remain visible under the long strike. The looped d and low e follow, then a compressed sous body, the space-word p descender and final s. The long cancellation masks some joins, so the complete wording remains doubtful rather than being declared fully recovered.',confidence='medium',kind='readable ink left as \\ill{}',cat='5',mh=True)
ch('P02b','P02','Raised replacement after Soit',
 r'\inserted{$\bar T$ un vois. \deleted{tub.} conique absolu de $Y$.}',
 r'$T$ un voisinage \struck{tub.} conique absolu de $Y$.',
 r'\inserted{$T$ un vois. \deleted{tub.} conique absolu de $Y$.}',
 'The complete replacement sits above the crossed opening line. Its first T has one roof and upright only. The word is the short vois. with a distinct stop after s, followed by a separately cancelled tub. with its own stop; there is no inage continuation. The raised conique has no independent circumflex, unlike several later occurrences.',True,True,kind='abbreviation expanded or spelling modernised',cat='8')
ch('P03a','P03','Second opening Soit/Soient',r"Soit $\bar T'",r"Soient $T'",
 r'\unsure{Soit|Soient}',
 'S, o and the i dot are visible. The long low joining stroke before the terminal t can be either an extended connection or compressed en. Soit is preferred, with H’s Soient retained as an explicit alternative.',confidence='medium',cat='2')
ch('P03b','P03','Complete first T-prime inclusion',r"\bar T'\deleted{\unsure{_\varepsilon}}\subset\bar T",
 r"T'\subset T",r"\unsure{T'_\varepsilon|T'\deleted{_\varepsilon}}\subset T",
 'Both T letters have single roofs. A small lowered epsilon-like body is present beside the first T and below its prime; it is dark and retraced but lacks a secure independent cancellation stroke. The letter and its state are left doubtful, with live lowered epsilon preferred and deletion retained as an alternative. H omits the group.',True,True,'medium','deletion state (struck given live or live given struck)','7',con=True)
ch('P03c','P03','Definition sentence: the two T forms and source spelling',
 r"On dit que $\bar T'$ est \uline{sous-espace conique} dans $\bar T$ si on a",
 r"On dit que $T'$ est \emph{sous-espace conique} dans $T$ si on a",
 r"On dit que $T'$ est \uline{sous-espace cônique} dans $T$ si on a",
 'Each T has only its own horizontal roof. In the second line a separate short curved accent lies over the o of cônique. The underline continues the term sous-espace across the line break; no spelling normalization is made.',True,True,kind='misread symbol or index',cat='1')
ch('P04a','P04','Condition (12)a: homothéties and parameter',
 r"\bar T'\text{ stable par homothéties }\lambda\in I",
 r"$T'$ stable par les multiplications $\lambda\in\mathbf{I}$",
 r"T'\text{ stable par homothéties }\lambda\in\mathbf{I}",
 'The word begins with the tall h and low o/m/o groups, then the paired tall th/t members and the accented ending of homothéties. No les precedes it, and the long multiplications sequence is absent. The parameter I has a fully dark thick upright with broad serif caps. The T-prime again has only one roof.',True,True,kind='misread word',cat='2')
ch('P04b','P04','Cancelled formula at the end of condition a',
 r"\deleted{\unsure{\lambda\bar T'\subset\bar T'}}",r'\struck{\ill{}}',
 r"\deleted{\unsure{\lambda T'\subset T'}}",
 'The crossed right-end group contains an initial lambda-like diagonal, roof/stem traces and a separately legible final T-prime. The intervening relation/body is partly hidden by the diagonal strike. The inherited lambda T-prime subset T-prime candidate is retained as doubtful, without C’s unsupported extra T bars. H’s editorial possibility absolu is not supported by the final mathematical T-prime.',True,True,'low','misread symbol or index','1',mh=True,con=True)
ch('P04c','P04','Condition b and the physical extent of the brace',
 r"b)&\text{Pour cette opération, }\bar T'\text{ est un voisinage}\\"+'\n'+r'&\deleted{\text{tubulaire}}\text{ conique de }Y.',
 r"b) Pour cette opération, $T'$ est un voisinage \struck{tubulaire} conique de $Y$.",
 r"b)&\text{\unsure{Pour} cette opération, }T'\text{ est un voisinage}"+'\n'+r'\end{array}\right.'+'\n'+r'\]'+'\n'+r'\deleted{tubulaire} cônique de $Y$.',
 'The initial P of Pour is overworked, with a small raised remnant; no separate earlier T-prime can be securely recovered. The later T-prime after opération is clear and unbarred. The brace terminates after the first b-line, while cancelled tubulaire and live cônique de Y return to the left on the line below. The o has a separate curved circumflex. The final Y has no prime.',True,True,'medium','insertion or placement','6',con=True)
ch('P05a','P05','NB: On aura',r'On aura nécessairement',r'On a nécessairement',r'On aura nécessairement',
 'After the first a body there is a long low u/r connection and a final a-like return before the space and nécessairement. The word extends beyond the single a read by H.')
ch('P05b','P05','NB first complete identity',r"\dot T'=\bar T'\cap\dot T",r"\dot T'=T'\cap\dot T",
 r"\unsure{\dot T'}=T'\cap\dot T",
 'The left dotted T-prime has a dark overtraced body, with its separate dot and prime still clear; its T reading is therefore retained with local doubt rather than an invented earlier symbol. The middle T-prime has a single roof only. Intersection and the final separate dot above T are clear.',True,False,'medium','misread symbol or index','1')
ch('P05c','P05','NB second identity and following punctuation',
 r"$\bar T'_\lambda=\bar T'\cap\bar T_\lambda$ ;",
 r"$T'_\lambda=T'\cap T_\lambda$,",
 r"$T'_\lambda=T'\cap T_\lambda$ ;",
 'All three T forms have one roof each; the two lowered lambdas and the prime positions remain distinct. The following dark punctuation has an upper point and a lower comma-like part, supporting the source semicolon. H substitutes a comma.',True,True,kind='misread symbol or index',cat='1')
ch('P06a','P06','Cancelled family clause',
 r'\deleted{Si $(\bar T_i)_{i\in I}$ est une famille}',
 r'\struck{si $(T_i)_{i\in I}$ est une famille,}',
 r'\deleted{Si $(T_i)_{i\in I}$ est une famille\unsure{,}}',
 'A large curved S-like initial and dotted i start the cancelled clause. The indexed T has one roof, not an added bar. The final famille retains its f descender and twin l ascenders below/above the strike. A small low return at the end may be a comma, but is not completely separable from the final letter/strike; punctuation remains doubtful.',True,True,'medium','misread symbol or index','1')
ch('P06b','P06','Raised la donnée replacement and its attachment',
 r"\inserted{la donnée de $\bar T'$ équivaut à}",
 r"\add{la donnée de $T'$ équivaut à celle}",
 r"\inserted{la donnée de $T'$ équivaut à}",
 'The raised line reads la donnée de T-prime équivaut à and ends with the accented short à above the old family clause. Celle begins the next normal baseline; it is not on this raised line. The T-prime has one roof. H’s insertion scope extends one word too far.',True,True,kind='insertion or placement',cat='6')
ch('P07a','P07','First live baseline after the replacement',
 r"celle d'un sous-espace fermé $\dot T'$ de $\dot T$",
 r"celle} d'un sous-espace $T'$ \struck{\ill{}} de \ill{} $Y$, fermé \struck{\ill{}}",
 r"celle d'un sous-espace fermé $\dot T'$ de $\dot T$",
 'This is one live upper baseline: celle, d’un sous-espace, then the tall f and compressed ermé, followed by dotted T-prime de dotted T. The long f descender enters the lower line but is not a strike. Both boundary dots are separate from the T roofs. H’s sequence interleaves the two baselines and converts crossing descenders into cancellations.',kind='deletion state (struck given live or live given struck)',cat='7',mh=True,con=True)
ch('P07b','P07','First lower-baseline variable and tel ending',
 r"et d'un sous-espace $Y'$ de $Y$, tel que",
 r"et d'un sous-espace $Y'$ de $Y$, tels que",
 r"et d'un sous-espace $\unsure{T'|Y'}$ de $Y$, tel que",
 'The first small variable has a nearly straight roof and short descending stem with a separate prime, more T-prime-like than the clearly forked Y after de. T-prime is preferred with Y-prime retained as an alternative because of the compressed body. The letters after the comma support tel, with no independent s before que; the crossing stroke belongs to the f of fermé above.',True,True,'medium','misread symbol or index','1',con=True)
ch('P07c','P07','Comma after the final et in the NB prose',
 r"tel que $Y'\supset0.\dot T'$, et",r"tels que $Y'\supset0.\dot T'$, et,",
 r"tel que $Y'\supset0.\dot T'$, et,",
 'A separate curved descending comma follows et at the right end of the lower baseline. It is distinct from both the comma after dotted T-prime and the next on a line.',True,False,kind='omission',cat='3')
ch('P08a','P08','Live on a before the image formula',r'on a',r'\uncertain{on a}',r'on a',
 'The initial small oval/dot, low n connection and separate a return are visible on the formula’s baseline. The larger oblique strokes to the left belong to the margin note, not a cancellation of on a.',mh=True)
ch('P08b','P08','Whole image formula: T roofs, interval glyph, raised ink and connector',
 span(C,r"\bar T'=\operatorname{Im}",r"\cup Y'."),
 r"T'=\mathrm{Im}(\mathbf{I}\times\dot T'\to T)\cup Y'.",
 span(D,r"T'=\operatorname{Im}",r"\cup Y'."),
 'Both plain T forms have only one roof. The interval glyph has two parallel thin stems joined to broad top/bottom caps, so it is set as double-struck I, distinct from the solid heavy I of a). A separate raised overworked mark at approximately x950–979,y930–944 has no recoverable candidate and is retained above I with an empty-content doubt, which records present ink and placement only. The preceding prose comma after Y is farther right, approximately x1028–1043,y908–925, with no connecting stroke. The lowered lambda-like group after dotted T-prime has uncertain cancellation state; live and deleted alternatives remain. The action shaft ends in a short upturn without a secure two-arm head, so an unheaded shaft is preferred with arrow alternative. The union, final Y-prime and stop are clear.',True,True,'medium','misread symbol or index','1',con=True)
ch('P09a','P09','Upper marginal definition and strict term',
 r"On dit que $\bar T'$ est conique \uline{\unsure{strict|pur}}",
 r"On dit que $T'$ est \uncertain{conique} \uncertain{strict}",
 r"On dit que $T'$ est cônique \uline{strict}",
 'The marginal T-prime has one roof. A separate curved accent lies over the o of cônique. The underlined word has the initial s/t pair, r connection, dotted i, c and terminal crossed t of strict; it has neither the p descender nor the short three-letter body of pur. This resolves C’s strict/pur choice.',True,True,kind='misread word',cat='2',mh=True)
ch('P09b','P09','Whole strictness identity and following line break',
 r"si $\bar T'\cap Y=0.\dot T'$,",
 r"si $\dot T'\cap Y=0.\dot T'$ \ldots\ ",
 r"si $T'\cap Y=0.\dot T'$",
 'The left T-prime has only its roof, stem and prime, with no dot. The right T-prime has a separate upper dot, as well as the low multiplication point after the round 0. No secure comma appears after the final prime before the next line’s dash. H adds a dot to the left T-prime and substitutes an ellipsis for the following continuation.',True,True,kind='misread symbol or index',cat='1',con=True)
ch('P09c','P09','Continuation of the upper margin note',
 r"--- \unsure{ces $\bar T'$ correspondent donc aux fermés}"+'\n'+r"$\dot T'$ de $\dot T$.",
 r"\uncertain{i.e.} $T'$ \ill{} \uncertain{ouvert} et fermé \ldots",
 r"--- ces $T'$ correspondent donc aux fermés"+'\n'+r"$\dot T'$ de $\dot T$.",
 'The new line begins with a long dash, then the c/e/s bodies of ces and plain T-prime. Correspondent has a retraced initial c/o, low r/s joins, a p descender and tall d before its ending; donc has a looped d, and aux precedes the tall f and accented/plural ending of fermés. The final two boundary T forms each have a separate dot. The full continuation is recoverable, though compressed, and does not contain ouvert et fermé.',True,True,'medium','readable ink left as \\ill{}','5',mh=True)
ch('P10a','P10','Structure sentence and resolved Y',
 r"On dira qu'une structure conique sur"+'\n'+r"un $\bar T\supset\unsure{Y}$",
 r"On dira qu'une structure conique sur un $T\supset Y$",
 r"On dira qu'une structure cônique sur"+'\n'+r"un $T\supset Y$",
 'Cônique has a separate curved accent over o. The first T has one roof. The following Y has a short curved left arm joining a flatter right arm and a descending stem, unlike a single straight T roof; that local fork resolves C’s Y doubt.',True,True,kind='misread symbol or index',cat='1')
ch('P10b','P10','Indexed subspaces and ambient T after fermés',
 r'\inserted{fermés} $\bar T_i$ de $\bar T$ $(i\in I)$',
 r'\add{fermés} $T_i$ de $T$ ($i\in I$)',
 r'\inserted{fermés} $T_i$ de $T$ $(i\in I)$',
 'The two T letters have their own single roof strokes; lowered i is separate. The index-set I is a thin one-stem serif letter, unlike the heavy/double-stem interval forms. Fermés is raised, and its curved attachment leader enters before T_i; that leader is not an extra underline.',True,False,kind='misread symbol or index',cat='1')
ch('P10c','P10','Plural côniques in the structure paragraph',
 r'sont coniques pour cette structure.',r'sont coniques pour cette structure.',
 r'sont côniques pour cette structure.',
 'A separate small curved stroke is above the o of côniques. The final plural s is present before pour. Both witnesses omit the accent.',True,True,kind='abbreviation expanded or spelling modernised',cat='8')
ch('P11a','P11','Lower paragraph: Soit T',r'Soit $\bar T$ un voisinage',
 r'Soit $T$ un voisinage',r'Soit $T$ un voisinage',
 'The large T consists of one broad roof and one descending upright, without a second bar. Conique in this particular line has no separate circumflex.',True,False,kind='misread symbol or index',cat='1')
ch('P11b','P11','Overworked initial of partie after X-prime',
 r"$X'$ partie fermée",r"$X'$ \struck{\ill{}} partie fermée",r"$X'$ \unsure{p}artie fermée",
 'The dark group is in the initial p position of partie: a long descending body with a retraced upper loop, followed directly by artie. No separate earlier whole word can be separated from it. The initial is marked doubtful rather than inventing an independent cancelled word as H does.',confidence='medium',kind='deletion state (struck given live or live given struck)',cat='7',mh=True)
ch('P12a','P12','First compatible: false asterisk and plain T',
 r'dit que $\bar T$ est \uline{compatible}$^{*}$ avec',
 r'dit que $T$ est \emph{compatible}\,* avec',
 r'dit que $T$ est \uline{compatible} avec',
 'The T has only its roof. The apparent small mark above the end of compatible is the hooked lower return of the f in fermée on the preceding line, traced through P11/P12. It has no independent star crossing. The genuine later star is separately visible in P13. Both witnesses turn this descender into an asterisk.',True,True,kind='text not on the page',cat='9',con=True)
ch('P12b','P12','Conical intersection in the compatibility definition',
 r"$X'\cap\bar T$ est conique dans $\bar T$.",
 r"$X'\cap T$ est conique dans $T$.",
 r"$X'\cap T$ est cônique dans $T$.",
 'Both T bodies have one roof only. The o of cônique has a separate short circumflex-like curve. The X-prime, intersection and final period are distinct.',True,True,kind='misread symbol or index',cat='1')
ch('P13a','P13','Strict compatibility: literal target T and true star',
 r'est \uline{strictement compatible}$^{*}$ avec $\bar T$, si',
 r'est \emph{strictement compatible}\,* avec $T$, si',
 r'est \uline{strictement compatible}$^{*}$ avec $T$, si',
 'A separate multi-point filled star stands above the end of compatible. The target after avec is a T with one roof and upright, no prime and no X crossing. The source target T is preserved even though the preceding definition concerns X-prime.',True,False,kind='misread symbol or index',cat='1',con=True)
ch('P13b','P13','Next line: T est voisinage conique strict',
 r"$\bar T$ est voisinage conique strict, et s'il existe",
 r"$T$ est voisinage conique strict, et s'il existe",
 r"$T$ est voisinage conique strict, et s'il existe",
 'There is only one T roof. In this occurrence of conique no independent curved accent sits over o; the word remains unaccented. The comma after strict is separate from the next et.',True,False,kind='misread symbol or index',cat='1')
ch('P14a','P14','Written equals-sign abbreviation in prose',
 r'ou ce qui revient au $=$',r'ou ce qui revient au même',r'ou ce qui revient au $=$',
 'Two distinct parallel horizontal strokes stand after au. The letters of même are not written. The source shorthand is retained.',kind='abbreviation expanded or spelling modernised',cat='8')
ch('P15a','P15','Terminal iso with no following punctuation',
 r'et un iso',r'et un iso\ldots',r'et un iso',
 'The final short word has dotted i, small s and a low o ending. Blank paper follows it; no three-dot group or full stop is written at the end of this line.',kind='text not on the page',cat='9')
ch('P16a','P16','First cancelled lower marginal note',
 r"\margin{\deleted{\unsure{Définir la notion pour $X'$}}}",
 r'\marginal{* \struck{\ill{}}',
 r"\margin{\deleted{\unsure{Définir la notion pour $X'$}}}",
 'The cancelled diagonal group has a tall D-like beginning, an e loop, f/i members, then compressed la notion and a p-like descender before the final crossed X with prime. Wide repeated zigzag strikes obscure several letters and small internal marks. The full inherited candidate remains doubtful; H gives no recoverable wording and conflates this separate note with the starred one below.',confidence='low',kind='omission',cat='3',mh=True)
ch('P17a','P17','Starred cancelled underlined marginal note',
 r'\margin{$^{*}$ \deleted{\uline{\unsure{aussi dire}} \uline{\unsure{strict}}}}',
 r'\ill{} \emph{\uncertain{tautologie}} \struck{\ill{}}',
 r'\margin{$^{*}$ \deleted{\uline{\unsure{aussi dire}} \uline{\unsure{strict}}}}',
 'A separate star is above the cancelled note. Two underlines survive below its crossed words. The first group permits aussi dire, including a tall d-like loop and i dot, but its earlier letters are heavily masked. The second has a short strict-like body with tall t members and an i dot; tautologie does not fit that short sequence. Both cancelled readings remain doubtful because not every letter is separable.',confidence='low',kind='misread word',cat='2',mh=True)
ch('P18a','P18','Live lower marginal instruction',
 r'\margin{modifier \unsure{sans doute} la définition des'+'\n'+r'voisinages coniques stricts \unsure{\ldots}}',
 r'\ill{} \ldots\ \uncertain{définition} \uncertain{des} voisinages coniques \uncertain{stricts} \ldots',
 r'\margin{modifier \unsure{sans doute} la définition des'+'\n'+r'voisinages côniques \unsure{strict|stricts}\ldots}',
 'Modifier has a low m/o, looped d and tall f with dotted i members and is live, below the cancellation. Sans doute remains compressed and doubtful. La définition des is readable from its looped d, tall f/t and dotted i members. Côniques has a separate accent over o. The final word ends at a tall crossed t without a clearly separate s, so strict is preferred with stricts alternative. Exactly three detached dots follow, resolving the ellipsis doubt.',True,True,'medium','readable ink left as \\ill{}','5',mh=True)
rule=span(D,r'\margin{\figure{',r'\end{tikzpicture}}}')
ch('P18b','P18','Unheaded rule beside the lower marginal instruction',
 r'\margin{modifier',r'\marginal{* \struck{\ill{}}',rule,
 'One long independent stroke runs approximately from original (306,1887) to (339,2092), leaning slightly right downward. It separates/links the lower marginal instruction and the adjacent main paragraph. It has no arrowhead and is not a cancellation of the live wording. It is reproduced as a rule, with no invented textual meaning.',True,True,kind='drawing or diagram',cat='4')
ch('P19a','P19','Thin lower-left foliation',r'\margin{15}',
 r"Le feuillet s'arrête sur « un iso\ldots »",r'\margin{15}',
 'A thin hooked 1 is followed by a 5 with a distinct upper cap and lower rounded return. The instrument and weight differ from the main hand. H omits the folio; its terminal note is editorial.',kind='omission',cat='3')

decisions=[]
def dec(id,crop,result,reading,e,confidence='high'):
 assert reading in D,(id,reading)
 decisions.append(dict(id=id,cote='150',scan='16',decision=result,reading=reading,evidence=e,
  crop=f'crops/{P}_{crop}.png',box=B[crop],confidence=confidence))
dec('M0333','P09','first',r'\uline{strict}',
 'Initial s/t pair, r, dotted i, c and terminal t are visible above one underline; no p descender or pur body.')
dec('M0334','P09','first',r"ces $T'$ correspondent donc aux fermés",
 'Ces is separate before plain T-prime. Correspondent has its p descender and tall d; the following d/o/n/c, aux and tall f with accented plural ending are readable. Initial c/o remains retraced but the phrase is recoverable.','medium')
dec('M0335','P10','first',r'T\supset Y',
 'The Y has a short curved left arm meeting the flatter right arm and descending stem, a genuine fork distinct from the preceding T roof.')
dec('M0336','P18','undecided',r'\unsure{sans doute}',
 'The s-like initial and compressed low groups followed by a d-like loop support sans doute, but the middle joining strokes do not separate every letter.','medium')
dec('M0337','P18','first',r'\ldots',
 'Exactly three detached dark dots follow the final strict/stricts group; none is connected to a word-ending stroke.')

inventory=[]
def inv(kind,pos,content,hand='his hand'):
 inventory.append(dict(scan=P,sheet_kind='text',hand=hand,element=f'E{len(inventory)+1:02d}',kind=kind,
  position=pos,first_words_or_objects=content,transcribed='yes'))
inv('margin note','upper left; P01','3)')
inv('text','opening; P02/P03','circled 3, Soit, old opening and revised cone-neighborhood premise')
inv('deletion','first original line; P02','X superset Y, X muni de sous-espaces; wording partly obscured')
inv('insertion','above old opening; P02','T un vois. [cancelled tub.] conique absolu de Y.')
inv('deletion','inside raised replacement; P02','tub.')
inv('text','small lowered group after first T-prime; P03','epsilon-like group with unresolved live/deleted state')
inv('display','conditions (12); P04','a) homothéties; b) Pour cette opération; brace ends before returned continuation line')
inv('deletion','right end of (12)a; P04','doubtful lambda T-prime subset T-prime')
inv('text','initial P of Pour; P04','overtraced P with small raised remnant; no independently recoverable earlier token')
inv('deletion','returned continuation below brace; P04','tubulaire')
inv('text','NB identities and reconstruction; P05–P08','On aura nécessairement … la donnée … Im formula')
inv('deletion','old family clause; P06','Si (T_i)_{i in I} est une famille, with final comma doubtful')
inv('insertion','above cancelled family clause; P06','la donnée de T-prime équivaut à; celle starts the next normal baseline')
inv('display','image formula; P08','T-prime = Im(double-stem I times dotted T-prime … unheaded/arrow connector T) union Y-prime')
inv('text','above interval I in image formula; P08','separate unrecoverable raised mark; placement preserved without naming an accent or cancellation')
inv('text','lowered group after dotted T-prime in image formula; P08','lambda-like group; live/deleted state unresolved')
inv('margin note','diagonal left margin; P09','On dit que T-prime est cônique strict … ces T-prime correspondent donc aux fermés …')
inv('text','middle compatibility paragraph; P10','On dira qu’une structure cônique … sous-espaces …')
inv('insertion','before T_i; P10','fermés, with curved attachment leader')
inv('text','last main paragraph; P11–P15','Soit T … compatible … strictement compatible with true star … X-star … un iso')
inv('text','initial p of partie; P11','overtraced initial, not a separable whole cancelled word')
inv('margin note','lower diagonal note 1; P16','cancelled doubtful Définir la notion pour X-prime')
inv('deletion','lower diagonal note 1; P16','entire note under repeated zigzag strikes')
inv('margin note','lower diagonal note 2; P17','starred, cancelled, separately underlined doubtful aussi dire / strict')
inv('deletion','lower diagonal note 2; P17','both underlined groups cancelled; star remains separate')
inv('margin note','lower live diagonal note; P18','modifier sans doute la définition des voisinages côniques strict/stricts …')
inv('drawing','beside lower margin note; approximately (306,1887) to (339,2092)','one long slightly leaning unheaded rule, not a strike')
inv('margin note','lower left; P19','15','thin pencil/other or undetermined hand')

audits=[]
def au(kind,xyxy,reading):
 assert reading in D or reading in DC,('audit',reading)
 audits.append(dict(box=f'B{len(audits)+1:02d}',kind=kind,xyxy=xyxy,reading=reading))
au('handwritten number',B['P01'],r'\mspage{3)}')
au('handwritten number; struck passage; insertion; C/H different words; less than high confidence departure',B['P02'],
 span(DC,r'\textcircled{3}',r'conique absolu de $Y$.}'))
au('doubtful formula; less than high confidence departure; C/H different words',B['P03'],
 span(DC,r'\unsure{Soit|Soient}',r'dans $T$ si on a'))
au('handwritten number; doubtful formula; struck passage; C/H different words; less than high confidence departure',B['P04'],
 span(DC,r'(12)\qquad',r'\deleted{tubulaire} cônique de $Y$.'))
au('doubtful formula; C/H different words; less than high confidence departure',B['P05'],
 span(DC,r'\uline{NB}',r"$T'_\lambda=T'\cap T_\lambda$ ;"))
au('struck passage; insertion; doubtful formula; C/H different words; less than high confidence departure',B['P06'],
 span(DC,r'\deleted{Si',r"\inserted{la donnée de $T'$ équivaut à}"))
au('doubtful formula; handwritten number; C/H different words; less than high confidence departure',B['P07'],
 span(DC,r"celle d'un sous-espace",r"$Y'\supset0.\dot T'$, et,"))
au('doubtful formula; C/H different words; less than high confidence departure',B['P08'],
 span(DC,'on a\n',r"\cup Y'."))
au('margin note; doubtful formula; handwritten number; C/H different words; less than high confidence departure',B['P09'],
 span(DC,r"\margin{On dit que",r"$\dot T'$ de $\dot T$.}"))
au('doubtful formula; C/H different words',[323,1060,1670,1210],
 span(DC,r"On dira qu'une structure",r'avec des sous-espaces'))
au('insertion; C/H different words',[323,1208,1670,1411],
 span(DC,r'\inserted{fermés}',r'sont côniques pour cette structure.'))
au('C/H different words; less than high confidence departure',B['P11'],
 span(DC,r'Soit $T$ un voisinage',r'fermée de $X$. On'))
au('C/H different words',B['P12'],
 span(DC,r'dit que $T$ est',r"dans $T$. On dit qu'il"))
au('C/H different words',B['P13'],
 span(DC,r'est \uline{strictement compatible}',r"strict, et s'il existe"))
au('doubtful formula; C/H different words',B['P14'],
 span(DC,r'un voisinage cylindrique',r"au $=$, s'il existe un"))
au('C/H different words',B['P15'],r'voisinage $E$ de $\dot T$ dans $X^*$, et un iso')
au('margin note; struck passage; doubtful formula; C/H different words; less than high confidence departure',B['P16'],
 r"\margin{\deleted{\unsure{Définir la notion pour $X'$}}}")
au('margin note; struck passage; C/H different words; less than high confidence departure',B['P17'],
 r'\margin{$^{*}$ \deleted{\uline{\unsure{aussi dire}} \uline{\unsure{strict}}}}')
au('margin note; C/H different words; less than high confidence departure',B['P18'],
 span(DC,r'\margin{modifier',r'\unsure{strict|stricts}\ldots}'))
au('margin note',[300,1870,348,2110],rule)
au('margin note; handwritten number',B['P19'],r'\margin{15}')

doubts=[]
def db(place,reading,alternatives,confidence,reason):
 assert reading in D,(place,reading)
 doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
db('P02 cancelled prose',r'\unsure{muni de sous-espaces}','muni de sous-espaces; some joins masked','medium','Long crossing strokes obscure several joins despite readable tall/descending members and dots.')
db('P03 opening verb',r'\unsure{Soit|Soient}','Soit | Soient','medium','The low joining stroke before final t may or may not contain compressed en.')
db('P03 lowered epsilon-like group',r"\unsure{T'_\varepsilon|T'\deleted{_\varepsilon}}",'live lowered epsilon | cancelled lowered epsilon; letter itself uncertain','medium','The retraced epsilon-like body has no secure separate strike; its presence, lowering and prime must not be omitted.')
db('P04 crossed formula',r"\deleted{\unsure{\lambda T'\subset T'}}",'lambda T-prime subset T-prime; intervening strokes obscured','low','An initial diagonal and final T-prime survive; internal relation/body cannot be read completely.')
db('P04 Pour initial',r'\unsure{Pour}','Pour; overworked initial and small raised remnant','medium','The P body is retraced and has a small raised remnant, but an earlier token or cancellation state cannot be established.')
db('P05 first dotted T-prime body',r"\unsure{\dot T'}",'dotted T-prime; underlying body unrecovered','medium','Dot, roof and prime are clear, while the central body is heavily retraced; no earlier Y/X is invented.')
db('P06 old family comma',r'famille\unsure{,}','comma | final letter/strike return','medium','The low terminal hook lies close to the old final e and crossing line.')
db('P07 first lower variable',r"\unsure{T'|Y'}",'T-prime | Y-prime','medium','A straight roof and stem favor T-prime; the body is compressed. The subsequent Y is clearly forked, so the intended classification cannot decide the literal letter.')
db('P08 raised unreadable mark',r'\overset{\unsure{}}{\mathbb{I}}','no recoverable candidate; placement only','low','Separate present ink above I is recorded by the empty doubt payload. It is not a blank, a named accent, or an asserted cancellation. It is separated from the preceding prose comma by position and blank space.')
db('P08 lowered lambda-like group',r"\unsure{\dot T'_\lambda|\dot T'\deleted{_\lambda}}",'live lowered lambda | cancelled lowered lambda; letter/height uncertain','medium','A looped/crossed descending group follows dotted T-prime. No secure independent stroke establishes deletion; both states remain.')
db('P08 action connector',r'\unsure{\mathrel{\relbar\joinrel\relbar}|\longrightarrow}','unheaded horizontal shaft | arrow','medium','The right tip rises briefly but lacks a secure two-arm head.')
db('P11 initial of partie',r'\unsure{p}artie','overworked p; no separate earlier word recovered','medium','Dark upper loops and the long p descender occupy the initial position immediately before artie.')
db('P16 cancelled note',r"\deleted{\unsure{Définir la notion pour $X'$}}",'Définir la notion pour X-prime; incompletely recoverable','low','Repeated zigzag cancellation masks several letters and small internal marks; the full wording remains only a candidate.')
db('P17 first cancelled underlined group',r'\uline{\unsure{aussi dire}}','aussi dire; letters obscured','low','Some loops and tall/dotted members survive, but the cancellation crosses most early letters.')
db('P17 second cancelled underlined group',r'\uline{\unsure{strict}}','strict; no fully recoverable alternative','low','Short word with t members and i dot; strokes obscure individual letters, so the inherited doubt stays.')
db('P18 sans doute',r'\unsure{sans doute}','sans doute; compressed middle','medium','The low joining strokes do not separate all letters despite a plausible initial s and later d-like loop.')
db('P18 final adjective',r'\unsure{strict|stricts}','strict | stricts','medium','The final tall crossed t is visible, but no distinct s can be separated before three detached dots. The plural grammar does not supply a letter.')

notes=[
 {'id':'N01','text':'This manuscript leaf has author number 3), a separate circled item 3, an opening replacement above a cancelled line, condition pair (12), a heavily revised NB, three lower marginal notes, a diagonal upper marginal definition, one unheaded marginal rule, and thin foliation 15. The full image and both supplied native halves were each inspected once, then all nineteen saved crops once. P09/P16/P17/P18 are rotated 45 degrees clockwise for readability; all boxes use original 1692×2365 coordinates. The main sequence occupies approximately twenty-five physical text/display rows, excluding raised and marginal additions. H’s page-order inference, explanatory comments, and supplied terminal ellipsis are editorial and are not source text.'},
 {'id':'N02','text':'The local mathematical content defines a conical subspace using (a) stability under interval homotheties and (b) a cone-neighborhood structure for the restricted operation. Its NB then asserts intrinsic-boundary and scaled-subspace intersection identities and describes such subspaces by a closed outer-boundary subset and a base subset containing its zero image. The upper margin calls the case with no extra base points strict. The final paragraphs define simultaneous compatibility with closed subspaces and a stronger compatibility involving an exterior cylindrical neighborhood. These descriptions are source summaries; the specific checks and failures are recorded separately below.'},
 {'id':'N03','text':'Independent radial-truncation counterexample to the two NB identities under the literal conditions (a),(b), using the interval-action mapping-cylinder definition supplied for this run. Take T=[0,1], Y={0}, with scalar action mu·t=mu t, and T-prime=[0,a] for 0<a<1. Condition (a) holds because 0≤mu t≤a for mu∈[0,1] and t∈[0,a]. The map h:[0,1]→[0,a], h(s)=as, is a homeomorphism fixing 0 and satisfies h(mu s)=mu h(s), so the restricted action on T-prime is again the absolute cone action. T-prime is also an ambient neighborhood of 0 in T because it contains [0,a), open relative to [0,1]. Thus the literal (b) is satisfied with the same Y={0}. But the intrinsic outer boundary of T-prime is {a}, whereas T-prime intersect dot T is [0,a] intersect {1}=empty. Also, for 0<lambda<1, lambda T-prime=[0,a lambda], whereas T-prime intersect T_lambda=[0,min(a,lambda)]. Taking a=lambda=1/2 gives [0,1/4] versus [0,1/2]. This refutes the implication from the printed local conditions alone to both NB identities. A stronger boundary-preserving, normalized-radius, or full-ambient-ray saturation convention could exclude this example, but such a condition is not present in (a),(b) as written. No source formula is repaired.'},
 {'id':'N04','text':'Targeted corrected-scope check of the reconstruction and strict correspondence. In a mapping cylinder C(f) of f:B→Y, write q for the quotient, with outer boundary B×{1}. For a closed subset A of B and a subspace C of Y satisfying f(A)⊂C, define S=q(A×[0,1]) union C. Then S has precisely A as its outer slice and C as its base intersection; it is invariant under the ambient scalar action. For every lambda∈[0,1], lambda S=C union q(A×[0,lambda]), and S intersect T_lambda is the same set. The source’s NB identities therefore hold for these full-ambient-ray saturated subcones. Conversely any such saturated S is uniquely determined by A=S intersect dot T and C=S intersect Y. Under the additional strict condition C=f(A), S is determined by A alone, proving the claimed closed-A/strict-subcone correspondence within this stronger class. The scalar-stable truncated example in N03 is not of this form. Closedness of A is retained as the source stipulates; it is not derived from conditions (a),(b) by this argument.'},
 {'id':'N05','text':'Independent topological check that the construction in N04 has the expected subspace topology when A is closed in B, without requiring C closed in Y. The natural continuous injection C(f restricted to A:A→C)→C(f) has image S. To prove it is an embedding, let F be closed in the smaller mapping cylinder. Its quotient preimages F_C⊂C and F_A⊂A×[0,1] are closed and compatible at zero. Extend F_C to a closed F_Y⊂Y with F_Y intersect C=F_C. Since A is closed in B, F_A is closed in B×[0,1]. The subset F_Y disjoint union (F_A union (f^{-1}(F_Y)×{0})) of Y disjoint union B×[0,1] is closed and saturated for the ambient quotient: zero-level membership agrees with F_Y, and compatibility of F_A at zero prevents an additional base identification. Its quotient image is closed in C(f), and its intersection with S is exactly F. Thus every closed set of the smaller cylinder is closed relative to S, which proves the embedding. This establishes the conditional construction used in N04, not the unrestricted classification asserted in the source NB.'},
 {'id':'N06','text':'Two separate base-variable diagnostics are preserved. First, condition (12)b ends in an unprimed Y, so read literally it makes T-prime a neighborhood of all of Y. The later classification permits a subspace Y-prime of Y containing only the zero image of the selected outer boundary. An arbitrary proper Y-prime need not contain all of Y. For example, for T=Y×[0,1] with two discrete base points and A one outer point, the strict saturated subcone A×[0,1] has only one base point and is not a neighborhood of the entire Y. Thus the classification with arbitrary Y-prime requires allowing a variable base, or retaining Y-prime=Y if (b) is literal. This is independent of the radial-truncation defect in N03. Second, the first lower variable in “et d’un sous-espace … de Y” is roofed T-prime-like, whereas the following inclusion clearly uses Y-prime. The transcript keeps T-prime|Y-prime doubt; the mathematical need for Y-prime does not decide the ink.'},
 {'id':'N07','text':'Compatibility diagnostic. With a fixed full-ray cone structure, compatibility with closed subspaces T_i or with X-prime is the requirement that the indicated intersections be conical for that same structure. The strict compatibility paragraph contains the literal words “avec T”, not “avec X-prime”; the surrounding preceding definition suggests X-prime may have been intended, but the written target is retained. Its exterior formulas are X-star=X minus ring T and X-prime-star=X-prime intersect X-star, with the hollow circle over T, three star marks and primes preserved. The asserted alternative formulation stops after “et un iso”; the map and its compatibility requirements are not written on this leaf, so no completed equivalence is claimed or proved.'},
 {'id':'N08','text':'Punctuation, decoration and revision diagnostics. All ordinary T occurrences have one roof and stem, without an independent overbar. The interval parameter in (12)a is solid heavy I; the image formula has a two-stem I and a separate raised unreadable mark, retained by an empty-content doubt at its observed height. That mark is spatially separate from the preceding comma; its rendering asserts placement only, no named accent. The epsilon- and lambda-like lowered groups have uncertain cancellation state. The apparent first compatible asterisk belongs to the hooked descender of fermée; only the later strictement compatible call has a separate star. The marginal rule is an independent unheaded stroke, not cancellation. Cônique/côniques is written with a separate accent in seven local occurrences, while other occurrences on this leaf remain unaccented. The terminal main-text iso has no supplied ellipsis; the live lower margin has exactly three points.'},
]
events=[
 {'statement_id':P+'.N03','type':'refuted, with refined id','outcome':'Constructed and checked the scalar-equivariant radial truncation T-prime=[0,a]; it refutes the literal-action version N03.L of both NB identities. The strengthened full-ray-saturated version is proved in N04 and is not refuted.'},
 {'statement_id':P+'.N04','type':'independent re-proof','outcome':'Verified reconstruction, scaled intersections and the strict correspondence for closed-boundary full-ambient-ray saturated mapping-cylinder subcones.'},
 {'statement_id':P+'.N05','type':'independent re-proof','outcome':'Proved the natural smaller mapping cylinder embeds with the ambient subspace topology when its outer slice A is closed, using a closed saturated extension argument.'},
 {'statement_id':P+'.N06','type':'targeted proof check','outcome':'Separated the literal unprimed-base requirement in (12)b from the arbitrary-base classification, using a two-point-base product example. Kept the T-prime/Y-prime paleographic doubt independent of this logical mismatch.'},
 {'statement_id':P+'.N07','type':'carried as background without fault found','outcome':'Recorded the compatibility definitions and checked the exterior formula notation; did not complete or verify an equivalence whose iso specification is cut off by the end of the leaf.'},
]
notation=[
 {'form':r'T,T\prime,T_\lambda,\dot T,\mathring T','meaning':'Cone object, its primed/scaled variants and distinguished dotted/circled parts; only actual decorations are retained.','evidence':'P02–P15: every ordinary T roof is single; dots, primes, lowered indices and the hollow circle in P14 are separate marks.'},
 {'form':r'\mathbf{I};\ \mathbb{I}','meaning':'Local solid-heavy and double-stem forms of the interval/action parameter, not regularized to the thin family-index I.','evidence':'P04 solid filled upright with broad caps; P08 two separate upright stems under shared caps; P06/P10 use thinner one-stem family indices.'},
 {'form':r'\overset{\unsure{}}{\mathbb{I}}','meaning':'Present unreadable raised ink above the interval glyph; placement only, not a named accent or a declaration of cancellation.','evidence':'P07/P08: separate mark near x950–979,y930–944, left of and below the preceding prose comma near x1028–1043,y908–925.'},
 {'form':r'\unsure{\mathrel{\relbar\joinrel\relbar}|\longrightarrow}','meaning':'Action connector in the reconstruction formula; unheaded shaft preferred, arrow alternative open.','evidence':'P08: horizontal shaft ends in a short upturn without a secure two-arm head.'},
 {'form':r"T'\cap Y=0.\dot T'",'meaning':'Written definition of a strict conical subspace in the upper margin.','evidence':'P09: first T-prime has no dot; zero has a separate following point; right boundary T-prime has a separate upper dot.'},
 {'form':r"X^*=X\setminus\mathring T,\quad X'{}^*=X'\cap X^*",'meaning':'Exterior space and the corresponding portion of X-prime in the strict compatibility paragraph.','evidence':'P14: hollow ring above T, crossed stars, primes and intersection read locally.'},
]
abbreviations=[
 {'form':'vois.','expansion':'voisinage'},
 {'form':'tub.','expansion':'tubulaire'},
 {'form':'NB','expansion':'nota bene'},
 {'form':'Im','expansion':'image'},
 {'form':'iso','expansion':'isomorphisme'},
 {'form':'= in prose','expansion':'même'},
]
hand=[
 {'habit':'A long detached T roof is the letter’s own topstroke, not an added overbar.','places':'150_scan016 P02–P15, including cancellations and raised insertions','consistency':'All ordinary T occurrences on this leaf; dots and hollow circles remain independently visible.','witness_errors':'C repeatedly adds bars; H mostly keeps plain T.'},
 {'habit':'Local cônique/côniques spelling is marked by a small separate curved stroke over o, but is not universal.','places':'150_scan016 P03, P04, P09, two P10 positions, P12, P18','consistency':'Seven accented occurrences; P02/P11/P13 have no independent accent.','witness_errors':'Both witnesses omit the visible accents; no accent is generalized to the three unaccented positions.'},
 {'habit':'An almost horizontal right Y arm can resemble a T roof; the short curved left arm decides where visible.','places':'150_scan016 P10 compared with the lower NB variable in P07','consistency':'P10 Y has a definite left fork; P07 remains T-prime/Y-prime doubtful and is not normalized from meaning.','witness_errors':'C leaves P10 Y doubtful; both witnesses give Y-prime without doubt in P07.'},
 {'habit':'Long descenders cross neighboring baselines and can resemble strikes or call marks.','places':'150_scan016 P07 and P11/P12','consistency':'The f of fermé crosses tel que; the hooked f of fermée produces the apparent first compatible star.','witness_errors':'H invents cancellations in P07; both witnesses add an independent first compatible star.'},
 {'habit':'Heavy or retraced lowered groups do not establish deletion on their own.','places':'150_scan016 P03/P08','consistency':'Both epsilon-like and lambda-like groups have uncertain state, despite dark overwork.','witness_errors':'C gives them as definitely deleted; H omits them.'},
 {'habit':'Overworked initial letters need not be independent cancelled words.','places':'150_scan016 P04 Pour and P11 partie','consistency':'The remnant at P and the retraced p cannot be separated into earlier whole tokens.','witness_errors':'H’s note treats P as a surcharged T-prime and its main transcription adds a cancelled word before partie.'},
]

coverage={
 1:'Editorial/macro-only: scanpage16 is a locator and H’s upper note is not source prose.',
 2:'P01a: written 3) with separate closing parenthesis; H’s page-order discussion is editorial.',
 3:'Source circled3 preserved; textcircled versus H’s parenthetical/cercling note is macro/editorial-only.',
 4:'P02a: muni remains a supported but partly obscured cancelled reading.',
 5:'P02a: sous-espaces remains in the doubtful cancelled phrase, with p descender and final letters visible.',
 6:'P02b: written short vois. with stop; no expansion to voisinage.',
 7:'P03a: Soit|Soient remains unresolved, Soit preferred.',
 8:'P03b: epsilon-like lowered ink present; its live/deleted state is unresolved.',
 9:'Display wrapper itself macro-only; P04c preserves the physical brace and continuation placement.',
 10:'Array syntax macro-only; P04a/P04c record the actual condition text and brace extent.',
 11:'P04a: homothéties, not les multiplications.',
 12:'P04b: crossed mathematical group retained with whole-formula doubt.',
 13:'P04c: brace joins a and the first b-line; returned continuation below brace retained. H’s explanatory note excluded.',
 14:'P04b/P04c: H’s absolu suggestion and surcharged-T-prime note do not provide literal text; local overwork remains doubtful.',
 15:'P05a: On aura, not On a.',
 16:'P05c: source semicolon after second identity.',
 17:'P06a: final comma after cancelled famille remains uncertain.',
 18:'P07a: fermé is live on the first baseline before dotted T-prime.',
 19:'P07a: dotted T-prime de dotted T is on the upper baseline; lower base variable handled separately in P07b.',
 20:'P07b: tel has no independent final s before que.',
 21:'P07c: separate comma after final et preserved.',
 22:'P08b: lambda-like lowered group present, with explicit state doubt.',
 23:'P07a/P09a–c: H’s long prose note is editorial; both main baselines and the full margin note are transcribed from ink.',
 24:'P09a/M0333: strict resolved, not pur.',
 25:'P09b/P09c: no secure comma after identity; next line begins dash and ces, not i.e.',
 26:'P09c/M0334: correspondent donc aux fermés dotted T-prime de dotted T recovered, no ouvert et fermé wording.',
 27:'P12a: apparent first star is a descender, so removed from both witnesses; superscript syntax alone not the issue.',
 28:'P13a: later star is independent and raised; macro positioning difference otherwise not a new text reading.',
 29:'Macro-only: C mathring T and H overset-circle T represent the same visible hollow ring, confirmed P14.',
 30:'P14a: literal equals-sign shorthand, not expanded même.',
 31:'P16a: separate cancelled marginal instruction retained with doubt.',
 32:'P17a/P18a: two cancelled underlined groups and later live modifier instruction kept distinct; no confident tautologie reading.',
 33:'P18a/P19a: live margin ends with three dots; thin15 preserved; H’s terminal editorial note excluded.',
}
rows=(R/'packets'/P/'differences.tsv').read_text().splitlines()[1:]
assert len(rows)==len(coverage)==33
diff_coverage=[dict(row=i,disposition=coverage[i]) for i in range(1,34)]

revisions=[
 {'text':r'\deleted{$X\supset Y$, $X$ \unsure{muni de sous-espaces}}','scope_attachment':'The whole original opening after live Soit is crossed; the raised replacement supplies the new premise.','evidence':'P02: two long crossing strokes run through the entire line; mathematical X/Y remain distinct.'},
 {'text':r'\inserted{$T$ un vois. \deleted{tub.} conique absolu de $Y$.}','scope_attachment':'Complete raised replacement above the old opening, attached after Soit.','evidence':'P02: continuous upper baseline from T through the final Y and stop.'},
 {'text':r'\deleted{tub.}','scope_attachment':'Only tub. within the raised premise is cancelled; conique follows live.','evidence':'P02: separate short cross through the abbreviated word and its stop.'},
 {'text':r"\unsure{T'_\varepsilon|T'\deleted{_\varepsilon}}",'scope_attachment':'Lowered group immediately after the first T-prime; cancellation state is open.','evidence':'P03: dark epsilon-like body without a secure independent strike.'},
 {'text':r"\deleted{\unsure{\lambda T'\subset T'}}",'scope_attachment':'Whole mathematical group at the right end of condition a.','evidence':'P04: long diagonal strike crosses the complete group; final T-prime remains visible.'},
 {'text':r'\unsure{Pour}','scope_attachment':'Overworked initial P and raised remnant belong to the beginning of the b-line; no earlier whole token is supplied.','evidence':'P04: the P loop is visible beside a small raised mark, while our is on the baseline.'},
 {'text':r'\deleted{tubulaire}','scope_attachment':'Whole old word on the returned b-continuation, before live cônique de Y.','evidence':'P04: horizontal strike crosses the word’s tall stems and low bodies; following text is outside it.'},
 {'text':r'\deleted{Si $(T_i)_{i\in I}$ est une famille\unsure{,}}','scope_attachment':'Entire old family clause is cancelled, including possible final comma.','evidence':'P06: one long line crosses the mathematical family and prose to its right; low end mark remains uncertain.'},
 {'text':r"\inserted{la donnée de $T'$ équivaut à}",'scope_attachment':'Raised line above old family clause; attachment continues with celle on the normal next baseline.','evidence':'P06/P07: à ends the raised line; celle is distinctly lower and left.'},
 {'text':r"\unsure{\dot T'_\lambda|\dot T'\deleted{_\lambda}}",'scope_attachment':'Lowered lambda-like group in the reconstruction formula; its live/deleted state is unresolved.','evidence':'P08: narrow looped group with overwork but no decisive independent strike.'},
 {'text':r'\inserted{fermés}','scope_attachment':'Raised adjective attaches before the indexed subspaces T_i.','evidence':'P10: curved leader descends to the gap immediately before T_i; it is not an underline.'},
 {'text':r'\unsure{p}artie','scope_attachment':'Overworked initial p within live partie, not a separable cancelled preceding word.','evidence':'P11: looped upper body and p descender are contiguous with artie.'},
 {'text':r"\deleted{\unsure{Définir la notion pour $X'$}}",'scope_attachment':'First lower diagonal note is cancelled as a whole.','evidence':'P16: repeated broad zigzag strokes cross all words; the final X-prime is within that scope.'},
 {'text':r'\deleted{\uline{\unsure{aussi dire}} \uline{\unsure{strict}}}','scope_attachment':'Second lower starred note has two underlined groups cancelled together; its star remains separate.','evidence':'P17: zigzag crossings above both surviving lower underlines; letters only partly recovered.'},
 {'text':r'\margin{modifier \unsure{sans doute} la définition des'+'\n'+r'voisinages côniques \unsure{strict|stricts}\ldots}',
  'scope_attachment':'Live instruction below the cancelled note, separate from both strikes; adjacent long rule is not a deletion.','evidence':'P18: uncrossed letter bodies and three terminal points; the long rule lies alongside.'},
]

report=dict(page=P,reader='reader_c',line_count=25,changes=changes,decisions=decisions,
 inventory=inventory,audit_boxes=audits,doubts=doubts,notes=notes,check_events=events,
 notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=diff_coverage,
 deletion_insertion_review=revisions)
ids=[x.split('\t')[0] for x in (R/'packets'/P/'marks.tsv').read_text().splitlines()[1:]]
assert [x['id'] for x in decisions]==ids
assert len({x['id'] for x in changes})==len(changes)
assert len(B)==19
for x in changes+decisions: assert (R/'work'/x['crop']).is_file()
for x in audits:
 x0,y0,x1,y1=x['xyxy'];assert 0<=x0<x1<=1692 and 0<=y0<y1<=2365
brace_depth=0
for token in re.findall(r'(?<!\\)[{}]',DC):
 brace_depth += 1 if token=='{' else -1
 assert brace_depth>=0
assert brace_depth==0
assert D.count(r'\begin{array}')==D.count(r'\end{array}')==1
assert D.count(r'\begin{tikzpicture}')==D.count(r'\end{tikzpicture}')==1
assert r'\bar T' not in D
assert r'\illegible' not in D
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=P,changes=len(changes),marks=len(decisions),audit_boxes=len(audits),
 crops=len(B),inventory=len(inventory),diff_rows=len(diff_coverage),doubts=len(doubts))))
