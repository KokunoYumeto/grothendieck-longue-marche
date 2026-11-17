from workflow import save_page
save_page(55,r'''
\scanpage{55}
% archive foliation: 54
\[
X=\frac{y^2-x^2}{z^2}\qquad Y=-\frac{2xy}{z^2}
\]
\[
X+iY=\frac1{z^2}(y^2-x^2-2ixy)=\frac1{z^2}(y\unsure{-|+}ix)^2
\]
\[
\begin{aligned}
(X+iY)^n&=\frac1{z^{2n}}(y-ix)^{2n}
=\frac1{z^{2n}}\bigl(P_n(x,y)+iQ_n(x,y)\bigr)\\
&\overset{?}{=}\frac{y'^2-x'^2}{z'^2}\unsure{-|+}2i\frac{x'y'}{z'^2}
\end{aligned}
\]
$x',y',z'$ fonctions rat. de $x,y,z$ ?? P.ex. $z'=z^n$
\[
\deleted{P_n(x,y)=}\quad\frac{\unsure{A_n}(x,y,z)}{\deleted{z^n}}\quad\text{et}\quad B_n
\]
\[
\unsure{B_n|A_n}(x,y)^2-A_n(x,y)^2=P_n(x,y)
\]
\[
-2A_n(x,y)B_n(x,y)=Q_n(x,y)
\]
\[
X+iY=\left(\frac{y-ix}{z}\right)^2=\left(\frac yz-i\frac xz\right)^2
\]
\[
\left(\frac yz\unsure{-|=}i\frac xz\right.\qquad
\left(\frac yz-i\frac xz\right)^{2n+1}
\]
\margin{$(-i)^3=-i(i^2)=i$}
\[
\left(\frac yz-i\frac xz\right)^3
=\frac1{z^3}\left[
\underbrace{y^3\unsure{-|+}3iy^2x\unsure{-|+}3yx^2+ix^3}_{
\begin{gathered}
y^3-3yx^2+i(x^3-3y^2x)\\
y(y^2-3x^2)+ix(x^2-3y^2)
\end{gathered}}
\right]
\]
''',[
('display','top','X=(y^2-x^2)/z^2; Y=-2xy/z^2'),
('display','upper second line','X+iY=1/z^2(y^2-x^2-2ixy)'),
('display','upper long third line','(X+iY)^n=1/z^2n(y-ix)^2n'),
('display','under long equality','question over equals; (y prime squared-x prime squared)/z prime squared'),
('text','middle','x prime,y prime,z prime fonctions rat. de x,y,z ??'),
('deletion','middle left below prose','P_n(x,y)='),
('display','middle below prose','A_n(x,y,z)/z^n et B_n'),
('deletion','denominator in middle fraction','z^n'),
('display','below fold','B_n(x,y)^2-A_n(x,y)^2=P_n(x,y)'),
('display','below preceding','-2A_n(x,y)B_n(x,y)=Q_n(x,y)'),
('display','lower middle','X+iY=((y-ix)/z)^2'),
('display','lower left unfinished','(y/z-i x/z'),
('display','lower centre','(y/z-i x/z)^(2n+1)'),
('margin note','lower right','(-i)^3=-i(i^2)=i'),
('display','bottom three-line expansion','(y/z-i x/z)^3; y^3-3iy^2x-3yx^2+ix^3; underbrace')])
