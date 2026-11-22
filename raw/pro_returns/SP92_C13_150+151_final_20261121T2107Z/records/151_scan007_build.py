import json
from pathlib import Path

BASE = Path('/workspace/scratch/d7279cb02214')
OUT = BASE / 'SP92_C13_150+151_work/records'
P = json.loads((BASE / 'reading_packets/151_scan007/packet.json').read_text())
C, H = P['witness_C'], P['witness_H']
T = (OUT / '151_scan007.tex').read_text()
CM = json.loads((OUT / '151_scan007_cropmap.json').read_text())
Q = chr(96) * 2
changes = []

def sub(s, start, end, include_end=True):
    a=s.index(start)
    b=s.index(end,a)+ (len(end) if include_end else 0)
    return s[a:b]

top_diagram = sub(T, r'\diagram{\deleted{\mbox{\begin{tikzcd}', r'\end{tikzcd}}}}')
rho_diagram = sub(T, r'\diagram{\deleted{\mbox{\begin{tikzpicture}', r'\end{tikzpicture}}}}')
last_diagram = sub(T[T.index('% Tail bar and square'):], r'\diagram{\deleted{\mbox{\begin{tikzpicture}', r'\end{tikzpicture}}}}')
main_diagram = sub(T[T.index('Donc, en plus'):], r'\diagram{\begin{tikzcd}', r'\end{tikzcd}}')
lower_diagram = sub(T[T.index(r'\margin{$\uline'):], r'\begin{tikzcd}', r'\end{tikzcd}')
main_box = sub(T, r'\[\boxed{\begin{aligned}', r'\end{aligned}}\]')
right_box = sub(T, r'\margin{$\boxed{\begin{aligned}', r'\end{aligned}}$}')

def change(place, c, h, final, evidence, crop, kind, error_kind,
           ac=False, ah=True, confidence='high', consequential=False,
           marked=False, doubt_resolution=False):
    assert c in C, (place, 'C', c)
    assert h in H, (place, 'H', h)
    row = dict(id=f'C{len(changes)+1:02d}',place=place,C=c,H=h,
               final=final,evidence=evidence,crop=CM[crop]['crop'],
               box=CM[crop]['box'],confidence=confidence,kind=kind,
               error_kind=error_kind,against_C=ac,against_H=ah,
               consequential=consequential,marked_in_H=marked)
    if doubt_resolution: row['change_type']='doubt resolution'
    changes.append(row)
    return row['id']

change('Upper authorial circled 3',r'\mspage{\textcircled{3}}','',
       r'\mspage{\textcircled{3}}',
       'Two rounded right lobes form 3 inside the authorial dark oval; it is not the editorial scan number.',
       'circled_top','omission','3 omissions')
change('Upper canceled p0 identity',sub(C,r'\deleted{\[p_0p_{12}=',r'\]}'),
       r'p_0p_{12} = p_0p_{13} = p_0\,\underbrace{p_{12}\rho^2}_{p_{31}}\,\sigma_2,',
       r'\deleted{p_0p_{12}=p_0p_{13}=p_0\underbrace{p_{12}\rho^2}_{p_{31}}\sigma_2}',
       'The diagonal cancellation crosses the final sigma and lower p31 label. The equality, indices 0/12/13/31 and rho exponent 2 are all distinct; there is no final comma.',
       'top_p0','deletion state (struck given live or live given struck)','7 struck state')
change('Upper canceled rho equality',r'\deleted{\[\rho^2\sigma_2=\sigma_3\rho^2\]}',
       r'\rho^2\sigma_2 = \sigma_3\rho^2,',
       r'\deleted{\rho^2\sigma_2=\sigma_3\rho^2}',
       'Both superscript 2s and the sigma indices 2/3 are clear. No terminal comma is written. This row belongs to the upper block canceled by the encompassing long strokes, although a diagonal does not cross this individual row.',
       'top_rho','deletion state (struck given live or live given struck)','7 struck state')
change('Canceled two-row coordinate/projection diagram',sub(C,r'\deleted{\diagram{',r'\end{tikzcd}}}'),'',
       top_diagram,
       'The first row has (x,y,z), a tail-bar arrow with a distinct chevron, and (z,y,x). Below are a source-free right arrow, (x,z), and a second right arrow to x. H condenses the coordinate calculations and omits this distinct two-row diagram.',
       'top_diagram','omission','3 omissions')
change('Canceled p0p12 sigma1 equality',r'\deleted{\[p_0p_{12}\sigma_1=p_0p_{12}\]}',
       r'p_0\,p_{12}\,\sigma_1 = p_0\,p_{12}.',
       r'\deleted{p_0p_{12}\sigma_1=p_0p_{12}}',
       'The sigma has the small vertical 1; both p12 groups remain legible within the crossed-out block. There is no stop after the final 12.',
       'top_p0sigma','deletion state (struck given live or live given struck)','7 struck state')
change('Separate upper canceled (x,x,y)',r'\deleted{\[(x,x,y)\]}','',
       r'\deleted{(x,x,y)}',
       'Both first coordinates have the same short crossing/return form of x, followed by a descending y and the closing parenthesis. This separate occurrence is absent from H.',
       'top_xxy','omission','3 omissions')
change('Canceled rho2sigma2 coordinate calculation, continuation arrow and delimiters',
       sub(C,r'\deleted{\[\rho^2\sigma_2:',r'\]}'),
       r'$(x,y,z) \mapsto (z,y,x) \mapsto (y,x,z)$',
       rho_diagram,
       'The written operator rho²sigma₂: precedes the first mapping. Two closing parentheses follow (z,y,x). The continuation is on the next line, begins with a separate tail bar, and ends in an open little loop rather than the upper diagram’s clear chevron. Its target has y,x underlined before the final z. The entire calculation is in the canceled block.',
       'top_rho_mapping','drawing or diagram','4 drawing/diagram',ac=True)
