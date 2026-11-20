from pathlib import Path
import json
from datetime import datetime, timezone

out=Path(__file__).resolve().parent
source=str(Path('source/SP53_CW_156-6_scans/J156-6-02_156-6_scan015.jpg').resolve())
plan=json.loads((out/'crop_plan.json').read_text())
by_no={int(p['name'].split('_')[0]):p for p in plan}
differences=[]

def add(place,c,h,reading,ac,ah,kind,evidence,box=None,crop=None,confidence='high',marked='no',mathematical=False):
    if crop is not None:
        p=by_no[crop]
        cp='readers/scan015/R3/crops/'+p['name']+'.jpg'
        box=p['box']
    else: cp=None
    differences.append(dict(id=f'R3-015-D{len(differences)+1:02d}',place=place,c=c,h=h,reading=reading,against_C=ac,against_H=ah,kind=kind,marked_in_H=marked,confidence=confidence,evidence=evidence,crop=cp,crop_box=box,crop_source=source,mathematical=mathematical))

sym='misread symbol or index'
add('Opening, family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,sym,'Broad detached rising cap with a hooked right end, central cross-arm and returning foot. The identity as the family F is clear; the printed alphabet is not determined. The notation table’s mathcal/fraktur candidates are retained, with a first-occurrence doubt.',crop=1,confidence='medium',mathematical=True)
add('Opening, c’est de la donnée','c’est de la donnée','c’est la donnée','c’est de la donnée',False,True,'omission','The first line ends with a separate de after c’est; the next line starts la donnée. Both letters of de are visible in half_a.',box=[1420,78,1540,159])
add('(1.30), enclosing outline',r'\boxed{...}',r'\boxed{...}; note: la formule est encadrée','Three separate enclosing strokes, open at the right; small gaps at upper-left and lower-left',True,True,'drawing or diagram','Half_a shows a long upper rule, a separate left vertical beginning below it, and a lower rule beginning slightly right of that vertical. The top and bottom reach the right sheet edge; no right vertical is visible. H is credited for explicitly noticing an enclosure. No claim is made about ink beyond the image boundary.',box=[532,230,1667,419],confidence='high')
add('(1.30), brace and annotation placement',r'\underset{\overbrace{\text{rel. d’ordre dans }\mathcal{F}}}{\leq,\ll}','Inline parenthetical annotation in formula; note correctly says below the signs, attached by a brace','Annotation below the line, with an overbrace displaced right; its left end starts below the comma/right of the first sign',True,True,'drawing or diagram','Half_a settles the geometry: brace begins about x=681, its upward point is about x=884, and its right end is about x=1030. The first order sign is left of the brace’s left end. H’s explanatory note is credited, so the difference is only the more specific lateral extent/placement, not omission of the brace.',box=[666,295,1039,398],confidence='medium')
add('(1.30), parentheses supplied around annotation','No parentheses','(rel. d’ordre dans F)','rel. d’ordre dans F',False,True,'text not on the page','Half_a shows the annotation beginning directly with rel. and ending at the family letter, with no enclosing parentheses. H’s formula supplies a pair, although its separate descriptive note quotes the annotation without them.',box=[675,342,1017,397],confidence='high')
add('(1.30), family F in annotation',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,sym,'Small capital has a rising cap, upright and transverse arm, and lower return. Same recurring family sign; local occurrence inspected in half_a.',box=[958,341,1016,394],confidence='medium',mathematical=True)
add('En termes de celles-ci, on definit',r'\unsure{definit|définit}','définit','definit',True,True,'misread word','Crop includes generous space above the d–e group. No detached acute is visible there; the tall arch belongs to the following f. The i has its own dot.',crop=2)
add('Canceled symbol after definit',r'\deleted{\unsure{M|\mathcal{F}}}',r'\struck{\mathcal{M}}',r'\deleted{\unsure{\mathcal{M}|M}}',True,True,sym,'Two uprights and a rounded intervening trough survive under the diagonal/looped cancellation strokes, supporting M rather than family F. The glyph’s cursive-versus-ordinary alphabet remains uncertain, and this is the first M occurrence on the page.',crop=2,confidence='medium',mathematical=True)
add('First inclusion, M',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Two peaked uprights, a rounded trough, long rising entry and short descending exit. The letter identity is clear; the established first-occurrence mathcal/M ambiguity is carried after the preceding deleted M.',crop=3,confidence='medium',mathematical=True)
add('First inclusion, family F',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,sym,'Detached broad curved cap, central upright and crossing arm. This occurrence remains distinct from ordinary operand F; it is visible beside M in crop 03.',crop=3,confidence='medium',mathematical=True)
add('After (1.20), avec','avec',r'\uncertain{avec}','avec',False,True,'misread word','Half_a shows the short connected word avec between the comma and les; no letter is missing or overwritten.',box=[641,748,767,808],marked='yes')
add('After (1.20), M centered below ≤',r'\underset{M}{\leq}',r'\leq_{\mathcal{M}}',r'\underset{\mathcal{M}}{\leq}',True,True,sym,'The two-peak cursive M is directly centered below the relation, not displaced to its lower right. C differs in alphabet; H differs in index placement.',box=[1228,735,1300,821],confidence='medium',mathematical=True)
add('After (1.20), M centered below ≪',r'\underset{M}{\ll}',r'\ll_{\mathcal{M}}',r'\underset{\mathcal{M}}{\ll}',True,True,sym,'The two-peak M is directly below the double-chevron sign. This is a separate written occurrence, independently inspected in half_a.',box=[1315,737,1391,824],confidence='medium',mathematical=True)
add('After induites par, family F below ≤',r'\underset{\mathcal{F}}{\leq}',r'\leq_{\mathfrak{F}}',r'\underset{\mathcal{F}}{\leq}',False,True,sym,'The first index has a broad cap, short upper loop and returning lower stem. It is centered under ≤; H’s lower-right index and unqualified fraktur alphabet differ.',crop=4,confidence='medium',mathematical=True)
add('After induites par, family/barred-f index below ≪',r'\underset{\unsure{\mathcal{F}|\overline{f}}}{\ll}',r'\ll_{\mathfrak{F}}',r'\underset{\unsure{\mathcal{F}|\overline{f}}}{\ll}',False,True,sym,'A long detached horizontal cap sits above a short stem and transverse arm. The cap could belong to the family F or be a bar over a small f. It is centered below ≪. The crop does not eliminate this local ambiguity.',crop=4,confidence='low',mathematical=True)
add('Inclusion L ⊂ M, M',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Tall double-peaked M with curved left entry and central trough; inspected in half_a.',box=[916,934,1009,1022],confidence='medium',mathematical=True)
add('Reference before L’application',r'(1.2\unsure{6|5})','(1.25)','(1.25)',True,False,sym,'The final digit has a rightward top bar and an open lower descending turn, without a closed lower loop. Literal 5 is retained; the number has not been corrected to match another page or an expected definition.',crop=5,confidence='medium',mathematical=True)
add('(*) domain family F',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,sym,'Broad upward-returning cap and separate upright/cross-arm distinguish the family sign from the ordinary mapped operand. Inspected in half_a.',box=[557,1150,629,1232],confidence='medium',mathematical=True)
add('(*) power-set P',r'\unsure{\mathcal{P}|\mathrm{P}}',r'\mathfrak{P}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}',True,True,sym,'Large angular bowl; long descending stem; the bowl returns across the stem to a left hook. This ornamental form does not support silently choosing plain roman P. Exact calligraphic/script/fraktur typography remains uncertain.',crop=7,confidence='medium',mathematical=True)
add('(*) argument M in P(M)',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Cursive two-peak M between parentheses, with a rising left entry; inspected in the supplied halves.',box=[870,1145,945,1223],confidence='medium',mathematical=True)
add('(*) overwritten input X/F',r'\deleted{\unsure{X}}F','F; note explicitly records a biffé X',r'\mathord{\rlap{$\deleted{X}$}F}',True,False,sym,'Two complete oblique limbs form an X beneath the live F’s upright and two arms. X is readable without a doubt. The replacement occupies the same position; H’s explicit note is credited for the cancellation and is not counted as an omission.',crop=8,confidence='high',mathematical=True)
add('(*) deployment operator',r'\unsure{\mathrm{Dep}|\mathrm{Def}}',r'\mathrm{Dépl}',r'\mathrm{Dep}',True,True,sym,'Visible D and small e are followed by a long descending loop with a short rightward shoulder: p. No detached acute appears above e and no independent final l appears before the parenthesis.',crop=9,confidence='medium',mathematical=True)
add('Insertion after est',r'\inserted{alors}',r'\add{donc}',r'\inserted{alors}',False,True,'misread word','The raised word begins with a low loop and tall looped l, then the remaining compact strokes of ors. It is linked into the space after est by the long curved insertion stroke. This is alors, not donc.',crop=10,confidence='medium')
add('After (*), definie',r'\unsure{définie|definie}','définie','definie',True,True,'misread word','The broad raised curve is continuous with the insertion leader; no separate acute is visible over the e. The small detached mark farther right belongs to an i.',crop=10,confidence='medium')
add('(1.31), M in X ∈ M',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Double-peaked cursive M immediately after the membership sign; inspected in half_b.',box=[863,1351,928,1427],confidence='medium',mathematical=True)
add('(**) domain family F',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,sym,'Sweeping cap with a curved upturn and distinct lower stem; recurring family sign, inspected locally in half_b.',box=[573,1538,645,1628],confidence='medium',mathematical=True)
add('(**), M in Fig(M)',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Two peaked strokes and curved entry between the parentheses after Fig; inspected in half_b.',box=[862,1546,934,1620],confidence='medium',mathematical=True)
add('(**), input F and extra diagonal',r'\deleted{\unsure{X}}F','F',r'\unsure{F|\deleted{X}F}',True,True,'deletion state','One long diagonal rises from far lower left across the F to its upper stem/arm. A separate second X limb cannot be isolated as in (*). The live F is certain, but the diagonal may be a remnant of an overwritten X or part of a retraced letter. The transcription marks the state alternatives, rather than asserting a canceled X.',crop=12,confidence='low',mathematical=True)
add('(**), M subscript in mapped Fig_M(F)',r'\mathrm{Fig}_{M}(F)',r'\mathrm{Fig}_{\mathcal{M}}(F)',r'\mathrm{Fig}_{\mathcal{M}}(F)',True,False,sym,'Small two-peak cursive M is at lower right of Fig, unlike the centered indices of the order signs; inspected in half_b.',box=[1297,1564,1355,1618],confidence='medium',mathematical=True)
add('After par (1.4), colon',':','no colon',':',False,True,'omission','Two small separate points immediately follow the closing parenthesis, one above-left of the other. Both are visible in half_b.',box=[516,1657,564,1702])
add('Canceled (1.32), placement',r'\tag*{\deleted{(1.32)}}','par (1.4) followed immediately in prose by struck (1.32)',r'\tag*{\deleted{(1.32)}}',False,True,'insertion or placement','The canceled number is level with the following Fig formula, below the par (1.4) line. Both witnesses correctly recognize its deletion; the difference concerns which line it labels.',box=[269,1735,443,1806],confidence='high')
add('Fig formula, subscript M on left side',r'\mathrm{Fig}_{M}(F)',r'\mathrm{Fig}_{\mathcal{M}}(F)',r'\mathrm{Fig}_{\mathcal{M}}(F)',True,False,sym,'Two small cursive peaks form the subscript immediately after the descending g; independently inspected in half_b.',box=[681,1744,738,1805],confidence='medium',mathematical=True)
add('Fig formula, power-set P on right side',r'\mathcal{P}',r'\mathfrak{P}',r'\mathcal{P}',False,True,sym,'Angular bowl returns left across the upright, matching the ornamental P of (*); this second occurrence was read separately in half_b.',box=[1312,1675,1402,1767],confidence='medium',mathematical=True)
add('Fig formula, M in right-side P(M)',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Two peaks and short curved terminal inside the parentheses; inspected locally in half_b.',box=[1426,1680,1501,1756],confidence='medium',mathematical=True)
add('Definition of tilde X, M in Y ∈ M',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Cursive double-peaked M after membership, with a broad rising entry; inspected in half_b.',box=[973,1817,1042,1895],confidence='medium',mathematical=True)
add('Concluding paragraph, family F after Ainsi',r'\mathcal{F}',r'\mathfrak{F}',r'\mathcal{F}',False,True,sym,'Long slanted cap, upright, crossing arm and lower return. This final family occurrence is distinct from ordinary F in the equivalence below.',box=[529,1980,611,2076],confidence='medium',mathematical=True)
add('Concluding paragraph, M in parties dans M',r'M',r'\mathcal{M}',r'\mathcal{M}',True,False,sym,'Tall two-peak M with curved left entry and bottom trough; inspected in half_b.',box=[964,2072,1048,2145],confidence='medium',mathematical=True)
add('Concluding paragraph, s’interprète',r'\unsure{s’interprète|s’interprête}','s’interprète',r'\unsure{s’interprète|s’interprête}',False,True,'misread word','The final accent lies close to the tall t and a descending stroke from the line above. The crop leaves a small dark/gray stroke whose grave versus folded/circumflex form cannot be established securely. The uncertainty is retained, with the grave candidate first.',crop=13,confidence='low')

c_doubts=[]
def doubt(place,c,reading,disposition,evidence,crop):
    p=by_no[crop]
    c_doubts.append(dict(place=place,c=c,reading=reading,disposition=disposition,evidence=evidence,crop='readers/scan015/R3/crops/'+p['name']+'.jpg',crop_box=p['box'],crop_source=source))
doubt('Opening family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Identity F is clear; exact printed alphabet is not. The table’s existing mathcal/fraktur candidates replace C’s script alternative.',1)
doubt('definit before canceled symbol',r'\unsure{definit|définit}','definit','resolved','No independent acute above e; the tall neighboring stroke is the f arch.',2)
doubt('Canceled symbol after definit',r'\unsure{M|\mathcal{F}}',r'\deleted{\unsure{\mathcal{M}|M}}','resolved','The C letter-identity question is resolved to M by the two uprights and rounded trough. A distinct typographic alphabet doubt remains at this first M occurrence.',2)
doubt('Family index below second ≪',r'\unsure{\mathcal{F}|\overline{f}}',r'\unsure{\mathcal{F}|\overline{f}}','retained','Detached cap and short lower body permit both family F and barred f.',4)
doubt('Reference before L’application',r'(1.2\unsure{6|5})','(1.25)','resolved','Upper bar and open lower turn support 5; no lower loop supports 6. No cross-page correction was made.',5)
doubt('Power-set P in (*)',r'\unsure{\mathcal{P}|\mathrm{P}}',r'\unsure{\mathcal{P}|\mathscr{P}|\mathfrak{P}}','retained','Left-returning bowl is ornamental; exact printed alphabet remains uncertain, using existing table candidates.',7)
doubt('Canceled input before first map',r'\deleted{\unsure{X}}',r'\deleted{X}','resolved','Two oblique limbs crossing below F make X readable.',8)
doubt('Deployment operator in (*)',r'\unsure{\mathrm{Dep}|\mathrm{Def}}',r'\mathrm{Dep}','resolved','Last letter has a descending loop and right shoulder of p; no high f arch, independent l, or acute over e.',9)
doubt('definie after (*)',r'\unsure{définie|definie}','definie','resolved','Raised curve is the insertion leader. No separate acute over e.',10)
doubt('Canceled input before second map',r'\deleted{\unsure{X}}F',r'\unsure{F|\deleted{X}F}','retained','Only one additional diagonal is separable; the unresolved issue includes cancellation state, so both full states are given explicitly.',12)
doubt('s’interprète in last paragraph',r'\unsure{s’interprète|s’interprête}',r'\unsure{s’interprète|s’interprête}','retained','The accent remains crowded by the t and neighboring-line ink; the permitted crop does not determine its exact contour.',13)

inventory=[]
def inv(element,kind,position,words):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('Manuscript page number','text','top center, y=30–62','14')
inv('Opening paragraph and its two separate single underlines','text','upper page, y=72–235','En résumé, en termes de F; relations; d’ordre')
inv('Order-data display, including label and implication','display','upper framed area, y=277–345','(1.30); ≤, ≪; telles que F≤G ⇒ F≪G')
inv('Three-sided visible enclosure with two left gaps','drawing','around (1.30), x=548–1664, y=241–408','top, left and bottom strokes; no visible right vertical')
inv('Annotation beneath the two relations','text','inside lower portion of frame, y=350–391','rel. d’ordre dans F')
inv('Brace above annotation, shifted right','drawing','inside frame, x=680–1031, y=302–376','curved overbrace with upward point')
inv('End of opening sentence','text','y=461–538','que je vais partir.')
inv('Second paragraph opening','text','y=526–615','En termes de celles-ci, on definit')
inv('Canceled M after definit','deletion','right end of line, x=1535–1628, y=537–596','deleted M; alphabet doubt retained')
inv('First inclusion','display','y=644–704','M ⊂ F')
inv('First line of restricted-order prose','text','y=736–820','par (1.20), avec les relations; M below ≤ and ≪; induites')
inv('Second line of restricted-order prose','text','y=855–945','par; family F below ≤ and ambiguous family F/barred f below ≪; puis')
inv('Second inclusion','display','y=946–1016','L ⊂ M')
inv('Reference and map introduction','text','y=1045–1125','par (1.25). L’application')
inv('First map and its star label','display','y=1144–1242','(*); F ↪ P(M); F ↦ tilde F = Dep(F)')
inv('Overwritten input X in first map','deletion','x=1103–1148, y=1156–1210','X overwritten by live F')
inv('Definition introduction','text','y=1275–1334','est definie par')
inv('Raised insertion with curved leader','insertion','x=340–447, y=1239–1302','alors, inserted after est')
inv('Principal lower-set definition','display','y=1352–1445','(1.31); tilde F = {X∈M | X≤F}')
inv('Connecting word before second map','text','left, y=1494–1540','et')
inv('Second map and double-star label','display','y=1541–1642','(**); F ↪ Fig(M); F ↦ Fig_M(F)')
inv('Possible overwritten input in second map','deletion','x=1060–1118, y=1547–1600','extra diagonal at F; F versus deleted X plus F state doubt')
inv('Reference introducing figure formula','text','y=1667–1730','par (1.4) :')
inv('Canceled earlier formula number','deletion','left of figure formula, y=1750–1796','(1.32), canceled with a long stroke')
inv('Figure assigned to F','display','y=1685–1801','Fig_M(F) = {tilde X | X∈tilde F} ⊂ P(M)')
inv('Introduction of subordinate lower-set definition','text','left, y=1857–1889','avec')
inv('Lower-set definition for X and terminal point','display','y=1818–1906','tilde X = {Y∈M | Y≤X} .')
inv('Concluding interpretation paragraph','text','y=1991–2236','Ainsi, F est interprété comme un ens. de parties dans M via (*), et ≤ s’interprète simplement par l’inclusion')
inv('Final order/inclusion equivalence','display','bottom, y=2241–2322','(1.32); F≤G ⇔ tilde F ⊂ tilde G')

unresolved=[
 dict(place='Opening family F; recurring throughout page',reading=r'\mathcal{F}',alternatives=[r'\mathfrak{F}'],confidence='medium',evidence='Hooked cap, cross-arm and foot establish the family F, but not a unique printed alphabet. Doubt appears only at first family occurrence.'),
 dict(place='First M, canceled after definit; recurring M thereafter',reading=r'\mathcal{M}',alternatives=['M'],confidence='medium',evidence='Cursive two-peak handwriting and curved trough do not uniquely distinguish mathcal M from ordinary handwritten M. The symbol’s identity M is resolved.'),
 dict(place='Index below the second induced ≪',reading=r'\mathcal{F}',alternatives=[r'\overline{f}'],confidence='low',evidence='Detached horizontal cap above a small crossed stem leaves the family-letter versus barred-f reading open.'),
 dict(place='First power-set P in (*)',reading=r'\mathcal{P}',alternatives=[r'\mathscr{P}',r'\mathfrak{P}'],confidence='medium',evidence='Ornamental angular bowl and left return exclude treating the letter as an unqualified plain roman form, but do not settle printed alphabet.'),
 dict(place='Input F in (**)',reading='F',alternatives=[r'\deleted{X}F'],confidence='low',evidence='Extra long diagonal is visible; no independent second X limb is recoverable. Cancellation state is explicitly retained in reading.tex.'),
 dict(place='Final paragraph, s’interprète',reading='s’interprète',alternatives=['s’interprête'],confidence='low',evidence='Small accent crowded by the tall t and neighboring-line ink remains unresolved after its single crop.')
]

notes={
 'content':[
  'The page restates a starting datum of two order relations ≤ and ≪ on the family F, with F≤G implying F≪G.',
  'It introduces M as a subset of the family, with the two induced orders, then L as a subset of M. The literal references are (1.20) and (1.25).',
  'The first map sends F to its set of elements X in M satisfying X≤F; its operator is written Dep. The second sends F to the figure consisting of lower sets tilde X for X in tilde F.',
  'The closing paragraph interprets the family as an ens. de parties dans M and asserts that ≤ becomes inclusion, ending with F≤G iff tilde F⊂tilde G.'
 ],
 'math_reading_decisions':[
  'Eight family-F occurrences and thirteen M occurrences, including the canceled M, were inspected locally. Every occurrence whose alphabet or placement differs from a witness has its own differences row.',
  'Order subscripts are directly underneath the four order signs. Fig subscripts remain at lower right. Ordinary operands F and G remain distinct from the family letter.',
  'All displayed wave marks are tildes; set separators are single vertical strokes; inclusion signs have no equality bar. The two domain arrows have left hooks; both element arrows have initial vertical bars.',
  'The literal reference (1.25) is not silently corrected to another number. H’s remark about another page was not verified against any other image.',
  'No independent mathematical verification or proof was attempted. The formulas were read and their stated roles followed only to avoid transcription normalization.',
  'The first input has a readable crossed X beneath F. The second input has only one separately visible diagonal; its live-versus-replacement state is explicitly uncertain.',
  'The enclosing frame has no visible right vertical; its shape and the lateral displacement of the brace are reproduced with standard TikZ. The label (1.30) is a TikZ text node because the formula is part of this drawn frame.'
 ],
 'author_doubts':[],
 'titles_dates_counts':[
  'Manuscript page number: 14. Our scan: 15. No independent title, date, archive pencil number, marginal note, or authorial question/check phrase appears.',
  'Live numbered labels: (1.30), (1.31), final (1.32). An earlier (1.32) beside the Fig formula is canceled. Additional labels: (*) and (**); both were inspected for surcharge, with no recoverable separate earlier token established.',
  'There are two separate single underlines, under relations and d’ordre; one raised prose insertion, alors; one canceled M; one certain overwritten X; one possible overwritten X; and the canceled (1.32).',
  'Actual image views: 1 whole, 1 half_a, 1 half_b, and 13 unique enhanced crops. No image was re-emitted or re-cropped.'
 ]
}

check_events=[]
for sid in ['scan015-1.30-orders','scan015-M-and-L-definitions','scan015-star-map','scan015-1.31-lower-set','scan015-double-star-and-Fig-formula','scan015-final-1.32-equivalence']:
    check_events.append(dict(statement_id=sid,type='carried as background without fault found',outcome="read as the author's assertion; no mathematical verification performed"))

notation_proposals=[
 dict(sign='family F',latex=r'\mathcal{F}',ink='Detached hooked cap, central upright with transverse arm, returning foot; eight local occurrences.',alternatives=[r'\mathfrak{F}']),
 dict(sign='collection M',latex=r'\mathcal{M}',ink='Two peaked uprights, rounded trough and curved left entry; thirteen occurrences including one canceled.',alternatives=['M']),
 dict(sign='power-set P',latex=r'\mathcal{P}',ink='Large angular bowl returns left across a long descending stem; two occurrences.',alternatives=[r'\mathscr{P}',r'\mathfrak{P}']),
 dict(sign='small index beneath induced ≪',latex=r'\unsure{\mathcal{F}|\overline{f}}',ink='Detached upper horizontal stroke over a small crossed body.',alternatives=[r'\mathcal{F}',r'\overline{f}']),
 dict(sign='deployment operator',latex=r'\mathrm{Dep}',ink='D, e and a descending p-loop; no acute and no final l.',alternatives=[]),
 dict(sign='positions of order labels',latex=r'\underset{\mathcal{M}}{\leq},\ \underset{\mathcal{M}}{\ll},\ \underset{\mathcal{F}}{\leq},\ \underset{\unsure{\mathcal{F}|\overline{f}}}{\ll}',ink='Each letter is centered below its own order sign.',alternatives=[]),
 dict(sign='second-map intervention',latex=r'\unsure{F|\deleted{X}F}',ink='Live F plus one long additional diagonal; no independently recoverable full X.',alternatives=['unqualified live F','F replacing a canceled X'])
]

report=dict(scan=15,reader='R3',started_utc='2026-11-20 12:48:35 UTC',finished_utc=None,status='draft',view_log=json.loads((out/'view_log.json').read_text()),differences=differences,c_doubts=c_doubts,s_rows=[],inventory=inventory,notes=notes,check_events=check_events,notation_proposals=notation_proposals,abbreviations=[dict(form='rel.',expansion='relation(s), not expanded in the reading'),dict(form='ens.',expansion='ensemble, not expanded in the reading'),dict(form='Fig',expansion='figure(s), mathematical operator; not expanded'),dict(form='Dep',expansion='déploiement, probable operator expansion; literal unaccented Dep retained')],unresolved=unresolved,brief_feedback=[],counts=dict(differences=len(differences),c_doubt_loci=len(c_doubts),s_rows=0,inventory=len(inventory),actual_crops=13,unresolved=len(unresolved),family_F_occurrences=8,M_occurrences_including_deleted=13,power_P_occurrences=2))
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False))
