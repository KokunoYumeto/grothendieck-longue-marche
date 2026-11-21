from pathlib import Path
import csv
import json

OUT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan035')
PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan035')
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
F = (OUT / 'candidate.tex').read_text()
BOXES = json.loads((OUT / 'crop_boxes.json').read_text())
changes = []

def between(s, start, end, include_end=False):
    i = s.index(start)
    j = s.index(end, i)
    return s[i:j + (len(end) if include_end else 0)]

def change(place, c, h, final, ink, crop, confidence='high', kind='misread word', against_c=False, against_h=True, math=False):
    assert not c or c in C, ('C snippet', place, c)
    assert not h or h in H, ('H snippet', place, h)
    changes.append(dict(place=place, c=c, h=h, final=final, ink=ink,
                        crop=f'crops/148_scan035_{crop}.png', box=BOXES[crop],
                        confidence=confidence, kind=kind,
                        against_c=against_c, against_h=against_h, math=math))

change('circled_case_4', r'\textcircled{4}', '(4)', r'\textcircled{4}',
       'A continuous curved enclosure surrounds the angular 4; these are not two separate parentheses.',
       'heading_case', kind='misread symbol or index')
change('canceled_opening_clause', r'\deleted{Il y a \unsure{deux cas}}', r'\struck{Il y a deux \ill{}}',
       r'\deleted{Il y a \unsure{deux cas}}',
       'Il y a is plain beneath the horizontal cancellation. The following humps, crossing x and short c/oval/s group favor deux cas, but the strike prevents a letter-by-letter resolution.',
       'heading_case', 'low', 'omission')
change('initial_interlinear_insertion', '', '\\add{\\uncertain{Dans}\n\\uncertain{ce cas}}',
       r'\inserted{\unsure{Dans ce cas}}',
       'A separate interlinear group is present above the canceled opening clause. Its D-like loop and compressed following groups favor Dans ce cas; they are not sufficiently clear to remove doubt.',
       'heading_case', 'low', 'omission', True, False)
change('live_est_reunion', 'est réunion', r'\struck{est réunion}', 'est réunion',
       'The curved leader for =I rises above the words; it does not cross the bodies of est réunion. The words remain live.',
       'first_kg', kind='deletion state')
change('short_autom_abbreviation', 'autom.', 'automorph.', 'autom.',
       'The word stops after the m-shaped humps and a short terminal mark. There are no following o/r/p/h strokes.',
       'autom_universel', kind='abbreviation expanded or spelling modernised')
change('canceled_de_after_autom', r'\deleted{\unsure{de}}', r'\struck{\ill{}}', r'\deleted{\unsure{de}}',
       'A short crossed group follows autom.; a loop and low ending permit de. The crossing strokes obscure the internal letters, so the tentative reading remains.',
       'autom_universel', 'low', 'omission')
change('universel_quotation_marks', "``universel''", '« universel »', "``universel''",
       'Paired short ticks, not angled guillemets, stand on each side of universel.',
       'autom_universel', kind='misread symbol or index')
change('D_I_alphabet', r'g\in V(\unsure{D_I})', r'g \in V(\mathbb{D}_I)', r'g\in V(\unsure{D_I|\mathbb D_I})',
       'The whole formula has g, membership, V and two enclosing parentheses. The inner capital has a D-shaped bowl and an upright that may be doubled; the small serifed I is clear. Plain versus doubled D remains undecided.',
       'di_fixed', 'low', 'misread symbol or index', False, True, True)
change('insertion_after_P_est', r'\inserted{un de ses}', r'\add{\uncertain{un}}', r'\inserted{\unsure{un de|un}}',
       'The small interlinear strokes permit un de, with un as the shorter alternative. No distinct ses sequence can be identified after them.',
       'di_fixed', 'low', 'misread word', True, True)
change('canceled_baseline_word_after_P_est', '', r'\struck{\ill{}}', r'\deleted{\unsure{un}}',
       'A crossed word remains on the baseline below the small insertion. Its low joined strokes permit un, but the leader and cancellation prevent a secure letter-by-letter reading.',
       'di_fixed', 'low', 'omission', True, True)
change('singular_fixed_point', 'pts fixes.', 'pt fixe.', r'p\textsuperscript{t} fixe.',
       'A raised t follows p, and fixe ends with a low e and a stop. There is no final s on either abbreviated noun or adjective.',
       'di_fixed', kind='misread word', against_c=True, against_h=False)
change('canceled_De_before_Cette', r'\deleted{\unsure{De}}', r'\struck{\ill{}} Cette fois', r'\deleted{\unsure{De}} Cette fois',
       'The short crossed group before Cette fois has a D-like loop and a low ending. It remains tentative because the strike covers the letter bodies.',
       'di_fixed', 'low', 'omission')
change('modules_quotation_marks', "``modules''", '« modules »', "``modules''",
       'The quotation marks are paired short upright or slanted ticks, matching those around universel.',
       'modules_orbit', kind='misread symbol or index')
change('canceled_OPS_que', 'OPS que', r'\struck{$\lbrace P \rbrace$ \ill{}}', r'\unsure{OPS} que',
       'Before que, the squared loop, angular middle stroke and final curved stroke favor the letter group OPS. They do not securely resolve all three letters under the cancellation; no enclosing set braces are clear.',
       'canceled_mu', 'low', 'misread word')
change('canceled_elle_est_celle_de', 'elle est celle de', r"sur \ill{} \ill{} \ill{}", 'elle est celle de',
       'The e/l/l/e sequence, est, c/e/l/l/e and de can be followed beneath the crossing line. The group is within the large canceled passage.',
       'canceled_mu', 'high', r'readable ink left as \ill{}')
change('local_cancellation_donnee_par', 'est donnée par un', r'\ill{} \ill{} \ill{} une', r'est \deleted{\unsure{donnée par}} un',
       'A separate horizontal strike passes through the words between est and un. The d and following low groups favor donnée par, but internal letters remain covered; the local deletion is additional to the large canceled frame.',
       'canceled_orbit', 'low', 'deletion state', True, True)
