from record_page import save_page
save_page(120,18,r'''
et ce foncteur est encore fidèle conservatif transportable \inserted{exact à gauche}. \deleted{\unsure{Je trouve}} On a une réciproque quand $R\in\deleted{\unsure{\operatorname{Esp}}}\mathcal M_1$ (donc $R$ cpt) en termes d'un \unsure{un} tel foncteur et d'un objet $R\in\operatorname{Ob}\mathcal E$, tel que $\forall$ objet de $\mathcal E$ se plonge dans un $R^n$.

Tous espaces ind-modérés seront munis de la top. limite inductive. Elle induit sur chaque partie modérée sa topologie propre, quand on suppose que l'espace est ind-dénombrable, i.e. $\varinjlim$ de \uline{suites} croissantes d'espaces modérés.

On voudrait que dans un espace modéré, il y ait pour $\forall$ pt un syst. fond. de voisinages \deleted{de} modérés. Il suffit que \deleted{\unsure{ce}} \inserted{l'analogue} soit vrai dans $R$, donc dans les $R^n$, c'est l'axiome
\[
 (M10)\quad\text{Dans }R,\ \forall\text{ pt a un syst. fond. de voisinages}\in\mathcal M_1.
\]
\mspage{17}
''',[
('text','top','et ce foncteur'),('insertion','above second line','exact à gauche'),('deletion','second line','Je trouve'),('deletion','after R in','Esp'),('text','upper middle','On a une réciproque'),('text','middle','Tous espaces ind-modérés'),('text','lower','On voudrait'),('deletion','after voisinages','de'),('deletion','after que','ce'),('insertion','above soit','l’analogue'),('display','bottom','M10 Dans R'),('text','bottom left','17')], observations='Ind-countability appears explicitly in the statement about the inductive-limit topology inducing the given topology on moderate parts. M10 gives a moderate-neighbourhood basis on R. The manuscript says “On voudrait” before this additional local requirement.')
