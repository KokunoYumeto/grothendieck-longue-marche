import json
from pathlib import Path

ROOT = Path('/workspace/scratch/8f839dff4bf0')
WORK = ROOT / 'SP74_C13_143+145_work'
packet = json.loads((ROOT / 'reader_packets/143_scan033.json').read_text())
C, H = packet['witness_C'], packet['witness_H']
candidate = (WORK / 'reviews/143_scan033_readerA.tex').read_text()

crop_specs = {
    'top_left_object': ([800,295,1120,425],2600,0),
    'top_right_object': ([1180,295,1510,430],2600,0),
    'upper_middle_row': ([865,415,1690,510],3200,0),
    'upper_lower_row': ([1170,570,2155,770],3200,0),
    'lower_left_deleted': ([720,885,1130,1065],3000,0),
    'lower_right_pi': ([1220,880,1710,1045],2800,0),
    'lower_T_plus': ([970,1040,1340,1160],2600,0),
    'lower_Autlac': ([1345,1030,1805,1145],2800,0),
    'lower_T': ([1110,1220,1570,1355],2800,0),
    'lower_Autext': ([1570,1205,2080,1315],3000,0),
    'gamma_double_link': ([1870,1110,2035,1220],2400,0),
    'word_brace': ([1860,1315,2110,1390],2600,0),
    'left_bottom_notes': ([350,1260,675,1545],2600,0),
    'bottom_sigma': ([1520,1540,2200,1875],3200,0),
    'ibm_strip': ([105,35,146,2210],3200,90),
    'upper_top_exit': ([1490,325,1670,380],2600,0),
    'upper_middle_entry': ([720,435,865,495],2600,0),
    'upper_middle_exit': ([1700,425,1935,495],2600,0),
    'upper_bottom_entry': ([990,590,1160,655],2600,0),
    'lower_middle_exit': ([1815,1035,2045,1120],2600,0),
    'lower_bottom_exit': ([2055,1220,2300,1315],2600,0),
}

def crop_ref(name):
    if name == 'page':
        return 'page', None
    return f'crops/143_scan033_A_{name}.png', crop_specs[name][0]

changes = []
def settled_case(s):
    return s.replace(r'\unsure{\Pi|\pi}',r'\pi').replace(r'\Pi_{g,\nu}(X)|\Pi_1(X)',r'\pi_{g,\nu}(X)|\pi_1(X)')

def change(place, c, h, final, ac, ah, kind, ink, confidence='high', crop='page', marked=False, consequential=False):
    assert c in C, (place, 'C', c)
    assert h == '[no witness]' or h in H, (place, 'H', h)
    if place.endswith(': group-letter case'):
        return
    final=settled_case(final)
    assert final in candidate, (place, 'final', final)
    cr, box = crop_ref(crop)
    changes.append(dict(place=place,C=c,H=h,final=final,against_C=ac,against_H=ah,
        kind=kind,ink=ink,confidence=confidence,crop=cr,box=box,
        marked_in_H=marked,consequential=consequential))

ibm = C[C.index(r'\margin{\begin{tabular}{c}'):C.index(r'\diagram{')].rstrip()
change('Printed left edge: 31 IBM logos',ibm,'[no witness]',ibm,False,True,'omission',
       'The strip has 31 separate printed IBM logos; each was counted in the original strip, with the rotation retained only in the review crop.',crop='ibm_strip')

for n in (1,2):
    change(f'Upper diagram: auxiliary top 1 number {n}, descending link',r'1 \arrow[dr,dash]',r'1 \arrow[dr]',r'1 \arrow[dr,dash]',False,True,
           'drawing or diagram','The oblique shaft reaches toward the object below without a separate triangular or barbed endpoint. No head is supplied from the diagram pattern.',consequential=True)

change('Upper diagram, first X: low index',r'\overline X_{\unsure{g|\xi}}',r'\overline{X}_\xi',r'\overline X_{\unsure{g|\xi}}',False,True,
       'misread symbol or index','The low graph has an open upper e/g-like turn and a long curved descender. These strokes leave g and xi locally unresolved; the preferred g is provisional.',
       'low','top_left_object',consequential=True)
change('Upper diagram, second X: low index',r'\overline X_{\unsure{j|\xi}}',r'\overline{X}_\xi',r'\overline X_{\unsure{j|\xi}}',False,True,
       'misread symbol or index','A separate undotted stem turns at its top and hooks below the X. The j-like outline is preferred, with xi retained because the small graph does not uniquely identify the letter.',
       'low','top_right_object',consequential=True)
change('Upper diagram, second X: separator before S',r'\overline X_{\unsure{j|\xi}}-S_\nu',r'\overline{X}_\xi \smallsetminus S_\nu',
       r'\overline X_{\unsure{j|\xi}}\unsure{-}S_\nu',False,True,'misread symbol or index',
       'Only a pale horizontal trace, with tiny dark ends, appears between the low X index and S. There is no blue diagonal set-minus stroke like that in the first object. The trace may be non-textual; a doubtful dash preserves the open locus.',
       'low','top_right_object',consequential=True)

pi_nodes = [
 ('Upper diagram, first top object',r'\pi_1(\overline X_{\unsure{g|\xi}}\setminus S_\nu)',r'\pi_1(\overline{X}_\xi \smallsetminus S_\nu)',r'\unsure{\Pi|\pi}_1(\overline X_{\unsure{g|\xi}}\setminus S_\nu)','top_left_object','The broad cap and two comparatively upright legs support capital Pi, but the turned right foot leaves lowercase pi possible.'),
 ('Upper diagram, second top object',r'\pi_1(\overline X_{\unsure{j|\xi}}-S_\nu)',r'\pi_1(\overline{X}_\xi \smallsetminus S_\nu)',r'\unsure{\Pi|\pi}_1(\overline X_{\unsure{j|\xi}}\unsure{-}S_\nu)','top_right_object','The group graph has a wide horizontal cap and long, almost straight legs; this is locally capital-like, with a short curved return still admitting pi.'),
 ('Upper diagram, middle barred M object',r'\pi_1(\overline M_{g,\nu+1})',r'\pi_1(\overline{M}_{g,\nu+1})',r'\unsure{\Pi|\pi}_1(\overline M_{g,\nu+1})','upper_middle_row','The cap spans both stems. The stems are tall relative to the nearby low 1, although a handwritten pi cannot be excluded.'),
 ('Upper diagram, middle unbarred M object',r'\pi_1(M_{g,\nu+1})',r'\pi_1(M_{g,\nu+1})',r'\unsure{\Pi|\pi}_1(M_{g,\nu+1})','upper_middle_row','A broad cap joins two near-vertical stems; the ends are not sufficiently diagnostic to settle the alphabet.'),
 ('Upper diagram, bottom barred M object',r'\pi_1(\overline M_{g,\nu})',r'\pi_1(\overline{M}_{g,\nu})',r'\unsure{\Pi|\pi}_1(\overline M_{g,\nu})','upper_lower_row','The two-legged graph is broad and capital-sized; the end turn also permits a cursive pi.'),
 ('Upper diagram, bottom unbarred M object',r'\pi_1(M_{g,\nu})',r'\pi_1(M_{g,\nu})',r'\unsure{\Pi|\pi}_1(M_{g,\nu})','upper_lower_row','The cap and largely upright pair of legs resemble the capital-like graphs earlier in this diagram. The case remains locally uncertain.'),
]
for place,c,h,f,cr,ink in pi_nodes:
    change(place+': group-letter case',c,h,f,True,True,'misread symbol or index',ink+' This row concerns alphabet encoding only; all physical indices are recorded separately.',
           'medium',cr,consequential=False)

