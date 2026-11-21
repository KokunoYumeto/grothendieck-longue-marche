from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan061'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B01':'The upper number consists of a straight 1 and angled 7. The heading reads Recapitulation des operations elementaires. The difference is the mspage wrapper and line break only.',
'B02':'The two interlinear baselines were distinguished. The upper word has the d ascender, descending j and final -ointe: disjointe, not directe. Below its end is the short underlined total, followed by des reperes en a, i.e.; the long stroke below this qualification bends down to attach it to gommage and is not a cancellation. The tall overlapping strokes do not constitute a separate drawing. The small added zero-degree item retains its surrounding curves.',
'B03':'The first item digit has an ascending diagonal, a right upright and a transverse stroke, giving a 4-like form; 1 remains possible under retracing and is not imposed by the sequence. The first raised circle symbol has a capital open C and a low oval, permitting a or 0 as index. The second raised group has a tall loop and reduced es-like ending, so les/C_a remains unresolved. The cancelled sur un cercle is not promoted to certainty.',
'B04':'Both equivalence signs have two shafts. The short horizontal stroke beneath the live r is an underline, with no separate lower-right a. In the old continuation after trouvant a tall d and low ans-like run favour dans over sur; the cancellation still hides other letters. The raised R_a replaces crossed partie. The compressed article remains d-une/de la.',
'B05':'Two separate physical word lines have separate underline strokes, one below fortement and one below irreversible. The initial i/r/re strokes precede -versible; the prefix is not omitted. The lower formula has two bars crossed by a slant and a closed 0: r_a not-equal 0.',
'B06':'The added heading has a separate underline below gommage. Two small dots stand to the left of the upright divisibility stroke in d_a :| r_a; the lower r-prime divides r has no such dots. The source denominator Z has no a, while the target denominator has a separate lower a. Groupes de R_a is the replacement below cancelled scalaires. In the same-box D06 detail the short word after possibles has curved o/u strokes and a raised accent, supporting ou-grave rather than si. The isolated 2/question-mark remains doubtful.',
'B07':'The whole rotated margin was viewed. The terminal strokes of de/structure/faible can contain small plural s strokes, so these endings are now explicitly doubtful without being supplied from grammar. The r_a condition ends in a tall hooked 1, not a closed oval 0. The overworked relation still permits greater-or-equal/greater. The first lower relation is heavily overwritten; its divides/not-equal alternatives remain. The later not-equal and the ratio formula are clear. The old crossed word retains its anodin doubt. The open upper/right boundary is retained once.',
'B08':'The canonical crop and D07 detail show a short horizontal stroke before a looped descending g, then the low o/mm/a sequence and the second g descender. No separate Surmar- sequence is exposed. The primary heading is now -gommage, with degommage retained as an alternative because the small opening strokes are compressed. The numeral has two curved lobes supporting 3. Extension des is crossed below the added heading.',
'B09':'The article before groupes has a looped d and low es run; the noun has g and p descenders followed by es, supporting des groupes. The target numerator is a doubled Z without a separate low a. The multiplier d has a long foot but no securely separate subscript; d/d_a is retained with unindexed d first. The source quotient has both a indices. The final target Z has no lower a, and the terminal comma is distinct.',
'B10':'The open top/right boundary and separate lower formula were viewed. The final hooks can be singular word exits or plural s, so de/des, structure/structures and faible/faibles are explicitly uncertain. The lower sign is a clear crossed equals followed by oval 0. The underline below faible is distinct; the faint trace below structure is not extended into a continuous underline.',
'B11':'Both numerals are circled and one left brace joins the two lines. The short articles have reduced e/u bowls, so de remains first with du as alternative. The same-box index detail shows one looped cursive l directly after A in item 5, with no independent 0 or comma: A_l. Item 4 has a separate small oval 0. The circled 4 and 5 are not duplicated in the margin.',
'B12':'The prefix i/r/re is visible in irreversible. The right curved fragment is the same brace beside items 4 and 5, already transcribed with those lines, not an additional margin brace. The lower long line continues across the margin and is the separator above item 6, already represented there; it is not a second local underline under irreversible. The top separator remains.',
'B13':'The 6 has a closed lower bowl and its own upper stroke. A separate right parenthesis follows the degree mark; the left curve belongs to the digit, not a complete surrounding circle. C_a, A_0 and the separate upper-right asterisk remain.',
'B14':'Under the long cancellation, faible is followed by further low m/e/n/t-like strokes, so faiblement is now first while faible remains an alternative because the strike covers the joins. After reversible two short bars precede a low a/n/o run, tall d, dotted i and final n: anodin. There are no separate a/en condition words. The lower inequality has its additional bar and ends in 1 plus a separate point. The bottom separator belongs to the next margin and is represented there once.',
'B15':'The canonical box, D11 and the opening detail were viewed. Between the opening parenthesis and a,a-prime there is faint compressed ink; it is not blank, but the v/e/c joins formerly read avec are not individually secure, so avec is retained under doubt. The pair uses the same open handwritten a forms as the nearby a indices. A_l has one cursive l. The raised equality has a curved leader returning before the closing parenthesis; that leader is not an additional parenthesis. The final product is an unbarred wedge.',
'B16':'The equality of the two r parameters and the prime on the second index are visible. The overworked greater sign has a lower short bar, but its final state still permits greater as an alternative. The next line has two short equals bars and the readable a-n-o-d-i-n sequence with tall d, not a/en condition. The upper separator is retained once.',
'B17':'A short separate dash precedes the star and is now restored. The verb after faudrait and the inserted peut-etre has an early s/e group and a p descender, supporting separer rather than distinguer. The whole two-case formula remains r_a=0 or r_a not-equal 0. Before exclure there are an upper straight bar and lower wavy stroke; the existing equals/cancelled-ou ambiguity is retained, rather than replacing the readable alternatives with an unlabelled drawing. The final question mark and closing parenthesis have no extra point.',
'B18':'The folio consists of a 6 with a closed lower bowl followed by a tall oval 0. The only difference is the mspage wrapper.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B02':[(r'\unsure{disjointe|directe}','disjointe')],
'B03':[(r'$1^\circ$)',r'$\unsure{4^\circ|1^\circ}$)'),(r'\unsure{$C_a$}',r'\unsure{$C_a$|$C_0$}')],
'B05':[(r'\uline{fortement irréversible}\quad',r'\uline{fortement}\\\uline{irréversible}\\')],
'B06':[(r'\uline{gommage partiel uniforme}',r'\uline{gommage} \uline{partiel uniforme}'),(r'd_a\mid r_a',r'd_a\mathrel{:\!|}r_a')],
'B07':[(r'\uline{renforcement} de',r'\uline{renforcement} \unsure{de|des}'),(r'\uline{structure faible}',r'\uline{\unsure{structure|structures} \unsure{faible|faibles}}')],
'B08':[('Surmarquage',r'\unsure{-gommage|dégommage}')],
'B09':[(r'\unsure{\mathbb Z|\mathbb Z_a}/d_ar_a',r'\mathbb Z/\unsure{d|d_a}r_a')],
'B10':[(r'\uline{affaiblissement de}',r'\uline{affaiblissement \unsure{de|des}}'),(r'structure \uline{faible}',r'\unsure{structure|structures} \uline{\unsure{faible|faibles}}')],
'B11':[('gommage de cercle',r'gommage \unsure{de|du} cercle'),('bouchage de trou',r'bouchage \unsure{de|du} trou')],
'B12':[(r'fortement \uline{irréversible}','fortement irréversible')],
'B14':[(r'\deleted{faible}',r'\deleted{\unsure{faiblement|faible}}')],
'B15':[('(avec',r'(\unsure{avec}')],
'B16':[(r"r_a=r_{a'}\ge1",r"r_a=r_{a'}\unsure{\ge|>}1")],
'B17':[(r'\({}^*\) Il faudrait',r'--- \({}^*\) Il faudrait')]
}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,rs in repls.items():
 v=C[b]['first']
 for a,z in rs:
  assert a in v and a in s,(b,a);v=v.replace(a,z);s=s.replace(a,z)
 D[b].update(choice='reading',reading=v)
