from pathlib import Path
import json, datetime, re
ROOT=Path('/workspace/scratch/4770596940a0')
OUT=ROOT/'out/readers/R3'
Cpath=ROOT/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan032.tex'
Hpath=ROOT/'working/H/scan032.tex'
tex=r'''\scanpage{32}\mspage{31}
% @ top, continuation lines 1–3
Si $A\in F\setminus G$, $A\cap B$ est réunion de strates de $F$. \deleted{Reste} reste à voir que une strate \inserted{\unsure{$G$|$\in$}} de $F$ est réunion de strates de $F'$. Soit $A$ cette strate de $F$. \deleted{\unsure{On}}
% @ top, cancelled union; the lower limit is literally F
\[
 \deleted{A=\bigcup_{\substack{B\in F\\B\leq F}}B^\circ}
\]
% @ upper part, two cases; both first-case G primes are visible
Si $A\notin G'$, alors $A\in F\setminus G'\subset F'$, et on gagne. Si $A\in G$, alors (comme $G'\preceq G$) $A$ est réunion de strates de $G'$, qui sont des strates de $F'$, et on gagne encore.

% @ left beside corollary
% slanted
\margin{Ultra faux}
% @ upper middle, corollary heading
\uline{Corollaire} Le \deleted{raffinement}\inserted{subdivision} précédente $F'$ de $F$ est caractérisée par \inserted{chacune} des propriétés équivalentes suivantes~:

% @ centre, condition a), cancelled by a large cross
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,inner sep=0pt,text width=13.2cm,align=left] (conditiona) at (0,0) {\deleted{a) Pour toute subdivision $F''$ de $F$ qui induit $G'$ sur $G$, on a $F''\preceq F'$ -- i.e. $F'$ est \deleted{\uline{maximal}}\inserted{un plus grand \unsure{élémt|élément|élt}}, pour $\preceq^{*}$, dans l'ens des subdivisions de $F$ qui induisent $G'$ sur $G$.}};
\draw[line width=.5pt] ([xshift=4.2cm,yshift=.3cm]conditiona.north west) -- ([xshift=-4.0cm,yshift=-.25cm]conditiona.south east);
\draw[line width=.5pt] ([xshift=4.2cm,yshift=-.25cm]conditiona.south west) -- ([xshift=-3.6cm,yshift=.1cm]conditiona.north east);
\end{tikzpicture}}
% @ within the crossed a), below qui: isolated angular pen mark.
% Identity unresolved (E / membership-like mark); these strokes are not assigned a textual role.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.7pt] (0,.48) -- (.02,.03) .. controls (.10,-.02) and (.22,.01) .. (.42,.02);
\draw[line width=.65pt] (.13,.16) .. controls (.25,.22) and (.34,.22) .. (.47,.20);
\draw[gray,line width=.3pt] (.08,.47) .. controls (.21,.50) and (.35,.48) .. (.43,.44);
\draw[line width=.5pt] (.37,.73) -- (.43,.57);
\end{tikzpicture}}
% @ left of a), starred gloss
% slanted
\margin{$*$ ou pour $\ll$, cela revient au $=$ parmi des subdivisions d'une $=$ $F$}
% @ centre left, long oblique note. A transverse curved stroke crosses the full note.
% Its cancellation function is probable but uncertain; the stroke is reproduced without asserting an unambiguous whole-note deletion.
% slanted
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,inner sep=0pt,text width=5.0cm,align=left,font=\footnotesize] (longnote) at (0,0) {les conditions \deleted{\unsure{a)}} b) c) d) sont équivalentes, \unsure{et} \uline{impliquées} par a), lesquelles \unsure{caractérisent|caractérise} la subdivision construite précédemment. Mais ces trois \unsure{cond.} (b,c,d) sont \unsure{loin} d'impliquer a)};
\draw[line width=.45pt] ([xshift=2.45cm,yshift=.1cm]longnote.north west) .. controls (1.85,-.70) and (1.45,-.85) .. (1.65,-1.20) .. controls (1.95,-1.55) and (.65,-2.20) .. ([xshift=1.0cm,yshift=-.05cm]longnote.south west);
\end{tikzpicture}}}
% @ lower middle, condition b)
b) L'application can. associée à $F'\preceq F$
\[
 \varphi:F'\longrightarrow F
\]
induit une bijection
\[
 F'\setminus G'\xrightarrow{\sim}F\setminus G.
\]
% @ right, NB with a vertical left rule
\margin{\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt,text width=4.4cm,align=left,font=\footnotesize] (nb) at (0,0) {NB. c'est \unsure{tjrs|tojrs} surj. donc c'est l'\uline{injectivité} qu'il faut prouver ici};
\draw[line width=.4pt] ([xshift=-.13cm]nb.north west) -- ([xshift=-.13cm]nb.south west);
\end{tikzpicture}}}
% @ lower part, condition c), cancelled draft and interlinear replacement
c) \deleted{Les strates ouvertes de $F'$ qui ne sont} \inserted{$\forall A\in F\setminus G$, $A^\circ$ est une strate ouverte de $F'$.}
% @ lower part, condition d)
d) $F'\supset F\setminus G$, i.e. $\forall A\in F\setminus G$, on a $A\in F'$.

% @ foot, proof heading: one live On; no separate cancelled On is visible
\uline{Dém} On va prouver p. ex
\[
 \text{d)}\Longrightarrow\text{b)}\Longrightarrow\text{c)}\Longrightarrow\text{a)}\Longrightarrow\text{d)}
\]
% @ bottom, first implication and overwritten identity / inclusion
\deleted{\uline{Dém}} $\text{d)}\Rightarrow\text{b)}$ Si $(F\setminus G)\subset F'$, alors $\varphi\mid F\setminus G$ est l'\deleted{\unsure{identité}}\unsure{inclusion} \deleted{(trivial)} \inserted{can. $F\setminus G\hookrightarrow F$}, \deleted{donc} donc il reste à prouver
\[
 F\setminus G=F'\setminus G'.
\]
'''
(OUT/'scan032.tex').write_text(tex)
D=[]
def add(id,place,C,H,reading,ink,confidence,kind,crop,ac=False,ah=False,mh=False):
 D.append(dict(id=id,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,kind=kind,crop=crop,against_C=ac,against_H=ah,marked_in_H=mh))
