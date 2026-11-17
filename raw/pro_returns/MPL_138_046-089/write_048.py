from workflow import save_page, ROOT, PREFIX
save_page(48,r'''
\scanpage{48}
% archive foliation: 47
% The printed sheet is upside down in the supplied scan; reading order below follows its text upright.
ACADEMIE DE MONTPELLIER

\texttt{----------}

JC/JV

LE RECTEUR DE L'ACADEMIE DE MONTPELLIER

Chancelier des Universités

VU\qquad la loi N° 68-978 du 12 novembre 1968
d'orientation de l'enseignement supérieur
et notamment son article 18

VU\qquad la démission présentée par M. le Profes-\\
seur Jacques ROUZAUD, administrateur
provisoire de l'Université de
MONTPELLIER II

A R R E T E

\texttt{-----------}

\uline{Article premier}.

La démission de M. le Professeur Jacques ROUZAUD
de ses fonctions d'administrateur provisoire de
l'Université de Montpellier II est acceptée à compter
du 26 juin 1978 et l'arrêté rectoral du 15 décembre
1977 est abrogé à la même date.

\uline{Article deux.}

Monsieur Yvan MEYERHOEFFER, Conseiller du Tribunal
Administratif de Montpellier, est chargé des fonctions
d'administrateur provisoire de l'Université de
Montpellier II à compter du 27 juin 1978 et jusqu'à
la date d'installation d'un président élu.

Fait à Montpellier, le 27 Juin 1978

LE RECTEUR,

\unsure{Ricouard}

\uline{Diffusion} : liste D

n° 4027

MONTPELLIER, le 27 Juin 1978
''',[
('text','upright top left','ACADEMIE DE MONTPELLIER; dashed rule'),
('text','upright upper left','JC/JV'),
('text','upright upper right','LE RECTEUR DE L ACADEMIE; Chancelier'),
('text','upright first VU','VU la loi N° 68-978'),
('text','upright second VU','VU la démission présentée'),
('text','upright centre','A R R E T E; dashed rule'),
('text','upright lower first article','Article premier. La démission'),
('text','upright lower second article','Article deux. Monsieur Yvan MEYERHOEFFER'),
('text','upright lower right date line','Fait à Montpellier, le 27 Juin 1978'),
('text','upright lower right','LE RECTEUR,'),
('text','upright signature','Ricouard'),
('text','upright bottom left','Diffusion : liste D; n° 4027; MONTPELLIER, le 27 Juin 1978')],sheet_kind='reused_typed')
p=ROOT/(PREFIX+'_doubts.md')
s=p.read_text().replace('|---|---|---|\n\n# Doubts','''|---|---|---|
| C, subscript n or 2 | `C_n`, `C_2` | Scan 46; the looped later occurrence is marked `\\unsure` for possible script form. |
| Double-stroked Q, Z, D | `\\mathbf{Q}`, `\\mathbf Z`, `\\mathbb D` | 46–47; D is visibly doubled, Q and Z use the same number-field/integer style. |
| Upper/lower case pi | `\\Pi`, `\\pi` | Capital Pi on 46; do not interchange. |
| Star, infinity subscript | `^*`, `_\\infty` | 46–47. |
| Raised mark over Spec | `\\unsure{\\widehat{\\operatorname{Spec}}|\\operatorname{Spec}}` | 47; preserve doubt about the visible accent-like mark. |
| Compressed ramification | `\\unsure{ramfctn|ramification}` | 46–47; contractions not silently expanded. |
| Double quotation marks | two backticks and two apostrophes | Reserved for actual handwritten double quotes, not guillemets. |

# Doubts''')
p.write_text(s)
