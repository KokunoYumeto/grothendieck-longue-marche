from record import save_page
printed=[
('09:40:12','0.0242','CSP','JOBNAME GUTS1   SQ 55958'),
('09:40:12','0.0242','CSP','TIME EXECUTING IN CPU - 00:00:00.0242'),
('09:40:12','0.0242','CSP','TIME WAITING TO EXECUTE 00:00:07.6248'),
('09:40:12','0.0242','CSP','TIME WAITING FOR I/O -- 00:00:01.2005'),
('09:40:12','0.0243','CSP','MEMORY USAGE ---     0.04790 MWDS-SEC'),
('09:40:12','0.0243','CSP','DISK BLOCKS MOVED -----      265'),
('09:40:12','0.0243','CSP','PHYSICAL I/O REQUESTS -       29'),
('09:40:12','0.0243','CSP',''),('09:40:12','0.0243','CSP',''),('09:40:12','0.0243','CSP',''),
('09:40:12','0.0243','USER','TIME WAITING FOR JXT-             00:02:21.1570'),
('09:40:12','0.0243','USER','OPEN CALLS-                               14'),
('09:40:12','0.0243','USER','CLOSE CALLS-                              10'),
('09:40:12','0.0243','USER','MEMORY RESIDENT DATASETS-                   0'),
('09:40:12','0.0243','USER','TEMPORARY FILE SPACE USED-                  2 BLOCKS'),
('09:40:12','0.0243','USER','PERMANENT FILE SPACE ACCESSED-              0 BLOCKS'),
('09:40:12','0.0243','USER','PERMANENT FILE SPACE SAVED-                 0 BLOCKS'),
('09:40:12','0.0243','USER','MINIMUM MEMORY USED-                   28160 WORDS'),
('09:40:12','0.0243','USER','MAXIMUM MEMORY USED-                   44032 WORDS'),
('09:40:12','0.0244','USER','MEMORY INTEGRAL (EXECUTION TIME)-     0.00105 MWDS-SEC'),
('09:40:12','0.0244','USER','MEMORY INTEGRAL (I/O WAIT TIME)-      0.04686 MWDS-SEC'),
('09:40:12','0.0244','USER','BLOCKS RECEIVED FROM FRONT END-             0'),
('09:40:12','0.0244','USER','BLOCKS SENT TO THE FRONT END-               1'),
('09:40:12','0.0244','USER',''),('09:40:12','0.0244','USER',''),('09:40:12','0.0244','USER',''),
('09:40:12','0.0244','USER','*'*80),
('09:40:12','0.0244','USER','*                                                                              *'),
('09:40:12','0.0246','USER','*   CPU TIME USED              0.024 SECONDS         0.03 UC CNRS               *'),
('09:40:13','0.0247','USER','*   DISK IO BLOCKS MOVED        0.267 KIOB            0.13 UC CNRS               *'),
('09:40:13','0.0248','USER','*   MEMORY USAGE               0.001 MWDS-SCPU       0.00 UC CNRS               *'),
('09:40:13','0.0250','USER','*                              0.047 MWDS-SIOW       0.02 UC CNRS               *'),
('09:40:13','0.0250','USER','*                                                                              *'),
('09:40:13','0.0251','USER','*   TOTAL SBUS USED                                  1.19 UC CNRS               *'),
('09:40:13','0.0251','USER','*                                                                              *'),
('09:40:13','0.0251','USER','*'*80)]
table='\\diagram{\\begin{array}{llll}\n'
for n,row in enumerate(printed):
 vals=[r'\texttt{'+s+'}' for s in row]
 if n in (26,35): vals[-1]=r'\unsure{'+vals[-1]+'}'
 table+=' & '.join(vals)+r' \\'+'\n'
