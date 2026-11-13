#!/usr/bin/env python3
"""Freeze E.88 with the exact all-level scope and retained arithmetic."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1];L=ROOT/'ledger';L.mkdir(exist_ok=True)
proof=ROOT/'sections/E_global_sdivisors.tex'
s=proof.read_text()
assert len(re.findall(r'^\\\[$',s,re.M))==len(re.findall(r'^\\\]$',s,re.M))==17
assert len(re.findall(r'\\tag\{E88\.\d+\}',s))==16
assert not any(ord(c)<32 and c not in '\n\t\r' for c in s)
assert not re.search(r'(?<!\\)\b(?:quad|qquad)\b',s)
cert=json.loads((ROOT/'code/e_global_sdivisors.json').read_text());assert cert['status']=='PASS'
def save(n,o):(L/n).write_text(json.dumps(o,indent=2)+'\n')
save('e_global_sdivisors_results.json',[{
 'id':'E.88','status':'Proved',
 'statement':'The entire complex multiplicative norm system has outside-{3,17} divisor image exactly the kernel of two mod3 congruences evaluated in the fixed certified degree6 field L1. The proof supplies compatible lifts by compact fibers, a complete restricted Z3 pivot basis, a convergent product splitting and its exact choice ambiguity. The compact kernel is the full coherent S-unit product of E69/E72. The normalized base3 phase is evaluated modulo3 by the actual L2 ordinary class map. For the entire complex positional component with pure component1, the total-norm cube condition is exactly b in3Z3, D=3r and sum c_p r_p=0 mod3, with the actual scaled toric map and two explicit norm-coherent examples.',
 'where_proved':'sections/E_global_sdivisors.tex, E88.1--E88.16 and full proof; code/e_global_sdivisors.py/.gp, complete two-stage reconstruction, all actual outputs and BIN certificate.',
 'depends_on':['E.46','E.57','E.69','E.72','E.86','E_PARICertifiedUnits'],
 'manuscript_passages':['LM section51.16, folios733v--736v, scans172--178; exact positional, norm, divisor and toric comparisons E.46,E.69,E.72,E.86.'],
 'depends_on_doubtful_reading':False,
 'notes':'The all-level sufficiency uses compact completed S-unit fibers, never compactness of the infinite restricted divisor module. The two congruences are actual L1 class coordinates and their necessity/sufficiency are both proved. Eventual h and the phase modulo3^h beyond the evaluated modulo3 reduction remain retained arithmetic data. Full author reconstruction session62031 exited0. No intrinsic metabelian/marked preimage is inferred from the exact H-target comparison.'}])
save('e_global_sdivisors_coverage.json',{
 'statement':'E.88','scope':'Exact complex norm-system evaluation within E(c),E(d),Lead3.',
 'completed':[
 'All higher outside-S S-principal class equations replaced by two explicitly evaluated L1 mod3 conditions.',
 'Both directions of coherent multiplicative lifting, including all norm compatibilities.',
 'Complete restricted pivot coordinates, continuous product splitting and full choice ambiguity.',
 'Exact compact S-unit kernel and explicit norm-system coordinate inverse.',
 'Actual L2 ordinary-to-S comparison and normalized base3 phase modulo3.',
 'Entire pure-component1 complex H cube locus, scaled toric map and literal beta+1/beta-1 examples.'],
 'remaining':['Evaluate the original eventual exponent h and the residual phase modulo3^h.',
              'Evaluate the complete pure radical component and the remaining intrinsic comparison kernels.'],
 'combined_original_tasks_complete':False})
save('e_global_sdivisors_source_evidence.json',{
 'statement':'E.88',
 'primary_sources':[{
  'key':'E_PARICertifiedUnits',
  'url':'https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.19.0/users.pdf',
  'local_source':'research_e52/vendor/pari-2.19.0/doc/usersch3.tex',
  'passages':'bnfcertify,bnfisprincipal,bnrisprincipal,idealhnf; official entries read before use.',
  'use':'The one fixed L1 field is certified with default flag0, return1. Every eligible residue prime is an actual maximal-order ideal; the class and Artin maps use retained generator coordinates.'}],
 'proved_comparisons':['E86 actual all-level S-class norm identities and coherent prime bases.',
                       'E72 exact completed divisor norm system and local prime-chain classification.',
                       'E69 actual compact coherent3-unit coordinates and base projection.',
                       'E46 exact Kummer-Shapiro positional norm map and division-by3 toric coordinate.'],
 'new_proof':'Finite-index completion exactness; finite-chain compact-fiber sufficiency; restricted Z3 pivot basis and convergent product splitting; precise ambiguity; ordinary L2 phase and both directions of total-norm cube condition.',
 'audit':'Requested from A and root; author full proof and exact two-stage execution complete.'})
save('e_global_sdivisors_computation_status.json',{
 'complete_author_run':{'session_id':62031,'exit_code':0,
   'command':'python research_e88/code/e_global_sdivisors.py --gp research_e52/vendor/pari-2.19.0/gp',
   'stages':['e_stable_lower_genus.gp','e_global_sdivisors.gp'],
   'output':'code/e_global_sdivisors.out'},
 'retained_attempt':{'source':'code/e_global_sdivisors_syntax_attempt.gp',
  'output':'code/e_global_sdivisors_syntax_attempt.out',
  'outcome':'Actual PARI syntax error from one extra closing parenthesis in the rational-matrix exporter; corrected source and full reconstruction pass. No arithmetic assertion uses the failed run.'},
 'certification_counts':cert})
(L/'e_global_sdivisors_refs.bib').write_text(
 '% Existing bibliography keys only.\n'
 '% verified: E_PARICertifiedUnits, official2.19.0 class/ideal/ray entries.\n'
 '% The compact inverse-limit and topology arguments are proved directly in E88.\n')
(L/'e_global_sdivisors_report.md').write_text("""# E.88: the entire complex norm system

