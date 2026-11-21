from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/8759b8008681')
OUT = ROOT / 'work/reports/150_scan024'
PACKET = ROOT / 'packets/150_scan024'
PAGE = '150_scan024'
boxes = json.loads((OUT / 'crop_boxes.json').read_text())
draft = (OUT / 'draft.tex').read_text()
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()

report = dict(page=PAGE, reader='reader_a', line_count=0, changes=[], decisions=[],
              inventory=[], audit_boxes=[], doubts=[], notes=[], check_events=[],
              notation=[], abbreviations=[], hand=[], diff_coverage=[],
              deletion_insertion_review=[])

categories = {
    'misread symbol or index': '1 Symbols and indices',
    'misread word': '2 Words',
    'omission': '3 Omissions',
    'drawing or diagram': '4 Drawings and diagrams',
    'readable ink left as \\ill{}': '5 Readable ink left as illegible',
    'insertion or placement': '6 Insertions put in wrong place',
    'deletion state (struck given live or live given struck)': '7 Struck text',
    'abbreviation expanded or spelling modernised': '8 Abbreviations expanded or spelling modernised',
    'text not on the page': '9 Text not on page',
    'other': '10 Other',
}

def change(id, p, place, c, h, final, evidence, kind, ac, ah,
           confidence='high', consequential=False, marked=False, fragments=None):
    row = dict(id=id, place=place, c=c, h=h, final=final, evidence=evidence,
               crop=f'crops/{PAGE}_{p}.png', box=boxes[p], confidence=confidence,
               kind=kind, against_c=ac, against_h=ah, marked_in_h=marked,
               consequential=consequential, error_category=categories[kind])
    if fragments:
        row['final_fragments'] = fragments
        row['representation_note'] = 'The final expression is the semantic reading of separate typeset diagram cells/relations; fragments identify its exact components in draft.tex.'
    report['changes'].append(row)

change('P04_a','P04','Corollary: the baseline fermées after de parties',
       r'de parties fermées de $\widetilde X$ et de $Y$',
       r'de parties \struck{fermées} fermées de $\tilde X$ et de $Y$',
       r'de parties fermées de $\widetilde X$ et de $Y$',
       'There is one tall f followed by one connected ermées body. Retracing does not supply a second word or an independent cancellation. H duplicates the word and invents a struck instance.',
       'text not on the page',False,True)

change('P05_a','P05','Condition a): lower interlinear qualification and its punctuation',
       r'\inserted{de $\widetilde X,\dot X$}',
       r'structure cylindrique de $\tilde X,\dot X$ ;',
       r'\inserted{de $\widetilde X,\dot X$}',
       'The smaller de and two X forms occupy an interlinear row below the cylindrical-structure phrase and attach to a), not b). The dot over the final X is a filled upper point, not a terminal semicolon; no separate final punctuation is present.',
       'insertion or placement',False,True)

change('P06_a','P06','Condition b): crossed variable immediately after applique',
       r'\deleted{$\unsure{\widetilde X\'}$}'.replace("\\'", "'"),
       r'\struck{\ill{}}',
       r'\deleted{$\unsure{\widetilde X\'}$}'.replace("\\'", "'"),
       'The crossed group has X diagonals and an upper tilde-like stroke; the prime/retracing is not independently secure. A doubtful tilde-X-prime reading is retained, rather than H’s entirely illegible placeholder. C’s doubt is not resolved.',
       'readable ink left as \\ill{}',False,True,'medium',marked=True)

change('P06_b','P06','Condition b): label over defining equality',
       r'\overset{\mathrm{def}}=',r'\overset{\text{déf}}{=}',
       r'\overset{\text{déf}}{=}',
       'A small separate oblique accent is visible above the e, independent of the d ascender and f. The written label is déf.',
       'misread word',True,False)

image_formula = r"X'=\underbrace{\operatorname{Im}(\widetilde X'\ \text{par}\ \widetilde X\to X)}_{\overline{X'\setminus\underbrace{Y\cap X'}_{Y'}}}\cup Y'"
change('P07_a','P07','On aura: whole image expression, upper brace, closure bar, nested brace',
       r"X'=\operatorname{Im}\underbrace{(\widetilde X'\ \text{par}\ \widetilde X\to X)}_{\overline{X'\setminus\underbrace{Y\cap X'}_{Y'}}}\cup Y'.",
       r"X'=\underbrace{\mathrm{Im}\,(\tilde X'\ \text{par}\ \tilde X\to X)}_{X'\setminus Y\cap X'}\cup Y'",
       image_formula,
       'The upper brace starts below the right half of Im’s m and continues under the parenthesized image argument: attachment to the whole image expression is preferred, with its imperfect left alignment recorded. A separate long bar spans the lower X-prime-minus-intersection expression. A small nested brace sits under Y intersection X-prime and is labelled Y-prime. No terminal point follows the outer Y-prime. C attaches the upper brace to the parentheses alone and adds a point; H omits the closure bar from the formula but mentions the nested brace editorially.',
       'insertion or placement',True,True,'medium',True)

change('P08_a','P08','Pour que: the old underlined abbreviated strict word',
       r'\deleted{\uline{strict.} compatible avec}',
       r'\struck{strictement compatible avec}',
       r'\deleted{\uline{strict\unsure{.}} compatible avec}',
       'The word ends after the tall t, without the additional ement sequence supplied by H. The underline is separate from the long cancellation through strict, compatible and avec. The putative abbreviation point is crossed/merged, so only that punctuation remains doubtful; the preferred abbreviation is not changed against C.',
       'abbreviation expanded or spelling modernised',False,True,'medium',True)

change('P08_b','P08','Pour que: raised live replacement cônique strict',
       r'\inserted{cônique \uline{\unsure{strict}}}',
       r'\add{cônique strict}',
       r'\inserted{cônique \uline{strict}}',
       'The raised s, t ascent, r shoulder, dotted i, c bowl and final t read strict; its single lower emphasis stroke is independent of the old cancellation. C M0359 is resolved to its first reading at medium confidence. Cônique has a separate circumflex. H omits the strict underline, a source emphasis difference rather than a macro substitution.',
       'other',True,True,'medium',True)

change('P09_a','P09','Cancelled lower clause and cancelled raised word: article and attachment',
       r'\deleted{\inserted{\unsure{purement}} la structure cônique}',
       r'\struck{le germe de structure cônique}',
       r'\deleted{\unsure{la|le} \inserted{\unsure{purement|germe de}} structure cônique}',
       'Two long strokes cross the entire old article–structure–cônique clause. The bent leader from the raised word lands after the old article and before structure, unlike C’s placement before la. Its descending first letter favours purement but overlaps permit germe de; the article’s a/e is covered. No further revision chronology is imposed. A long vertical from the que above is excluded from the raised word’s letters.',
       'insertion or placement',True,True,'medium',True,True)

