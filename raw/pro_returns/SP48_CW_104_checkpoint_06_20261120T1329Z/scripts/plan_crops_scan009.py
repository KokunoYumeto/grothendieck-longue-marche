from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, subprocess, sys
out=Path(__file__).resolve().parents[1]; rec=out/'records/scan009'
assert not (rec/'main_crop_plan.json').exists()
spec=[
('opening_memberships',[740,60,1620,165],3200),
('opening_cancellation','records/scan009/reader_B/crops/c01_opening_cancellation.png'),
('isom_and_lorsque_prime','records/scan009/reader_B/crops/c02_isom_insertion_prime.png'),
('brace_and_isom_map',[875,135,1440,342],3000),
('singleton',[900,288,1275,386],2600),
('identity',[565,400,880,520],2600),
('J_family',[1110,525,1375,640],2400),
('rho_family','records/scan009/reader_A/crop03_family_index.png'),
('cancelled_reconstruction','records/scan009/reader_A/crop04_cancelled_reconstruction.png'),
('equiv_accent','records/scan009/reader_B/crops/c06_equiv.png'),
('condition_oldword','records/scan009/reader_A/crop06_condition_description.png'),
('composer',[790,1020,1095,1120],2600),
('hom_standart','records/scan009/reader_B/crops/c08_standart.png'),
('entre_les_and_ie',[255,1120,1055,1235],3200),
('pair_and_Donc','records/scan009/reader_C/crops/10_pair_Donc.png'),
('une_situation',[675,1205,1580,1320],3200),
('composition_diagram','records/scan009/reader_A/crop09_diagram.png'),
('lower_old_subscript','records/scan009/reader_A/crop10_zeta_correction.png'),
('lower_evaluation_and_point',[850,1785,1650,1930],3200),
('cancelled_stability','records/scan009/reader_A/crop11_stability_correction.png'),
('singular_hom',[205,2010,875,2125],3000),
('entre_and_J','records/scan009/reader_A/crop12_entre.png'),
('final_cancellation_and_insertion',[210,2080,1330,2265],3400),
('final_cases',[375,2185,1640,2355],3500),
]
plan=[]
for number,item in enumerate(spec,1):
 name,target,*rest=item
 if isinstance(target,str):
  assert (out/target).exists(); path=target; source='reader reuse'
 else:
  subprocess.run([sys.executable,str(out/'scripts/make_crop.py'),'9',name,*map(str,target),'--width',str(rest[0])],check=True,stdout=subprocess.DEVNULL)
  path=f'crops/scan009_{name}.png'; source='new main crop'
 row={'number':number,'locus':name,'path':path,'viewed':False,'source':source}
 if not isinstance(target,str):row['bbox']=target
 plan.append(row)
(rec/'main_crop_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
counts={}; hashes={}
for a in 'ABC':
 p=rec/f'reader_{a}'; counts[a]=len(json.loads((p/'report.json').read_text())['issues'])
 hashes[a]={f:hashlib.sha256((p/f).read_bytes()).hexdigest() for f in ['reading.tex','report.json','read_log.md']}
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(rec/'main_comparison.json').write_text(json.dumps({'scan':9,'compared_utc':now,'all_three_full_readings_compared':True,'all_source_issues_compared_before_main_crops':True,'source_issue_counts':counts,'reader_hashes':hashes,'main_images_viewed_before_comparison':0,'key_disagreements':['plus cancellation state','isom and brace return','second inline index n-prime/n^4/n','acute/grave accent in pres','description versus retained alternative','old a/xi','cancelled stability candidates including compatibility','entre punctuation state','isolated point at later equality'],'notes':['All129 source issues, complete readings, inventories, and actual check events were compared.','Crop metadata, not issue boxes, determines reused image coverage.','New brace map and final cancellation crops cover reader-clipped descenders; no main locus has previously been viewed.','Only assigned undecided loci are adjudicated in any overlap.']},ensure_ascii=False,indent=2)+'\n')
(rec/'main_observations.md').write_text('# Scan 009 main adjudication observations\n\nAll three complete readings and all129 source issues were compared before any main image. No main whole or half scan was viewed. Each crop is inspected once. Adjacent already-decided ink is context only.\n')
print(json.dumps({'crops':len(plan),'new':sum(x['source']=='new main crop' for x in plan),'reused':sum(x['source']=='reader reuse' for x in plan),'counts':counts,'compared_utc':now}))
