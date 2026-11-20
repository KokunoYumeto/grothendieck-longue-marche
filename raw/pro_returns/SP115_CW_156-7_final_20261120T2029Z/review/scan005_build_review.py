from pathlib import Path
import json
R=Path('/workspace/scratch/ddf8babdc42e')
manifest=json.loads((R/'out/review/scan005_crop_manifest.json').read_text())
changes=[]; ids={}
compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
barred=r'\mathrel{\tikz[baseline=-.45ex,x=.7em,y=.45em]{\draw (0,-.44)--(0,.44) (0,0)--(1.2,0) (1.2,-.44)--(1.2,.44);}}'
def add(key,place,C,H,final,shows,crop,kind='misread word',conf='high',ac=False,ah=True,mh=False,con=True):
 i=f'S005-{len(changes)+1:02d}';ids[key]=i;m=manifest[crop]
 changes.append(dict(id=i,place=place,C=C,H=H,final=final,scan_shows=shows,confidence=conf,kind=kind,crop=m['path'],box=m['box'],against_C=ac,against_H=ah,marked_in_H=mh,consequential=con))
add('page','top centre, overwritten page numeral',r'\mspage{\deleted{\unsure{3}}4}','editorial page 4; note says numeral overwritten',r'\mspage{\deleted{\unsure{3}}4}','The visible final form has the diagonal/cross stroke and long descending stem of 4. Earlier rounded strokes remain under it, but do not permit the 3 doubt to be removed. H does not transcribe the overwritten numeral.','page_number','deletion state (struck given live or live given struck)','low',mh=True,con=False)
add('circles','two circled labels before the M and L entries',r'\textcircled{\scriptsize\unsure{e}}; \textcircled{\scriptsize\unsure{f}}','(e); (f)',r'\textcircled{\scriptsize\unsure{e}}; \textcircled{\scriptsize\unsure{f}}','Both small signs are actually circled. Their interior strokes remain cramped; the inferred sequence e/f does not by itself settle them. The label before L is separately visible in scan005_L_heading.png.','M_heading','other','low',con=False)
add('M','first M and repeated M throughout the page',r'\unsure{M|\mathcal M}, later M',r'\mathcal M',r'\unsure{M|\mathcal M}, later M','The bare capitals consistently have two tall stems with a rounded low valley. The ink does not securely distinguish ordinary cursive M from an intentional calligraphic alphabet. First-occurrence doubt is retained; the first candidate governs repetitions.','M_heading','misread symbol or index','low')
add('F_alphabet','first ambient F and its recurring plain/overlined/tilded forms',r'\unsure{\mathscr F|\mathcal F}, later \mathscr F',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F|\mathfrak F}, later \mathscr F','The ambient letter has a hooked/curved top and a cross-stroke through the stem, unlike the block F used for an individual figure. Its exact typographic alphabet remains uncertain; H\'s blackletter candidate is added explicitly rather than silently adopted.','M_heading','misread symbol or index','low',ac=True)
add('quotes','figures élémentaires, lieux, and sine qua non','paired high ticks, first opening pair doubtful','guillemets','paired high ticks; first opening pair remains doubtful','Closing marks after élémentaires and both pairs around lieux and sine qua non consist of short raised pen ticks. They are not angle-shaped guillemets. The first opening pair is still retained as C\'s doubt.','M_heading','other',con=False)
add('subset_place','M entry, between figures and élémentaires',r'figures $\subset\mathscr F$ élémentaires',r'figures élémentaires ou multistrates $\subset\mathfrak F$',r'figures $\subset\unsure{\mathscr F|\mathcal F|\mathfrak F}$ élémentaires','The subset sign and ambient letter are on the first line immediately after figures. Élémentaires and multistrates follow on the next two baselines. The formula is not written after multistrates.','M_heading','insertion or placement')
add('right_placement','upper right definition, formé des objets…',r'\margin{formé des objets…}','inline continuation after multistrates',r'\margin{formé des objets…}','The definition occupies a separate six-line block on the far right. It is preserved as a marginal block at the M entry rather than moved into the central list line.','right_note','insertion or placement',con=False)
add('right_deleted_F','upper right note, after induites par',r'\deleted{\unsure{$\mathscr F$}}','omitted',r'\deleted{\unsure{$\mathscr F$}}','A small crossed ambient letter is visible immediately after par. It is separate from the live ≤ and ≪ on the next line. Its overwritten strokes do not justify removing the doubt.','right_note','deletion state (struck given live or live given struck)','low')
add('elements','L entry, underlying word beneath lieux',r'\deleted{\unsure{éléments}}','underlying word omitted; lieux emphasized',r'\deleted{\uline{\unsure{éléments}}}','The original baseline word is heavily struck. A separate shorter underline survives below that cancelled word. Lieux stands above it; the underline is not beneath the added word itself. The underlying reading éléments remains doubtful.','L_heading','deletion state (struck given live or live given struck)','medium',ac=True,mh=True)
add('lieux','L entry, above the cancelled word',r'\inserted{``lieux\'\'}','« lieux » as baseline emphasized text',r'\inserted{``lieux\'\'}','Lieux is raised above the old baseline and substitutes for the struck word. Its own letters are not crossed. H lacks the insertion state.','L_heading','insertion or placement')
add('minimaux','L entry, following physical line',r'\deleted{\unsure{minimaux}}','omitted',r'\deleted{\unsure{minimaux}}','A second long cancelled word occupies the lower baseline. Its initial and medial strokes support minimaux, but the crossing obscures enough letters to retain the existing doubt.','L_heading','deletion state (struck given live or live given struck)','low',mh=True)
add('L','L entry, first symbol',r'\unsure{L|\mathcal L}',r'\mathcal L',r'\unsure{L|\mathcal L}','The letter is a looped cursive L. The page alone does not settle ordinary versus calligraphic alphabet; C\'s alternatives remain.','L_heading','misread symbol or index','low')
add('L_definition','right-hand replacement definition of lieux',r'\inserted{connector; éléments minimaux de $\mathscr F\setminus\{\varnothing_{\mathscr F}\}$ pour $\ll$}','inline definition after a colon',r'\inserted{connector; éléments minimaux de $\mathscr F\setminus\{\varnothing_{\mathscr F}\}$ pour $\ll$}','A long bent connector runs from the central correction to the two-line definition at right. The empty-set sign has an oblique slash and the ambient letter is its subscript. No colon is written after lieux.','L_definition','insertion or placement')
add('deployement','upper left marginal note',r'\uline{déployement}',r'\emph{déploiement}',r'\uline{déployement}','After déplo the source has a long descending y stroke crossing the underline. It is not an i; the written spelling déployement is retained.','left_note','abbreviation expanded or spelling modernised')
add('strates_underlines','upper left note, strates at beginning and after ens. de ses','both strates occurrences underlined','neither occurrence marked as emphasized','both strates occurrences underlined','A short horizontal line lies beneath the opening strates. A second underline lies beneath the final strates in ens. de ses strates and meets the note\'s connector.','left_note','omission',con=False)
add('left_punctuation','upper left note, after X≤F and after the set formula','no semicolon or period','semicolon after X≤F; period after the set formula','no semicolon or period','Both formulas end without the extra punctuation supplied by H. The visible vertical stroke after the set brace belongs to the surrounding connector.','left_note','text not on the page',con=False)
add('top_terminal_punctuation','right definitions, ends of the M and L definitions','no terminal semicolon/period','semicolon after the M definition; period after the L definition','no terminal semicolon/period','The final ambient F in the upper block and ≪ in the lower block are followed by blank paper. H\'s closing punctuation is not written.','L_definition','text not on the page',con=False)
add('intro_words','axiom introduction, Les premiers trois…','ne concernent que',r'\add{concernent}; remainder replaced by parenthesis/struck illegibility','ne concernent que','Ne is at the end of the first baseline; concernent que begins the next baseline. The words are live baseline text, not an insertion or cancellation.','axiom_intro','misread word',mh=True)
add('intro_insert','above the end of the first axiom-introduction line',r'\inserted{At~1 - At~3}','parenthesized At 1 – At 3; inserted concernent instead',r'\inserted{At~1 - At~3}','The separate raised phrase consists of At 1 - At 3. There are no parentheses surrounding it. It supplies the numbers after premiers trois.','axiom_intro','insertion or placement')
add('intro_deleted1','beginning of the third introduction line, first cancelled group',r'\deleted{\unsure{At 1}}','omitted in text; editorial note suggests At 4',r'\deleted{\unsure{At 1|At 4}}','The group begins At and ends in heavily crossed digit strokes. They permit 1 or 4; the cancelled digit is not resolved. The H note is treated as a competing reading, not source text.','axiom_intro','deletion state (struck given live or live given struck)','low',ac=True,mh=True)
add('intro_deleted2','third introduction line, second cancelled group',r'\deleted{\unsure{et|4}}','omitted',r'\deleted{\unsure{et|4}}','The second compact cancellation is separate from the first At group and precedes live les. Its descending and cross strokes do not decisively distinguish et from 4.','axiom_intro','deletion state (struck given live or live given struck)','low',mh=True)
add('intro_period','end of axiom introduction','no final period','period after ≪','no final period','No dot follows the final two chevrons.','axiom_intro','text not on the page',con=False)
add('axiomes_plural','slanted margin beside At 1','Axiomes des','Axiome des','Axiomes des','A separate final s stroke follows the e of Axiomes before des. The whole following phrase sommes majorées de figures is underlined over two lines.','margin_at1')
add('equivaut','slanted margin beside At 2','équivaut à','équivalent à','équivaut à','The word ends in the connected aut sequence and final t. It does not contain the longer alent ending.','margin_at2')
add('margin_C','At 2 margin, first formula',r'F,\unsure{C|G}\in\mathscr F',r'F,G\in\mathfrak F',r'F,C\in\mathscr F','The second letter after F, is an open C with a simple lower exit and no internal G hook. The G in the following F≤G has an internal return/leg and supplies a local comparison. The written C is retained despite the following use of G.','margin_at2','misread symbol or index',ac=True)
add('de_figures','At 2 margin, Critère d\'inclusion…','de figures','des figures','de figures','The word between inclusion and figures is de; there is no final s stroke. The underline begins with d\'inclusion, not Critère, and continues through par strates.','margin_at2')
add('capital_Si','At 2 marginal condition and body condition b)','Si at both places','si at both places','Si at both places','Both initials are tall capital S forms. The body instance is also visible in scan005_conditions_ab.png.','margin_at2','misread word',con=False)
add('deleted_d','At 2 main sentence, before est',r'\deleted{\unsure{d}}est','est',r'\deleted{\unsure{d}}est','An underlying loop/ascender has been overwritten at the beginning of est. Its outline remains compatible with d but is not completely separable from the live e, so the doubt stays.','at2','deletion state (struck given live or live given struck)','low')
add('map_caps','Scholie, F to F-tilde',r'\unsure{bar-ended shaft|\mapsto}',r'\mapsto',barred,'The shaft has a short upright at each end. At the right end there is no oblique arrowhead; the complete F–shaft–F-tilde expression was read.','scholie','misread symbol or index',ac=True)
add('raised_family','Scholie, after partie',r'partie $\widetilde{\mathscr F}$',r'partie $\widetilde{\mathfrak F}$',r'partie \inserted{$\widetilde{\mathscr F}$}','The tilded ambient letter is raised into the interlinear space above the end of partie, rather than on its baseline. It is preserved as an added symbol attached there.','scholie','insertion or placement',ac=True)
add('F_of_M','Scholie, ambient family expression',r'\unsure{\mathscr F|\mathscr P}(M)',r'\mathfrak F(\mathcal M)',r'\mathscr F(M)','The initial letter has the same stem and two transverse strokes as the ambient F elsewhere. It lacks a P bowl. The source is transcribed as F(M), without substituting the expected powerset letter.','scholie','misread symbol or index',ac=True,mh=True)
add('ens_scholie','Scholie, M ens ordonné','ens','ens.','ens','The short ens group is followed by a gap and ordonné, with no separate abbreviation point.','scholie','other',con=False)
add('pour','Scholie, ordonné (…)','pour','par','pour','After p the rounded ou sequence precedes the terminal r. The word is longer than par and is written inside the parenthesis before ≤.','scholie')
add('Phi','condition a), first Greek letter',r'\unsure{\Phi|\varphi}',r'\Phi',r'\Phi','The letter has a broad closed loop with a straight central stem and capital height. Its repetitions in b) and c) confirm the same capital Phi form.','conditions_ab','misread symbol or index',ac=True,ah=False)
add('fermes','condition a), final word','fermés',r'\uncertain{fermées}','fermés','The word has a single e before the final s; there is no additional e of fermées. The singular-looking masculine ending is retained as written.','conditions_ab',mh=True)
add('et_parenthesis','below the cancelled start of condition c)',r'\deleted{\unsure{(et}}','not transcribed; editorial note mentions unread parenthetical word',r'(\deleted{\unsure{et}}','The opening parenthesis stands to the left of the short horizontal cancellation and is not crossed. The letters of et are covered by the stroke and remain doubtful. The uncancelled opening parenthesis is retained without inventing a closing one.','condition_c','deletion state (struck given live or live given struck)','medium',ac=True,mh=True)
add('margin_c_text','slanted note beside c)',r'\widetilde{\mathscr F}\neq\varnothing automatique si M\neq\varnothing et dans tous les cas, \unsure{équivaut} à \varnothing\in\widetilde{\mathscr F}',r'\widetilde{\mathfrak F}\neq\varnothing [ill.] [ill.] et donc \varnothing\in\widetilde{\mathfrak F}',r'\widetilde{\mathscr F}\neq\varnothing automatique si M\neq\varnothing et dans tous les cas, \unsure{équivaut} à \varnothing\in\widetilde{\mathscr F}','The rotated crop shows automatique si M≠∅ and et dans tous les cas, with no donc. The final équivaut is light and compressed, so its C doubt is retained. The three-line marginal text is preserved in full.','margin_c','readable ink left as \\ill{}','medium',mh=True)
add('un','following c), un ens de parties',r'\unsure{un|une}','un','un','The word consists of the u/n humps and a terminal exit into a wide gap. There is no following e before ens.','ou_un','misread word',ac=True,ah=False,con=False)
add('ens_ou','following c), un ens de parties','ens','ens.','ens','No separate point follows ens before de.','ou_un','other',con=False)
add('bprime_case','condition b′, quantified variable, superscript and membership variable',r'\forall x\in M; \widetilde{\mathscr F}^{x}; x\in\Phi',r'\forall X\in\mathcal M; \widetilde{\mathfrak F}^{X}; X\in\Phi',r'\forall x\in M; \widetilde{\mathscr F}^{x}; x\in\Phi','The first x is a small cross beside the larger quantifier, the superscript is correspondingly small, and the membership variable repeats it. The later X-tilde is a distinct larger capital. Case is preserved as C reads it.','b_prime','misread symbol or index')
add('ens_bprime','condition b′, l\'ens','ens','ens.','ens','The abbreviation ends before the raised family symbol, without a period.','b_prime','other',con=False)
add('bprime_old_F','condition b′, inside the opening set brace',r'\deleted{\unsure{F}}\Phi',r'\Phi',r'\deleted{\unsure{F}}\Phi','Old angular strokes remain beneath the live Phi. They are not fully separable and the F doubt is retained; H omits the overwritten state.','b_prime','deletion state (struck given live or live given struck)','low')
add('bprime_bar','condition b′, after Phi membership',r'\unsure{\overline{\mathscr F}|\widetilde{\mathscr F}}',r'\widetilde{\mathfrak F}',r'\overline{\mathscr F}','The upper stroke over this F is straight and slightly rising. The first family symbol on the same line has an unmistakably wavy tilde. The complete set expression was inspected, and the straight overbar is retained.','b_prime','misread symbol or index',ac=True)
add('bprime_cancelled_F','condition b′, after plus petit élément',r'\deleted{\unsure{F}}','omitted',r'\deleted{F}','The underlying single F has a clear upright and two primary bars. Several oblique cancellation strokes run to its right/below; they do not conceal the identifying F strokes. This one-letter deleted doubt is resolved.','b_prime','deletion state (struck given live or live given struck)',ac=True)
add('aprime_label','lower primed condition label',r'\unsure{a|c}\prime','d′','a′','The label has a closed low oval and right-hand exit, with no d ascender. The following prime is separate. It is a, not c or d.','a_prime','misread symbol or index',ac=True)
add('aprime_cancel','after a′), before Dans',r'\deleted{\unsure{\forall|F}}','omitted from text; note says cancelled ∀',r'\deleted{\unsure{\forall|F}}','The leading glyph is heavily crossed. Upper converging strokes permit ∀, while the lower upright/barred residue also permits F. Every identifying stroke is not clear, so both C candidates remain.','a_prime','deletion state (struck given live or live given struck)','low',mh=True)
add('toutes','a′), before famille',r'\unsure{toute|toutes}','toute','toutes','After the second t and small e there is a separate downward curling final s. The singular famille that follows does not license removing it.','a_prime','misread word',ac=True)
add('up_arrow','left of b′) and a′)','upward curved arrow','editorial note calls it a brace','upward curved arrow','The upper end has two distinct oblique strokes meeting the shaft as an arrowhead. The lower end curves toward a′) without a second head. It is not a brace; the C tikz-cd arrow is retained.','left_arrow','drawing or diagram')
add('relation_heading','Relation heading','plain Relation',r'\emph{Relation}','plain Relation','There is no separate underline beneath Relation. The two underlines beneath figures and compatibles below the formula are clearly separate strokes.','relation','other',con=False)
add('compat','compatibility sign, all seven source occurrences','custom intersecting-chevron glyph',r'\between',compat,'The glyph consists of two opposing broken chevrons whose crossed strokes enclose a small central diamond and continue above/below it. C\'s explicit TikZ reproduces this visible form. H\'s named symbol is not used to replace the pen shape. All later occurrences were checked in the reconstitution/properties crops.','relation','misread symbol or index')
add('join_C','compatibility definition, F∨C',r'F\vee C',r'F\vee G',r'F\vee C','The letter after ∨ is an open C with a simple lower exit. It does not have the internal return/leg of the clearly written G to the left of the equivalence. The written C is retained.','relation','misread symbol or index')
add('brace_C','compatibility definition, two-element brace',r'\{F,G\}',r'\{F,G\}',r'\{F,C\}','The second letter inside the brace repeats the open C form after ∨ and lacks the internal G stroke visible in the left member of the same equation. Both witnesses give G here; the proposed reading preserves the apparent source C.','relation','misread symbol or index',ac=True)
add('defn','label over the defining equivalence',r'\unsure{défn|defn}','déf',r'\unsure{défn|defn}','A final short n-like connected exit follows the tall f. The accent over the compressed e cannot be isolated securely; the C accent alternatives remain, while H omits the final letter.','relation','abbreviation expanded or spelling modernised','medium')
add('relation_punctuation','compatibility definition and caption','existe i.e.; no final period after figures compatibles','existe, i.e.; period after figures compatibles','existe i.e.; no final period after figures compatibles','No comma occurs in the gap after existe, and no period follows the underlined caption.','relation','text not on the page',con=False)
add('avec_insert','above se reconstitue par',r'\inserted{avec At~1, At~2, At~3}',r'\add{avec (At 1, At 2, At 3)}',r'\inserted{avec At~1, At~2, At~3}','The added phrase is above the baseline. The large curved stroke before At 1 belongs to the f of figures on the line above; the line below At 1…At 3 is the attachment connector, not parentheses. Its left end reaches the gap before se.','reconstitution','insertion or placement')
add('est_deleted','after (ambient F,≤), before se',r'\deleted{\unsure{est}}',r'\struck{\ill{}}',r'\deleted{\unsure{est}}','Several oblique crossing strokes cover a short old word. A faint final t-like stroke supports est, but the full word remains obscured. It is retained as doubtful cancelled ink; the inserted phrase attaches beside it.','reconstitution','readable ink left as \\ill{}','low',mh=True)
add('reflexive_X','first line of the final brace',r'\unsure{X|\forall}\;[compat]\;réflexive symétrique',r'X\;[compat]\;X\;réflexive, symétrique',r'X\;'+compat+r'\;\text{réflexive symétrique}','The first glyph is X: two crossing diagonals with no quantifier bar. Between the compatibility sign and réflexive there is only a gap, not another X. No comma is present between réflexive and symétrique. The whole line and the following implication were inspected.','properties','misread symbol or index',ac=True)

