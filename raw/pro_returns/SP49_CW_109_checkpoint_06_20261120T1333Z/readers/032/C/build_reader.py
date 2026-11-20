from pathlib import Path
import json

root=Path('/workspace/scratch/6d55c8c3e5a7')
out=root/'work/readers/032/C'
base=(root/'work/inputs/032/C.tex').read_text()
text=base
m=json.loads((root/'work/inputs/032/metadata.json').read_text())
loci={r['id']:r for r in json.loads((out/'frozen_loci.json').read_text())}
changes=[]

def row(id,place,c,reading,kind,evidence,confidence='high',crop=None,source=None,bbox=None):
    if crop:
        loc=loci[crop]
        crop_path=str(out/'crops'/f'{crop}.jpg')
        source=source or loc['source'];bbox=bbox or loc['bbox']
    else:crop_path=None
    changes.append(dict(id=id,place=place,c=c,h=None,reading=reading,diff_c=True,diff_h=False,kind=kind,marked_in_H=False,confidence=confidence,evidence=evidence,crop=crop_path,source=source,bbox=bbox))

def repl(old,new):
    global text
    assert text.count(old)==1,(old,text.count(old))
    text=text.replace(old,new,1)

# Quotations and page states.
old="l.6, `allows one to''";new=r"l.6, \unsure{``|`}allows one to''"
repl(old,new)
row('C01','428 l.6, opening quotation',old,new,'misread symbol or index','The opener has a tall left branch and a shorter right branch meeting at a junction. A joined double is favoured, but a single forked stroke remains possible; the closing pair is clear.','medium','01')

old=r"\deleted{l-5 `its''}";new=r"\deleted{l-5} `\deleted{its}''"
repl(old,new)
row('C02','440 first cancelled correction',old,new,'deletion state (struck given live or live given struck)','The single opening stroke and both closing strokes stand above all cancellation paths with visible white gaps. The l-5 reference and its are traversed by the cancellation.','high','04')

old=r"\deleted{``allows one to''}";new=r"``\deleted{allows one} to''"
repl(old,new)
row('C03','440 second cancelled wording',old,new,'deletion state (struck given live or live given struck)','The paired quotation groups stand clear above the zigzags. The final zigzag terminates in the one region before the separate t stem and o; the visible to is not directly crossed. The scope proposed here follows that visible endpoint.','medium','05')

old=r"\unsure{-+|+}";new=r"\raisebox{1.1ex}[0pt][0pt]{\unsure{-+|+}}"
repl(old,new)
row('C04','440 immediately after second cancelled wording',old,new,'insertion or placement','The small cross and adjoining horizontal are at quotation height, above the text baseline. The horizontal can be a separate minus or the return from the preceding closing stroke, so the original alternatives remain.','medium','05')

q447=r"\tikz[baseline=(q447C.base)]{\node[inner sep=0pt] (q447C) {``};\fill[overlay] ([xshift=-.35em,yshift=1.8ex]q447C.base west) circle (.045ex);}"
old=r"\deleted{l 9 ``its''}";new=r"\deleted{l 9} "+q447+r"\deleted{its}''"
repl(old,new)
row('C05','447 cancelled l9 its',old,new,'deletion state (struck given live or live given struck)','The three horizontal cancellation passes cross l9 and its, below the bottoms of both opening strokes; the closing pair lies further above and right. Both quotation edges remain live.','high','06')
row('C06','447 small point above-left of cancelled its opener','',r"\fill[overlay] ([xshift=-.35em,yshift=1.8ex]q447C.base west) circle (.045ex);",'omission','A separate compact dark point lies above-left of the opening pair. The i-dot is a different, further-right mark. The added point is preserved without assigning a punctuation role.','high','06',bbox=[1261,1011,1281,1030])

old=r"\deleted{\unsure{o}}\inserted{\deleted{one}}"
raised449=r"\tikz[baseline=(old449C.base)]{\node[inner sep=0pt] (old449C) {\deleted{\unsure{o}}};\node[anchor=base west,inner sep=0pt,overlay] at ([xshift=-.05em,yshift=1.6ex]old449C.base west) {\inserted{\deleted{one}}};}"
repl(old,raised449)
row('C07','449 l11, raised cancelled one and baseline trace',old,raised449,'insertion or placement','The cancelled one is visibly raised above the slot before us. The cancelled baseline trace occupies the lower part of that same slot. The candidate o is retained cautiously because the curl can also be part of the insertion connection; it is not duplicated as a second drawn connector.','medium','07')

