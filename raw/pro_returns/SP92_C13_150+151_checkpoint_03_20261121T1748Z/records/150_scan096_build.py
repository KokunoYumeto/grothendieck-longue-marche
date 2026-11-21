from pathlib import Path
import json

BASE = Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
PACKET = json.loads(Path('/workspace/scratch/d7279cb02214/reading_packets/150_scan096/packet.json').read_text())
C, H = PACKET['witness_C'], PACKET['witness_H']
CM = json.loads((BASE/'records/150_scan096_cropmap.json').read_text())

# Candidate variables retain precisely scoped uncertainty while the visible marks are reviewed.
EDGE1 = r'incomparab\unsure{l}'
EDGE2 = "d'introduir"
BORNE = r'\unsure{borne|bornera}'
OPENING = r'\unsure{(}'
LIMIT = r'$\varinjlim$'
MARGIN = r"\margin{$^*$(et des protopos homotopes $\mathcal V_{i_0,\mathord{-}i_n}^{Z}$ plus bas)}"

TEX = r'''\scanpage{96}

en faisant attention que pour $i$ et $j$ EDGE1 et $X$ metrisable, on \deleted{\unsure{trouve}} aura $\mathcal V_{ij}=\phi$ \deleted{et} (donc pas la peine d'en parler!), et pour $i=j$, on aura $\mathcal V_{ij}=\mathcal V_{ii}=\mathcal V_i$ (donc pas la peine de l'introduire, $\mathcal V_i$ suffit!), enfin \deleted{\unsure{et}} si $i$ et $j$ sont distincts et comparables, \deleted{\unsure{d|donc}} comme $\mathcal V_{ij}=\mathcal V_{ji}$, il suffit EDGE2 $\mathcal V_{ij}$ pour \deleted{\unsure{les}} $i<j$. Plus généralement, on introduit les
\[(98)\qquad\mathcal V_{i_0\mathord{-}i_n}=\mathcal V_{i_0}\cap\mathord{-}\mathord{-}\cap\mathcal V_{i_n},\]
mais on se BORNE en règle générale au cas où $\{i_0,\mathord{-},i_n\}$ est un drapeau (sinon on trouve $\phi$\} et où en fait ils sont rangés en ordre str. croissant
\[i_0<i_1<\mathord{-}\mathord{-}<i_n\]
OPENINGpour éviter des redondances). Les protopos $^*$ sont les ``pierres de construction'' élémentaires, pour en construire des tas d'autres, par LIMIT (finies si $I$ fini), compte tenu des morphismes semi-simpliciaux évidents entre les $\mathcal V_d$ $(d=(i_0,\mathord{-},i_n)\in\mathrm{Drap}(I))$.
MARGIN
\margin{95}
'''
for key in ('EDGE1','EDGE2','BORNE','OPENING','LIMIT','MARGIN'):
    TEX=TEX.replace(key,globals()[key])

changes=[]
def add(place,c,h,final,evidence,crop,kind,error_kind,ac=False,ah=True,confidence='high',consequential=False,marked=False,change_type=None):
    assert not c or c in C, ('C snippet',c)
    assert h is not None and (not h or h in H), ('H snippet',h)
    x={'id':f'C{len(changes)+1:02d}','place':place,'C':c,'H':h,'final':final,'evidence':evidence,'crop':CM[crop]['crop'],'box':CM[crop]['box'],'confidence':confidence,'kind':kind,'error_kind':error_kind,'against_C':ac,'against_H':ah,'consequential':consequential,'marked_in_H':marked}
    if change_type: x['change_type']=change_type
    changes.append(x)
    return x['id']

