import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(43,r"""\scanpage{43}
à déterminer $Z_{\mathrm{aff}}$ en termes de $\varphi$, et écrire ensuite qu'il est 1).
On voit \deleted{que} aisément que $Z_{\mathrm{aff}}$ est un quotient \inserted{$\mathfrak z_1$} de \deleted{\unsure{$\varphi$}} $\mathfrak z$
--- savoir le plus grand quotient de $\mathfrak z$ tel que l'extension
correspondante de $A$ par $\mathfrak z_1$ \deleted{\unsure{y}} soit triviale, et c'est aussi,
$\mathfrak z_1=D(\operatorname{Ker}\varphi)$, donc il faut exprimer $\operatorname{Ker}\varphi=1$.

\deleted{\unsure{On}} Il y a deux cas à distinguer, en décomposant
$\mathfrak z=\underbrace{\mathfrak z_u}_{\mathrm{unipot.}}\times\underbrace{\mathfrak z_m}_{\mathrm{t.\ mult.}}$,
et posant $\Gamma=D(\mathfrak z_m)$

1°) $k$ de car. 0, donc $\mathfrak z_u$ est un groupe vectoriel, \deleted{Alors} $\varphi$
\inserted{soit $\mathfrak z_u=W(t)$ ($t$ tangent à l'origine)}
correspond à deux hom
\[
\varphi_0:\deleted{\unsure{\mathfrak z_u\longrightarrow}}\ t\longrightarrow
 t_{\uline{\operatorname{Pic}}_{A/k}}\simeq H^1(A,\uline O_A)
\]
\[
\varphi_{\deleted{\unsure{m}}1}:\uline\Gamma\longrightarrow\uline{\operatorname{Pic}}_{A/k}
\]
\deleted{Si $t_0=\operatorname{Ker}\unsure{\varphi}$}

Il faut $\varphi_0$ injectif, $\varphi_1$ injectif. (donc la donnée de
$\mathfrak z=\mathfrak z_u\times\mathfrak z_m$ \inserted{et de l'extension $Z$ telle que $Z_{\mathrm{aff}}=1$} équivaut, par dualité, à la donnée d'un \inserted{couple}
\deleted{\unsure{sous espace}} $(\unsure{\Lambda|A},\Gamma)$ d'un \deleted{\unsure{un}} sous-espace vect. de $H^1(A,\uline O_A)=$
$t_{\uline{\operatorname{Pic}}_{A/k}}$ et d'un sous-groupe constant de \deleted{(de t.f.}
\deleted{\unsure{de pt de tors}} à engendrement fini de $\uline{\operatorname{Pic}}_{A/k}$)

2°) $k$ de car. pos. Alors \deleted{\unsure{si}} il est bien connu que
$(Z_{\mathrm{aff}})_u$ \deleted{est} est isogène à $\mathfrak z_u$, ce qui montre que si
$(Z_{\mathrm{aff}})_u=0$, $\mathfrak z_u$ est fini; let --- est plus à l'aise pour
manipuler $D(\mathfrak z_u)$, \deleted{\unsure{Donc on doit avoir}}
\inserted{les groupes alg. comm. finis unipotents}
correspondant par dualité exactement aux groupes alg. comm. \uline{radiciels}.
\deleted{$\varphi_0:D(\mathfrak z_u)$}

Ici la donnée de $\varphi$ équivaut à
\[
\varphi_0:D(\mathfrak z_u)\longrightarrow\uline{\operatorname{Pic}}_{A/k}
\qquad\text{(se factorise par $\uline{\operatorname{Pic}}^0=A^*$}
\]
\[\text{et même par $\widehat{A^*}$)}\]
\[
\varphi_1:\uline\Gamma\longrightarrow\uline{\operatorname{Pic}}_{A/k}
\]
et la condition $Z_{\mathrm{aff}}=1$ équivaut à : $\varphi_0$, $\varphi_1$ injectifs.

(Donc la donnée de $\mathfrak z=\mathfrak z_u\times\mathfrak z_m$, $\mathfrak z_u$ fini, et de l'ext. $Z$ équivaut
à la donnée d'un couple $(\tau,\uline\Gamma)$, d'un sous-groupe alg.
radiciel $\tau$ de $\uline{\operatorname{Pic}}_{A/k}$ et d'un sous-groupe constant libre
$\uline\Gamma$ de $\uline{\operatorname{Pic}}_{A/k}$, pour avoir $D(\mathfrak z)=\tau\times\uline\Gamma\hookrightarrow\uline{\operatorname{Pic}}_{A/k}$
\mspage{42}
""",'text',[('text','top','à déterminer Zaff'),('text','upper','On voit aisément'),('display','upper','z1=D(Ker phi)'),('text','upper-middle','Il y a deux cas'),('display','upper-middle','z=zu times zm'),('text','upper-middle','1° k de car.0'),('marginalia','upper-right insertion','soit zu=W(t)'),('display','middle','phi0 t to tangent Pic'),('display','middle','phi1 Gamma to Pic'),('text','middle cancellation','Si t0=Ker phi'),('text','middle','Il faut phi0 injectif'),('text','middle-lower','2° k de car. pos.'),('text','lower','manipuler D(zu)'),('display','lower','phi0 D(zu) to Pic'),('marginalia','lower-right','se factorise par Pic0'),('display','lower','phi1 Gamma to Pic'),('text','lower','et la condition Zaff=1'),('text','bottom','Donc la donnée de z'),('marginalia','bottom-left','42')],doubts=[('characteristic positive paragraph','let --- est plus à l’aise','Ink appears to begin with let; neither a smooth grammatical replacement nor a mathematical completion has been supplied.','low'),('bottom','tau','Small curved letter transcribed tau; it is repeated consistently on this sheet.','medium')],observations='Central extension Zaff described as Cartier dual of Ker phi. Characteristic zero splits into injective tangent-space and character-lattice maps to Picard; positive characteristic treats finite unipotent kernels, their radicial duals, and embeddings into Picard/formal dual abelian variety. Scope of perfect/algebraically closed base and finite-type/free lattice conditions needs later literature checking.')