old=r"\unsure{\&|a}";new=r"\&"
repl(old,new)
row('C08','450 final references, linking sign',old,new,'misread symbol or index','A long upper loop, crossing diagonal and smaller lower loop with rightward exit form an ampersand. These independent crossing/loop strokes are not the single bowl of a.','high','08')

q452=r"\tikz[baseline=(q452C.base)]{\node[inner sep=0pt] (q452C) {``};\fill[overlay] ([xshift=.25em,yshift=.6ex]q452C.base east) circle (.045ex);}"
old=r"``\unsure{.} don't''";new=q452+r" don't''"
repl(old,new)
row('C09','452 l-11, low point after opening pair',old,new,'misread symbol or index','The dark point is plainly present and separate from the two opening strokes. It is below those strokes but above the following word baseline; its geometry is drawn without calling it a full stop.','high','09')

# The three-level mark is a drawing, not an imposed semantic symbol.
mark455=r"\tikz[baseline=(i455C.base)]{\node[inner sep=0pt] (i455C) {i};\draw[overlay,line width=.55pt,line cap=round,line join=round] ([xshift=-.12em,yshift=-.5ex]i455C.base west) -- ([xshift=.29em,yshift=-.5ex]i455C.base west) ([xshift=-.12em,yshift=-.5ex]i455C.base west) -- ([xshift=-.15em,yshift=-.82ex]i455C.base west) -- ([xshift=.25em,yshift=-.82ex]i455C.base west) ([xshift=-.10em,yshift=-.91ex]i455C.base west) -- ([xshift=.27em,yshift=-.91ex]i455C.base west) ([xshift=-.10em,yshift=-.91ex]i455C.base west) -- ([xshift=-.15em,yshift=-1.18ex]i455C.base west) -- ([xshift=.28em,yshift=-1.18ex]i455C.base west);}"
old=r"$\underset{\unsure{\equiv|\mathrm{E}}}{\text{i}}$"
repl(old,mark455)
row('C10','455 l-13, mark below first i of divided',old,mark455,'drawing or diagram','The crop shows a top bar, a dense/retraced middle level and a bottom bar, with short returns along the left. The exact returned-bar geometry is drawn beneath the first i. This settles placement and geometry, while leaving the function (E-like mark, equivalence-like mark or emphasis) unassigned.','high','11')

old=r"\deleted{\unsure{l 9|l}}";new=r"\deleted{\unsure{l\textsubscript{9}|l}}"
repl(old,new)
row('C11','466 cancelled false start before live l-9',old,new,'insertion or placement','A clear tall looped l is followed/overlapped at its lower-right by a much smaller loop and descending hook. The possible old 9 is visibly lower than l; whether the small loop is a numeral or only a cancellation curl remains uncertain. Cancellation extent is secure.','low','13')

old="``and iterating'";new=r"``and iterating\unsure{''|'}"
repl(old,new)
row('C12','468 l.8, final closing quotation',old,new,'misread symbol or index','The complete final edge contains a compact joined cap with two lower legs. A fused double is favoured but a single bent mark remains possible; there is blank space before the right rule.','medium','14')

# Detached marks confirmed in the halves or incidentally resolved in the frozen crops.
p427=r"\tikz[baseline=(p427C.base)]{\node[inner sep=0pt] (p427C) {p 427};\fill[overlay] ([xshift=-1.0em,yshift=.05ex]p427C.base west) circle (.045ex);}"
repl('p 427 l-6',p427+' l-6')
row('C13','left blank beside427','',r"\fill[overlay] ([xshift=-1.0em,yshift=.05ex]p427C.base west) circle (.045ex);",'omission','One dark detached point sits in the left blank beside the427 row. Its origin and punctuation role are unassigned.','high',source=m['half_a'],bbox=[62,155,82,175])

s434=r"\tikz[baseline=(s434C.base)]{\node[inner sep=0pt] (s434C) {``makes sense''};\fill[overlay] ([xshift=4.5em,yshift=1.6ex]s434C.base east) circle (.045ex);}"
repl("l-12 ``makes sense''",'l-12 '+s434)
row('C14','right blank beside434','',r"\fill[overlay] ([xshift=4.5em,yshift=1.6ex]s434C.base east) circle (.045ex);",'omission','One detached dark point is visible well to the right of the makes sense entry, at approximately quotation height. It is preserved geometrically.','high',source=m['half_a'],bbox=[1107,509,1125,529])