change('un_before_t_pair', r'un \(\{t,-t\}\)', r'une $\lbrace t, -t \rbrace$', r'un \(\{t,-t\}\)',
       'The determiner ends at the n hump; there is no separate final e. Both t letters, the minus and the braces are visible.',
       'canceled_orbit', 'high', 'misread word', False, True, True)
change('multiplicative_k_superscript', r'\lambda\in k^\times', r'\lambda \in k^{*}', r'\lambda\in k^\times',
       'The small raised mark has two crossing diagonal strokes with four arms, without a third stroke of an asterisk.',
       'canceled_orbit', 'medium', 'misread symbol or index', False, True, True)
change('local_deleted_lambda_equals', r'\deleted{\(\lambda=\)}', r'donc $\lambda =$' + '\n' + '$J =', r'\deleted{\(\lambda=\)} \(J=',
       'A local horizontal strike crosses lambda and the equals sign before the live-in-the-draft J formula, independently of the later large cancellation.',
       'canceled_J', 'high', 'deletion state', False, True, True)
change('canceled_radicals_after_J', r'\deleted{\(\unsure{\sqrt\lambda,\sqrt\lambda}\)}', r'\pm\sqrt{\lambda})$ \ill{},',
       r'\deleted{\(\unsure{\sqrt\lambda,\sqrt\lambda}\)}',
       'Two root-like hooks and lambda-like strokes survive after the completed J tuple, crossed by a local strike. The crossing prevents resolution of the complete group.',
       'canceled_J', 'low', 'omission', False, True, True)
change('domain_Sigma_k', r'\lambda\in\unsure{\mathbb P^1}(k)\setminus\{0,1,\infty\}',
       '$\\lambda \\in\n\\Sigma(k) \\setminus \\lbrace 0, 1, \\infty \\rbrace$',
       r'\lambda\in\Sigma(k)\setminus\{0,1,\infty\}',
       'The capital is a zigzag between long top and bottom bars. There is no separate raised 1. The following k, parentheses and excluded 0,1,infinity are also legible.',
       'canceled_J', 'high', 'misread symbol or index', True, False, True)
change('orbit_change_prose', r'\unsure{en} \deleted{\unsure{changeant}} changeant le choix de l’orbite',
       "défini au changement\n\\ill{} près \\ill{} le choix de l'orbite",
       r'\unsure{en} \deleted{\unsure{changeant}} changeant le choix de l’orbite',
       'The initial short group favors en; the next group is locally crossed and remains changeant in doubt. The following changeant has a visible g descender and is followed by le choix de l’orbite. The strokes do not support défini or près.',
       'canceled_change', 'medium', 'misread word')
change('rho_parameter_definition', r'\(\beta=\lambda+\frac1\lambda\),', '$\\rho = \\lambda +\n\\frac{1}{\\lambda}$',
       r'\(\rho=\lambda+\frac1\lambda\),',
       'The parameter has one closed upper bowl and a long descending stem. There is no second lower bowl of beta; the plus sign and the fraction 1/lambda are clear.',
       'canceled_parameter', 'high', 'misread symbol or index', True, False, True)
change('rho_in_quadratic', r'\lambda^2-\beta\lambda+1=0', '$\\lambda^{2} - \\rho\\lambda + 1\n= 0$',
       r'\lambda^2-\rho\lambda+1=0',
       'The coefficient repeats the one-bowl descending rho from the definition. Both minus and plus, the exponent 2, the final 1 and 0 were read in the complete equation.',
       'canceled_parameter', 'high', 'misread symbol or index', True, False, True)
change('deleted_quadratic_root_formula', r'\deleted{\(\lambda=\frac12(\beta\pm\sqrt{\beta^2-4})\)},',
       r'$\lambda = \frac{1}{2}(\rho \pm \sqrt{\rho^{2} - 4})$',
       r'\deleted{\(\lambda=\frac12(\rho\pm\sqrt{\rho^2-4})\)},',
       'Both parameter letters have a single upper bowl and descending stem. A separate horizontal stroke cancels this whole formula, including lambda=, beyond the later large diagonal cancellation.',
       'canceled_parameter', 'medium', 'misread symbol or index', True, True, True)
change('rho_in_final_tuple', r'(0,\pm1,\pm\sqrt{\frac12(\beta\pm\sqrt{\beta^2-4})})',
       '$(0, \\pm 1, \\pm\\sqrt{\\tfrac{1}{2}(\\rho \\pm \\sqrt{\\rho^{2} -\n4})})$',
       r'(0,\pm1,\pm\sqrt{\frac12(\rho\pm\sqrt{\rho^2-4})})',
       'The two parameter letters again show upper loops with long descenders. The outer and inner roots, both plus-minus signs, fraction, exponent, minus 4 and closing parentheses remain visible under the cancellation.',
       'canceled_triple', 'high', 'misread symbol or index', True, False, True)
change('Comme_in_canceled_prose', r'\unsure{Eliminer}', 'Comme', r'\unsure{Comme}',
       'The initial open C and following low joined humps favor Comme. The tall l/i/n sequence required by Eliminer is not visible. Several crossing strokes still prevent complete resolution.',
       'canceled_eliminer', 'medium', 'misread word', True, False)
change('deux_in_canceled_prose', r'\unsure{deux}', r'et \ill{} \ill{} \ill{} $\lambda$', r'\unsure{deux}',
       'After et, a d-like loop and compressed low strokes ending in a crossing favor deux, but the crossing-out prevents a secure reading of every letter.',
       'canceled_eliminer', 'low', 'omission')
change('discriminant_different_in_canceled_prose', r'\unsure{discriminant différent}', r'et \ill{} \ill{} \ill{} $\lambda$',
       r'\unsure{discriminant différent}',
       'The first group has a d loop and compressed pointed strokes; the second has a d-like beginning and tall medial stroke. These permit the retained tentative words but do not make every letter plain.',
       'canceled_discriminant', 'low', 'omission')
