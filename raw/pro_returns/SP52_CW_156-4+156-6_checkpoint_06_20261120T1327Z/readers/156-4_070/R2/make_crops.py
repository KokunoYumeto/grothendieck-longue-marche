from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R2')
src='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan070.jpg'
im=Image.open(src)
specs=[
('c01_opening',(630,145,1670,350),0,'Opening relation, reduced tres/très and spaced aura; includes surrounding opening line.'),
('c02_cancelled_noun',(1000,330,1575,505),0,'Cancelled noun after deux; previous line and complete right end included.'),
('c03_raised_condition',(235,445,865,700),0,'Raised F primes, possibly cancelled relation and trailing dash, and live phrase following figures.'),
('c04_ie_subdivisions',(855,465,1660,675),0,'Dotted/parenthetic word and capital Subdivisions, through d\'une, with following line.'),
('c05_repetition_f',(235,585,1080,805),0,'Repetition sign and F terminal punctuation, with inf line.'),
('c06_second_noun_primes',(300,730,1650,950),0,'Singular/plural subdivision ending and second F prime count, with following line.'),
('c07_worked_adjective',(625,835,1640,1055),0,'Worked underlined adjective and entire cancelled clause, with quoted adjective below.'),
('c08_diamond',(340,1165,690,1380),0,'All four objects and all four sloping relation signs; no diagram target clipped.'),
('c09_upper_margin',(22,1135,475,1650),-38,'Entire oblique upper marginal note including its highest continuation and lowest final word.'),
('c10_definition_words',(780,1190,1645,1385),0,'Double-underlined contrée and modérée, with adjacent full sentence words.'),
('c11_definition_corrections',(260,1370,1640,1580),0,'Subdivisions, dense d\'une correction/repetition and complete cancelled Dans clause.'),
('c12_initial_c5',(250,1530,1450,1790),0,'Cancelled on a, punctuation, cancelled underlined C5 and donner/aucune gap.'),
('c13_ses_relations',(260,1765,1635,1975),0,'Cancelled tout, seul ending, ses/les relations and final straight order sign.'),
('c14_lower_margin',(22,1975,355,2340),-38,'Entire oblique Reporter note, C6/C7 tiny mark, ces, axiomes, disjonction and adjacent bars.'),
('c15_tte',(1030,1980,1660,2210),0,'Reduced word before figure G, with surrounding axiom words.'),
('c16_nb_formula',(310,2200,1520,2353),0,'Entire NB condition, overwritten G/F, X/x, membership and M, with line above.')]
rows=[]
for name,box,rotation,reason in specs:
 crop=im.crop(box)
 if rotation: crop=crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
 scale=2400/crop.width
 crop=crop.resize((2400,round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=ImageOps.autocontrast(crop).filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
 path=out/'crops'/f'{name}.jpg';crop.save(path,quality=94)
 rows.append({'path':str(path),'source':src,'bbox':list(box),'scale':scale,'rotation':rotation,'reason':reason,'transforms':'crop; rotate when nonzero with white expansion; resize LANCZOS to 2400 px; autocontrast; UnsharpMask(radius=1,percent=110,threshold=3); JPEG quality 94'})
(out/'crop_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(out/'inspection_log.md').write_text('# R2 inspection log — 156-4 scan 070\n\nStarted reading at 2026-11-20 11:00:52 UTC. Packet and brief were read in full. No OCR, outside research, other readers, or LaTeX compiler.\n\n1. Whole scan: '+src+' — viewed once, original, for layout.\n2. Upper supplied half: '+src.replace('.jpg','_a.jpg')+' — viewed once, original, every line compared with C and H.\n3. Lower supplied half: '+src.replace('.jpg','_b.jpg')+' — viewed once, original, every line compared with C and H. Lower half origin in whole is y=1099.\n\nOpen-locus list before crops: first relation/très/aura; cancelled noun; raised formula and en-phrase; dotted i.e./Subdivisions; repetition and F punctuation; subdivision ending and prime count; worked adjective and cancelled clause; diamond; oblique upper note; contrée/modérée; dense d\'une and cancelled Dans clause; cancelled on a/C5 and H\'s proposed extra deletion; seul/ses; oblique lower note and its tiny index; tte; NB correction and X/x.\n\nAll crop coordinates are on the whole image. Each listed crop was newly made by R2. Crops were made once per listed locus, with no recropping. Actual successful crop views are appended below.\n')
print('Created',len(rows),'own crops and initial inspection log.')
