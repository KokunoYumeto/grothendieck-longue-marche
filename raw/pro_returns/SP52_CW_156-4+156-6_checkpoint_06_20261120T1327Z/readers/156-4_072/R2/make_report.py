from pathlib import Path
import json, re
from datetime import datetime, timezone

OUT=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R2')
PKT=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_072')
META=json.loads((PKT/'metadata.json').read_text())
WHOLE,A,B=META['images']
C=(PKT/'C.tex').read_text(); H=(PKT/'H.tex').read_text()
R=(OUT/'reading.tex').read_text()
CROPS=json.loads((OUT/'crops_metadata.json').read_text())
CP={int(Path(x['path']).name[:2]):x for x in CROPS}

def blocks(s, macro):
    ans=[]; needle='\\'+macro+'{'; p=0
    while True:
        p=s.find(needle,p)
        if p<0:return ans
        st=p; j=p+len(needle); depth=1
        while depth and j<len(s):
            if s[j]=='\\' and j+1<len(s) and s[j+1] in '{}': j+=2; continue
            if s[j]=='{': depth+=1
            elif s[j]=='}': depth-=1
            j+=1
        ans.append(s[st:j]); p=st+len(needle)

CU=blocks(C,'unsure'); CM=blocks(C,'margin'); HN=blocks(H,'note'); HM=blocks(H,'marginal')
CD=blocks(C,'diagram')
RD=re.findall(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',R,re.S)
assert len(CU)==30 and len(CD)==2 and len(RD)==2

CAP=r'\unsure{\rlap{$\deleted{\mathcal F}$}\mathcal C|\mathscr C|\mathbb C}'
MAP=r'\unsure{\mathrel{\mapstochar\relbar}|\mapsto|\mathrel{\vdash\joinrel\dashv}}'
SUP=r"Je ne sais s'il faut prendre des sup quelconques (\unsure{condition} stricte) \deleted{\unsure{et}} ou bien de sup finis seulement \unsure{(condition lge|(condition large|(condition lge)|(condition large)}"
CN=r"\unsure{reporter|rajouter} \textcircled{c} Pour $F'\preceq F$ subd. fixé, l'application $G\mathrel{\vdash\joinrel\dashv}G'$ \unsure{\rlap{\deleted{F}}sous-fig.|Sous-fig.} de $F$ $\mathrel{\relbar\joinrel\relbar}$ sous-fig. de $F'$ commute aux Sup (pour $\leq$) i.e."
BN=r"et \textcircled{b} les \unsure{strates|str.tes} de $G'$ sont les \unsure{\deleted{s}|s}tr\unsure{a|.}tes $X'$ de $F'$ \unsure{tel|\deleted{tel}}les que $X'\ll\unsure{G_m|G_n|G}$."
BC=r'Ce \unsure{complément|complement} \unsure{servira} plus bas'
BOTTOM=r'\margin{sur la sous-figure $\unsure{G|\mathcal G}$ de $F$}'

diff=[]
def d(n,loc,c,h,reading,ink,kind='other',cc=False,ch=True,cp=None,bbox=None,src=None,conf='high',marked='no',math=False):
    z=CP[cp] if cp else None
    diff.append(dict(id=f'D{n:02}',location=loc,c=c,h=h,reading=reading,scan_shows=ink,confidence=conf,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=z['path'] if z else None,bbox=bbox or (z['bbox'] if z else None),bbox_image=src or (z['source'] if z else WHOLE),math_consequential=math))

d(1,'Opening, first word','Pour','Par','Pour','Large P followed by the low ou group and terminal r; the word is Pour.','misread word',bbox=[284,62,375,160],src=A)
d(2,'Opening, predicate after axiomes','vont passer',r'\ill{} passent','vont passer','The distinct group vont precedes passer; the final rising r belongs to passer.','readable ink left as \\ill{}',bbox=[798,176,1135,258],src=A,marked='yes')
d(3,'Opening, after quand',r'$=\unsure{=}$','même','$==$','Two adjacent pairs of horizontal strokes, including a short left return on the second pair.','misread symbol or index',cc=True,cp=1)
d(4,'Opening, final phrase',CU[1],'en forme','en forme','The tall loop and crossing entry are f; the following low r and terminal me support forme. No extra word follows.','other',cc=True,ch=False,cp=2)
d(5,'Opening, after en forme','','[\\ill{}]','','There is blank paper after forme, not a separate bracketed word.','text not on the page',cp=2,marked='yes')
d(6,'Definition, raised bracketed adjective',r'\inserted{[\uline{pleine}]}','',r'\inserted{[\uline{pleine}]}','Bracketed pleine is raised above sous-contrée and has its own underline.','omission',cp=5)
d(7,'Definition, hooked insertion leader','','','reading.tex: figure pleine-leader, the drawn curved leader below [pleine]','A separate long curved arm runs under the insertion and hooks down at the right of sous-contrée.','drawing or diagram',cc=True,cp=5)
d(8,'Definition, capital before equals',CU[2],r'\mathcal{C}',CAP,'A heavy outer C-like loop surrounds a thinner F-like vertical and crossbar at one glyph position; a single elaborate C remains possible.','insertion or placement',cc=True,cp=3,conf='low')
d(9,'Definition, family within tuple',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','Bent top stroke and curved lower stem, not a Gothic segmented F.','misread symbol or index',cp=3)
d(10,'Definition, second order',CU[3],r'\preccurlyeq',r'\preceq','The upper arms bend and the detached lower stroke is bowed; this is the same curved order used in C6.','other',cc=True,ch=False,cp=3)
d(11,'Definition, tout','tout',r'\struck{tout}',r'\unsure{tout|\deleted{tout}}','Two extended strokes run through the compressed middle; they may be letter strokes or a cancellation.','deletion state (struck given live or live given struck)',cc=True,cp=4,conf='low')
d(12,'Definition, after qui',CU[4],'satisfait',r'\unsure{satisfont|satisfait}','The group after f has a low oval and long joining stroke before final t; no secure dotted i distinguishes ai from on.','misread word',cc=True,cp=4,conf='low')
d(13,'a, abbreviation after sup',CU[5],'quelc.','quelc.','The final c and a detached point are both visible.','other',cc=True,ch=False,cp=6)
d(14,'a, line-broken verb after s’en',CU[6],'correspond','correspond','The second line ends spond, with an ascending d and no additional ant group.','other',cc=True,ch=False,cp=7)
d(15,'a, inserted correspondence formula',r"\inserted{par $\mathcal F'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}\mathcal F'\cap M$,}",r"\add{par $\mathfrak{F}' \mapsto \mathfrak{F}' \cap \mathcal{M}$,}",r"\inserted{par $\mathcal F'\mathrel{\vdash\joinrel\dashv}\mathcal F'\cap M$,}",'The horizontal link has a short cap at each end; the two F forms are curved and M has plain peaked stems.','misread symbol or index',cc=True,cp=8)
d(16,'a, inserted M prime and following de M',r"\inserted{$M'$} de $M$",r"\add{$\mathcal{M}'$} de $\mathcal{M}$",r"\inserted{$M'$} de $M$",'Both M forms have simple peaked strokes; the raised M has one separate prime.','misread symbol or index',cp=8)
d(17,'a, leaders for the two raised additions','','','reading.tex: figure a-insertion-leaders, both drawn strokes','One long hook begins before aux and runs beneath the added formula; a second short curved arm places M prime before de.','drawing or diagram',cc=True,cp=8)
d(18,'a, final correspondence and set condition',r"$M'\unsure{\mathrel{\mapstochar\relbar}|\mapsto}\mathcal F'=\{F\in\mathcal F\mid\overline F\subset M'\}$",r"$\mathcal{M}' \mapsto \mathfrak{F}' = \lbrace F \in \mathfrak{F} \mid F \subset \mathcal{M}' \rbrace$",r"$M'"+MAP+r"\mathcal F'=\{F\in\mathcal F\mid\overline F\subset M'\}$",'A left cap is clear and the dark right endpoint remains ambiguous; the condition F has a separate roof. M is plain and the family letters are curved.','misread symbol or index',cc=True,cp=8,conf='medium',math=True)
d(19,'Slanted left note on arbitrary versus finite sup',CM[0],HM[0],r'\margin{'+SUP+'}','The note reads Je ne sais ... quelconques ... ou bien de sup finis seulement. Condition is reduced; stricte has final e, and the last lge/large group and its closing parenthesis remain uncertain.','readable ink left as \\ill{}',cc=True,cp=9,conf='medium',marked='yes',math=True)
d(20,'b, M prime de M and following curved sign',r"$M'$ de $M$\unsure{\}|?},",r"$\mathcal{M}'$ de $\mathcal{M}$,",r"$M'$ de $M$\unsure{\}|?},",'Both M forms are plain. A separate crossed-top curly stroke stands before the comma; brace versus question-like mark is retained.','misread symbol or index',cp=10,conf='medium')
d(21,'b, deleted clause',r'\deleted{\unsure{à savoir|savoir} : si $X\in$}',r'\struck{\ill{} si $X \in F$}',r'\deleted{\unsure{savoir|à savoir} : si $X\in$}','One continuous strike crosses a compressed savoir/à savoir, colon and si X membership sign; no F follows that sign.','readable ink left as \\ill{}',cc=True,cp=10,conf='medium',marked='yes',math=True)
d(22,'b, raised replacement',r"\inserted{qu'on va formuler}",r'\ill{}',r"\inserted{qu'on va formuler}",'All three groups qu’on va formuler occupy the raised line above the cancelled clause. The line below belongs to the cancellation.','readable ink left as \\ill{}',cp=10,marked='yes')
d(23,'Marginal c, complete text excluding its separate pointer',CM[1],HM[1],CN,'Fixé ends at the accented e; G has a link capped at both ends. A single worked initial starts sous-fig., with no separate later cancelled s. The long link is a dash, commute and i.e. are readable, and no comma follows the first G prime.','readable ink left as \\ill{}',cc=True,cp=11,conf='medium',marked='yes')
d(24,'Marginal c, downward pointer','','','reading.tex: figure marginal-c, the oblique pointer with its hooked head','An oblique stroke descends from the aux area to a small hooked head beside i.e.; the head is visible.','drawing or diagram',cc=True,cp=11)
d(25,'C6, first diagram and right qualifier',CD[0],r"$F' \preccurlyeq F$, $G \leq F$ dans $\mathfrak{F}$.",RD[0]+r" ; \unsure{de|dans|ds} $\mathcal F$",'F prime is left of F and G below F; the vertical order points down with its bar at the right. The reduced d-word and looped family F stand lower and well to the right.','drawing or diagram',cc=True,cp=12,conf='medium')
d(26,'C6, slanted left gloss',CM[2],r'\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$',r'\unsure{symétrique|symetrique} en $\leq,\preceq$','The word has the ending trique and the next line begins en. A separate acute on the reduced middle is not secure; the long crossing rule does not cancel the gloss.','readable ink left as \\ill{}',cc=True,cp=13,conf='medium',marked='yes')
d(27,'C6, left vertical rule','','Editorial note excerpt: un trait vertical borde C6 à gauche','reading.tex: diagram C6-group, long left rule','The rule begins beside the heading and runs down past the start of the square; it is separate from the words.','drawing or diagram',cc=True,bbox=[236,521,275,1041],src=B)
d(28,'C6, two points left of first diagram','','','reading.tex: diagram C6-group, two diagonal points','Two separate dark points lie at about (517,1703) and (524,1707), well left of F prime; no punctuation function is assigned.','drawing or diagram',cc=True,cp=18)
d(29,'C6, small detached point by slanted orders','','','reading.tex: diagram C6-group, small point beside the left rule','A small independent point lies just beside the long rule below the slanted curved-order glyph.','drawing or diagram',cc=True,cp=13)
d(30,'C6(a), family after H membership',r'$H\in\mathcal F$',r'$H \in \mathfrak{F}$',r'$H\in\mathcal F$','H has two uprights and a cross stroke; the following F has a looped top and returned lower stroke.','misread symbol or index',cp=14)
d(31,'C6(a), final word and punctuation',CU[22],r'\ill{} :',CU[22],'A small closed group and two low strokes allow avec or ou; no separate colon follows.','readable ink left as \\ill{}',cp=14,conf='low',marked='yes')
d(32,'C6(a), circled label',r'\textcircled{a}','(a)',r'\textcircled{a}','A single continuous circle surrounds a at the start of the line.','drawing or diagram',bbox=[252,805,309,864],src=B)
d(33,'C6, lower square',CD[1],r"\[\n  F' \preccurlyeq F , \quad G' \preccurlyeq G , \qquad G' \leq F' , \quad G \leq F\n\]".replace(r'\n','\n'),RD[1],'The four nodes form a square; lower-left is G prime, although the preceding declaration says H. All four signs have the directions drawn in C.','drawing or diagram',bbox=[647,912,934,1135],src=B)
d(34,'C6(b), statement through X prime relation',r"et \textcircled{b} les \unsure{strates|str.tes|arêtes} de $G'$ sont les \deleted{\unsure{S}} \unsure{strates|str.tes|arêtes} $X'$ de $F'$ \unsure{tel|\deleted{tel}}les que $X'\ll\unsure{G|G_m|G_n}$.",r"(b) et les strates de $G'$ sont les strates $X'$ de $F'$ telles que $X' \ll G$.",BN,'The first noun has a point-like medial group. The second has one crossed initial s-position, not an additional complete s-word. The tel cross stroke remains ambiguous; two lowered terminal legs on G favour a small m.','deletion state (struck given live or live given struck)',cc=True,cp=15,conf='low',math=True)
d(35,'C6(b), two border strokes','','Editorial note excerpt: (b) est bordé d\'un double trait','reading.tex: diagram C6-group, two right-note rules and their short crossing strokes','Two parallel long rules border the note at left; their lower ends have a short diagonal and transverse stroke.','drawing or diagram',cc=True,cp=15)
d(36,'C6(b), lower added sentence',r'Ce complément \unsure{servira} plus bas',r'\ill{} complètement \ill{}',BC,'Ce precedes a worked complément group; its accent is point-like. Servira is reduced, while plus bas is readable on the next line.','readable ink left as \\ill{}',cc=True,cp=15,conf='medium',marked='yes')
d(37,'Bottom body, first G prime',r"$G'$",r"$G'$",r"$\unsure{G|\mathcal G}'$",'The small G has an inner bar and an extra outer return, unlike the plain square node; plain versus calligraphic form is retained without inventing an earlier glyph.','misread symbol or index',cc=True,cp=16,conf='medium')
d(38,'Bottom, first subd and underlines',r'\uline{subd} \uline{de} $G$ induite',r'\emph{subd.\ de $G$ induite}',r'\uline{subd} \uline{de} $G$ induite','There are two independent underlines, under subd and de. G and induite are not underlined, and no point follows this subd.','other',cp=16)
d(39,'Bottom, second subd','subd','subd.','subd','The final d runs into clear space before F prime; no separate point is visible.','abbreviation expanded or spelling modernised',cp=16)
d(40,'Bottom, marks after final F',r'$F$,',r'$F$,','reading.tex: figure bottom-punctuation, F with doubt-marked slant/loop and second low curve','The scan edge contains a long descending slant with a low loop and a second small curved stroke; one comma does not preserve both components.','drawing or diagram',cc=True,cp=16,conf='low')
d(41,'Bottom, before que','ou',r'\ill{}','ou','A low connected ou group precedes que; there is no secure accent above it.','readable ink left as \\ill{}',cp=16,marked='yes')
d(42,'Bottom, struck final word',r'\deleted{\unsure{sous-fig}}',r'\struck{sous-fig.}',r'\deleted{\unsure{sous-fig|sous-fig.}}','The struck word has sous-, a tall f and descending g; a final separate point cannot be distinguished from the thick strike at the edge.','other',cc=True,cp=16,conf='medium')
d(43,'Bottom-left slanted note',CM[4],r'\ill{} sur la sous-figure $G$ de $F$',BOTTOM,'The complete slanted note reads sur la sous-figure G de F. Its G has an inner bar and outer return; no extra word occupies H’s initial unread token.','readable ink left as \\ill{}',cc=True,cp=17,conf='medium',marked='yes')

for item in diff:
    if item['id']=='D25':item['additional_evidence']=[dict(crop=CP[18]['path'],bbox=CP[18]['bbox'],bbox_image=WHOLE,reason='The first-diagram nodes and orders; crop 12 supplies its distant right qualifier.')]
    if item['id']=='D23':item['additional_evidence']=[dict(crop=None,bbox=[1030,245,1670,536],bbox_image=B,reason='Complete upper F-prime and full marginal note in the single supplied-half view.')]

cd=[]
def cdisp(n,loc,reading,status,ink,cp,related=()):
    x=CP[cp]
    z=dict(location=f'C{n:02}: '+loc,c=CU[n-1],reading=reading,status=status,scan_shows=ink,crop=x['path'],bbox=x['bbox'],bbox_image=x['source'])
    if related:z['additional_evidence']=[dict(crop=CP[v]['path'],bbox=CP[v]['bbox'],bbox_image=CP[v]['source']) for v in related]
    cd.append(z)

cdisp(1,'Second repetition sign','=', 'resolved','A second pair of bars is visible; its left return does not form a word.',1)
cdisp(2,'Opening final phrase','en forme','resolved','Tall descending f and low r/me group.',2)
cdisp(3,'Initial contrée capital',CAP,'revised','One overprinted position; retain F-under-C versus one elaborate C, with layers superimposed.',3)
cdisp(4,'Tuple second order',r'\preceq','resolved','Bent upper arms and bowed detached lower stroke.',3)
cdisp(5,'Verb after qui',r'\unsure{satisfont|satisfait}','revised','Low oval and join after f favour on, but ai remains possible; the crop cuts the low f tail, not this medial group.',4)
cdisp(6,'sup abbreviation','quelc.','resolved','Separate c and terminal point.',6)
cdisp(7,'a correspondence verb','correspond','resolved','The continued line ends spond, without ant.',7)
cdisp(8,'Inserted family link',r'\mathrel{\vdash\joinrel\dashv}','resolved','Short caps at both ends; no sloped head.',8)
cdisp(9,'Link after M prime',MAP,'revised','Left cap is clear; dark right terminal permits a point, cap or very small head.',8)
cdisp(10,'First parenthetic condition',r'(\unsure{condition} stricte)','revised','Stricte ends with e. The compressed preceding word retains uncertainty.',9)
cdisp(11,'Cancelled word after stricte',r'\deleted{\unsure{et}}','retained','A small crossed group has an e/t-like loop and stem.',9)
cdisp(12,'After ou bien','de','resolved','A d and short terminal stroke, without an additional s.',9)
cdisp(13,'Last parenthetic condition',r'\unsure{(condition lge|(condition large|(condition lge)|(condition large)}','revised','The final group is l plus a small g-like loop; full large and the closing parenthesis remain uncertain.',9)
cdisp(14,'Curved mark after M',r'\unsure{\}|?}','retained','Curly lower stroke with a crossed top; no secure separate question point.',10)
cdisp(15,'Deleted beginning of clause',r'\unsure{savoir|à savoir}','revised','The left crossed group can be s; a distinct preceding à is not secure.',10)
cdisp(16,'Instruction above marginal c',r'\unsure{reporter|rajouter}','retained','A descending p-like stroke and later upright favour reporter, but the low middle remains reduced.',11)
cdisp(17,'subd. fixé','fixé','resolved','An acute and a final low e are visible; no extra e follows.',11)
cdisp(18,'Worked initial before sous-fig.',r'\unsure{\rlap{\deleted{F}}sous-fig.|Sous-fig.}','revised','F-like crossbars and a curled s share one initial position; do not add a separate leading letter.',11)
cdisp(19,'Line between sous-fig. phrases',r'\mathrel{\relbar\joinrel\relbar}','resolved','Long horizontal with no secure sloping arrowhead.',11)
cdisp(20,'Alleged separate cancelled s after F prime','','revised','No second word-sized or letter-sized position is visible there; the lower worked stroke belongs to the initial at the left.',11)
cdisp(21,'Marginal c ending','i.e.','resolved','i stem, its point, e loop and final point are present.',11)
cdisp(22,'Qualifier right of first diagram',r'\unsure{de|dans|ds}','retained','An initial looped d and one low terminal undulation.',12)
cdisp(23,'C6(a) last word',r'\unsure{avec|ou}','retained','Closed low first group and two subsequent short strokes do not decide the word.',14)
cdisp(24,'First noun in C6(b)',r'\unsure{strates|str.tes}','revised','The initial st/r sequence is visible, but the middle is point-like; arêtes lacks support here.',15)
cdisp(25,'Crossed initial at second noun',r'\unsure{\deleted{s}|s}','revised','Only one initial position is present; its loop is crossed. No independent older S plus full new word is asserted.',15)
cdisp(26,'Second noun in C6(b)',r'\unsure{\deleted{s}|s}tr\unsure{a|.}tes','revised','Following the worked initial, t/r and tes are visible; the medial a versus point remains open.',15)
cdisp(27,'tel in telles',r'\unsure{tel|\deleted{tel}}les','retained','The long t-like bar also traverses tel; cancellation versus letter bar is unresolved.',15)
cdisp(28,'Terminal G in X prime relation',r'\unsure{G_m|G_n|G}','revised','Two short lowered legs are distinct and favour m; n or a worked G ending remains possible.',15)
cdisp(29,'Verb before plus bas',r'\unsure{servira}','retained','The group is a run of low connected strokes with too little internal separation for certainty.',15)
cdisp(30,'Last cancelled word',r'\deleted{\unsure{sous-fig|sous-fig.}}','revised','Letters through g are readable; terminal point is not separable from the strike.',16)

context_rows=[z for z in (PKT/'C_context.md').read_text().split('# C notes')[0].splitlines() if z.startswith('|')]
assert len(context_rows)==23
ctx_specs=[
 (1,3,[3],CAP+r', \mathcal F','revised','One worked initial C position; adjacent family F is clearly curved.'),
 (2,3,[3,18],r'\leq,\preceq,\rotatebox{90}{$\leq$}','resolved','Straight order and bowed subdivision are distinct; vertical orders point down with detached bars at right.'),
 (3,8,[8,11],r'\mathrel{\vdash\joinrel\dashv}; '+MAP+r'; \mathrel{\vdash\joinrel\dashv}; \mathrel{\relbar\joinrel\relbar}','revised','Inserted family and marginal G links have caps; M-prime endpoint stays doubtful; sous-fig. link is a dash.'),
 (4,8,[8],r"\overline F\subset M';\quad \inserted{$M'$}",'resolved','Separate roof above the plain F; one prime on each M prime.'),
 (5,15,[15],r"X'\ll\unsure{G_m|G_n|G}",'revised','Two lowered legs favour m; no normalization to the simple G.'),
 (6,11,[11,15],r'\textcircled{a},\textcircled{b},\textcircled{c}','resolved','C6 labels have surrounding circles; definition a) and b) have closing parentheses.'),
 (7,1,[1,2],r'$==$; en forme','resolved','Two pairs of bars and a descending f at forme.'),
 (8,3,[3],CAP+r';\preceq','revised','Capital state remains open; curved order is clear.'),
 (9,6,[6,7],'quelc.; s’en correspond','resolved','Terminal dot on abbreviation; d rather than ant at the end of the line-broken verb.'),
 (10,8,[8,11],r'\mathrel{\vdash\joinrel\dashv}; '+MAP+'; marginal G two caps','revised','Each link was checked locally; the M-prime endpoint alone remains open.'),
 (11,9,[9],SUP,'revised','Retain reduced condition, crossed et and lge/large with uncertain closing parenthesis; stricte ends in e.'),
 (12,10,[10],r'\unsure{\}|?}, \deleted{\unsure{savoir|à savoir} : si $X\in$}','revised','Curly mark remains open; cancelled clause ends at membership, with no F.'),
 (13,11,[11],CN,'revised','Fixé and i.e. resolved; reporter and initial overlay retained; alleged separate s rejected.'),
 (14,12,[12],r'\unsure{de|dans|ds}','retained','Low undulation after d remains ambiguous.'),
 (15,14,[14],r'\unsure{avec|ou}','retained','Three small groups at line end do not resolve the wording.'),
 (16,15,[15],r'\unsure{strates|str.tes};\quad\unsure{\deleted{s}|s}tr\unsure{a|.}tes','revised','Two occurrences checked separately; second has one worked initial position.'),
 (17,15,[15],r'\unsure{tel|\deleted{tel}}les;\quad\unsure{servira}','retained','Cross stroke through tel and reduced servira remain open.'),
 (18,16,[16],r'\deleted{\unsure{sous-fig|sous-fig.}}','revised','Word readable; punctuation at edge doubtful.'),
 (19,4,[4],r'\unsure{satisfont|satisfait}','revised','On is favoured but not decided over ai.'),
 (20,9,[9],'de','resolved','No separate final s after the short d/e group.'),
 (21,15,[15],r'\unsure{G_m|G_n|G}','revised','Two short legs retained, independently of the earlier plain G nodes.'),
 (22,14,[14],r"H;\quad G'",'resolved','Declaration has two upright H stems; the square has rounded G and a prime. The mismatch is preserved.'),
 (23,7,[7],"s'en correspond",'resolved','The second line ends with a d; grammatical agreement was not used to supply an ending.'),
]
for n,primary,ev,read,status,ink in ctx_specs:
    x=CP[primary]
    cells=re.split(r'(?<!\\)\|',context_rows[n-1])
    scope=cells[2].strip() if cells[1].strip()=='72' else cells[1].strip()
    quoted=cells[3].strip().strip('`').replace(r'\|','|')
    z=dict(location=f'CTX{n:02}: '+scope,c=quoted,reading=read,status=status,scan_shows=ink,crop=x['path'],bbox=x['bbox'],bbox_image=x['source'],additional_evidence=[dict(crop=CP[k]['path'],bbox=CP[k]['bbox'],bbox_image=CP[k]['source']) for k in ev if k!=primary])
    if n in (2,22):z['additional_evidence'].append(dict(crop=None,bbox=[647,912,934,1135],bbox_image=B,reason='Lower square, observed in the single supplied-half view.'))
    if n==6:z['additional_evidence'].append(dict(crop=None,bbox=[252,805,309,864],bbox_image=B,reason='Circled a, observed in the supplied-half view.'))
    cd.append(z)

inv=[]
def invadd(el,kind,pos,words):inv.append(dict(element=el,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
for row in [
 ('folio','text','top centre','71'),('opening','text','top four lines','Pour la suite'),
 ('definition heading','text','upper body, left','Définition 1'),('definition body','text','below opening','On appelle sous-contrée'),
 ('pleine','insertion','above sous-contrée','[pleine]'),('pleine leader','drawing','below raised adjective','curved hooked arm'),
 ('worked contrée capital','deletion','before tuple equals','possible F beneath C, retained as an alternative'),
 ('possible tout cancellation','deletion','after tuple','tout, live/cancelled alternatives'),
 ('condition a','text','middle upper body','a) fermé pour'),('family correspondence','insertion','above aux parties','par F prime capped-link F prime intersection M'),
 ('family correspondence leader','drawing','under raised formula','long hooked line'),('M prime insertion','insertion','above de M','M prime'),('M prime leader','drawing','beside raised M prime','short curved arm'),
 ('sup question','margin note','slanted left middle','Je ne sais'),('crossed et','deletion','inside slanted sup note','et, uncertain'),
 ('condition b','text','middle body','b) fermé pour'),('cancelled b clause','deletion','after M and curved mark','savoir/à savoir : si X membership'),
 ('replacement b clause','insertion','above cancellation','qu’on va formuler'),
 ('marginal c','margin note','right above C6','reporter/rajouter; circled c Pour'),('worked sous-fig. initial','deletion','marginal c, left of sous-fig.','possible F/s overlay at one position'),
 ('c pointer','drawing','descending from marginal c','long oblique pointer with hooked head'),
 ('C6 heading','text','lower third, left','C6 Soit'),('first C6 diagram','diagram','below Soit','F prime, F above G'),
 ('first diagram points','drawing','left of first diagram','two diagonally offset points'),('symmetry gloss','margin note','slanted left of first diagram','symétrique/symetrique en'),
 ('C6 left rule','drawing','left of C6 statement','long vertical rule crossing the slanted gloss'),('gloss point','drawing','beside left rule below orders','one detached point'),
 ('C6 a sentence','text','between diagrams','circled a Alors il existe un unique H'),('C6 square','diagram','below C6 a','F prime F over G prime G'),
 ('C6 b statement','margin note','right of square','et circled b les strates/str.tes'),('worked second noun initial','deletion','C6 b second line','single crossed s-position'),
 ('possible tel cancellation','deletion','C6 b third line','tel in telles, retained alternatives'),('C6 b border','drawing','left of right marginal statement','two rules with lower cross strokes'),
 ('C6 b lower sentence','margin note','under X prime relation','Ce complément/complement servira plus bas'),
 ('bottom definition','text','last two horizontal lines','On dit que G prime est la subd de G induite'),('bottom punctuation','drawing','after F in last line','long slant/loop and second low curved stroke'),
 ('last cancelled word','deletion','bottom right','sous-fig, possible final point'),('lower slanted note','margin note','bottom left','sur la sous-figure G de F'),
]:invadd(*row)

remaining=[
 ('Definition capital',CAP,[r'F overwritten by C at one position',r'\mathscr C',r'\mathbb C'],'low','Inner F-like strokes coexist with an outer C-like loop.'),
 ('tout',r'\unsure{tout|\deleted{tout}}',['tout',r'\deleted{tout}'],'low','Extended middle strokes may be lettering or cancellation.'),
 ('satisfont/satisfait',r'\unsure{satisfont|satisfait}',['satisfont','satisfait'],'low','The medial ai/on group is compressed.'),
 ('M prime link',MAP,[r'\mathrel{\mapstochar\relbar}',r'\mapsto',r'\mathrel{\vdash\joinrel\dashv}'],'medium','The right endpoint is dark and very short.'),
 ('First condition word',r'\unsure{condition}',['condition'],'medium','Several middle letters are reduced to low strokes.'),
 ('Cancelled et',r'\deleted{\unsure{et}}',['et'],'low','Crossing obscures the small loop and stem.'),
 ('Last slanted parenthesis',r'\unsure{(condition lge|(condition large|(condition lge)|(condition large)}',['(condition lge','(condition large','(condition lge)','(condition large)'],'low','Reduced final group and no secure separate closing parenthesis.'),
 ('Mark after M in b',r'\unsure{\}|?}',[r'\}','?'],'low','Crossed top over a curled lower stroke.'),
 ('Deleted clause opening',r'\unsure{savoir|à savoir}',['savoir','à savoir'],'low','An independent initial à is not securely separable.'),
 ('Marginal instruction',r'\unsure{reporter|rajouter}',['reporter','rajouter'],'low','Low medial strokes remain insufficiently separated.'),
 ('Initial sous-fig. state',r'\unsure{\rlap{\deleted{F}}sous-fig.|Sous-fig.}',[r'\rlap{\deleted{F}}sous-fig.','Sous-fig.'],'low','One dense initial position has both bar-like and curled strokes.'),
 ('First-diagram qualifier',r'\unsure{de|dans|ds}',['de','dans','ds'],'low','Only d and a low undulation are individually secure.'),
 ('Slanted symmetry accent',r'\unsure{symétrique|symetrique}',['symétrique','symetrique'],'medium','No secure separate acute is visible over the reduced middle.'),
 ('C6(a) last word',r'\unsure{avec|ou}',['avec','ou'],'low','Three low groups do not resolve the letters.'),
 ('C6(b) first noun',r'\unsure{strates|str.tes}',['strates','str.tes'],'medium','Point-like medial group could be reduced a or literal point.'),
 ('C6(b) second initial',r'\unsure{\deleted{s}|s}',[r'\deleted{s}','s'],'low','The single initial loop is crossed; cancellation status remains open.'),
 ('C6(b) second noun middle',r'\unsure{a|.}',['a','.'],'low','Tiny medial group is not securely alphabetic.'),
 ('tel in telles',r'\unsure{tel|\deleted{tel}}les',['telles',r'\deleted{tel}les'],'low','The t-like bar crosses the same span that a deletion would.'),
 ('Terminal G relation',r'\unsure{G_m|G_n|G}',[r'G_m',r'G_n','G'],'low','Two lowered legs suggest m but merge with the main letter exit.'),
 ('complément accent',r'\unsure{complément|complement}',['complément','complement'],'medium','The high mark is point-like and the ending is retraced.'),
 ('servira',r'\unsure{servira}',['servira'],'low','The low internal letters are not individually secure.'),
 ('First bottom G prime',r"$\unsure{G|\mathcal G}'$",['G',r'\mathcal G'],'medium','A local inner bar and outer return leave alphabet style open.'),
 ('Bottom punctuation','reading.tex: figure bottom-punctuation',['one comma with additional worked stroke','two comma-like strokes','unassigned graphic marks'],'low','Long slant/loop and second low curve meet the sheet edge.'),
 ('Final deleted punctuation',r'\deleted{\unsure{sous-fig|sous-fig.}}',['sous-fig','sous-fig.'],'medium','The dark strike and edge obscure any independent final point.'),
 ('Lower slanted G',r'$\unsure{G|\mathcal G}$',['G',r'\mathcal G'],'medium','This local glyph also has a clear inner bar and outer return.'),
]
remaining=[dict(location=a,reading=b,alternatives=c,confidence=d,reason=e) for a,b,c,d,e in remaining]

hp_dispositions=[
 ('vont passer','vont passer',['D02'],None,'The unread group is vont; passent is also corrected to passer.'),
 ('after en forme','',['D05'],2,'No distinct word or bracket occupies the unread placeholder.'),
 ('b raised clause',r"\inserted{qu'on va formuler}",['D22'],10,'The complete raised phrase replaces the cancelled clause.'),
 ('b deleted clause',r'\deleted{\unsure{savoir|à savoir} : si $X\in$}',['D21'],10,'Unread opening belongs to the cancelled savoir/à savoir group.'),
 ('sup marginal note, first placeholder',SUP,['D19'],9,'The three placeholders are aligned collectively with this complete physical note; they are not counted again as three omissions.'),
 ('sup marginal note, second placeholder',SUP,['D19'],9,'Same complete-note disposition; the finite/arbitrary wording is transcribed.'),
 ('sup marginal note, parenthetic placeholder',SUP,['D19'],9,'Same complete-note disposition; parenthetic wording remains explicitly doubtful.'),
 ('marginal c before aux Sup','commute',['D23'],11,'Commute is readable.'),
 ('C6 a end',r'\unsure{avec|ou}',['D31'],14,'Best alternatives retained; the supplied colon is not visible.'),
 ('H note on lower C6 b sentence, first placeholder',BC,['D36'],15,'Ce and the worked complément word are represented together; H’s complètement is editorial, not literal text.'),
 ('H note on lower C6 b sentence, second placeholder',BC,['D36'],15,'The remainder is servira plus bas, with servira still doubtful.'),
 ('H marginal before symétrie',r'\unsure{symétrique|symetrique} en $\leq,\preceq$',['D26'],13,'The entire physical gloss has this wording; there is no independently separable additional word before it.'),
 ('H marginal after symétrie','en',['D26'],13,'The short word en precedes the two orders.'),
 ('H marginal before sur la sous-figure',BOTTOM,['D43'],17,'No extra word before sur; H merged two physically separate slanted notes.'),
 ('Final main line before que','ou',['D41'],16,'Ou is readable and has no secure accent.'),
]
ill_positions=[m.start() for m in re.finditer(r'\\ill\{\}',H)]
assert len(ill_positions)==len(hp_dispositions)==15
hp=[]
for i,(pos,sp) in enumerate(zip(ill_positions,hp_dispositions),1):
    loc,read,ids,cropn,why=sp;z=CP[cropn] if cropn else None
    hp.append(dict(id=f'HILL{i:02}',location=loc,h_context=H[max(0,pos-38):min(len(H),pos+65)],reading=read,disposition=why,difference_ids=ids,crop=z['path'] if z else None,bbox=z['bbox'] if z else [798,176,1135,258],bbox_image=z['source'] if z else A))

notation=[
 dict(sign='two repetition pairs',latex='$==$',appearance='Two adjacent unequal bar pairs, second with a short left return.',location='Opening after quand',alternatives=[]),
 dict(sign='contrée capital',latex=CAP,appearance='Outer C-like loop and inner upright/crossbar in one position.',location='Definition before equals',alternatives=[r'\mathscr C',r'\mathbb C']),
 dict(sign='family F',latex=r'\mathcal F',appearance='Bent or looped top and returned lower stem; local occurrences checked.',location='Tuple, both a formulas, right of first diagram, H declaration',alternatives=[]),
 dict(sign='ambient M',latex='M',appearance='Simple peaked strokes; primes are detached short ticks.',location='All M and M-prime occurrences in a and b',alternatives=[]),
 dict(sign='two orders',latex=r'\leq,\preceq',appearance='Straight angular order versus bent upper arms with bowed lower stroke.',location='Tuple, conditions, both diagrams and slanted note',alternatives=[]),
 dict(sign='vertical order',latex=r'\rotatebox{90}{$\leq$}',appearance='Downward angle and detached stroke at right.',location='First diagram once, square twice',alternatives=[]),
 dict(sign='capped correspondence',latex=r'\mathrel{\vdash\joinrel\dashv}',appearance='Horizontal line with short end caps; no full arrowhead.',location='Inserted a formula and marginal G link',alternatives=[]),
 dict(sign='M-prime link',latex=MAP,appearance='Clear left cap and very short dark right endpoint.',location='Final a formula',alternatives=[r'\mapsto',r'\mathrel{\vdash\joinrel\dashv}']),
 dict(sign='roof over F',latex=r'\overline F',appearance='Separate horizontal roof above a plain F.',location='Set condition in a',alternatives=[]),
 dict(sign='terminal small legs on G',latex=r'\unsure{G_m|G_n|G}',appearance='Two short lowered stems touch the end of G.',location='C6 b, X prime relation',alternatives=[r'G_n','G']),
 dict(sign='bottom small G forms',latex=r'\unsure{G|\mathcal G}',appearance='Inner bar and outer loop/return; no independently recoverable older glyph asserted.',location='First G prime of bottom body and G of lower slanted note',alternatives=[r'\mathcal G']),
 dict(sign='circled labels',latex=r'\textcircled{a},\textcircled{b},\textcircled{c}',appearance='Letters inside continuous circles; b is raised beside et.',location='C6',alternatives=[]),
 dict(sign='detached points and bottom strokes',latex='TikZ in C6-group and bottom-punctuation',appearance='Two diagonal points, one point beside the left rule, and two low punctuation-like strokes.',location='First C6 diagram, slanted orders, bottom line',alternatives=['No linguistic function assigned to the points; bottom punctuation function retained as doubtful.']),
]
abbreviations=[dict(form=a,expansion=b) for a,b in [('sous-ens.','sous-ensemble'),('sup','supremum'),('quelc.','quelconques'),('lge','large (uncertain abbreviation)'),('subd.','subdivision'),('subd','subdivision'),('sous-fig.','sous-figure'),('sous-fig','sous-figure'),('Sup','supremum'),('i.e.','id est')]]

report=dict(reader='R2',cote='156-4',scan='72',brief_version='v08',started_utc='2026-11-20T12:06:37Z',finished_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),image_views=[WHOLE,A,B],reading_file=str(OUT/'reading.tex'),differences=diff,c_doubts=cd,inventory=inv,remaining_doubts=remaining,notation=notation,abbreviations=abbreviations,notes=dict(summary='Handwritten folio 71: definition of a full sub-contrée, question about arbitrary or finite sup, and C6 with two diagrams and several slanted/marginal additions. All text, insertions, worked positions and separate drawing strokes are represented.',math_reading_decisions='The H versus G-prime mismatch between the existence sentence and square triggered a local letter comparison; H and G-prime are retained. The roof over F and relation directions were checked because their loss would change the formula. No mathematical argument overruled the ink, and no theorem was proved.',author_checks='The author explicitly questions whether arbitrary or finite sup should be used. The lower sentence says the complement will serve below, with its reduced verb left doubtful. These are manuscript notes, not proof certificates.',title_dates_pagination='Visible folio 71; scan marker 72 retained. Définition 1 and C6 are underlined. No date or overall page count is visible.'),check_events=[],crops=CROPS,workflow_feedback=['One-crop framing limits are reported: crop 04 cuts the deep f tail, though its target medial letters remain visible; crop 11 reaches the top of the c formula, whose full F-prime was already seen in the half. Neither clipped boundary is used to establish absence.','A workspace replacement lost the first crop files. They were regenerated from the identical retained rectangles and transformations after the parent restored the same assigned source; already viewed images were not viewed again.'],h_placeholders=hp,h_editorial_dispositions=[dict(h=HN[0],disposition='The inserted wording is qu’on va formuler, not the editorial suggestion qui ne plus an unread word. The long stroke below belongs to the cancelled clause. The circled c and its pointer are represented.'),dict(h=HN[1],disposition='The circle and square-layout observations agree with visible marks. The lower note reads Ce complément/complement servira plus bas with explicit doubts, rather than complètement. Both side rules are drawn.')],inspection_log=str(OUT/'inspection_log.md'),recovery=dict(workspace_replacement=True,regenerated_identically=True,repeated_successful_views=False,last_successful_view_before_loss='09_oblique_sup_note.jpg',first_successful_view_after_restore='10_b_correction.jpg'))

(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(diff),c_doubts=len(cd),inventory=len(inv),remaining_doubts=len(remaining),crops=len(CROPS),h_placeholders=len(hp)),indent=2))