change('canceled_two_infinity_pair', r'\(2,\infty\)', r'$1/\lambda$', r'\(2,\infty\)',
       'A curved 2, a comma and two connected infinity loops are visible before the long dash. No fraction bar with 1 above lambda occupies this place.',
       'canceled_discriminant', 'medium', 'misread symbol or index', False, True, True)
change('lower_canceled_comme_les_lambda_et', r'\unsure{comme} \deleted{\unsure{les}} \(\lambda\), et',
       r'$\lambda$, \ill{}' + '\n' + r'\ill{} \ill{} \ill{} $1/\lambda$, \ill{} \ill{}',
       r'\unsure{comme} \deleted{\unsure{les}} \(\lambda\), et',
       'The low humps after an uncertain initial support comme tentatively. A separate horizontal strike crosses a short following group read les in doubt. Lambda, the comma and et are clear; the added H fraction has no matching strokes in this short sequence.',
       'canceled_comme', 'low', 'misread word')
change('final_canceled_g_formula_and_points', r'\(g(z)=\frac{\lambda}{z}\), pts fixes.',
       r'${}^{g}(0,\lambda) =' + '\n' + r'\frac{\lambda}{z}$, pts \uncertain{fixes}',
       r'\(g(z)=\frac{\lambda}{z}\), p\textsuperscript{ts} fixes',
       'The left letter has a g loop and descender, followed by parentheses containing one angular z. The right fraction has lambda above another angular z. The raised ts and the letters fixes are visible. No separate final stop can be distinguished from the cancellation strokes.',
       'canceled_g', 'medium', 'misread symbol or index', True, True, True)
change('du_notre_point_de_vue', 'de notre point de vue', 'du notre point de vue', r'\unsure{du|de} notre point de vue',
       'The letter after d has an open low cup, favoring u; its compressed final turn still permits e. The unusual first reading du is retained without grammatical correction.',
       'pointdevue', 'medium', 'misread word', True, False)
change('live_d_un_after_des_sommets', r'\inserted{des sommets} d’un', r"\struck{d'un \ill{}} \add{des" + '\n' + r"sommets}\note{en interligne} \uncertain{d'un}",
       r'\inserted{des sommets} d’un',
       'The bracketed leader places des sommets before the baseline d’un. The tall d intersects the leader, but the word itself is not crossed out; a separate following group bears the cancellation.',
       'des_sommets', 'high', 'deletion state')
change('canceled_word_before_carre', r'\deleted{\unsure{carré|cas}}', r"\struck{d'un \ill{}}", r'\deleted{\unsure{carré|cas}}',
       'A crossed group follows the live d’un. Its initial c/a-like strokes permit carré, with cas as the shorter alternative; the remaining strokes are too covered to settle the word.',
       'des_sommets', 'low', 'omission')
change('possible_comma_after_equilateral', r'\unsure{équilatéral}, et', r'\uncertain{équilatéral} et',
       r'\unsure{équilatéral}\unsure{,} et',
       'A small terminal curl may be a comma after the word, but it is not securely separate from the final letter. The comma is retained as the first reading with explicit doubt.',
       'equilateral_edge', 'low', 'misread symbol or index')
change('singular_midpoint_phrase_M0459', r'\unsure{du milieu de l’une|des milieux de deux}', r'des milieux de \uncertain{deux}',
       'du milieu de l’une',
       'The determiner ends with u; milieu has no terminal x. After de, a short l with apostrophe precedes u-n-e, rather than the d/e/u/x group required by deux.',
       'equilateral_edge', 'high', 'misread word')
change('ordinal_in_inserted_question', r'\inserted{Est-ce le cas \(1^\circ\) ?}', r'\add{Est-ce le cas 10 ?}',
       r'\inserted{Est-ce le cas \(1^\circ\) ?}',
       'The upright 1 is followed by a small raised circle. The circle is above the baseline and much smaller than a full-height zero; the question mark and insertion leader are visible.',
       'question_tetra', 'high', 'misread symbol or index', False, True, True)

c_upper = between(C, r'\draw(0,0)ellipse(1 and 1.05);', r'\begin{scope}')
c_lower = between(C, r'\begin{scope}[shift={(-.8,-3)}]', r'\end{scope}', True)
h_drawing = between(H, r'\drawing{', '\n\n', False)
f_upper = between(F, '% Upper sphere:', r'\begin{scope}')
f_lower = between(F, r'\begin{scope}[shift={(25,305)}]', r'\end{scope}', True)
change('upper_sphere_drawing', c_upper, h_drawing, f_upper,
       'Five large equatorial points are visible, with three on the solid front curve and two on the broken rear curve. P is below the middle front point. The outer contour has lower-right and right-side gaps. The detached left hook has no secure arrowhead.',
       'figure_upper', 'high', 'drawing or diagram', True, True)
change('lower_sphere_drawing', c_lower, h_drawing, f_lower,
       'Four vertex points, two extra edge points and the separate P point are visible. Broken side segments and a dotted oblique slant are distinct. The outer contour is doubled at the left and remains open toward the lower right. These surviving strokes replace the witnesses’ closed generic contour and incomplete edge pattern.',
       'figure_lower', 'high', 'drawing or diagram', True, True)
change('heading_sigma_and_underline_scope', r'\uline{Cas des antiautomorphismes de \(\Sigma\)} \inserted{\(\sigma\)}',
       r'\emph{Cas des antiautomorphismes} $\sigma$ \emph{de} $\Sigma$',
       r'\uline{Cas des antiautomorphismes \inserted{\(\sigma\)} de} \(\Sigma\)',
       'The small sigma is written above the gap before de. The long underline runs through de and stops before the large Sigma; Sigma itself is outside the underline.',
       'antiauto_heading', 'high', 'insertion or placement', True, True, True)
