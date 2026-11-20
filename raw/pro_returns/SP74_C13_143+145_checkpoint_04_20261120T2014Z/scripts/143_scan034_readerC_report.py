from pathlib import Path
from decimal import Decimal
import json,re
root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
p=json.loads((root/'reader_packets/143_scan034.json').read_text())
C=p['witness_C']
assert p['witness_H'] is None and p['differences']==[]
rows=re.findall(r'^(0\.\d{4})&([^&]+)&([^&]+)&',C,re.M)
assert len(rows)==62,len(rows)
assert Decimal('39.1337')-Decimal('12.7459')==Decimal('26.3878')
boxes={'delta-u-statement':[1150,1320,1630,1405],'u-m-statement':[1200,1220,1635,1310],'first-arithmetic':[165,755,405,925]}

def decision(mid,place,ink):
 return dict(id=mid,decision='undecided',reading=r'\unsure{\mathrm{m/s}|\mathrm{m/o}}',ink=ink,crop=f'crops/143_scan034_readerC_{place}.png',box=boxes[place],confidence='medium')
decisions=[
 decision('M0751','delta-u-statement','After the cursive m and slash, the terminal character is a low closed loop with a short leading stroke. It can be a compressed cursive s or an o-like letter; no independent upper s lobe settles it. The unit role supports s as preferred but does not erase the graphic alternative.'),
 decision('M0752','u-m-statement','The terminal unit character again consists of a small loop with a left entry stroke after the slash. Its form matches the preceding unit closely, and both s and o remain possible on the ink. No expected-unit completion is supplied.')
]

inventory=[
 dict(sheet_kind='computer printout with handwritten annotations',hand='machine print; producer not identified',element='E01',kind='display',position='Top of print in the 180-degree reading orientation; original bottom edge',first_words_or_objects='Three header rows: 12 asterisks with 0.0000; 12 with 10 asterisks; 12 with 10 asterisks; then 75.000',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='machine print; producer not identified',element='E02',kind='display',position='Left side in reading orientation; original right side',first_words_or_objects='62 three-column numeric rows, from 0.0307 / 20.4842 / 0.9297 to 0.0389 / 24.6183 / -0.4818',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='unnamed hand (blue ink)',element='E03',kind='insertion',position='Beside the middle-column values on the 0.0347 and 0.0349 rows',first_words_or_objects=') max, spanning the two occurrences of 39.1337',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='unnamed hand (blue ink)',element='E04',kind='display',position='To the right of the numeric table, near rows 0.0335–0.0337 in reading orientation',first_words_or_objects='ΔU = 26.3878 m/s|m/o',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='unnamed hand (blue ink)',element='E05',kind='display',position='Below the ΔU statement, near row 0.0339 in reading orientation',first_words_or_objects='U_m = 25.939 m/s|m/o; m heavily retraced',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='unnamed hand (blue ink)',element='E06',kind='display',position='Farther right and lower, near the table rows 0.0355–0.0359 in reading orientation',first_words_or_objects='39.1337 / 12.7459 / horizontal rule / 26.3878',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='unnamed hand (blue ink)',element='E07',kind='display',position='Below the first arithmetic stack, near rows 0.0362–0.0366 in reading orientation',first_words_or_objects='12.7459 / 13.1939 / horizontal rule / 25.9398',transcribed='yes'),
 dict(sheet_kind='computer printout with handwritten annotations',hand='unnamed hand (pencil)',element='E08',kind='margin note',position='Original bottom left; opposite orientation to the print and blue notes',first_words_or_objects='33',transcribed='yes')
]

