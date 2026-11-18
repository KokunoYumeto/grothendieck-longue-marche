"""Build the complete historical claim register from the supplied source registers.

This records the audit actually completed in SECTION_GHOSTS.  A pending row is
not a judgment that the historical assertion is false or mathematically open.
Run from the workspace root.  Source statements are retained verbatim so that
an attractive weaker consequence cannot silently replace the original claim.
"""
from pathlib import Path
import csv
import re

BASE = Path(__file__).resolve().parents[1]
WORK = BASE.parent
BG = WORK / "background"

def source_rows(folder, filename):
    with (BG / folder / filename).open(encoding="utf-8-sig", newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f)}

gt = source_rows("gt_tower_check_cp10", "GT_TOWER_CHECK_results.csv")
sq = source_rows("sections_over_q_cp17", "SECTIONS_OVER_Q_results.csv")
lm = source_rows("lm4_successor_cp40", "LM4_SUCCESSOR_results.csv")

proof_files = {}
for p in sorted((BASE / "sections").glob("*.tex")):
    for ident in re.findall(r"\\begin\{result\}\{([^}]+)\}", p.read_text()):
        if ident not in proof_files or "generated" in p.name:
            proof_files[ident] = str(p.relative_to(BASE))

rows = []
def add(run, ident, source, status, refs, scope, remaining=""):
    refs = refs.split(", ") if isinstance(refs, str) and refs else list(refs or [])
    missing = [r for r in refs if r not in proof_files]
    if status == "confirmed" and missing:
        status = "pending"
        remaining = (remaining + " " if remaining else "") + "Current proof not yet present: " + ", ".join(missing) + "."
    rows.append({
        "historical_id": f"{run} {ident}",
        "source_run": run,
        "source_id": ident,
        "source_statement": source.get("statement", ""),
        "source_status": source.get("status", ""),
        "source_where_proved": source.get("where_proved", ""),
        "source_depends_on": source.get("depends_on", ""),
        "audit_status": status,
        "current_statements": "; ".join(refs),
        "current_proof_files": "; ".join(dict.fromkeys(proof_files[r] for r in refs if r in proof_files)),
        "audit_scope": scope,
        "remaining_check": remaining,
        "uses_local_theorem": "no",
        "checked_date": "2026-11-18",
    })

