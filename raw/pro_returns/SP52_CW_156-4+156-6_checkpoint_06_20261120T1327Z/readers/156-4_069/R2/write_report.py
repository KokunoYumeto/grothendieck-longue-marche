import json
from pathlib import Path
from datetime import datetime, timezone
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_069/R2')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_069')
meta=json.loads((packet/'metadata.json').read_text())
crops=json.loads((out/'crop_metadata.json').read_text())
cm={int(Path(c['path']).stem.split('_')[0]):c for c in crops}
whole,ha,hb=meta['images']
D=[]
def diff(location,c,h,reading,shows,kind='other',confidence='high',marked='no',cc=False,ch=True,crop=None,bbox=None,image=None,math=False):
 if crop is not None:
  ci=cm[crop]; path=ci['path']; bb=bbox or ci['bbox']; img=whole
 else: path=None; bb=bbox; img=image
 D.append(dict(id=f'D{len(D)+1:02d}',location=location,c=c,h=h,reading=reading,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=path,bbox=bb,bbox_image=img,math_consequential=math))
diff('Opening, after réunion',r'engendrée par la réunion)',r'engendrée par la réunion).',r'engendrée par la réunion)','Half a shows the closing parenthesis and clear space before Je; no separate full stop.',bbox=[900,90,1340,185],image=ha)
diff('Opening correction: distinct leader from présume',r'Je \deleted{dis} \inserted{présume} qu\'on',r'Je \struck{dis} \add{présume} qu\'on',r'Figure F01: Je / \deleted{dis} / raised \inserted{présume} / qu\'on, with curved diagonal arm','A separate curved stroke descends from the right of présume into the gap before qu’on; the deletion itself is secure.','drawing or diagram',cc=True,crop=1)
diff('Boole qualification: insertion state of ultra',r'\inserted{``ultra}stonienne\'\'',r'« ultra-stonienne »',r'Figure F01: raised \inserted{``ultra}, baseline stonienne\'\'','Ultra and its opening quotation marks are above the baseline, joined to the beginning of stonienne.','insertion or placement',crop=2)
diff('Boole qualification: quotation glyphs',r'``ultrastonienne\'\'',r'« ultra-stonienne »',r'``ultrastonienne\'\'','Two short upright marks occur before ultra and two after stonienne, not angle-shaped guillemets.',crop=2)
diff('Boole qualification: junction ultra/stonienne',r'\inserted{``ultra}stonienne\'\'',r'« ultra-stonienne »',r'\inserted{``ultra}stonienne\'\'','The connecting stroke is the insertion arm; no hyphen is separately written between the words.',crop=2)
diff('Boole qualification: insertion arm and detached low stroke',r'\inserted{``ultra}stonienne\'\'',r'« ultra-stonienne »',r'Figure F01: curved arm under ultra and short detached stroke below stonienne','The arm curves under the inserted word and hooks upward at its right end. A small detached diagonal dash is visible below the early middle of stonienne. Its function is not inferred.','drawing or diagram',cc=True,crop=2)
diff('After Sup',r'\unsure{quelc.}',r'quelc.',r'quelc.','The long initial descender and following compressed u-e-l-c group end with a discrete point; resolved as quelc.','other',cc=True,ch=False,crop=3)
C=(packet/'C.tex').read_text()
margin=C[C.index('\\margin{Cela'):C.index('\n\n\\deleted{Il faudra')]
final=(out/'reading.tex').read_text()
margin_final=final[final.index('\\margin{Cela'):final.index('\n\n\\deleted{Il faudra')]
diff('Entire long left marginal note, including its display',margin,'',margin_final,'The slanted note has continuous text from Cela sera valable through pour trois supports, followed by P,Q,R and the distributive expression. H supplies only editorial fragments, not a diplomatic transcription. Local doubts and revisions are separately itemized below.','omission','high','yes',False,True,19,math=True)
diff('Marginal note, Stone',r'le compactifié de Stone',r'',r'le compactifié de \unsure{Stone}','The body writing intrudes into the final word of this slanted line. I retain Stone as best reading but cannot secure every stroke in the supplied crop; no appeal to the mathematical name was used.','other','medium','yes',True,True,17)
diff('Marginal equality, extra opening mark',r'=\unsure{(|\{}(P\wedge Q)',r'',r'=\unsure{\{|(}(P\wedge Q)','There is a distinct hooked mark before the ordinary opening parenthesis. Its top has a small return and its lower stroke descends; a brace is my first candidate, with parenthesis retained.','misread symbol or index','low','yes',True,True,19,math=True)
diff('Marginal equality, terminal extra mark',r'(P\wedge R)\unsure{.|,|)}',r'',r'(P\wedge R)\unsure{\}|.|,|)}','A compact hooked/looped mark follows the last parenthesis in the zone of crossing body ink. A closing brace is possible; a point, comma, or parenthesis cannot be excluded.','misread symbol or index','low','yes',True,True,19,math=True)
diff('Beginning of supports paragraph',r'\unsure{Donc}',r'\ill{}',r'\unsure{Donc}','An initial D and long reduced continuation support Donc, but the medial letters remain reduced.','readable ink left as \\ill{}','medium','yes',False,True,5)
diff('Supports paragraph, verb',r'\unsure{s\'identifient|s\'identifieraient}',r's\'identifient',r's\'identifient','The tall f is followed by an i point and a short reduced final sequence; there is no separate raient-sized run. The present form is resolved.','other','high','no',True,False,5)
diff('Supports paragraph, Parties through spectre',r'\unsure{Parties|Partie} à la fois ouvertes et fermées du spectre',r'\ill{} \ill{} et \ill{} \ill{} espace',r'\unsure{Parties|Partie} à la fois ouvertes et fermées du spectre','The words à la fois ouvertes et fermées are visible in the second body line; du spectre follows. The terminal s of Parties remains uncertain. H’s espace at this earlier position has no support.','readable ink left as \\ill{}','medium','yes',False,True,5,math=True)
diff('Before compact abbreviation, cancelled group',r'\deleted{\unsure{to|tot}}',r'\ill{}',r'\deleted{\unsure{to|tot}}','A separate short word-sized group precedes the live abbreviation, with a tall first stroke and overwritten oval(s); its cancellation is visible.','omission','low','yes',False,True,6)
diff('Live compact abbreviation',r'\unsure{compact|cpct}',r'\ill{}',r'\unsure{cpct|cpt|compact}','A wide c-like entrance, p descender, and final ct/t are visible. The space before the descender does not independently resolve a full om sequence; cpct is first, cpt and compact retained.','abbreviation expanded or spelling modernised','medium','yes',True,True,6)
diff('After compact abbreviation, cancelled group',r'\deleted{\unsure{tot}}',r'',r'\deleted{\unsure{tot}}','Two tall t-like stems joined by lower ink stand in a separately cancelled group after the live abbreviation.','omission','low','no',False,True,6)
diff('Before ultra',r'\unsure{disconnexe}',r'discontinu',r'\unsure{disconnexe}','The beginning has disc-like strokes and the end has a crossed x and e-like return. The middle is compressed; discontinu does not fit the ending.','misread word','medium','no',False,True,7,math=True)
diff('Separator between ultra and stonien',r'ultra\unsure{.|-}stonien.',r'ultra-stonien.',r'ultra.stonien.','The separator is a compact, almost square point at mid-height, distinct from the two adjacent words; the separate final point is also present.','other','high','no',True,True,7)
diff('Involution sentence, subject',r'L\'involution',r'\ill{}',r'L\'involution','The tall initial L, apostrophe and following in-volu-tion sequence are readable in half a.','readable ink left as \\ill{}','high','yes',False,True,None,[340,770,750,900],ha,True)
diff('Involution sentence, verb',r'correspond',r'correspondant',r'correspond','The visible verb ends with the high final d return; no added ant group is present.','misread word','high','no',False,True,None,[790,750,1160,870],ha)
diff('Involution sentence, object',r'au passage au complémentaire.',r'au passage \ill{} l\'inclusion \ill{}',r'au passage au complémentaire.','The right of the upper line gives au passage; the following line starts au and has complémentaire with a separate terminal point.','misread word','high','yes',False,True,None,[335,755,1635,1020],ha,True)
diff('Construction paragraph, opening through Sigma',r'On fera attention que la construction $\Sigma$',r'\ill{} la construction \ill{} $\Sigma$',r'On fera attention que la construction $\Sigma$','Half a shows On fera attention que, followed by la construction; the next line begins with angular Sigma.','readable ink left as \\ill{}','high','yes',False,True,None,[425,1020,1655,1225],ha)
diff('Construction paragraph, dependence wording',r'ne dépend que de',r'en \ill{} que \ill{}',r'ne dépend que de','The short ne precedes the d-pendant-stroke sequence of dépend; que de follow.','readable ink left as \\ill{}','high','yes',False,True,None,[565,1130,1235,1215],ha,True)
diff('Construction paragraph, ens punctuation',r'l\'ens',r'l\'ens.',r'l\'ens','The final s has an attached down-turn; no independent abbreviation point follows it.','other','high','no',False,True,None,[1280,1110,1495,1190],ha)
diff('Construction paragraph, first M',r'$M$',r'$\mathcal{M}$',r'$M$','The letter has the two ordinary pointed stems seen in this occurrence; no separate script alphabet is indicated.','misread symbol or index','high','no',False,True,8,bbox=[490,1220,605,1305])
diff('Compatibility insertion, initial words',r'\inserted{muni de la relation}',r'\add{et de la relation}',r'\inserted{muni de la relation}','The raised clause starts with the reduced humps of muni, then de la relation; it does not begin et.','misread word','high','no',False,True,8)
diff('Compatibility insertion, local R',r'\unsure{\mathcal R|R}',r'R',r'\unsure{\mathcal R|R}','The insertion’s R has a round return, but is less elaborately curled than the relation in the bottom display. The local alphabet doubt is retained.','misread symbol or index','medium','no',False,True,8,bbox=[1025,1150,1125,1230])
diff('Compatibility insertion, complete enclosure',r'\inserted{muni de la relation $\unsure{\mathcal R|R}$ de compatibilité}',r'\add{et de la relation $R$ de compatibilité}',r'Figure F02: upper inserted clause with long curved enclosure and left descending arm','A separate line runs below the whole raised clause, curls upward at the far right, and drops left into the gap following M.','drawing or diagram','high','no',True,True,8)
diff('Lower insertion before la famille',r'\inserted{\unsure{toute|toutes}}',r'\add{toutes}',r'\inserted{toute}','The inserted word is below the line and shows t-ou-t-e without a separate terminal s. The peaked leader targets the gap before la.','misread word','high','no',True,True,9)
diff('Family wording',r'la famille des parties',r'les parties',r'la famille des parties','La famille occurs to the right of connaître; des parties follows on the next manuscript line.','omission','high','no',False,True,9)
diff('Lower insertion, angular connector',r'\inserted{\unsure{toute|toutes}}',r'\add{toutes}',r'Figure F02: below-line \inserted{toute} with peaked connecting bracket','A separate angular upper bracket has a central peak at the insertion site and two lower arms enclosing the added word.','drawing or diagram','high','no',True,True,9)
diff('Phi after parties',r'\unsure{\overline\Phi|\Phi\'|\Phi}',r'\Phi',r'\unsure{\Phi\'|\overline\Phi|\Phi}','A heavy short mark lies high and to the right of the Phi. Displacement favours a prime as first candidate, but its nearly horizontal shape and dense ink leave bar or stray mark possible.','misread symbol or index','low','no',True,True,10,math=True)
diff('After Phi, M',r'de $M$',r'de $\mathcal{M}$',r'de $M$','The M is a plain pointed capital, without script flourishes.','misread symbol or index','high','no',False,True,10,bbox=[960,1285,1095,1385])
diff('Tuple, M alphabet',r'(M,\leq,R)',r'(\mathcal{M}, \leq, R)',r'(M,\leq,R)','A plain two-peaked M, the two-stroke less-than-or-equal sign, and the plainer R are visible with both commas.','misread symbol or index','high','no',False,True,11)
diff('Definition prose, M prime and M',r'une partie $M\'$ de $M$',r'une partie $\mathcal{M}\'$ de $\mathcal{M}$',r'une partie $M\'$ de $M$','Both capitals are plain M; the first has one short detached high tick.','misread symbol or index','high','no',False,True,11)
diff('Displayed operator, spelling',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosupp}',r'\operatorname{cosup}','Only one p downstroke follows the cosu run before the lowered M; this occurrence is read cosup.','other','high','no',True,True,12)
diff('Display, M alphabet in operator, argument and set',r'\operatorname{cosup}_M(M\')=\{x\in M',r'\operatorname{cosupp}_{\mathcal{M}}(\mathcal{M}\')=\lbrace X\in\mathcal{M}',r'\operatorname{cosup}_M(M\')=\{x\in M','The subscript, argument, and ambient-set capitals all use plain M forms. Operator spelling and x capitalization are separately recorded.','misread symbol or index','high','no',False,True,12)
diff('Display, bound x and its two repeated occurrences',r'x\in M\mid(x,x\')\in\mathcal R\quad\forall x\'',r'X\in\mathcal M\mid(X,X\')\in R\quad\forall X\'',r'x\in M\mid(x,x\')\in\mathcal R\quad\forall x\'','The crossed letters are small relative to M and R and read as lower-case x throughout. The comma and two x primes are visible.','misread symbol or index','high','no',False,True,13)
diff('Display, compatibility relation alphabet',r'\mathcal R',r'R',r'\mathcal R','The relation has a pronounced encircling left loop and curled return, unlike the tuple R.','misread symbol or index','high','no',False,True,13,bbox=[1390,1645,1480,1765])
diff('Display, last M prime',r'M\'',r'\mathcal M\'',r'\unsure{M\'|M\'\'}','The final high mark is kinked and crowded against the closing brace. One prime is the best reading; I cannot exclude two linked short strokes. Plain M is certain.','misread symbol or index','medium','no',True,True,13,bbox=[1585,1650,1670,1775],math=True)
diff('Bottom example, de',r'\uline{Ex} de',r'\emph{Ex} des',r'\uline{Ex} de','The small word after Ex has d and e with a terminal hook, but no independent final s.','misread word','high','no',False,True,20)
diff('Bottom example, quotation marks',r'``supports\'\'',r'supports',r'``supports\'\'','Two high marks precede supports and two high marks follow it.','omission','high','no',False,True,20)
diff('Bottom example, connective',r'``supports\'\', ou parties',r'supports : parties',r'``supports\'\', ou parties','The closing quotes are followed by a comma and a small ou before the line with parties.','misread word','high','no',False,True,20)
diff('Bottom example, both M occurrences',r'parties saturées de $M$ : les comp. connexes de $M$',r'parties saturées de $\mathcal{M}$ : \ill{} comp. conn. de $\mathcal{M}$',r'parties saturées de $M$ : les comp. connexes de $M$','Both M forms are ordinary capitals. The first has a following colon. The independent lexical differences are recorded in the next entries.','misread symbol or index','high','yes',False,True,20)
diff('Bottom example, before comp.',r'les comp.',r'\ill{} comp.',r'les comp.','The small word reads les, with an l loop and a terminal s.','readable ink left as \\ill{}','high','yes',False,True,20)
diff('Bottom example, connexes',r'connexes',r'conn.',r'connexes','After the initial co loop, reduced n strokes and a distinct x-ending run continue to the final es; the full word is written.','abbreviation expanded or spelling modernised','high','no',False,True,20)
diff('Bottom example, slant and long rule',r'\margin{\uline{Ex} de ``supports\'\', ou parties saturées de $M$ : les comp. connexes de $M$ (utiliser C4).}',r'\emph{Ex} des supports : parties saturées de $\mathcal{M}$ : \ill{} comp. conn. de $\mathcal{M}$ (utiliser C4).',r'Figure F03: slanted example note with separate long rule from the connexes area toward the right','The example is oblique. A long rule begins beside/intersects the initial co of connexes and extends nearly horizontally in the page orientation. It does not cancel the entire line. H describes a trait in an editorial note but does not draw it.','drawing or diagram','high','no',True,True,20)

