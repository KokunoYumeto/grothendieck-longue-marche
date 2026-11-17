import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(53,r'''
\scanpage{53}
% archive foliation: 52
\mspage{82}
XVIII\qquad L e s\quad é p o u s a i l l e s\qquad (2)

J'ai scruté et j'ai fouillé - par pleines brassées je ramasse tout à l'entour les paires enlacées disant un même message. Pêle-mêle je les jette devant moi ...

Puis, comme un enfant appliqué intensément enfile collier de pierres multicolores qu'il assemble à son gré - sans en laisser une seule, car toutes lui semblent belles ! ... lestement passant les unes, et sur d'autres s'arrêtant longement pour les contempler à loisir ... ainsi du chaos chatoyant de mes trouvailles je prépare ce collier - m o n collier - pour te l'offrir ... et \deleted{pour} l'oublier ...

Le jeu était p l a i s i r - il était découverte ! Qu'importe s'il reste \deleted{collier}\inserted{trace} pour témoigner du jeu \inserted{révolu} d'un enfant qui découvre \unsure{!} Quel sens a un collier, si ce n'est le plaisir de le faire ...

Ou ... susciter en \uline{toi} \unsure{désir}\deleted{\unsure{i r}} de scruter et fouiller - de ramasser toi-même perles et pierres par poignées ... contempler longuement une à une celles qui t e parlent, et au gré de \deleted{ta} \inserted{\uline{ton} « \deleted{\unsure{désir}}\inserted{désir} \unsure{»}} \deleted{fantaisie} assembler t o n collier ?

\margin{\figure{\begin{tikzpicture}\draw (.05,1.2) .. controls (.13,.8) and (-.07,.35) .. (0,.1) --(.38,0);\end{tikzpicture}}}

\deleted{A quoi bon un collier qui ne suscite désir d'en faire un plus beau ?}

\margin{\figure{\begin{tikzpicture}\draw (.38,1)--(0,1)--(0,0);\end{tikzpicture}}}
Je termine d'un deuxième rang de paires enlacées \unsure{...} \unsure{Si} le jeu \unsure{te} plait encore, \deleted{tu peux} regarde\deleted{r} faire - ou \deleted{tu peux} fai\deleted{re}\inserted{s-en \deleted{\illegible{2}}\inserted{un plus beau !}}

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
\draw (5.1,.6)--(4.65,-.6)--(4.05,-2.35);
\node[anchor=west] at (5,0) {nécessité et hasard};
\node[anchor=west] at (5,-.55) {veille et sommeil};
\node[anchor=north west,align=left] at (5,-1.15) {ce qui naît - et ce qui l'en\\\hspace{4cm}fante};
\node[anchor=north west,align=left] at (5,-1.75) {ce qui meurt - et ce qui l'\\\hspace{3cm}accueille};
\end{tikzpicture}}
''',[
('text','top handwritten number','82'),
('text','typed heading','XVIII Les épousailles (2)'),
('text','first paragraph','Jai scruté et jai fouillé'),
('text','second paragraph','Puis comme un enfant appliqué'),
('deletion','before loublier','pour'),
('text','third paragraph','Le jeu était plaisir'),
('deletion','after sil reste','collier'),
('insertion','over collier','trace'),
('insertion','above du jeu','révolu'),
('text','fourth paragraph','Ou susciter en toi désir'),
('deletion','after compressed désir','i r'),
('deletion','after au gré de','ta'),
('insertion','after cancelled ta','ton « désir »'),
('deletion','beneath handwritten désir','désir'),
('insertion','above cancelled désir','désir'),
('deletion','before assembler','fantaisie'),
('margin note','left of last two lines of fourth paragraph','curved bracket'),
('drawing','left of fourth paragraph','curved bracket'),
('deletion','at fold whole line','A quoi bon un collier qui ne suscite désir den faire un plus beau?'),
('margin note','left of Je termine','square bracket'),
('drawing','left of Je termine','square bracket'),
('text','below fold','Je termine dun deuxième rang de paires enlacées'),
('deletion','before regarder','tu peux'),
('deletion','regarder ending','r'),
('deletion','after ou','tu peux'),
('deletion','faire ending','re'),
('insertion','faire ending and right margin','s-en un plus beau!'),
('deletion','beneath un plus beau','two heavily crossed handwritten words'),
('insertion','above last cancellation','un plus beau!'),
('text','lower heading','11. En les choses de la Création'),
('text','lower first list','lumière et ombre; le clair et lobscur; le jour et la nuit; le brillant et le terne'),
('text','lower second list','savoir et mystère; le connu et linconnu; le connaissable et linconnaissable; connaissance et ignorance'),
('text','lower third list','le précis et le vague; le particulier et le général'),
('text','bottom left','le défini et lindéfini through ordre et chaos'),
('drawing','bottom between columns','slanting divider'),
('text','bottom right','nécessité et hasard; veille et sommeil; ce qui naît; ce qui meurt')
],[
('after qui découvre','!','overwritten punctuation, possibly ?','medium'),
('after en toi','désir with cancelled i r','word respaced by writing over and cancelling typed letters; exact layer division uncertain','low'),
('au gré de handwritten replacement','ton « deleted désir inserted désir »','old désir and closing guillemet obscured by repeated revision','low'),
('Je termine revised punctuation and characters','...; Si; te','typed points and initial letters overwritten','medium'),
('after fais-en','illegible 2 beneath inserted un plus beau!','autant, toi, un plus considered; no defensible full reading under thick crosshatching','low'),
('bottom edge','ordre et chaos','lower portions clipped but word tops visible','medium')],sheet_kind='reused_typed')
