# Proposed inventory reconciliation

These are proposals only. The inventory and page files were not changed. For the listed scan/kind combinations, replace the listed existing grouped rows with the candidate rows. Each candidate corresponds to one actual state-macro occurrence, including nested cancellations. Other rows remain unchanged. Root should review and renumber. Positions below are exact TeX locations, not new visual judgments.

## Scan 097

Replace existing row IDs: 097-01.

### 097-QA-diagram-01: diagram, line 3

```latex
\diagram{\begin{tikzcd}
0 \arrow[r,no head] & L \arrow[r,no head] \arrow[d,"-\mathrm{id}"'] & E \arrow[r,no head] \arrow[d,"g","?"'] & \underline{\mathcal O} \arrow[r] \arrow[d,"\mathrm{id}"] & 0\\
0 \arrow[r,no head] & L \arrow[r,no head] & \mathcal A\otimes L \arrow[r,"\varphi\otimes\mathrm{id}_L"] & \underline{\mathcal O} \arrow[r] & 0
\end{tikzcd}}
```

### 097-QA-diagram-02: diagram, line 7

```latex
\diagram{\begin{tikzcd}\text{Attention au \unsure{signe}}\arrow[r]&\end{tikzcd}}
```

### 097-QA-figure-01: drawing, line 31

```latex
\figure{\begin{tikzpicture}\node (s) at (0,0) {\unsure{signe}};\draw (0,0) ellipse (.6 and .2);\draw[->] (0,.2)--(.1,.6);\end{tikzpicture}}
```

## Scan 099

Replace existing row IDs: 099-07, 099-09, 099-12, 099-14, 099-16, 099-19, 099-23.

### 099-QA-deleted-01: deletion, line 12

```latex
\deleted{Pour expliciter $i$, il faut donner les deux composés
$\inserted{\alpha=}i\circ *$, $\inserted{\beta=}i\circ\mathrm{inj}$,
en sorte que $\alpha\circ\mathrm{inc}=2\beta$.}
```

### 099-QA-inserted-01: insertion, line 13

```latex
\inserted{\alpha=}
```

### 099-QA-inserted-02: insertion, line 13

```latex
\inserted{\beta=}
```

### 099-QA-deleted-02: deletion, line 15

```latex
\deleted{\diagram{\begin{tikzcd}[column sep=large]
E_1\otimes E_2 \arrow[dr,"*"] \arrow[rr,bend left=25,"?"] & & E_1\otimes E_2\\
\begin{array}{c}L_1\otimes E_2\oplus E_1\otimes L_2\\E_1*_0E_2\end{array} \arrow[u,hook,"\mathrm{inc}"] \arrow[drr,no head,"\deleted{\unsure{\mathrm{proj}}}"'] & E \arrow[ur,"i"] & \\
& L_1\otimes L_2 \arrow[u,hook,"\mathrm{inj}"] \arrow[uur,bend right=25,"?\ \text{i.e. can.}"'] &
\end{tikzcd}}}
```

### 099-QA-deleted-03: deletion, line 17

```latex
\deleted{\unsure{\mathrm{proj}}}
```

### 099-QA-deleted-04: deletion, line 20

```latex
\deleted{\deleted{Je pense} on voudra $L_1\otimes L_2\longrightarrow E_1\otimes E_2$ inclusion canonique, donc un \unsure{hom}}
```

### 099-QA-deleted-05: deletion, line 20

```latex
\deleted{Je pense}
```

### 099-QA-deleted-06: deletion, line 21

```latex
\deleted{\diagram{\begin{tikzcd}
E_1\otimes_0 E_2\;\deleted{\unsure{L_2}} \arrow[r,no head] & \unsure{E_1\otimes L_2}\subset E_1\otimes E_2\\
E_1\otimes E_2 \arrow[u,no head,"\unsure{\cap}"] \arrow[ur,dashed,"?"'] &
\end{tikzcd}}}
```

### 099-QA-deleted-07: deletion, line 22

```latex
\deleted{\unsure{L_2}}
```

### 099-QA-deleted-08: deletion, line 25

```latex
\deleted{(pour $\boxed{\uuline{\unsure{\chi}=2.}}$),}
```

### 099-QA-deleted-09: deletion, line 26

