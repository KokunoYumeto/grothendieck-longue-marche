from pathlib import Path
import json, re
from datetime import datetime, timezone
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R2')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_073')
C=(packet/'C.tex').read_text(); H=(packet/'H.tex').read_text()
meta=json.loads((packet/'metadata.json').read_text())
whole,a,b=meta['images']
crops=json.loads((root/'crop_manifest.json').read_text())
by={i+1:x for i,x in enumerate(crops)}
def evidence(n=None,bbox=None,source=None):
    return {'crop':by[n]['path'] if n else None,'bbox':by[n]['bbox'] if n else bbox,'bbox_image':by[n]['source'] if n else source}
diffs=[]
def add(loc,c,h,r,ink,confidence='high',kind='other',marked='no',cc=True,ch=True,n=None,bbox=None,source=None,math=False):
    d={'id':f'D{len(diffs)+1:02d}','location':loc,'c':c,'h':h,'reading':r,'scan_shows':ink,'confidence':confidence,'kind':kind,'marked_in_h':marked,'change_c':cc,'change_h':ch,'math_consequential':math}
    d.update(evidence(n,bbox,source));diffs.append(d)
add('Opening continuation: cancelled primed capital',r"\deleted{$\unsure{G'|F'}$}",r'\struck{\ill{}}',r"\deleted{$\unsure{G'|F'}$}",'One cancelled capital with a distinct high prime; the rounded outer stroke favours G, but crossing strokes leave F possible.','medium','readable ink left as \\ill{}','yes',False,True,1,math=True)
add('Opening continuation: old capital under G',r'$\deleted{\unsure{F|E}}G$',r'$G$',r'$\deleted{F}G$','A straight old stem with top and middle bars remains inside the new rounded G; no separate old bottom bar.','high','omission','no',True,True,2,math=True)
add('Slanted upper-left note',r"\margin{\unsure{double} \unsure{Transitivité} de l'induction}",r'\marginal{\ill{} \ill{} \ill{}}',r"\margin{double \unsure{Transitivité} de l'induction}",'The entire three-line note is framed; double has two tall final stems, while the middle of Transitivité remains compressed. The low de belongs to its third line.','medium','readable ink left as \\ill{}','yes',True,True,3)
add('C7 heading: underline extent',r'$\uline{C}7_0$',r'\emph{C$7_0$}',r'$\uline{C}7_0$','The single rule ends under C, before the tall seven and its low oval zero.','high','other','no',False,True,bbox=[280,320,460,450],source=a)
add('C7 statement: verb at right',r'\unsure{induise|induit}',r'induise',r'induise','After the d/u group the ending is a low se-shaped return, without a terminal t stem.','high','misread word','no',True,False,4)
add('C7 statement: final primed capital',r"$\unsure{C'|G'}$",r"$G'$",r"$\unsure{C'|G'}$",'The final capital is open with only a short low terminal stroke; its single high prime is clear.','medium','misread symbol or index','no',False,True,4,math=True)
add('C7 statement: terminal punctuation',r"$\unsure{C'|G'}$.",r"$G'$.",r"$\unsure{C'|G'}$\unsure{,|.}",'A detached small hook sits low to the right of the prime; its curved tail favours a comma over a round point.','medium','other','no',True,True,4)
add('Parenthesis: noun after les',r'\unsure{rôle|rôles}',r'rôles',r'rôle','After the tall l there is one low returning exit, with no separately written final s.','high','misread word','no',True,True,5)
add('Parenthesis: worked mark before the first straight order',r'\deleted{\unsure{l|F}}',r'',r'R2-FIG-PARENTHESIS: q-descender junction before $\leq$','The long q descender enters a short upright, two oblique arms and a low right tick. These do not securely establish an additional cancelled l or F.','low','drawing or diagram','no',True,True,5,math=True)
add('Parenthesis: order after et',r'$\unsure{\preceq|\leqslant}$',r'$\preccurlyeq$',r'$\preceq$','The lower stroke is visibly bowed; the upper angle points left.','high','misread symbol or index','no',True,False,bbox=[1360,730,1480,815],source=a,math=True)
add('Parenthesis: mark after faux',r'\unsure{\deleted{)}|?|\}|!}',r'',r'R2-FIG-PARENTHESIS: crossed curled mark after faux','A curled lower stem, high loop, crossing short strokes and a rising diagonal precede a separate colon; a single punctuation glyph does not preserve all the ink.','low','drawing or diagram','no',True,True,6)
add('Parenthesis: adjective after F-prime order F',r'\unsure{donnés|données}',r'donnés',r'donnés','One open e with a separate high accent precedes the rounded final s; there is no second e group.','high','misread word','no',True,False,7)
add('Parenthesis: abbreviation before sous figure',r'tte',r'ttes',r'tte','Two t uprights and a low e are visible; there is no further s.','high','abbreviation expanded or spelling modernised','no',False,True,bbox=[957,925,1085,1010],source=a)
add('Parenthesis: sous figure spelling and number',r'\unsure{sous figure|sous-figure}',r'sous-figures',r'sous figure','A clear gap separates sous and figure; the right end is singular and no hyphen crosses the gap.','high','abbreviation expanded or spelling modernised','no',True,True,bbox=[1150,920,1500,1035],source=a)
add('Parenthesis: verb and participle before par',r'\unsure{soit|sont|est} induite',r'soient induites',r'\unsure{soit|sont} induite','The first word begins with s and ends with t; its compressed middle lacks a distinct i point. The participle has no final s.','medium','misread word','no',True,True,8)
add('Parenthesis: old capital under the last F',r'$\deleted{\unsure{G}}F$',r'$F$',r'$\deleted{G}F$','The curved old bowl and low inward return remain inside the later straight F.','high','omission','no',True,True,9,math=True)
add('On paragraph: corrected verb',r'\unsure{renforcera|renforce}',r'renforcer',r'renforcera','After the tall f and following c there is an extended era-shaped sequence ending in a small loop.','high','misread word','no',True,True,10)
add('On paragraph: following phrase',r'par la suite',r'\uncertain{un peu}',r'par la suite','A long p stem is followed by the raised la group and the separate s-u-i-t-e sequence.','high','misread word','yes',False,True,10)
add('On paragraph: small mark before unindexed C7, identity and state',r'\deleted{\unsure{s}}',r'\struck{\ill{}}',r'R2-MARK-BEFORE-C7','Only one short curved upright is present. No independent cancellation stroke or complete additional word is established. H’s isolated unreadable group is aligned here by physical ink.','low','drawing or diagram','yes',True,True,11)
add('On paragraph: position of H’s isolated unreadable group',r'$C7_0$ en \deleted{\unsure{s}}$C7$',r'\struck{\ill{}} C$7_0$ en C7',r'$C7_0$ en [R2-MARK-BEFORE-C7]$C7$','The small group immediately precedes the second, unindexed C7 on the next physical line, not the first C7 with low zero.','high','insertion or placement','yes',False,True,11)
# Large passages are quoted once for state only; lexical readings have their own non-identical scopes.
cstate=C[C.index(r'\deleted{\deleted{\uline'):C.index(r'\diagram{')].rstrip()+"\n"+r'\deleted{\deleted{a) $\Rightarrow$ b) résulte de C6}}'
hstate=H[H.index(r'\struck{\ill{}} Soient'):H.index('\nb) $\\Rightarrow$ a) résulte de C$7_0$.')].strip()
add('Lower draft through the separately cancelled C6 line: broad deletion state only; excludes the final C7 line',cstate,hstate,r'R2-FIG-DRAFT: text crossed by broad diagonal strokes','The long oblique strokes cross the proposed conditions, displays, conclusion and small square. Their geometry supplies the deletion state of this body; local lexical differences are separate.','high','deletion state (struck given live or live given struck)','no',False,True,bbox=[285,370,1650,1150],source=b,math=True)
add('Lower draft: exact broad cancellation drawing only',r'% Three diagonal cancellation strokes cover the draft below.',r'\note{ce dernier alinéa, depuis « Soient $F$, $G$ », est traversé de deux longs traits obliques ; en marge droite un petit schéma : $F$ et $F\prime$ reliés par un signe de subdivision barré}',r'R2-FIG-DRAFT: three continuous oblique strokes','Two long diagonals end near the C6 line and the square respectively; a third shorter diagonal crosses the far-right upper part. All three endpoints are retained. H’s cited wording is an editorial description, not additional manuscript text.','high','drawing or diagram','no',True,True,bbox=[420,370,1620,1150],source=b)
# Replace the abbreviated editorial quote with the actual full note, without treating it as manuscript words.
diffs[-1]['h']=H[H.index(r'\note{ce dernier alinéa'):H.index('\n\\drawing{')]
add('Lower heading: readable lettering under its local scribble',r'\unsure{Corollaire|Comparabilité} \unsure{1}',r'\struck{\ill{}}',r'\unsure{Corollaire|Comparabilité} \unsure{1}','An initial C and lower word strokes survive; heavy zigzags hide the middle and the final narrow numeral-like position.','low','readable ink left as \\ill{}','yes',False,True,12)
add('Lower heading: underline extent and local cancellation geometry',r'\deleted{\uline{\unsure{Corollaire|Comparabilité} \unsure{1}}}',r'\struck{\ill{}}',r'R2-FIG-DRAFT: \uline{\unsure{Corollaire|Comparabilité}} \unsure{1}, with separate zigzag cancellation','The underline stops beneath the word, before the last numeral-like position. A dense zigzag is distinct from the broad diagonal.','high','drawing or diagram','yes',True,True,12)
add('Lower Soient line: old capital under G',r'$F,\deleted{\unsure{A|F}}G$',r'$F$, $G$',r'$F,\deleted{A}G$','The earlier capital has two converging sloping legs and a crossbar: A beneath the G loop.','high','omission','no',True,True,13,math=True)
add('Lower Conditions line: raised insertion state',r'\inserted{Considérons les}',r'Considérons les',r'\inserted{Considérons les}','Both words occupy the raised line above Conditions.','high','insertion or placement','no',False,True,14)
add('Lower Conditions line: insertion enclosure',r'',r'',r'R2-FIG-DRAFT / R2-INSERTION-ENCLOSURE','A long lower arm runs beneath the complete raised phrase, curls upward at its right end and descends beside Conditions at the left.','high','drawing or diagram','no',True,True,14)
add('Lower Conditions: capital initial',r'Conditions',r'conditions',r'Conditions','The large open initial C is distinct from the small following letters.','high','abbreviation expanded or spelling modernised','no',False,True,14)
add('Lower Conditions: separately cancelled adjective',r'\deleted{\unsure{équivalentes}}',r'\struck{équivalentes}',r'\deleted{équivalentes}','The q descender, l stem, t and final s survive the single crossing rule.','high','misread word','no',True,False,14)
add('Lower a and b: placement of the two order chains',r"\[\deleted{G\leq F'\preceq F}\] ; \[\deleted{G\preceq G'\leq F.}\]",r"$G \leq F' \preccurlyeq F$ ; $G \preccurlyeq G' \leq F$.",r"\[G\leq F'\preceq F\] ; \[G\preceq G'\leq F.\] in R2-FIG-DRAFT",'Each chain stands on its own centered line below its condition, with a final point only after the second chain. The sign and letter readings otherwise agree.','high','insertion or placement','no',False,True,bbox=[650,690,1110,1010],source=b)
add('Lower conclusion: word after Mais pas',r'\unsure{vrai|vice}',r'nécess.',r'\unsure{vrai|vice}','A short low wave followed by a small upright allows vrai or vice; it does not show the longer accented nécessaires abbreviation.','low','misread word','no',False,True,15)
add('Lower conclusion: possible comma after the short word',r'\unsure{,}',r'',r'\unsure{,}','A small low hook is close to the diagonal cancellation and could belong to it; a comma remains possible.','low','omission','no',False,True,15)
add('Lower conclusion: closing parenthesis and tiny side mark',r')\unsure{.}',r')',r'R2-FIG-DRAFT / R2-CLOSING-TICK','The little dark extension is attached at midheight to the right side of the closing curve; no separate baseline full stop is visible.','high','drawing or diagram','no',True,True,15)
cdiag=C[C.index(r'\diagram{'):C.index('\n\n\\deleted{\\deleted{a)')]
hdiag=H[H.index(r'\drawing{'):H.index('\n\\note{relu')]
add('Lower-right square: complete literal geometry and uncertain top/left signs',cdiag,hdiag,r'R2-FIG-DRAFT / R2-DIAG-SQUARE','Four plain nodes F, F-prime, G, G-prime are clear. The top bowed sign has two joined rising strokes; the left sign is rounded; the bottom has three dots; the right dotted trace ends in a worked downward loop/head.','medium','drawing or diagram','no',True,True,16,math=True)
add('Final line: heavy implication',r'$\unsure{\Longrightarrow|\longrightarrow}$',r'$\Rightarrow$',r'$\Longrightarrow$','Two separated shafts at the left converge into the heavy right head.','high','misread symbol or index','no',True,False,17,math=True)
add('Final line: terminal stop',r'$C7_0$}',r'C$7_0$.',r'$C7_0$','The zero is a closed low oval, with blank space after it and no further point.','high','text not on the page','no',False,True,17)
add('Final b-to-a line: extent of broad cancellation',r'\deleted{b) $\unsure{\Longrightarrow|\longrightarrow}$ a) résulte de $C7_0$}',r'b) $\Rightarrow$ a) résulte de C$7_0$.',r'\unsure{b) $\Longrightarrow$ a) résulte de $C7_0$} in R2-FIG-DRAFT','This line lies below every oblique endpoint and has no local strike. Its possible inclusion in the cancelled draft is left open; the figure does not extend a stroke across it.','medium','deletion state (struck given live or live given struck)','no',True,True,17,math=True)

