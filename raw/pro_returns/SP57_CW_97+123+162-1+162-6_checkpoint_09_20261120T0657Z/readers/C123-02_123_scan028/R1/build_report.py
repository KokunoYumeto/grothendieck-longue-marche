from pathlib import Path
import json

base = Path('/workspace/scratch/288d9a82260f')
out = base/'out/readers/C123-02_123_scan028/R1'
C = (base/'packets/C123-02_123_scan028/C.tex').read_text()
H = (base/'packets/C123-02_123_scan028/H.tex').read_text()
R = (out/'reading.tex').read_text()
manifest = [json.loads(line) for line in (out/'crops/crop_manifest.jsonl').read_text().splitlines()]
crop_map = {row['dest'].removesuffix('.png'): row for row in manifest}
source = 'source/SP57_CW_97+123+162-1+162-6_scans/C123-02_123_scan028.jpg'

def cx(s):
    assert s in C, ('C quotation', s)
    return s

def hx(s):
    assert s in H, ('H quotation', s)
    return s

def cspan(start, end):
    a = C.index(start)
    b = C.index(end, a) + len(end)
    return C[a:b]

def rspan(start, end):
    a = R.index(start)
    b = R.index(end, a) + len(end)
    return R[a:b]

differences = []
def diff(place, c, h, reading, evidence, kind, changed_c=False, changed_h=True,
         confidence='high', crop=None, bbox=None):
    if crop:
        row = crop_map[crop]
        bbox = bbox or row['box']
        crop = 'readers/C123-02_123_scan028/R1/crops/' + row['dest']
    assert bbox is not None
    differences.append(dict(id=f'D{len(differences)+1:02d}', place=place, C=c, H=h,
        reading=reading, evidence=evidence, confidence=confidence, kind=kind,
        marked_in_H=False, c_changed=changed_c, h_changed=changed_h,
        crop=crop, bbox=bbox, bbox_source=source))

diff('Handwritten page number', cx(r'\mspage{\handwritten{22}}'), hx('paginé « 72 »'),
     r'\mspage{\handwritten{\unsure{2|7}2}}',
     'The first digit has a bowed top and a descending stem with a very short basal turn; the basal stroke does not securely distinguish 2 from 7. The second digit has a definite lower rightward foot.',
     'misread symbol or index', True, confidence='medium', crop='01_page_number')
diff('Opening continuation paragraph',
     cspan(r'\deleted{un morphisme', r'3.2.1)}}'), '',
     cspan(r'\deleted{un morphisme', r'3.2.1)}}'),
     'Half a contains three complete typed lines beginning un morphisme, with the two quotation pairs, resp., both starred functors, and the final pen reference. H summarizes the subject but does not transcribe this paragraph.',
     'omission', bbox=[269,153,1683,344])
diff('Older digit in the opening reference', cx(r'\handwritten{(\deleted{\unsure{2|3}}3.2.1)}'), hx('« (3.2.1) »'),
     r'\handwritten{(\deleted{\unsure{2|3}}3.2.1)}',
     'A final two-lobed 3 overlies a smaller form with a low horizontal foot. The latter favors 2 but its covered middle remains compatible with 3; H gives only the final number.',
     'omission', confidence='low', crop='02_opening_reference')
diff('Revised initial digit of 3.1.2', cx(r'\deleted{\unsure{2|3}}\handwritten{3}.1.2.'), hx('n°~3.1.2'),
     r'\deleted{2}\handwritten{3}.1.2.',
     'Inside the larger pen 3, the smaller original digit retains a down-left diagonal ending in a straight typewriter baseline and right serif. Those are the surviving contours of 2.',
     'misread symbol or index', True, crop='03_section_digit')
diff('Exactness paragraph: full typed exposition',
     cspan(r'Si $\mathrm{u}', r'\uline{exact}.'), '',
     r'Si $\mathrm{u}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}\prime$ est un morphisme de topos, il résulte des propriétés des foncteurs adjoints ... on voit donc en particulier que $\mathrm{u}^{\handwritten{*}}$ \uline{est} \deleted{exac} \uline{exact}.',
     'Half a supplies the prose, directions E to E-prime and E-prime to E, the two kinds of limits, and the explicit finite-limit condition. H has an editorial summary in place of the complete cancelled typescript.',
     'omission', bbox=[270,364,1683,764])
diff('Curved insertion leader for (I 2.11)', cx(r'\inserted{\handwritten{(I 2.11)}}'), hx('« (I~2.11) »'),
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1que.base)', r'\end{tikzpicture}}'),
     'The curve begins below the baseline immediately before que, sweeps under the raised reference, and turns upward at the right. It is one graphic stroke separate from the long vertical cancellation.',
     'drawing or diagram', True, crop='04_adjoints_reference_leader')
diff('Cancelled left marginal reference', cx(r'\margin{\handwritten{\deleted{\unsure{(I 2.11)|(I 4.11)|(I 4.1)}}.}}'), '',
     r'\margin{\handwritten{\deleted{\unsure{(I 2.11)|(I 4.11)}}.}}',
     'Two separate narrow stems follow the decimal point. The preceding digit remains crossed by the diagonal cancellation and can be 2 or 4. The final point lies to the right of the closing parenthesis and outside the crossing strokes.',
     'other', True, confidence='low', crop='05_margin_reference')
diff('Cancelled body reference after inductives', cx(r'\deleted{\unsure{(2.11)|(2.1)|(I 2.11)}}'), '',
     r'\deleted{\unsure{(2.11)|(I 2.11)}}',
     'After the low point there are two distinct vertical stems before the closing parenthesis. The heavy blue crossing conceals whether a separate I precedes 2.',
     'other', True, confidence='low', crop='06_body_reference_star')
diff('Footnote marker after cancelled body reference', cx(r'\handwritten{(${}^{*}$)}'), '',
     rspan(r'\handwritten{\mbox{\begin{tikzpicture}[baseline=(p28r1star.base)', r'\end{tikzpicture}}}.Comme'),
     'The star is definite. Below its central junction two additional descending prongs survive inside the parentheses; they are not represented by a plain superscript star. Both are drawn, with their function left uncertain.',
     'drawing or diagram', True, confidence='medium', crop='06_body_reference_star')
