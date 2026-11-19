from pathlib import Path
from datetime import datetime, timezone
import json, re

BASE=Path('/workspace/scratch/17347c1714f0')
PACKET=BASE/'packets/scan006'
OUT=BASE/'out/readers/scan006/R1'
C=(PACKET/'C.tex').read_text()
H=(PACKET/'H.tex').read_text()
HD=(PACKET/'H_drawing_01-3.tex').read_text()
text=C
replacements={
    r'\unsure{aussi}':'aussi',
    r'\unsure{somme amalgamée}':'somme amalgamée',
    r'\unsure{W|w}':r'\unsure{w|W}',
    r'\unsure{ouvert}':'ouvert',
    r'\unsure{pts}':'pts',
    r'\unsure{imm}':'imm',
    r'\unsure{invariance}':'invariance',
    r'\unsure{remplacement}':'remplacement',
    r'\unsure{pourvu}':'pourvu',
    r'\unsure{vérifier}':'vérifier',
    r'\unsure{précis}':'précis',
    r'\unsure{K\'|\dot K\'}':r'\unsure{\dot K\'|K\'}',
    r'\unsure{div.}':'div.',
    r'\mspage{\unsure{5}}':r'\mspage{5}',
}
# Quotes in the mathematical K-prime alternatives are literal apostrophes.
replacements.pop(r'\unsure{K\'|\dot K\'}')
replacements[r"\unsure{K'|\dot K'}"]=r"\unsure{\dot K'|K'}"
for old,new in replacements.items():
    assert old in text, old
    text=text.replace(old,new)
old=r"$\deleted{\unsure{K^*|K'}}$ soit $K'\supset\bigcup C_i$"
new=r"$\deleted{\unsure{K^*|K'}}\ \operatorname{int}K'\supset\bigcup C_i$"
assert old in text
text=text.replace(old,new)
loop=r'\draw (-1.92,1.36) .. controls (-1.82,1.39) and (-1.55,1.30) .. (-1.60,1.16);'
anchor=r'\draw (0,0) .. controls (.67,.31) and (1.20,.49) .. (1.57,.70);'
assert anchor in text
text=text.replace(anchor,loop+'\n'+anchor)
text=text.replace('% slanted','% slanted left-margin note, three lines in its own orientation')
(OUT/'reading.tex').write_text(text)

