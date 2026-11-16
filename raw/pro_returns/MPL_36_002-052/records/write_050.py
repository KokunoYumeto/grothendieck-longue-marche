from save_page import save
tex=r'''
\scanpage{50}
biextension \deleted{\unsure{de}} de $P,Q$ par $G$, et où $(E',\varphi)$ est le couple d'une biext. $E'$ de $P',Q$ par $G$ et d'un hom
\diagram{\begin{tikzcd}\varphi:T_\Pi(P)\times T_\Pi(Q)\arrow[r]&T_\Pi(G)\end{tikzcd}}
\uline{qui étend l'hom}
\diagram{\begin{tikzcd}\deleted{\unsure{\varphi}}\ \varphi_{\Pi,E'}:T_\Pi(P')\times T_\Pi(Q)\arrow[r,no head]&T_\Pi(G)\end{tikzcd}}

\margin{\fbox{\begin{minipage}{.65\linewidth}
$\unsure{2}$\quad\uline{NB} On considère les $T_\Pi(P)$ comme syst. projectifs \deleted{par suite} \deleted{\uline{\unsure{stricts}}}, \inserted{\unsure{elle est vraie}} cette description \unsure{ne marche que} \deleted{\unsure{en} \unsure{termes} de syst. projectifs (\unsure{sans passage à la limite})} si $\forall p\in\Pi$ on a $pP'=P'$, $\unsure{pP''=pP''|pP''=P''}$ donc $\unsure{pP=pP|pP=P}$. Sinon, il faut garder le syst. des ${}_nP\times{}_nQ\mathbin{-}{}_nG$ \deleted{\unsure{prolongeant} ${}_nP'\times{}_nQ\mathbin{-}{}_nG$} avec la compatibilité \unsure{pour} \deleted{\unsure{un et}} \unsure{les restrictions} aux $\deleted{\unsure{\times}}{}_nP'\times{}_nQ\ \ldots$
\end{minipage}}}

\uline{Corollaire 1} Soient deux suites exactes
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r,no head]&P'\arrow[r,no head]&P\arrow[r,no head]&P''\arrow[r,no head]&0\\
0\arrow[r,no head]&Q'\arrow[r,no head]&Q\arrow[r]&Q''\arrow[r]&0
\end{tikzcd}}
et supposons que, pour un $\Pi$ de nbs premiers, on ait :
\[
\text{a)}\quad p\in\Pi\Longrightarrow\uline{pP=P},\quad\uline{pQ'=Q'}\quad
\deleted{\unsure{et}\ pQ''=Q''\ \unsure{ou}\ pP''=P''}
\]
\inserted{(ou le symétrique)}
\margin{\deleted{(donc $pP=P$, $pQ=Q$)}}
\[
\text{b)}\quad\text{les}\quad\varinjlim_{n\to\Pi}{}_nP\longrightarrow P''\quad\text{et}\quad
\varinjlim_{n\to\Pi}{}_nQ\mathbin{-}Q''\quad\text{épim.}
\]
\figure{\begin{tikzpicture}\draw (0,.1)..controls (.4,.2) and (.8,-.1)..(1.4,.1)..controls (1.8,.2) and (2,-.1)..(2.4,.1);\end{tikzpicture}}
\margin{\fbox{\begin{minipage}{.65\linewidth}
\unsure{Ne vaut que}, celle en modules tel quel que si on suppose que $P',Q;P'',Q'$ sont $\Pi$ divisibles dans a), en plus de b). Sinon, garder les ${}_nP\times{}_nQ\longrightarrow{}_nG\ \ldots$
\end{minipage}}}

Alors le foncteur
\diagram{\begin{tikzcd}E\arrow[r,mapsto]&(E',\varphi)\end{tikzcd}}
\unsure{associant à} les biext. de $P,Q$ par $G$ \unsure{la restriction} $E':P',Q'$ et la forme $\varphi_{E,\Pi}$
\diagram{\begin{tikzcd}\varphi:T_\Pi(P)\times T_\Pi(Q)\arrow[r,no head]&T_\Pi(G)\end{tikzcd}}
prolongeant
\diagram{\begin{tikzcd}\varphi_{E',\Pi}:T_\Pi(P')\times T_\Pi(Q')\arrow[r,no head]&T_\Pi(G)\end{tikzcd}}
est une équivalence de catégories.

\uline{Dém.} \inserted{Supposons p.ex.} On applique d'abord le \deleted{\unsure{proposition}} corollaire 1 à
\diagram{\begin{tikzcd}[column sep=small]0\arrow[r,no head]&P'\arrow[r]&P\arrow[r,no head]&P''\arrow[r,no head]&0\end{tikzcd}}
et $Q'$, en utilisant $pQ'=Q'$, $\varinjlim{}_nP\longrightarrow P''$ épim.

Cela donne une description des biextensions de $P,Q'$. On applique ensuite le sym. du cor. 1 à $P$ et
\diagram{\begin{tikzcd}[column sep=small]0\arrow[r,no head]&Q'\arrow[r]&Q\arrow[r]&Q''\arrow[r]&0\end{tikzcd}}
en utilisant $pP=P$ \deleted{$\unsure{pP''=P''}$} et $\varinjlim_{n\to\Pi}{}_nQ\mathbin{-}Q''$ épim.
\margin{49}
'''
e=[('text','top continuation','biextension de P,Q par G'),('deletion','top line','de'),('diagram','first display','φ:T_Π(P)×T_Π(Q)→T_Π(G)'),('text','right of first display','qui étend l’hom'),('diagram','second display','φ_{Π,E′}:T_Π(P′)×T_Π(Q)—T_Π(G)'),('deletion','before second display','φ'),('margin note','upper right boxed','NB On considère les T_Π(P) comme syst. projectifs'),('deletion','inside upper-right note','par suite; stricts; terms of projective systems; prolongeant'),('insertion','inside upper-right note','elle est vraie'),('text','new corollary','Corollaire 1 Soient deux suites exactes'),('diagram','two exact sequences','0—P′—P—P″—0 / 0—Q′—Q→Q″→0'),('text','hypothesis introduction','et supposons que, pour un Π'),('display','hypothesis a','p∈Π⇒pP=P,pQ′=Q′'),('deletion','after hypothesis a','et pQ″=Q″ ou pP″=P″'),('insertion','above deleted part of a','ou le symétrique'),('margin note','right of a, cancelled','donc pP=P,pQ=Q'),('display','hypothesis b','lim _nP→P″ et lim _nQ—Q″ épim.'),('drawing','under first limit','wavy underline'),('margin note','middle right boxed','Ne vaut que, celle en modules tel quel'),('text','main conclusion introduction','Alors le foncteur'),('diagram','functor','E↦(E′,φ)'),('text','explanation of functor','associant à les biext. de P,Q'),('diagram','pairing on P,Q','φ:T_Π(P)×T_Π(Q)—T_Π(G)'),('text','between pairings','prolongeant'),('diagram','pairing on P′,Q′','φ_{E′,Π}:T_Π(P′)×T_Π(Q′)—T_Π(G)'),('text','conclusion','est une équivalence de catégories'),('text','proof','Dém. On applique d’abord'),('insertion','above proof opening','Supposons p.ex.'),('deletion','before corollaire 1','proposition'),('diagram','proof first exact sequence','0—P′→P—P″—0'),('text','proof first application','et Q′, en utilisant'),('text','proof second application','Cela donne une description'),('diagram','proof second exact sequence','0—Q′→Q→Q″→0'),('deletion','last line','pP″=P″'),('text','last line','en utilisant pP=P et lim _nQ—Q″ épim.'),('margin note','bottom left','49')]
d=[{'line':'first line cancelled word','reading':'de','alternatives':'crossed word before live de','confidence':'low'},{'line':'upper-right NB, added qualification','reading':'elle est vraie; ne marche que; en termes de syst. projectifs (sans passage à la limite)','alternatives':'overwritten connective and cancellation layering unresolved','confidence':'low'},{'line':'upper-right NB divisibility equations','reading':'pP″=pP″; pP=pP','alternatives':'pP″=P″; pP=P; preceding p-like strokes visible but uncertain','confidence':'low'},{'line':'upper-right NB final compatibility words','reading':'pour les restrictions aux _nP′×_nQ','alternatives':'several words overwritten','confidence':'low'},{'line':'smaller boxed marginal note','reading':'Ne vaut que, celle en modules tel quel que si on suppose que','alternatives':'opening words very compressed; the Π-divisibility qualification and finite-level pairing are clearer','confidence':'low'},{'line':'functor explanation','reading':'associant à ... la restriction','alternatives':'abbreviated grammar and endings uncertain','confidence':'low'},{'line':'limit indexing','reading':'n→Π','alternatives':'shorthand n composed of primes in Π possible, but not expanded in transcription','confidence':'medium'}]
save(50,tex,e,d,'Continuation of048 across intervening reused typescript049. A second “Corollaire 1” treats exact sequences in both variables and is proved by two applications of the one-variable statement. The boxed NB explicitly treats T_Π as projective systems; its correction about a description “en modules”, Π-divisibility, and retaining compatible finite-level pairings is mathematically central but palaeographically weak. Do not silently collapse the system into its inverse limit, or regard the boxed marginal caveats as optional. Research should compare live statement, marginal qualification, and the proof rather than assign the cancelled formulas theorem status.')
