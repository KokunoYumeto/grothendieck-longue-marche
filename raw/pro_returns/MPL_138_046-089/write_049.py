from workflow import save_page
save_page(49,r'''
\scanpage{49}
% archive foliation: 48
\[
z'=z^3
\]
\[
y'=y(y^2-3x^2)
\]
\[
x'=-x(x^2-3y^2)
\]
\[
\begin{aligned}
z^6+y^2(y^4+9x^4-6x^2y^2)+x^2(x^4+9y^4-6x^2y^2)\\
{}=x^6+y^6+z^6+\unsure{3|9}x^2y^2(x^2+y^2)
=\deleted{(x^2+y^2+z^2)^3}\\
{}=x^6+y^6+z^6-3x^2y^2z^2
\end{aligned}
\]
\[
\left(\frac yz\right)^2+\left(\frac xz\right)^2=-1
\qquad x^6+y^6+z^6+
\]
$a$ et $b$
\[
\deleted{a^2+b^2=-1}
\]
\[
\deleted{x^2+y^2+z^2}\qquad\deleted{x^6+y^6+3}
\]

\diagram{\begin{tikzcd}[column sep=large,row sep=small]
0\arrow[r,bend left=20]&0\\
X\quad\unsure{2}&X'\\[-1ex]
1\quad -1\arrow[r,bend right=20]\arrow[r,bend right=8,shorten <=12pt,shorten >=12pt]&1\\
\infty\arrow[r,bend right=18]\arrow[dd,dash]&\infty\arrow[dd,"n"]\\
&\\
{}&{}
\end{tikzcd}}
\[
\frac{p(x)}{q(x)}=\lambda
\]
\[
p(x)-\lambda q(x)=0
\]
\[
p'(x)-\lambda q'(x)=0
\]
\[
\lambda=\frac{p'}{q'}\qquad p-\frac{p'}{q'}q=0
\]
\[
(x^2)^n=(\unsure{\pm}x^n)^2
\]
\[
\frac{\unsure{a}z^2+bz+c}{z^2}\qquad
\deleted{q'p\unsure{-}}\quad p'q-q'p=0
\]
\[
\deleted{\unsure{a}}\qquad 2z(az^2+bz+c)-
\]
''',[
('display','top line 1',"z'=z^3"),
('display','top line 2',"y'=y(y^2-3x^2)"),
('display','top line 3',"x'=-x(x^2-3y^2)"),
('display','upper middle long calculation','z^6+y^2(y^4+9x^4-6x^2y^2)'),
('deletion','end of equality second line','(x^2+y^2+z^2)^3'),
('display','middle left','(y/z)^2+(x/z)^2=-1'),
('display','middle right','x^6+y^6+z^6+'),
('text','middle centre','a et b'),
('deletion','middle right below','a^2+b^2=-1'),
('deletion','lower edge of upper half left','x^2+y^2+z^2'),
('deletion','lower edge of upper half centre','x^6+y^6+3'),
('diagram','lower left','X, X prime; 0,1,-1,infini; n'),
('display','lower right top','p(x)/q(x)=lambda'),
('display','lower right next','p(x)-lambda q(x)=0'),
('display','lower right next',"p'(x)-lambda q'(x)=0"),
('display','lower right pair',"lambda=p'/q'; p-(p'/q')q=0"),
('display','bottom centre','(x^2)^n=(plus or minus x^n)^2'),
('display','bottom centre lower','(az^2+bz+c)/z^2'),
('deletion','bottom right before p prime q',"q'p-"),
('display','bottom right',"p'q-q'p=0"),
('deletion','bottom below fraction','a'),
('display','last line','2z(az^2+bz+c)-')])
