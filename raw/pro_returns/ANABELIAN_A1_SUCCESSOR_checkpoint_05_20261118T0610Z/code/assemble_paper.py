"""Assemble the continuing paper, retaining every numbered assertion.

The supplied flattened source is an input, never silently treated as a
verified result. Actual check records determine the two-part placement.
"""
import csv
import json
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
BASE = WORK.parent / "background/A1_checkpoint03"
REG = json.loads((WORK / "notes/statement_registry.json").read_text())
META = json.loads((WORK / "notes/consolidated_metadata.json").read_text()) if (WORK / "notes/consolidated_metadata.json").exists() else {}
NUMBERS = json.loads((BASE / "notes/statement_number_map.json").read_text())
NUMBERS.update({f"A.DC{i}": f"A.{44+i}" for i in range(1, 5)})
NUMBERS.update({f"B.N4.{i}": f"B.{89+i}" for i in range(1, 8)})
NUMBERS.update({f"B.N3.{i}": f"B.{96+i}" for i in range(1, 10)})
NUMBERS.update({f"B.B8.{i}": f"B.{105+i}" for i in range(1, 6)})
NUMBERS.update({f"B.N2.{i}": f"B.{110+i}" for i in range(1, 9)})
NUMBERS.update({f"B.META.{i}": f"B.{118+i}" for i in range(1, 6)})
NUMBERS["B.META.6"] = "B.126"
NUMBERS["B.META.7"] = "B.127"
NUMBERS["B.META.8"] = "B.128"
NUMBERS["B.META.9"] = "B.129"
NUMBERS["B.META.10"] = "B.131"
NUMBERS["B.META.11"] = "B.132"
NUMBERS["B.META.12"] = "B.133"
NUMBERS["B.META.13"] = "B.134"
NUMBERS["B.META.14"] = "B.136"
NUMBERS["B.META.15"] = "B.139"
NUMBERS["B.META.16"] = "B.140"
NUMBERS["B.META.17"] = "B.142"
NUMBERS["B.META.18"] = "B.143"
NUMBERS["B.META.19"] = "B.144"
NUMBERS["B.META.20"] = "B.146"
NUMBERS["B.META.21"] = "B.147"
ALIASES = {"ST2009": "LA_ST2009", "ST2017": "LA_ST2017",
    "CF_Milne2013": "MilneEtale", "CF_Bellingeri2004": "Bellingeri2004",
    "CF_MT2008": "LA_MT2008", "CF_Stix2005": "LA_Stix2005",
    "CF_SGA1": "LA_SGA1", "AN_SGA1": "LA_SGA1",
    "AN_CHW2024": "CarlsonHaineWolf2024",
    "AN_Rousseau1969": "Rousseau1969"}

def transform(s):
    s = s.replace("predecessor.\\citep", "predecessor. \\citep")
    # The supplied flattened predecessor mapped only the first endpoint of
    # these abbreviated working-number ranges. Restore both verified endpoints.
    legacy_ranges = {
        'B.62--5': 'B.62--B.66', 'B.56--13': 'B.56--B.57',
        'B.48--7': 'B.48--B.49', 'B.57--14': 'B.57--B.58',
        'B.59--17': 'B.59--B.61', 'B.49--9': 'B.49--B.51',
        'B.54--6': 'B.54--B.55', 'B.36--4': 'B.36--B.38',
    }
    for before, after in legacy_ranges.items():
        s = re.sub(re.escape(before) + r'(?![0-9])', after, s)
    # Expand abbreviated working-number ranges before their endpoints are mapped.
    s = re.sub(r"(B\.(?:N[234]|B8|META)\.)([0-9]+)--([0-9]+)", r"\1\2--\1\3", s)
    s = re.sub(r"([ABC]\.[A-Z]+)([0-9]+)--([0-9]+)", r"\1\2--\1\3", s)
    for key in sorted(NUMBERS, key=len, reverse=True):
        s = re.sub(re.escape(key) + r"(?![0-9A-Za-z]|\.[0-9A-Za-z])", NUMBERS[key], s)
    for key, value in ALIASES.items():
        s = s.replace("{" + key + "}", "{" + value + "}")
    s = re.sub(r"\\begin\{claim\}\{([^}]+)\}\{Refuted\}", r"\\begin{claim}{\1}{False as stated}", s)
    s = re.sub(r"(\\begin\{claim\}\{[^}]+\}\{)Proved[^}]*\}", r"\1Proved}", s)
    s = s.replace("{Known, with derivation}", "{Known}")
    return s

def ranges(s):
    found = list(re.finditer(r"\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}", s))
    result = []
    for k, match in enumerate(found):
        limit = found[k+1].start() if k+1 < len(found) else len(s)
        end_claim = s.index(r"\end{claim}", match.end()) + len(r"\end{claim}")
        end_proof = s.find(r"\end{proof}", end_claim, limit)
        if end_proof >= 0:
            end = end_proof + len(r"\end{proof}")
        else:
            heads = [s.find(x, end_claim, limit) for x in (r"\subsection", r"\section", r"\bibliographystyle")]
            end = min([x for x in heads if x >= 0] + [limit])
        result.append((match.group(1), match.group(2), match.start(), end))
    return result

