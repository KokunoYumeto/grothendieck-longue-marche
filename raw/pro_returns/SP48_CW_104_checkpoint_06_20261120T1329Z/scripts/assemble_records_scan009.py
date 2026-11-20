"""Text-only source crosswalk and staged records for scan 009.

This program reads current-page witness text, finalized reader returns, crop
metadata and main observations. It never opens images, decides ink, performs a
mathematical check, writes the selected page or authoritative decision.json,
compiles, or rebuilds cumulative records. Only numbered main observations may
supply a final choice. scan008 was consulted for record structure only.
"""
from pathlib import Path
from collections import Counter
import argparse
import copy
import hashlib
import json
import re

O = Path(__file__).resolve().parents[1]
P = O / "records/scan009"
PACKET = O.parent / "reader_inputs/scan009"
PAGE = O / "pages/H104-01_104_scan009.tex"

# Filled from the main reader's numbered observations, never from a vote.
MAIN_NUMBERS = {
    "folio":24,"opening_old_x":1,"opening_J1":1,"opening_clause_placement":1,"opening_J2":1,
    "opening_notation":1,"evaluation":24,"De":2,"plus":2,"fword_encore":2,
    "upper_brace":[3,4],"isom":3,"phantom_deleted":3,"upper_source_J":4,
    "upper_label":4,"upper_target_J":4,"upper_stop":4,"lorsque_n":3,"lorsque_J":5,
    "identity_J":6,"families_J":7,"families_register":[7,8,24],"rho":8,
    "family_pair_first":8,"family_pair_second":8,"category_replacement":9,
    "cancelled_approx":9,"cancelled_essential":9,"cancelled_il":10,"equiv":10,
    "pres_accent":10,"pres_stop":10,"condition_insertion":11,"description":11,
    "composer":12,"hom_1":13,"standart":13,"middle_J":14,"middle_ie":14,
    "paired_J_letter":15,"paired_J_second_index":15,"Donc":15,"situation":16,
    "diagram_eta_top":17,"diagram_xi_top":17,"diagram_membership_left":17,
    "diagram_membership_right":17,"diagram_J_left":17,"diagram_eta_arrow":17,
    "diagram_J_middle":17,"diagram_geometry":17,"diagram_J_right":17,"diagram_lower_row":17,
    "ondoit":24,"composite_eta1":18,"old_zeta":18,"composite_eta_arg":19,
    "composite_point":19,"composite_eta2":19,"composition_register":[18,19],
    "cancel_stability":20,"hom_lower":21,"entre":22,"lower_J":22,
    "M0_replacement":23,"cancel_final":23,"final_register":24,"final_hom":24,
    "final_J_source":24,"final_J_target":24,"final_layout":24,"archive":24,
}
def spec(final, confidence, diff_C, diff_H, kind, unresolved=False, alternatives=""):
    return {"final":final,"confidence":confidence,"diff_C":diff_C,"diff_H":diff_H,
            "kind":kind,"unresolved":unresolved,**({"alternatives":alternatives} if alternatives else {})}


SPECS = {
    "opening_old_x":spec(r"\deleted{x}\xi","medium",False,True,"deletion state"),
    "opening_J1":spec("J_n(n')","high",False,True,"misread symbol or index"),
    "opening_clause_placement":spec("Second i.e. clause continues on the original baseline without an insertion leader","high",False,True,"insertion or placement"),
    "opening_J2":spec("J_n","high",False,True,"misread symbol or index"),
    "opening_notation":spec("Two top i.e. abbreviations; xi first, ordinary x in the following membership and tau_n(x)=n-prime","high",False,False,"other"),
    "De":spec(r"\deleted{De}","high",False,True,"deletion state"),
    "plus":spec("plus,","medium",True,False,"deletion state"),
    "fword_encore":spec(r"\unsure{fort|faut|fut} encore,","low",False,True,r"readable ink left as \ill{}",True,"fort | faut | fut; no extra intervening word supplied"),
    "upper_brace":spec("Double low central notch and long rising right return; B's inline path with endpoint about y=1.45em; lower inserted phrase attached","high",True,True,"drawing or diagram"),
    "isom":spec("isom; no final point","medium",True,True,"abbreviation expanded or spelling modernised"),
    "phantom_deleted":spec("No independent canceled word between un and isom","high",False,True,"text not on the page"),
    "upper_source_J":spec("J_{n'}","high",False,True,"misread symbol or index"),
    "upper_label":spec("u_xi above tilde above right-pointing arrow","high",False,True,"omission"),
    "upper_target_J":spec(r"(J_n)_{\leq\xi}","high",False,True,"misread symbol or index"),
    "upper_stop":spec("No terminal period after target xi","high",False,True,"text not on the page"),
    "lorsque_n":spec("n'=n","high",True,False,"misread symbol or index"),
    "lorsque_J":spec(r"J_{n,n}=\{d_n\}","high",False,True,"misread symbol or index"),
    "identity_J":spec(r"\mathrm{id}_{J_n}","high",False,True,"misread symbol or index"),
    "families_J":spec(r"(J_n)_{n\in\mathbb N}","high",False,True,"misread symbol or index"),
    "rho":spec(r"\rho_{n,n'}","high",False,True,"misread symbol or index"),
    "family_pair_first":spec("n' as the first outer-pair member","high",False,True,"misread symbol or index"),
    "family_pair_second":spec(r"\deleted{\unsure{n'|m}}n","low",False,True,"deletion state",True,"older n-prime | m beneath live n"),
    "category_replacement":spec(r"\inserted{la catégorie}; following M remains live","high",False,True,"insertion or placement"),
    "cancelled_approx":spec(r"\deleted{à peu de \unsure{chose|choses} près}","low",False,True,r"readable ink left as \ill{}",True,"chose | choses; whole canceled phrase retained"),
    "cancelled_essential":spec(r"\deleted{essentiellement \unsure{la|le} sous-catégorie pleine}","low",False,True,r"readable ink left as \ill{}",True,"la | le; whole canceled phrase retained"),
    "cancelled_il":spec(r"\deleted{il}","high",True,True,"misread word"),
    "equiv":spec("équiv","medium",True,True,"abbreviation expanded or spelling modernised"),
    "pres_accent":spec(r"\unsure{prés|près}","low",True,True,"other",True,"prés | près; acute-looking mark first, grave still possible"),
    "pres_stop":spec("Comma after the près/pres word","high",False,True,"other"),
    "condition_insertion":spec(r"\inserted{condition}","high",False,False,"insertion or placement"),
    "description":spec(r"\deleted{\unsure{description|descripteur}}","low",False,True,r"readable ink left as \ill{}",True,"description | descripteur; covered final letters remain uncertain"),
    "composer":spec("pour composer","high",False,True,"misread word"),
    "hom_1":spec("hom; no s or abbreviation stop","high",False,True,"abbreviation expanded or spelling modernised"),
    "standart":spec("``standart; terminal t and no closing pair","high",True,True,"abbreviation expanded or spelling modernised"),
    "middle_J":spec("J_n","high",False,True,"misread symbol or index"),
    "middle_ie":spec("i.e; no final point before ceux","medium",False,True,"other"),
    "paired_J_letter":spec("J; first index n-prime","high",False,True,"misread symbol or index"),
    "paired_J_second_index":spec(r"J_{n',\unsure{n'|n^{4}|n}}","low",True,True,"misread symbol or index",True,"Second index n-prime | n^{4} | bare n; detached angular mark retained"),
    "Donc":spec(r"\deleted{Donc}","medium",True,False,"deletion state"),
    "situation":spec("On considère une situation","high",False,True,"misread word"),
}
MAIN_SOURCE_CONFIRMED = False
MAIN_SOURCE_CONFIRMATION = "Pending explicit main confirmation of source correspondence."
MATH_SOURCE_OBSERVATIONS = {}
EXPECTED_SELECTED_PAGE_SHA256 = ""
INVENTORY_VERIFIED = False
PAGE_REQUIRED = {}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def snapshot(path):
    data = path.read_bytes()
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def relpath(value, reader=None):
    p = Path(value)
    if p.is_absolute():
        return str(p.relative_to(O))
    if str(p).startswith(O.name + "/"):
        return str(p.relative_to(O.name))
    if reader and not str(p).startswith(("records/", "crops/scan")):
        return f"records/scan009/reader_{reader}/{p}"
    return str(p)


