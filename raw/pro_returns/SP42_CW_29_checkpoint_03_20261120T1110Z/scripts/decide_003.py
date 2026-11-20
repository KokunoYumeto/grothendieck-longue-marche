from adjudication_helpers import *
from datetime import datetime,timezone
scan=3
d,rs,ts=start(scan)
text=ts['R1'].replace('you developed things','you developped things').replace('of giving directly',r'of \unsure{giv\deleted{e}ing|giv\deleted{i}eng} directly')
# Every selected locus below was inspected by the main reader in the recorded crop.
map2={1:1,2:3,3:4,4:5,5:6,6:7,7:8,9:10,10:11,11:12,12:13,13:14,14:15,15:16,16:17,18:19,19:20,20:22,21:23,22:25,23:24,24:27,25:28}
maincrops={2:'01_first_r.jpg',6:'02_variations.jpg',7:'03_definition.jpg',15:'04_exclamation.jpg',16:'05_consists.jpg',24:'06_double_a.jpg'}
for i in [1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25]:
 r=row_from(rs['R1'],i)
 r['readers']={k:rs[k]['differences'][(map2[i] if k=='R2' else i)-1]['reading'] for k in rs}
 r['marked_in_H']=False
 if i in maincrops:r['crop']='crops/scan003/'+maincrops[i]
 elif i==1:r['crop']='readers/scan003/R3/crops/01_developed.png'
 elif i==23:r['crop']='readers/scan003/R3/crops/11_baseline_product.png'
 else:r['crop']=normal_crop(scan,'R1',r['crop'])
 r['scan_shows']=r['scan_shows'].replace('Half a:','Main crop:').replace('Half b:','Main crop:')
 if i==1:
  r.update(final='developped',against_c=True,against_h=False,confidence='high',scan_shows='Two separate p cells each have a stem, bowl and descender. The main crop supports R2 and R3 against R1 and C; the doubled p is retained.')
 if i==10:r['scan_shows']+=' Main inspection retains the taller initial C as first candidate, with lowercase still possible; the matched pointer fixes the insertion point. H has an editorial placement note, not an uncertainty flag.'
 if i==20:r['scan_shows']='Four separately typed dots follow cas, five follow etc, then a comma. Main inspection confirms their counts.'
 if i==22:
  r.update(c='....sauf si [formula], auquel cas.....',h='…sauf si [formula], auquel cas…',final='....sauf si [formula], auquel cas.....',scan_shows='The main crops show four leading periods before sauf and five after cas. This row concerns dot counts only; the intervening product is recorded separately.',crop='readers/scan003/R1/09_ellipsis.png; crops/scan003/06_double_a.jpg')
 if i==21:r['scan_shows']+=' R3 uses a block-producing figure wrapper; the final retains the inline TikZ correction so the mark remains over the typed uo.'
 d['rows'].append(r)
g=row_from(rs['R2'],2,crop='readers/scan003/R2/crops/02_giving.png')
g['readers']={'R1':'giving','R2':g['final'],'R3':'giving'}
g['scan_shows']='The cell after giv contains a curved e body and a tall i impression with its dot/foot. Main inspection confirms an overstrike overlooked by C, H, R1 and R3; the chronological order remains unestablished.'
d['rows'].insert(1,g)
# The following state details were inventoried by a reader but absent from all readings.
upperdot=r'\rlap{\handwritten{\raisebox{.55ex}{.}}}'
states=[
 ('itself:', 'itself'+upperdot+'.','15_itself_colon_corrected.jpg','paragraph 2, itself:','The lower round dot is black typed ink; an irregular blue dot has been added above it, completing a colon.'),
 ('commute;', 'commute'+upperdot+',','08_commute_semicolon.jpg','paragraph 2, commute;','The black typed comma retains its tail; a separate blue dot above completes a semicolon.'),
 ('Some other points:', 'Some other points'+upperdot+'.','10_points_colon.jpg','paragraph 3, points:','A small blue loop/dot is above the black typed period.'),
 ('$G(M)$;', '$G(M)$'+upperdot+',','11_gm_semicolon.jpg','paragraph 3, G(M);','A blue upper dot is above a black typed comma.'),
 ('Also you write:', 'Also you write'+upperdot+'.','12_write_colon.jpg','paragraph 3, write:','The upper dot has blue ink; the lower dot is black typed ink.'),
 ('revenant à la', r'revenant \handwritten{\`}{a} la','13_grave_first.jpg','paragraph 2, revenant à','The grave accent is an irregular descending blue stroke over a black typed a.'),
 ('correspondants à $X$',r'correspondants \handwritten{\`}{a} $X$','14_grave_second.jpg','paragraph 2, correspondants à','The grave accent consists of blue descending strokes above the black typed a.')]