D=[]
def doubt(place,reading,alternatives,reason,confidence='low'):
 D.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
doubt('top page-number overwrite','3',[],'Earlier rounded digit strokes are partly covered by the final 4; the overwritten reading is not fully plain.')
doubt('first circled list label','e',[],'The small enclosed intersecting strokes are too cramped to identify every part securely; sequence alone is not evidence.')
doubt('first bare set capital and its repetitions','M',[r'\mathcal M'],'Rounded cursive M does not securely determine ordinary versus calligraphic alphabet.')
doubt('opening quotation marks before figures','``',[],'The opening pair is crowded against the tall f and the top boundary of this writing; the source quote form is plausible but retained as doubtful.')
doubt('first ambient F and its repeated forms',r'\mathscr F',[r'\mathcal F',r'\mathfrak F'],'The hooked ambient F is distinct from block F, but its exact typographic alphabet remains unsettled.')
doubt('upper right note, cancelled symbol after par',r'\mathscr F',[],'Compact crossing strokes obscure the small underlying letter.')
doubt('second circled list label','f',[],'The enclosed small strokes resemble f but are not fully separable from the circle.')
doubt('first L symbol','L',[r'\mathcal L'],'Looped cursive shape is clear, intentional alphabet is not.')
doubt('cancelled baseline word beneath lieux','éléments',[],'The strike covers the middle letters; the separate underlying underline remains visible.')
doubt('cancelled word below L entry','minimaux',[],'Several letters are obscured by multiple long cancelling strokes.')
doubt('first cancelled group in axiom introduction','At 1',['At 4'],'Digit strokes are crossed; 1 and 4 remain possible.')
doubt('second cancelled group in axiom introduction','et',['4'],'The overlap does not decide a short word versus numeral.')
doubt('At 2, overwritten initial before est','d',[],'Underlying loop/ascender cannot be completely separated from the live e.')
doubt('cancelled short word below c), after live opening parenthesis','et',[],'The horizontal strike conceals the letters; the opening parenthesis itself is not crossed.')
doubt('union subscript in c)',r'\in',['+'],'The small middle mark has insufficient separated strokes to distinguish membership from a plus; the whole union expression was read.','medium')
doubt('last word of second line of lower marginal note','équivaut',[],'The ending is light and compressed, with thin strokes merging into the exit.','medium')
doubt('overwritten symbol under Phi inside b′) set brace','F',[],'The live Phi crosses the old angular strokes; every old stroke is not plain.')
doubt('cancelled glyph before Dans in a′)',r'\forall',['F'],'Heavy crossing permits both C alternatives; no full identification is asserted.')
doubt('superscript label over defining equivalence','défn',['defn'],'The final n is visible, but an acute accent cannot be separated confidently from the compressed ascenders.','medium')
doubt('cancelled word before se reconstitue','est',[],'Several oblique cancellation strokes cover its beginning and middle.')

