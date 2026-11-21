import json
from pathlib import Path

root = Path('/workspace/scratch/4644e52611c0')
boxes = json.loads((root/'work/149_scan027_reader_a_crop_boxes.json').read_text())['boxes']
tex = r'''\scanpage{27}
\mspage{13}
L'hyp. que $\pi_1(f')$ \deleted{et} $=\pi_1(g)$ signifie donc qu'il existe $\alpha\in\pi_1(Y)$, tel que
\[
\pi_1(j')(\unsure{\sigma|\gamma})=\inserted{\operatorname{int}(\alpha)}\pi_1(j)(\unsure{\sigma|\gamma})
\]
pour tt $\unsure{\sigma|\gamma}\in\operatorname{Im}(\pi_1(X)\overset{\pi_1(f)}{-}\pi_1(U))$. Or cette image est un sous-groupe \uline{ouvert} de $\pi_1(U)$ (tjrs vrai pour un morphisme dominant!). \deleted{D'ailleurs} Donc on est ramené à ceci: Soit $U$ ouvert \inserted{$\ne\varnothing$} de $Y$, et $u\in G$, tels que $\tau_uU\subset Y$ [et tels que (désignant par $j,j'$ les \deleted{applications} \inserted{morphismes} $y\longrightarrow y$ et $y\unsure{\mapstochar\relbar|\longmapsto}y+u$ de $U$ dans $Y$) $\pi_1(j)$ et $\pi_1(j')$ coïncident extérieurement sur un sous-groupe ouvert de $\pi_1(U)$] -- \uline{alors} $j=j'$ i.e $u=0$.

\margin{\uline{NB} ceci n'est pas plus fort que le corollaire, comme on voit en prenant pour $X$ le rev. étale fini de $U$ correspondant à un sous-groupe ouvert \unsure{arbitraire} de $\pi_1(U)$\unsure{. --}}

Finalement, je m'aperçois que je n'arrive pas à le prouver par voie géométrique -- pour ceci je me rabats sur une méthode \uline{arithmétique};
\margin{Si -- cf. plus bas!}

\deleted{\unsure{Je ferai} d'ailleurs \deleted{\unsure{affaibli}} \unsure{généraliser|généralisé} le th. géométrique; on montre que (quitte à remplacer $X$ par un ouvert non vide connexe\unsure{,|.} ce qui ne détruit pas les hyp. ni ne modifie la conclusion) OPS que $X$ est une variété}
\margin{26}
'''
(root/'edition/reviews/149_scan027.tex').write_text(tex, encoding='utf-8')

changes=[]
def change(place,C,H,final,evidence,crop,confidence,against_C,against_H,kind,category,marked=False,mathematical=False):
    ident=f'c{len(changes)+1:02}'
    changes.append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/149_scan027_c{crop:02}.png',box=boxes[str(crop)],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=category,marked_in_H=marked,mathematical=mathematical))
    return ident