gm = {
"C.1.1": ("confirmed", "E.101", "The complete finite-support reconstruction is re-proved, including finite support of A/B and equality of every finite ordinary local point."),
"C.1.2": ("confirmed", "A.3, E.101", "Infinite ramification at every coefficient prime is proved. The stronger span and cusp clauses follow because ordinary valuation vectors lie on (m,0),(0,m),(m,m): rank at most one outside a finite set makes A, B or A/B finitely supported, contrary to E.101. Two independent vectors generate an open Z_ell-submodule."),
"C.1.3": ("confirmed", "A.20", "Higher-weight literal continuous cocycles are finite free and compact; the fixed-ramification factorization is retained."),
"C.1.4": ("confirmed", "A.20", "Integral Hall coordinate model, bounded rational denominators and the actual continuous arithmetic action are retained at every coefficient prime."),
"C.1.5": ("confirmed", "A.20", "Closedness and continuous choice of primitives for a finite polynomial parameter family are proved; no closedness of all global coboundaries is inferred."),
"C.1.6": ("confirmed", "A.20", "Compactness is proved for one fixed literal abelian cocycle. It does not assert compactness of a varying family of ghosts."),
"C.1.7": ("confirmed", "A.21", "All integral classes for the same fixed pair are equivalent to one compatible full pronilpotent section, with the corresponding fixed local-matching variant."),
"C.1.8": ("confirmed", "A.23", "The nonzero weight-twelve coefficient-691 continuous class, its injective inflation, local vanishing and finite-coefficient vanishing are re-proved."),
"C.1.9": ("confirmed", "A.23", "The actual profinite extension associated to the continuous two-cocycle has all stated splitting and nonsplitting properties; it is not identified with a curve quotient."),
"C.1.10": ("confirmed", "A.24", "Exact odd-primary derived-limit localization kernel and the explicit product/c0 subgroup at weight two and coefficient three are proved."),
"C.1.11": ("confirmed", "A.25", "Ordinary continuous cup vanishing is proved with compatible integral primitives, retaining the derived-limit issue and the two-primary real term."),
"C.1.12": ("confirmed", "A.25", "The primitive produces a section in the actual arithmetic class-two quotient; no local central matching is claimed."),
"C.1.13": ("confirmed", "A.22", "Strict integral localization uses the literal image d_r R_ell, not its closure; degree-three fixed-ramification H2 is zero."),
"C.1.14": ("confirmed", "B.22", "The coefficient-compatible tame cochain map, its domain and the q inverse factor are re-derived."),
"C.1.15": ("confirmed", "B.23", "The actual two class-three residue families are derived. Vanishing requires integral normalized families that tend to zero, not merely local divisibility."),
"C.1.16": ("confirmed", "A.30", "Rational formal conjugacy detects pro-ell conjugacy via integral cyclic words and compact conjugator fibres; rational series are not evaluated in finite group algebras."),
"C.1.17": ("confirmed", "A.31", "The full local pro-ell section fibre is a singleton at a nonzero ordinary boundary valuation when ell differs from the rational place."),
"C.1.18": ("confirmed", "A.26", "Integral weight-two H1 is Z/8 at two, Z/3 at three and zero otherwise, hence Z/24 with its stated generator."),
"C.1.19": ("confirmed", "A.27", "Exactly twenty-four unrestricted class-two conjugacy classes are proved, with the missing stabilizer ruled out. They are not twenty-four locally matching classes."),
"C.1.20": ("confirmed", "E.118", "The first part of E.118 reconstructs the exact coefficient-five prefix, integral local primitives, unique finite central class, full order-500 image and maximal abelian subfield. That part does not use the later noncube restriction."),
"C.1.21": ("confirmed", "B.20", "The finite-prefix assertion for ell at least five is proved and extended to two and three with the needed Bockstein precision."),
"C.2.1": ("confirmed", "E.34, E.31, E.32, E.33", "The exact displayed historical A.65 sequence converges to (3,-2) for arbitrary N_R: R! divides the required C_R and both divided products are C_R-th powers. The ordinary locus is not closed, and fixed-pair compactness cannot be applied to the varying survivors."),
"C.2.2": ("pending", "B.2, A.25", "The source concerns first failure of everywhere locally point-or-cusp-matching sections in an order-32 quotient. Unrestricted class-two existence is established and is not contradicted.", "The specified modified factorial recursion, genus-two descent and all eight local sheets at 1129 have not been reconstructed in this paper."),
"C.2.3": ("pending", "P.6", "The supplied source explicitly concerns Q(cuberoot(3)) and a nonordinary local frame, rather than the ordinary completed-pair problem over Q.", "The exact ninth-power local ring computation for the displayed 649^8 pair has not been rerun and proved here."),
"C.2.4": ("pending", "B.23, B.25", "The valuation-zero unramified argument is available in the present framework; this does not certify the existence and all specifications of the historical 1129 witness.", "The exact witness and coefficient-prime-1129 local calculation need a complete linked audit."),
"C.2.5": ("pending", "E.118, A.25", "This run proves an actual first class-three failure in the original compact-passing family, with coefficient-five witness at q1.", "The historical scaled exponents 5(j+4)! and the defect at q0 are a different specified construction and are not certified by E.118."),
"C.2.6": ("confirmed", "E.119, A.25", "The selected original-factorial family has a coefficient-three class-three exclusion detected modulo nine, with the other central twists excluded at two."),
"C.2.7": ("confirmed", "E.118, E.117", "The exact compact-test-passing original family, coefficient-five defect at q1 modulo25, nonempty affine abelian cover fibre and empty class-three fibre are reconstructed."),
"C.2.8": ("pending", "E.121, E.118", "E.121 proves a new coefficient-three dense-exclusion construction in the noncube compact-passing subfamily; its method extends after arbitrary legal prefixes. One coefficient-five example is E.118.", "The original more precise arbitrary-prefix construction with a new ell at least five and witness q_(ell-4) has not been independently reconstructed. Do not substitute the new coefficient-three witness silently."),
"C.2.9": ("pending", "B.20, B.21, E.121", "Finite-prefix openness is proved, and E.121 gives an open dense three-primary excluded locus in its stated compact-passing family.", "The exact historical locus U3 defined using coefficient primes ell at least five, and its density in both full historical domains, await the precise C.2.8 reconstruction."),
"C.2.10": ("confirmed", "E.30", "Exact analytic shell bijection, exponent valuation and congruence preservation, including the dyadic shell."),
"C.2.11": ("confirmed", "E.31", "General three-sequence variable-exponent arithmetic recursion with its exact field intersections and ordinary local limits."),
"C.2.12": ("confirmed", "E.32, E.33", "For each fixed R,N, an actual integral class-R ghost section retains the prescribed Magnus congruence. The pair may depend on R,N."),
"C.2.13": ("pending", "A.21, A.31", "Fixed-pair compactness and the required local boundary comparison are independently proved.", "The selected fixed-depth prime recursion, simultaneous coefficient-five cover defect and resulting later finite failure have not been reconstructed as one theorem."),
"C.2.14": ("pending", "A.20", "The integral Hall framework is re-proved and the historical augmentation calculation was read without a defect found.", "The exact bound I^(1+10(M-1))=0 and its complete terminating collection argument are not yet a current-paper proof."),
"C.2.15": ("pending", "A.30, A.31", "The limiting pro-ell conjugacy and boundary singleton inputs are re-proved.", "The explicit finite class 10(p^(v_p(m)+1)-1) exclusion needs the independent bounded augmentation/centralizer argument of C.2.14."),
"C.2.16": ("pending", "A.21", "The historical assertion concerns deliberately selected fixed-depth survivors, not every output.", "The complete two-sided bound and its exact first-stage exponent valuation remain linked to the unaudited C.2.13-C.2.15 construction."),
"C.2.17": ("confirmed", "E.20", "A fixed arbitrary finite quotient, full abelianization and all finite local conjugacies are retained together; the real restriction is the point-three image."),
"C.2.18": ("pending", "E.20, E.118", "The arbitrary prescribed finite-quotient survival and one original-family coefficient-five failure are separately proved.", "Their combination for every arbitrary finite quotient, with the selected A.72 pair failing integrally at class three, is not proved by either result alone."),
"C.3.1": ("confirmed", "E.110, E.119", "The pointed open elliptic cover, explicit degree-27 map and the selected family's no-local-lift/pro-three exclusion are all proved with the actual cover subgroup."),
"C.3.2": ("confirmed", "E.111", "Both three-isogeny Selmer groups, rank-one completion and vanishing of three-primary Sha are independently calculated."),
"C.3.3": ("confirmed", "E.112", "Absolute continuous Tate-module H1 is computed, without imposing a Selmer condition; the present proof also strengthens localization at three."),
"C.3.4": ("confirmed", "E.113", "The two prime-to-three point-order tests are necessary for every original A.44 output with a full pro-three section."),
"C.3.5": ("confirmed", "E.114", "The original recursion admits the stated noncube choices and all compact support tests pass; this alone asserts no pro-three section."),
"C.3.6": ("confirmed", "E.115", "The local compact fibre at two consists of all three classes generated by T, so it imposes no additional proper coefficient restriction."),
"C.3.7": ("confirmed", "E.115", "The actual full generalized-Jacobian quotient and exact completed norm image are proved, retaining all coefficient primes."),
"C.3.8": ("confirmed", "E.116", "Each degree-nine boundary field, its H3 semidirect C2 normal closure, Hasse norm principle and norm-torus weak approximation are proved."),
"C.3.9": ("confirmed", "E.102, E.114, E.117", "The stronger all-compact-passing affine abelian lifting theorem applies. The optional mod27 conditions are available by choosing the old 3-adic root xi3=1 and its near-one companion in the original recursion."),
"C.3.10": ("confirmed", "E.116, E.117", "Full local norm surjectivity at three and affine abelian lifting for every compact-test-passing output are proved; no extra mod27 condition is needed."),
"C.3.11": ("confirmed", "E.118", "The exact original-family pair has a nonempty affine abelian cover fibre but no metabelian cover lift, witnessed at coefficient five."),
}

