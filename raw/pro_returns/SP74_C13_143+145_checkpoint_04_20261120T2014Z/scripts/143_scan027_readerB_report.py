from pathlib import Path
import json

root = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
pkt = json.loads(Path('/workspace/scratch/8f839dff4bf0/reader_packets/143_scan027.json').read_text())
Csrc, Hsrc = pkt['witness_C'], pkt['witness_H']
key = '143_scan027'

candidate = r'''\scanpage{27}
que l'opération de $\pi$ sur $\unsure{\tau|\mathcal T}$ a été prolongée en une opération de $\unsure{\mathcal E|\Sigma}$ sur $\unsure{\tau|\mathcal T}$. Mais ceci ne donne pas d'interprétation symp. de la $T$- Arrêtons\ldots.
\figure{\begin{tikzpicture}\draw (0,0)--(1.5,0);\end{tikzpicture}}

\textcircled{9} Les schémas et Topos fondamentaux dans la théorie.

\textcircled{A} \deleted{Topos \unsure{Étendus|Étendue}} \inserted{Topos} modulaires \inserted{$(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}$} pour les courbes de genre $0$ avec $\nu$ points marqués, et famille \deleted{des} modulaire \deleted{\unsure{par}} $\nu$-ponctuée sur $\mathcal T_{0\nu}$\ldots.

Le Topos $(\mathcal T_{0,\nu})_{\mathbf Q}$ pour $\nu=0,1,2$ \uline{n'est} pas un étendu --- car les schémas d'Isom \unsure{d'un|d'une} $X/S$ fibré projectif de rang $1$, avec $\unsure{2|\nu}$ sections marquées (distinctes sur chaque fibre) est lisse de dim rel. $3-\nu\deleted{\unsure{\geq|=|\leq}}>0$ (si $\deleted{\unsure{\nu}}0\leq\nu\leq2$).
\deleted{\unsure{Néanmoins}} \inserted{En fait} ce sont les topos
\[
B_{\operatorname{GP}(1)},\quad B_{\operatorname{Aff}(1)},\quad B_{G_m},\quad\inserted{B_e=e}
\]
dont les
\mspage{26}
'''

boxes = {
    'opening_symbols':[983,45,1600,274],
    'second_set':[312,282,934,392],
    'opening_close':[320,393,1612,613],
    'heading_revisions':[430,844,1528,1101],
    'punctured_family':[349,1280,1405,1446],
    'les_schemas':[1000,1541,1510,1655],
    'isom_and_article':[350,1660,1170,1787],
    'rank_and_sections':[349,1780,1505,1909],
    'dimension_condition':[837,1985,1564,2111],
    'en_fait_revision':[363,2104,1345,2240],
    'first_classifying_group':[388,2210,911,2316],
    'last_classifying_insertion':[943,2140,1513,2319],
}

def loc(name):
    return ('page',None) if name is None else (f'crops/{key}_readerB_{name}.png',boxes[name])

def row(place,C,H,final,ac,ah,kind,ink,confidence='high',crop=None,marked=False,consequential=False):
    assert C == '[no witness]' or C in Csrc, ('Nonliteral C',place,C)
    assert H == '[no witness]' or H in Hsrc, ('Nonliteral H',place,H)
    assert not final or final in candidate, ('Nonliteral final',place,final)
    path,box = loc(crop)
    return {'place':place,'C':C,'H':H,'final':final,'against_C':ac,'against_H':ah,'kind':kind,'ink':ink,'confidence':confidence,'crop':path,'box':box,'marked_in_H':marked,'consequential':consequential}

