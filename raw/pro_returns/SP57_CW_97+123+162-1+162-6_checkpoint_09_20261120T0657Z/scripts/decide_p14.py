"""Root's manually adjudicated page-14 synthesis. No image recognition."""
from pathlib import Path
import copy,json,re
O=Path(__file__).resolve().parents[1]
stem='H162-01_162-1_scan003'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ['R1','R2','R3']}
T={r:(O/'readers'/stem/r/'reading.tex').read_text() for r in ['R1','R2','R3']}
t=T['R1']
def edit(a,b):
 global t
 assert t.count(a)==1,(a,t.count(a))
 t=t.replace(a,b)
edit(r'10.\unsure{I|1}.66',r'10.\unsure{5|I|1|3}.66')
edit(r'Quillen Deviations \ldots',r'Quillen Deviations \unsure{....|...}')
edit(r'Notes sur $B_G$',r'Notes sur \unsure{$B_G$|$B_g$}')
edit(r'sur fibrés vectoriels',r'sur \unsure{fibrés} vectoriels')
edit(r'\unsure{N|M}\illegible{1}',r'\unsure{M|N}\illegible{1}')
edit(r'deux schémas, Exp',r'deux sch\unsure{é|e}mas, Exp')
edit(r'K\unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}',r'K(\mathrm{P}^{n}')
edit(r'\uline{\unsure{Terjanian|Terzanian}}',r'\uline{Terjanian}')
edit(r'Greenberg sur $C_i$',r'Greenberg sur \unsure{$C_i$|$C_1$}')
edit(r'\draw[gray,line width=.9pt] (948,75)--(1355,67);',r'''\draw[gray,line width=.9pt] (948,75)--(1355,67);
% Detached source trace beneath the crossed word; no character value assigned.
\node[anchor=center] at (1176,83) {\unsure{\tikz[baseline=0pt]{\fill (0,0) circle[radius=.014cm];}}};''')
edit(r'\fill (938,265) ellipse (4 and 1.7);',r'\node[anchor=center] at (938,265) {\unsure{\tikz[baseline=0pt]{\fill (0,0) ellipse (.04cm and .017cm);}}};')
edit(r'\draw[line width=.4pt] (1127,278) .. controls (1148,237) and (1212,260) .. (1252,247);',r'''\draw[line width=.4pt] (1128,280) .. controls (1144,245) and (1159,246) .. (1191,252)
 .. controls (1224,255) and (1250,249) .. (1280,247)
 .. controls (1292,255) and (1308,278) .. (1270,290);''')
edit(r'''\draw[line width=.35pt] (600,133)--(762,131) .. controls (867,132) and (879,144) .. (888,249)
 .. controls (893,349) and (891,363) .. (939,365) .. controls (1150,371) and (1450,367) .. (1640,375);
\draw[line width=.35pt] (888,249) .. controls (898,340) and (908,397) .. (920,399)
 .. controls (1035,435) and (1410,413) .. (1660,414);''',r'''\draw[line width=.35pt] (600,133)--(762,131) .. controls (867,132) and (879,144) .. (888,249)
 .. controls (890,325) and (895,349) .. (909,360)
 .. controls (940,371) and (1450,367) .. (1640,375);
\draw[line width=.35pt] (909,360) .. controls (915,380) and (909,397) .. (932,405)
 .. controls (1035,435) and (1410,413) .. (1660,414);''')
