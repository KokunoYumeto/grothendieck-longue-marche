from pathlib import Path
import csv
import json

ROOT = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
OUT = ROOT / 'edition/reader_reports'
PACKET = ROOT / 'packets/145_scan018'
manifest = json.loads((OUT / '145_scan018_crop_manifest.json').read_text())
crops = {item['name']: item for item in manifest}

top = r'''\[
(2)\quad\left\{\begin{gathered}
\sigma_0^2=\sigma_1^2=\sigma_\infty^2=1\\
\sigma_0\sigma_1=\deleted{\unsure{l_0\rho}}\inserted{\rho l_0}\qquad
\sigma_1\sigma_\infty=\deleted{\unsure{l_1\rho}}\inserted{\rho l_1}\qquad
\sigma_\infty\sigma_0=\deleted{l_\infty\rho}\inserted{\rho l_\infty}
\end{gathered}\right.
\]'''
margin_heading = r'''NB Comme $\sigma_1=\rho\sigma_0\rho^{-1}\ldots$, ces $\leftarrow$ relations s'écrivent aussi'''
trials = r'''\deleted{\[
\begin{aligned}
l_0&=(\sigma_0\rho)^2\unsure{\sigma_\infty}(\unsure{l_0\sigma_0\sigma_0\rho^{-1}})\\
l_1&=(\sigma_1\rho)^2\unsure{\sigma_1}\qquad&\unsure{l_0}&=\unsure{\rho^{-1}\sigma_0}\\
l_\infty&=(\sigma_\infty\rho)^2\unsure{\sigma_\infty}
\end{aligned}
\]}'''
identity = r'''\begin{aligned}
l_0&=\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}\\
\deleted{\unsure{\sigma_\infty}}&=\rho^{-1}[\sigma_0,\rho]
\end{aligned}'''
deleted_actions = r'''\begin{aligned}
\deleted{\sigma_0(l_0)=l_1}\\
\deleted{\sigma_0(l_1)=l_0}\\
\deleted{\sigma_0(l_\infty)=\unsure{l_1^{-1}l_0^{-1}}}
\end{aligned}'''
live_actions = r'''\begin{aligned}
\sigma_0(l_0)&=l_\infty^{-1}l_1^{-1}\\
\sigma_0(l_1)&=l_\infty\\
\sigma_0(l_\infty)&=l_1
\end{aligned}'''
margin = '\\margin{' + margin_heading + '\n' + trials + '\n' + r'''\begin{tabular}{|l}
$''' + identity + r'''$\\
On a\\
$''' + deleted_actions + r'''$\\
$\begin{aligned}
\sigma_0(l_0)&=l_\infty^{-1}l_1^{-1}\\
\sigma_0(l_1)&=l_\infty
\end{aligned}$
\end{tabular}
\[
\sigma_0(l_\infty)=l_1
\]}'''
rho_path = r'''où $\rho$, au dessus de $\dot\rho$, est défini par le chemin trivial de $P$ à $P$. On a donc'''
conjugations = r'''\[
\left\{\begin{aligned}
\rho\sigma_0\rho^{-1}&=\sigma_1\\
\rho\sigma_1\rho^{-1}&=\sigma_\infty\\
\rho\sigma_\infty\rho^{-1}&=\sigma_0
\end{aligned}\right.
\qquad\text{i.e.}\quad
\left\{\begin{aligned}
\rho\sigma_0&=\sigma_1\rho\\
\rho\sigma_1&=\sigma_\infty\rho\\
\rho\sigma_\infty&=\sigma_0\rho
\end{aligned}\right.
\]'''
relation_marks = r'''\begin{tikzpicture}[baseline=(relation.base)]
\node[inner sep=0pt,outer sep=0pt] (relation) {la relation};
\draw ([xshift=0.05em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=0.77em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=1.49em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=2.21em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=2.93em,yshift=0.35ex]relation.north west) -- ++(0.42em,0);
\draw ([xshift=0.40em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=1.12em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=1.84em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\draw ([xshift=2.56em,yshift=-0.35ex]relation.south west) -- ++(0.42em,0);
\end{tikzpicture}'''
main_open = r'''On ne voit pas apparaître d'expression de $\rho$ en fonction des $\sigma_0,\sigma_1,\sigma_\infty$ seuls --- '''
cancelled_start = r'''on voit par contre (utilisant le fait que $l_0,l_1,l_\infty$ avec '''
cancelled_middle = relation_marks + r''' fondamentale (1) est une présentation de $\unsure{\Pi|\pi}$, que \deleted{$\rho$} \inserted{$(\sigma_0\sigma_1)^3$ (p.ex.)} doit s'exprimer en fonction des $l_i$; \unsure{puisque} en outre'''
rho_trial = r'''\deleted{\[
\rho=l_0l_1l_\infty
\]}'''
live_tail = r'''il faudra que $\rho$ soit produit de termes $\sigma_i$ \uline{pas deux consécutifs} \deleted{\unsure{distincts|abstrait\textsuperscript{t}}}, \deleted{ou $\sigma_0\sigma_1\sigma_0=$} \inserted{et $\sigma$}'''
main = main_open + '\\deleted{' + cancelled_start + cancelled_middle + '\n' + rho_trial + '\n' + r'''des relations $\sigma_i^2=1$}, ''' + live_tail
dotted = r'''\[
\left\{\begin{aligned}
\dot\sigma_1^2=\dot\sigma_{\unsure{1|0}}^2=\dot\sigma_\infty^2&=1\\
\dot\sigma_0\dot\sigma_1=\dot\sigma_1\dot\sigma_\infty=\dot\sigma_\infty\dot\sigma_0&=\dot\rho\\
\dot\rho^3&=1
\end{aligned}\right.
\quad\text{est une présentation de }\unsure{\mathfrak S_3|\mathcal S_3}\text{),}
\]'''
small_margin = r'''\margin{\unsure{comme on voit} \unsure{ils sont} \unsure{\uline{pas} conjugués}}'''
que = r'''que le système des relations (1)(2) et enfin'''
rho_cube = r'''\[
\rho^3=1
\]'''
final_paragraph = r'''est une présentation de l'image inverse de $\unsure{\mathfrak S_3|\mathcal S_3}$ dans $\mathcal E$ (dis dans $\widehat{\mathcal E}$, au pt de vue profini).'''
faux = r'''\margin{C'est faux, comme on voit en faisant dans les relations $\rho=1$, \unsure{on a le groupe $(\sigma_i)$}}'''
page = '\n'.join([r'\scanpage{18}', top, margin, rho_path, conjugations, main, dotted, small_margin, que, rho_cube, final_paragraph, faux, r'\mspage{17}', ''])
(OUT / '145_scan018.tex').write_text(page, encoding='utf-8')

