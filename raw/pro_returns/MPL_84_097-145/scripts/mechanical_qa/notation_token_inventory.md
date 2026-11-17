# Mechanical notation-token inventory

Created: 2026-11-17 00:12:54 UTC. Page files examined: 48.

This is a source-token snapshot during the principal agent's visual audit. It does not decide whether any sign is correct, does not inspect an image or context, and does not freeze or change any transcription. Snippets reproduce complete source lines exactly. Line numbers may change during later audits.

## Counts

| Category | Matching lines | Matching tokens / characters |
|---|---:|---:|
| Exclamation exponents | 10 | 17 |
| Primes on Hom | 0 | — |
| Primes after square brackets | 2 | 2 |
| All Hom token lines | 9 | — |
| Non-ASCII quotation marks | 0 | — |
| Literal double quotes | 52 | 236 |

52 of 52 literal-double-quote lines contain a `\arrow` command. This is a lexical observation; the snippets below preserve the complete lines for review.

## Command classification

The allowed editorial-state macro set is treated separately from core LaTeX and named package dependencies. Package commands below are not undefined if their listed packages are loaded. `\uline` and `\uuline` are allowed state macros; the optional harness supplies them through `ulem`. The allowed `\figure` command requires overriding LaTeX's existing command in that harness.

| Dependency | Commands currently present |
|---|---|
| amsmath | `\boxed`, `\operatorname`, `\overset`, `\substack`, `\text`, `\underset`, `\xrightarrow` |
| amsfonts/amssymb | `\mathbb`, `\mathfrak` |
| tikz-cd/TikZ | `\arrow`, `\draw`, `\node` |
| mathtools | None |

Unclassified named commands: none.

All named commands were tokenized with escaped backslashes respected; the second backslash of a row break is not mistaken for a new command.


## Exclamation exponents

### MPL_84_097-145_84_scan134.tex, line 42

```latex
0\arrow[r,no head]&\mathcal H\arrow[r]\arrow[d,equal]&\operatorname{Hom}^{!}(E,\mathcal H)\arrow[r]&O\arrow[r,no head]&0\\
```

### MPL_84_097-145_84_scan136.tex, line 4

```latex
\arrow[r,no head]&L\arrow[r]&\operatorname{Hom}^{!}(E,L)\arrow[r,no head]&\underline O\arrow[r,no head]&0
```

### MPL_84_097-145_84_scan144.tex, line 14

```latex
 \unsure{u_i|f_i}\big|_{L_i}=\unsure{u^!_i|f^!_i}:L_i\longrightarrow L_i
```

### MPL_84_097-145_84_scan144.tex, line 20

```latex
 f^!_1\otimes f^!_2&\text{---}&L_1\otimes L_2
```

### MPL_84_097-145_84_scan144.tex, line 27

```latex
 f(u_1\otimes u_2)&=f^!_1(u_1)\otimes f^!_2(u_2)
```

### MPL_84_097-145_84_scan144.tex, line 34

```latex
 &\pi_1(x_1)\otimes u_2\arrow[r,mapsto]&f^!_1(\pi_1(x_1))\otimes f^!_2(u_2)
```

### MPL_84_097-145_84_scan144.tex, line 37

```latex
 f_1(x_1)*v_2=f^!_1(\pi_1(x_1))\otimes v_2
```

### MPL_84_097-145_84_scan144.tex, line 61

```latex
 &L_1\otimes L_2\arrow[uur,"{\deleted{\unsure{\chi f_1\otimes f_2}}\ \unsure{f^!_1f^!_2|f^!_1\otimes f^!_2}}"']&
```

### MPL_84_097-145_84_scan144.tex, line 77

```latex
 \deleted{f_1\otimes f_2}\qquad f_1(\pi_1(\unsure{x^!_1|x'_1}))\otimes f_2(u_2)
```

### MPL_84_097-145_84_scan144.tex, line 87

```latex
 \deleted{\unsure{f_1(f^!_1(x_1)\otimes u_2}\ \unsure{\longrightarrow}}
```


## Primes on Hom

No matches.

## Primes after square brackets

### MPL_84_097-145_84_scan136.tex, line 37

```latex
\bigl([\pi'_1,f'_1]'\otimes U_2\bigr)(x_1\otimes x_2).
```

