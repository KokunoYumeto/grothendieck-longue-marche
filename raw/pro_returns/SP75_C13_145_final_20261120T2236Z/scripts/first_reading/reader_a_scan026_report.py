from pathlib import Path
import json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=root/'edition/reader_reports'
manifest=json.loads((out/'145_scan026_crop_manifest.json').read_text())
crops={x['name']:x for x in manifest}
def ev(name):
    x=crops[name]
    return {'crop':x['crop'],'box':x['box']}
changes=[]
ids={}
def change(key,place,C,H,final,ink,confidence,kind,c_changed,h_changed,crop,categories,marked='no',consequence=''):
    ident=f's026-{len(changes)+1:02d}'
    ids[key]=ident
    changes.append(dict(id=ident,place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c_changed,h_changed=h_changed,marked_in_H=marked,**ev(crop),error_category=categories,math_consequence=consequence))

change('de','parameter line, cancelled word before p=1',r'\deleted{\text{de}}',r'\struck{dans}',r'\deleted{\text{\unsure{de|dans}}}',
       'The first letter has a closed lower loop and rising d stem. The next low trace favors e; the long strike masks the remainder and has a downturned portion that cannot securely be separated into extra letters. Keep de first, with dans as the local alternative.',
       'medium','misread word',False,True,'parameter_trials',[2,7])
change('gdot','parameter line, tuple subscript',r'(g_i)',r'(g_\cdot)',r'(g_\cdot)',
       'A single detached dark point stands at the lower-right of g. No independent i stem is visible below it; the next descending curve belongs to the closing parenthesis.',
       'high','misread symbol or index',True,False,'parameter_trials',[1])
change('trial1','parameter line, first cancelled parenthesized trial',r'\deleted{\unsure{(l_i^{\alpha_i})}}',r'\struck{\ill{}}',r'\deleted{\unsure{(l_i^{\alpha_i})}}',
       'Both enclosing curves and a lower l-like return survive the dense diagonal hatching. Higher looped material can support alpha with index i, but the individual internal strokes are not all recoverable. Preserve the entire C candidate as doubtful, not as a certified formula.',
       'low',r'readable ink left as \ill{}',False,True,'parameter_trials',[1,5,7])
change('trial2','parameter line, second cancelled parenthesized trial',r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}',r'\struck{\ill{}}',r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}',
       'The wider cancelled group retains opening and closing curves, a tall looped l-like stroke, a low g-like descender, and high overwritten material near the right end. Hatching prevents certain recovery of the internal indices and inverse exponent. Retain C as a whole-formula uncertainty.',
       'low',r'readable ink left as \ill{}',False,True,'parameter_trials',[1,5,7])
change('duplicate_order','parameter display, H duplicated surviving product and split order',r'p=1,\quad(g_i)=\deleted{\unsure{(l_i^{\alpha_i})}}\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}(gl_i^{\alpha_i})',r'\struck{\ill{}}\ \struck{\ill{}}\ (g\, l_i^{\alpha_i})\quad\struck{dans}\ p = 1,\ (g_\cdot) = \struck{\ill{}}\,(g\, l_i^{\alpha_i})',r'p=1,\quad(g_\cdot)=\deleted{\unsure{(l_i^{\alpha_i})}}\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}(gl_i^{\alpha_i})',
       'One continuous manuscript baseline runs from the cancelled short word through p=1, the tuple and equals sign, two cancelled parenthesized trials, and one live product. There is no separate earlier live copy of the product and no separate second formula row.',
       'high','text not on the page',False,True,'parameter_trials',[6,9])
change('parameter_stop','end of the live parameter product','','.','',
       'The closing parenthesis ends the written formula. The space immediately to its right has no independent full stop.',
       'high','text not on the page',False,True,'parameter_trials',[9])
change('sur_deleted','main prose, word before the first membership parenthesis',r'\deleted{sur}','',r'\deleted{sur}',
       'A small s-like opening, low u and short r lie under a horizontal cancellation immediately before the opening parenthesis. The strike is separate from that curved parenthesis.',
       'high','omission',False,True,'operations_groups',[2,3,7])
