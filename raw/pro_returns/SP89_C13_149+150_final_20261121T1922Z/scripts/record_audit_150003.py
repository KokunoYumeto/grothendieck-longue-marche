"""Serialize the main reader's explicit, visually adjudicated decisions."""
from pathlib import Path
import json, subprocess, sys
W=Path(__file__).resolve().parents[1]; page='150_scan003'
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

decision('B02','The tall final d and round retraced opening favor Ord. Older p-like ink remains inseparable. No independent accent is present over the possible older e.','Keep the unresolved layered operator, remove the unwritten accent from its alternative only.',[(r'\operatorname{Spéc}',r'\operatorname{Spec}')])
decision('B03','The raised p has its own descender and separate accent; its curved attachment meets the first o of ordonné.','Retain the inserted prefix; the second reader included extra baseline context.')
decision('B05','Two distinct parentheses enclose T and lowered 0; the outer prose close is separate. The wider original crop also shows l’axiome before de séparation.','Retain; omission of the earlier words is a crop-boundary difference.',crop='crops/150_scan003_root_upper.png')
decision('B06','The first prose word begins with an e-loop and ends in a low s-return: ens. The inserted pré is accented; the baseline ordonne has no separate accent in the wider original. The thick I has ordinary mathematical serifs.','Retain ens and the inserted pré, remove only the unwritten accent of baseline ordonne.',[('ordonné','ordonne')],crop='crops/150_scan003_root_upper.png')
decision('B07','The closed/open-set formulas, lower relation bars, singleton tilde, and explanatory wave are all visible. Extra espace top. lies before the target phrase.','Retain; macro aliases, apostrophe style and context extent account for the differences.')
decision('B08','A large D-like opening, a raised apostrophe-like stroke, and a further high mark survive before the f-descender. The strike obliterates most low joins; the later tall stroke and ending admit foncteurs but do not settle the phrase.','Prefer a doubtful D’où un opening, with Deux/lien alternatives; retain the whole passage as cancelled and unresolved.',[(r'\unsure{lien foncteurs|\illegible{1} fondamentales}',r"\unsure{D'où un|Deux|lien} \unsure{foncteurs|fondamentales}")])
decision('B09','After continue there is one horizontal mark appreciably longer than the small points in the same block. The arrow and preceding words agree.','Replace the terminal period by the visible dash.', [('continue.','continue --')])
decision('B10','The long line curves above the small added sentence and connects with the NB1 brace; it does not cross the bodies as a cancellation. The ≤ below I has both its angle and lower bar.','Retain the inserted generalization and the literal closure relations.')
decision('B11','Two tall initial legs join at the bottom, followed by a low shoulder and final e-loop. U+n+e is favored; the heavy strike still prevents certain separation. A capital B is not supported by the small final loop.','Prefer Une while retaining Vue/lien as cancelled alternatives.',[(r'\unsure{Vue|lien}',r'\unsure{Une|Vue|lien}')])
decision('B13','The abbreviated n-é-c group has a high mark and separate stop. After the cancellation, distinct ce / sera / celui / de groups remain, including the narrow final i of celui.','Retain néc. and ce sera celui de; no expansion or grammatical substitution.')
decision('B14','The second baseline supports sont, but the small terminal returns after intersection and ouvert merge with their last letters. They cannot securely establish the final s at both places.','Keep the first preferred plurality but mark both endings as uncertain.',[("intersections d'ouverts sont ouverts",r"\unsure{intersections|intersection} d'ouverts sont \unsure{ouverts|ouvert}")])
decision('B15','The initial C is followed by a small e-loop and long low s-like exit, with no separate i-dot; one independent point follows.','Prefer Ces, preserving Ceci/Cas as lower-confidence alternatives and retaining the point.',[(r'\unsure{Ceci|Cas}',r'\unsure{Ces|Ceci|Cas}')])
decision('B16','The first connector is a solid dot, the second an open circle. The first identity has a two-lobed E subscript, the second a rounded O; the second relation is an arrow.','Retain the literal formulas; math wrapper and arrow-length differences are representational.')
decision('B17','The line ends cond. with a separate stop, followed by the short d/u group and NB2; no close parenthesis follows.','Retain the abbreviation and du; reject expansion to condition.')
decision('B18','The supplied second box shows I→X, already present in the prose. The broader original P17 crop separately shows a horizontal rule below that baseline, starting well left of I and ending beneath X.','Retain the separator and the existing I→X sentence; record that the neutral box missed the rule itself.',crop='crops/150_scan003_P17.png')
decision('B19','The long p-descender begins pseudo-, followed by an independent hyphen and partition. A separate crossed une precedes it. The following punctuation has one definite point and an insecure second.','Retain pseudo-partition and the unresolved colon/period; the second excerpt omitted the prefix.')
decision('B20','The lower index has a hooked J return; the inverse-image argument has top and bottom bars of I. After its close, a comma and les are visible. The long bent stroke lies above continue ssi, not across their bodies.','Retain the inserted Posons definition, its les, and the following live words.')
decision('B22','The index has a separate high dot and retraced small body supporting i. After the tall t of ouverts a curved low s-return remains.','Retain ouverts and i; do not regularize the written plural.')
decision('B23','The initial index mark is a C-shaped complement sign before the tilde; both summation conditions and their vertical order are visible. Neighboring prose continues outside the narrower crop.','Retain complement notation and the existing surrounding prose.')
decision('B24','The tiny definition label has d/e/f strokes but no independently placed accent; the descending stroke nearby belongs to the upper word. The wider color crop confirms this separation.','Read the label def without supplying an accent.',[(r'\mathrm{déf}',r'\mathrm{def}')],crop='crops/150_scan003_root_B24wide.png')
decision('B26','No independent opening parenthesis occurs between fini and car; the closing parenthesis at the far right is clear. After est, the small opening bowl and l-stem support alors, not donc.','Remove the supplied opening parenthesis while retaining the written closing one.', [('fini (car','fini car')])
decision('B27','At the right edge, a low e-return follows the last dotted i, matching the earlier finie on the same line. The loc. and val. stops and paired opening quotation strokes are visible.','Read the final word finie, preserving the source agreement.', [('de val. fini','de val. finie')])
decision('B28','The initial fragments are torn and crossed; they do not securely separate into exclamation marks and words. At the right, an open c-like curve, low a-bowl and short r-like exit favor car over en, still weakly.','Keep the damaged cancellation and formula, prefer car as a doubtful final word.',[(r'\unsure{en}',r'\unsure{car|en}')])
decision('B29','The tiny top note retains a q-descender in quotient, a barred I, and crowded joins in the following verb. Lower lines show conditions, a long supplémentaires group, φ, the starred fibers and unicité. No independent leader establishes a new insertion within its sloping first line.','Retain the full six-line note and its existing unresolved first two groups; do not replace the visible lower wording by a partial excerpt.')
decision('B30','Quel ends at its l-return with no distinct s. After the apostrophe the short ens group lacks the long image sequence and g-descender.','Retain quel and l’ens; prefix and underline remain unchanged.')
decision('B31','Dans le lies on the ordinary line without an independent cancellation. Plus précisément is raised above a heavily crossed cluster; par and the starred family remain on the lower line. The tiny parenthetical par stays ambiguous.','Retain the separate revision layers and the explicit uncertainty around the small par.')
decision('B32','Before the crossing, a small d-bowl with tall stem and a separate apostrophe-like stroke survive. The remaining low joins and final ascender favor d’abord but cannot establish it completely.','Prefer doubtful d’abord, with tout/donc alternatives; retain the cancellation.',[(r'\unsure{tout}',r"\unsure{d'abord|tout|donc}")])
decision('B33','The next line begins with a tall f-loop and short aut sequence, not the repeated f-strokes needed for suffit. The final map has a closed loop and descender before soit.','Retain il faut and que φ soit; the phi-shaped empty-set signs remain literal.')
decision('B34','The map after donc has a tall crossing stem and small loop: φ remains favored, but f cannot be excluded locally. Surjective has its low final ve return, and the top. point is independent.','Add only a local φ/f uncertainty; preserve surjective and the other words.',[(r'Supposons donc $\varphi$',r'Supposons donc $\unsure{\varphi|f}$')])
decision('B36','The short group before réunions and its terminal return remain compressed enough to admit tte réunion. The last vowel of fermé merges with the insertion leader; a second e is insecure. The raised note begins cas with a low s-like exit.','Retain the first preferred wording with explicit noun/agreement uncertainty, and retain cas.', [('les réunions',r'\unsure{les réunions|tte réunion}'),('est fermé',r'est \unsure{fermé|fermée}')])
decision('B37','The group before I has a low d-loop and e-return. The conditional formula, cancelled x∈ and J-indexed starred term agree. The final on continues to a at the next baseline.','Retain de I and the on / a line continuation.')
decision('B38','The initial capital A has its crossbar and apex but no separate accent above it. The following cette has crossed t-strokes; préordre and est-il are separate groups.','Remove the supplied accent on A; preserve the source wording cette préordre est-il.', [('À quelles','A quelles')])
decision('B39','After the quotes, en is short; général begins with a g-descender and continues through compressed accented letters. The later chance and chaotique retain their distinctive beginnings. A single s and stop follow et.','Retain en général and the abbreviated sufficiency phrase.')
decision('B41','The local abbreviation has a raised t-like stroke and separate point. Above the cancelled transition, the capital and following low joins favor Plus but also admit a Récip-like group; the wider color crop leaves this unresolved.','Retain the revision state and preferred Plus, adding a competing reading only.',[(r'\unsure{Plus}',r'\unsure{Plus|Récip}')],crop='crops/150_scan003_root_transition.png')
decision('B42','Précis-like live ink and a separate crossed lower group are distinct. The f. and s. abbreviations have independent points. The quantifier has a clear insertion caret before l’on ait; another crossed formula follows.','Retain the explicit doubts and distinct insertion/cancellation scopes.')
decision('B43','After équiv, the small dark terminal mark can be a stop; no secure tall final t separates an expanded équivaut. The two decorations on i, the superset insertion and the following saturated-set text remain visible.','Prefer the doubtful abbreviation équiv., retaining équivaut as an alternative; leave the formulas unchanged.', [('équivaut',r'\unsure{équiv.|équivaut}')],crop='crops/150_scan003_root_transition.png')
decision('B44','After équivalence, the short loc. group precedes a long f-descender and finie, then a separate compressed assoc. group. There is no second full fibration word followed by φ.','Retain loc. finie assoc. literally.')
decision('B45','The right-edge verb has the paired descenders of appeler; the following line contains une, stratification fidèle and d’équiv. The faithful qualifier is visible between its quotation marks.','Retain the complete wording; the second reader omitted several visible groups.')
decision('B46','After the dash, dotted i, tall l and low s form ils. The next long group ends in ent; à une famille follows. The raised t and baseline stop in locᵗ. are distinct.','Retain ils correspondent à une famille and the local abbreviation.')
decision('B47','The partition word ends in a low n-return before a separate comma-like mark; no independent s is secure. Ensembliste has its high l and crossed t and remains visible.','Prefer singular partition with the former plural retained as an alternative.', [('partitions',r'\unsure{partition|partitions}')])
decision('B48','The raised indicée clause has independent horizontal strokes beneath it, distinct from the heavy lower cancellation. Below that strike, the first low group ends in a separate i-dot; the next has a long f-like descender and tall l/t-like strokes.','Restore underlining of the raised clause and prefer doubtful qui filtre below the cancellation.', [(r'\inserted{indicée par $I$ ordonné}',r'\inserted{\uline{indicée par $I$ ordonné}}'),(r'\unsure{tels que}',r'\unsure{qui filtre|tels que}')],crop='crops/150_scan003_root_bottom.png')
decision('B49','The initial d-loop, i-dot and j-descender support disjoints. In the wider original, telle que follows the slightly rising baseline after et, without a caret or replacement; its apparent elevation in the narrow crop does not establish insertion.','Retain the live wording disjoints et telle que.',crop='crops/150_scan003_root_bottom.png')
decision('B50','The first X_J has no independent upper star. The next line begins a d-loop followed by onc, not avec. The definition label here has a small separate accent, unlike B24.','Retain X_J, donc and the accented definition label at this occurrence.')
decision('B51','The tiny horizontal joins after X_J may contain est, but its letters cannot be isolated securely before the f-loop. The accented final e of fermé and the inner implication parentheses remain visible.','Mark est uncertain while retaining fermé and the established insertion scope.', [('X_J$ est fermé',r'X_J$ \unsure{est} fermé')])