def replace_claim(s, ident, replacement):
    for key, status, begin, end in ranges(s):
        if key == ident:
            return s[:begin] + replacement.strip() + s[end:]
    raise ValueError(ident)

def latex_escape(s):
    s = re.sub(r'([,;])(?=\S)',r'\1 ',s)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#")]:
        s = s.replace(a, b)
    s = re.sub(r'\b[0-9a-f]{64}\b', lambda m: r'\allowbreak{}'.join(m.group()[i:i+8] for i in range(0,64,8)), s)
    return s

original = (BASE / "ANABELIAN_A1_paper.tex").read_text()
preamble, rest = original.split(r"\begin{document}", 1)
preamble = preamble.replace(r"\usepackage[numbers,sort&compress]{natbib}", r"\usepackage[authoryear,round]{natbib}")
preamble = preamble.replace(r"\setlength{\emergencystretch}{2em}", r"\setlength{\emergencystretch}{3em}")
preamble = re.sub(r"\\title\{.*?\}\n\\author", r"\\title{ANABELIAN\\_A1\\_SUCCESSOR\\\\Point sections, cuspidal exactness, and arithmetic continuations}\n\\author", preamble, flags=re.S)
preamble = preamble.replace("17 November 2026", "18 November 2026")
preamble += "\n\\newtheorem{lemma}{Lemma}\n\\newtheorem{remark}[lemma]{Remark}\n"
preamble += "\n\\tracinglostchars=3\n"
preamble += "\\setlength{\\tabcolsep}{5.8pt}\n"
body = rest[rest.index(r"\section{The point-separation argument}"):rest.index(r"\bibliographystyle")]
body = transform(body)

# The old broad criterion is retained, but its proof now cites the separated
# steps so that the alternatives cannot inherit the finiteness dependency.
old19 = r"""
\begin{claim}{A.19}{Proved}{The cuspidal criterion with finite exceptional support}
Let $k$ be finite of characteristic $p$, let $C/k$ be smooth proper
geometrically connected of genus at least two, and let $P,Q\in C(k)$.
For $r\ne p$, a cusp-preserving isomorphism $G_P\simeq G_Q$ of the
arithmetic relative cuspidally pro-$r$ quotients over
$\operatorname{id}_{\Pi_C}$ forces $P=Q$.
\end{claim}
\begin{proof}
A.49 carries every noncuspidal point section to an actual point
section in the whole target quotient. A.16 identifies its label with
the original point outside one finite exceptional image, uniformly
over all finite residue fields. Thus the hypothesis of A.44 holds.
A.42 constructs the full central extensions and their difference
cocycle, A.43 evaluates it at each unchanged label, and A.44 gives
the contradiction. Each of those arguments is written out separately
below. This proof uses A.16. The alternative proof A.20--A.21 cites
A.42--A.43 and A.49 directly and has no such dependency.
\end{proof}
"""
body = replace_claim(body, "A.19", old19)

intro_start = body.index(r"\begin{claim}{A.1}")
intro_end = next(x[3] for x in ranges(body) if x[0] == "A.1")
intro = body[intro_start:intro_end]
proof_start = intro.index(r"\begin{proof}")
intro = intro[:proof_start] + r"""\begin{proof}
Fix $r\ne p$. A.45 extends every finite $r$-group fibre torsor in
the labelled product family, and A.46 proves tame right exactness.
The finite proper-cover and core argument in A.13 therefore gives
the relative configuration sequence. A.47 proves survival of full
$r$-adic cusp inertia algebraically; A.48 constructs the diagonal
boundary group and transports the actual cusp between the two
arithmetic fibres whenever the proper sections are geometrically
conjugate. It retains the entire $G_k$ and is over the identity of
$\Pi_C$.

A.14--A.15 and A.49 recognize the transported noncuspidal sections
as actual points. B.68 identifies their abelian differences with
the positive Kummer classes, so A.21 puts all potentially changed
labels in a proper support field. A.42--A.43 construct and evaluate
the central difference cocycle. A.20's Kummer cover and Weil-bound
argument then force $P=Q$. This chain uses neither lifting to
characteristic zero nor finite exceptional support. Alternatively,
A.16 and A.44 give the finite-exception endgame A.19. The
topological proof A.2--A.5 is retained as a separately checked
route, rather than a dependency of the direct route.

Every argument applies over any finite constant extension $L/k$.
Thus the conclusion is the asserted all-extension injectivity in
the entire arithmetic quotient, under conjugation by its entire
geometric subgroup.
\end{proof}
"""
body = body[:intro_start] + intro + body[intro_end:]

# Optional replacement prepared by the independent configuration reader.
gen15 = WORK / "configuration/A15_general.tex"
if gen15.exists():
    t = transform(gen15.read_text())
    rr = ranges(t)
    if rr:
        body = replace_claim(body, "A.15", t[rr[0][2]:rr[0][3]])