ids={}
ids['edge1']=add('Opening line, physical right edge','incomparables','incomparables',EDGE1,'The final b/l group reaches the black paper boundary. No separately visible final e or s survives beyond it; the terminal l remains narrowly uncertain. The full agreed word is not completed from grammar.','incomparables_edge','text not on the page','9 not on page',ac=True,confidence='medium')
ids['et']=add('Opening of second line','et $X$',', si $X$','et $X$','A small connected e is followed by the short upright and cross-stroke of t. There is no s-i sequence or preceding comma at this line opening.','et_metrisable','misread word','2 words')
ids['metric']=add('Condition on X','métrisable','unibranche','metrisable','The word has initial m, low e, tall crossed t, r, dotted i, then sable with tall b/l. No detached acute stroke is visible over the first e. The sequence is not unibranche.','et_metrisable','abbreviation expanded or spelling modernised','8 abbreviation/spelling',ac=True,consequential=True)
ids['trouve_state']=add('Revision between on and aura',r'\deleted{\unsure{trouve}}',r'trouve \struck{\ill{}}',r'\deleted{\unsure{trouve}}','One word-sized group is crossed by a strong horizontal deletion stroke; the initial t is visible but the interior is obscured. There is no separate live trouve followed by a second canceled word. The uncertain old reading is retained without resolving its concealed letters.','first_revision','deletion state (struck given live or live given struck)','7 struck state',marked=True)
ids['aura1']=add('Live replacement after first cancellation','aura','donc','aura','The live word to the right is a low a-u-r-a sequence, with no tall d or terminal c. It is separate from the horizontal cancellation.','first_revision','misread word','2 words')
ids['phi1']=add('First empty-set sign',r'\mathcal V_{ij}=\varnothing',r'\mathcal V_{ij}=\emptyset',r'\mathcal V_{ij}=\phi','A small loop is traversed by a long axial stroke extending well below the loop, the same phi-shaped empty sign as the lower occurrence.','empty_and_et','misread symbol or index','1 symbols/indices',ac=True)
ids['et_resolved']=add('Canceled word after first phi',r'\deleted{\unsure{et}}',r'\ill{} (dans',r'\deleted{et}','The left e loop and the right upright of t remain distinct under a single horizontal cancellation. The word is struck, rather than live illegible text, and its two letters can be read.','empty_and_et','deletion state (struck given live or live given struck)','7 struck state',ac=True,marked=True,change_type='doubt resolution')
ids['paren1']=add('First parenthetical comment',"donc pas la peine d'en parler",r"dans \uncertain{par là} \uncertain{fixés} d'un \uncertain{coup}","donc pas la peine d'en parler",'The opening d is followed by o-n-c; pas has final s, then separate la. Peine begins with a descender and has dotted i; the following apostrophe group is d’en, followed by p-a-r-l-e-r. The exclamation mark and closing parenthesis are live.','parenthesis1','misread word','2 words',marked=True)
ids['aura2']=add('Case i=j, live verb','on aura','on trouve','on aura','After on, the four low letters repeat the first aura; there is no t ascender or trouve-length group.','aura_and_parenthesis2','misread word','2 words')
ids['paren2a']=add('Second parenthetical opening','(donc pas la',r'(dans \uncertain{par là}','(donc pas la','The opening word ends in angular c, followed by a separate pas and la. Their division matches the first parenthetical comment.','aura_and_parenthesis2','misread word','2 words',marked=True)
ids['paren2b']=add('Second parenthetical, beginning of following line','peine',r'\uncertain{besoin}','peine','The first letter descends as p; the small i has its dot, followed by n-e. There is no initial b ascender or final besoin sequence.','peine_suffix','misread word','2 words',marked=True)
ids['old_d']=add('Canceled start immediately before comme',r'\deleted{\unsure{donc}}',r'comparables, \struck{\ill{}} comme',r'\deleted{\unsure{d|donc}}','The old mark is a compact tall loop with a small basal return, crossed out before the separate live comme. It visibly supports d; distinct o-n-c letters cannot be separated, so the fuller C proposal remains only an alternative.','donc_comme','misread word','2 words',ac=True,confidence='low',marked=True)
ids['edge2']=add('End of line containing il suffit',"d'introduire", "d'introduire",EDGE2,'The final written return meets the black edge. The surviving d’introduir sequence is retained; an additional final e is not supplied beyond the physical boundary.','introduire_edge','text not on the page','9 not on page',ac=True,confidence='medium')
ids['f98_index']=add('Formula (98), left multi-index',r'i_0\ldots i_n',r'i_0\ldots i_n',r'i_0\mathord{-}i_n','Between the first and last index groups there is one continuous horizontal continuation stroke, not three dots. Both endpoint i letters have dots; the first numerical subscript is a closed 0.','formula98','misread symbol or index','1 symbols/indices',ac=True)
ids['f98_middle']=add('Formula (98), between intersection signs',r'\cap\cdots\cap',r'\cap\cdots\cap',r'\cap\mathord{-}\mathord{-}\cap','Between the two cap signs there are exactly two separated short horizontal continuation strokes. The full display, including (98), both endpoint indices and final comma, was read together.','formula98','misread symbol or index','1 symbols/indices',ac=True)
ids['set_rule']=add('Set of indices before drapeau',r'\{i_0,\ldots,i_n\}',r'\lbrace i_0,\ldots,i_n\rbrace',r'\{i_0,\mathord{-},i_n\}','The set has a comma after i_0, one horizontal continuation rule, a second comma, and i_n. Its outer left and right braces remain as written.','flag_passage','misread symbol or index','1 symbols/indices',ac=True)
ids['phi2']=add('Lower empty-set sign',r'\varnothing',r'\emptyset',r'\phi','The small loop has a long diagonal axial stem with a descending extension. It matches the first phi-shaped empty sign; it is not reduced to the conventional empty-set macro. This row concerns only the glyph, not the following delimiter.','empty2','misread symbol or index','1 symbols/indices',ac=True)
ids['brace']=add('Closing delimiter after lower phi',')',')',r'\}','The closer has a hooked upper turn, a near-vertical middle with a bend, and a leftward lower return, agreeing with a right curly brace. The opening delimiter before sinon remains a parenthesis; their mismatch is preserved. This row concerns the delimiter alone; the preceding phi glyph is recorded separately.','empty2','misread symbol or index','1 symbols/indices',ac=True)
ids['en_fait']=add('Phrase after et où','en fait','on fait','en fait','The first word is an open initial e running into n, rather than an o loop. The tall f and dotted i of fait follow separately.','en_fait_ranges','misread word','2 words')
ids['ranges']=add('Phrase before en ordre','ils sont rangés',r'\uncertain{les indices} à \uncertain{jamais}','ils sont rangés','A dotted i and tall l begin ils; a separate compressed s-o-n-t precedes r-a-n-g-é-s, whose g descender and accent are distinct. No indices-length group or separate à occurs.','en_fait_ranges','misread word','2 words',marked=True)
ids['order_rule']=add('Increasing-index display',r'i_0<i_1<\cdots<i_n',r'i_0<i_1<\cdots<i_n',r'i_0<i_1<\mathord{-}\mathord{-}<i_n','The continuation comprises two separated short horizontal strokes. The inequality signs are angular open chevrons; the first two subscripts are 0 and 1, followed by n.','order_chain','misread symbol or index','1 symbols/indices',ac=True)
ids['protopos']=add('Main text, starred technical noun','protopos','pro-espaces','protopos','The first p descends, followed by r-o, a tall t, o, a second descending p, o and terminal s. There is no hyphen or espaces group. The small raised star follows the noun.','protopos_main','misread word','2 words',consequential=True)
ids['pierres']=add('Quoted noun and opening quotation marks','``pierres','« pièces','``pierres','Two high upright quotation ticks precede p-i-e-r-r-e-s; the doubled reduced r group is visible after the dotted i and e. No c loop occurs in that position.','pierres_construction','misread word','2 words')
ids['close_quotes']=add('Closing quotation marks after construction',"construction''",'construction »',"construction''",'Two separate high ticks follow construction. No paired angular guillemet is drawn.','pierres_construction','misread symbol or index','1 symbols/indices')
ids['construire']=add('After élémentaires, pour','en construire','une construction','en construire','A small two-letter en precedes construire, with its dotted i and final r-e return. There is no initial u in the first word or terminal t-i-o-n group in the infinitive.','en_construire_tas','misread word','2 words')
ids['tas']=add('Objects to be constructed',"tas d'autres",r"\uncertain{types} d'homotopie","tas d'autres",'The short noun has tall t followed by a and terminal s. After the clear d and apostrophe, the remaining low a-u, crossed t, r-e-s sequence reads autres; no homotopie-length group is present.','en_construire_tas','misread word','2 words',marked=True)
ids['limit']=add('Limit sign before finies si I fini',r'\uline{$\lim$}',r'$\varinjlim$',r'$\varinjlim$','The rule below lim terminates in a short down-and-back leg at its right endpoint, giving a right arrow rather than a simple underline. The small head is visible in the tip crop; the complete expression was reread separately.','limit_tip','misread symbol or index','1 symbols/indices',ac=True,ah=False,confidence='medium',consequential=True)
ids['final_rule']=add('Final parenthetic definition of d',r'd=(i_0,\ldots,i_n)\in\mathrm{Drap}(I)',r'd=(i_0,\ldots,i_n)\in\mathrm{Drap}(I)',r'd=(i_0,\mathord{-},i_n)\in\mathrm{Drap}(I)','Between the two endpoint indices is one horizontal continuation stroke with a comma on each side. The entire d=(...) membership formula, including Drap(I), was inspected together.','final_formula','misread symbol or index','1 symbols/indices',ac=True)
ids['des']=add('Slanted marginal note, word after et',r'\unsure{des|les}',r'de \uncertain{tels}','des','The initial character has a closed basal loop and an ascending looped stroke, the form of d. A small e and final s follow before the p of protopos; there is no separate tels group.','margin','misread word','2 words',ac=True,marked=True,change_type='doubt resolution')
ids['margin_words']=add('Slanted marginal technical phrase','protopos homotopes',r'pro-\uncertain{espaces}','protopos homotopes','The first line repeats the main-text protopos with two descending p forms and a tall t. The second line begins h and continues the compressed o-m-o-t-o-p-e-s sequence; its final p descender and s turn remain visible.','margin','misread word','2 words',marked=True,consequential=True)
ids['margin_rule']=add('Marginal V multi-index',r'i_0,\ldots,i_n',r'i_0,\ldots,i_n',r'i_0,\mathord{-}i_n','The marginal index has i_0, one comma below, then a single short horizontal rule and i_n. No second comma is visible between the rule and the second i.','margin_math','misread symbol or index','1 symbols/indices',ac=True)
ids['margin_Z']=add('Marginal exponent and final words',r'^{Z}$ plus bas',r'$ \ill{} \ill{} \ill{}',r'^{Z}$ plus bas','Above V’s right shoulder is an angular Z with upper and lower horizontal bars joined diagonally. The following line has plus, then a looped b and a-s, closed by a parenthesis. These marks are live.','margin','readable ink left as \\ill{}','5 readable left illegible',marked=True,consequential=True)
ids['folio']=add('Lower-left thin foliation',r'\margin{95}','','95','The fine grey figures are a looped 9 with long descending leg and a 5 with upper bar, distinct from the author’s brown main hand. H has no transcription of this foliation.','folio95','omission','3 omissions')

