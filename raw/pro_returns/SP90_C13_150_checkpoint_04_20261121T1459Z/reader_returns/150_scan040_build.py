from pathlib import Path
import json, re

BASE=Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACK=Path('/workspace/scratch/481648fc487b/reader_packets/150_scan040')
C=(PACK/'C.tex').read_text()
H=(PACK/'H.tex').read_text()
tex=C
replacements=[
 (r"\unsure{pour que l'on ait}", "pour que l'on ait"),
 (r"\unsure{signifie par|dit que pour les}", r"\unsure{dit que pour les|dit que par les}"),
 (r"\unsure{mono.}", "mono."),
 (r"\Sigma_{\unsure{d''|d'}}-\Sigma_d", r"\Sigma_{d''}-\Sigma_d"),
 ("est fibrant.}", "est fibrant}"),
 (r"\inserted{\unsure{sans plus}\(^*\)}", r"\inserted{sans plus\(^*\)}"),
 (r"\Sigma_{d''}\arrow[r,hook]\arrow[d]&\Sigma_{d'}\arrow[d]\\"+'\n'+r" \Sigma_d\arrow[r,hook]&\Sigma_i",
  r"\Sigma_{d''}\arrow[r,hook]\arrow[d]&\Sigma_{d'}\arrow[d]\arrow[r,hook]&{}\\"+'\n'+r" \Sigma_d\arrow[r,hook]&\Sigma_i&"),
 (r"\unsure{ce dernier|est}", "ce dernier"),
 ("i.e. réduit à", "i.e. réduit :"),
 ("est triviale.)", "est triviale)"),
 (r"\deleted{\unsure{la généralité que si}}", r"\deleted{\unsure{la généralité que si}}"+'\n'+r"\inserted{de plus}"),
 (r"\(\delta=d\cap d'\)"+'\n'+r"\deleted{\(d\cup d'\)}",
  r"\((\delta=d\cap d')\)"+'\n'+r"\(\deleted{d\cup d^{\unsure{\prime|\prime\prime}}}\)"),
 (r"\unsure{cat. ou un}", "cat. ou un"),
 (r"\unsure{-|\longrightarrow}", r"\longrightarrow"),
 (r"\Sigma_{\unsure{\delta}}", r"\Sigma_\delta"),
 ("--- et idem pour les structures cylindriques.}", "--- et idem pour les structures cylindriques}"),
 (r"\varnothing", r"\phi"),
 (r"\unsure{\le}", r"\le "),
 (r"\Sigma_{i_{n-1}i_n}", r"\Sigma_{\unsure{i_{n-1}i_n}}"),
 (r"\unsure{pas un drapeau}", "pas un drapeau"),
 (r"\inserted{can.}", r"\inserted{can}"),
 (r"\unsure{que}", r"\unsure{que|qui}"),
 (r"\mathrm{déf}", r"\mathrm{def}"),
 (r"\Sigma_{ijk}", r"\Sigma_{ij\unsure{k|n}}"),
]
for a,b in replacements:
    assert a in tex, a
    tex=tex.replace(a,b)
tex=tex.replace(r"\margin{\(^*\)", "% Top note: horizontal separating stroke with a stepped return toward the starred insertion.\n"+r"\margin{\(^*\)",1)
tex=tex.replace(r"\margin{Il suffit", "% Right marginal note: enclosing right/bottom stroke and a left-pointing attachment leader.\n"+r"\margin{Il suffit",1)
tex=tex.replace(r"\margin{(\unsure{comme", "% Long left-margin addition, written diagonally; its attachment arrows are not mathematical map arrows.\n"+r"\margin{(\unsure{comme",1)
tex=tex.replace(r"\diagram{\begin{tikzcd}"+'\n'+r" \Sigma_{d''}\arrow[r,hook]", "% The extra upper-right arrow has a looped/retraced tail and an unwritten target.\n"+r"\diagram{\begin{tikzcd}"+'\n'+r" \Sigma_{d''}\arrow[r,hook]",1)
(BASE/'reader_returns/150_scan040.tex').write_text(tex)

coords={
'top_first':[55,15,1668,88], 'top_second':[205,49,1675,129],
'sans_plus':[1360,105,1683,225], 'inserted_i':[620,155,1000,270],
'main_diagram':[415,380,930,690], 'cartesian_line':[280,680,1040,826],
'zero_clause':[260,817,1670,995], 'right_note':[895,265,1675,798],
'transverse_note':[810,875,1677,1105], 'left_upper':[0,385,615,1300],
'left_middle':[0,1015,650,1750], 'left_lower':[0,1480,800,2350],
'reconstruction':[300,1030,1678,1312], 'little_diagram':[760,1305,1110,1540],
'pour_nb':[1215,1320,1650,1450], 'vertical_sentence':[260,1520,1665,1725],
'transition':[260,1755,1668,2078], 'product':[650,2130,1430,2356],
'final_words':[1150,2270,1683,2358], 'folio':[17,2295,85,2353],
'top_phrase':[570,42,1030,120], 'top_maps':[1015,55,1683,137],
'right_revision':[1030,360,1590,630], 'right_formula':[890,505,1675,795],
'left_formulas':[0,1120,805,2205], 'left_intro':[0,320,570,1100]
}
data=dict(scan=40,reader='reader_b',line_count=48,changes=[],marks=[],inventory=[],doubts=[],notes=[],check_events=[],notation=[],abbreviations=[],hand_log=[],second_boxes=[])
def ch(place,c,h,f,crop,evidence,kind='misread word',error='words',cc=False,hh=True,conf='high',marked=False,effect=''):
    data['changes'].append(dict(place=place,C=c,H=h,final=f,evidence=evidence,crop='150_scan040_'+crop+'.jpg',box=coords[crop],confidence=conf,kind=kind,error_kind=error,marked_in_H=marked,change_C=cc,change_H=hh,consequential=effect))
def mark(m,context,decision,reading,crop,evidence,conf='medium'):
    data['marks'].append(dict(mark=m,context=context,decision=decision,reading=reading,evidence=evidence,crop='150_scan040_'+crop+'.jpg',box=coords[crop],confidence=conf))
def inv(element,kind,position,words,hand='his hand'):
    data['inventory'].append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
