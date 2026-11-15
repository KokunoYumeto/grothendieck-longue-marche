from record_page import save
save(18,15,'text',r'''
\uline{Comparaison de classes fondamentales} analytiques (= alg) et topologiques (= transc.).

$X$ variété \deleted{analytique} holomorphe

$Y$ sous-variété holomorphe de codim $p$ partout.

$\underline\Omega_X^\bullet$ résolution de $C$

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\underline H_Y^{2p}(X,Z)\arrow[r,"\substack{\mathrm{can}\\i}"]&\underline H_Y^{2p}(X,Z)\otimes_Z C\arrow[r,"\substack{\mathrm{can}\\\sim}"]&\underline H_Y^{2p}(X,C)\arrow[r,"\substack{\text{De Rham (i.e. can)}\\\sim}"]&\underline{\underline H}_Y^{2p}(X,\underline\Omega_X^\bullet)&\\
Z_{Y\deleted{\unsure{X}}}\arrow[u,"\substack{\wr\ P_{\mathrm{top}}^Z\\\text{Poincaré}\\\text{topologique}\\\text{local}}"]\arrow[r,hook]&\substack{\deleted{\unsure{P_{\mathrm{top}}^C}}\\C_Y}\arrow[r,equal]&C_Y\arrow[u,"\wr\ P_{\mathrm{top}}^C"]\arrow[r,"\frac{1}{(2i\pi)^p}"']&C_Y\arrow[u,"\wr\ P_{\mathrm{an}}^{\unsure{C}}"]\arrow[ur]&\underline H_Y^p(X,\underline\Omega_X^p)\arrow[ul,"\unsure{\text{suite spectrale}}"']\\
&&\deleted{\unsure{\underline H_Y^{2p}(X,\underline\Omega_X^\bullet)}}\arrow[u,phantom,"\deleted{\unsure{\updownarrow\ \wr}}"]\arrow[r,phantom,"\deleted{\longrightarrow}"]&&
\end{tikzcd}}
\margin{\uuline{résidu}}
\margin{\uline{Poincaré} \uline{analytique} \uline{local} [défini par voie \unsure{ess.} alg.] si $f_1\cdots f_p$ est un syst. d'équations locales de $Y$, on prend la section
$\dfrac{df_1}{f_1}\wedge\cdots\wedge\dfrac{df_p}{f_p}$ de $\underline H_Y^p(\underline\Omega_X^p)$)}

On est ramené au cas où $Y$ est réduit à un pt $a$ (prendre une \deleted{section} $X'^{n-p}$ transversale à $Y$ en un pt) et par cup-produit au cas où $X$ est de dim $1$, \unsure{sinon} un disque de $C\unsure{\simeq X}$
[NB. à priori, \unsure{c'est acquis pourvu} \unsure{déjà} qu'il le\inserted{existe un} multiplicateur de la forme $\lambda^p$, $\lambda\in C^*$ étant indépendant de $X,Y,p$]. Alors on a
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
H^1(X-a,Z)\arrow[r]\arrow[d,phantom,"\wr"]&H^1(X-a,C)\arrow[r,"\sim"]\arrow[d,phantom,"\wr"]&\underline H^1(X-a,\underline\Omega_X^\bullet)\arrow[d,phantom,"\wr"]&\\
H_a^2(X,Z)\arrow[r]&H_a^2(X,C)\arrow[r,"\sim"]&\underline{\underline H}_a^2(X,\underline\Omega_X^\bullet)&\underline H_a^1(X,\underline\Omega_X^1)\quad\frac{dz}{z}\arrow[l,"\sim"]\\
Z\arrow[u,"P_t^Z"]\arrow[r]&C\arrow[u,"P_t^C"]\arrow[r,"\lambda"]&C\arrow[u,"P_{\mathrm{an}}^C"]\arrow[ur]&
\end{tikzcd}}
\figure{\begin{tikzpicture}[scale=.55]\draw (0,0) circle (0.55);\fill (0,0) circle (0.045);\end{tikzpicture}}
\mspage{14}
''',[
('text','top heading','Comparaison de classes fondamentales analytiques (=alg) et topologiques (=transc.)'),
('text','upper','X variété holomorphe; Y sous-variété holomorphe'),
('display','upper middle','Omega dot_X résolution de C'),
('diagram','upper middle full width','H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p'),
('text','middle','On est ramené au cas où Y est réduit à un pt a'),
('text','lower','NB. à priori; multiplicateur de la forme lambda^p'),
('diagram','bottom','H^1(X-a,Z) to H_a^2(X,Z); Z to C to C; dz/z'),
('drawing','bottom left','circle with central filled point')
], 'Whole and both halves inspected, with enlarged diagram, marginal and prose regions. The underlined H and double-underlined H are differentiated; the crossed-out old diagram node and arrow are retained. The reduction paragraph and beginning of NB are faint and explicitly uncertain. The exponent n-p is copied as written, without correcting the transverse-dimension claim.')