change('Upper diagram: second top object to right 1',r'\pi_1(\overline X_{\unsure{j|\xi}}-S_\nu) \arrow[r,dash]',
       r'\pi_1(\overline{X}_\xi \smallsetminus S_\nu) \arrow[rr]',
       r'\unsure{\Pi|\pi}_1(\overline X_{\unsure{j|\xi}}\unsure{-}S_\nu) \arrow[r]',True,False,'drawing or diagram',
       'The right endpoint has a separate raised triangular shoulder attached to the shaft, with a pointed rightward edge. It is more than a rounded pen stop.',
       'medium','upper_top_exit',consequential=True)
change('Upper diagram: middle left 1 to barred M object',r'\&1 \arrow[r,dash] \& \pi_1(\overline M_{g,\nu+1})',
       r'& 1 \arrow[r] & \pi_1(\overline{M}_{g,\nu+1})',
       r'\&1 \arrow[r] \& \unsure{\Pi|\pi}_1(\overline M_{g,\nu+1})',True,False,'drawing or diagram',
       'The long horizontal stroke ends in an upstanding filled triangular head. The detached spot beside the numeral is not given a mathematical role.',
       'medium','upper_middle_entry',consequential=True)
change('Upper diagram: middle unbarred M object to Gamma',r'\pi_1(M_{g,\nu+1}) \arrow[r,dash]',r'\pi_1(M_{g,\nu+1}) \arrow[rr]',
       r'\unsure{\Pi|\pi}_1(M_{g,\nu+1}) \arrow[r]',True,False,'drawing or diagram',
       'The shaft ends with a small upturned triangular shoulder, unlike the genuinely bare diagonal shafts above.',
       'medium','upper_middle_row',consequential=True)
change('Upper diagram: middle Gamma to right 1, direction',r'\Gamma \arrow[r,dash] \arrow[dr]',r'\Gamma \arrow[r] \arrow[dr]',
       r'\Gamma \arrow[r,phantom,"{\unsure{\longleftarrow|\longrightarrow}}" description] \arrow[dr]',True,True,'drawing or diagram',
       'The strongest acute/barbed end is at the LEFT. The right end is blunt, with a small downward interior bump before it. A left arrow is preferred from the visible end, but direction remains doubtful; neither exactness nor the surrounding arrows decides it.',
       'low','upper_middle_exit',consequential=True)
change('Upper diagram: bottom left 1 to barred M object',r'\&\&1 \arrow[r,dash] \& \pi_1(\overline M_{g,\nu})',
       r'& & 1 \arrow[r] & \pi_1(\overline{M}_{g,\nu})',
       r'\&\&1 \arrow[r] \& \unsure{\Pi|\pi}_1(\overline M_{g,\nu})',True,False,'drawing or diagram',
       'The right end is a distinct filled triangular point; the left end has a short downward hook. The rightward head is retained without turning the left hook into another labelled decoration.',
       'high','upper_bottom_entry',consequential=True)
change('Upper diagram: bottom barred M object to unbarred M object',r'\pi_1(\overline M_{g,\nu}) \arrow[r,dash]',r'\pi_1(\overline{M}_{g,\nu}) \arrow[rr]',
       r'\unsure{\Pi|\pi}_1(\overline M_{g,\nu}) \arrow[r]',True,False,'drawing or diagram',
       'A small filled triangular projection rises from the right endpoint; the stroke is not an undecorated bar.',
       'medium','upper_lower_row',consequential=True)
change('Upper diagram: bottom unbarred M object down to 1',r'\pi_1(M_{g,\nu}) \arrow[r] \arrow[dr,Rightarrow]',
       r'\pi_1(M_{g,\nu}) \arrow[rr] \arrow[dr]',
       r'\unsure{\Pi|\pi}_1(M_{g,\nu}) \arrow[r] \arrow[dr,Rightarrow]',False,True,'drawing or diagram',
       'Two separate diagonal shafts descend toward the terminal 1, with projections at their lower end. A single-shaft arrow drops visible ink.',
       'high','upper_lower_row',consequential=True)
change('Upper diagram: bottom Gamma to right 1',r'\Gamma \arrow[r,dash] \arrow[dr,Rightarrow]',r'\Gamma \arrow[r] \arrow[dr]',
       r'\Gamma \arrow[r,phantom,"{\unsure{\longrightarrow|\relbar}}" description] \arrow[dr,Rightarrow]',True,False,'drawing or diagram',
       'The right endpoint has a fat, slightly pointed shoulder. A small head is preferred, but its rounded outline does not exclude a bare stopping stroke; the alternative remains in place.',
       'low','upper_lower_row',consequential=True)
change('Upper diagram: bottom Gamma down to terminal 1',r'\Gamma \arrow[r,dash] \arrow[dr,Rightarrow]',r'\Gamma \arrow[r] \arrow[dr]',
       r'\arrow[dr,Rightarrow]',False,True,'drawing or diagram',
       'The diagonal connection consists of two diverging shafts, one ending in a clear head. The doubled drawing is retained rather than H\'s single arrow.',
       'medium','upper_lower_row',consequential=True)

change('Lower diagram: first auxiliary top 1, descending link',r'1 \arrow[dr,dash] \&1 \arrow[dr]',r'1 \arrow[dr] & & 1 \arrow[dr]',
       r'1 \arrow[dr,dash] \&1 \arrow[dr]',False,True,'drawing or diagram',
       'The first auxiliary diagonal is a simple shaft without an isolated endpoint head; the adjacent second auxiliary diagonal does have a head.',consequential=True)

for place,cr,ink in [
    ('Lower diagram, first top hatted group','lower_left_deleted','The live top graph has a broad cap and two long legs beneath a separate hat. The long low stroke underneath belongs to the cancelled material, not to a gamma-like live index.'),
    ('Lower diagram, second top hatted group','lower_right_pi','A separate hat sits over the two-legged, broad-capped group graph. Its legs are comparatively upright.'),
    ('Lower diagram, Autlac argument','lower_Autlac','The argument has a distinct hat above a broad two-legged graph, whose cap is wider and legs straighter than an unambiguous compact pi.'),
    ('Lower diagram, Autextlac argument','lower_Autext','The hatted argument has a broad cap; the lower ends curve outward more than those above. Capital Pi remains preferred only provisionally.'),
]:
    change(place+': group-letter case',r'\widehat\pi_{g,\nu}',r'\widehat{\pi}_{g,\nu}',r'\widehat{\unsure{\Pi|\pi}}_{g,\nu}',
           True,True,'misread symbol or index',ink+' Case alone is encoded here, with medium confidence and no consequential mathematical-correction claim.',
           'medium',cr,consequential=False)

change('Lower diagram: cancelled earlier line below first hatted group',r'\deleted{\unsure{\pi_{g,\nu}}}',r'\pi_1(\overline{X}) \ldots',
       r'\deleted{\unsure{1}\mathbin{-}\unsure{\Pi_{g,\nu}(X)|\Pi_1(X)}}',True,True,'deletion state',
       'Beneath the live group is a cancelled line: a short 1-like upright at the left, a long crossing/wavy connecting stroke, a Pi-like graph, and a large X with parenthesis-like strokes. The old low index is obscured (g,nu versus 1); a separate overbar on X is not secure. C leaves out the X and the incoming fragment; H records an uncertain editorial reconstruction rather than the visible fragment in the diagram.',
       'low','lower_left_deleted',marked=True,consequential=True)
