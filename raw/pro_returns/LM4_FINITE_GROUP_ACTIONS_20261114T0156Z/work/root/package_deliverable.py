#!/usr/bin/env python3
"""Package the exact paper, registries, computations and reproducible inputs.

The package retains the INCOMPLETE marker while any obligation remains open.
It never assigns mathematical status from a successful build or computation.
"""
from pathlib import Path
import ast, csv, hashlib, json, shutil, subprocess, sys, zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
PREFIX = 'LM4_FINITE_GROUP_ACTIONS'
STAGE = ROOT / 'work' / 'package_staging'
MARKER = STAGE / '.lm4_package_owned'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def copy(source, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)

# A PDF inspection certifies one exact byte sequence, not an earlier build.
assembly=json.loads((OUT/'assembly_check.json').read_text())
for name,expected in assembly.get('source_input_sha256',{}).items():
    if sha(ROOT/name)!=expected:
        raise RuntimeError('Assembly input changed after assembly: '+name)
pdf_hash = sha(OUT / (PREFIX + '_paper.pdf'))
build = json.loads((OUT/'build_artifact.json').read_text())
if not build['success'] or build['pdf_sha256'] != pdf_hash:
    raise RuntimeError('The current PDF has no successful matching build')
for name, expected in build['source_sha256'].items():
    if sha(OUT/name) != expected:
        raise RuntimeError('Source changed after the PDF build: '+name)
for name in ['pdf_qa.json', 'render_review.json']:
    review = json.loads((OUT / name).read_text())
    if review.get('sha256') != pdf_hash:
        raise RuntimeError('Stale or missing exact-PDF review: ' + name)
if json.loads((OUT / 'pdf_qa.json').read_text())['overfull_greater_than_2pt']:
    raise RuntimeError('The current PDF has an overfull box exceeding 2pt')

if STAGE.exists():
    if not MARKER.exists():
        raise RuntimeError('Refusing to replace an unmarked staging directory')
    shutil.rmtree(STAGE)
STAGE.mkdir(parents=True)
MARKER.write_text('Private staging directory owned by package_deliverable.py\n')

# Retain every mathematical program, exact output and finite presentation cache.
for part in ['part_a', 'part_b', 'part_c', 'part_d_attack']:
    for p in sorted((ROOT / 'work' / part / 'code').rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
            copy(p, STAGE / 'code' / part / p.relative_to(ROOT / 'work' / part / 'code'))
for name in ['catalogue_higher_genus.py', 'finite_checks.py', 'finite_checks.json',
             'finite_checks_stdout.txt', 'higher_genus_stdout.txt',
             'haran_pair_counts.py', 'haran_pair_counts_output.json',
             'haran_pair_counts_stdout.txt']:
    copy(ROOT / 'work' / 'root' / name, STAGE / 'code' / 'root' / name)
for folder in ['research_data', 'higher_genus_output']:
    shutil.copytree(ROOT / 'work' / 'root' / folder, STAGE / 'code' / 'root' / folder)

# The active source fragments and metadata suffice to reproduce the assembly.
tree = ast.parse((ROOT / 'work' / 'root' / 'assemble.py').read_text())
inputs = set()
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in
                                          ['FRAGMENTS', 'METADATA', 'BIBS'] for t in node.targets):
        inputs.update(ast.literal_eval(node.value))
inputs.add('work/root/prelude.tex')
for part in ['part_a', 'part_b', 'part_c', 'root']:
    p = ROOT / 'work' / part / 'readings.json'
    if p.exists(): inputs.add(str(p.relative_to(ROOT)))
inputs.add('work/part_c/b_extra_readings.json')
for name in ['assemble.py', 'build_pdf.py', 'make_report.py', 'pdf_qa.py',
             'package_deliverable.py']:
    inputs.add('work/root/' + name)
for part in ['part_a', 'part_b', 'part_c']:
    for p in (ROOT / 'work' / part).glob('*report*.md'):
        inputs.add(str(p.relative_to(ROOT)))