for old,new,crop,place,evidence in states:
 assert old in text,old
 text=text.replace(old,new)
 d['rows'].append(dict(place=place,c=old,h=old,final=new,against_c=True,against_h=False,kind='insertion or placement',marked_in_H=False,confidence='high',scan_shows=evidence+' The C change records the hand-added component of a composite typed/handwritten character. H has the same resulting punctuation/accent, so its different encoding convention alone does not make a collation row.',crop='crops/scan003/'+crop,readers={k:old for k in rs}))
d['doubts']=rs['R1']['remaining_doubts']+[u for u in rs['R2']['remaining_doubts'] if 'giv' in u['reading']]
# Inventory ordered by first vertical position; the text-block rows precede their internal changes.
inv=[]
for x in rs['R3']['inventory']:
 if x['element'] in ['E11','E33']:continue
 x=dict(x);x['transcribed']='yes'
 if x['element']=='E19':x['first_words_or_objects']='isolated f crossed in blue (resolved from f/i)'
 if x['element']=='E13':x['first_words_or_objects']='Corresponding / with (initial case uncertain) and paired insertion markers'
 inv.append(x)
for kind in ['deletion','insertion']:
 inv.append(dict(sheet_kind='letter',hand='typewriter',element='',kind=kind,position='paragraph 1, giving directly',first_words_or_objects='superposed e/i in giving; correction order uncertain',transcribed='yes'))
for old,new,crop,place,evidence in states:
 inv.append(dict(sheet_kind='letter',hand='unnamed hand (blue ink)',element='',kind='insertion',position=place,first_words_or_objects=evidence,transcribed='yes'))
ys={'E01':150,'E02':200,'E03':270,'E04':330,'E05':800,'E06':1550,'E07':650,'E08':650,'E09':755,'E10':900,'E12':1145,'E13':1180,'E14':1245,'E15':1245,'E16':1300,'E17':1300,'E18':1440,'E19':1500,'E20':1500,'E21':1500,'E22':1500,'E23':1600,'E24':1640,'E25':1690,'E26':1690,'E27':1710,'E28':1750,'E29':1750,'E30':1800,'E31':1900,'E32':2000}
def y(x):
 if x['element'] in ys:return ys[x['element']]
 p=x['position']
 return 490 if 'giving' in p else 890 if 'itself' in p else 1245 if 'commute' in p else 1550 if 'points' in p else 1600 if 'G(M)' in p else 1700 if 'write' in p else 990 if 'revenant' in p else 1040
inv.sort(key=y)
for i,x in enumerate(inv,1):x['element']=f'E{i:02d}'
d['inventory']=inv
d['notes']=rs['R3']['notes']
d['notes']['content']=d['notes']['content'].split(' All words')[0]
d['notes']['math_reading_decisions']=[
 'The visible slanted lower stroke gives \\geqslant; this changes the encoded shape, not the mathematical relation. The proposed replacement retains the written baseline period and underlined multi-index letters (changes log, paragraph 3).',
 'Arithmetic distinction only (003-M01): for the one-component example n=2 and n′=3, n′≥n is true but n′=m.n has no positive-integer solution m. This confirms that the two written conditions differ. It does not verify the claimed Hom description or the surrounding Galois-covering theory.',
 'The group-letter alphabet and the case of the primed Hom subscript are not established by the ink and remain marked; no reading is selected from the expected theory.'
]
d['check_events']=[dict(statement_id='003-M01 (notes, arithmetic distinction)',date=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),who='GPT-6 Astra Pro; effort not exposed; main-reader run',type='computation or formal certificate',outcome='Direct integer calculation: 3>=2, whereas 3/2 is not an integer. This checks only inequality versus positive-integer divisibility, not the Hom formula.')]
d['slips']=['developped, apparantly, then, sheme, the typed shuold with its hand transposition mark, and the doubled a in is a a set are retained. No grammatical normalization is applied.']
d['workflow']=dict(brief='brief_v001_scan003.md',r1_crops=11,r2_crops=11,r3_crops=11,main_crops=15,feedback='Three independent readers viewed whole + two halves once each. Main inspected the recorded reader crops and made 15 additional crops: 14 targeted usable crops and one mispositioned attempt for itself, retained for audit. An overlarge eight-image output was truncated before inspection; the same files were subsequently viewed in smaller batches, not recreated. R1 missed a doubled p; R2 alone caught giving overtyping. R3 inventory identified hand-added punctuation/accents without encoding them, and misclassified the typed semicolon after conditions as handwritten; main inspection corrected those state records. Pure emphasis macro differences, editorial italics, and archive-page metadata were excluded from H collation. Brief v002 supplies PREAMBLE, clarifies uncertainty flags and inline drawings, insists on complete crop bounds and inventory/text consistency, and uses JPEG evidence to reduce package size.')
d['workflow']['main_reader_crops_viewed']=14
d['main_adjudication_complete']=True
save(d,text)
print(json.dumps({'scan':scan,'rows':len(d['rows']),'doubts':len(d['doubts']),'inventory':len(inv)}))
