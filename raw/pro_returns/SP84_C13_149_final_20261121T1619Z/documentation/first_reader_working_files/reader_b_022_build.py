from pathlib import Path
import json
root=Path('/workspace/scratch/4644e52611c0')
boxes=json.loads(Path('/tmp/reader_b_022_boxes.json').read_text())
tri=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&]
\Pi_{K'} \arrow[rr,shift left,"f^*"] \arrow[rr,shift right,"g^*"'] \arrow[dr,no head,"p'"'] \& \& \Pi_K \arrow[dl,"p"]\\
\& \Pi_{\mathbb Q} \&
\end{tikzcd}}'''
square=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&]
pf^*(\bar\eta') \arrow[r,phantom,"{\overset{p(\alpha)}{\simeq}}" description] \arrow[d,"\wr"'] \& pg^*(\eta) \arrow[d,no head,"\wr"]\\
p'(\bar\eta') \arrow[r,phantom,"\simeq" description] \& p'(\bar\eta')
\end{tikzcd}}'''
upper=r'''\margin{En fait, ce théorème n'est pas spécial à $\mathbb Q$ --- il marcherait sur un corps de base quelconque de car $0$. \unsure{La|car la} démon. montre bien que c'est en fait un énoncé de nature géométrique non arithmétique (j'énonce pour \unsure{rendre} la démon. facile \unsure{et|une} arithmétique pure)}'''
first_insert=r'''\inserted{donnant via $f,g$ deux clôtures alg. de $\unsure{\bar K_\varepsilon|\bar K}$, $\unsure{K|\widetilde K}$ de $K$}'''
long_insert=r'''\inserted{l'on peut trouver un isomorphisme entre celles-ci (permettant donc d'identifier $\mathcal E_{\bar K/K}$ et $\mathcal E_{\widetilde K/K}$), de telle façon que les deux hom}'''
middle=r'''\margin{induisant ``l'identité'' sur les clôtures alg. \deleted{\unsure{et|de}} $\overline{\mathbb Q}$ de $\mathbb Q$ dans $\bar K$ et $\widetilde K$, identifiées à celle dans $\bar K'$}'''
display=r'''f^*,g^*:\mathcal E_{\bar K'/K'}\unsure{\rightrightarrows}\mathcal E_{\bar K/K}'''
old_cancel=r'''\deleted{Il \unsure{s'agit} en \unsure{conclusion}}'''
upper_cancel=r'''\inserted{\deleted{\unsure{C'est} \unsure{sans} doute plus}}'''
bottom=r'''\margin{On doit se ramener au cas $k=k'$ --- c'est immédiat en \deleted{\unsure{faisant le chgt de base}}\inserted{\unsure{prenant}} extension finie de $\mathbb Q$}'''
map_formula=r'''\unsure{K-\Pi_K/\Pi_{\mathbb Q}|K\to\Pi_K/\Pi_{\mathbb Q}}'''
page=r'''\scanpage{22}
\uline{Théorème 2} Le foncteur $MAP$ des catégories des t.f. de $\mathbb Q$ vers les groupoïdes profinis sur $\Pi_{\mathbb Q}$ est \uline{fidèle}.

UPPER

Si deux hom. $K\overset{f,g}{\rightrightarrows}K'$ définissent des hom de groupoïdes \inserted{sur $\Pi_{\mathbb Q}$} isomorphes
TRIANGLE
(i.e. $\exists$ isomorphisme de foncteurs $\alpha:f^*\simeq g^*$, tel que $\forall\bar\eta'\in\operatorname{Ob}\Pi_{K'}$, l'e\deleted{isom}\inserted{carré}
\deleted{correspondant}
SQUARE
est commutatif) alors $f=g$.

L'hypothèse sur $f,g$ signifie aussi, en termes d'une clôture alg. choisie $\bar K'$ \deleted{\unsure{qui ne|qu'on} \unsure{peut}}FIRSTINSERT de $K'$, que \deleted{les deux hom d'exten}LONGINSERT
\deleted{\unsure{disons}}
MIDDLE
\[
DISPLAY
\]
sont égaux, OLDCANCEL
% The following cancelled replacement is written above the preceding cancelled run.
UPPERCANCEL
\unsure{Ou bien} en termes d'une clôture alg. $\overline{\mathbb Q}$ fixée, de $\mathbb Q$, en disant que les deux hom $f^*,g^*:\pi_{K'}\rightrightarrows\pi_K$ de groupes profinis extérieurs (avec opérateurs $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$) sont égaux.
BOTTOM
\margin{21}
'''
for key,val in sorted([('MAP',map_formula),('UPPER',upper),('TRIANGLE',tri),('SQUARE',square),('FIRSTINSERT',first_insert),('LONGINSERT',long_insert),('MIDDLE',middle),('DISPLAY',display),('OLDCANCEL',old_cancel),('UPPERCANCEL',upper_cancel),('BOTTOM',bottom)], key=lambda p: len(p[0]), reverse=True):
    page=page.replace(key,val)
