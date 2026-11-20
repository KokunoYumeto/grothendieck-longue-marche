"""Explicit main-reader adjudication, after all three independent returns."""
from adjudication import Page,O
import copy,json
p=Page(11,brief='v02')
p.text('R1',[
 (r'H^{\handwritten{2}}',r'H^{\unsure{2|\handwritten{2}}}'),
 ("qu'on notera",r"qu'on no\deleted{o}tera"),
 ('soit vraiment',r'soit vrai\deleted{\unsure{e}}ment'),
 ('hypothèses restrictives',r'hypothèses restricti\deleted{b}ves'),
])
# Each triple is the reading actually returned; combined/absent rows are explicit.
maps={1:(1,1,1),2:(2,2,'R3: both exponents m\u2032−1 and m−1 confirmed'),3:(3,3,4),4:(4,5,5),5:(5,4,6),6:(6,6,7),7:(7,'t_0(S)',8),8:(8,'t_0',9),9:(9,7,10),10:(10,9,11),11:(11,8,12),12:(12,10,13),13:(13,14,14),14:(14,15,15),15:(15,16,16),16:(16,r'\handwritten{\leqslant}',r'\handwritten{\leqslant}'),17:(17,'no terminal period',17),18:(18,'new paragraph before Sous',19),19:(19,'outer NB unclosed',18),20:(20,19,20),21:(21,18,21),22:(22,'z=Z(t_1)-Z(t_0)',22),23:(23,20,23),24:(24,21,24),25:(25,22,25),26:(26,23,26),27:(27,24,27)}
rows=[]
for j,triple in maps.items():
 variants=[f'{rr}-011-{v:02d}' if isinstance(v,int) else v for rr,v in zip(('R1','R2','R3'),triple)]
 rows.append(p.row(f'R1-011-{j:02d}',variants))