gen35 = WORK / "configuration/A35_repaired.tex"
if gen35.exists():
    t = transform(gen35.read_text())
    rr = ranges(t)
    if rr:
        body = replace_claim(body, "A.35", t[rr[0][2]:rr[0][3]])
for ident, filename in [
    ("A.37", "A37_scope_corrected.tex"),
    ("A.39", "A39_corollary.tex"),
    ("C.9", "C9_scope_corrected.tex"),
    ("C.12", "C12_scope_corrected.tex"),
]:
    p = WORK / "configuration" / filename
    if p.exists():
        t = transform(p.read_text())
        rr = ranges(t)
        if rr:
            body = replace_claim(body, ident, t[rr[0][2]:rr[0][3]])

# Expand the direct algebraic replacement at the preserved number A.13.
direct = WORK / "configuration/direct_characteristic_p.tex"
if direct.exists():
    d = transform(direct.read_text())
    head = r"\paragraph{The repaired proof of A.13 (paper A.13).}"
    start = d.find(head)
    if start < 0:
        start = d.find(r"\paragraph{The repaired proof of")
    stop = d.find(r"\begin{claim}{A.47}", start)
    if start >= 0 and stop > start:
        repair = d[d.find("\n", start)+1:stop]
        claim13 = next(x for x in ranges(body) if x[0] == "A.13")
        txt13 = body[claim13[2]:claim13[3]]
        txt13 = txt13[:txt13.index(r"\begin{proof}")] + "\\begin{proof}\n" + repair + "\n\\end{proof}\n"
        body = replace_claim(body, "A.13", txt13)
        d = d[:start] + d[stop:]
    direct_text = d
else:
    direct_text = ""

# Remove the explicit transport assumption where the stronger proof supplies it.
body = body.replace("Assume the cuspidal transport construction from equal point sections\nhas been established for a prime set $\\Sigma$ containing some\n$r\\ne p$, allowing $p\\in\\Sigma$. Then", "Let $\\Sigma$ contain a prime $r\\ne p$, allowing $p\\in\\Sigma$. The\ntransport theorem A.48 applies, and")
body = body.replace("If the configuration transport is verified for every such \\(\\Sigma\\)", "Since A.48 proves the configuration transport for every such \\(\\Sigma\\)")
body = body.replace("If the configuration transport is verified for every such \\({\\Sigma}\\)", "Since A.48 proves the configuration transport for every such \\({\\Sigma}\\)")
body = body.replace("again under the generalized transport theorem", "by the generalized transport theorem A.48")
body = body.replace("already been proved in the Kummer step of \\statementref{A.19}", "proved directly in B.68")
body = body.replace("which has proved directly in B.68", "which has been proved directly in B.68")
body = body.replace("the exact cuspidal transport and \\statementref{A.19}; the latter\nmay use its independent support-field proof\n\\statementref{A.21}.", "the point-separation theorem A.1, using its direct support-field route. The point-to-section Kummer comparison is B.68.")
body = body.replace("Hence the conditional criterion\n\\statementref{A.19} admits a proof using", "Hence the cuspidal criterion admits a proof from A.42--A.43 and A.49, using")
body = body.replace("Only the final Kummer argument changes.", "We use A.42 for the full central extensions and the residue cocycle, A.43 for same-label evaluation, and A.49 for point recognition. None of these uses A.16. The final Kummer argument is as follows.")
body = body.replace("Consequently, after the independent verification of AG.41 and AG.42, this is an alternative complete route to the main theorem. The original K1 audit remains useful for checking the earlier proof exactly as written, but it is not an indispensable external premise of this replacement proof.", "Together with A.45--A.48 and the finite-core proof in A.13, this gives the direct route to A.1, without an exceptional-set finiteness input.")

# The norm proof and its uniform tame-grid transfer settle both named families.
body = body.replace("They do not decide reconstruction at that union.", "B.138 below proves reconstruction at that union and every finite extension for every prime, including $2,3$; the kernel assertions here are retained unchanged.")
body = body.replace("The unbounded tower therefore still requires a separate\nreconstruction argument.", "The separate reconstruction argument is supplied for every prime in B.137--B.138 below.")
body = body.replace("It leaves open the bounded derived-length\nfield \\(B_p=\\overline\\Q^{I^{(2)}}\\), and the lower-central union\n\\(\\bigcup_c\\overline\\Q^{\\gamma_{c+1}(I)}\\).", "The bounded derived-length field $B_p$ and the lower-central union are different fields; B.136 and B.138 respectively prove their reconstruction below.")
body = replace_claim(body, "B.52", (WORK / "sections/B8_remaining_scope.tex").read_text())

