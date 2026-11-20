from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
PACKET = ROOT / 'packets/145_scan020'
OUT = ROOT / 'edition/reader_reports'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
crop_meta = json.loads((ROOT / 'edition/crops/145_scan020_crop_meta.json').read_text())
crops = {int(x['file'].split('_')[2]): x for x in crop_meta}

old_product = r'''\deleted{$\unsure{[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}]
[\underbrace{\rho\sigma_0\rho^{-1}}_{\sigma_1}
\underbrace{\rho^{-1}\sigma_0\rho}_{\sigma_\infty}\rho^{-1}]=1}$}'''
short_product = r'[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}][\underbrace{\rho\sigma_0\rho^{-1}}_{\sigma_1}\underbrace{\rho^{-1}\sigma_0}_{\sigma_\infty}\rho^{-1}]'
long_product = r'[\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}][\underbrace{\rho\sigma_0\rho^{-1}}_{\sigma_1}\underbrace{\rho^{-1}\sigma_0\rho}_{\sigma_\infty}\rho^{-1}]'
new_product = r'\deleted{$\unsure{' + short_product + '|' + long_product + '}$}'
new_linfty = r'l_\infty&=(\unsure{\rho^{\deleted{-1}}|\rho^{-1}}\sigma_0\deleted{\unsure{\rho}})^2'

replacements = [
    (r'(6)\qquad \rho^3=1.', r'(6)\qquad \rho^3=1'),
    (old_product, new_product),
    (r'\unsure{vient du fait}', 'vient du fait'),
    (r'l_\infty&=(\rho^{-1}\sigma_0\deleted{\unsure{\rho}})^2', new_linfty),
    (r'\operatorname{int}(\sigma_0)(l_0)&=l_\infty^{-1}l_1^{-1}.', r'\operatorname{int}(\sigma_0)(l_0)&=l_\infty^{-1}l_1^{-1}'),
    (r'et itou pour $\sigma_1,\sigma_\infty$.}', r'et itou pour $\sigma_1,\sigma_\infty$}'),
    (r'\deleted{donc}', r'\deleted{\unsure{donc}}'),
    (r'\unsure{p.r.|p.v.}', r'\unsure{p.v.|p.r.}'),
    (r"\unsure{qu'on interprète|pris les transposés}", r"\unsure{qu'on interprète}"),
    (r"\deleted{\unsure{de notre groupe} $\sigma_i'$}", r"\deleted{\unsure{de notre groupe} $\unsure{\mathcal E'|\sigma_i'}$}"),
    (r"\unsure{\sigma'_{\dot\rho^{-1}(i)}|\sigma^{-1}_{\dot\rho^{-1}(i)}}", r"\sigma'_{\dot\rho^{-1}(i)}"),
    (r'\inserted{(i,j,k)\text{ distincts}}', r'\inserted{(i,j,k)\text{ distincts})}'),
    (r'\operatorname{int}(\rho)l_i&=l_{\dot\rho(i)}.', r'\operatorname{int}(\rho)l_i&=l_{\dot\rho(i)}'),
    (r'\unsure{idem|à dire}', 'idem'),
    (r'l_{\unsure{1|0}}', r'l_{\unsure{0|1}}'),
]
tex = C
for old, new in replacements:
    assert tex.count(old) == 1, (old, tex.count(old))
    tex = tex.replace(old, new)
tex = tex.rstrip() + '\n'
OUT.mkdir(parents=True, exist_ok=True)
(OUT / '145_scan020.tex').write_text(tex)

changes = []
def change(place, c, h, final, ink, crop_no, kind, cats, *, cc=False, hc=True,
           confidence='high', marked='no', math='', extra=()):
    assert cc or hc
    cr = crops[crop_no]
    item = dict(id=f's020-{len(changes)+1:02d}', place=place, C=c, H=h, final=final,
                ink=ink, confidence=confidence, kind=kind, c_changed=cc,
                h_changed=hc, marked_in_H=marked, crop=cr['file'], box=cr['box'],
                error_category=cats, math_consequence=math)
    if extra:
        item['additional_crops'] = [crops[n]['file'] for n in extra]
    changes.append(item)
    return item['id']

rel4 = r'''(4)\qquad
\overbrace{(\rho^{-1}\sigma_\infty\sigma_0\deleted{\rho})}^{l_\infty}
\overbrace{(\rho^{-1}\sigma_1\sigma_\infty\deleted{\rho})}^{l_1}
\overbrace{(\rho^{-1}\sigma_0\sigma_1\deleted{\rho})}^{l_0}=1'''
rel4h = r'''(4) \qquad
\overbrace{(\rho^{-1}\sigma_\infty\sigma_0 \struck{\ill{}})}^{l_\infty}\,
\overbrace{(\rho^{-1}\sigma_1\sigma_\infty \struck{\ill{}})}^{l_1}\,
\overbrace{(\rho^{-1}\sigma_0\sigma_1 \struck{\ill{}})}^{l_0} = 1'''
id_equal = change('Opening sentence, au =', r'au $=$', 'au même', r'au $=$',
    'Two short parallel horizontal bars follow au. There are no letter bodies for même.', 1,
    'abbreviation expanded or spelling modernised', [8])
id_rhos = change('Relation (4), three cancelled terminal factors', rel4, rel4h, rel4,
    'Each parenthesized group ends in a crossed loop-headed descending rho. The three overbrace labels are respectively l_infinity, l_1 and l_0; these labels and all surviving factors were independently read.', 2,
    'readable ink left as \\ill{}', [1,5,7], confidence='medium', marked='yes')
id_six_stop = change('Relation (6), after 1', r'(6)\qquad \rho^3=1.', r'(6) \qquad \rho^3 = 1.', r'(6)\qquad \rho^3=1',
    'The dark lower hook belongs continuously to the foot of the numeral 1; no separate full stop follows it.', 3,
    'text not on the page', [9], cc=True)

margin_intro = r'Il faut ajouter les relations $\rho\sigma_0\rho^{-1}=\sigma_1$ etc.'
id_margin_intro = change('Left margin, opening instruction', margin_intro,
    r'Il faut \uncertain{ajouter} \uncertain{la} relation (4) \ill{} $\rho\sigma_0\rho^{-1} = \sigma_1$ \ill{}', margin_intro,
    'The tall j and following outer loops spell ajouter; les has the final s stroke and relations has its plural ending. The displayed conjugation is followed by the compact etc. The numeral (4) is lower down in the consequence sentence, not here.', 17,
    'misread word', [1,2,3,5,6], marked='yes')
margin_presentation = r'On a deux gén. $\sigma_0,\rho$ en fait avec relations $\sigma_0^2=\rho^3=1$, la'
id_presentation = change('Left margin, two generators and their relations',
    'On a deux gén. $\\sigma_0,\\rho$ en fait avec relations\n\\[\n\\sigma_0^2=\\rho^3=1,\n\\]\nla',
    r'\ill{} relations (5) \ill{}', margin_presentation,
    'On a deux and the abbreviated gén. are visible before the two named generators. The next line has en fait avec relations. The small formula has a raised 2 on sigma_0, a raised 3 on rho, and equals 1, then a comma and la. No relation number (5) belongs to this margin formula.', 17,
    'readable ink left as \\ill{}', [1,2,3,5,8,9], marked='yes', extra=(18,))