def setrow(j,**kw):rows[j-1].update(kw)
setrow(1,evidence='crops/scan011/R2/first_left_coefficient.jpg',decision='All three put ordinary E first. Main inspection confirms overlapping straight and rounded contours without a separable old/new sequence. All six literal candidates remain; the expected coefficient F does not decide the ink.',consequential='The left coefficient remains unidentified; it is not silently restored to F from the target coefficient.')
setrow(2,decision='All readers independently confirm the same degrees and ordinary R capitals from the halves/crops. No transcription change or mathematical proof is claimed.')
setrow(3,evidence='crops/scan011/MAIN/drux.jpg',decision='All readers retain drux. Main crop shows the second live letter with r shoulder, followed by u and x; H’s grammatical deux is rejected.')
setrow(4,against_H=False,evidence='crops/scan011/R2/first_integer_coefficient.jpg',decision='All three read the mechanical crossed glyph as chi|ell and a single underlined Z. Main inspection agrees; alphabet uncertainty is not resolved by the prime-number role.')
setrow(5,final=r'H^{\unsure{2|\handwritten{2}}}',against_C=True,confidence='medium',ink='The digit has a smooth curved top, diagonal descent and flat foot like the 2 in the following two 2n exponents. Machine type is the preferred source layer; the reproduction does not exclude pen work of the same shape. The numerical value is certainly 2.',evidence='crops/scan011/R2/first_integer_coefficient.jpg; crops/scan011/R2/cycle_class_coefficient.jpg; crops/scan011/R2/image_class_coefficient.jpg',decision='R1/R3 assign pen provenance; R2 prefers type but explicitly retains doubt. Main comparison favours the mechanically repeated numeral, with the pen alternative marked in place. No H error is counted for absent provenance markup.')
setrow(6,decision='All readers independently confirm final i without e in the halves. The grammatical mismatch is retained.')
setrow(7,evidence='crops/scan011/R1/section_indices.jpg',decision='R1/R3 prefer literal lowercase o; R2 retains zero. The main crop shows an o-height rounded glyph substantially shorter than adjacent 1. Use o|0 initially, with o at the two same-shaped recurrences.')
setrow(8,evidence='crops/scan011/R1/section_indices.jpg',decision='Same main crop as the preceding divisor difference; the second named section has the same o-height glyph. The first occurrence carries the uncertainty.')
setrow(9,evidence='crops/scan011/R2/cycle_class_coefficient.jpg',decision='Main crop confirms a baseline serifed x, agreeing with all three readers and C.')
setrow(10,against_H=False,evidence='crops/scan011/R2/cycle_class_coefficient.jpg',decision='Main crop confirms the same mechanical hooked/crossed subscript and separately underlined Z. The first occurrence carries the alphabet uncertainty.')
setrow(11,evidence='crops/scan011/R2/cycle_class_coefficient.jpg',decision='All three and the main crop confirm ordinary H, degree 2n and capital class Z. Handwritten membership provenance is inventory information, not an H difference by itself.')
setrow(12,evidence='crops/scan011/R2/cycle_class_coefficient.jpg',decision='The same crop includes the separate inline occurrence and confirms the baseline typed x and lowered S.')
setrow(13,against_H=False,confidence='low',evidence='crops/scan011/R2/restriction_edge_inequality.jpg',decision='All three retain nulle with a clipped last letter. Main crop shows null and only the left fragment of the last curve. H has the same word, so differing editorial doubt markup alone is not an H collation error.')
setrow(14,evidence='crops/scan011/MAIN/dycle_quotes.jpg',decision='Main crop confirms the ascender of d in dycle, with a normal c in the later cycle on the same line for comparison.')
setrow(15,evidence='crops/scan011/MAIN/dycle_quotes.jpg',decision='Main crop confirms paired upright typewriter quotation strokes, not guillemets.')
setrow(16,evidence='crops/scan011/R2/restriction_edge_inequality.jpg',decision='All three choose a slanted lower stroke. Main inspection confirms its direction. The C change is a literal shape refinement of the same inequality, not a reversed mathematical bound.')
setrow(17,evidence='crops/scan011/R2/restriction_edge_inequality.jpg',confidence='medium',decision='All three find no visible terminal stop; main inspection agrees. The right page edge is clipped, so no invisible punctuation is supplied.')
setrow(18,evidence='crops/scan011/MAIN/transition_sous.jpg',decision='R1/R3 retain an ordinary line transition; R2 follows C’s paragraph division. Main crop shows the same left margin and ordinary line spacing, without indentation or blank. No paragraph break is introduced; authorial intention beyond those visible cues is unknown.')
setrow(19,evidence='crops/scan011/R2/restriction_edge_inequality.jpg',decision='All three retain the unclosed outer NB. The two detached edge traces do not establish an authorial closing parenthesis.')
setrow(20,against_H=False,evidence='crops/scan011/R2/image_class_coefficient.jpg',decision='Main crop confirms the repeated underlined single Z and mechanical crossed subscript; first occurrence carries uncertainty.')
setrow(21,evidence='crops/scan011/R2/image_class_coefficient.jpg',decision='All three and the main crop confirm 2n without a prime or descender.')
setrow(22,evidence='crops/scan011/MAIN/section_final.jpg',decision='R1/R3 prefer o and R2 zero. Main crop again shows a round glyph of lower x-height than 1; retain o under the first occurrence’s o|0 uncertainty. Lowercase initial z, capital action Z and minus are clear.')
setrow(23,evidence='crops/scan011/MAIN/classes_underline.jpg',against_H=False,decision='All readers and the main crop see upright typed letters and one separate pen underline. Use the established uline macro; record pen provenance for the rule in inventory, without wrapping the command alone or relabelling the typed word. H’s supplied preamble uses emph for the author’s own emphasis, so this equivalent markup is not counted as an H reading error.')
setrow(24,evidence='crops/scan011/R2/last_correction.jpg',decision='Main crop confirms one short typed dash; H’s doubled dash is not retained.')
setrow(25,evidence='crops/scan011/R2/last_correction.jpg',decision='All three retain the same three live-word alternatives. Main crop cannot separate the nearly upright accent from adjacent overtyping; no doubt is removed.')
setrow(26,evidence='crops/scan011/R2/last_correction.jpg',decision='All three retain ax|xx. Main crop confirms two cancelled cells and an a-like lower contour in the first; a complete old word cannot be restored.')
setrow(27,decision='All three independently confirm the final stop without an outer closing parenthesis in the bottom half. No missing close is supplied.')
extra=[]
for src,variants,final,ink,decision in [
 ('R2-011-11',['qu\u2019on notera','R2-011-11','qu\u2019on notera'],r"qu'on no\deleted{o}tera",'A complete round bowl remains under/around the tall t stem and crossbar, at one overtyped cell. The old o and live t are both discernible.','Only R2 retained the old cell. The main crop supports old o without an additional letter alternative; the live word remains notera.'),
 ('R2-011-12',['vraiment','R2-011-12','vraiment'],r'vrai\deleted{\unsure{e}}ment','An extra cell between i and m has crossing cancellation strokes and an e-like bowl/bar beneath. Its cancellation is clear, but the underlying e is partly obscured.','Only R2 retained the extra cancelled cell. Main inspection confirms it and retains uncertainty on old e.'),
 ('R2-011-13',['restrictives','R2-011-13','restrictives'],r'restricti\deleted{b}ves','An old ascender with top serif and lower closed bowl is visible beneath the live v diagonals at the same cell. This is a b overtyped by v, not mere heavy printing.','Only R2 retained the old letter. Main inspection resolves the old b from the surviving ascender and bowl; the live word remains restrictives.')]:
 extra.append(p.row(src,variants,final=final,ink=ink,decision=decision,confidence='medium'))