edit(r'''\draw[line width=.4pt] (456,767)--(499,713) (489,760)--(537,711) (523,761)--(572,714)
 (556,762)--(599,718) (588,758)--(624,721);''',r'''\draw[line width=.4pt] (451,772)--(490,709);
\draw[line width=.4pt] (496,757) .. controls (479,778) and (478,770) .. (486,758)--(522,714);
\draw[line width=.4pt] (518,760) .. controls (510,771) and (509,765) .. (513,754)--(551,711);
\draw[line width=.4pt] (546,762)--(579,715);
\draw[line width=.4pt] (591,760) .. controls (580,773) and (578,765) .. (585,755)--(618,721);
\draw[line width=.4pt] (602,768)--(626,735);''')
edit(r'\draw[line width=.55pt] (196,836) .. controls (198,903) and (219,955) .. (236,983);',r'''\draw[line width=.55pt] (196,836) .. controls (198,903) and (219,955) .. (236,983);
% The faint diagonal is retained without asserting the chronology of the strokes.
\draw[gray,line width=.16pt] (236,983)--(272,848);''')
edit(r'\node (addedpapers) at (635,1287) {\resizebox{9.50cm}{!}{\inserted{Papiers Hartshorne (dim. coh.) et Goodman}}};',r'''\node[rotate=3] (addedpapers) at (635,1287) {\resizebox{3.81cm}{!}{\inserted{Papiers Hartshorne}}};
\node[rotate=3] (addedpaperscontinuation) at (1056,1268) {\resizebox{5.24cm}{!}{\inserted{(dim. \unsure{ch.|coh.}) et Goodman}}};''')
edit(r'\node (gabriel) at (573,1980) {\resizebox{2.04cm}{!}{\deleted{\unsure{Gabriel}}}};',r'''\node (gabriel) at (573,1980) {\resizebox{2.04cm}{!}{\deleted{\unsure{Gabriel}}}};
\draw[gray,line width=.35pt] (707,1953)--(721,1967)--(727,1952)--(740,1970)--(748,1955)--(759,1972)--(769,1957)--(779,1970);''')
edit(r'\draw[gray,line width=.4pt] (662,1569) .. controls (752,1697) and (854,1931) .. (953,1993);',r'\draw[gray,line width=.4pt] (658,1554) .. controls (752,1697) and (854,1931) .. (953,1993);')
edit(r'''\draw[gray,line width=.4pt] (1277,1514)--(1374,1698);
\draw[gray,line width=.4pt] (1343,1674)--(1374,1698)--(1360,1659);''',r'''\draw[gray,line width=.4pt] (1284,1521)--(1424,1843);
\draw[gray,line width=.4pt] (1341,1680)--(1370,1695)--(1354,1660);''')
edit(r'\draw[gray,line width=.7pt] (564,1697) .. controls (574,1870) and (589,2041) .. (615,2059)',r'\draw[gray,line width=.7pt] (555,1670) .. controls (574,1870) and (589,2041) .. (615,2059)')
edit(r'''\draw[gray,line width=.6pt] (1045,1670) .. controls (1215,1658) and (1432,1654) .. (1483,1658)
 .. controls (1599,1648) and (1594,1904) .. (1597,2080);''',r'''\draw[line width=.4pt] (602,1694)--(1454,1660);
\draw[gray,line width=.6pt] (1454,1660) .. controls (1580,1648) and (1594,1740) .. (1597,1850)--(1597,2080);''')
t+='\n\\clearpage\n'
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
# Root-authored apparatus modifications and final inventories are below.
spec={'stem':stem,'base_reader':'R1','brief':'reader_v14.md','text_edits':[{'old':T['R1'],'new':t}],'exclude_difference_ids':[],'difference_overrides':{},'additional_differences':[],'main_new_crops':7,'consequential':[],'s_decisions':[],'check_events':[]}
root='decisions/rootcrops/'+stem+'/'
r1='readers/'+stem+'/R1/crops/'
r2='readers/'+stem+'/R2/crops/'
r3='readers/'+stem+'/R3/crops/'
D={d['id']:copy.deepcopy(d) for d in R['R1']['differences']}
def ov(n,**kw):
 key=f'R1-D{n:03d}'
 spec['difference_overrides'].setdefault(key,{}).update(kw)
 D[key].update(kw)
def choice(n,readers,evidence,**kw):
 ov(n,readers=readers,evidence=evidence,**kw)
choice(1,r'R1/R3: suite; R2: \unsure{suite}. Root: suite.',
 'The low initial s, u connection, short i, crossed t and closing e are individually recoverable under the stroke; the cancellation does not erase the final e.')
choice(3,r'R1: $B_G$; R2/R3: \unsure{$B_G$|$B_g$}. Root retains G/g.',
 'The lowered right letter has a bowl and terminal stem, but crossing ink does not securely separate a small capital G from a lowercase g. No distinct numeral 67 follows.',final=r'\unsure{$B_G$|$B_g$}',c_changed=False)
choice(12,r'R1: 10.\unsure{I|1}.66; R2: \unsure{10.5.66|10.3.66|10.I.66}; R3: \unsure{10.5.66|10.3.66}. Root: 10.\unsure{5|I|1|3}.66.',
 'The middle form has a short upper turn and a low return that favour 5. The cancellation obscures their connection; a narrow I/1 form and a rounded 3 cannot be excluded. The first 10, separators and final 66 remain readable. No calendar or catalogue inference decides the digit.',
 final=r'10.\unsure{5|I|1|3}.66',crop=r2+'05_artin_date.png',confidence='low')
choice(16,r'R1/R2: fibrés; R3: \unsure{fibrés}. All omit the comma. Root: \unsure{fibrés}.',
 'The opening f and closing s are visible but the closely crossed middle and accent area leave the word locally doubtful. The blank gap after the terminal has no separate comma.',
 final=r'\unsure{fibrés}',c_changed=True,h_changed=True,confidence='medium',crop=r2+'11_fibres.png')