diff_coverage=[]
mapping={
'D0691':('editorial-only',[],'C’s scan marker and H’s editorial attribution/continuation note are not source wording. No authorial number is visible.'),
'D0692':('reading',[ids['et']],'The source has et, without the comma and si supplied by H.'),
'D0693':('reading',[ids['metric']],'The lexical reading is metrisable; its absent acute also differs from C.'),
'D0694':('reading',[ids['trouve_state'],ids['aura1']],'The alignment crosses a canceled word and its live replacement; both state and live verb are recorded.'),
'D0695':('reading',[ids['et_resolved']],'The crossed et is legible; H leaves an unstruck illegibility marker.'),
'D0696':('reading',[ids['paren1']],'The entire parenthetical wording was read; H’s final \\, is spacing, not a source comma.'),
'D0697':('reading',[ids['aura2']],'The live verb after i=j is aura.'),
'D0698':('reading',[ids['paren2a'],ids['paren2b']],'The differing phrase spans two manuscript lines, each cropped.'),
'D0699':('macro-only',[],'The apparent comma is the comma token of H’s \\, spacing command; there is no different punctuation reading.'),
'D0700':('reading',[],'The cancellation after enfin is real, but its letters remain obscured; C’s narrow uncertain et is retained and not counted as a settled correction.'),
'D0701':('reading',[ids['old_d']],'The compact canceled start favors d; the fuller donc remains an uncertain alternative.'),
'D0702':('reading',[],'The canceled word before i<j remains narrowly unsure as les. Its scope is recorded, but the obscured interior is not claimed as a resolved H error.'),
'D0703':('reading',[],'The compressed ending is retained as an unresolved borne/bornera reading pending the blind reread.'),
'D0704':('reading',[ids['en_fait']],'The first word of en fait has an open e form.'),
'D0705':('reading',[ids['ranges']],'The source has ils sont rangés.'),
'D0706':('reading',[],'The putative opening parenthesis meets the slanted marginal descender; a narrow uncertainty is retained without a settled correction.'),
'D0707':('reading',[ids['protopos']],'The written technical noun is protopos.'),
'D0708':('reading',[ids['pierres']],'Both the opening ticks and noun were read on the crop.'),
'D0709':('reading',[ids['close_quotes']],'Two high ticks close the quotation.'),
'D0710':('reading',[ids['construire']],'The source has en construire.'),
'D0711':('reading',[ids['tas']],'The source has tas d’autres.'),
'D0712':('editorial-only',[],'H’s note about the repeated formula number and its reading difficulty is editorial. Source number (98) is preserved without renumbering.'),
'D0713':('reading',[ids['des'],ids['margin_words']],'The marginal mark and both technical words are recorded with the slanted note crop.'),
'D0714':('reading',[ids['margin_Z']],'The exponent Z and plus bas are visible where H has illegibility markers.'),
'D0715':('reading',[ids['folio']],'The alignment juxtaposes C’s source foliation with H’s editorial marginal-note description. The source 95 is omitted by H; the editorial description is excluded.'),
}
for d in PACKET['differences']:
    cls,cids,reason=mapping[d['diff_id']]
    diff_coverage.append({'diff_id':d['diff_id'],'classification':cls,'change_ids':cids,'reason':reason})

