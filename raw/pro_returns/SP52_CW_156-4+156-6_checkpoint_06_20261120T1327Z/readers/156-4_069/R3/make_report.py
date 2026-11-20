from pathlib import Path
import json
from datetime import datetime, timezone
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_069/R3')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_069')
meta=json.loads((packet/'metadata.json').read_text())
C=(packet/'C.tex').read_text();H=(packet/'H.tex').read_text();reading=(root/'reading.tex').read_text()
crops=json.loads((root/'crop_metadata.json').read_text())
cm={Path(x['path']).stem:x for x in crops}
whole,ha,hb=meta['images']
D=[]
def diff(loc,c,h,r,shows,kind='other',confidence='high',crop=None,bbox=None,source=None,math=False,cc=True,ch=True,marked=None):
    ci=cm.get(crop) if crop else None
    D.append(dict(id=f'R3-D{len(D)+1:02d}',location=loc,c=c,h=h,reading=r,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h=('yes' if ('\\ill' in h or '\\uncertain' in h) else 'no') if marked is None else marked,change_c='yes' if cc else 'no',change_h='yes' if ch else 'no',crop=ci['path'] if ci else None,bbox=bbox or (ci['bbox'] if ci else None),bbox_image=source or (ci['source'] if ci else whole),math_consequential=math))

