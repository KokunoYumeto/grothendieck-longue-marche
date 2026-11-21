"""Serialize the root reader's explicit image adjudications; never infer readings."""
from pathlib import Path
import json

W=Path(__file__).resolve().parents[1]
p='150_scan007'; S=W/'second'
out=S/f'{p}_root_decisions.json'
if out.exists(): raise RuntimeError('Already recorded')
cmp={x['box']:x for x in json.loads((S/f'{p}_comparison.json').read_text())}
r=json.loads((W/'reports'/p/'report.json').read_text())
ed={'source_replacements':[],'report_updates':[],'report_removals':[],
    'report_appends':{'changes':[],'doubts':[],'notes':[],'check_events':[]}}
ds=[]
def decision(b,e,final=None,outcome=None,crop=None):
 d=dict(box=b,decision='retain' if final is None else 'revise',evidence=e,
        outcome=outcome or ('Main reader retains the first reading after examining the second crop.' if final is None else 'Main reader revises the final transcription on the visible ink.'))
 if final is not None:d['final']=final
 if crop:d['crop']=crop
 ds.append(d)
def rep(a,b,count=1):ed['source_replacements'].append(dict(old=a,new=b,count=count))
def up(c,key,value,**fields):ed['report_updates'].append(dict(collection=c,match={key:value},set=fields))
def change(id,**fields):up('changes','id',id,**fields)
def inv(id,**fields):up('inventory','element',id,**fields)
def doubt(place,reading,alternatives,reason):up('doubts','place',place,reading=reading,alternatives=alternatives,reason=reason)
def add_doubt(place,reading,alternatives,reason):ed['report_appends']['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence='low',reason=reason))
def add_change(id,b,place,c,h,final,evidence,kind,consequential=False,category='1'):
 import csv
 boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((S/f'{p}_boxes.tsv').open(),delimiter='\t')}
 ed['report_appends']['changes'].append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/{p}_second_{b}.png',box=boxes[b],confidence='low' if r'\unsure' in final else 'high',kind=kind,against_c=True,against_h=True,marked_in_h=False,consequential=consequential,error_category=category))