change('Canceled delta1sigma tuple',r'\delta_1\sigma=(x,y,y)',
       '$\\delta_1\\sigma =\n\\uncertain{(x,y,y)}$',
       r'\deleted{\delta_1\sigma=(x,y,y)}',
       'The three coordinates are x,y,y: the first has a short crossed return and both following letters have long descenders. A diagonal cancellation crosses the first coordinate; the separate delta index 1 and equality are clear.',
       'top_delta_triplets','deletion state (struck given live or live given struck)','7 struck state',marked=True)
change('Bare canceled z,x,y on its own right-hand line',r'z,x,y','',
       r'\deleted{z,x,y}',
       'Three separate letters z, x and y with two commas stand on their own line below the rho calculation; no opening or closing parenthesis surrounds them. C attaches them to the delta1sigma line, while the source places them in the right column.',
       'top_zxy','insertion or placement','6 insertion placement',ac=True)
change('Two lower canceled left tuples',r'\deleted{\[(x,x,y)\qquad(y,y,x)\]}',
       r'$(x,x,y)$ et $(y,y,x)$',
       r'\deleted{(x,\unsure{x},y)}\\\deleted{(y,y,x)}',
       'The tuples are on separate left-hand baselines inside the long diagonal cancellation. The second is plainly (y,y,x); the first has a heavily retraced middle x, retained under a narrow doubt. The added doubt is not itself counted as a correction.',
       'top_delta_triplets','deletion state (struck given live or live given struck)','7 struck state')
change('Final canceled coordinate mapping and following sigma1 equation',
       sub(C,r'\deleted{\[(x,y,z)\mapsto(z,x,y)',r'\]}'),
       r'$(x,y,z) \mapsto (z,x,y)$, enfin $(x,z,y) = \sigma_1$.',
       last_diagram,
       'The first source is (x,y,z), target (z,x,y). Its tail bar is visible, but the right terminal is a square upright with a short lower leftward return, not a triangular chevron. The next baseline reads (x,z,y)=sigma₁ and has no written terminal full stop. All are within the cancellation; H’s connective enfin is editorial.',
       'top_last_mapping','drawing or diagram','4 drawing/diagram',ac=True)
change('Repeated circled 3 before the live paragraph',r'\mspage{\textcircled{3}}','',
       r'\mspage{\textcircled{3}}',
       'The lower dark circled numeral again has two right lobes of 3; its lower lobe has a doubled terminal stroke. It is a second written authorial number, not the grey foliation.',
       'circled_numbers','omission','3 omissions')
change('First point abbreviation with raised t',r'pt','point',r'p\textsuperscript{t}',
       'Only p and t are written. The t’s foot finishes at the p’s upper bowl level, substantially above the main p baseline; it is raised, not a fully written point.',
       'opening_donc_par','abbreviation expanded or spelling modernised','8 abbreviation/spelling',ac=True)
change('Donc after the first p-t abbreviation',r'\unsure{donc|les}','les','donc',
       'The opening tall loop and rising stem form d, followed by the reduced o/n run and a separate short c-like terminal; the word has no initial l and ends before par.',
       'opening_donc_par','misread word','2 words',ac=True,doubt_resolution=True)
change('Par before delta0',r'par','',r'par',
       'The long descending p is followed by the compact joined a/r stroke. The word is separately written after donc and before the next line’s delta0.',
       'opening_donc_par','omission','3 omissions')
change('Delta composition and following E1,E2',r'$\delta_0,\delta_1\delta_0$ $E_1,E_2$',
       '$\\delta_0, \\delta_1, \\partial_0$, $E_1$,\n$E_2$',
       r'$\delta_0,\delta_1\delta_0$ $E_1,E_2$',
       'The composition has two matching delta loops with separate indices 1 and 0 and no comma between them. The second sign is delta, not partial. There is no comma between the composition and E1; the written comma separates E1 and E2.',
       'opening_delta','misread symbol or index','1 symbols/indices',consequential=True)
change('First group sign with index2',r'\unsure{\mathfrak S_2|\mathcal G_2}',r'\mathfrak{S}_2',
       r'\mathcal G_2','The sign has a broad enclosing C-shaped bowl and a horizontal inward return in its lower half, the characteristic written G rather than a two-lobed S. Its small index is 2.',
       'first_groups','misread symbol or index','1 symbols/indices',ac=True,consequential=True,doubt_resolution=True)
change('First group sign with index3',r'\unsure{\mathfrak S_3|\mathcal G_3}',r'\mathfrak{S}_3',
       r'\mathcal G_3','The second sign repeats the enclosing bowl and inward horizontal G return; the separate small subscript has the two bends of 3.',
       'first_groups','misread symbol or index','1 symbols/indices',ac=True,consequential=True,doubt_resolution=True)
change('Singular la ponctuation',r'\unsure{la ponctuation|les ponctuations}',r'le pointage',
       r'la ponctuation','The determiner has the tall loop l and a short joined a, without a final s. In the noun, the p descender, c/t group, t/i/on ending and lack of final s support ponctuation, not pointage or the plural.',
       'first_ponctuation','misread word','2 words',ac=True,doubt_resolution=True)
change('Marginal parenthetic quoted ponctués',r'\unsure{'+Q+"ponctués''}",r'(« pointés »)',
       '('+Q+"ponctués'')",
       'The note has round parentheses, two small quote ticks, the p descender and internal n/c/t run of ponctués, an accent over the final e, a short final s and two closing quote ticks; these are not guillemets.',
       'margin_ponctues','misread word','2 words',ac=True,doubt_resolution=True)
