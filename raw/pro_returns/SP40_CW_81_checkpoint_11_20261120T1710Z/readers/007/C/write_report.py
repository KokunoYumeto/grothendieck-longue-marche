from pathlib import Path
import json

root = Path('/workspace/scratch/94548b74fbe0/out/readers/007/C')
inventory_specs = [
 ('007.C.01','deletion','top left before Soit','blacked-out unreadable item','another unnamed hand'),
 ('007.C.02','text','first line','Soit a∈ℕ* … q nombre premier (q≠1)','another unnamed hand'),
 ('007.C.03','text','second line with right-hand parenthesis','On suppose que … premiers entre eux deux à deux','another unnamed hand'),
 ('007.C.04','insertion','left between second and third lines','et a^q+b^q=c^q','another unnamed hand'),
 ('007.C.05','text','upper section, below insertion','On a c>a et c>b car …','another unnamed hand'),
 ('007.C.06','text','above binomial expansion','On pose c=a+b′=b+a′ …','another unnamed hand'),
 ('007.C.07','display','upper middle, two lines','alors a^q+b^q=c^q=… (Newton); =b′^q+…','another unnamed hand'),
 ('007.C.08','display','below expansion, label (1)','donc b^q=Σ…+b′^q (1)','another unnamed hand'),
 ('007.C.09','text','three lines above fold','la puissance de b′ n’étant jamais nulle … (b′ divise b^q)','another unnamed hand'),
 ('007.C.10','text','across fold','Soit p un nombre premier … et tel que :','another unnamed hand'),
 ('007.C.11','deletion','between premier and et tel que','ou p=1, crossed by two rising strokes','another unnamed hand'),
 ('007.C.12','text','immediately beneath fold','p|b′ donc p|b. Soit α∈ℕ* et α′∈ℕ* tels que','another unnamed hand'),
 ('007.C.13','display','middle lower, two divisibility pairs','p^α′|b′ et p^(α′+1)∤b′; et p^α|b et p^(α+1)∤b','another unnamed hand'),
 ('007.C.14','margin note','pale two-line note at right of divisibility pairs','a/α n’exist/n’existe pas si on avait p=1','undetermined hand'),
 ('007.C.15','text','right of second divisibility pair','On a α′≤qα car b′|b^q','another unnamed hand'),
 ('007.C.16','display','lower third, two implications','(1)⇒p^(qα)|Σ…; ⇒p^(qα)|b′(Σ…) (car q≥2)','another unnamed hand'),
 ('007.C.17','text','above last three implications','posons b′=p^α′b″ donc b″ bowl/1 p (propriété de α′)','another unnamed hand'),
 ('007.C.18','display','foot, three implications','⇒p^(qα)|p^α′b″(…); ⇒p^(qα−α′)|b″(…); ⇒p^(qα−α′)|Σ…','another unnamed hand'),
 ('007.C.19','text','lower left, pencil archive numeral','6; represented only by archive-number comment','undetermined hand'),
]
inventory = [dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes') for element,kind,position,words,hand in inventory_specs]

report = {
 'scan':7,
 'reader':'C',
 'start_utc':'2026-11-20 11:08:19 UTC',
 'end_utc':None,
 'full_image_viewed':True,
 'halves_viewed':True,
 'complete_visual_read':True,
 'differences':[
  {
   'id':'007-C-01',
   'location':'Opening black cancellation immediately before Soit',
   'C':r'\deleted{\illegible{1}}',
   'H':None,
   'reading':r'\deleted{\illegible{1}}',
   'evidence':'The enlarged black patch contains dense overlapping loops, short top projections and a rounded lower outline. No internal character sequence can be recovered. The original unreadability is retained; one placeholder denotes the single compact unreadable item.',
   'confidence':'low',
   'kind':'other',
   'diff_C':False,
   'diff_H':False,
   'C_doubt_status':'retained',
   'readers_crop':'01_top_cancel.png',
   'bbox':[22,18,180,94]
  },
  {
   'id':'007-C-02',
   'location':'Pale marginal note, initial character',
   'C':r'\unsure{a|\alpha}',
   'H':None,
   'reading':r'\unsure{a|\alpha}',
   'evidence':'The complete pale note was enlarged. Its initial character has a low oval at left and a rightward descending tail. The strokes support the existing a and alpha candidates without settling their choice; a remains first.',
   'confidence':'medium',
   'kind':'other',
   'diff_C':False,
   'diff_H':False,
   'C_doubt_status':'retained',
   'readers_crop':'04_pale_note.png',
   'bbox':[1006,961,1326,1053]
  },
  {
   'id':'007-C-03',
   'location':'Pale marginal note, ending of n’exist / n’existe',
   'C':r'\unsure{n\'exist|n\'existe}',
   'H':None,
   'reading':r'\unsure{n\'exist|n\'existe}',
   'evidence':'After n and its apostrophe, the word ends in a tall stem with a short rightward curved continuation. The continuation has insufficient independent structure to settle the presence of a final e. Retain n’exist first and n’existe as the supported alternative. The two uncertainty-table entries in C_doubts concern this single locus.',
   'confidence':'medium',
   'kind':'other',
   'diff_C':False,
   'diff_H':False,
   'C_doubt_status':'retained',
   'readers_crop':'04_pale_note.png',
   'bbox':[1006,961,1326,1053]
  }
 ],
 'doubts':[
  {'location':'Opening black cancellation','reading':r'\deleted{\illegible{1}}','alternatives':[],'confidence':'low','reason':'Dense overlapping ink prevents recovery of a character sequence.','crop':'01_top_cancel.png'},
  {'location':'Pale note, initial character','reading':'a','alternatives':[r'\alpha'],'confidence':'medium','reason':'Low oval and falling right tail support both existing shapes.','crop':'04_pale_note.png'},
  {'location':'Pale note, word ending','reading':"n'exist",'alternatives':["n'existe"],'confidence':'medium','reason':'Terminal tall stroke and short rightward continuation do not settle a separate final e.','crop':'04_pale_note.png'},
 ],
 'inventory':inventory,
 'notes':{
  'page_content':'Handwritten arithmetic argument beginning Soit a∈ℕ* and introducing a prime q, pairwise bowl/1 signs, the interlinear equality a^q+b^q=c^q, a binomial expansion, the numbered expression (1), divisibility pairs and a final implication chain. This describes the written content only.',
  'author_own_uncertainty':{'exact_words':None,'comment':'No explicit authorial words of uncertainty were observed. Editorial uncertainty remains at the opening cancellation and two loci in the pale note.'},
  'pale_note_exact_reading':r'\unsure{a|\alpha} \unsure{n\'exist|n\'existe} pas si on avait p=1',
  'title_date_page_counts':{'title':None,'date':None,'manuscript_page_number':None,'archive_sheet_number':'6','scan_pages_read':1},
  'mathematics_led_reading_decisions':'No mathematical derivation was used to choose or repair ink. The comparison marks, summation limits, primes and dotted i forms were read from their visible strokes.',
  'source_status':{'C':'Complete supplied witness, visually checked throughout','H':'nothing; H has no full text and contributes no collation rows'},
  'view_attestation':{'whole_views':1,'half_a_views':1,'half_b_views':1,'crop_views':6,'crops_created':6,'no_recrops':True,'whole_dimensions':[1405,1720],'half_dimensions':[1405,940],'half_a_full_scan_origin':[0,0],'half_b_full_scan_origin':[0,780]},
  'actual_order':'Read brief; recorded current UTC start; read assigned packet, notation snapshot and preamble; checked image dimensions; viewed whole once; viewed a once; viewed b once; read crop helper; made six crops; viewed each crop once; wrote and cross-checked local outputs.',
  'visual_resolutions_without_witness_difference':[
   'Crop 02: main comparison angle plus separate lower oblique stroke supports C’s geqslant.',
   'Crop 03: mark left below the summation is the dot above the lower-limit i; all upper and lower limits agree with C.',
   'Crop 05: crowded lower-limit i, coefficient indices and two exponent minus strokes agree with C; the dot under the sum belongs to i.',
   'Crop 06: the mark above the a factor is the dot of its raised i; the last bowl/1 sign and double prime are visible.'
  ],
  'physical_marks':'Opening black cancellation; two rising cancellation strokes over ou p=1; interlinear et a^q+b^q=c^q; pale two-line marginal note; archive pencil 6. The remaining small dots inspected are constituents of dotted i forms. No independent drawing or diagram was observed.',
  'crop_bounds':'All intended crop targets retain complete ink bounds. Crops 05 and 06 intersect incidental neighboring-line fragments; crop 04 includes tips of adjacent darker writing. Those peripheral fragments are not used as evidence for the target readings.',
  'independence':'No other reader or other page was read. No OCR, internet, external source, or delegation was used.'
 },
 'notation':[
  {'location':'Top line and conditions on b′, a′, α, α′','sign':'Doubled left N strokes with a raised star','latex':r'\mathbb N^*'},
  {'location':'Second line and both lower coprimality expressions','sign':'Shallow bowl with separate hooked 1 below','latex':r'\mathrel{\underset{1}{\smile}}'},
  {'location':'All expansions and sums','sign':'C with dotted i above and q below; summation with independently placed limits','latex':r'C_q^i,\sum_{i=1}^{q-1}'},
  {'location':'Upper comparison and lower implication comments','sign':'Main angle with a separate oblique lower stroke','latex':r'\geqslant'},
  {'location':'Right of second divisibility pair','sign':'Left-pointing angle with separate lower oblique stroke','latex':r'\leqslant'},
  {'location':'Divisibility pairs','sign':'Long vertical stroke; crossed form with diagonal stroke','latex':r'\mid,\nmid'},
  {'location':'Implication chain','sign':'Two horizontal strokes with right-pointing head','latex':r'\Longrightarrow'},
  {'location':'Introduced exponents and later powers of p','sign':'Curled alpha, separate raised prime stroke on alpha-prime','latex':r"\alpha,\alpha'"},
  {'location':'Definition of b′ and final lines','sign':'One or two separate short raised strokes after b','latex':"b',b''"},
  {'location':'Numbered sum and final two rows','sign':'Separated dot plus short lower stem in i; last raised i dot is high above a','latex':'i'},
 ],
 'check_events':[],
 'crops':[
  {'path':'01_top_cancel.png','bbox':[22,18,180,94],'rotation':0,'purpose':'Initial cancelled mark and adjoining Soit'},
  {'path':'02_upper_comparison.png','bbox':[929,408,1212,515],'rotation':0,'purpose':'Upper parenthetical car q comparison 2'},
  {'path':'03_numbered_sum.png','bbox':[271,521,958,632],'rotation':0,'purpose':'Numbered sum, small dot left of summation and complete indices'},
  {'path':'04_pale_note.png','bbox':[1006,961,1326,1053],'rotation':0,'purpose':'Complete two-line pale note, initial character and word ending'},
  {'path':'05_crowded_sum.png','bbox':[395,1487,991,1590],'rotation':0,'purpose':'Crowded penultimate summation, indices and extra local marks'},
  {'path':'06_final_sum.png','bbox':[235,1574,1184,1673],'rotation':0,'purpose':'Final expression, small indices and detached mark'},
 ],
 'brief_feedback':[
  'The opening black cancellation has no surviving word boundary. The existing illegible{1} is retained to designate one compact unreadable item, without claiming recovery of a one-word text.',
  'C_doubts repeats the n’exist/n’existe uncertainty in two rows; the report records one local decision for that physical locus.'
 ]
}

# Literal apostrophes in the prose doubt must agree exactly with reading.tex.
for row in report['differences']:
    if row['id']=='007-C-03':
        row['C']=row['reading']="\\unsure{n'exist|n'existe}"
report['notes']['pale_note_exact_reading']="\\unsure{a|\\alpha} \\unsure{n'exist|n'existe} pas si on avait p=1"
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
