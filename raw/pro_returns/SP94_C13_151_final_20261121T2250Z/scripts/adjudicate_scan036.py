"""Main-reader decisions after visual inspection of the blind crops."""
from pathlib import Path
import csv, json
W=Path(__file__).resolve().parents[1]
p='151_scan036'
r=json.loads((W/'reports'/f'{p}.json').read_text())
t=(W/'pages'/f'{p}.tex').read_text()
dec={}
def d(b, decision, evidence, changed=False):
    dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b01','retain first','The two crossing subscript strokes have the same form as X in the neighboring X-star; their reduced size is due to subscript placement. The recurring pair is Y,X. No distinct lower-case ductus compels x. The display wrapper is editorial.')
d('b02','retain first','The article has the open trough and terminal return of du, not a separate e; diagramme ends with one long return and no separate plural s.')
d('b03','mark doubt on raised round number','The 1 is an oblique upright; the following small rounded mark is raised. Its position permits an ordinal circle as the blind reader proposed, while the preceding diagram-reference wording supports 10. The ink does not securely distinguish them. The insertion leader ends before groupoïdes; capital Quand is clear.',True)
d('b04','retain first','Only the opening parenthesis and two connected lobes of 8 precede the closing parenthesis; there is no separate 1. The last subscript X has the same two-crossing-stroke form as the neighboring X-star. Script V and its star are visible.')
d('b05','retain live text; broaden cancelled alternatives','The long stroke crosses the lower phrase and leaves the raised en considérant E_X* comme live. Its middle bodies are merged with the strike; both comme des systèmes and comme un système remain possible. The surviving comma is after the live ces systèmes; a terminal comma in the cancelled phrase is not independently separable from the strike.',True)
d('b06','retain first','The crop edge and diagonal note overlap the beginning un ens.; the blind omission concerns edge context. The upright roof with two legs gives capital Pi, and the crossed subscript shares the established X form. No main-text words are removed.')
d('b08','retain first','Two horizontal bars followed by a separate small s are plainly present between ces and ensembles. The raised considérés replaces the crossed uncertain munis. The blind omission of =s is rejected; paragraph wrappers do not change the reading.')
d('b09','retain first','The last word has a tall crossed t followed by the low connected eur sequence and terminal s; opérateurs is supported, not opérations. The capital Pi roof and legs, script V, and crossed qui are visible.')
d('b10','retain marginal reading with abbreviation qualification and no hom stop','The opening D has a tall loop; two horizontal bars stand after on a. The short veut has a low v onset and crossed t, unlike dit. Pi_1(Y) has one forked Y, and apparaît has its descending p and final t. The small un before quotient and et after the D formula survive. The cancelled group formula remains wholly unsure, with no illegible placeholder inside mathematics. The abbreviated ss-gr. is compressed and crossed by main-text writing, so is now explicitly unsure rather than expanded. After hom there is no independent stop before de. Crossing main-text fragments and the apparent angular outline are already accounted for in the main lines; they are not extra marginal words or a separate diagram. The arrow, target superscript I, and underbrace label remain.',True)
d('b12','retain first','The doubtful article is before the strike; the strike begins at the following a of applic. and ends after à. Its two long p descenders and shortened ending support the abbreviation rather than an expansion to applications. The large looped initial of Géométrie is capital G. The la/les doubt remains.')
d('b13','retain first','The D has two distinct near-parallel upright strokes inside the outer bowl, unlike the plain marginal D. Double-struck D is retained; the parenthesized insertion and its leader are unchanged.')
d('b14','retain first','The D again has a doubled upright; its small subscript is a closed oval without the exit of neighboring a. Retain double-struck D-star with subscript 0, as independently confirmed for the index.')
d('b15','retain first','The pale digits read 35. The margin wrapper records their provenance and adds no ink.')
old=r'\deleted{\unsure{comme des systèmes}}'
new=r'\deleted{\unsure{comme des systèmes|comme un système}}'
t=t.replace('(10) Quand',r'$(\unsure{10|1^\circ})$ Quand').replace(old,new).replace('le ss-gr.',r'le \unsure{ss-gr.}').replace('hom. de','hom de')
for row in r['changes']:
    if row['id']=='r02':
        row['final']=r'$(\unsure{10|1^\circ})$'
        row['confidence']='low'
        row['evidence']=dec['b03']['evidence']+' Blind crop second_151_scan036_b03.jpg.'
    if row['id']=='r03': row['evidence']=row['evidence'].replace('between (10) and Quand','between the parenthesized number and Quand')
    if row['id']=='r06':
        row['final']=row['final'].replace(old,new)
        row['evidence']+=' Blind review leaves comme un système as an additional possible cancelled reading.'
    if row['id']=='r13':
        row['final']=row['final'].replace('le ss-gr.',r'le \unsure{ss-gr.}').replace('hom. de','hom de')
        row['evidence']+=' Blind review removes the unsupported stop after hom and marks the compressed ss-gr. uncertain.'
for q in r['doubts']:
    if q['reading']==old:
        q['reading']=new;q['alternatives']='comme des systèmes / comme un système';q['reason']=dec['b05']['evidence']
r['doubts'] += [
 {'place':'main line 3, number before Quand','reading':r'$(\unsure{10|1^\circ})$','alternatives':'10 / ordinal 1°','confidence':'low','reason':dec['b03']['evidence']},
 {'place':'marginal line 5, abbreviation','reading':r'\unsure{ss-gr.}','alternatives':'Exact abbreviated strokes obscured; no expanded form supplied.','confidence':'low','reason':'The small bodies are compressed and crossed by the main text.'}]
r['changes'].append({'id':'r21','place':'marginal line 8, after hom','c':'hom.','h':'(included in H’s omitted marginal passage)','final':'hom','evidence':'No separate stop is visible between the final return of hom and de in blind crop second_151_scan036_b10.jpg. The whole H omission is already counted in r13.','confidence':'medium','kind':'text not on the page','error_category':9,'diff_c':True,'diff_h':False,'marked_h':True,'crop':'crops/second_151_scan036_b10.jpg','box':[15,550,635,1994],'consequential':''})
r['notes'][1]=r['notes'][1].replace('after (10)','after a number now left unsure as 10 / 1° following blind review')
r['notes'].append('scan036.N11 Blind review: the raised round mark after 1 is not securely distinguished from an ordinal circle; both readings are retained. The strike permits a singular cancelled comme un système as well as the earlier plural reading. The compressed marginal ss-gr. is now marked doubtful and the unsupported stop after hom is removed. No missing words, expanded abbreviation, or diagram is supplied from context.')
for a in r['abbreviations']:
    if a['form']=='hom.':a['form']='hom'
    if a['form']=='ss-gr.':a['form']=r'\unsure{ss-gr.}'
with (W/'second'/f'{p}_comparison.tsv').open() as f: comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f: boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
finals={'b03':r'$(\unsure{10|1^\circ})$ Quand les \inserted{trois} groupoïdes composants de','b05':comp['b05']['first'].replace(old,new),'b10':comp['b10']['first'].replace('le ss-gr.',r'le \unsure{ss-gr.}').replace('hom. de','hom de')}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'low' if b!='b10' else 'medium'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t)
(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
