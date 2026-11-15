#!/usr/bin/env python3
"""Prepare supplementary candidates only; no canonical notes or TeX writes."""
from pathlib import Path
import json,re,subprocess,hashlib
R=Path(__file__).resolve().parent.parent
C=R.parent/"context"
notes=[]
ORG="WG2 §1.1 #3 [unchecked organizational plan; no topical settled result ID]"
def add(id,title,kind,location,quote,terms,context,body,ledger=ORG):
    notes.append(dict(id=id,title=title,kind=kind,location=location,quote=quote,
                      terms=terms,context=context,ledger=ledger,body=body))
add("R12","The requested generalization involving sl₂ has no supplied proof",
 "self-flagged","15/196:L8",r"généralisations des prop. 5 et 6",
 ["sl_2","Lefschetzien","produit"],
 "Adds a separate representation-theory task; CT16/018 (MPL_16+47+54+44_transcription.tex, L694–724) concerns a graded Lefschetz correspondence ring, not the referenced propositions.",
 "The redactor is asked to generalize two propositions to the indicated algebras, whose form is written with the words commutative and x sl₂, but those propositions are not reproduced here. The task is a deferred mathematical generalization whose precise algebra, representation class and coefficient assumptions remain to be recovered. Shared sl₂ terminology supplies no identification with the neighbouring motivic or Lefschetz group.",
 "WG2 §2.4 #3 [unchecked plan]; MPL_14_087-132 M04 [first-pass subgroup-comparison lead, different assertion]")
add("R13","Splitness and diagonalizability are explicit missing qualifications",
 "reading question","15/196:L12",r"couple $(\underline{g},\underline{h})$",
 ["déploi","diagonal","semi-simple"],
 "Differs from CT16/048–049's semisimplicity programme; no definition of the requested split Lie pair was found in the supplied CT/CN files.",
 "The requested definition uses the written pair (g,h), and the instruction distinguishes semisimplicity of an adjoint operator from diagonalizability over the ground field. Those conditions differ unless the relevant eigenvalues already lie in that field. The missing definition and coefficient hypotheses must be recovered before treating the instruction as a completed splitness argument.")
add("R14","Root-vector normalization and the requested theorem proof remain separate tasks",
 "self-flagged","15/196:L16–18,24","démontrer le th. 3, c)",
 ["racines","Cartan",r"\varphi"],
 "Adds proof/normalization requests to CT44/005's cancelled root-data draft and CT44/007's root-system comments (CT L2889–2937,2948–2964); neither states the referenced Theorem 3(c).",
 "The sheet requests a proof of Theorem 3(c), explicit root isomorphisms and a one-dimensional Cartan subspace, then fixes representatives of opposite roots and corresponding root vectors. These are mathematical normalization and proof requirements beyond title changes. The original theorem is absent, so its conclusion and compatibility conditions cannot be reconstructed from the instructions alone.")
add("R15","Highest-weight alternatives and divided-power stability need source hypotheses",
 "unpursued implication","15/198:L6–8;15/200:L22",
 r"ajouter la stabilité par les binomiaux $\binom{H}{n}$",
 ["puissances divis","binom","entier",r"\mathbb Z"],
 "Adds divided-power/binomial-operator requirements to the integral-operator concerns of CT16/014–018 (especially CT L507–525); CT47/009's integrality formula is a different problem.",
 "The requested highest-weight corollary separates an indefinitely independent sequence from one terminating at an integral weight, while the exercise must additionally require stability under binomial operators. The next paragraph normalizes the generator and basis with factorial denominators, and scan 200 requests a generating-series exercise. The coefficient ring, highest-weight hypotheses and intended lattice must be recovered before identifying these constructions with an integral Lefschetz model.",
 "WG2 §2.3 #3 [unchecked plan about a different integral Lefschetz failure]; no settled entry for this representation task")