add('D01','top, first F',r'\unsure{F|\mathcal F}','F','F','Upright stem and short bars; the top curl is not sufficient evidence of a separate script alphabet.','medium','other','top',True)
add('D02','top, cancelled Reste',r'\deleted{\unsure{Reste}}','struck Reste','deleted Reste','Tall initial R and the remaining small letter sequence survive the horizontal stroke.','medium','other','top',True)
add('D03','top, live continuation','reste à voir que une',"Reste : voir qu'une",'reste à voir que une','Lowercase initial, accented à, and separately written que une; neither colon nor apostrophe is visible.','high','misread word','top',False,True)
add('D04','top, insertion after strate',r'\inserted{\unsure{G|in}}','added de G',r'\inserted{\unsure{G|\in}}','One raised curved glyph with horizontal middle and lower strokes; its top meets the tail of réunion above. No separate de is inserted.','low','insertion or placement','top_insertion',False,True)
add('D05','top, cancelled On',r'\deleted{\unsure{On}}','struck On',r'\deleted{\unsure{On}}','Open round initial and low final stroke under cancellation; On remains plausible but not secure.','medium','other','top',False,False)
add('D06','first case, nonmembership',"A\\notin G'",'A notin G',"A\\notin G'",'A separate high prime follows G.','high','misread symbol or index','cases',False,True)
add('D07','first case, complement',"F\\setminus G'\\subset F'","F setminus G subset F'", "F\\setminus G'\\subset F'",'G carries a high prime; F at the right also carries its own prime. The inclusion has no lower equality bar.','high','misread symbol or index','cases',False,True)
add('D08','end of second case','et on gagne encore','et on a gagné encore','et on gagne encore','One low on followed directly by gagne; no separate a or accent over final e.','high','text not on the page','cases',False,True)
add('D09','left, short oblique note',r'\unsure{Ultra} faux','Ultra faux','Ultra faux','Rotated: opening U, two tall narrow ascenders and low terminal ra; faux follows.','medium','other','ultra',True)
add('D10','corollary article',r'\unsure{Le|La}','La','Le','Tall L ends in a low e loop and horizontal exit, not a rounded a bowl. Grammar of the inserted noun was not used to choose.','high','misread word','corollary',True,True)
add('D11','Corollaire heading',r'\uline{Corollaire}','bold Corollaire',r'\uline{Corollaire}','A single underline runs under the whole heading.','high','other','corollary',False,True)
add('D12','corollary, insertion before des','inserted chacune des','added des','inserted chacune des','Raised/small chacune is distinct from the following main-line des; the first syllable begins ch and ends with the low une sequence.','high','omission','corollary',False,True)
add('D13','a), qui induit','qui induit','qui induise','qui induit','Final tall crossed t, with no further se sequence.','high','misread word','condition_a',False,True)
add('D14','a), overall cancellation','whole a) deleted, no drawn cross','text a) with note that large cross cancels it','whole a) cancelled; large X reproduced in TikZ','Two long diagonals cross the entire condition, distinct from local cancellation of maximal.','high','drawing or diagram','condition_a',True,True)
add('D15','a), inserted noun',r'\unsure{élémt|élément|élt}','élément',r'\unsure{élémt|élément|élt}','Small initial accent-like stroke, tall l and flattened middle run, with a raised final t-like triangular stroke. The crossing diagonal prevents a confident full-versus-abbreviated resolution.','medium','abbreviation expanded or spelling modernised','a_noun',False,True)
add('D16','a), local replacement order','deleted underlined maximal; inserted un plus grand ...','inserted un plus grand élément; struck maximal','deleted underlined maximal; inserted un plus grand ...','Replacement is above maximal, whose main-line letters are struck and whose underline remains.','high','insertion or placement','condition_a',False,True)
add('D17','a), comma after local replacement','no comma','comma after maximal','comma retained after replacement group','A separate descending comma is visible after the cancelled main-line word and before pour.','high','omission','condition_a',True,False)
add('D18','a), abbreviation ens',"l'ens", "l'ens.","l'ens",'No separate full stop is distinguishable after the final s before the line break.','medium','other','condition_a',False,True)
add('D19','a), below qui','omitted','omitted','unassigned angular pen mark drawn in TikZ','Left vertical joins the heavy bottom bar; shorter separate middle bar, faint top bar and detached short upper stroke. E/membership-like, without secure textual role.','low','drawing or diagram','angular_mark',True,True)
add('D20','starred note, subject','cela revient','il revient','cela revient','After rotation, c plus connected e/l/a strokes precede revient.','high','misread word','star_note',False,True)
add('D21','starred note, first shorthand','au =','au même','au =','Two short approximately parallel strokes, not the written word même.','high','abbreviation expanded or spelling modernised','star_note',False,True)
add('D22','starred note, parmi/pour',r'\unsure{parmi|pour}','pour','parmi','p descender followed by several small strokes and an i dot; longer than the nearby pour.','high','misread word','star_note',True,True)
add('D23','starred note, final phrase',"d'une = F","d'un même F","d'une = F",'The article has a final low e; the following equality-like shorthand is two strokes.','high','abbreviation expanded or spelling modernised','star_note',False,True)
add('D24','long note, cancelled initial a)',r'\deleted{\unsure{a)}}','omitted',r'\deleted{\unsure{a)}}','An angular compact blackened group precedes clear b) c) d); cancellation is secure, its a) reading remains uncertain.','low','omission','note_upper',False,True)
add('D25','long note, conjunction',r'\unsure{et}','uncertain et ...',r'\unsure{et}','The two small forms at the left are crowded and overtraced; et is plausible but not fully resolved.','medium','other','note_upper',False,False,True)
add('D26','long note, implication direction',r'\uline{\unsure{impliquées}} par a)','uncertain équivalentes à a)',r'\uline{impliquées} par a)','The i and p/l ascenders, descending q, and underline are visible; a separate par follows. This is not a repetition of équivalentes.','medium','misread word','note_upper',True,True,True)
add('D27','long note, relative pronoun',r'\unsure{lesquelles|laquelle}','uncertain lesquelles','lesquelles','Readable le-, q descender, two l loops and final low es; the end is plural-shaped.','medium','other','note_lower',True,False,True)
add('D28','long note, verb',r'\unsure{caractérisent|caractérise}','conditions and illegible span',r'\unsure{caractérisent|caractérise}','Initial carac-/téri- sequence is visible, but the final run meets larger main-text strokes. Singular/plural ending retained.','medium','readable ink left as \\ill{}','note_lower',False,True,True)
add('D29','long note, prior construction',r'la subdivision construite \unsure{précédemment}','subdivision construite followed by #','la subdivision construite précédemment','The long following word begins pré-, shows céd- and a repeated low run ending in a raised t. The raised crossing is part of the word, not a # reference.','medium','omission','note_complete_tail',True,True,False)
add('D30','long note, Mais ces trois','Mais ces trois','Mais c) très','Mais ces trois','Mais has its tall M, ces its small e/s sequence, and trois begins with a crossed t. Main-text c) is a separate overlapping object.','medium','misread word','note_complete_tail',False,True)
add('D31','long note, cond.',r'\unsure{cond.}','illegible',r'\unsure{cond.}','Short c-initial run after trois is partly over main text; ending/dot not secure enough to remove doubt.','medium','readable ink left as \\ill{}','note_complete_tail',False,True,True)
add('D32','long note, loin',r'\unsure{loin}','illegible',r'\unsure{loin}','Thin lower-letter run crosses the main arrow area; reading loin remains plausible but incompletely separated from the other ink.','low','readable ink left as \\ill{}','note_complete_tail',False,True,True)
add('D33','long note, final assertion','(b,c,d) sont ... d’impliquer a)','(b,c,d), rest illegible',"(b,c,d) sont \\unsure{loin} d'impliquer a)",'Parenthesized b,c,d begins the last line. The extended rotated crop captures d’, the p descender of impliquer and final a) at the upper-right source endpoint.','medium','readable ink left as \\ill{}','note_complete_tail',False,True,True)
add('D34','long note, curved transverse stroke','prose without stroke or whole-note deletion','prose; note says crossed by a curved line','full prose plus drawn transverse curve; whole-note cancellation probable but uncertain','Curve passes internally through conditions, équivalentes, impliquées, later lines and the final line; it is not a clean outer boundary. A cancellation function is plausible, not certain.','medium','drawing or diagram','long_note',True,True)
add('D35','b), can.',r'\unsure{can.}','uncertain canonique','can.','Small c, compact a/n group and a separate stop; no long -onique sequence.','high','abbreviation expanded or spelling modernised','condition_b',True,True,True)
add('D36','NB, abbreviation',r'\unsure{tjrs|tojrs}','toujours',r'\unsure{tjrs|tojrs}','t and long j descender are clear; a possible intervening small oval cannot be confidently assigned as o. Abbreviation is certain.','medium','abbreviation expanded or spelling modernised','NB',False,True)
add('D37','NB, ending and punctuation','surj. donc ... ici','surj., donc ... [no ici]','surj. donc ... ici','End of first line has a stop; no added comma. Final short ici is visible after prouver.','high','omission','NB',False,True)
add('D38','NB, left rule and emphasis','underlined injectivité, no rule','bold NB and plain injectivité, no rule','plain NB.; underlined injectivité; vertical left rule','Continuous underline below injectivité and separate vertical rule to the left of all three lines.','high','drawing or diagram','NB',True,True)
add('D39','c), cancelled draft','deleted Les strates ouvertes de F′ qui ne sont','struck illegible fragments after strate and F′','deleted Les strates ouvertes de F′ qui ne sont','One continuous lower draft is crossed through, from Les to sont; the replacement is above it. The drafts are not two later fragments.','high','deletion state (struck given live or live given struck)','c_full',False,True,True)
add('D40','c), live ouverte','une strate ouverte de F′','une strate [struck illegible] de F′','une strate ouverte de F′','ouverte is written in the upper replacement and is not crossed.','high','deletion state (struck given live or live given struck)','c_full',False,True,True)
add('D41','c), replacement placement','live replacement unmarked as inserted','live replacement unmarked as inserted','replacement wrapped as inserted above the cancelled draft','The quantified sentence is interlinear above the struck sentence, with de F′ continuing below at left.','high','insertion or placement','c_full',True,True)
add('D42','proof heading, alleged cancelled On',r'\deleted{\unsure{On}} before live On','one live On','no distinct cancelled On','A broad O entry curve returns into its inner loop and then a single n. There is no second separate word and no crossing cancellation stroke; high horizontal line is Dém’s underline.','high','text not on the page','On_heading',True,False)
add('D43','proof heading, live On',r'\unsure{On}','On','On','One large looping O followed by n, then a space before va.','high','other','On_heading',True,False)
add('D44','proof heading, p. ex',r'\unsure{p. ex}','omitted','p. ex','p descender, point and compact ex are visible after prouver.','high','omission','proof_heading',True,True)
add('D45','proof heading, emphasis/punctuation',r'\uline{Dém}','bold Dém.',r'\uline{Dém}','One underline; no separate terminal stop distinguishable.','high','other','proof_heading',False,True)
add('D46','bottom, cancelled Dém',r'\deleted{\uline{\unsure{Dém}}}','struck Dém.','deleted underlined Dém','Tall D and small following humps survive repeated oblique cancellation; separate low underline. No visible full stop.','medium','other','bottom',True,True)
add('D47','bottom, overwritten old word',r'\deleted{\unsure{identité}}','live identité',r'\deleted{\unsure{identité}}','Fainter older ascenders and -ité sequence lie beneath darker replacement strokes; exact old word stays uncertain.','medium','deletion state (struck given live or live given struck)','bottom',False,True)
add('D48','bottom, replacement word',r'\unsure{inclusion}','omitted',r'\unsure{inclusion}','Darker i/n/c/l-like sequence and low ending overlay the old word; inclusion plausible but crowded.','medium','omission','bottom',False,True)
add('D49','bottom, cancelled parenthesis','deleted (trivial)','omitted','deleted (trivial)','Parentheses and t/r/i/v/i/a/l sequence remain faintly beneath a long thin stroke.','medium','omission','bottom',False,True)
add('D50','bottom, inserted canonical map',r'\inserted{\unsure{can.} F\setminus G\hookrightarrow F}','added (car F setminus G subset F)',r'\inserted{can. F\setminus G\hookrightarrow F}',r'Small can. precedes F\G and a horizontal arrow with a hooked left entry and right arrowhead. No car or set-inclusion-only assertion.','high','misread symbol or index','bottom',True,True)
add('D51','bottom, implication punctuation','d)⇒b) Si','d)⇒b). Si','d)⇒b) Si','No independent full stop between the closing parenthesis and Si.','medium','text not on the page','bottom',False,True)
# Individual C doubt occurrences, in the order in C; refer to full evidence rows above.
refs=[('F|mathcal F','D01','resolved'),('deleted Reste','D02','resolved'),('inserted G|in','D04','retained'),('deleted On top','D05','retained'),('Ultra','D09','resolved'),('Le|La','D10','resolved'),('élémt|élément|élt','D15','retained'),('parmi|pour','D22','resolved'),('deleted a) in long note','D24','retained'),('et in long note','D25','retained'),('impliquées','D26','resolved'),('lesquelles|laquelle','D27','resolved'),('caractérisent|caractérise','D28','retained'),('précédemment','D29','resolved'),('cond.','D31','retained'),('loin','D32','retained'),('can. in b)','D35','resolved'),('tjrs|tojrs','D36','retained'),('deleted On in proof heading','D42','resolved: no separate cancelled occurrence'),('live On in proof heading','D43','resolved'),('p. ex','D44','resolved'),('deleted Dém bottom','D46','resolved'),('deleted identité','D47','retained'),('inclusion','D48','retained'),('can. in inserted map','D50','resolved')]
cd=[{'occurrence':i+1,'C':c,'decision':s,'difference_id':d} for i,(c,d,s) in enumerate(refs)]
I=[]
def inv(kind,position,first,crop):
 I.append({'id':f'I{len(I)+1:02}','kind':kind,'position':position,'first_words_or_objects':first,'crop':crop,'included_in_tex':True})
