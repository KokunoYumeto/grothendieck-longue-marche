"""Assemble research artifacts; never writes the frozen transcription."""
from pathlib import Path
import csv
import datetime
import json
import re

root = Path(__file__).resolve().parents[1]
r = root / "research"
parts = sorted(r.glob("note_entries_part*.json"))
entries = [n for p in parts for n in json.loads(p.read_text())]
plan = {n["id"]: n for n in json.loads((r / "note_plan.json").read_text())}
assert len(entries) == len({n["id"] for n in entries}) == len(plan)
assert {n["id"] for n in entries} == set(plan)
order = {k: i for i, k in enumerate("PNGBTR")}
entries.sort(key=lambda n: (order[n["id"].split(".")[-1][0]],
                            int(n["id"].split(".")[-1][1:])))
for n in entries:
    n["scans"] = plan[n["id"]]["scans"]
    n["title"] = plan[n["id"]]["title"]
    assert 1 <= len(n["sentences"]) <= 4
    assert all(not any(ord(c) < 32 or c == "\ufffd" for c in s)
               for s in n["sentences"])
(r / "note_entries.json").write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")

groups = {
    "P": "Scope and chronology",
    "N": "Norms, symmetric powers, and axioms",
    "G": "Group actions, descent, and cohomology",
    "B": "Bounded families, field extensions, Tor, and Ext",
    "T": "The reused topology and abelian-variety typescripts",
    "R": "Reading questions raised by the supplied context",
}
out = [(r / "notes_introduction.md").read_text().rstrip(),
       f"\n## Numbered notes\n\nThere are **{len(entries)} notes** below. "
       "The file is 98.pdf throughout; scan numbers are the supplied PDF scan numbers, "
       "not archival foliation or reused printed pagination. "
       "Each note has its own recorded context search and one to four sentences of analysis.\n"]
previous = None
for n in entries:
    group = n["id"].split(".")[-1][0]
    if group != previous:
        out.append(f"### {groups[group]}\n")
        previous = group
    out.extend([
        f"#### {n['id']} — {n['title']}\n",
        f"**File / scan:** 98.pdf, {n['scans']}.  \n"
        f"**Kind:** {n['kind']}.  \n"
        f"**Brief source quotation:** {n['quote']}.  \n"
        f"**Context:** {n['context']}  \n"
        f"**Register:** {n['register']}\n",
        " ".join(n["sentences"]) + "\n",
    ])
    if n.get("confidence"):
        out.append(f"**Confidence and reason:** {n['confidence']}\n")
standing = (r / "standing_sections.md").read_text().rstrip()
for filename in ["norm_research.md", "cohomology_research.md", "boundedness_research.md", "root_proof_checks.md"]:
    standing = standing.replace("](" + filename + ")", "](research/" + filename + ")")
out.append(standing)
bib = (r / "primary_sources.md").read_text().split("## 1. Consolidated APA references\n", 1)[1]
bib = bib.split("\n## 2.", 1)[0].strip()
out.append("## References\n\n" + bib)
out.append(
    "\nExact passage locators, electronic-witness qualifications, and individual Stacks tags "
    "are recorded in [primary_sources.md](research/primary_sources.md). "
    "Metadata-only entries are included as identified leads, not as inspected mathematical proofs.\n"
)
(root / "MPL_98_notes.md").write_text("\n\n".join(out).rstrip() + "\n")

