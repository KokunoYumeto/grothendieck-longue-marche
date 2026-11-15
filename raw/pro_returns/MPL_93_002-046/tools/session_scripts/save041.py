import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(41,r'''\scanpage{41}
b) \uline{Filtration}s\deleted{\unsure{ass}} \uline{associées aux cristaux de Dieudonné}. Revenons au cas d'un S général (sur lequel p soit loc. nilp.). On \unsure{définira|définita} alors, pour tout $G\in\operatorname{Ob}\mathrm{BT}(S)$, une filtration \deleted{en deux crans} de MoDule localement libre $\underline D^*(G)_S$ sur S par un sous-Module localement facteur direct (donc localement libre de t.f.) \inserted{$\uline{Fil}^{1}=$} $\underline\omega_G$, donnant lieu à une suite exacte
\[
(*)\qquad
\diagram{\begin{tikzcd}
0 \arrow[r] & \underline\omega_G \arrow[r] & \underline D^*(G) \arrow[r] & \underline t_{G^*} \arrow[r] & 0,
\end{tikzcd}}
\]
où en fait $\underline\omega_G$ est le module des différentielles invariantes sur le groupe formel $\overline G\subset G$ associé à G (qui sera construit plus bas), et $\underline t_G=\underline\omega_{G^*}^{\vee}$ est l'Algèbre de Lie associée au groupe de BT dual $G^*$ de G (définition à reporter aux généralités sur les goupes de BT). Cette \deleted{\unsure{filtr}} suite exacte est fonctorielle \inserted{en G} et compatible aux images inverses par un $S'\longrightarrow S$.

\margin{(*) \unsure{formule inutile si} $S_0$ \unsure{parfait}}
\margin{40}
''','typed',[
('text','heading and first paragraph','b) Filtrations associées'),('deletion','heading after Filtrations','ass'),('deletion','after une filtration','en deux crans'),('insertion','before omega_G','Fil^1='),('diagram','middle','(*) 0 to omega_G to D*(G) to t_G* to 0'),('text','lower paragraph','où en fait omega_G'),('deletion','Cette filtr suite','filtr'),('insertion','above final line','en G'),('margin note','faint bottom line','(*) formule inutile si S_0 parfait'),('margin note','bottom left','40')
],[
('heading, cancelled fragment','ass','','low','Three overstruck letters following Filtrations; a start of the next word is plausible but not certain.'),('first paragraph verb','définira','définita','medium','A dark overprint makes r resemble t.'),('first paragraph module','MoDule','Module','high','Internal capital D is visible in the type.'),('after Cette, cancelled fragment','filtr','','medium','Five letters remain readable under the cancellation.'),('bottom pencil note','formule inutile si S_0 parfait','','low','Very faint pencil and lower clipping; enlarged contrast-adjusted crop still does not settle every word.'),('Lie-algebra equality','t_G = omega_G* dual','','high','The source uses t_G here, while the preceding exact sequence uses t_G*.')
])
