from record import save_page
tex=r'''\scanpage{3}
% archive foliation: 2
\[
H_A^{\deleted{\unsure{*}}}
\bigl(f^*(\underset{\substack{\vert\\b^\circ}}{\Psi_*}),
\underset{\substack{\vert\\a^\circ}}{\Phi^{\unsure{*|\circ}}}\bigr)
\overset{?}{\simeq}
H_B\bigl(\Psi_*,f^\circ_!(\Phi^*)\bigr)
\]
\[
\operatorname{Hom}_B(b,f(a))=
\operatorname{Hom}_{\widehat B}(b,f_{\unsure{!}}(a))
\overset{?}{\simeq}\operatorname{Hom}_{\widehat A}(\unsure{f^*b},a)
\]
\[
H_A\bigl(\underset{\wedge}{f^*(b)},\underset{\substack{\vert\\\vee}}a\bigr)
\simeq H_B\bigl(\underset{\wedge}{b^\circ},\underset{\vee}{f^\circ(a)}\bigr)
=\operatorname{Hom}_B(b,f(a))
\]
\[
\unsure{\Vert}\quad\inserted{\overset{\wedge\quad\vee}{\operatorname{Hom}}}
\quad\deleted{\operatorname{Hom}_{\widehat A}(f^*(b),a)=\operatorname{Hom}}
\]
\[
f^*(b)=\varinjlim_{a'\text{ ds }A/b}a'^{\unsure{\circ}}
\]
\[
\unsure{\forall|H_A}\ \varprojlim_{a'\text{ ds }A/b}\operatorname{Hom}_A(a',a)
\]

% The following draft is written in the opposite orientation and crossed by two long diagonal strokes.
\diagram{\begin{array}{l}
\deleted{\widehat B^\circ\unsure{\longrightarrow|{-}}\widehat A}\quad
\left\{\deleted{\unsure{B\times}}\ \deleted{\widehat B^\circ\times}\right.\\
\deleted{B^\vee\unsure{\longrightarrow|{-}}\widehat A}\\
\deleted{\widehat A^\circ\unsure{\longrightarrow|{-}}\widehat B}\\
\deleted{A^\vee\unsure{\longrightarrow|{-}}\widehat B}
\end{array}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (0,1) {$\deleted{\widehat B^\circ}$};
\node at (1.4,1) {$\deleted{B^\vee}$};
\node at (3.4,1) {$\deleted{\widehat A^{\unsure{\circ}}}$};
\node at (4.8,1) {$\deleted{A^\vee}$};
\draw (0,.55)--(0,.35)--(3.4,.35)--(3.4,.55);
\draw (1.4,.55)--(1.4,.45)--(4.5,.45)--(4.5,.6);
\draw (0,.35)--(4.8,.2)--(4.8,.35);
\end{tikzpicture}}

\diagram{\begin{array}{c|c}
\deleted{\widehat A^\circ}&\deleted{\widehat B^\circ}\\
\deleted{A^\vee}&\deleted{B^\vee}
\end{array}}

\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\deleted{\widehat B^\circ}\arrow[r,"\deleted{!}"] & \deleted{\widehat A}
& \deleted{\widehat B^\circ\times\widehat A^\circ}\arrow[r,"\deleted{!!}"]
& \deleted{\operatorname{Ens}}\arrow[dddd,no head,bend left=20]\\
&&\deleted{\widehat B^\circ\times A^\vee}\arrow[r,"\deleted{!}","\deleted{!}"']
&\deleted{\operatorname{Ens}}\arrow[ddddd,no head,bend left=48]\\
\deleted{B^\vee}\arrow[r,"\deleted{!}"'] &\deleted{\widehat A}
&\deleted{B^\vee\times\widehat A^\circ}\arrow[r,"\deleted{!}","\deleted{!}"']
&\deleted{\operatorname{Ens}}\arrow[ddd,no head,bend left=35]\\
&&\deleted{B^\vee\times A^\vee}\arrow[r,"\deleted{!!}"']
&\deleted{\operatorname{Ens}}\arrow[dddd,no head,bend left=65]\\
\deleted{\widehat A^\circ}\arrow[r,"\deleted{!}"] &\deleted{\widehat B}
&\deleted{\widehat A^\circ\times\widehat B^\circ}\arrow[r,"\deleted{!!}"]
&\deleted{\operatorname{Ens}}\\
&&\deleted{\widehat A^\circ\times B^\vee}\arrow[r,"\deleted{!}","\deleted{!}"']
&\deleted{\operatorname{Ens}}\\
\deleted{A^\vee}\arrow[r,"\deleted{!}"'] &\deleted{\widehat B}
&\deleted{A^\vee\times\widehat B^\circ}\arrow[r,"\deleted{!}","\deleted{!}"']
&\deleted{\operatorname{Ens}}\\
&&\deleted{A^\vee\times B^\vee}\arrow[r,"\deleted{!!}"']
&\deleted{\operatorname{Ens}}
\end{tikzcd}}
\figure{\begin{tikzpicture}
\foreach \y in {0,1.5,3,4.5}{\draw (0,\y+.65) .. controls (-.15,\y+.65) and (-.05,\y+.25) .. (-.2,\y)
 .. controls (-.05,\y-.25) and (-.15,\y-.65) .. (0,\y-.65);}
\end{tikzpicture}}

\margin{\deleted{$\underline{\operatorname{Hom}}(\widehat A^\circ,\unsure{''})$}}
\margin{\deleted{\uuline{Hom}\unsure{.}}}
\diagram{\begin{array}{l|ll}
&\deleted{\widehat A}\ \deleted{\text{contr}}&\deleted{\text{contr }\widehat B}\\
&\deleted{A^\vee}\ \deleted{\text{co}}&\deleted{B}
\end{array}}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&\deleted{\widehat A^\circ-\widehat B}\arrow[ddll,no head]\arrow[d,no head]
&&\deleted{\widehat B^\circ-\widehat A}\arrow[dd,no head]\arrow[dl,no head]\\
&\deleted{\widehat A,\widehat B}\arrow[dl,no head,"\deleted{\widehat A}"']
\arrow[rrr,no head,"\deleted{\widehat B}"]&&&\deleted{A^\vee,\widehat B}\arrow[dl,no head,"\deleted{A^\vee}"]\\
\deleted{\widehat A,B^\vee}\arrow[rrr,no head,"\deleted{B^\vee}"']&&&\deleted{A^\vee,B^\vee}
\end{tikzcd}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (1.6,1) {$\deleted{\{A,B\}\times\{\wedge,\vee\}}$};
\node at (1.6,0) {$\deleted{(\unsure{\wedge},\vee)\times(\wedge,\vee)}$};
\draw (.15,1.3)--(.15,1.55)--(2.7,1.55)--(2.7,1.3);
\draw (.1,.75)--(.1,.55)--(2,.55)--(2,.75);
\end{tikzpicture}}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&&\deleted{\underline{\operatorname{Hom}}^!(\widehat A^\circ,\widehat B)}\arrow[dll,bend right=20]\arrow[drr,bend left=15]&&\\
\deleted{\underline{\operatorname{Hom}}^{\unsure{!!}}_{\deleted{\unsure{!}}}(\widehat A^\circ,\widehat B^\circ;\operatorname{Ens})}
&&\deleted{\widehat A}\arrow[dd,no head]
&&\deleted{\underline{\operatorname{Hom}}^{\unsure{!}}_{!}(\widehat A^\circ,B^\vee;\operatorname{Ens})}\\
&\deleted{\wedge\wedge}\ \deleted{\unsure{\operatorname{Ens}\ \underline{\operatorname{Hom}}}}
&&\deleted{\wedge\vee}&\unsure{\wr}\arrow[d,no head]\\
\deleted{\underline{\operatorname{Hom}}^!(\widehat B^\circ,\widehat A)}\arrow[uuu,bend left=10]\arrow[ddd,bend right=15]
&\deleted{\widehat B}\arrow[r,no head]
&\deleted{\widehat{(A\times B)}}\arrow[r,no head]
&\deleted{B^\vee}
&\deleted{\underline{\operatorname{Hom}}_!(B^\vee,\widehat A)}\arrow[uuu,bend right=20]\arrow[ddd,bend left=15]\\
&\deleted{\vee\wedge}
&\deleted{A^\vee}\arrow[u,no head]
&\deleted{\vee\vee}\ \deleted{\unsure{\underline{\operatorname{Hom}}}}&\\
&&&&\\
\deleted{\underline{\operatorname{Hom}}^{\unsure{!}}_{\unsure{!}}(\unsure{A^\vee},\unsure{\widehat B^\circ};\operatorname{Ens})}
&&\deleted{\underline{\operatorname{Hom}}_!(A^\vee,\widehat B)}\arrow[ll]\arrow[rr,bend right=15]
&&\deleted{\underline{\operatorname{Hom}}_{!!}(A^\vee,B^\vee;\operatorname{Ens})}\\
\deleted{\unsure{(\widehat A,\widehat B,\operatorname{Ens})}}&&&&
\end{tikzcd}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,5.7)--(12,0.1);
\draw (5.8,0)--(11.7,7.2);
\end{tikzpicture}}

'''
rows=[
'//PREDONMA JOB CNU0049$NODER=PREDONT',
'/*JOBPARM L=15',
'//COMP EXEC FORTXC,PARM=TERM,REGION=300K',
'//FORT.SYSPRINT DD DSN=&MESSYS,SPACE=(CYL,4),UNIT=SYSDA,DISP=(MOD,PASS)',
'//FORT.SYSTERM DD DSN=&MESCOM,SPACE=(CYL,2),UNIT=SYSDA,DISP=(MOD,PASS)',
'//SYSIN DD DSN=CNU1.MODULEF.V33.INTERME1(MEFCONVS),DISP=OLD',
'//CUTR EXEC PGM=CUTTER',
'//STEPLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
'//TERMINAL DD DSN=&MESCOM,DISP=(OLD,DELETE)',
'//OBJECT1 DD DSN=&ORJ,DISP=(OLD,DELETE)',
'//SOURCE1 DD DSN=&MESSYS,DISP=(OLD,DELETE)',
'//SYSPRINT DD DUMMY',
'//SOURCE2 DD DSN=&SOURCE,SPACE=(CYL,4),UNIT=SYSDA,DISP=(MOD,PASS)',
'//OBJECT2 DD DSN=&ORJ2,SPACE=(CYL,3),UNIT=SYSDA,DISP=(MOD,PASS)',
'//UPDT EXEC PGM=UPDATE,COND=(0,NE,CUTR),PARM=NEW',
'//STEPLIB DD DSN=CNU2.MODULEF.UTIA,DISP=SHR',
'//SYSIN DD DSN=&SOURCE,DISP=(OLD,DELETE)',
'//SYSIN2 DD UNIT=SYSDA,SPACE=(CYL,4)',
'//SYSUT2 DD DSN=CNU2.MODULEF.CONVS,DISP=(,CATLG),SPACE=(TRK,(20,2,35)),',
'// DCB=(RECFM=FB,LRECL=80,BLKSIZE=19040),UNIT=SYSDA,VOL=SER=SYSPPP',
'//SYSPRINT DD SYSOUT=*',
'//LIEN EXEC FORTXL,COND=(0,NE,CUTR)',
'//LKED.SYSLIN DD DSN=&ORJ2,DISP=(OLD,DELETE)',
'//LKED.SYSLMOD DD DSN=CNU2.MODULEF.CONV,SPACE=(TRK,(40,4,35)),',
'// DCB=(RECFM=U,BLKSIZE=19040),UNIT=SYSDA,VOL=SER=SYSPPP,DISP=(,CATLG)',
'//FIN EXEC PGM=IEFBR14,COND=((0,EQ,UPDT),(4,GE,LIEN.LKED),EVEN)',
'//SOURCE DD DSN=CNU2.MODULEF.CONVS,DISP=(OLD,DELETE)',
'//MODEX DD DSN=CNU2.MODULEF.CONV,DISP=(OLD,DELETE)',
'//']
def esc(s):
 return s.replace('&',r'\&').replace('$',r'\$')
