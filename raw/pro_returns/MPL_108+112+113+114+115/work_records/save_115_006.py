from record import save_page,ROOT,utc
tex=r'''\scanpage{6}
\mspage{2}
% archive foliation: 5
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
A^\circ,\widehat A^\circ,A^\vee\arrow[dr] & \widehat A\\
B^\circ,\widehat B^\circ,B^\vee\arrow[ur] & \widehat B
\end{tikzcd}}\quad(6\text{ Cas})
\[
\left|\widehat A^\circ\ \underset{\unsure{\rightarrow}}{\text{ou}}\ A^\vee\right|
\times\left|\widehat B^\circ\ \text{ou}\ B^\vee\right|\longrightarrow\mathrm{Ens}
\qquad(4\text{ Cas})
\]
\uline{NB}
\diagram{\begin{tikzcd}[row sep=small]
\widehat A^{\circ\unsure{-}}&&A^\vee\\
&A^\circ\arrow[ul,hook]\arrow[ur,hook]&
\end{tikzcd}}
\diagram{\begin{tikzcd}[row sep=small]
\widehat B^\circ&&B^\vee\\
&B^\circ\arrow[ul,hook]\arrow[ur,hook]&
\end{tikzcd}}

\margin{$(\widehat B\rightarrow)$}
\margin{\figure{\begin{tikzpicture}\draw[->,very thick](0,0)--(.4,.4);\node[anchor=west] at (.4,.4){$(\widehat A\rightarrow)$};\end{tikzpicture}}}
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&&&\underline{\mathrm{Hom}}^{!!}(\widehat A^\circ,\widehat B^\circ;\mathrm{Ens})&&&\\
&\underline{\mathrm{Hom}}^!(\widehat B^\circ,\widehat A)\arrow[urr,bend left=15]\arrow[ddl,bend right=15]&&&&\underline{\mathrm{Hom}}^!(\widehat A^\circ,\widehat B)\arrow[ull,bend right=15]\arrow[ddr,bend left=15]\arrow[dl] &\\
&&\underline{\mathrm{Hom}}(B^\circ,\widehat A)\arrow[ul]&&\underline{\mathrm{Hom}}(A^\circ,\widehat B)&&\\
\underline{\mathrm{Hom}}_!^!(A^\vee,\widehat B^\circ;\mathrm{Ens})&&&
\begin{gathered}(A\times B)^\wedge\\=\underline{\mathrm{Hom}}(A^\circ,B^\circ;\mathrm{Ens})\end{gathered}
\arrow[ul]\arrow[ur]\arrow[dl]\arrow[dr]
\arrow[uuu,no head,"\wedge\wedge" description]
\arrow[lll,no head,"\vee\wedge" description]
\arrow[rrr,no head,"\wedge\vee" description]
\arrow[ddd,no head,"\vee\vee" description]
&&&\underline{\mathrm{Hom}}^!_!(\widehat A^\circ,B^\vee;\mathrm{Ens})\\
&&\underline{\mathrm{Hom}}(A^\circ,\widehat B)\arrow[dl]&&\underline{\mathrm{Hom}}(B^\circ,\widehat A)\arrow[dr]&&\\
&\underline{\mathrm{Hom}}_!(A^\vee,\widehat B)\arrow[uul,bend left=15]\arrow[drr,bend right=15]&&&&\underline{\mathrm{Hom}}_!(B^\vee,\widehat A)\arrow[uur,bend right=15]\arrow[dll,bend left=15]&\\
&&&\underline{\mathrm{Hom}}_{!!}(A^\vee,B^\vee;\mathrm{Ens})&&&
\end{tikzcd}}
\margin{$(A^\vee\rightarrow)$\qquad$(B^\vee\rightarrow)$}
Toutes les flèches du diagramme sont des équivalences de catégories

$I$ ens d'indices

$(A_i)_{i\in I}$ famille de (petites) catégories

Si $I'\subset I$, on pose
\[
A_{I'}=\prod_{i'\in I'}A_{i'}
\]
\[
I=\coprod_{j\in J}I_j,\quad J=J^+\amalg J^-\qquad
I^+=\coprod_{j\in J^+}I_{j^+},\quad I^-=\coprod_{j\in J^-}I_{j^-}
\]
Je suppose $I,J$ finis pour ``play safe''.
\figure{\begin{tikzpicture}\draw(0,0)--(3,1.5);\end{tikzpicture}}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
&\widehat A_I\arrow[d,"\unsure{\varphi}"',"\simeq"]&\\
&\underline{\mathrm{Hom}}^{\deleted{\unsure{!}}!}_!\left(
\prod_{j^-\in J^-}A_{I_{j^-}}^\vee,
\prod_{j^+\in J^+}A_{I_{j^+}}^{\wedge\circ};\mathrm{Ens}\right)
\arrow[dl,"\approx"']\arrow[dr,"\approx"]&\\
\underline{\mathrm{Hom}}_!\left(\prod_{j^-\in J^-}A_{I_{j^-}}^\vee,\widehat A_{I^+}\right)
&&\underline{\mathrm{Hom}}^!\left(\prod_{j^+\in J^+}A_{I_{j^+}}^{\wedge\circ},\widehat A_{I^-}\right)
\end{tikzcd}}
'''
el=[('diagram','top right','A°, Ahat°, Avee / B°, Bhat°, Bvee → Ahat / Bhat; 6 Cas'),('display','top right below','|Ahat° ou Avee| × |Bhat° ou Bvee| → Ens; 4 Cas'),('diagram','right NB upper','A° → Ahat°; A° → Avee'),('diagram','right NB lower','B° → Bhat°; B° → Bvee'),('margin note','above circle left','(Bhat →)'),('drawing','above circle right','arrow (Ahat →)'),('diagram','large upper circle','(A×B)^ = Hom(A°,B°;Ens), twelve Hom categories'),('margin note','below circle left/right','(Avee →), (Bvee →)'),('text','right of circle lower','Toutes les flèches du diagramme'),('text','lower left','I ens d’indices'),('text','lower left','(A_i) famille de (petites) catégories'),('text','lower left','Si I′ ⊂ I, on pose'),('display','lower left','A_I′ = product A_i′'),('display','lower middle','I = coproduct I_j; J = J+ ∐ J−; I+, I−'),('text','lower right','Je suppose I,J finis pour “play safe”'),('drawing','above lower diagram','diagonal separating stroke'),('diagram','lower','Ahat_I → Hom → Hom_! / Hom^!'),('deletion','lower diagram first Hom superscript','!')]
save_page(115,6,tex,el,doubts=[('top small diagram','two crossing arrows with retraced upper tip','overwritten extra horizontal stroke possibly an additional arrow','medium'),('NB Ahat exponent','circle followed by short dash','stray stroke','low'),('large circle','Hom exclamation positions','some slightly offset double signs','medium'),('bottom mixed Hom','deleted ! before live upper ! and lower !','overwritten superscript rather than deletion','low'),('bottom vertical arrow label','varphi','phi or question mark','low')],notes='Full circular diagram of equivalences, with four pencil diameters labelled wedge/vee pairs. Text explicitly calls all arrows equivalences. Bottom generalisation to a finite index family; finiteness assumed to “play safe”. Small top diagram has overwritten crossing arrows. Distinguish Ahat opposite and Avee throughout; no mathematical normalization.')
with (ROOT/'progress.log').open('a') as f:f.write('hourly checkpoint 01 persisted '+utc()+' library_file_id=libfile_fde3_f-c4878e56ba38819198474971b04164b6_3de54532f60c8191850458563edee173\n')