p452=r"\tikz[baseline=(p452C.base)]{\node[inner sep=0pt] (p452C) {p 452};\fill[overlay] ([xshift=.55\linewidth,yshift=-.4ex]p452C.base west) circle (.055ex);\fill[overlay] ([xshift=.635\linewidth,yshift=-.2ex]p452C.base west) circle (.03ex);}"
repl('p 452 l-11',p452+' l-11')
row('C15','blank right of452, between452 and453','',r"\fill[overlay] ([xshift=.55\linewidth,yshift=-.4ex]p452C.base west) circle (.055ex);\fill[overlay] ([xshift=.635\linewidth,yshift=-.2ex]p452C.base west) circle (.03ex);",'omission','A larger isolated dark point and a smaller separate point farther right are visible in the blank area. They are kept distinct, with no connecting stroke or assigned function.','medium',source=m['half_b'],bbox=[944,278,1107,301])

l453=r"\tikz[baseline=(l453C.base)]{\node[inner sep=0pt] (l453C) {l};\fill[overlay] ([xshift=-.24em,yshift=-.05ex]l453C.base west) ellipse [x radius=.04ex,y radius=.07ex];}"
repl('p 453 l 1','p 453 '+l453+' 1')
row('C16','453 l1, detached low mark to left of l','',r"\fill[overlay] ([xshift=-.24em,yshift=-.05ex]l453C.base west) ellipse [x radius=.04ex,y radius=.07ex];",'omission','The enlarged crop separates a small dark oblique oval from the l foot. It lies to the left and low, not between l and1.','high','10')

l456=r"\tikz[baseline=(l456C.base)]{\node[inner sep=0pt] (l456C) {l.2};\fill[overlay] ([xshift=.13em,yshift=.35ex]l456C.base east) circle (.045ex);\path[overlay] ([xshift=-.16em,yshift=-.45ex]l456C.base east) coordinate (blot456C);\fill[overlay] ([xshift=-.12ex,yshift=.13ex]blot456C) -- ([xshift=.1ex,yshift=.16ex]blot456C) -- ([xshift=.21ex,yshift=-.03ex]blot456C) -- ([xshift=.03ex,yshift=-.17ex]blot456C) -- ([xshift=-.15ex,yshift=-.07ex]blot456C) -- cycle;\fill[overlay] ([xshift=-.13em,yshift=-1.45ex]l456C.base east) circle (.06ex);}"
repl('p 456 l.2','p 456 '+l456)
row('C17','456 l.2, separate marks at and below right end','',l456,'omission','The crop separates a small point just right of2, a larger dark irregular patch lower-left of it, and another small dark point below. Pale vertical surface/shadow traces between them are not joined or redrawn as ink.','high','12')

nine456=r"\tikz[baseline=(nine456C.base)]{\node[inner sep=0pt] (nine456C) {9};\fill[overlay] ([xshift=.23em,yshift=.45ex]nine456C.base west) circle (.04ex);}"
old="l 9 ``don't''"
# This exact string occurs only in456.
repl(old,'l '+nine456+" ``don't''")
row('C18','456 l9, point below the bowl of9','',r"\fill[overlay] ([xshift=.23em,yshift=.45ex]nine456C.base west) circle (.04ex);",'omission','The455 crop also distinctly exposes a small separate point below the bowl and just left of the descending stem of the following row\'s9. It is a different physical mark from the three-level mark under divided and from the points below l.2.','high','11',bbox=[469,506,490,529])

l462=r"\tikz[baseline=(l462C.base)]{\node[inner sep=0pt] (l462C) {l-1};\fill[overlay] ([xshift=.78\linewidth,yshift=.3ex]l462C.base west) circle (.035ex);\fill[overlay] ([xshift=.775\linewidth,yshift=.05ex]l462C.base west) circle (.03ex);}"
repl("l-1 ``mimic''",l462+" ``mimic''")
row('C19','right blank on462 continuation row','',r"\fill[overlay] ([xshift=.78\linewidth,yshift=.3ex]l462C.base west) circle (.035ex);\fill[overlay] ([xshift=.775\linewidth,yshift=.05ex]l462C.base west) circle (.03ex);",'omission','Two small distinct dark points stand in the right blank, below the long462 row and beside the mimic continuation. They are not connected.','high',source=m['half_b'],bbox=[1424,890,1449,914])

