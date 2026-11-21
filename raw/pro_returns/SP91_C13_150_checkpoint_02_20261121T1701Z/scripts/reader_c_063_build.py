from pathlib import Path
import csv
import json
import os

ROOT = Path(__file__).resolve().parents[1]
RETURN = ROOT / "reader_returns"
C = (ROOT.parent / "input/SP91_C13_150_texts/pages/150_scan063.tex").read_text()
H = (ROOT.parent / "input/SP91_C13_150_texts/hua/hua_150_scan063.tex").read_text()
crops = json.loads((ROOT / "scripts/reader_c_063_crop_manifest.json").read_text())
crop_by_number = {int(x["file"].split("_p")[1][:2]): x for x in crops}

def atomic_text(path, value):
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        handle.write(value)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)

tex = r"""\scanpage{63}
\mspage{27}
\deleted{c) Si $(z_\alpha)_{\alpha\in I}$ est l'ens des éléments de
$\Sigma_{<x}=\uline{b}^{-1}(\{x\})$ (où $\uline{b}:\Sigma^{\unsure{<|*}}(1)\longrightarrow\Sigma$), les
\unsure{les};}

a) Pour \unsure{tt|$\forall$} $x\in\Sigma$, l'ens $\Sigma_{<x}$ \deleted{(fini) \unsure{est}}\inserted{est tot${}^t$}
\deleted{$\simeq\uline{b}^{-1}(\{x\}$} ordonné

b) Si $\Sigma^{\unsure{*|<}}(1)$ est le graphe de la relation
$x<y$, et $\uline{s},\uline{b}:\Sigma^{<}(1)\unsure{\rightrightarrows|=}\Sigma$ sont les applications
source et but, \deleted{\illegible{1}} l'application $\uline{b}$ est une immer-
sion \deleted{\uline{\unsure{bordante}}} \uline{propre} (donc les $\Sigma_{<x}\unsure{\ne|=}\uline{b}^{-1}(\{x\})$
sont finis)

c) Si $(z_\alpha)_{\alpha\in I}$ sont les éléments de $\Sigma_{<x}=b^{-1}(\{x\})$,
alors \inserted{la famille} \unsure{des|les} \unsure{g}ermes \inserted{en $x$} de sous-espaces \deleted{\unsure{bordants}}\inserted{de $\Sigma$}
images par $\uline{b}$ des \inserted{germes} $(\Sigma^{<}(1),z_\alpha)$, est \inserted{une famille}
\deleted{\unsure{transversaux}}\inserted{transversale}
de sous-espaces \uline{bordants}.

d) $\uline{\unsure{b|s|p_1}}:\Sigma^{<}(1)\longrightarrow\Sigma^*$ est \uline{transversal} p.r. à l'immersion
bordante $\uline{b}:\Sigma^{<}(1)\mathrel{-}\Sigma^{\unsure{*}}$
\deleted{\unsure{la diag.}}
\margin{ou sous forme d'une \unsure{récollection|récollement}
pour les $z_\alpha\in\Sigma^{<}(1)$ au dessus d'un même
$x\in\Sigma^*$\ldots}

$1^{\circ})$ Cas équisingulier : $\uline{s}:\Sigma^{<}(1)\mathrel{-}\Sigma$ fibrant \inserted{(propre)}

$2^{\circ})$ Cas non singulier : $\unsure{\Sigma}$ est une variété à bord,
dont le bord est $\uline{b}(\Sigma^{*}(1))$:

$3^{\circ})$ Cas \unsure{équisingulier|équi-singulier}-non-singulier : $\uline{s}:\Sigma^{<}(1)\mathrel{-}\Sigma$ est
fibrant \inserted{propre}, à fibres des variétés à bord, et le
fibré des bords est l'image de $\Sigma^{*}(2)$ par
le morphisme $\Sigma^{*}(2)\xrightarrow{\uline{s'}}\Sigma^{\unsure{*|<}}(1)$ \deleted{\unsure{avec}}\inserted{donné}
par $(x\prec y\prec z)\longrightarrow(x\prec z)$.
\margin{c'est sans doute conséquence de la conjonction des deux conditions $1^{\circ}),2^{\circ})$}
\margin{62}
"""
atomic_text(RETURN / "150_scan063.tex", tex)
changes = []

def change(place, c, h, final, against_c, against_h, kind, category,
           confidence, evidence, crop_number, marked_h=False, consequence=""):
    if c and c not in C:
        raise ValueError("C quotation not literal at " + place + ": " + repr(c))
    if h and h not in H:
        raise ValueError("H quotation not literal at " + place + ": " + repr(h))
    crop = crop_by_number[crop_number]
    changes.append({
        "id": f"063-{len(changes)+1:02d}", "place": place,
        "C": c, "H": h, "final": final,
        "against_C": against_c, "against_H": against_h,
        "kind": kind, "error_category": category, "marked_in_H": marked_h,
        "confidence": confidence, "evidence": evidence,
        "crop": crop["file"], "box": crop["box"],
        "mathematical_consequence": consequence,
    })

change("cancelled opening, l'ens", "l'ens des éléments", "l'une des éléments",
       "l'ens des éléments", False, True, "misread word", "Words", "high",
       "After the apostrophe are a low e, joined n and final s; the group ends before des. No full une is written.", 2)
