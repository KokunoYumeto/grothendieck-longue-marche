#!/usr/bin/env python3
"""Consolidate already established results after restoration of checkpoint08."""
from pathlib import Path
import csv, json, re
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/"notes/results_checkpoint08.csv"
with base.open(newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
assert fields==['id','statement','status','where_proved','depends_on','answers (item or lead)','checks (the earlier statement it checks, and confirmed / repaired / refuted)','uses_local_theorem (yes or no, and where)','manuscript_passages (cote; scan)','notes']
notes=json.loads((ROOT/"notes/recovery_final_open_notes.json").read_text())
for row in rows:
    if row["id"] in notes:
        row["notes"]=notes[row["id"]]
        if row["id"]=="C.7":
            row["statement"]=row["statement"].replace("Existence of a full section for every remaining member of that family is undecided.","Whether any member of the post-exclusion remainder admits a full section is undecided.")
        if row["id"] in ("A.2","B.1"):
            row["statement"] += " Recovery update: E.214 proves selected original outputs first fail at pro-five class four. In a separate primitive-five family, E.215 constructs selected outputs with off-five point matching through class seven and a global class-eight lift. Neither closes this Open assertion."
added=json.loads((ROOT/"notes/recovery_final_result_rows.json").read_text())
for r in added:
    rows.append(dict(zip(fields,[r["id"],r["statement"],r["status"],r["where_proved"],r["depends_on"],r["answers"],r["checks"],r["local"],r["passages"],r["notes"]])))
assert len({x["id"] for x in rows})==len(rows)
with (ROOT/"SECTION_GHOSTS_results.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
with (ROOT/"notes/RESULTS_recovery_delta.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows[-len(added):])
old=(ROOT/"notes/report_checkpoint08.md").read_text()
table=old.split("# SECTION_GHOSTS research report")[0].strip()
updates={
"A.2":" E.215 additionally gives selected off-five matched lifts through class seven and a global class-eight lift; weight-eight matching and the whole compatible tower remain open.",
"A.3":" E.216-E.217 are finite coefficient refinements at fixed class, not class jumps.",
"A.4":" E.214 supplies a selected original-family class-four obstruction; E.218 is a local interior/cusp detector, not an evaluation for every ghost.",
"A.5":" The exact finite-geometric-support formulation is Stix Corollary5, author pp5-6; Corollary6 gives the alternate adelic-unit route.",
"B.1":" E.214 now gives selected original outputs first failing at pro-five class four. E.215 belongs to a different support family and gives selected class-four matching there.",
"B.2":" Add the precisely selected E.214 class-four exclusions; no universal table for residual outputs is certified.",
"C.1":" E.218 supplies a local finite-field detector at every coefficient distinct from the characteristic, without a global universal-target claim.",
"C.4":" P.16 proves the base-tripod five-primary Brauer evaluations also obey global reciprocity, and states the separate fixed embedding-problem criterion.",
"L.1":" The new finite-class results E.215-E.217 do not close this assertion.",
"L.4":" E.214 supplies a locally detectable selected obstruction; the blanket assertion that the first higher obstruction must be an invisible lim-one class is not established.",
"L.6":" P.16 makes the base-tripod Brauer calculation and the additional embedding-problem Brauer classes separate; no universal cover-wise nonvanishing is proved."
}
lines=[]
for line in table.splitlines():
    if line.startswith("| "):
        label=line.split("|")[1].strip()
        if label in updates:line=line.rstrip().removesuffix("|").rstrip()+updates[label]+" |"
    lines.append(line)
table="\n".join(lines)
report=table+"\n\n"+r"""# Final research disposition

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. No human authorship or priority is claimed. This is an incomplete final return under the user's stopping rule, not a solution of the main question.

## The stopping decision

The seventh formal hourly review, at approximately 11:45 UTC (12:45 CET), recorded no qualifying main-question movement. The eighth formal review at approximately 12:45 UTC (13:45 CET) again recorded none. These are two consecutive no-movement reviews. Research stopped under the explicit rule; subsequent work only restores, transcribes, compiles, verifies and packages results already reached.

The precise nine Open result entries remain **A.2, A.7, B.1, B.2, B.3, C.7, D.3, E.120, and E.1**. The added results do not close any of them. Each Open CSV row now states cases proved, actual computations, the exact remaining obstruction, a concrete smallest outstanding task instance, and the failed approach. A selected next instance is not claimed to be a universal minimal obstruction.

## Mathematical outcome

We have neither proved the full-pronilpotent finite-support assertion nor constructed an ordinary infinite-support pair with a section through the full tower. The requested complete single-prime decisions remain open, including at two, three and five.

The strongest general reduction is E.209-E.210. For each odd prime ell not dividing the class number of Q(zeta_ell), fixed-ramification H2(G_Q,{ell,infinity}, Z_ell(w)) vanishes in every weight w>=2. The exact global H1 correction groups and their localizations are also computed. Above a predecessor with the required actual local support matches, the next global lift exists. Simultaneously preserving those matches is a separate global H1 localization problem. E.212 shows that failure in one fixed nonempty lifting fibre has a witness at at most two support places; it does not bound those places or force consistency.

P.16 gives the exact finite embedding-problem Brauer pairing and a carefully quantified integral matching criterion, retaining the literal negative Tate dual at each finite coefficient level. It also proves that the base-tripod five-primary Brauer test is automatic on ordinary completed pairs. It does not establish automatic vanishing of the additional embedding-problem or cover-wise Brauer classes.

E.214 proves that selected legal outputs of the original factorial construction first fail at pro-five class four, although they lift through class three. E.215 constructs a different primitive-five support family with one common 25-element catalog for class-four matching. A selected subfamily has an actual off-five matched class-four lift. The established automatic nonresonant steps preserve matching through classes five, six and seven and give a global class-eight lift. The next resonant matching gate, at weight eight, and full-tower survival remain unproved.

E.216-E.217 prove relative ordinary interpolation at fixed geometric classes two, three and four, with their stated arithmetic, ramification, frame and first-coordinate compatibility hypotheses. Raising coefficient precision in a fixed class is not a lift to the next nilpotency class.

E.218 gives a finite characteristic geometric pro-ell quotient separating every interior point section from every cusp section over a finite field of characteristic different from ell, with an explicit quotient bound. This rules out the inappropriate indefinite freezing of the same local reference Frobenius. It is not a universal global finite-support theorem.

For a full profinite section which is actually locally ordinary everywhere, a rational completed abelian pair already determines the rational-point section: A.4 uses Stix's finite-geometric-support result after local Kummer injectivity. The twenty-four class-two choices are not an additional unresolved gate under those full local hypotheses. This result does not apply merely to abelian-local or pronilpotent data.

## Continuous cohomology and quantifiers

We retain Jannsen's continuous-cohomology comparison and its lim-one term, actual localization images rather than their closures, and the strict c0 conditions after division. Vanishing at every finite coefficient level or at every individual place is not silently identified with vanishing of the integral continuous obstruction.

Fixed-pair fibres are compact under the proved finite-parameter hypotheses. The varying ordinary-ghost space is not compact in the asserted manner. Existence for every finite quotient with a pair depending on the quotient does not provide one fixed pair surviving the whole tower. Likewise, formal free-Lie identities outside an established integral comparison are not promoted to identities for the actual arithmetic group.

The recovered scope note records two further precise limitations. A fixed nonzero ordinary support exponent eventually ceases to agree with a fixed rational reference modulo increasing powers of five. At geometric class six the ordinary Hall lattice is not stable under conjugation: the fifth adjoint term has denominator120. Neither limitation proves nonexistence of a corrected all-depth construction.

## Historical audit and manuscript assertions

The exact E.2 list of66 claims is audited. The broader historical table has90 entries:87 confirmed,2 repaired,1 pending. The remaining pending claim is the literal numerical compiler in GT_TOWER_CHECK A4.57, including its BCV and HCF/KFU bound recursions. Qualitative finite separation and the checked finite quaternion inputs do not supply those missing numerical bounds.

The conditional implications for Grothendieck cote149, scan56, and birational assertion b), scans126-127, are stated precisely. We read the supplied transcriptions; we do not claim to have inspected absent original manuscript scans. No unconditional proof or counterexample to those manuscript assertions is obtained.

The supplied unrefereed local p-adic section theorem is not used.

## Recovery and verification provenance

The earlier execution workspace became unavailable at approximately11:35:30 UTC. After the prescribed retry period, the post-checkpoint source and proof material was supplied in full as labeled chat recovery blocks, with the explicitly stated exceptions. Execution later became available in a new workspace with the old working directory missing. Checkpoint08 was restored and its SHA-256 verified:
3f67e030dc6328440381bb3c9e78b688991bc376ec4408df37b00837694b49b5.

That archive contained392 files and3,999,748 bytes, a349-page paper and222 numbered result rows. It remains unchanged. This final package uses it as the exact baseline and incorporates freshly transcribed, already reviewed additions. The original baseline report and result register are retained in notes.

Some post-checkpoint source text is a fresh mathematical transcription from the reviewed conversation, not a byte-for-byte recovery of the lost working files. The per-agent provenance notes identify these cases. The exact lost original E.214 Python checker and output bytes have not been fabricated. Their earlier actual execution counts and retained output hash are recorded; the complete earlier chat delivery remains available in the conversation. The recovered primitive-five JavaScript and its actual stored output are included as a distinct executable recovery check.

No old build count, old visual inspection or agent agreement is treated as verification of a later PDF. The final build and rendering report records what was actually compiled and viewed after restoration. Agreement among AI proof readers is internal checking, not independent external mathematical certification.

## Remaining work

The task/lead table above is the requested per-item disposition. A complete solution requires either:
1. a proof that one ordinary completed pair surviving every compatible integral class and every coefficient prime has finite support, or
2. one explicit ordinary infinite-support pair with a compatible actual full-pronilpotent section and complete verification of all local and arithmetic requirements.

Neither has been obtained. The next concrete finite problem in the new five-primary family is preserving point matching for its selected global class-eight lift; solving that problem alone would still not establish the required infinite compatible branch.
"""
(ROOT/"SECTION_GHOSTS_report.md").write_text(report,encoding="utf-8")
print(json.dumps({"results":len(rows),"status_counts":dict(Counter(r["status"] for r in rows)),"open_ids":[r["id"] for r in rows if r["status"]=="Open"]},indent=2))