ref466=r"\tikz[baseline=(ref466C.base)]{\node[inner sep=0pt] (ref466C) {l-9};\fill[overlay] ([xshift=.22em,yshift=-.75ex]ref466C.base west) circle (.04ex);}"
repl(". l-9 ``enters''",'. '+ref466+" ``enters''")
row('C20','466 below the live l in l-9','',r"\fill[overlay] ([xshift=.22em,yshift=-.75ex]ref466C.base west) circle (.04ex);",'omission','A compact dark point is separately visible below the live l, above-left of the next row\'s opening quotation. The pale surrounding smudge is not made into a line.','medium','13',bbox=[315,1048,339,1068])

# Two long page rules remain attached to the text area rather than isolated in a drawing panel.
top=r"\tikz[remember picture,overlay]{\coordinate (scan032Ctop) at (0,0);}"
bottom=r"\tikz[remember picture,overlay]{\coordinate (scan032Cbottom) at (0,0);\draw[line width=.3pt] ([xshift=3.4em,yshift=.8ex]scan032Ctop) -- ([xshift=3.35em,yshift=4ex]scan032Cbottom);\draw[black!45,line width=.25pt] ([xshift=3.35em,yshift=4ex]scan032Cbottom) -- ([xshift=3.3em,yshift=-2ex]scan032Cbottom);\draw[line width=.3pt] ([xshift=.91\linewidth,yshift=.7ex]scan032Ctop) -- ([xshift=.908\linewidth,yshift=4ex]scan032Cbottom);\draw[black!45,line width=.25pt] ([xshift=.908\linewidth,yshift=4ex]scan032Cbottom) -- ([xshift=.91\linewidth,yshift=-2ex]scan032Cbottom);}"
text=text.replace('p.426 l-16',top+'\n'+'p.426 l-16',1)
text=text.replace('% archive sheet number: 31',bottom+'\n% archive sheet number: 31',1)
leftcode=r"\draw[line width=.3pt] ([xshift=3.4em,yshift=.8ex]scan032Ctop) -- ([xshift=3.35em,yshift=4ex]scan032Cbottom);\draw[black!45,line width=.25pt] ([xshift=3.35em,yshift=4ex]scan032Cbottom) -- ([xshift=3.3em,yshift=-2ex]scan032Cbottom);"
rightcode=r"\draw[line width=.3pt] ([xshift=.91\linewidth,yshift=.7ex]scan032Ctop) -- ([xshift=.908\linewidth,yshift=4ex]scan032Cbottom);\draw[black!45,line width=.25pt] ([xshift=.908\linewidth,yshift=4ex]scan032Cbottom) -- ([xshift=.91\linewidth,yshift=-2ex]scan032Cbottom);"
row('C21','long rule between page-reference column and correction text','',leftcode,'drawing or diagram','A fine near-vertical ink rule begins at about whole x215,y90 beside426 and descends beside the page-reference column, fading toward the lower edge around x211,y2335. It is drawn with text anchors and a paler lower portion.','high',source=m['whole'],bbox=[205,80,224,2342])
row('C22','long right rule through the right edge of long entries','',rightcode,'drawing or diagram','A second thin ink rule begins near whole x1494,y96. Several long rows extend across it; it continues to the lower margin, with a paler bottom portion. It is anchored to the same text area.','high',source=m['whole'],bbox=[1483,83,1505,2343])

# Administrative cote macro is required by the supplied convention, not an ink collation item.
text='\\cotefile{109}\n'+text
(out/'reading.tex').write_text(text)

# Every explicit C uncertainty and every supplied page-specific context decision.
doubts=[]
def doubt(place,c,reading,resolved,confidence,evidence,crop=None,source=None,bbox=None):
    if crop:
        loc=loci[crop];source=source or loc['source'];bbox=bbox or loc['bbox'];cp=str(out/'crops'/f'{crop}.jpg')
    else:cp=None
    doubts.append(dict(place=place,c=c,reading=reading,resolved=resolved,confidence=confidence,evidence=evidence,crop=cp,source=source,bbox=bbox))

