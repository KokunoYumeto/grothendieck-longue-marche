import sys
sys.path.insert(0,'/workspace/scratch/74077fe5e995/MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{42}
\margin{\unsure{Commencer}\par\unsure{Voir ça}\par\unsure{Voir} \unsure{dans le livre de} \illegible{1}\par\unsure{puis au corollaire}}
\figure{\begin{tikzpicture}[x=.25cm,y=.6cm]\draw (1,8) .. controls (-.1,8.6) and (.2,7.5) .. (.6,6.7) .. controls (1.5,5.8) and (1,5.1) .. (0,5) .. controls (1,4.9) and (1.5,4.4) .. (.7,3.3) .. controls (.2,2.5) and (0,1.3) .. (1,1);\end{tikzpicture}}
Soit $B$ un anneau avec unité et un groupe fini $G$ d'automorphismes. $A=B^G$. On pose $\operatorname{Tr}_G b=\sum_{g\in G}gb$. Conditions équivalentes, ($q$ est un entier donné) ; $A$ est un sous-anneau, et $\operatorname{Tr}_G:B\longrightarrow A$ est un hom de bi-$A$-modules
\[
\begin{array}{ll}
a)&A=\operatorname{Tr}_G B\quad\text{i.e.}\quad\widehat H^0(G,B)=\{0\}\\
a')&1=\operatorname{Tr}_G b\quad\text{avec }b\in B\\
\unsure{b})&\widehat H(G,M)=0\quad\text{pour }\unsure{\forall}\ (B,G)\text{-modules }M\\
\unsure{b(q)})&\widehat H^q(G,M)=0\qquad\rule{4cm}{.3pt}
\end{array}
\]

