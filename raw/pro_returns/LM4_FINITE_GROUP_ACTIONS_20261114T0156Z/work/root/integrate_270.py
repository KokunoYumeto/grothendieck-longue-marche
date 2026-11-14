#!/usr/bin/env python3
"""Register F31 and accepted continuations without changing frozen proofs."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[2]
proof = 'work/part_a/f_full_product_one_affine_images.tex'
proof_hash = '909cb42466354ecebfede5b5d27077381d13e87f9261ea62180dc507cf91c345'
assert sha256((ROOT/proof).read_bytes()).hexdigest() == proof_hash
gate = json.loads((ROOT/'work/root/final_new_claim_acceptance_270.json').read_text())
assert gate['status'] == 'PASS_ROOT_AND_PEER' and gate['proof_sha256'] == proof_hash
baseline = ROOT/'work/root/prior_269_snapshot/paper.pdf'
assert sha256(baseline.read_bytes()).hexdigest() == '6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
for name in ['actual_class_two_acceptance_270.json','filled_carriers_acceptance_270.json']:
    assert json.loads((ROOT/'work/root'/name).read_text())['status'] == 'PASS_ROOT_AND_PEER'
f7 = ROOT/'work/part_a/f_centralizer_audit.tex'
f7_hash = sha256(f7.read_bytes()).hexdigest()
changes = []

def once(s,old,new):
    assert s.count(old) == 1, (old,s.count(old))
    return s.replace(old,new,1)

def edit(name,operation):
    p=ROOT/name
    old=p.read_bytes();new=operation(old.decode()).encode()
    assert new != old,name
    p.write_bytes(new)
    changes.append({'path':name,'old_sha256':sha256(old).hexdigest(),
                    'new_sha256':sha256(new).hexdigest()})

def assembly(s):
    s=once(s," 'work/part_a/f_product_one_first_scalar_field_images.tex']",
             " 'work/part_a/f_product_one_first_scalar_field_images.tex',\n 'work/part_a/f_full_product_one_affine_images.tex']")
    return once(s," 'work/part_a/f_product_one_first_scalar_field_images_results.json']",
                 " 'work/part_a/f_product_one_first_scalar_field_images_results.json',\n 'work/part_a/f_full_product_one_affine_images_results.json']")
edit('work/root/assemble.py',assembly)
edit('work/root/pdf_qa.py',lambda s:once(s,"'F.29.', 'F.30.'","'F.29.', 'F.30.', 'F.31.'"))

f_note = ('F31 proves the full product-one affine marginal theorem without the first-scalar field-generation restriction. '
          'The actual fields are k1=F_p(u,v,w,c), k0=k1(r,t), c=rstuvw. '
          'The r!=1 chart uses the exact fixed field of the Frobenius difference, eight moving rows and four determinants; '
          'the r=1 chart uses a four-dimensional boundary/X1 kernel, a unit row determinant and every one of the fifteen nontrivial sign strata. '
          'All minimal-type comparisons, the exact principal tuple kernel and rank6m+1 are proved. '
          'The actual coefficient and based sign maps cover every original finite field and both signs. '
          'The remaining affine target has chi(P0)!=1; full marginal equality and the original interaction comparison remain unresolved.')
c_note = (' The independently accepted filled-carrier note proves both original metric comparisons, equivariant filling with exact diameter equality, '
          'and a specified finite fixed-region expansion with explicit inverse and both forward/inverse displacement bounds. '
          'It also constructs an actual radial loop with a based nullhomotopy and proves the exact failure of correction by one disjoint-disk paste. '
          'The initial common fixed region, compatible edge/cycle stages and controlled infinite composition remain to be constructed.')
d_note = (' The independently accepted class-two note gives both inverse full quotient coordinate maps and the actual GT0 order-three extension automorphism. '
          'Its unique original endpoint transporters give D(k)=x^k omega^2(h)^-1 z^k omega(h)^-1 y^k h^-1, '
          'd=-3t and the exact class-two locus mu^2=1-24t. The prime-coordinate homeomorphism and explicit lifting maps give roots at 2 and 3. '
          'All-prime nonemptiness and a zero of the full original word remain unresolved.')

def report(s):
    old=('rows=[(label, current_269[label][0], current_269[label][1])\n'
         '      if label in current_269 else (label, references, state)')
    new='current_270 = dict(current_269)\n'
    new+="for _key in ['Lead 3', 'F.b']:\n    _refs, _state = current_270[_key]\n"
    obsolete='General product-one characters without the field-generation equality, full marginal equality and the original interaction comparison remain unresolved.'
    new+='    assert _state.count('+repr(obsolete)+') == 1\n'
    new+="    current_270[_key] = (_refs.replace('F.30', 'F.31'), _state.replace("+repr(obsolete)+', '+repr(f_note)+', 1))\n'
    new+="for _key in ['Item 5', 'C.b']:\n    _refs, _state = current_270[_key]\n"
    new+='    current_270[_key] = (_refs, _state + '+repr(c_note)+')\n'
    new+="_refs, _state = current_270['D.b']\ncurrent_270['D.b'] = (_refs, _state + "+repr(d_note)+')\n'
    new+=('rows=[(label, current_270[label][0], current_270[label][1])\n'
          '      if label in current_270 else (label, references, state)')
    s=once(s,old,new)
    anchor="add_report('work/root/research_update_269.md')"
    addition="\nadd_report('work/root/research_update_270.md')"
    addition+="\nadd_report('work/part_a/f_full_product_one_affine_images_report.txt',title='Full product-one finite affine marginal images')"
    addition+="\nadd_report('work/part_d_attack/actual_transporter_class_two_and_gt0.txt',title='Actual full class-two coordinates and cyclic GT0 transporters')"
    addition+="\nadd_report('work/part_c/compact_family_filled_carriers_and_expansions_report.txt',title='Actual filled carriers and finite controlled fixed-region expansions')"
    return once(s,anchor,anchor+addition)
edit('work/root/make_report.py',report)

def package(s):
    s=once(s,'checkpoint_269_extra_paths.json','checkpoint_270_extra_paths.json')
    anchor="# Retain every mathematical program, exact output and finite presentation cache.\nfor part in ['part_a', 'part_b', 'part_c']:"
    s=once(s,anchor,anchor[:-2]+", 'part_d_attack']:")
    start=s.index('f30_manifest=ROOT/')
    end=s.index('for name in sorted(inputs):',start)
    block=s[start:end].replace('f30_','f31_').replace('F30','F31').replace(
        'f_product_one_first_scalar_field_images','f_full_product_one_affine_images')
    s=s[:end]+block+s[end:]
    start=s.index('for entry in f30_routes:')
    end=s.index('required = json.loads',start)
    block=s[start:end].replace('f30_','f31_').replace('F30','F31')
    s=s[:end]+block+s[end:]
    old=('`code/part_a`, `code/part_b`, `code/part_c`, and `code/root` contain the\n'
         'main mathematical programs and their captured outputs. The original\n'
         'transporter and finite-generation continuations are retained under\n'
         '`work/part_d_attack/code`; isolated independent replays are retained in their\n')
    new=('`code/part_a`, `code/part_b`, `code/part_c`, `code/part_d_attack`, and\n'
         '`code/root` contain the mathematical programs and their captured outputs.\n'
         'Selected original `work/part_d_attack/code` paths are also retained so the\n'
         'frozen review bindings remain literal. Isolated independent replays retain their\n')
    return once(s,old,new)
edit('work/root/package_deliverable.py',package)
assert sha256((ROOT/proof).read_bytes()).hexdigest() == proof_hash
assert sha256(f7.read_bytes()).hexdigest() == f7_hash
record={'status':'REGISTERED_REVIEWED_F31_AND_ACCEPTED_CONTINUATIONS',
        'new_claims':['F.31'],'proof_sha256':proof_hash,
        'earlier_f7_proof_unchanged':True,'f7_sha256':f7_hash,
        'changes':changes,'preserved_611_page_pdf':str(baseline.relative_to(ROOT)),
        'part_d_code_copied_to_code_directory':True}
(ROOT/'work/root/integration_270_source_changes.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','changed_files':len(changes),'new_claims':['F.31']},indent=2))