diff('Opening, immediately after réunion',r'réunion)',r'réunion).',r'réunion)','Closing parenthesis is followed by clear space and Je; no separate stop is visible.','text not on the page',crop='01_opening',cc=False)
diff('Opening raised présume, separate descending leader','','','Figure R3-01, descending curved leader from présume toward the gap before qu\'on','A distinct curved descending stroke runs from the end of the raised word toward its insertion position. Both witnesses retain insertion text but omit this graphic.','drawing or diagram',crop='01_opening')
diff('Opening ultra: quotation style, insertion extent, and alleged hyphen',r'(\inserted{``ultra}stonienne\'\')',r'(« ultra-stonienne »)',r'(\inserted{``ultra}stonienne\'\')','Two opening strokes stand with raised ultra; the closing marks are two strokes after stonienne. The line below ultra bends toward stonienne and is an insertion leader, not a lexical hyphen.','insertion or placement',crop='01_opening',cc=False)
diff('Opening ultra, distinct curved insertion leader','','','Figure R3-02, curved leader beneath raised ultra','The curved line is separate from the letters and has a right-hand upward end and left-hand downward turn.','drawing or diagram',crop='01_opening')
diff('Opening after Sup',r'\unsure{quelc.}','quelc.','quelc.','Long descending initial q, a compressed u/e sequence, tall l, short final c and detached point are visible.','other',crop='01_opening',ch=False)
marginC=C.split('\\margin{',1)[1].split('\n\n\\deleted',1)[0]
marginR=reading.split('\\margin{',1)[1].split('\n\n\\deleted',1)[0]
diff('Entire long oblique left note',r'\margin{'+marginC,'',r'\margin{'+marginR,'The oblique note contains the ensembliste qualification, E and Sigma statement, Stone phrase, proof reservation and formula. H offers only an editorial description and quoted fragments, not a diplomatic transcription. Local R3 differences from C are listed separately.','omission',confidence='medium',crop='07_margin_top',bbox=[20,155,585,1650],cc=False)
diff('Oblique note before le compactifié',r'\unsure{on trouve|on trouvera|on retrouve}','',r'\unsure{on trouvera|on trouve}','The verb begins directly with a crossed t after on; there is no distinct re group before it. The long run and a small terminal curve do not securely settle trouve versus trouvera.','misread word',confidence='low',crop='08_margin_middle',ch=True)
diff('Oblique note after je',r'ne vois','',r'\unsure{ne vois}','The rightward/upward continuation is crowded by the horizontal prose and not fully framed in my note crops. I cannot claim ne vois as certain and do not supply pas.','other',confidence='low',crop='11_margin_upper_right_tail',bbox=[330,730,585,1100],cc=True,ch=True)
diff('Main supports paragraph, first word',r'\unsure{Donc}',r'\ill{}','Donc','The initial closed D and the continuing reduced onc group are present below the struck line.','readable ink left as \\ill{}',crop='02_supports')
diff('Main supports paragraph, verb',r"\unsure{s'identifient|s'identifieraient}",r"s'identifient",r"\unsure{s'identifient|s'identifieraient}",'There is a clear s-apostrophe/i beginning and f descender, but the compressed final run does not establish which inflection is written.','other',confidence='medium',crop='02_supports',cc=False)
diff('Main supports paragraph, aux through spectre',r'aux \unsure{Parties|Partie} à la fois ouvertes et fermées du spectre',r'aux \ill{} \ill{} et \ill{} \ill{} espace',r'aux \unsure{Parties|Partie} à la fois ouvertes et fermées du spectre','The two lines give Parties/Partie, à la fois, ouvertes et fermées, then du spectre. H’s espace at the end of this span is not the visible spectre. The final s of Parties remains compressed.','readable ink left as \\ill{}',confidence='medium',crop='02_supports',cc=False)
diff('Before compact abbreviation: cancelled group',r'\deleted{\unsure{to|tot}}','',r'\deleted{\unsure{to|tot}}','A distinct small t/o-like group immediately precedes the live abbreviation and is crossed; no confident extra full word is recoverable.','omission',confidence='low',crop='03_compact',cc=False)
diff('Main supports paragraph, live compact word',r'\unsure{compact|cpct}',r'\ill{}',r'\unsure{cpct|cpt|compact}','The visible group is very short: an opening c-like rise, a pronounced p descender, and a terminal t; a small intermediate c is possible. I prefer an abbreviation and retain the longer reading as uncertain.','abbreviation expanded or spelling modernised',confidence='medium',crop='03_compact')
diff('After compact abbreviation: cancelled tot group',r'\deleted{\unsure{tot}}','',r'\deleted{\unsure{tot}}','A separate crossed group with two t-like uprights stands before disconnexe. Its lettering stays uncertain.','omission',confidence='low',crop='03_compact',cc=False)
diff('Main supports paragraph, disconnexe',r'\unsure{disconnexe}','discontinu',r'\unsure{disconnexe}','The initial dis/c strokes and terminal crossing/return support disconnexe; the reduced centre remains uncertain. The ending is not a secure inu sequence.','misread word',confidence='medium',crop='03_compact',cc=False)
diff('Between ultra and stonien',r'ultra\unsure{.|-}stonien.','ultra-stonien.','ultra.stonien.','A short detached diamond-like point separates the two words. It is much shorter than a dash; the terminal full stop is also present.','other',crop='03_compact')
diff('Full involution sentence',r"L'involution correspond au passage au complémentaire.",r"\ill{} correspondant au passage \ill{} l'inclusion \ill{}",r"L'involution correspond au passage au complémentaire.",'The two horizontal lines read L’involution correspond au passage / au complémentaire. The first noun is not inclusion, and correspond has no ant ending.','readable ink left as \\ill{}',source=ha,bbox=[330,760,1655,1015],cc=False)
diff('Beginning of last main paragraph, before la construction','On fera attention que',r'\ill{}','On fera attention que','On, fera, attention, and que are visible in the main horizontal line; neighbouring diagonal strokes belong to the margin note.','readable ink left as \\ill{}',source=ha,bbox=[385,1030,1265,1145],cc=False)
diff('Last main paragraph, construction through de l’ens',r'la construction $\Sigma$ ne dépend que de',r'la construction \ill{} $\Sigma$ en \ill{} que \ill{}',r'la construction $\Sigma$ ne dépend que de','The lines give construction, Sigma, ne dépend que de. The short first word after Sigma begins n and ends e, rather than en.','readable ink left as \\ill{}',source=ha,bbox=[450,1020,1650,1230],cc=False,math=True)
diff('Last main paragraph, ens point',"l'ens ordonné", "l'ens. ordonné", "l'ens ordonné",'No separate point follows the reduced ens before ordonné.','text not on the page',crop='04_relation_insertion',cc=False)
diff('Ambient letter immediately after ordonné',r'$M$',r'$\mathcal{M}$',r'$M$','The letter has two plain peaks without a separate script flourish.','misread symbol or index',crop='04_relation_insertion',cc=False)
diff('Compatibility insertion, wording before R',r'\inserted{muni de la relation',r'\add{et de la relation',r'\inserted{muni de la relation','The raised clause begins with the reduced but distinct muni, then de la relation. H’s et is not the initial word. The entire clause is raised.','misread word',crop='04_relation_insertion',cc=False)
diff('Compatibility insertion, relation alphabet',r'\unsure{\mathcal R|R}',r'R',r'\mathcal R','The relation glyph has a broad looping bowl and a returning stroke, unlike the straighter R in the tuple.','misread symbol or index',crop='04_relation_insertion')
diff('Compatibility insertion, long connector','','','Figure R3-03, long curved line beneath the entire compatibility clause','A line begins just after M, curves upward under the phrase, and turns upward at its far right.','drawing or diagram',crop='04_relation_insertion')
diff('Lower addition before la famille',r'\inserted{\unsure{toute|toutes}}',r'\add{toutes}',r'\inserted{\unsure{toute|toutes}}','The lower word is placed before la. A final independent s is not secure; the word is not confidently toutes.','other',confidence='medium',crop='05_toute_phi',cc=False)
diff('Lower addition, enclosing caret/arm','','','Figure R3-03, smaller curved insertion enclosure above the lower toute(s)','The short enclosure rises to a peak between connaître and la, then runs down over the added word with hooked ends.','drawing or diagram',crop='05_toute_phi')
diff('Following connaître, family wording','la famille des parties','les parties','la famille des parties','The baseline has la famille, followed on the next line by des parties. This is not simply les parties.','omission',crop='05_toute_phi',cc=False)
diff('Phi after parties',r'\unsure{\overline\Phi|\Phi\'|\Phi}',r'\Phi',r'\unsure{\overline\Phi|\Phi\'|\Phi}','The Phi has a thick, short high mark displaced to its upper right. Its relation to Phi is uncertain; bare Phi alone suppresses visible ink.','misread symbol or index',confidence='medium',crop='05_toute_phi',cc=False,math=True)
diff('Ambient M after Phi',r'$M$',r'$\mathcal{M}$',r'$M$','The visible M has the same plain two-peaked form as the earlier main-text M.','misread symbol or index',crop='05_toute_phi',cc=False)
diff('Tuple in terms of',r'$(M,\leq,R)$',r'$(\mathcal{M}, \leq, R)$',r'$(M,\leq,R)$','M is plain. Both commas and the less-than-or-equal sign are present; the tuple R has a simple upper bowl.','misread symbol or index',source=hb,bbox=[485,400,830,510],cc=False)
diff('Before final definition: M prime and M',r"une partie $M'$ de $M$",r"une partie $\mathcal{M}'$ de $\mathcal{M}$",r"une partie $M'$ de $M$",'Both letters have the plain peaked form; the first has a distinct high prime.','misread symbol or index',source=hb,bbox=[295,490,1075,615],cc=False)
diff('Definition operator',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosupp}',r'\operatorname{cosup}','After cosu there is one descending p stroke before the lowered M, not two.','abbreviation expanded or spelling modernised',crop='06_set_definition')
diff('Definition, all M occurrences',r"_M(M')=\{x\in M\mid(x,x')\in\mathcal R\quad\forall x'\in M'\}",r"_{\mathcal{M}}(\mathcal{M}') = \lbrace X \in \mathcal{M} \mid (X, X') \in R \ \forall X' \in \mathcal{M}' \rbrace",r"_M(M')=\{x\in M\mid(x,x')\in\mathcal R\quad\forall x'\in M'\}",'All four M letters are plain. The operator subscript is distinctly lowered; both M-primes are high short strokes. X/x and relation differences in this same span are separately identified below.','misread symbol or index',crop='06_set_definition',cc=False)
diff('Definition, element letters',r"x\in M\mid(x,x')\in\mathcal R\quad\forall x'\in M'",r"X \in \mathcal{M} \mid (X, X') \in R \ \forall X' \in \mathcal{M}'",r"x\in M\mid(x,x')\in\mathcal R\quad\forall x'\in M'",'The crossing letters are short relative to M and belong to the lowercase x form at each occurrence. Renaming alone does not change the mathematical object.','misread symbol or index',crop='06_set_definition',cc=False)
diff('Definition, relation glyph',r'\mathcal R',r'R',r'\mathcal R','A large outer oval returns around the vertical/diagonal R strokes. It is markedly curled relative to the tuple R.','misread symbol or index',crop='06_set_definition',cc=False)
diff('Foot note, beginning through first colon',r'\uline{Ex} de ``supports\'\', ou parties saturées de $M$ :',r'\emph{Ex} des supports : parties saturées de $\mathcal{M}$ :',r'\uline{Ex} de ``supports\'\', ou parties \unsure{saturées|saturees} de $M$ :','Ex is singly underlined; de has no final s; supports has paired quotation strokes, then a comma and ou. The first M is plain. The reduced accent in saturées is not secure.','misread word',confidence='medium',crop='10_footnote',cc=False)
diff('Foot note, accent in saturées','saturées','saturées',r'\unsure{saturées|saturees}','The word is readable, but the small acute stroke above its reduced middle is not securely distinguishable in the light ink. I preserve the accent doubt.','other',confidence='low',crop='10_footnote')
diff('Foot note, les comp. connexes',r'les comp. connexes de $M$',r'\ill{} comp. conn. de $\mathcal{M}$',r'les comp. connexes de $M$','Les is visible in light ink; comp. has a detached point. Connexes is written out, including a crossing near the end, and M is plain.','readable ink left as \\ill{}',crop='10_footnote',cc=False)
diff('Foot note, long rule','','','Figure R3-04, long slightly rising rule beginning near connexes','A separate long line runs rightward from the connexes area. H describes it in an editorial note but neither witness actually draws it. It does not cancel the note.','drawing or diagram',crop='10_footnote')

