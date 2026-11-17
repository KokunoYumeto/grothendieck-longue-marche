import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(217,r'''\scanpage{217}
\diagram{\begin{tikzcd}[row sep=large]
\alpha=\sigma_{BC'}=\frac12\bigl((\uline{a'+a})\unsure{-|+}(b'-b)+(c'-c)\bigr)\ \bullet\arrow[dd,bend left=55]\\
\beta=\sigma_{AB'}=\frac12\bigl(-(a'\unsure{-|+}a)+(b'-b)+(\uline{c'+c})\bigr)\arrow[u,bend right=30]\\
\gamma=\sigma_{CA'}=\frac12\bigl((a'-a)+(\uline{b'+b})-(c'-c)\bigr)\arrow[u,bend right=30]
\end{tikzcd}}
\diagram{\begin{tikzcd}[row sep=large]
\alpha'=\sigma_{AC'}=\frac12\bigl(-(a'-a)+(\uline{b+b^{\unsure{'|3}}})+(c'-c)\bigr)\arrow[dd,bend left=55]\\
\beta'=\sigma_{CB'}=\frac12\bigl((a'+a)+(b'-b)-(\unsure{c}c'-c)\bigr)\ \bullet\arrow[u,bend right=30]\\
\gamma'=\sigma_{BA'}=\frac12\bigl((a'-a)\unsure{-|+}(b'-b)+(c'+c)\bigr)\arrow[u,bend right=30]
\end{tikzcd}}
\margin{\[
\begin{gathered}-c'+c+2c'\\-b'+b\\-a'+a\\c'-c\end{gathered}\]}
\unsure{Sommes} des $\sigma_a$ sur les arêtes d'une face
\[\begin{aligned}
\varphi_a&=\deleted{\unsure{b+c+}}(a'-a)+2(b+c)\\
\varphi_b&=(b'-b)+2(a+c)\\
\varphi_c&=(c'-c)+2(a+b)
\end{aligned}\]
\figure{\begin{tikzpicture}\draw[->] (0,0)--(0,-3.5);\end{tikzpicture}}
\[a-a'+(b'+c')\]
\[\begin{aligned}
\varphi_{a'}&=(b'+c')\unsure{-|=}(a'-a)+b'+c'=2(b'+c')-(a'-a)\\
\varphi_{b'}&=a'+c'+a'-(b'-b)+c'=2(c'+a')-(b'-b)\\
\varphi_{c'}&=(a'+b')+a'+b'-(c'-c)=2(a'\unsure{+|-}b')-(c'-c)
\end{aligned}\]
\diagram{\begin{tikzcd}[column sep=large]
2\arrow[d,phantom] &2&2\\
&\deleted{\text{\unsure{les signes sont partout !}}}\arrow[ul,bend left=35]\arrow[u,bend left=15]\arrow[ur,bend right=20]&
\end{tikzcd}}
\margin{216}
''',[
('diagram','upper left','alpha,beta,gamma equations with cyclic arrows'),('diagram','middle left','alpha prime,beta prime,gamma prime equations with cyclic arrows'),('margin note','upper right','-c prime+c+2c prime;-b prime+b;-a prime+a;c prime-c'),('text','lower left','Sommes des sigma_a sur les aretes d une face'),('display','lower left','phi_a,phi_b,phi_c'),('deletion','phi_a prefix','b+c+'),('drawing','lower middle','vertical line ending down arrow'),('display','above lower-right equations','a-a prime+(b prime+c prime)'),('display','lower right','phi_a prime,phi_b prime,phi_c prime'),('diagram','bottom right','cancelled note with three upward arrows to coefficients2'),('deletion','bottom right','les signes sont partout !'),('margin note','lower left','216')],
[('alpha and gamma prime formulas','minus before b prime-b','operation blackened, alternative plus','medium'),('beta formula','-(a prime-a)','inner operation blackened','medium'),('alpha prime formula','b+b prime','second superscript resembles3','medium'),('beta prime formula','extra c before c prime-c','visible opening stroke could be duplicated parenthesis','low'),('bottom caption','Sommes','letters compressed','medium'),('bottom cancelled note','les signes sont partout !','large cancellation leaves only parts of words, proposed reading very uncertain','low')],
['Six off-axis edge coefficients expressed as half-sums and differences of six chosen values. Face-sum formulas follow; cancelled bottom note with arrows warrants checking coefficient2 arithmetic after freeze.'],sheet_kind='reused_typed')
