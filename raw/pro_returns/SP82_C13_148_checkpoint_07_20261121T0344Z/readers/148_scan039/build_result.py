import csv
import json
import re
from pathlib import Path

BASE = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan039')
PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan039')
plan_list = json.loads((BASE/'crop_plan.json').read_text())
plan = {x['label']:x for x in plan_list}
c = (PACKET/'C.tex').read_text()
h = (PACKET/'H.tex').read_text()
candidate = (BASE/'candidate.tex').read_text()
marks = list(csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t'))
changes=[]
unresolved=[]

def change(place,c_,h_,final,ink,label,confidence='high',kind='misread word',
           against_c=False,against_h=True,math=False,mark_ids=None):
    evidence=plan[label] if label!='page' else {'crop':'page','box':[0,0,1540,2252]}
    row=dict(place=place,c=c_,h=h_,final=final,ink=ink,crop=evidence['crop'],
             box=evidence['box'],confidence=confidence,kind=kind,
             against_c=against_c,against_h=against_h,math=math)
    if mark_ids:
        row['mark_ids']=mark_ids
    changes.append(row)

change('first line: heavy horizontal mark before e1','','',
       r'\unsure{\deleted{\illegible{1}}|---}',
       'A short, dense horizontal patch lies between base and the first e1. Its uneven thick edges favour an obliteration, but no underletters certify cancellation rather than a heavy dash. Both states are retained in doubt without supplying a former letter.',
       'firstline',confidence='medium',kind='omission',against_c=True)
change('second line: live verb change',
       r'\unsure{change}','change','change',
       'The single verb retains an initial c, the tall h, low a-n joins, a g with its long lower loop and an e before the terminal dark patch. The surviving word is change.',
       'opening_edit',kind='other',against_c=True,against_h=False,mark_ids=['M0526'])
change('second line: scope of opening corrections',
       r'\deleted{revient à changer \unsure{par}} \unsure{change}',
       r'\struck{revient à changer} \struck{\ill{}} change',
       r'\deleted{revient à} change\deleted{\unsure{r}} \deleted{\unsure{par}}',
       'The first strike ends after revient à. The following change is the only occurrence of that verb; a separate dense patch covers its final remnant, tentatively r. The p-led word to its right has its own strike. There is no second complete changer or change elsewhere on the line.',
       'opening_edit',confidence='medium',kind='deletion state',against_c=True)
change('second line: separately cancelled word after change',
       r'\deleted{\unsure{par}}',r'\struck{\ill{}}',r'\deleted{\unsure{par}}',
       'The short cancelled word has a descending p stem and low rounded strokes under the horizontal strike. Par remains a tentative reading; the last joins are not fully exposed.',
       'opening_edit',confidence='medium',kind=r'readable ink left as \ill{}')
change('second paragraph: state of rigidifiées',
       r'\uline{rigidifiées}',r'\struck{\uncertain{rigidifiées}}',r'\uline{rigidifiées}',
       'The long horizontal line lies below the letter bodies and crosses only the descending g and f strokes. The word remains live and underlined.',
       'rigidifiees',kind='deletion state')
change('second paragraph: doubled projective P',
       r'\mathbb P^1\setminus\{0,\pm2,\infty\}',
       r'\mathbf P^1\setminus\{0,\pm2,\infty\}',
       r'\mathbb P^1\setminus\{0,\pm2,\infty\}',
       'The P has two distinct parallel vertical stems beneath its upper bowl. The raised 1, set-difference stroke and full excluded set 0, plus-or-minus 2, infinity were read together.',
       'projective',kind='misread symbol or index',math=True)
change('second paragraph: supposed stop after the projective formula',
       r'\mathbb P^1\setminus\{0,\pm2,\infty\}.',
       r'\mathbf P^1\setminus\{0,\pm2,\infty\}.',
       r'\mathbb P^1\setminus\{0,\pm2,\infty\}',
       'The closing brace is followed by blank paper. No independent full stop is visible after it before the next manuscript line begins Elle.',
       'projective',kind='text not on the page',against_c=True)

first_print=c.index(r'\unsure{\texttt{000000}}')
diag1=c.index(r'\diagram{',first_print)
diag2=c.index(r'\diagram{',diag1+1)
jobstart=c.index(r'\texttt{****A START',diag2)
datestart=c.index(r'\texttt{DERNIERE',jobstart)
folio=c.index(r'\mspage{38}',datestart)
prefix=c[first_print:diag1].strip()
table1=c[diag1:diag2].strip()
table2=c[diag2:jobstart].strip()
jobs=c[jobstart:datestart].strip().split('\n\n')
assert len(jobs)==6
date_line=c[datestart:folio].strip()

change('reverse printing: preliminary digit run',prefix,'','',
       'The pale blue fixed-pitch run belongs to the same laterally reversed printing as the large banner below. It is not dark front-side handwriting or front-side print.',
       'bleedthrough',kind='text not on the page',against_c=True,against_h=False,
       mark_ids=['M0527','M0528'])
change('reverse printing: large digit banner',table1,'','',
       'The regular pale blue character rows form a reverse-side banner behind the dark handwritten equations. Their orientation follows the mirrored listing; they are not a front-side mathematical array.',
       'bleedthrough',kind='text not on the page',against_c=True,against_h=False,
       mark_ids=[f'M{n:04d}' for n in range(529,565)])
change('reverse printing: large letter banner',table2,'','',
       'The block letters are constructed from pale blue machine characters. The L and P forms and their reading direction are laterally reversed, unlike the dark manuscript above them. They are not a source diagram.',
       'bleedthrough',kind='text not on the page',against_c=True,against_h=False,
       mark_ids=[f'M{n:04d}' for n in range(565,613)])
for n,job in enumerate(jobs,1):
    change(f'reverse printing: repeated job row {n}',job,'','',
           'This pale blue fixed-pitch row runs in the reversed direction shared by the other job rows and the banner. Its letters belong to printing showing through the sheet, not to the front-side manuscript; the C illegible span is therefore removed rather than called unreadable source text.',
           'bleedthrough',kind='text not on the page',against_c=True,against_h=False,
           mark_ids=[f'M{612+n:04d}'])
change('reverse printing: update-date row',date_line,'','',
       'The update line is pale blue, mechanically aligned and laterally reversed like the job rows. It supplies no front-side manuscript date.',
       'bleedthrough',kind='text not on the page',against_c=True,against_h=False)
heading=re.search(r'\\section\{Catalogue.*?\n',h).group(0).strip()
change('terminal Catalogue heading in H','',heading,'',
       'The current sheet has the two handwritten paragraphs, its foliation and otherwise blank lower paper. The Catalogue heading is absent. H itself assigns that heading to its following page.',
       'page',kind='text not on the page')
change('bottom-left foliation',r'\mspage{38}','',r'\margin{38}',
       'The light handwritten number has a double-curved 3 followed by an 8 with two joined loops. It stands separately at the lower left; no author page number appears at the head of this sheet.',
       'folio38',kind='omission')

decisions=[]
for mark in marks:
    if mark['id']=='M0526':
        decisions.append(dict(id=mark['id'],decision='first',reading='change',
                              ink='The surviving c-h-a-n-g-e sequence is visible in the single verb on the line, with a separate dark cancellation at its end. The g has a long lower loop and the final e precedes the patch.',
                              crop=plan['opening_edit']['crop'],box=plan['opening_edit']['box'],
                              confidence='high'))
    else:
        n=int(mark['id'][1:])
        if n<=528:
            location='the preliminary machine-character run'
        elif n<=564:
            location='the pale machine-character digit banner'
        elif n<=612:
            location='the pale machine-character letter banner'
        else:
            location=f'repeated machine job row {n-612}'
        decisions.append(dict(id=mark['id'],decision='other',reading='',
                              ink=f'This mark represents {location}. The characters are pale blue, regularly spaced and laterally reversed with the surrounding listing. They are reverse-side bleed-through, not front-side source text; no illegibility is asserted.',
                              crop=plan['bleedthrough']['crop'],box=plan['bleedthrough']['box'],
                              confidence='high'))

def doubt(place,reading,issue,alternatives,label,confidence):
    p=plan[label]
    unresolved.append(dict(place=place,reading=reading,issue=issue,alternatives=alternatives,
                           confidence=confidence,crop=p['crop'],box=p['box']))
doubt('first line: ambiguous mark before e1',
      r'\unsure{\deleted{\illegible{1}}|---}',
      'The short thick patch does not expose underlying letters. A cancelled unread fragment is favoured, but a heavy dash cannot be excluded. No former word or character count is asserted.',
      [r'\deleted{\illegible{1}}','---'], 'firstline','medium')
doubt('second line: cancelled terminal remnant of change',
      r'\deleted{\unsure{r}}',
      'A dense patch follows the readable change. A cancelled r would account for the old changer reading, but the letter itself is not fully recoverable.',
      ['r','unidentified cancelled ending'], 'opening_edit','low')
doubt('second line: separately cancelled short word',
      r'\deleted{\unsure{par}}',
      'The strike obscures the interior joins. The visible descending p and low rounded run admit par, without exposing every letter.',
      ['par'], 'opening_edit','medium')

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position=position,
                          first_words_or_objects=first,sheet_kind='reused_typed',
                          hand=hand,transcribed='yes'))