inventory=[
 dict(element='overwritten page number, handwritten',kind='deletion',position='top centre [775,10,843,75]',first_words_or_objects='doubtful 3 overwritten by 4'),
 dict(element='M entry, three handwritten baselines',kind='text',position='upper central block [323,61,1100,221]',first_words_or_objects='circled e; M = ensemble des figures'),
 dict(element='strates / déployement note, nine baselines',kind='margin note',position='upper left [37,109,520,490]',first_words_or_objects="strates d'une figure : les X∈M"),
 dict(element='connector around the strates note',kind='drawing',position='upper left/centre, from note around circled f to below incident line',first_words_or_objects='unlabelled bent enclosing connector; reproduced by C TikZ'),
 dict(element='definition of M, six baselines',kind='margin note',position='upper right [1215,60,1670,360]',first_words_or_objects='formé des objets de (ambient F,≤)'),
 dict(element='cancelled ambient letter after par',kind='deletion',position='right note, near [1590,278,1650,315]',first_words_or_objects='doubtful ambient F'),
 dict(element='L entry',kind='text',position='upper centre [323,270,1030,402]',first_words_or_objects='circled f; L ⊂ M, ens. des'),
 dict(element='underlined cancelled word below lieux',kind='deletion',position='L entry baseline, about [816,309,1008,357]',first_words_or_objects='doubtful éléments'),
 dict(element='raised replacement word',kind='insertion',position='above L entry baseline [813,275,1000,318]',first_words_or_objects='lieux'),
 dict(element='cancelled lower word in L entry',kind='deletion',position='about [618,365,890,398]',first_words_or_objects='doubtful minimaux'),
 dict(element='replacement definition of lieux, two baselines',kind='insertion',position='upper right, reached by bent connector [900,245,1670,480]',first_words_or_objects='éléments minimaux de ambient F minus singleton empty object'),
 dict(element='long connector to the replacement definition',kind='drawing',position='from [935,263] via [1100,275] to [1340,380], ending at [1448,380]',first_words_or_objects='unlabelled connector/arrow reproduced by C TikZ'),
 dict(element='Axiomes heading and introduction',kind='text',position='middle upper body [262,500,1665,739]',first_words_or_objects='Axiomes; I) Axiomes sine qua non'),
 dict(element='first three axiom numbers',kind='insertion',position='above introduction at right [1360,543,1605,585]',first_words_or_objects='At 1 - At 3'),
 dict(element='two cancelled groups before les relations',kind='deletion',position='start of third introductory line [285,668,498,739]',first_words_or_objects='At 1 / At 4; et / 4'),
 dict(element='At 1 statement',kind='text',position='[275,730,1580,815]',first_words_or_objects='At 1; ambient F ≠ empty set et stable par Sup'),
 dict(element='At 1 marginal name, three baselines',kind='margin note',position='slanted left [21,670,295,898]',first_words_or_objects='Axiomes des sommes majorées de figures'),
 dict(element='At 2 statement',kind='text',position='[275,803,1625,890]',first_words_or_objects='At 2; Toute figure est le sup de ses strates'),
 dict(element='overwritten beginning of est',kind='deletion',position='At 2, about [866,808,922,861]',first_words_or_objects='doubtful d'),
 dict(element='At 2 displayed formula',kind='display',position='[575,890,1550,986]',first_words_or_objects='F = Sup X; F-tilde = {X∈M | X≤F}'),
 dict(element='At 2 marginal criterion, seven baselines',kind='margin note',position='slanted left [20,805,465,1265]',first_words_or_objects='Axiome des strates équivaut à; Si F,C∈…'),
 dict(element='Scholie, four body baselines',kind='text',position='[402,1005,1667,1270]',first_words_or_objects='Scholie; At 1 et At 2 signifient…'),
 dict(element='raised tilded ambient family',kind='insertion',position='above end of partie, about [1580,1064,1642,1115]',first_words_or_objects='ambient F-tilde'),
 dict(element='conditions a), b), c)',kind='text',position='[705,1255,1655,1465]',first_words_or_objects='les Φ∈… sont fermés'),
 dict(element='cancelled initial formula in c)',kind='deletion',position='[765,1360,1250,1428]',first_words_or_objects='ambient F-tilde ≠ empty set (iff empty set belongs to ambient F-tilde)'),
 dict(element='cancelled et with uncancelled opening parenthesis',kind='deletion',position='[754,1405,855,1448]',first_words_or_objects='(et, with only et crossed'),
 dict(element='nonemptiness comment, three diagonal baselines',kind='margin note',position='[120,1300,637,1610]',first_words_or_objects='ambient F-tilde ≠ empty set automatique si M≠empty set'),
 dict(element='alternate formulation lead-in, two baselines',kind='text',position='[620,1435,1660,1540]',first_words_or_objects="ou, indépendamment d'une relation d'ordre sur M, un ens"),
 dict(element='primed conditions with upward arrow',kind='diagram',position='[615,1480,1660,1805]',first_words_or_objects='b′) ∀x∈M; a′) Dans…; upward arrow at left'),
 dict(element='overwritten F inside b′) brace',kind='deletion',position='about [1207,1540,1259,1599]',first_words_or_objects='doubtful F under live Phi'),
 dict(element='cancelled F after élément',kind='deletion',position='about [1330,1595,1386,1648]',first_words_or_objects='F'),
 dict(element='cancelled leading glyph of a′)',kind='deletion',position='about [776,1630,827,1700]',first_words_or_objects='∀ / F'),
 dict(element='Relation heading',kind='text',position='[413,1810,567,1880]',first_words_or_objects='Relation; no underline'),
 dict(element='compatibility definition and caption',kind='display',position='[535,1860,1645,1990]',first_words_or_objects='F [compat] G iff F∨C existe i.e. {F,C}…; figures compatibles'),
 dict(element='reconstitution paragraph',kind='text',position='[430,1970,1660,2153]',first_words_or_objects='Cette relation induit X [compat] Y dans M'),
 dict(element='axiom qualifier above the line',kind='insertion',position='[980,2066,1410,2124]',first_words_or_objects='avec At 1, At 2, At 3'),
 dict(element='cancelled old word before se',kind='deletion',position='about [984,2104,1045,2146]',first_words_or_objects='doubtful est'),
 dict(element='final compatibility properties',kind='display',position='[805,2140,1630,2325]',first_words_or_objects='(M,≤,[compat]), où [compat] satisfait; X [compat] réflexive symétrique'),
]