CD=[]
def cd(location,c,reading,status,shows,crop=None,bbox=None,image=None):
 ci=cm.get(crop)
 CD.append(dict(location=location,c=c,reading=reading,status=status,scan_shows=shows,crop=ci['path'] if ci else None,bbox=bbox or (ci['bbox'] if ci else None),bbox_image=whole if ci else image))
cd('C.tex: after Sup',r'\unsure{quelc.}',r'quelc.','resolved','Descender, compressed remaining letters, and final point are separable.',3)
cd('C.tex: cancelled word after donnés',r'\deleted{\unsure{tout}}',r'\deleted{\unsure{tout}}','retained','A short crossed group lies below the descender of types; t-like ends and medial reduced ink allow tout but do not fully resolve it.',15)
cd('C.tex: marginal verb before le compactifié',r'\unsure{on trouve|on trouvera|on retrouve}',r'\unsure{on trouve|on trouvera|on retrouve}','retained','The t cross stroke and long nearly level continuation are visible, but the compressed final syllable cannot distinguish the alternatives.',17)
cd('C.tex: after qui vient',r'\unsure{je}',r'\unsure{je}','retained','A descending loop with a short upper return supports je; both letters are not independently separable.',18)
cd('C.tex: after comment',r'\unsure{prouver}',r'\unsure{prouver}','retained','The p descender and low continuation support prouver; middle lettering remains reduced.',18)
cd('C.tex: extra opening sign in marginal equality',r'\unsure{(|\{}',r'\unsure{\{|(}','revised','The top return and descending hook favour a brace, with a parenthesis still possible.',19)
cd('C.tex: last sign of marginal equality',r'\unsure{.|,|)}',r'\unsure{\}|.|,|)}','revised','The extra compact loop/hook permits a closing brace in addition to the C alternatives; crossing body ink prevents settlement.',19)
cd('C.tex: beginning of supports paragraph',r'\unsure{Donc}',r'\unsure{Donc}','retained','Initial D is clear; the reduced following run supports Donc without resolving all middle strokes.',5)
cd('C.tex: s’identifient',r'\unsure{s\'identifient|s\'identifieraient}',r's\'identifient','resolved','An i follows the tall f and a short terminal run follows; no distinct conditional ending is visible.',5)
cd('C.tex: Parties/Partie',r'\unsure{Parties|Partie}',r'\unsure{Parties|Partie}','retained','A short terminal stroke could be a reduced s or the exit of e.',5)
cd('C.tex: cancelled group before compact',r'\deleted{\unsure{to|tot}}',r'\deleted{\unsure{to|tot}}','retained','Tall first stroke and dense oval ink remain crossed; a further t cannot be separated securely.',6)
cd('C.tex: compact/cpct',r'\unsure{compact|cpct}',r'\unsure{cpct|cpt|compact}','revised','The visible compact group most strongly suggests cpct; cpt is also possible, while full compact cannot be ruled out in the reduced horizontal run.',6)
cd('C.tex: cancelled group after compact',r'\deleted{\unsure{tot}}',r'\deleted{\unsure{tot}}','retained','Separate t-like tall stems remain under the cancellation; medial lettering is unclear.',6)
cd('C.tex: disconnexe',r'\unsure{disconnexe}',r'\unsure{disconnexe}','retained','Beginning disc and an x/e-like ending are visible; the central run is insufficiently differentiated.',7)
cd('C.tex: separator in ultra.stonien',r'\unsure{.|-}',r'.','resolved','A compact nearly square point is visibly distinct from a long hyphen.',7)
cd('C.tex: compatibility insertion R',r'\unsure{\mathcal R|R}',r'\unsure{\mathcal R|R}','retained','The round return gives a calligraphic appearance but is less conclusive than the large displayed R.',8)
cd('C.tex: inserted toute/toutes',r'\unsure{toute|toutes}',r'toute','resolved','The last t/e ends without a separate s; the angular leader places the word before la famille.',9)
cd('C.tex: Phi modifier',r'\unsure{\overline\Phi|\Phi\'|\Phi}',r'\unsure{\Phi\'|\overline\Phi|\Phi}','revised','The high mark is displaced to the right; prime is first, with bar and unmodified Phi retained because the mark is densely worked.',10)
cd('C.tex: displayed cosup/cosupp',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','A single final p descender precedes the lowered M.',12)
cd('C_context notation check: upper and marginal quotation pairs',r'French text in TeX double quotes',r'``ultrastonienne\'\'; ``le cas ensembliste\'\'','resolved','The upper and marginal pairs consist of two short strokes. The upper opening marks are raised with ultra.',14)
cd('C_context notation check: E, E_disc. and Sigma',r'E, E_{\mathrm{disc.}}, \Sigma',r'E, E_{\mathrm{disc.}}, \Sigma','resolved','The letters E show three arms; disc. is lower and smaller with a final point; Sigma is angular.',16)
cd('C_context notation check: wedge, vee, P Q R',r'P\wedge(Q\vee R)=\unsure{(|\{}(P\wedge Q)\vee(P\wedge R)\unsure{.|,|)}',r'P\wedge(Q\vee R)=\unsure{\{|(}(P\wedge Q)\vee(P\wedge R)\unsure{\}|.|,|)}','revised','The same pointed/rounded inverted-V strokes occur at each wedge position and pointed Vs at each vee. P,Q,R are distinct plain capitals. Only the extra opening/terminal marks remain open.',19)
cd('C_context notation check: insertion, tuple and display R alphabets',r'\unsure{\mathcal R|R},\;(M,\leq,R),\;\mathcal R',r'\unsure{\mathcal R|R},\;(M,\leq,R),\;\mathcal R','retained','Insertion remains locally uncertain. Tuple R is plainer. The display relation has the full encircling return and is securely calligraphic.',13)
cd('C_context notation check: high Phi mark',r'\unsure{\overline\Phi|\Phi\'|\Phi}',r'\unsure{\Phi\'|\overline\Phi|\Phi}','revised','Right displacement favours prime but the short thick mark does not establish its function.',10)
cd('C_context notation check: comma and primes in final display',r'(x,x\'),\;\forall x\'\in M\'',r'(x,x\'),\;\forall x\'\in\unsure{M\'|M\'\'}','revised','The pair separator has a descending comma tail and both x primes are clear. The final M high mark is more crowded and kinked, so only that occurrence is newly uncertain.',13)
cd('C_context notation check: final operator tail',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}_M(M\')',r'\operatorname{cosup}_M(M\')','resolved','Only one p downstroke occurs locally; no other scan was consulted.',12)
cd('C_context wording check: possible pas',r'je ne vois comment prouver',r'\unsure{je} ne vois comment \unsure{prouver}','resolved','No independent word-sized group lies between vois and comment; no pas is supplied. The local je and prouver uncertainties remain.',18)

RD=[]
def rd(loc,reading,alts,conf,reason): RD.append(dict(location=loc,reading=reading,alternatives=alts,confidence=conf,reason=reason))
rd('Margin, cancelled word after donnés',r'\deleted{\unsure{tout}}',['tout'],'low','Cancellation and the descender above obscure the reduced middle letters.')
rd('Margin, verb before le compactifié',r'\unsure{on trouve|on trouvera|on retrouve}',['on trouve','on trouvera','on retrouve'],'low','A long reduced final run does not establish the tense or the possible re syllable.')
rd('Margin, proper name after compactifié de',r'\unsure{Stone}',['Stone'],'medium','Crossing body writing prevents a confident stroke-by-stroke reading of this final word.')
rd('Margin, after qui vient',r'\unsure{je}',['je'],'medium','The descending loop does not cleanly separate the two letters.')
rd('Margin, after comment',r'\unsure{prouver}',['prouver'],'medium','The middle and ending remain greatly reduced after the p.')
rd('Margin equality, extra opening mark',r'\unsure{\{|(}',['\\{','('],'low','A hooked mark precedes the ordinary factor parenthesis; exact form is open.')
rd('Margin equality, extra terminal mark',r'\unsure{\}|.|,|)}',['\\}','.',',',')'],'low','A hooked or looped mark coincides with body-writing territory; its extent and function remain open.')
rd('Supports paragraph beginning',r'\unsure{Donc}',['Donc'],'medium','D is clear; the following letters are reduced to a long run.')
rd('Supports paragraph, Parties ending',r'\unsure{Parties|Partie}',['Parties','Partie'],'medium','Final short exit may or may not carry a distinct s.')
rd('Before compact abbreviation',r'\deleted{\unsure{to|tot}}',['to','tot'],'low','Dense crossing makes the number of t-like stems uncertain.')
rd('Live compact abbreviation',r'\unsure{cpct|cpt|compact}',['cpct','cpt','compact'],'medium','The beginning and medial stroke are too reduced to distinguish abbreviation from full word.')
rd('After compact abbreviation',r'\deleted{\unsure{tot}}',['tot'],'low','Cancelled medial lettering is not independently clear.')
rd('Before ultra.stonien',r'\unsure{disconnexe}',['disconnexe'],'medium','Ending x/e is visible, but compressed middle lettering remains uncertain.')
rd('Raised compatibility clause, R only',r'\unsure{\mathcal R|R}',['\\mathcal R','R'],'medium','Round return suggests calligraphic form without the decisive display flourish.')
rd('Phi after parties',r'\unsure{\Phi\'|\overline\Phi|\Phi}',['\\Phi\'','\\overline\\Phi','\\Phi'],'low','The high thick mark is displaced to the right and may be prime, bar or an independent blot.')
rd('Final display, last M only',r'\unsure{M\'|M\'\'}',["M'","M''"],'medium','The small high mark is kinked and crowded against the closing brace; one prime is first.')

INV=[]
def inv(element,kind,pos,words): INV.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('I01','text','top centre','68')
inv('I02','text','upper body, three manuscript lines','engendrée par la réunion) Je …')
inv('I03','deletion','upper right, after Je','dis')
inv('I04','insertion','above dis','présume')
inv('I05','drawing','upper right','curved diagonal présume arm, Figure F01')
inv('I06','insertion','above stonienne','``ultra')
inv('I07','drawing','below raised ultra','curved insertion arm with right hook, Figure F01')
inv('I08','drawing','below early middle of stonienne','short detached low dash, Figure F01')
inv('I09','margin note','left edge, long oblique note','Cela sera valable dans ``le cas ensembliste\'\' …')
inv('I10','deletion','within oblique note, after donnés','tout (uncertain)')
inv('I11','display','end of long oblique note','P,Q,R and P wedge (Q vee R) equality')
inv('I12','deletion','body below opening Boole paragraph','Il faudra y revenir')
inv('I13','text','upper-middle body','Donc les supports …')
inv('I14','deletion','before live compact abbreviation','to/tot')
inv('I15','deletion','after live compact abbreviation','tot')
inv('I16','text','middle body, two lines','L’involution correspond au passage …')
inv('I17','text','lower body, before final display','On fera attention que la construction Sigma …')
inv('I18','insertion','raised after first M','muni de la relation R de compatibilité')
inv('I19','drawing','under compatibility insertion','long enclosure and left descending arm, Figure F02')
inv('I20','insertion','below connaître / before la famille','toute')
inv('I21','drawing','above lower inserted toute','peaked bracket with two arms, Figure F02')
inv('I22','display','lower body','cosup_M(M prime) = { x in M | … }')
inv('I23','margin note','bottom, shallow oblique hand','underlined Ex de ``supports\'\', ou …')
inv('I24','drawing','bottom, near connexes to the right','long nearly horizontal rule, Figure F03')

N=[
 dict(sign='Plain M',latex=r'M,M\'',appearance='two pointed strokes; plain alphabet throughout this page',location='body, tuple, display and bottom note',alternatives=[]),
 dict(sign='Compatibility R, raised insertion',latex=r'\unsure{\mathcal R|R}',appearance='round returned bowl, less elaborate than display',location='raised compatibility clause only',alternatives=[r'\mathcal R','R']),
 dict(sign='Compatibility R, tuple',latex='R',appearance='plainer upright and short bowl with right leg',location='(M,≤,R)',alternatives=[]),
 dict(sign='Compatibility R, display',latex=r'\mathcal R',appearance='encircling left loop and curled return',location='(x,x prime) in relation',alternatives=[]),
 dict(sign='Phi high mark',latex=r'\unsure{\Phi\'|\overline\Phi|\Phi}',appearance='oval across upright with baseline foot; small thick high mark displaced right',location='after parties',alternatives=[r'\Phi\'',r'\overline\Phi',r'\Phi']),
 dict(sign='Cosupport operator',latex=r'\operatorname{cosup}',appearance='single final p downstroke',location='final display',alternatives=[]),
 dict(sign='Set elements',latex=r'x,x\'',appearance='small crossed letters, detached high prime ticks on x',location='final display',alternatives=[]),
 dict(sign='Final M mark',latex=r'\unsure{M\'|M\'\'}',appearance='kinked high small stroke immediately before closing brace',location='last member of final display',alternatives=["M'","M''"]),
 dict(sign='Lower abbreviation disc.',latex=r'E_{\mathrm{disc.}}',appearance='three-bar E with smaller lower disc and final point',location='left marginal note',alternatives=[]),
 dict(sign='Wedge and vee',latex=r'\wedge,\vee',appearance='heavy inverted V/rounded peak versus pointed V',location='oblique distributive equality',alternatives=[]),
 dict(sign='Detached low stroke',latex='Figure F01 TikZ short line',appearance='small oblique dash below stonienne',location='upper qualification',alternatives=['unassigned function'])]
A=[dict(form='Sup',expansion='supremum / supremums'),dict(form='quelc.',expansion='quelconque(s)'),dict(form='top.',expansion='topologique'),dict(form='ens',expansion='ensemble'),dict(form='disc.',expansion='discret'),dict(form='cpct / cpt (uncertain)',expansion='compact'),dict(form='cosup',expansion='cosupport'),dict(form='Ex',expansion='exemple'),dict(form='comp.',expansion='composantes')]
notes=dict(summary='The page continues a discussion of supports: a presumed Boolean algebra and Stone-space interpretation, a long marginal reservation about distributivity, a compatibility-based cosupport definition, and an example of saturated parts. All three required source views and 20 independent local crops were actually viewed.',math_reading_decisions='No proof or mathematical validation was attempted. Tracking the repeated P,Q,R factors prompted symbol-by-symbol inspection of the marginal equality, but the extra bracket-like marks were retained as ink doubts. The final prime doubt comes from the crowded high stroke, not a proposed change to the expected formula. C4 is only transcribed.',author_checks='The author writes “Je [dis cancelled] présume” and in the margin “je ne vois comment prouver”; these are authorial statements, not checks performed in this run. The crossed “Il faudra y revenir” is retained. H’s note asserting R rather than disjunction is editorial; the literal display was read directly and its calligraphic relation form retained.',title_dates_pagination='Manuscript page number 68 at top; scan marker 69 retained. No date or title is visible. No cote marker has been added.')
report=dict(reader='R2',cote='156-4',scan='69',brief_version='v05',started_utc='2026-11-20T10:41:37Z',finished_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),image_views=meta['images'],reading_file=str(out/'reading.tex'),differences=D,c_doubts=CD,inventory=INV,remaining_doubts=RD,notation=N,abbreviations=A,notes=notes,check_events=[],crops=crops,workflow_feedback=['Rotation of a rectangular crop of the steep marginal note creates a large diamond containing crossing body ink. A permitted original-bbox-plus-postrotation crop specification would make these loci easier to inspect without revisiting a decided place. The current report records the untrimmed transforms faithfully.'])
# Raw source strings escaped for Python quotes must retain literal TeX apostrophes.
def normalize_quotes(v):
 if isinstance(v,str): return v.replace(chr(92)+"'", "'")
 if isinstance(v,list): return [normalize_quotes(x) for x in v]
 if isinstance(v,dict): return {k:normalize_quotes(x) for k,x in v.items()}
 return v