diff('Uncertainty retained in the word exact of the insertion', cx(r'est \unsure{exact} à gauche i.e.'), hx(r'\marginal{est exact à gauche i.e.}'),
     r'est \unsure{exact} à gauche i.e.',
     'The e, crossed x and final rising t are visible; the tiny central material is compressed into a point and low curve. The full word remains a plausible but not fully resolved reading.',
     'other', confidence='medium', crop='07_exact_insertion')
diff('Leader below est exact à gauche i.e.', cx(r'\inserted{\handwritten{est \unsure{exact} à gauche i.e.}}'), hx(r'\marginal{est exact à gauche i.e.}'),
     r'\draw[line width=.35pt] (-.3,-.25) .. controls (-.6,.5) and (-.1,.8) .. (1.15,.9) .. controls (4.1,1.15) and (8.7,.95) .. (9.5,1.1) .. controls (9.9,1.16) and (10,1.35) .. (9.92,1.48);',
     'A continuous curve comes up from the left of commute, passes under the insertion, and turns upward at its right end.',
     'drawing or diagram', True, crop='07_exact_insertion')
diff('Detached point above the right end of the exactness insertion leader', '', '',
     r'\unsure{\begin{tikzpicture}\fill (0,0) circle (.35pt);\end{tikzpicture}}',
     'There is a detached small dark point above and slightly left of the final upward hook. Its graphic presence is recorded without making it sentence punctuation; ink versus incidental surface mark remains uncertain.',
     'omission', True, confidence='low', crop='07_exact_insertion', bbox=[1590,550,1606,568])
diff('Local state of commute aux limites projectives finies', cx('commute aux limites projectives finies'), hx('au-dessus de « commute aux limites projectives finies », qu\'il remplace'),
     'commute aux limites projectives finies (live locally within the cancelled sheet)',
     'The added curve is above commute and falls at its left; it does not strike through the typed letters. All words remain locally live. The long vertical sheet cancellation is a separate state.',
     'deletion state (struck given live or live given struck)', crop='07_exact_insertion', bbox=[275,580,1623,693])
diff('Cancelled exac at the right edge', cx(r'\deleted{exac}'), '', r'\deleted{exac}',
     'The four visible cells retain e, x, a and c under the typewriter x cancellation; the image ends immediately after the c cell. No final t is supplied.',
     'omission', crop='08_exac_edge')
diff('Underlines beneath est and exact', cx(r'\uline{est} \deleted{exac} \uline{exact}'), hx('donc $u^*$ est exact'),
     r'\uline{est} \deleted{exac} \uline{exact}',
     'Half a shows a low pen rule under est on the upper physical line and another under exact on the following line; the full stop is outside the second underline.',
     'omission', bbox=[275,643,1585,766])
diff('On peut donc dire que: physical position and leader', cx(r'\inserted{On peut donc dire que}'), hx(r'\marginal{On peut donc dire que}'),
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1cest.base)', r'\end{tikzpicture}}'),
     'The insertion is typed above c\'est. A separate thin curved leader starts to the left of c\'est, runs beneath the inserted words, and has a short upward right terminal.',
     'drawing or diagram', True, crop='09_on_peut_cest')
diff('Initial C corrected to c in c\'est', cx(r"\deleted{C}\handwritten{c}'est"), hx('c\'est le foncteur image inverse'),
     r"\deleted{C}\handwritten{c}'est",
     'The original larger typed contour and the smaller round pen contour both survive at the initial cell; H quotes only the final lower-case form.',
     'omission', crop='09_on_peut_cest')
diff('Cancelled qui before dans le couple', cx(r'\deleted{qui}, dans le couple'), hx(r'$u^*$ qui, dans le couple'),
     r'\deleted{qui}, dans le couple',
     'The q descender, u stems and i point survive beneath three overtyped x impressions. The following comma is separate and uncancelled locally.',
     'deletion state (struck given live or live given struck)', crop='10_cancelled_qui')
diff('Second live qui after the pair of functors', cx(r'\uline{qui possède les propriétés'), hx(r'$(u_*,u^*)$, possède les propriétés'),
     r"$(\mathrm{u}_{\handwritten{*}},\mathrm{u}^{\handwritten{*}})$, \uline{qui possède les propriétés d'exactitude les plus remarquables}",
     'Half a shows qui immediately after the comma following the parenthesized pair, and the underline begins beneath this qui. H\'s quoted sentence omits it.',
     'omission', bbox=[279,786,1666,838])
diff('Underlining of the two assertions about image inverse',
     cx(r"\uline{\deleted{C}\handwritten{c}'est \deleted{donc} le foncteur image inverse}"),
     hx(r"c'est le foncteur image inverse $u^*$ qui, dans le couple"),
     r"\uline{\deleted{C}\handwritten{c}'est \deleted{donc} le foncteur image inverse}; \uline{qui possède les propriétés d'exactitude les plus remarquables}",
     'Two distinct low horizontal pen rules underline these successive source lines. The first stops before u-star, the second stops before the final comma.',
     'omission', bbox=[410,720,1666,839])
diff('Cancelled assurant before Ces propriétés', cx(r'\deleted{assurant} Ces propriétés'), '', r'\deleted{assurant} Ces propriétés',
     'Half a shows all eight letters of assurant beneath the x cancellation, followed by the capitalized live Ces.',
     'omission', bbox=[274,852,530,906])
diff('Full prose defining the admissible structures',
     cspan('Ces propriétés assurent', 'quelconques,'), '',
     cspan('Ces propriétés assurent', 'quelconques,'),
     'Halves a and b give the full passage about data of arrows, base sets, repeated finite projective limits and arbitrary inductive limits. H replaces it with a short descriptive summary.',
     'omission', bbox=[275,853,1683,1185])
