#!/usr/bin/env python3
"""Register the fully reviewed C92, F27 and F28 without editing their proofs."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]
changes=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def edit(name,func):
 p=ROOT/name;old=p.read_bytes();new=func(old.decode()).encode();assert old!=new,name
 p.write_bytes(new);changes.append({'path':name,'old_sha256':sha(old),'new_sha256':sha(new)})
def once(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
proofs={'work/part_c/c92.tex':'e978d4c54fa14090d67e1fd0620561bd251a8e3673132284aa144030b129ad7c',
 'work/part_a/f_product_one_character_locus_images.tex':'91dbd2e919ebda809dcfaa61f05d2ee465ef67739252b34991fb29fc44c9d21f',
 'work/part_a/f_three_parameter_product_one_images.tex':'b9e5941bddeb92cc831825c067bc1ff8c6e8b952f35eb608cf02c142dae26262'}
for p,h in proofs.items():assert sha((ROOT/p).read_bytes())==h,p
def assembly(s):
 for a,b in [
  (" 'work/part_c/c91.tex',"," 'work/part_c/c91.tex',\n 'work/part_c/c92.tex',"),
  (" 'work/part_a/f_trace_obstruction_and_f9_images.tex']"," 'work/part_a/f_trace_obstruction_and_f9_images.tex',\n 'work/part_a/f_product_one_character_locus_images.tex',\n 'work/part_a/f_three_parameter_product_one_images.tex']"),
  (" 'work/part_c/c91_result.json',"," 'work/part_c/c91_result.json',\n 'work/part_c/c92_result.json',"),
  (" 'work/part_a/f_trace_obstruction_and_f9_images_results.json']"," 'work/part_a/f_trace_obstruction_and_f9_images_results.json',\n 'work/part_a/f_product_one_character_locus_images_results.json',\n 'work/part_a/f_three_parameter_product_one_images_results.json']"),
  (" 'work/part_d_attack/pants_lift_new_references.bib']"," 'work/part_d_attack/pants_lift_new_references.bib',\n 'work/root/noncompact_uniform_source_followup_references.bib']")]:s=once(s,a,b)
 return s
edit('work/root/assemble.py',assembly)
c_add=r'''C.92 proves that every element of the entire original point stabilizer descends into the pointed identity path component for an arbitrary actual quotient. A locally finite based homotopy and the precise orientation comparison meet Epstein's based isotopy theorem. The unique point-fixed lift gives the exact subgroup whose actual lift displacement belongs to $C_0(N)$, with an isometric comparison to the original topology and the exact compact-family uniform-tail criterion. An explicit radial-disk sequence converges downstairs in the compact-open topology while its unique pointed lifts stay more than $2/5$ from the identity. A noncompact deformation with that uniform tail and the general frontier comparisons remain unresolved.
'''
f_add=r'''F.27 proves the exact trace rank and affine marginal image equality over every finite coefficient field on the actual two-parameter character locus $(1,s,t,1,1,1,(st)^{-1})$. Its integer Laurent commutators force an essential source line, and actual character-one seed conjugates give an invertible Frobenius Vandermonde comparison. F.28 extends this to the three-parameter locus $(r,s,t,1,1,1,(rst)^{-1})$: an explicit two-dimensional invariant inclusion and four quotient coordinates separate all minimal source submodules across distinct Frobenius factors. The individual restriction theorem then proves summed restriction injective and rank $6m+1$. Both results retain the exact based sign map and include larger original coefficient fields. The general scalar-character locus, full marginal equalities, interaction source image and original residual membership remain unresolved.
'''
def add_to_claim(s,cid,addition):
 pattern=r'(\\begin\{claim\}\{'+re.escape(cid)+r'\}.*?)(\\end\{claim\})'
 m=re.search(pattern,s,re.S);assert m
 return s[:m.start()]+m.group(1)+addition+m.group(2)+s[m.end():]
edit('work/part_c/c.tex',lambda s:add_to_claim(s,'C.12',c_add))
edit('work/part_a/f_centralizer_audit.tex',lambda s:add_to_claim(s,'F.7',f_add))
def add_note(s,cid,note):
 obj=json.loads(s);rows=[obj] if isinstance(obj,dict) else obj
 matches=[r for r in rows if r['id']==cid];assert len(matches)==1
 matches[0]['notes']+=' '+note
 return json.dumps(obj,indent=2,ensure_ascii=False)+'\n'
c_note='C92 proves arbitrary actual pointed descent into the pointed identity path component, the unique lift and its compact-open continuity, the exact C0 image and lifted isometry, and the precise compact-family uniform tail. An explicit original radial-disk sequence has downstairs compact-open convergence but pointed-lift distance greater than2/5. A controlled noncompact deformation and general frontier comparisons remain unresolved.'
f_note='F27 proves all-field affine marginal image equality on the precise two-parameter product-one locus by an essential-line Laurent determinant and actual Vandermonde evaluations. F28 proves the larger three-parameter locus via an explicit two-dimensional invariant subspace and four quotient coordinates: exact source scalars exclude all cross-factor minimal-submodule intertwiners, and F24 individual injection gives summed rank6m+1. Both retain the original scalar character, original based sign maps and larger coefficient fields. The general character locus, full marginal equality, interaction source image and original residual equation remain unresolved.'
edit('work/part_c/results.json',lambda s:add_note(s,'C.12',c_note))
edit('work/part_a/f_centralizer_audit_results.json',lambda s:add_note(s,'F.7',f_note))
edit('work/root/pdf_qa.py',lambda s:once(once(s,"'C.90.', 'C.91.'","'C.90.', 'C.91.', 'C.92.'"),"'F.25.', 'F.26.'","'F.25.', 'F.26.', 'F.27.', 'F.28.'"))
def report(s):
 old="rows=[(label, current_264[label][0], current_264[label][1])\n      if label in current_264 else (label, references, state)"
 new="current_267 = dict(current_264)\n"
 new+="for _key in ['Item 5', 'C.b']:\n    _refs, _state = current_267[_key]\n    current_267[_key] = (_refs.replace('C.91', 'C.92'), _state + "+repr(' '+c_note)+")\n"
 new+="for _key in ['Lead 3', 'F.b']:\n    _refs, _state = current_267[_key]\n    current_267[_key] = (_refs.replace('F.26', 'F.28'), _state + "+repr(' '+f_note)+")\n"
 d_note=' The folded actual map is injective on every original cusp normalizer and identifies its image normalizer exactly. Its crossed difference from the free-basis map takes values in the specified normal closure N_f, with F0=tau(F)N_f, and a displayed fiber-product surjection describes all labelled maps. An exact full-to-pro-2 coproduct map and its odd-prime kernel settle the cited source wording. Every actual finite transitive action satisfies the proved fixed-point inequality S<=n+2; a complete S5 computation excludes nine parameter values through the original third cusp. Full generation, standard-cusp alignment and D74.40 remain unresolved.'
 new+="_refs, _state = current_267['D.b']\ncurrent_267['D.b'] = (_refs, _state + "+repr(d_note)+")\n"
 new+="rows=[(label, current_267[label][0], current_267[label][1])\n      if label in current_267 else (label, references, state)"
 s=once(s,old,new)
 anchor="add_report('work/root/research_update_264.md')"
 additions=[
  ('work/root/research_update_267.md',None),
  ('work/part_c/c92_report.txt','Arbitrary actual pointed descents and exact original lift topology'),
  ('work/part_a/f_product_one_character_locus_images_report.txt','All-field affine images on the exact two-parameter locus'),
  ('work/part_a/f_three_parameter_product_one_images_report.txt','All-field affine images on the exact three-parameter locus'),
  ('work/part_d_attack/tau_original_cusp_followup.txt','Actual folded map, original cusp normalizers and exact image comparison'),
  ('work/part_d_attack/wilkes_6_9_literal_coproduct_comparison.txt','Literal full and pro-two coproduct comparison'),
  ('work/part_d_attack/actual_finite_quotient_generation_constraints.txt','Actual finite quotient inequality and original third-cusp exclusions'),
  ('work/root/noncompact_uniform_source_followup_264.txt','Exact noncompact metric and source-hypothesis comparison')]
 lines=[anchor]+['add_report('+repr(p)+((',title='+repr(t)) if t else '')+')' for p,t in additions]
 return once(s,anchor,'\n'.join(lines))
edit('work/root/make_report.py',report)
def package(s):
 s=once(s,'checkpoint_264_extra_paths.json','checkpoint_267_extra_paths.json')
 start=s.index("f26_manifest=ROOT/")
 end=s.index('for name in sorted(inputs):',start)
 block=s[start:end]
 blocks=[]
 for n,stem in [(27,'f_product_one_character_locus_images'),(28,'f_three_parameter_product_one_images')]:
  blocks.append(block.replace('f26_',f'f{n}_').replace('F26',f'F{n}').replace('f_trace_obstruction_and_f9_images',stem))
 s=s[:end]+''.join(blocks)+s[end:]
 start=s.index('for entry in f26_routes:')
 end=s.index('required = json.loads',start)
 block=s[start:end]
 return s[:end]+''.join(block.replace('f26_',f'f{n}_').replace('F26',f'F{n}') for n in [27,28])+s[end:]
edit('work/root/package_deliverable.py',package)
for p,h in proofs.items():assert sha((ROOT/p).read_bytes())==h,p
(ROOT/'work/root/integration_267_source_changes.json').write_text(json.dumps({'status':'REGISTERED_REVIEWED_PROOFS','proofs_unchanged':proofs,'changes':changes},indent=2)+'\n')
print(json.dumps({'status':'PASS','changed_files':len(changes),'new_claims':['C.92','F.27','F.28'],'proofs_unchanged':True}))
