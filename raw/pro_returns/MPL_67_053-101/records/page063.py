import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{63}
% archive foliation: 65
a) Cat. des surfaces conformes à bord $X$,
avec comp. connexe \inserted{compacte} choisie $C$ du bord,
et une structure toroïdale dessus
rectifiable (?) pour la structure
analytique réelle, et

b) Cat. des surfaces conformes à
bord \inserted{$X'$}, avec \deleted{\unsure{le|un}} disque pointé $(D,a)$, $D$
$\subset\operatorname{Int}(X')$ marqué, tel que $\delta D$ soit rectifiable
dans $X'$ (i.e. l'application $\delta D\longrightarrow X'$
rectifiable, pour la structure analytique
naturelle de $\delta D$ comme bord de $D$).

De plus, Pour $(X',a)$ fixé, chaque
disque $D$ autour de $x$ définit un
``disque \deleted{canonique}\inserted{euclidien}'' dans $T_{X',a}$ (au sens de
la structure \inserted{vectorielle} conforme \inserted{(de $T_{X',a}$)}). Comme
\unsure{les|ces} disques forment un torseur sous
$\mathbb R^{*+}$ (par homothéties), \unsure{donc un espace}
de dim $1$, il est clair que l'application
"""
save(63,tex,[('text','top','a) Cat. des surfaces conformes à bord X'),('insertion','line 2','compacte'),('text','upper middle','b) Cat. des surfaces conformes'),('insertion','b line 2','X′'),('deletion','b line 2','le / un'),('text','lower half','De plus Pour (X′,a) fixé'),('deletion','lower half','canonique'),('insertion','lower half','euclidien'),('insertion','lower half','vectorielle'),('insertion','lower half','(de T_{X′,a})'),('text','bottom','Comme les disques forment un torseur')],
 doubts=[('b line 2','le','un; heavily struck through','low'),('last two lines','donc un espace','connected strokes; final espace less distinct','medium')],
 notations=[('Positive multiplicative reals',r'\mathbb R^{*+}','star and plus in that order'),('Tangent line in scan 63',r'T_{X\prime,a}','plain T; compare earlier horizontal stroke')],
 leads=['Proposition retains rectifiable (?) in boundary toroidal structure, then asserts disc boundary rectifiability in the capped surface.','For fixed (X′,a), each disc gives a Euclidean disc in the tangent line; claim that these form a positive-real torsor continues on scan 64.'])
