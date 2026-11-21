"""Serialize the main reader's explicit, visually adjudicated decisions."""
from pathlib import Path
import json, subprocess, sys
W=Path(__file__).resolve().parents[1]; page='150_scan005'
C={r['box']:r for r in json.loads((W/'second'/f'{page}_comparison.json').read_text())}
R=json.loads((W/'reports'/page/'report.json').read_text())
rows=[]; E={'source_replacements':[],'report_updates':[],'report_appends':{}}
def decision(box,evidence,outcome,changes=(),crop=None):
    final=C[box]['first']
    for a,b in changes:
        assert a in final,(box,a)
        final=final.replace(a,b)
    d=dict(box=box,decision='revise' if changes else 'retain',evidence=evidence,outcome=outcome)
    if changes:d['final']=final
    if crop:d['crop']=crop
    rows.append(d)
def replace(a,b): E['source_replacements'].append(dict(old=a,new=b,count=1))
def update(collection,key,value,**fields):
    assert sum(x.get(key)==value for x in R[collection])==1,(collection,value)
    E['report_updates'].append(dict(collection=collection,match={key:value},set=fields))
def change(id,**fields):update('changes','id',id,**fields)
def doubt(place,reading,alternatives,reason,confidence='low'):
    fields=dict(reading=reading,alternatives=alternatives,reason=reason,confidence=confidence)
    if any(x['place']==place for x in R['doubts']):update('doubts','place',place,**fields)
    else:E['report_appends'].setdefault('doubts',[]).append(dict(place=place,**fields))
def newchange(box,id,place,c,h,final,evidence,kind,category,confidence='medium',consequential=False):
    coords=next(x['xyxy'] for x in R['audit_boxes'] if x['box']==box)
    E['report_appends'].setdefault('changes',[]).append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{page}_second_{box}.png',box=coords,confidence=confidence,kind=kind,against_c=True,against_h=True,marked_in_h=False,consequential=consequential,error_category=category))


rows=json.loads((W/"second"/f"{page}_root_decisions.json").read_text())
D={x["box"]:x for x in rows}
for d in rows:
 if d["decision"]=="revise":replace(C[d["box"]]["first"],d["final"])
