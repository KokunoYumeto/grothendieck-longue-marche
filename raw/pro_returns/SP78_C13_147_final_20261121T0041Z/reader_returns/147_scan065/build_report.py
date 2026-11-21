from pathlib import Path
import json,re
W=Path('/workspace/scratch/ea90d891106a/SP78_C13_147_work'); R=W/'reader_returns/147_scan065'
P=Path('/workspace/scratch/ea90d891106a/runtime/packets/147_scan065')
text=(R/'proposed.tex').read_text(); boxes=json.loads((R/'crop_boxes.json').read_text())
changes=[]
def change(place,c,h,final,evidence,key,confidence,ac,ah,kind,error,marked=False,consequential=False):
 changes.append(dict(id=f'065-{len(changes)+1:02d}',place=place,C=c,H=h,final=final,evidence=evidence,crop=f'147_scan065_place{key}.png',box=boxes[key],confidence=confidence,against_C=ac,against_H=ah,kind=kind,marked_in_H=marked,error_sheet_kind=error,consequential=consequential))
change('Opening formula, left member',r'M_{1,1}',r'[M_{1,1}]',r'M_{1,1}','There is blank paper to the left of M and between its final subscript1 and the equals sign. The class brackets that surround U and the subsequent strata are absent around the opening M.','01','high',False,True,'text not on the page','text not on page',False,True)
change('First formula for U, alphabet of E',r'\mathbf E^1',r'\mathbb{E}^1',r'\mathbb E^1','Inside the outer class bracket, the E has a further two-stroke upright/outline joined by its three horizontal arms. The outer bracket is separate. The letter is E, with a raised1, and is double-stroked.','02','high',True,False,'misread symbol or index','symbols and indices')
change('Prose introducing the prime notation, before pour','où de façon générale on pose,','où on a posé en général,','où de façon générale on pose,','After où are a separate de and a tall f with descending return in façon; générale begins with a looped descending g. The following on is a short group before pose. The p of pose descends, and its terminal e has no acute accent. H reorders and rewrites this phrase.','03','high',False,True,'misread word','words')
change('Prime clause, words between pour and premier','un nb','','un nb','After pour the crop has a separate low un, followed by nb with a tall b stem and return; premier follows with its descending p. Both un and the abbreviation nb are live ink.','04','high',False,True,'omission','omissions')
change('Prime clause, position of p',r'premier $p$',r'$p$ premier',r'premier $p$','Crop04 ends the prose baseline with premier. The separate p in crop11 begins the next baseline at the left margin, before the displayed zeta definition farther right. It therefore follows premier in the sentence.','11','high',False,True,'insertion or placement','insertions put in wrong place')
change('Prime clause, terminal punctuation','',',','','Neither the end of premier in crop04 nor the separate final p in crop11 is followed by a dark comma. H adds one after its reordered premier.','11','high',False,True,'text not on the page','text not on page')
change('Definition of zeta_p, first Z after Spec',r'\operatorname{Spec}\mathbf Z',r'\operatorname{Spec} \mathbb{Z}',r'\operatorname{Spec}\mathbb Z','The first Z has two separately visible slanting diagonal strokes between its top and bottom horizontals. They belong to the letter, not the neighboring class bracket.','05','high',True,False,'misread symbol or index','symbols and indices')
change('Definition of zeta_p, second Z after p',r'p\mathbf Z',r'p\mathbb{Z}',r'p\mathbb Z','The Z immediately after the descending p again has a doubled diagonal/outline, especially distinct at its lower-left turn.','05','high',True,False,'misread symbol or index','symbols and indices')
change('Map i_p!, Z with subscript p in the source',r'K_!(\mathbf Z_p)',r'K_!(\mathbb{Z}_p)',r'K_!(\mathbb Z_p)','Inside the source parentheses, the Z has two parallel diagonals; the p descends separately at its lower right.','06','high',True,False,'misread symbol or index','symbols and indices')
change('Map i_p!, Z in the target',r'K_!(\mathbf Z)',r'K_!(\mathbb{Z})',r'K_!(\mathbb Z)','The target Z repeats the paired diagonal strokes and the two horizontal ends. The closing parenthesis lies to its right and does not create the doubled stroke.','06','high',True,False,'misread symbol or index','symbols and indices')
change('Transition before the two S-prime formulas',r'De $=$','De même',r'De $=$','After the tall looped D and its joined e are exactly two separate horizontal bars. The letters of même are not written.','07','high',False,True,'abbreviation expanded or spelling modernised','abbreviations expanded spelling modernised')
change('First weighted expansion, sign before zeta3',r'\zeta_2\unsure{-|+}\zeta_3',r'\zeta_2+\zeta_3',r'\zeta_2\unsure{-|+}\zeta_3','The sign is a short horizontal stroke with a small closed or nearly closed loop near its right end. There is no clean separate vertical upright comparable to the other plus signs in this formula. Minus remains preferred, but the small loop prevents a certain exclusion of plus. This is an unresolved comparison with H, not an adjudicated H error; arithmetic does not resolve the ink.','08','medium',False,True,'misread symbol or index','symbols and indices',False,True)
change('Inside the coefficient parenthesis, canceled mark after 1/4',r'\frac14\deleted{\unsure{+}}+\frac16',r'\tfrac14+\tfrac16',r'\frac14\deleted{\unsure{+}}+\frac16','Between the live 1/4 and the clearly separate live plus before 1/6 is a compact angular overworked mark. Its oblique stem and crossing strokes obscure the original shape. C’s tentative canceled plus is retained with its doubt; H’s note acknowledges overwork here but the transcription has no canceled mark. No hidden digit is asserted.','08','low',False,True,'deletion state','struck text',True)
change('Placement of the 5/12 brace annotation',r'\overbrace{\left(\frac14\deleted{\unsure{+}}+\frac16\right)}^{5/12}',r'\underbrace{\bigl(\tfrac14+\tfrac16\bigr)}_{5/12}',r'\overbrace{\left(\frac14\deleted{\unsure{+}}+\frac16\right)}^{5/12}','The brace arches above the coefficient parenthesis, with its middle tip pointing upward. The slashed 5/12 is still higher. No underbrace or lower annotation is present.','08','high',False,True,'insertion or placement','insertions put in wrong place')
change('Next derived formula, canceled mark immediately after 7/12',r'7/12\deleted{\unsure{\zeta}}',r'\tfrac{7}{12}',r'7/12\deleted{\unsure{\zeta}}','After the slashed 7/12 and before a separate live plus there is a small densely crossed mark with short upper loops and a descending return. The crossing strokes prevent a secure original-letter reading. C’s tentative canceled zeta remains doubtful. H mentions overworked figures nearby but omits this canceled mark from its formula.','09','low',False,True,'deletion state','struck text',True)
change('Lower-left pale foliation',r'\margin{64}','',r'\margin{64}','The pale separate numeral has a hooked6 with a closed lower oval, followed by a4 with a long upright/oblique stroke and cross-stroke. It lies below the displayed system, apart from the author’s ink.','10','high',False,True,'omission','omissions')

