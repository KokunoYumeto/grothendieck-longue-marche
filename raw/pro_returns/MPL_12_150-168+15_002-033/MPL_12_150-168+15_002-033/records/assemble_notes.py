#!/usr/bin/env python3
"""Assemble the post-freeze research report; never write transcription files."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "records"
STEM = ROOT.name
ALLOWED = {
    "conjecture", "unproved claim", "unpursued implication", "own idea",
    "reading question", "self-flagged", "withdrawn in the same text",
}

KINDS = {}
def assign(prefix, kinds):
    KINDS.update({f"{prefix}{i:02d}": k for i, k in enumerate(kinds, 1)})

U = "unpursued implication"
P = "unproved claim"
O = "own idea"
Q = "reading question"
S = "self-flagged"
assign("M", [U,P,U,U,P,O,U,O,P,O,O,U,O,O,S,S,U,O,O,P,S,U,U,Q,U,U,U,Q,Q,Q,Q,Q])
assign("FF", ["conjecture",U,Q,U,U,Q,U,Q,U,U,O,O,O,U,Q,U,Q,Q,U,Q,Q,U])
assign("D", [O,O,Q,O,O,Q,O,U,"withdrawn in the same text",O,Q,O,O,O,U,U,Q,O,U,U,Q,O,P,O,O,O,U,O,O,S])

def extract_items(filename):
    source = (RECORDS / filename).read_text()
    headings = list(re.finditer(r"(?m)^#{2,3} .+$", source))
    found = []
    for i, heading in enumerate(headings):
        match = re.match(r"### ([A-Z]+\d+)\s+—\s+(.+)", heading[0])
        if not match:
            continue
        stop = headings[i + 1].start() if i + 1 < len(headings) else len(source)
        found.append((match[1], source[heading.start():stop].strip()))
    return found

def search_terms(item):
    direct = re.search(r"(?m)^\*\*Search terms:\*\*\s*(.+)", item)
    if direct:
        return direct[1].strip()
    line = re.search(r"(?m)^\*\*Context search(?:ed| and relation)?:\*\*\s*(.+)", item)
    if not line:
        raise ValueError("Missing context-search metadata")
    value = line[1]
    if "→" in value:
        return value.split("→", 1)[0].strip()
    quoted = re.search(r"“([^”]+)”", value)
    if quoted and "|" in quoted[1]:
        return quoted[1].strip()
    return " | ".join(x.strip() for x in value.split(";", 1)[0].split(","))

def replace_body(item, body):
    parts = item.split("\n\n", 2)
    assert len(parts) == 3
    return parts[0] + "\n\n" + parts[1] + "\n\n" + body.strip()

def normalize(identifier, item):
    original_id = identifier
    if identifier.startswith("RQ"):
        identifier = f"M{27 + int(identifier[2:]):02d}"
        item = item.replace("### " + original_id + " —", "### " + identifier + " —", 1)
    terms = search_terms(item)
    kind_match = re.search(r"(?m)^\*\*Kind:\*\*\s*(.+)$", item)
    if identifier in KINDS:
        kind = KINDS[identifier]
    else:
        kind = kind_match[1].strip().rstrip(".")
    assert kind in ALLOWED, (identifier, kind)
    if kind_match:
        old = kind_match[1].strip()
        replacement = "**Kind:** " + kind + "  "
        if old.rstrip(".") != kind:
            replacement += "\n**Assessment:** " + old + "  "
        item = item[:kind_match.start()] + replacement + item[kind_match.end():]
    else:
        first, rest = item.split("\n\n", 1)
        item = first + "\n\n**Kind:** " + kind + "  \n" + rest
    if "**Search terms:**" not in item:
        item = item.replace("**Kind:** " + kind + "  ",
                            "**Kind:** " + kind + "  \n**Search terms:** " + terms + "  ", 1)
    # Original reading-question identifiers remain in the source memorandum.
    for n in range(1, 6):
        item = re.sub(r"\bRQ" + str(n) + r"\b", f"M{27+n:02d}", item)
    # Supporting constructions are in the enclosed working memorandum.
    if identifier.startswith("D"):
        if identifier == "D05":
            item = item.replace("Construction A below", "Constructions A–B")
        if identifier == "D09":
            item = item.replace("Construction A", "Construction B")
        item = re.sub(r"\bConstruction ([A-D])\b(?! in records/)",
                      r"Construction \1 in records/research_deuring.md", item)
        item = item.replace("Constructions A–B", "Constructions A–B in records/research_deuring.md")
        item = item.replace(" in records/research_deuring.md below",
                            " in records/research_deuring.md")
    if identifier == "M07":
        item = item.replace("“catégorie pseudo-lim”", r"“catégorie pseudo-\(\varinjlim\)”")
    if identifier == "M11":
        item = item.replace("“La structure multiplication … est connue quand on connaît les foncteurs”",
                            "“est connue quand on connaît les foncteurs”")
    if identifier == "M12":
        item = item.replace("“M* = Hom(M, Λ(−i))”", r"\(M^*=\operatorname{Hom}(M,\Lambda(-i))\)")
        item = item.replace("“check M = Hom(M, Λ(0))”", r"\(\check M=\operatorname{Hom}(M,\Lambda(0))\)")
    if identifier == "M13":
        item = item.replace("“si Hom(M,N) existe dans M, il existe aussi dans M-hat et est le même”",
                            r"“si \(\operatorname{Hom}(M,N)\) existe dans \(\mathcal M\), il existe aussi dans \(\widehat{\mathcal M}\) et est le même”")
    if identifier == "M14":
        item = item.replace("“Hom(M,N(−i)) ≃ M* ⊗ N”; “vérification facile”",
                            r"“vérification facile”; the displayed final superscript is frozen as \(*|\circ\), not resolved here")
        item = item.replace("Consequently the claimed formula requires genuine duality or an equivalent nondegeneracy condition in addition to representability, as reflected in the separate rigidity axiom of Deligne–Milne.",
                            r"With \(M^*\) interpreted by the preceding explicit definition, the claimed formula therefore requires genuine duality or an equivalent nondegeneracy condition in addition to representability, as reflected in the separate rigidity axiom of Deligne–Milne; this calculation does not resolve the doubtful superscript.")
    if identifier == "M15":
        item = item.replace("the correction from “injectif” to “épim.”", "the correction from “injectif” to the doubtful inserted “épim.”")
        item = item.replace("so the inserted correction is the expected variance", "so the doubtful inserted “épim.” would have the expected variance")
    if identifier == "M25":
        item = item.replace("12/150–152, universal factorization and realizations.",
                            "12/150–152, universal factorization and realizations: “additif universel”; “foncteur exact fidèle”.")
    if identifier == "M26":
        item = item.replace("conditional semisimplicity and faithful realization.",
                            "“donc est semi-simple”; “foncteur exact fidèle”.")
    if identifier == "M28":
        item = item.replace("**Relation and RS:**",
            "**Confidence/reason:** high for the stated localization counterexample; the letter remains unresolved.  \n**Relation and RS:**")
    if identifier == "M29":
        item = item.replace("**Witness:**", "**Brief quotation:** frozen “M(1)” and “M(−1)”, with the surrounding uncertain twist signs retained.  \n**Witness:**", 1)
    if identifier == "M30":
        item = item.replace("**Witness:**", r"**Brief quotation:** frozen \(\kappa_{i,k}(M\otimes N)(k)\).  " + "\n**Witness:**", 1)
    if identifier == "M32":
        item = item.replace("**Witness:**", r"**Brief quotation:** \(\lambda'\lambda=\mu'\mu=\operatorname{id}\).  " + "\n**Witness:**", 1)
    if identifier == "FF03":
        item = item.replace("The literal effective set is a monoid, not a subgroup",
                            "The literal effective set is not a subgroup")
        item = item.replace("The displayed conditions include", "Under the frozen first reading of the membership sign, the displayed conditions include")
        item = item.replace(r"\(\nu\in\mathbf Z^+\).", r"\(\nu\in\mathbf Z^+\), with the membership sign marked uncertain in the frozen text.")
    if identifier == "FF07":
        item = item.replace("in the diagonalizable group", r"in the group of multiplicative type")
        item = item.replace("through every finite quotient", "through every quotient of finite type")
    if identifier == "FF10":
        item = item.replace("scans 007–009", "scans 007 and 009")
    if identifier == "FF12":
        item = item.replace("For a countable inverse system", "For a strict countable inverse system")
        item = item.replace("Milne’s protorus cohomology sequence", "Milne’s continuous protorus cohomology sequence")
    if identifier == "FF16":
        item = item.replace(r"Thus \(D\otimes_{\mathbb Q}\mathbb Q_\ell\)",
                            r"Thus, for \(\ell\ne p\), \(D\otimes_{\mathbb Q}\mathbb Q_\ell\)")
    if identifier == "FF17":
        item = item.replace(r"\(M\to\unsure{\mathbf Z|\mathbf Z^+}\)",
                            r"\(M\to\mathbf Z\), with the frozen alternative \(\mathbf Z^+\) and the uncertainty retained")
    if identifier == "FF13":
        item = replace_body(item, r"""