# Explicit final excerpts and collation flags selected by the main reader.
updates={
'P01b':dict(final=r'ouvert \unsure{dans|de} $X\Rightarrow',against_c=True,against_h=False,confidence='medium',evidence=D['B01']['evidence']),
'P06a':dict(final=r'par \unsure{images inverses|image inverse}',against_c=True,against_h=False,confidence='medium',evidence=D['B07']['evidence']),
'P06b':dict(final=r'(\unsure{par|pas} $\unsure{=|\mathrm{ex.}}$ pour',against_c=True,confidence='low',evidence='The short group favors par but its ending remains doubtful. The following sign consists of two parallel strokes; ex. is only an alternative, not an expansion.'),
'P07a':dict(final=r"relations d'\unsure{équivalences|équivalence} ouvertes",confidence='medium',evidence=D['B08']['evidence']),
'P09a':dict(final=r'\inserted{3° bis (\unsure{en présence de|en plus de} 1° et 2°)}',confidence='medium',evidence=D['B10']['evidence']),
'P10a':dict(final=r'\deleted{\unsure{Si on a la fidélité, on aurait,|i.e. la fidélité, on aurait,} $X_i^*=\phi$ i.e. $X_i=\bigcup_{j<i}X_j$}',confidence='low',evidence=D['B11']['evidence']),
'P13d':dict(final=r'\deleted{\unsure{lesquels|tels que}} \inserted{$\ne\phi$}',confidence='medium',evidence=D['B14']['evidence']),
'P14d':dict(final=r'stricte \unsure{de|avec|sur} $U$)',confidence='low',evidence='The compressed preposition retains de preferred, with avec/sur alternatives. No detached point follows the closing parenthesis.'),
'P15a':dict(final=r'\margin{\unsure{cl|ch|des}}',against_c=True,confidence='low',evidence=D['B18']['evidence']),
'P17a':dict(final=r'\inserted{\unsure{Supposons|Prenons} $J$ minimal}',confidence='low',evidence=D['B20']['evidence']),
'P19a':dict(final='parmi de tels $J$!',against_c=True,evidence='A separate tall mark and lower point follow J, before the opening parenthesis.'),
'P19c':dict(final=r'non fermé \inserted{en $I$}',against_c=True,confidence='medium',evidence='Small e/n letter bodies precede I. The curved leader descends to non fermé; the earlier attachment to simplifier was mistaken.',kind='insertion or placement',error_category=6),
'P20a':dict(final=r'plus \unsure{grd|grand} él. de $J$',against_c=True,confidence='low',evidence='The short first group is secure as g/r/d-like strokes, without separable a/n; the expanded grand remains an alternative. Él. retains its separate stop.'),
'P22b':dict(final=r'\deleted{\unsure{$i\in\overline j\cap I$|i.e. $\overline j\cap I$}}',confidence='low',evidence='The struck prefix is compatible with i∈ or i.e.; the barred j and cap/I group remain under the cancellation.'),
'P23a':dict(final=r"qui est fermé, \unsure{donc|d'où}",against_c=True,against_h=False,confidence='medium',evidence='The terminal low n/c-like sequence favors donc; an apostrophe/accent is not securely separable.'),
'P26b':dict(final=r'$\overline j\not\subset J$ \unsure{ce|ceci},',against_c=True,confidence='low',evidence='The short word has ce bodies without a separate second ci; no tall d is visible.'),
'P27a':dict(final=r'\overset{\overline J=}{J_0}',confidence='medium',evidence='The small raised annotation has barred J and two equality strokes. The curved leader joins the preceding inclusions to this annotation.'),
'P27b':dict(final=r'\deleted{\unsure{\overline j}}\overset{\deleted{\unsure{\overline j|\illegible{1}}}}{\overline j}',against_c=True,confidence='low',evidence='There is one cancelled blob before the live barred j and a separate crossed group above it. The latter is preserved as a doubtful barred-j/unreadable item.'),
'P28b':dict(final=r'Comme \unsure{\inserted{tt}|le|$\downarrow$}',confidence='low',evidence=D['B32']['evidence']),
'P30b':dict(final=r'\unsure{3|?} conditions équiv. :',confidence='low',evidence='A curved upper body and indistinct lower return admit 3 or question mark; the character and final colon are present, so C still omits source ink.'),
'P31a':dict(final=r'\unsure{ops|sps|ssi}',against_c=True,confidence='low',evidence='Compact o/p/s-like bodies include a descending middle stem. Ops is preferred, with sps/ssi alternatives; no long arrow shaft is present.')}
for id,fields in updates.items():change(id,**fields)

# A correction is primary only if preferred ink/state differs from C, or a
# source omission is restored. Mere added uncertainty has no new primary row.
newchange('B01','S_def','Three unaccented definition labels',r'\mathrm{déf}',r'\text{déf}',r'\mathrm{def}','No independent accent occurs over the definition labels in B01, B27 or B35.','abbreviation expanded or spelling modernised',8)
newchange('B02','S_B02_word','NB adjective',"est l'essentiel","est l'essentiel",'est élémentaire','The long final word has élém-ent-aire letter groups, including a final t/aire sequence.','misread word',2)
newchange('B02','S_B02_close','Absent outer closing parenthesis',r'\overline{\varphi^{-1}(B)})',r'\overline{\varphi^{-1}(B)}$)',r'\overline{\varphi^{-1}(B)}','Only the inverse-image parenthesis closes before the NB parenthesis; no extra outer close is written.','text not on the page',9)
newchange('B04','S_B04_case','Argument of second Ouv quantifier',r'\operatorname{Ouv}(X)',r'\mathrm{Ouv}(X)',r'\operatorname{Ouv}(\unsure{x|X})','The small crossed argument favors lowercase x; case remains uncertain.','misread symbol or index',1,confidence='low')
newchange('B10','S_B10_inverse','Raised L’inverse after crossed end group','[omitted]','[omitted]',r"\inserted{L'inverse}",'A separate raised L, apostrophe and inverse sequence appears above the crossed end group.','omission',3)
newchange('B16','S_B16_stop','No full stop after closing U parenthesis','$U$).','$U$.)','$U$)','The closing parenthesis is followed directly by Ainsi; no detached full stop is visible.','text not on the page',9)
newchange('B22','S_B22_comma','No comma after fini','fini, pour','fini, pour','fini pour','The first line has no independent comma between fini and pour.','text not on the page',9)
newchange('B22','S_B22_marks','Point dash point before K superset J',r'\ldots',r'\ldots',r'$\unsure{\mathinner{\cdot-\cdot}|\ldots}$','Two points flank a short horizontal dash.','misread symbol or index',1,confidence='medium')
newchange('B23','S_B23_marks','Point dash point before J subset barred j',r'\ldots',r'\ldots',r'$\unsure{\mathinner{\cdot-\cdot}|\ldots}$','The middle mark is a short dash rather than a point.','misread symbol or index',1,confidence='medium')
newchange('B23','S_B23_short','Second shortened grand group','plus grand','plus grand',r'plus \unsure{grd.|grand}','The short g/r/d-like sequence ends in a separate point; no certain a/n sequence is isolated.','abbreviation expanded or spelling modernised',8,confidence='low')
newchange('B24','S_B24_comma','Comma after barred j-prime subset J',r'\subset J$. Donc',r'\subset J$. Donc',r'\subset J$, Donc','The detached mark descends below the line as a comma.','misread symbol or index',1)
newchange('B25','S_B25_relation','Comparison after avec','avec $i<j$','avec $i<j$',r'avec $i\leq j$','A second lower bar accompanies the comparison angle.','misread symbol or index',1,consequential=True)
newchange('B27','S_B27_comma','Comma immediately after equals',r'X_{J_0}^*=X_{J_0}',r'X_{J_0}^{*}=X_{J_0}',r'X_{J_0}^*=,X_{J_0}','A separate comma follows the equality before the unstarred X. It is retained literally.','omission',3)

