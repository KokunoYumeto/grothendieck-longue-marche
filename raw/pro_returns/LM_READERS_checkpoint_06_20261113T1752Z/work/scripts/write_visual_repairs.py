"""Curate confirmed visual repairs and their exact-source/probe evidence."""
from pathlib import Path
import csv,json,shutil,re,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'work/visual_repair_proofs';OUT.mkdir(exist_ok=True)
P='work/layout_probes/'
CASES=[
('140-1-10-L1','The diagonal from Z/3Z to E crossed the first-projection label in the second large branching diagram.',P+'scan10_projection_{lang}.pdf',P+'scan10_projection_{lang}_pr_zoom.png',{'fr':3,'en':2},'work/verification_before_repairs/FR_reading/zoom_vector_0010_crossing.png'),
('140-1-20-T1','In the lower-right triangle, the Cartesian face label met the diagonal canonical label, and the bottom canonical label touched an arrowhead.',P+'scan20_forms_{lang}.pdf',P+'scan20_triangle_{lang}.png',{'fr':1,'en':1},'work/build/EN_reading_p19_diagram_zoom.png'),
('140-2-165-L1','In the cancelled diamond, the pseudo-commutativity label met the central object and diagonal; a lower illegibility marker was crossed by the central vertical.',P+'scan165_candidate_{lang}.pdf',P+'scan165_candidate_{lang}_1.png',{'fr':2,'en':2},'work/verification_before_repairs/EN_app/zoom_vector_0178_deleted_diagram.png'),
('140-2-331-T1','The prose cell repeated the marginal-note rule and heading already emitted by the note renderer.',P+'scan331_note_candidate_{lang}.pdf',P+'scan331_note_candidate_{lang}_1.png',{'fr':2,'en':2},''),
('140-2-344-NP1','The two adjacent doubtful marginal notes overprinted one another; their old baselines were only about 2pt apart.','PAIR_PDF','PAIR_PNG',{'fr':7,'en':7},''),
('140-2-417-L1','The uncertain noncommutativity annotation and the commutativity annotation were crossed by the diagonal/right vertical paths.',P+'scan417_candidate_{lang}.pdf',P+'scan417_candidate_{lang}.png',{'fr':1,'en':1},'work/verification_before_repairs/EN_app/zoom_raster_0394_labels.png'),
('140-2-520-L1','The Galois-covering label overlapped the adjacent object subscripts.',P+'scan520_forms_{lang}.pdf',P+'scan520_label_{lang}.png',{'fr':1,'en':1},'work/build/EN_reading_p271_zoom.png'),
('140-3-33-L1','The determinant-map label touched the two neighbouring group objects.',P+'scan33_label.pdf',P+'scan33_label.png',{'fr':1,'en':1},'work/build/EN_reading_p319_zoom.png'),
('140-3-97-L1','The final letter of the upper restriction label in equation (49) touched its arrowhead barb; the lower label was separately cleared.',P+'scan97_restriction_{lang}.pdf',P+'scan97_restriction_{lang}_5.png',{'fr':5,'en':5},'work/visual_repair_proofs/native_final_residual/ENapp_p617_restriction_1.png'),
('140-3-440-L1','The cube in equation (116) placed G_m on a vertical path and brought three mu labels, the kappa-circle label and the lower PG label into contact with crossing paths.',P+'scan440_candidate_{lang}.pdf',P+'scan440_candidate_{lang}_4.png',{'fr':5,'en':5},'work/visual_repair_proofs/pagination_original/LM_FR_texte_de_lecture_p0584_116.png'),
('140-3-446-T1','Both quotient labels overprinted the isomorphism signs in the right-hand objects.',P+'latest_label_candidates_{lang}.pdf',P+'latest_label_candidates_{lang}_1.png',{'fr':1,'en':1},'work/build/EN_reading_p593_diagram_zoom.png'),
('140-3-495-N1','The two-line French short marginal note extended below the allowed foot area in the full reading book.','MARGIN495_PDF',P+'scan495_margin_{lang}.png',{'fr':2,'en':2},'work/verification_before_repairs/FR_reading/zoom_vector_0622_margin_foot.png'),
('140-3-525-L1','The middle vertical epimorphism label overprinted chi on the next vertical map.',P+'latest_label_candidates_{lang}.pdf',P+'latest_label_candidates_{lang}_2.png',{'fr':2,'en':2},'work/build/EN_reading_p653_diagram_zoom.png'),
('140-3-542-L1','The horizontal epimorphism label in marginal equation (46bis) crossed both adjacent effective-object superscripts.',P+'epimorphism_clearance_{lang}.pdf',P+'epimorphism_clearance_{lang}_1.png',{'fr':1,'en':1},'work/verification_before_repairs/EN_app/zoom_raster_1089_labels.png'),
('140-3-545-L1','The epsilon-map label in equation (59) overlapped the left object and the target brace.',P+'latest_label_candidates_{lang}.pdf',P+'latest_label_candidates_{lang}_4.png',{'fr':4,'en':4},'work/build/EN_reading_p669_labelcheck.png'),
('140-3-545-L2','The terminal parenthesis of the epsilon-pair label in equation (58) touched the upper arrowhead barb in the full diplomatic book.',P+'scan545_eq58_{lang}.pdf',P+'scan545_eq58_{lang}_1.png',{'fr':2,'en':2},'work/layout_probes/scan545_eq58_before_native.png'),
('140-3-556-L1','The two vertical epimorphism labels in equation (43) overprinted in the shared column gap.',P+'epimorphism_clearance_{lang}.pdf',P+'epimorphism_clearance_{lang}_2.png',{'fr':2,'en':2},''),
('140-3-557-T1','The three convergent dashed-map labels collided with strokes or the character-tuple label.',P+'scan557_candidate_{lang}.pdf',P+'scan557_candidate_{lang}.png',{'fr':1,'en':1},'work/verification_before_repairs/EN_app/zoom_vector_1107_diagram.png'),
('140-3-561-D1','The dashed boundary crossed the top of region label II in landscape equation (62).',P+'scan561_route_{lang}.pdf',P+'scan561_route_{lang}_II_zoom.png',{'fr':2,'en':2},'work/verification_before_repairs/EN_app/zoom_vector_1113_II.png'),
('140-3-562-L1','The two central vertical edges crossed uncertain central objects and their superscripts.',P+'additional_label_candidates_{lang}.pdf',P+'additional_label_candidates_{lang}_1.png',{'fr':1,'en':1},'work/verification_before_repairs/EN_app/zoom_vector_1115_center.png'),
('140-3-568-L1','The epimorphism label in the composite following equation (79) crossed the adjacent effective-object superscripts.',P+'epimorphism_clearance_{lang}.pdf',P+'epimorphism_clearance_{lang}_3.png',{'fr':3,'en':3},''),
('140-3-573-L1','The second line of the restriction label met the adjacent automorphism object and arrow barb.',P+'additional_label_candidates_{lang}.pdf',P+'additional_label_candidates_{lang}_2.png',{'fr':2,'en':2},'work/verification_before_repairs/EN_app/zoom_vector_1129_restriction.png'),
('140-3-574-L1','The sign-of-a-permutation label met the upper curved-arrow barb and target opening brace.',P+'additional_label_candidates_{lang}.pdf',P+'additional_label_candidates_{lang}_3.png',{'fr':3,'en':3},'work/verification_before_repairs/EN_app/zoom_vector_1130_sign.png'),
('140-3-619-T1','The homomorphism (130) label overprinted the quotient objects on the top row of equation (144).',P+'latest_label_candidates_{lang}.pdf',P+'latest_label_candidates_{lang}_3.png',{'fr':3,'en':3},''),
('140-3-628-L1','The diagonal toward the elliptic-curve object crossed the gerbe-of-group label.',P+'additional_label_candidates_{lang}.pdf',P+'additional_label_candidates_{lang}_5.png',{'fr':5,'en':5},'work/build/EN_reading_p735_diagram26.png'),
('140-3-637-T1','A long diagonal crossed the middle-left object in equation (37).',P+'scan637_route_{lang}.pdf',P+'scan637_route_{lang}_1.png',{'fr':1,'en':1},'work/verification_before_repairs/EN_app/zoom_vector_1203_diagonal.png'),
('140-3-638-L1','Long paths crossed equation (38), node 1, the uncertain N object and the upper M-zero object.',P+'scan638_forms_{lang}.pdf',P+'scan638_forms_{lang}_1.png',{'fr':2,'en':2},'work/verification_before_repairs/EN_app/zoom_vector_1204_cube.png'),
('140-3-660-L1','The heads of two distinct diagonal maps overlapped below the live sharp object after the cancelled target cell became empty.',P+'scan660_candidate_{lang}.pdf',P+'scan660_candidate_{lang}_'+('LANGPAGE')+'.png',{'fr':1,'en':2},'work/build/EN_reading_p756_diagram31.png'),
('140-2-568-L1','The Galois degree-two label in equation (67) touched the horizontal arrowhead and the following M object.',P+'final_label_clearances_{lang}.pdf',P+'final_label_clearances_{lang}_1.png',{'fr':1,'en':1},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan568_clearance.png'),
('140-3-519-L1','The additional shortened diagonal arrowhead in equation (77) touched the uncertain1 label.',P+'final_label_clearances_{lang}.pdf',P+'final_label_clearances_{lang}_2.png',{'fr':2,'en':2},'work/verification/LM_FR_texte_de_lecture/zoom_vector_0644_12x.png'),
('140-3-536-L1','The two horizontal delta-label subscripts and the uncertain chi-gamma subscript met their nearby arrowhead barbs.',P+'final_label_clearances_{lang}.pdf',P+'final_label_clearances_{lang}_3.png',{'fr':3,'en':3},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan536.png'),
('140-3-448-L1','The two determinant-of-T label subscripts met the horizontal arrowhead tips in equation (134); the upper determinant-of-G label was separately cleared.',P+'final_label_clearances_{lang}.pdf',P+'final_label_clearances_{lang}_4.png',{'fr':4,'en':4},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan448.png'),
('140-3-480-L1','The three short labels in equation (12bis) met the arrowheads at their final subscripts or denominator.',P+'scan480_554_candidate_{lang}.pdf',P+'scan480_554_candidate_{lang}_0.png',{'fr':1,'en':1},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan480.png'),
('140-3-480-L2','The long character tuple in equation (13) met the injection arrowhead and adjacent product object.',P+'scan480_554_candidate_{lang}.pdf',P+'scan480_554_candidate_{lang}_0.png',{'fr':1,'en':1},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan480.png'),
('140-3-554-L1','The final G subscript in the character tuple of equation (29) touched the arrowhead barb.',P+'scan480_554_candidate_{lang}.pdf',P+'scan480_554_candidate_{lang}_1.png',{'fr':2,'en':2},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan554.png'),
('140-4-276-L1','The uncertain phantom-arrow description in equation (134) covered portions of the source U-tilde and target Cont object.',P+'scan276_clearance_{lang}_1.pdf',P+'scan276_clearance_{lang}_1.png',{'fr':1,'en':1},'work/verification/LM_FR_corrige_apparat/zoom_baseline_scan276.png'),
]
# The native final-page inspection refined five existing repairs. These
# accepted all-form probe images supersede the earlier target-only images.
RESIDUALS={
 '140-3-446-T1':(446,1,'The later native check also found contact between the terminal quotient-label letters and the lower arrowhead barbs.'),
 '140-3-574-L1':(574,2,'The later native check also found contact between the uncertain sg|sgn label and its upper curved arrow.'),
 '140-3-561-D1':(561,3,'The later native check also found three labels crossed by vertical paths: both right-hand epsilon labels and the uncertain projection label.'),
 '140-3-637-T1':(637,4,'The later native check also found both middle-row horizontal degree labels crossed by vertical paths.'),
 '140-3-638-L1':(638,5,'The later native check also found two upper vertical degree labels crossed by horizontal paths.'),
}
CASES=[(ident,issue+' '+RESIDUALS[ident][2],P+'final_residual_labels_{lang}_1.pdf',
        P+f'final_residual_scan{RESIDUALS[ident][0]}'+'_{lang}_1.png',
        {'fr':RESIDUALS[ident][1],'en':RESIDUALS[ident][1]},before)
       if ident in RESIDUALS else (ident,issue,pdf,png,pages,before)
       for ident,issue,pdf,png,pages,before in CASES]

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy(src,name=None):
 src=ROOT/src;assert src.exists(),src
 dest=OUT/(name or src.name);shutil.copyfile(src,dest)
 return 'proofs/visual_repairs/'+dest.name,digest(dest)

def publication_evidence(language,cote,scan):
 books={'fr':['LM_FR_diplomatique','LM_FR_corrige_apparat','LM_FR_texte_de_lecture','LM_FR_master_annotated'],
        'en':['LM_EN_corrected_apparatus','LM_EN_reading','LM_EN_master_annotated']}[language]
 result=[]
 for book in books:
  path=ROOT/'work/verification'/f'{book}.verification.json'
  if not path.exists():continue
  v=json.loads(path.read_text());pages=v['links']['scan_to_physical_pages'].get(f'{cote}:{scan}',[])
  assert pages,(book,cote,scan)
  result.append(dict(archive='LM_READERS_'+language.upper()+'.zip',file=book+'.pdf',
      pdf_sha256=v['sha256'],scan=f'{cote}:{scan}',physical_pages=pages,
      trace_record='work/verification/'+path.name))
 return result

def main():
 records=json.loads((ROOT/'work/data/layout_repairs_applied.json').read_text());lookup={(r['id'],r['language']):r for r in records};rows=[];inventory=[]
 for ident,issue,pdf0,png0,pages,before in CASES:
  beforefile='';beforehash=''
  if before and (ROOT/before).exists():beforefile,beforehash=copy(before,ident+'_before.png')
  for lang in ['fr','en']:
   r=lookup[(ident,lang)];pdf=pdf0.format(lang=lang);png=png0.format(lang=lang).replace('LANGPAGE','1' if lang=='fr' else '2')
   if pdf=='PAIR_PDF':
    stem='LM_FR_corrige_apparat' if lang=='fr' else 'LM_EN_corrected_apparatus';pdf='work/layout_pair_validation/'+stem+'_paired_notes.pdf';png='work/layout_pair_validation/'+stem+'_paired_notes_margin.png'
   if pdf=='MARGIN495_PDF':pdf='work/layout_margin495_validation/'+('LM_FR_texte_de_lecture' if lang=='fr' else 'LM_EN_reading')+'_margin495.pdf'
   # Development PDFs remain available to immutable checkpoint packaging.
   # They are explicitly excluded from every FINAL archive; only the seven
   # publication PDFs are delivered as finished PDFs.
   proofpdf,pdfhash=copy(pdf);proofpng,pnghash=copy(png,ident+'_'+lang+'.png')
   prooftex,texhash=copy(str(Path(pdf).with_suffix('.tex')))
   prooflog,loghash=copy(str(Path(pdf).with_suffix('.log')))
   log=(ROOT/pdf).with_suffix('.log').read_text(errors='replace')
   gate=dict(errors=len(re.findall(r'^!',log,re.M)),overfull_hboxes=log.count('Overfull \\hbox'),missing_glyphs=log.count('Missing character:'))
   assert not any(gate.values()),(pdf,gate)
   affected_scan=495 if ident=='140-3-495-N1' else r['scan']
   publications=publication_evidence(lang,r['cote'],affected_scan)
   row=dict(repair_id=ident,language=lang,cote=r['cote'],affected_scan=affected_scan,source_scan=r['scan'],package=r['package'],source_path=r['source_path'],source_line=r['source_line'],source_byte_start=r['source_byte_start'],source_byte_end=r['source_byte_end'],before_issue=issue,exact_action=r['reason'],exact_tex_record='LAYOUT_REPAIR_DETAILS.tsv: '+ident+' / '+lang,probe_pdf=proofpdf,probe_pdf_status='historical development probe; not delivered in FINAL',probe_pdf_delivered_in_final=False,probe_page=pages[lang],probe_image=proofpng,probe_tex=prooftex,probe_log=prooflog,probe_errors=gate['errors'],probe_overfull_hboxes=gate['overfull_hboxes'],probe_missing_glyphs=gate['missing_glyphs'],probe_pdf_sha256=pdfhash,probe_image_sha256=pnghash,probe_tex_sha256=texhash,probe_log_sha256=loghash,before_image=beforefile,before_image_sha256=beforehash,publication_evidence_json=json.dumps(publications,ensure_ascii=False,separators=(',',':')),proof_scope='The accepted local PNG, TeX, log and hashes are delivered as development evidence. Probe PDFs are retained only in historical checkpoints and excluded from FINAL. Publication evidence is the hash-bound reader/master scan-to-page trace listed here.')
   rows.append(row);inventory.append(dict(repair_id=ident,language=lang,original_pdf=pdf,original_image=png,historical_checkpoint_pdf=proofpdf,delivered_pdf=None,pdf_status='historical_not_delivered_in_final',delivered_image=proofpng,delivered_tex=prooftex,delivered_log=prooflog,pdf_sha256=pdfhash,image_sha256=pnghash,tex_sha256=texhash,log_sha256=loghash,publication_evidence=publications))
 with (ROOT/'work/records/VISUAL_REPAIRS.tsv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
 (ROOT/'work/data/visual_repair_proof_inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
 for lang in ['fr','en']:
  for mode in [0,2]:
   for extension in ['pdf','png','tex','log']:
    copy(P+f'scan276_clearance_{lang}_{mode}.{extension}')
  for scan,_,_ in RESIDUALS.values():
   copy(P+f'final_residual_scan{scan}_{lang}_forms.png')
   for mode in [0,1,2]:copy(P+f'final_residual_scan{scan}_{lang}_{mode}.png')
  for mode in [0,2]:
   for extension in ['pdf','tex','log']:copy(P+f'final_residual_labels_{lang}_{mode}.{extension}')
  for mode in [0,1,2]:
   copy(P+f'scan97_restriction_{lang}_{mode+4}.png')
   copy(P+f'scan440_candidate_{lang}_{mode+3}.png')
   copy(P+f'scan545_eq58_{lang}_{mode}.png')
  for pattern in [f'scan97_restriction_{lang}_*_native.png',f'scan440_final_labels_{lang}_*.png']:
   for path in (ROOT/P).glob(pattern):copy(path.relative_to(ROOT).as_posix())
 for name in ['scan97_restriction_proof_index.json','scan440_geometry_validation.json',
              'scan545_eq58_validation.json','final_residual_labels_visual_review.json',
              'final_residual_labels_probe_summary.json','tag_pattern_stress_validation.json',
              'tag_pattern_stress_index.json']:
  copy(P+name)
 for lang in ['fr','en']:
  for mode in [0,1,2]:
   for extension in ['tex','log']:copy(P+f'tag_pattern_stress_{lang}_{mode}.{extension}')
 for name in ['tag_pattern_stress_fr_0_groups.png','tag_pattern_stress_en_2_groups.png']:
  copy(P+name)
 print(len(CASES),'confirmed visual display/placement occurrences;',len(rows),'paired records;',len(list(OUT.iterdir())),'curated proof files')
 from write_visual_batch_proofs import extend
 extend()
 from write_visual_residual578_proofs import extend_revision578
 extend_revision578()
if __name__=='__main__':main()
