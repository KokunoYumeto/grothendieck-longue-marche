# Annotation/inventory reconciliation — source-only review

This report quotes the current LaTeX and existing inventory metadata. It makes no claims about unseen ink. Counts are reconciled through explicit grouped labels or nested wrapper structure. No deliverable was changed.

## Items needing the reader’s decision

- Scan 155, source line 48: the second deleted diagram object has no separately identifying inventory row; deletion element 25 may be intended to cover both objects.
- Scan 162, source lines 47–48: three deleted arguments are literal `1`; grouped element 25 describes “twice and a prime.”
- Scan 155 upper array and scan 157 arrow-bearing product block have display rows but no corresponding diagram-kind rows.

## Exact evidence by scan

### Scan 144

The two-count difference is accounted for by two existing grouped deletion rows. Element 20 explicitly names both `hom dans C_k` and `B`; element 33 explicitly names both `u_i:M` and `est loc. finie`. Each of these rows corresponds textually to two separate deleted arguments. No additional fragment is left unaccounted for by this count comparison.

Source `144:deleted:6`, TeX line 20:

```latex
\deleted{hom dans $C_k$}
```

Source `144:deleted:7`, TeX line 20:

```latex
\deleted{\unsure{B}}
```

Source `144:deleted:9`, TeX line 47:

```latex
\deleted{$\unsure{u_i:M}$}
```

Source `144:deleted:10`, TeX line 47:

```latex
\deleted{\unsure{est} ``loc. finie''}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 46, scan/element 144/20:

```csv
136,144,text,20,deletion,within correspond,hom dans C_k; B,yes
```

CSV row 59, scan/element 144/33:

```csv
136,144,text,33,deletion,above family formula,u_i:M; est loc. finie,yes
```

### Scan 146

The first margin wrapper contains a figure. Element 13 records that figure as a drawing; element 19 records the numeric margin. The extra margin wrapper thus has an existing drawing entry.

Source `146:margin:1`, TeX line 20:

```latex
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0.05,-1.2);\draw (0.12,0.05)--(0.17,-1.15);\end{tikzpicture}}}
```

Source `146:margin:2`, TeX line 34:

```latex
\margin{145}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 102, scan/element 146/13:

```csv
136,146,text,13,drawing,left margin beside limits sentence,two vertical emphasis strokes,yes
```

CSV row 108, scan/element 146/19:

```csv
136,146,text,19,margin note,bottom left,145,yes
```

### Scan 155

The upper array has existing display entries 3 and 4; its diagram-wrapper count therefore exceeds the number of rows classified as diagram. At the bottom, element 25 names the first of the two deleted objects on source line 48. No separate row explicitly names the second deleted object, `\operatorname{Hom}_k(s^k,C\otimes k)`. The existing first-words field may label the whole cancelled row, so the intended grouping needs the sole visual reader to decide.

Source `155:diagram:1`, TeX line 5–11:

```latex
\diagram{\[
\begin{array}{rclll}
C\otimes_k k^{(I)}&\longrightarrow&(C\otimes_k k)^I=&C^I&\text{est-il injectif ?}\\
&&&\text{\textquotedbl}&\\
&&&\operatorname{Hom}(k^{(I)},C).&
\end{array}
\]}
```

Source `155:deleted:2`, TeX line 48:

```latex
\deleted{C\otimes_k\underbrace{\operatorname{Hom}_k(s^k,k)}_{(s^k)^k}}
```

Source `155:deleted:3`, TeX line 48:

