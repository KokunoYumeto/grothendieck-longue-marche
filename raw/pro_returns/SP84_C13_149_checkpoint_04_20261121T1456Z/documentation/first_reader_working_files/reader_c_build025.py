from pathlib import Path
import json
r=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads((r/'work/reader_c_scan025_boxes.json').read_text())
tex=r'''\scanpage{25}
\mspage{12}
d'examiner les actions de $\pi_1(f),\pi_1(g)$ sur les groupes abélianisés des $\pi_1$, et même sur leurs composantes $\ell$-adiques. Prenant alors jacobienne généralisée du type ``ext. d'une V.A. par un tore'' de $X$, on sait que

1°) Les morphismes $f:X\longrightarrow G$ tels que $f(a)=0$ se factorisent de façon unique par
\diagram{\begin{tikzcd}[ampersand replacement=\&]X \arrow[r,"{\mathrm{can}}"] \& J \arrow[r,"\varphi"] \& G\end{tikzcd}},
avec $\varphi$ un hom de groupes algébriques

2°) \deleted{$\varphi$ est} Un tel hom $\varphi$ est connu quand on connaît son action sur les $H_1(\ ,\mathbb Z_\ell)$ Ce qui revient à le connaître sur les points d'ordre $\ell^\nu$, quel que soit $\nu$ -- or ceux-ci sont denses\ldots

3°) $H_{\unsure{1|n}}(X,\mathbb Z_\ell)\simeq H_1(J,\mathbb Z_\ell)$

De ceci, \deleted{le \unsure{cas}} on conclut \inserted{(par 3°)} que $H_1(f)=H_1(g)$ implique (si $f=\varphi\circ\mathrm{can}$, $g=\psi\circ\mathrm{can}$) $H_{\unsure{1|n}}(\varphi)=H_1(\psi)$, donc par 2°) que $\varphi=\unsure{\varphi|\psi}$, donc $f=g$, cqfd

\deleted{b)} Notons que l'on ne peut conclure de l'hyp. \inserted{de a)} que $f=g$, puisque pour $X=Y=G$, les translations $\tau_a$ induisent l'identité sur $\pi_1(G)$ (du moins \unsure{en|\deleted{en}} la car. $0$ ou si $G$ est une VA), sans être l'identité.

b) On va pourtant prouver l'égalité,
\margin{24}
'''
(r/'edition/reviews/149_scan025.tex').write_text(tex,encoding='utf-8')
changes=[]
def ch(num,place,C,H,final,evidence,crop,confidence='high',against_C=False,against_H=True,kind='other',error_category='Other',marked_in_H=False,mathematical=False):
    changes.append(dict(id=f'c{num:02d}',place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/149_scan025_{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical))
ch(1,'Main line 3, after Prenant','Prenant une',r'\uncertain{Prenant alors} la','Prenant alors','The following word is one compact unit: an opening low a, a tall looped l, then a rounded o and compressed r/s exit. It is longer and has a tall l absent from une. There is no separate la after this word or before jacobienne on the next line. The literal missing article is retained.','c01',against_C=True,kind='misread word',error_category='Words',marked_in_H=True)
ch(2,'Main lines 4–5, quotation marks',"``ext. d'une V.A. par un tore''",'« ext. d\'une V.A. par un tore »',"``ext. d'une V.A. par un tore''",'At the opening and closing positions the manuscript has two short raised strokes, not inward-facing angular guillemets. Both pairs are visible in the same two-line crop.','c02')
ch(3,'Main line 5, before X','de $X$',r'\struck{de} de $X$','de $X$','Only one d-loop with tall ascender and following e occurs before X. Its lower traces are dark and retraced, but they do not form a second independently readable de. The small crossing/retracing near X likewise supplies no second word. No extra cancelled de is inserted.','c02',kind='text not on the page',error_category='Text that is not on the page')
ch(4,'Main line 6, opening of item 1','Les','les','Les','The initial letter has a tall upright descending to a long rightward base, followed by the low es group: a capital L, not the small looped l of nearby words.','c03',kind='misread word',error_category='Words')
ch(5,'Main line 6, morphismes','morphismes',r'\struck{morphismes}','morphismes','The initial morph- strokes are heavily retraced, but no cancellation stroke traverses the whole word. The h and following low suffix remain connected as live writing. A broad strike through the entire word, as encoded by H, is not supported. No underlying word is reconstructed from the retracing.','c03',kind='deletion state',error_category='Struck text')
ch(6,'Main line 8, diagram terminal punctuation','G (no following comma)','G,','G,','A detached curved comma stands below and to the right of G. Both arrow shafts have rightward heads, with can above the first and the phi glyph crossing the middle of the second; these objects and arrows are retained.','c04',against_C=True,against_H=False,kind='omission',error_category='Omissions')
ch(7,'Main line 8, first hom','hom.','hom.','hom','The h is followed by the low om strokes and their thickened terminal return. The space before de contains no separate point. The stop supplied by both witnesses is removed.','c19',against_C=True,against_H=True)
ch(8,'Main line 9, after algébriques','algébriques.','algébriques','algébriques','The terminal s ends in a dark downturned return, followed by blank paper. No detached terminal stop is visible. The word is complete; its q-descender continues downward separately from punctuation.','c05',against_C=True,against_H=False)
ch(9,'Main line 10, short form before live phi','hom.',r'homomorphisme','hom','A tall h followed by the low compact om group precedes a separate phi. There is no further morphisme letter sequence and no detached stop after m. The short form is preserved without expansion. The following est has a small opening e and compressed terminal st.','c06',against_C=True,kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised')
ch(10,'Main line 10, live phi after hom',r'$\varphi$','omitted',r'$\varphi$','Between the abbreviated hom and est is a separate upright-descending stem with a small upper loop/cup. It matches the local phi glyphs and is not part of a spelled-out homomorphisme.','c06',kind='omission',error_category='Omissions',mathematical=True)
ch(11,'Main lines 11–12, H formula to Ce',r'$H_1(\ ,\mathbb Z_\ell)$. Ce',r'$H_1(\ ,\mathbb Z_\ell)$ (ce',r'$H_1(\ ,\mathbb Z_\ell)$ Ce','The formula closes with its curved parenthesis; the adjacent long descender belongs to the quand group above. No detached stop follows the formula. The next line starts with a large open C joined to e, with no preceding opening parenthesis.','c07',against_C=True,against_H=True)
ch(12,'Main line 14, after denses',r'denses\ldots','denses …)',r'denses\ldots','Three separate dark points follow the final s. There is blank paper after the third point and no closing parenthesis.','c08')
ch(13,'Main line 16, cancelled phrase after De ceci',r'\deleted{\unsure{le cas}}',r'\struck{\ill{}}',r'\deleted{le \unsure{cas}}','A tall looped l and lower e remain visible beneath the long horizontal cancellation; the next word begins with an open c. The medial and final strokes are largely merged with the strike, so cas remains tentative. A dark fleck beyond the end may be a strike endpoint and is not independently read as punctuation. This is a provisional readable phrase against H, not a full resolution of the struck letters.','c10',confidence='medium',kind='readable ink left as \\ill{}',error_category='Readable ink left as illegible',marked_in_H=True)
ch(14,'Insertion above main line 16',r'\inserted{(par 3°)}','(par 3°),',r'\inserted{(par 3°)}','The complete parenthesized par 3° is raised above the line. A long curved leader runs from the gap before que toward the raised words; its dark curled endpoint is connected to that leader and is not an additional comma.','c11',kind='insertion or placement',error_category='Insertions put in the wrong place')
ch(15,'Main line 17, opening of parenthesized formulas','si','vu','si','The first low letter has an s-like turn. The following short i has a distinct detached dot above it. There is no two-stroke v/u pair. Both complete formulas, composition circles and closing parenthesis are visible in the crop.','c12',kind='misread word',error_category='Words',mathematical=True)
ch(16,'Main line 18, M1049, whole equality',r'$\varphi=\unsure{\varphi|\psi}$',r'$\varphi=\psi$',r'$\varphi=\unsure{\varphi|\psi}$','The left glyph has the local phi loop and descender. The right glyph has a tall central stem and a curved right cup/near-loop whose top return is crowded. It resembles phi but can also be the local psi form; comparison with the clearer psi in the preceding g-formula does not give a decisive closed-loop distinction. Equality and final comma are clear. The first reading remains provisional and is counted against H without claiming resolution.','c13',confidence='medium',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
ch(17,'Insertion above main line 20',r'\inserted{de a)}',r'\add{dans a)}',r'\inserted{de a)}','The first word consists of a rounded d with tall loop and a short e exit. There is no a-n-s sequence. The separate small a and right parenthesis follow. The long curved leader attaches this insertion between hyp. and que; it is not an additional parenthesis or strike.','c14',kind='misread word',error_category='Words')
ch(18,'Main line 22, M1050 after du moins',r'\unsure{en la} car. $0$',r'\struck{\ill{}} \uncertain{en car.} $0$',r'\unsure{en|\deleted{en}} la car. $0$','Only one compact en-like unit lies between moins and the clearly looped l plus low a of la. Its initial strokes are crossed/retraced, and the n-like right return is visible; whether the crossing cancels this unit is unresolved. There is no room or separate letter group for a cancelled fragment followed by another en. The following car., detached stop and 0 are clear. The surviving la is preserved.','c15',confidence='medium',kind='misread word',error_category='Words',marked_in_H=True)
ch(19,'Lower-left margin, separate thin foliation',r'\margin{24}','omitted',r'\margin{24}','A thin small 2 has a rounded upper turn and long lower foot; the following 4 has an upright and cross-stroke. It reads 24 in a separate, lighter foliation hand, distinct from the dark top 12.','c16',kind='omission',error_category='Omissions')
ch(20,'Main line 18, after cqfd','cqfd.','cqfd.','cqfd','The last d has a continuous rightward exit ending in a thickened dark spot. The spot is joined to that exit and no detached stop follows it; the terminal period supplied by both witnesses is removed.','c18',against_C=True,against_H=True)
# Contract uses a literal single TeX backslash in this enum.
changes[12]['kind']=r'readable ink left as \ill{}'
D=[
 dict(id='M1049',decision='undecided',reading=r'\unsure{\varphi|\psi}',evidence=changes[15]['evidence'],crop='crops/149_scan025_c13.png',box=boxes['c13'],confidence='medium'),
 dict(id='M1050',decision='undecided',reading=r'\unsure{en|\deleted{en}} la',evidence=changes[17]['evidence'],crop='crops/149_scan025_c15.png',box=boxes['c15'],confidence='medium')]
inv=[]
def item(kind,position,first,hand='author, main manuscript hand'):
    inv.append(dict(scan=25,sheet_kind='text',hand=hand,element=f'e{len(inv)+1:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
item('text','top centre, above first main line','12')
item('text','main lines 1–5, upper block',"d'examiner les actions")
item('text','main lines 6–7, item 1 opening','1°) Les morphismes')
item('diagram','main line 8, left half',r'$X\xrightarrow{\mathrm{can}}J\xrightarrow{\varphi}G$,')
item('text','main lines 8–9, continuation after diagram','avec phi un hom de groupes algébriques')
item('text','main lines 10–14, item 2','2°) Un tel hom')
item('deletion','main line 10, immediately after item number',r'\deleted{$\varphi$ est}')
item('display','main line 15, item 3',r'3°) $H_{\unsure{1|n}}(X,\mathbb Z_\ell)\simeq H_1(J,\mathbb Z_\ell)$')
item('text','main lines 16–18, deduction block','De ceci, ... on conclut')
item('deletion','main line 16, after De ceci',r'\deleted{le \unsure{cas}}')
item('insertion','above main line 16, leader to gap before que',r'\inserted{(par 3°)}')
item('text','main lines 19–23, limitation paragraph',"Notons que l'on ne peut conclure")
item('deletion','main line 19, to left of Notons',r'\deleted{b)}')
item('insertion','above main line 20, leader between hyp. and que',r'\inserted{de a)}')
item('deletion','main line 22, possible cancellation of one crowded word; state remains doubtful',r'\unsure{en|\deleted{en}}')
item('text','main line 24, bottom continuation','b) On va pourtant prouver')
item('text','lower-left margin','24','separate thin foliation hand')
notes=[
 'S025.1 — Scan 25 bears the dark author page number 12 at top centre and thin separate foliation 24 at the lower left. It is a continuation of handwritten mathematical notes. Reader: /root/reader_c; GPT-6 Astra Pro, effort not exposed, run SP84_C13_149. The 28 inspected manuscript lines comprise 24 main rows (including the diagram/formula rows), two raised insertion rows, and the two number-only positions.',
 'S025.2 — The page proposes examining the induced actions of f and g on abelianized fundamental groups and their ell-adic components. It states three facts involving a generalized Jacobian: factorization through can, determination of a group homomorphism from its action on H1 or ell-power torsion points, and an isomorphism between the H groups of X and J. This is a summary of the manuscript, not a proof check.',
 'S025.3 — The deduction invokes items 3 and 2 and ends with equality of f and g. The right glyph in the intermediate phi equality remains phi|psi from the ink. The two connected left H subscripts remain 1|n; no mathematical value has been used to force a reading. These uncertainties are localized and the complete affected formulas are retained.',
 'S025.4 — The following paragraph says that the hypothesis of a) alone does not imply f=g, using translations when X=Y=G, and mentions characteristic 0 or G a VA. It then begins b), promising to prove an equality. These claims were read and summarized only; no mathematical check event is asserted.',
 'S025.5 — The literal wording is Prenant alors jacobienne, with no separate article between alors and jacobienne. The missing article is not supplied. There is one de before X. Initial retracing in morphismes does not justify cancelling the whole word. Both occurrences of hom and the terminal cqfd lack detached stops; the abbreviation text is not expanded.',
 'S025.6 — The cancelled phi est is readable beneath a straight strike. In the cancelled phrase after De ceci, le and the initial c remain visible but the rest of cas is obscured. A terminal fleck beside the cancellation may belong to the strike endpoint; it is not securely independent punctuation. The leader of (par 3°) and the leader of de a) are kept distinct from punctuation and deletion strokes.',
 'S025.7 — After du moins there is only one en-like group, with an unresolved live/cancelled state, then clear la car. 0. H cannot be followed by inventing a second en. The source ellipsis consists of three points; no closing parenthesis follows it, and no opening parenthesis precedes the capital Ce.',
 'S025.8 — A first close inspection of the isolated diagonal mark in the left margin beside sont denses (c20, box [115,1295,205,1400]) shows an irregular speckled dark edge next to a bright parallel ridge, without a formed letter or numeral. It is excluded as a paper/surface or scan trace, not transcribed as manuscript text. Root independently inspected and agreed with this classification.',
 'S025.9 — The complete image and each prepared full-resolution half were inspected once, then twenty distinct first-pass crops were inspected. All agreed words, formulas, indices and source corrections were checked against the ink. No OCR, external research, mathematical verification, or TeX compilation was used.'
]
hand=[
 dict(habit='A subscript attached directly to the final H downstroke can form a low hump resembling n.',pages=[25],consistency='Observed in item 3 and in the left H of the later phi/psi homology equality. The separate 1 indices nearby have short vertical or angled heads. The two joined examples remain 1|n; no general resolution is claimed.',misread='Both C and H give unqualified 1 at the two joined examples.'),
 dict(habit='Terminal returns may thicken into a dark spot without an independent punctuation stop.',pages=[25],consistency='Verified at both hom short forms, algébriques, and cqfd. Actual detached stops remain visible at ext., V.A., hyp. and car.; this is a local distinction, not a rule to delete punctuation.',misread='Both witnesses supply the first hom stop and cqfd stop; C also supplies the second hom and algébriques stops.'),
 dict(habit='Long curved insertion leaders end in a darker hooked tip.',pages=[25],consistency='Both raised insertions, (par 3°) and de a), have this form and attach into the main-line gap. The separate straight cancellation through phi est is visibly different.',misread='H reads an extra comma after (par 3°) and changes de to dans.'),
 dict(habit='Phi may have an open left cup and a near-closed right loop around the central stem; psi has a cup with an upright central stroke.',pages=[25],consistency='The f/phi and g/psi formulas provide distinct local forms, but the right glyph in the final phi equality is crowded enough that the distinction remains unresolved.',misread='H fixes the final glyph as psi; C offers phi|psi. The proposal retains the doubt.'),
 dict(habit='Thick retracing of initial letters need not be a cancellation of the entire word.',pages=[25],consistency='The initial morph- part is heavy but the suffix is not traversed by a cancellation stroke. The en-like group has genuine crossing/overlap and its state remains uncertain.',misread='H cancels all of morphismes and splits the single en-like group into cancelled ink plus a separate en.')
]
notation=[
 dict(written='can',rendering=r'\mathrm{can}',meaning='label of the canonical map from X to J in the source',evidence='c04 has c-a-n over the first headed arrow, with no final stop; the same short label appears in the composition formulas of c12.'),
 dict(written='J',rendering='J',meaning='generalized Jacobian used in the factorization on this page',evidence='The middle diagram object has a horizontal upper stroke, right descending stroke and lower leftward return; the same object is the argument in the right H group in item 3.'),
 dict(written='π with subscript 1',rendering=r'\pi_1',meaning='fundamental-group notation in the source',evidence='Both first-line map actions, the second-line group and the lower pi1(G) have the short pi construction and a separate lowered 1.'),
 dict(written='H with lowered index',rendering=r'H_1; H_{\unsure{1|n}}',meaning='homology notation; two joined index forms remain graphically uncertain',evidence='The indices in H1(f)=H1(g) are clear in c17; the joined left indices in c09 and the lower formula of c17 admit 1/n.'),
 dict(written='double-traced Z with lower ell',rendering=r'\mathbb Z_\ell',meaning='coefficient notation written in the H formulas',evidence='c07 and c09 show a doubled oblique of Z and the small lower looped ell.'),
 dict(written='tilde over one horizontal stroke',rendering=r'\simeq',meaning='relation between the two groups in item 3',evidence='The full formula in c09 shows a short upper wave and one distinct lower horizontal stroke.')
]
abbr=[
 dict(form='ext.',expansion='extension',place='opening paragraph, quoted type'),
 dict(form='V.A.',expansion='variété abélienne',place='opening paragraph, quoted type'),
 dict(form='hom',expansion='homomorphisme',place='item 1 continuation and item 2; no stop at either occurrence'),
 dict(form='can',expansion='canonique',place='first diagram arrow and both composition formulas'),
 dict(form='cqfd',expansion="ce qu'il fallait démontrer",place='end of deduction; no detached final stop'),
 dict(form='hyp.',expansion='hypothèse',place='Notons paragraph'),
 dict(form='car.',expansion='caractéristique',place='parenthesis in Notons paragraph'),
 dict(form='VA',expansion='variété abélienne',place='end of parenthesis in Notons paragraph')
]
doubts=[
 dict(place='Main line 15, left H subscript in item 3',reading=r'H_{\unsure{1|n}}(X,\mathbb Z_\ell)\simeq H_1(J,\mathbb Z_\ell)',alternatives=['1','n'],confidence='medium',reason='The low index is connected to the H downstroke and has an up-and-down hump. It can be a hooked 1 with a connecting return or an n-like glyph. The whole formula is inspected and audited in c09; no mathematical completion settles it.'),
 dict(place='Main line 16, cancelled second word',reading=r'\deleted{le \unsure{cas}}',alternatives=['cas','unrecovered medial/final letters after c'],confidence='low',reason='The l and e and following initial c are visible; the horizontal cancellation masks much of the next two letters. cas is retained tentatively, not asserted as fully recovered.'),
 dict(place='Main line 17, left H subscript before phi',reading=r'H_{\unsure{1|n}}(\varphi)=H_1(\psi)',alternatives=['1','n'],confidence='medium',reason='The same connected low hump as in item 3 is present; neighboring detached 1 forms have a similar angled head but do not prove that the connected contour is only a 1. The entire formula is preserved and audited in c17.'),
 dict(place='Main line 18, M1049 right glyph',reading=r'\varphi=\unsure{\varphi|\psi}',alternatives=[r'\varphi',r'\psi'],confidence='medium',reason='A near-loop/cup and tall stem are visible, but the upper-right return does not securely distinguish a closed phi loop from a curved psi arm. The expected algebraic conclusion does not replace the source doubt.'),
 dict(place='Main line 22, M1050 one crowded word',reading=r'\unsure{en|\deleted{en}} la',alternatives=['live en',r'\deleted{en}'],confidence='medium',reason='There is one en-like group with crossed initial strokes and an n-like terminal return. Its cancellation state is not secure. The following la is clear and independent; no second en is present.')
]
audit=[]
def ab(kind,box,reading):
    audit.append(dict(box=f'b{len(audit)+1:02d}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
ab('number',[750,30,825,80],r'\mspage{12}')
ab('formula',[1055,55,1235,155],r'$\pi_1(f),\pi_1(g)$')
ab('formula',[930,155,1070,235],r'$\pi_1$,')
ab('text',boxes['c01'],'Prenant alors')
ab('text',boxes['c02'],r'''jacobienne généralisée du type ``ext. d'une V.A. par un tore'' de $X$, on sait que''')
ab('text',boxes['c03'],'1°) Les morphismes')
ab('number',[295,680,400,745],r'$=0$')
ab('diagram',boxes['c04'],r'\diagram{\begin{tikzcd}[ampersand replacement=\&]X \arrow[r,"{\mathrm{can}}"] \& J \arrow[r,"\varphi"] \& G\end{tikzcd}}, avec $\varphi$')
ab('text',boxes['c19'],'un hom de')
ab('text',[280,855,710,975],'algébriques')
ab('deletion',boxes['c06'],r'2°) \deleted{$\varphi$ est} Un tel hom $\varphi$ est')
ab('formula',[295,1005,1630,1210],r'connaît son action sur les $H_1(\ ,\mathbb Z_\ell)$ Ce qui revient à le connaître sur les points')
ab('punctuation',boxes['c08'],r'sont denses\ldots')
ab('formula',boxes['c09'],r'3°) $H_{\unsure{1|n}}(X,\mathbb Z_\ell)\simeq H_1(J,\mathbb Z_\ell)$')
ab('deletion',boxes['c10'],r'\deleted{le \unsure{cas}}')
ab('insertion',boxes['c11'],r'\inserted{(par 3°)} que')
ab('formula',boxes['c17'],r'$H_1(f)=H_1(g)$'+'\n'+r'$H_{\unsure{1|n}}(\varphi)=H_1(\psi)$,')
ab('formula',boxes['c12'],r'(si $f=\varphi\circ\mathrm{can}$, $g=\psi\circ\mathrm{can}$)')
ab('number',[475,1680,715,1790],'par 2°)')
ab('formula',boxes['c13'],r'$\varphi=\unsure{\varphi|\psi}$,')
ab('text',[1435,1650,1610,1765],'cqfd')
ab('deletion',[345,1825,435,1910],r'\deleted{b)}')
ab('insertion',boxes['c14'],r'\inserted{de a)} que')
ab('formula',[335,2100,525,2180],r'$\pi_1(G)$')
ab('text',boxes['c15'],r'(du moins \unsure{en|\deleted{en}} la car. $0$')
ab('number',boxes['c16'],r'\margin{24}')
coverage=[]
def cov(row,classification,change_id,reason): coverage.append(dict(row=row,classification=classification,change_id=change_id,reason=reason))
cov(1,'editorial-only','','Scan marker versus H editorial pagination note; author 12 is transcribed and audited separately.')
cov(2,'editorial-only','','The terminal stop belongs to H editorial pagination prose, not manuscript ink.')
cov(3,'material','c01','One word alors, with no separate article la; neither complete witness wording is followed.')
cov(4,'material','c02','The source uses paired raised short quote strokes rather than guillemets.')
cov(5,'material','c02,c03','Closing quote shape is preserved and the unsupported extra struck de is omitted; one de precedes X.')
cov(6,'macro-only','','The tikzcd wrapper has no textual counterpart in H display syntax.')
cov(7,'material','c06','Underlying X/can/J/phi/G map is the same; the detached comma after G is a material punctuation omission in C.')
cov(8,'macro-only','','Remaining diagram serialization tokens represent the same source map.')
cov(9,'material','c08','No terminal stop after algébriques.')
cov(10,'material','c09,c10','Short unpunctuated hom and a separate phi are visible; H expands/drops these and C supplies an absent short-form stop.')
cov(11,'material','c11','Neither C period nor H opening parenthesis is present; the next line begins capital Ce.')
cov(12,'macro-only','','C double hyphen and H long dash render the same single separating source dash.')
cov(13,'material','c12','Three source points are retained; H added closing parenthesis has no ink.')
cov(14,'material','c13','Partly readable struck le cas replaces H whole illegibility; cas remains tentative.')
cov(15,'material','c14','The apparent comma is the end of the continuous insertion leader; raised insertion state is retained.')
cov(16,'material','c15','Distinct dotted i settles si against vu.')
cov(17,'material','c16','First-reading phi versus H psi remains a localized unresolved alternative, not a resolved correction.')
cov(18,'material','c17','Inserted de a), not dans a), with attachment after hyp.')
cov(19,'material','c18','Clear la follows the single crowded en-like group; H extra split cannot be supported. Its state remains uncertain.')
cov(20,'material','c19','Thin lower-left foliation 24 is present and omitted by H.')
report=dict(scan=25,reader='/root/reader_c',lines_read=28,changes=changes,decisions=D,inventory=inv,notes=notes,checks=[],hand=hand,notation=notation,abbreviations=abbr,doubts=doubts,audit_boxes=audit,diff_coverage=coverage)
(r/'edition/reviews/149_scan025.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Wrote scan025 proposal/report: {len(changes)} changes, {len(D)} mark decisions, {len(inv)} inventory elements, {len(doubts)} doubts, {len(audit)} audit boxes, {len(coverage)} diff rows.')
