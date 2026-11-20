from pathlib import Path
import subprocess,json
out=Path('/workspace/scratch/42e661864e98/out/readers/scan012/R1')
source='/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012.jpg'
crops=[
 ('01_diagram_frame',[531,340,886,724],0,2800,'Whether the oblique frame is closed at the two left corners.'),
 ('02_diagram_compatibility',[809,562,965,647],0,2800,'Shape and live/deleted state of the densely retraced compatibility sign.'),
 ('03_slanted_correction',[18,746,620,1320],-38,3400,'Read the coherent slanted correction, including membership, cancellation, reflexivization, and terminal punctuation.'),
 ('04_relation_start',[235,986,579,1084],0,2800,'Whether an initial Les is canceled before La relation.'),
 ('05_family_f',[519,1067,613,1158],0,2400,'First family F: drawn alphabet and foot, distinct from ordinary F.'),
 ('06_element_word',[1312,1064,1597,1158],0,2800,'Abbreviated or full element word and following empty-figure subscript.'),
 ('07_remarques_initial',[526,1379,668,1474],0,2400,'Capital or lower-case first letter after a).'),
 ('08_final_inequality_120',[1423,1625,1670,1706],0,2800,'State of the retraced last inequality and the i index and closing brace.'),
 ('09_deleted_before_dautre',[255,1783,468,1878],0,2800,'Canceled group above the opening D of D’autre.'),
 ('10_bottom_revision',[877,2138,1673,2264],0,3400,'Read the complete replacement above the canceled phrase, including compressed adjective and equivalent.')
]
records=[]
for name,box,rotation,width,why in crops:
 dest=out/'crops'/f'{name}.jpg'
 subprocess.run(['python','/workspace/scratch/42e661864e98/out/scripts/crop_locus.py',source,str(dest),*[str(x) for x in box],'--rotation',str(rotation),'--width',str(width)],check=True)
 records.append(dict(name=name,image=str(dest),source=source,box=box,rotation=rotation,width=width,reason=why))
(out/'crop_plan.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
