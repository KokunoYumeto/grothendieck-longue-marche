import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{77}
% archive foliation: 79
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
MDB_{g,\nu} \arrow[rr,dash] \arrow[dr] && M_{\mathrm{st}}ND_{g,\nu} \arrow[dl] \\
& mdt_{g,\nu} &
\end{tikzcd}}
(dans $mdt$, la lettre $t$ rappelle qu'on a inclus
des structures toriques dans le type
combinatoire). Sûrement aussi, si on
\deleted{définit}\inserted{considère} $MD_{g,\nu}$ (sans bord, ou à bord
``généralisé'' réduit à un ens de $\nu$ pts)
et $M_{\mathrm{st}}N\deleted{D}_{g,\nu}$ (sans structure \inserted{multi}disque) on
aura
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
MD_{g,\nu} \arrow[rr] \arrow[dr] && M_{\mathrm{st}}N_{g,\nu} \arrow[dl] \\
& md_{g,\nu} &
\end{tikzcd}}
cette fois un morphisme de \deleted{\unsure{de}}
multiplicités \deleted{\unsure{analyti.}} $\mathbb C$-algébriques.
Dans le cas 1), les dimensions \inserted{(réelles)} de
part et d'autre sont celles de $\mathbb C^{3g-3+\nu}\times\mathbb R^\nu$,
dans le cas 2), \inserted{les dim. complexes sont} celle de $\mathbb C^{3g-3+\nu}$.
"""
save(77,tex,[('diagram','top','MDB g,nu; M st ND g,nu; mdt g,nu'),('text','middle','(dans mdt, la lettre t'),('deletion','middle before MD','définit'),('insertion','above définit','considère'),('deletion','after M st N','D'),('insertion','above disque','multi'),('diagram','lower middle','MD g,nu; M st N g,nu; md g,nu'),('text','bottom','cette fois un morphisme'),('deletion','after de','de'),('deletion','after multiplicités','analyti.'),('insertion','above de part','(réelles)'),('insertion','above dans le cas 2)','les dim. complexes sont')],doubts=[('top diagram horizontal edge','plain stroke','A short downstroke at the end may be an incomplete arrowhead; drawn without a head here.','medium'),('deleted word before C-algébriques','analyti.','Cancellation prevents reliable ending.','low'),('final line','celle','Ink appears singular despite plural dimensions.','medium')],notations=[('type symbols',r'mdt_{g,\nu},\ md_{g,\nu}','Lower-case roman-shaped handwriting; t explicitly explained.')],abbreviations=[('ens','ensemble')],leads=['Asserted algebraicity of MD -> M_st N without boundary/discs, unlike the real analytic bordered map; claimed dimensions are 6g-6+3nu real and 3g-3+nu complex. Need identify fixed combinatorial strata and stability restrictions.'])