change('P10_a','P10','Abbreviated necessity/sufficiency clause',
       'il f. et s. que','il faut et suffit que','il f et. s. que',
       'The f has a tall loop/descender but no independent following point. Two isolated dots follow et and s respectively. The abbreviated letters and displaced punctuation are literal; H expands faut and suffit.',
       'abbreviation expanded or spelling modernised',True,True,consequential=True)

change('P10_b','P10','Terminal image equality after il f et. s. que',
       r"$Y'=\operatorname{Im}(\dot X'\to Y)$",
       r"$Y'=\mathrm{Im}\,(\dot X'\to Y)$.",
       r"$Y'=\operatorname{Im}(\dot X'\to Y)$",
       'The final right parenthesis is followed by bare paper to the edge; there is no separate terminal point. All dots/primes internal to the image expression are retained.',
       'text not on the page',False,True)

change('P12_a','P12','Compatibility definition: conique before calligraphic T',
       r'avec le germe de structure cônique $\mathcal T$',
       r'avec le germe de structure cônique $\mathcal T$',
       r'avec le germe de structure conique $\mathcal T$',
       'No independent accent stands over the o in this occurrence. The separate upper point belongs to the later i. Both witnesses supply the circumflex from spelling or neighbouring occurrences; the local unaccented form is preserved.',
       'misread word',True,True)

upper_margin = r"au lieu de ``compatible'' il est plus parlant de dire ``\uline{transversal}''"
change('P13_a','P13','Whole upper slanted terminology margin',
       r"au lieu de ``compatible'' il \unsure{est} plus \unsure{parlant} de dire ``\uline{transversal}''.",
       r'on dira aussi « $E$ est compatible » ou « \ill{} \ill{} » \ldots',
       upper_margin,
       'The start reads au lieu de: the following quoted compatible is continuous with it. Est has a low e/s run and a rising terminal t; parlant has a long p descender, a/r, tall looped l and ending nt. These resolve M0360 and M0361 to the first readings, medium. Paired upper ticks enclose the two quoted words; transversal has one underline. No terminal point is visible. Large upright marks at the right/bottom are main-text spillover, not additional margin words.',
       'misread word',True,True,'medium',True,True)

change('P14_a','P14','Inserted product representative after E: weight of interval I',
       r'\inserted{\simeq X_0\times I}',
       r'\add{$\simeq X_0\times\mathbf{I}$}',
       r'\inserted{\simeq X_0\times\mathbf I}',
       'The inserted interval symbol has a filled heavy stem and broad serifs, in contrast to the thin serif I forms in the bottom diagram. The product sign has two intersecting strokes, and the X has a separate lowered round zero.',
       'misread symbol or index',True,False)

change('P15_a','P15','Parenthetical structure: inserted sa',
       r'(avec \inserted{sa} structure cônique)',
       '(avec structure cônique)',
       r'(avec \inserted{sa} structure cônique)',
       'The tiny raised s curve is followed by an a with a right foot; its leader lands directly before structure. Both cônique occurrences in this row have separate accents. H omits the insertion.',
       'omission',False,True)

change('P16_a','P16','Lower a): first whole intersection',
       r'\overline T\cap E',r'T\cap E',r'T\cap\unsure{\overline E|E}',
       'The T has one thick cap and its stem, with no separate upper bar: plain T is preferred confidently against C. The E has a detached-looking high curved stroke, but its distinction from E’s upper arm is not fully separable; barred E is the local preferred reading with plain E retained. This is a preferred-symbol departure against both witnesses, not a change logged merely for added uncertainty.',
       'misread symbol or index',True,True,'medium',True)

change('P16_b','P16','Lower a): third whole intersection',
       r'Y\cap E',r'Y\cap E',r'Y\cap\unsure{\overline E|E}',
       'Above this E is a short detached-looking mark, distinct-looking but not securely separable from the upper arm. Barred E is preferred locally with plain E retained. The middle intersection’s E has only its ordinary three arms and stays plain.',
       'misread symbol or index',True,True,'medium',True)

change('P16_c','P16','Lower a): crossed short compat form',
       r'\deleted{\unsure{compat.}}',r'\struck{compatible}',r'\deleted{\unsure{compat.}}',
       'The crossed word stops after the compat-like short body; there is no separately written ible ending. The last stroke/point is obscured by the cancellation, so C’s local abbreviation doubt stays unresolved rather than being expanded as H does.',
       'abbreviation expanded or spelling modernised',False,True,'medium')

change('P16_d','P16','End of live a) row, before the cancelled homothety draft',
       'des parties cylindriques de',r'des parties cylindriques \struck{et',
       'des parties cylindriques de',
       'The baseline ends in d with an ascender and a following e, not et. Only soient is raised above the old crossed compat form; des parties cylindriques de lies on the main baseline. H attaches a different conjunction to the cancelled block.',
       'misread word',False,True,consequential=True)

change('P17_a','P17','Cancelled homothety row: first whole intersection',
       r'\unsure{\overline E}\cap\overline T',r'E\cap T',
       r'\unsure{\overline E|E}\cap\unsure{\overline T|T}',
       'The upper marks over both capitals overlap the long horizontal cancellation and neighbouring ink. Barred E/barred T remain the preferred local candidates, with plain alternatives explicitly retained; C’s barred-E doubt is not resolved. H’s plain pair differs from these preferred readings.',
       'misread symbol or index',False,True,'low',True)

first_map = r'\unsure{\overline x|x}\mapsto\unsure{\lambda x}_{X_0}'
change('P18_a','P18','Cancelled homothety row: first whole map and lowered X0',
       r'\unsure{\overline x}\mapsto\unsure{\lambda x}_{X_0}',r'x\mapsto\lambda.x',
       first_map,
       'The initial small x has a separate short high mark, bar preferred but not secure under the strike. The first shaft has a tail-like vertical and a covered head. The lambda-x target remains overworked; its lowered X with a round zero is separately visible beneath the whole group. No independent multiplication point occurs between lambda and x, unlike H.',
       'misread symbol or index',False,True,'low',True)

second_map = r't\unsure{\longrightarrow|\mapsto}\unsure{\lambda_Y\times t|\lambda\times_Y t}'
change('P18_b','P18','Cancelled homothety row: second whole map',
       r't\mapsto\lambda\times_Y t','[not transcribed]',second_map,
       'After the initial t is a long shaft; no independent left tail is secure and the right head is crossed by a diagonal, so an ordinary arrow is preferred with mapsto retained. The product sign has two separate crossing strokes, not a point. The lowered Y lies between lambda and the cross, nearer lambda, so attachment to lambda is preferred but attachment to the product sign remains open. The terminal t is also crossed. H omits this second map.',
       'misread symbol or index',True,True,'low',True)