# One disposition for every unsure macro in C.tex, followed by explicit notation checks.
doubts=[]
def doubt(loc,c,r,status,ink,n=None,bbox=None,source=None):
 d={'id':f'C{len(doubts)+1:02d}','location':loc,'c':c,'reading':r,'status':status,'scan_shows':ink};d.update(evidence(n,bbox,source));doubts.append(d)
doubt('Opening cancelled capital',r"\unsure{G'|F'}",r"\unsure{G'|F'}",'retained','Prime clear; outer bowl survives, inner letter is crossed.',1)
doubt('Opening older capital inside G',r'\unsure{F|E}',r'F','resolved','Top and middle bars without a distinct bottom bar.',2)
doubt('Slanted note, first word',r'\unsure{double}',r'double','resolved','Looped initial d and two tall final stems survive the reduced middle.',3)
doubt('Slanted note, second word',r'\unsure{Transitivité}',r'\unsure{Transitivité}','retained','T, medial tall stems and final accent are present; the tiny middle remains compressed.',3)
doubt('C7 statement verb',r'\unsure{induise|induit}',r'induise','resolved','Low se ending, with no terminal t upright.',4)
doubt('C7 final letter',r"\unsure{C'|G'}",r"\unsure{C'|G'}",'retained','Open bowl and short exit; no secure inner G return.',4)
doubt('Parenthesis role ending',r'\unsure{rôle|rôles}',r'rôle','resolved','One low ending after the tall l, no separately visible s.',5)
doubt('Parenthesis before first order',r'\deleted{\unsure{l|F}}',r'R2-FIG-PARENTHESIS: q-descender junction','revised','Extra short upright and cross arms touch the q tail; additional letter and cancellation state are both uncertain.',5)
doubt('Parenthesis bowed order after et',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','A bowed lower line is distinct from the preceding straight order.',bbox=[1360,730,1480,815],source=a)
doubt('Parenthesis after faux',r'\unsure{\deleted{)}|?|\}|!}',r'R2-FIG-PARENTHESIS: crossed curled mark','revised','Several crossing strokes and a lower curl do not reduce securely to one punctuation glyph.',6)
doubt('Parenthesis adjective',r'\unsure{donnés|données}',r'donnés','resolved','Single e group before final s.',7)
doubt('Parenthesis sous figure',r'\unsure{sous figure|sous-figure}',r'sous figure','resolved','The intervening space has no hyphen.',bbox=[1150,920,1500,1035],source=a)
doubt('Parenthesis soit',r'\unsure{soit|sont|est}',r'\unsure{soit|sont}','revised','Initial s and final t clear; inner arch versus i remains unresolved.',8)
doubt('Parenthesis overwritten final letter',r'\deleted{\unsure{G}}',r'\deleted{G}','resolved','Old rounded bowl and inner return remain beneath F.',9)
doubt('On paragraph verb',r'\unsure{renforcera|renforce}',r'renforcera','resolved','Extended era ending follows the c.',10)
doubt('On paragraph small mark',r'\deleted{\unsure{s}}',r'R2-MARK-BEFORE-C7','revised','One short curved stroke; its letter identity and deleted state are not secure.',11)
doubt('Crossed heading word',r'\unsure{Corollaire|Comparabilité}',r'\unsure{Corollaire|Comparabilité}','retained','Dense cancellation hides the medial letters.',12)
doubt('Crossed heading numeral',r'\unsure{1}',r'\unsure{1}','retained','A narrow final upright lies beneath the last zigzag; its complete shape is hidden.',12)
doubt('Lower older capital inside G',r'\unsure{A|F}',r'A','resolved','Two sloping legs and an A crossbar are visible.',13)
doubt('Lower struck adjective',r'\unsure{équivalentes}',r'équivalentes','resolved','q descender, l, t and final s remain legible around the strike.',14)
doubt('Lower conclusion short word',r'\unsure{vrai|vice}',r'\unsure{vrai|vice}','retained','Short low wave and a separated upright do not settle the middle.',15)
doubt('Lower conclusion comma',r'\unsure{,}',r'\unsure{,}','retained','Low hook is crowded by the long diagonal.',15)
doubt('Lower conclusion final point',r'\unsure{.}',r'R2-CLOSING-TICK','revised','The tiny stroke is attached at the middle of the closing parenthesis, not at the baseline.',15)
doubt('Square top relation',r'\unsure{\preceq\mkern-5mu{}^{\prime}|\preceq|\leqslant}',r'R2-DIAG-SQUARE: doubt-marked literal forked sign','revised','Two joined rising curves stand above the heavily retraced bowed comparison; neither is a securely detached prime.',16)
doubt('Square left sign',r'\unsure{\cup|U|\vee}',r'\unsure{\cup|U}','revised','The bottom is rounded, excluding a pointed wedge.',16)
doubt('Last implication',r'\unsure{\Longrightarrow|\longrightarrow}',r'\Longrightarrow','resolved','Two left shafts are separated before the filled head.',17)
doubt('C_context notation check: all local F/G/C alphabets and high primes',r"F, G, \unsure{C'|G'}",r"F, G, \unsure{C'|G'}",'retained','Fs are plain with separate bars. Earlier Gs have inward exits; only the last C7 capital retains its local C/G ambiguity. High single primes remain at each written occurrence.',bbox=[280,50,1670,640],source=a)
doubt('C_context notation check: C7 heading and later references',r'C7_0',r'C7_0','resolved','The heading and two later C7 references have a low closed oval; the middle en C7 has no low index. Heading underline is under C alone.',bbox=[280,325,1660,1245],source=a)
doubt('C_context notation check: bowed versus flat orders in the two cancelled displays',r'\leq, \unsure{\preceq|\leqslant}',r'\leq, \preceq','resolved','Both displays pair straight lower bars with distinctly bowed comparison signs; middle primed nodes are F-prime and G-prime respectively.',bbox=[675,700,1110,1010],source=b)
doubt('C_context notation check: conclusion and C6-line implications',r'\Rightarrow',r'\Rightarrow','resolved','Both conclusion arrows and the separately cancelled C6-line arrow have two shafts and right heads.',bbox=[350,950,1650,1140],source=b)
doubt('C_context notation check: square dotted edges and endpoints',r'\cdots; \text{dotted downward pointer}',r'R2-DIAG-SQUARE: three bottom dots and dotted right trace with worked downward head','revised','Three horizontal points are distinct. The right endpoint is a looped down-facing head, preserved literally; no idealized empty corner or extra target was supplied.',16)

contexts=[
 {'context_row':1,'scope':'Upper continuation, C7 and crossed-heading alphabets','disposition':['C01','C02','C06','C19','C27']},
 {'context_row':2,'scope':'C7 heading and later references','disposition':['C28']},
 {'context_row':3,'scope':'Flat and bowed comparison signs','disposition':['C09','C29']},
 {'context_row':4,'scope':'Final arrows and complete square','disposition':['C24','C25','C26','C30','C31']},
 {'context_row':5,'scope':'Opening cancelled primed capital and overwritten G','disposition':['C01','C02']},
 {'context_row':6,'scope':'Inclined note','disposition':['C03','C04']},
 {'context_row':7,'scope':'C7 ending verb and final capital','disposition':['C05','C06']},
 {'context_row':8,'scope':'Role ending and mark adjoining q descender','disposition':['C07','C08']},
 {'context_row':9,'scope':'Faux mark, adjective and sous figure spelling','disposition':['C10','C11','C12']},
 {'context_row':10,'scope':'Old G inside final F','disposition':['C14']},
 {'context_row':11,'scope':'Renforcera and mark before C7','disposition':['C15','C16']},
 {'context_row':12,'scope':'Crossed title and numeral','disposition':['C17','C18']},
 {'context_row':13,'scope':'Old A inside G and struck adjective','disposition':['C19','C20']},
 {'context_row':14,'scope':'Conclusion word/punctuation and square signs','disposition':['C21','C22','C23','C24','C25']},
 {'context_row':15,'scope':'Last heavy arrow','disposition':['C26']},
 {'context_row':16,'scope':'Soit/sont/est','disposition':['C13']},
 {'context_row':17,'scope':'Repeated role ending check','disposition':['C07']},
 {'context_row':18,'scope':'Repeated C7 final capital check','disposition':['C06']}
]

inventory=[]
def inv(el,kind,pos,words):
 inventory.append({'element':el,'kind':kind,'position':pos,'first_words_or_objects':words,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('I01','text','Top centre, (820,30)–(910,80)','72')
inv('I02','text','Top continuation, two lines, (290,80)–(1630,255)','sous-figure de … induite par la sous-figure …')
inv('I03','deletion','Opening continuation below folio, (820,80)–(890,130)',r"\unsure{G'|F'}")
inv('I04','deletion','Second opening line, (1305,175)–(1360,225)',r'F overwritten by G')
inv('I05','margin note','Three slanted lines in upper-left, (25,40)–(305,445)',r"double \unsure{Transitivité} de l'induction")
inv('I06','text','Heading at (290,338)–(445,439)',r'$\uline{C}7_0$')
inv('I07','text','Three-line C7 statement, (295,333)–(1655,635)','Pour toute figure F, sous-figure G …')
inv('I08','text','Parenthetical paragraph, (280,650)–(1650,1140)',r"(mais l'énoncé symétrique …)")
inv('I09','drawing','Junction at bottom of symétrique q, (1150,744)–(1184,795)','R2-FIG-PARENTHESIS: worked q-descender junction')
inv('I10','drawing','After faux, (635,855)–(675,932)','R2-FIG-PARENTHESIS: crossed curled mark')
inv('I11','deletion','Final capital of parenthesis, (1548,1053)–(1600,1120)','G overwritten by F')
inv('I12','text','On paragraph, (310,1155)–(1655,1440)','On … renforcera par la suite C7_0 en … C7 …')
inv('I13','deletion','After On, (592,1180)–(720,1230)','peut')
inv('I14','drawing','Before unindexed C7, (445,1285)–(465,1310)','R2-MARK-BEFORE-C7')
inv('I15','text','Lower heading, (310,1515)–(715,1605)',r'\unsure{Corollaire|Comparabilité} \unsure{1}; word underlined')
inv('I16','deletion','Dense local zigzag across lower heading, (350,1510)–(715,1605)','Local title cancellation in R2-FIG-DRAFT')
inv('I17','text','Lower opening line, (840,1490)–(1650,1590)','Soient F, G deux figures.')
inv('I18','deletion','Older capital in lower G, (1190,1510)–(1252,1572)','A overwritten by G')
inv('I19','insertion','Raised line above Conditions, (300,1595)–(645,1650)','Considérons les')
inv('I20','drawing','Beneath full raised phrase and beside Conditions, (300,1598)–(696,1706)','R2-INSERTION-ENCLOSURE')
inv('I21','text','Conditions line, (325,1640)–(1025,1710)','Conditions … :')
inv('I22','deletion','Adjective and its crossing rule, (675,1640)–(1012,1735)','équivalentes')
inv('I23','text','Condition a, (405,1695)–(1650,1790)',r"a) G est une sous-figure d'une subd. de F :")
inv('I24','display','Separate first chain, (720,1810)–(1040,1880)',r"G\leq F'\preceq F")
inv('I25','text','Condition b on two physical lines, (345,1895)–(1610,2050)',r"b) G est une subdivision d'une sous-figure de F :")
inv('I26','display','Separate second chain, (690,2038)–(1090,2105)',r"G\preceq G'\leq F.")
inv('I27','text','Draft conclusion, (370,2050)–(1637,2170)',r'On a alors b) \Rightarrow a) (Mais pas … a \Rightarrow b !!!)')
inv('I28','drawing','Closing-parenthesis side tick, (1626,2086)–(1636,2093)','R2-CLOSING-TICK')
inv('I29','diagram','Lower right, (1310,2120)–(1510,2260)',r'R2-DIAG-SQUARE: F, F\prime, G, G\prime; top worked sign, left cup, dots and down head')
inv('I30','text','Penultimate line, (368,2165)–(1085,2245)',r'a) \Rightarrow b) résulte de C6')
inv('I31','deletion','Continuous local strike through C6 line, (370,2187)–(1083,2226)','Local C6-line cancellation')
inv('I32','deletion','Three oblique strokes across draft, endpoints (793,2212), (1423,2233), (1598,1849)','Broad draft cancellation; exact geometry in R2-FIG-DRAFT')
inv('I33','text','Last line below all diagonal ends, (370,2240)–(1095,2310)',r'b) \Longrightarrow a) résulte de C7_0; cancellation extent uncertain')

remaining=[
 {'location':'Opening cancelled primed capital','reading':r"\unsure{G'|F'}",'alternatives':["G'","F'"],'confidence':'medium','reason':'Crossing strokes obscure the inner letter; the high prime is distinct.'},
 {'location':'Slanted note second word','reading':r'\unsure{Transitivité}','alternatives':['Transitivité'],'confidence':'medium','reason':'The middle is reduced to tiny strokes; the T and final accented ending survive.'},
 {'location':'C7 last capital','reading':r"\unsure{C'|G'}",'alternatives':["C'","G'"],'confidence':'medium','reason':'Open bowl with a short exit; no decisive internal G return.'},
 {'location':'C7 terminal punctuation','reading':r'\unsure{,|.}','alternatives':[',','.'],'confidence':'medium','reason':'A detached low hook has a small curved tail.'},
 {'location':'Parenthesis before first straight order','reading':'R2-FIG-PARENTHESIS: doubt-marked q-descender junction','alternatives':[r'\deleted{l}',r'\deleted{F}','retraced q-descender, with no additional complete letter'],'confidence':'low','reason':'Extra strokes directly meet q; the added-letter and cancellation interpretations are not separable.'},
 {'location':'Parenthesis after faux','reading':'R2-FIG-PARENTHESIS: doubt-marked crossed curl','alternatives':[r'\deleted{)}','worked ?','worked }','worked !'],'confidence':'low','reason':'High loop, crossing arms and lower curl survive; a single normalized glyph loses strokes.'},
 {'location':'Parenthesis verb before induite','reading':r'\unsure{soit|sont}','alternatives':['soit','sont'],'confidence':'medium','reason':'s and t are clear, compressed inner arch and missing i point are not.'},
 {'location':'Small mark before unindexed C7','reading':'R2-MARK-BEFORE-C7: doubt-marked short curve','alternatives':['s','abandoned initial stroke','unidentified short pen stroke'],'confidence':'low','reason':'There is one group, with no independent crossing to establish deletion.'},
 {'location':'Lower title word','reading':r'\unsure{Corollaire|Comparabilité}','alternatives':['Corollaire','Comparabilité'],'confidence':'low','reason':'Dense zigzag obscures the medial lettering.'},
 {'location':'Lower title final numeral','reading':r'\unsure{1}','alternatives':['1'],'confidence':'low','reason':'A narrow upright is hidden by the terminal scribble; no second secure candidate is claimed.'},
 {'location':'Lower conclusion after Mais pas','reading':r'\unsure{vrai|vice}','alternatives':['vrai','vice'],'confidence':'low','reason':'Low waves and a short upright permit both readings.'},
 {'location':'Lower conclusion following hook','reading':r'\unsure{,}','alternatives':[',','part of diagonal cancellation'],'confidence':'low','reason':'The little hook meets the long oblique stroke.'},
 {'location':'Square top sign','reading':'R2-DIAG-SQUARE: doubt-marked literal forked comparison','alternatives':[r'worked \preceq',r'\preceq with a prime-like attached stroke',r'worked \leqslant'],'confidence':'low','reason':'Two joined rising curves and the heavy middle cannot be separated into a secure ordinary sign plus prime.'},
 {'location':'Square left sign','reading':r'\unsure{\cup|U}','alternatives':[r'\cup','U'],'confidence':'medium','reason':'Rounded bottom excludes wedge, while cup versus a letter is not settled by shape.'},
 {'location':'Last b-to-a line, state only','reading':r'\unsure{b) $\Longrightarrow$ a) résulte de $C7_0$}','alternatives':['uncrossed final assertion','part of the broadly cancelled draft despite lying below the drawn endpoints'],'confidence':'medium','reason':'All three broad strokes stop above this line; no extra strike is supplied.'}
]

notes={
 'summary':'Continuation defining an induced subfigure, C7_0, a statement that the symmetric assertion is false, and a planned strengthening. The lower proposed comparison of two conditions is worked and broadly cancelled. Every text group and graphical mark was read from this page; the supplied witnesses remained drafts.',
 'math_reading_decisions':'No mathematical argument was used to choose letters or signs. The different lower strokes of the straight and bowed orders prompted local visual comparison only. The final open C/G was not normalized to the preceding G-prime. Double shafts, rather than the expected logical implication, settled the last arrow. The author’s assertions were transcribed, not validated.',
 'author_checks':'The parenthesis says the symmetric assertion is false, without an example on this page. The lower a-to-b claim attributed to C6 has its own crossing rule. The last b-to-a attribution to C7_0 is physically below the broad diagonal endpoints; whether the author included it in the overall cancellation remains open.',
 'title_dates_pagination':'Manuscript folio 72 is clear at the top; scan marker 73 retained. The only proposed lower heading is locally scribbled out and remains doubtful. No date, title sheet or overall page count appears.',
 'h_placeholder_alignment':'The opening struck placeholder maps to the cancelled primed capital; the three marginal placeholders map jointly to the three-line note; the isolated struck placeholder in the On paragraph maps to the small mark before the second C7 (H placed it before the first C7_0); the lower opening placeholder maps to the crossed title. No placeholder was silently discarded.',
 'h_editorial_notes':'H’s statements that the draft has two diagonal strokes and that the inserted wording is underlined are editorial descriptions, not manuscript words. The image shows three diagonals and a hooked insertion enclosure beneath the full Considérons les phrase. H’s later correction that the top square sign is worked rather than separately struck is consistent with preserving its worked strokes and the independent broad diagonal.',
 'scope_of_graphic_states':'Deletion and insertion state in the composite lower group is carried by the literal drawing. No extra horizontal strike was added across an entire line merely to replace a long diagonal. Ordinary overwritten capitals still use the prescribed old-before-new convention. The final line’s unsure wrapper concerns only block-cancellation scope.',
 'source_scope':'Only this assigned page packet, the supplied conventions and notation snapshot, and this reader’s own output were used. The unrelated cross-page tail initially present in C_context was disregarded. No other scans, reader files, OCR, research, delegation or LaTeX compilation were used.',
 'missing_crop_continuations':'None of the seventeen targeted loci is clipped. Some adjacent non-target text reaches crop edges, but no target absence is inferred from those edges.'
}
notation=[
 {'sign':'individual figure F','latex':'F','appearance':'Plain stem with separate top and middle bars, including the diagram nodes.','location':'Opening, C7, parenthesis, two lower chains and square','alternatives':[]},
 {'sign':'G and the locally open final capital','latex':r"G; \unsure{C'|G'}",'appearance':'Earlier Gs have a low inward return; C7’s last letter is more open.','location':'C7 last primed capital versus its earlier local G occurrences','alternatives':["C'","G'"]},
 {'sign':'numbered condition','latex':r'C7_0','appearance':'Tall seven with a small closed low oval; only C is underlined at the heading.','location':'Heading, On paragraph first reference, last line','alternatives':[]},
 {'sign':'straight and bowed order signs','latex':r'\leq, \preceq','appearance':'Straight lower bar versus bowed lower line beneath left-pointing angles.','location':'Parenthetical pair and the two cancelled chains','alternatives':[]},
 {'sign':'double right implication','latex':r'\Rightarrow; \Longrightarrow','appearance':'Two shafts, with a filled heavy head in the last occurrence.','location':'Lower conclusion and final two lines','alternatives':[]},
 {'sign':'square top worked sign','latex':'R2-DIAG-SQUARE: literal doubt-marked TikZ','appearance':'Bowed lower strokes with a heavy middle and two joined rising branches.','location':'Between F and F-prime in the small square','alternatives':[r'worked \preceq','attached prime-like stroke',r'worked \leqslant']},
 {'sign':'square left rounded sign','latex':r'\unsure{\cup|U}','appearance':'Two short uprights joined by a rounded bottom.','location':'Between F and G in the small square','alternatives':[r'\cup','U']},
 {'sign':'right dotted trace and endpoint','latex':'R2-DIAG-SQUARE: literal dotted trace and worked downward head','appearance':'Separated dark marks above a looped down-facing endpoint.','location':'Under F-prime and above G-prime','alternatives':[]},
 {'sign':'local overwritten capitals','latex':r'\deleted{F}G; \deleted{G}F; \deleted{A}G','appearance':'Old straight bars, old curved bowl, and old triangular A remain beneath replacements.','location':'Opening line 2; parenthesis end; lower Soient line','alternatives':[]},
 {'sign':'high primes','latex':r"F', G'",'appearance':'Single detached high ticks.','location':'All written prime-bearing figure labels','alternatives':[]}
]

# Log every successful image display in exact order. No tool result was truncated.
visible=[
 'Layout: top continuation and slanted note; C7 heading and three-line assertion; parenthesis; On paragraph; cancelled lower draft with raised insertion, two displays, small square and final lines.',
 'Read all upper lines against both witnesses; isolated unresolved lettering, punctuation and correction states; C-only heading underline, singular tte/sous figure, and bowed order visible.',
 'Read all lower lines against both witnesses; three broad diagonals, two order chains, raised insertion enclosure, small square, independent C6 strike and final line beneath the diagonal endpoints visible.'
]
crop_evidence=[
 'Cancelled capital has rounded outer stroke and distinct prime; G/F remains uncertain.',
 'F top and middle bars remain under G; no old bottom bar.',
 'Complete rotated note: double; compressed Transitivité; de l’induction, including the low de.',
 'Induise ending, locally open C/G prime, and low hooked terminal punctuation.',
 'Role ends without a separate s; q descender directly enters the worked pre-order junction.',
 'Crossed curl has high loop, oblique arms and lower turn; colon is separate.',
 'Donnés has one e group and a separate high accent.',
 'Initial s and final t of soit/sont visible; induite has no plural s.',
 'Old G bowl and return survive beneath F; closing parenthesis and period clear.',
 'Renforcera ending and full par la suite group; peut is separately crossed.',
 'Single short curved mark precedes the second C7; no separate cancellation stroke.',
 'Initial C and lower strokes survive title zigzags; word and numeral remain doubtful; underline stops before numeral.',
 'Old triangular A and its bar beneath G.',
 'Full Considérons les insertion, hooked enclosing arm, capital Conditions and struck équivalentes.',
 'Vrai/vice and nearby possible comma remain open; tiny final extension attaches to closing parenthesis.',
 'All four square nodes, joined forked top sign, rounded left sign, three bottom dots and dotted downward worked endpoint.',
 'Two shafts of last arrow clear; final low oval zero and blank following space; all diagonal ends are above the final line.'
]
log=[]
for i,p in enumerate(meta['images']):
 log.append({'view':i+1,'path':p,'kind':'whole' if i==0 else 'supplied half','transforms':'none','success':True,'evidence':visible[i]})
for i,crop in enumerate(crops):
 log.append({'view':i+4,'path':crop['path'],'kind':'own tight crop','source':crop['source'],'bbox':crop['bbox'],'scale':crop['scale'],'rotation':crop['rotation'],'transforms':crop['transforms'],'success':True,'evidence':crop_evidence[i]})
(root/'inspection_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
lines=['# R2 inspection log — scan 156-4_073','', 'The whole image and each supplied half were viewed once. Each own crop was viewed alone once. No image display was truncated. No OCR or LaTeX compiler was used.','']
for e in log:
 lines += [f"{e['view']:02d}. {e['path']}",f"    {e['transforms']}",f"    {e['evidence']}"]
 if 'bbox' in e: lines += [f"    Original bbox {e['bbox']} on {e['source']}; scale {e['scale']:.8f}; rotation {e['rotation']} degrees."]
 lines += ['']
(root/'inspection_log.md').write_text('\n'.join(lines))
report={
 'reader':'R2','cote':'156-4','scan':73,'brief_version':'v09','started_utc':'2026-11-20T12:58:40Z','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'image_views':meta['images'],'reading_file':str(root/'reading.tex'),
 'differences':diffs,'c_doubts':doubts,'context_dispositions':contexts,'inventory':inventory,'remaining_doubts':remaining,'notation':notation,'abbreviations':[{'form':'tte','expansion':'toute'},{'form':'ss-figure','expansion':'sous-figure'},{'form':'subd.','expansion':'subdivision'}],'notes':notes,'check_events':[], 'crops':crops,'inspection_log':str(root/'inspection_log.json'),'missing_crop_continuations':[],
 'workflow_feedback':['The packet context initially included unrelated cross-page material; it was disregarded, as instructed. Restricting the distributed context to the assigned page avoids this contamination risk.','The exact stroke endpoint can establish that a final line is physically uncrossed while leaving the intended scope of a broad block cancellation unresolved. A literal composite drawing and explicit state doubt are needed here.']}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(diffs),'c_doubts':len(doubts),'context_dispositions':len(contexts),'remaining_doubts':len(remaining),'inventory':len(inventory),'crops':len(crops),'image_displays':len(log)},indent=2))