The all-level outside-{3,17} class problem now reduces to two congruences in the one certified degree6 field L1. Norm identifies every higher S-class group with its specified L1 coordinates. Each zero-class divisor fiber is a compact completed S-unit torsor; compatible finite chains and the finite-intersection property give an actual coherent lift. This proves sufficiency as well as necessity.

The actual primes7 and73 give the pivot lattice. Its basis is3e7,3e73, and e_p+c_p e7−(c_p+d_p)e73. Exact forward/inverse formulas give Z3² times the restricted sequence module. Choosing one coherent lift per basis vector gives a continuous product splitting. Its full ambiguity is a continuous homomorphism into the coherent3-unit group after normalizing the17-valuation to zero.

The compact kernel is beta^Z3 times E69's entire coherent3-unit group. Consequently E88 gives forward and inverse product coordinates for the whole complex multiplicative norm system. Restricted sequence factors remain prodiscrete and are not treated as compact.

The actual L2 ordinary class group evaluates the normalized base3 phase modulo3. It yields both directions of the total-norm cube condition for the entire complex component with pure component1: D=3r, the17 coordinate divisible by3, and one explicit congruence sum c_p r_p=0. The scaled toric map retains the actual h and phase modulo3^h. The literal coherent families beta_d+1 and beta_d−1 have rational norms273 and307; their cubes give actual H-section examples.

## Rebuild

    python research_e88/code/e_global_sdivisors.py --gp research_e52/vendor/pari-2.19.0/gp

The driver also works in a flat final code directory with e_stable_lower_genus.gp beside it. It performs only a certified degree6 BNF, writes every output and retains its BIN data. The full author run62031 exited0.

Checks:79 eligible primes through2000;790 literal coherent root-chain identities; complete79-dimensional pivot Smith maps/inverses;729 kernel cases;120 exact inverse-coordinate cases;2187 complete modulo9 cube-condition cases; nine uniform-tail checks; and the exact polynomial norm signs for both explicit families. A historical syntax-error source/output is retained without an arithmetic conclusion.

The remaining h and the phase modulo3^h beyond modulo3 are stated as actual arithmetic data. This computes the complex H-target component through E46; the remaining pure component and intrinsic quotient preimages retain their exact comparison tasks.
""")
files={}
for d in ['sections','code']:
 for p in sorted((ROOT/d).glob('*')):
  if p.is_file() and p.name!='e_global_sdivisors_freeze.out':
   files[str(p.relative_to(ROOT))]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
save('e_global_sdivisors_manifest.json',{'statement':'E.88','status':'author-frozen','files':files,
 'rebuild':'python code/e_global_sdivisors.py --gp PATH_TO_OFFICIAL_PARI_GP'})
print('PASS: E88 exact proof, arithmetic certificate, ledgers and manifest.')
for p in [proof,ROOT/'code/e_global_sdivisors.py',ROOT/'code/e_global_sdivisors.json']:
 print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