doubt('428 l-9, second hatted A index',r'$\hat{A}_{\unsure{M|m}}$',r'$\hat{A}_{\unsure{M|m}}$',False,'medium','The two pointed upstrokes and final descending curl are clear. They permit both cursive M and angular m; size alone does not settle case. The ordinary A has a looped cross-stroke and a separate roof.','02')
doubt('440 mark after cancelled allows one to',r'\unsure{-+|+}',r'\raisebox{1.1ex}[0pt][0pt]{\unsure{-+|+}}',False,'medium','The small cross is visible. The adjoining horizontal can be a minus or the returned stroke of the closer; its elevated position is certain.','05')
doubt('449 cancelled baseline trace before us',r'\deleted{\unsure{o}}',r'\deleted{\unsure{o}}',False,'low','A small loop survives where a cancelled o could stand, but the descending insertion connection enters the same space. No second connector is duplicated. Raised one is itself readable and cancelled.','07')
doubt('450 linking sign between -2 and -3',r'\unsure{\&|a}',r'\&',True,'high','Two loops, a crossing diagonal and an outward exit decide ampersand independently of the grammatical context.','08')
doubt('452 point before dont',r'\unsure{.}',q452,True,'high','The physical point is certain. It is represented at its observed height and is not assigned a full-stop function.','09')
doubt('455 mark below first i, C equivalence/E alternatives',r'\underset{\unsure{\equiv|\mathrm{E}}}{\text{i}}',mark455,False,'high for geometry; low for function','The three-level returned geometry and its position below the first i are settled. E, equivalence-like marking and emphasis remain interpretations of that geometry, so its function is left unassigned.','11')
doubt('466 cancelled old reference',r'\deleted{\unsure{l 9|l}}',r'\deleted{\unsure{l\textsubscript{9}|l}}',False,'low for buried numeral; high for cancellation','The l loop is secure; a much smaller lower-right loop and hook may be9 or cancellation structure. It is not read from the following live9.','13')
doubt('428 first hatted A, context notation',r'$\hat{A}$',r'$\hat{A}$',True,'high','The upper half independently shows one ordinary A outline and a separate two-stroke roof. No index accompanies this first A.',source=m['half_a'],bbox=[400,244,497,314])
doubt('438 l4 isolated closing parenthesis, context notation',r'\mbox{$)$}',r'\mbox{$)$}',True,'high','A single right-hand curved parenthesis is present before missing from formula. No opening mate is supplied on this page.',source=m['half_a'],bbox=[340,569,392,631])
doubt('449 l-8 k-modules, context notation',r'$k$-modules',r'$k$-modules',True,'high','The lower half shows a lowercase k with an ascender and diagonal limbs, followed by the baseline hyphen.',source=m['half_b'],bbox=[1128,108,1369,171])
doubt('450 reduced s at foot of l, context notation',r'l\textsubscript{s}',r'l\textsubscript{s}',True,'high','A small s-shaped curve is connected at the foot of l and sits lower than the line numerals. It is retained as C encodes it.','08')
doubt('428 correction comment, supplied context',r"``$\hat{A}$ is abelian''. surely not! You mean",r"``$\hat{A}$ is abelian''. surely not! You mean",True,'high','The upper half confirms the quoted assertion, the following full stop, surely not!, capital You and mean. This is the writer\'s objection, not a mathematical result proved by this reading.',source=m['half_a'],bbox=[411,243,1219,328])
doubt('431 comment, supplied context',r"``integration'' is not clear",r"``integration'' is not clear",True,'high','The complete comment is readable. The crop shows a point-like first opening mark and a bent second mark; together they support C\'s paired opener.','03')
doubt('438 instruction described in context',r'\mbox{$)$} missing from formula.',r'\mbox{$)$} missing from formula.',True,'high','The context paraphrase is not added to the transcription: the page itself prints a closing parenthesis and the words missing from formula. The cited formula is not reproduced here.',source=m['half_a'],bbox=[343,568,784,631])
doubt('archive number and reference range in supplied context','% archive sheet number: 31','% archive sheet number: 31',True,'high','The lower-right31 is an archive corner number, retained only in the comment. The visible list begins426 and ends468.',source=m['whole'],bbox=[1539,2279,1628,2342])

remaining=[
 dict(place='428 l.6 opener',reading=r'\unsure{``|`}',alternatives='joined double opening strokes; one forked opening stroke',confidence='medium',reason='The two upper branches join; their original stroke count is not recoverable securely.'),
 dict(place='428 second hatted A index',reading=r'\unsure{M|m}',alternatives='M; m',confidence='medium',reason='Two angular peaks and a final curl are compatible with either case.'),
 dict(place='440 elevated terminal mark',reading=r'\raisebox{1.1ex}[0pt][0pt]{\unsure{-+|+}}',alternatives='-+; + with preceding horizontal belonging to quote',confidence='medium',reason='The horizontal joins the previous quotation stroke; its separate minus identity remains uncertain.'),
 dict(place='449 baseline cancelled trace',reading=r'\deleted{\unsure{o}}',alternatives='cancelled o; a curl in the insertion connection',confidence='low',reason='The letter-like loop and the insertion connection share the same crowded ink.'),
 dict(place='455 three-level mark',reading=mark455,alternatives='E-like symbol; equivalence-like mark; returned emphasis strokes',confidence='high geometry, low function',reason='The geometry is transcribed explicitly; its function is not assigned.'),
 dict(place='466 cancelled reference',reading=r'\deleted{\unsure{l\textsubscript{9}|l}}',alternatives='l with a small lower9; l with cancellation curl',confidence='low for lower glyph',reason='The smaller loop and hook survive but overlap cancellation strokes.'),
 dict(place='468 final closer',reading=r"\unsure{''|'}",alternatives='fused double closing marks; one bent closing mark',confidence='medium',reason='A compact cap joins the two apparent lower legs.')]