diff('Sigma insertion leader', cx(r'\inserted{\handwritten{$\Sigma$}}'), hx(r'lettre $\Sigma$ encrées'),
     r'\draw[line width=.35pt] (-.25,-.35) .. controls (-.5,.3) and (-.1,.65) .. (1,.78) .. controls (2.5,.82) and (3.7,.93) .. (4,1.12) .. controls (4.15,1.22) and (4.1,1.4) .. (4.1,1.45);',
     'The broad Sigma is above the cancelled words; its separate leader curves up from before qui and ends in an upward hook to the right beneath the letter.',
     'drawing or diagram', True, crop='11_sigma_qui_peut')
diff('Faint arc below Sigma', '', '',
     r'\unsure{\begin{tikzpicture}[x=1em,y=1em]\draw[line width=.2pt,gray] (0,.12) .. controls (.15,-.08) and (.48,-.04) .. (.72,.1);\end{tikzpicture}}',
     'A short faint curved trace sits immediately below the left portion of Sigma\'s bottom bar. It is distinct from the lower dark insertion leader. Its function and whether it is ink are unresolved.',
     'omission', True, confidence='low', crop='11_sigma_qui_peut', bbox=[495,930,532,945])
diff('Cancellation x in the blank cell between qui and peut', cx(r'\deleted{qui peut}'), '',
     r'\deleted{qui}\texttt{x}\deleted{peut}',
     'The cancelled q, u, i and p, e, u, t remain legible. Between the two words an otherwise unoccupied cell contains a complete standalone x impression.',
     'omission', True, crop='11_sigma_qui_peut')
diff('et pour insertion leader', cx(r'\inserted{\handwritten{et pour}}'), hx(r'\marginal{et pour}'),
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1tout.base)', r'\end{tikzpicture}}'),
     'The words sit above and slightly left of tout; the pen curve starts before tout, sweeps under pour and turns back upward at the far right.',
     'drawing or diagram', True, crop='12_et_pour_quote_E')
diff('Quotation around objet de E-prime ... Sigma', cx(r'\handwritten{``}objet'), hx('« tout objet de $E\'$ muni d\'une structure d\'espèce $\Sigma$ »'),
     r"\handwritten{``}objet de $\underline{\mathrm{E}}\prime$ muni d'une structure d'espèce $\handwritten{\Sigma}$''",
     'Two tall opening pen quotation strokes precede objet, and the closing paired typewriter strokes follow the later Sigma. H\'s editorial quotation does not transcribe this inner quotation state.',
     'omission', crop='12_et_pour_quote_E', bbox=[1251,1134,1668,1256])
diff('Underlined E in objet de E-prime', cx(r"$\underline{\mathrm{E}}'$"), hx(r"« tout objet de $E'$ muni"),
     r'$\underline{\mathrm{E}}\prime$',
     'The E has a single ordinary typewriter contour and a detached low horizontal rule. The prime is a separate high stroke to its right.',
     'misread symbol or index', crop='12_et_pour_quote_E', bbox=[1441,1146,1492,1190])
diff('Parenthetical explanation of internal exactness',
     cspan('(notion qui a un sens', '(II 4.1))'), '',
     '(notion qui a un sens grâce aux propriétés d\'exactitude \\deleted{de} internes du topos E\' (II 4.1))',
     'Half b gives this full parenthesis, including the numbered reference and the small cancelled de. H omits the parenthesis.',
     'omission', bbox=[275,1207,1683,1333])
diff('Cancelled de before internes', cx(r'\deleted{de} internes'), '', r'\deleted{de} internes',
     'The d ascender and e bowl survive under the two x impressions; internes starts after a gap.',
     'omission', bbox=[527,1289,758,1326])
diff('E-prime after topos: heavy lower material', cx(r"$\mathbb{E}'$"), '',
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1E.base)', r'\end{tikzpicture}}'),
     'E and its prime are definite. The lower half is heavily filled and the right lower contour projects downward, but a second complete E impression cannot be isolated. The definite E is kept outside the doubt; the extra lower bar/right trace is drawn as uncertain second impression or pen reinforcement.',
     'other', True, confidence='medium', crop='13_topos_E')
diff('Cancelled inverse in son image inverse par', cx(r'son image \deleted{inverse} par'), hx(r"l'image inverse par $u^*$"),
     r'son image \deleted{inverse} par',
     'Half b shows a heavy horizontal pen stroke through inverse, with a rising terminal at the right. The adjacent son image and par are not locally crossed.',
     'deletion state (struck given live or live given struck)', bbox=[1211,1280,1647,1331])
diff('Formal justification explicitly declined in the full prose',
     cspan('est muni des mêmes structures.', 'au lecteur de'), '',
     cspan('est muni des mêmes structures.', 'au lecteur de'),
     'Half b reads est muni and then Plutôt que d\'entrer ... donner un sens précis ... le justifier de façon formelle. This explicit hesitation is absent from H\'s summary.',
     'omission', bbox=[275,1350,1683,1536])
diff('l\'expliciter et de: raised position and curved leader', cx(r"\inserted{l'expliciter et de}"), hx(r"\marginal{l'expliciter et de}"),
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1se.base)', r'\end{tikzpicture}}'),
     'Half b shows typewritten added words above se convaincre. A thin curve comes up immediately before se and runs beneath the insertion to an upward right terminal.',
     'drawing or diagram', True, bbox=[1189,1458,1596,1540])
diff('Three detached points below pour des', '', '',
     r'\fill (.3,0) circle (.45pt); \fill (.15,-.27) circle (.45pt); \fill (0,-.56) circle (.35pt);',
     'The crop shows exactly three dark detached points in a descending-left diagonal below the space after pour. They are drawn as three separate points, with no assigned textual function.',
     'omission', True, confidence='medium', crop='14_dots_below_pour')
diff('Full example list and singular celle',
     cspan('des espèces de structure telles que celle de groupe', 'de torseur sous un groupe.'),
     hx('exemples : groupe, anneau, module, comodule,\nbigèbre, torseur'),
     cspan('des espèces de structure telles que celle de groupe', 'de torseur sous un groupe.'),
     'Half b preserves singular celle, the repeated sur un anneau, sous un groupe, articles and punctuation; H gives only six example nouns.',
     'omission', bbox=[276,1569,1653,1751])