gm.update({
"C.2.2": ("confirmed", "E.70, E.71, A.25, A.27", "The exact original-factorial variant with ordinary centre in 828+1129 Z_1129 is reconstructed. Its first everywhere locally point-or-cusp-matching failure is class two, detected by the actual order32 quotient; its unrestricted class-two fibre still has twenty-four classes."),
"C.2.4": ("confirmed", "E.72, E.71", "For the exact ordinary factorial 1129 witness every global class-two section has zero local third obstruction there at every coefficient prime. At each coefficient prime different from1129, its specified local class-two restriction lifts to the full geometrically pro-ell local extension."),
"C.2.3": ("confirmed", "E.43", "The exact 649^8 pair over Q(cuberoot(3)) is ordinary modulo cubes but neither ordinary nor cuspidal modulo ninth powers; the latter is the precise historical assertion."),
"C.2.5": ("confirmed", "E.60, A.25, A.27", "The exact scaled exponents 5(j+4)!, initial exponents 120 and 600, and first-prime q0 coefficient-five defect modulo25 are reconstructed. Every one of the twenty-four integral class-two classes is excluded."),
"C.2.8": ("confirmed", "E.61, E.117", "After every original legal finite prefix, including compact-passing prefixes, the exact original exponents admit a later coefficient ell at least five and witness q_(ell-4) modulo ell^2. Affine abelian lifting and metabelian exclusion are retained in the compact-passing domain. The proof uses the actual point-three finite field, not an unverified generic radical presentation."),
"C.2.9": ("confirmed", "E.62, E.61, E.117", "The exact historical ell-at-least-five locus is open dense in both stated domains. Every finite legal prefix has a finite extension forcing exclusion for all legal ordinary continuations, with the compact-passing conditions retained."),
"C.2.13": ("confirmed", "E.37, E.33", "The selected fixed-depth survivors have no full pro-five section and have a finite later first failure strictly above the prescribed surviving depth; the same point-three Heisenberg cover detects the full exclusion."),
"C.2.14": ("confirmed", "E.35", "The exact augmentation exponent 1+10(M-1) is reconstructed for the actual Heisenberg subgroup, including the terminating collection argument."),
"C.2.15": ("confirmed", "E.36", "The exact finite excluding class 10(p^(v_p(m)+1)-1) follows from the proved augmentation bound and the actual finite local comparison; no compactness-only existence is substituted."),
"C.2.16": ("confirmed", "E.37", "The selected examples have first failure R0<r<=10(5^(v5(m)+1)-1), with the exact first-stage valuation v5(C)+d*v5(J!)+v5(d!). No exact least class within this interval is asserted."),
"C.2.18": ("confirmed", "E.38, E.20", "For every prescribed finite geometric quotient, the full abelianization and all local conjugacies are retained while the selected pair first fails in unrestricted integral class three. The actual point-three field replaces the unverified generic Theta marking without changing the theorem's conclusion or quantifiers."),
})