changes = []
def change(place, c, h, final, ink, kind, crop, c_changed=False, h_changed=True, confidence='high', marked='no', categories=(2,), consequence=''):
    cid = f's018-{len(changes)+1:02d}'
    changes.append(dict(id=cid, place=place, C=c, H=h, final=final, ink=ink, confidence=confidence, kind=kind, c_changed=c_changed, h_changed=h_changed, marked_in_H=marked, crop=crops[crop]['crop'], box=crops[crop]['box'], error_category=list(categories), math_consequence=consequence))
    return cid

c01=change('Upper display (2), three overwritten right members', r'\deleted{\unsure{l_0\rho}}\inserted{\rho l_0}; \deleted{\unsure{l_1\rho}}\inserted{\rho l_1}; \deleted{l_\infty\rho}\inserted{\rho l_\infty}', r'\rho\,l_0; \rho\,l_1; \rho\,l_\infty', r'\deleted{\unsure{l_0\rho}}\inserted{\rho l_0}; \deleted{\unsure{l_1\rho}}\inserted{\rho l_1}; \deleted{l_\infty\rho}\inserted{\rho l_\infty}', 'Three old products are physically cancelled. The first two are blackened and remain doubtful; the third has a readable looped l, two-lobed infinity and descending rho. The new rho precedes each l; the first replacement is below, the other two above. H relegates the old inscriptions to an editorial note.', 'deletion state', 'top_system', confidence='medium', marked='yes', categories=(6,7), consequence='Records the change in multiplication order without recovering obscured old indices as certain.')
c02=change('Upper display (2), separators after the first two new products', r'\rho l_0\qquad\sigma_1\sigma_\infty=\rho l_1\qquad', r'\rho\,l_0,\qquad\sigma_1\sigma_\infty=\rho\,l_1,\qquad', r'\rho l_0\qquad\sigma_1\sigma_\infty=\rho l_1\qquad', 'There is blank space, not a detached comma, after either replacement product.', 'text not on the page', 'top_system', categories=(9,))
c03=change('Right-margin NB heading, end of the conjugation example', r'\rho\sigma_0\rho^{-1}\ldots', r'\rho\sigma_0\rho^{-1}', r'\rho\sigma_0\rho^{-1}\ldots', 'Small successive dots follow the inverse exponent before the prose continues.', 'omission', 'margin_trials', categories=(3,))
c04=change('Right-margin NB heading, immediately before relations', r'ces relations', r'ces relations', r'ces $\leftarrow$ relations', 'A short shaft with a left-pointing head precedes relations; it is independent of the letters.', 'drawing or diagram', 'margin_trials', c_changed=True, categories=(3,4))
c05=change('Right margin, three cancelled trial rows and a side trial', r'l_0=(\sigma_0\rho)^2\unsure{\sigma_\infty}(\unsure{l_0\sigma_0\sigma_0\rho^{-1}})\\l_1=(\sigma_1\rho)^2\unsure{\sigma_1}\\l_\infty=(\sigma_\infty\rho)^2\unsure{\sigma_\infty}\\\unsure{l_0}=\unsure{\rho^{-1}\sigma_0}', r'\struck{\ill{}}', trials, 'The three leading l-indices, parenthesized sigma-rho products and superscript 2s remain recognizable through the hatching. The later symbols remain doubtful. The small l0=rho^-1 sigma0 trial sits to the right of the second row, not on a fourth baseline.', r'readable ink left as \ill{}', 'margin_trials', c_changed=True, confidence='low', marked='yes', categories=(5,6,7))
c06=change('Right-margin live identity, cancelled lower-left annotation', r'l_0=\underbrace{\rho^{-1}\sigma_0}_{\deleted{\unsure{\sigma_\infty}}}\rho\sigma_0\rho^{-1}=\rho^{-1}[\sigma_0,\rho]', r'$l_0=\rho^{-1}\sigma_0\rho\sigma_0\rho^{-1}$, \struck{\ill{}} $=\rho^{-1}[\sigma_0,\rho]$', identity, 'The live equality occupies two rows. The cancelled sigma-like trace lies left of the lower equality. No U-shaped underbrace is visible beneath rho^-1 sigma0, and there is no comma ending the upper row. Its exact attachment remains uncertain.', 'insertion or placement', 'margin_identity', c_changed=True, confidence='medium', marked='yes', categories=(5,6,7,9))
c07=change('Right margin, tall separator beside the identity and action calculations', '', '', r'\begin{tabular}{|l}'+identity+r'\\ On a\\'+deleted_actions+r'\\ \sigma_0(l_0)=l_\infty^{-1}l_1^{-1}\\ \sigma_0(l_1)=l_\infty\end{tabular}', 'A tall ruled stroke begins beside the live identity and continues beside the action calculations, ending near the second live action row. The saved identity crop covers its upper part and the actions crop its lower part. H mentions it editorially but does not reproduce it.', 'drawing or diagram', 'margin_actions', c_changed=True, categories=(3,4))
c08=change('Right margin, between the identity and the action trials', 'On a', r'\ill{} —', 'On a', 'A closed O, following n and separate a are readable. There is no literal em dash after these words.', r'readable ink left as \ill{}', 'margin_actions', marked='yes', categories=(5,9))
c09=change('Right margin, three cancelled action trials', r'\deleted{\sigma_0(l_0)=l_1;\ \sigma_0(l_1)=l_0;\ \sigma_0(l_\infty)=\unsure{l_1^{-1}l_0^{-1}}}', '', deleted_actions, 'Three crossed rows precede the live action formulas. The first two right members l1 and l0 are readable; the crowded inverse product in the third is retained as doubtful.', 'omission', 'margin_actions', confidence='medium', marked='yes', categories=(3,7))
c10=change('Right margin, first live action', r'\sigma_0(l_0)=l_\infty^{-1}l_1^{-1}', r'\sigma_0(l_0)=l_0^{-1}l_1^{-1}', r'\sigma_0(l_0)=l_\infty^{-1}l_1^{-1}', 'The first right-member index has two connected lobes, not the single oval of 0. Both inverse exponents are present.', 'misread symbol or index', 'margin_actions', categories=(1,), consequence='Changes the first inverse factor in the displayed action.')
c11=change('Right margin, punctuation between the three live action rows', r'\sigma_0(l_0)=l_\infty^{-1}l_1^{-1}\\\sigma_0(l_1)=l_\infty\\\sigma_0(l_\infty)=l_1', r'$\sigma_0(l_0)=l_0^{-1}l_1^{-1}$, $\sigma_0(l_1)=l_\infty$, $\sigma_0(l_\infty)=l_1$', live_actions, 'The three equalities occupy separate rows; no detached comma follows the first or second right member. The factor correction is separately recorded.', 'text not on the page', 'margin_actions', categories=(9,))
c12=change('Main text, after the first rho in où rho', r'où $\rho$,', r'où $\rho$', r'où $\rho$,', 'A dark short curved comma follows the first rho.', 'omission', 'rho_path', categories=(3,))
c13=change('Main text, au dessus', 'au dessus', r'\uncertain{au-dessus}', 'au dessus', 'The two words are separated by plain space; there is no hyphen.', 'abbreviation expanded or spelling modernised', 'rho_path', marked='yes', categories=(8,9))
c14=change('Main text, second rho after de', r'de $\dot\rho$', r'de $\rho$', r'de $\dot\rho$', 'A discrete dark dot stands above the second looped rho.', 'misread symbol or index', 'rho_path', categories=(1,), consequence='Preserves the distinction between rho and its dotted image.')
c15=change('Main text, chemin trivial de P à P', 'chemin trivial de', r'chemin direct \uncertain{de}', 'chemin trivial de', 'The word begins with crossed t and r, then the narrow i-v-i sequence, followed by a and tall l. The following de is plain.', 'misread word', 'rho_path', marked='yes', categories=(2,), consequence='Names the path trivial rather than direct.')
c16=change('Right-hand conjugation system, final rho', r'\rho\sigma_\infty=\sigma_0\rho.', r'\rho\sigma_\infty=\sigma_0\rho', r'\rho\sigma_\infty=\sigma_0\rho', 'No detached full stop follows the descending final rho.', 'text not on the page', 'conjugation_system', c_changed=True, h_changed=False, categories=(9,))
c17=change('Opening of the large cancellation, par contre', 'on voit par contre', r'on voit en \ill{}', 'on voit par contre', 'The first word has the descender of p and a following a-r; contre has a rounded c/o start, n and crossed t before r-e.', 'misread word', 'contre', marked='yes', categories=(2,5))
c18=change('Cancelled argument, after l0,l1,linfty and before avec', r'$l_0,l_1,l_\infty$ avec', r'$l_0,l_1,l_\infty$ \ill{} $\sigma$ \ill{} avec', r'$l_0,l_1,l_\infty$ avec', 'No independent sigma on the text baseline intervenes between the final l-infinity and avec. The nearby oblique strokes belong to the cancellation.', 'text not on the page', 'contre', marked='yes', categories=(9,))
c19=change('Cancelled argument, singular relation and verb', 'la relation fondamentale (1) est une', 'les relations fondamentales (1) sont une', 'la relation fondamentale (1) est une', 'The article ends a; relation and fondamentale have no final s. After (1) the short e-s-t sequence is visible, rather than s-o-n-t.', 'misread word', 'crossed_relation_and_cube', categories=(2,))
c20=change('Cancelled argument, group letter after présentation de', r'$\pi$', r'$\Pi$', r'$\unsure{\Pi|\pi}$', 'The sign is tall, with a horizontal top and two substantial descending legs; the right foot is curved. The tall capital-shaped outline is preferred, with case left locally doubtful.', 'misread symbol or index', 'crossed_relation_and_cube', c_changed=True, h_changed=False, confidence='medium', categories=(1,), consequence='Records the written group-name alphabet without a global case normalization.')
c21=change('Cancelled argument, short marks above and below la relation', 'la relation', 'la relation', relation_marks, 'Five short separate horizontal strokes are above the phrase and four below. Their geometry is retained without assigning them the function of emphasis or cancellation; the long oblique cancellation is separate.', 'drawing or diagram', 'crossed_relation_and_cube', c_changed=True, confidence='medium', categories=(3,4))
c22=change('Cancelled argument, rho replaced above by the cube example', r'que \deleted{$\rho$} \inserted{$(\sigma_0\sigma_1)^3$ (p.ex.)} doit', r"que $\rho$ doit s'exprimer en fonction des $l_i$, $\rho$ \uncertain{puissance} \ill{} $(\sigma_0\sigma_1)^3$ (p. ex.)", r'que \deleted{$\rho$} \inserted{$(\sigma_0\sigma_1)^3$ (p.ex.)} doit', 'The old rho after que has its own strike. The parenthesized sigma product, exponent 3 and (p.ex.) sit above this local replacement position, not after the subsequent sentence.', 'insertion or placement', 'crossed_relation_and_cube', marked='yes', categories=(6,7))
c23=change('Cancelled argument, immediately after li', r'$l_i$; \unsure{puisque}', r'$l_i$, $\rho$ \uncertain{puissance}', r'$l_i$; \unsure{puisque}', 'A comma-like lower stroke and point form the punctuation after li. The supposed extra rho has no independent baseline body; it is supplied by a descender and an oblique crossing. Puisque remains crossed and locally uncertain.', 'text not on the page', 'crossed_relation_and_cube', confidence='medium', marked='yes', categories=(9,10))
c24=change('Cancelled argument, puisque en outre', r'\unsure{puisque} en outre', r'\uncertain{puissance} \ill{}', r'\unsure{puisque} en outre', 'The word has the compact proposed puisque outline under a crossing, but not every letter is plain. The following en outre is readable; the extra ance required by puissance is not supported.', 'misread word', 'crossed_relation_and_cube', confidence='medium', marked='yes', categories=(2,5))
c25=change('Cancelled continuation before sigma_i squared', r'des relations $\sigma_i^2=1$', r'\ill{} $\sigma_i^2=1$', r'des relations $\sigma_i^2=1$', 'The d-e-s start and the long relation(s) sequence remain visible despite the oblique strikes; the sigma, index i, superscript 2, equals sign and 1 are readable.', r'readable ink left as \ill{}', 'rho_deletion_and_faudra', marked='yes', categories=(5,))
c26=change('Main text, live continuation il faudra que rho soit', r'\deleted{il faudra que $\rho$ soit}', r'il faudrait que $\rho$ soit', r'il faudra que $\rho$ soit', 'The oblique cancellation ends to the left, over des relations sigma_i²=1. The right-hand phrase is not crossed. Faudra ends with a, with no final i-t sequence.', 'deletion state', 'rho_deletion_and_faudra', c_changed=True, categories=(2,7))
c27=change('Main text, produit de termes sigma_i', r'\deleted{produit de termes $\sigma_i$}', r'produit de termes $\sigma_i$', r'produit de termes $\sigma_i$', 'The phrase and sigma_i are locally unstruck; the line to the left is the initial p descender, not a strike through this text.', 'deletion state', 'pas_and_struck_ending', c_changed=True, h_changed=False, categories=(7,))
c28=change('Main text, underlined pas deux consécutifs', r'\deleted{pas \uline{deux consécutifs}}', r'\uncertain{pris} deux consécutifs', r'\uline{pas deux consécutifs}', 'The short word has p-a-s, not the extra r and i of pris. The separate underline begins beneath pas and runs beneath deux consécutifs. The words are outside the long cancellation.', 'misread word', 'pas_and_struck_ending', c_changed=True, marked='yes', categories=(2,7,10))
c29=change('Lower local cancellation, word before the comma', r'\deleted{\unsure{abstrait\textsuperscript{t}|distincts}}', r'\struck{\uncertain{abstraitement}}', r'\deleted{\unsure{distincts|abstrait\textsuperscript{t}}}', 'The opening loop and upright favor d, and the crossed sequence favors distincts. Several medial letters are traversed by the horizontal strike, so the alternate abbreviated reading is retained rather than resolved.', 'misread word', 'pas_and_struck_ending', c_changed=True, confidence='low', marked='yes', categories=(2,7,8))
c30=change('Lower local cancellation, ou and the unfinished sigma equality', r'\deleted{ou $\sigma_0\sigma_1\sigma_0=$}', r'\struck{\ill{} $\sigma_0\sigma_1\sigma_0=$},', r'\deleted{ou $\sigma_0\sigma_1\sigma_0=$}', 'A small o-u sequence precedes the three sigma factors; the horizontal strike continues through the unfinished equality. The visible comma is after the preceding cancelled word, not after this equals sign.', r'readable ink left as \ill{}', 'pas_and_struck_ending', marked='yes', categories=(5,7,9))
c31=change('Lower main text, live et sigma above/right of the unfinished equality', r'\deleted{\unsure{et $\sigma$}}', r'et \uncertain{$\sigma$}', r'\inserted{et $\sigma$}', 'The e and crossed t are readable beside a sigma with curved body and top stroke. They are unstruck and sit above/right of the struck ou equality. Their exact replacement attachment is not asserted.', 'insertion or placement', 'pas_and_struck_ending', c_changed=True, confidence='medium', marked='yes', categories=(6,7))
c32=change('Dotted presentation, first squared sigma index', r'\dot\sigma_{\unsure{1|0}}^2', r'\dot\sigma_0^2', r'\dot\sigma_1^2', 'The first index is a narrow upright with a small foot, not a closed oval. It is retained as 1 even though this repeats the preferred following index.', 'misread symbol or index', 'dotted_presentation', categories=(1,), consequence='The first two squared symbols are not silently regularized to indices 0 and 1.')
c33=change('Small slanted margin below the dotted-rho cube', r'\margin{\unsure{comme on voit} \unsure{ils sont} \unsure{pas conjugués}}', r'\marginal{\uncertain{\ill{} en \ill{}}}', small_margin, 'The three compressed lines support the tentative C phrases but not every letter is distinct. A separate short horizontal line lies directly under pas. A further short terminal stroke near conjugués has uncertain status and is not extended into a continuous underline.', r'readable ink left as \ill{}', 'small_margin', c_changed=True, confidence='low', marked='yes', categories=(5,10))
c34=change('Continuation after the dotted presentation, le système', 'que le système', 'que les symétries', 'que le système', 'The article is le without a final s; système has the long y descender and the t crossing, and lacks the r-i sequence needed for symétries.', 'misread word', 'que_systeme', categories=(2,))
c35=change('Continuation after references (1)(2), enfin', 'et enfin', r'et \uncertain{autres}', 'et enfin', 'The small e-n beginning is followed by the tall f and narrow i-n ending; the a-u-t-r sequence of autres is absent.', 'misread word', 'que_systeme', marked='yes', categories=(2,))
c36=change('Final paragraph, est une présentation', 'est une présentation', r'\uncertain{donnent} une présentation', 'est une présentation', 'The brief e-s-t opening is followed by une; there is no long doubled-n ending of donnent.', 'misread word', 'final_paragraph', marked='yes', categories=(2,))
c37=change('Final paragraph, parenthetical dis dans', 'dis dans', 'ou dans', 'dis dans', 'Inside the opening parenthesis a tall looped d precedes the small i and s; this is not a rounded o-u pair.', 'misread word', 'final_paragraph', categories=(2,8))
c38=change('Lower-left oblique note, punctuation after C\'est faux', "C'est faux,", "C'est faux (+)", "C'est faux,", 'The cross is the terminal x of faux. A dark comma follows it; there is no separate parenthesized plus sign.', 'text not on the page', 'faux_margin', categories=(3,9))
c39=change('Lower-left oblique note, en faisant dans les', 'comme on voit en faisant dans les relations', r'comme on \uncertain{voit} \ill{} \ill{} relations \ill{}', 'comme on voit en faisant dans les relations', 'The tall f of faisant and its following short connected letters are readable; dans and les follow on the same oblique baseline before relations. Voit has the v opening, dotted i and crossed t.', r'readable ink left as \ill{}', 'faux_margin', marked='yes', categories=(5,))
c40=change('Lower-left oblique note, final crowded clause', r'\unsure{on a le groupe $(\sigma_i)$}', r'\ill{} $\sigma_0\rho(\uncertain{?})=\ill{}$', r'\unsure{on a le groupe $(\sigma_i)$}', 'The baseline permits on a le groupe and a parenthesized sigma with small index, but overlap prevents a secure letter-by-letter reading. H\'s extra rho and equality do not have independent clear strokes; the entire proposed clause stays doubtful.', 'misread symbol or index', 'faux_margin', confidence='low', marked='yes', categories=(1,2,5,9))
c41=change('Lower-left oblique note, end punctuation', r'\unsure{on a le groupe $(\sigma_i)$}.', r'\ill{} $\sigma_0\rho(\uncertain{?})=\ill{}$', r'\unsure{on a le groupe $(\sigma_i)$}', 'There is no dark separate full stop following the crowded terminal parenthesis. The other differences in the clause are recorded separately.', 'text not on the page', 'faux_margin', c_changed=True, h_changed=False, confidence='medium', categories=(9,))
c42=change('Lower-right manuscript page number', r'\mspage{17}', '', r'\mspage{17}', 'A tall 1 and a crossed 7 are separately visible above the bottom edge. This is a handwritten source number, not H\'s editorial page identification.', 'omission', 'footer17', categories=(3,))

