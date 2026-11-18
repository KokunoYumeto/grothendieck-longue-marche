from save_page import save_page

save_page(130, r'''
\scanpage{130}
\mspage{6}
% archive foliation: 129
pour ton théorème une formulation plus naturelle (qui devrait \deleted{\unsure{en}} fournir une démonstration uniforme, sans distinction du cas $\ell\ne p$ et $\ell=p$), de même qu'on voit en même temps que ta somme abracadabrante se comporte bien quand on fait varier $X$ dans une famille, i.e si $X$ est \deleted{en fait un} un schéma abélien sur $Y$ (car alors les ${}_nX$ seront d'excellents schémas en groupes finis et plats sur $Y$, dont on peut prendre formellement la limite projective\ldots).

J'espère \unsure{arriver-dans|arriver dans} l'année prochaine à une théorie satisfaisante du groupe fondamental, \deleted{\unsure{ce qui}} et achever la rédaction des Chapitres IV,V,VI,VII (ce dernier étant le groupe fondamental), en même temps que des catégories. Dans deux ans résidus, dualité, intersections, Chern, Riemann-Roch. Dans trois ans cohomologie de Weil, et un peu d'homotopie si Dieu veut. Et entre-temps, je ne sais quand, le grand théorème d'existence avec Picard etc, un peu de courbes algébriques, \inserted{les schémas abéliens.} Sauf difficultés imprévues ou enlisement, le multiplodoque devrait être fini d'ici 3 ans, ou 4 au maximum. On pourra commencer à faire de la géométrie algébrique !

Bien à toi
''', [
('text','first paragraph continuation','pour ton théorème une formulation plus naturelle'),
('deletion','end of first line after devrait','en'),
('deletion','after si X est','en fait un'),
('text','second paragraph','J’espère arriver-dans l’année prochaine'),
('deletion','after groupe fondamental','ce qui'),
('insertion','after courbes algébriques','les schémas abéliens.'),
('text','closing','Bien à toi'),
], [
('first line cancelled word','en','two overtyped letters','medium'),
('after J’espère','arriver-dans','thin oblique stroke may be incidental rather than a hyphen','low'),
('second paragraph cancelled words','ce qui','x-overtyping but q descender visible','low'),
('near end','multiplodoque','typed word clearly ends doque; retained rather than normalized','high'),
], [
'Continuation expects a uniform formulation across ℓ≠p and ℓ=p and good variation for an abelian scheme via finite flat torsion kernels; this is presented as an anticipated benefit, not a proof.',
'The letter closes with a schedule for the fundamental group, Chapters IV–VII, categories, residues/duality/intersections/Chern/Riemann–Roch, Weil cohomology and homotopy, existence/Picard, curves and abelian schemes. “J’espère” and “Sauf difficultés imprévues ou enlisement” explicitly mark expectation; no date or signature is visible on this sheet.',
], sheet_kind='typed')
