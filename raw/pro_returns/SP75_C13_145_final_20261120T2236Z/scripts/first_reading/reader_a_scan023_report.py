from pathlib import Path
import json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=root/'edition/reader_reports'
manifest=json.loads((out/'145_scan023_crop_manifest.json').read_text())
crops={item['name']:item for item in manifest}

def evidence(name):
    item=crops[name]
    return {'crop':item['crop'],'box':item['box']}

changes=[]
ids={}
def change(key,place,C,H,final,ink,confidence,kind,c_changed,h_changed,crop,error_category,marked_in_H='no',math_consequence=''):
    ident=f's023-{len(changes)+1:02d}'
    ids[key]=ident
    changes.append(dict(id=ident,place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c_changed,h_changed=h_changed,marked_in_H=marked_in_H,**evidence(crop),error_category=error_category,math_consequence=math_consequence))

change('inverse','opening line, after image','réciproque','inverse',r'\unsure{inverse|réciproque}',
       'A detached point or short high stroke stands over the initial low upright. It is followed by a shallow arch and compressed angled/open strokes. These favor dotted i and n/v/e/r/s/e; no distinct descending p or q can be isolated. The compressed middle still prevents a certain letter-by-letter resolution. The initial preference for C was reconsidered on this same saved crop.',
       'medium','misread word',True,False,'opening_header10',[2])
change('quoted','opening paragraph, double-quoted expression',r"``triangulé \unsure{pondéré|pointé}''",r'« \ill{} \ill{} »',r"``triangulé pondéré''",
       'The first word has the descending g and final l/é. In the second, a descending p is followed by low o/n forms, a distinct rising d, then the accented compressed ending é/r/é. The d ascender excludes pointé. Two short high ticks occur at each quotation boundary.',
       'high',r'readable ink left as \ill{}',False,True,'quoted_name_gen',[2,5])
change('gen','opening paragraph, before the three tau generators','gén','générateurs','gén',
       'A looped descending g, the accent over the compressed é, and a terminal short n are present. No letters for érateurs and no distinct terminal stop follow this short form.',
       'high','abbreviation expanded or spelling modernised',False,True,'quoted_name_gen',[8])
change('relati','cancelled short word before avec',r'\deleted{\unsure{relati.}}',r'\struck{relation}',r'\deleted{\unsure{relati.}}',
       'The horizontal cancellation crosses a short r/e/l/t-like sequence; an i-like final stroke and a separate point survive. The interior a-like trace is obscured. There is no full terminal on sequence supporting the expansion relation. Retain the doubtful abbreviated reading.',
       'low','abbreviation expanded or spelling modernised',False,True,'quoted_name_gen',[2,7,8])
change('old0','(17), first row, first right-hand tau index',r'\tau_{\deleted{\unsure{0}}\infty}',r'\tau_\infty',r'\tau_{\deleted{\unsure{0}}\infty}',
       'The live index has two joined lobes, infinity. Earlier dark/grey material lies within and below its left lobe, consistent with an overwritten zero but not separable enough to certify the old digit. H drops this earlier layer.',
       'low','omission',False,True,'system17',[1,3,7])
change('oldinf1','(17), first row, second right-hand tau index',r'\tau_{\deleted{\unsure{\infty}}1}',r'\tau_1',r'\tau_{\deleted{\unsure{\infty}}1}',
       'The live index is a thick single upright 1. A lighter crossed, low, two-turn form extends to its left; infinity is plausible, but the overwrite prevents complete recovery. Preserve the cancelled doubtful old index.',
       'low','omission',False,True,'system17',[1,3,7])
change('oldinf2','(17), second row, first right-hand tau index',r'\tau_{\deleted{\unsure{\infty}}0}',r'\tau_0',r'\tau_{\deleted{\unsure{\infty}}0}',
       'A dark closed live oval is 0. A lighter loop extends left of it and another trace is covered by the live oval, allowing but not proving an old infinity. H gives only the final index.',
       'low','omission',False,True,'system17',[1,3,7])
nb_graphic=r'\begin{tikzpicture}[baseline=0.2ex]\draw (0,0.12)--(0.32,0.15);\fill (0.17,0.06) circle (0.015);\end{tikzpicture}'
change('nb','upper-right margin, mark to the right of underlined NB',r'$-$','',nb_graphic,
       'A short slightly rising horizontal stroke is followed underneath by one detached dark point near its middle. There is no second full horizontal bar. Reproduce the two visible components without assigning an equality or other function.',
       'high','drawing or diagram',True,True,'nb_mark',[3,4])
