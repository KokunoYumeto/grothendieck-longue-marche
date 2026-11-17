from save_page import save_page
save_page(82,r'''\scanpage{82}
% archive foliation: 81
$C$ courbe lisse \inserted{propre} sur $\mathbf{F}_{\unsure{q|p}}$

$A$ schéma abélien sur $C$.

Des conjectures de Weil, résulte que
\[
H^i(C,A)=0\qquad\text{si }i\ge2
\]
et sans doute, utilisant Tate, on doit avoir
\[
H^1(C,A)=0
\]
Soit $x$ un pt fermé de $C$, $U=C-\{x\}$, alors on a
\diagram{\begin{tikzcd}[column sep=small]
\deleted{\unsure{H^0(C,A)}}\arrow[r,dash]&\deleted{\unsure{H^1_x(C,A)}}\arrow[r]\arrow[d,dashed]&H^1(C,A)\arrow[r]\arrow[d,phantom,"\Vert" description]&H^1(U,A)\arrow[r]&H^2_x(C,A)\arrow[r]&H^2(C,A)\arrow[d,phantom,"\Vert" description]\\
&0&0&&&0
\end{tikzcd}}
d'où
\[
H^1(U,A)\simeq H^2_x(C,A)
\]
Or par Tate,
\[
H^2_x(C,A)\deleted{\unsure{(\ell)}}\quad H^1(K_x,A)\deleted{\unsure{(\ell)}}\quad\uline{\text{dual}}\text{ de }H^0(K_x,A^*)\deleted{\unsure{(\ell)}}
\]
\deleted{\unsure{Ce n'est en général pas un groupe de}}
C'est donc \uuline{essentiellement un $p$-groupe}, modulo groupe fini !

OK.

Peut se généraliser au cas où on prend $X$ régulier dont on enlève un diviseur \uline{régulier} ----
''',[
('top','text','C courbe lisse propre sur F_q'),
('upper','text','A schéma abélien sur C'),
('upper','text','Des conjectures de Weil, résulte que'),
('upper middle','display','H^i(C,A)=0 si i≥2'),
('upper middle','text','et sans doute, utilisant Tate'),
('middle','display','H^1(C,A)=0'),
('middle','text','Soit x un pt fermé de C'),
('middle','diagram','localization sequence with two cancelled terms and zero identifications'),
('middle lower','display','H^1(U,A) ≃ H^2_x(C,A)'),
('lower','text','Or par Tate'),
('lower','display','H^2_x(C,A), H^1(K_x,A), dual de H^0(K_x,A*)'),
('lower','text','Ce n’est en général pas un groupe de'),
('lower','text','C’est donc essentiellement un p-groupe'),
('bottom','text','OK.'),
('bottom','text','Peut se généraliser au cas où on prend X régulier')
],remarks='Whole, halves and lower corrected conclusion enlarged. Three small cancellations in local duality formula are unreadable except for probable (l); all marked. Inverted faint verso type excluded as show-through.')