### MPL_84_097-145_84_scan136.tex, line 43

```latex
\bigl(U_1\otimes[\pi'_2,f'_2]'\bigr)(x_1\otimes x_2)\\
```


## All Hom token lines

### MPL_84_097-145_84_scan097.tex, line 11

```latex
\varphi\otimes\mathrm{id}_L\bigl(\underbrace{g(x)}_{\mathcal A\otimes L=\operatorname{Hom}(E,L)}\bigr)=\psi(x)\qquad \forall x\in\Gamma(E).
```

### MPL_84_097-145_84_scan111.tex, line 18

```latex
d) Des Hom de $k$-algèbres
```

### MPL_84_097-145_84_scan132.tex, line 19

```latex
\operatorname{Hom}(M_i,L_i)\quad
```

### MPL_84_097-145_84_scan132.tex, line 20

```latex
\operatorname{Hom}(M_i,L_i)\quad\operatorname{Hom}(M_i,L_i)
```

### MPL_84_097-145_84_scan132.tex, line 30

```latex
b_1\otimes b_2\in\operatorname{Hom}(M,L)
```

### MPL_84_097-145_84_scan134.tex, line 42

```latex
0\arrow[r,no head]&\mathcal H\arrow[r]\arrow[d,equal]&\operatorname{Hom}^{!}(E,\mathcal H)\arrow[r]&O\arrow[r,no head]&0\\
```

### MPL_84_097-145_84_scan134.tex, line 43

```latex
&\operatorname{Hom}(\underline O,\mathcal H)&&&
```

### MPL_84_097-145_84_scan134.tex, line 50

```latex
\deleted{=\unsure{\lambda\operatorname{Hom}|\lambda}\ \mathcal E\longrightarrow\mathcal H}
```

### MPL_84_097-145_84_scan136.tex, line 4

```latex
\arrow[r,no head]&L\arrow[r]&\operatorname{Hom}^{!}(E,L)\arrow[r,no head]&\underline O\arrow[r,no head]&0
```


## Non-ASCII quotation marks

No matches.

## Literal double quotes

### MPL_84_097-145_84_scan097.tex, line 4

```latex
0 \arrow[r,no head] & L \arrow[r,no head] \arrow[d,"-\mathrm{id}"'] & E \arrow[r,no head] \arrow[d,"g","?"'] & \underline{\mathcal O} \arrow[r] \arrow[d,"\mathrm{id}"] & 0\\
```

### MPL_84_097-145_84_scan097.tex, line 5

```latex
0 \arrow[r,no head] & L \arrow[r,no head] & \mathcal A\otimes L \arrow[r,"\varphi\otimes\mathrm{id}_L"] & \underline{\mathcal O} \arrow[r] & 0
```

### MPL_84_097-145_84_scan098.tex, line 4

```latex
\underline E={} & \underline L \arrow[d,"-\mathrm{id}_L"'] & \oplus & \underline{\mathcal O}.x_0 \arrow[d,no head,"\mathrm{id}"]\\
```

### MPL_84_097-145_84_scan099.tex, line 16

```latex
E_1\otimes E_2 \arrow[dr,"*"] \arrow[rr,bend left=25,"?"] & & E_1\otimes E_2\\
```

### MPL_84_097-145_84_scan099.tex, line 17

```latex
\begin{array}{c}L_1\otimes E_2\oplus E_1\otimes L_2\\E_1*_0E_2\end{array} \arrow[u,hook,"\mathrm{inc}"] \arrow[drr,no head,"\deleted{\unsure{\mathrm{proj}}}"'] & E \arrow[ur,"i"] & \\
```

### MPL_84_097-145_84_scan099.tex, line 18

```latex
& L_1\otimes L_2 \arrow[u,hook,"\mathrm{inj}"] \arrow[uur,bend right=25,"?\ \text{i.e. can.}"'] &
```

### MPL_84_097-145_84_scan099.tex, line 23

```latex
E_1\otimes E_2 \arrow[u,no head,"\unsure{\cap}"] \arrow[ur,dashed,"?"'] &
```

### MPL_84_097-145_84_scan100.tex, line 4

```latex
E_1\otimes E_2 \arrow[r,no head,"x_1\otimes x_2\mapsto x_1*x_2"] \arrow[d,phantom,"\wr"] & E_1\unsure{*|\wedge}E_2=E \arrow[d,phantom,"\wr"]\\
```

