from pathlib import Path
from datetime import datetime, timezone
import json,re
O=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R3')
P=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_072')
C=(P/'C.tex').read_text(); H=(P/'H.tex').read_text(); R=(O/'reading.tex').read_text()
M=json.loads((O/'crop_metadata.json').read_text())
whole=M[0]['source']; a=whole.replace('.jpg','_a.jpg'); b=whole.replace('.jpg','_b.jpg')
D=[]
def d(loc,c,h,r,ink,n=None,box=None,half='a',conf='high',kind='other',marked='no',cc=False,hh=True,math=False):
 if n:
  m=M[n-1]; crop=m['path']; bbox=m['bbox']; source=m['source']
 else:
  crop=None; bbox=box; source=a if half=='a' else b
 D.append(dict(id=f'D{len(D)+1:02}',location=loc,c=c,h=h,reading=r,scan_shows=ink,confidence=conf,kind=kind,marked_in_h=marked,change_c=cc,change_h=hh,crop=crop,bbox=bbox,bbox_image=source,source=source,math_consequential=math))
 return D[-1]['id']
# Opening and definition.
d('Opening, first word','Pour','Par','Pour','The first word has the rounded ou group after P.',box=[280,65,385,170],kind='misread word')
d('Opening, after axiomes','vont passer',r'\ill{} passent','vont passer','A separate vont precedes passer; passer ends with a low r.',box=[800,180,1140,260],kind='readable ink left as \\ill{}',marked='yes')
d('Opening, quand and repetition signs',r'quand $=\unsure{=}$','quand même',r'quand $= =$','Two adjacent pairs of bars are present; the second lower bar starts with a hook.',1,kind='misread symbol or index',cc=True)
d('Opening, final phrase',r'\unsure{en forme|en jeu}','en forme','en forme','The large ascender and descending closed loop are f, followed by reduced orme.',2,kind='misread word',cc=True,hh=False)
d('Raised bracketed pleine',r'\inserted{[\uline{pleine}]}',r'[\ill{}]',r'\inserted{[\uline{pleine}]}','The bracketed underlined word is pleine; its leader joins sous-contrée, not en forme.',3,kind='insertion or placement',marked='yes',math=True)
d('Hooked leader of pleine','','',r'% fig-pleine','A long separate curved stroke passes over contrée, dips at the right and turns upward.',3,kind='drawing or diagram',cc=True)
d('Definition, composite capital',r'\unsure{\deleted{\mathcal F}\mathcal C|\mathscr C|\mathbb C}',r'\mathcal{C}',r'\unsure{\deleted{\mathcal F}\mathcal C|\mathscr C|\mathbb C}','One composite position contains an outer curve, an upright and an interior cross stroke; overprint versus elaborate C remains open.',4,conf='low',kind='misread symbol or index')
d('Definition, family F inside tuple',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The family capital has a swept upper arm and hooked stem, not a Gothic construction.',4,kind='misread symbol or index')
d('Definition, second order',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','The upper arms and lower stroke are bowed, visibly unlike the adjacent straight order.',4,kind='misread symbol or index',cc=True,hh=False,math=True)
d('Definition, state of tout','tout',r'\struck{tout}',r'\unsure{tout|\deleted{tout}}','A long transverse stroke can belong to the letters or to cancellation; neither state is secure.',4,conf='low',kind='deletion state (struck given live or live given struck)',cc=True,math=True)
d('Definition, verb after qui',r'\unsure{satisfait|satisfont}','satisfait',r'\unsure{satisfait|satisfont}','The low connected group after f does not distinguish ai from on.',5,conf='low',kind='misread word')
# Condition a.
d('a, after sup',r'\unsure{quelc.}','quelc.','quelc.','The abbreviation and its separate final point are visible.',6,kind='misread word',cc=True,hh=False)
d('a, correspondence word',r'\unsure{correspond|correspondant}','correspond','correspond','The lower continuation ends in a rising d; there is no additional ant group.',7,kind='misread word',cc=True,hh=False)
d('a, inserted family mapping link',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mapsto',r'\mathrel{\vdash\joinrel\dashv}','The short horizontal has a vertical cap at both ends and no separate arrowhead.',7,kind='misread symbol or index',cc=True)
d('a, both inserted family symbols',r'\mathcal F\;\mathcal F',r'\mathfrak{F}\;\mathfrak{F}',r'\mathcal F\;\mathcal F','Both raised F capitals have swept or returned upper arms; the two occurrences were checked locally.',7,kind='misread symbol or index')
d('a, M in inserted intersection',r'M',r'\mathcal{M}',r'M','The inserted M is a plain two-peaked capital.',7,kind='misread symbol or index')
d('a, raised M prime and following de M',r"\inserted{$M'$} de $M$",r"\add{$\mathcal{M}'$} de $\mathcal{M}$",r"\inserted{$M'$} de $M$",'The raised letter has one prime; the following plain M has none.',7,kind='misread symbol or index')
d('a, separate leaders for par phrase and M prime','','',r'% fig-a-insertions','One long curved leader runs below the raised par phrase; a shorter separate curved arm lifts toward M prime.',7,kind='drawing or diagram',cc=True)
d('a, lower M prime mapping link',r'\unsure{\mathrel{\mapstochar\relbar}|\mapsto}',r'\mapsto',r'\unsure{\mathrel{\mapstochar\relbar}|\mathrel{\vdash\joinrel\dashv}|\mapsto}','The left cap is clear; a thick short right endpoint permits a cap or an imperfect head.',8,conf='low',kind='misread symbol or index',cc=True)
d('a, two plain M primes in lower mapping',r"M'\ ;\ M'",r"\mathcal{M}'\ ;\ \mathcal{M}'",r"M'\ ;\ M'",'Both lower M letters are plain and both have a distinct prime.',8,kind='misread symbol or index')
d('a, lower mapping family F prime and membership family F',r"\mathcal F'\ ;\ \mathcal F",r"\mathfrak{F}'\ ;\ \mathfrak{F}",r"\mathcal F'\ ;\ \mathcal F",'The left F has an upper loop; the membership-family F has a bent swept cap, unlike the adjacent plain F.',8,kind='misread symbol or index')
d('a, barred plain F in the set condition',r'\overline F',r'F',r'\overline F','A separate horizontal roof stands over the second plain F.',8,kind='omission',math=True)
marginC=r"\margin{Je ne sais s'il faut prendre des sup quelconques \unsure{(condition stricte)|(condition stricts)} \deleted{\unsure{et}} ou bien \unsure{de|des} sup finis seulement \unsure{(condition large)|(condition lge)}}"
marginH=r'\marginal{il faudra \ill{} des \ill{} (\ill{})}'
d('Entire upper-left oblique question',marginC,marginH,marginC,'The note begins Je ne sais s’il faut prendre and continues through both alternatives; the compressed condition forms, crossed et and de/des remain doubtful.',9,conf='low',kind='omission',marked='yes',math=True)
# Condition b.
d('b, M prime de M alphabets',r"$M'$ de $M$",r"$\mathcal{M}'$ de $\mathcal{M}$",r"$M'$ de $M$",'Both capitals have the same plain peaked form; only the first carries a prime.',10,kind='misread symbol or index')
d('b, extra sign after final M',r'\unsure{\}|?}',r'',r'\unsure{\}|?}','A crossed upper loop and bent lower stroke precede the comma; no separate question point is secure.',10,conf='low',kind='omission')
d('b, raised replacement phrase',r"\inserted{qu'on va formuler}",r'\ill{}',r"\inserted{qu'on va formuler}",'The complete raised phrase is qu’on va formuler, above the cancelled clause.',10,kind='readable ink left as \\ill{}',marked='yes')
d('b, entire cancelled clause, before plus bas',r'\deleted{\unsure{à savoir|savoir} : si $X\in$}',r'\struck{\ill{} si $X \in F$}',r'\deleted{\unsure{à savoir|savoir} : si $X\in$}','The struck clause ends at the visible membership sign; no following F appears, and the whole clause stands before plus bas.',10,conf='low',kind='insertion or placement',marked='yes',math=True)
# Right marginal c.
d('Marginal c, introductory instruction',r'\unsure{reporter|rajouter}',r'',r'reporter','The initial r and descending p followed by the t-group support reporter.',11,kind='omission',cc=True)
d('Marginal c, circled label',r'\textcircled{c}','(c)',r'\textcircled{c}','A continuous enclosing circle surrounds c.',11,kind='drawing or diagram',marked='yes')
d('Marginal c, subd. adjective',r'\unsure{fixé|fixée}','fixée',r'\unsure{fixé|fixée}','The accent is visible, but the tiny terminal group does not securely separate an extra e.',11,conf='low',kind='misread word')
d('Marginal c, G mapping',r'\mathrel{\vdash\joinrel\dashv}',r'\mapsto',r'\mathrel{\vdash\joinrel\dashv}','Both ends of the horizontal link are capped; there is no full right arrowhead.',11,kind='misread symbol or index')
d('Marginal c, worked initial of first sous-fig.',r'\deleted{\unsure{F}}sous-fig.','sous-fig.',r'\unsure{S|s|\rlap{\deleted{F}}s}ous-fig.','The dark initial and its low strokes share one position; an old F is possible but not a separate preceding letter.',11,conf='low',kind='deletion state (struck given live or live given struck)',cc=True)
d('Marginal c, alleged extra cancelled s',r'\deleted{\unsure{s}}','',r'% fig-marginal-c','The low crossed strokes continue the same worked initial at the left; no independent s after F prime is established.',11,conf='low',kind='text not on the page',cc=True,hh=False)
d('Marginal c, long link between sous-fig. phrases',r'\unsure{-|\longrightarrow}',r'\to',r'\unsure{-|\longrightarrow}','The long horizontal ends with a slight dark rise, insufficient to establish an arrowhead.',11,conf='low',kind='misread symbol or index')
d('Marginal c, punctuation after second F prime',r"$F'$",r"$F'$,",r"$F'$",'The prime is present; no separate following comma is visible before the next line.',11,kind='other')
d('Marginal c, commute','commute',r'\ill{}','commute','The joined low groups end in the tall t and final e of commute.',11,kind='readable ink left as \\ill{}',marked='yes')
d('Marginal c, i.e.',r'\unsure{i.e.}','i.e.','i.e.','The i, the low intermediate point, looped e and separate terminal point are visible.',11,kind='misread word',cc=True,hh=False)
d('Marginal c, descending pointer','','',r'% fig-marginal-c','A long curved stroke descends from the aux area and ends in a returning hook beside i.e.',11,kind='drawing or diagram',marked='yes',cc=True)
# C6, diagrams and notes.
d('C6, first diagram geometry',r'\diagram{\begin{tikzcd}',r"\emph{C6} \quad Soit $F' \preccurlyeq F$, $G \leq F$ dans $\mathfrak{F}$.",r'% diagram-C6-first','F prime is left of F, while G is directly below F with a downward-facing straight order between them.',box=[625,555,905,775],half='b',kind='drawing or diagram')
d('C6, qualifier beside first diagram',r'\unsure{de|dans|ds}','dans',r'\unsure{de|dans|ds}','The d-loop is followed by a single low extended group, leaving de/dans/ds open.',12,conf='low',kind='misread word')
d('C6, family F beside first diagram',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The upper arm returns in a distinct loop on this local F.',12,kind='misread symbol or index')
d('C6, H terminal period after family qualifier',r'',r'$\mathfrak{F}$.',r'$\mathcal F$','There is clear paper after the family letter without a separate stop.',12,kind='other')
d('C6, two detached marks left of first diagram','','',r'% detached-points-C6','Two distinct small black points lie diagonally down and right, without an assigned function.',18,kind='drawing or diagram',cc=True)
d('C6, left rule','','',r'% fig-C6-group','A long nearly vertical rule runs from beside C6 to beside the lower square, crossing the slanted note.',box=[235,510,285,1045],half='b',kind='drawing or diagram',marked='yes',cc=True)
d('C6, upper slanted note and separation from lower note',r'\margin{symétrique en $\leq,\preceq$}',r'\marginal{\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{} sur la sous-figure $G$ de $F$}',r'\unsure{symétrique|symetrique} en\quad$\leq,\preceq$','The upper note reads symétrique/symetrique en and two orders; there is no separate word before it or after the signs, and the lower sur-note is spatially separate.',13,conf='medium',kind='insertion or placement',marked='yes',cc=True)
d('C6 a, circled label',r'\textcircled{a}','(a)',r'\textcircled{a}','The small a is enclosed by a circular stroke.',box=[245,802,315,877],half='b',kind='drawing or diagram',marked='yes')
d('C6 a, family F in membership',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The family capital has both a curled top and a broad lower return.',14,kind='misread symbol or index')
d('C6 a, final word',r'\unsure{avec|ou}',r'\ill{}',r'\unsure{avec|ou}','Three separate low groups follow the family symbol; they leave avec/ou unresolved.',14,conf='low',kind='readable ink left as \\ill{}',marked='yes')
d('C6 a, H colon after final word','',':','','No colon follows the low final groups.',14,kind='text not on the page')
d('C6, square diagram geometry',r'\diagram{\begin{tikzcd}',r"F' \preccurlyeq F , \quad G' \preccurlyeq G , \qquad G' \leq F' , \quad G \leq F",r'% diagram-C6-square','F prime and F form the top row, G prime and G the bottom; the straight orders point down with detached strokes to the right.',box=[650,915,935,1135],half='b',kind='drawing or diagram',marked='yes')
d('C6 b, circled label and relative word placement',r'et \textcircled{b} les','(b) et les',r'et \raisebox{.65ex}{\textcircled{b}} les','The circle around b is raised after et and before les.',15,kind='insertion or placement',marked='yes',cc=True)
d('C6 b, first strates',r'\unsure{strates|str.tes|arêtes}','strates',r'\unsure{strates|str.tes}','The initial s/t structure is visible; a point-like medial group leaves full spelling versus contraction open.',15,conf='low',kind='misread word',cc=True)
d('C6 b, cancelled initial before second strates',r'\deleted{\unsure{S}}','',r'\deleted{\unsure{S}}','A crossed S-shaped group stands immediately left of the second word; the older letter remains doubtful.',15,conf='low',kind='omission')
d('C6 b, second strates',r'\unsure{strates|str.tes|arêtes}','strates',r'\unsure{strates|str.tes}','The second word has its own tied medial strokes; it is checked separately from the first.',15,conf='low',kind='misread word',cc=True)
d('C6 b, beginning of telles',r'\unsure{tel|\deleted{tel}}les','telles',r'\unsure{tel|\deleted{tel}}les','The long horizontal across tel can be a t-bar or cancellation; the following les is live.',15,conf='low',kind='deletion state (struck given live or live given struck)')
d('C6 b, final G with lowered ticks',r'\unsure{G|G_m|G_n}',r'G',r'\unsure{G_m|G_n|G}','Two low dark ticks adjoin the G’s terminal stroke, favouring a small m/n but not settling a subscript.',15,conf='low',kind='misread symbol or index',cc=True,math=True)
d('C6 b, sentence below X relation',r'Ce complément \unsure{servira} plus bas','',r'Ce compl\unsure{é|e}ment \unsure{servira} plus bas','Ce and plus bas are visible; the tiny high accent-like point and reduced servira strokes remain uncertain.',15,conf='low',kind='omission',marked='yes',cc=True)
d('C6 b, paired bordering rules','','',r'% note-C6-b and paired rules','Two long parallel strokes border the note, with additional short crossed strokes near their lower ends.',15,kind='drawing or diagram',marked='yes',cc=True)
# Bottom paragraph.
d('Bottom, first subd punctuation','subd','subd.','subd','No point follows the first d before the next word.',16,kind='other')
d('Bottom, extent of underlining',r'\uline{subd} \uline{de} $G$ induite',r'\emph{subd.\ de $G$ induite}',r'\uline{subd} \uline{de} $G$ induite','There are two separate rules, under subd and de; G and induite have no rule.',16,kind='other')
d('Bottom, second subd punctuation',r'par la subd',r'par la subd.',r'par la subd','The second abbreviation also has no separate point.',16,kind='other')
d('Bottom, final F after de',r'F',r'F',r'\unsure{F|F\prime}','A long high-to-low stroke and a low hook follow this F at the sheet edge; an extra prime cannot be excluded.',16,conf='low',kind='misread symbol or index',cc=True,math=True)
d('Bottom, ou before que','ou',r'\ill{}','ou','The low ou group is present, without a separate upper accent.',16,kind='readable ink left as \\ill{}',marked='yes')
d('Bottom, cancelled ending',r'\deleted{\unsure{sous-fig}}',r'\struck{sous-fig.}',r'\deleted{\unsure{sous-fig}}','The f, dot of i and descending g remain under the cancellation; no separate terminal stop is secure.',16,conf='medium',kind='deletion state (struck given live or live given struck)')
# Mark composite noncontiguous alphabet snippets as explicit excerpts, not alleged source strings.
for i in [15,20,21]:
 D[i-1]['quotation_scope']='Noncontiguous local alphabet occurrences, in physical reading order; each occurrence belongs to this one named phrase.'
# Extract C unsure macros so every literal C doubt receives its own disposition.
def macros(s,macro):
 out=[]
 for m in re.finditer(re.escape('\\'+macro+'{'),s):
  j=m.end(); dep=1
  while dep:
   if s[j]=='{' and s[j-1]!='\\':dep+=1
   elif s[j]=='}' and s[j-1]!='\\':dep-=1
   j+=1
  out.append(s[m.start():j])
 return out
diags=macros(C,'diagram')
D[38]['c']=diags[0]
D[38]['h']=r"$F' \preccurlyeq F$, $G \leq F$"
D[38]['quotation_scope']='Diagram excerpt: only relative node and sign positions are compared here; qualifier, alphabet and punctuation have separate rows.'
D[49]['c']=diags[1]
D[49]['quotation_scope']='Complete C square and complete H displayed relations; only geometry is counted in this row.'
D[34]['c']=''; D[34]['h']=','; D[34]['reading']=''
D[41]['c']=''; D[41]['h']='.'; D[41]['reading']=''
D[44]['c']=r'\margin{symétrique en $\leq,\preceq$}'+'\n'+r'\margin{sur la sous-figure $G$ de $F$}'
D[44]['reading']=r'\unsure{symétrique|symetrique} en $\leq,\preceq$'+'\n'+r'\margin{sur la sous-figure $G$ de $F$}'
D[44]['quotation_scope']='Noncontiguous excerpt of the two notes: the upper note is in fig-C6-group, the lower note alongside the bottom paragraph. H merges them. The long rule has its own graphic row.'
D[63]['kind']='other'
cu=macros(C,'unsure'); assert len(cu)==30
spec=[
('Opening, second repetition sign','=', 'resolved',1,'Two separate bars, with a small hook on the lower one.',[7]),
('Opening, en forme','en forme','resolved',2,'Tall f ascender and descending loop exclude jeu.',[7]),
('Definition, first capital',cu[2],'retained',4,'Outer C-like curve and interior F-like upright/cross stroke share one position.',[1,8]),
('Definition, second order',r'\preceq','resolved',4,'The lower stroke is bowed rather than straight.',[2,8]),
('Definition, after qui',cu[4],'retained',5,'The reduced ai/on group is not settled.',[19]),
('a, after sup','quelc.','resolved',6,'Terminal c and a detached point are visible.',[9]),
('a, after s’en','correspond','resolved',7,'The line continuation ends at d.',[9,23]),
('a, raised mapping link',r'\mathrel{\vdash\joinrel\dashv}','resolved',7,'Two short end caps are visible.',[3,10]),
('a, lower mapping link',r'\unsure{\mathrel{\mapstochar\relbar}|\mathrel{\vdash\joinrel\dashv}|\mapsto}','revised',8,'The right endpoint also permits a cap, alongside the existing alternatives.',[3,10]),
('Oblique question, first condition phrase',cu[9],'retained',9,'Compressed condition strokes and final e/s-like exit remain unsettled; no confident full expansion is claimed.',[11]),
('Oblique question, crossed small group',cu[10],'retained',9,'Small crossed loops could be et.',[11]),
('Oblique question, after ou bien',cu[11],'retained',9,'A short d-and-tail group does not decide a final s.',[20]),
('Oblique question, last parenthesis',cu[12],'retained',9,'The low joined middle of large/lge is not separable.',[11]),
('b, after M',cu[13],'retained',10,'The curved sign has a crossed head and no secure detached question point.',[12]),
('b, struck clause opening',cu[14],'retained',10,'The cancellation obscures whether à precedes savoir.',[12]),
('Marginal c, instruction','reporter','resolved',11,'A descending p and later t-group are visible.',[13]),
('Marginal c, adjective',cu[16],'retained',11,'The accent is clear; an extra final e remains doubtful.',[13]),
('Marginal c, alleged prior F',r'\unsure{S|s|\rlap{\deleted{F}}s}','revised',11,'One worked initial may contain old F; it is not a separate full letter to the left.',[13]),
('Marginal c, long link',cu[18],'retained',11,'No full right arrowhead is secure.',[3,10]),
('Marginal c, alleged separate deleted s',r'% fig-marginal-c','revised',11,'Low strokes belong to the same worked initial position; no separate s is asserted.',[13]),
('Marginal c, endpoint','i.e.','resolved',11,'The two letters and points can be distinguished.',[13]),
('C6, first diagram qualifier',cu[21],'retained',12,'The d is clear but its low continuation is reduced.',[14]),
('C6 a, last word',cu[22],'retained',14,'Three low separated groups do not settle avec/ou.',[15]),
('C6 b, first strates',r'\unsure{strates|str.tes}','revised',15,'The s/t beginning is visible; medial point-like strokes leave full versus contracted spelling.',[16]),
('C6 b, deleted S',cu[24],'retained',15,'The crossed group has S-like loops but remains partly obscured.',[16]),
('C6 b, second strates',r'\unsure{strates|str.tes}','revised',15,'This occurrence has its own tied medial strokes, separately inspected.',[16]),
('C6 b, tel state',cu[26],'retained',15,'A t-bar and cancellation are both compatible with the long touch.',[17]),
('C6 b, G ending',r'\unsure{G_m|G_n|G}','revised',15,'Lowered ticks favour m/n before the single-letter interpretation.',[5,21]),
('C6 b, added sentence verb',cu[28],'retained',15,'The low humps and final exit support servira without settling every letter.',[17]),
('Bottom, crossed ending',cu[29],'retained',16,'The cancellation leaves fig clearer than the reduced sous prefix.',[18])]
CD=[]
for k,(loc,r,status,n,ink,rows) in enumerate(spec,1):
 m=M[n-1]; CD.append(dict(id=f'CU{k:02}',location=loc,c=cu[k-1],reading=r,status=status,scan_shows=ink,crop=m['path'],bbox=m['bbox'],bbox_image=whole,source=whole,context_rows=rows))
def cx(id,loc,c,r,status,ink,n=None,box=None,half='b',rows=[]):
 m=M[n-1] if n else None
 CD.append(dict(id=id,location=loc,c=c,reading=r,status=status,scan_shows=ink,crop=m['path'] if m else None,bbox=m['bbox'] if m else box,bbox_image=whole if m else (a if half=='a' else b),source=whole if m else (a if half=='a' else b),context_rows=rows))
cx('CTX-FAMILY','Tuple, local family F',r'\mathcal F',r'\mathcal F','resolved','The upper arm is curved; no Gothic or double-stroke construction is present.',4,rows=[1])
cx('CTX-DIAGRAMS','C6, both local order diagrams',r'\preceq;\rotatebox{90}{$\leq$}',r'\preceq;\rotatebox{90}{$\leq$}','resolved','Both horizontal curved orders point left; each vertical straight order points down with its detached stroke on the right.',box=[630,550,940,1140],rows=[2])
cx('CTX-G-LINK','Marginal c, local G link',r'G\mathrel{\vdash\joinrel\dashv}G\prime',r'G\mathrel{\vdash\joinrel\dashv}G\prime','resolved','The G link has two short vertical caps, unlike an ordinary arrowhead.',11,rows=[3,10])
cx('CTX-BAR','a, roof over plain F',r'\overline F\subset M\prime',r'\overline F\subset M\prime','resolved','The roof is separate and covers only the plain F.',8,rows=[4])
cx('CTX-MPRIME','a, raised M prime and following plain M',r"\inserted{$M'$} de $M$",r"\inserted{$M'$} de $M$",'resolved','One prime is raised with the inserted M; the following baseline M has none.',7,rows=[4])
cx('CTX-CIRCLES','C6 labels a, b, c',r'\textcircled{a},\textcircled{b},\textcircled{c}',r'\textcircled{a},\textcircled{b},\textcircled{c}','resolved','Each label is enclosed; definition labels a) and b) instead have a closing parenthesis. Local evidence is half b for a, crop 15 for b and crop 11 for c.',box=[245,250,1665,935],rows=[6])
cx('CTX-H-G','C6 a declaration and lower-left square node',r'H;G\prime',r'H;G\prime','resolved','The declaration has two uprights joined diagonally; the square node is rounded G plus a prime. Both positions are contained in this half-image box; the mismatch is preserved.',box=[640,770,1490,1145],rows=[22])
# Remaining doubts: every final unsure, in physical/textual occurrence order.
ru=macros(R,'unsure')
rd_specs=[
('Definition, composite capital',['overwritten family F then C','single script C','double-stroked C'],'One composite glyph has both outer curve and inner cross stroke.'),
('Definition, tout state',['live tout','cancelled tout'],'The long stroke can be a letter join or a cancellation.'),
('Definition, verb',['satisfait','satisfont'],'Low medial strokes remain reduced.'),
('a, lower M prime link',['left-capped dash','two-capped line','mapsto'],'The right endpoint is thick and short.'),
('Oblique question, first condition phrase',['condition stricte','condition stricts'],'The word condition itself is compressed, and the terminal letter of stricte is not secure.'),
('Oblique question, cancelled group',['et'],'Crossing obscures a small looped group.'),
('Oblique question, after ou bien',['de','des'],'The final low tail is unresolved.'),
('Oblique question, final condition phrase',['condition large','condition lge'],'The low middle could be contracted.'),
('b, after M',['closing brace','question-like mark'],'A crossed upper loop and bent stem lack a separate secure dot.'),
('b, struck opening',['à savoir','savoir'],'The long cancelling rule obscures the first group.'),
('Marginal c, adjective',['fixé','fixée'],'There is too little terminal separation to settle an extra e.'),
('Marginal c, one worked initial',['S','s','old F overlaid by s'],'One dark initial and its low strokes do not establish two successive cancelled letters.'),
('Marginal c, long horizontal',['dash','arrow'],'There is no secure full head.'),
('C6, first diagram qualifier',['de','dans','ds'],'Only d and a reduced low continuation are clear.'),
('C6, upper slanted note accent',['symétrique','symetrique'],'No independent acute stroke is secure in this occurrence.'),
('C6 a, final word',['avec','ou'],'Three reduced separated groups remain ambiguous.'),
('C6 b, first noun',['strates','str.tes'],'The medial group can be a contraction point.'),
('C6 b, cancelled initial',['S'],'A crossing leaves only partly recoverable loops.'),
('C6 b, second noun',['strates','str.tes'],'Its independent medial group remains tied.'),
('C6 b, first three letters of telles',['live tel','cancelled tel'],'The long horizontal may be the t-bar.'),
('C6 b, terminal mathematical object',['G_m','G_n','G'],'Two downward ticks abut G; their separation as a subscript is not certain.'),
('C6 b, complément accent',['é','e'],'The upper point is not a secure acute slash.'),
('C6 b, final sentence verb',['servira'],'The medial pen humps are reduced.'),
('Bottom, last F after de',['F','F prime'],'A high-to-low stroke and a low hook crowd the sheet edge.'),
('Bottom, cancelled last abbreviation',['sous-fig'],'The heavy cancellation obscures the initial letters.')]
assert len(ru)==len(rd_specs),(len(ru),len(rd_specs))
RD=[dict(location=loc,reading=u,alternatives=alt,confidence='low',reason=reason) for u,(loc,alt,reason) in zip(ru,rd_specs)]
# Inventory: every block, drawing, insertion and deletion is represented separately.
I=[]
def inv(element,kind,pos,first): I.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('folio','text','top centre','71')
inv('opening','text','upper four lines','Pour la suite')
inv('definition-heading','text','below opening','Définition 1')
inv('definition-body','text','below heading','On appelle sous-contrée')
inv('pleine','insertion','above sous-contrée','[pleine]')
inv('pleine-leader','drawing','above and across sous-contrée','fig-pleine: hooked enclosure')
inv('composite-capital','deletion','definition tuple, first capital','Possible F under C, one position, alternatives retained')
inv('tout-state','deletion','definition, after tuple','Possible cancellation of tout, alternatives retained')
inv('condition-a','text','middle-upper body','a) fermé pour')
inv('raised-map','insertion','a, above aux parties','par family F prime capped-link family F prime intersection M')
inv('raised-map-leader','drawing','a, below raised map','Long shallow curved arm')
inv('raised-Mprime','insertion','a, above de M','M prime')
inv('raised-Mprime-leader','drawing','a, above de M','Short separate curved arm')
inv('a-set-formula','display','a, last line','M prime mapping family F prime equals set')
inv('oblique-question','margin note','left of a and b, rising rightward','Je ne sais')
inv('oblique-et','deletion','inside oblique question','Uncertain et')
inv('condition-b','text','middle body','b) fermé pour')
inv('b-cancelled-clause','deletion','after M prime de M','à savoir/savoir : si X membership')
inv('b-replacement','insertion','above cancelled clause','qu’on va formuler')
inv('marginal-c','margin note','right, above C6','reporter; circled c Pour')
inv('marginal-c-worked-initial','deletion','first sous-fig. initial in c','One worked S/s, possible prior F')
inv('marginal-c-pointer','drawing','below c toward C6','Long descending returning hook')
inv('C6-heading','text','lower half, left','C6')
inv('Soit','text','beside C6','Soit')
inv('C6-first','diagram','below Soit','F prime, F, G; two orders; qualifier and family F')
inv('C6-detached-points','drawing','left of first diagram','Two separate diagonal points')
inv('C6-left-rule','drawing','left of C6 and both diagrams','Single long rule')
inv('C6-upper-oblique','margin note','left of first diagram, crossing rule','symétrique/symetrique en')
inv('C6-a','text','below first diagram','circled a Alors il existe un unique H')
inv('C6-square','diagram','below a','F prime and F above G prime and G')
inv('C6-b','margin note','right of square','et circled b les strates')
inv('C6-b-old-S','deletion','second strates in b','Uncertain crossed S')
inv('C6-b-tel','deletion','telles in b','Possible cancellation of tel')
inv('C6-b-relation','display','fourth line of b note','X prime much less than G with possible lowered m/n')
inv('C6-b-extension','margin note','immediately below b relation','Ce complément/complement servira plus bas')
inv('C6-b-rules','drawing','left border of b note','Two parallel rules with short lower crossed strokes')
inv('lower-oblique','margin note','bottom left, rising rightward','sur la sous-figure G de F')
inv('bottom-definition','text','bottom two lines','On dit que G prime est la subd de G')
inv('bottom-cancelled-ending','deletion','lower right at sheet edge','sous-fig')
# All H unreadable placeholders, in physical source order; no double-counted omission claims.
hp=[
('Opening after axiomes','D02','vont within vont passer'),
('Bracket after en forme','D05','[pleine], raised over sous-contrée; this is not an extra missing word after en forme'),
('b before plus bas','D26','qu’on va formuler'),
('b struck clause opening','D27','à savoir/savoir; the final alleged F is unsupported'),
('Oblique question after il faudra','D23','Whole oblique question mapped as one passage; H’s prefix is itself inaccurate'),
('Oblique question after des','D23','Same single passage, sup quelconques and finite alternative'),
('Oblique question parenthesis','D23','Same single passage, both uncertain condition phrases'),
('Marginal c before aux Sup','D36','commute'),
('C6 a after family F','D48','avec/ou remains doubtful'),
('H editorial quotation below b, first ill','D57','Ce; editorial quotation only, not an independent missing word in H body'),
('H editorial quotation below b, second ill','D57','servira plus bas; editorial quotation only'),
('H marginal note before symétrie','D45','No independent preceding word is visible'),
('H marginal note after symétrie','D45','en; word itself is symétrique/symetrique'),
('H marginal note after order signs','D45','No independent extra word; sur-note occurs separately below'),
('Bottom before que','D63','ou')]
# Bind placeholder audit to actual row IDs by robust location lookup rather than numerical guesses.
locid={x['location']:x['id'] for x in D}
refs=['Opening, after axiomes','Raised bracketed pleine','b, raised replacement phrase','b, entire cancelled clause, before plus bas','Entire upper-left oblique question','Entire upper-left oblique question','Entire upper-left oblique question','Marginal c, commute','C6 a, final word','C6 b, sentence below X relation','C6 b, sentence below X relation','C6, upper slanted note and separation from lower note','C6, upper slanted note and separation from lower note','C6, upper slanted note and separation from lower note','Bottom, ou before que']
HP=[dict(id=f'HILL{i:02}',location=t[0],difference_id=locid[ref],disposition=t[2]) for i,(t,ref) in enumerate(zip(hp,refs),1)]
N=[
 dict(sign='two repetition marks',latex=r'= =',appearance='Two pairs of bars, the second lower bar beginning in a hook.',location='Opening after quand',alternatives=[]),
 dict(sign='composite contrée capital',latex=cu[2],appearance='One outer loop plus interior F-like upright and bar.',location='Definition tuple',alternatives=[r'\mathscr C',r'\mathbb C']),
 dict(sign='family letters',latex=r'\mathcal F',appearance='Swept upper arm or loop; each occurrence locally checked.',location='Tuple; two inserted map symbols; two lower-map family symbols; first diagram qualifier; a membership',alternatives=[]),
 dict(sign='plain M',latex='M',appearance='Two peaks without a separate script flourish.',location='All M occurrences, prime counts kept locally',alternatives=[]),
 dict(sign='straight and curved orders',latex=r'\leq;\preceq;\rotatebox{90}{$\leq$}',appearance='Straight angle/bar versus bowed arms; vertical straight orders point down with detached stroke right.',location='Definition, conditions, c and both C6 diagrams',alternatives=[]),
 dict(sign='two-capped links',latex=r'\mathrel{\vdash\joinrel\dashv}',appearance='Horizontal with a short vertical at each end.',location='Raised family map; marginal G map',alternatives=[]),
 dict(sign='lower M map',latex=spec[8][1],appearance='Clear left cap, thick uncertain right termination.',location='a, lower map',alternatives=[r'\mathrel{\vdash\joinrel\dashv}',r'\mapsto']),
 dict(sign='long horizontal',latex=cu[18],appearance='Long line with a small dark end-rise.',location='Marginal c between sous-fig. phrases',alternatives=[r'\longrightarrow']),
 dict(sign='bar and primes',latex=r'\overline F;M\prime;F\prime;G\prime;X\prime',appearance='Separate roof or single raised short tick at each named occurrence.',location='a, diagrams and marginal b',alternatives=[]),
 dict(sign='lowered terminal ticks',latex=r'\unsure{G_m|G_n|G}',appearance='G ends with two short descending strokes.',location='b beside square',alternatives=['G_n','G']),
 dict(sign='circled labels',latex=r'\textcircled{a},\textcircled{b},\textcircled{c}',appearance='Actual surrounding circular strokes; b raised after et.',location='C6 a, right b and marginal c',alternatives=[]),
 dict(sign='detached points',latex=r'% detached-points-C6',appearance='Two small separate dark points arranged down-right.',location='Left of first C6 diagram',alternatives=['function unassigned']),
 dict(sign='last F prime doubt',latex=r'\unsure{F|F\prime}',appearance='High-to-low stroke and low hook at lower page edge.',location='Bottom, second de F',alternatives=['F prime'])]
A=[dict(form=x,expansion=y) for x,y in [('sous-ens.','sous-ensemble'),('sup','supremum'),('quelc.','quelconques'),('subd.','subdivision'),('subd','subdivision'),('sous-fig.','sous-figure'),('sous-fig','sous-figure'),('Sup','supremum'),('i.e.','id est'),('str.tes (possible)','strates'),('lge (possible)','large')]]
report=dict(reader='R3',cote='156-4',scan='72',brief_version='v08',started_utc='2026-11-20T12:06:46.643829Z',finished_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),image_views=[whole,a,b],reading_file=str(O/'reading.tex'),differences=D,c_doubts=CD,inventory=I,remaining_doubts=RD,notation=N,abbreviations=A,notes=dict(summary='Folio 71 introduces a full sub-contrée by two closure conditions and adds C6 with two order diagrams and marginal refinements. All ink is manuscript. One worked initial is kept as one position; both diagrams, insertion arms, marginal pointer, rules and detached points are drawn.',math_reading_decisions='No theorem was proved or independently validated. Comparing the two distinct order shapes, the roof over F, capped map links, and the literal H versus square-node G prime drew attention to local signs; visible ink alone determined or preserved each reading. The lowered ticks on G and the last F prime remain uncertain.',author_checks='The author writes H in the existence clause but G prime in the square. This inconsistency is transcribed without repair. The oblique question explicitly leaves arbitrary versus finite suprema open. No external mathematical inference was used.',title_dates_pagination='Visible running folio 71; headings Définition 1 and C6. No date or page count. The lowest line reaches the sheet edge.'),check_events=[],crops=[{k:m[k] for k in ['path','source','bbox','scale','rotation','reason']} for m in M],workflow_feedback=['The one-crop rule was respected for each open locus. Spatially overlapping difficult words in one marginal block were handled in one complete local crop, avoiding recropping a settled mark.','A workspace replacement interrupted this run after crop 12. Only identical own crops and logs were reconstructed, and inspection resumed at crop 13 after root authorization; no repeated image view.'],h_placeholder_audit=HP,h_editorial_note_dispositions=[dict(quotation='« qui ne » et un mot souligné non lu',disposition='The actual raised phrase is qu’on va formuler; formuler has no separate secure underline. The quoted H note is editorial and is not counted as literal omitted page text.',evidence=M[9]['path']),dict(quotation='« \\ill{} complètement \\ill{} »',disposition='The added line is Ce complément/complement servira plus bas. The two unreadable markers in this editorial quotation map to the same one restored sentence, not additional missing groups.',evidence=M[14]['path']),dict(quotation='un trait vertical borde C6 à gauche; (b) est bordé d’un double trait',disposition='These descriptions identify real strokes; both are transcribed graphically in fig-C6-group rather than left as notes.',evidence=b)],inspection_log=str(O/'inspection_log.md'),restoration=dict(occurred=True,repeated_views=False,description='Own crop files 01–17 and inspection metadata were lost with the workspace, then reconstructed identically from preserved rectangles and transformations before continuation. Crop 18 was a genuinely new still-open point locus.'))
# Explicit scope notes for all quotations constructed from separated alphabet occurrences.
for x in D:
 if '\\;' in x['c'] or '\\ ;' in x['c']:
  x['quotation_scope']='Diagram/phrase alphabet excerpt: multiple separated occurrences named in location, not a contiguous sentence quotation.'
# Source excerpt indices on unmarked context checks make their coverage auditable.
report['context_coverage']={str(i):[x['id'] for x in CD if i in x.get('context_rows',[])] for i in range(1,24)}
assert all(report['context_coverage'].values())
assert len(HP)==len(re.findall(r'\\ill\{\}',H))
assert all(type(x[k]) is bool for x in D for k in ['change_c','change_h','math_consequential'])
assert all(Path(x['crop']).exists() for x in D if x['crop'])
assert all(x['kind'] in ['text','display','diagram','drawing','margin note','insertion','deletion'] for x in I)
assert all(x['sheet_kind']=='text' and x['hand']=='his hand' for x in I)
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(D),c_doubts=len(CD),remaining_doubts=len(RD),inventory=len(I),crops=len(M),h_placeholders=len(HP)),ensure_ascii=False))