wave_group=r'S\overset{\unsure{\sim|\deleted{\sim}}}{\widehat{\widehat{\mathcal E}}}^{!}'
change('wave1','main prose, first S-double-hatted-E group',r'S\widehat{\widehat{\mathcal E}}^!',r'S\hat{\hat{\mathcal{E}}}^{!}',wave_group,
       'Above the two distinct carets over E is an additional dark low wavy trace, separated from the E body and from both carets. Its shape is retained as a locally uncertain wavy adornment; neither witness records it. The exclamation stroke and its point stand separately to the right.',
       'high','omission',True,True,'operations_groups',[1,3],consequence='The added visible adornment is not assigned a group-theoretic meaning.')
change('sur_live','main prose, immediately after the membership parenthesis','sur',', ou','sur',
       'After the closing curve, a small descending s-like return is followed by joined u/r strokes. The initial return is part of sur, not a separate comma followed by ou.',
       'high','misread word',False,True,'operations_groups',[2,9])
change('old_u','main prose, overwritten symbol preceding live tilde-u',r'\deleted{\unsure{u}}',r'\tilde\varepsilon',r'\deleted{\unsure{u|\varepsilon}}',
       'A dark retraced small body precedes the separate live u. Its upper loop and lower return admit u or epsilon; overtracing prevents a secure letter choice. The overwritten state is preserved instead of making this a live tilde-epsilon.',
       'low','deletion state',False,True,'operations_groups',[1,7])
change('tilde_u','main prose, live symbol after the overwritten body',r'\tilde u',r'\ill{}',r'\tilde u',
       'A distinct low u with two joins follows the dark old body. A separate shallow wave lies directly over it; the following membership sign is separately visible.',
       'high',r'readable ink left as \ill{}',False,True,'operations_groups',[1,5])
change('wave2','main prose, second S-double-hatted-E group',r'S\widehat{\widehat{\mathcal E}}^!',r'S\hat{\hat{\mathcal{E}}}^{!}',wave_group,
       'The second group likewise has two carets and a third, darker low wavy trace above them. The trace is not the upper curl of the lower E or S. Its exact adornment/state remains uncertain, but its presence cannot be omitted.',
       'high','omission',True,True,'operations_groups',[1,3],consequence='The added visible adornment is not assigned a group-theoretic meaning.')
change('conjugaison','main prose, phrase after the second group',r'par \deleted{\unsure{leurs}} conjugaison','sur ces groupes',r'par \deleted{\unsure{leurs}} conjugaison',
       'A live p/a/r group precedes a crossed short word with an initial tall l and compressed following strokes; the latter remains leurs-first uncertain. The longer following word has c/o/n and the descending j/g forms of conjugaison, continuing to its s/o/n ending. The oblique marginal words cross this region and are read on their own direction.',
       'medium','misread word',False,True,'conjugaison_trouve',[2,7])
change('rho_trouve','main prose, after et en particulier',r'de $\rho$. On trouve',r'\ill{}',r'de $\rho$. On trouve',
       'A short d/e precedes a loop-headed descending rho and a detached low stop. Then a large open O with following n is followed by the tall crossed t and joined r/o/u/v/e of trouve.',
       'high',r'readable ink left as \ill{}',False,True,'conjugaison_trouve',[1,2,3,5])
change('p_bien','main prose, cancelled material after que',r'\deleted{\unsure{$p$ (bien sûr)}}',r'\struck{\ill{}}',r'\deleted{$\unsure{p}$ (bien sûr)}',
       'The long cancellation traverses a descending initial letter whose head is obscured; p is retained only as doubtful. Both parenthesis curves, the tall b, dotted i, joined e/n, and s/u/r with a separate circumflex are readable. The C uncertainty is narrowed to the initial letter.',
       'medium',r'readable ink left as \ill{}',False,True,'conjugaison_trouve',[1,2,5,7])
change('quotes','main prose, quotation marks around covariants',r"``covariants''",'« covariants »',r"``covariants''",
       'The opening consists of two small high ticks; the closing high pair is compressed. There are no angular guillemets. The word itself reads covariants in both witnesses and in the ink.',
       'high','other',False,True,'covariants',[10])
