import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{80}
\mspage{14}
% archive foliation: 82
paire ne change rien; car si on remplace
$D_i'$ par $\lambda D_i'$, donc $D_i''$ par $\frac1\lambda D_i''$, avec $\lambda\in\mathbb R^{*+}$
voisin de 1, ces deux relations vaudront
pour les disques obtenus dans \inserted{le normalisé} $X''$
(c'est probablement tout à fait faux !)
et on obtiendrait la même surface recollée $X$
mais les $\Gamma_i$ remplacés par des cercles
``voisins'' $\Gamma_i'$.

Le cas-clef à comprendre sans
doute est celui où $(g,\nu)=(0,4)$,
i.e. le mécanisme du recollement
de deux ``pantalons'' de Thurston,
donc pour \deleted{\unsure{ces cas}}\inserted{deux} ens. $\varepsilon',\varepsilon''$ à deux
éléments, fixes, les foncteurs des
\[
\left\{\begin{gathered}
\text{pantalons de type combinatoire }\varepsilon'\amalg\{s\},\quad\varepsilon''\amalg\{t\},\\
\text{recollés suivant }\{s,t\},\quad\deleted{\text{donné}}\ \text{suivant}\\
\text{les données }(\ell_i)_{i\in\varepsilon'\amalg\varepsilon''\amalg\unsure{u}}
\in(\mathbb R^{*+})^{\varepsilon'\amalg\varepsilon''\amalg\unsure{u}},\\
\text{et }\theta\in\mathbb U_{\varepsilon'\unsure{\wedge|\times}\varepsilon''}\quad\text{qui fixe le recollement}
\end{gathered}\right.
\]
vers
"""
save(80,tex,[('text','top','paire ne change rien'),('insertion','above X double-prime','le normalisé'),('text','middle','Le cas-clef à comprendre'),('deletion','before ens.','ces cas'),('insertion','above deleted ces cas','deux'),('display','bottom brace','pantalons; recollés; données ell; theta'),('deletion','within brace after s,t','donné'),('text','foot','vers')],doubts=[('line 6','obtiendrait','Ending highly cursive, possibly obtiendrait rather than obtiendront.','medium'),('deletion before ens.','ces cas','Cancellation passes through both short words.','low'),('brace last index in lengths','u','Possibly another letter or a one-element label; no braces supplied in ink.','low'),('subscript of U','epsilon prime wedge epsilon double-prime','The central mark may be times or wedge; subscript kept as written, not inferred.','low')],notations=[('positive real multiplicative group',r'\mathbb R^{*+}','Superscript star then plus.'),('length data',r'(\ell_i)','Slender looped ell.'),('disjoint union',r'\amalg','Handwritten double-cup sign.')],leads=['Explicitly undermines the preceding heuristic: c’est probablement tout à fait faux ! concerning radial scaling of globally realised admissible discs.','Four-holed sphere (0,4) singled out as key case; gluing two Thurston pants with length and angle parameters.'])