Honda–Tate gives a simple abelian surface over \(\mathbb F_p\) with Frobenius \(\sqrt p\), whose endomorphism algebra becomes \(\mathbb H\times\mathbb H\) over \(\mathbb R\), where \(\mathbb H\) is Hamilton's quaternion division algebra (Tate, 1971, p. 97, example (a), odd exponent case). A real tensor fibre functor preserves categorical dimension and trace, so if \(r_\pm\) are the real dimensions of the \(\pm\sqrt p\) eigenspaces, then \(r_++r_-=4\) and \(\sqrt p(r_+-r_-)=0\), forcing \(r_+=r_-=2\). Each eigenspace is a nonzero module for the corresponding quaternion factor, whose real dimension must be divisible by four, giving a contradiction. This supplies an obstruction over the exact ground field of the sheet; mere \(\mathbb Q\)-linear faithfulness, without the tensor trace condition, would not justify the two-factor argument.
""")
    if identifier == "FF22":
        item = replace_body(item, r"""
For a strict countable inverse system of tori, Milne's continuous protorus cohomology includes a \(\varprojlim{}^1H^1\) term in \(H^2\) (Proposition 2.8), while Propositions 3.5(b) and 3.10, together with Proposition 2.13 at finite stages, give global-to-all-local injectivity for the specific Weil-number protorus; Proposition 4.3 further gives existence and uniqueness for its specified fundamental local classes, not arbitrary local tuples (Milne, 2003, pp. 17–19, 24–25, 29). For the explicitly \(p\)-integral Weil group defined above, the map \(W(p)\to\varinjlim_n W(p^n)\), \(\alpha\mapsto[(\alpha,1)]\), has kernel \(\mu_\infty\) and is surjective by taking an \(n\)-th root of a level-\(p^n\) representative while retaining \(p\)-integrality, hence induces the Galois-equivariant isomorphism from \(W(p)/\mu_\infty\) to the germ group. The weight-zero part is a direct factor through the Galois-invariant section \(m\mapsto[p^{m/2}]\), so this supplies the later route to the \(H^0\) uniqueness used on scans 009 and 011 (compare Proposition 3.12). The conclusion is defensible for that identified band, but neither compactness alone nor the literal archimedean-only definition printed on p. 23 supplies the missing hypotheses or the inverse-limit justification.
""")
    if identifier == "D06":
        item = item.replace("“π_[deleted 0]1”", r"\(\pi\) with a deleted, uncertain subscript \(0\), followed by the live subscript \(1\)")
    if identifier == "D11":
        item = item.replace("“n(x) … rg de _A O”", r"\(n(x)\) … uncertain “rg” de \({}_A O\)")
    if identifier == "D12":
        item = item.replace("“compatible … ass.”", "“compatible” … uncertain “ass.” (15/022:L22)")
    if identifier == "D15":
        item = item.replace("“pas décomposé sur R”", r"uncertain “pas décomposé”, followed by “sur \(R\)”")
    if identifier == "D20":
        item = item.replace("“Z_2*/Z_2*2”", r"\(\mathbf Z_\ell^*/\mathbf Z_\ell^{*2}\), with the separate condition \(\ell=2\)")
    if identifier == "D24":
        item = item.replace("“commute … P⊗_O X”", r"uncertain “commute” … \(P\otimes_O X\)")
        item = item.replace("“O⊗_A A′→O′”", r"\(O\otimes_A A'\mathbin{-}O'\), with a dash in the frozen text")
    if identifier == "D30":
        item = item.replace("“vraisemblᵗ”; uncertain", "uncertain “vraisemblᵗ”; uncertain")
    if identifier == "R06":
        item = item.replace(r"the present commutative \(G\)", r"the present conditionally commutative \(G\)")
    if identifier == "D28":
        item = replace_body(item, r"""
