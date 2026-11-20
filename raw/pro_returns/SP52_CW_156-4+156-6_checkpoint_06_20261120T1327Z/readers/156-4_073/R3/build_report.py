from pathlib import Path
from datetime import datetime, timezone
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R3')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_073')
meta=json.loads((packet/'metadata.json').read_text())
whole,half_a,half_b=meta['images']
crops=json.loads((root/'crop_manifest.json').read_text())
C=(packet/'C.tex').read_text(); H=(packet/'H.tex').read_text()
differences=[]; doubts=[]; source_checks=[]

def evidence(crop=None,bbox=None,source=None):
    if crop is not None:
        v=crops[crop-1]
        return {'crop':v['path'],'bbox':v['bbox'],'bbox_image':v['source'],'source':v['source']}
    return {'crop':None,'bbox':bbox,'bbox_image':source or whole,'source':source or whole}

def diff(id,location,c,h,reading,scan,kind,cc,ch,crop=None,bbox=None,source=None,conf='high',marked='no',math=False):
    row={'id':id,'location':location,'c':c,'h':h,'reading':reading,'scan_shows':scan,'confidence':conf,'kind':kind,'marked_in_h':marked,'change_c':cc,'change_h':ch,'math_consequential':math,**evidence(crop,bbox,source)}
    differences.append(row)
    for label,s,txt in [('c',c,C),('h',h,H)]:
        if s and not s.startswith(('C diagram excerpt:','H editorial','H drawing excerpt:','C layout:','H layout:','C figure reference:','H figure reference:')):
            source_checks.append({'id':id,'witness':label,'literal_snippet_present':s in txt})

def cd(id,location,c,reading,status,scan,crop=None,bbox=None,source=None):
    doubts.append({'id':id,'location':location,'c':c,'reading':reading,'status':status,'scan_shows':scan,**evidence(crop,bbox,source)})

