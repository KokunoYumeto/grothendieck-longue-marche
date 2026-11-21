from pathlib import Path
import json

out = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work/reader_returns')
crop_root = out.parent / 'crops'

def crop(place):
    name = f'150_scan026_{place}.jpg'
    meta = json.loads((crop_root / name).with_suffix('.json').read_text())
    return name, meta['box']

changes=[]
def change(place,C,H,final,evidence,cp,kind,error_kind,confidence='high',marked_in_H=False,change_C=False,change_H=True,consequential=''):
    name,box=crop(cp)
    changes.append(dict(place=place,C=C,H=H,final=final,evidence=evidence,crop=name,box=box,confidence=confidence,kind=kind,error_kind=error_kind,marked_in_H=marked_in_H,change_C=change_C,change_H=change_H,consequential=consequential))

change('line 1 / left endpoint of the parameter interval',
       r"\lambda_0,\lambda'_0\in]0,1]",r"\lambda_0,\lambda'_0\in[0,1]",
       r"\lambda_0,\lambda'_0\in\unsure{]0,1]|[0,1]}",
       'The left bracket has two retraced upright strokes and horizontal returns in both directions. The right bracket and the digits 0,1 are clear. The retracing does not safely establish whether the left endpoint is open or closed; the disagreement is explicitly left unresolved.',
       'parameters','other','symbols and indices',confidence='low',change_C=False,change_H=False,
       consequential='The unresolved bracket controls whether the zero scale parameter is included.')
change('line 4 / de deux', 'de deux', 'des deux', 'de deux',
       'The first word is the looped d followed by a single low e return; there is no additional s before the separately begun d of deux.',
       'de_deux','misread word','words')
change('insertion above line 6 / heading stop',r'\inserted{\uline{Prop.}}',r'\emph{Prop.}',r'\inserted{\uline{Prop}}',
       'The abbreviation consists of P-r-o-p with an underline. The small middle dot belongs to the compressed o; there is no separate terminal stop after the p. A curved leader attaches the heading before Si.',
       'prop_leader','abbreviation expanded or spelling modernised','abbreviation/spelling',change_C=True,change_H=True)
change('line 6 / arrow in the descriptive tuple',
       r'(\widetilde X,\dot X,\mathcal E_{\dot X},Y,\dot X\unsure{-|\to}Y)',
       r'(\tilde X,\dot X,\mathcal E_{\dot X},Y,\dot X\to Y)',
       r'(\widetilde X,\dot X,\mathcal E_{\dot X},Y,\dot X\to Y)',
       'The horizontal shaft has a short downward terminal head at its right end, matching both map arrows in b). It is not an undecorated minus. The full tuple and the dot on the indexed X are visible.',
       'description_tuple','misread symbol or index','symbols and indices',change_C=True,change_H=False,
       consequential='The final item of the tuple is a map from dot X to Y.')
change('line 6 / closing parenthesis after descriptive tuple',
       r'\dot X\unsure{-|\to}Y)$,',r'\dot X\to Y)$\add{)},',r'\dot X\to Y)$,',
       'There is one closing parenthesis for the descriptive tuple, followed by a comma. There is no second inserted closing parenthesis. The separate curve before Si belongs to the Prop insertion leader; H also supplies an opening parenthesis editorially, which has not been treated as manuscript ink.',
       'description_tuple','text not on the page','text not on page')
change('line 7 / main word and insertion before the pair',
       r'\unsure{lors|alors|les} \inserted{les} $(X_0,\mathcal E)$',
       r'alors les \add{couples} $(X_0,\mathcal E)$',
       r'lors \inserted{les} $(X_0,\mathcal E)$',
       'The baseline word begins directly with a tall looped l, then the low o/r/s run; there is no initial a. Above it, les is attached by a curved leader immediately before the pair. No separate word couples is written at this place. The awkward wording is retained rather than repaired.',
       'lors_insertions','misread word','words',change_C=True,change_H=True)
change('line 8 / structure cône', 'structure cônique', 'structure cônique', 'structure cône',
       'The word has c, the small o loop with an accent above it, and a short n/e ending. There is no i dot or q descender. The q descenders in the nearby occurrences of cylindrique are conspicuous. The visible word is cône, although both witnesses expand it to cônique.',
       'conique','misread word','words',change_C=True,change_H=True,
       consequential='This records the author’s noun-form terminology structure cône; it is not a change to a mathematical claim.')
change('line 9 / tilde on the neighborhood symbol in the system',
       r'\widetilde{\mathcal E}_{\widetilde X_0}',r'\mathcal E_{\tilde X_0}',r'\widetilde{\mathcal E}_{\widetilde X_0}',
       'Two distinct wavy marks are visible: one above the main neighborhood symbol and one above the subscript X. H retains only the latter.',
       'systems_tuple','misread symbol or index','symbols and indices',consequential='The marked neighborhood germ over tilde X_0 is distinguished from the other neighborhood germs.')
