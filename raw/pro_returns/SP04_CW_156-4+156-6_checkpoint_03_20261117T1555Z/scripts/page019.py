from author import Page
p=Page('156-4',19)
p.replace(r'\unsure{raffiner en}',r'\unsure{raffiner en|raffinement}')
p.replace(r'\unsure{renforcer}',r'\inserted{renforcer}')
p.replace(r'\uline{\unsure{Contr|Cond}}',r'\uline{Contr}')
p.replace(r'\unsure{F_{\grave e l}|F_{\acute e l}|F_{el}}',r'\mathcal{F}_{\grave e l}')
p.replace(r"l'ens \unsure{des}","l'ens des")
p.replace(r'\unsure{F_{el}|X}',r'\mathcal{F}_{el}')
p.replace('F_{el}',r'\mathcal{F}_{el}')
p.replace('F_{\\bar e l}',r'\mathcal{F}_{\bar e l}')
p.replace(r'\unsure{tt}',r'$\forall$')
p.replace(r'\unsure{Leur}','Leur')
p.replace(r'\unsure{géom}','géom')
p.replace(r'\unsure{ses}','ses')
p.replace(r'\unsure{la|les}','la')
p.replace(r"\unsure{Donc|D'où}",'Donc')
p.replace(r'\unsure{Elle|Ell}','Elle')
p.replace(r'\unsure{infinie}','infinie')
p.replace(r"Si $F'$",r"\unsure{Si} $F'$")
p.replace(r"\unsure{\dim F'|\dim F}",r"\dim F'")
p.replace(r'\unsure{\leq|=}',r'\leq')
p.replace(r'\unsure{un peu|un jour|une fois}','un jour')
for word in ['avec','seules','plutôt','contrée']:
    p.replace('\\unsure{'+word+'}',word)