decision('B01','The thin sign has the continuous curved upper and lower parts supporting S, while 5 remains possible. The second reading adds only the marginal wrapper; no authorial foliation is established.')
cnew=r'\unsure{C_{01}|c_{01}}'
b02=cmp['B02']['first'].replace(r'{$c_{01}$}',r'{$'+cnew+r'$}')
e='The enlarged center label has a broad open C body, with a closed lower 0 and separate short 1. Its size favors capital C but does not securely exclude lowercase c. All ten labels, the three rays, thin right boundary and interior pen strokes remain present; the second array does not replace the drawing.'
decision('B02',e,b02)
rep(r'{$c_{01}$}',r'{$'+cnew+r'$}')
change('P02b',place='Upper-left drawing: C/c label beside center',final=cnew,evidence=e,confidence='low',against_c=True,against_h=True)
change('P02c',final=b02)
up('decisions','id','M0295',decision='undecided',reading=cnew,evidence=e,confidence='low')
add_doubt('P02 center label case',cnew,'C_01 | c_01',e)
decision('B03','After turning the target to its natural orientation, the long hooked relation lies to the left of a d-like body and raised prime. This supports the inherited superset-d-prime candidate. The unrotated vertical 3/omega interpretation is not preferred; the exact relation remains doubtful.',crop=f'crops/{p}_root_B03upright_corrected.png')
gnew=r'\unsure{i|2|1}'
b04=cmp['B04']['first'].replace(r'\unsure{i}',gnew)
e='The upper label consists of a long upright and a separate curved raised stroke. Neither a complete 2 nor a conventional dotted i is secure; retain i as the first candidate and record 2/1 alternatives. The middle 1 and lower closed 0 are clear. The five blobs, crossing segments, small isolated dot, horizontal gap and two complete arrows remain as drawn.'
decision('B04',e,b04,outcome='Retain the preferred upper-label reading and add local alternatives; this uncertainty alone is not a new primary C correction.')
rep(r'\node[left] at (1203,179) {$\unsure{i}$};',r'\node[left] at (1203,179) {$'+gnew+r'$};')
change('P04a',final=gnew+r';\quad1;\quad0',evidence=e,confidence='low')
change('P04b',final=b04)
up('decisions','id','M0297',reading=gnew,evidence=e)
doubt('P04 upper graph label',gnew,'i | 2 | 1',e)
sigma=r'\Sigma_{i_0i_1\mathord{\cdot-}i_n}'
e='Between i_1 and i_n the crop contains one low point followed by one short horizontal stroke, not three individually visible points. Endpoints and subscripts remain unchanged.'
decision('B05',e,sigma)
rep(r'\Sigma_{i_0i_1\ldots i_n}',sigma)
add_change('A01','B05','Sigma flag-index punctuation',r'\Sigma_{i_0i_1\ldots i_n}',r'\Sigma_{i_0i_1\cdots i_n}',sigma,e,'omission',False,'3')
up('notation','form',r'\Sigma_{i_0i_1\ldots i_n}',form=sigma)
inv('E05',first_words_or_objects=sigma+'; foncteur contravariant par rapport aux drapeaux variables')
word=r'\deleted{\unsure{simplicial|covariant}}'
e='The cancelled word has an early dotted short stroke, two internal tall stems consistent with p/l, a second dotted i-like stroke and a tall final l-like ending. These favor simplicial over covariant, whose expected internal stems are not supported. Crossing still obscures several joins, so covariant remains an alternative.'
decision('B06',e,word)
rep(r'\deleted{\unsure{covariant}}',word)
change('P05',final=word,evidence=e,against_c=True,against_h=True)
doubt('P05 cancelled word',word,'simplicial | covariant',e)
inv('E06',first_words_or_objects=r'\unsure{simplicial|covariant}')
up('deletion_insertion_review','text',r'\deleted{\unsure{covariant}}',text=word,evidence=e)
told=r'\unsure{{:}\ldots|i_1\ldots}'
tnew=r'\unsure{{:}\mathord{\cdot-\cdot}|i_1\mathord{\cdot-\cdot}}'
b07=cmp['B07']['first'].replace(told,tnew)
e='The live words retain the p descender and ending of drapeaux and the plural variables; diverses is not supported. The tuple interior has a high point above a low pill, then a low point, short dash and point. Preserve that point/dash geometry within the existing colon-versus-i_1 uncertainty. Endpoint marks are i tittles, not extra primes.'
decision('B07',e,b07)
rep(told,tnew)
for id in ['P06c','P06d']:
 old=next(x['final'] for x in r['changes'] if x['id']==id)
 change(id,final=old.replace(told,tnew),evidence=e)