for optional in ['work/root/render_preparation_541.json', 'work/root/render_preparation_541_supplement.json', 'work/root/render_review_541.json', 'work/part_c/render_review_541.json', 'work/root/pdf_qa_252_stdout.json', 'work/root/research_update_252.md', 'work/root/review_c84.txt', 'work/root/review_f22.txt', 'work/root/c84_independent_audit_stdout.txt', 'work/root/f22_independent_audit_stdout.txt', 'work/part_c/review_c84.txt', 'work/part_c/review_f22.txt', 'work/part_c/c84_radial_monotone_audit_stdout.txt', 'work/part_c/f22_joint_kernel_audit_stdout.txt', 'work/part_a/f_joint_kernel_presentation_report.txt', 'work/part_b/discrete_q_controlled_lifting_continuation.txt', 'work/part_c/d_recognition_followup_250.txt', 'work/root/fabel_operator_label_source_audit.txt', 'work/root/f22_typesetting_repair.json', 'work/root/build_252_initial_hat_error.log', 'work/root/assemble_252_stdout.json', 'work/root/build_252_final_stdout.txt', 'work/root/render_preparation_534.json', 'work/root/render_preparation_534_final.json', 'work/root/root_visual_review_534_initial.json', 'work/root/render_review_534.json', 'work/part_c/render_review_534.json', 'work/root/f21_typesetting_repair.json', 'work/root/overflow_250_initial.json', 'work/root/build_250_initial_overflow.log', 'work/root/build_250_final_stdout.txt', 'work/root/build_250_typography_stdout.txt', 'work/root/assemble_250_stdout.json', 'work/root/pdf_qa_250_final_stdout.json', 'work/root/research_update_250.md', 'work/root/review_c83.txt', 'work/root/review_f21.txt', 'work/root/c83_independent_audit_stdout.txt', 'work/root/f21_independent_audit_stdout.txt', 'work/root/teh_preprints_independent_audit.txt', 'work/root/teh_configuration_audit_stdout.txt', 'work/part_c/review_c83.txt', 'work/part_c/review_f21.txt', 'work/part_c/c83_evaluation_path_audit_stdout.txt', 'work/part_c/f21_symbolic_audit_stdout.txt', 'work/part_c/d_recognition_recheck_250.txt', 'work/part_b/teh_preprints_source_audit.txt', 'work/part_a/f_cross_divisor_transitivity_report.txt', 'work/root/render_preparation_525.json', 'work/root/render_preparation_525_final.json', 'work/root/render_review_525.json', 'work/part_c/render_review_525.json', 'work/root/build_248_typography_stdout.txt', 'work/root/assemble_248_stdout.json', 'work/root/pdf_qa_248_typography_stdout.json', 'work/root/research_update_248.md', 'work/root/review_c81.txt', 'work/root/review_c82.txt', 'work/root/review_d77.txt', 'work/root/review_f20.txt', 'work/root/f20_radial_cross_product_check.json', 'work/root/pants_incidence_limit_audit_stdout.txt', 'work/part_c/review_c81.txt', 'work/part_c/review_c82.txt', 'work/part_b/review_d77.txt', 'work/part_b/d77_independent_rerun_stdout.txt', 'work/part_c/d77_report.txt', 'work/part_c/pants_incidence_limit.txt', 'work/part_c/negative_fixed_group_pd1_limit.txt', 'work/part_a/f_cross_divisor_monodromy_report.txt', 'work/part_b/review_f19_relative_tracks_exact.txt', 'work/part_b/review_f20_finite.txt', 'work/part_b/f20_finite_independent_rerun_stdout.txt', 'work/part_b/f20_finite_independent_audit_summary.json', 'work/part_c/review_f20.txt', 'work/part_c/f20_monodromy_audit_stdout.txt', 'work/part_c/f20_finite_audit_stdout.txt', 'work/root/render_preparation_508.json', 'work/part_c/render_review_508.json', 'work/root/review_c76_c77.txt', 'work/root/review_c78.txt', 'work/root/review_c79.txt', 'work/root/review_c80.txt', 'work/root/review_d76.txt', 'work/root/research_update_244.md', 'work/root/post_238_research_log.md', 'work/part_c/review_c76.txt', 'work/part_c/review_c77.txt', 'work/part_a/review_c76.md', 'work/part_a/review_c78.md', 'work/part_a/review_c79.md', 'work/part_a/review_c80.md', 'work/part_b/review_d76.txt', 'work/part_c/d76_report.txt', 'work/root/review_c73_d73.txt', 'work/root/review_c74_c75_f19.txt', 'work/root/review_d74.txt', 'work/root/review_d75.txt', 'work/root/research_update_238.md', 'work/part_c/review_c73.txt', 'work/part_a/review_c74.md', 'work/part_a/c74_audit_stdout.txt', 'work/part_c/review_c74.txt', 'work/part_c/c74_principal_interpolation_audit_stdout.txt', 'work/part_a/review_c75.md', 'work/part_a/review_d73.md', 'work/part_a/d73_audit_stdout.txt', 'work/part_a/review_pants_twisted_duality.md', 'work/part_a/review_d75.md', 'work/part_b/review_f19.txt', 'work/part_c/d73_report.txt', 'work/part_c/d74_report.txt', 'work/part_c/d75_report.txt', 'work/part_a/f_cross_diagonal_kernel_report.txt', 'work/root/review_c71_c72_d71_f17_f18.txt', 'work/root/research_update_231.md', 'work/part_a/review_c71.md', 'work/part_a/c71_audit_stdout.txt', 'work/part_c/review_c72.txt', 'work/part_c/c72_spiral_comparison_audit_stdout.txt', 'work/part_b/review_d71.txt', 'work/part_c/review_d72.txt', 'work/part_c/pants_cochains_d72_audit_stdout.txt', 'work/part_c/review_f17.txt', 'work/part_c/common_reflection_drilling_f17_audit_stdout.txt', 'work/part_b/review_f18.txt', 'work/part_a/f_branch_drilling_report.txt', 'work/part_a/f_unique_branch_lift_report.txt', 'work/root/review_c68_d69.txt', 'work/root/review_d70_c69_f16.txt', 'work/root/research_update_225.md', 'work/part_c/review_c68.txt', 'work/part_c/review_c69.txt', 'work/part_b/review_c70.txt', 'work/part_a/review_d69.md', 'work/part_a/d69_audit_stdout.txt', 'work/part_a/review_d70.md', 'work/part_b/review_f16.txt', 'work/part_a/f_forgetting_ambiguity_report.txt', 'work/root/review_c67_d68.txt', 'work/root/review_f15.txt', 'work/root/research_update_219.md', 'work/part_c/review_c67.txt', 'work/part_a/review_d68.md', 'work/part_a/d68_audit_stdout.txt', 'work/part_b/review_j_section_comparison.md', 'work/part_a/f_two_point_cocycle_report.txt', 'work/root/review_c66_f13.txt', 'work/root/review_f14.txt', 'work/root/research_update_216.md', 'work/part_a/review_c66.md', 'work/part_c/review_c66.txt', 'work/part_c/review_f12_retraction.txt', 'work/part_c/common_reflection_retraction_audit_stdout.txt', 'work/part_c/review_f14.txt', 'work/part_c/common_reflection_forgetting_f14_audit_stdout.txt', 'work/root/review_c65_d67.txt', 'work/root/review_d66_f12.txt', 'work/root/research_update_213.md', 'work/part_b/review_c64.txt', 'work/part_a/review_c65.md', 'work/part_c/review_c65.txt', 'work/part_a/review_d66.md', 'work/part_a/d66_audit_stdout.txt', 'work/part_a/review_d67.md', 'work/part_a/d67_audit_stdout.txt', 'work/part_c/review_f12.txt', 'work/part_c/c5_common_reflection_f12_audit_stdout.txt', 'work/part_b/post_c63_frontier_audit.md', 'work/part_b/planar_disk_filling_audit.md', 'work/root/review_c63_f11.txt', 'work/root/review_c5_seven_kernel_code.txt', 'work/part_c/review_c63.txt', 'work/part_c/review_f11.txt', 'work/part_c/review_c5_seven_kernel.txt', 'work/part_c/c5_seven_kernel_audit_stdout.txt', 'work/part_c/c5_centralizer_labels_audit_stdout.txt', 'work/part_b/principal_fiber_word_extension.md', 'work/root/review_c62_d63_d64.txt', 'work/root/review_d65_and_prefix_hulls.txt', 'work/part_c/review_c62.txt', 'work/part_a/review_d63_d64.md', 'work/part_a/d64_audit_stdout.txt', 'work/part_a/review_d65.md', 'work/part_a/d65_audit_stdout.txt', 'work/part_b/prefix_fiber_hull_selection_audit.md', 'work/root/review_c61_d62.txt', 'work/part_c/review_c61.txt', 'work/part_a/review_d62.md', 'work/part_c/d62_unit_addendum.tex', 'work/root/review_modular_cone_parameters_f7.txt', 'work/part_c/review_modular_cone_f7.txt', 'work/part_c/modular_cone_audit_stdout.txt', 'work/part_a/f_modular_cone_parameters.tex', 'work/part_a/f_modular_cone_parameters_results.json', 'work/part_b/prefix_lifting_audit.md', 'work/root/rendered/page244_334_followup.png', 'work/root/review_modular_detector_defect_f7.txt','work/part_c/review_modular_detector_f7.txt','work/part_c/modular_detector_audit_stdout.txt','work/part_a/f_modular_detector_defect.tex','work/part_a/f_modular_detector_defect_results.json', 'work/root/review_c59_c60.txt','work/part_c/review_c59.txt','work/part_c/review_c60.txt','work/root/review_d61.txt','work/part_a/review_d61.md','work/part_a/d61_audit_stdout.txt','work/root/review_modular_c3_correspondence_f7.txt','work/part_c/review_modular_c3_f7.txt','work/part_c/modular_c3_audit_stdout.txt','work/part_a/f_modular_c3_correspondence.tex','work/part_a/f_modular_c3_correspondence_results.json', 'work/root/review_c58.txt', 'work/part_c/review_c58.txt', 'work/part_c/c58_audit_stdout.txt', 'work/root/review_modular_f7.txt', 'work/part_c/review_modular_f7.txt', 'work/part_c/modular_f7_audit_stdout.txt', 'work/part_a/f_modular_gt0_comparison.tex', 'work/part_a/f_modular_gt0_comparison_results.json', 'work/root/review_d60.txt', 'work/part_a/review_d60.md', 'work/part_a/d60_audit_stdout.txt', 'work/part_c/review_c57.txt', 'work/root/review_c54_c57_d59_f10.txt', 'work/part_c/review_c54.txt', 'work/part_b/review_c55.txt', 'work/part_c/review_c55.txt', 'work/part_b/review_c56.txt', 'work/part_b/c56_independent_rerun_stdout.txt', 'work/part_a/review_d59.md', 'work/part_a/d59_audit_stdout.txt', 'work/part_c/review_f10.txt', 'work/part_c/current_rank_obstruction.md', 'work/part_a/f_second_a4_c3_attack.tex', 'work/root/review_c52.txt', 'work/part_c/review_c52.txt', 'work/part_b/review_c53.txt', 'work/part_c/review_c51.txt', 'work/part_c/c50_independent_rerun_stdout.txt', 'work/part_c/f9_independent_rerun_stdout.txt', 'work/root/review_c50_f9.txt', 'work/part_c/review_c50.txt', 'work/part_c/review_f9.txt', 'work/part_a/review_d58.md', 'work/part_a/d58_audit_stdout.txt', 'work/root/review_d58.txt', 'work/part_c/review_c49.txt', 'work/root/review_c49.txt', 'work/root/review_c47_d56_d57.txt', 'work/part_c/review_c47.txt', 'work/part_c/review_c48.txt', 'work/part_c/review_d56.txt', 'work/part_c/review_d57.txt', 'work/root/review_c43_c44_c45.txt', 'work/root/review_d53_d54_d55.txt', 'work/part_a/review_d53.md', 'work/part_a/d53_audit_stdout.txt', 'work/part_a/review_d54_d55.md', 'work/part_a/d54_d55_audit_stdout.txt', 'work/part_c/review_c43_c46.txt', 'work/part_a/pants_recognition_centralizer_audit.md', 'work/part_c/review_c42.txt', 'work/part_c/review_c42_rerun.txt', 'work/part_a/review_d52.md', 'work/part_a/d52_audit_stdout.txt', 'work/root/review_d52.txt', 'work/part_c/d51_incidence_audit.txt', 'work/part_a/a5_cross_refinement_auxiliary.tex', 'work/part_a/a5_cross_refinement_auxiliary_results.json', 'work/part_b/c_scope_audit.md', 'work/part_b/c12_auxiliary_audit.md', 'work/part_c/d22_independent_audit.tex', 'work/part_c/review_c37.txt', 'work/part_c/review_d45.txt', 'work/part_a/review_d43.md', 'work/root/review_c38_d45_d46.txt', 'work/part_c/review_c39.txt', 'work/part_c/review_c40.txt', 'work/part_c/review_c41.txt', 'work/part_c/review_f8.txt', 'work/part_b/review_f8.txt', 'work/root/review_f8_rerun_stdout.txt', 'work/root/research_updates_20261113.md', 'work/part_a/review_d50.md', 'work/part_a/review_d51.md', 'work/root/review_d51.txt', 'work/part_b/review_d50.txt', 'work/part_c/review_d47.txt', 'work/part_c/review_d49.txt', 'work/root/review_d47_rerun_stdout.txt', 'work/root/review_c39_d47_d48_d49.txt']:
    if (ROOT / optional).exists(): inputs.add(optional)