change('heading_stables_plural_and_scope', r'laissant \uline{stables}', r'\emph{laissant stable}', r'laissant \uline{stables}',
       'The final curved s is visible after stable. A short underline is below stables only; the higher word laissant is not underlined.',
       'antiauto_heading', 'high', 'misread word')
change('capital_Cas_insertion', r'\inserted{(cas \(k=\mathbb C\))}',
       '(\\uncertain{Cas} $k =\n\\mathbf{C}$)',
       r'\inserted{\unsure{(}Cas \(k=\mathbb C\))}',
       'The initial C is tall and open, like the capital C of Comme. The formula has k= and a C with a doubled left stroke. The closing parenthesis is clear; the broad initial curve may be the insertion leader, so the opening parenthesis is doubtful.',
       'antiauto_heading', 'medium', 'misread word', True, True, True)
change('pronoun_after_Comme_M0460', r'Comme \unsure{il|\(\sigma\)}', r'Comme $\sigma$', r'Comme \unsure{il|\(\sigma\)}',
       'A short left stroke and high bowed right stroke favor il, but the condensed joining also permits sigma. Reader and root retained the alternatives after comparing the saved heading and body crops.',
       'antiauto_heading', 'low', 'misread word')
change('local_canceled_a', r'\deleted{\unsure{a}} a', r"qu'il \struck{\ill{}} a", r'\deleted{\unsure{a}} a',
       'A crossed loop with a right-hand exit precedes the live a. It permits a, but the local crossing prevents complete resolution.',
       'antiauto_body', 'low', 'omission')
change('raised_t_in_bottom_live_fixed_point', r'un pt fixe au moins dans \(K\)', r'un pt fixe au moins dans $K$',
       r'un p\textsuperscript{t} fixe au moins dans \(K\)',
       'The small t has an upright and short cross-stroke above the baseline after p. It is raised relative to the following fixe; both witnesses flatten this visible placement.',
       'antiauto_body', 'high', 'insertion or placement', True, True)
change('local_canceled_et_and_preceding_comma', r'\(\Sigma\), \deleted{\unsure{et}}', r'$\Sigma$ \struck{\ill{}}.',
       r'\(\Sigma\), \deleted{\unsure{et}}',
       'A descending comma follows Sigma. The following short group is crossed; its low loop and tall stroke favor et but remain obscured. The witness H period does not match the separate comma before the canceled group.',
       'antiauto_body', 'medium', 'misread symbol or index', False, True, True)
change('bottom_foliation_34', r'\mspage{34}', '', r'\margin{34}',
       'The bottom-left gray number has the two curves of 3 followed by an open 4 with a descending right limb.',
       'folio', 'high', 'omission', False, True)

decisions = [
    dict(id='M0457', decision='undecided', reading=r'\unsure{D_I|\mathbb D_I}',
         ink='The D-shaped bowl is clear, but the upright may be doubled. The subscript I is serifed and clear; the complete g∈V(D_I) formula was read.',
         crop='crops/148_scan035_di_fixed.jxl', box=BOXES['di_fixed'], confidence='low'),
    dict(id='M0458', decision='undecided', reading=r'\unsure{équilatéral}',
         ink='The q descender and tall later ascenders favor équilatéral. The compressed internal joins do not certify every letter; doubt is retained after root comparison.',
         crop='crops/148_scan035_equilateral_edge.jxl', box=BOXES['equilateral_edge'], confidence='medium'),
    dict(id='M0459', decision='first', reading='du milieu de l’une',
         ink='The initial u, singular milieu ending, apostrophe after l, and u-n-e sequence are visible. No final x or deux sequence is present.',
         crop='crops/148_scan035_equilateral_edge.jxl', box=BOXES['equilateral_edge'], confidence='high'),
    dict(id='M0460', decision='undecided', reading=r'\unsure{il|\(\sigma\)}',
         ink='The short left stroke and bowed tall stroke favor il, but their condensed join also permits sigma. Both alternatives remain after comparison with the body crop.',
         crop='crops/148_scan035_antiauto_heading.jxl', box=BOXES['antiauto_heading'], confidence='low'),
]

inventory = []
def inv(element, kind, position, first, hand='his hand'):
    inventory.append(dict(element=element, kind=kind, position=position,
                          first_words_or_objects=first, sheet_kind='text', hand=hand, transcribed='yes'))