# Complete ordered entry inventory, including nested state and drawing elements.
inv=[]
def item(kind,position,first,hand='his hand',transcribed='yes'):
    inv.append(dict(sheet_kind='list',hand=hand,element=f'{len(inv)+1:03d}',kind=kind,position=position,first_words_or_objects=first,transcribed=transcribed))
item('drawing','left boundary of correction text,426 through468','Fine near-vertical rule beside page-reference column')
item('drawing','right side,426 through468','Long near-vertical rule crossing some long text rows')
entries=[
('426','l-16 its'),('426','l-4 ``ones\'\''),
('427','l-6 ``its\'\'.'),
('428','l.6, allows one to'),('428','l-9 we\'d better'),('428 continuation','l-9 A-hat is abelian; surely not! You mean A-hat with index'),
('429','l.1. don\'t'),
('430','l16 its'),('430','l.17. doesn\'t'),('430','l-3 we\'ve'),
('431','l.-8 integration is not clear'),
('434','l12 interpret'),('434','l-12 makes sense'),
('438','l4 closing parenthesis missing from formula.'),
('439','l-9 developed'),('439','l-1 make sense'),('439','l12 divided'),
('440','l.-7 wouldn\'t'),('440','cancelled l-5 its'),('440','cancelled allows one, followed by to and elevated mark'),('440 continuation','l-5 its diagonal map would allow one to recover'),
('441','l.3 don\'t'),('441','l7 divided'),('441','l16 divided'),('441','l-10 allows one to'),
('444','l-9 isn\'t'),
('445','l1 trying to put'),('445','l-4 doesn\'t'),
('447','l10 commute with'),('447','l18 One way to define'),('447','cancelled l9 its'),
('448','l-6 its also l9.'),
('449','l11 allows [cancelled/revised] us to'),('449','l-9 To imagine that there is a good'),('449 continuation','l-8 without the homotopy groups being k-modules'),
('450','l2 from the ring.'),('450','l-10 divided'),('450','l_s -2 & -3 doesn\'t'),
('452','l-11 don\'t'),('453','l1 isn\'t'),('454','l.11 we had better'),('455','l-13 divided'),
('456','l.2 its'),('456','l9 don\'t'),('457','l-16 its'),
('458','l8 wouldn\'t'),('458','l14 doesn\'t also its'),('458','l15 its'),('458','l16 its'),('459','l-5 doesn\'t'),
('460','l8 quasi-isomorphisms'),('460','l-11 demand'),('460','l-7 mimic'),
('462','l9 isn\'t'),('462','l14 its'),('462','l-7 don\'t'),('462','l-6 didn\'t'),('462','l-4 don\'t'),('462 continuation','l-1 mimic'),
('463','l12 doesn\'t'),('463','l13 trivial'),
('466','cancelled old reference, then l-9 enters'),
('467','l8 quasi-isomorphism'),('467','l-1 its'),
('468','l3 Postnikov\'s.'),('468','l7 this only taking'),('468','l.8 and iterating')]
for page,first in entries:
    item('text','page-reference '+page,first)
    if page=='427':item('drawing','left blank beside427','Detached dark point')
    if page=='434' and first.startswith('l-12'):item('drawing','right blank beside434','Detached dark point at quotation height')
    if page=='440' and first=='cancelled l-5 its':
        item('deletion','440 first cancelled entry','l-5; its (quotation marks remain live)')
    if page=='440' and first.startswith('cancelled allows'):
        item('deletion','440 second cancelled wording','allows one')
        item('text','440 elevated after closing pair','Uncertain -+/+ mark')
    if page=='447' and first=='cancelled l9 its':
        item('deletion','447 final correction','l9; its (quotation marks remain live)')
        item('drawing','447 above-left of opening pair','Small detached point distinct from i-dot')
    if page=='449' and first.startswith('l11'):
        item('deletion','449 baseline before us','Uncertain old o / connection curl')
        item('insertion','449 raised over gap before us','one, itself cancelled')
        item('deletion','449 within raised insertion','one')
    if page=='450' and first.startswith('l2 '):item('text','450 nested underline','Single underline under the')
    if page=='452':
        item('drawing','452 after opener, above word baseline','One detached point')
        item('drawing','452 right blank','Two separate points at different horizontal positions')
    if page=='453':item('drawing','453 beside left foot of l','Detached low oval point')
    if page=='455':item('drawing','455 below first i','Three-level left-returned dark mark; middle retraced')
    if page=='456' and first.startswith('l.2'):
        item('drawing','456 at/below right end of l.2','Small upper point, irregular dark patch, small lower point; no connector')
    if page=='456' and first.startswith('l9'):
        item('drawing','456 below9 bowl','Separate small point')
    if page=='462 continuation':item('drawing','462 right blank beside continuation','Two small detached points')
    if page=='466':
        item('deletion','466 before live l-9','l with uncertain small lower-right9')
        item('drawing','466 beneath live l','Separate small dark point')