choice(17,r'R1/R2: \unsure{N|M}; R3: \unsure{M|N}. Root: \unsure{M|N}.',
 'Two tall outer strokes and a low central valley favour M. Multiple diagonal hatches cross them, so N remains possible. The covered group after the initial is physically unreadable and remains one estimated word.',
 final=r'\unsure{M|N}',c_changed=True,crop=r3+'11_label.png')
choice(18,r'R1/R3: PTTM; R2: \unsure{PTTM|PTT M}. Root: PTTM.',
 'Four contiguous capitals P, T, T and M remain recoverable beneath the hatches; the final interval does not form a separate word gap.',crop=r3+'12_PTTM.png')
choice(20,r'R1/R3: Mme; R2: \unsure{Mme|Mne}. Root: Mme.',
 'After the capital M, the small m has two low joined humps before the final e; the overlying line is separable from this body.')
choice(21,r'R1/R3: Hakim; R2: \unsure{Mathieu|Mathies}. Root: Hakim.',
 'The first tall joined strokes form H, followed by a, a high branching k, a short i and final m humps. The sequence does not contain the th and final ieu required by Mathieu.',confidence='high')
choice(25,r'R1: par.factoriel; R2/R3: \unsure{par.factoriel|parafactoriel}. Root: par.factoriel.',
 'A detached small stop follows par before the f ascender. It is not joined into an a bowl; the remaining factoriel sequence is readable.',confidence='medium')
choice(26,r'R1/R3: en; R2: \unsure{de|en}. Root: en.',
 'A low looped e joins a single n arch before dim. There is no independent tall d stem at this position.',confidence='medium')
choice(27,r'R1: \unsure{foncteur}; R2/R3: foncteur. Root retains \unsure{foncteur}.',
 'The f ascender and eur ending are visible; the central n/c/t joins lie against a cancellation contour and remain insufficiently distinct for an unqualified word.',crop=r2+'20_foncteur.png')
choice(30,r'R1/R3: équ.; R2: \unsure{équ.}. Root: équ.',
 'An accented e, descending q, joined u and separate stop are recoverable at the beginning of the upper braced subject.')
choice(31,r'R1/R3: fonction; R2: \unsure{fonction|fonctions}. Root: fonction.',
 'The final n has a low returning terminal followed by blank space before L. No separate s body follows.')
choice(36,r'R1: \unsure{n-\nu|n-i|n-1}; R2/R3: \unsure{n-i|n-1|n-\nu}. Root keeps R1 preference.',
 'After n and the raised minus, the last form has two close arms with a low curved join, favouring nu. Intersections with two cancellation rules prevent excluding i or 1. The expected formula does not settle the exponent.',crop=r2+'27_ch_formula.png')
choice(37,r'R1: \unsure{(\mathrm{P}^{n}|\mathrm{CP}^{n}}; R2/R3: (\mathrm{P}^{n}. Root resolves the opening parenthesis and P.',
 'The curve after K is separate from the P stem; n is raised at P’s right. Both inner and outer closing curves remain. The entire K-expression, which H leaves unread, is retained; the inner letter and short bar are separately adjudicated in D038.',
 final=r'Calcul $K(\mathrm{P}^{n}(\unsure{\mathrm L^{-}|\overline{\mathrm L}}))$',c_changed=True,H=r'Calcul \ill')
choice(38,r'R1/R3: \unsure{\mathrm L^{-}|\overline{\mathrm L}}; R2 additionally retains \overline{\mathrm C}. Root: L with high-right minus | overlined L.',
 'A tall upright and distinct rightward foot support L; a separate short stroke sits high to the right. Its attachment remains unclear, but the upright-foot combination does not support C.')
choice(39,r'R1: \unsure{Photocopies|photocopies}; R2/R3: \unsure{photocopies|Photocopies}. Root retains P first.',
 'The initial loop rises above the following bodies and favours a capital P; the stroke through its top prevents a definite case decision.')
choice(42,r'R1: \unsure{holodéterminants|bidéterminants}; R2/R3: \unsure{bidéterminants|holodéterminants}. Root retains holodéterminants first.',
 'Several narrow loops and a tall initial stem favour holo before the better-preserved déterminants ending. Two crossing tracks obscure the initial group; bidéterminants remains a live alternative.',crop=r2+'31_agison_bidet.png')
choice(44,r'R1/R3: \unsure{Gabriel}; R2: Gabriel. Root retains the doubt.',
 'The initial G-like loop, b ascender and final l-like stroke support Gabriel, but the middle and terminal letters are covered by the main crossing and a small separate zigzag mesh.',crop=r3+'28_gabriel.png')
choice(45,r'R1: \unsure{Terjanian|Terzanian}; R2/R3: Terjanian. Root: Terjanian.',
 'The disputed letter has a smooth descending hook rather than the body and terminal of z. The following anian sequence is separately visible.',final='Terjanian',c_changed=True,confidence='high')