lines=[]
for i,s in enumerate(rows):
 t=esc(s)
 if i==0:t=t.replace('PREDONMA',r'\unsure{PREDONMA|PREDONAA}')
 if i==18:t=t.replace('SYSUT2',r'SYSUT\deleted{\unsure{1}}\inserted{2}')
 lines.append(r'\texttt{'+t+'}')
tex+=r'\diagram{\begin{array}{l}'+'\n'+(' \\\\\n'.join(lines))+'\n'+r'\end{array}}'+r'''

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[->](0,4.7)--(.5,4.7);
\draw[->](0,2.2)--(.5,2.2);
\draw[->](0,1.2)--(.5,1.2);
\draw[->](0,.8)--(.5,.8);
\draw[->](6.5,2.2)--(6,2.2);
\end{tikzpicture}}
'''
e=[
('display','original upper left 1','H_A(f*(Psi_*),Phi*) ?= H_B(Psi_*,f! opposite(Phi*))'),
('deletion','first display H','overwritten superscript'),
('display','original upper right','Hom_B(b,f(a))=Hom_Bhat(b,f!(a)) ?= Hom_Ahat(f*b,a)'),
('display','original upper left 2','H_A(f*(b),a)=H_B(b opposite,f opposite(a))=Hom_B(b,f(a))'),
('insertion','original upper left 3','Hom; hat and vee'),
('deletion','original upper left 3','Hom_Ahat(f*(b),a)=Hom'),
('display','original upper left right side','f*(b)=colimit a prime'),
('display','original upper left lower','inverse limit Hom_A(a prime,a)'),
('diagram','rotated upper left','four preliminary functor rows'),
('deletion','rotated preliminary brace','B x; Bhat opposite times'),
('drawing','rotated upper middle','four symbols and three bracket strokes'),
('diagram','rotated middle top','Ahat opposite | Bhat opposite; Avee | Bvee'),
('diagram','rotated left main','four functors, eight bifunctors to Ens, exclamation signs and curved pairings'),
('drawing','rotated left main braces','four braces grouping bifunctors in pairs'),
('margin note','rotated middle','underlined Hom(Ahat opposite, ditto)'),
('margin note','rotated middle','double underlined Hom, mark'),
('diagram','rotated middle classification','Ahat contr contr Bhat; Avee co B'),
('diagram','rotated upper right','six objects and square/triangular connecting lines, hat/vee labels'),
('drawing','rotated right','{A,B} x {hat,vee}; brackets; (hat,vee)x(hat,vee)'),
('diagram','rotated right central wheel','eight Hom categories, inner pair symbols, four radial labels, center (A x B)hat'),
('deletion','wheel','overwritten Hom exclamations and alphabets; Ens Hom labels; bottom parenthesis'),
('drawing','whole opposite-orientation draft','two diagonal cancellation strokes'),
]
for i,s in enumerate(rows,1):e.append(('text',f'rotated printer row {i}',s))
e.extend([('deletion','printer SYSUT','original final digit, probably 1'),('insertion','printer SYSUT','2'),('drawing','printer margins','five arrows pointing to printer records')])
save_page(115,3,tex,e,sheet_kind='reused_typed',doubts=[
('original top display 1','H_A superscript *; Phi*; Psi_*','H superscript deleted; Phi exponent could be opposite circle.','low'),
('original top right','f_!(a); f*b','Adjoint subscript and last overwritten argument uncertain.','medium'),
('original left lower','forall or H_A before inverse limit; a prime opposite','Overwritten initial sign and small superscript.','low'),
('rotated first four arrows','rightward arrows or plain dashes','Small terminal marks may be arrowheads.','low'),
('rotated incomplete margin','Hom(Ahat opposite, ditto)','Unfinished notation, not completed.','low'),
('wheel','Hom exclamation positions; Avee/Bhat opposite','Several symbols overwritten; alternatives are left marked in place.','low'),
('wheel cancelled inner words','Ens Hom; Hom; (Ahat,Bhat,Ens)','Dense scribbles and diagonal strike.','low'),
('rotated geometrical diagram','plain connecting strokes','No clear arrowheads; drawing retained as unoriented connections.','medium'),
('printer first row','PREDONMA','PREDONAA; handwritten overlay obscures job name.','low'),
('printer SYSUT correction','deleted 1, inserted 2','Underlying printed digit partly hidden.','medium')],notes='Two orientations: upright equations (including question-marked Hom/adjunction comparisons) plus an opposite-orientation broad cancelled draft of a four-variance/four-Hom duality wheel. Need record every question and the cancellation status; do not infer missing arrows or normalize Hom variance. Main wheel links four unary Hom categories and four bilinear Hom categories around (A x B)hat. Printer listing is JCL, reused paper; five handwritten pointers and SYSUT digit correction retained. Long diagonal strokes cancel the opposite-orientation mathematical draft, not a theorem proved here.')
