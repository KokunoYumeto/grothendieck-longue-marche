from pathlib import Path
import csv,json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='148_scan059'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((R/'second'/f'{p}_boxes.tsv').open(),delimiter='\t')}
E={
'B03':'The cancelled clause continues from the upper right through desormais and the formula line. The middle category letter has a high cross-stroke and curled trunk, supporting the established script T rather than C. A distinct curved stroke before par is now retained as a doubtful opening parenthesis; no matching close is supplied. The words sont effectivement marques in the independent TSV are preceding live context and are already transcribed outside this target.',
'B04':'The small raised determiner begins with an open rounded c and has no tall l ascender: ces. Its curved leader returns after oublier. A separate short dash remains before meme. A straight stroke passes through the compressed body of meme and beyond its final letter, so the existing cancellation is retained. The final exclamation mark is distinct.',
'B05':'The title underline ends before the following point. The end of Operation has a low horizontal run and downward terminal hook; a separate plural s cannot be securely distinguished from that exit stroke. Singular remains first with plural now an explicit alternative.',
'B07':'The initial tall open curve of the short determiner can be an open l loop or c. The ending supports es but does not decide the initial. Les/ces remains uncertain rather than resolved from grammar.',
'B08':'The main phrase is unchanged. Preliminaire is visibly continued as naire on the next line; the first part reaches the image edge and any separating hyphen is not independently secure. The joined word is retained; the second line break does not establish a different lexical reading.',
'B09':'The cancelled short word has a tall initial and low loop with an obscured hooked ending. Les remains first, with de added as a plausible alternative. The low index of the live A is a looped lowercase l, not a digit; l/ell here are representations of that same letter.',
'B10':'The complete box and both same-box details were viewed. The left cancellation has an e-like entry and tall t, then a looped l and reduced low letters, followed by a separate oval-and-top-bar sigma. Its long horizontal rule is cancellation and has no independent arrowhead, so it is not recast as a map sigma:A-prime-to-sigma. At right the live oval/top-bar sigma has a detached prime; de follows it. The two pair letters are open c forms, with a prime on the second, while A-prime is raised to the right with a curved attachment. Their former withdrawal-state uncertainty remains. Relation has a faint terminal run that permits an abbreviation alternative. The following d-equiv word ends after the v-like downstroke with small points and no securely exposed -alence; d-equiv. is now the doubtful primary reading rather than an unqualified expansion.',
'B11':'The canonical box and same-box formula detail were viewed. The low final index has an arch and return consistent with a small 2 or cursive l. There is no distinct quotient slash to the right of A, nor a clear horizontal pi bar with two legs. The old A is heavily retraced, so the first index alternatives remain. The horizontal stroke through tout joins the two tall t strokes as their common crossbar; no following e is visible before orbite. The curve above de may be an attachment rather than cancellation, so that state stays uncertain. A tiny isolated dot near the strike endpoint does not securely establish old sentence punctuation.',
'B14':'The first mark consists of two small separated strokes and can be the reduced handwritten a-grave or a colon; that ambiguity is now explicit. Isom has no terminal point. The final word has u/n/i, a q descender and u/e ending; its last hooked exit can include s, so unique/uniques remains uncertain. No additional v/o group supports univoques.',
'B15':'The pale folio has a barred open-bowl 5 and a two-loop 8: 58. The isolated dot to its left has no punctuation position or textual connection and is not transcribed as a period.'}
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
repls={
'B03':[('désormais par',r'désormais \unsure{(}par')],
'B05':[(r'\uline{Opération de recollement}',r'\uline{\unsure{Opération|Opérations} de recollement}')],
'B09':[(r'\unsure{les}',r'\unsure{les|de}')],
'B10':[("une relation d'équivalence",r"une \unsure{relation|relat.} \unsure{d'équiv.|d'équivalence}")],
'B14':[('à isom unique',r'\unsure{à|:} isom \unsure{unique|uniques}')]
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
update(2,'B03',final=D['B03']['reading'].replace(r' \inserted{Néanmoins on}',''),diff_c=True,confidence='medium')
update(6,'B05',final=r'\uline{\unsure{Opération|Opérations} de recollement}',confidence='medium')
update(13,'B09',final=r'\deleted{\unsure{les|de}}')
update(23,'B14',final=D['B14']['reading'],confidence='medium')
r['changes'].append(dict(id=p+'-25',place='Equivalence abbreviation in item a',c="d'équivalence",h="d'équivalence",final=r"\unsure{d'équiv.|d'équivalence}",diff_c=True,diff_h=True,kind='abbreviation expanded or spelling modernised',error_kind='Abbreviations expanded, spelling modernised',evidence=E['B10'],crop=f'crops/{p}_second_B10.png',box=boxes['B10'],confidence='medium',marked_in_h=False,consequential=False))
for x in r['doubts']:
 if x['place']=='Cancelled word after Une partie':x.update(reading=r'\deleted{\unsure{les|de}}',alternatives='les; de',reason=E['B09'])
for place,reading,alt,b in [
 ('Curved old stroke before par',r'\unsure{(}','opening parenthesis; revision curve','B03'),
 ('Title grammatical number',r'\unsure{Opération|Opérations}','singular; plural terminal s','B05'),
 ('Relation ending',r'\unsure{relation|relat.}','relation; relat.','B10'),
 ('Equivalence abbreviation',r"\unsure{d'équiv.|d'équivalence}",'abbreviated; full word with concealed ending','B10'),
 ('Before final isom',r'\unsure{à|:}','reduced à; colon','B14'),
 ('Final unique ending',r'\unsure{unique|uniques}','unique; uniques','B14')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alt,confidence='medium',reason=E[b]))
for x in r['inventory']:
 if x['element']=='E04':x['first_words_or_objects']='Si on désigne désormais; possible opening parenthesis before par; S𝒯D_top^± le groupoïde'
 if x['element']=='E09':x['first_words_or_objects']='D) Opération / Opérations de recollement.'
 if x['element']=='E13':x['first_words_or_objects']='les / de'
 if x['element']=='E14':x['first_words_or_objects']='et une involution ss pts fixes ... relation/relat. d’équiv./d’équivalence ... classes de cardinal 2 ...'
 if x['element']=='E23':x['first_words_or_objects']='Pour que l’opération soit bien déterminée; à/colon isom unique/uniques'
r['abbreviations'].append(dict(form="d'équiv.",expansion="d’équivalence (doubtful abbreviated reading)"))
r['notes'].append(dict(id=p+'-N-audit',text='The independent TSV was frozen before comparison, and all ten unequal boxes were viewed. The two cancelled formulas retain STD and the short et les sigma fragment: the cancellation rule has no independent arrowhead. The old item-b index remains 2/l, with no securely distinct quotient slash or pi. The c,c-prime pair remains different in glyph from the later a,a-prime pair; no mathematical regularization was made. The d-equiv ending is now recorded as a doubtful abbreviation. The final a-grave/colon and singular/plural endings remain explicit uncertainties.'))
extra=[f'second/{p}_second_{b}_detail.png' for b in ['B10_left','B10_right','B11_formula']]
r['second_main_review']={'viewed_boxes':list(E),'reviewed_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'decisions':f'second/{p}_main_decisions.json','additional_existing_crops_viewed':extra}
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