change('L1, first fundamental-group argument',r"\pi_1(\unsure{f'|f})",r'\pi_1(f)',r"\pi_1(f')",'A separate small raised stroke follows the f and precedes the closing parenthesis. It is distinct from both the f stem and the parenthesis. The whole opening formula was read; its two subscript numerals are 1. This is also decision M1054, first reading.',1,'high',False,True,'misread symbol or index','Symbols and indices',mathematical=True)
change('L1, overwritten conjunction between the two terms',r'\unsure{=|\simeq}',r'\struck{et} =',r'\deleted{et} =','Two equality bars cross an older small e-loop and a taller t-like upright. The surviving letters support et as cancelled/overwritten material. The curved residual ink belongs to the older letters, rather than a clean isomorphism wave. Equality itself resolves M1055 to its first reading; this substantive row records the old conjunction omitted by C.',1,'high',True,False,'omission','Struck text',mathematical=True)
change('L1, signifie',r'signifie',r'\emph{signifie}',r'signifie','The long low stroke is continuous with the g descender and turns back to the left under the beginning of the word. No independent underline crosses beneath the whole word. The remaining letters s-i-g-n-i-f-i-e and its two dotted i positions were checked.',2,'high',False,True,'other','Other')
change('Display L3, the two argument letters',r'\pi_1(j\prime)(\sigma)=\inserted{\operatorname{int}(\alpha)}\pi_1(j)(\sigma)'.replace('j\prime',"j'"),r"\pi_1(j')(\gamma)=\operatorname{int}(\alpha)\,\pi_1(j)(\gamma)",r"\pi_1(j')(\unsure{\sigma|\gamma})=\inserted{\operatorname{int}(\alpha)}\pi_1(j)(\unsure{\sigma|\gamma})",'Both argument forms have two upper arms and a narrow lower oval. Sigma remains the leading reading, but gamma is not cleanly excluded by the joined construction. The full equation, its equality, prime after the first j, both numeric indices, and the inserted int(alpha) were read together. No new certainty is claimed from the witnesses agreeing on the surrounding formula.',3,'low',False,True,'misread symbol or index','Symbols and indices',mathematical=True)
change('Display L3, raised operator insertion',r'\inserted{\operatorname{int}(\alpha)}',r'\operatorname{int}(\alpha)',r'\inserted{\operatorname{int}(\alpha)}','The operator and its parenthesized alpha sit above the principal baseline. A small insertion leader takes them to the gap before the second pi_1(j). It is a live addition, not a cancelled part of the equation. H has the same letters but does not preserve their insertion state.',3,'high',False,True,'insertion or placement','Insertions put in the wrong place',mathematical=True)
change('L4, argument before the image expression',r'\sigma',r'\gamma',r'\unsure{\sigma|\gamma}','The small letter again has two upper arms and a joined lower oval, matching the two display arguments. The whole image formula was inspected, including all three numeric indices and the label above the shaft. Sigma/gamma remains a local letter-form uncertainty.',4,'low',False,True,'misread symbol or index','Symbols and indices',mathematical=True)
change('L4, labelled connector within Im',r'\xrightarrow{\pi_1(f)}',r'\xrightarrow{\pi_1(f)}',r'\overset{\pi_1(f)}{-}','There is one horizontal shaft, ending in a short blunt/downturned cap rather than the separated two-branch head visible in the first y map later on the page. There is no left map bar. The label is pi with low 1 and unprimed f in parentheses. The literal shaft is kept, without supplying a right arrowhead.',4,'high',True,True,'misread symbol or index','Symbols and indices',mathematical=True)
change('L6, parenthesis after pi_1(U)',r'tjrs',r'\uncertain{fait}',r'tjrs','The initial t is followed by a long j descender and the low r/s run. There is no initial f sequence or final t upright that would support fait. No final abbreviation stop is visible.',5,'high',False,True,'misread word','Words',marked=True)
change('L8–L9, conjunction after de Y',r'de $Y$, et $a\in G$',r'de $Y$, $u\in G$',r'de $Y$, et $u\in G$','At the upper right after Y and its comma a short e-loop and t stroke form et before the following baseline begins with the parameter. H omits this actual conjunction. The parameter itself is separately collated in c10.',6,'high',False,True,'omission','Omissions',mathematical=True)
change('L9, translation parameter in G',r'a\in G',r'u\in G',r'u\in G','The parameter is an open bowl with a returning right limb and no closed a oval. It agrees graphically with the later three translation parameters. The membership sign and capital G are visible on the same line.',6,'high',True,False,'misread symbol or index','Symbols and indices',mathematical=True)
change('L9, translation subscript',r'\tau_aU\subset Y',r'\tau_uU\subset Y',r'\tau_uU\subset Y','Below tau the small parameter has the same open u construction. The following larger U, inclusion sign and Y are distinct. The square bracket beginning the next condition is an independent stroke.',6,'high',True,False,'misread symbol or index','Symbols and indices',mathematical=True)
change('L10, first y map',r'y\longrightarrow y',r'y\mapsto y',r'y\longrightarrow y','The connector has a visible right-pointing head with two branches. Its left end begins as the horizontal shaft, without an upright mapsto bar. The adjacent applications is independently crossed, while morphismes is live above it; both states are preserved.',7,'high',False,True,'misread symbol or index','Symbols and indices',mathematical=True)
change('L11, second y map connector',r'y\longmapsto y+a',r'y\mapsto y+u',r'y\unsure{\mapstochar\relbar|\longmapsto}y+u','A distinct left upright crosses the shaft. At the right end there is only a tiny downward nib, without a securely separable second branch. The leading rendering preserves the left bar and headless shaft; a mapsto arrow remains an explicit alternative. This differs from the plainly headed first y map. The whole map, including its open u parameter, is kept in the audit box.',8,'medium',True,True,'misread symbol or index','Symbols and indices',mathematical=True)
change('L11, parameter added to the second y',r'y+a',r'y+u',r'y+u','After the plus sign the letter is an open low cup with a right return, matching the parameter in G and the tau subscript. There is no closed a loop.',8,'high',True,False,'misread symbol or index','Symbols and indices',mathematical=True)
change('L14, final parameter equation',r'a=0',r'u=0',r'u=0','The first glyph is an open u. Two equality strokes lead to a closed zero oval with retracing; the internal return is not a second numeral. A distinct final stop follows the equation.',9,'high',True,False,'misread symbol or index','Symbols and indices',mathematical=True)
change('L14, short form before the equation',r'i.e.',r'i.e.',r'i.e','A dot is visible between the first short letter and the e. The e finishes with its own upward return, followed by clear blank space before u; there is no independent terminal stop after e. The separate stop after zero remains.',9,'high',True,True,'text not on the page','Abbreviations expanded, spelling modernised')
change('NB margin, initial heading',r'\uline{NB}',r'NB',r'\uline{NB}','A separate short horizontal stroke lies beneath both capital letters. It does not continue into a descender or an insertion leader. H gives the letters but loses this actual underline.',10,'high',False,True,'other','Other')
change('NB margin, after rev.',r'étale',r'\uncertain{ét.}',r'étale','After the accented opening and t upright, the low a and a later separate tall l lead into the terminal e. The word continues beyond the abbreviated ét. proposed by H. The preceding rev. has its own stop and the following fini is separate.',10,'high',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',marked=True)
change('NB margin, word after ouvert',r'(nothing)',r'\uncertain{donné}',r'\unsure{arbitraire}','An extra word is present on its own lower line before de. Its small initial loop, r-like turn, tall b-like stroke and longer dotted/low run favor arbitraire; the middle is crossed by the descender from the row above and cannot all be separated. The extent and ascender sequence do not support a plain donné. The word is restored with localized doubt, not silently completed.',10,'medium',True,True,'omission','Omissions',marked=True)
change('NB margin, terminal marks after pi_1(U)',r'.',r'\ill{}',r'\unsure{. --}','After the closing parenthesis are two detached dark marks: a short point-like stroke and a longer horizontal dash. They are retained as a qualified period-and-dash sequence. No additional word is inferred from H’s illegible placeholder. The exact typographic value of the first short stroke remains open.',10,'medium',True,True,'omission','Omissions',marked=True)
change('L15, after Finalement',r"je m'aperçois que",r'(nothing)',r"je m'aperçois que",'The line continues after Finalement and its comma with je, the m/apostrophe, aperçois and que. The p and ç descenders, dotted i, and final que are present in the long sequence. H omits this clause entirely.',11,'high',False,True,'omission','Omissions')
change('L17, géométrique',r'géométrique',r'\emph{géométrique}',r'géométrique','The low leftward curve joins continuously to the initial g descender. There is no separate baseline below the word. This differs from the independent underline beneath arithmétique on the next line.',12,'high',False,True,'other','Other')
change('L18, punctuation after arithmétique',r'.',r',',r';','Two separate marks follow the word: a short dark upper point and a longer lower comma sweep. Their separation supports a semicolon. The underline itself is a different horizontal stroke beneath the word and is not confused with either mark.',13,'high',True,True,'other','Other')
change('Left lower margin, separator in Si note',r'Si -- cf. plus bas!',r'Si : cf. plus bas !',r'Si -- cf. plus bas!','The separating stroke is horizontal, not a pair of vertically stacked colon points. The cf. abbreviation has its terminal dot. The lower line reads plus bas and ends with an explicit upright and low point forming an exclamation mark. The note is live outside the cancelled paragraph.',14,'high',False,True,'other','Other')
change('Cancelled L19, opening words',r'\unsure{Je ferai}',r'ce qui fournit',r'\unsure{Je ferai}','The first large joined form and the following f stem, low er/a run and short terminal trace favor Je ferai. The heavy upper frame crosses the first word and the f top; the ending is compact. The letters are not all plain, so C’s doubt is retained. No full ce qui fournit sequence can be read in the available ink.',15,'medium',False,True,'misread word','Words')
change('Cancelled L19, independently struck inner word',r'\deleted{\unsure{faible}}',r'\struck{affaibli}',r'\deleted{\unsure{affaibli}}','Two distinct tall f-like stems and descenders precede the smaller a/i run, followed by b/l uprights and a short dotted ending. This favors affaibli over the shorter faible. An independent heavy horizontal stroke masks the body of the word, so its full spelling remains qualified. That inner strike is retained inside the surrounding paragraph cancellation.',16,'medium',True,False,'misread word','Words')
change('Cancelled L19, word before le th.',r'\unsure{généraliser}',r'généralisé',r'\unsure{généraliser|généralisé}','The g loop, two accented vowel positions, middle r/a run and tall l are visible. The compact final s/e/r-like return is not securely separated from an é ending. Généraliser remains first, partly comparable to the terminal return of remplacer in L21, but généralisé is retained as an alternative. No grammatical repair is used.',16,'low',False,True,'misread word','Words')
change('Cancelled L20, verb after on',r'montre',r'notera',r'montre','The word begins with a low multi-humped m run and has its t upright in the middle, followed by the low r/e ending. It is not an initial n followed by the o-t-e-r-a sequence of notera. The adjacent que and opening parenthesis are separate.',17,'high',False,True,'misread word','Words')
change('Cancelled L20–L21, opening parenthetical words',r'(quitte à',r'\ill{}',r'(quitte à','The parenthesis is followed by a q with a long descending stem, the short u/i run and the paired tall t strokes of quitte. The next line begins with à before remplacer. The parenthetical material is legible despite the separate oblique paragraph strokes; c18 continues the same place.',17,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('Cancelled L21, article after par',r'un',r'\ill{}',r'un','After par, two low joined humps form un before the separate ouvert. The diagonal cancellation passes immediately to the left of this word but does not erase its letters. Remplacer and capital X were also read on the same crop.',18,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('Cancelled L21, adjective after non vide',r'connexe',r'convenable',r'connexe','The low succession c-o-n-n-e-x-e has a compact crossing near its end. It has no tall b/l ascenders and is too short for convenable. The small following punctuation remains separately qualified as comma/point rather than being settled by syntax.',19,'high',False,True,'misread word','Words')
change('Cancelled L22, opening clause through pas',r'ce qui ne détruit pas',r'\ill{} \ill{} par',r'ce qui ne détruit pas','The separate ce, q-descender and dotted i in qui, then low ne, accented détruit with its t upright, and p-descender plus low a/s ending of pas survive between the oblique cancellation strokes. The ending of pas has no final r upright/return supporting H’s par.',20,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('Cancelled L22, after les',r'hyp. ni ne modifie',r'\ill{} \ill{} \ill{}',r'hyp. ni ne modifie','The h upright and y/p descenders identify the short hyp. form; ni has its dotted final i, followed by separate ne. The longer modifie run retains its f upright/descender and final dotted i/e run. The oblique paragraph strokes cross these forms but do not obliterate the complete sequence.',20,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('Cancelled L23, conclusion of the parenthesis and short form',r'la conclusion) OPS',r'\ill{}',r'la conclusion) OPS','The faint last row still has la, the low conclusion run, a closing parenthesis, and three separate capital forms O, P and S. OPS is not expanded. The same row continues with que X est une variété to the physical edge; no continuation or final stop is supplied.',21,'high',False,True,r'readable ink left as \ill{}','Readable ink left as illegible',marked=True)
change('Bottom left, thin foliation',r'26',r'(nothing)',r'\margin{26}','A thin 2 with a curved upper entry and long lower return precedes a 6 with a closed lower loop and rising upper arm. It is separate from the author’s upper page number 13. H omits this penned folio.',22,'high',False,True,'omission','Omissions')
assert len(changes)==35

nb=r"\uline{NB} ceci n'est pas plus fort que le corollaire, comme on voit en prenant pour $X$ le rev. étale fini de $U$ correspondant à un sous-groupe ouvert \unsure{arbitraire} de $\pi_1(U)$\unsure{. --}"
last=r"\deleted{\unsure{Je ferai} d'ailleurs \deleted{\unsure{affaibli}} \unsure{généraliser|généralisé} le th. géométrique; on montre que (quitte à remplacer $X$ par un ouvert non vide connexe\unsure{,|.} ce qui ne détruit pas les hyp. ni ne modifie la conclusion) OPS que $X$ est une variété}"
inventory=[]
def inv(el,kind,pos,first,hand='main cursive hand'):
    inventory.append(dict(scan=27,sheet_kind='text',hand=hand,element=el,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
inv('upper page number','text','above the main text, upper centre','13','pen, upper numbering')
inv('opening paragraph','text','main L1–L2',"L'hyp. que")
inv('overwritten conjunction','deletion','L1 between the two fundamental-group terms','et')
inv('conjugation equation','display','main L3',r"\pi_1(j')(\unsure{\sigma|\gamma})")
inv('operator addition','insertion','above the right member of L3',r'\operatorname{int}(\alpha)')
inv('main reduction paragraph','text','main L4–L14','pour tt')
inv('cancelled transition','deletion','main L7 before Donc',"D'ailleurs")
inv('nonempty condition','insertion','above ouvert in main L8',r'\ne\varnothing')
inv('superseded noun','deletion','main L10 after les','applications')
inv('replacement noun','insertion','above applications in main L10','morphismes')
inv('NB note','margin note','slanted left margin beside main L12–L17',r'\uline{NB} ceci n\textquotesingle est')
inv('method paragraph','text','main L15–L18',"Finalement, je m'aperçois que")
inv('Si note','margin note','left margin beside main L18–L21','Si -- cf. plus bas!')
inv('boxed cancelled paragraph','deletion','main L19–L23 to the lower edge',r'\unsure{Je ferai} d\textquotesingle ailleurs')
inv('inner cancelled word','deletion','main L19 inside the cancelled paragraph',r'\unsure{affaibli}')
inv('lower foliation','text','extreme lower left','26','thin pen foliation; identity not established')

abbreviations=[
 dict(form='hyp.',expansion='hypothèse',place='L1, L\'hyp.'),
 dict(form='tt',expansion='tout',place='L4, pour tt before the variable'),
 dict(form='tjrs',expansion='toujours',place='L6, parenthesis'),
 dict(form='i.e',expansion='id est',place='L14, before u=0; no terminal dot supplied'),
 dict(form='NB',expansion='nota bene',place='left margin heading'),
 dict(form='rev.',expansion='revêtement',place='NB margin'),
 dict(form='cf.',expansion='confer',place='Si margin'),
 dict(form='th.',expansion='théorème',place='cancelled L20'),
 dict(form='hyp.',expansion='hypothèses',place='cancelled L22'),
 dict(form='OPS',expansion='on peut supposer',place='cancelled L23')
]

hand=[
 dict(habit='The g descender can turn far left beneath the opening of its own word and resemble an underline.',pages=[27],consistency='Verified in signifie (c02) and géométrique (c12); the separate strokes under NB, ouvert, alors and arithmétique are retained. This is not a rule to remove every underline.',misread='H underlines signifie and géométrique where the apparent stroke belongs to g.'),
 dict(habit='The translation parameter has a low open u bowl with a right return, sometimes v-like.',pages=[27],consistency='Verified in u in G, the tau subscript, y+u, and u=0; all four agree locally.',misread='C reads a in all four parameter positions.'),
 dict(habit='The generic group-element letter has two upper arms and a narrow joined lower oval.',pages=[27],consistency='The three occurrences match, but the local forms do not securely separate sigma from gamma.',misread='C gives sigma and H gamma; all three remain qualified sigma/gamma.'),
 dict(habit='Map endpoints vary on the same page and must be distinguished individually.',pages=[27],consistency='The first y map has a clear head and no left bar; the second has a left bar and only a tiny right nib; the labelled Im connector has a blunt capped shaft.',misread='H supplies a left bar to the first y map; both witnesses supply heads to the other two places.'),
 dict(habit='A heavy equality can overlie the old letters of a conjunction.',pages=[27],consistency='One local occurrence, opening formula; no general correction chronology inferred elsewhere.',misread='C omits the underlying et and treats its curved remainder as a possible isomorphism wave.'),
 dict(habit='Two long f stems survive a heavy inner strike in a cancelled word.',pages=[27],consistency='One local occurrence; the shorter body letters remain masked, so the full affaibli reading stays doubtful.',misread='C’s faible does not account for the two f-like stems visible in c16.'),
 dict(habit='Abbreviation stops are independent ink marks, not automatic parts of an expansion.',pages=[27],consistency='i.e has an internal dot but no final stop; tjrs and OPS are undotted, while hyp., rev., th. and cf. have their written stops.',misread='Both witnesses add a terminal stop to i.e; H shortens the fully written étale to ét..')
]

notation=[
 dict(written=r'\pi_1',rendering=r'\pi_1',meaning='Fundamental-group notation used in this page’s formulas.',evidence='All occurrences inspected, including display, label above the Im shaft, later inline terms and NB margin; the lowered numeral is 1.'),
 dict(written=r"\pi_1(f')\ \deleted{et}\ =\pi_1(g)",rendering=r"$\pi_1(f')$ \deleted{et} $=\pi_1(g)$",meaning='The opening hypothesis as literally written.',evidence='c01: separate raised prime after f, older e/t under two equality bars.'),
 dict(written='two-armed lower-loop letter',rendering=r'\unsure{\sigma|\gamma}',meaning='The generic element in the displayed relation and following quantified image condition.',evidence='c03 and c04: three matching letter forms, with no local contrast decisive enough to remove the alternative.'),
 dict(written=r'\operatorname{int}(\alpha)',rendering=r'\inserted{\operatorname{int}(\alpha)}',meaning='Conjugation operator inserted into the equation.',evidence='c03: raised int(alpha), parentheses, and insertion leader before the second pi_1(j).'),
 dict(written='labelled headless shaft',rendering=r'\overset{\pi_1(f)}{-}',meaning='The literal connector inside the Im expression.',evidence='c04: one shaft with a blunt small terminal cap, unlike the explicit first y arrowhead.'),
 dict(written='left-barred shaft with a tiny right nib',rendering=r'\unsure{\mapstochar\relbar|\longmapsto}',meaning='Connector in the second written point map; head unresolved.',evidence='c08: clear left bar, right end insufficient to separate an arrowhead from a pen return.'),
 dict(written=r'u,\ \tau_u',rendering=r'u,\ \tau_u',meaning='Parameter of the translation written in the reduction.',evidence='c06, c08 and c09: all four parameters have an open u bowl; no closed a loop.'),
 dict(written='unequal sign followed by an obliquely slashed oval',rendering=r'\ne\varnothing',meaning='The added nonempty condition on U.',evidence='c23: two bars with crossing stroke, followed by a narrow closed oval and diagonal slash; both symbols are raised as a live insertion.'),
 dict(written='thin pen 26',rendering=r'\margin{26}',meaning='Physical lower foliation, distinct from the upper author-page number.',evidence='c22: two separate thin digits with a closed lower loop on 6.')
]

doubts=[
 dict(place='Display L3, both argument letters',reading=r'\sigma',alternatives=[r'\gamma'],confidence='low',reason='The upper arms and closed lower oval are clear, but their joining does not uniquely separate sigma and gamma. Whole display audited; first C reading kept with added local uncertainty, not counted as a departure from C.'),
 dict(place='L4, argument before Im',reading=r'\sigma',alternatives=[r'\gamma'],confidence='low',reason='Same local form as the two display arguments. Entire image formula inspected and boxed.'),
 dict(place='L11, second y connector',reading=r'\mapstochar\relbar',alternatives=[r'\longmapsto'],confidence='medium',reason='The left bar is definite, but the tiny downturned right nib does not establish a two-branch arrowhead.'),
 dict(place='NB margin, word after ouvert',reading='arbitraire',alternatives=[],confidence='medium',reason='Initial loop, r turn, b-like ascender and word length favor this reading; an upper descender crosses the middle and the complete letter sequence is not plain.'),
 dict(place='NB margin, terminal punctuation',reading='. --',alternatives=['-- --'],confidence='medium',reason='Two marks are certain, a short point-like stroke and a longer dash; exact interpretation of the shorter mark remains qualified. No additional letters are supplied.'),
 dict(place='Cancelled L19, first words',reading='Je ferai',alternatives=[],confidence='medium',reason='Large initial joined form and following f/low run favor C; upper frame crosses the first letters and the ending is compact. The existing C doubt is retained.'),
 dict(place='Cancelled L19, inner struck word',reading='affaibli',alternatives=[],confidence='medium',reason='Two f-like stems, later b/l forms and a dotted ending favor H, but the heavy inner cancellation masks several body strokes.'),
 dict(place='Cancelled L19, generalized verb ending',reading='généraliser',alternatives=['généralisé'],confidence='low',reason='The final compact return could contain r or finish the preceding vowel. No syntax or expected theorem wording settles it. C’s leading reading remains under doubt.'),
 dict(place='Cancelled L21, punctuation after connexe',reading=',',alternatives=['.'],confidence='medium',reason='The small detached mark is clear but its downward extension is not cleanly separated from nearby cancellation/frame ink. This is a certainty-only qualification of the leading C punctuation.'),
]

audit=[]
def auditbox(kind,box,reading):
    audit.append(dict(box=f'b{len(audit)+1:02}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
auditbox('handwritten number',[772,39,810,75],'13')
auditbox('formula',boxes['1'],r"$\pi_1(f')$ \deleted{et} $=\pi_1(g)$")
auditbox('prose',boxes['2'],'signifie donc')
auditbox('formula',[310,157,1585,260],r'$\alpha\in\pi_1(Y)$')
auditbox('formula',boxes['3'],r"$\pi_1(j')(\unsure{\sigma|\gamma})=\inserted{\operatorname{int}(\alpha)}\pi_1(j)(\unsure{\sigma|\gamma})$")
auditbox('formula',boxes['4'],r'$\unsure{\sigma|\gamma}\in\operatorname{Im}(\pi_1(X)\overset{\pi_1(f)}{-}\pi_1(U))$')
auditbox('prose',boxes['5'],'tjrs vrai')
auditbox('formula',[315,567,665,690],r'$\pi_1(U)$')
auditbox('deletion',[773,674,1075,758],r"\deleted{D'ailleurs}")
auditbox('insertion',boxes['23'],r'\inserted{$\ne\varnothing$}')
auditbox('formula',boxes['6'],r'ramené à ceci: Soit $U$ ouvert de $Y$, et $u\in G$, tels que $\tau_uU\subset Y$ [et tels que')
auditbox('prose',[315,932,1607,1065],r"(désignant par $j,j'$ les \deleted{applications} \inserted{morphismes} $y\longrightarrow y$ et")
auditbox('formula',[318,1065,1045,1205],r'$y\unsure{\mapstochar\relbar|\longmapsto}y+u$ de $U$ dans $Y$)')
auditbox('formula',[1030,1065,1605,1205],r"$\pi_1(j)$ et $\pi_1(j')$")
auditbox('formula',[315,1295,1610,1430],r"groupe ouvert de $\pi_1(U)$] -- \uline{alors} $j=j'$")
auditbox('formula',boxes['9'],r'i.e $u=0$.')
auditbox('margin note',boxes['10'],r'\margin{'+nb+'}')
auditbox('prose',boxes['11'],r"Finalement, je m'aperçois que")
auditbox('prose',boxes['12'],'voie géométrique')
auditbox('prose',boxes['13'],r'\uline{arithmétique};')
auditbox('margin note',boxes['14'],r'\margin{Si -- cf. plus bas!}')
auditbox('deletion',boxes['15'],r"\deleted{\unsure{Je ferai} d'ailleurs}")
auditbox('deletion',boxes['16'],r'\deleted{\deleted{\unsure{affaibli}} \unsure{généraliser|généralisé}}')
auditbox('deletion',[315,2012,1580,2145],r'\deleted{le th. géométrique; on montre que (quitte}')
auditbox('deletion',[317,2094,1650,2240],r'\deleted{à remplacer $X$ par un ouvert non vide connexe\unsure{,|.}}')
auditbox('deletion',boxes['20'],r'\deleted{ce qui ne détruit pas les hyp. ni ne modifie}')
auditbox('deletion',boxes['21'],r'\deleted{la conclusion) OPS que $X$ est une variété}')
auditbox('handwritten number',boxes['22'],r'\margin{26}')

coverage=[]
def diff(row,classification,change_id,reason):
    coverage.append(dict(row=row,classification=classification,change_id=change_id,reason=reason))
diff(1,'editorial-only','',r'C scan metadata versus H editorial pagination prose; source upper 13 is independently retained.')
diff(2,'editorial-only','','Stop belongs to H’s editorial pagination sentence, not the handwritten number.')
diff(3,'material','c01','Raised prime after f is visible; M1054 resolves first, against H’s unprimed f.')
diff(4,'material','c02','Older et survives beneath the equality strokes; C omits it.')
diff(5,'reading-agrees','','The first C relation and H both give equality. M1055 resolves to =; certainty-only removal of the alternative is not an additional substantive row.')
diff(6,'material','c04','First display argument has sigma first with gamma alternative; full equation inspected.')
diff(7,'macro-only','',r'H’s comma token is the TeX thin-space command \, after int(alpha), not an ink comma.')
diff(8,'material','c04','Second display argument matches the first and carries the same local sigma/gamma doubt.')
diff(9,'material','c06','The third letter, before Im, has the same form; whole image formula inspected. The connector departure from both is separately c07.')
diff(10,'material','c08','The actual t/j-descender/r/s sequence reads tjrs, not fait.')
diff(11,'material','c09','Composite row: et is present (c09), and the first parameter is u rather than a (c10).')
diff(12,'material','c11','The low translation subscript is u; the following U is a separate capital.')
diff(13,'material','c12','First map has a right head and no left bar; C retained.')
diff(14,'macro-only','c13',r'The apparent missing C connector is parser loss of \longmapsto; C and H both give headed mapsto forms. Independent crop inspection nevertheless gives the qualified headless barred shaft first; that departure from both is c13.')
diff(15,'material','c14','The translation parameter in the second map is open u.')
diff(16,'macro-only','','C -- and H’s single em-dash character represent the same written dash; no substantive change.')
diff(17,'material','c15','Final equation is u=0, with a real stop after zero. The separate supplied stop after i.e is removed in c16.')
diff(18,'material','c18','Margin spells étale in full; H’s ét. is too short.')
diff(19,'material','c19','An extra word after ouvert is present; arbitraire is favored under localized doubt, against C’s omission and H’s donné.')
diff(20,'material','c20','Two terminal marks are visible after pi_1(U); qualified . -- retained, no invented unreadable word.')
diff(21,'material','c21',"je m'aperçois que is plainly written and omitted by H.")
diff(22,'macro-only','','Different encoding of the same dash after géométrique; the independent false H underline is collated in c22.')
diff(23,'material','c23','Composite row: semicolon after arithmétique is c23; the Si-note separator/state is c24; the cancelled opening Je ferai is c25. H’s different margin placement is editorial ordering, not missing source words.')
diff(24,'material','c26','Nested word favors qualified affaibli (c26); adjacent généraliser/généralisé remains locally doubtful (c27).')
diff(25,'material','c28','Low initial m and middle t support montre, not notera.')
diff(26,'material','c29','Opening parenthesis and quitte à are legible over the row break; H leaves them unread.')
diff(27,'material','c30','Un before ouvert is visible after par, against H’s illegible placeholder.')
diff(28,'material','c31','Connexe is supported by the low run without b/l ascenders (c31); ce qui ne détruit pas is restored from the next row in c32. Following punctuation is retained with a certainty-only comma/point doubt.')
diff(29,'material','c33','The omitted/masked block is read as hyp. ni ne modifie (c33), then la conclusion) OPS (c34). No expansion of OPS is inserted.')
diff(30,'material','c35','Lower handwritten 26 is retained, against H’s omission. The actual Si margin is collated in c24; H’s explanatory note about continuation is editorial and excluded. No later page was read or supplied.')

report=dict(
 scan=27,
 reader='reader_a',
 lines_read=39,
 changes=changes,
 decisions=[
  dict(id='M1054',decision='first',reading="f'",evidence='c01 shows a discrete raised prime after f and before the closing parenthesis. The full opening formula was inspected.',crop='crops/149_scan027_c01.png',box=boxes['1'],confidence='high'),
  dict(id='M1055',decision='first',reading='=',evidence='c01 has two equality bars. The apparent curved extra ink belongs to overwritten et, preserved separately as deleted text; there is no independent clean isomorphism wave.',crop='crops/149_scan027_c01.png',box=boxes['1'],confidence='high')
 ],
 inventory=inventory,
 notes=[
  'First reader: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149. Only scan027 packet, its source/halves, shared instructions and provided notation were consulted. No other page text, second-reading return, OCR, external research or TeX compilation was used.',
  'Reading extent: one whole image for layout, both prepared full-resolution halves once line by line, followed by 23 saved enlarged crops. Existing saved crops were reused for the unresolved NB punctuation and i.e stop; no second crop of a decided place was made. All agreed text, formula indices, underlines, deletion boundaries and insertion attachments were inspected.',
  'Line count 39 = 23 main physical baselines including the displayed equation and five cancelled lower rows, 9 rows of the NB margin, 2 rows of the Si margin, 3 raised insertion rows, and the 2 separate penned number rows. Line labels L1–L23 refer to the main baselines.',
  'The page converts the written equality of fundamental-group maps into a conjugation relation with an inserted int(alpha), then states a reduction involving an open U and a translation parameter u. It states that exterior agreement on an open subgroup should imply j=j\' and u=0. These statements were transcribed, not proved or otherwise checked.',
  'The NB margin says the reduction is no stronger than the corollary and refers to a finite étale covering corresponding to an open subgroup; an extra word after ouvert favors arbitraire but remains qualified. Its two terminal punctuation strokes are preserved as qualified . --.',
  'The next paragraph explicitly says je m\'aperçois que je n\'arrive pas à le prouver par voie géométrique, then turns to an underlined arithmétique method. The live Si -- cf. plus bas! margin sits outside the cancellation. A visible upper point plus lower comma supports the semicolon after arithmétique.',
  'The bottom five-row paragraph is enclosed/cancelled with a frame and oblique strokes. It starts with a qualified Je ferai, contains an independently struck qualified affaibli, and continues with a doubtful generalized-verb ending and a legible parenthetical reduction of X. The faint final row ends at variété at the sheet edge; no continuation or terminal stop is supplied. H’s explanatory continuation note is not source ink.',
  'Upper author-page number 13 and lower thin foliation 26 are both retained. The lower hand is not identified. No date or title occurs on this leaf. No genuine diagram or drawing occurs; the lower frame and diagonals are cancellation apparatus.',
  'No expected mathematics settled a letter or supplied a connector. Sigma/gamma remains unresolved at all three locally matching occurrences. U, Y, j, j\', f\', unprimed f in the label, and translation parameter u were read from their visible forms. The first y map is headed without a left bar; the second has a definite left bar and uncertain right head; the Im map retains a literal shaft.',
  'Both packet marks, M1054 and M1055, are resolved by c01. The additional C doubts inside the cancelled paragraph, although absent from the packet marks table, were all inspected: Je ferai stays doubtful, faible changes to qualified affaibli, and généraliser stays first with généralisé as an explicit alternative.',
  'Certainty-only changes are confined to doubts/evidence: adding sigma/gamma alternatives to C’s sigma, retaining doubt in Je ferai and généraliser, and qualifying the punctuation after connexe do not by themselves count as substantive departures from C. Independent differences from H at those places are still collated.',
  'Audit boxes use neutral category labels. Whole formulas carrying uncertainty are boxed, as are both margins, all three additions, all cancellation material including the inner strike, all C/H different words, all numbered pi occurrences (including the arrow label and NB margin), the zero and both foliation/page numbers. No extra first-pass crop was made solely for the clear upper 13 or clear inline numeral 1s.'
 ],
 checks=[],
 hand=hand,
 notation=notation,
 abbreviations=abbreviations,
 doubts=doubts,
 audit_boxes=audit,
 diff_coverage=coverage
)
(root/'edition/reviews/149_scan027.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Structural checks only; no TeX compilation and no second reading.
assert len(coverage)==30 and [d['row'] for d in coverage]==list(range(1,31))
assert len(report['decisions'])==2
assert all(c['against_C'] or c['against_H'] for c in changes)
assert len({c['id'] for c in changes})==len(changes)
assert len({b['box'] for b in audit})==len(audit)
assert all(0<=b['x0']<b['x1']<=1680 and 0<=b['y0']<b['y1']<=2364 for b in audit)
assert all((root/'edition'/c['crop']).is_file() for c in changes)
assert '\\prime' not in tex
assert tex.count('{')==tex.count('}')
assert report['checks']==[]
print(json.dumps({'scan':27,'changes':len(changes),'decisions':len(report['decisions']),'inventory':len(inventory),'audit_boxes':len(audit),'diff_rows':len(coverage),'lines_read':39,'crops':len(boxes),'files':['edition/reviews/149_scan027.tex','edition/reviews/149_scan027.json']},ensure_ascii=False))