change('bar_u','covariance formula, final argument',r'\unsure{\bar u|\tilde u}',r'\tilde u',r'\bar u',
       'The upper mark is a short, almost level, thick horizontal stroke. It has no alternating dip/rise, unlike the clearly wavy mark above the earlier u in the same formula. Read the local mark as a bar.',
       'high','misread symbol or index',False,True,'covariance_formula',[1],consequence='The two u adornments are preserved as distinct; no rho action is supplied on the right.')
change('struck_ie','last cancelled line, first surviving cluster','',r'i.e.',r'\unsure{i.e.}',
       'A first small cluster stands well to the left of the later si-like cluster. It retains a sloping upright and a detached high mark, while the cancellation masks its baseline. H suggests i.e.; retain that only as a doubtful reading of actual additional ink omitted by C.',
       'low','omission',True,False,'struck_si',[2,3,7])
change('struck_si','last cancelled line, second surviving cluster before tilde-u','si',r'\ill{}',r'\unsure{si}',
       'The second separate cluster retains a short rising stroke, a partly covered low curve, and a detached high point. The s is obscured by the strike, so si is not certified. The following tilde-u, est, défini and par remain readable.',
       'low',r'readable ink left as \ill{}',False,True,'struck_si',[2,5,7])
change('nb_underline','beginning of oblique margin note',r'\uline{NB}',r'\textbf{NB}',r'\uline{NB}',
       'One independent dark line lies beneath the two letters NB. H uses bold letters without preserving that separate underline.',
       'high','omission',False,True,'nb_oblique',[3,10])
change('un','oblique margin, after d\'introduire','un','aussi le','un',
       'The short joining u/n arches occur directly after introduire. No extra sequence for aussi and no separate le are written before the next line groupe.',
       'high','misread word',False,True,'nb_oblique',[2,9])
change('margin_comma','oblique margin, after the first S-hatted-E','',' ,','',
       'The first hatted group sign is followed directly by the space before extension. No distinct low comma lies between them; the marks on the next oblique baseline belong to the lattice expression.',
       'high','text not on the page',False,True,'nb_oblique',[9])
change('deduite','oblique margin, beginning of parenthesis',r"déduite d'une",r"\uncertain{celle-ci} étant d'ailleurs une",r"déduite d'une",
       'After the opening parenthesis, the initial looped d, high accent, second tall d and compressed u/i/t/e ending support déduite. A separate d-apostrophe then precedes une. There is no celle-ci or intervening étant d\'ailleurs sequence.',
       'high','misread word',False,True,'nb_oblique',[2,9],marked='yes')
change('canonique','oblique margin, before de Gamma','canonique','','canonique',
       'The low c/a/n/o/n/i run is followed by a long q descender and final u/e. The word occupies the start of its oblique baseline before de Gamma.',
       'high','omission',False,True,'nb_oblique',[2,3])
change('bare_Z','oblique margin, second lattice expression',r'\mathbb Z^{\{0,1,\infty\}}',r'\hat{\mathbb{Z}}^{\{0,1,\infty\}}',r'\mathbb Z^{\{0,1,\infty\}}',
       'The second Z has its letter strokes and raised index set, but no separate caret above the letter. The earlier Z in the same note does have its own detached hat; the two occurrences are kept distinct.',
       'high','misread symbol or index',False,True,'nb_oblique',[1,9])
change('phantom_margin','oblique margin, between Gamma par and the second Z','',r'\struck{\ill{}} \ill{} \ill{}','',
       'The marginal sequence continues from Gamma and par to the next-line Z expression. Crossing strokes in this area run with the main horizontal prose/cancellation after rotation; they do not supply a separate cancelled-and-illegible marginal passage.',
       'medium','text not on the page',False,True,'nb_oblique',[6,7,9])
change('old_des','oblique margin, cancelled short word before the live des relèvements',r'\deleted{\unsure{des}}',r'\ill{}',r'\deleted{\unsure{des}}',
       'A compact dark strike obscures most of a small word at the turn into the last lines. A tall beginning and low traces allow des but do not expose every letter. Its cancelled state is definite and is preserved.',
       'low','deletion state',False,True,'nb_oblique',[2,5,7])
change('live_des','oblique margin, immediately before relèvements','des','les','des',
       'The live short word begins with a looped d rather than a plain l, followed by low e/s. The subsequent relèvements is not cancelled.',
       'high','misread word',False,True,'nb_oblique',[2])
