import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-03',10,58);ch=r.change
r.edit(r'\unsure{Bourbaki}',r'\unsure{Bour}baki')
r.edit(r'\illegible{3})',r'\illegible{3}\unsure{)}')
r.edit('un groupe diagonalisable',r'un groupe diagonalis\unsure{a}ble')
ch('manuscript number','25','omitted','25','The rotated top-left inscription gives 2 followed by a larger angular 5; adjacent brown marks belong to the damaged paper strip.','number','omission')
ch('cancelled author name',r'\unsure{Bourbaki}','Bourbaki',r'\unsure{Bour}baki','B and partial round strokes remain at the right edge; the next line clearly starts baki below the heavy strike.','reference-right; reference-left','misread word','low',True,True)
ch('comma after cancelled author','absent','present','absent','No separate comma can be isolated after the visible i before Alg.; the cancellation passes across the area.','reference-left','other','medium')
ch('closing cancelled reference parenthesis',')',')',r'\unsure{)}','A small curved upper remnant remains next to the heavy terminal cancellation, but the body is obscured.','reference-close','misread symbol or index','low',True,True)
ch('Corollaire heading','underlined word only','bold word and number','underlined word only','The separate straight rule ends below the final e before the number begins.','corollary','other')
ch('dash after corollary number','absent','em dash','absent','The period after 18 is followed by whitespace and Soient; there is no dash.','corollary','text not on the page')
ch('first diagonalisable overtyped letter','a','a',r'\unsure{a}','The a after s has overlapping dark upper and lower loops; its underlayer cannot be separated securely.','diagonalisable','misread word','medium',True,True)
ch('Z-module letter',r'\text{\uline{Z}}',r'\mathbb{Z}',r'\text{\uline{Z}}','A single-stroke Z has a clearly separate lower underline, without a second diagonal or doubled stem.','Z','misread symbol or index','high',False,True,False,True)
ch('following editorial section heading','absent','Catégorie tannakienne de lien un groupe diagonalisable (pages 59 et 60)','absent','Both halves show a blank sheet below the cancelled corollary, apart from the archive folio. The following H section is editorial material outside this sheet.','whole and both halves','text not on the page')
r.doubt('cancelled author prefix','Bour','','low','The following baki is clear; prefix remains crossed out.')
r.doubt('cancelled reference after Alg. Comm.',r'\illegible{3}','','low','Estimated obscured word count only; no reference supplied from context.')
r.doubt('cancelled reference closing character',')','','low')
r.doubt('first diagonalisable, a after s','a','unresolved overtyped underlayer','medium')
r.notation('underlined integer letter',r'\text{\uline{Z}}','10/058 cancelled corollary','read')
r.r['crops']=json.loads(Path('work/crops058.json').read_text())
r.r['inspection_note']='Whole page and both halves read, including blank lower area. All text, accents, mathematical capitals, indices, limit and morphism arrows, punctuation and nested cancellation checked at enlargement. Reference and overtyped adjective enlarged separately. Numeral rotated. Large loop cancellation of the entire corollary and typed x cancellation of its inner phrase retained. Soient and the source spacing fpqc,c.q.f.d. retained. H editorial transition is not attributed to the sheet. No context opened or mathematical check performed.'
r.save('work/record058.json')