changes = [
    row('Opening, first object-set glyph',r'\tau',r'\mathcal{T}',r'\unsure{\tau|\mathcal T}',False,True,'misread symbol or index',
        'The cap descends at the left and runs into a small upper-right loop, then a single broad lower return. Preferred tau is retained with T as an explicit alternative; this is an alphabet encoding only.',
        'medium','opening_symbols'),
    row('Opening, a été prolongée','a été prolongée','soit prolongée','a été prolongée',False,True,'misread word',
        'A detached compact a precedes the accented e, tall t, and final accented e of été. The verb prolongée continues on the following manuscript line. There is no initial s or oi group supporting soit.',
        'high','opening_symbols'),
    row('Opening, action-group glyph',r'\mathcal E',r'\Sigma',r'\unsure{\mathcal E|\Sigma}',False,True,'misread symbol or index',
        'The glyph has a rounded returning upper bowl and a lower open bowl. Shared preferred E is retained with Sigma unresolved; low-confidence alphabet encoding only, not a consequential mathematical correction.',
        'low','opening_symbols'),
    row('Opening, second object-set glyph',r'\tau',r'\mathcal{T}',r'\unsure{\tau|\mathcal T}',False,True,'misread symbol or index',
        'The head is heavily retraced around the same upper loop, while one clean lower curve remains. No independent struck-out symbol can be separated from the retouching. Preferred tau/T uncertainty is retained at this occurrence.',
        'medium','second_set'),
    row('Opening, symp. abbreviation','symp. de la',r'\ill{} de la','symp. de la',False,True,'readable ink left as \\ill{}',
        'The word has a short initial s, the long descending y, a low m, a descending p and a separate terminal point. The abbreviated form is readable and is not expanded.',
        'high','opening_close',True),
    row('Opening, unfinished T- expression',r'$T$---',r'$T$-\ill{}.',r'$T$-',True,True,'text not on the page',
        'A single short horizontal hyphen follows the plain capped T. The remaining right margin is blank. No following word, illegible passage, terminal point, or long em dash is written before the next line Arrêtons.',
        'high','opening_close',True),
    row('Opening suspension after Arrêtons',r'\unsure{Arrêtons}\ldots',r'Arrêtons \ldots',r'Arrêtons\ldots.',True,True,'omission',
        'Four separate dark continuation points follow Arrêtons, not three. The extra point is retained as ldots plus a period; the word itself is settled separately in M0710.',
        'high','opening_close'),
    row('Short separator below opening paragraph',r'\figure{\begin{tikzpicture}\draw (0,0)--(1.5,0);\end{tikzpicture}}','[no witness]',r'\figure{\begin{tikzpicture}\draw (0,0)--(1.5,0);\end{tikzpicture}}',False,True,'drawing or diagram',
        'A short isolated horizontal rule lies centrally below Arrêtons and above the circled 9. It has no arrowheads or attached text.'),
    row('Section 9 title, final punctuation','la théorie.',r'la théorie \ldots','la théorie.',False,True,'text not on the page',
        'The title ends with one dark point after théorie. There is no row of continuation points at this title ending.'),
    row('Heading A, cancelled adjective and its accent',r'\deleted{Topos \unsure{Etendus|Etendue}}',r'\struck{Topos \ill{}}',r'\deleted{Topos \unsure{Étendus|Étendue}}',True,True,'misread word',
        'The cancelled first word is Topos. The following capital E has a short accent above it; the tall t and lower tendu sequence can be followed under the strike. Its last e/s-like return remains obscured, so both endings are retained, now with the written accent.',
        'medium','heading_revisions',True),
    row('Heading A, inserted moduli-topos formula and attachment',r'\inserted{$(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}$}',r'\ldots\ $(\mathcal{T}_{0,\nu})_{\overline{\mathbb{Q}}}$',r'\inserted{$(\mathcal T_{0,\nu})_{\overline{\mathbf Q}}$}',False,True,'insertion or placement',
        'The parenthesized indexed T and barred-Q base are written above pour les. A long curved attachment descends to the place between modulaires and pour. No leading ellipsis is present at that insertion site.',
        'high','heading_revisions'),
    row('Inserted moduli formula, rational-field alphabet convention',r'\overline{\mathbf Q}',r'\overline{\mathbb{Q}}',r'\overline{\mathbf Q}',False,True,'other',
        'The base letter is a Q with a diagonal return and a separate bar above. C’s bold-Q convention is retained rather than H’s blackboard rendering; this is a medium-confidence encoding-only row, not a different source variable.',
        'medium','heading_revisions'),
    row('Modular-family sentence, struck des',r'\deleted{des}','famille des modulaires',r'\deleted{des}',False,True,'deletion state',
        'The d loop and low es between famille and modulaire are crossed by a horizontal cancellation. They are not live words in the revised sentence.'),
    row('Modular-family adjective, singular modulaire','modulaire','modulaires','modulaire',False,True,'misread word',
        'The later adjective, after the struck des, ends in a low e return at the right margin. No extra terminal s follows; this differs from the plural modulaires in the heading above.'),
    row('Before nu-ponctuée, cancelled word',r'\deleted{\unsure{par}}',r'\ill{}',r'\deleted{\unsure{par}}',False,True,'deletion state',
        'A descending p-like initial and a small rounded remnant survive below the strike. The remainder is covered; par remains only a tentative reading, with the deletion state definite.',
        'low','punctured_family',True),
    row('Family qualification, nu-ponctuée',r'$\nu$-ponctuée',r'\ill{}',r'$\nu$-ponctuée',False,True,'readable ink left as \\ill{}',
        'The check-shaped nu is followed by a distinct short hyphen, then the descending p, o loop, flattened n/c, crossed t and accented ending of ponctuée. These are written text, not an unreadable gap.',
        'high','punctured_family',True,True),
    row('Family-base symbol, absent comma in index',r'\mathcal T_{0\nu}',r'\mathcal{T}_{0,\nu}',r'\mathcal T_{0\nu}',False,True,'misread symbol or index',
        'Under the modular-topos letter are a small 0 and the rising nu, with no dark descending comma between them. This occurrence is transcribed locally as 0nu, unlike the two other formulas with a visible comma.',
        'high','punctured_family'),
    row('Suspension after family-base symbol',r'$\mathcal T_{0\nu}$\ldots',r'$\mathcal{T}_{0,\nu}$ \ldots',r'$\mathcal T_{0\nu}$\ldots.',True,True,'omission',
        'Three closely spaced dark dots are followed by a fourth separated point on the same baseline. All four are retained; the index-comma difference has its own row.',
        'high','punctured_family'),
    row('Main paragraph, rational-field alphabet convention',r'(\mathcal T_{0,\nu})_{\mathbf Q}',r'(\mathcal{T}_{0,\nu})_{\mathbb{Q}}',r'(\mathcal T_{0,\nu})_{\mathbf Q}',False,True,'other',
        'The lower-right base is a Q, with no overbar at this occurrence. C’s established bold-Q convention is retained; the change from H is rendering-only, not a mathematical correction.',
        'medium'),
    row('Main paragraph, negative statement and underline',r"\uline{n'est} pas un étendu",r'\uncertain{existe} [\uncertain{comme} topos] étendues',r"\uline{n'est} pas un étendu",False,True,'misread word',
        'The end of the first line has n, an apostrophe, and the est return over a single underline. The next line has pas un étendu. There is no exists/parenthetical-comme-topos passage; the source explicitly negates being an étendu.',
        'high',None,True,True),
    row('After car, plural les schémas and no extra word',r'\unsure{les schémas|le schéma}',r'les schémas \ill{}','les schémas',False,True,'text not on the page',
        'The article has a tall l, looped e and terminal s return. Schémas ends with a separate s-shaped return. The remainder of that manuscript line is blank before d’Isom starts the next line; no additional illegible word stands there.',
        'high','les_schemas',True),
    row('Main paragraph, Isom rather than hom',"d'Isom","d'hom.\\","d'Isom",False,True,'misread word',
        'After the apostrophe is a tall straight I, then a low s, a compact o and the m return. There is no h loop or final abbreviation point. The named construction is Isom in the source.',
        'high','isom_and_article',False,True),
    row('Main paragraph, article before X/S',r"\unsure{d'un|d'une}","d'une",r"\unsure{d'un|d'une}",False,True,'misread word',
        'The d and apostrophe are distinct. The following low connected humps favor un, but the extended last return could include an e. Preferred d’un is retained with d’une explicit; this is not a confident rejection of the alternative.',
        'medium','isom_and_article'),
    row('Projective-fibration qualifier, rang','rang','genre','rang',False,True,'misread word',
        'The short word before the numeral has a low initial r/a sequence and a descending g loop. It is rang; the longer genre sequence is not present.',
        'high','rank_and_sections',False,True),
    row('Projective-fibration rank numeral',r'$1$',r'$0$',r'$1$',False,True,'misread symbol or index',
        'The numeral after rang is one tall upright with a small basal foot. It has no enclosed oval and therefore is 1, not 0.',
        'high','rank_and_sections',False,True),
    row('After rank numeral, avec',', avec','et de',', avec',False,True,'misread word',
        'After the low punctuation mark, the compact a, v movement and final ec return form avec. No et de pair is written.',
        'high','rank_and_sections'),
    row('Number of marked sections, new doubt against both witnesses',r'$\nu$ sections marquées','$\\nu$ sections\nmarquées',r'$\unsure{2|\nu}$ sections marquées',True,True,'misread symbol or index',
        'The heavily inked character has a rounded upper hook, diagonal descending return and a dense basal foot, resembling 2 more than the nearby check-shaped nu forms. Retouching obscures the stroke order, so nu remains an explicit alternative; no confident numeral correction is claimed.',
        'low','rank_and_sections',False,True),
    row('Parenthetical condition on the marked sections','(distinctes sur chaque fibre)',r'\ill{} (disjointes)','(distinctes sur chaque fibre)',False,True,'misread word',
        'Inside the parentheses are distinctes, with tall t strokes and no descending j, followed by sur chaque with its long q descender, then fibre. There is no extra word before the parenthesis in this source line.'),
    row('Predicate following the parenthesis','est lisse',r'Cela tient au fait que \ill{}','est lisse',False,True,'misread word',
        'Immediately after the closing parenthesis the short est leads into the tall l and low isse of lisse. The page has no sentence beginning Cela tient au fait que at this locus. The singular est is preserved after the earlier plural les schémas.',
        'high',None,True,True),
    row('Relative-dimension abbreviation','dim rel.',r'lieu \ill{}','dim rel.',False,True,'misread word',
        'After de, the dotted i is embedded in dim; a separate short rel. follows with a final point. These two abbreviations precede the displayed-looking inline dimension expression.',
        'high',None,True,True),
    row('Dimension expression, cancelled comparison sign',r'\deleted{\unsure{\geq|=}}','[no witness]',r'\deleted{\unsure{\geq|=|\leq}}',False,True,'deletion state',
        'Between nu and the live >0 is a separately cancelled relation. Several diagonal and short horizontal remnants remain; the angle direction and the possible lower equality bar cannot be securely separated from the cancellation. The earlier greater/equality alternatives are retained with less-or-equal added as a graphic possibility.',
        'low','dimension_condition'),
    row('Condition after dimension, si rather than i.e.','(si','(i.e.\\','(si',False,True,'misread word',
        'The parenthesis is followed by a compact s and a distinct i dot. There are no separate i, e and abbreviation points corresponding to i.e.',
        'high','dimension_condition'),
    row('Condition before 0, deleted symbol',r'\deleted{\unsure{\nu}}','[no witness]',r'\deleted{\unsure{\nu}}',False,True,'deletion state',
        'A small heavily filled cancellation stands before the live 0. Only an oblique upper trace survives, allowing but not establishing nu; the deleted source element is retained explicitly.',
        'low','dimension_condition'),
    row('Before final topos list, cancelled Néanmoins',r'\deleted{Néanmoins}',r'\struck{\ill{}}',r'\deleted{\unsure{Néanmoins}}',False,True,'other',
        'The initial capital N is distinct, with low remnants of the remainder under a continuous rising strike. Néanmoins is plausible, but the middle letters are too covered for C’s certainty; the whole deleted word is now localized as doubtful.',
        'low','en_fait_revision',True),
    row('Replacement phrase and order before final topos list',r'\inserted{En fait} ce sont les topos','Ce sont en\nfait les topos',r'\inserted{En fait} ce sont les topos',False,True,'insertion or placement',
        'En fait is written above the cancelled word, with the long f descender crossing its strike. The live baseline to the right reads ce sont les topos. The insertion therefore precedes ce sont; it is not placed after those words.',
        'high','en_fait_revision'),
    row('First classifying topos, group name and argument',r'B_{\unsure{\operatorname{GP}(1)|\operatorname{PGL}(1)}}',r'B_{\mathrm{PGL}(2)}',r'B_{\operatorname{GP}(1)}',False,True,'misread symbol or index',
        'Below B are precisely two letters: an open G with an inward return, then P with a rounded upper loop and descending stem. A left parenthesis, one upright 1 and a right parenthesis follow. No L is present and the numeral has no curved top or diagonal base of 2.',
        'high','first_classifying_group',False,True),
    row('Third classifying topos, G alphabet rendering',r'B_{G_m}',r'B_{\mathbb{G}_m}',r'B_{G_m}',False,True,'other',
        'The subscript is G with its inner return, followed by a small m. C’s ordinary G rendering is retained rather than a blackboard alphabet; this does not change the source group and is not consequential.',
        'medium','last_classifying_insertion'),
    row('Inserted fourth classifying topos',r'\inserted{B_e=e}',r'($B_G$ = \uncertain{classifiant} de \ill{})',r'\inserted{B_e=e}',False,True,'misread symbol or index',
        'Above the continuation is B with a small e subscript, a two-bar equality sign and another small e. A curved attachment brings this item into the list after B_Gm. The following prose is on the baseline; there is no parenthetical formula defining B_G as classifiant here.',
        'high','last_classifying_insertion',True,True),
    row('Bottom continuation, dont les','dont les','[no witness]','dont les',False,True,'omission',
        'Below the inserted B_e=e are a tall looped d, low on and t return, then a tall l with the es ending. These are the words dont les and continue off the page without a supplied object.',
        'high','last_classifying_insertion'),
    row('Bottom-left pencil pagination',r'\mspage{26}','[no witness]',r'\mspage{26}',False,True,'omission',
        'The lower-left corner has two pale pencil digits: 2 followed by a looped 6. The hand is unknown; the page-number macro records only the value.'),
]