change('margin_end','oblique margin, after sigma_i and rho','par des éléments de','dans','par des éléments de',
       'The oblique continuation contains multiple separated word groups, including a short par, looped d/e/s, the tall l and joined m/e/n/t/s of éléments, then de before the last S-hatted-E. It is substantially longer than a single dans. Interfering main-line traces are not assigned additional marginal letters or punctuation.',
       'medium','misread word',False,True,'nb_oblique',[2,3])
change('four_points','end of oblique margin note',r'\ldots','',r'\ldots\ .',
       'Four separate dark marks continue the oblique line beneath its ending: a slightly longer first point followed by three shorter points. H has no terminal sequence; C gives only a conventional three-point ellipsis.',
       'high','omission',True,True,'nb_oblique',[3,10])
change('footer','lower-left handwritten page number',r'\mspage{25}','',r'\mspage{25}',
       'The first digit has a rounded head, descending diagonal and foot, 2. The second has a short top bar, upper turn and broad lower curve, 5. The source footer is 25 and is absent from H.',
       'high','omission',False,True,'footer25',[3])

decisions=[dict(id='M0867',decision='first',reading=r'\bar u',ink='A short almost level horizontal upper stroke is distinct from the wavy tilde over the earlier u in this same formula. The final u is therefore barred.',confidence='high',**ev('covariance_formula'))]
unlisted=[]
for ident,place,mark,reading,decision,ink,crop,confidence in [
    ('U026-01','parameter line, first cancelled trial',r'\unsure{(l_i^{\alpha_i})}',r'\deleted{\unsure{(l_i^{\alpha_i})}}','undecided','The enclosing curves and a lower l-like return survive, but hatching masks the internal symbols and indices.','parameter_trials','low'),
    ('U026-02','parameter line, second cancelled trial',r'\unsure{(l_i^{\alpha_i}g^{-1})}',r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}','undecided','A l-like tall loop and g-like descender are visible, but the internal exponent and index material are not independently plain.','parameter_trials','low'),
    ('U026-03','main prose, overwritten body before tilde-u',r'\unsure{u}',r'\deleted{\unsure{u|\varepsilon}}','undecided','Overtraced upper loop and lower return admit u or epsilon; the overwritten state is clear.','operations_groups','low'),
    ('U026-04','main prose, cancelled word after par',r'\unsure{leurs}',r'\deleted{\unsure{leurs}}','undecided','A tall initial l survives, but the strike merges the low e/u/r/s-like strokes.','conjugaison_trouve','low'),
    ('U026-05','main prose, cancelled letter and parenthetical phrase',r'\unsure{$p$ (bien sûr)}',r'\deleted{$\unsure{p}$ (bien sûr)}','other','The leading descending letter remains p-first doubtful. Both enclosing curves and every letter of bien sûr, including i point and circumflex, are readable, so uncertainty is narrowed to the letter.','conjugaison_trouve','medium'),
    ('U026-06','oblique margin, cancelled short word before des relèvements',r'\unsure{des}',r'\deleted{\unsure{des}}','undecided','The dark cancellation leaves insufficient internal strokes to resolve des.','nb_oblique','low'),
]:
    unlisted.append(dict(id=ident,place=place,C_mark=mark,decision=decision,reading=reading,ink=ink,confidence=confidence,**ev(crop)))