def load_inputs():
    reports, readings, logs, metadata = {}, {}, {}, {}
    for a in "ABC":
        q = P / f"reader_{a}"
        reports[a] = json.loads((q / "report.json").read_text())
        readings[a] = (q / "reading.tex").read_text()
        logs[a] = (q / "read_log.md").read_text()
        metadata[a] = json.loads((q / "crop_metadata.json").read_text())
        assert reports[a].get("finished_utc"), f"Reader {a} unfinished"
        assert logs[a].strip(), f"Reader {a} has no checked log"
        assert "Pending the single final comparison" not in logs[a], f"Reader {a} final comparison pending"
        assert r"\scanpage{9}" in readings[a]
        assert "% archive sheet number: 8" in readings[a]
    assert {a: len(reports[a]["issues"]) for a in "ABC"} == {"A": 41, "B": 43, "C": 45}
    issues = {a: {x["id"]: x for x in reports[a]["issues"]} for a in "ABC"}
    witnesses = {a: (PACKET / f"{a}.tex").read_text() for a in "CH"}
    doubts = json.loads((P / "witness_doubts.json").read_text())
    assert len(doubts["C"]) == 17 and len(doubts["H"]) == 4
    return reports, readings, logs, metadata, issues, witnesses, doubts, (PACKET / "C_context.md").read_text()


def get_main():
    p = P / "main_observations.md"
    text = p.read_text() if p.exists() else ""
    obs = {int(n): body.strip() for n, body in re.findall(
        r"^([0-9]+)\. (.*?)(?=\n[0-9]+\. |\Z)", text, re.M | re.S)}
    p = P / "main_crop_plan.json"
    plans = json.loads(p.read_text()) if p.exists() else []
    return text, obs, plans, {x["number"]: x for x in plans}


def same(text):
    return {a: text for a in "ABC"}


def refs(a=(), b=(), c=()):
    def f(prefix, values):
        if isinstance(values, int):
            values = [values]
        return [f"{prefix}{n:02d}" for n in values]
    return {"A": f("A", a), "B": f("B", b), "C": f("", c)}