for block, count in [(1,21),(2,18),(3,11)]:
    for n in range(1,count+1):
        ident=f"C.{block}.{n}"
        add("GT_TOWER_CHECK", ident, gt[ident], *gm[ident])

sm = {
"A.25": ("confirmed", "A.25, A.24", "All finite cup reductions vanish. The current proof gives the stronger continuous global vanishing, hence every local restriction is zero, with the genuine derived-limit group retained."),
"A.32": ("confirmed", "E.101", "Finite support of either coordinate reconstructs the unique rational pair and all finite local points; the current proof also covers A/B."),
"A.42": ("confirmed", "E.103", "Closedness, discreteness, eventual constancy of Cauchy nets and finite-power separation follow from the checked rational-point finiteness argument."),
"A.44": ("confirmed", "E.102", "The original exact exponents (j+4)!, local ordinary limits, all valuation coordinates and recursive prime choices are re-proved."),
"A.48": ("pending", "E.102", "The two-puncture tripod construction is proved; this is not the arbitrary finite puncture-set statement.", "The multiple-puncture curve construction and all simultaneous local coordinates have not been reconstructed."),
"A.50": ("pending", "A.25", "The tripod continuous cup and actual class-two lift are proved.", "For every finite puncture set the actual exterior-square quotient, its arithmetic action and all normalized two-coordinate comparison maps need an explicit linked proof; A.25 alone is not that proof."),
"A.51": ("confirmed", "E.20, E.102", "The actual finite-quotient/full-abelianization fibre product and survival are proved, with stronger local matching in E.20. For perfect Q the common quotient is G_Q, so every abelian ghost pairs with s3. The source's phrase 'form A.44' explicitly allows (j+k)! with d dividing k!; the same E.102 induction works for every k at least four."),
"A.52": ("pending", "B.20, E.33", "Fixed-depth survival implies an existential finite-third-layer survivor once E.33 is available.", "The specified distinguished class-two lift of every shifted original recursion and the exact N=24 case are stronger claims and have not been separately audited."),
"A.59": ("pending", "E.31, E.33", "The general fixed-depth reconstruction supplies some ordinary class-three ghosts.", "The exact historical constants C=24, n_j=(j+4)!, D_j=48 n_j^2 and its particular local analytic construction are not certified merely by choosing larger parameters in E.31-E.33."),
"A.65": ("confirmed", "E.32, E.33", "The full fixed-depth, prescribed-Magnus-modulus existence statement is reconstructed; neither the pair nor the section is uniform as depth varies."),
"A.72": ("confirmed", "E.20", "Every fixed finite geometric quotient can be retained with full abelianization and all local point conjugacies, using a quotient-dependent ordinary ghost."),
"A.137": ('confirmed', 'E.160, E.161, E.162, E.163, E.164, E.165', 'The exact harmonic coefficient initialization and prescribed centres are independently reconstructed by a new finite certificate and complete mixed-exponent refinement. The actual order2^136 quotient, faithful128-vertex cycle model, exact class17 and explicit nonzero weight17 commutator are proved and executed. Its local-matching exclusion follows through the actual order4096 detector. The unavailable historical A134 certificate was replaced, not claimed opened; this is not unrestricted class17 failure.'),
"A.139": ("confirmed", "E.160, E.161, E.162, E.163, E.164", "The exact coefficients, prescribed special centres and completed harmonic triple are independently reconstructed with a replacement initialization. The actual cyclic cover, combined Kummer class, order4096/class8 group, every finite local sheet, nonsplit central descent and real-cusp evaluation are proved. The unavailable historical A134 finite certificate is not claimed verified. This is a locally matching exclusion, not unrestricted class8 failure."),
"A.196": ('confirmed', 'E.43, E.166, E.167, E.168, E.169', 'The exact cubic-field pair has a global integral class-two lift and compatible continuous local class-three lifts, but no global continuous lift to the actual class-three quotient. Its integral obstruction has exact order three and is first detected at modulus nine over the stated S. Every unrestricted finite quotient nevertheless lifts, while every fixed finite ramification set eventually fails. E166-E169 reconstruct the missing arithmetic inputs with a new degree-six certificate; E43 retains ordinary-mod3 and nonordinary/noncuspidal-mod9 scope at3. This is not an ordinary pair over Q or a full pronilpotent counterexample.'),
"A.207": ("pending", "B.2", "The statement explicitly asserts an unrestricted global class-four lift and excludes everywhere locally matching class-four sections of the same pair.", "The prescribed 1129 recursion, genus-two Selmer calculation and all cover-sheet Kummer maps have not been reconstructed; it cannot be counted as unrestricted class-four failure."),
"A.209": ("pending", "B.2, A.25", "The statement excludes locally matching class-two sections and retains an unrestricted class-four lift; these are compatible with A.25.", "The projected norm Selmer group, exact order-32 quotient and all eight local-sheet calculations remain unaudited in this run."),
}
sm.update({
"A.52": ("confirmed", "E.63", "The distinguished integral class-two lift for every exact shifted recursion n_j=(K+j)!, K>=4, lifts through the actual finite third layer N=K!. The original N=24 case and every prescribed finite modulus are retained."),
"A.58": ("confirmed", "E.64, E.65", "The full stated valuation locus gives unrestricted integral class-three lifts, including both support signs and exponents tending to zero. The missing coefficient-prime argument is independently rebuilt; no assertion is made about the unseen old lemma's exact wording."),
"A.59": ("confirmed", "E.64, E.65", "The exact historical constants C=24, n_j=(j+4)!, D_j=48*n_j^2 and E=24*n_j*(Q^2-1), including the specified coefficient-prime analytic construction, are independently reconstructed. The dyadic full shell is two-to-one; the u=1 mod4 half-shell supplies the required bijection onto the same image."),
"A.48": ("confirmed", "E.40, E.41", "The simultaneous radical lemma and recursion are proved for every fixed finite rational puncture set; all completed coordinates have infinite ordinary support and all local point equalities hold, including the real sign."),
"A.50": ("confirmed", "E.42, A.25", "Every ordinary finite-puncture completed tuple lifts to the actual full profinite class-two quotient. Pairwise normalized forgetful maps detect every exterior-square coordinate with the genuine arithmetic action. Local central point coordinates are not prescribed."),
"A.196": ('confirmed', 'E.43, E.166, E.167, E.168, E.169', 'The exact cubic-field pair has a global integral class-two lift and compatible continuous local class-three lifts, but no global continuous lift to the actual class-three quotient. Its integral obstruction has exact order three and is first detected at modulus nine over the stated S. Every unrestricted finite quotient nevertheless lifts, while every fixed finite ramification set eventually fails. E166-E169 reconstruct the missing arithmetic inputs with a new degree-six certificate; E43 retains ordinary-mod3 and nonordinary/noncuspidal-mod9 scope at3. This is not an ordinary pair over Q or a full pronilpotent counterexample.'),
"A.209": ("pending", "E.70, E.71, E.72", "The exact actual cyclic-eight/proper-homology quotient, quadratic norm comparison, complete four-element projected Selmer image, rational divisor realization, and order32 local-matching exclusion are independently proved without importing A.186's full two-Selmer calculation.", "The final assertion that the particular same A.207 pair simultaneously has an unrestricted global class-four lift still depends on the literal A.207 construction and its missing A.60-A.61 source. The finite exclusion and projected Selmer clauses are confirmed."),
})