diff('Two x impressions in cancelled ou de bimodule', cx(r'\deleted{ou de bimodule}'), '',
     r'\deleted{ou}\texttt{x}\deleted{de}\texttt{x}\deleted{bimodule}',
     'Each otherwise blank separator cell, after ou and after de, contains its own x. The underlying letters of all three words remain visible.',
     'omission', True, crop='15_bimodule')
diff('Unfinished final body parenthesis', cx('(Dans ces exemples, les trois premières espèces de structure se définis'), '',
     '(Dans ces exemples, les trois premières espèces de structure se définis',
     'Half b shows the opening parenthesis and the visible word fragment définis running into the right image edge. There is no visible completion or closing parenthesis.',
     'omission', bbox=[276,1770,1683,1826])
diff('Long wavy footnote separator', cspan(r'\handwritten{\figure{', r'\end{tikzpicture}}}'), '',
     cspan(r'\handwritten{\figure{', r'\end{tikzpicture}}}'),
     'Whole-page layout and half b show a single long, slightly wavy horizontal separator from near the left sheet margin to the right edge.',
     'drawing or diagram', bbox=[78,1823,1655,1857])
diff('Page-wide vertical cancellation, including interruption at the raised footer reference',
     cx('% A single long vertical cancellation stroke runs through the typescript, from the opening paragraph into the footnote. The three enclosing deletion macros preserve this page-wide cancellation; inner deletion macros preserve the local revisions.'),
     hx('barré d\'un long trait vertical'),
     rspan(r'\handwritten{\figure{\begin{tikzpicture}[remember picture,overlay]', r'\end{tikzpicture}}}'),
     'The whole view locates a long slightly bowed cancellation through the body and footer. The footer crop shows an interrupted part near 1.5: two detached dark points and a short segment between the upper and continuing lower paths. All five graphic components are drawn; prose deletion wrappers alone do not preserve them.',
     'drawing or diagram', True, confidence='medium', crop='17_verifier_reference', bbox=[719,237,862,2125])
diff('Footnote: complete prose and both functor directions',
     cspan(r'\deleted{($\handwritten{*}$)', r'\unsure{(ii)|(iii)|(i)}}}'), '',
     '($\\handwritten{*}$) ... pour un foncteur $\\mathrm{u}_{\\handwritten{*}}:\\mathrm{E}\\handwritten{\\longrightarrow}\\mathrm{E}\prime$ resp. $\\mathrm{u}^{\\handwritten{*}}:\\mathrm{E}\prime\\handwritten{\\longrightarrow}\\mathrm{E}$ donné, ... admet un adjoint à gauche (resp. à droite si et seulement si il commute aux ... limites projectives (resp. aux $\\underline{\\mathrm{U}}$-limites inductives).',
     'Half b gives four source lines, the left/right adjoint alternatives, si et seulement si, the two U-qualified limit conditions, and the local revisions. H transcribes none of this prose, mentioning only selected corrections editorially.',
     'omission', bbox=[274,1847,1683,2125])
diff('Footnote cancelled On peut', cx(r'\deleted{On peut}'), '', r'\deleted{On peut}',
     'Both words survive beneath the pen crossing; On begins with a round capital and peut retains its p descender and final t.',
     'omission', crop='16_footnote_opening', bbox=[369,1868,521,1916])
diff('Footnote d changed to D in D\'ailleurs', cx(r"\deleted{d}\handwritten{D}'ailleurs"), '',
     r"\deleted{d}\handwritten{D}'ailleurs",
     'The small typed d has a surviving lower bowl and stem inside the much taller handwritten D.',
     'omission', crop='16_footnote_opening', bbox=[527,1851,730,1914])
diff('Cancelled vérifier que resolved', cx(r'\deleted{\unsure{vérifier que}}'), hx('« vérifier » est biffé'),
     r'\deleted{vérifier que}',
     'The crop exposes the accented é, dotted i cells, tall f, final r, q descender, u and terminal e despite the diagonal strokes. The cancelled text includes que as well as vérifier.',
     'other', True, crop='17_verifier_reference')
diff('Raised (1.5 et 1.8) and its leader', cx(r'\inserted{\handwritten{(1.5 et 1.8)}}'), hx('« (1.5 et 1.8) »'),
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1verifier.base)', r'\end{tikzpicture}}'),
     'The reference is above the cancelled phrase. A lighter leader rises before vérifier, runs beneath the reference, and turns sharply up at the right; the following typed comma is live locally.',
     'drawing or diagram', True, crop='17_verifier_reference')
diff('Footnote d corrected to c in ce foncteur', cx(r'\deleted{d}\handwritten{c}e foncteur'), '',
     r'\deleted{d}\handwritten{c}e foncteur',
     'The typed d contour and ascender remain inside a broader handwritten c-shaped curve; the following e is separate and undisturbed.',
     'omission', crop='18_ce_overprint')
diff('First U: alphabet and medium', cx(r'\inserted{$\underline{\mathrm{U}}$-}'), hx('« $\mathcal{U}$- » devant'),
     r'\inserted{$\underline{\mathrm{U}}$-}',
     'The raised U has straight slab serifs, the same machine form as the second U, and its own detached low rule. It is typed ordinary underlined U, not a handwritten script capital.',
     'misread symbol or index', crop='19_first_U')
diff('Leader for the first U-', cx(r'\inserted{$\underline{\mathrm{U}}$-}limites'), hx('« $\mathcal{U}$- » devant\n« limites projectives »'),
     rspan(r'\mbox{\begin{tikzpicture}[baseline=(p28r1limites.base)', r'\end{tikzpicture}}'),
     'A separate thin pen curve starts before limites below its baseline and rises past the l to the upper right; the detached underline under U is a different stroke.',
     'drawing or diagram', True, crop='19_first_U')
diff('Second underlined U-', cx(r'(resp. aux $\underline{\mathrm{U}}$-limites inductives)'), '',
     r'(resp. aux $\underline{\mathrm{U}}$-limites inductives)',
     'The second U is on the typed baseline with one ordinary contour and a detached low rule; the hyphen follows at mid-height.',
     'omission', crop='20_second_U')
