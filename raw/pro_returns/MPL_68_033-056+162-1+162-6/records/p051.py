import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(51,r'''
\scanpage{51}
% archive foliation: 50
XVIII\qquad L e s\quad é p o u s a i l l e s\qquad (2)

J'ai scruté et j'ai fouillé - par pleines brassées je ramasse tout à l'entour les paires enlacées disant un même message. Pêle-mêle je les jette devant moi ...

Puis, comme un enfant appliqué intensément enfile collier de pierres multicolores qu'il \unsure{assem\deleted{t}ble} à son gré - sans en laisser une seule, car toutes lui semblent belles ! ... lestement passant les unes, et sur d'autres s'arrêtant longement pour les contempler à loisir ... ainsi du chaos chatoyant de mes trouvailles je prépare ce collier - m o n collier - pour te l'offrir ... et \deleted{pour} l'oublier ...

Le jeu était p l a i s i r - il était découverte ! Qu'importe s'il reste \deleted{\unsure{cela|trace}} \inserted{trace} pour témoigner du jeu \inserted{révolu} d'un enfant qui découvre \unsure{!} Quel sens a un collier, si ce n'est le plaisir de le faire ...

Ou ... susciter en \uline{toi} d é s i r de scruter et fouiller - de ramasser toi-même perles et pierres par poignées ... contempler longuement une à une celles qui t e parlent, et au gré de \deleted{ta} \inserted{\uline{ton} « \unsure{désir} »} \deleted{fantaisie} assembler t o n collier ?

\deleted{A quoi bon un collier qui ne suscite désir d'en faire un plus beau ?}

Je termine d'un deuxième rang de paires enlacées ... \unsure{Si} le jeu \unsure{te} plait encore, \deleted{tu peux} regarde\deleted{r} faire ... ou \deleted{tu peux} fai\deleted{re}\inserted{s} \inserted{en un plus beau.}

11. En les choses de la Création s'enlacent et s'unissent :

\begin{flushleft}
l u m i è r e\quad et\quad o m b r e\\
le clair et l'obscur\\
le jour et la nuit\\
le brillant et le terne

savoir et mystère\\
le connu et l'inconnu\\
le connaissable et l'inconnaissable\\
connaissance et ignorance

le précis et le vague\\
le particulier et le général
\end{flushleft}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (0,0) {le défini et l'indéfini};
\node[anchor=west] at (0,-.55) {l'exprimé et l'inexprimé};
\node[anchor=west] at (0,-1.3) {l'achevé et l'inachevé};
\node[anchor=west] at (0,-1.62) {le formé et l'informe};
\node[anchor=west] at (0,-1.92) {simplicité et complexité};
\node[anchor=west] at (0,-2.25) {\unsure{ordre et chaos}};
\draw (5.1,.6)--(4.6,-.6)--(3.9,-2.35);
\node[anchor=west] at (5,0) {nécessité et hasard};
\node[anchor=west] at (5,-.55) {veille et sommeil};
\node[anchor=north west,align=left] at (5,-1.15) {ce qui naît - et ce qui l'en-\\\hspace{4cm}fante};
\node[anchor=north west,align=left] at (5,-1.75) {ce qui meurt - et ce qui l'\\\hspace{3cm}\unsure{accueille}};
\end{tikzpicture}}
''',[
('text','typed heading','XVIII Les épousailles (2)'),
('text','first paragraph','Jai scruté et jai fouillé'),
('text','second paragraph','Puis comme un enfant appliqué'),
('deletion','inside assemble','t'),
('deletion','before loublier','pour'),
('text','third paragraph','Le jeu était plaisir'),
('deletion','after sil reste','cela / trace'),
('insertion','after sil reste','trace'),
('insertion','above du jeu','révolu'),
('text','fourth paragraph','Ou susciter en toi désir'),
('deletion','after au gré de','ta'),
('insertion','after cancelled ta','ton « désir »'),
('deletion','before assembler','fantaisie'),
('deletion','at fold whole line','A quoi bon un collier qui ne suscite désir den faire un plus beau?'),
('text','below fold','Je termine dun deuxième rang de paires enlacées'),
('deletion','before regarder','tu peux'),
('deletion','regarder ending','r'),
('deletion','after ou','tu peux'),
('deletion','faire ending','re'),
('insertion','faire ending','s'),
('insertion','right edge','en un plus beau.'),
('text','lower heading','11. En les choses de la Création'),
('text','lower first list','lumière et ombre; le clair et lobscur; le jour et la nuit; le brillant et le terne'),
('text','lower second list','savoir et mystère; le connu et linconnu; le connaissable et linconnaissable; connaissance et ignorance'),
('text','lower third list','le précis et le vague; le particulier et le général'),
('text','bottom left','le défini et lindéfini through ordre et chaos'),
('drawing','bottom between columns','slanting divider'),
('text','bottom right','nécessité et hasard; veille et sommeil; ce qui naît; ce qui meurt')
],[
('second paragraph assemble','assem deleted t ble','overtyped/deleted narrow character before b','medium'),
('third paragraph after sil reste','deleted cela; inserted trace','underlying word may be trace; thick writing obscures typescript','low'),
('after qui découvre','!','overwritten punctuation, perhaps ?','medium'),
('fourth paragraph handwritten replacement','ton « désir »','last letter of désir strongly overworked; guillemets visible','medium'),
('paragraph Je termine','Si; te','initial S and t handwritten over typed characters','medium'),
('bottom cut edge','ordre et chaos; accueille','lower parts clipped by scan edge','medium')],sheet_kind='reused_typed')