old_tail = r"\unsure{qui|que} \unsure{agissent} \unsure{de part et d'autre}"
change('P18_c','P18','Cancelled words after the two maps',
       r"qui \unsure{agissent} \unsure{de part et d'autre}",r'que celles \ill{}',old_tail,
       'The first word has a q descender; its final i/e overlaps neighbouring diagram/prose ink, so qui is preferred but que remains possible. The following tall/short runs support C’s agissent and de part et d’autre candidates, but the long strike obscures individual letters. Those C doubts remain unresolved. H’s celles is not supported by a distinct initial c plus full elles sequence.',
       'misread word',False,True,'low',True,True)

change('P20_a','P20','E i.e. immediately before the diagram',
       '$E$ i.e.','« i.e. »',r'\deleted{$E$ i.e.}',
       'The first long diagonal passes through the E, and the phrase belongs to the globally cancelled lower draft. C leaves it live; H’s editorial quotation gives only i.e. and omits this E. The source’s running text is transcribed separately, not drawn inside the diagram.',
       'deletion state (struck given live or live given struck)',True,True,'medium',True)

change('P20_b','P20','Diagram: upper row E identified with X0 times I',
       'E \\arrow[r,phantom,"\\simeq"] & X_0\\times I',
       r'$T\cap E\simeq T_0\times\mathbf{I}$',
       r'E\simeq X_0\times I',
       'The actual upper row has a standalone three-arm E, a wavy identification over a short lower bar, and X with a lowered round zero followed by a crossing product and thin serif I. There is no additional plain-T-intersection row of the form H’s editorial reconstruction supplies. The upper E has no independent fourth upper stroke; only the lower two E forms retain local bar alternatives.',
       'drawing or diagram',False,True,consequential=True,
       fragments=['|[alias=pA]| E',r'\simeq',r'X_0\times I'])

change('P20_c','P20','Diagram: middle left dotted T intersection',
       r'\unsure{\dot T|\overline T}\cap E',r'\dot T\cap E',
       r'\dot T\cap\unsure{E|\overline E}',
       'A filled independent point sits above the one-cap T: C’s dot/bar doubt is resolved to dot T. The E has three horizontal arms in total, including its high detached-looking arm; no fourth bar is established. Plain E is preferred with a bar alternative retained locally. H’s preferred dot-T/plain-E reading agrees.',
       'misread symbol or index',True,False,'medium',True)

change('P20_d','P20','Diagram: middle product target',
       r'\overline T_0\times I',r'\dot T_0\times\mathbf{I}',r'T_0\times I',
       'The T has one curved cap and a lowered round zero, with no separate bar or dot. Its I has a thin stem with serifs, unlike the earlier heavy inserted I. Thus the product is plain T0 times thin I.',
       'misread symbol or index',True,True,consequential=True)

change('P20_e','P20','Diagram: definition to the right of the middle row',
       r'\overline T_0=X_0\cap\overline T',r'T_0=X_0\cap T',r'T_0=X_0\cap T',
       'Both T forms have only their own cap and stem; neither has a separate overbar. The first T and the X each have a clear lowered oval zero. The equality is two horizontal strokes and the intersection is an arch.',
       'misread symbol or index',True,False,consequential=True)

change('P20_f','P20','Diagram: lower product interval weight',
       r'Y_0\times I',r'Y_0\times\mathbf{I}',r'Y_0\times I',
       'The lower I is one thin stem between serifs, like the other two diagram I forms. H gives the heavier alphabet. The Y has two upper arms and a lowered round zero.',
       'misread symbol or index',False,True)

change('P20_g','P20','Diagram: lower right defining equality',
       r'Y_0=X_0\cap Y',r'Y_0=\dot X_0\cap Y',r'Y_0=\dot X_0\cap Y',
       'A separate filled point is visible over the left arm of this lower-right X, unlike the plain X in the upper definition. Both zeros are distinct ovals. The dot is retained even though it differs from the neighbouring definition.',
       'misread symbol or index',True,False,consequential=True)

change('P20_h','P20','Diagram: three vertical cup relations',
       r'\arrow[u,phantom,"\cup" description]','[not transcribed]',
       r'\arrow[u,phantom,"\cup" description]',
       'There are exactly three U-shaped vertical relation glyphs: one below the upper E and two in the product column. None has an independent arrowhead or connecting shaft; the last thick U is crossed by a cancellation diagonal. H’s prose reconstruction omits these relations. C’s three phantom cups are retained, with no fourth left-column cup.',
       'omission',False,True,consequential=True)

change('P20_i','P20','Separate small crossed group near the lower diagram',
       r'\deleted{\unsure{E\cap T}}','[not transcribed]',
       r'\deleted{$\unsure{E\cap T}$}',
       'A compact E-like body, arch and T-like cap are crossed by their own heavy strokes as well as the global cancellation. The preferred E-intersection-T reading remains uncertain, as in C; H omits this extra group.',
       'omission',False,True,'low')

change('P21_a','P21','Thin lower-left foliation',r'\margin{23}','[not transcribed]',r'\margin{23}',
       'Two thin grey numerals stand at the lower paper edge: the first has a rounded top and lower base of 2; the second has upper and lower lobes of 3. Their hand/weight differs from the bold authorial 7. H does not transcribe the foliation.',
       'omission',False,True)

for mid, reading, p, evidence in [
    ('M0359','strict','P08','Raised s, tall first t, r shoulder, dotted i, c bowl and final t are distinguishable above the cancelled old phrase; a separate underline is visible. The first C reading is resolved, medium.'),
    ('M0360','est','P13','Low connected e/s run followed by a rising t; the whole slanted phrase has il immediately before and plus after. The letter strokes, not that syntax alone, decide the first reading, medium.'),
    ('M0361','parlant','P13','Long p descender, small a/r, tall looped l and final nt are distinguishable in the slanted margin. First reading resolved, medium.'),
]:
    report['decisions'].append(dict(id=mid,cote='150',scan='24',decision='first',reading=reading,
                                   evidence=evidence,crop=f'crops/{PAGE}_{p}.png',box=boxes[p],confidence='medium'))