decisions=[]
def decision(target, ident, decision_type, reading, ink, crop, confidence='medium', **extra):
    target.append(dict(id=ident, decision=decision_type, reading=reading, ink=ink, crop=crops[crop]['crop'], box=crops[crop]['box'], confidence=confidence, **extra))
decision(decisions,'M0825','first','1','The first dotted-sigma index is an upright narrow stroke with a foot; no oval closes around it.','dotted_presentation','high')
decision(decisions,'M0826','undecided',r'\unsure{1|0}','The second index is narrow and bent, favoring 1, but less distinctly formed than the first.','dotted_presentation')
decision(decisions,'M0827','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The large ornate S has a rounded outer sweep and hooked upper end; this local glyph does not securely distinguish the two typographic alphabets.','dotted_presentation')
decision(decisions,'M0828','undecided',r'\unsure{comme on voit}','The connected first slanted line permits the offered words, but several joins do not separate into certain letters.','small_margin','low')
decision(decisions,'M0829','undecided',r'\unsure{ils sont}','The short middle line is compressed and partly adjacent to the display; the individual letters remain uncertain.','small_margin','low')
decision(decisions,'M0830','undecided',r'\unsure{\uline{pas} conjugués}','Pas has its own short independent underline. The following word remains crowded; a terminal horizontal stroke may belong to its ending or to a second short underline.','small_margin','low')
decision(decisions,'M0831','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The final ornate S repeats the broad rounded and hooked outline, without a decisive local alphabet distinction.','final_paragraph')
decision(decisions,'M0832','undecided',r'\unsure{on a le groupe $(\sigma_i)$}','The opening short words and looped group-word outline are plausible; the final parenthesized symbols overlap other writing and remain uncertain.','faux_margin','low')