notation=[
 dict(form='ambient hooked F',reading=r'\mathscr F | \mathcal F | \mathfrak F',place='M heading and every repeated ambient family',observation='Hooked top and cross-stroke distinguish it from plain block F; exact alphabet is unresolved and is marked once.'),
 dict(form='bare M and L',reading=r'M | \mathcal M; L | \mathcal L',place='first definitions and repetitions',observation='Cursive forms do not securely decide intentional alphabets; first-occurrence doubts retained.'),
 dict(form='two-ended barred shaft',reading=barred,place='Scholie, between F and F-tilde',observation='Short upright bars at both ends; no arrowhead at the right.'),
 dict(form='compatibility glyph',reading=compat,place='definition, induced relation, triple, predicate, and two final properties',observation='Two opposing bent chevrons form a small central diamond. All seven occurrences were read directly.'),
 dict(form='straight overbar on ambient F',reading=r'\overline{\mathscr F}',place='inside the b′) set expression',observation='Straight rising bar differs from the wavy tilde over the family at the beginning of the same expression.'),
 dict(form='Φ',reading='capital Phi',place='a), b), c), b′)',observation='Broad loop with straight central stem; first C capital/lowercase doubt resolved.'),
 dict(form='slashed oval',reading=r'\varnothing',place='At 1, replacement lieux definition, c), lower note and a′)',observation='The diagonal slash runs through the oval; this page does not require replacing it with an unslashed phi.'),
 dict(form='ens and ens.',reading='abbreviation for ensemble; punctuation preserved locally',place='top L entry / left note versus Scholie, ou lead-in and b′)',observation='Top ens. occurrences visibly have a point. The three later ens occurrences do not.'),
 dict(form='déployement',reading='written spelling with y',place='upper left note',observation='Long descending y crosses the underline; not modernized to déploiement.'),
 dict(form='At and Roman I)',reading='axiom reference label and first section label',place='introduction, statements, Scholie and final insertion',observation='Every numerical inscription is included in second_boxes; cancelled digits retain their uncertainty.'),
]
hand_log=[
 dict(habit='C and G are distinguishable by an internal return/leg.',place='margin Si F,C; F≤G; compatibility display',observation='The proposed C readings have open right sides with simple exits. The G beside the initial compatibility sign and in F≤G has an inward return and leg. This comparison supports retaining C in F∨C and {F,C}, even where G would fit the mathematics.'),
 dict(habit='The author can flatten a decoration into a straight bar.',place='b′), two family symbols on the same line',observation='The first decoration is clearly wavy; the second is straight. The latter is transcribed as an overbar, with no mathematical normalization.'),
 dict(habit='An ordinary connective shaft may end in two upright caps.',place='Scholie',observation='The right cap must not be supplied with a conventional arrowhead; H uses mapsto, but no head is visible.'),
 dict(habit='Final s strokes can hang below a compressed word ending.',place='Axiomes in the At 1 margin; toutes before famille',observation='The visible final s is preserved in both places despite H\'s singular readings and the following singular famille.'),
 dict(habit='An f descender can look like a parenthesis in an interlinear addition.',place='figures above avec At 1, At 2, At 3',observation='The apparent opening curve before At 1 belongs to the f above. The lower long stroke is the insertion connector, not a closing parenthesis.'),
 dict(habit='Cancellation does not necessarily cross adjacent punctuation.',place='(et below c)',observation='The opening parenthesis survives to the left of the strike. Only the letters et are coded deleted.'),
 dict(habit='Underlining and cancellation can remain independently visible.',place='éléments under lieux',observation='A separate underline belongs to the old cancelled baseline word; the replacement above it is not thereby underlined.'),
]
notes=[
 dict(id='N005-01',claim='The proposal deliberately preserves written C in the compatibility definition and marginal hypothesis.',source='scan005_relation.png; scan005_margin_at2.png',reasoning_if_any='The neighboring G shapes have an internal return missing from the three proposed Cs. A mathematical expectation of G was used only to identify the places needing inspection, not to replace the letters.'),
 dict(id='N005-02',claim='F(M) is retained, rather than changed to a powerset P(M).',source='scan005_scholie.png',reasoning_if_any='The ink has the ambient F shape, regardless of which notation would normally be expected.'),
 dict(id='N005-03',claim='Toutes famille and fermés are retained as written.',source='scan005_a_prime.png; scan005_conditions_ab.png',reasoning_if_any='Grammatical agreement is not used to remove the source s or add an extra e.'),
 dict(id='N005-04',claim='No second X is supplied in the first final property.',source='scan005_properties.png',reasoning_if_any='The ink reads X, the compatibility glyph, and réflexive symétrique; the mathematical property does not license an added X.'),
 dict(id='N005-05',claim='H editorial notes and its expansion of t.f. are excluded from source text.',source='packets/scan005/H.tex; direct full-page and half-page reading',reasoning_if_any='Descriptions of marks, the note about the previous page, and the expansion de type fini are editorial prose, not inscriptions on this sheet.'),
 dict(id='N005-06',claim='The 30 C doubts have all been reviewed: ten resolved and twenty retained.',source='packets/scan005/C.tex and 22 named crops',reasoning_if_any='Resolved: marginal C; barred shaft; F(M); capital Phi; un; overbar; the second cancelled F; a′; toutes; first X of final properties. The deleted-digit and all other obscured cancelled readings remain doubtful.'),
 dict(id='N005-07',claim='All thirteen C deletions and four C insertions were individually audited; one further insertion is proposed.',source='deletion_insertion_audit; scan005_scholie.png',reasoning_if_any='The added wrapper records the raised ambient F-tilde after partie. The source-state corrections do not change the count of thirteen cancellation spans.'),
 dict(id='N005-08',claim='The note and connector shapes are reproduced rather than replaced by verbal descriptions.',source='scan005_left_note.png; scan005_L_definition.png; scan005_left_arrow.png',reasoning_if_any='C\'s two small TikZ connectors and upward tikz-cd arrow are retained because their directions and topology agree with the ink.'),
]