### MPL_84_097-145_84_scan101.tex, line 5

```latex
0 \arrow[r] & \overbrace{\mathcal A_1\unsure{\oplus|\amalg}_{\underline{\mathcal O}}\mathcal A_2}^{=\mathcal A_1\otimes_0\mathcal A_2} \arrow[r,no head] \arrow[d,"\tau"'] & \mathcal A_1\otimes\mathcal A_2 \arrow[r] \arrow[d,no head,"\unsure{\uparrow|\downarrow}"] & L_1^\vee\otimes L_2^\vee \arrow[r,no head] \arrow[d,equal] & 0\\
```

### MPL_84_097-145_84_scan110.tex, line 4

```latex
 k\arrow[r,"\deleted{\unsure{\alpha}}\,\alpha"] & A\ (k.\mathrm{alg})\arrow[l,bend left=35,"t"]\arrow[l,bend left=65,"n"]
```

### MPL_84_097-145_84_scan111.tex, line 9

```latex
\diagram{\begin{tikzcd}A_i\arrow[r,shift left=2,"t_i"]\arrow[r,shift right=2,"n_i"']&k\end{tikzcd}}
```

### MPL_84_097-145_84_scan111.tex, line 20

```latex
 A_1\arrow[dr,"\alpha_1"']&A_2\arrow[d,"\alpha_2"]&A_3\arrow[dl,"\alpha_3"]\\
```

### MPL_84_097-145_84_scan111.tex, line 25

```latex
 &A\arrow[dl,shift right=2,"\unsure{T_1}"']\arrow[dl,shift left=2,"N_1"]\arrow[d,shift right=2,"\unsure{T_2}"']\arrow[d,shift left=2,"N_2"]\\
```

### MPL_84_097-145_84_scan111.tex, line 29

```latex
 &A\arrow[dl,shift right=2,"T_1"']\arrow[dl,shift left=2,"N_1"]\arrow[d,shift right=2,"T_2"']\arrow[d,shift left=2,"N_2"]\arrow[dr,shift right=2,"T_3"']\arrow[dr,shift left=2,"N_3"]&\\
```

### MPL_84_097-145_84_scan112.tex, line 4

```latex
A_1 \arrow[r,no head,"\alpha_1"] \arrow[d,no head] & A \arrow[d,no head,"\alpha_2"] \\
```

### MPL_84_097-145_84_scan112.tex, line 16

```latex
A_1\otimes_k A_2 \arrow[r,no head] \arrow[d,"t_1\otimes\mathrm{id}_{A_2}"'] & A \arrow[d,"\unsure{T_1|T_2}"] \\
```

### MPL_84_097-145_84_scan113.tex, line 4

```latex
A_1\otimes_k A_2 \arrow[r] \arrow[d,"{\deleted{\unsure{N}}n_1\otimes_k\mathrm{id}_{A_2}}"',"=N_{12}"] & A \arrow[d,no head,"N_2"] \\
```

### MPL_84_097-145_84_scan118.tex, line 8

```latex
B\arrow[rr,"f"]\arrow[dr]&&A\\
```

### MPL_84_097-145_84_scan121.tex, line 14

```latex
\unsure{\subset}X_1\times_X X_2\times_X X_3\arrow[r,"\pi"]&X_1\wedge X_2\wedge X_3
```

### MPL_84_097-145_84_scan122.tex, line 14

```latex
X_1\times X_2\times X_3\arrow[ur,no head,"(\operatorname{pr}_1,\wedge)"]\arrow[r,no head,"(\operatorname{pr}_2,\wedge)"]\arrow[dr,"(\operatorname{pr}_3,\wedge)"']&X_{2\mathcal X_0}\arrow[r]&\mathcal X_0=\\
```

### MPL_84_097-145_84_scan122.tex, line 27

```latex
B=A_1\otimes_{\mathcal O}A_2\otimes_{\mathcal O}A_3\arrow[r,bend left=65,"\operatorname{Tr}_1"]\arrow[r,bend left=40,"N_1\unsure{?}"]\arrow[r,shift left=1.4ex,"\deleted{\unsure{\operatorname{Tr}_1,N_1}}"]\arrow[r,leftrightarrow,shift right=1.4ex,"2(!)"']&A_1\otimes_{\mathcal O}B_0=B_1\\
```