change('Lower diagram: top right 1 down to middle Gamma',r'\&1 \arrow[dr,dash]',r'1 \arrow[dr]',r'\&1 \arrow[dr,dash]',False,True,
       'drawing or diagram','The oblique link is a single plain shaft. No separate head is visible at the Gamma end.',crop='lower_right_pi',consequential=True)
change('Lower diagram: middle left 1 to hatted T with nu+1',r'\&1 \arrow[r,dash] \& \widehat{\mathcal T}_{g,\nu+1}',
       r'& 1 \arrow[r] & \widehat{\mathcal{T}}_{g,\nu+1}',r'\&1 \arrow[r] \& \widehat{\mathcal T}_{g,\nu+1}',True,False,
       'drawing or diagram','There is a separate small triangular arrowhead at the end before the hatted T.',crop='lower_T_plus',consequential=True)
change('Lower diagram: Autlac baseline',r'\operatorname{Autlac}^{\circ}',r'\mathrm{Aut}_{\mathrm{lac}}^{\circ}',r'\operatorname{Autlac}^{\circ}',
       False,True,'insertion or placement','The letters A-u-t-l-a-c run on one baseline. The l-a-c letters do not descend to the argument-index level; the circle is a separate raised mark.',crop='lower_Autlac')
change('Lower diagram: middle Gamma to right 1',r'\Gamma \arrow[r,dash] \arrow[dr,Rightarrow]',r'\Gamma \arrow[r] \arrow[dr, no head, "=" description]',
       r'\Gamma \arrow[r] \arrow[dr,phantom',True,False,'drawing or diagram',
       'The right endpoint has distinct upper and lower wings outside the thickness of the shaft, converging at a narrow rightward point.',
       'medium','lower_middle_exit',consequential=True)
double_link = r'\begin{tikzpicture}[x=.65cm,y=.65cm,line cap=round,baseline=-.15cm]\draw (0,.58)--(.68,-.10);\draw (-.14,.38)--(.49,-.25);\draw (.22,.36)--(.13,.49);\draw (.09,.15)--(.22,.17);\end{tikzpicture}'
change('Lower diagram: diagonal link between the two Gamma terms',r'\arrow[dr,Rightarrow]',r'\arrow[dr, no head, "=" description]',double_link,
       True,True,'drawing or diagram','There are two parallel oblique strokes, one shorter than the other. Their far ends are blunt. Each has a small interior projection, rather than a shared terminal arrowhead. A small literal drawing retains those shafts and projections; neither a conventional double arrow nor a single shaft with an equality label reproduces them.',
       'high','gamma_double_link',marked=True,consequential=True)
change('Lower diagram: Autextlac baseline',r'\operatorname{Autextlac}^{\circ}',r'\mathrm{Autext}_{\mathrm{lac}}^{\circ}',r'\operatorname{Autextlac}^{\circ}',
       False,True,'insertion or placement','All letters A-u-t-e-x-t-l-a-c stand on one baseline. The separate small ring lies above the operator before the opening parenthesis.',crop='lower_Autext')
change('Lower diagram: word under the last operator-to-Gamma link',r'\text{\unsure{traces|tresses}}',r'\uncertain{tresses}',r'\text{traces}',False,True,
       'misread word','After t-r there is a closed a-like bowl followed by an open c, then e and a rising final s. This supports traces rather than tresses. The joining strokes follow a curved baseline.',
       'medium','word_brace',marked=True,consequential=True)
change('Lower diagram: attachment of traces',r'\begin{gathered}\operatorname{Autextlac}^{\circ}(\widehat\pi_{g,\nu})^{!}\\\text{\unsure{traces|tresses}}\end{gathered} \arrow[r]',
       r'\mathrm{Autext}_{\mathrm{lac}}^{\circ}(\widehat{\pi}_{g,\nu})^{!} \to \Gamma',
       r'''\operatorname{Autextlac}^{\circ}(\widehat{\unsure{\Pi|\pi}}_{g,\nu})^{!} \arrow[r,"{\text{traces}}"']''',True,False,'insertion or placement',
       'The word begins under the right-hand part of the operator/link span and continues toward Gamma, rather than sitting centered below the full operator. It is placed under that rightward link.',
       'high','word_brace',marked=True)
change('Lower diagram: no independent brace beneath traces',r'\text{\unsure{traces|tresses}}',"un mot souligné d'une accolade",r'\text{traces}',False,True,
       'drawing or diagram','The apparent lower curve is formed by the connected letter strokes themselves. No distinct second stroke below the word forms an underbrace or an underline.',
       'medium','word_brace',marked=True)
change('Lower diagram: bottom Gamma to right 1',r'\&\Gamma \arrow[r,dash]',r'\Gamma \arrow[r] & 1 \quad \Sigma_\nu',r'\&\Gamma \arrow[r,dash]',False,True,
       'drawing or diagram','The horizontal shaft has a slightly downward, rounded stop at the right. It has neither upper/lower head wings nor a sharp terminal projection.',crop='lower_bottom_exit',consequential=True)

change('Lower-left first formula: argument K',r"M'_{g,\nu}(K)",r"M'_{g,\nu}(k)",r"M'_{g,\nu}(K)",False,True,'misread symbol or index',
       'The argument is a full-height vertical with two diagonal branches, comparable in height to M and not the low k form.',crop='left_bottom_notes',consequential=True)
change('Lower-left formulas: physical two-line arrangement',r"M'_{g,\nu}(K)\ni\xi\\"+'\n'+r"\mathcal T'_{g,\nu}\ni G_\xi",
       r"M'_{g,\nu}(k) \ni \xi, \qquad \mathcal{T}'_{g,\nu} \ni G_\xi",
       r"M'_{g,\nu}(K)\ni\xi\\"+'\n'+r"\mathcal T'_{g,\nu}\ni G_\xi",False,True,'insertion or placement',
       'The M-prime membership formula is on the upper line; the T-prime membership formula is separately below it.',crop='left_bottom_notes')
change('Lower-left first formula: no comma after xi',r'(K)\ni\xi',r'(k) \ni \xi,',r'(K)\ni\xi',False,True,'text not on the page',
       'After the long-tailed xi the line ends; there is no separate comma stroke at the baseline.',crop='left_bottom_notes')
change('Bottom Sigma group: cancelled earlier graph and low g',r'\deleted{\unsure{\Gamma|\Sigma}}',
       'le premier terme est précédé et surmonté de signes raturés, illisibles',r'\deleted{\unsure{\Gamma_g|\Sigma_g}}',True,True,'deletion state',
       'Above-left of the live hatted Sigma is a crossed cap/angled graph. Its alphabet remains Gamma/Sigma, but a separate low loop with a descending return is visible to its lower right and reads g. C omits that low index; H leaves the cancelled material untranscribed.',
       'medium','bottom_sigma',marked=True,consequential=True)