pp.write_text(s)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
def update(n,b,**kw):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 x.update(evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],**kw)
for n in (1,2,3):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 update(n,'B02',final=x['final'].replace(r'\unsure{disjointe|directe}','disjointe'),confidence='high')
update(5,'B03',final=r'\inserted{\unsure{$C_a$|$C_0$}}')
for n in (13,14):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 update(n,'B05',final=x['final'].replace(r'\uline{fortement irréversible}\quad',r'\uline{fortement}\\\uline{irréversible}\\').replace(r'\uline{fortement irréversible}',r'\uline{fortement}\\\uline{irréversible}'))
for n in (15,16):
 x=next(x for x in r['changes'] if x['id']==f'{p}-{n:02d}')
 update(n,'B06',final=x['final'].replace(r'\uline{gommage partiel uniforme}',r'\uline{gommage} \uline{partiel uniforme}').replace(r'd_a\mid r_a',r'd_a\mathrel{:\!|}r_a'))
update(18,'B06')
update(27,'B08',final=D['B08']['reading'].split('\\inserted',1)[-1] if False else r"\inserted{\uline{\unsure{-gommage|dégommage} uniforme} \uline{d'exposant} $d_a>1$}",diff_c=True,confidence='medium')
update(28,'B09',final=r'$\mathbb Z/\unsure{d|d_a}r_a\mathbb Z$',confidence='medium')
update(29,'B09',final=r'$\mathbb Z/\unsure{d|d_a}r_a\mathbb Z$,')
update(36,'B12',final='fortement irréversible',diff_c=True,diff_h=False,confidence='high')
update(41,'B15',final=r'(\unsure{avec}',confidence='low')
update(44,'B16',final=r"$r_a=r_{a'}\unsure{\ge|>}1$\quad réversible = anodin")
def add(n,place,c,h,final,b,kind,err,confidence='medium',consequential=False):
 r['changes'].append(dict(id=f'{p}-{n:02d}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=True,kind=kind,error_kind=err,evidence=E[b],crop=f'crops/{p}_second_{b}.png',box=boxes[b],confidence=confidence,marked_in_h=False,consequential=consequential))
add(54,'First main item, retraced numeral',r'$1^\circ$)',r'1°)',r'$\unsure{4^\circ|1^\circ}$)','B03','misread symbol or index','Symbols and indices','low')
add(55,'Added item 2 heading, dotted divisor sign',r'd_a\mid r_a',r'd_a\mid r_a',r'd_a\mathrel{:\!|}r_a','B06','misread symbol or index','Symbols and indices','high')
add(56,'Margin to item 6, cancelled adjective ending',r'\deleted{faible}',r'\struck{faible}',r'\deleted{\unsure{faiblement|faible}}','B14','misread word','Words','medium')
add(57,'Footnote, dash before star','absent','absent','---','B17','omission','Omissions','high')
for x in r['decisions']:
 if x['id']=='M0751':x.update(decision='first',reading='disjointe',evidence=E['B02'],crop=f'crops/{p}_second_B02.png',box=boxes['B02'],confidence='high')
 if x['id']=='M0752':x.update(reading=r'\unsure{$C_a$|$C_0$}',evidence=E['B03'],crop=f'crops/{p}_second_B03.png',box=boxes['B03'])
r['doubts']=[x for x in r['doubts'] if x['place']!='Inserted item 0']
for x in r['doubts']:
 if x['place']=='Item 1, first raised circle group':x.update(reading=r'\inserted{\unsure{$C_a$|$C_0$}}',alternatives='C_a; C_0',reason=E['B03'])
 if x['place']=='Item 3, whole quotient pair':x.update(reading=r'$\mathbb Z_a/r_a\mathbb Z_a$ à $\mathbb Z/\unsure{d|d_a}r_a\mathbb Z$',alternatives='multiplier d; d_a',reason=E['B09'])
for place,reading,alt,b,conf in [
 ('First main item number',r'$\unsure{4^\circ|1^\circ}$)','4-degree; 1-degree','B03','low'),
 ('Margin to item 2, grammatical endings',r'\unsure{de|des} \unsure{structure|structures} \unsure{faible|faibles}','singular exits; plural s strokes','B07','medium'),
 ('Item 3, replacement operation name',r'\unsure{-gommage|dégommage}','-gommage; dégommage','B08','medium'),
 ('Margin to item 3, grammatical endings',r'\unsure{de|des} \unsure{structure|structures} \unsure{faible|faibles}','singular exits; plural s strokes','B10','medium'),
 ('Articles in items 4 and 5',r'\unsure{de|du}','de; du','B11','medium'),
 ('Cancelled adjective before reversible',r'\deleted{\unsure{faiblement|faible}}','faiblement; faible','B14','medium'),
 ('Word after item 7 opening parenthesis',r'\unsure{avec}','avec; incompletely separable low letters','B15','low'),
 ('Margin to item 7 inequality',r'\unsure{\ge|>}','greater or equal; greater','B16','medium')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence=conf,reason=E[b]))
for x in r['inventory']:
 x['first_words_or_objects']=x['first_words_or_objects'].replace('Surmarquage','-gommage / dégommage')
r['notation'].append({'sign': '\\mathrel{:\\!|}', 'meaning_or_form': 'Item 2 raised heading has two dots immediately left of a divisibility upright, transcribed \\mathrel{:\\!|}; the lower divisor relation has an undotted upright. This is local graphic evidence, not a change of the stated arithmetic.', 'places': 'Added heading above item 2', 'universality': 'Local dotted form; the lower divisor relation on this page is undotted.', 'witness_errors': 'Both witnesses omit the two dots.'})
r['notes'].append(dict(id=p+'-N-audit',text='All eighteen unequal boxes were viewed after the independent TSV was frozen. The item-3 heading now has -gommage as its doubtful primary reading; its initial short bar and descending g do not expose Surmar-. The first main item numeral is explicitly 4/1 under retracing, with no repair from the expected sequence. In the target extension quotient, the multiplier is d/d_a, while the unindexed target Z letters remain. The added item-2 heading preserves a dotted divisibility glyph. The item-5 subscript is a single looped l, without a separate 0. The repeated reversible = anodin labels were confirmed by their letter strokes. The margin brace and separator lines are represented once, where they attach. These are transcription checks, not independent proofs of the operations.'))
extra=[f'crops/{p}_second_{z}.png' for z in ('D06','D07','D11','main_index5','main_opening7')]
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