for id,reading,evidence in [
 ('M0288',r'\unsure{cl|ch|des}',D['B18']['evidence']),
 ('M0291',r'\unsure{\inserted{tt}|le|$\downarrow$}',D['B32']['evidence']),
 ('M0292',r'\unsure{ops|sps|ssi}',D['B35']['evidence'])]:
 update('decisions','id',id,reading=reading,decision='undecided',evidence=evidence,confidence='low')
# Preserve the unresolved preferred readings as doubts, without double counting.
for place,reading,alternatives,box in [
 ('P01 preposition',r'\unsure{dans|de}','dans preferred; de possible','B01'),
 ('P04 x/X case',r'\unsure{x|X}','lowercase preferred; uppercase possible','B04'),
 ('P06 degree numeral',r'\unsure{2°|7°}','2° preferred; 7° possible','B07'),
 ('P06 number agreement',r'\unsure{images inverses|image inverse}','plural preferred','B07'),
 ('P06 abbreviation',r'\unsure{par|pas} $\unsure{=|\mathrm{ex.}}$','par/pas and equals/ex.','B07'),
 ('P07 noun ending',r'\unsure{équivalences|équivalence}','plural retained preferred','B08'),
 ('P09 raised condition wording',r'\unsure{en présence de|en plus de}','presence preferred','B10'),
 ('P10 cancelled sentence',r'\unsure{Si on a la fidélité, on aurait,|i.e. la fidélité, on aurait,}','opening unresolved; on aurait favored','B11'),
 ('P13 cancelled group',r'\deleted{\unsure{lesquels|tels que}}','lesquels preferred','B14'),
 ('P14 short preposition',r'\unsure{de|avec|sur}','de preferred','B16'),
 ('P15 M0288',r'\unsure{cl|ch|des}','cl preferred','B18'),
 ('P17 raised instruction',r'\unsure{Supposons|Prenons}','Supposons retained preferred','B20'),
 ('P19 subset-I attachment',r'non fermé \inserted{en $I$}','en I preferred, attached to non fermé','B22'),
 ('P20 compressed grand groups',r'\unsure{grd|grand}; \unsure{grd.|grand}','short forms preferred','B23'),
 ('P21 small relation',r'J_0\unsure{=|:}J','equals preferred','B24'),
 ('P22 cancelled formula',r'\deleted{\unsure{$i\in\overline j\cap I$|i.e. $\overline j\cap I$}}','i∈ preferred; i.e. possible','B25'),
 ('P23 union equality',r'X_J^*\unsure{=|:}X_{J_0}^*','equals preferred','B26'),
 ('P23 conjunction',r"\unsure{donc|d'où}",'donc preferred','B26'),
 ('P26 compressed final word',r'\unsure{ce|ceci}','ce preferred','B30'),
 ('P27 second cancelled formula',r'\deleted{\unsure{\overline j|\illegible{1}}}','barred j or unrecoverable short item','B31'),
 ('P28 M0291',r'\unsure{\inserted{tt}|le|$\downarrow$}','tt, le, or downward pointer','B32'),
 ('P30 heading number',r'\unsure{3|?}','3 preferred; question mark possible','B34'),
 ('P31 M0292',r'\unsure{ops|sps|ssi}','ops preferred; sps/ssi alternatives','B35')]:doubt(place,reading,alternatives,D[box]['evidence'])