diff('Cancelled D\'ailleurs at the start of the final sentence', cx(r"\deleted{\unsure{D'ailleurs},"), '',
     r"\deleted{\unsure{D'ailleurs}\unsure{,}}",
     'The initial word is heavily covered. Surviving ascenders and the latter e/u/r/s-like contours support D\'ailleurs, but several initial cells cannot be separated from the crossing strokes.',
     'omission', confidence='low', crop='21_final_dailleurs')
diff('Comma after the final cancelled D\'ailleurs', cx(r"\unsure{D'ailleurs},"), '',
     r"\unsure{D'ailleurs}\unsure{,}",
     'A dark down-turn occurs at the expected separator cell but joins the cancellation. It does not independently establish an ordinary comma, so the punctuation is retained with doubt.',
     'other', True, confidence='low', crop='21_final_dailleurs', bbox=[756,2073,783,2104])
diff('Additional low-right tail under final cancelled D\'ailleurs', '', '',
     r'\draw[line width=.25pt,gray] (0,0) .. controls (.2,-.1) and (.5,-.4) .. (.75,-.45);',
     'A faint diagonal tail runs down-right below the word ending and the main cancellation. It is drawn separately without assigning it to a letter or punctuation sign.',
     'drawing or diagram', True, confidence='low', crop='21_final_dailleurs', bbox=[744,2080,777,2110])
diff('Final cancelled reference after 1.2.', cx(r'1.2.\unsure{(ii)|(iii)|(i)}'), hx('« c\'est une conséquence immédiate de 1.2 » est barrée'),
     r'1.2.\unsure{(ii)|(iii)|(i)}',
     'The typed 1, point, 2 and following point remain exposed. A further dense cancelled group with dotted narrow stems follows; the number of i strokes and enclosing parentheses remain uncertain. H stops its quotation at 1.2.',
     'omission', confidence='low', crop='22_final_index')

c_doubts = []
def cd(place, c, decision, evidence, confidence='medium', crop=None, bbox=None):
    if crop:
        row = crop_map[crop]
        bbox = bbox or row['box']
        crop = 'readers/C123-02_123_scan028/R1/crops/' + row['dest']
    c_doubts.append(dict(place=place, C=c, decision=decision, evidence=evidence,
                         confidence=confidence, crop=crop, bbox=bbox, bbox_source=source))

cd('Opening reference: older digit', r'\deleted{\unsure{2|3}}3.2.1', 'Retain older 2|3 doubt; final 3 certain.',
   'A low foot favors 2, but the covered central portion does not eliminate an older 3.', 'low', '02_opening_reference')
cd('Section number: older digit', r'\deleted{\unsure{2|3}}\handwritten{3}.1.2.', r'\deleted{2}\handwritten{3}.1.2.',
   'The smaller diagonal and straight lower serif remain distinguishable within the larger final 3.', 'high', '03_section_digit')
cd('Left marginal reference', r'\unsure{(I 2.11)|(I 4.11)|(I 4.1)}', r'\unsure{(I 2.11)|(I 4.11)}',
   'Two narrow final stems are separate; the earlier digit is crossed and remains 2|4.', 'low', '05_margin_reference')
cd('Cancelled body reference', r'\unsure{(2.11)|(2.1)|(I 2.11)}', r'\unsure{(2.11)|(I 2.11)}',
   'Two final 1 stems survive. Any initial I is obscured in the blue cancellation.', 'low', '06_body_reference_star')
cd('est exact à gauche i.e.', r'est \unsure{exact} à gauche i.e.', 'Retain the local exact doubt.',
   'The central a/c material is too compressed to certify every letter, although the surrounding strokes support exact.', 'medium', '07_exact_insertion')
cd('Footnote vérifier que', r'\deleted{\unsure{vérifier que}}', r'\deleted{vérifier que}',
   'The accented é, dotted i cells, tall f and q descender can be followed through the strokes.', 'high', '17_verifier_reference')
cd('Final cancelled D\'ailleurs', r"\unsure{D'ailleurs}", r"\unsure{D'ailleurs}",
   'Several covered initial cells remain uncertain; late letter contours support the proposed word.', 'low', '21_final_dailleurs')
cd('Final reference subdivision', r'1.2.\unsure{(ii)|(iii)|(i)}', 'Retain all three supplied candidates.',
   'The added cancelled group has visible narrow stems but the dense crossing prevents a secure stem count.', 'low', '22_final_index')
cd('Run-together marker boundary', ').Comme', ').Comme retained.',
   'A baseline point is visible between the closing parenthesis and C, with no typed space cell.', 'high', '06_body_reference_star')
cd('Agreement est muni', 'est muni', 'Retain muni, without a final e.',
   'Half b has a final dotted i followed by the blank before des.', 'high', bbox=[337,1348,609,1398])
cd('Singular celle', 'telles que celle de', 'Retain singular celle.',
   'Half b shows e then the gap before de; no s occupies that gap.', 'high', bbox=[1110,1565,1494,1607])
cd('des ensembles déduits', 'des ensembles déduits', 'Retain as read; no correction needed.',
   'Halves a and b show des followed by ensembles, and déduits with its final ts.', 'high', bbox=[1231,1001,1683,1050])
cd('Body right edge', 'se définis', 'Retain the visible fragment only.',
   'Half b ends in the s contour at the right image boundary; no unseen continuation is supplied.', 'high', bbox=[1474,1772,1683,1824])
cd('Footnote after droite', '(resp. à droite si', 'Do not add a closing parenthesis after droite.',
   'Half b has droite at the image edge and si on the next physical line; a closing parenthesis is not visible.', 'high', bbox=[1372,1935,1683,1992])
cd('Own page number in prior C notes', '22', r'\unsure{2|7}2',
   'The first numeral has a rounded upper stroke but an abbreviated base; 7 cannot be securely excluded.', 'medium', '01_page_number')

inventory = []
def inv(element, kind, position, first, hand='typescript with pen corrections'):
    inventory.append(dict(sheet_kind='cancelled_draft', hand=hand, element=element,
        kind=kind, position=position, first_words_or_objects=first, transcribed='yes'))