def decision(mark,choice,reading,ink,confidence='high',crop=None):
    path,box=loc(crop)
    return {'id':mark,'decision':choice,'reading':reading,'ink':ink,'crop':path,'box':box,'confidence':confidence}

decisions = [
    decision('M0710','first','Arrêtons','The opening capital A, repeated short r movements, accented middle and low final ons return are readable. The word was settled from the native half; the closure crop additionally confirms its four following points.'),
    decision('M0711','first','les schémas','The article has a terminal s, and the noun has a separate final s-shaped return after its a. The plural is retained despite the singular predicate later in the sentence.','high','les_schemas'),
    decision('M0712','undecided',r"\unsure{d'un|d'une}",'The low humps favor un, but the extended final return can include an e. The ink does not securely exclude either ending.','medium','isom_and_article'),
    decision('M0713','first',r'\operatorname{GP}(1)','Two source letters G and P are followed immediately by parentheses around one upright 1. There is no L or digit 2.','high','first_classifying_group'),
]

items = [
    ('text','top five manuscript lines','que l’opération ... Arrêtons, four continuation points','his hand'),
    ('drawing','below opening paragraph, centered','short bare horizontal separator','his hand'),
    ('margin note','left of section title','circled 9','his hand'),
    ('text','two-line section title','Les schémas et Topos fondamentaux dans la théorie.','his hand'),
    ('margin note','left of modular-topos heading','circled A','his hand'),
    ('deletion','heading A, first crossed word','Topos','his hand'),
    ('deletion','heading A, second crossed word','Étendus / Étendue, ending doubtful','his hand'),
    ('insertion','above the second crossed heading word','Topos','his hand'),
    ('text','heading A and following two manuscript lines','modulaires pour les courbes de genre 0 avec nu points marqués, et famille ... modulaire','his hand'),
    ('insertion','above pour les, attached by curved call','(T_(0,nu)) over barred Q','his hand'),
    ('deletion','between famille and modulaire','des','his hand'),
    ('deletion','before nu-ponctuée','par, doubtful','his hand'),
    ('text','end of modular-family paragraph','nu-ponctuée sur T_(0nu), four continuation points','his hand'),
    ('text','main paragraph beginning Le Topos','Le Topos ... n’est pas un étendu ... les schémas d’Isom ... rang 1 ... sections ... est lisse de dim rel.','his hand'),
    ('deletion','inside 3-nu ... >0 expression','comparison sign obscured by crossing strokes','his hand'),
    ('deletion','inside si ... 0<=nu<=2','small doubtful nu before the live 0','his hand'),
    ('deletion','line before final list','Néanmoins, doubtful under long strike','his hand'),
    ('insertion','above the cancelled Néanmoins','En fait','his hand'),
    ('text','to the right of the En fait replacement','ce sont les topos','his hand'),
    ('display','bottom baseline, three initial entries','B_GP(1), B_Aff(1), B_Gm','his hand'),
    ('insertion','above last continuation, with curved attachment into the list','B_e=e','his hand'),
    ('text','bottom-right continuation','dont les','his hand'),
    ('margin note','bottom-left corner','26','unknown (pencil pagination)'),
]
inventory = [{'sheet_kind':'text','hand':hand,'element':f'E{i:02d}','kind':kind,'position':position,'first_words_or_objects':content,'transcribed':'yes'} for i,(kind,position,content,hand) in enumerate(items,1)]