def make_loci(witnesses):
    """Localized source readings; all final-selection fields remain separate."""
    C, H = witnesses["C"], witnesses["H"]
    hnote = H[H.index(r"\note{sur le feuillet"):H.index("\non doit avoir")].strip()
    hdiagram = H[H.index(r"\begin{tikzcd}"):H.index(r"\note{sur le feuillet")].strip()
    cdiagram = C[C.index(r"\diagram{"):C.index("\non doit avoir")].strip()
    rows = []

    def add(key, location, source, wc, wh, readings=None, role="physical_locus", note="", fallback=None):
        assert wc in C, (key, "C excerpt is not verbatim", wc)
        assert wh in H, (key, "H excerpt is not verbatim", wh)
        rows.append({"key": key, "location": location, "source_issues": source,
                     "witness_C": wc, "witness_H": wh, "local_readings": readings,
                     "role": role, "countable": role == "physical_locus",
                     "notes": [note] if note else [], "fallback": fallback or {}})

    def fallback(tex, log, interpretation):
        return {"reading_tex_anchor": tex, "read_log_anchor": log, "interpretation": interpretation}

    add("folio", "Own folio at top centre", refs(), r"\mspage{2}", r"\page{8}\note{sa page 2}", same("2; own handwritten folio"), "metadata_register",
        "H's page 8 and note sa page 2 are editorial metadata, not two inscriptions at the head.",
        {a: fallback(r"\mspage{2}", "folio", "Own folio 2") for a in "ABC"})
    add("opening_old_x", "First membership, older x under xi", refs(1, 1, 1), r"\deleted{x}\xi", r"\xi \in I_n(n')", same(r"\deleted{x}\xi"))
    add("opening_J1", "First membership, J_n(n-prime)", refs(1, 2, 2), "J_n(n')", "I_n(n')", same("J_n(n')"))
    add("opening_clause_placement", "Second i.e. clause, baseline placement", refs(2, 3, 3), r"i.e. \(x\in J_n,\ \tau_n(x)=n'\)", r"\add{i.e.\ $x \in I_n$, $\tau_n(x) = n'$}", same("Second i.e. clause on the original baseline; no insertion leader"),
        note="This compares placement only. Its J/I letter is counted at opening_J2.")
    add("opening_J2", "Second i.e. clause, object after x in", refs(2, 2, 2), r"x\in J_n", r"x \in I_n", same("J_n"))
    add("opening_notation", "Opening two i.e. abbreviations and xi/x/tau notation", refs(), r"i.e. on a, pour \(\deleted{x}\xi\in J_n(n')\) i.e. \(x\in J_n,\ \tau_n(x)=n'\)", r"i.e.\ on a, pour $\xi \in I_n(n')$ \add{i.e.\ $x \in I_n$, $\tau_n(x) = n'$}", same("Both top i.e. stops; xi first, ordinary x in the following membership and tau_n(x); n-prime"), "context_register",
        fallback={a: fallback(r"\tau_n(x)=n'", "First" if a == "A" else "membership", "Opening stops and xi/x distinction retained") for a in "ABC"})
    add("evaluation", "Opening evaluation identity", refs(), r"u_\xi(d_{n'})=\xi .", r"u_\xi(d_{n'}) = \xi.", same(r"u_\xi(d_{n'})=\xi ."), "context_register",
        fallback={a: fallback(r"u_\xi(d_{n'})=\xi .", "evaluation" if a != "B" else "normalization", "Full evaluation identity with terminal point") for a in "ABC"})
    add("De", "Canceled opening word De", refs(3, 4, 4), r"\deleted{De}", "De plus,", same(r"\deleted{De}"), note="A03 spans De and plus; it is localized into these two physical words, without a third broad row.")
    add("plus", "Opening plus and cancellation status", refs(3, 5, 5), r"\unsure{plus,|\deleted{plus,}}", "plus,", {"A": "plus,", "B": r"\unsure{plus,|\deleted{plus,}}", "C": "plus,"})
    add("fword_encore", "Uncertain f-word and readable encore before on a", refs(4, 6, 6), r"\unsure{fort|faut|fut} encore,", r"De plus, \ill{} on a :", same(r"\unsure{fort|faut|fut} encore,"),
        note="H01 is the single ill mark covering this local continuation. The readable encore is not counted again as a nested omission.")
    add("upper_brace", "Underbrace at on a and attached lower insertion", refs(5, 9, 7), r"\(\underbrace{\text{on a :}}\) \inserted{\(u_\xi\) induit un \unsure{isom|iso}}", r"on a : $u_\xi$ induit un",
        {"A": "Ordinary underbrace retained in TeX; log observes a long rising right return; attached lower insertion", "B": "Custom trace of notched brace with long rising right return and lower insertion", "C": "Custom trace of notched brace with long rising right return and lower insertion"},
        note="Insertion attachment and its brace form one physical annotation. The word isom and H's alleged old word are separately localized.")
    add("isom", "Last word of upper inserted phrase", refs(6, 7, 8), r"\unsure{isom|iso}", "isomorphisme", same("isom; no final point"),
        note="Reader C08 combines abbreviation and adjacent alleged cancellation; H's ill belongs to phantom_deleted, so isom itself is unmarked in H.")
    add("phantom_deleted", "Gap between un and isom", refs(7, 8, 8), r"un \unsure{isom|iso}", r"un \struck{\ill{}} isomorphisme", same("No independent canceled word between un and isom"))
    add("upper_source_J", "Upper isomorphism, source object", refs(8, 10, 9), r"J_{n'}\xrightarrow", r"I_{n'} \overset{\sim}", same("J_{n'}"))
    add("upper_label", "Upper isomorphism, u_xi above tilde", refs(8, 10, 9), r"\xrightarrow{\overset{u_\xi}{\sim}}", r"\overset{\sim}{\longrightarrow}", same("u_xi above tilde above right-pointing arrow"))
    add("upper_target_J", "Upper isomorphism, parenthesized target object", refs(8, 10, 9), r"(J_n)_{\leq\xi}", r"(I_n)_{\leq \xi}", same(r"(J_n)_{\leq\xi}"))
    add("upper_stop", "Right of upper isomorphism target", refs(8, 10, 9), r"(J_n)_{\leq\xi}\)", r"(I_n)_{\leq \xi}$.", same("No terminal point"))
    add("lorsque_n", "Lorsque, first n and its prime", refs(9, 11, 10), r"\unsure{n'|n}=n", "n' = n", same("n'=n"))
    add("lorsque_J", "Lorsque, singleton object J_{n,n}", refs(10, 11, 11), r"J_{n,n}=\{d_n\}", r"I_{n,n} = \{d_n\}", same(r"J_{n,n}=\{d_n\}"))
    add("identity_J", "Identity display, target of id", refs(11, 12, 12), r"\mathrm{id}_{J_n}", r"\mathrm{id}_{I_n}", same(r"\mathrm{id}_{J_n}"))
    add("families_J", "La connaissance, first indexed family", refs(12, 13, 13), r"(J_n)_{n\in\mathbb N}", r"(I_n)_{n \in \mathbb{N}}", same(r"(J_n)_{n\in\mathbb N}"))
    add("families_register", "La connaissance, N and tau family", refs(), r"\mathbb N,\ (J_n)_{n\in\mathbb N},\ (\tau_n)_{n\in\mathbb N}", r"\mathbb{N}$, $(I_n)_{n \in \mathbb{N}}$,\n$(\tau_n)_{n \in \mathbb{N}}$".replace(r"\n", "\n"), same(r"\mathbb N and (\tau_n)_{n\in\mathbb N}; doubled/barred N"), "context_register",
        fallback={a: fallback(r"(\tau_n)_{n\in\mathbb N}", "La connaissance", "N and tau family checked independently") for a in "ABC"})
    add("rho", "Map-family letter rho", refs(13, 14, 14), r"\rho_{n,n'}", r"\varphi_{n,n'}", same(r"\rho_{n,n'}"))
    add("family_pair_first", "Map-family indexing pair, first member", refs(14, 14, 14), r"(n',\deleted{\unsure{n'|m}}n)", r"(n,n') \in \mathbb{N}", same("n' as first pair member"))
    add("family_pair_second", "Map-family indexing pair, overwritten second member", refs(14, 14, 15), r"\deleted{\unsure{n'|m}}n", r"(n,n') \in \mathbb{N}", same(r"\deleted{\unsure{n'|m}}n"),
        note="Overwritten older ink and live second member form one physical cluster. No additional broad pair-omission row is counted.")
    add("category_replacement", "Raised la catégorie above reconstruction cancellation", refs(17, 17, 18), r"\inserted{la catégorie}", "la catégorie", same(r"\inserted{la catégorie}; following M and à live"))
    add("cancelled_approx", "First long canceled reconstruction phrase", refs(15, 15, 16), r"\deleted{à peu de \unsure{chose|choses} près}", r"\struck{\ill{}} la catégorie", same(r"\deleted{à peu de \unsure{chose|choses} près}"),
        note="H03 spans both physical canceled phrases. Each phrase counts once; its nested singular/plural doubt does not create a second count.")
    add("cancelled_essential", "Second long canceled reconstruction phrase", refs(16, 16, 17), r"\deleted{essentiellement \unsure{la|le} sous-catégorie pleine}", r"\struck{\ill{}} la catégorie", same(r"\deleted{essentiellement \unsure{la|le} sous-catégorie pleine}"),
        note="The nested la/le doubt belongs to this whole canceled phrase and is not counted twice.")
    add("cancelled_il", "Short canceled fragment before équiv", refs(18, 18, 19), r"\deleted{\unsure{il|à}}", r"\struck{l'équi}", same(r"\deleted{il}"))
    add("equiv", "Live abbreviation équiv", refs(19, 19, 20), r"\unsure{équiv|équiva}", "équivalence", same("équiv"))
    add("pres_accent", "Accent on près after équiv", refs(20, 20, 21), "près, il manque", "près ; il manque", {"A": "près", "B": r"\unsure{prés|près}", "C": "près"},
        note="B20 introduces an acute/grave doubt. A20/C21 quote près and their complete text/logs retain it; this is distinct from the following punctuation.")
    add("pres_stop", "Punctuation after près", refs(20, 20, 21), "près, il manque", "près ; il manque", same("Comma after près"))
    add("condition_insertion", "Raised condition replacing old noun", refs(21, 21, 22), r"\inserted{condition}", r"\add{condition}", same(r"\inserted{condition}"), "context_register",
        note="All witnesses represent the insertion; this is a checked, noncounted context place beside its canceled parent word.")
    add("description", "Canceled noun beneath condition", refs(21, 21, 22), r"\deleted{\unsure{description|descripteur}}", r"\struck{\ill{}} \add{condition}", {"A": r"\deleted{description}", "B": r"\deleted{\unsure{description|descripteur}}", "C": r"\deleted{\unsure{description|descripteur}}"})
    add("composer", "Verb following pour", refs(22, 22, 23), "pour composer", "pour comprendre", same("pour composer"))
    add("hom_1", "First hom abbreviation", refs(23, 23, 24), "les hom", "les homs.", same("hom without s or stop"))
    add("standart", "Quoted designation at right edge", refs(24, 23, 25), r"``\unsure{standart|standard}", "« standard »", same("``standart; two opening ticks, terminal t, no closing ticks"),
        note="Spelling and enclosing marks belong to this one physical designation; no separate broad quote-omission row.")
    add("middle_J", "Object after entre les", refs(25, 24, 26), r"entre les \(J_n\)", "entre\nles $I_n$", same("J_n"))
    add("middle_ie", "Middle i.e before ceux", refs(26, 24, 27), "i.e ceux", r"i.e.\ ceux", same("i.e without final stop"))
    add("paired_J_letter", "Inline family before Donc, object letter", refs(27, 25, 28), r"J_{n',\unsure{n|n'}}", "I_{n',n}", same("J"))
    add("paired_J_second_index", "Inline family before Donc, second index", refs(27, 25, 28), r"J_{n',\unsure{n|n'}}", "I_{n',n}", {"A": r"J_{n',\unsure{n'|n^{4}|n}}", "B": "J_{n',n'}", "C": "J_{n',n'}"},
        note="A27's extra n^{4} candidate is explicitly retained as a reader interpretation. Main alone decides whether the high angular mark is a prime, a 4-like form or extraneous.")
    add("Donc", "Canceled word before On considère", refs(28, 26, 29), r"\deleted{\unsure{Donc|Don}}", r"\struck{Donc}", same(r"\deleted{Donc}"))
    add("situation", "Clause introducing diagram", refs(29, 27, 30), "On considère une situation", "On considère\nleurs compositions", same("On considère une situation"))
    add("diagram_eta_top", "Diagram, eta above middle object", refs(30, 29, (31,33)), r"\& \& \eta \& \& \xi", hnote, same(r"\eta above middle object"),
        note="H's note calls this y and does not draw it. The arrow-subscript eta is a separate physical character.")
    add("diagram_xi_top", "Diagram, xi above right object", refs(30, (), 33), r"\& \& \eta \& \& \xi", hnote, same(r"\xi above right object"),
        note="H acknowledges xi in its note but omits the actual upper-row placement.",
        fallback={"B": fallback(r"\& \xi\\[-.8em]", "top eta/xi", "xi placed above right object")})
    add("diagram_membership_left", "Diagram, turned membership over middle object", refs(31, 30, (33, 34)), r"\rotatebox{90}{\(\in\)}", hnote, same(r"\rotatebox{-90}{\(\in\)}; downward-open arch"))
    add("diagram_membership_right", "Diagram, turned membership over right object", refs(31, 30, (33, 34)), r"\rotatebox{90}{\(\in\)}", hnote, same(r"\rotatebox{-90}{\(\in\)}; downward-open arch"))
    add("diagram_J_left", "Diagram, left object", refs(30, 28, 32), "J_{n''}", "I_{n''}", same("J_{n''}"))
    add("diagram_eta_arrow", "Diagram, first-arrow subscript eta", refs(30, 29, 31), r"u^{n'}_{\eta}", r"u_y^{n'}", same(r"u^{n'}_{\eta}"))
    add("diagram_J_middle", "Diagram, middle object", refs(30, 28, 32), r"J_{n'}\arrow", r"I_{n'} \arrow", same("J_{n'}"))
    add("diagram_geometry", "Diagram, unequal arrow spans and crossing second label", refs(32, 32, 35), cdiagram, hdiagram,
        {"A": "Longer second interval; second label at pos=.35 with description,yshift=.8ex; 1.4em before order row", "B": "Longer second interval; first/second labels pos=.32/.27, second yshift=-.3em; .5em before order row", "C": "Longer second interval; second label yshift=-1.1ex; ordinary order-row spacing"},
        note="All readers report unequal shafts and the second xi descender crossing its shaft, but their returned geometric approximations differ. No consensus on exact code is inferred.")
    add("diagram_J_right", "Diagram, right object", refs(30, 28, 32), r"\& \& J_n", "& I_n", same("J_n"))
    add("diagram_lower_row", "Diagram, lower n-double-prime <= n-prime <= n row", refs(32, 31, 33), r"n'' \& \leq \& n' \& \leq \& n", hnote, same("n'' <= n' <= n below corresponding objects; no separate canceled predecessor at middle n'"),
        note="H's note acknowledges the row; its diagram omits it. Membership-sign differences are counted only at the two sign rows.")
    add("ondoit", "Formula introduction beneath diagram", refs(), "on doit avoir", "on doit avoir", same("on doit avoir"), "context_register",
        fallback={a: fallback("on doit avoir", "on doit avoir", "on doit avoir") for a in "ABC"})
    add("composite_eta1", "Composite display, eta in left product", refs(33, 34, 36), r"u_\xi^n\,u_\eta^{n'}", r"u_\xi^n\, u_y^{n'}", same(r"u_\eta^{n'}"))
    add("old_zeta", "Older subscript beneath result zeta", refs(34, 33, 37), r"\deleted{\unsure{\xi|a}}\zeta", r"u_\zeta^n", same(r"\deleted{\unsure{a|\xi}}\zeta"))
    add("composite_eta_arg", "Evaluation display, eta argument", refs(33, 34, 36), r"u_\xi^n(\eta)", r"u_\xi^n(y)", same(r"\eta"))
    add("composite_point", "Separate point above-right of later equality", refs((), 35, ()), r"u_\xi^n(\eta)=", r"u_\xi^n(y) =", {"A": "No separate point encoded in returned equality; no standalone point issue", "B": "Separate small point traced above-right of equality, without a mathematical role", "C": "No separate point encoded in returned equality; no standalone point issue"},
        note="Only B35 reports this point separately. A/C's complete texts omit a point; omission of an issue is not reported as a visual denial or consensus. C's contextual audit mentions a nearby speck.",
        fallback={"A": fallback(r"u_\xi^n(\eta)=", "Composition display", "No separate point encoded"), "C": fallback(r"u_\xi^n(\eta)=", "Lower evaluation equality", "No separate point encoded")})
    add("composite_eta2", "Evaluation display, eta in right product", refs(33, 34, 36), r"(u_\xi^n\,u_\eta^{n'})(d_{n''})", r"(u_\xi^n\, u_y^{n'})(d_{n''})", same(r"u_\eta^{n'}"))
    add("composition_register", "Composite display, remaining xi/zeta/d and equality notation", refs(), r"\qquad\text{où}\quad \zeta=u_\xi^n(\eta)=", r"\qquad \text{où } \zeta = u_\xi^n(y) =", same("xi/zeta distinct; exponents n/n-prime; d_{n-double-prime}; parentheses and equality bars checked"), "context_register",
        fallback={a: fallback(r"(d_{n''})", "display" if a != "C" else "equality", "Remaining composition-display notation checked") for a in "ABC"})
    add("cancel_stability", "Canceled word before live stabilité", refs(35, 36, 38), r"\deleted{\unsure{stabilité|composition|stabilis}}", r"\struck{compatibilité}", {"A": r"\deleted{\unsure{composition|stabilité|stabilis}}", "B": r"\deleted{\unsure{composition|stabilité|compatibilité|stabilis}}", "C": r"\deleted{\unsure{stabilité|composition|stabilis}}"})
    add("hom_lower", "Lower prose, hom admissible endings", refs(36, 37, 39), "d'hom admissible", "d'homs.\\\nadmissibles", same("d'hom admissible; singular without abbreviation point"))
    add("entre", "Lower prose, entre and adjacent point", refs(37, 38, 40), r"\unsure{entre|entre.}", "pour les", {"A": "entre.", "B": "entre.", "C": r"\unsure{entre.|entre}"},
        note="The point's uncertain presence belongs to this local word/punctuation cluster and is not a second omitted-passage count.")
    add("lower_J", "Lower prose, J before par composition", refs(38, 39, 41), r"\(J_n\) par composition.", "$I_n$ par composition.", same("J_n"))
    add("M0_replacement", "Raised Soit M_0 introduction", refs(40, 41, 43), r"\inserted{Soit \(M_0\) la catégorie définie par}", "Soit $M_0$ la catégorie définie par", same(r"\inserted{Soit \(M_0\) la catégorie définie par}"))
    add("cancel_final", "Final canceled sentence ending", refs(39, 40, 42), r"\deleted{Il est évident que la \unsure{catég|caté}}", r"\struck{Il est évident que la cat.}", same(r"\deleted{Il est évident que la \unsure{catég|caté}}"))
    add("final_register", "Final definition, Ob/M_0/N/Hom and case relations", refs(), r"\mathrm{Ob}\,M_0=\mathbb N,\quad \mathrm{Hom}_{M_0}(n',n)=", "\\mathrm{Ob}\\,M_0 = \\mathbb{N},\n\\qquad\n\\mathrm{Hom}_{M_0}(n', n) =", same("Ob M_0=N; Hom_{M_0}(n',n); slashed empty set and n' not<=n, then n'<=n"), "context_register",
        fallback={a: fallback(r"\varnothing\ \text{si }n'\nleq n", "Final" if a != "B" else "Final object", "Final alphabets, brace, empty-set slash and two inequalities checked") for a in "ABC"})
    add("final_hom", "Second case, hom abbreviation", refs(41, 42, 44), r"\text{ens. des hom. admissibles}", r"\text{ens.\ des homs.\ admissibles }", same("ens. des hom. admissibles; no s in hom"))
    add("final_J_source", "Second case, source J_n-prime", refs(41, 42, 45), r"J_{n'}\to J_n", r"I_{n'} \to I_n", same("J_{n'}"))
    add("final_J_target", "Second case, target J_n", refs(41, 42, 45), r"J_{n'}\to J_n", r"I_{n'} \to I_n", same("J_n"))
    add("final_layout", "Second case, two-line arrangement", refs(41, 43, 45), "&\\text{ens. des hom. admissibles}\\\\\n &\\qquad J_{n'}\\to J_n\\quad\\text{si }n'\\leq n", r"\text{ens.\ des homs.\ admissibles } I_{n'} \to I_n & \text{si } n' \leq n", same("ens. des hom. admissibles on its own line; J-to-J map and condition below"),
        note="Only line arrangement is counted here. Abbreviation and two physical object letters have their own localized rows.")
    add("archive", "Archive numeral at lower left", refs(), "% archive sheet number: 8", r"\page{8}", same("8; archive numeral"), "metadata_register",
        note="Inventory kind text; hand unattributed archival hand. This is separate from own folio 2.",
        fallback={a: fallback("% archive sheet number: 8", "archive" if a != "A" else "Archive", "Archive numeral 8") for a in "ABC"})
    return rows


