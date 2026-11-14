"""Integrate four fully audited results without closing the unrestricted tasks."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'LM7_FERMAT_TOWER'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
enc = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + '\n'
specs = [
    ('D.56', 'D56_EXPERIMENTS', 'd_arithmetic_detecting_quotient', 'D_arithmetic_detecting_quotient.tex', 'root_d56_audit'),
    ('E.101', 'research_e101', 'e_unit_norm_complete', 'E_first_unit_norms.tex', 'root_e101_audit'),
    ('E.103', 'research_e103', 'e_quartic_odd', 'E_quartic_odd_abelian.tex', 'root_e103_audit'),
    ('E.104', 'research_e104', 'e_two_prime_full_family', 'E_two_prime_full_family.tex', 'root_e104_audit')]
pending = {}
reasons = {}
mapping = []
def prep(p, data, why):
    pending[p] = data.encode() if isinstance(data, str) else data
    reasons[p] = why
def add_file(source, target, why):
    if target.exists():
        assert target.read_bytes() == source.read_bytes(), target
    else:
        prep(target, source.read_bytes(), why)

for ident, staging, stem, section, audit in specs:
    src = ROOT / staging
    mf = src / 'ledger' / (stem + '_manifest.json')
    manifest = read(mf)
    rows = manifest['files']
    if isinstance(rows, dict):
        rows = [{'path': k, 'sha256': v if isinstance(v, str) else v['sha256']} for k, v in rows.items()]
    for row in rows:
        assert sha(src / row['path']) == row['sha256'], row['path']
    assert read(ROOT / audit / 'comparison.json')['status'] == 'PASS'
    assert not (BASE / 'sections' / section).exists()
    for folder in ['sections', 'code', 'ledger']:
        for p in sorted((src / folder).rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts:
                continue
            relative = p.relative_to(src)
            # This is supplementary coverage evidence, not one of the33
            # authoritative coverage tables consumed by assemble.py.
            if ident == 'E.101' and p.name == 'e_unit_norm_complete_coverage.json':
                relative = Path('ledger/e101_staging') / p.name
            if ident == 'E.101' and p.name in ['e_unit_norm_freeze.py', 'e_unit_norm_freeze.out']:
                relative = Path('code') / ('e101_metadata_freeze' + p.suffix)
            target = BASE / relative
            mapping.append({'statement': ident, 'frozen_path': str(p.relative_to(src)),
                            'archive_path': str(relative)})
            add_file(p, target, 'Frozen ' + ident + ' proof, program, output or metadata.')
    if ident == 'D.56':
        for p in sorted((src / 'audit').glob('*')):
            add_file(p, BASE / 'code/d56_proof_versions' / p.name,
                     'Exact frozen proof versions before source-typing clarification.')
    if ident == 'E.101':
        for p in sorted((src / 'inputs').glob('*.gp')):
            add_file(p, BASE / 'code' / p.name, 'Exact portable E101 dependency source.')
            add_file(p, BASE / 'code/e101_inputs' / p.name, 'Frozen E101 dependency snapshot.')

dpeer = read(ROOT / 'bc_d56_audit/audit.json')
epeer = read(ROOT / 'a_e104_audit/audit.json')
assert dpeer['status'] == epeer['status'] == 'PASS'
assert dpeer['section_sha256'] == sha(ROOT / 'D56_EXPERIMENTS/sections/D_arithmetic_detecting_quotient.tex')
assert epeer['certificate']['section_sha256'] == sha(ROOT / 'research_e104/sections/E_two_prime_full_family.tex')
for relative, digest in epeer['files'].items():
    assert sha(ROOT / relative) == digest, relative
for relative, digest in dpeer['program_sources'].items():
    assert sha(ROOT / relative) == digest, relative
for stage in read(ROOT / 'root_d56_audit/comparison.json')['stages']:
    assert sha(ROOT / 'D56_EXPERIMENTS/code' / stage['program']) == stage['source_sha256']
for name in ['source', 'target']:
    change = read(ROOT / ('D56_EXPERIMENTS/ledger/d56_' + name + '_typing_correction.json'))
    assert change

sd = ('D.56 evaluates an actual irreducible C3^4 quotient of the arithmetic normal span. '
      'The parameter is exactly(2,1,2,1), the marked quotient has order3888, and the original arithmetic action is Int(t^6). '
      'Its exact A4 comparison kernel gives onto integral homology, peripheral-pair, derivation and class-two obstruction maps. '
      'The smaller derivation parameter space has dimension40 and invariant central target dimension2560. '
      'The actual quadratic zero locus and full profinite realization remain unevaluated.')
se101 = ('E.101 evaluates the ordinary-unit product defect as(0,2) and every first ordinary/S-unit norm image. '
         'The L1 ordinary and S-unit quotients are C3^2 and C3^3; the B1 quotients are C3^4 and C3^6. '
         'Literal polynomial norms, an eigenline divisor, actual genus Artin and horizontal norm maps, '
         'six exact congruences, Smith inverses and every nonempty norm fibre are retained. '
         'The next ordinary tower layer and eventual exponent h remain active.')
se103 = ('E.103 computes the unrestricted global odd-primary and prime-to-two abelian section spaces of the plus quartic, '
         'and the rational abelian pushouts at every prime. The actual degree-four coset section, integral isogeny inverses '
         'and evaluated elliptic cohomology give free factor R^6 and restricted prime multiplicities2,11,5. '
         'The exact toric norm map is onto, with fibre multiplicities0,9,3 and free factor R^6. '
         'The higher odd-primary and rational nonabelian targets retain their actual lifting questions; '
         'full profinite source section sets retaining the two-primary abelian obstruction remain empty.')
se104 = ('E.104 computes the complete full and intrinsic-metabelian cubic pro-three section spaces over both infinite '
         'two-prime arithmetic source families of E.55 and E.56. The original-root generator maps, all cusp and residue '
         'coordinates, every ramified and unramified full-to-metabelian fibre, and the boundary topology are explicit. '
         'The calculation checks173 applicable primes through2000; the all-prime assertion follows from the proved actual source maps. '
         'Other arithmetic ramification sets and other geometric prime components remain in E.23.')
details = {'D.56': sd, 'E.101': se101, 'E.103': se103, 'E.104': se104}

for ident, staging, stem, section, audit in specs:
    record = {'status': 'PASS', 'statement': ident,
              'complete_proof_and_all_proof_bearing_mathematical_program_sources_read': True,
              'presented_section_sha256': sha(ROOT / staging / 'sections' / section),
              'complete_fresh_rebuild': read(ROOT / audit / 'comparison.json')}
    if ident == 'D.56':
        record.update({'full_peer_audit': 'ledger/bc_d56_audit.md',
                       'proof_source_typing_corrections': ['ledger/d56_source_typing_correction.json',
                                                         'ledger/d56_target_typing_correction.json'],
                       'all_seven_mathematical_programs_unchanged_after_fresh_run': True,
                       'corrected_subgroup_maps_checked_by_root': True})
    if ident == 'E.101':
        record['audit_guard_provenance'] = 'code/e101_root_rebuild/guard_correction.json'
    if ident == 'E.103':
        record['audit_reader_provenance'] = 'code/e103_root_rebuild/manifest_schema_correction.json'
    if ident == 'E.104':
        record['full_peer_audit'] = 'ledger/a_e104_audit.md'
    prep(BASE / 'ledger' / (audit + '.json'), enc(record), 'Exact completed root verification scope.')
    p = BASE / 'ledger' / (stem + '_results.json')
    rows = json.loads(pending[p])
    rows[0]['where_proved'] += '; ledger/' + audit + '.json'
    rows[0]['notes'] = rows[0].get('notes', '').replace('Parent/peer audit pending.', 'Complete root and peer audits PASS.')
    rows[0]['notes'] += (' The complete copied-source reconstruction agrees with every retained mathematical output; '
                         + ('only named elapsed_seconds fields differ.' if ident == 'D.56' else 'there are no comparison exclusions.'))
    if ident == 'E.104':
        rows[0]['notes'] += ' Independent complete proof/source review and separately coded focused generator checks PASS.'
    prep(p, enc(rows), 'Attach completed independent audit to the presented result.')
    p = BASE / 'ledger' / (stem + '_report.md')
    report = pending[p].decode()
    report += '\n## Completed independent verification\n\n' + details[ident] + '\n\n'
    report += ('Root read the complete proof and all owned mathematical source programs and ran a complete copied reconstruction. '
               'The exact verification record is ledger/' + audit + '.json. ')
    report += ('Every mathematical JSON field and stdout prefix agrees; only the named run times differ. '
               'The independent full peer review and separately written map certificate passed after the retained source-typing clarifications.\n'
               if ident == 'D.56' else 'Every complete stdout and JSON byte agrees without exclusions.\n')
    if ident == 'E.101':
        report += 'All five complete PARI binary objects also agree; no component was excluded. The initial warning-guard repair is retained separately.\n'
    if ident == 'E.103':
        report += 'Root independently opened and checked all four primary theorem inputs and their precise use in the proof.\n'
    if ident == 'E.104':
        report += 'The independent complete peer proof/source review and focused generator/map calculation also passed.\n'
        report = report.replace('A separate full peer review is pending at this freeze.',
                                'The original freeze preceded the separate full peer review, which has now passed and is retained.')
    prep(p, report, 'Record full completed verification in the assembled report.')

for source, target in [('bc_d56_audit', 'bc_d56_audit'), ('a_e104_audit', 'a_e104_audit')]:
    for ext in ['.md', '.json']:
        prep(BASE / 'ledger' / (target + ext), (ROOT / source / ('audit' + ext)).read_bytes(),
             'Independent full peer proof and focused computation audit.')

p = BASE / 'LM7_FERMAT_TOWER_paper.tex'
t = p.read_text()
for anchor, new in [('D_arithmetic_boundary_norm', 'D_arithmetic_detecting_quotient'),
                    ('E_two_three_full', 'E_first_unit_norms'),
                    ('E_kernel_degree4_smith', 'E_quartic_odd_abelian'),
                    ('E_quartic_odd_abelian', 'E_two_prime_full_family')]:
    marker = '\\input{sections/' + anchor + '.tex}'
    assert t.count(marker) == 1
    t = t.replace(marker, marker + '\n\\input{sections/' + new + '.tex}')
prep(p, t, 'Register all four audited mathematical sections.')
p = BASE / 'sections/D.tex'
t = p.read_text()
addition = r'''

D.56 evaluates an actual irreducible $C_3^4$ quotient of
the arithmetic normal span and the unique parameter $(2,1,2,1)$.
The marked quotient has order3888 and actual action
$\operatorname{Int}(t^6)$. Its exact $A_4$ comparison kernel
gives surjective integral homology and class-two boundary maps.
The smaller arithmetic correction space has dimension40,
with invariant central target dimension2560. Its actual
quadratic zero set and full profinite realization remain
unevaluated; every source and comparison kernel is retained.
'''
for ident in ['D.13', 'D.19']:
    a = t.index('\\begin{statement}{' + ident + '}')
    b = t.index('\\end{statement}', a)
    assert 'D.56 evaluates' not in t[a:b]
    t = t[:b] + addition + t[b:]
prep(p, t, 'Record the actual smaller arithmetic target at both original open tasks.')
p = BASE / 'sections/E.tex'
t = p.read_text()
a = t.index('\\begin{statement}{E.23}')
b = t.index('\\end{statement}', a)
addition = r'''

E.101 evaluates all first ordinary-unit and S-unit norm
images, including the scalar previously left on the product
of the two lower free units. Its actual field, divisor,
Artin and horizontal norm maps give every norm fibre.
The next ordinary tower layer and eventual exponent remain active.

E.103 computes all unrestricted global odd-primary and
prime-to-two abelian quartic sections, their onto toric norm
map and every fibre. It also computes every rational abelian
pushout. The degree-four coset section and exact integral
isogeny inverses are supplied. The higher odd-primary and
rational nonabelian targets retain their lifting questions.

E.104 computes the entire full and intrinsic-metabelian
cubic pro-three section spaces for both infinite two-prime
families of E.55 and E.56. All original-root source maps,
ramified cusp coordinates, unramified strata, comparison
fibres and boundary topologies are explicit. General global
ramification and the other geometric prime components remain
outside those completed arithmetic sources.
'''
prep(p, t[:b] + addition + t[b:], 'Keep the complete new cases and the remaining unrestricted scope together.')
for name in ['d_results.json', 'd_coverage.json']:
    p = BASE / 'ledger' / name
    rows = read(p)
    for row in rows:
        if row.get('id') in ['D.13', 'D.19']:
            row['depends_on'].append('D.56')
            row['notes'] += ' ' + sd
        if row.get('task') in ['D.e', 'D.afterLM2.1']:
            row['statement_ids'].append('D.56')
            row['outcome'] += ' ' + sd
            row['remaining_step'] = ('evaluate the actual forty-parameter arithmetic quadratic zero locus and its exact lifting comparison; '
                                     'continue the full arithmetic source to the requested full profinite realization')
    prep(p, enc(rows), 'Update exact original-task state without declaring full realization.')

p = BASE / 'code/assemble.py'
t = p.read_text()
needle = '\ne_rows = []\n'
assert t.count(needle) == 1
block = '\ne_deps[\'E.23\'].extend([\'E.101\',\'E.103\',\'E.104\'])\n'
block += "e_notes['E.23'] += " + repr(' ' + se101 + ' ' + se103 + ' ' + se104) + '\n'
t = t.replace(needle, block + needle)
needle = "(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')"
assert t.count(needle) == 1
block = ('for identifier, section, detail in ' + repr([
    ('E.101', 'E_first_unit_norms.tex', se101), ('E.103', 'E_quartic_odd_abelian.tex', se103),
    ('E.104', 'E_two_prime_full_family.tex', se104)]) + ':\n'
    "    if (BASE/'sections'/section).exists():\n"
    '        for row in e_coverage:\n'
    "            if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
    "                if identifier not in row['statement_ids']: row['statement_ids'].append(identifier)\n"
    "            if row['task'] in ('E.d','E.follow-up-4'):\n"
    "                row['outcome'] += '; ' + detail\n"
    "                row['remaining_step'] = " + repr(
        'evaluate unrestricted coupled global ramification and particular joint origins outside the completed two-prime families; '
        'continue higher wild cubic stages and the higher odd-primary and rational nonabelian quartic targets; '
        'evaluate other-primary and mixed sources, the next ordinary norm/class layer, eventual exponent h and phase modulo3^h') + '\n')
prep(p, t.replace(needle, block + needle), 'Generate complete statement and33-task coverage with exact scope.')

allowed = {BASE / 'LM7_FERMAT_TOWER_paper.tex', BASE / 'sections/D.tex', BASE / 'sections/E.tex',
           BASE / 'ledger/d_results.json', BASE / 'ledger/d_coverage.json', BASE / 'code/assemble.py'}
for p in pending:
    assert not p.exists() or p in allowed, p
changes = []
for p, data in pending.items():
    before = sha(p) if p.exists() else None
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    changes.append({'path': str(p.relative_to(BASE)), 'before_sha256': before,
                    'after_sha256': sha(p), 'reason': reasons[p]})
for source, target in [('root_d56_audit', 'd56_root_rebuild'), ('bc_d56_audit', 'd56_peer_audit'),
                       ('root_e101_audit', 'e101_root_rebuild'), ('root_e103_audit', 'e103_root_rebuild'),
                       ('root_e104_audit', 'e104_root_rebuild'), ('a_e104_audit', 'e104_peer_audit')]:
    dst = BASE / 'code' / target
    assert not dst.exists()
    shutil.copytree(ROOT / source, dst, ignore=shutil.ignore_patterns('__pycache__'))
    (dst / 'README.md').write_text(
        '# Exact independent verification\n\nThe complete audit scope, copied mathematical sources and actual outputs are retained here. '
        'Original staging-directory paths in the audit drivers identify the corresponding archived main-code files and frozen manifests. '
        'The main owned mathematical programs have portable commands in code/README.md. '
        'The audit drivers deliberately require a fresh copied directory; they do not overwrite previous verification evidence.\n')
for name in ['freeze.py', 'freeze.out']:
    shutil.copyfile(ROOT / 'research_e104' / name, BASE / 'code' / ('e104_metadata_' + name))
with (BASE / 'code/README.md').open('a') as f:
    f.write('\n\n## D56, E101, E103 and E104\n\n'
            'D56 runs its seven programs in the order recorded in d_arithmetic_detecting_quotient_manifest.json, beginning with '
            'd_arithmetic_sign_quotient.py and ending with d_arithmetic_affine_homology.py. All read the adjacent frozen D53 graph '
            'and the preceding actual outputs. The fresh complete rebuild and independent row-matrix map verifier are retained.\n\n'
            'Run `python code/e_unit_norm_complete.py --gp /absolute/path/to/gp` for all five E101 arithmetic stages and the '
            'complete independent rational checks. Python3, SymPy and PARI/GP are required; the three exact dependency GP files '
            'are adjacent in code. All full stdout/JSON bytes and all five complete PARI objects were independently compared.\n\n'
            'Run `python code/a_quartic_odd.py --gp /absolute/path/to/gp` for E103, including the owned GP field/elliptic computation. '
            'All literal isogeny, torus, coset, Shapiro and norm-coordinate checks are retained.\n\n'
            'Run `python code/e_two_prime_full_family.py --input code/a_s23_full.json` for E104. It checks all173 applicable '
            'primes through2000 and the full displayed finite coordinate identities; the all-prime proof uses the actual source maps.\n')
(BASE / 'ledger/checkpoint200_integration.json').write_text(enc({
    'status': 'PASS', 'statements': [x[0] for x in specs], 'all_frozen_manifests_checked': True,
    'frozen_to_archive_path_mapping': mapping, 'changes': changes,
    'open_original_tasks': ['D.13', 'D.19', 'E.23'],
    'source_verification_gap': 'The exact D.a original-source scope remains as already recorded.'}))
print(enc({'status': 'PASS', 'statements': [x[0] for x in specs], 'changed_files': len(changes)}))