CD=[]
def doubt(loc,c,r,status,shows,crop=None,bbox=None,source=None):
 ci=cm.get(crop) if crop else None
 CD.append(dict(location=loc,c=c,reading=r,status=status,scan_shows=shows,crop=ci['path'] if ci else None,bbox=bbox or (ci['bbox'] if ci else None),bbox_image=source or (ci['source'] if ci else whole)))
doubt('First paragraph, quelc.',r'\unsure{quelc.}','quelc.','resolved','Descending q, tall l, short c and terminal point are separable.','01_opening')
doubt('Oblique note, cancelled word after donnés',r'\deleted{\unsure{tout}}',r'\deleted{\unsure{tout}}','retained','The short crossed group intersects the descender of types; tout remains only a possible reading.','07_margin_top')
doubt('Oblique note before compactifié',r'\unsure{on trouve|on trouvera|on retrouve}',r'\unsure{on trouvera|on trouve}','revised','A crossed t follows on directly; the ending does not settle the tense. No distinct re prefix is visible.','08_margin_middle')
doubt('Oblique note, je',r'\unsure{je}',r'\unsure{je}','retained','A descending loop is present, but the reduction does not securely separate both letters.','09_margin_lower')
doubt('Oblique note, prouver',r'\unsure{prouver}',r'\unsure{prouver}','retained','Initial p and a long reduced remainder are present. Individual medial letters are not all recoverable.','09_margin_lower')
doubt('Oblique display, additional opening hook',r'\unsure{(|\{}',r'\unsure{(|\{}','retained','An extra curved hook precedes the first factor parenthesis; its exact bracket identity stays open.','09_margin_lower')
doubt('Oblique display, terminal mark',r'\unsure{.|,|)}',r'\unsure{.|,|)}','retained','The final factor is legible, but a nearby curved stroke overlaps horizontal body lettering. I cannot identify a secure independent punctuation or delimiter. Crop 11 contains the endpoint; crop 09 did not.','11_margin_upper_right_tail')
doubt('Main supports paragraph, Donc',r'\unsure{Donc}','Donc','resolved','D has a distinct loop and its final reduced nc run is visible beneath the cancellation.','02_supports')
doubt('Main supports paragraph, s’identifient',r"\unsure{s'identifient|s'identifieraient}",r"\unsure{s'identifient|s'identifieraient}",'retained','The final horizontal run is too compressed to settle the inflection.','02_supports')
doubt('Main supports paragraph, Parties',r'\unsure{Parties|Partie}',r'\unsure{Parties|Partie}','retained','Initial capital P is clear; the reduced terminal trace could contain s.','02_supports')
doubt('Before compact abbreviation',r'\deleted{\unsure{to|tot}}',r'\deleted{\unsure{to|tot}}','retained','A crossed t/o-like group is distinct from the live following word; its final t is not secure.','03_compact')
doubt('Live compact abbreviation',r'\unsure{compact|cpct}',r'\unsure{cpct|cpt|compact}','revised','A short c-like opening, p descender, possible c and final t favour abbreviated cpct/cpt.','03_compact')
doubt('After compact abbreviation',r'\deleted{\unsure{tot}}',r'\deleted{\unsure{tot}}','retained','Two t-like ascenders and heavy crossing remain; no more definite lettering is justified.','03_compact')
doubt('Disconnexe',r'\unsure{disconnexe}',r'\unsure{disconnexe}','retained','The initial and final strokes support this word, but its reduced centre is not wholly legible.','03_compact')
doubt('Ultra separator',r'ultra\unsure{.|-}stonien.','ultra.stonien.','resolved','The separator is a compact point rather than a sustained horizontal dash.','03_compact')
doubt('Compatibility insertion R',r'\unsure{\mathcal R|R}',r'\mathcal R','resolved','The bowl wraps round into a broad loop; it is locally distinct from the plainer tuple R.','04_relation_insertion')
doubt('Lower insertion toute(s)',r'\inserted{\unsure{toute|toutes}}',r'\inserted{\unsure{toute|toutes}}','retained','The lower caret points before la; there is no secure independent final s.','05_toute_phi')
doubt('High mark above Phi',r'\unsure{\overline\Phi|\Phi\'|\Phi}',r'\unsure{\overline\Phi|\Phi\'|\Phi}','retained','A short dark horizontal mark is high and displaced to the right; bar, prime, or nonletter mark remain possible.','05_toute_phi')
doubt('Definition operator',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','Only one final p descender is visible before lowered M. This also disposes of both repeated C_context cosup/cosupp checks.','06_set_definition')
doubt('C_context quotation check: ultra and ensembliste',r'``ultra ... stonienne\'\'; ``le cas ensembliste\'\'',r'``ultra ... stonienne\'\'; ``le cas ensembliste\'\'','resolved','Paired short strokes are visible at both ends of each quoted expression; ultra’s opening pair is raised with the insertion.','07_margin_top',bbox=[20,155,1655,760])
doubt('C_context E, E-disc and Sigma',r'E, E_{\mathrm{disc.}}, \Sigma',r'E, E_{\mathrm{disc.}}, \Sigma','resolved','The E has three arms, disc. is below the E baseline, and Sigma is angular. The lowered point after disc is visible in crop 09.','09_margin_lower',bbox=[20,570,565,1370])
doubt('C_context wedge/vee, and P Q R letters',r'P\wedge(Q\vee R)=(P\wedge Q)\vee(P\wedge R)',r'P\wedge(Q\vee R)=(P\wedge Q)\vee(P\wedge R)','resolved','The conjunction marks point upward and the disjunction marks downward; P, Q and R have distinct bowls/tails. Extra opening/terminal marks are retained separately.','09_margin_lower')
doubt('C_context tuple R versus curled relation in set',r'(M,\leq,R);\ (x,x\')\in\mathcal R',r'(M,\leq,R);\ (x,x\')\in\mathcal R','resolved','The tuple R has a short bowl and simple stem; the final set relation has an outer oval and returning leg. No inference from compatibility was needed.','06_set_definition',bbox=[485,1500,1675,1815])
doubt('C_context small x, comma and primes',r"(x,x'),\ \forall x'\in M'",r"(x,x'),\ \forall x'\in M'",'resolved','The comma has a downward tail; both x primes and the final M prime stand high. The signs are small x, not capital X.','06_set_definition')
doubt('C_context je ne vois versus possible pas',r'\unsure{je} ne vois comment \unsure{prouver}',r'\unsure{je} \unsure{ne vois} comment \unsure{prouver}','revised','No pas is supplied. My rotated note crops do not fully settle the upward continuation after je, so ne vois is explicitly uncertain rather than accepted from C.','11_margin_upper_right_tail',bbox=[330,730,585,1100])

remaining=[
('Oblique cancelled word after donnés',r'\deleted{\unsure{tout}}',['tout'], 'low','Crossing and the types descender obscure the short group.'),
('Oblique verb before compactifié',r'\unsure{on trouvera|on trouve}',['on trouvera','on trouve'],'low','The crossed t is distinct; the ending is compressed.'),
('Oblique je',r'\unsure{je}',['je'],'medium','The lone descending loop does not separate both letters.'),
('Oblique ne vois',r'\unsure{ne vois}',['ne vois'],'low','Rightward/upward continuation is not securely framed/separated from the horizontal prose; no pas added.'),
('Oblique prouver',r'\unsure{prouver}',['prouver'],'medium','Only initial p and broad remainder can be read confidently.'),
('Oblique equality extra opening mark',r'\unsure{(|\{}',['(',r'\{'],'low','An extra hook precedes an otherwise clear opening factor parenthesis.'),
('Oblique equality terminal mark',r'\unsure{.|,|)}',['.',',',')'],'low','The endpoint lies among crossing main-text strokes; ownership and punctuation remain uncertain.'),
('Main supports verb',r"\unsure{s'identifient|s'identifieraient}",["s'identifient","s'identifieraient"],'medium','The reduced ending does not settle the inflection.'),
('Main capital Parties',r'\unsure{Parties|Partie}',['Parties','Partie'],'medium','The final s may be reduced to the short last trace.'),
('Cancelled group before compact',r'\deleted{\unsure{to|tot}}',['to','tot'],'low','The last possible t is crossed and crowded.'),
('Live compact abbreviation',r'\unsure{cpct|cpt|compact}',['cpct','cpt','compact'],'medium','Short live group favours abbreviation; exact medial c is uncertain.'),
('Cancelled group after compact',r'\deleted{\unsure{tot}}',['tot'],'low','Heavy crossing through two t-like ascenders.'),
('Main disconnexe',r'\unsure{disconnexe}',['disconnexe'],'medium','Reduced centre remains unclear.'),
('Lower inserted toute(s)',r'\inserted{\unsure{toute|toutes}}',['toute','toutes'],'medium','No secure separate terminal s.'),
('High mark at Phi',r'\unsure{\overline\Phi|\Phi\'|\Phi}',[r'\overline\Phi',r"\Phi'",r'\Phi'],'medium','High mark is detached to the upper right; exact function is unclear.'),
('Foot note saturées accent',r'\unsure{saturées|saturees}',['saturées','saturees'],'low','Faint accent cannot be isolated securely.')]
RD=[dict(location=a,reading=b,alternatives=c,confidence=d,reason=e) for a,b,c,d,e in remaining]

inv=[]
def item(el,kind,pos,words):inv.append(dict(element=el,kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
item('I01','text','top centre','68')
item('I02','text','upper main block','engendrée par la réunion) Je ... algèbre de Boole')
item('I03','deletion','upper right, after Je','dis')
item('I04','insertion','above dis','présume')
item('I05','drawing','from raised présume to its insertion gap','curved descending leader; Figure R3-01')
item('I06','insertion','above stonienne, near upper left of main block','``ultra')
item('I07','drawing','under raised ultra','curved insertion leader; Figure R3-02')
item('I08','margin note','long diagonal left note','Cela sera valable dans ``le cas ensembliste\'\'')
item('I09','deletion','within diagonal note after donnés','tout, uncertain')
item('I10','display','end of diagonal note','P,Q,R; P wedge (Q vee R) = ...')
item('I11','deletion','across main block below opening','Il faudra y revenir')
item('I12','text','main paragraph below cancellation','Donc les supports ... ultra.stonien.')
item('I13','deletion','before compact abbreviation','to/tot')
item('I14','deletion','after compact abbreviation','tot')
item('I15','text','middle, two horizontal lines','L’involution correspond au passage au complémentaire.')
item('I16','text','lower main paragraph','On fera attention que la construction Sigma ... défini par')
item('I17','insertion','above line after M','muni de la relation calligraphic R de compatibilité')
item('I18','drawing','beneath whole compatibility insertion','long line with curved ends; Figure R3-03')
item('I19','insertion','below connaître / before la famille','toute/toutes')
item('I20','drawing','over lower toute(s)','peaked curved insertion enclosure; Figure R3-03')
item('I21','display','lower main block','cosup_M(M prime) = { x in M | ... }')
item('I22','margin note','foot, oblique upward to right','underlined Ex de ``supports\'\', ou parties saturées de M')
item('I23','drawing','from connexes region rightward','long slightly rising rule; Figure R3-04')

report=dict(reader='R3',cote='156-4',scan='69',brief_version='v05',started_utc='2026-11-20T10:41:43Z',finished_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),image_views=meta['images'],reading_file=str(root/'reading.tex'),differences=D,c_doubts=CD,inventory=inv,remaining_doubts=RD,
notation=[
 dict(sign='ambient M',latex='M',appearance='Plain two-peaked capital, including primes and operator subscript.',location='Main construction paragraph, set display, foot note',alternatives=[]),
 dict(sign='relation R',latex=r'\mathcal R',appearance='Broad outer loop and returning diagonal; tuple R is plainer.',location='Raised compatibility insertion and displayed membership; tuple comparison',alternatives=[]),
 dict(sign='Phi and high mark',latex=r'\unsure{\overline\Phi|\Phi\'|\Phi}',appearance='Oval around upright, lower base stroke, short thick mark high to the right.',location='After parties',alternatives=[r'\overline\Phi',r"\Phi'",r'\Phi']),
 dict(sign='cosup',latex=r'\operatorname{cosup}',appearance='One final descending p before lowered M.',location='Bottom set definition',alternatives=[]),
 dict(sign='E disc',latex=r'E_{\mathrm{disc.}}',appearance='Three-armed E, disc and its point placed low.',location='Long oblique note before Dans',alternatives=[]),
 dict(sign='small x and primes',latex=r"(x,x'),\forall x'\in M'",appearance='Small crossing x; high primes and low comma.',location='Bottom set definition',alternatives=[]),
 dict(sign='wedge / vee',latex=r'\wedge,\vee',appearance='Pointed upper conjunctions and lower disjunctions.',location='Oblique equality',alternatives=[]),
 dict(sign='extra hook and terminal mark',latex=r'\unsure{(|\{} ... \unsure{.|,|)}',appearance='Extra curved opening and uncertain terminal stroke amidst crossing prose.',location='Oblique equality right side',alternatives=['opening parenthesis','opening brace','point','comma','closing parenthesis'])],
abbreviations=[dict(form='quelc.',expansion='quelconques'),dict(form='ens',expansion='ensemble'),dict(form='top.',expansion='topologique'),dict(form='disc.',expansion='discret'),dict(form='cpct / cpt',expansion='compact (abbreviated reading uncertain)'),dict(form='Ex',expansion='exemple'),dict(form='comp.',expansion='composantes')],
notes=dict(summary='Handwritten continuation about a presumed Boolean algebra of supports, a qualification in a long diagonal note, and a cosupport definition from the ordered set plus compatibility. The final example concerns connected components.',math_reading_decisions='The paired wedge/vee pattern prompted close reading of each small sign; no sign was corrected from an expected distributive law. Comparing only this page’s tuple and set relation helped distinguish the locally plainer R and curled relation. No theorem was proved or formally checked.',author_checks='The author writes “Je [dis cancelled] présume”, cancels “Il faudra y revenir”, and raises a proof difficulty for the three-support formula. My transcription retains the uncertain “je ne vois comment prouver” wording without supplying pas.',title_dates_pagination='Manuscript number 68 at top centre; scan marker 69 retained. No title or date. No cote marker added. H editorial descriptions are treated as commentary, not literal manuscript text.'),
check_events=[],crops=crops,
workflow_feedback=['The tightly overlapping oblique note makes axis-aligned crop framing difficult. Crop 09 did not contain its upper-right continuation; crop 11 addressed the still-open tail, but ne vois remains incompletely framed. No clipped boundary was used as evidence of absence.','A single local crop often serves several adjacent doubts in one crowded line. This was recorded explicitly; no whole or supplied half was re-viewed, and no decided locus was recropped.'])
# Correct textual apostrophes in strings assembled with raw-string escaping.
def clean(v):
 if isinstance(v,str):return v.replace("\\'", "'")
 if isinstance(v,list):return [clean(x) for x in v]
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
 return v
report=clean(report)
for row in report['differences']:
 if row['kind'].startswith('readable ink left as'): row['kind']='readable ink left as \\ill{}'
 if row['id'] in ['R3-D06','R3-D36']: row['change_c']='yes'
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (root/'inspection_log.md').open('a') as f:
 f.write('\nEvidence decisions: one-p cosup; plain M; lowercase x; curled relation in insertion/set versus plainer tuple R; dot between ultra and stonien. Retained all crowded word and bracket doubts. New uncertainty on ne vois reflects incomplete framing, and an accent doubt remains in saturées.\n')
 f.write('No OCR, external research, other reader/page inspection, delegation, or LaTeX compilation. Only structural text/JSON checks follow.\n')
 f.write('\nFull crop transforms:\n')
 for c in crops:f.write(f"- {Path(c['path']).name}: source {c['source']}; bbox {c['bbox']}; scale {c['scale']}; rotation {c['rotation']} degrees; {c['transform_order']}.\n")
print('differences',len(D),'C dispositions',len(CD),'remaining doubts',len(RD),'inventory',len(inv),'crops',len(crops))