inv('opening base-change statement','text','first manuscript line',r'Changer la base e_1 en \zeta e_1')
inv('ambiguous heavy mark before e1','text','first line between base and e1',r'\unsure{\deleted{\illegible{1}}|---}')
inv('fourth-root condition','display','right end of first line',r'\zeta^4=1')
inv('cancelled opening phrase','deletion','left of second line','revient à')
inv('retained verb','text','second line after the first cancellation','change')
inv('cancelled terminal remnant','deletion','at end of change','r')
inv('separately cancelled word','deletion','between change and the first set','par')
inv('unordered-pair transformation','display','second line',r'\{\xi,\eta\} en \{\zeta^2\xi,\zeta^2\eta\}')
inv('mu transformation and its two cases','text','third through fifth manuscript lines',r'donc \mu en \zeta^2\mu')
inv('modular multiplicity paragraph','text','sixth through eighth manuscript lines','La multiplicité modulaire pour les structures envisagées')
inv('underlined qualification','text','seventh manuscript line','rigidifiées')
inv('punctured projective-line formula','display','right part of eighth manuscript line',r'\mathbb P^1\setminus\{0,\pm2,\infty\}')
inv('map and fundamental-groupoid question','text','ninth through eleventh manuscript lines',r'Elle s’envoie dans la multiplicité M_{0,5}')
inv('bottom foliation','margin note','bottom left','38','another unnamed hand')