change('Separate deleted opening word before the second paragraph',r'\deleted{\unsure{Donc.|On a.}}','',
       r'\deleted{\unsure{Donc.|On a.}}',
       'A distinct short line with a looped capital and final point is crossed by a heavy horizontal stroke. Its internal letters remain entangled, so the C alternatives remain; H omits this separate deleted line.',
       'cancelled_words','omission','3 omissions',confidence='low')
change('Initial delta1 in the deleted phrase',r'\unsure{qui|$\delta_1$}',r'\ill',
       r'$\deleted{\delta_1}$',
       'The initial sign is a large open upper arc returning into the lower loop of delta, with a detached vertical small 1 at its lower right; it has neither the joined qu nor the dot expected for qui.',
       'cancelled_words','readable ink left as \\ill{}','5 readable left illegible',ac=True,doubt_resolution=True,marked=True)
change('Respecte in the deleted phrase',r'respecte les',r'respectant le',
       r'\deleted{respecte \unsure{les|le}}',
       'The p descender and raised crossed t are followed by a low e-like return, without an a/n run; respecte is legible despite the horizontal strike. The final determiner remains narrowly les/le under the strike.',
       'cancelled_words','misread word','2 words',marked=True)
change('Donc opening the next live paragraph',r'\unsure{Donc|Dans|Ainsi|Alors}',r'Dans',
       'Donc','A looped capital D is followed by a tiny rounded o and compressed n/c run before the comma. There is no initial A or tall l; the small medial loop favors o over a.',
       'donc_operations','misread word','2 words',ac=True,confidence='medium',doubt_resolution=True)
change('Second group sign with index2',r'\unsure{\mathfrak S_2|\mathcal G_2}',r'\mathfrak{S}_2',
       r'\mathcal G_2','This larger sign again encloses a low inward horizontal return within a broad outer bowl; the separate subscript 2 agrees with the first occurrence.',
       'second_groups','misread symbol or index','1 symbols/indices',ac=True,consequential=True,doubt_resolution=True)
change('Second group sign with index3',r'\unsure{\mathfrak S_3|\mathcal G_3}',r'\mathfrak{S}_3',
       r'\mathcal G_3','The upper bowl is squarer here, but the bottom inward loop/return still forms G. The subscript is a separate angular 3, not a component of the letter.',
       'second_groups','misread symbol or index','1 symbols/indices',ac=True,consequential=True,doubt_resolution=True)
change('Main E1,E2 arrow geometry',sub(C,r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]',r'\end{tikzcd}}'),
       sub(H,r'\begin{tikzcd}[column sep=large]',r'\end{tikzcd}'),
       main_diagram,'The upper p12 arrow is straight and points left from E2 to E1, with its label above. A separate lower curve points right and has delta1 below. H bends both arrows and puts the right arrow above; the source does not.',
       'main_diagram','drawing or diagram','4 drawing/diagram')
change('Comma and où following the main diagram',r', où',r'i.e.',r', où',
       'A detached comma precedes the short o/u run with a small accent above it. No letters i or e or intervening stops are written.',
       'ou_insertion','misread word','2 words')
change('Inserted et p12 attached after delta1',r'\inserted{et $p_{12}$}',r'\uncertain{et $p_{12}$}',
       r'\inserted{et $p_{12}$}',
       'The small et and p12 sit above the baseline. A curved leader descends to the gap immediately after delta1 and before respectent; it is an insertion leader, not a parenthesis or deletion.',
       'ou_insertion','insertion or placement','6 insertion placement',marked=True)
change('Respectent rather than respectant at the right edge',r'respectent',r'\uncertain{respectant}',
       r'respect\unsure{ent}',
       'After the central raised crossed t, a low e-like return is visible, ruling against respectant. The final arch/downstroke and short return touch the paper edge, so the compressed n/t boundary remains uncertain. This is only an added doubt against C, not a correction of C.',
       'respectent_edge','misread word','2 words',confidence='medium',marked=True)
change('Les ponctuations',r'ponctuations',r'pointations',r'ponctuations',
       'The noun starts with the descending p, then a compressed on/c group before the raised t, and ends in the plural s return. There is no dot for an i in point-; the written word matches the earlier ponctuation stem.',
       'les_ponctuations','misread word','2 words')
change('Et où before p12,delta1',r'et où',r'et on a',r'et où',
       'After et, the short o/u trace carries a detached grave-like mark above. There is no separate terminal a or additional word.',
       'et_ou_satisfont','misread word','2 words')
change('Satisfont before the five relations',r'satisfont',r'satisfaisant',r'satisfont',
       'The visible sequence has s/a, crossed t, short i, the long f, and one compressed o/n/t ending. The additional ai/sa syllables of satisfaisant are absent.',
       'et_ou_satisfont','misread word','2 words')
change('Five relations enclosed in a rectangular box',r'\boxed{\begin{aligned}',r'\begin{cases}',
       r'\boxed{\begin{aligned}',
       'The five main rows lie inside long top, left, bottom and right straight boundaries. There is no left curly cases brace. All five equalities, their indices and both under-brace labels were re-read.',
       'main_box','drawing or diagram','4 drawing/diagram')
change('Parenthetic marked-point explanation with raised t',
       r'\text{(pt marqué de }E_1\text{)}','',
       r'\text{(p\textsuperscript{t} marqué de }E_1\text{)}',
       'After e1, a separate opening parenthesis encloses the short p with a raised t, marqué (including its accent), de E1 and a closing parenthesis. H omits the entire parenthetic; C flattens the raised t.',
       'main_constant','omission','3 omissions',ac=True)
change('Delta1 label under rho delta2 in the small box',
       r'p_{12}\underbrace{\rho\delta_2}_{\delta_1}&=\sigma',
       r'p_{12}\rho\delta_2 = \sigma',
       r'p_{12}\underbrace{\rho\delta_2}_{\delta_1}=\sigma',
       'A shallow bracket below rho delta2 carries a complete delta with index1. The label is distinct from the row above and remains live; H omits it from the recap.',
       'right_box','omission','3 omissions',consequential=True)