change('Bottom Sigma group: cancelled graph above-left, not on the live baseline',r'\deleted{\unsure{\Gamma|\Sigma}}\ \widehat\Sigma_{g,\nu}^{\sim}',
       'le premier terme est précédé et surmonté de signes raturés, illisibles',
       r'\deleted{\unsure{\Gamma_g|\Sigma_g}}&&\\'+'\n'+r'&\widehat\Sigma_{g,\nu}^{\sim}&\Sigma_{g,\nu}',True,False,'insertion or placement',
       'The cancelled graph is visibly above and to the left of the live hatted Sigma. A separate array row preserves that relative position.',crop='bottom_sigma',marked=True)
change('Bottom Sigma group: separate hat and upper-right wavy mark',r'\widehat\Sigma_{g,\nu}^{\sim}',r'\widehat{\widetilde{\Sigma}}_{g,\nu}',r'\widehat\Sigma_{g,\nu}^{\sim}',False,True,
       'misread symbol or index','A retraced angular hat lies directly above Sigma. The small wavy mark is separately to the upper RIGHT of that symbol, not nested between its hat and cap.',crop='bottom_sigma',consequential=True)
change('Bottom Sigma group: vertical equality arrangement',r'\Vert&&\\'+'\n'+r'\overline\Sigma_{g,\nu}',
       r'\widehat{\widetilde{\Sigma}}_{g,\nu} = \overline{\Sigma}_{g,\nu}',r'&\Vert&\\'+'\n'+r'&\overline\Sigma_{g,\nu}&',False,True,
       'insertion or placement','Two short vertical strokes stand below the hatted Sigma and above the barred Sigma. H\'s note recognizes this placement, but its displayed equation makes it horizontal.',crop='bottom_sigma',marked=True)
change('Printed lower-left sequence',r'\margin{\begin{tabular}{c}6\\5\\4\\3\\2\\1\\0\end{tabular}}','[no witness]',
       r'\margin{\begin{tabular}{c}6\\5\\4\\3\\2\\1\\0\end{tabular}}',False,True,'omission',
       'The printed sequence reads 6, 5, 4, 3, 2, 1, 0 down the lower-left edge; all seven digits are retained.')
change('Printed lower-right code',r'\margin{2975 -- 132}','[no witness]',r'\margin{2975 -- 132}',False,True,'omission',
       'The small printed vertical code reads 2975 followed by one dash and 132; the two TeX hyphens encode that single printed dash.')
change('Pencil lower-left pagination',r'\mspage{32}','[no witness]',r'\mspage{32}',False,True,'omission',
       'A separate pale pencil 32 is written near the lower-left edge. Its hand is unnamed; the page supplies no identifying evidence.')

decisions = [
    dict(id='M0748',decision='undecided',reading=r'\unsure{g|\xi}',
         ink='The low first-X index has an open upper turn and long curved descender. Neither a complete closed g bowl nor an independently diagnostic xi zigzag is secured.',
         crop=crop_ref('top_left_object')[0],box=crop_specs['top_left_object'][0],confidence='low'),
    dict(id='M0749',decision='undecided',reading=r'\unsure{j|\xi}',
         ink='The second low index is a separate undotted stem with top turn and lower hook. Its j-like silhouette is preferred, but the small-form xi alternative remains.',
         crop=crop_ref('top_right_object')[0],box=crop_specs['top_right_object'][0],confidence='low'),
    dict(id='M0750',decision='first',reading='traces',
         ink='The word has t-r, a closed a-like bowl, an open c, e, and final rising s. The pen connections are not a separate underline or brace.',
         crop=crop_ref('word_brace')[0],box=crop_specs['word_brace'][0],confidence='medium'),
]

inventory = []
def inv(element,kind,position,first,hand='main blue-ink hand'):
    first=settled_case(first)
    inventory.append(dict(sheet_kind='handwritten diagrams on landscape printed listing sheet',hand=hand,
                          element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('E01','margin note','left printed strip, x105–146, full sheet height','31 separate IBM logos','printed')
inv('E02','diagram','upper sheet, approximately x600–2160, y190–770','Two auxiliary 1s; three staggered object rows; three terminal 1s; 19 objects and 22 links')
inv('E03','diagram','middle/lower sheet, approximately x740–2540, y780–1460','Two auxiliary 1s; three staggered object rows; two terminal 1s; two detached far-right Sigma labels; 20 objects and 21 links')
inv('E04','deletion','beneath first live hatted group in lower diagram, x720–1130, y965–1050',r'\deleted{\unsure{1}\mathbin{-}\unsure{\Pi_{g,\nu}(X)|\Pi_1(X)}}')
inv('E05','drawing','lower diagram, diagonal Gamma-to-Gamma link, x1870–2035, y1110–1220','Two blunt parallel shafts with separate interior projections')
inv('E06','text','under rightward Autextlac-to-Gamma span, x1860–2110, y1315–1390','traces')
inv('E07','margin note','far right of lower diagram, upper of the two labels',r'\Sigma_{\nu+1}; detached from the row and without a connecting arrow')
inv('E08','margin note','far right of lower diagram, lower of the two labels',r'\Sigma_\nu; detached from the row and without a connecting arrow')
inv('E09','display','lower-left, first of two short formula lines, x350–675, y1260–1405',r"M'_{g,\nu}(K)\ni\xi")
inv('E10','display','lower-left, second short formula line, x350–675, y1395–1545',r"\mathcal T'_{g,\nu}\ni G_\xi")
inv('E11','diagram','bottom middle, x1520–2200, y1540–1875',r'\widehat\Sigma_{g,\nu}^{\sim} above \Vert above \overline\Sigma_{g,\nu}; a separate \Sigma_{g,\nu} at the right')
inv('E12','deletion','above-left of the live hatted Sigma in the bottom group',r'\deleted{\unsure{\Gamma_g|\Sigma_g}}')
inv('E13','margin note','lower-left printed edge','6, 5, 4, 3, 2, 1, 0, vertically arranged','printed')
inv('E14','margin note','lower-right printed edge, vertical orientation','2975 – 132','printed')
inv('E15','margin note','near lower-left edge','32','unnamed pencil hand')

remaining = []
def doubt(place,reading,alternatives,reason,crop,confidence='low'):
    if place.endswith(': case'):
        return
    reading=settled_case(reading)
    cr, box = crop_ref(crop)
    remaining.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason,crop=cr,box=box))
doubt('Upper diagram: first X index',r'\unsure{g|\xi}','g / xi','Open upper turn and long descender do not uniquely identify the low graph.','top_left_object')
doubt('Upper diagram: second X index',r'\unsure{j|\xi}','j / xi','Undotted hooked stem is j-like, but the xi alternative is not eliminated.','top_right_object')
doubt('Upper diagram: second-object separator',r'\unsure{-}','horizontal dash / no textual character; H diagonal set-minus not supported',
      'The trace is much paler than the nearby blue writing and may be print, show-through or an erased stroke. No secure diagonal separator exists.','top_right_object')
for place,c,h,f,cr,ink in pi_nodes:
    doubt(place+': case',r'\unsure{\Pi|\pi}_1','capital Pi / lowercase pi',ink,cr,'medium')
for place,cr in [('Lower diagram: first top group','lower_left_deleted'),('Lower diagram: second top group','lower_right_pi'),
                 ('Lower diagram: Autlac argument','lower_Autlac'),('Lower diagram: Autextlac argument','lower_Autext')]:
    doubt(place+': case',r'\widehat{\unsure{\Pi|\pi}}_{g,\nu}','hatted capital Pi / hatted lowercase pi',
          'The broad cap and long legs are capital-like, but the cursive foot shape does not settle alphabet case.',cr,'medium')