inv('top_page_number', 'margin note', 'Top center, above the first line', '2', 'another unnamed hand')
inv('opening_case_paragraph', 'text', 'Upper portion, approximately y=100–590', r'\textcircled{4} \(\nu=2\)')
inv('opening_canceled_clause', 'deletion', 'First line, left of K^g', 'Il y a deux cas')
inv('Dans_ce_cas_insertion', 'insertion', 'Above the canceled opening clause', 'Dans ce cas')
inv('I_insertion', 'insertion', 'Above the gap before est réunion, with a curved leader', '=I')
inv('de_after_autom', 'deletion', 'After autom., before universel', 'de')
inv('un_de_insertion', 'insertion', 'Above the baseline after P est', 'un de')
inv('baseline_un_cancellation', 'deletion', 'Below the preceding insertion', 'un')
inv('De_before_Cette', 'deletion', 'Before Cette fois', 'De')
inv('large_canceled_calculation', 'deletion', 'Framed upper-middle block, approximately y=520–1445', 'OPS que l’opération')
inv('first_mu_set_insertion', 'insertion', 'Above the first mu_2 in the canceled block', r'=\{\pm1\}')
inv('second_mu_set_insertion', 'insertion', 'Above the second mu_2 in the canceled block', r'=\{\pm1\}')
inv('donnee_par_local_cancellation', 'deletion', 'Between est and un in the t,-t sentence', 'donnée par')
inv('lambda_equals_local_cancellation', 'deletion', 'After donc, immediately before J', r'\lambda=')
inv('J_formula', 'display', 'Middle of the canceled block, y≈880', r'J=(0,\pm1,\pm\sqrt\lambda)')
inv('radical_pair_local_cancellation', 'deletion', 'Immediately after the J tuple', r'\sqrt\lambda,\sqrt\lambda')
inv('changeant_local_cancellation', 'deletion', 'Between tentative en and the following changeant', 'changeant')
inv('changed_orbit_tuple', 'display', 'Left of Prenons le paramètre, y≈1090', r'(0,\pm1,\pm\sqrt{1/\lambda})')
inv('rho_parameter_and_equation', 'display', 'Across the parameter line, y≈1090–1150', r'\rho=\lambda+1/\lambda')
inv('not_two_insertion', 'insertion', 'Above the parameter definition', r'\ne2')
inv('quadratic_root_local_cancellation', 'deletion', 'Below the parameter equation', r'\lambda=\frac12(\rho\pm\sqrt{\rho^2-4})')
inv('final_tuple', 'display', 'Line beginning on trouve, within the cancellation', r'(0,\pm1,\pm\sqrt{\frac12(\rho\pm\sqrt{\rho^2-4})})')
inv('les_local_cancellation', 'deletion', 'Between tentative comme and lambda in the last canceled prose', 'les')
inv('g_formula', 'display', 'Bottom-left of the canceled frame', r'g(z)=\lambda/z')
inv('live_configuration_paragraph', 'text', 'From Cas moins intéressant through octaèdre associé', 'Cas moins intéressant')
inv('des_sommets_insertion', 'insertion', 'Above the line before live d’un', 'des sommets')
inv('canceled_carre_or_cas', 'deletion', 'After d’un and before live carré', 'carré')
inv('case_question_insertion', 'insertion', 'Between arêtes and Quand, with curved leader', 'Est-ce le cas 1° ?')
inv('six_insertion', 'insertion', 'Between des and sommets in the octahedron sentence', '6')
inv('upper_sphere', 'drawing', 'Left margin, approximately x=120–650,y=1865–2150', 'Five equatorial points; P')
inv('lower_sphere', 'drawing', 'Left margin below the first sphere, approximately x=145–465,y=2170–2465', 'Tetrahedral strokes; seven marked points including P')
inv('antiautomorphism_heading', 'text', 'Lower portion, heading through stables K', 'Cas des antiautomorphismes')
inv('heading_sigma_insertion', 'insertion', 'Above the gap before de Sigma', r'\sigma')
inv('complex_case_insertion', 'insertion', 'Between the heading underline and Comme, with a leader from K', '(Cas k=C)')
inv('antiautomorphism_paragraph', 'text', 'From Comme through the final ou 5', 'Comme il est d’ordre pair')
inv('a_local_cancellation', 'deletion', 'Before the live a un p^t fixe', 'a')
inv('et_local_cancellation', 'deletion', 'After réelle sur Sigma and a comma', 'et')
inv('bottom_foliation', 'margin note', 'Bottom-left, separate gray number', '34', 'another unnamed hand')

unresolved = []
def doubt(place, reading, issue, alternatives=(), confidence='low'):
    unresolved.append(dict(place=place, reading=reading, issue=issue,
                           alternatives=list(alternatives), confidence=confidence))

doubt('canceled_opening_clause', 'deux cas', 'The cancellation covers parts of both words; every letter is not plain.')
doubt('initial_interlinear_insertion', 'Dans ce cas', 'The small interlinear groups are compressed; some joins remain uncertain.')
doubt('canceled_de_after_autom', 'de', 'The two-letter group is covered by crossing strokes.')
doubt('D_I_alphabet', r'D_I', 'The bowl is D-shaped, but the upright may be doubled.', [r'\mathbb D_I'])
doubt('insertion_after_P_est', 'un de', 'The small insertion does not securely separate all letters; no distinct ses can be established.', ['un'])
doubt('canceled_baseline_word_after_P_est', 'un', 'The baseline word is crossed and overlaps the insertion leader.')
doubt('canceled_De_before_Cette', 'De', 'The capital-like loop and ending are partly covered by the strike.')
doubt('canceled_OPS_que', 'OPS', 'The large cancellation crosses the initial loop and middle letter.')
doubt('local_cancellation_donnee_par', 'donnée par', 'A local horizontal strike covers internal letters.')
doubt('canceled_radicals_after_J', r'\sqrt\lambda,\sqrt\lambda', 'Local crossing strokes obscure parts of both radical groups.')
doubt('orbit_change_initial_word', 'en', 'The frame overlaps the initial loop; capitalization is also uncertain.', ['En'])
doubt('locally_deleted_changeant', 'changeant', 'Several internal letters are covered by the local cancellation.')
doubt('Comme_in_canceled_prose', 'Comme', 'The open C and low humps favor this reading, but diagonal cancellation obscures the complete sequence.', [], 'medium')
doubt('deux_in_canceled_prose', 'deux', 'The low central strokes and final crossing cannot all be separated from cancellation.')
doubt('discriminant_different_in_canceled_prose', 'discriminant différent', 'Only parts of the initial loops, low strokes and ascenders survive clearly.')
doubt('lower_canceled_comme', 'comme', 'The initial group and low humps remain crossed and compressed.')
doubt('locally_deleted_les', 'les', 'The short group is crossed by a separate horizontal line.')
doubt('du_notre_point_de_vue', 'du', 'The open final cup favors u, but its compressed exit also permits e.', ['de'], 'medium')
doubt('canceled_word_before_carre', 'carré', 'The cancellation covers the end of the word.', ['cas'])
doubt('M0458', 'équilatéral', 'The descender and ascenders favor the word, but the internal joins do not certify every letter.', [], 'medium')
doubt('possible_comma_after_equilateral', ',', 'The mark may be the terminal curl of the last letter rather than separate punctuation.', ['no separate comma'])
doubt('opening_parenthesis_of_case_insertion', '(', 'The broad opening curve may belong entirely to the insertion leader; only the closing parenthesis is secure.', ['insertion leader only'])
doubt('M0460', 'il', 'The compressed left and bowed right strokes also admit sigma.', [r'\sigma'])
doubt('local_canceled_a', 'a', 'The short loop is crossed by a local strike.')
doubt('local_canceled_et', 'et', 'The low loop and tall stroke are partly obscured by cancellation.')