choice(47,r'R1: $C_i$; R2/R3: \unsure{$C_i$|$C_1$}. Root retains i/1.',
 'The small lowered mark is visible at C’s right, but its upper point intersects the long cancellation. Its dot versus serif cannot be separated securely.',final=r'\unsure{$C_i$|$C_1$}',c_changed=False,confidence='medium')
ov(49,crop=root+'letterhead.png')
choice(50,'R1/R2 draw three definite upright traces; R3 marks the shorter third trace uncertain. Root retains all three physical traces without assigning them letter or numeral values.',
 'Two long approximately upright strokes and a separate shorter right-hand stroke precede the crossed Griffiths group. The shorter stroke is distinguishable from the two long ones; its function remains unassigned.')
choice(53,r'R1: \unsure{:|.}; R2/R3: colon. Root retains colon | point.',
 'The lower detached point is visible after Quillen; the possible upper point lies on the cancellation stroke. A colon is favoured but not certain.')
ov(55,final=r'\unsure{\tikz[baseline=0pt]{\fill (0,0) ellipse (.04cm and .017cm);}}',
 readers='R1/R3 draw the detached point without a local doubt marker; R2 marks its identity uncertain. Root retains the physical point with a local unsure graphic and assigns no character value.',
 evidence='A short separate oval trace lies below the numeral/cross at approximately (938,265). Its presence is visible but its relation to the cancellation or punctuation is not established.')
ov(56,final=r'\inserted{\deleted{10.\unsure{5|I|1|3}.66}}',readers='All three put the date below the Artin line and mark it crossed; their numeral alternatives are recorded in D012. Root retains the lowered crossed insertion. No source du occurs.')
choice(57,'R1: shallow arch ending near (1252,247); R2: arch; R3: arch with right returning hook. Root adopts the larger hooked contour.',
 'The fine stroke rises over the date, continues right and curls downward into a short return. It is separate from the heavier line through the numerals.',
 final='Thin arch from (1128,280), across (1191,252) and (1280,247), returning to (1270,290).',crop=r2+'05_artin_date.png')
choice(59,r'R1: \ldots; R2: \unsure{....|\ldots}; R3: \unsure{....|...}. All cancel the entry and omit H’s comma. Root: \unsure{....|...}.',
 'There are several short low marks after Deviations. Four are favoured, but the last meets the enclosing curve and could belong to it. The entire entry is crossed and enclosed; no comma follows Quillen.',
 final=r'\deleted{Quillen Deviations \unsure{....|...}}',c_changed=True,crop=r2+'08_quillen_goodman.png',confidence='medium')
choice(61,'R1 joins the two upper paths too early near (888,249); R2/R3 preserve near-contact without asserting a junction. Root: a real junction near (909,360), with separate rightward upper and lower tails.',
 'The local junction crop shows the upper line meeting the down-curving contour at (909,360). The separately inspected path-start crop shows the horizontal stroke beginning in the letterhead blank at (600,133), turning down at the right. The title crop shows the lower tail and the distinct closed Quillen oval. No arrowhead is added.',
 final='Long path (600,133) to (888,249) to shared (909,360), then right to (1640,375); lower branch from (909,360) to (932,405) to (1660,414); separate closed Quillen oval.',crop=root+'upper_return_junction.png')
ov(62,final=r'Notes sur \unsure{$B_G$|$B_g$}',marked_in_H='no')
ov(64,crop=root+'algebre.png')
choice(65,'R1/R2: R. Wood à Bourbaki calcul différentiel; R3: Rapport à Bourbaki calcul différentiel. Root: R. Wood; no comma after Bourbaki.',
 'A capital R and separate point precede a capital W with two low returns, then oo and a tall d. The following à is separate. There is no body sequence app-ort. No comma is visible after Bourbaki.',confidence='high')
choice(66,r'R1/R3: \uline{3}; R2: \unsure{\uline{3}|3}. Root: \uline{3}.',
 'A separate faint low stroke runs beneath the numeral and projects to its right; it is not the lower curve of 3 or the higher cancellation.',crop=r2+'36_underlined3.png',confidence='medium')
choice(67,'R1 draws six left-label strokes and five PTTM strokes; R2 draws and inventories five and four; R3 draws six each. Root adopts six at each group, with the small lower hooks visible on several PTTM strokes.',
 'The tight label and PTTM crops separate six oblique strokes at each group. Some PTTM strokes turn back at their lower ends. The left label has an independent low underline. Counts refer to physical strokes, not to the letters beneath them.',
 final='Six oblique hatches across the left label, six across PTTM, with several hooked lower ends; independent underline below the left label.',crop=r3+'12_PTTM.png')