crop_list=json.loads((OUT/'crop_manifest.json').read_text())
observations=[
 'Two sweeping curved diagonals are crossed by a long middle stroke. The symbol is the recurrent script X; the ink does not uniquely select mathcal versus mathscr.',
 'Both de endings contain a returned or retraced short final form. A cancelled s remains a plausible reading; the first is marked and the second carries the same uncertainty without a repeated marker. The overbars, coproduct and i in I are visible.',
 'After the parenthesis are a short curved initial form and strongly compressed following strokes. sur remains the best candidate; the pixels do not settle all letters. No ink support for the H expansion via.',
 'Two tall final l strokes and the terminal e form support naturelle. The cancellation crosses and masks the middle letters, so the word remains marked.',
 'A low loop and an upright loop survive under two crossing cancellation strokes. de is plausible but the second letter is not securely separable.',
 'A curved lower return and central curved prong survive beneath the heavier baseline and upright prongs of the live coproduct. A previous union is plausible but not uniquely recoverable.',
 'The parenthesized form has two rounded low turns, unlike the crossed capital W earlier in the same half. Lowercase w is the first candidate; a small capital W remains possible.',
 'The first X has a low two-turn ending without a clean separate dot; w is the best candidate, with i retained because the rightmost rising piece is partly detached. The script X has a small i; parallel strokes and Im X_i are clear. The note reads ouvert de script X, and the arrow curves down-left from beneath the displayed relation.',
 'Six transverse marks are visible: two on the thin upper-left segment, one at the B_3 end of the heavy segment, and one beside each C_3, C_2, C_1. A narrow return loop runs from the upper-left outer join to the first transverse mark. The six B/C labels and their numerals are visible.',
 "An initial c with an apostrophe is followed by a compressed est, then une. This is c'est une, not i.e. une.",
 'A dotted short i precedes two separate low m-like runs. The written abbreviation is imm, without an added expansion.',
 'The prime is distinct. Both raised signs have a peaked body and a short additional stroke, with insufficiently distinct rays to exclude a wedge. The first sign remains star/wedge; the K sign repeats it. The long line below turns to the insertion point after the host formula.',
 "After rotation the three lines read vérifier / l'énoncé / précis followed by three dots. The long f, p descender, accents and final s settle the two C word doubts.",
 'The inserted condition has a separate dot above K, a clear star, a subset sign, an unindexed union, U_i, comma and et. In the cancelled condition a right prime is clear and a dark point above K survives on the cancellation stroke; dotted K prime is preferred, but plain K prime remains possible.',
 'The cancelled parenthesis contains K, a backslash, K prime and the closing parenthesis. At upper right a heavy short horizontal stroke is crossed by a slanted stroke. A raised minus remains the best marked candidate.',
 "The cancelled group preserves a K-like lower skeleton but its upper marks remain entangled. The live word has a dotted i, low n and tall final t: int. The following symbol is K prime, then superset, unindexed union and C_i, with no final full stop.",
 'The freehand numeral has an open angled top and long curved lower return, supporting 5. The separate lower-left dark archival 5 was already seen in the lower half and is not the same mark.'
]
assert len(observations)==len(crop_list)
for cr,obs in zip(crop_list,observations): cr['observed']=obs
(OUT/'crop_manifest.json').write_text(json.dumps(crop_list,ensure_ascii=False,indent=2)+'\n')
crop_by_num={i+1:x['file'] for i,x in enumerate(crop_list)}
findings=[]
def add(place,c,h,reading,*,cd=False,diffc=None,diffh=None,kind='other',marked=False,evidence='',crop=None,confidence='high',unresolved=False,consequential=False):
    if c is not None and c!='':
        assert c in C or c in (PACKET/'C_doubts.md').read_text(), ('C fragment absent',c)
    if h is not None and h!='':
        assert h in H or h in HD, ('H fragment absent',h)
    assert reading=='' or reading in text, ('Reading fragment absent',reading)
    f={'id':f'R1-006-{len(findings)+1:02d}','place':place,'c':c,'h':h,'reading':reading,
       'diff_c':(c!=reading) if diffc is None else diffc,'diff_h':(h!=reading) if diffh is None else diffh,
       'c_doubt':cd,'s_id':None,'kind':kind,'marked_in_H':marked,'evidence':evidence,
       'crop':crop_by_num.get(crop) if crop else None,'confidence':confidence,'unresolved':unresolved,'consequential':consequential}
    findings.append(f)