notes = [
    dict(id='S035-01', kind='claim', text='The live opening treats nu=2, with K^g={P} and I=K minus K^g a union of two orbits. It calls g a universal automorphism of Sigma minus I and says that P is a fixed point. These assertions were transcribed, not mathematically checked.'),
    dict(id='S035-02', kind='claim', text='The canceled calculation uses a parameter lambda and then rho=lambda+1/lambda, followed by the written quadratic equation and root expressions. The canceled status and local revisions are retained. No algebraic computation or proof was performed.'),
    dict(id='S035-03', kind='claim', text='The live configuration paragraph says that this case has moduli, describes square configurations, asks whether one construction is case 1°, and places P among the six vertices of an associated octahedron in the tetrahedral case. These are manuscript claims, not verified conclusions.'),
    dict(id='S035-04', kind='claim', text='The last paragraph asserts that the finite-order antiautomorphism under discussion has order 2 and corresponds to a real structure, then distinguishes fixed-set cardinalities 1, 3 and 5. This argument was not checked.'),
    dict(id='N035-01', kind='deletion state', text='The large framed calculation is canceled by long diagonal strokes. Local deletions inside it are separately retained: donnée par, lambda=, the radicals after J, the first changeant, the quadratic-root formula and les. The two inserted mu-set formulas remain part of the canceled draft.'),
    dict(id='N035-02', kind='reading', text='The first reading du notre point de vue is retained with de as an alternative; grammatical expectation does not decide the compressed last letter. Similarly, the canceled final prose remains tentative rather than being completed into a coherent argument.'),
    dict(id='N035-03', kind='reading', text='The initial interlinear Dans ce cas and the insertion after P est are present. The latter is read un de with un as an alternative; the witnesses do not justify supplying ses. A separate crossed baseline word remains tentatively un.'),
    dict(id='N035-04', kind='review', text='Reader C initially favored il and a resolved équilatéral. Root comparison of the same saved crops did not securely exclude sigma or certify every internal letter of équilatéral, so both doubts are retained. Root also identified the possible opening parenthesis of the case note as an insertion-leader ambiguity.'),
    dict(id='N035-05', kind='drawing', text='Both drawings preserve open contours and visible gaps. The lower drawing includes two edge points in addition to its four vertex points and P, plus a dotted oblique slant. No arrowhead is supplied for the detached upper-left curved stroke.'),
    dict(id='N035-06', kind='date', text='No manuscript date appears on this sheet. The top number 2 and bottom foliation 34 are transcribed separately; neither number is used to infer a date.'),
    dict(id='N035-07', kind='method', text='Whole-page layout and both native overlapping halves were read once. All 25 saved crops were visually inspected; each PNG was successfully loaded before a same-pixel JPEG transport copy was made. The added canceled_comme rectangle is the first crop for that distinct word place, which earlier rectangles clipped. No OCR, research or TeX compilation was used.'),
    dict(id='N035-08', kind='accounting', text='Run SP82_C13_148; reader C; model GPT-6 Astra Pro; reasoning effort is not exposed. Reading completed on 2026-11-20 UTC. Line accounting includes the main baselines, separate interlinear additions and canceled formula line, two figure labels and the two separate handwritten numbers. The checks list is empty because no mathematical computation or proof was carried out.'),
]

hand_log = [
    dict(form=r'\rho', observation='One closed upper bowl with a long descending stem; no second lower bowl.', pages=[35], holds_at_every_observed_occurrence=True, witness_effect='C read beta at all six parameter occurrences in the four formula places; the visible forms are rho.'),
    dict(form=r'\mu_2', observation='The two mu letters are tall and doubled in their uprights, resembling the previously recorded mu habit.', pages=[35], holds_at_every_observed_occurrence=True, witness_effect='No new letter change is needed here; both occurrences were read from the ink.'),
    dict(form=r'\Sigma', observation='The capital in the canceled domain is a zigzag between long horizontal arms, matching the other Sigma forms on this page.', pages=[35], holds_at_every_observed_occurrence=True, witness_effect='C’s doubtful projective-line notation at the domain is replaced by Sigma(k).'),
    dict(form=r'p\textsuperscript{t}; p\textsuperscript{ts}', observation='The abbreviation endings are raised; the two live fixed-point statements are singular, while the canceled final note has raised ts.', pages=[35], holds_at_every_observed_occurrence=True, witness_effect='C supplied a plural in the opening fixed-point phrase. Both witnesses flatten the raised endings typographically.'),
    dict(form='insertion leaders', observation='Curved or bracketed leaders pass close to baseline letters and can resemble cancellation or punctuation.', pages=[35], holds_at_every_observed_occurrence=False, witness_effect='H cancels est réunion and d’un where the visible strokes are placement leaders. The opening parenthesis of the Cas insertion remains ambiguous.'),
]

notation = [
    dict(form=r'\rho', use='Parameter in the canceled relation rho=lambda+1/lambda and its following quadratic formulas.', pages=[35], caution='Read from the one-bowl descending form, not from the expected algebra.'),
    dict(form=r'\Sigma(k)', use='Written domain for lambda in the canceled passage.', pages=[35], caution='The capital is Sigma, without a separate exponent 1.'),
    dict(form=r'k^\times', use='Nonzero-parameter notation in the canceled t,-t sentence.', pages=[35], caution='The raised mark has two diagonal strokes.'),
    dict(form=r'D_I\text{ or }\mathbb D_I', use='Inner symbol of g in V(D_I).', pages=[35], caution='Plain versus doubled upright remains unresolved.'),
    dict(form='open contour and broken segments', use='Both margin sphere drawings.', pages=[35], caution='Do not close gaps or replace the visible broken and dotted paths by a regular polyhedron.'),
]

