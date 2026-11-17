#!/usr/bin/env python3
"""Write the research check ledger, preserving separately authored events."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re

R=Path(__file__).resolve().parents[1]; P=R/"records"
HEAD=["statement_id","date","who","type","outcome"]
DATE="2026-11-17"
WHO="GPT-6 Astra Pro; effort not exposed; run MPL_138_090-133/root"
rows=[]
def event(ident,kind,outcome,date=DATE):
    rows.append(dict(zip(HEAD,[ident,date,WHO,kind,outcome])))

checks={
 "BC03":("targeted proof check","Conditional coefficient-conjugation construction is independent of raw fine representability; no descent theorem is reproved."),
 "BC04":("targeted proof check","Constant pin relabellings commute with coefficient conjugation on geometric classes; integral-model recovery remains conditional."),
 "BC09":("targeted proof check","A fixed finite passport gives a finite permutation set, whereas cyclotomic quotients of Gamma_Q have unbounded orders; no one finite action is faithful."),
 "OP04":("targeted proof check","Only the powerset descent identity P(X/H)=P(X)^H checked by inverse image; full operator-functor descent left unproved."),
 "OP12":("independent re-proof","Finite face-wise criterion proved in operations_proofs.md P1, with the converse restricted to the category containing the indicated double covers."),
 "OP14":("targeted proof check","Inverse-image composition and branch-set inclusion checked by local ramification multiplication, P2."),
 "OP16":("targeted proof check","Local square-map lift of a leaf has two rays; index2 times index1 gives index2; global classification not asserted, P2."),
 "OP17":("targeted proof check","Stronger inclusion is sufficient for the clean composite; identity endpoint case shows it is not necessary in the broader category, P2."),
 "OP18":("computation or formal certificate","Corrected final operations_certificate.py passed: nonconstant m_c has square=id exactly for c=0,2; c=1 excluded."),
 "OP19":("computation or formal certificate","q(t)-1=4t(t-1) and q derivative checked exactly; fibre claims verified, final operations_certificate.json."),
 "OP20":("computation or formal certificate","For f=z^3, (2f-1)^2-1=4z^3(z^3-1) gives index3 above1, so general Belyi preservation is weaker than cartographic preservation."),
 "OP22":("targeted proof check","Finite cellular reduction and CK Proposition3.2 invariant-arc step checked; the preceding topological lemma and full rigidification theorem not reproved, P6."),
 "OP25":("targeted proof check","h_(2^m) is a faithful infinite cyclic map action with explicit identity isotopy; not the hyperbolic centralizer problem LM4 C.12, P4/P6."),
 "OP27":("used and rechecked in this run","Compared frozen129's i.e. with the certified torus cell-kernel example; fixed cells do not imply incidence-fixing isotopy."),
 "OP28":("targeted proof check","Real-equator preserving identity subgroups computed from fractional-linear maps; field/sign doubts in source remain, P4."),
 "OP29":("refuted, with refined statement OP34","For normalized caseIII the identity group is positive real dilation, not Aff(1,C); n=1 model in OP34 supplies refinement."),
 "OP31":("independent re-proof","Finite analytic prime-end proof of the one-face-order>=3 sufficient condition, retaining isotopy THROUGH map automorphisms, P5."),
 "OP32":("computation or formal certificate","R=z^4/(4(z^2-1)) has passport(4)|(2,2)|(2,1,1); this refutes the proposed combinatorial exclusion list, not the sufficient condition."),
 "OP33":("used and rechecked in this run","Hua's already-existing positive-dilation orange counterexample checked against strict holomorphic models; explicit verification is OP34/P4."),
 "OP34":("computation or formal certificate","General F_n identities and interval-preimage argument verified in P4; symbolic identities checked for n=1..8 as supporting examples, not as induction."),
 "OP35":("refuted, with refined statement OP34","The claimed only-I/II/III list omits oranges n>=3, explicitly realized by strict F_n."),
 "OP37":("targeted proof check","Face-centre/edge-midpoint claims checked for I,II,III and F_n; no arbitrary-infinite-map uniqueness theorem inferred, P4."),
 "OP41":("targeted proof check","Exact sufficient local-index criterion checked by multiplication; <=2 alone does not imply index2 at other preimages, P2."),
 "OP43":("targeted proof check","Coefficient identity gives Q-equivariance and guarantees G_K-equivariance; no necessity/converse or only-G_K assertion retained, P7."),
 "OP44":("targeted proof check","Cleaned-sextic isomorphism factors into equality or target swap; passports and unique zero orders eliminate both ambiguities; reference-cover non-equivariance follows, P7."),
 "OP45":("targeted proof check","I invariant and Omega equivariant imply I composed Omega invariant; no completeness or within-orbit separation follows, P8."),
 "OP46":("targeted proof check","A transposition and a3-cycle do not commute in S3; Jones's wider-operation example is distinguished from rational postcomposition."),
 "SR05":("targeted proof check","Conditional degree identity 2(3N)=6N checked; for sextic degree6 gives36, while monodromy order720 gives4320, so a group-order reading needs extra conditions."),
 "SR06":("targeted proof check","Inertia cycle types(2,2) and(3,1) on four letters have identical two-element orbit sets and different ramification lengths."),
 "SR07":("targeted proof check","Double-counting darts proves vertex and face degree sums equal n; no catalogue-completeness claim inferred."),
 "SR09":("targeted proof check","Under D3=S3 convention, D3 x C2 is an extension of S3 by C2; dotted notation alone does not refute that group or determine an extension."),
}

roottext=(P/"root_research.md").read_text()+"\n"+(P/"root_research_supplement.md").read_text()
for ident,title in re.findall(r"^### ((?:BC|OP|SR)\d\d) — (.+)$",roottext,re.M):
    if ident in checks:
        kind,outcome=checks[ident]; event(ident,kind,outcome)
    else:
        event(ident,"used and rechecked in this run",
              "Post-freeze source/context comparison for '"+title+
              "'; wording, scope or missing proof distinguished in the note and root_context_search.json. This is not a mathematical proof of the source claim.")

event("ROOT-OPCERT-ATTEMPT-1","computation or formal certificate",
      "Initial auxiliary-script assertion failed: the handwritten-by-researcher expected rational denominator had constant+1 instead of-1. Script expectation corrected; no manuscript or research theorem altered.")
event("ROOT-OPCERT-ATTEMPT-2","computation or formal certificate",
      "Second draft assertion used SymPy structural equality for equivalent expanded/factored derivatives and failed. Changed to exact zero-remainder comparison; final assertions all passed.")
event("138:125:15-26 / 138-operations-subset-criterion","refuted, with refined statement OP12",
      "The CONTEXT formulation placing at-most-one marked point in A is refuted by A=[0,1]; source damaged syntax not overwritten. Corrected finite face-wise theorem separately stated.")
event("138:131:7-8","refuted, with refined statement OP34",
      "Positive dilations preserve every strict F_n orange for n>=2; already observed abstractly in Hua, now checked with exact strict models.")
event("138:130:27-131:8","refuted, with refined statement OP32",
      "Two-loop map has no face order>=3 but is neither I nor an orange; equality of proposed combinatorial exclusions fails.")
event("138-operations-belyi-extending","used and rechecked in this run",
      "Hua finding credited and compared with Wood primary source; exact local-index, endpoint and field-of-definition qualifications retained. No complete classification or priority claim.")

# Background here is the stated research interpretation/status, not an endorsement
# of an unproved manuscript theorem. ER17 has its separate actual proof-check event.
for i in range(1,21):
    ident=f"ER{i:02}"
    event(ident,"carried as background without fault found",
          "Used the bounded early-page report's source/context interpretation with its stated uncertainties and open status. No additional re-proof of the manuscript or LM claims is claimed by root.")
event("MM01","used and rechecked in this run",
      "Root compared scan98 definition with report: pinning labels degree-labelled S,A,F, not flags; conservativity and faithfulness kept distinct.")
for i in range(1,8):
    event(f"TA{i:02}","used and rechecked in this run",
          "Title/date/count classification compared with frozen sheet text and archive-comment convention; numbers not promoted to authorial pagination or a date of every mathematical layer.")

background={
 "Belyi Theorem4":"Primary Theorem4 used for the curve/three-point-cover equivalence; not independently reproved.",
 "Gonzalez-Diez--Jaikin-Zapirain Theorem18":"Primary theorem statement used only as a later regular-dessin faithfulness comparison; no proof recheck.",
 "Wood Proposition4":"Specific later orbit-separation example carried as a cited result; not recomputed.",
 "SGA1 XIII Corollary2.9 and Lemma2.11":"Primary statements and smooth-pair scope read; no re-proof of specialization theorem or raw functor representability.",
 "Constantin--Kolev Lemma2.4":"Plane-topology input to Proposition3.2 carried as background; its full proof not independently verified.",
}
for ident,outcome in background.items():event(ident,"carried as background without fault found",outcome)
event("Wood Definition3.1 / Proposition2","used and rechecked in this run",
      "Opened primary text; matched Q-definition and branch-set conditions; direct coefficient identity independently checks the equivariance implication.")
event("Jones Example7.7","used and rechecked in this run",
      "Root opened primary PDF printedp12 and compared its exact cubic/passport/S3/S6 claims with the independently completed arithmetic and permutation certificates; known example explicitly credited.")
event("Stacks 03QR","used and rechecked in this run",
      "Root opened primary lemma and checked finite orbit/fixed-field construction against the conditional finite-etale-algebra statements in MM11.")
event("Fulton 1969 bibliography","used and rechecked in this run",
      "Publisher record confirms title, volume90, pages542-575 and DOI; no theorem from the paper used as a checked premise.")

statuses={
 "EXIT_TOWER E.24":"Open; only finite examples supplied",
 "LM1 D.7":"Open; no Galois/GT/GT0 image equality inferred",
 "LM4 C.12":"Open; sphere isotopy example not its hyperbolic centralizer comparison",
 "LM4 D.12":"Open; one complex-conjugation test not a torsion classification",
 "LM4 D.32":"Register reports refereed proof as claimed; no re-proof here",
 "LM4_SUCCESSOR B.38":"Open; no congruence-kernel computation",
 "LM4_SUCCESSOR B.12":"Open; weighted orbifold comparison only",
 "LM6 F.35":"Proved return claim, not independently rechecked",
 "LM6 B.27":"Open; no centralizer solution",
 "LM7_PUSH E.3":"Open; small Kummer example not a CM image computation",
 "EXIT_TOWER E.49":"Explicitly unrefereed in supplied orientation; not used to settle E.3",
 "LM2 C.d1":"Unreviewed return claim; bridgeB5 comparison only",
 "LM2 C.r1":"Unreviewed return claim; not reproved",
 "LM2 C.r2":"Unreviewed return's refutation/correction claim; not reproved",
 "LM2 C.r3":"Unreviewed return claim; not reproved",
 "WG H1":"Unchecked hunch; not used as theorem",
 "WG H5":"Unchecked hunch; not used as theorem",
 "MPL_147_003-047 N075":"First-pass research lead; compatibility distinction used, cited later-paper claims not imported",
}
for ident,outcome in statuses.items():
    event(ident,"carried as background without fault found",
          "Supplied status and scope retained: "+outcome+". This event records use of the register, not validation of its underlying theorem.")

with (P/"root_check_events.tsv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=HEAD,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)

inputs=["early_check_events.tsv","maps_moduli_check_events.tsv","arithmetic_check_events.tsv",
        "operations_peer_check_events.tsv","b6_arithmetic_peer_events.tsv",
        "maps_moduli_supplement_check_events.tsv","root_check_events.tsv"]
merged=[]
for name in inputs:
    with (P/name).open(newline="") as f:
        rr=csv.DictReader(f,delimiter="\t")
        assert rr.fieldnames==HEAD,(name,rr.fieldnames)
        for row in rr:
            assert None not in row and all(row[k] for k in HEAD),(name,row)
            if row["type"]=="refuted":
                m=re.search(r"Refined statement ([A-Z]+\d+R)",row["outcome"])
                if m:row["type"]="refuted, with refined statement "+m.group(1)
            merged.append(row)
# Final mechanical events, once created, are retained on regeneration.
final=P/"final_check_events.tsv"
if final.exists():
    with final.open(newline="") as f:merged.extend(csv.DictReader(f,delimiter="\t"))
with (R/"CHECK_EVENTS.tsv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=HEAD,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(merged)
manifest=json.loads((P/"notes_assembly.json").read_text())
event_ids={r["statement_id"] for r in merged}
assert set(manifest["ids"])<=event_ids,sorted(set(manifest["ids"])-event_ids)
(P/"check_events_assembly.json").write_text(json.dumps(
    {"date":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
     "sources":inputs,"root_events":len(rows),"total_events":len(merged),
     "all_main_note_ids_have_scoped_event":True},indent=2)+"\n")
print(json.dumps({"root_events":len(rows),"total_events":len(merged),"all127notes_accounted":True}))