doubt('Upper diagram: middle Gamma–1 direction',r'\unsure{\longleftarrow|\longrightarrow}','left / right head',
      'The left end has the strongest acute wing, while the right end has an interior bump and a blunt stop. Direction is not inferred from the row.','upper_middle_exit')
doubt('Upper diagram: bottom Gamma–1 endpoint',r'\unsure{\longrightarrow|\relbar}','small right head / bare horizontal shaft',
      'The terminal shoulder is fat and slightly pointed but not as clearly separated as the neighboring heads.','upper_lower_row')
doubt('Lower diagram: cancelled line below first group',r'\deleted{\unsure{1}\mathbin{-}\unsure{\Pi_{g,\nu}(X)|\Pi_1(X)}}',
      'Left 1-like fragment; old low g,nu versus 1; parenthesis/X reading is partial; no secure separate overbar',
      'Cancellation and overlap with the live low index obscure the older expression. X and the incoming fragment survive, so neither is omitted.','lower_left_deleted')
doubt('Bottom group: cancelled graph',r'\deleted{\unsure{\Gamma_g|\Sigma_g}}','Gamma_g / Sigma_g',
      'A crossing passes through the cap and angled body. The small low g-like loop/descender survives, but the principal letter remains uncertain.','bottom_sigma')

certainty_resolutions = [
    dict(place='Upper diagram: bar above second X',C=r'\overline X_{\unsure{j|\xi}}',final=r'\overline X_{\unsure{j|\xi}}',
         H=r"\note{le trait sur le second $X_\xi$ de la première ligne n'est pas sûr}",
         ink='A separate shallow curved horizontal stroke lies above the second plain crossed X. It is distinct from the cap of the preceding group graph.',
         crop=crop_ref('top_right_object')[0],box=crop_specs['top_right_object'][0]),
    dict(place='Lower diagram: C doubt traces/tresses',C=r'\unsure{traces|tresses}',final='traces',
         ink='The closed third-letter bowl and open following c support the first reading. The differing H word has its own material row.',
         crop=crop_ref('word_brace')[0],box=crop_specs['word_brace'][0]),
    dict(place='Upper diagram: certainty of C horizontal separator',C=r'-S_\nu',final=r'\unsure{-}S_\nu',
         ink='C\'s horizontal interpretation is retained only provisionally because the trace is paler than the blue writing. The differing H diagonal is separately collated.',
         crop=crop_ref('top_right_object')[0],box=crop_specs['top_right_object'][0]),
]

physical_indices = []
def idx(place,mark,position,ink,crop,confidence='high'):
    cr,box=crop_ref(crop)
    physical_indices.append(dict(place=place,mark=mark,position=position,ink=ink,crop=cr,box=box,confidence=confidence))

for label,cr,xindex in [('Upper first X object','top_left_object',r'\unsure{g|\xi}'),('Upper second X object','top_right_object',r'\unsure{j|\xi}')]:
    idx(label,r'_1','low, immediately after the two-legged group graph','One small upright digit sits below the group-letter baseline. It is not part of the following parenthesis.',cr)
    idx(label,r'\overline X','above the X','A separate upper stroke lies over the plain diagonal-crossed X; it is not a looped mathfrak X.',cr)
    idx(label,xindex,'low, right of X','A separately lowered tailed graph remains uncertain; it is not a full-height argument.',cr,'low')
    idx(label,r'S_\nu','low, right of S','The small nu lies at the foot of the S; the preceding S and its low index are separate strokes.',cr)

for label,cr,bar,plus in [('Upper middle barred M','upper_middle_row',True,True),('Upper middle unbarred M','upper_middle_row',False,True),
                         ('Upper bottom barred M','upper_lower_row',True,False),('Upper bottom unbarred M','upper_lower_row',False,False)]:
    idx(label,r'_1','low, after the group graph','A small single upright stands at the lower right of the group letter, before the opening parenthesis.',cr)
    idx(label,'bar above M' if bar else 'unbarred M','above the main M','A distinct horizontal upper stroke is present.' if bar else 'The space above M has no separate bar; its own upper strokes belong to the letter.',cr)
    idx(label,'g','first low component after M','The initial low component has a small loop/turn and descending stroke; it is separate from M.',cr)
    idx(label,',','low separator after g','A short comma separates the low g and nu components.',cr)
    idx(label,r'\nu','second low component after M','The low nu is a small angled/curving graph to the right of the comma.',cr)
    if plus:
        idx(label,'+','same low level as nu','A short cross follows nu; both its horizontal and upright strokes are present.',cr)
        idx(label,'1','after the low plus','A single small upright follows the plus, with no extra index added above it.',cr)

for label,cr in [('Lower first top hatted group','lower_left_deleted'),('Lower second top hatted group','lower_right_pi'),
                 ('Autlac argument','lower_Autlac'),('Autextlac argument','lower_Autext')]:
    idx(label,'hat','above the group graph','A separate angular upper mark lies above the broad cap of the two-legged letter.',cr)
    idx(label,'g','first low index','A low turned/looped graph with descender follows the group letter. Its position is below, not above, the baseline.',cr)
    idx(label,',','between the low g and nu','The small separating stroke occurs on the low-index line; in the second top group it is close to the adjacent writing.',cr,'medium')
    idx(label,r'\nu','second low index','A small angled nu sits to the right of the comma. In the first group its low vicinity overlaps the cancelled older X, whose long stroke is not a gamma tail on this index.',cr)

for label,cr,plus in [('Lower middle hatted T','lower_T_plus',True),('Lower bottom hatted T','lower_T',False)]:
    idx(label,'hat','above T','The angular hat is separate from the curled top of the modular T.',cr)
    idx(label,'g','first low component','The first subscript is a small g-like loop and descender.',cr)
    idx(label,',','low separator','A short comma occurs between the two lowered letters.',cr)
    idx(label,r'\nu','second low component','The nu sits below-right of T, not beside it on the main baseline.',cr)
    if plus:
        idx(label,'+','low continuation after nu','The plus has a vertical and a horizontal crossing stroke at the index level.',cr)
        idx(label,'1','low after plus','One upright digit follows the plus.',cr)

for label,cr in [('Autlac','lower_Autlac'),('Autextlac','lower_Autext')]:
    idx(label,r'\circ','raised after the operator, before the opening parenthesis','The mark is a small closed ring, not a numerical zero on the baseline.',cr)
    idx(label,'!','raised after the closing parenthesis','A short raised upright has a separate dot below it. It is an exclamation mark, not a prime.',cr)
    idx(label,'lac','on the operator baseline','The l-a-c letters align with the preceding letters; they are not a subscript.',cr)
idx('Far-right upper Sigma',r'\nu','low, right of Sigma','A low nu follows the angular Sigma.','page')
idx('Far-right upper Sigma','+','same low line after nu','A plus cross is visible after the low nu.','page')
idx('Far-right upper Sigma','1','low after plus','A single upright digit follows the low plus.','page')
idx('Far-right lower Sigma',r'\nu','low, right of Sigma','The lower detached Sigma has a low nu alone, without plus or digit.','page')

for label in ["M' membership line","T' membership line"]:
    idx(label,"'",'raised after the initial letter','A separate short high slash follows the letter; it is not the upper end of the low g.','left_bottom_notes')
    idx(label,'g','first low component','A small loop with a descender is physically low and right of the initial letter.','left_bottom_notes')
    idx(label,',','low separator','A short comma separates g from nu.','left_bottom_notes')
    idx(label,r'\nu','second low component','A small nu follows the comma on the same low line.','left_bottom_notes')