abbreviations = [
    dict(form='autom.', expansion='automorphisme', place='Opening live paragraph'),
    dict(form='p.ex.', expansion='par exemple', place='Opening live paragraph'),
    dict(form=r'p\textsuperscript{t}', expansion='point', place='Two live fixed-point statements'),
    dict(form=r'p\textsuperscript{ts}', expansion='points', place='Final line of the canceled block'),
    dict(form='OPS', expansion='on peut supposer', place='Beginning of the canceled block', note='The written abbreviation itself remains doubtful; the expansion is proposed only.'),
]

second_boxes = []
def second(label, kind, reading, coords=None):
    x0, y0, x1, y1 = BOXES[label] if coords is None else coords
    second_boxes.append(dict(box='035_'+label, kind=kind, x0=x0, y0=y0, x1=x1, y1=y1, reading=reading))

second('heading_case', 'insertion and deletion', r'\textcircled{4}\;\nu=2.\;\deleted{Il y a deux cas}\;\inserted{Dans ce cas}')
second('first_kg', 'formula and insertion', r'K^g=\{P\},\quad K\setminus K^g\;\inserted{=I}\quad\text{est réunion}')
second('autom_universel', 'word difference and deletion', "autom. \\deleted{de} ``universel''")
second('di_fixed', 'formula insertion and deletion', r'\Sigma\setminus I\quad(g\in V(D_I))\quad P\text{ est }\inserted{un de}\;\deleted{un}\;p\textsuperscript{t}\text{ fixe. }\deleted{De}\text{ Cette fois}')
second('modules_orbit', 'word difference', "la situation a des ``modules'', p.ex. en choisissant une")
second('canceled_mu', 'deletion and insertions', r'\deleted{OPS que l’opération de \(g\) sur elle est celle de \(\mu_2\)\inserted{\(=\{\pm1\}\)} sur \(\mu_2\)\inserted{\(=\{\pm1\}\)}, et \(P=0\), l’autre orbite}')
second('canceled_orbit', 'deletion and formula', r'\deleted{est \deleted{donnée par} un \(\{t,-t\}\), avec \(\lambda=t^2\ne1,\lambda\in k^\times\)}')
second('canceled_J', 'deletion and formula', r'\deleted{donc \deleted{\(\lambda=\)}\(J=(0,\pm1,\pm\sqrt\lambda)\)\deleted{\(\sqrt\lambda,\sqrt\lambda\)}, avec \(\lambda\in\Sigma(k)\setminus\{0,1,\infty\}\)}')
second('canceled_change', 'deletion and insertion', r'\deleted{en \deleted{changeant} changeant le choix de l’orbite, on trouve}\quad\inserted{\ne2}')
second('canceled_parameter', 'deletion and formulas', r'\deleted{(0,\pm1,\pm\sqrt{1/\lambda}).\quad\rho=\lambda+1/\lambda,\quad\lambda^2-\rho\lambda+1=0,\quad\deleted{\lambda=\frac12(\rho\pm\sqrt{\rho^2-4})}}')
second('canceled_triple', 'deleted formula', r'\deleted{(0,\pm1,\pm\sqrt{\frac12(\rho\pm\sqrt{\rho^2-4})})}')
second('canceled_eliminer', 'deleted word difference', r'\deleted{Comme \(0,\infty\), et deux}')
second('canceled_discriminant', 'deleted text and numbers', r'\deleted{discriminant différent \(2,\infty\) ---}')
second('canceled_g', 'deleted formula', r'\deleted{\(g(z)=\lambda/z\), p\textsuperscript{ts} fixes}')
second('pointdevue', 'word difference', 'Cas moins intéressant que les précédents, du notre point de vue, car il y a des')
second('des_sommets', 'insertion and deletion', r'\inserted{des sommets} d’un \deleted{carré} carré')
second('equilateral_edge', 'doubt and word difference', 'équilatéral, et du milieu de l’une des arêtes')
second('question_tetra', 'insertions and numbers', r'\inserted{Est-ce le cas \(1^\circ\) ?}\quad P\text{ est un des }\inserted{6}\text{ sommets}')
second('figure_upper', 'drawing', r'\begin{tikzpicture}' + '\n' + f_upper + r'\end{tikzpicture}')
second('figure_lower', 'drawing', r'\begin{tikzpicture}' + '\n' + f_lower + r'\end{tikzpicture}')
second('antiauto_heading', 'insertions and word differences', r'\uline{Cas des antiautomorphismes \inserted{\(\sigma\)} de} \(\Sigma\) laissant \uline{stables} \(K\).\inserted{(Cas \(k=\mathbb C\))} Comme il est d’ordre pair')
second('antiauto_body', 'deletions and numbers', r'\deleted{a} a un p\textsuperscript{t} fixe\quad\text{d’ordre }2\quad\Sigma,\deleted{et}\quad K^\sigma,\text{ qui est }1,3,\text{ ou }5')
second('page_two', 'handwritten number', '2')
second('folio', 'margin note', r'\margin{34}')
second('canceled_comme', 'deleted word difference', r'\deleted{comme \deleted{les} \(\lambda\), et}')
second('square_case_number', 'handwritten number', r'Quand la structure \((\Sigma,I)\) est une structure carrée, on retrouve soit le cas \(2^\circ\) (si \(g\) laisse stables les deux diagonales)', [310,1450,2180,1790])
large_deleted = between(F, r'\deleted{\unsure{OPS}', '\n\nCas moins intéressant')
second('large_canceled_scope', 'deletion', large_deleted, [295,520,2210,1445])