change('Delta3 label under rho squared delta2 in the small box',
       r'p_{12}\underbrace{\rho^2\delta_2}_{\delta_3}&=e_1',
       r'p_{12}\rho^2\delta_2 = e_1',
       r'p_{12}\underbrace{\rho^2\delta_2}_{\delta_3}=e_1',
       'The lower bracket has a delta with a separate two-bend index3; rho has exponent2, delta has index2 and the result is e1. H drops the lower bracket label.',
       'right_box','omission','3 omissions',consequential=True)
change('Small-box parenthetic application de E1 sur e1',
       r'\text{(application de }E_1\text{ sur }e_1\text{)}','',
       r'\text{(application de }E_1\text{ sur }e_1\text{)}',
       'A round parenthesis opens before application. The following line reads de E1 sur, and the e1 continues on the short line below; the right parenthesis encloses these lines. H’s editorial constant-map synopsis does not transcribe these written words.',
       'right_explanation','omission','3 omissions')
change('Underlined right-hand relation has literal RHS p11',
       r'\uline{p_{12}\sigma_3=\sigma p_{12}}',
       '$p_{12}\\sigma_3 = \\sigma\np_{12}$',
       r'\uline{p_{12}\sigma_3=\sigma p_{11}}',
       'The RHS p is followed by two short upright numeral strokes. Neither has the curved head and rightward foot of the clear left-hand 2 in the same row. The long line beneath is an underline, not a cancellation. The literal 11 is kept despite the repeated p12 relation elsewhere.',
       'right_top_formula','misread symbol or index','1 symbols/indices',ac=True,confidence='medium',consequential=True)
change('Partially recovered canceled repeated relation',
       r'\unsure{p_{12}\sigma_3=\sigma p_{12}}','',
       r'\deleted{p_{12}\sigma_3\unsure{=\sigma}p_{12}}',
       'The left p loop and stem, indices12, sigma loop/bar and index3 protrude distinctly from the hatching. The right p and final12 are also exposed. The central equals/sigma remains merged with oblique hatching, so only the exposed portions of C’s whole-formula doubt are resolved.',
       'right_cancelled_formula','misread symbol or index','1 symbols/indices',ac=True,confidence='medium',doubt_resolution=True)
change('Separate canceled id-like entry',r'\unsure{\mathrm{id}}','',
       r'\deleted{\unsure{\mathrm{id}}}',
       'A separate small heavily hatched entry lies below-left of the canceled repeated relation. Its upright and loop could be id but are not separable from the cancellation; the existing narrow doubt remains. H omits this entry.',
       'right_cancelled_id','omission','3 omissions',confidence='low')
change('Lower-right E1,E2 diagram',sub(C[C.index(r'\margin{$\uline'):],r'\diagram{\begin{tikzcd}',r'\end{tikzcd}}'),'',
       lower_diagram,
       'Two visible objects E1 and E2 are connected by a straight upper arrow pointing left, labeled p12, and a shallower lower arrow pointing right, labeled delta1 below. The right object reaches the paper edge but E and subscript2 survive. H omits the diagram.',
       'lower_diagram','omission','3 omissions')
change('Thin other-hand foliation6',r'\margin{6}','',r'\margin{6}',
       'The lower-left thin grey loop and rising stroke read6; its light, narrow pen differs from the author’s dark circled3s. It is retained as a margin item.',
       'folio6','omission','3 omissions')

assert len(changes)==43, len(changes)

# Every supplied difference is accounted for without treating TeX spacing or
# H's explicitly editorial prose as manuscript words.
dc = {}
def cover(nums, classification, ids, reason):
    for n in nums:
        dc[f'D{n:04d}']=dict(diff_id=f'D{n:04d}',classification=classification,
                            change_ids=[f'C{x:02d}' for x in ids],reason=reason)
