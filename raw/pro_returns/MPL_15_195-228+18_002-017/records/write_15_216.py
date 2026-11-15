from record_page import save
save(15,216,'reused_typed',r'''
\mspage{215}
1 -- 48 -- \hfill n° 413

17. \uline{Noyaux de groupe}.

DÉFINITION 5.-- \uline{On appelle noyau de classe} $C^r$ \uline{une variété} $V$ \uline{de classe} $C^r$ \uline{munie
d'un point marqué} $e$. \uline{Un noyau de groupe de classe} $C^r$ \uline{est un noyau} $G$ \uline{muni d'une
application} $\theta_G$ \uline{de classe} $C^r$ \uline{de} $G$ \uline{dans} $G$ \uline{et d'une application} $m_G$ \uline{de classe} $C^r$
\uline{d'un ouvert} $\Omega(G)$ \uline{de} $G\times G$ \uline{dans} $G$ \uline{satisfaisant aux conditions suivantes} :

(i) $\Omega$ \uline{contient les points} $(x,\theta(x))$ \uline{et} $(\theta(x),x)$ \uline{et on a}
\[
\tag{36} m(x,\theta(x))=m(\theta(x),x)=e
\]
\uline{pour tout} $x\in G$ ;

(ii) $\Omega$ \uline{contient les points} $(e,x)$ \uline{et} $(x,e)$ \uline{et on a}
\[
\tag{37} m(e,x)=m(x,e)=x
\]
\uline{pour tout} $x\in G$ ;

(iii) \uline{si} $x,y,z$ \uline{sont trois éléments de} $G$ \uline{tels que} $(x,y)$, $(y,z)$, $(m(x,y),z)$
\uline{et} $m(x,m(y,z))$ \uline{appartiennent à} $\Omega$, \uline{on a} :
\[
\tag{38} m(m(x,y),z)=m(x,m(y,z)).
\]
On a $e=m(e,\theta(e))=\theta(e)$ et
\[
\begin{aligned}
x&=m(e,x)=m(m(\theta(\theta(x)),\theta(x)),x)=\\
&=m(\theta(\theta(x)),m(\theta(x),x)=m(\theta(\theta(x)),e)=\theta(\theta(x)).
\end{aligned}
\]

\uline{Exemple} 1.-- Une variété de groupe est un noyau de groupe.

\uline{Exemple} 2.-- Soient $X$ une variété, $e\in X$ et $m$ une application d'un ouvert $\Omega$ de $X\times X$
dans $X$ satisfaisant aux conditions (ii) et (iii) de la définition 5. Le lemme 1
du n° 3 montre qu'il existe un voisinage ouvert $G$ de $e$ dans $X$ et un automorphisme $\theta$
de $G$ sur lui-même satisfaisant à (i). Il suffit alors de prendre pour $\Omega(G)$
l'ensemble des $(x,y)\in(G\times G)\cap\Omega$ tels que $m(x,y)\in G$ et pour $m_G$ la restriction de $m$
à $\Omega(G)$ pour obtenir sur $G$ une structure de noyau de groupe.
''',[
('text','typed header','1 - 48 -; n° 413'),
('text','typed upper','17. Noyaux de groupe; DÉFINITION 5'),
('text','typed middle','(i) Omega contient les points'),
('display','typed middle','(36) m(x,theta(x))=m(theta(x),x)=e'),
('text','typed middle','(ii) Omega contient les points'),
('display','typed middle','(37) m(e,x)=m(x,e)=x'),
('text','typed middle-lower','(iii) si x,y,z sont trois éléments de G'),
('display','typed middle-lower','(38) m(m(x,y),z)=m(x,m(y,z))'),
('display','typed lower','On a e=m(e,theta(e)) and chain proving theta(theta(x))=x'),
('text','typed lower','Exemple 1. Une variété de groupe'),
('text','typed bottom','Exemple 2. Soient X une variété'),
('text','manuscript bottom left','215')], 'Typescript formula m(x,m(y,z)) in condition (iii), and apparent missing parenthesis in subsequent calculation, retained literally.')