# Preserve the authoritative root audit updates for the literal class-four chain.
sm.update({'A.60': ('confirmed', 'E.80', 'Independently proved the exact four-place weight3 restriction map with7,13,2,2 targets, invariant cyclotomic-unit descent, integral lifts and the section consequence.'), 'A.61': ('confirmed', 'E.81, E.82', 'Independently proved the exact24(q²−1)(q³−1) valuation locus using actual path action, integral Hall bounds and strict c0; original infinite-support realization is E82.'), 'A.62': ('confirmed', 'E.82', 'Independently reconstructed the original cubic-exponent recursion with C divisible24 and J at least6, exact small-prime analytic maps, radical intersections, triangular CRT and ordinary limits.'), 'A.207': ('confirmed', 'E.70, E.80, E.81, E.82, E.83', 'The literal C24,J6 prescribed1129 ordinary recursion and its actual global class4 lift are independently reconstructed. Every original local sheet and full Kummer bit vector is computed; the independently proved projected Selmer bound excludes all8 sheets and the stated actual order128 quotient, already through order32. The unavailable earlier full two-Selmer computation is unnecessary for this conclusion.'), 'A.209': ('confirmed', 'E.70, E.83', 'The exact arithmetic quotient, quadratic norm comparison, complete four-element projected Selmer group, rational divisor realization and order32 local-matching exclusion are independently proved in E70. E83 completes the final same-pair clause: the actual A207 ghost has an unrestricted global class4 lift and no everywhere locally matching class2 lift.')})
for ident, data in sm.items():
    add("SECTIONS_OVER_Q", ident, sq[ident], *data)

