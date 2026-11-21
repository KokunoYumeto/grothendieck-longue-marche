from pathlib import Path
import json, re

W=Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
P=Path('/workspace/scratch/481648fc487b/reader_packets/150_scan039')
T=(W/'reader_returns/150_scan039.tex').read_text()
C=(P/'C.tex').read_text()
H=(P/'H.tex').read_text()
boxes={
'page15':[65,31,121,97], 'title':[203,52,542,158],
'equisinguliere':[566,38,916,171], 'ens_order':[1264,72,1683,150],
'presentation':[454,143,1029,248], 'donnee':[1055,160,1642,239],
'category':[226,235,467,341], 'moderee':[805,221,1129,306],
'en_sens':[1148,250,1624,307], 'precise_ca':[241,335,911,446],
'contr':[479,510,753,628], 'functor':[414,631,1141,835],
'one_intro':[248,973,840,1077], 'one_map':[533,1047,1103,1165],
'relatif':[264,1183,954,1270], 'one_d':[1276,1166,1512,1307],
'fibrant':[1406,1222,1683,1349], 'margin_nb':[14,1058,425,1522],
'margin_star':[1105,437,1683,1196], 'enfin':[268,1346,583,1479],
'suffit_map':[610,1453,1351,1573], 'two_intro':[268,1563,802,1641],
'two_map':[702,1612,1667,1739], 'plongement':[267,1722,1069,1828],
'nb_fibrant':[277,1837,965,1945], 'plongement_insert':[945,1736,1667,1889],
'margin_lower':[19,1665,690,2307], 'cor_arrow':[392,1928,1597,2028],
'cor_objects':[276,2027,744,2126], 'cor_map':[832,2027,1643,2126],
'canceled_three':[235,2178,353,2262], 'folio38':[21,2297,77,2346],
'star_order_words':[1410,445,1683,1133]}

R={'scan':39,'reader':'reader_c','line_count':21,'changes':[],'marks':[],
   'inventory':[],'doubts':[],'notes':[],'check_events':[],
   'notation':[],'abbreviations':[],'hand_log':[],'second_boxes':[]}

def add(place,c,h,f,ev,crop,conf='high',kind='misread word',err='words',cc=False,ch=True,marked=False,cons=''):
    R['changes'].append(dict(place=place,C=c,H=h,final=f,evidence=ev,
      crop=f'150_scan039_{crop}.jpg',box=boxes[crop],confidence=conf,
      kind=kind,error_kind=err,marked_in_H=marked,change_C=cc,change_H=ch,consequential=cons))

add('opening / I ens.',r'\(I\) ens.',r'$I$ un ens.',r'\(I\) ens.',
    'After the capital I the next visible letters are ens and its stop; there is no intervening un.','ens_order',kind='text not on the page',err='text not on page')
add('opening / ordonne', 'ordonné','ordonné','ordonne',
    'No detached acute is visible above the final e in the supplied edge pixels. The word reaches the dark right edge, so absence is limited to the supplied image; no accent is supplied from spelling.','ens_order','medium','abbreviation expanded or spelling modernised','abbreviation/spelling',True,True)