Démonstration : $a)\Rightarrow a')$ trivial, $a'\Rightarrow b$ car on a, en désignant par $\varphi_M(b)$ l'homothétie dans $M$ définie par un $b\in B$ :
\[
g\varphi_M(b)g^{-1}=\varphi_M(gb)\quad\text{d'où}\quad\varphi_M(\operatorname{Tr}_G b)=\operatorname{Tr}_G\varphi_M(b),
\]
d'où le

\uline{Corollaire} Si $\lambda\in\operatorname{Tr}_G B$, l'homothétie $\lambda$ dans $\widehat H(G,M)$ est \uline{nulle}
[et la condition est \unsure{manifestement} nécessaire, en prenant $M=B$)

qui implique $a'\Rightarrow b$. $b\Rightarrow b(q)$ trivial. Or $b(q)\Rightarrow b(q+1)$ car on a
\diagram{\begin{tikzcd}
0\arrow[r]&M\arrow[r]&M\otimes_Z Z(G)\arrow[r]&N\arrow[r]&0\\
&m\arrow[r,mapsto]&\sum m\otimes g
\end{tikzcd}}
où on met dans le terme médian la \deleted{\unsure{$B$}} structure de $B$-module définie par $\lambda(m\otimes g)=\lambda m\otimes g$, et la structure de $G$-module définie par $g'(m\otimes g)=g'm\otimes g'g$, alors
\[
g'.(\lambda[m\otimes g])=(g'.\lambda)(g'.[m\otimes g])
\]
car ces deux mb. sont resp\textsuperscript{t}
\[
g'.(\lambda m\otimes g)=g'(\lambda m)\otimes g'g
\]
et
\[
(g'\lambda)(g'm\otimes g'g)=(g'\lambda)(g'm)\otimes g'g
\]
c'est le $=$ cherché car $g'.(\lambda m)=(g'.\lambda)(g'.m)$. Alors on a, puisque
\[
\widehat H(G,M\otimes_Z Z(G))=0,\quad\widehat H^{q+1}(G,M)=\widehat H^q(G,N)=0.
\]
On prouve de façon \unsure{analogue} $b(q)\Rightarrow b(q-1)$, d'où $b(q)\Rightarrow b(0)$. Mais $b(0)\Rightarrow a$ trivialement.

\uline{Corollaire} Supposons $B$ \inserted{commutatif} intègre et intégralement clos, \inserted{$A$ local.} les conditions de la proposition sont vérifiées si l'indice de ramification $e$ de $B$ sur $A$ (= ordre du groupe d'inertie) \deleted{\unsure{étant premier à la} \inserted{\unsure{car. résiduelle}} \unsure{égale caractéristique} (supposée $\ne0$) \unsure{plus trivialement s'il existe un} $\alpha\in B$ tel que $e\alpha=1$.} est inversible dans $A$, i.e. une unité dans $A/\unsure{\mathfrak r(A)|\operatorname{rad}(A)}$ \deleted{\unsure{$=0$}}
\figure{\begin{tikzpicture}[x=.25cm,y=.6cm]\draw (0,3.5)--(.02,0);\end{tikzpicture}}

\margin{41}
'''
elements=[('margin note','upper left vertical','Commencer; Voir ça; Voir dans le livre de ...'),('drawing','left of first statement','long curved brace'),('text','top','Soit B un anneau avec unité'),('display','top inline','A=B^G'),('display','top inline','Tr_G b=∑gb'),('text','top','Conditions équivalentes'),('text','top continuation','A est un sous-anneau'),('display','top inline','Tr_G:B→A'),('text','top continuation','un hom de bi-A-modules'),('display','upper','a) A=Tr_G B i.e. Hhat0(G,B)={0}'),('display','upper','a′) 1=Tr_G b avec b∈B'),('display','upper','b) Hhat(G,M)=0'),('display','upper','b(q)) Hhatq(G,M)=0'),('drawing','upper right ditto line','long horizontal line'),('text','middle','Démonstration'),('display','middle inline','a)⇒a′); a′⇒b'),('text','middle','car on a, en désignant'),('display','middle','gφ_M(b)g^-1=φ_M(gb)'),('display','middle','φ_M(Tr_G b)=Tr_G φ_M(b)'),('text','middle','d’où le'),('text','middle','Corollaire Si λ∈Tr_G B'),('display','middle inline','Hhat(G,M)'),('text','middle bracketed','et la condition est manifestement nécessaire'),('text','middle','qui implique a′⇒b'),('display','middle inline','b⇒b(q), b(q)⇒b(q+1)'),('text','middle','car on a'),('diagram','middle','0→M→M⊗_Z Z(G)→N→0; m↦∑m⊗g'),('text','middle','où on met dans le terme médian'),('deletion','before structure','B'),('display','middle inline','λ(m⊗g)=λm⊗g'),('text','middle','et la structure de G-module'),('display','middle inline','g′(m⊗g)=g′m⊗g′g'),('display','middle','g′.(λ[m⊗g])=(g′.λ)(g′.[m⊗g])'),('text','middle','car ces deux mb. sont respt'),('display','middle','g′.(λm⊗g)=g′(λm)⊗g′g'),('display','middle right','(g′λ)(g′m⊗g′g)=(g′λ)(g′m)⊗g′g'),('text','middle lower','c’est le = cherché car'),('display','middle lower inline','g′.(λm)=(g′.λ)(g′.m)'),('text','middle lower','Alors on a, puisque'),('display','middle lower','Hhat(G,M⊗_Z Z(G))=0'),('display','middle lower','Hhat^{q+1}(G,M)=Hhat^q(G,N)=0'),('text','lower','On prouve de façon analogue'),('display','lower inline','b(q)⇒b(q-1); b(q)⇒b(0)'),('text','lower','Mais b(0)⇒a trivialement'),('text','bottom','Corollaire Supposons B intègre'),('insertion','above intègre','commutatif'),('insertion','after clos','A local'),('text','bottom','les conditions de la proposition'),('display','bottom inline','e; B; A; ordre du groupe d’inertie'),('deletion','bottom three lines','étant premier à la ... égale caractéristique ...'),('insertion','within deleted condition','car. résiduelle'),('display','inside deleted condition','α∈B; eα=1'),('text','bottom','est inversible dans A'),('display','bottom','A/r(A)|A/rad(A)'),('deletion','bottom after quotient','=0'),('drawing','left of bottom corollary','vertical line'),('margin note','bottom left','41')]
save(42,text,elements,observations='Whole and both halves personally read; 3× and 4× crops used for every compressed section, the rotated margin, both condition labels, and the deleted corollary. The margin remains particularly low-confidence; an attempted personal-name reading after livre de could not be recovered from the ink and one word is marked illegible. The last corollary contains several alternative formulations with overlapping strike-throughs; scope and readings are marked rather than harmonized. Plain Z in the group-ring formulas retained. The source bracket/parenthesis mismatch in the first corollary is retained.')
