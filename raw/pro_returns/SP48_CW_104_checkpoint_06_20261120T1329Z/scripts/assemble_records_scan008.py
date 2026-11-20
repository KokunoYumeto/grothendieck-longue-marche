"""Text-only reader crosswalk and staged records for scan 008.

This assembler reads only current-page text, reports, crop metadata and main
observations. It never opens an image, decides ink, writes the selected page,
writes decision.json, compiles, renders, or rebuilds cumulative deliverables.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import copy
import difflib
import hashlib
import json
import re

O = Path(__file__).resolve().parents[1]
P = O / "records/scan008"
PACKET = O.parent / "reader_inputs/scan008"

# These are main-only choices. Empty entries remain pending; a reader majority
# or source issue's confidence never supplies a main decision.
MAIN_NUMBERS = {
    "opening":1,"definition":2,"J_definition":3,"ens_definition":3,
    "sous_objet":4,"on_a_pour":5,"canonique":5,"quantifier":5,
    "J_type_arrow":6,"type_caption":6,"formee":7,"deleted_des_1":7,
    "ens_image":8,"deleted_I_des":9,"point_after_des":9,
    "chaque":10,"J_notons":10,"Dn_quote":11,"en_tant":12,"inserted_le":12,
    "naming_cluster":13,"par_ii":14,"cancelled_Si_J":15,"cancelled_Si_stop":15,
    "upper_old_x":16,"Soient_J":16,"Soient_cancelled_on":17,"avec_insertion":17,
    "considerons":18,"via_group":18,"on_a_alors_application":18,
    "first_Hom_old_D":19,"first_Hom_plain_D":19,"first_map_J":19,"first_map_layout":19,
    "ens_bijection":20,"second_Hom_old_D":21,"second_Hom_superscript":21,
    "second_Hom_brackets":22,"detached_pair":23,"cancelled_bijec":24,
    "def_unaccented":25,"lower_J":26,"lower_J_cancelled_group":26,
    "rho_lower":27,"lower_Hom":27,"vertical_relation":28,"lower_Hom_annotation":28,
    "ens_des_annotation":29,"ou_mapping":30,"xi_layout":30,"no_ou_before_plus":31,
    "commutativite":32,"no_de_after_commutativite":33,"final_J_pair":34,
    "rho_final":34,"final_Hom":34,"final_J":34,"inclusion_curve":34,
    "REG_N_tau":5,"REG_inverse_xi":30,
}
def spec(final,confidence,diff_C,diff_H,kind,unresolved=False,alternatives="",**extra):
    return {"final":final,"confidence":confidence,"diff_C":diff_C,"diff_H":diff_H,
            "kind":kind,"unresolved":unresolved,**({"alternatives":alternatives} if alternatives else {}),**extra}

SPECS = {
    "opening":spec("De plus, se rappelant","high",False,True,"misread word"),
    "definition":spec("definition","high",True,True,"abbreviation expanded or spelling modernised"),
    "J_definition":spec(r"J_n","high",False,True,"misread symbol or index"),
    "ens_definition":spec("ens; no abbreviation stop","high",False,True,"abbreviation expanded or spelling modernised"),
    "sous_objet":spec("sous-objet","high",True,True,"misread word"),
    "on_a_pour":spec("on a, pour","high",False,True,"misread word"),
    "canonique":spec("une application canonique, strictement croissante","high",False,True,"misread word"),
    "quantifier":spec(r"\unsure{\mathrm{H}|\forall}","medium",True,True,"misread symbol or index",True,
                      r"Roman H-like sign | \forall; separated lower legs do not settle a universal sign"),
    "J_type_arrow":spec(r"J_n\xrightarrow{\tau_n}\mathbb N","high",False,True,"misread symbol or index"),
    "type_caption":spec(r"\tau_n, application ``type; no enclosing parentheses or closing ticks","high",False,True,"text not on the page"),
    "formee":spec("formée","high",True,True,"misread word"),
    "deleted_des_1":spec(r"\deleted{des}","high",False,True,"misread word"),
    "ens_image":spec("l'ens; no abbreviation stop","high",False,True,"abbreviation expanded or spelling modernised"),
    "deleted_I_des":spec(r"\deleted{\(I_{\leq n}\) des}","high",False,True,"deletion state"),
    "point_after_des":spec("Separate literal ink point after canceled des and before live N; no punctuation function assigned","high",True,True,"drawing or diagram"),
    "chaque":spec("chaque","high",False,True,"misread word"),
    "J_notons":spec(r"J_n","high",False,True,"misread symbol or index"),
    "Dn_quote":spec(r"``\(D_n\); opening ticks only","high",False,True,"text not on the page"),
    "en_tant":spec("(en tant que","medium",True,True,"misread word"),
    "inserted_le":spec(r"\inserted{le}","high",False,True,"insertion or placement"),
    "naming_cluster":spec(r"\unsure{que je|qu'\deleted{est}on|qu'\deleted{il}on|qu'\deleted{est}on y|qu'\deleted{il}on y}",
        "low",True,True,"deletion state",True,
        "Live que je preferred; canceled est or il followed by on, with or without y; cancellation history unresolved"),
    "par_ii":spec(r"\inserted{(par (ii))}","high",False,True,"insertion or placement"),
    "cancelled_Si_J":spec(r"\deleted{Si \(n'\leq n\), alors pour tout \(x\in J_n\)}; J alphabet","high",False,True,"misread symbol or index"),
    "cancelled_Si_stop":spec("No terminal full stop in the canceled Si sentence","high",True,False,"text not on the page"),
    "REG_N_tau":spec(r"\mathbb N with returning barred uprights; \tau_n above the type arrow and in its side caption",
        "high",False,False,"notation check",main_observations=[5,6]),
    "upper_old_x":spec(r"\deleted{\(\unsure{x\in J|x\in}\)}","low",False,True,"omission",True,
        r"x\in J | x\in; the upper final contour overlaps the separate lower J"),
    "Soient_J":spec(r"\deleted{\(x\in J_n,\ \ldots\)}; plain J","high",False,True,"misread symbol or index"),
    "Soient_cancelled_on":spec(r"\deleted{\(n'=\tau_n(x)\), on}; on is within the cancellation","high",False,True,"deletion state"),
    "avec_insertion":spec(r"\inserted{avec \(n'\leq n\)}; no terminal comma","high",False,True,"insertion or placement"),
    "considerons":spec("considérons; one live occurrence","medium",True,True,"deletion state"),
    "via_group":spec(r"\deleted{\unsure{via \(x\)|via \((x)\)}}","medium",True,True,r"readable ink left as \ill{}",True,
        r"via x | via (x); parenthetic status remains uncertain, l'in excluded"),
    "on_a_alors_application":spec(r"\deleted{on a alors \unsure{une|un} application}","low",False,True,"deletion state",True,
        "une | un inside the one canceled application line"),
    "first_Hom_old_D":spec(r"\deleted{\unsure{O|D}}D_{n'}","low",False,True,"omission",True,"Old O | D beneath the separate live D"),
    "first_Hom_plain_D":spec(r"D_n","high",True,False,"misread symbol or index"),
    "first_map_J":spec(r"\widetilde D_n=J_n","high",False,True,"misread symbol or index"),
    "first_map_layout":spec("Two rows; lower maps-to tail starts slightly right of upper hook start and its arrowhead extends slightly beyond the upper head; lower u under the upper-left neighborhood; no comma after upper target",
        "high",True,True,"drawing or diagram"),
    "ens_bijection":spec("l'ens; no abbreviation stop","high",False,True,"abbreviation expanded or spelling modernised"),
    "second_Hom_old_D":spec(r"\deleted{\unsure{D|O}}D_{n'}","low",False,True,"omission",True,"Old D | O beneath the live first-argument D"),
    "second_Hom_superscript":spec(r"D_{n'}^{\unsure{4|\ast}}","medium",True,True,"misread symbol or index",True,
        r"4 preferred | angular \ast; distinct ordinary n-prime below"),
    "second_Hom_brackets":spec(r"Two separate shallow square-ended brackets below \widetilde D_{n'} and \widetilde D_n, with plain J_{n'} and J_n beneath",
        "high",False,True,"drawing or diagram"),
    "detached_pair":spec("Two detached ink points, upper to the right of lower, without assigned function","high",True,True,"drawing or diagram"),
    "cancelled_bijec":spec(r"\deleted{bijec}","medium",True,True,r"readable ink left as \ill{}"),
    "def_unaccented":spec("def; unaccented label above equality","high",False,True,"abbreviation expanded or spelling modernised"),
    "lower_J":spec(r"J_{n',n}; both indices live","high",False,True,"misread symbol or index"),
    "lower_J_cancelled_group":spec(r"\deleted{\unsure{(n')|(n)}}","low",False,True,"misread symbol or index",True,
        "Canceled parenthetic (n-prime) | (n), separately above/right of live indices"),
    "rho_lower":spec(r"\rho_{n,n'}","high",False,True,"misread symbol or index"),
    "lower_Hom":spec(r"\mathrm{Hom}(J_{n'},J_n)","high",False,True,"misread symbol or index"),
    "vertical_relation":spec("Literal bent-left/near-straight-right vertical strokes with upper-left point, enclosed in an in-place uncertainty; interpretation rotated simeq preferred over rotated equals",
        "medium",True,True,"drawing or diagram",True,
        r"\simeq rotated 90 degrees | = rotated 90 degrees; literal trace retained in the body"),
    "lower_Hom_annotation":spec(r"Tall square brackets enclose BOTH the literal relation/point and \mathrm{Hom}(D_{n'},D_n) below it, all under the left inverse image",
        "high",True,True,"insertion or placement"),
    "ens_des_annotation":spec(r"Shallow square-ended bracket over four lines: ens des / éléments / de J_n de / type n'",
        "high",False,True,"misread word"),
    "ou_mapping":spec("ou; no accent","high",True,True,"misread word"),
    "xi_layout":spec(r"Separate lower row: ou \xi\longmapsto u_\xi^n; no comma after upper Hom",
        "high",False,True,"insertion or placement",main_observations=[27,30]),
    "no_ou_before_plus":spec("qui est injective, plus précisément; no added ou","high",False,True,"text not on the page"),
    "commutativite":spec(r"\unsure{commutativité|commutativite}","medium",False,True,"abbreviation expanded or spelling modernised",True,
        "commutativité | commutativite; terminal e and faint high mark do not settle accent"),
    "no_de_after_commutativite":spec("No de after the final commutativity word","high",False,True,"text not on the page"),
    "final_J_pair":spec(r"J_{n,n'}","high",False,True,"misread symbol or index",
        consequential="The final first object has n,n-prime, whereas the preceding definition has n-prime,n. Both manuscript orders remain literal; the source-confirmed type discrepancy is recorded in the existing main check metadata."),
    "rho_final":spec(r"\rho_{n,n'}","high",False,True,"misread symbol or index"),
    "final_Hom":spec(r"\mathrm{Hom}(J_{n'},J_n)","high",False,True,"misread symbol or index"),
    "final_J":spec(r"J_n","high",False,True,"misread symbol or index"),
    "inclusion_curve":spec("Headless lower curve with inward left curl open to the right; both ends detached; right end below-left of final J; inclusion centered above low middle",
        "high",True,True,"drawing or diagram"),
    "REG_inverse_xi":spec(r"Reader registers retain -1 and local primes; main confirms \xi and u_\xi^n and the two distinct J index orders",
        "high",False,False,"notation check",main_observations=[19,26,30,34]),
}
MATH_SOURCE_CONFIRMED = True
MATH_SOURCE_CONFIRMATION = (
    "Main source confirmation, 2026-11-20 13:00:18 UTC: all three complete scan008 returns and main observations 3, 5, 6, 9, 10, 19, 26, 27, 28, 30 and 34. "
    "Main26 confirms J_{n-prime,n}; main34 confirms J_{n,n-prime}. Both orders are retained. This is ink confirmation, not a new mathematical proof event. "
    "The five original events are imported unchanged, including their historically conditional/pending outcomes."
)
MATH_SOURCE_OBSERVATIONS = {
    "008-SCOPE":[3,5,6,9,10,19,26,27,28,30,34],
    "008-TYPE":[3,5,6,9,10],"008-HOM-FIBER":[19],
    "008-RHO":[19,26,27,28,30,34],"008-INDEX-TYPE":[26,34],
}
EXPECTED_SELECTED_PAGE_SHA256 = "63f3250d9f44125fe8c275d4e9df9d9a5612384c3b7555b45f7615a9c83f6f31"
PAGE_REQUIRED = {
    "root-reviewed uncertainty and layout choices":[
        r"\unsure{\mathrm{H}|\forall}",
        r"\unsure{que je|qu'\deleted{est}on|qu'\deleted{il}on|qu'\deleted{est}on y|qu'\deleted{il}on y}",
        r"u&\mkern2mu\longmapsto u(d_{n'})",
        r"\underset{\left[\begin{gathered}",
        r"\unsure{\tikz[x=1em,y=1em,baseline=0pt]",
        r"\end{gathered}\right]}{\tau_n^{-1}(n')}",
        r"J_{n',n}\deleted{\unsure{(n')|(n)}}",
        r"J_{n,n'} \arrow[r," ,
        r"[xshift=.15em,yshift=-1em]",
        r"[xshift=-1em,yshift=-.75em]",
    ],
}
INVENTORY_REQUIRED = {
    "E01":["De plus, se rappelant la definition de"],
    "E02":[r"J_n=\widetilde D_n=\text{ens des sous-objet de }D_n"],
    "E03":[r"on a, pour \(\unsure{\mathrm{H}|\forall} n\in\mathbb N\), une application canonique, strictement croissante"],
    "E04":[r"J_n\xrightarrow{\tau_n}\mathbb N"],
    "E05":[r"\text{\(\tau_n\), application ``type}"],
    "E06":[r"dont l'image est formée \deleted{des} de l'ens"],
    "E07":[r"formée \deleted{des}"],
    "E08":[r"\deleted{\(I_{\leq n}\) des}"],
    "E09":[r"\(\mathbb N_{\leq n}=\{n'\in\mathbb N\mid n'\leq n\}\)."],
    "E10":[r"Notons que chaque \(J_n\)",r"\unsure{que je|qu'\deleted{est}on|qu'\deleted{il}on|qu'\deleted{est}on y|qu'\deleted{il}on y} note \(d_n\). On a donc"],
    "E11":[r"\inserted{le} sous-objet"],
    "E12":[r"On a donc \inserted{(par (ii))}"],
    "E13":[r"\tau_n^{-1}(n)=\{d_n\}"],
    "E14":[r"\deleted{Si \(n'\leq n\), alors pour tout \(x\in J_n\)}"],
    "E15":[r"Soient \(n,n'\in\mathbb N\),"],
    "E16":[r"\deleted{\(\unsure{x\in J|x\in}\)}"],
    "E17":[r"\inserted{avec \(n'\leq n\)}"],
    "E18":[r"\deleted{\(x\in J_n,\ n'=\tau_n(x)\), on}"],
    "E19":[r"considérons \deleted{\unsure{via"],
    "E20":[r"\deleted{\unsure{via \(x\)|via \((x)\)}}"],
    "E21":[r"\deleted{on a alors \unsure{une|un} application}"],
    "E22":[r"\mathrm{Hom}(\deleted{\unsure{O|D}}D_{n'},D_n)&\hookrightarrow \widetilde D_n=J_n",r"u&\mkern2mu\longmapsto u(d_{n'})"],
    "E23":[r"\deleted{\unsure{O|D}}D_{n'}"],
    "E24":[r"qui est une bijection des \(\mathrm{Hom}\) sur l'ens \(\tau_n^{-1}(n')\), et considérons"],
    "E25":[r"\mathrm{Hom}(\deleted{\unsure{D|O}}D_{n'}^{\unsure{4|\ast}},D_n)"],
    "E26":[r"\deleted{\unsure{D|O}}D_{n'}"],
    "E27":[r"\draw(0,.08)--(0,0)--(.60,0)--(.60,.08);",r"\draw(0,.08)--(0,0)--(.54,0)--(.54,.08);"],
    "E28":[r"\\ J_{n'}}}{\widetilde D_{n'}}",r"\\J_n}}{\widetilde D_n}"],
    "E29":[r"on en déduit une \deleted{bijec} application"],
    "E30":[r"\deleted{bijec}"],
    "E31":[r"\tau_n^{-1}(n')",r"\overset{\mathrm{def}}{=}",r"\xrightarrow{\rho_{n,n'}}\mathrm{Hom}(J_{n'},J_n)"],
    "E32":[r"J_{n',n}\deleted{\unsure{(n')|(n)}}"],
    "E33":[r"\draw(0,.07)--(0,0)--(.86,0)--(.86,.07);"],
    "E34":[r"\unsure{\tikz[x=1em,y=1em,baseline=0pt]",r"\draw[line width=.35pt] (.43,.59)--(.43,.08);",r"\fill (0,.61) circle (.025);"],
    "E35":[r"\underset{\left[\begin{gathered}",r"\mathrm{Hom}(D_{n'},D_n)",r"\end{gathered}\right]}{\tau_n^{-1}(n')}"],
    "E36":[r"\text{ens des}\\\text{éléments}\\\text{de \(J_n\) de}\\\text{type \(n'\)}"],
    "E37":[r"\text{ou}\quad \xi\longmapsto u_{\xi}^{n}"],
    "E38":[r"qui est injective, plus précisément on a la \unsure{commutativité|commutativite}"],
    "E39":[r"J_{n,n'} \arrow[r,",r'''\arrow[r,"u\mapsto u(d_{n'})"]''',r"\& J_n"],
    "E40":["% archive sheet number: 7"],
    "E41":[r"\tikz[baseline=.2ex]{\fill (0,0) circle (.025);}"],
    "E42":[r"\raisebox{-3.5ex}{\tikz{\fill (0,.12) ellipse (.025 and .018);\fill (-.07,0) circle (.022);}}"],
}

# Fine source locations follow B's report; overlapping naming/article rows are
# consolidated. The two points are C-only additions. REG rows are noncounted.
# Each tuple: key, reader-A issue numbers, reader-B issue numbers, reader-C ids.
LOCUS_SOURCES = [
    ("opening", [1], [1], ["opening"]),
    ("definition", [2], [2], ["definition"]),
    ("J_definition", [3], [3], ["J_definition"]),
    ("ens_definition", [4], [4], ["ens_definition"]),
    ("sous_objet", [5], [5], ["sous_objet"]),
    ("on_a_pour", [6], [6], ["on_a_pour"]),
    ("canonique", [6], [7], ["canonique"]),
    ("quantifier", [6], [59], ["N_tau_prime_register"]),
    ("J_type_arrow", [7], [8], ["J_type_arrow"]),
    ("type_caption", [8], [9], ["type_caption"]),
    ("formee", [9], [10], ["formee"]),
    ("deleted_des_1", [10], [11], ["deleted_des_1"]),
    ("ens_image", [11], [12], ["ens_image"]),
    ("deleted_I_des", [12], [13], ["deleted_I_des"]),
    ("point_after_des", [], [], ["point_after_des"]),
    ("chaque", [13], [14], ["chaque_J"]),
    ("J_notons", [13], [15], ["chaque_J"]),
    ("Dn_quote", [14], [16], ["Dn_quote"]),
    ("en_tant", [15], [17], ["en_tant"]),
    ("inserted_le", [16], [18], ["inserted_le"]),
    ("naming_cluster", [17], [19,20], ["que_je_or_rewrite"]),
    ("par_ii", [18], [21], ["par_ii"]),
    ("cancelled_Si_J", [19], [22], ["cancelled_Si"]),
    ("cancelled_Si_stop", [19], [23], ["cancelled_Si"]),
    ("upper_old_x", [20], [24], ["upper_old_x"]),
    ("Soient_J", [21], [25], ["Soient_cancelled_line"]),
    ("Soient_cancelled_on", [21], [26], ["Soient_cancelled_line"]),
    ("avec_insertion", [21], [27], ["avec_insertion"]),
    ("considerons", [22], [28], ["considerons"]),
    ("via_group", [23], [29], ["via_group"]),
    ("on_a_alors_application", [24], [30,31], ["on_a_alors_application"]),
    ("first_Hom_old_D", [25], [32], ["first_Hom_old_D"]),
    ("first_Hom_plain_D", [26], [33], ["first_Hom_plain_D"]),
    ("first_map_J", [27], [34], ["first_map_layout"]),
    ("first_map_layout", [27], [35], ["first_map_layout"]),
    ("ens_bijection", [28], [36], ["ens_bijection"]),
    ("second_Hom_old_D", [29], [37], ["second_Hom_old_D"]),
    ("second_Hom_superscript", [30], [38], ["second_Hom_superscript"]),
    ("second_Hom_brackets", [31], [39], ["second_Hom_brackets"]),
    ("detached_pair", [], [], ["detached_pair"]),
    ("cancelled_bijec", [32], [40], ["cancelled_bijec"]),
    ("def_unaccented", [33], [41], ["def_unaccented"]),
    ("lower_J", [34], [42], ["lower_J_and_cancel"]),
    ("lower_J_cancelled_group", [35], [43], ["lower_J_and_cancel"]),
    ("rho_lower", [36], [44], ["rho_lower"]),
    ("lower_Hom", [37], [45], []),
    ("vertical_relation", [38], [46], ["vertical_relation_and_enclosure"]),
    ("lower_Hom_annotation", [39], [47], ["vertical_relation_and_enclosure"]),
    ("ens_des_annotation", [40], [48], ["ens_des_annotation"]),
    ("ou_mapping", [41], [49], ["ou_mapping"]),
    ("xi_layout", [], [50], ["xi_register"]),
    ("no_ou_before_plus", [42], [51], ["no_ou_before_plus"]),
    ("commutativite", [43], [52], ["commutativite"]),
    ("no_de_after_commutativite", [44], [53], ["no_de_after_commutativite"]),
    ("final_J_pair", [45], [54], ["final_diagram_letters"]),
    ("rho_final", [46], [55], ["final_diagram_letters"]),
    ("final_Hom", [45], [56], ["final_diagram_letters"]),
    ("final_J", [45], [57], ["final_diagram_letters"]),
    ("inclusion_curve", [47], [58], ["inclusion_curve"]),
    ("REG_N_tau", [], [59], ["N_tau_prime_register"]),
    ("REG_inverse_xi", [], [60], ["N_tau_prime_register", "xi_register"]),
]

C_DOUBT_KEYS = [
    "definition","sous_objet","formee","en_tant","naming_cluster",
    "naming_cluster","upper_old_x","considerons","via_group",
    "on_a_alors_application","first_Hom_old_D","first_Hom_plain_D",
    "second_Hom_old_D","second_Hom_superscript","cancelled_bijec",
    "lower_J_cancelled_group","ou_mapping","commutativite",
]
H_DOUBT_KEYS = [
    ["opening"],["opening"],["chaque"],["en_tant"],
    ["via_group"],["cancelled_bijec"],
]

# Local strings separate the content of broad source reports. Original exact
# reports and complete reading.tex files are preserved without editing below.
LOCAL_READINGS = {
    "on_a_pour":dict.fromkeys("ABC","on a, pour"),
    "canonique":dict.fromkeys("ABC","une application canonique, strictement croissante"),
    "quantifier":dict.fromkeys("ABC",r"\forall"),
    "chaque":dict.fromkeys("ABC","chaque"),
    "J_notons":dict.fromkeys("ABC",r"J_n"),
    "en_tant":dict.fromkeys("ABC","(en tant que"),
    "naming_cluster":{
        "A":"que je",
        "B":r"\unsure{que je|qu'\deleted{est}on|qu'\deleted{il}on y}",
        "C":r"\unsure{que je|qu'\deleted{est}on|qu'\deleted{il}on|qu'\deleted{est}on y|qu'\deleted{il}on y}",
    },
    "cancelled_Si_J":dict.fromkeys("ABC",r"x\in J_n"),
    "cancelled_Si_stop":dict.fromkeys("ABC","No terminal full stop after the canceled J_n"),
    "Soient_J":dict.fromkeys("ABC",r"x\in J_n"),
    "Soient_cancelled_on":dict.fromkeys("ABC",r"\deleted{..., on}"),
    "avec_insertion":dict.fromkeys("ABC",r"\inserted{avec \(n'\leq n\)}"),
    "via_group":{
        "A":r"\deleted{\unsure{via \(x\)|via \((x)\)}}",
        "B":r"\deleted{\unsure{via \((x)\)|via \(x\)}}",
        "C":r"\deleted{\unsure{via \(x\)|via \((x)\)}}",
    },
    "on_a_alors_application":dict.fromkeys("ABC",r"\deleted{on a alors \unsure{une|un} application}"),
    "first_map_J":dict.fromkeys("ABC",r"\widetilde D_n=J_n"),
    "first_map_layout":dict.fromkeys("ABC","Two rows: hook arrow above mapsto; no comma after upper J_n"),
    "lower_J":dict.fromkeys("ABC",r"J_{n',n}; both indices live"),
    "lower_J_cancelled_group":dict.fromkeys("ABC",r"\deleted{\unsure{(n')|(n)}}"),
    "lower_Hom":dict.fromkeys("ABC",r"\mathrm{Hom}(J_{n'},J_n)"),
    "lower_Hom_annotation":{
        "A":r"[\mathrm{Hom}(D_{n'},D_n)] below the left inverse image; relation above the bracketed Hom",
        "B":r"[\mathrm{Hom}(D_{n'},D_n)] below the left inverse image; relation above the bracketed Hom",
        "C":r"Tall square brackets enclose both the vertical relation and \mathrm{Hom}(D_{n'},D_n), below the left inverse image",
    },
    "xi_layout":dict.fromkeys("ABC",r"ou \xi\longmapsto u_\xi^n on a separate lower row; no comma after upper Hom"),
    "final_J_pair":dict.fromkeys("ABC",r"J_{n,n'}"),
    "rho_final":dict.fromkeys("ABC",r"\rho_{n,n'}"),
    "final_Hom":dict.fromkeys("ABC",r"\mathrm{Hom}(J_{n'},J_n)"),
    "final_J":dict.fromkeys("ABC",r"J_n"),
    "REG_N_tau":dict.fromkeys("ABC",r"\forall n\in\mathbb N; \tau_n; local J/D/D-tilde forms checked"),
    "REG_inverse_xi":dict.fromkeys("ABC",r"-1, n', \xi, u_\xi^n; separate paired-index orders checked"),
    "point_after_des":{
        "A":"No detached-point trace in returned reading.tex",
        "B":"No detached-point trace in returned reading.tex",
        "C":r"\tikz[baseline=-.2ex]{\fill (0,0) circle (.025);}",
    },
    "detached_pair":{
        "A":"No detached-pair trace in returned reading.tex",
        "B":"No detached-pair trace in returned reading.tex",
        "C":r"\quad\raisebox{-3.5ex}{\tikz{\fill (0,.12) ellipse (.025 and .018);\fill (-.07,0) circle (.022);}}",
    },
    "inclusion_curve":{
        "A":"Open curl with detached endpoints; changes C's start to xshift=.15em,yshift=-1em and end to xshift=-1em,yshift=-.75em",
        "B":"Retains witness C's complete existing TikZ path, including its endpoint placements; no head",
        "C":"Retains witness C's complete existing TikZ path, including its endpoint placements; no head",
    },
}
LOCAL_C_DIFF = {
    "cancelled_Si_J":dict.fromkeys("ABC",False),
    "cancelled_Si_stop":dict.fromkeys("ABC",True),
    "lower_Hom_annotation":{"A":False,"B":False,"C":True},
    "point_after_des":{"A":False,"B":False,"C":True},
    "detached_pair":{"A":False,"B":False,"C":True},
    "inclusion_curve":{"A":True,"B":False,"C":False},
}

def load_inputs():
    reports, readings, logs, metadata = {}, {}, {}, {}
    for a in "ABC":
        q = P / f"reader_{a}"
        reports[a] = json.loads((q/"report.json").read_text())
        assert reports[a].get("finished_utc"), f"Reader {a} report incomplete"
        readings[a] = (q/"reading.tex").read_text()
        logs[a] = (q/"read_log.md").read_text()
        assert logs[a].strip(), f"Reader {a} log incomplete"
        assert r"\scanpage{8}" in readings[a] and "% archive sheet number: 7" in readings[a]
        metadata[a] = json.loads((q/"crop_metadata.json").read_text())
    issues = {a:{x["id"]:x for x in reports[a]["issues"]} for a in "ABC"}
    witnesses = {a:(PACKET/f"{a}.tex").read_text() for a in "CH"}
    doubts = json.loads((P/"witness_doubts.json").read_text())
    context = (PACKET/"C_context.md").read_text()
    assert {a:len(issues[a]) for a in "ABC"} == {"A":47,"B":60,"C":49}
    assert len(doubts["C"]) == 18 and len(doubts["H"]) == 6
    return reports, readings, logs, metadata, issues, witnesses, doubts, context

def snapshot(path):
    b = path.read_bytes()
    return {"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}

def relpath(value, reader=None):
    p = Path(value)
    if p.is_absolute():
        return str(p.relative_to(O))
    s = str(p)
    if s.startswith(O.name+"/"):
        return str(p.relative_to(O.name))
    if reader and not s.startswith(("records/", "crops/scan")):
        return f"records/scan008/reader_{reader}/{s}"
    return s

def get_main():
    mp = P/"main_observations.md"
    text = mp.read_text() if mp.exists() else ""
    obs = {int(n):re.split(r"\n\nDelivery note\b",body)[0].strip() for n,body in re.findall(
        r"^([0-9]+)\. (.*?)(?=\n[0-9]+\. |\Z)",text,re.M|re.S)}
    pp = P/"main_crop_plan.json"
    plan_list = json.loads(pp.read_text()) if pp.exists() else []
    return text, obs, plan_list, {x["number"]:x for x in plan_list}

def build_inventory(reports):
    bmap = {
        1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:9,9:8,10:10,11:11,12:12,
        13:14,14:15,15:18,16:16,17:17,18:19,19:20,20:21,21:22,22:23,
        23:24,24:25,25:26,26:27,27:26,28:26,29:28,30:29,31:30,32:31,
        33:32,34:33,35:33,36:32,37:34,38:35,39:36,40:37,
    }
    cmap = {
        1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:11,11:12,12:13,
        13:15,14:16,15:19,16:18,17:17,18:20,19:21,20:22,21:23,22:24,
        23:25,24:26,25:27,26:28,27:27,28:27,29:31,30:30,31:32,32:33,
        33:32,34:32,35:32,36:32,37:32,38:34,39:35,40:36,
    }
    rows = []
    for n,item in enumerate(reports["A"]["inventory"],1):
        row = copy.deepcopy(item)
        row.update(element=f"E{n:02d}: {item['element']}",transcribed="pending",
                   source_inventory_rows={"A":[n],"B":[bmap[n]],"C":[cmap[n]]})
        rows.append(row)
    for ci,label in [(10,"detached point after old set"),(29,"detached pair after second Hom")]:
        row = copy.deepcopy(reports["C"]["inventory"][ci-1])
        row.update(element=f"E{len(rows)+1:02d}: {label}",transcribed="pending",
                   source_inventory_rows={"A":[],"B":[],"C":[ci]},
                   coverage_note="Only reader C separately reports and draws this candidate mark group; main adjudication pending.")
        rows.append(row)
    naming = SPECS.get("naming_cluster",{})
    if naming:
        rows[9]["source_inventory_rows"]["B"].append(13)
        rows[9]["source_inventory_rows"]["C"].append(14)
        rows[9]["first_words_or_objects"] = "Notons que chaque J_n ... et [uncertain naming/correction cluster] note d_n. On a donc"
        rows[9]["coverage_note"] = "Main inventories the naming cluster once inside this text paragraph, with cancellation status uncertain. B13/C14's correction-status candidates are covered here; no definite additional deletion is inventoried."
    else:
        row = copy.deepcopy(reports["B"]["inventory"][12])
        row.update(element="E43: naming-cluster correction-status candidate",transcribed="pending",
                   source_inventory_rows={"A":[10],"B":[13],"C":[14]},
                   coverage_note="A includes this text in its paragraph and denies a separate deletion; B/C separately inventory uncertain correction status. Main determines the selected classification; this is not an extra omitted passage count.")
        rows.append(row)
    for row in rows:
        row["reader_inventory"] = {
            a:[copy.deepcopy(reports[a]["inventory"][n-1]) for n in row["source_inventory_rows"][a]]
            for a in "ABC"}
    for a in "ABC":
        covered = {n for row in rows for n in row["source_inventory_rows"][a]}
        assert covered == set(range(1,len(reports[a]["inventory"])+1)), (a,covered)
    byid={row["element"].split(":",1)[0]:row for row in rows}
    byid["E03"]["first_words_or_objects"] = r"on a, pour \unsure{\mathrm{H}|\forall} n in doubled N, une application canonique, strictement croissante"
    byid["E34"]["first_words_or_objects"] = "Uncertain literal bent-left/straight-right relation with upper-left point, inside the tall enclosure"
    byid["E35"]["first_words_or_objects"] = "Tall square enclosure containing BOTH relation and Hom(D_n-prime,D_n), beneath the inverse image"
    byid["E40"].update(kind="text",hand="unattributed archival hand",first_words_or_objects="7 (archive sheet number)")
    ordered=[]
    for n in range(1,41):
        ordered.append(byid[f"E{n:02d}"])
        if n==8:ordered.append(byid["E41"])
        if n==28:ordered.append(byid["E42"])
    if "E43" in byid:ordered.insert(11,byid["E43"])
    for n,row in enumerate(ordered,1):row["physical_order"]=n
    rows=ordered
    return rows

def build_crosswalk(data):
    reports, readings, logs, metadata, issues, witnesses, doubts, context = data
    _, main, plan_list, plan = get_main()
    rows = []
    for key,an,bn,cn in LOCUS_SOURCES:
        refs = {"A":[f"a{n:02d}" for n in an],"B":[f"B{n:03d}" for n in bn],"C":cn}
        for a in "ABC":
            assert all(k in issues[a] for k in refs[a]), (key,a,refs[a])
        primary = issues["B"][refs["B"][0]] if bn else issues["C"][cn[0]]
        local = LOCAL_READINGS.get(key,{
            a:"; ".join(issues[a][k]["reading"] for k in refs[a]) for a in "ABC"})
        role = "context_register" if key.startswith("REG_") else "physical_locus"
        number = MAIN_NUMBERS.get(key)
        rows.append({
            "id":f"008L{len(rows)+1:02d}","key":key,"location":primary["location"],
            "witness_C":primary["C"],"witness_H":primary["H"],
            "readers":copy.deepcopy(local),"source_issues":refs,"role":role,
            "countable":role=="physical_locus","notes":[],"C_doubts":[],
            "main_plan_number":number,
            "planned_main_crop":plan[number]["path"] if number in plan else "",
            "main_adjudication_status":("main observation recorded; decision staged"
                if key in SPECS and number in main else "pending; text assembler makes no ink choice"),
            "reader_return_differs_from_C":LOCAL_C_DIFF.get(key,{
                a:any(issues[a][k].get("diff_C") for k in refs[a]) for a in "ABC"}),
            "reader_report_readings":{
                a:[{"id":k,"reading":issues[a][k]["reading"]} for k in refs[a]] for a in "ABC"},
            "reported_bboxes":{
                a:[{"id":k,"bbox":issues[a][k].get("bbox",[])} for k in refs[a]] for a in "ABC"},
            "reader_crop_options":[],
        })
    bykey = {x["key"]:x for x in rows}
    bykey["naming_cluster"]["notes"].extend([
        "B019 and B020 cover the same physical naming/rewrite cluster; count it once. C05 and C06 are linked doubts, not two changed places.",
        "The final reader C report and complete reading both retain all five alternatives. An earlier report had four; root compared the updated five-alternative return before main crops.",
    ])
    bykey["naming_cluster"]["witness_C"] = r"qu'\deleted{\unsure{est|il}}\unsure{on|on y}"
    bykey["first_map_layout"]["witness_C"] = r"Two aligned rows at the same & column: upper &\hookrightarrow and lower u&\longmapsto, with shared shaft origin and no lower \mkern displacement; no comma after the upper target"
    bykey["inclusion_curve"]["witness_C"] = r"Open headless curl starting ([xshift=.25em,yshift=-.15em]\tikzcdmatrixname-1-1.south east), finishing directly at \tikzcdmatrixname-1-3.south west (last node corner); higher prior left endpoint and no detached right gap"
    bykey["on_a_alors_application"]["notes"].append(
        "B030 is the broad cancellation and B031 its internal une/un doubt; one physical canceled-phrase locus, without an additional omitted-passage count.")
    bykey["on_a_alors_application"]["notes"].append(
        "Actual H.tex has live l'application here. Its preceding ill mark belongs to the canceled via cluster; A/C's marked_in_H=yes at this whole old line is not adopted.")
    bykey["quantifier"].update(location="Sign before n in the canonical-application sentence",
        witness_C=r"\forall",witness_H=r"\forall")
    bykey["quantifier"]["notes"].append(
        "Root's main observation 5 introduces a new local H-like/forall doubt against all three readers and both witnesses. This is a separate physical sign, not an inference from formula syntax.")
    bykey["canonique"]["notes"].append(
        "Reader C's H paraphrase adds a fictitious comma after croissante. Actual H.tex has no such comma; the only compared word change is croissante to canonique.")
    bykey["J_notons"]["notes"].append(
        "H's I_n is unmarked. Broad A13/C chaque_J source issues also include the preceding uncertain déjà, whose H mark belongs only to the separate chaque row.")
    bykey["en_tant"].update(witness_C=r"(\unsure{en tant|en} que",
        witness_H=r"(au sens \uncertain{que c'est}")
    bykey["inserted_le"].update(witness_H="un (unmarked live article)")
    bykey["inserted_le"]["notes"].append(
        "H's un is unmarked; its adjacent uncertain que c'est belongs to the parenthetic-wording row. A16's broader marked_in_H=yes does not apply to this localized article.")
    bykey["lower_Hom"]["notes"].append(
        "Reader C has no standalone report issue for Hom(J,J) versus H's Hom(I,I); its complete reading.tex and Rho arrow and element map log row explicitly supply Hom(J,J).")
    bykey["lower_Hom_annotation"]["reader_return_differs_from_C"]={"A":False,"B":False,"C":True}
    bykey["lower_Hom_annotation"]["notes"].append(
        "C's broad vertical_relation_and_enclosure issue covers this bracket scope plus the relation sign. Main must decide both. Location, enclosure and existing H note form one annotation locus, not a second omission.")
    bykey["vertical_relation"]["notes"].append(
        "A traces two strokes plus a separate point; B traces them inside an uncertainty macro; C uses rotated simeq and includes the sign within tall brackets. A/B's point is part of this relation cluster, distinct from C's two newly reported point groups elsewhere.")
    bykey["inclusion_curve"]["notes"].append(
        "A changes endpoint gaps in the returned TikZ; B/C retain witness C's exact path. This is a main adjudication question even though all report an open headless path.")
    bykey["first_map_layout"]["notes"].append(
        "Main19 adds a modest horizontal displacement of the lower arrow relative to the upper hook. All returned aligned environments share the same arrow column; this newly recorded main choice changes witness C's geometry.")
    for key in ["cancelled_Si_J","cancelled_Si_stop","first_map_J","first_map_layout",
                "final_J_pair","final_Hom","final_J"]:
        bykey[key]["notes"].append(
            "A/C broad source wording is localized here; separate physical symbols or terminal/layout marks are not duplicated by an additional broad counted row.")
    bykey["cancelled_Si_J"].update(witness_C=r"x\in J_n",witness_H=r"x\in I_n")
    bykey["cancelled_Si_stop"].update(witness_C="Terminal full stop inside canceled sentence",witness_H="No terminal full stop")
    bykey["lower_Hom_annotation"].update(
        witness_C=r"Vertical equals above [\mathrm{Hom}(D_{n'},D_n)], all beneath left inverse image; square brackets surround Hom only",
        witness_H=r"Prose note places [\mathrm{Hom}(D_{n'},D_n)] and a simeq under the right member",
    )
    bykey["xi_layout"]["notes"].append(
        "Reader A has no standalone issue, but its complete reading and Mapping below log row preserve the separate lower row. C's source issue checks xi/index identity rather than H layout; exact source report remains separate.")
    catalog = []
    for a in "ABC":
        source = metadata[a].get("crops",[]) if isinstance(metadata[a],dict) else metadata[a]
        for item in source:
            entry = copy.deepcopy(item)
            entry.update(reader=a,path=relpath(item["path"],a),catalog_id=f"R{len(catalog)+1:02d}")
            catalog.append(entry)
    crop_index = {(x["reader"],x["path"]):x for x in catalog}
    source_map = {a:{k:[] for k in issues[a]} for a in "ABC"}
    for row in rows:
        for a in "ABC":
            for k in row["source_issues"][a]:
                source_map[a][k].append(row["id"])
                cp = issues[a][k].get("crop")
                if cp:
                    path = relpath(cp,a)
                    if (a,path) not in crop_index:
                        candidates = [x for x in catalog if x["reader"]==a and Path(x["path"]).name==Path(path).name]
                        assert len(candidates)==1,(a,path)
                        entry=candidates[0]
                    else:entry=crop_index[(a,path)]
                    if entry not in row["reader_crop_options"]:
                        row["reader_crop_options"].append(copy.deepcopy(entry))
    assert all(ids for sm in source_map.values() for ids in sm.values()), source_map
    c_doubt_map=[]
    for d,key in zip(doubts["C"],C_DOUBT_KEYS):
        row=bykey[key]
        row["C_doubts"].append(d["id"])
        c_doubt_map.append({**copy.deepcopy(d),"locus_key":key,"locus_id":row["id"],
            "readers":copy.deepcopy(row["readers"]),
            "reader_return_differs_from_C":copy.deepcopy(row["reader_return_differs_from_C"]),
            "status":"pending main adjudication",
            "counting_note":"C05 and C06 share one naming-cluster physical locus." if key=="naming_cluster" else "One source doubt at its physical locus."})
    contextual = build_context(context,bykey)
    inventory=build_inventory(reports)
    paths=[PACKET/f for f in ["C.tex","H.tex","C_context.md","page.json"]]
    paths += [P/"witness_doubts.json",P/"witness_locus_checklist.json"]
    paths += [P/f"reader_{a}"/f for a in "ABC" for f in ["reading.tex","report.json","read_log.md","crop_metadata.json"]]
    result={
        "scan":8,"created_utc":datetime.now(timezone.utc).isoformat(),
        "status":"complete text-only reader crosswalk; main choices recorded in staged decision draft",
        "scope":"Current scan008 text only. No image, crop content, OCR, web, mathematical proof, compilation, rendering, selected-page or cumulative-file writing.",
        "counts":{"reader_issues":{a:len(issues[a]) for a in "ABC"},"source_issues":sum(len(v) for v in issues.values()),
            "comparison_rows":len(rows),"physical_loci":sum(x["countable"] for x in rows),
            "noncounted_register_rows":sum(not x["countable"] for x in rows),
            "C_inline_doubts":len(c_doubt_map),"H_marked_doubts":len(doubts["H"]),
            "C_context_table_rows":len(contextual["table_rows"]),"context_checks":len(contextual["checks"]),
            "inventory_union":len(inventory),"reader_crops":{a:reports[a]["crop_count"] for a in "ABC"}},
        "loci":rows,"source_issue_map":source_map,"source_issue_index":copy.deepcopy(issues),
        "C_doubt_map":c_doubt_map,
        "H_doubt_map":[{**copy.deepcopy(d),"locus_keys":keys,"locus_ids":[bykey[k]["id"] for k in keys]}
                       for d,keys in zip(doubts["H"],H_DOUBT_KEYS)],
        "contextual_C_checks":contextual["checks"],"C_context_table_rows":contextual["table_rows"],
        "C_context_text":context,
        "inventory_crosswalk":inventory,
        "inventory_count_note":("A's 40 rows plus two C-only detached-point groups = 42 union rows; B/C naming-status candidates are mapped into the single paragraph entry with cancellation status uncertain, per main13. All source inventory rows remain preserved."
            if len(inventory)==42 else "A's 40 rows plus two C-only detached-point groups and B/C's separately reported naming correction-status candidate = 43 candidate union rows. Main may fold the naming candidate into live paragraph coverage; no transcription is marked complete in advance."),
        "reader_crop_catalog":catalog,"main_crop_plan_snapshot":copy.deepcopy(plan_list),
        "reader_checks":{a:copy.deepcopy(reports[a].get("checks",[])) for a in "ABC"},
        "reader_notes":{a:copy.deepcopy(reports[a].get("notes",[])) for a in "ABC"},
        "reader_notation":{a:copy.deepcopy(reports[a].get("notation",[])) for a in "ABC"},
        "reader_full_readings":readings,"reader_logs":logs,"witness_full_texts":witnesses,
        "returned_tex_diffs":{a:list(difflib.unified_diff(witnesses["C"].splitlines(),readings[a].splitlines(),
            fromfile="witness_C.tex",tofile=f"reader_{a}/reading.tex",lineterm="")) for a in "ABC"},
        "input_snapshots":{str(p.relative_to(O.parent)):snapshot(p) for p in paths},
        "counting_policy":"Count each physical place once per differing witness. Broad source issues map to constituent places without an extra broad count. The two naming doubts share one place; the canceled application and its internal article share one place. Drawing annotations partly described in H notes are not also counted as whole omitted passages. Notation-register rows are noncounted. Removal, refinement, expansion or reordering of C uncertainty counts; equivalent TeX syntax does not.",
        "assembly_next_step":"Map root's numbered main observations and viewed crop plan to these rows; selected page and text validation required before main_complete can become true. Import five actual root events only after explicit root source confirmation. No mathematical audit is created.",
    }
    write_json(P/"reader_crosswalk.json",result)
    write_crosswalk_md(result)
    return result

def build_context(context,bykey):
    def item(cid,topic,keys,note):
        return {"id":cid,"topic":topic,"locus_keys":keys,
                "locus_ids":[bykey[k]["id"] for k in keys],"coverage":note,
                "source":"reader_inputs/scan008/C_context.md","status":"reader checks cross-referenced; main pending"}
    checks=[
        item("CTX01","J, D, D-tilde, tau and N forms",["REG_N_tau","quantifier","J_definition","J_type_arrow","J_notons","first_map_J","second_Hom_brackets","lower_J","lower_Hom","final_J_pair","final_Hom","final_J"],
             "All readers record local checking of the full formula register. C's missing lower-Hom issue is covered by its complete reading and log. No cross-page form is used as evidence."),
        item("CTX02","Inverse powers, primes, xi, u indices and rho labels",["REG_inverse_xi","second_Hom_superscript","rho_lower","rho_final","xi_layout","lower_J","final_J_pair"],
             "Actual letters and indices, including unequal J pair orders, remain source readings; no mathematical argument determines a glyph."),
        item("CTX03","Abbreviations and opening quotation ticks",["ens_definition","ens_image","ens_bijection","def_unaccented","type_caption","Dn_quote"],
             "Each local abbreviation endpoint and both unclosed quote pairs have separate physical coverage."),
        item("CTX04","First sous-objet plural question",["sous_objet"],
             "This contextual repeat maps to C02 and the same word; it adds no second change count."),
        item("CTX05","Two quotation closures",["type_caption","Dn_quote"],
             "Two separate positions; the contextual comparison with scan7 is historical witness prose, not current image evidence."),
        item("CTX06","Different paired-index orders",["lower_J","final_J_pair","rho_lower","rho_final"],
             "Definition and final diagram positions are independent loci, even if their mathematical relation is later checked."),
        item("CTX07","Folio/archive and page inventory",[],
             "All logs record archive 7, no own folio/title/date and no recoverable typed reuse; this is coverage metadata, not an omitted passage."),
        item("CTX08","C audit corrections and placements",["deleted_des_1","deleted_I_des","inserted_le","naming_cluster","par_ii","cancelled_Si_J","cancelled_Si_stop","upper_old_x","Soient_J","Soient_cancelled_on","avec_insertion","considerons","via_group","on_a_alors_application","first_Hom_old_D","first_Hom_plain_D","second_Hom_old_D","second_Hom_superscript","cancelled_bijec","lower_J_cancelled_group"],
             "Every current-page correction/cancellation described by C's audit has source issues; its audit is witness commentary, not a new reader or check event."),
        item("CTX09","C audit lower layout and diagram",["first_map_layout","second_Hom_brackets","vertical_relation","lower_Hom_annotation","ens_des_annotation","xi_layout","inclusion_curve"],
             "The three low brackets, vertical relation/enclosure, caption lines and final curve require main adjudication. A's altered endpoint gaps and C's broader brackets are explicit alternatives."),
    ]
    raw_rows=[]
    for line_no,line in enumerate(context.splitlines(),1):
        if not line.startswith("|"):continue
        cells=[x.strip() for x in line.strip().strip("|").split("|")]
        raw_rows.append({"id":f"CT{len(raw_rows)+1:02d}","line":line_no,"raw":line,"cells":cells})
    assert len(raw_rows)==25,len(raw_rows)
    for i,row in enumerate(raw_rows):
        if i<3:
            row["context_check_ids"]=[f"CTX{i+1:02d}"]
            row["locus_keys"]=checks[i]["locus_keys"]
        elif i<21:
            row["C_doubt_id"]=f"C{i-2:02d}"
            row["locus_keys"]=[C_DOUBT_KEYS[i-3]]
        elif i<24:
            row["context_check_ids"]=[f"CTX{i-17:02d}"]
            row["locus_keys"]=checks[i-18]["locus_keys"]
        else:
            row["context_check_ids"]=["CTX07"]
            row["locus_keys"]=[]
    return {"checks":checks,"table_rows":raw_rows}

def mdcell(value):
    return str(value).replace("|","&#124;").replace("\n","<br>")

def write_json(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")

def write_crosswalk_md(cw):
    c=cw["counts"]
    lines=["# Scan 008 — complete reader source crosswalk","",
        f"Text-only collation: {c['source_issues']} source issues (A47/B60/C49), 18 inline C doubts, 6 H doubt marks, 25 current-context table rows, {c['physical_loci']} physical comparison places and 2 noncounted notation registers.","",
        "Main choices are recorded in the staged decision draft; selected-page validation controls completion. The physical row count is not a change total. The two naming doubts and B019/B020 form one location; B030/B031 form one canceled-phrase location. Broad omissions and their parts are not both counted.","",
        "## Coverage anomalies requiring main decisions","",
        "- C alone draws one detached point after the old set and a pair after the second Hom; both are represented.",
        "- A changes the final curve's endpoint gaps; B/C retain witness C's exact geometry.",
        "- C enlarges the lower square enclosure to include the relation and Hom; A/B leave the relation above the bracketed Hom.",
        "- C's final full reading and report have five naming alternatives; root compared that updated return before main crops.",
        "- Main observation 5 introduces a distinct H-like/forall uncertainty against every reader and witness; its new physical sign row is included.",
        "- C lacks a standalone lower Hom(J,J) issue, but its full reading and log explicitly check that witness-H difference.",
        "- "+cw["inventory_count_note"]+" Source-to-parent mappings are retained; transcription status requires selected-page validation.","",
        "| Key | Place | Witness C | Witness H | A | B | C | Source issues |",
        "|---|---|---|---|---|---|---|---|"]
    for x in cw["loci"]:
        src="; ".join(a+": "+(", ".join(x["source_issues"][a]) or "full text/log only") for a in "ABC")
        vals=[x["key"],x["location"],x["witness_C"],x["witness_H"],*[x["readers"][a] for a in "ABC"],src]
        lines.append("| "+" | ".join(mdcell(v) for v in vals)+" |")
    lines += ["","## Every inline C doubt","","| ID | Exact source alternatives | Physical key |","|---|---|---|"]
    for x in cw["C_doubt_map"]:
        lines.append("| "+" | ".join(mdcell(x[k]) for k in ["id","reading","locus_key"])+" |")
    lines += ["","## Every H doubt mark","","| ID | Macro and body | Physical keys |","|---|---|---|"]
    for x in cw["H_doubt_map"]:
        lines.append("| "+" | ".join(mdcell(v) for v in [x["id"],x["macro"]+"{"+x["reading"]+"}",", ".join(x["locus_keys"])])+" |")
    lines += ["","## Context coverage",""]
    for x in cw["contextual_C_checks"]:
        lines.append(f"- **{x['id']} — {x['topic']}**: {x['coverage']} Rows: {', '.join(x['locus_keys']) or 'inventory/metadata'}.")
    lines += ["","## Inventory union","","| Element | Kind | A/B/C source rows | Main status |","|---|---|---|---|"]
    for x in cw["inventory_crosswalk"]:
        refs=" / ".join(",".join(map(str,x["source_inventory_rows"][a])) or "—" for a in "ABC")
        lines.append("| "+" | ".join(mdcell(v) for v in [x["element"],x["kind"],refs,x["transcribed"]])+" |")
    lines += ["","All three actual reader check lists are empty. Main confirmed the source correspondence at 13:00:18 UTC; the five original main events are imported unchanged in the staged decision. No audit or re-proof is performed by this assembler. Exact reports, complete returned TeX, logs, crop metadata, current-context table rows and input hashes are retained in the JSON crosswalk.",""]
    (P/"reader_crosswalk.md").write_text("\n".join(lines))

def check_selected_page(issues,cw):
    path=O/"pages/H104-01_104_scan008.tex"
    errors=[]
    if not path.exists():return {"passed":False,"status":"pending selected page","errors":["Selected page does not exist."]}
    text=path.read_text(); sha=snapshot(path)["sha256"]
    if not EXPECTED_SELECTED_PAGE_SHA256:errors.append("Main-selected expected page hash pending.")
    elif sha!=EXPECTED_SELECTED_PAGE_SHA256:errors.append("Selected-page hash differs from the main-confirmed version.")
    if not PAGE_REQUIRED:errors.append("Main-decision text guards pending.")
    guards=[]
    for key,parts in PAGE_REQUIRED.items():
        missing=[s for s in parts if s not in text]
        guards.append({"key":key,"passed":not missing,"missing":missing})
        if missing:errors.append(f"Missing selected-page main content for {key}.")
    inventory_guards=[]
    for row in cw["inventory_crosswalk"]:
        key=row["element"].split(":",1)[0]
        parts=INVENTORY_REQUIRED.get(key)
        missing=[] if parts is None else [s for s in parts if s not in text]
        passed=parts is not None and not missing
        inventory_guards.append({"element":key,"passed":passed,"missing":missing})
        if not passed:errors.append(f"Inventory {key} has no passing selected-text guard.")
    return {"passed":not errors,"status":"passed" if not errors else "pending/failed selected-page text validation",
            "sha256":sha,"errors":errors,"main_guards":guards,"inventory_guards":inventory_guards}

def math_events(cw,main):
    actual=[]
    for a in "ABC":
        for n,raw in enumerate(cw["reader_checks"][a],1):
            event=copy.deepcopy(raw)
            event.update(source_file=f"records/scan008/reader_{a}/report.json",source_event_index=n)
            actual.append(event)
    if not MATH_SOURCE_CONFIRMED:return actual
    path=P/"math_checks.json"; data=json.loads(path.read_text())
    assert len(data["events"])==5
    for n,raw in enumerate(data["events"],1):
        event=copy.deepcopy(raw)
        observations=MATH_SOURCE_OBSERVATIONS.get(event["statement_id"],[])
        assert observations and all(k in main for k in observations),event["statement_id"]
        event.update(source_file="records/scan008/math_checks.json",source_event_index=n,
                     source_sha256=snapshot(path)["sha256"],main_source_observations=observations)
        actual.append(event)
    return actual

def page_notes():
    if not MATH_SOURCE_CONFIRMED:return []
    return [
        "The page identifies J_n with the subobjects of D_n and introduces the canonical type map tau_n to the ordered object classes N. It describes this map as strictly increasing, with image N_{<=n}, and records the singleton fiber over n as {d_n}, where d_n is the greatest subobject. These claims are checked under the recorded monicity and identity-endomorphism hypotheses and the usual subobject convention; the set-level convention remains ambient scope.",
        "The first two-row Hom map sends an arrow from D_n-prime to D_n to its represented subobject and identifies Hom with the type-n-prime fiber. The next construction sends such an arrow to its action on subobjects, inducing rho from that fiber to Hom(J_n-prime,J_n). The recorded check establishes injectivity by evaluation at the greatest subobject and the stated inclusion composite. Full arguments are retained in the five actual main event records, without an additional audit or re-proof. The three image readers report no mathematical check events.",
        "The definition uses J_{n-prime,n}, whereas the final diagram begins J_{n,n-prime}. Main's source confirmation at 13:00:18 UTC establishes that index discrepancy from the ink; both orders are retained. The five original events keep their historical outcomes, including the initially conditional index check. Ink confirmation is not a new proof event. The transcription preserves cancellations, insertions, uncertain overwritten letters, captions, brackets and the open inclusion path. Remaining doubts, including the H-like/forall sign and literal relation trace, stay in the body. Archive sheet 7 is recorded without assigning an author folio, date or title.",
    ]

def build_draft(cw):
    main_text,main,plan_list,plan=get_main()
    bykey={x["key"]:x for x in cw["loci"]}
    decisions=[]; locus_map={}
    for key,raw in SPECS.items():
        s=copy.deepcopy(raw); x=bykey[key]
        keys=[key]+s.pop("merge",[])
        ns=s.pop("main_observations",[MAIN_NUMBERS.get(key)])
        assert ns and all(n in main and n in plan and plan[n].get("viewed") for n in ns),(key,ns)
        refs={a:[] for a in "ABC"}
        for k in keys:
            assert k not in locus_map,k
            locus_map[k]=x["id"]
            for a in "ABC":refs[a]+= [z for z in bykey[k]["source_issues"][a] if z not in refs[a]]
        crops=[plan[n]["path"] for n in ns]
        row={"id":x["id"],"location":x["location"],"C":x["witness_C"],"H":x["witness_H"],
            **s,"marked_in_H":"yes" if any(cw["source_issue_index"][a][z].get("marked_in_H")=="yes" for a in "ABC" for z in refs[a]) else "no",
            "readers":copy.deepcopy(x["readers"]),"source_issues":refs,"main_observations":ns,
            "crop":crops[0],"crops":crops,"evidence":"\n".join(f"Main {n}: {main[n]}" for n in ns),
            "reader_evidence":{a:[{"id":z,"evidence":cw["source_issue_index"][a][z]["evidence"]} for z in refs[a]] for a in "ABC"},
            "reader_report_readings":{a:[{"id":z,"reading":cw["source_issue_index"][a][z]["reading"]} for z in refs[a]] for a in "ABC"},
            "crosswalk_keys":keys,"countable":x["countable"]}
        if key in {"on_a_alors_application","J_notons","inserted_le"}:row["marked_in_H"]="no"
        assert all(k in row for k in ["final","confidence","diff_C","diff_H","kind","unresolved"]),key
        assert row["countable"] or not(row["diff_C"] or row["diff_H"]),key
        decisions.append(row)
    source_map={a:{k:[] for k in cw["source_issue_index"][a]} for a in "ABC"}
    for x in decisions:
        for a in "ABC":
            for k in x["source_issues"][a]:source_map[a][k].append(x["id"])
    covered_ids={bykey[k]["id"] for k in locus_map}
    source_coverage={a:{k:{"required_crosswalk_loci":ids,"decision_ids":source_map[a][k],
        "status":"complete" if set(ids)<=covered_ids else "pending"} for k,ids in sm.items()}
        for a,sm in cw["source_issue_map"].items()}
    idmap={x["id"]:x for x in decisions}
    doubts=copy.deepcopy(cw["C_doubt_map"])
    for d in doubts:
        if d["locus_key"] in locus_map:
            x=idmap[locus_map[d["locus_key"]]]
            d.update(status="adjudicated",decision_id=x["id"],final=x["final"],unresolved=x["unresolved"],
                     main_observations=x["main_observations"],crop=x["crop"],doubt_changed_from_C=x["diff_C"],
                     disposition="resolved" if not x["unresolved"] else "refined or reordered" if x["diff_C"] else "retained")
    counts=Counter()
    for x in decisions:
        if x["diff_C"]:counts["C"]+=1;counts["C_"+x["confidence"]]+=1
        if x["diff_H"]:counts["H"]+=1;counts["H_"+x["confidence"]]+=1
        if x["diff_C"] or x["diff_H"]:counts[x["confidence"]]+=1
    validation=check_selected_page(decisions,cw)
    main_done=bool(plan) and set(plan)<=set(main) and all(x.get("viewed") for x in plan_list) and len(locus_map)==len(bykey) and MATH_SOURCE_CONFIRMED
    complete=main_done and validation["passed"]
    inventory=copy.deepcopy(cw["inventory_crosswalk"])
    if complete:
        for row in inventory:row.update(transcribed="yes",selected_reading=True,page_text_sha256=validation["sha256"])
    included=sorted({n for x in decisions for n in x["main_observations"]})
    selected=[plan[n] for n in included]
    contextual=copy.deepcopy(cw["contextual_C_checks"])
    for row in contextual:
        row["main_observations"]=sorted({n for k in row["locus_keys"] if k in locus_map for n in idmap[locus_map[k]]["main_observations"]})
        row["status"]=("reader registers and recorded main decisions cover current-page context"
            if row["locus_keys"] and all(k in locus_map for k in row["locus_keys"]) else
            "metadata/inventory checked against selected page" if complete else "reader metadata covered; selected-page inventory validation pending")
    h_doubts=copy.deepcopy(cw["H_doubt_map"])
    for row in h_doubts:
        row["decision_ids"]=list(dict.fromkeys(locus_map[k] for k in row["locus_keys"] if k in locus_map))
        row["status"]="adjudicated" if all(k in locus_map for k in row["locus_keys"]) else "pending"
    result={
        "scan":8,"folder":"H104-01","issues":decisions,
        "remaining":[{"location":x["location"],"reading":x["final"],"alternatives":x.get("alternatives","No separately identified alternative."),
                      "confidence":x["confidence"],"reason":x["evidence"],"decision_id":x["id"],"crop":x["crop"]} for x in decisions if x["unresolved"]],
        "inventory":inventory,"notes":page_notes(),"checks":math_events(cw,main),
        "math_source_statements_confirmed":MATH_SOURCE_CONFIRMED,"math_source_confirmation":MATH_SOURCE_CONFIRMATION,
        "math_checks_status":"Five actual main events imported; no reader checks or audit" if MATH_SOURCE_CONFIRMED else "Five actual main events pending explicit main source confirmation; reader actual checks preserved",
        "crop_counts":{**cw["counts"]["reader_crops"],"main":sum(x.get("source")=="new main crop" for x in selected)},
        "main_reused_crop_count":sum(x.get("source")=="reader reuse" for x in selected),
        "main_count":len(selected),"main_total_decision_crop_count":len(selected),"planned_main_crop_count":len(plan),
        "planned_main_new_crop_count":sum(x.get("source")=="new main crop" for x in plan_list),
        "planned_main_reused_crop_count":sum(x.get("source")=="reader reuse" for x in plan_list),
        "main_complete":complete,"main_adjudication_complete":main_done,
        "assembly_status":"complete staged decision; main choices and selected-page text verified" if complete else "all main choices staged; selected-page text validation pending" if main_done else "staged; main decisions and selected-page validation pending",
        "main_observations_included":included,"main_observations_available":sorted(main),
        "main_image_delivery_events":([
            {"main_plan_number":n,"path":plan[n]["path"],
             "first_delivery":"Tool result truncated before image reached main; not an inspection.",
             "redelivery":"Identical existing file delivered once; no new crop.",
             "successful_inspections":1,"failed_delivery_is_not_a_view":True}
            for n in [6,7] if n in main and n in plan]
            if "existing crops 6 and 7 was truncated" in main_text else []),
        "source_issue_map":source_map,"source_issue_coverage":source_coverage,
        "pending_source_issues":{a:[k for k,v in sm.items() if v["status"]!="complete"] for a,sm in source_coverage.items()},
        "crosswalk_locus_map":locus_map,"pending_loci":[k for k in bykey if k not in locus_map],
        "C_doubt_map":doubts,"H_doubt_map":h_doubts,
        "contextual_C_checks":contextual,
        "page_text_guard_status":validation["status"],"page_text_sha256":validation.get("sha256",""),"page_validation":validation,
        "counts":dict(counts),"counting_policy":cw["counting_policy"],
        "residual_questions":[] if complete else ["Selected-page text validation is pending; all 34 main observations and five actual source-confirmed events are staged."] if main_done else ["Remaining main decisions, explicit source confirmation and selected-page text validation are pending."],
    }
    write_json(P/"decision_draft.json",result)
    return result

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--crosswalk-only",action="store_true")
    args=parser.parse_args()
    cw=build_crosswalk(load_inputs())
    if not args.crosswalk_only:
        draft=build_draft(cw)
        if draft["main_complete"]:
            cw.update(status="complete crosswalk; all main decisions and selected-page inventory verified",
                inventory_crosswalk=copy.deepcopy(draft["inventory"]),
                C_doubt_map=copy.deepcopy(draft["C_doubt_map"]),
                H_doubt_map=copy.deepcopy(draft["H_doubt_map"]),
                contextual_C_checks=copy.deepcopy(draft["contextual_C_checks"]),
                selected_page_sha256=draft["page_text_sha256"],
                assembly_next_step="Ready for root review and copy; authoritative decision and cumulative files remain untouched.")
            write_json(P/"reader_crosswalk.json",cw)
            write_crosswalk_md(cw)
    print(json.dumps(cw["counts"],ensure_ascii=False))