decisions=[{'id':'M0725','cote':'150','scan':'96','decision':'first','reading':'des','ink':'The initial d has a closed basal loop with a rising looped stroke, followed by reduced e and a terminal s before protopos; this is not the plain l initial.','crop':CM['margin']['crop'],'box':CM['margin']['box'],'confidence':'high'}]

inventory=[]
def inv(element,kind,position,words,hand='author, brown ink'):
    inventory.append({'sheet_kind':'text','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('Opening continuation and incomparable-index case','text','Upper body, first three baselines','en faisant attention que pour i et j incomparab…')
inv('First canceled verb','deletion','Second baseline, between on and aura','trouve (uncertain), crossed once horizontally')
inv('Live replacement verb','text','Second baseline, immediately after cancellation','aura')
inv('First phi formula','display','Second baseline, inline at right','V_ij = phi')
inv('Canceled et after phi','deletion','Second baseline, right of first phi','et')
inv('First parenthetical note','text','Third baseline','(donc pas la peine d’en parler!),')
inv('Equal-index case and second parenthetical','text','Third through fifth baselines','et pour i=j, on aura …')
inv('Finally, distinct comparable case','text','Sixth through ninth baselines','enfin … si i et j sont distincts et comparables, …')
inv('Canceled et after enfin','deletion','Beginning of sixth baseline','et (uncertain)')
inv('Canceled old start before comme','deletion','Beginning of seventh baseline','d | donc (uncertain)')
inv('Canceled word before i<j','deletion','Eighth baseline, after pour','les (uncertain)')
inv('Intersection definition (98)','display','Middle page, isolated baseline','(98) V_i0–in = V_i0 cap – – cap V_in,')
inv('Flag restriction','text','Below (98), three baselines','mais on se borne|bornera …')
inv('Index set','display','Inline in flag restriction','{i_0, –, i_n}')
inv('Parenthetical empty case','text','Within flag restriction, across two baselines','(sinon on trouve phi}')
inv('Strict increasing-order phrase','text','Immediately above order chain','en ordre str. croissant')
inv('Increasing-index chain','display','Lower middle, isolated baseline','i_0 < i_1 < – – < i_n')
inv('Redundancy comment and starred noun','text','Immediately beneath chain','(uncertain opening) pour éviter des redondances). Les protopos *')
inv('Construction paragraph','text','Last five main baselines','sont les ``pierres de construction’’ élémentaires, …')
inv('Limit expression','display','Inline near foot, before finies si I fini','lim with rightward lower rule and small terminal hook')
inv('Final simplex/flag-index formula','display','Last main baseline','V_d (d=(i_0, –, i_n) in Drap(I)).')
inv('Starred diagonal marginal addition','margin note','Left margin, slanting upward right beside final paragraph','*(et des protopos homotopes V_i0,–in^Z plus bas)')
inv('Thin lower foliation','margin note','Lower-left foot, below all authorial text','95','another hand, thin grey foliation')

second_boxes=[]
def blind(kind,box,reading):
    assert reading in TEX, ('blind text outside candidate',reading)
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,'x0':box[0],'y0':box[1],'x1':box[2],'y1':box[3],'reading':reading})
blind('different word; clipped edge',[1397,76,1683,173],EDGE1)
blind('different words; unaccented spelling',[310,161,738,258],r'et $X$ metrisable,')
blind('cancellation; live replacement',[756,166,1158,246],r'\deleted{\unsure{trouve}} aura')
blind('whole formula; cancellation',[1195,137,1559,245],r'$\mathcal V_{ij}=\phi$ \deleted{et}')
blind('different words; parenthetical',[318,253,1290,370],r"(donc pas la peine d'en parler!),")
blind('different words; complete inline formula',[324,328,1639,444],r'on aura $\mathcal V_{ij}=\mathcal V_{ii}=\mathcal V_i$ (donc pas la')
blind('different word; parenthetical continuation',[310,421,1627,555],r"peine de l'introduire, $\mathcal V_i$ suffit!), enfin")
blind('cancellation',[313,575,449,675],r'\deleted{\unsure{et}}')
blind('cancellation; uncertain old start',[334,688,559,759],r'\deleted{\unsure{d|donc}} comme')
blind('clipped edge',[1390,620,1683,696],EDGE2)
blind('cancellation',[691,765,791,845],r'\deleted{\unsure{les}}')
blind('formula number; complete displayed formula; mathematical digits',[309,992,1388,1133],r'\[(98)\qquad\mathcal V_{i_0\mathord{-}i_n}=\mathcal V_{i_0}\cap\mathord{-}\mathord{-}\cap\mathcal V_{i_n},\]')
blind('different word; compressed ending',[709,1138,946,1225],BORNE)
blind('whole formula; mathematical digits; different words; mismatched delimiter',[305,1216,1649,1442],r'cas où $\{i_0,\mathord{-},i_n\}$ est un drapeau (sinon on trouve $\phi$\} et où en fait ils sont rangés')
blind('complete displayed chain; mathematical digits; abbreviation',[310,1444,1155,1595],r'en ordre str. croissant'+'\n'+r'\[i_0<i_1<\mathord{-}\mathord{-}<i_n\]')
blind('uncertain punctuation; marginal overlap',[288,1625,1201,1744],OPENING+'pour éviter des redondances).')
blind('different technical word; marginal call',[1231,1586,1629,1677],r'Les protopos $^*$')
blind('different word; quotation marks',[609,1702,1276,1818],"``pierres de construction''")
blind('different words',[292,1778,1438,1931],"pour en construire des tas d'autres,")
blind('whole limit expression; below-high-confidence change',[293,1885,995,2027],LIMIT+r' (finies si $I$ fini)')
blind('whole final formula; mathematical digits',[291,2075,1321,2185],r'les $\mathcal V_d$ $(d=(i_0,\mathord{-},i_n)\in\mathrm{Drap}(I))$.')
blind('margin note; resolved C mark; complete formula; mathematical digit',[20,1630,376,2038],MARGIN)
blind('other-hand handwritten foliation',[24,2300,94,2347],r'\margin{95}')