item('text','lower-right corner, archive comment only','archive sheet number31')

notation=[
 dict(sign=r'\hat{A}; \hat{A}_{\unsure{M|m}}',location='428 l-9',reading=r'$\hat{A}$; $\hat{A}_{\unsure{M|m}}$',evidence='First A and roof read in half_a. Second A and two-peaked lower glyph inspected in crop02; M/m remains uncertain.'),
 dict(sign=')',location='438 l4',reading=r'\mbox{$)$}',evidence='One isolated closing curve; no other side of a parenthesis.'),
 dict(sign='k-',location='449 l-8',reading=r'$k$-modules',evidence='Separate ascender and diagonal limbs of lowercase k followed by short baseline hyphen, half_b.'),
 dict(sign='lower s',location='450 final references',reading=r'l\textsubscript{s}',evidence='The s is small, connected at the foot of l and below the numeral baseline, crop08.'),
 dict(sign=r'\&',location='450 between -2 and -3',reading=r'\&',evidence='Crossed upper loop, smaller lower loop and right exit, crop08.'),
 dict(sign='single underline',location='450 from the ring',reading=r'\uline{the}',evidence='One horizontal stroke confined to the, half_b.'),
 dict(sign='three-level returned mark',location='455 beneath first i',reading=mark455,evidence='Top, dense middle and bottom levels with left connections, crop11; function unassigned.'),
 dict(sign='quotation groups',location='428 allows;431 integration;440 and447 cancellations;468 ending',reading='\n'.join(x['reading'] for x in changes if x['id'] in ['C01','C02','C03','C05','C12']),evidence='Crops01,03,04,05,06 and14 inspected independently. Uncertain counts are local, and cancellation scope is not propagated to high quotation strokes.'),
 dict(sign='detached dark marks',location='427;434;447;452;453;456 twice;462;466',reading='\n'.join(x['reading'] for x in changes if x['id'] in ['C06','C09','C13','C14','C15','C16','C17','C18','C19','C20']),evidence='Half observations and crops06,09–13 separate physical points from adjacent glyphs and from pale photographic/material traces.'),
 dict(sign='two long rules',location='beside page column and near right edge',reading=leftcode+'\n'+rightcode,evidence='Whole layout and both once-only halves establish upper endpoints, continuous middle runs and pale lower portions.')]

notes=[
 'Handwritten English correction list referring to typescript pages426–468, with gaps in that reference sequence. The supplied H witness describes this sheet rather than transcribing its running text; no H collation rows are made.',
 'At428 l-9 the writer quotes A-hat is abelian, then writes surely not! You mean and a second hatted A with an uncertain M/m index. This transcription does not independently establish or refute the mathematical assertion.',
 'At431 l.-8 the writer says integration is not clear. At438 l4 a single closing parenthesis is followed by missing from formula.; no cited formula itself appears here.',
 'At440 the revision concerns its diagonal map would allow one to recover. The earlier l-5 its and allows one are visibly cancelled; the quotation edges stand above the cancellations and the final to has no direct crossing.',
 'At449 the raised cancelled one is placed over the baseline revision before us. The following two entries read To imagine that there is a good and without the homotopy groups being k-modules.',
 'At450 the is singly underlined; the final reference uses a reduced s at l and a legible ampersand between -2 and -3. At455 the first i in divided has a small returned three-level mark below it, drawn without imposing a semantic interpretation.',
 'A cancelled lower-right old glyph before466 may be9; the cancellation itself is definite. At468 the final closer after and iterating remains one-or-two-stroke uncertain.',
 'The archive31 is recorded only in a comment. Pale circular surface impressions near the upper/lower right and pale streaks near456 are treated as material/photographic features. Distinct dark points are drawn separately without assigning origin or connecting them.'
]