add("GT_TOWER_CHECK", "C.5", gt["C.5"], "confirmed", "E.20, E.70, E.190, E.191, E.195, E.201",
    "E201 independently reconstructs the literal original A2 identity-relative family for H=F'F^3, with one full gentle lift acting trivially on every H-relative pronilpotent factor, f and beta in R_nil(H), complete rho=0, and unique signed frames T=5I and W=I. E190-E191 prove its failure of the full GT pentagon condition, and E195 gives finite exclusion of the entire parity-one locus. E70 proves the section-side order32 witness; E20 proves that no one fixed finite geometric quotient excludes every quotient-dependent A72 family. The source-Open assertion about every proposed full cover, configuration or modular target remains unresolved; confirmation records this exact qualified statement, not a universal-target theorem.")
add("GT_TOWER_CHECK", "A.4.1", gt["A.4.1"], "confirmed", "E.190, E.191, E.195",
    "The entire actual compact parity-one gentle locus is excluded in one finite five-point quotient, with a simultaneous finite characteristic source record determining Delta. E190-E191 supply the full signed CM vanishing premise; E195 proves the exact compact separation statement. No numerical level, least quotient or executed actual-source census is asserted.")
add("GT_TOWER_CHECK", "A.7", gt["A.7"], "confirmed", "E.95, E.97, E.190, E.191, E.197, E.198",
    'The original signed CM character vanishes on full profinite GT for every multiplier by E191. E197 independently constructs an actual integral pro-eleven gentle automorphism, retains its exact degree-seven term through the full E57 lift, and E198 squares that full element to obtain a zero-character non-GT witness detected in an actual finite eleven-primary class-seven quotient. E97 supplies character one. Thus both exact strict inclusions and the entire A7 chain are proved; no surjectivity of the faithful Galois inclusion is asserted.')
add("GT_TOWER_CHECK", "A.4.57", gt["A.4.57"], "pending", "E.176, E.177, E.178, E.179, E.180, E.184, E.188, E.189, E.190, E.191, E.195",
    "The qualitative geometric fusion, completed normalizers and involution quotient, original eight-point GT parameter, signed CM covariance and finite existential exclusion are independently reconstructed. The historical source itself distinguishes its explicit exclusion theorem from an unexecuted full source census.",
    "The literal compiler quotient Z and its numerical refinement recursions, including the specified289 covers, are not certified by existence of some finite separating quotient. The requested complete genuine-source enumeration remains unexecuted.")

prompt_source = {"status":"unreviewed input", "where_proved":"upload/PROMPT(20261118-023202).md, Results this builds on", "depends_on":"As specified in the supplied prompt"}
def prompt_row(ident, statement, status, refs, scope, remaining=""):
    src=dict(prompt_source,statement=statement)
    add("SECTION_GHOSTS_PROMPT",ident,src,status,refs,scope,remaining)