doubt('P06 tuple interior',tnew,'colon-like pair plus point-dash-point | i_1 plus point-dash-point',e)
decision('B08','The open ring is distinctly above and right of b; the separate filled, angular mark lies directly above T. Its blackness does not by itself resolve live bullet versus cancelled circle. Both marks, k<i and the nested parentheses are retained; the second reading leaves the first mark unnamed.')
oldpost=r'\deleted{\unsure{\varnothing}}'
newpost=r'\unsure{\deleted{\varphi}|\varphi|\deleted{\varnothing}}'
b09=cmp['B09']['first'].replace(oldpost,newpost)
e='The small post-X_j sign has a dense upper curl and a distinct lower loop/descending return, favoring phi over a simple slashed circle; its crossing/deletion state is not secure. Keep cancelled phi first, live phi and cancelled empty-set alternatives. The pre-Tub loop is independently crossed. The overwritten index groups and curved leader to the sole lower i<k<j remain. A wider crop below that leader shows blank space: there is no second independent i<k<j display.'
decision('B09',e,b09)
rep(oldpost,newpost)
rep('\\[i<k<j\\]\n\n','')
change('P08b',final=r'X_j'+newpost+r'\setminus',evidence=e,against_c=True,against_h=True)
doubt('P08 cancelled post-X_j symbol',newpost,'cancelled phi | live phi | cancelled empty-set-like sign',e)
inv('E09',first_words_or_objects=b09)
inv('E11',kind='text',first_words_or_objects=newpost)
up('deletion_insertion_review','text',oldpost,text=newpost,scope_attachment='Post-X_j sign is separate from the live setminus; cancellation itself remains uncertain.',evidence=e)
ed['report_removals'].append(dict(collection='inventory',match={'element':'E14'}))
add_change('A02','B09','Duplicated lower range removed',r'\[i<k<j\]',r'$i<k<j$ plus claim of repetition','One inserted i<k<j attached to the union; no extra display','The lower range appears once, at the end of the curved leader. The wider root_indexscope crop extends below it to blank space. Both witnesses duplicated that same insertion as separate text.','addition',True,'3')
lo=r'\unsure{\delta|d}';ln=r'\unsure{\delta|d|\varphi}'
dotold="\\diagram{\\begin{tikzcd}\\bullet\\arrow[d]\\\\d'\\end{tikzcd}}"
dotnew="\\diagram{$\\begin{array}{c}\\bullet\\\\\\unsure{\\downarrow|\\cup}\\\\d'\\end{array}$}"
b10=cmp['B10']['first'].replace(lo,ln).replace(dotold,dotnew)
e='The rotated square has two hooked rightward arrows and two downward arrows, with delta labels above and d labels below. The word shows the tall f, following i-like stroke and joined naux ending, supporting cofinaux rather than cofaces. The lower-left relation-array loop admits phi in addition to delta/d. The isolated point is secure; the curved stroke below it can be a one-sided down-arrow or cup-like stroke, so its exact interpretation remains local uncertainty.'
decision('B10',e,b10)
rep(lo,ln);rep(dotold,dotnew)
for id in ['P10a']:
 old=next(x['final'] for x in r['changes'] if x['id']==id)
 change(id,final=old.replace(lo,ln),evidence=e)