change('line 9 / cancelled delimiter inside the system',
       r'\deleted{\unsure{\}}}', '[absent]', r'\deleted{\unsure{\}|)}}',
       'A tall closing-shaped sign immediately after the neighborhood symbol has been crossed with short diagonal strokes. Its outer contour could be a curly brace or a parenthesis; the cancellation prevents a secure choice. Its presence and deletion state are clear, so it is retained with uncertainty.',
       'systems_tuple','omission','struck text',confidence='medium')
change('line 10 / cancelled object before live tilde X',
       r'\deleted{$\unsure{\mathcal E}$}', '[absent]', r'\deleted{$\unsure{X_0|\mathcal E_{X_0}}$}',
       'The cancelled patch preserves an X-like crossing near its bottom and a small closed 0 at the lower right. The dense upper cancellation does not establish whether these constitute the whole X_0 or an index under an E-like letter. The proposed alternatives retain those readable lower strokes without pretending to recover the obscured upper writing.',
       'deleted_E','misread symbol or index','symbols and indices',confidence='low',change_C=True,change_H=True)
change('line 11 / first singular neighborhood phrase',
       'voisinage cylindrique','voisinages cylindriques','voisinage cylindrique',
       'Both words end in the final e return; no separate s is visible at either word end. The following neighborhood symbol begins independently.',
       'neighborhood_1','misread word','words')
change('line 11 / tilde on neighborhood symbol',
       r'\widetilde{\mathcal E}_{\widetilde X_0}',r'\mathcal E_{\tilde X_0}',r'\widetilde{\mathcal E}_{\widetilde X_0}',
       'The wavy mark over the main symbol and the separate wavy mark over its indexed X are both explicit.',
       'neighborhood_1','misread symbol or index','symbols and indices')
change('line 13 / cancelled beginning of voisinage',
       r'\deleted{vois.}',r'\struck{voisin}',r'\deleted{\unsure{vois.|voisin}}',
       'The initial voi sequence survives a horizontal cancellation. The final compressed strokes and any terminal stop are obscured by that cancellation, so the competing abbreviated and longer readings are not safely resolved. This row records the substantive witness disagreement without claiming a correction.',
       'neighborhood_2','other','struck text',confidence='low',change_C=False,change_H=False)
change('line 13 / second singular neighborhood phrase',
       'voisinage cylindrique','voisinages cylindriques','voisinage cylindrique',
       'The live replacement phrase is separate from the cancelled beginning. Its two words each end with the same low e return as the singular phrase in line 11; no final s is present.',
       'neighborhood_2','misread word','words')
change('line 16 / tilde on first symbol of condition a)',
       r'\widetilde{\mathcal E}_{\widetilde X_0}',r'\mathcal E_{\tilde X_0}',r'\widetilde{\mathcal E}_{\widetilde X_0}',
       'A separate wavy accent is plainly present over the main E-like symbol, as well as over the X in its index; the other neighborhood symbol has a dot on its X and no tilde over E.',
       'condition_a','misread symbol or index','symbols and indices')
change('lines 17–18 / vertical identity annotation',
       r'\dot X_0\subset\dot X \inserted{$\dot X_0=\widetilde X_0\cap\dot X$}',
       r'\dot X_0\subset\dot X \add{($\dot X_0=\tilde X_0\cap\dot X$)}',
       r'\underset{\inserted{\substack{\Vert\\\widetilde X_0\cap\dot X}}}{\dot X_0}\subset\dot X',
       'Under the baseline dot X_0 stand two short parallel vertical strokes, with tilde X_0 cap dot X directly below. There is no second written dot X_0, no horizontal equality sign, and no enclosing pair of parentheses. The proposed TeX preserves the vertical relation and its attachment.',
       'a_insertions','insertion or placement','insertion placement',change_C=True,change_H=True,
       consequential='The annotation identifies dot X_0 with the intersection tilde X_0 cap dot X, retaining the manuscript’s vertical geometry.')
change('lines 17–18 / location and index of inserted dans dot X',
       r'\uline{compatibles} --- donc ... structure cylindrique \inserted{dans $\dot X$}',
       r'\emph{compatibles} dans \add{$\tilde X$}, donc ... structure cylindrique',
       r'germe de structure cylindrique \inserted{dans $\dot X$} (induit par',
       'The words dans dot X are above the gap after cylindrique and before the parenthesis. A curved insertion leader descends exactly to that gap. The accent on X is an isolated dot/stroke, not a tilde. The earlier line has only compatibles followed by a dash and donc.',
       'a_insertions','insertion or placement','insertion placement',consequential='The inserted ambient space belongs to the inherited cylindrical structure in dot X.')