inventory_rows = [
 ('Own page number','text',[917,29,977,75],'2|7 followed by 2','handwritten; hand not independently identified'),
 ('Archive number','margin note',[1564,24,1639,83],'27, inverted; comment only','archive handwriting'),
 ('Opening continuation paragraph','text',[272,154,1683,344],'un morphisme de topos','typescript with pen fills'),
 ('Opening morphism arrow','text',[788,171,838,197],'u: E → E\'','handwritten arrow in typed formula'),
 ('Opening upper functor star','text',[1128,222,1158,248],'u^*','handwritten star'),
 ('Opening lower functor star','text',[1331,248,1360,279],'u_*','handwritten star'),
 ('Opening added reference','insertion',[1561,293,1666,340],'(3.2.1)','handwritten'),
 ('Opening reference older digit','deletion',[1575,296,1605,333],'2|3 below final 3','overlapping pen digits'),
 ('Section number and exactness exposition','text',[271,365,1683,764],'3.1.2. Si u:E → E\'','typescript with pen corrections'),
 ('Section older first digit','deletion',[265,367,298,407],'2 below 3','typed digit with pen correction'),
 ('Section final first digit','insertion',[266,367,298,407],'3','handwritten'),
 ('Section morphism arrow','text',[563,381,608,405],'u:E → E\'','handwritten arrow'),
 ('Adjunction reference','insertion',[690,402,824,437],'(I 2.11)','handwritten'),
 ('Adjunction reference leader','drawing',[707,416,851,484],'single curved leader before que','pen'),
 ('Direct image formula','text',[1301,444,1504,490],'u_*:E → E\'','typed letters; pen star and arrow'),
 ('Inverse image formula','text',[1052,505,1277,552],"u^*:E' → E",'typed letters; pen star and arrow'),
 ('Cancelled reference after inductives','deletion',[490,581,563,621],'(2.11)|(I 2.11)','handwritten crossed reference'),
 ('Body footnote marker','insertion',[570,563,612,621],'(*)','handwritten'),
 ('Two lower prongs inside body marker','drawing',[585,577,601,602],'two short lower strokes below star','pen; function uncertain'),
 ('Cancelled left marginal reference','margin note',[110,576,239,636],'(I 2.11)|(I 4.11), followed by a live point','handwritten cancellation'),
 ('Exactness insertion','insertion',[1275,543,1609,580],'est exact à gauche i.e.','handwritten'),
 ('Exactness insertion leader','drawing',[1378,562,1610,622],'curve before commute with upturned right end','pen'),
 ('Detached point at exactness leader','drawing',[1590,550,1606,568],'one detached point','ink or surface mark uncertain'),
 ('u-star in exactness conclusion','text',[1448,646,1502,683],'u^*','typed u and pen star'),
 ('Underline beneath est','drawing',[1494,679,1581,694],'est','pen'),
 ('Cancelled edge fragment exac','deletion',[1583,651,1683,691],'exac','typewriter x cancellation'),
 ('Underline beneath exact','drawing',[278,746,385,766],'exact','pen'),
 ('Raised On peut donc dire que','insertion',[376,688,815,725],'On peut donc dire que','typewritten addition'),
 ('On peut insertion leader','drawing',[395,706,848,783],'curve before c\'est and upturned right terminal','pen'),
 ('Initial C corrected to c','deletion',[413,721,445,755],'C with pen c','typed C and pen c'),
 ('Cancelled donc','deletion',[533,721,616,758],'donc','typewriter x cancellation'),
 ('First image-inverse assertion underline','drawing',[413,752,1129,767],"c'est donc le foncteur image inverse",'pen'),
 ('Image-inverse assertion star','text',[1136,712,1188,753],'u^*','typed u and pen star'),
 ('Cancelled first qui','deletion',[1195,722,1264,759],'qui, with live following comma','typewriter x cancellation'),
 ('Pair of image functors','text',[277,784,437,829],'(u_*,u^*)','typed letters and pen stars'),
 ('Second assertion underline','drawing',[453,819,1664,839],"qui possède les propriétés d'exactitude les plus remarquables",'pen'),
 ('Cancelled assurant','deletion',[277,863,443,901],'assurant','typewriter x cancellation'),
 ('Structure preservation exposition','text',[276,861,1683,1336],'Ces propriétés assurent que','typescript with pen additions'),
 ('Raised Sigma','insertion',[488,895,555,939],'Sigma','handwritten'),
 ('Sigma leader','drawing',[476,918,594,983],'curve before cancelled qui','pen'),
 ('Faint short arc under Sigma','drawing',[495,930,532,945],'one short arc','ink or surface trace uncertain'),
 ('Cancelled qui and peut','deletion',[493,940,662,978],'qui peut','typewriter x cancellation'),
 ('Extra cancellation x between qui and peut','drawing',[551,940,582,975],'standalone x in blank cell','typewriter'),
 ('et pour addition','insertion',[1111,1109,1210,1146],'et pour','handwritten'),
 ('et pour leader','drawing',[1138,1110,1246,1190],'curve before tout','pen'),
 ('Opening object quotation','insertion',[1253,1138,1287,1175],'two opening quotation strokes','handwritten'),
 ('Underlined E in object phrase','text',[1444,1145,1495,1193],"underlined E'",'typed E and prime, low pen rule'),
 ('Second Sigma and closing quotation','text',[769,1210,832,1256],'Sigma followed by two closing strokes','handwritten Sigma; typed quotation'),
 ('Cancelled de before internes','deletion',[533,1291,577,1324],'de','typewriter x cancellation'),
 ('E-prime after topos','text',[939,1290,981,1330],"definite E' with extra heavy lower material",'typed letter; lower material of uncertain medium'),
 ('Heavy extra material below E','drawing',[940,1309,975,1331],'lower bar and right lower projection','second impression or pen reinforcement uncertain'),
 ('Cancelled inverse','deletion',[1413,1282,1568,1333],'inverse','pen cancellation'),
 ('Inverse-image star before est muni','text',[279,1342,324,1392],'u^*','typed u and pen star'),
 ('Formal hesitation and reader advice','text',[275,1354,1683,1613],"est muni ... Plutôt que d'entrer",'typescript with raised typed addition'),
 ('l\'expliciter et de addition','insertion',[1196,1461,1564,1503],"l'expliciter et de",'typewritten addition'),
 ('l\'expliciter insertion leader','drawing',[1241,1482,1587,1540],'curve before se with long upper horizontal part','pen'),
 ('Three detached points beneath pour','drawing',[593,1601,610,1629],'three points descending left','dark points; function uncertain'),
 ('Examples','text',[277,1570,1651,1756],'telles que celle de groupe','typescript'),
 ('Cancelled ou de bimodule','deletion',[1350,1636,1641,1686],'ou de bimodule','typewriter x cancellation'),
 ('Extra cancellation x after ou','drawing',[1394,1644,1423,1681],'x in blank separator cell','typewriter'),
 ('Extra cancellation x after de','drawing',[1451,1643,1482,1681],'x in blank separator cell','typewriter'),
 ('Unfinished final body sentence','text',[278,1778,1683,1828],'(Dans ces exemples ... se définis','typescript'),
 ('Footnote separator','drawing',[78,1823,1655,1857],'one long wavy horizontal rule','pen'),
 ('Footnote body','text',[276,1850,1683,2126],'(*) On peut D\'ailleurs ...','typescript with pen revisions'),
 ('Footer star','text',[303,1861,333,1895],'* between typed parentheses','handwritten star'),
 ('Cancelled On peut','deletion',[369,1868,521,1916],'On peut','pen cancellation of typed words'),
 ('d corrected to D','deletion',[529,1854,570,1912],'d inside capital D','typed d, pen D'),
 ('Cancelled vérifier que','deletion',[733,1877,985,1921],'vérifier que','pen cancellation of typed words'),
 ('Raised footer reference','insertion',[744,1843,937,1886],'(1.5 et 1.8)','handwritten'),
 ('Footer reference leader','drawing',[724,1853,967,1925],'curve before vérifier with high right end','pen'),
 ('Footer direct-image formula','text',[1331,1875,1537,1918],"u_*:E → E'",'typed letters, pen star and arrow'),
 ('Footer inverse-image formula','text',[275,1930,479,1980],"u^*:E' → E",'typed letters, pen star and arrow'),
 ('d corrected to c in ce','deletion',[628,1938,660,1981],'d with c-shaped overstroke','typed d and handwritten correction'),
 ('Raised U-','insertion',[908,1982,959,2018],'underlined U-','typewritten addition'),
 ('Raised U leader','drawing',[932,1985,1005,2054],'curve before limites','pen'),
 ('Second U-','text',[1540,2014,1603,2054],'underlined U-','typewritten U and hyphen; separate low rule'),
 ('Final cancelled sentence','deletion',[579,2054,1683,2125],"D'ailleurs, c'est une conséquence immédiate de 1.2.(ii|iii|i)",'typed words with pen cancellation'),
 ('Extra tail below final cancelled D\'ailleurs','drawing',[744,2080,777,2110],'faint down-right tail','pen or surface trace uncertain'),
 ('Long vertical cancellation upper component','deletion',[795,237,862,1864],'long slightly bowed path through body','pen'),
 ('First detached cancellation point near 1.5','drawing',[793,1866,801,1871],'point','pen'),
 ('Second detached cancellation point near 1.5','drawing',[792,1871,800,1876],'point','pen'),
 ('Short cancellation segment near 1.5','drawing',[791,1875,799,1881],'short descending segment','pen'),
 ('Continuing lower cancellation component','deletion',[719,1881,800,2125],'continuing descending path through footnote','pen'),
]
for row in inventory_rows:
    inv(*row)

