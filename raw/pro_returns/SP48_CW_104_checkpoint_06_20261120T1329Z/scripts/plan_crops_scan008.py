from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, subprocess, sys

out=Path(__file__).resolve().parents[1]; rec=out/'records/scan008'
assert not (rec/'main_crop_plan.json').exists()
spec=[
('opening', [180,45,825,155],2800),
('definition','records/scan008/reader_A/crops/01_definition.png'),
('first_display_J_ens',[440,130,990,250],2800),
('sous_objet','records/scan008/reader_A/crops/02_sous_objet.png'),
('canonical_sentence',[190,235,1480,455],3200),
('type_map_caption',[540,390,1675,530],3200),
('formee_deleted_des','records/scan008/reader_A/crops/03_formee.png'),
('image_ens',[1120,490,1460,605],2800),
('old_I_des_and_point',[185,635,665,785],2800),
('chaque_J',[185,785,960,950],3000),
('Dn_quotation',[750,880,985,990],2800),
('en_tant_le','records/scan008/reader_A/crops/04_en_tant_le.png'),
('naming_cluster','records/scan008/reader_C/05_quon.png'),
('par_ii_insertion',[1365,935,1670,1070],2800),
('deleted_Si',[285,1100,1385,1225],3200),
('old_x_and_lower_J','records/scan008/reader_A/crops/06_old_x.png'),
('Soient_equation_on_avec',[1080,1150,1605,1300],3000),
('considerons_cancellations','records/scan008/reader_A/crops/07_considerons.png'),
('first_Hom_complete','records/scan008/reader_C/08_first_Hom.png'),
('bijection_ens',[195,1525,430,1630],2800),
('second_Hom_old_and_high','records/scan008/reader_A/crops/09_second_Hom.png'),
('second_Hom_brackets',[1165,1595,1455,1780],2800),
('detached_pair','records/scan008/reader_C/15_points_after_map.png'),
('deleted_bijec','records/scan008/reader_A/crops/10_bice.png'),
('def_label',[680,1788,790,1890],2400),
('lower_J_and_canceled_group','records/scan008/reader_A/crops/11_lower_J.png'),
('rho_and_target_Hom',[995,1795,1675,1955],3000),
('vertical_relation_brackets','records/scan008/reader_A/crops/12_lower_Hom.png'),
('lower_caption',[740,1900,1015,2135],2800),
('ou_xi_row',[1050,1940,1420,2058],2800),
('injective_plus_precisement',[190,2035,1615,2165],3200),
('commutativite','records/scan008/reader_A/crops/13_commutativite.png'),
('space_after_commutativite',[1005,2125,1265,2240],2600),
('complete_final_diagram',[585,2170,1580,2360],3200),
]
plan=[]
for number,item in enumerate(spec,1):
    name,target,*rest=item
    if isinstance(target,str):
        assert (out/target).exists(); path=target; source='reader reuse'
    else:
        width=rest[0]
        subprocess.run([sys.executable,str(out/'scripts/make_crop.py'),'8',name,*map(str,target),'--width',str(width)],check=True,stdout=subprocess.DEVNULL)
        path=f'crops/scan008_{name}.png'; source='new main crop'
    row={'number':number,'locus':name,'path':path,'viewed':False,'source':source}
    if not isinstance(target,str):row['bbox']=target
    plan.append(row)
(rec/'main_crop_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
source_counts={}; source_hashes={}
for a in 'ABC':
    p=rec/f'reader_{a}'
    d=json.loads((p/'report.json').read_text()); source_counts[a]=len(d['issues'])
    source_hashes[a]={f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in ['reading.tex','report.json','read_log.md']}
(rec/'main_comparison.json').write_text(json.dumps({'scan':8,'compared_utc':now,'all_three_full_readings_compared':True,'all_source_issues_compared_before_main_crops':True,'source_issue_counts':source_counts,'reader_hashes':source_hashes,'main_images_viewed_before_comparison':0,'key_disagreements':['naming cluster resolved versus 3/5 alternatives','via x versus via (x) ordering','bijec resolved versus uncertain split alternatives','vertical relation identity and bracket enclosure','two C-reader detached-point groups','A final inclusion endpoint gaps versus retained C geometry'],'notes':['C reader reading.tex was reread at its updated naming line: all five alternatives are preserved in the comparison record.','Existing crop metadata, not approximate issue boxes, was used for coverage.','Main09 is new because the reader point crop does not contain the complete old I/des cancellation.','Main33 covers new blank context after the full word crop; it will not re-adjudicate the word.']},ensure_ascii=False,indent=2)+'\n')
(rec/'main_observations.md').write_text('# Scan 008 main adjudication observations\n\nAll three complete readings and all 156 source issue records were compared before any main image. No main whole or half scan was viewed. Every following crop is inspected once; adjacent portions outside its assigned locus are context only.\n')
print(json.dumps({'crops':len(plan),'new':sum(x['source']=='new main crop' for x in plan),'reused':sum(x['source']=='reader reuse' for x in plan),'source_issue_counts':source_counts,'compared_utc':now}))
