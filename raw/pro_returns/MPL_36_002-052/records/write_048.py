from save_page import save
tex=r'''
\scanpage{48}
\diagram{\begin{tikzcd}[column sep=small]0\arrow[r,no head]&P'\arrow[r,no head]&P\arrow[r,no head]&P''\arrow[r,no head]&0&Q\end{tikzcd}}
\deleted{$\unsure{nP''=0}$}
\[\text{a)}\quad nQ=Q\qquad\text{b)}\quad {}_nP\longrightarrow P''\quad\text{épimorphisme}\]
Toute biextension \inserted{$E$} de $P\times Q$ \deleted{\unsure{définit}} par $G$ définit

a) Une biextension \inserted{$E'$} de $P'\times Q$ par $G$

d'où un accouplement
\diagram{\begin{tikzcd}{}_nP'\times{}_nQ\arrow[r,"E'(n)"]&G\end{tikzcd}}
\margin{\deleted{\unsure{Si} la suite $0\longrightarrow P'\longrightarrow P\longrightarrow P''\longrightarrow0$ est \unsure{splittée} \deleted{\unsure{ou}} ou elle est
\[\deleted{\operatorname{Hom}(P\otimes Q,G)\longrightarrow\operatorname{Hom}(P'\otimes Q,G)}\]
\uline{\unsure{loc.}} \uline{\unsure{splittée}} et
\[\underline{\operatorname{Hom}}(\unsure{P'|P''}\otimes Q,G)=0\]}}

b) Une biextension de ${}_nP\times Q$ par $G$, i.e. un accouplement
\diagram{\begin{tikzcd}{}_nP\times{}_nQ\arrow[r,"\varphi"]&G\end{tikzcd}}

\deleted{\unsure{Donc le}} Ces deux $(E',\varphi)$ satisfont la condition que
\[\varphi|({}_nP'\times{}_nQ)=E'(n)\]

Un hom de biextensions $E_1\longrightarrow E_2$ définit un hom $(E'_1,\varphi_1)\mathbin{-}(\unsure{E_2|E'_2},\varphi_2)$, i.e. \inserted{(déf.)} un hom de biextensions $u:E'_1\longrightarrow E'_2$, tel que $\varphi\sim$

\uline{Je dis que le foncteur} $E\longmapsto(E',\varphi)$ \uline{est une équiv. de catégories.}

\deleted{\deleted{a) \unsure{pl. fid.}}\quad\deleted{b) \unsure{pl. fid.}}
\[
\deleted{\text{a)}\quad\operatorname{Hom}(P\otimes Q,G)\xrightarrow{\sim}\operatorname{Hom}(P'\otimes Q,G)}
\]
\[\deleted{\text{b)}\quad E_1\simeq E_2\quad\text{ssi}\quad(E'_1,\varphi_1)\simeq(E'_2,\varphi_2)}\]
\uline{Pl. fidèle} signifie aussi que $E\leftarrow E'(P',Q)$ est pl. fid., ou encore, par la suite exacte, que
\[
(*)\quad\operatorname{Hom}(P''\otimes Q,G)=0,\qquad
(**)\quad\operatorname{Hom}(P\otimes Q,G)\longrightarrow\operatorname{Hom}(P'\otimes Q,G)\quad\uuline{\text{surj.}}
\]
\deleted{\unsure{Ce qui est} \illegible{2}}
\deleted{$(***)$ si $\unsure{E\simeq1}$ tel que $(E',\varphi)$ \illegible{1} \unsure{alors} $\unsure{E\simeq1}$}
\inserted{Si $E$ est tel que $E'\simeq1$, $\varphi=0$, alors $E\simeq1$}

La première assertion résulte de a) et b) qui impliquent $P''\otimes Q=0$; la deuxième résulte de c) [dans la démonstration de c), les deux \unsure{objets} de $(**)$ sont nuls!].

\deleted{\uline{\unsure{Ess. surj.}}} Pour $(***)$, on note que si $E'=0$, alors par la suite exacte $E$ est déterminé par un élément de $\operatorname{Ext}^1(P''\otimes^LQ,G)$, \unsure{or ceci équivaut à} un élément de $\operatorname{Hom}(P''\otimes_1Q,G)$, on trouve que c'est ce qui définit $\varphi$, on gagne.}

\uline{Corollaire 1} Supposons, pour un $\Pi$ de nbs premiers que
\[\left(\varinjlim_{\substack{n\\\text{\unsure{composé}}\ \Pi}}{}_nP\right)\longrightarrow P''\quad\text{surjectif},\qquad\text{et que}\quad p\in\Pi\Longrightarrow pQ=Q.\]
Alors on a une équivalence $E\longmapsto(E',\varphi)$, où $E'$ est une
\margin{47}
'''
e=[('diagram','top','0—P′—P—P″—0; Q'),('deletion','before hypotheses','nP″=0'),('display','hypotheses','a) nQ=Q; b) _nP→P″ épimorphisme'),('text','upper paragraph','Toute biextension de P×Q'),('insertion','above biextension','E'),('deletion','after P×Q','définit'),('text','item a','Une biextension de P′×Q'),('insertion','above item a','E′'),('text','under item a','d’où un accouplement'),('diagram','first pairing','_nP′×_nQ→G, E′(n)'),('margin note','upper right bracketed','Si la suite ... est splittée'),('deletion','entire upper-right note','split sequence, Hom restriction and vanishing'),('display','inside upper-right note','Hom(P⊗Q,G)→Hom(P′⊗Q,G); underlined Hom(P′⊗Q,G)=0'),('text','item b','Une biextension de _nP×Q'),('diagram','second pairing','_nP×_nQ→G, φ'),('deletion','before compatibility paragraph','Donc le'),('text','compatibility paragraph','Ces deux (E′,φ) satisfont'),('display','compatibility','φ|(_nP′×_nQ)=E′(n)'),('text','middle paragraph','Un hom de biextensions E₁→E₂'),('insertion','above i.e. un hom','(déf.)'),('text','underlined assertion','Je dis que le foncteur ... équiv. de catégories'),('deletion','large lower block','crossed proof attempt'),('deletion','start of proof block','a) pl. fid.; b) pl. fid.'),('display','first cancelled condition','a) Hom restriction isomorphism'),('display','second cancelled condition','b) E₁≃E₂ ssi pairs isomorphic'),('text','cancelled proof heading and paragraph','Pl. fidèle signifie aussi'),('display','cancelled conditions (*) and (**)','Hom(P″⊗Q,G)=0; Hom restriction surj.'),('deletion','heavily crossed extra lines','Ce qui est ...; (***) si E ...'),('insertion','between crossed line and next paragraph','Si E est tel que E′≃1,φ=0,alors E≃1'),('text','cancelled proof continuation','La première assertion résulte de a) et b)'),('deletion','crossed subheading','Ess. surj.'),('text','cancelled final argument','Pour (***), on note que si E′=0'),('text','bottom corollary','Corollaire 1 Supposons, pour un Π'),('display','corollary hypothesis','lim _nP→P″; p∈Π⇒pQ=Q'),('text','last line incomplete','Alors on a une équivalence ... où E′ est une'),('margin note','bottom left','47')]
d=[{'line':'crossed initial condition','reading':'nP″=0','alternatives':'overwritten expression before a)','confidence':'low'},{'line':'upper-right crossed note','reading':'Si la suite ... est splittée ... ou elle est loc. splittée et Hom(P′⊗Q,G)=0','alternatives':'compressed connective; P″ possible in final Hom argument','confidence':'low'},{'line':'homomorphism of pairs paragraph','reading':'E₂ without prime in second pair','alternatives':'E′₂; prime not securely visible','confidence':'low'},{'line':'heavily crossed proof lines after (**)','reading':'Ce qui est [2 unreadable words]; (***) si E≃1 ... [1 unreadable word] ...','alternatives':'hatching physically obscures words; surviving mathematical symbols given as unsure','confidence':'low'},{'line':'cancelled proof functor','reading':'E←E′(P′,Q)','alternatives':'direction and apostrophe closely overlap cancellation strokes','confidence':'low'},{'line':'bracket in cancelled proof','reading':'les deux objets de (**) sont nuls','alternatives':'objets uncertain','confidence':'low'},{'line':'last cancelled paragraph connector','reading':'or ceci équivaut à','alternatives':'compressed phrase','confidence':'low'},{'line':'corollary limit index','reading':'n composé Π','alternatives':'qualifying word not fully resolved','confidence':'low'}]
save(48,tex,e,d,'The live assertion is an equivalence between biextensions E and compatible pairs (E′,φ), under nQ=Q and surjectivity _nP→P″. A substantial attempted proof (including Hom restriction, derived tensor, and Tor/⊗₁) is crossed out; it remains evidence of a method, not an accepted proof. The final corollary passes to Π-primary torsion and continues on049. The phrase “tel que φ∼” is unfinished; no compatibility equation has been supplied. Cancellations in the dense proof and upper-right note are among the least secure readings in the package.')