# Replace an unnecessarily strong wild-freeness input by a direct finite argument.
old_nonabelian = r"""Such an
\(x\) exists because \(I'\) is a nontrivial closed subgroup
of the free wild pro-\(p\) group, hence has nontrivial
abelianization; multiplying an element of \(B_p\setminus F_p\)
by a sufficiently large power of \(p\) ensures positive value.
This is also the nontriviality argument in AS-FF.40."""
new_nonabelian = r"""Such an \(x\) exists by the following elementary argument.
The commutator group \(I'\) is pro-\(p\), since tame inertia
is abelian. It is nontrivial. For odd \(p\), the splitting
field of \(X^p-p\) over \(K_p\) has nonabelian group
\(C_p\rtimes(\mathbf Z/p)^\times\): Eisenstein gives the
radical degree \(p\), the cyclotomic degree is \(p-1\),
and the scalar action is faithful. For \(p=2\), put
\(\beta=2^{1/4}\). The polynomial \(X^4-2\) is Eisenstein,
so \([K_2(\beta):K_2]=4\). The distinct quadratic fields
\(K_2(\sqrt2)\) and \(K_2(i)\) have compositum of degree
four: their equality would make \(-2\) a square in \(K_2\),
contrary to its odd valuation. This compositum does not contain
\(\beta\). Indeed, writing \(\beta=a+bi\) with
\(a,b\in K_2(\sqrt2)\) and squaring would force \(ab=0\);
then \(\sqrt2\) or \(-\sqrt2\) would be a square in that
field, contrary to its value group \(\tfrac12\mathbf Z\).
Hence \(i\notin K_2(\beta)\), and the splitting field has
the nonabelian dihedral group of order eight. Every nontrivial
pro-\(p\) group has a nontrivial finite \(p\)-group quotient,
and then a quotient of order \(p\). Thus \(I'/I''\ne1\),
so \(B_p\ne F_p\). Multiplication by a large power of \(p\)
makes an element of \(B_p\setminus F_p\) have positive value."""
body = body.replace(old_nonabelian, new_nonabelian)

# Fix the variance convention explicitly for the reconstructed site equivalence.
claim49 = next(x for x in ranges(body) if x[0] == "B.49")
part49 = body[claim49[2]:claim49[3]]
part49 = part49.replace(r"\begin{proof}", r"""\begin{proof}
We use the inverse-image orientation: a covering with target puncture
set $F(S)$ is sent to the corresponding covering with source puncture
set $S$. With this orientation the induced map on underlying points
is $F$. Transport in the reverse direction constructs its inverse.
""", 1)
body = body[:claim49[2]] + part49 + body[claim49[3]:]

# B.45 is a recorded consequence rather than an unproved cross-reference.
claim45 = next(x for x in ranges(body) if x[0] == "B.45")
part45 = body[claim45[2]:claim45[3]]
if r"\begin{proof}" not in part45:
    proof45 = r"""
\begin{proof}
B.62 supplies coherent relative realization and its slice compatibility
from the ordinary pro-category data. B.63 compares the whole Kummer
system after one finitely generated refinement. B.64 then recovers an
actual value over the fixed source field. B.65 reconstructs that
representative and its entire inverse-image functor, and B.66 descends
the resulting morphism independently of the target level. Thus the
ordinary pro-category formulation is fully faithful in the asserted
arbitrary transcendence degree. The example in B.44 concerns only the
different category with pinned transition arrows.
\end{proof}
"""
    body = body[:claim45[3]] + proof45 + body[claim45[3]:]

extra_a = []
for f in ["sections/A_split_criterion.tex", "sections/A_recognition.tex", "finite_checks/finite_checks.tex", "configuration/A53_finite_sigma_density.tex", "configuration/A54_frobenius_gate.tex", "configuration/A55_finite_sigma_not_large.tex", "configuration/A56_restricted_tower_bound.tex", "configuration/A57_retained_p_detection.tex", "configuration/A58_abstract_automorphism_obstruction.tex", "configuration/A59_alternating_tower.tex", "configuration/A60_frobenius_order_jump.tex", "configuration/A61_first_alternation_obstruction.tex", "configuration/A12_source_scope.tex"]:
    p = WORK / f
    if p.exists(): extra_a.append(transform(p.read_text()))
extra_a.insert(1, direct_text)
for f in ["configuration/S1_comparison.tex", "configuration/configuration_sources.tex", "configuration/source_dependency_audit.tex", "configuration/literature_audit_successor.tex"]:
    p = WORK / f
    if p.exists(): extra_a.append(transform(p.read_text()))
extra_b = []
for f in ["sections/B_N1.tex", "finite_checks/quartic_all3.tex", "finite_checks/quartic_census.tex", "finite_checks/b5_cyclic7.tex", "finite_checks/b5_all_f8.tex", "finite_checks/b5_fourbranch.tex", "finite_checks/b5_genus2_positive.tex", "finite_checks/b4_finite_avoidance.tex", "finite_checks/s2_pro3_separator.tex", "finite_checks/b1_finite_prime_obstruction.tex", "arithmetic_notes/N4.tex", "arithmetic_notes/N3.tex", "sections/B_N3_lattice.tex", "arithmetic_notes/B8_norm_reconstruction.tex", "arithmetic_notes/N2.tex", "arithmetic_notes/B8_metabelian.tex", "sections/B_norm_zero_families.tex", "arithmetic_notes/B8_local_analysis.tex", "sections/B_finite_logarithmic_grid.tex", "arithmetic_notes/B8_norm_metabelian.tex", "sections/B_small_prime_nilpotent.tex", "arithmetic_notes/B8_relative_local.tex", "finite_checks/b1_canonical_point.tex", "arithmetic_notes/B8_normal_extensions.tex", "arithmetic_notes/B8_procyclic_obstruction.tex", "finite_checks/b1_automorphism_orbits.tex", "arithmetic_notes/B8_discrete_residue.tex", "configuration/B43_55_source_audit.tex"]:
    p = WORK / f
    if p.exists(): extra_b.append(transform(p.read_text()))
