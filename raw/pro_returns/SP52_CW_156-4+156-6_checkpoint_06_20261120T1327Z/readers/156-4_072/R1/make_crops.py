from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R1')
src=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan072.jpg')
items=[
 ('01_quand_marks',[1080,255,1635,470],0,'Two repetition-like signs after quand; complete strokes and next line.'),
 ('02_en_forme',[270,265,980,470],0,'End of opening paragraph, including en forme and preceding line.'),
 ('03_definition_capital',[785,450,1390,755],0,'Worked capital C and tuple alphabets/order, with neighbouring line.'),
 ('04_pleine_connector',[1210,350,1655,660],0,'Bracketed raised pleine, underline and full hooked insertion stroke.'),
 ('05_tout_satisfait',[740,545,1668,790],0,'State of tout and verb satisfait/satisfont in next line.'),
 ('06_correspond',[440,775,1670,1020],0,'quelc. and s’en corre-/spond across line boundary.'),
 ('07_a_mappings',[495,895,1590,1120],0,'Both a mappings, inserted M prime, F roof and enclosing punctuation.'),
 ('08_oblique_question',[24,850,550,1410],-40,'Whole slanted finite/arbitrary-supremum question with all terminal words; the successful view showed the final word/parenthesis incompletely framed, recorded below.'),
 ('09_b_correction',[510,1200,1540,1490],0,'Extra mark after M and whole interlinear replacement/deleted clause.'),
 ('10_marginal_c',[1025,1338,1670,1635],0,'Entire marginal c, reporter, subd ending, mapping, deletions, i.e. and pointer.'),
 ('11_C6_first',[475,1560,1555,1878],0,'First C6 diagram, qualifier, family alphabet, and two low detached points.'),
 ('12_C6_a_end',[1210,1845,1655,2010],0,'H, family F and word at end of a with adjacent line.'),
 ('13_C6_b_note',[1150,1940,1668,2245],0,'Whole b note: both strates, correction, telles, G tail, continuation and rules.'),
 ('14_symetrique',[25,1620,330,1925],-42,'Whole diagonal symmetry note and crossing vertical rule.'),
 ('15_last_body',[285,2205,1668,2359],0,'Both final body lines, exact underline extents, contraction points and deletion.'),
 ('16_last_margin',[25,2140,435,2359],-27,'Whole diagonal sur la sous-figure note, including G de F.')
]
(out/'crops').mkdir(exist_ok=True)
records=[]
with Image.open(src) as whole:
 for name,bbox,rotation,reason in items:
  crop=whole.crop(bbox)
  crop=ImageOps.autocontrast(crop,cutoff=0)
  if rotation:
   crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  scale=2500/crop.width
  crop=crop.resize((2500,round(crop.height*scale)),Image.Resampling.LANCZOS)
  crop=ImageEnhance.Sharpness(crop).enhance(1.15)
  path=out/'crops'/f'{name}.jpg'
  crop.save(path,quality=94,subsampling=0)
  records.append(dict(path=str(path),source=str(src),bbox=bbox,scale=scale,rotation=rotation,reason=reason,autocontrast_cutoff=0,sharpen_factor=1.15,size=list(crop.size)))
(out/'crop_metadata.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Restored 16 identical crop images and metadata; this script does not display images.')