(root/'edition/reviews/149_scan022.tex').write_text(page,encoding='utf-8')
report={'scan':22,'reader':'/root/reader_b','lines_read':60,'changes':[],'decisions':[],'inventory':[],'notes':[],'checks':[],'hand':[],'notation':[],'abbreviations':[],'doubts':[],'audit_boxes':[],'diff_coverage':[]}
def change(id,place,C,H,final,evidence,crop,confidence='high',against_C=False,against_H=True,kind='misread word',error_category='Words',marked_in_H=False,mathematical=False):
    report['changes'].append(dict(id=id,place=place,C=C,H=H,final=final,evidence=evidence,crop=f'crops/149_scan022_{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,error_category=error_category,marked_in_H=marked_in_H,mathematical=mathematical))
change('c01','Theorem heading',r'\uline{Théorème 2}',r'\textbf{Théorème 2.}',r'\uline{Théorème 2}','The numeral has a curved top, descending oblique and broad lower return. The underline runs beneath the words and numeral; the space after 2 has no separate stop.','c01',kind='text not on the page',error_category='Text that is not on the page')
change('c02','Theorem, complete functor formula',r'K-\Pi_K/\Pi_{\mathbb Q}',r'K\mapsto\Pi_K/\Pi_{\mathbb Q}',map_formula,'The shaft begins freely, without a perpendicular mapsto bar. Its right end has a very small curled cap; this does not securely separate a bare shaft from a tiny arrowhead. Both Pi letters, K index, slash and double-stroked Q were read in the full formula.','c02',confidence='medium',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change('c03','Theorem, second line','des extensions de t.f.','des catégories des t.f.','des catégories des t.f.','The noun begins with open c, a and a tall crossed t, followed by compressed loops and a dotted i with the terminal -ies run. It does not begin ex-. The next small word has a d-loop followed by e and a terminal s-like turn: des. The literal phrase is retained despite its syntax.','c03',against_C=True,against_H=False,marked_in_H=True)
change('c04','Upper margin, after Q',r'$\mathbb Q$ --- il',r'$\mathbb Q$ : il',r'$\mathbb Q$ --- il','There is one horizontal separating stroke after Q, not two vertically spaced points.','c04',kind='misread symbol or index',error_category='Symbols and indices')
change('c05','Upper margin, fourth line','marcherait',"s'énoncerait",'marcherait','The word begins with a connected low m/a run; its middle has the ascender of h and its end the dotted i and crossed t. No initial s-apostrophe or énonc- sequence is visible.','c04',marked_in_H=True)
change('c06','Upper margin, base characteristic','de car $0$',r'$k$, et \ill{} fait la diff.','de car $0$','A tall d is followed by the small car run and an oval zero. The zero is a numeral, not a letter k; the surviving stop following it is distinct.','c04',kind='misread symbol or index',error_category='Symbols and indices',marked_in_H=True,mathematical=True)
change('c07','Upper margin, central argument',r"\unsure{La|car la} démon. montre bien que c'est en fait un énoncé de nature géométrique non arithmétique",r"\ill{} fait la diff. \ill{} bien que l'énoncé \ill{} fait sur \ill{} l'énoncé est \ill{} arith. \ill{} géométrique \ill{}",r"\unsure{La|car la} démon. montre bien que c'est en fait un énoncé de nature géométrique non arithmétique",'The note has démon. with a visible stop, then montre; c-apostrophe-est, fait, un énoncé, de nature, géométrique, non and the continuation arithmétique can be followed in sequence. The small lead-in before démon. remains compressed and is retained as La/car la. H splits this continuous passage into unrelated fragments and omissions.','c04',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True)
change('c08','Upper margin, parenthetical ending',r"(\unsure{j'énonce|l'énoncé} pour \unsure{rendre} la démon. facile \unsure{et|une} \unsure{arithmétique|intuitivement} \unsure{pure|courte})",r'(bien que \ill{}) \ill{} mais \ill{}',r"(j'énonce pour \unsure{rendre} la démon. facile \unsure{et|une} arithmétique pure)",'A descending j-shaped initial favors j\'énonce, followed by pour. The small rendre run and the short token after facile remain uncertain. The final arithmétique has the q-descender and -tique ending; pure begins with a long p-descender and has no tall t that would support courte. Both parentheses are present.','c04',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True)
change('c09','Upper margin, terminal punctuation',r'pure}).',r'\ill{}.',r'pure)}','The close parenthesis ends the note. There is no separately written full stop after it.','c04',against_C=True,kind='text not on the page',error_category='Text that is not on the page')
change('c10','Beginning of proof','Si deux hom.','I.e. si deux hom.','Si deux hom.','The line begins with Si, then a tall d and the deux run. No I.e. precedes it in the indented opening. The stop following hom. is a dark separate point.','c05',kind='text not on the page',error_category='Text that is not on the page')
change('c11','Proof, hom before de groupoïdes','des hom de groupoïdes','des hom. de groupoïdes','des hom de groupoïdes','The final m is followed by blank space and the next de. There is no separate stop. The inserted sur Pi_Q is above this line, carried to the point immediately before isomorphes by a curved leader.','c06',kind='text not on the page',error_category='Text that is not on the page')
change('c12','Triangular diagram, geometry, heads and order','Triangle with the bottom node below the upper right node; p vertical and p-prime headless','Centered lower node; both diagonals headed; diagram moved after f=g',tri,'The bottom Pi_Q is between the two upper nodes. Both upper horizontal shafts have distinct right-facing two-arm heads. The p-prime diagonal descends to the right and ends without a head; the p diagonal descends to the left and has a clear head. The diagram stands alongside the opening parenthetical explanation, before the line est commutatif.','c07',against_C=True,kind='drawing or diagram',error_category='Drawings and diagrams',mathematical=True)
change('c13','Article before the replacement carré',"l'",'le',"l'e",'After a tall l there are two separate pieces of ink: a detached high apostrophe-like tick and a complete low e-loop. Neither is crossed by the line through isom. Literal l\'e preserves both; the order in which e and the residual tick were written is not asserted.','c08',against_C=True,marked_in_H=True)
change('c14','Cancelled noun before inserted carré',r'\deleted{isom}\inserted{carré}',r'\struck{\ill{}}\add{\uncertain{carré}}',r'\deleted{isom}\inserted{carré}','The cancellation crosses the i/s/o/m run, with a separate i dot and visible rounded o. Above it, c-a-r-r-é and the accent are clear. The cancellation does not extend to the preceding article.','c08',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True)
change('c15','Complete square diagram','Phantom horizontal equivalences; right vertical headless; top-right eta/eta-prime','Headed horizontal arrows with sim labels, both verticals headed, and barred eta-prime at top right',square,'Both horizontal links are a wave over one horizontal bar, with no arrowhead. p(alpha) is above the upper equivalence. The left vertical shaft has a small head; the right one has only its terminal return. Top right has eta alone: the blank above and to its right contains neither bar nor prime, in contrast to the other three barred, primed arguments. All four complete node formulas were read.','c10',kind='drawing or diagram',error_category='Drawings and diagrams',mathematical=True)
change('c16','Short cancellation after chosen closure',r"\deleted{\unsure{qui|qu'on} \unsure{peut}}",r'\struck{qui ne peut}',r"\deleted{\unsure{qui ne|qu'on} \unsure{peut}}",'The q-descender, a dot/tick above the next run, and a further low cluster before peut are visible. That extra cluster permits qui ne or qu\'on; qui alone omits it. In peut the p-loop/descender and t are clear, but the crossing leaves the e/u sequence uncertain.','c12',confidence='low',against_C=True,against_H=False,kind='deletion state',error_category='Struck text')
change('c17','First lower insertion, including both decorated fields',r'\inserted{donnant via $f,g$ deux clôtures alg. de $\unsure{K_\varepsilon|\bar K}$, $\unsure{K|\widetilde K}$ de $K$}',r'\add{donnant via $f,g$ deux clôtures alg. de $K$, $\bar K$ et $\widetilde K$}',first_insert,'The insertion reads donnant via f,g deux clôtures alg. de, followed by two fields separated by a comma, then de K. The first K has a flat overhead stroke and an additional lower-right epsilon-like curl; the curl remains doubtful. The second K overlaps the descender of the chosen closure above, so its possible tilde remains uncertain. No et occurs between the two fields; the terminal de K is present.','c13',confidence='medium',against_C=True,kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change('c18','Placement of de K-prime after the first insertion',r"$\bar K'$ \deleted{...}\inserted{...} de $K'$",r"$\overline{K'}$ de $K'$ \struck{...}\add{...}",r"$\bar K'$ \deleted{\unsure{qui ne|qu'on} \unsure{peut}}"+first_insert+r" de $K'$",'The live de K-prime is on the lower baseline below the short cancellation, after the interlinear replacement has been read. H moves it back up beside the originally chosen closure. The prime beside the lower K is separate and clear.','c12',kind='insertion or placement',error_category='Insertions put in the wrong place',mathematical=True)
change('c19','Live que before the crossed homomorphism phrase',r"que \deleted{les deux hom d'exten}",r"\struck{que les deux hom. d'exten\ill{}} que",r"que \deleted{les deux hom d'exten}",'The long strike begins to the right of que, at les. Que is intact; there is no second que after d\'exten.','c14',kind='deletion state',error_category='Struck text')
change('c20','Crossed homomorphism phrase, abbreviation and stop',r"\deleted{les deux hom d'exten}",r"\struck{les deux hom. d'exten\ill{}}",r"\deleted{les deux hom d'exten}",'Under the continuous strike, les, deux, hom and d\'exten remain readable. There is no distinct stop after hom, and no additional word or obscured continuation follows the final abbreviated run at the right.','c14',kind='deletion state',error_category='Struck text',marked_in_H=True)
change('c21','Long replacement, state and donc',r"\inserted{l'on peut trouver un isomorphisme entre celles-ci (permettant donc d'identifier ...), de telle façon que les deux hom}",r"l'on peut trouver un isomorphisme entre celles-ci (\uncertain{permettant d'identifier} ...), ...",long_insert,'The three sloping lines are a replacement beneath the crossed les deux hom d\'exten. The first runs l\'on peut trouver un isomorphisme entre celles-ci. The next has permettant, then a distinct d-loop and onc run before d\'identifier: donc is present. The parenthesis is real, and the third line continues the same added passage.','c15',kind='insertion or placement',error_category='Insertions put in the wrong place',marked_in_H=True)
change('c22','End of long replacement',r'de telle façon que les deux hom',r'de telle \supplied{sorte} que les deux hom','de telle façon que les deux hom','The lower line has de telle, a long f and the a/ç/on run, then que les deux hom. It is façon, not a blank requiring sorte. This line belongs to the replacement before the display, not after the marginal note.','c15',kind='insertion or placement',error_category='Insertions put in the wrong place',marked_in_H=True)
change('c23','Two extension symbols inside the long replacement',r'E_{\bar K/K}\text{ et }E_{\widetilde K/K}',r'\mathcal E_{\bar K/K}\text{ et }\mathcal E_{\widetilde K/K}',r'\mathcal E_{\bar K/K}\text{ et }\mathcal E_{\widetilde K/K}','Both letters are rounded, open, cursive E forms, with curved upper/lower lobes and a sweeping foot rather than a vertical stem with separate bars. The same pair of forms recurs in the display. Bar and tilde on the two numerator K letters are separate and visible.','c15',against_C=True,against_H=False,kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change('c24','Cancelled word below the replacement',r'\deleted{\unsure{disons}}',r'\struck{\ill{}}',r'\deleted{\unsure{disons}}','A d-shaped beginning and i dot survive, followed by the compressed -sons run under the strike. The crossing prevents every middle letter from being plain, so disons remains tentative rather than being resolved.','c15',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True)
change('c25','Middle marginal note opening','induisant',r'\uncertain{i.e.} induisant','induisant','The first detached i and long low n-stroke continue directly into d-u-i-s-a-n-t. There is no independent i.e. preceding that word.','c16',kind='text not on the page',error_category='Text that is not on the page',marked_in_H=True)
change('c26','Middle marginal quotation',"``l'identité''",'« l’identité »',"``l'identité''",'The opening and closing quotation marks are paired short raised strokes, not chevrons. The accent on the final é of identité is present.','c16',kind='misread symbol or index',error_category='Symbols and indices',marked_in_H=True)
change('c27','Middle marginal note, closures and cancelled token',r"les clôtures alg. \deleted{\unsure{et|de}} $\overline{\mathbb Q}$ de $\mathbb Q$ dans $\bar K$ et $\widetilde K$",r'les clôtures alg. $\bar K$ et $\widetilde K$ de \ill{}',r"les clôtures alg. \deleted{\unsure{et|de}} $\overline{\mathbb Q}$ de $\mathbb Q$ dans $\bar K$ et $\widetilde K$",'After the visible stop in alg., a crossed two-letter cluster remains et/de, unresolved. It is followed by a Q with an overhead bar, then de Q dans on the same run, and the two decorated K letters on the next. No extra de follows the second K.','c16',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True,mathematical=True)
change('c28','Middle marginal note, singular reference','celle','celles','celle','The word has c, e, two tall l loops and a final e return. There is no additional s before dans.','c16')
change('c29','Middle marginal note, terminal punctuation',r"$\bar K'$.",r"$\overline{K'}$",r"$\bar K'$",'The terminal prime is present beside the barred K, but no separate full stop follows it. The large nearby curve is the marginal leader.','c16',against_C=True,against_H=False,kind='text not on the page',error_category='Text that is not on the page')
change('c30','Complete display of the two homomorphisms',r'f^*,g^*:E_{\bar K\prime/K\prime}\rightrightarrows E_{\bar K/K}',r"f^*,g^*:\mathcal E_{\overline{K'}/K'}\rightrightarrows\mathcal E_{\bar K/K}",display,'Both E letters have the same rounded cursive construction as the two inside the insertion, so mathcal E is used. Both primes in the source group index, the bar, quotient slash and target index were checked. The upper shaft has a small but definite head; the lower ends in a very small turned cap, so the parallel-arrow reading retains an explicit lower-head doubt.','c17',confidence='medium',against_C=True,against_H=False,kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change('c31','After the display','sont égaux,','soient égaux,','sont égaux,','The first word is the short s/o/n/t run. There is no extra i or e between o and n. The following comma is a separate dark hooked mark.','c18')
change('c32','Two cancelled runs after sont égaux',r"\deleted{Il \unsure{(Ceci)|C'est} \unsure{s'agit} \unsure{en} \unsure{donc} \unsure{plus} \unsure{conclusion}}",r"\struck{Il \uncertain{s'agit donc des} \ill{}} \uncertain{Ceci s'exprime} \add{\uncertain{plus}} \ill{}",old_cancel+' '+upper_cancel,'There are two vertically distinct runs under the common cancellation. The lower begins Il and continues a heavily crossed s\'agit, then the separate en and a compressed conclusion. Above it are C\'est, sans, doute and plus: doute has a clear d-loop, o, tall t and final e; plus has p/l/u/s. C\'est and sans remain tentative, as do the two crowded lower words. The upper run is recorded as an inserted replacement that was also cancelled; exact timing of the strokes cannot be recovered.','c19',confidence='medium',against_C=True,kind='deletion state',error_category='Struck text',marked_in_H=True)
change('c33','Opening of the final reformulation',r'\unsure{Ou bien}',r"\uncertain{Ceci s'exprime} \add{\uncertain{plus}} \ill{}",r'\unsure{Ou bien}','A large looped b, i dot and the -en run are visible. The first short word is partly covered by a marginal leader and remains Ou tentatively. The visible ink at this place does not support Ceci s\'exprime.','c20',confidence='medium',marked_in_H=True)
change('c34','Final paragraph, after fixée',r'fixée, de $\mathbb Q$,',r'fixée de $\mathbb Q$,',r'fixée, de $\mathbb Q$,','A separate curved comma follows the final e of fixée. The following de, double-stroked Q and second comma are also clear.','c21',kind='omission',error_category='Omissions')
change('c35','Final paragraph, hom before f-star/g-star','les deux hom','les deux hom.','les deux hom','The long final m is followed by blank space; no point is present after hom.','c22',kind='text not on the page',error_category='Text that is not on the page')
change('c36','Bottom marginal note opening','On doit se ramener au cas','On se ramène au cas','On doit se ramener au cas','The separate doit has a d-loop, dotted i and terminal t; it is not absent. In ramener the final low return is r, and no accent lies above the preceding e.','c23')
change('c37','Bottom marginal note, field letters',r'$k=k\prime$',r"$K=K'$",r"$k=k'$",'Both letters are small lower-case-size k forms relative to the nearby capital K letters in the middle margin. The equality consists of two bars, and the second k has a distinct prime.','c23',kind='misread symbol or index',error_category='Symbols and indices',mathematical=True)
change('c38','Bottom marginal cancellation',r'\deleted{\unsure{faisant le chgt de base}}',r'\struck{\uncertain{faisant le changement de base}}',r'\deleted{\unsure{faisant le chgt de base}}','The cancellation is heavy over part of the phrase. The short chgt cluster has neither the length nor the extra letter run of changement. The surrounding phrase remains uncertain as a whole because not every letter under the strike is recoverable.','c23',confidence='medium',kind='abbreviation expanded or spelling modernised',error_category='Abbreviations expanded, spelling modernised',marked_in_H=True)
change('c39','Bottom marginal replacement and conclusion',r'\inserted{\unsure{prenant}} extension finie de $\mathbb Q$',r'\ill{} \uncertain{catégories} finies \uncertain{sur} $\overline{\mathbb Q}$ \ill{} de $\mathbb Q$',r'\inserted{\unsure{prenant}} extension finie de $\mathbb Q$','Below the strike is a p-descender and a low compressed -renant run, retained tentatively as the replacement prenant. The next line has extension with a tall t and dotted i, followed by finie with two i dots and no plural s. The last line is de Q, with no overhead bar. No catégories or sur occurs here.','c23',confidence='medium',kind=r'readable ink left as \ill{}',error_category='Readable ink left as illegible',marked_in_H=True)
change('c40','Bottom marginal note, final stop',r'$\mathbb Q$.',r'$\mathbb Q$.',r'$\mathbb Q$','The Q ends with its short tail. No separate terminal full stop is visible after the symbol.','c23',against_C=True,kind='text not on the page',error_category='Text that is not on the page')
change('c41','Lower-left foliation',r'\margin{21}','omitted',r'\margin{21}','The thin small hand has a curved 2 with flat lower return and a narrow 1. It is separate from the large main-hand note and is kept as foliation, not an author page heading.','c24',kind='omission',error_category='Omissions')

def decision(id,choice,reading,evidence,crop,confidence):
    report['decisions'].append(dict(id=id,decision=choice,reading=reading,evidence=evidence,crop=f'crops/149_scan022_{crop}.png',box=boxes[crop],confidence=confidence))
decision('M1026','undecided',r'\unsure{La|car la}','The initial compact strokes before démon. remain compatible with La and car la. The following demonstration abbreviation and verb are readable; they do not decide the lead-in.','c04','low')
decision('M1027','first',"j'énonce",'The initial has a long descending j-shaped stroke and a detached apostrophe; the following énonc- run and final e favor j\'énonce over l\'énoncé.','c04','high')
decision('M1028','undecided',r'\unsure{rendre}','The r-shaped entry and the compressed following run are present, but the middle n/d segmentation is not secure at this slant.','c04','medium')
decision('M1029','undecided',r'\unsure{et|une}','The very short run after facile remains too compressed to distinguish et from une securely.','c04','low')
decision('M1030','first','arithmétique','The final word has the arithm- sequence, a q-descender and the -tique ending. These strokes exclude intuitivement.','c04','high')
decision('M1031','first','pure','A long p-descender is followed by a short ure run. There is no tall t within the word to support courte.','c04','high')
decision('M1032','first',r'\eta','In the full square, the top-right argument has eta alone. The space above it is blank and no prime follows it; the other three arguments have distinct bars and primes.','c10','high')
decision('M1033','first','est','The word has an initial e loop, low s and final t rise/cross. No o/i run appears.','c11','high')
decision('M1034','undecided',r'\unsure{\bar K_\varepsilon|\bar K}','The first K has a horizontal overhead stroke and a small lower-right epsilon-like curl. The curl may be a genuine subscript or a crowded return; no regularization to the expected pair of closures is made.','c13','medium')
decision('M1035','undecided',r'\unsure{K|\widetilde K}','The second K is clear. Its upper region overlaps the descending strokes of the chosen closure written above, leaving a possible tilde uncertain.','c13','low')
decision('M1036','undecided',r'\unsure{Ou bien}','The b-loop, i dot and -en run are visible, but the first word is partly crossed by the marginal leader. Ou bien remains the best reading without being resolved.','c20','medium')
decision('M1037','undecided',r'\unsure{prenant}','Below the cancellation, the word begins with a p-descender and ends in a compact -nant/t-shaped return; the middle letters remain compressed.','c23','medium')

def inv(element,kind,position,first,hand='main manuscript hand'):
    report['inventory'].append(dict(scan=22,sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('e01','text','top, three main lines','Théorème 2 Le foncteur')
inv('e02','margin note','upper left, long oblique note','En fait, ce théorème')
inv('e03','text','upper middle, proof opening','Si deux hom.')
inv('e04','insertion','above proof line, before isomorphes',r'sur $\Pi_{\mathbb Q}$')
inv('e05','diagram','left of the parenthetical explanation',r'\Pi_{K\prime}, \Pi_K, \Pi_{\mathbb Q}')
inv('e06','text','middle right, parenthetical explanation','(i.e. exists isomorphisme de foncteurs')
inv('e07','deletion','after literal article l\'e','isom')
inv('e08','insertion','above cancelled isom','carré')
inv('e09','deletion','below the parenthetical prose, left of square','correspondant')
inv('e10','diagram','middle right, under parenthetical explanation',r'pf^*(\bar\eta\prime), pg^*(\eta), p\prime(\bar\eta\prime)')
inv('e11','text','below the two diagrams','est commutatif) alors f=g.')
inv('e12','text','lower half, opening of the reformulation',"L'hypothèse sur f,g signifie aussi")
inv('e13','deletion','after chosen closure, before the interlinear replacement',"qui ne / qu'on peut")
inv('e14','insertion','interlinear, after chosen closure and before baseline de K-prime','donnant via f,g deux clôtures alg.')
inv('e15','deletion','after live que on the next baseline',"les deux hom d'exten")
inv('e16','insertion','three sloping lines beneath that cancellation',"l'on peut trouver un isomorphisme")
inv('e17','deletion','below beginning of long replacement','disons')
inv('e18','margin note','middle left, oblique, with a curved leader',"induisant ``l'identité''")
inv('e19','deletion','inside middle marginal note, before barred Q','et / de')
inv('e20','display','below the long replacement',r"f^*,g^*:\mathcal E_{\bar K'/K'}\rightrightarrows\mathcal E_{\bar K/K}")
inv('e21','text','below the display','sont égaux,')
inv('e22','deletion','baseline after sont égaux',"Il s'agit en conclusion")
inv('e23','insertion','above the preceding cancelled run, itself cancelled',"C'est sans doute plus")
inv('e24','deletion','the same upper replacement run under the common cancellation',"C'est sans doute plus")
inv('e25','text','last main paragraph, continuing to bottom','Ou bien en termes d\'une clôture alg.')
inv('e26','margin note','lower left, oblique','On doit se ramener au cas')
inv('e27','deletion','inside bottom marginal note','faisant le chgt de base')
inv('e28','insertion','below that cancellation','prenant')
inv('e29','text','bottom left, separate small foliation','21','another/uncertain hand; thin small foliation')

report['notes']=[
    'The page states Théorème 2: faithfulness of the displayed association from fields of finite type over Q to profinite groupoids over Pi_Q. The literal theorem phrase is des catégories des t.f.; neither its noun nor its following des is repaired to fit the expected syntax. This is transcription, not verification of the theorem.',
    'The upper marginal note asserts that the theorem also works over an arbitrary characteristic-zero base and describes its nature as geometric rather than arithmetic. Several compressed words in the parenthetical explanation remain doubtful. The paragraph was read as a complete oblique note, with its numeral 0 and punctuation.',
    'The proof opening is expressed with two diagrams. In the triangle the lower node is centered, both horizontal arrows are headed, the left p-prime diagonal is headless, and the right p diagonal is headed. In the square both horizontal links are equivalence signs, the left vertical is headed, and the right vertical is headless. The top-right argument is literal unbarred, unprimed eta; it has not been regularized to match the other three arguments.',
    'The article before cancelled isom is literal l\'e: both the high residual tick and the low e-loop survive. Carré is written above the cancelled noun. No unsupported order of the article correction has been assigned.',
    'The lower paragraph reformulates the condition using chosen algebraic closures and an isomorphism between the two induced closures, then gives equality of two homomorphisms of extension groups. A marginal note describes the identity on the algebraic closures of Q. The first decorated K in the insertion has a doubtful lower-right curl; both field readings retain local uncertainty instead of being regularized by the mathematical meaning.',
    'All four rounded extension letters, two inside the addition and two in the display, are transcribed as calligraphic E from their curved lobes and foot. The display retains a doubt on the lower terminal of its two parallel shafts. This is an alphabet and stroke judgment, not a mathematical check.',
    'The cancellation after sont égaux contains a lower run Il s\'agit en conclusion and an upper replacement C\'est sans doute plus. The two runs are kept separate, with the genuinely crossed or crowded words still doubtful. Both are within the cancelled passage; exact pen chronology cannot be reconstructed.',
    'The final main paragraph gives the equivalent formulation using the outer profinite groups pi_K and Gamma operators. The bottom note says On doit se ramener au cas k=k\' and gives a cancelled chgt de base phrase with a tentative prenant replacement. Its lower-case k letters, the abbreviation chgt and the singular finie are preserved.',
    'No terminal full stop is securely present after the upper note\'s closing parenthesis, the middle note\'s barred K-prime, or the bottom note\'s Q. Stops following the heading numeral and two instances of hom are likewise not supplied. The actual stop in the initial hom. and the commas after fixée and Q are retained.',
    'The heading is Théorème 2, underlined; no author page number or date is visible. The separate thin lower-left foliation reads 21 and is attributed to another/uncertain hand, not the main manuscript hand.',
    'The whole image and both supplied halves were personally viewed once, followed by the 24 saved enlarged crops. Every agreed word and sign was checked against the ink, and all 54 supplied difference rows are accounted for. The line tally includes the oblique marginal lines, diagram rows and separately placed revision lines, rather than TeX source lines. No OCR, outside research, TeX compilation or mathematical proof check was performed. Reader: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149.'
]
report['hand']=[
    {'habit':'The four extension symbols have rounded open lobes and a sweeping lower foot, supporting calligraphic E.','pages':[22],'consistency':'All four locally visible occurrences agree; the judgment is based on their construction, not only the expected notation.','misread':'C used ordinary E in the two inserted formulas and the two display terms.'},
    {'habit':'Short hom abbreviations do not all carry a stop.','pages':[22],'consistency':'The initial hom. has a separate point; the later proof hom, cancelled hom and final hom do not.','misread':'H supplied stops at the three unstopped occurrences.'},
    {'habit':'Arrow shafts sometimes end in only a small turned cap, distinct from a fully drawn two-arm head.','pages':[22],'consistency':'The triangle heads and square left head are clear; the theorem map and lower shaft of the extension display remain doubtful.','misread':'H supplies a mapsto bar in the theorem and heads on the two clearly headless diagram branches.'},
    {'habit':'An article correction can leave both a detached apostrophe and a baseline e.','pages':[22],'consistency':'One local occurrence, before cancelled isom and inserted carré.','misread':'C omitted the e; H omitted the surviving high tick.'},
    {'habit':'Capital K and the smaller k in the bottom marginal note remain distinguishable by size and ductus.','pages':[22],'consistency':'The two bottom-note letters agree with each other and are smaller than the nearby main-note K letters.','misread':'H capitalized the bottom-note k=k-prime.'},
    {'habit':'The lower-left foliation is thin and small, unlike the main manuscript writing.','pages':[22],'consistency':'One separate foliation number 21; no author page heading is visible.','misread':'H omitted the foliation; it must not be promoted to author numbering.'}
]
report['notation']=[
    {'written':r'\Pi_K,\Pi_{K\prime},\Pi_{\mathbb Q}','rendering':r"\Pi_K,\Pi_{K'},\Pi_{\mathbb Q}",'meaning':'Profinite groupoids appearing in the stated faithful functor and its diagrams.','evidence':'Theorem and triangular diagram; each capital Pi has two uprights joined by a top bar.'},
    {'written':r'\pi_K,\pi_{K\prime}','rendering':r"\pi_K,\pi_{K'}",'meaning':'Outer profinite groups in the final reformulation.','evidence':'Final main paragraph; the lower-case forms were read on the supplied lower half.'},
    {'written':'rounded cursive E with a relative-closure index','rendering':r'\mathcal E_{\bar K/K}','meaning':'Extension group notation used to express the two homomorphisms.','evidence':'Two examples inside the long replacement and two in the following display have matching curved construction.'},
    {'written':'Q with an internal doubled stroke','rendering':r'\mathbb Q','meaning':'Rational base field named throughout the page.','evidence':'Theorem, both diagrams and all three marginal notes.'},
    {'written':r'\Gamma_{\overline Q/Q}','rendering':r'\Gamma_{\overline{\mathbb Q}/\mathbb Q}','meaning':'Operator group in the final outer-group formulation.','evidence':'Final main paragraph, checked on the lower half.'}
]
report['abbreviations']=[
    {'form':'t.f.','expansion':'type fini','place':'theorem'},
    {'form':'hom. / hom','expansion':'homomorphisme(s)','place':'proof opening and lower reformulations; the stop is local'},
    {'form':'car','expansion':'caractéristique','place':'upper marginal note'},
    {'form':'démon.','expansion':'démonstration','place':'upper marginal note'},
    {'form':'alg.','expansion':'algébrique(s)','place':'lower paragraph and middle marginal note'},
    {'form':"d'exten",'expansion':"d'extension(s)",'place':'cancelled phrase after live que'},
    {'form':'chgt','expansion':'changement','place':'bottom marginal cancellation'},
    {'form':'i.e.','expansion':'id est','place':'parenthetical explanation before the square'}
]

def doubt(place,reading,alternatives,confidence,reason):
    report['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
doubt('Theorem functor formula',r'K-\Pi_K/\Pi_{\mathbb Q}',[r'K\to\Pi_K/\Pi_{\mathbb Q}'],'medium','The tiny curled right terminal is not a securely separable two-arm head; no mapsto bar is present.')
doubt('Upper margin before démon.','La',['car la'],'low','The compact lead-in is not securely segmented.')
doubt('Upper margin after pour','rendre',[],'medium','The middle letters remain compressed in the slanted run.')
doubt('Upper margin after facile','et',['une'],'low','The short token is too compact to distinguish these alternatives securely.')
doubt('Short cancellation after chosen closure','qui ne',["qu'on"],'low','A dot/tick and low additional cluster permit both readings beneath the strike.')
doubt('Same short cancellation','peut',[],'medium','The p and t are plain; the e/u sequence is crossed.')
doubt('First field in the lower insertion',r'\bar K_\varepsilon',[r'\bar K'],'medium','An epsilon-like lower-right curl may be a subscript or a crowded return; the overhead stroke is retained.')
doubt('Second field in the lower insertion','K',[r'\widetilde K'],'low','The region for a tilde overlaps the chosen closure above.')
doubt('Cancelled word below the long replacement','disons',[],'medium','The middle run is obscured by the strike.')
doubt('Middle marginal cancellation','et',['de'],'low','The two-letter cluster is heavily crossed.')
doubt('Extension-group display, parallel shafts',r'\rightrightarrows',['upper arrow over a headless lower shaft'],'medium','The upper head is clear; the lower terminal is only a small turned cap.')
doubt('Lower run of the final cancellation',"s'agit",[],'medium','The overlying replacement and strike obscure internal letters.')
doubt('End of the lower cancelled run','conclusion',[],'medium','The middle and terminal letters overlap the upper plus and the strike.')
doubt('Upper cancelled replacement',"C'est",[],'medium','The initial and apostrophe are visible, while the final letters overlap the lower run.')
doubt('Upper cancelled replacement before doute','sans',[],'medium','The short a/n sequence is compressed.')
doubt('Final main paragraph opening','Ou bien',[],'medium','A marginal leader crosses the first short word; bien is clearer.')
doubt('Bottom marginal cancellation','faisant le chgt de base',[],'medium','The heavy strike prevents every letter from being read; chgt is not expanded.')
doubt('Bottom marginal replacement','prenant',[],'medium','The p-descender is clear but the central run remains compressed.')

def audit(box_id,kind,coords,reading):
    x0,y0,x1,y1=coords
    report['audit_boxes'].append(dict(box=box_id,kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
audit('b01','number',boxes['c01'],r'\uline{Théorème 2}')
audit('b02','formula',boxes['c02'],'$'+map_formula+'$')
audit('b03','prose',boxes['c03'],r'des catégories des t.f. de')
audit('b04','margin (slanted)',boxes['c04'],upper)
audit('b05','prose',[299,477,999,588],'Si deux hom.')
audit('b06','insertion',boxes['c06'],r'des hom de groupoïdes \inserted{sur $\Pi_{\mathbb Q}$} isomorphes')
audit('b07','diagram',boxes['c07'],tri)
audit('b08','insertion',boxes['c08'],r"l'e\deleted{isom}\inserted{carré}")
audit('b09','deletion',boxes['c09'],r'\deleted{correspondant}')
audit('b10','diagram',boxes['c10'],square)
audit('b11','prose',boxes['c11'],r'est commutatif) alors $f=g$.')
audit('b12','deletion',boxes['c12'],r"\deleted{\unsure{qui ne|qu'on} \unsure{peut}} de $K'$, ")
audit('b13','insertion',boxes['c13'],r"d'une clôture alg. choisie $\bar K'$ "+first_insert)
audit('b14','deletion',boxes['c14'],r"que \deleted{les deux hom d'exten}")
audit('b15','insertion',[343,1568,1655,1805],long_insert+r' \deleted{\unsure{disons}}')
audit('b16','margin (slanted)',boxes['c16'],middle)
audit('b17','formula',[560,1705,1428,1878],'$'+display+'$')
audit('b18','prose',boxes['c18'],'sont égaux,')
audit('b19','deletion',boxes['c19'],old_cancel+' '+upper_cancel)
audit('b20','prose',boxes['c20'],r'\unsure{Ou bien}')
audit('b21','prose',boxes['c21'],r'$\overline{\mathbb Q}$ fixée, de $\mathbb Q$,')
audit('b22','prose',boxes['c22'],'deux hom')
audit('b23','margin (slanted)',boxes['c23'],bottom)
audit('b24','number',boxes['c24'],r'\margin{21}')
audit('b25','deletion',[343,1687,604,1770],r'\deleted{\unsure{disons}}')

coverage=[
(1,'editorial-only',None,'Archive/scan markers and H\'s initial editorial note are not manuscript prose.'),
(2,'material','c01','H supplies a stop after the theorem numeral.'),
(3,'material','c02','The source has no mapsto bar; a limited shaft/arrow doubt remains.'),
(4,'material','c03','The ink supports catégories des, against C\'s extensions de.'),
(5,'material','c04','The source separator is one dash, not a colon.'),
(6,'material','c05','The word is marcherait.'),
(7,'material','c06','The note reads de car 0.'),
(8,'material','c07','The demonstration phrase is present; only its compact lead-in remains doubtful.'),
(9,'material','c07','The continuous c\'est ... central argument is recovered; H\'s editorial-note words are excluded.'),
(10,'material','c07','The source continues fait un énoncé ...; the following parenthesis is covered in c08. H\'s oblique dans is editorial wording.'),
(11,'material','c08','The second démon. belongs to the source parenthesis. H\'s description of the margin is editorial.'),
(12,'material','c08','The marginal ending is transcribed with narrowed doubts. H\'s extra I.e. before the proof is separately rejected in c10.'),
(13,'material','c11','No stop follows this hom.'),
(14,'material','c12','The triangle is present here, with its source geometry and heads.'),
(15,'macro-only',None,'This comma is the token from H\'s TeX thin-space command after forall, not extra manuscript punctuation.'),
(16,'material','c13','Both the residual high tick and low e are preserved as literal l\'e; the readable cancelled isom is covered in c14.'),
(17,'macro-only',None,'Ampersand replacement and spacing p f versus pf do not change the reading.'),
(18,'material','c15','The upper horizontal link is an equivalence sign, not a headed arrow.'),
(19,'material','c15','The wave-over-bar equivalence is present.'),
(20,'macro-only',None,'Description-label syntax is rendering syntax; the sign reading itself is covered in c15.'),
(21,'macro-only',None,'Spacing p g versus pg is not a source reading difference.'),
(22,'material','c15','The top-right argument is unbarred, unprimed eta; M1032 resolves to the first C reading.'),
(23,'material','c15','The right vertical shaft has no head.'),
(24,'material','c15','The bottom horizontal link is an equivalence sign, not a headed arrow.'),
(25,'material','c15','The lower wave-over-bar sign is present.'),
(26,'macro-only',None,'Label-placement syntax alone; the sign is already covered in c15.'),
(27,'reading-agrees',None,'The crop resolves M1033 to est, agreeing with the first C reading and H.'),
(28,'material','c12','H relocates the triangular diagram after f=g; its source position is retained.'),
(29,'material','c18','H moves de K-prime beside the chosen closure; the source places it on the lower baseline after the insertion.'),
(30,'material','c16','The short cancellation retains a qui ne/qu\'on doubt and the crossed peut.'),
(31,'material','c17','The first decorated field has an overhead stroke and a doubtful epsilon-like lower curl.'),
(32,'material','c17','The source has a comma and a second uncertainly decorated K, with no inserted et.'),
(33,'material','c17','The insertion ends de K; the following baseline de K-prime is separately covered in c18.'),
(34,'material','c20','The cancelled hom has no stop.'),
(35,'material','c19','There is one live que before the strike, not a cancelled que plus a new que.'),
(36,'material','c21','Donc is present in the long replacement.'),
(37,'material','c22','The source has de telle façon ... in the replacement; cancelled disons and the marginal opening are covered in c24/c25.'),
(38,'material','c26','The source quotation marks are paired ticks, not guillemets.'),
(39,'material','c27','The cancelled token, barred Q, de Q and dans are present in the middle margin.'),
(40,'material','c27','No added de follows the second decorated K.'),
(41,'material','c28','Celle is singular in the source.'),
(42,'material','c22','H supplies sorte and misplaces this clause; façon is written in the earlier replacement.'),
(43,'material','c31','The source reads sont, not soient.'),
(44,'material','c32','The cancelled material contains two distinct runs; the lower starts Il s\'agit.'),
(45,'material','c32','The upper cancelled run is C\'est sans doute plus, with local doubts; it is not live Ceci s\'exprime.'),
(46,'material','c32','The lower conclusion belongs to the cancelled run; the separate Ou bien is recorded in c33.'),
(47,'material','c34','The comma after fixée is visible.'),
(48,'material','c35','No stop follows the final hom.'),
(49,'material','c36','Doit is present in the bottom note.'),
(50,'material','c36','The source has infinitive ramener, without an accent on the e.'),
(51,'macro-only',None,'Three TeX hyphens and H\'s em dash encode the same single source dash.'),
(52,'material','c38','The cancelled abbreviation is chgt, not the expanded changement.'),
(53,'material','c39','The note has tentative prenant, then extension finie de Q; H\'s catégories finies sur is unsupported.'),
(54,'material','c41','The thin foliation 21 is source ink. H\'s marginal-note description is editorial and excluded.')
]
report['diff_coverage']=[dict(row=r,classification=k,change_id=c,reason=e) for r,k,c,e in coverage]
# Synchronize prime spelling in all strings, including quoted witness strings and inventory.
def prime_sync(value):
    if isinstance(value,str): return value.replace('\\prime',"'")
    if isinstance(value,list): return [prime_sync(x) for x in value]
    if isinstance(value,dict): return {k:prime_sync(v) for k,v in value.items()}
    return value
report=prime_sync(report)
(root/'edition/reviews/149_scan022.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
