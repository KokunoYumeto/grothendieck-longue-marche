from record_page import save_page
save_page(152,7,r'''
\mspage{1'}
\deleted{$\unsure{A}$ \unsure{Prenant le décou}}
\inserted{Si $\Gamma$ n'est pas \inserted{le graphe} ponctuel,} Prenant le découpage de $X$ suivant $|\Gamma|$, on trouve une surface avec un bord connexe, qui est muni de façon naturelle d'une structure de polygone topologique (i.e. avec un ens. fini \inserted{non vide} de sommets donné), et le polygone combinatoire correspondant ne dépend que de $\Gamma$, à isom. can. près. \deleted{\unsure{Voici}}

Si on partait d'un graphe circularisé \deleted{plan} général, la même construction marcherait, mais on trouverait un \uline{contour} comb. (pas néc. connexe), dont voici la construction. Soit $\vec A$ l'ens des \uline{arcs} ($=$ arêtes orientées) de $\Gamma$, $\sigma_\Gamma$ l'involution can. sur $\vec A$ (passage à l'orientation opposée).

\deleted{L'ens $\vec A$ s'identifie \unsure{can$^{t}$} à l'ens des \deleted{\illegible{1}}\inserted{côtés} \unsure{respectifs} (via application : \unsure{face} gauche) des contours $C_i$ (disjoints), et $\unsure{\sigma_\Gamma}$ à \unsure{l'app.} \unsure{qui} \unsure{correspond} \unsure{sur} $C$, \unsure{il} \unsure{revient} à définir $\sigma_\Gamma$.}

\deleted{\deleted{\unsure{Alors}} Sur $\vec A$ on a \inserted{aussi} l'opération $\rho_\Gamma$ (``rotation autour de son sommet'') \unsure{décrite} \deleted{\unsure{par}} \unsure{la} circularisation, avec
\[
S\simeq\vec A/\rho_\Gamma
\]
(si $\Gamma$ n'a pas de sommet isolé).}
\mspage{6}
''',[
('text','top right page number','1 prime'),('deletion','top left before first paragraph','A; Prenant le décou'),('insertion','top, leading into first paragraph','Si Gamma n’est pas ponctuel'),('insertion','inside leading insertion','le graphe'),('text','upper half','Prenant le découpage de X suivant |Gamma|'),('insertion','above fini','non vide'),('deletion','after près','Voici'),('text','middle','Si on partait d’un graphe circularisé'),('deletion','after circularisé','plan'),('deletion','lower first paragraph, crossed through','L’ens vec A s’identifie'),('insertion','within deleted lower paragraph','côtés'),('deletion','within deleted lower paragraph','one overwritten word'),('deletion','bottom paragraph, diagonal cancellations','Sur vec A on a ... rho_Gamma'),('deletion','inside bottom paragraph','Alors; par'),('insertion','inside bottom paragraph','aussi'),('display','inside bottom cancelled paragraph','S simeq vec A/rho_Gamma'),('text','bottom left page number','6')
],observations='Top number 1′ and foot number 6. First paragraph associates a topological polygon to cutting along a nonpoint tree; next broadens to a contour for a general circularized graph. The lower two paragraphs are cancelled but retained. They discuss arcs, the involution sigma_Gamma, a rotation rho_Gamma, and S ≃ vec A/rho_Gamma. Cancellation status must be retained when discussing these statements later; no later resolution presumed during this reading.')