id_product = change('Left margin, entire crossed bracketed product', old_product, r'\ill{}', new_product,
    'Dense diagonal cancelling strokes cross both brackets. The first bracket supports rho^-1 sigma_0 rho sigma_0 rho^-1. In the second, the shorter factor sequence is visually favored; the sigma_infinity underbrace endpoint and a possible further rho cannot be separated securely from loops and cancellation. The newly exposed edge beyond the closing bracket is blank: there is no terminal =1. Both factor/scope readings are retained under one whole-formula doubt.', 18,
    'text not on the page', [1,3,5,7,9], cc=True, confidence='low', marked='yes', extra=(23,))
consequence_c = r"relation (4) est conséquence des précédentes (\unsure{vient du fait} $\sigma_1=\rho\sigma_0\rho^{-1}$, \deleted{\illegible{1}} $\sigma_\infty=\rho^{-1}\sigma_0\rho$). Noter"
consequence = consequence_c.replace(r'\unsure{vient du fait}', 'vient du fait')
id_consequence = change('Left margin, consequence sentence and parenthetical identities', consequence_c,
    r'relation (4) \ill{} $\rho\sigma_0\rho^{-1} = \sigma_1$ \ill{} relations (5) \ill{} Noter \ill{} (7) \ill{}', consequence,
    'The ascending and descending loops support est conséquence des précédentes. Vient ends one slanting line, and du fait begins the next with a long f descender. The two sigma subscripts and the placement of rho^-1 are visible across the overlapping margin crops. The short crossed item between the identities remains unreadable. H’s additional margin numerals (5) and (7) are not written at these positions.', 19,
    'readable ink left as \\ill{}', [1,2,3,5,6,9], marked='yes', extra=(18,20))
l0 = r'l_0=\deleted{\unsure{(\rho\sigma_0\rho^{-1})^2}}\rho^{-1}(\sigma_0\rho)^2\rho=\boxed{\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}}'
id_l0 = change('Left margin, l_0 computation and its box', l0, r'l_0 = \ill{}', l0,
    'The first parenthesized square is crossed and remains doubtful. The following live expression has initial rho^-1, the parenthesized sigma_0 rho with superscript 2, and a final rho. The result is enclosed in a genuine box, not crossed out; its five factors and both inverse exponents can be read.', 20,
    'readable ink left as \\ill{}', [1,3,5,7], confidence='medium', marked='yes', extra=(21,))
l1 = r'l_1=(\deleted{\unsure{\rho}}\sigma_0\rho)^2'
id_l1 = change('Left margin, l_1 square', l1, r'l_1 = \ill{}', l1,
    'The subscript is a single 1. The initial letter inside the parenthesis is cancelled and has rho-like surviving strokes but remains occluded. Sigma_0, the live final rho, and raised 2 are visible.', 21,
    'readable ink left as \\ill{}', [1,3,5,7], confidence='medium', marked='yes')
linfty = new_linfty.replace('&', '')
id_linfty = change('Left margin, l_infinity square and initial-rho exponent state',
    r'l_\infty=(\rho^{-1}\sigma_0\deleted{\unsure{\rho}})^2', r'l_\infty = l_0^{\ill{}} l_1', linfty,
    'The initial rho has a short thick zigzag across the exponent position, unlike the clean separate minus and upright 1 in the neighboring l_0 line. Cancellation of -1 is favored but a live -1 cannot be excluded. The final crossed rho also remains doubtful. The enclosing parentheses and raised 2 are clear; H’s l_0 power times l_1 is not the written shape.', 21,
    'deletion state', [1,5,7], cc=True, confidence='low', marked='yes',
    math='The parent reader flagged a possible mathematical distinction between the two exponent states. No algebra was used by this first reader to settle the ink.')
conjugations_c = r'''\begin{aligned}
\operatorname{int}(\sigma_0)l_1&=l_\infty\\
\operatorname{int}(\sigma_0)l_\infty&=l_1\\
\operatorname{int}(\sigma_0)(l_0)&=l_\infty^{-1}l_1^{-1}.
\end{aligned}'''
conjugations = r'''\begin{aligned}
\operatorname{int}(\sigma_0)l_1&=l_\infty\\
\operatorname{int}(\sigma_0)l_\infty&=l_1\\
\operatorname{int}(\sigma_0)(l_0)&=l_\infty^{-1}l_1^{-1}
\end{aligned}'''
id_conjugations = change('Left margin, three inner-conjugation formulas', conjugations_c,
    r'\mathrm{int}(\sigma_0) l_1 = l_\infty^{\ill{}}, \mathrm{int}(\sigma_0) l_\infty = l_1^{\ill{}}', conjugations,
    'The first two right sides have bare infinity and 1 subscripts, without exponent ink. The third line has parentheses around l_0 and the two explicit -1 exponents on its right side. There is no separated final full stop after that product.', 22,
    'omission', [1,3,5,9], cc=True, marked='yes')
right_nb_c = r'''\uline{NB}
\begin{aligned}
\sigma_0(l_0)&=l_\infty^{-1}l_1^{-1}\\
\sigma_0(l_1)&=l_\infty\\
\sigma_0(l_\infty)&=l_1\deleted{\unsure{l_\infty^{-1}}}
\end{aligned}
et itou pour $\sigma_1,\sigma_\infty$.'''
right_nb = right_nb_c[:-1]
id_right_nb = change('Right margin, underlined NB and three formulas', right_nb_c,
    r'NB $\sigma_0(l_0) = l_\infty^{-1} l_1^{-1}$, $\sigma_0(l_1) = l_\infty$, $\sigma_0(l_\infty) = l_1$ \struck{\ill{}}, et itou pour $\sigma_1, \sigma_\infty$', right_nb,
    'NB has a distinct underline. The three rows carry the written subscripts and inverse exponents shown. In the crossed term at the end of the third row the infinity-shaped index survives, but the letter and exponent are entangled, so the term remains doubtful. The final sigma_infinity has no following full stop; H’s commas between separate formula rows are editorial separators.', 4,
    'readable ink left as \\ill{}', [1,5,7,9,10], cc=True, confidence='medium', marked='yes')
id_nb_underline = change('Main NB, underline', r'\uline{NB}', r'\textbf{NB}', r'\uline{NB}',
    'A separate horizontal ink stroke runs under NB; it is an authorial underline.', 5,
    'other', [10])
id_donc = change('Main NB, cancelled word after rho^3=1', r'\deleted{donc}', r'\struck{\ill{}}', r'\deleted{\unsure{donc}}',
    'The tall loop of d and rounded following o survive; the n/c region is merged with the thick cancellation. Donc is the provisional reading, not a fully resolved struck word.', 6,
    'readable ink left as \\ill{}', [2,5,7], confidence='medium', marked='yes')
id_aussi = change('Main NB, after prouve', 'ce qui prouve que', r'ce qui prouve \uncertain{aussi} que', 'ce qui prouve que',
    'Prouve ends the upper line; que starts the next. No intervening word or insertion supplies aussi.', 7,
    'text not on the page', [9], marked='yes')
id_un_mot = change('Main NB, after n’est pas', 'un mot', r'\ill{}', 'un mot',
    'Two low humps form un; the next word has the m/o run and a tall t with crossbar. The preceding n’est pas was also read directly.', 7,
    'readable ink left as \\ill{}', [2,5], marked='yes')
