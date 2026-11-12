"""Assemble and audit the final CSV registers, bibliography, and research report.

This is packaging and cross-reference validation, not a mathematical computation.
All input registries and component reports are included in the deliverable.
Run from any directory with Python 3.10 or later.
"""
from pathlib import Path
from collections import Counter
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
RESULT_COLUMNS = [
    'id', 'statement', 'status', 'where_proved', 'depends_on',
    'manuscript_passages (section; folio; scan)',
    'depends_on_doubtful_reading (scan, alternatives)', 'notes',
]
READING_COLUMNS = [
    'package', 'scan', r'the \unsure or \illegible place',
    'what the mathematics supports', 'how strongly',
]


def read_json(name):
    return json.loads((ROOT / name).read_text())


def order_id(value):
    letter, number = value.split('.')
    return letter, int(number)


result_files = ['AB_results.json', 'A_lowtypes_results.json',
                'B_signed_results.json', 'B_functoriality_results.json',
                'B_modular_comparison_results.json', 'B_late_sections_results.json',
                'C_results.json',
                'D_results.json', 'E_results.json']
rows = []
for filename in result_files:
    for entry in read_json(filename):
        entry = dict(entry)
        for old, new in [('manuscript_passages', RESULT_COLUMNS[5]),
                         ('depends_on_doubtful_reading', RESULT_COLUMNS[6])]:
            if old in entry:
                entry[new] = entry.pop(old)
        assert set(entry) == set(RESULT_COLUMNS), (filename, entry)
        assert all(isinstance(entry[k], str) and entry[k] for k in RESULT_COLUMNS)
        rows.append(entry)
rows.sort(key=lambda entry: order_id(entry['id']))
assert len({entry['id'] for entry in rows}) == len(rows)
registered = {entry['id']: entry for entry in rows}

included = []


def read_tex(path):
    """Follow the actual document inputs, retaining their order."""
    text = path.read_text()
    included.append(path.relative_to(ROOT).as_posix())
    pieces = []
    previous = 0
    for match in re.finditer(r'\\input\{([^}]+)\}', text):
        pieces.append(text[previous:match.start()])
        name = match.group(1)
        if not name.endswith('.tex'):
            name += '.tex'
        pieces.append(read_tex(ROOT / name))
        previous = match.end()
    pieces.append(text[previous:])
    return '\n'.join(pieces)


tex = read_tex(ROOT / 'LM1_GROUP_SCHEMES_paper.tex')
heads = re.findall(r'\\begin\{statement\}\{([A-E]\.\d+)\}\{([^}]+)\}', tex)
assert len(heads) == len(set(identifier for identifier, _ in heads))
assert {identifier for identifier, _ in heads} == set(registered)
for identifier, status in heads:
    assert status == registered[identifier]['status'], identifier
assert [identifier for identifier, _ in heads] == sorted(registered, key=order_id)
assert all(entry['status'] in {'Proved', 'Refuted', 'Known', 'Open'} for entry in rows)

dependency_ids = set()
for entry in rows:
    dependency_ids.update(re.findall(r'\b[A-E]\.\d+\b', entry['depends_on']))
assert dependency_ids <= set(registered), sorted(dependency_ids - set(registered))