unlisted=[]
unlisted_spec=[
 ('Upper display, first cancelled old product',r'\unsure{l_0\rho}',r'\unsure{l_0\rho}','The loops and lower index are traversed by heavy local strokes.','top_system','low','undecided'),
 ('Upper display, second cancelled old product',r'\unsure{l_1\rho}',r'\unsure{l_1\rho}','The narrow proposed index and rho body are blackened by the cancellation.','top_system','low','undecided'),
 ('First marginal trial, trailing sigma',r'\unsure{\sigma_\infty}',r'\unsure{\sigma_\infty}','The sigma body and proposed infinity are overlaid by dense hatching.','margin_trials','low','undecided'),
 ('First marginal trial, parenthetic product',r'\unsure{l_0\sigma_0\sigma_0\rho^{-1}}',r'\unsure{l_0\sigma_0\sigma_0\rho^{-1}}','The sequence has crossed loops, with the internal indices and final inverse insufficiently separate.','margin_trials','low','undecided'),
 ('Second marginal trial, trailing sigma',r'\unsure{\sigma_1}',r'\unsure{\sigma_1}','A sigma-like top is visible but its index is obscured by local crossing strokes.','margin_trials','low','undecided'),
 ('Third marginal trial, trailing sigma',r'\unsure{\sigma_\infty}',r'\unsure{\sigma_\infty}','The trailing body and subscript are crossed; every component cannot be certified.','margin_trials','low','undecided'),
 ('Small side trial beside second marginal row, left member',r'\unsure{l_0}',r'\unsure{l_0}','The small looped l and lower round trace are crowded into the side of the row.','margin_trials','low','undecided'),
 ('Small side trial beside second marginal row, right member',r'\unsure{\rho^{-1}\sigma_0}',r'\unsure{\rho^{-1}\sigma_0}','The compact superscript and final index are entangled with crossing strokes.','margin_trials','low','undecided'),
 ('Cancelled lower-left trace beside the live marginal identity',r'\unsure{\sigma_\infty}',r'\unsure{\sigma_\infty}','A sigma-like body and possible infinity remain crossed. Its lower-left position is visible but an underbrace is not.','margin_identity','low','undecided'),
 ('Third cancelled marginal action, right member',r'\unsure{l_1^{-1}l_0^{-1}}',r'\unsure{l_1^{-1}l_0^{-1}}','The product is small and struck; the exponent strokes cannot all be separated from the cancellation.','margin_actions','low','undecided'),
 ('Large cancelled argument, puisque',r'\unsure{puisque}',r'\unsure{puisque}','The compact word is compatible with puisque, but its middle is crossed and not every letter is plain.','crossed_relation_and_cube','medium','undecided'),
 ('Lower cancelled word',r'\unsure{abstrait\textsuperscript{t}|distincts}',r'\unsure{distincts|abstrait\textsuperscript{t}}','The opening loop and tall stroke favor d and the short terminal sequence favors distincts; the horizontal strike still masks medial letters.','pas_and_struck_ending','low','undecided'),
 ('Live words above/right of the lower unfinished equality',r'\unsure{et $\sigma$}',r'et $\sigma$','The e, crossed t and sigma body/top stroke are all visible and are not crossed. The exact replacement attachment remains separately doubtful.','pas_and_struck_ending','high','first'),
]
for n,(place,original,reading,ink,crop,confidence,decision_type) in enumerate(unlisted_spec,1):
    decision(unlisted,f'U018-{n:02d}',decision_type,reading,ink,crop,confidence,place=place,C_mark=original)