ov(68,crop=root+'atiyah_underlines.png')
ov(69,crop=root+'atiyah_underlines.png')
choice(72,r'R1/R2: schémas; R3: sch\unsure{é|e}mas. All read deux schémas, not H’s deux séminaires. Root retains the local accent doubt.',
 'The short sch-mas body sequence is visible. The stroke above the e overlaps cancellation ink, so its accent is not secure. No comma follows Gabriel; a comma does follow the noun.',
 final=r'Séminaire Gabriel deux sch\unsure{é|e}mas,',c_changed=True,confidence='medium')
choice(73,'R1/R2 leave the left low-turn path and next broad wave separate; R3 draws a diagonal joining them. All reproduce repeated broad curves across the Bertin/Hakim rows. Root retains the faint R3-type connector without asserting chronology.',
 'The local low-turn crop shows the sloping cross-line through the two rows and the succession of broad downward curves. A very faint connector rises from approximately (236,983) to (272,848); its continuity is drawn without assigning a stroke chronology.',
 crop=root+'bertin_hakim_wave.png')
ov(75,H=r'\struck{\ill}',marked_in_H='yes',kind=r'readable ink left as \ill{}',
 evidence='After the doubly cancelled photocopies the letter group épreuves remains readable under the outer row strike. H’s undivided struck unread segment covers this region without separately rendering the word.')
ov(76,readers='R1/R3 explicitly draw repeated oblique hatches over photocopies within the cancelled EGA row; R2 inventories them but omits the separate drawing commands. Root retains R1’s nested state and hatch paths.')
ov(80,evidence='The short source le stands before the locally doubtful foncteur. H’s unread segment is unsegmented and does not separately render le; its explicit doubt applies to that region.',marked_in_H='yes')
choice(82,'R1 places a single horizontal insertion; R2/R3 retain a raised continuation. Root uses two slightly rising nodes, the continuation higher at the right.',
 'Papiers Hartshorne begins above the cancelled cohomologie line; the parenthesis and et Goodman continue slightly higher to the right. The addition is opposite Jouanolou and is not an appendage of sur cat. de Picard.',
 final=r'\inserted{Papiers Hartshorne} at (635,1287), then \inserted{(dim. \unsure{ch.|coh.}) et Goodman} at (1056,1268), both slightly rising.')
choice(83,r'R1: (dim. coh.); R2: (dim. \unsure{ch.|coh.}); R3: (dim. \unsure{coh.|ch.}). All read Hartshorne and Goodman live. Root: ch.|coh.',
 'The abbreviation has a c-like opening, tall h and stop; the intervening tiny loop may be an o or the join into h. Hartshorne and Goodman are readable and the raised entry has no local strike. H’s Godement and crossed Hertzbrouck do not match these letters or state.',
 final=r'\inserted{Papiers Hartshorne (dim. \unsure{ch.|coh.}) et Goodman}',c_changed=True,crop=r2+'21_hartshorne_insertion.png',confidence='medium')
ov(84,final=r'\deleted{Notes cohomologie $\unsure{\ell|l}$-adique}')
ov(88,readers='R1/R2/R3 all draw one left brace grouping two subject rows. Their schematic lower endpoints are respectively (863,1510), (866,1491) and (862,1505). Root retains R1’s lower arm at the observed low left of the second subject; no third grouped row is implied.',
 evidence='The brace has an upper arm, a pinched centre and a lower arm to the left of the two Serre subject baselines. Its lower curve extends below the lower words, without enclosing the following Berthelot row.')
ov(89,crop=root+'lower_cancellation_paths.png',
 readers='All three put the Deligne words in two staggered right-hand rows. R1 puts the second word at (1375,1515), R2 at (1431,1522), R3 at (1380,1524). Root retains R1’s relative horizontal placement, the long left rule and the cross-line shared with Berthelot; the lower word also has its own cancellation state.')
choice(94,r'R1/R3: Chev\unsure{.}; R2: Chev. Root retains the local point doubt.',
 'Chev is readable as an abbreviation. The small dark terminal beside v partly merges with an oblique cancellation, leaving the stop locally doubtful; the expanded Chevalley is not on this line.')
choice(100,'R1/R2/R3 all draw multiple thin diagonals and a large lower wave. Their starting points, lower extents and the fourth diagonal’s spur differ. Root retains four thin diagonals; the fourth continues through the small angled spur toward (1424,1843), and the broad wave begins near Calcul at (555,1670).',
 'The lower-context crop separates four descending thin tracks from the larger repeated wave. The fourth shaft continues beyond its two-arm angled side mark; no second independent arrow is supplied. A separate line crosses Rapport Serre from (602,1694) to (1454,1660), then the outer right contour bends down to (1597,2080). The other shafts and troughs cross both words and intervening blanks.',
 final='Four thin lower diagonals, one small angled side spur, repeated broad lower wave, Rapport strike and rounded outer right return, reproduced in their shared page coordinates.',crop=root+'lower_cancellation_paths.png')