change('line 18 / apparent repeated germe',
       'germe de structure',r'\struck{germe} germe de structure','germe de structure',
       'There is one baseline word extending from the heavily retraced initial to the e/m/e run. The initial has overlapping loops, but no distinct second complete germe can be isolated. I therefore retain the one readable word and do not add H’s separate cancelled full word. The retracing remains a second-pass target.',
       'germe','text not on the page','text not on page',confidence='medium')
change('line 19 / marked neighborhood symbol closing a)',
       r'\widetilde{\mathcal E}_{\widetilde X_0}',r'\mathcal E_{\tilde X_0}',r'\widetilde{\mathcal E}_{\widetilde X_0}',
       'Both wavy accents are clear in this isolated formula: one above the main symbol and one above the indexed X_0.',
       'E_closing','misread symbol or index','symbols and indices')
change('line 19 / punctuation after closing parenthesis',
       r'$\widetilde{\mathcal E}_{\widetilde X_0}$)',r'$\mathcal E_{\tilde X_0}$) ;',r'$\widetilde{\mathcal E}_{\widetilde X_0}$)',
       'The closing parenthesis is followed by blank paper before the next item; no semicolon is present.',
       'E_closing','text not on the page','text not on page')
change('line 20 / cancelled morphism formula',
       r'\deleted{$(\dot X,\unsure{\mathcal E})\longrightarrow(Y,$}',
       r'\struck{$(\dot X,\ldots)\to(Y,\ldots)$}',
       r'\deleted{$(\dot X,\unsure{\mathcal E})\longrightarrow(Y,$}',
       'The first source pair has a cancelled E-like token, still uncertain, and a visible closing parenthesis. The right-hand expression stops after the comma following Y. No three-dot sequence or closing right parenthesis is visible there. The full original map is crossed horizontally, with its replacement above it.',
       'morphism','text not on the page','text not on page',confidence='medium')
change('line 20 / arrow in inserted map',
       r'\dot X\overset{p}{\unsure{-|\longrightarrow}} Y',r'\dot X\xrightarrow{\ p\ }Y',r'\dot X\overset{p}{\longrightarrow} Y',
       'The shaft has a short downward head at its right end, like the cancelled arrow below and the map in line 6. The p label is above the shaft. Those repeated arrow forms resolve the dash/arrow ambiguity.',
       'morphism','misread symbol or index','symbols and indices',change_C=True,change_H=False)
change('line 22 / évident', 'évident', '[absent]', 'évident',
       'The word is written at the left of the line, with its initial accent and the final t, immediately before the insertion leader and qu’il existe.',
       'evident_inverse','omission','omissions')
change('line 22 insertion / underline on et',
       r'\inserted{que $\dot X_0=\unsure{\beta|p}^{-1}(Y_0)$, et}',
       r'\add{que $\dot X_0=p^{-1}(Y_0)$, et}',
       r'\inserted{que $\dot X_0=\unsure{p|\beta}^{-1}(Y_0)$, \uline{et}}',
       'Immediately below et is a short independent underline; the longer curved insertion leader lies farther below and runs under the whole added clause. The inverse-map letter remains uncertain because it intersects the previous line’s closing parenthesis; favoring p does not claim to settle that mark.',
       'evident_inverse','omission','omissions',change_C=True,change_H=True)
change('line 23 / représentatifs', 'représentatifs','respectifs','représentatifs',
       'The initial re-pré run is followed by the extended senta sequence and a tall terminal t/f formation before s. The word is visibly longer than respectifs and contains the internal strokes omitted by H.',
       'representatives','misread word','words')
change('line 23 / des deux', 'des deux','de ces','des deux',
       'Two separate words are visible: the first has the terminal s return, and the second begins with the same looped d used in données/de elsewhere, followed by the low eux run.',
       'representatives','misread word','words')
change('line 23 / envisagés', 'envisagés',r', \uncertain{munis de}','envisagés',
       'A single word follows germes. Its initial en/vi run, s, long g descender and final accented ending are visible. There is no separately begun de or preceding comma at this place.',
       'representatives','misread word','words',marked_in_H=True)
change('line 24 / cancelled prefix before products',
       r'\deleted{\unsure{\dot X_0}}',r'\struck{\ill{}}',r'\deleted{\unsure{\dot X_0|X_0}}',
       'A crossed X-like letter and a closed lower-right 0 remain readable. The cancellation covers the upper part where a dot may have stood, so that detail stays uncertain. H’s complete illegibility omits those readable components.',
       'final_formula',r'readable ink left as \ill{}','readable ink left as illegible',confidence='medium',marked_in_H=True)
