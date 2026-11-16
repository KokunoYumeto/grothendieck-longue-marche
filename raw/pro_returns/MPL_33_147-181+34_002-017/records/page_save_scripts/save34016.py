import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{16}
\mspage{14}

3.\unsure{14|15}. Soit $\pi'$ un sous-groupe d'indice fini de $\pi$. Il correspond donc à une extension séparable finie $K'$ de $K$, d'où un normalisé $V'$ de $V$ dans $K'$, qui est un anneau de val. discrète hensélien. Si $k'$ est son corps résiduel, $k'/k$ est une extension finie, donc $\pi'_0\mathrel{\text{---}}\pi'$ \deleted{est} \inserted{induit} un isom de $\pi'_0$ \inserted{$=\operatorname{Gal}(\bar k'/k')$} sur un sous-groupe ouvert de $\pi_0=\operatorname{Gal}(\bar k/k)$. \deleted{D'autre part} \inserted{Il s'impose \unsure{de} vérifier que $\pi'_0\mathrel{\text{---}}\pi'$ est injectif, i.e. que} l'on a \deleted{on voit que}
\[
(3.\unsure{14}.1)\qquad I'=I\cap\pi'
\]
Notons que d'après la théorie générale appliquée à $V'$, on aura pour tt $\ell$ \inserted{nb premier} $\unsure{\ne}p$
\[
(\unsure{3.14.2|2.14.2})\qquad [I'/(I',I')]^{\deleted{\unsure{(\ell)}}(\ell)}\simeq\mathbf Z_\ell(1)
\]
(isom canonique). \deleted{D'autre part,} L'hom $I'_t\mathrel{\text{---}}I_t$ s'identifie, sur $I_t$, à la multiplication par $e$ \inserted{comme dessus}; \deleted{qui} lorsque $k'/k$ est séparable, \deleted{\unsure{p. ex. que}} i.e. l'extension résiduelle de $\widetilde V'/\widetilde V$ \deleted{séparable} \inserted{triviale}, \deleted{\unsure{donc}} p. ex. si $k$ est parfait, alors on peut interpréter $e$ en termes purement ``groupethéorique'' comme
\[
 e=[I:I']=\operatorname{card}I/I'.
\]
\inserted{Sinon, il faut diviser par le facteur inséparable $p^s$ de $k'/k$.}

\deleted{3.\unsure{16}. Il \unsure{reste à examiner}, lorsque \deleted{\unsure{$k'/k$}} \inserted{$I'$} \unsure{est invariant dans} $\pi$ \inserted{dans $I$}, $\unsure{\pi'/K|\pi'/I}$ \unsure{opère sur}}

3.15. Lorsque $\pi'$ est invariant dans $\pi$, \inserted{(i.e. $K'/K$ galoisienne)} il en est de même de \deleted{$\pi'_0$ dans $\pi_0$, puisque (on \unsure{sait} que $k'/k$ est \unsure{purement} galoisienne), donc \unsure{l'hom}} \inserted{$I'=I\cap\pi'$ dans $\pi$ (puisque $I$ est invariant)}, donc \deleted{$\unsure{\pi/\pi'_0}$} \deleted{\unsure{l'hom}} $\pi$ opère sur $I'/(I',I')$ \unsure{,} et par suite sur
\margin{15}
'''
e=[('text','top','3.14|15 Soit π′ un sous-groupe'),('deletion','after residue group map','est'),('insertion','above est','induit'),('insertion','above π′₀','Gal(kbar′/k′)'),('deletion','upper right','D’autre part'),('insertion','upper right to left interlinear','Il s’impose de vérifier'),('deletion','before first display','on voit que'),('display','upper-middle','(3.14.1) I′=I∩π′'),('text','middle','Notons que d’après la théorie générale'),('insertion','above ℓ','nb premier'),('display','middle','(3.14.2) [I′/(I′,I′)]^(ℓ) ≃ Zℓ(1)'),('deletion','exponent of middle display','(ℓ)'),('text','middle-lower','isom canonique; L’hom I′_t—I_t'),('deletion','before L’hom','D’autre part'),('insertion','right after e','comme dessus'),('deletion','after e','qui'),('deletion','after séparable','p.ex. que'),('deletion','residue extension','séparable'),('insertion','above séparable','triviale'),('deletion','after triviale','donc'),('text','lower','p.ex. si k est parfait'),('display','lower','e=[I:I′]=card I/I′'),('insertion','below e formula','Sinon il faut diviser par le facteur inséparable'),('deletion','lower boxed passage','3.16 Il reste à examiner'),('insertion','inside cancelled passage','I′; dans I'),('text','bottom','3.15 Lorsque π′ est invariant'),('insertion','above bottom paragraph','i.e. K′/K galoisienne'),('deletion','bottom','π′₀ dans π₀ puisque...'),('insertion','bottom','I′=I∩π′ dans π'),('deletion','bottom before π opère','π/π′₀; l’hom'),('margin note','bottom left','15')]
save_page(34,16,tex,e,remarks='The first residue-group map visibly reads π′₀—π′ and is repeated in the checking insertion, despite its unexpected form. The equation numbers and the superscript preceding (ℓ) are overwritten. The cancelled 3.16 passage and the cancelled clause about the residue extension at the bottom are low confidence; the latter must not be read as a polished mathematical statement. The author adds a correction dividing by the inseparable residue degree p^s.')