audit=[]
def aud(span,decision,place,evidence): audit.append(dict(C_span=span,decision=decision,place=place,evidence=evidence))
aud(r'\deleted{\unsure{3}}','Retain cancellation and doubt; final 4 remains live.','page number','page_number: earlier rounded strokes are overlaid by diagonal/cross-stroke and long stem of the final 4.')
aud(r'\deleted{\unsure{$\mathscr F$}}','Retain cancelled ambient letter and doubt.','upper right note after par','right_note: small crossed glyph is separate from the live relation signs below.')
aud(r'\deleted{\unsure{éléments}}',r'Add the visible underline: \deleted{\uline{\unsure{éléments}}}.','L entry beneath lieux','L_heading: cancelling stroke runs through old letters; separate shorter underline survives below them. Lieux is above, outside this strike.')
aud(r'\deleted{\unsure{minimaux}}','Retain deletion and doubt.','lower baseline of L entry','L_heading: multiple long cancelling strokes cross the word; not every letter is plain.')
aud(r'\deleted{\unsure{At 1}}','Retain cancellation; add At 4 as an unresolved digit alternative.','third axiom-introduction line','axiom_intro: the final digit has crossed upright/diagonal strokes admitting 1 or 4.')
aud(r'\deleted{\unsure{et|4}}','Retain both readings and deletion.','next cancelled group in introduction','axiom_intro: this group is separately cancelled before live les; no secure letter-by-letter reading.')
aud(r'\deleted{\unsure{d}}','Retain overwritten state and doubt.','At 2, beginning of est','at2: old loop/ascender overlaps the live initial e.')
aud(r'\deleted{\widetilde{\mathscr F}\neq\varnothing\quad(\Longleftrightarrow\varnothing\in\widetilde{\mathscr F})}','Retain the complete cancellation span.','first formula in c)','condition_c: one continuous horizontal strike covers the whole formula through the closing parenthesis; the later union and its final nonemptiness statement are live.')
aud(r'\deleted{\unsure{(et}}',r'Keep opening parenthesis live and only et deleted: (\deleted{\unsure{et}}.','below cancelled c) formula','condition_c: the strike begins to the right of the opening parenthesis; et remains covered and doubtful.')
aud(r'\deleted{\unsure{F}}','Retain doubt under the live Phi.','inside b′) opening set brace','b_prime: old angular strokes overlap live Phi and are not all separable.')
aud(r'\deleted{\unsure{F}}',r'Resolve the single letter to \deleted{F}.','after plus petit élément in b′)','b_prime: upright and two primary bars of F are visible to the left of the oblique cancellation strokes.')
aud(r'\deleted{\unsure{\forall|F}}','Retain both candidates.','before Dans in a′)','a_prime: the glyph is heavily crossed; converging upper strokes and lower barred residue do not settle it.')
aud(r'\deleted{\unsure{est}}','Retain deletion and doubt.','before se reconstitue','reconstitution: multiple sloping cancellation strokes conceal the short word; the inserted qualifier attaches beside it.')
aud(r'\inserted{``lieux\'\'}','Retain insertion, with no inherited underline from the cancelled word.','L entry','L_heading: lieux is above the old baseline and not crossed.')
aud('C inserted connector and éléments minimaux de ambient F minus singleton empty object pour ≪','Retain two-line inserted definition and its connector.','upper right','L_definition: the bent connector runs from the L correction to the definition. The whole set-difference formula and its subscript were inspected.')
aud(r'\inserted{At~1 - At~3}','Retain as raised phrase after premiers trois; no parentheses.','axiom introduction','axiom_intro: actual inserted text is At 1 - At 3, above the line; concernent is baseline text.')
aud(r'\inserted{avec At~1, At~2, At~3}','Retain placement after cancelled est and before se; no parentheses.','reconstitution paragraph','reconstitution: lower connector descends into that gap. The apparent left parenthesis belongs to the f above.')
aud('(no C insertion wrapper around ambient F-tilde after partie)',r'Propose \inserted{$\widetilde{\mathscr F}$}.','Scholie','scholie: ambient F-tilde is raised into the interlinear space above the end of partie.')

