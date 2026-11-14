#!/usr/bin/env python3
"""Register reviewed F29 and the exact unnumbered continuation notes."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
changes = []
sha = lambda b: hashlib.sha256(b).hexdigest()
proof = 'work/part_a/f_four_parameter_product_one_images.tex'
proof_hash = '8aa897e0df17844ff6fb538be5770aaace072afa25d14a378cfc934e06d557cd'
assert sha((ROOT/proof).read_bytes()) == proof_hash
gate = json.loads((ROOT/'work/root/final_new_claim_acceptance_268.json').read_text())
assert gate['status'] == 'PASS_ROOT_AND_PEER' and gate['proof_sha256'] == proof_hash

def once(s, a, b):
    assert s.count(a) == 1, (a, s.count(a))
    return s.replace(a, b)

def edit(name, operation):
    p = ROOT/name
    old = p.read_bytes()
    new = operation(old.decode()).encode()
    assert new != old, name
    p.write_bytes(new)
    changes.append({'path': name, 'old_sha256': sha(old), 'new_sha256': sha(new)})

def assembly(s):
    for a, b in [
        (" 'work/part_a/f_three_parameter_product_one_images.tex']",
         " 'work/part_a/f_three_parameter_product_one_images.tex',\n 'work/part_a/f_four_parameter_product_one_images.tex']"),
        (" 'work/part_a/f_three_parameter_product_one_images_results.json']",
         " 'work/part_a/f_three_parameter_product_one_images_results.json',\n 'work/part_a/f_four_parameter_product_one_images_results.json']"),
        (" 'work/root/noncompact_uniform_source_followup_references.bib']",
         " 'work/root/noncompact_uniform_source_followup_references.bib',\n 'work/part_d_attack/zalesskii_2024_prosoluble_reference.bib']")]:
        s = once(s, a, b)
    return s

edit('work/root/assemble.py', assembly)
addition = r'''F.29 proves the larger exact four-parameter locus
$(r,s,t,u,1,1,(rstu)^{-1})$ over every finite coefficient field.
Four actual principal-coordinate charts retain all original source words.
Three charts have complete comparisons of their minimal invariant
subspaces across Frobenius factors; the exceptional overlap has a
forced-lift residual with coordinate $-2$ in its proved odd
characteristic. The fourth chart has an essential line detected by
actual character-one seed conjugates and an explicit Vandermonde
inverse. Summed restriction has rank $6m+1$, and the exact trace
and based sign maps give both marginal image equalities on this locus.
The general character locus and the original full marginal and
interaction comparisons remain unresolved.
'''

def scope(s):
    pattern = r'(\\begin\{claim\}\{F\.7\}.*?)(\\end\{claim\})'
    m = re.search(pattern, s, re.S)
    assert m
    return s[:m.start()] + m.group(1) + addition + m.group(2) + s[m.end():]

edit('work/part_a/f_centralizer_audit.tex', scope)
f_note = ('F29 proves all finite affine marginal images on the exact four-parameter '
          'product-one locus (r,s,t,u,1,1,(rstu)^-1), with summed restriction rank6m+1. '
          'Four actual principal charts retain all sources; complete cross-factor '
          'submodule comparisons, an exceptional residual -2 and an actual '
          'essential-line Vandermonde inverse prove the trace kernel. The exact '
          'trace and based sign maps include both signs and larger original fields. '
          'The general character locus, full marginal equality, interaction image '
          'and original residual equation remain unresolved.')

def metadata(s):
    obj = json.loads(s)
    rows = [obj] if isinstance(obj, dict) else obj
    found = [x for x in rows if x['id'] == 'F.7']
    assert len(found) == 1
    found[0]['notes'] += ' ' + f_note
    return json.dumps(obj, indent=2, ensure_ascii=False)+'\n'

edit('work/part_a/f_centralizer_audit_results.json', metadata)
edit('work/root/pdf_qa.py', lambda s: once(s, "'F.27.', 'F.28.'", "'F.27.', 'F.28.', 'F.29.'"))

def report(s):
    old = ('rows=[(label, current_267[label][0], current_267[label][1])\n'
           '      if label in current_267 else (label, references, state)')
    new = 'current_268 = dict(current_267)\n'
    new += "for _key in ['Lead 3', 'F.b']:\n    _refs, _state = current_268[_key]\n"
    new += "    current_268[_key] = (_refs.replace('F.28', 'F.29'), _state + " + repr(' '+f_note) + ')\n'
    c_note = (' The unnumbered displacement-graph continuation identifies the actual '
              'point stabilizer with the closed graph of b->delta_b in the product '
              'of pointed compact-open homeomorphisms and C0(N). It proves exact '
              'compact-family tail equivalences and constructs a continuous positive '
              'C0 envelope for both maps and inverses. The controlled noncompact '
              'deformation is still unconstructed.')
    d_note = (' A fully executed GL3(F2)^8 times C2^3 diagram has a two-generated '
              'parity kernel, all stated finite peripheral identities, the universal '
              'transitive fixed-point bound and exact unit congruences, yet no '
              'generating triple in the three prescribed reflection classes. The '
              'literal Fhat2 quotient is given; its identification of the original '
              'f,h and alpha, and consequently a quotient of the original E, remain '
              'unproved. This records the exact limit of those finite constraints.')
    new += "for _key in ['Item 5', 'C.b']:\n    _refs, _state = current_268[_key]\n"
    new += '    current_268[_key] = (_refs, _state + ' + repr(c_note) + ')\n'
    new += "_refs, _state = current_268['D.b']\ncurrent_268['D.b'] = (_refs, _state + " + repr(d_note) + ')\n'
    new += ('rows=[(label, current_268[label][0], current_268[label][1])\n'
            '      if label in current_268 else (label, references, state)')
    s = once(s, old, new)
    anchor = "add_report('work/root/research_update_267.md')"
    additions = [
        ('work/root/research_update_268.md', None),
        ('work/part_a/f_four_parameter_product_one_images_report.txt', 'All-field affine images on the exact four-parameter locus'),
        ('work/part_c/compact_family_displacement_graph_report.txt', 'Actual displacement graph and compact-family tail envelopes'),
        ('work/part_d_attack/finite_pants_diagram_gl3_2.txt', 'Exact finite pants diagram with a two-generated parity kernel'),
        ('work/part_d_attack/finite_generation_primary_source_check.txt', 'Primary-source read scope for finite-generation follow-up'),
        ('work/part_d_attack/zalesskii_2024_metadata_read_scope.txt', 'Verified metadata and precise prosoluble comparison hypotheses'),
    ]
    lines = [anchor] + ['add_report('+repr(p)+((',title='+repr(t)) if t else '')+')' for p,t in additions]
    return once(s, anchor, '\n'.join(lines))

edit('work/root/make_report.py', report)

def package(s):
    s = once(s, 'checkpoint_267_extra_paths.json', 'checkpoint_268_extra_paths.json')
    start = s.index('f28_manifest=ROOT/')
    end = s.index('for name in sorted(inputs):', start)
    block = s[start:end].replace('f28_', 'f29_').replace('F28', 'F29').replace(
        'f_three_parameter_product_one_images', 'f_four_parameter_product_one_images')
    s = s[:end] + block + s[end:]
    start = s.index('for entry in f28_routes:')
    end = s.index('required = json.loads', start)
    block = s[start:end].replace('f28_', 'f29_').replace('F28', 'F29')
    return s[:end] + block + s[end:]

edit('work/root/package_deliverable.py', package)
assert sha((ROOT/proof).read_bytes()) == proof_hash
(ROOT/'work/root/integration_268_source_changes.json').write_text(json.dumps({
    'status': 'REGISTERED_REVIEWED_F29', 'proof_sha256': proof_hash,
    'changes': changes, 'unnumbered_notes': ['compact_family_displacement_graph', 'finite_pants_diagram_gl3_2'],
    'new_bibliography_key': 'D-ZalesskiiProsolubleSubgroups2024'}, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'changed_files': len(changes),
                  'new_claims': ['F.29'], 'proof_unchanged': True}))
