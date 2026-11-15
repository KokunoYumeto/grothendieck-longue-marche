from record_page import save
save(15,226,'reused_typed',r'''
\mspage{225}
\begin{center}-- 6 --\end{center}\hfill n\textsuperscript{o}370

2. \uline{Le théorème d'existence et d'unicité}.

DÉFINITION 2.--- \uline{Soit} $G$ \uline{un groupe localement compact}. \uline{On appelle mesure de Haar à gauche} (resp. \uline{à droite}) \uline{sur} $G$ \uline{une mesure positive non nulle sur} $G$, \uline{invariante à gauche} (resp. \uline{à droite}).

THÉORÈME 1.--- \uline{Sur tout groupe localement compact}, \uline{il existe une mesure de Haar à gauche} (resp. \uline{à droite}), \uline{et}, \uline{à un facteur constant près}, \uline{il n'en existe qu'une}.

A) \uline{Existence} -- Posons $\mathcal K(G)=\mathcal K$, $\mathcal K_+(G)=\mathcal K_+$, $\mathcal K^*_+=\mathcal K_+-\{0\}$. Si $C$ est une partie compacte de $G$, on notera $\mathcal K^*_+(C)$ l'ensemble des $f\in\mathcal K^*_+$ à support dans $C$. Pour $f\in\mathcal K$ et $g\in\mathcal K^*_+$, il existe des nombres $c_1,\ldots,c_n\geq0$ et des éléments $s_1,\ldots,s_n$ de $G$ tels que $f\leq\sum_{i=1}^n c_i\gamma(s_i)g$. (En effet, il existe une partie ouverte non vide $U$ de $G$ telle que $\inf_{s\in U}g(s)>0$, et le support de $f$ peut être recouvert par un nombre fini de translatés à gauche de $U$). Soit alors $(f:g)$ la borne inférieure des nombres $\sum_{i=1}^n c_i$ pour tous les systèmes $(c_1,\ldots,c_n,s_1,\ldots,s_n)$ de nombres $\geq0$ et d'éléments de $G$ tels que $f\leq\sum_{i=1}^n c_i\gamma(s_i)g$. On a :
\[
\begin{array}{lll}
\text{(i)}&(\gamma(s)f:g)=(f:g)&\text{pour }f\in\mathcal K,\ g\in\mathcal K^*_+,\ s\in G\ ;\\
\text{(ii)}&(\lambda f:g)=\lambda(f:g)&\text{pour }f\in\mathcal K,\ g\in\mathcal K^*_+,\ \lambda\geq0\ ;\\
\text{(iii)}&(f+f':g)\leq(f:g)+(f':g)&\text{pour }f,f'\in\mathcal K,\ g\in\mathcal K^*_+\ ;\\
\text{(iv)}&(f:g)\geq(\sup f)/(\sup g)&\text{pour }f\in\mathcal K,\ g\in\mathcal K^*_+\ ;\\
\text{(v)}&(f:h)\leq(f:g)(g:h)&\text{pour }f\in\mathcal K,\ g,h\in\mathcal K^*_+\ ;\\
\text{(vi)}&0<\dfrac1{(f_0:f)}\leq\dfrac{(f:g)}{(f_0:g)}\leq(f:f_0)&\text{pour }f,f_0,g\in\mathcal K^*_+\ ;
\end{array}
\]
(vii) soient $f,f',h\in\mathcal K_+$ avec $h(s)\geq1$ sur le support de $f+f'$, et soit $\varepsilon>0$ ; il existe un voisinage compact $V$ de $e$ tel que, pour toute $g\in\mathcal K^*_+(V)$, on ait $(f:g)+(f':g)\leq(f+f':g)+\varepsilon(h:g)$.

Les propriétés (i), (ii), (iii) sont évidentes. Soient $f\in\mathcal K$, $g\in\mathcal K^*_+$ ;
''',[
('text','sheet edge','225'),('text','typed header','–6–; n°370'),
('text','upper heading','2. Le théorème d’existence et d’unicité'),
('text','upper','DÉFINITION 2'),('text','upper middle','THÉORÈME 1'),
('text','middle','A) Existence – Posons K(G)=K'),
('display','lower middle','(i)–(vi) inequalities for (f:g)'),
('text','lower','(vii) soient f,f′,h'),
('text','bottom','Les propriétés (i), (ii), (iii) sont évidentes')
], 'Upside-down reused typescript read whole and both halves after rotation; each condition and inequality checked.')