C_DOUBT_KEYS = ["plus", "fword_encore", "isom", "lorsque_n", "family_pair_second", "cancelled_approx", "cancelled_essential", "cancelled_il", "equiv", "description", "standart", "paired_J_second_index", "Donc", "old_zeta", "cancel_stability", "entre", "cancel_final"]
H_DOUBT_KEYS = [["fword_encore"], ["phantom_deleted"], ["cancelled_approx", "cancelled_essential"], ["description"]]
H_MARKED_KEYS = {k for keys in H_DOUBT_KEYS for k in keys}


def build_inventory(reports):
    """Union source inventory without duplicating uncertain deletion states."""
    bmap = {1:[1],2:[2],3:[3],4:[4],5:[10],6:[5,7],7:[6],8:[8],9:[11],10:[12],11:[13,18,22],12:[14],13:[17],14:[15],15:[16],16:[19],17:[20],18:[21],19:[23],20:[24],21:[25],22:[26],23:[27],24:[28],25:[29],26:[30],27:[31],28:[32],29:[33]}
    cmap = {1:1,2:2,3:3,4:4,5:8,6:5,7:6,8:7,9:9,10:10,11:11,12:12,13:15,14:13,15:14,16:16,17:18,18:17,19:19,20:20,21:21,22:22,23:23,24:24,25:25,26:26,27:27,28:28,29:29}
    rows = []
    for n, item in enumerate(reports["A"]["inventory"], 1):
        row = copy.deepcopy(item)
        row.update(element=f"E{n:02d}: {item['element']}", transcribed="pending", source_inventory_rows={"A":[n],"B":bmap[n],"C":[cmap[n]]})
        if n == 6:
            row["element"] = "E06: upper prose and plus cancellation-status candidate"
            row["first_words_or_objects"] = "De plus, fort/faut/fut encore, on a :; plus cancellation status disputed"
            row["coverage_note"] = "B's plus_cluster is this physical word once, with disputed cancellation status; no additional definite deletion is invented. The distinct brace drawing is E31 beside this parent. A's source row combines prose and brace."
        if n == 22:
            row["coverage_note"] = "The separate point reported only by B35 is inventoried immediately beside this parent display, not at the end of the page."
        if n == 29:
            row.update(kind="text", hand="unattributed archival hand", first_words_or_objects="8 (archive numeral)")
        row["reader_inventory"] = {a:[copy.deepcopy(reports[a]["inventory"][i-1]) for i in row["source_inventory_rows"][a]] for a in "ABC"}
        rows.append(row)
        if n == 7:
            rows.append({"element":"E31: brace beneath on a with rising return", "kind":"drawing", "position":"beneath on a with a return rising beside the upper isomorphism; B inventory row9", "first_words_or_objects":"notched brace with long rising right return", "sheet_kind":"text", "hand":"his hand", "transcribed":"pending", "source_inventory_rows":{"A":[],"B":[9],"C":[]}, "reader_inventory":{"A":[],"B":[copy.deepcopy(reports['B']['inventory'][8])],"C":[]}, "coverage_note":"Distinct physical annotation from B9, placed beside the upper prose/insertion. A6 and C7 describe it within compound parent entries; those source entries are mapped once to their parents, with the relationship recorded here."})
        if n == 22:
            rows.append({"element":"E30: point beside composite equality", "kind":"drawing", "position":"above-right of later equality in the lower composition display; B35 bbox", "first_words_or_objects":"separate small point; status awaits main", "sheet_kind":"text", "hand":"his hand", "transcribed":"pending", "source_inventory_rows":{"A":[],"B":[],"C":[]}, "source_issue_rows":{"A":[],"B":["B35"],"C":[]}, "reader_inventory":{"A":[],"B":[],"C":[]}, "coverage_note":"B35 and B's complete text/log supply this candidate mark although B's inventory omits a separate row. A/C have no encoded point. Main determines its final status; do not infer a consensus."})
    for n, row in enumerate(rows, 1):
        row["physical_order"] = n
    for a in "ABC":
        covered = [i for row in rows for i in row["source_inventory_rows"][a]]
        assert sorted(covered) == list(range(1, len(reports[a]["inventory"])+1)), (a, covered)
    return rows