rowmap={}
def rows(ns,classification,keys=()):
 for n in ns: rowmap[n]=dict(source_row=n,classification=classification,change_ids=[ids[k] for k in keys])
rows([119],'page-marker/list-wrapper syntax mixed with genuine overwritten page number and circled source labels',['page','circles'])
rows([120],'alphabet doubt and circled label; not merely itemize syntax',['M','circles'])
rows([121,123,130,131],'source quotation form differs from editorial guillemets',['quotes'])
rows([122],'actual location of subset formula and ambient alphabet alternatives',['subset_place','F_alphabet'])
rows([124],'long alignment/syntax stretch: compare both marginal blocks, alphabet, underlines, spelling and source punctuation',['right_placement','M','F_alphabet','deployement','strates_underlines','left_punctuation'])
rows([125],'cancelled ambient letter is real omitted ink',['right_deleted_F'])
rows([126],'H adds terminal semicolon; list-wrapper tail is syntax',['top_terminal_punctuation'])
rows([127],'L alphabet doubt and actual circled label',['L','circles'])
rows([128],'long stretch includes two deletions, raised lieux, surviving underline and inserted replacement definition',['elements','lieux','minimaux','L_definition','quotes'])
rows([129],'H editorial descriptions excluded; marginal source text and source punctuation separately checked',['L_definition','deployement','strates_underlines','top_terminal_punctuation'])
rows([132,135],'genuine baseline words and wrong H insertion/parenthesis treatment',['intro_words','intro_insert'])
rows([133,134,136,137],'nonbreaking-space syntax only; actual At numerals checked',[])
rows([138],'two separate cancelled source groups; preserve doubtful readings',['intro_deleted1','intro_deleted2'])
rows([139,140],'H editorial note mixed with real marginal text and terminal punctuation difference',['axiomes_plural','intro_period','intro_insert'])
rows([141,142,146,147],'Sup/underset/subscript serialization only; entire formulas read and indices checked',[])
rows([143,144,148],'marginal block order mixed with genuine words, capitalization and C/G distinction',['equivaut','margin_C','de_figures','capital_Si','axiomes_plural'])
rows([145],'overwritten source glyph omitted by H',['deleted_d'])
rows([149,150],'nonbreaking-space and repeated heading alignment only; At 1 and At 2 checked',[])
rows([151],'TikZ syntax conceals real barred correspondence sign; also raised family symbol and alphabet issues',['map_caps','raised_family','F_alphabet','M'])
rows([152],'C F/P doubt resolved from complete F(M) expression',['F_of_M'])
rows([153],'H adds abbreviation point absent in source',['ens_scholie'])
rows([154],'actual pour/par word difference',['pour'])
rows([155,156,159,160,161],'itemize wrapper syntax only',[])
rows([157],'C capital/lowercase Phi doubt resolved on whole formula',['Phi'])
rows([158],'actual ending fermés/fermées; H marks doubt',['fermes'])
rows([162],'uncancelled opening parenthesis and cancelled doubtful et both require transcription',['et_parenthesis'])
rows([163],'union-index C membership/plus doubt retained after whole-expression crop',[])
rows([164],'itemize termination and editorial quotation delimiter are syntax',[])
rows([165,166,167],'source lower marginal text is distinct from H editorial note; substantial omitted wording',['margin_c_text'])
rows([168],'C un/une doubt resolved by crop',['un'])
rows([169],'H adds unwritten abbreviation point',['ens_ou'])
rows([170,171,172],'layout wrapper syntax includes substantive source arrow and labels; not discarded wholesale',['up_arrow','aprime_label'])
rows([173],'H adds unwritten abbreviation point; variable case also checked',['ens_bprime','bprime_case'])
rows([174],'old overwritten F omitted by H',['bprime_old_F'])
rows([175],'straight overbar versus tilde; complete b′) formula inspected',['bprime_bar'])
rows([176,181,182],'text-column and row wrapper syntax only',[])
rows([177],'cancelled F is real source ink and is now readable',['bprime_cancelled_F'])
rows([178,179],'source upward arrow, a′) label and cancelled glyph differ from H rendering',['up_arrow','aprime_label','aprime_cancel'])
rows([180],'C toute/toutes doubt resolved to written toutes',['toutes'])
rows([183],'H editorial descriptions excluded; real arrow, labels, margin note and Relation heading separately checked',['up_arrow','aprime_label','aprime_cancel','margin_c_text','relation_heading'])
rows([184,187],'aligned/display delimiter syntax only',[])
rows([185,186],'TikZ syntax stretch conceals compatibility glyph, defining label and genuine C/G differences',['compat','join_C','brace_C','defn','relation_punctuation'])
rows([188],'display delimiter syntax plus H added caption period',['relation_punctuation'])
rows([189],'TikZ syntax for repeated compatibility sign; actual glyph inspected',['compat'])
rows([190],'cancelled old word has doubtful readable candidate est',['est_deleted'])
rows([191,195],'parentheses are not written around inserted At references',['avec_insert'])
rows([192,193,194],'nonbreaking-space syntax only; all handwritten inserted numerals checked',['avec_insert'])
rows([196],'display delimiter only',[])
rows([197,198,199,200],'long symbol/layout serialization stretch includes real first-X doubt and H additional X/comma; all final formulas inspected',['compat','reflexive_X'])
rows([201,202,203,204],'repeated glyph serialization and H editorial t.f. expansion; source primes, inequalities and double implication checked',['compat'])
assert sorted(rowmap)==list(range(119,205))

