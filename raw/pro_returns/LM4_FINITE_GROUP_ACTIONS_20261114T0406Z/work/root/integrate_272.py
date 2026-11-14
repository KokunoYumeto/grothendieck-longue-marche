#!/usr/bin/env python3
"""Register reviewed F33 and the accepted post271 continuations."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
proof='work/part_a/f_quadratic_sign_pair_restriction.tex'
proof_hash='8a2cd87d9139c6e2bccd99cc9bb8db53883d064da5653fd804e2e2457ab96037'
assert sha256((ROOT/proof).read_bytes()).hexdigest()==proof_hash
gate=json.loads((ROOT/'work/root/final_new_claim_acceptance_272.json').read_text())
assert gate['status']=='PASS_ROOT_AND_PEER' and gate['proof_sha256']==proof_hash
baseline=ROOT/'work/root/prior_271_snapshot/paper.pdf'
assert sha256(baseline.read_bytes()).hexdigest()=='9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
accepted=[
 'orbit_track_component_continuation_acceptance.json',
 'order_three_candidate_continuation_acceptance.json',
 'four_order_three_continuation_acceptance.json',
 'cyclic_carrier_continuation_acceptance.json',
 'hr_minus_one_uw_one_continuation_acceptance.json',
 'haran_c2_c3_continuation_acceptance.json',
 'disjoint_trace_carrier_continuation_acceptance.json',
 'canonical_transporter_continuation_acceptance.json',
 'finite_overlap_carrier_continuation_acceptance.json']
for name in accepted:
    assert json.loads((ROOT/'work/root'/name).read_text())['status'].startswith('ACCEPTED_'),name
bib='work/part_d_attack/haran_closed_subgroups_1987_reference.bib'
assert sha256((ROOT/bib).read_bytes()).hexdigest()=='8abd868b76f5423855f9b9d1de99a4777eddb5dbc834dc7435f9e7ae1bdcdf9f'
changes=[]
def once(s,old,new):
    assert s.count(old)==1,(old,s.count(old));return s.replace(old,new,1)
def edit(name,operation):
    p=ROOT/name;old=p.read_bytes();new=operation(old.decode()).encode()
    assert old!=new,name;p.write_bytes(new)
    changes.append({'path':name,'old_sha256':sha256(old).hexdigest(),'new_sha256':sha256(new).hexdigest()})
def assembly(s):
    s=once(s," 'work/part_a/f_nonproduct_first_character_one_images.tex']",
             " 'work/part_a/f_nonproduct_first_character_one_images.tex',\n 'work/part_a/f_quadratic_sign_pair_restriction.tex']")
    s=once(s," 'work/part_a/f_nonproduct_first_character_one_images_results.json']",
             " 'work/part_a/f_nonproduct_first_character_one_images_results.json',\n 'work/part_a/f_quadratic_sign_pair_restriction_results.json']")
    return once(s," 'work/part_d_attack/zalesskii_2024_prosoluble_reference.bib']",
                  " 'work/part_d_attack/zalesskii_2024_prosoluble_reference.bib',\n '"+bib+"']")
edit('work/root/assemble.py',assembly)
edit('work/root/pdf_qa.py',lambda s:once(s,"'F.31.', 'F.32.'","'F.31.', 'F.32.', 'F.33.'"))

f_new=(' F33 proves the exact opposite-first-character summed restriction kernel over every finite odd-characteristic field: '
       'the kernel is precisely the paired principal line, with original cochain rank13 and injective summed H1 restriction. '
       'The explicit64x13 matrix has rank13 over every field, and the pair theorem includes r^2=1. '
       'All64 rows are reconstructed from the nineteen actual negative braids and transported by the original based positive-sign maps. '
       'The independent252309-check original-word replays,32427-check root row audit,77-check actual-TeX audit and27737-check peer audit pass. '
       'The general nonproduct many-factor source comparisons and their complete literal-word certification remain in progress; the full marginal and interaction targets remain unresolved.')
c_new=(' The accepted post271 constructions give the actual small orbit track and relative component witness, '
       'cyclic annulus/Mobius carrier corrections, and disjoint-trace corrections bounded independently of the subdivision count. '
       'For arbitrary actual overlaps they identify the finite set S, the subgroup H=<S>, every component qHA, the quotient HA/H=pi(A), '
       'the exact equality S(Fill A)=S(A), and the section of O/H->O/Q over the original small-tile image. '
       'The resulting finite correction retains B=n diam_eQ(D1) and the original inverse modulus. '
       'An actual radial-cylinder family has trace radii tending to zero and saturated component diameter2. '
       'A general vanishing ambient tail bound, compatible edge/cycle stages and infinite deformation remain unresolved.')
d_new=(' The accepted post271 order-three construction lists all four actual j-inverted candidates with separate source maps and exact cusp defects. '
       'The canonical conjugators a,L are unique in the original F; they give k=3chi_x(L), nu0=2k+1 and an actual A. '
       'The exact continuous map R(k) is z^(-(k+1)/2) on the odd component and g^-1 z^(-k/2) on the even component, with inverse Sigma(A)-1. '
       'The original transporter set is exactly {nu in {nu0,-nu0}: nu0 is a full unit and A=R(k)}, with all four inverse candidate maps retained. '
       'Both full-unit and full cusp-membership conclusions remain unproved. '
       'The actual common order-three image is either all C2 coproduct C3 or has infinite index. '
       'The checked Haran comparison preserves the local-image scope of relative projectivity and supplies explicit proper-image maps; it does not identify them with that original common image.')
def report(s):
    old=('rows=[(label, current_271[label][0], current_271[label][1])\n'
         '      if label in current_271 else (label, references, state)')
    new='current_272 = dict(current_271)\n'
    new+="for _key in ['Lead 3', 'F.b']:\n    _refs, _state = current_272[_key]\n"
    new+="    current_272[_key] = (_refs.replace('F.32', 'F.33'), _state + "+repr(f_new)+')\n'
    new+="for _key in ['Item 5', 'C.b']:\n    _refs, _state = current_272[_key]\n"
    new+='    current_272[_key] = (_refs, _state + '+repr(c_new)+')\n'
    new+="_refs, _state = current_272['D.b']\ncurrent_272['D.b'] = (_refs, _state + "+repr(d_new)+')\n'
    new+=('rows=[(label, current_272[label][0], current_272[label][1])\n'
          '      if label in current_272 else (label, references, state)')
    s=once(s,old,new)
    reports=[
     ('work/root/research_update_272.md',None),
     ('work/part_a/f_quadratic_sign_pair_restriction_report.txt','Exact opposite-first-character paired restriction kernel'),
     ('work/root/review_f33.txt','Root mathematical audit of F33'),
     ('work/part_c/review_f33.txt','Independent F33 audit and exact preservation-count correction'),
     ('work/root/review_compact_family_finite_overlap_carriers.txt','Accepted actual finite overlap carriers and retained quantitative bound')]
    anchor="add_report('work/root/research_update_271.md')"
    added=''
    for name,title in reports:
        added+='\nadd_report('+repr(name)+((',title='+repr(title)) if title else '')+')'
    return once(s,anchor,anchor+added)
edit('work/root/make_report.py',report)
def package(s):
    s=once(s,'checkpoint_271_extra_paths.json','checkpoint_272_extra_paths.json')
    start=s.index('f32_manifest=ROOT/');end=s.index('for name in sorted(inputs):',start)
    block=s[start:end].replace('f32_','f33_').replace('F32','F33').replace(
        'f_nonproduct_first_character_one_images','f_quadratic_sign_pair_restriction')
    s=s[:end]+block+s[end:]
    start=s.index('for entry in f32_routes:');end=s.index('required = json.loads',start)
    block=s[start:end].replace('f32_','f33_').replace('F32','F33')
    return s[:end]+block+s[end:]
edit('work/root/package_deliverable.py',package)
assert sha256((ROOT/proof).read_bytes()).hexdigest()==proof_hash
record={'status':'REGISTERED_REVIEWED_F33_AND_ACCEPTED_CONTINUATIONS',
        'new_claims':['F.33'],'proof_sha256':proof_hash,'accepted_continuations':accepted,
        'verified_bibliography_addition':bib,'changes':changes,
        'preserved_625_page_pdf':str(baseline.relative_to(ROOT))}
(ROOT/'work/root/integration_272_source_changes.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','changed_files':len(changes),'new_claims':['F.33'],
                  'accepted_continuations':len(accepted)},indent=2))