doubts=[]
def doubt(place, reading, alternatives, reason, confidence='low'):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
for u in unlisted:
    if u['decision']=='undecided':
        doubt(u['place'],u['reading'],['reading retained as tentative; obscured ink not supplied as certain'],u['ink'],u['confidence'])
doubt('Cancelled lower-left marginal sigma trace, attachment',r'\deleted{\unsure{\sigma_\infty}}',['lower-left annotation beside the second equality','annotation attached to a preceding factor'],'The trace is lower-left of the live second equality; no actual underbrace fixes its attachment.')
doubt('Group letter after présentation de in the large cancellation',r'\unsure{\Pi|\pi}',[r'\Pi',r'\pi'],'Tall two-legged outline favors Pi, but the curved right foot leaves case locally uncertain.','medium')
doubt('Short horizontal marks surrounding la relation',relation_marks,['unassigned graphic strokes','possible emphasis or cancellation-related marks'],'Five short upper strokes and four lower strokes are preserved geometrically; their function is not readable from the local arrangement.','medium')
doubt('Live et sigma, exact attachment',r'\inserted{et $\sigma$}',['addition above/right of the struck equality','replacement for some or all of the struck ou clause'],'The text is readable and live; its elevated position does not uniquely specify the scope of replacement.','medium')
for d in decisions:
    if d['decision']=='undecided':
        doubt(d['id'],d['reading'],['the alternatives or tentative phrase displayed in the reading'],d['ink'],d['confidence'])