# Additional loci are source elements or literal case differences, not layout punctuation.
def add(id,place,C,H,final,evidence,crop,kind,confidence='high',c_changed=False,h_changed=True,readers='R1/R2/R3 agree; root confirms on the cited crop.',marked=None):
 spec['additional_differences'].append(dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=crop,kind=kind,confidence=confidence,c_changed=c_changed,h_changed=h_changed,readers=readers,marked_in_H=marked if marked is not None else ('yes' if '\\ill' in H or '\\uncertain' in H else 'no')))
add('ROOT-D101','Upper right: detached point beneath the crossed Griffiths group','','',
 r'\unsure{\tikz[baseline=0pt]{\fill (0,0) circle[radius=.014cm];}} at (1176,83)',
 'A small separate dark point sits below the crossed word. It is retained without a character or punctuation value; its exact relation to the word and cancellation is uncertain.',r3+'02_griffiths.png','drawing or diagram','low',True,True,
 'R1/R2 omit the detached point in their drawings; R3 draws it. Root retains it with a local unsure graphic.')
add('ROOT-D102','Klose entry: initial case of lettre','lettre sur', 'Lettre sur','lettre sur',
 'The opening l is a narrow looped ascender continuing into the small e, not the broader capital L form elsewhere on the page.',r1+'08_klose.jpg','other')
add('ROOT-D103','Deligne right note: initial case of Lettre','Lettre Deligne','lettre\nDeligne','Lettre Deligne',
 'The opening L is tall with a clear broad lower foot; its capital form is preserved independently of the wording and placement corrections.',r1+'20_margin.jpg','other')
add('ROOT-D104','Notes Serre formula: equality and zero','=0',r'\ill','=0',
 'Two short parallel strokes are followed by a separate oval zero on the baseline. These signs remain visible beneath the two crossing rules.',r1+'21_rr_ch.jpg',r'readable ink left as \ill{}')
add('ROOT-D105','Gabriel ending: small separate cancellation mesh','','',
 'Irregular zigzag mesh from (707,1953) through alternating low/high turns to (779,1970).',
 'At the right end of the Gabriel entry, several short back-and-forth strokes form a small mesh distinct from the main row strike and broad lower cancelling curve.',r3+'28_gabriel.png','drawing or diagram','medium',True,True,
 'R1/R2 omit the local mesh from their drawings; R3 reproduces it. Root retains R3’s mesh in its observed position.')

# All C questions, including unchanged uncertainties, receive a root disposition.
cd=copy.deepcopy(R['R2']['c_doubts'])
cmap={1:1,2:2,3:3,4:4,5:None,6:5,7:6,8:7,9:8,10:9,11:10,12:11,13:12,14:13,15:14,16:15,17:16,18:17,19:None,20:18,21:19,22:20,23:21,24:22,25:23,26:24,27:25,28:26,29:27,30:28,31:29,32:30,33:31,34:32,35:33,36:34,37:35,38:36,39:37,40:38,41:39,42:40,43:41,44:42,45:43,46:44,47:45,48:46,49:47}
for q in cd:
 number=int(q['id'].split('-')[-1])
 if number in cmap and cmap[number] is not None:
  d=D[f'R1-D{cmap[number]:03d}']
  q.update(decision=d.get('final',d.get('reading')),evidence=d['evidence'],crop=d['crop'],confidence=d['confidence'])
  q['status']='retained or revised uncertainty' if '\\unsure' in q['decision'] else 'resolved from ink'
 if number==39:q['decision']=r'(\mathrm{P}^{n}';q['status']='resolved from ink'
 if number==50:q['crop']=r1+'02_griffiths_sga.jpg'
 if number==51:q['crop']=root+'algebre.png'
 if number in [54,55]:q['crop']=root+'atiyah_underlines.png'
 if number==58:q['decision']='A left brace groups the two actual subject rows, with équ. fonctionnelle fonction L above suite, début de monodromie ....';q['crop']=r1+'19_serre.jpg'
 if number==60:q['crop']=r1+'19_serre.jpg'
 if number==61:q['decision']=r'\deleted{Notes sur R.R.}\quad ?';q['crop']=r1+'16_rr_foncteur.jpg'
spec['c_doubts']=cd

rd=copy.deepcopy(R['R1']['remaining_doubts'])
rd=[x for x in rd if x['place'] not in ['Calcul: group between K and inner parenthesis','Last left name']]
for x in rd:
 if x['place']=='Artin: lowered date':x.update(reading=r'10.\unsure{5|I|1|3}.66',alternatives=['5','I','1','3'],confidence='low')
 if x['place']=='Hatched left label: initial':x.update(reading=r'\unsure{M|N}',alternatives=['M','N'])
 if x['place']=='Detached point below Artin numeral':x['reading']=r'\unsure{\tikz[baseline=0pt]{\fill (0,0) ellipse (.04cm and .017cm);}}'