# All changes of lettering, certainty, state, punctuation and placement are scoped separately.
diff('D01','Continuation: cancelled primed letter',r"\deleted{$\unsure{G'|F'}$}",r'\struck{\ill{}}',r"\deleted{$\unsure{G'|F'}$}",'A detached high prime survives beside crossed upper curves and bars; G/F remains open.','readable ink left as \\ill{}',False,True,2,conf='low',marked='yes',math=True)
diff('D02','Continuation: G written over F',r'$\deleted{\unsure{F|E}}G$',r'$G$',r'$\deleted{F}G$','Two older horizontal arms and a straight stem are visible within the newer G bowl; no separate older bottom arm.','omission',True,True,3,math=True)
diff('D03','Entire oblique upper-left margin',r"\margin{\unsure{double} \unsure{Transitivité} de l'induction}",r'\marginal{\ill{} \ill{} \ill{}}',r"\margin{double Transitivité de l'induction}",'The three slanted lines read double / Transitivité / de l’induction; the low de belongs to the last line.','readable ink left as \\ill{}',True,True,1,marked='yes')
diff('D04','C7 heading: underline extent',r'$\uline{C}7_0$',r'\emph{C$7_0$}',r'$\uline{C}7_0$','The short underline stops under C; 7 and its lower oval are not underlined.','other',False,True,bbox=[280,325,454,448],source=half_a)
diff('D05','C7: final verb',r'\unsure{induise|induit}',r'induise',r'induise','The ending is a separate rounded s-like sweep followed by a low e, without a terminal t shaft.','misread word',True,False,4)
diff('D06','C7: final primed capital',r"$\unsure{C'|G'}$",r"qui induise $G'$.",r"qui induise $\unsure{C'|G'}$",'The final capital is open with a short low exit; C is the first reading, but its short exit does not exclude G.','misread symbol or index',False,True,4,conf='medium',math=True)
diff('D07','C7: terminal punctuation',r"$\unsure{C'|G'}$.",r"$G'$.",r"$\unsure{C'|G'}$,",'The small detached terminal mark has a hooked, descending comma shape, comparable to the comma after the G above.','other',True,True,4)
diff('D08','Parenthesis: rôle ending',r'\unsure{rôle|rôles}',r'rôles',r'\unsure{rôle|rôles}','After the tall l, the low final exit lacks a separately clear s; rôle remains first, with rôles possible.','misread word',False,True,5,conf='medium')
diff('D09','Parenthesis: worked group immediately before ≤',r'\deleted{\unsure{l|F}}',r'',r'Figure fig:order-overlap in reading.tex','The descending q above meets a short upright, crossing diagonal and low hook; a separate complete older l/F is not established.','drawing or diagram',True,True,5,conf='low')
diff('D10','Parenthesis: second order sign after et',r'$\unsure{\preceq|\leqslant}$',r'$\preccurlyeq$',r'$\preceq$','The lower stroke and the right end of the middle stroke are bowed, unlike the straight ≤ beside it.','misread symbol or index',True,False,5,math=True)
diff('D11','Parenthesis: worked mark after faux',r'\unsure{\deleted{)}|?|\}|!}',r'est faux :',r'est faux [Figure fig:faux-mark] :','A curled vertical group has several crossings and a descending tail; the following two-point colon is distinct. A literal drawing preserves more than a guessed punctuation glyph.','drawing or diagram',True,True,6,conf='low')
diff('D12','Parenthesis: donnés/données',r'\unsure{donnés|données}',r'donnés',r'\unsure{donnés|données}','A small high accent-like point stands over the last e-shaped curve; the compressed medial strokes leave the e count uncertain.','misread word',False,True,7,conf='medium')
diff('D13','Parenthesis: tte sous figure',r'tte \unsure{sous figure|sous-figure}',r'ttes sous-figures',r'tte sous figure','The abbreviation ends with one low e; the noun has no separate final s; the gap before figure contains no detached hyphen.','misread word',True,True,8)
diff('D14','Parenthesis: soit … induite',r'\unsure{soit|sont|est} induite',r'soient induites',r'\unsure{soit|sont|est} induite','The first group has a curved initial and terminal t with an undotted compressed middle. Induite ends after the low e, without a separate plural s.','misread word',False,True,9,conf='medium')
diff('D15','Parenthesis: final F over G',r'$\deleted{\unsure{G}}F$',r'une ss-figure $G$ de $F$)',r'une ss-figure $G$ de $\deleted{G}F$)','The older curved bowl and rightward hooked bar remain under the later F stem and arms.','omission',True,True,10,math=True)
diff('D16','Strengthening paragraph: verb',r'\unsure{renforcera|renforce}',r'renforcer',r'\unsure{renforcera|renforce}','After the tall f, the low continuation ends in a small closed loop; renforcera is favoured, but the reduced ending remains uncertain.','misread word',False,True,11,conf='medium')
diff('D17','Strengthening paragraph: par la suite',r'par la suite',r'\uncertain{un peu}',r'par la suite','The first group has a p descender, the next a looped l, and the last ends with a tall t and low e; the phrase has no local cancellation.','misread word',False,True,11,marked='yes')
diff('D18','Strengthening paragraph: small mark and H unreadable placement',r'$C7_0$ en \deleted{\unsure{s}}$C7$',r'\struck{\ill{}} C$7_0$ en C7',r'$C7_0$ en [Figure fig:before-C7]$C7$','A single low curved stroke is before the second C7. It has no secure crossing stroke. H’s additional unreadable group is provisionally aligned here, displaced in H to before C7₀; no separate struck word is visible after suite.','insertion or placement',True,True,12,conf='medium',marked='yes')
diff('D19','Cancelled draft: title and possible numeral',r'\deleted{\uline{\unsure{Corollaire|Comparabilité} \unsure{1}}}',r'\struck{\ill{}}',r'Figure fig:cancelled-draft, title: \unsure{Corollaire|Comparabilité} \unsure{1}','The initial C and scattered medial loops survive under one continuous zigzag; the last tall group may be 1. No confident full title is recovered.','readable ink left as \\ill{}',False,True,13,conf='low',marked='yes')
diff('D20','Cancelled draft: title cancellation and underline geometry',r'\deleted{\uline{\unsure{Corollaire|Comparabilité} \unsure{1}}}',r'\struck{\ill{}}',r'Figure fig:cancelled-draft, title zigzag and shorter underline','The local cancellation is a zigzag, with a separate near-horizontal underline that stops before the rightmost title group.','drawing or diagram',True,True,13,marked='yes')
diff('D21','Cancelled draft: G over A after F comma',r'$F,\deleted{\unsure{A|F}}G$',r'$F$, $G$',r'$F,\deleted{A}G$','A triangular pair of strokes and middle crossbar are legible inside the newer G.','omission',True,True,14,math=True)
diff('D22','Cancelled draft: inserted phrase and paragraph placement',r"\deleted{\inserted{Considérons les} Conditions \deleted{\unsure{équivalentes}} :}",r'Considérons les conditions \struck{équivalentes} :',r'Figure fig:cancelled-draft, raised \inserted{Considérons les} before Conditions','Considérons les occupies the raised line between the title underline and Conditions, not the baseline after figures. C has a paragraph boundary here and H does not; the figure retains the physical separation without inventing an additional paragraph signal.','insertion or placement',False,True,13)
diff('D23','Cancelled draft: insertion enclosure/connector',r'\inserted{Considérons les}',r'H editorial note excerpt: le mot souligné ajouté dessous est « considérons »',r'Figure fig:insertion-enclosure in reading.tex','A long low line rises and hooks at the right of les, then curves down at the left toward Conditions; it is more than an underline under one word.','drawing or diagram',True,True,13)
diff('D24','Cancelled draft: Conditions capital',r'Conditions',r'conditions',r'Conditions','The large open initial has capital height.','misread word',False,True,13)
diff('D25','Cancelled draft: cancelled équivalentes',r'\deleted{\unsure{équivalentes}}',r'\struck{équivalentes}',r'\deleted{équivalentes}','The q descender, tall l/t strokes and final s-like curve remain readable through the local rule; the crop clips the low end of q, already visible in the prescribed lower half.','misread word',True,False,13)
diff('D26','Lower draft: broad cancellation geometry and extent',r'% Three diagonal cancellation strokes cover the draft below.',r'H editorial note excerpt: est traversé de deux longs traits obliques',r'Figure fig:cancelled-draft, three broad drawn strokes','There are three diagonals: two long strokes and a shorter right stroke. They cross the title/body/diagram region and end above the final implication baseline. Per-word synthetic strikes do not reproduce this geometry.','drawing or diagram',True,True,bbox=[300,1480,1645,2310],source=whole)
diff('D27','Lower draft: first displayed chain placement',r'\[\n\deleted{G\leq F\'\preceq F}\n\]',r"$G \leq F' \preccurlyeq F$",r"\[G\leq F'\preceq F\]",'The first chain occupies a separate centered line below condition a). Its broad cancellation state is recorded by D26, not counted again here.','insertion or placement',False,True,bbox=[690,1790,1060,1885],source=whole)
diff('D28','Lower draft: second displayed chain placement',r'\[\n\deleted{G\preceq G\'\leq F.}\n\]',r"$G \preccurlyeq G' \leq F$.",r"\[G\preceq G'\leq F.\]",'The second chain is a separate line with a detached terminal point after F. Broad cancellation is scoped to D26.','insertion or placement',False,True,bbox=[675,2025,1095,2105],source=whole)
diff('D29','Draft conclusion: word after Mais pas',r'\unsure{vrai|vice}',r'nécess.',r'\unsure{vrai|vice}','A short waved group and a narrow upright survive; there are no securely readable letters supporting nécess. The crossing diagonal obscures the end.','misread word',False,True,15,conf='low')
diff('D30','Draft conclusion: possible comma after disputed word',r'\unsure{,}',r'(Mais pas nécess. a',r'(Mais pas \unsure{vrai|vice}\unsure{,} a','A small short protrusion meets the broad diagonal after the word; it may be a comma, but is not securely separate. This row concerns only that mark.','other',False,True,15,conf='low')
diff('D31','Draft conclusion: closing curve and adjoining mark',r')\unsure{.}',r'b !!!)',r'b !!![Figure fig:draft-close-mark]','A tiny right-facing tick meets the closing parenthesis at mid-height, rather than standing as a clear baseline full stop.','drawing or diagram',True,True,15,conf='medium')
diff('D32','Small square: worked top relation',r'\deleted{\unsure{\preceq\mkern-5mu{}^{\prime}|\preceq|\leqslant}}',r'H drawing excerpt: un signe de subdivision surchargé et barré',r'Figure fig:small-square, five-stroke top relation','Beside the bowed lower strokes, two high returning arms share the worked center. A separate prime is not established. The crossing diagonal belongs to the broad cancellation.','drawing or diagram',True,True,16,conf='medium',math=True)
diff('D33','Small square: rounded left sign',r'\deleted{\unsure{\cup|U|\vee}}',r'H drawing excerpt: un signe d\'inclusion vertical ($\cup$)',r'\unsure{\cup|U}','The bottom is smoothly rounded, excluding a pointed ∨; cup versus letter U remains a semantic ambiguity of the same local form.','misread symbol or index',True,True,16,conf='medium',math=True)
diff('D34','Small square: right endpoint, lower G and literal geometry',r'C diagram excerpt: \deleted{F\'} \arrow[d,dotted,->]',r'H drawing excerpt: un trait vertical en pointillés, puis $G\'$',r'Figure fig:small-square, irregular dotted pointer and retraced G','The right side has irregular separated short marks ending in a dark loop/triangle; the lower-left G has an additional upper arc. The three bottom dots and all four node/prime positions are retained.','drawing or diagram',True,True,16)
diff('D35','Final implication: double arrow',r'\unsure{\Longrightarrow|\longrightarrow}',r'$\Rightarrow$',r'$\Longrightarrow$','Two distinct bars reach a heavy rightward head; the doubled shaft is visible before the filled end.','misread symbol or index',True,False,17,math=True)
diff('D36','Final implication: terminal punctuation',r'$C7_0$}',r'C$7_0$.',r'$C7_0$','The low oval zero is followed by clear paper without a full stop.','text not on the page',False,True,17)
diff('D37','Final implication: cancellation state',r'\deleted{b) $\unsure{\Longrightarrow|\longrightarrow}$ a) résulte de $C7_0$}',r'b) $\Rightarrow$ a) résulte de C$7_0$.',r'\unsure{b) $\Longrightarrow$ a) résulte de $C7_0$}','All three broad strokes end above this line. The line itself has no crossing stroke; whether it is included in the abandonment of the adjoining draft remains uncertain.','deletion state (struck given live or live given struck)',True,True,17,conf='medium')