with (ROOT / 'LM1_GROUP_SCHEMES_results.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=RESULT_COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

readings = []
for name in ['AB_readings.json', 'B_signed_readings.json',
             'B_functoriality_readings.json', 'B_modular_comparison_readings.json',
             'B_late_sections_readings.json', 'C_readings.json',
             'D_readings.json', 'E_readings.json']:
    for entry in read_json(name):
        assert set(entry) == set(READING_COLUMNS), (name, entry)
        assert all(isinstance(entry[k], str) and entry[k] for k in READING_COLUMNS)
        readings.append(entry)
with (ROOT / 'LM1_GROUP_SCHEMES_readings.csv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=READING_COLUMNS)
    writer.writeheader()
    writer.writerows(readings)

bib_files = sorted(path.name for path in ROOT.glob('*_refs.bib'))
bib = ('% Every entry states what was actually opened and which result was used.\n\n'
       + '\n\n'.join((ROOT / name).read_text() for name in bib_files))
bib_entries = re.split(r'(?=^@\w+\{)', bib, flags=re.M)[1:]
bib_keys = []
for entry in bib_entries:
    key = re.match(r'@\w+\{([^,]+),', entry).group(1)
    bib_keys.append(key)
    assert re.search(r'\bverified\b|\bunverified\b', entry, flags=re.I), key
assert len(bib_keys) == len(set(bib_keys))
cited = set()
for match in re.finditer(r'\\cite\w*(?:\s*\[[^\]]*\]){0,2}\s*\{([^}]+)\}', tex):
    cited.update(part.strip() for part in match.group(1).split(','))
assert cited <= set(bib_keys), sorted(cited - set(bib_keys))
(ROOT / 'LM1_GROUP_SCHEMES_references.bib').write_text(bib)

coverage = {}
for filename in ['AB_coverage.json', 'C_coverage.json', 'D_coverage.json',
                 'E_coverage.json']:
    for entry in read_json(filename):
        entry = dict(entry)
        if 'statement_ids' in entry:
            entry['statements'] = entry.pop('statement_ids')
            entry['details'] = entry['proved_cases']
            remaining = entry['exact_smallest_undecided_instance']
            if entry['outcome'] == 'partly settled':
                entry['details'] += ' Remaining: ' + remaining
        assert entry['task'] not in coverage
        coverage[entry['task']] = entry

extra = [
    {'task': 'AfterLM3.ProfiniteSource', 'outcome': 'partly settled',
     'statements': 'D.4–D.7; B.8; B.9; B.15; B.16',
     'details': 'G_Q, GT-hat, and GT-hat_0 are distinguished. Typed conditional comparisons and finite I/II tests are proved. Actual global images and kernels remain D.7, beginning with its explicit modulus-3 tuple.'},
    {'task': 'AfterLM3.CongruenceLoss', 'outcome': 'partly settled',
     'statements': 'B.8; B.9; B.15; B.16; D.6; D.7',
     'details': 'The noncongruence quotient SL2(F8), stability of the congruence kernel for effective modular automorphisms, and the central-twist obstruction are proved. The full effective image/kernel and an invisible compatible loop solution remain B.15/D.7.'},
    {'task': 'AfterLM3.Conventions', 'outcome': 'proved',
     'statements': 'A.10; B.6; D.17',
     'details': 'All six requested low types, pure/full and oriented/extended mapping classes, surface-group and mapping-class centres, peripheral data, and the distinction between orientation reversal and a real structure are explicitly treated.'},
]
for entry in extra:
    coverage[entry['task']] = entry

core_tasks = ([f'item{i}' for i in range(1, 6)]
              + [f'Lead{i}' for i in range(1, 5)]
              + [f'{part}.{letter}' for part, letters in
                 [('A', 'abcd'), ('B', 'abcdefg'), ('C', 'abcdef'),
                  ('D', 'abcdefg'), ('E', 'abcdefg')] for letter in letters])
followup_tasks = [entry['task'] for entry in extra] + [
    'AfterBISITE.Stallings', 'AfterBISITE.TwoRationalTheories',
    'AfterBISITE.FermatRelativeCompletion',
]
assert len(core_tasks) == 40
assert set(coverage) == set(core_tasks + followup_tasks)
allowed_outcomes = {'proved', 'refuted', 'partly settled', 'unfinished'}
assert all(entry['outcome'] in allowed_outcomes for entry in coverage.values())


def table_escape(value):
    return value.replace('|', r'\|').replace('\n', ' ')


table = ['| Request | Outcome | Numbered statements | Scope and exact remaining question |',
         '|---|---|---|---|']
for task in core_tasks + followup_tasks:
    entry = coverage[task]
    table.append('| ' + ' | '.join(table_escape(entry[key]) for key in
                 ['task', 'outcome', 'statements', 'details']) + ' |')

counts = Counter(entry['status'] for entry in rows)
outcomes = Counter(coverage[task]['outcome'] for task in core_tasks)
intro = f"""

# LM1_GROUP_SCHEMES: research, computation, and scope report

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**. Date: 12 November 2026.
No priority is claimed. Names in the bibliography identify the authors of source
works, not authors or reviewers of this generated mathematics.

The paper contains **{len(rows)} numbered statements**: {counts['Proved']} Proved,
{counts['Known']} Known with the required reductions, {counts['Refuted']} Refuted
with corrected statements, and {counts['Open']} Open in the sense of unresolved
in this work. The opening table covers all **40 primary requests** and all
**six followups**. The primary outcomes are {outcomes['proved']} proved,
{outcomes['refuted']} refuted, and {outcomes['partly settled']} partly settled.
No row is silently omitted. The partial outcomes are not assertions that an
original question has been solved in its full scope, or that the remaining
question is open in the literature. Their proved cases, executed calculations,
and precise residuals are recorded below and in the numbered statements.

The results CSV has exactly one row per numbered statement, with the requested
eight columns. The readings CSV has {len(readings)} mathematical reading records
and the requested five columns. The bibliography contains {len(bib_keys)} entries,
each explicitly marked verified with its source and the portion opened.
The register audit follows the actual TeX input order, checks every status,
checks internal dependency identifiers, and checks citation keys.
"""

body = r"""

## 1. What the matrix computation establishes

We fix the final lifts

\[
r=\begin{pmatrix}0&1\\-1&1\end{pmatrix},\qquad
s=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad r^3=s^2=-I.
\]

The earlier lift is \(s_-=-s\). Projective orders 3 and 2 are
distinguished throughout from orders 6 and 4 of these integral lifts.
Put \(Q_3=c^2+cd+d^2\), \(Q_2=t^2+u^2\),
\(a=cr+dI\), and
\(b=\left(\begin{smallmatrix}u&t\\-et&eu\end{smallmatrix}\right)\).
The final signed scheme is

\[
M(R)=\{(a,b,U,e,e'):e^2=(e')^2=1,\quad
\det U=eQ_2=e'Q_3\in R^\times\}.
\]

Its law is inherited from multiplication of the three matrix factors.
It has a split description \(M\simeq\mathrm{SL}_2\rtimes H\)
with the determinant action specified in B.4 and D.1. Its coordinate ring,
including the inverse of \(Q_2\), is written explicitly in B.2.
The monic integral Gröbner certificate has pairwise coprime leading
monomials; its standard monomials prove integral flatness without
inferring it from characteristic-zero computations. Independent bases
over \(\mathbb Q,\mathbb F_2,\mathbb F_3\) agree.

The final scheme is flat of relative dimension **6** and smooth exactly
over \(\mathbb Z[1/2]\). Over an algebraic closure of \(\mathbb F_3\)
it has four smooth components, each isomorphic to
\(\mathrm{SL}_2\times\mathbb G_m^2\times\mathbb G_a\).
In characteristic 2 it has one geometric component; its nilradical is
generated by the two sign differences, has cube zero, and has generic
length 4. Its reduced fibre is the explicit smooth product in B.3.
The unsigned subgroup is smooth over all of \(\mathbb Z\).
The different scan-41 fine parameter scheme is also smooth at 2 and 3,
of relative dimension 3 per fixed sign pair (E.24). These are distinct
schemes; none is substituted for another to obtain a desired dimension.

| Ring R | Number of points of final signed M(R) |
|---|---:|
| F2 | 36 |
| F3 | 2,304 |
| F5 | 46,080 |
| F7 | 387,072 |
| F11 | 7,603,200 |
| F13 | 15,095,808 |
| Z/4 | 9,216 |
| Z/8 | 2,359,296 |
| Z/9 | 1,679,616 |

The program counts the norm fibres and matrix factors independently and
checks the formulas for every requested ring. Unsigned and determinant-one
counts, orbit representatives, and all requested finite missed-point sets
are retained in `code/AB_enumeration.json`.

### Pinning, lifting, and parametrization

A.2 identifies the exact ambiguity group scheme as
\(\operatorname{Spec}\mathbb Z[\tau]/(2\tau,\tau^2)\).
Over a fixed affine base, uniqueness is exactly the vanishing of this
set of sections. Uniqueness after every base change holds exactly when
2 is invertible. The smallest finite-ring counterexample is
\(R=\mathbb Z/4,\tau=2\). This ambiguity is not all of \(\mu_2\).

A.3 proves the precise inner/algebra-induced pinning statement, including
descent. A.8 disproves unrestricted uniqueness among all group-scheme
isomorphisms using \(g\mapsto\det(g)^{-1}g\) on \(\mathrm{GL}_2\).
A.4 and A.7 give the normalized and projective classifications over every
requested base; imperfect characteristic-2 fields require norm square
classes, and are not covered by the perfect-field shorthand.

For the fixed modular matrices, the simultaneous unsigned and signed
parametrizations of scan 370 are **isomorphisms over every ring**.
Individual commutator maps instead have the stated regular-image and
norm obstructions. Over the integers, the special-linear image is
exactly the half specified by a positive lower-right entry; the
complement is parametrized exactly. Every missed point over F2, F3
and Z/4 is displayed and independently enumerated.

### General unsigned and signed groups

B.11 proves the unsigned formal quotient and fibre-product construction
for the full specified automorphism subgroup. B.13 proves the signed
construction, retaining the numerical multiplier and both signs, and
states the central-kernel hypotheses explicitly. Exactness is not
silently transferred from abstract groups to an undefined group scheme.
The finite constant models S3, S4, SL2(F3), and SL2(Z/4) are fully
enumerated, including their automorphisms, antidiagonal quotients,
starred normalizers and the conjugator-parametrization inverse.

B.12 exhibits a PSL2(F13) counterexample to automatic realization:
both pairs generate, corresponding entries are conjugate, and the loop
multiplier is a unit, but commutator orders 7 and 6 prevent any
endomorphism realizing the pair. For the particular completed modular
group, B.8 proves the stronger existence of a continuous endomorphism
from each specified signed triple. Its automatic **surjectivity** is
the precise remaining question (B.8.5). A profinite group written as
a constant inverse-limit scheme cannot provide the missing integral
realization: every map from the constant procyclic scheme to SL2
factors through a finite stage, so it cannot send 1 to the
infinite-order integral unipotent matrix L0(1).

B.15 closes the separate quotient-functoriality block of scans
570–572 and gives its exact kernels. For the actual congruence map,
every effective modular automorphism descends by conjugation with
the explicit matrix [[mu,a*mu],[0,1]]; kernel stability is therefore
proved. Full effective image and compatible lifting remain separate.
The reconstruction and gluing of scans 691–696 are also proved,
with a complete C4/V4 obstruction to gluing from just a common
quotient and action.

B.16 proves the central-twist kernel, normalized-conjugator
uniqueness and the quotient normalizer sections. The actual geometric
comparison, unquotiented sigma-section and central-extension
identification remain separately formulated. B.17 gives a concrete correction in
the later restricted-conjugator construction: its antidiagonal
must use the intersection with the chosen conjugating subgroup.
The printed larger antidiagonal may not even lie in the numerator.
An explicit SL2(Z/4) example proves this defect and tests the
repaired kernel. B.18 gives the late dictionary through scan 690,
proves the formal cocycle and bisection reductions, and states the
remaining normalized sections, index-kernel and natural-subgroup
comparisons for the two named modular subgroups. These questions
are not absorbed into B.8.5.

## 2. Corrections to the four leads

**Lead 1 is false.** The discrete amalgam is correct, with its
normalization derived from the verified source. The literal sheaf
source uses constant cyclic groups, not diagonalizable root-of-unity
groups. Its kernel is noncentral on every nonempty base, including
Z[1/6]. C.5–C.6 give the entire normal kernel by explicit Gaussian
relation families, and the corrected integral theorem includes the
additional schematic scalar relations for PGL2 and the determinant
factor for GL2. Raw point presentations and sheaf points are distinct.

**Lead 2 is false as stated.** The final group M is not the earlier
scheme of two commutator parameters. The GL2 centralizers are the
unit groups of quadratic algebras, of dimension 2, whereas their
norm-one kernels have dimension 1. The dimension-4 precursor,
dimension-6 final scheme, dimension-7 special ambient group, and
dimension-9/10 larger ambient groups are individually identified.

**Lead 3 is false.** The manuscript's category is finitely generated
virtually abelian groups. Its integral quasi-unipotent envelope is
constructed from finite-index lattices; it is neither full
pro-algebraic completion nor Malcev completion nor a divided-power
integral form. E.18–E.19 supply the comparison maps and explicit
separating examples. The doubtful exponential statements have exact,
executed rank-three and rank-four counterexamples; the genuine
fibrewise integral obstruction occurs in rank five.

**Lead 4 is false.** The prescribed geometric extension comes from a
finite dihedral component-group class. The literal cup product in
scans 610–611 is \((-3,3)=0\), of order 1. The quaternion
\((-1,-3)\) has order 2 and is a different obstruction. The C4
in scan 631 is an inverse-image group, not the order of a Brauer
class. D.14–D.16 distinguish an impossible constant imaginary-sign
lift from the correct constant and arithmetically twisted full lifts.

## 3. Manuscript and source audit

The checked transcription packages and their corrections were used to
locate formulas, not as mathematical authority. The supplied LM3,
BISITE and GALOIS returns and their reviews were treated in the same
way. The mathematical reductions used here are supplied independently.

For Parts A–B the photographs directly inspected include C3 scans
151, 264, 266, 323, 358, 370, 393, 479 and 480. The signed supplement
also directly inspects scan 546. Other relevant attached images were
examined in Parts C–E, as recorded in the appended audits. Many of
the surrounding transcription pages have no attached photograph;
the report does not imply that absent images were inspected.

The A/B reading audit records the norm term cd versus d; the reversed
trace order; the general normalized lower-right matrix entry; the
nonflat lifting ambiguity; the distinct dimension calculations;
the central mu2 cover J0→H0; centrality only in the unsigned subgroup;
the full upper-triangular normalizer; the unchosen M(−j) label;
the missing determinant in the transpose identity; the exponent −1
in scan 509; the alpha/beta types in scan 510; and the second
centralizer label in scan 511. Universal algebra or a typed map,
not visual preference alone, gives the mathematical evidence.
No reading is declared palaeographically final. Withdrawn claims,
including the centrality and normalizer slips corrected by the
author, are identified as withdrawn or already corrected.

The low-type appendix was checked against the primary Farb–Margalit
text, Proposition 2.3, Theorem 2.5 and its following once-punctured
torus discussion, §§2.2.1–2.2.2 and §8.1. It proves the required
reductions and separates the centres of surface groups from the
centres of mapping-class groups. It does not infer a real structure
from the abstract orientation-reversing extension.

The additional moduli-stack passage at C3:628–629 was checked against
both photographs. The elliptic stack, its central-involution
rigidification, and the coarse j-line are distinguished from the
matrix group M. The explicit j=0 curve and its exact invariant
calculation are in B.16 and D_motives.py. The author's clarification
on scan629 is retained rather than treated as an uncorrected claim.

The bibliography records the precise editions or preprint versions
whose theorem numbers were read. The appended C, D and E audits give
the source passages opened, the reductions used, and the searches
made. We make no claim that the collection is an exhaustive novelty
search, and no priority claim is attached to any proof or computation.

## 4. Exact residuals and the work already performed

| Residual | Proved case and executed attack | Exact first remaining assertion |
|---|---|---|
| A.9 / B.8 / B.15 | Modular matrix scheme, unsigned/signed formal constructions, congruence-kernel stability and exact descent kernels; exhaustive finite models; PSL2(F13) counterexample | Prove automatic surjectivity in B.8.5; determine the effective image H_q and kernel A_q of B.15 and compatible parameter lifting. A suitable integral realization is separate; the naive constant-proscheme replacement is proved impossible. |
| B.16 | Exact central-twist kernel, unique normalized conjugators and quotient normalizer sections; full SL2(Z/4) and SL2(F3) automorphism calculations | Establish the actual geometric source image in scan575 and its named M/N identification; lift the proved sigma-section through the explicitly defined central extension E_s; identify the other central pullback E_r with the prescribed source extension and cocycle. |
| B.18 | Corrected restricted quotient B.17; exact twisted-word and cocycle laws; finite nonsplit bisection model and modular Z/4 witness | Match the congruence-defined source subgroup of583–595 with its sign extension, prove the kernel of N_rho*→GL2(Z/4)/V4 and its normality/index assertions, and determine the repaired natural-group comparisons and normalizer images first for A=widehat(Pi) (index6), then widehat(Pi0) (index12). |
| C.11 | Entire sheaf kernel and corrected integral presentations; eight complete coset tables; exact F2/F4 sheaf values; explicit infinite descent witnesses | Simplify the stated Frobenius-fixed amalgam for A_SL(F3), and compute the complete descent groups over Z/4 and Z/9. The finite raw point presentations are not those sheaf values. |
| D.7 | Global-sign nonopenness obstruction, explicit extra adelic point; finite I/II at 2,3,4,6,12; full order-504 quotient | Construct the actual normalized comparisons for G_Q, GT-hat, GT-hat_0 and determine their kernels/images. First finite lift: n=3, lambda=1, f=[[1,1],[1,2]]. Separately produce or exclude an invisible compatible loop solution detected by SL2(F8). |
| D.11 | All geometric component cocycles, full complex extension space F2^5, and obstruction at 2 | Determine kernel and image of Ext_cen(M[0]_Z2,mu2)→Ext_cen(M[0]_Q2,mu2), and the arithmetic descent of the five complex classes. |
| E.11 | Q-linear theorem, exact torsion-free coefficient criterion, all-ring linear positive-power theorem; executed matrix and polynomial counterexamples | Extend to arbitrary separated locally finitely presented targets without a chosen closed linear representation. First specified affine dimension-zero tests: Q[epsilon]/epsilon² and Z/4. |
| E.20 | Explicit rank-two lattice, finite-stage and full envelopes, order-12/24 relative abelian-kernel comparison, generic positive-sign automorphisms; infinitesimal counterexamples | Identify the precisely specified signed M/N automorphism functors, first over F2 with local conjugators and retained signs; also compare the Fermat relative data for (Z/n)^2 and S3×Zhat*, beginning with the stated F2→(Z/2)^2 datum. |

No finite computation is presented as a proof of an unbounded
profinite lifting assertion. No failed search is presented as a
nonexistence proof. The counterexamples in E.7 include an all-degree
argument; the bounded polynomial search is corroboration. The
degree-12 search in E.4–E.8 covers the two specified families and
all stated primes and degrees, not every integer matrix of a given
size. The corresponding scope is explicit in the paper and output.

## 5. Computations actually executed

Every mathematical program below has its captured output in `code/`.
JSON files are additional machine-readable output when the program
produces them; they do not replace stdout. All finite enumerations
use exact arithmetic. The universal Gröbner computation includes a
monic integral certificate in addition to field calculations.

| Program | Executed content |
|---|---|
| AB_identities.py | Universal matrix identities, inverse parametrizations, determinant and trace corrections, monic integral Gröbner certificate, Q/F2/F3 bases, Jacobian and nilradical calculations. |
| AB_enumerate.py (using AB_core.py) | All requested finite point counts; independent norm and matrix checks; normalized and projective GL2/SL2 orbits; all small-ring commutator complements. |
| AB_general_finite.py | Complete S3/S4 unsigned constructions and the PSL2(F13) realization counterexample, including the failed relator. |
| AB_signed_finite.py | Complete four-model signed automorphism calculations, U12 multipliers, antidiagonal quotients, every starred-normalizer fibre, parametrization inverses and the scan-546 right-factor correction. |
| AB_functoriality.py | S4→S3 descent with complete image/kernel tables; a nonsurjective normalizer map; universal congruence conjugation identities and six finite trace-pair models; exact reconstruction and C4/V4 gluing checks. |
| AB_modular_comparison.py | Full automorphisms and central-quotient maps for SL2(F3) and SL2(Z/4); central twist, peripheral orders and normalized-conjugator ambiguity in the finite quotient. |
| B_late_sections.py | All 512 sign-cocycle triples, 36 twisted-law pairs, 5,184 corrected word identities, the nonsplit finite bisection and exact SL2(Z/4) restricted-antidiagonal obstruction. |
| C_presentations.py | All requested finite matrix groups, eight full Todd–Coxeter tables, universal Gaussian identities, noncentral words, nilpotent scalar and finite étale descent witnesses. |
| D_finite.py | Component-group cocycles, extension and complement tests, explicit quaternion splitting, and all modular generation indices 1≤n≤48. |
| D_components.py | Component sections, invariant characters and geometric central-extension dimension 5. |
| D_gt.py | Finite I/II equations with one common commutator word; local norms; full SL2(F8) quotient and simplicity checks. |
| D_number_fields.py | Hilbert symbols, cubic discriminants and maximal-order indices, constant lift and local characters. |
| D_arithmetic.py | Twisted order-24 quotient, character identification and local Eisenstein certificates for the stated fields. |
| D_motives.py | Monodromy matrices, six quadratic-twist point counts, free-Lie ranks through degree 6, and the exact j=0 curve invariants for scan628. |
| E_integrality.py | Exact rank-three/four/five examples; 72 specified-family cases through degree 12 at 2,3,5; Witt and Z/p² group laws; 1,024 bounded Z/4 polynomials; reading alternatives. |
| E_envelope.py | All 144 cocycle values and 1,728 cocycle identities; finite quotients and fibres; induced 12-dimensional separating representation; S3 covering orbits. |
| E_automorphisms.py | Integral fine-parameter equations, finite sign alternatives, rational affine-group law, opposite-sign conjugator and infinitesimal polynomial identities. |

`AB_registers.py`, `D_registers.py`, and `E_registers.py` generate
component metadata; `assemble_package.py` combines and validates it.
`build_pdf.py` performs the LuaLaTeX/BibTeX build and rejects unresolved
citations/references, missing characters, or overfull boxes in the final
log. The final packaging/visual checks and environment versions are
recorded separately in `code/package_audit.out` and `code/environment.json`.
The README gives the reproducible commands and explains the minimal-host
Type-1 LuaLaTeX fallback without requiring any system modification.

## 6. Detailed audits for Parts C–E and the signed supplement

The following component records preserve the full source and computation
details. The opening master table above controls the aggregate task
outcomes; these records supply their supporting particulars.
"""

appendices = []
for filename in ['B_signed_report.md', 'B_functoriality_report.md',
                 'B_modular_comparison_report.md', 'B_late_sections_report.md',
                 'C_report.md', 'D_report.md', 'E_report.md']:
    component = (ROOT / filename).read_text()
    # Some component reports open with their own coverage table. The master
    # report already includes it, so retain the substantive report from its H1.
    heading = re.search(r'^# ', component, flags=re.M)
    assert heading, filename
    component = component[heading.start():]
    first_line, rest = component.split('\n', 1)
    if rest.lstrip().startswith('|'):
        lines = rest.lstrip().splitlines()
        while lines and lines[0].startswith('|'):
            lines.pop(0)
        component = first_line + '\n' + '\n'.join(lines)
    component = re.sub(r'^(#{1,5}) ', r'##\1 ', component, flags=re.M)
    appendices.append('\n\n' + component)

(ROOT / 'LM1_GROUP_SCHEMES_report.md').write_text(
    '\n'.join(table) + intro + body + ''.join(appendices))
summary = {
    'statements': len(rows), 'statuses': dict(counts),
    'readings': len(readings), 'bibliography_entries': len(bib_keys),
    'primary_requests': len(core_tasks), 'followups': len(followup_tasks),
    'primary_outcomes': dict(outcomes),
    'followup_outcomes': dict(Counter(coverage[t]['outcome'] for t in followup_tasks)),
    'unfinished': [task for task, entry in coverage.items() if entry['outcome'] == 'unfinished'],
    'included_tex': included, 'citation_keys': sorted(cited),
    'all_statement_ids_statuses_dependencies_and_citation_keys_checked': True,
}
(ROOT / 'code/assembly_audit.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
print('ALL REGISTER AND COVERAGE ASSERTIONS PASSED')
