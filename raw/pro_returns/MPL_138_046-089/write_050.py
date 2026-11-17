from workflow import save_page
save_page(50,r'''
\scanpage{50}
% archive foliation: 49
U N I V E R S I T E

DES SCIENCES ET TECHNIQUES

DU LANGUEDOC

\texttt{------------}

MONTPELLIER, le 8 JUIN 1978

Service de la Scolarité

MR/GJ

Diffusion : Liste H

N°3548

\uline{AVIS DE SOUTENANCE D'UNE THESE DE DOCTORAT D'ETAT}

\uline{Nom et prénom de la candidate} : LINDHEIMER née MONNIER Arlette

\uline{Titre de la thèse} : Contribution à l'étude diffusiométrique des électrolytes dans
des solvants mixtes de constantes diélectriques variables.

\uline{Date, heure et lieu de soutenance prévus} :

1er JUILLET 1978 à 9 Heures 30 mn

Salle de cours n° 2, U.S.T.L.

\uline{Nom du Directeur de thèse} : Monsieur le Professeur B. BRUN

\uline{Désignation du laboratoire où la thèse est préparée} :

Laboratoire des Interactions moléculaires, U.S.T.L.

\uline{Résumé de la thèse} : Les coefficients de diffusion ioniques ont été mesurés à 25°\unsure{c|C}
pour des électrolytes dissous dans des solvants mixtes dont les constantes diélec-\\
triques prenaient des valeurs différentes :

- soit élevées comme dans les mélanges eau-N-méthylpropionamide,

- soit faibles comme dans les mélanges eau-alcool et eau-éther.

Dans le premier cas, la loi étendue relative au coefficient de
diffusion a été vérifiée jusqu'à 0,2M environ ; dans les autres cas la présence
d'associations ioniques a été mise en évidence et les paramètres d'associations ont
été obtenus dans le cadre du modèle des paires d'ions.

\uline{Durée approximative des recherches ayant abouti à la thèse} : 5 ans

\uline{Noms des Rapporteurs} :

\diagram{\begin{tabular}{ll}
SANFELD A. & Professeur, Chimie Physique, Univ. BRUXELLES\\
TURQ P. & Chargé de Cours, Chimie Physique, Univ. PARIS\\
BRUN B. & Professeur, Chimie Physique, U.S.T.L.
\end{tabular}}

\uline{Composition du jury} :

\diagram{\begin{tabular}{ll}
BRUN B. & Professeur, Chimie Physique, Univ. Sciences et Techn. Languedoc\\
& MONTPELLIER\\
& (Président)\\
SANFELD A. & Professeur, Chimie Physique, Univ. BRUXELLES\\
TURQ P. & Chargé de Cours, Chimie Physique, Univ. PARIS\\
& (Membre extérieur choisi en raison de sa compétence scientifique)\\
GROMB S. & Professeur, Chimie Physique, U.S.T.L.\\
GIRAL L. & Professeur, Chimie Organique,U.S.T.L.\\
& (Membre étranger à la spécialité de la candidate)
\end{tabular}}

Le Secrétaire Général,

\figure{\begin{tikzpicture}
\node[rotate=14] at (1.6,.25){\unsure{E S}};
\draw (2.5,.65) .. controls (1.4,.45) and (-.4,-.05) .. (-1.3,-.4)
.. controls (-1.9,-.65) and (1.9,-.1) .. (2.75,.25)
.. controls (3.15,.46) and (2,.36) .. (1.96,.35);
\end{tikzpicture}}

\uline{E. SIAU}

MR LE PROFESSEUR GROTHENDIECK A.

MATHEMATIQUES\qquad 5
''',[
('text','top left heading','UNIVERSITE DES SCIENCES ET TECHNIQUES DU LANGUEDOC'),
('text','top right','MONTPELLIER, le 8 JUIN 1978'),
('text','upper left service block','Service de la Scolarité; MR/GJ; Diffusion : Liste H; N°3548'),
('text','title line','AVIS DE SOUTENANCE D UNE THESE DE DOCTORAT D ETAT'),
('text','candidate field','Nom et prénom de la candidate'),
('text','thesis title field','Titre de la thèse : Contribution'),
('text','date field','Date, heure et lieu; 1er JUILLET 1978'),
('text','director field','Nom du Directeur de thèse'),
('text','laboratory field','Désignation du laboratoire'),
('text','abstract first paragraph and two dashes','Résumé de la thèse : Les coefficients'),
('text','abstract second paragraph','Dans le premier cas'),
('text','duration field','Durée approximative des recherches; 5 ans'),
('text','reporters heading','Noms des Rapporteurs'),
('diagram','reporters table','SANFELD A.; TURQ P.; BRUN B.'),
('text','jury heading','Composition du jury'),
('diagram','jury table','BRUN B.; SANFELD A.; TURQ P.; GROMB S.; GIRAL L.'),
('text','bottom right signature heading','Le Secrétaire Général,'),
('drawing','bottom right signature','E S and flourish'),
('text','bottom right typed name','E. SIAU'),
('text','bottom left address label','MR LE PROFESSEUR GROTHENDIECK A.; MATHEMATIQUES; 5')],sheet_kind='reused_typed')