remaining = [
    {'place':'Opening action-group letter','reading':r'\unsure{\mathcal E|\Sigma}','alternatives':'calligraphic E; Sigma','confidence':'low','reason':'The shared alphabet identification remains open despite the two rounded bowls. Preferred E is used only as the collation preference.'},
    {'place':'Two opening object-set letters','reading':r'\unsure{\tau|\mathcal T}','alternatives':'tau; calligraphic T','confidence':'medium','reason':'Both have an upper loop/cap and one curved lower return; the second head is heavily retraced. Preferred tau is not a claim that T is impossible.'},
    {'place':'Cancelled adjective in heading A','reading':r'\deleted{Topos \unsure{Étendus|Étendue}}','alternatives':'Étendus; Étendue','confidence':'low','reason':'The accent and stem sequence are visible, but the terminal e/s return is merged with the strike.'},
    {'place':'Cancelled word before nu-ponctuée','reading':r'\deleted{\unsure{par}}','alternatives':'par; another partly obliterated word','confidence':'low','reason':'Only a p-like descending start and small rounded remnant remain below the cancellation.'},
    {'place':'M0712 before X/S','reading':r"\unsure{d'un|d'une}",'alternatives':"d'un; d'une",'confidence':'medium','reason':'The final low stroke cannot securely be assigned to n alone or to ne.'},
    {'place':'Character before sections marquées','reading':r'\unsure{2|\nu}','alternatives':'2; nu','confidence':'low','reason':'A curved upper hook and heavy foot resemble 2, unlike adjacent check-shaped nu forms, but the retouching leaves stroke order uncertain. Both witnesses give nu; their agreement was checked and not assumed.'},
    {'place':'Cancelled relation in 3-nu ... >0','reading':r'\deleted{\unsure{\geq|=|\leq}}','alternatives':'greater than or equal; equals; less than or equal','confidence':'low','reason':'Diagonal cancellation strokes obscure the original angle direction and possible equality bar. All alternatives remain deleted.'},
    {'place':'Deleted symbol before 0 in the condition','reading':r'\deleted{\unsure{\nu}}','alternatives':'nu; another obliterated symbol','confidence':'low','reason':'The filled strike preserves only an oblique upper remnant.'},
    {'place':'Cancelled word replaced by En fait','reading':r'\deleted{\unsure{Néanmoins}}','alternatives':'Néanmoins; an incompletely recoverable word beginning N','confidence':'low','reason':'The initial N and low ending remnants survive, but the middle letters are under the continuous strike.'},
]