remaining_doubts = [
 dict(place='Own page number', reading=r'\unsure{2|7}2', alternatives=['22','72'], confidence='medium'),
 dict(place='Opening reference older digit', reading=r'\deleted{\unsure{2|3}}3.2.1', alternatives=['older 2','older 3'], confidence='low'),
 dict(place='Cancelled marginal reference', reading=r'\unsure{(I 2.11)|(I 4.11)}', alternatives=['(I 2.11)','(I 4.11)'], confidence='low'),
 dict(place='Cancelled body reference', reading=r'\unsure{(2.11)|(I 2.11)}', alternatives=['(2.11)','(I 2.11)'], confidence='low'),
 dict(place='Extra strokes below the body footnote star', reading='Definite star plus two drawn lower prongs', alternatives=['additional pen trace','overlapping earlier mark'], confidence='low'),
 dict(place='Inserted exact', reading=r'\unsure{exact}', alternatives=['exact; central letters not fully resolved'], confidence='medium'),
 dict(place='Point above exactness insertion leader', reading='One drawn point', alternatives=['pen point','surface mark'], confidence='low'),
 dict(place='Faint arc below Sigma', reading='One drawn faint short arc', alternatives=['pen tail','surface trace'], confidence='low'),
 dict(place='Heavy lower material in E-prime after topos', reading='Definite E and prime plus uncertain drawn lower reinforcement', alternatives=['second E impression','pen reinforcement'], confidence='medium'),
 dict(place='Three points below pour', reading='Three drawn points', alternatives=['ink points of unestablished function','incidental marks'], confidence='medium'),
 dict(place='Final cancelled D\'ailleurs', reading=r"\unsure{D'ailleurs}", alternatives=["D'ailleurs; initial covered cells unresolved"], confidence='low'),
 dict(place='Comma after final cancelled D\'ailleurs', reading=r'\unsure{,}', alternatives=['comma','portion of cancellation'], confidence='low'),
 dict(place='Down-right tail below final cancelled D\'ailleurs', reading='One separately drawn faint tail', alternatives=['pen cancellation tail','surface trace'], confidence='low'),
 dict(place='Final reference subdivision', reading=r'\unsure{(ii)|(iii)|(i)}', alternatives=['(ii)','(iii)','(i)'], confidence='low'),
]