columns = ["statement_id", "date", "who", "type", "outcome"]
events = []
for name in ["consolidated_agent_events.tsv", "final_notes_peer_events.tsv",
             "root_proof_peer_events.tsv"]:
    with (r / name).open(newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        assert reader.fieldnames == columns
        for row in reader:
            if name == "final_notes_peer_events.tsv" and row["statement_id"] == "MPL98.T03":
                row["statement_id"] = "MPL98.T14"
                row["outcome"] = (
                    "Original review ID MPL98.T03, subsequently split into products T03 "
                    "and gluing T14. " + row["outcome"]
                )
            events.append(row)

who = "GPT-6 Astra Pro; effort inherited/unspecified; MPL_98 root"
date = "2026-11-18"
def add(ident, kind, outcome, when=date):
    events.append(dict(zip(columns, [ident, when, who, kind, outcome])))

add("MPL98.B19", "targeted proof check",
    "Explicit A=k[t], B=A[x], M1=B/(tx), M2=B/(x) computation shows failure after deleting input flatness despite flat output Tors. Corrected source disposition: scan039 already states input flatness, so this checks necessity rather than an omission; R09 records the disagreement with Hua.",
    "2026-11-18 01:50:33 UTC")
add("MPL98.B24", "targeted proof check",
    "Descending through short exact sequences from flat terminal cokernel proves base change in all degrees of truncated K; only its Ext identification is restricted to p<=N.",
    "2026-11-18 01:50:33 UTC")
add("MPL98.N04", "independent re-proof",
    "Expanded det(I+epsilon M) over dual numbers, obtaining 1+epsilon trace(M) without factorial division; proof in root_proof_checks.md. No arithmetic register result checked.")
add("MPL98.N08", "targeted proof check",
    "Separated the stated quotient/fibre-product/degree/section axioms from finite coproduct existence; checked that Hua's any-category wording is usable only as an added axiomatic structure.")
add("MPL98.N12", "used and rechecked in this run",
    "Compared the frozen degree definition, which includes rank-r local freeness, with the finite/flat/finite-presentation hypotheses of Stacks02K9 reported in the inspected primary-source ledger; no arbitrary-base finite-flat theorem inferred.")
add("MPL98.N15", "targeted proof check",
    "The dual-number algebra is finite free but not etale and cannot become a constant two-point etale algebra by faithfully flat descent; root_proof_checks.md explains the limit of the covering argument.")
add("MPL98.B01", "targeted proof check",
    "Checked the separate fixed-polynomial counterexample O(n)+O(-n) on P1: polynomial 2m+2 while h0 is unbounded. Positive Quot boundedness is a literature comparison, not an independent full proof.")
add("MPL98.B03", "targeted proof check",
    "Checked the projective-family repair via parameterized maps to bounded quotients and stratified kernels; source-stage comparison confirms that frozen scan028 already names kernels. Does not assert boundedness of arbitrary subsheaves.")
add("MPL98.B11", "independent re-proof",
    "Computed the tensor of point modules as R/(x-a,x-b), equal to a point module when a=b and zero otherwise; confirms dependence on relative embeddings. Proof in root_proof_checks.md.")
add("MPL98.B12", "targeted proof check",
    "Computed k[x]/(x^p-a) after adjoining a^(1/p), exhibiting a nonzero nilpotent and failure of reduction to commute with this extension.")
add("MPL98.B13", "independent re-proof",
    "Verified (x) intersect (x^2,y-a*x)=(x^2,xy), primaryness and distinctness of the varying embedded factors; no uniqueness claim attributed to source.")
add("MPL98.B14", "targeted proof check",
    "Checked tensor-family construction on the product of finite-type parameter schemes and fibrewise tensor base change; distinct relative embeddings are distinct product points.")
add("MPL98.B15", "targeted proof check",
    "After restricting the inputs to each stratum, finite presentation expresses the newly computed Hom as a kernel; flatness of its coefficient module and cokernel gives flat image and further base change. This does not identify restriction of the original Hom with that new Hom. Finite affine cover and common parameter stratification are explicit in root_proof_checks.md.")
add("MPL98.B21", "targeted proof check",
    "Checked passage from generic open statements to finitely many reduced locally closed strata by noetherian induction for a fixed finite degree range, after the B20 resolution repair.")
add("MPL98.B25", "targeted proof check",
    "Checked canonicity by full projective resolutions and chain-homotopy independence, plus compatibility with restriction; only the asserted finite Ext range is glued. Proof in root_proof_checks.md.")
add("MPL98.B30", "targeted proof check",
    "Finite disjoint union of parameter schemes gives boundedness of finite union; research-stage comparison counts seven propositions and five corollary entries on scan044, without certifying all planned assertions.")
add("MPL98.B31", "refuted, with the refined statement's id",
    "Generic length one does not imply global inclusion in the support structure sheaf: Hom(O(n),O)=0 for n>0, although O(n) is a quotient of O². Refined scope MPL98.B02/MPL98.B31 keeps the Hilbert-polynomial condition and separates uncertain pale-pencil intent.")
add("MPL98.B32", "used and rechecked in this run",
    "Compared explicit scan038 question with the subsequent flat-input sufficient Tor criterion and B18-B20 proof checks; identifies a later answer without treating uncertain coefficient subscripts as settled.")
add("MPL98.T02", "targeted proof check",
    "Verified quotient-restriction criterion with every relatively saturated open subset of A, and equivalent closed version; proposed trace correction is mathematical only.")
add("MPL98.T03", "targeted proof check",
    "Verified finite-support product basis, coordinatewise continuity and regrouping homeomorphisms; root_proof_checks.md.")
add("MPL98.T04", "used and rechecked in this run",
    "Read Milne1986/2022 Proposition9.2 and following Pic0 formulas, and checked pullback along (alpha,beta) plus integer multiplication deduction. No Fermat/Jacobian register arithmetic checked.")
add("MPL98.T05", "used and rechecked in this run",
    "Read Milne8.1 and9.2, distinguished finite-kernel isogeny from zero-map Pic0 criterion; checked dimension/proper-image inference, not all postponed typescript assertions.")
add("MPL98.T06", "independent re-proof",
    "Proved final nonzero coefficient-kernel step is one dimensional under finite dimension and injective expansion; K-rationality requires K-defined ambient space and functionals.")
add("MPL98.T07", "refuted, with the refined statement's id",
    "Full-rank homogeneous system has only zero solution, with basis1,t explicit. Refined statement MPL98.T06 uses prefix immediately before first full rank; source equations unchanged.")
add("MPL98.T08", "targeted proof check",
    "Verified that degree-ordered surviving monomials form an ideal; compared lower infinity limit with preceding zero-index enumeration only as a literal formula issue.")
add("MPL98.T09", "used and rechecked in this run",
    "Read Milne9.1 with effectiveness/nonzero section, Remark7.3 for very ample power, Theorem7.1 separately for projectivity, and Milne2008 I6.3 for tangent separation.")
add("MPL98.T11", "targeted proof check",
    "Expanded a linear combination indexed0..n and checked that dropping the index-zero coefficient is not justified; source lower bound remains unchanged.")
add("MPL98.T12", "targeted proof check",
    "Checked type distinction between rational functions and divisors in the displayed product equality; outer divisor operator is a proposed correction only.")
add("MPL98.T13", "targeted proof check",
    "Constructed three compatible singleton-glued pieces and checked quotient opens and missing singleton in discrete piece; independently reviewed by norm agent.")
add("MPL98.T14", "targeted proof check",
    "Checked saturation proof under uniformly open or uniformly closed overlaps and locally finite integral-translate argument for interval quotient; root_proof_checks.md.")

notes = {n["id"]: n for n in entries}
for ident in ["MPL98.P01", "MPL98.P02", "MPL98.T01", "MPL98.T10"] + [
        f"MPL98.R{i:02d}" for i in range(1, 14)]:
    add(ident, "used and rechecked in this run",
        "Research-stage source/context comparison, not a mathematical proof or another image audit: "
        + notes[ident]["title"] + ". " + notes[ident]["sentences"][-1]
        + " Actual per-note context search is recorded in context_searches.jsonl.")
add("MPL98.G11", "used and rechecked in this run",
    "Compared all five selected open register entries with the manuscript's cohomological mechanisms and RS's own Orientation; no solution, counterexample or status upgrade established.")
add("98-axiomatic-norms-can-section", "used and rechecked in this run",
    "Exact RESULTS_STATE identifier corresponding to the agent's Hua-prefixed event: concrete scheme and G-set models checked in MPL98.N01-N15, with the degree/empty-base refinement. The supplied status remains conjecture (unsearched), Lean card partly proved; no Lean sources or formal certificate inspected.")

background = {
    "LM7 E.23": "Open; section-map fibres not determined by these pages; bears on MPL98.G11.",
    "FLAGGED_149 B9": "Open; prime-to-p point question not settled; bears on MPL98.G11.",
    "LM1 D.11": "Open; integral mu2 extension problem not settled; bears on MPL98.G11.",
    "LM4 D.12": "Open; full profinite torsion classification not settled; bears on MPL98.G11.",
    "LM4 F.7": "Open; A5 completion centralizer comparison not proved; bears on MPL98.G11.",
    "LM7 C.1": "Known in originating run; Picard background only here; underlying arithmetic statement not checked; MPL98.T04.",
    "LM7 C.5": "Proved in originating run; extension order/splitting/degree not checked; MPL98.T04/T05.",
    "LM7 E.124": "Proved in originating run; unit norm and class-group computations not checked; MPL98.N04.",
    "SECTIONS_OVER_Q A.179": "Proved in originating run; tower arithmetic not checked; MPL98.N04.",
    "SECTIONS_OVER_Q A.184": "Proved in originating run; residue/norm-image arithmetic not checked; MPL98.N04.",
    "WG H9": "Unchecked hunch; intersection-formula identification not established; MPL98.T05.",
    "WG H2": "Unchecked hunch; monodromy examples do not settle its arithmetic statement; MPL98.G09/G12.",
    "WG2 §1.1 #3": "Unchecked planning item; reused typescript inventory only; no Book II theorem established.",
    "WG2 §Summary #2": "Unchecked planning item; thematic comparison only.",
    "MPL_131 RN001": "First-pass lead; original manuscript/return not supplied; MPL98.B30.",
    "MPL_131 §2": "First-pass lead; no representability result inferred from boundedness; MPL98.B30.",
    "MPL_131 10": "First-pass planning-disposition lead; underlying return not supplied; MPL98.P01.",
    "S19": "Planning prompt used for primary-literature comparison, not a mathematical theorem.",
    "Book I I.VI": "Planning placement used for scope comparison; no unsupported representability assertion."
}
for ident, outcome in background.items():
    add(ident, "carried as background without fault found",
        outcome + " Status retained as a supplied originating-run claim or planning lead.")

allowed = {
    "targeted proof check", "independent re-proof", "computation or formal certificate",
    "used and rechecked in this run", "carried as background without fault found",
    "refuted, with the refined statement's id",
}
for e in events:
    assert e["type"] in allowed
    assert all(isinstance(e[k], str) and e[k] and not any(c in e[k] for c in "\t\r\n")
               for k in columns)
with (root / "CHECK_EVENTS.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(events)

index = [{"id": n["id"], "scans": n["scans"], "title": n["title"],
          "sentence_count": len(n["sentences"]),
          "search_utc": plan[n["id"]]["searched_utc"],
          "context_match_count": len(plan[n["id"]]["matches"])}
         for n in entries]
(r / "note_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
with (root / "progress.log").open("a") as f:
    f.write(f"research notes assembled {now}: {len(entries)} notes, {len(events)} check events; transcription untouched\n")
print(json.dumps({"notes": len(entries), "events": len(events),
                  "words": len((root / "MPL_98_notes.md").read_text().split())}))