add("R16","The group-representation and fourth-power claims exceed the dimension correction",
 "reading question","15/198:L16",r"$\unsure{\theta|\varphi}^4=1$",
 ["holomorphe","représentations","exponentielle","Tribu"],
 "No matching holomorphic-representation or exponential statement was found in CT/CN; CT44/007's Tribu comments (CT L2954–2962) provide a reuse parallel, not the missing group or operator.",
 "Besides R02's finite-dimensional restriction, the paragraph claims that the indicated representations exhaust the irreducible holomorphic representations of G, defers exponentials to another chapter, and imposes a fourth-power identity. The definition and global form of G and the identity of the uncertain operator must come from the absent source pages. Neither assertion follows merely from adding finite dimensionality.")
add("R17","Cartan conjugacy must retain its specified acting group",
 "unproved claim","15/200:L6,10","opère transitivement",
 ["Cartan","Autel","transitiv"],
 "Differs from CT16/026's extension of a generic Cartan subgroup after shrinking the base (CT L1091; CN16:26); that erratum supplies no Autel-action proof.",
 "The requested revisions assert invariance of the subgroup written Autel and state Cartan conjugacy as transitivity of its action. This specifies more than an abstract isomorphism between Cartans. The definition of Autel, field assumptions and original theorem are needed to evaluate the revision.")
add("R18","The added Cartan and regular-element propositions are distinct claims",
 "unproved claim","15/200:L12–14;15/202:L8,16","Ajouter la prop. suivante",
 ["Cartan","régulier","nilespace"],
 "Adds Lie-subalgebra inheritance and regular-element assertions, differing from CT16/026's relative group-scheme Cartan extension (CT L1091); the supplied CT/CN do not prove the new propositions.",
 "The added proposition on scan 202 relates Cartan inheritance, regularity and nilespaces for nested Lie algebras, while scan 200 requests a corollary with equal-rank and regular-element hypotheses. A further instruction says that every subalgebra containing a Cartan equals its normalizer. These claims need their field, dimension and nilpotence assumptions and proofs; the adjacent positive-characteristic corrections make those qualifications material.")
add("R19","Restriction of scalars in the Cartan assertion needs a dimensional convention",
 "reading question","15/200:L16",
 r"les Cartans de $\underline{g}$ considérée comme algèbre sur $k$ sont les mêmes",
 ["Cartan","sous-corps","restriction des scalaires"],
 "Differs from CT16/026's shrinking-base Cartan extension (CT L1091); the searched CT/CN supply no restriction-of-scalars theorem for these Lie algebras.",
 "The addition quantifies over a subfield k of K and asserts equality of the Cartan subalgebras when the same Lie algebra is viewed over either field. If K/k is infinite, finite dimensionality over K does not imply finite dimensionality over k, so the permitted category and definition of Cartan must be explicit. The sheet gives no finite-extension restriction and no proof of this scalar-change assertion.")
add("R20","The reused Lefschetz-principle lemma belongs to an analytic-group argument",
 "self-flagged","15/204:L20;15/202:L6",
 "On donnera le principe de Lefschetz comme lemme.",
 ["principe de Lefschetz","groupe analytique","valeur propre","Lefschetz"],
 "The exact principle/analytic-group statement was not found in CT/CN; it differs from CT16/006–018's cohomological operators and correspondence rings.",
 "The relocated statement starts on typed leaf (3), scan 204, and continues on typed leaf (4), scan 202: it bounds the multiplicity of the eigenvalue 1 of Ad(x) on a suitable open subgroup. The next instruction requests a Lefschetz-principle lemma and the connected real/complex conclusion U=G. The principle is not stated here and must not be silently identified with hard Lefschetz or a motivic subgroup construction.",
 "WG2 §2.4 #3 [unchecked plan, subject distinction]; MPL_14_087-132 M04 [first-pass subgroup-comparison lead, different assertion]")