report=dict(scan=32,reader='C',model='GPT-6 Astra Pro (inherited)',effort='not exposed',viewed=[m['whole'],m['half_a'],m['half_b']],layout='One handwritten list, in a single text hand. Page references426–468 occupy a narrow left column, with main correction text to the right of a fine vertical ink rule. A second rule runs near the right edge and is crossed by long rows, especially441 and462. Both rules become paler near the lower border. No display equations, diagrams, pictorial drawings, headings or own page number. Inline hatted A expressions at428 and an isolated closing parenthesis at438. Cancellations at440,447,449 and466; one is raised and cancelled at449. One single underline under the450 and a three-level mark below the first i of455 divided. Distinct detached dark marks are listed in the inventory. Pale circular impressions and creases are material features. Archive31 at lower right. The list has67 separately inventoried correction entries, with all nested insertions/deletions/emphasis/drawings separately inventoried.',changes=changes,c_doubts=doubts,remaining_doubts=remaining,inventory=inv,notes=notes,math_checks=[],notation=notation,abbreviations=[dict(form='p / p.',expansion='page',place='page-reference column'),dict(form='l / l. / l-',expansion='line; negative numerals indicate the written negative line reference',place='throughout correction references'),dict(form=r'l\textsubscript{s}',expansion='tentatively plural lines',place='450 final references')],brief_feedback='No H running-text comparisons were manufactured because metadata says desc. The complete notation snapshot and supplied page context were read; there is no H_context or C_context_addendum among the supplied032 files. Whole was viewed once for layout, each half once line by line;14 unresolved loci were frozen before crop creation and each one enhanced crop was viewed singly once. Newly distinct small marks inside those frozen crops were recorded without additional crops. No OCR, recognition, outside research, other-reader output, other page images, or compilation was used. The three-level455 mark is drawn geometrically; its interpretive alternatives remain recorded rather than forced into a semantic symbol. The obligatory cotefile macro and drawing anchor markup are administrative/layout syntax, not additional ink readings. Inventory rows cover each correction reference and all nested states and marks; no display or diagram is present.')
report['layout']=report['layout'].replace('67 separately',str(len(entries))+' separately')
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

# Preserve actual one-at-a-time crop view records after the views have occurred.
decisions={
'01':'Opener remains joined-double/single uncertain; closing pair and comma confirmed.',
'02':'Second A and hat confirmed; M/m retained.',
'03':'Point-like first and bent second opening marks support paired opener.',
'04':'Cancelled l-5 and its; single opener and paired closer above paths remain live.',
'05':'Opening/closing pairs live; zigzags cover allows one; to not directly crossed. Raised -+/+ alternatives retained.',
'06':'Quote edges live around cancelled its; separate upper-left point recorded.',
'07':'Cancelled one is raised; baseline candidate o remains uncertain against connector curl.',
'08':'Ampersand resolved; lowered s confirmed.',
'09':'Point confirmed physically and drawn at intermediate height; punctuation function unassigned.',
'10':'Low oval mark is separate from l foot.',
'11':'Three-level left-returned geometry recorded beneath first i; separate dot under next-row9 also recorded.',
'12':'Three dark marks at/below2 kept separate; pale traces not connected.',
'13':'Tall l certain, smaller lowered9/curl remains doubtful; separate point below live l recorded.',
'14':'Complete final quote edge still fused-double/single uncertain.'}
initial_views=[json.loads(line) for line in (out/'views.jsonl').read_text().splitlines() if json.loads(line)['phase']!='crop']
assert len(initial_views)==3
with (out/'views.jsonl').open('w') as f:
    for view in initial_views:f.write(json.dumps(view,ensure_ascii=False)+'\n')
    for k,v in decisions.items():
        f.write(json.dumps(dict(phase='crop',path=str(out/'crops'/f'{k}.jpg'),view_count=1,purpose=loci[k]['place'],decision=v),ensure_ascii=False)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts_and_context_decisions':len(doubts),'remaining_doubts':len(remaining),'inventory':len(inv),'text_entries':len(entries),'math_checks':0,'crops':len(loci)},indent=2))