cover([978],'reading',[1],'The authorial circled3 is ink; scanpage7 is only an editorial marker.')
cover([979,980,984,985,986,1017,1019,1020],'macro-only',[],'The tokenized comma comes from TeX thin-space commands, not a written punctuation difference.')
cover([981],'reading',[2],'The top identity is canceled and has no final comma.')
cover([982],'reading',[3],'The rho equality belongs to the canceled block and has no final comma.')
cover([983],'reading',[4],'H condenses away the separate two-row coordinate/projection diagram.')
cover([987],'reading',[5],'The canceled p0p12sigma1 equation has no terminal stop.')
cover([988],'reading',[6],'The separate upper (x,x,y) is ink omitted in H; Le calcul de is editorial connective prose.')
cover([989],'editorial-only',[],'H supplies est mené en coordonnées as a synopsis; these words are not a manuscript reading.')
cover([990],'reading',[7],'The rho coordinate row visibly has the second closing parenthesis.')
cover([991,992],'reading',[8,9,10],'The separate delta tuple, bare right-hand triple and repeated left tuples are retained in their canceled state and actual arrangement.')
cover([993],'editorial-only',[],'H supplies enfin to join separate calculations; it is not source prose.')
cover([994],'reading',[11,12],'The extra source number3 and canceled last rows are retained; the long H note about the curves is editorial.')
cover([995],'reading',[13],'The written short form has a raised t; H expands it to point.')
cover([996],'reading',[14],'The crop settles C’s donc/les doubt in favor of donc.')
cover([997],'reading',[15],'The descending p and joined ar of par are visible.')
cover([998,999],'reading',[16],'The written composition is delta1delta0 with no internal comma or comma before E1.')
cover([1000],'reading',[17],'The first indexed sign is calligraphic G2.')
cover([1001],'reading',[18],'The second indexed sign is calligraphic G3.')
cover([1002],'reading',[19,20],'The main singular la ponctuation and separate quoted marginal ponctués are both read directly.')
cover([1003],'reading',[20,21,22,23],'The margin and two distinct deleted lines remain separate; the initial deleted delta1 and respecte are readable.')
cover([1004],'reading',[24],'Live initial Donc is favored by the small rounded o and nc ending.')
cover([1005],'reading',[25],'Second occurrence of G2, read from its enclosing bowl and internal return.')
cover([1006],'reading',[26],'Second occurrence of G3, with the same bottom return despite a squarer top.')
cover([1007],'macro-only',[],'Ampersand-replacement syntax changes no written content.')
cover([1008,1009,1010],'reading',[27],'Source upper left arrow is straight; lower right arrow is curved, with labels on their actual sides.')
cover([1011],'reading',[28],'The source has comma plus où, not i.e.')
cover([1012],'reading',[30],'Visible low e supports respectent, with the compressed edge ending narrowly doubtful.')
cover([1013],'reading',[31],'The written stem is ponctu-, not pointa-.')
cover([1014],'reading',[32],'The accent and short o/u trace read où.')
cover([1015],'reading',[33],'Satisfont has a short ending, without H’s added ai/sa run.')
cover([1016,1021],'reading',[34],'The actual enclosing shape is rectangular, not a cases brace.')
cover([1018],'reading',[35],'The entire parenthetic marked-point explanation is visible, with raised t.')
cover([1022],'editorial-only',[],'H’s introductory explanation of the second box is editorial; the candidate retains the actual small boxed rows.')
cover([1023,1025],'editorial-only',[],'H’s comma separates formulas in its prose synopsis; it is not a source punctuation reading.')
cover([1024],'reading',[36],'The under-bracket delta1 label is actual ink omitted from H’s recap.')
cover([1026],'reading',[37],'The under-bracket delta3 label is actual ink omitted from H’s recap.')
cover([1027,1028,1029],'reading',[38],'The literal parenthetic application de E1 sur e1 is retained; H paraphrases it as a constant map.')
cover([1030],'reading',[39,40,41],'Live underlined p11 and the two distinct heavily canceled entries are not the same as H’s editorial recap.')
cover([1031,1032],'reading',[42,43],'The actual lower-right diagram and thin foliation6 are present; H’s remaining prose is editorial.')
assert set(dc)=={d['diff_id'] for d in P['differences']}

decisions=[]
mark_data=[
('M0754','first','donc','opening_donc_par','high','Tall d and reduced onc run precede a separate par.'),
('M0755','alternative',r'\mathcal G_2','first_groups','high','Broad bowl enclosing an inward horizontal return; small2.'),
('M0756','alternative',r'\mathcal G_3','first_groups','high','Repeated G bowl and internal return; separate3.'),
('M0757','first','la ponctuation','first_ponctuation','high','Singular determiner and noun lack final s; c/t and tion are visible.'),
('M0758','first',Q+"ponctués''",'margin_ponctues','high','Paired quotation ticks, internal n/c/t and accented final e with s.'),
('M0759','first','Donc','donc_operations','medium','Capital D, small rounded o and compressed nc before comma.'),
('M0760','alternative',r'\mathcal G_2','second_groups','high','Large enclosing bowl and low internal G return, index2.'),
('M0761','alternative',r'\mathcal G_3','second_groups','high','Squarer upper bowl but same low inward G return, index3.')]
for id,decision,reading,crop,confidence,ink in mark_data:
    decisions.append(dict(id=id,cote='151',scan='7',decision=decision,reading=reading,
                          ink=ink,crop=CM[crop]['crop'],box=CM[crop]['box'],confidence=confidence))

record=dict(page='151_scan007',cote='151',scan='7',
 reader='reader_a; GPT-6 Astra Pro; effort not exposed; run SP92',
 line_count=53,
 line_count_note='53 written baseline units: parallel calculation columns count separately; detached brace/arrow labels, the insertion, multiline parenthetic, two circled3s and thin foliation6 each count at their written baseline. Cancellation strokes and box rules do not count.',
 half_review='One successful whole-source view for layout after an earlier truncated tool return; both supplied native overlapping halves then viewed once. Every word, symbol, numeral, arrow end, revision, margin item and agreed C/H reading was read directly. All34 saved original-box crops were viewed. Original28 boxes were subsequently rendered at2400px with LANCZOS without changing their bounds; no OCR, external sources or compilation used.',
 deletion_insertion_review=[
 {'place':'Upper draft block','C_items':'All nine C deleted displays/diagram groups','state':'deleted en bloc','bounds':'Both top equalities, two-row diagram, p0p12sigma1 equality, separate upper tuple, rho coordinate calculation, delta tuple, bare right triple, two left tuples, last mapping and sigma1 line.','attachment':'Three broad diagonals and the sweeping left/bottom cancellation enclose the complete upper draft, ending above the live circled3 and Si paragraph.'},
 {'place':'Deleted short line Donc./On a.','state':'deleted; unresolved internal letters','bounds':'Only the short separate word and its stop.','attachment':'Independent abandoned opening above the deleted delta1 phrase; not joined to live Donc.'},
 {'place':'Deleted delta1 respecte les/le','state':'deleted','bounds':'Initial delta1, respecte and last short determiner.','attachment':'A horizontal cancellation crosses this whole line; the group signs below remain live.'},
 {'place':'et p12 above right-edge prose','state':'live insertion','bounds':'et and p12 only.','attachment':'Curved leader attaches immediately after baseline delta1 and before respectent. The leader is not a parenthesis or strike.'},
 {'place':'Marginal quoted ponctués','state':'live margin note','bounds':'Round parentheses, paired quotes and ponctués.','attachment':'Beside the end of the first live paragraph; not part of the later et p12 insertion.'},
 {'place':'Small-box live relations','state':'live','bounds':'All three left rows, two under-bracket labels, parenthetical application de E1 sur e1; plus adjacent underlined relation and sigma2delta2=delta2.','attachment':'The small compartment shares the outer box’s right/bottom border. Its nearby diagonal does not cancel the three left rows.'},
 {'place':'Right canceled repeated p12sigma3 relation','state':'deleted with partial recovery','bounds':'Complete repeated relation, not the live underlined relation above.','attachment':'Dense oblique hatching crosses this row; exposed p12sigma3 and final p12 are retained, central equals/sigma stays doubtful.'},
 {'place':'Right separate id-like entry','state':'deleted, narrowly unresolved','bounds':'Only the compact small entry below-left of the repeated relation.','attachment':'Separate hatching; not a label of the lower diagram.'}
 ],
 changes=changes,diff_coverage=[dc[d['diff_id']] for d in P['differences']],
 decisions=decisions,check_events=[])