change('ayant','middle paragraph, base words before the insertion','ayant comme','engendré par','ayant comme',
       'The base word begins with a small a, followed by a descending y and a long joined ant ending; the next word is comme with low repeated arches. There is no initial engendr- sequence here.',
       'high','misread word',False,True,'main_insertion_hom',[2])
change('insert_gen','middle paragraph, phrase inserted before seules',r'\inserted{gén. les $\tau_i$, avec les}',r'les $\tau_i$, avec les',r'\inserted{gén. les $\tau_i$, avec les}',
       'The complete phrase is above the base line. A long guide runs beneath it and turns down immediately before seules. The initial short gén. has a distinct terminal point; les, tau with dotted i, the comma, avec and les are legible.',
       'high','insertion or placement',False,True,'main_insertion_hom',[3,6,8])
change('hom','middle paragraph, after (16) and the dash','on a un hom signature évident',r'\ill{} \ill{} \ill{}','on a un hom signature évident',
       'After the dash, the short round on, a, and joined un are visible. On the next baseline h/o/m precedes signature: its g has the long returning descender; this is not a separate underline. The following word has the accented initial é and the v/i/d/e/n/t sequence.',
       'high',r'readable ink left as \ill{}',False,True,'main_insertion_hom',[2,3,5,8])
change('kernel_pi','middle paragraph, group named as the kernel',r'\pi',r'\pi',r'\Pi',
       'The glyph has a full horizontal cap over two separately descending legs. The left leg is substantially straight and full height; the right turns slightly at its foot. Read this local capital form as Pi.',
       'high','misread symbol or index',True,True,'kernel_decrits',[1])
change('decrits','middle paragraph, last line','décrits','définis','décrits',
       'After d/é, the third letter is an open c, followed by a low r, a separately dotted i, a tall t, and a final s-like return. There is no tall f or subsequent n of définis.',
       'high','misread word',False,True,'kernel_decrits',[2])
change('four_points','middle paragraph, after the final (17)',r'\ldots','…',r'\ldots\ .',
       'Three close, short, dark horizontal points follow the closing parenthesis. A fourth detached dark point sits farther right on the same baseline. All four are retained; the fourth is not part of the paper crease below the previous line.',
       'high','omission',True,True,'kernel_decrits',[3,10])
separator=r'\figure{\begin{tikzpicture}\draw (0,0)--(0.8,0.025);\end{tikzpicture}}'
change('separator','short central rule between the two main blocks',separator,'',separator,
       'A single dark nearly horizontal stroke stands alone in the central blank. Its right endpoint is slightly higher and thickened. It is separate from text and has no arrowhead.',
       'high','drawing or diagram',False,True,'separator',[3,4])
change('margin_prefix','left slanted margin, before relations','On a les',r'\ill{}','On a les',
       'After rotation, the first line has a large open O with following n, a separate small a, then a tall l and low e/s ending. The next line is relations.',
       'high',r'readable ink left as \ill{}',False,True,'margin_relations',[2,5])
change('margin_rho','left margin, detached symbol below relations',r'\unsure{\rho}',r'\ill{}',r'\rho',
       'The isolated sign has a closed narrow head with a continuous long descending stem and a small return at the head/stem junction. This supports rho. It stands well below the prose and is retained as a separate lower entry, without supplying an unfinished relation.',
       'high',r'readable ink left as \ill{}',False,True,'margin_relations',[1,5])
change('autom_ext','lower paragraph, second baseline',r'des autom. extérieurs à lacets de',r'\uncertain{des extensions de}',r'des autom. extérieurs à lacets de',
       'The short autom. has a visible terminal point. The next word begins e/x with a tall t, retains the accented é and the final r/s turn. A separate accented a is followed by the l/a/c/e/t/s word. This is a longer, differently segmented inscription than extensions de.',
       'high','misread word',False,True,'revenons_designera',[2,3,8],marked_in_H='yes')
change('designera','lower paragraph, beginning of third baseline','désignera','désigne','désignera',
       'The descending g is followed by the compressed n/e and then two further low returns for r/a. These terminal strokes extend beyond the désigne reading.',
       'high','misread word',False,True,'revenons_designera',[2])