# Exact current continuation evidence and relocatable routes for its source manifest.
for optional in json.loads((ROOT/'work/root/checkpoint_271_extra_paths.json').read_text()):
    if (ROOT/optional).exists(): inputs.add(optional)
f23_manifest=ROOT/'work/part_a/f_source_sign_and_marginal_images_evidence_manifest.json'
f23_routes=[]
if f23_manifest.exists():
    evidence=json.loads(f23_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F23 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f23_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f24_manifest=ROOT/'work/part_a/f_rank_one_marginal_obstruction_evidence_manifest.json'
f24_routes=[]
if f24_manifest.exists():
    evidence=json.loads(f24_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F24 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f24_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f25_manifest=ROOT/'work/part_a/f_affine_scalar_field_images_evidence_manifest.json'
f25_routes=[]
if f25_manifest.exists():
    evidence=json.loads(f25_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F25 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f25_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f26_manifest=ROOT/'work/part_a/f_trace_obstruction_and_f9_images_evidence_manifest.json'
f26_routes=[]
if f26_manifest.exists():
    evidence=json.loads(f26_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F26 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f26_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f27_manifest=ROOT/'work/part_a/f_product_one_character_locus_images_evidence_manifest.json'
f27_routes=[]
if f27_manifest.exists():
    evidence=json.loads(f27_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F27 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f27_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f28_manifest=ROOT/'work/part_a/f_three_parameter_product_one_images_evidence_manifest.json'
f28_routes=[]
if f28_manifest.exists():
    evidence=json.loads(f28_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F28 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f28_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f29_manifest=ROOT/'work/part_a/f_four_parameter_product_one_images_evidence_manifest.json'
f29_routes=[]
if f29_manifest.exists():
    evidence=json.loads(f29_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F29 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f29_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f30_manifest=ROOT/'work/part_a/f_product_one_first_scalar_field_images_evidence_manifest.json'
f30_routes=[]
if f30_manifest.exists():
    evidence=json.loads(f30_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F30 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f30_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f31_manifest=ROOT/'work/part_a/f_full_product_one_affine_images_evidence_manifest.json'
f31_routes=[]
if f31_manifest.exists():
    evidence=json.loads(f31_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F31 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f31_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
f32_manifest=ROOT/'work/part_a/f_nonproduct_first_character_one_images_evidence_manifest.json'
f32_routes=[]
if f32_manifest.exists():
    evidence=json.loads(f32_manifest.read_text())
    for entry in evidence['entries']:
        source=Path(entry['path'])
        if not source.is_absolute(): source=ROOT/source
        if sha(source)!=entry['sha256'] or source.stat().st_size!=entry['bytes']:
            raise RuntimeError('F32 evidence changed after its frozen manifest: '+str(source))
        relative=source.relative_to(ROOT)
        parts=relative.parts
        if len(parts)>3 and parts[0]=='work' and parts[1] in ['part_a','part_b','part_c'] and parts[2]=='code':
            archived=Path('code')/parts[1]/Path(*parts[3:])
        else:
            archived=relative
            inputs.add(str(relative))
        f32_routes.append({'original_path':str(source),'archive_path':str(archived),
                           'bytes':entry['bytes'],'sha256':entry['sha256']})
for name in sorted(inputs):
    if (ROOT / name).exists(): copy(ROOT / name, STAGE / name)

for name in [PREFIX + '_paper.tex', PREFIX + '_paper.pdf', PREFIX + '_references.bib',
             PREFIX + '_results.csv', PREFIX + '_readings.csv', PREFIX + '_report.md']:
    copy(OUT / name, STAGE / name)
for name in ['assembly_check.json', 'build_commands.json', 'build_artifact.json', 'pdf_qa.json', 'render_review.json',
             PREFIX + '_paper.log', PREFIX + '_paper.bbl', PREFIX + '_paper.blg',
             'build_stage_1_stdout.txt', 'build_stage_2_stdout.txt',
             'build_stage_3_stdout.txt', 'build_stage_4_stdout.txt']:
    p = OUT / name
    if p.exists(): copy(p, STAGE / 'verification' / name)
for name in ['build_244_initial_alignment_error.log', 'build_238_initial_alignment_error.log', 'build_213_initial_overflow.log', 'overflow_390_page.json', 'build_208_initial_set_error.log', 'build_200_initial_alignment_error.log', 'build_197_initial_set_error.log', 'build_197_initial_table_error.log', 'build_195_initial_macro_error.log', 'overflow_initial.json', 'overflow_second.json',
             'overflow_204_page.json', 'overflow_261_page.json', 'render_review_211.json', 'render_review_222.json', 'render_review_232.json', 'render_review_238.json', 'render_review_240.json', 'render_review_247.json', 'render_review_261.json', 'render_review_290.json', 'render_review_293.json', 'render_review_300.json', 'render_review_324.json', 'render_review_334.json', 'render_review_345.json', 'render_review_354.json', 'render_review_365.json', 'render_review_374.json', 'render_review_390.json', 'render_review_398.json', 'render_review_409.json', 'render_review_429.json', 'render_review_453.json', 'render_review_483.json', 'render_review_508.json', 'build_initial_success.log', 'build_second_overflow.log']:
    p = ROOT / 'work' / 'root' / name
    if p.exists(): copy(p, STAGE / 'verification' / name)

for entry in f23_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F23 evidence: '+entry['archive_path'])
(STAGE/'verification/f23_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f23_routes},indent=2)+'\n')
for entry in f24_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F24 evidence: '+entry['archive_path'])
(STAGE/'verification/f24_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f24_routes},indent=2)+'\n')

for entry in f25_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F25 evidence: '+entry['archive_path'])
(STAGE/'verification/f25_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f25_routes},indent=2)+'\n')

for entry in f26_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F26 evidence: '+entry['archive_path'])
(STAGE/'verification/f26_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f26_routes},indent=2)+'\n')

for entry in f27_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F27 evidence: '+entry['archive_path'])
(STAGE/'verification/f27_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f27_routes},indent=2)+'\n')

for entry in f28_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F28 evidence: '+entry['archive_path'])
(STAGE/'verification/f28_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f28_routes},indent=2)+'\n')

for entry in f29_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F29 evidence: '+entry['archive_path'])
(STAGE/'verification/f29_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f29_routes},indent=2)+'\n')

for entry in f30_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F30 evidence: '+entry['archive_path'])
(STAGE/'verification/f30_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f30_routes},indent=2)+'\n')

for entry in f31_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F31 evidence: '+entry['archive_path'])
(STAGE/'verification/f31_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f31_routes},indent=2)+'\n')

for entry in f32_routes:
    target=STAGE/entry['archive_path']
    if not target.is_file() or sha(target)!=entry['sha256'] or target.stat().st_size!=entry['bytes']:
        raise RuntimeError('Missing or mismatched archived F32 evidence: '+entry['archive_path'])
(STAGE/'verification/f32_evidence_archive_routes.json').write_text(
    json.dumps({'all_entries_resolve':True,'entries':f32_routes},indent=2)+'\n')

required = json.loads((STAGE / 'code/part_b/low_complexity_catalogue_required_paths.json').read_text())
missing = [p for p in required['required_for_assembler'] if not (STAGE / p).is_file()]
if missing: raise RuntimeError('Missing catalogue inputs: ' + repr(missing))
before = {p: sha(STAGE / p) for p in required['generated_outputs']}
proc = subprocess.run([sys.executable, str(STAGE / 'code/part_b/assemble_low_complexity_catalogues.py')],
                      cwd=STAGE, capture_output=True, text=True)
(STAGE / 'verification' / 'package_catalogue_stdout.txt').write_text(proc.stdout + proc.stderr)
if proc.returncode: raise RuntimeError('Packaged catalogue validation failed')
after = {p: sha(STAGE / p) for p in required['generated_outputs']}
if before != after: raise RuntimeError('Packaged catalogue output changed')

stats = {}
for row in csv.DictReader((OUT / (PREFIX + '_results.csv')).open()):
    stats[row['status']] = stats.get(row['status'], 0) + 1
state = 'INCOMPLETE' if stats.get('Open') else 'See the obligation register'
readme = f'''# {PREFIX}

**{state}**

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

The paper and its report retain every unresolved obligation. A successful
computation or PDF build does not change the mathematical status of a claim.
The report begins with the complete 39-obligation register.

## Main files

- `{PREFIX}_paper.pdf` and `{PREFIX}_paper.tex`: the self-contained paper.
- `{PREFIX}_results.csv`: one row for each numbered statement.
- `{PREFIX}_readings.csv`: doubtful manuscript readings and mathematical evidence.
- `{PREFIX}_references.bib`: source metadata and individual verification notes.
- `{PREFIX}_report.md`: proof, source, computation and remaining-obligation record.
- `manifest.csv`: exact size and SHA-256 hash of every other packaged file.

Registered statuses: {', '.join(f'{k}={v}' for k,v in sorted(stats.items()))}.

## Complete finite-action index

Start with `code/part_b/low_complexity_catalogue_README.md` and
`code/part_b/low_complexity_catalogue_index.csv`. They route all 16 types,
882 mapping-class subgroup rows and 889 injective realization rows to their
exact section certificates. The exceptional realization fibers are retained.
All paths in the index are relative to this ZIP root.

The master assembler can be rerun from this directory:

```sh
python code/part_b/assemble_low_complexity_catalogues.py
```

Every required input is included. Packaging itself reruns this command and
compares all eight generated outputs byte for byte with the accepted outputs.

## Computation layout

`code/part_a`, `code/part_b`, `code/part_c`, `code/part_d_attack`, and
`code/root` contain the mathematical programs and their captured outputs.
Selected original `work/part_d_attack/code` paths are also retained so the
frozen review bindings remain literal. Isolated independent replays retain their
explicit `work/` directories. The archive also includes the finite presentation caches,
and the original machine-readable genus-two/genus-three census inputs.
The latter include their source attribution and hash verification. Individual
programs write their outputs beside themselves; invoke each by its file path.
Python 3.12 was used. The finite-presentation enumerators use SymPy; accepted exact checks also use
the Python standard library and the included modules. The explicitly marked
seven-point braid exploration uses NumPy and numerical crossing extraction;
it supplies no asserted relation or injectivity proof. Accepted certificates
use exact integer, rational, finite-field, permutation or free-word operations.
Every infinite assertion has its separate proof; exploratory files retain
their stated scope and are not promoted by inclusion in this archive.

## Paper build and source assembly

With LuaLaTeX and BibTeX installed, the root paper builds directly:

```sh
lualatex -interaction=nonstopmode -halt-on-error {PREFIX}_paper.tex
bibtex {PREFIX}_paper
lualatex -interaction=nonstopmode -halt-on-error {PREFIX}_paper.tex
lualatex -interaction=nonstopmode -halt-on-error {PREFIX}_paper.tex
```

The active modular sources and metadata are retained under `work/`.
Running `python work/root/assemble.py` regenerates the paper and registers
under a newly created `deliverable/` directory. The supplied
`work/root/build_pdf.py --full` configures writable TeX caches for the Linux
environment used here; an ordinary TeX installation can use the four commands
above instead. `pdf_qa.py` needs PyMuPDF and renders pages for visual review.
Its rendered images alone do not certify that they have been viewed.

`verification/` retains build logs, the assembly audit, PDF checks, visual
review records when present, and the packaged catalogue execution record.
'''
(STAGE / 'README.md').write_text(readme)

# Captured interpreter caches are irrelevant and excluded from the ZIP.
for cache in STAGE.rglob('__pycache__'):
    shutil.rmtree(cache)
MARKER.unlink()
files = sorted(p for p in STAGE.rglob('*') if p.is_file())
summary = {
    'status': state, 'claims_by_status': stats,
    'catalogue_required_inputs': len(required['required_for_assembler']),
    'missing_catalogue_inputs': missing,
    'catalogue_outputs_byte_identical': before == after,
    'catalogue_output_count': len(before),
    'payload_file_count_before_manifest_and_summary': len(files),
    'uncompressed_payload_bytes_before_manifest_and_summary': sum(p.stat().st_size for p in files),
    'excluded': ['__pycache__', '*.pyc'],
}
(OUT / 'package_manifest_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
copy(OUT / 'package_manifest_summary.json', STAGE / 'verification/package_manifest_summary.json')
# Incorporate the successful package-layout check in the report before hashing.
report = subprocess.run([sys.executable, str(ROOT / 'work/root/make_report.py')],
                        cwd=ROOT, capture_output=True, text=True)
if report.returncode:
    raise RuntimeError('Report regeneration failed: ' + report.stderr)
copy(OUT / (PREFIX + '_report.md'), STAGE / (PREFIX + '_report.md'))
with (STAGE / 'manifest.csv').open('w', newline='') as f:
    w = csv.writer(f); w.writerow(['path', 'bytes', 'sha256'])
    for p in sorted(STAGE.rglob('*')):
        if p.is_file() and p.name != 'manifest.csv':
            w.writerow([str(p.relative_to(STAGE)), p.stat().st_size, sha(p)])
archive = OUT / (PREFIX + '.zip')
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(STAGE.rglob('*')):
        if p.is_file(): z.write(p, str(p.relative_to(STAGE)))
with zipfile.ZipFile(archive) as z:
    bad = z.testzip()
    if bad: raise RuntimeError('ZIP CRC failed at ' + bad)
    entries = len(z.namelist())
MARKER.write_text('Private staging directory owned by package_deliverable.py\n')
verification = {'archive': archive.name, 'bytes': archive.stat().st_size,
                'sha256': sha(archive), 'entries': entries, 'crc_error': bad,
                **summary}
(OUT / 'package_zip_verification.json').write_text(json.dumps(verification, indent=2) + '\n')
print(json.dumps(verification, indent=2))
