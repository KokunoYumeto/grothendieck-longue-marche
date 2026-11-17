from workflow import save_page
save_page(51,r'''
\scanpage{51}
% archive foliation: 50
\[
\cos 2u=\frac{1-\operatorname{tg}^{2}u}{1+\operatorname{tg}^{\unsure{2}}u}
\qquad 2\sin u\cos u=2\uline{$\cos^2u$}\operatorname{tg}u=
\]
\[
\sin 2u=\frac{2\operatorname{tg}u}{1+\operatorname{tg}^2u}
\qquad
\left\{\begin{aligned}x&=\frac{1-t^2}{1+t^2}\\y&=\frac{2t}{1+t^2}\end{aligned}\right.
\]
\[
t=\frac yx\quad\text{quand }z=1
\]
\[
\deleted{\unsure{1+t^4+2t^2}}
\]
\[
t=0
\]
\[
x=1-t^2\quad y=2t\quad z=1+t^2
\]
\[
\deleted{y\qquad t=\pm i}
\]
\[
\begin{aligned}
z=0\quad\text{i.e. }t=\mp i&\Longrightarrow x=2,\ y=\mp2i\quad
\unsure{\sim|=}\quad x=1\quad y=\mp i\\
&&\unsure{\sim|=}\quad x=\pm i\quad y=1\\
y=0\quad\text{i.e. }t=0&\qquad(1,0,1)
\end{aligned}
\]
\[
x^2+y^2+z^2=0
\]
\diagram{\begin{tikzcd}
C_2=X\arrow[r]&\mathbf P^1=\widehat{\operatorname{Spec}}(k[t])\\
(\pm i,1,0)\arrow[r]&t=\mp i\\
(\pm i,0,1)\arrow[r,tail,dash]&t=0
\end{tikzcd}}
\[
t=\frac yx
\]
\[
\begin{aligned}
x'&=1-t^2=1-\frac{y^2}{x^2}=\frac{x^2-y^2}{x^2}\\
y'&=2t=\frac{2y}{x}\\
z'&=1+t^2=\frac{x^2+y^2}{x^2}
\end{aligned}
\]
ou\quad $(x',y',z')=(x^2-y^2,2xy,x^2+y^2)$
\[
\left\{\begin{aligned}x'&=x^2-y^2\\y'&=2xy\\z'&=x^2+y^2\end{aligned}\right.
\qquad
\begin{aligned}
x'^2+y'^2-z'^2&=x^4+y^4-2x^2y^2\\
&\quad+4x^2y^2\\
&\quad\unsure{-|+}(x^2+y^2)^2=0
\end{aligned}
\]
\diagram{\begin{tikzcd}
X\arrow[r,"2"]\arrow[dr,bend right=20,dash,"f_n"']&X'\arrow[r,"{n\text{ impair}}"]&X'\\
&X\arrow[ur,"2"']&
\end{tikzcd}}
\[
\deleted{\unsure{t}}\qquad
s=-\frac{t+i}{t-i}=-\frac{(t+i)^2}{t^2+1}
=-\frac{t^2-1}{t^2+1}-\frac{2it}{t^2+1}
\]
\[
\left(\frac{t+i}{t-i}\right)^n\qquad=
\]
''',[
('display','top left first','cos 2u=(1-tg^2u)/(1+tg^2u)'),
('display','top right first','2 sin u cos u=2 cos^2u tg u='),
('display','top left second','sin 2u=2tg u/(1+tg^2u)'),
('display','top centre braced pair','x=(1-t^2)/(1+t^2); y=2t/(1+t^2)'),
('display','top right below','t=y/x quand z=1'),
('deletion','top right crossed formula','1+t^4+2t^2'),
('display','upper right isolated','t=0'),
('display','upper centre','x=1-t^2; y=2t; z=1+t^2'),
('deletion','upper centre below','y; t=plus or minus i'),
('display','above first fold','z=0 i.e. t=minus or plus i; x=2,y=minus or plus 2i'),
('display','above first fold second','y=0 i.e. t=0; (1,0,1)'),
('display','below first fold left','x^2+y^2+z^2=0'),
('diagram','middle','C_2=X -> P^1; (plus or minus i,1,0); (plus or minus i,0,1)'),
('display','middle right','t=y/x'),
('display','middle lower three equations','x prime; y prime; z prime'),
('text','right beside three equations','ou (x prime,y prime,z prime)='),
('display','bottom left braced equations','x prime=x^2-y^2; y prime=2xy; z prime=x^2+y^2'),
('display','bottom right calculation','x prime squared+y prime squared-z prime squared'),
('diagram','bottom left','X ->2 X prime ->n impair X prime; X ->f_n X ->2 X prime'),
('deletion','left of s formula','t'),
('display','bottom right','s=-(t+i)/(t-i)'),
('display','bottom last','((t+i)/(t-i))^n; equals')])