notes=[]
def note(id_,kind,text,place,status='observed'):
    notes.append(dict(id=id_,statement_id=id_,kind=kind,text=text,place=place,status=status))
note('S039-C01','claim',
     r'The text states that replacing the base e_1 by zeta e_1, with zeta^4=1, changes {xi,eta} into {zeta^2 xi,zeta^2 eta} and mu into zeta^2 mu.',
     'first paragraph','transcribed; the basis-to-coordinate transformation was not derived here')
note('S039-C02','claim',
     r'The transformed mu equals mu for zeta in {+1,-1} and equals -mu for zeta in {+i,-i}.',
     'first paragraph','the four stated substitutions were checked')
note('S039-C03','claim',
     r'The modular multiplicity for the structures rigidified by e_1 is written as P^1 minus {0,+2,-2,infinity}.',
     'second paragraph','transcribed, not mathematically checked')
note('S039-C04','claim',
     r'This multiplicity maps to M_{0,5}; the text proposes examining the effect on fundamental groupoids.',
     'last three manuscript lines','transcribed, not mathematically checked')
note('S039-N01','source layer',
     'The pale blue machine characters, banners, repeated job rows and date-like row are laterally reversed. They are printing showing through reused listing paper and are excluded from the front-side transcription. The 92 associated C mark IDs remain individually accounted for as other with empty readings.',
     'reverse-print layer')
note('S039-N02','date',
     'No authorial date is written on this face. C’s update-date string belongs to the reverse printing and is not used to date the manuscript.',
     'whole sheet')
note('S039-N03','wrong-page inclusion',
     'H appends a Catalogue heading that its own note assigns to its following page. That heading does not appear anywhere on scan039 and is omitted here.',
     'terminal H section')
note('S039-N04','deletion scope',
     'The source contains only one change/changer verb in the opening correction. The proposed diplomatic state keeps change live, with a doubtful cancelled terminal r; it does not duplicate a whole cancelled changer and a second live change.',
     'second manuscript line')
note('S039-N05','unread source ink',
     'The short black patch before the first e1 remains uncertain between an obliteration and a heavy dash. No former word or letter count is inferred.',
     'first manuscript line')
note('S039-N06','underline',
     'The line under rigidifiées passes below its letter bodies and through its long descenders. It is an underline, not a cancellation.',
     'seventh manuscript line')
note('S039-N07','pagination',
     'There is no top author page number. The lighter bottom-left 38 is foliation in another unnamed hand and is retained in a margin macro.',
     'whole sheet')
note('S039-N08','drawings',
     'No front-side drawing or diagram occurs on this sheet. C’s two character arrays are representations of the reverse-print banners, so no TikZ figure is supplied for them.',
     'whole sheet')
note('S039-N09','punctuation',
     'No independent full stop is visible after the projective-line formula; the next manuscript line begins Elle. The final stop after fondamentaux and the stop after the first paragraph are visible and retained.',
     'paragraph endings')