add('Opening, recurrent script capital',r'\unsure{\mathcal{X}|\mathscr{X}}',r'\mathcal{X}',r'\unsure{\mathcal{X}|\mathscr{X}}',cd=True,diffc=False,diffh=True,kind='misread symbol or index',evidence='Crop 01 shows crossed curved limbs. The plain X at the cancelled arrow target is visibly distinct in half a; font identification remains open.',crop=1,confidence='medium',unresolved=True)
add('Opening phrase, including aussi',r'qui est \unsure{aussi}',r"\uncertain{peut aussi s'identifier à}",r'qui est aussi',cd=True,kind='misread word',marked=True,evidence='Half a: qui has a long q descender; est is a short two-part run; aussi has the initial loop, low successive turns and final short upright. The longer H phrase is not present.')
add('Opening, somme amalgamée',r'\unsure{somme amalgamée}',r'\uncertain{somme amalgamée}',r'somme amalgamée',cd=True,kind='misread word',marked=True,evidence='Half a shows the low s/m runs, the long descending g in amalgamée, and its terminal accented ending.',confidence='medium')
add('First de ending, before barred W',r'de\deleted{\unsure{s}}',r'des $\overline{W}$',r'de\deleted{\unsure{s}}',cd=True,diffc=False,kind='deletion state (struck given live or live given struck)',evidence='Crop 02: the returned final trace is retraced through its end. Cancelled s remains uncertain; H gives it live.',crop=2,confidence='low',unresolved=True)
add('Second de ending, before first coproduct',r'de\deleted{s}',r'des\n$\coprod_{i \in I} \overline{U_i}$'.replace('\\n','\n'),r'de\deleted{s}',diffc=False,kind='deletion state (struck given live or live given struck)',evidence='Crop 02 shows the shorter repeated crossed ending. It carries the first occurrence\'s uncertainty without a new marker.',crop=2,confidence='low',unresolved=True)
add('Opening parenthesis, introductory word',r'\unsure{sur}',r'via',r'\unsure{sur}',cd=True,diffc=False,kind='misread word',evidence='Crop 03 shows the short curved initial and compressed following strokes, compatible with sur; the entire word is not secure.',crop=3,confidence='medium',unresolved=True)
add('Cancelled heading, naturelle',r'\unsure{naturelle}',r'\struck{L\'application naturelle}'.replace("\\'","'"),r'\unsure{naturelle}',cd=True,diffc=False,kind='misread word',evidence='Crop 04 retains the two tall final l strokes and final e; the crossing line conceals the central sequence.',crop=4,confidence='medium',unresolved=True)
add('Cancelled word before script-X to X map',r'\unsure{\text{de}}',None,r'\unsure{\text{de}}',cd=True,diffc=False,kind='omission',evidence='Crop 05: a looped old word survives to the left of the cancelled map. de remains a low-confidence candidate.',crop=5,confidence='low',unresolved=True)
add('Overwritten operator inside main-display parenthesis',r'\deleted{\unsure{\bigcup}}',None,r'\deleted{\unsure{\bigcup}}',cd=True,diffc=False,kind='omission',evidence='Crop 06 shows a lower curved return beneath the live coproduct baseline. The underlying union is retained as uncertain.',crop=6,confidence='low',unresolved=True)
add('Second row of main display, parenthesized letter under coproduct',r'\unsure{W|w}',r'\coprod_{i\,(W)}',r'\unsure{w|W}',cd=True,kind='misread symbol or index',evidence='Crop 07 shows two rounded low turns. They favour w over the earlier crossed capital W, but case cannot be fixed uniquely at this size.',crop=7,confidence='medium',unresolved=True,consequential=True)
add('Right display, first X subscript',r'X_{\unsure{w|i}}',r'X_i \simeq \mathcal{X}_i',r'X_{\unsure{w|i}}',cd=True,diffc=False,kind='misread symbol or index',evidence='Crop 08: two low turns and no clean separate dot favour w. A partly detached last rising piece leaves i possible; no mathematical normalization made.',crop=8,confidence='low',unresolved=True,consequential=True)
add('Arrowed gloss, ouvert',r'\unsure{ouvert}',r'\uncertain{ouvert}',r'ouvert',cd=True,kind='misread word',marked=True,evidence='Crop 08 shows the open initial ou run, low middle strokes and terminal t before de; the whole word reads ouvert.',crop=8,confidence='medium')
add('Drawing, six transverse branch marks',r'\draw (-1.65,1.10)--(-1.58,1.23) (-.90,.60)--(-.88,.66) (-.75,.25)--(-.62,.53)\n (-.34,.07)--(-.26,.26) (.36,.09)--(.29,.25) (-.17,-.34)--(.01,-.32);'.replace('\\n','\n'),None,r'\draw (-1.65,1.10)--(-1.58,1.23) (-.90,.60)--(-.88,.66) (-.75,.25)--(-.62,.53)\n (-.34,.07)--(-.26,.26) (.36,.09)--(.29,.25) (-.17,-.34)--(.01,-.32);'.replace('\\n','\n'),diffc=False,kind='drawing or diagram',evidence='Crop 09 gives two thin-segment ticks, a heavier B3-end cross and three crosses at C3/C2/C1. H drawing source includes all six labels but none of these six transverse paths; its comments acknowledge only the first two missing ticks.',crop=9)
add('Drawing, narrow return loop at upper-left outer join','',None,loop,kind='drawing or diagram',evidence='Crop 09 shows a second short edge returning alongside the first thin interior segment before its first transverse mark. Neither C nor H drawing source contains this return path.',crop=9)
add('Sentence below display, first pts',r'\unsure{pts}',r'pts',r'pts',cd=True,diffh=False,kind='misread word',evidence='Half a: tall p and short raised ts. The second pts near the end of the sentence repeats the same form.')
add('Sentence below display, set difference sign',r'\mathcal X\smallsetminus\coprod_i C_i',r'\mathcal{X} - \coprod_i C_i',r'\mathcal X\smallsetminus\coprod_i C_i',diffc=False,kind='misread symbol or index',evidence='Half a: the mark after script X is a short falling diagonal. Preserved as the smaller set-difference sign; this is not a change of the set-theoretic assertion.')
add('Sentence below display, c\'est une',r"c'est une",r'i.e.\ une',r"c'est une",diffc=False,kind='misread word',evidence='Crop 10 shows c, apostrophe, the compressed est and une. It does not show the separately dotted i.e. of H.',crop=10)
add('Sentence below display, immersion abbreviation',r'\unsure{imm}',r'\ill{}',r'imm',cd=True,kind='readable ink left as \\ill{}',marked=True,evidence='Crop 11: a dotted i followed by two low m-like sequences. No full expansion is written.',crop=11)
add('Sentence below display, fermée',r'fermée',r'\uncertain{fermée}',r'fermée',diffc=False,kind='misread word',marked=True,evidence='Half a shows the long f descender, joined er/m strokes and accented final ending; no unresolved word remains here.')
add('Item 6, Énoncé',r"Énoncé d'",r'\uncertain{Lemme}',r'Énoncé',diffc=False,kind='misread word',marked=True,evidence='Half b begins with a tall accented E followed by noncé. There is no initial L or second m.')
add('Item 6, invariance',r'\unsure{invariance}',r"d'immersion",r'invariance',cd=True,kind='misread word',evidence='Half b has the successive i/n/v forms followed by ariance. The word is long enough and has no mm grouping for immersion.',consequential=True)
add('Item 6, par rapport au remplacement de',r'par rapport au \unsure{remplacement} de',r"\ill{}\n\n\uncertain{remplaçant} au voisinage de".replace('\\n','\n'),r'par rapport au remplacement de',cd=True,kind='misread word',marked=True,evidence='Half b: par ends the first line; rapport au begins the next, followed by a long p-descender/l-ascender sequence and the ment ending of remplacement.')
add('Item 6, interlinear U-prime formula and its small raised marks',r"\inserted{$U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*$}",r"$U'^{*}_i = U'_i \cap K^{*}$",r"\inserted{$U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*$}",cd=True,diffc=False,kind='insertion or placement',evidence='Crop 12 shows the interlinear formula and its leader down to the host-line comma. Prime is distinct. Both small superscripts are peaked with short extra strokes; star and wedge remain possible. The second repeats the first uncertainty without a repeated marker.',crop=12,confidence='medium',unresolved=True,consequential=True)
add('Item 6, pourvu que',r'\unsure{pourvu} que',r'\uncertain{on suppose} que',r'pourvu que',cd=True,kind='misread word',marked=True,evidence='Half b shows the long initial p descender and the low ourvu run, then a separate que with q descender.')
add('Slanted margin note, vérifier',r'\unsure{vérifier}',r'vérifier',r'vérifier',cd=True,diffh=False,kind='misread word',evidence='Crop 13 rotated clockwise: the accented first run, long f and short final ier settle vérifier.',crop=13)
add('Slanted margin note, l\'énoncé',r"l'énoncé",r'\ill{} \ill{}',r"l'énoncé",diffc=False,kind='readable ink left as \\ill{}',marked=True,evidence='Crop 13: looped l, apostrophe, accented e, joined non and final cé are visible in the second of three lines.',crop=13)
add('Slanted margin note, précis',r'\unsure{précis}',r'\ill{} \ill{}',r'précis',cd=True,kind='readable ink left as \\ill{}',marked=True,evidence='Crop 13: long p descender, r, accented short middle sequence and final s, followed by three separate dots.',crop=13)
add('Item 6, cancelled K-prime condition',r"\unsure{K'|\dot K'}",r'\struck{$\dot{K} \subset \bigcup U_i$, et}',r"\unsure{\dot K'|K'}",cd=True,kind='misread symbol or index',evidence='Crop 14: the raised right prime is clear. A dark dot lies above K on the diagonal cancellation stroke; dot K prime is preferred but the dot may be cancellation overtrace.',crop=14,confidence='low',unresolved=True,consequential=True)
add('Item 6, inserted condition includes an unindexed union',r'\inserted{$\dot K^*\subset\bigcup U_i$, et}',r'$\dot{K}^{*} \subset U_i$, et',r'\inserted{$\dot K^*\subset\bigcup U_i$, et}',diffc=False,kind='misread symbol or index',evidence='Crop 14: the inserted line has separate dotted K, star, subset and large union before U_i, followed by comma et. H loses the union and does not encode the insertion state.',crop=14,consequential=True)
add('Item 6, cancelled parenthesis and raised final mark',r"\deleted{(K\smallsetminus K')^{\unsure{-}}}",r"\struck{$(K \setminus K')$}",r"\deleted{(K\smallsetminus K')^{\unsure{-}}}",cd=True,diffc=False,kind='omission',evidence='Crop 15 shows the right parenthesis and an additional short raised horizontal mark under an oblique strike. Minus remains the candidate; no additional equality is inferred.',crop=15,confidence='low',unresolved=True)
add('Item 6, live universal quantifier after cancellation',r'\forall i',r'= V_i',r'\forall i',diffc=False,kind='misread symbol or index',evidence='Half b: two rising legs joined at their lower turn and a cross-stroke form the universal quantifier; the following dotted i is separate.',consequential=True)
add('Item 6, short dash immediately after opening parenthesis',r'(- il suffit que',r'(il suffit que',r'(- il suffit que',diffc=False,kind='omission',evidence='Half b shows a distinct short horizontal dash after the opening parenthesis and before il.')
add('Item 6, cancelled K group after il suffit que',r'\unsure{K^*|K\'}'.replace("\\'","'"),r'\struck{\ill{}}',r'\unsure{K^*|K\'}'.replace("\\'","'"),cd=True,diffc=False,kind='readable ink left as \\ill{}',marked=True,evidence='Crop 16 preserves a K-like lower framework while upper angular marks are tangled with the zigzag cancellation. K star and K prime remain candidates.',crop=16,confidence='low',unresolved=True)
add('Item 6, live word before K prime',r"soit $K'",r"$\operatorname{int} K'",r"\operatorname{int}K'",diffc=True,diffh=False,kind='misread word',evidence='Crop 16 shows a separate dotted i, a low joined n and a tall final t with a leftward cross-stroke. It reads int, agreeing with H; C\'s soit is overturned by these strokes.',crop=16,consequential=True)
add('End of item 6 sufficiency line, final punctuation','',r"\bigcup C_i$.",'',diffc=False,diffh=True,kind='text not on the page',evidence='Crop 16 and half b: after the final C_i there is no full stop or closing parenthesis. The high dot belongs to i.',crop=16)
add('Bottom verification paragraph, div. hypothèses',r'\unsure{div.} hypothèses',r'développements',r'div. hypothèses',cd=True,kind='abbreviation expanded or spelling modernised',evidence='Half b shows a short d-i-v group with a point, followed by the distinct h/y/p opening and long ending of hypothèses.')
pen=r'\margin{\tikz{\draw[line width=.3pt] (0,0) .. controls (-.04,.25) and (-.05,.6) .. (0,.9);}}'
add('Independent pen stroke left of final line',pen,None,pen,diffc=False,kind='drawing or diagram',evidence='Half b: a single long slightly bowed vertical stroke stands to the left of d\'exiger, independent of the nearby page numeral.')
add('Own page number above the separate archival 5',r'\mspage{\unsure{5}}',r'\page{5}',r'\mspage{5}',cd=True,diffh=False,kind='other',evidence='Crop 17 supports a long freehand 5 with angled open top and curved lower return. The darker archival 5 is separate and remains comment-only.',crop=17,confidence='medium')