inventory=[]
def item(element,kind,position,first,hand='author'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,
                          position=position,first_words_or_objects=first,transcribed='yes'))
item('Upper authorial foliation','margin note','upper center',r'\textcircled{3}')
item('Canceled p0 identity with lower label','deletion','top left',r'p_0p_{12}=p_0p_{13}')
item('Canceled rho equality','deletion','top right',r'\rho^2\sigma_2=\sigma_3\rho^2')
item('Canceled coordinate/projection diagram','diagram','upper right, two rows',r'(x,y,z); (z,y,x); (x,z); x')
item('Canceled p0p12sigma1 equality','deletion','upper left second formula',r'p_0p_{12}\sigma_1=p_0p_{12}')
item('Separate canceled tuple','deletion','left below second formula','(x,x,y)')
item('Canceled rho coordinate calculation','diagram','right middle of discarded block',r'\rho^2\sigma_2: (x,y,z)')
item('Canceled delta1sigma formula','deletion','left middle',r'\delta_1\sigma=(x,y,y)')
item('Canceled bare triple','deletion','right below rho continuation','z,x,y')
item('Canceled repeated left tuple','deletion','left lower middle',r'(x,\unsure{x},y)')
item('Canceled reversed tuple','deletion','left below repeated tuple','(y,y,x)')
item('Canceled last coordinate mapping','diagram','lower right of draft','(x,y,z) to (z,x,y)')
item('Canceled sigma1 coordinate formula','deletion','bottom right of draft',r'(x,z,y)=\sigma_1')
item('Repeated authorial foliation','margin note','left between canceled and live blocks',r'\textcircled{3}')
item('First live paragraph','text','middle, three lines','Si E0 est réduit à un p-t')
item('Quoted parenthetic marginal note','margin note','right after first paragraph',Q+"ponctués''")
item('Canceled alternative opening','deletion','left before second live paragraph',r'\unsure{Donc.|On a.}')
item('Canceled delta1 phrase','deletion','left below canceled opening',r'\delta_1 respecte \unsure{les|le}')
item('Second live paragraph and five-relation lead-in','text','middle-lower, four baselines','Donc, en plus des opérations')
item('Main E1/E2 diagram','diagram','within second live paragraph','E1, E2; p12 above, delta1 below')
item('Added second map in pointedness assertion','insertion','above right-edge respectent','et p12')
item('Main five-row boxed relations','display','bottom outer rectangle',r'p_{12}\delta_1=\sigma')
item('Main bracket labels','display','below rho delta1 and rho2delta1',r'\delta_3; \delta_2')
item('Marked-point parenthetic','text','right of main constant-map row','(p-t marqué de E1)')
item('Small inner boxed relations','display','lower right within outer rectangle',r'p_{12}\delta_2=\mathrm{id}_{E_1}')
item('Small-box bracket labels','display','below rho delta2 and rho2delta2',r'\delta_1; \delta_3')
item('Small-box parenthetic','margin note','three short lines to right of e1','(application de E1 sur e1)')
item('Underlined live relation with p11','display','right upper edge of small compartment',r'p_{12}\sigma_3=\sigma p_{11}')
item('Second live right relation','display','below underline',r'\sigma_2\delta_2=\delta_2')
item('Heavily canceled repeated relation','deletion','right beneath live equations',r'p_{12}\sigma_3\unsure{=\sigma}p_{12}')
item('Separate canceled id-like entry','deletion','below-left of repeated relation',r'\unsure{\mathrm{id}}')
item('Lower right repeated diagram','diagram','bottom right across box border','E1, E2; p12 and delta1')
item('Thin foliation6','margin note','bottom left','6','other hand: thin grey foliation')
record['inventory']=inventory
record['notes']="""## Page content and mathematical rereading

The page has two authorial circled 3s, one beside an abandoned upper calculation block and one before the live paragraph. The thin grey 6 at lower left is another hand's foliation. No title or date is written.

The discarded work gives compositions involving p0, p12, p13, rho and sigma, followed by repeated coordinate permutations/projections. Every repetition is retained, including the separate upper (x,x,y), the bare z,x,y and the doubled closing parenthesis in the rho²sigma₂ row. Three long diagonal strokes and a sweeping left/bottom boundary cancel this upper draft as a block; they are not ordinary diagram arrows.

The live paragraph says that when E0 is reduced to a point (written with the short form p and raised t), delta0 and delta1delta0 make E1 and E2 pointed sets, and the written groups G2,G3 respect the pointing. The page then adds the maps delta1 and p12 and lists five supplementary relations. A smaller compartment works with delta2; adjacent live and canceled equations and a repeated E1/E2 diagram remain separately transcribed. This describes the claims on the page; no proof verification or computation was performed by this reader.

Whole formulas were re-read wherever a label, index or state was at issue. The four group signs have enclosing G bowls and low inward returns, not S forms. Every delta/rho index and all four under-bracket labels were checked. In the underlined right-hand relation, the RHS really has two short upright numeral strokes after p, unlike the clear 2 on the left. The candidate therefore preserves p11 at medium confidence even though p12 recurs elsewhere; this is a literal possible slip, not a repaired equality. The lower diagram retains its written delta1 label.

## Revisions, placement and graphical marks

The separate canceled opening Donc./On a. remains uncertain. In the following canceled phrase the initial delta1 is exposed enough to recover, while the final les/le is still partly covered by the stroke. The et p12 above the later prose is live and attaches after delta1 by a curved leader; the curve does not supply a parenthesis. The quoted ponctués remains an independent marginal parenthetic by the first paragraph.

The top coordinate/projection diagram has a clear chevron on its first tail-bar arrow. The later rho continuation instead has a little open loop at the right terminal. The last mapping has a square downturned right terminal with a lower leftward return. These endpoints are encoded literally as drawing geometry, without substituting a uniform mapsto. All tuple letters remain ordinary mathematical node text. Each complete discarded diagram is inside a deleted wrapper around an indivisible mbox, so its arrow paths as well as its nodes carry the cancellation state; the paragraph-producing diagram wrapper stays outside. The main live p12 arrow is straight and leftward; delta1 runs below on a rightward curve. The bottom repeated diagram has the same directions and a shallower lower curve.

The small box is a compartment within the lower right of the large outer rectangle, sharing its right and bottom border. Marginal typesetting follows the supplied conventions; source positions and the shared boundary are documented. The long line under the live p12sigma3=sigma p11 is an underline. Only the repeated equation and separate id-like mark below it have dense hatching. The former can be narrowed to exposed p12sigma3 and final p12 with only the intervening equals/sigma doubtful; the latter remains doubtful as id.

## Edge, spelling and witnesses

The ending of respectent touches the right paper edge. The low e-like loop distinguishes it from H's respectant, but the final compressed n/t cannot be split with certainty, so respect followed by unsure ent is retained. No off-edge punctuation is supplied. The right E2 of the lower diagram also approaches the edge, but its E and index2 remain visible.

Both point abbreviations have raised t and are not expanded. The stop in ens. is visible. The main phrase is singular la ponctuation; the later phrase is plural les ponctuations. Paired quotation ticks, accents and actual punctuation are retained. H's connective summaries (Le calcul de, est mené en coordonnées, enfin and its long notes) are not source prose and are excluded from correction counts as editorial. TeX thin spaces are likewise not commas on the page.

There was no actual proof check, independent re-proof, computation, formal certificate or mathematical use-check by this reader. The record therefore has no check events.
"""
record['notation']=[
 dict(sign=r'\mathcal G_2,\mathcal G_3',reading='Calligraphic capital G with indices2 and3',evidence='All four signs have an outer bowl and a low inward horizontal/looped return; even the squarer second G3 keeps the same return.'),
 dict(sign=r'p\textsuperscript{t}',reading='Point abbreviation with raised t',evidence='In the opening and marked-point parenthetic, t finishes near the upper p bowl, above the main baseline.'),
 dict(sign='Tail-bar shaft with a square downturned terminal',reading='Literal final coordinate-mapping mark; no chevron supplied',evidence='The last upper mapping ends in an upright and short leftward lower return.'),
 dict(sign='Tail-bar shaft with a loop at its right end',reading='Literal continuation arrow in the canceled rho calculation',evidence='Small open loop distinct from the clear upper diagram chevron.'),
 dict(sign=r'p_{11}',reading='Literal RHS index11 in the underlined right relation',evidence='Two short upright strokes; the left index12 supplies a local contrast for the missing2-foot.'),
 dict(sign='Thin grey6',reading='Other-hand foliation',evidence='Lower-left fine grey ink contrasts with the author’s two dark circled3s.')
]
record['hand_log']=[
 dict(habit='Capital G may be mistaken for an ornate S; the inward low return distinguishes it.',places=['151_scan007 first paragraph G2/G3','151_scan007 second paragraph G2/G3'],scope='Confirmed in all four occurrences on this page.',witness_errors='C offered S/G alternatives; H printed S at all four.'),
 dict(habit='Terminal prose syllables can collapse into low runs and a single high arch.',places=['151_scan007 donc','151_scan007 respectent edge','151_scan007 satisfont'],scope='Occurrence-specific; no grammatical completion used.',witness_errors='H les/Dans, respectant and satisfaisant; the edge ending remains narrowly doubtful.'),
 dict(habit='Small t in the point abbreviation is genuinely raised, not merely a tall ascender.',places=['151_scan007 opening p-t','151_scan007 marked-point parenthetic'],scope='Both written occurrences.',witness_errors='C flattens both t positions; H expands the first abbreviation and omits the second parenthetic.'),
 dict(habit='Mapping terminals vary between a clear chevron, an open loop and a square turned end.',places=['151_scan007 upper diagram','151_scan007 rho continuation','151_scan007 last coordinate mapping'],scope='Read separately; no single arrow-head convention imposed.',witness_errors='C/H generic mapsto loses the later endpoint distinctions.'),
 dict(habit='Separate dark index uprights can be normalized to the more expected12.',places=['151_scan007 underlined right-hand relation'],scope='Only this RHS shows11; other12s remain12.',witness_errors='Both C and H give p12 where the crop shows two upright strokes.')
]
record['abbreviations']=[dict(form=r'p\textsuperscript{t}',expansion='point'),dict(form='ens.',expansion='ensembles'),dict(form=r'\mathrm{id}',expansion='identity map; the separate canceled occurrence remains doubtful')]
record['doubts']=[
 dict(place='Middle coordinate of the lower repeated left tuple',reading=r'(x,\unsure{x},y)',alternatives=['x with retracing','unresolved overwritten coordinate'],confidence='low',reason='Dense local retracing covers the middle letter; the other tuple letters are exposed. Added doubt only against C.'),
 dict(place='Separate deleted opening',reading=r'\deleted{\unsure{Donc.|On a.}}',alternatives=['Donc.','On a.'],confidence='low',reason='Horizontal cancellation merges the small internal letters; the capital loop and stop survive.'),
 dict(place='Final determiner in deleted delta1 phrase',reading=r'\deleted{respecte \unsure{les|le}}',alternatives=['les','le'],confidence='medium',reason='The final return merges with the deletion line; a distinct final s cannot be certified.'),
 dict(place='Right-edge respectent ending',reading=r'respect\unsure{ent}',alternatives=['ent','terminal n/t boundary obscured at edge'],confidence='medium',reason='Visible e-like loop favors ent over ant; terminal arch and return touch the paper edge.'),
 dict(place='Center of the canceled right repeated relation',reading=r'p_{12}\sigma_3\unsure{=\sigma}p_{12}',alternatives=['equals followed by sigma','central hatching not fully separable'],confidence='low',reason='Only the exposed left and right groups are recovered; central equals/sigma is entangled with the hatching.'),
 dict(place='Separate canceled id-like entry',reading=r'\deleted{\unsure{\mathrm{id}}}',alternatives=['id','unresolved short canceled mathematical mark'],confidence='low',reason='The upright/loop remains merged with dense hatching; no full recovery claimed.')
]