# Exact source edits; no witness or fixed first/second reading is rewritten.
replace(r'\operatorname{Spéc}(X)',r'\operatorname{Spec}(X)')
replace(r'$I$ ens \inserted{pré}ordonné',r'$I$ ens \inserted{pré}ordonne')
replace(r'\unsure{lien foncteurs|\illegible{1} fondamentales}',r"\unsure{D'où un|Deux|lien} \unsure{foncteurs|fondamentales}")
replace('$f$ continue.','$f$ continue --')
replace(r'\unsure{Vue|lien}',r'\unsure{Une|Vue|lien}')
replace("intersections d'ouverts\nsont ouverts",r"\unsure{intersections|intersection} d'ouverts"+'\nsont '+r'\unsure{ouverts|ouvert}')
replace(r'\unsure{Ceci|Cas}.',r'\unsure{Ces|Ceci|Cas}.')
replace(r'$X_i\overset{\mathrm{déf}}=X_{\overline i}',r'$X_i\overset{\mathrm{def}}=X_{\overline i}')
replace('si $I$ est fini (car','si $I$ est fini car')
replace('de val. fini','de val. finie')
replace(r'\unsure{en}',r'\unsure{car|en}')
replace(r'\unsure{tout}',r"\unsure{d'abord|tout|donc}")
replace(r'Supposons donc $\varphi$',r'Supposons donc $\unsure{\varphi|f}$')
replace('telle que les réunions\nde fermés est fermé',r'telle que \unsure{les réunions|tte réunion}'+'\nde fermés est '+r'\unsure{fermé|fermée}')
replace('À quelles conditions','A quelles conditions')
replace(r'\inserted{\unsure{Plus}}',r'\inserted{\unsure{Plus|Récip}}')
replace('ce qui équivaut à',r'ce qui \unsure{équiv.|équivaut} à')
replace('partitions ensembliste',r'\unsure{partition|partitions} ensembliste')
replace(r'\inserted{indicée par $I$ ordonné}',r'\inserted{\uline{indicée par $I$ ordonné}}')
replace(r'\unsure{tels que}',r'\unsure{qui filtre|tels que}')
replace(r'$\Rightarrow X_J$ est fermé',r'$\Rightarrow X_J$ \unsure{est} fermé')