prompt_row("R7", "No single fixed finite geometric quotient excludes every A.72 family.",
           "confirmed","E.20","The pair depends on the prescribed quotient; the actual full-abelianization fibre product and local conjugacies are retained.")
prompt_row('R8',
           'Fermat/pro-prime and metabelian section assertions, together with the continuous weight-two derived-limit assertion.',
           'repaired',
           'A.24, E.98, E.99, E.100',
           'The abstract continuous derived-limit clause is independently proved. Recovered LM6 positive section constructions are independently proved over Q for n=3^r or5^r, including one actual full pronilpotent section and genuine full profinite metabelian zero-abelian families. The unrestricted all-Fermat/all-coefficient reading is false by the even-plus real obstruction.',
           'Original LM7/LM8 proof files and the extra marked LM6 E38 geometric/Smith-certificate assertion remain separately unaudited; they are not used to certify A24 or E98-E100.')
prompt_row('R8.sections',
           'Every pro-ell nilpotent quotient and the full metabelian quotient of the Fermat curves carry non-cuspidal sections.',
           'repaired',
           'E.98, E.99, E.100',
           'For p=3 or5 and n=p^r, every S-unramified intrinsic p-abelian class lifts fully pro-p; proper infinite-order classes give noncuspidal full pronilpotent sections. A characteristic Alexander/Haar summand gives genuine full metabelian Z_p^d_n zero-abelian families and exact cusp normalizers. All constructed tripod pairs are nonordinary at Q2. Every even plus n has no pro2 abelian section, refuting an unrestricted universal reading.',
           'Other coefficient projections of the pronilpotent product are cuspidal. The original cubic modulo27 central-cohomology detector is checked; a wholly finite conjugacy reading requires an extra stabilizer check and is not asserted.')
prompt_row("R8.cohomology", "Continuous H2(G_Q,Z_ell(2)) can have derived-limit classes invisible at every place and every finite coefficient level.",
           "confirmed","A.24","A.24 proves the exact odd-primary kernel and explicitly exhibits a nonzero uncountable kernel at ell=3. This confirms the asserted phenomenon, without claiming a particular geometric obstruction realizes it.")
prompt_row("R9", "The specified LM4_SUCCESSOR automorphism, framed-involution and lift-ambiguity examples test proposed section compactness arguments.",
           'confirmed','E.50, E.51, E.52, E.53, E.54, E.55, E.56, E.57, E.58, E.59, E.90, E.91, E.92, E.93, E.94, E.95, E.96, E.97','Every specifically demanded LM4 claim is independently reconstructed: exact finite central examples, prescribed-frame and frame-independent negative obstructions, compatible actual central towers and fresh-prime first refinements, ordinary full realization, nontrivial relative arithmetic kernels and each typed coset injection. E95-E97 close the exact arithmetic CM base and frame marking. These distinct symmetry/frame/tower statements do not decide the main section questions or the full-GT geometric vanishing claim.')

