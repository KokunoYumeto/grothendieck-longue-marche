"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(126,
    "\\scanpage{126}\n\\mspage{2}\n% archive foliation: 125\n de schémas en groupes finis et plats sur $S$\n\\diagram{\\begin{tikzcd}[column sep=small]\ne \\arrow[r] & H_{\\mathrm{inf}} \\arrow[r] & H \\arrow[r] & H_{\\text{sép}} \\arrow[r] & e\n\\end{tikzcd}}\noù $H_{\\mathrm{inf}}$ est purement infinitésimal (i.e. la projection $H_{\\mathrm{inf}}\\to S$ est géométriquement injectif) et où $H_{\\text{sép}}$ est non ramifié sur $S$. (Dans le cas d'un corps de base $k$, une telle suite exacte est déduite d'une suite exacte analogue pour un groupe algébrique fini \\inserted{$G$} sur $k$; d'ailleurs si $k$ est parfait, cette suite splitte canoniquement, car $G_{\\text{réd}}$ est \\inserted{alors} un sous-groupe de $G$, isomorphe à $G_{\\text{sép}}$ par la projection $G\\quad G_{\\text{sép}}$. Faire attention cependant que $G_{\\text{réd}}$ va opérer sur $G_{\\mathrm{inf}}$, on aura seulement un produit semi-direct). Enfin\n\n\\deleted{La condition (v) \\unsure{est essentiellement provisoire}.}\n\n(vi) $S$ est réduit.\n\nLes conditions (v) et (vi) ont une sale gueule, et sont essentiellement provisoires. Elles servent à \\deleted{\\unsure{justifier la vérité}} \\inserted{\\unsure{cause}} du\n\n\\uline{Lemme}. Soit $H$ comme dans (v), $S$ comme dans (vi), $P$ un fibré principal homogène sous $H$, $Q$ un autre, $u,v$ deux isomorphismes de $P$ dans $Q$ transformant un \\inserted{``}point \\deleted{\\unsure{géométrique}} \\inserted{marqué''} donné en un autre donné, alors $u=v$. (On est ramené, en tordant $H$, au cas où $P$ est trivial, et alors cela résulte du fait suivant: une section de $Q$ est un isomorphisme de $S$ sur une composante connexe de $Q_{\\text{réd}}$).\n\nRemarque néanmoins que les conditions (i) à (vi) n'excluent pas des groupes structuraux tordus (relativement à un corps de base $k$).\n\nSoit maintenant $a$ un ``point marqué'' de $S$ (i.e. une extension algébriquement close du corps résiduel d'un $s\\in S$). Pour tout $G\\in\\underline G$, on désigne par $Z(S,a;G)$ ou simplement $Z(G)$ l'ensemble des classes (à isomorphisme près) de fibrés principaux homogènes sur $S$, de groupe $F(G)$, munis d'un point marqué au dessus de $a$. Evidemment $Z(G)$ est un foncteur de $\\underline G$ dans la catégorie des ensembles. Ce foncteur satisfait aux conditions suivantes: 1) Il commute aux produits (\\deleted{trivial) \\unsure{et}} car $F$ y commute) 2) il commute aux noyaux de couples, en d'autres termes si\n\\diagram{\\begin{tikzcd}[column sep=small]\nG'' \\arrow[r] & G \\arrow[r,shift left=.6ex] \\arrow[r,shift right=.6ex] & G'\n\\end{tikzcd}}\nest exact dans $\\underline G$, alors\n\\diagram{\\begin{tikzcd}[column sep=small]\nZ(G'') \\arrow[r] & Z(G) \\arrow[r,shift left=.6ex] \\arrow[r,shift right=.6ex] & Z(G')\n\\end{tikzcd}}\nest exacte, i.e. $Z(G'')$ s'identifie à l'ensemble des éléments de $Z(G)$ dont l'image dans $Z(G')$ par $Z(u)$ et $Z(v)$ est la même. (Ceci résulte de l'exactitude de $F$, et du lemme).\n\\figure{\\begin{tikzpicture}[scale=.4]\n\\draw[line width=.6pt] (0,.1)--(.08,.32)--(.22,.35)--(.4,.53)--(.13,.42)--(.04,.3)--(.1,-.1)--(.21,-.22)--(.41,-.14)--(.23,-.3)--(.12,-.1)--(-.03,.17)--(.22,.23);\n\\end{tikzpicture}}\n",
    elements=[['text', 'top continuation', 'de schémas en groupes finis et plats'],
 ['diagram', 'top exact sequence', 'e → H_inf → H → H_sép → e'],
 ['text', 'first paragraph', 'où H_inf est purement infinitésimal'],
 ['insertion', 'after groupe algébrique fini', 'G'],
 ['insertion', 'after G_réd est', 'alors'],
 ['deletion', 'above vi', 'La condition (v) … provisoire'],
 ['text', 'condition vi', 'S est réduit'],
 ['text', 'provisionality paragraph', 'Les conditions (v) et (vi)'],
 ['deletion', 'after servent à', 'justifier la vérité'],
 ['insertion', 'over deleted phrase', 'cause'],
 ['text', 'lemma', 'Soit H comme dans (v)'],
 ['insertion', 'before point', 'opening double quote'],
 ['deletion', 'after point', 'géométrique'],
 ['insertion', 'above deleted word', 'marqué and closing double quote'],
 ['text', 'remark after lemma', 'Remarque néanmoins'],
 ['text', 'final paragraph', 'Soit maintenant a un point marqué'],
 ['deletion', 'after produits', 'trivial) et'],
 ['diagram', 'final paragraph first sequence', 'G″ → G ⇉ G′'],
 ['diagram', 'final paragraph second sequence', 'Z(G″) → Z(G) ⇉ Z(G′)'],
 ['drawing', 'bottom near centre', 'short angular ink strokes']],
    doubts=[['cancelled sentence above vi',
  'est essentiellement provisoire',
  'x-overtyping obscures most of the cancelled sentence',
  'low'],
 ['before Lemme',
  'justifier la vérité; cause',
  'first phrase heavily crossed; inserted word looks like cause despite awkward wording',
  'low'],
 ['lemma point', 'cancelled géométrique', 'x-overtyping largely conceals the old word', 'low'],
 ['after produits',
  'trivial) et',
  'several overtyped x marks; et itself may be cancelled original matter',
  'medium'],
 ['projection G to G_sép', 'G [blank] G_sép', 'no arrow visible; not supplied', 'high'],
 ['bottom mark', 'drawn angular ink mark', 'not securely a letter; reproduced as strokes', 'low']],
    leads=['The author calls hypotheses (v) and (vi) “une sale gueule” and “essentiellement provisoires”; '
 'the lemma asserts uniqueness of pointed torsor isomorphisms under those hypotheses and sketches '
 'reduction by twisting.',
 'Products and equalizers are asserted to be preserved by the pointed-torsor class functor Z, the '
 'latter by exactness of F and the rigidity lemma. Full earlier assumptions lie on an excluded '
 'page and must be recovered only after freezing.',
 'The warning about G_réd acting on G_inf explicitly permits only a semidirect product, not a '
 'direct product; compare later fundamental-group constructions.'],
    sheet_kind='typed',
)