idx("M' membership line",'K','full-height parenthesized argument','The K has a full-height upright and two separate diagonal arms.','left_bottom_notes')
idx("M' membership line",r'\xi','baseline after membership sign','The xi has a strongly angular multi-turn outline and long tail. There is no detached final comma.','left_bottom_notes')
idx("T' membership line",r'G_\xi','xi low, at the right foot of G','The large looped G has an inner return; the xi is a separate low tailed graph.','left_bottom_notes')

for label in ['Bottom live hatted Sigma','Bottom live barred Sigma','Bottom separate plain Sigma']:
    idx(label,'g','first low component','A distinct lowered g-like loop and descender follows the main angular Sigma.','bottom_sigma')
    idx(label,',','low separator','A short comma separates the two subscript components.','bottom_sigma')
    idx(label,r'\nu','second low component','The nu is on the low-index line, separately to the right of the comma.','bottom_sigma')
idx('Bottom live hatted Sigma','hat','directly above Sigma','The heavily retraced upper mark is angular and remains a live hat; it is distinct from the cancelled graph above-left.','bottom_sigma')
idx('Bottom live hatted Sigma',r'\sim','upper right of Sigma','The short wavy stroke is to the right of the hat, not between the hat and the main graph.','bottom_sigma')
idx('Bottom live barred Sigma','bar','directly above lower Sigma','A separate horizontal overbar sits above the lower Sigma.','bottom_sigma')
idx('Bottom cancelled graph','g','low to the right of the crossed main graph','A small loop followed by a lower return remains outside the strongest crossing stroke.','bottom_sigma','medium')
idx('Lower cancelled line','old index','low after the older Pi-like graph','The crossing and overlapping live material do not securely distinguish g,nu from 1; both are retained.','lower_left_deleted','low')

diagram_edges = []
def edge(diagram,start,end,shape,ink,crop='page',label=None,confidence='high'):
    cr,box=crop_ref(crop)
    diagram_edges.append(dict(diagram=diagram,start=start,end=end,shape=shape,label=label,ink=ink,crop=cr,box=box,confidence=confidence))
# Upper diagram, all twenty-two physical links, each inspected at both ends.
edge('upper','auxiliary first 1','first top object','bare diagonal','Single oblique shaft, without a separate endpoint head.')
edge('upper','auxiliary second 1','second top object','bare diagonal','Single oblique shaft, without the head visible on neighboring descending arrows.')
edge('upper','top left 1','first top object','right arrow','The right endpoint has a triangular head.')
edge('upper','first top object','second top object','right arrow','One horizontal shaft ends in a rightward head.','top_left_object')
edge('upper','second top object','top right 1','right arrow','A raised triangular shoulder is attached at the right endpoint.','upper_top_exit',confidence='medium')
edge('upper','first top object','middle barred M','down-right arrow','Single diagonal shaft with a lower-right head.')
edge('upper','second top object','middle unbarred M','down-right arrow','Single diagonal shaft ends at the lower-right object with a head.')
edge('upper','top right 1','middle Gamma','down-right arrow','The oblique stroke has a separate head before Gamma.')
edge('upper','middle left 1','middle barred M','right arrow','The endpoint has a filled upstanding triangular projection.','upper_middle_entry',confidence='medium')
edge('upper','middle barred M','middle unbarred M','right arrow','A single shaft and pointed right head are visible.','upper_middle_row')
edge('upper','middle unbarred M','middle Gamma','right arrow','The right end has a small upturned triangular shoulder.','upper_middle_row',confidence='medium')
edge('upper','middle Gamma','middle right 1','uncertain left/right arrow','The left end is the more visibly acute one; the right end is blunt with an interior downward bump.','upper_middle_exit',confidence='low')
edge('upper','middle barred M','bottom barred M','down-right arrow','The diagonal single shaft ends in a head.')
edge('upper','middle unbarred M','bottom unbarred M','down-right arrow','The diagonal single shaft has a lower-right head.')
edge('upper','middle Gamma','bottom Gamma','down-right arrow','The oblique single shaft has a terminal head.')
edge('upper','bottom left 1','bottom barred M','right arrow','The left end hooks down; the right endpoint is a distinct filled triangular point.','upper_bottom_entry')
edge('upper','bottom barred M','bottom unbarred M','right arrow','A small filled upper projection forms the right endpoint head.','upper_lower_row',confidence='medium')
edge('upper','bottom unbarred M','bottom Gamma','right arrow','The horizontal shaft ends with a distinct rightward head.','upper_lower_row')
edge('upper','bottom Gamma','bottom right 1','uncertain right arrow/bare shaft','The ending has a fat shoulder, but the separation of a head from the stopping stroke is not secure.','upper_lower_row',confidence='low')
edge('upper','bottom barred M','first terminal 1','single down-right arrow','One diagonal shaft ends in a head before the terminal 1.','upper_lower_row')
edge('upper','bottom unbarred M','second terminal 1','double down-right arrow','Two shafts, with lower-end head/projection strokes, are separately visible.','upper_lower_row')
edge('upper','bottom Gamma','third terminal 1','double down-right arrow','Two diverging shafts descend, one with a distinctly headed lower end.','upper_lower_row',confidence='medium')
# Lower diagram, all twenty-one physical links.
edge('lower','auxiliary first 1','first top hatted group','bare diagonal','The shaft has no separated terminal head.')
edge('lower','auxiliary second 1','second top hatted group','down-right arrow','A head is visible at the lower end.')
edge('lower','top left 1','first top hatted group','right arrow','A rightward head occurs at the end before the group.','lower_left_deleted')
edge('lower','first top hatted group','second top hatted group','right arrow','One rightward head and a separate wavy label above the shaft.','lower_left_deleted',label=r'\sim')
edge('lower','second top hatted group','top right 1','right arrow','The end is pointed; a retraced loop along the shaft is not a second written label.','lower_right_pi')
edge('lower','first top hatted group','middle hatted T','down-right arrow','The diagonal descends through the vicinity of the cancelled line and has its own lower head.','lower_left_deleted')
edge('lower','second top hatted group','Autlac','down-right arrow','A single diagonal shaft terminates in a head.','lower_right_pi')
edge('lower','top right 1','middle Gamma','bare diagonal','The oblique link lacks a separated head.','lower_right_pi')
edge('lower','middle left 1','middle hatted T','right arrow','A small triangular head is visible.','lower_T_plus')
edge('lower','middle hatted T','Autlac','right arrow','The horizontal shaft has a rightward terminal head.')
edge('lower','Autlac','middle Gamma','right arrow','One shaft ends in a rightward head.','lower_Autlac')
edge('lower','middle Gamma','middle right 1','right arrow','The endpoint has upper and lower wings extending beyond the shaft thickness.','lower_middle_exit',confidence='medium')
edge('lower','middle hatted T','bottom hatted T','down-right arrow','One diagonal arrow has a visible lower-right head.')
edge('lower','Autlac','Autextlac','down-right arrow','One diagonal shaft ends with a head before the lower operator.')
edge('lower','middle Gamma','bottom Gamma','two blunt diagonal shafts with interior projections','Two parallel strokes of different lengths, each with an interior projection; no shared endpoint head.','gamma_double_link')
edge('lower','bottom left 1','bottom hatted T','right arrow','The rightward head is separated from the shaft.','lower_T')
edge('lower','bottom hatted T','Autextlac','right arrow','The horizontal stroke ends with a rightward head.')
edge('lower','Autextlac','bottom Gamma','right arrow','A rightward head is visible; traces is written below the rightward span.','lower_Autext',label='traces')
edge('lower','bottom Gamma','bottom right 1','bare horizontal','The right stop is rounded and slightly downturned, without head wings.','lower_bottom_exit')
edge('lower','bottom hatted T','first terminal 1','down-right arrow','A single diagonal descends to a headed end before 1.')
edge('lower','Autextlac','second terminal 1','down-right arrow','A single diagonal shaft ends with a head before 1.')