reading_rows = {
    516:'circled_case_4', 518:'initial_interlinear_insertion', 519:'initial_interlinear_insertion',
    526:'short_autom_abbreviation', 527:'universel_quotation_marks', 528:'canceled_de_after_autom; universel_quotation_marks',
    533:'insertion_after_P_est; singular_fixed_point', 534:'canceled_De_before_Cette', 535:'modules_quotation_marks',
    536:'canceled_OPS_que', 539:'canceled_elle_est_celle_de', 540:'canceled_elle_est_celle_de',
    547:'local_cancellation_donnee_par; un_before_t_pair', 550:'multiplicative_k_superscript',
    553:'canceled_radicals_after_J', 555:'domain_Sigma_k', 557:'orbit_change_prose',
    561:'rho_parameter_definition', 562:'rho_parameter_definition', 565:'rho_in_quadratic',
    569:'deleted_quadratic_root_formula; rho_in_final_tuple', 570:'Comme_in_canceled_prose',
    571:'rho_in_final_tuple; lower_canceled_comme_les_lambda_et; final_canceled_g_formula_and_points',
    572:'rho_in_final_tuple; Comme_in_canceled_prose; deux_in_canceled_prose; discriminant_different_in_canceled_prose; canceled_two_infinity_pair; lower_canceled_comme_les_lambda_et',
    573:'final_canceled_g_formula_and_points', 575:'final_canceled_g_formula_and_points', 576:'du_notre_point_de_vue',
    583:'live_d_un_after_des_sommets', 584:'live_d_un_after_des_sommets; canceled_word_before_carre',
    585:'possible_comma_after_equilateral', 586:'singular_midpoint_phrase_M0459', 587:'ordinal_in_inserted_question',
    595:'upper_sphere_drawing; lower_sphere_drawing', 596:'upper_sphere_drawing', 597:'upper_sphere_drawing',
    598:'lower_sphere_drawing', 599:'lower_sphere_drawing', 600:'upper_sphere_drawing; lower_sphere_drawing; heading_sigma_and_underline_scope; heading_stables_plural_and_scope',
    601:'heading_sigma_and_underline_scope', 603:'heading_sigma_and_underline_scope', 604:'heading_stables_plural_and_scope',
    608:'pronoun_after_Comme_M0460', 611:'local_canceled_a', 621:'local_canceled_et_and_preceding_comma', 628:'bottom_foliation_34',
}
with (PACKET / 'differences.tsv').open(newline='') as f:
    source_rows = list(csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE))
differences_review = []
for row in source_rows:
    n = int(row['source_row'])
    differences_review.append(dict(source_row=n,
        classification='reading decision' if n in reading_rows else 'macro-only',
        place=reading_rows.get(n, 'math delimiters, equivalent macro or apostrophe typography, or H editorial framing')))

# Preserve the candidate's full diplomatic readings in the blind-reread record.
# Excerpts inside the large canceled block retain that enclosing deletion as well
# as every local deletion, insertion, uncertainty mark and written formula.
def canceled_excerpt(start, end):
    return r'\deleted{' + between(F, start, end) + '}'

exact_second_readings = {
    '035_heading_case': between(F, r'\textcircled{4}', r' \(K^g'),
    '035_first_kg': between(F, r'\(K^g', ' de deux orbites'),
    '035_autom_universel': between(F, 'autom.', r' de \(\Sigma'),
    '035_di_fixed': between(F, r'\(\Sigma\setminus I\)', ', la situation'),
    '035_modules_orbit': between(F, 'la situation a des', ' des deux orbites'),
    '035_canceled_mu': canceled_excerpt(r'\unsure{OPS}', r' est \deleted{\unsure{donnée par}}'),
    '035_canceled_orbit': canceled_excerpt(r'est \deleted{\unsure{donnée par}}', '\ndonc'),
    '035_canceled_J': canceled_excerpt(r'donc \deleted{\(\lambda=\)}', '\n' + r'\unsure{en}'),
    '035_canceled_change': canceled_excerpt(r'\unsure{en}', '\n' + r'\[') + '\n' + r'\deleted{\inserted{\(\ne2\)}}',
    '035_canceled_parameter': canceled_excerpt('\\[\n(0,', '\non trouve \\((0,'),
    '035_canceled_triple': canceled_excerpt(r'on trouve \((0,', '\n' + r'\unsure{Comme}'),
    '035_canceled_eliminer': canceled_excerpt(r'\unsure{Comme}', ' ' + r'\unsure{discriminant différent}'),
    '035_canceled_discriminant': canceled_excerpt(r'\unsure{discriminant différent}', ' ' + r'\unsure{comme}'),
    '035_canceled_g': r'\deleted{' + between(F, r'\(g(z)=', '}\n\nCas moins') + '}',
    '035_pointdevue': between(F, 'Cas moins intéressant', ' modules. Quand'),
    '035_des_sommets': between(F, r'\inserted{des sommets}', ' sphérique'),
    '035_equilateral_edge': between(F, r'\unsure{équilatéral}', '. ' + r'\inserted{Est-ce'),
    '035_question_tetra': between(F, r'\inserted{Est-ce', ' sommets de l’octaèdre') + ' sommets',
    '035_antiauto_heading': between(F, r'\uline{Cas des antiautomorphismes', ' est d’ordre pair') + ' est d’ordre pair',
    '035_antiauto_body': between(F, r'\deleted{\unsure{a}} a', '\n' + r'\margin{34}'),
    '035_page_two': r'\mspage{2}',
    '035_canceled_comme': canceled_excerpt(r'\unsure{comme}', '\n' + r'\(g(z)='),
}
for entry in second_boxes:
    if entry['box'] in exact_second_readings:
        entry['reading'] = exact_second_readings[entry['box']]

for entry in changes:
    if entry['place'] == 'singular_midpoint_phrase_M0459':
        entry['against_c'] = True
    elif entry['place'] == 'singular_fixed_point':
        entry['against_h'] = True

for entry in hand_log:
    entry['habit'] = entry['form'] + ': ' + entry['observation']

result = dict(scan=35, reader='C', lines_read=43, changes=changes, decisions=decisions,
              inventory=inventory, unresolved=unresolved, notes=notes, checks=[],
              hand_log=hand_log, notation=notation, abbreviations=abbreviations,
              second_boxes=second_boxes, differences_review=differences_review)
(OUT / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:len(result[k]) for k in ['changes','decisions','inventory','unresolved','second_boxes','differences_review']}, indent=2))