body = body.replace(r"\section{Independent existence and reconstruction questions}", "\n" + "\n".join(extra_a) + "\n\\section{Independent existence and reconstruction questions}")
body = body.replace(r"\section{Consequences and limits}", "\n" + "\n".join(extra_b) + "\n\\section{Consequences and limits}")

# Produce check records and keep genuinely unchecked proof blocks together.
unchecked = []
gate_updates = {
 'A.28': r"A.53--A.61 add the all-cover Frobenius-order criterion, its retained-characteristic-prime extension, precise limitations of finite-prime and bounded-generator methods, an explicit cofinal alternating homology tower over the fixed finite field, an actual first arithmetic order jump, and the precise orbit/multiplicity thresholds for a second factor. The remaining universal task is to determine whether the omitted-prime orders on this tower are unbounded and, when the action is faithful, to decide point separation.",
 'B.5': r"B.89 proves that any prescribed finite set of admissible odd primes can fail permanently for suitable pointed curves of each fixed genus and characteristic. Thus no witness-prime bound depending only on these two integers can settle the unrestricted question, including its displayed large-characteristic range. B.141 removes the entire genus-two marked-curve locus with a nonzero canonical-point class modulo some admissible odd prime of even p-order; its explicit congruence family includes characteristics above that threshold. B.145 proves the broader automorphism-eigencharacter criterion in every genus, including a genus-three quartic family with all constant-extension tests.",
 'B.12': r"B.130 removes two complete nonempty geometric genus-two families from this gate: the ordinary cubic locus of B.85 and the two-rank-one quintic locus of B.86. Every finite-field form, finite extension and rational pointing in those families has no all-level free fixed norm vector. The other genus-two loci and the general all-level existence assertion remain undecided.",
 'B.24': r"B.85--B.86 prove primitive-zero covers on the two stated genus-two loci. B.87 shows that no fixed finite list of odd cyclic degrees suffices for all ordinary genus-two curves. It does not provide a single curve avoiding every odd degree, and the degree-one-allowed universal assertion remains open.",
 'B.32': r"B.145 settles the quartic $Y^3Z-YZ^3=X^4$ over $\mathbf F_3$ at its earliest witness field, for all four original rational markings: the exact field-first minimum is degree three and prime seven. The seven displayed covers have exact class-number unit tests through every constant extension. This does not determine least primes over arbitrary fields, all-cover minima at each extension, or the full quartic census.",
 'B.52': r"B.136--B.147 remove the stated finite-derived and lower-central families in every finite transcendence degree, all proper Galois algebraic extensions of the specified relative local bases, and all fields with a nontrivial core in some open local group. Explicit wild procyclic fixed fields and every finite extension are negative; slimness is necessary. B.146--B.147 add derived and nilpotent inertia fields over complete mixed-characteristic discrete valuation bases with finitely generated residue fields of arbitrary transcendence degree. The remaining gate is the general mixed-characteristic field classification outside the stated positive and negative classes. B.134 remains a counterexample to general point-evaluation detection of Kummer classes, and is not a reconstruction counterexample.",
 'B.67': r"B.85--B.86 give actual supersingular correspondences on the ordinary cubic and two-rank-one quintic loci, with the entire cover and map written explicitly. The other parameters and higher-genus cases remain open; the bounded exclusions B.83--B.84 are not universal nonexistence results."
}
allranges = ranges(body)
for ident, status, begin, end in reversed(allranges):
    text = body[begin:end]
    old = REG.get(ident)
    is_pending = old is not None and old["review_state"] == "pending"
    is_open = status == "Open"
    if is_pending or is_open:
        if ident in gate_updates:
            text += "\n\\paragraph{Current proved reductions and remaining scope.} " + gate_updates[ident] + "\n"
        reason = "The supplied proof has not yet completed a targeted check in this writing." if is_pending else "The stated universal assertion remains unproved; the accompanying text records its exact current gate."
        unchecked.append((ident, text + "\n\\paragraph{Reason for placement in Part II.} " + reason + "\n"))
        marker = "\n\\noindent\\emph{Statement " + ident + " and its produced argument are retained in Part II.}\n"
        body = body[:begin] + marker + body[end:]
    elif old is not None:
        rec = "\n\\paragraph{Check record.} " + latex_escape(old["check_record"]) + "\n"
        body = body[:end] + rec + body[end:]
    else:
        md=META.get(ident,{})
        record=md.get('check_record','Checked only in this writing, 18 November 2026, GPT-6 Astra (OpenAI), ChatGPT Pro mode; separate effort setting not exposed. Complete proof written and read by its named authoring reader; see CHECK_EVENTS.tsv for additional second readings and computation scope.')
        body=body[:end]+"\n\\paragraph{Check record.} "+latex_escape(record)+"\n"+body[end:]