raw_notes = [
 ('material','31 IBM logos retained; H listing-layout note is editorial, not manuscript prose.'),
 ('markup only','Ampersand replacement changes syntax, not the displayed objects.'),
 ('markup only','Column separation setting alone does not alter the source reading.'),
 ('markup only','Scriptsize node style is a font choice.'),
 ('material','First upper auxiliary link is bare.'),
 ('material','Second upper auxiliary link is bare.'),
 ('material','First X low g/xi remains locally doubtful, preferred g.'),
 ('markup only','r/rr compensates for H\'s extra empty grid cells.'),
 ('material','Second X low j/xi remains locally doubtful, preferred j.'),
 ('material','Second separator is a very pale horizontal trace, not a secured diagonal.'),
 ('material','Top object-to-1 has a small triangular right head.'),
 ('material','Middle left entry has a raised triangular head.'),
 ('markup only','Same middle barred-to-unbarred map, r/rr grid syntax.'),
 ('material','Middle unbarred M-to-Gamma has a small right head.'),
 ('material','Middle Gamma–1 has locally doubtful direction; left end is more strongly barbed.'),
 ('material','Bottom left entry has a rightward triangular head.'),
 ('material','Bottom barred-to-unbarred map has a small right head.'),
 ('markup plus material','Bottom unbarred M-to-Gamma is a right arrow; its separate doubled diagonal is recorded independently.'),
 ('material','Both bottom descending doubled links retained; bottom Gamma exit remains head/bar doubtful.'),
 ('certainty only','Second X overbar is visible as a distinct shallow upper stroke; H note is not source text.'),
 ('markup only','Second diagram ampersand replacement.'),
 ('markup only','Second diagram column separation.'),
 ('markup only','Second diagram font setting.'),
 ('material','Lower first auxiliary diagonal is bare.'),
 ('markup plus material','Gathered syntax alone is excluded; cancelled fragment beneath the node is retained and enlarged from visible ink.'),
 ('material','Cancelled Pi-like fragment includes X and incoming strokes; old index remains doubtful.'),
 ('markup only','r/rr on the top isomorphism reflects grid spacing; the single sim above it is confirmed.'),
 ('markup only','r/rr on the second top group-to-1 link reflects grid spacing.'),
 ('material','Top right 1-to-Gamma diagonal is bare.'),
 ('material','Middle left entry to hatted T has a head.'),
 ('markup only','Middle T-to-Autlac map is the same arrow in either grid.'),
 ('material','Autlac letters share one baseline, not subscript lac.'),
 ('markup only','Autlac-to-Gamma r/rr grid difference.'),
 ('material','Middle Gamma exit has distinct head wings.'),
 ('material','The Gamma-to-Gamma link is drawn literally as two blunt shafts with internal projections.'),
 ('markup only','Bottom T-to-Autextlac r/rr grid difference.'),
 ('material','Autextlac letters share one baseline. Gathered placement of the word is separately corrected.'),
 ('material plus certainty','The word reads traces; its preferred C reading is settled and differing H word is collated.'),
 ('markup plus material','Arrow grid span excluded; traces is placed below the rightward link, not centered under the full operator.'),
 ('material','Bottom Gamma exit is a bare horizontal shaft.'),
 ('editorial plus material','H narrative is not source prose. Its reported deletion, word, alleged brace, Gamma link, and detached Sigma labels were individually checked and inventoried.'),
 ('material','Two lower-left lines remain vertically separate; gathered syntax itself is excluded.'),
 ('material','No comma follows xi; the two formulas are on separate lines. Uppercase K is also checked independently of the normalized raw diff.'),
 ('markup only','Closing gathered command has no independent source content.'),
 ('material','Cancelled bottom graph is above-left and includes a visible low g; alphabet unresolved.'),
 ('material','Hat and separate upper-right wavy mark retained; equality remains physically vertical.'),
 ('material plus editorial','Printed numbers, printed footer and pencil 32 retained. H bottom-layout note is editorial; the actual layout is typeset.'),
]
assert len(raw_notes)==len(packet['differences'])==47
raw_checks=[dict(index=i+1,words_before=d['words before'],C=d['witness C'],H=d['witness H'],
                 disposition=raw_notes[i][0],result=raw_notes[i][1]) for i,d in enumerate(packet['differences'])]