def build_context(context, bykey):
    specs = [
        ("CTX01", "Xi/eta/zeta, d and arrow direction", ["opening_old_x","opening_notation","evaluation","upper_label","upper_target_J","diagram_eta_top","diagram_xi_top","diagram_eta_arrow","composite_eta1","old_zeta","composite_eta_arg","composite_eta2","composition_register"]),
        ("CTX02", "N/M/M_0 and J/tau/rho alphabets", ["families_J","families_register","rho","family_pair_first","family_pair_second","category_replacement","M0_replacement","final_register","final_J_source","final_J_target"]),
        ("CTX03", "Abbreviations, stops and opening quotation", ["opening_notation","identity_J","isom","equiv","hom_1","standart","middle_ie","hom_lower","final_register","final_hom"]),
        ("CTX04", "Final empty-set slash and inequalities", ["final_register","final_layout"]),
        ("CTX05", "First xi and later ordinary x occurrences", ["opening_old_x","opening_J1","opening_clause_placement","opening_J2","opening_notation"]),
        ("CTX06", "F-word before encore without supplied extra word", ["fword_encore"]),
        ("CTX07", "Unmatched opening ticks and terminal t", ["standart"]),
        ("CTX08", "Final Ob/Hom notation and cases", ["final_register","final_hom","final_J_source","final_J_target","final_layout"]),
        ("CTX09", "Own folio and archive numeral", ["folio","archive"]),
        ("CTX10", "Current C audit corrections, placements and equality speck", ["De","plus","upper_brace","family_pair_second","category_replacement","cancelled_approx","cancelled_essential","cancelled_il","description","condition_insertion","Donc","diagram_membership_left","diagram_membership_right","diagram_lower_row","old_zeta","composite_point","cancel_stability","entre","M0_replacement","cancel_final"]),
    ]
    checks = [{"id":i,"topic":topic,"locus_keys":keys,"locus_ids":[bykey[k]["id"] for k in keys],"coverage":"Mapped to localized reader interpretations and numbered main decisions when available.","source":"reader_inputs/scan009/C_context.md","status":"reader coverage complete; main pending"} for i, topic, keys in specs]
    raw_rows = []
    for n, line in enumerate(context.splitlines(), 1):
        if line.startswith("|"):
            raw_rows.append({"id":f"CT{len(raw_rows)+1:02d}","line":n,"raw":line})
    assert len(raw_rows) == 26, len(raw_rows)
    for i, row in enumerate(raw_rows):
        if i < 4:
            row.update(context_check_ids=[checks[i]["id"]], locus_keys=checks[i]["locus_keys"])
        elif i < 21:
            row.update(C_doubt_id=f"C{i-3:02d}", locus_keys=[C_DOUBT_KEYS[i-4]])
        elif i < 25:
            row.update(context_check_ids=[checks[i-17]["id"]], locus_keys=checks[i-17]["locus_keys"])
        else:
            row.update(context_check_ids=["CTX09"], locus_keys=["folio","archive"])
        row["locus_ids"] = [bykey[k]["id"] for k in row["locus_keys"]]
    return checks, raw_rows