certainty = [
    {'place':'M0710','C':r'\unsure{Arrêtons}','final':'Arrêtons','ink':'The capital A, middle accent/stems and final low ons return support the first reading.'},
    {'place':'M0711','C':r'\unsure{les schémas|le schéma}','final':'les schémas','ink':'Both the article and noun have visible final s returns.'},
    {'place':'M0713','C':r'\unsure{\operatorname{GP}(1)|\operatorname{PGL}(1)}','final':r'\operatorname{GP}(1)','ink':'There are two group letters, then a left parenthesis, upright 1 and right parenthesis; no L.'},
    {'place':'Cancelled relation, expanded uncertainty only','C':r'\deleted{\unsure{\geq|=}}','final':r'\deleted{\unsure{\geq|=|\leq}}','ink':'The crossing strokes leave the angle direction unresolved, so a less-or-equal graph cannot be excluded. The preferred first reading and deletion state are unchanged.'},
    {'place':'Cancelled Néanmoins, reduced certainty','C':r'\deleted{Néanmoins}','final':r'\deleted{\unsure{Néanmoins}}','ink':'Only the initial N and low remnants can be separated from the long strike. The proposed word is retained but no longer asserted confidently.'},
]

notation = [
    {'form':r'\pi;\unsure{\tau|\mathcal T};\unsure{\mathcal E|\Sigma}','meaning':'The group, its operated-on set and the extension/action group in the opening continuation.','evidence':'One compact pi, two loop-capped set letters and one two-bowl action-group letter were individually checked. Preferred tau and E remain explicit alternatives, not established names.'},
    {'form':r'T','meaning':'The unfinished T- expression in the opening.','evidence':'It has a plain curved cap and an isolated upright, followed by one short hyphen. No subsequent word is supplied.'},
    {'form':r'\mathcal T_{0,\nu};\mathcal T_{0\nu}','meaning':'The modular-topos notation in the heading and main paragraph.','evidence':'The inserted and main formulas have a visible comma between 0 and nu. The intervening family-base occurrence does not. These locally written indices are not harmonized.'},
    {'form':r'\overline{\mathbf Q};\mathbf Q','meaning':'The barred and unbarred rational-field bases of the two parenthesized modular-topos formulas.','evidence':'Only the inserted heading formula has a separate bar over Q. C’s established bold-Q alphabet convention is retained.'},
    {'form':r'X/S','meaning':'The projective fibration in the Isom sentence.','evidence':'X has two ordinary crossing strokes without the ornamental loops used for the separate shared fraktur-X notation; the source here is left as plain X.'},
    {'form':r'\nu;\unsure{2|\nu}','meaning':'The marked-point parameter elsewhere, and the doubtful character immediately before sections.','evidence':'The point count, puncturing prefix, parameter range and dimension formula use check-shaped nu graphs. The sections character has a round upper hook and heavy foot and is kept separately doubtful.'},
    {'form':r'B_{\operatorname{GP}(1)}, B_{\operatorname{Aff}(1)}, B_{G_m}, B_e=e','meaning':'The source’s list of toposes, with its fourth entry inserted above the continuation.','evidence':'GP has exactly two letters and argument 1; Aff has two f strokes and argument 1; the third has G with lower m; the added entry has lower e, a two-bar equals sign and e.'},
]

