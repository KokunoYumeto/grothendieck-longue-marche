from workflow import save_page
from pathlib import Path
ns={}
exec((Path(__file__).parent/'page006.py').read_text().split("tex=r'''")[0],ns)
tex=r'''\scanpage{27}
\margin{26}
\figure{\begin{tikzpicture}[x=.75cm,y=.75cm,line cap=round,line join=round]
\begin{scope}[shift={(0,0)}]
\draw[yellow!65!green,thick] (-1.1,.8)--(1.1,.8);\draw[yellow!65!green,thick,dashed] (-1.2,-.2)--(1.1,-.2);
\draw[orange!90!yellow,very thick] (-.8,-.6)--(.1,1.4) (-.1,1.45)--(.55,-.8) (-.65,.3)--(.05,-.9) (-.1,-.9)--(.7,1.2);
\node[rotate=180] at (0,.55) {$5$};
\end{scope}
\begin{scope}[shift={(3,0)}]
\draw[orange!90!yellow,very thick] (-.9,.5)--(1,.5) (-.2,1)--(.4,-.9) (.5,1)--(-.1,-.9);\draw[orange!90!yellow,very thick,dashed] (-.3,-.65)--(.7,-.65);
\end{scope}
\begin{scope}[shift={(7.3,-.35)}]
\draw[yellow!65!green,thick] (0,0) ellipse(.65 and 1.3);\draw[yellow!65!green,thick] (-.63,.1) .. controls (-.45,1.8) and (.65,1.3) .. (.64,-.15);\draw[yellow!65!green] (0,1.05) .. controls (.45,1.1) and (.65,.4) .. (.65,-.1);
\end{scope}
\begin{scope}[shift={(0,-2)}]
\draw[yellow!65!green,thick] (-1.2,.7)--(2.5,.7);
\draw[orange!90!yellow,very thick] (-.5,1.15)--(.25,-.4) (.3,1.1)--(-.2,-.75) (-.7,.7)--(-.15,-.85) (.55,.8)--(.15,-.65);
\draw[line width=3pt] (-.27,.72)--(.15,.72) (-.27,.82)--(.15,.82);\draw[very thick,dotted] (-.3,.95)--(.17,.95);
\node[rotate=180] at (-.25,.4) {$4$};\node[rotate=180] at (.25,.35) {$4$};
\draw[orange!90!yellow,very thick] (1,1)--(1.3,-.5) (1.4,1.35)--(1.75,-.35) (1.65,1.4)--(1.55,-.45) (1.9,1.2)--(1.2,-.55);
\fill (1.58,.7) circle(.04);\draw[very thick] (1.15,.55)--(1.65,.55);\draw[very thick,dotted] (1.05,.95)--(1.68,.95);
\end{scope}
\begin{scope}[shift={(5,-2.2)}]
\draw[yellow!65!green,thick] (-1.7,.7)--(1.3,.7);\draw[yellow!65!green,thick,dashed] (-.65,.7)..controls(-.3,-.25)and(.5,.1)..(1.1,.7);
\draw[orange!90!yellow,line width=2pt] (-1.6,.45)--(-1.3,.95) (-1.55,.9)--(-1.5,.4) (-.3,1.3)--(.12,-.65) (-.7,-.6)--(.85,1.25) (-.1,-.4)--(.4,1.2) (1.15,.55)--(1.22,.9);
\draw[orange!90!yellow,line width=2pt] (-1.2,1.1)..controls(-.85,.5)and(-.75,1.3)..(-.8,1.4) (-1.05,-.7)..controls(-.9,-.05)and(-1.5,-.1)..(-1.35,-.2);
\draw[orange!90!yellow,line width=4pt] (-.95,1.1)..controls(-.65,.5)and(-.75,.05)..(-1.1,-.25);
\draw[orange!90!yellow,very thick] (-.5,1.2)--(-.1,1.3) (.65,1.3)--(1,1.1) (-.85,-.6)--(-.65,-.72)--(-.8,-.8) (0,-.65)--(.35,-.55);
\fill (0,.15) circle(.05);
\node[rotate=180] at (-.38,.1) {$p-1$};\node[rotate=180] at (-.25,.3) {$q$};\node[rotate=180] at (-.5,.55) {$p\ge1$};\node[rotate=180] at (-.55,.85) {$q\ge3$};
\node[rotate=180] at (.32,.08) {$p'-1$};\node[rotate=180] at (.38,.3) {$q'$};\node[rotate=180] at (.52,.53) {$p'\ge1$};\node[rotate=180] at (.78,.85) {$q'\ge3$};
\end{scope}
\begin{scope}[shift={(0,-5.1)}]
\draw[yellow!65!green,thick] (-1.2,0)..controls(0,1)and(.6,.65)..(1,.05);\draw (-1.15,0)..controls(-.1,.8)and(.6,.7)..(1,.05) (-.95,.15)..controls(-.2,-.2)and(.6,.1)..(1,.6);
\draw (-.6,-.02)--(-.65,.4) (-.3,0)--(-.4,.52) (-.3,0)--(-.05,.6) (-.05,0)--(.25,.7) (.05,.04)--(.95,.7);
\foreach \x/\y/\v in {-.7/.2/3,-.48/.28/4,-.19/.36/3,.08/.3/4,.4/.3/3}{\node[rotate=180] at(\x,\y){$\v$};}
\end{scope}
\begin{scope}[shift={(4.8,-4.8)}]
\draw (-1.25,.25)..controls(-.2,.65)and(.8,.5)..(1.3,.05)..controls(.5,-.45)and(-.6,-.3)..cycle;
\draw (-1.2,.45)--(1.3,-.2) (-.35,.55)--(.35,-.3) (-.1,.6)--(-.6,-.4) (.2,.6)--(-.4,-.5) (.3,.55)--(-.2,-.35);
\foreach \x/\y/\v in {-.65/.08/4,-.25/.08/3,.02/.07/4,.7/-.05/4}{\node[rotate=180] at(\x,\y){$\v$};}\node[rotate=180] at (-.1,.8) {$3,4,4,4,$};
\end{scope}
\begin{scope}[shift={(7.2,-5.7)}]
\draw[yellow!65!green,thick] (-1.2,.3)--(1.2,.3);\draw (-1,.1)--(1.1,.1);
\draw[orange!90!yellow,very thick] (-1.2,-1.1)--(1.3,.7) (.45,1)--(.9,-.5) (.95,.8)--(.35,-.9) (-.3,.4)--(-.25,-.75) (.1,.4)--(-.5,-.9);
\draw[yellow!65!green] (1,.3)--(1,.1) (.85,.2)--(1.1,.2);
\end{scope}
\begin{scope}[shift={(0,-5.9)}]
\draw (-1.25,.15)..controls(-.3,.65)and(.6,.7)..(1,.3) (-1.4,.35)..controls(-.3,-.2)and(.5,.3)..(1,.65);
\draw (-.65,.75)--(-.2,-.05) (-.4,.65)--(.1,.1) (-.2,-.05)--(.1,.8) (.1,.05)--(.5,.8);
\draw[orange] (-.1,.5)--(.15,.25);\draw (-.1,.5)--(-.02,.6)--(.02,.47)--cycle;
\foreach \x/\v in {-.65/3,-.36/4,.35/4,.65/3}{\node[rotate=180]at(\x,.4){$\v$};}\node[rotate=180]at(-.03,.49){$\unsure{3}$};
\end{scope}
\begin{scope}[shift={(-.75,-6.65)}]
\draw (-1,0)..controls(-.4,.7)and(.1,.3)..(.4,.2) (-1,.3)..controls(-.5,-.3)and(0,.1)..(.4,.45);
\draw (-.6,.4)--(-.4,.05)--(-.3,.45) (-.4,.05)--(-.55,.45) (-.2,.42)--(-.1,.08)--(.1,.37);
\end{scope}
\begin{scope}[shift={(-.1,-7.2)}]
\draw (-1.4,.15)..controls(-.8,.7)and(.5,.65)..(1,.4)..controls(.7,-.2)and(-.9,-.2)..cycle;
\draw (-1.15,.55)--(-.7,-.2) (-.3,.65)--(.2,-.15) (.15,.65)--(.6,-.1) (.05,-.2)--(.55,.8) (.48,-.1)--(.7,.6);\fill(1,.4)circle(.035);
\end{scope}
\begin{scope}[shift={(4.1,-7.15)},rotate=180]
\draw[yellow!65!green,thick] (-1,0)..controls(-.4,-.3)and(.5,-.1)..(1,.4);\draw[orange!90!yellow,thick] (-1,0)..controls(-.3,.5)and(.5,.5)..(1,.4);
\draw (-1.1,-.05)..controls(-.3,.5)and(.5,.5)..(1.1,.4) (-1.1,.05)..controls(-.4,-.3)and(.5,-.1)..(1.1,.5);
\foreach \x in {-.95,-.6,-.2,.2,.6,.95}{\draw[orange!90!yellow,very thick] (\x,-.35)--({\x-.1},.7);}
\foreach \x/\y/\v in {-.75/.05/3,-.4/.05/4,0/.1/4,.4/.2/4,.8/.3/3}{\node at(\x,\y){$\v$};}
\end{scope}
\begin{scope}[shift={(0,-8.5)}]
\draw[yellow!65!green,thick] (-1,.5)--(1.2,.65);\draw[yellow!65!green,dashed,thick] (-.35,.55)..controls(.3,-.1)and(.65,.15)..(1.1,.6);
\draw[orange!90!yellow,very thick] (-.8,.9)--(-.45,-.7) (-.25,1.1)--(-.7,-.7) (-.4,1)--(.05,-.8) (0,1)--(.55,-.65) (.7,1.1)--(.35,-.65) (.2,-.5)..controls(.55,.1)and(.6,.8)..(1,1.05);
\draw[purple!40] (-.65,-.7)--(-.5,-1)--(.05,-.85);\node[rotate=180]at(0,.35){$\unsure{4}$};\node[rotate=180]at(.8,.45){$\unsure{4}$};
\end{scope}
\begin{scope}[shift={(2.2,-8.45)}]
\draw[gray] (-.75,1)--(.9,-.4) (-.9,-.2)--(.8,1.2) (-.7,-1.15)--(.65,-.55) (-.6,-.5)--(.5,-1.3) (-.2,-1)--(.15,-1.35);
\draw[orange!90!yellow,very thick,->] (0,.55)--(-.1,-.65);\draw[orange!90!yellow,very thick,dashed,->] (0,.55)--(.1,1.4);\draw[orange!90!yellow,very thick,dashed] (-.1,-.65)--(-.15,-1.45);\draw[black,dashed] (-.15,.2)--(-.13,-.6) (-.07,-.8)--(.05,-1.3);
\end{scope}
\end{tikzpicture}}

\texttt{//*\quad CRAY2\quad 0352\qquad \unsure{I|1}}
'''+ns['charfigure']([ns['zero']]*4,14)+ns['charfigure']([ns['C'],ns['R'],ns['A'],ns['Y'],ns['T']],14)
row=r'\texttt{****A}&\texttt{END}&\texttt{JOB 352}&\texttt{CRAY2}&\texttt{ROOM}&\texttt{3.11.31 PM 19 AUG 82}&\texttt{R6.PR1}&\texttt{SYS JES2}&\texttt{JOB 352}&\texttt{END}&\texttt{A****}'
tex+='\n\\diagram{\\begin{array}{lllllllllll}\n'+'\\\\\n'.join([row]*6)+'\n\\end{array}}\n'
e=[('drawing','top left','orange crossing lines; 5'),('drawing','top centre','orange X with solid and dashed crossbars'),('drawing','top right','green oval, retraced upper arcs'),('drawing','upper left middle','four orange lines; black strips; 4,4'),('drawing','upper middle','orange concurrent lines and black strips'),('drawing','upper right middle','green line and dotted bend; p,q,p prime,q prime'),('drawing','middle left','lens 3,4,3,4,3'),('drawing','middle centre','crossed lens 4,3,4,4; 3,4,4,4,'),('drawing','middle right','two orange concurrence points and green/black lines'),('drawing','lower left upper','lens with tiny triangle; 3,4,3,4,3'),('drawing','lower left middle','small lens with four chords'),('drawing','lower left middle','larger lens with crossing chords'),('drawing','lower centre','coloured lens 3,4,4,4,3'),('drawing','bottom left','orange intersections and dotted green bend; 4,4'),('drawing','bottom centre','two stars with orange arrow and dashed continuations'),('text','printed header, rotated','//* CRAY2 0352 I'),('drawing','printed banner, rotated','four zero-character glyphs'),('drawing','printed banner, rotated','CRAY2 character glyphs')]+[('text',f'printed job line {i}, rotated','****A END JOB 352 CRAY2 ROOM 3.11.31 PM 19 AUG 82')for i in range(1,7)]
d=[('labelled coloured star','p≥1; q≥3; p prime≥1; q prime≥3','Labels read after 180-degree rotation; primes and inequality strokes are small','medium'),('lower coloured sketch','4;4','Two faint pencil numerals; possible 5-like terminal stroke','low'),('small central triangular region','3','Black strokes merge with tiny numeral','low'),('printed mosaics and header','four 0 figures; CRAY2; I / 1','Repeated-character counts manually compared; exact spacing approximate','medium')]
obs='Sheet contains fifteen separate handwritten sketches, mostly lens subdivisions, concurrence moves and a labelled local configuration p,q,p prime,q prime. All text/drawing labels were additionally inspected in 180-degree orientation. Printed stock: job END, 352, 19 AUG 82 at 3.11.31 PM; not a manuscript date. No mathematical prose or explicit title/page count.'
save_page(27,tex,e,d,obs,sheet_kind='reused_typed')
