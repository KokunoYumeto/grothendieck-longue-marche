import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{92}
% archive foliation: 94
\begin{verbatim}
//*   CRAY2   0344        I
        00000000      00000000    555555555555       11
      0000000000    0000000000   555555555555       111
    00      0000  00      0000  55               1111
   00     00 00  00     00 00  55                 11
  00     00 00  00     00 00  55                 11
 00     00 00  00   00   00  555555555           11
00  00    00  00  00    00  555555555           11
00 00     00  00 00    00          55         11
0000      00  0000     00          55        11
000       00  000      00         55        11
0000000000    0000000000   555555555555   1111111111
00000000      00000000    55555555555   1111111111
\end{verbatim}
\[
\deleted{M'}\quad P\oplus Q\supset M'\supset2P\oplus2Q
\]
\deleted{\unsure{de}}
\[
\begin{aligned}
\sigma(x,y)&=x-y\\
(1+\sigma)(x,y)&=2x\\
(1\unsure{-|+}\sigma)(x,y)&=2y
\end{aligned}
\]
\[
\deleted{\unsure{\forall x\in P,\ \exists x,y\in M'},\ (1+\sigma)(x,y)=\unsure{x}\quad\text{i.e. }2x}
\]
\[
P=\qquad\deleted{\unsure{x\in(x,y)\in M'}}\qquad
(\deleted{x,y})x+2y\in M'
\]
\[
\left\{\begin{aligned}M'\cap P&=2P\\M'\cap Q&=2Q\end{aligned}\right.
\qquad\text{i.e.}\quad
\underbrace{M'\cap(P+2Q)}_{(M'\cap P)+2Q}=2P+2Q
\]
\begin{verbatim}
 CCCCCCCCCC   RRRRRRRRRRR    AAAAAAAAAA   YY        YY   2222222222
CCCCCCCCCCCC  RRRRRRRRRRRR  AAAAAAAAAAAA  YY        YY  222222222222
CC        CC  RR        RR  AA        AA   YY      YY   22        22
CC            RR        RR  AA        AA    YY    YY             22
CC            RR        RR  AA        AA     YY  YY              22
CC            RRRRRRRRRRRR  AAAAAAAAAAAA      YYYY               22
CC            RRRRRRRRRRR   AAAAAAAAAAAA       YY               22
CC            RR    RR      AA        AA       YY              22
CC            RR     RR     AA        AA       YY             22
CC        CC  RR      RR    AA        AA       YY            22
CCCCCCCCCCCC  RR       RR   AA        AA       YY           222222222222
 CCCCCCCCCC   RR        RR  AA        AA       YY           222222222222
\end{verbatim}
\[
m\subset\underbrace{P/2P}_p\times\underbrace{Q/2Q}_q
\]
sous-module de $k/2k$ modules
\[
\begin{aligned}m\cap p&=0\\m\cap q&=0\end{aligned}
\qquad
\begin{aligned}m&\longrightarrow p\quad\text{injectif}\\m&\longrightarrow q\quad\text{injectif}\end{aligned}
\]
\begin{verbatim}
****A  START  JOB  344  CRAY2       ROOM     3.08.27 PM 19 AUG 82  R6.PR1  SYS JES2  JOB 344  START  A****
****A  START  JOB  344  CRAY2       ROOM     3.08.27 PM 19 AUG 82  R6.PR1  SYS JES2  JOB 344  START  A****
****A  START  JOB  344  CRAY2       ROOM     3.08.27 PM 19 AUG 82  R6.PR1  SYS JES2  JOB 344  START  A****
****A  START  JOB  344  CRAY2       ROOM     3.08.27 PM 19 AUG 82  R6.PR1  SYS JES2  JOB 344  START  A****
****A  START  JOB  344  CRAY2       ROOM     3.08.27 PM 19 AUG 82  R6.PR1  SYS JES2  JOB 344  START  A****
****A  START  JOB  344  CRAY2       ROOM     3.08.27 PM 19 AUG 82  R6.PR1  SYS JES2  JOB 344  START  A****

DERNIERE MISE A JOUR DE JOURNAL : 11-08-82
ATTENTION .........
   ]         UN ARRET EXCEPTIONNEL POUR PREPARER L'ARRIVEE DE NOUVELLES
   ]         UNITES AURA LIEU DU VENDREDI 20 AOUT A 17H 30 AU LUNDI
   ]         23 AOUT A 8H.
\end{verbatim}
\deleted{
$x\mapsto2x:M\longrightarrow M$ injectif

\deleted{\unsure{k}} $k\longrightarrow k'=k[\frac12]$
\[
M\subset M\otimes k'=M'=M'_+\oplus M'_- =\unsure{M_{+k'}}
\]
\margin{\uline{$M$ plat sur $\deleted{\unsure{k[\frac12]}}k$}\par donc $x\mapsto2x$\par $M\longrightarrow M$\par injectif}
\[
\begin{aligned}
M_+&=\{\unsure{m|x}\in M\mid\sigma x=\unsure{x}\}=\operatorname{Ker}(1-\sigma)\\
M_-&=\{\unsure{m|x}\in M\mid\sigma x=-x\}=\operatorname{Ker}(1+\sigma)
\end{aligned}
\]
\[
M_+\cap M_-=0\qquad M/M_++M_-\text{ annulé par }2
\]
\[
2x=\underbrace{(x+\sigma x)}_{\in M_+}+\underbrace{(x-\sigma x)}_{\in M_-}
\]
\[
M_+\oplus M_-\subset M\subset\tfrac12(M_+\oplus M_-)\qquad\text{ou}
\]
\[
2M_++2M_-\deleted{\unsure{\subset}}\subset\underbrace{2M}_{M'}\subset M_+\oplus M_-
\]
}
\[
\deleted{P\quad Q}\quad P,Q\qquad M
\]
\[
m\in P/2P\oplus Q/2Q
\]
\[
(1+\sigma)M'=2M_+\qquad (1\unsure{-|+}\sigma)M'=2M_-
\]
"""
save(92,tex,[('text','printed header','//* CRAY2 0344 I'),('text','printed upper banner twelve rows','00000000 00000000 555555555555 11'),('display','upper right','P direct sum Q superset M prime'),('deletion','before P','M prime'),('deletion','below first display','de'),('display','far upper right','sigma(x,y)=x-y'),('deletion','upper right two-line draft','forall x in P exists x,y in M prime'),('display','below cancelled draft','P= ; x+2y in M prime'),('deletion','after P=','x in (x,y) in M prime'),('deletion','before x+2y','x,y'),('display','upper right brace','M prime intersection P=2P'),('text','printed middle banner twelve rows','CRAY2 character banner'),('display','right middle','m subset P/2P times Q/2Q'),('text','right middle below m','sous-module de k/2k modules'),('display','right middle','m intersection p=0 ; m to p injectif'),('text','printed repeated job lines six rows','****A START JOB 344 CRAY2'),('text','printed journal notice','DERNIERE MISE A JOUR DE JOURNAL'),('text','printed notice title','ATTENTION'),('text','printed notice three rows','UN ARRET EXCEPTIONNEL'),('deletion','lower diagonal stroke through draft','x maps to 2x; k prime; M prime; eigenspaces; inclusions'),('text','lower left cancelled draft','x maps to 2x M to M injectif'),('deletion','lower before k','k'),('display','lower draft','k to k prime=k[half]'),('display','lower draft','M subset M tensor k prime=M prime'),('margin note','lower left','M plat sur k donc x maps to 2x injectif'),('deletion','inside lower margin','k[half]'),('display','lower draft eigenspaces','M+=... M-=...'),('display','lower draft right','M+ intersection M-=0'),('display','lower draft right','2x=(x+sigma x)+(x-sigma x)'),('display','lower draft left','M+ direct sum M- subset M'),('display','foot left','2M+ plus 2M- subset 2M'),('deletion','foot left before subset','subset'),('deletion','foot centre','P Q'),('display','foot centre','P,Q M'),('display','foot centre','m in P/2P direct sum Q/2Q'),('display','foot centre last line','(1+sigma)M prime=2M+')],doubts=[('printed large numeric banner','individual repeated 0,5,1 characters','Character counts and horizontal spacing of the slanted banner are less secure than the ordinary printed lines; reproduced row by row, no OCR.','medium'),('printed CRAY2 banner','repeated C,R,A,Y,2 characters','Character counts and spaces checked visually, with minor spacing approximations.','medium'),('top cancelled equations','forall x in P exists x,y in M prime','Heavy strike and rewriting obscure quantifiers and adjacent indices.','low'),('lower draft last term after M prime decomposition','M_{+k prime}','Term is unfinished or overdrawn, and the entire draft is crossed diagonally.','low'),('eigenspace set variable','m','May be x; variable differs visibly from subsequent x.','medium'),('two (1 minus sigma) expressions','minus','Signs overdrawn; plus is a visual alternative, not a proposed correction.','low'),('lower diagonal cancellation extent','lower draft through 2M inclusions','Large stroke passes through this group, while right-foot P,Q and m notes appear outside its scope.','medium')],notations=[('printed character banners',r'\begin{verbatim}...\end{verbatim}','Characters transcribed as printed text, not replaced by large logo letters.'),('localization',r'k[\frac12]','Fraction inside square brackets.'),('lower m membership',r'm\in P/2P\oplus Q/2Q','The ink is membership here, unlike subset in upper block.')],leads=['Reused computer output bears printed date 19 AUG 82 and journal update 11-08-82; these are not manuscript dates or author page counts.','Rough calculation repeats the involution classification of scan091 and records the intermediate lattice between 2P+2Q and P+Q.'],sheet_kind='reused_typed')