abbreviations = [
    {'form':'symp.','expansion':'Expansion not established on this page; the abbreviation is retained without choosing one.'},
    {'form':'Isom','expansion':'isomorphismes'},
    {'form':'dim','expansion':'dimension'},
    {'form':'rel.','expansion':'relative'},
    {'form':'GP','expansion':'Expansion not explicitly given on this page; the two written letters are retained.'},
    {'form':'Aff','expansion':'affine (operator abbreviation retained as written)'},
]

hand_log = [
    {'habit':'A dot or short flattened stroke can be a whole small a/e movement; tall t and accent traces then identify the word.','places':'a été in the opening; avec after rang 1; short prose words throughout','scope':'All words on this page were inspected, with these particular examples enlarged where needed.','misreadings':'H soit for a été and et de for avec.'},
    {'habit':'Object-set heads can be looped or repeatedly retraced above a single lower curve.','places':'Both opening set letters','scope':'Both occurrences inspected independently; no Z harmonization.','misreadings':'C tau versus H calligraphic T remains one preferred-tau uncertainty.'},
    {'habit':'The action-group glyph can have two very open rounded bowls.','places':'Opening opération de E/Sigma','scope':'This single occurrence inspected against the supplied shared notation.','misreadings':'Preferred E versus H Sigma remains unresolved at low confidence.'},
    {'habit':'Continuation marks may have four points, while a title has one full stop.','places':'After Arrêtons; after T_(0nu); after théorie','scope':'All three endings inspected and counted separately.','misreadings':'Both witnesses reduce the first two to three points; H extends the title ending to an ellipsis.'},
    {'habit':'A heavy strike can hide a final e/s or the middle of a word while leaving a readable beginning.','places':'Étendus/Étendue; par; Néanmoins','scope':'Each cancellation has its own retained uncertainty, not a shared inferred reading.','misreadings':'C’s unmarked Néanmoins is now doubtful; H leaves these passages illegible.'},
    {'habit':'The writer may keep a plural subject and a singular verb in the same sentence.','places':'les schémas ... est lisse','scope':'Both forms are directly inspected on this page.','misreadings':'No grammatical correction to le schéma or sont lisses is introduced.'},
    {'habit':'The ordinary nu is often check-shaped, but the sections character is round-topped and retouched.','places':'All nu occurrences and the character before sections marquées','scope':'The two graphic families are distinguished locally; the numeral/letter ambiguity is not resolved by the formula that follows.','misreadings':'Both witnesses give nu before sections; candidate flags 2/nu instead of assuming their agreement.'},
    {'habit':'Open G plus a P loop can be mistaken for a familiar three-letter group abbreviation.','places':'First classifying topos subscript GP(1)','scope':'This subscript and its argument inspected in the dedicated crop.','misreadings':'C’s PGL(1) alternative and H’s PGL(2) are unsupported: no L, and the argument is one upright 1.'},
    {'habit':'Inserted formulas use long curved calls whose lower sweep is not a parenthesis around prose.','places':'Barred-Q moduli formula above pour; B_e=e above dont les','scope':'Both insertion calls inspected from their formulas to the attachment sites.','misreadings':'H separates the first with an ellipsis and treats the second as a parenthetical B_G definition.'},
]