```latex
\deleted{\deleted{Je pense} Considérons les inv. canoniques $\sigma_1,\sigma_2$ de $E_1$, de $E_2$, d'où $\sigma=\sigma_1\otimes\sigma_2$ de $\unsure{E}$, noté $\xi\mapsto\bar\xi$. Je pense à l'hom
\[
\xi\longmapsto\xi+\bar\xi
\]
donc
\[
\begin{aligned}
x_1\otimes x_2&\longmapsto x_1\otimes x_2+\bar x_1\otimes\bar x_2\\
&=x_1\otimes x_2+(\unsure{\overline T_1|\varpi_1}\inserted{\psi_1(x_1)}-x_1)\otimes(\unsure{\overline T_2|\varpi_2}\inserted{\psi_2(x_2)}-x_2).
\end{aligned}
\]
Si $x_1=u_1\in\Gamma L_1$, alors on trouve $\bar x_1=-u_1$,
\[
u_1\otimes x_2\longmapsto u_1\otimes x_2+(-u_1)(\unsure{\overline T_2|\varpi_2}\psi_2(x_2)-x_2)
\]
}
```

### 099-QA-deleted-10: deletion, line 26

```latex
\deleted{Je pense}
```

### 099-QA-inserted-03: insertion, line 34

```latex
\inserted{\psi_1(x_1)}
```

### 099-QA-inserted-04: insertion, line 34

```latex
\inserted{\psi_2(x_2)}
```

## Scan 102

Replace existing row IDs: 102-02, 102-05, 102-06, 102-11, 102-14, 102-17.

### 102-QA-deleted-01: deletion, line 3

```latex
\deleted{^{\unsure{\natural}}}
```

### 102-QA-deleted-02: deletion, line 9

```latex
\deleted{\unsure{\overline T_1}\psi_1(x_1)}
```

### 102-QA-inserted-01: insertion, line 9

```latex
\inserted{\operatorname{Tr}_1(x_1)}
```

### 102-QA-deleted-03: deletion, line 10

```latex
\deleted{\unsure{\overline T_2}\psi_2(x_2)}
```

### 102-QA-inserted-02: insertion, line 10

```latex
\inserted{\operatorname{Tr}_2(x_2)e_2}
```

### 102-QA-deleted-04: deletion, line 19

```latex
\deleted{\unsure{^{\natural}}}
```

### 102-QA-deleted-05: deletion, line 23

```latex
\deleted{\unsure{la structure}}
```

### 102-QA-inserted-03: insertion, line 27

```latex
\inserted{donc}
```

## Scan 106

Replace existing row IDs: none.

### 106-QA-figure-01: drawing, line 44

```latex
\figure{\begin{tikzpicture}
\node at (0,0) {$N_{A_1\otimes A_2/O}(\xi)=$};
\node at (2.3,0) {$\xi_0$};
\node at (2.8,0) {$\xi_1$};
\node at (3.3,0) {$\xi_2$};
\node at (3.8,0) {$\xi_3$};
\node at (4.15,0) {$.$};
\draw (2.12,-.17)--(2.12,-.42)--(3.95,-.42)--(3.95,-.17);
\draw (2.65,.2)--(2.65,.4)--(3.45,.4)--(3.45,.2);
\end{tikzpicture}}
```

## Scan 113

Replace existing row IDs: none.

### 113-QA-figure-01: drawing, line 7

```latex
\figure{\begin{tikzpicture}\draw[->] (.6,.6)--(0,0);\end{tikzpicture}}
```

## Scan 132

Replace existing row IDs: 132-06.

### 132-QA-diagram-01: diagram, line 10

```latex
\diagram{\begin{tikzcd}[column sep=huge,row sep=large]
& E_1\vee E_2\arrow[dl,"\Theta_{p_1,p_2}"',"\sim"]\arrow[d,no head,"\Theta_{p'_1,p'_2}"',"\sim"]\arrow[dr,"\Theta_{p''_1,\unsure{p''_3|p''_2}}","\sim"'] &\\
M\oplus L\arrow[r,"\substack{(U_1,U_2,U)\\\Theta_{(p_1,p_2)(p'_1,p'_2)}\\\sim}"]\arrow[rr,bend right=25,"\substack{U''_1,U''_2,U''\\\Theta_{(p_1,p_2)(p''_1,p''_2)}}"'] & M\oplus L\arrow[r,"\substack{(U'_1,U'_2,U')\\\Theta_{(p'_1,p'_2)(p''_1,\unsure{p''_3|p''_2})}\\\sim}"] & M\oplus L
\end{tikzcd}}
```

### 132-QA-diagram-02: diagram, line 51

```latex
\diagram{\begin{tikzcd}[row sep=small]
(p_1,p_2)\arrow[d]\\(p'_1,p'_2)\arrow[d]\\\uline{(p''_1,p''_2)}
\end{tikzcd}}
```

## Scan 134

Replace existing row IDs: 134-01, 134-06, 134-08, 134-09, 134-12, 134-15, 134-18, 134-20.

