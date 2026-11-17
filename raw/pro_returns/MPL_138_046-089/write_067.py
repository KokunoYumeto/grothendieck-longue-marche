from workflow import save_page
save_page(67,r'''
\scanpage{67}
% archive foliation: 66
\diagram{\begin{tabular}{c l}
U N I V E R S I T E & Montpellier, le 28 Juin 1978\\
DES SCIENCES ET TECHNIQUES &\\
DU LANGUEDOC &\\
\texttt{------------}&\\
Service de la Scolarité &\\
MR / GJ &\\
Diffusion : Liste A &\\
N° : 4066 &
\end{tabular}}
\uline{AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT DE 3ème CYCLE}

\uline{( CHIMIE ORGANIQUE PHYSIQUE )}

\uline{Nom et prénom du candidat} :\qquad AURELLY Michèle

\uline{Titre de la thèse} : Application de la corrélation de Hammett à l'étude de l'énolisation des cétones en milieux basique et superbasique.

\uline{Date, heure et lieu de soutenance prévus} :

JEUDI 13 JUILLET 1978 à 16 Heures\\
Salle de cours n° 9 - U. S. T. L.

\uline{Nom du Directeur de thèse} :

Monsieur le Professeur LAMATY.

\uline{Désignation du laboratoire où la thèse est préparée} :

Laboratoire de Chimie Organique Physique.

\uline{Analyse de l'ouvrage} :

Ce travail consiste à cerner de plus près les mécanismes de l'énolisation des cétones par l'étude d'acétophénones et de méthyl-2 phényl-1 butanones-1 substituées, dans des milieux basiques. Les constantes p de Hammett ont été mesurées en fonction de la nature du milieu.

\uline{Durée approximative des recherches ayant abouti à la thèse : 3 ans.}

\uline{Composition du jury proposé} :
\diagram{\begin{tabular}{ll}
MM. : & LAMATY, Président\\
& SCHUE\\
& WYLDE\\
& MION
\end{tabular}}
Le Secrétaire Général,

\unsure{E. Siau}

\uline{E. SIAU}
''',[
('diagram','top letterhead','Université des Sciences et Techniques du Languedoc; date 28 Juin 1978; service, diffusion, N°4066'),
('text','upper third','Avis de soutenance ... Chimie Organique Physique'),
('text','middle','Nom et prénom du candidat: AURELLY Michèle'),
('text','middle','Titre de la thèse: Application de la corrélation de Hammett'),
('text','middle','Date heure lieu; Jeudi 13 Juillet 1978; Salle de cours n°9'),
('text','middle','Directeur de thèse; Monsieur le Professeur LAMATY'),
('text','middle','Désignation du laboratoire; Laboratoire de Chimie Organique Physique'),
('text','lower middle','Analyse de l’ouvrage; Ce travail consiste à cerner'),
('text','lower third','Durée approximative des recherches: 3 ans'),
('diagram','lower third','Composition du jury: LAMATY, SCHUE, WYLDE, MION'),
('text','bottom right','Le Secrétaire Général; signature; E. SIAU')],sheet_kind='reused_typed')