add("R21","The eigenvalue erratum and Galois descent are explicitly deferred",
 "self-flagged","15/204:L12–14","sera faite en Alg. VII",
 ["Galois","descente","valeurs propres"],
 "Differs from CT16/056's faithfully flat descent of module properties (CT L2032) and CT16/052's Kummer extensions (CT L1922); neither supplies this Lie-module proof.",
 "The text relies on a future eigenvalue erratum, removes a nilpotence hypothesis and warns that the simple-quotient argument is unavailable in characteristic p. It then delegates descent to Algèbre VII and replaces the algebraic closure by an arbitrary Galois extension. The missing source definitions must determine the generalized-eigenspace and descent conventions; these instructions do not prove the revised argument.")
add("R22","The replacement nilpotence claim retains unresolved Ad notation",
 "reading question","15/204:L18",r"nilpotence de $\operatorname{Ad}(x)$",
 ["nilpotent","Ad(","ad("],
 "Differs from CT16/017's graded-operator discussion and CT16/054's nilpotent-thickening programme; no matching adjoint-nilpotence assertion was found in CT/CN.",
 "After deleting Proposition 5, the editor requests a remark asserting nilpotence of the literally written Ad(x) under Proposition 4's conditions. That proposition and the notation convention are absent. The transcription therefore does not authorize replacing Ad by ad or treating this as a proved statement about an adjoint group automorphism.")
add("R23","The infinite-module and invariant-operator supplement remains a programme",
 "self-flagged","15/206:L14",r"Les modules infinis $W(\lambda)$",
 ["Harish","Casimir","modules","semi-simple"],
 "Adds an infinite-dimensional representation programme, differing from CT16/048–049's finite-dimensional correspondence-algebra semisimplicity; CT/CN contain no matching Harish-Chandra or Casimir theorem.",
 "The next redactor is asked to add infinite modules W(λ), Harish-Chandra formulas and results on invariant differential operators. No formulas, parameter restrictions or theorem statements are supplied by this programme line. It cannot inherit R02's finite-dimensional complete-reducibility justification or establish motivic semisimplicity.",
 "WG2 §2.3 #7 [unchecked semisimplicity plan, different subject]; no settled result ID for this supplement")
add("R24","Triality is an explicit omitted construction request",
 "self-flagged","15/206:L18",r"montrer les autom. de trialité de $D_4$",
 ["trialité","D_4","classique","racines"],
 "Adds a triality request to CT44/005,007's root-data/editorial material (CT L2889–2937,2954–2962); no D4-triality construction was found in CT/CN.",
 "The programme requests the classical split Lie algebras and fundamental representations, explicitly requires a demonstration of D4 triality, and assigns exceptional algebras to exercises. No construction or verification of those automorphisms appears here. The restriction to Lie-algebra representations must remain attached to the request instead of becoming a statement about every global group form.")
add("R25","Cartier's integral Lie-theory supplement is assigned but not supplied",
 "self-flagged","15/206:L20",
 r"Cartier rédigera un tapis arithmétique sur les $Z$-structures.",
 ["Cartier",r"\mathbb Z","intégral","sur Z"],
 "Adds an assigned integral Lie-theory project, distinct from CT16/014–018's integral Lefschetz model (especially CT L507–525) and CT54/007's p-primary comparison.",
 "The sentence assigns Cartier a future arithmetic treatment of Z-structures, while other supplements are described as discarded or incorporated. It supplies neither an integral Lie algebra nor a theorem about reduction or representations. This is an additional programme, not a repair of the different integral Lefschetz failures recorded in the ledger.",
 "WG2 §2.3 #3 [unchecked plan about integral Lefschetz failures; thematic comparison only]")
add("R26","The density clause requires the missing irreducibility convention",
 "reading question","15/206:L26–28",
 "En particulier toutou vert non vide est dense",
 ["Zariski","non vide","dense","régulier"],
 "No matching Appendix I Proposition 1 was found in CT/CN; CT16/019's regular-scheme passage (CT L753) is different and supplies no density hypothesis.",
 "The editor asks that Proposition 1 include density of every nonempty open and that its proof be given by references, then specifies Zariski topologies in the next item. Such density requires irreducibility of the relevant space, possibly already built into the missing definition of variety. Without Proposition 1 and its conventions, the instruction cannot be asserted for arbitrary reducible spaces.")
