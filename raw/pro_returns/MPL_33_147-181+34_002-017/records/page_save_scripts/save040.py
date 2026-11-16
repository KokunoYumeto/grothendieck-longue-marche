import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{40}
\mspage{16}
\uline{Lemma} Let $\Phi\subset\mathrm{Fl}(M)$ be left Q-saturated (i.e. $\Phi=\Psi^*$) for some $\Psi$
Then \deleted{$\Phi$ is stable by composition.}

$a)$ $\Phi$ contains iso

$b)$ $\Phi$ stable \deleted{by} \inserted{under} composition and cobase changes

$c)$ $\Phi$ stable \deleted{by direct} \inserted{under} arbitrary amalgamated sums \inserted{(including ``\unsure{infinite}'')}
\deleted{\unsure{ordinals under well ordered}}

$d)$ $\Phi$ stable \deleted{by direct limits, indexed by any well ordered set --- i.e. if we have any direct system}
\inserted{under ordinal direct systems, i.e.}
if we have any well ordered set $I$ and $(A_i)_{i\in I}$ direct system, with $\unsure{\varphi_{ij}|u_{ij}}:A_i\to A_j$ in $\Phi$, and $A_{i_0}=\varinjlim_{j<i_0}A_j$ if $i_0\in I$ is a limit,
then \inserted{$\forall i_0\in I$} $A_{i_0}\xrightarrow{\unsure{\varphi_{i_0}|g_{i_0}}}B=\varinjlim A_i$ is in $\Phi$.
\margin{\uline{NB} $a,b,d\Longrightarrow c)$}

\deleted{The only}
\uline{Then} we get,

\uline{Thm} Let $M$ be a category, stable by small direct limits and (relatively) accessible. Then

\textcircled{1} \deleted{\unsure{a}} Let $\Phi_0^{\deleted{\unsure{*}}}\subset\mathrm{Fl}(M)$ $*$, and $\Phi_0\subset\Phi\subset\overline\Phi_0\stackrel{\mathrm{def}}=\Psi^*$ (with $\Psi=\Phi_{0*}$)
if $\Phi$ \deleted{stable and} satisfies $a)\ b)\ c)\ d)$ $*$, then the $(\Phi,\Psi)$ satisfies factorization condition. (Hence, if $\Phi$ stable by direct factors, $\Phi=\overline\Phi_0$.)
\margin{We have to assume $\Phi_0$ small \deleted{\unsure{(?)}}.}
\margin{We may ignore $c)$ (which results from $a)\ b)\ d)$), \uline{or} assume only $a,b',c,d$, where $b')$ is stability under cobase changes (without assuming stability under composition).}

\textcircled{2} \inserted{(same data $\Phi_0,\Phi$.)} In order that $\Phi\deleted{=\overline\Phi_0}$ \inserted{be saturated}, it is n.s. that $\Phi$ satisfy conditions $a)\ b)\ c)\ d)$ and $e)$ stability by direct factors. In this case, factorization holds for the Q-orthogonal pair $(\Phi,\Psi)$.

NB. In 2, \deleted{besides} there was the preliminary assumption of existence of $\Phi_0\subset\Phi$ s.th. $\Phi_0$ and $\Phi$ have the same left Q-saturation, with $\Phi_0$ \uuline{small}. Next step is to try to get rid of this.
\mspage{39}
'''
e=[('text','top','16'),('text','top','Lemma Let Phi'),('text','upper','Then'),('deletion','upper','Phi is stable by composition'),('text','upper a','Phi contains iso'),('text','upper b','Phi stable composition'),('deletion','upper b','by'),('insertion','upper b','under'),('text','upper c','Phi stable arbitrary amalgamated sums'),('deletion','upper c','by direct'),('insertion','upper c','under'),('insertion','upper c','including infinite'),('deletion','upper c-d','ordinals under well ordered'),('text','upper d','Phi stable'),('deletion','upper d','by direct limits indexed'),('insertion','upper d','under ordinal direct systems'),('text','upper middle','if we have any well ordered set'),('display','upper middle','transition maps Ai Aj'),('display','upper middle','Ai0=lim Aj'),('insertion','upper middle','for all i0 in I'),('display','upper middle','Ai0 to B=lim Ai'),('margin note','left upper','NB a b d implies c'),('deletion','middle','The only'),('text','middle','Then we get'),('text','middle','Thm Let M'),('text','lower 1','Let Phi0'),('deletion','lower 1','a'),('deletion','lower 1','star on Phi0'),('display','lower 1','Phi0 subset Phi subset barPhi0'),('text','lower 1','if Phi satisfies'),('deletion','lower 1','stable and'),('margin note','left lower','We have to assume Phi0 small'),('deletion','left lower','question mark'),('margin note','left lower','We may ignore c'),('text','lower 2','In order that Phi'),('insertion','lower 2','same data Phi0 Phi'),('deletion','lower 2','=barPhi0'),('insertion','lower 2','be saturated'),('text','lower 2','it is n.s.'),('text','bottom','NB In 2'),('deletion','bottom','besides'),('text','bottom left','39')]
record_page(40,s,e,'text',notes='Lemma on closure of left Q-saturated classes; theorem explicitly keeps the small-generating-class hypothesis and ends Next step is to try to get rid of this. Marginal claim: c follows from a,b,d and one may reduce composition to cobase-change stability in bprime. Several revisions of ordinal-limit wording retained.')
build_doubts()