note('S039-N10','checks',
     'Only the four numerical substitutions in the root-of-unity sign split were checked. No verification is claimed for the moduli-space identification or its map to M_{0,5}.',
     'mathematical verification')

note('S039-N11','mathematical caution',
     'The exclusion of 0 from the written projective-line parameter space is explicit. Its role in the structures being classified has not been derived here; no mathematical error is inferred from that exclusion.',
     'projective-line formula')

checks=[dict(statement_id='S039-C02',date='2026-11-20',
             who='reader A; GPT-6 Astra Pro; run SP82_C13_148; effort not exposed',
             type='computation or formal certificate',
             outcome='For zeta=1,-1,i,-i, direct computation gives squares 1,1,-1,-1 and fourth powers 1,1,1,1. Thus multiplication by zeta^2 has the two signs stated for mu.')]
hand_log=[
    dict(pages=[39],habit='Broad angular zeta with a curved lower return',
         holds_at_every_observed_occurrence=True,
         witness_effect='No C/H letter replacement is needed for the seven zeta occurrences; each was read against the local xi and eta forms.',
         evidence='The zeta has a long upper bend and lower return in the base change, fourth-power condition, two scaled coordinates, scaled mu and both membership conditions.'),
    dict(pages=[39],habit='Underline intersecting long descenders',
         holds_at_every_observed_occurrence=True,
         witness_effect='H mistakes the underline of rigidifiées for a strike.',
         evidence='At the one observed underlined word, the horizontal line stays below the ordinary letter bodies while the g and f descend through it.'),
    dict(pages=[39],habit='Doubled stem of projective P',
         holds_at_every_observed_occurrence=True,
         witness_effect='C gives blackboard P; H gives bold P. The visible doubled stem supports C’s alphabet.',
         evidence='The one P in the displayed moduli expression has two parallel vertical strokes under one upper bowl.'),
]
notation=[
    dict(form=r'e_1\mapsto\zeta e_1,\quad\zeta^4=1',pages=[39],
         observed_use='The base change and its fourth-root condition are explicit.',
         caution='The raised 4 is a numeral, while the e subscript is 1.'),
    dict(form=r'\{\xi,\eta\}\mapsto\{\zeta^2\xi,\zeta^2\eta\}',pages=[39],
         observed_use='The coordinate pair is written in braces and each entry is multiplied by zeta squared.',
         caution='Xi, eta and zeta were checked separately; their similar turns are not merged.'),
    dict(form=r'\mu\mapsto\zeta^2\mu',pages=[39],
         observed_use='The following cases give unchanged mu or negative mu according to the stated values of zeta.',
         caution='No definition of mu beyond this page’s explicit transformation is supplied.'),
    dict(form=r'\mathbb P^1\setminus\{0,\pm2,\infty\}',pages=[39],
         observed_use='Written modular multiplicity for the rigidified structures.',
         caution='Preserve the doubled P stem and the literal removed set.'),
    dict(form='38',pages=[39],observed_use='Bottom-left foliation.',
         caution='The hand is unnamed; no author pagination is inferred.'),
]