doubts=[
 {'place':'Canceled verb before first aura','reading':'trouve','alternatives':[],'confidence':'low','reason':'A strong horizontal strike obscures the interior letters. The C proposal is retained under uncertainty; only the cancellation state is settled.'},
 {'place':'Canceled word after enfin','reading':'et','alternatives':[],'confidence':'low','reason':'The small looped group is crossed repeatedly. Its two-letter C proposal is plausible, but every letter is not independently clear.'},
 {'place':'Canceled old start before comme','reading':'d','alternatives':['donc'],'confidence':'low','reason':'A compact tall loop and basal turn support d; the strike prevents secure exclusion of a fuller old word, but separate onc is not visible.'},
 {'place':'Canceled word before i<j','reading':'les','alternatives':[],'confidence':'low','reason':'The l-like loop and final s-like turn survive, while the middle is crossed and not securely resolved.'},
 {'place':'Opening line at right paper edge','reading':EDGE1,'alternatives':['incomparab'],'confidence':'medium','reason':'The end of the b/l group meets the paper boundary. Final es is absent from the surviving image and is not completed.'},
 {'place':'End of line containing il suffit','reading':EDGE2,'alternatives':[],'confidence':'medium','reason':'The word’s terminal return reaches the black edge; no final e is supplied outside the surviving writing.'},
 {'place':'Verb after mais on se','reading':'borne','alternatives':['bornera'],'confidence':'medium','reason':'The short ending has compressed turns that do not yet securely separate the two witnesses.'},
 {'place':'Before pour éviter','reading':'(','alternatives':['no independent opening parenthesis'],'confidence':'low','reason':'The long curved stroke overlaps the descending final p from the slanted marginal protopos; its status as a separate main-text delimiter remains uncertain.'},
]