change('line 24 / first product relation',
       r'E_{\dot X}=\dot X_0\times I',r'E_{\dot X}\simeq\dot X_0\times\mathbf{I}',r'E_{\dot X}\simeq\dot X_0\times I',
       'The upper stroke of the relation is visibly wavy, above a straight lower bar, matching the relation in the second product. It is not an ordinary equality sign. I is the same capital serifed I in both products; typographic boldness in H is not counted as a reading difference.',
       'final_formula','misread symbol or index','symbols and indices',change_C=True,change_H=False,
       consequential='The first product relation is an isomorphism sign, as in the second product, rather than literal equality.')
change('bottom left margin / separate foliation',r'\margin{25}','[absent]',r'\margin{25}',
       'The thin grey figures are a 2 followed by a 5. This is separate foliation, visually distinct from the dark 8 at the top; its writer is not securely identified.',
       'folio','omission','omissions')

marks=[]
def mark(m,context,decision,reading,evidence,cp,confidence):
    name,box=crop(cp)
    marks.append(dict(mark=m,context=context,decision=decision,reading=reading,evidence=evidence,crop=name,box=box,confidence=confidence))
mark(r'\unsure{-|\to}',r'\mathcal E_{\dot X},Y,\dot X\unsure{-|\to}Y','alternative',r'\to',
     'A right terminal downward head matches the two map arrows of b); the sign is not a plain minus.','description_tuple','high')
mark(r'\unsure{lors|alors|les}',r'Y)$, \unsure{lors|alors|les} \inserted{les}','first','lors',
     'The initial is a tall l with no a before it; the following low o/r/s run is longer than the inserted les above.','lors_insertions','high')
mark(r'\unsure{\}}',r'\widetilde{\mathcal E}_{\widetilde X_0}\deleted{\unsure{\}}}','undecided',r'\unsure{\}|)}',
     'A closing-shaped sign is crossed; the surviving contour admits a brace or parenthesis. The cancellation prevents full recovery.','systems_tuple','low')
mark(r'\unsure{\mathcal E}',r'partie bordante de \deleted{$\unsure{\mathcal E}$}','undecided',r'\unsure{X_0|\mathcal E_{X_0}}',
     'The lower X-like crossing and 0 are visible, but the dense upper cancellation leaves the whole symbol versus indexed-symbol alternatives unresolved.','deleted_E','low')
mark(r'\unsure{ces}',r'$\mathcal E_{Y_0}$, \unsure{ces} données','undecided',r'\unsure{ces|les}',
     'The initial has overlapping strokes and a tall l-like loop; the ending es is clearer. The crop does not securely distinguish a retraced c from l.','ces','low')
mark(r'\unsure{\mathcal E}',r'\deleted{$(\dot X,\unsure{\mathcal E})\longrightarrow(Y,$}','undecided',r'\unsure{\mathcal E}',
     'The source token is crossed several times. An E-like outline remains possible, but the overlying diagonals prevent recovery of every stroke.','morphism','low')
mark(r'\unsure{-|\longrightarrow}',r'\inserted{$\dot X\overset{p}{\unsure{-|\longrightarrow}} Y$}','alternative',r'\longrightarrow',
     'A short head points down from the right end of the shaft, the same convention as the cancelled map immediately below.','morphism','high')
mark(r'\unsure{\beta|p}',r'\dot X_0=\unsure{\beta|p}^{-1}(Y_0)','undecided',r'\unsure{p|\beta}',
     'A p-like stem and bowl are visible, but the closing parenthesis from the line above overlaps the top, creating a beta-like extra loop. The map label p supports the first alternative without making the ink certain.','evident_inverse','medium')
mark(r'\unsure{\dot X_0}',r'\deleted{\unsure{\dot X_0}}\quad E_{\dot X}','undecided',r'\unsure{\dot X_0|X_0}',
     'X and the lower 0 survive cancellation; a separate upper dot cannot be confirmed through the zigzag strokes.','final_formula','low')