change('hat_pi_1','lower paragraph, after the product and par',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
       'Below a separate caret, a full grey cap joins two long dark legs. The right leg bends only at its lower end. This is the capital Pi outline, not a one-stem gamma.',
       'high','misread symbol or index',True,True,'extension_cancelled_exterieurs',[1])
change('autom_abbrev','lower paragraph, le groupe des autom.',r'autom.',r'\uncertain{automorphismes}',r'autom.',
       'A short a/u/t/o/m run ends in a detached low stop before the cancelled word. The long morphismes ending is not written.',
       'high','abbreviation expanded or spelling modernised',False,True,'extension_cancelled_exterieurs',[8],marked_in_H='yes')
change('insert_a','lower paragraph, replacement above cancelled extérieurs','à','',r'\inserted{à}',
       'A detached small open bowl with its own high accent sits above the right end of the crossed word. The next baseline begins lacets, with no baseline à. Preserve this visible à as an interlinear replacement.',
       'high','insertion or placement',True,True,'extension_cancelled_exterieurs',[3,6])
change('hat_pi_2','lower paragraph, lacets de, before the comma',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
       'The caret is separate from a full horizontal cap. Both legs extend down from that cap; the left is straight and the right is curved at its foot.',
       'high','misread symbol or index',True,True,'lacets_autext_pi',[1])
change('hat_pi_3','lower paragraph, operand of Aut ext lac',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
       'Inside the parentheses a small separate caret lies above a complete cap and two long legs. The small outward feet do not reduce either leg to a gamma-like short tip.',
       'high','misread symbol or index',True,True,'lacets_autext_pi',[1])
change('hat_pi_4','lower paragraph, last short baseline par',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
       'The final small hatted group sign again has a complete cap over two full descending legs, with a curved right foot.',
       'high','misread symbol or index',True,True,'lacets_autext_pi',[1])
change('no_colon','after the last par hatted-Pi, before (18)','',':','',
       'The space after the final hatted group sign is blank. There are no two aligned punctuation points at the end of that baseline. H supplies a colon.',
       'high','text not on the page',False,True,'lacets_autext_pi',[9])
change('hat_pi_5','(18), group after the first 1',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
       'A separate caret surmounts a broad cap. Two long legs descend independently beneath it, with the left nearly straight and the right curved at its foot.',
       'high','misread symbol or index',True,True,'diagram18',[1])
change('vertical_relation','(18), short vertical mark and placement below double-hatted Gamma',r'\arrow[d,equal]',r'\qquad \hat{\hat\Gamma} \subset',r'\\ &&&&\unsure{\Vert|\cup}&\\',
       'Two short downward strokes lie directly under the single double-hatted Gamma. The longer left stroke turns right at its bottom and nearly meets the shorter right stroke. The join is not secure enough to decide two vertical bars versus a small cup. The Aut ext expression is beneath this mark; there is no separately repeated Gamma to its left. Preserve the local alternatives and the vertical arrangement.',
       'medium','drawing or diagram',False,True,'diagram18',[1,4,6,9],marked_in_H='yes')
change('hat_pi_6','(18), operand in the expression below Gamma',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
       'Within the lower parentheses the hatted sign has a full cap and two long dark legs. These match the other local capital Pi forms.',
       'high','misread symbol or index',True,True,'diagram18',[1])
change('diagram_comma','(18), after the terminal 1 on the main row','',',','',
       'No comma or other separate point follows the terminal upright 1. H inserts a comma before its horizontal restatement of the lower expression.',
       'high','text not on the page',False,True,'diagram18',[9])
change('footer','lower-left handwritten page number',r'\mspage{22}','',r'\mspage{22}',
       'Two separate digits each have a curved upper head, descending diagonal and horizontal foot. They are the handwritten footer 22 at the lower left, not an editorial page marker.',
       'high','omission',False,True,'footer22',[3])