rd += [
 dict(place='Giraud: lowered letter after B',reading=r'\unsure{$B_G$|$B_g$}',alternatives=['G','g'],confidence='medium'),
 dict(place='Quillen Deviations: terminal points',reading=r'\unsure{....|...}',alternatives=['four points','three points; final trace belongs to enclosure'],confidence='medium'),
 dict(place='Schwarzenberger: fibrés',reading=r'\unsure{fibrés}',alternatives=['fibrés; covered middle and accent'],confidence='medium'),
 dict(place='Séminaire Gabriel: schémas accent',reading=r'sch\unsure{é|e}mas',alternatives=['é','e'],confidence='medium'),
 dict(place='Raised Hartshorne: short abbreviation',reading=r'\unsure{ch.|coh.}',alternatives=['ch.','coh.'],confidence='low'),
 dict(place='Final Greenberg entry: C subscript',reading=r'\unsure{$C_i$|$C_1$}',alternatives=['i','1'],confidence='medium'),
 dict(place='Detached point beneath Griffiths',reading=r'\unsure{\tikz[baseline=0pt]{\fill (0,0) circle[radius=.014cm];}}',alternatives=['unassigned ink point','surface or cancellation trace'],confidence='low')]
for x in rd:
 if isinstance(x['alternatives'],list):x['alternatives']='; '.join(x['alternatives'])
spec['remaining_doubts']=rd
spec['consequential']=[r'Calcul: an independent opening parenthesis after K and a separate P with raised n are resolved, eliminating C’s CP alternative. The inner L/bar remains locally doubtful (D037–D038).',r'The Serre title’s =0 and the full K-expression, left unread in H, are retained from their visible strokes. This restores mathematical content but does not verify either expression (D035–D038, ROOT-D104).']

inv=copy.deepcopy(R['R3']['inventory'])
for x in inv:
 s=x['first_words_or_objects']
 for a,b in [('Rapport à Bourbaki','R. Wood à Bourbaki'),('10.5.66/10.3.66','10.(5/I/1/3).66'),('Quillen : sur','Quillen (:/.) sur'),('M/N and unread group','M/N and one unread word'),('sur fibrés vectoriels','sur doubtful fibrés vectoriels'),('par.factoriel/parafactoriel','par.factoriel'),('le foncteur dét.','le doubtful foncteur dét.'),('dim. coh./ch.','dim. ch./coh.'),('n-i/n-1/n-nu','n-nu/n-i/n-1'),('photocopies/Photocopies','Photocopies/photocopies'),('bidéterminants/holodéterminants','holodéterminants/bidéterminants')]:s=s.replace(a,b)
 x['first_words_or_objects']=s
 if x['element']=='Circled R.R. entry':x['first_words_or_objects']='Notes sur R.R. (cancelled); separate following ? live';x['source_state']='mixed: words cancelled, following question live'
 if x['element']=='Circled R.R. entry cancellation':x['first_words_or_objects']='Notes sur R.R. only; following ? remains live'
 if x['element']=='Hatched PTTM: six slants':x['first_words_or_objects']='six diagonals; several hooked lower ends'
 if x['element']=='Bertin/Mme Hakim connected cancellation':x['first_words_or_objects']='repeated troughs spanning both rows; faint left diagonal connector; upper return at right'
 if x['element']=='Two tall shafts, shorter third shaft and detached point before/below Griffiths':x['first_words_or_objects']='two long shafts; separate shorter third shaft; detached point of uncertain function'
 if x['element']=='Deligne note vertical stroke':x['first_words_or_objects']='vertical rule left of note; cancellation shared with Berthelot; lower row also cancelled'
 if x['element']=='Long upper return contours':x['first_words_or_objects']='left horizontal and downward return, shared junction at (909,360), two distinct rightward tails'
 if x['element']=='Lower long diagonal cancellations':x['first_words_or_objects']='four long diagonals; fourth continues beyond a small two-arm angled side spur'
 if x['element']=='Lower broad repeated cancellation and outer return':x['first_words_or_objects']='broad repeating troughs from Calcul downward; Rapport strike; rounded outer right return'
 if x['element']=='Gabriel entry':x['first_words_or_objects']='doubtful Gabriel'
 if x['element']=='Gabriel entry cancellation':x['first_words_or_objects']='doubtful Gabriel'
 if x['element']=='Chev. grassmanniennes entry' or x['element']=='Chev. grassmanniennes entry cancellation':x['first_words_or_objects']='Notes Chev (stop doubtful) sur grassmanniennes/grassmaniennes'
 x['transcribed']='yes'