rows[12:12]=extra
inv=p.inventory('R2')
for x in inv:
 x['sheet_kind']='typescript'
 if x['element']=='011-I07':x.update(first_words_or_objects='2 with explicit type/pen provenance uncertainty; type preferred',hand='typewriter preferred; pen not excluded')
 if x['element']=='011-I13':x['first_words_or_objects']='old o under live t, resolved from round bowl'
 if x['element']=='011-I16':x['first_words_or_objects']='old b under live v, resolved from ascender and bowl'
 if x['element']=='011-D05':x['first_words_or_objects']='z = Z(t_1) - Z(t_o); o/0 uncertainty at first occurrence'
 if x['element']=='011-T06':x['first_words_or_objects']='Sous ces conditions; ordinary next line, no added paragraph'
for j,x in enumerate(inv,1):x['element']=f'011-{j:02d}'
unresolved=copy.deepcopy(p.R['R1']['unresolved'])
unresolved.extend([
 dict(place='D2 numeral provenance',reading='typed 2',alternatives=['pen-filled 2'],confidence='medium',reason='Same shape as following typed-looking 2n, but instrument cannot be established conclusively. Both alternatives are marked in place; the digit itself is certain.'),
 dict(place='L12 extra cancelled cell in vraiment',reading='e',alternatives=[],confidence='medium',reason='Extra x-out cell and rounded/barred remnant visible; underlying e remains partly covered.'),
 dict(place='L15/L16 paragraph intention',reading='ordinary line transition',alternatives=['intended paragraph without an indent or blank'],confidence='medium',reason='The scan has normal line spacing and aligned left margins. Final transcription adds no blank paragraph; intended rhetorical division cannot be recovered solely from these cues.'),
])
notation=copy.deepcopy(p.R['R1']['notation'])
for x in notation:
 x['convention']=x.pop('latex')
 if x['sign']=='ordinary cohomology/direct-image capitals':x['appearance']='Single serifed H and R; the first degree-2 numeral has uncertain type/pen provenance, unlike the clearly added membership/arrow signs'