decisions=[
    dict(id='M0851',decision='first',reading='pondéré',ink='The second quoted word has a distinct d ascender between its low initial p/o/n sequence and accented é/r/é ending; pointé does not fit that d and ending.',confidence='high',**evidence('quoted_name_gen')),
    dict(id='M0852',decision='first',reading=r'\rho',ink='A closed narrow head joins a continuous long descending stem. The small left return is part of this head/stem junction; no independent competing letter-stroke remains.',confidence='high',**evidence('margin_relations')),
    dict(id='M0853',decision='undecided',reading=r'\unsure{\mathfrak S_3|\mathcal S_3}',ink='The ornate S has a rounded outer sweep, high right return and short inner sweep; its subscript is clearly 3. The handwritten form does not distinguish the two proposed typographic alphabets. The whole formula was also read in the native half.',confidence='medium',**evidence('extension_cancelled_exterieurs')),
]
unlisted=[]
for ident,place,C_mark,reading,ink,crop in [
    ('U023-01','cancelled short word before avec',r'\unsure{relati.}',r'\deleted{\unsure{relati.}}','The horizontal strike obscures the compressed middle; short r/e/l/t-like traces and a final point survive, but not every letter is plain.','quoted_name_gen'),
    ('U023-02','(17), first row, old first right-hand index',r'\unsure{0}',r'\deleted{\unsure{0}}','Old material is covered by the new infinity; a complete old zero is not separable.','system17'),
    ('U023-03','(17), first row, old second right-hand index',r'\unsure{\infty}',r'\deleted{\unsure{\infty}}','The light low crossed form extends left of the dark live 1, but both old lobes are not independently plain.','system17'),
    ('U023-04','(17), second row, old first right-hand index',r'\unsure{\infty}',r'\deleted{\unsure{\infty}}','One earlier loop extends left of the dark live 0; the rest is obscured by the overwrite.','system17'),
]:
    unlisted.append(dict(id=ident,place=place,C_mark=C_mark,decision='undecided',reading=reading,ink=ink,confidence='low',**evidence(crop)))

doubts=[
    dict(place='opening line, image ... de Z/2',reading=r'\unsure{inverse|réciproque}',alternatives=['inverse','réciproque'],confidence='medium',reason='Dotted initial and low sequence favor inverse; no p/q descenders are identifiable, but the compressed middle is not fully separable.'),
    dict(place='cancelled word before avec',reading=r'\deleted{\unsure{relati.}}',alternatives=['relati.','unresolved shorter r/e/l/t/i abbreviation'],confidence='low',reason='The cancellation covers the middle letters. A full relation is not visible.'),
    dict(place='(17), first row, first overwritten right-hand index',reading=r'\deleted{\unsure{0}}',alternatives=['0','unresolved earlier loop'],confidence='low',reason='The live infinity covers the old index.'),
    dict(place='(17), first row, second overwritten right-hand index',reading=r'\deleted{\unsure{\infty}}',alternatives=[r'\infty','unresolved earlier low form'],confidence='low',reason='The dark live 1 and crossing strokes obscure part of the old form.'),
    dict(place='(17), second row, first overwritten right-hand index',reading=r'\deleted{\unsure{\infty}}',alternatives=[r'\infty','unresolved earlier loop'],confidence='low',reason='The new dark zero overlies most of the old form.'),
    dict(place='lower paragraph, ornate S with subscript 3',reading=r'\unsure{\mathfrak S_3|\mathcal S_3}',alternatives=[r'\mathfrak S_3',r'\mathcal S_3'],confidence='medium',reason='Letter and subscript are clear, but the handwritten ornament does not decide the typographic alphabet.'),
    dict(place='lower paragraph, cancelled extérieurs',reading=r'\deleted{\unsure{extérieurs}}',alternatives=['extérieurs','interior letters partly obscured'],confidence='medium',reason='The initial e/x/t and accented é, plus the final s-like curve, favor extérieurs; the horizontal cancellation merges several compressed internal strokes. H also marks this reading uncertain.'),
    dict(place='(18), small vertical sign below double-hatted Gamma',reading=r'\unsure{\Vert|\cup}',alternatives=[r'\Vert',r'\cup'],confidence='medium',reason='The left descending stroke curls right at its foot and almost joins the shorter right stroke; the ink does not securely separate two vertical bars from a cup-shaped sign.'),
]