def build_crosswalk(data):
    reports, readings, logs, metadata, issues, witnesses, doubts, context = data
    _, main, plan_list, plan = get_main()
    rows = make_loci(witnesses)
    source_map = {a:{k:[] for k in issues[a]} for a in "ABC"}
    for n, row in enumerate(rows, 1):
        row["id"] = f"009L{n:02d}"
        row["physical_order"] = n
        local = row.pop("local_readings")
        row["readers"] = copy.deepcopy(local) if local is not None else {}
        row["reader_report_readings"] = {}
        row["reader_provenance"] = {}
        row["reader_crop_options"] = []
        row["reported_bboxes"] = {}
        for a in "ABC":
            rr = row["source_issues"][a]
            assert all(k in issues[a] for k in rr), (row["key"], a, rr)
            for k in rr:
                source_map[a][k].append(row["id"])
            row["reader_report_readings"][a] = [{"id":k,"reading":issues[a][k]["reading"]} for k in rr]
            row["reported_bboxes"][a] = [{"id":k,"bbox":issues[a][k].get("bbox",[])} for k in rr]
            if rr:
                row["reader_provenance"][a] = {"source":"report issue(s), localized to this physical place","file":f"records/scan009/reader_{a}/report.json","ids":rr}
                if a not in row["readers"]:
                    row["readers"][a] = "; ".join(issues[a][k]["reading"] for k in rr)
            else:
                fb = row["fallback"].get(a)
                assert fb, (row["key"], a, "missing full-text/log provenance")
                assert fb["reading_tex_anchor"] in readings[a], (row["key"], a, "text anchor")
                assert fb["read_log_anchor"].lower() in logs[a].lower(), (row["key"], a, "log anchor")
                row["reader_provenance"][a] = {"source":"complete returned text and checked log; no standalone issue","reading_file":f"records/scan009/reader_{a}/reading.tex","log_file":f"records/scan009/reader_{a}/read_log.md",**fb}
            for k in rr:
                cp = issues[a][k].get("crop")
                if cp:
                    item = {"reader":a,"path":relpath(cp,a),"source_issue":k}
                    if item not in row["reader_crop_options"]:
                        row["reader_crop_options"].append(item)
        row.pop("fallback")
        row["C_doubts"] = []
        number = MAIN_NUMBERS.get(row["key"])
        ns = number if isinstance(number, list) else [number] if number else []
        row["main_plan_numbers"] = ns
        row["planned_main_crops"] = [plan[n]["path"] for n in ns if n in plan]
        row["main_adjudication_status"] = "main observation recorded; decision staged" if row["key"] in SPECS and ns and all(n in main for n in ns) else "pending; text assembler makes no ink choice"
        row["marked_in_H"] = "yes" if row["key"] in H_MARKED_KEYS else "no"
    assert all(ids for sm in source_map.values() for ids in sm.values()), source_map
    bykey = {x["key"]:x for x in rows}
    cd = []
    for d, key in zip(doubts["C"], C_DOUBT_KEYS):
        row = bykey[key]
        row["C_doubts"].append(d["id"])
        cd.append({**copy.deepcopy(d),"locus_key":key,"locus_id":row["id"],"readers":copy.deepcopy(row["readers"]),"status":"pending main adjudication","counting_note":"Removal, refinement or reordering of this C doubt is a change; it is counted at the physical parent only."})
    hd = [{**copy.deepcopy(d),"locus_keys":keys,"locus_ids":[bykey[k]["id"] for k in keys],"status":"pending main adjudication"} for d, keys in zip(doubts["H"], H_DOUBT_KEYS)]
    checks, raw_context = build_context(context, bykey)
    catalog = []
    for a in "ABC":
        source = metadata[a].get("crops", []) if isinstance(metadata[a], dict) else metadata[a]
        for item in source:
            entry = copy.deepcopy(item)
            entry.update(reader=a,path=relpath(item.get("path",item.get("file")),a),catalog_id=f"R{len(catalog)+1:02d}")
            catalog.append(entry)
    input_paths = [PACKET/"C.tex",PACKET/"H.tex",PACKET/"C_context.md",PACKET/"page.json",P/"witness_doubts.json"]
    input_paths += [P/f"reader_{a}"/f for a in "ABC" for f in ["report.json","reading.tex","read_log.md","crop_metadata.json"]]
    cw = {"scan":9,"folder":"H104-01","status":"complete reader source crosswalk; main decisions and selected-page verification pending","loci":rows,"source_issue_index":issues,"source_issue_map":source_map,"source_reports":reports,"complete_reader_readings":readings,"complete_reader_logs":logs,"reader_crop_metadata":metadata,"reader_crop_catalog":catalog,"reader_checks":{a:copy.deepcopy(reports[a].get("checks",[])) for a in "ABC"},"C_doubt_map":cd,"H_doubt_map":hd,"contextual_C_checks":checks,"context_table_rows":raw_context,"inventory_crosswalk":build_inventory(reports),"input_snapshots":{str(p.relative_to(O.parent)):snapshot(p) for p in input_paths},"counts":{"source_issues":sum(len(issues[a]) for a in "ABC"),"by_reader":{a:len(issues[a]) for a in "ABC"},"physical_loci":sum(x["countable"] for x in rows),"noncounted_registers":sum(not x["countable"] for x in rows),"C_inline_doubts":17,"H_doubt_marks":4,"context_table_rows":26,"reader_crops":{a:reports[a]["crop_count"] for a in "ABC"}},"counting_policy":"Each physical comparison place counts at most once against C and once against H. Broad reader issues may map to several distinct letters or layout places, but no broad duplicate row is retained. Whole canceled phrases include their nested doubtful endings/articles. Doubt removal, refinement and reordering count as changes. Equivalent TeX macros or ordinary spacing do not. H doubt flags follow the actual four ill marks, not nearby reader paraphrases. Noncounted context/metadata registers have no discrepancy counts.","inventory_count_note":"All A29/B33/C29 inventory entries map once to physical parents. B's disputed plus cancellation is inventoried once as text with uncertain status; its separate brace drawing is beside the parent annotation. B35's extra point is adjacent to the lower display. The union has31 physical entries. Archive8 is text in an unattributed archival hand.","assembly_next_step":"Main must observe all planned crops, supply numbered choices, confirm original mathematical source correspondence, install the selected page and verify inventory."}
    return cw


