import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(48,r'''
\scanpage{48}
% archive foliation: 47
\uline{Jeux à $N$ joueurs}.

$C$ ensemble des configurations (ou positions)

$J$ ensemble des joueurs $(\operatorname{Card}J=N)$

$j:C\longrightarrow J$ application (pour $\forall$ configuration, il y a un joueur ``dont c'est le tour'' de jouer)

$\sigma:C\longrightarrow\mathcal P(C)$ pour toute configuration $\inserted{x}$, il y a l'ensemble $\sigma(x)$ des configurations ``suivantes''.

$\bigl[$ $\Sigma\subset C\times C$ une relation $[\mathrm{NB}.\quad(x,y)\in\Sigma\Longleftrightarrow y\in\sigma(x)]$

$x_0\in C$ configuration initiale.

$C_0\subset C$ ens des configurations \deleted{\uline{gagnantes}} \uline{terminales}
\[
\text{i.e.}\qquad C_0=\{x\in C\mid\sigma(x)=\varnothing\}.
\]

\deleted{Jeu} \uline{Partie} soit $j_0=j(x_0)$ (joueur initial)

1) $j_0$ ``choisit'' un $x_1\in\sigma(\unsure{x_0|y_0})$. Soit $j_1=j(x_1)$

2) $j_1$ ``choisit'' un $x_2\in\sigma(\unsure{x_1|y_1})$ Soit $j_2=j(x_2)$

\figure{\begin{tikzpicture}\draw (0,0)--(.35,0);\end{tikzpicture}}

$n)$ $j_{n-1}$ ``choisit'' $x_n\in\sigma(\unsure{x_{n-1}|y_{n-1}})$

Partie à $n$ coups :
\[
\deleted{\unsure{(x_0)}}(x_1,\ldots,x_n)\in C^n
\]
\[
x_i\in\sigma(x_{i-1})\qquad 1\leq i\leq n.
\]

\uline{Jeu circulaire}

1) $j$ surjectif (tout joueur est effectif)

2) $\unsure{\exists}\rho:J\longrightarrow J$ telle que
\[
\deleted{\forall x\in C,\ y\in\sigma(x)}
\]
\[
\forall(x,y)\in\Sigma\subset C\times C,\quad\text{on a}\quad j(y)=\rho(j(x)).
\]

\uline{NB} $\rho$ unique si on suppose que $\forall x\in C$, \inserted{\unsure{i.e.}} $\sigma(x)\neq\varnothing$, ou plus gén. que $\forall j\in J$, $\exists x\in C$ tel que $\sigma(x)\neq\varnothing$, $j(x)=j$

3) $\rho$ est une permutation circ.
''',[
('text','heading','Jeux à N joueurs'),
('text','upper','C ensemble des configurations'),
('text','upper','J ensemble des joueurs'),
('text','upper','j:C to J application'),
('text','upper-middle','sigma:C to P(C)'),
('insertion','above configuration','x'),
('display','upper-middle bracket','Sigma subset C x C; NB equivalence'),
('text','middle','x_0 in C configuration initiale'),
('text','middle','C_0 subset C ens des configurations terminales'),
('deletion','before terminales','gagnantes'),
('display','middle','C_0={x in C | sigma(x)=empty}'),
('deletion','before Partie','Jeu'),
('text','middle','Partie soit j_0=j(x_0)'),
('text','middle-lower','1) j_0 choisit un x_1'),
('text','middle-lower','2) j_1 choisit un x_2'),
('drawing','fold','short horizontal stroke'),
('text','below fold','n) j_(n-1) choisit x_n'),
('text','lower','Partie à n coups'),
('deletion','before tuple','(x_0)'),
('display','lower','(x_1,...,x_n) in C^n; x_i in sigma(x_(i-1))'),
('text','lower heading','Jeu circulaire'),
('text','lower','1) j surjectif'),
('text','lower','2) exists rho:J to J telle que'),
('deletion','above relation condition','forall x in C,y in sigma(x)'),
('display','lower','forall(x,y) in Sigma j(y)=rho(j(x))'),
('text','bottom','NB rho unique si on suppose'),
('insertion','above sigma(x) nonempty','i.e.'),
('text','bottom','3) rho est une permutation circ.')
],[
('moves 1, 2 and n','x_0; x_1; x_(n-1)','y-shaped first strokes, altered in place','medium'),
('before n-tuple','deleted (x_0)','multiple overwritten strokes, opening and subscript uncertain','low'),
('condition 2 quantifier','exists','overwritten universal-like sign with small adjacent stroke','medium'),
('NB above sigma(x)','inserted i.e.','short dotted mark; attachment uncertain','low')])