# One disposition per explicit C unsure, including those retained.
cd('C01','Continuation: cancelled primed letter',r"\unsure{G'|F'}",r"\unsure{G'|F'}",'retained','Detached prime and crossed curves/bars do not decide the capital.',2)
cd('C02','Continuation: older letter under G',r'\unsure{F|E}',r'F','resolved','Two old arms and a straight stem identify F.',3)
cd('C03','Margin: double',r'\unsure{double}',r'double','resolved','Rotated crop shows d loop, compressed ou, tall b/l and final e.',1)
cd('C04','Margin: Transitivité',r'\unsure{Transitivité}',r'Transitivité','resolved','Large T, reduced medial strokes, tall late t and detached acute are visible.',1)
cd('C05','C7 final verb',r'\unsure{induise|induit}',r'induise','resolved','Rounded s sweep plus final e; no terminal t shaft.',4)
cd('C06','C7 final capital',r"\unsure{C'|G'}",r"\unsure{C'|G'}",'retained','Open C-shaped bowl and short low exit; G remains possible.',4)
cd('C07','Parenthesis: rôle ending',r'\unsure{rôle|rôles}',r'\unsure{rôle|rôles}','retained','No separate secure s after the low exit.',5)
cd('C08','Parenthesis: group before ≤',r'\deleted{\unsure{l|F}}',r'Figure fig:order-overlap','revised','The short worked group intersects the q descender, without a securely complete separate letter.',5)
cd('C09','Parenthesis: bowed order',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','Both lower right ends visibly curve.',5)
cd('C10','Parenthesis: post-faux mark',r'\unsure{\deleted{)}|?|\}|!}',r'Figure fig:faux-mark','revised','Curled stem, several crossing arms and connected descending tail retained literally.',6)
cd('C11','Parenthesis: donnés',r'\unsure{donnés|données}',r'\unsure{donnés|données}','retained','Compressed medial strokes leave the number of e forms open.',7)
cd('C12','Parenthesis: sous figure hyphen',r'\unsure{sous figure|sous-figure}',r'sous figure','resolved','Clear gap lacks a separate hyphen.',8)
cd('C13','Parenthesis: soit',r'\unsure{soit|sont|est}',r'\unsure{soit|sont|est}','retained','Curved initial, undotted compressed middle and terminal t.',9)
cd('C14','Parenthesis: older G under final F',r'\deleted{\unsure{G}}',r'\deleted{G}','resolved','Old bowl and hooked low arm show G.',10)
cd('C15','Strengthening: verb',r'\unsure{renforcera|renforce}',r'\unsure{renforcera|renforce}','retained','Ending has a small loop but the reduced internal strokes remain ambiguous.',11)
cd('C16','Strengthening: small s-like mark before C7',r'\deleted{\unsure{s}}',r'Figure fig:before-C7','revised','One low curved stroke with no secure cancellation line.',12)
cd('C17','Cancelled draft: title word',r'\unsure{Corollaire|Comparabilité}',r'\unsure{Corollaire|Comparabilité}','retained','One continuous zigzag obscures most of the word.',13)
cd('C18','Cancelled draft: possible title numeral',r'\unsure{1}',r'\unsure{1}','retained','The last tall group is not separately decipherable beyond a possible 1.',13)
cd('C19','Cancelled draft: older A under G',r'\unsure{A|F}',r'A','resolved','Two sloping legs and middle crossbar are present.',14)
cd('C20','Cancelled draft: équivalentes',r'\unsure{équivalentes}',r'équivalentes','resolved','q, tall l/t and terminal curve are readable through the local rule; lower q endpoint comes from the lower-half view.',13)
cd('C21','Draft conclusion: vrai/vice',r'\unsure{vrai|vice}',r'\unsure{vrai|vice}','retained','A waved beginning and narrow upright survive, with the last stroke crossed.',15)
cd('C22','Draft conclusion: comma',r'\unsure{,}',r'\unsure{,}','retained','Small protrusion at the crossing can be a comma or part of another stroke.',15)
cd('C23','Draft conclusion: final dot',r'\unsure{.}',r'Figure fig:draft-close-mark','revised','Tiny tick is attached at the middle of the closing curve, not clearly a separate period.',15)
cd('C24','Small square: worked comparison',r'\unsure{\preceq\mkern-5mu{}^{\prime}|\preceq|\leqslant}',r'Figure fig:small-square, top relation','revised','Two high arms share the worked center with bowed lower strokes; their function is not decided.',16)
cd('C25','Small square: left relation',r'\unsure{\cup|U|\vee}',r'\unsure{\cup|U}','revised','Smoothly rounded bottom excludes ∨.',16)
cd('C26','Final heavy implication',r'\unsure{\Longrightarrow|\longrightarrow}',r'\Longrightarrow','resolved','Two separate shaft bars remain visible left of the filled head.',17)

# Explicit local notation/context checks not limited to unsure macros.
context=[]
def ctx(id,location,disposition,refs,crop=None,bbox=None,source=None):
    context.append({'id':id,'location':location,'disposition':disposition,'c_doubt_refs':refs,**evidence(crop,bbox,source)})
ctx('CTX01','Upper continuation, C7 and lower heading: local F/G/C alphabets','Plain F stems/arms and bowl-shaped G forms are individually retained; the sole uncertain live capital is the final C7 C′/G′. Older F and A are resolved locally.',['C01','C02','C06','C19'],bbox=[285,65,1655,620],source=half_a)
ctx('CTX02','C7 heading and its two C7₀ references; C7 without zero','The heading has underline under C alone. Heading, strengthening reference, and final reference each have a small low oval zero. The second reference in en C7 lacks a zero.',[],bbox=[280,325,454,448],source=half_a)
ctx('CTX03','Parenthesis and both lower display chains: order signs','The straight ≤ and bowed ≼ are distinct. Both displays retain their middle prime, and the second display retains its terminal point.',['C09'],bbox=[675,1790,1095,2105],source=whole)
ctx('CTX04','Conclusion/final implications and small square','The first two implications have double shafts; the last heavy implication also has two visible bars. The square keeps its extra high arms, rounded left sign, lower dots and irregular downward endpoint.',['C24','C25','C26'],16)
ctx('CTX05','Upper continuation corrections','First cancelled primed capital remains G′/F′; the next G is over a readable F.',['C01','C02'],2)
ctx('CTX06','Inclined upper-left note','Read from own rotated crop as double Transitivité de l’induction, with the low de included.',['C03','C04'],1)
ctx('CTX07','C7 right end: verb and capital','induise resolves; the C′/G′ capital remains local and uncertain.',['C05','C06'],4)
ctx('CTX08','Parenthesis after les and before ≤','rôle/rôles remains uncertain. The mark before ≤ is drawn with its connection to the q descender rather than asserted as an independent cancelled l/F.',['C07','C08'],5)
ctx('CTX09','Post-faux mark, donnés and sous figure','Post-faux shape is literal; donnés/données remains; sous figure has no certain lexical hyphen and is read without it.',['C10','C11','C12'],6)
ctx('CTX10','Parenthesis: last F','The older G under F resolves.',['C14'],10)
ctx('CTX11','Strengthening paragraph and pre-C7 mark','Verb alternatives remain; par la suite is clear. The small pre-C7 curve is preserved without a confidently asserted deletion.',['C15','C16'],11)
ctx('CTX12','Lower title','Word and last possible numeral remain uncertain under the one continuous scribble.',['C17','C18'],13)
ctx('CTX13','Lower older capital and cancelled adjective','Older A and équivalentes resolve. The clipped q endpoint is explicitly documented.',['C19','C20'],14)
ctx('CTX14','Draft conclusion and square','vrai/vice and possible comma remain; the final parenthesis tick and worked comparison are drawn literally. Cup/U remains, ∨ is excluded.',['C21','C22','C23','C24','C25'],15)
ctx('CTX15','Final heavy arrow','Double right arrow resolves from two bars.',['C26'],17)
ctx('CTX16','Parenthesis: soit','soit/sont/est retained; no grammatical argument used to select an unmarked form.',['C13'],9)
ctx('CTX17','Repeated context: les rôle(s)','Same exact occurrence as C07/CTX08; no independent plural stroke is secured.',['C07'],5)
ctx('CTX18','Repeated context: C7 last character','Same exact occurrence as C06/CTX07; the final open capital is not normalized from the earlier G′.',['C06'],4)

inventory=[]
def inv(element,kind,position,first):
    inventory.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':first,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('I01','text','Top center, above continuation','72')
inv('I02','text','Top two lines','sous-figure de … la subdivision')
inv('I03','deletion','First continuation line after de','Cancelled G′/F′')
inv('I04','deletion','Second continuation line under G','F overwritten by G')
inv('I05','margin note','Upper-left margin, oblique','double Transitivité de l’induction')
inv('I06','text','Upper body, three lines','C7₀ Pour toute figure F')
inv('I07','text','Middle, five-line parenthesis','(mais l’énoncé symétrique')
inv('I08','drawing','Parenthesis, before ≤ and at q descender','fig:order-overlap')
inv('I09','drawing','Parenthesis after faux','fig:faux-mark')
inv('I10','deletion','Parenthesis final letter','G overwritten by F')
inv('I11','text','Middle-lower three lines','On … renforcera par la suite')
inv('I12','deletion','After On','peut')
inv('I13','drawing','Immediately before second C7','fig:before-C7')
inv('I14','text','Lower draft, upper-left title','Corollaire/Comparabilité 1?; short underline')
inv('I15','deletion','Over lower title','Continuous zigzag in fig:cancelled-draft')
inv('I16','text','To right of lower title','Soient F, G deux figures.')
inv('I17','deletion','Under G after F comma','A overwritten by G')
inv('I18','insertion','Raised line above Conditions','Considérons les')
inv('I19','drawing','Below raised phrase, turning at both ends','fig:insertion-enclosure')
inv('I20','text','Lower draft before a)','Conditions équivalentes :')
inv('I21','deletion','Local rule through adjective','équivalentes')
inv('I22','text','Lower draft condition a)','a) G est une sous-figure d’une subd. de F :')
inv('I23','display','Below condition a)','G ≤ F′ ≼ F')
inv('I24','text','Lower draft condition b), source wraps after sous-','b) G est une subdivision d’une sous-figure de F :')
inv('I25','display','Below condition b)','G ≼ G′ ≤ F.')
inv('I26','text','Sloping conclusion above last two lines','On a alors b) ⇒ a) (Mais pas …)')
inv('I27','drawing','Right end of draft conclusion','fig:draft-close-mark')
inv('I28','diagram','Lower right','fig:small-square: F, F′, G, G′')
inv('I29','text','Next-to-last line','a) ⇒ b) résulte de C6')
inv('I30','deletion','Through next-to-last line','Separate long horizontal/sloping local rule')
inv('I31','text','Bottom line below diagonal endpoints','b) ⇒ a) résulte de C7₀; overall deletion state uncertain')
inv('I32','deletion','Lower draft across body and square','Three broad diagonals, two long and one shorter')

remaining=[]
def rem(location,reading,alts,reason,conf='low'):
    remaining.append({'location':location,'reading':reading,'alternatives':alts,'confidence':conf,'reason':reason})
rem('Opening cancelled capital',r"\deleted{$\unsure{G'|F'}$}",[r"G'",r"F'"],'Crossed curves and bars do not isolate the capital; prime is secure.')
rem('C7 final capital',r"\unsure{C'|G'}",[r"C'",r"G'"],'Open bowl has only a short exit; earlier G′ is not used to force identity.','medium')
rem('Parenthesis rôle ending',r'\unsure{rôle|rôles}',['rôle','rôles'],'Reduced final exit does not securely reveal an extra s.','medium')
rem('Before ≤',r'Figure fig:order-overlap',['cancelled l-like letter','cancelled F-like letter','worked continuation/retrace of q descender'],'Overlapping arms do not establish a separate complete older glyph.')
rem('After faux',r'Figure fig:faux-mark',['crossed closing parenthesis','worked question-like sign','worked brace-like sign'],'Curled sign has connected tail and several crossing arms; literal drawing retains them.')
rem('Parenthesis donnés',r'\unsure{donnés|données}',['donnés','données'],'Compressed medial letters leave the e count unresolved.','medium')
rem('Parenthesis verb',r'\unsure{soit|sont|est}',['soit','sont','est'],'No clear i dot; only curved beginning and terminal t are secure.','medium')
rem('Strengthening verb',r'\unsure{renforcera|renforce}',['renforcera','renforce'],'The final small loop favours renforcera but the reduced ending remains ambiguous.','medium')
rem('Before second C7',r'Figure fig:before-C7',['abandoned initial stroke','small s-like mark, live','small s-like mark, cancelled by replacement'],'No separate crossing stroke establishes cancellation.')
rem('Cancelled title word',r'\unsure{Corollaire|Comparabilité}',['Corollaire','Comparabilité'],'Continuous zigzag hides most middle letters.')
rem('Cancelled title final group',r'\unsure{1}',['1','last strokes of the title word'],'The last tall group is not securely separable.')
rem('Draft conclusion after Mais pas',r'\unsure{vrai|vice}',['vrai','vice'],'A waved group and thin upright are cut at the right by the diagonal.')
rem('Draft conclusion comma',r'\unsure{,}',['comma','no independent punctuation stroke'],'The candidate meets the cancellation diagonal.')
rem('Draft conclusion close',r'Figure fig:draft-close-mark',['closing parenthesis with attached stroke','closing parenthesis and crowded point'],'Small mark is at mid-height and attached to the curve.','medium')
rem('Small square top relation',r'Figure fig:small-square, top relation',[r'worked \preceq',r'\preceq with a prime-like arm','overprinted/partly retraced order sign'],'Two high arms share one center; drawing avoids assigning one detached prime.','medium')
rem('Small square left sign',r'\unsure{\cup|U}',[r'\cup','U'],'Its rounded form settles shape but not whether to treat it as a symbol or letter.','medium')
rem('Final implication cancellation extent',r'\unsure{b) $\Longrightarrow$ a) résulte de $C7_0$}',['live last line below the cancellation strokes','included in the cancelled draft despite no crossing stroke'],'Actual broad strokes end above the baseline; the doubt concerns state only.','medium')

notation=[
 {'sign':'Plain F and G','latex':r'F, G','appearance':'F has upright plus two arms; G has open bowl and low return. Three local overwritten letters are recorded separately.','location':'Continuation, C7, parenthesis, lower draft and square','alternatives':[]},
 {'sign':'Open final primed capital','latex':r"\unsure{C'|G'}",'appearance':'Narrow open curve with short low exit and one high prime.','location':'C7 last character','alternatives':[r"C'",r"G'"]},
 {'sign':'C7 zero','latex':r'C7_0','appearance':'Small low oval to right of seven; only C underlined in heading.','location':'Heading, strengthening first reference, final implication','alternatives':[]},
 {'sign':'Two orders','latex':r'\leq,\preceq','appearance':'Straight angle/bar versus bowed middle/lower ends.','location':'Parenthesis and two displayed chains','alternatives':[]},
 {'sign':'Worked relation','latex':'Figure fig:small-square, top relation','appearance':'Bowed lower strokes plus two tall returning arms at one dark center; long diagonal crosses as part of block deletion.','location':'Small square top edge','alternatives':[r'\preceq',r'\preceq with extra prime-like/retraced strokes']},
 {'sign':'Rounded left relation','latex':r'\unsure{\cup|U}','appearance':'Narrow upright sides with rounded bottom, not pointed.','location':'Small square left edge','alternatives':[r'\cup','U']},
 {'sign':'Heavy final implication','latex':r'\Longrightarrow','appearance':'Two distinct bars ending in filled rightward head.','location':'Final line','alternatives':[]},
 {'sign':'Literal worked marks','latex':'Figures fig:order-overlap, fig:faux-mark, fig:before-C7, fig:draft-close-mark','appearance':'Connected, crossed, or attached strokes whose function is not securely one ordinary punctuation/letter glyph.','location':'As named','alternatives':['See remaining_doubts at the precise loci']}
]

view_evidence=[
'Whole page viewed once for blocks, folio, margin, deletions and complete lower drawing layout.',
'Upper half viewed once, reading every upper line and all inline formulas, ending at the beginning of the strengthening paragraph.',
'Lower half viewed once, reading the overlap, complete strengthening paragraph, cancelled draft, displays, final lines and square.',
'The rotated margin shows all three slanted lines, including the low de; double and Transitivité resolve.',
'Crossed capital retains G′/F′ alternatives; prime and folio 72 are secure.',
'Older F stem/two arms under new G resolve; final period and preceding comma also visible.',
'induise resolves; final C′/G′ remains; terminal mark is hooked comma.',
'rôle(s) remains; bowed order resolves; q descender intersects worked short group.',
'Curled crossed post-faux sign and separate colon drawn literally.',
'donnés/données remains; compressed e count cannot be settled.',
'tte and figure are singular; no separate hyphen in sous figure.',
'soit/sont/est retained; induite has no final plural s.',
'Older G under final F resolves; closing parenthesis and period secure.',
'renforcera/renforce retained; par la suite read live; C7₀ zero clear.',
'Small curved mark before second C7 has no secure cancellation stroke.',
'Title word/numeral remain; insertion/enclosure and équivalentes read; crop clips q descender endpoint as documented.',
'Older A under G resolves from triangular legs and crossbar.',
'vrai/vice and comma remain; closing curve has a small mid-height attached tick.',
'Complete square: two extra high relation arms, rounded U/cup, irregular dotted downward endpoint, three bottom dots, retraced lower G.',
'Final arrow has two bars; no terminal period; broad diagonal endpoints lie above last line.'
]
framing=[{'crop':crops[12]['path'],'source':whole,'missing_continuation_bbox':[710,1710,742,1736],'coordinates_status':'approximate region, original-image pixels','description':'Lower continuation of q descender in équivalentes extends below the crop boundary y=1710. It was visible in the prescribed lower-half view; no recrop was made. The title, insertion connector, adjective baseline, and other target strokes are framed.','half_source':half_b,'missing_continuation_half_bbox':[710,612,742,638]}]

report={
'reader':'R3','cote':'156-4','scan':'73','brief_version':'v09','started_utc':'2026-11-20T12:58:49Z','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
'image_views':meta['images'],'reading_file':str(root/'reading.tex'),'differences':differences,'c_doubts':doubts,'context_dispositions':context,'inventory':inventory,'remaining_doubts':remaining,'notation':notation,
'abbreviations':[{'form':'tte','expansion':'toute'},{'form':'ss-figure','expansion':'sous-figure'},{'form':'subd.','expansion':'subdivision'}],
'notes':{
 'summary':'Independent ink reading of scan 073 only. The opening correction is F under G, the lower correction A under G, induise and singular tte sous figure are clear. Worked punctuation and the square are preserved as literal drawings. The lower draft contains three broad cancellation strokes; its final implication lies below their endpoints.',
 'math_reading_decisions':'No mathematical proof or computation was performed. Following the stated figure/subdivision roles prompted comparison of the final open C′/G′ with earlier G′, and inspection of the two order shapes and implication shafts. Shape alone decides each retained reading; the final capital is not normalized. The two display chains and their primes are copied as written.',
 'author_checks':'The author’s page states the failure of the symmetric assertion and, in the draft, b) ⇒ a) with references C6 and C7₀. These are transcribed claims, not validations. A separate rule cancels the C6 line. The last C7₀ line has uncertain relation to the block cancellation because no broad stroke crosses it.',
 'title_dates_pagination':'Running handwritten folio 72. No date or separate title sheet. Lower draft title remains Corollaire/Comparabilité with possible 1. No additional cote marker was introduced.',
 'witness_placeholder_dispositions':'H’s first struck unreadable maps to the cancelled primed capital. Its three marginal unreadables map to the three slanted lines. Its lower struck unreadable maps to the title/possible numeral. Its extra unreadable in the strengthening paragraph is provisionally aligned to the small stroke before the second C7, displaced by H before the first C7₀; no additional word-sized erased group is asserted.',
 'h_editorial_dispositions':'H’s oblique-margin note correctly identifies location. Its two-long-stroke comment omits a third, shorter diagonal. Its later correction that the top relation is crossed by a broad cancellation rather than a separate strike agrees with the visible long line. The raised words are Considérons les together; their drawn enclosure/connector is retained rather than reduced to an underline under Considérons.',
 'scope_and_workflow':'Only the assigned packet, conventions, notation snapshot and own outputs were used. The trailing cross-page audit originally present in C_context was disregarded after the parent’s instruction. No other reader/page, outside source, delegation, OCR or LaTeX compiler was used. The start timestamp is the first recorded inspection clock.'
},
'check_events':[],
'crops':[{k:v for k,v in item.items() if k not in ('width','height')} for item in crops],
'crop_framing':framing,
'workflow_feedback':['The one-crop rule makes endpoint framing particularly important: the heading crop clipped the q descender tail by a few pixels. Its missing original/half coordinates are documented and no recrop was used.','A continuous cancelled draft with an embedded diagram is better represented by one named TikZ figure; this avoids repeating long graphics in difference rows.'],
'figure_references':['fig:order-overlap','fig:faux-mark','fig:before-C7','fig:cancelled-draft','fig:insertion-enclosure','fig:draft-close-mark','fig:small-square'],
'literal_witness_snippet_checks':source_checks
}
# Final scope/literal corrections are checked against the actual packet.
byid={row['id']:row for row in differences}
byid['D06']['h']=r"$G'$"
byid['D06']['reading']=r"$\unsure{C'|G'}$"
byid['D15']['c']=r'une ss-figure $G$ de $\deleted{\unsure{G}}F$)'
byid['D27']['c']="\\[\n\\deleted{G\\leq F'\\preceq F}\n\\]"
byid['D28']['c']="\\[\n\\deleted{G\\preceq G'\\leq F.}\n\\]"
byid['D30']['h']=''
byid['D30']['reading']=r'\unsure{,}'
byid['D31']['c']=r'!!!)\unsure{.}'
byid['D31']['h']='!!!)'
byid['D31']['reading']='!!![Figure fig:draft-close-mark]'
byid['D33']['h']="H drawing excerpt: un signe d'inclusion vertical ($\\cup$)"
byid['D34']['c']="C diagram excerpt: \\deleted{F'} \\arrow[d,dotted,->]"
byid['D34']['h']="H drawing excerpt: un trait vertical en pointillés, puis $G'$"
for row in differences:
    if row['kind'].startswith('readable ink left as'):
        row['kind']=r'readable ink left as \ill{}'
source_checks=[]
for row in differences:
    for label,txt in [('c',C),('h',H)]:
        snippet=row[label]
        if snippet and not snippet.startswith(('C diagram excerpt:','H editorial','H drawing excerpt:','C layout:','H layout:','C figure reference:','H figure reference:')):
            source_checks.append({'id':row['id'],'witness':label,'literal_snippet_present':snippet in txt})
report['literal_witness_snippet_checks']=source_checks
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# R3 inspection log — scan 156-4_073','', 'All images were emitted alone. No truncation was reported; each successful image display below was inspected once. No half was revisited.','']
for i,path in enumerate(meta['images']):
    lines += [f'{i+1}. `{path}`',f'   - Transformation: none; supplied image.',f'   - Evidence: {view_evidence[i]}']
for i,item in enumerate(crops):
    lines += [f'{i+4}. `{item["path"]}`',f'   - Source: `{item["source"]}`',f'   - Original bbox: {item["bbox"]}; rotation {item["rotation"]} degrees; scale {item["scale"]:.8f}; output {item["width"]} × {item["height"]}.', '   - Transformations: PIL crop; BICUBIC rotation with white fill when nonzero; LANCZOS resize; autocontrast; UnsharpMask radius 1.2, percent 110, threshold 3; JPEG quality 94.',f'   - Evidence: {view_evidence[i+3]}']
lines += ['', '## Framing exception', '', f'- Crop 13 misses the lower continuation of the q descender in équivalentes, original-image region {framing[0]["missing_continuation_bbox"]}; lower-half region {framing[0]["missing_continuation_half_bbox"]}. The endpoint was seen in prescribed half b. No second crop/view of that locus was made.', '', '## Non-image work', '', '- Read assignment, complete brief v09, metadata, C, H, conventions, preamble, notation snapshot, and page-local C context.', '- Created own crops with make_crops.py. No OCR or image recognition API was used.', '- Created reading.tex and report.json with literal mark drawings and all local C/H/context dispositions.', '- Structural checks only; no LaTeX compilation or mathematical validation.']
(root/'inspection_log.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'differences':len(differences),'c_doubts':len(doubts),'context_dispositions':len(context),'inventory':len(inventory),'remaining_doubts':len(remaining),'crops':len(crops),'failed_literal_snippet_checks':[x for x in source_checks if not x['literal_snippet_present']]},ensure_ascii=False,indent=2))