doubt('Small margin, short stroke near the end of conjugués',r'\unsure{\uline{pas} conjugués}',['terminal writing stroke','second short underline below the last syllable'],'The line under pas is distinct. A later short horizontal stroke may be a second line, but its independence and scope are not secure; it is not extended across the absent intervening space.')

inventory=[]
def inv(kind,position,first,box):
    inventory.append(dict(element=f'I{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=first,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('display','Top main column',r'(2), \sigma_0^2=\sigma_1^2=\sigma_\infty^2=1 and three product equations',[300,50,1278,281])
inv('deletion','First top right member',r'\deleted{\unsure{l_0\rho}}',[485,174,656,243])
inv('insertion','Below first top right member',r'\inserted{\rho l_0}',[492,223,665,281])
inv('deletion','Second top right member',r'\deleted{\unsure{l_1\rho}}',[800,171,957,244])
inv('insertion','Above second top right member',r'\inserted{\rho l_1}',[795,121,959,183])
inv('deletion','Third top right member',r'\deleted{l_\infty\rho}',[1095,177,1278,246])
inv('insertion','Above third top right member',r'\inserted{\rho l_\infty}',[1095,121,1278,182])
inv('margin note','Upper-right heading','NB Comme ... ces relations s\'écrivent aussi',[1309,48,1678,166])
inv('drawing','Upper-right heading before relations',r'\leftarrow',[1309,87,1435,153])
inv('deletion','Upper-right three trial rows',trials,[1332,143,1678,329])
inv('deletion','To the right of the second cancelled trial',r'\unsure{l_0}=\unsure{\rho^{-1}\sigma_0}',[1515,209,1678,288])
inv('display','Right margin below trials',identity,[1330,294,1678,419])
inv('deletion','Lower-left of the second marginal equality',r'\deleted{\unsure{\sigma_\infty}}',[1390,353,1490,413])
inv('drawing','Left boundary beside the marginal identity and actions','Tall vertical separator with upper curved sweep; ends near second live action row',[1370,294,1422,644])
inv('text','Right margin above action trials','On a',[1390,391,1538,446])
inv('deletion','Right margin, three action trials',deleted_actions,[1395,436,1678,558])
inv('display','Right margin, three live action rows',live_actions,[1390,547,1678,707])
inv('text','Main column, two lines below (2)',rho_path,[246,292,1377,472])
inv('display','Upper-middle main column, two conjugation systems',conjugations,[407,500,1230,791])
inv('text','Main column before long cancellation',main_open,[223,798,1602,977])
inv('deletion','Main column from on voit through des relations sigma_i²=1',cancelled_start+cancelled_middle+' '+rho_trial+r' des relations $\sigma_i^2=1$',[224,933,1585,1565])
inv('drawing','Above and below la relation in the cancelled argument','Five short upper strokes and four short lower strokes',[385,1080,795,1178])
inv('deletion','After que in the cancelled argument',r'\deleted{$\rho$}',[775,1183,941,1288])
inv('insertion','Above the deleted rho after que',r'\inserted{$(\sigma_0\sigma_1)^3$ (p.ex.)}',[875,1075,1480,1219])
inv('deletion','Locally struck display within the large cancellation',rho_trial,[525,1397,908,1498])
inv('deletion','Final cancelled continuation at left','des relations sigma_i²=1',[249,1455,839,1565])
inv('text','Unstruck continuation at right and on the following line',r'il faudra que $\rho$ soit produit de termes $\sigma_i$',[252,1455,1590,1697])
inv('text','End of product phrase, underlined',r'\uline{pas deux consécutifs}',[950,1570,1566,1660])
inv('deletion','Lower local cancelled word',r'\deleted{\unsure{distincts|abstrait\textsuperscript{t}}}',[252,1686,543,1778])
inv('deletion','After the lower cancelled word and comma',r'\deleted{ou $\sigma_0\sigma_1\sigma_0=$}',[620,1686,1030,1768])
inv('insertion','Above/right of the unfinished local equality',r'\inserted{et $\sigma$}',[1040,1632,1285,1719])
inv('display','Lower main column, three-row dotted presentation',dotted,[420,1776,1620,2013])
inv('text','To the right of the dotted presentation',r'est une présentation de $\unsure{\mathfrak S_3|\mathcal S_3}$),',[1050,1845,1620,2013])
inv('margin note','Slanted note beneath dotted-rho cube',small_margin,[460,1899,818,2049])
inv('text','Main continuation after the dotted presentation',que,[270,2012,1620,2118])
inv('display','Main column before final two prose lines',rho_cube,[550,2118,1400,2188])
inv('text','Final two main prose lines',final_paragraph,[240,2188,1627,2348])
inv('margin note','Oblique lower-left corner',faux,[38,2010,550,2344])
inv('text','Lower-right manuscript number',r'\mspage{17}',[1530,2280,1643,2351])

second=[]
def sb(kind,coords,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,coords=coords,reading=reading))
sb('Complete numbered formula (2), all three local deletions and insertions, numeric indices and exponents',[300,50,1278,281],top)
sb('Entire right-margin note, arrow, all numeric formulas and trials, cancellation, uncertain attachment and separator',[1309,48,1678,707],margin)
sb('Lexical differences, punctuation and dotted rho in the path explanation',[246,292,1377,472],rho_path)
sb('Full paired conjugation systems, all numeric indices and inverse exponents, final punctuation',[407,500,1230,791],conjugations)
sb('Opening main paragraph and beginning of cancellation, all sigma/l indices and par contre disagreement',[223,798,1602,1088],main_open+r'\deleted{on voit par contre (utilisant le fait que $l_0,l_1,l_\infty$}')
sb('Cancelled argument, reference (1), short graphic strokes, group-letter doubt, rho deletion and cube insertion',[224,1075,1585,1390],r'\deleted{avec '+cancelled_middle+r'}')
sb('Locally and globally cancelled rho formula, numeric relations, end of cancellation, live il faudra',[249,1397,1590,1565],r'\deleted{'+rho_trial+r' des relations $\sigma_i^2=1$}, il faudra que $\rho$ soit')
sb('Live product phrase and underline, both local cancellations, all sigma indices, elevated et sigma',[252,1570,1566,1778],r'produit de termes $\sigma_i$ \uline{pas deux consécutifs} \deleted{\unsure{distincts|abstrait\textsuperscript{t}}}, \deleted{ou $\sigma_0\sigma_1\sigma_0=$} \inserted{et $\sigma$}')
sb('Full dotted presentation, all numeric indices and exponents, ornate S3 alphabet and closing punctuation',[420,1776,1620,2013],dotted)
sb('Complete small slanted margin, all tentative words and separate underline',[460,1899,818,2049],small_margin)
sb('System/ending lexical disagreements and references (1)(2)',[270,2012,1620,2118],que)
sb('Complete final rho-cube equation with handwritten exponent and right member',[550,2118,1400,2188],rho_cube)
sb('Full final two prose lines, S3 index/alphabet, hats, est/dis disagreements, abbreviation and punctuation',[240,2188,1627,2348],final_paragraph+'\n'+r'\mspage{17}')
sb('Entire lower-left oblique note, all word/formula disagreements, rho=1 and uncertain sigma index',[38,2010,550,2344],faux)
sb('Handwritten footer number omitted by H',[1530,2280,1643,2351],r'\mspage{17}')

diff_map={
 1:('macro/editorial',None,'C scan identification is editorial, not a source inscription.'),
 2:('macro/editorial',None,'gathered/cases syntax describes the same brace and rows.'),
 3:('substantive',[c01,c02],'Top rewritten products and added H separators; tokenizer splits the states.'),
 4:('substantive',[c01,c02],'Same first overwritten product and non-source comma.'),
 5:('substantive',[c01,c02],'Same second overwritten product and non-source comma.'),
 6:('substantive',[c01,c02],'Same second overwritten product and non-source comma.'),
 7:('substantive',[c01],'The three old products and their replacement positions are source states; H puts the description in an editorial note.'),
 8:('macro/editorial',None,'Continuation of H editorial prose about the overwritten top products; source states covered in s018-01.'),
 9:('macro/editorial',None,'Comma in H editorial list, not manuscript punctuation.'),
 10:('substantive',[c03,c04,c05,c06,c07],'Long alignment artifact spans the NB note and its cancelled trials; all source elements are separately inventoried.'),
 11:('substantive',[c08,c09],'On a and cancelled action trials must remain in the margin.'),
 12:('substantive',[c09],'Cancelled action-trial continuation; editorial-list tokens are not source words.'),
 13:('substantive',[c09],'Cancelled third action trial; H editorial description supplies no replacement reading.'),
 14:('substantive',[c09],'Same third cancelled right member and uncertain inverse product.'),
 15:('substantive',[c09,c10,c11,c13,c14],'Long shift spans the live margin actions and return to the rho path explanation.'),
 16:('substantive',[c12],'Visible comma after the first rho.'),
 17:('substantive',[c13],'No manuscript hyphen in au dessus.'),
 18:('substantive',[c15],'Trivial, not direct.'),
 19:('macro/editorial',None,'aligned/cases syntax only.'),
 20:('macro/editorial',None,'Environment closure and invisible delimiter syntax only.'),
 21:('macro/editorial',None,'aligned/cases syntax only.'),
 22:('substantive',[c16],'The literal stop after the final rho is absent; other tokens are environment syntax.'),
 23:('substantive',[c03,c04,c05,c06,c07,c08,c09,c10,c11],'H serializes the right-margin note after the main conjugations. Its actual marginal placement and all substantive readings are recorded.'),
 24:('macro/editorial',None,'LaTeX --- and Unicode em dash represent the same manuscript dash.'),
 25:('substantive',[c17],'Par contre is readable.'),
 26:('substantive',[c18],'No additional independent sigma at this position.'),
 27:('substantive',[c19],'Singular la relation fondamentale is written.'),
 28:('substantive',[c19],'Est, not sont, is written.'),
 29:('substantive',[c22,c23,c24],'The cube example is above the deleted rho; H also supplies a non-source rho and a different doubtful word.'),
 30:('substantive',[c22,c23,c24],'Restores source order and the readable en outre, retaining the local puisque doubt.'),
 31:('macro/editorial',None,'Adjacent math tokens 0l versus 0 l differ only in TeX source spacing.'),
 32:('macro/editorial',None,'Adjacent math tokens 1l versus 1 l differ only in TeX source spacing.'),
 33:('substantive',[c25],'Des relations is visible within the cancellation.'),
 34:('substantive',[c26],'Faudra, with the phrase locally live.'),
 35:('substantive',[c28],'Pas is readable and belongs to the underline.'),
 36:('substantive',[c29,c30,c31],'Cancelled word, ou equality and elevated live et sigma have distinct states and positions.'),
 37:('substantive',[c26,c27,c28,c30,c31],'Cancellation scope and et sigma placement corrected; H explanatory prose is editorial.'),
 38:('macro/editorial',None,'aligned/cases syntax only.'),
 39:('substantive',[c32],'First dotted-sigma index reads 1.'),
 40:('macro/editorial',None,'Second-index certainty only: retain C 1|0; H reads the preferred 1.'),
 41:('substantive',[c33],'Environment tokens are editorial, but H\'s fragmentary marginal en belongs to the separately transcribed small note.'),
 42:('macro/editorial',None,'Ornate-S alphabet certainty only; the C alternatives are retained in M0827.'),
 43:('substantive',[c33],'All three tentative small-margin phrases and the underline are retained.'),
 44:('substantive',[c34],'Le système, not les symétries.'),
 45:('substantive',[c35],'Enfin, not autres.'),
 46:('substantive',[c36],'Est, not donnent.'),
 47:('macro/editorial',None,'Ornate-S alphabet certainty only; the C alternatives are retained in M0831.'),
 48:('substantive',[c37],'Dis, not ou.'),
 49:('substantive',[c38],'Comma after faux; no separate (+).'),
 50:('substantive',[c39],'En faisant dans les is readable.'),
 51:('substantive',[c40],'Crowded final group clause remains tentative rather than omitted.'),
 52:('substantive',[c40],'The final sigma-index/group reading remains uncertain; H\'s extra rho is not independently supported.'),
 53:('substantive',[c40],'No independent final equals sign is clear; the accompanying description is H editorial prose.'),
 54:('substantive',[c42],'Actual handwritten 17 is retained. H\'s comment about (+) is editorial; the alleged sign is separately rejected.'),
}
with (PACKET/'differences.tsv').open(encoding='utf-8',newline='') as f:
    diff_rows=list(csv.DictReader(f,delimiter='\t'))
assert len(diff_rows)==len(diff_map)==54
coverage=[]
for i in range(1,55):
    status,ids,explanation=diff_map[i]
    row=dict(row=i,status=status,explanation=explanation)
    if ids: row['change_id']=ids[0] if len(ids)==1 else ids
    coverage.append(row)

report=dict(
 scan=18,reader='/root/reader_a',lines_read=54,
 layout='Text sheet in his hand. Main column begins with numbered system (2), followed by the rho path explanation, two three-row conjugation systems, a prose cancellation with local replacements and deletions, a dotted presentation, a final rho-cube display and two prose lines. A dense right-margin NB note has trials, an arrow, a vertical separator and action formulas. Two lower slanted notes occupy the space beneath the dotted cube and the lower-left corner. Handwritten 17 is at lower right; no source header number is present. Line count treats separate replacement inscriptions, marginal baselines, display rows and the footer as read units.',
 changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
 notation=[
  dict(observation='Rho and dotted rho are distinct in the path sentence and dotted presentation.',places=['path explanation','conjugation arrays','dotted presentation'],qualification='The separate dot is clear in the sentence and on every relevant dotted display symbol; no dot is supplied from mathematical expectation.'),
  dict(observation='The first squared dotted-sigma index is 1; the second favors 1 but remains 1|0.',places=['dotted presentation, first row'],qualification='The repeated preferred index is retained as written; the row is not normalized to 0,1,infinity.'),
  dict(observation='Two ornate S3 glyphs have the rounded outer sweep and hooked upper ending.',places=['caption of dotted presentation','final paragraph'],qualification='Fraktur versus calligraphic alphabet remains unresolved locally, consistently marked at both places.'),
  dict(observation='The group letter in the cancelled prose is tall and two-legged.',places=['présentation de Pi in cancelled argument'],qualification='Preferred Pi is retained with lowercase alternative; this page does not settle global Pi case.'),
  dict(observation='The first live marginal action has l_infinity^-1 l_1^-1.',places=['right-margin action, first live row'],qualification='The two-lobed infinity is visible and distinct from the single oval zero; no identity was used to choose the factor.'),
 ],
 hand=[
  dict(observation='Long descending strokes can be misidentified as separate rho symbols or cancellation lines.',places=['before puisque','initial p of produit'],universal_on_page=False,witness_effect='H inserts a rho before its puissance reading; C extends cancellation over uncrossed following words.'),
  dict(observation='An upright small 1 can be narrow and hooked without forming the closed oval of 0.',places=['first and second squared dotted-sigma indices'],universal_on_page=False,witness_effect='H regularizes the first index to 0; the second remains locally doubtful.'),
  dict(observation='The terminal x of faux is written as an independent-looking small cross.',places=['lower-left oblique note'],universal_on_page=False,witness_effect='H treats this as part of a separate (+), although it is the final letter of faux.'),
  dict(observation='Several simultaneous cancellation layers are spatially distinct.',places=['large prose block','local rho deletion and cube insertion','lower word and unfinished equality'],universal_on_page=False,witness_effect='C collapses locally live continuation into the outer cancellation; H moves the cube example away from the rho it replaces.'),
 ],
 abbreviations=[
  dict(form='NB',expansion='nota bene',place='right-margin heading'),
  dict(form='i.e.',expansion='id est',place='between the two conjugation systems'),
  dict(form='p.ex.',expansion='par exemple',place='cube insertion above the deleted rho'),
  dict(form='pt',expansion='point',place='final parenthesis, au pt de vue profini'),
  dict(form='dis',expansion='disons (interpretive expansion only)',place='final parenthesis, dis dans E-hat'),
 ],
 notes=[
  'The page writes system (2), revises the order of the products in its three right members, and describes rho above dotted rho using the trivial path from P to P. It then writes two equivalent-looking conjugation arrays. This report transcribes those assertions and does not verify their derivation.',
  'The right-margin NB contains heavily cancelled trial expressions, a two-line live identity for l0 in terms of rho and sigma0, cancelled action trials, and three live formulas for sigma0 acting on the l_i. The cancelled sigma-infinity trace is below/left of the second live equality, with no visible underbrace; its exact attachment remains uncertain. A left-pointing arrow and the tall ruled separator are source marks.',
  'The large oblique cancellation begins at on voit par contre and runs through des relations sigma_i²=1. The following il faudra que rho soit and produit de termes are locally live. The old rho after que and the displayed rho=l0l1linfinity have additional local deletions. The lower word and ou sigma0sigma1sigma0= have their own horizontal cancellation, while et sigma is live above/right. This accounts separately for every C deletion and insertion.',
  'Five short upper and four short lower strokes surround la relation. They are reproduced geometrically without interpreting them as emphasis or as another deletion. The independent underline begins under pas in pas deux consécutifs. In the small slanted note, pas also has its own short underline; a later short stroke near the end of conjugués has uncertain status.',
  'The dotted presentation begins with index 1, followed by another index favoring 1 but still doubtful. The apparent repeated index is preserved. The author then states that relations (1)(2) and rho³=1 give a presentation of the inverse image of the ornate S3 in E, with a profinite qualification in E-hat. The later oblique note says C\'est faux and invokes setting rho=1, but its final group clause remains uncertain. These are authorial assertions and criticism, not proof results supplied by this reader.',
  'The singular la relation fondamentale (1) est une, the abbreviation dis, missing terminal stop in the oblique note, and other literal irregularities are retained. Both ornate-S alphabet choices, the local Pi case and all heavily crossed trial readings remain marked. There is no date on this sheet. The handwritten source page number is 17 and is counted as an omission from H, separately from editorial page markers.',
  'Whole-page layout and both native overlapping halves were read once, including C/H agreements. Sixteen page-specific crops were saved, read, and made available to the root reader. No OCR, other-page evidence, external research, TeX compilation or mathematical check was used by this reader. Parent adjudication supplied the agreed count of the short strokes around la relation and confirmed local source readings; the retained uncertainties remain explicit.',
 ],
 check_events=[],diff_coverage=coverage)

assert all(ch['c_changed'] or ch['h_changed'] for ch in changes)
assert [d['id'] for d in decisions]==[f'M{i:04d}' for i in range(825,833)]
assert len(unlisted)==13
assert all((ROOT/'edition'/ch['crop']).is_file() for ch in changes)
assert all(len(i['box'])==4 and i['sheet_kind']=='text' and i['hand']=='his hand' for i in inventory)
(OUT/'145_scan018.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(changes=len(changes),decisions=len(decisions),unlisted_decisions=len(unlisted),doubts=len(doubts),inventory=len(inventory),second_boxes=len(second),diff_rows=len(coverage)),ensure_ascii=False))