doubts=[
    dict(place='parameter line, initial cancelled word',reading=r'\deleted{\text{\unsure{de|dans}}}',alternatives=['de','dans'],confidence='medium',reason='d/e-like opening survives; the strike masks any following letters.'),
    dict(place='parameter line, first cancelled trial',reading=r'\deleted{\unsure{(l_i^{\alpha_i})}}',alternatives=[r'(l_i^{\alpha_i})','unresolved internal formula'],confidence='low',reason='Dense hatching obscures the indices and high material.'),
    dict(place='parameter line, second cancelled trial',reading=r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}',alternatives=[r'(l_i^{\alpha_i}g^{-1})','unresolved internal formula'],confidence='low',reason='Overlapping cancellation obscures the superscript and intervening strokes.'),
    dict(place='main prose, first upper group adornment',reading=wave_group,alternatives=['live extra wavy adornment over the double hat','overwritten or cancelled upper adornment'],confidence='medium',reason='The dark extra wave is visible, but its precise function and retracing state are not secure.'),
    dict(place='main prose, overwritten symbol before live tilde-u',reading=r'\deleted{\unsure{u|\varepsilon}}',alternatives=['u',r'\varepsilon'],confidence='low',reason='The small body is heavily retraced and has both upper-loop and lower-return material.'),
    dict(place='main prose, second upper group adornment',reading=wave_group,alternatives=['live extra wavy adornment over the double hat','overwritten or cancelled upper adornment'],confidence='medium',reason='The independent third upper trace is plain, but its precise state is not.'),
    dict(place='main prose, cancelled word after par',reading=r'\deleted{\unsure{leurs}}',alternatives=['leurs','unresolved short l-initial word'],confidence='low',reason='The horizontal line merges the low middle and ending strokes.'),
    dict(place='main prose, cancelled letter before (bien sûr)',reading=r'\deleted{$\unsure{p}$ (bien sûr)}',alternatives=['p','unresolved descending letter'],confidence='low',reason='The cancellation obscures the head of the long descending initial letter.'),
    dict(place='last cancelled line, first cluster',reading=r'\unsure{i.e.}',alternatives=['i.e.','unresolved short initial cluster'],confidence='low',reason='Only a sloping upright and detached high mark are independently recoverable; H supplies the plausible i.e. candidate.'),
    dict(place='last cancelled line, second cluster',reading=r'\unsure{si}',alternatives=['si','unresolved second short word'],confidence='low',reason='The high point and short rise are visible, while the s is covered by the cancellation.'),
    dict(place='oblique margin, cancelled des',reading=r'\deleted{\unsure{des}}',alternatives=['des','unresolved short cancelled word'],confidence='low',reason='The compact dark strike does not leave every letter plain.'),
    dict(place='overlap at final marginal S-hatted-E and main conjugaison',reading=r'conjugaison; $S\hat{\mathcal E}$',alternatives=['thin curved trace belongs to the main conjugaison ink','a separate marginal closing curve, not sufficiently supported'],confidence='medium',reason='The thin curve aligns with the main text crossing the oblique note. There is no matching marginal opening that would justify adding a closing parenthesis. The main word is preserved and no extra marginal punctuation is supplied.'),
]

