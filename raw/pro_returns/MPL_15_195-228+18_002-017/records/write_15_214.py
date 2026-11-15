from record_page import save
save(15,214,'reused_typed',r'''
\mspage{213}
1 -- 49 -- \hfill n° 413

Soient $G$ et $H$ deux noyaux de groupe de classe $C^r$. Un \uline{morphisme} $\psi$ de $G$
dans $H$ est une application de classe $C^r$ de $G$ dans $H$ satisfaisant aux conditions
suivantes :

(a) $\psi(e_G)=e_H\qquad \psi(\theta_G(x))=\theta_H(\psi(x))$ pour tout $x\in G$ ;

(b) si $(x,y)\in\Omega(G)$, alors $(\psi(x),\psi(y))\in\Omega(H)$ et on a :
\[
m_H(\psi(x),\psi(y))=\psi(m_G(x,y))
\]
(autrement dit $\psi$ est une représentation pour les lois de composition non partout
définies sur $G$ et $H$). Nous laisserons au lecteur le soin d'étendre au cas des
noyaux de groupe les propositions 3 et 3 bis.

Soit $G$ un noyau de groupe. Il existe un voisinage ouvert $V$ de $e$ tel que les
conditions de (iii) soient réalisées pour $x,y,z\in V$. En particulier le \uline{produit de
convolution} associé à la restriction de $m$ à $V\times V$ définit une loi de composition
sur $T_e^{(r)}(G)$, qui est bilinéaire et associative (bien que non partout définie
si $r<\infty$). Nous désignerons encore par $U(G)$ l'espace $T_e^{(r)}(G)$ muni de cette multiplication.
Nous laisserons au lecteur le soin d'étendre les autres notations et
résultats des n°s 12 à 16. Signalons par exemple que si $f$ est un morphisme de $G$
dans un noyau de groupe $H$, alors $f_*$ est une \uline{représentation} de $U(G)$ dans $U(H)$.

De plus, l'application tangente $m^T$ à $m$ est une application de classe $C^{r-1}$
de $T(\quad)$ dans $T(G)$. On peut identifier $T(\quad)$ à un ouvert de $T(G)\quad T(G)$ et on
vérifie aisément que $T(G)$ muni du point marqué $0_e$, de l'application $m^T$ de $T(\quad)$
dans $T(G)$ et de l'application $\theta^T$ de $T(G)$ dans $T(G)$ est un \uline{noyau de groupe} de
classe $C^{r-1}$ ; la projection canonique est un morphisme de classe $C^{r-1}$ de $T(G)$
sur $G$. Nous laisserons au lecteur le soin d'étendre au cas des noyaux de groupe
les propositions 11 et 12 ainsi que leurs corollaires.
''',[
('text','typed header','1 - 49 -; n° 413'),
('text','typed upper','Soient G et H deux noyaux de groupe de classe C^r'),
('text','typed upper-middle','(a) psi(e_G)=e_H; (b) si (x,y) dans Omega(G)'),
('display','typed upper-middle','m_H(psi(x),psi(y))=psi(m_G(x,y))'),
('text','typed middle','autrement dit psi est une représentation'),
('text','typed middle-lower','Soit G un noyau de groupe; produit de convolution'),
('text','typed bottom','De plus, application tangente m^T; T(blank)'),
('text','manuscript bottom left, inverted relative to typescript','213')], 'Upside-down reused typescript read after rotation. Empty T( ) arguments and missing product sign retained as visible spaces.')