id_debuts = change('Compatibility paragraph, relations des débuts', 'débuts', r'\uncertain{listes}', 'débuts',
    'The opening rounded d and a further b ascender, followed by the u/t/s ending, support débuts; the shape is not listes.', 8,
    'misread word', [2], marked='yes')
deleted_first = r'\deleted{\unsure{si dans ces dernières on avait tout pris des primes}}'
id_deleted_first = change('Compatibility paragraph, first part of cancelled sentence', r'\unsure{si dans ces dernières on avait tout pris des primes}',
    r'\ill{} dans ces dernières, on \ill{} par \ill{}', deleted_first,
    'The long cancellation crosses si and the low strokes of the clause. Dans ces dernières and parts of avait, tout, pris des are recoverable; primes continues on the next line. The whole clause remains explicitly doubtful. A separate comma after dernières is not visible.', 8,
    'readable ink left as \\ill{}', [2,5,7,9], confidence='low', marked='yes', extra=(9,))
prime_formulas = r"\deleted{$l_i'=l_i^{-1}$, $\sigma_i'=\sigma_{\unsure{\dot\rho(i)}}$}"
id_prime_formulas = change('Cancelled sentence, two primed formulas', r"$l_i'=l_i^{-1}$, $\sigma_i'=\sigma_{\unsure{\dot\rho(i)}}$",
    r"$l'_i = l_i^{-1}$, $\sigma'_i = \sigma_{\rho(i)}$", prime_formulas,
    'A single raised prime follows each left-hand letter. A small dot is present above the rho-shaped index on the second right side; the cancelling line obscures part of that index, so its complete reading remains doubtful. Prime placement before or after the TeX subscript alone is not a difference.', 9,
    'misread symbol or index', [1,7], confidence='medium')
group_c = r"\deleted{\unsure{de notre groupe} $\sigma_i'$}"
group_final = r"\deleted{\unsure{de notre groupe} $\unsure{\mathcal E'|\sigma_i'}$}"
id_group = change('Cancelled phrase below i.e. sigma_i', group_c, r'\struck{\ill{}}', group_final,
    'The crossed phrase supports de notre groupe but not every letter is clear. Its final primed symbol has a broad E-like body and no separately secure i subscript. The strike can mimic an E middle stroke, so sigma_i prime is explicitly retained as an alternative. The separate cancelled i.e. sigma_i above it is preserved.', 10,
    'readable ink left as \\ill{}', [1,2,5,7], confidence='low', marked='yes')
id_ici = change('Introduction to (7)', 'Ici on a', 'Ceci dit', 'Ici on a',
    'The tall initial I, the c/i sequence, a low on, and a separate oval a precede a clear comma; there is no dit.', 11,
    'misread word', [2])
sigma_c = r"\sigma_i=\unsure{\sigma'_{\dot\rho^{-1}(i)}|\sigma^{-1}_{\dot\rho^{-1}(i)}}"
sigma_final = r"\sigma_i=\sigma'_{\dot\rho^{-1}(i)}"
id_sigma = change('Introduction to (7), sigma relation', sigma_c,
    r'\sigma_i = \sigma^{-1}_{\uncertain{\rho(i)}}', sigma_final,
    'There is one upright prime immediately above the right sigma, with no preceding minus at that height. The separate lower index has a dot above rho, an explicit -1, and (i).', 11,
    'misread symbol or index', [1], marked='yes', math='Preserves the written prime and the inverse permutation in the index; no equation was checked.')
id_j = change('Relation (7), overwritten subscript before k', r'l_{\deleted{\unsure{j}}k}', r'l_k', r'l_{\deleted{\unsure{j}}k}',
    'A long narrow downward stroke remains beneath and to the left of the heavy k. It may be the earlier j, but retracing obscures its head; cancellation and the local doubt are retained.', 12,
    'deletion state', [1,7], confidence='low')
insert_c = r'\inserted{(i,j,k)\text{ distincts}}'
insert_final = r'\inserted{(i,j,k)\text{ distincts})}'
id_insert = change('Relation (7), inserted distinctness phrase', insert_c, r'(i, j, k \text{ distincts})', insert_final,
    'The interlinear text has a closing parenthesis immediately after k and a second separate closing curve after distincts. The extra unmatched close is authorial and retained. The phrase lies above the cancelled comment.', 12,
    'insertion or placement', [3,6,10], cc=True)
id_et = change('Relation (7), cancelled et after the insertion', r'\deleted{\text{et}}', '', r'\deleted{\text{et}}',
    'A small crossed e/t group remains to the right of the inserted phrase; it is separate from the beginning of the longer deleted comment below.', 12,
    'omission', [3,7], confidence='medium')
deleted_comment = r"\deleted{\text{(et le }\unsure{\text{dernier}|\text{devenir}}\ l_{\dot\rho(i)}\ \text{s'en déduit par (1))}}"
id_comment = change('Relation (7), two-line cancelled comment', deleted_comment,
    r"\struck{(et \ill{} $l_{\rho(i)}$, \ill{} déduit par (1))}", deleted_comment,
    'The cancelled comment begins beside the exchange line and continues underneath at the right. Le is visible; the next word has a tall initial d but internal strokes remain crossed, preserving dernier/devenir. The index has a dot over rho. S’en, déduit par, and the parenthesized 1 have surviving characteristic strokes.', 12,
    'readable ink left as \\ill{}', [1,2,5,6,7], confidence='medium', marked='yes')
id_rho_action = change('Relation (7), lower formula', r'\operatorname{int}(\rho)l_i=l_{\dot\rho(i)}.',
    r'\mathrm{int}(\rho)\, l_i = l_{\rho(i)}', r'\operatorname{int}(\rho)l_i=l_{\dot\rho(i)}',
    'The rho in the subscript has a distinct dot above its loop. The closing parenthesis has no following full stop. The two-dot colon in the upper int(sigma_i) line is independently clear.', 12,
    'misread symbol or index', [1,9], cc=True)
id_generators = change('Epsilon paragraph, generator/centralizer phrase', 'étant un des générateurs du centralisateur',
    r'étant \uncertain{dans} un générateur des automorphismes', 'étant un des générateurs du centralisateur',
    'The short words un des end the first line and générateurs begins the next. Centralisateur has the c opening, the n/t run and later tall l/t strokes; automorphismes would require a different length and different descenders. There is no preceding dans.', 13,
    'misread word', [2,9], confidence='medium', marked='yes')
id_normalisateur = change('Epsilon paragraph, first parenthesis', 'normalisateur', 'normalisateurs', 'normalisateur',
    'The word ends in a short r stroke before the comma; no additional s follows it.', 13,
    'misread word', [2])
id_idem = change('Epsilon paragraph, c’est idem', r"c'est \unsure{idem|à dire}", "c'est à dire", "c'est idem",
    'The next line has a single compact idem: the d ascender and e/m ending are visible. The crop slightly clips the left edge of the initial i, which was present in the native-half reading. There are no two words à dire.', 13,
    'misread word', [2], confidence='medium')