inventory=[]
def inv(kind,position,words):
    inventory.append({'scan':6,'sheet_kind':'text','hand':'his hand','element':f'006-R1-{len(inventory)+1:02d}','kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('text','opening two lines above drawing','script X qui est aussi la somme amalgamée')
inv('deletion','opening, first de ending before barred W','cancelled s, uncertain')
inv('deletion','opening, second de ending before coproduct','cancelled s, repeated unresolved form')
inv('diagram','upper right inside parenthesis','coproduct B_i with horizontal hooked arrow to barred W and down-right arrow to coproduct barred U_i')
inv('drawing','upper-left quadrant','three outer lobes, thin Y, heavy central Y, six transverse marks, short return loop, B_3/C_3/B_2/C_2/C_1/B_1 and K')
inv('deletion','upper right, first struck line',"L'application naturelle")
inv('deletion','upper right, second struck line','de, uncertain, and script X to plain X')
inv('display','right of drawing, two-line construction','script X isomorphic to barred W amalgamated over coproduct B_i with coproduct barred U_i; coproduct X_i with i and (w/W)')
inv('deletion','main construction, operator inside parentheses','possible union overwritten by coproduct')
inv('display','right of second construction line','X_(w/i) isomorphic to script X_i; two vertical strokes; Im X_i')
inv('margin note','beneath right-hand display, curved arrow down-left','ouvert de script X')
inv('text','three lines below construction and right of drawing','script X to X est étale en les pts; closed immersion along coproduct C_i')
inv('text','lower half, item 6 first three lines',"Énoncé d'invariance de script X par rapport au remplacement")
inv('insertion','interlinear above end of replacement formula','U prime_i with star/wedge equals U prime_i intersect K with same small mark')
inv('margin note','left of item 6, slanted in three lines',"vérifier / l'énoncé / précis…")
inv('deletion','item 6, first condition on original line','dot K prime / K prime subset union U_i, et')
inv('insertion','above cancelled first condition','dot K star subset union U_i, et')
inv('deletion','item 6 before universal quantifier','(K setminus K prime) with uncertain raised minus')
inv('text','item 6 remaining condition and sufficiency parenthesis','for all i, C_i subset the two starred U closures; (- il suffit que; int K prime superset union C_i')
inv('deletion','after il suffit que','K star or K prime under zigzag cancellation')
inv('text','bottom three lines','vérifier si dans les div. hypothèses précédentes; union C_i subset int K; C_i intersect dot K equals empty for every i in I')
inv('drawing','left of final body line','single bowed vertical pen stroke')
inv('text','lower left, above archive number','freehand page 5')

# Doubt strings are exactly the affected TeX substrings in reading.tex.
doubts=[]
def doubt(place,reading,alternatives,confidence,reason):
    assert reading in text
    doubts.append({'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason})
doubt('Opening, recurrent script X',r'\unsure{\mathcal{X}|\mathscr{X}}',r'\mathscr{X}','medium','Curved crossed capital is certain; no unique typographic face follows from the strokes. Later same script is unmarked.')
doubt('Opening first de ending',r'de\deleted{\unsure{s}}','No secure second letter candidate','low','Return trace and overstrike preserve only part of the presumed s.')
doubt('Opening second de ending',r'de\deleted{s}','Same unresolved s identification as the first occurrence','low','Unmarked repetition does not increase confidence.')
doubt('Opening parenthesis',r'\unsure{sur}','No secure alternative word','medium','Highly compressed following strokes do not securely separate u and r.')
doubt('Cancelled heading',r'\unsure{naturelle}','No secure alternative word','medium','Central sequence coincides with strike line.')
doubt('Cancelled word before map',r'\unsure{\text{de}}','No secure alternative word','low','Looped trace is crowded by two cancellation strokes.')
doubt('Overwritten main-display operator',r'\deleted{\unsure{\bigcup}}','No secure second operator candidate','low','Curved remnants suggest a union but cannot reconstruct its complete old outline.')
doubt('Main coproduct parenthesis',r'\unsure{w|W}',r'W','medium','Small rounded double trough favours w; case remains unresolved.')
doubt('Right display first subscript',r'X_{\unsure{w|i}}',r'i','low','Low double turn favours w, but partly detached last rising stroke leaves i possible.')
doubt('Inserted U-prime superscript',r"U_i'{}^{\unsure{*|\wedge}}",r'\wedge','medium','Peaked form has too few distinct rays to force a star.')
doubt('Repeated small superscript on K in the inserted formula',r"U'_i\cap K^*",r'K^{\wedge}','medium','Same unresolved small glyph as on the immediately preceding U prime; later unmarked repetition is not confirmation.')
doubt('Cancelled first condition',r"\unsure{\dot K'|K'}",r"K'",'low','Right prime survives; dark point above K may belong to the cancellation overtrace.')
doubt('Cancelled parenthesis final raised mark',r"\deleted{(K\smallsetminus K')^{\unsure{-}}}",'No secure second mathematical sign candidate','low','Short horizontal mark is intersected by a diagonal cancellation stroke.')
doubt('Cancelled K group after il suffit que',r"\unsure{K^*|K'}",r"K'",'low','K-like lower skeleton survives but upper marks do not separate star from prime.')

notes=[
 'The page continues a construction of script X as the amalgamated sum of barred W and the coproduct of barred U_i along the coproduct of B_i. A two-arrow span is drawn above a three-lobed example labelled K, B_1/B_2/B_3 and C_1/C_2/C_3.',
 'The main display also identifies script X with a coproduct of X_i, carrying the uncertain parenthesized letter w/W beneath the coproduct. At the right, X_(w/i) is related to script X_i, which is identified vertically with Im X_i and glossed as ouvert de script X. These are statements of the page, not proved here.',
 'The page states that script X to X is étale at the points of script X outside the coproduct of C_i and is an imm fermée at the points of the coproduct of C_i.',
 'Item 6 requests an Énoncé d\'invariance under replacing K by K star subset K and replacing U_i and U prime_i by their intersections with K star. Its edited conditions include dot K star subset union U_i and, for every i, C_i contained in the intersection of the closures of the two starred U sets. The parenthetical sufficiency phrase reads int K prime superset union C_i; the written prime is retained and the parenthesis remains open.',
 "The slanted self-instruction is vérifier l'énoncé précis… . The final paragraph asks whether the preceding div. hypothèses should have required union C_i subset int K, followed by i.e. C_i intersect dot K equals the empty set for every i in I. It remains a verification request on the page.",
 'The own page numeral reads 5. A separate darker archival 5 appears in the corner. There is no date or title on this scan.'
]
checks=[
 {'statement_id':'006-claim-01','type':'carried as background without fault found','statement':'The amalgamated-sum and coproduct identifications for script X.','outcome':'Read visually and compared with both witnesses. No proof was attempted: the spaces and gluing maps are not defined on this page alone. The uncertain parenthesized index was preserved.'},
 {'statement_id':'006-claim-02','type':'carried as background without fault found','statement':'The right-hand identification with Im X_i and its open-subspace gloss.','outcome':'No mathematical verification was attempted. The ambiguous first subscript remains w/i; the open-subspace wording was read from the ink.'},
 {'statement_id':'006-claim-03','type':'carried as background without fault found','statement':'The map is étale outside the coproduct of C_i and a closed immersion along it.','outcome':'Carried as the page\'s assertion. No definitions or local morphism calculation were supplied on this scan, and no proof claim is made.'},
 {'statement_id':'006-claim-04','type':'carried as background without fault found','statement':'Invariance under replacement by K star with the edited conditions and the parenthetical sufficient condition.','outcome':'No invariance proof was attempted. The page itself asks to verify the precise statement. Live K prime in the sufficient condition was not changed to K star.'},
 {'statement_id':'006-claim-05','type':'carried as background without fault found','statement':'The final proposed equivalence between union C_i subset int K and C_i intersect dot K empty for every i.','outcome':'Read as the author\'s i.e. statement and verification question, without asserting a re-proof. The page-local definitions needed to interpret dot K and ambient containment are not independently available.'}
]
notation=[
 {'sign':'recurrent script X','tex':r'\mathcal X','place':'opening, cancelled and live maps, displays, gloss and item 6','ink':'Two curved crossing limbs with a long middle stroke; the plain X is drawn with two straighter diagonals.','alternatives':r'\mathscr X; unresolved, marked at first occurrence'},
 {'sign':'barred W and U','tex':r'\overline W,\overline U_i','place':'opening span and main display','ink':'Long separate horizontal overmarks. Capital W has crossing inner strokes.','alternatives':''},
 {'sign':'coproduct and amalgamation','tex':r'\coprod_i,\amalg','place':'opening, main construction and map sentence','ink':'Two legs on a common horizontal foot; low dotted i.','alternatives':''},
 {'sign':'parenthesized small w/W','tex':r'\unsure{w|W}','place':'under the final coproduct in the main construction','ink':'Two rounded low troughs; unlike the earlier crossed full-size W.','alternatives':'W; unresolved'},
 {'sign':'right-display subscript','tex':r'X_{\unsure{w|i}}','place':'first X of the right-hand display','ink':'Low returning two-turn form; no clean independent dot.','alternatives':'i; unresolved'},
 {'sign':'isomorphism and vertical identity','tex':r'\simeq,\shortparallel','place':'main and side displays','ink':'A small wave over a bar; beneath script X_i are two short uprights.','alternatives':''},
 {'sign':'prime, star and small interlinear superscript','tex':r"U'_i,U_i^*,U_i'{}^{\unsure{*|\wedge}},K'",'place':'item 6','ink':'Prime is one slanted or upright stroke; large stars have several rays. The two interlinear superscripts are peaked with short extra strokes.','alternatives':r'\wedge for each of the two small superscripts; unresolved even at the unmarked K repetition'},
 {'sign':'dotted K','tex':r'\dot K^*','place':'inserted first replacement condition and final line','ink':'A dark point is separate above the K in the inserted and final live conditions.','alternatives':r"The cancelled earlier K prime retains \dot K'|K' uncertainty."},
 {'sign':'empty set','tex':r'\varnothing','place':'bottom line','ink':'A small oval crossed by a long falling slash extending below the baseline.','alternatives':''},
 {'sign':'int abbreviation','tex':r'\operatorname{int}K\' '.rstrip().replace("\\'","'"),'place':'after cancelled K group in sufficiency line','ink':'Dotted i, low n and tall t with a leftward cross-stroke; followed by K prime.','alternatives':''},
 {'sign':'repeated cancelled s','tex':r'de\deleted{\unsure{s}}; de\deleted{s}','place':'both opening de endings','ink':'A returned or retraced terminal trace after e.','alternatives':'Identity of s remains unresolved at both occurrences.'}
]
abbreviations=[
 {'written':'pts','expansion':'points'},
 {'written':'imm','expansion':'immersion'},
 {'written':'Im','expansion':'image'},
 {'written':'div.','expansion':'diverses'},
 {'written':'int','expansion':'intérieur'},
 {'written':'i.e.','expansion':'id est'}
]
report={
 'scan':6,'reader':'R1','model':'inherited parent model','effort':'inherited; value not independently exposed',
 'started_utc':'2026-11-19T22:18:08.192977Z','finished_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
 'timing_note':'The start field is the first recorded clock timestamp, taken after the required whole-page and half-page views; the reading session began shortly before it.',
 'images_viewed':[str(BASE/'source/SP36_CW_71_scans'/n) for n in ['J71-01_71_scan006.jpg','J71-01_71_scan006_a.jpg','J71-01_71_scan006_b.jpg']],
 'image_view_counts':{'whole':1,'half_a':1,'half_b':1,'each_saved_crop':1},
 'crops':crop_list,'findings':findings,'inventory':inventory,'doubts':doubts,'notes':notes,'checks':checks,'notation':notation,'abbreviations':abbreviations,
 's_decisions':[],
 's_note':'S.json is an empty array; no S rows were supplied for this scan.',
 'comparison_notes':['Read the complete supplied C and H page texts and H drawing source. H\'s drawing includes B_1/B_2/B_3, C_1/C_2/C_3 and K; these were not reported as omissions.','The two-arrow opening span has the same mathematical objects and maps in H\'s inline encoding, so no purely macro-level discrepancy is claimed.','All agreed portions of the text, formulas, diagram and drawing were checked in the required halves. No OCR, outside source, other page, other reader output, rendering or compilation was used.'],
 'brief_feedback':['No procedural ambiguity blocked this reading. The image-time field is explicitly qualified because no clock was recorded before the first image view.']
}
assert sum(f['c_doubt'] for f in findings)==24, sum(f['c_doubt'] for f in findings)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Saved reading.tex and report.json')
print('Findings:',len(findings),'C doubts:',sum(f['c_doubt'] for f in findings),'remaining doubt entries:',len(doubts),'inventory blocks:',len(inventory))