def mdcell(value):
    return str(value).replace("|", "&#124;").replace("\n", "<br>")


def write_crosswalk_md(cw):
    c = cw["counts"]
    lines = ["# Scan 009 — reader source crosswalk", "", f"Text-only collation: {c['source_issues']} source issues (A41/B43/C45), 17 inline C doubts, four actual H ill marks, 26 current-context table rows, {c['physical_loci']} countable physical places and {c['noncounted_registers']} noncounted context/metadata registers.", "", cw["counting_policy"], "", "All H cells below are verbatim excerpts from the supplied H.tex. Omission/placement explanations are separate notes. A missing standalone issue is filled from that reader's complete returned text and checked log with explicit provenance, never from the other readers.", "", "## Reader differences requiring main attention", "", "- Plus cancellation: A/C select live plus; B retains both states.", "- The brace has a long rising return in B/C's code; A's log observes it but A's code retains the ordinary underbrace.", "- B introduces prés/près; A/C retain près. A resolves description; B/C retain description/descripteur.", "- A27 retains n-prime / n^{4} / bare n for the second paired-family index; B/C choose n-prime.", "- B35 alone draws a separate point above-right of the later equality. A/C's text omits a separate point, without an explicit visual denial.", "- The canceled stability word has three reordered alternatives in A, four in B, and C's original three in C. A/B select entre.; C retains entre./entre.", "", "## Physical comparison places", "", "| Key | Place | Witness C | Witness H (verbatim) | Reader A | Reader B | Reader C | Source issues |", "|---|---|---|---|---|---|---|---|"]
    for x in cw["loci"]:
        src = "; ".join(a+": "+(", ".join(x["source_issues"][a]) or "complete text/log") for a in "ABC")
        vals = [x["key"],x["location"],x["witness_C"],x["witness_H"],*[x["readers"][a] for a in "ABC"],src]
        lines.append("| " + " | ".join(mdcell(v) for v in vals) + " |")
    lines += ["", "## Every C doubt", "", "| ID | Exact alternatives | Physical key | Status |", "|---|---|---|---|"]
    for x in cw["C_doubt_map"]:
        lines.append("| "+" | ".join(mdcell(x[k]) for k in ["id","reading","locus_key","status"])+" |")
    lines += ["", "## Every H doubt mark", "", "| ID | Actual macro | Physical keys |", "|---|---|---|"]
    for x in cw["H_doubt_map"]:
        lines.append("| "+" | ".join(mdcell(v) for v in [x["id"],"\\"+x["macro"]+"{"+x["reading"]+"}",", ".join(x["locus_keys"])])+" |")
    lines += ["", "## Context coverage", ""]
    for x in cw["contextual_C_checks"]:
        lines.append(f"- **{x['id']} — {x['topic']}**: {', '.join(x['locus_keys'])}.")
    lines += ["", "## Inventory union in physical order", "", cw["inventory_count_note"], "", "| Order | Element | Kind | A/B/C source rows | Status |", "|---|---|---|---|---|"]
    for x in cw["inventory_crosswalk"]:
        src = " / ".join(",".join(map(str,x["source_inventory_rows"][a])) or "—" for a in "ABC")
        lines.append("| "+" | ".join(mdcell(v) for v in [x["physical_order"],x["element"],x["kind"],src,x["transcribed"]])+" |")
    lines += ["", "Reader A records no mathematical checks. B records one targeted conditional evaluation check; C records its background assumption and one targeted conditional check. These actual events are preserved unchanged. The six original main events are imported only after explicit source confirmation. This assembler performs no proof, audit or re-proof.", ""]
    (P/"reader_crosswalk.md").write_text("\n".join(lines))


def check_selected_page(cw):
    if not PAGE.exists():
        return {"passed":False,"status":"pending selected page","errors":["Selected page not installed."]}
    text = PAGE.read_text()
    sha = snapshot(PAGE)["sha256"]
    errors = []
    if not EXPECTED_SELECTED_PAGE_SHA256:
        errors.append("Main-confirmed selected-page hash pending.")
    elif sha != EXPECTED_SELECTED_PAGE_SHA256:
        errors.append("Selected page differs from the confirmed main version.")
    if not INVENTORY_VERIFIED:
        errors.append("Selected-page inventory verification pending.")
    if not PAGE_REQUIRED:
        errors.append("Numbered main-choice text guards pending.")
    guards = []
    for key, parts in PAGE_REQUIRED.items():
        missing = [s for s in parts if s not in text]
        guards.append({"key":key,"passed":not missing,"missing":missing})
        if missing:
            errors.append(f"Missing selected main text for {key}.")
    return {"passed":not errors,"status":"passed" if not errors else "pending/failed selected-text validation","sha256":sha,"errors":errors,"main_guards":guards,"inventory_verified":INVENTORY_VERIFIED}


def math_events(cw, main):
    actual = []
    for a in "ABC":
        for i, raw in enumerate(cw["reader_checks"][a], 1):
            event = copy.deepcopy(raw)
            event.update(source_file=f"records/scan009/reader_{a}/report.json",source_event_index=i,source_sha256=snapshot(P/f"reader_{a}"/"report.json")["sha256"])
            report = cw["source_reports"][a]
            event.setdefault("date",report["finished_utc"])
            event.setdefault("who",f"{report['model']}; effort {report['effort']}; independent reader {a}, scan009")
            event["date_provenance"] = "Reader report completion timestamp; exact mathematical-check time not supplied."
            actual.append(event)
    if MAIN_SOURCE_CONFIRMED:
        data = json.loads((P/"math_checks.json").read_text())
        assert len(data["events"]) == 6
        for i, raw in enumerate(data["events"], 1):
            ns = MATH_SOURCE_OBSERVATIONS.get(raw["statement_id"], [])
            assert ns and all(n in main for n in ns), (raw["statement_id"], ns)
            event = copy.deepcopy(raw)
            event.update(source_file="records/scan009/math_checks.json",source_event_index=i,source_sha256=snapshot(P/"math_checks.json")["sha256"],main_source_observations=ns)
            actual.append(event)
    return actual


def page_notes():
    if not MAIN_SOURCE_CONFIRMED:
        return []
    return [
        "The page records the evaluation of u_xi at the greatest domain subobject, its induced isomorphism onto the principal ideal below xi, and the identity map associated with d_n. The recorded main checks use the preceding subobject and Hom/fiber conventions under the stated monicity and identity-endomorphism hypotheses. These arguments concern the mathematical statements; they do not decide the switch between xi and ordinary x, an uncertain prime, a crossed letter, or an abbreviation. The original six event records preserve the background event, recheck event and targeted proof-check types without alteration.",
        "The reconstruction paragraph lists N, the J families, the type maps and rho maps. It then requires composition closure and defines M_0 using admissible maps. The main record checks composition and the equivalence with the representative category for realized data under the recorded hypotheses. It does not assert those conditions automatically for arbitrary abstract input. Reader B separately records a conditional evaluation substitution. Reader C records the page's evaluation rule as an unproved background assumption and then a conditional substitution check. Reader A records none. Copying these actual events adds no new mathematical check.",
        "The diplomatic text preserves recoverable canceled phrases, raised replacements, unmatched quotation marks, singular abbreviations, the diagram's stacked labels and its lower order row. Reader differences and every original C doubt remain linked to their physical locations, including any removal, refinement or reordering of alternatives. Numbered main observations supply the final choices, independently of mathematical expectation. Own folio 2 and archive numeral 8 are distinct; the archive numeral is text in an unattributed archival hand. Remaining literal doubts are retained in the body rather than silently normalized."
    ]