id_E_stop = change('Epsilon paragraph, after E^+', r'$\mathcal E^+$.', r'$\mathcal{E}^{+}$', r'$\mathcal E^+$.',
    'A separate dark low dot follows the calligraphic E with its raised plus, before the next opening parenthesis.', 13,
    'omission', [3])
id_central2 = change('Epsilon paragraph, second parenthesis', 'ou le centralisateur dans', r'\uncertain{ou} le normalisateur dans', 'ou le centralisateur dans',
    'The second occurrence again begins with c and has the internal n/t and l/t ascenders of centralisateur. Ou is a short rounded pair after the opening parenthesis.', 13,
    'misread word', [2], marked='yes')
id_chgts = change('Last prose line, notation changes', 'chgts. de notation indiqués', r'relations \uncertain{inexactes}', 'chgts. de notation indiqués',
    'The initial abbreviation has c/h ascender and g descender; de and notation follow. Indiqués has the descending q and final accent/ending. The words relations inexactes are not written.', 14,
    'misread word', [2,8], marked='yes')
id_donnent = change('Last prose line, final verb', 'donnent', 'donnant', 'donnent',
    'The internal letter before the final n/t is a small closed e, not an a body; the last t has a high stem and crossbar.', 14,
    'misread word', [2])
epsilon0_c = r'\varepsilon_0=l_0^{\deleted{\unsure{-1}}}\sigma_1 l_{\unsure{1|0}}^{\deleted{\unsure{-1}}}'
epsilon0 = epsilon0_c.replace(r'\unsure{1|0}', r'\unsure{0|1}')
id_epsilon0 = change('Cancelled relation (8), first row and internal cancellations', epsilon0_c,
    r'\varepsilon_0 = l_0^{\ill{}}\, \sigma_1\, l_{\ill{}}^{\ill{}}', epsilon0,
    'Both raised regions have earlier minus/1-like strokes overwritten by local cancellation; neither exponent is certified. The last subscript is a retraced closed oval, favoring 0, with 1 retained because of overstroke. The complete first row is selected for second reading.', 15,
    'readable ink left as \\ill{}', [1,5,7], confidence='low', marked='yes')
epsilon_inf = r'\varepsilon_\infty=l_0^{-1}\sigma_0 l_\infty^{\unsure{-1}}'
id_epsilon_inf = change('Cancelled relation (8), final right exponent', epsilon_inf,
    r'\varepsilon_\infty = l_0^{-1}\, \sigma_0\, l_\infty', epsilon_inf,
    'Above the final l_infinity there is an upright 1-like stroke and a horizontal/curving mark, partly entangled with the large cancellation. The possible -1 is preserved as doubtful; it is not silently dropped.', 15,
    'omission', [1,3,7], confidence='low')
id_footer = change('Lower-left handwritten page number', r'\mspage{19}', '', r'\mspage{19}',
    'A straight 1 is followed by a looped 9 with a long descending hook. This is the physical footer number, separate from the top 8.', 16,
    'omission', [3])

decisions = []
def decide(id_, decision, reading, ink, crop_no, confidence='high', **extra):
    cr = crops[crop_no]
    x = dict(id=id_, decision=decision, reading=reading, ink=ink, crop=cr['file'], box=cr['box'], confidence=confidence)
    x.update(extra)
    return x
decisions.append(decide('M0839','first','vient du fait',
    'Vient is visible at the end of one diagonal line; du fait follows on the next, with the characteristic tall f and t. The phrase itself is not cancelled.',19,'medium'))
decisions.append(decide('M0840','undecided',r'\unsure{p.v.|p.r.}',
    'After the descending p and dot, the next letter is a shallow v-shaped pair of strokes. The r alternative cannot be excluded in this compressed abbreviation, so only the ordering of alternatives changes.',7,'low'))
decisions.append(decide('M0841','first',r"\sigma'_{\dot\rho^{-1}(i)}",
    'The right sigma bears one upright prime; its separate lower index has a dot above rho, then explicit -1 and (i). There is no minus before the sigma prime.',11))
decisions.append(decide('M0842','first','idem',
    'The word has d/e/m letter bodies and occupies one word, not à dire. The initial-i edge is slightly clipped by crop13, but was seen in the native half; the framing limitation is recorded.',13,'medium'))

unlisted = []
def unlisted_dec(source, reading, ink, crop_no, confidence='low', decision='undecided', extra=()):
    x = decide(f'U020-{len(unlisted)+1:02d}', decision, reading, ink, crop_no, confidence, source_mark=source)
    if extra: x['additional_crops'] = [crops[n]['file'] for n in extra]
    unlisted.append(x)
unlisted_dec(old_product[len(r'\deleted{$'):-2], new_product,
    'Whole cancelled product remains uncertain; the shorter second bracket is favored, but factor count and the second underbrace endpoint remain entangled. Crop23 establishes the absence of the terminal =1 supplied in C.',18,extra=(23,))
unlisted_dec(r'\unsure{(\rho\sigma_0\rho^{-1})^2}',r'\deleted{\unsure{(\rho\sigma_0\rho^{-1})^2}}',
    'The first parenthesized l_0 expression is crossed densely; several interior letter bodies and the exponent are not all independently plain.',20)
unlisted_dec(r'\unsure{\rho}',r'\deleted{\unsure{\rho}}',
    'The initial cancelled letter in the l_1 parenthesis has a rho-like loop/descender, but hatching masks its body.',21)
unlisted_dec(r'\unsure{\rho}',r'\deleted{\unsure{\rho}}',
    'The terminal cancelled letter in the l_infinity parenthesis has rho-like surviving strokes; it remains obscured.',21)
unlisted_dec(r'\unsure{l_\infty^{-1}}',r'\deleted{\unsure{l_\infty^{-1}}}',
    'In the right NB the infinity index is comparatively visible, but the cancelled letter and inverse exponent are not all plain.',4)
unlisted_dec(r'\unsure{si dans ces dernières on avait tout pris des primes}',r'\unsure{si dans ces dernières on avait tout pris des primes}',
    'The long horizontal strike crosses several low letter strokes; primes continues on the following line. Retain the whole crossed-clause doubt.',8,extra=(9,))
unlisted_dec(r"\unsure{qu'on interprète|pris les transposés}",r"\unsure{qu'on interprète}",
    'The surviving long q descender and the interprète letter run favor the first reading; pris les transposés does not fit the visible word divisions. Crossing strokes still prevent certifying every letter, so the first reading remains under unsure.',9,'medium')
unlisted_dec(r'\unsure{\dot\rho(i)}',r'\unsure{\dot\rho(i)}',
    'A dot, rho-like loop and (i) survive in the cancelled sigma formula, but the strike crosses the index body; retain the complete index doubt.',9)
unlisted_dec(r'\unsure{de notre groupe}',r'\unsure{de notre groupe}',
    'Tall d/t and the g/p descenders support the phrase, while the heavy wavering deletion passes through its lower bodies. The phrase is not fully resolved.',10)
unlisted_dec(r'\unsure{j}',r'\deleted{\unsure{j}}',
    'The overwritten index before k leaves a long thin descender, but its head is merged with the replacement.',12)
unlisted_dec(r'\unsure{\text{dernier}|\text{devenir}}',r'\unsure{\text{dernier}|\text{devenir}}',
    'The initial tall d survives; the r/n versus v/n interior remains crossed by the horizontal cancellation.',12)
