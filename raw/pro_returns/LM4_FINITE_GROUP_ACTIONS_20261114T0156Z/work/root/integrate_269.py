#!/usr/bin/env python3
"""Register frozen, independently accepted F30 without altering earlier proof text."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[2]
proof = 'work/part_a/f_product_one_first_scalar_field_images.tex'
proof_hash = '1703a98c06269ec8ad73cdd5e420f7213ba620e06a6dcc104905447566a613f5'
assert sha256((ROOT/proof).read_bytes()).hexdigest() == proof_hash
gate = json.loads((ROOT/'work/root/final_new_claim_acceptance_269.json').read_text())
assert gate['status'] == 'PASS_ROOT_AND_PEER' and gate['proof_sha256'] == proof_hash
baseline = ROOT/'work/root/prior_268_snapshot/paper.pdf'
assert sha256(baseline.read_bytes()).hexdigest() == '2038bacd186770710f3a949d2edf6adb92fb800ab6d531133088b6694fd07cd5'
f7_hash = sha256((ROOT/'work/part_a/f_centralizer_audit.tex').read_bytes()).hexdigest()
changes = []

def once(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)

def edit(name, operation):
    p = ROOT/name
    old = p.read_bytes()
    new = operation(old.decode()).encode()
    assert new != old, name
    p.write_bytes(new)
    changes.append({'path': name, 'old_sha256': sha256(old).hexdigest(),
                    'new_sha256': sha256(new).hexdigest()})

def assembly(s):
    s = once(s, " 'work/part_a/f_four_parameter_product_one_images.tex']",
             " 'work/part_a/f_four_parameter_product_one_images.tex',\n 'work/part_a/f_product_one_first_scalar_field_images.tex']")
    return once(s, " 'work/part_a/f_four_parameter_product_one_images_results.json']",
                " 'work/part_a/f_four_parameter_product_one_images_results.json',\n 'work/part_a/f_product_one_first_scalar_field_images_results.json']")

edit('work/root/assemble.py', assembly)
edit('work/root/pdf_qa.py', lambda s: once(s, "'F.28.', 'F.29.'", "'F.28.', 'F.29.', 'F.30.'"))
f_note = (' F30 proves affine marginal image equality for the full product-one character family '
          '(r,s,t,u,v,w,(rstuvw)^-1) on the exact locus k0=k1(r), where '
          'k1=F_p(u,v,w,rstuvw). The actual X1 principal quotient identifies a '
          'five-dimensional boundary kernel. Original source0 acts there by r, '
          'and original sources2 and7 give boundary characters rt and t^-1. '
          'Distinct Frobenius conjugates of r exclude all three minimal-type '
          'comparisons, proving summed restriction rank6m+1 and the exact trace '
          'kernel. The stated coefficient and based sign maps cover every original '
          'finite field and both signs. General product-one characters without '
          'the field-generation equality, full marginal equality and the original '
          'interaction comparison remain unresolved.')

def report(s):
    anchor = ('rows=[(label, current_268[label][0], current_268[label][1])\n'
              '      if label in current_268 else (label, references, state)')
    new = 'current_269 = dict(current_268)\n'
    new += "for _key in ['Lead 3', 'F.b']:\n    _refs, _state = current_269[_key]\n"
    new += "    current_269[_key] = (_refs.replace('F.29', 'F.30'), _state + " + repr(f_note) + ')\n'
    new += ('rows=[(label, current_269[label][0], current_269[label][1])\n'
            '      if label in current_269 else (label, references, state)')
    s = once(s, anchor, new)
    anchor = "add_report('work/root/research_update_268.md')"
    return once(s, anchor, anchor+"\nadd_report('work/root/research_update_269.md')\n"
                "add_report('work/part_a/f_product_one_first_scalar_field_images_report.txt',"
                "title='Product-one affine images on the exact first-scalar field locus')")

edit('work/root/make_report.py', report)

def package(s):
    s = once(s, 'checkpoint_268_extra_paths.json', 'checkpoint_269_extra_paths.json')
    start = s.index('f29_manifest=ROOT/')
    end = s.index('for name in sorted(inputs):', start)
    block = s[start:end].replace('f29_', 'f30_').replace('F29', 'F30').replace(
        'f_four_parameter_product_one_images', 'f_product_one_first_scalar_field_images')
    s = s[:end]+block+s[end:]
    start = s.index('for entry in f29_routes:')
    end = s.index('required = json.loads', start)
    block = s[start:end].replace('f29_', 'f30_').replace('F29', 'F30')
    return s[:end]+block+s[end:]

edit('work/root/package_deliverable.py', package)
historical = '''The intermediate 268-claim build completed all four LuaLaTeX/BibTeX stages with exit code zero. Its final PDF has 608 pages, 4,117,520 bytes and SHA-256 `2038bacd186770710f3a949d2edf6adb92fb800ab6d531133088b6694fd07cd5`. The final TeX SHA-256 is `cd4b5c8425a596878f9520c0346125b5a9273488a2d3f24ee813a96bf2472977`. The complete final logs were independently read; there are no overfull boxes, missing characters, undefined citations/references or fatal errors.

An initial 9.15942-point overflow in F.29.25 was viewed and repaired solely by the reversible gathered-row spacing map recorded in `f29_typesetting_repair.json`. The frozen proof file was unchanged. The final display was actually viewed, and the exact forward and inverse whole-fragment comparison passed. The separate completion record is `f29_typesetting_final_gate_608.json`.

The final visual review binds 84 selected page images to this PDF: 36 freshly viewed pages, split between root and peer, and 48 whole PNG files reproduced byte for byte from the previously reviewed 600-page build. The selection includes every historical overflow passage, the new F.29 section, its difficult matrix, the amended F.7 scope and sample spreads. The combined record `render_review_608.json` has SHA-256 `aff852bc32f486a5799ede8ebb6878d413dc98c9081aa8dfc27e32e5149af599`.

This was a completed intermediate document gate. No 268-claim ZIP was published: F.30 completed both reviews before packaging, and the next archive incorporates that additional proved claim. The exact intermediate PDF and its binding are preserved for the next whole-image comparison. At this stage the register contained 268 claims (237 Proved, 3 Known theorem, 25 Refuted and 3 Open), 88 bibliography records, 77 cited/printed references, 36 manuscript-reading entries and the unchanged 39-obligation table.
'''
edit('work/root/research_update_268.md', lambda s: once(s, 'FINAL_VERIFICATION_268_PENDING', historical.rstrip()))
assert sha256((ROOT/proof).read_bytes()).hexdigest() == proof_hash
assert sha256((ROOT/'work/part_a/f_centralizer_audit.tex').read_bytes()).hexdigest() == f7_hash
record = {'status': 'REGISTERED_REVIEWED_F30', 'proof_sha256': proof_hash,
          'earlier_f7_proof_unchanged': True, 'f7_sha256': f7_hash,
          'changes': changes, 'new_claims': ['F.30'],
          'preserved_608_page_pdf': str(baseline.relative_to(ROOT))}
(ROOT/'work/root/integration_269_source_changes.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'changed_files': len(changes),
                  'new_claims': ['F.30'], 'proofs_unchanged': True}, indent=2))