evidence={d['box']:d['evidence'] for d in rows}
for id,box,final,against_c in [
 ('P01','B02',r'\unsure{\operatorname{Ord}(X)|\operatorname{Spec}(X)}',False),
 ('P05a','B06',r'$I$ ens \inserted{pré}ordonne',True),
 ('P07','B08',r"\margin{\deleted{\unsure{D'où un|Deux|lien} \unsure{foncteurs|fondamentales}}}",True),
 ('P10','B11',r'\margin{\deleted{\unsure{Une|Vue|lien}}}',True),
 ('P12a','B14',r"\unsure{intersections|intersection} d'ouverts sont \unsure{ouverts|ouvert}",False),
 ('P13','B15',r'\unsure{Ces|Ceci|Cas}.',True),
 ('P26b','B27','i.e. loc. à ens. de val. finie',True),
 ('P27','B28',r'\margin{\deleted{\illegible{3} $\unsure{x\leq y}\Longleftrightarrow\overline{\{x\}}\subset\overline{\{y\}}$ \unsure{car|en}}}',True),
 ('P32','B32',r"\deleted{\unsure{d'abord|tout|donc}}",True),
 ('P34a','B34',r'les $X_i^*\ne\phi$. Supposons donc $\unsure{\varphi|f}$ surj. i.e. $X_i^*\ne\phi$',True),
 ('P36','B36',r'de fermés est \unsure{fermé|fermée} \inserted{(cas $\varphi$ loc. finie)}',False),
 ('P42a','B41',r'\inserted{\unsure{Plus|Récip}} \unsure{précis,}',False),
 ('P43a','B43',r'$\{i\}=\overline i\cap\widetilde i$ ce qui \unsure{équiv.|équivaut} à \deleted{$\unsure{\forall i\in I}$} $X_{\overline i}^*\cap X_{\widetilde i}^*=X_i^*$',True),
 ('P47','B47',r'$(X_i^*)_{i\in I}$, \unsure{partition|partitions} ensembliste de $X$',True),
 ('P48a','B48',r'\inserted{\uline{indicée par $I$ ordonné}}',True),
 ('P48b','B48',r'\unsure{qui filtre|tels que}',True),
 ('P51','B51',r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ \unsure{est} fermé ($\Rightarrow$ les $X_i^*$ loc. f.)}',True),
]:
    change(id,final=final,evidence=evidence[box],against_c=against_c,against_h=True,confidence='high' if box=='B06' else 'low' if box in ['B02','B08','B11','B28','B32','B41','B43','B48','B51'] else 'medium')