notes = [
    {'id':key+'-N1','text':'The opening continues a prior sentence: the operation of pi on the unresolved tau/T set has been extended to an action of the unresolved E/Sigma group. The author then says this does not give an interprétation symp. de la T-, leaves that expression unfinished, and writes Arrêtons followed by four points. Symp. is not expanded, and no missing word after T- is supplied.'},
    {'id':key+'-N2','text':'After a short rule, the circled section 9 is headed Les schémas et Topos fondamentaux dans la théorie. The circled A begins a revised heading: Topos and an accented Étendus/Étendue are struck, Topos is reinserted above, and the live adjective is modulaires. An interlinear formula over barred Q attaches before pour les courbes de genre 0 avec nu points marqués. The source then describes a modular nu-punctured family and uses an intervening T index written 0nu without a comma.'},
    {'id':key+'-N3','text':'The main paragraph explicitly states that the indicated topos over Q, for nu=0,1,2, n’est pas un étendu. Its given explanation names les schémas d’Isom of an X/S that is fibré projectif de rang 1, with marked sections distinct on each fibre, and uses the singular predicate est lisse de dim rel. 3-nu >0. The plural subject and singular verb are retained exactly. This report describes the page’s assertion; it does not prove it.'},
    {'id':key+'-N4','text':'The character before sections marquées resembles the numeral 2 but is heavily retouched; both source witnesses read nu. The candidate therefore has an explicit 2/nu alternative rather than a silent normalization. If later comparison confirms a written 2, that source reading should stand even if the surrounding parameter argument suggests nu. The cancelled relation before >0 and the deleted symbol before 0 in the condition remain separately doubtful.'},
    {'id':key+'-N5','text':'At the bottom, a cancelled word tentatively read Néanmoins is replaced by the interlinear En fait before ce sont les topos. The list is B_GP(1), B_Aff(1), B_Gm, with B_e=e inserted as another entry. GP(1) is the literal two-letter name and argument shown by the ink; no modern identification with PGL or different dimension convention is supplied. The page ends in the words dont les.'},
    {'id':key+'-N6','text':'The only pagination visible is pencil 26 at the lower left, in an unidentified hand. The circled 9 and A belong to the inked text. There are no geometric diagrams or further independent drawings beyond the short horizontal separator and the insertion calls. Alphabet-only E/Sigma and tau/T comparisons use preferred C readings with against_C false and against_H true, without claiming that an unresolved alternative has been disproved.'},
]