notes=r'''# Scan 96 — reader A, SP92

## Content and scope
The page continues a sentence about the objects V indexed by pairs. It treats incomparable indices with X written **metrisable**, equal indices, and distinct comparable indices; then it gives an intersection definition labeled **(98)** and restricts the indices to a flag ordered strictly increasingly. The last paragraph calls the protopos “pierres de construction” and speaks of forming others through a limit expression with the written qualification “finies si I fini”. Its final indexing formula uses Drap(I). A starred, diagonal marginal addition refers to homotopic protopos V with superscript Z “plus bas”. These are descriptions of the page’s claims, not verified results.

## Source lettering and boundaries
The page has no authorial title, date or page number at its head. The thin grey **95** at the lower left belongs to another hand and is preserved as a margin item, not as an authorial mspage. The candidate’s scan marker is editorial. H’s introductory note, repeated-number comment and description of the marginal note are editorial and excluded. No numbering sequence was repaired: the written display label remains (98).

The right paper edge clips the opening word’s final b/l group and the final return of d’introduir. Their full shared witness spellings are not completed beyond the visible ink. These areas remain in the blind reread set. The acute accent supplied by C in métrisable is absent from the enlarged source; metrisable is retained. The literal short form str. keeps its visible stop. The quotation is enclosed by two high ticks on each side, not French guillemets.

## Revisions and attachment
There are five canceled groups in the main text: the old verb between on and aura; et immediately after the first phi; a small uncertain et after enfin; a compact old d/donc before the live comme; and the uncertain les before i<j. The first canceled group is not a live trouve followed by a second deletion as H parses it. Both live aura readings are independent of those strikes. Only the et after the first phi is resolved: its e loop and t upright survive the single strike. The other obscured groups remain narrowly uncertain. No strike extends into the following formula or live replacement.

The star after the main-text protopos calls the diagonal left-margin note. The note is live throughout and its opening and closing parentheses are preserved. Its text is not inserted into a different sentence. The marginal final p’s descending stroke approaches the main-text opening before pour éviter; the status of an independent opening parenthesis remains uncertain and has its own blind box. The closer after the lower phi is visibly a right curly brace although the opener before sinon is a parenthesis; this mismatch is retained.

## Mathematical rereading triggered by the witnesses or small signs
Both empty signs were reread with their surrounding formulas: each is a small loop traversed by a long axial descending stroke, transcribed as phi. The diagonal sign is not silently converted to the witnesses’ standard empty-set glyphs. Their meaning here is the empty case described by the sentence.

The entire (98) display was reread. Its first index has a closed 0; the left continuation is one horizontal rule, while the continuation between the two intersection signs comprises two separated short rules. The displayed increasing chain likewise has two short continuation rules, and its numerical subscripts are 0 and 1. The set of indices, the final definition of d, and the marginal V subscript were each read as complete expressions. The first two have one continuation rule between written commas. The marginal index has only the comma after i_0, then one rule and i_n, with no second comma. These literal marks are represented by mathord minus strokes rather than normalized three-dot ellipses; the notation does not claim subtraction.

The limit sign was reread in its full phrase and in a tip detail because C gives an underline and H a direct-limit arrow. The short terminal backward/downward leg supports a right arrow at medium confidence; the candidate uses varinjlim. No categorical claim was inferred to decide the ink. The whole expression remains in the blind reread set. The complete final V_d / d=(...) membership formula and the marginal V^Z formula were inspected, including their indices, commas, parentheses and exponent.

No proof check, computation or mathematical use was performed by reader A; check_events is empty. Root’s separate checks, if any, are not attributed here.
'''