unlisted_dec(r'\unsure{-1}',r'\deleted{\unsure{-1}}',
    'First l_0 exponent of (8): a short raised horizontal and upright remnant lie under dense local cancellation, insufficient to certify both signs.',15)
unlisted_dec(r'\unsure{1|0}',r'\unsure{0|1}',
    'Last l subscript in the epsilon_0 row is a dark closed oval with retracing. Prefer 0 but retain 1; no mathematical normalization is made.',15)
unlisted_dec(r'\unsure{-1}',r'\deleted{\unsure{-1}}',
    'Second l exponent of the first row of (8): local cancelling strokes obscure the supposed minus and upright 1.',15)
unlisted_dec(r'\unsure{-1}',r'\unsure{-1}',
    'The final l_infinity exponent in (8) overlaps the large cancellation curve; the -1 reading remains provisional.',15)

doubts = []
def doubt(place, reading, alternatives, reason, confidence='low'):
    doubts.append(dict(place=place, reading=reading, alternatives=alternatives, confidence=confidence, reason=reason))
doubt('Left margin, cancelled product',new_product,[short_product,long_product],
    'Diagonal hatching obscures factor boundaries and the sigma_infinity underbrace endpoint. The ending =1 is excluded by recovered blank space beyond the close bracket.')
doubt('Left margin, unreadable crossed item between the two sigma identities',r'\deleted{\illegible{1}}',[],
    'A short word-like crossed group has no securely recoverable full letter sequence. It is preserved as one illegible item.')
doubt('Left margin, cancelled first expression for l_0',r'\deleted{\unsure{(\rho\sigma_0\rho^{-1})^2}}',[r'(\rho\sigma_0\rho^{-1})^2'],
    'Crossing strokes obscure interior letters and the power; the complete expression remains doubtful.')
doubt('Left margin, cancelled first rho in l_1',r'\deleted{\unsure{\rho}}',[r'\rho'],
    'Loop/descender remnants favor rho, but the body is covered by deletion.')
doubt('Left margin, initial-rho exponent in l_infinity',r'\unsure{\rho^{\deleted{-1}}|\rho^{-1}}',[r'\rho^{\deleted{-1}}',r'\rho^{-1}'],
    'A thick zigzag favors cancellation of -1, but a live inverse remains a possible ink state. The algebraic prompt did not settle the reading.')
doubt('Left margin, cancelled terminal rho in l_infinity',r'\deleted{\unsure{\rho}}',[r'\rho'],
    'A rho-like trace remains under hatching; not every stroke is distinguishable.')
doubt('Right NB, crossed final term',r'\deleted{\unsure{l_\infty^{-1}}}',[r'l_\infty^{-1}'],
    'Index shape survives better than letter and exponent; whole term stays doubtful.')
doubt('Main NB, cancelled donc',r'\deleted{\unsure{donc}}',['donc'],
    'The d/o survive but the n/c overlap the heavy strike. This new doubt does not count as a substantive change to C.', 'medium')
doubt('Main NB, abbreviation after un mot',r'\unsure{p.v.|p.r.}',['p.v.','p.r.'],
    'The second letter is v-shaped, but a compressed r cannot be excluded.')
doubt('Compatibility paragraph, first cancelled clause',r'\unsure{si dans ces dernières on avait tout pris des primes}',['si dans ces dernières on avait tout pris des primes'],
    'The two-line cancellation intersects several letter bodies; no whole-clause certainty is claimed.')
doubt('Compatibility paragraph, cancelled qu’on interprète',r"\unsure{qu'on interprète}",["qu'on interprète"],
    'The first reading is favored, but the strike still crosses part of the q/on and subsequent letter run.', 'medium')
doubt('Compatibility paragraph, cancelled sigma index',r'\unsure{\dot\rho(i)}',[r'\dot\rho(i)'],
    'The overdot is visible but the cancelled index body is partly entangled.')
doubt('Cancelled phrase below i.e.',r'\unsure{de notre groupe}',['de notre groupe'],
    'The wavering strike crosses low portions of multiple letters.')
doubt('Cancelled final group symbol',r"\unsure{\mathcal E'|\sigma_i'}",[r"\mathcal E'",r"\sigma_i'"],
    'The body looks E-like and the prime is clear, but the cancellation could create an E middle stroke and obscure a sigma subscript.')
doubt('Relation (7), overwritten index before k',r'\deleted{\unsure{j}}',['j'],
    'A long descender is present; the head cannot be separated from retracing.')
doubt('Relation (7), cancelled comment word',r'\unsure{\text{dernier}|\text{devenir}}',['dernier','devenir'],
    'The internal r/n or v/n sequence is crossed; initial d alone does not settle it.')
doubt('Relation (8), first cancelled exponent',r'\deleted{\unsure{-1}}',['-1'],
    'Dense local cancellation prevents a fully plain minus and 1.')
doubt('Relation (8), last index in epsilon_0 row',r'\unsure{0|1}',['0','1'],
    'The closed oval favors 0 but retracing leaves 1 as an alternative.')
doubt('Relation (8), second cancelled exponent',r'\deleted{\unsure{-1}}',['-1'],
    'The raised signs are substantially overwritten.')
doubt('Relation (8), last exponent in epsilon_infinity row',r'\unsure{-1}',['-1'],
    'The horizontal/curving part overlaps a large strike; retain provisional -1.')

inventory = []
def inv(kind, position, first, box):
    element = f'E{len(inventory)+1:02d}'
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,box=box,
                          sheet_kind='text',hand='his hand',transcribed='yes'))
    return element