report = dict(
    key='143_scan033',reader='A',stage='first',
    image_views=['original','half1','half2']+[crop_ref(n)[0] for n in crop_specs],
    changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining,
    certainty_resolutions=certainty_resolutions,
    notation=[
        dict(form=r'\pi_1; \widehat{\pi}_{g,\nu}',meaning='The same group-letter notation is encoded consistently as pi.',evidence='All six upper group graphs and all four lower live group graphs were inspected individually. They share wide flat caps and mostly upright legs, with more curved feet in the final argument. No distinct local capital-Pi exemplar or functional Pi/pi contrast was found. The initial alternatives rested on those non-diagnostic cap/leg traits alone. Main reported already-viewed 029–031 pi_1 exemplars with the same flat-crossbar hand and the same group notation; that communicated comparison supports settling pi consistently without another image view.'),
        dict(form=r'X',meaning='Plain crossed X in the two top objects.',evidence='Both are composed of diagonal crossing strokes, not the looped capital described by the shared mathfrak-X entry. Each separate bar is retained.'),
        dict(form=r'S_\nu',meaning='The removed-set label in the two top objects.',evidence='Two S-shaped letters, one more looped than the other, each with low nu. No cross-page image comparison or forced alphabet choice was made here.'),
        dict(form=r'\widehat{\mathcal T}_{g,\nu+1}, \widehat{\mathcal T}_{g,\nu}, \mathcal T\prime',meaning='Modular T notation, retained under current shared notation.',evidence='Each local T has a curled/flagged cap and descending return. This is not converted to the earlier object-set tau alternative.'),
        dict(form=r'\Sigma',meaning='Angular Sigma in the two detached right labels and three live bottom symbols.',evidence='The angular caps and diagonal bodies are distinct from the rounded extension/action-group E/Sigma uncertainty. All five live occurrences were inspected.'),
        dict(form=r'\operatorname{Autlac}, \operatorname{Autextlac}',meaning='Operator names exactly on one baseline.',evidence='The lac letters stand with the preceding operator letters, while circles and final exclamation marks are separately raised.'),
        dict(form=r'\widehat\Sigma_{g,\nu}^{\sim}',meaning='Physical hat plus separate upper-right wavy mark.',evidence='The wave sits to the right, not under the hat; the heavy retracing does not delete the live hat.'),
    ],
    abbreviations=[],
    hand_log=[
        dict(habit='Small filled triangular shoulders can form an arrowhead even when the head is short relative to the shaft.',places='Upper top exit; upper middle entry; upper middle M-to-Gamma; upper bottom entry; upper bottom barred-to-unbarred map; lower middle entry and Gamma exit.',scope='Each endpoint inspected individually; the bare lower final exit is kept distinct, and two upper endpoints remain uncertain.',misreadings='Several C dash edges have a small head; H conversely supplies heads on genuinely bare diagonals and the lower final exit.'),
        dict(habit='The pi hand can have a broad flat cap and two nearly straight legs.',places='Six upper group symbols and four lower live hatted group symbols.',scope='All ten live occurrences checked separately; no same-page Pi/pi contrast was demonstrated. The final argument has more curved feet but remains within the same notation.',misreadings='The initial proposed capital-Pi alternatives treated flat caps and straight legs as more diagnostic than the local evidence justified. Main\'s communicated comparison with its already-inspected 029–031 group exemplars supports the witnesses\' consistent pi encoding.'),
        dict(habit='A small descender beneath a live symbol can belong to a cancelled earlier line.',places='First lower hatted group and cancelled X immediately below it.',scope='One local overlap only.',misreadings='Do not turn the live low nu into gamma by joining it to the cancelled X or connecting stroke.'),
        dict(habit='The l-a-c ending is written at the operator baseline.',places='Lower middle Autlac and lower bottom Autextlac.',scope='Both occurrences confirmed.',misreadings='H subscript lac is a placement error.'),
        dict(habit='The exclamation exponent consists of a short upright and a detached point.',places='After the closing parenthesis in both lower operators.',scope='Both inspected individually.',misreadings='Neither occurrence is a prime; both witness exclamation readings are confirmed.'),
        dict(habit='The joined lower strokes of a word can resemble an underbrace.',places='traces under the Autextlac-to-Gamma span.',scope='One word; no independent brace below it.',misreadings='H describes an accolade that is not separated from the word strokes.'),
        dict(habit='A separate superscript wave can be mistaken for a nested tilde accent.',places='Bottom hatted Sigma.',scope='One occurrence, with the hat, wave and low indices separately inventoried.',misreadings='H widehat-widetilde encoding moves the wave from its upper-right position.'),
    ],
    notes=[
        dict(id='143_scan033-N1',text='This landscape listing sheet contains two staggered diagrams. The upper diagram places two X-minus-S-type group expressions over barred and unbarred M expressions, with Gamma and terminal 1 labels. The transcription records their drawn links without inferring exactness or repairing direction from algebra.'),
        dict(id='143_scan033-N2',text='The lower diagram has hatted group symbols, hatted modular T labels, and the written operators Autlac and Autextlac with circle and exclamation marks. Its far-right Sigma labels are detached. The word below the last horizontal span is read traces; no independent brace is supplied.'),
        dict(id='143_scan033-N3',text='The two lower-left membership formulas are on separate lines. The first has uppercase K, and the second ends with G carrying low xi. The bottom middle group has hatted Sigma with a separate upper-right wave, a vertically oriented equality to barred Sigma below, and a separate plain Sigma on the right.'),
        dict(id='143_scan033-N4',text='The cancelled lower-diagram line retains a partial incoming fragment and X, with its older index unresolved. The cancelled predecessor above-left of the bottom live Sigma retains a low g. These are partial readings of struck ink, not reconstructions supplied from the mathematical setting.'),
        dict(id='143_scan033-N5',text='Printed IBM logos, the printed 6-to-0 edge sequence, footer 2975 – 132, and pencil 32 are retained. The pencil hand is unnamed. Pale mirrored listing characters showing through are not text on this face; the detached small spot beside the upper middle leading 1 is treated as an incidental point without a syntactic role and is not transcribed.'),
        dict(id='143_scan033-N6',text='This first-pass work establishes transcription candidates only. No mathematical assertion was proved, re-proved, or computed. The common group notation and main\'s communicated already-inspected graphic comparison were used to settle the ten non-contrastive live group graphs as pi; no new image was opened for that decision. A mathematical expectation was not used to repair a clearly contrary letter or arrow.'),
        dict(id='143_scan033-N7',text='The initial ten Pi/pi alternatives reflected wide caps and relatively straight legs, not ten independent source distinctions. The page offers no separate clear capital-Pi comparator. Main identified the same flat-crossbar pi hand in already-inspected group examples on029–031 and the same pi_1 / genus-puncture group notation here. The candidate therefore adopts pi consistently; the local shape observations remain in physical_indices and this report rather than multiplying alphabet doubts.'),
    ],
    check_events=[dict(statement_id='143_scan033-group-letter-notation',type='carried as background without fault found',outcome='The identification of the upper labels as pi_1 groups and the lower hatted genus/puncture labels as the same group notation was used only to choose between graphically non-distinguished alphabet renderings, together with main\'s communicated prior graphic comparison. No group-theoretic statement was proved or independently verified.')],
    unresolved_for_main=[dict(place=d['place'],reading=d['reading'],crop=d['crop'],box=d['box']) for d in remaining],
    raw_difference_disposition='All 47 packet raw differences were inspected against the original, native halves and the one crop for each unresolved locus. Material readings are recorded in changes; pure grid/macro/font differences are excluded. H editorial notes are not source prose, but every described deletion, brace, detached label and orientation was checked. Agreements were checked as well, producing a full physical-index/edge inventory. The normalized raw diff missed uppercase K, which is explicitly collated. The ten live pi graphs were checked individually but show no local alphabet contrast; consistent pi is retained after main\'s communicated existing graphic comparison, so there are no alphabet-change rows for them.',
    raw_difference_checks=raw_checks,
    physical_indices=physical_indices,
    diagram_edges=diagram_edges,
    workflow=dict(original_view_count=1,native_half_view_counts=[1,1],other_page_images_or_packets_opened=False,
                  crop_method='Each box is a distinct unresolved locus, cropped from the original; Pillow LANCZOS scaling, autocontrast and sharpening; no OCR or recognition.',
                  crops=[dict(name=n,path=crop_ref(n)[0],box=s[0],width=s[1],rotation_degrees=s[2],viewed=True) for n,s in crop_specs.items()],
                  failed_emission='An attempted three-image emission of upper_top_exit, upper_middle_entry and upper_middle_exit returned only a context-truncation notice. Each existing crop was then emitted singly and actually viewed; no crop was regenerated.',
                  tex_compiled=False,external_research=False,proof_checks_performed=False),
)

assert [d['id'] for d in decisions] == [d['id'] for d in packet['marks']]
assert len(diagram_edges)==43
assert sum(e['diagram']=='upper' for e in diagram_edges)==22
assert sum(e['diagram']=='lower' for e in diagram_edges)==21
assert all((WORK/v).exists() for v in report['image_views'] if v.startswith('crops/'))
assert candidate.count('IBM')==31
assert candidate.count(r'\unsure{\Pi|\pi}')==0
assert candidate.count(r'\widehat{\pi}_{g,\nu}')==4
assert all(d['reading'] in candidate for d in decisions)
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(c['kind'] in allowed for c in changes)
dest=WORK/'reviews/143_scan033_readerA.json'
dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(report=str(dest),candidate=str(WORK/'reviews/143_scan033_readerA.tex'),changes=len(changes),decisions=len(decisions),inventory=len(inventory),remaining_doubts=len(remaining),physical_index_entries=len(physical_indices),diagram_edges=len(diagram_edges),raw_differences=len(raw_checks)),ensure_ascii=False))