p.replace(r'\unsure{données|donnés}','données')
p.replace(r'$F_{\text{él.}}$',r'$\mathcal{F}_{\text{él.}}$')
p.replace(r'\unsure{\leq}',r'\leq')
p.replace(r'($\leq$), \uline{composantes}',r"($\leq$), \unsure{``connexité''|``constituants''}, \uline{composantes}")
p.change('opening cancelled word','raffiner en?','raffinement','raffiner en|raffinement, deleted','Two f ascenders survive; cancellation suppresses the low ending and its spacing.','top',dc=True,kind='misread word',confidence='low')
p.doubt('opening cancelled word','raffiner en|raffinement','Ending obscured by heavy horizontal strike','top',confidence='low')
p.change('opening replacement','renforcer? on baseline','renforcer inserted','renforcer inserted','Word has initial ren and tall f, positioned above the end of the cancelled word.','top',dc=True,dh=False)
p.change('opening final cancellation','illegible 1','deleted dash','illegible 1, deleted','Short black overdrawn patch retains no separable letters.','top',kind='deletion state (struck given live or live given struck)',confidence='low')
p.doubt('opening final cancellation','illegible 1','Thick black patch physically conceals its underlying text','top',confidence='low')
p.change('first Contr₂ heading','Contr|Cond','Contr','Contr','Tall t crossing and terminal r visible before the small 2.','top',dc=True,dh=False)
p.change('first premise, family index','F_èl|F_él|F_el','fraktur F_él',r'\mathcal{F}_{\grave e l}','Curving family glyph; separate short accent falls leftward above e.','top',dc=True,kind='misread symbol or index',confidence='medium')
p.change('first premise, connective','alors','dans','alors','Initial a followed by tall l and low ors sequence.','top',kind='misread word')
p.change('first premise, des','des?','ill','des, deleted with block','Small d loop and e/s traces remain below the stroke.','top',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.change('first block, small lower-left text','X′ << X?','ill','X′ << X?','Several angular strokes and a prime survive but the cancellation crosses the relation.','topdelete',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
p.doubt('first block, lower-left formula','X′ << X','Overlapping oblique and horizontal cancellations prevent secure separation','topdelete',confidence='low')
p.change('cancelled set, membership family','F_el','fraktur F_él',r'\mathcal{F}_{el}','Low el with no detached acute follows the curved family letter.','top',dc=True,kind='misread symbol or index',confidence='medium')
p.change('cancelled set, right-hand object','F_el|X','fraktur F_él',r'\mathcal{F}_{el}','Tall stem, crossbar, hooked bottom and small el are visible; not a pair of X diagonals.','top',dc=True,kind='misread symbol or index',confidence='medium',consequential='The abandoned clause retains X′ << family_el as written.')
p.change('second condition, quantifier','tt?','forall','forall','Two arms with a curved lower join and a crossbar form the handwritten universal sign.','condition',dc=True,dh=False,confidence='medium')
for place,final in [('second condition, first family',r'\mathcal{F}_{\bar e l}'),('second condition, primed membership',r'\mathcal{F}_{el}')]:
    p.change(place,'F with indicated index','fraktur F_él',final,'Curving family letter; first index has a horizontal mark above e, second has no distinct acute.','condition',dc=True,kind='misread symbol or index',confidence='medium')
for place,crop in [('first crossed premise X','top'),('second condition initial X','condition'),('second condition raffinent X','condition')]:
    p.change(place,'X','bold X','X','Crossed diagonal glyph; the last occurrence is retraced, without a distinct new letter shape.','top' if crop=='top' else 'condition',kind='misread symbol or index',confidence='medium')
p.change('cancelled restriction','tels que','tel que','tels que, deleted','Final small s before the long q descender survives the cancellation.','condition',kind='misread word',confidence='medium')
p.change('boundedness verb','sont majorées','est majorée','sont majorées','The verb begins with low s and ends in nt; final word extends through ées.','condition',kind='misread word')
p.change('dimension opening','Leur?','[ill deleted] Leur','Leur','Tall L and low eur are live; the nearby crossing belongs to the cancelled oblique note.','dimension',dc=True,kind='deletion state (struck given live or live given struck)')
p.change('dimension inserted abbreviation','géom?','géom.','géom','Inserted parenthesized word ends in m immediately before the closing curve; no separate terminal dot.','dimension',dc=True,kind='abbreviation expanded or spelling modernised',confidence='medium')
p.change('dimension underline','dimension (géom) de X underlined','dimension only underlined','dimension (géom) de X underlined','One underline continues beneath de X; inserted parenthesis sits above it.','dimension',kind='insertion or placement')
p.change('before La dim','deleted U?','omitted','deleted U?','Two older vertical strokes with a curved base underlie the new La.','dimension',kind='omission',confidence='low')
p.doubt('before La dim','U','Overwriting leaves the abandoned letter uncertain','dimension',confidence='low')
p.change('after des, cancelled word','ses?','ill before dim géom','ses deleted after des','Small s/e/s sequence lies after des and is crossed horizontally.','dimension',dc=True,kind='insertion or placement',confidence='medium',marked='yes')
p.change('constituents clause','qui la|les constituent','constituantes','qui la constituent','Separate qui, tall l/a, and constituent with two t ascenders are visible.','dimension',dc=True,kind='misread word')
p.change('old oblique note','Donc|D’où la dimension, deleted','Donc la dimension [ill], deleted','Donc la dimension, deleted','Rotated note shows D/o/n/c and la dimension through a single continuous strike, ending there.','oldmargin',dc=True,kind='text not on the page',confidence='medium',marked='yes')
p.change('chain introductory words','C’est donc le sup des longueurs des chaînes','C’est donc le sup [des n] pour [les] longueurs? des chaînes?','C’est donc le sup des longueurs des chaînes','Right-hand first line continues on the small left-hand baseline; no des n or pour insertion is visible.','dimension',kind='text not on the page',marked='yes')
p.change('chain after X₁','X₁ … < Xₙ₋₁','X₁ < … < Xₙ₋₁','X₁ … < Xₙ₋₁','After subscript 1 there are dots, then the one < before Xₙ₋₁.','dimension',kind='misread symbol or index')
p.change('right note opening','Elle|Ell, deleted F?','Elle ill','Elle, deleted F?','E with lower bar followed by ll/e; an overwritten F follows it.','edge',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.doubt('right note deleted glyph','F','Heavy overtrace leaves the letter uncertain','edge',confidence='low')
p.change('right note finiteness','peut être infinie pour F infinie?','ill fragments','peut être infinie pour F infinie','Tall p and f stems plus low inf/inie sequence recur in the two short lines.','edge',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.change('right note condition','Si F′ raffine F','F raffine F fragment','Si? F′ raffine F','Prime after first F is visible; tiny initial connective remains compressed.','edge',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.doubt('right note initial connective','Si','Tiny connective beside the descender is not fully separated','edge')
p.change('right note inequality','dim F′|dim F ≤|= dim F','élément ill subdivision fragment',r"\dim F'\leq\dim F",'Raised prime follows first F; below it an angular upper stroke with a lower bar precedes dim F.','edge',dc=True,kind='misread symbol or index',confidence='medium',marked='yes',consequential='The margin retains dim F′ ≤ dim F with a visible prime on the first F.')
p.change('dated paragraph, verb','On aurait pu développer','On aurait pu dire ill','On aurait pu développer','Long d loop and subsequent évelopper descenders remain on the main baseline.','laterwords',kind='readable ink left as \\ill{}',marked='yes')
p.change('dated paragraph, time phrase','un peu|un jour|une fois','un ill','un jour','After un a long j descender is followed by low our; no second-word p loop.','laterwords',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
for place,C,H,final,evidence in [
('notions','les notions','la notion','les notions','Plural les and final s on notions.'),
('constructible phrase','de ``partie constructible’’','de parties [ill] constructibles','de ``partie constructible’’','Singular partie and constructible enclosed by two-stroke quotation marks.'),
('adhérence','adhérence','admissions with cancellations','adhérence','Tall d/h and final rence sequence; live baseline.'),
('intérieur','intérieur','ill and figure fragments','intérieur','Initial i/n/t and accent over the following e; no strike.'),
('frontière','frontière','constructibles? with cancellations','frontière','Initial f descender and crossed t, followed by ière.'),
('composantes connexes','composantes connexes','comme … ill fragments','composantes connexes','Words span consecutive main lines, with long p descender then repeated n/x sequence.'),
('associated figure','associés à une figure','d’une figure … à une figure fragments','associés à une figure','One continuous live main clause; small oblique note crosses it.'),
('data connective','avec?','ill donnée par? ill','avec','Low a/v/e/c sequence at start of the main line.'),
('restriction','seules?','omitted','seules','Low seu and tall l followed by es.'),
('data noun','données|donnés','donnée','données','Final small es and plural s remain on the baseline.')]:
    p.change('dated paragraph, '+place,C,H,final,evidence,'lower',dc=('?' in C or '|' in C),kind='misread word',confidence='medium' if '?' in C or '|' in C else 'high',marked='yes')
p.change('dated paragraph, relation','≤','<<','≤','One angular upper stroke with a separate lower bar, rather than two angles.','lower',kind='misread symbol or index',consequential='The proposed data here use ≤ and compatibility; the closing direction uses <<.')
for word in ['la','un']:
    p.change('dated paragraph, deleted '+word,word+'? deleted','ill or omitted',word+'? deleted','Small crossed group before family glyph; cancellation retains only partial letter contours.','lower',kind='omission',confidence='low',marked='yes')
    p.doubt('dated paragraph, deleted '+word,word,'Crossing prevents secure letter separation','lower',confidence='low')
p.change('dated paragraph, family alphabet','F_él.','fraktur F_él',r'\mathcal{F}_{\text{él.}}','Curved family glyph, accented small él and terminal point.','lower',dc=True,kind='misread symbol or index',confidence='medium')
p.change('lower oblique note, opening','Aussi, la notion de structure de contrée? induite sur une … figure','Aussi? ill figures ill','Aussi, la notion de structure de contrée induite sur une … figure','Rotated line separates Aussi, structure underlined, contrée underlined, and induite sur une.','slanttext',dc=True,kind='readable ink left as \\ill{}',marked='yes',confidence='medium')
p.change('lower oblique note, order sign','≤?','omitted','≤','Small angle with lower bar is visible inside parentheses.','slantend',dc=True,kind='omission',confidence='medium')
p.change('lower oblique note, after order parentheses','omitted','omitted','``connexité’’|``constituants’’?','Small co/n initial and several tall ending strokes followed by closing quotation marks; phrase partly crosses larger writing.','slantend',dc=True,kind='omission',confidence='low')
p.doubt('lower oblique note, after order parentheses','connexité|constituants','Newly retained word has a compressed and overlapping ending','slantend',confidence='low')
for word in ['multistrate|multistr.','sous-figure|sous figure',"d'un",'univers|ensemble','des','points|parties','pour','``disj.\'\'',"d'une",'figure','connexes|maximales','de|des','Aussi']:
    p.change('lower oblique note, '+word,word+'?','ill fragments',word+'?','Small oblique writing crosses the main text; retained candidate cannot be fully resolved from the surviving joins.','slanttext',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
    p.doubt('lower oblique note, '+word,word,'Overlap of baselines and compressed lettering remains unresolved','slanttext',confidence='low')
p.change('lower oblique note, unreadable word','illegible 1','ill fragments','illegible 1','Dense crossing at the word after celle de/des conceals separate characters.','slanttext',kind='readable ink left as \\ill{}',confidence='low',marked='yes')
p.doubt('lower oblique note, unreadable word','illegible 1','Physically overlaid characters remain undecipherable','slanttext',confidence='low')
p.change('closing promise','J’y reviendrai sûrement','ill sérieusement','J’y reviendrai sûrement','Reviendrai lies on the main baseline; adverb has a circumflex over u and short rement, without rieusement.','adverb',kind='misread word',marked='yes')
p.change('closing time phrase','Pour le moment','Pour la peine? ultérieurement','Pour le moment','Pour le ends one main line, moment begins the next; no intervening extra words.','lower',kind='misread word',marked='yes')
p.change('closing deletion','plutôt?','ill deleted','plutôt deleted','Tall p/l/t sequence and circumflex survive the crossing stroke.','lower',dc=True,kind='readable ink left as \\ill{}',confidence='medium',marked='yes')
p.change('closing abbreviation','ds|dans','dans','ds|dans','Initial d and compressed terminal strokes do not settle internal a/n.','lower',confidence='medium',kind='abbreviation expanded or spelling modernised')
p.doubt('closing abbreviation','ds|dans','Compressed middle letters remain undecided','lower')
p.inventory([
('text','header','18'),('text','opening','la'),('deletion','opening','raffiner en|raffinement'),('insertion','above opening','renforcer'),('deletion','end opening','illegible 1'),
('deletion','first condition','Contr₂ Si X ∈ family_èl'),('deletion','first condition end','des'),('deletion','small lower-left formula','X′ << X'),('display','cancelled set','{X′ ∈ family_el | X′ << family_el}'),
('text','second condition','Contr₂ Pour ∀ X'),('deletion','second condition','tels que'),('text','boundedness','Alors les dim. comb.'),
('text','definition','Leur borne sup.'),('insertion','above dimension','(géom)'),('deletion','before La dim','U'),('text','figure dimension','La dim géom d’une figure'),('deletion','after des','ses'),
('margin note','middle left oblique','Donc la dimension, deleted'),('deletion','middle left oblique','Donc la dimension'),
('insertion','between definition and dated paragraph','C’est donc le sup des longueurs des chaînes'),('display','interline chain','X₀<X₁ …<Xₙ₋₁<<Xₙ∈F'),
('margin note','right of chain','Elle peut être infinie'),('deletion','right note after Elle','F'),('margin note','left dated paragraph','(11 juin)'),
('text','dated paragraph','On aurait pu développer un jour'),('deletion','dated paragraph before family','la'),('deletion','dated paragraph before family','un'),
('margin note','lower oblique','Aussi, la notion de structure de contrée'),('text','closing','J’y reviendrai sûrement'),('deletion','closing','plutôt')])
p.notation('universal quantifier',r'\forall','Two upright arms, curved lower joining stroke and horizontal crossbar; follows Pour')
p.notation('family index marks',r'\mathcal{F}_{\grave e l},\mathcal{F}_{\bar e l},\mathcal{F}_{el}','First cancelled premise has leftward accent; live replacement has horizontal mark; other occurrences lack detached accent')
p.r['abbreviations']=[{'abbreviation':a,'expansion':e,'evidence':'Visible on scan 019'} for a,e in [('Contr','contrée / condition (heading)'),('ens','ensemble'),('dim','dimension'),('comb.','combinatoire'),('sup.','supérieure'),('géom','géométrique'),('déf.','définition'),('ds','dans (uncertain reading)')]]
p.save()