inv('text','Top center','8',[805,5,890,70])
inv('text','Main opening, two lines','Il revient au = de dire',[270,60,1655,222])
inv('display','Upper main, relation (4)','(4), three overbraced products',[315,215,1377,388])
inv('deletion','Relation (4), first parenthesis','cancelled rho after sigma_0',[585,285,725,380])
inv('deletion','Relation (4), second parenthesis','cancelled rho after sigma_infinity',[882,285,1020,380])
inv('deletion','Relation (4), third parenthesis','cancelled rho after sigma_1',[1170,285,1310,380])
inv('display','Upper main, relation (5)','sigma_0^2=sigma_1^2=sigma_infinity^2=1',[305,382,1090,465])
inv('display','Upper main, relation (6)','rho^3=1',[308,466,790,554])
inv('margin note','Diagonal left upper margin','Il faut ajouter les relations',[14,280,365,1160])
inv('display','Inside upper left margin','sigma_0^2=rho^3=1',[14,850,355,1155])
inv('deletion','Diagonal left margin, after la','two bracketed products and underbraces',[10,780,475,1305])
inv('margin note','Diagonal left middle margin','relation (4) est conséquence',[14,1140,365,1625])
inv('deletion','Left margin, between two parenthetical identities','one short illegible crossed item',[170,1450,355,1590])
inv('display','Left margin, l_0 calculation','l_0=... boxed product',[8,1410,380,1860])
inv('deletion','Left margin, first l_0 expression','(rho sigma_0 rho^-1)^2, doubtful',[45,1450,355,1760])
inv('display','Left margin, l_1 line','l_1=(... sigma_0 rho)^2',[14,1640,355,1930])
inv('deletion','Left margin, start of l_1 parenthesis','rho, doubtful',[135,1680,280,1875])
inv('display','Left margin, l_infinity line','l_infinity=(rho... sigma_0 ...)^2',[14,1760,355,2020])
inv('deletion','Left margin, initial rho exponent in l_infinity','-1, cancellation state uncertain',[125,1750,285,1925])
inv('deletion','Left margin, terminal l_infinity parenthesis letter','rho, doubtful',[185,1750,355,1960])
inv('display','Left margin, three final inner-conjugation lines','int(sigma_0)l_1=l_infinity',[14,1870,355,2210])
inv('margin note','Slanted right margin, upper half','underlined NB; three sigma_0 formulas; et itou',[1324,326,1664,636])
inv('deletion','Right margin, end of third formula','l_infinity^-1, doubtful',[1420,425,1664,595])
inv('text','Main NB, three lines','underlined NB Si on y fait',[270,550,1665,875])
inv('insertion','Above main sigma list','de plus',[750,550,950,620])
inv('deletion','Main NB, after rho^3=1','donc, newly doubtful',[875,690,1035,755])
inv('text','Compatibility paragraph','Tout ceci est compatible',[260,890,1665,1285])
inv('deletion','Compatibility paragraph, two-line cancellation','si dans ces dernières...; primes; two primed formulas',[260,975,1665,1168])
inv('deletion','Small separate line above crossed group phrase','i.e. sigma_i',[340,1175,590,1228])
inv('deletion','Before live si on y remplace','de notre groupe and primed symbol, doubtful',[270,1215,653,1282])
inv('text','Introduction to relation (7)','Ici on a, comme sigma_i=...',[268,1244,1006,1350])
inv('display','Main relation (7)','two-line braced exchange/action statement',[261,1308,1664,1575])
inv('deletion','Relation (7), subscript before k','j, doubtful',[900,1340,1020,1430])
inv('insertion','Above cancelled comment beside (7)','(i,j,k) distincts)',[1040,1280,1515,1380])
inv('deletion','Right of inserted distinctness phrase','et',[1500,1285,1605,1370])
inv('deletion','Right of (7), two cancelled lines','(et le dernier|devenir l_dot-rho(i) s’en déduit par (1))',[1040,1350,1664,1495])
inv('text','Main lower paragraph, six lines','On voudrait maintenant expliciter les epsilon_i',[245,1580,1665,2210])
inv('deletion','Main bottom, complete relation (8)','three epsilon formulas and relation number',[376,2183,931,2360])
inv('deletion','Within cancelled (8), first l_0 exponent','-1, doubtful and locally cancelled',[675,2183,735,2248])
inv('deletion','Within cancelled (8), last l exponent of first row','-1, doubtful and locally cancelled',[805,2183,875,2248])
inv('text','Bottom left','19',[35,2272,107,2347])

second = []
def second_box(kind, coords, reading):
    second.append(dict(box=f'B{len(second)+1:02d}', kind=kind, coords=coords, reading=reading))
second_box('Handwritten upper page number',[805,5,890,70],r'\mspage{8}')
second_box('Opening lexical disagreement and complete indexed generator list',[270,60,1655,222],
    r'Il revient au $=$ de dire que $\sigma_0,\sigma_1,\sigma_\infty,\rho$ sont des générateurs, avec relations de définition')
second_box('Complete numbered formula, three deletions, all indices and brace labels',crops[2]['box'],r'\['+rel4+r'\]')
second_box('Complete handwritten relation (5), all numeral indices and exponents',[305,382,1090,465],
    r'\[(5)\qquad \sigma_0^2=\sigma_1^2=\sigma_\infty^2=1\]')
second_box('Complete relation (6), handwritten numerals and punctuation departure',crops[3]['box'],r'\[(6)\qquad \rho^3=1\]')
second_box('Left marginal instruction and two-generator presentation; full selected margin text',[14,280,365,1160],
    r'\margin{'+margin_intro+r' On a deux gén. $\sigma_0,\rho$ en fait avec relations \[\sigma_0^2=\rho^3=1,\] la}')
second_box('Entire cancelled marginal formula, all disputed factors and underbrace labels',[10,780,475,1305],new_product)
second_box('Entire selected marginal consequence paragraph, both identities and short deletion',[14,1140,365,1625],r'\margin{'+consequence+'}')
second_box('Complete l_0 computation, deleted formula, box and all indices/exponents',[8,1410,380,1860],r'\['+l0+r'\]')
second_box('Complete l_1 and l_infinity formulas, cancelled letters and exponent-state alternative',[14,1640,355,2020],
    r'\[\begin{aligned}'+l1+r'\\'+linfty+r'\end{aligned}\]')
second_box('All three final left-margin formulas and every numerical index/exponent',[14,1870,355,2210],r'\['+conjugations+r'\]')
second_box('Complete right NB margin, underline, three formulas and doubtful crossed term',crops[4]['box'],r'\margin{'+right_nb+'}')
main_nb = r"\uline{NB} Si on y fait \inserted{de plus} $\sigma_0,\sigma_1,\sigma_\infty=1$, on trouve comme relation de définition $\rho^3=1$, \deleted{\unsure{donc}} sans plus, ce qui prouve que $\rho$ n'est pas un mot \unsure{p.v.|p.r.} aux $\sigma_i$\ldots"
second_box('Complete NB paragraph: insertion, deletion, lexical omissions, abbreviation doubt and numeric formulas',[270,550,1665,875],main_nb)
compat_deleted = r"débuts, \deleted{\unsure{si dans ces dernières on avait tout pris des primes}, et \unsure{qu'on interprète} $l_i'=l_i^{-1}$, $\sigma_i'=\sigma_{\unsure{\dot\rho(i)}}$}"
second_box('Lexical débuts and entire two-line cancelled sentence including both complete primed formulas',[260,975,1665,1168],compat_deleted)
second_box('Both separate cancelled items; complete words and formulas',crops[10]['box'],r'\deleted{i.e. $\sigma_i$} '+group_final)
second_box('Agreed live substitution with its complete inverse exponent',[650,1165,1664,1285],r'si on y remplace les $l_i$ par les $l_i^{-1}$.')
second_box('Complete introductory sentence and C-doubt formula',crops[11]['box'],r'Ici on a, comme $'+sigma_final+'$')
rel7 = r'''\[
(7)\quad\left\{\begin{aligned}
\operatorname{int}(\sigma_i)&:\text{ échange }l_j\text{ et }l_{\deleted{\unsure{j}}k}
\quad\inserted{(i,j,k)\text{ distincts})}\ \deleted{\text{et}}\\[-2pt]
&\deleted{\text{(et le }\unsure{\text{dernier}|\text{devenir}}\ l_{\dot\rho(i)}\ \text{s'en déduit par (1))}}\\
\operatorname{int}(\rho)l_i&=l_{\dot\rho(i)}
\end{aligned}\right.
\]'''
second_box('Complete relation (7), all insertions/deletions, unmatched parenthesis, numbered reference and dots',[261,1280,1664,1575],rel7)
epsilon_prose = r"On voudrait maintenant expliciter les $\varepsilon_i$ avec $\varepsilon_i^2=l_i$ $(i=0,1,\infty)$, $\varepsilon_i$ étant un des générateurs du centralisateur (ou normalisateur, c'est idem) des $L_i$ dans $\mathcal E^+$. (ou le centralisateur dans $\mathcal E$). Les calculs faits plus haut, avec les"
second_box('Complete selected epsilon prose, all lexical discrepancies, formulas and handwritten numbers',[245,1580,1665,2100],epsilon_prose)
second_box('Complete final prose line, abbreviation and lexical disagreements',crops[14]['box'],'chgts. de notation indiqués, donnent')
rel8 = r'''\deleted{\[
(8)\quad\left\{\begin{aligned}
\varepsilon_0&=l_0^{\deleted{\unsure{-1}}}\sigma_1 l_{\unsure{0|1}}^{\deleted{\unsure{-1}}}\\
\varepsilon_1&=l_\infty^{-1}\sigma_\infty l_1^{-1}\\
\varepsilon_\infty&=l_0^{-1}\sigma_0 l_\infty^{\unsure{-1}}
\end{aligned}\right.
\]}'''
second_box('Entire cancelled relation (8), three complete rows, nested deletions and every doubtful/numeric sign',crops[15]['box'],rel8)
second_box('Handwritten lower page number',crops[16]['box'],r'\mspage{19}')