change('P10c',final=dotnew,evidence=e)
up('decisions','id','M0299',evidence='The isolated filled point is secure. The curved stroke below remains arrow/cup-like and is separately qualified in the final diagram.')
doubt('P10 lower-left array label',ln,'delta | d | phi',e)
add_doubt('P10 stroke below isolated point',r'\unsure{\downarrow|\cup}','down-arrow | cup-like stroke',e)
inv('E15',first_words_or_objects='Square, relation array, cofinaux, separate point / uncertain down-arrow or cup-like stroke / d-prime diagram')
inv('E17',first_words_or_objects=next(x['first_words_or_objects'] for x in r['inventory'] if x['element']=='E17').replace(lo,ln))
inv('E18',first_words_or_objects=dotnew)
decision('B11','A diagonal cancellation crosses Sigma, i-comma-j, equals and the T; the independent final point is visible. The second reading changes only math/period bracketing. Keep the cancelled formula and stop.')
b12=cmp['B12']['first'].replace(r'\cap X_k\arrow',r'\cap\unsure{X_n|X_k}\arrow')
e='The index after the intersection X is a low arch with a rightward foot, favoring n; it lacks the clear upright-and-two-arm k shape in the nearby union bound. Retain k as an alternative rather than regularizing the formula. The range visibly has the extra lower stroke of <=, and the downward arrow starts under V_i,j. The separate X lies outside this box and is covered at B13.'
decision('B12',e,b12)
rep(r'\cap X_k\arrow',r'\cap\unsure{X_n|X_k}\arrow')
add_change('A03','B12','Intersection object index in V formula',r'X_k',r'X_k',r'\unsure{X_n|X_k}',e,'misread symbol or index',True)
add_doubt('P12 intersection-object index',r'\unsure{X_n|X_k}','n | k',e)
inv('E20',first_words_or_objects=next(x['first_words_or_objects'] for x in r['inventory'] if x['element']=='E20').replace(r'\cap X_k\arrow',r'\cap\unsure{X_n|X_k}\arrow'))
decision('B13','The isolated object has two crossing strokes of X with no attached index or exponent. The second reading differs only by math delimiters. Retain its separate position to the left of the vertical-arrow target.')
decision('B14','The detached V label has dotted i, a descending j and a clear k with upright and arm. It is independent of the larger lower diagram. Math delimiters alone differ.')
b15=cmp['B15']['first'].replace(r'\mathcal V_{ijk}\arrow[r]',r'\mathcal V_{ij\unsure{n|k}}\arrow[r]')
e='The upper-left label of the large diagram ends in a small n-like arch, unlike the clearly branched k in the separate B14 label and the upper-right X_k. Preserve n|k locally. The top connector has a left hook and no terminal head; the lower horizontal shaft and right X_k are struck. The dashed diagonal and its short angular endpoint strokes remain distinct from the vertical arrow, with the wave/r ambiguity retained.'
decision('B15',e,b15)
rep(r'\mathcal V_{ijk}\arrow[r]',r'\mathcal V_{ij\unsure{n|k}}\arrow[r]')
change('P13b',final=b15)
inv('E23',first_words_or_objects=b15)
add_change('A04','B15','Upper-left label of lower diagram',r'\mathcal V_{ijk}',r'V_{ijk}',r'\mathcal V_{ij\unsure{n|k}}',e,'misread symbol or index',True)
add_doubt('P13 upper-left final index',r'\unsure{n|k}','n | k',e)
decision('B16','The slanted equality retains the low i-like stroke only under the first lambda, one first prime and two primes on the right lambda and T. The first T raised mark has a small body with detached material and remains prime-versus-i uncertain. The inequality reads a<=Inf, with one unindexed first lambda-prime and low i at the last. The second i/1 doubt does not outweigh the repeated i form; no symmetric indices are supplied.')
decision('B17','The thin digit has the open upper rise and closed lower bowl of 6, with a separate underline. The second reading adds only the marginal wrapper.')
ed['report_appends']['notes'].extend([
 dict(id='N08',text='Independent second-reading adjudication: all 17 nonidentical targets were personally inspected by the main reader. Targeted rotation resolved the orientation at B03; root_postXj, root_indexscope and root_labelC address only the outstanding sign, duplication and letter-case questions.'),
 dict(id='N09',text='The i<k<j below the second Sigma formula is the insertion at the end of the curved union-index leader. It occurs once. Both supplied witnesses duplicated it as an additional display; inventory E14 was removed as that duplicate, while E13 remains.'),
 dict(id='N10',text='Point/dash punctuation is preserved literally in the Sigma flag subscript and tuple. The lower formula intersection index and the large diagram initial-object last index favor n but retain k as an alternative. Neither is made k merely to fit the bound or neighboring labels.'),
])
up('notes','id','N02',text='The live phrase is "foncteur contravariant par rapport aux drapeaux variables". The cancelled preceding word favors simplicial with covariant retained as an alternative. The marginal word reads cofinaux; no unstated direction or universal property is added.')
ed['report_appends']['check_events'].append(dict(statement_id='150007-independent-audit',type='independent image comparison',outcome='17 nonidentical targets personally inspected; local source/report revisions serialized; no mathematical normalization.'))
assert [x['box'] for x in ds]==list(cmp)
out.write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
(S/f'{p}_edits.json').write_text(json.dumps(ed,ensure_ascii=False,indent=2)+'\n')
print(p,len(ds),'decisions;',sum(x['decision']=='revise' for x in ds),'revised boxes')
