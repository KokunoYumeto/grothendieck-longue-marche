from save_page import save_page

save_page(100, r'''
\scanpage{100}
% archive foliation: 99
\deleted{Il y a un s-groupe d'indice fini\inserted{$I'$} de \deleted{$\pi_1(U)$}\inserted{$I$} qui opère sur $E$ via un pro-$\ell$-groupe. À fortiori,}
\deleted{\diagram{\begin{tikzcd}
I_0(\deleted{\unsure{\bar\xi}}) \arrow[r] \arrow[d] & I'_0 \arrow[d] \\
I(\deleted{\unsure{\bar\xi}}) \arrow[r] & I'
\end{tikzcd}}}

\textcircled{a} Un résultat\inserted{local} de Abhyankar $\oplus$

\textcircled{b} \uline{Version \inserted{semi}globale du \deleted{\unsure{un}} résultat de Abhyankar}.

$X$ schéma loc. \unsure{n.th.} connexe

$\unsure{D}=\sum\unsure{D_i}$ diviseur\inserted{strictement} à croisements normaux

(composantes $Y_i$ \uline{régulières})

On suppose $Z=\bigcap_i\unsure{D_i}\ne\varnothing$, et que \deleted{\unsure{pour tt}}\inserted{le couple $(X,Z)$ est ``hensélien'', i.e. \unsure{pour} $\forall X'$ fini\inserted{sur $X$, conn $\ne\varnothing$}, \deleted{\unsure{l'image inverse} de $Z$ dans $X'$, $\pi_0(\unsure{Z'})\simeq\pi_0(X')$} $Z'$ est connexe $\ne\varnothing$}

\deleted{Alors} Soit \deleted{$\unsure{X}$} $U=X-\deleted{\unsure{supp}}Y$, $\xi$ un pt géom de $U$.

Alors a) $U$ connexe, et $\pi_1(U,\xi)_t\longrightarrow\pi_1(X,\xi)$ surjectif.

b) Pour tout $\unsure{D_i}$, le groupe d'inertie dans $\pi_1(U,\xi)_t$ relatif \unsure{à|:} $\pi_1(U)$ est un sous-groupe distingué \deleted{de $\pi_1(U)\unsure{,\xi}$} commutatif $I_i$ de $Y_i$, \deleted{\unsure{on a}} et on a un épimorphisme canonique
\[
\deleted{\unsure{\xi}}
\prod_{\substack{\ell\ \text{inversible}\\\text{sur }\deleted{Z}\unsure{D_i}\\(\text{ou encore sur }Z)}}T_\ell(\Omega^*)\longrightarrow I_i.
\]

c) Les groupes $I_i$ commutent, et le \deleted{produit}\inserted{groupe engendré} est le noyau\inserted{$I$} de $\pi_1(U,\xi)_t\unsure{-|\longrightarrow}\pi_1(X,\xi)$.

a) Est immédiat.

b) L'image inverse de $\unsure{D_i}$ dans un rec. \deleted{\unsure{fini}}\inserted{connexe} \unsure{normal} modérément ramifié $X'$ de $X$ est normale (étude locale) et \uline{connexe}, \deleted{donc $I_i$ est} \unsure{irred}, donc $I_i$ est invariant. On sait bien qu'il est $\simeq$ quotient de $\prod_\ell T_\ell(\Omega^*)$, $\ell\ne\text{car. gén.}\text{ de }\unsure{D_i}$. Il faut prouver que $I$ est premier aux car. résiduelles en $\unsure{D_i}$. C'est une histoire locale sur $\unsure{D_i}$.

c) Commutation des $I_i$: \deleted{\unsure{Et.}} Étude locale en un pt de
''', [
('deletion','upper, entire diagonal-cancelled paragraph','Il y a un s-groupe d\u0027indice fini'),
('insertion','upper, above fini','I prime'),
('deletion','upper, after de','pi_1(U)'),
('insertion','upper, over deleted pi_1(U)','I'),
('diagram','upper-left, cancelled square','I_0 to I_0 prime; I to I prime'),
('deletion','upper-left, argument of I_0','xi-bar'),
('deletion','upper-left, argument of I','xi-bar'),
('text','below cancelled block, heading a','Un résultat de Abhyankar; circled plus'),
('insertion','above heading a','local'),
('text','below heading a, underlined heading b','Version globale du résultat de Abhyankar'),
('insertion','heading b, before globale','semi'),
('deletion','heading b, after du','un'),
('text','upper-middle, X hypothesis','X schéma loc. n.th. connexe'),
('text','upper-middle, divisor hypothesis','D=sum D_i diviseur à croisements normaux'),
('insertion','above divisor condition','strictement'),
('text','upper-middle, parenthesis','composantes Y_i régulières'),
('text','middle, intersection hypothesis','On suppose Z=intersection D_i neq emptyset'),
('deletion','middle, after et que','pour tt'),
('insertion','middle-right, henselian hypothesis','le couple (X,Z) est hensélien'),
('insertion','middle-right, within henselian definition','sur X conn neq emptyset'),
('deletion','middle-right, abandoned definition','l\u0027image inverse de Z; pi_0(Z prime) simeq pi_0(X prime)'),
('text','middle, U and base point','Soit U=X-Y; xi un pt géom de U'),
('deletion','middle-left, before Soit','Alors'),
('deletion','middle, before U','X'),
('deletion','middle, after X-','supp'),
('text','middle, statement a)','U connexe; pi_1 surjectif'),
('text','lower-middle, statement b)','Pour tout D_i le groupe d\u0027inertie'),
('deletion','lower-middle, before commutatif','de pi_1(U),xi'),
('deletion','lower-middle, after I_i de Y_i','on a'),
('display','lower-middle, canonical epimorphism','product T_ell(Omega^*) to I_i'),
('deletion','before product','xi'),
('deletion','in subscript of product','Z'),
('text','lower, statement c)','Les groupes I_i commutent'),
('deletion','lower-left, after le','produit'),
('insertion','above deleted produit','groupe engendré'),
('insertion','above noyau de','I'),
('text','bottom, proof a)','Est immédiat'),
('text','bottom, proof b)','L\u0027image inverse de D_i'),
('deletion','bottom, after rec.','fini'),
('insertion','bottom, over rec. qualifier','connexe'),
('deletion','bottom, before irred','donc I_i est'),
('text','bottom edge, beginning proof c)','Commutation des I_i; Étude locale en un pt de'),
('deletion','bottom edge before Étude','Et.')
], [
('cancelled square, object arguments','xi-bar','Heavy overstriking prevents identification; best symbol reading','low'),
('X hypothesis','n.th.','noeth.; preserve the shorter visible abbreviation','medium'),
('divisor and component letters','D, D_i; Y_i in parenthesis','D/Y distinction in the overwritten large letters is uncertain','low'),
('henselian insertion','pour; l\u0027image inverse; pi_0(Z prime)','Very small marginal revision at right edge; cancelled phrases overlap','low'),
('U definition deletion','supp','support abbreviated; final stroke uncertain','low'),
('statement b), relatif','à / colon','Two dot-like strokes after relatif','low'),
('statement b), deleted symbols and phrase','de pi_1(U),xi; on a; xi before product','Heavy local cancellation','low'),
('product subscript','D_i, replacing Z','Component letter partly overwritten','medium'),
('statement c), map separator','plain dash','Arrowhead not clearly visible','medium'),
('proof b), qualifiers','fini (deleted); normal; irred','compressed and overwritten words','low'),
('proof b), I','I without subscript','No clearly visible subscript on Il faut prouver que I','medium'),
('proof c), deletion','Et.','Overwritten abbreviation','low')
], [
'Semi-global version of Abhyankar: connected locally noetherian X, strict normal crossing divisor, nonempty common intersection Z, and inserted henselian-pair assumption. Inertia groups are claimed normal, commutative, mutually commuting, and to generate the kernel of the tame-to-unramified fundamental-group map.',
'Proof b) explicitly leaves a task: Il faut prouver que I est premier aux car. résiduelles en D_i. The paragraph says this is local on D_i; proof c) begins at the lower edge and continues elsewhere.',
'Cancelled opening paragraph concerns a finite-index subgroup acting through a pro-ell group; retain as a withdrawn draft rather than as a live assertion.'
])