### MPL_84_097-145_84_scan122.tex, line 28

```latex
B_0\arrow[u,"4(!)","{\text{(\unsure{pas univ. inj.})}}"']\arrow[ur,"2"]&\\
```

### MPL_84_097-145_84_scan122.tex, line 29

```latex
\mathcal O\arrow[u,"2"]\arrow[uu,bend left=40,no head,"8"]&
```

### MPL_84_097-145_84_scan124.tex, line 3

```latex
0\arrow[r]&L\arrow[r]\arrow[d,"\alpha"']&E\arrow[r,no head]\arrow[l,bend right=45,"\pi"']\arrow[d,no head,"\beta"]&M\arrow[r,no head]\arrow[l,bend right=45,"\unsure{\varpi|\overline\omega}"']\arrow[d,no head,"\gamma"]&0\\
```

### MPL_84_097-145_84_scan124.tex, line 4

```latex
0\arrow[r,no head]&L'\arrow[r,no head]&E'\arrow[r,no head]\arrow[l,bend left=45,"\pi'"]&M'\arrow[r,no head]\arrow[l,bend left=45,"\unsure{\varpi'|\overline\omega'}"]&0
```

### MPL_84_097-145_84_scan124.tex, line 21

```latex
&E_1\otimes E_2\arrow[r]&E'_1\otimes\unsure{E'_2}\arrow[dr,"\unsure{*}"]&\\
```

### MPL_84_097-145_84_scan124.tex, line 23

```latex
&L_1\otimes L_2\arrow[r,no head]&L'_1\otimes L'_2\arrow[ur,"\text{inj. can.}"']&
```

### MPL_84_097-145_84_scan126.tex, line 3

```latex
\mathcal E_{(p_1,q_1),(p_2,q_2)}=(M_1\otimes M_2)\oplus(L_1\otimes L_2)\arrow[rr,no head,"T_U"]\arrow[dd,Rightarrow,"T_{-\gamma b}"']&&\mathcal E_{(p'_1,q'_1),(p'_2,q'_2)}\arrow[dd,no head,"T_{-\gamma b'}"]\\
```

### MPL_84_097-145_84_scan126.tex, line 5

```latex
\mathcal E\arrow[rr,"T_{-U}"']&&\mathcal E
```

### MPL_84_097-145_84_scan128.tex, line 29

```latex
\mathcal E_{(p_1,q_1)(p_2,q_2)}\deleted{\unsure{\simeq}}=M_1\otimes M_2\oplus L_1\otimes L_2\arrow[d,leftrightarrow,"\sim"',"T_{v_{(p_1,q_1)(p_2,q_2)}}"]\\
```

### MPL_84_097-145_84_scan128.tex, line 34

```latex
M_1\otimes M_2\arrow[r,no head,"b=b_1b_2"]&L_1\otimes L_2
```

### MPL_84_097-145_84_scan130.tex, line 28

```latex
\mathcal E_{(p_1,p_2)}\deleted{\unsure{\simeq 0}}=(M_1\otimes M_2)\oplus(L_1\otimes L_2)\arrow[r,"\deleted{\unsure{T_{-U}}}","{\Theta_{p,p'}\ \deleted{\unsure{\Theta_{p,p'}}}=T_{-U}}"']&\mathcal E_{p'_1,p'_2}
```

### MPL_84_097-145_84_scan132.tex, line 11

```latex
& E_1\vee E_2\arrow[dl,"\Theta_{p_1,p_2}"',"\sim"]\arrow[d,no head,"\Theta_{p'_1,p'_2}"',"\sim"]\arrow[dr,"\Theta_{p''_1,\unsure{p''_3|p''_2}}","\sim"'] &\\
```

### MPL_84_097-145_84_scan132.tex, line 12

```latex
M\oplus L\arrow[r,"\substack{(U_1,U_2,U)\\\Theta_{(p_1,p_2)(p'_1,p'_2)}\\\sim}"]\arrow[rr,bend right=25,"\substack{U''_1,U''_2,U''\\\Theta_{(p_1,p_2)(p''_1,p''_2)}}"'] & M\oplus L\arrow[r,"\substack{(U'_1,U'_2,U')\\\Theta_{(p'_1,p'_2)(p''_1,\unsure{p''_3|p''_2})}\\\sim}"] & M\oplus L
```