coverage = []
def cover(n, ids=(), explanation=''):
    if isinstance(ids,str): ids=(ids,)
    x = dict(row=n,status='substantive' if ids else 'macro/editorial')
    if ids:
        x['change_id']=ids[0]
        if len(ids)>1: x['related_change_ids']=list(ids[1:])
    if explanation:x['explanation']=explanation
    coverage.append(x)
cover(1,explanation='Editorial scan/page-identification syntax differs; the handwritten upper 8 is retained and independently selected in B01.')
cover(2,explanation='H editorial de l’auteur is not manuscript text.')
cover(3,id_equal)
cover(4,explanation='aligned environment only.')
cover(5,id_rhos)
cover(6,explanation='H thin-space macro \\, was tokenized as a comma; no punctuation difference.')
cover(7,id_rhos)
cover(8,explanation='H thin-space macro \\, was tokenized as a comma.')
cover(9,id_rhos)
cover(10,explanation='Different boundaries of display environments.')
cover(11,explanation='Different boundaries of display environments. The agreed but unsupported final stop in (6) is separately corrected in '+id_six_stop+'.')
cover(12,(id_margin_intro,id_presentation,id_product,id_consequence,id_l0,id_l1,id_linfty,id_conjugations),
    'Large moved/fragmentary margin stretch; all left-margin content is covered by the linked loci. H’s right NB belongs to the separate right margin.')
cover(13,explanation='Display/aligned layout of the right NB only; diplomatic underline and content are audited in '+id_right_nb+'.')
cover(14,id_right_nb,'H inserts a comma to separate manuscript formula rows; final uses the manuscript row layout.')
cover(15,id_right_nb,'H inserts a comma to separate manuscript formula rows.')
cover(16,id_right_nb)
cover(17,id_right_nb)
cover(18,id_donc)
cover(19,id_aussi)
cover(20,id_un_mot)
cover(21,explanation='Difference is C’s alternative-reading apparatus. M0840 remains undecided with v-shaped letter favored; crop07 and B13 cover the entire locus. No certainty-only changes row is created.')
cover(22,explanation='Ellipsis macro/text representation and H editorial explanation of the agreed de plus insertion. The insertion itself is inventoried and included in B13.')
cover(23,id_debuts)
cover(24,id_deleted_first)
cover(25,id_deleted_first)
cover(26,id_deleted_first)
cover(27,explanation='C’s alternative phrase and prime/subscript tokenization. U020-07 retains doubtful qu’on interprète and rejects the unsupported second phrase; H already has the primary words. No certainty-only changes row.')
cover(28,explanation='Prime after subscript versus before subscript is equivalent TeX and not a manuscript difference; complete primed formulas are in B14.')
cover(29,explanation='Prime/subscript tokenization only. The substantive overdot in the same formula is separately recorded in '+id_prime_formulas+'.')
cover(30,explanation='Prime/subscript tokenization only.')
cover(31,id_group)
cover(32,id_ici)
cover(33,id_sigma)
cover(34,id_sigma)
cover(35,explanation='aligned versus cases environment only.')
cover(36,id_j)
cover(37,id_insert)
cover(38,(id_insert,id_et,id_comment))
cover(39,explanation='H thin-space macro \\, tokenized as comma; no ink punctuation is inferred.')
cover(40,id_rho_action,'Includes layout environment tokens, but the supplied C final stop and H missing overdot are substantive at this formula.')
cover(41,(id_comment,id_generators),'Moved cancelled comment and H editorial note account for the long tokenized stretch; the live On voudrait sentence follows the manuscript main text.')
cover(42,explanation='H sets the inline epsilon equation as a separate display; typesetting only, preserved as continuous manuscript prose.')
cover(43,explanation='Closing delimiter of the same H display; typesetting only.')
cover(44,id_generators)
cover(45,id_generators)
cover(46,id_generators)
cover(47,id_normalisateur)
cover(48,id_idem)
cover(49,id_E_stop)
cover(50,id_central2)
cover(51,id_chgts)
cover(52,id_donnent)
cover(53,explanation='aligned/cases and outer strike placement are macro choices; the entire display is cancelled in both witnesses and the manuscript.')
cover(54,id_epsilon0)
cover(55,explanation='H thin-space macro between factors.')
cover(56,id_epsilon0)
cover(57,id_epsilon0)
cover(58,explanation='H thin-space macro between factors.')
cover(59,explanation='H thin-space macro between factors.')
cover(60,explanation='H thin-space macro between factors.')
cover(61,(id_epsilon_inf,id_margin_intro,id_presentation,id_product,id_consequence,id_l0,id_l1,id_linfty,id_conjugations),
    'Long alignment artifact includes the last row of (8), H editorial note and moved fragmentary left margin; all substantive content is linked.')
cover(62,(id_epsilon_inf,id_conjugations),'Last doubtful exponent and H’s differently positioned margin formulas.')
cover(63,(id_footer,id_conjugations),'Physical handwritten footer 19 is substantive; H’s prose description of the margin is editorial.')

