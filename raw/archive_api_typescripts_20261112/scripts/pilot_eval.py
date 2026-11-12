r"""Pilot evaluation (12 Nov 2026): recall of the existing-editions check's differences.

The items are the differences listed page by page in grothendieck_archive_montpellier/EXISTING_EDITIONS_CHECK_20261112.md
(written down here before the pilot results were read). For Pursuing Stacks and the Esquisse each item has
  diff  a regex looked for in the API's DIFFERENCES lines (draft, page and note fields together), and
  trans a regex for the page's reading in the API's TRANSCRIPTION (in a handwriting macro where the item is about
        handwriting: H: prefix = inside \hand, \over (2nd arg), \inserted or \margin; D: prefix = inside \deleted;
        M: prefix = inside \margin or \inserted; !: prefix = must NOT occur).
For EGA V there is no draft: the items are the readings the check made on the scans, looked for in the transcription.
An item counts as caught when the API reports it (diff) or its transcription has the page's reading (trans).
Every automatic verdict is then reviewed by hand (pilot_review.tsv); the report gives the reviewed figures.
usage: python pilot_eval.py
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))
from parse import results, sections, match_brace  # noqa: E402

I = []


def it(key, cls, desc, diff=None, trans=None):
    I.append({"key": key, "class": cls, "desc": desc, "diff": diff, "trans": trans})


k = "ps_134-2_017"
it(k, "wording", "handwritten 'as' (for struck 'for') -> 'to' in 'inadequate to a sweeping'", r"sweeping|inadequate to|\bas\b", r"H:\bas\b")
it(k, "wording", "'composition' -> 'compoisition'", r"compoisition", r"composition")
it(k, "formula", "margin note id_a = k_1^i(a) -> d_a=\\cst", r"d_a|id_a|\\cst|\\id", r"M:id")
it(k, "silent-correction", "'unadequate' -> 'inadequate'", r"unadequate", r"unadequate")
it(k, "normalization", "'too bad !' -> 'too bad!'", r"too bad", r"too bad[ ~]+!")
it(k, "normalization", "roman s, t, k", r"roman|upright|mathrm|italic", None)
it(k, "hand-unmarked", "'(or rather, homotopy)'", r"or rather", r"H:or rather")
it(k, "hand-unmarked", "'etc'", r"etc", r"H:etc")
it(k, "hand-unmarked", "subscript l on *", r"\\ell|ℓ|_l|subscript", r"H:\\ell|ℓ|\bl\b")
it(k, "hand-unmarked", "the 'notation' note (marginpar)", r"notation", r"M:notation")

k = "ps_134-2_044"
it(k, "wording", "'dans le langage' -> 'dans la langage'", r"la langage", r"dans le langage")
it(k, "omission", "closing quotation mark after 'pour 0<=i<=n'", r"quot|guillemet|''|»|\"", None)
it(k, "normalization", "'dim. n' -> 'dimension n'", r"dim\.|dimension", r"dim\.")
it(k, "normalization", "'disparaitre' -> 'disparaître'", r"dispara[iî]tre", r"disparaitre")
it(k, "normalization", "'chaines' -> 'chaînes'", r"cha[iî]nes", r"chaines")
it(k, "silent-correction", "'stablilise' -> 'stabilise'", r"stablilise", r"stablilise")
it(k, "silent-correction", "'interpéter' -> 'interpréter'", r"interp[ée]ter", r"interp[ée]ter")
it(k, "hand-missing", "struck 'pouvoir' printed ('pour espérer pouvoir conclure')", r"pouvoir", r"D:pouvoir")
it(k, "hand-unmarked", "'de plus'", r"de plus", r"H:de plus")
it(k, "hand-unmarked", "'espérer'", r"esp[ée]rer", r"H:esp[ée]rer")
it(k, "hand-unmarked", "'équivalente à'", r"[ée]quivalente", r"H:[ée]quivalente")
it(k, "hand-unmarked", "'général'", r"g[ée]n[ée]ral", r"H:g[ée]n[ée]ral")

k = "ps_134-3_024"
it(k, "addition", "'for such topology' -> 'for such a topology'", r"such a topology|such topology", r"for such topology")
it(k, "omission", "'a still coarser' -> 'a coarser'", r"still coarser", r"still coarser")
it(k, "silent-correction", "'caracterizing'", r"caracteriz", r"caracterizing")
it(k, "silent-correction", "'developped'", r"developped", r"developped")
it(k, "hand-altered", "margin note 'fibers are aspheric ... contractible (in Cech sense)' rewritten", r"contractible|weakly|aspheric", r"M:contractible")
it(k, "hand-unmarked", "'many'", r"\bmany\b", r"H:\bmany\b")
it(k, "hand-unmarked", "'section 23' (for struck 'page 19 ff')", r"section 23|page 19", r"H:23")
it(k, "hand-unmarked", "'direct' (for struck 'inverse')", r"\bdirect\b|inverse", r"H:\bdirect\b")
it(k, "hand-unmarked", "'arbitrary'", r"arbitrary", r"H:arbitrary")
it(k, "hand-unmarked", "'sheaves'", r"sheaves", r"H:sheaves")
it(k, "hand-unmarked", "'Hot-'", r"Hot", r"H:Hot")

k = "ps_134-3_081"
it(k, "wording", "'attractive in this condition' -> 'in the condition'", r"this condition|the condition", r"in this condition")
it(k, "wording", "'whereas' -> 'wheres'", r"wheres\b", r"whereas")
it(k, "wording", "footnote 'In fact' -> 'If fact'", r"If fact", r"In fact")
it(k, "silent-correction", "'respresented'", r"respresent", r"respresented")
it(k, "silent-correction", "'strenghtening'", r"strenght", r"strenghtening")
it(k, "silent-correction", "'dont'", r"\bdont\b|don't", r"\bdont\b")
it(k, "normalization", "parentheses around '(and nothing on either factor ... in (5))' dropped", r"either factor|parenthes", r"\(\s*and\b")
it(k, "normalization", "'implies (vii) i.e.' -> '(vii), i.e.,'", r"\(vii\),? i\.e|i\.e\.,", r"\(vii\)\s*i\.e\.")
it(k, "hand-unmarked", "margin note '27.3. But this is true for any equivalence of categories ...' as footnote", r"27\.3|equivalence of categories", r"M:27\.3|equivalence of categories")
it(k, "hand-unmarked", "margin note 'The plus is unnecessary visibly ...'", r"unnecessary", r"M:unnecessary")
it(k, "hand-unmarked", "margin note 'In fact, it is the condition that j_A ... model preserving'", r"model preserving|model-preserving", r"M:model")
it(k, "hand-unmarked", "'induce auto'", r"induce", r"H:induce")
it(k, "hand-unmarked", "'of (Hot)'", r"Hot", r"H:Hot")
it(k, "hand-unmarked", "'nothing on'", r"nothing on", r"H:nothing on")
it(k, "hand-unmarked", "'in (5)'", r"in \(5\)|\(5\)", r"H:\(5\)")
it(k, "hand-unmarked", "'and local test categories'", r"local test categories", r"H:local test")
it(k, "hand-unmarked", "'the first'", r"the first", r"H:the first")

k = "ps_134-4_044"
it(k, "wording", "'loc. cit.' -> 'loc. sit.'", r"loc\. ?sit|loc\. ?cit", r"loc\. ?cit")
it(k, "wording", "'homotopy structures definable' -> 'structure definable'", r"structures? definable", r"structures\W+(\w+\W+)?definable|structures")
it(k, "formula", "'W_h ⊂ W' -> W_{h_W}", r"h_W|h_\{W\}|W_\{?h", r"W_\{?h\}?\s*\\subset")
it(k, "silent-correction", "'was'nt'", r"was'nt|wasn't", r"was'nt")
it(k, "normalization", "comma 'compatible, i.e.,'", r"compatible,? i\.e", r"compatible i\.e")
it(k, "normalization", "comma 'W-aspheric, i.e.,'", r"aspheric,? i\.e", r"aspheric\}?\$? i\.e")
it(k, "hand-unmarked", "margin note '11.4. By which we mean ... universally in W' as dated footnote", r"11\.4|universally", r"M:11\.4|universally")
for w in ["moreover", "definitely", "many", "strictly", r"i\.e\. is", "mathematical", "natural", "homotopism", "itself"]:
    it(k, "hand-unmarked", f"'{w}'", w, "H:" + w)

k = "ps_134-4_082"
it(k, "wording", "'nor is it implied by it' -> 'implies by it'", r"implie[sd] by", r"implied by it")
it(k, "hand-missing", "'in Â' not printed in '(ii) The product of two W-aspheric objects [in Â]'", r"\\hat|Â|\\widehat|in A", r"H:\\hat|\\widehat|Â")
it(k, "hand-unmarked", "'the' (twice)", r"\bthe\b", r"H:\bthe\b")
it(k, "hand-unmarked", "'and map a->G'", r"map", r"H:map")
it(k, "hand-unmarked", "heading 'A) Total asphericity'", r"Total asphericity", r"H:Total")
it(k, "hand-unmarked", "'and moreover A is W-aspheric'", r"moreover", r"H:moreover")
it(k, "hand-unmarked", "'(i)'", r"\(i\)", r"H:\(i\)")
it(k, "other", "call '(*)' after 'totally W-aspheric' without counterpart", r"\(\*\)", r"\(\*\)")

k = "ps_134-5_029"
it(k, "omission", "'restricted to be an object b in B' -> 'be object b'", r"an object|be object", r"be an object")
it(k, "formula", "handwritten 'projection BxC -> B' printed 'B x C -> C'", r"projection|B\s*\\times\s*C|BxC", r"projection.{0,80}(\\over\{C\}\{B\}|\\hand\{B\})")
it(k, "formula", "diagram vertex 'Hot(W)' printed \\Cat", r"\\Cat|Hot", r"Hot\s*\(")
it(k, "silent-correction", "'it's image'", r"it's image|its image", r"it's image")
it(k, "silent-correction", "'in the the functor'", r"the the", r"the the")
it(k, "hand-unmarked", "'(A_b)_{b in I}'", r"A_b|A_\{b\}", r"H:A_")
it(k, "hand-unmarked", "'between'", r"between", r"H:between")
it(k, "hand-unmarked", "'W-'", r"W-|\\scrW", r"H:W")
it(k, "hand-unmarked", "bar over i*", r"bar|overline", r"H:\\bar|\\overline")
it(k, "hand-unmarked", "'lambda-bar_i ≃'", r"lambda", r"H:lambda")

k = "ps_134-6_001"
it(k, "wording", "'considerably clearer' -> 'clear'", r"clear(er)? understanding|clearer", r"clearer")
it(k, "wording", "'but belongs to' -> 'belong to'", r"belongs? to", r"belongs to")
it(k, "wording", "'situations where' -> 'when'", r"situations (where|when)", r"situations where")
for w, r in [("undispensable", "undispensable"), ("developping", "developping"), ("it's twin brothers", "it'?s twin"),
             ("sacro-saint", "sacro-?saint|sacrosanct"), ("Independance", "Independ[ae]nce")]:
    it(k, "silent-correction", f"'{w}'", r, r.split("|")[0].replace("-?", "-").replace("'?", "'").replace("[ae]", "a"))
it(k, "normalization", "underlined 'Hom(A°,M)' -> \\bHom", r"Hom", r"(uline|underline)\{?[^}]{0,12}Hom")
for w in ["part of", "handy criterion", "one or the other", r"\bone\b", r"strict"]:
    it(k, "hand-unmarked", f"'{w}'", w, "H:" + w)

k = "ps_134-6_018"
it(k, "omission", "'There is the problem of course' -> 'There is problem'", r"is (the )?problem", r"There is the problem")
it(k, "silent-correction", "'then it seemed' -> 'than'", r"(then|than) it seemed", r"then it seemed")
it(k, "silent-correction", "handwritten 'and for whom now' -> 'for which'", r"for wh(om|ich)", r"H:whom")
it(k, "normalization", "'non ordered'", r"non[- ]ordered", r"non ordered")
it(k, "normalization", "'non trivial' (three times)", r"non[- ]trivial", r"non trivial")
it(k, "normalization", "'so called'", r"so[- ]called", r"so called")
it(k, "normalization", "'A°' -> A^op", r"\\op|\^\{?\\circ|A°|\\mathrm\{op", r"\^\{?\\circ|A°|\^\{?o\b")
it(k, "normalization", "'L.' -> L_•", r"L_\{?\\bullet|L\.|bullet", r"L\.|L_\{?\.|L_\{?\\cdot")
it(k, "normalization", "commas added after 'Therefore', 'Thus' (twice)", r"Therefore|Thus", None)
it(k, "normalization", "commas after '(non-ordered simplices)', 'boundary maps)', one removed", r"simplices\)|maps\)", None)
it(k, "hand-unmarked", "'but only'", r"but only", r"H:but only")
it(k, "hand-unmarked", "'cases'", r"cases", r"H:cases")

k = "ps_134-7_064"
it(k, "silent-correction", "'Adam's' -> 'Adams''", r"Adam", r"Adam's")
it(k, "silent-correction", "'analyzor'", r"analyz[oe]r", r"analyzor")
it(k, "silent-correction", "'it's tensor powers'", r"it'?s tensor", r"it's tensor")
it(k, "silent-correction", "handwritten 'a Ω-structure' -> 'an'", r"an? \$?\\Omega|a \\Omega|\ban\b", r"\ba\s*\$?\\Omega")
it(k, "normalization", "'i.th' -> i^th", r"i\.th|textsuperscript|\^\{?th|i\$?\.th", r"i\$?\.th")
it(k, "normalization", "commas added ('possibly, too,', '119),', 'Thus,')", r"possibly|119\)|Thus", None)
it(k, "hand-unmarked", "insertion '(prompted by the reflections from the day before, cf. section 119)'", r"prompted", r"H:prompted")
it(k, "hand-unmarked", "'(n>=-1)'", r"\\geq?\s*-\s*1|≥", r"H:\\ge")
it(k, "hand-unmarked", "'extra'", r"extra", r"H:extra")
it(k, "hand-unmarked", "'(n+1)'", r"n\s*\+\s*1", r"H:n\s*\+\s*1")
it(k, "hand-unmarked", "'where'", r"\bwhere\b", r"H:\bwhere\b")
it(k, "hand-unmarked", "'(F,G) -> F∘G'", r"mapsto|\\circ", r"H:mapsto|\\circ")
it(k, "hand-unmarked", "'Ω_n over k_0'", r"k_0|k_\{0", r"H:k_\{?0")
it(k, "hand-unmarked", "'yield a Ω-structure'", r"yield", r"H:yield")
it(k, "hand-missing", "margin instruction 'à la ligne' not reproduced", r"ligne", r"M:ligne")
it(k, "hand-missing", "margin instruction 'id' not reproduced", r"\bid\b", r"M:\bid\b")

k = "ps_134-8_002"
it(k, "wording", "'– even as discovering them again' -> '-- and as'", r"even as|and as", r"even as")
it(k, "wording", "'out of a mist' -> 'out of the mist'", r"(a|the) mist", r"out of a mist")
it(k, "silent-correction", "'affraid'", r"affraid", r"affraid")
it(k, "silent-correction", "'was'nt'", r"was'nt|wasn't", r"was'nt")
it(k, "silent-correction", "'arpegios'", r"arpegg?ios", r"arpegios")
it(k, "normalization", "comma 'Rather surprisingly,'", r"surprisingly", None)
it(k, "normalization", "comma 'way, maybe'", r"way,? maybe", r"way maybe")
it(k, "hand-altered", "'(and the atmosphere relaxed and friendly)' printed without parentheses", r"atmosphere", r"H:atmosphere")
for w in ["Rather", "start", "special"]:
    it(k, "hand-unmarked", f"'{w}'", w, "H:" + w)

k = "esq_119_002"
it(k, "wording", "'Polyèdres réguliers et corps finis' -> 'sur les corps finis'", r"sur les corps|et corps", r"r[ée]guliers et corps")
it(k, "normalization", "'\"jeu de Légo-Teichmüller\",' -> 'jeu de \"Lego-Teichmüller\"'", r"L[ée]go", r"jeu de L[ée]go")
it(k, "silent-correction", "'bidimensionelle'", r"bidimensionn?elle", r"bidimensionelle")
it(k, "silent-correction", "'astéristiques'", r"ast[ée]ris", r"ast[ée]ristiques")
it(k, "hand-unmarked", "handwritten '1' and '7' of the N.B.", r"\(1\)|\(7\)|1|7", r"H:1|7")
k = "esq_119_003"
it(k, "wording", "'par A. Grothendieck' -> 'Alexandre'", r"Alexandre", r"par A\. ?Grothendieck")
it(k, "wording", "'illusoires' -> 'illusoire'", r"illusoires?", r"illusoires")
k = "esq_119_025"
it(k, "wording", "'standards' -> 'standard'", r"standards?", r"standards")
k = "esq_119_042"
it(k, "omission", "full stop after 'Weierstrass (*)'", r"Weierstrass", r"Weierstrass\s*\(\*\)\.")
k = "esq_119_058"
it(k, "wording", "'système' -> 'sytème'", r"syt[eè]me|syst[eè]me", r"syst[eè]me")
it(k, "wording", "'carrés de droite' -> 'droites'", r"de droites?", r"carr[ée]s de droite\b")
it(k, "silent-correction", "second 'X_{i,j} -> X_i' -> 'Xij -> Xj'", r"X_\{?j|Xj|X_j|X_i\b|X_\{i\}", None)
it(k, "normalization", "indices X_{i,j}, X_{i,j,k} -> Xij, Xijk", r"Xij|indice|comma|X_\{i, ?j", r"X_\{i, ?j")

k = "ega24_24_004"
it(k, "reading", "'(locally direct summands or factors)'", None, r"summands or factors")
it(k, "reading", "'or also the transpose homomorphism'", None, r"transpose homomorphism")
it(k, "reading", "'which is therefore determined'", None, r"which is therefore determined")
it(k, "reading", "'an invertible quotient L_P' (no 'module')", None, r"invertible quotient\s*\$?\\?(mathcal\{)?L|invertible quotient \$")
k = "ega24_24_018"
it(k, "reading", "'X is separable over k'", None, r"separable over")
it(k, "reading", "'should be'", None, r"should be")
it(k, "reading", "'Z_i' (not Ziη)", None, r"Z_\{?i\}?(?!\s*\\eta)")
it(k, "reading", "typed query '[PB incomprehensible].*' in place", None, r"PB incomprehensible")
it(k, "reading", "no 'and we are reduced'", None, r"!and we are reduced")
k = "ega24_24_037"
it(k, "reading", "'start from a closed subset'", None, r"start from a closed")
it(k, "reading", "'dimension of' (not 'fo')", None, r"dimension of")
it(k, "reading", "'(S_k) [illegible ask Grothendieck]* S_{k-1}' gap kept", None, r"illegible ask Grothendieck")
it(k, "reading", "handwritten '* Ask AG'", None, r"H:Ask AG|M:Ask AG")
k = "ega25_25_002"
it(k, "reading", "heading 'IV 20 ... (Etat 0)'", None, r"Etat 0|[ÉE]tat\s*0")
it(k, "reading", "'Commentaires'", None, r"Commentaires")
it(k, "reading", "'esquisse détaillée'", None, r"esquisse d[ée]taill[ée]e")
it(k, "reading", "'Je n'ai pas encore rédigé le n° 16'", None, r"pas encore r[ée]dig[ée]")
it(k, "reading", "'sans doute les actuels nos 11, 12, 14, 15'", None, r"sans doute les actuels")
it(k, "reading", "handwritten 'nouveau EGA V'", None, r"H:nouveau|M:nouveau")
k = "ega25_25_004"
it(k, "reading", "handwritten 'coniques' for struck 'linéaires'", None, r"H:coniques")
it(k, "reading", "struck 'linéaires'", None, r"D:lin[ée]aires")
it(k, "reading", "'20.1'", None, r"20\.1")
it(k, "reading", "'Module' with capital M", None, r"Module")
it(k, "reading", "'(loc facteurs directs)'", None, r"loc\.? facteurs directs")
it(k, "reading", "'un module quotient inversible L_P'", None, r"module quotient inversible")
it(k, "reading", "Ě, P̌ (checks)", None, r"\\check|\\v\{|Ě|P̌")
k = "ega25_25_140"
it(k, "reading", "'Ce n° sera utilisé au par. 20'", None, r"sera utilis[ée] au par")
it(k, "reading", "'sa place naturelle me semble bien au par. 16'", None, r"place naturelle")
it(k, "reading", "'m_x' (lower-case x)", None, r"m_\{?x\b|\\mathfrak\{m\}_\{?x\b")
it(k, "reading", "'point ξ de X à valeurs dans k′'", None, r"valeurs dans\s*\$?k'|valeurs dans\s*\$?k\^\{?\\prime|valeurs dans \$k'")
it(k, "reading", "'x′ de X_{k′}'", None, r"X_\{k'\}|X_\{k\^\{?\\prime")
it(k, "reading", "'φ_{k′}'", None, r"(phi|varphi)_\{k'|(phi|varphi)_\{k\^")
it(k, "reading", "'Remarques 2'", None, r"Remarques\s*2")
it(k, "reading", "the struck passage marked as deleted", None, r"\\deleted\{")

HMAC = ("\\hand{", "\\inserted{", "\\inserted[typed]{", "\\margin{", "\\over{")
MMAC = ("\\inserted{", "\\inserted[typed]{", "\\margin{")


def spans(t, macs):
    out = []
    for mac in macs:
        i = 0
        while True:
            k = t.find(mac, i)
            if k < 0:
                break
            b = k + len(mac) - 1
            e = match_brace(t, b)
            if mac == "\\over{":  # second argument
                if e < len(t) and t[e] == "{":
                    e2 = match_brace(t, e)
                    out.append(t[e + 1:e2 - 1])
                    e = e2
            else:
                out.append(t[b + 1:e - 1])
            i = e
    return "\n".join(out)


def norm(t):
    t = t.replace("’", "'").replace("‘", "'")
    t2 = re.sub(r"-%\s*\n\s*", "", t)  # words hyphenated at line ends joined
    t2 = re.sub(r"%[^\n]*", "", t2)
    return re.sub(r"\s+", " ", t2)


def test_trans(rx, tr):
    if rx is None:
        return None
    if rx.startswith("!"):
        return re.search(rx[1:], norm(tr), re.I) is None
    if rx.startswith("H:"):
        return re.search(rx[2:], norm(spans(tr, HMAC)), re.I) is not None
    if rx.startswith("M:"):
        return re.search(rx[2:], norm(spans(tr, MMAC)), re.I) is not None
    if rx.startswith("D:"):
        return re.search(rx[2:], norm(spans(tr, ("\\deleted{",))), re.I) is not None
    return re.search(rx, norm(tr), re.I | re.S) is not None


def main():
    res = results()
    rows = []
    for x in I:
        if x["key"] not in res:
            rows.append([x["key"], x["class"], x["desc"], "", "", "NO ANSWER"])
            continue
        sec = sections(res[x["key"]][0])
        tr = sec.get("TRANSCRIPTION", "")
        dl = sec.get("DIFFERENCES", "")
        d_ok = None if x["diff"] is None else re.search(x["diff"], norm(dl), re.I) is not None
        t_ok = test_trans(x["trans"], tr)
        rows.append([x["key"], x["class"], x["desc"], d_ok, t_ok, "caught" if (d_ok or t_ok) else "MISSED?"])
    with open(BASE / "pilot" / "pilot_auto.tsv", "w", encoding="utf-8") as f:
        f.write("key\tclass\tcheck_item\treported_in_differences\tpage_reading_in_transcription\tauto_verdict\n")
        for r in rows:
            f.write("\t".join(str(c) for c in r) + "\n")
    n = len(rows)
    c = sum(1 for r in rows if r[5] == "caught")
    print(f"{c}/{n} items caught automatically")
    for t in ("ps", "esq", "ega"):
        sub = [r for r in rows if r[0].startswith(t)]
        print(t, sum(1 for r in sub if r[5] == "caught"), "/", len(sub),
              "reported:", sum(1 for r in sub if r[3] is True), "transcribed:", sum(1 for r in sub if r[4] is True))
    for r in rows:
        if r[5] != "caught":
            print("  MISSED?", r[0], r[1], r[2])


if __name__ == "__main__":
    main()