change("cancelled opening, raised sign on the source Sigma",
       r"\Sigma^{<}(1)\longrightarrow\Sigma", r"\Sigma^{*}(1)\to\Sigma",
       r"\Sigma^{\unsure{<|*}}(1)\longrightarrow\Sigma", False, True,
       "misread symbol or index", "Symbols and indices", "medium",
       "The raised mark has an angled left junction and two rightward portions. The cancellation and adjoining parenthesis leave the star alternative open. The underlined b retains its separate lower stroke.", 3)
change("cancelled opening, final short word", r"\unsure{les}", r"les \ill{}",
       r"\unsure{les}", False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", "medium",
       "The third cancelled line retains a tall initial loop and a low joined es-like ending. The crossing line masks part of the word, so les stays doubtful.", 4, True)
change("cancelled opening, terminal semicolon", r"\unsure{les}", r"les \ill{}",
       r"\unsure{les};", True, True, "omission", "Omissions", "high",
       "A separate upper dot and lower comma-shaped stroke follow the final les-like group inside the cancelled opening.", 4, True)
change("a), short form after Pour", "Pour tt", "Pour tout",
       r"Pour \unsure{tt|$\forall$}", False, True,
       "abbreviation expanded or spelling modernised", "Abbreviations expanded, spelling modernised", "medium",
       "Only two tall joined strokes with a crossbar are written. They support short tt or a quantifier-shaped sign, without the four-letter sequence tout.", 5)
change("a), l'ens without a stop", "l'ens $", r"l'ens.\ $", "l'ens $",
       False, True, "text not on the page", "Text that is not on the page", "high",
       "There is a clear gap between the terminal s of ens and the following Sigma; no separate point is visible.", 5)
change("a), cancelled parenthesis and est", r"\deleted{(fini) est}", r"\struck{(fini, \ldots}",
       r"\deleted{(fini) \unsure{est}}", False, True,
       "misread word", "Struck text", "medium",
       "The curved right delimiter after fini is visible beneath the horizontal cancellation. A low word ending in a tall t-like stroke follows; its crossed letters are retained as doubtful est.", 6, True)
change("a), inserted est tot raised t and its position", r"\inserted{est tot${}^t$}",
       r"\add{tot\textsuperscript{t}}", r"\inserted{est tot${}^t$}", False, True,
       "omission", "Omissions", "high",
       "The interlinear insertion begins with a separate est before tot and its small raised t. It sits above the cancelled fini/est phrase, before the next-line cancelled preimage formula.", 6)
change("a), cancelled preimage, final delimiter",
       r"\simeq\uline{b}^{-1}(\{x\})", r"\simeq\underline b^{-1}(\lbrace x\rbrace)",
       r"\simeq\uline{b}^{-1}(\{x\}", True, True,
       "text not on the page", "Text that is not on the page", "high",
       "The cancelled expression ends at the right brace after x. The gap before ordonné contains no closing parenthesis. A short underline beneath b is separate from the long cancellation stroke.", 7)
change("b), first source Sigma superscript",
       r"b) Si $\Sigma^{<}(1)$", r"b) Si $\Sigma^{*}(1)$",
       r"b) Si $\Sigma^{\unsure{*|<}}(1)$", True, False,
       "misread symbol or index", "Symbols and indices", "medium",
       "The raised group has several dark joined short arms; star is the leading visible candidate. Its compactness leaves an angle reading open. The nearby lower speck is not treated as punctuation.", 8)
change("b), source of the two labelled maps",
       r"\uline{s},\uline{b}:\Sigma^{<}(1)", r"\underline s,\underline b : \Sigma^{*}(1)",
       r"\uline{s},\uline{b}:\Sigma^{<}(1)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The raised sign has a pointed left junction and two short rightward arms. Both s and b carry separate short underlines.", 9)
change("b), cancelled short group after but",
       r"\deleted{\unsure{---}}", "source et but, l'application",
       r"source et but, \deleted{\illegible{1}} l'application", True, True,
       "omission", "Struck text", "low",
       "A dense horizontal cancellation with small lower remnants occupies the gap after the comma. No complete letters can be recovered, and no sequence of three textual hyphens is established.", 10)
change("b), written line-end hyphen", "immer-\nsion", "immersion",
       "immer-\nsion", False, True, "omission", "Words", "high",
       "p32 shows the dotted initial i, joined middle letters, final r-like return and separate horizontal hyphen extending toward the right paper edge. The following-line sion is visible in p11.", 32)
change("b), cancelled and separately underlined bordante",
       r"\deleted{bordante}", r"\struck{\ill{}}",
       r"\deleted{\uline{\unsure{bordante}}}", True, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "medium",
       "The tall initial b, rounded middle remnants and terminal te-like strokes survive the zigzag strike. A separate sloping underline runs below the word. Several internal letters remain masked.", 11, True)
change("b), underline on propre", r"\uline{propre}", r"\uncertain{propre}",
       r"\uline{propre}", False, True, "other", "Other", "high",
       "The letters propre, including both descenders, are clear. A separate straight stroke below them is an underline.", 11, True)