inventory_items = [
 ('text','upper left, P01','7','his hand'),
 ('text','top continuation, P02','de dot X subset tilde X est déterminé par la connaissance de','his hand'),
 ('display','upper first formula, P02','tilde X prime subscript 1 intersection dot X = dot X prime subscript 1.','his hand'),
 ('text','upper Corollaire, P03–P04','Corollaire Les parties ... corr. 1-1 ...','his hand'),
 ('insertion','above Les parties / before X prime, P03/P22','fermées, attached by a bent leader','his hand'),
 ('text','condition a), P05','tilde X prime soit compatible avec le ... structure cylindrique','his hand'),
 ('insertion','above structure in a), P05','germe de','his hand'),
 ('insertion','small lower row belonging to a), P05','de tilde X, dot X','his hand'),
 ('text','condition b), P06','f: dot X to Y applique ... dot X prime déf = ... dans Y prime.','his hand'),
 ('deletion','after applique, P06','uncertain tilde X prime','his hand'),
 ('display','On aura image formula, P07','X prime = underbraced Im(...) with closure annotation, nested Y prime brace, union Y prime','his hand'),
 ('text','Pour que and its abbreviated condition, P08–P10','Pour que X prime soit ... il f et. s. que ...','his hand'),
 ('deletion','old wording in Pour que row, P08','underlined strict[.] compatible avec','his hand'),
 ('insertion','raised replacement in Pour que row, P08','cônique, underlined strict','his hand'),
 ('deletion','lower old clause, P09','uncertain la/le ... structure cônique','his hand'),
 ('insertion','raised and cancelled between old article and structure, P09','uncertain purement / germe de','his hand'),
 ('text','Soit maintenant paragraph, P11–P15','X0 subset X une partie bordante; calligraphic E une germe de structure cylindrique; compatibility with calligraphic T','his hand'),
 ('insertion','after literal une, P11','germe de','his hand'),
 ('margin note','slanted upper left, P13','au lieu de compatible il est plus parlant de dire transversal','his hand'),
 ('insertion','after representative E, P14','isomorphism X0 times bold serif I, attached by leaders','his hand'),
 ('insertion','after avec and before structure, P15','sa','his hand'),
 ('text','lower a) baseline, P16','three intersections ... des parties cylindriques de','his hand'),
 ('deletion','after third intersection, P16','short uncertain compat.','his hand'),
 ('insertion','above old compat, P16','soient only; following des parties cylindriques de remains on baseline','his hand'),
 ('deletion','two homothety draft rows, P17–P18','uncertain barred E intersection barred T soit stable ... two maps ... qui agissent de part et d’autre','his hand'),
 ('deletion','left of diagram, P20','E i.e., within the global cancellation','his hand'),
 ('margin note','slanted lower left, P19','donc stable par E-homothéties par lambda in [0,1]','his hand'),
 ('diagram','lower page, P20','cancelled three-row diagram: eight principal objects, three identifications, three cups, nine long diagonals','his hand'),
 ('deletion','separate small crossed group near lower diagram, P20','uncertain E intersection T','his hand'),
 ('margin note','lower left paper edge, P21','23','thin secondary foliation; attribution indeterminate'),
]
for i,(kind,pos,words,hand) in enumerate(inventory_items,1):
    report['inventory'].append(dict(scan=PAGE,sheet_kind='text',hand=hand,element=f'E{i:02d}',kind=kind,
                                   position=pos,first_words_or_objects=words,transcribed='yes'))

def audit(id,p,kind,reading,scope='',xy=None,semantic=False):
    row=dict(box=id,kind=kind,xyxy=xy or boxes[p],reading=reading)
    if scope: row['scope']=scope
    if semantic: row['semantic_diagram_reading']=True
    report['audit_boxes'].append(row)

audit('B01','P01','handwritten number','7','Authorial numeral only.')
audit('B02','P02','handwritten number',r"\widetilde X'_1\cap\dot X=\dot X'_1.",'Whole displayed first equation, including both handwritten subscript ones, primes, tildes and dots; exclude prose above.')
audit('B03','P22','insertion',r'\inserted{fermées}','Raised word and its bent attachment leader only; exclude lower baseline spillover. P22 completes P03.')
audit('B04','P04','handwritten number; C/H different words',
      r"corr. $1$-$1$ avec les couples $(\widetilde X'\subset\widetilde X,Y'\subset Y)$ de parties fermées de $\widetilde X$ et de $Y$, telles que",
      'Both baseline rows; one live fermées, no duplicate deletion.')
audit('B05','P05','insertion; C/H different words',
      r"a) $\widetilde X'$ soit compatible avec le \inserted{germe de} structure cylindrique \inserted{de $\widetilde X,\dot X$}",
      'Condition a) only, including its two small insertions and absence of terminal punctuation; exclude b) spillover.')
audit('B06','P06','struck passage; doubtful formula; C/H different words; less than high confidence departure',
      r"b) $f:\dot X\to Y$ applique \deleted{$\unsure{\widetilde X'}$} $\dot X'\overset{\text{déf}}{=}\widetilde X'\cap\dot X$ dans $Y'$.",
      'Whole b) row and crossed variable; no reconstruction of the prime under the strike.')
audit('B07','P07','doubtful formula; less than high confidence departure',image_formula,
      'Whole displayed image formula and both annotations, excluding On aura. Brace starts under the right half of m; no terminal point.')
audit('B08','P08','insertion; struck passage; C/H different words; less than high confidence departure',
      r"Pour que $X'$ soit \deleted{\uline{strict\unsure{.}} compatible avec} \inserted{cônique \uline{strict}},",
      'Main Pour que row plus raised replacement; old lower clause is B09.')
audit('B09','P09','insertion; struck passage; C/H different words; less than high confidence departure',
      r'\deleted{\unsure{la|le} \inserted{\unsure{purement|germe de}} structure cônique}',
      'Whole old lower clause and raised cancelled word, attached after the article. Exclude descender of que from the row above.')
audit('B10','P10','C/H different words',r"il f et. s. que $Y'=\operatorname{Im}(\dot X'\to Y)$",
      'Abbreviated prose and full equality through the final parenthesis; no end point.')
audit('B11','P11','insertion; handwritten number',
      r'Soit maintenant $X_0\subset X$ une partie bordante de $X$, et $\mathcal E$ une \inserted{germe de} structure cylindrique',
      'The two main rows, including literal une and raised germe de.')
audit('B12','P12','handwritten number; C/H different words',
      r'de $X_0$ dans $X$. On dit que $\mathcal E$ est compatible avec le germe de structure conique $\mathcal T$',
      'The two main rows; unaccented conique is the occurrence before calligraphic T. Exclude slanted margin and later representatives row.')
