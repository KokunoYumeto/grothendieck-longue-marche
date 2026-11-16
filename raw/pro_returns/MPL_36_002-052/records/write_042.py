from save_page import save
tex=r'''
\scanpage{42}
\deleted{\diagram{\begin{tikzcd}[column sep=large,row sep=large]
f^{-1}(U)\arrow[r,hook,"i"]\arrow[d,"f"']&X\arrow[d,"f"]\\
U\arrow[r,"j"']\arrow[ur,"g"]\arrow[ur,bend left=12,"\deleted{\unsure{g}}"',no head]&Y
\end{tikzcd}}}
\deleted{\[gf=i\qquad fg=j\]}
\deleted{$f$ morphisme birationnel \inserted{propre} de préschémas intègres $X,Y$

$U$ ouvert de $Y$ sur lequel $f^{-1}$ est défini

[Si $Y$ est régulier en codim 1, alors $U$ est le complémentaire d'un ens de codim $\geq2$], \deleted{\unsure{i.e. aussi le fait}} \unsure{i.e.} \unsure{aussi le} $\unsure{\forall}$ \unsure{que} un \unsure{voisinage} $V$ \unsure{tel} que $f$ induise un isom $f^{-1}(U)\longrightarrow V$.

Soit $\xi\in\operatorname{Pic}(X)$ défini par un \deleted{\unsure{cycle}} \uline{diviseur} $D$ (\unsure{X connexe}) considérons \deleted{\unsure{un}} \deleted{le morphisme} $g^{-1}(\xi)\in\operatorname{Pic}(U)$, il correspond à \deleted{\unsure{un}} cycle divisoriel}
\margin{41}
'''
e=[('deletion','whole written draft, after rotation','two oblique cancellation strokes through the draft'),('diagram','upper left after rotation','f⁻¹(U) ↪ X / U → Y'),('deletion','diagonal in diagram','overwritten diagonal label g'),('display','under diagram','gf=i; fg=j'),('text','first line after rotation','f morphisme birationnel'),('insertion','above first line','propre'),('text','second paragraph','U ouvert de Y'),('text','bracketed paragraph','Si Y est régulier en codim 1'),('deletion','after closing bracket','i.e. aussi le fait'),('text','continuation after bracket','i.e. aussi le ... voisinage V'),('text','last paragraph','Soit ξ∈Pic(X)'),('deletion','above diviseur','cycle'),('deletion','before g⁻¹(ξ)','un; le morphisme'),('deletion','last line before cycle','un'),('margin note','physical bottom left','41')]
d=[{'line':'bracketed paragraph after codim ≥2','reading':'i.e. aussi le fait (deleted); i.e. aussi le ∀ que un voisinage V','alternatives':'compressed phrase and quantifier-like sign unresolved; each reading is marked in place','confidence':'low'},{'line':'last paragraph, after D','reading':'X connexe','alternatives':'X ...; adjective uncertain','confidence':'low'},{'line':'last paragraph insertion/deletion','reading':'cycle','alternatives':'short crossed word above diviseur','confidence':'low'},{'line':'diagram diagonal','reading':'g, with an earlier crossed g/diagonal','alternatives':'earlier label obscured','confidence':'low'}]
save(42,tex,e,d,'Cancelled draft on a proper birational morphism of integral preschemes, the open where the inverse is defined, and divisor classes. Entire draft crossed through by two long oblique strokes, so the surviving assertions are not silently promoted to live claims. The phrase after codimension ≥2 is especially compressed; the quantifier-like sign and the adjective after D are low-confidence readings. The draft ends after “cycle divisoriel”, with no completion.',sheet_kind='cancelled_draft')