check_events = [
    {'statement_id':key+'-N1','type':'carried as background without fault found','outcome':'The action-extension wording and every associated symbol were visually collated only. No independent reconstruction of the preceding argument or proof was attempted.'},
    {'statement_id':key+'-N2','type':'carried as background without fault found','outcome':'The modular-topos formulas, bases, genus, marked-point parameter, cancellation states and insertion attachments were checked on the page. This was source comparison, not a mathematical verification of a moduli construction.'},
    {'statement_id':key+'-N3','type':'carried as background without fault found','outcome':'The negative statement, Isom wording, rank 1, fibrewise condition and dimension/range expression were read from the ink. No independent re-proof of smoothness, dimension or non-étendue was performed. The sections-count glyph and cancelled relations remain unresolved.'},
    {'statement_id':key+'-N5','type':'carried as background without fault found','outcome':'The group labels, argument digits and inserted B_e=e were checked visually. No external definition or mathematical equivalence was used to replace GP(1) with PGL(2); the literal source label controls the transcription.'},
]

report = {
    'key':key,'reader':'B','stage':'first','image_views':['original','half1','half2'],
    'changes':changes,'decisions':decisions,'inventory':inventory,'remaining_doubts':remaining,
    'certainty_resolutions':certainty,'notation':notation,'abbreviations':abbreviations,'hand_log':hand_log,
    'notes':notes,'check_events':check_events,
    'unresolved_for_main':[
        'Sections-count character: crops/143_scan027_readerB_rank_and_sections.png, box [349,1780,1505,1909]. Candidate retains 2/nu against both witnesses, with low confidence and consequential status.',
        'Heading adjective ending: crops/143_scan027_readerB_heading_revisions.png, box [430,844,1528,1101]. Accent over E is visible; Étendus/Étendue remains open.',
        'Cancelled par: crops/143_scan027_readerB_punctured_family.png, box [349,1280,1405,1446].',
        'M0712 d’un/d’une: crops/143_scan027_readerB_isom_and_article.png, box [350,1660,1170,1787].',
        'Deleted relation and pre-0 symbol: crops/143_scan027_readerB_dimension_condition.png, box [837,1985,1564,2111]. Candidate leaves relation direction/equality and deleted nu uncertain.',
        'Cancelled Néanmoins: crops/143_scan027_readerB_en_fait_revision.png, box [363,2104,1345,2240]. Source word remains tentative; En fait placement is settled.',
        'Shared E/Sigma and two tau/T occurrences remain unresolved at the requested low/medium, non-consequential encoding levels. They are covered by opening_symbols and second_set crops.',
    ],
    'raw_difference_disposition':'All packet differences and all agreements were checked against the original once, both native halves once each, and one saved crop for each remaining open locus or adjacent open block. Twelve crops were each viewed once; no whole half was upscaled. Changes include source words, signs, indices, punctuation counts, cancellations, insertion placement and alphabet rendering choices. Pure section/subsection, circled-label, operator-font, spacing and TeX-wrapper syntax are not separate material rows when their reading is the same. H’s editorial notes are not copied as source text. Preferred E/Sigma rows are low confidence and non-consequential; preferred tau/T rows are medium and non-consequential, with against_C false and against_H true. All C/H and final excerpts were checked as literal substrings. Decisions use only M0710–M0713 in packet order; every new doubt is confined to remaining_doubts. No OCR, research, web access, TeX compilation, audit of other pages, or independent proof was used.'
}

assert [d['id'] for d in decisions] == [m['id'] for m in pkt['marks']]
allowed = {'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(c['kind'] in allowed for c in changes)
assert len({e['element'] for e in inventory}) == len(inventory)
for c in changes:
    if c['place'] == 'Opening, action-group glyph':
        assert c['confidence'] == 'low' and not c['against_C'] and c['against_H'] and not c['consequential']
    if c['place'] in {'Opening, first object-set glyph','Opening, second object-set glyph'}:
        assert c['confidence'] == 'medium' and not c['against_C'] and c['against_H'] and not c['consequential']

tex = root/'reviews'/f'{key}_readerB.tex'
js = root/'reviews'/f'{key}_readerB.json'
tex.write_text(candidate)
js.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Candidate: {tex}')
print(f'Report: {js}')
print(f'{len(changes)} changes; {len(decisions)} original MARKS decisions; {len(inventory)} inventory items; {len(boxes)} crops; {len(remaining)} retained doubts.')