inventory=[]
def inv(kind,pos,first,hand='his hand'):
 inventory.append(dict(scan=65,sheet_kind='text',hand=hand,element=f'{len(inventory)+1:02d}',kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
inv('display','Opening baseline','Bare M_{1,1}=weighted sum of U,S0-prime,S1-prime,a2,a3')
inv('text','Below opening display','et on a')
inv('display','Next two baselines','[U]=[double-stroked E^1]−[S0]−[S1]+[a2]+[a3]=T(1)−2+zeta2+zeta3')
inv('text','Middle prose baseline and its single-letter continuation','où de façon générale on pose, pour un nb premier p')
inv('display','To the right of the continuation p','zeta_p=[Spec double-stroked Z/p double-stroked Z]=i_p!(1)')
inv('text','Left of the next displayed map','où')
inv('display','Next baseline','i_p!:K_!(double-stroked Z_p)→K_!(double-stroked Z).')
inv('text','Left transition before S-prime equations','De =')
inv('display','Two baselines before d’où','[S0-prime]=[S0]−[a2]−[a3] and [S1-prime]=[S1]−[a2]−[a3], each1−zeta2−zeta3')
inv('text','Before the weighted expansion','d’où')
inv('display','First two baselines of the expansion','[M_{1,1}]=half(T(1)−2+zeta2 sign zeta3)+(1/4+1/6)(1−zeta2−zeta3)+1/24 zeta2+1/12 zeta3')
inv('display','Above the coefficient parenthesis','Overbrace and5/12 annotation')
inv('deletion','Between 1/4 and the live plus before1/6','Tentative canceled plus, obscured by angular overwork')
inv('display','Next derived baseline','Half T(1)−7/12, canceled mark, doubtful rewritten1/8 zeta2+1/6 zeta3')
inv('deletion','Immediately after7/12','Tentative canceled zeta, under crossing strokes')
inv('display','Coefficient of zeta2 on the same derived baseline','Heavily overwritten numerator and denominator, tentatively1/8')
inv('display','Following baseline','Half(T(1)−1)−1/12+1/8 zeta2+1/6 zeta3,')
inv('text','At the right of that baseline','donc')
inv('display','Bottom, system numbered (80)','Two class formulas for M and widehat M, left brace; second adds1/2')
inv('margin note','Bottom left','64','pencil foliation; hand not confidently attributed')

doubts=[
 dict(place='M1043, sign before zeta3 in the first weighted expansion',reading=r'\unsure{-|+}',alternatives='Minus preferred; plus remains possible.',confidence='medium',reason='The crop shows a horizontal dash with a small loop at its right end but no separately legible plus upright. The later expansion would fit plus, which is a conditional arithmetic observation, not a reading of this ink.'),
 dict(place='Unindexed canceled mark in the coefficient parenthesis',reading=r'\deleted{\unsure{+}}',alternatives='Tentative canceled plus; an overworked symbol or digit cannot be excluded.',confidence='low',reason='Angular crossing strokes and two-level contours prevent recovery of every original stroke. The C doubt stays; no extra decision ID is created.'),
 dict(place='Unindexed canceled mark after7/12',reading=r'\deleted{\unsure{\zeta}}',alternatives='Tentative canceled zeta; another canceled character remains possible.',confidence='low',reason='The short upper loops, crossings and descending return do not reveal the original character securely. The C doubt stays; H’s editorial overwork note does not resolve it.'),
 dict(place='Rewritten coefficient before zeta2 on the next derived baseline',reading=r'\unsure{\frac18}',alternatives='The conventional current reading is1/8; the numerator also has a4-like triangular/crossed contour, and the underlying digit sequence is not recoverable.',confidence='low',reason='Both levels are heavily overworked. The numerator has an upright, foot, crossbar and triangular contour; the denominator has several overlapping loops. A whole-fraction doubt is added. No prior numerator or denominator is transcribed as a separately readable canceled digit.')]

notes=[
 'The manuscript opens with a weighted expression for bare M_{1,1}: one half of[U], one quarter of[S0-prime], one sixth of[S1-prime], one twenty-fourth of[a2], and one twelfth of[a3]. It then writes[U]=[double-stroked E^1]−[S0]−[S1]+[a2]+[a3]=T(1)−2+zeta2+zeta3. These geometric class identities are manuscript claims, carried as background without an independent geometric verification. The opening M has no class brackets; no correction is supplied.',
 'For a prime p, the manuscript defines zeta_p=[Spec Z/pZ]=i_p!(1), with all four Z glyphs on this and the following line double-stroked. It displays i_p!:K_!(Z_p)→K_!(Z). These are the page’s definitions and displayed map; the precise geometric formalism and the notation Z_p are not independently reconstructed from other pages. The rounded right-hand arrow tip is read with the written source/target map, without adding a hook, bar or second shaft.',
 'The two displayed stratum identities state[S0-prime]=[S0]−[a2]−[a3]=1−zeta2−zeta3 and the same expression for[S1-prime]. These identities are retained as background manuscript assertions; their geometric hypotheses were not checked.',
 'An exact rational-coefficient calculation was performed with Python fractions.Fraction. It verifies1/4+1/6=5/12. Taking the unresolved sign before zeta3 as plus gives coefficients1/2 for T(1),−7/12 for the constant,1/8 for zeta2, and1/6 for zeta3, matching the later displayed expression. Taking that sign as minus instead gives zeta3 coefficient−5/6, with the other coefficients unchanged. The rewrite−1/2−1/12=−7/12 and the addition−7/12+1/2=−1/12 also check. These are conditional algebra checks only: they neither resolve M1043 nor read the canceled and overwritten digits.',
 'System(80) states[M_{1,1}]=one half(T(1)−1)−1/12+1/8 zeta2+1/6 zeta3 and[widehat M_{1,1}]=[M_{1,1}]+1/2=one half T(1)−1/12+1/8 zeta2+1/6 zeta3. The coefficient addition is included in the exact check of note4. The geometric assertion that adjoining the boundary contributes1/2 is carried as background, not independently proved here.',
 'Physical-lines count:19. There are17 main prose/formula baselines; the isolated continuation p shares a baseline with the zeta_p definition, and donc shares the rewritten-class baseline. The separate5/12 annotation above its overbrace and the pale foliation64 add two units. Canceled marks and rewritten digits are counted with their host lines. No separate author’s ink page number is visible at the head.',
 'The full scan and both native halves were read once, line by line against both witnesses, including all numeric ink, all signs, indices, primes, exclamation marks, cancellations and the final brace. Eleven distinct places were cropped once and all eleven saved crops were viewed. Each substantive comparison cites an original-pixel crop. No OCR, web research or TeX compilation was used.',
 'Source forms retained include un nb, literal De=, the source word order premier p with p on the next baseline, and the absence of a terminal comma there. The source slashes in5/12 and7/12 are preserved. Stacked versus slashed typesetting of the same rational number is not separately counted as a substantive value change. The two canceled hypotheses and M1043 remain uncertain, and the newly added whole-fraction doubt is certainty-only. H’s editorial note on overwork is not added to the manuscript text.',
 f'Coverage totals: {len(changes)} substantive comparison rows, {sum(x["against_C"] for x in changes)} against C and {sum(x["against_H"] for x in changes)} against H; the unresolved M1043 comparison is not a proven H error. There is exactly one indexed decision, M1043, left undecided. Four doubtful places are recorded, including both unindexed C deletion doubts and the added rewritten-fraction doubt.'
]
when='2026-11-20 21:38:15 UTC'; who='reader_a; GPT-6 Astra Pro, inherited effort not separately exposed'
checks=[]
for n,outcome in [
 (1,'The weighted-stratum decomposition and U-class identity are carried from the manuscript as background. No independent geometric proof was performed; visual page reading is not labeled as a mathematical recheck.'),
 (2,'The zeta_p definition and displayed i_p! map are recorded as the manuscript’s notation/background. No proof or external reconstruction of the K_! formalism was attempted.'),
 (3,'Both S-prime class identities are carried as background without independent verification of their geometric hypotheses.'),
 (5,'The geometric boundary contribution[widehat M]=[M]+1/2 is carried as background. Only its rational coefficient addition was checked, separately under note4.')]:
 checks.append(dict(statement_id=f'147-065-N{n}',date=when,who=who,type='carried as background without fault found',outcome=outcome))
checks.insert(3,dict(statement_id='147-065-N4',date=when,who=who,type='computation or formal certificate',outcome='Python fractions.Fraction:1/4+1/6=5/12. Plus branch gives(T(1),constant,zeta2,zeta3) coefficients(1/2,−7/12,1/8,1/6); minus branch gives(1/2,−7/12,1/8,−5/6). Also−1/2−1/12=−7/12 and−7/12+1/2=−1/12. This is conditional exact algebra, not an ink resolution or geometric proof.'))

notation=[
 dict(sign='E with two upright/outline strokes and three rightward arms',reading=r'\mathbb E^1',evidence='Crop02 separates the outer class bracket from both upright strokes of E and the raised1.',scope='065 first U-class formula'),
 dict(sign='Z with doubled diagonal tracks',reading=r'\mathbb Z',evidence='Crops05 and06 show paired diagonals at all four occurrences.',scope='065 two Zs in the zeta definition and two in the displayed map'),
 dict(sign='literal equality sign following De',reading='=',evidence='Crop07 contains two parallel horizontal bars, with no letters after De.',scope='065, abbreviation for même; preserved literally'),
 dict(sign='long zeta with a short upper turn and descending lower return',reading=r'\zeta_p;\zeta_2;\zeta_3',evidence='The clear definition and repeated indexed terms establish the same curved letter. The isolated canceled mark after7/12 remains unresolved despite this comparison.',scope='065 live indexed zeta terms only'),
 dict(sign='arched brace with the label5/12 above it',reading=r'\overbrace{\left(\frac14\deleted{\unsure{+}}+\frac16\right)}^{5/12}',evidence='Crop08 places both the brace and its label above the coefficient parenthesis.',scope='065 first weighted expansion')]
hand_log=[
 dict(habit='Doubled mathematical-letter strokes must be distinguished from neighboring brackets',pages=[65],all_occurrences='The E in[ E^1 ] has its own doubled upright inside the outer bracket; all four Zs have separate diagonal tracks.',witness_misreadings='C uses bold E and Z; H uses the double-stroked forms supported by the crops.'),
 dict(habit='Rapid prose suppresses many bowls but retains the tall f/p stems and g descender',pages=[65],all_occurrences='façon, générale, pose, pour and premier were read in their original order in crops03–04; on is compressed between générale and pose.',witness_misreadings='H rewrites où de façon générale on pose as où on a posé en général and omits un nb.'),
 dict(habit='A numerator1 can have a broad short upper-left serif;7 has a longer descending stroke and crossbar here',pages=[65],all_occurrences='The opening1/6 numerator is short and upright with a cap; the7 of7/12 in crop09 has a long downward stroke crossed midway. Other live1 numerators are mostly simple uprights.',witness_misreadings='Neither witness changes these two readings; the comparison was used to avoid treating the serifed1 as a new7.'),
 dict(habit='A very small loop on a horizontal arithmetic stroke is insufficient to assert a plus upright',pages=[65],all_occurrences='M1043 is the one unresolved small-loop sign; neighboring unambiguous plus signs have distinct vertical strokes.',witness_misreadings='H prints plus without a doubt. C’s minus/plus doubt is retained; the arithmetic is not substituted for the ink.'),
 dict(habit='Overwriting can leave a triangular numerator contour and multiple denominator loops',pages=[65],all_occurrences='The1/8 coefficient after7/12 has overwork at both numerator and denominator; the later1/8 coefficients are separately read in their clear forms.',witness_misreadings='Both witnesses print1/8; H flags rewriting in an editorial note. The proposed page adds a whole-fraction doubt, without inventing an earlier digit sequence.')]
abbreviations=[dict(written='nb',expansion='nombre'),dict(written='=',expansion='même, in De ='),dict(written='Spec',expansion='spectre, as the written mathematical operator')]

displays=re.findall(r'\\\[\n(.*?)\n\\\]',text,re.S)
assert len(displays)==7
# Each box receives a complete mathematical reading, not a description of its contents.
second=[]
def sb(kind,box,reading):
 second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
def disp(body):return '\\[\n'+body+'\n\\]'
sb('handwritten number',boxes['01'],disp(displays[0]))
sb('handwritten number',boxes['02'],disp(displays[1]))
sb('word disagreement',boxes['03'],'où de façon générale on pose,')
sb('word disagreement',boxes['04'],'pour un nb premier')
sb('word disagreement',boxes['11'],'$p$')
sb('handwritten number',boxes['05'],disp(displays[2]))
sb('handwritten number',boxes['06'],'où\n'+disp(displays[3]))
sb('word disagreement',boxes['07'],'De $=$')
srows=displays[4].splitlines()[1:-1]
sb('handwritten number',[415,1015,1380,1145],disp('\\begin{aligned}\n'+srows[0]+'\n\\end{aligned}'))
sb('handwritten number',[420,1145,1385,1265],disp('\\begin{aligned}\n'+srows[1]+'\n\\end{aligned}'))
mrows=displays[5].splitlines()[1:-1]
sb('doubtful formula',boxes['08'],"d'où\n"+disp('\\begin{aligned}\n'+'\n'.join(mrows[:2])+'\n\\end{aligned}'))
sb('doubtful formula',boxes['09'],disp('\\begin{aligned}\n'+mrows[2]+'\n\\end{aligned}'))
sb('handwritten number',[385,1810,1530,1920],disp('\\begin{aligned}\n'+mrows[3]+'\n\\end{aligned}')+'\ndonc')
sb('handwritten number',[235,1980,1555,2250],disp(displays[6]))
sb('margin note',boxes['10'],r'\margin{64}')
report=dict(scan=65,reader='reader_a',physical_lines_read=19,changes=changes,decisions=[dict(id='M1043',cote=147,scan=65,decision='undecided',reading=r'\unsure{-|+}',ink='Short horizontal stroke with a small loop at its right end; no independent vertical plus upright is securely visible. Minus is preferred by the ink, but plus is not ruled out. The later algebra fits plus and is recorded only as a conditional calculation.',crop='147_scan065_place08.png (235,1280,1570,1670)',confidence='medium')],inventory=inventory,doubts=doubts,notes=notes,check_events=checks,notation=notation,hand_log=hand_log,abbreviations=abbreviations,second_boxes=second,unresolved=['M1043 remains minus/plus, with minus preferred and no ink resolution from arithmetic.','The canceled mark after1/4 remains tentatively plus; its original strokes are obscured.','The canceled mark after7/12 remains tentatively zeta; its original letter is not plain.','Both numerator and denominator of the rewritten1/8 coefficient remain under a whole-fraction doubt; no earlier digits are invented.'],witness_comparison='C preserves the bare opening M, the prose order and nb, literal De=, the overbrace above its coefficient, tentative canceled marks, the sign doubt and foliation64. H correctly represents E and all four Zs with double strokes. H rewrites prose, adds opening class brackets and a terminal comma, moves p, expands the abbreviation and places the brace below; it supplies an unqualified plus where the sign remains unresolved. Both print1/8 at the heavily rewritten coefficient; H acknowledges overwork editorially, and the proposed page explicitly marks the whole fraction as doubtful. No canceled character is promoted to certainty, and the mathematical check is conditional.')
(R/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'against_C':sum(x['against_C'] for x in changes),'against_H':sum(x['against_H'] for x in changes),'inventory':len(inventory),'second_boxes':len(second),'decisions':len(report['decisions']),'crops':len(boxes),'check_events':len(checks)}))
