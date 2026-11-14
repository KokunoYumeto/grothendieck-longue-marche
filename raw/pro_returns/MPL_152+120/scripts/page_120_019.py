from record_page import save_page
save_page(120,19,r'''
\mspage{9}
On voit \inserted{alors} que l'on a la notion d'application $X\longrightarrow Y$ entre espaces modérés, qui est \uline{modérée au voisinage d'un pt}, et on trouve

\uline{Prop} Pour qu'une application d'un espace modéré $X$ dans un espace ind-modéré soit modérée, il \unsure{faut s.} qu'elle le soit au voisinage de chaque pt.

Donc les applications modérées de $X$ dans $Y$ forment les sections d'un faisceau --- le faisceau des applications modérées de $X$ dans $Y$. La structure \inserted{modérée} de $X$ est connue quand on connaît l'ens des applications modérées de $X$ dans $R$ (cela \deleted{\unsure{faut}} dans le contexte purement ensembliste, avec $\unsure{(M1)_0|(M1)}$, $(M2)$ $(M3)$ $(M4)$ seulement), donc aussi quand on connaît le faisceau des germes de fonctions modérées.
\mspage{18}
''',[
('text','top right','9'),('text','upper','On voit que l’on a'),('insertion','above que','alors'),('text','upper middle','Prop Pour qu’une application'),('text','middle','Donc les applications modérées'),('insertion','above de X','modérée'),('deletion','after cela','faut'),('text','bottom left','18')], observations='Local criterion for moderate maps and corresponding sheaf of germs; asserts recovery of the structure from scalar-valued moderate functions, then from their germ sheaf. The handwritten necessary-and-sufficient abbreviation and exact M1 suffix remain uncertain.')