### 134-QA-diagram-01: diagram, line 2

```latex
\diagram{\begin{tikzcd}[column sep=huge,row sep=large]
& E_1\unsure{\wedge|\vee}E_2\arrow[dl,very thick,"\Theta_{p_1*p_2}"']\arrow[dr,"\Theta_{p'_1*p'_2}=\Theta_{p_1*p_2}\unsure{-|+}U"] &\\
(M_1\otimes M_2)\oplus(L_1\otimes L_2)\arrow[rr] && (M_1\otimes M_2)\oplus(L_1\otimes L_2)\\
b_1,b_2&&b'_1,b'_2
\end{tikzcd}}
```

### 134-QA-diagram-02: diagram, line 20

```latex
\diagram{\begin{tikzcd}[row sep=small]
U_1:M_1\arrow[r]&L_1\\
U_2:M_2\arrow[r,no head]&\unsure{L_2|L_1}
\end{tikzcd}}
```

### 134-QA-deleted-01: deletion, line 28

```latex
\deleted{\unsure{+}}
```

### 134-QA-deleted-02: deletion, line 30

```latex
\deleted{\(\unsure{b_2|b_1}\)}
```

### 134-QA-deleted-03: deletion, line 34

```latex
\deleted{\unsure{étrange}}
```

### 134-QA-diagram-03: diagram, line 40

```latex
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
0\arrow[r,no head]&\mathcal H\arrow[r,no head,"\alpha"]\arrow[d,"-\mathrm{id}"']&\mathcal E\arrow[r,no head,"\psi"]\arrow[d,"\Phi"',"\unsure{R|\sim}"]&\underline O\arrow[r]\arrow[d,equal]&0\\
0\arrow[r,no head]&\mathcal H\arrow[r]\arrow[d,equal]&\operatorname{Hom}^{!}(E,\mathcal H)\arrow[r]&O\arrow[r,no head]&0\\
&\operatorname{Hom}(\underline O,\mathcal H)&&&
\end{tikzcd}}
```

### 134-QA-deleted-04: deletion, line 50

```latex
\deleted{=\unsure{\lambda\operatorname{Hom}|\lambda}\ \mathcal E\longrightarrow\mathcal H}
```

### 134-QA-deleted-05: deletion, line 53

```latex
\deleted{\unsure{qui a le}\ \unsure{val.}}
```

### 134-QA-diagram-04: diagram, line 58

```latex
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&\arrow[r,mapsto]&\deleted{\unsure{\eta}}\\
\zeta_1,\eta_1\arrow[rr]&&\chi\eta_1+b_1(\zeta_1)\\
M_1\otimes M_2\arrow[u]&L_1\otimes L_2\arrow[ul]&
\end{tikzcd}}
```

### 134-QA-deleted-06: deletion, line 59

```latex
\deleted{\unsure{\eta}}
```

## Scan 144

Reclassify existing row `144-29` from its current kind to `drawing`, retaining its other fields, after root confirms it identifies the new grouping arch. This is a proposed one-row update, not an additional duplicate row.

Current row: `{'cote': '84', 'scan': '144', 'sheet_kind': 'text', 'element': '144-29', 'kind': 'display', 'position': 'bottom left', 'first_words_or_objects': 'lambda quotient f; chi f1(x1) tensor f2(u2)', 'transcribed': 'yes'}`

Actual drawing macro at TeX line 5:

```latex
\figure{\begin{tikzpicture}
\node at (0,0) {$E_1\unsure{\wedge|\vee}E_2=$};
\node at (3.7,0) {$E_1\otimes E_2\quad\oplus L_1\otimes L_2$};
\node at (4.9,-.7) {$(E_1\otimes_0 E_2)$};
\draw (3.8,-.55)--(4.4,-.22)--(4.7,-.35)--(5.8,-.4)--(6,-.55);
\end{tikzpicture}}
```

Actual drawing macro at TeX line 57:

```latex
\figure{\begin{tikzpicture}\draw (0,0)--(0,2.5);\end{tikzpicture}}
```

Actual drawing macro at TeX line 79:

```latex
\figure{\begin{tikzpicture}
\node at (0,0) {$\frac{\unsure{\lambda_2|\lambda_1}}{\unsure{\lambda_2}}f$};
\node at (3,0) {$\chi f_1(x_1)\otimes$};
\node at (5.05,0) {$f_2(u_2)$};
\draw (4.4,.38)--(4.44,.62)--(5.57,.62)--(5.65,.40);
\node at (5.05,1.04) {$\deleted{\unsure{\lambda_2}}\lambda_2u_2$};
\end{tikzpicture}}
```
