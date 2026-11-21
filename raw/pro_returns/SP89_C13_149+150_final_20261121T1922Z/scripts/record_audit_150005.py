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

pairs_by_box={}
def revise(box,evidence,outcome,pairs,crop=None):
 pairs_by_box[box]=pairs;decision(box,evidence,outcome,pairs,crop)
lettercl=r'\unsure{cl|ch|des}'
shortops=r'\unsure{ops|sps|ssi}'
oldcancel=r'\unsure{Si on a la fidélité, au contraire,}'
newcancel=r'\unsure{Si on a la fidélité, on aurait,|i.e. la fidélité, on aurait,}'
oldcomme=r'\inserted{\unsure{tt}}'
newcomme=r'\unsure{\inserted{tt}|le|$\downarrow$}'
dotdash=r'$\unsure{\mathinner{\cdot-\cdot}|\ldots}$'

revise('B01','The definition label has d/e/f with no independent high accent. The word before X has a longer low join than a certain de, admitting dans.','Read def and prefer dans with de as an alternative.',[(r'\mathrm{déf}',r'\mathrm{def}'),('ouvert de',r'ouverts DUMMY')] if False else [(r'\mathrm{déf}',r'\mathrm{def}'),('ouvert de',r'ouvert \unsure{dans|de}')],crop='crops/150_scan005_P01.png')
revise('B02','The NB phrase ends in the long élém-ent-aire sequence. Its initial relation has a separate lower stroke, supporting subset. No second close follows the inverse-image closing parenthesis.','Read élémentaire, retain the subset sign and cancelled quantifier uncertainty, and remove the unwritten outer close.',[("est l'essentiel",'est élémentaire'),(r'\overline{\varphi^{-1}(B)})',r'\overline{\varphi^{-1}(B)}')],crop='crops/150_scan005_P02.png')
decision('B03','The crossed preimage retains only partial phi/exponent strokes. Ouv. lies below U and the empty-set sign has a traversed oval, not a slashed circle.','Retain the qualified cancelled group, lower annotation, and phi-shaped empty set.')
revise('B04','The small x below Ouv belongs to its subscript. V= is raised over phi(U), while the later quantified variable is a hooked y. In the second Ouv parenthesis the small crossed argument looks like x but does not securely distinguish case.','Keep the positions and literal quantifier punctuation; qualify that one x/X argument.',[(r'\forall(U\in\operatorname{Ouv}(X))',r'\forall(U\in\operatorname{Ouv}(\unsure{x|X}))')])
decision('B05','Both empty-set glyphs have oval/stem forms. The lower annotation literally uses crossed X in the complement, and the negated membership points toward y.','Retain the first reading, including the literal X complement and underbrace placement.')
decision('B06','One long horizontal rule spans the page.','Retain the existing rule representation.')
revise('B07','The second degree digit has a curved/angular body admitting 2/7. The endings of images inverses have low s-like returns. After bien sûr the short group favors par; two parallel strokes follow, rather than securely separated e/x letters.','Qualify the digit, prefer plural images inverses, and preserve the equals-shaped abbreviation with local alternatives.',[('1° et 2°)',r'1° et \unsure{2°|7°})'),('par image inverse',r'par \unsure{images inverses|image inverse}'),('(pas $=$ pour',r'(\unsure{par|pas} $\unsure{=|\mathrm{ex.}}$ pour')])
revise('B08','The final low return after équivalence may be s, but it is not isolated cleanly. The ending en principe is visible at the start of the neighboring B09 crop.','Retain the first preferred plural and qualify the ending; retain the complete parenthesis.',[("d'équivalences",r"d'\unsure{équivalences|équivalence}")])
decision('B09','The cancelled opening retains A/d/m-like bodies compatible with Admettons. The condition labels and raised 3 bis remain visible; the small intervening words are covered by the long strike.','Retain the existing qualified cancelled passage and added label.')
revise('B10','The condition phrase is above the baseline; the long middle word is compressed enough to admit présence/plus. Above the crossed final group, L’inverse has a tall L, apostrophe, and readable inverse ending.','Qualify the raised condition wording and restore the separate L’inverse insertion.',[('en présence de',r'\unsure{en présence de|en plus de}'),(r"\deleted{$I$ \unsure{l'inclusion}}",r"\deleted{$I$ \unsure{l'inclusion}} \inserted{L'inverse}")],crop='crops/150_scan005_root_leftmiddle.png')
revise('B11','In the cancelled line, the later group has on / aurait with a final crossed t, not the longer contraire sequence. The earlier opening is still struck. The wider original shows the following live n’est pas vrai, exemple I=.','Prefer on aurait within the uncertain cancelled clause; keep the live continuation omitted by the narrow second crop.',[(oldcancel,newcancel)],crop='crops/150_scan005_root_leftmiddle.png')
decision('B12','The cancelled drawing has four visible points and only two discernible arrowheads through its heavy strokes. The live fork has three points, with arrows from both lower points toward c.','Retain the first drawing and its actual cancellation strokes; do not supply concealed edges.')
decision('B13','The live short word after the cancellation has an a/v/e/c sequence. The three non-emptiness/emptiness glyphs are phi-shaped. The low on a group remains compressed.','Retain avec, the qualified on a, and the inserted nonempty X_i statement.')
revise('B14','Suppose ends before désormais without a separate ra. The crossed group after U_i has a central q descender and a later l-like stem, favoring lesquels; the replacement non-emptiness expression is raised.','Retain suppose and the insertions, but qualify the cancelled group with lesquels preferred.',[(r'\deleted{tels que}',r'\deleted{\unsure{lesquels|tels que}}')])
decision('B15','The long isolated stroke after et has no recoverable letters beneath it; its status as cancellation or dash cannot be settled. U is written after de.','Retain both source uncertainties and the literal U.')
revise('B16','The short preposition before U is compressed; de remains preferred but avec/sur cannot be excluded. The closing parenthesis is immediately followed by Ainsi, with no independent point.','Qualify the short preposition and remove the unwritten period.', [('stricte de $U$).',r'stricte \unsure{de|avec|sur} $U$)')],crop='crops/150_scan005_P14.png')
decision('B17','The wider P14 crop shows Ainsi, les strat. ps. fidèles des immediately before the second excerpt. The remaining préfaisceau/locales wording agrees.','Retain; the beginning is absent only because the second crop starts later.',crop='crops/150_scan005_P14.png')
revise('B18','At the paper edge an open c-like curve precedes a tall loop and low terminal return; a fully closed initial d is not secure.','Prefer cl, with ch/des retained as local alternatives.',[(r'\unsure{des}',lettercl)])
decision('B19','The thin lower folio has the same angular 4 body.','Retain the margin wrapper and foliation.')
revise('B20','The raised instruction has a large opening and compressed low humps; the p-count does not securely choose Supposons against Prenons. The second crop also includes the beginning of the separately recorded cancellation.','Retain Supposons preferred with Prenons as an alternative; do not duplicate the following cancelled clause.',[(r'\inserted{Supposons $J$ minimal}',r'\inserted{\unsure{Supposons|Prenons} $J$ minimal}')],crop='crops/150_scan005_P17.png')
decision('B21','The negated relations have open subset bodies with crossing strokes, not secure membership symbols. The lower J-prime mark remains 1-like but uncertain. The boxed/diagonal cancellation encloses the whole passage; Soit has a separate underline inside it.','Retain the first reading and its extensive local uncertainties; the more detailed letter/subscript alternatives are not resolved by the crossed ink.')
revise('B22','A tall mark and lower point follow the first J. No independent comma follows fini. The small raised en I group has letter bodies and its curved leader attaches to non fermé below. After that phrase the three marks are point/dash/point.','Restore the exclamation, move/read the insertion at non fermé, remove the unwritten comma and preserve the literal point/dash sequence.',[('tels $J$ (','tels $J$! ('),('fini, pour','fini pour'),(r'pour simplifier\inserted{$\subset I$})','pour simplifier)'),('non fermé,',r'non fermé \inserted{en $I$},'),(r'\ldots',dotdash)])
revise('B23','The first grand-like group has a g descender followed by a compressed r/d-like ending; the second has an independent terminal point. The earlier ellipsis-like mark has a dash between two points. On ait retains its final t.','Prefer the short grd forms with grand alternatives; preserve the punctuation shapes and retain tt/on ait.',[(r'\ldots',dotdash),('plus grand él.',r'plus \unsure{grd|grand} él.'),('plus grand\n',r'plus \unsure{grd.|grand}'+'\n')])
revise('B24','A low comma follows the barred-j-prime inclusion. The sign after J_0 has two very short marks whose horizontal extent does not securely distinguish equality from colon.','Restore the comma and qualify the small equality/colon mark.',[(r'\subset J$. Donc',r'\subset J$, Donc'),(r'$J_0=J\setminus',r'$J_0\unsure{=|:}J\setminus')])
revise('B25','The i/j comparison after avec has a separate lower bar under its angle. The short preceding existential/et-like mark remains ambiguous. In the cancelled phrase, the small prefix can be i∈ or i.e. under the strike.','Read i≤j literally and qualify the cancelled prefix; retain the J_0 notation supported by its repeated hooked forms.',[('avec $i<j$',r'avec $i\leq j$'),(r'\deleted{$i\in\unsure{\overline j\cap I}$}',r'\deleted{\unsure{$i\in\overline j\cap I$|i.e. $\overline j\cap I$}}')])
revise('B26','The disjointness phrase has réunion/disjointe letter groups. The terminal conjunction has a low n/c-like ending without a secure high apostrophe/accent. The equality before the union is reduced to two short marks.','Prefer donc with d’où retained as an alternative; qualify the first equality/colon sign.',[(r'X_J^*=X_{J_0}',r'X_J^*\unsure{=|:}X_{J_0}'),("d'où",r"\unsure{donc|d'où}")])
revise('B27','The boundary marker is a filled point. Def has no separate accent. A comma occurs immediately after the equality before the unstarred X_{J_0}. The prose has sans qu’on ait.','Remove the unwritten definition accent and restore the comma; retain the bullet and the rest literally.',[(r'\mathrm{déf}',r'\mathrm{def}'),(r'X_{J_0}^*=X_{J_0}',r'X_{J_0}^*=,X_{J_0}')])
decision('B28','The underlined word has the tall f, low erm group, separate accent and final e of fermée. Fini follows I-prime later, and the ending has plural les propriétés précédentes with a comma.','Retain the first reading; the second confuses distinct fermée/fini occurrences.')
decision('B29','The empty-set sign is traversed-oval phi; the conjunction et and the uncertain cancelled symbol are separate. The J_0 forms match the established hooked notation.','Retain the first reading.')
revise('B30','The line below the two inclusions joins the leader to the small annotation on the next formula; it is not an independent underline. The short word before i.e. has ce bodies without a secure further ci.','Keep the inclusions and leader interpretation; prefer ce with ceci retained as an alternative.',[(r'\unsure{ceci|ce}',r'\unsure{ce|ceci}')],crop='crops/150_scan005_root_rightstrict.png')
revise('B31','Above J_0 the small annotation is barred J followed by two equality strokes. The right end has a distinct crossed group above the final live barred j, in addition to the earlier cancelled blob. Pour tte remains visible.','Correct the raised annotation and restore the separate upper cancelled group without inventing its obscured word/symbol.',[(r'\overbrace{J_0}^{\subset\overline j}',r'\overset{\overline J=}{J_0}'),(r'\deleted{\unsure{\overline j}}\overline j)',r'\deleted{\unsure{\overline j}}\overset{\deleted{\unsure{\overline j|\illegible{1}}}}{\overline j})')],crop='crops/150_scan005_root_rightstrict.png')
revise('B32','The mark after Comme is compact and may be a raised tt, le, or a downward pointer. The relation after J-prime has an open curved body without a secure middle membership bar. Both large barred J forms retain their capital shapes.','Broaden the first mark’s uncertainty and resolve the relation to subset; retain the other cancellations.',[(oldcomme,newcomme),(r"J'\unsure{\subset|\in}",r"J'\subset")],crop='crops/150_scan005_P28.png')
decision('B33','Seventeen filled points are visible: six left, three within the closed lobed contour, one beside j and seven right. J_0 lies lower left.','Retain the existing geometry, labels and point count; coordinate-system differences are representational.')
revise('B34','The heading number has an upper curved stroke and poorly separated lower return, admitting 3 or question mark. The cancelled abbreviation above retains two crossed stems and a low e-like ending.','Qualify the heading character while retaining the first preferred 3 and the cancelled tte.',[('3 conditions',r'\unsure{3|?} conditions')])
revise('B35','The boundary marker is filled; def has no independent accent. After underlined NB are compact o/p/s-like bodies, with a p-like descender, not a long arrow shaft. Two pour words and the single-shaft final arrow are visible.','Prefer ops with sps/ssi alternatives, read def without an accent, and retain the repeated pour and final arrow.',[(r'\mathrm{déf}',r'\mathrm{def}'),(r'\unsure{ssi}',shortops)])
decision('B36','The cancelled equality contains a separately blackened token after equals, then a partly crossed singleton and union i. Its original token is not recoverable.','Retain the explicit empty unsure payload and the qualified singleton; do not invent a mathematical object.')

# These exact replacements do not overlap: repeated observations in B36 and
# neighboring context-only boxes have retained decisions.
for d in rows:
 if d['decision']=='revise':replace(C[d['box']]['first'],d['final'])
source=(W/'pages'/f'{page}.tex').read_text()
for x in E['source_replacements']:
 assert source.count(x['old'])==1,(x['old'][:120],source.count(x['old']))
 source=source.replace(x['old'],x['new'])
assert [x['box'] for x in rows]==[x['box'] for x in C.values() if not x['token_equal']]
assert not (W/'second'/f'{page}_root_decisions.json').exists()
subprocess.run([sys.executable,str(W/'scripts'/'append_root_decisions.py'),page],input=json.dumps(rows,ensure_ascii=False),text=True,check=True)
# Report updates follow below; source is not changed by this serialization step.
