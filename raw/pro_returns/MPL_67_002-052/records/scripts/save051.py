import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save

def char_picture(lines):
    out=[r'\figure{\begin{tikzpicture}[x=0.12cm,y=0.22cm]']
    for row,line in enumerate(lines):
        for col,ch in enumerate(line):
            if ch!=' ': out.append(r'\node[inner sep=0pt,font=\ttfamily\tiny] at ('+str(col)+','+str(-row)+'){'+ch+'};')
    out.append(r'\end{tikzpicture}}')
    return '\n'.join(out)
z=[
'           00000000',
'         0000000000',
'       00      0000',
'      00     00 00',
'     00    00  00',
'    00   00   00',
'   00  00    00',
'  00 00     00',
' 0000      00',
'000       00',
'0000000000',
'00000000',
]
zero_lines=[('  '.join([s.ljust(20)]*4)).rstrip() for s in z]
logo=[
' CCCCCCCCCC   RRRRRRRRRRR   AAAAAAAAAA   YY        YY   2222222222 ',
'CCCCCCCCCCCC  RRRRRRRRRRRR  AAAAAAAAAAAA  YY        YY  222222222222',
'CC        CC  RR        RR  AA        AA   YY      YY   22        22',
'CC            RR        RR  AA        AA    YY    YY              22',
'CC            RR        RR  AA        AA     YY  YY               22',
'CC            RRRRRRRRRRRR  AAAAAAAAAAAA      YYYY               22 ',
'CC            RRRRRRRRRRR   AAAAAAAAAAAA       YY               22  ',
'CC            RR    RR      AA        AA       YY             22    ',
'CC            RR     RR     AA        AA       YY           22      ',
'CC        CC  RR      RR    AA        AA       YY         22        ',
'CCCCCCCCCCCC  RR       RR   AA        AA       YY        222222222222',
' CCCCCCCCCC   RR        RR  AA        AA       YY        222222222222',
]
body=r'''% archive foliation: 53
% Printed matter is upright in the supplied scan; the manuscript is inverted.
\texttt{//*\quad CRAY2\quad 0369\qquad I}
'''+char_picture(zero_lines)+'\n\n'+char_picture(logo)+r'''

\begin{verbatim}
****A  START JOB  369  CRAY2             ROOM       3.45.56 PM 16 AUG 82  R6.PR1   SYS JES2 JOB  369 START A****
****A  START JOB  369  CRAY2             ROOM       3.45.56 PM 16 AUG 82  R6.PR1   SYS JES2 JOB  369 START A****
****A  START JOB  369  CRAY2             ROOM       3.45.56 PM 16 AUG 82  R6.PR1   SYS JES2 JOB  369 START A****
****A  START JOB  369  CRAY2             ROOM       3.45.56 PM 16 AUG 82  R6.PR1   SYS JES2 JOB  369 START A****
****A  START JOB  369  CRAY2             ROOM       3.45.56 PM 16 AUG 82  R6.PR1   SYS JES2 JOB  369 START A****
****A  START JOB  369  CRAY2             ROOM       3.45.56 PM 16 AUG 82  R6.PR1   SYS JES2 JOB  369 START A****
\end{verbatim}
\texttt{DERNIERE MISE A JOUR DE JOURNAL : 11-08-82}

\texttt{ATTENTION \unsure{.............|..............}}

\begin{verbatim}
]     1. UNE MODIFICATION SYSTEME NOUS CONTRAINDRA A DETRUIRE
]        LE CONTENU DU DISQUE-SPOOL LE MARDI 17 AOUT A 6 HEURES
]        VEUILLEZ RECUPERER VOS SORTIES EN ATTENTE AVANT CETTE
]        DATE. MERCI DE VOTRE COMPREHENSION.
]     2. UN ARRET EXCEPTIONNEL POUR PREPARER L'ARRIVEE DE NOUVELLES
]        UNITES AURA LIEU DU VENDREDI 20 AOUT A 17H 30 AU LUNDI
]        23 AOUT A 8H.
\end{verbatim}

% Manuscript, read after rotating the sheet through 180 degrees.
\figure{\begin{tikzpicture}[scale=.65]
\draw (0,0)--(0,.7)..controls(-.05,1)and(.35,1.15)..(.32,.91)..controls(.23,.77)and(-.07,.75)..(0,.7);
\draw[thin] (.4,-3)..controls(.35,-1.4)and(2,-1.25)..(2.05,-3.1);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.8cm,y=.8cm]
\draw (0,0) ellipse (1.8 and 2.15);
\draw (0,0) ellipse (1.78 and .43);
\draw[thick] (0,2.15)..controls(-.7,1.25)and(-.85,-1.65)..(-.1,-2.15);
\draw[dashed] (0,2.15)..controls(.2,.8)and(.07,-.8)..(-.1,-2.15);
\draw (-.1,-2.15)..controls(1.15,-1.7)and(1.6,1.7)..(.88,1.8);
\draw[dashed] (.88,1.8)..controls(.6,.8)and(.6,-.7)..(.63,-1.55);
\draw (-1.6,-.14)..controls(-1.4,-.5)and(-.8,-1.15)..(-.1,-2.15);
\draw[thin] (-1.6,-.14)..controls(-.45,.05)and(-.2,.6)..(0,2.15);
\fill (-1,.33) circle (.055) node[above] {$1$};
\fill (1.2,.2) circle (.045) node[right] {$0$};
\fill (.5,-.4) circle (.045) node[below] {$\infty$};
\draw (-1.56,-.12) circle (.10); \draw (-1.56,-.12) circle (.15);
\node[below] at (-1.56,-.2) {$\unsure{\alpha|\infty}$};
\fill (-.4,-.37) circle (.045); \fill (.02,.42) circle (.045);
\draw (.81,1.77)--(.98,1.77) (.89,1.68)--(.89,1.87);
\draw (.55,-1.57)--(.73,-1.57) (.64,-1.67)--(.64,-1.48);
\end{tikzpicture}}

\[
\mathcal T_{0,4}^{+!}\simeq\Pi_{0,3}\quad\deleted{\unsure{m}}
\]
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
1\arrow[r]&\Pi_{0,3}\arrow[r]\arrow[d,equal]&\mathcal T_{0,4}^{+}\arrow[r]\arrow[d,"{\mathrm{can}^{\unsure{t}}}"]&\widetilde{\mathfrak S}_4\arrow[r]\arrow[d,"\mathrm{can}"]&1\\
1\arrow[r]&\Pi_{0,3}\arrow[r,dash]&\mathcal T_{\unsure{0|1},1[\unsure{1}]}^{+}\arrow[r]\arrow[d,equal]&\widetilde{\mathfrak S}_3\arrow[r]\arrow[d,equal]&1\\
&&\mathrm{SL}(2,\mathbb Z)/\!\pm1&\mathrm{SL}(2,\mathbb Z/2\mathbb Z)&
\end{tikzcd}}
\[
\mathcal T_{0,4}^{+!}\simeq\mathcal T_{\unsure{0|1},1}^{+}/\!\pm1
\quad\begin{matrix}\Vert\\ \mathrm{SL}(2,\mathbb Z)/\!\pm1\end{matrix}
\]

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
0\arrow[r]&\Pi_{0,3}\arrow[r]&\mathcal T_{\unsure{0|1},1}^{+}\arrow[r]\arrow[d,equal]&\deleted{\unsure{\mathbb Z\times\mathbb Z}}\ \widetilde{\mathfrak S}_3\arrow[r,dash]\arrow[d,equal]&1\\
&\deleted{\unsure{\ell_1\ \ell_0\ \ell_1\ \ell_2}}&\mathrm{SL}(2,\mathbb Z)&\mathrm{SL}(2,\mathbb Z/4\mathbb Z)/---&
\end{tikzcd}}
\[
\unsure{\mathrm{GL}|\mathrm{PGL}}(2,\mathbf F_2)
\]

\[
\mathrm{SL}(2,\mathbb Z)/\underbrace{(\pm1.\mathbb Z)}_{\text{\uline{Borel}}}
\simeq\unsure{\mathbf P^1_{\mathbb Z}|\mathbf P^1(\mathbb Z)}
\simeq\mathbf P^1(\mathbb Q)
\]
\diagram{\begin{tikzcd}
\unsure{\mathbf P^1_{\mathbb Z}|\mathbf P^1(\mathbb Z)}\arrow[d]\\
\mathbf P^1(\mathbb Z/2\mathbb Z)
\end{tikzcd}}
\[
\ell_0\ \ell_1\ \ell_2\ \ell_3=1
\]
\[
\ell_0\ell_1\ell_\infty=1\qquad
\ell'_\infty=\ell_\infty^{\unsure{\prime}}
\]
\[
\ell'_{\unsure{\infty|0}}\ell'_2\ell'_3=1
\]

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (0,1.4) {$\mathcal T$};
\node at (1.7,1.4) {$\Pi_{0,3}$};
\draw[very thick] (3.8,1.5)..controls(3.45,2.35)and(3.15,.3)..(3.6,-.3)..controls(3.9,-.6)and(4.0,-.1)..(4.05,.1);
\draw[dashed] (3.8,1.5)..controls(3.95,1.0)and(4.1,.4)..(4.05,.1);
\node[font=\Large] at (1.0,.1) {$\mathcal T S D$};
\node[font=\Large] at (.8,-.7) {$\mathcal T S$};
\node[font=\Large] at (2.5,-.7) {$\mathcal T D$};
\node[font=\Large] at (2.0,-1.55) {$\unsure{\mathcal T|\mathfrak T}$};
\node[font=\Large] at (4.7,-.7) {$\Pi D$};
\node[font=\Large] at (4.7,-1.5) {$\Pi S\quad\Pi D$};
\node[font=\Large] at (4.7,-2.3) {$\mathbb T$};
\end{tikzpicture}}

\[
\mathcal T_{0,4}^{+!}\qquad
\mathcal T^+\ \deleted{\unsure{\mathcal T}}
\]
\diagram{\begin{array}{ll}
\text{groupoïdes}&\mathcal T\\
\text{groupes}&T\\
\text{multiplicités}&M\\
\text{\uline{espaces} de T}&\widetilde M
\end{array}}
\[
T^+,\ T^!,\ T^{+!},\quad T/T^+
\qquad\mathrm{GL}(2,\mathbb Z)/\mathbb Z^*
\]

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
1\arrow[r]&\Pi_{g,\nu-1}\arrow[r]&\unsure{\mathbb T|\mathcal T}_{g,\nu}\arrow[r]\arrow[d,"\simeq",phantom,sloped]&\underbrace{\unsure{\mathbb T|\mathcal T}_{g,\nu-1}}_{X_{g,\nu-1}}\arrow[r]&1\\
&&\Pi(\mathcal X_{g,\nu-1},\unsure{\mathbb T|\mathcal T}_{g,\nu-1};s_\nu)&&
\end{tikzcd}}
\[
X_{g,\nu-1}\subset\mathcal X
\]

\figure{\begin{tikzpicture}[x=.75cm,y=.75cm]
\draw (0,0) ellipse (1.55 and 1.9);
\draw (0,1.9)..controls(-1,-.5)and(-.9,-1.8)..(0,-1.9);
\draw[thick] (0,1.9)..controls(.95,1)and(.9,-1)..(0,-1.9);
\draw[dashed] (0,1.9)..controls(.55,1.55)and(.7,1.1)..(.72,.7);
\node at (-1.4,.15) {$\unsure{\alpha_0|d_0}$};
\end{tikzpicture}}

\[
\unsure{\mathcal M|M}_{g,\nu}-
\]
\figure{\begin{tikzpicture}[x=.8cm,y=.8cm]
\draw (0,0) ellipse (1.85 and 1.95);
\draw (0,-.4) ellipse (1.82 and .4);
\draw[thin] (.03,1.95)..controls(-.75,1.8)and(-1.25,.25)..(-1.2,-.7);
\draw (.03,1.95)..controls(1.6,1.75)and(1.4,.15)..(1.2,-.68);
\draw (.03,1.95)..controls(.4,1.0)and(.05,.9)..(0,.4);
\fill (.03,1.95) circle (.05); \draw(-.03,2.16)--(.04,2.1)--(.1,2.16);
\fill (-1.2,-.7) circle (.055) node[below] {$0$};
\fill (1.2,-.68) circle (.055) node[below] {$1$};
\fill (0,.4) circle (.055) node[right] {$\infty$};
\node at (2.8,.4) {$\Pi_{0,3}$}; \node[font=\Large] at (4.0,.4) {$\mathfrak S_3$};
\end{tikzpicture}}
'''
save(51,body,[
('text','printed top','//* CRAY2 0369 I'),
('drawing','printed upper','Four character-built zero forms'),
('drawing','printed centre','CRAY2 character lettering'),
('text','printed lower','Six START JOB 369 lines'),
('text','printed foot','DERNIERE MISE A JOUR DE JOURNAL'),
('text','printed foot','ATTENTION; notices 1 and 2'),
('drawing','manuscript upper left','Faint loop and arch'),
('drawing','manuscript upper left','Sphere: 0,1,infinity,alpha; meridians'),
('display','manuscript upper','T04 +! and Pi03'),
('deletion','manuscript upper','m after Pi03'),
('diagram','manuscript upper middle','Two group sequences and SL identifications'),
('display','manuscript upper right','T04+! = T01+/+-1'),
('diagram','manuscript upper right below','0 -> Pi03 -> T01+ -> tilde S3 - 1'),
('deletion','manuscript upper right below','Z times Z; ell indices'),
('display','manuscript upper middle below','GL(2,F2)'),
('display','manuscript left middle','SL(2,Z)/(+-1.Z); Borel'),
('diagram','manuscript left middle','P1Z to P1(Z/2Z)'),
('display','manuscript left middle','ell0 ell1 ell2 ell3=1'),
('display','manuscript left middle below','ell0 ell1 ell infinity; primes'),
('drawing','manuscript centre','Calligraphic letters and curved open stroke'),
('display','manuscript middle','T04+!; T+'),
('deletion','manuscript middle','Calligraphic T'),
('diagram','manuscript middle','groupoides/groupes/multiplicites/espaces de T'),
('display','manuscript middle right','T+, T!, T+!, T/T+; GL(2,Z)/Z*'),
('diagram','manuscript middle right','1 -> Pi g nu-1 -> T g nu -> T g nu-1 -> 1'),
('display','manuscript middle right below','X g nu-1 subset script X'),
('drawing','manuscript lower left','Ellipse and meridian; alpha0'),
('display','manuscript lower middle','M g nu -'),
('drawing','manuscript lower middle','Sphere with 0,1,infinity; Pi03 and S3')
],sheet='reused_typed',leads='Birman-type sequence with Pi(g,nu-1), double-stroked T and family script X; groupoid/group/multiplicity/Teichmuller space alphabet key; low-genus modular/symmetric quotient sequences, Borel-coset projective-line identifications and two gluing relations ell0 ell1 ell-infinity=1 / primed relation. These are manuscript claims not checked results. Several indices visually resemble 0 where expected genus 1 must not overwrite ink. Printed computer header and notices dated August 1982 provide reused-sheet provenance, not a date asserted for the handwriting.')