add("A41","The inserted local-case assertion lacks a recoverable precise hypothesis",
 "reading question","15/225:L4–8",
 r"Vrai pour un schéma \unsure{$k$ local}, et pour le premier \unsure{cas}",
 ["k local","schéma local","Hodge"],
 "Adds an uncertain restricted case to the Hodge/place question; CT54/003,005 and CT44/008 discuss Hodge realizations but supply no definition identifying this local-scheme condition.",
 "The insertion asserts a true restricted case between an aborted opening and the cancelled reduction, but both the local condition and the reference to a first case remain uncertain. It does not specify whether the restriction concerns a local scheme, its base field or another already discussed case. A37's general Hodge-enrichment question needs this unresolved qualifier rather than an inferred local theorem.",
 "MPL_14_002-044 M24a [first-pass abelian-realization lead]; WG2 §2.4 #3 [unchecked reconstruction plan]")

for n in notes:
    passages=[]
    for cote,scan,segs in re.findall(r"(15)/(\d+):L([0-9,–-]+)",n["location"]):
        ss=(R/"pages"/f"{R.name}_{cote}_scan{int(scan):03d}.tex").read_text().splitlines()
        for seg in segs.split(","):
            ns=re.split("[–-]",seg);a=int(ns[0]);b=int(ns[-1])
            passages.append("\n".join(ss[a-1:b]))
    if " ".join(n["quote"].split()) not in " ".join("\n".join(passages).split()):
        raise RuntimeError("Quote mismatch "+n["id"])
    if set(n)!={"id","title","kind","location","quote","terms","context","ledger","body"}:
        raise RuntimeError("Incorrect schema")
paths=[C/"MPL_16+47+54+44_transcription.tex",C/"MPL_16+47+54+44_notes.md"]
maps={}
for p in paths:
    cote=scan=None;mapping={}
    for i,s in enumerate(p.read_text().splitlines(),1):
        m=re.search(r"\\cotefile\{([^}]+)\}",s)
        if m:cote=m.group(1)
        m=re.search(r"\\scanpage\{([^}]+)\}",s)
        if m:scan=m.group(1)
        mapping[i]=(cote,scan)
    maps[str(p)]=mapping
audit=[]
for n in notes:
    cmd=["rg","-n","-i","--fixed-strings","--with-filename"]
    for term in n["terms"]:cmd+=["-e",term]
    result=subprocess.run(cmd+list(map(str,paths)),text=True,capture_output=True)
    if result.returncode not in (0,1):raise RuntimeError(result.stderr)
    hits=[]
    for line in result.stdout.splitlines():
        p,num,excerpt=line.split(":",2);num=int(num);cote,scan=maps[p][num]
        hits.append(dict(file=Path(p).name,line=num,cote=cote,scan=scan,excerpt=excerpt[:260]))
    audit.append(dict(id=n["id"],terms=n["terms"],match_count=len(hits),
                      searched_files=[p.name for p in paths],hits=hits,
                      selected_context=n["context"],ledger=n["ledger"]))
frozen=json.loads((R/"records/frozen_manifest.json").read_text())["sha256"]
for p,v in frozen.items():
    if hashlib.sha256((R/p).read_bytes()).hexdigest()!=v:raise RuntimeError("Frozen mismatch "+p)
(R/"records/research_cote15_extra_notes.json").write_text(json.dumps(notes,ensure_ascii=False,indent=2)+"\n")
(R/"records/research_cote15_extra_context_searches.json").write_text(json.dumps(audit,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"notes":len(notes),"ids":[n["id"] for n in notes],"queries":len(audit),
                  "schema":"nine required fields","frozen_checked":len(frozen)},indent=2))