B=[]
def box(kind,coords,reading):
 n=len(B)+1;B.append(dict(box=f'scan005-b{n:02d}',kind=kind,x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
box('handwritten overwritten page number',[775,10,843,75],r'\deleted{\unsure{3}}4')
box('circled doubtful label',[330,72,375,111],'circled e, uncertain')
box('whole first mathematical expression and heading',[323,45,1100,221],r'M= ensemble des figures ⊂ ambient F élémentaires ou multistrates; alphabets/opening quote doubtful')
box('whole marginal note and its three formulas',[37,109,520,490],r'strates; déployement; F-tilde set; X triangleleft F; X∈M and X≤F')
box('whole marginal definition and relations',[1215,60,1670,360],r'formé des objets; ambient (F,≤); ≤_M and ≪_M; cancelled ambient F')
box('deletion',[1590,278,1650,315],r'\deleted{\unsure{\mathscr F}}')
box('circled doubtful label',[325,299,371,351],'circled f, uncertain')
box('whole formula with doubtful L alphabet',[323,270,1030,402],r'L⊂M, ens. des; old words cancelled; lieux inserted')
box('deletion with underline',[816,309,1008,357],r'\deleted{\uline{\unsure{éléments}}}')
box('insertion',[813,275,1000,318],'lieux in paired high quotes')
box('deletion',[618,365,890,398],r'\deleted{\unsure{minimaux}}')
box('insertion and complete set-difference formula',[900,245,1670,480],r'éléments minimaux de F\setminus{empty_F} pour ≪; long connector')
box('whole introduction and source word differences',[262,545,1665,739],'Les premiers trois ne concernent que…; cancelled groups; no final period')
box('handwritten section number',[267,588,339,643],'I)')
box('insertion and handwritten numerical inscription',[1360,543,1605,585],'At 1 - At 3')
box('handwritten numerical inscription',[1450,645,1658,697],'At 4 - At 7')
box('deletion containing handwritten numeral',[285,680,405,739],r'\deleted{\unsure{At 1|At 4}}')
box('deletion possibly containing handwritten numeral',[404,668,498,739],r'\deleted{\unsure{et|4}}')
box('whole At 1 statement and number',[275,730,1580,815],'At 1; ambient F ≠ empty, stable par Sup_I majorés (I quelconque)')
box('whole slanted marginal note',[21,670,295,898],'Axiomes des sommes majorées de figures')
box('whole At 2 statement/display and number',[275,803,1625,995],'At 2; Toute figure [deleted d]est le sup; F=Sup X; F-tilde set')
box('overwritten deletion',[866,808,922,861],r'\deleted{\unsure{d}}est')
box('whole marginal criterion and all formulas',[20,805,465,1265],'équivaut à; Si F,C∈ambient F, alors F≤G iff ∀X∈F-tilde ∃Y∈G-tilde avec X≤Y; de figures')
box('whole Scholie and complete expressions',[402,1005,1667,1270],'F barred-shaft F-tilde; inserted family; ambient F(M), M ens ordonné (pour ≤)')
box('handwritten numerical references',[635,1008,965,1078],'At 1 et At 2')
box('newly recorded insertion',[1580,1064,1642,1115],r'\inserted{\widetilde{\mathscr F}} after partie')
box('whole formula/condition and word difference',[705,1255,1320,1330],'a) les capital Phi∈ambient F-tilde sont fermés')
box('whole condition and capitalization',[705,1315,1655,1383],'b) Si Phi∈ambient F-tilde, toute partie fermée de Phi est ∈ambient F-tilde')
box('whole c) expression, including uncertain union subscript',[705,1370,1655,1465],'cancelled nonemptiness formula; live union indexed Phi [in|+] ambient F-tilde, equals M')
box('whole deleted formula',[765,1360,1250,1428],r'\deleted{\widetilde{\mathscr F}\neq\varnothing (\Longleftrightarrow\varnothing\in\widetilde{\mathscr F})}')
box('live punctuation adjacent to deletion',[754,1405,855,1448],r'(\deleted{\unsure{et}}')
box('whole slanted marginal note and formulas',[120,1300,637,1610],'nonemptiness automatique si M nonempty; et dans tous les cas, doubtful équivaut à empty∈family')
box('word alternatives and abbreviation point',[620,1435,1660,1540],'un ens de parties, no period after ens')
box('whole b-prime formula and two deletions',[690,1515,1660,1655],r'∀x∈M, l’ens family^x={deleted F Phi∈overline family |x∈Phi}; plus petit élément deleted F (noté X-tilde)')
box('overwritten deletion',[1207,1540,1259,1599],r'\deleted{\unsure{F}} under Phi')
box('deleted single mathematical letter',[1330,1595,1386,1648],r'\deleted{F}')
box('whole a-prime condition and formulas',[695,1630,1540,1805],'a′) deleted ∀/F; Dans (family,⊂), toutes famille majorée a un Sup, et family nonempty (iff empty∈family)')
box('resolved differing label',[692,1640,765,1680],'a′)')
box('deletion',[776,1630,827,1700],r'\deleted{\unsure{\forall|F}}')
box('real differing word',[1180,1650,1318,1710],'toutes')
box('whole arrow with both ends',[615,1480,815,1690],'curved upward arrow from beside a′) toward b′)')
box('whole compatibility formula and defining label',[413,1810,1645,1990],r'F compat G iff^[défn|defn] F∨C existe i.e. {F,C} majoré dans (ambient F,≤); figures compatibles')
box('whole definition label',[730,1863,820,1905],'défn / defn, accent uncertain')
box('clear differing mathematical letter',[900,1883,952,1939],'C after ∨')
box('proposed departure from both witnesses',[1215,1885,1265,1944],'C inside {F,C}')
box('whole paragraph including deletion and insertion',[430,1970,1660,2153],'Cette relation induit X compat Y; with At references inserted before se reconstitue')
box('insertion containing all handwritten numerical references',[980,2066,1410,2124],'avec At 1, At 2, At 3; no parentheses')
box('deletion',[984,2104,1045,2146],r'\deleted{\unsure{est}}')
box('whole final formulas and first-X decision',[805,2140,1630,2325],'(M,≤,compat); X compat réflexive symétrique; X compat Y, X′≤X,Y′≤Y ⇒ X′ compat Y′')

review=dict(scan=5,
 lines_read=dict(count=71,convention='Count distinct physical handwritten baselines, not LaTeX lines. Main column: 36, including two separate cancelled baselines (minimaux and et), headings, formula rows and the compatibility caption. Marginal notes: 28 (upper left 9; upper right 6; At 1 note 3; At 2 note 7; lower note 3). Inserted inscriptions: 6 baselines (lieux 1; replacement definition 2; At 1–At 3 1; raised ambient F-tilde 1; final avec At 1, At 2, At 3 1). Page-number inscription: 1. Mathematical superscripts, subscripts and the defining-equivalence label are counted with their parent formula, not as independent prose lines.',main=36,marginal=28,inserted=6,page_number=1),
 changes=changes,doubts=D,inventory=inventory,notation=notation,hand_log=hand_log,notes=notes,
 check_events=[
  dict(action='allowed-source reading',details='Read only scan005 packet files, its three named images, and updated packets/NOTATION.md; RULES and PREAMBLE were already read. No other page, peer output, external source or OCR read.'),
  dict(action='whole-image visual layout check',details='Personally viewed the 1684×2361 whole image once for layout: separated central list/text, five marginal blocks, corrections, connectors, displays and page overwrite.'),
  dict(action='first-half visual reading',details='Personally viewed the full-resolution upper half once and read every line, sign, underline, correction and marginal feature against C and H.'),
  dict(action='second-half visual reading',details='Personally viewed the full-resolution lower half once and read every line, Greek letter, variable case, decoration, inequality, prime and source punctuation against C and H.'),
  dict(action='crop creation and visual inspection',details='Created and personally read 22 original-image crops, all at 2800 px wide with LANCZOS, autocontrast cutoff 0.4, unsharp radius 1.3/percent120/threshold3; three slanted notes rotated as recorded. All original boxes and transforms are in scan005_crop_manifest.json; exact script saved in out/scripts/scan005_crops.py.'),
  dict(action='source-state visual audit',details='Individually audited 13 C deletions and 4 C insertions. Recorded separate underline under cancelled éléments, uncancelled opening parenthesis before struck et, and a new raised-symbol insertion after partie.'),
  dict(action='all C doubt marks reviewed',details='30 C doubt marks: 10 resolved on complete local crops, 20 retained. All cancelled-text doubts retained except the single clearly readable F after élément in b′).'),
  dict(action='all raw rows reviewed',details='Every supplied source_row 119–204 classified. Long syntax stretches were checked for hidden source differences rather than rejected wholesale. H editorial notes were excluded from source text.'),
  dict(action='formula and glyph visual checks',details='Compared C/G locally; inspected every complete formula with a doubt, both ends of the barred correspondence sign and upward arrow, all seven compatibility signs, all primes, ≤/≪, the straight overbar and all empty-set signs. These are visual reading events, not mathematical validation CHECK_EVENTS.'),
  dict(action='numeric inscription visual check',details='Read page overwrite; Roman I); inserted At 1–At 3; live At 4–At 7; cancelled At and possible 4; At 1/At 2 headings and Scholie references; final inserted At 1, At 2, At 3. All are included in second_boxes.'),
  dict(action='excluded operations',details='No OCR, recognition tool, external research, TeX compilation, finalized-page write or global-log write used.'),
 ],deletion_insertion_audit=audit,difference_review=[rowmap[n] for n in sorted(rowmap)],second_boxes=B)
# Apostrophes in raw strings above are literal source apostrophes, not accent commands.
def clean(v):
 if isinstance(v,str): return v.replace("\\'","'")
 if isinstance(v,list): return [clean(x) for x in v]
 if isinstance(v,dict): return {k:clean(x) for k,x in v.items()}
 return v
review=clean(review)
(R/'out/review/scan005_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print(f'Saved scan005 review: {len(changes)} records, {len(D)} retained doubts, {len(audit)} state audits, {len(B)} boxes, {len(rowmap)} raw rows.')