report = dict(
 page='C123-02_123_scan028', reader='R1',
 viewed=dict(whole=source, a=source.replace('.jpg','_a.jpg'), b=source.replace('.jpg','_b.jpg')),
 reading_file='out/readers/C123-02_123_scan028/R1/reading.tex',
 differences=differences, c_doubts=c_doubts, inventory=inventory,
 remaining_doubts=remaining_doubts,
 notes=[
  'This is a cancelled typescript with handwritten corrections. The visible section is 3.1.2 after revision of its first digit. Its own page number is read as 22 with a local first-digit 2|7 doubt; an inverted archive 27 is recorded only as a comment. No date, title sheet, or total page count is visible.',
  'The opening continuation describes a morphism of topoi as unique up to unique isomorphism in terms of the inverse or direct image functor. The section states preservation of projective limits by u_*, inductive limits by u^*, and finite projective limits by u^*.',
  'The structure passage discusses operations given by finite projective limits and arbitrary inductive limits and lists groups, rings, modules, comodules, bialgebras and torsors. The examples retain the source singular celle and the agreement est muni.',
  'The source explicitly says “Plutôt que d\'entrer dans la tâche peu engageante de donner un sens précis à cet énoncé et de le justifier de façon formelle”. It recommends that the reader “l\'expliciter et de se convaincre de sa validité”; the first words are a raised typed insertion. This is a stated avoidance of a formal justification here, not a proof supplied on this sheet.',
  'The footer\'s vérifier que is visibly cancelled and replaced by the raised reference (1.5 et 1.8). The final sentence beginning D\'ailleurs is also cancelled. Neither cancelled phrase is a surviving instruction to this reader.',
  'The body ends at the visible fragment définis. The footer\'s right-edge parenthesis after droite is not visible. No ending or parenthesis has been supplied from grammar.',
  'H is chiefly an editorial summary with four additions transcribed. The omission rows identify source text and graphic states absent from that witness; H\'s descriptive editorial prose is not itself treated as manuscript text.',
  'All additions, cancellation cells, separate leaders, the two lower star prongs, faint Sigma arc, detached point, three-point cluster and footer tail have an actual TeX/TikZ representation. The long cancellation is drawn with two main paths, two detached points and one short intervening segment; its exact rendered alignment has not been compiled or tested.',
 ],
 notation=[
  dict(place='Ordinary functor and topos letters', form='typed u, E and E-prime', reading=r'\mathrm{u},\mathrm{E},\mathrm{E}\prime', evidence='Single ordinary typewriter contours in the opening, section and footer formula groups; pen stars and arrows are kept distinct.'),
  dict(place='Object phrase', form='E with detached lower rule', reading=r'\underline{\mathrm{E}}\prime', evidence='Single E contour, separate low rule and high right prime.'),
  dict(place='After topos', form='E with heavy lower material', reading='Definite E plus separately drawn uncertain lower reinforcement', evidence='The upper E shape and prime are secure; a second full same-letter impression is not separable.'),
  dict(place='Both U-limit expressions', form='ordinary typed U with independent underline', reading=r'\underline{\mathrm{U}}', evidence='Both local crops show slab-serif machine U; the first is raised and the second is on the body baseline.'),
  dict(place='Structure species', form='handwritten zigzag capital', reading=r'\Sigma', evidence='The raised first occurrence and later inline occurrence have top and bottom bars joined by the characteristic zigzag.'),
  dict(place='All morphism arrows', form='rightward pen shafts with right heads', reading=r'\longrightarrow', evidence='Opening, section, direct/inverse-image statements and footer were read separately in the halves; none points left.'),
  dict(place='Functor indices', form='upper and lower pen stars', reading=r'\mathrm{u}^{*},\mathrm{u}_{*}', evidence='The u-star inverse-image occurrences are raised; direct-image stars are below the baseline. The body footnote star has two additional lower traces and is drawn separately.'),
  dict(place='Cancellation blank cells', form='standalone typed x', reading=r'\texttt{x}', evidence='One x between qui and peut; two between ou, de and bimodule. They are cancellation impressions, not source words.'),
 ],
 abbreviations=[
  dict(form='resp.', expansion='respectivement (editorial expansion; not inserted in the transcription)'),
  dict(form='i.e.', expansion='id est (editorial expansion; not inserted in the transcription)'),
 ],
 math_checks=[
  dict(check='Adjunction directions and preservation statements', performed=True,
       method='Used the written directions u^*:E-prime to E and u_*:E to E-prime with u^* left adjoint to u_*. For a diagram B_i in E, Hom_E-prime(A,u_*(lim B_i)) is identified successively with Hom_E(u^*A,lim B_i), lim Hom_E(u^*A,B_i), and lim Hom_E-prime(A,u_*B_i); the dual Hom calculation gives preservation of colimits by u^*.',
       result='The two preservation directions on the page agree with this targeted adjunction calculation. No glyph was changed to obtain the agreement.',
       limits='This does not prove the manuscript\'s broader assertion about all species of structures or the converse adjoint-existence claim in the footer.'),
  dict(check='Scope of the i.e. insertion', performed=True,
       method='Compared the added “est exact à gauche i.e.” with the following finite-projective-limit phrase and then checked the local pen curve and cancellation state in crop 07.',
       result='The following typed commute phrase remains locally live; the insertion supplies a reformulation. H\'s assertion that the addition replaces the words is not supported by a local strike.',
       limits='This is a logical and ink-state check, not a verification of a theorem about exact functors.'),
  dict(check='Footnote converse and references', performed=False,
       result='Read only. The referred sections 1.5 and 1.8 are outside this assigned page and were not consulted; their hypotheses and the converse theorem were not verified.'),
 ],
 crop_count=len(manifest),
 workflow_feedback='Whole page viewed once, then a and b once each line by line, including witness agreements. Original dimensions 1683 x 2140; each half 1683 x 1150, with b beginning at whole-image y=990. Twenty-two unresolved loci were cropped once with the required crop.py and viewed once. No OCR, text recognition, web, other-page images, other readers, root decisions, compilation, or repeated image views were used. Complete reading.tex was saved before this report. The heavy E and cancelled final reference remain deliberately unresolved rather than being repaired from mathematical expectation.'
)
(out/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
(out/'crop_manifest.jsonl').write_text((out/'crops/crop_manifest.jsonl').read_text())
print(json.dumps(dict(saved=str(out/'report.json'), differences=len(differences), inventory=len(inventory), c_doubts=len(c_doubts), crops=len(manifest))))