audit('B13','P13','margin note; C/H different words; less than high confidence departure',upper_margin,
      'Slanted margin only; exclude upright main-text E, curves and formula spillover. Paired upper ticks and transversal underline included.')
audit('B14','P14','insertion; handwritten number',
      r'de $X$ autour de $Y$, si $\exists$ représentants $E\inserted{\simeq X_0\times\mathbf I}$ voisinage cylindrique de $X_0$, et $T$ voisinage',
      'Main representatives rows plus inserted product and its leaders; no independent underline or parenthesis is inferred from the large return.')
audit('B15','P15','insertion',r'cônique de $Y$ (avec \inserted{sa} structure cônique), tels que',
      'Main row with sa insertion and both independent circumflex accents.')
audit('B16','P16','insertion; struck passage; doubtful formula; C/H different words; less than high confidence departure',
      r'a) $T\cap\unsure{\overline E|E}$, $\dot T\cap E$, et $Y\cap\unsure{\overline E|E}$ \deleted{\unsure{compat.}} \inserted{soient} des parties cylindriques de',
      'Whole live a) row, including crossed compat and raised soient only. Des parties cylindriques de remains on the main baseline; exclude the next cancelled row.')
audit('B17','P17','struck passage; doubtful formula; less than high confidence departure',
      r"$\unsure{\overline E|E}\cap\unsure{\overline T|T}$ soit stable par les deux types d'homothéties",
      'First cancelled homothety row only; all words/first formula struck. Upper context is already in P16, not a new reading from P23.')
audit('B18','P18','struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',
      '$'+first_map+'$ et $'+second_map+'$ '+old_tail,
      'Second cancelled homothety row only. Include both whole maps and all following old words; exclude overlapping E i.e. and diagram objects, which have separate boxes.')
audit('B19','P19','margin note; handwritten number',r'donc stable par $E$-homothéties par $\lambda\in[0,1]$',
      'Slanted live margin only, including both interval digits and brackets; exclude upright cancelled body, diagram strokes and the separately audited foliation.')
audit('B20','P20','struck passage; C/H different words; less than high confidence departure',r'\deleted{$E$ i.e.}',
      'Only the running E i.e. at the left of the diagram and the diagonal crossing its E; exclude other old prose and small extra formula.',xy=[278,2135,590,2240])
diagram_reading = r'''\deleted{\begin{tikzcd}
E \arrow[r,phantom,"\simeq"] & X_0\times I \\
\dot T\cap\unsure{E|\overline E} \arrow[u,phantom,"\cup" description] \arrow[r,phantom,"\simeq"] & T_0\times I \arrow[u,phantom,"\cup" description] & T_0=X_0\cap T \\
Y\cap\unsure{E|\overline E} \arrow[r,phantom,"\simeq"] & Y_0\times I \arrow[u,phantom,"\cup" description] & Y_0=\dot X_0\cap Y
\end{tikzcd}}'''
audit('B21','P20','struck passage; doubtful formula; handwritten number; C/H different words; less than high confidence departure',diagram_reading,
      'Entire genuine three-row diagram: eight principal formula objects, three horizontal identifications, three vertical cups, all globally cancelled by nine diagonal strokes. Exclude old homothety prose, running E i.e., the separate small crossed group and thin foliation. State wrapper is a semantic reading of the drawn cancellation, not a request for a single horizontal strike.',semantic=True)
audit('B22','P20','struck passage; doubtful formula; less than high confidence departure',r'\deleted{$\unsure{E\cap T}$}',
      'Only the small separately crossed E-intersection-T-like group left of the lower diagram; exclude the large global diagonals as letters and exclude margin/body words.',xy=[480,2170,940,2340])
audit('B23','P21','margin note; handwritten number',r'\margin{23}','Thin foliation only; paper edge is not text.')
for row in report['audit_boxes']:
    if row['box'] in ('B17','B18'):
        row['reading'] = r'\deleted{' + row['reading'] + '}'
        row['scope_excerpt_of_deleted_passage'] = True
    labels = {'B20':'running text left of diagram', 'B21':'whole cancelled diagram', 'B22':'small separately crossed group'}
    if row['box'] in labels:
        row['kind'] += '; ' + labels[row['box']]