Fix \(X\), identify \(C\simeq P_1(O)\), and suppose the coherent reduced-norm line functor \(N:P_1(O)\to P_1(A)\) is defined on all module maps. In the target 2-category of \(A\)-preadditive categories admitting tensoring by every invertible \(A\)-module, admissible \(A\)-linear functors \(P_1(A)\to D\) are determined by \(T_0=F(A)\), with \(F(L)=L\otimes_A T_0\), giving the model \(V_A(C)\simeq P_1(A)\). Changing \(X\) changes this presentation by tensoring with its norm line, so a canonical presentation or section requires the additional coherent trivialization. The margin only asks for tensoring by norm lines, which may be weaker, and the general semisimple-centre and base-change claims remain unproved here; the complete restricted construction is Construction D in records/research_deuring.md.
""")
        item = item.replace("high in the central Azumaya/maximal-order setting once the coherent reduced-norm line functor is specified;",
                            "high for the restricted target 2-category and central Azumaya/maximal-order setting once the coherent reduced-norm line functor is specified;")
    return identifier, item

finite_intro = r"""
For the finite-field calculations, the comparison model is
\[
W(p)=\{\alpha\in\overline{\mathbb Q}^{\,*}:
|\sigma\alpha|=p^{w/2}\text{ for every }\sigma,\ w\in\mathbb Z,\
p^N\alpha\text{ is integral for some }N\geq0\}.
\]
This explicitly \(p\)-integral rigid Weil group is not a replacement for the algebraic-integer/positive-weight wording of scan 005. Write \(\mu_\infty\) for the roots of unity and \(W_0(p)=\ker(w)\); any passage to a protorus retains its stated finite-level and cohomology conventions.
"""

groups = [
    ("A. Correspondence motives, grading, duals, and positivity",
     "research_motives.md", ""),
    ("B. Finite-field motives, Frobenius, and the band",
     "research_finite_field.md", finite_intro),
    ("C. Deuring categories, orders, gerbes, and reduced norm",
     "research_deuring.md",
     r"Here \(P_1(O)\) denotes right \(O\)-modules locally free of rank one over \(O\), with all module maps. Full supporting constructions are in records/research_deuring.md; they are calculations made after the transcription freeze."),
    ("D. Cross-package questions, arithmetic comparisons, and reused sources",
     "research_root.md", ""),
]

parts = [(RECORDS / "notes_frontmatter.md").read_text().strip()]
manifest = []
for title, filename, intro in groups:
    parts.append("## " + title)
    if intro:
        parts.append(intro.strip())
    for identifier, block in extract_items(filename):
        identifier, block = normalize(identifier, block)
        parts.append(block)
        manifest.append({"id": identifier, "source_memo": filename,
                         "kind": re.search(r"\*\*Kind:\*\*\s*([^\n]+)", block)[1].strip(),
                         "search_terms": search_terms(block).split("|")})
for filename in ("notes_endmatter.md", "notes_bibliography.md"):
    path = RECORDS / filename
    if path.exists():
        parts.append(path.read_text().strip())
assert len(manifest) == 100, len(manifest)
assert len({item["id"] for item in manifest}) == 100
destination = ROOT / f"{STEM}_notes.md"
destination.write_text("\n\n".join(parts) + "\n")
(RECORDS / "notes_manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"notes": len(manifest), "characters": destination.stat().st_size,
                  "file": destination.name}))
