from page_work import save_page
text=r'''\scanpage{114}
\[
\mu_n^\vee\qquad\mathbb Z/p\mathbb Z\qquad1
\]
\[
\operatorname{Ext}
\]
\[
\boxed{H^i(K,D(\unsure{\widehat G|G}))\simeq
\operatorname{Ext}^{1-i}(f_*G,\mathbb Q/\mathbb Z)}
\]
\[
A(k)
\]
\[
\underset{\sim}{\operatorname{Ext}}^i(
\]
\[
\operatorname{Ext}^0(A(k),\mathbb Q/\mathbb Z))^{1-i}
\]
\[
\boxed{f_*D(G)\simeq(Tf_*G)\unsure{(-1)|(1)}}
\]
\[
=\operatorname{Ext}^{\unsure{i}}(A,\mathbb Q/\mathbb Z)(k)^{1-i}
\]
\[
H^i(K,D(G))\simeq\operatorname{Ext}^i(f_*G,\mathbb Q/\mathbb Z)
\]
\[
\operatorname{Ext}^{\unsure{1+d-i|1+0-i}}(A,\mathbb Q/\mathbb Z)^{\unsure{1+d-i|1+0-i}}
\]
\figure{\begin{tikzpicture}\draw (0,1.5)..controls(.5,2)and(.2,.7)..(.8,0);\end{tikzpicture}}
\[
\boxed{H^i((T\unsure{f_*}G)(-1))=H^{\unsure{i-1}}(T\unsure{f_*}G)
=\underline{\underline{\operatorname{Ext}}}^{\unsure{i-1}}(f_*G,\mathbb Q/\mathbb Z)}
\]
\margin{\figure{\begin{tikzpicture}\draw[line width=1pt] (0,0)..controls(.2,.7)and(.5,.8)..(.7,1);\draw (0,0)..controls(-.2,.4)and(.5,1)..(.4,.5)..controls(.2,.1)and(.1,.9)..(.5,.75);\end{tikzpicture}}}
\[
\boxed{H^i(K,D(G))\deleted{\unsure{f_*G}}
\overset{\uline{\unsure{1}}}{\overset{\sim}{\longrightarrow}}
\underline{\underline{\operatorname{Ext}}}^{\unsure{i-1}}(f_*G,\mathbb Q/\mathbb Z)}
\]
\[
\operatorname{Ext}^{i-1}(M(-1),\mathbb Q/\mathbb Z)
=\operatorname{Ext}^{\unsure{i}}(M,\mathbb Q/\mathbb Z)(1)^{i-1}
\]
\margin{$\operatorname{Ext}^{i-1}(H_{\deleted{\unsure{\mathrm{coh}}}}^{1-i}(f_*G))$}
\margin{$=\operatorname{Ext}^{\unsure{i}}(\unsure{\gamma}$}
\[
\boxed{H^{\unsure{i+1|p+q}}(K,DG)\Longleftarrow
\operatorname{Ext}^{p}(H^{-q}(K,G),\mathbb Q/\mathbb Z)}
\]
\[
0\longrightarrow\operatorname{Ext}^{1}_{k\mathrm{gr}}(H^{1-i}(K,G),\mathbb Q/\mathbb Z)
\longrightarrow H^{i-1}(K,DG)\longrightarrow
\operatorname{Hom}_{k.\mathrm{gr}}(H^{-i}(K,G),\mathbb Q/\mathbb Z)
\]
\mspage{113}
'''
save_page(114,text,[('display','top left','mu n dual'),('display','top middle','Z/pZ'),('display','top right','1'),('display','upper loose','Ext'),('display','upper boxed duality','H i(K,D(Ghat)) ≃ Ext1-i(fstarG,Q/Z)'),('display','upper right below box','A(k)'),('display','middle left unfinished','wavy-underlined Ext i('),('display','middle right','Ext0(A(k),Q/Z))1-i'),('display','middle left boxed','fstarD(G) ≃ (TfstarG)(-1)'),('display','middle right next','= Ext i(A,Q/Z)(k)1-i'),('display','middle left below box','H i(K,D(G)) ≃ Ext i(fstarG,Q/Z)'),('display','middle right lower','Ext1+d-i(A,Q/Z)1+d-i'),('drawing','middle connecting curve','curved line to lower boxed strip'),('display','middle lower boxed strip','H i((TfstarG)(-1)) = H i-1(TfstarG) = double-underlined Ext i-1'),('drawing','left beside lower strip','looped emphasis stroke'),('display','lower boxed map','H i(K,D(G)) isom to Ext i-1'),('deletion','lower boxed map before arrow','fstarG'),('display','lower left shift formula','Ext i-1(M(-1),Q/Z)=Ext i(M,Q/Z)(1)i-1'),('margin note','lower right first unfinished','Ext i-1(H1-i(fstarG))'),('deletion','lower right H subscript','coh'),('margin note','lower right second unfinished','= Ext i(gamma'),('display','bottom boxed spectral sequence','H i+1(K,DG) ⇐ Ext p(H minusq(K,G),Q/Z)'),('display','bottom exact sequence','0→Ext1 kgr(H1-i(K,G),Q/Z)→Hi-1(K,DG)→Hom k.gr(H-i(K,G),Q/Z)'),('text','bottom left page number','113')],observations='Whole and both halves read, with enlarged shift box, isomorphism arrow, spectral-sequence exponent and overwritten right-hand exponents. The page contains incompatible-looking written shifts; they are retained without mathematical correction. The superscript total degree is overwritten and uncertain. Extra closing punctuation and unfinished Ext expressions are retained. Plain, wavy-underlined and double-underlined Ext remain separate.')
