from save_page import save
save(17,r'''\scanpage{17}
\uline{Suite des recollements}

\[
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
\]

a) Map \deleted{to $Z$} $f:X\longrightarrow Z$

(i) $f_U:U\longrightarrow Z$ simply $f$

(ii) $f_Y:Y\longrightarrow Z$ simply $f$

(iii) hom. of bifunctors
\[
H_X(u,y)\longrightarrow\mathrm{Hom}_Z(fu,fy\unsure{,})
\]

b) Map $f\deleted{\unsure{\sharp}}:X'\longrightarrow X$, defines decomposition
\[
X'=U'\deleted{\unsure{\subset}}\cup Y',\quad\text{with }H_{X'}:U'^\circ\times Y'\longrightarrow(\mathrm{Ens}),\text{ we}
\]
must have

(i) $f_{U'}:U'\longrightarrow U$

(ii) $f_{Y'}:Y'\mathbin{\text{---}}Y$

(iii) bifunctorial $H_{X'}(u',y')\mathbin{\text{---}}H_X(u,y)$

\begin{center}
MR LE PROFESSEUR GROTHENDIECK ALEX.

MATHEMATIQUES \hfill 5
\end{center}

c) Product
\[
T\times U\subset T\times X\supset T\times Y\qquad
H_{T\times X}((t,u),(t',y))\simeq\mathrm{Hom}_T(t,t')\times H_X(u,y)
\]

\hrulefill

d) homotopy $\unsure{\Delta^1|I}\times\unsure{X'|Z'}\xrightarrow{h}X$. \uline{compatible} with decompositions

\[
\text{i.e.}\quad\begin{aligned}
h^{-1}(U)&=\unsure{\Delta^1|I}\times U'\\
h^{-1}(Y)&=\unsure{\Delta^1|I}\times Y'
\end{aligned}
\]
\diagram{\begin{array}{ccc}
U',&Y'&\text{necessarily }\deleted{\unsure{f_i}}\\
\Vert&\Vert&\\
h_i^{-1}(U)&h_i^{-1}(Y),&i\in\{0,1\}
\end{array}}

$h$ given by
\[
\begin{aligned}
h_{U'}&:\unsure{\Delta^1|I}\times U'\mathbin{\text{---}}U\\
h_{Y'}&:\unsure{\Delta^1|I}\times Y'\mathbin{\text{---}}Y
\end{aligned}
\]

plus \unsure{bifunctorial} map in $(s,u')(t,y')$
\[
\mathrm{Hom}(s,t)\times H_{X'}(u',y')\longrightarrow
H_X(\unsure{h_{U'}(s,u')},h_{Y'}(t,y'))
\]
% archive foliation: 16
''','reused_typed',[
('text','top','Suite des recollements'),('display','top','U subset X superset Y; H_X'),('text','upper a','Map f:X→Z; i ii iii'),('deletion','upper a','to Z'),('display','upper a i','f_U:U→Z simply f'),('display','upper a ii','f_Y:Y→Z simply f'),('display','upper a iii','H_X(u,y)→Hom_Z(fu,fy,)'),('text','middle b','Map f X prime→X defines decomposition; we must have'),('deletion','middle b beside f','sharp'),('display','middle b','X prime=U prime cup Y prime with H_X prime'),('deletion','middle b decomposition','subset'),('display','middle b i','f_U prime:U prime→U'),('display','middle b ii','f_Y prime:Y prime dash Y'),('display','middle b iii','bifunctorial H_X prime→H_X'),('text','typed label upside down centre','MR LE PROFESSEUR GROTHENDIECK ALEX.; MATHEMATIQUES; 5'),('text','lower c','Product'),('display','lower c','T×U subset T×X superset T×Y; H product formula'),('text','lower d','homotopy; compatible with decompositions'),('display','lower d first','Delta1×X prime→X'),('display','lower d inverse images','h inverse U and Y'),('diagram','lower d right','U prime Y prime necessarily; h_i inverse images; i in 0,1'),('deletion','lower d right','f_i'),('text','bottom','h given by; plus bifunctorial map'),('display','bottom restrictions','h_U prime; h_Y prime'),('display','bottom last','Hom(s,t)×H_X prime→H_X')],
'The reused typed address label is physically upside down, transcribed in normal reading orientation at its position between b) and c). Its printed 5 is not an author page number. Interval symbols are heavily retraced; Delta^1 is preferred with I alternative. Some connecting strokes have no visible arrowhead and are retained as dashes. The bifunctor labels use H, distinct from the uncertain eta/H inclusion labels in scans 011–014.')