unchecked.sort(key=lambda x: (x[0][0], int(x[0].split('.')[1])))

introdoc = r"""
\begin{document}
\maketitle
\begin{abstract}
We continue the prime-to-characteristic point-separation argument with
explicit dependency separation, direct algebraic configuration exactness,
and independently implemented finite certificates. We retain every earlier
numbered assertion and distinguish checked proofs from work still awaiting
completion. The further arithmetic questions are treated with the same
distinction. No priority claim or different-model-family verification is made.
\end{abstract}
\noindent\textbf{Overall task status: INCOMPLETE.}
Every open item remains an open item. Individual proved results are stated
with their hypotheses and their check records. The exact available model
identification is GPT-6 Astra (OpenAI), ChatGPT Pro mode; a separate internal
reasoning-effort setting is not exposed. Prior external readings are recorded
as prior events, not as source openings or computations in this writing.
\tableofcontents
\part{Checked results}
"""
second = "\n\\part{Arguments whose verification or completion remains open}\n"
for letter in "ABC":
    entries = [t for i, t in unchecked if i.startswith(letter + ".")]
    if entries:
        second += "\\section*{Part " + letter + ": retained statements and produced arguments}\n" + "\n".join(entries)

tail = r"""
\bibliographystyle{plainnat}
\bibliography{ANABELIAN_A1_SUCCESSOR_references}
\end{document}
"""
paper = preamble + introdoc + body + second + tail
# Normalize keys inside multi-source as well as single-source citations.
# These are verified duplicate works, not different versions with different
# theorem numbering (the Stix2008/2012 entries remain separate).
def canonical_citation(m):
    return m.group(1)+'{'+','.join(ALIASES.get(k.strip(),k.strip())
                                  for k in m.group(2).split(','))+'}'
paper=re.sub(r'(\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*)\{([^}]+)\}',
             canonical_citation,paper)
# Explicit break opportunities in inherited long textual identifiers.
paper = paper.replace("Definition~1.18/Definition~1.5", "Definition~1.18/\\allowbreak Definition~1.5")
paper = paper.replace("/Theorem~", "/\\allowbreak Theorem~").replace("/Proposition~", "/\\allowbreak Proposition~").replace("/Corollary~", "/\\allowbreak Corollary~")
paper = paper.replace("Propositions~1.12,1.14--1.16,", "Propositions~1.12, 1.14--1.16, ")
paper = paper.replace(r"\citep[Corollary~4.5(1)]{HoshiTsujimura2023}", r"\citep[Corollary~4.5(1),(3)]{HoshiTsujimura2023}")
(WORK / "ANABELIAN_A1_SUCCESSOR_paper.tex").write_text(paper)

# Source verification is refreshed independently; inherited 'verified' flags
# are not evidence of an opening in this run.
bib = (BASE / "ANABELIAN_A1_references.bib").read_text()
bib = re.sub(r"verification\s*=\s*\{verified\}", "verification={unverified}", bib)
bib = re.sub(r"keywords\s*=\s*\{verified\}", "keywords={unverified}", bib)
bib = re.sub(r"note\s*=\s*\{", "note={Prior supplied annotation, not a current verification event: ", bib)
for f in ["configuration/references_configuration.bib", "configuration/references_literature_additions.bib", "configuration/references_A12_additions.bib", "arithmetic_notes/arithmetic_references.bib", "finite_checks/finite_references.bib", "notes/references_new.bib"]:
    p = WORK / f
    if p.exists(): bib += "\n" + p.read_text()
entries={}
for match in re.finditer(r'@[a-zA-Z]+\{([^,]+),.*?(?=\n@|\Z)',bib,flags=re.S):
    entries[match.group(1)]=match.group().strip()
preferred = {
    'MilneEtale':'CF_Milne2013', 'Bellingeri2004':'CF_Bellingeri2004',
    'LA_MT2008':'CF_MT2008', 'LA_Stix2005':'CF_Stix2005',
    'LA_SGA1':'CF_SGA1', 'CarlsonHaineWolf2024':'AN_CHW2024',
    'Rousseau1969':'AN_Rousseau1969'
}
for canonical,source in preferred.items():
    if source in entries:
        entries[canonical]=re.sub(r'(@[a-zA-Z]+\{)'+re.escape(source)+',',
                                 lambda m:m.group(1)+canonical+',',
                                 entries[source],count=1)
for alias,canonical in ALIASES.items():
    if alias in entries and canonical in entries:
        del entries[alias]