def build_draft(cw):
    main_text, main, plan_list, plan = get_main()
    bykey = {x["key"]:x for x in cw["loci"]}
    decisions, locus_map = [], {}
    for x in cw["loci"]:
        key = x["key"]
        if key not in SPECS:
            continue
        raw = SPECS[key]
        spec = copy.deepcopy(raw)
        number = MAIN_NUMBERS.get(key)
        ns = spec.pop("main_observations", number if isinstance(number,list) else [number])
        assert ns and all(n in main and n in plan and plan[n].get("viewed") for n in ns), (key,ns)
        for field in ["final","confidence","diff_C","diff_H","kind","unresolved"]:
            assert field in spec, (key,field)
        assert x["countable"] or not (spec["diff_C"] or spec["diff_H"]), key
        crops = [plan[n]["path"] for n in ns]
        row = {"id":x["id"],"location":x["location"],"C":x["witness_C"],"H":x["witness_H"],**spec,"marked_in_H":x["marked_in_H"],"readers":copy.deepcopy(x["readers"]),"reader_provenance":copy.deepcopy(x["reader_provenance"]),"source_issues":copy.deepcopy(x["source_issues"]),"main_observations":ns,"crop":crops[0],"crops":crops,"evidence":"\n".join(f"Main {n}: {main[n]}" for n in ns),"reader_evidence":{a:[{"id":z,"evidence":cw["source_issue_index"][a][z]["evidence"]} for z in x["source_issues"][a]] for a in "ABC"},"reader_report_readings":copy.deepcopy(x["reader_report_readings"]),"crosswalk_keys":[key],"countable":x["countable"]}
        decisions.append(row)
        locus_map[key] = x["id"]
    source_map = {a:{k:[] for k in cw["source_issue_index"][a]} for a in "ABC"}
    for x in decisions:
        for a in "ABC":
            for k in x["source_issues"][a]:
                source_map[a][k].append(x["id"])
    covered = set(locus_map.values())
    source_coverage = {a:{k:{"required_crosswalk_loci":ids,"decision_ids":source_map[a][k],"status":"complete" if set(ids)<=covered else "pending"} for k,ids in m.items()} for a,m in cw["source_issue_map"].items()}
    byid = {x["id"]:x for x in decisions}
    cd = copy.deepcopy(cw["C_doubt_map"])
    for d in cd:
        if d["locus_key"] in locus_map:
            x = byid[locus_map[d["locus_key"]]]
            d.update(status="adjudicated",decision_id=x["id"],final=x["final"],unresolved=x["unresolved"],main_observations=x["main_observations"],crop=x["crop"],doubt_changed_from_C=x["diff_C"],disposition="resolved" if not x["unresolved"] else "refined or reordered" if x["diff_C"] else "retained")
    hd = copy.deepcopy(cw["H_doubt_map"])
    for d in hd:
        d["decision_ids"] = [locus_map[k] for k in d["locus_keys"] if k in locus_map]
        d["status"] = "adjudicated" if all(k in locus_map for k in d["locus_keys"]) else "pending"
    counts = Counter()
    for x in decisions:
        if not x["countable"]:
            continue
        for a in "CH":
            if x[f"diff_{a}"]:
                counts[a] += 1
                counts[f"{a}_{x['confidence']}"] += 1
        if x["diff_C"] or x["diff_H"]:
            counts[x["confidence"]] += 1
    validation = check_selected_page(cw)
    main_done = bool(plan) and set(plan)<=set(main) and all(x.get("viewed") for x in plan_list) and len(locus_map)==len(bykey) and MAIN_SOURCE_CONFIRMED
    complete = main_done and validation["passed"]
    inventory = copy.deepcopy(cw["inventory_crosswalk"])
    if complete:
        for row in inventory:
            row.update(transcribed="yes",selected_reading=True,page_text_sha256=validation["sha256"])
    included = sorted({n for x in decisions for n in x["main_observations"]})
    selected = [plan[n] for n in included]
    contextual = copy.deepcopy(cw["contextual_C_checks"])
    for row in contextual:
        row["main_observations"] = sorted({n for k in row["locus_keys"] if k in locus_map for n in byid[locus_map[k]]["main_observations"]})
        row["status"] = "adjudicated and selected-text verified" if complete else "main decisions staged" if all(k in locus_map for k in row["locus_keys"]) else "pending main decisions"
    draft = {"scan":9,"folder":"H104-01","issues":decisions,"remaining":[{"location":x["location"],"reading":x["final"],"alternatives":x.get("alternatives","No separately identified alternative."),"confidence":x["confidence"],"reason":x["evidence"],"decision_id":x["id"],"crop":x["crop"]} for x in decisions if x["unresolved"]],"inventory":inventory,"notes":page_notes(),"checks":math_events(cw,main),"math_source_statements_confirmed":MAIN_SOURCE_CONFIRMED,"math_source_confirmation":MAIN_SOURCE_CONFIRMATION,"math_checks_status":"Six original main events and three actual reader events imported without changed types" if MAIN_SOURCE_CONFIRMED else "Six original main events pending explicit source confirmation; three actual reader events preserved","crop_counts":{**cw["counts"]["reader_crops"],"main":sum(x.get("source")=="new main crop" for x in selected)},"main_reused_crop_count":sum(x.get("source")=="reader reuse" for x in selected),"main_count":len(selected),"main_total_decision_crop_count":len(selected),"planned_main_crop_count":len(plan),"planned_main_new_crop_count":sum(x.get("source")=="new main crop" for x in plan_list),"planned_main_reused_crop_count":sum(x.get("source")=="reader reuse" for x in plan_list),"main_complete":complete,"main_adjudication_complete":main_done,"assembly_status":"complete staged decision; main choices and selected page verified" if complete else "staged; main decisions and selected-page verification pending","main_observations_included":included,"main_observations_available":sorted(main),"main_image_delivery_events":[],"source_issue_map":source_map,"source_issue_coverage":source_coverage,"pending_source_issues":{a:[k for k,v in sm.items() if v["status"]!="complete"] for a,sm in source_coverage.items()},"crosswalk_locus_map":locus_map,"pending_loci":[k for k in bykey if k not in locus_map],"C_doubt_map":cd,"H_doubt_map":hd,"contextual_C_checks":contextual,"page_text_guard_status":validation["status"],"page_text_sha256":validation.get("sha256",""),"page_validation":validation,"counts":dict(counts),"counting_policy":cw["counting_policy"],"residual_questions":[] if complete else ["Pending numbered main choices, explicit mathematical source confirmation, installed selected page and verified inventory."]}
    write_json(P/"decision_draft.json",draft)
    return draft


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--crosswalk-only",action="store_true")
    args = parser.parse_args()
    crosswalk = build_crosswalk(load_inputs())
    if not args.crosswalk_only:
        draft = build_draft(crosswalk)
        if draft["main_complete"]:
            crosswalk.update(status="complete source crosswalk; main choices and selected-page inventory verified",inventory_crosswalk=copy.deepcopy(draft["inventory"]),C_doubt_map=copy.deepcopy(draft["C_doubt_map"]),H_doubt_map=copy.deepcopy(draft["H_doubt_map"]),contextual_C_checks=copy.deepcopy(draft["contextual_C_checks"]),selected_page_sha256=draft["page_text_sha256"],assembly_next_step="Ready for root review and copy. Authoritative decision and cumulative files remain untouched.")
    write_json(P/"reader_crosswalk.json",crosswalk)
    write_crosswalk_md(crosswalk)
    print(json.dumps(crosswalk["counts"],ensure_ascii=False))