add('opening / standart','standart','standard','standart',
    'The final letter has the upright and cross stroke of t, followed by a separate stop.','presentation',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling')
add('opening / initial category overtrace','catégorie',r'\struck{catégorie} catégorie',r'\unsure{ca}tégorie',
    'Only one tégorie continuation is written. The initial c-like cluster is overtraced; the horizontal overstroke does not clearly cancel the closed a oval. The cancellation state of the initial cluster remains unsettled. A second complete canceled catégorie is not present.','category','medium','text not on the page','text not on page')
add('opening / separate canceled blot below category',r'(\deleted{\illegible{1}}',r'(\struck{\ill{}}',r'\shortstack[l]{\unsure{ca}tégorie\\[-.2ex]\deleted{\illegible{1}}}',
    'A separate short canceled, unreadable cluster lies below the beginning of the category word, not beside the later opening parenthesis after M. Its underlying letters cannot be identified.','category','high','insertion or placement','insertion placement',True,True,True)
add('opening / modérée','modérée','modèle','modérée',
    'The middle group has a low r rather than a tall l; the d loop and accented endings support modérée.','moderee')
add('opening / en un sens non précisé',r'\unsure{en} un sens non précisé',r'par ex. pour \uncertain{fixer les} idées','en un sens non précisé',
    'The short opening has an overtraced e-loop followed by the n run; un sens non is separated on the same baseline and précisé begins the next. The longer phrase in H is not written.','en_sens','medium','misread word','words',True,True,True)
add('opening / ça','ça','ce','ça',
    'The first character has a lower cedilla-like return, and the following low closed/returning form fits a rather than e.','precise_ca','medium')
add('functor introduction / contr.',r'\inserted{contr.}','[absent]',r'\inserted{contr.}',
    'The raised contr. is visible above foncteur, including a separate terminal dot; the long bar below belongs to the f.','contr',kind='omission',err='omissions')
add('functor display / comma after M',r'\longrightarrow\mathcal M',r'\longrightarrow\mathcal M,',r'\longrightarrow\mathcal M',
    'The first display row ends at M without a following comma. The tuple is on the next row.','functor',kind='text not on the page',err='text not on page')
add('functor display / tuple punctuation',r'(i_0,\ldots,i_n)',r'(i_0,\ldots,i_n)',r'(i_0,\ldots i_n)',
    'There is a small comma after i_0, then the continuation marks and final i_n. No comma precedes the final index.','functor',kind='text not on the page',err='text not on page',cc=True)
add('condition 1 / singular introduction',r'Le \deleted{\unsure{app}} morphisme',r'Les \struck{\ill{}} morphismes',r"Le\unsure{'} \deleted{\unsure{app}} morphisme",
    'Le ends in its short e with no s; morphisme ends in a low e with no plural s. The detached tick is independently catalogued.','one_intro',marked=True)
add('condition 1 / detached tick after Le',r'Le \deleted{\unsure{app}}',r'Les \struck{\ill{}}',r"Le\unsure{'}",
    'A small unstruck tick sits above/right of the e in Le, before the canceled app. Its apostrophe-like shape is preserved without assigning a grammatical function.','one_intro','medium','omission','omissions',True,True,True)
add('condition 1 / canceled app',r'\deleted{\unsure{app}}',r'\struck{\ill{}}',r'\deleted{\unsure{app}}',
    'The initial a-like head and two descending p strokes survive, but the cross stroke obscures letter interiors. The prior C doubt is retained; H leaves this partially recoverable sequence wholly illegible.','one_intro','low',r'readable ink left as \ill{}','readable ink left as illegible',False,True,True)
add('condition 1 / target index punctuation',r'\Sigma_{i_0,\ldots,i_p}',r'\Sigma_{i_0,\ldots,i_p}',r'\Sigma_{i_0,\ldots i_p}',
    'The index contains a comma after i_0, but none between the continuation marks and i_p.','one_map',kind='text not on the page',err='text not on page',cc=True)
add('condition 1 / relatif :','relatif à','relatifs :','relatif :',
    'The word ends at f, with no s. Two distinct dots form the following colon; they do not form an à.','relatif',cc=True)
add('condition 1 / inclusion hook',r'd\unsure{\hookrightarrow}d\x27',r'd\hookrightarrow d\x27',r'\hookrightarrow',
    'The left end curves upward into a hook and the right end carries an arrowhead. This clears the C uncertainty from ink, without using the mathematical role.','one_d',kind='misread symbol or index',err='symbols and indices',cc=True,ch=False)
R['changes'][-1]['C']="d\\unsure{\\hookrightarrow}d'"
R['changes'][-1]['H']="d\\hookrightarrow d'"
add('condition 1 / opaque canceled low symbol','[absent]','[absent]',r'd_{\deleted{\unsure{?}}}',
    'A separate opaque canceled blot lies low/right of the first d. No underlying letter or symbol can be read. The ? in this transcription is an editorial uncertainty placeholder, not manuscript punctuation; subscript placement records its low location only.','one_d','medium','omission','omissions',True,True)
add('condition 1 / p and n below d and d prime',r'\inserted{\(\unsure{p}\)\quad\(\unsure{n}\)}','[absent]',r"\underset{\inserted{p}}{d_{\deleted{\unsure{?}}}}\hookrightarrow\underset{\inserted{n}}{d'}",
    'A p with descender lies under the first d and a short n under d prime in the inclusion formula. They are not appended after the later d prime at the end of the prose clause.','one_d','medium','insertion or placement','insertion placement',True,True)
add('condition 1 / est fibrant',r'est \uline{fibrant}',r'sont \emph{fibrants}',r'est \uline{fibrant}',
    'The source has est and singular fibrant. The horizontal line is below fibrant and leaves the word live.','fibrant')
add('condition 1 / terminal punctuation',r'\uline{fibrant}\(^*\).',r'\emph{fibrants}${}^{*}$',r'\uline{fibrant}\(^*\)',
    'The raised asterisk is visible, but no independent terminal period is recoverable before the dark edge. This records the supplied pixels only.','fibrant','medium','text not on the page','text not on page',True,False)
add('left NB / inserted on',r'\inserted{on}','[absent]',r'\inserted{on}',
    'A small on is raised above the note and linked by a curved leader to the beginning of ne poser.','margin_nb',kind='omission',err='omissions')
add('left NB / ne poser',r'\unsure{ne poser}',r'NB cette condition \ill{} \ill{} \ill{} \ill{}', 'ne poser',
    'The n/e group, p descender, o/s run, and terminal r can be separated. The phrase is retained without supplying a conjugated verb.','margin_nb','medium',r'readable ink left as \ill{}','readable ink left as illegible',True,True,True)
add('left NB / que dans le cas équisingulier','cette condition que dans le cas équisingulier.',r'cette condition \ill{} \ill{} \ill{} \ill{} \uncertain{équisingulière}', 'cette condition que dans le cas équisingulier',
    'The note continues que dans le cas and ends in the masculine équisingulier; no final e is separated. No final period is visible.','margin_nb','medium','misread word','words',True,True,True)
add('asterisk note / Cela','Cela',"C'est",'Cela',
    'The initial capital C is followed by a small e, tall l, and low a; it is not C apostrophe est.','margin_star')
add('asterisk note / si on veut',r'\unsure{si on veut|$=$ pour}','si on veut','si on veut',
    'The narrow opening s/i, rounded on, and following veut form three groups. The alternative equals-sign phrase does not fit those separated strokes.','margin_star','medium','misread word','words',True,False)
add('asterisk note / equality in extension flag',r"d'\unsure{\supset|=}d\amalg\delta",r"d'=d\amalg\delta",r"d'=d\amalg\delta",
    'The relation has two short horizontal strokes; their close right ends had suggested a curved relation, but the two bars support equality. Root independently adjudicated the same two-bar reading in the existing crop.','margin_star','medium','misread symbol or index','symbols and indices',True,False)
add('asterisk note / variable and extra delta',r'\unsure{variable}',r'$\delta$ variable','variable',
    'The v start, tall b, and final l/e support variable. No second delta is written between the preceding formula and this word.','margin_star','medium','misread word','words',True,True)
add('asterisk note / où delta est donc',r'(où \(\delta\) est \unsure{donc}',r'(i.e. $\delta$ est donné comme',r'(où \(\delta\) est donc',
    'The opening is a short où, not i.e.; after est, the looped d, low on and c-return fit donc. There is no separate comme.','margin_star','medium','misread word','words',True,True)
add('asterisk note / un drapeau quelconque de','un drapeau quelconque de','drapeau quelconque des','un drapeau quelconque de',
    'A short un precedes drapeau. The end of the line is de; the following line begins the separate l’ens.','margin_star')
add('asterisk note / ordered-set line',r"l'ens \(I'\) des \(i\in I\)",r'des $I^{\,\ill{}}$, \ill{} \ill{} \ill{}',r"l'ens \(I'\) des \(i\in I\)",
    'The abbreviation l’ens and barred capital I with a separate prime are followed by des i in I. The membership sign and both i/I forms are recoverable; H leaves this stretch largely illegible.','margin_star','medium',r'readable ink left as \ill{}','readable ink left as illegible',False,True,True)
add('asterisk note / crowded order wording',r'\unsure{fort\(^{t}\)|fortement} \uline{\unsure{supérieur|supérieurs}}',r'\ill{} \ill{} \ill{}',r'\unsure{fort\(^{t}\)} \uline{\unsure{plus grands|supérieurs}}',
    'The first group is visibly abbreviated, with a tall f/t-like structure and a raised terminal sign. The next low run and descender suggest plus grands, but plus is not independently secure and supérieurs remains possible. This is an unresolved partial reading, not a cleared C doubt.','star_order_words','low',r'readable ink left as \ill{}','readable ink left as illegible',False,True,True)
add('asterisk note / raised strict-like insertion','[absent]','[absent]',r'\inserted{\unsure{strict}}',
    'Small raised letters at the far right form a strict-like group above the crowded order wording. The separate insertion is real, but its precise ending and attachment remain doubtful. No expansion to strictement is supplied.','star_order_words','low','omission','omissions',True,True)
add('asterisk note / cancellation of famille',r'\deleted{\unsure{famille}}','la famille',r'\deleted{\unsure{famille}}',
    'The family-word is crossed by a heavy horizontal stroke. Several interior letters remain covered, so the C doubt is kept even though the cancellation is clear.','margin_star','medium','deletion state (struck given live or live given struck)','struck text',False,True)
add('asterisk note / stratification',r'\unsure{stratification}','[absent]',r'\unsure{stratification}',
    'A live long word follows the canceled family-word. Its opening and long terminal run favor stratification, but crowding and the edge prevent a secure complete reading. H supplies no corresponding live word.','margin_star','low','omission','omissions',False,True)
add('asterisk note / qu’ils forment au dessus de',"qu'ils forment au dessus de",r"des $\Sigma_{d'}$ au-dessus de", "qu'ils forment au dessus de",
    'The source has qu’ils with apostrophe, the f descender and run of forment, then au dessus de. There is no separate Sigma term on this line.','margin_star','medium')
add('asterisk note / final Sigma index',r"\(\Sigma_{d'}\)",r'$\Sigma_d$',r"\(\Sigma_{d'}\)",
    'A distinct prime stands to the right of the final d subscript. It is preserved although the surrounding assertion might invite a different base index.','star_order_words',kind='misread symbol or index',err='symbols and indices',cons='The marginal local-triviality assertion is written over Sigma with d prime, without editorial repair.')
add('asterisk note / terminal stop','est loc. triviale.','est loc. triviale','est loc. triviale',
    'The abbreviation loc. has its stop. The end of triviale runs into the dark edge; no independent sentence stop is recoverable.','margin_star','medium','text not on the page','text not on page',True,False)
add('parenthetic reduction / canceled Enfin',r'\deleted{\unsure{Enfin}}','[absent]',r'\deleted{\unsure{Enfin}}',
    'After the opening parenthesis a canceled word has the tall E/n/f-like structures and final dotted i/n run of Enfin. Its interiors remain obscured, so the C doubt is retained. H omits this canceled span.','enfin','low','omission','omissions',False,True)
add('condition 2 / singular introduction','Le morphisme','Les morphismes','Le morphisme',
    'Le has a short terminal e and morphisme a low terminal e; there is no s on either word.','two_intro')
add('condition 2 / placement of replaced map',r'\deleted{\unsure{\Sigma_{d\x27}}\longrightarrow\Sigma_d}',r'\struck{$\Sigma_{d\x27}\to\Sigma_d$}',r'\begin{aligned}',
    'The live indexed map is above the crossed earlier map, whose left end starts farther left. C places both on one horizontal row. The new aligned display records their vertical relation; the canceled source index stays doubtful.','two_map','high','insertion or placement','insertion placement',True,False)
R['changes'][-1]['C']=r"\deleted{\unsure{\Sigma_{d'}}\longrightarrow\Sigma_d}"
R['changes'][-1]['H']=r"\struck{$\Sigma_{d'}\to\Sigma_d$}"
start=T.index(' \\begin{aligned}',T.index('(2) Le morphisme'))
end=T.index(' \\end{aligned}',start)+len(' \\end{aligned}')
R['changes'][-1]['final']=T[start:end].strip()
oval=r'\tikz[baseline=(v.base)]{\node[inner sep=2pt] (v) at (0,0) {\(p\ne n\)};\draw (0,0) ellipse [x radius=.48cm,y radius=.28cm];}'
add('condition 2 / oval around p not equal n',r'\boxed{p\ne n}',r'« $p\neq n$ » est entouré.',oval,
    'A rounded hand-drawn enclosure surrounds p not equal n. It has no rectangular corners. H’s explicit note accounts for the enclosure; only C’s rectangle is changed.','two_map',kind='drawing or diagram',err='drawings and diagrams',cc=True,ch=False)
add('condition 2 / est un plongement-bord','est un plongement-bord',r'sont des \emph{plongements-bord}','est un plongement-bord',
    'The source has est un and a singular plongement before the hyphen; bord is singular.','plongement')
add('condition 2 / singular inserted explanation',r'\inserted{i.e. plongement \inserted{\unsure{bord}} cylindrique}',r'\add{i.e. plongements \uncertain{bords} cylindriques}',r'\inserted{i.e plongement \inserted{\unsure{bord}} cylindrique}',
    'The inserted explanation has singular plongement and cylindrique. Its raised bord remains doubtful, but no separate final s is visible. The nested insertion is kept in place.','plongement_insert','medium','misread word','words',False,True,True)
add('condition 2 / i.e punctuation','i.e.','i.e.','i.e plongement',
    'The i and e are separated by one point. There is no point on the baseline after e. A detached dot much lower is unassigned and is documented separately rather than attached as punctuation.','plongement_insert',kind='text not on the page',err='text not on page',cc=True)
add('condition 2 / ordinary morphisme in NB','morphisme fibrant',r'\add{morphisme} fibrant','morphisme fibrant',
    'Morphisme is written on the ordinary continuation baseline before fibrant, with no local insertion leader or raised placement.','nb_fibrant',kind='insertion or placement',err='insertion placement')
add('lower margin / On va supposer','On va supposer','On veut','On va supposer',
    'After On a short va is visible, followed by the long supposer group with paired descending p strokes. H collapses this to veut.','margin_lower')
add('lower margin / données',r'\unsure{données|donnés}',r'de plus \ill{}',r'\unsure{données|donnés}',
    'The initial d and low onn run are recoverable, but the compressed final sequence does not decide the extra e. The original C alternatives are retained.','margin_lower','low',r'readable ink left as \ill{}','readable ink left as illegible',False,True,True)
add('lower margin / canceled family and inserted des',r'une \deleted{\unsure{famille}} \inserted{des}','une structure',r'une \deleted{\unsure{famille}} \inserted{des}',
    'Une remains live. The following family-word is horizontally canceled and a raised des is linked toward structures. Covered letter interiors prevent clearing the C famille doubt; H omits both this canceled word and its insertion.','margin_lower','medium','omission','omissions',False,True)
add('lower margin / structures cylindriques','structures cylindriques','structure cylindrique','structures cylindriques',
    'Both words have a final low plural run. The long l and q descender in cylindriques are distinct.','margin_lower')
add('lower margin / correspondantes et formuler',r'correspondantes, et \unsure{formuler}',r'\ill{} \ill{} \ill{}',r'correspondantes, et \unsure{formuler}',
    'Correspondantes, comma, and et can be followed. The subsequent f-like tall stroke and compressed ending favor formuler, but intersections with the main text leave it unresolved.','margin_lower','medium',r'readable ink left as \ill{}','readable ink left as illegible',False,True,True)
add('lower margin / des conditions plus fortes que','des conditions plus fortes que','conditions (2)','des conditions plus fortes que',
    'Des, the conditions run, plus, the tall f and t of fortes, and que form the visible line before the numbered reference.','margin_lower','medium','omission','omissions')
add('lower margin / énoncées en langage',r'\unsure{énoncées en langage}',r'(2), \ill{} \ill{} \ill{}','énoncées en langage',
    'The initial accent and low énoncées group are followed by a separate en and the tall l plus g loop of langage. The whole phrase is readable at medium confidence.','margin_lower','medium',r'readable ink left as \ill{}','readable ink left as illegible',True,True,True)
add('lower margin / suivant',r'\unsure{suivant}',r'(2), \ill{} \ill{} \ill{}','suivant',
    'The final line begins with the s-return, short ui/v run, and an ending with the tall crossed t; a dash follows.','margin_lower','medium',r'readable ink left as \ill{}','readable ink left as illegible',True,True,True)
add('corollary / inclusion hook',r"d\unsure{\hookrightarrow}d'",r"d\hookrightarrow d'",r"d\hookrightarrow d'",
    'The left end turns upward before the straight arrow shaft, and the right arrowhead is distinct.','cor_arrow',kind='misread symbol or index',err='symbols and indices',cc=True,ch=False)
add('corollary / written equals',r'\(\unsure{=}\)','même',r'\(=\)',
    'Two detached horizontal bars, the lower with a slight upturn, are the written symbol after aient. They are not the spelled-out word même.','cor_arrow',kind='abbreviation expanded or spelling modernised',err='abbreviation/spelling',cc=True)
add('corollary / objt maximals',r'\unsure{objt maximals}',r'\ill{} \ill{} \ill{} \ill{} \ill{}',r'\unsure{objt maximals}',
    'The abbreviated objt has a loop and descender; the following maximal-like group is strongly compressed. The best partial reading is retained with C’s doubt and is not expanded or corrected to a grammatical phrase.','cor_objects','low',r'readable ink left as \ill{}','readable ink left as illegible',False,True,True)
add('bottom / canceled number 3',r'\deleted{\unsure{(3)}}','[absent]',r'\deleted{\unsure{(3)}}',
    'Parenthesis-like sides and a two-lobed central digit survive a broad diagonal cancellation. The digit is still partly obscured, so the original C doubt remains.','canceled_three','low','omission','omissions',False,True)
add('bottom / foliation 38',r'\margin{38}','[absent]',r'\margin{38}',
    'Thin, lighter strokes form a 3 followed by a two-loop 8 at the bottom left. The hand attribution is uncertain and differs in weight from the main text.','folio38',kind='omission',err='omissions')

# Exact original C marks, each occurrence separately.
def macros(s):
    out=[]
    for m in re.finditer(r'\\(?:unsure|illegible)\{',s):
        j=m.end(); depth=1
        while depth:
            if s[j]=='{' and (j==0 or s[j-1]!='\\'): depth+=1
            elif s[j]=='}' and (j==0 or s[j-1]!='\\'): depth-=1
            j+=1
        out.append((m.start(),s[m.start():j]))
    return out

md=[
('equisinguliere','undecided',r'\unsure{équisingulière}','The canceled word is recognizable in outline but multiple interior letters remain covered; the clear replacement cannot clear the old word.','low'),
('category','undecided',r'\illegible{1}','The separate lower canceled blot has no securely recoverable letters; its position is corrected.','low'),
('en_sens','first','en','An overtraced e loop and low n run can be separated before un sens non.','medium'),
('one_intro','undecided',r'\unsure{app}','The head and two descenders favor app, but cancellation covers interiors.','low'),
('one_d','first',r'\hookrightarrow','A curved left hook, shaft and right arrowhead are visible.','high'),
('one_d','first','p','The lower label has a short bowl and descender; it lies below the first d.','medium'),
('one_d','first','n','The lower label has one low arch and lies below d prime.','medium'),
('margin_nb','first','ne poser','The two word groups and final r can be followed; no conjugation is supplied.','medium'),
('margin_star','first','si on veut','Three short separated groups fit si/on/veut rather than the equality-sign alternative.','medium'),
('margin_star','alternative','=','Two short horizontal bars are visible; their close right ends do not require a superset curve. Root independently adjudicated equality in the same existing crop.','medium'),
('margin_star','first','variable','The v start, tall b and l/e ending are visible.','medium'),
('margin_star','first','donc','Looped d, low on and c return are recoverable.','medium'),
('star_order_words','undecided',r'\unsure{fort\(^{t}\)}','The group is visibly abbreviated; the expanded fortement alternative is removed because its extra letters are not written. The exact abbreviated reading remains doubtful.','low'),
('star_order_words','undecided',r'\unsure{plus grands|supérieurs}','The low run and later descending form can fit plus grands, but the letters of plus cannot all be separated; supérieurs remains possible. No syntax-based resolution.','low'),
('margin_star','undecided',r'\unsure{à}','The short linking stroke is too crowded for secure letter identification.','low'),
('margin_star','undecided',r'\unsure{\max}','The compact group before i_p is unresolved; the apparently redundant expression is not repaired from meaning.','low'),
('margin_star','undecided',r'\unsure{famille}','Several interior strokes remain under the cancellation; the visible outline is insufficient to clear the earlier doubt.','low'),
('margin_star','undecided',r'\unsure{stratification}','Live word after the cancellation, with compatible opening and long ending, but edge crowding prevents full identification.','low'),
('enfin','undecided',r'\unsure{Enfin}','Tall initial and f-like descender remain, but the heavy strike crosses the word body.','low'),
('two_map','undecided',r"\unsure{\Sigma_{d'}}",'The canceled source Sigma and its subscript are covered by overlapping strike strokes; the prime-like stroke does not clear the entire original doubt.','low'),
('plongement_insert','undecided',r'\unsure{bord}','The raised group has compatible b/r/d structures but its short interiors are crowded.','low'),
('margin_lower','undecided',r'\unsure{données|donnés}','The final low run does not distinguish an extra e; agreement cannot decide it.','low'),
('margin_lower','undecided',r'\unsure{famille}','The horizontal strike obscures several internal letters.','low'),
('margin_lower','undecided',r'\unsure{formuler}','A tall f-like stroke and compressed final run remain intersected by the horizontal main text.','low'),
('margin_lower','first','énoncées en langage','Initial accent, separate en, tall l and g loop support the complete phrase.','medium'),
('margin_lower','first','suivant','The short s/ui/v run ends with a tall crossed t before the dash.','medium'),
('cor_arrow','first',r'\hookrightarrow','A left hook and right arrowhead are distinct.','high'),
('cor_arrow','first','=','Two detached horizontal bars form the written equals sign.','high'),
('cor_objects','undecided',r'\unsure{objt maximals}','The abbreviation and next word remain strongly compressed; no expansion or spelling correction is made.','low'),
('canceled_three','undecided',r'\unsure{(3)}','The central two-lobed form is partly overwritten; parentheses and cancellation remain visible.','low')]
cm=macros(C)
assert len(cm)==len(md),(len(cm),len(md))
for (pos,mark),(crop,dec,reading,ev,conf) in zip(cm,md):
    context=re.sub(r'\s+',' ',C[max(0,pos-24):min(len(C),pos+len(mark)+35)])
    R['marks'].append(dict(mark=mark,context=context,decision=dec,reading=reading,evidence=ev,
       crop=f'150_scan039_{crop}.jpg',box=boxes[crop],confidence=conf))

def inv(kind,pos,words,hand='his hand'):
    R['inventory'].append(dict(element=f'039.E{len(R["inventory"])+1:02}',kind=kind,position=pos,
      first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('text','top left','15')
inv('text','main lines 1–6','Stratification … présentation standart … par un foncteur')
inv('deletion','title, line 1','équisingulière, canceled and still doubtful')
inv('insertion','above title, line 1','équisingulière')
inv('text','line 3 / category initial cluster','One live ca/tégorie word; initial ca-like cluster overtraced, cancellation state unsettled')
inv('deletion','below category at x≈275,y≈310','Separate unreadable canceled cluster')
inv('insertion','above foncteur','contr.')
inv('display','main lines 7–8','Σ:Drap(I)→M; tuple maps to indexed Σ')
inv('margin note','right diagonal margin, asterisk return','Cela est trop faible … local triviality note')
inv('insertion','far right within asterisk note','Raised strict-like group with uncertain ending and attachment')
inv('deletion','asterisk note, before stratification','famille, heavily canceled')
inv('text','main lines 9–10','avec les propriétés suivantes; (1) Le … morphisme')
inv('text','after Le in line 10','Detached unstruck apostrophe-like tick; function uncertain')
inv('deletion','line 10','app, canceled and doubtful')
inv('display','line 11','Σ with i0…in → Σ with i0,…ip')
inv('text','lines 12–13','relatif : une inclusion … est fibrant*')
inv('deletion','low/right of first d in inclusion formula','Opaque canceled symbol; editorial ? placeholder, not a written question mark')
inv('insertion','below the two d terms of inclusion formula','p below d, n below d prime')
inv('text','line 13','Underline under live fibrant; raised asterisk return')
inv('margin note','left diagonal margin beside condition 1','NB on ne poser cette condition que dans le cas équisingulier')
inv('insertion','above beginning of left NB','on with curved leader')
inv('deletion','before parenthetic reduction in line 14','(2), clearly canceled')
inv('deletion','inside opening parenthesis in line 14','Enfin, doubtful canceled word')
inv('text','line 14','il suffit de le supposer pour')
inv('display','line 15','Σ with i0…in → Σ with i0…i(n−1), followed by closing parenthesis')
inv('text','line 16','(2) Le morphisme')
inv('display','line 17','Replacement indexed Σ map, with hat on i_p; p≠n enclosed in oval')
inv('deletion','below replacement map','Earlier Σ-map, with doubtful source index')
inv('drawing','right of condition 2 display','Rounded oval around p≠n')
inv('text','lines 18–19','est un plongement-bord; NB si p=n … morphisme fibrant')
inv('insertion','between lines 18 and 19, to right','i.e plongement … cylindrique, with curved insertion leader')
inv('insertion','raised within inserted explanation','bord, doubtful')
inv('drawing','below/right of i.e, x≈1032,y≈1865','Small detached low dot, unassigned; documented in crop and notes without unsupported punctuation attachment')
inv('margin note','lower left diagonal margin','On va supposer de plus … suivant —')
inv('deletion','third line of lower marginal note','famille, canceled and doubtful')
inv('insertion','third line of lower marginal note','des, with small leader toward structures')
inv('text','main lines 20–21','Cor. Soit d↪d′ … = objt maximals … plongement.')
inv('text','under Cor.','Underline below live abbreviation Cor.')
inv('deletion','bottom of written area','(3), canceled and doubtful')
inv('margin note','bottom left','38','uncertain; thinner and lighter than the main hand')

def doubt(place,reading,alt='',conf='low'):
    R['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence=conf))
for m in R['marks']:
    if m['decision']=='undecided': doubt(m['context'],m['reading'],'Unresolved alternatives, where shown, remain tied to this crop.')
doubt('opening ending',r'\unsure{donné|donnée}','A final extra e is not independently separable.')
doubt('category initial cluster',r'\unsure{ca}tégorie','Initial letters and their cancellation state remain unsettled; no full repeated word.')
doubt('tick after Le',r"Le\unsure{'}",'Apostrophe-like mark; function unknown.','medium')
doubt('opaque canceled low symbol',r'\deleted{\unsure{?}}','? is an editorial placeholder only.','medium')
doubt('raised right-margin addition',r'\inserted{\unsure{strict}}','Exact abbreviated ending and attachment unsettled.')
doubt('NB terminal dot count',r'fibrant\unsure{.|:})','Two tiny diagonal marks may be one stop plus incidental mark or a colon; no asserted extra punctuation.','medium')

R['notes']=[
 'Reported content only: the page presents an equisingular stratification of a finite ordered set I by a contr. functor from Drap(I) to a topological modérée category. It states fibrancy for initial-segment restrictions and a border-embedding condition for deletion of a nonfinal index, then gives a corollary about flags with the same maximal object(s). None of these assertions was proved or checked in this reading.',
 'The left NB restricts the first condition to the equisingular case. The asterisk note calls the stated condition too weak and asks for a locally trivial stratification as the extension flag varies. The order wording and several canceled/marginal words remain unresolved; no mathematical reconstruction is used to complete them.',
 'The final base in the asterisk note is visibly Sigma_{d prime}. It is preserved even though the preceding fixed-d wording could invite an editorial index repair. No such repair or proof check was performed.',
 'Whole image and the two native halves were each inspected once. Thirty-three crop images, representing thirty-two principal places plus one permitted completion/detail of the unsettled right-margin wording, were all inspected. Existing category, order-word and broad marginal crops were reopened only to address the subsequently raised unresolved questions; no further crops were generated.',
 'Line count 21 denotes the principal horizontal text/display baselines. Marginal notes, raised insertions, the canceled bottom number and foliation are separately inventoried rather than added to that baseline count.',
 'The crossed/overtraced initial ca-like group of catégorie is not a second complete word. Its cancellation state is unsettled: the overstroke crosses the c-like cluster but does not clearly cross the closed a oval. The word stays live with a narrow initial doubt; the separate illegible canceled blot is positioned below it.',
 'The question mark used for the opaque canceled symbol low/right of d is an editorial uncertainty placeholder, not a manuscript question mark. Mathematical subscript placement represents its observed low location only; no underlying index is asserted.',
 'The apostrophe-like tick after Le is unstruck and preserved without assigning a grammatical function. The short ne poser is not conjugated or repaired. Donné/donnée and données/donnés are not decided from agreement.',
 'No detached acute is visible above ordonne at the upper right edge. Likewise no separate stop is recoverable after fibrant* or the edge-ending triviale; the missing image area is not reconstructed. Abbreviation and spelling forms such as standart, contr., fort^t, l’ens, and objt are not normalized.',
 'The small low dot beneath/right of i.e is real but lacks a supported textual attachment. It is retained in the crop and visual inventory as an unassigned mark, not silently made a final punctuation point. The literal abbreviation has only its middle point. After the other fibrant in the NB, two tiny diagonal marks leave a narrow period/colon doubt.',
 'The handwritten 15 uses the main dark hand. Bottom 38 is much thinner and lighter, with uncertain attribution. H’s editorial note already accounts for 15; it was not counted as an H omission.',
 'The title and présentation have no separately visible underline. H emphasis formatting is not treated as an independent ink disagreement. The clear underlines beneath fibrant and Cor. are retained. H’s note explicitly accounts for the oval around p≠n, so its note was not treated as omitted drawing content.',
 'All uncertainty-only additions and narrowed/reordered alternatives are documented as doubts rather than independently asserted errors against C. A retained partial reading can still differ substantively from H’s absent or wholly illegible passage; those rows explicitly retain low confidence.',
 'Validation was structural only: original mark coverage, source-string correspondence, crop existence, proposed-snippet presence and balanced TeX delimiters. No OCR, external research, TeX compilation, or reading of another page/reader was used.'
]
R['notation']=[
 dict(form=r'\Sigma_{i_0\ldots i_n}',meaning_or_shape='Capital Sigma indexed by a flag; its cap is part of the letter, not an overbar.',places='Functor and condition displays'),
 dict(form=r'\operatorname{Drap}(I)',meaning_or_shape='Drap written as a word with capital D, applied to the finite ordered set I.',places='Functor display'),
 dict(form=r'\hookrightarrow',meaning_or_shape='Inclusion arrow has an upturned left hook and right arrowhead.',places='Condition 1 and corollary'),
 dict(form=r'\widehat{i_p}',meaning_or_shape='Hat sits above i_p in the target flag.',places='Condition 2 display'),
 dict(form=r'\amalg',meaning_or_shape='Amalgamation/disjoint-union glyph between d and delta, not changed from its ink shape.',places='Asterisk note'),
 dict(form=r'=',meaning_or_shape='Two horizontal bars used in prose after aient; not expanded to même.',places='Corollary'),
 dict(form=r'\Sigma_{d\prime}',meaning_or_shape='Separate prime is visible on the final base index of the marginal assertion.',places='End of asterisk note')]
R['abbreviations']=[
 dict(form='ens.',expansion='ensemble'),dict(form="l’ens",expansion='l’ensemble'),
 dict(form='contr.',expansion='contravariant, probable in this context; expansion is not transcribed'),
 dict(form='NB',expansion='nota bene'),dict(form='loc.',expansion='localement'),
 dict(form=r'\unsure{fort\(^{t}\)}',expansion='fortement, possible expansion of the doubtful written abbreviation only'),
 dict(form=r'\unsure{strict}',expansion='possibly strictement; exact written abbreviated ending remains unsettled'),
 dict(form='i.e',expansion='id est'),dict(form='Cor.',expansion='corollaire'),
 dict(form='objt',expansion='objet, probable; the source abbreviation remains doubtful and unexpanded')]
R['hand_log']=[
 dict(habit='Terminal e and s can be extremely low but must be separated from grammatical expectation.',places='donné/donnée; Le/morphisme/fibrant; données/donnés',consistent='Clear singular endings in conditions; compressed endings remain doubtful in donnée(s).',witness_errors='H pluralizes both condition statements; no resolution claimed for the compressed participle endings.'),
 dict(habit='Small detached marks require a supported attachment before being made punctuation.',places='Le tick; i.e low dot; fibrant NB ending',consistent='Three distinct positional cases kept separate.',witness_errors='Both omit the tick and supply a final point after i.e; the NB dot count is unresolved.'),
 dict(habit='Cancellations may cover only part of a word and may be separate from a lower canceled blot.',places='catégorie initial cluster; canceled famille and Enfin',consistent='Initial category cancellation state differs from clearly canceled whole words.',witness_errors='H supplies an entire repeated canceled catégorie; both witnesses misplace the separate lower blot.'),
 dict(habit='Short strokes at index height are not inserted commas without visible separation.',places='Functor tuple; condition 1 target',consistent='Comma after first i_0 present; no comma before final indexed i.',witness_errors='Both witnesses supply the latter comma in these two places.'),
 dict(habit='Raised words and low labels retain their physical relation to the main writing.',places='contr.; p/n labels; on; bord; des; strict-like insertion',consistent='Separate insertion leaders/height shifts distinguish placement.',witness_errors='H omits several annotations; C places p/n after a later d prime.'),
 dict(habit='Thin foliation ink should not automatically be attributed to the main writer.',places='Bottom 38 versus top 15',consistent='Distinct stroke weight and tone within this sheet.',witness_errors='H omits 38; no hand-attribution error asserted.')]

# Audit boxes contain only literal transcription, with complete doubtful formulas.
def audit(crop,kind,reading,reason):
    R['second_boxes'].append(dict(box='',kind=kind,coords=boxes[crop],reading=reading,reason=reason))
audit('page15','handwritten number',r'\mspage{15}','Author foliation, both digits; H editorial note already accounts for it.')
audit('equisinguliere','struck passage | insertion',r'\deleted{\unsure{équisingulière}}\inserted{équisingulière}','Canceled doubtful word and complete raised replacement.')
audit('ens_order','C/H word difference | low-confidence departure',r'\(I\) ens. ordonne','H extra un and both witnesses’ supplied acute; physical edge limitation.')
audit('presentation','C/H word difference','présentation standart.','Actual final t versus normalized d.')
audit('donnee','C/H word difference | low-confidence departure',r'On suppose \unsure{donné|donnée} une','Witness difference remains unresolved, without grammar completion.')
audit('category','struck passage | C/H word difference | low-confidence departure',r'\shortstack[l]{\unsure{ca}tégorie\\[-.2ex]\deleted{\illegible{1}}}','Initial overtrace state and separate lower cancellation; no invented repeated complete word.')
audit('moderee','C/H word difference','topologique modérée','Low r establishes modérée against modèle.')
audit('en_sens','C/H word difference | low-confidence departure','en un sens non','Resolved en and different source phrase.')
audit('precise_ca','C/H word difference | low-confidence departure','précisé, pour que ça puisse être aussi celle des','Continuation of competing phrase and ça/ce difference.')
ms=T[T.index('\\margin{\\(^*\\)'):T.index('\n\n\\deleted{(2)}')]
audit('margin_star','margin note | insertion | struck passage | doubt formula | C/H word difference | low-confidence departure',ms,'Entire asterisk note, including full d-prime relation, max i_p expression, final Sigma formula, every uncertain word, cancellation and raised insertion.')
audit('star_order_words','insertion | C/H word difference | low-confidence departure',r'\(i\in I\) \unsure{fort\(^{t}\)} \uline{\unsure{plus grands|supérieurs}}\inserted{\unsure{strict}}','Additional permitted detail for the still-unsettled order wording and newly identified raised insertion.')
audit('contr','insertion | C/H word difference',r'par un \inserted{contr.} foncteur','Raised abbreviation omitted by H.')
audit('functor','handwritten number',r'\begin{aligned}\Sigma:\ \operatorname{Drap}(I)&\longrightarrow\mathcal M\\(i_0,\ldots i_n)&\longmapsto\Sigma_{i_0\ldots i_n}\end{aligned}','Whole two-row map, including both written zero indices and punctuation.')
audit('one_intro','handwritten number | struck passage | C/H word difference | low-confidence departure',r"(1) Le\unsure{'} \deleted{\unsure{app}} morphisme",'Number 1, canceled word, singular/plural disagreement and detached tick.')
audit('one_map','handwritten number',r'\Sigma_{i_0\ldots i_n}\longrightarrow\Sigma_{i_0,\ldots i_p}','Complete formula, both zero indices and target punctuation.')
audit('margin_nb','margin note | insertion | C/H word difference | low-confidence departure',r'NB \inserted{on} ne poser cette condition que dans le cas équisingulier','Full NB note, inserted on, resolved ne poser, missing/misread H words and absent terminal stop.')
audit('one_d','insertion | struck passage | doubt formula | low-confidence departure',r"\underset{\inserted{p}}{d_{\deleted{\unsure{?}}}}\hookrightarrow\underset{\inserted{n}}{d'}",'Whole inclusion formula, both low labels and opaque canceled symbol; editorial ? meaning explained in metadata.')
audit('relatif','C/H word difference','relatif : une inclusion de drapeaux','Singular relatif and actual colon against both witnesses.')
audit('fibrant','C/H word difference | low-confidence departure',r'est \uline{fibrant}\(^*\)','Singular text, underline, asterisk and right-edge punctuation.')
audit('enfin','handwritten number | struck passage',r'\deleted{(2)} (\deleted{\unsure{Enfin}}','Canceled number 2 and separately canceled doubtful word.')
audit('suffit_map','handwritten number',r'\Sigma_{i_0\ldots i_n}\longrightarrow\Sigma_{i_0\ldots i_{n-1}}\quad)','Whole formula including zero indices, n−1, and closing parenthesis.')
audit('two_intro','handwritten number | C/H word difference','(2) Le morphisme','Live number 2 and singular wording.')
audit('two_map','struck passage | doubt formula | handwritten number',R['changes'][next(i for i,x in enumerate(R['changes']) if x['place']=='condition 2 / placement of replaced map')]['final'],'Entire replacement and canceled formula, zero indices, hat, and oval p≠n annotation.')
lm=T[T.index('\\margin{On va supposer'):T.index('\n\n\\uline{Cor.}')]
audit('margin_lower','margin note | insertion | struck passage | handwritten number | C/H word difference | low-confidence departure',lm,'Full lower note, canceled family, inserted des, number 2 and all retained/resolved doubts.')
audit('plongement','C/H word difference','est un plongement-bord','Singular formulation against H plural.')
audit('plongement_insert','insertion | C/H word difference | low-confidence departure',r"\inserted{i.e plongement \inserted{\unsure{bord}} cylindrique} (NB si \(p=n\), c'est un",'Complete inserted explanation, nested raised bord, abbreviation punctuation and adjacent full equality formula.')
audit('nb_fibrant','C/H word difference | low-confidence departure',r'morphisme fibrant\unsure{.|:})','Ordinary morphisme baseline and unresolved terminal dot count.')
audit('cor_arrow','doubt formula | C/H word difference',r"\uline{Cor.} Soit \(d\hookrightarrow d'\) tel que \(d\) et \(d'\) aient \(=\)",'Complete inclusion relation and written equals sign, both formerly doubtful.')
audit('cor_objects','C/H word difference',r'\unsure{objt maximals}, alors','Retained abbreviated doubtful phrase against H illegibility.')
audit('cor_map','doubt formula',r"\(\Sigma_{d'}\longrightarrow\Sigma_d\) est un plongement.",'Whole final map inspected for prime and terminal stop; neighboring Cor phrase remains doubtful, map itself is clear.')
audit('canceled_three','struck passage | handwritten number',r'\deleted{\unsure{(3)}}','Complete canceled number and its two parentheses.')
audit('folio38','margin note | handwritten number',r'\margin{38}','Both digits and uncertain hand attribution.')
R['second_boxes'].sort(key=lambda x:(x['coords'][1],x['coords'][0]))
for i,x in enumerate(R['second_boxes'],1): x['box']=f'b{i:02}'

# Every quoted source is checked without pretending typography-only differences are findings.
norm=lambda s:re.sub(r'\s+',' ',s).strip()
for x in R['changes']:
    assert x['final'] in T,('final missing',x['place'],x['final'])
    for witness,src in [('C',C),('H',H)]:
        assert x[witness]=='[absent]' or norm(x[witness]) in norm(src),(witness,x['place'],x[witness])
    assert (W/'crops'/x['crop']).exists()
for crop in boxes: assert (W/'crops'/f'150_scan039_{crop}.jpg').exists()
for x in R['marks']: assert (W/'crops'/x['crop']).exists()
assert len(R['marks'])==len(cm)
depth=0
for i,ch in enumerate(T):
    if ch=='{' and (i==0 or T[i-1]!='\\'): depth+=1
    elif ch=='}' and (i==0 or T[i-1]!='\\'): depth-=1
    assert depth>=0,('brace underflow',i)
assert depth==0,depth
assert T.count('$')%2==0
out=W/'reader_returns/150_scan039.json'
out.write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'output':str(out),'changes':len(R['changes']),'C_marks':len(R['marks']),
 'inventory':len(R['inventory']),'audit_boxes':len(R['second_boxes']),'crops_viewed':len(boxes),
 'check_events':len(R['check_events']),'validation':'source quotes, final snippets, crop existence, braces and dollars passed'},ensure_ascii=False))