(WORK/'notes/BIBLIOGRAPHY_ALIASES.json').write_text(json.dumps({
    'aliases':ALIASES,'preferred_entries':preferred,
    'scope':'Duplicate works consolidated after exact source comparison. SGA1 citations use the actually read SMF2003 edition; its1971 original publication remains source metadata. Stix2008 and2012 remain distinct consulted versions. Full per-reader source records and input bibliographies are retained.'
},indent=2)+'\n')
bib='\n\n'.join(entries.values())+'\n'
verified_keys = {'MilneEtale','MilneJac','Conrad2006','LA_ST2009','LA_ST2017','LA_Mochizuki2014','LA_SGA1','Bellingeri2004','LA_MT2008','LA_Poonen2005','CarlsonHaineWolf2024','StacksProject','LMPT2019','Rousseau1969','FeitThompson1963','WeilCurves','MilneAV2008','LA_Stix2005','LA_Raynaud2000'}
configuration_metadata = WORK / 'configuration/configuration_metadata.json'
if configuration_metadata.exists():
    verified_keys.update(json.loads(configuration_metadata.read_text()).get('verified_reference_keys', []))
for key in sorted(verified_keys):
    pat=r'(@[a-zA-Z]+\{'+re.escape(key)+r',.*?)(?=\n@|\Z)'
    def promote(m):
        t=re.sub(r'verification\s*=\s*\{unverified\}', 'verification={verified}', m.group())
        t=re.sub(r'keywords\s*=\s*\{unverified\}', 'keywords={verified}', t)
        if not re.search(r'\bverification\s*=', t):
            pos=t.rfind('}')
            prefix=t[:pos].rstrip()
            if not prefix.endswith(','): prefix+=','
            t=prefix+'\n  verification={verified},\n'+t[pos:]
        t=t.replace('note={Prior supplied annotation, not a current verification event: ', 'note={Current verification: relevant numbered passages opened on 18 November 2026; exact scope in source records. Prior supplied annotation: ')
        return t
    bib=re.sub(pat,promote,bib,flags=re.S)
# Every entry carries an explicit machine-readable verification field.
def ensure_verification(m):
    t=m.group()
    if re.search(r'\bverification\s*=',t): return t
    verified=bool(re.search(r'keywords\s*=\s*\{verified\}',t))
    pos=t.rfind('}')
    prefix=t[:pos].rstrip()
    if not prefix.endswith(','): prefix+=','
    return prefix+'\n'+('  verification={verified},\n' if verified else '  verification={unverified},\n')+t[pos:]
bib=re.sub(r'@[a-zA-Z]+\{.*?(?=\n@|\Z)',ensure_verification,bib,flags=re.S)
# Verification prose belongs in the machine-readable bibliography/source table.
bib=re.sub(r'\bnote\s*=\s*\{', 'verification_note={', bib)
(WORK / "ANABELIAN_A1_SUCCESSOR_references.bib").write_text(bib)