report=dict(
 key='143_scan034',reader='C',stage='first',image_views=['original','half1','half2'],changes=[],decisions=decisions,inventory=inventory,
 remaining_doubts=[
 dict(place='ΔU statement unit, M0751',reading=r'\unsure{\mathrm{m/s}|\mathrm{m/o}}',alternatives='m/s / m/o',confidence='medium',reason='The final letter is a small closed loop with an entry stroke; it admits cursive s and o. The unit interpretation does not uniquely establish the physical letter.'),
 dict(place='U_m statement unit, M0752',reading=r'\unsure{\mathrm{m/s}|\mathrm{m/o}}',alternatives='m/s / m/o',confidence='medium',reason='The same looped terminal form recurs. It remains unresolved for the same graphic reason as M0751.')
 ],
 certainty_resolutions=[],
 notation=[
 dict(form='Three-column decimal printout',meaning='Column roles are not named on this sheet.',evidence='All 62 rows were read directly from the native-resolution rotated half. No headings, function names or explanatory units are added to the printed columns.'),
 dict(form=r'\Delta U',meaning='The first handwritten reported quantity.',evidence='A triangular Delta is followed by an open U bowl; the numeric value reads 26.3878.'),
 dict(form=r'U_m',meaning='The second handwritten reported quantity.',evidence='The subscript is a heavily retraced three-stroke m. No separately readable canceled letter is visible beneath it. The written value ends at 25.939.'),
 dict(form=r'\unsure{\mathrm{m/s}|\mathrm{m/o}}',meaning='Both handwritten unit strings retain the same terminal-letter uncertainty.',evidence='Each ending is looped and can be read as compressed cursive s or o; the equation crops preserve the comparison.'),
 dict(form=') max',meaning='Blue annotation spanning the two equal middle-column values 39.1337.',evidence='A tall closing-parenthesis guide extends across the 0.0347 and 0.0349 rows, with max written at its middle.'),
 dict(form='Unlabeled arithmetic rules',meaning='The two handwritten stacks contain horizontal rules without explicit plus or minus signs.',evidence='The source places three decimal numbers vertically with a separating rule. Operator signs have not been inserted from the implied arithmetic.')
 ],
 abbreviations=[dict(form='max',expansion='maximum')],
 hand_log=[
 dict(habit='A small cursive terminal s can be looped enough to resemble o.',places='143_scan034 two handwritten unit strings',scope='Both occurrences inspected in separate tight crops; neither fully resolves the letter.',misreadings='C already preserves m/s|m/o at M0751 and M0752; neither alternative is suppressed.'),
 dict(habit='Small 3 can have a very weak or flattened middle indentation; 9 can have an open or short upper bowl.',places='143_scan034 U_m value, both arithmetic stacks',scope='Every handwritten decimal inspected; the U_m and first arithmetic crops specifically checked reduced digit forms.',misreadings='No material digit correction found. The source difference 25.939 versus 25.9398 is preserved.'),
 dict(habit='Handwritten 7 carries a transverse stroke, while 1 can have a short entry stroke near the upper part of its stem.',places='143_scan034 first arithmetic stack and handwritten numeric statements',scope='The first decimal digit of 39.1337 was compared with the final crossed 7 and nearby handwritten 1 forms.',misreadings='The leading post-decimal digit favors C’s 1; it lacks the distinct top sweep of the crossed 7. The written subtraction result also agrees with that reading.'),
 dict(habit='Heavy retracing does not by itself identify a canceled prior character.',places='143_scan034 U_m subscript',scope='One heavily retraced m inspected in the formula crop.',misreadings='No deleted layer is invented below the visible m.'),
 dict(habit='Opposite writing orientation can identify a separate annotation event without identifying its writer.',places='143_scan034 pencil 33 versus print and blue notes',scope='The full original was inspected before native halves were rotated for reading.',misreadings='The pencil numeral remains attributed to an unnamed hand; no authorship is inferred.')
 ],
 notes=[
 dict(id='143_scan034-N1',text='This sheet is a computer printout with blue handwritten annotations. The print and blue notes are upside down in the supplied scan; the pencil 33 has the opposite orientation. The original was viewed once. Each existing native half was then rotated losslessly by 180 degrees, without rescaling, for its first and only detailed view. The three subsequent tight crops were also rotated by 180 degrees after extraction from their recorded original-image boxes.'),
 dict(id='143_scan034-N2',text='The print has three initial rows of asterisks and a visible 0.0000, followed by 75.000 and 62 rows of three decimal values. The first column runs from 0.0307 to 0.0389. Every number, sign and decimal point was read against C, including the sign transition at the 0.0333/0.0334 rows and the -1.0000 value at 0.0366. No numeric correction to C was found. The source does not name the columns.'),
 dict(id='143_scan034-N3',text='The blue max annotation has a closing-parenthesis guide across both printed 39.1337 values, on rows 0.0347 and 0.0349. The separate blue statements read ΔU=26.3878 and U_m=25.939, each followed by the unresolved m/s|m/o unit string. The shortened 25.939 is kept even though the separate addition stack ends at 25.9398.'),
 dict(id='143_scan034-N4',text='The first arithmetic stack writes 39.1337 above 12.7459, a rule, and 26.3878. The second writes 12.7459 above 13.1939, a rule, and 25.9398. No operator signs occur beside either stack, so none are supplied. A narrow decimal subtraction check was used only to corroborate the ambiguous-looking first post-decimal digit in the first stack; it did not substitute calculated text for the visible numerals.'),
 dict(id='143_scan034-N5',text='The candidate retains C’s transcription and its order of the separate annotation blocks. The inventory records their physical positions to the right of the table. The printer producer and the blue and pencil writers are not identified by evidence on this page. Paper folds, holes and isolated background specks are not transcribed as source writing.')
 ],
 check_events=[
 dict(statement_id='143_scan034-N2',type='carried as background without fault found',outcome='Visually collated all 62 printed data rows, three header rows, 75.000 and the max attachment against C. This is a reading check, not a reconstruction or validation of the program that generated the values.'),
 dict(statement_id='143_scan034-N3',type='carried as background without fault found',outcome='Checked both written quantities and their unit graphs in separate tight crops. No physical model, unit conversion or derivation was assumed; the source’s 25.939 versus 25.9398 difference remains.'),
 dict(statement_id='143_scan034-N4',type='computation or formal certificate',outcome='Using exact decimal arithmetic, checked that Decimal("39.1337") - Decimal("12.7459") equals Decimal("26.3878"). This corroborates the preferred 1 among the locally similar 1/7 forms in the first stack. All three numbers were first read from ink; no number was completed from the calculation.'),
 dict(statement_id='143_scan034-N4-second-stack',type='carried as background without fault found',outcome='Read the three numbers and horizontal rule of the second arithmetic stack from the native half. No operator sign was supplied, and this report does not treat the page’s larger numerical model as proved.')
 ],
 unresolved_for_main=[
 'M0751 remains m/s|m/o: crops/143_scan034_readerC_delta-u-statement.png, original box [1150,1320,1630,1405], rotated 180 degrees.',
 'M0752 remains m/s|m/o: crops/143_scan034_readerC_u-m-statement.png, original box [1200,1220,1635,1310], rotated 180 degrees.',
 'For review of the first arithmetic digit retained as 1, crops/143_scan034_readerC_first-arithmetic.png, original box [165,755,405,925], rotated 180 degrees. The leading reading is 39.1337; no new uncertainty has been introduced after the stroke comparison and narrow subtraction corroboration.',
 'No material correction to C was found. The two unit uncertainties remain; numerical differences between the formula and the separate stack are deliberately unregularized.'
 ],
 raw_difference_disposition='Witness H is absent, so there are no packet C/H differences and no against-H claims. C was read throughout against the image: all 62 three-column numeric rows, all initial asterisk/number rows, the two-row max guide, both handwritten formulas, both arithmetic stacks and pencil 33. The candidate retains C unchanged; therefore changes is empty. Both original MARKS remain undecided in their original order. The 3 tight crops were each viewed once. The two additional files named native-half1-rot180 and native-half2-rot180 are lossless rotations of the existing native halves, not extra crops or repeated image inspections. No OCR, research or TeX compilation was performed.'
)
assert [d['id'] for d in report['decisions']]==[m['id'] for m in p['marks']]
assert all(d['reading'] in C for d in report['decisions'])
for name in boxes: assert (work/'crops'/f'143_scan034_readerC_{name}.png').is_file()
(work/'reviews/143_scan034_readerC.tex').write_text(C)
(work/'reviews/143_scan034_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate':str(work/'reviews/143_scan034_readerC.tex'),'report':str(work/'reviews/143_scan034_readerC.json'),'data_rows':len(rows),'material_changes':0,'original_marks':2,'inventory':len(inventory),'tight_crops':3,'unit_doubts_retained':2},ensure_ascii=False,indent=2))