boxes=[]
def blind(kind,coords,reading):
    x0,y0,x1,y1=coords
    boxes.append(dict(box=f'B{len(boxes)+1:02d}',kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
def bc(kind,crop,reading): blind(kind,CM[crop]['box'],reading)
bc('authorial circled number','circled_top',r'\mspage{\textcircled{3}}')
bc('whole canceled identity, digits and lower bracket label','top_p0',changes[1]['final'])
bc('whole canceled equality and indices','top_rho',changes[2]['final'])
bc('whole canceled diagram','top_diagram',top_diagram)
bc('whole canceled equality and indices','top_p0sigma',changes[4]['final'])
bc('separate canceled tuple','top_xxy',r'\deleted{(x,x,y)}')
bc('whole canceled delta formula and lower tuples','top_delta_triplets',r'\deleted{\delta_1\sigma=(x,y,y)}\\\deleted{(x,\unsure{x},y)}\\\deleted{(y,y,x)}')
bc('whole canceled rho coordinate calculation and literal arrows','top_rho_mapping',rho_diagram)
bc('separate bare canceled triple','top_zxy',r'\deleted{z,x,y}')
bc('whole last canceled mapping and sigma1 equation','top_last_mapping',last_diagram)
bc('repeated authorial circled number','circled_numbers',r'\mspage{\textcircled{3}}')
blind('opening line with E0, abbreviation and lexical decision',[240,1060,1480,1175],r'Si $E_0$ est réduit à un p\textsuperscript{t}, donc par')
blind('delta composition and numbered objects on second prose line',[200,1190,1565,1305],r'$\delta_0,\delta_1\delta_0$ $E_1,E_2$ deviennent des ens. pointés,')
bc('first pair of doubtful group signs and indices','first_groups',r'$\mathcal G_2,\mathcal G_3$')
bc('singular noun and determiner lexical decision','first_ponctuation','la ponctuation.')
bc('complete marginal parenthetic','margin_ponctues','\\margin{('+Q+"ponctués'')}")
bc('two separate canceled prose lines','cancelled_words',r'\deleted{\unsure{Donc.|On a.}}\\$\deleted{\delta_1}$ \deleted{respecte \unsure{les|le}}')
bc('live paragraph opening lexical decision; overlapping inserted item separately covered','donc_operations','Donc, en plus des opérations de')
bc('second group pair and following words','second_groups',r'$\mathcal G_2,\mathcal G_3$, on a')
bc('complete main E1/E2 diagram and numeric labels','main_diagram',main_diagram)
bc('where clause and live insertion with its attachment','ou_insertion',r', où $\delta_1$ \inserted{et $p_{12}$} respect\unsure{ent}')
bc('plural noun lexical decision','les_ponctuations','les ponctuations,')
bc('where clause, numbered maps and lexical decision','et_ou_satisfont',r'et où $p_{12},\delta_1$ satisfont')
bc('complete main five-row boxed system, all numeric labels and parenthetic; inner compartment separately covered','main_box',main_box)
bc('small-box three-row system, bracket labels and multiline parenthetic','right_box',right_box)
blind('live underlined formula and following sigma2delta2 equation',[1260,2030,1575,2150],r'$\uline{p_{12}\sigma_3=\sigma p_{11}}$\\$\sigma_2\delta_2=\delta_2$')
bc('whole canceled repeated relation','right_cancelled_formula',r'$\deleted{p_{12}\sigma_3\unsure{=\sigma}p_{12}}$')
bc('separate canceled id-like entry','right_cancelled_id',r'$\deleted{\unsure{\mathrm{id}}}$')
bc('complete lower-right diagram and all numeric labels','lower_diagram',lower_diagram)
bc('other-hand foliation','folio6',r'\margin{6}')
record['second_boxes']=boxes
record['crops']=[dict(place=name,**data) for name,data in CM.items()]

allowed={'misread word','misread symbol or index','omission','text not on the page',
'deletion state (struck given live or live given struck)','insertion or placement',
'abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in changes)
assert [x['id'] for x in decisions]==[x['id'] for x in P['marks']]
assert all((BASE/'SP92_C13_150+151_work'/x['crop']).exists() for x in changes)
assert all(x['viewed'] for x in record['crops'])
(OUT/'151_scan007.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(page=record['page'],changes=len(changes),crops=len(CM),
 differences=len(dc),marks=len(decisions),inventory=len(inventory),second_boxes=len(boxes),
 unresolved=len(record['doubts'])),ensure_ascii=False))
