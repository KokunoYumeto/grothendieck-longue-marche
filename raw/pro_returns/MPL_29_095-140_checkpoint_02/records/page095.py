"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(95,
    '\\cotefile{29}\n\\scanpage{95}\n% Image orientation: the typescript is upside down in the supplied scan.\n% archive foliation: 94\ntera donc du a) dans le\n\n\\uline{Corollaire} 3.2. Soit\\inserted{\\unsure{en}} $S$ un préschéma non vide, $u:M\'\\quad M$ un homomorphisme de groupes commutatifs ordinaires, $u\':G\\quad G\'$ l\'homomorphisme transposé. Alors :\n% Blank connector positions in this carbon typescript are retained as spaces.\n\na) Pour que $u$ soit un monomorphisme, il f et s que $u\'$ soit fidèlement plat.\n\nb) Pour que $u$ soit un épimorphisme, il f et s que $u\'$ soit un monomorphisme (et alors $u\'$ est même une immersion fermée).\n\nPour prouver a), on note que si $u$ est un monomorphisme, alors $\\underline{O}_S(M)$ est un Module \\deleted{\\unsure{libre sur}}\\inserted{sur} $\\underline{O}_S(M\')$, \\deleted{\\unsure{tout système de représentants}} admettant une base non vide (savoir, le système de sections défini par n\'importe quel système de représentants dans $M$ modulo $M\'$), à fortiori il est fidèlement plat. Réciproquement, s\'il en est ainsi, alors $\\underline{O}_S(M\')\\quad\\underline{O}_S(M)$ est injectif, ce qui (pour $S\\ne\\varnothing$) implique que $u:M\'\\quad M$ est injectif.\n\nPour prouver b), on note que si $u$ est un épimorphisme, alors $\\underline{O}_S(M\')\\quad\\underline{O}_S(M)$ est surjectif, donc $u\'$ est une immersion fermée et à fortiori un monomorphisme. Inversement, s\'il en est ainsi, alors $\\operatorname{Ker}u\'={}$ groupe unité, or \\deleted{\\unsure{posant}} posant $M\'\'=\\operatorname{Coker}u$, on a vu que $\\operatorname{Ker}u\'\\quad D_S(M\'\')$, donc par 2.1. d) on a $M\'\'=0$ donc $u$ est un épimorphisme.\n\nOn conclut de 3.1. de la façon habituelle:\n\n\\uline{Corollaire} 3.3. Soit\n\\diagram{\\begin{tikzcd}[column sep=small]\nM\' \\arrow[r,phantom,"u"] & M \\arrow[r,phantom,"v"] & M\'\'\n\\end{tikzcd}}\nune suite exacte de groupes commutatifs ordinaires, considérons la suite transposée\n\\diagram{\\begin{tikzcd}[column sep=small]\nG\'\' \\arrow[r,phantom,"v\'"] & G \\arrow[r,phantom,"u\'"] & G\'.\n\\end{tikzcd}}\nAlors $v\'$ induit un morphisme fidèlement plat et quasi-compact de $G\'\'$ dans $\\operatorname{Ker}u\'$, et ce dernier est un groupe diagonalisable.\n',
    elements=[['text', 'top, continuation fragment', 'tera donc du a) dans le'],
 ['text', 'upper, Corollaire 3.2 statement', 'Soit S un préschéma non vide'],
 ['insertion', 'above Soit', 'en'],
 ['text', 'upper-middle, a)', 'Pour que u soit un monomorphisme'],
 ['text', 'upper-middle, b)', 'Pour que u soit un épimorphisme'],
 ['text', 'middle, proof a)', 'Pour prouver a)'],
 ['deletion', 'middle, after Module', 'libre sur'],
 ['insertion', 'middle, above deleted libre sur', 'sur'],
 ['deletion', "middle, after O_S(M')", 'tout système de représentants'],
 ['text', 'lower-middle, proof b)', 'Pour prouver b)'],
 ['deletion', 'lower-middle, after or', 'posant'],
 ['text', 'lower, transition', 'On conclut de 3.1.'],
 ['text', 'lower, Corollaire 3.3', 'Soit; une suite exacte de groupes'],
 ['diagram', 'lower, inline sequence', "M' u M v M''"],
 ['diagram', 'bottom, transposed sequence', "G'' v' G u' G'"],
 ['text', 'bottom, conclusion', "Alors v' induit un morphisme"]],
    doubts=[['above Soit in Cor. 3.2', 'en', 'Misplaced typed correction; attachment unclear', 'low'],
 ['all blank mathematical connectors',
  'Visible gaps retained as spaces / phantom arrows',
  'No connector strokes can be read; no direction supplied',
  'low'],
 ['proof a), first deletion', 'libre sur', 'libre; overtyping conceals the last strokes', 'medium'],
 ['proof a), second deletion', 'tout système de représentants', 'Overtyped letters', 'medium'],
 ['proof b), deletion', 'posant', 'pesant', 'medium'],
 ['Cor. 3.3 last sentence',
  "de G'' dans Ker u'",
  'The printed double prime is retained despite mathematical tension',
  'high']],
    leads=['Cor. 3.2 gives mono/faithfully-flat and epi/closed-immersion correspondences for the transposed '
 'diagonalizable group morphism. The carbon copy has blank connector positions.',
 "Cor. 3.3 says v' induces a faithfully flat quasi-compact morphism de G'' dans Ker u'. Retain "
 'this visible wording; compare direction only in research notes.'],
    sheet_kind='reused_typed',
)