inventory=[]
def inv(kind,position,first,box):
    inventory.append(dict(element=f'I{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=first,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('text','top centre','10',[819,20,899,85])
inv('text','upper block, first three baselines','Le sous-groupe ... cartographique ... Malgoire, ayant comme',[230,85,1645,350])
inv('text','upper block, generator line and following avec',r'gén $\tau_0,\tau_1,\tau_\infty$ ... avec',[230,337,762,463])
inv('deletion','upper block, short word before avec',r'\deleted{\unsure{relati.}}',[247,409,395,461])
inv('display','upper-left three-row system',r'(17), l_0, l_1, l_\infty',[276,473,842,704])
inv('deletion','(17), first row, left trial product',r'\deleted{\tau_1\tau_\infty={}}',[397,481,571,566])
inv('deletion','(17), second row, left trial product',r'\deleted{\tau_\infty\tau_0={}}',[397,556,571,625])
inv('deletion','(17), first row, earlier first RHS index',r'\deleted{\unsure{0}}',[688,503,727,549])
inv('deletion','(17), first row, earlier second RHS index',r'\deleted{\unsure{\infty}}',[748,503,797,549])
inv('deletion','(17), second row, earlier first RHS index',r'\deleted{\unsure{\infty}}',[692,571,741,621])
inv('margin note','upper-right of (17)',r'\uline{NB}',[1060,425,1168,532])
inv('drawing','right of NB','short dash with detached point underneath',[1196,438,1243,482])
inv('text','middle block, five base lines',r'$\mathcal E_\tau$ peut être considéré ... décrits par (17), four points',[222,700,1637,1300])
inv('insertion','above middle block second baseline, attached before seules',r'\inserted{gén. les $\tau_i$, avec les}',[685,786,1195,911])
inv('drawing','central blank between main blocks','short slightly rising separator rule',[744,1350,924,1422])
inv('margin note','left, slanting beside the start of the lower block','On a les / relations',[23,1312,220,1580])
inv('margin note','left, detached below the slanted words',r'$\rho$',[30,1627,115,1720])
inv('text','lower block, seven base lines','Revenons à une description plus symétrique ... par hatted Pi',[244,1440,1645,2126])
inv('display','lower block, inline product equality',r'\hat\Gamma_{0,3}=\Gamma_{0,3}=\unsure{\mathfrak S_3|\mathcal S_3}\times\mathbb Z/2',[659,1713,1265,1825])
inv('deletion','lower block, after le groupe des autom.',r'\deleted{\unsure{extérieurs}}',[1398,1834,1642,1920])
inv('insertion','above right end of cancelled extérieurs',r'\inserted{à}',[1567,1809,1615,1865])
inv('display','lower block, inline definition of double-hatted Gamma',r'\widehat{\widehat\Gamma}=\operatorname{Aut}\operatorname{ext}_{\mathrm{lac}}(\hat\Pi)',[1175,1894,1599,2010])
inv('diagram','bottom, main row and dependent lower expression',r'(18), 1 to hatted Pi to double-hatted E to double-hatted Gamma to 1',[239,2085,1245,2355])
inv('drawing','below the single Gamma in (18)',r'\unsure{\Vert|\cup}',[994,2227,1020,2263])
inv('text','lower-left footer','22',[31,2276,126,2352])

system17=r'''\[
(17)\quad\left\{\begin{aligned}
\deleted{\tau_1\tau_\infty={}}\ l_0&=\tau_{\deleted{\unsure{0}}\infty}\tau_{\deleted{\unsure{\infty}}1}\\
\deleted{\tau_\infty\tau_0={}}\ l_1&=\tau_{\deleted{\unsure{\infty}}0}\tau_\infty\\
l_\infty&=\tau_1\tau_0
\end{aligned}\right.
\]'''
diagram18=r'''\diagram{\begin{tikzcd}[column sep=large,row sep=small]
(18)\quad&1\arrow[r]&\hat\Pi\arrow[r]&\widehat{\widehat{\mathcal E}}\arrow[r]&\widehat{\widehat\Gamma}\arrow[r]&1\\
&&&&\unsure{\Vert|\cup}&\\
&&&&\operatorname{Aut}\operatorname{ext}_{\mathrm{lac}}(\hat\Pi)&
\end{tikzcd}}'''
second_boxes=[]
def sb(kind,coords,reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}',kind=kind,coords=coords,reading=reading))
sb('handwritten header 10, numerical quotient, and disputed opening word',[245,20,1645,166],r'\mspage{10} Le sous-groupe $\mathcal E_\tau$ de $\mathcal E$ image \unsure{inverse|réciproque} de $\mathbb Z/2$')
sb('quoted lexical disagreement, agreed proper name, abbreviation, numerical indices, and cancelled doubt',[229,257,1632,463],r"``triangulé pondéré'' de Malgoire, ayant comme gén $\tau_0,\tau_1,\tau_\infty$ \deleted{\unsure{relati.}} avec")
sb('complete numbered display (17), all live numerical indices and all five mathematical cancellations',[276,473,842,704],system17)
sb('underlined margin NB and separate dash-over-point drawing',[1060,425,1280,532],r'\margin{\uline{NB}\quad'+nb_graphic+'}')
sb('all inserted words and their attachment, base lexical disagreements, reference (16), and signature formula',[228,700,1637,1088],r'$\mathcal E_\tau$ peut être considéré comme le groupe ayant comme \inserted{gén. les $\tau_i$, avec les} seules relations (16) --- on a un hom signature évident $\tau_i\longrightarrow-1$ de $\mathcal E_\tau$ dans')
sb('numeral in ±1, local capital Pi, disputed décrits, reference (17), and four continuation points',[222,1066,1620,1300],r'$\pm1$, dont le noyau est $\Pi$ engendré par les $l_i$ décrits par (17)\ldots\ .')
sb('independent separator omitted in H',[744,1350,924,1422],separator)
sb('complete slanted marginal note and detached rho',[23,1312,220,1730],r'\margin{\begin{tabular}{@{}l@{}}On a les\\relations\\[2ex]$\rho$\end{tabular}}')
sb('full lower opening lines with lexical disagreements and hatted-E definition',[244,1440,1645,1762],r'Revenons à une description plus symétrique des autom. extérieurs à lacets de $\mathcal E$. On désignera par $\hat{\mathcal E}$ le complété profini de $\mathcal E$,')
sb('complete numerical product formula with font doubt, hatted Pi, double-hatted E, abbreviated autom., cancellation, and interlinear à',[254,1710,1642,1942],r'extension de $\hat\Gamma_{0,3}=\Gamma_{0,3}=\unsure{\mathfrak S_3|\mathcal S_3}\times\mathbb Z/2$ par $\hat\Pi$, et par $\widehat{\widehat{\mathcal E}}$ le groupe des autom. \deleted{\unsure{extérieurs}} \inserted{à}')
sb('last two lower prose baselines, all three local hatted Pi forms, double-hatted Gamma and omitted H colon',[253,1894,1630,2126],r'lacets de $\hat\Pi$, extension de $\widehat{\widehat\Gamma}=\operatorname{Aut}\operatorname{ext}_{\mathrm{lac}}(\hat\Pi)$ par $\hat\Pi$')
sb('complete numbered diagram (18), both terminal 1s, all hats, both Pi forms and ambiguous lower relation',[239,2085,1245,2355],diagram18)
sb('handwritten footer 22 omitted by H',[31,2276,126,2352],r'\mspage{22}')

diff_coverage=[]
def diff(row,keys=None,explanation=None):
    if keys:
        chosen=[ids[k] for k in keys]
        entry={'row':row,'status':'substantive'}
        if len(chosen)==1: entry['change_id']=chosen[0]
        else: entry['change_ids']=chosen
        if explanation: entry['explanation']=explanation
    else:
        entry={'row':row,'status':'macro/editorial','explanation':explanation}
    diff_coverage.append(entry)
diff(1,explanation='C scan identifier versus H editorial page-note syntax. The source header 10 is explicitly recognized in H as the author\'s page number, and is preserved in our inventory and B01; no omission of that source number is counted.')
diff(2,explanation='H editorial phrase de l\'auteur attached to its recognition of the source header 10; not manuscript prose.')
diff(3,['inverse'])
diff(4,['quoted'])
diff(5,['gen'])
diff(6,['relati'])
diff(7,['old0'])
diff(8,['oldinf1'])
diff(9,['oldinf2'])
diff(10,explanation='H editorial description of the two hatched left-hand trial products and the NB. Both trial products were independently read and retained, with their cancellation scope inventoried.')
diff(11,['nb'],explanation='The underlined NB itself is recognized by H\'s note; the actual short mark to its right, including its detached point, is a source inscription and a substantive omission.')
diff(12,['ayant','insert_gen'])
diff(13,['hom'])
diff(14,['decrits'])
diff(15,['four_points','separator','margin_prefix'],explanation='This token row combines H\'s ellipsis, the omitted separator drawing and omitted readable words in the margin; all are accounted for separately.')
diff(16,['margin_rho'])
diff(17,['autom_ext'])
diff(18,['designera'])
diff(19,explanation='The ornate S and index 3 agree; C retains an alphabet alternative while H chooses fraktur. The typographic uncertainty is retained in M0853 and doubts, with no certainty-only change row.')
diff(20,['autom_abbrev'])
diff(21,['insert_a'])
diff(22,explanation='Aut/ext versus Autext is operator macro/spacing syntax for the same written Aut ext sequence. No extra word or symbol is inferred from the macro split.')
diff(23,['no_colon'])
diff(24,explanation='TikZ environment token, not source text; substantive diagram letter forms and lower relation are separately logged.')
diff(25,explanation='TikZ arrow syntax versus longrightarrow: same first right-pointing connecting stroke, including its short dark head.')
diff(26,explanation='TikZ arrow syntax versus longrightarrow: same second right-pointing arrow.')
diff(27,explanation='TikZ arrow syntax versus longrightarrow: same third right-pointing arrow.')
diff(28,['vertical_relation','diagram_comma'],explanation='The main right arrow and terminal 1 agree. The token row also reaches the dependent vertical mark and H\'s punctuation/restatement, which are substantive.')
diff(29,['vertical_relation'],explanation='The lower expression is physically below the single Gamma; the short sign retains Vert/cup alternatives, without turning it into H\'s horizontal repeated-Gamma subset statement.')
diff(30,explanation='Closing TikZ environment token only.')
diff(31,['footer'],explanation='The handwritten lower-left 22 is absent from H; H\'s separate editorial explanation of the diagram is excluded from manuscript text.')

report=dict(
    scan=23,reader='/root/reader_a',lines_read=31,
    layout='Upright manuscript sheet. Header 10 near top centre. Five-line opening block and three-row system (17), with underlined NB and a separate small dash-over-point mark at upper right. Five base lines in the middle block, one interlinear phrase, then a short central separator. Slanted left-margin words On a les / relations and a detached rho lower down. Seven lower prose baselines, with an interlinear à above cancelled extérieurs; (18) below is a horizontal five-object row with a short vertical sign and Aut ext expression beneath its single Gamma. Footer 22 is at lower left. The 31 read units count text/formula baselines, separate insertions and marginal entries, header/footer and the diagram\'s three levels; the standalone separator is inventoried separately.',
    changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second_boxes,
    notation=[
        {'form':r'\Pi,\hat\Pi','places':['middle kernel clause','all six hatted group signs in lower prose and (18)'],'observation':'Each local sign has a full cap and two long descending legs. Read these as capital Pi. The right foot is sometimes curved; this does not make the form a one-stem Gamma.','qualification':'This local conclusion covers the seven occurrences on this sheet only.'},
        {'form':r'\Gamma,\hat\Gamma_{0,3},\widehat{\widehat\Gamma}','places':['lower product formula','lower inline Aut ext definition','(18)'],'observation':'Gamma has a long left stem and top stroke with only a short right return, distinct from the two full Pi legs. The double hats are separate carets.','qualification':'No case is changed from a numerical or group-theoretic expectation.'},
        {'form':r'\unsure{\mathfrak S_3|\mathcal S_3}','places':['lower product formula'],'observation':'Ornate rounded S and clear index 3; the exact typographic alphabet is unresolved.','qualification':'No normalization to a plain S or uniform alphabet elsewhere.'},
        {'form':r'\rho','places':['detached lower part of left margin note'],'observation':'Closed head, small return at the junction, and long descending stem.','qualification':'The symbol is kept isolated; no missing relation is supplied.'},
        {'form':r'\unsure{\Vert|\cup}','places':['under Gamma in (18)'],'observation':'Two short downward strokes with possible joining curvature at their feet.','qualification':'The diagram\'s surrounding algebra is not used to force equality or inclusion.'},
    ],
    hand=[
        {'habit':'Low compressed cursive sequences may lose easily separable letter boundaries.','places':['opening inverse/réciproque','désignera','signature'],'universal_on_page':False,'witness_effect':'The opening word remains inverse-first uncertain; H shortens désignera and leaves the signature phrase illegible.'},
        {'habit':'The long returning g descender can resemble an underline.','places':['signature','Malgoire','engendré'],'universal_on_page':False,'witness_effect':'No extra underline is supplied beneath signature; its low stroke is continuous with g.'},
        {'habit':'A full cap and two long legs identify the local capital Pi even at small size.','places':['kernel clause and six hatted group forms'],'universal_on_page':True,'witness_effect':'Both C and H transcribe these local capital outlines as small pi.'},
        {'habit':'Short word forms retain their actual punctuation.','places':['first gén','inserted gén.','two autom. forms','hom'],'universal_on_page':False,'witness_effect':'H expands gén and autom.; the first gén is unpunctuated while the inserted gén. and both autom. have stops.'},
        {'habit':'Cancelled indices can be overwritten heavily rather than struck cleanly.','places':['three old RHS indices in (17)'],'universal_on_page':False,'witness_effect':'H omits the earlier layers. All three remain uncertain because the old strokes are not fully recoverable.'},
    ],
    abbreviations=[
        {'form':'gén','expansion':'générateurs','place':'opening generator list; no stop written'},
        {'form':'gén.','expansion':'générateurs','place':'interlinear phrase in middle block'},
        {'form':'hom','expansion':'homomorphisme','place':'hom signature évident'},
        {'form':'autom.','expansion':'automorphismes','place':'both occurrences in lower paragraph'},
        {'form':'NB','expansion':'nota bene','place':'underlined upper-right margin'},
        {'form':r'\unsure{relati.}','expansion':'possibly relation(s), not resolved or expanded in the text','place':'cancelled short word before avec'},
    ],
    notes=[
        'The author identifies the preimage of the subgroup generated by tau with the cartographic group called triangulé pondéré and names Malgoire. The proper name was checked on its enlarged crop: capital M, a/l, descending g, o/i and r/e ending support Malgoire. The opening inverse/réciproque preference is determined from the local strokes and remains doubtful; no external source was consulted.',
        'The author writes three tau-product descriptions of l_0, l_1 and l_infinity in (17). Both hatched left trial products and all three earlier overwritten right-hand indices are preserved. The live products are transcribed as infinity,1 / 0,infinity / 1,0. None was altered to make a product identity hold.',
        'The next paragraph asserts a presentation using the tau generators and relations (16), gives a signature map to ±1, and identifies its kernel with the group generated by the l_i. There are four points after its final reference (17). The inserted phrase belongs before seules; its long insertion guide is not emphasis under the following text.',
        'The lower paragraph turns to exterior automorphisms with loops, introduces the profinite completion and a twice-hatted automorphism group, and writes their displayed relationships. The interlinear à replaces the cancelled extérieurs. The cancellation itself is definite, but the internal letters of extérieurs are retained with a local doubt because the strike merges them. The six hatted group signs and the middle kernel sign are locally capital Pi.',
        'Diagram (18) has one Gamma in its main row and an Aut ext expression below it. The small intervening vertical sign is not forced to equality or inclusion. No comma follows the last 1, and no colon follows the last prose hatted Pi. The NB mark is reproduced geometrically as a dash with a detached point below; its function is not assigned.',
        'The left-margin rho is a detached lower entry, not the beginning of a relation reconstructed by the reader. The central separator is an independent single stroke. The handwritten numbers are header 10 and lower-left footer 22. H explicitly recognizes the header 10 in an editorial author-page note, so that note is treated as a representational difference; H has no corresponding reading of footer 22, which is counted as an omission.',
        'Every agreed word and mathematical sign was read against the whole/native-half evidence; every C deletion and insertion is separately inventoried. Whole sheet and each native half were successfully viewed once. The first attempted bottom-half tool result was truncated before a usable image was delivered, so its one successful native view followed context compaction. Thirteen crops were saved and each inspected; the opening crop alone was revisited, without remaking it, to reassess the disputed word. Root reviewed the same crop set independently. No OCR, outside page, external research, second reading, or TeX compilation was used.',
        'No mathematical assertion was independently proved, computed or used to supply a reading in this reader report. Mathematical checks are reserved for the root reader\'s separate record.',
    ],
    check_events=[],diff_coverage=diff_coverage,
)
(out/'145_scan023.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'marks':len(decisions),'unlisted_C_marks':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second_boxes),'diff_rows':len(diff_coverage),'crop_count':len(manifest)},ensure_ascii=False))