record={
'page':'150_scan096','cote':'150','scan':'96','reader':'reader_a — GPT-6 Astra Pro; effort not exposed; run SP92',
'line_count':25,
'line_count_note':'21 main manuscript baselines including the (98) display and the increasing-index display; three slanted marginal baselines; one lower foliation baseline. Canceled groups on a main baseline are not counted again.',
'half_review':'Original whole page inspected once for layout, then both supplied native overlapping halves once. Every main-text word, agreed reading, inline/display formula, number, accent, punctuation mark, deletion and margin item was read against C and H. Twenty-nine current saved crops were inspected, including the four additional details and the final reframings. No OCR, external research or TeX compilation.',
'deletion_insertion_review':[
 {'place':'Between on and first aura','C':r'\deleted{\unsure{trouve}}','state':'struck; one old word-sized group','bounds':'Only the old group is crossed; preceding on and following aura remain live.','reading':r'\deleted{\unsure{trouve}}','crop':CM['first_revision']['crop'],'box':CM['first_revision']['box']},
 {'place':'After first empty-set sign','C':r'\deleted{\unsure{et}}','state':'struck, resolved as et','bounds':'One e/t group at the end of the line; the next-line parenthetical remains live.','reading':r'\deleted{et}','crop':CM['empty_and_et']['crop'],'box':CM['empty_and_et']['box']},
 {'place':'After enfin','C':r'\deleted{\unsure{et}}','state':'struck, not resolved','bounds':'The small old group alone precedes live si; no cancellation of enfin or si.','reading':r'\deleted{\unsure{et}}','crop':CM['enfin_struck']['crop'],'box':CM['enfin_struck']['box']},
 {'place':'Before comme','C':r'\deleted{\unsure{donc}}','state':'struck, first reading narrowed to d','bounds':'The compact old mark is separate from live comme and the following V formula.','reading':r'\deleted{\unsure{d|donc}}','crop':CM['donc_comme']['crop'],'box':CM['donc_comme']['box']},
 {'place':'After pour before i<j','C':r'\deleted{\unsure{les}}','state':'struck, not resolved','bounds':'Only the short word between pour and i<j is canceled; the inequality remains live.','reading':r'\deleted{\unsure{les}}','crop':CM['les_struck']['crop'],'box':CM['les_struck']['box']},
 {'place':'Diagonal marginal addition','C':r'\margin{...}','state':'live marginal addition; star attachment','bounds':'The raised star after main-text protopos corresponds to the marginal star; three slanted lines enclosed by parentheses are all live. No ordinary insertion macro occurs in C.','reading':MARGIN,'crop':CM['margin']['crop'],'box':CM['margin']['box']},
],
'changes':changes,'diff_coverage':diff_coverage,'decisions':decisions,'inventory':inventory,'notes':notes,'check_events':[],
'notation':[
 {'sign':r'\phi','reading':'empty set, literal phi-shaped form','evidence':'Both empty cases show a small loop with a long axial descending stem; first and lower crops inspected.'},
 {'sign':'horizontal continuation rules','reading':'one or two literal horizontal strokes, retaining their local count','evidence':'One in formula (98)’s left index, the set, final d tuple and marginal index; two between intersection signs and in the increasing chain.'},
 {'sign':'str.','reading':'strictement (abbreviation retained)','evidence':'Small s, tall crossed t, reduced r and a distinct terminal stop before croissant.'},
 {'sign':'protopos','reading':'technical coined noun','evidence':'Repeated clearly in the starred main-text noun and diagonal marginal note, with two p descenders and t.'},
 {'sign':r'\varinjlim','reading':'lim with a rightward arrow below, medium confidence','evidence':'The right tip has a small backward/downward leg; the full expression and close detail were inspected without resolving by mathematical expectation.'},
 {'sign':'star after protopos','reading':'call to the diagonal marginal note','evidence':'The small raised main-text star has its matching marginal star before the parenthesis.'},
],
'hand_log':[
 {'habit':'Reduced word interiors can become nearly horizontal, while ascenders and i dots remain decisive.','places':'Both aura, metrisable, peine, en fait ils sont rangés, en construire, tas d’autres.','scope':'Repeated prose groups on this page; each was inspected separately.','witness_errors':'H’s donc/trouve, unibranche, besoin, les indices à jamais, une construction and types d’homotopie do not match the surviving strokes.'},
 {'habit':'The lower-case d may have a closed basal loop plus a large looped ascender resembling l.','places':'des in the diagonal note, M0725.','scope':'Settled locally using the basal loop; not applied indiscriminately to every looped letter.','witness_errors':'C des|les resolved to des; H de tels does not reflect the word division.'},
 {'habit':'Continuation is often indicated by one or two horizontal pen strokes instead of three dots.','places':'(98), index set, strict-order chain, final d tuple, marginal V index.','scope':'All five continuations on this page inspected and counted independently.','witness_errors':'Both witnesses normalize these to ldots/cdots; the marginal index also gains an unwritten second comma.'},
 {'habit':'Empty-set sign has a long phi-like axial stem.','places':'Two empty cases, upper and lower main text.','scope':'Both occurrences on this page.','witness_errors':'C varnothing and H emptyset replace the literal glyph.'},
 {'habit':'Two high quotation ticks are distinct from guillemets.','places':'pierres de construction.','scope':'Opening and closing pair on this page.','witness_errors':'H renders angular guillemets.'},
 {'habit':'Thin grey foliation differs from the author’s larger brown text.','places':'Lower-left 95.','scope':'This single lower foliation.','witness_errors':'H omits it; it is not an authorial page number.'},
],
'abbreviations':[{'form':'str.','expansion':'strictement'}],
'doubts':doubts,'second_boxes':second_boxes,
'crops':[{'name':name,**v,'viewed':True} for name,v in CM.items()],
}

allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in changes)
assert {x['diff_id'] for x in diff_coverage}=={x['diff_id'] for x in PACKET['differences']}
assert [x['id'] for x in decisions]==[x['id'] for x in PACKET['marks']]
assert all(x['id'] in {y['id'] for y in changes} for d in diff_coverage for x in [{'id':z} for z in d['change_ids']])
assert all((BASE/x['crop']).exists() for x in changes)
(BASE/'records/150_scan096.tex').write_text(TEX)
(BASE/'records/150_scan096.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'crops':len(CM),'diffs':len(diff_coverage),'marks':len(decisions),'blind_boxes':len(second_boxes),'doubts':len(doubts),'inventory':len(inventory)},ensure_ascii=False))