### MPL_84_097-145_84_scan134.tex, line 3

```latex
& E_1\unsure{\wedge|\vee}E_2\arrow[dl,very thick,"\Theta_{p_1*p_2}"']\arrow[dr,"\Theta_{p'_1*p'_2}=\Theta_{p_1*p_2}\unsure{-|+}U"] &\\
```

### MPL_84_097-145_84_scan134.tex, line 41

```latex
0\arrow[r,no head]&\mathcal H\arrow[r,no head,"\alpha"]\arrow[d,"-\mathrm{id}"']&\mathcal E\arrow[r,no head,"\psi"]\arrow[d,"\Phi"',"\unsure{R|\sim}"]&\underline O\arrow[r]\arrow[d,equal]&0\\
```

### MPL_84_097-145_84_scan136.tex, line 3

```latex
0\arrow[r]&L\arrow[r,no head]\arrow[d,"-\mathrm{id}_L"']&E\arrow[r,"\psi"]\arrow[d,"\sim"]&\underline O\arrow[r]\arrow[d,equal]&0\\
```

### MPL_84_097-145_84_scan136.tex, line 10

```latex
\diagram{\begin{tikzcd}E\arrow[r,"\psi(x)"']&L\end{tikzcd}}
```

### MPL_84_097-145_84_scan140.tex, line 3

```latex
M_1\arrow[d,bend left=35,no head,"q_1"]\\
```

### MPL_84_097-145_84_scan140.tex, line 4

```latex
E_1\arrow[d,"\alpha_1"']\arrow[d,bend left=35,no head,"p_1"]\\L_1
```

### MPL_84_097-145_84_scan140.tex, line 8

```latex
(E_1\otimes L_2)\oplus(L_1\otimes E_2)\arrow[r]\arrow[dr,"\unsure{\pi|\alpha}"']&
```

### MPL_84_097-145_84_scan140.tex, line 9

```latex
\underset{x_1\otimes x_2}{E_1\otimes E_2}\arrow[dr,"\unsure{\lambda_1|\lambda}"]&
```

### MPL_84_097-145_84_scan140.tex, line 12

```latex
\underset{x_1*x_2}{E}\arrow[r]\arrow[ul,phantom,"\text{comm.}"]\arrow[l,bend left=35,"p"]\arrow[u,bend right=35,"\deleted{\unsure{q}}"]&
```

### MPL_84_097-145_84_scan140.tex, line 13

```latex
\underset{m_1\otimes m_2}{M_1\otimes M_2}\arrow[l,bend left=35,"q"]
```

### MPL_84_097-145_84_scan142.tex, line 15

```latex
 E_1\otimes_0\uline{E_2}\arrow[r,hook,"\mu"]\arrow[dr,dashed,no head,"\pi"']&
```

### MPL_84_097-145_84_scan142.tex, line 16

```latex
 E_1\otimes E_2\arrow[r,"F_{11}"]&E_1\otimes E_2\\
```

### MPL_84_097-145_84_scan142.tex, line 17

```latex
 &L_1\otimes L_2\arrow[ur,dashed,leftrightarrow,"\alpha_1\otimes\alpha_2"']&
```

### MPL_84_097-145_84_scan142.tex, line 22

```latex
 E_1\otimes E_2\arrow[r,"F_{11}"]\arrow[dr,"\psi_1\otimes\psi_2"']&
```

### MPL_84_097-145_84_scan142.tex, line 23

```latex
 E_1\otimes E_2\arrow[r,"\nu"]&\deleted{\unsure{E_1}}E_1\otimes^0 E_2\\
```

### MPL_84_097-145_84_scan142.tex, line 24

```latex
 &M_1\otimes M_2\arrow[ur,"\omega"']&
```

### MPL_84_097-145_84_scan144.tex, line 53

```latex
 E_1\arrow[d,"f_1"']&E_2\arrow[d,"f_2"]\\
```

### MPL_84_097-145_84_scan144.tex, line 61

```latex
 &L_1\otimes L_2\arrow[uur,"{\deleted{\unsure{\chi f_1\otimes f_2}}\ \unsure{f^!_1f^!_2|f^!_1\otimes f^!_2}}"']&
```