inventory=[]
def item(element,kind,position,first,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
item('source-page-number','margin note','top left','8')
item('nb-paragraph','text','lines 1–2','NB Cette condition implique que pour')
item('symmetry-paragraph','text','lines 3–5','Si T est aussi cylindrique')
item('inserted-proposition-heading','insertion','above line 6, left','underlined Prop, with curved leader before Si')
item('proposition-main-text','text','lines 6–15','Si (X,Y,mathcal T) est décrit par')
item('inserted-les','insertion','above line 7, before (X_0,mathcal E)','les')
item('inserted-germes-proposition','insertion','above line 7, before structures','germes de')
item('cancelled-couples','deletion','line 9, after aux','couples')
item('replacement-systemes','insertion','above cancelled couples in line 9','systèmes')
item('system-tuple','display','line 9, after systèmes','(tilde X_0, tilde E_{tilde X_0}, Y_0, E_{Y_0})')
item('cancelled-internal-delimiter','deletion','line 9, after tilde E_{tilde X_0}','uncertain closing brace or parenthesis')
item('retraced-leading-X0','text','line 10, after où','tilde X_0; heavy retracing does not establish a separate recoverable erased token')
item('cancelled-object-before-X','deletion','line 10, before live tilde X','uncertain X_0 or E_{X_0}')
item('cancelled-vois','deletion','line 13, between de and voisinage','uncertain vois. or voisin')
item('condition-a-body','text','lines 16–19','a) tilde E_{tilde X_0} et E_{dot X}')
item('inserted-germes-a','insertion','above line 16, before structures','germes de')
item('vertical-intersection-identity','insertion','below dot X_0 in line 17','two vertical strokes above tilde X_0 cap dot X')
item('retraced-germe','text','line 18, beginning','germe; initial loops retraced, no separately established complete struck germe')
item('inserted-dans-X','insertion','above line 18, after cylindrique','dans dot X, with curved leader before (induit par')
item('condition-b-body','text','lines 20–24','b) Le morphisme ... est compatible')
item('cancelled-original-morphism','deletion','line 20','(dot X, uncertain E) to (Y,')
item('replacement-p-map','insertion','above cancelled morphism in line 20','dot X with p-labelled arrow to Y')
item('inverse-image-clause','insertion','above line 22, after évident','que dot X_0 = uncertain p^{-1}(Y_0), underlined et')
item('cancelled-product-prefix','deletion','line 24, before E_{dot X}','uncertain dot X_0 or X_0')
item('product-identifications','display','line 24','E_{dot X} simeq dot X_0 times I, E_Y simeq Y_0 times I, tels que')
item('thin-foliation','margin note','bottom left','25','thin separate foliation; attribution uncertain')

second=[]
def secondbox(kind,coords,reading,reason):
    second.append(dict(box=f'b{len(second)+1:02d}',kind=kind,coords=list(coords),reading=reading,reason=reason))
secondbox('margin note|handwritten number',(29,24,82,72),r'\mspage{8}','The authorial page number is a handwritten numeral in the top margin.')
secondbox('doubt formula|handwritten number',(1250,75,1605,181),r"\lambda_0,\lambda'_0\in\unsure{]0,1]|[0,1]}",'The entire formula includes the newly doubtful retraced bracket and every parameter/endpoint numeral.')
secondbox('handwritten number',(264,167,682,263),r'\underset{E}{\lambda_0}E\quad\text{et}\quad\underset{T}{\lambda\prime_0}T','Both scale factors contain handwritten zero subscripts and low action labels E/T.')
secondbox('C/H word difference',(1035,321,1300,415),'de deux','C has de, H des; the complete words are boxed.')
secondbox('insertion',(233,506,445,650),r'\inserted{\uline{Prop}}','Inserted heading and its curved leader; also the omitted terminal stop present in both witnesses.')
secondbox('doubt formula',(1197,547,1644,701),r'(\widetilde X,\dot X,\mathcal E_{\dot X},Y,\dot X\to Y)',r'The whole descriptive tuple contains C’s dash/arrow doubt; the closing punctuation disagreement is also covered.')
secondbox('insertion|handwritten number|C/H word difference',(250,634,615,762),r'lors \inserted{les} $(X_0,\mathcal E)$','C/H disagree over lors/alors and added les/couples; the inserted les and the zero in X_0 are included.')
secondbox('insertion',(612,630,838,716),r'\inserted{germes de}','Complete inserted phrase and its attachment immediately before structures.')
secondbox('C/H word difference',(1138,744,1411,841),r'cône $\mathcal T$','New reader departure from the agreeing witnesses cônique; the whole disputed word and following symbol are included for independent review.')
secondbox('insertion|struck passage',(615,818,837,953),r'\deleted{couples}\inserted{systèmes}','The struck word and its replacement above it are both mandatory targets.')
secondbox('doubt formula|struck passage|handwritten number',(837,818,1470,962),r'(\widetilde X_0,\widetilde{\mathcal E}_{\widetilde X_0}\deleted{\unsure{\}|)}},Y_0,\mathcal E_{Y_0})','The full system tuple contains the uncertain cancelled delimiter and all its zero subscripts.')
secondbox('handwritten number',(392,939,569,1060),r'\widetilde X_0\ \text{est}','The zero and heavily retraced main X are covered together; no separate erased underletter is established.')
secondbox('struck passage|doubt formula|handwritten number|low-confidence departure',(1209,939,1426,1056),r'\deleted{\unsure{X_0|\mathcal E_{X_0}}}\ \widetilde X','The whole cancelled object and following live symbol; low-confidence departure from C preserves the visible lower 0.')
secondbox('C/H word difference|handwritten number',(788,1036,1646,1157),r'voisinage cylindrique $\widetilde{\mathcal E}_{\widetilde X_0}$,','The singular/plural disagreement, both tildes and the indexed zero are covered.')
secondbox('handwritten number',(426,1144,534,1240),r'Y_0','The zero in the separately stated Y_0 is mandatory.')
secondbox('struck passage|C/H word difference',(805,1217,1573,1345),r'\deleted{\unsure{vois.|voisin}} voisinage cylindrique','The whole cancelled word and the live singular phrase cover both lexical disagreements.')
secondbox('handwritten number',(258,1335,407,1446),r'\mathcal E_{Y_0},','The zero in E_{Y_0} at the start of line 14 is mandatory.')
secondbox('low-confidence departure',(481,1331,845,1441),r'\unsure{ces|les} données','C’s doubtful ces has a retraced initial; added les alternative remains unresolved.')
secondbox('insertion',(1124,1476,1367,1591),r'\inserted{germes de}','Every insertion is mandatory; this one precedes structures in a).')
secondbox('handwritten number',(485,1526,848,1627),r'\widetilde{\mathcal E}_{\widetilde X_0}\ \text{et}\ \mathcal E_{\dot X}','The first neighborhood index contains zero; the distinct tilde/dot marks are included.')
secondbox('insertion|handwritten number',(1058,1628,1290,1795),r'\underset{\inserted{\substack{\Vert\\\widetilde X_0\cap\dot X}}}{\dot X_0}\subset\dot X','The baseline and inserted identity must be seen as one vertically aligned expression; both zeros are covered.')
secondbox('insertion|C/H word difference',(1285,1693,1503,1841),r'\inserted{dans $\dot X$} (induit','The complete added phrase, dotted X and attachment after cylindrique are mandatory; H relocates it and reads a tilde.')
secondbox('C/H word difference',(281,1754,612,1861),'germe de','H adds a separately cancelled full germe; the heavily retraced initial of the single visible word needs review.')
secondbox('handwritten number',(307,1852,493,1965),r'\widetilde{\mathcal E}_{\widetilde X_0})','The indexed zero and closing punctuation after a) are covered.')
secondbox('insertion|struck passage|doubt formula',(959,1852,1446,2020),r'\deleted{(\dot X,\unsure{\mathcal E})\longrightarrow(Y,}\quad\inserted{\dot X\overset{p}{\longrightarrow}Y}',r'The entire cancelled and replacement maps include both C formula doubts, the map label and the right-hand truncation.')
secondbox('handwritten number',(454,2016,1225,2142),r'(\dot X_0,\mathcal E_{\dot X_0})\ \text{et}\ (Y_0,\mathcal E_{Y_0})','All four zero-bearing occurrences in the two pairs are included together.')
secondbox('insertion|doubt formula|handwritten number|C/H word difference',(320,2091,1024,2237),r'évident \inserted{que $\dot X_0=\unsure{p|\beta}^{-1}(Y_0)$, \uline{et}}','This includes omitted évident, the whole added clause, the inverse-map doubt, zeros and exponent 1, and the independent underline under et.')
secondbox('C/H word difference',(320,2189,1357,2305),'représentatifs des deux germes envisagés','The full line covers représentatifs/respectifs, des deux/de ces, and envisagés/munis de.')
secondbox('struck passage|doubt formula|handwritten number',(607,2247,1431,2345),r'\deleted{\unsure{\dot X_0|X_0}}\quad E_{\dot X}\simeq\dot X_0\times I,\qquad E_Y\simeq Y_0\times I,','The whole final formula includes the cancelled C doubt, product zero subscripts, and the changed first relation sign.')
secondbox('margin note|handwritten number',(24,2290,91,2346),r'\margin{25}','The separate thin foliation is omitted by H and contains handwritten digits.')

result=dict(
 scan=26,reader='reader_b',line_count=24,changes=changes,marks=marks,inventory=inventory,
 doubts=[
  dict(place='line 1 / interval',reading=r'\unsure{]0,1]|[0,1]}',alternatives='Open or closed left endpoint; the left bracket is retraced.',confidence='low'),
  dict(place='line 9 / cancelled internal delimiter',reading=r'\unsure{\}|)}',alternatives='Closing curly brace or parenthesis under cancellation.',confidence='low'),
  dict(place='line 10 / cancelled object',reading=r'\unsure{X_0|\mathcal E_{X_0}}',alternatives='Whole X_0 or an E-like main symbol with X_0 below; upper strokes are obscured.',confidence='low'),
  dict(place='line 13 / struck beginning',reading=r'\unsure{vois.|voisin}',alternatives='The final letters and terminal stop of the cancelled beginning are not independently recoverable.',confidence='low'),
  dict(place='line 14 / ces',reading=r'\unsure{ces|les}',alternatives='The es ending is clearer than the retraced initial c/l.',confidence='low'),
  dict(place='line 20 / cancelled pair',reading=r'\unsure{\mathcal E}',alternatives='An E-like token is possible under dense cancellation; no secure alternative recovered.',confidence='low'),
  dict(place='line 22 insertion / inverse map letter',reading=r'\unsure{p|\beta}',alternatives='p favored by stem/bowl and the map label; beta-like appearance may be produced by overlap from the closing parenthesis above.',confidence='medium'),
  dict(place='line 24 / cancelled prefix',reading=r'\unsure{\dot X_0|X_0}',alternatives='X_0 is partly readable; a separate dot above X is obscured.',confidence='low')
 ],
 notes=[
  'This handwritten page reports that the preceding compatibility condition implies compatibility of the two scaled structures, then states symmetry when T is also cylindrical. These are manuscript claims; this reading has not verified their proofs or the preceding definition.',
  'The proposition describes compatible cylindrical germs (X_0,E) by systems over the descriptive data for (X,Y,T). Condition a) requires compatible cylindrical germs and identifies dot X_0 vertically with tilde X_0 cap dot X. Condition b) requires compatibility of the map to Y with the indicated germs and begins choosing representative cylindrical neighborhoods. The sentence stops at tels que on this leaf.',
  'The main text has 24 physical baseline lines, excluding the interlinear insertions and the two margin numbers. All 24 were read from the native halves, including words on which C and H agreed; no OCR or TeX compilation was used.',
  'The manuscript page number is 8. The bottom-left 25 is thin separate foliation; its attribution is uncertain. No date is written on the page.',
  'Prop has no clearly visible terminal stop. The literal word cône is retained in structure cône; both witnesses give cônique. The baseline word lors likewise retains its absent initial a rather than silently supplying alors.',
  'Several source cancellations remain unreadable in part. No cancelled doubt has been declared settled merely from the mathematical context. The overwritten initial of germe and the retraced leading tilde X_0 have not been expanded into additional complete erased words or letters without secure ink evidence.',
  'The two vertical strokes below dot X_0 express an identity in the manuscript’s vertical arrangement. They have not been normalized into a new horizontal equation or into a diagram.',
  'The nearby displayed map label is p; the inverse-image insertion is still ambiguous because strokes from the previous line overlap it. A p reading is favored but not asserted as certain.',
  'The action labels E and T are placed low beneath/at the right of the scale factors. C’s underset representation has been retained; H’s linearized subscript syntax has not been counted as a different lexical reading.',
  'No genuine figure or commutative diagram occurs on this page. Curved lines next to Prop, les, germes de, dans dot X, and the inverse-image clause are insertion leaders, not extra parentheses or drawings.',
  'All 22 first-pass crop files listed by this return were generated once with the supplied helper and visually inspected. The second_boxes list provides 30 coherent targets for the independent second pass; it includes every insertion, cancellation, handwritten number, disputed C formula and C/H word difference.'
 ],
 check_events=[
  dict(statement_id='150.026.N1',type='carried as background without fault found',outcome='The NB compatibility assertion was transcribed. Its prior condition is not supplied on this page, and no proof check was performed.'),
  dict(statement_id='150.026.N2',type='carried as background without fault found',outcome='The symmetry assertion for two cylindrical structures was read as a manuscript assertion. No independent re-proof was attempted.'),
  dict(statement_id='150.026.P1',type='carried as background without fault found',outcome='The beginning of the correspondence proposition and conditions a), b) were transcribed. The statement continues beyond this leaf, so this is a reading record and not a mathematical verification.')
 ],
 notation=[
  dict(form=r'\underset{E}{\lambda_0}E,\quad\underset{T}{\lambda\prime_0}T',meaning_or_shape='Scale factors with small structure labels E/T placed below or low at the right; the labels are distinct from the following main E/T.',places='line 2'),
  dict(form=r'\widetilde X,\quad\dot X',meaning_or_shape='The tilde is a short wave; the dot is detached and sometimes elongated. They remain distinct throughout the page.',places='descriptive tuple, system, a), b)'),
  dict(form=r'\widetilde{\mathcal E}_{\widetilde X_0}',meaning_or_shape='The cylindrical neighborhood germ on tilde X_0 explicitly carries a tilde on the main E-like symbol and another tilde on the indexed X.',places='lines 9, 11, 16, 19'),
  dict(form=r'\mathcal E_{\dot X},\quad\mathcal E_{Y_0}',meaning_or_shape='E-like calligraphic neighborhood symbols with dotted-X or Y_0 subscripts; no tilde is supplied to their main symbols.',places='lines 6, 9, 14, 16, 21'),
  dict(form=r'\underset{\substack{\Vert\\\widetilde X_0\cap\dot X}}{\dot X_0}',meaning_or_shape='An inserted identity uses two vertical strokes between stacked expressions, not a baseline equality sign.',places='below line 17'),
  dict(form=r'\dot X\overset{p}{\longrightarrow}Y',meaning_or_shape='The map arrow has a horizontal shaft and only a short downward terminal head; p is above it.',places='replacement map above line 20'),
  dict(form=r'E_{\dot X}\simeq\dot X_0\times I,\quad E_Y\simeq Y_0\times I',meaning_or_shape='Both product relations have a wavy upper stroke and straight lower bar. The interval letter is a serifed capital I.',places='line 24')
 ],
 abbreviations=[
  dict(form='NB',expansion='nota bene'),
  dict(form='Prop',expansion='Proposition; no terminal stop is visible in this occurrence'),
  dict(form=r'\unsure{vois.|voisin}',expansion='Cancelled beginning of voisinage; the exact abbreviated or unfinished form remains uncertain')
 ],
 hand_log=[
  dict(habit='A map arrow may end in only a short downward terminal stroke, making it resemble a minus with a tiny hook.',places='line 6 descriptive tuple; line 20 cancelled and inserted maps',consistent='All three map arrows seen on this page have that abbreviated right head.',witness_errors='C leaves the two live arrows as dash/arrow doubts; both are resolved from the repeated ink form. H reads them as arrows.'),
  dict(habit='A tilde over a calligraphic E is separate from, and may sit well to the left of, the tilde over its indexed X.',places='lines 9, 11, 16, 19',consistent='All four visible occurrences of the tilde-X_0 neighborhood symbol carry both tildes.',witness_errors='H drops the tilde on the main E-like symbol at all four occurrences; C preserves it.'),
  dict(habit='Curved insertion leaders sweep under added phrases and descend into the intended gap, sometimes resembling parentheses.',places='Prop above line 6; les and germes de above line 7; germes de above line 16; dans dot X above line 18; inverse clause above line 22',consistent='All these additions have a leader or clear interlinear placement; the vertical identity uses two upright strokes instead.',witness_errors='H adds/supplies enclosing parentheses around the proposition opening and the identity annotation, and relocates dans dot X.'),
  dict(habit='Fast final e returns must not automatically be read as plural s.',places='voisinage cylindrique in lines 11 and 13; de deux in line 4',consistent='The two neighborhood phrases have matching singular endings. No general rule beyond these checked occurrences is asserted.',witness_errors='H reads both phrases as plural and de as des; C follows the visible singular and de endings.'),
  dict(habit='Long q descenders are conspicuous even in compressed words; their absence can discriminate cône from cônique.',places='cône in line 8 compared with nearby cylindrique/cylindriques',consistent='The inspected cylindrique forms show descending q strokes; the short word cône has none.',witness_errors='Both C and H give cônique at line 8, despite the shorter written form.'),
  dict(habit='Dots and small zeroes may both be dark or filled, but are placed above versus below/right of the X or lambda.',places='parameters, X_0 indices, dot X, and final products',consistent='The visible non-cancelled occurrences distinguish the positions consistently; the cancelled prefix is an exception where the upper dot remains uncertain.',witness_errors='No new zero/dot error established in the live text; the cancelled forms remain uncertain.'),
  dict(habit='Retracing may create extra loops that resemble another letter; do not infer a complete erased word from one tangled initial.',places='line 10 leading tilde X_0; line 14 ces/les; line 18 germe; inverse-map letter in line 22',consistent='These local cases differ and do not establish a general letter substitution habit.',witness_errors='H supplies a full struck germe before the single visible word; C’s ces and inverse-letter doubts remain partly unresolved.')
 ],
 second_boxes=second
)

for collection in [changes,marks]:
    for x in collection:
        assert (crop_root/x['crop']).is_file(),x['crop']
assert len(marks)==9
assert len(second)==30
assert len(list(crop_root.glob('150_scan026_*.jpg')))==22
(out/'150_scan026.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'marks':len(marks),'inventory':len(inventory),'second_boxes':len(second),'crop_count':22,'json':str(out/'150_scan026.json')},indent=2))