inventory=[]
def inv(kind,position,first,box):
    inventory.append(dict(element=f'I{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=first,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('text','top, continuing opening baseline',r'en associant à $(g,(\alpha_i)_{i\in\{0,1,\infty\}})$ le système',[286,74,1612,171])
inv('display','second baseline, one parameter formula',r'p=1, (g_\cdot)= ... (gl_i^{\alpha_i})',[290,171,1330,306])
inv('deletion','parameter line, before p=1',r'\deleted{\text{\unsure{de|dans}}}',[296,205,396,266])
inv('deletion','parameter line, first parenthesized trial',r'\deleted{\unsure{(l_i^{\alpha_i})}}',[750,178,884,274])
inv('deletion','parameter line, second parenthesized trial',r'\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}',[887,172,1106,286])
inv('text','main block, five base lines',r'Il faudrait expliciter ... les gamma_i sont covariants ... i.e.',[288,290,1634,812])
inv('deletion','main prose, before first membership parenthesis',r'\deleted{sur}',[984,409,1062,452])
inv('drawing','above first double-hatted E','extra dark wavy upper trace',[1108,367,1158,403])
inv('deletion','main prose, old body preceding tilde-u',r'\deleted{\unsure{u|\varepsilon}}',[1315,392,1364,457])
inv('drawing','above second double-hatted E','extra dark wavy upper trace',[1454,353,1507,391])
inv('deletion','main prose, after par',r'\deleted{\unsure{leurs}}',[465,542,591,594])
inv('deletion','main prose, after On trouve que',r'\deleted{$\unsure{p}$ (bien sûr)}',[1304,593,1625,691])
inv('display','main covariance formula',r'\gamma_i(\rho\tilde u\rho^{-1})=\gamma_{i+1}(\bar u)',[370,842,1255,970])
inv('deletion','last horizontal line',r'\deleted{\unsure{i.e.} \unsure{si} $\tilde u$ est défini par}',[278,950,1084,1070])
inv('margin note','left, long oblique note overlapping main text',r'\uline{NB} Il y a lieu ... par des éléments de S-hatted-E',[32,288,718,1180])
inv('drawing','beginning of oblique margin note','single underline under NB',[55,405,111,467])
inv('display','oblique margin, first lattice term',r'\hat{\mathbb Z}^{\{0,1,\infty\}}',[183,472,316,582])
inv('display','oblique margin, second lattice term',r'\mathbb Z^{\{0,1,\infty\}}',[44,777,216,923])
inv('deletion','oblique margin, short cancelled word before live des',r'\deleted{\unsure{des}}',[290,766,350,818])
inv('drawing','end of oblique note','four continuation points',[68,1113,139,1170])
inv('text','lower-left footer','25',[31,2271,115,2350])

parameter=r'''\[
\deleted{\text{\unsure{de|dans}}}\quad p=1,\quad(g_\cdot)=\deleted{\unsure{(l_i^{\alpha_i})}}\deleted{\unsure{(l_i^{\alpha_i}g^{-1})}}(gl_i^{\alpha_i})
\]'''
ops=r'Il faudrait expliciter les opérations des éléments $\sigma_i$ ou $\varepsilon_i$ \deleted{sur} $(\in '+wave_group+r')$ sur $\deleted{\unsure{u|\varepsilon}}\tilde u\in '+wave_group+r'$,'
margin=r"\margin{\uline{NB} Il y a lieu d'introduire un groupe $S\hat{\mathcal E}$ extension de $\mathcal E$ par $\hat{\mathbb Z}^{\{0,1,\infty\}}$ (déduite d'une extension canonique de $\Gamma$ par $\mathbb Z^{\{0,1,\infty\}}$) et d'introduire \deleted{\unsure{des}} des relèvements des $\sigma_i,\rho$ par des éléments de $S\hat{\mathcal E}$\ldots\ .}"
second=[]
def sb(kind,coords,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,coords=coords,reading=reading))
sb('complete opening baseline with all handwritten index-set numbers',[286,74,1612,171],r'en associant à $(g,(\alpha_i)_{i\in\{0,1,\infty\}})$ le système')
sb('entire parameter line: cancelled word, p=1, point subscript, both cancelled trials, live product and all exponents',[290,171,1330,306],parameter)
sb('first two main prose baselines: cancelled sur and old u, both group adornments, exclamations and all H disagreements',[288,290,1631,496],ops)
sb('two main horizontal prose baselines crossing the oblique note: live par/conjugaison, cancelled leurs, rho and On trouve, cancelled parenthesis',[386,493,1634,725],r'par \deleted{\unsure{leurs}} conjugaison, et en particulier de $\rho$. On trouve que \deleted{$\unsure{p}$ (bien sûr)}')
sb('complete covariants prose baseline, literal quotes, gamma_i, rho, and i.e. punctuation',[395,712,1450,812],r"les $\gamma_i$ sont ``covariants'' par $\rho$, i.e.")
sb('complete covariance formula and cancelled next line; all numerical exponents/indices, bar/tilde, both surviving initial clusters',[278,842,1255,1070],r'\[\gamma_i(\rho\tilde u\rho^{-1})=\gamma_{i+1}(\bar u)\] \deleted{\unsure{i.e.} \unsure{si} $\tilde u$ est défini par}')
sb('complete oblique margin layer: underline, every lexical discrepancy, both numerical lattice index sets, old des, single hats and four continuation points',[32,288,718,1180],margin)
sb('handwritten footer 25 omitted from H',[31,2271,115,2350],r'\mspage{25}')

diffs=[]
def diff(row,keys=None,explanation=None):
    if keys:
        entry={'row':row,'status':'substantive'}
        selected=[ids[k] for k in keys]
        if len(selected)==1:entry['change_id']=selected[0]
        else:entry['change_ids']=selected
        if explanation:entry['explanation']=explanation
    else:entry={'row':row,'status':'macro/editorial','explanation':explanation}
    diffs.append(entry)
diff(1,explanation='C scan identifier 26 is editorial; there is no handwritten header 26.')
diff(2,['de','duplicate_order'],explanation='The initial cancelled word and p=1 are on the same single source formula baseline; H splits and reorders the material.')
diff(3,['gdot','duplicate_order'])
diff(4,['de','duplicate_order'])
diff(5,['duplicate_order'],explanation='Token alignment created by H\'s earlier duplicate live product; the manuscript has one tuple and one surviving product in a single row.')
diff(6,['parameter_stop','duplicate_order'],explanation='H\'s final full stop is not on the page; the following quoted p=1 wording belongs to H\'s editorial note.')
diff(7,['trial2'],explanation='The old inverse exponent is part of the second cancelled C candidate and remains uncertain; H leaves the trial illegible.')
diff(8,explanation='H editorial explanation of the biffed groups and opening p=1, not further source writing. The actual trials and order are separately collated.')
diff(9,explanation='H g\\,l uses the thin-space macro \\,; its comma token is not literal manuscript punctuation. Both witnesses identify the surviving product g l_i to alpha_i.')
diff(10,explanation='End-display syntax versus the end of H\'s editorial explanation est ce qui reste; not manuscript text.')
diff(11,['sur_deleted'])
diff(12,['sur_live','old_u','tilde_u'])
diff(13,['conjugaison'])
diff(14,['rho_trouve'])
diff(15,['p_bien'])
diff(16,['quotes'])
diff(17,['bar_u'])
diff(18,['struck_ie','struck_si'],explanation='The ink has two separated short clusters before tilde-u. H\'s i.e. candidate and C\'s si candidate are both retained as doubtful, without certifying letters hidden by the strike.')
diff(19,['un'])
diff(20,['margin_comma'])
diff(21,['deduite'])
diff(22,['canonique'])
diff(23,['old_des','live_des'])
diff(24,['margin_end'])
diff(25,['footer'],explanation='Source lower-left 25 is omitted from H. The margin continuation points, which disappear during tokenization, are separately logged.')

report=dict(scan=26,reader='/root/reader_a',lines_read=20,
    layout='Upright sheet, with all continuous writing in the upper half. One continuing opening line and one parameter formula are followed by five main prose baselines, a covariance formula and a long cancelled line. A dense NB note slopes upward to the right along the left margin and overlaps several main lines; its independent text direction is retained. It has a four-point continuation. The rest of the sheet is blank apart from the lower-left footer 25. The 20 read units comprise nine main text/formula rows, ten oblique marginal text/continuation units, and the footer; crowded short marginal words share local baselines.',
    changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
    notation=[
        {'form':r'(g_\cdot)','places':['parameter display'],'observation':'The tuple subscript is a single dot with no i stem.','qualification':'This does not change the explicit i indices in the opening alpha family or the products.'},
        {'form':wave_group,'places':['both group occurrences in the main operations sentence'],'observation':'Two distinct carets over E have a third dark wavy trace above them. Both exclamation marks are separately written.','qualification':'The extra upper trace is retained with local uncertainty; no meaning or uniform notation on other pages is imposed.'},
        {'form':r'S\hat{\mathcal E}','places':['first and final group names in oblique NB'],'observation':'These have a single separate hat, unlike the crowded double-hat-plus-wave forms in the main prose.','qualification':'No additional wave is transferred to the margin names.'},
        {'form':r'\tilde u,\bar u','places':['left and right arguments in the covariance formula'],'observation':'The left upper mark is distinctly wavy; the right is a short almost level bar.','qualification':'The distinction is read from the same formula crop.'},
        {'form':r'i+1','places':['right gamma index in covariance formula'],'observation':'A short upright visibly intersects the horizontal stroke between i and 1, so the sign is plus.','qualification':'No algebraic expectation supplies the sign, and no rho action is added to the RHS.'},
        {'form':r'\hat{\mathbb Z}^{\{0,1,\infty\}},\mathbb Z^{\{0,1,\infty\}}','places':['first and second lattice terms in the NB'],'observation':'Only the first Z has a detached hat. Both raised sets contain 0, 1 and infinity.','qualification':'The second hat is not supplied from the first occurrence or from a completion interpretation.'},
    ],
    hand=[
        {'habit':'Oblique marginal writing can run through the horizontal main prose.','places':['main conjugaison and cancelled leurs','marginal Gamma/par and final S-hatted-E'],'universal_on_page':False,'witness_effect':'H misassigns some crossed strokes as additional cancelled/illegible marginal text. A thin curve near final marginal S-hatted-E is not promoted to a new closing parenthesis.'},
        {'habit':'Dark overtracing may obscure whether an upper adornment is live or abandoned.','places':['both dark waves above the double-hatted E groups','old body before tilde-u'],'universal_on_page':False,'witness_effect':'Both witnesses omit the additional waves; H makes the overwritten body a live tilde-epsilon.'},
        {'habit':'A single point is distinguishable from a dotted i when no stem survives.','places':['tuple subscript in parameter line versus sigma/gamma indices'],'universal_on_page':False,'witness_effect':'C reads the tuple point as i; H preserves the point.'},
        {'habit':'Long cancellation lines can leave separated word clusters without recoverable complete letters.','places':['last struck line','cancelled de/dans','old des'],'universal_on_page':False,'witness_effect':'C omits the first cluster of the last line; both witness candidates are retained only with local uncertainty.'},
        {'habit':'The continuation here has four separately written points.','places':['end of oblique NB'],'universal_on_page':False,'witness_effect':'C regularizes the sequence to a three-point ellipsis and H omits it.'},
    ],
    abbreviations=[
        {'form':'NB','expansion':'nota bene','place':'underlined start of oblique margin note'},
        {'form':'i.e.','expansion':'id est','place':'live prose immediately before covariance formula'},
        {'form':r'\unsure{i.e.}','expansion':'possibly id est; expansion not inserted in the text','place':'first cluster of the cancelled last line'},
    ],
    notes=[
        'The opening continues a construction by associating a system to g and an indexed alpha family. The source parameter line has p=1, a tuple whose subscript is one dot, two cancelled trials, and one live product g l_i to alpha_i. The old trials are kept as doubtful C candidates. H\'s extra live copy and separate formula row are not supported by the page.',
        'The author asks to make explicit the conjugation operations of sigma_i or epsilon_i and particularly rho, then states that the gamma_i are covariant under rho. The displayed right index is i+1, the left u is tilded and the right u is barred. No additional rho action or factor occurs outside the written RHS. These are ink readings, not a verification of the asserted covariance.',
        'The two main S-double-hatted-E signs each carry an extra dark wavy upper trace. The transcription retains each visible trace with a local doubt concerning its exact adornment/state. The two marginal S-hatted-E signs remain single-hatted.',
        'The entire last horizontal line is crossed out. Before tilde-u there are two separate surviving clusters. The first is retained as doubtful i.e., suggested by H; the second as doubtful si, suggested by C. Neither is presented as fully recovered under the strike. In the earlier cancelled parenthesis, bien sûr is readable while its leading descending letter remains p-first doubtful.',
        'The NB introduces a group S-hatted-E as an extension by the first, hatted lattice, describes a canonical extension involving Gamma and a second, unhatted lattice, and calls for lifts of sigma_i and rho. The exact words un, déduite d\'une extension canonique, des relèvements and par des éléments de are preserved. The small old des remains doubtful and cancelled. Four continuation points follow the note.',
        'The note crosses main-line lettering in several places. A thin apparent closing curve after the final marginal S-hatted-E aligns with the main conjugaison ink; there is no secure matched marginal opening, so no extra margin parenthesis is supplied. The main cancellation line under par touches its low stroke but passes through the following old leurs; par is kept live and the short old word remains cancelled.',
        'The sheet has no source header 26. Its only separate page number is handwritten 25 at lower left, which H omits and which is counted as a source omission. The large lower blank and isolated nontextual paper specks have not been filled with inferred content.',
        'Every agreed word, formula sign, index, punctuation mark and source correction was checked against the ink. The whole sheet and each supplied native half were viewed once; eight single saved enlarged crops were made and read, with no replacement crops. Every C deletion is separately inventoried. No source insertion was identified on this sheet.',
        'No OCR, external research, other-page reading, blind second reading, or TeX compilation was performed. No mathematical assertion was independently checked or used to force a reading; the root reader records any conditional algebra separately.',
    ],check_events=[],diff_coverage=diffs)
(out/'145_scan026.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'formal_marks':len(decisions),'unlisted_C_marks':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(diffs),'crops':len(manifest)}))