inv('page number','top centre','31','top')
inv('text block','top three lines','Si A∈F\\G, A∩B est réunion ... Soit A cette strate de F','top')
inv('deletion','top line 2','Reste','top')
inv('insertion','after strate in top line 2','G|∈','top_insertion')
inv('deletion','end of top line 3','On','top')
inv('cancelled display','upper left','A=union_{B∈F;B≤F} B°','union')
inv('text block','upper part first case',"Si A∉G′ ... F\\G′⊂F′ ... et on gagne",'cases')
inv('text block','upper part second case',"Si A∈G ... G′≼G ... et on gagne encore",'cases')
inv('margin note','left of corollary, oblique','Ultra faux','ultra')
inv('underlined heading','upper middle','Corollaire','corollary')
inv('deletion','corollary noun','raffinement','corollary')
inv('insertion','above raffinement','subdivision','corollary')
inv('text block','corollary assertion','Le ... précédente F′ ... propriétés équivalentes suivantes','corollary')
inv('insertion','before des propriétés','chacune','corollary')
inv('cancelled text block','central condition a)','a) Pour toute subdivision F′′ ... G′ sur G','condition_a')
inv('drawing','across full condition a)','large X','condition_a')
inv('deletion with underline','within a)','maximal','condition_a')
inv('insertion','above maximal','un plus grand élémt|élément|élt','a_noun')
inv('reference mark','a), after order sign','star above ≼','condition_a')
inv('unidentified drawing','below qui in final long line of a)','angular E/∈-like strokes and short detached upper stroke','angular_mark')
inv('margin note','left of a), oblique','* ou pour ≪, cela revient au = parmi ...','star_note')
inv('margin note','left lower middle, long oblique block','les conditions ... Mais ces trois cond. ... d’impliquer a)','long_note')
inv('deletion','start of long note enumeration','a)','note_upper')
inv('underline','long note','impliquées','note_upper')
inv('drawing; deletion state uncertain','transverse through long note','curved stroke crossing the full prose block','long_note')
inv('text block','condition b)','L’application can. associée à F′≼F','condition_b')
inv('display','under b)','φ:F′→F','condition_b')
inv('text block','between b) displays','induit une bijection','condition_b')
inv('display','second b) display','F′\\G′ →~ F\\G','condition_b')
inv('margin note','right of b)','NB. c’est tjrs|tojrs surj. donc ... ici','NB')
inv('underline and rule','NB','injectivité underline; vertical left rule','NB')
inv('deletion','c), lower line','Les strates ouvertes de F′ qui ne sont','c_full')
inv('insertion/text block','c), above deletion, then left continuation','∀A∈F\\G, A° est une strate ouverte de F′','c_full')
inv('text block','d)','F′⊃F\\G, i.e. ∀A∈F\\G, on a A∈F′','condition_d')
inv('underlined heading and text','foot','Dém On va prouver p. ex','proof_heading')
inv('display','foot cycle','d)⇒b)⇒c)⇒a)⇒d)','proof_heading')
inv('deletion with underline','bottom left','Dém','bottom')
inv('text block','bottom proof','d)⇒b) Si (F\\G)⊂F′ ... il reste à prouver','bottom')
inv('overwritten deletion','bottom proof, old word','identité','bottom')
inv('overwriting','bottom proof, replacement','inclusion','bottom')
inv('deletion','bottom proof','(trivial)','bottom')
inv('insertion','above cancelled trivial','can. F\\G↪F','bottom')
inv('deletion and repetition','bottom proof','deleted donc then live donc','bottom')
inv('display','bottom edge','F\\G=F′\\G′','bottom')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who={'model':'inherited','effort':'inherited; not separately exposed','run':'R3 scan032'}
checks=[
 {'statement_id':'R3-032-d-membership','place':'condition d), its i.e. reformulation','date':now,'who':who,'type':'targeted proof check','outcome':'With the inclusion symbol used non-strictly as the manuscript’s following i.e. specifies, F′ contains F\\G iff every A in F\\G belongs to F′. Both directions follow immediately from the definition of subset. This checks only the written reformulation, not the corollary.'},
 {'statement_id':'R3-032-bottom-sufficiency','place':'bottom d)⇒b), reduction to F\\G=F′\\G′','date':now,'who':who,'type':'targeted proof check','outcome':'Conditional check: assuming the preceding restriction φ|F\\G is the canonical inclusion and assuming the displayed equality F\\G=F′\\G′, the restriction φ:F′\\G′→F\\G maps each element to itself and is therefore injective and surjective. This verifies that the equality would suffice; it does not establish either assumption or the equality.'}
]
crops=json.loads((OUT/'scan032_crops.json').read_text())
for r in crops:
 if 'id' not in r:r['id']=r.pop('name')
 r['viewed']=True