E.setdefault('report_removals',[]).append(dict(collection='doubts',match={'place':'P28 relation between J-prime and I-prime minus the singleton'}))
for id,words in [
 ('E05','5) ... par images inverses (singular alternative)'),
 ('E07','Raised 3° bis labels; en présence de/en plus de wording uncertain'),
 ('E08','Implique que la fidélité; raised L’inverse; n’est pas vrai, exemple I='),
 ('E09','I and doubtful l’inclusion; cancelled fidelity clause with on aurait preferred'),
 ('E15','i in I tels que before X_i cap U; ne phi replacing doubtful lesquels/tels que'),
 ('E16','Cancelled lesquels/tels que; uncertain cancellation or dash after et'),
 ('E17','Doubtful cl/ch/des'),
 ('E20','Soit; Supposons/Prenons J minimal'),
 ('E23','en I attached at non fermé; j-prime after autre élément'),
 ('E28','partie; exists; barred-j nonmembership; two cancelled barred-j-like groups; de I-prime; singleton i; En'),
 ('E29','barred J equals above J_0; doubtful tt/le/downward mark after Comme'),
 ('E32','Doubtful 3/? conditions équiv. :; a), b), c); NB ops/sps/ssi and repeated pour')]:update('inventory','element',id,first_words_or_objects=words)
update('notation','form','$=$ in prose',meaning='literal equals-shaped abbreviation; semantic expansion unresolved',evidence='P06: two horizontal strokes follow the uncertain par/pas group. Ex. is retained only as an alternative; no expansion to même is imposed.')
update('notation','form',r'X_j^\bullet=\overline{X_j^*}\setminus X_j^*',evidence='The explicitly written unaccented def label appears in P24 and again in c), P31; the filled superscript is retained.')
update('notes','id','N09',text='The final line visibly repeats pour, retained against both witnesses’ tout. Its terminal arrow has one shaft, unlike the doubled implication above. The edge word now favors cl, with ch/des alternatives. The compact NB abbreviation favors ops, with sps/ssi alternatives; no expansion is supplied.')
E['report_appends'].setdefault('notes',[]).extend([
 dict(id='N14',text='Independent visual audit: restored raised L’inverse, corrected the small barred-J/equality annotation above J_0, and recorded the additional cancelled group above the final live barred j. The non-fermé insertion is read en I with a leader to the lower phrase. Two ellipsis-like sequences are recorded as point/dash/point. Definition labels are unaccented def. No mathematical wording is supplied to regularize the source.'),
 dict(id='N15',text='Scope differences: B08’s en principe continues in B09; B11’s live n’est pas vrai, exemple I= lies below the narrow second crop and was checked in the wider original; B17’s opening appears in the wider P14 crop. The fixed second records remain unchanged. New uncertainty alone, with the same preferred C reading, is not promoted into a new primary C correction.')])
E['report_appends'].setdefault('notation',[]).append(dict(form=r'\mathinner{\cdot-\cdot}',meaning='literal point/dash/point sequence, possible ellipsis',evidence='Right minimality argument before K superset J and J subset barred j; both have a visibly extended middle mark.'))
# Revision-review summaries are updated by exact approved literal replacements.
review_pairs=[(r'\deleted{tels que}',r'\deleted{\unsure{lesquels|tels que}}'),(r'\inserted{Supposons $J$ minimal}',r'\inserted{\unsure{Supposons|Prenons} $J$ minimal}'),(r'\inserted{$\subset I$}',r'\inserted{en $I$}'),(r'\overbrace{J_0}^{\subset\overline j}',r'\overset{\overline J=}{J_0}'),(r'\inserted{\unsure{tt}}',r'\unsure{\inserted{tt}|le|$\downarrow$}')]
for x in R.get('deletion_insertion_review',[]):
 t=x['text'];n=t
 for a,b in review_pairs:n=n.replace(a,b)
 if n!=t:update('deletion_insertion_review','text',t,text=n,evidence='Updated from the explicit main-reader second-reading adjudication; see the corresponding source crop and audit record.')
assert not (W/'second'/f'{page}_edits_receipt.json').exists()
(W/'second'/f'{page}_edits.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'decisions;',sum(x['decision']=='revise' for x in rows),'revised boxes;',len(E['report_appends']['changes']),'new primary rows')
