from save_page import save
tex=r'''\scanpage{52}
\uline{Biextensions \unsure{sous hyp. de} rigidité}

$A,G$ faisceaux abéliens sur topos $S$, $f:A\longrightarrow S$
\margin{\diagram{\begin{tikzcd}[column sep=small] S\arrow[r,no head]&\text{objet final}\end{tikzcd}}}

a) Supposons $\underline{\operatorname{Hom}}_{\unsure{grs|gr}}(A,G)\simeq0$. Alors
\[
\operatorname{Ext}^1(A,G)\xrightarrow{\sim}H^0(S,\underline{\operatorname{Ext}}(A,G))
\]
donc la connaissance du \uline{faisceau} $\underline{\operatorname{Ext}}(A,G)$ implique celle de $\operatorname{Ext}(A,G)$ \unsure{et ts des} $\operatorname{Ext}(A_{\unsure{T|S}},G_{\unsure{T|S}})$.

b) Supposons $\underline{\operatorname{Hom}}_{\unsure{pct|pt}}(A,G)=0$, Alors
\margin{i.e. $f_*(G_A)\xleftarrow{\sim}G$}
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0,-.35);\node[anchor=north,align=left] at (1.8,-.35) {\unsure{Hom (pas nécessairemt additifs)}\\qui \unsure{respectent} les sections\\unités};\end{tikzpicture}}}
\[
H^1(A,\unsure{A_G|G_A})\simeq H^1(S,G)\times H^0(S,R^1f_*(G_A))
\]
\diagram{\begin{tikzcd}[row sep=small]
H^0(S,R^1f_*(G_A))\arrow[d,phantom,"\rotatebox{90}{$\simeq$}"]\\
\text{Classes à isom près de $G_A$-torseurs}\quad\deleted{\unsure{fou}}\ \text{rigidi\uline{fiés} rel. à $e_A$}\arrow[d,phantom,"\rotatebox{90}{$\simeq$}"]\\
\text{Classes de \deleted{torseurs} $G_A$-torseurs rigidi\uline{fiables} rel. à $e_A$.}
\end{tikzcd}}
\margin{\figure{\begin{tikzpicture}[scale=.5]\draw(0,0)--(.4,.05)--(.05,.18)--(.12,.66)--(.32,.49)--(.17,.3)--(.38,.4)--(.31,.65)--(.08,.47)--(.21,.08)--(.49,.17)--(.5,.02)--(.05,.03);\end{tikzpicture}}}

De plus, le foncteur oubli, qui va de la catégorie des extensions de $A$ par $G$ en la catégorie des $G_A$-torseurs $e_A$-rigidifiés, est un fonct. pl. fid. (de catégories discrètes), (i.e. on a une \uline{injection}
\[
0\longrightarrow\operatorname{Ext}^1(A,G)\longrightarrow H^1(A,G_A)
\]
); l'image essentielle est formée des \deleted{\unsure{classes}\inserted{\unsure{fib}}} $G_A$-torseurs tels que \deleted{\unsure{classes.}\quad\xi\quad\unsure{telles}}
\[
\pi^*(\deleted{\unsure{F}}L)\simeq\operatorname{pr}_1^*(L)\operatorname{pr}_2(L)
\]
i.e tels que
\[
\pi^{\unsure{*|\alpha}}(L)\operatorname{pr}_1^*(L)^{-1}\operatorname{pr}_2^{\unsure{*|\alpha}}(L)^{-1}\simeq0.
\]
On trouve encore comme \unsure{corollaire} une suite exacte
\margin{\diagram{\begin{tikzcd}[column sep=large]
A\times A\arrow[r,shift left=2.5ex,"\operatorname{pr}_1"]\arrow[r,"\operatorname{pr}_2"]\arrow[r,shift right=2.5ex,"\pi"']&A
\end{tikzcd}}}
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
0\arrow[r,no head]&\underline{\operatorname{Ext}}^1(A,G)\arrow[r,"i"]&R^1f_*(G_A)\arrow[r,"j"]\arrow[d,"k"']&\underline{\operatorname{Tors}}\ \underline{\mathrm{birig}}\ \underline{\mathrm{sym}}(A,A;G)\\
\text{i.e.}&0\arrow[r]&\underline{\mathrm{NS}}(A)\arrow[r,"\deleted{\unsure{k}}","j'"']&\underline{\operatorname{Tors}}\ \underline{\mathrm{birig}}\ \underline{\mathrm{sym}}(\unsure{A|B},A;G)\arrow[u,"\unsure{i}"]\arrow[u,phantom,shift right=3ex,"\text{''}"]
\end{tikzcd}}
\margin{51}
'''
e=[('text','top title','Biextensions sous hyp. de rigidité'),('text','top','A,G faisceaux abéliens sur topos S; f:A→S'),('margin note','top right','objet final'),('text','upper','a) Supposons Hom_grs(A,G) ≃ 0. Alors'),('display','upper','Ext^1(A,G) → H^0(S,Ext(A,G))'),('text','upper middle','donc la connaissance du faisceau'),('text','middle','b) Supposons Hom_pct(A,G)=0, Alors'),('margin note','middle right','i.e. f_*(G_A) ← G'),('margin note','under Hom subscript','Hom (pas nécessairemt additifs) qui respectent les sections unités'),('display','middle','H^1(A,A_G) ≃ H^1(S,G) × H^0(S,R^1f_*(G_A))'),('diagram','middle right downward','Classes à isom près, rigidifiés; Classes de G_A-torseurs rigidifiables'),('deletion','middle right','fou; torseurs'),('drawing','middle left','small blue crossed pen mark'),('text','lower','De plus, le foncteur oubli'),('display','lower','0 → Ext^1(A,G) → H^1(A,G_A)'),('text','lower','l’image essentielle est formée'),('deletion','lower essential image sentence','classes / fib; classes. xi telles'),('insertion','above classes','fib'),('display','lower','pi^*(L) ≃ pr_1^*(L)pr_2(L)'),('deletion','lower pullback formula','F before L'),('text','lower','i.e tels que'),('display','lower','pi^*(L)pr_1^*(L)^-1 pr_2^*(L)^-1 ≃ 0'),('text','bottom','On trouve encore comme corollaire une suite exacte'),('diagram','bottom left margin','A × A with three arrows pr_1, pr_2, pi to A'),('diagram','bottom','0—Ext^1→R^1f_*→Tors birig sym; k downward to NS; j prime'),('deletion','bottom diagram above j prime','overwritten k'),('margin note','lower left','51')]
d=[{'line':'title','reading':'sous hyp. de','alternatives':'small compressed words','confidence':'medium'},{'line':'a) Hom subscript','reading':'grs','alternatives':'gr','confidence':'medium'},{'line':'after connaissance','reading':'et ts des; T','alternatives':'word ts uncertain; S as subscript','confidence':'low'},{'line':'b) Hom subscript and explanation','reading':'pct; Hom (pas nécessairemt additifs); respectent','alternatives':'pt; abbreviation endings not clear','confidence':'low'},{'line':'middle cohomology display, left','reading':'A_G','alternatives':'G_A','confidence':'medium'},{'line':'classes of torsors','reading':'fou','alternatives':'crossed beginning of word, perhaps for','confidence':'low'},{'line':'essential image sentence','reading':'classes; fib; classes.; xi telles','alternatives':'multiple struck word starts','confidence':'low'},{'line':'pullback identity','reading':'deleted F; superscript *','alternatives':'deleted character uncertain; alpha-like star shape','confidence':'medium'},{'line':'before exact sequence','reading':'corollaire','alternatives':'compressed ending','confidence':'medium'},{'line':'last diagram','reading':'deleted k; i; (A,A;G)','alternatives':'scribbled letter; upward-arrow label; (B,A;G)','confidence':'low'}]
save(52,tex,e,d,'Handwritten title likely Biextensions sous hyp. de rigidité. Claims: internal Hom vanishing gives local-to-global Ext identification; pointed Hom vanishing gives splitting of H^1 and identification of rigidified/rigidifiable torsors; forgetful extension-to-torsor functor fully faithful; essential-image additivity condition; exact sequence toward symmetric birigidified torsors and NS(A). The first cohomology coefficient looks A_G, although G_A appears elsewhere: retained with doubt, not silently exchanged. The first pullback display omits the star at pr_2 in the ink. The full-faithfulness sentence is asserted, not proved here. Bottom diagram is provisional and several strokes remain doubtful. Scan 050 continues 048 across the interposed reused typescript 049; correct the earlier precontext reference to a continuation on 049.',sheet_kind='text')