newchange('B09','S_B09_dash','NB1 terminal mark','$f$ continue.','$f$ continue.','$f$ continue --',evidence['B09'],'misread punctuation','10')
newchange('B24','S_B24_def','Definition label in the left closure formula',r'\mathrm{déf}',r'\text{déf}',r'\mathrm{def}',evidence['B24'],'abbreviation expanded or spelling modernised','8')
newchange('B26','S_B26_parenthesis','Opening parenthesis before car','fini (car','fini (car','fini car',evidence['B26'],'text not on the page','9')
newchange('B38','S_B38_accent','Capital A before quelles conditions','À quelles','À quelles','A quelles',evidence['B38'],'abbreviation expanded or spelling modernised','8')

for id,box,reading in [('M0241','B02',r'\unsure{\operatorname{Ord}(X)|\operatorname{Spec}(X)}'),('M0244','B15',r'\unsure{Ces|Ceci|Cas}'),('M0252','B41',r'\unsure{Plus|Récip}'),('M0255','B48',r'\unsure{qui filtre|tels que}')]:
    update('decisions','id',id,decision='undecided',reading=reading,evidence=evidence[box],confidence='low')
for place,box,reading,alts in [
 ('P01 operator','B02',r'\unsure{\operatorname{Ord}(X)|\operatorname{Spec}(X)}','Ord(X) / unaccented Spec(X); overtraced layers'),
 ('P07 cancelled phrase','B08',r"\unsure{D'où un|Deux|lien} \unsure{foncteurs|fondamentales}",'D’où un / Deux / lien; foncteurs / fondamentales'),
 ('P10 cancelled word','B11',r'\unsure{Une|Vue|lien}','Une / Vue / lien'),
 ('B14 terminal plurals','B14',r"\unsure{intersections|intersection} d'ouverts sont \unsure{ouverts|ouvert}",'terminal s at both nouns/adjectives uncertain'),
 ('P13 heading','B15',r'\unsure{Ces|Ceci|Cas}','Ces / Ceci / Cas'),
 ('P27 damaged cancelled line','B28',r'\illegible{3} $\unsure{x\leq y}\Longleftrightarrow\overline{\{x\}}\subset\overline{\{y\}}$ \unsure{car|en}','car / en; initial fragments unresolved'),
 ('P32 cancelled word','B32',r"\deleted{\unsure{d'abord|tout|donc}}",'d’abord / tout / donc'),
 ('B34 map letter','B34',r'\unsure{\varphi|f}','φ / f'),
 ('B36 noun and agreement','B36',r'\unsure{les réunions|tte réunion} de fermés est \unsure{fermé|fermée}','les réunions / tte réunion; fermé / fermée'),
 ('P41/P42 raised and live transition','B41',r'\inserted{\unsure{Plus|Récip}} \unsure{précis,}','Plus / Récip; précis and its punctuation still uncertain'),
 ('B43 abbreviation','B43',r'\unsure{équiv.|équivaut}','équiv. / équivaut'),
 ('P47 partitions wording','B47',r'\unsure{partition|partitions} ensembliste de X','partition / partitions'),
 ('P48 live group below cancellation','B48',r'\unsure{qui filtre|tels que}','qui filtre / tels que'),
 ('B51 tiny est','B51',r'\unsure{est}','est / no separately recoverable word before fermé'),
]:doubt(place,reading,alts,evidence[box])