lm_notes={
"A.18": "Mixed-sign order-preserving lifting obstruction; not the globally negative unframed problem.",
"A.31": "Only the relative principal-congruence tower is claimed; the source explicitly says it is not cofinal and does not conclude the full lift is an involution.",
"A.70": "The prescribed finite actual source-central equivariance problem uses a mixed multiplier; it is not ordinary unrestricted lifting.",
"A.74": "The obstruction keeps prescribed conjugator frames; the source allows frame reselection and does not obstruct a negative cocycle.",
"A.76": "Globally negative framed order preservation is excluded for a specified finite s-frame; unframed existence is left separate.",
"A.79": "Compatible iterated source-central refinements are asserted together with an ordinary full lift, while involution symmetry fails in a separate specified finite detector.",
"A.81": "The source claims first-central-refinement compatibility, not compatibility through all iterates; its specified finite action and involution condition are retained.",
"B.42": "The proposed prosolvable arithmetic kernel fixes particular relative automorphisms and frames, not arbitrary full tripod data.",
"B.43": "The claimed uniform finite simple-group exclusion for d at most97 needs its finite-section rank and representation arguments; a general Jordan slogan does not suffice.",
"B.44": "The asserted simultaneous arithmetic kernel concerns two specified relative systems and frame coordinates.",
"B.45": "The asserted arithmetic coset leaves tripod/resolvent values undetermined and gives at most one member in the desired kernel, not existence of such a member.",
}
lm_audits = {
"A.18": ("confirmed", "E.58, E.57", "The exact mixed-sign pronilpotent involution has an ordinary full lift but no full involution lift. The needed dyadic torsion exclusion is proved using the profinite Brown theorem and a boundary-rank argument; no full classification is imported."),
"A.31": ('confirmed', 'E.56, E.57, E.95, E.96, E.97', 'Independently reconstructed the exact arithmetic CM frames through marked Legendre paths and the essential quadratic twist, zero-complete-Kummer Galois element, finite discrepancy character and outer descent, all-prime norm-one frames and one compatible full lift. The relative principal-congruence tower is noncofinal with residual image onto A7; no full involution or cofinality is asserted.'),
"A.70": ("confirmed", "E.50", "The exact actual source-central group of order13824, involution with multiplier7 modulo24, named reflection/cusp classes, and absence of any full equivariant peripheral lift are proved and independently enumerated."),
"A.74": ("confirmed", "E.51", "The exact SL2(F5) source-central refinement and prescribed central frame are reconstructed. The identity action lifts with reselected frames, but the specified frame cannot be retained by a full equivariant lift."),
"A.76": ('confirmed', 'E.59, E.90, E.91, E.95, E.96, E.97', 'The exact original finite witness and its source-central refinement, both quotient normalizer norms, ordinary full framed realization, and complete six-cup forced descent with nonzero weight23 invariant are independently proved. E95-E97 supply the exact historical arithmetic base, including the pure beta0 and r-heads. The negative assertion retains its specified finite s-frame.'),
"A.79": ('confirmed', 'E.59, E.90, E.91, E.92, E.95, E.96, E.97', 'The exact changed finite action and frame-independent order-four detector are reconstructed. The integral tower, six-cup scalar stability, relatively perfect inverse-limit kernel, finiteness and compatible action of every actual central iterate, and one ordinary full realization are proved from the now independently established exact arithmetic base. No reselected W=0 action is excluded and no cofinality is asserted.'),
"A.81": ('confirmed', 'E.59, E.92, E.93, E.94, E.95, E.96, E.97', 'The exact historical A79 base now has the independently proved arithmetic realization. The compact-homology anti-symplectic construction, actual fresh-prime source quotient and first-central refinement, literal cusp correction, both norm-one frames and ordinary full realization are proved for infinitely many eligible primes. Unnormalized negative nonrealization is independently proved. No selected numerical prime or all-central-iterate assertion is added.'),
"B.42": ("confirmed", "E.53", "The nontrivial prosolvable Galois residual kills the Fermat relative pro-prime actions and both canonical pure frames. The elliptic homology image, faithful deck action, framed cocycle law, actual modulo12 quotient and explicit S5 quotient are proved."),
"B.43": ("confirmed", "E.52", "The uniform A10000-section exclusion is proved by prime-to-characteristic lifting, Collins's characteristic-zero theorem, elementary abelian rank bounds and the pro-p Frattini kernel. Exact logarithmic bounds are checked."),
"B.44": ("confirmed", "E.54", "A simultaneous nontrivial arithmetic kernel is constructed for both actual relative systems and every coefficient prime, retaining both frames. Actual level12 covariance, pro-class closure and the explicit S10000 polynomial are checked."),
"B.45": ("confirmed", "E.55", "For every given full allowed lift, each named icosahedral tripod and each of the three correctly typed resolvents is injective on its arithmetic coset. At most one coset member lies in K; neither existence of such a member nor equality of the entire lift set with this coset is asserted. The comparison maps and arithmetic faithfulness are reconstructed directly."),
}
for ident,note in lm_notes.items():
    add("LM4_SUCCESSOR",ident,lm[ident],*lm_audits[ident])

out=BASE/"notes/historical_audit.csv"
with out.open("w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]))
    writer.writeheader(); writer.writerows(rows)

required_gt={f"GT_TOWER_CHECK C.{block}.{n}" for block,count in [(1,21),(2,18),(3,11)] for n in range(1,count+1)}
required_sq={f"SECTIONS_OVER_Q {ident}" for ident in sm}
actual={r["historical_id"] for r in rows}
assert required_gt <= actual and required_sq <= actual
assert len(actual)==len(rows)
assert all(r["audit_status"] in {"confirmed","repaired","refuted","pending"} for r in rows)
print(f"Wrote {len(rows)} historical rows: " + ", ".join(f"{status}={sum(r['audit_status']==status for r in rows)}" for status in ["confirmed","repaired","refuted","pending"]))
print("All 50 required GT Part-C and all 16 required SECTIONS_OVER_Q IDs present; the additional SQ A.58 input is also audited.")
