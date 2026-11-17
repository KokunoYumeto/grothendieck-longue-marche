import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{48}

Cela nous ramène au cas où $G$ est soit complet, soit \uline{linéaire}. Dans le \deleted{premier} \inserted{deuxième} cas, \deleted{\unsure{introduisons} pour tout entier $n$} $G=G_u\times G_s$ (décomposition en partie semi-simple et unipotente) et cette décomposition est \uline{définie sur $k$}.
\margin{à vérifier}
Donc on peut supposer que $G$ est soit unipotent, soit \deleted{semi-simple} formé d'éléments semi-simples, soit complet.
Dans les deux derniers cas, soit $U$ l'ens. des éléments d'ordre fini de $G=G^{\bar k}$ ; alors le groupe $G^{\deleted{\unsure{\bar k}}}/U$ est un groupe sans torsion, de plus il est divisible ; pour le voir, on note que $G_0$ (comp. connexe de $0$) est divisible (c'est un th. de Weil pour une variété abélienne, et \deleted{\unsure{bien sûr}} trivial pour le cas où $G\simeq\bar k^{*n}$) et \deleted{\unsure{on}} par suite $G\simeq G_0+G/G_0$, \deleted{\unsure{et}} (abstraction faite des opérations de $\unsure{\mathfrak g_k}$) d'où résulte que $U$ contient le facteur $G/G_0$ et que $G/U$ s'identifie au quotient de $G_0$ par $U\cap G_0$, donc est divisible aussi].
\margin{Lemme :\par \unsure{dire qqp}\par cf plus bas\par ici le fait de passer à la limite inductive est essentiel}
\figure{\begin{tikzpicture}\draw (0,0)--(0,-.9);\end{tikzpicture}}
Donc \deleted{$\unsure{H}$}
\[
\underline H^i(\unsure{\mathfrak g},G/U)=0,\qquad\inserted{\text{pour }i>0}
\]
\deleted{tandis que} d'où
\[
\underline H^i(\unsure{\mathfrak g},G)\simeq H^i(\unsure{\mathfrak g},U)\qquad\text{pour }i\geq1
\]
(compte tenu que $G\longrightarrow G/U$ est une \unsure{surjection})
\margin{\unsure{dégager} un \uline{lemme} [lorsque $G$ n'a pas de sous-groupe linéaire connexe unipotent non nul]}

Or, pour \deleted{$\unsure{\forall}$} $\unsure{m|n}$, soit $U(\unsure{m|n})$ le sous-groupe de $U$ formé des éléments annulés par $\unsure{m|n}$. On a
\[
H^i(\unsure{\mathfrak g},U)=\varinjlim_{\unsure{m|n}}H^i(\unsure{\mathfrak g},U(\unsure{m|n}))
\]

\mspage{47}'''
elements=[('text','top','Cela nous ramène au cas où G'),('deletion','top line 2','premier'),('insertion','above premier','deuxième'),('deletion','top lines 2–3','introduisons pour tout entier n'),('display','within top paragraph','G=Gu × Gs'),('text','upper','décomposition en partie semi-simple et unipotente'),('margin note','left upper','à vérifier'),('text','upper middle','Donc on peut supposer'),('deletion','upper middle','semi-simple'),('text','middle','Dans les deux derniers cas'),('deletion','superscript on G/U','bar k'),('text','middle','pour le voir, on note que G0'),('deletion','middle','bien sûr'),('display','within paragraph','G ≃ bar k^(star n)'),('deletion','middle','on'),('display','within paragraph','G ≃ G0 + G/G0'),('deletion','before abstraction','et'),('text','lower middle','abstraction faite des opérations'),('text','lower middle','d’où résulte que U contient'),('margin note','left middle','Lemme : dire qqp cf plus bas'),('drawing','left middle','vertical marginal stroke'),('text','lower','Donc'),('deletion','before H formula','H'),('display','lower','underline Hi(g,G/U)=0'),('insertion','above display','pour i>0'),('deletion','after display','tandis que'),('text','lower','d’où'),('display','lower','underline Hi(g,G) ≃ Hi(g,U), i≥1'),('text','lower','compte tenu que G → G/U'),('margin note','left lower','dégager un lemme [lorsque G n’a pas'),('text','foot','Or, pour m, soit U(m)'),('deletion','foot after pour','∀'),('display','bottom','Hi(g,U)=lim_m Hi(g,U(m))'),('text','bottom left','47')]
save(48,text,elements,observations='Whole and halves read; enlarged all main text and both rotated margins. The initial G=G^{bar k}, the deleted superscript, the plus sign G0+G/G0 and the final unmatched square bracket are retained. The index in the last paragraph is visually ambiguous m/n and is marked at each occurrence. The short instruction beneath Lemme in the left margin is especially uncertain. Fraktur g readings reflect the repeated tall looped sign; no Galois identification has been inserted into the transcription.')