second_boxes=[]
def blind(id_,kind,box,reading):
    second_boxes.append(dict(box=id_,kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
blind('S39-01','struck passage, handwritten numbers and departure from C below high confidence',
      plan['firstline']['box'],
      r'Changer la base \unsure{\deleted{\illegible{1}}|---} \(e_1\) en \(\zeta e_1\) (où \(\zeta^4=1\))')
blind('S39-02','struck passages, resolved C doubt and whole formula',
      plan['opening_edit']['box'],
      r'\deleted{revient à} change\deleted{\unsure{r}} \deleted{\unsure{par}} \(\{\xi,\eta\}\) en \(\{\zeta^2\xi,\zeta^2\eta\}\),')
blind('S39-03','whole formulas and handwritten numbers',plan['mu_cases']['box'],
      r'donc \(\mu\) en \(\zeta^2\mu\), qui est donc égal à \(\mu\) si \(\zeta\in\{\pm1\}\), égal à \(-\mu\) si \(\zeta\in\{\pm i\}\).')
blind('S39-04','handwritten text on reused listing paper',[260,610,1390,714],
      'La multiplicité modulaire pour les')
blind('S39-05','C/H deletion-state difference and handwritten text',
      plan['rigidifiees']['box'],
      r'structures envisagées, \uline{rigidifiées} par la')
blind('S39-06','whole formula and handwritten numbers',plan['projective']['box'],
      r'donnée de \(e_1\), est donc \(\mathbb P^1\setminus\{0,\pm2,\infty\}\)')
blind('S39-07','handwritten text and handwritten numbers',plan['finaltext']['box'],
      r'Elle s’envoie dans la multiplicité \(M_{0,5}\) --- il y a lieu de regarder l’effet sur les groupoïdes fondamentaux.')
blind('S39-08','handwritten number and margin note',plan['folio38']['box'],r'\margin{38}')

differences_review=[
    dict(source_row=770,decision='macro-only',place='page identification',
         note='C scan marker versus H editorial sheet description. No author number is written at the top.'),
    dict(source_row=771,decision='reading decision',place='opening correction',
         note='The separately cancelled par remains doubtful; H leaves it unread. The narrower correction scope and single live change are also adjudicated from this crop.'),
    dict(source_row=772,decision='reading decision',place='reverse-print prefix and absent H heading',
         note='C’s digit run and illegible span belong to reverse printing; H’s Catalogue heading belongs to its following page and is absent here. Both are excluded for distinct reasons.'),
    dict(source_row=773,decision='reading decision',place='reverse digit banner',
         note='The apparent array is pale mirrored machine printing, not a front-side diagram. H’s accompanying note is editorial metadata.'),
    dict(source_row=774,decision='macro-only',place='H editorial discussion of another page',
         note='The uncertainty about the heading’s R and reference to another page are H commentary, not source text on scan039. No other page was opened.'),
    dict(source_row=775,decision='reading decision',place='reverse letter banner',
         note='C’s letter array belongs to mirrored reverse printing and is excluded. H’s comparison with another page is editorial commentary.'),
    dict(source_row=776,decision='reading decision',place='reverse job rows, reverse date row and foliation',
         note='The job and date rows are reverse printing and are excluded; the real handwritten foliation 38 is retained. H’s trailing editorial sentence is not manuscript prose.'),
]
result=dict(
    scan=39,reader='A',lines_read=12,
    reader_metadata=dict(model='GPT-6 Astra Pro',reasoning_effort='not exposed',run='SP82_C13_148'),
    reading_workflow=dict(
        whole_page_views=1,successful_half_views=[1,1],
        image_proxies='The original whole JPEG and same-dimension quality95 JPEG proxies of both native halves were visually read.',
        line_count_detail='Eleven physical manuscript prose/math baselines, plus the separate foliation baseline. The reverse machine rows are excluded source layers and are not counted as manuscript lines.',
        crops_saved=8,crops_visually_read=8,
        crop_rule='One saved first crop for each designated place; no crop was recut or replaced. The large bleed-through crop was viewed through its same-dimension quality95 JPEG proxy.',
        root_review='Root independently viewed the whole, both native halves and all eight crops; the uncertainty between obliteration and dash is retained after comparison.',
        agreed_text='Every agreed manuscript word, letter, index, exponent, sign and punctuation place was read from the halves; the entire formulas were read around open signs.',
        boundaries='Only scan039 packet, its supplied current notation snapshot and its own original/half/crop images were read. No OCR, web research or TeX compilation.',
        excluded_blind_items='Reverse-print glyphs and the absent next-page heading are not nominated as alternative current-page manuscript words.'
    ),
    changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,
    notes=notes,checks=checks,hand_log=hand_log,notation=notation,abbreviations=[],
    second_boxes=second_boxes,differences_review=differences_review,
    crop_manifest=[dict(x,visually_read=True) for x in plan_list],
    excluded_layers=[dict(layer='reverse-side machine printing',
                          crop=plan['bleedthrough']['crop'],box=plan['bleedthrough']['box'],
                          reason='Pale blue regular character rows and block letters are laterally reversed.',
                          mark_ids=[f'M{n:04d}' for n in range(527,619)])]
)
assert len(marks)==93
assert len(decisions)==93 and {d['id'] for d in decisions}=={m['id'] for m in marks}
covered_marks=[m for x in changes for m in x.get('mark_ids',[])]
assert set(covered_marks)=={m['id'] for m in marks}
assert len(covered_marks)==len(set(covered_marks))
assert len(differences_review)==7
assert {d['source_row'] for d in differences_review}==set(range(770,777))
assert all(x['against_c'] or x['against_h'] for x in changes)
assert all(x['box']==plan[x['crop'].removeprefix('crops/148_scan039_').removesuffix('.png')]['box']
           for x in changes if x['crop']!='page')
assert len({x['box'] for x in second_boxes})==len(second_boxes)
(BASE/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),
                  'unresolved':len(unresolved),'notes':len(notes),'checks':len(checks),
                  'second_boxes':len(second_boxes),'differences_review':len(differences_review),
                  'mark_ids_in_changes':len(covered_marks)}))