(OUT/'scan032_crops.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2))
base=ROOT/'source/SP34_CW_156-5_scans'
images=[{'sequence':1,'path':str(base/'J156-5-04_156-5_scan032.jpg'),'role':'whole first'},{'sequence':2,'path':str(base/'J156-5-04_156-5_scan032_a.jpg'),'role':'upper half'},{'sequence':3,'path':str(base/'J156-5-04_156-5_scan032_b.jpg'),'role':'lower half'}]
images += [{'sequence':i+4,'path':r['path'],'role':'enlarged/rotated crop','crop_id':r['id']} for i,r in enumerate(crops)]
report={
 'scan':'032','manuscript_page':'31','reader':'R3','model':'inherited','effort':'inherited; not separately exposed','start_utc':(OUT/'scan032_start.txt').read_text().strip(),'end_utc':now,
 'source_C':str(Cpath),'source_H':str(Hpath),'proposed_tex':str(OUT/'scan032.tex'),
 'workflow':{'independent':True,'whole_then_halves':True,'all_text_read_against_ink':True,'other_readers_or_root_decisions_consulted':False,'later_page_opened':False,'ocr_used':False,'web_research_used':False,'scope':'scan032 only'},
 'images_viewed':images,'image_view_notes':['The first combined corollary/ultra output was truncated; both were subsequently emitted individually and read.','The whole image was viewed again after the detailed crops to locate the full long-note endpoint.','Initial long-note crop missed its far-right high endpoint; note_complete_tail extends the source bbox and includes the final a).'],
 'crops':crops,'differences':D,'C_doubt_resolutions':cd,
 'S_row_decisions':{'applicable_rows':[],'decision':'No numeric scan range in the S CORRECTIONS where field includes 032; no S correction imported.'},
 'inventory':I,
 'remaining_doubts':[{'difference_id':d['id'],'place':d['place'],'reading':d['reading'],'confidence':d['confidence']} for d in D if d['id'] in ['D04','D05','D15','D19','D24','D25','D28','D31','D32','D34','D36','D47','D48']],
 'notation':[
  {'symbol':'F, G and primes','reading':'plain capitals; F′, F′′ and G′ retained occurrence by occurrence','evidence':'The two G primes in the first case are secure despite their possible mathematical difficulty. Second-case G is unprimed.'},
  {'symbol':'preceq / preccurlyeq','reading':r'\preceq','evidence':'Curved order sign with lower stroke; H’s macro variant is not treated as a different mathematical reading.'},
  {'symbol':'B° and A°','reading':r'\circ','evidence':'Small open circles at upper right, not zero subscripts.'},
  {'symbol':'literal B≤F','reading':'F in cancelled union lower limit','evidence':'Vertical with two bars, matching F above; not changed to A from expected mathematics.'},
  {'symbol':'= in starred note','reading':'literal shorthand = at both occurrences','evidence':'Not expanded to même in transcription.'},
  {'symbol':'arrows','reading':'ordinary φ arrow; bijection arrow with raised tilde; bottom hooked inclusion arrow; doubled implication arrows','evidence':'Every arrowhead/decoration viewed at enlarged scale.'},
  {'symbol':'supset in d)','reading':r'\supset','evidence':'No separate equality bar; the following i.e. supplies the author’s non-strict interpretation.'},
  {'abbreviations':'can.; tjrs|tojrs; ens; p. ex; cond.; surj.; uncertain élémt|élément|élt','expansion_notes_only':'can. likely canonique; tjrs/tojrs toujours; ens ensemble; p. ex par exemple; cond. conditions; surj. surjectif/surjective; élémt/élt élément. No expansion made in text.'}
 ],
 'notes_while_reading':[
  'The page continues a refinement argument, then states a corollary with four conditions. Condition a) is crossed with a large X; Ultra faux is an oblique marginal warning.',
  'The long marginal note asserts equivalence of b), c), d), implication from a), and failure of the converse, subject to the retained local reading doubts. A long internal curved stroke may cancel the note as a whole. It is preserved graphically and its function is not presented as certain.',
  'No expected mathematics was used to remove the two first-case G primes or to replace F by A in the cancelled union limit.',
  'One live On is visible beneath Dém. C’s extra cancelled On is not an independently visible word: its supposed strokes are the outer and inner portions of the same O and the higher heading underline.',
  'The E/∈-like isolated mark under qui is transcribed as strokes. Its identity and role remain unknown.',
  'C’s 25 doubt occurrences were individually reviewed. The dense overwritten bottom words and several oblique-note endings remain the least secure readings.',
  'Only the two limited logical checks below were performed. Reading the corollary, its cycle of implications, or the author’s marginal correction is not reported as a proof check. No proof of the full equivalence or first-case construction is claimed.'
 ],
 'check_events':checks,
 'validation':{'full_tex_saved':True,'C_doubt_count':len(cd),'difference_count':len(D),'inventory_count':len(I),'crop_count':len(crops),'compiled':False,'structural_checks':'pending external script check'}
}
(OUT/'scan032.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'tex':str(OUT/'scan032.tex'),'json':str(OUT/'scan032.json'),'differences':len(D),'C_doubts':len(cd),'inventory':len(I),'crops':len(crops)},indent=2))