```latex
\deleted{\operatorname{Hom}_k(s^k,C\otimes k)}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 290, scan/element 155/3:

```csv
136,155,text,3,display,upper,C tensor k^{(I)},yes
```

CSV row 291, scan/element 155/4:

```csv
136,155,text,4,display,upper,C^I=Hom,yes
```

CSV row 304, scan/element 155/17:

```csv
136,155,text,17,deletion,lower left,NB,yes
```

CSV row 311, scan/element 155/24:

```csv
136,155,text,24,diagram,bottom,C → C tensor s subset Hom,yes
```

CSV row 312, scan/element 155/25:

```csv
136,155,text,25,deletion,bottom,"C tensor Hom_k(s^k,k)",yes
```

### Scan 157

The diagram starts with the expression identified by display element 17 (`s^k=prod`). Element 22 records another product expression and is included for disambiguation. There is existing display coverage of these expressions, while no row is classified as diagram. The source fragment below identifies the exact arrow-bearing block for metadata reconciliation.

Source `157:diagram:1`, TeX line 29–31:

```latex
\diagram{\begin{tikzcd}
s^k=\displaystyle\prod_{n\in D}s_n^k\arrow[r,phantom,"=" description]\arrow[r,bend right=35,"\mathrm{dfn}"'] & \displaystyle\prod_{n\in D}(s^k)_n.
\end{tikzcd}}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 345, scan/element 157/17:

```csv
136,157,text,17,display,lower,s^k=prod,yes
```

CSV row 350, scan/element 157/22:

```csv
136,157,text,22,display,lower,s^k=prod(s^k)_n,yes
```

### Scan 158

The first margin wrapper contains a figure recorded by drawing element 15. The other three margin wrappers have the three numeric margin-note entries 16–18. The extra margin wrapper therefore has existing drawing coverage.

Source `158:margin:1`, TeX line 24:

```latex
\margin{\figure{\begin{tikzpicture}\draw (0,.1)--(.45,.1) (.35,.28)--(.38,0);\draw (.85,.18)--(.9,0);\draw (5.5,0)--(5.6,.17)--(5.7,0);\end{tikzpicture}}}
```

Source `158:margin:2`, TeX line 25:

```latex
\margin{429}
```

Source `158:margin:3`, TeX line 26:

```latex
\margin{429}
```

Source `158:margin:4`, TeX line 27:

```latex
\margin{157}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 372, scan/element 158/15:

```csv
136,158,reused_typed,15,drawing,bottom strip,faint pencil strokes,yes
```

CSV row 373, scan/element 158/16:

```csv
136,158,reused_typed,16,margin note,bottom strip,429,yes
```

CSV row 374, scan/element 158/17:

```csv
136,158,reused_typed,17,margin note,bottom label,429,yes
```

CSV row 375, scan/element 158/18:

```csv
136,158,reused_typed,18,margin note,bottom left,157,yes
```

### Scan 162

The title inside the first margin wrapper is represented by text element 1 and drawing element 2. The remaining three margins have margin-note entries 29, 33 and 34. Three deleted arguments on source lines 47–48 all contain `1`; grouped deletion element 25 says `index 1 on A prime twice and a prime`. That grouped row accounts for the count difference structurally, but its wording and the three literal arguments require the reader’s reconciliation.

Source `162:margin:1`, TeX line 2:

```latex
\margin{\figure{\begin{tikzpicture}\node[align=center,anchor=south west] at (0,0) {Opérations sur complexes de De Rham\\à p.d.};\draw (0,1)--(0,0)--(8,0);\end{tikzpicture}}}
```

Source `162:deleted:7`, TeX line 47:

```latex
\deleted{1}
```

Source `162:deleted:8`, TeX line 48:

```latex
\deleted{1}
```

Source `162:deleted:9`, TeX line 48:

```latex
\deleted{1}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 405, scan/element 162/1:

```csv
136,162,text,1,text,top right,Opérations sur complexes de De Rham,yes
```

CSV row 406, scan/element 162/2:

```csv
136,162,text,2,drawing,top right,title border,yes
```

CSV row 429, scan/element 162/25:

```csv
136,162,text,25,deletion,lower condition 2,index 1 on A prime twice and a prime,yes
```

CSV row 433, scan/element 162/29:

```csv
136,162,text,29,margin note,bottom left rotated,NB dans la suite supprimer,yes
```

CSV row 437, scan/element 162/33:

```csv
136,162,text,33,margin note,bottom right,TSVP,yes
```

CSV row 438, scan/element 162/34:

```csv
136,162,text,34,margin note,bottom left,161,yes
```

### Scan 168

All four extra deletion occurrences have existing grouped or differently classified coverage: the outer deleted formula is display element 3, whose first-words field explicitly says deleted; its nested alpha deletion is element 4. Element 23 explicitly lists the three deleted arguments at source line 40, accounting for two extra occurrences. Element 26 explicitly says twice and accounts for the two arguments at source line 47, accounting for one extra occurrence.

Source `168:deleted:2`, TeX line 4:

```latex
\deleted{\varphi_0(T)=\sum_{i\geq1}\deleted{\unsure{\alpha_i}}\gamma'_iT^{(i)}\qquad(\gamma'_i\in k',\ i\geq1)}
```

Source `168:deleted:7`, TeX line 40:

```latex
\deleted{1}
```

Source `168:deleted:8`, TeX line 40:

```latex
\deleted{\unsure{S'}}
```

Source `168:deleted:9`, TeX line 40:

```latex
\deleted{++}
```

Source `168:deleted:10`, TeX line 47:

```latex
\deleted{1}
```

Source `168:deleted:11`, TeX line 47:

```latex
\deleted{1}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 555, scan/element 168/3:

```csv
136,168,text,3,display,top,deleted phi_0(T)=sum gamma prime_i,yes
```

CSV row 556, scan/element 168/4:

```csv
136,168,text,4,deletion,top formula,alpha_i,yes
```

CSV row 575, scan/element 168/23:

```csv
136,168,text,23,deletion,lower system,index 1 and S prime and ++,yes
```

CSV row 578, scan/element 168/26:

```csv
136,168,text,26,deletion,lower conditions,index 1 on A prime twice,yes
```

### Scan 184

The first margin wrapper contains only a deleted formula. Deletion element 6 records that formula and its marginal position. The other two margins have entries 12 and 34. The extra margin-wrapper count therefore has existing deletion coverage.

Source `184:margin:1`, TeX line 19:

```latex
\margin{\deleted{$\unsure{(d\xi_1)^2=0}$}}
```

Existing inventory rows (CSV row numbers shown separately; fields otherwise reproduced exactly):

CSV row 834, scan/element 184/6:

```csv
136,184,text,6,deletion,upper right pencil,(d xi_1)^2=0 uncertain,yes
```

CSV row 840, scan/element 184/12:

```csv
136,184,text,12,margin note,middle left pencil,On aura phi_1(d(...)) ?= d phi_1(...),yes
```

CSV row 862, scan/element 184/34:

```csv
136,184,text,34,margin note,bottom left,183,yes
```