cols = ["id", "statement", "status", "hypotheses_and_where_they_hold", "check_record", "where_proved", "depends_on", "A1_id (the checkpoint-03 number it continues, or empty)", "answers (item)", "manuscript_passages (cote; scan)", "depends_on_doubtful_reading (scan, alternatives)", "notes"]
rows = []
for ident, status, start, end in ranges(paper):
    chunk = paper[start:end]
    old = REG.get(ident)
    title_end = chunk.find("\n")
    statement = chunk[title_end:chunk.index(r"\end{claim}")].strip()
    source = old["source"] if old else {}
    rows.append({
        "id": ident, "statement": statement, "status": status,
        "hypotheses_and_where_they_hold": "Exact assertion and hypotheses: " + statement + " Application checks are in this statement's proof; external source hypotheses are transcribed in the source tables.",
        "check_record": old["check_record"] if old else "Checked only in this writing: full proof written and checked by the named authoring reader, 18 November 2026; see CHECK_EVENTS.tsv for exact event scope.",
        "where_proved": "ANABELIAN_A1_SUCCESSOR_paper.tex, Statement " + ident,
        "depends_on": old["depends_on"] if old else "PENDING exact dependency transcription",
        "A1_id (the checkpoint-03 number it continues, or empty)": ident if old else "",
        "answers (item)": source.get("answers (item or check item)", "PENDING item map"),
        "manuscript_passages (cote; scan)": source.get("manuscript_passages (cote; scan)", "See numbered assertion"),
        "depends_on_doubtful_reading (scan, alternatives)": source.get("depends_on_doubtful_reading (scan, alternatives)", "No doubtful reading used as a mathematical premise"),
        "notes": source.get("notes", "New continuing statement; per-statement metadata is being consolidated."),
    })
    md=META.get(ident,{})
    for col,aliases in {
        'hypotheses_and_where_they_hold':['hypotheses_and_where_they_hold'],
        'check_record':['check_record'],
        'answers (item)':['answers','answers_item'],
        'manuscript_passages (cote; scan)':['manuscript_passages','source_cotes'],
        'depends_on_doubtful_reading (scan, alternatives)':['depends_on_doubtful_reading'],
        'notes':['notes'],
        'depends_on':['direct_internal_dependencies','depends_on']}.items():
        for alias in aliases:
            if alias in md:
                val=md[alias]
                rows[-1][col]=';'.join(val) if isinstance(val,list) and all(isinstance(x,str) for x in val) else json.dumps(val,ensure_ascii=False) if isinstance(val,(dict,list)) else str(val)
                rows[-1][col]=transform(rows[-1][col])
                break
    # External theorem invocations are direct dependencies too. Preserve the
    # actual displayed locator; an absent locator is explicitly marked rather
    # than invented. Contextual literature comparisons are not theorem edges.
    proof = chunk.split(r"\begin{proof}",1)[1] if r"\begin{proof}" in chunk else ""
    ext=[]
    for cm in re.finditer(r'\\cite(?:p|t)?(?:\[([^\]]*)\])?(?:\[([^\]]*)\])?\{([^}]+)\}',proof):
        loc='; '.join(x for x in cm.group(1,2) if x)
        for key in cm.group(3).split(','):
            item='external '+key.strip()+' ['+(loc or 'source as cited; exact passage in source audit')+']'
            if item not in ext: ext.append(item)
    manual_external={
        'A.3':['Bellingeri2004, Section 2.1 (discrete configuration fibre sequence)'],
        'A.4':['LA_SGA1, III 7.3–7.4 and XIII 2.9–2.11 (lifted pair and prime-to-characteristic specialization)'],
        'A.5':['LA_SGA1, XIII 5.2 (tame boundary charts); finite étale descent'],
        'A.7':['Bellingeri2004, Theorem 1.2 (presentation used by the retained finite certificate)'],
        'A.12':['Bellingeri2004, Theorem 1.2 (genus-three presentation words)'],
        'A.16':['LA_ST2009, Definitions 1.3(iii), 1.5, 1.10; Remark 1.2; Proposition 1.8(iii)–(vi), with cofinite Σ for (vi)'],
        'A.22':['LA_ST2009, Lemma 1.7 and Proposition 1.8(iii) (same-geometric-point injectivity)'],
        'A.24':['MilneJac, Proposition 9.1 (elliptic geometric fundamental group and Tate module)'],
        'B.22':['MilneJac, Proposition 9.1 (Abel map on geometric abelian fundamental groups)'],
        'B.48':['LA_SGA1, XIII 5.2 (local tame Kummer charts); stable marked genus-zero models constructed in the proof'],
        'B.49':['Lepage2013, Theorem 1.8 (proper comparison over a noetherian henselian base)'],
        'B.51':['ADH2017, Proposition 3.3.25 and Corollary 3.3.26 (henselization and immediacy)'],
        'B.53':['StacksProject, Lemma 58.13.5, Tag 0BUA (profinite tame/wild inertia sequence)'],
        'B.62':['HoshiTsujimura2023, Corollary 4.5(1),(3) (slimness: (1) for positive transcendence degree, (3) for number fields); StacksProject, Lemma 32.4.2, Tag 0CUF (underlying limit)'],
        'B.65':['CarlsonHaineWolf2024, Proposition 6.22 and Claim 6.23, Remark 4.20, Theorem A.8, Corollary A.9 and Proposition 4.8; HoshiTsujimura2023, Corollary 4.5(1),(3)'],
        'B.66':['CarlsonHaineWolf2024, Theorem 1.13 and Proposition 2.28 (geometric-point function and base change)'],
        'C.10':['LA_Sun2025, Definition 3.1 and Corollary 3.2 (predecessor; pullback exactness is proved here)'],
        'C.11':['LA_Mochizuki2007, original Remark 1.7.1; LA_Sun2025, Corollary 3.8 (local boundary comparison under the stated hypotheses)'],
        'C.13':['LA_CiperianiStix2015, Lemma 3 and Remark 4 (all-prime Jacobian Kummer injectivity)'],
    }
    for item in manual_external.get(ident,[]):
        ext.append('external '+item)
    if ident=='A.40':
        ext.append('literature comparison sources: see the exact per-paper locators in configuration/dependency_table.tsv and configuration/literature_audit_successor.tex; no mathematical predecessor conclusion is silently imported')
    if ext:
        rows[-1]['depends_on']+='; ' if rows[-1]['depends_on'] else ''
        rows[-1]['depends_on']+='; '.join(ext)
    if ident=='A.1':
        rows[-1]['notes']+=' Dependency column records the complete direct characteristic-p, proper-support-field route. The separately retained alternative uses A.16, A.19 and A.44; these are not premises of the recorded route.'
    if status=='Open':
        rows[-1]['notes']+=' For this Open row the dependency column records proved reductions and attempted approaches, not a proof of the universal assertion.'
rows.sort(key=lambda x: (x["id"][0], int(x["id"].split(".")[1])))
with (WORK / "ANABELIAN_A1_SUCCESSOR_results.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=cols)
    writer.writeheader(); writer.writerows(rows)
(WORK / "notes/assembly_status.json").write_text(json.dumps({"statements": len(rows), "part_ii": [i for i, _ in unchecked], "new_number_map": NUMBERS}, indent=2) + "\n")
print(json.dumps({"statements": len(rows), "part_ii": len(unchecked), "tex_bytes": len(paper.encode())}))