table+=r'\end{array}}'+'\n'
tex=r'''\scanpage{5}
% archive foliation: 4
'''+table+r'''
% Handwriting to the right of the printed listing, from its top down.
\[
F*k^{(b_\beta^\circ)}\simeq F(b_\beta)
\]
\[
\underbrace{L^{(a)}*k^{(b_\beta^\circ)}}_{G(a)\ \text{où }a\in A}
\simeq L(b_\beta)^{(\mathrm{Hom}_A(b_\beta,a))}
\]
\[
\begin{aligned}
x&\longmapsto\left[k^{(a_\alpha)}*G^{(x^\circ)}
 \simeq G_{\unsure{i}\deleted{\unsure{a}}}^{(x^\circ)}(a_\alpha^\circ)\right.\\
&\simeq G(a_\alpha)^{(\mathrm{Hom}_{\unsure{B}}(a_\alpha^\circ,x^\circ))}\\
&\simeq G(a_\alpha)^{(\mathrm{Hom}_A(x,a_\alpha))}\\
&\simeq L(b_\beta)^{(\mathrm{Hom}_A(b_\beta,a_\alpha)\times\mathrm{Hom}_A(x,a_\alpha))}
\end{aligned}
\]
\[
x\longmapsto\bigoplus_{\alpha,\beta,i}L_i(b_\beta)^{(\mathrm{Hom}(b_\beta,a_\alpha)\times\mathrm{Hom}_A(x,a_\alpha))}
\]
\margin{$L_i^{(\mathrm{Hom}(X,a_\alpha))}$}

$D^b$

\diagram{\begin{tikzcd}[row sep=small]
\unsure{LH}_\bullet^{(k)}\ \text{\unsure{appl. diag.}} & \\
DR_k\ \text{\unsure{opérat. dér.}} & \\
Add_k(A)\arrow[uur,bend right]\arrow[d,Rightarrow] & {}\arrow[uu]\arrow[ul,Rightarrow] \\
D_{lc}^b(\widehat A_k) &
\end{tikzcd}}

\[
D_{lc}^b(\widehat A_k)\longrightarrow D_{lc}^b(\widehat{\unsure{B}}_k)
\]
\[
L_\bullet\qquad a\longmapsto\underbrace{L_\bullet^{(a)}*L_\bullet^B}
\qquad M=\coprod_{\unsure{J}}
\]
\[
\bigoplus_{i,\alpha,\beta}
\left(L_i(b_\beta)^{(\mathrm{Hom}(b_\beta,a_\alpha))}*k^{(a_\alpha)}\right)
\]
\margin{$L_i(b_\beta)^{(a_\alpha)}$}
\[
b\longmapsto M_{i\beta}^{(b)}
\]
\[
\underbrace{k^{(a_\alpha)}*\left[a\longmapsto
\left(L_i^{(a)}*k^{(b_\beta^\circ)}\right)\right]}_{M_{i\beta}}
=\int L_i(b_\beta)^{\mathrm{Hom}(b_\beta,a)}
\]
\margin{$M_{i\beta}^{(b)}$}
\[
k^{(a_\alpha)}*\left[b\longmapsto M_{i\beta}^{(b)}\right]
\simeq M_{i\beta}(a_\alpha)^{(\mathrm{Hom}_A(b,a_\alpha))}
\]
\[
b\longmapsto \deleted{\unsure{L}}\bigoplus_{\alpha,\beta}
L_i(b_\beta)^{(\mathrm{Hom}(b_\beta,a_\alpha)\times\mathrm{Hom}(b,a_\alpha))}
\]
'''
elements=[('diagram',f'printed listing row {i}', ' '.join(row)) for i,row in enumerate(printed,1)]
elements += [('display','upper right first','F*k^(b_beta°) ≃ F(b_beta)'),('display','upper right second','L^(a)*k^(b_beta°) ≃ L(b_beta)^Hom'),('text','underbrace upper right','G(a) où a in A'),('display','right aligned calculation','x ↦ k^(a_alpha)*G^(x°)'),('deletion','right aligned calculation subscript','a'),('display','middle handwritten over listing','x ↦ direct sum L_i(b_beta)'),('margin note','right of printed box','L_i^Hom(X,a_alpha)'),('display','below listing centre','D^b'),('diagram','below listing left bracket','LH, DR_k, Add_k(A), D_lc^b(A-hat_k)'),('display','below listing right','D_lc^b(A-hat_k) → D_lc^b(B-hat_k)'),('display','middle-lower','L_.; a ↦ L_.^(a)*L_.^B; M=coproduct'),('display','lower left','direct sum (L_i(b_beta)^Hom*k^(a_alpha))'),('margin note','lower left above b map','L_i(b_beta)^(a_alpha)'),('display','lower left b map','b ↦ M_i_beta^(b)'),('display','lower right brace','k^(a_alpha)*[a ↦ (L_i^(a)*k^(b_beta°))]'),('margin note','below right calculation','M_i_beta^(b)'),('display','bottom left','k^(a_alpha)*[b ↦ M_i_beta^(b)]'),('display','bottom right','b ↦ direct sum L_i(b_beta)^Hom'),('deletion','bottom right before direct sum','L')]
save_page(112,5,tex,elements,sheet_kind='reused_typed',doubts=[('printed frame','80 asterisks','Exact number of repeated border marks uncertain','low'),('right calculation','B under Hom','A°; handwritten subscript uncertain','low'),('lower bracket','LH; appl. diag.; DR; opérat. dér.','Abbreviations compressed','low'),('lower right target','B-hat_k','Letter overwritten','medium'),('M=coproduct','J','Lower glyph may be an integral','low'),('lower equations','a_alpha, b_beta and i','Indices small; all retained with best reading','medium')],notes='Reused computer accounting printout, JOBNAME GUTS1 SQ 55958, fully transcribed without OCR. Handwritten sheet is a chain of representable-pairing/direct-sum calculations, with a derived-category comparison but no explanatory proof or explicit numbered theorem. Lower bracket abbreviations and some diagram connections remain uncertain; do not build a research conclusion on them alone.')