report=normalize_quotes(report)
for d in report['differences']:
 if d['kind'].startswith('readable ink left'): d['kind']='readable ink left as '+chr(92)+'ill{}'
 if d['location']=='Display, M alphabet in operator, argument and set':
  d['c']=r"\unsure{\operatorname{cosup}|\operatorname{cosupp}}_M(M')=\{\,x\in M"
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
evidence={
1:'dis is struck and présume is raised, with an independent curved diagonal arm to the qu’on gap.',
2:'Raised ultra has double opening marks and an insertion arm; stonienne has double closing marks. A separate small low stroke is retained graphically.',
3:'Sup quelc. has a definite final abbreviation point; quelc. resolved.',
4:'Il faudra y revenir is a single cancelled sentence; no additional live word is inferred.',
5:'Donc retained uncertain; s’identifient resolved; Parties terminal s remains uncertain. À la fois ouvertes et fermées read directly.',
6:'Two separately cancelled groups flank a live compressed compact abbreviation; cpct/cpt/compact retained, without inventing an extra old word.',
7:'disconnexe retained uncertain in its middle; ultra separator resolved as a compact point; final period visible.',
8:'muni de la relation … de compatibilité is all raised. Local R remains uncertain; full enclosure recorded.',
9:'toute is below line, with peaked angular connector before la. No final s independently visible.',
10:'Phi high mark lies to upper right; prime/bar/unmodified alternatives retained. Following M is plain.',
11:'Tuple M and prose M primes are plain; ≤ and both commas are visible; tuple R is plainer than displayed relation.',
12:'One p descender in cosup; subscript M and argument M prime visible.',
13:'Lowercase x, comma and x primes visible; relation is clearly calligraphic. Last M high stroke retained uncertain between one and two primes.',
14:'Opening slanted sentence and double quotes around le cas ensembliste read; no guillemets.',
15:'types, donnés, crossed tout, au début, en termes d’un and E qualification read. Crossed tout remains uncertain.',
16:'E three-bar form, angular Sigma, l’ens and parties read; no alphabet change inferred from mathematical context.',
17:'Compressed on trouve/on trouvera/on retrouve unresolved. The Stone locus remains insufficiently isolated from crossing body ink and is marked uncertain, not claimed resolved.',
18:'je and prouver remain uncertain. No independent pas-sized group between vois and comment.',
19:'P,Q,R and each wedge/vee read. Hook before first right parenthesis and compact terminal hooked mark remain uncertain; closing brace added as a permitted reading.',
20:'Ex is singly underlined; de, paired quotes, comma ou, full connexes, two plain M, and utiliser C4 read. Long rule is reproduced without treating the text as cancelled.'}
with (out/'inspection_log.md').open('a') as f:
 for i in range(1,21):
  ci=cm[i]
  f.write(f"\n{3+i}. Viewed `{ci['path']}` once with view_image. Source `{ci['source']}`; original bbox {ci['bbox']}; rotation {ci['rotation']} degrees; postrotation resize scale {ci['scale']:.9f}; {ci['transform']}. Evidence: {evidence[i]}\n")
 f.write('\nAll 20 crop images were displayed completely. No source half was shown again and no crop was remade or revisited. Report and LaTeX received structural checks only; no mathematical proof is claimed.\n')
print(json.dumps({'differences':len(D),'c_doubts':len(CD),'inventory':len(INV),'remaining_doubts':len(RD),'crops':len(crops)},ensure_ascii=False))