def doubt(place,reading,alternatives,confidence,reason):
    report['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))

doubt('P06 crossed variable',r'\unsure{\widetilde X\'}'.replace("\\'", "'"),'prime and exact overworked decoration unresolved','medium','Crossing leaves X and tilde-like upper mark but does not separate every stroke; C doubt retained.')
doubt('P08 old abbreviation point',r'strict\unsure{.}','strict with no independently written terminal stop','medium','The short word is clear; putative point is merged with the cancellation. Added punctuation doubt alone is not a change against C.')
doubt('P09 old article',r'\unsure{la|le}','le','medium','a/e body is crossed; la remains preferred, with no grammatical correction.')
doubt('P09 cancelled raised word',r'\unsure{purement|germe de}','germe de','low','Descending first letter and compact following run favour purement, but the cancellation and overlap do not separate all letters; insertion attaches after article.')
doubt('P16 first and third E',r'\unsure{\overline E|E}','plain E','medium','Detached-looking high marks can be bars or upper E arms; local preferred bar is retained without claiming certainty.')
doubt('P16 short cancelled compat form',r'\unsure{compat.}','compat without independently secure point; final short-body details obscured','medium','Short body, ending and point are crossed; no expansion to compatible.')
doubt('P17 first crossed intersection',r'\unsure{\overline E|E}\cap\unsure{\overline T|T}','plain E and/or plain T','low','Upper strokes coincide with horizontal cancellation and neighbouring main-row ink.')
doubt('P18 first whole map',first_map,'plain x; exact lambda-x target strokes or their bar state unresolved','low','Short upper x mark and target group are crossed; lowered X0 is visible. No multiplication point is supplied.')
doubt('P18 second whole map',second_map,r't\mapsto\lambda\times_Y t; terminal t remains crossed','low','Tail/head and lowered Y attachment are not fully separable; crossing product is certain.')
doubt('P18 final cancelled prose',old_tail,'que; exact agissent and de part et d’autre letters remain obscured','low','q descender survives but final i/e and later letter bodies overlap strike/diagram; no resolution of C’s old doubts.')
doubt('P20 middle and lower E in diagram',r'\unsure{E|\overline E}','barred E','medium','Three horizontal E arms are counted in each; high arm detachment alone does not establish a fourth bar. Plain is preferred; uncertainty is added only, not a departure against C/H at these E forms.')
doubt('P20 small separately crossed group',r'\unsure{E\cap T}','exact old letters remain unresolved','low','Own heavy cross/zigzag and global diagonals obscure the group; C candidate retained without resolving it.')

notes = [
 ('N01','This undated manuscript leaf bears the authorial 7 and thin secondary foliation 23. It continues a characterization of closed subsets compatible with a conical germ by cylindrical data upstairs and closed data in Y, then defines compatibility between a cylindrical germ at X0 and a conical germ near Y. The lower homothety draft and diagram are cancelled. These are transcription-level descriptions; they are not a verification of the corollary or of all compatibility assertions.'),
 ('N02','The image formula is retained literally with the underbrace attached to Im(tilde X′ par tilde X→X), although its left end lies beneath the right half of m rather than at the full left edge. The lower annotation has a closure bar over X′\\(Y∩X′), with a second brace identifying Y∩X′ as Y′. No grouping or hypothesis is silently supplied to the source. The intended image–closure equality is the limited target of N03.'),
 ('N03','Independent counterexample to the underbrace equality only. Let S=(0,1]×[0,1], B=(0,1]×{0}, Y=[0,1], and f:B→Y be f(a,0)=a. Form the quotient X=S amalg_B Y and let q denote the quotient map from S disjoint-union Y. Choose tilde X′=S, Y′=Y and X′=X. These chosen parts are closed in their own ambient spaces; S has the evident product cylinder near B, and f maps B into Y′. The image q(S) is X with the class of 0∈Y omitted: no point of B maps to 0, while all positive basepoints do. Meanwhile X′\\Y is precisely the positive-height cylinder. Every neighbourhood U of the class of 0 has q^{-1}(U)∩Y open in Y and containing 0, so it contains some a>0. The same quotient class is q(a,0), hence q^{-1}(U)∩S is open in S and contains (a,0). Product topology then forces (a,t) in that preimage for some t>0. Thus every neighbourhood of 0 meets the positive-height part; the same statement is immediate at positive basepoints, and positive-height points already belong to that part. Consequently closure_X(X′\\Y)=X, whereas Im(tilde X′→X)=q(S)=X\\{0}. The written identification of that image with the closure is false under these general quotient assumptions.'),
 ('N04','Scope of N03: the union identity X′=q(S)∪Y′ remains true in the same example, since X is the quotient of S disjoint-union Y. The example therefore refutes only the underbrace’s image–closure equality. It neither refutes nor proves the full claimed correspondence with canonical cylindrical subsets. No theorem about the entire corollary is certified by this report, and no source symbol is changed in response to this calculation.'),
 ('N05','Revision stages are preserved locally: the old underlined strict[.] compatible avec is crossed; cônique strict is a live raised replacement with strict underlined; the entire lower article–structure cônique clause and its inserted purement/germe de candidate are crossed. The raised candidate attaches after the article, not before it. Only soient, not the following baseline des parties cylindriques de, is raised in the lower condition. Because E i.e. falls within the global cancellation, the retained live lower wording ends with de; no completion is supplied.'),
 ('N06','Literal wording includes une germe de and the abbreviation il f et. s. (no point after f; points after et and s). Cônique is accented where an independent mark is present, while the occurrence before calligraphic T in P12 is conique without an independent accent. The page’s abbreviations and lack of final points are not normalized.'),
 ('N07','Both slanted margins are distinct from upright body spillover. The upper reads au lieu de “compatible” il est plus parlant de dire “transversal”, with paired source ticks and a single underline under transversal. The lower reads donc stable par E-homothéties par λ∈[0,1]. Rotated cropping is for inspection only; the transcription keeps them as margins. Extra upright E/curves near the upper margin and the main cancellations near the lower margin are excluded, not duplicated.'),
 ('N08','Bars are decided locally. In the lower live condition the first T has one cap and is plain; the first and third E have detached-looking high marks that leave bar/plain uncertainty, bar preferred. In the diagram, top E has its three ordinary arms with no separately identified fourth bar. Middle/lower E each have three arms in total, including the high detached-looking arm; plain E is preferred there with a bar alternative. Each T0 and the final T in the diagram has one cap only. The final lower-right X0 has a separate dot, unlike the upper definition’s X0, and is retained as dotted rather than harmonized.'),
 ('N09','Diagram accounting: eight principal formula objects, three horizontal ≃ relations and three vertical cups; no fourth cup or arrowhead is supplied. The product factors use thin serif I, unlike the heavy inserted I in P14. The entire lower draft is cancelled by nine long diagonal strokes, including the leftmost across E i.e.; the small old E∩T-like group has additional local crossing. Tikz-cd typesets the formula cells, with end-picture strokes recording the global cancellation; running text E i.e. is separately transcribed as deleted. Normal diagram spacing is used and no text glyphs are redrawn as paths.'),
 ('N10','Inspection record: original whole image once and each supplied native half once, then saved P01–P21 crops inspected once; the failed P21 delivery produced no viewed image and was redelivered successfully. P22 completes the clipped upper f of fermées and was inspected once. P23 was intended as an ascender completion but overlaps almost entirely with the already inspected P16 frame; it is retained as an inadvertent overlapping strip, with no new source decision and no claim of previously unexamined ink. No further crop was made. P16 plus P17 already provide that shared context. No OCR, external research, compilation or other-page access was used.'),
]
for nid,text in notes: report['notes'].append(dict(id=nid,text=text))

report['check_events'] = [
 dict(statement_id=PAGE+'.N01',type='carried as background without fault found',outcome='Page-level subject description only; no general corollary or compatibility theorem was proved.'),
 dict(statement_id=PAGE+'.N03',type='independent re-proof',outcome='Independently checked the exact quotient counterexample supplied as a root lead: closed chosen parts, cylindrical S, image missing 0, and density of positive heights by the quotient-open neighbourhood argument.'),
 dict(statement_id=PAGE+'.N03.underbrace',type='refuted, with refined id',outcome='Only Im(tilde X′→X)=closure_X(X′\\Y) is refuted under the stated general quotient assumptions: left side X\\{0}, right side X.'),
 dict(statement_id=PAGE+'.N04',type='used and rechecked in this run',outcome='For the same example q(S)∪Y=X follows from the quotient presentation; this was checked separately to avoid claiming the whole corollary is refuted.'),
]

report['notation'] = [
 dict(form=r'\widetilde X,\dot X,\widetilde X\prime,\dot X\prime',meaning='Upstairs space, its dotted boundary and the indicated primed portions; no new global construction is assumed beyond the written page.',evidence='P02/P05/P06: separate tildes, dots, primes and both initial subscript ones.'),
 dict(form=r'\mathcal E,\mathcal T',meaning='Cylindrical and conical germs, distinct from their ordinary-letter representatives E and T.',evidence='P11–P15: calligraphic letter bodies in the prose, plain representatives below.'),
 dict(form=r'\mathbf I;\ I',meaning='Locally heavy interval factor in the inserted representative and thin serif interval factors in the diagram.',evidence='P14 filled stem/broad serifs; P20 three thin stems with serifs. Alphabet is not homogenized.'),
 dict(form=r'\cup\text{ vertically}',meaning='Three vertical inclusion-like relations in the cancelled diagram; glyphs are cups, not arrows.',evidence='P20: three U-shaped marks without independent heads; last is crossed by a diagonal.'),
 dict(form=r'\lambda_Y\times t\ |\ \lambda\times_Y t',meaning='Unresolved attachment of the lowered Y in the second cancelled homothety map; crossing product is visible.',evidence='P18: Y lies below and between lambda and the cross, nearer lambda; no multiplication point replaces the cross.'),
]

report['abbreviations'] = [
 dict(form='corr.',expansion='correspondance'),
 dict(form='déf',expansion='définition'),
 dict(form='strict[.]',expansion='strictement (old crossed short form; terminal point uncertain)'),
 dict(form='il f et. s.',expansion='il faut et suffit'),
 dict(form='compat[.]',expansion='compatible / compatibles (crossed short form; ending and point uncertain)'),
 dict(form='i.e.',expansion='id est'),
]

report['hand'] = [
 dict(habit='A detached high horizontal stroke can be E’s own upper arm, not an added bar.',places='150_scan024 P14/P16/P19/P20',consistency='Local arm counts differ in clarity: top/middle/bottom diagram E have three counted arms; first/third E in live condition remain bar/plain uncertain.',witness_errors='C supplies bars on adjacent T forms; H and C omit possible E bars in live condition. No global convention is imposed.'),
 dict(habit='T’s broad cap is often retraced but remains a single cap unless another stroke is independently present.',places='150_scan024 P14–P20',consistency='Plain live first T and three plain diagram T/T0 forms; old cancelled intersection remains locally doubtful.',witness_errors='C adds bars to first live T and to the diagram T0/final T; the old crossed T bar is not resolved merely by analogy.'),
 dict(habit='Insertion leaders bend and can resemble underlines or parentheses.',places='150_scan024 P03/P05/P09/P11/P14/P15/P16',consistency='Attachments are independently traced; only soient is raised before baseline des parties cylindriques de.',witness_errors='C places the cancelled raised purement candidate before the article; H misses lower de qualification state and sa.'),
 dict(habit='Independent small accents must be checked occurrence by occurrence.',places='150_scan024 P03/P06/P08/P12/P15/P22',consistency='Accented cônique and déf occur, but P12 conique has no independent o accent.',witness_errors='C omits déf accent; both witnesses supply P12 circumflex.'),
 dict(habit='Weight distinguishes the inserted interval I from the diagram interval I forms.',places='150_scan024 P14/P20',consistency='One heavy inserted I; all three diagram factors thin serif.',witness_errors='C gives plain I in insertion; H gives bold I throughout the lower diagram.'),
]

coverage = {
 1:'Scan marker is editorial, not manuscript text; authorial 7 is retained separately. No macro-only change row.',
 2:'H editorial description of authorial 7 versus C mspage wrapper: same numeral, inventory E01 and audit B01; no source-text difference.',
 3:'P04_a: one live fermées; no duplicate struck word.',
 4:'H enumerate wrapper only; no source-text change row.',
 5:'H item wrapper only; literal a) retained.',
 6:'P05_a: smaller lower phrase is inserted and no terminal semicolon is present; item wrapper excluded.',
 7:'H item wrapper only; literal b) retained.',
 8:'P06_a/P06_b: crossed doubtful variable retained rather than illegible placeholder; independent accent in déf.',
 9:'H enumerate closing wrapper only; no source-text change row.',
 10:'H thin-space macro after Im is formatting only. P07_a covers actual brace/bar/terminal-point differences.',
 11:'P07_a: nested Y-prime brace label is retained; H puts the annotation in editorial prose rather than the displayed formula.',
 12:'P07_a: source nested brace/label transcribed directly; H editorial explanatory wording is not extra source text.',
 13:'P07_a: no terminal point after union Y prime; display delimiters are macro-only.',
 14:'P08_a/P08_b: old strict short form, local stop doubt, live underlined strict resolved.',
 15:'P09_a: whole lower old clause cancelled; raised purement/germe de attaches after doubtful article.',
 16:'P10_a: literal f without point, followed by et. s.; H expansion rejected.',
 17:'P10_a: literal et. s. point placement, no expansion.',
 18:'H thin-space macro after Im is formatting only.',
 19:'P10_b: terminal point supplied by H is absent.',
 20:'P15_a: sa insertion present before structure.',
 21:'P13_a plus M0360/M0361: full upper margin read, local doubts resolved; no terminal point.',
 22:'P16_c: crossed short compat form, not full compatible.',
 23:'P16_d: final live de, not H crossed et; only soient is raised.',
 24:'P18_a: no separate multiplication point in first map.',
 25:'P18_a/P18_b/P18_c: lowered X0, second map with crossing product and doubtful Y attachment, old prose retained with local doubts.',
 26:'P20_a: running E i.e. belongs to global cancellation; H mis-associates wording with margin.',
 27:'P20_b–P20_i: full actual diagram and extra group read; H notes are editorial descriptions, not source words. P19 live lower margin retained.',
 28:'P20_a/P20_b: i.e. is deleted running text; actual top row is E ≃ X0 times thin I. Row-spacing macro text is not source.',
 29:'P20_b/P20_c: top row and dotted middle-left T; C dot/bar doubt resolved locally.',
 30:'P20_h: actual vertical cup and horizontal identification; arrow syntax is only encoding.',
 31:'P20 diagram: actual horizontal ≃ retained; quotation syntax in TikZ options is not source text.',
 32:'P20_d/P20_h: middle product and vertical cup, without added arrowhead.',
 33:'P20_b/P20_d: no extra T-intersection row; actual middle target is plain T0 times thin I.',
 34:'P20_f/P20_h: lower Y0 product and third vertical cup; no additional relation invented.',
 35:'P20_e/P20_g: both right-hand definitions; only lower-right X0 is dotted.',
 36:'P20_f/P20_h: lower row objects, horizontal identification and vertical cup all transcribed.',
 37:'P20_i/P21_a: small crossed E-intersection-T candidate and thin 23 retained; H omits both. Closing diagram macros are not source text.',
}
report['diff_coverage'] = [dict(row=i,disposition=coverage[i]) for i in range(1,38)]

reviews = [
 ('fermées','Live insertion before X prime; leader is not an independent underline.','P03 plus completing P22: tall f, independent accent and bent leader.'),
 ('baseline fermées','One live word; no preceding cancelled duplicate.','P04: one f/body, retracing without separate strike.'),
 ('a) germe de','Raised insertion before structure.','P05 bent leader.'),
 ('a) de tilde X, dot X','Smaller interlinear addition to the cylindrical-structure clause, not part of b); no terminal semicolon.','P05 position and upper filled X dot.'),
 ('b) old variable','Crossed doubtful tilde X prime before the new dotted X prime.','P06 X diagonals/tilde-like mark; prime obscured.'),
 ('old strict compatible avec','Whole old sequence crossed, including avec; underline under old short strict is separate.','P08 long strike crosses all three words.'),
 ('cônique strict','Live raised replacement; strict has one underline.','P08 separate raised bodies and emphasis.'),
 ('old article structure cônique','Entire clause crossed; article remains la/le doubtful.','P09 two long cancelling strokes.'),
 ('purement / germe de','Raised insertion is itself cancelled and attaches after the old article, before structure.','P09 bent leader; que-descender excluded from the word.'),
 ('Soit maintenant germe de','Live insertion after literal une.','P11 smaller raised words and leader.'),
 ('E product representative','Live inserted isomorphism after E, with heavy I; large return is attachment, not deletion of de X autour.','P14 traced inner/outer leaders.'),
 ('sa','Live insertion after avec and before structure.','P15 small s/a and leader.'),
 ('compat / soient','Old short compat crossed; only soient is raised as replacement; des parties cylindriques de stays on baseline.','P16, with already inspected overlapping context retained in P23.'),
 ('homothety rows','Both rows cancelled, including the first intersection, both maps and their following words.','P17/P18 horizontal and diagonal strikes; individual obscured symbols remain doubtful.'),
 ('E i.e.','Within global deletion, although C leaves it live.','P20 first diagonal crosses E and the phrase belongs to the old lower draft.'),
 ('bottom diagram','All eight objects and six relations cancelled by global diagonals; no false vertical arrowheads.','P20 nine long diagonal strokes, three cups, three ≃ signs.'),
 ('small E intersection T','Separately crossed and globally cancelled; uncertain content retained.','P20 compact group with own heavy crossing.'),
 ('two slanted margins','Both live; neither is consumed by neighbouring main-text cancellation.','P13/P19 rotation and exclusion of upright spillover.'),
]
for text,scope,evidence in reviews:
    report['deletion_insertion_review'].append(dict(text=text,scope_attachment=scope,evidence=evidence))

# Nonempty transcription lines, excluding comments and TikZ drawing/option mechanics.
mechanic = re.compile(r'^\s*(?:%|\\draw|column sep=|execute at end picture=|\}\s*\]?\s*$|\]\s*$)')
report['line_count'] = sum(bool(s.strip()) and not mechanic.match(s) for s in draft.splitlines())
report['line_count_basis'] = 'Nonempty draft lines excluding comments and diagram option/cancellation-drawing mechanics; this is a transcription-file count, not a claim about manuscript baselines.'
report['inspection'] = dict(original_whole_views=1,native_half_views=[1,1],
                            saved_crops=23,first_pass_crop_views=23,
                            failed_image_delivery='P21 first delivery failed before any visible image; successful redelivery counted once.',
                            completing_crop='P22 completes P03.',
                            overlap_exception='P23 inadvertently overlaps already inspected P16; no new decision; retained and disclosed.',
                            external_research=False,ocr=False,compilation=False,
                            all_agreed_words_read=True,root_review='Parent personally reviewed P01–P23 and supplied independent crop feedback; root finalization remains pending.')

(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

def compact(s):
    return re.sub(r'\s+','',s)

checks=[]
for row in report['changes']:
    for key,source in [('c',C),('h',H)]:
        ok=row[key]=='[not transcribed]' or compact(row[key]) in compact(source)
        checks.append((f"{row['id']}.{key}",ok))
    fragments=row.get('final_fragments',[row['final']])
    checks.append((f"{row['id']}.final",all(compact(f) in compact(draft) for f in fragments)))
for row in report['decisions']:
    checks.append((f"{row['id']}.final",compact(row['reading']) in compact(draft)))
checks.append(('marks_order',[r['id'] for r in report['decisions']]==['M0359','M0360','M0361']))
checks.append(('diff_rows',[r['row'] for r in report['diff_coverage']]==list(range(1,38))))
for key,box in boxes.items():
    checks.append((key+'.bounds',0<=box[0]<box[2]<=1685 and 0<=box[1]<box[3]<=2361))
    checks.append((key+'.file',(ROOT/f'work/crops/{PAGE}_{key}.png').is_file()))
for row in report['audit_boxes']:
    b=row['xyxy']; checks.append((row['box']+'.bounds',0<=b[0]<b[2]<=1685 and 0<=b[1]<b[3]<=2361))
for row in report['decisions']+report['changes']:
    checks.append((row['id']+'.crop',(ROOT/'work'/row['crop']).is_file()))
without_comments='\n'.join(s.split('%',1)[0] for s in draft.splitlines())
depth=0; balanced=True
for ch in re.sub(r'\\[{}]','',without_comments):
    if ch=='{':depth+=1
    elif ch=='}':
        depth-=1
        if depth<0:balanced=False
checks.append(('braces_balanced',balanced and depth==0))
checks.append(('dollar_parity',len(re.findall(r'(?<!\\)\$',without_comments))%2==0))
checks.append(('display_delimiters',without_comments.count(r'\[')==without_comments.count(r'\]')))
checks.append(('tikzcd_environment',without_comments.count(r'\begin{tikzcd}')==without_comments.count(r'\end{tikzcd}')==1))
checks.append(('diagram_stroke_count',len(re.findall(r'\\draw\[',without_comments))==9))
checks.append(('diagram_cup_count',without_comments.count(r'\arrow[u,phantom,"\cup" description]')==3))
checks.append(('diagram_identification_count',without_comments.count(r'\arrow[r,phantom,"\simeq"]')==3))
checks.append(('diagram_object_count',len(re.findall(r'alias=p[A-H]',without_comments))==8))
failed=[name for name,ok in checks if not ok]
validation=dict(page=PAGE,checks=len(checks),failures=failed,compilation_performed=False,
                statement='Mechanical bookkeeping and source-string/structure checks only; no TeX compilation, OCR or new visual reading.',
                counts={k:len(report[k]) for k in ['changes','decisions','inventory','audit_boxes','doubts','notes','check_events','diff_coverage']})
(OUT/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(validation,ensure_ascii=False))
