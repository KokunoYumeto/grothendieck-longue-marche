from record_page import save_page
save_page(120,25,r'''
À prouver

1) Si $X\to Y$ morphisme d'espaces modérés, $\exists$ partie modérée $Y'$ \uline{rare} dans $Y$ et
\[
(Z_i)_{i\in\underbrace{\pi_0(Y\setminus Y')}_{I}}=(U_i)_{i\in I},\quad Z_i\text{ modérés}
\]
\deleted{et des}
(de sorte que les $\unsure{\overline U_i|U_i}$ sont des parties modérées de $Y$) et enfin $\forall i\in I=\pi_0(Y\setminus Y')$, on ait une correspondance modérée
\[
R_i\subset(\overline U_i\times Z_i)\times X
\]
induisant une bijection entre $U_i\times Z_i$ et $X|U_i$ i.e. $X|\deleted{\unsure{(X\times_Y)}}U_i$ est fibré \deleted{\unsure{loc.}} trivial au sens modéré relatif ($U_i$ étant un espace modéré relatif \ldots)

Énoncé analogue pour un diagramme fini d'espaces modérés au dessus de $Y$ ?

Ce diagramme est \unsure{ess\textsuperscript{t}} ``trivial par morceaux'' au dessus d'un $Y\setminus Y'$ convenable, avec $Y'$ modéré rare dans $Y$ ??? Ce serait déjà intéressant dans le cas particulier \unsure{d'un} diagramme de la forme $Z\subset X\subset Y\times[0,1]$ \deleted{$\unsure{I\subset[0,}$} au dessus de $Y$\ldots

\mspage{24}
''',[
('text','top','À prouver'),
('text','upper','1) Si X→Y morphisme d’espaces modérés'),
('display','upper','(Zi)i∈π₀(Y\\Y′)=(Ui)i∈I, Zi modérés'),
('deletion','below upper display','et des'),
('text','upper middle','de sorte que les Ūi'),
('display','middle','Ri⊂(Ūi×Zi)×X'),
('text','middle','induisant une bijection'),
('deletion','middle','(X×Y)'),
('deletion','middle','loc.'),
('text','lower middle','Énoncé analogue pour un diagramme fini'),
('text','lower','Ce diagramme est esst “trivial par morceaux”'),
('deletion','bottom','I⊂[0,'),
('text','bottom left','24')], observations='Explicit heading “À prouver”; a generic triviality statement over the complement of a rare subset is followed by questions for a finite diagram over Y and by a special diagram Z⊂X⊂Y×[0,1]. The manuscript writes one question mark and then three question marks in the later paragraph. These are manuscript questions, not established results.')