for id,words in [('E09',r"\deleted{\unsure{D'où un|Deux|lien} \unsure{foncteurs|fondamentales}}"),('E12',r'\deleted{\unsure{Une|Vue|lien}}'),('E15',r'\unsure{Ces|Ceci|Cas}. deux foncteurs'),('E26',r'X_i\overset{def}=X_{\bar i}^*=\bigcup_{j\leq i}X_j'),('E29',r'\deleted{\illegible{3} ... \unsure{x\leq y} ... \unsure{car|en}}'),('E37',r"\deleted{\unsure{d'abord|tout|donc}}"),('E41','A quelles conditions cette préordre ...'),('E43',r'\unsure{Plus|Récip}'),('E53',r'\uline{indicée par I ordonné}'),('E55',r'\unsure{qui filtre|tels que}'),('E57',r'i.e. J fermé ⇒ X_J \unsure{est} fermé (⇒ les X_i^* loc. f.)')]:
    update('inventory','element',id,first_words_or_objects=words)

# Apply the same explicit literal updates only to the revision-review text field.
for a,b in [(r'\deleted{\unsure{lien foncteurs|\illegible{1} fondamentales}}',r"\deleted{\unsure{D'où un|Deux|lien} \unsure{foncteurs|fondamentales}}"),(r'\deleted{\unsure{Vue|lien}}',r'\deleted{\unsure{Une|Vue|lien}}'),(r'\deleted{\illegible{3} ... \unsure{en}}',r'\deleted{\illegible{3} ... \unsure{car|en}}'),(r'\deleted{\unsure{tout}}',r"\deleted{\unsure{d'abord|tout|donc}}"),(r"\deleted{\unsure{D'ailleurs}} \inserted{\unsure{Plus}}",r"\deleted{\unsure{D'ailleurs}} \inserted{\unsure{Plus|Récip}}"),(r'\inserted{indicée par $I$ ordonné}',r'\inserted{\uline{indicée par $I$ ordonné}}'),(r'\deleted{\illegible{4}} \unsure{tels que}',r'\deleted{\illegible{4}} \unsure{qui filtre|tels que}'),(r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ est fermé ($\Rightarrow$ les $X_i^*$ loc. f.)}',r'\inserted{i.e. $J$ fermé $\Rightarrow X_J$ \unsure{est} fermé ($\Rightarrow$ les $X_i^*$ loc. f.)}')]:
    update('deletion_insertion_review','text',a,text=b,evidence='Updated by explicit main-reader adjudication; see the corresponding second-box crop and audit decision. The uncertain letters remain uncertain.')
update('notes','id','N03',text='Source grammar is not regularized. The current text retains cette préordre; the noun/agreement in les réunions ... est fermé is now explicitly doubtful, and singular partition is preferred with partitions as an alternative. The initial capital A before quelles has no written accent. The identity-map explanation still has no closing parenthesis after NB2. No missing word or punctuation has been supplied.')
E['report_appends'].setdefault('notes',[]).extend([
 dict(id='N10',text='Blind-audit findings: distinguish the unaccented baseline ordonne and left definition label def from separately accented occurrences. The terminal NB1 mark is a dash. The finite-case explanation has a closing parenthesis but no secure opening one. Final finie in the explanation of local finiteness is written with a small e. New uncertainties that preserve the preferred C reading are recorded as doubts, not new primary corrections.'),
 dict(id='N11',text='Audit scope limitation: neutral box B18 contains the already-transcribed I→X but misses the paragraph rule. The main reader inspected saved original crop P17, which includes both. The separator is retained on that independent visual evidence; the fixed second reading has not been altered or represented as having read the missing rule.'),
 dict(id='N12',text='The lower indexing clause is raised and independently underlined above a separate heavy cancellation. The low group beneath it favors qui filtre, with tels que retained as an alternative. The nearby telle que after disjoints et follows the rising baseline in the wider image; it is not asserted to be a separate insertion.')])
E['report_appends'].setdefault('abbreviations',[]).append(dict(form='équiv. (doubtful)',expansion='équivaut; abbreviation preferred from the terminal point, expanded form retained only as an alternative'))

source=(W/'pages'/f'{page}.tex').read_text()
for x in E['source_replacements']:
    assert source.count(x['old'])==1,x
    source=source.replace(x['old'],x['new'])
assert [d['box'] for d in rows]==[x['box'] for x in C.values() if not x['token_equal']]
assert not (W/'second'/f'{page}_root_decisions.json').exists()
subprocess.run([sys.executable,str(W/'scripts'/'append_root_decisions.py'),page],input=json.dumps(rows,ensure_ascii=False),text=True,check=True)
(W/'second'/f'{page}_edits.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'decisions;',sum(d['decision']=='revise' for d in rows),'revised boxes;',len(E['source_replacements']),'source edits')