notation.append(dict(sign='typed-letter overprint',appearance='A live letter superposed on a recoverable old letter; separately an x-cancelled extra cell',convention=r'no\deleted{o}tera; vrai\deleted{\unsure{e}}ment; restricti\deleted{b}ves',evidence='011: crops/scan011/R2/vraiment_overtype.jpg; crops/scan011/R2/restrictives.jpg'))
checks=p.checks()
checks.extend([
 dict(statement_id='N011.2-primitive-background',type='carried as background without fault found',outcome='The page’s primitivity assertion and allowance of an arbitrary relative degree-zero divisor were transcribed and described. Only the conditional numerical degree subtraction was computed by the readers; no primitive-cohomology theorem was proved.'),
 dict(statement_id='N011.3-cycle-class-background',type='carried as background without fault found',outcome='The degree-2n correspondence class, induced class x and cycle difference are source assertions described in the notes. No existence or functoriality theorem for cycle classes/intersections was checked; the source reservations remain explicit.'),
])
notes=[
 'This is the continuation of the annotated typescript, with handwritten text-page number 2 and archive sheet number 10 (comment only). There is no new title, date or total page count.',
 'The page continues an étale-local map of higher direct images in degrees m\u2032−1 and m−1 and its H¹(S, ) map. It specializes to a relative curve C with m\u2032=2 and the divisor difference t₁(S)−tₒ(S). The round subscript is literally o-like; o|0 remains marked. The page asserts primitivity for connected geometric fibres. The readers checked only the conditional arithmetic degree 1−1=0; they did not prove primitivity.',
 'It writes a degree-2n class with twist n for a codimension-n correspondence on Y x_S C and identifies its image x with the class of z=Z(t₁)−Z(tₒ). The first direct-image coefficient is still a fused uncertain capital, so it is not restored to expected F. The numerical exponent 2 is secure, but type versus pen provenance is marked as uncertain.',
 'The author’s reservation is explicit: “pour que cette classe de cohomologie soit vraiment définie en l’état actuel de la Science, il faut faire des hypothèses restrictives”. He lists finite type over a field, excellent of characteristic nulle (last letter clipped), or a relative cycle with fibrewise codimension ≤ n. The sloping lower stroke of the inequality is preserved; no conjectural reversal is made. These hypotheses were read, not certified sufficient.',
 'The final NB says “on suppose que les intersections écrites ont un sens” and alternatively speaks of underlined classes of cycles; it again qualifies the latter case by finite type over a field. Both long outer NB parentheses remain unclosed, and no period is supplied after fibre par fibre.',
 'Main inspection confirmed old o under the t of notera, an uncertain old e cancelled between i and m in vraiment, and old b under the v of restrictives. These were absent from both witnesses and from R1/R3; the old letters are retained without restoring whole previous words. Visible drux, défini and dycle are not grammaticalized.',
 'The margin-edge diagonal traces are not securely authorial or textual and are documented as unresolved source-edge marks, without inventing a parenthesis or drawing. The transition before Sous has ordinary spacing and alignment, so no paragraph break is added.',
]
views=[f'crops/scan011/R2/{n}.jpg' for n in ('first_left_coefficient','first_integer_coefficient','last_correction','vraiment_overtype','restrictives','restriction_edge_inequality','cycle_class_coefficient','image_class_coefficient')]
views+=['crops/scan011/R1/section_indices.jpg']
views+=[f'crops/scan011/MAIN/{n}.jpg' for n in ('drux','dycle_quotes','transition_sous','section_final','classes_underline')]
p.write(rows,inv,unresolved,notation,notes,views,
 overview='All three independent complete readings were compared. The main reader viewed nine distinct existing crops and five new local crops. The main differences concern hidden typewriter correction layers, a round section index, numeral provenance and a paragraph boundary. Shape refinements and uncertainty are distinguished from mathematical emendations; neither witness is treated as authoritative.',
 abbreviations=p.R['R1']['abbreviations'],check_events=checks,
 legibility='Live typescript is largely clear. The fused first coefficient, clipped nulle, cancelled extra e, final accent and x-outs are least secure. C preserves the obvious slips and final cancellation better than H, but both omit three smaller overtyped old letters. R1/R3 also missed those layers; R2 identified them. The type/pen provenance of the first 2 remains uncertain.',
 workflow_observation='22 independent crops (5/9/8); main reused 9 reader crops and made 5 new loci. One five-image tool output was truncated before inspection; the same saved crops were then delivered in small batches and actually inspected, without recropping. v03 adds overtyping/numeral guidance, half-only bboxes and underline convention.',sweep=[])
vp=O/'decisions/scan011_main_views.json'
d=json.loads(vp.read_text());d['delivery_exception']='A batch requesting five existing R2 crops was truncated before any images reached the main reader’s usable context. Those five files were requested again in smaller batches and inspected; no crop was regenerated and no decided locus was reread.'
vp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