def doubt(place,reading,alternatives,conf='medium'):
    data['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=conf))
def box(name,kind,xy,reading,reason):
    data['second_boxes'].append(dict(box=name,kind=kind,coords=coords[xy] if isinstance(xy,str) else xy,reading=reading,reason=reason))

# Top note and principal condition.
ch('top note, opening',r"\unsure{pour que l'on ait}",r"\uncertain{déjà} que l'on ait","pour que l'on ait",'top_first','The initial p descends, followed by the short ou/r run; the separate que, l’on and ait are visible. No initial déjà sequence is present.',cc=True,marked=True,conf='medium')
ch('top note, intersection definition',r"\delta=d\cap d'",r"si $d\cap d'",r"\delta=d\cap d'",'top_first','A small looped delta is followed by two horizontal equality strokes before d; the prime belongs to the second d.',kind='misread symbol or index',error='symbols and indices')
ch('top note, phrase after ce qui',r"\unsure{signifie par|dit que pour les}","signifie par",r"\unsure{dit que pour les|dit que par les}",'top_phrase','A short compact verb is followed by que and a p-initial word and les. The long letter sequence required by signifie is absent. The compact verb and pour/par remain doubtful; narrowing C’s alternatives is not counted as a C textual change.',conf='medium')
ch('top note, first connector',r"\Sigma_d-\Sigma_\delta",r"\Sigma_d\to\Sigma_\delta",r"\Sigma_d-\Sigma_\delta",'top_maps','The connector is a blunt horizontal dash without a separate terminal head. Both neighboring subscripts are read with it.',kind='misread symbol or index',error='symbols and indices')
ch('top note, mono.',r"\unsure{mono.}",r"\ill{}","mono.",'top_maps','The low m-o-n-o sequence ends in a distinct dark full stop; the word is not physically illegible.',kind=r'readable ink left as \ill{}',error='readable ink left as illegible',cc=True,marked=True)
ch('top note, second connector and index',r"\Sigma_{\unsure{d''|d'}}-\Sigma_d",r"\Sigma_{d''}\to\Sigma_d",r"\Sigma_{d''}-\Sigma_d",'top_maps','Two small prime strokes follow the first d. The intervening horizontal stroke is headless, like the preceding connector; the second subscript is unprimed d.',kind='misread symbol or index',error='symbols and indices',cc=True,conf='medium')
ch('top note, terminal punctuation','est fibrant.','est fibrant','est fibrant','top_maps','The final t ends close to the right edge; no separate terminal stop is visible.',kind='text not on the page',error='text not on page',cc=True,hh=False,conf='medium')
ch('main line 1, inserted qualification',r"\inserted{\unsure{sans plus}\(^*\)}",r"\add{sans plus}${}^{*}$",r"\inserted{sans plus\(^*\)}",'sans_plus','The four letters sans and the p-l-u-s sequence are visible above the line, followed by the star matching the top note.',kind='other',cc=True,hh=False)
ch('main line 2, inserted index',r"\inserted{\(i\)}","élément $i$",r"\inserted{\(i\)}",'inserted_i','A separate dotted i is written above the baseline after élément; its raised placement is not the ordinary line of the following de d.',kind='insertion or placement',error='insertion placement')
main_diagram=tex[tex.index(r'\diagram{\begin{tikzcd}'):tex.index(r'\end{tikzcd}}')+len(r'\end{tikzcd}}')]
ch('principal square, extra rightward arrow',r"\Sigma_{d''}\arrow[r,hook]\arrow[d]&\Sigma_{d'}\arrow[d]",r"\Sigma_{d''} \arrow[r, hook] \arrow[d] & \Sigma_{d'} \arrow[d]",main_diagram,'main_diagram','There are five arrows: two horizontal hooked arrows and two downward arrows in the square, plus a rightward arrow leaving the upper-right object. Its tail is looped/retraced and its target area is blank. No target object is supplied.',kind='drawing or diagram',error='drawings and diagrams',cc=True,effect='Preserves an additional drawn arrow with unwritten target.')
ch('below principal square, ce dernier',r"\unsure{ce dernier|est}","Ce dernier","ce dernier",'cartesian_line','The small initial c-e and following d-e-r-n-i-e-r are visible before the separate est. Crossing slanted strokes here belong to the neighboring margin addition.',cc=True)
ch('trivial case, length',r"de longueur \(0\)",r"\ill{} i.e.",r"de longueur \(0\) i.e.",'zero_clause','The words de longueur are followed by a small closed zero, before i.e.; this is readable source text.',kind=r'readable ink left as \ill{}',error='readable ink left as illegible',marked=True)
ch('trivial case, colon',"réduit à","réduit à","réduit :",'zero_clause','Two vertically separated ink dots follow réduit. They do not form an accented à.',kind='other',error='other',cc=True)
ch('trivial case, closing punctuation',"est triviale.)","est triviale)","est triviale)",'zero_clause','The closing parenthesis follows triviale without an independently visible preceding full stop.',kind='text not on the page',error='text not on page',cc=True,hh=False)

# Dense right-hand annotation.
ch('right note, first length condition',"Il suffit de le supposer pour\n\\(d\\) de longueur \\(2\\)","Il suffit de le supposer quand $d$ et $d'$ sont de longueur 2",r"Il suffit de le supposer pour \(d\) de longueur \(2\)",'right_note','The word is pour, and only d occurs before de longueur 2. The separate alternative involving d-prime is parenthetical.',effect='Does not conflate the two alternative length assumptions.')
ch('right note, parenthetical alternative',r"(ou \(d'\) de longueur \(2\))",r"(\ill{} \ill{} \ill{})",r"(ou \(d'\) de longueur \(2\))",'right_note','The parenthesis contains ou, d with one high prime, de longueur and the curved digit 2.',kind=r'readable ink left as \ill{}',error='readable ink left as illegible',marked=True)
ch('right note, first cancelled wording',r"\deleted{\unsure{la généralité que si}}","généralement que lorsque",r"\deleted{\unsure{la généralité que si}}",'right_revision','A long horizontal cancellation crosses the phrase. The full sequence under it is not sufficiently plain to remove C’s doubt. H prints its different phrase as live.',kind='deletion state (struck given live or live given struck)',error='struck text',conf='low')
ch('right note, live interlinear addition','[absent]','[absent]',r"\inserted{de plus}",'right_revision','A smaller d-e and p-l-u-s line lies below the cancelled wording. These are independent live letters, not merely descenders from the deleted line.',kind='omission',error='omissions',cc=True,conf='medium')
ch('right note, second cancelled word',r"\deleted{\unsure{quelconques}}",'[absent]',r"\deleted{\unsure{quelconques}}",'right_revision','A separate horizontal strike crosses a q-initial word with a tall l and a later q-descender. Some intervening letters remain obscured, so the doubt is retained.',kind='omission',error='omissions',conf='medium')
ch('right note, relation of the two flags',"sont deux drapeaux tels que","sont deux drapeaux et que","sont deux drapeaux tels que",'right_note','The sequence after drapeaux starts with a tall t and a low e-l-s run, followed by que.',conf='medium')
ch('right note, inserted union definition',r"\inserted{\(d''=d\cup d'\)}",r"$d''=d\cup d'$",r"\inserted{\(d''=d\cup d'\)}",'right_formula','The union definition is squeezed into the left gap on a separate short line; it is an insertion before soit un drapeau.',kind='insertion or placement',error='insertion placement')
ch('right note, parenthesized intersection',r"\(\delta=d\cap d'\)",r"\ill{} $d''=d\amalg_\delta d'$",r"\((\delta=d\cap d')\)",'right_formula','Curved opening and closing parenthesis marks enclose delta equals d intersection d-prime. H leaves this expression unread; C omits the literal parentheses.',kind='omission',error='omissions',cc=True,marked=True,conf='medium')
ch('right note, cancelled union',r"\deleted{\(d\cup d'\)}",'[absent]',r"\(\deleted{d\cup d^{\unsure{\prime|\prime\prime}}}\)",'right_formula','A horizontal strike crosses d, a union sign and another d with crowded high ticks. The number of prime strokes remains one-or-two uncertain. This added uncertainty alone is not a C textual change.',kind='omission',error='omissions',conf='medium')
ch('right note, cat. ou un',r"\unsure{cat. ou un}",r"\ill{} \ill{}, alors","cat. ou un",'right_formula','The small c-a-t ends in a separate stop; ou follows, and a raised u-n precedes the next crossed token. No expansion of cat. is supplied.',kind=r'readable ink left as \ill{}',error='readable ink left as illegible',cc=True,marked=True,conf='medium')
ch('right note, cancelled ens',r"\deleted{\unsure{ens}}",'[absent]',r"\deleted{\unsure{ens}}",'right_formula','A short, heavily struck token stands before ordonné. Its e/n/s candidate remains doubtful; the physical cancellation is clear.',kind='omission',error='omissions',conf='low')
right_diagram=r"\diagram{\begin{tikzcd}"+'\n'+r" \Sigma_{d''}\arrow[r]\arrow[d]&\Sigma_{d'}\arrow[d]\\"+'\n'+r" \Sigma_d\arrow[r]&\Sigma_\delta"+'\n'+r"\end{tikzcd}}"+'\n'+'est cartésien.'
ch('right note, small cartesian square',right_diagram,r"$\Sigma_{d''}\to\Sigma_{d'}$, $\Sigma_d\to\Sigma_\delta$ \ill{} cartésien.",right_diagram,'right_formula','The four named vertices are connected by two horizontal and two downward arrows. Their small rightward heads are abbreviated. The separate words est cartésien follow. H’s editorial description is not treated as source transcription.',kind='drawing or diagram',error='drawings and diagrams',marked=True)

# Horizontal marginal transversality note.
ch('transversality note, placement',r"\margin{De plus, il faut supposer que lorsque","De plus, il faut supposer que lorsque",r"\margin{De plus, il faut supposer que lorsque",'transverse_note','The small passage occupies the right margin beside the end of (3), separate from the large main-line reconstruction paragraph.',kind='insertion or placement',error='insertion placement')
ch('transversality note, bracketed map',r"[\Sigma_{d'}\unsure{-|\longrightarrow}\Sigma_\delta]",r"\Sigma_{d'}\to\Sigma_\delta",r"[\Sigma_{d'}\longrightarrow\Sigma_\delta]",'transverse_note','The connector has a small projecting terminal head; bracket-like delimiters are visible on both sides of the map. The first subscript has a single prime, and the target is delta.',kind='misread symbol or index',error='symbols and indices',cc=True)
ch('transversality note, ambient subscript',r"\Sigma_{\unsure{\delta}}",r"\Sigma_{\ill{}}",r"\Sigma_\delta",'transverse_note','The low looped delta after the last Sigma matches the delta at the target of the bracketed map; it is not missing ink.',kind=r'readable ink left as \ill{}',error='readable ink left as illegible',cc=True,marked=True,conf='medium')
ch('transversality note, final words','et idem pour les structures cylindriques',r"et \ill{} pour ces structures cylindriques \ill{} \ill{}",'et idem pour les structures cylindriques','transverse_note','The short i-d-e-m is followed by pour and l-e-s, then structures cylindriques. No extra readable words follow this clause.',conf='medium',marked=True)
ch('transversality note, terminal punctuation','structures cylindriques.','structures cylindriques','structures cylindriques','transverse_note','No separate terminal dot can be distinguished at the end of the crowded small line; the transcription does not supply one.',kind='text not on the page',error='text not on page',cc=True,hh=False,conf='medium')

# Long diagonal marginal addition. Large missing spans are grouped by coherent physical lines.
left1=r"(\unsure{comme au n° précédent})"+'\n'+'On suppose de\n'+r"plus que \deleted{\unsure{d'ailleurs}} si pour \(i\in I\),"+'\n'+r"\(\operatorname{Dr}(I,i)\) désigne le sous-ens ordonné"+'\n'+r"de \(\operatorname{Dr}(I)\) formé des drapeaux"
ch('left margin, introduction and flag-poset notation',left1,r"\ill{} $\mathrm{Dr}(I)$ \ldots",left1,'left_intro','The definition names Dr(I,i), with a comma and a second dotted i, then Dr(I) on the next line. The surrounding prose and membership i∈I are readable. The initial parenthesis and the crossed d’ailleurs remain uncertain. H preserves only Dr(I) and an editorial ellipsis for this span.',kind='omission',error='omissions',marked=True,conf='medium')
left2=r"\(d\) dont le dernier élément est \(i\),"+'\n'+r"de sorte que les \(\Sigma_d\) sont \(\subset\Sigma_i\),"
ch('left margin, terminal element and inclusion',left2,'[absent]',left2,'left_upper','The prose specifies the last element i; the following line has Sigma-d, sont, an inclusion sign and Sigma-i. The nearby arrows attach the marginal writing; they are not extra symbols in this sentence.',kind='omission',error='omissions',conf='medium')
left3=r"alors les \(\Sigma_d\) forment dans \(\Sigma_i\) une"+'\n'+r"\uline{stratification précylindrique} de"+'\n'+r"type \(\operatorname{Dr}(I,i)^\circ\), ce qui s'exprime par"+'\n'+'les conditions supplémentaires'
ch('left margin, stratification requirement',left3,'[absent]',left3,'left_middle','The two technical words are underlined; the type is Dr(I,i) followed by an open superscript circle. The clause leads into conditions a), b), c).',kind='omission',error='omissions',conf='medium')
a_final=r"\text{a)}\quad \Sigma_{kj}\cap\Sigma_{\ell j}=\phi"+'\n'+r" \quad\text{si }k,\ell\le j\text{ sont des noncomparables}."
a_c=r"\text{a)}\quad \Sigma_{kj}\cap\Sigma_{\ell j}=\varnothing"+'\n'+r" \quad\text{si }k,\ell\unsure{\le}j\text{ sont des noncomparables}."
ch('left margin, complete condition a)',a_c,r"a) $\Sigma_d\cap\Sigma_{d'}=\emptyset$ si \ill{}",a_final,'left_formulas','The subscripts are kj and ℓj. The relation after k,ℓ has an angle and a separate short lower bar, supporting ≤. The empty-set glyph is a small loop crossed by a long descending stroke, literally phi-shaped. Noncomparables is written as one word.',kind='misread symbol or index',error='symbols and indices',cc=True,marked=True,conf='medium',effect='Restores both indices, the order restriction and the written phi-shaped glyph.')
b_final=r"\text{b)}\quad"+'\n'+r" \Sigma_{i_0\ldots i_n}"+'\n'+r" =\Sigma_{i_0i_n}\cap\Sigma_{i_1i_n}\cdots"+'\n'+r" \cap\Sigma_{\unsure{i_{n-1}i_n}}"+'\n'+r" \qquad\text{dans }\Sigma_{i_n}"
b_c=b_final.replace(r'\unsure{i_{n-1}i_n}',r'i_{n-1}i_n')
ch('left margin, complete condition b)',b_c,r"\uncertain{$\Sigma_{i_0\ldots i_n}=\Sigma_{i_0}\cap\ldots$} \ldots\ b) $\Sigma_{i_0\ldots i_n}$ \ill{}",b_final,'left_formulas','The first two intersection factors each carry a second terminal i_n; the first contains the digit 0 and the next the digit 1. The last factor’s small cluster is obscured by crossing main-text strokes and remains doubtful. Adding that doubt does not count as a C textual change.',kind='misread symbol or index',error='symbols and indices',marked=True,conf='medium')
cases_final=r"\left(\Longleftrightarrow"+'\\\n'+r" \Sigma_d\cap\Sigma_{d'}="+'\n'+r" \begin{cases}"+'\n'+r" \phi&\text{si }d\cup d'\text{ pas un drapeau}\\"+'\n'+r" \Sigma_{d\cup d'}&\text{sinon}"+'\n'+r" \end{cases}\right)"
cases_c=cases_final.replace(r'\phi',r'\varnothing').replace('pas un drapeau',r'\unsure{pas un drapeau}')
ch('left margin, parenthetical two-case formula',cases_c,r"($\Leftarrow$ $\Sigma_d\cap\Sigma_{d'}=\Sigma_{d\cup d'}$)",cases_final,'left_formulas','The outlined equivalence sign has heads at both ends. A left brace separates two cases, the first phi-shaped glyph followed by si d∪d′ pas un drapeau, and the second Sigma indexed by the union followed by sinon. The words pas un drapeau are individually recoverable; no n’est is added.',kind='misread symbol or index',error='symbols and indices',cc=True,conf='medium',effect='Preserves the written two-case alternative and equivalence, rather than an unconditional equality.')
ch('left margin, condition c) opening',"c) L'intersection dans b) est transversale.",'[absent]',"c) L'intersection dans b) est transversale.",'left_lower','The full sentence names the intersection in b) and calls it transversale. H’s partial c) begins with the following On instead.',kind='omission',error='omissions',conf='medium')
c_final=r"On suppose plus précisément, \unsure{choisis|choisies} des structures"+'\n'+r"cylindriques \unsure{qui rendent transversales}"+'\n'+r"\(\Sigma_{ij}\) \(\unsure{(i<j)}\)."
ch('left margin, final structures clause',c_final,r"On \ill{} \ill{} cylindriques \ill{} \ill{} \ill{} transverses \ill{}",c_final,'left_lower','On suppose plus précisément and des structures are visible. The choisis/choisies ending and the crowded intervening phrase remain doubtful; the candidate reads transversales, not H’s shorter transverses. Sigma-ij and the following parenthetical inequality are kept with the latter in doubt.',kind='omission',error='omissions',marked=True,conf='low')

# Main reconstruction passage and bottom display.
ch('reconstruction, opening sentence',r"Cela nous donne un procédé \unsure{canonique} pour",r"Cela revient donc à \ill{} \ill{} $\Sigma_{\ill{}}$ \ill{} \ill{}",r"Cela nous donne un procédé \unsure{canonique} pour",'reconstruction','The main baseline reads nous donne un procédé and ends pour. No standalone Sigma is written in this clause; nearby marginal symbols cross its area. Canonique remains doubtful where descenders overlap.',conf='medium',marked=True)
ch('reconstruction, verb','reconstruire les','construire les','reconstruire les','reconstruction','The word starts with the separate r-e sequence before construire.',conf='high')
ch('reconstruction, isomorphism qualification',r"à isom. \inserted{can.} près",r"\uncertain{précisément} \ill{}",r"à isom. \inserted{can} près",'reconstruction','The baseline has à isom. and près. Above it is the small can insertion, attached by a curved leader; no independent stop follows can.',kind='abbreviation expanded or spelling modernised',error='abbreviation/spelling',cc=True,marked=True,conf='medium')
ch('reconstruction, knowledge clause','quand on connaît',r"\uncertain{connaissant}",'quand on connaît','reconstruction','Three words are visible, with a separate q-initial quand and on before connaît; the circumflex is detached above the latter word.',marked=True)
ch('NB parenthesis, extra word',r"\unsure{que}",'(NB,',r"\unsure{que|qui}",'pour_nb','A q-like descender and short terminal strokes form an actual word after NB; there is no comma in its place. The ending remains que/qui uncertain.',kind='omission',error='omissions',conf='medium')
ch('NB parenthesis, flèche','la flèche verticale','la verticale','la flèche verticale','vertical_sentence','The long f and linked l-è-c-h-e appear between la and verticale.',kind='omission',error='omissions')
ch('transition maps, flag index',r"\(\Sigma_d\) (construits",r"$\Sigma_{d'}$ (construits",r"\(\Sigma_d\) (construits",'transition','The subscript is unprimed d. The nearby high slanted stroke belongs to the diagonal marginal writing rather than to this index.',kind='misread symbol or index',error='symbols and indices')
ch('transition induction, length wording',r"les \(0\) et \(1\) étant déjà donné",r"\uncertain{pour} long 0 et 1 étant déjà donné",r"les \(0\) et \(1\) étant déjà donné",'transition','A short l-e-s precedes the plain zero and one. No additional long is written before them, and donné has no final plural s.',marked=True)
ch('bottom product, definition label',r"\mathrm{déf}",r"\text{déf}",r"\mathrm{def}",'product','The small d-e-f label above the equality has no detached accent over e; the f descends toward the bottom edge.',kind='abbreviation expanded or spelling modernised',error='abbreviation/spelling',cc=True)
ch('bottom line, added ellipsis','satisfaisant aux conditions',r"satisfaisant aux conditions\ldots",'satisfaisant aux conditions','final_words','The word conditions reaches the paper edge; no following sequence of points is visible.',kind='text not on the page',error='text not on page')
ch('bottom-left foliation',r"\margin{39}",'[absent]',r"\margin{39}",'folio','The separate thin foliation consists of a double-curved 3 and a loop with descending tail forming 9. It is not treated as his own page number.',kind='omission',error='omissions')

# Every original C doubt, including cancelled text.
mark(r"\unsure{pour que l'on ait}","Il suffit \\unsure{pour que l'on ait} que",'first',"pour que l'on ait",'top_first','The descending p and subsequent separate que, l’on, ait are present; the initial word is not déjà.')
mark(r"\unsure{signifie par|dit que pour les}",r"ce qui \unsure{signifie par|dit que pour les}",'undecided',r"\unsure{dit que pour les|dit que par les}",'top_phrase','The short verb and following que exclude a full signifie sequence; the verb and compressed p-word are not completely resolved.')
mark(r"\unsure{mono.}",r"est \unsure{mono.} et",'first','mono.','top_maps','The low m-o-n-o sequence and its following dark point are visible.','high')
mark(r"\unsure{d''|d'}",r"\Sigma_{\unsure{d''|d'}}-\Sigma_d",'first',"d''",'top_maps','The full map is read as Sigma-d-double-prime, a headless dash, Sigma-d; the two high ticks are distinct.')
mark(r"\unsure{sans plus}",r"\inserted{\unsure{sans plus}\(^*\)}",'first','sans plus','sans_plus','All letters of the two inserted words are visible above the baseline, before the star.','high')
mark(r"\unsure{ce dernier|est}",r"\unsure{ce dernier|est} est",'first','ce dernier','cartesian_line','Small ce followed by d-e-r-n-i-e-r precedes the separate est; the long crossing strokes belong to the slanted addition.','high')
mark(r"\unsure{la généralité que si}",r"\deleted{\unsure{la généralité que si}}",'undecided',r"\unsure{la généralité que si}",'right_revision','The broad deletion is unambiguous, but its line covers enough of the internal letters that the complete phrase cannot be certified.','low')
mark(r"\unsure{quelconques}",r"\deleted{\unsure{quelconques}}",'undecided',r"\unsure{quelconques}",'right_revision','An initial q and a tall l, with a later q-descender, fit quelconques; the strike obscures intervening letters.')
mark(r"\unsure{cat. ou un}",r"\unsure{cat. ou un} \deleted",'first','cat. ou un','right_formula','The c-a-t with point, ou, and raised u-n are separately visible; no expansion is made.')
mark(r"\unsure{ens}",r"\deleted{\unsure{ens}} ordonné",'undecided',r"\unsure{ens}",'right_formula','A short word is crossed immediately before ordonné; the three letters remain too compressed under the thick strike.','low')
mark(r"\unsure{-|\longrightarrow}",r"[\Sigma_{d'}\unsure{-|\longrightarrow}\Sigma_\delta]",'alternative',r"\longrightarrow",'transverse_note','The complete bracketed map has a short projecting terminal arrowhead; neighboring subscripts are d-prime and delta.','high')
mark(r"\unsure{\delta}",r"\Sigma_{\unsure{\delta}}",'first',r"\delta",'transverse_note','The last subscript has the same low looped delta form as the target in the preceding bracketed map.')
mark(r"\unsure{comme au n° précédent}",r"\margin{(\unsure{comme au n° précédent})",'undecided',r"\unsure{comme au n° précédent}",'left_intro','The parenthetical line begins at the paper edge. The small initial words and the n° candidate are compressed; précédent is more legible.')
mark(r"\unsure{d'ailleurs}",r"plus que \deleted{\unsure{d'ailleurs}} si",'undecided',r"\unsure{d'ailleurs}",'left_intro','The strike traverses the token after que. The long letter strokes admit d’ailleurs, but all letters are not independently plain.','low')
mark(r"\unsure{\le}",r"k,\ell\unsure{\le}j",'first',r"\le",'left_formulas','The complete a) formula has an angle sign and short lower bar before j. Crossing main-text strokes are distinguished from that bar.')
mark(r"\unsure{pas un drapeau}",r"d\cup d'\text{ \unsure{pas un drapeau}}",'first','pas un drapeau','left_formulas','In the first case, the p-descender, short a-s, separate un and d-r-a-p-e-a-u sequence are visible. The full two-case formula is retained.')
mark(r"\unsure{choisis|choisies}",r"précisément, \unsure{choisis|choisies} des structures",'undecided',r"\unsure{choisis|choisies}",'left_lower','The choi- initial is visible, but the compressed last strokes do not securely distinguish the two endings. Grammar is not used to choose.')
mark(r"\unsure{qui rendent transversales}",r"cylindriques \unsure{qui rendent transversales}",'undecided',r"\unsure{qui rendent transversales}",'left_lower','The linked low strokes and long descenders overlap the larger main writing; the candidate phrase remains only partly recoverable.','low')
mark(r"\unsure{(i<j)}",r"\(\Sigma_{ij}\) \(\unsure{(i<j)}\)",'undecided',r"\unsure{(i<j)}",'left_formulas','The complete Sigma-ij and following parenthesis are crowded by main-line descenders. A dotted i, angle and j-shaped stroke are plausible, but the grouping is not fully separable.')
mark(r"\unsure{canonique}",r"procédé \unsure{canonique} pour",'undecided',r"\unsure{canonique}",'reconstruction','The baseline word fits canonique, but letters in its middle are crossed by the small transversality note; the doubt is not removed.')
mark(r"\unsure{que}",r"(NB \unsure{que}",'undecided',r"\unsure{que|qui}",'pour_nb','The q-descender is present, followed by a compact ending with a high point. Que and qui remain possible; no comma substitutes for the word.')

# Complete physical inventory.
inv('T01','text','upper main three lines','(3) Soient d,d′ deux drapeaux tels que')
inv('M01','margin note','two lines across the top, above horizontal separator','* Il suffit pour que l’on ait que; the separating line steps downward toward sans plus')
inv('I01','insertion','above end of main first line','sans plus *')
inv('I02','insertion','above élément in main second line','i')
inv('D01','diagram','upper middle, below main condition','Σd″, Σd′, Σd, Σi; four square arrows and fifth rightward arrow to blank')
inv('T02','text','below principal square','ce dernier est cartésien. (Pour d ou d′')
inv('M02','margin note','right of principal square, slanted and bounded by a long enclosing stroke','Il suffit de le supposer pour d de longueur 2; left-pointing attachment leader')
inv('C01','deletion','right marginal note below On en déduit plus','la généralité que si, doubtful')
inv('I03','insertion','under first cancelled line in right note','de plus')
inv('C02','deletion','right marginal note, next line','quelconques, doubtful')
inv('I04','insertion','left gap inside right marginal note','d″=d∪d′')
inv('C03','deletion','right note before live amalgamation equation','d∪d′/d″, prime count doubtful')
inv('C04','deletion','right note before ordonné','ens, doubtful')
inv('D02','diagram','lower part of right marginal note','circled D; Σd″, Σd′, Σd, Σδ with four arrows')
inv('M03','margin note','small horizontal right note beside trivial case','De plus, il faut supposer que lorsque')
inv('M04','margin note','long diagonal note filling left margin','(comme au n° précédent); On suppose de plus que; attachment strokes point into main writing')
inv('C05','deletion','near beginning of diagonal note after plus que','d’ailleurs, doubtful')
inv('F01','display','diagonal marginal condition a)','Σkj∩Σℓj=phi, si k,ℓ≤j sont des noncomparables')
inv('F02','display','diagonal marginal condition b)','Σi0…in=Σi0in∩Σi1in…∩Σ[doubtful last index], dans Σin')
inv('F03','display','diagonal marginal parenthesis after b)','two-headed equivalence and two-case intersection formula')
inv('T03','text','diagonal marginal ending','c) L’intersection dans b) est transversale; On suppose plus précisément')
inv('T04','text','main reconstruction paragraph','Cela nous donne un procédé canonique pour reconstruire')
inv('I05','insertion','above à isom. près','can, without visible stop; curved attachment leader')
inv('I06','insertion','above end of reconstruction paragraph before et les morphismes','(i<j)')
inv('D03','diagram','middle main span','Σij hooks right to Σj and maps downward to Σi')
inv('C06','deletion','right of little span above NB','Pour')
inv('T05','text','beside and below little span','(NB que/qui la flèche verticale est fibrante')
inv('T06','text','lower main paragraph','Pour avoir les morphismes de transition entre les Σd')
inv('F04','display','bottom edge','underbraced Σij×ΣjΣjk, defining Σij[k/n], arrow to Σi,k')
inv('T07','text','bottom-right final line','satisfaisant aux conditions')
inv('N01','margin note','bottom-left corner','39','thin separate foliation; attribution uncertain')

# Retained and newly identified doubts, without inflating textual change counts.
doubt('top note after ce qui',r"\unsure{dit que pour les|dit que par les}",'The short verb and pour/par run are compressed; signifies is excluded.')
doubt('right note first cancelled phrase',r"\deleted{\unsure{la généralité que si}}",'Internal letters under cancellation remain incompletely legible.','low')
doubt('right note second cancelled token',r"\deleted{\unsure{quelconques}}",'The outline fits quelconques; several letters lie under the strike.')
doubt('right note cancelled union',r"\deleted{d\cup d^{\unsure{\prime|\prime\prime}}}",'One or two high prime ticks after the second d.')
doubt('right note cancelled ens',r"\deleted{\unsure{ens}}",'Heavily crossed short token.','low')
doubt('diagonal margin initial parenthesis',r"\unsure{comme au n° précédent}",'Compressed opening and abbreviation at the paper edge.')
doubt('diagonal margin cancellation',r"\deleted{\unsure{d'ailleurs}}",'Letter sequence partially covered by its deletion stroke.','low')
doubt('condition b), last factor',r"\Sigma_{\unsure{i_{n-1}i_n}}",'Small index cluster intersects main-text strokes. The expected n−1 is not silently certified.')
doubt('condition c), choice of structures',r"\unsure{choisis|choisies}",'Final ending cannot be separated with confidence.')
doubt('condition c), crowded phrase',r"\unsure{qui rendent transversales}",'Linked strokes and descenders overlap larger main writing.','low')
doubt('condition c), final inequality',r"\Sigma_{ij}\) \(\unsure{(i<j)}",'Complete final expression kept; the inequality and parentheses are crowded.')
doubt('main reconstruction adjective',r"\unsure{canonique}",'Overlapping small marginal writing prevents secure reading of all letters.')
doubt('NB word',r"\unsure{que|qui}",'The terminal short stroke and high point admit e or i.')
doubt('bottom underbrace index',r"\Sigma_{ij\unsure{k|n}}",'The final index is small and clipped by the physical bottom edge; the preceding i and j are identifiable.')

data['notes']=[
 'This leaf has no visible page number in his own hand. It carries separate thin bottom-left foliation 39; attribution of that foliation is uncertain.',
 'The page states a cartesian-square condition for concatenated flags and reports a reduction to a length-2 case. It adds a transversality requirement and a diagonal marginal proposal for a precylindrical stratification indexed by Dr(I,i) with an open-circle decoration. These are reported claims, not checked theorems.',
 'The lower main paragraph reports a reconstruction of the Sigma_d from Sigma_i, Sigma_ij and the indicated spans, then asks for transition maps from a fiber product to Sigma_{i,k}. No proof or independent mathematical check was performed in this reading.',
 'The upper-right vertex of the principal square emits an additional rightward arrow into blank space. It has a looped/retraced tail. The empty target is deliberately preserved.',
 'Top map connectors are headless horizontal dashes. In the transversality note the short connector has a visible arrowhead. These locally different forms have not been standardized.',
 'The right marginal note has a large enclosing boundary stroke and a left-pointing attachment leader. The top note is separated by a long horizontal line with a stepped return toward the starred insertion. The diagonal note has attachment arrows. These attachment features are recorded separately from the mathematical diagrams.',
 'A live de plus sits below the first crossed line of the right note. It is retained despite the repeated plus in the surrounding draft syntax. The crossed wording is not silently repaired into a fluent sentence.',
 'The two empty-set signs in the diagonal note are loop-and-descender, phi-shaped glyphs. The transcription uses phi for their written shape; interpreting them as the empty set follows the local cases and disjointness context.',
 'Condition b) is transcribed with the last factor index doubtful because large main-text strokes obscure part of the small marginal cluster. The digit components in the other factors are retained as written.',
 'The bottom underbrace label is unaccented def. Its last index remains k/n doubtful at the page edge; the target Sigma_{i,k} has a visible comma and a k-shaped final letter. The target is not used to force the clipped label.',
 'The source has singular donné in les 0 et 1 étant déjà donné. The first case says pas un drapeau without n’est. These are retained without grammatical completion.',
 'No distinct stop is visible after top-note fibrant, inserted can, or the final small transversality clause. There is no stop before the closing parenthesis after triviale and no ellipsis after the edge-ending conditions.',
 'All 26 saved crops were directly viewed. The supplemental crops address unresolved crowded places or complete formulas that the first rotated boxes divided; no decided reading was reopened merely for repetition. Whole image and both native halves were viewed once each.',
 'The line_count includes physical text/display rows and marginal rows as counted during this one-page reading; source line wrapping is not normalized into a prose word count.'
]
data['notation']=[
 {'form':r'\phi','meaning_or_shape':'Loop with a long descending crossing stroke; used here for the empty set. The actual phi-like shape is retained.','places':'diagonal condition a) and first case of the following intersection formula'},
 {'form':r'\Sigma_d-\Sigma_\delta,\quad\Sigma_{d\prime\prime}-\Sigma_d','meaning_or_shape':'Headless horizontal connectors, distinct from the tiny-headed arrow in the later transversality note.','places':'top marginal note'},
 {'form':r'\delta=d\cap d\prime','meaning_or_shape':'Small looped delta, then two-bar equality and cap. Literal parentheses enclose its right-note repetition.','places':'top note and right marginal note'},
 {'form':r'\operatorname{Dr}(I,i)^\circ','meaning_or_shape':'Dr with a capital serif I, comma and dotted small i; a hollow superscript circle follows the closing parenthesis.','places':'diagonal marginal stratification type'},
 {'form':r'\mathrm{def}','meaning_or_shape':'Unaccented d-e-f over the defining equality.','places':'bottom underbrace label'},
 {'form':r'\Sigma_{i,k}','meaning_or_shape':'An independent low comma separates i and k; the k has a broad lower return.','places':'target of bottom product map'},
 {'form':r'\Longleftrightarrow','meaning_or_shape':'Outlined double shaft with heads at both ends.','places':'parenthetical intersection formula in diagonal note'},
 {'form':r'\Sigma_{ij\unsure{k|n}}','meaning_or_shape':'The clipped last index is retained as k/n uncertain; no claim that the product factors settle the ink.','places':'bottom underbrace label'}
]
data['abbreviations']=[
 {'form':'mono.','expansion':'monomorphisme or monomorphe, according to syntactic use; not expanded in the page'},
 {'form':'cat.','expansion':'catégorie; retained as the written abbreviation'},
 {'form':'ens','expansion':'ensemble; cancelled candidate remains doubtful'},
 {'form':'sous-ens','expansion':'sous-ensemble'},
 {'form':'isom.','expansion':'isomorphisme'},
 {'form':'can','expansion':'canonique; inserted without a visible stop'},
 {'form':'i.e.','expansion':'id est'},
 {'form':'NB','expansion':'nota bene'},
 {'form':'long','expansion':'longueur'},
 {'form':'def','expansion':'définition; expansion does not restore an accent to the source'},
 {'form':'n°','expansion':'numéro; the whole parenthetical phrase remains doubtful'}
]
data['hand_log']=[
 {'habit':'A short map connector may be a headless dash or may carry only a tiny rightward head.','places':'top two maps; transversality map; two squares','consistent':'Top two connectors have no head; transversality connector does. These are local forms, not a uniform convention.','witness_errors':'H supplies arrows for the two headless top connectors; C leaves the transverse connector doubtful.'},
 {'habit':'The empty-set glyph can be drawn as a small loop with a long descending stroke, visually phi-shaped.','places':'condition a) and first case of the parenthetical intersection formula','consistent':'Both visible uses on this leaf have the same shape.','witness_errors':'C uses varnothing and H emptyset, losing the particular written form.'},
 {'habit':'A k can finish with a broad arch/return that resembles n; edge clipping removes the distinction.','places':'bottom Sigma_jk, target Sigma_i,k, clipped underbrace index','consistent':'The uncut target supports k; the final underbrace index remains doubtful.','witness_errors':'Both witnesses assert k in the clipped index; no substantive error is claimed from added uncertainty alone.'},
 {'habit':'Interlinear insertions can sit immediately under a cancellation without being crossed themselves.','places':'de plus below the first crossed line of the right note','consistent':'The separate baseline and independent letter strokes distinguish this insertion from cancellation descenders.','witness_errors':'Both witnesses omit the live de plus.'},
 {'habit':'Diagonal marginal text crosses large main-text baselines and can resemble primes or strikes.','places':'ce dernier; transition Sigma_d; canonique; marginal b) final index','consistent':'The trajectories are traceable to the marginal hand; some intersections still obscure letters.','witness_errors':'H adds a prime to the main transition Sigma_d and misreads substantial reconstruction prose.'},
 {'habit':'Small def is written without an accent; can lacks a clearly separate final stop.','places':'bottom equality label and inserted reconstruction qualifier','consistent':'Single occurrence of each on this leaf; judged locally.','witness_errors':'Both witnesses accent déf; C supplies the stop after can.'},
 {'habit':'Foliation is thinner and separate from the main handwriting.','places':'bottom-left 39','consistent':'One foliation on this leaf; attribution remains uncertain.','witness_errors':'H omits the foliation.'}
]

# Mandatory second-pass boxes, all with coherent complete local readings.
top_margin=tex[tex.index(r'\margin{\(^*\)'):tex.index('\n\n(3)')]
box('b01','margin note|doubt formula|C/H word difference|low-confidence departure',[55,15,1683,137],top_margin,'Complete two-line starred note, including every original top-note doubt, both full map expressions and its ending punctuation.')
main_condition=tex[tex.index('(3) Soient'):tex.index('% The extra upper-right arrow')].strip()
box('b02','handwritten number|insertion|C/H word difference',[160,105,1685,375],main_condition,'The handwritten item number 3, both sans plus and i insertions, the flag variables and the full concatenation definition.')
box('b03','drawing or diagram','main_diagram',main_diagram,'Every object and all five drawn arrows, including the extra upper-right arrow with blank target.')
trivial=tex[tex.index('ce dernier'):tex.index('% Right marginal note')].strip()
box('b04','handwritten number|C/H word difference|low-confidence departure',[260,680,1670,995],trivial,'Complete assertion and parenthetical trivial case, the digit zero, ce dernier, colon after réduit and closing punctuation.')
right_margin=tex[tex.index(r'\margin{Il suffit'):tex.index(r'\margin{De plus')].strip()
box('b05','margin note|insertion|struck passage|doubt formula|handwritten number|C/H word difference|low-confidence departure','right_note',right_margin,'Complete right note: both handwritten 2s; all four cancelled spans; live de plus and inserted union definition; full parenthesized intersection and amalgamation expressions; circled D and complete small square.')
transverse=tex[tex.index(r'\margin{De plus'):tex.index('% Long left-margin addition')].strip()
box('b06','margin note|doubt formula|handwritten number|C/H word difference|low-confidence departure','transverse_note',transverse,'Complete small transversality note, digit 2, bracketed map, ambient Sigma-delta and final words; arrowhead and all neighboring indices reread together.')
box('b07','margin note|struck passage|doubt formula|C/H word difference','left_intro',left1,'Opening of diagonal addition, its doubtful parenthesis and cancellation, full membership i∈I and both Dr expressions; H’s absent prose.')
box('b08','margin note|C/H word difference','left_upper',left2,'Complete terminal-element clause and resulting inclusion sentence; checks agreed words as well as H’s omission.')
box('b09','margin note|C/H word difference','left_middle',left3,'Full requirement of a precylindrical stratification, its underlining and full Dr(I,i)-circle type.')
box('b10','margin note|doubt formula|handwritten number|C/H word difference|low-confidence departure','left_formulas',r'\['+'\n '+a_final+'\n'+r'\]'+'\n'+r'\['+'\n '+b_final+'\n'+r'\]'+'\n'+r'\['+'\n '+cases_final+'\n'+r'\]','Complete a), b) and parenthetical cases. Includes all handwritten 0 and 1 digits in the multi-indices, the doubtful n−1 cluster, ≤, both phi-shaped glyphs, and the full two-headed equivalence with both cases.')
box('b11','margin note|doubt formula|C/H word difference|low-confidence departure','left_lower',"c) L'intersection dans b) est transversale.\n"+c_final,'Complete c) and final structures clause, including all retained word doubts and the complete Sigma-ij plus parenthetical inequality.')
reconstruction=tex[tex.index('Cela nous donne'):tex.index(r'\diagram{\begin{tikzcd}',tex.index('Cela nous donne'))].strip()
box('b12','insertion|C/H word difference|low-confidence departure','reconstruction',reconstruction,'Complete reconstruction paragraph: canonique doubt, inserted can without supplied stop, and inserted (i<j); all C/H prose differences are read in context.')
little_diagram=r'\diagram{\begin{tikzcd}'+'\n'+r' \Sigma_{ij}\arrow[r,hook]\arrow[d]&\Sigma_j\\'+'\n'+r' \Sigma_i&'+'\n'+r'\end{tikzcd}}'
box('b13','drawing or diagram','little_diagram',little_diagram,'Three objects, hooked horizontal arrow, plain downward arrow and blank lower-right position.')
box('b14','struck passage|C/H word difference|low-confidence departure','pour_nb',r'\deleted{Pour}'+'\n'+r'(NB \unsure{que|qui}','Readable cancelled Pour and complete local NB opening. The later closing parenthesis is preserved with its main-line continuation.')
box('b15','C/H word difference','vertical_sentence',"la flèche verticale est fibrante, et l'horizontale\nun morphisme-bord). Pour avoir les",'The complete NB continuation and its closing punctuation; specifically includes flèche, which H omits.')
transition=r'morphismes de transition entre les'+'\n'+r'\(\Sigma_d\) (construits par récurrence sur \(\operatorname{long}d\),'+'\n'+r'les \(0\) et \(1\) étant déjà donné) il faut se donner'+'\n'+'les morphismes'
box('b16','handwritten number|C/H word difference',[260,1755,1668,2135],transition,'Full transition clause, plain Sigma-d, the phrase les 0 et 1, both digits and singular donné; the neighboring diagonal stroke is not a prime.')
product=tex[tex.index(r'\[',tex.index('les morphismes\n',tex.index('Pour avoir les'))):tex.index('satisfaisant aux conditions')].strip()
box('b17','doubt formula|C/H word difference|low-confidence departure','product',product,'Complete product map, base subscript Sigma-j, both factors, whole underbrace equality with unaccented def and clipped k/n index, and the comma-bearing target Sigma-i,k.')
box('b18','C/H word difference','final_words','satisfaisant aux conditions','Complete final wording and the blank/edge after conditions; no ellipsis is supplied.')
box('b19','margin note|handwritten number','folio',r'\margin{39}','Both digits of the separate foliation, 3 and 9, read together.')

def norm(s):
    return re.sub(r'\s+',' ',s).strip()
issues=[]
for i,row in enumerate(data['changes'],1):
    if norm(row['final']) not in norm(tex): issues.append(f'change {i} final not found: {row["place"]}')
    if row['C']!='[absent]' and norm(row['C']) not in norm(C): issues.append(f'change {i} C not found: {row["place"]}')
    if row['H']!='[absent]' and norm(row['H']) not in norm(H): issues.append(f'change {i} H not found: {row["place"]}')
    if not (BASE/'crops'/row['crop']).exists(): issues.append(f'change {i} crop missing')
    if not (row['change_C'] or row['change_H']): issues.append(f'change {i} has no witness change')
for i,row in enumerate(data['marks'],1):
    if row['mark'] not in C: issues.append(f'mark {i} original missing')
    if norm(row['context']) not in norm(C): issues.append(f'mark {i} context missing')
    if not (BASE/'crops'/row['crop']).exists(): issues.append(f'mark {i} crop missing')
for row in data['second_boxes']:
    if norm(row['reading']) not in norm(tex): issues.append(f'second box {row["box"]} reading not found')
    a,b,c,d=row['coords']
    if not (0<=a<c<=1685 and 0<=b<d<=2359):issues.append(f'second box {row["box"]} coords invalid')
orig=[]
for m in re.finditer(r'\\(?:unsure|illegible)\{',C):
    k=m.end(); dep=1
    while dep:
        if C[k]=='{':dep+=1
        elif C[k]=='}':dep-=1
        k+=1
    orig.append(C[m.start():k])
if orig!=[x['mark'] for x in data['marks']]:issues.append('Original C marks not covered once in order')
depth=0
for m in re.finditer(r'(?<!\\)[{}]',tex):
    depth+=1 if m.group()=='{' else -1
    if depth<0:issues.append('Early unmatched TeX closing brace')
if depth:issues.append('Unbalanced TeX braces')
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
for row in data['changes']:
    if row['kind'] not in allowed:issues.append('Invalid change kind: '+row['kind'])
output=BASE/'reader_returns/150_scan040.json'
output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tex':str(BASE/'reader_returns/150_scan040.tex'),'json':str(output),'changes':len(data['changes']),'change_C':sum(x['change_C'] for x in data['changes']),'change_H':sum(x['change_H'] for x in data['changes']),'marks':len(data['marks']),'resolved_marks':sum(x['decision']!='undecided' for x in data['marks']),'inventory':len(data['inventory']),'doubts':len(data['doubts']),'second_boxes':len(data['second_boxes']),'crops':len(coords),'validation_issues':issues},ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)