change("b), relation in the parenthetical preimage expression",
       r"\Sigma_{<x}=\uline{b}^{-1}(\{x\})", r"\Sigma_{<x}=\underline b^{-1}(\lbrace x\rbrace)",
       r"\Sigma_{<x}\unsure{\ne|=}\uline{b}^{-1}(\{x\})", True, True,
       "misread symbol or index", "Symbols and indices", "medium",
       "Two short bars have a dark diagonal connection across their middle. The diagonal supports a crossed-equality reading first; the crowded strokes leave equality as the alternative. The complete preimage expression was inspected.", 12,
       consequence="The manuscript's relation sign remains unresolved; neither candidate is treated as an established mathematical assertion.")
change("c), plain b in the preimage",
       r"\Sigma_{<x}=b^{-1}(\{x\})", r"\Sigma_{<x}=\underline b^{-1}(\lbrace x\rbrace)",
       r"\Sigma_{<x}=b^{-1}(\{x\})", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The small b before the inverse exponent has a stem and bowl with open paper immediately below it; no separate underline is visible.", 13)
change("c), live word after the inserted la famille",
       r"\deleted{les}\inserted{la famille} des", r"\add{la famille} des",
       r"\inserted{la famille} \unsure{des|les}", True, False,
       "deletion state", "Struck text", "medium",
       "The insertion leader ends before a single body word. Its oval base and tall loop support des, with les still possible. No independent cancellation crosses it and no second preceding les is isolated.", 14)
change("c), overwritten initial g and H's additional cancelled group",
       r"des germes", r"des \struck{\ill{}} germes",
       r"\unsure{des|les} \unsure{g}ermes", False, True,
       "text not on the page", "Text that is not on the page", "medium",
       "The dark group lies at the first letter of germes and includes its descender; ermes follows it. No separately recoverable cancelled word is present. The overwritten g is marked without inventing an underlying letter.", 14, True)
change("c), punctuation after inserted de Sigma",
       r"\inserted{de $\Sigma$}", r"\add{de $\Sigma$},", r"\inserted{de $\Sigma$}", False, True,
       "text not on the page", "Text that is not on the page", "high",
       "The curved stroke below de Sigma is the insertion leader descending toward cancelled bordants. No separate comma follows Sigma.", 15)
change("c), inserted germes before the germ tuple",
       r"\inserted{germes}", r"des $(\Sigma^{*}(1),z_\alpha)$",
       r"des \inserted{germes} $(\Sigma^{<}(1),z_\alpha)$", False, True,
       "omission", "Omissions", "high",
       "The complete small word germes is above the gap between des and the tuple; its g descender and terminal s are visible.", 16)
change("c), Sigma superscript inside the germ tuple",
       r"(\Sigma^{<}(1),z_\alpha)", r"(\Sigma^{*}(1),z_\alpha)", r"(\Sigma^{<}(1),z_\alpha)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The raised mark next to Sigma has the two-arm angled form. The tuple retains its written 1, comma, z-alpha and closing parenthesis.", 16)
change("c), live est before the family insertion",
       r"\deleted{sont}\inserted{une famille}", r"est \add{une famille}", r"est \inserted{une famille}", True, False,
       "deletion state", "Struck text", "high",
       "The body word has an open initial e, joined s and tall final t. The strike through the following adjective begins to its right; no separate line crosses est.", 17)
change("c), cancelled transversaux",
       r"\deleted{transversaux}", r"\struck{\ill{}} \add{transversale}",
       r"\deleted{\unsure{transversaux}}\inserted{transversale}", False, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "medium",
       "The body adjective retains its trans- beginning and an -aux-like ending under the strike. Smaller transversale is above it. Several central letters of the cancelled word remain obscured.", 17, True)

change("d), overwritten first map label",
       r"\uline{s}", r"\underline s", r"\uline{\unsure{b|s|p_1}}", True, True,
       "misread symbol or index", "Symbols and indices", "low",
       "The heavy overwritten glyph has a tall stem and right-hand bowl, giving b the leading shape. Its black interior prevents separation of an s or p-with-index candidate. The underline is separate; no underlying cancelled letter is asserted.", 18, True)
change("d), first map source superscript",
       r"\Sigma^{<}(1)", r"\Sigma^{*}(1)", r"\Sigma^{<}(1)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The source superscript has a clear left vertex and two rightward strokes before the opening parenthesis.", 18)
change("d), first target star, M0603",
       r"\Sigma^{\unsure{*}}", r"\to\Sigma$ est", r"\Sigma^*", False, True,
       "omission", "Symbols and indices", "high",
       "The raised target mark has several arms around a dark junction, above and to the right of Sigma. The headed arrow, source and label were inspected together.", 18, True)
change("d), second map source superscript",
       r"\Sigma^{<}(1)", r"\Sigma^{*}(1)", r"\Sigma^{<}(1)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The source superscript repeats the narrow left-angle shape before the written (1).", 19)
change("d), second map unheaded shaft",
       r"\longrightarrow", r"\to", r"\mathrel{-}", True, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The shaft terminates in a short thickened end without a separately exposed V. The first d) arrow above has an exposed head. The bare horizontal sign records the observed shaft.", 18)
change("d), second target superscript, M0604",
       r"\Sigma^{\unsure{*}}", r"\to\Sigma$. \struck", r"\Sigma^{\unsure{*}}", False, True,
       "omission", "Symbols and indices", "medium",
       "A small raised dark triangular group is present above the second target Sigma. Its arms cannot be separated, so star remains doubtful. The complete mark is in p18; p19 clips its top.", 18, True)
change("d), no separate terminal stop after the second target",
       r"\Sigma^{\unsure{*}}",
       r"\to\Sigma$. \struck", r"\Sigma^{\unsure{*}}", False, True,
       "text not on the page", "Text that is not on the page", "high",
       "The raised dark mark lies in the superscript area. No separate baseline stop follows the target Sigma before the cancelled note below.", 18)
change("d), cancelled la diag. beneath the maps",
       r"\deleted{\unsure{la diag}}", r"\struck{\ill{}}\note{La lettre",
       r"\deleted{\unsure{la diag.}}", True, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "medium",
       "An initial l/a sequence, d loop, i dot and long terminal g descender survive the strike. A small separate dark dot follows g. The masked middle letters and stop remain within the local doubt.", 20, True)
change("upper margin, first word ou", r"\margin{ou sous forme", r"\marginal{au sens",
       "ou", False, True, "misread word", "Words", "high",
       "The opening is a rounded o followed by u; the first letter has no tall a-stem.", 21)
change("upper margin, sous", "ou sous forme", r"au sens \ill{}",
       "sous", False, True, "misread word", "Words", "high",
       "The second word has a joined low ou group between its initial and final s strokes.", 21)
change("upper margin, forme", "sous forme d'une", r"sens \ill{} d'une",
       "forme", False, True, r"readable ink left as \ill{}", "Readable ink left as illegible", "medium",
       "The word has a tall f, rounded o and joined rme ending. A long connecting stroke traverses nearby but does not cancel this wording.", 21, True)
change("upper margin, M0605 word",
       r"d'une \unsure{récollection|récollement}", r"d'une \ill{} \ldots",
       r"\unsure{récollection|récollement}", False, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "low",
       "Initial ré- and the tall middle loops are readable. The compressed ending and traversing leader leave récollection and récollement unresolved.", 21, True)
change("upper margin, source Sigma superscript",
       r"z_\alpha\in\Sigma^{<}(1)", r"z_\alpha\in\Sigma^{*}(1)",
       r"z_\alpha\in\Sigma^{<}(1)", False, True,
       "misread symbol or index", "Symbols and indices", "medium",
       "The raised mark before (1) shows the small angle form after rotation; the complete z-alpha membership expression was read.", 21)
change("upper margin, au dessus d'un même x",
       "au dessus d'un même\n" + r"$x\in\Sigma^*$",
       r"\ldots\ $\in\Sigma^{*}$",
       "au dessus d'un même\n" + r"$x\in\Sigma^*$", False, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "high",
       "The slanted lines contain au dessus with a gap, d'un même with its detached accent, and x before membership. Three terminal points follow the final Sigma-star.", 21, True)
change("case 1, source Sigma superscript",
       r"\Sigma^{<}(1)", r"\Sigma^{*}(1)", r"\Sigma^{<}(1)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The raised source sign forms a left-pointing angle. Its lower arm joins toward the following parenthesis without a separately crossing star-arm.", 22)
change("case 1, unheaded shaft",
       r"\longrightarrow", r"\to", r"\mathrel{-}", True, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The horizontal stroke has rounded ends, with no exposed V at the right. The curved stroke above belongs to the (propre) insertion leader.", 22)
change("case 2, terminal colon",
       r"\uline{b}(\Sigma^{*}(1))$.", r"\underline b(\Sigma^{*}(1))$.",
       r"\uline{b}(\Sigma^{*}(1))$:", True, True,
       "misread symbol or index", "Other", "high",
       "Two separate dark points stand vertically after the closing parentheses, giving a colon.", 23)
change("case 3, heading and non-singulier hyphen",
       "équisingulier-non singulier", "équisingulier-non singulier",
       r"\unsure{équisingulier|équi-singulier}-non-singulier", True, True,
       "omission", "Words", "medium",
       "A separate horizontal stroke is clear between non and singulier. The earlier short stroke after équi lies beside compressed dotted letter strokes, so the first word's possible hyphen remains open.", 24)
change("case 3, source Sigma superscript",
       r"\Sigma^{<}(1)", r"\Sigma^{*}(1)", r"\Sigma^{<}(1)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The source sign has a left-pointing junction with two rightward arms, matching the locally visible angle form.", 24)
change("case 3, unheaded shaft",
       r"\longrightarrow", r"\to", r"\mathrel{-}", True, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The source-to-target stroke is a plain horizontal shaft with a rounded right end; no arrowhead is exposed.", 24)
change("case 3, propre attaches before the comma after fibrant",
       r"fibrant, \inserted{propre}", r"\add{propre} fibrant,", r"fibrant \inserted{propre},", True, True,
       "insertion or placement", "Insertions put in the wrong place", "high",
       "The curved leader from interlinear propre descends to the space after fibrant and before the existing comma. Its endpoint is to the left of that comma.", 25)
change("case 3, cancelled avec",
       r"\deleted{\unsure{avec}}", r"\struck{\ill{}} \add{donné}",
       r"\deleted{\unsure{avec}}\inserted{donné}", False, True,
       r"readable ink left as \ill{}", "Readable ink left as illegible", "medium",
       "The strike leaves the top of an a loop, a v-shaped join and final ec-like remnants. Donné above has a detached final accent. The cancelled word remains doubtful.", 27, True)
change("final element mapping, source relations",
       r"(x\prec y\prec z)", r"(x<y<z)", r"(x\prec y\prec z)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "Both source relations have curved upper arms returning to their left junctions, with distinct lower arms.", 28)
change("final element mapping, target relation",
       r"(x\prec z)", r"(x<z)", r"(x\prec z)", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The relation in the target pair has the curved upper return visible in the source pair as well.", 28)
change("final element mapping, arrow has no initial bar",
       r"\longrightarrow", r"\longmapsto",
       r"\longrightarrow", False, True,
       "misread symbol or index", "Symbols and indices", "high",
       "The shaft starts with a rounded left end and finishes in a clear right-pointing head. No vertical bar stands at the left. A terminal point follows the target parenthesis.", 28)
change("bottom-left other-hand foliation",
       r"\mspage{62}", "", r"\margin{62}", True, True,
       "other", "Other", "high",
       "The pale thin 62 at the lower left has a different weight and hand from the dark authorial 27. It is retained as another hand's foliation.", 30)

def decision(mark, state, reading, evidence, number, confidence):
    crop = crop_by_number[number]
    return {"id": mark, "decision": state, "reading": reading, "evidence": evidence,
            "crop": crop["file"], "box": crop["box"], "confidence": confidence}

decisions = [
    decision("M0603", "first", r"\Sigma^*",
             "The complete first d) map is visible in p18. The raised target mark has several distinct arms around its dark junction.", 18, "high"),
    decision("M0604", "undecided", r"\Sigma^{\unsure{*}}",
             "p18 contains the complete raised triangular group. Its individual arms remain inseparable; p19 alone clips the top.", 18, "low"),
    decision("M0605", "undecided", r"\unsure{récollection|récollement}",
             "The rotated margin shows ré- and tall middle loops. The compressed ending is traversed by a leader; neither full ending is secure.", 21, "low"),
]

inventory = []
def item(kind, position, words, hand="his hand"):
    inventory.append({"element": f"E{len(inventory)+1:02d}", "kind": kind,
                      "position": position, "first_words_or_objects": words,
                      "sheet_kind": "text", "hand": hand, "transcribed": "yes"})

item("text", "upper-left corner", "27")
item("deletion", "top, principal lines 1–3", r"c) Si $(z_\alpha)_{\alpha\in I}$ est l'ens ... \unsure{les};")
item("text", "a), principal lines 4–5", r"a) Pour \unsure{tt|$\forall$} $x\in\Sigma$, l'ens ... ordonné")
item("deletion", "a), right end of line 4", r"(fini) \unsure{est}")
item("insertion", "a), above the cancelled right end", r"est tot${}^t$")
item("deletion", "a), beginning of line 5", r"$\simeq\uline{b}^{-1}(\{x\}$")
item("text", "b), principal lines 6–10", r"b) Si $\Sigma^{\unsure{*|<}}(1)$ ... sont finis)")
item("deletion", "b), line 8 after source et but,", r"\illegible{1}")
item("deletion", "b), line 9 between sion and propre", r"\uline{\unsure{bordante}}")
item("text", "c), principal lines 11–14", r"c) Si $(z_\alpha)_{\alpha\in I}$ ... de sous-espaces \uline{bordants}.")
item("insertion", "c), above line 12, leader before the live des/les word", "la famille")
item("text", "c), line 12, overwritten first letter of germes", r"\unsure{g}ermes")
item("insertion", "c), above germes/de sous-espaces", r"en $x$")
item("deletion", "c), right of de sous-espaces", r"\unsure{bordants}")
item("insertion", "c), above cancelled bordants with descending leader", r"de $\Sigma$")
item("insertion", "c), above line 13 between des and the tuple", "germes")
item("insertion", "c), above line 13 after live est", "une famille")
item("deletion", "c), right end of line 13", r"\unsure{transversaux}")
item("insertion", "c), above the cancelled adjective", "transversale")
item("text", "d), principal lines 15–16", r"d) $\uline{\unsure{b|s|p_1}}:\Sigma^{<}(1)\longrightarrow\Sigma^*$ ...")
item("text", "d), overwritten initial map label", r"\uline{\unsure{b|s|p_1}}")
item("deletion", "d), below the first map, principal line 17", r"\unsure{la diag.}")
item("margin note", "left margin opposite d), cases 1 and 2; five slanted lines", r"ou sous forme d'une \unsure{récollection|récollement} ... $x\in\Sigma^*$...")
item("text", "case 1, principal line 18", r"$1^{\circ})$ Cas équisingulier ... fibrant")
item("insertion", "case 1, above fibrant with a curved leader", "(propre)")
item("text", "case 2, principal lines 19–20", r"$2^{\circ})$ Cas non singulier : $\unsure{\Sigma}$ ... $\uline{b}(\Sigma^{*}(1))$:")
item("text", "case 2, overwritten Sigma after the colon", r"\unsure{\Sigma}")
item("text", "case 3, principal lines 21–25", r"$3^{\circ})$ Cas \unsure{équisingulier|équi-singulier}-non-singulier ...")
item("insertion", "case 3, above fibrant; leader before its comma", "propre")
item("deletion", "case 3, after the labelled morphism", r"\unsure{avec}")
item("insertion", "case 3, above cancelled avec", "donné")
item("margin note", "lower-left margin, five slanted lines", r"c'est sans doute conséquence de la conjonction des deux conditions $1^{\circ}),2^{\circ})$")
item("text", "bottom-left corner", "62", "another unnamed hand")

doubts = []
def doubt(place, reading, alternatives, confidence, reason):
    if reading not in tex:
        raise ValueError("Doubt is not marked in TeX: " + reading)
    doubts.append({"place": place, "reading": reading, "alternatives": alternatives,
                   "confidence": confidence, "reason": reason})

doubt("cancelled opening, source Sigma", r"\Sigma^{\unsure{<|*}}(1)", "<; *", "medium",
      "The raised sign is crossed by the cancellation and crowded against its parenthesis.")
doubt("cancelled opening, third line", r"\unsure{les}", "les; no secure second candidate", "medium",
      "The loop and low ending survive, but the cancellation conceals part of the word.")
doubt("a), after Pour", r"\unsure{tt|$\forall$}", "tt; forall-shaped sign", "medium",
      "Two tall joined strokes and a crossbar support both local readings.")
doubt("a), cancelled word after (fini)", r"\unsure{est}", "est; no secure alternative", "medium",
      "The crossing line obscures the low middle letters.")
doubt("b), first Sigma superscript", r"\Sigma^{\unsure{*|<}}(1)", "*; <", "medium",
      "Several joined short arms give star the leading shape, but the junction is crowded.")
doubt("b), paired map shafts", r"\unsure{\rightrightarrows|=}", "paired right arrows; two plain bars", "medium",
      "Each shaft has a short downward end-tick; a fully exposed V is absent.")
doubt("b), cancelled underlined adjective", r"\deleted{\uline{\unsure{bordante}}}", "bordante; no secure alternative", "medium",
      "The separate underline is clear while the zigzag cancellation masks internal letters.")
doubt("b), parenthetical preimage relation", r"\unsure{\ne|=}", "crossed equality; equality", "medium",
      "A dark diagonal joins the two bars, but the tiny central group remains crowded.")
doubt("c), live body word after la famille", r"\unsure{des|les}", "des; les", "medium",
      "A low oval and tall loop support des; the initial stroke is not fully separated. No independent strike is visible.")
doubt("c), first letter of germes", r"\unsure{g}ermes", "g; unidentified overwrite", "medium",
      "The first-letter group is heavily retraced. Its descender is visible, but no underlying letter is asserted.")
doubt("c), cancelled bordants", r"\deleted{\unsure{bordants}}", "bordants; no secure alternative", "medium",
      "The horizontal strike masks several internal letter joins.")
doubt("c), cancelled transversaux", r"\deleted{\unsure{transversaux}}", "transversaux; no secure alternative", "medium",
      "The central part of the long word lies beneath a dense strike.")
doubt("d), first map label", r"\uline{\unsure{b|s|p_1}}", "b; s; p_1", "low",
      "A tall stem and right bowl are foremost, while the black overwrite prevents separation of the alternatives.")
doubt("d), second target superscript, M0604", r"\Sigma^{\unsure{*}}", "*; no secure further candidate", "low",
      "Only a compact raised triangular group is visible; its arms cannot be separated.")
doubt("d), cancelled note beneath first map", r"\deleted{\unsure{la diag.}}", "la diag. including a doubtful small stop", "medium",
      "Several letters are crossed and a small separate dark point follows the g descender.")
doubt("upper margin, M0605", r"\unsure{récollection|récollement}", "récollection; récollement", "low",
      "The tall loops and ré- remain visible, but the ending is crowded and crossed by a leader.")
doubt("case 2, initial Sigma", r"\unsure{\Sigma}", "Sigma with an unidentified overwrite", "medium",
      "A left upright and small lower interior arch remain within the retraced body. No separate underline or underlying glyph is securely isolated.")
doubt("case 3, first word of heading", r"\unsure{équisingulier|équi-singulier}", "équisingulier; équi-singulier", "medium",
      "A detached short stroke near équi may belong to the compressed following letters or mark a hyphen.")
doubt("case 3, target of the labelled morphism", r"\Sigma^{\unsure{*|<}}(1)", "*; <", "medium",
      "The raised target mark has a dark compressed junction and a long lower arm, leaving its form open.")
doubt("case 3, cancelled word beneath donné", r"\deleted{\unsure{avec}}", "avec; no secure alternative", "medium",
      "The strike leaves only portions of the a loop, v join and final ec-like strokes.")

notes = [
    {"id": "150-063-N01", "text": "The sheet bears the author's dark number 27 at the upper left and a separate pale foliation 62 in another hand at the lower left. There are 25 principal body baselines, including the cancelled opening and the cancelled short line below d); the insertions and two five-line margins are inventoried separately."},
    {"id": "150-063-N02", "text": "The manuscript cancels its opening draft c) with oblique crossing and enclosing strokes. Its final les-like group and semicolon remain transcribed. In a), est tot with raised t is inserted above the cancelled (fini) est area. The following cancelled preimage expression has no written closing parenthesis after the right brace."},
    {"id": "150-063-N03", "text": "The manuscript's a)–d) list uses the words ordonné, propre, transversale and transversal. The preimage expression in b) has a visible diagonal across its two-bar relation sign; both candidate readings remain in place. These observations record the manuscript, and no proof check is claimed."},
    {"id": "150-063-N04", "text": "In c), la famille attaches before a live des/les word; the first g of germes is overwritten. The body est before une famille remains live. The inserted words and cancelled bordants and transversaux are retained individually, including the manuscript's resulting wording. The first d) map label and second target superscript remain open."},
    {"id": "150-063-N05", "text": "The author gives three numbered Cas headings. The upper margin contains the unresolved récollection/récollement and ends with three points. The lower margin says c'est sans doute conséquence de la conjonction des deux conditions 1°), 2°); that doubt belongs to the author and is preserved without a supplied final stop."},
    {"id": "150-063-N06", "text": "The last element arrow has a visible head and no initial bar; its three relation signs have curved arms. Earlier plain horizontal shafts retain their visible form. The second case ends with two vertically separated dots. Its initial Sigma is overwritten, without a securely identifiable underlying glyph."},
    {"id": "150-063-N07", "text": "The composite lower audit region begins at sont finis) and includes every later body line, both margins, all interlinear changes and the pale foliation. It keeps interleaved slanted writing together so that no complete insertion is quoted from a rectangle that clips it. The 32 individual evidence crops retain their original pixel coordinates; the two margins are rotated only in the viewing crops."},
]

notation = [
    {"form": r"\Sigma_{<x}", "meaning": "The author's notation in the ordering and preimage passages.",
     "evidence": "Visible in the cancelled opening and a), b), c); the b) relation sign remains doubtful.",
     "places": "cancelled opening; a); b); c)"},
    {"form": r"\uline{s},\uline{b}", "meaning": "The labels called source et but in the manuscript.",
     "evidence": "The two separately underlined letters precede the paired shafts in b).",
     "places": "b), labelled maps; later occurrences individually read"},
    {"form": r"\Sigma^{<}(1)", "meaning": "Written Sigma with a raised angle and argument 1.",
     "evidence": "The local raised marks have left vertices and rightward arms; doubtful occurrences retain alternatives.",
     "places": "cancelled opening; b) second occurrence; c) tuple; d) sources; upper margin; cases 1 and 3"},
    {"form": r"\Sigma^*,\Sigma^{*}(1),\Sigma^{*}(2)", "meaning": "Written Sigma with a raised multiarmed mark.",
     "evidence": "The first d) target, margin ending and case 2 expression have visible arms; case 3's target stays doubtful.",
     "places": "d) first target; upper margin ending; case 2 ending; case 3 image and source"},
    {"form": r"\unsure{\rightrightarrows|=}", "meaning": "Two written horizontal shafts with small end-ticks.",
     "evidence": "Both strokes have short downward right-end marks; their head form remains open.",
     "places": "b), maps labelled s and b"},
    {"form": r"\mathrel{-}", "meaning": "Literal unheaded horizontal shaft between the written objects.",
     "evidence": "No separately exposed V is visible at the right ends.",
     "places": "d) second map; case 1 map; case 3 first map"},
    {"form": r"\uline{s'}", "meaning": "The manuscript's label on the headed morphism in case 3.",
     "evidence": "Small s, detached prime and separate underline appear above the shaft.",
     "places": "case 3, morphism from Sigma-star(2)"},
    {"form": r"\prec", "meaning": "The curved relation sign used in the final element mapping.",
     "evidence": "Curved upper returns and lower arms are visible in all three occurrences.",
     "places": "case 3, final source triple and target pair"},
]

abbreviations = [
    {"written": "ens", "expansion": "ensemble", "places": "cancelled opening; a), both without a supplied stop"},
    {"written": "tt", "expansion": "tout, as the leading short-form reading; the quantifier-shaped alternative remains open", "places": "a), after Pour"},
    {"written": "tot" + "$" + "{}^t$", "expansion": "totalement", "places": "a), interlinear insertion"},
    {"written": "p.r.", "expansion": "par rapport", "places": "d), before à l'immersion"},
    {"written": "diag.", "expansion": "diagramme, proposed only for the abbreviation list", "places": "d), cancelled la diag. remains doubtful"},
]

hand_log = [
    {"habit": "Small raised angles can join visually into the following opening parenthesis; darker groups can resemble stars.",
     "places": "b), c), d), upper margin, cases 1 and 3",
     "scope": "Each occurrence checked locally; the cancelled opening, b)'s first source and case 3 target retain alternatives.",
     "witness_errors": "H prints stars at several locally angular sources; C's first b) mark leads with angle while the proposed reading leads with star."},
    {"habit": "Curved insertion leaders can cross nearby text or end beside punctuation.",
     "places": "c) la famille, en x, de Sigma; case 1 (propre); case 3 propre",
     "scope": "The endpoint was traced separately from the inserted wording at each listed place.",
     "witness_errors": "C's extra cancelled les in c); H's comma after de Sigma; both drafts' placement of case 3 propre."},
    {"habit": "Heavy retracing can conceal an initial letter without a separately readable cancelled word.",
     "places": "c) first g of germes; d) first map label; case 2 initial Sigma",
     "scope": "These three local overwrites only; no underlying glyph is supplied.",
     "witness_errors": "H's separate cancelled illegible group before germes; both primary d) labels are more definite than the ink supports."},
    {"habit": "Cancellation and underlining can remain separate beneath the same word.",
     "places": "b), cancelled bordante; cancelled top and a) preimage b",
     "scope": "Separate exposed underlines are retained.",
     "witness_errors": "Both drafts omit the underline on cancelled bordante; the two cancelled preimage b underlines are retained from C/H."},
    {"habit": "Headed arrows, paired tick-ended shafts and plain horizontal shafts occur on this page.",
     "places": "b), d), cases 1 and 3",
     "scope": "Each visible endpoint form was read locally.",
     "witness_errors": "Both drafts supply heads to the second d) map and first maps in cases 1 and 3; H supplies a bar to the final element arrow."},
]

audit_boxes = []
def audit(kind, box, reading):
    audit_boxes.append({"box": f"B{len(audit_boxes)+1:02d}", "kind": kind,
                        "x0": box[0], "y0": box[1], "x1": box[2], "y1": box[3],
                        "reading": reading})

audit("handwritten number", [23, 35, 99, 104], r"\mspage{27}")
audit("struck passage", [371, 49, 1512, 157],
      r"\deleted{c) Si $(z_\alpha)_{\alpha\in I}$ est l'ens des éléments de}")
audit("struck passage", [274, 168, 1653, 291],
      r"\deleted{$\Sigma_{<x}=\uline{b}^{-1}(\{x\})$ (où $\uline{b}:\Sigma^{\unsure{<|*}}(1)\longrightarrow\Sigma$), les}")
audit("struck passage", [282, 302, 550, 363], r"\deleted{\unsure{les};}")
audit("lexical disagreement", [419, 373, 1367, 461],
      r"a) Pour \unsure{tt|$\forall$} $x\in\Sigma$, l'ens $\Sigma_{<x}$")
audit("insertion", [1389, 332, 1663, 458],
      r"\deleted{(fini) \unsure{est}}\inserted{est tot${}^t$}")
audit("struck passage", [260, 483, 603, 576],
      r"\deleted{$\simeq\uline{b}^{-1}(\{x\}$}")
audit("lexical disagreement", [435, 557, 1668, 647],
      r"b) Si $\Sigma^{\unsure{*|<}}(1)$ est le graphe de la relation")
audit("doubtful formula", [268, 648, 1668, 763],
      r"$x<y$, et $\uline{s},\uline{b}:\Sigma^{<}(1)\unsure{\rightrightarrows|=}\Sigma$ sont les applications")
audit("struck passage", [268, 758, 1668, 852],
      r"source et but, \deleted{\illegible{1}} l'application $\uline{b}$ est une immer-")
audit("struck passage", [266, 862, 846, 965],
      r"sion \deleted{\uline{\unsure{bordante}}} \uline{propre}")
audit("doubtful formula", [906, 838, 1662, 945],
      r"(donc les $\Sigma_{<x}\unsure{\ne|=}\uline{b}^{-1}(\{x\})$")
audit("doubtful formula", [23, 963, 1668, 2352],
      tex[tex.index("sont finis)"):].strip())
audit("handwritten number", [32, 2306, 88, 2350], r"\margin{62}")

# Correct the initial location descriptions after the visual reading.
crop_by_number[14]["purpose"] = "First c) revisions: la famille, live des/les, overwritten germes, en x"
crop_by_number[17]["purpose"] = "Live est; inserted une famille and transversale; cancelled transversaux"
atomic_text(ROOT / "scripts/reader_c_063_crop_manifest.json",
            json.dumps(crops, ensure_ascii=False, indent=2) + "\n")

with (ROOT / "packets/150_scan063/diffs.tsv").open(newline="") as handle:
    diff_count = len(list(csv.DictReader(handle, delimiter="\t")))
with (ROOT / "packets/150_scan063/marks.tsv").open(newline="") as handle:
    expected_marks = [x["id"] for x in csv.DictReader(handle, delimiter="\t")]
assert [x["id"] for x in decisions] == expected_marks
assert tex.count("$") % 2 == 0
for crop in crops:
    assert (ROOT / crop["file"]).is_file()
for row in changes:
    assert row["confidence"] in {"high", "medium", "low"}

counts = {"against_C": sum(x["against_C"] for x in changes),
          "against_H": sum(x["against_H"] for x in changes),
          "rows": len(changes)}

record = {
    "scan": "063", "reader": "reader_c", "line_count": 25,
    "changes": changes, "decisions": decisions, "inventory": inventory,
    "doubts": doubts, "notes": notes, "check_events": [],
    "notation": notation, "abbreviations": abbreviations, "hand_log": hand_log,
    "audit_boxes": audit_boxes, "crops": crops,
    "unresolved": [x["place"] + ": " + x["reading"] for x in doubts],
    "coverage": {
        "whole_image_viewed": True, "halves_viewed": ["top", "bottom"],
        "all_tokens_read": True, "all_C_insertions_deletions_checked": True,
        "differences_considered": diff_count,
        "macro_only_differences_ignored":
        r"\underline/\uline, \struck/\deleted, \add/\inserted, \marginal/\margin, \uncertain/\unsure, \ill/\illegible, equivalent brace syntax, degree notation, \emph for visible underlining, ordinary arrow length where its head agrees, whitespace and editorial H notes/page descriptions. The written immer- line-end hyphen is retained as ink."
    },
    "comparison_counts": counts,
}
atomic_text(RETURN / "150_scan063.json", json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"scan": "063", **counts, "decisions": len(decisions),
                  "inventory": len(inventory), "doubts": len(doubts),
                  "audit_boxes": len(audit_boxes), "crops": len(crops),
                  "packet_differences_considered": diff_count}, ensure_ascii=False))