report = dict(
    scan=20, reader='reader_b', lines_read=51,
    layout='Upright main text with relations (4)–(8), a dense diagonal left-margin calculation, a shorter slanting right NB, top handwritten 8 and bottom handwritten 19. The insertion above (7), the separate small cancelled i.e. line and page-number inscriptions are counted separately; formula rows are counted as lines.',
    changes=changes, decisions=decisions, unlisted_decisions=unlisted, doubts=doubts,
    inventory=inventory, second_boxes=second,
    notation=[
        'Main relation (4) has overbraces labelled l_infinity, l_1, l_0, and three separately cancelled terminal rho factors. These are visible ink states, not substitutions justified algebraically.',
        'In the live introduction to (7), sigma bears a prime, while the lower permutation index has dot-rho^-1(i). Dot-rho(i) also appears in both relevant lines of (7). The cancelled earlier sigma formula retains an index doubt.',
        'The manuscript uses int(sigma_i): with a genuine colon, int(rho)l_i without a colon, and both int(sigma_0)l_j and int(sigma_0)(l_0) in the margin. Parentheses and punctuation are preserved locally.',
        'The l_0 result is enclosed by a real box in the left margin. There is no independent diagram or drawing on this sheet.',
        'The initial-rho exponent in the marginal l_infinity square has uncertain cancellation state. Both rho^{deleted{-1}} and live rho^-1 remain explicit; the adjacent clean l_0 exponent supplies only a graphic comparison.'
    ],
    hand=[
        'All inscriptions appear to be in his hand. The upright main prose and two slanted margins differ in orientation and density; no identifiable other hand is present.',
        'Low connecting strokes can compress several letters into shallow waves, as in un des and the p.v./p.r. abbreviation. This habit is not uniform enough to eliminate local doubts.',
        'Rho generally has a looped head and descending tail; cancellation can merge the head with hatching. The three rho deletions in (4) are more legible than the cancelled rhos in the dense lower margin.',
        'Primes can appear as single upright dark ticks. In crop11 the sigma prime is distinct from the lower index’s explicit minus and 1; H interpreted the former as an inverse.',
        'The author uses long horizontal strikes over prose and diagonal hatching over formulas. An entire passage can remain readable in outline while individual letters remain occluded; such struck doubts are retained.',
        'The last index in the epsilon_0 row is a closed retraced oval; 0 is favored but the crossing/retracing prevents excluding 1.'
    ],
    abbreviations=[
        dict(form='=', expansion='même, in the expression revient au même; expansion is not inserted into the transcription', place='Opening sentence'),
        dict(form='NB', expansion='nota bene', place='Main paragraph and right margin, both underlined'),
        dict(form='gén.', expansion='générateurs', place='Left margin, On a deux gén.'),
        dict(form='etc.', expansion='et cetera', place='Left margin after the first conjugation identity'),
        dict(form='int', expansion='inner conjugation notation; retained literally', place='Relation (7) and lower left margin'),
        dict(form='i.e.', expansion='id est', place='Separate cancelled line above de notre groupe'),
        dict(form='chgts.', expansion='changements', place='Final prose line'),
        dict(form='p.v.|p.r.', expansion='not expanded; reading of the second abbreviated letter remains open', place='Main NB, after un mot')
    ],
    notes=[
        'The physical sheet bears top number 8 and lower-left number 19, with no date. Its main text gives a presentation in sigma_0, sigma_1, sigma_infinity and rho with relations labelled (4), (5) and (6). The left note adds conjugation relations and states that two generators sigma_0 and rho suffice, with sigma_0^2=rho^3=1. These are the author’s assertions, not results proved by this reader.',
        'The main NB says that imposing sigma_0,sigma_1,sigma_infinity=1 leaves rho^3=1 and draws a conclusion that rho is not a word in the sigma_i; the abbreviated qualifier after un mot remains p.v./p.r. A struck donc is preserved provisionally. The next paragraph relates the notation to earlier relations and cancels a lengthy attempted explanation with primed symbols.',
        'Relation (7) records the exchange of l_j and l_k under int(sigma_i), with a distinctness insertion and a cancelled comment, followed by the action of rho. The insertion physically reads (i,j,k) distincts), with an extra unmatched close. That authorial punctuation is retained. The parenthetical word in the deleted comment remains dernier/devenir.',
        'The final live paragraph asks to explicate epsilon_i with epsilon_i^2=l_i for i=0,1,infinity, describing a generator of the centralizer or normalizer. The whole proposed relation (8) is cancelled, with two further local exponent cancellations. Its first-row last index and final-row exponent remain doubtful. There is no authorial date or separate interrogative doubt phrase beyond the aspirational On voudrait and the alternative descriptions in prose.',
        'The parent reader raised a mathematical prompt concerning the initial-rho exponent in the left-margin l_infinity formula. This first reader inspected the existing crop: its thick zigzag favors cancellation of -1, but a live inverse remains possible. No mathematical proof or algebraic computation was performed by this first reader, and no algebra was used to choose the ink state. Any parent algebra check is separate.',
        'Whole page and the two supplied native halves were each viewed once. Twenty-two initial saved crops covered all open or mandatory loci; one additional crop recovered only the previously uncovered ending of the cancelled marginal product. It showed blank space beyond the bracket and excluded the =1 supplied by C. No OCR, external research, other page reading, or TeX compilation was used. Root has inspected all 23 crops.',
        'The product formula remains a whole-formula doubt, with explicit shorter/longer second-bracket alternatives and no terminal =1. The crop of idem slightly clips the initial-i edge; that edge was seen during the native-half reading and the remaining d/e/m strokes identify the word. The manuscript has no isolated full stops where C supplied them after relation (6), the right NB, the last left-margin inner-conjugation formula and the lower formula of (7).',
        'The line count includes both handwritten page numbers, the separate small cancelled i.e. line, interlinear insertion at (7), and each physical formula row. The inventory explicitly accounts for every one of C’s 19 deleted spans and both inserted spans, plus the newly uncertain exponent-cancellation state. All such spans, all numeral-bearing formulas and all lexical disagreements have complete selected readings in second_boxes.'
    ],
    check_events=[], diff_coverage=coverage,
    crop_manifest=crop_meta,
    c_markup_audit=dict(deleted_spans=19, inserted_spans=2, indexed_marks=4, unlisted_unsure_occurrences=15,
                       all_accounted_in_inventory=True, all_selected_for_second_reading=True)
)

def source_macros(s, name):
    result = []
    for match in re.finditer(r'\\' + name + r'\{', s):
        k, depth = match.end(), 1
        while depth and k < len(s):
            if s[k] in '{}':
                p, slashes = k-1, 0
                while p >= 0 and s[p] == '\\':
                    slashes += 1
                    p -= 1
                if slashes % 2 == 0:
                    depth += 1 if s[k] == '{' else -1
            k += 1
        assert depth == 0
        result.append(s[match.start():k])
    return result

deleted_map = [('E04','B03'),('E05','B03'),('E06','B03'),('E11','B07'),
               ('E13','B08'),('E15','B09'),('E17','B10'),('E20','B10'),
               ('E23','B12'),('E26','B13'),('E28','B14'),('E29','B15'),
               ('E30','B15'),('E33','B18'),('E35','B18'),('E36','B18'),
               ('E38','B21'),('E39','B21'),('E40','B21')]
inserted_map = [('E25','B13'),('E34','B18')]
for macro, mapping in [('deleted',deleted_map),('inserted',inserted_map)]:
    sources = source_macros(C,macro)
    assert len(sources) == len(mapping)
    report['c_markup_audit'][macro+'_details'] = [
        dict(occurrence=n,source=source,inventory_element=element,second_box=box)
        for n,(source,(element,box)) in enumerate(zip(sources,mapping),1)
    ]
report['c_markup_audit']['new_local_state'] = dict(
    reading=r'\unsure{\rho^{\deleted{-1}}|\rho^{-1}}',
    inventory_element='E19',second_box='B10',crop=crops[21]['file'])
(OUT / '145_scan020.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(report=str(OUT/'145_scan020.json'),tex=str(OUT/'145_scan020.tex'),crops=len(crop_meta),changes=len(changes),indexed_decisions=len(decisions),unlisted_decisions=len(unlisted),doubts=len(doubts),inventory=len(inventory),second_boxes=len(second),diff_rows=len(coverage)),indent=2))