inv=[x for x in inv if x['element']!='Serre letter with two subjects']
for i in [54,55,56]:
 x=copy.deepcopy(R['R2']['inventory'][i-1]);x['hand']='principal manuscript hand; personal attribution not independently established'
 if i==55:x['first_words_or_objects']='équ. fonctionnelle fonction L'
 inv.append(x)
inv.sort(key=lambda x:(x['position']['bbox'][1],x['position']['bbox'][0],x['kind']=='deletion'))
for x in inv:
 p=x['position'];x['position']='Whole-image box '+str(p['bbox'])+('; '+p.get('note','') if p.get('note') else '')
spec['inventory']=inv
spec['abbreviations']=copy.deepcopy(R['R2']['abbreviations'])
spec['abbreviations'].append({'form':'par.factoriel','expansion':'Probably parafactoriel; proposed editorial expansion of the abbreviated first component only.'})
for x in spec['abbreviations']:
 if x['form']=='Mme | Mne':x.update(form='Mme',expansion='Madame; editorial expansion only.')
 if x['form']=='équ.':x['expansion']='équation; editorial expansion only.'
spec['notes']='''This is a handwritten list of papers, letters, copies and subjects on printed Institut des Hautes Études Scientifiques stationery. Underlined names stand at the left of associated entries. Numerous local and grouped cancellations cross both entries and blank intervals; these marks do not by themselves establish whether a document was returned or where it was kept. The printed address and telephone line are transcribed in full. A pale archive number 2 is retained only in the required source comment.

The live Shih subject begins “R. Wood à Bourbaki calcul différentiel”: the separate R., double-return W, two low o forms and d stem favour this over C’s Rapport. The crossed title under Goodman reads Deviations, without the extra r of Derivations. The recipient beneath Bertin reads Mme Hakim rather than Mathieu/Mathies. Other restored wording includes the English Hartshorne title, dimension with two following points, and the final mon exemplaire personnel. The place-specific apparatus records the literal witness strings and all reader disagreements.

The crossed lowered date is 10.(5/I/1/3).66, with 5 preferred only from its short upper turn and low return. The stroke through the middle character leaves the alternatives open. No catalogue chronology or date mentioned on another sheet has been used to resolve it. Explicit source hesitations are the live question mark outside the cancelled, circled Notes sur R.R. and the question mark after Congrès d'Amsterdam; both visible closing curves after the latter are retained.

The short mathematical entries are subjects or titles, not derivations. B has a lowered G/g; the Serre formula retains doubtful ch/dh and n−ν/n−i/n−1, followed by visible =0; Calcul has K followed by an independent opening parenthesis and P with raised n, while the inner L and its high-right short stroke remain locally doubtful. The final C has a doubtful i/1 subscript. These decisions concern stroke identity and placement. No truth of a formula, computation in K-theory, or bibliographic identification was checked, so these visual readings are not recorded as proof events.

The raised Hartshorne/Goodman addition is distinct from both the Picard line and the cancelled cohomologie line below it. The cramped parenthesis retains ch./coh. uncertainty. The two Serre subjects remain on separate baselines under one brace, with L on the upper baseline. The right-hand Deligne note has complexes on its first line and elliptiques below; its long rule and cancellation are preserved. Physical roman numeral cap/base strokes, local R.R. versus RR punctuation, six hatches at each small crossed label, the separate Gabriel ending mesh, and the extended lower cancellation paths are all retained without assigning an unrecorded chronology or function.'''
spec['workflow_note']='''Three fresh readers used v14 and each viewed the whole and each half once, followed by 28/36/30 local crops. Root compared all three complete texts, difference lists, C decisions, notes and inventories, and adjudicated with 28 existing R1 crops, nine existing R2 crops, four existing R3 crops, and seven new bounded crops (letterhead, Atiyah underlines, Algèbre numeral, upper junction, Bertin low turns, lower spanning paths, upper path start). Five R1 image displays initially failed and were successfully displayed later; failed displays supplied no visual evidence. Oversized text outputs were reread in smaller pieces. No whole image or half was reread by root.

R1 supplied the positioned base; root selected the other readers’ visible additions and retained actual uncertainty where their letters differed. A separate text-only audit checked witness quotation scope and the union of reader variations; it had no image authority. R2’s list-wide dash/semicolon differences are excluded as linearizing editorial layout, not manuscript text. Archive-number metadata is likewise not counted as a textual correction. The next brief will require drawing paths and inventories to agree in stroke count, local accent and punctuation doubts to remain visible, and unsegmented H unread spans to be quoted without claiming an unwritten word was certainly absent. Reader mathematical remarks were visual checks of titles and symbols, not proofs.'''
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2))
print(json.dumps({'preview_saved':stem,'base_loci':100,'additional_loci':len(spec['additional_differences']),'c_questions':len(cd),'inventory':len(inv),'remaining':len(rd)}))
